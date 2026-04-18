---
title: "MVP Happy Path (release-gate)"
type: source
updated: 2026-04-17
sources: []
related: [product-doc-project-state.md, product-doc-project-operations.md, product-doc-drill-engineering.md, product-doc-drill-evaluation.md]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/project/mvp-happy-path.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# MVP Happy Path (release-gate)

## Summary

`docs/project/mvp-happy-path.md` is the narrow manual release gate for Socratink. Used to decide if the current branch is healthy enough to merge, run a manual smoke test, or define what "working loop" means for MVP.

Release gate: thermostat starter map supports this loop without obvious breaks: (1) Core Thesis cold attempt, (2) Core Thesis study and return to map, (3) Backbone cold attempt, (4) Backbone study unlocks the cluster, (5) Cluster exposes child drill rooms, (6) Child cold attempt resolves cleanly, (7) Original node can later re-drill after spacing/interleaving, (8) Graph truthfully ends in `drilled` or `solidified`.

Manual test flow: `uvicorn main:app --reload` → open `localhost:8000` → configure Gemini API key → open Thermostat Control Loop → cold attempt on Core Thesis → return from study → cold attempt on Backbone → enter Cluster → cold attempt on child room → re-drill readiness check.

Go criteria: no graph crash; no CTA offers impossible action; no stale drill panel after returning to map; no cold attempt leaks score/classification; graph and side panel agree on node truth; cluster unlock and child-room selection work.

No-go: wrong node patched; graph stale after successful transition; node jumps `locked` straight to `drilled`/`solidified`; re-drill offered before spacing satisfied; cluster opens but child rooms cannot be selected.

Evidence to capture per serious test run: `logs/drill-runs.jsonl`, transcript logs, screenshots for UI contradictions, short note on what felt false or blocked.

## Raw Artifacts
- `../../../docs/project/mvp-happy-path.md`

## Connections
- Release gates: [Project State](product-doc-project-state.md), [Operations](product-doc-project-operations.md)
- Engineering: [Drill Engineering](product-doc-drill-engineering.md), [Drill Evaluation](product-doc-drill-evaluation.md)
