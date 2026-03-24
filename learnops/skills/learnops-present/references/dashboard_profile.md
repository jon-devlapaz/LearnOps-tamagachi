# Output Profile: Knowledge-Map Study-Guide Dashboard v3

## Status

This is the current stable output profile for turning Obsidian-style knowledge-map notes into a single-file HTML dashboard.

It formalizes what has already been tested in live artifacts and should be treated as the default profile for notes shaped like:

- YAML frontmatter
- one strong H1
- a backbone or thesis section
- concept clusters
- synthesis or cross-links
- prerequisites, leverage, caveats, and knowledge gaps

Use this profile with:

- [style_spec.md](style_spec.md)
- [source_profile.md](source_profile.md)

## 1. Purpose

This profile narrows the master style spec into a proven dashboard grammar for conceptual markdown notes.

Its job is to serve as **Stage 2 (Presentation)** of the LearnOps pipeline: rendering extracted knowledge architecture as a navigable surface that prepares the learner for Feynman drilling in Stage 3.

The result must be:

- fast to scan — the learner builds a mental model of the map's territory before diving in
- easy to navigate — each cluster and sub-node is independently accessible
- drill-ready — every concept the Feynman drill will probe is visually identifiable as a distinct unit
- suitable for side-by-side comparison across notes

This profile is for qualitative knowledge dashboards, not KPI dashboards.

## 2. Design Intent

The dashboard should feel like an editorial study guide with light scaffolding for navigation and comprehension.

The reader should be able to answer:

- what the note is about (overview pre-training)
- what the backbone claims are (structural load-bearing principles)
- how the concepts cluster and relate (architecture visibility)
- which concepts they can assess independently (drill granularity)
- what the prerequisite order is (drill sequence)
- where the map's authority ends (knowledge gaps)

These six questions map directly to what the learner needs before entering Stage 3.

## 3. Stable Mode

This profile uses a single stable mode:

- `study-guide`

This is now the default for knowledge-map notes.

Older `reference` and `study` edition language should be treated as deprecated.

Study-guide mode includes:

- a compact overview functioning as pre-training
- a sidebar dossier functioning as ambient orientation
- section navigation with single-section visibility (cognitive segmenting)
- optional related concept chips with deep-link behavior
- faithful rendering of source sections with drill-ready node visibility

Study-guide mode does not require:

- an epistemic legend
- reader prompts
- synthetic section signals

## 4. Section Strategy

Default section strategy is:

1. Overview
2. one main section per strong H2 heading, in source order

This profile is intentionally source-first.

If the source already contains headings such as `Backbone`, `Concept Clusters`, `Cross-Cluster Logic`, `Prerequisite Chain`, `Strategic Leverage`, `Meta-Level Analysis`, or `Knowledge Gaps`, keep them and render them cleanly.

Compress only when the source is meaningfully smaller or too granular for navigation.

## 5. Section Contracts

### 5.1 Overview

The overview is pre-training, not a summary. Its cognitive function is to introduce the key concepts and scope so the learner can devote full processing capacity to understanding mechanisms when they reach the detail sections (Mayer: pre-training, effect size 0.75).

It should contain:

- the visible title
- one framing paragraph when available — keep under 150 words
- optional backbone or lead-idea cards when the note provides them — render as compact cards (not full paragraphs) when there are 3 or more

The overview must not:

- duplicate the full metadata block already shown in the sidebar (Mayer: redundancy, 16/16 studies)
- explain the source parsing process
- introduce a claim taxonomy

### 5.2 Source Sections

Each strong H2 heading should usually become a main dashboard section.

It should contain:

- the original H2 heading text
- the source prose, split into readable blocks
- H3 subsections rendered as individually identifiable cards, grouped panels, or compact callouts

**Drill-readiness requirement:** H3 sub-node cards must be visually distinguishable from cluster-level introductory prose. The intro states the governing principle that unites the cluster. The cards detail the independently assessable concepts the Feynman drill will probe. If these look identical, the learner cannot self-assess at the correct granularity.

Visual distinction pattern:
- Cluster intro: standard prose or a lightly styled context box
- Sub-node cards: bordered cards with clear titles, each with its own card-level anchor

### 5.3 Relationship Sections

If the source includes a section such as `Cross-Cluster Logic` or any explicit concept-to-concept mapping:

- preserve it as a relationship section rather than flattening it into generic prose
- label each relationship with the actual source concept names being connected
- use human-readable relationship chips or labels drawn from the source section names
- make both concept references in each relationship card clickable — clicking executes section-switch + scroll + highlight to the target concept

Do not show internal shorthand such as `C1 -> C2`, `Cluster 1`, or similar placeholder IDs when the underlying concept names are available in the note. Shorthand forces working-memory cross-referencing that wastes cognitive capacity (Mayer: spatial contiguity, effect size >1.0).

### 5.4 Sequence Sections

If the source section is explicitly ordered, preserve that visually. The prerequisite chain is the drill order for Stage 3 — it must be the most obviously sequential element in the entire dashboard.

Good candidates:

- prerequisite chains
- staged processes
- numbered dependency lists

Required treatment: use a timeline, numbered step cards with connectors, or an ordered rail. See the runtime contract §5 (Sequence Sections) for canonical Tailwind patterns.

Do not flatten sequence into an unordered card pile. Do not render as plain bullet lists.

### 5.5 Follow-Up Sections

If the source includes explicit open questions, `→ Learn:` items, or `Knowledge Gaps`, keep them visible near the end.

Normalize them into:

- follow-up cards
- next-learn lists
- question blocks

These sections mark the boundary of the map's authority and signal to the learner where Stage 3 drilling should not probe (the map doesn't cover these topics).

## 6. Shared Study-Guide Scaffolds

These elements are part of the stable profile.

### 6.1 Sidebar Dossier

The sidebar should provide:

- compact note metadata (functions as ambient pre-training — orients the learner before they read)
- section navigation
- related concepts when available

### 6.2 Related Concepts

Related concepts may be interactive when a meaningful target exists.

Preferred behavior:

- jump to the most relevant section or card-level anchor
- briefly highlight the destination

If there is no meaningful target, render the chip passively.

Limit related concept chips to 6–8. Beyond this, the chip cluster becomes visual noise that violates coherence rather than aiding navigation.

### 6.3 Source-First Presentation

Keep scaffolding light. The dashboard's job is to present the map's architecture, not to add interpretation.

Do not add:

- reader prompts
- taxonomic legends
- synthetic section takeaways unless the source already implies them strongly

## 7. Interaction Contracts

### 7.1 Navigation

- one section visible at a time (primary cognitive segmenting mechanism)
- sidebar buttons switch sections deterministically
- mobile menu closes after navigation

### 7.2 Deep Links

Use anchored jump actions for:

- overview lead-idea card → source section anchor
- related concept chip → section or card-level anchor
- relationship card concept reference → section or card-level anchor

If a jump target exists, it should be used. Deep-linking eliminates the need to hold a reference in working memory while navigating — the connection is traversable in one action (Mayer: temporal contiguity + spatial contiguity).

### 7.3 Highlight Behavior

When jumping to an anchor inside a section:

- reveal the correct section first
- scroll to the anchor
- briefly highlight the destination card (`200ms` fade, then settle)

## 8. Source-to-UI Mapping Defaults

For notes in this profile, map source structures like this:

- frontmatter → compact sidebar dossier (ambient pre-training)
- `backbone` array or backbone section → overview lead cards or first-section cards (structural emphasis)
- H2 sections → main navigation and main content sections in source order
- H3 concept groups → individually identifiable cards or grouped panels inside their parent section (drill-ready nodes)
- cluster-level intro prose → context box or standard prose above cards (governing principle)
- cross-link bullets → relationship cards with clickable concept references, using actual source names
- numbered dependency lists → sequential timeline or ordered step cards (drill order)
- leverage markers such as `🔑` → key takeaway callouts
- `→ Learn:` or `🔍` items → follow-up cards or knowledge-gap lists (map boundary markers)

## 9. Anti-Patterns

- Do not make the first screen about the transformation process instead of the note.
- Do not duplicate metadata in both the sidebar and overview unless the source makes it essential.
- Do not add a `Fact / Inference / Speculation` legend or similar taxonomy.
- Do not manufacture bridge, leverage, or meta-analysis sections when the source does not contain them.
- Do not use internal shorthand such as `C1 -> C2` or `Cluster 1` in relationship labels when the note provides the actual source concept names.
- Do not render prerequisite or sequence content as visually unordered if sequence matters.
- Do not make related concepts decorative only when a target exists.
- Do not add charts to concept-only material.
- Do not turn the study-guide profile into a workbook with invented prompts.
- Do not render H3 sub-nodes identically to cluster-level prose — the learner must visually distinguish "governing principle" from "individually drillable concept."
- Do not exceed 8 related concept chips — past this point, they become noise, not navigation.

## 10. Validation Checklist

A good output under this profile should satisfy all of the following:

**Structure**
- the note title is obvious immediately
- the overview is concise (<150 words prose) and does not duplicate the sidebar
- strong H2 section order is preserved or lightly compressed
- H3 content is grouped under the correct parent section

**Drill readiness**
- H3 sub-node cards are visually distinct from cluster-level introductory prose
- each H3 card has a card-level anchor
- prerequisite chain is rendered as a visually sequential component (timeline/steps), not an unordered list
- backbone items have the strongest visual emphasis in the overview

**Navigation and linking**
- relationship sections use actual source concept names rather than shorthand IDs
- relationship cards contain clickable references that execute jump behavior
- related concepts are interactive when anchors exist (capped at 6–8)
- deep links execute section-switch + scroll + highlight

**Constraints**
- sequence content feels sequential
- knowledge gaps and follow-up items remain explicit near the end
- no epistemic legend is added
- no reader prompts are invented
- no weak charts are introduced
- single-section visibility is enforced

## 11. Recommended Invocation

For future runs against notes of this family, treat this profile as the default output target.

Recommended configuration:

- `source profile`: `knowledge-map-markdown`
- `display mode`: `study-guide`
- `navigation variant`: `sidebar`
- `density`: `standard`
- `interpretation level`: `minimal`
- `charts`: `0`
