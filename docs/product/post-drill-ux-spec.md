# Post-Drill UX Spec

Purpose: define how the graph and side panel should look immediately after a drill turn resolves, especially when a session exits without mastery.

Use this document when changing:

- post-drill panel copy
- result-state visual treatment
- transcript visibility after a drill resolves
- the handoff from drill mode back to graph navigation

Do not use this document as the source of truth for:

- routing semantics
- persisted graph state
- unlock rules

For those, read:

- [progressive-disclosure.md](progressive-disclosure.md)
- [graph-invariants.md](../drill/graph-invariants.md)
- [ux-framework.md](ux-framework.md)

## Core Distinction

Post-drill UX must distinguish between:

- session resolution
- mastery resolution

Those are not the same.

- a drill turn can resolve the session with `NEXT`
- only `classification = solid` should read as mastery

If the UI blurs those states, the graph stops telling the truth.

## Canonical Result States

### 1. Solidified

Use when:

- `routing === "NEXT"`
- `classification === "solid"`

What it means:

- the room is cleared
- the node is mastered
- downstream unlock checks may now re-evaluate

Required visual treatment:

- node appears `solidified`
- side panel headline says the room is cleared
- copy acknowledges genuine reconstruction
- result state remains visible until the learner presses `Continue`

Preferred copy shape:

- headline: `Solidified`
- body: short, earned, non-generic acknowledgment

### 2. Unresolved Exit

Use when:

- `routing === "NEXT"`
- `classification !== "solid"`

What it means:

- the session moved on
- the room is still unresolved
- node should remain return-worthy, not shameful

Required visual treatment:

- node appears `drilled`
- side panel must explicitly say the room is not yet cleared
- panel should include one concise diagnosis of what is missing
- result state remains visible until `Continue`

Preferred copy shape:

- headline: `Needs revisit`
- body: `Attempt logged. This room is still unresolved.`

Avoid:

- copy that sounds like completion
- praise that implies mastery
- raw classifier jargon as the main learner-facing label

### 3. In-Progress Drill

Use when:

- `routing === "PROBE"` or `routing === "SCAFFOLD"`

What it means:

- learner is still inside the room
- no graph mutation has happened

Required visual treatment:

- active drill context stays visible
- result framing must not appear yet
- node may be highlighted as the active room, but should not adopt result styling

## Graph-State Meaning

The learner-facing graph should keep these meanings stable:

### `locked`

- unavailable
- low-information

### `drilled`

- attempted but not solid
- unresolved stack pressure
- worth revisiting

### `solidified`

- cleared
- verified understanding

Amber is acceptable for `drilled` only if the accompanying copy clearly frames it as unresolved progress, not failure and not completion.

## Side Panel Rules

The side panel should be mode-pure.

At any given moment it should be in one of three modes:

- inspect
- drill-active
- post-drill

The panel must not silently mix those modes.

### Inspect

- orientation only
- start drill affordance if reachable
- may show concise revisit metadata

### Drill-Active

- one active target
- transcript visible
- no result headline

### Post-Drill

- result headline visible
- chat input hidden
- result remains sticky until `Continue`
- graph clicks should not silently collapse the result state

## Transcript Policy

MVP-safe rule:

- unresolved and solid results may keep the transcript visible below the result card
- the result card must dominate the top of the panel

Recommended next refinement:

- collapse the prior transcript behind a `Review attempt` affordance in post-drill mode

Why:

- keeps the result state legible
- reduces visual mud after a room resolves
- preserves access to the learner's actual attempt without making the panel noisy

## Learner-Facing Labels

Do not expose raw backend terms like:

- `deep`
- `shallow`
- `gap: deep`
- `status: deep`

Prefer translated learner-facing labels, for example:

- `Needs revisit`
- `Needs one more clean pass`
- `Needs a fuller mechanism`
- `Needs correction`

Detailed diagnostic language can appear in the supporting body copy, not as the primary badge.

## Continue Behavior

`Continue` should mean:

- close the resolved session state
- return the panel to normal graph navigation
- preserve the truthful graph node state

It should not:

- silently start another node
- auto-hide the result before the learner sees it
- imply a recommended route unless a separate traversal cue exists

## Anti-Patterns

Do not ship:

- a resolved-session screen that looks identical for `solidified` and `drilled`
- a `drilled` node that reads like completion
- a graph click that silently erases the result state before `Continue`
- a post-drill panel dominated by transcript rather than outcome
- classifier jargon exposed as if it were a user-facing pedagogy model

## Current MVP Decision

As of 2026-04-02:

- `drilled` remains the truthful unresolved state
- post-drill results should stay sticky until `Continue`
- unresolved exits should use explicit revisit language
- raw status/gap labels should be translated into learner-facing copy

## Next UX Slice

When bandwidth allows, the next improvement should be:

1. keep the result card at the top
2. collapse old transcript content behind a reveal
3. optionally add a single `Try again later` or `Re-drill later` cue without implying failure
