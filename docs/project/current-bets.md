# socratink — Current Bets

## Agent Summary

> **What this document is**: The explicit record of what socratink is betting on, what could go wrong, what we don't know yet, and what we are deliberately not doing. This is the strategic risk surface — it makes assumptions visible so they can be tested, challenged, and updated.
>
> **When to read it**: Before starting a new engineering phase. Before proposing a new feature or direction. Before arguing that something is settled when it might still be a hypothesis. During sprint planning and prioritization.
>
> **What it is NOT**: It is not the UX design contract (read `ux-framework.md`), the tradeoff resolution framework (read `decision-principles.md`), or the implementation plan (read the implementation brief).
>
> **Key facts an agent should know**: Every bet has an evidence strength tag. Every research bet has a "what would change our mind" condition. The top risk is first-session attrition from cold-attempt failure. The product is explicitly not building streaks, database/auth, voice input, narrative layers, teacher dashboards, or engagement-metric optimization this quarter.

---

Last updated: 2026-04-05

## Top 5 Product Bets

### 1. The three-phase node loop is the core product differentiator

Cold attempt → targeted study → spaced re-drill. This sequence is grounded in pretesting effect research, prediction error learning, and spaced retrieval science. We believe this loop produces meaningfully better learning outcomes than study-then-test, and that making it feel magnetic (not punitive) is solvable through framing, attribution management, and social normalization.

Evidence strength: strong. Multiple RCTs, meta-analyses, and the full research synthesis from April 2026 support every phase.

### 2. Interleaved node work replaces hard time gates

Spacing does not require clock-time lockouts. Interleaving cold attempts and study across different nodes produces sufficient buffer flush (10-15 min of cognitive interference) within a single session. This keeps learners inside the product while achieving genuine long-term retrieval on re-drill.

Evidence strength: strong for the cognitive mechanism. The specific rhythm (cold A → cold B → study A → re-drill A) is a product hypothesis, not a tested UX pattern.

### 3. Social normalization prevents cold-attempt attrition

Showing learners that "most people get this wrong the first time" — delivered at the moment of guaranteed failure — is the highest-leverage, lowest-cost intervention for retaining users through the pretesting architecture. The belonging intervention literature shows durable effects from brief, well-timed messages.

Evidence strength: strong. Multiple large-scale RCTs (Walton & Cohen, Park et al., Lin-Siegler et al.) with combined N > 36,000.

### 4. The graph-as-truth is a market positioning advantage

Every competing learning product has an incentive to inflate progress. By making the graph tell the truth — mastery only from spaced retrieval, no celebration of unresolved outcomes — the product earns a form of trust that streak-driven and activity-rewarding products cannot replicate.

Evidence strength: product hypothesis. No competitive analysis has validated this as a user-acquisition advantage, only as a learning-outcome advantage.

### 5. The tier/band trajectory contrast is the metacognitive vehicle

Showing "your cold attempt was a spark, your re-drill hit chain" serves as the prediction-contrast mechanism that corrects the learner's tendency to undervalue pretesting. This is the only intervention the research identifies as capable of updating metacognitive beliefs about the value of productive failure.

Evidence strength: indirectly supported. Pan & Rivers 2023 validated prediction-contrast as a mechanism; the specific tier/band implementation is a design hypothesis.

## Top 5 Engineering Bets

### 1. The four-state model can be implemented without a full backend rewrite

Adding `primed` between `locked` and `drilled` requires new persisted fields (`drill_phase`, `cold_attempt_at`, `study_completed_at`, `re_drill_eligible_after`) and frontend phase tracking, but the existing `concept.graphData` patching architecture should support it without a database migration — because there is no database. The state lives in localStorage.

Risk: localStorage as the persistence layer is fragile. A browser clear wipes all progress. This is acceptable for MVP but not for retention.

### 2. Spacing validation can be enforced client-side

The frontend can track `study_completed_at` and compare against current time + interleaving activity to determine re-drill eligibility. This avoids backend complexity while the persistence layer is localStorage.

Risk: client-side enforcement is bypassable. For MVP this is acceptable. For production, spacing validation should move server-side.

### 3. Gemini 2.5 Flash can support both cold-attempt and re-drill prompt modes

The drill prompt contract requires two distinct modes: an open exploratory question for cold attempts (no scoring, no classification) and a multi-step causal reconstruction demand for re-drills (full scoring). The current `ai_service.py` can support this by extending `session_phase` to distinguish cold-attempt init from re-drill init.

Risk: Gemini's structured response schema may need adjustment to support null classification on cold attempts without breaking validation.

### 4. Vercel serverless can handle the interleaved session pattern

The interleaved rhythm generates more API calls per session than the old linear drill (multiple cold attempts + study views + re-drills). Vercel's cold-start behavior and Gemini rate limits must be validated under this pattern.

Risk: increased API calls per session may hit Gemini rate limits or Vercel function timeouts more frequently.

### 5. Cytoscape can render the four-state model without a full graph rewrite

Adding a `primed` visual state requires new styling rules and potentially new node classes, but the existing Cytoscape rendering pipeline should support it as an additive change.

Risk: Cytoscape teardown/remount bugs may resurface with more frequent state transitions.

## Top 5 Research Bets

### 1. The 10-15 minute interleaving window is sufficient for the pretesting effect + consolidation

The research supports 10-15 minutes as ideal for buffer clearance and early-stage consolidation. We are betting that the natural rhythm of interleaving 2-3 nodes produces this window organically.

What would change our mind: if user testing shows learners rushing through cold attempts and studies in under 5 minutes total, defeating the spacing mechanism.

### 2. Zero-schema detection is feasible within one conversational turn

We are betting that the AI can detect a total absence of domain knowledge from the learner's first cold-attempt response and pivot to scaffolded generation.

What would change our mind: if the AI consistently misclassifies partial knowledge as zero schema, or fails to detect genuine zero schema, leading to either unnecessary scaffolding or cognitive overload.

### 3. ADHD learners benefit from the three-phase loop without modification beyond session caps

We are betting that the existing design constraints (25-min cap, 2-3 node rotation, micro-delay on feedback, no timed interactions, macro-level retrieval prompts) are sufficient for ADHD learners without a fundamentally different product path.

What would change our mind: if ADHD testers report the interleaving rhythm itself as overwhelming or if cold-attempt failure triggers disproportionate dropout in this population.

### 4. The generation effect holds in a typed Socratic chat interface for causal mechanisms

The classic generation effect research used paper-based tasks. The Harvard physics RCT and AI tutoring studies validate the transfer to digital/AI contexts. We are betting this extends to socratink's specific format: typed responses in a Socratic chat about multi-step mechanisms extracted from source material.

What would change our mind: if learners consistently produce shallow keyword responses rather than causal explanations, and the AI cannot distinguish these from genuine generation.

### 5. Pretesting inoculates against test anxiety rather than amplifying it

The affective inoculation literature supports this, but socratink guarantees failure on every first interaction with every node. We are betting that unscored framing + social normalization + dungeon metaphor is sufficient to prevent anxiety cascade.

What would change our mind: if new users report the cold attempt as aversive despite normalization messaging, especially anxious or neurodivergent users.

## Top 5 Risks

### 1. The cold-attempt-first architecture kills first-session retention

The research warns that pretesting increases MOOC dropout. If the first session is all failure (cold attempts on nodes the learner has never seen), the product may lose users before they experience the payoff of the re-drill phase. This is the single highest-risk design decision in the product.

Mitigation: social normalization, unscored framing, dungeon metaphor, the study view as immediate reward for attempting. These must be in place before external testing.

### 2. localStorage wipes destroy trust

A browser clear or device switch erases all progress. A learner who solidified 15 nodes and loses them will not return. This is the most fragile part of the current architecture.

Mitigation: ship a persistence layer (database + auth) before any serious user acquisition. Until then, set expectations clearly and consider export/import as a stopgap.

### 3. Gemini produces inconsistent classifications across similar answers

If two similar explanations of the same mechanism receive different classifications on different attempts, the graph's truthfulness is undermined from the evaluation layer, not the state layer. The learner experiences this as the product being arbitrary.

Mitigation: classification normalization in `ai_service.py` helps, but model-level consistency is not fully controllable. The classification rubric must be concrete (structural checklist, not vibes). The system should err toward false negatives — a slightly strict gate protects graph credibility better than a slightly loose one. Log and monitor classification variance per node.

### 4. The passive trap is hard to detect algorithmically

If the AI's scaffold or feedback is too rich, the learner shifts to passive reading. The current architecture can detect help requests and short responses, but cannot reliably detect a learner who is reading the AI's words and rephrasing them as their own generation.

Mitigation: keep AI responses deliberately sparse. Enforce the constraint that AI talks less than the learner during drill. Track the ratio of AI-generated content to learner-generated content within a drill session. This is a prompt engineering constraint, not an algorithmic detection problem.

### 5. Session caps and spacing feel like gatekeeping, not science

If the learner wants to keep drilling and the product stops them, the framing must be perfect. A badly worded session cap feels like a paywall or a punishment. The transparent-science framing is the mitigation, but it has not been tested with real users.

Mitigation: absolute limits, transparent rationale, warm copy, ending at engagement not exhaustion. Test the copy with real users before shipping.

## Top 5 Unknowns

### 1. What does the first session actually feel like?

We have not tested the cold-attempt-first architecture with a naive user. The research supports it. The framing is designed. But no one has experienced: create concept → extract → cold attempt (fail) → study → cold attempt on next node (fail) → study → re-drill first node. We do not know if this feels magnetic or bewildering.

### 2. How many nodes can a learner interleave before cognitive overload?

The framework says 2-3. The research supports low counts for ADHD. But the optimal number for neurotypical adults on complex material is unknown within this product. It may be 2, it may be 4, it may depend on node complexity.

### 3. Does the tier/band trajectory contrast actually update metacognitive beliefs?

Pan & Rivers showed prediction-contrast works. socratink's implementation (showing spark → chain progression) is a specific design hypothesis. It may land. It may feel like a game score that learners ignore. It needs testing.

### 4. What is the right visual treatment for `primed`?

We know locked = dim, drilled = warm amber, solidified = green/gold. Primed is new. It needs to feel warm and open (entered the room) without feeling like progress toward mastery. No direct experimental validation exists for color choices in learning graph contexts.

### 5. How do learners react to re-drill being blocked by spacing?

When a learner finishes studying and wants to immediately prove they know it, and the product says "not yet — work on another node first," this is either a trust-building moment ("the product is protecting me from fake mastery") or a frustration moment ("the product is stopping me from learning"). We do not know which it will be.

## What We Are Explicitly Not Doing This Quarter

### Not building a database or auth layer yet

The three-phase loop, four-state model, spacing validation, and framing contracts must work end to end before persistence is hardened. Shipping a database before the product architecture is stable risks building the wrong schema.

### Not adding streaks, leaderboards, or competitive mechanics

The research shows these corrode learning goals in truth-oriented products. The Duolingo trap ("people weren't logging in to learn anymore") is the anti-pattern we are designed to avoid. No streaks in MVP. If ever added, only as spaced session streaks.

### Not building voice input

Speech-to-text would activate the Production Effect for additive encoding benefits, and may be especially valuable for ADHD learners. But it requires voice-to-text integration, multimodal AI evaluation, and accessibility testing. Future slice.

### Not building elaborate narrative or story layers

Light quest language (enter the room, clear the boss) is supported. Elaborate storylines decrease procedural knowledge transfer. The dungeon metaphor is structural framing, not fiction.

### Not building a teacher dashboard or multi-learner analytics

The product serves individual learners first. Teacher-facing summaries, class-level analytics, and operator dashboards are downstream of a working, trustworthy individual learning loop.

### Not optimizing for engagement metrics

Time-on-platform, session count, daily active users — none of these are the success metric. The success metric is: does the graph tell the truth, and does the learner trust it? Engagement metrics that conflict with this are discarded, not optimized.
