---
schema_version: 3.2
slug: ikea
service_name: IKEA
site_url: https://www.ikea.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: light
brand_color: "#FFDB00"
primary_font: "Noto IKEA"
font_weight_normal: 400
token_prefix: ikea

bold_direction: Democratic Editorial
aesthetic_category: editorial-product
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high

archetype: editorial-product
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "실제 CSS 변수 142개와 Astro/Svelte 컴포넌트 CSS가 존재하지만 공개 토큰 문서가 아니라 운영 UI에서 추출된 system in use."

colors:
  brand-yellow: "#FFDB00"
  brand-blue: "#0058A3"
  surface-off-white: "#FFFEFB"
  text-primary: "#111111"
  text-black: "#000000"
  border-soft: "#F0EDE8"
  grey: "#DFDFDF"
  yellow-hover: "#FFE53A"
typography:
  display: "Noto IKEA"
  body: "Noto IKEA"
  ladder:
    - { token: hero-title, size: "clamp(2rem, observed 3rem+, 4rem)", weight: 700, tracking: "normal to -0.06rem" }
    - { token: section-title, size: "2.25rem", weight: 700, tracking: "-0.06rem" }
    - { token: mobile-title, size: "1.25rem", weight: 700, tracking: "normal" }
    - { token: body, size: "1rem", weight: 400, tracking: "normal" }
  weights_used: [300, 400, 700, 800]
  weights_absent: [500, 600]
components:
  yellow-shopping-panel: { bg: "{colors.brand-yellow}", radius: ".5rem", layout: "tall panel + bottom store bar" }
  black-primary-button: { bg: "{colors.text-primary}", hover: "#333333", active: "#000000", radius: "pill focus ring" }
  white-secondary-button: { bg: "#FFFFFF", hover: "#F5F5F5", active: "#DFDFDF", radius: "pill focus ring" }
  media-tile: { radius: ".5rem", overflow: "hidden", image: "full-bleed product photography/video" }
---

# DESIGN.md — IKEA (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

IKEA Global does not behave like a conventional ecommerce homepage. It opens like a flat-pack catalog spread that has been unfolded into a room: a fixed white navigation bar, a large moving product story, and one blunt yellow action slab. The page lets product photography carry the domestic weather, then brings in #FFDB00 (`{colors.brand-yellow}`) only when the user needs a commercial command big enough to read from across the aisle.

The strongest visual decision is asymmetry. This is not a centered headline with two polite buttons; it is a showroom bay on the left and a warehouse sign on the right. The media tile behaves like a furnished room seen through a clean catalog cutout, while the yellow panel says "Go shopping" with the confidence of in-store wayfinding. No second brand color competes for that job: `{colors.brand-blue}` supports the system, but `{colors.brand-yellow}` owns the moment of action.

The neutral system is warmer than a generic white UI. The page base is #FFFEFB (`{colors.surface-off-white}`), bordered with #F0EDE8 (`{colors.border-soft}`), and text drops to #111111 (`{colors.text-primary}`). It is the color of paper under product photography, not the cold white of a checkout app; wood, textile, and kitchen light need a slightly domestic floor. In that sense, the chrome tries to become the catalog paper, leaving the furniture to supply texture.

Typography is direct and heavy, closer to shelf labels and assembly-guide headings than luxury editorial type. `Noto IKEA` carries both body and display, with weight 700 doing much of the brand work. The system deliberately avoids the 500/600 middle; navigation jumps from regular to bold like a physical sign becoming active, while headlines stay practical instead of delicate.

Micro-interaction is functional rather than ornamental. Navigation hides on scroll with a sharp `.15s cubic-bezier(1,.26,.51,.72)` transition, focus states use a black/white/black inset stack, and media/video controls stay simple. Shadow mostly belongs to dialogs and focus mechanics, not the main product chrome; the catalog does not float, it lies flat, and the room inside the photograph creates the depth.

### Key Characteristics

- Warm off-white page surface: #FFFEFB, not cold white.
- IKEA yellow is a command surface, not a decorative wash.
- IKEA blue appears as brand/system support, not the dominant homepage background.
- Editorial product media uses .5rem clipped corners and full-bleed imagery.
- Fixed navigation is tall on desktop: 6rem, shrinking to 4.25rem on mobile.
- Grid vocabulary is simple: 90rem max-width, 1.5rem desktop gutters, 1rem mobile gutters.
- Link hover state changes weight to 700 instead of adding underline decoration.
- Focus treatment is explicit: #111111 / #FFFFFF / #111111 inset ring stack.
- Headlines are bold and compact, but body text keeps normal tracking.
- Mobile collapses grids aggressively into one-column editorial flow.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Democratic Editorial
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **large product media beside a blunt IKEA-yellow shopping slab**으로 기억된다.
> **Code Complexity**: medium — Astro/Svelte component CSS, responsive grids, fixed nav behavior, and accessible focus rings; no heavy canvas/parallax system observed.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 IKEA처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Noto IKEA", "Noto Sans", "Roboto", "Open Sans", system-ui, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFEFB; --fg: #111111; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #FFDB00; --brand-blue: #0058A3; }
```

**절대 하지 말아야 할 것 하나**: IKEA yellow를 작은 accent chip처럼 흩뿌리지 말 것. #FFDB00은 큰 행동 면, 쇼핑 진입점, 브랜드 기억 장치로 써야 한다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.ikea.com` |
| Fetched | 2026-04-14 phase1 asset reused; design.md generated 2026-05-03 |
| Extractor | reused local `insane-design/ikea` HTML/CSS/phase1/screenshots |
| HTML size | 742343 bytes (Astro + Svelte island markers observed) |
| CSS files | 11 files, 272990 chars summarized |
| Token prefix | `ikea` / raw CSS variables use descriptive names such as `--color-ikea-yellow` |
| Method | CSS custom property parsing + frequency candidates + screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Astro + Svelte islands (`data-astro-cid`, `svelte-*`, Vite markers observed)
- **Design system**: IKEA operational web tokens — prefix is not a strict namespace, but core variables use `--color-*`, `--container-*`, `--navigation-*`
- **CSS architecture**:
  ```css
  core       (--color-*, --container-*, --navigation-*)  raw values and semantic site constants
  component  (.header.svelte-*, .grid-container-setup, .img-container) component layout rules
  state      (:hover, :active, .focus-visible)           interaction and accessibility states
  ```
- **Class naming**: Svelte scoped classes plus Astro `data-astro-cid-*` attributes
- **Default theme**: light (bg = `#FFFEFB`)
- **Font loading**: `@font-face` WOFF2 for `Noto IKEA`, `font-display: swap`
- **Canonical anchor**: global homepage hero with product/video media tile and `Go shopping` yellow panel

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Noto IKEA` (IKEA-hosted brand font)
- **Code font**: N/A (no code UI observed)
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --ikea-font-family:       "Noto IKEA", "Noto Sans", "Roboto", "Open Sans", system-ui, sans-serif;
  --ikea-font-family-code:  ui-monospace, SFMono-Regular, Menlo, monospace;
  --ikea-font-weight-normal: 400;
  --ikea-font-weight-bold:   700;
}
body {
  font-family: var(--ikea-font-family);
  font-weight: var(--ikea-font-weight-normal);
}
```

### Note on Font Substitutes

- **Noto IKEA** — proprietary/site-hosted family, with normal and italic cuts at 400 and 700.
  - Open-source fallback: **Noto Sans** at 400/700, then `Roboto` or `Open Sans`.
  - Preserve the weight jump. Do not replace IKEA's 700 headings with 600; the site uses direct boldness as a navigation and editorial signal.
  - Keep body letter-spacing at `normal`. Only larger hint/editorial headings show negative compensation such as `-.06rem`.
  - If `Noto Sans` looks wider in the target environment, reduce large heading letter-spacing by `-.01em` to approximate the denser `Noto IKEA` face.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `body` | `1rem` | `400` | `normal` | `normal` |
| `nav-link` | `1rem` implied | `400`, hover/active `700` | normal | normal |
| `section-heading-mobile` | `1.25rem` | `700` | `normal` | `normal` |
| `hint/editorial-heading` | `2.25rem` | `700` | `120%` | `-.06rem` |
| `hint/editorial-heading-mobile` | `1.5625rem` | `700` | `120%` | `-.03375rem` |
| `hero-title` | large display in screenshot | `700` | compact | normal to tight |

> ⚠️ Typography extraction found no generic scale map; weights are reliable, but visible heading sizes come from component CSS and screenshot interpretation.

### Principles

1. IKEA uses `400 → 700` as the meaningful jump. Intermediate weights 500 and 600 are absent from the extracted homepage CSS.
2. Navigation does not add decorative link treatment on hover; it becomes bold. That tiny layout risk is handled with hidden `:after` text preserving width.
3. Display type is not luxury-thin. The brand voice is practical, loud enough, and immediately legible.
4. Body text keeps `letter-spacing: normal`; optical tightening is reserved for larger editorial headings.
5. Font substitution must preserve the utilitarian Noto shape before chasing a fashionable SaaS typeface.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (4 steps)

| Token | Hex |
|---|---|
| `--color-ikea-yellow` | `#FFDB00` |
| `--color-ikea-yellow-hover` | `#FFE53A` |
| `--color-ikea-yellow-light` | `#FFF094` |
| `--color-ikea-blue` | `#0058A3` |

### 06-2. Brand Dark Variant

> N/A — dark brand ramp was not observed in the reused homepage CSS.

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| page | `#FFFEFB` | N/A |
| surface | `#FFFFFF` | N/A |
| border | `#F0EDE8` | N/A |
| grey | `#DFDFDF` | `#999999` |
| text-muted | `rgba(0, 0, 0, .74)` | N/A |
| text-primary | `#111111` | `#000000` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| IKEA yellow | canonical | `#FFDB00` |
| IKEA blue | canonical | `#0058A3` |
| success/green candidates | low-frequency observed | `#008D3D`, `#009521` |
| editorial teal/green candidates | low-frequency observed | `#0E748A`, `#62AD47` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--background-color` | `#FFFEFB` | page background |
| `--color-background` | `#FFFEFB` | component background alias |
| `--color-border` | `#F0EDE8` | soft dividers and structural borders |
| `--color-text-darker` | `#111111` | primary text and black buttons |
| `--color-light` | `#FFFFFF` | light surfaces and inverse text |
| `--confirm-onetrust` | `#0058A3` | consent/action support |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--background-color` | `#FFFEFB` | body/page floor |
| `--color-off-white` | `#FFFEFB` | warm surface primitive |
| `--color-ikea-yellow` | `#FFDB00` | brand action plane |
| `--color-ikea-blue` | `#0058A3` | brand/logo/action support |
| `--color-text-darker` | `#111111` | text, primary button background, focus ring |
| `--dotnet-border-color` | `#CCCCCC` | legacy/consent border |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---|---|
| text/focus | `#111111` | 30 |
| black active | `#000000` | 20 |
| white surface | `#FFFFFF` | 13 |
| white overlay | `#FFFFFF80` | 12 |
| primary hover | `#333333` | 11 |
| off-white | `#FFFEFB` | 9 |
| grey | `#DFDFDF` | 7 |
| secondary hover | `#F5F5F5` | 7 |

### 06-8. Color Stories

**`{colors.brand-yellow}` (`#FFDB00`)** — The loud democratic action surface. It is not sprinkled as decoration; in the captured hero it owns an entire right-side panel and makes "Go shopping" impossible to miss.

**`{colors.surface-off-white}` (`#FFFEFB`)** — The warm global floor. It keeps the shell softer than pure white so product photography, wood tones, textile colors, and domestic scenes do not feel pasted onto a sterile SaaS canvas.

**`{colors.text-primary}` (`#111111`)** — IKEA's readable black. It appears in body text, focus rings, button backgrounds, and navigation, giving the page a retail-signage clarity.

**`{colors.brand-blue}` (`#0058A3`)** — Brand support, not page wash. It appears in logo/action contexts and should stay subordinate to yellow and neutral surfaces on the homepage.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--container-max-width` | `90rem` | global content and nav max width |
| `--container-spacing-desktop` | `1.5rem` | desktop side padding |
| `--container-spacing-tablet` | `1rem` | tablet side padding |
| `--container-spacing-mobile` | `1rem` | mobile side padding |
| `--vertical-spacing-desktop` | `10.5rem` | major section rhythm |
| `--vertical-spacing-tablet` | `5rem` | medium viewport section rhythm |
| `--vertical-spacing-mobile` | `4rem` | mobile section rhythm |
| `--grid-gap` | `1.5rem` / `1.25rem` | editorial grid gap variants |
| `--grid-gap-mobile` | `1rem` | collapsed mobile grid gap |

**주요 alias**:
- `--navigation-spacing-desktop` → `1.5rem` (nav horizontal padding)
- `--navigation-spacing-mobile` → `1rem` (mobile nav horizontal padding)

### Whitespace Philosophy

IKEA's whitespace is practical rather than precious. The shell gives the hero enough air to make the product scene feel editorial, but it does not leave luxury-grade empty space around every object. The 90rem container and 1.5rem gutters make the page feel like a catalog spread that still needs to sell things.

The important contrast is "open story, dense utility." Top-level stories get large media tiles and 10.5rem desktop vertical rhythm, while shopping controls, nav links, store picker, and carousel/card systems compress into direct touchable units. The system breathes when it is telling a story and tightens when it is helping the user act.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--radius` | `.5rem` | media tiles, image containers, hero panels |
| `--box-border-radius` | `.5rem` | OneTrust/box surfaces |
| `--content-border-radius` | `.125rem` | small content/legacy surfaces |
| focus round | `50%` | circular icon button focus ring |
| button focus | `1.75rem` | pill button focus ring |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| consent/elevation | `0 .25rem .9375rem #0000001A` | OneTrust floating dialog |
| focus ring | `inset 0 0 0 .0625rem #111, inset 0 0 0 .1875rem #fff, inset 0 0 0 .25rem #111` | accessibility focus |
| product/media | mostly none observed | photography/video itself carries depth |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| nav hide | `.15s cubic-bezier(1,.26,.51,.72)` | fixed header translateY hide/show |
| opacity control | `.4s cubic-bezier(1,.26,.51,.72)` | button/menu opacity transitions |
| focus ring | `.2s ease-out` | focus-visible box-shadow transition |
| reduced motion | media query present | motion accommodation exists in CSS |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `90rem`
- **Grid type**: CSS Grid for editorial rows, Flexbox for header/nav alignment
- **Column count**: `repeat(3, 1fr)`, `repeat(9, 1fr)`, and two-column hero/editorial combinations observed
- **Gutter**: `1.5rem` desktop, `1rem` mobile

### Hero

- **Pattern Summary**: `large media tile + right yellow shopping slab + fixed white nav`
- Layout: two-column editorial/action split in the captured desktop screenshot
- Background: page-level `#FFFEFB`; hero media tile uses product photography/video; right action tile uses `#FFDB00`
- **Background Treatment**: solid off-white shell + clipped media/video tile + solid brand-yellow panel
- H1: screenshot hero title uses large bold white text over media; CSS heading references include `2.25rem / 700 / -.06rem`
- Max-width: `90rem` global container behavior

### Section Rhythm

```css
section {
  padding: 10.5rem 1.5rem; /* desktop major rhythm */
  max-width: 90rem;
}
@media (max-width: 47.9375rem) {
  section {
    padding: 4rem 1rem;
  }
}
```

### Card Patterns

- **Card background**: `#FFFFFF` or media/photo fill; yellow action panels use `#FFDB00`
- **Card border**: usually none on media tiles; soft borders use `#F0EDE8`
- **Card radius**: `.5rem`
- **Card padding**: content panels around `1rem` to `1.5rem`
- **Card shadow**: no generic card shadow; use clipped media and color planes

### Navigation Structure

- **Type**: horizontal desktop nav; mobile hides desktop links at `64rem`
- **Position**: fixed top header
- **Height**: `6rem` desktop, `4.25rem` mobile
- **Background**: `var(--menu-background-color, var(--color-off-white))`
- **Border**: no strong bottom border observed; relies on surface continuity and spacing

### Content Width

- **Prose max-width**: `49.625rem` in `top-content`, `75.6875rem` wide variant
- **Container max-width**: `90rem`
- **Sidebar width**: N/A on homepage; mobile menu width `25.625rem`

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Small mobile | `23.4375rem`, `28.125rem`, `33.125rem` | narrow-device and consent/layout adjustments |
| Mobile | `47.9375rem` | grids collapse, navigation height becomes `4.25rem`, heading sizes reduce |
| Tablet | `64rem` | desktop nav links hidden, spacing shifts to tablet values |
| Desktop | `64.0625rem` | desktop interaction/pointer rules begin |
| Large | `90rem` | full container rhythm and max-width behavior |

### Touch Targets

- **Minimum tap size**: explicit button/icon affordances; exact universal min not extracted
- **Button height (mobile)**: inferred from nav/header `4.25rem` and icon button patterns
- **Input height (mobile)**: not observed in homepage CSS sample

### Collapsing Strategy

- **Navigation**: desktop links hide at `max-width: 64rem`; menu button/mobile menu takes over
- **Grid columns**: `.col-2`, `.col-3`, `.col-9` collapse to `grid-template-columns: 100%` at `47.9375rem`
- **Sidebar**: no persistent homepage sidebar; mobile menu uses `25.625rem` panel width
- **Hero layout**: editorial/media grid collapses into stacked mobile sections; special row-9 retains custom mobile template

### Image Behavior

- **Strategy**: clipped containers with `overflow: hidden`; product/media uses `object-fit`
- **Max-width**: image containers are width `100%` within grid tracks
- **Aspect ratio handling**: square/tile heights are controlled by component variables such as `--square-height-two-columns`; carousel images use equal width/height variable

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary black button**

| Property | Value |
|---|---|
| Background | `#111111` |
| Text | `#FFFFFF` |
| Hover | `#333333` |
| Active | `#000000` |
| Focus | three-layer inset ring `#111111 / #FFFFFF / #111111` |

```html
<button class="btn-color-primary btn-focus-visible">Continue</button>
```

**Secondary white button**

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#111111` |
| Hover | `#F5F5F5` |
| Active | `#DFDFDF` |
| Focus | same pill focus ring |

### Badges

Badges were not a primary homepage signature in the inspected CSS. If needed, borrow the focus/hairline system: `#FFFFFF` surface, `#F0EDE8` border, `#111111` text, and `.5rem` radius.

### Cards & Containers

**Media tile**

| Property | Value |
|---|---|
| Container | `.img-container` |
| Radius | `.5rem` / `var(--radius)` |
| Overflow | `hidden` |
| Image | `object-fit` driven, full tile |
| Shadow | none by default |

**Yellow shopping panel**

| Property | Value |
|---|---|
| Background | `#FFDB00` |
| Text | `#111111` |
| Radius | `.5rem` |
| Structure | large action area + bottom store bar |
| Icon | circular black arrow button in captured hero |

### Navigation

The nav is a fixed horizontal header with `6rem` desktop height. Logo sits left, links follow with 1rem padding, and link hover/active state switches to weight 700. A hidden `:after` text clone preserves layout width when the visible text becomes bold.

### Inputs & Forms

Homepage form fields were not surfaced. Consent/onetrust UI suggests `#FFFFFF` panels, `.5rem` boxes, `#0058A3` confirm action, and `#CCCCCC`/`#DDDDDD` border treatment.

### Hero Section

Hero composition is the signature component: left product/video tile with white title over media, right #FFDB00 shopping panel, and a bottom store selector row. The hero is a functional split between brand story and retail path.

### 13-2. Named Variants

**`yellow-shopping-panel`**

```css
.yellow-shopping-panel {
  background: #FFDB00;
  color: #111111;
  border-radius: .5rem;
  display: grid;
  grid-template-rows: 1fr auto;
}
```

State notes: arrow CTA remains visually black; panel should not gain gradient, shadow, or decorative border.

**`media-story-tile`**

```css
.media-story-tile {
  border-radius: .5rem;
  overflow: hidden;
  background: #DFDFDF;
}
```

State notes: keep depth inside the photo/video; chrome stays flat.

**`bold-nav-link`**

```css
.bold-nav-link:hover,
.bold-nav-link.active {
  font-weight: 700;
}
```

State notes: reserve layout width with hidden bold clone if implementing dynamic text weight.

### 13-3. Signature Micro-Specs

```yaml
bold-hover-width-reservation:
  description: "Navigation hover becomes bold without causing layout jump."
  technique: "hidden a:after clone with content: attr(data-text); visibility: hidden; font-weight: 700"
  applied_to: ["{component.Navigation}", "{component.bold-nav-link}"]
  visual_signature: "Practical hover confidence with no sideways wobble."

triple-inset-focus-ring:
  description: "Accessibility ring with IKEA black/white/black retail clarity."
  technique: "box-shadow: inset 0 0 0 .0625rem #111, inset 0 0 0 .1875rem #fff, inset 0 0 0 .25rem #111; transition: .2s ease-out"
  applied_to: ["{component.black-primary-button}", "{component.white-secondary-button}", "{component.Navigation}", "icon buttons"]
  visual_signature: "A sign-like focus halo that reads clearly without neon color."

yellow-plane-command:
  description: "Brand yellow appears as a full command surface, not an accent chip."
  technique: "solid #FFDB00 background, #111111 text, .5rem radius, grid-template-rows: 1fr auto, black circular directional CTA"
  applied_to: ["{component.yellow-shopping-panel}", "{component.Hero Section}"]
  visual_signature: "A warehouse wayfinding sign embedded directly into the hero."

clipped-domestic-media:
  description: "Product/video photography is framed as soft domestic editorial content."
  technique: "border-radius: .5rem; overflow: hidden; object-fit media fill; no default card shadow"
  applied_to: ["{component.media-tile}", "{component.media-story-tile}", "hero tile", "carousel image blocks"]
  visual_signature: "Catalog-room warmth held inside a controlled rounded grid cutout."

sharp-retail-scroll-hide:
  description: "Fixed navigation gets out of the way with a quick operational motion."
  technique: "transition: transform .15s cubic-bezier(1,.26,.51,.72); desktop height 6rem; mobile height 4.25rem"
  applied_to: ["{component.Navigation}"]
  visual_signature: "A store-header snap rather than a glossy app animation."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Direct, plain, product/story-led | "IKEA PS 2026 collection" |
| Primary CTA | Verb-first utility | "Go shopping" |
| Secondary CTA | Store/context selector | "Store: IKEA.kr (en)" |
| Subheading | Friendly peek behind the brand | "A sneak peek!" |
| Tone | Democratic, useful, unfussy, catalog-editorial | short phrases, no abstract SaaS promise |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* IKEA — copy into your root stylesheet */
:root {
  /* Fonts */
  --ikea-font-family:       "Noto IKEA", "Noto Sans", "Roboto", "Open Sans", system-ui, sans-serif;
  --ikea-font-family-code:  ui-monospace, SFMono-Regular, Menlo, monospace;
  --ikea-font-weight-normal: 400;
  --ikea-font-weight-bold:   700;

  /* Brand */
  --ikea-color-brand-25:  #FFF094;
  --ikea-color-brand-300: #FFE53A;
  --ikea-color-brand-500: #FFDB00;
  --ikea-color-brand-600: #FFDB00;   /* canonical */
  --ikea-color-brand-900: #0058A3;

  /* Surfaces */
  --ikea-bg-page:    #FFFEFB;
  --ikea-bg-dark:    #111111;
  --ikea-text:       #111111;
  --ikea-text-muted: rgba(0, 0, 0, .74);
  --ikea-border:     #F0EDE8;
  --ikea-grey:       #DFDFDF;

  /* Key spacing */
  --ikea-container-max: 90rem;
  --ikea-space-sm:  1rem;
  --ikea-space-md:  1.5rem;
  --ikea-space-lg:  10.5rem;

  /* Radius */
  --ikea-radius-sm: .125rem;
  --ikea-radius-md: .5rem;
  --ikea-radius-pill: 1.75rem;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — IKEA approximation
module.exports = {
  theme: {
    extend: {
      colors: {
        ikea: {
          yellow: '#FFDB00',
          yellowHover: '#FFE53A',
          yellowLight: '#FFF094',
          blue: '#0058A3',
        },
        neutral: {
          page: '#FFFEFB',
          border: '#F0EDE8',
          grey: '#DFDFDF',
          ink: '#111111',
        },
      },
      fontFamily: {
        sans: ['Noto IKEA', 'Noto Sans', 'Roboto', 'Open Sans', 'system-ui', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        bold: '700',
      },
      borderRadius: {
        ikea: '.5rem',
      },
      maxWidth: {
        ikea: '90rem',
      },
      spacing: {
        'ikea-gutter': '1.5rem',
        'ikea-section': '10.5rem',
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
| Brand primary | `{colors.brand-yellow}` | `#FFDB00` |
| Brand support | `{colors.brand-blue}` | `#0058A3` |
| Background | `{colors.surface-off-white}` | `#FFFEFB` |
| Text primary | `{colors.text-primary}` | `#111111` |
| Text muted | `text-muted` | `rgba(0, 0, 0, .74)` |
| Border | `{colors.border-soft}` | `#F0EDE8` |
| Grey | `{colors.grey}` | `#DFDFDF` |

### Example Component Prompts

#### Hero Section
```
IKEA Global 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFEFB
- 레이아웃: 90rem max-width 안에서 왼쪽 큰 제품/영상 타일, 오른쪽 #FFDB00 쇼핑 패널
- H1: Noto IKEA, bold 700, white on media, compact line-height
- CTA 패널: #FFDB00 배경, #111111 텍스트, 검은 원형 arrow button
- 타일 radius: .5rem, overflow hidden
- 장식 그라디언트나 카드 그림자는 넣지 말 것
```

#### Card Component
```
IKEA 스타일 media tile을 만들어줘.
- 배경: 사진/영상 자체가 주인공
- border: 없음 또는 #F0EDE8 1px만
- radius: .5rem
- overflow: hidden
- shadow: 없음
- 제목: Noto IKEA, 700, #111111 또는 이미지 위에서는 #FFFFFF
- hover: 과한 lift 대신 명확한 focus ring 또는 텍스트 weight 변화
```

#### Badge
```
IKEA 스타일 배지를 만들어줘.
- font: Noto IKEA, 14px, weight 700
- bg: #FFFFFF
- color: #111111
- border: 1px solid #F0EDE8
- radius: .5rem
- 브랜드 배지는 #FFDB00 전체 면으로만 사용하고 작은 노란 pill 남발 금지
```

#### Navigation
```
IKEA 스타일 상단 네비게이션을 만들어줘.
- 높이: desktop 6rem, mobile 4.25rem
- 배경: #FFFEFB
- max-width: 90rem, side padding 1.5rem desktop / 1rem mobile
- 링크: Noto IKEA 400 #111111, hover/active는 700
- focus: #111111 / #FFFFFF / #111111 세 겹 inset ring
```

### Iteration Guide

- **색상 변경 시**: yellow는 `#FFDB00`, blue는 `#0058A3`, page는 `#FFFEFB`를 우선 사용.
- **폰트 변경 시**: `Noto IKEA`가 없으면 `Noto Sans`를 쓰되 400/700 구조를 유지.
- **여백 조정 시**: global max-width `90rem`, desktop gutter `1.5rem`, mobile gutter `1rem` 기준.
- **새 컴포넌트 추가 시**: `.5rem` radius와 flat chrome을 먼저 적용하고 shadow는 피한다.
- **반응형**: `47.9375rem`, `64rem`, `90rem` 기준을 유지.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#FFFEFB` as the warm page floor.
- Use `#FFDB00` as a large action plane for shopping or brand command moments.
- Keep product photography/video inside `.5rem` clipped tiles.
- Use `Noto IKEA` or close Noto-based fallback with 400/700 weights.
- Preserve the fixed nav rhythm: `6rem` desktop, `4.25rem` mobile.
- Make focus states explicit with a black/white/black ring.
- Collapse grids to one column on mobile rather than squeezing multi-column layouts.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#FFFEFB` 사용.
- 본문 텍스트를 `#000000` 또는 `black`으로만 두지 말 것 — 대신 기본 텍스트는 `#111111` 사용.
- IKEA yellow를 `#FACC15`, `#FFD500`, 또는 임의 노랑으로 대체하지 말 것 — canonical은 `#FFDB00`.
- IKEA blue를 `#2563EB` 같은 generic SaaS blue로 바꾸지 말 것 — 실제 blue는 `#0058A3`.
- secondary hover를 `#EEEEEE`로 뭉개지 말 것 — 관측 hover는 `#F5F5F5`, active는 `#DFDFDF`.
- 카드/미디어 radius를 `16px` 이상으로 키우지 말 것 — 기본 radius는 `.5rem`이다.
- body에 `font-weight: 500` 또는 `600`을 기본으로 쓰지 말 것 — IKEA homepage CSS는 400/700 중심이다.
- nav hover에 underline을 기본 추가하지 말 것 — 관측된 desktop nav hover/active는 `font-weight: 700`.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Brand gradient: absent. IKEA yellow is a solid plane, not a yellow-orange gradient.
- Purple/blue SaaS gradient: zero role. `#667eea` style backgrounds would erase the retail identity.
- Thin luxury typography: absent. The page uses practical 400/700 weight jumps, not elegant 300 display as a main voice.
- Persistent card shadows: absent from the main editorial chrome; media and color planes do the structural work.
- Rounded 24px app cards: absent. The core radius is `.5rem`, not bubbly mobile-app softness.
- Dense rainbow palette: absent. Low-frequency chromatic colors exist, but the homepage identity is yellow, blue, off-white, black.
- Decorative borders around product media: absent. The image tile is clipped, not framed.
- Centered SaaS hero with CTA pair: absent. The hero is a split story/action composition.
- Weight 500/600 typography: deliberately absent in extracted weights; do not invent middle-weight hierarchy.
- Generic Inter-only styling: absent. The font voice is Noto IKEA/Noto-family, not default startup Inter.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Phase1 reuse instead of live refetch** — This guide uses existing `insane-design/ikea` assets. It does not claim that the live homepage on 2026-05-03 is identical to the Apr 2026 capture.
- **Homepage-only evidence** — Analysis is based on global homepage assets and does not cover checkout, product detail pages, account flows, planner tools, or store inventory UI.
- **Typography scale incomplete** — `typography.json` produced weights/families but no complete scale map; heading sizes were inferred from component CSS and screenshot.
- **Motion logic partial** — CSS transitions and media queries were observed, but JavaScript scroll logic, carousel timing, and video playback behavior were not instrumented.
- **Color frequency contamination possible** — Some low-frequency chromatic candidates may come from imagery-adjacent UI, consent flows, or regional modules rather than core brand tokens.
- **Mobile visual not screenshot-verified in this pass** — CSS breakpoints were read, but no fresh mobile screenshot was generated because the task requested phase1 reuse and skipped HTML render.
- **Form/input states under-observed** — Homepage CSS did not expose a full form validation system; input guidance is conservative and based on shared surface/focus rules.
- **Dark mode not established** — No full dark-mode token mapping was observed; any dark surface should be treated as component-local, not a site-wide theme.
