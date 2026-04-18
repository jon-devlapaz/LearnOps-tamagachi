---
title: "Drill & Graph Engineering (implementation invariants)"
type: source
updated: 2026-04-17
sources: []
related: [product-doc-progressive-disclosure.md, product-doc-evidence-weighted-map.md, product-doc-spec.md]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/drill/engineering.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Drill & Graph Engineering (implementation invariants)

## Summary

`docs/drill/engineering.md` defines the hard engineering rules for keeping drill behavior, graph state, and persisted learner state in sync. Graph state is the persisted, machine-checkable projection of evidence Socratink has seen. Only spaced reconstruction may mutate graph truth to `solidified`.

Five core invariants: (1) **One Active Node At A Time** — highlighted node, active drill target, backend evaluation, persisted result must all refer to the same `node_id`. (2) **Derived Graph State** — Cytoscape is projection layer, not system of record; persist into `concept.graphData` first, derive graph from data. (3) **Patch by `node_id`, Never Position** — extraction ordering not guaranteed stable. (4) **Derived Cluster State** — clusters are containers in MVP; state derived from subnodes. (5) **Unlocking Must Match Product Truth** — distinguish traversal unlock (open after engagement, e.g., backbone `primed` opens cluster), adjacent cluster traversal (every prerequisite child room genuinely worked), and mastery unlock (only on genuine `solidified`).

Four-state mutation table: cold attempt complete → `locked → primed`; study complete → no state change but `re_drill_eligible_after = now + 5m`; re-drill solid → `primed`/`drilled → solidified`; re-drill non-solid → `primed → drilled`.

Prohibited mutations: no graph mutation on `PROBE` or `SCAFFOLD`; no graph mutation/interleaving credit/mastery unlock from Repair Reps; no `locked → solidified`; no scoring of cold attempts; no re-drill if `re_drill_eligible_after` is in the future.

Pre-change checklist (8 items) verifies one active node identified, backend evaluates same node, only that node patched, non-solid does not masquerade as mastery, derived cluster state matches subnode truth, CTAs match routing layer, graph re-render preserves persisted state, local matches hosted Vercel behavior.

## Raw Artifacts
- `../../../docs/drill/engineering.md`

## Connections
- Implementation: [Progressive Disclosure](product-doc-progressive-disclosure.md)
- Doctrine override: [Evidence-Weighted Map](product-doc-evidence-weighted-map.md)
- Binding contract: [Product Spec](product-doc-spec.md)
- Eval set: [Drill Evaluation](product-doc-drill-evaluation.md)
