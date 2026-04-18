---
title: "Repair Reps Self-Rating Spec (implementation)"
type: source
updated: 2026-04-17
sources: []
related: [product-doc-repair-reps-card-stack.md, product-doc-repair-reps-focused-mode.md, product-doc-spec.md]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/product/repair-reps-self-rating-spec.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Repair Reps Self-Rating Spec (implementation)

## Summary

`docs/product/repair-reps-self-rating-spec.md` is the spec for adding a learner self-rating step to the Repair Reps reveal flow. After the target bridge is shown, the learner rates their own reconstruction (`close_match` / `partial` / `missed`) before advancing. Ratings store in repair evidence and surface on the completion screen as a per-rep breakdown.

Hard invariants: self-ratings are learner-assigned, never AI-scored — no LLM call per rep. Ratings must NOT use mastery language ("you mastered this", "correct", "score"). No graph mutation, no `patchActiveConceptDrillOutcome()`, no `recordInterleavingEvent()`. Completion screen shows rep-kind breakdown but no aggregate score or percentage.

Adds two fields to `repairRepsState`: `ratings` array (one per rep) and `ratingSelected` boolean (resets per rep). Adds `rateRepairRep(rating)` function exported on `SocratinkApp`. Modifies `nextRepairRep()` to gate advance on `ratingSelected === true`. Modifies `recordRepairRepsCompletion()` to store ratings in `learnops_repair_reps_v1`.

Three rating options: `close_match` ("The causal link I typed captures the bridge"), `partial` ("I got part of the chain but missed a step"), `missed` ("My answer didn't capture the causal bridge"). No default selection — learner must actively choose.

Rep-kind labels for completion summary: `missing_bridge` → "Bridge", `next_step` → "Next Step", `cause_effect` → "Cause → Effect".

## Raw Artifacts
- `../../../docs/product/repair-reps-self-rating-spec.md`

## Connections
- Sibling specs: [Repair Reps Card Stack](product-doc-repair-reps-card-stack.md), [Repair Reps Focused Mode](product-doc-repair-reps-focused-mode.md)
- Binding contract: [Product Spec](product-doc-spec.md)
- Triple-spec consolidation candidate: [Doc Map](product-doc-doc-map.md)
