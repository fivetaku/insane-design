---
schema_version: 3.2
slug: retool
service_name: Retool
site_url: https://retool.com
fetched_at: 2026-05-03T07:04:16Z
default_theme: dark
brand_color: "#E9EBDF"
primary_font: Saans
font_weight_normal: 300
token_prefix: retool

bold_direction: Warm Productivity
aesthetic_category: industrial-minimalism
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "506 CSS variables, resolved action/component token layers, and state-specific button/input/nav aliases are present in the captured production CSS."

colors:
  surface-dark: "#151515"
  surface-cream: "#E9EBDF"
  surface-cream-focused: "#F7F8F4"
  surface-muted: "#CBCCC4"
  text-primary: "#E9EBDF"
  text-muted: "#CBCCC4"
  ink-primary: "#151515"
  blue-primary: "#518DD2"
  orange-primary: "#E8765E"
  critical: "#C72844"
  success: "#11997A"
  warning: "#F1A42E"

typography:
  display: "Saans"
  body: "Saans"
  accent: "Px Grotesk"
  code: "ui-monospace"
  ladder:
    - { token: hero, size: "clamp(4.75rem, 3.51923rem + 1.92308vw, 5.25rem)", weight: 300, line_height: 0.85, tracking: "-0.031em" }
    - { token: headline-xl, size: "2.25rem", weight: 300, line_height: "2.5rem", tracking: "-0.022em" }
    - { token: title, size: "1rem", weight: 570, line_height: "1.5", tracking: "0.02em" }
    - { token: body, size: "16px", weight: 300, line_height: "1.5", tracking: "0.01em" }
    - { token: nav, size: "13px", weight: 400, line_height: "19.5px", tracking: "0.01em" }
  weights_used: [300, 380, 400, 500, 570, 600, 700]
  weights_absent: [800]

components:
  button-primary: { bg: "{colors.surface-cream}", text: "{colors.ink-primary}", radius: "9999px", hover_bg: "#FFFFFF" }
  button-secondary-outline: { bg: "transparent", text: "{colors.surface-cream}", border: "1px solid rgba(233,235,223,.4)", radius: "9999px" }
  prompt-panel: { bg: "#242424", border: "1px solid rgba(233,235,223,.1)", radius: "8px", backdrop: "none" }
  nav-glass: { bg: "#15151500", scrolled_bg: "#000000CC", height: "4rem / 5rem" }
  input-dark: { bg: "#E9EBDF00", stroke: "#E9EBDF10", focus_bg: "#F7F8F4" }
---

# DESIGN.md — Retool (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Retool's homepage is not the old orange developer-tool brand. The captured page has moved into a darker, quieter product-trust frame: a near-black control room at `#151515` (`{colors.surface-dark}`), cream typography at `#E9EBDF` (`{colors.surface-cream}`), and only restrained operational accents. It feels less like a SaaS homepage and more like the lights have come up inside an operations bay: not a terminal, not a showroom, but a room where production systems are watched calmly.

The hero is a staged internal-tool prompt surface rather than a decorative SaaS collage. A huge centered headline hangs above a dark command panel, then customer logos lock the bottom of the first viewport into grid cells. The page behaves like a backlit drafting table: the grid is visible enough to imply engineering discipline, but the object of attention is the prompt panel sitting on top of it. Retool does not make "AI" into a floating nebula; it makes AI look like a field in an internal tool.

The system's strongest signature is subtraction. Retool uses a broad token library underneath, including blue, orange, green, yellow, purple, pink, and semantic states, but the first impression suppresses that palette. There is effectively no second brand color in the hero. Orange is not allowed to retell the old brand story; blue and orange appear as small state utilities, while `#151515` (`{colors.surface-dark}`) and `#E9EBDF` (`{colors.surface-cream}`) carry the whole public face.

The cream foreground is important because it is not white. Pure white would turn the page into a developer console; Retool's `#E9EBDF` reads like warm industrial enamel on black metal, closer to labeling on equipment than glowing UI chrome. The primary CTA reverses that material logic: a cream pill with `#151515` (`{colors.ink-primary}`) text, like a physical key on the command surface.

Typography carries the premium shift. Saans is used as the primary voice, with headline weights as light as 300, body weights also around 300, and display tracking pulled tight to `-0.031em`. Px Grotesk appears as a harder accent face. The mix avoids generic Inter productivity UI and gives the site the feeling of an engineering manual that hired an editorial designer.

Motion exists, but it is mostly micro-operational: shimmer text, gradient border pulse, underline reveal, cursor labels, and icon press/release transitions. Retool's craft is in the prompt surface and grid math, not in scroll spectacle. The site does not perform a product demo on the page; it lays down the console, lights the controls, and lets the trust proof grid do the rest.

### Key Characteristics

- Dark-first marketing surface: `#151515` is the dominant stage, not a fallback dark mode.
- Warm cream foreground: `#E9EBDF` replaces pure white for text, CTA fill, logo wall, and premium contrast.
- Hero as command panel: the central object is a prompt composer, not a product screenshot carousel.
- Large light-weight display: hero text uses Saans at roughly 76-84px with weight 300 and tight tracking.
- Thin structural grid: visible horizontal/vertical dividers create an industrial frame around the first viewport.
- Pill CTA grammar: primary and secondary actions are rounded capsules, not squared enterprise buttons.
- Token-rich but visually restrained: many accent ramps exist, but the page mostly withholds them.
- State-specific component tokens: buttons, inputs, nav, and subnav expose default/hover/active aliases.
- Logo wall as proof grid: customer marks are integrated into the layout frame instead of floated as a separate trust strip.
- Motion as interface feedback: shimmer, underline, cursor, and gradient-border effects replace decorative animation.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Warm Productivity
> **Aesthetic Category**: industrial-minimalism
> **Signature Element**: 이 사이트는 **dark command-panel hero with cream operational trust**으로 기억된다.
> **Code Complexity**: high — token-rich component states, responsive grid math, shimmer/gradient-border/keyframe effects, and nav state aliases are all present.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Retool처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Saans", "Saans Fallback", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 300;
  letter-spacing: 0.01em;
}

/* 2. 배경 + 텍스트 */
:root {
  --retool-bg: #151515;
  --retool-fg: #E9EBDF;
  --retool-muted: #CBCCC4;
}
body {
  background: var(--retool-bg);
  color: var(--retool-fg);
}

/* 3. CTA grammar */
:root { --retool-cta: #E9EBDF; --retool-ink: #151515; }
.button-primary {
  background: var(--retool-cta);
  color: var(--retool-ink);
  border-radius: 9999px;
  padding: 12px 24px;
}
```

**절대 하지 말아야 할 것 하나**: Retool을 orange SaaS로 만들지 말 것. 현재 homepage의 primary impression은 `#151515` + `#E9EBDF`의 dark cream control-room이며, orange `#E8765E`는 보조 accent다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://retool.com` |
| Fetched | 2026-05-03T07:04:16Z |
| Extractor | reused phase1 artifacts from `insane-design/retool/` |
| HTML size | 391308 bytes |
| CSS files | 6 external files, total 686044 chars |
| Token prefix | `retool` (normalized report prefix; source tokens are mostly raw/surface/btn/input/nav) |
| Method | existing CSS custom-property extraction + screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js production build indicators (`next/static` references in captured HTML)
- **Design system**: Retool marketing token layer — source prefixes include `--raw-*`, `--surface-*`, `--btn-*`, `--input-*`, `--nav-*`, `--subnav-*`, and `--dvt-*`
- **CSS architecture**:
  ```css
  raw       (--raw-*)        primitive color ramps and alpha steps
  surface   (--surface-*)    page/background/text semantic surfaces
  action    (--btn-*)        button variants and state tokens
  component (--input-*, --nav-*, --subnav-*, --dvt-*) component/state/grid APIs
  ```
- **Class naming**: CSS Modules with hashed suffixes, e.g. `PromptAction-module__...`, `HeroProductSolutionPage-module__...`
- **Default theme**: dark marketing homepage (`#151515` page, `#E9EBDF` foreground)
- **Font loading**: custom font-face variables detected: `--font-saans`, `--font-px-grotesk`
- **Canonical anchor**: first viewport screenshot: nav + centered headline + prompt panel + logo proof grid

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Saans` via `--font-saans: "saansFont","saansFont Fallback"`
- **Accent font**: `Px Grotesk` via `--font-px-grotesk: "pxGroteskFont","pxGroteskFont Fallback"`
- **Code font**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace`
- **Weight normal / display / title**: `300` / `300-380` / `570`

```css
:root {
  --retool-font-family:       "saansFont", "saansFont Fallback";
  --retool-font-family-accent:"pxGroteskFont", "pxGroteskFont Fallback";
  --retool-font-family-code:  ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --retool-font-weight-body:  300;
  --retool-font-weight-title: 570;
}
body {
  font-family: var(--retool-font-family), sans-serif;
  font-weight: var(--retool-font-weight-body);
}
```

### Note on Font Substitutes

- **Saans** — if unavailable, use **Inter Tight** rather than plain Inter.
  - Open-source substitute: `Inter Tight` at weight 300 for body/display and 600 only for short emphasis.
  - Correction: display letter-spacing must stay tight: `-0.031em` for hero-scale text, not browser default.
  - Correction: body tracking should be slightly open (`0.01em`) to mimic the captured Saans spacing.
- **Px Grotesk** — if unavailable, use **Space Grotesk** sparingly for labels/accent moments.
  - Do not apply the accent face to all body copy; Retool uses it as a harder editorial flavor.
  - Keep label/title weight around 570/600, not 700+.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| hero-display | `clamp(4.75rem, 3.51923rem + 1.92308vw, 5.25rem)` | `300` | `.85` | `-0.031em` |
| headline-xl | `2.25rem` | `300` | `2.5rem` | `-0.022em` |
| headline-md | `1.875rem` | `300/380` | `2.25rem` | `-0.01em` |
| title | `1rem` | `570` | `1.5` | `.02em` |
| body | `16px` | `300` | `1.5` | `.01em` |
| nav/body-small | `13px` | `400` | `19.5px` | `.01em` |
| badge/eyebrow | `.75rem-.875rem` | `400/500` | `1rem-1.25rem` | `.025em-.05em` |

> ⚠️ The key is not "big SaaS type"; it is light Saans, warm cream color, and optical compression. A 700-weight hero immediately breaks the Retool homepage voice.

### Principles

1. Display text is light, not loud — hero weight sits around 300, with negative tracking doing the tightening.
2. Body also leans light — captured body variables include `--font-weight-body: 300`, so default 400 feels too heavy.
3. Title weight 570 is the productive middle — it is used for labels/titles without jumping to bold 700.
4. Letter-spacing is asymmetric — display compresses (`-0.031em` to `-0.01em`), body opens slightly (`0.01em`).
5. Px Grotesk is an accent layer — use it for technical/editorial moments, not as a global replacement.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (cream/ink operating pair)

| Token | Hex |
|---|---|
| `--surface-background-base` | `#151515` |
| `--surface-background-focused` | `#242424` |
| `--surface-background-muted` | `#0E0E0E` |
| `--surface-text-primary` | `#E9EBDF` |
| `--surface-text-muted` | `#CBCCC4` |
| `--raw-neutral-light-white-1` | `#F7F8F4` |
| `--raw-neutral-light-white-2-primary` | `#E9EBDF` |
| `--raw-neutral-dark-black-2-primary` | `#151515` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--nav-default-background` | `#15151500` |
| `--nav-scrolled-background` | `#000000CC` |
| `--footer-background` | `#151515` |
| `--btn-primary-default-background` | `#E9EBDF` |
| `--btn-primary-hover-background` | `#FFFFFF` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 | `#FFFFFF` | `#000000` |
| 1 | `#F7F8F4` | `#0E0E0E` |
| 2 / primary | `#E9EBDF` | `#151515` |
| 3 | `#CBCCC4` | `#242424` |
| 4 | `#B6B8AF` | `#2E2F2D` |
| 5 | `#94958E` | `#3F403D` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Blue | `--raw-blue-primary` | `#518DD2` |
| Orange | `--raw-orange-primary` | `#E8765E` |
| Green | `--raw-green-primary` | `#4D9987` |
| Purple | `--raw-purple-primary` | `#9874D2` |
| Pink | `--raw-pink-primary` | `#CC64CE` |
| Yellow | `--raw-yellow-primary` | `#ECA438` |
| Lime | `--raw-lime-primary` | `#E0D643` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--raw-semantic-critical-10` | `#F15264` | critical/error ramp |
| `--raw-semantic-critical-11` | `#C72844` | input error stroke/text |
| `--raw-semantic-success-10` | `#11997A` | success state |
| `--raw-semantic-success-11` | `#008163` | strong success state |
| `--raw-semantic-warning-10` | `#F1A42E` | warning state |
| `--raw-semantic-warning-11` | `#AA6800` | strong warning state |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--btn-primary-default-background` | `#E9EBDF` | primary CTA fill |
| `--btn-primary-hover-background` | `#FFFFFF` | primary CTA hover fill |
| `--btn-primary-default-text` | `#151515` | primary CTA text |
| `--btn-secondary-blue-default-stroke` | `#518DD2` | blue secondary outline |
| `--input-default-background` | `#E9EBDF00` | transparent dark input base |
| `--input-default-stroke` | `#E9EBDF10` | subtle input hairline |
| `--input-focused-background` | `#F7F8F4` | focused input surface |
| `--nav-scrolled-background` | `#000000CC` | darkened nav after scroll |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency |
|---|---|---|
| ink/surface dark | `#151515` | 933 |
| cream foreground | `#E9EBDF` | 908 |
| pure white utility | `#FFFFFF` | 377 |
| black utility | `#000000` | 271 |
| blue accent | `#518DD2` | 257 |
| transparent ink | `#15151500` | 246 |
| transparent cream | `#E9EBDF00` | 197 |
| muted cream | `#CBCCC4` | 135 |

### 06-8. Color Stories

**`{colors.surface-dark}` (`#151515`)** — The homepage floor. It makes Retool feel like infrastructure rather than a cheerful app builder. Use it for first-viewport backgrounds, footer, and dark panels; do not lighten it to charcoal-blue.

**`{colors.surface-cream}` (`#E9EBDF`)** — The new Retool signature. It is text, primary CTA fill, logo-wall color, and warm foreground all at once. It should replace pure white in most visible homepage chrome.

**`{colors.blue-primary}` (`#518DD2`)** — Operational accent, not primary brand paint. It appears in selected nav/subnav states and blue secondary strokes. Use it as a state marker or technical highlight, not as hero background.

**`{colors.surface-muted}` (`#CBCCC4`)** — The calm secondary foreground. It carries muted nav/footer text and logo-wall softness. It should sit above `#151515`, not above white.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--dvt-nav-height` | `4rem` / `5rem` | top navigation height by responsive state |
| `--dvt-grid-items` | `26` / `36` | responsive page grid column count |
| `--dvt-grid-col` | `calc(width / items)` | derived modular column unit |
| `--dvt-grid-outer` | `var(--dvt-grid-col)` | outer page margin |
| small gap | `16px` | compact controls and icon clusters |
| card/grid gap | `24px` / `32px` | card grids and section internals |
| section padding | `72px 40px` / `96px 40px` | larger marketing bands |
| hero band | `112px 24px 56px` / `152px 24px 96px` | top-heavy hero rhythm |

**주요 alias**:
- `--dvt-grid-inner` -> calculated inner content width from grid columns.
- `--dvt-nav-plus-banner-height` -> nav plus announcement/banner offset.
- `--dvt-nav-plus-sticky-offset-height` -> sticky elements below nav.

### Whitespace Philosophy

Retool's spacing is not card-grid SaaS spacing. The first viewport is a large dark chamber split by faint grid lines. The headline gets room to breathe above the prompt panel, but the logo wall below is compressed into proof cells. This creates a useful contrast: platform confidence above, enterprise validation below.

The underlying grid is mechanical: 26 items, then 36 items, with `--dvt-grid-col` as a derived unit. That matters. Elements should align to calculated columns and outer gutters rather than arbitrary `max-width: 1200px` centering everywhere.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| `--border-radius` | `1rem` | general rounded container token |
| small utility | `.375rem` / `4px` | labels, cursor tags, compact utilities |
| prompt panel | `8px` | central command composer |
| card radius | `16px` | icon/customer cards and larger containers |
| pill CTA | `9999px` / `100px` | primary and secondary action buttons |
| circle controls | `50%` | icon or round action buttons |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

Retool keeps the homepage chrome mostly flat. Shadows appear in interactive/cursor/card internals rather than as a global elevation system.

| Level | Value | Usage |
|---|---|---|
| cursor tag | `0 1px 2px 0 #0000001F, 0 0 0 .5px var(--cursor-default-cursor-stroke)` | small cursor/label overlay |
| soft overlay | `0 0 10px #0000001A` | floating utility surfaces |
| card hover | `0 6px 18px 2px #00000014` | subtle card depth |
| outline depth | `0 0 0 1px #0000001A` | border-like shadow |
| Tailwind utility | `0 4px 6px -1px #0000001A, 0 2px 4px -1px #0000000F` | generic utility shadow |
| focus emphasis | `0 0 0 3px #7A839614, 0 15px 45px #0000001A` | focused/active surface emphasis |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| `--dvt-ease-in` | `cubic-bezier(.12,0,.72,0)` | entrance or tightening motion |
| `--dvt-ease-in-out` | `cubic-bezier(.72,0,.12,1)` | central UI transitions |
| `--dvt-ease-in-out-back` | `cubic-bezier(.72,-.4,.36,1.4)` | expressive overshoot |
| `--dvt-ease-out` | `cubic-bezier(.12,1,.72,1)` | release motion |
| shimmer text | `linear-gradient(...); animation ... 6s linear infinite` | prompt/action text shimmer |
| gradient border pulse | background-position keyframes | highlighted prompt/action borders |
| underline reveal | `background-size .3s/.6s` | link underline animation |
| icon press/release | translated icon positions | circular arrow button state motion |
| reduced motion | `@media (prefers-reduced-motion: reduce)` | disables variable-word animation |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `--dvt-grid-inner-max: 1440px`
- **Grid type**: CSS Grid/Flex hybrid, with marketing sections aligned to derived DVT grid columns
- **Column count**: `--dvt-grid-items: 26` baseline, `36` at larger widths
- **Gutter**: `--dvt-grid-outer`, normally one derived grid column

### Hero

- **Pattern Summary**: dark full-width operational hero + centered oversized H1 + prompt panel + logo proof grid
- Layout: single-column centered hero above command composer; nav fixed visually to top frame; logo wall cells below
- Background: solid `#151515`
- **Background Treatment**: solid dark with hairline grid dividers; no mesh background in first viewport
- H1: `clamp(4.75rem, 3.51923rem + 1.92308vw, 5.25rem)` / weight `300` / tracking `-0.031em`
- Max-width: visual H1 sits around `780px`; prompt panel around `576px` wide in screenshot

### Section Rhythm

```css
section {
  padding: 72px 40px;
  max-width: 1440px;
}
@media (min-width: 1024px) {
  section { padding: 96px 40px; }
}
```

### Card Patterns

- **Card background**: dark panels such as `#242424`, or transparent surfaces with cream hairlines
- **Card border**: `1px solid` low-alpha cream/ink (`#E9EBDF10`, `#1515151F`)
- **Card radius**: `8px` for prompt surfaces, `16px` for larger cards
- **Card padding**: compact internals (`16px-24px`), larger bands (`32px-40px`)
- **Card shadow**: mostly none; occasional soft black shadow for overlays

### Navigation Structure

- **Type**: horizontal marketing nav with dropdown affordances and right-aligned auth/CTA group
- **Position**: visually fixed/sticky top chrome in first viewport
- **Height**: `4rem` / `5rem`
- **Background**: transparent dark `#15151500`, scrolled `#000000CC`
- **Border**: faint vertical and horizontal frame lines; active/selected state uses accent tokens

### Content Width

- **Prose max-width**: `740px-784px` for large text blocks
- **Container max-width**: `1440px` grid inner max
- **Sidebar width**: not a homepage primary pattern; product subflows may differ

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `<640px` | single-column grids, compact nav behavior, touch-first controls |
| Tablet | `640px` / `768px` | card grids move from 1 to 2 columns; announcement/hero offsets change |
| Desktop | `1024px` / `1200px` | card grids expand to 4 columns; section padding increases |
| Large | `1280px` / grid max `1440px` | DVT grid resolves to larger column count and constrained inner width |

### Touch Targets

- **Minimum tap size**: target should stay at least `44px`; pill CTAs visually exceed this in the screenshot.
- **Button height (mobile)**: inferred from pill CTA family, approximately `40-48px`.
- **Input height (mobile)**: prompt/input internals are not fully measured; use `44px+` minimum.

### Collapsing Strategy

- **Navigation**: desktop horizontal nav should collapse to menu/drawer below tablet widths.
- **Grid columns**: marketing card grids use `1fr`, then `1fr 1fr`, then `1fr 1fr 1fr 1fr`.
- **Sidebar**: not used in homepage hero; product/app pages may introduce sidebars.
- **Hero layout**: keep headline and prompt panel stacked; scale display type with clamp rather than viewport font-size.

### Image Behavior

- **Strategy**: screenshots/product media should sit in dark/cream frames; logo wall uses cell-based alignment.
- **Max-width**: `100%` with grid-constrained containers.
- **Aspect ratio handling**: cards use fixed width/height in some modules, e.g. `260px` icon cards; prompt surface is fixed-rhythm rather than image ratio-driven.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

Primary buttons are cream pills over dark surfaces.

```css
.retool-button-primary {
  background: #E9EBDF;
  color: #151515;
  border: 1px solid #E9EBDF;
  border-radius: 9999px;
  padding: 12px 24px;
  font-family: "Saans", sans-serif;
  font-size: 14px;
  font-weight: 400;
  transition: background-color .15s ease-in-out, color .15s ease-in-out;
}
.retool-button-primary:hover {
  background: #FFFFFF;
}
```

Secondary buttons are transparent pills with a low-alpha cream border, used for "Book a demo" style actions.

### Badges

Small badges use compact rounded rectangles and may introduce accent ramps. The first-viewport "BETA" badge uses a light blue treatment near the hero eyebrow, but it remains tiny relative to the cream/dark system.

```css
.retool-badge {
  font-size: 12px;
  line-height: 1rem;
  border-radius: 4px;
  padding: 2px 6px;
}
.retool-badge-ai-gradient {
  color: #151515;
  background: linear-gradient(93deg, #9874D2 0%, #CC64CE 25%, #9874D2 50%, #518DD2 100%);
}
```

### Cards & Containers

The hero prompt panel is the primary container pattern: dark focused surface, subtle border, medium radius, sparse controls, and a cream CTA nested inside the panel.

| Property | Value |
|---|---|
| background | `#242424` or `#151515` on page |
| border | `1px solid rgba(233,235,223,.25)` visually; token hairlines include `#E9EBDF10` |
| radius | `8px` prompt, `16px` larger cards |
| padding | `16px-24px` internal controls |
| shadow | none or very soft black overlay |

### Navigation

Navigation is part of the first-viewport frame. It uses white/cream logo, muted links, tiny dropdown chevrons, and a right utility group.

| State | Background | Text/Icon |
|---|---|---|
| default | `#15151500` | `#E9EBDF` / muted cream |
| hover | transparent/dark | `#FFFFFF` or brighter cream |
| scrolled | `#000000CC` | cream foreground |
| selected | transparent | accent marker `#518DD2` |

### Inputs & Forms

Input tokens exist and are stateful. The homepage prompt composer behaves like a large dark input rather than a classic white form.

| State | Background | Stroke | Text |
|---|---|---|---|
| default | `#E9EBDF00` | `#E9EBDF10` | `#E9EBDF` |
| hover | `#F7F8F4CC` in light contexts | `#1515153D` in light contexts | `#151515` |
| focused | `#F7F8F4` in light contexts | transparent | `#151515` |
| error | state-specific | `#C72844` | `#C72844` |

### Hero Section

```html
<section class="retool-hero">
  <nav class="retool-nav">...</nav>
  <p class="retool-eyebrow"><span>BETA</span> Explore Retool's AppGen</p>
  <h1>Build how you want.<br>Ship on a platform you<br>can trust.</h1>
  <div class="retool-prompt-panel">
    <p>Build me a manufacturing dashboard...</p>
    <button>Start building</button>
  </div>
  <div class="retool-logo-grid">...</div>
</section>
```

Key anatomy: headline centered, command panel centered below, proof logos locked into grid cells at the viewport bottom.

### 13-2. Named Variants

#### `button-primary-cream`

| Spec | Value |
|---|---|
| background | `#E9EBDF` |
| hover background | `#FFFFFF` |
| text | `#151515` |
| radius | `9999px` |
| use | "Start for free", "Start building" |

#### `button-secondary-outline-dark`

| Spec | Value |
|---|---|
| background | transparent |
| border | cream/white low-alpha stroke |
| text | `#E9EBDF` |
| radius | `9999px` |
| use | "Book a demo" |

#### `prompt-panel-dark`

| Spec | Value |
|---|---|
| background | `#242424` |
| border | subtle cream hairline |
| radius | `8px` |
| text | muted cream |
| use | hero AI prompt composer |

#### `nav-transparent-to-black`

| Spec | Value |
|---|---|
| default background | `#15151500` |
| scrolled background | `#000000CC` |
| height | `4rem` / `5rem` |
| use | global marketing navigation |

### Signature Micro-Specs
<!-- §13-3 -->

```yaml
cream-on-ink-command-hero:
  description: "Retool's homepage identity is built from a dark operating surface and warm cream foreground, not the legacy orange brand."
  technique: "#151515 stage, #E9EBDF foreground, primary pill inversion with #E9EBDF background and #151515 text, hover background #FFFFFF"
  applied_to: ["{component.button-primary}", "{component.nav-glass}", "{component.prompt-panel}"]
  visual_signature: "An industrial command surface where the CTA reads like a physical cream key on black equipment."

prompt-panel-dark-composer:
  description: "The hero's main product object is a prompt composer treated as an internal-tool control panel."
  technique: "background #242424, border 1px solid #E9EBDF10, radius 8px, sparse nested controls, muted cream text"
  applied_to: ["{component.prompt-panel}", "{component.input-dark}", "{component.button-primary}"]
  visual_signature: "AI appears as a usable field inside a tool, not as a decorative SaaS illustration."

dvt-derived-grid-frame:
  description: "Viewport structure and proof logos are locked to a calculated engineering grid."
  technique: "--dvt-grid-items: 26/36, --dvt-grid-col, --dvt-grid-outer, --dvt-grid-inner-max: 1440px"
  applied_to: ["{component.nav-glass}", "{component.logo-grid}", "{component.hero-frame}"]
  visual_signature: "A faint mechanical frame that makes the homepage feel assembled like an operations dashboard."

saans-light-tight-display:
  description: "Large headlines gain authority through optical compression and light weight instead of bold mass."
  technique: "font-family Saans, font-weight 300, line-height .85, letter-spacing -0.031em, font-size clamp(4.75rem, 3.51923rem + 1.92308vw, 5.25rem)"
  applied_to: ["{component.hero-title}", "{component.marketing-headline}"]
  visual_signature: "Huge type that feels engineered and calm, never shouty or generic Inter-bold SaaS."

prompt-shimmer-interface-feedback:
  description: "AI/action emphasis is expressed as interface feedback rather than atmospheric decoration."
  technique: "linear-gradient(90deg, ...), background-size 200%, 6s linear infinite shimmer, gradient-border pulse, prefers-reduced-motion guard"
  applied_to: ["{component.prompt-panel}", "{component.badge}", "{component.action-highlight}"]
  visual_signature: "The motion reads like a live control state on the command surface, not a background animation."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | direct platform promise, short lines, trust verb | "Build how you want. Ship on a platform you can trust." |
| Primary CTA | action-oriented, low-friction | "Start for free" |
| Secondary CTA | sales conversation, understated | "Book a demo" |
| Subheading | operational capability, database/API/LLM integration | "Connect to any database, API, or LLM." |
| Tone | calm enterprise builder language; confidence without hype | "Build, deploy, and manage internal tools..." |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Retool — copy into your root stylesheet */
:root {
  /* Fonts */
  --retool-font-family: "saansFont", "saansFont Fallback", -apple-system, BlinkMacSystemFont, sans-serif;
  --retool-font-family-accent: "pxGroteskFont", "pxGroteskFont Fallback", sans-serif;
  --retool-font-family-code: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --retool-font-weight-body: 300;
  --retool-font-weight-title: 570;

  /* Core colors */
  --retool-bg-page: #151515;
  --retool-bg-focused: #242424;
  --retool-bg-muted: #0E0E0E;
  --retool-cream: #E9EBDF;
  --retool-cream-focused: #F7F8F4;
  --retool-muted: #CBCCC4;
  --retool-ink: #151515;

  /* Accent states */
  --retool-blue: #518DD2;
  --retool-orange: #E8765E;
  --retool-critical: #C72844;
  --retool-success: #11997A;
  --retool-warning: #F1A42E;

  /* Layout */
  --retool-grid-inner-max: 1440px;
  --retool-nav-height: 4rem;
  --retool-radius-panel: 8px;
  --retool-radius-card: 16px;
  --retool-radius-pill: 9999px;
}

body {
  margin: 0;
  background: var(--retool-bg-page);
  color: var(--retool-cream);
  font-family: var(--retool-font-family);
  font-weight: var(--retool-font-weight-body);
  letter-spacing: 0.01em;
}

.retool-hero-title {
  font-size: clamp(4.75rem, 3.51923rem + 1.92308vw, 5.25rem);
  line-height: .85;
  font-weight: 300;
  letter-spacing: -0.031em;
  color: var(--retool-cream);
}

.retool-primary-button {
  background: var(--retool-cream);
  color: var(--retool-ink);
  border: 1px solid var(--retool-cream);
  border-radius: var(--retool-radius-pill);
  padding: 12px 24px;
}

.retool-primary-button:hover {
  background: #FFFFFF;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Retool-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        retool: {
          ink: '#151515',
          panel: '#242424',
          black: '#0E0E0E',
          cream: '#E9EBDF',
          creamFocused: '#F7F8F4',
          muted: '#CBCCC4',
          blue: '#518DD2',
          orange: '#E8765E',
          critical: '#C72844',
          success: '#11997A',
          warning: '#F1A42E',
        },
      },
      fontFamily: {
        sans: ['Saans', 'Inter Tight', 'system-ui', 'sans-serif'],
        accent: ['Px Grotesk', 'Space Grotesk', 'sans-serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      },
      fontWeight: {
        body: '300',
        title: '570',
      },
      borderRadius: {
        panel: '8px',
        card: '16px',
        pill: '9999px',
      },
      transitionTimingFunction: {
        retool: 'cubic-bezier(.72,0,.12,1)',
        'retool-out': 'cubic-bezier(.12,1,.72,1)',
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
| Brand primary | `{colors.surface-cream}` | `#E9EBDF` |
| Background | `{colors.surface-dark}` | `#151515` |
| Panel | `{colors.surface-focused}` | `#242424` |
| Text primary | `{colors.text-primary}` | `#E9EBDF` |
| Text muted | `{colors.text-muted}` | `#CBCCC4` |
| Border | cream hairline | `#E9EBDF10` |
| Accent | `{colors.blue-primary}` | `#518DD2` |
| Error | `{colors.critical}` | `#C72844` |

### Example Component Prompts

#### Hero Section
```
Retool 스타일 히어로 섹션을 만들어줘.
- 배경: #151515
- H1: Saans, clamp(4.75rem, 3.51923rem + 1.92308vw, 5.25rem), weight 300, tracking -0.031em, line-height .85
- 텍스트 컬러: #E9EBDF
- 히어로 중앙에 dark prompt panel 배치: background #242424, border 1px solid #E9EBDF10, radius 8px
- CTA 버튼: background #E9EBDF, text #151515, pill radius 9999px
- 하단에는 logo wall을 faint grid cell로 정렬
```

#### Card Component
```
Retool 스타일 카드 컴포넌트를 만들어줘.
- 배경: #242424 또는 #151515
- border: 1px solid #E9EBDF10
- radius: 8px for prompt panel, 16px for larger cards
- padding: 24px
- shadow: 기본 none, hover에만 아주 약한 #00000014
- 제목: Saans, weight 570 또는 300, color #E9EBDF
- 본문: 16px, weight 300, color #CBCCC4, line-height 1.5
```

#### Badge
```
Retool 스타일 배지를 만들어줘.
- font: Saans, 12px, weight 400
- padding: 2px 6px, radius 4px
- dark hero 위에서는 light blue 또는 cream 기반의 작은 label만 사용
- badge가 hero보다 시각적으로 커지면 안 됨
```

#### Navigation
```
Retool 스타일 상단 네비게이션을 만들어줘.
- 높이: 4rem desktop base, large에서 5rem 가능
- 배경: 기본 #15151500, 스크롤 후 #000000CC
- 로고와 링크: #E9EBDF / #CBCCC4
- 링크: 13px, letter-spacing .01em
- 우측 CTA: "Book a demo" outline pill + "Start for free" cream filled pill
```

### Iteration Guide

- **색상 변경 시**: orange `#E8765E`를 primary brand로 끌어올리지 말 것. homepage primary는 cream on ink다.
- **폰트 변경 시**: Inter로 대체하더라도 `Inter Tight` + weight 300 + negative tracking을 먼저 맞춘다.
- **여백 조정 시**: arbitrary centered 1200px layout보다 DVT grid logic (`26/36` columns, `1440px` inner max)을 따른다.
- **새 컴포넌트 추가 시**: default/hover/active/focus state tokens를 분리한다. Retool CSS는 state alias가 강하다.
- **모션 추가 시**: big parallax보다 shimmer/underline/icon micro-feedback을 사용한다.
- **다크 모드**: 이 분석의 default 자체가 dark homepage다. light app surfaces와 혼동하지 않는다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#151515` as the homepage stage color and let it dominate the first viewport.
- Use `#E9EBDF` as the primary visible brand foreground and CTA fill.
- Keep hero typography light: Saans, weight `300`, tight tracking around `-0.031em`.
- Build the hero around a prompt/command panel instead of a generic feature-card grid.
- Use pill CTAs with ink-on-cream inversion for primary actions.
- Preserve state-specific aliases for buttons, inputs, nav, and subnav rather than collapsing states into one style.
- Align large sections to a calculated grid rhythm, ideally echoing `26/36` grid-item logic.
- Use accent colors like `#518DD2` and `#E8765E` sparingly as operational states.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 homepage hero는 `#151515` 사용.
- 본문/hero 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — dark homepage에서는 `#E9EBDF` 사용.
- primary CTA를 `#E8765E` orange로 칠하지 말 것 — 대신 `#E9EBDF` fill + `#151515` text 사용.
- hero foreground를 순백 `#FFFFFF` 중심으로 만들지 말 것 — 대신 warm cream `#E9EBDF`를 기본값으로 둔다.
- panel border를 강한 `#FFFFFF` stroke로 두지 말 것 — 대신 low-alpha cream such as `#E9EBDF10` 사용.
- body에 `font-weight: 400`을 기본으로 고정하지 말 것 — Retool body/display 감각은 `300`이 핵심.
- hero headline에 `font-weight: 700` 사용 금지 — weight `300` + negative tracking으로 만든다.
- generic `Inter`만으로 끝내지 말 것 — Saans 대체라면 `Inter Tight` + tracking correction이 필요하다.
- section layout을 균등 3-card SaaS 블록으로 환원하지 말 것 — prompt panel + grid frame + logo proof wall 구조가 우선이다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Brand-orange dominance: absent. `#E8765E` exists, but it does not own the homepage hero.
- Pure white stage: never for the first viewport. `#FFFFFF` is a hover/utility value, not the page floor.
- Heavy hero weights: no 700/800 display hero. The recognizable voice is light and tightly tracked.
- Blue SaaS wash: no full-page blue gradient, despite `#518DD2` being a real accent token.
- Card-heavy feature hero: no "headline + three feature cards" first impression.
- Decorative gradient blobs: none in the captured hero; gradient exists in small AI/badge/action details.
- Strong chrome shadows: mostly absent. Structure comes from hairlines, dark panels, and grid cells.
- Rounded pastel dashboard look: absent. The prompt panel is darker and more industrial than friendly.
- Unstructured spacing: no arbitrary floaty hero composition; grid math and dividers anchor the layout.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage capture** — this report is based on the captured `https://retool.com` homepage artifacts in `insane-design/retool/`, not on every Retool product, docs, pricing, or app-builder subflow.
- **Screenshot scope** — visual interpretation uses the 1280x800 hero screenshot. Lower mobile visual states were inferred from CSS breakpoints, not separately viewed.
- **CSS bundle breadth** — six CSS files and 686044 characters were available, but large CSS-module bundles include many pages/components beyond the homepage; this guide prioritizes first-viewport evidence.
- **Token prefix normalization** — frontmatter uses `retool` as report prefix, while actual source tokens are mixed (`--raw-*`, `--surface-*`, `--btn-*`, `--input-*`, `--nav-*`, `--dvt-*`). Do not assume a single real `--retool-*` namespace exists in production.
- **Font licensing not verified** — Saans and Px Grotesk were detected from CSS variable names, but licensing/source files were not independently audited in this run.
- **Interaction timing partial** — CSS transitions/keyframes were observed, but JavaScript-driven scroll, prompt, or AppGen interactions were not executed.
- **Logo wall color contamination risk** — frequency counts include customer logos and utility SVG values; top-color interpretation intentionally favors surface/text/action tokens over raw frequency alone.
- **Form validation subflows** — input error tokens exist (`#C72844`), but actual validation UI flows were not visited.
- **Light app surfaces** — Retool product UI may use light operational surfaces; this guide describes the marketing homepage's dark hero identity.
- **Report HTML skipped by request** — Step 6 render/report generation was intentionally skipped; only `design.md` was produced.
