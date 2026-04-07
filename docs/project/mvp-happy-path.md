# MVP Happy Path

Purpose: current end-to-end tester flow for the MVP branch.

Read this when:

- validating whether the current MVP is healthy enough for sharing
- running manual smoke tests
- checking what "working" means right now for testers

Read these first if you need deeper context:

- [project/state.md](state.md)
- [product/progressive-disclosure.md](../product/progressive-disclosure.md)
- [drill/graph-invariants.md](../drill/graph-invariants.md)

This document describes the intended end-to-end flow for today's MVP tester share.

It is not the full future-state product spec.

It is the concrete "what should work right now" path for manual testing and bug reporting.

## Goal

A tester should be able to:

1. add a concept
2. extract a knowledge map
3. open the graph with four node states visible
4. begin a cold attempt on the first available node
5. see the node become `primed` (no score shown)
6. study the targeted material
7. interleave with cold attempts on other nodes
8. complete a spaced re-drill on the first node
9. see the node become `solidified` or remain `drilled`
10. verify the graph updates without crashing

## Current Product Truth

The graph is an epistemic map, not a progress tracker.

Four states:

- `locked` = not yet available
- `primed` = cold attempt completed, study accessible
- `drilled` = re-drilled but not solid
- `solidified` = verified understanding via spaced re-drill

The graph should update based on structured drill results.

This document is intentionally operational.
It should not become the source of truth for UX philosophy or low-level drill invariants.

## Happy Path: Manual Test

### 1. Start The App

Run:

```bash
uvicorn main:app --reload
```

Open:

```text
http://localhost:8000
```

### 2. Configure API Access

Open Settings and add a valid Gemini API key.

Expected result:

- extraction requests can succeed
- drill requests can succeed

### 3. Create A Concept

Use the drawer flow:

- paste source text or upload a supported file
- enter a concept name
- create the concept

Expected result:

- concept is created in `growing`
- content preview is stored
- the concept appears in the sidebar/grid

### 4. Extract The Knowledge Map

Run extraction for the concept.

Expected result:

- `/api/extract` returns a knowledge map
- `concept.graphData` is populated
- map view becomes available

### 5. Open The Graph

Open the map view and switch to graph mode.

Expected result:

- graph renders without console errors
- core thesis node is visible
- clusters and subnodes render with current derived states
- four node states are visually distinguishable
- graph should not crash when opening/closing quickly

### 6. Begin Cold Attempt On First Available Node

Start a cold attempt on the core thesis or a subnode.

Expected result:

- exactly one active drill node is highlighted
- drill title matches the node being drilled
- cold attempt is explicitly unscored — no classification, no tier/band, no performance metrics shown
- backend receives that node id as the drill target

### 7. Cold Attempt Completes — Node Becomes `primed`

After the cold attempt resolves:

Expected result:

- node state transitions to `primed`
- study view opens with targeted material
- no score or classification is shown to the learner
- normalization message is displayed ("most people get this wrong the first time")
- graph updates to show `primed` state

### 8. Study The Targeted Material

Learner reads the study view.

Expected result:

- study material is targeted to the gap revealed by the cold attempt
- study view does not offer immediate re-drill

### 9. Interleave With Other Nodes

System recommends a cold attempt on a different node (interleaving for buffer flush).

Expected result:

- spacing validation blocks premature re-drill on the first node
- learner completes 1-2 more cold attempts + studies on different nodes
- minimum ~10-15 minutes of interleaved cognitive work before re-drill becomes available

### 10. Spaced Re-Drill On First Node

When `re_drill_eligible_after` has passed, re-drill becomes available.

Expected result:

- re-drill is offered only after spacing requirement is met
- backend receives re-drill phase context
- backend returns structured drill result with classification

### 11. Node State Updates From Re-Drill Classification

Expected result:

- if classification is `solid`, node becomes `solidified` — celebration feedback
- if classification is non-solid, node becomes `drilled` — no celebration, wise feedback
- graph updates without a full remount
- no Cytoscape teardown error appears in console

### 12. Verify Persistence And Graph Truth

After the graph updates:

- click around the graph
- switch map modes
- reopen graph view if needed

Expected result:

- patched node state remains visible
- cluster state reflects subnode outcomes
- no state is lost on graph refresh/re-render inside the current browser session

## Acceptance Criteria

- cold attempt produces `primed` (no score)
- study view opens after cold attempt
- spacing validation blocks premature re-drill
- re-drill produces `solidified` or `drilled`
- four states render in graph (`locked`, `primed`, `drilled`, `solidified`)
- graph updates truthfully from persisted state

## Known MVP Limitations

### 1. localStorage Is The Only Persistence Layer

All learner progress lives in `localStorage`. A browser clear wipes everything. No database, no auth, no server-side persistence. This is acceptable for MVP but not for retention.

### 2. Spacing Validation Is Client-Side

The frontend tracks `study_completed_at` and compares against current time + interleaving activity. This is bypassable. For production, spacing validation should move server-side.

### 3. Mechanism Travels Over The Wire

The frontend still sends `node_mechanism` to `/api/drill`. This is known design debt.

### 4. Session State Lives In Browser Memory

Refresh can interrupt continuity of the active drill session. Persisted graph outcomes survive because they are patched into `concept.graphData`, but in-progress chat/session state does not fully persist.

### 5. Unlock Cascade Is Not Fully Built

The graph reflects drill outcomes and derived cluster state, but the full downstream unlock cascade is still a follow-up slice.

## What Testers Should Report

Ask testers to report:

- which node they were drilling
- what phase they were in (cold attempt vs re-drill)
- what they answered in plain language
- whether the graph updated
- whether the update matched their experience
- whether spacing validation felt correct or premature/overdue
- whether the app crashed or the graph disappeared
- any confusing mismatch between the active drill target and the highlighted graph node

## Failure Conditions

The MVP should be considered unhealthy if any of these occur:

- graph crashes when opening, closing, or updating
- drill result updates the wrong node
- graph changes but `concept.graphData` does not persist the change
- active drill highlight does not match the node being evaluated
- node becomes `solidified` on a non-solid classification
- cold attempt shows a score or classification
- re-drill is offered before spacing requirement is met
- node transitions directly from `locked` to `drilled` or `solidified`
- backend returns success but the graph remains stale

## Minimum Demo Narrative

This is the shortest coherent demo of the three-phase loop:

1. Create concept
2. Extract map
3. Open graph
4. Cold attempt on core thesis — node becomes `primed`
5. Study the targeted material
6. Cold attempt on a subnode — second node becomes `primed`
7. Re-drill first node after spacing — node becomes `solidified` or `drilled`
8. Show graph reflects all four states truthfully

If those eight steps work, the MVP is ready for external qualitative feedback.
