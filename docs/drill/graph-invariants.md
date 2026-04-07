# Drill-Graph Invariants

Purpose: hard engineering rules for keeping drill behavior, graph state, and persisted learner state in sync.

Use this document before changing:

- `public/js/app.js`
- `public/js/graph-view.js`
- `ai_service.py`
- drill routing logic
- graph patching logic
- drill-state persistence

This document is intentionally narrower than the UX framework and the progression spec.

Related docs:

- [../product/ux-framework.md](../product/ux-framework.md)
- [../product/progressive-disclosure.md](../product/progressive-disclosure.md)

## Invariant 1: One Active Node At A Time

A drill session is always bound to exactly one node.

At all times, the following must refer to the same `node_id`:

- the highlighted graph node
- the active drill target
- the node evaluated by the backend
- the node whose result is persisted

No silent target switching.

## Invariant 2: Routing And Mastery Are Different

`routing` controls conversation flow.
It does not, by itself, mean mastery.

Allowed interpretation:

- `NEXT` means move forward in the session

Forbidden interpretation:

- `NEXT` always means unlock downstream content

Only verified understanding should unlock the map.

## Invariant 3: The Graph Must Be Derived From Persisted Data

Cytoscape is a projection layer, not the system of record.

Persist drill results into the knowledge map first.
Then derive graph state from that persisted data.

Do not rely on temporary graph-only classes as authoritative learner state.

## Invariant 4: Patch By `node_id`, Never By Position

When writing drill outcomes:

- patch by stable node identifier
- never assume extraction ordering is stable
- never rely on array position as semantic identity

## Invariant 5: Graph Mutation Rules Must Stay Narrow

Allowed graph mutation:

- `NEXT` with `solid` -> active node becomes `solidified`
- `NEXT` with non-solid classification -> active node becomes `drilled`

No graph mutation on:

- `PROBE`
- `SCAFFOLD`

`SESSION_COMPLETE` does not imply mastery by itself.

## Invariant 6: Cluster State Is Derived

Clusters are containers.
They are not primary drill targets.

Cluster state should be derived from subnode outcomes:

- all subnodes solid -> `solidified`
- some attempted but not all solid -> `drilled`
- no attempts -> `locked`

Do not promote cluster state into a separate conflicting source of truth.

## Invariant 7: Unlock Logic Must Follow Verified Dependencies

Downstream content should open only when its dependency conditions are genuinely satisfied.

That means:

- core thesis gates backbone availability
- backbone state gates dependent clusters
- prerequisite clusters must be solidified before dependent clusters open

Exposure, session advancement, or weak answers are not unlock conditions.

## Invariant 8: Active Drill Presentation Must Not Become A Cheat Sheet

During drill:

- the active target may remain visually identifiable
- the graph may provide orientation
- the graph must not reveal the answer-rich explanation the learner is meant to reconstruct

## Invariant 9: Local And Hosted Behavior Must Be Considered Separately

When drill or ingestion behavior depends on external services:

- verify local behavior
- verify deployed behavior
- do not assume they are the same

This matters in this repo because hosted behavior can differ materially on Vercel.

## Four-State Model Compatibility Flags

> Added 2026-04-05 during doc consolidation. These flags identify where the invariants above need updating for the three-phase loop and four-state model. A full rewrite is deferred — these are conflict markers, not resolutions.

**Invariant 5 (Graph Mutation Rules)** assumes three states. Under the four-state model:

- Cold attempt completion → node transitions from `locked` to `primed` (new mutation type not listed)
- Cold attempts are unscored: no `classification` field, no `solid`/non-solid distinction
- Re-drill with `solid` → `solidified` (unchanged)
- Re-drill with non-solid → `drilled` (unchanged)

**Invariant 6 (Cluster State Is Derived)** needs a `primed` derivation rule:

- Current: `locked` / `drilled` / `solidified`
- Needed: add `primed` — at least one subnode has been cold-attempted but not re-drilled

**Invariant 7 (Unlock Logic)** does not account for spacing validation:

- Downstream content should not unlock based on a cold attempt alone (`primed` is not an unlock condition)
- Re-drill eligibility requires spacing validation (`re_drill_eligible_after` must have passed)
- The frontend must enforce spacing — this is a new invariant not currently listed

**No invariant currently addresses:**

- The prohibition on scoring cold attempts
- The spacing validation contract
- The interleaving requirement between cold attempt and re-drill

## Pre-Change Checklist

Before shipping a drill or graph change, verify:

1. one active node remains clearly identified
2. the backend evaluates that same node
3. only that node is patched on completion
4. non-solid completion does not masquerade as mastery
5. derived cluster state still matches subnode truth
6. graph re-rendering does not lose persisted state

## If A Proposed Change Violates These Rules

Do not patch around it visually.

Fix the state model or the routing contract.
