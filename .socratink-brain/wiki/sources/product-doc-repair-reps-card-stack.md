---
title: "Repair Reps Card-Stack Spec (implementation)"
type: source
updated: 2026-04-17
sources: []
related: [product-doc-repair-reps-focused-mode.md, product-doc-repair-reps-self-rating.md, product-doc-spec.md]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/product/repair-reps-card-stack-spec.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Repair Reps Card-Stack Spec (implementation)

## Summary

`docs/product/repair-reps-card-stack-spec.md` is the visual-only spec for making the Repair Reps UI feel like a physical card deck rather than a panel view. Cards deal in (slide-up + fade), flip on reveal (vertical unfold), and stack on completion (gentle scale-in). The mechanical metaphor distinguishes Repair Reps from drill mode (drill = conversation, repair = cards).

Hard constraints: all animations respect `prefers-reduced-motion: reduce`; no layout shifts that move interactive elements after they are visible; transitions complete within 400ms; do not reuse the solidified celebration animations (`graphSolidSnap`, `graphSolidGlow`, `graphSolidInk`) — those belong to mastery, repair gets its own vocabulary.

Includes three keyframe specs (`repairDeal` 280ms, `repairReveal` 320ms, `repairSettle` 360ms), three-dot progress indicator markup, readonly textarea after reveal pattern, and complete-state wrapper rules. No JS logic changes, no state shape changes, no API changes — visual layer only.

Files touched: `public/js/graph-view.js` for markup, `public/css/layout.css` for animations.

## Raw Artifacts
- `../../../docs/product/repair-reps-card-stack-spec.md`

## Connections
- Sibling specs: [Repair Reps Focused Mode](product-doc-repair-reps-focused-mode.md), [Repair Reps Self-Rating](product-doc-repair-reps-self-rating.md)
- Binding contract: [Product Spec](product-doc-spec.md)
- Triple-spec consolidation candidate: [Doc Map](product-doc-doc-map.md)
