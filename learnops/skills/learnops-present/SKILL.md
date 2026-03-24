---
name: learnops-present
description: >-
  Stage 2 of the LearnOps pipeline. Generates a single-file HTML study-guide
  dashboard from an Obsidian-style knowledge-map markdown note, rendering
  extracted knowledge architecture as a navigable, drill-ready study surface.
  Use when the user says "generate a dashboard," "render this map," "dashboard
  this note," "create a study guide dashboard," "turn this into HTML," or
  provides a knowledge-map markdown file and wants a visual HTML output.
  Handles YAML frontmatter, wiki-links, emoji markers, backbone sections,
  concept clusters, cross-cluster logic, prerequisite chains, strategic
  leverage, and knowledge gaps. Produces an editorial, restrained,
  Tailwind-based single-file HTML dashboard optimized for pre-drill
  comprehension. Do NOT use for creating knowledge maps (use learnops-extract),
  for general frontend design (use frontend-design), or for drilling maps
  (use learnops-drill).
license: Apache-2.0
metadata:
  author: jonsthomas
  version: "1.0"
  pipeline-stage: "2"
---

# Knowledge Map Dashboard Generator

Stage 2 (Presentation) of the LearnOps pipeline. Converts a structured knowledge-map markdown note into a single-file editorial HTML study-guide dashboard.

The output is a navigable, drill-ready HTML file — not a generic admin panel. It preserves the note's conceptual architecture while making every drillable node visible, identifiable, and self-assessable. The learner uses this surface to internalize the map's structure before entering Stage 3 (Feynman drilling).

---

## Reference Files

Read these before generating. They are in the `references/` folder.

- **`knowledge_map_runtime_contract.md`** — The binding generation contract. **Read this every run before writing any HTML.** Contains pipeline context, parsing order, section strategy, sequence component spec, anchor/deep-link rules, anti-patterns, generation strategy, and validation checklist.
- **`cognitive_design_rationale.md`** — Maps Mayer's multimedia learning principles to specific dashboard design rules, with Stage 2 pipeline implications for each. **Read this every run** to understand *why* each design rule exists. Reasoning-backed compliance is more robust than rule-following.
- **`style_spec.md`** — The full master visual and structural specification. **Read only when debugging** a generation that doesn't match the expected style, or when the user is refining the spec system itself.
- **`source_profile.md`** — Input parsing rules for knowledge-map markdown. **Read only when debugging** parsing failures (raw wiki-links, broken frontmatter, misclassified sections).
- **`dashboard_profile.md`** — Output profile with section contracts, drill-readiness requirements, and validation checklist. **Read only when debugging** structural issues (wrong section order, missing scaffolds, violated anti-patterns).

---

## Input Handling

The source note can arrive three ways:

**1. Vault file reference:** User names a note in the vault.
- Use `obsidian-mcp-tools:list_vault_files` to locate it
- Use `obsidian-mcp-tools:show_file_in_obsidian` to open it (mandatory — `get_active_file` reads whatever is currently open)
- Use `obsidian-mcp-tools:get_active_file` with `format: markdown` to read content

**2. File upload:** User attaches a `.md` file.
- Read from `/mnt/user-data/uploads/`

**3. Pasted markdown:** User pastes note content directly into chat.
- Use the pasted content as-is.

---

## Generation Workflow

Execute in this order every run:

### Step 1 — Read references
Read `references/knowledge_map_runtime_contract.md` and `references/cognitive_design_rationale.md` before writing any code.

### Step 2 — Read the source note
Obtain the full markdown content via whichever input method applies.

### Step 3 — Resolve configuration
Apply defaults unless the user overrides them:

| Parameter | Default |
|---|---|
| APP_NAME | Derived from note H1 title |
| LANG_CODE | en |
| PRIMARY_HEX | #1e293b |
| ACCENT_HEX | #3b82f6 |
| Navigation | sidebar |
| Density | standard |
| Interpretation | minimal |
| Charts | 0 (unless note contains numeric evidence) |

### Step 4 — Parse the note
Follow the parsing order from the runtime contract §3:
1. YAML frontmatter → metadata
2. H1 → title
3. Opening paragraph → framing text
4. H2 sections → main nav sections (source order)
5. H3 subsections → individually identifiable cards within parent H2
6. Bullets and numbered lists → structured content
7. Wiki-links → plain readable labels
8. Emoji markers → emphasis cues (not literal markup)

### Step 5 — Generate HTML
Follow the runtime contract's generation strategy (§11):
1. Normalize metadata
2. Build overview from title, framing paragraph, optional backbone items (compact cards if 3+, max ~150 words prose)
3. Create one main section per strong H2 in source order
4. Render H3s as individually identifiable cards — each gets a card-level anchor
5. Resolve relationship labels into actual source concept names
6. Create clickable references in relationship cards that execute section-switch + scroll + highlight
7. Render prerequisite chains using the sequence component (timeline/numbered steps), not plain lists
8. Add section-level and card-level anchors to all navigable elements
9. Emit final HTML

Apply cognitive design principles throughout — coherence for content decisions, signaling for visual hierarchy, segmenting via single-section visibility, spatial contiguity for labels, pre-training for overview design.

### Step 6 — Write and present the file
- Write to `/mnt/user-data/outputs/{slug}.html`
- Use `present_files` to deliver to the user
- Filename slug: lowercase, hyphens, derived from note title

### Step 7 — Post-output summary
Provide a brief summary:
```
📊 Dashboard generated: {filename}

Sections: [count] — [brief labels]
Source: [note title]
Config: [any non-default settings]

This is Stage 2 output — study the dashboard, then drill it in Stage 3.
```

---

## Constraints

- Return exactly one complete HTML5 document.
- Single file: inline CSS and inline JavaScript only.
- Vanilla JavaScript only. No frameworks.
- Tailwind CSS via CDN. Inter font via CDN.
- Chart.js via CDN only if the note contains genuine numeric evidence.
- No SVG, no Mermaid, no external images, no build steps.
- Preserve the note's H2 section order — do not rearrange unless compression is clearly needed.
- Never render raw YAML, raw `[[wiki-links]]`, or literal emoji markers.
- Never add epistemic legends, reader prompts, claim taxonomies, or invented sections.
- Never use internal shorthand like "C1 → C2" when source concept names are available.
- Sequence content (prerequisite chains, dependency lists) must render as visually ordered using the timeline/step component.
- H3 sub-node cards must be visually distinct from cluster-level introductory prose.
- Every H3 card must have a card-level anchor for deep-linking.
- Related concept chips capped at 6–8.
- Single-section visibility must be enforced — this is the primary cognitive segmenting mechanism.
- The dashboard must pass the sameness test: it should not be mistakable for a generic SaaS admin template after removing the content.
