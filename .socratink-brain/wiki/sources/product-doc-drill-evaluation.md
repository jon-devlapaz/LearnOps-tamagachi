---
title: "Drill & Graph Evaluation (manual eval set)"
type: source
updated: 2026-04-17
sources: []
related: [product-doc-drill-engineering.md, product-doc-mvp-happy-path.md]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/drill/evaluation.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Drill & Graph Evaluation (manual eval set)

## Summary

`docs/drill/evaluation.md` defines the smallest useful evaluation set for the current MVP loop. Use the Thermostat Control Loop starter map unless the task specifically targets extraction or ingestion.

Four manual evals: (1) Core Thesis Cold Attempt — verify unscored cold attempt → `primed` → study, with strong sample answer about thermostat compares + heater triggers; (2) Backbone Unlock Path — verify next branch can be traversed, sample answer about feedback control as measure/compare/act; (3) Child Room Cold Attempt — verify drillability inside cluster, e.g., Temperature Comparison or Call For Heat; (4) Spaced Re-Drill Truth — verify earlier room cannot be re-drilled too early and can later resolve truthfully.

Answer modes table maps turn types to expected routing: explicit unknown → SCAFFOLD; shallow attempt → PROBE; partial causal attempt → PROBE; solid attempt → NEXT. Each row gives a sample answer for the thermostat domain.

Obvious-break checklist for an unhealthy build: stale drill transcript after returning to map; graph highlights one node while backend evaluates another; cluster opens but child rooms cannot be selected; cold attempt shows score or classification; graph state contradicts what just happened; node reaches `solidified` from non-solid path.

Evidence capture after meaningful eval: `logs/drill-runs.jsonl`, transcript logs, screenshots of visual contradictions, short note on what broke or felt truthful.

## Raw Artifacts
- `../../../docs/drill/evaluation.md`

## Connections
- Engineering invariants: [Drill Engineering](product-doc-drill-engineering.md)
- Release gate: [MVP Happy Path](product-doc-mvp-happy-path.md)
