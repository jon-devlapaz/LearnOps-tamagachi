---
title: "Operations & Stabilization (release-gate)"
type: source
updated: 2026-04-17
sources: []
related: [product-doc-project-state.md, product-doc-mvp-happy-path.md]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/project/operations.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Operations & Stabilization (release-gate)

## Summary

`docs/project/operations.md` defines the release discipline for the current Socratink MVP. Do not expand scope until the narrow thermostat loop is healthy on hosted and local.

Minimum acceptable loop: cold attempt → study → interleave on another room → spaced re-drill → truthful graph update.

Six release checks before merging to `main`: (1) loop integrity per `mvp-happy-path.md`, (2) truthful state — only valid transitions, (3) graph stability — no UI crash/stale panel/wrong-node patch, (4) hosted caution — local success is not final if Vercel could diverge, (5) error handling — external/API failures don't leak internals to learner, (6) evidence captured in Socratink Brain KB or explicitly noted as missing coverage.

Current evidence policy: branch-local. Live findings, open issues, shipping syntheses, instrumentation gaps. Supporting evidence in `logs/drill-runs.jsonl`, transcript logs, exported Vercel runtime logs from Socratink Brain-marked drill events, screenshots for visible contradictions, short merge note. **If evidence is missing, say so explicitly instead of writing confident prose around it.**

For hosted drill-conversation capture: `/api/drill` emits structured `socratink_event` runtime log events. Summary capture default-on. Full transcript capture requires `SOCRATINK_CAPTURE_DRILL_TRANSCRIPTS=true` in Vercel + `scripts/eval-pull` export.

Active decisions log includes: 2026-04-08 ship narrow truthful loop first; 2026-04-05 three-phase node loop is MVP architecture.

Near-term engineering priorities: keep drill/panel/graph state aligned; keep CTA logic and allowed actions aligned; improve transcript/replay coverage without blocking narrow gate; harden hosted fallbacks for external ingestion; reduce `app.js` state entanglement after loop is stable.

## Raw Artifacts
- `../../../docs/project/operations.md`

## Connections
- Release gates: [Project State](product-doc-project-state.md), [MVP Happy Path](product-doc-mvp-happy-path.md)
