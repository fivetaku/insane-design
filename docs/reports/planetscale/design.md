---
schema_version: 3.2
slug: planetscale
service_name: PlanetScale
site_url: https://planetscale.com
fetched_at: 2026-05-03T06:58:13Z
default_theme: light
brand_color: "#F35815"
primary_font: ui-monospace
font_weight_normal: 400
token_prefix: none

bold_direction: Terminal Infrastructure
aesthetic_category: brutal-minimal
signature_element: orange-rule-monospace-hero
code_complexity: medium

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Production CSS exposes a Tailwind-like utility layer plus real core color tokens, but no public named component API."

colors:
  bg-primary: "#FFFFFF"
  text-primary: "#414141"
  text-contrast: "#111111"
  text-secondary: "#818181"
  text-blue: "#0B6EC5"
  text-blue-bright: "#1E9DE7"
  text-orange: "#F35815"
  border-muted: "#C1C1C1"
  code-bg-dark: "#41414199"

typography:
  display: "ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace"
  body: "ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace"
  sans_support: "ui-sans-serif, system-ui, sans-serif"
  code: "ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace"
  ladder:
    - { token: body, size: "16px", line_height: "1.5", weight: 400, tracking: "0" }
    - { token: h1, size: "16px inherited", line_height: "1.5", weight: 700, tracking: "0" }
    - { token: sans-h1, size: "24px", line_height: "1.2", weight: 600, tracking: "-0.019em" }
    - { token: sans-h2, size: "20px", line_height: "1.1", weight: 600, tracking: "-0.017em" }
    - { token: sans-h3, size: "18px", line_height: "1.5", weight: 600, tracking: "-0.014em" }
    - { token: small, size: "12px", line_height: "1rem", weight: 500, tracking: "0.1em" }
  weights_used: [400, 500, 600, 700, "bold"]
  weights_absent: [300, 800, 900]

components:
  button-primary: { bg: "{colors.text-orange}", color: "#FFFFFF", height: "40px", padding: "0 16px", radius: "0", weight: 600 }
  button-small: { bg: "{colors.text-orange}", color: "#FFFFFF", height: "32px", padding: "0 8px", radius: "0", weight: 600 }
  focus-ring: { ring: "{colors.text-blue-bright}", offset: "0-2px", shadow: "Tailwind ring variables" }
  heading-rule: { border_left: "2px solid {colors.text-orange}", padding_left: "16px", margin_left: "-16px" }
  logo-grid-cell: { border: "1px solid #414141", height: "96-128px", bg: "#FFFFFF", alignment: "center" }
---

# DESIGN.md — PlanetScale

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

PlanetScale is not doing the familiar soft-gradient database cloud page. It behaves like a production manual that accidentally became a homepage: white paper, black ink, monospaced rhythm, hard grid lines, and a small orange signal that says "this part is live." The screenshot's first impression is almost anti-heroic. The largest statement is not a giant display headline but a compact terminal-like line with a 2px orange rule, like a shell prompt pinned to the margin of a printed runbook.

The page borrows trust from engineering interfaces, not from lifestyle SaaS polish. It has the feel of a database incident binder laid open on a clean metal desk: no soft cards, no vapor gradients, no second brand color trying to perform emotion. The body type is `ui-monospace` at 16px, links are blue, customer logos sit in a bordered table, and sections stack as arguments. The visual language says: this product survives load, audits, failovers, and boring production realities. That is the brand.

Color is a sparse operational layer. The surface is `#FFFFFF` (`{colors.bg-primary}`), text falls into charcoal `#414141` (`{colors.text-primary}`) and near-black `#111111` (`{colors.text-contrast}`), links use database-blue `#0B6EC5` / `#1E9DE7`, and the action temperature is carried by orange `#F35815` (`{colors.text-orange}`). The orange is not a sunset, not a gradient ribbon, not a decorative wash. It behaves like an active terminal cursor or a warning strip on a server rack: CTA fill, heading rule, selected/open state, then it disappears.

The customer wall is not a logo cloud; it is an evidence table. Each mark is boxed into a thin `#414141` grid cell as if the page were filing proof exhibits, not decorating a pitch deck. Shadows are almost absent because the site does not need atmospheric depth. Its depth comes from rules, borders, focus rings, and the pressure of exact technical nouns.

The metaphor is a database incident runbook with better taste: every line has a reason, every border is structural, and every accent is a state change. PlanetScale feels fastest because the page refuses visual latency. The site has no theatrical hero machinery; it makes the browser feel like a command surface where production truth has already been compiled.

이 페이지는 SaaS 마케팅 표면이지만, 실제로는 **production 실험실의 공구함**이다. left-rule heading은 server-rack의 라벨 띠, 16px 모노스페이스 본문은 실험실 노트의 줄자, 로고 그리드는 측정 결과를 진열한 evidence drawer다. 오렌지 사각 CTA는 공구함의 단 하나뿐인 빨간 스위치, 차콜 잉크는 blueprint 위의 연필 자국이다. 시연(demo)은 화려한 페이지가 아니라 차분한 노트로 제출되고, 엔지니어링 다이어그램은 illustration이 아니라 본문의 기술적 명사들로 그려진다. SaaS 갤러리가 아니라, 작업복을 입고 들여다보는 실험실 공구함의 인쇄면이다.

### Key Characteristics

- Monospace-first homepage, with body copy and navigation sharing terminal cadence.
- White default surface `#FFFFFF` with dark text rather than a dark console background.
- 2px orange left rule attached to primary headings.
- Orange CTA blocks with square corners, 40px height, and 600 weight.
- Blue links and focus rings instead of broad brand gradients.
- Logo wall rendered as a thin bordered grid, not floating logo clouds.
- Minimal shadow language; rings and borders do most of the work.
- Dense proof copy: benchmark, uptime, sharding, replicas, compliance, support.
- Tailwind utility classes are visible, but tokens stay small and literal.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Terminal Infrastructure
> **Aesthetic Category**: brutal-minimal
> **Signature Element**: 이 사이트는 **orange-rule-monospace-hero**으로 기억된다.
> **Code Complexity**: medium — utility-heavy CSS, responsive grids, dark-mode branches, and focus-ring state logic without heavy animation.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 PlanetScale처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
  font-size: 16px;
  line-height: 1.5;
  font-weight: 400;
  text-wrap: pretty;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #414141; --contrast: #111111; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --orange: #F35815; --link: #0B6EC5; --link-bright: #1E9DE7; }
h1 { border-left: 2px solid var(--orange); padding-left: 16px; margin-left: -16px; }
.btn { background: var(--orange); color: #FFFFFF; height: 40px; padding: 0 16px; }
```

**절대 하지 말아야 할 것 하나**: PlanetScale을 둥근 카드와 보라/파랑 그라디언트가 있는 일반 SaaS 히어로로 만들지 말 것.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://planetscale.com` |
| Fetched | `2026-04-20` phase1 artifacts reused; design.md generated `2026-05-03T06:58:13Z` |
| Extractor | Existing `insane-design/planetscale` phase1 bundle |
| HTML size | `89808` bytes |
| CSS files | `1` external CSS, `81300` chars |
| Token files | `resolved_tokens.json`, `alias_layer.json`, `brand_candidates.json`, `typography.json` |
| Screenshot | `insane-design/planetscale/screenshots/hero-cropped.png` |
| Token prefix | `none` / direct Tailwind-style variables plus literal core names |
| Method | CSS custom properties, HTML text, and screenshot observation; no report HTML rendered |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Static/SSR marketing build; captured HTML does not expose `__NEXT_DATA__`, but class output is Tailwind-like.
- **Design system**: Internal utility system with direct core tokens such as `--gray-900`, `--blue-700`, `--orange-400`, plus semantic classes like `.text-primary`, `.bg-primary`, `.btn`.
- **CSS architecture**:
  ```css
  core       (--gray-*, --blue-*, --orange-*, --red-*, --green-*, --purple-*) raw palette
  utility    (.container, .grid-cols-*, .text-primary, .hover:text-orange) Tailwind-style layout
  component  (.btn, .cta a:first-child, .dashed-box, .code-block) product-specific wrappers
  state      (:focus-visible, .ui-open:text-orange, dark/hover media branches)
  ```
- **Class naming**: Tailwind utility naming plus component classes. Examples: `grid-cols-12`, `max-w-7xl`, `font-semibold`, `dashed-box`, `dot-fill`, `btn-sm`.
- **Default theme**: light (`#FFFFFF` page surface) with `prefers-color-scheme: dark` branches present.
- **Font loading**: system fonts only; no remote brand font required in captured CSS.
- **Canonical anchor**: the hero screenshot shows product claims, enterprise proof, and customer grid above the fold, all in one restrained editorial block.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `ui-monospace` stack. PlanetScale lets the product voice be monospaced even in marketing copy.
- **Code font**: same `ui-monospace` stack.
- **Support sans**: `ui-sans-serif, system-ui, sans-serif` appears in `.sans-prose` documentation/prose contexts.
- **Weight normal / bold**: `400` / `700`; frequent operational emphasis uses `500` and `600`.

```css
:root {
  --ps-font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
  --ps-font-sans: ui-sans-serif, system-ui, sans-serif;
  --ps-font-weight-normal: 400;
  --ps-font-weight-medium: 500;
  --ps-font-weight-semibold: 600;
  --ps-font-weight-bold: 700;
}

body {
  font-family: var(--ps-font-mono);
  font-size: 16px;
  line-height: 1.5;
  font-weight: var(--ps-font-weight-normal);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-wrap: pretty;
}
```

### Note on Font Substitutes

Use the native monospace stack first. If the target environment needs a branded substitute, choose a restrained coding font with normal-width metrics, not a rounded tech font. Good substitutes are `SF Mono`, `IBM Plex Mono`, or `JetBrains Mono` with conservative tracking. Do not use `Inter` as the primary voice; it removes the database-console identity and turns the site into generic SaaS.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

### Principles

1. Keep the base paragraph at `16px / 1.5`; the page earns authority through density, not oversized hero type.
2. Use weight jumps rather than size jumps: `400` body, `500` inline code/emphasis, `600` buttons and sans headings, `700` primary headings.
3. Let monospace remain visible in navigation, body, proof copy, and labels.
4. Apply optical tightening only in sans prose contexts: `-0.019em`, `-0.017em`, `-0.014em`.
5. Use underline and left-border treatments for hierarchy instead of decorative display type.

### Scale

```css
body        { font-size: 16px; line-height: 1.5; font-weight: 400; letter-spacing: 0; }
h1          { font-size: inherit; line-height: inherit; font-weight: 700; }
h2          { font-size: inherit; font-weight: 700; text-decoration: underline; text-underline-offset: 4px; }
h3          { font-size: inherit; font-weight: 700; }
.sans-prose h1 { font-size: 24px; line-height: 1.2;  font-weight: 600; letter-spacing: -0.019em; }
.sans-prose h2 { font-size: 20px; line-height: 1.1;  font-weight: 600; letter-spacing: -0.017em; }
.sans-prose h3 { font-size: 18px; line-height: 1.5;  font-weight: 600; letter-spacing: -0.014em; }
.text-xs    { font-size: 12px; line-height: 1rem; }
.text-sm    { font-size: 14px; line-height: 1.25rem; }
```

### Voice in Type

PlanetScale's type should read like a well-edited engineering memo. Avoid fluffy headline forms like "Unlock the future of data." Prefer assertive technical nouns: `NVMe`, `Vitess`, `Postgres`, `replicas`, `failover`, `benchmarks`, `Traffic Control`, `Tier 0`.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Core Palette

```css
:root {
  --bg-primary: #FFFFFF;
  --text-primary: #414141;
  --text-contrast: #111111;
  --text-secondary: #818181;
  --text-blue: #0B6EC5;
  --text-blue-bright: #1E9DE7;
  --text-orange: #F35815;
  --border-muted: #C1C1C1;
  --code-bg-dark: #41414199;
}
```

### Observed Token Families

- **Gray** — `#FAFAFA`, `#EBEBEB`, `#E1E1E1`, `#C1C1C1`, `#A1A1A1`, `#818181`, `#737373`, `#616161`, `#414141`, `#2B2B2B`, `#1A1A1A`, `#111111`.
- **Blue** — `#F3FBFF`, `#DDF2FF`, `#73C7F9`, `#1E9DE7`, `#0B6EC5`, `#144EB6`, `#04122E`.
- **Orange** — `#FFF8F3`, `#FFE8D8`, `#FFC59B`, `#FC9C66`, `#FD812D`, `#F35815`, `#962D00`, `#672002`, `#3C1403`, `#240B00`.
- **Status colors** — green, red, purple, and yellow exist, but the public homepage should not read as a multi-color dashboard.

### Usage Rules

- Use `#FFFFFF` as the primary canvas and reserve `#FAFAFA` / `#EBEBEB` for subtle utility surfaces.
- Use `#414141` for paragraph text, not full black.
- Use `#111111` for high-contrast labels, headings, and key UI text.
- Use `#0B6EC5` for normal links and `#1E9DE7` for focus/active link energy.
- Use `#F35815` sparingly: CTA fill, left rule, open state, and selected tab-like moments.

### Color Stories

1. **White Infrastructure Paper** — `#FFFFFF` is not empty space; it is the page's operating surface, like a status report printed with no ornamental chrome.
2. **Charcoal Engineering Ink** — `#414141` and `#111111` create a technical document feel while avoiding harsh pure-black body copy.
3. **Query Link Blue** — `#0B6EC5` / `#1E9DE7` marks navigable technical concepts: fastest databases, NVMe drives, deployment options, docs.
4. **Failover Orange** — `#F35815` is the only warm command color, used where the interface wants action or attention.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

PlanetScale spacing is utilitarian and grid-bound. The captured CSS uses container ramps from `640px` to `1536px`, horizontal page padding from `var(--spacing-3)` through `var(--spacing-6)`, and prose rhythm centered on `24px` block margins.

```css
.container {
  width: 100%;
  margin-right: auto;
  margin-left: auto;
  padding-right: var(--spacing-4);
  padding-left: var(--spacing-4);
}

@media (min-width: 640px)  { .container { max-width: 640px;  padding-inline: var(--spacing-3); } }
@media (min-width: 768px)  { .container { max-width: 768px;  padding-inline: var(--spacing-4); } }
@media (min-width: 1024px) { .container { max-width: 1024px; padding-inline: var(--spacing-5); } }
@media (min-width: 1280px) { .container { max-width: 1280px; padding-inline: var(--spacing-6); } }
@media (min-width: 1536px) { .container { max-width: 1536px; } }

p, h1, h2, h3, blockquote, figure, pre, table, section {
  margin-bottom: 24px;
}
```

### Whitespace Philosophy

Whitespace here is not luxury whitespace. It is separation between arguments. Blocks sit close enough to feel like a technical document, while bordered grids create precise pauses. Use `16px` for inset mechanics, `24px` for paragraph/module rhythm, and `40px` when a grid hands off to a new heading. Avoid oversized 96px marketing gaps unless the content genuinely changes mode.

---

## 08. Radius & Borders
<!-- SOURCE: auto+manual -->

PlanetScale is mostly square. The site uses border and underline language more than radius. Captured radius values include `0`, `.125rem`, `.25rem`, `4px`, `100%`, and `9999px`, but the signature homepage CTA and grid cells are hard-edged.

```css
.btn {
  border-radius: 0;
  height: 40px;
}

.btn-sm {
  height: 32px;
  padding-left: 8px;
  padding-right: 8px;
}

h1 {
  margin-left: -16px;
  border-left: 2px solid #F35815;
  padding-left: 16px;
  text-indent: -2px;
}

blockquote {
  border-left: 2px solid #C1C1C1;
  padding-left: 12px;
}
```

Use radius only for true circular/dot controls or small utility chips. Do not round primary CTAs into pills.

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

Shadow is function, not atmosphere. The CSS mostly exposes Tailwind ring variables and `0 0 #0000` reset values. The brand relies on borders, focus rings, and dense layout rather than soft elevated cards.

```css
.btn:focus {
  --tw-ring-color: #1E9DE7;
  --tw-ring-offset-width: 0px;
  box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
}

.btn:focus-visible {
  outline: 2px solid transparent;
  outline-offset: 2px;
}
```

If elevation is needed, keep it mechanical: a 1px border plus focus ring. Avoid multi-layer card shadows.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

Motion is small and stateful. Buttons use a Tailwind default transition of `150ms` with `cubic-bezier(.4,0,.2,1)`. Disclosure arrows rotate `180deg`; hover states change text or background, and group hover reveals supporting controls.

```css
.btn {
  transition-property: all;
  transition-timing-function: cubic-bezier(.4, 0, .2, 1);
  transition-duration: .15s;
}

.ui-open\\:rotate-180[data-headlessui-state~="open"] {
  --tw-rotate: 180deg;
}
```

No scroll-jacking, parallax, elastic cards, or cinematic page transitions are required to reproduce the feel.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Pattern A: Document Hero

The hero is closer to a changelog announcement than a marketing splash. It begins with a narrow black announcement strip, then a horizontal nav, then a left-ruled title line and paragraph proof. Rebuild it as a document column inside a wide container, not as a centered H1 stack.

```css
.document-hero {
  max-width: 1200px;
  margin: 0 auto;
  padding: 48px 96px 32px;
}

.document-hero h1 {
  border-left: 2px solid #F35815;
  margin-left: -16px;
  padding-left: 16px;
  font-weight: 700;
}
```

### Pattern B: Bordered Proof Grid

Customer logos are arranged in a strict grid. The borders are not decoration; they turn proof into a data table.

```css
.logo-grid {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  border-top: 1px solid #414141;
  border-left: 1px solid #414141;
}

.logo-grid > * {
  min-height: 96px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-right: 1px solid #414141;
  border-bottom: 1px solid #414141;
}
```

### Pattern C: Dense Technical Sections

Feature arguments appear as paragraphs with technical links and inline bold phrases. Preserve the editorial density. Do not split every sentence into separate cards.

### Pattern D: Responsive Utility Grid

The CSS includes `grid-cols-1`, `grid-cols-2`, `grid-cols-3`, `grid-cols-6`, `grid-cols-12`, and named responsive classes. Use 12-column structure for real product/data layouts, but keep homepage proof sections readable at narrow widths.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

Breakpoints follow the Tailwind convention:

```css
sm: 640px
md: 768px
lg: 1024px
xl: 1280px
2xl: 1536px
```

The logo grid should collapse by reducing columns, not by turning into free-floating logo chips. Navigation can hide lower-priority links, but the rhythm should remain monospaced and line-based. The captured CSS also includes max-width hiding utilities such as `max-xl:hidden`, `max-lg:hidden`, `max-md:hidden`, and `max-sm:hidden`.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### 13-1. Component Inventory

- **Announcement bar** — black `#111111` strip with compact mono copy and a yellow learn-more button.
- **Primary navigation** — logo, dropdown labels, vertical separators, login/get-started links, orange contact CTA.
- **Heading rule** — `h1` with `2px` orange left border, `16px` left padding, and negative left offset.
- **Text link** — blue link (`#0B6EC5`) with brighter hover/focus treatment (`#1E9DE7`).
- **Primary button** — orange square rectangle, 40px height, 16px horizontal padding, 600 weight.
- **Small button** — same structure at 32px height and 8px horizontal padding.
- **Logo grid cell** — bordered white cell with centered brand mark; the cell matters as much as the logo.
- **Code/pre block** — mono block, `16px / 1.5`, `16px` padding, grey or translucent dark background.
- **Blockquote** — 2px left border, quote marks injected with pseudo-elements, author line italicized.
- **Focus ring** — blue ring using Tailwind CSS variables rather than custom outlines.

### 13-2. Named Variants

```yaml
button-primary:
  height: 40px
  padding: "0 16px"
  background: "#F35815"
  color: "#FFFFFF"
  border-radius: 0
  font-weight: 600
  transition: "all 150ms cubic-bezier(.4,0,.2,1)"

button-small:
  height: 32px
  padding: "0 8px"
  background: "#F35815"
  color: "#FFFFFF"
  border-radius: 0
  font-weight: 600

heading-rule:
  border-left: "2px solid #F35815"
  margin-left: "-16px"
  padding-left: "16px"
  text-indent: "-2px"
  font-weight: 700

logo-grid-cell:
  background: "#FFFFFF"
  border: "1px solid #414141"
  min-height: "96px"
  align: center
```

### 13-3. Signature Micro-Specs

```yaml
orange-rule-monospace-heading:
  description: "Turns a compact mono heading into a live command prompt rather than a display billboard."
  technique: "font-weight: 700; border-left: 2px solid #F35815; padding-left: 16px; margin-left: -16px; text-indent: -2px"
  applied_to: ["{component.heading-rule}", "hero h1", "section headings"]
  visual_signature: "A thin orange server-rack marker locks the heading to the left edge and makes the line feel executable."

square-orange-command-button:
  description: "Primary actions read as command blocks, not rounded SaaS pills."
  technique: "height: 40px; padding: 0 16px; background: #F35815; color: #FFFFFF; border-radius: 0; font-weight: 600; line-height: 1; transition: all 150ms cubic-bezier(.4,0,.2,1)"
  applied_to: ["{component.button-primary}", "{component.button-small}", "contact CTA"]
  visual_signature: "A flat orange rectangle interrupts the monochrome document like an active terminal state."

proof-table-logo-wall:
  description: "Customer proof is filed into a grid, making logos feel like evidence rather than decoration."
  technique: "display: grid; border-top: 1px solid #414141; border-left: 1px solid #414141; child border-right/bottom: 1px solid #414141; min-height: 96-128px; align-items: center; justify-content: center"
  applied_to: ["{component.logo-grid-cell}", "customer logo wall", "proof grids"]
  visual_signature: "A white evidence table with hard charcoal rulings; no floating logo chips, no shadowed cards."

blue-technical-link-ring:
  description: "Links and focus states stay operational blue while orange remains reserved for action and state."
  technique: "color: #0B6EC5; hover/focus decoration: #1E9DE7; focus ring via Tailwind ring variables with 2px transparent outline and 2px offset"
  applied_to: ["{component.text-link}", "{component.focus-ring}", "inline technical nouns"]
  visual_signature: "Blue marks navigable technical facts without turning the page into a multicolor dashboard."

charcoal-citation-side-rule:
  description: "Quotations and emphasis blocks echo the orange heading rule in a quieter charcoal weight, keeping the document feeling like a printed engineering memo."
  technique: "blockquote { border-left: 2px solid #C1C1C1; padding-left: 12px; } — half the visual weight of the #F35815 heading rule (2px stays, color steps down to muted border)"
  applied_to: ["{component.blockquote}", "callout-quote", "inline citations"]
  visual_signature: "Body-rank annotations carry the same left-edge marker grammar as headings, but in a recessive gray so they read as supporting evidence — not commands."
```

---

## 14. Content Voice
<!-- SOURCE: auto+manual -->

PlanetScale writes for senior technical buyers. Claims are paired with operational nouns and proof phrases:

- "fastest and most scalable cloud databases"
- "NVMe drives"
- "unlimited IOPS"
- "Tier 0 databases"
- "horizontal sharding"
- "high availability"
- "automated failover"
- "branch-per-environment"
- "Database Traffic Control"

The copy should be direct, evidence-heavy, and low on metaphor. The visual metaphor can be strong; the product copy should stay practical.

---

## 15. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  --ps-bg: #FFFFFF;
  --ps-text: #414141;
  --ps-contrast: #111111;
  --ps-muted: #818181;
  --ps-border: #C1C1C1;
  --ps-border-strong: #414141;
  --ps-link: #0B6EC5;
  --ps-link-active: #1E9DE7;
  --ps-orange: #F35815;
  --ps-code-bg: #41414199;
  --ps-font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
  --ps-font-sans: ui-sans-serif, system-ui, sans-serif;
}

body {
  margin: 0;
  background: var(--ps-bg);
  color: var(--ps-text);
  font-family: var(--ps-font-mono);
  font-size: 16px;
  line-height: 1.5;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-wrap: pretty;
}

a {
  color: var(--ps-link);
  text-decoration-color: var(--ps-link-active);
  text-underline-offset: 2px;
}

a:hover {
  color: var(--ps-link-active);
}

.ps-container {
  width: min(100% - 48px, 1200px);
  margin-inline: auto;
}

.ps-announcement {
  background: var(--ps-contrast);
  color: #FFFFFF;
  min-height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  font-size: 16px;
}

.ps-heading-rule {
  margin-left: -16px;
  border-left: 2px solid var(--ps-orange);
  padding-left: 16px;
  text-indent: -2px;
  color: var(--ps-contrast);
  font-weight: 700;
}

.ps-btn {
  display: inline-flex;
  height: 40px;
  align-items: center;
  justify-content: center;
  gap: 4px;
  white-space: nowrap;
  background: var(--ps-orange);
  color: #FFFFFF;
  padding-inline: 16px;
  border: 0;
  border-radius: 0;
  font-family: var(--ps-font-mono);
  font-weight: 600;
  line-height: 1;
  cursor: pointer;
  transition: all 150ms cubic-bezier(.4, 0, .2, 1);
}

.ps-btn:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
  box-shadow: 0 0 0 2px #1E9DE7;
}

.ps-logo-grid {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  border-top: 1px solid var(--ps-border-strong);
  border-left: 1px solid var(--ps-border-strong);
}

.ps-logo-grid > * {
  min-height: 104px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-right: 1px solid var(--ps-border-strong);
  border-bottom: 1px solid var(--ps-border-strong);
  background: #FFFFFF;
}

pre,
code {
  font-family: var(--ps-font-mono);
}

pre {
  max-width: 100%;
  overflow-x: auto;
  padding: 16px;
  background: #EBEBEB;
  color: #111111;
  font-size: 16px;
  line-height: 1.5;
}
```

---

## 16. Tailwind Mapping
<!-- SOURCE: manual -->

```js
export const planetscaleTheme = {
  colors: {
    bg: "#FFFFFF",
    text: "#414141",
    contrast: "#111111",
    muted: "#818181",
    border: "#C1C1C1",
    link: "#0B6EC5",
    linkActive: "#1E9DE7",
    orange: "#F35815",
  },
  fontFamily: {
    mono: ['ui-monospace', 'SFMono-Regular', 'SF Mono', 'Menlo', 'Consolas', 'Liberation Mono', 'monospace'],
    sans: ['ui-sans-serif', 'system-ui', 'sans-serif'],
  },
  borderRadius: {
    none: '0',
    sm: '.125rem',
    md: '.25rem',
    full: '9999px',
  },
}
```

---

## 17. Agent Prompt
<!-- SOURCE: manual -->

Build a PlanetScale-inspired database infrastructure page. Use a white `#FFFFFF` document surface, monospaced body typography, charcoal text `#414141`, near-black contrast `#111111`, blue technical links `#0B6EC5`, and orange action accents `#F35815`. Do not make a generic SaaS hero. Start with a compact announcement bar, then a restrained navigation row, then a document-like hero with a 2px orange left rule and dense technical proof copy.

Use square orange CTAs at 40px height with 16px horizontal padding and 600 weight. Use bordered proof grids for customer logos or metrics. Prefer line, border, underline, and focus-ring language over shadows. Keep copy practical and operational: database scale, NVMe, Vitess, Postgres, failover, replicas, benchmarks, compliance, support. Avoid decorative gradients, oversized display type, floating rounded cards, soft drop shadows, and playful illustration.

---

## 18. 🚫 What This Site Doesn't Use
<!-- SOURCE: manual -->

- 배경을 `#F7F7F5`, `#FAF4E8`, `#0B1020`, 또는 `#111827`로 두지 말 것 — PlanetScale의 기본 표면은 `#FFFFFF`이다.
- 본문 텍스트를 `#000000` 또는 `#1D1D1F`로 두지 말 것 — 대신 차콜 `#414141`을 사용한다.
- 주요 CTA를 `#0B6EC5`, `#6366F1`, `#7C3AED`로 만들지 말 것 — 행동 색은 오렌지 `#F35815`이다.
- 링크를 `#F35815`로 통일하지 말 것 — 링크는 블루 `#0B6EC5`, hover/focus 장식은 `#1E9DE7`이다.
- 히어로 제목에 보라 그라디언트 `#667EEA` → `#764BA2`를 쓰지 말 것 — 제목은 `#111111` 텍스트와 `#F35815` left rule로 충분하다.
- 로고 wall 배경을 카드 회색 `#F3F4F6` 또는 테두리 없는 흰 카드로 만들지 말 것 — `#FFFFFF` 셀과 `#414141` 얇은 그리드 라인이 필요하다.
- primary button에 `border-radius: 9999px`를 쓰지 말 것 — 기본 CTA는 `border-radius: 0`인 square command이다.
- body를 `Inter`, `Roboto`, `Arial`, `system-ui` 산세리프 중심으로 바꾸지 말 것 — primary voice는 `ui-monospace`이다.
- `box-shadow: 0 20px 60px rgba(0,0,0,.15)` 같은 부드러운 카드 그림자를 쓰지 말 것 — border와 `#1E9DE7` focus ring이 깊이 역할을 한다.
- 80px 이상 hero display type과 중앙 정렬 CTA stack을 쓰지 말 것 — PlanetScale은 문서형 left-rule hero와 16px mono density가 핵심이다.

### Absent / None / Zero / Never (Negative-Space Identity)

- Lab demo video autoplay on hero: absent. The runbook does not perform; it documents.
- Toolbox iconography / wrench illustrations: zero. Tools are typeset, not drawn.
- Engineering blueprint mesh background: never. The page surface is flat printed paper.
- Animated benchmark chart in the hero: none. Numbers are inline body copy.
- Decorative server-rack 3D render: absent. The proof grid replaces the diagram.
- Second action color competing with orange: none. Blue is link-only, not a CTA.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- phase1 artifacts were reused from `insane-design/planetscale`; no fresh May 3 live fetch was performed, so content or CSS may have shifted after the captured April 20 bundle.
- The captured CSS does not expose a public design-token namespace such as `--ps-*`; token names in this guide are normalized aliases for implementation clarity, while raw observed tokens remain listed.
- The screenshot used for visual interpretation is `hero-cropped.png`; below-the-fold component behavior is inferred from HTML text and CSS selectors rather than a full visual crawl.
- `default_theme: light` is based on the visible homepage screenshot and CSS defaults, even though `prefers-color-scheme: dark` branches exist.
- Framework identification is intentionally conservative because the stored HTML did not expose a clear `__NEXT_DATA__` marker.
- Logo colors were treated as proof-content noise and not as PlanetScale UI palette colors.
