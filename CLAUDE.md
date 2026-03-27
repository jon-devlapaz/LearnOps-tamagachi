# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**LearnOps Tamagachi** is an interactive prototype demonstrating a neurocognitive learning pipeline. The concept: raw information enters a three-stage lifecycle (Ingest → Drill → Consolidate) modeled as a living ecosystem that grows or hibernates based on learner performance.

The UI maps internal JS state names to visual indicators (colored `.concept-dot` elements in the sidebar list, plus dark mode for `hibernating`):
- `growing` — active/structurally sound
- `fractured` — misconception detected, needs repair
- `hibernating` — consolidating; triggers `body.night` dark mode
- `actualized` — consolidated/mastered

> Note: `instantiated` still exists in the state machine for backward compatibility with old localStorage data, but new concepts are never created in that state.

## Running the Project

No build step. Serve locally (required for AI extraction — `fetch()` calls fail over `file://`):

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Architecture

The app is pure vanilla HTML/CSS/JavaScript with no build step and no frameworks. The structure across files:

| File | Role |
|------|------|
| `index.html` | Shell: HTML structure + script/style tags |
| `styles.css` | All CSS (12 numbered sections) |
| `app.js` | Main `App` IIFE — all UI logic, state machine, data store |
| `graph.js` | `GraphEngine` (canvas force-directed graph) + `performAIExtraction()` |
| `ai_service.js` | `AIService.generateKnowledgeMap()` — full knowledge map via Gemini API |
| `file_system.js` | `FileSystem` module — Web File System Access API + IndexedDB handle persistence |

**Script load order in `index.html`:** `file_system.js` → `ai_service.js` → `app.js` → `graph.js`

**Key patterns in `app.js`:**
- **`setState(state)`** — central function that drives all UI transitions; calls `applyControlsForState()` at its end — this is the *only* place controls are updated (no manual `showControls`/`setButtons` calls elsewhere)
- **`applyControlsForState(state, concept)`** — owns all button visibility/enabled state for a given state
- **`setButtons(extract, drill)`** — two-parameter helper (extract-enabled, drill-enabled); `btn-present` was removed
- **CSS variables** — `--bg`, `--primary`, `--danger`, `--success` etc. for theming; `hibernating` state triggers a dark mode swap via `body.night`
- **24-hour timer** — `setInterval`-based countdown; a hidden dev-skip button (top-right corner, click to reveal) fast-forwards it for demos
- **Drill UI** — `#drill-ui` panel with `#chat-history` / `#chat-input` for chat-style Socratic drilling
- **Data persistence** — `localStorage` keys `learnops_concepts` (array of concept objects) and `learnops_active` (selected concept ID); max 4 concepts
- **Transient content store** — `contentStore = new Map()` (module-level) holds full text keyed by concept ID; does not survive page reload (intentional)

**`app.js` is organized into 16 numbered sections** (see the table of contents comment near line ~25):
1. DOM references
2. Pub/sub `Bus` — lightweight event emitter used for cross-section communication
3. `GEO` — polygon coordinate arrays (5 states × 8 polygons) for the SVG crystal shapes
4. `STATES` — display config (title/desc text per state)
5. Coordinate utilities + easing
6. `MorphEngine` — shared `requestAnimationFrame` loop; morphs polygon coordinates between states
7. Transition animation helpers (`playAnim`)
8. Grid rendering — builds tile + crystal SVG content
9. Data store — `localStorage` CRUD helpers + `_readFile()` shared file-reading helper
10. Drawer UI
11. Concept list render
12. CRUD — `startAddConcept()` (content-first creation form), `renderAddTrigger()`, `deleteConcept()`
13. `setState()` + `applyControlsForState()`
14. Pipeline handlers — `extract()`, `showContentOverlay()`, `hideContentOverlay()`, `drill()`, `drillPass()`, `drillFail()`, `consolidate()`, `completeConsolidation()`, `fastForward()`
15. Timer
16. Init / restore

**`graph.js`** contains two things:
- `GraphEngine` — IIFE; mounts a `<canvas>` inside `#extract-overlay` during extraction; physics-based force-directed layout; call `init()` before streaming nodes/edges, `stop()` on completion
- `performAIExtraction(text, onSuccess, onError, onPhaseChange)` — orchestrates the Gemini streaming call, feeds nodes/edges into `GraphEngine` as they arrive, then hands the parsed knowledge map back via `onSuccess`

**`ai_service.js`** — `AIService.generateKnowledgeMap(rawText, onProgress)` — non-streaming full extraction; fetches the system prompt from `learnops/skills/learnops-extract/extract-system-v1.txt` at call time; returns raw JSON string.

**`file_system.js`** — `FileSystem` module; persists the user-selected staging directory `FileSystemDirectoryHandle` in IndexedDB (`LearnOps_FS_DB` / `handles` store / key `staging_dir_handle`) so it survives page reload; exposes `initDirectoryPicker()`, `writeStagingFile(filename, content)`, `hasDirectorySelected()`, `getDirectoryName()`.

**CSS is organized into 12 numbered sections in `styles.css`:**
1–10. Base styles, layout, grid, crystal, card, buttons, drawer, concept list, states, animations
11. Content overlay (shown when clicking Extract on a legacy `instantiated` concept)
12. Drawer creation form (`.creation-form`, `.creation-name-input`, `.creation-footer`, etc.)

## External Integrations & Configuration

Two settings are required for AI extraction — both configured via the **Settings** panel (sidebar nav → Settings):

| Setting | Storage | Key |
|---------|---------|-----|
| Gemini API key | `localStorage` | `gemini_key` |
| Staging directory handle | IndexedDB | `staging_dir_handle` |

The Gemini model is `gemini-2.5-flash` (constant `GEMINI_MODEL` in `graph.js`). Both `graph.js` and `ai_service.js` read the key via `getGeminiKey()` defined in `graph.js`.

The extraction system prompt is loaded at runtime from `learnops/skills/learnops-extract/extract-system-v1.txt` — this file must be present when serving locally (it's fetched via `fetch('./learnops/...')`). Opening `index.html` directly via `file://` will fail this fetch; use `python3 -m http.server 8000`.

## Content-First Concept Creation

Concepts are created via a form embedded in the drawer (`startAddConcept()`). The form collects content first, name second, and creates the concept directly in `growing` state — bypassing `instantiated` entirely.

**Flow:**
```
Drawer → paste/upload content → type name → "Add Concept →" → concept born in 🌱 growing
```

**`startAddConcept()` form features:**
- Two tabs: **Text** (textarea with cycling placeholder) and **File** (.txt/.md/.pdf upload with drag-and-drop)
- "⌘ Paste from clipboard" button in the Text tab (`navigator.clipboard.readText()` with `execCommand` fallback)
- "Add Concept →" stays disabled until both content and name are provided
- On submit: stores full text in `contentStore`, persists `contentPreview` (first 500 chars) + `contentType` + `contentFilename` to localStorage, creates concept in `growing` state

**`_readFile(file, onSuccess, onError)`** — shared helper used by both `startAddConcept` and `showContentOverlay`:
- Validates extension (.txt/.md/.pdf) and size (≤2MB)
- PDF: ArrayBuffer → BT/ET regex extraction; fallback message if <50 chars extracted
- Text: `FileReader.readAsText()`

## Three-Stage Pipeline

1. **Ingest** (at concept creation) — user provides raw content (paste or file upload); concept is born in `growing` state with content stored
2. **Drill** — Socratic stress-testing; pass keeps `growing`, fail transitions to `fractured` (requires repair before re-drill)
3. **Consolidate** — 24-hour sleep-gated hibernation; timer expires → concept becomes `actualized` 💎

> The "Extract" step (clicking "1. Extract" on a card) still exists as a fallback for legacy `instantiated` concepts in old localStorage data. New concepts never need it.

The biological constraint of hibernation-over-death is intentional: concepts go dormant rather than disappear, reducing shame spirals for learners with executive function variability.

## API Docs — Use chub Before Touching AI Code

This project calls the Gemini API directly via `fetch()` (no SDK). Before editing `graph.js` or `ai_service.js`, fetch current docs with the `chub` CLI to avoid stale API assumptions:

```bash
chub get gemini/genai --lang js        # main Gemini JS reference
chub get gemini/deep-research --lang js # if working on the Extract deep-research flow
```

Common triggers:
- Changing the model constant `GEMINI_MODEL` → verify the model ID is still valid
- Modifying the streaming SSE parsing in `performAIExtraction()` → check streaming API shape
- Adding structured output / response schema enforcement → check `responseSchema` param
- Wiring drill or consolidate stages to an AI backend → fetch docs for whichever API you use

If you discover a gotcha during work (e.g. a streaming quirk, deprecated param), annotate it so future sessions start smarter:
```bash
chub annotate gemini/genai "your note here"
```

## learnops/ Agent Skills

The `learnops/` directory contains Claude Agent Skills for each pipeline stage. Stage 1 (Extract) is partially wired to the UI:

- `learnops/skills/learnops-extract/` — Stage 1. `extract-system-v1.txt` is actively fetched by `ai_service.js` as the Gemini system prompt during extraction. `SKILL.md` and `references/` contain the full cognitive processing pipeline spec.
- `learnops/skills/learnops-drill/` — Stage 3. Standalone skill spec; not yet wired to the UI's drill chat.
- `learnops/skills/learnops-present/` — Stage 2. Standalone skill spec; not yet wired.
- Stage 4 (Consolidate) — designed but not yet built.

`learnops/tools/get_transcript.py` — CLI utility to fetch YouTube transcripts as text files (input for Stage 1). Requires `youtube-transcript-api`, `yt-dlp`, `pyperclip`, `rich`.
