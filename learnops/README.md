# LearnOps

A neurocognitive learning pipeline built as [Agent Skills](https://agentskills.io/) for Claude. LearnOps converts raw information (transcripts, articles, lectures) into durable knowledge through a four-stage process grounded in cognitive science.

## The Pipeline

```
Raw Text → [Extract] → [Present] → [Drill] → [Consolidate]
              Stage 1      Stage 2     Stage 3     Stage 4
```

**Stage 1 — Extract** (`learnops-extract`): Recovers the causal architecture beneath a text. Produces a structured knowledge map with mechanism-level claims, not topic labels. Prevents the "Bird-Naming Fallacy" — knowing what something is called without understanding how it works.

**Stage 2 — Present** (`learnops-present`): Renders a knowledge map as a navigable single-file HTML dashboard. Enforces Mayer's Segmenting Principle (single-section visibility) to build a spatial mental model before drilling. This is the last passive exposure before active recall.

**Stage 3 — Drill** (`learnops-drill`): Socratic stress-testing of the learner's understanding, node by node. Forces attempted recall before any correction (the Generation Effect). Classifies failures as Shallow, Deep, or Misconception and applies matched remediation. Produces a structured handoff payload for Stage 4.

**Stage 4 — Consolidate** *(not yet built)*: Sleep-gated verification. After ≥24 hours, tests whether repairs from Stage 3 survived consolidation. The spacing law is a biological constraint — knowledge repaired in Stage 3 is still too accessible for a valid retention test.

## Why This Architecture

Each stage exists because of a specific neurocognitive requirement:

- **Extraction before presentation**: The brain stores causal networks, not topic lists. Forcing mechanism-level syntax at extraction ensures the map is drillable downstream.
- **Presentation before drilling**: Cognitive load must be managed. The dashboard provides a segmented, navigable surface — not an information dump — so the learner builds spatial familiarity before high-friction recall.
- **Drilling before consolidation**: The hippocampus requires a prediction error signal (attempted recall → failure → correction) to encode effectively. Passive re-reading doesn't generate this signal.
- **24-hour spacing before verification**: Synaptic consolidation requires sleep. Testing immediately after repair measures accessibility, not durability.

## Installation

Each skill is a self-contained directory following the [Agent Skills specification](https://agentskills.io/specification). Install individually or as a set.

### Claude.ai (Custom Skills)

Zip and upload individual skill directories via **Settings → Features → Custom Skills**.

### Claude Code

```bash
# Copy to your project's skills directory
cp -r skills/learnops-extract .claude/skills/
cp -r skills/learnops-present .claude/skills/
cp -r skills/learnops-drill .claude/skills/
```

### Any Agent Skills-compatible platform

The skills use the open Agent Skills format (SKILL.md + references/). Consult your platform's documentation for the skill installation path.

## Tools

`tools/get_transcript.py` — A CLI utility that fetches YouTube transcripts and saves them as text files. This is the input funnel for Stage 1.

```bash
# Requires: youtube-transcript-api, yt-dlp, pyperclip, rich
pip install youtube-transcript-api yt-dlp pyperclip rich

python tools/get_transcript.py "https://youtube.com/watch?v=..."
```

## Repo Structure

```
learnops/
├── skills/
│   ├── learnops-extract/       # Stage 1: Knowledge extraction
│   │   ├── SKILL.md
│   │   └── references/
│   ├── learnops-present/       # Stage 2: Dashboard presentation
│   │   ├── SKILL.md
│   │   └── references/
│   └── learnops-drill/         # Stage 3: Socratic gap detection
│       ├── SKILL.md
│       └── references/
├── tools/
│   └── get_transcript.py       # YouTube transcript fetcher
├── LICENSE                     # Apache-2.0
└── README.md
```

## Status

This is an active build. Stage 4 (consolidation verification) is designed but not yet implemented. The three built stages are functional and tested against live content.

## License

Apache-2.0. See [LICENSE](LICENSE).
