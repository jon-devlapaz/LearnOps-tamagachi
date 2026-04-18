---
title: "Feedback After Failure Is a Required Scaffold"
type: synthesis
updated: 2026-04-17
sources: [../sources/research-note-testing-effect.md, ../sources/research-note-spacing-effect.md, ../sources/research-note-generation-effect.md]
related: [../concepts/testing-effect.md, ../concepts/spacing-effect.md, ../concepts/generation-effect.md, ../doctrine/]
basis: inferred
workflow_status: open
flags: [open-question]
confidence: high
---

# Feedback After Failure Is a Required Scaffold

## Pattern

Three independent learning-science literatures — the testing effect, the spacing effect, and the generation effect — converge on the same single moderator: **feedback after a failed attempt is what separates productive struggle from harmful error encoding**.

This is not a soft "feedback is nice." It is a load-bearing scaffold. Without it:

- The testing effect collapses on failed retrievals (Rowland 2014: g≈0.39 without feedback vs. g≈0.73 with).
- The generation effect on novel material disappears (McElroy & Slamecka 1982; Hays-Kornell-Bjork 2013).
- Errorful generation may *intrude*, becoming worse than restudy (Potts & Shanks 2014, 2019).
- The spacing effect on long lags inverts when the second-episode retrieval fails without correction.

The mechanism is the same across all three: a failed attempt without feedback either does nothing (no semantic activation, no trace strengthening) or actively encodes the error.

## Evidence

- [Testing Effect Concept](../concepts/testing-effect.md) — Rowland 2014 meta-analysis quantifies the moderator at the highest confidence in this set.
- [Generation Effect Concept](../concepts/generation-effect.md) — Potts & Shanks 2014, 2019 directly demonstrate error intrusion when feedback is withheld.
- [Spacing Effect Concept](../concepts/spacing-effect.md) — Pyc & Rawson 2009 retrieval-effort hypothesis: *successful effortful* retrieval is what matters; failed retrievals at long lags can hurt without correction.
- Convergent third-party support: Metcalfe (2017) hypercorrection finding — high-confidence errors are corrected *more* reliably with feedback, suggesting feedback is not just damage-control but actively converts wrong attempts into stronger learning than passive study would have produced.

## Inference

For Socratink, this pattern collapses three boundary conditions into one product invariant: **the cold attempt → targeted study transition cannot be skipped or weakened**. The cold attempt is unscored on purpose, and that decision is well-justified — but the unscored design only works because the immediately-following corrective exposure is what discharges the boundary condition for *all three* mechanisms simultaneously.

This means abandonment after a failed cold attempt is the dominant product risk to truthful learning. It is more dangerous than a wrong cold attempt, because:

- The wrong attempt with feedback is an asset (hypercorrection, generation effect with corrective exposure, pretesting potentiation).
- The wrong attempt without feedback is a liability (error intrusion, no testing-effect benefit, no spacing benefit, no generation benefit).

The current product implicitly assumes learners always proceed through study after the cold attempt. The literature suggests that assumption is the load-bearing one.

## Product Implication

- **Treat cold-attempt → targeted-study completion rate as a release-gate metric.** It is not a UX nicety; it is the empirical condition under which the entire learning model operates as advertised.
- **The "Generation Before Recognition" doctrine implicitly depends on a "Feedback Before Departure" companion invariant.** Surface this in the spec.
- **Consider blocking session-end or graph progression on un-discharged cold attempts** — at minimum, instrument abandonment so the rate is visible.
- **Instrumentation gap:** Socratink does not currently log whether the post-cold-attempt study material was actually consumed (vs. skipped, vs. abandoned). This is the highest-value missing measurement implied by the convergent literature.
- **`re_drill_band` interpretation:** a band that increments after failed re-drills with no intervening corrective exposure is reporting noise, not progress.

## Open Question

The cleanest empirical test would be: among learners with similar cold-attempt accuracy, compare 7-day retention across (a) those who completed targeted study before leaving the session and (b) those who abandoned. If the literature is right, group (a) should massively outperform — and group (b) should sometimes do *worse* than no cold attempt at all (error intrusion). This is a falsifiable claim about Socratink's own loop and is the right next experiment.
