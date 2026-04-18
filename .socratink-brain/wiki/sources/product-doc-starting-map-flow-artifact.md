---
title: "Starting Map Flow Artifact (design storyboard, non-binding)"
type: source
updated: 2026-04-17
sources: []
related: [product-doc-evidence-weighted-map.md, product-doc-spec.md]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/product/starting-map-flow-artifact.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Starting Map Flow Artifact (design storyboard, non-binding)

## Summary

`docs/product/starting-map-flow-artifact.md` is a lightweight design storyboard for the metacognitive happy path before implementation. Not the binding implementation spec — operational rules live in `evidence-weighted-map.md`. Marked `binding: no` in the doc registry.

Product framing: the concept page should not be where the learner goes to read; it should be where their understanding becomes inspectable. Socratink should ask for the learner's starting map before showing explanatory content. The starting map is an **anchor, not a diagnostic** — it can shape routing and repair, but must not create mastery claims.

Storyboards seven screens: (1) Concept Threshold (capture starting map, no graph mutation), (2) Provisional Graph (draft path, no mutation), (3) First Cold Attempt (local question derived from threshold; mutation only on substantive attempt), (4) Locked Study Silhouette (intentional absence of mechanism content), (5) Study Repair Artifact (attempt-scoped, with hinge correction + causal spine + diagram), (6) Interleaving Bridge (2-3 nearby room choices, not whole graph), (7) Accumulating Repair History (personal metacognitive field journal).

Friction fixes the flow must avoid: generation fatigue (threshold and first cold attempt cannot ask the same question twice), zero-signal frustration (analogical fallback for low-vocabulary learners), interleaving whiplash (short bridge explaining why the learner is leaving the node).

Includes a Truth Table mapping each moment to allowed state changes — only substantive cold attempt mutates `locked → primed`; only spaced re-drill mutates to `solidified`.

## Raw Artifacts
- `../../../docs/product/starting-map-flow-artifact.md`

## Connections
- Operationalized doctrine: [Evidence-Weighted Map Doctrine](product-doc-evidence-weighted-map.md)
- Binding contract: [Product Spec](product-doc-spec.md)
- Future-canonical candidate per Doc Map: should become `starting-map.md` once threshold flow is built
