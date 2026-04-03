# Project State

## Snapshot

- Product: LearnOps-tamagachi
- Current branch focus: MVP delivery with drill flow, graph progression, and hosted deployment hardening
- Active concerns: deployment reliability, onboarding clarity, and evidence-backed product framing
- Hosted runtime: Vercel serverless
- Operational workflow: narrow regressions can now be routed through `docs/codex/hotfix-workflow.md`

## Current Priorities

- stabilize hosted user flows
- refine drill UX and graph progression
- document research support for learning claims
- establish repeatable agent workflows in-repo

## Target User Signals

- Students are overwhelmed by fragmented study stacks and setup-heavy workflows.
- Card-authoring friction is a major abandonment risk, even when learners believe spaced repetition works.
- Many learners distrust AI that collapses the learning act into shortcut answers or cheating-adjacent behavior.
- Students report burnout from high-effort, low-yield habits and still want systems that push real retrieval.
- Accountability, pacing, and emotional regulation matter, but they must not be confused with mastery.

## Positioning

- MVP value proposition: remove prep friction and increase truthful retrieval reps.
- MVP is not an "AI studies for you" product; AI should automate setup, scheduling, provenance, and support around the loop rather than replace generation.

## Open Questions

- which hosted ingestion paths are reliable enough for MVP
- how YouTube and external content ingestion should degrade gracefully
- which product claims should be softened until evidence docs are complete

## Environment Lessons

- Local success is not deployment validation.
- Hosted YouTube transcript retrieval can fail because YouTube blocks cloud/serverless IPs.
- Current hosted fallback for blocked YouTube transcript retrieval is manual transcript paste.
- External ingestion work must be reviewed for SSRF risk and internal error leakage.
