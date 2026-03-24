# Output Templates

These templates define the structure for the final knowledge map output. **Read this file only when you reach the output generation stage** — not during signal extraction, clustering, or analysis.

Choose the appropriate template based on the low-signal check from Step 1.

---

## OUTPUT FORMAT — FULL

Use when signal corpus has 5+ substantive claims.

```
---
created: YYYY-MM-DD
source: "[Video Title](YouTube URL if available)"
type: knowledge-map
tags:
  - domain/[primary-domain]
  - domain/[secondary-domain-if-truly-needed]
backbone:
  - "backbone principle 1"
  - "backbone principle 2"
difficulty: easy|medium|hard
mindnode_recommended: true/false
---

# Video Title — Conceptual Frame

One sentence: the core thesis this content defends or demonstrates.

## ⭐ Backbone

The 2–4 load-bearing principles the entire argument depends on. If any are wrong, everything else falls.

### ⭐ Backbone Principle 1

One sentence stating the principle and why it is structurally foundational. Bold key concepts on first use like **concept name** when they are load-bearing mechanisms or named frameworks, but only on first significant appearance.

### ⭐ Backbone Principle 2

One sentence.

## Concept Clusters

The primary semantic groupings — divergent aspects of the subject, not a topic list.

### Cluster 1: Principle-Level Label

One sentence framing what this cluster represents and its internal logic.

- **Sub-concept or mechanism:** One sentence explaining the mechanism. Use → ↔ ⚡ inline for causal direction.
- **Sub-concept or mechanism:** One sentence.
- ⚠ **Constraint:** One sentence on what limits this cluster's applicability.

### Cluster N: Principle-Level Label (decomposed — concepts are independently assessable)

One sentence: the governing principle that unites the sub-nodes below.

#### Sub-Node A: Concept Name

1–2 sentences: what this concept is, how it works mechanically, and its functional role within the cluster.

#### Sub-Node B: Concept Name

1–2 sentences.

#### Sub-Node C: Concept Name

1–2 sentences.

- ⚠ **Constraint:** One sentence on what limits this overall cluster's applicability.

(Continue for 3–7 clusters total. Only clusters that pass the Step 3b functional independence test use #### sub-nodes. Others use the standard bullet format above.)

## Cross-Cluster Logic

Relationships between clusters (not within them). This maps **system mechanics** — how the domain actually works, NOT how the speaker structured their argument:

- **[Shortened cluster mechanism phrase] → [Shortened cluster mechanism phrase]:** One sentence explaining the mechanical cause-and-effect (e.g., "High task complexity disables semantic similarity retrieval"). Use mechanical verbs (*causes, disables, restricts, amplifies, degrades*). Do NOT use rhetorical verbs (*explains why, motivates, leads the reader to*). Use the cluster's core mechanism phrase as the label, never "Cluster N" numbering — the reader should never need to scroll back to decode a reference.
- **[Shortened cluster mechanism phrase] ⚡ [Shortened cluster mechanism phrase]:** One sentence explaining the mechanical tension.

## Prerequisite Chain

The order in which understanding should be built — based on logical necessity, not the order the speaker presented. This maps **learning prerequisites** — the order a human must learn concepts, which may differ from causal order.

1. **Foundation — [Concept/Cluster Name]:** The concept everything else depends on. It is cognitively impossible to understand what follows without this.
2. **[Requires Foundation] — [Concept/Cluster Name]:** What this adds and why it structurally needs the prior step.
3. **[Requires Above] — [Concept/Cluster Name]:** The conclusion or application layer.

## Strategic Leverage

Transforming passive learning into applied capital.

### 🔑 Framework Name 1

One sentence: the transferable model, the decision type it changes, and a domain outside this content where it applies.

### 🔑 Framework Name 2

One sentence.

### High-Leverage Applications

- **Application 1:** Where and how this applies in work, leadership, or systems.
- **Application 2:** One sentence.

### Decision Implications

- **Implication 1:** What should change in how you act or think.

### Signal of Expertise

- **Beginners:** The common misunderstanding or surface-level view.
- **Experts:** What experts actually see or do differently.

## Meta-Level Analysis

What the model assumes, what would break it, where it fails.

- **Governing Assumptions:** What the speaker takes as axiomatic without arguing.
- **Speaker Incentive:** What the speaker gains if you accept the thesis. Omit if no visible bias.
- **What Would Falsify This:** What evidence or condition would break the thesis.
- **Where It Breaks Down:** Scope limits, edge cases, or failure modes.

## 🔍 Knowledge Gaps

Load-bearing unknowns — places where the speaker's argument depends on a claim they didn't defend. Not "related topics."

- → **Learn: Topic 1** — Why this gap matters and what understanding it would unlock.
- → **Learn: Topic 2** — One sentence.
- → **Learn: Topic 3** — One sentence.
```

---

## OUTPUT FORMAT — COMPRESSED

Use when the low-signal check triggers (fewer than 5 substantive claims).

```
---
created: YYYY-MM-DD
source: "[Video Title](YouTube URL if available)"
type: knowledge-map
tags:
  - domain/[primary-domain]
backbone:
  - "backbone principle 1"
difficulty: easy|medium|hard
mindnode_recommended: false
---

# Video Title — Conceptual Frame

One sentence: the core thesis.

## ⭐ Backbone

### ⭐ Backbone Principle 1

One sentence.

## Key Mechanisms

The substantive claims worth retaining, without artificial clustering.

- **Mechanism 1:** One sentence.
- **Mechanism 2:** One sentence.

## Strategic Leverage

### 🔑 Framework Name

One sentence: transferable model and where it applies.

### Decision Implication

One sentence: what should change in how you act or think.

## Meta-Level Analysis

- **What Would Falsify This:** One sentence.
- **Where It Breaks Down:** One sentence.
```