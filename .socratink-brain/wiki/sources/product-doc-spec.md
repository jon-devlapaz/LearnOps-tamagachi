---
title: "Product Spec (canonical)"
type: source
updated: 2026-04-17
sources: []
related: [../doctrine/, ../mechanisms/, ../records/]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/product/spec.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Product Spec (canonical)

## Summary

`docs/product/spec.md` is the binding design and implementation contract for Socratink. It defines product philosophy, cognitive architecture, the four-state model (`locked → primed → drilled → solidified`), the three-phase loop (cold attempt → targeted study → spaced re-drill), the seven side-panel modes, traversal/routing, session guardrails, and a 7-question evaluation checklist that gates any new feature.

Core thesis: the enemy is the *illusion of competence*. The product rewards reconstruction, not exposure. Generation Before Recognition is non-negotiable. Cold attempts are explicitly unscored. Only spaced re-drill with a `solid` classification can produce `solidified` — `solidified` is an evidence record, not a mastery claim about the learner.

The unifying principle is **metacognitive UX**: every surface is designed for the learner's awareness of their own cognitive process, not just the content. Cold Attempt reveals the shape of what is unknown; Targeted Study anchors correction to the prediction error just generated; the Spacing Block teaches that the "feeling of knowing" is a cognitive illusion; Trajectory Contrast updates beliefs about productive struggle; the Graph shows what Socratink has evidence for — not what the learner knows.

Read alongside `evidence-weighted-map.md`, which controls when wording could imply the graph shows what the learner knows.

## Raw Artifacts
- `../../../docs/product/spec.md` (live canonical doc — not copied into raw/)

## Connections
- Doctrine override: [Evidence-Weighted Map Doctrine](product-doc-evidence-weighted-map.md)
- Implementation: [Progressive Disclosure](product-doc-progressive-disclosure.md), [Drill Engineering](product-doc-drill-engineering.md)
- UX: [UX Framework](product-doc-ux-framework.md), [Post-Drill UX Spec](product-doc-post-drill-ux-spec.md)
