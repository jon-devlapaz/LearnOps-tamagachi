# Hot-Fix Workflow

Purpose: define a repeatable workflow for narrow, high-priority regressions that need a fast fix without collapsing into vague feature work or speculative debugging.

Use this when:

- a current user-facing behavior is broken or clearly misaligned with an already intended rule
- the intended behavior can be stated in one or two sentences
- the smallest plausible fix is localized to a small surface area
- the work is important enough to interrupt normal sequencing

Do not use this when:

- the request changes product policy rather than restoring intended behavior
- the change touches graph truth, progression rules, or drill-state semantics in a way that needs a fresh product decision
- the change introduces schema, persistence, API-contract, or ingestion-surface changes
- the issue is primarily hosted/deployment reliability with unclear root cause
- the issue needs research-backed claim changes or new evidence framing

If any of those are true, reclassify as normal feature, investigation, or architecture work.

## Core Principle

Hot-fixes are for restoring truthful behavior quickly.

They are not a shortcut around:

- graph-truth constraints
- generation-before-recognition constraints
- Vercel deployment realities
- SSRF or error-leakage review where relevant
- explicit verification before claiming success

## Default Party

Use the smallest party that can restore the rule safely.

Default hot-fix party:

- `orchestrator`
- `sherlock`
- `thurman`

Add `elliot` when:

- the intended rule is not yet explicit
- the request may actually be feature work
- scope boundary or non-goals are fuzzy

Add `glenna` only after the fact when the workflow itself needs critique.

## Required Brief

Before routing the work, capture a hot-fix brief with these fields:

- surface: where the issue appears
- broken behavior: what currently happens
- intended behavior: what should happen instead
- repro: the smallest set of steps that reproduces it
- impact: why it matters now
- constraints: product or engineering constraints that still apply
- non-goals: what this fix must not expand into

If the brief cannot be written cleanly, the work is probably not yet a hot-fix.

## Role Inputs

### Elliot Needs

Elliot should receive:

- the hot-fix brief
- the affected user flow
- the explicit rule being restored
- the non-goals
- any relevant product constraints, especially graph truth and generation-before-recognition

Elliot outputs:

- hot-fix vs non-hot-fix classification
- the intended interaction or behavior rule in plain language
- scope boundary
- recommended next owner, usually `sherlock` or `orchestrator`

### Sherlock Needs

Sherlock should receive:

- the hot-fix brief
- screenshots or logs if available
- the likely files or surface area if known
- whether the issue reproduces locally, hosted, or both

Sherlock outputs:

- confirmed findings
- likely hypotheses if confirmation is incomplete
- the smallest plausible patch surface
- escalation recommendation if the issue is wider than a hot-fix
- a handoff artifact with:
  - observed bug
  - repro
  - state owner
  - likely root cause
  - patch scope
  - do-not-break invariants
  - residual unknowns

### Orchestrator Needs

Orchestrator should receive:

- Elliot's intended rule
- Sherlock's confirmed root cause or best current hypothesis
- the patch boundary
- the acceptance criteria

Orchestrator outputs:

- the minimal implementation
- any explicit state/doc updates if durable project truth changed
- a concise note of what was changed and what remains out of scope

### Thurman Needs

Thurman should receive:

- the intended rule
- the changed surfaces
- the expected happy path
- likely regression zones
- whether hosted behavior differs from local behavior

Thurman outputs:

- pass/block findings in severity order
- missing verification or fallback paths
- residual risk acceptable for MVP vs not acceptable

### Glenna Needs

Glenna is optional and post-hoc.

Glenna should be invoked when:

- the hot-fix flow felt slow, noisy, or confusing
- role boundaries blurred
- completion was claimed before verification
- the team wants a durable workflow improvement entry

## Workflow

### 1. Declare The Hot-Fix

Owner: `user` or `orchestrator`

Decision:

- is this restoring intended behavior quickly
- or is this actually a product/architecture decision in disguise

Output:

- written hot-fix brief

### 2. Frame The Rule

Owner: `elliot`

Decision:

- what rule is being restored
- what is explicitly out of scope
- does the request remain a hot-fix after framing

Output:

- one-sentence intended rule
- one-sentence scope boundary

### 3. Triage The Cause

Owner: `sherlock`

Decision:

- is the issue local to one interaction surface
- or is it a state-model, data, deployment, or architecture issue

Output:

- confirmed root cause or best current hypothesis
- smallest plausible patch surface
- escalation flag if needed

### 4. Execute The Smallest Fix

Owner: `orchestrator`

Decision:

- what is the smallest change that restores the intended rule
- what should remain untouched to avoid scope drift

Output:

- minimal code diff
- short implementation note

### 5. Verify Before Claiming Success

Owner: `thurman`

Minimum checks:

- the broken behavior is actually gone
- the intended behavior works
- the adjacent flow still works
- the drill/graph/user-facing contract still holds
- hosted-specific risk is called out when relevant

Sufficient evidence to claim a hot-fix is done:

- the original repro no longer fails
- the restored rule is observable in the changed surface
- at least one adjacent regression check passed
- verification is named explicitly in close-out
- hosted status is stated plainly: hosted-verified, local-only, or not yet checked

Output:

- pass/block summary
- residual risk summary

### 6. Log Workflow Improvements If Needed

Owner: `glenna`

Output:

- optional review entry in `docs/codex/agent-review-log.md`

## Scope Drift Guardrails

The following must be named explicitly in every hot-fix:

- what exact rule is being restored
- what surfaces are in scope
- what surfaces are explicitly out of scope
- what would force reclassification out of hot-fix mode
- what evidence counts as fixed

If those are not explicit, the workflow will drift into open-ended polishing or feature design.

## Anti-Patterns To Ban

- claiming a hot-fix is complete before verification matches the original failure mode
- using “hot-fix” as cover for broader UX redesign or cleanup
- skipping the written intended rule and fixing only from intuition
- treating local success as proof of hosted safety
- implying a specialist was queried when the output is really orchestrator synthesis
- silently handing work from one agent to another without naming the next owner
- bundling multiple unrelated regressions into one urgent patch unless they share one root cause

## Reclassify Out Of Hot-Fix Mode When

- more than one domain boundary is involved
- the issue touches backend contract, persistence, or ingestion surfaces
- the requested behavior changes what the graph is allowed to mean
- the issue depends on hosted-only behavior that has not been reproduced or bounded
- the user starts asking for additional UX improvements beyond restoring the rule

## Recommended Trigger Template

Use this exact pattern:

`Hot-fix: <surface>. Broken: <current behavior>. Intended: <restored behavior>. Repro: <short steps>. Impact: <why now>. Constraints: <must-still-hold rules>. Non-goals: <what this is not>.`

Example:

`Hot-fix: graph detail panel. Broken: hovering nodes rewrites the committed right-side drill preview. Intended: hover only orients the graph; click commits the preview. Repro: open graph view and move across nodes. Impact: silent target switching hurts drill UX. Constraints: one active node, no cheat-sheet drift. Non-goals: no traversal redesign.`

## Close-Out Template

Use this shape when reporting completion:

```text
Hot-fix close-out

Root cause:
Rule restored:
Files changed:
Verification performed:
Residual risk:
Status: fixed locally / fixed in hosted path / not yet hosted-verified
Next owner:
```

## Audit Rubric

Use this after each hot-fix run:

1. Was the intended behavior written down before code changed?
2. Was the issue reproduced or otherwise grounded in direct evidence?
3. Did the patch remain inside the declared scope boundary?
4. Did verification match the actual user-visible failure mode?
5. Did the close-out distinguish confirmed fix from remaining uncertainty?

If any answer is `no`, the hot-fix workflow was not fully respected.
