---
name: learnops-extract
description: "Stage 1 of the LearnOps pipeline. Extracts a structural knowledge map from a YouTube transcript or raw text, recovering causal architecture rather than topic lists. Writes a standalone .md file to the vault's Staging folder. Trigger when the user provides a text/URL and asks to 'map this video', extract knowledge, or create a concept map."
license: Apache-2.0
metadata:
  author: jonsthomas
  version: "1.0"
  pipeline-stage: "1"
---

## WHAT THIS IS

A transcript is a monologue shaped by rhetoric, not logic. This skill recovers the **conceptual architecture** beneath the surface and renders it as a standalone knowledge map.

Output: a `.md` file written to the vault's Staging folder at:
`/Users/jonathandelapaz/Desktop/Obsidian Vault/Staging/`

The map is **not integrated into the knowledge graph at creation time.** No wikilinks. No MOC routing. No framework catalog updates. No graph compounding. The map is a raw extraction — a deposit that must be earned through drilling and gap closure before it enters the graph.

Three objectives drive every output:
1. **Knowledge Architecture** — model the speaker's conceptual system, not their talking points
2. **Extraction Quality** — backbone principles, mechanism-level cluster labels, and functionally independent sub-nodes that support downstream Feynman drilling
3. **Applied Leverage** — transferable frameworks and decision implications. When the source material is domain-relevant to the user's work, include concrete career applications. When the source is general knowledge, keep the leverage section focused on broadly transferable frameworks.

---

## REFERENCE FILES

Consult these files in the `references/` folder for detailed guidance on judgment-heavy steps:

- **`cluster-and-subnode-examples.md`** — Good/bad cluster label examples with reasoning, Step 3b decomposition decisions with worked examples showing when to decompose vs. keep as prose, and a decision flowchart. **Read when executing Steps 3 and 3b.**
- **`gold-standard-output.md`** — A complete annotated knowledge map showing target quality with `<!-- ANNOTATION -->` comments explaining every structural choice. **Skim before writing output to calibrate quality expectations.**
- **`output-templates.md`** — The FULL and COMPRESSED output format templates. **Read only when you reach the output generation stage** — not before. Choose the appropriate template based on the low-signal check from Step 1.

---

## INPUT HANDLING

**Pasted transcript:** Proceed directly to the pipeline.

**YouTube URL:** Attempt to fetch the transcript via web tools. If unavailable, instruct the user to copy the transcript from YouTube's transcript panel (click '⋯' below the video → Show transcript → copy all text). Warn that auto-fetched transcripts may lack punctuation.

**Vault transcript:** The user may reference a transcript already in the vault at `/Users/jonathandelapaz/Desktop/Obsidian Vault/transcripts/`.

**Primary method (handles all filenames including Unicode):**
1. Use `obsidian-mcp-tools:list_vault_files` with `directory: transcripts` to find the file
2. Use `obsidian-mcp-tools:show_file_in_obsidian` to open it — this is mandatory before step 3, because `get_active_file` reads whatever file is currently open in Obsidian. If you skip this step, you will read the wrong file.
3. Use `obsidian-mcp-tools:get_active_file` with `format: markdown` to read the content

**Why not Filesystem tools:** Vault filenames often contain curly quotes, em dashes, and other Unicode characters that cause Filesystem:read_file to fail with ENOENT errors even when the file exists. The Obsidian REST API handles its own filenames correctly regardless of encoding.

**Also avoid `get_vault_file`:** This tool has the same Unicode encoding issue as Filesystem tools — it fails on filenames with curly quotes or special characters. Only `show_file_in_obsidian` → `get_active_file` reliably handles all vault filenames.

If the user says something like "use the transcript about X" or "map that video I saved," list the transcripts folder and match by keyword.

**No title available (pasted text with no metadata):** Derive the filename slug from the core thesis identified in Step 2.

---

## COGNITIVE PROCESSING PIPELINE

Before writing the final `.md` file, execute the following steps sequentially inside a `<thinking>` block. This is mandatory — Steps 1 through 7 involve computationally demanding operations (thesis inference, functional clustering, relational abstraction) that require explicit chain-of-thought reasoning to avoid context flattening and shallow associative defaults on long transcripts. Do not generate the final output until all steps are complete inside the thinking block.

### Step 1 — Macrostructure Recovery

Apply Kintsch & van Dijk's three macrorules in sequence to recover the conceptual skeleton from spoken rhetoric.

**1a. Deletion** — Strip conversational filler, sponsor reads, verbal tics, false starts, redundant restatements, engagement bait, and pure transitions. In spoken monologue, also delete pedagogical scaffolding ("as I mentioned earlier," "to recap") and spontaneous conversational repair where the speaker restates to correct themselves.

**1b. Generalization** — Identify extended narrative examples, analogies, and anecdotal sequences. Replace each with the single categorical mechanism it illustrates. A 3-minute story about a specific patient becomes one sentence stating the clinical principle. Multiple examples making the same point collapse into one.

**1c. Construction** — Synthesize unstated macropropositions. Spoken monologues frequently defer or never explicitly state the governing claim of a section. When a sequence of propositions implies a structural conclusion the speaker didn't articulate, construct that macroproposition explicitly. This is thesis inference — the most cognitively demanding macrorule, and the one most transcripts require.

What remains after all three operations is the signal corpus.

**Low-signal check:** If the signal corpus contains fewer than 5 substantive claims, flag the transcript as low-density and use the compressed output template.

**Why three operations, not one:** Written prose uses paragraph breaks and topic sentences to signal macrostructure explicitly. Spoken monologue does not — it relies on intonation, discourse markers, and meandering repetition. An extractor that only deletes filler (Step 1a) without also generalizing examples (1b) and constructing unstated theses (1c) will produce a cleaner transcript, not a conceptual skeleton.

### Step 2 — Knowledge Architecture Analysis
From the signal corpus, identify:
- **Core thesis:** the single claim the entire content defends or demonstrates
- **Top-level architecture:** Determine whether the speaker's core thesis is best represented as a **Causal Chain** (A → B → C), a **Problem-Solution** framework, or a **Comparison** structure. This classification overrides the speaker's chronological delivery order and will govern how clusters are sequenced in the output. Do not default to the order the speaker presented ideas — determine the logical architecture that best represents the argument's actual structure.
- **Governing assumptions:** what the speaker takes as axiomatic without arguing
- **Speaker incentive:** what the speaker gains if the audience accepts the thesis (product, reputation, ideology). Note only if it visibly shapes the argument.
- **Key constraints:** what limits or scopes the thesis
- **Mechanisms:** how things cause other things (not just what they are)
- **Tradeoffs:** what is gained and what is sacrificed
- **Difficulty rating:** Assess content complexity for the quest tracker. **Easy** = ≤4 clusters, straightforward mechanisms, single domain. **Medium** = 5–6 clusters, cross-domain connections, moderate abstraction. **Hard** = 7+ clusters, dense causal chains, high abstraction, or requires significant prerequisite knowledge.

### Step 3 — Functional Clustering

Group concepts into primary clusters by **causal mechanism**, not by shared topic or vocabulary.

**The critical constraint:** Novices cluster by surface features — they see the same words and group them together. Experts cluster by underlying functional principles — they see the same mechanism operating beneath different vocabulary and group *that*. An LLM's default embedding-based clustering replicates novice categorization. You must override this by clustering exclusively around shared causal mechanisms and governing principles, ignoring surface-level vocabulary similarity.

**Practical test:** If a speaker uses a biological analogy to explain a software architecture concept, the analogy belongs in the software cluster (it shares the mechanism), not in a separate "Biology" cluster (it shares vocabulary). The cluster boundary wraps around the complete lifecycle of one mechanism — its cause, its process, and its effect — regardless of how widely the speaker's vocabulary ranged while describing it.

**Nucleus-satellite filtering:** Within each forming cluster, apply the RST deletion test: *"If this specific claim were deleted, would surrounding claims lose their logical coherence?"* If yes, the claim is a structural nucleus and deserves top-level representation in the cluster. If no, it is supporting evidence or elaboration (a satellite) and must be demoted to a sub-node or discarded. This prevents anecdotal scaffolding from cluttering the cluster at the same level as load-bearing mechanisms.

**Scaling rule:** Aim for ~1 cluster per distinct mechanism or thesis branch. Floor: 3. Ceiling: 7. A 10-minute focused talk should produce 3–4. A 90-minute wide-ranging interview may need 6–7.

**Cluster labels must be complete propositional sentences containing an active causal verb.** Noun-phrase labels are prohibited. The label must state the mechanism: what causes what, what restricts what, what produces what. "Neuroplasticity" fails (noun phrase, no mechanism). "Neuroplasticity requires myelination of active synapses" passes (complete proposition, active verb, states the mechanism). "Benefits of X" fails (topic frame). "X restricts Y by forcing Z" passes (causal chain in the label).

### Step 3b — Sub-Node Decomposition (Functional Independence Test)

For each cluster containing 4+ distinct concepts, test each concept: **"Can a learner assess their understanding of this concept independently of the other concepts in this cluster?"**

- If **yes** for 3+ concepts within a cluster → decompose into `####` sub-nodes. The cluster prose introduces the governing principle that unites them; sub-nodes detail the individual instantiations with a 1–2 sentence mechanism statement each.
- If **no** (concepts are tightly coupled and only meaningful together) → keep as prose with bold inline labels. No decomposition.

**The interdependence test (KLI framework):** Not all multi-concept clusters should decompose. Distinguish between:
- **Constant-constant mappings** (independent facts, rote associations, distinct instantiations of a pattern) — these decompose safely because understanding one doesn't depend on understanding another.
- **Variable-variable mappings** (interdependent mechanisms where changing one variable intrinsically alters another) — these must stay unified. Decomposing a tightly coupled system into isolated sub-nodes destroys the learner's ability to see how the variables interact, which is the actual knowledge.

**Why this exists:** The primary downstream consumer of knowledge maps is the Feynman drill protocol, which triages understanding node-by-node ("rate each: solid / fuzzy / shallow"). A cluster that bundles independently-assessable concepts into a single node forces the learner to rate a composite — hiding granular gaps. Sub-nodes restore drill granularity without breaking the cluster's semantic coherence.

**Consistency rule:** When in doubt, decompose. A false positive (unnecessary sub-node) costs only slight verbosity. A false negative (hidden composite) costs a missed gap in the Feynman session. But never decompose a variable-variable mapping — the system *is* the assessable unit.

### Step 4 — Backbone Identification
From all clusters, identify 2–4 backbone principles the entire argument structurally depends on.

**Validation test:** For each candidate, ask: *if I remove this, do multiple clusters lose their foundation?* If only one cluster is affected, it's a cluster principle, not backbone. Demote it.

### Step 5 — Relationship Mapping
Map two distinct types of relationships **between clusters only** (within-cluster relationships belong in cluster content). These map to different output sections:

**System mechanics** → output in Cross-Cluster Logic section (how the domain works):
- → causal / leads to
- ↔ bidirectional / mutually reinforcing
- ↑ amplifies
- ↓ suppresses
- ⚡ tension or tradeoff

**Learning prerequisites** → output in Prerequisite Chain section (the order a human must learn them):
- [Requires] — cognitively impossible to understand B without first mastering A

**Do not conflate these.** "A causes B" in the domain does not mean "I must learn A before B." Causation describes how a system operates; prerequisites describe how a learner must sequence their understanding. A feedback loop where A causes B and B causes A has bidirectional mechanical causality but may still have an asymmetric learning prerequisite (one side may be a simpler concept that scaffolds the other). Map both relationship types independently.

**Every relationship must be expressed as a complete proposition with an active linking verb.** Do not compress causal chains into flat topic lists. "Cluster A → Cluster B" without a verb is prohibited. "Cluster A *restricts* Cluster B by reducing X" passes. The verb is what makes the relationship a mechanism rather than an association.

**Anti-bias rule for cross-links:** To find non-obvious cross-links, you must combat your default semantic-matching bias. LLMs naturally connect clusters that share vocabulary — this replicates novice-level association, not expert-level synthesis. Instead, look for **structural analogies**: do two distant clusters share the same underlying mechanism (e.g., a feedback loop, a bottleneck, a threshold gate, diminishing returns) even though they use completely different vocabulary? Map these functional analogies explicitly. These are the cross-links that Novak's research identifies as the primary indicator of deep conceptual integration.

**Pruning rule:** After identifying all cross-cluster relationships, retain only the most direct, load-bearing causal pathways. If Cluster A connects to Cluster C both directly and indirectly through Cluster B, keep only the direct path unless the indirect path reveals a qualitatively different mechanism. The goal is a sparse network of high-value links, not a dense web of every possible connection.

### Step 6 — Framework Abstraction
Extract 1–3 transferable mental models that apply beyond this content.

**Quality gate (three tests, all required):**

1. **Decision test:** The framework must name a specific decision type it changes and a domain outside this content where it applies. "Think in systems" fails. "When evaluating X, check for Y before committing to Z" passes.

2. **Relational abstraction test (Gentner):** After drafting the framework, strip all domain-specific nouns from the source content (e.g., "neurons," "interest rates," "Kubernetes pods") and replace them with abstract system variables (e.g., "agents," "inputs," "constraints," "catalysts"). If the framework still makes sense and still changes a decision — it transfers. If it collapses into a truism without the domain nouns — it was description, not a framework. Discard it.

3. **Mechanism test:** The framework must state a causal relationship, not just a category. "There are three types of X" fails (taxonomy). "When X exceeds threshold Y, the system shifts from state A to state B" passes (mechanism with conditions and consequences).

### Step 7 — MindNode Recommendation
Assess whether this map warrants spatial visualization in MindNode. Evaluate:
- **Cross-cluster relationship count:** How many inter-cluster links from Step 5?
- **Relationship type distribution:** Primarily hierarchical (→) or lateral (↔, ⚡)?
- **Nesting depth:** Did clusters exceed 3 levels?

**Recommend MindNode if** 3+ cross-cluster tensions/bidirectional links exist AND relationships are predominantly non-hierarchical. Otherwise, recommend staying with the .md.

---

## MULTI-SPEAKER HANDLING

For interviews, panels, or debates:
- Separate the interviewer's framing from the guest's actual claims
- In debates or disagreements, identify competing theses and map each, noting where they diverge
- Attribute backbone principles to specific speakers when claims conflict

---

## CONCEPT REFERENCES

Since this map is not yet graph-integrated, **do not use wikilinks.** Write concept names as plain text. Bold key concepts on first significant use within a section for scanability, but do not use `[[brackets]]`.

When you would normally wikilink a concept, ask: is this a load-bearing mechanism or a named framework that the learner will need to recognize later? If yes, bold it on first use. If it's just a passing reference, leave it plain.

---

## OUTPUT FORMAT

**Do not read the templates until you reach this stage.** Read `references/output-templates.md` now and use the structure exactly as defined there. Choose the appropriate template (FULL or COMPRESSED) based on the low-signal check from Step 1.

---

## CONSTRAINTS

- Extract architecture, not content. Do not rewrite the transcript.
- Do not include examples unless they reveal a mechanism not stated elsewhere.
- Prefer abstraction over repetition. One precise node beats three vague ones.
- **Node count target: 25–50 headings for full output, 10–15 for compressed.** Sub-nodes from Step 3b count toward this total. This is a soft target — exceed it if the content genuinely demands more distinct nodes, but if you're above 50, verify each node carries unique structural weight. Padding is worse than density.
- Mechanism over description. How and why outrank what.
- **Cluster labels must be complete propositional sentences with active causal verbs.** Noun-phrase labels ("The Economy," "Key Brain Disorders") are prohibited. Every label must state what causes, restricts, produces, or requires what.
- Backbone must pass the multi-cluster dependency test.
- **Every cross-cluster relationship must contain an explicit linking verb.** Do not compress causal chains into flat topic lists. The verb preserves the mechanism.
- **Cross-cluster references must use shortened propositional labels, never "Cluster N" numbering.** "Role shift → Skills decay" passes. "Cluster 1 → Cluster 2" fails. The reader should never need to scroll back to decode a cluster number. If the full label is too long for inline use, compress to its core mechanism phrase (e.g., "Threshold gating → Synaptic integration" instead of the full sentence labels).
- **Prerequisite chains must be ordered by logical necessity, not chronological presentation.** Speakers present ideas in the order that makes rhetorical sense, not in the order that makes learning sense. For every proposed prerequisite link, apply the Reference Distance test: *"Is it cognitively impossible to understand the definition of Node B without first understanding the mechanics of Node A?"* If A merely provides helpful context but is not structurally required, no prerequisite exists.
- Strategic Leverage must be specific to this content, not generic advice. High-Leverage Applications section is optional — include only when the source material has clear domain-specific applications relevant to the user's work. Omit for general-knowledge content.
- No wikilinks. No graph metadata. No MOC routing. This is a staging artifact.
- Tags in frontmatter should be coarse `domain/...` filters, not topic inventories.

---

## FILE OUTPUT

Do not print the full markdown to the chat. Instead:

1. Determine the filename slug: lowercase, hyphens, no special characters. Derived from video title or core thesis. Prefix with date: `YYYY-MM-DD-slug.md`
2. Write the file directly to the vault Staging folder using Filesystem tools:
   - Path: `/Users/jonathandelapaz/Desktop/Obsidian Vault/Staging/{filename}`
3. **The vault write IS the delivery.** Do NOT copy to `/mnt/user-data/outputs/` or use `present_files` — those produce a confusing duplicate download. The file is already in the user's vault and visible in Obsidian immediately.

For transcripts exceeding ~60 minutes: note `<!-- Part [N] of [M] -->` at the top and process in thematic segments rather than chronologically.

---

## POST-OUTPUT SUMMARY

After writing the file, provide a brief summary in chat:

```
📝 Knowledge map staged: Staging/{filename}

Core thesis: [one sentence]
Backbone: [2-4 principles listed]
Clusters: [count] — [brief labels]
Difficulty: [easy|medium|hard]

⚠️ This map is staged, not graph-integrated.
   Drill it → close gaps → then promote to Knowledge Maps/ and link it.

🗺️ MindNode recommendation: [YES/NO] — [brief reason]
```