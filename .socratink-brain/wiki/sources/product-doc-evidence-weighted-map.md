---
title: "Evidence-Weighted Map Doctrine (canonical, overrides)"
type: source
updated: 2026-04-17
sources: []
related: [product-doc-spec.md, product-doc-ux-framework.md, product-doc-progressive-disclosure.md, product-doc-starting-map-flow-artifact.md]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/product/evidence-weighted-map.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Evidence-Weighted Map Doctrine (canonical, overrides)

## Summary

`docs/product/evidence-weighted-map.md` is the binding doctrine on what the Socratink graph is and what it may claim. **It overrides every other binding doc on graph-truth, evidence, mastery, completion, diagnostic capability, and what the learner knows.**

Core claim: Socratink is not an AI tutor that claims to know what the learner knows. Socratink is an evidence-weighted map of understanding. The graph shows what Socratink has evidence for — not what the learner knows. The starting map is an anchor, not a diagnostic. Mastery requires spaced reconstruction, not reading.

Defines the **true game loop**: `hypothesis → attempt → delta → repair → spacing → proof → trust`. Distinguishes **proposed structure** (extractor's hypothesis) from **verified learning state** (per-node drill state). Defines **map maturity language**: Draft → Provisional → Tested → Repaired → Verified — these are descriptors, not new states. Defines **app state vs learner capability evidence** — the persisted node states are machine-readable projections of capability evidence; never claims about the learner's mind.

Includes a critical **§13 Legacy Shorthand Replacement Table** that translates phrases like "verified understanding", "mastered", "proved it", "real learning", "you know X", "diagnostic", "primed means learned", "study proves understanding" into evidence-anchored alternatives. Agents must replace these phrases on read and reject them on write — they are not individually catastrophic but load-bearing when they accumulate.

Lists §8 (what the graph MAY claim) and §9 (what the graph MUST NEVER claim) as a closed inventory: any claim absent from §8 and not flagged in §9 is out of scope.

## Raw Artifacts
- `../../../docs/product/evidence-weighted-map.md`

## Connections
- Overrides: all other product/spec docs on graph-truth claims
- Operationalized by: [Starting Map Flow Artifact](product-doc-starting-map-flow-artifact.md)
- Implementation: [Progressive Disclosure](product-doc-progressive-disclosure.md), [Drill Engineering](product-doc-drill-engineering.md)
