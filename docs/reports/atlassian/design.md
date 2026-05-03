---
schema_version: 3.2
slug: atlassian
service_name: Atlassian
site_url: https://www.atlassian.com
fetched_at: 2026-04-20T19:58:00+09:00
default_theme: mixed
brand_color: "#1868DB"
primary_font: "Atlassian Sans"
font_weight_normal: 400
token_prefix: ds

bold_direction: Collaborative Enterprise
aesthetic_category: Refined SaaS
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: saas-marketing
archetype_confidence: high
design_system_level: lv3
design_system_level_evidence: "Atlassian Design System tokens are present as --ds-* variables, with 490 custom properties, semantic aliases, font tokens, spacing tokens, shadows, and component state colors."

colors:
  primary: "#1868DB"
  primary-hover: "#1558BC"
  primary-pressed: "#144794"
  primary-dark: "#1C2B42"
  surface: "#FFFFFF"
  surface-sunken: "#F8F8F8"
  text-primary: "#292A2E"
  text-muted: "#505258"
  border: "#0B120E24"
  focus: "#4688EC"
  event-accent: "#FCA700"
  discovery: "#803FA5"
typography:
  display: "Charlie Display"
  brand_body: "Charlie Text"
  ui: "Atlassian Sans"
  mono: "Atlassian Mono"
  ladder:
    - { token: brand-hero, size: "clamp-scale observed; screenshot about 64px", weight: 800, tracking: "-1px" }
    - { token: ds-heading-xxlarge, size: "2rem", weight: 653, line_height: "2.25rem" }
    - { token: ds-heading-xlarge, size: "1.75rem", weight: 653, line_height: "2rem" }
    - { token: ds-body, size: "0.875rem", weight: 400, line_height: "1.25rem" }
  weights_used: [400, 500, 600, 653, 700, 800]
  weights_absent: []
components:
  button-primary: { bg: "{colors.primary}", hover: "{colors.primary-hover}", pressed: "{colors.primary-pressed}", radius: "999px", padding: "6px 22px" }
  button-event: { bg: "{colors.event-accent}", text: "{colors.text-primary}", radius: "999px", padding: "12px 24px" }
  nav-link: { color: "{colors.text-primary}", weight: 500, height: "68px" }
  surface-card: { bg: "{colors.surface}", shadow: "var(--ds-shadow-raised)", radius: "8px" }
---

# DESIGN.md - Atlassian (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Atlassian is not using the old corporate-blue-only homepage anymore. The current page is a teamwork operating system dressed as a conference keynote: a white product catalogue above and below, a black Team '26 stage in the middle, and a dense Atlassian Design System machinery room underneath. The important blue is `#1868DB` (`{colors.primary}`), not the legacy `#0052CC` that still appears as residue in older CSS. That blue behaves like wayfinding tape on an enterprise campus: links, selected states, primary actions, and brand text all return to it, while the hero is allowed to borrow the spotlight from `#FCA700` event CTAs and chromatic stage graphics.

The strongest visual move is contrast switching. The navigation is a clean airport departures board for work software: white, precise, category-heavy, and built for people who already know they have somewhere to go. Immediately below it, the Team '26 band turns into a keynote theatre with `#101214` walls, inverse white type, lime/purple/blue event color, and media framed like a live demo screen. Then the page drops back to `#FFFFFF` (`{colors.surface}`) and turns "human+AI" into the central typographic object, as if the keynote lights shut off and the product catalogue rolls back into place.

This is not a gradient SaaS hero and not a luxury empty room. Atlassian's white space is closer to a well-labeled enterprise expo hall: many booths, clear aisles, no ornamental fog. The page wants many doors on the first viewport: products, collections, teams, AI agents, conference registration, enterprise navigation, search, and sign-in. The 12-column grid and `24px` gaps keep that density from becoming a drawer of loose brochures.

Typography carries more identity than most of the color system. Atlassian splits the voice into two registers: `Charlie Display` / `Charlie Text` are the human announcer on the keynote stage, while `Atlassian Sans` / `Atlassian Mono` are the product operations staff keeping labels, menus, and cards exact. The unusual DS heading weight `653` is part of the signature; it lands between friendly and procedural, like a conference badge printed in good ink rather than a generic bold web font.

The negative identity matters. There is no second global brand color competing with `{colors.primary}`; yellow is event-scoped, purple/discovery is semantic, and black is a stage surface rather than a site-wide dark mode. Shadows are not lifestyle haze. They appear as DS perimeter shadows on menus, overlays, and raised cards, more like laminated wayfinding panels than floating glass. The result is enterprise collaboration staged as a human+AI event poster, but with every poster edge snapped back to a token grid.

### Key Characteristics

- Current canonical blue is `#1868DB` (`--ds-background-brand-bold`, `--ds-text-brand`, `--ds-link`), replacing the older `#0052CC` as the practical UI anchor.
- Mixed homepage theme: white navigation and body sections, black event hero, and chromatic event side bands.
- Brand typography is split: `Charlie Display` / `Charlie Text` for marketing expression, `Atlassian Sans` for DS/UI precision.
- DS token namespace is explicit and broad: `--ds-*` color, font, spacing, shadow, surface, link, border, and state variables.
- Buttons are rounded pills, not square enterprise buttons; event CTA uses yellow/orange `#FCA700`, while product CTAs use blue `#1868DB`.
- Navigation is high-density but calm: logo left, dropdown product taxonomy, search divider, sign-in link.
- Cards use surface contrast and DS shadows rather than decorative gradients.
- Product and collection grids lean on 12-column structure with `24px` gaps and max-width bands around `72pc` / `1152px`.
- Accent families exist in the DS palette, but most accents are semantic or event-specific, not free decoration.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Collaborative Enterprise
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **enterprise collaboration staged as a human+AI event poster**으로 기억된다.
> **Code Complexity**: high — broad DS token graph, mixed-theme homepage bands, dropdown navigation, video/photo hero, and multi-state component tokens.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Atlassian처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Atlassian Sans", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}
.brand-hero {
  font-family: "Charlie Display", "Atlassian Sans", ui-sans-serif, sans-serif;
  font-weight: 800;
  letter-spacing: -1px;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #292A2E; --muted: #505258; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #1868DB; --brand-hover: #1558BC; --event: #FCA700; }
```

**절대 하지 말아야 할 것 하나**: Atlassian을 `#0052CC` 단색 블루 SaaS로 복원하지 말 것. 현재 홈페이지의 실전 anchor는 `#1868DB`이고, hero에서는 `#FCA700` event CTA와 black-stage band가 강하게 등장한다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.atlassian.com` |
| Fetched | 2026-04-20T19:58:00+09:00 |
| Extractor | reused existing phase1 artifacts: HTML + CSS + screenshot + JSON token extraction |
| HTML size | 1,230,803 bytes |
| CSS files | 5 files, about 354,679 chars |
| Phase1 JSON | `brand_candidates.json`, `resolved_tokens.json`, `typography.json`, `alias_layer.json` |
| Custom properties | 490 total vars, 446 resolved |
| Token prefix | `ds` |
| Method | CSS custom properties and frequency candidates parsed first; screenshot and HTML used for layout interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React/SSR marketing page with generated atomic classes and large inline style payload.
- **Design system**: Atlassian Design System - prefix `--ds-*`.
- **CSS architecture**:
  ```css
  --ds-background-*      semantic surfaces, actions, selected states
  --ds-text-*            text roles, accent text, inverse text
  --ds-border-*          borders, focus rings, semantic borders
  --ds-space-*           spacing ladder from 0rem to 5rem
  --ds-font-*            heading/body/code shorthands and font families
  --ds-shadow-*          raised / overlay / overflow elevation atoms
  ```
- **Class naming**: generated atomic/hash classes such as `._5cs9130s`, plus component-level semantic anchors in HTML.
- **Default theme**: mixed. Page shell uses `#FFFFFF`, event hero uses near-black `#101214`, DS text uses `#292A2E`.
- **Font loading**: custom Atlassian/Charlie font CSS is present: `Atlassian Sans`, `Atlassian Mono`, `Charlie Display`, `Charlie Text`.
- **Canonical anchor**: `--ds-background-brand-bold: #1868DB`, `--ds-text-brand: #1868DB`, `--ds-link: #1868DB`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Charlie Display` for brand/marketing hero expression.
- **Brand body font**: `Charlie Text` appears in marketing typography stacks.
- **UI font**: `Atlassian Sans` is the DS body and heading workhorse.
- **Code font**: `Atlassian Mono`.
- **Weight normal / bold**: `400` / `653` for DS heading tokens; homepage brand hero also uses heavier `700-800` display weights.

```css
:root {
  --ds-font-family-heading: "Atlassian Sans", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, "Helvetica Neue", sans-serif;
  --ds-font-family-body:    "Atlassian Sans", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, "Helvetica Neue", sans-serif;
  --ds-font-family-code:    "Atlassian Mono", ui-monospace, Menlo, "Segoe UI Mono", "Ubuntu Mono", monospace;
  --ds-font-family-brand-heading: "Charlie Display", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, "Helvetica Neue", sans-serif;
  --ds-font-family-brand-body:    "Charlie Text", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, "Helvetica Neue", sans-serif;
}
```

### Note on Font Substitutes

- **Charlie Display unavailable**: use `Atlassian Sans` or `Inter` at 800 for hero only, then tighten `letter-spacing` to about `-1px`. Do not use Inter 600 as a direct substitute; it loses the heavy, friendly event-poster tone.
- **Atlassian Sans unavailable**: use `Inter` at 400 for body and 650/700 for headings. Preserve DS line-height ratios rather than matching only size.
- **Atlassian Mono unavailable**: use `ui-monospace`, `Menlo`, or `Segoe UI Mono` at 400. Code is a support role; it should not become the visual signature.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `brand-hero-display` | about 64px observed in screenshot | 800 | tight / display | `-1px` |
| `--ds-font-heading-xxlarge` | `2rem` | 653 | `2.25rem` | normal |
| `--ds-font-heading-xlarge` | `1.75rem` | 653 | `2rem` | normal |
| `--ds-font-heading-large` | `1.5rem` | 653 | `1.75rem` | normal |
| `--ds-font-heading-medium` | `1.25rem` | 653 | `1.5rem` | normal |
| `--ds-font-body-large` | `1rem` | 400 | `1.5rem` | normal |
| `--ds-font-body` | `0.875rem` | 400 | `1.25rem` | normal |
| `--ds-font-body-small` | `0.75rem` | 400 | `1rem` | normal |
| `--ds-font-code` | `0.875em` | 400 | `1` | normal |

> ⚠️ The unusual DS heading weight is `653`, not a generic 600 or 700. Marketing hero copy can go heavier, but product UI headings should preserve the DS token.

### Principles

1. Brand hero typography and DS typography are separate systems. Use `Charlie Display` for campaign-scale statements, then return to `Atlassian Sans` for UI and product taxonomy.
2. DS headings use weight `653`, which gives a crisp enterprise voice without becoming cartoon-bold.
3. Body copy is `0.875rem/1.25rem` in the DS layer, but homepage marketing paragraphs scale larger through page-level classes.
4. Heavy display text is reserved for identity moments such as "team'26" and "human+AI"; do not make every card headline 800.
5. Letter-spacing adjustments are sparse. Use `-1px` only on display-scale hero text; keep body tracking normal.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (6 steps)

| Token | Hex |
|---|---|
| `--ds-background-brand-subtlest` | `#E9F2FE` |
| `--ds-background-brand-subtlest-hovered` | `#CFE1FD` |
| `--ds-background-brand-subtlest-pressed` | `#ADCBFB` |
| `--ds-background-brand-bold` | `#1868DB` |
| `--ds-background-brand-bold-hovered` | `#1558BC` |
| `--ds-background-brand-bold-pressed` | `#144794` |
| `--ds-background-brand-boldest` | `#1C2B42` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--ds-background-brand-boldest` | `#1C2B42` |
| `--ds-background-brand-boldest-hovered` | `#123263` |
| `--ds-background-brand-boldest-pressed` | `#144794` |
| event hero background | `#101214` |
| inverse text | `#FFFFFF` |

### 06-3. Neutral Ramp

| Step | Light | Dark/Ink |
|---|---|---|
| surface | `#FFFFFF` | `#101214` |
| sunken | `#F8F8F8` | `#1E1F21` |
| hovered | `#F0F1F2` | `#292A2E` |
| pressed | `#DDDEE1` | `#3B3D42` |
| muted text | `#505258` | `#A9ABAF` |
| subtlest text | `#6B6E76` | `#B7B9BE` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Blue / information | `--ds-text-accent-blue` | `#1558BC` |
| Purple / discovery | `--ds-text-discovery` | `#803FA5` |
| Yellow / event accent | `--rovo-yellow-color` / event CTA | `#FCA700` |
| Green / success | `--ds-text-success` | `#4C6B1F` |
| Red / danger | `--ds-text-danger` | `#AE2E24` |
| Teal | `--ds-text-accent-teal` | `#206A83` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--ds-text` | `#292A2E` | Primary body text |
| `--ds-text-subtle` | `#505258` | Muted navigation/body support |
| `--ds-text-inverse` | `#FFFFFF` | Dark hero and inverse buttons |
| `--ds-text-brand` | `#1868DB` | Brand links and selected text |
| `--ds-link` | `#1868DB` | Links |
| `--ds-link-pressed` | `#1558BC` | Pressed link |
| `--ds-border` | `#0B120E24` | Hairline border |
| `--ds-border-focused` | `#4688EC` | Focus ring |
| `--ds-surface` | `#FFFFFF` | Card/page surface |
| `--ds-surface-sunken` | `#F8F8F8` | Subtle background well |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--ds-background-selected-bold` | `#1868DB` | selected/primary filled state |
| `--ds-background-selected-bold-hovered` | `#1558BC` | primary hover |
| `--ds-background-selected-bold-pressed` | `#123263` | primary pressed |
| `--ds-background-input` | `#FFFFFF` | input default |
| `--ds-background-input-hovered` | `#F8F8F8` | input hover |
| `--ds-background-neutral` | `#0515240F` | neutral subtle fill |
| `--ds-background-neutral-bold` | `#292A2E` | dark neutral button/chip |
| `--ds-surface-raised` | `#FFFFFF` | elevated card |

### 06-7. Dominant Colors (실제 DOM/CSS 빈도 순)

| Token / Role | Hex | Frequency signal |
|---|---|---:|
| event/black stage | `#101214` | highest chromatic-like frequency in phase1 |
| brand primary | `#1868DB` | 596 in phase1 candidates; 35 CSS hits |
| muted text | `#505258` | 235 in phase1 candidates |
| surface | `#FFFFFF` | 214 in phase1 candidates |
| brand hover | `#1558BC` | 138 in phase1 candidates |
| surface-sunken | `#F8F8F8` | 134 in phase1 candidates |
| discovery purple | `#803FA5` | 123 in phase1 candidates |
| event yellow | `#FCA700` | 46 in phase1 candidates |

### 06-8. Color Stories

**`{colors.primary}` (`#1868DB`)** - The practical Atlassian blue. It owns links, selected states, brand text, borders, and primary product UI. Treat this as the canonical UI anchor, not the older `#0052CC`.

**`{colors.surface}` (`#FFFFFF`)** - The main floor. Atlassian uses white to make a complex product taxonomy readable; density comes from navigation and grids, not from tinted backgrounds everywhere.

**`{colors.text-primary}` (`#292A2E`)** - The DS ink. It is softer than `#000000`, which keeps enterprise density from becoming harsh.

**`{colors.event-accent}` (`#FCA700`)** - A campaign accent, not the global brand color. It works on the black Team '26 stage and should be scoped to event/announcement CTAs.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--ds-space-0` | `0rem` | reset |
| `--ds-space-025` | `0.125rem` | icon micro padding |
| `--ds-space-050` | `0.25rem` | compact icon padding |
| `--ds-space-075` | `0.375rem` | button vertical padding |
| `--ds-space-100` | `0.5rem` | small gap |
| `--ds-space-150` | `0.75rem` | compact rows |
| `--ds-space-200` | `1rem` | standard component padding |
| `--ds-space-250` | `1.25rem` | wider component padding |
| `--ds-space-300` | `1.5rem` | card/section gap |
| `--ds-space-400` | `2rem` | grid gutters and section interior |
| `--ds-space-500` | `2.5rem` | large block spacing |
| `--ds-space-600` | `3rem` | section stack |
| `--ds-space-800` | `4rem` | large section air |
| `--ds-space-1000` | `5rem` | top-level section separation |

**주요 alias**:
- `--cl-gap` -> `24px` in the collected CSS, used by the 12-column calculation.
- `--content-columns` -> `1 / span 12`, describing full-grid content tracks.

### Whitespace Philosophy

Atlassian whitespace is operational rather than luxurious. The system gives the nav and product menus enough room to hold many destinations, then uses `24px`, `32px`, `64px`, and `80px`-class vertical bands to keep the page from turning into a directory.

The homepage alternates density: the Team '26 hero is tight and poster-like, while the "human+AI superteam" section opens with centered type and broad white margins. That contrast is the point. Use dense grids for product choice, but protect the campaign headline with a full breath of white space.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Context |
|---|---:|---|
| small DS radius | `3px` / `4px` | compact controls and small surfaces |
| medium DS radius | `6px` | forms and standard components |
| card radius | `8px` | marketing cards and containers |
| large radius | `9pt` / `12px` | larger panels |
| circular | `50%` | icon/video controls |
| pill CTA | `999px` visual convention | event and product CTAs |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `--ds-shadow-raised` | `0px 1px 1px #1E1F2140, 0px 0px 1px #1E1F214F` | raised cards, menus |
| `--ds-shadow-overlay` | `0px 8px 12px #1E1F2126, 0px 0px 1px #1E1F214F` | dropdowns, overlays, hover elevation |
| `--ds-shadow-overflow` | `0px 0px 8px #1E1F2129, 0px 0px 1px #1E1F211F` | scroll/overflow affordance |
| legacy fallback | `0 8px 9pt #091e4226, 0 0 1px #091e424f` | older ADG-style shadow values still present |

Atlassian shadows are multi-layer utility shadows. Do not replace them with a single soft card shadow; the 1px perimeter layer is part of the DS look.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| transform ease | `transform .25s ease-in-out` | cards/media movement |
| quick background | `background .1s ease-out` | small interactive states |
| hover/pressed state | `background-color .15s, border-color .15s` | controls |
| reduced motion branch | `prefers-reduced-motion: reduce` | accessibility branch present |
| no-preference branch | `prefers-reduced-motion: no-preference` | motion-enabled branch present |

Motion exists, but it is not the identity. Keep transitions short and state-driven; do not add parallax or large scroll drama unless reproducing the event hero media treatment.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: commonly `72pc` (`1152px`) and `75pc` (`1200px`) bands; some wide bands reach `90pc` (`1440px`).
- **Grid type**: CSS Grid and Flexbox mix.
- **Column count**: 12-column grid appears as `repeat(12, 1fr)` / `repeat(12, minmax(0, 1fr))`.
- **Gutter**: `--cl-gap: 24px`, with `--ds-space-400: 2rem` used for broader component spacing.

### Hero

- **Pattern Summary**: mixed-stage homepage: white nav + black Team '26 media banner + centered white AI-team headline below.
- Layout: event hero is two-column: left copy/CTA, right image/video frame; following hero headline is centered one-column.
- Background: `#101214` black stage for event hero; `#FFFFFF` for main product narrative.
- **Background Treatment**: solid black stage plus chromatic side bands and embedded photo/video; white body uses typography and underline accent rather than decorative background.
- H1: `Charlie Display`-like heavy display, about 64px in screenshot, weight 800, tight tracking.
- Max-width: right media frame and copy sit inside wide 12-column container; body headline sits centered with a large text max-width.

### Section Rhythm

```css
section {
  padding: var(--ds-space-800, 4rem) var(--ds-space-400, 2rem);
  max-width: 72pc;
}
.grid {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: 24px;
}
```

### Card Patterns

- **Card background**: `#FFFFFF` or `#F8F8F8` depending on surface depth.
- **Card border**: `1px solid #0B120E24` / `--ds-border`.
- **Card radius**: `8px` is the common marketing-card feel; DS controls can be smaller.
- **Card padding**: `24px` / `32px` from `--ds-space-300` and `--ds-space-400`.
- **Card shadow**: `--ds-shadow-raised` default, `--ds-shadow-overlay` on stronger hover/overlay moments.

### Navigation Structure

- **Type**: horizontal mega-nav with dropdown product taxonomy.
- **Position**: static/sticky-like top shell in screenshot; white bar above hero.
- **Height**: about `68px` observed in screenshot.
- **Background**: `#FFFFFF`.
- **Border**: subtle separator; search divider uses a vertical hairline.
- **Behavior**: product, solution, why, resources dropdowns; search icon and sign-in on the right.

### Content Width

- **Prose max-width**: marketing copy around `20pc` to `29pc` in extracted max-width samples.
- **Container max-width**: `72pc` / `75pc` / `90pc` depending on section.
- **Sidebar width**: not a homepage primary pattern; mega-menu panels replace sidebar behavior.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `0-29.99rem` | compact view; nav likely collapses |
| Small | `30rem` | early layout upgrade |
| Tablet | `48rem` / `768px` | two-column and menu changes begin |
| Desktop | `64rem` / `1024px` | full grid and desktop nav patterns |
| Wide | `1280px` / `1306px+` | wide hero/container adjustments |

### Touch Targets

- **Minimum tap size**: DS conventions imply 40-44px targets; homepage buttons visually exceed this in hero CTAs.
- **Button height (mobile)**: not directly measured from mobile screenshot; use `44px` minimum when implementing.
- **Input height (mobile)**: not surfaced on homepage capture; preserve DS input background tokens.

### Collapsing Strategy

- **Navigation**: horizontal mega-nav on desktop; mobile collapse not directly captured, but breakpoint CSS is present.
- **Grid columns**: 12-column desktop collapses to `1fr` / `repeat(2, 1fr)` / `repeat(3, 1fr)` variants.
- **Sidebar**: not applicable for homepage.
- **Hero layout**: event hero should collapse from two-column media/copy to stacked copy/media.

### Image Behavior

- **Strategy**: media frame in the event hero; product/story imagery should use controlled aspect ratios.
- **Max-width**: `100%` appears repeatedly.
- **Aspect ratio handling**: media should be clipped/cropped intentionally rather than stretching.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<a class="atl-button atl-button--primary" href="#">Get started</a>
<a class="atl-button atl-button--event" href="#">Register now</a>
```

| State | Primary spec |
|---|---|
| default | bg `#1868DB`, text `#FFFFFF`, radius pill, padding around `6px 22px` or `12px 24px` by context |
| hover | bg `#1558BC` |
| active / pressed | bg `#144794` or `#123263` |
| focus | ring/border `#4688EC` |
| disabled | text `#080F214A`, border/fill `#0515240F` |
| event variant | bg `#FCA700`, text `#292A2E`, black-stage context |

### Badges

Atlassian badges should use semantic DS fills rather than invented pastel chips.

| Variant | Background | Text |
|---|---|---|
| selected | `#E9F2FE` | `#1868DB` |
| discovery | `#F8EEFE` | `#803FA5` |
| success | `#EFFFD6` or green subtle family | `#4C6B1F` |
| warning | `#FFF5DB` or yellow/orange subtle family | `#9E4C00` |

### Cards & Containers

```html
<article class="atl-card">
  <h3>Jira</h3>
  <p>Flexible project management</p>
</article>
```

| Property | Value |
|---|---|
| background | `#FFFFFF` |
| border | `1px solid #0B120E24` |
| radius | `8px` |
| padding | `24px` or `32px` |
| shadow | default none or `--ds-shadow-raised`; overlay/hover can use `--ds-shadow-overlay` |
| hover | subtle shadow/border shift, no large transform |

### Navigation

```html
<nav class="atl-nav">
  <a class="atl-logo">Atlassian</a>
  <button>Products</button>
  <button>Solutions</button>
  <button>Why Atlassian?</button>
  <a>Enterprise</a>
  <a class="atl-signin">Sign in</a>
</nav>
```

| Part | Spec |
|---|---|
| shell | `#FFFFFF`, about `68px` high |
| link text | `#292A2E`, `Atlassian Sans`, 14-16px, medium |
| sign in | `#1868DB` |
| search divider | subtle vertical hairline |
| dropdown | surface `#FFFFFF`, overlay shadow, product taxonomy cards |

### Inputs & Forms

| State | Token |
|---|---|
| default bg | `--ds-background-input: #FFFFFF` |
| hover bg | `--ds-background-input-hovered: #F8F8F8` |
| pressed bg | `--ds-background-input-pressed: #FFFFFF` |
| border | `--ds-border-input: #8C8F97` |
| focus | `--ds-border-focused: #4688EC` |
| error | `--ds-text-danger: #AE2E24`, `--ds-border-danger: #E2483D` |

### Hero Section

The homepage hero is not a generic centered SaaS hero. It has two stacked identities:

- **Event stage**: black `#101214`, Team '26 display text, event metadata row with icons, yellow `#FCA700` CTA, media frame on the right, chromatic side bands.
- **AI-team statement**: white floor, centered oversized display text, `human+AI` emphasized in black with a yellow underline scribble.

### 13-2. Named Variants

| Variant | Spec |
|---|---|
| `button-primary` | `#1868DB` fill, `#FFFFFF` text, hover `#1558BC`, pressed `#144794`, pill radius |
| `button-event-yellow` | `#FCA700` fill, `#292A2E` text, pill radius, black-stage context |
| `button-link-arrow` | text link with arrow, no filled surface, usually inverse or brand text depending on section |
| `nav-dropdown-trigger` | text button, medium weight, down chevron, no fill by default |
| `surface-card-raised` | `#FFFFFF`, `--ds-shadow-raised`, `8px` radius, border optional |
| `semantic-badge-selected` | `#E9F2FE` bg, `#1868DB` text |

### 13-3. Signature Micro-Specs

```yaml
rebrand-blue-wayfinding:
  description: "Current Atlassian blue works as navigation tape across the DS layer, while old #0052CC stays residue."
  technique: "Use #1868DB /* {colors.primary} */ via --ds-background-brand-bold, --ds-text-brand, and --ds-link; hover #1558BC, pressed #144794."
  applied_to: ["{component.button-primary}", "{component.nav-link}", "{component.semantic-badge-selected}", "selected states"]
  visual_signature: "The page reads unmistakably Atlassian without reverting to the heavier legacy corporate blue."

black-stage-event-band:
  description: "A scoped keynote-theatre surface interrupts the white SaaS catalogue without becoming a global dark mode."
  technique: "Set stage background #101214, inverse text #FFFFFF, event CTA #FCA700, and keep media/photo frame inside the band."
  applied_to: ["Team '26 hero banner", "{component.button-event}", "event media frame"]
  visual_signature: "Enterprise software suddenly behaves like a live conference poster, then snaps back to white product structure."

charlie-display-ds-split:
  description: "Brand moments use Charlie fonts, while reusable UI returns to Atlassian Sans and DS heading weights."
  technique: "Use Charlie Display at about 64px / 800 / -1px for hero-scale copy; use --ds-font-heading-* at weight 653 and --ds-font-body at 400 for UI."
  applied_to: ["hero headline", "event banner", "product taxonomy cards", "navigation"]
  visual_signature: "A friendly campaign voice sits on top of disciplined enterprise interface typography."

perimeter-overlay-shadow:
  description: "Elevation is a two-layer DS shadow with a crisp 1px perimeter, not a generic cloudy card shadow."
  technique: "Raised: 0px 1px 1px #1E1F2140, 0px 0px 1px #1E1F214F; overlay: 0px 8px 12px #1E1F2126, 0px 0px 1px #1E1F214F."
  applied_to: ["{component.surface-card}", "dropdowns", "overlays", "hover cards"]
  visual_signature: "Panels feel laminated and precise, with edge definition even when the soft shadow appears."

twelve-column-product-catalogue:
  description: "Dense enterprise choice is made readable by a fixed catalogue grid rather than by removing options."
  technique: "Use repeat(12, minmax(0, 1fr)) or repeat(12, 1fr), --cl-gap: 24px, and max-width bands around 72pc / 1152px."
  applied_to: ["product grids", "collection sections", "mega-nav taxonomy", "content containers"]
  visual_signature: "Many product doors remain visible, but the page feels like a mapped expo hall instead of a link directory."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | collaboration outcome first, AI as team amplifier | "Unleash your human+AI superteam" |
| Event CTA | direct registration/action | "Register now" |
| Secondary CTA | exploratory link with arrow | "See the agenda ->" |
| Product label | noun + short capability line | "Jira - Flexible project management" |
| Tone | confident, team-oriented, enterprise-safe, optimistic about AI |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Atlassian-inspired root tokens */
:root {
  /* Fonts */
  --atl-font-ui: "Atlassian Sans", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --atl-font-display: "Charlie Display", "Atlassian Sans", ui-sans-serif, sans-serif;
  --atl-font-brand-body: "Charlie Text", "Atlassian Sans", ui-sans-serif, sans-serif;
  --atl-font-mono: "Atlassian Mono", ui-monospace, Menlo, "Segoe UI Mono", monospace;
  --atl-font-weight-normal: 400;
  --atl-font-weight-heading: 653;
  --atl-font-weight-display: 800;

  /* Brand */
  --atl-color-brand-subtlest: #E9F2FE;
  --atl-color-brand-pressed-soft: #ADCBFB;
  --atl-color-brand: #1868DB;
  --atl-color-brand-hover: #1558BC;
  --atl-color-brand-pressed: #144794;
  --atl-color-brand-dark: #1C2B42;

  /* Surfaces */
  --atl-bg-page: #FFFFFF;
  --atl-bg-sunken: #F8F8F8;
  --atl-bg-stage: #101214;
  --atl-text: #292A2E;
  --atl-text-muted: #505258;
  --atl-text-inverse: #FFFFFF;
  --atl-border: #0B120E24;
  --atl-focus: #4688EC;
  --atl-event: #FCA700;

  /* Spacing */
  --atl-space-sm: 0.5rem;
  --atl-space-md: 1rem;
  --atl-space-lg: 1.5rem;
  --atl-space-xl: 2rem;
  --atl-space-2xl: 4rem;

  /* Radius + elevation */
  --atl-radius-sm: 4px;
  --atl-radius-md: 8px;
  --atl-radius-pill: 999px;
  --atl-shadow-raised: 0px 1px 1px #1E1F2140, 0px 0px 1px #1E1F214F;
  --atl-shadow-overlay: 0px 8px 12px #1E1F2126, 0px 0px 1px #1E1F214F;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js - Atlassian-inspired
module.exports = {
  theme: {
    extend: {
      colors: {
        atl: {
          brand: '#1868DB',
          brandHover: '#1558BC',
          brandPressed: '#144794',
          brandSubtlest: '#E9F2FE',
          stage: '#101214',
          surface: '#FFFFFF',
          sunken: '#F8F8F8',
          text: '#292A2E',
          muted: '#505258',
          border: '#0B120E24',
          event: '#FCA700',
        },
      },
      fontFamily: {
        sans: ['Atlassian Sans', 'ui-sans-serif', 'system-ui'],
        display: ['Charlie Display', 'Atlassian Sans', 'ui-sans-serif'],
        mono: ['Atlassian Mono', 'ui-monospace', 'Menlo'],
      },
      fontWeight: {
        dsHeading: '653',
      },
      borderRadius: {
        atl: '8px',
        pill: '999px',
      },
      boxShadow: {
        atlRaised: '0px 1px 1px #1E1F2140, 0px 0px 1px #1E1F214F',
        atlOverlay: '0px 8px 12px #1E1F2126, 0px 0px 1px #1E1F214F',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `--ds-background-brand-bold` | `#1868DB` |
| Brand hover | `--ds-background-brand-bold-hovered` | `#1558BC` |
| Background | `--ds-surface` | `#FFFFFF` |
| Stage background | event hero | `#101214` |
| Text primary | `--ds-text` | `#292A2E` |
| Text muted | `--ds-text-subtle` | `#505258` |
| Border | `--ds-border` | `#0B120E24` |
| Focus | `--ds-border-focused` | `#4688EC` |
| Event CTA | event accent | `#FCA700` |
| Error | `--ds-text-danger` | `#AE2E24` |

### Example Component Prompts

#### Hero Section

```text
Atlassian homepage style hero를 만들어줘.
- 상단 nav는 #FFFFFF 배경, #292A2E 링크, Sign in은 #1868DB.
- 첫 band는 #101214 black stage, 왼쪽에 heavy Charlie Display headline, 오른쪽에 media/image frame.
- CTA는 event context면 #FCA700 pill + #292A2E text, product context면 #1868DB pill + #FFFFFF text.
- 아래 section은 #FFFFFF 배경, centered oversized "human+AI" headline, tight display tracking.
- 12-column grid, max-width 1152px, gap 24px를 사용.
```

#### Card Component

```text
Atlassian DS 스타일 카드 컴포넌트를 만들어줘.
- background #FFFFFF, border 1px solid #0B120E24, radius 8px.
- padding 24px 또는 32px.
- hover 시 --ds-shadow-overlay에 가까운 2-layer shadow: 0px 8px 12px #1E1F2126, 0px 0px 1px #1E1F214F.
- 제목은 Atlassian Sans, weight 653, 본문은 400, #505258.
```

#### Badge

```text
Atlassian semantic badge를 만들어줘.
- selected: bg #E9F2FE, text #1868DB.
- discovery: bg #F8EEFE, text #803FA5.
- success: green subtle family, text #4C6B1F.
- radius는 pill이지만 과한 glow나 gradient는 쓰지 마.
```

#### Navigation

```text
Atlassian 스타일 상단 네비게이션을 만들어줘.
- 높이 약 68px, 배경 #FFFFFF.
- 좌측 로고, Products/Solutions/Why Atlassian?/Resources dropdown trigger, Enterprise plain link.
- 오른쪽 search icon, thin divider, Sign in #1868DB.
- dropdown은 #FFFFFF surface + DS overlay shadow.
```

### Iteration Guide

- **색상 변경 시**: `#1868DB` 계열을 brand action으로 유지하고, `#FCA700`은 event/campaign CTA에만 제한한다.
- **폰트 변경 시**: display와 UI를 분리한다. 모든 것을 Inter 하나로 통일하면 Atlassian 특유의 human+enterprise split이 사라진다.
- **여백 조정 시**: `--ds-space-*` ladder 또는 `24px` 12-column grid gap을 기준으로 움직인다.
- **새 컴포넌트 추가 시**: shadow는 반드시 2-layer perimeter 포함 형태로 둔다.
- **다크 모드**: 홈페이지 전체 dark가 아니라 black stage section이다. dark section을 만들 때 inverse text와 scoped accent를 함께 설계한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#1868DB` as the current canonical Atlassian action/brand blue.
- Preserve the `--ds-*` naming model when building reusable tokens.
- Split brand typography from product UI typography: `Charlie Display` / `Charlie Text` for marketing, `Atlassian Sans` for DS surfaces.
- Use white `#FFFFFF` and ink `#292A2E` as the default enterprise floor.
- Scope `#FCA700` to event/campaign CTA moments, especially on black hero bands.
- Use `--ds-space-*` and 12-column grid rhythm for dense product/category sections.
- Use 2-layer DS shadows for overlays and hover cards.

### ❌ DON'T

- 색상 primary를 `#0052CC`로 두지 말 것 — 대신 현재 UI anchor `#1868DB` 사용.
- 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 DS ink `#292A2E` 사용.
- 기본 페이지 배경을 `#F4F5F7`로 두지 말 것 — 현재 homepage floor는 `#FFFFFF`, subtle well은 `#F8F8F8` 사용.
- event CTA를 `#1868DB`로만 두지 말 것 — Team/event band에서는 `#FCA700` CTA가 관측된다.
- hover primary를 같은 `#1868DB`로 고정하지 말 것 — hover에는 `#1558BC`, pressed에는 `#144794` 계열 사용.
- dark hero 텍스트를 `#292A2E`로 두지 말 것 — black stage에서는 `#FFFFFF` inverse text 사용.
- border를 `#DDDEE1` 단색으로만 두지 말 것 — 기본 hairline은 alpha border `#0B120E24`가 더 가깝다.
- 모든 headline을 `font-weight: 700`으로 통일하지 말 것 — DS heading은 `653`, campaign display는 `800`까지 분리한다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- No single blue-only brand system: `#1868DB` is core, but the homepage deliberately makes room for black stage, yellow event CTA, purple/lime/green event graphics.
- No generic Inter-only typography: Atlassian identity depends on the split between Charlie fonts and Atlassian Sans.
- No pure-black body text: `#292A2E` is the primary ink.
- No all-gradient SaaS hero: the current hero uses a stage/photo/media composition, not a purple-blue mesh.
- No universal card shadow: many surfaces stay flat; elevation appears for dropdowns, overlays, and selected hover contexts.
- No arbitrary pastel badge palette: accent colors are DS semantic families.
- No square primary CTA: buttons read as pills/capsules in hero/action contexts.
- No decorative borders on every card: surface contrast, spacing, and subtle DS hairlines carry structure.
- No dark homepage identity: dark is section-scoped to the event stage, not the entire brand.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage snapshot**: analysis is based on the existing `atlassian` homepage phase1 artifacts and one desktop hero screenshot. Product subpages, pricing, login, and app UI were not visited.
- **Mobile behavior not visually captured**: CSS media queries are present, but mobile screenshot verification was not performed in this pass.
- **Legacy token residue exists**: `#0052CC` appears in CSS, but phase1 frequency and DS variables show `#1868DB` as the current practical anchor. Treat old blue as residue unless a specific component proves otherwise.
- **Motion logic partially observed**: CSS transitions and reduced-motion branches were read, but JS-driven video, carousel, and scroll-trigger logic were not audited.
- **Form states not fully surfaced**: DS input/error/focus tokens exist, but a live form flow was not opened.
- **Logo/media color contamination**: chromatic colors from event graphics, Rovo colors, and SVG/media may inflate frequency. Brand-color selection prioritizes CTA/DS semantic tokens over raw chromatic frequency.
- **Exact hero typography size is screenshot-derived**: CSS contains generated atomic classes and font tokens, but the first-viewport hero size is reported from visual observation rather than a clean named token.
- **Report HTML intentionally skipped**: user requested design.md only, so Step 6 `report.ko.html` rendering was not generated or validated in this workflow.
