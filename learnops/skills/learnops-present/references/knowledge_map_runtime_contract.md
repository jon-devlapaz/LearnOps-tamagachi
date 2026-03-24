# Knowledge Map Runtime Contract v3

Use this file for actual generation runs.

It is the binding runtime contract for turning a structured knowledge-map markdown note into a single-file HTML study-guide dashboard.

This contract distills and replaces the need to attach `style_spec.md`, `source_profile.md`, and `dashboard_profile.md` during normal generation. Those files remain available in `references/` for debugging only.

## 0. Pipeline Context

This dashboard is **Stage 2 (Presentation)** of a four-stage neurocognitive learning pipeline:

1. **Extraction** — recovers conceptual architecture from raw text (learnops-extract)
2. **Presentation** — renders maps as navigable study surfaces ← **this skill**
3. **Gap Detection & Repair** — Socratic Feynman drilling to find and fix mental model gaps
4. **Consolidation** — spaced verification and surgical remediation after sleep

The dashboard's job is not to look good. Its job is to **render the knowledge architecture as a surface the learner can internalize before drilling**. Every design decision must serve this downstream handoff:

- Each drillable node must be visually distinct and independently identifiable — the learner needs to self-assess "do I understand THIS concept?" by scanning the dashboard before entering Stage 3.
- The prerequisite chain IS the drill order. It must be visually prominent and obviously sequential.
- Backbone principles must dominate — they are the structural claims the drill will stress-test first.
- Knowledge gaps must be explicit — they signal where the map's authority ends and the learner should not yet be drilled.
- Cluster boundaries must be obvious — the drill protocol triages understanding cluster-by-cluster.
- Sub-nodes (H3 concepts decomposed for independent assessment) must be visually distinguishable from cluster-level prose — they are the granular units the Feynman drill probes.

## 1. Output Rules

- Return exactly one complete HTML5 document and nothing else.
- Use a single-file app with inline CSS and inline JavaScript.
- Use vanilla JavaScript only.
- Use Tailwind CSS via CDN.
- Use semantic landmarks: `nav`, `main`, `section`, headings, lists, buttons, and tables when needed.
- Use Inter for typography.
- Keep the output restrained, editorial, and study-friendly.

If you use a chart, use Chart.js via CDN.
If the note does not clearly need a chart, do not include Chart.js.

## 2. Default Configuration

Unless explicitly overridden, use:

- display mode: `study-guide`
- navigation: `sidebar`
- density: `standard`
- interpretation level: `minimal`
- charts: `0`

Do not spend time inferring defaults if they are unspecified. Apply these defaults automatically.

## 3. Source Parsing

Parse the note in this order:

1. YAML frontmatter
2. H1 title
3. opening framing paragraph
4. H2 sections
5. H3 subsections
6. bullet and numbered lists
7. wiki-links and semantic markers

Normalize:

- raw YAML into metadata
- `[[wiki-links]]` into readable labels
- `⭐`, `⚠`, `🔑`, `🔍`, and `→ Learn:` into emphasis cues, not literal markup

Never render raw YAML or raw wiki-link syntax.

## 4. Section Strategy

Use this section strategy by default:

1. Overview
2. one main section per strong H2 heading, in source order

Rules:

- preserve H2 wording where possible
- preserve H2 order unless the note is clearly too granular
- keep `Knowledge Gaps`, `Next Learn`, or equivalent follow-up material near the end
- treat H3 headings as grouped blocks inside their parent section, not as top-level nav items
- keep exactly one main section visible at a time — this is the primary cognitive segmenting mechanism that prevents capacity overload on dense maps (Mayer: segmenting, 10/10 studies)

If the source already contains headings such as `Backbone`, `Concept Clusters`, `Cross-Cluster Logic`, `Prerequisite Chain`, `Strategic Leverage`, `Meta-Level Analysis`, or `Knowledge Gaps`, keep those headings instead of remapping them.

## 5. Required Behavior

### Overview

The overview is pre-training — it orients the learner to the conceptual territory before they navigate detail sections (Mayer: pre-training, effect size 0.75). It is not a summary and not a replacement for the detail sections.

Must include:

- visible note title
- opening framing paragraph when available — keep under 150 words; beyond this, the overview becomes a wall of text that violates segmenting
- optional lead idea cards when the note provides a `backbone` array or a strong lead section — render backbone items as compact cards, not full paragraphs, when there are 3 or more

Must not:

- duplicate the full metadata block already shown in the sidebar — presenting the same information in two adjacent channels wastes visual processing capacity (Mayer: redundancy, 16/16 studies)
- explain the transformation process
- add a claim taxonomy or legend

### Source Sections

Each strong H2 heading should become a main dashboard section. Within each section, H3 subsections are the primary drillable units — they must be visually distinct so the learner can self-assess comprehension at the node level before entering Stage 3.

Must:

- keep the original H2 heading text
- split long prose into readable paragraphs or cards
- render H3 subsections as individually identifiable cards or grouped panels with clear boundaries — each card represents one concept the Feynman drill can probe independently
- preserve the relationship between each H3 block and its parent H2 section
- distinguish H3 sub-node cards from cluster-level introductory prose — the intro states the governing principle; the cards detail the independently assessable instantiations

### Relationship Sections

If the source contains a section such as `Cross-Cluster Logic`, relationship bullets, or explicit concept-to-concept links:

- preserve that section as a relationship section
- label each relationship with the actual source concept names being connected
- use human-readable chips or labels such as `Emotional saturation → Fake action patterns`

Do not use internal shorthand such as `C1 -> C2`, `Cluster 1`, `A -> B`, or similar placeholder IDs in the final UI — forcing the reader to cross-reference a legend wastes the same working memory they need for understanding the relationships (Mayer: spatial contiguity, effect size >1.0, 22/22 studies).

### Sequence Sections

If a section is explicitly ordered, preserve that visually. The prerequisite chain is the drill order for Stage 3 — it must be unambiguously sequential.

Required treatment — use one of:

- vertical timeline with numbered steps, connecting lines, and dependency labels
- numbered cards with explicit step connectors
- ordered rail with visual flow direction

Canonical Tailwind pattern for the sequence component:

- container: `space-y-0` (no gap — connection lines bridge steps)
- each step: a card with a numbered indicator, step title, and dependency label
- connector: a vertical line or border-left between steps using `border-l-2 border-slate-300` with padding to indent the step content
- step indicator: `flex items-center justify-center w-8 h-8 rounded-full bg-[PRIMARY_HEX] text-white text-sm font-bold` positioned to overlap the connector line
- step content: standard card classes adjacent to the indicator

Do not flatten sequence into an unordered card pile. Do not render prerequisite chains as plain bullet lists.

### Follow-Up Sections

If the source includes explicit open questions, `→ Learn:` items, or knowledge gaps, keep them visible near the end as:

- follow-up cards
- next-learn lists
- question blocks

Knowledge gaps mark the boundary of the map's authority. They signal to the learner what NOT to expect from Stage 3 drilling — these are open questions, not comprehension failures.

## 6. Shared Scaffolds

These are required:

- compact sidebar dossier
- deterministic section navigation
- source-first overview
- section-level anchors for all H2 sections
- card-level anchors for all H3 subsections — this enables relationship chips and related concept chips to deep-link to specific concepts, not just section tops (Mayer: temporal contiguity, 9/9 studies)

These are allowed:

- compact metadata chips
- related concept chips (limit to 6–8 — more becomes visual noise that violates coherence)
- small warning or key-takeaway callouts derived from source markers

These are not allowed by default:

- epistemic legends
- reader prompts
- synthetic section signals
- invented summary taxonomies

## 7. Charts

Default to zero charts.

Only use charts if the note contains genuine numeric evidence such as:

- numeric trends
- counts
- percentages
- ranked quantitative comparisons

Do not chart:

- concept clusters
- framework bullets
- knowledge gaps
- relationship lists
- list length

A chart with no numeric evidence is a seductive detail that consumes attention without aiding comprehension (Mayer: coherence, 23/23 studies).

## 8. Sidebar Rules

The sidebar should contain:

- compact dossier metadata
- section navigation
- related concepts or related notes in compact form when present

The sidebar functions as ambient pre-training — it orients the learner to the map's scope, difficulty, and domain before they start reading. Keep it compact.

Do not let the sidebar become a duplicate of the overview.

## 9. Anchor and Deep-Link Rules

### Anchor Granularity

Create anchors at two levels:

- **Section anchors** for every H2 section: `id="section-slug"`
- **Card anchors** for every H3 subsection rendered as a card: `id="card-slug"`

Use kebab-case slugs derived from the heading text.

### Jump Behavior

When a chip, relationship label, or overview card links to an anchor:

1. Switch to the correct section (reveal it, hide others)
2. Scroll to the specific card anchor within that section
3. Briefly highlight the destination card (subtle background pulse, `200ms` fade, then settle)

This three-step sequence ensures the reader never has to hold a reference in working memory while searching for its target (Mayer: spatial contiguity + temporal contiguity).

### Relationship Card Links

In relationship sections, each relationship card should contain clickable references to both connected concepts. Clicking either reference executes the jump behavior above. If a concept is a cluster-level heading (H2), jump to the section. If it's a sub-node (H3), jump to the specific card within its parent section.

## 10. Anti-Patterns

- Do not make the first screen about the transformation process.
- Do not duplicate metadata in both sidebar and overview unless essential.
- Do not add `Fact / Inference / Speculation` labels or any similar claim taxonomy.
- Do not invent bridge, leverage, or meta-analysis sections if the source does not contain them.
- Do not use internal shorthand such as `C1 -> C2` for relationship labels when the note provides the actual concept names.
- Do not add reader prompts or study questions unless explicitly requested.
- Do not add charts to concept-only material.
- Do not explain your reasoning before or after the HTML.
- Do not render H3 sub-nodes identically to cluster-level prose — the learner must visually distinguish "governing principle" from "individually drillable concept."
- Do not render prerequisite chains as unordered content — sequence is the information.

## 11. Generation Strategy

Do not invent the dashboard structure from scratch each run.

Instantiate the same stable shell, then fill it from the source note in this order:

1. normalize metadata
2. build the overview from the title, framing paragraph, and optional backbone items (compact cards if 3+, max ~150 words of prose)
3. create one main section per strong H2 in source order
4. render H3s as individually identifiable cards inside their parent section — each card gets a card-level anchor
5. resolve relationship labels into actual source concept names when applicable
6. create clickable references in relationship cards that execute section-switch + scroll + highlight
7. render prerequisite chains using the sequence component (timeline/numbered steps), not plain lists
8. add section-level and card-level anchors to all navigable elements
9. emit final HTML

## 12. Validation Checklist

A generated dashboard passes only if all of these hold:

- note title is immediately obvious
- overview is concise (<150 words prose), does not duplicate sidebar
- H2 section order is preserved
- H3 sub-nodes are visually distinct from cluster-level prose
- each H3 card has a card-level anchor
- relationship sections use actual concept names, never shorthand
- relationship cards contain clickable references that execute jump behavior
- prerequisite chain renders as a visually sequential component
- knowledge gaps are explicit and near the end
- related concept chips are interactive when anchors exist, capped at 6–8
- no epistemic legend, no reader prompts, no invented sections
- no charts unless genuine numeric evidence exists
- single-section visibility is enforced
- the dashboard could not be mistaken for a generic SaaS admin template
