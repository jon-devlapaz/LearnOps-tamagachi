# Product UX Framework

Purpose: enduring product philosophy for how LearnOps-tamagachi should feel and what kinds of UX decisions are acceptable.

Use this document when deciding:

- what the product should reward
- what the graph should mean
- how drill should feel
- whether a proposed UX pattern is aligned or misleading

Do not use this document as the source of truth for:

- current routing semantics
- persistence fields
- unlock implementation details

For current implementation behavior, read:

- [progressive-disclosure.md](progressive-disclosure.md)
- [graph-invariants.md](../drill/graph-invariants.md)

## Product Thesis

The enemy is the illusion of competence.

Most learning tools reward exposure, recognition, and streak maintenance.
LearnOps-tamagachi should reward reconstruction.

The product is trying to make a hard cognitive act feel magnetic:

- select one idea
- reconstruct it from memory
- get a truthful result
- see the board change because of what was actually understood

The graph is not a content browser.
It is not a completion checklist.
It is a spatial record of verified understanding.

## Core Experience Goal

Make learning feel rewarding without lying to the learner.

That means:

- the learner should feel momentum
- the learner should feel curiosity
- the learner should feel a strong payoff when understanding is genuine
- the learner should get fast, specific feedback after they attempt reconstruction
- the system should adapt support to the learner without lowering the mastery bar
- the product should become more accessible and more usable for different kinds of learners
- the system should never fake mastery to preserve motivation

Reward is allowed.
False reward is not.

## AI Value Model

AI is desirable in this product when it increases the quality, speed, accessibility, and frequency of truthful learning loops.

AI is not the learning event.
It is a support layer around the learning event.

The core learning event is still:

- learner sees the target
- learner generates from memory
- system evaluates the attempt
- graph updates truthfully

If AI makes that loop easier to enter, easier to understand, or easier to repeat, it is useful.
If AI replaces that loop, it is misaligned.

### Desirable Uses Of AI

#### 1. Personalization Without Comfort-Lying

AI should tailor pacing, scaffolding, modality, and follow-up prompts to the learner's current state.

Good personalization:

- picks the right next challenge
- adjusts support based on observed gaps
- varies explanation style or representation
- preserves the same standard for `solidified`

Bad personalization:

- hides difficulty to keep engagement high
- gives easier success in place of real understanding
- confuses learner preference with learner mastery

#### 2. Immediate Feedback After Generation

AI should provide fast, specific feedback after the learner attempts an answer.

That feedback should help the learner see:

- what they got right
- what mechanism is missing
- what kind of retry or scaffold would help

The order matters.
Generation first.
Recognition and explanation second.

#### 3. Content Creation As Support, Not Substitution

AI can help generate drills, examples, assessments, visuals, lesson material, and alternate phrasings.

This is desirable when it:

- reduces authoring overhead for educators, coaches, or internal operators
- increases the range of practice material
- creates alternate explanations for the same underlying mechanism

It is not desirable when generated content becomes:

- answer leakage
- decorative volume with no cognitive purpose
- low-truth assessment that inflates progress

#### 4. Inclusivity And Access

AI should make the learning loop more accessible across reading, language, speech, and perceptual differences.

Desirable examples:

- text-to-speech or speech-to-text support
- alternate reading levels or simplified phrasing
- visual, spoken, or interactive representations of the same idea
- assistance that helps a learner participate in generation rather than bypass it

Accessibility support should widen access to the same real task, not quietly swap in a weaker task.

#### 5. Concept Rendering For Hard Ideas

AI can help make abstract ideas more graspable through diagrams, imagery, analogies, and alternate framings.

This is useful when it:

- clarifies structure
- makes invisible mechanisms more legible
- helps the learner return for another genuine attempt

These supports should illuminate the concept without collapsing the answer into the interface.

#### 6. Resource Expansion And Operational Leverage

AI can expand what the product can provide around the core learning loop.

Useful areas:

- brainstorming and lesson planning
- generating practice variants
- summarizing learner patterns for a teacher or coach
- administrative help such as grading support, scheduling, communication drafts, or record organization

This matters because human time should move toward coaching, diagnosis, and direct learner support.

#### 7. Critical Thinking About AI Itself

The product should treat AI as something learners must evaluate, not merely consume.

Good AI-enabled learning should reinforce:

- checking whether an explanation is actually coherent
- noticing uncertainty and possible error
- discussing when an output is useful, misleading, biased, or overconfident
- ethical use of generated material

We do not want passive trust in fluent outputs.

### Risk Flags To Avoid

AI can improve the product.
It can also degrade trust, fairness, safety, cost discipline, and real learning if used carelessly.

The product should treat these as active design risks:

#### 1. Privacy And Security Drift

AI systems often require collection, storage, or transmission of sensitive learner data.

Risk signals:

- collecting more learner data than the product actually needs
- unclear retention or deletion behavior
- exposing sensitive inputs to third-party systems without clear boundaries
- leaking internal errors, prompts, or hidden system details back to the user

Principle:

Use the minimum necessary data, protect it tightly, and do not trade learner privacy for convenience.

#### 2. Algorithmic Bias And Unequal Misclassification

AI can unfairly score, route, or interpret learners because of biased training data or brittle heuristics.

This matters especially when learners differ by:

- language background
- disability or accessibility needs
- cultural phrasing
- accent, speech pattern, or writing style

Principle:

Do not let model fluency preferences masquerade as learning truth.
If an evaluation system may systematically disadvantage certain learners, it is not acceptable as a mastery gate.

#### 3. Human Relationship Erosion

AI should not displace the teacher, coach, or socially meaningful parts of learning.

Risk signals:

- replacing feedback that should involve human judgment
- reducing opportunities for encouragement, mentorship, or discussion
- turning learning into isolated transaction loops with no human context

Principle:

AI should create more room for high-value human support, not less.

#### 4. Cost Structures That Break Equity

Advanced AI systems can be expensive to deploy and maintain.

Risk signals:

- core learning value depends on expensive model usage
- schools or learners with fewer resources get a degraded version of the product
- infrastructure cost pushes the product toward manipulative engagement tactics

Principle:

The product should not require unsustainable spend to deliver its core truth-telling loop.
Cost discipline is part of accessibility and equity.

#### 5. Academic Misconduct And Answer Outsourcing

AI can make it easier for learners to skip the act of reconstruction.

Risk signals:

- learners can generate or view the answer before attempting
- assessments can be completed by prompting instead of thinking
- the interface cannot distinguish self-generated understanding from outsourced output

Principle:

If the system makes cheating easier than thinking, the UX is broken.

#### 6. Inaccuracy, Overconfidence, And Unpredictability

AI can produce false, misleading, or unstable outputs even when it sounds authoritative.

Risk signals:

- explanations stated with unjustified certainty
- feedback that is inconsistent across similar answers
- generated content that introduces factual or conceptual errors
- model output being treated as correct by default

Principle:

AI output is assistive, not self-authenticating.
The product must be designed so learners and educators can question it, inspect it, and recover from its mistakes.

## Primary Metaphor

The graph behaves like a dungeon map.

- each graph node is a room
- the active drill target is the room's boss
- the learner must beat that boss before the room is truly cleared
- a room can be entered without being cleared
- new rooms should open only when prerequisite understanding is real

This metaphor is useful because it keeps effort, difficulty, and progression tied to truth.

If a feature makes it feel like the learner fought one room while the system updated another, the feature is wrong.

## Secondary Emotional Analogy

Tetris is a useful analogy for the rhythm of drilling.

Not visually.
Mechanically and emotionally.

The right feeling is:

- one problem at a time
- visible structure, hidden solution
- meaningful consequence
- satisfaction when a move is genuinely clean

Applied here:

- the graph is the board
- the active node is the current problem
- drill is the cognitive move
- `solidified` is a clean resolution
- `drilled` is unresolved stack pressure, not failure

## Non-Negotiable UX Principles

### 1. Generation Before Recognition

The learner must generate the answer before the interface lets them recognize it.

That means:

- the active mechanism should not remain visible during drill
- AI help should not pre-answer the task
- the graph may identify the active room
- the graph must not become a cheat sheet

### 2. One Active Cognitive Target

At any moment, the learner should know:

- what they are drilling
- where it sits in the map
- whether it is unresolved or cleared

No silent target switching.
No mixed-state drill sessions.

### 3. The Graph Must Tell The Truth

The graph represents understanding, not activity.

That means:

- attempted is not mastered
- session advance is not mastery
- time spent is not mastery
- personalization is not mastery
- fluent AI interaction is not mastery
- only verified understanding should open downstream territory

### 4. Reward Must Be Earned

Good reward design:

- selective visual change
- clear acknowledgment of what changed
- stronger payoff when understanding is genuinely solid

Bad reward design:

- generic praise
- fake unlocks
- inflated positive feedback for weak answers

### 5. In-Progress Must Not Feel Punitive

Unresolved nodes should feel return-worthy, not shameful.

Preferred framing:

- unfinished
- worth revisiting
- the next gain is here

Avoid:

- failure identity language
- punitive color systems
- over-graded emotional feedback

### 6. AI Should Reduce Friction, Not Remove Thinking

The system should automate setup, access, authoring, and feedback overhead.
It should not automate away the learner's reconstruction work.

Good friction reduction:

- faster entry into a drill session
- clearer diagnosis after an attempt
- easier access for different learners
- less authoring or admin burden around the learning loop

Bad friction reduction:

- skipping the attempt
- revealing the mechanism too early
- converting challenge into passive consumption

### 7. AI Must Preserve Trust, Fairness, And Human Judgment

An AI-heavy product that feels efficient but becomes invasive, biased, unauditable, or socially thinning is not a good learning product.

Good use:

- bounded data use
- fair evaluation standards
- visible uncertainty where appropriate
- preserving the role of teachers, coaches, or human review

Bad use:

- opaque scoring
- hidden data risk
- replacing human support where it matters
- letting confident wrongness shape learner progress

## What The Graph Is For

The graph exists for orientation and truthful progression.

It should answer:

- where am I
- what is available
- what changed

It should not answer:

- what exact mechanism should I parrot back right now

## What This Means In Practice

When evaluating a new UX idea, ask:

1. Does this make the learner's current target clearer or blurrier?
2. Does this make the graph more truthful or more decorative?
3. Does this reward real reconstruction or mere participation?
4. Does this preserve curiosity without revealing the answer?
5. Does the AI support the learning loop or replace the learner's thinking?
6. Does this preserve trust, fairness, privacy, and meaningful human oversight?

If the answer is wrong on those questions, the idea is misaligned even if it feels polished.
