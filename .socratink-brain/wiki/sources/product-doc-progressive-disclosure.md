---
title: "Progressive Disclosure (implementation)"
type: source
updated: 2026-04-17
sources: []
related: [product-doc-spec.md, product-doc-evidence-weighted-map.md, product-doc-drill-engineering.md]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/product/progressive-disclosure.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Progressive Disclosure (implementation)

## Summary

`docs/product/progressive-disclosure.md` is the implementation-facing product spec for how the graph, drill system, and learner progression work together. It is the document an engineer reads before touching state, routing, persistence, or graph rendering code.

Defines the four-state model with explicit valid transitions (`locked → primed → drilled → solidified`) and explicit invalid transitions to never allow (`locked → drilled`, `locked → solidified`, `primed → solidified` without spacing, `solidified → drilled` regression). Lists persisted drill fields: `drill_status`, `drill_phase`, `gap_type`, `gap_description`, `last_drilled`, `cold_attempt_at`, `study_completed_at`, `re_drill_eligible_after`. Defines drill contract response fields and the classification sufficiency rubric (causal chain not vocabulary; spacing satisfied; self-generated not AI-walked).

Specifies routing rules: PROBE/SCAFFOLD never mutate graph state; NEXT with solid mutates to `solidified` and triggers strongest celebration; NEXT with non-solid mutates to `drilled` and triggers no celebration; SESSION_COMPLETE frames as save point.

Progression layers: core thesis is starting room; backbone independently unlocks dependent clusters; clusters are containers (state derived from subnodes), not primary drill targets; subnodes are the main drill units. Per-node retrieval ceiling: 3 successful retrievals per session.

Source-of-truth invariant: the knowledge map is the system of record. Drill outcomes write into `concept.graphData`; the graph derives from that data — never the reverse.

## Raw Artifacts
- `../../../docs/product/progressive-disclosure.md`

## Connections
- Binding contract: [Product Spec](product-doc-spec.md)
- Doctrine override: [Evidence-Weighted Map Doctrine](product-doc-evidence-weighted-map.md)
- Engineering invariants: [Drill Engineering](product-doc-drill-engineering.md)
- Post-phase UX: [Post-Drill UX Spec](product-doc-post-drill-ux-spec.md)
