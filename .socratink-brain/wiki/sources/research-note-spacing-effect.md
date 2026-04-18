---
title: "Spacing Effect Research Note"
type: source
updated: 2026-04-17
sources: []
related: [../concepts/spacing-effect.md, ../syntheses/feedback-after-failure-required-scaffold.md]
basis: sourced
workflow_status: active
flags: []
source_kind: research-note
raw_artifacts: [raw/research-notes/2026-04-17-spacing-effect-distributed-practice.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Spacing Effect Research Note

## Summary

This source is a 2026-04-17 deep research note on the spacing effect / distributed practice, anchored in the Cepeda et al. (2006) meta-analysis (839 effect sizes across 317 experiments) and Cepeda et al. (2008) which established the "temporal ridgeline" of optimal interstudy interval as a function of retention interval (~20–40% ratio at 1-week RI, dropping to ~5–10% at 1-year RI).

The note's central tension for Socratink concerns the **expanding vs. uniform schedule debate**. Karpicke & Roediger (2007) is the strongest counter to SuperMemo/Anki-style aggressive expansion: expanding wins on immediate tests but uniform spacing beats expanding at 2-day delays. Storm, Bjork & Storm (2010) partially rebut, showing context-dependent results. The literature does not unambiguously support expanding for long retention; the note recommends quasi-uniform with a slight expanding tail (e.g., 1d → 4d → 10d → 21d) as the safest MVP prior.

The note is sharp on Socratink's current ad hoc spacing: re-drills within a single session are *massed*, not spaced, and `solidified` would be epistemically fraudulent in that case. It proposes a falsifiable operational definition of `solidified`: ≥3 successful re-drills, across ≥2 calendar days, with the final success at ≥7-day gap. It also proposes that `re_drill_band` should encode the *gap that produced the success*, not just an ordinal rank.

The note documents required instrumentation that is not yet present: per-drill `timestamp_utc`, `gap_since_prior_drill_hours`, `retrieval_success`, and a 7d/30d retention probe on a sample of solidified nodes — the only direct evidence the spacing mechanism is actually operating in the app.

Important uncertainty: most spacing literature is on flashcards and short passages. Optimal intervals for Socratic conversational drill are not directly studied; the recommended schedule is a *prior*, not a settled answer.

## Raw Artifacts
- `raw/research-notes/2026-04-17-spacing-effect-distributed-practice.md`

## Connections
- Concept page: [Spacing Effect](../concepts/spacing-effect.md)
- Synthesis: [Feedback After Failure Is Required Scaffold](../syntheses/feedback-after-failure-required-scaffold.md)
- Related concept: [Desirable Difficulty](../concepts/desirable-difficulty.md)
