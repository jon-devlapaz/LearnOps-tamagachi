# socratink — Three-Phase Node Loop: Implementation Brief

## Agent Summary

> **What this document is**: The phased engineering plan for implementing the three-phase node loop across the socratink codebase. It contains eight implementation phases, each scoped for a single Codex session, with dependency ordering, copy-ready task prompts, acceptance criteria, and agent assignments. This is the document the orchestrator reads to plan and execute the architecture transition.
>
> **When to read it**: Before starting any implementation work on the three-phase loop. Before scoping a Codex session for state model, backend, frontend, graph rendering, panel, guardrail, or copy changes.
>
> **What it is NOT**: It is not the UX philosophy (read `ux-framework.md`), the implementation spec (read `progressive-disclosure.md`), or the result-state spec (read `post-drill-ux-spec.md`). This document assumes you have read those first.
>
> **Key execution constraints**:
> - Phases 1 → 2 → 3 are strictly sequential. Phases 4-6 can parallelize after Phase 3. Phase 7 depends on 4-6. Phase 8 is the QA gate.
> - No phase should break backward compatibility with existing drilled/solidified nodes.
> - The cold-attempt prompt must not reveal the node mechanism. Test with 3+ node types before proceeding.
> - Every phase must be verified on hosted (Vercel), not just local.
> - After Phase 8 passes, orchestrator must update `docs/project/state.md`.

---

Read before starting:

- `docs/product/ux-framework.md` — the design contract
- `docs/product/progressive-disclosure.md` — the implementation spec
- `docs/product/post-drill-ux-spec.md` — the result-state spec
- `AGENTS.md`
- `docs/project/state.md`

## Architecture Summary

The product is moving from a Study → Immediate Drill flow to a three-phase node loop:

```
Phase 1: Cold Attempt (unscored, exploratory)
    ↓
Phase 2: Targeted Study (corrective feedback, immediate)
    ↓
    [interleaved work on other nodes — 10-15 min buffer flush]
    ↓
Phase 3: Spaced Re-Drill (scored, mastery verification)
```

This requires changes across four layers:

1. **State model**: add `primed` state and phase tracking fields
2. **Backend**: add cold-attempt mode to `ai_service.py`
3. **Frontend**: spacing validation, study gating, panel modes, graph rendering
4. **Copy/framing**: normalization messages, attribution copy, session cap copy

## Phased Execution Plan

Eight phases, sequenced by dependency. Each phase is scoped for a single Codex session.

---

### Phase 1: State Model Foundation

**Agent**: `orchestrator` (direct execution)

**Goal**: extend persisted state to support the four-state model and phase tracking without breaking existing behavior.

**Files touched**:

- `public/js/store.js` — add new fields to concept.graphData node schema
- `public/js/graph-view.js` — accept `primed` as a valid state (stub visual; Phase 4 fills it in)
- Any frontend code that reads/writes `drill_status` — audit for three-state assumptions

**Changes**:

- Add `primed` as a valid `drill_status` value alongside `locked`, `drilled`, `solidified`
- Add new persisted fields per node:
  - `drill_phase`: `"cold_attempt"` | `"study"` | `"re_drill"` | `null`
  - `cold_attempt_at`: ISO timestamp or null
  - `study_completed_at`: ISO timestamp or null
  - `re_drill_eligible_after`: ISO timestamp or null
- Existing nodes without new fields default gracefully (null/undefined = `locked`, no phase)
- Graph rendering must not crash when encountering `primed` — use `drilled` visual as fallback

**Acceptance criteria**:

- All existing drill/graph behavior works unchanged
- A node can be manually set to `primed` in devtools and the graph renders without error
- New fields persist through graph re-render and concept switching
- No console errors on graph open/close/update

**Codex task prompt**:

```
Read AGENTS.md, then docs/product/progressive-disclosure.md (four-state model section).

Task: Extend the persisted state model to support four node states.

1. Add `primed` as a valid `drill_status` in the frontend.
2. Add `drill_phase`, `cold_attempt_at`, `study_completed_at`, `re_drill_eligible_after` fields to the node schema in concept.graphData.
3. Audit all code that reads `drill_status` for three-state assumptions and make it four-state safe.
4. Graph rendering must accept `primed` without crashing — use `drilled` visual as temporary fallback.
5. Existing nodes without new fields must default gracefully.
6. No regressions in current drill/graph behavior.

Do not change ai_service.py, drill routing, or side panel behavior in this phase.
```

---

### Phase 2: Backend Cold Attempt Mode

**Agent**: `orchestrator` (direct execution)
**Consult**: `elliot` if prompt contract ambiguity arises

**Goal**: modify `ai_service.py` to support two distinct drill modes — cold attempt (unscored) and re-drill (scored).

**Files touched**:

- `ai_service.py` — `drill_chat()` function, prompt construction, normalization logic
- `main.py` or `api/` — drill endpoint to accept and forward `drill_mode`

**Changes**:

- Add `drill_mode` parameter to `drill_chat()`: `"cold_attempt"` | `"re_drill"`
- When `drill_mode === "cold_attempt"`:
  - Use an open exploratory prompt. Example: "What do you think [node_label] involves? Share your best understanding, even if it's a guess."
  - Force `classification` to null
  - Force `score_eligible` to false
  - Force `response_tier` and `response_band` to null
  - Force `routing` to null (frontend handles transition to study)
  - Still return `agent_response` and `node_id`
  - Enforce minimum generative commitment: if the learner's response has <3 content words or is an explicit "I don't know," the AI's `agent_response` should nudge once for elaboration ("Tell me more — what's your best guess about what happens here?") before allowing study transition
  - Zero-schema detection: if the learner cannot produce even basic relevant vocabulary, the AI seeds 2-3 foundational concepts and asks for a micro-generation
  - Log with `drill_mode: "cold_attempt"` in telemetry
- When `drill_mode === "re_drill"` (or absent for backward compatibility):
  - Existing scoring/classification behavior unchanged
  - Update the prompt to demand multi-step causal reconstruction
  - Vary the prompt angle across re-drill attempts on the same node: self-explanation, summarization, teaching, problem-posing. This prevents linguistic mimicry.
  - Classification rubric must be concrete: "Does the response contain (a) the initiating condition, (b) the causal transition, and (c) the resulting state? If all three are present and correctly linked, classify as solid."
  - Err toward false negatives on borderline cases
- Default to `"re_drill"` if `drill_mode` is absent (backward compatibility)

**Acceptance criteria**:

- `drill_chat(drill_mode="cold_attempt")` returns null classification, null routing, score_eligible=false
- `drill_chat(drill_mode="re_drill")` behaves identically to current behavior
- Calling without `drill_mode` behaves identically to current behavior
- Cold attempt telemetry logs correctly
- The cold-attempt prompt does not reveal the node mechanism
- Minimum generative commitment nudge fires on "idk" responses
- Zero-schema scaffold fires on genuinely empty responses

**Codex task prompt**:

```
Read AGENTS.md, then docs/product/ux-framework.md (AI Drill Prompt Contract and Phase 1: Cold Attempt).

Task: Add cold-attempt mode to ai_service.py drill_chat().

1. Add `drill_mode` parameter: "cold_attempt" or "re_drill". Default to "re_drill" for backward compatibility.
2. In cold_attempt mode: use an open exploratory prompt, force classification/score/tier/routing to null, return agent_response and node_id only.
3. In cold_attempt mode: enforce minimum generative commitment — nudge once on minimal responses before allowing transition.
4. In cold_attempt mode: detect zero-schema states and seed foundational concepts before requesting micro-generation.
5. In re_drill mode: demand multi-step causal reconstruction. Vary prompt angle across attempts (self-explanation, summarization, teaching, problem-posing).
6. In re_drill mode: use concrete classification rubric (initiating condition + causal transition + resulting state). Err toward false negatives.
7. Update the drill API endpoint to accept and forward drill_mode.
8. No regressions when drill_mode is absent.
9. Log drill_mode in telemetry.

Do not change frontend state management or graph rendering in this phase.
```

---

### Phase 3: Frontend Phase Orchestration

**Agent**: `orchestrator` (direct execution)
**Consult**: `elliot` for flow ambiguity; `sherlock` if state bugs emerge

**Goal**: implement the frontend three-phase loop — controlling when cold attempts, study, and re-drills are offered, and enforcing spacing validation.

**Files touched**:

- `public/js/app.js` — drill initiation logic, phase transitions
- `public/js/store.js` — phase tracking reads/writes
- `public/js/graph-view.js` — node click behavior based on phase
- Side panel code — which mode to show based on node state and phase

**Changes**:

- When learner clicks an available `locked` node:
  - Initiate cold attempt: call `/api/drill` with `drill_mode: "cold_attempt"`
  - On response: set `drill_status` to `primed`, `drill_phase` to `study`, `cold_attempt_at` to now
  - After 2-3 second transition beat, open study view (ADHD micro-delay)
- When learner is in study mode for a `primed` node:
  - Show mechanism text for this specific node
  - On "Continue" or study completion: set `study_completed_at` to now, `re_drill_eligible_after` to now + 5 minutes (minimum), `drill_phase` to `re_drill`
  - Recommend next cold attempt on a different available node (interleaving)
- Spacing validation on `primed` node in `re_drill` phase:
  - Check: is `re_drill_eligible_after` in the past? If not, block re-drill. Show: "Work on another node first — your brain needs time to consolidate this one."
  - Check: has at least one other cognitively demanding activity been completed since study? (Heuristic: at least one other cold attempt or study completed since this node's `study_completed_at`)
  - If spacing satisfied: initiate re-drill with `drill_mode: "re_drill"`
- On re-drill result:
  - `classification === "solid"`: set `drill_status` to `solidified`, clear gap metadata, trigger unlock evaluation
  - `classification !== "solid"`: set `drill_status` to `drilled`, persist gap
  - Set `drill_phase` to null (loop complete for this attempt)
- Interleaving recommendation: after study completes, surface next available `locked` node for cold attempt, or next `primed` node eligible for re-drill. Single clear "next step" — not a menu.

**Acceptance criteria**:

- Full loop works: locked → cold attempt → primed → study → (interleave) → re-drill → solidified/drilled
- A node cannot go directly from locked to solidified
- Re-drill is blocked when spacing requirement is not met
- Spacing message appears when re-drill attempted too early
- Study view shows mechanism text only for the cold-attempted node
- Interleaving recommendation appears after study as a single next step
- No regressions for existing drilled/solidified nodes
- 2-3 second transition beat before study view appears

**Codex task prompt**:

```
Read AGENTS.md, then docs/product/progressive-disclosure.md (Three-Phase Node Loop, Phase Tracking, Spacing Validation sections).

Task: Implement the frontend three-phase loop orchestration.

1. Cold attempt: when learner clicks available locked node, call /api/drill with drill_mode "cold_attempt". On response, set drill_status "primed", drill_phase "study", cold_attempt_at now. After 2-3 second beat, show study view.
2. Study: show mechanism text for the primed node. On completion, set study_completed_at, re_drill_eligible_after (now + 5 min), drill_phase "re_drill".
3. Spacing validation: block re-drill if re_drill_eligible_after is future or if no interleaved activity since study. Show spacing message.
4. Re-drill: call /api/drill with drill_mode "re_drill". Set drill_status to solidified or drilled based on classification.
5. Interleaving: after study, recommend next available locked node or next spacing-eligible primed node. Single clear "next step" — not a menu.
6. Backward compatibility: pre-existing drilled/solidified nodes must continue working.

Do not change graph visual rendering (Phase 4) or copy/framing (Phase 7).
```

---

### Phase 4: Graph Rendering — Primed Visual State

**Agent**: `orchestrator` (direct execution)
**Dependency**: Phase 1

**Goal**: add a distinct visual treatment for `primed` nodes in Cytoscape.

**Changes**:

- Add `primed` style class to Cytoscape node definitions
- Visual: warm, open, inviting — distinct from locked (dim) and drilled (amber). Consider soft blue-white or light warm tone. Treat as hypothesis.
- Solidified transition: strongest visual treatment (the line clear), calibrated to cognitive load if feasible
- Drilled transition: warm but subdued — no celebration
- Ensure state transitions animate smoothly without Cytoscape teardown

**Codex task prompt**:

```
Read docs/product/post-drill-ux-spec.md (Graph-State Meaning and Sensory Treatment sections).

Task: Add primed visual state to Cytoscape graph rendering.

1. Add Cytoscape style class for `primed` nodes. Warm, open, inviting — distinct from locked (dim) and drilled (amber).
2. All four states must render distinctly at a glance.
3. Solidified transition gets strongest visual treatment.
4. Drilled transition is subdued — no celebration.
5. Test that transitions between valid state pairs don't cause teardown/re-render errors.
```

---

### Phase 5: Side Panel Modes

**Agent**: `orchestrator` (direct execution)
**Dependency**: Phase 3

**Goal**: update side panel to support six distinct modes.

**Six modes**: inspect, cold-attempt-active, study, re-drill-active, post-re-drill, session-complete. Each must be mode-pure — no content bleed.

**Codex task prompt**:

```
Read docs/product/post-drill-ux-spec.md (Side Panel Rules — all six modes).

Task: Implement six side panel modes for the three-phase loop.

1. Inspect: orientation. Content varies by node state.
2. Cold-attempt-active: Phase 1. AI question + transcript. No mechanism text, no scores.
3. Study: Phase 2. Mechanism text for cold-attempted node. Normalization message. "Continue" marks study complete.
4. Re-drill-active: Phase 3. Transcript. No result headline yet.
5. Post-re-drill: result card (Solidified or Needs Revisit). Trajectory contrast if available. Chat input hidden. Sticky until Continue.
6. Session-complete: session cap triggered. Save-point copy.

Modes must be pure — no content bleed between modes.
```

---

### Phase 6: Session Guardrails Update

**Agent**: `orchestrator` (direct execution)
**Dependency**: Phase 3

**Changes**:

- Reduce session time cap from 35 to 25 minutes
- Keep 4-node cap
- Add per-node retrieval ceiling: 3 successful retrievals per node per session
- On guardrail trigger, transition to session-complete panel mode
- Prefer ending between phases rather than mid-drill

**Codex task prompt**:

```
Read docs/product/progressive-disclosure.md (Session Guardrails section).

Task: Update session guardrails.

1. Reduce time cap to 25 minutes.
2. Keep 4-node cap.
3. Add per-node ceiling: after 3 successful retrievals on one node, block further re-drill on that node this session.
4. On guardrail trigger, transition to session-complete panel mode.
5. Prefer ending between phases rather than mid-drill.
```

---

### Phase 7: Copy and Framing

**Agent**: `orchestrator` (execution)
**Consult**: `rob` for copy texture and tone review (read-only)

**Goal**: implement learner-facing copy for normalization, attribution, session endings, and spacing.

**Copy sets**:

- **Cold-attempt normalization** (4 rotating variants): "Your guess just primed your brain..." / "Most learners get this wrong the first time..." / "This is how your brain prepares to learn..." / "That attempt just activated your semantic networks..."
- **Spacing block**: "Work on another node first — your brain needs time to consolidate this one."
- **Solidified**: headline "Solidified", trajectory contrast, earned acknowledgment
- **Unresolved (wise feedback)**: headline "Needs revisit", strategy-focused gap description, belief in learner, specific next step. No raw classifier labels. No ability framing.
- **Session complete**: headline "Session saved", transparent spacing science, forward-looking warmth

**Codex task prompt**:

```
Read docs/product/ux-framework.md (Attribution Management and Framing sections).
Read docs/product/post-drill-ux-spec.md (Canonical Result States and Tier/Band Display sections).

Task: Implement learner-facing copy for the three-phase loop.

1. Add 4 rotating normalization messages after cold attempt completion.
2. Add spacing-blocked message when re-drill attempted too early.
3. Add solidified result copy with trajectory contrast (if tier/band data available).
4. Add unresolved result copy using wise feedback — strategy-focused, never ability-focused.
5. Add session-complete copy with transparent spacing science.
6. No raw classifier labels in any learner-facing surface.

Invoke rob (read-only) for copy texture and tone review. Rob evaluates warmth and non-judgment but does not edit files. Orchestrator makes final copy decisions.
```

---

### Phase 8: QA and Release Validation

**Agent**: `thurman` (read-only review)
**Dependency**: Phases 1-7 complete

**Validation checklist (10 points)**:

1. Happy path end to end (cold attempt → study → interleave → re-drill → graph update)
2. No invalid state transitions (locked→solidified, primed→solidified without spacing)
3. Spacing enforcement works and shows correct message
4. Per-node retrieval ceiling (3 per session) works
5. Session cap (25 min) triggers session-complete panel
6. Cold attempt is fully unscored (no classification, no tier/band)
7. Copy is strategy-focused, no raw labels, normalization messages appear
8. Graph renders all four states distinctly, solidified is most prominent
9. Backward compatibility with pre-update node states
10. All behavior confirmed on hosted (Vercel), not just local

**Codex task prompt**:

```
Read AGENTS.md, then docs/product/progressive-disclosure.md, post-drill-ux-spec.md, and ux-framework.md.

You are Thurman. Review the completed three-phase loop for release readiness.

Validate against 10 criteria:
1. Happy path works end to end
2. No invalid state transitions
3. Spacing enforcement works with correct message
4. Per-node retrieval ceiling works
5. Session cap triggers session-complete panel
6. Cold attempt is fully unscored
7. Copy is strategy-focused, no raw labels, normalization messages appear
8. Graph renders all four states, solidified most prominent
9. Backward compatibility with pre-update states
10. All confirmed on hosted (Vercel)

Report findings by severity (high/medium/low). Recommend next owner for any issues.
```

---

## Dependency Graph

```
Phase 1 (State Model)
    ↓
Phase 2 (Backend Cold Attempt) ──────────────────────┐
    ↓                                                 │
Phase 3 (Frontend Phase Orchestration)                │
    ↓                    ↓              ↓             │
Phase 4 (Graph)    Phase 5 (Panel)  Phase 6 (Guardrails)
    ↓                    ↓              ↓             │
    └────────────────────┴──────────────┘             │
                         ↓                            │
                  Phase 7 (Copy) ←────────────────────┘
                         ↓
                  Phase 8 (QA)
```

Phases 1 → 2 → 3 are strictly sequential.
Phases 4, 5, 6 can run in parallel after Phase 3.
Phase 7 depends on Phases 4-6.
Phase 8 runs after all phases complete.

## Risk Notes For Orchestrator

- **localStorage migration**: existing concepts will not have new fields. Phase 1 must handle graceful defaults. Do not wipe existing progress.
- **Backward compatibility**: the drill endpoint must accept calls without `drill_mode` and behave identically. Phase 2 must not break existing flows.
- **Gemini prompt sensitivity**: the cold-attempt prompt must not accidentally reveal the mechanism. Test with at least 3 different node types before proceeding to Phase 3.
- **Classification consistency**: the concrete rubric (initiating condition + causal transition + resulting state) must be tested for consistency across similar answers. Log classification variance per node. Err toward false negatives.
- **Cytoscape re-render**: adding a fourth state may trigger edge cases. Phase 4 should be tested with rapid state transitions.
- **Copy tone**: Phase 7 should invoke `rob` for a read-only tone review. Rob evaluates warmth and non-judgment but does not edit files.
- **Phase 3 is the riskiest session**: it touches app.js, store.js, and graph-view.js simultaneously, implements spacing validation, and introduces interleaving recommendations. If it gets messy, invoke `sherlock` to trace state bugs before proceeding.

## State Update

After Phase 8 passes, `orchestrator` must update `docs/project/state.md` with:

- three-phase loop is implemented and validated
- four-state model is live
- session cap is 25 minutes
- spacing validation is enforced client-side
- the previous Study → Immediate Drill path is deprecated
- known limitations (client-side enforcement, localStorage fragility)
