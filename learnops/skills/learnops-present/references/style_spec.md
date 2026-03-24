# Master Style Spec: Editorial Study-Guide Dashboard

## 1. Purpose

This document is a master generation contract for producing a distinct dashboard style as a single-file HTML application.

It is optimized for AI one-shot code generation, not for human-only design review. Every section is written to reduce ambiguity, suppress generic dashboard defaults, and preserve portability.

The target outputs are:

- Knowledge maps
- Study guides
- Structured reading dashboards
- Synthesis notes that still need faithful source display

The intended style is:

- Editorial
- Restrained
- Study-friendly
- Instrument-panel

## 2. Operating Directive

Use this document as a system directive for an AI information architect.

> You are generating an editorial, single-file HTML study-guide dashboard.  
> You must preserve the structural grammar, visual restraint, and source-display rules in this specification.  
> When a choice is unclear, choose the more conservative, more legible, and more study-friendly option.  
> Omit weak or empty sections instead of inventing filler.  
> Never substitute a generic SaaS admin dashboard pattern when this document gives a stricter rule.

## 3. Priority Order

When rules conflict, follow this order:

1. Output contract
2. Hard invariants
3. Core grammar
4. Component contracts
5. Visual system
6. Fallback behavior
7. Optional variants

Lower-priority rules may never violate higher-priority ones.

## 4. Design Intent

The dashboard should feel like a compact reading console for studying and navigating structured insight.

The user is not casually browsing. They are reading a dense structured note, moving between sections, and building a mental model quickly.

The interface must therefore prioritize:

- readability over novelty
- source fidelity over extra interpretation
- hierarchy over visual noise
- consistency over flexibility
- modular composition over bespoke layouts

## 5. Output Contract

Every generated artifact must satisfy all of the following:

- Output exactly one `.html` file.
- Use HTML5 with a valid `<html lang="...">`.
- Use vanilla JavaScript only.
- Use Tailwind CSS via CDN.
- If charts are used, use Chart.js via CDN.
- Do not use React, Vue, Svelte, Alpine, jQuery, D3, Plotly, Mermaid, or any build step.
- Do not use SVG icons, inline SVG, SVG charts, canvas-free chart libraries, or external image assets.
- Keep all author-written HTML, CSS, and JavaScript inside the single file.
- Use semantic landmarks: `<nav>`, `<main>`, `<section>`, headings, lists, tables, and buttons.

Important network assumption:

- This spec mandates CDN-based delivery.
- Assume the user's device is always online.
- Do not attempt to write large inline CSS payloads, fallback SVG charts, base64-encoded libraries, or embedded library source to make the file offline-capable.
- Doing so violates the core grammar by inflating file size and reducing generation reliability.
- Accept the CDN dependency as a hard invariant.
- If strict offline execution is required, define a separate export profile instead of modifying this spec implicitly.

## 6. Hard Invariants

These rules are mandatory and must not be broken.

### 6.1 File and Runtime Constraints

- One HTML file only.
- Vanilla JS only.
- Tailwind CSS via CDN only.
- If charts are used, Chart.js via CDN only.
- No package manager assumptions.
- No build tooling.
- No network requests for data.
- Data must be embedded inline in the file.

### 6.2 Structural Constraints

- The page is a single-page application with section switching, not multi-page navigation.
- One navigation system controls visibility of content sections.
- Exactly one content section is visible at a time.
- Navigation items map to section IDs deterministically.
- The main content area scrolls independently from the page shell.
- Charts must always live inside constrained wrapper containers.

### 6.3 Content Integrity Constraints

- Preserve the source note's structure and meaning unless a source profile explicitly calls for light compression.
- Do not invent heavier analysis than the source supports.
- If a section has no meaningful content, omit it entirely.
- Do not create placeholder charts, placeholder tables, or filler prose.

### 6.4 Visual Integrity Constraints

- Use Inter as the font family.
- Keep motion restrained.
- Keep shadows subtle or absent.
- Maintain a high data-to-ink ratio.
- Preserve a neutral editorial base with configurable primary and accent colors.

## 7. Authorized Configuration Surface

The spec is intentionally narrow. Only the following values should vary routinely between outputs.

### 7.1 Primary Knobs

- `APP_NAME`
- `LANG_CODE`
- `PRIMARY_HEX`
- `ACCENT_HEX`
- section names
- section count
- section content
- chart data
- chart type selection from the approved list

Color application rule:

- When applying `PRIMARY_HEX` or `ACCENT_HEX`, use Tailwind arbitrary value syntax such as `bg-[#bf5700]`, `text-[#bf5700]`, `border-[#bf5700]`, or equivalent utility-safe forms.
- Do not attempt to convert arbitrary hex values into guessed named Tailwind palette tokens.

### 7.2 Controlled Optional Knobs

These may vary only when explicitly requested.

- source profile: `knowledge-map-markdown`
- display mode: `study-guide`
- navigation pattern: `sidebar` or `top-nav`
- density: `standard` or `compact`
- evidence emphasis: `balanced` or `narrative-heavy`

### 7.3 Non-Authorized Variability

Do not improvise these:

- font family
- chart library
- general page architecture
- decorative icon system
- animation style
- neumorphism, glassmorphism, or gradient-heavy themes
- bespoke per-section layouts with no shared grammar

## 8. Layer Model

This spec is modular. Each layer has a fixed responsibility.

### 8.1 Core Grammar

Defines:

- app shell
- navigation model
- responsive structure
- section rhythm
- scroll behavior
- grid rules

### 8.2 Visual System

Defines:

- typography
- color roles
- spacing scale
- border and radius treatment
- surface layering
- motion rules

### 8.3 Component Contracts

Defines:

- exact responsibilities of tags, cards, tables, charts, callouts, and context panels
- how components combine
- what content belongs in each component

### 8.4 Implementation Profile

Defines:

- document skeleton
- CDN dependencies
- JavaScript behavior
- chart initialization rules
- accessibility baseline

### 8.5 Variants

Defines:

- limited, controlled extensions
- what can change without breaking the house style

Variant layers may override proportions and density, but may not violate hard invariants.

### 8.6 Source Profiles

Defines:

- how structured source material should be interpreted before layout decisions are made
- how source-native semantics map into dashboard sections and components
- what source artifacts must be normalized rather than rendered literally

Source profiles may guide section derivation and evidence selection, but may not violate hard invariants or the output contract.

## 9. Core Grammar

### 9.1 Default Shell

Default navigation pattern is a left sidebar with a scrollable main panel.

Desktop shell:

- full viewport height
- horizontal flex container
- fixed-width left nav
- flexible main content column
- main content scrolls vertically
- page-level scrollbars suppressed

Mobile shell:

- fixed top header
- menu button toggles nav visibility
- nav slides over content from the left
- main content gets top padding to clear the mobile header

Default breakpoint:

- `md` / `768px`

Default width guidance:

- sidebar width: `16rem`
- content max width inside the main panel: `80rem`
- long-form narrative blocks: keep to roughly `48rem` max width

### 9.2 Section Switching Model

Each navigation item is a `<button>` with class `.nav-item`.

Each content view is a `<section>` with class `.content-section`.

Mapping rule:

- nav button ID: `nav-[section-id]`
- section ID: `[section-id]`

Behavior:

- exactly one nav item is active at a time
- exactly one section is visible at a time
- on mobile, navigation closes after a section is selected
- section changes may use a subtle fade-in, but no theatrical transitions
- keep visible section count in navigation manageable, ideally `4` to `8`

### 9.3 Section Rhythm

Each content section should follow a repeatable reading structure.

Required order:

1. Section heading
2. Optional short intro or framing line
3. Primary content block
4. Optional supporting block such as a list, table, or callout

This order is stable even when content changes.

The first section should normally be `Overview`, `Study Guide`, or a close equivalent.

Allowed adaptation:

- if evidence is numeric, use chart or table
- if evidence is qualitative, use cards, lists, or a structured prose block
- if a section does not need an intro, omit it

Preferred section archetypes when the source material supports them:

- overview
- backbone or core ideas
- concept groups
- relationships or comparisons
- next learn or follow-up items

### 9.4 Layout Patterns

Use only a small set of repeatable patterns.

Allowed patterns:

- full-width editorial section intro
- two-column evidence grid
- three-card finding strip
- full-width table card
- chart-plus-commentary split panel

Default grid ratios:

- balanced split: `1fr 1fr`
- narrative-heavy split: `3fr 2fr`
- chart-heavy split: `2fr 3fr`

Do not invent arbitrary new page-level compositions per section.

### 9.5 Density Rules

Default density is `standard`.

`standard`:

- section gap: `2rem`
- card gap: `1rem`
- card padding: `1rem` to `1.25rem`

`compact`:

- section gap: `1.5rem`
- card gap: `0.75rem`
- card padding: `0.875rem` to `1rem`

Compact mode may tighten spacing, but must not reduce legibility.

### 9.6 Canonical Tailwind Shell Classes

Unless a variant explicitly overrides them, use these class recipes or their direct equivalents.

- `body`: `min-h-screen bg-slate-100 text-slate-900 antialiased`
- `#app`: `flex h-screen overflow-hidden`
- `#sidebar` desktop: `hidden md:flex md:w-64 md:flex-col md:border-r md:border-slate-200 md:bg-slate-50`
- `#sidebar` mobile shell: `fixed inset-y-0 left-0 z-40 w-64 transform border-r border-slate-200 bg-slate-50 transition-transform duration-150 ease-out md:static md:z-auto md:translate-x-0`
- `#mobile-header`: `fixed inset-x-0 top-0 z-30 flex h-14 items-center justify-between border-b border-slate-200 bg-white px-4 md:hidden`
- `#main-content`: `flex-1 overflow-y-auto bg-slate-100`
- main inner wrapper: `mx-auto max-w-7xl space-y-8 p-4 pt-20 md:p-8 md:pt-8`
- `.content-section`: `space-y-6`

Equivalent classes are acceptable only if the resulting behavior and proportions remain effectively identical.

## 10. Visual System

### 10.1 Style Signature

The style should read like an evidence desk, not a startup admin panel.

Signature qualities:

- editorial typography
- calm neutral surfaces
- clear evidence labeling
- modular instrument-panel cards
- restrained use of color for emphasis rather than branding spectacle

### 10.2 Typography

Typography is fixed.

- Font family: `Inter`, sans-serif
- Body text: neutral, readable, regular weight
- Section titles: strong but not oversized
- Subheads: compact and disciplined
- Labels and metadata: smaller, tighter, semibold

Recommended text scale:

- app title: `text-lg` or `text-xl`
- section title: `text-2xl`
- subsection title: `text-lg`
- body: `text-sm` or `text-base`
- metadata: `text-xs` or `text-sm`

Do not use display fonts.
Do not use oversized marketing-style hero text.

### 10.3 Color Roles

The palette is role-based, not decorative.

Required roles:

- `canvas`
- `surface`
- `surface-muted`
- `border`
- `text-strong`
- `text-muted`
- `primary`
- `accent`
- `success`
- `warning`
- `danger`

Default tonal behavior:

- canvas is a cool light neutral
- cards sit on white or near-white surfaces
- borders are subtle and always visible
- text contrast is high
- primary and accent are used sparingly

Color usage rules:

- use neutral tones for structure
- use primary for active state, key emphasis, and chart lead series
- use accent for secondary emphasis and comparison series
- use success, warning, and danger only for status semantics
- never let accent colors dominate the whole interface

### 10.4 Surface Treatment

Surface logic must remain restrained.

- cards use a border first
- shadows are minimal and optional
- radius is moderate, not playful
- active and important regions can use a subtle tint, not heavy fills

Recommended shape language:

- radius: `rounded-xl`
- standard border: `border border-slate-200`
- card background: `bg-white`

Do not use:

- frosted glass
- heavy layered shadows
- glowing edges
- oversized rounded pills for large containers

### 10.5 Spacing

Spacing must be regular and modular.

Base spacing unit:

- `4px`

Use spacing steps consistently:

- `8px`
- `12px`
- `16px`
- `24px`
- `32px`

Avoid arbitrary spacing values unless needed to satisfy a strict wrapper constraint.

### 10.6 Motion

Motion is allowed only to clarify state change.

Allowed:

- subtle nav slide on mobile
- short fade-in on section change
- hover and focus transitions under `200ms`

Disallowed:

- parallax
- bounce
- scale theatrics
- entrance cascades
- pulsing highlights

## 11. Study-Guide Scaffolds

This dashboard should support reading without over-interpreting the source.

### 11.1 Source Fidelity

- Preserve the note's headings, sequence, and emphasis where they are strong.
- Compress only when the source is too granular for navigation.
- Prefer rearranging for clarity only when the result is obviously more readable.

### 11.2 Reading Support

Allowed scaffolds:

- a compact overview
- short section intros
- metadata chips
- related concept chips
- compact callouts for warnings or next-learn items

Do not add taxonomies, legends, or synthetic claim labels unless explicitly requested.

### 11.3 Chip Usage

Chips are for:

- metadata
- section labels
- related concepts
- lightweight status cues

When chips or labels represent relationships or section references:

- use human-readable source language
- prefer actual section or concept names
- never use internal shorthand such as `C1`, `C2`, `A`, `B`, or `Cluster 1` when readable names exist

Do not use chips to classify every claim in the document.

## 12. Component Contracts

Every component must have a stable purpose. Do not use components interchangeably without reason.

### 12.1 Sidebar Navigation

Purpose:

- orient the reader
- expose section structure
- provide rapid jumps between views

Required content:

- app name
- optional short meta block
- ordered nav items

Interaction rules:

- active item is visually distinct
- hover and focus states are obvious
- labels are concise
- nav should scroll internally if long

### 12.2 Mobile Header

Purpose:

- preserve orientation on narrow screens
- provide menu access

Required content:

- app name
- menu toggle button

Do not add search bars, filters, or extra chrome unless explicitly required.

### 12.3 Section Context Box

Purpose:

- explain what the section covers before evidence begins

Required structure:

- a small label such as `Section Context`
- one concise paragraph

Rules:

- short only
- never a wall of text
- visually quieter than the section heading

### 12.4 Finding Cards

Purpose:

- surface key ideas quickly

Recommended count:

- 2 to 4 cards

Each card may contain:

- short title
- concise point
- supporting micro-metric or short note

Finding cards should not become generic KPI tiles unless the data truly is KPI-shaped.

### 12.5 Alert and Callout Cards

Purpose:

- emphasize risk, warning, progress, or a decisive statement

Variants:

- `info`
- `warning`
- `success`
- `danger`

Structure:

- left accent border
- concise title
- brief body copy

Do not use callouts as decoration or to repeat what nearby text already says.

### 12.6 Evidence Grid

Purpose:

- pair explanation with proof

Allowed pairings:

- commentary + chart
- commentary + table
- commentary + structured list
- chart + supporting notes

At least one side of the evidence grid must explain the significance of the evidence.

### 12.7 Tables

Use tables when precision matters more than shape recognition.

Use a table instead of a chart when:

- there are too few data points
- exact values matter most
- row labels are long
- comparisons are categorical and sparse

Table rules:

- full width inside a card
- compact but readable cell padding
- aligned headers
- visible row separation
- no decorative zebra striping unless it improves scanability

### 12.8 Charts

Charts are evidence tools, not decoration.

Approved chart types:

- bar
- line
- doughnut
- pie
- radar

Rules:

- choose the simplest chart that clarifies the data
- do not force a chart where a table is clearer
- legends must be compact
- tooltips must be enabled
- maintain aspect ratio must be disabled
- charts must live in constrained wrappers
- default to no more than `2` charts per section

### 12.9 Chart Wrapper Contract

This is mandatory.

Every chart canvas must be wrapped in a container that constrains both width and height.

Required wrapper behavior:

- `position: relative`
- full available width
- explicit height
- reasonable max width
- optional centered layout

Recommended wrapper classes:

- `relative h-72 w-full max-w-3xl`
- `relative h-72 md:h-80 w-full max-w-3xl`

Failure to wrap charts correctly is a hard spec violation.

### 12.10 Lists

Lists are preferred over long prose blocks.

Use lists for:

- evidence bullets
- key judgments
- implications
- monitoring items
- scenario branches

Paragraphs should remain short and broken into digestible units.

### 12.11 Canonical Component Base Classes

Unless a variant explicitly overrides them, use these class recipes or their direct equivalents.

- nav item: `nav-item flex w-full items-start gap-2 rounded-lg px-3 py-2 text-left text-sm font-medium text-slate-700 transition hover:bg-slate-200/70 hover:text-slate-900 focus:outline-none focus:ring-2 focus:ring-slate-400`
- active nav item: add `bg-slate-900 text-white`
- card shell: `rounded-xl border border-slate-200 bg-white p-4 md:p-5`
- muted card shell: `rounded-xl border border-slate-200 bg-slate-50 p-4 md:p-5`
- context box: `rounded-xl border border-slate-200 bg-slate-50 p-4 text-sm text-slate-700`
- finding strip grid: `grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-3`
- evidence grid balanced: `grid grid-cols-1 gap-4 xl:grid-cols-2`
- evidence grid narrative-heavy: `grid grid-cols-1 gap-4 xl:grid-cols-[3fr_2fr]`
- evidence grid chart-heavy: `grid grid-cols-1 gap-4 xl:grid-cols-[2fr_3fr]`
- chip base: `inline-flex items-center rounded-full border px-2 py-0.5 text-xs font-semibold tracking-wide`
- table wrapper: `overflow-x-auto rounded-xl border border-slate-200 bg-white`

Equivalent classes are acceptable only if they preserve the same visual weight, spacing, and behavior.

## 13. Chart System

Chart.js is mandatory.

### 13.1 Global Defaults

On `DOMContentLoaded`, configure Chart.js defaults for:

- font family: Inter
- readable text color
- restrained grid and axis styling

Charts should visually match the editorial shell rather than default Chart.js styling.

### 13.2 Series Coloring

Use a disciplined chart palette:

- first series: primary
- second series: accent
- additional series: controlled tints or neutral variations

Do not produce rainbow palettes.
Do not assign unrelated colors to every category by default.

### 13.3 Chart Selection Rules

Choose chart types by meaning:

- line for trends or ordered progression
- bar for discrete comparison
- doughnut or pie for limited part-to-whole cases
- radar only for compact multi-dimension profile comparisons

Avoid radar charts unless the comparison benefits from radial symmetry.

### 13.4 Chart Fallback Rules

If a chart would be weak, replace it with:

- a table
- a comparison card group
- a structured evidence list

Weak chart signals include:

- fewer than 3 meaningful values
- no meaningful axis labels
- excessive label length
- data shape that requires precision over trend

## 14. Implementation Profile

### 14.1 Document Skeleton

The HTML document should follow this structure:

```html
<!doctype html>
<html lang="[LANG_CODE]">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>[APP_NAME]</title>
    <!-- Inter font -->
    <!-- Tailwind CDN -->
    <!-- Chart.js CDN -->
  </head>
  <body>
    <div id="app">
      <header id="mobile-header"></header>
      <nav id="sidebar"></nav>
      <main id="main-content">
        <section id="[section-id]" class="content-section"></section>
      </main>
    </div>
    <script>
      // navigation state
      // section switching
      // mobile toggle
      // chart initialization
    </script>
  </body>
</html>
```

### 14.2 JavaScript Behavior

Required JavaScript responsibilities:

- set initial active nav item
- show one section and hide others
- toggle mobile nav
- close mobile nav on section change
- initialize charts after DOM is ready
- fail gracefully if a chart cannot initialize

Use a simple deterministic navigation function shape.

Reference implementation:

```js
function nav(id) {
  document.querySelectorAll('.content-section').forEach((section) => {
    section.classList.add('hidden');
  });

  document.querySelectorAll('.nav-item').forEach((item) => {
    item.classList.remove('active', 'bg-slate-900', 'text-white');
  });

  const section = document.getElementById(id);
  const navButton = document.getElementById(`nav-${id}`);

  if (section) section.classList.remove('hidden');
  if (navButton) navButton.classList.add('active', 'bg-slate-900', 'text-white');

  if (window.innerWidth < 768) {
    document.getElementById('sidebar')?.classList.add('-translate-x-full');
  }
}
```

Equivalent logic is acceptable only if it preserves the same simplicity and behavior.

Do not add application frameworks or state managers.

### 14.3 CSS Policy

Tailwind utilities should do almost all the work.

Custom CSS is allowed only when one of these is true:

- Tailwind cannot express the required behavior cleanly
- a tiny helper rule is needed for chart containers
- a minimal animation keyframe is needed for a restrained fade
- scrollbar styling is explicitly desired

Recommended custom CSS block for scrollbars:

```css
::-webkit-scrollbar {
  width: 6px;
}

::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 3px;
}
```

Do not write large bespoke CSS systems.

### 14.4 Accessibility Baseline

Minimum requirements:

- all nav items are buttons
- focus states are visible
- contrast is readable
- headings are hierarchical
- tables use proper header cells
- interactive controls have accessible labels

## 15. Variant Modules

Variants are allowed only as controlled modules.

### 15.1 Navigation Variant

Default: `sidebar`

Optional: `top-nav`

`top-nav` is allowed only if:

- the section count is low
- the narrative remains scannable
- mobile behavior remains clear

The navigation variant may change shell geometry but not the section-switching model.

### 15.2 Density Variant

Default: `standard`

Optional: `compact`

Compact mode may tighten spacing and card padding, but may not:

- reduce chip legibility
- compress table cells excessively
- shrink charts below readable sizes

### 15.3 Evidence Emphasis Variant

Default: `balanced`

Optional:

- `narrative-heavy`
- `chart-heavy`

This variant changes evidence grid ratios only.
It does not change the overall component set.

## 16. Fallback and Degradation Rules

These rules exist to prevent brittle output.

### 16.1 Missing Data

If data for a section is weak or absent:

- omit the section
- or reduce it to a compact note if it still matters

Do not produce empty shells.

### 16.2 Weak Quantitative Evidence

If numeric evidence is too thin for a chart:

- use a small table
- or use finding cards with explicit values

### 16.3 Chart Failure

If Chart.js fails to initialize:

- keep the card shell intact
- replace the chart area with a short plain-text evidence summary
- do not allow layout collapse

### 16.4 Excessive Content

If the source material is too large:

- compress into fewer sections
- summarize into bullet-led findings
- keep navigation count manageable

Do not turn the dashboard into a document dump.

## 17. Anti-Patterns

These are explicit failure modes.

- Do not output walls of text.
- Do not generate filler sections.
- Do not use SVG or Mermaid.
- Do not leave charts unconstrained.
- Do not use decorative gradients as a theme foundation.
- Do not overuse shadows.
- Do not use giant KPI tiles unless the content truly is KPI-centric.
- Do not create a rainbow chart palette.
- Do not build custom CSS for things Tailwind already handles.
- Do not create generic admin panels with icon grids and vanity metrics.
- Do not invent content to satisfy a layout slot.
- Do not render raw markdown artifacts such as YAML frontmatter fences, `[[wiki-links]]`, or literal markdown bullets when a source profile is active.

## 18. Validation Checklist

A generated dashboard passes only if all checks below succeed.

### 18.1 Structural Checks

- one HTML file only
- one active nav item
- one visible section
- responsive nav behavior works
- main content scrolls independently

### 18.2 Content Checks

- source structure is preserved or clearly improved by light compression
- no empty sections
- no filler prose
- no synthetic claim taxonomy is added unless explicitly requested

### 18.3 Visual Checks

- Inter is used
- layout feels restrained
- color is sparse and purposeful
- cards share a common grammar
- charts are visually integrated into the same system

### 18.4 Failure Checks

- no SVG
- no Mermaid
- no broken chart expansion
- no page-level layout overflow caused by canvases

## 19. Sameness Test

The design fails if it can be mistaken for a generic SaaS admin template after removing the content.

To prevent that, ensure the output visibly expresses:

- study-guide scaffolding as a recurring structure
- editorial reading hierarchy
- source-first composition
- restrained instrument-panel modularity

If those qualities are not legible from the shell and section anatomy alone, revise before accepting the output.

## 20. Recommended Prompt Envelope

When using this file to drive one-shot generation, pair it with a task prompt that includes:

- the raw data or source notes
- the source profile, if one applies
- the intended audience
- the desired section count if known
- any requested variant modules
- the primary and accent hex colors

Use this instruction prefix:

> Generate a single-file HTML dashboard that follows the attached master style spec exactly.  
> Use the provided content to create an editorial study-guide dashboard.  
> Preserve all hard invariants, omit filler, and keep the source structure clear and readable.

## 21. Extension Rule

If this spec is revised in the future, add new flexibility only by:

- introducing a new variant module
- introducing a new source profile module
- refining a component contract
- tightening a validation rule

Do not loosen hard invariants casually.
Do not expand the configuration surface unless repeated real-world use shows the need.
