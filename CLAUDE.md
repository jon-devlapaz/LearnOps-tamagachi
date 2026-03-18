# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**LearnOps Tamagachi** is an interactive prototype demonstrating a neurocognitive learning pipeline. The concept: raw information enters a four-stage lifecycle (Extract → Present → Drill → Consolidate) modeled as a living ecosystem that grows or hibernates based on learner performance.

The UI uses emoji-driven states: `🟫` (seed) → `🌱` (extracted) → `🌿` (presented) → `🌳` (drilled/mastered) or `🥀` (needs repair) → `🐛💤` (consolidating) → `💎` (mastered).

## Running the Project

No build step. Open directly in a browser:

```bash
open index.html
# or serve locally
python3 -m http.server 8000
```

## Architecture

The entire application lives in a single file: `index.html`. It is pure vanilla HTML/CSS/JavaScript with no dependencies or frameworks.

**Key patterns in index.html:**
- **`setState(state)`** — central function that drives all UI transitions; all button handlers call this
- **CSS variables** — `--bg-color`, `--primary`, `--danger`, `--success` etc. for theming; consolidation phase triggers a dark mode swap
- **24-hour timer** — `setInterval`-based countdown; a hidden dev-skip button (top-right corner, click to reveal) fast-forwards it for demos
- **Drill simulation** — Pass/Fail buttons branch to growth (`🌳`) or wilt (`🥀`) states

## Four-Stage Pipeline (from README)

1. **Extract** — recovers causal architecture from raw text → "Knowledge Seed"
2. **Present** — renders as navigable single-file HTML dashboard → "Segmented Habitat"
3. **Drill** — Socratic stress-testing; pass strengthens, fail wilts and requires repair
4. **Consolidate** — 24-hour sleep-gated hibernation enforcing synaptic consolidation (Stage 4 marked as "pending" in README)

The biological constraint of hibernation-over-death is intentional: concepts go dormant rather than disappear, reducing shame spirals for learners with executive function variability.

## Integration Roadmap (per README)

The prototype is a UI demo. The intended production system uses Claude Agent Skills for each stage — extraction, presentation, drilling, and consolidation — none of which are wired up yet.
