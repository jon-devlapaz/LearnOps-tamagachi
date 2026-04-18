---
title: "Repair Reps Focused Mode Spec (implementation)"
type: source
updated: 2026-04-17
sources: []
related: [product-doc-repair-reps-card-stack.md, product-doc-repair-reps-self-rating.md, product-doc-spec.md]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/product/repair-reps-focused-mode-spec.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Repair Reps Focused Mode Spec (implementation)

## Summary

`docs/product/repair-reps-focused-mode-spec.md` is the focused-workbench spec for Repair Reps: the graph/detail layout while `interactionMode === "repair-reps"`, the context strip ("Node label - Repair Rep 1 of 3 - Practice only"), the input/reveal copy contract ("Your bridge", "Show reference bridge", "Reference bridge", "Compare the link, not the wording."), and the completion copy ("Practice logged", "These reps are saved. Graph progress comes from the next re-drill.").

Hard invariants: Repair Reps must NEVER call `patchActiveConceptDrillOutcome()`, `recordInterleavingEvent()`, or `markNodeVisitedThisSession()`. Repair Reps must not mutate `drill_status`, `drill_phase`, `study_completed_at`, `re_drill_eligible_after`, `gap_type`, or `gap_description`. The reference bridge renders only after the learner types and clicks reveal. Graph interactivity during focused Repair Reps controlled by CSS class state, not JS pointerEvents mutation. Copy avoids score, correct, mastered, streak, win, or celebration language.

Defines focused-mode CSS layout (graph de-emphasized to opacity 0.34, non-interactive), responsive collapse to single column on mobile (graph hidden), and reduced-motion overrides.

Frontend rendering and copy only — no backend changes, no API changes, no prompt changes.

## Raw Artifacts
- `../../../docs/product/repair-reps-focused-mode-spec.md`

## Connections
- Sibling specs: [Repair Reps Card Stack](product-doc-repair-reps-card-stack.md), [Repair Reps Self-Rating](product-doc-repair-reps-self-rating.md)
- Binding contract: [Product Spec](product-doc-spec.md)
- Triple-spec consolidation candidate: [Doc Map](product-doc-doc-map.md)
