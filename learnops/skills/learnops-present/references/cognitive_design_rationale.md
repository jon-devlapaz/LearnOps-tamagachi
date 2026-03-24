# Cognitive Design Rationale v2

This document maps empirically validated cognitive science principles to specific dashboard design decisions. Every design rule in the runtime contract exists because of how human cognition processes visual information under limited attention.

Read this before every generation run. When you understand *why* a rule exists, you comply with its intent — not just its letter — and handle edge cases correctly without additional instructions.

The source research is Richard Mayer's multimedia learning theory, validated across 200+ experimental comparisons.

---

## Stage 2 Pipeline Context

This dashboard is Stage 2 (Presentation) of a four-stage learning pipeline:

**Stage 1 → Stage 2 → Stage 3 → Stage 4**
Extraction → **Presentation** → Feynman Drilling → Consolidation

Stage 1 (learnops-extract) recovers the conceptual skeleton: backbone principles, functional clusters, sub-nodes, cross-cluster relationships, prerequisite chains, and knowledge gaps.

Stage 2 (this skill) renders that skeleton as a navigable surface the learner studies before drilling. The dashboard is the learner's **last passive exposure** to the material before they must generate understanding from memory in Stage 3.

Stage 3 (learnops-drill) probes the learner's understanding node-by-node, cluster-by-cluster. The drill protocol:
- Asks the learner to rate each node: solid / fuzzy / shallow
- Forces recall and Feynman-style explanation without notes
- Classifies gaps as Shallow, Deep, or Misconception
- Deploys matched remediation

**What this means for dashboard design:** The dashboard must make every drillable unit visible, identifiable, and self-assessable. If the learner can't look at the dashboard and think "I understand this card but not that one," the dashboard has failed its Stage 2 function — regardless of how good it looks.

---

## The Core Constraint: Limited Cognitive Capacity

The human mind processes visual and verbal information through two separate channels, each with severely limited capacity. All dashboard design decisions flow from this single biological reality.

**Design implication:** Every element on screen either supports comprehension or competes for the same limited resources. There is no neutral — every pixel either helps or hurts.

---

## Principle-to-Rule Mapping

### 1. Spatial Contiguity → Co-locate labels with referents

**Research:** Placing printed words next to the part of a graphic they describe (rather than in a separate caption or legend) improved transfer in 22/22 tests with effect size >1.0. This is the largest and most consistent effect in multimedia learning research.

**Dashboard rules this generates:**
- Relationship sections must use **actual concept names inline** with each relationship, not legend-style references like "C1 → C2" that force the reader to scroll back and decode.
- Card titles must be immediately adjacent to card content — no intermediate chrome that separates the label from what it describes.
- Metadata chips in the sidebar must be self-explanatory at point of use, not dependent on a key elsewhere.
- Anchor jumps from related-concept chips must take you directly to the referenced content, not to a separate index.

**Stage 2 implication:** Cross-cluster relationship cards are how the learner builds their mental model of how clusters connect. If the labels require cross-referencing, the learner wastes capacity on navigation instead of integration. Every relationship label must be self-contained and clickable.

**When generating:** Every time you create a label that references something elsewhere in the dashboard, ask: *does the reader have to hold this label in working memory while searching for its referent?* If yes, co-locate or create a direct jump.

---

### 2. Coherence → Remove everything that doesn't serve comprehension

**Research:** Removing interesting but irrelevant "seductive details" improved learning in 23/23 experiments with median effect size 0.86. Adding engaging content that doesn't serve the learning objective reliably *hurts* understanding by consuming limited capacity.

**Dashboard rules this generates:**
- No invented sections, filler prose, or decorative elements.
- No epistemic legends or claim taxonomies unless the source explicitly contains them.
- No charts for concept-only material — a chart with no numeric evidence is a seductive detail.
- No decorative gradients, glassmorphism, icon grids, or visual spectacle.
- No duplicate metadata (sidebar AND overview showing the same thing).
- Omit empty or weak sections entirely rather than creating shells.

**Stage 2 implication:** The learner is about to be drilled. Every element that doesn't represent a drillable concept, a structural relationship, or a navigation aid is actively harming their preparation. The dashboard should contain exactly the knowledge architecture and nothing else.

**When generating:** Before adding any element, ask: *does this direct the reader's attention toward understanding the knowledge map's conceptual structure, or does it consume attention without aiding comprehension?* If the latter, cut it.

---

### 3. Signaling → Direct attention to structural hierarchy

**Research:** Highlighting important information (headings, bold, color, arrows) improved transfer in 24/28 studies with effect size 0.4. When extraneous material can't be fully eliminated, signaling directs the selection process.

**Dashboard rules this generates:**
- ⭐ backbone items get visual prominence — lead cards or primary-color callouts in the overview.
- 🔑 key takeaways get callout treatment with accent styling.
- ⚠ constraints and warnings get distinct warning styling.
- 🔍 knowledge gaps get follow-up card treatment near the end.
- Active navigation state must be visually unambiguous (strong contrast, not subtle tint).
- Section headings must create clear visual hierarchy — the reader should instantly distinguish H2 (section) from H3 (sub-topic) from body text.

**Stage 2 implication:** The visual hierarchy maps directly to drill priority:
1. **Backbone** — the structural claims the drill stress-tests first and most aggressively
2. **Cluster principles** — the governing mechanisms the drill probes at the cluster level
3. **Sub-nodes** — the independently assessable concepts the drill probes individually
4. **Knowledge gaps** — the boundaries where the drill does not probe

If signaling is flat (everything looks the same), the learner can't build a priority model of what matters most.

**When generating:** The emoji markers in the source note ARE the author's signaling system. Translate them into visual emphasis that preserves their relative weight — not flatten them into uniform cards.

---

### 4. Redundancy → Don't present the same information twice in competing channels

**Research:** Adding on-screen text that duplicates narration hurt learning in 16/16 tests. Redundant information in the visual channel competes with graphics for limited visual processing capacity.

**Dashboard rules this generates:**
- Do not duplicate metadata in both the sidebar dossier AND the overview section.
- Do not repeat the framing paragraph in both the overview and the first content section.
- If backbone items appear as overview lead cards, they should not also appear verbatim at the top of the Backbone section — link to the section instead.
- Related concept chips should jump to their target, not duplicate the target's content inline.

**Stage 2 implication:** Redundancy creates the illusion of density without adding information. The learner mistakes "I've seen this twice" for "I understand this." This is especially dangerous before drilling, where false confidence leads to shallow self-assessment.

**When generating:** After completing the HTML, scan each piece of information: *does this appear in two places where both are visible or adjacent?* Remove the duplication — keep it where it has the most structural value.

---

### 5. Segmenting → Let the reader control pacing

**Research:** Breaking continuous presentation into learner-paced segments improved transfer in 10/10 tests. Allowing the reader to digest one part before moving to the next dramatically helps comprehension of complex material.

**Dashboard rules this generates:**
- Exactly one content section visible at a time. This is the dashboard's primary segmenting mechanism.
- Navigation switches sections deterministically — the reader chooses what to process next.
- Long prose within a section should be split into cards or grouped panels (sub-segments).
- The overview should be a lightweight entry point, not a wall of text that front-loads everything.

**Stage 2 implication:** Knowledge maps are dense by design — they compress an entire conceptual architecture into 25–50 nodes. Without segmenting, the learner sees the full map at once, which overwhelms working memory and produces the "I read it but I don't know what I read" experience. Single-section visibility forces cluster-by-cluster processing, which mirrors how the Feynman drill probes understanding.

**When generating:** The single-section-visible constraint is the most important structural decision in the dashboard. It is not a UI preference — it is the cognitive mechanism that prevents capacity overload. Never violate it.

---

### 6. Pre-training → Introduce key concepts before explaining their relationships

**Research:** Teaching component names and identities before explaining how a system works improved transfer in 13/16 tests with effect size 0.75. When learners already recognize vocabulary, they can devote full capacity to understanding mechanism.

**Dashboard rules this generates:**
- The overview section should include backbone cards that introduce the map's core concepts before the reader enters the detail sections.
- The sidebar dossier with metadata (tags, difficulty, backbone array) functions as ambient pre-training — it orients the reader to the conceptual territory before they start navigating.
- Prerequisite chains should be presented in learning order (which the source note already provides), not rearranged for visual convenience.

**Stage 2 implication:** The overview is not a summary — it is pre-training for the detail sections, which are themselves pre-training for the drill. The pipeline is: overview orients → sections build the model → drill verifies the model. Skip or bloat the overview and you weaken the entire chain.

**When generating:** Keep the overview under 150 words of prose. If there are 3+ backbone items, render as compact cards. The overview succeeds when the learner can navigate into any detail section and immediately recognize the territory.

---

### 7. Graphic Simplicity → Restrained design outperforms polished complexity

**Research:** Simple line drawings outperformed detailed illustrations and photographs for explaining how systems work. Realistic detail introduces extraneous visual complexity.

**Dashboard rules this generates:**
- Editorial restraint over production polish. The dashboard should feel like an evidence desk, not a startup landing page.
- Cards use borders, not heavy shadows. Surfaces are calm neutrals, not gradient spectacles.
- Color is role-based and sparse — primary for active state and key emphasis, accent for secondary emphasis. Never decorative rainbow palettes.
- Typography is fixed (Inter) and hierarchical. No display fonts, no oversized hero text.
- The "sameness test": if the dashboard could be mistaken for a generic SaaS admin template after removing content, the design has failed. Restrained ≠ generic.

**Stage 2 implication:** Visual spectacle is the graphic equivalent of seductive details. A learner who thinks "this looks impressive" is not the same as a learner who thinks "I can see the six clusters and how they connect." Optimize for architectural visibility, not aesthetic impact.

**When generating:** Production quality is not pedagogical quality. A beautiful dashboard that obscures the conceptual structure is worse than a plain one that makes every node and relationship obvious.

---

### 8. Temporal Contiguity → Keep related information accessible simultaneously

**Research:** Presenting corresponding words and graphics at the same time (rather than sequentially) improved transfer in 9/9 tests.

**Dashboard rules this generates:**
- When a relationship section references two concepts, both should be accessible from the relationship card — via anchor jumps, not by requiring the reader to navigate away and return.
- Related concept chips should be interactive when meaningful targets exist — the connection between "this reference" and "that content" should be traversable without losing context.
- Jump behavior: when clicking a reference, reveal the correct section AND scroll to the target AND briefly highlight it. Don't just switch sections and leave the reader searching.

**Stage 2 implication:** Cross-cluster relationships are where the deepest understanding lives. If the learner can't traverse a relationship in one click — seeing both the source and target concepts — they can't build the integrated mental model that the Feynman drill will test. Every untraversable cross-reference is a potential gap the drill will expose that the dashboard failed to prevent.

**When generating:** Every cross-reference in the dashboard is a temporal contiguity decision. The reader should never have to hold a concept in working memory while navigating to its referent.

---

## The Priority Hierarchy

These principles form a design priority chain, not an unordered checklist:

1. **Coherence** (remove waste) — must be satisfied first
2. **Signaling** (direct attention) — once waste is cleared, guide the eye
3. **Segmenting** (control pacing) — once attention is directed, prevent overload
4. **Spatial contiguity** (co-locate) — within each segment, keep related things together
5. **Pre-training** (orient first) — the overview enables everything that follows
6. **Redundancy** (don't duplicate) — after building, prune what appears twice
7. **Graphic simplicity** (restrain design) — throughout, resist the pull toward spectacle

This mirrors Mayer's own processing hierarchy: reduce extraneous processing → manage essential processing → foster generative processing.

In pipeline terms: **Coherence clears the channel → Signaling and Segmenting manage the load → Pre-training, Spatial Contiguity, and Temporal Contiguity foster the integrated mental model the drill will verify.**

---

## Quick Diagnostic

When a generated dashboard feels "off" but you can't pinpoint why, check these in order:

| Symptom | Likely violated principle | Fix |
|---|---|---|
| Feels cluttered despite correct content | Coherence — something is there that shouldn't be | Remove decorative elements, duplicate info, empty shells |
| Reader can't find what they're looking for | Signaling — hierarchy is flat | Strengthen visual distinction between H2/H3/body, add emphasis to markers |
| Reader feels overwhelmed | Segmenting — too much visible at once | Verify single-section constraint, break long sections into cards |
| Reader has to scroll back and forth | Spatial contiguity — labels separated from referents | Co-locate relationship labels, add anchor jumps |
| Overview feels redundant with first section | Redundancy — same info in two places | Keep overview as pre-training only, remove duplicated content |
| Dashboard looks generic | Graphic simplicity interpreted as "plain" | Add editorial hierarchy — restraint should feel intentional, not default |
| Can't tell which cards are drillable | Signaling — sub-nodes and prose look identical | Distinguish H3 cards from cluster intro, add visual boundaries |
| Prerequisite chain doesn't feel ordered | Sequence rendering — flat or unordered treatment | Use timeline/step component, never bullet lists for sequences |
| Cross-cluster relationships feel disconnected | Temporal contiguity — links aren't traversable | Add clickable references with jump behavior |
