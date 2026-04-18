---
title: "Post-Drill UX Spec (implementation)"
type: source
updated: 2026-04-17
sources: []
related: [product-doc-spec.md, product-doc-evidence-weighted-map.md, product-doc-progressive-disclosure.md]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/product/post-drill-ux-spec.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Post-Drill UX Spec (implementation)

## Summary

`docs/product/post-drill-ux-spec.md` is the binding implementation spec for what the learner sees after each phase of the three-phase loop resolves. It governs panel copy, result-state visual treatment, sensory feedback, transcript visibility, tier/band trajectory display, and the handoff from drill mode back to graph navigation.

Five canonical result states must look and feel distinct: **Primed** (cold attempt complete; subtle warm acknowledgment; required normalization message; no score), **Solidified** (solid spaced reconstruction recorded; strongest sensory celebration calibrated to cognitive load; trajectory contrast shown as evidence delta), **Unresolved Exit** (non-solid spaced reconstruction recorded; `Needs revisit` headline; no celebration; wise feedback framing strategy not ability), **In-Progress Drill** (no result framing yet), **Session Complete** (save-point framing; never end on failure state).

Six side-panel modes must be pure with no content bleed. Tier/band display rules: never during active drill; always after re-drill resolves; always with interpretive framing; band describes one attempt, not mastery — `chain` is not `solid`. Anti-patterns explicitly listed: cold-attempt result screens with scores, `drilled` nodes that read like completion, classifier jargon exposed as user-facing, celebration on unresolved outcomes, ability-framed copy on non-solid results.

Per the parent doctrine override, "Solidified", "Needs revisit", and "Cleared" are display shorthand for what Socratink has recorded — not claims about the learner's mind.

## Raw Artifacts
- `../../../docs/product/post-drill-ux-spec.md`

## Connections
- Doctrine override: [Evidence-Weighted Map Doctrine](product-doc-evidence-weighted-map.md)
- Binding contract: [Product Spec](product-doc-spec.md)
- Implementation: [Progressive Disclosure](product-doc-progressive-disclosure.md)
