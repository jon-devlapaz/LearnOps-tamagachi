# Cluster Labels and Sub-Node Decomposition — Reference Examples

Extended decision support for Steps 3 and 3b. The core rules are in SKILL.md; this file provides concrete examples drawn from real knowledge maps to anchor judgment calls.

## Cluster Label Quality

### The Rule

Cluster labels must be **principle-level** — they state a mechanism or causal claim, not a topic. The test: does the label tell you *how* or *why*, or just *what*?

### Good Labels (from real maps)

| Label | Why it passes |
|-------|--------------|
| "Intelligence asymmetry creates compounding execution debt" | Names the mechanism (asymmetry) and the consequence (compounding debt). You know what the cluster argues. |
| "Context Architecture: Preloading Beats Discovery" | States a causal claim with a clear winner. You could disagree with this — that's a sign it has content. |
| "Emotional saturation degrades cognitive capacity at the execution threshold" | Mechanism (saturation), effect (degraded capacity), and scope (at the threshold). |
| "Quality Gate Automation: Stop Hooks as Autonomous Error-Correction Loops" | Names the specific mechanism (stop hooks) and its function (autonomous error correction). |
| "Threshold gating converts graded input into discrete, frequency-coded output" | Describes a transformation with input, output, and mechanism all in the label. |

### Bad Labels (and how to fix them)

| Bad Label | Why it fails | Fixed Version |
|-----------|-------------|---------------|
| "Key Brain Disorders" | Topic listing — tells you the category but not what the cluster argues about disorders. | "Neurological disease is dysfunction at the same structural levels that explain normal function" |
| "Benefits of Context Preloading" | "Benefits of X" is always a red flag — it's a topic frame, not a principle. | "Preloading context is always worth the token cost — front-loaded tokens eliminate per-task exploration" |
| "Planning vs. Execution" | Comparison frame without a claim. What *about* planning vs. execution? | "Plans designed in calm states fail under emotional load" |
| "Types of Neural Connections" | Taxonomy, not mechanism. The cluster would just list types without arguing anything. | "Circuit motifs are reusable building blocks that produce functionally distinct behaviors" |
| "AI Coding Tools" | Pure topic. No mechanism, no claim, no explanatory content. | "Shell Automation Layer: Aliases as Personal Leverage Multipliers" |
| "Challenges with Memory" | Vague problem framing. Which memory? What challenge? What mechanism? | "AI has no persistent memory — every session starts blind; solve this architecturally" |

### Edge Cases

**When a cluster genuinely IS a taxonomy:** Sometimes the content really is a catalog of types (e.g., neurological disorders, programming paradigms). In these cases, the label should state *what the taxonomy reveals* — the governing principle that organizes it. "Neurological disease maps onto the same structural levels as normal function" is a taxonomy organized by an insight. "List of Brain Diseases" is a taxonomy organized by nothing.

**When the speaker didn't make a causal claim:** Some content is descriptive, not argumentative. If a cluster's source material is purely descriptive, the label should state the *structural relationship* the descriptions share. "Neuron polarity creates directional information flow" works even for descriptive content about neuron anatomy because it names the architectural consequence.

---

## Sub-Node Decomposition (Step 3b)

### The Rule

For clusters with 4+ distinct concepts, test each: **"Can a learner assess their understanding of this concept independently of the others in the cluster?"** If yes for 3+ concepts → decompose into `####` sub-nodes. If no → keep as prose.

**Consistency rule:** When in doubt, decompose. False positives (unnecessary sub-nodes) cost slight verbosity. False negatives (hidden composites) cost missed gaps in the Feynman drill.

### Example: DECOMPOSE — Circuit Motifs

**Source content:** A cluster about neural circuit patterns containing feed-forward excitation, feed-forward inhibition, lateral inhibition, feedback inhibition, feedback excitation, convergence, divergence, and serial inhibitory chains.

**Independence test:**
- Can you understand feed-forward excitation without understanding lateral inhibition? **Yes.**
- Can you understand lateral inhibition without understanding feedback inhibition? **Yes.**
- Can you understand convergence without understanding divergence? **Yes** (though they're often taught as a pair, the mechanisms are independently assessable).

**Result:** 6 of 8 concepts are independently assessable → **decompose**.

**Why it matters downstream:** A learner could rate "circuit motifs" as "fuzzy" when they're actually solid on feed-forward excitation but completely shallow on lateral inhibition. The Feynman drill can't find the specific gap if the node is a composite.

**Output pattern:**

```markdown
### 4. Circuit motifs are reusable building blocks that produce functionally distinct behaviors

Despite tens of thousands of possible connection patterns, the nervous system reuses a small catalog of motifs. Complex behavior emerges from combining these simple patterns.

#### Feed-forward excitation
One neuron directly activates another — the simplest motif. The monosynaptic stretch reflex (sensory neuron → extensor motor neuron → muscle contraction) is the canonical example.

#### Feed-forward inhibition
An excitatory neuron activates an inhibitory interneuron that suppresses a target. In the stretch reflex, this simultaneously inhibits the antagonist flexor muscle to prevent competing contraction.

#### Convergence and divergence
Convergence: many presynaptic neurons contact one postsynaptic neuron. Divergence: one presynaptic neuron contacts many. Together they make circuits robust — the stretch reflex works because it's many synapses, not one.

#### Lateral inhibition
Each neuron inhibits its neighbors' downstream targets. Produces edge enhancement — neurons at perceptual boundaries fire differently, making edges sharper. Explains Mach band visual illusions.

#### Feedback (recurrent) inhibition
A neuron activates a partner that feeds back to inhibit the original — a braking mechanism. Also generates oscillatory behavior at every timescale from seconds (endogenous bursting) to 24 hours (circadian rhythms).

#### Feedback (recurrent) excitation
The postsynaptic neuron feeds back to re-activate the original — a switch. Once on, stays on. Important for memory mechanisms in the hippocampus.
```

**Note:** Convergence and divergence are kept as a single sub-node because they are almost always taught, understood, and applied as a complementary pair — separating them would create two nodes that are meaningfully incomplete without each other.

---

### Example: DO NOT DECOMPOSE — Emotional Saturation

**Source content:** A cluster about how emotions consume cognitive capacity at the moment of execution, including fear, self-doubt, imposter syndrome, overwhelm, and the spotlight effect.

**Independence test:**
- Can you understand fear at execution without understanding the spotlight effect? **Partially, but they're aspects of the same mechanism — emotional flooding consumes cognitive resources.**
- Can you assess your understanding of "imposter syndrome at execution" independently of "overwhelm at execution"? **Not really — they're all manifestations of the same underlying claim (emotional saturation degrades capacity).**

**Result:** These are tightly coupled instantiations of a single mechanism, not independently assessable concepts → **keep as prose with bold inline labels**.

**Why:** Decomposing would create sub-nodes like "#### Fear at execution" and "#### Spotlight effect" that a learner can't meaningfully rate independently. You don't "understand fear but not overwhelm" at the mechanism level — you either understand emotional saturation or you don't.

---

### Example: DECOMPOSE — Workflow Acceleration (Permissions, Tools, Parallel Agents)

**Source content:** A cluster covering permission tiers, CLI vs. MCP tool choice, multi-agent coordination, and escape-as-steering.

**Independence test:**
- Can you understand permission configuration without understanding multi-agent coordination? **Yes — completely different operational skills.**
- Can you explain CLI vs. MCP tool selection without knowing about escape-as-steering? **Yes.**

**Result:** 4 concepts, all independently assessable → **decompose**.

**Output pattern:**

```markdown
### 4. Workflow Acceleration — Reducing Friction Between Decision and Execution

Speed comes from reducing the gap between the agent's decision and its execution — through permission configuration, tool selection, parallelism, and intervention timing.

#### Permission tiers
Read actions auto-approved → write/bash actions require approval → shift+tab enables auto-accept → specific commands can be permanently approved. Tuning this safety-speed tradeoff is high-leverage.

#### CLI over MCP when possible
Well-documented CLI tools (gh, Docker, BigQuery) outperform MCP servers because the model's training data contains extensive documentation for them. MCP fills gaps for tools without CLI interfaces.

#### Multi-agent coordination
Running 2–4 instances concurrently with shared state written to markdown files. No native protocol — agents communicate through the filesystem using handoff files like ticket.md.

#### Escape as steering
Pressing escape stops the agent mid-execution for course correction. Knowing when to escape vs. letting the agent self-correct is a core orchestration skill.
```

---

### Example: EDGE CASE — Fake Action Patterns

**Source content:** A cluster about how overwhelm triggers avoidance behaviors that look productive: knowledge acquisition loops, shiny object syndrome, portfolio polishing, and the infinite strategist loop.

**Independence test:**
- Can you understand shiny object syndrome without understanding knowledge acquisition loops? **Yes — different behavioral patterns.**
- But: are they independently *assessable* in the Feynman drill sense? **Debatable.** A learner who understands one probably understands the others because they share a single governing mechanism: "substituting planning comfort for execution risk."

**Decision:** This is the judgment call the consistency rule resolves. **Decompose** — because each pattern has a distinct behavioral signature that a learner might recognize in some forms but not others. You might catch yourself in a knowledge acquisition loop but be blind to your own infinite strategist loop. The Feynman drill benefits from being able to probe each independently.

---

## Decision Flowchart for Step 3b

```
Does the cluster contain 4+ distinct concepts?
├─ NO → Keep as prose. Standard format.
└─ YES → For each concept, ask: can a learner rate their
         understanding of this independently?
         ├─ YES for 3+ concepts → DECOMPOSE into #### sub-nodes
         │   • Cluster prose states the governing principle
         │   • Each sub-node gets 1–2 sentence mechanism statement
         │   • Tightly coupled pairs can share a sub-node
         └─ NO (concepts are aspects of one mechanism) → KEEP AS PROSE
             • Use bold inline labels for the instantiations
             • The cluster IS the assessable unit
```

**When in doubt:** Decompose. The Feynman drill can always skip sub-nodes that turn out to be trivially linked. It cannot recover from a composite that hides a specific gap.
