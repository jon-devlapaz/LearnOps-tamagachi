# Source Profile: Knowledge-Map Markdown

## Purpose

This source profile defines how to interpret Obsidian-style knowledge-map markdown files before generating a dashboard with [style_spec.md](style_spec.md).

Use this profile when the source resembles:

- YAML frontmatter
- one H1 title
- multiple H2 and H3 sections
- dense conceptual bullets
- wiki-links such as `[[context window]]`
- semantic markers such as `⭐`, `⚠`, `🔑`, `🔍`, or `→ Learn:`

This profile is an input-interpretation layer.
It does not override the master style spec's hard invariants.

When you want the current stable output shape for this source type, pair this profile with:

- [knowledge_map_dashboard_profile.md](knowledge_map_dashboard_profile.md)

## 1. Input Assumptions

The source note is likely to contain:

- frontmatter metadata
- an explicit conceptual title
- a summary or framing paragraph near the top
- a backbone or spine section
- clustered concepts rather than raw quantitative datasets
- synthesis or follow-up sections such as knowledge gaps, implications, or next-learn items

The note is already semi-structured.
Preserve that structure instead of replacing it with a generic dashboard taxonomy.

## 2. Parsing Order

Interpret the source in this order:

1. YAML frontmatter
2. H1 title
3. opening paragraph or framing block
4. H2 sections
5. H3 subsections
6. bullet lists and numbered lists
7. inline conventions such as wiki-links, bold labels, and emoji markers

Later layout decisions should respect this parse order.

## 3. Frontmatter Mapping

Treat frontmatter as authoritative metadata.

Recommended mapping:

- `created`: metadata row or sidebar meta
- `source`: source citation link
- `type`: metadata pill
- `status`: metadata pill
- `difficulty`: metadata pill
- `tags`: compact metadata list or tag chips
- `backbone`: candidate overview strip or lead idea cards
- `related`: related concepts panel or compact sidebar list
- `mindnode_recommended`: optional low-priority meta flag, usually omit unless meaningful

Do not render raw YAML syntax.
Render the meaning, not the markup.

## 4. Title and Framing Mapping

Use the note's H1 as the primary document title in the main content area.

The first non-heading paragraph should usually become:

- the overview framing paragraph
- or the opening explanatory paragraph in the first section

If `APP_NAME` is provided, use it as the shell or product label.
Do not replace the note title with `APP_NAME`.

## 5. Section Mapping Rules

Default behavior:

- create one main dashboard section per strong H2 heading
- preserve H2 wording where possible
- preserve H2 order unless the source is clearly too granular

Compression rules:

- merge only weak, repetitive, or overly granular H2s
- keep total visible nav sections manageable, ideally `4` to `10`
- never compress away a meaningful `Knowledge Gaps`, `Next Learn`, or equivalent follow-up section

If the note already uses headings such as `Backbone`, `Concept Clusters`, `Cross-Cluster Logic`, `Prerequisite Chain`, `Strategic Leverage`, `Meta-Level Analysis`, or `Knowledge Gaps`, keep those sections rather than remapping them into new labels.

## 6. H3 and List Mapping Rules

Subsections under H2 headings should usually become:

- cards
- sub-panels
- grouped blocks
- compact callouts

They should not automatically become separate nav sections.

Bullets with bold lead-ins such as `- **High reliability:** ...` should become:

- labeled bullets
- comparison rows
- idea cards

Numbered lists such as prerequisite chains should preserve sequence visually.

If a source section expresses relationships using shorthand references such as `C1`, `C2`, `Cluster 1`, or similar abbreviations:

- resolve those references to the actual nearby source section or concept names when rendering the UI
- use the shorthand only as internal parsing help, never as the final user-facing label

## 7. Wiki-Link Normalization

Internal wiki-links are semantic references, not literal UI text.

Normalize them by:

- removing the double brackets
- converting them to plain readable labels
- optionally rendering them as inline concept chips or muted related-note pills

Do not render raw strings like `[[context window]]` in the final dashboard.

## 8. Emoji and Marker Semantics

Treat common source markers as emphasis cues.

- `⭐` = backbone, primary idea, or high-salience concept
- `⚠` = caution, limitation, fragility, or non-scaling warning
- `🔑` = key takeaway, leverage point, or operating heuristic
- `🔍` = open question, unresolved area, or knowledge gap
- `→ Learn:` = explicit next-learning item or follow-up topic

These markers guide emphasis.
They do not require a special claim taxonomy.

## 9. Visualization Rules

This source type is concept-dense and usually weakly quantitative.

Default stance:

- use `0` charts unless the markdown contains explicit numeric series, counts, ranked comparisons, or time-based values
- prefer cards, lists, compact tables, and prose blocks over charts

Appropriate chart triggers:

- dated numeric trend values
- categorical comparisons with explicit counts or percentages
- ranked comparisons with enough numeric substance to benefit from visual encoding

Do not create charts from:

- concept clusters
- framework bullets
- knowledge gaps
- warnings
- relationship arrows
- list length alone

## 10. Display Priorities

When this profile is active, preserve the source's conceptual structure in this order:

1. what the note is about
2. its strong H2 section order
3. its H3 clusters and grouped bullets
4. its explicit sequences and follow-up items

The generated dashboard should feel like a navigable study guide, not a metrics board and not a synthetic analysis engine.

## 11. Anti-Patterns

- Do not dump the raw markdown into HTML verbatim.
- Do not render YAML frontmatter as body text.
- Do not preserve raw wiki-link syntax.
- Do not make one nav section for every H3 subsection.
- Do not chart conceptual bullets without numeric evidence.
- Do not replace the note's internal structure with generic synthesized dashboard categories.
- Do not add `Fact / Inference / Speculation` labels or any similar taxonomy.
- Do not leave relationship labels in shorthand form such as `C1 -> C2` when the source provides the corresponding concept names.
- Do not create new sections such as `Strategic Leverage` or `Meta-Level Analysis` unless the source actually contains that material.
- Do not lose source provenance when a `source` field is present.

## 12. Validation Checks

When this source profile is active, a good output should satisfy all of these:

- metadata from frontmatter is visible in normalized form when useful
- the note's H1 survives as the main title
- strong H2 headings survive in source order or in a clearly justified light compression
- wiki-links are normalized
- H3 content remains grouped under the correct parent section
- relationship labels are human-readable and use actual source concept names when available
- knowledge gaps and follow-up items remain explicit
- charts appear only if the source truly supports them
- no epistemic legend or claim-label taxonomy is added
- the dashboard still obeys the master style spec
