---
title: "Docs Registry (doc-map)"
type: source
updated: 2026-04-17
sources: []
related: [product-doc-evidence-weighted-map.md]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/project/doc-map.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Docs Registry (doc-map)

## Summary

`docs/project/doc-map.md` is the inventory of every document under `docs/`. Classification is durable; status reflects the docs pivot to the evidence-weighted map doctrine.

Classification legend: `canonical` (binding doctrine/contract), `implementation` (binding implementation-facing spec), `evidence` (binding release-gate or manual-validation contract), `release-gate`, `workflow`, `artifact` (design storyboard, non-binding), `historical`, `deprecated`.

**Precedence rule**: on any claim about graph truth, evidence, mastery, completion, diagnostic capability, or what the learner knows, `evidence-weighted-map.md` overrides every other binding doc — including the canonical `spec.md`, `ux-framework.md`, and all implementation-tier specs. Legacy shorthand phrases ("verified understanding", "cleared", "mastered", "proved it", "real learning", "possess") must be translated at read time and rejected at write time.

Canonical docs (binding): `evidence-weighted-map.md`, `spec.md`, `ux-framework.md`, `theta/state.md`. Implementation specs: `progressive-disclosure.md`, `post-drill-ux-spec.md`, `drill/engineering.md`, `drill/evaluation.md`, three repair-reps specs, `auth-rollout.md`. Release gates: `project/state.md`, `project/mvp-happy-path.md`, `project/operations.md`. Artifacts: `starting-map-flow-artifact.md`. Workflows (codex/): onboarding, workflows, drill-bml, brain-workflow-architecture, decision-log, agent-review-log.

Lean-startup consolidation candidates (post-MVP, do not consolidate during active release gate): three repair-reps specs should fold into one `repair-reps.md`; `codex/socratink-brain-workflow-architecture.md` duplicates `.socratink-brain/CLAUDE.md` and the skill, should collapse to a stub; `starting-map-flow-artifact.md` should become canonical `starting-map.md` once threshold flow is built.

Registry maintenance rules: register every new doc with status + binding flag + purpose; flip to historical/deprecated when superseded with "Superseded By" filled; do not delete superseded docs.

## Raw Artifacts
- `../../../docs/project/doc-map.md`

## Connections
- Doctrine override: [Evidence-Weighted Map](product-doc-evidence-weighted-map.md)
