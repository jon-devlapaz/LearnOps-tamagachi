# socratink — North Star

## Agent Summary

> **What this document is**: The five foundational strategic questions that govern product direction, market positioning, and identity boundaries, plus the core positioning analogy. This is the "why" and "who" document — it tells you what socratink is for, who it serves, what it refuses to become, and where the moat lives.
>
> **When to read it**: Before proposing a new product direction, evaluating competitive positioning, writing external messaging, or questioning whether a feature belongs in the product. Read this before `ux-framework.md` if you need to understand the strategic intent behind the design constraints.
>
> **What it is NOT**: It is not the UX design contract (read `ux-framework.md`), the implementation spec (read `progressive-disclosure.md`), or the execution plan (read `current-bets.md`).
>
> **Key facts an agent should know**: socratink serves three user profiles (students, PhD educators, ADHD learners). The moat is structural architecture, not Socratic prompting. The unifying design principle is **metacognitive UX** — designing for the learner's awareness of their own cognitive process, not just the content. The product refuses to optimize for engagement metrics over verified understanding. Trust is the most valuable asset — it comes from graph truthfulness, not feature volume. The emotional positioning is "Dark Souls for your brain" — difficulty is respect, not punishment.

---

This document should be stable across quarters. Update it when conviction changes, not when features ship.

## Who exactly is the primary learner?

Students who are overwhelmed by fragmented study stacks and setup-heavy workflows, but still want real recall practice instead of AI shortcutting.

More precisely: learners who suspect their current study methods are producing the illusion of competence rather than genuine understanding, and who are willing to trade comfort for truth — if the product makes the hard path feel magnetic rather than punitive.

The product must also work for two adjacent profiles that stress-test the design:

- Educators (PhD-level) who want to validate whether the pedagogical model is trustworthy.
- Neurodivergent learners (ADHD) who need the difficulty calibrated for shorter attention spans, smaller working memory buffers, and higher sensitivity to punitive framing.

If the product works for all three profiles, the design is sound. If it only works for the founder, it is not a product.

## What painful alternative are we replacing?

The status quo is a stack of disconnected tools that each fail differently:

- Passive rereading and highlighting that produce the illusion of fluency while encoding nothing durable.
- Flashcard apps (Anki, Quizlet) that test recognition of discrete facts but never verify causal understanding or mechanism reconstruction.
- AI chatbots (ChatGPT, Claude) used as crutches that outsource the cognitive work entirely — learners copy-paste answers and cannot recall what they wrote minutes later.
- AI "tutor" wrappers that withhold answers but still operate on unstructured material with no knowledge map, no graph truth, and no verified progression.

The common failure across all of these: none of them force the learner to reconstruct a mechanism from memory, verify that the reconstruction is genuine, and record the outcome truthfully.

socratink replaces this stack with a single loop: ingest source material → extract a structured knowledge map → cold attempt before study → targeted corrective study → spaced re-drill → truthful graph update. Every step is grounded in the cognitive science of how durable knowledge actually forms.

## What does "best in market" actually mean?

Best in market does not mean most features, most content, or most AI.

Best in market means: the product that tells the learner the most accurate truth about what they actually understand, while making the process of discovering that truth feel magnetic rather than punitive.

No other product in market connects all four structural differentiators:

1. **Extraction produces the answer key.** The knowledge map is not a topic list — it is a causal architecture of mechanisms, relationships, and dependencies. The extraction pipeline forces mechanism-level syntax that makes every node drillable downstream.

2. **The graph enforces truthful state.** Node states represent verified understanding, not activity or exposure. The four-state model (`locked → primed → drilled → solidified`) prevents the graph from lying about what the learner actually knows.

3. **The three-phase loop enforces cognitive sequencing.** Cold attempt before study (pretesting effect). Targeted study as corrective feedback (prediction error). Spaced re-drill after buffer flush (genuine long-term retrieval). No phase can be skipped. No phase can be collapsed into another.

4. **Mastery is verified against spaced retrieval, not buffer echo.** `Solidified` only comes from a re-drill that occurs after the working memory buffer has been cleared through interleaved cognitive work. Testing immediately after study is explicitly blocked as a mastery signal.

The moat is not Socratic prompting — that is a system prompt anyone can write. The moat is the structural architecture that connects extraction, graph truth, cognitive sequencing, and spaced verification into a single product loop.

### The Unifying Principle: Metacognitive UX Design

The four differentiators above are structural expressions of a single design principle that defines socratink's category.

Every other learning product is designed around **cognitive UX** — making learning content easier to consume, navigate, and complete. socratink is designed around **metacognitive UX** — making the learner's *own cognitive process* visible, interpretable, and trustworthy to themselves.

This is the difference:

- The cold attempt doesn't teach content. It teaches the learner **what they don't know** — and makes that discovery feel like exploration rather than judgment.
- The targeted study doesn't just present information. It shows the learner **exactly where their mental model broke** — anchored to the prediction error they just generated.
- The spacing block doesn't just enforce a delay. It teaches the learner **that their feeling of knowing is unreliable** — that the fluency they feel right after studying is a cognitive illusion, not evidence of understanding.
- The trajectory contrast doesn't just show progress. It shows the learner **how their own metacognitive predictions were wrong** — and that's the only intervention the research found that actually updates beliefs about the value of productive struggle.
- The normalization messages don't just reduce anxiety. They teach the learner **how to interpret difficulty** — as a feature of the process, not a verdict on their capacity.
- The graph doesn't just track progress. It gives the learner **a spatial mirror of their own understanding** — one they can trust because the system never inflates it.
- The session cap doesn't just prevent fatigue. It teaches the learner **that their brain has consolidation constraints** — and that respecting those constraints is part of how mastery actually works.

Every surface in socratink is doing the same thing: making the invisible cognitive process visible, and teaching the learner to read it accurately.

This is not a feature or a tagline. It is the design category socratink occupies. No other learning product designs for the learner's awareness of their own learning process as the primary UX objective. Duolingo designs for habit. Anki designs for recall scheduling. ChatGPT designs for conversational fluency. socratink designs for **metacognitive accuracy** — the learner's ability to know what they know, know what they don't, and trust the system that tells them the difference.

## What do we refuse to become?

We refuse to become a product that:

- rewards exposure, streak maintenance, or session completion as if they were learning
- lets AI replace the learner's reconstruction work
- fakes mastery to preserve engagement metrics
- uses loss-aversion mechanics (streak anxiety, FOMO, paid recovery) to drive return behavior
- treats difficulty as a bug to be smoothed away rather than the engine of genuine learning
- optimizes for time-on-platform over verified understanding
- ships features that make the graph lie

We are not Duolingo. We are not a flashcard app. We are not an AI homework assistant.

We are a product that tells the truth about what you know, makes the hard work of finding out feel like a game worth playing, and respects the cognitive science of how durable knowledge actually forms.

## What would make this product uniquely trustworthy?

Trust in a learning product comes from one thing: the learner's growing conviction that the product is not lying to them.

Every other learning product on the market has an incentive to inflate progress. Engagement metrics reward activity volume. Gamification rewards streaks and badges. AI wrappers reward fluent interaction. All of these can produce beautiful dashboards of fake progress while the learner retains nothing.

socratink earns trust by doing the opposite:

- The graph only changes when understanding is verified through genuine retrieval.
- The product tells you when you don't know something, clearly and without shame.
- The product explains why difficulty is productive, transparently, using real science.
- The session cap stops you before you're depleted, not after.
- The reward layer celebrates real achievement and stays silent on unresolved outcomes.
- The cold attempt is unscored — the product invites you to struggle without judging the struggle.

A learner who uses this product for a month should be able to look at their graph and trust that every solidified node represents something they can actually reconstruct from memory. That trust is the product's most valuable asset.

## Positioning: Dark Souls For Your Brain

The deepest emotional analogy for socratink is not a generic dungeon crawler or a puzzle game. It is the FromSoftware design philosophy — Dark Souls, Bloodborne, Elden Ring — where difficulty is respect, mastery is earned, and the system never lies to you about whether you won.

The mapping is structural, not decorative:

**The boss doesn't get easier because you died.** Dark Souls never secretly lowers a boss's health after five failed attempts. The boss is the boss. You either learned its patterns or you didn't. socratink does the same — the graph doesn't fudge a node to `solidified` because you tried hard. The mechanism is the mechanism. You either reconstructed it from memory or you didn't.

**Dying is data, not failure.** Every death teaches you which attack you didn't dodge, which phase you weren't ready for. Every non-solid re-drill teaches you which causal link broke, which step you conflated, which connection you couldn't reconstruct. You respawn at the bonfire. The node stays `drilled`. The boss is still there, unchanged, waiting. That's not punishment — that's information.

**Learning the patterns = studying your specific gap.** After a death in Bloodborne, you don't reread the entire strategy guide. You think about the specific move that killed you. The study revisit does the same — it reopens with a different framing, targeted at the gap you just revealed. You're not restudying the whole mechanism. You're studying what killed you.

**Summoning help ≠ winning for you.** In Soulsborne you can summon, but you still fight. The summon doesn't beat the boss for you. In socratink, the AI ramps up scaffolding after repeated failures, but `solid` still requires the learner to reconstruct the full mechanism independently. The help gets you closer. You still cross the threshold yourself.

**"Git gud" = the mastery bar never lowers.** The Soulsborne community ethos is that the game respects you by not patronizing you. The difficulty *is* the respect. socratink does the same. The graph tells the truth because it respects you enough not to lie. And the feeling when you finally solidify a node you've failed three times — "I did it. It's real. No one helped me." — is the exact emotional register the product is designed to produce.

**Explaining it to a five-year-old = owning the mechanism.** If you can teach the mechanism to someone with no context, you don't just remember it — you own it. That's the Feynman test. That's the generation effect at its peak. That's why the re-drill periodically asks "explain this to a confused beginner." If you can do that from memory, the node is solidified — not because you memorized words, but because you built the structure.

### Why This Matters For Positioning

"Dark Souls for your brain" is a positioning line that immediately communicates three things to the right audience:

1. This will be hard.
2. The difficulty is the point.
3. The payoff is real because the system doesn't lie.

The audience who resonates with this — people who *want* to earn it, who distrust easy wins, who feel insulted by participation trophies — is socratink's primary learner. They already know that fluency is not competence. They are looking for a product that agrees with them.

This positioning also serves as a filter: learners who want the AI to do the work for them will self-select out. That is correct behavior. socratink is not for everyone. It is for people who want the truth about what they know, even when the truth is hard.
