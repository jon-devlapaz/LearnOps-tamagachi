---
title: "Auth Rollout (implementation)"
type: source
updated: 2026-04-17
sources: []
related: [product-doc-project-state.md]
basis: sourced
workflow_status: active
flags: []
source_kind: product-doc
raw_artifacts: [../../../docs/project/auth-rollout.md]
log_surface: none
evaluated_sessions: 0
evaluated_runs: 0
---

# Auth Rollout (implementation)

## Summary

`docs/project/auth-rollout.md` is the implementation contract for introducing account identity and server-backed persistence without breaking the current MVP loop.

Decision: WorkOS AuthKit provider. Sealed `HttpOnly` cookie session. v1 auth methods: Google + email magic link / code. Guest mode stays available. No passwords in v1. FastAPI remains system boundary.

Product rules: do not force login before first value; auth required for save/sync, not for basic exploration; do not auto-merge mastery upward when local and cloud state disagree; signed-in state becomes server-authoritative only after persistence phases complete.

Five-phase rollout: Phase 0 (auth flag + scaffolding + bespoke routes + frontend bootstrap, concept truth still localStorage) → Phase 1 (guest-aware login UI + Save & sync entry + deep return-to behavior) → Phase 2 (account-backed concept persistence + one-time import + explicit conflict choice) → Phase 3 (signed-in concept truth + drill events server-side; localStorage becomes transient cache) → Phase 4 (bespoke branded login page + recovery polish).

Each phase has explicit release gates including auth-off regression checks and `locked → primed → drilled → solidified` validity after sync.

Test plan: automated for auth router, sealed-session, callback return-path sanitization, logout cookie clearing, guest-mode regression. Manual hosted: Google login on localhost and Vercel preview, email flow on preview, refresh after callback, logout, return-to-concept after auth.

Phase 0 deferred: database writes, concept import, conflict resolution UI, remote-authoritative graph persistence, provider/remote session revocation.

## Raw Artifacts
- `../../../docs/project/auth-rollout.md`

## Connections
- Release context: [Project State](product-doc-project-state.md)
