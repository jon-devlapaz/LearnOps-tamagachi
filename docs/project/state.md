# Project State

## Snapshot

- Product: socratink
- Current branch focus: implementing the three-phase node loop and four-state model as the MVP stabilization target
- Architecture: cold attempt → targeted study → spaced re-drill, with four states (`locked → primed → drilled → solidified`)
- Active concerns: three-phase loop implementation, spacing validation, graph state truthfulness, hosted deployment hardening
- Hosted runtime: Vercel serverless
- Session cap: moving from 35 min to 25 min
- Operational workflow: narrow regressions can now be routed through `docs/codex/hotfix-workflow.md`

## Current Priorities

- implement the three-phase node loop end to end
- enforce the four-state model with no invalid transitions
- add spacing validation to prevent buffer-echo mastery
- stabilize hosted user flows on Vercel
- document research support for learning claims
- establish repeatable agent workflows in-repo

## Architecture Changes In Progress

- The previous Study → Immediate Drill path is being deprecated in favor of the three-phase loop
- Cold attempts are explicitly unscored (no classification, no tier/band)
- `primed` is a new node state between `locked` and `drilled`
- `solidified` can only result from a spaced re-drill after buffer flush
- UX framework, progressive-disclosure, and post-drill-ux-spec have been rewritten (April 2026)
- New strategic docs placed: `north-star.md`, `decision-principles.md`, `current-bets.md`

## Target User Signals

- Students are overwhelmed by fragmented study stacks and setup-heavy workflows.
- Card-authoring friction is a major abandonment risk, even when learners believe spaced repetition works.
- Many learners distrust AI that collapses the learning act into shortcut answers or cheating-adjacent behavior.
- Students report burnout from high-effort, low-yield habits and still want systems that push real retrieval.
- Accountability, pacing, and emotional regulation matter, but they must not be confused with mastery.

## Positioning

- MVP value proposition: remove prep friction and increase truthful retrieval reps.
- MVP is not an "AI studies for you" product; AI should automate setup, scheduling, provenance, and support around the loop rather than replace generation.
- Desirable AI value: personalization, post-attempt feedback, accessibility, concept rendering, and operator leverage around the truthful learning loop.
- Non-negotiable constraint: AI must not pre-answer the active target, inflate mastery, or become the source of graph progression.

## AI Guardrails

- Privacy, security, and data minimization are product requirements, not later compliance work.
- Model evaluation must be treated as fallible and bias-prone, especially across language, phrasing, and accessibility differences.
- Human teaching or coaching value should be amplified, not replaced.
- Core learner value should remain available without unsustainable model spend.
- Any feature that makes answer outsourcing easier than genuine reconstruction is misaligned.
- Fluent model output must not be treated as self-authenticating truth.

## Open Questions

- which hosted ingestion paths are reliable enough for MVP
- how YouTube and external content ingestion should degrade gracefully
- which product claims should be softened until evidence docs are complete
- which AI-assisted feedback patterns improve learning without leaking answers or lowering the mastery bar
- which AI affordances belong in the learner path versus teacher/operator tooling

## Recent Decisions

### 2026-04-02

- Decision: adopt an explicit AI value-and-risk model inside the UX framework and treat it as part of MVP product doctrine.
- Why: the product needs a clearer shared standard for where AI is desirable and where it would break truth, fairness, privacy, or real learning.
- Consequence: future AI features should be evaluated against generation-before-recognition, truthful graph progression, accessibility, trust, and anti-outsourcing constraints.
- Decision: split the public web surface so the marketing site lives at `socratink.ai` and the hosted product lives at `app.socratink.ai`.
- Why: the product now has distinct landing and app deployments, and collapsing both onto one hostname made routing and positioning ambiguous.
- Consequence: hosted verification and future copy work should treat apex and `app.` as separate surfaces; the landing repo still needs its hardcoded app links updated to the new subdomain.

### 2026-04-05

- Decision: complete docs consolidation and product rename to socratink.
- What changed:
  - Renamed all product references from LearnOps-tamagachi to socratink across docs, config, and agent files.
  - Replaced `docs/product/ux-framework.md`, `progressive-disclosure.md`, and `post-drill-ux-spec.md` with rewritten versions reflecting the three-phase loop and four-state model.
  - Placed `north-star.md`, `decision-principles.md`, `current-bets.md` into `docs/project/` (moved from `docs/founder/`, which was removed).
  - Rewrote `docs/project/mvp-happy-path.md` to reflect the 12-step three-phase loop flow.
  - Updated `docs/codex/session-bootstrap.md` to reference the three-phase architecture.
  - Added four-state compatibility flags to `docs/drill/graph-invariants.md`.
  - Added interleaving and three-phase compatibility notes to `docs/product/graph-traversal.md`.
  - Created `docs/research/` directory.
- Missing: three documents referenced in the bootstrap were never created: `three-phase-loop-implementation-brief.md`, `research-prompts.md`, `research-prompt-8-reward-architecture.md`.
- Consequence: the docs directory is now aligned with the April 2026 architecture. `graph-invariants.md` and `graph-traversal.md` are flagged for deeper rewrites in a follow-up session.

### 2026-04-03

- Decision: treat post-drill UX as a separate product-spec layer and keep unresolved exits visibly distinct from true mastery.
- Why: `NEXT` can end a session without producing `solid`, and the UI must not let session resolution masquerade as room clearance.
- Consequence: future graph/detail changes should consult `docs/product/post-drill-ux-spec.md` before changing post-drill copy, badges, transcript visibility, or `Continue` behavior.

## Environment Lessons

- Local success is not deployment validation.
- Public host split is now `socratink.ai` for landing and `app.socratink.ai` for the app.
- Hosted YouTube transcript retrieval can fail because YouTube blocks cloud/serverless IPs.
- Current hosted fallback for blocked YouTube transcript retrieval is manual transcript paste.
- External ingestion work must be reviewed for SSRF risk and internal error leakage.
