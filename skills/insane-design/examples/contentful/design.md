---
schema_version: 3.2
slug: contentful
service_name: Contentful
site_url: https://www.contentful.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: light
brand_color: "#1770E5"
primary_font: "Avenir Next W01"
font_weight_normal: 400
token_prefix: contentful

bold_direction: Friendly SaaS
aesthetic_category: refined-saas
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "CSS modules plus consistent button, grid, type, and navigation patterns; only sparse public custom-property tokens were visible."

colors:
  primary: "#1770E5"
  ink: "#2B2D31"
  surface: "#FFFFFF"
  mist: "#EFF2F6"
  border: "#C4D1DE"
  muted: "#6D7682"
  soft-line: "#DDE5EC"
typography:
  display: "Avenir Next W01"
  body: "Avenir Next W01"
  fallback: "Arial, Helvetica, sans-serif"
  ladder:
    - { token: hero, size: "72px", weight: 600, line_height: "100%" }
    - { token: heading-xl, size: "56px", weight: 600, line_height: "63.84px" }
    - { token: heading-lg, size: "40px", weight: 600, line_height: "45.2px" }
    - { token: body, size: "16px", weight: 400, line_height: "26px" }
    - { token: label, size: "14px", weight: 600, line_height: "19px" }
  weights_used: [400, 500, 600, 700]
  weights_absent: [300, 800, 900]
components:
  button-primary: { bg: "{colors.ink}", color: "{colors.surface}", radius: "2rem", hover_bg: "{colors.primary}" }
  button-secondary-outline: { bg: "transparent", border: "1px solid {colors.ink}", color: "{colors.ink}", hover_border: "{colors.primary}" }
  nav-mega-item: { title_weight: 600, desc_color: "{colors.muted}", icon_size: "24px" }
  hero-pill: { bg: "{colors.surface}", radius: "2rem", padding: "0.8rem 1.6rem" }
---

# DESIGN.md - Contentful

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Contentful's marketing surface is a mint-tinted canvas holding Avenir copy in a strict 12-column scaffold — a content orchestration console that has chosen warmth over control-panel chrome. The page is light and conversational, but the underlying grid is exact: a 1320px max container and repeated 1.6rem / 2.4rem / 3.2rem spacing units give it the structure of a filing system dressed in frosted-glass panels.

The hero is a pale work surface, not a sterile terminal. #EFF2F6 (`{colors.mist}`) behaves like the tinted glass panel of an editorial planning room, while #2B2D31 (`{colors.ink}`) arrives as the single dark instrument: H1 ink, CTA fill, and the one object that gives the soft scene authority. The brand blue #1770E5 (`{colors.primary}`) is kept like an illuminated button on a content console: dormant until intent, then bright on hover, links, and emphasis moments. There is no full blue wash, no ambient gradient cloud; the canvas stays white and misted until interaction asks for electricity.

Typography does most of the conversion work. Avenir Next W01 gives the page rounder terminals than Inter, and the headline weight sits at 600 instead of jumping to a heavy 800/900 marketing voice. Body copy remains readable at 16px with a relaxed line-height around 26px. This is an enterprise site speaking in direct sentences — a parchment of structured clarity, not a developer tool pretending to be documentation.

The site's craft is in soft boundaries: 2rem buttons, 1.2rem and 2rem cards, rounded hero panels, and almost no chrome shadow. It feels like a content studio with rounded trays: every module has a rim, but few cast theatrical shadow. Borders and surface tint define hierarchy more than elevation. The mega menu reads like a library archive rebuilt for a DXP: product, solution, resource, developer, partner, and pricing taxonomy in compact Avenir labels. The site does not delete chaos; it files it into a friendly 12-column editorial structure. That is the Contentful move: the canvas receives everything, the console organizes it, and the parchment of the page stays calm throughout.

### Key Characteristics

- Soft enterprise SaaS: rounded surfaces, calm panels, and dense navigation under a friendly first impression.
- #2B2D31 (`{colors.ink}`) carries primary CTA and headline authority; #1770E5 (`{colors.primary}`) is mostly interaction energy.
- Avenir Next W01 is central to the brand feel; substituting generic Inter makes the page feel sharper and less Contentful.
- Desktop layout uses a 12-column grid with 82.5% width and 1320px max-width.
- Spacing repeats 1.6rem, 2.4rem, 3.2rem, 5.2rem, and 6.4rem rather than arbitrary one-off values.
- Buttons and hero pills use large radii, commonly 2rem or pill-like values.
- Navigation is a major component surface: mega-menu item density, icon rows, and product taxonomy matter.
- Shadows are sparse and secondary; surface tint, border, and radius do more visual work.
- The homepage mixes product-platform language with small friendly illustration diagrams rather than photographic drama.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Friendly SaaS
> **Aesthetic Category**: refined-saas
> **Signature Element**: 이 사이트는 **soft mint hero plus dark pill CTA**으로 기억된다.
> **Code Complexity**: high — CSS modules, responsive grids, mega-navigation, and many component variants need coordinated implementation.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Contentful처럼 만들기 - 3가지만 하면 80%

```css
/* 1. Font + weight */
body {
  font-family: "Avenir Next W01", "Avenir Next", Arial, Helvetica, sans-serif;
  font-weight: 400;
}

/* 2. Background + text */
:root {
  --bg: #FFFFFF;
  --fg: #2B2D31;
  --surface-mist: #EFF2F6;
}
body {
  background: var(--bg);
  color: var(--fg);
}

/* 3. Interaction accent */
:root {
  --brand: #1770E5;
}
.button-primary {
  background: #2B2D31;
  color: #FFFFFF;
  border-radius: 2rem;
}
.button-primary:hover {
  background: #1770E5;
}
```

**절대 하지 말아야 할 것 하나**: primary CTA를 처음부터 #1770E5 파란 버튼으로 만들지 말 것. Contentful의 homepage CTA 기본값은 #2B2D31이고, #1770E5는 hover/interaction에서 강하게 올라온다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.contentful.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | reused phase1 assets from `insane-design/contentful/` |
| HTML size | 3,351,092 bytes (`_next/static` markers present) |
| CSS files | 94 external CSS files, ~1,015,840 chars |
| Token prefix | `contentful` (analysis alias; site CSS uses CSS modules plus sparse `--tw-*` / swiper vars) |
| Method | phase1 JSON + CSS frequency + hero screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next-style static asset pipeline (`_next/static` markers present)
- **Design system**: CSS Modules component system; no broad public semantic token namespace was exposed.
- **CSS architecture**:
  ```text
  CSS modules       .button_markup_primary__SBfwO, .navigation_navBarDesktop__QOP93
  Utility grid      .main-grid, col-span classes, responsive span helpers
  Sparse vars       --font-avenir-next, --tw-ring-color, --swiper-theme-color
  Raw values        frequent #2B2D31, #FFFFFF, #1770E5, #C4D1DE, #EFF2F6
  ```
- **Class naming**: CSS Modules with component + element + hash suffix, e.g. `button_markup_primary__SBfwO`.
- **Default theme**: light, with white page chrome and pastel/tinted content panels.
- **Font loading**: Avenir Next W01 / Avenir Next declarations plus `avenirNextFont` fallback markers.
- **Canonical anchor**: homepage hero, mega navigation, primary button, and repeated 12-column grid.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Avenir Next W01` (commercial/webfont family)
- **Body font**: `Avenir Next W01`, `Avenir Next`, `Arial`, `Helvetica`, `sans-serif`
- **Code font**: `ui-monospace`, `SFMono-Regular`, `Menlo`, `Monaco`, `Consolas`, `Liberation Mono`, `Courier New`, `monospace`
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --contentful-font-family: "Avenir Next W01", "Avenir Next", Arial, Helvetica, sans-serif;
  --contentful-font-family-code: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --contentful-font-weight-normal: 400;
  --contentful-font-weight-semibold: 600;
  --contentful-font-weight-bold: 700;
}
body {
  font-family: var(--contentful-font-family);
  font-weight: var(--contentful-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Best substitute**: `Avenir Next` if the local platform has it; keep heading weight at 600 and body at 400.
- **Open-source fallback**: use `Nunito Sans` only if you need similar roundness, but tighten the display line-height from 1.10 to 1.04 so the hero does not become too soft.
- **Safer system fallback**: `Arial` / `Helvetica` preserves enterprise neutrality but loses Avenir's friendly geometry. Increase button font-weight to 600 to compensate.
- **Do not replace with Inter by default**: Inter makes the nav and H1 feel more developer-tool sharp than Contentful's current marketing surface.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| Hero H1 | 72px / 7.2rem | 600 | 100% | 0 |
| Display heading | 56px / 5.6rem | 600 | 63.84px | 0 |
| Section heading | 40px / 4rem | 600 | 45.2px | 0 |
| Card heading | 32px / 3.2rem | 600 | 36.8px | 0 |
| Body large | 20px | 400 | 29.9px | 0 |
| Body default | 16px | 400 | 26px | 0 |
| Nav / label | 14px | 600 | 19px | 0 |
| Micro label | 12px | 600 | 14px | 0 |

> Key insight: Contentful's typography is not extreme contrast. It relies on Avenir Next's rounded voice, 600-weight headings, and readable body line-height rather than aggressive display tracking.

### Principles
<!-- SOURCE: manual -->

1. Hero type is large but not black-heavy: 600 is the signature weight; 800/900 would turn the page into generic performance marketing.
2. Body text stays at 400 with generous line-height around 26px for 16px copy, which keeps long SaaS value propositions readable.
3. Labels and navigation become 600 rather than larger; hierarchy comes from weight before size.
4. Letter-spacing is effectively neutral in the observed CSS; do not add fashionable negative tracking unless matching a specific heading lockup.
5. Weight 300 is absent from the visible system. Contentful is friendly, not delicate.
6. The font choice is part of the brand. Rebuilding with default system UI changes the tone more than changing several colors.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp

| Token | Hex | Evidence |
|---|---|---|
| `contentful-blue-hover` | `#1770E5` | button hover, link and interactive accent frequency |
| `contentful-blue-alt` | `#1770E6` | SVG/pattern-adjacent blue variant |
| `contentful-blue-deep` | `#0B6AE6` | secondary blue occurrence |
| `contentful-blue-dark` | `#003CBE` | deep accent occurrence |
| `contentful-blue-soft` | `#71A0F5` | light accent occurrence |

### 06-2. Brand Dark Variant

| Token | Hex | Usage |
|---|---|---|
| `contentful-ink` | `#2B2D31` | headline text, primary CTA background, dark surface authority |
| `contentful-ink-alt` | `#2A3039` | nearby dark neutral occurrence |
| `contentful-black` | `#121212` | rare dark text/surface occurrence |

### 06-3. Neutral Ramp

| Step | Light | Dark / Text |
|---|---|---|
| 0 | `#FFFFFF` | primary page and light button surface |
| 50 | `#EFF2F6` | mist panel / pale surface |
| 100 | `#DDE5EC` | soft line / pale divider |
| 200 | `#C4D1DE` | border, disabled button background |
| 500 | `#6D7682` | muted text |
| 600 | `#55575B` | secondary text |
| 900 | `#2B2D31` | primary text and dark CTA |

### 06-4. Accent Families

| Family | Key Hex | Notes |
|---|---|---|
| Blue | `#1770E5` | true UI accent, especially interactive states |
| Green/mint | `#4A6E70` | low-frequency muted green, supports hero illustration/panel mood |
| Red/error | `#D12E2E` | rare status/accent occurrence |
| Yellow/logo | `#FFDB23` | brand/logo or decorative occurrence, not a primary UI system color |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `surface.base` | `#FFFFFF` | global background, header, light button surface |
| `surface.mist` | `#EFF2F6` | large calm content backgrounds |
| `text.primary` | `#2B2D31` | primary text, H1, CTA fill |
| `text.muted` | `#6D7682` | labels, secondary explanations |
| `border.default` | `#C4D1DE` | disabled, dividers, input/secondary boundaries |
| `action.hover` | `#1770E5` | primary hover, link emphasis, active accents |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--font-avenir-next` | `"avenirNextFont","avenirNextFont Fallback",Arial,Helvetica,sans-serif` | site font family token |
| `--tw-ring-color` | `rgb(59 130 246/0.5)` | Tailwind ring fallback residue |
| `--tw-ring-offset-color` | `#FFFFFF` | focus/ring offset |
| `--swiper-theme-color` | `#007AFF` | swiper library default, not Contentful brand |

### 06-7. Dominant Colors

| Hex | Frequency | Role |
|---|---:|---|
| `#2B2D31` | 207 normalized occurrences | ink, primary CTA, text |
| `#FFFFFF` | 151 normalized occurrences | base surface |
| `#1770E5` | 125 normalized occurrences | interaction accent |
| `#C4D1DE` | 72 normalized occurrences | border / disabled |
| `#EFF2F6` | 58 normalized occurrences | mist surface |
| `#6D7682` | 39 normalized occurrences | muted text |
| `#55575B` | 31 normalized occurrences | secondary text |
| `#DDE5EC` | 19 normalized occurrences | soft line / pale surface |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.ink}` (#2B2D31)** — This is the real authority color. It appears as headline ink and primary CTA fill, giving the friendly page a firm enterprise backbone.

**`{colors.surface}` (#FFFFFF)** — White is the chrome floor: header, nav, cookie banner, and light controls. It should stay clean so the pastel hero panel can read as the special first-viewport surface.

**`{colors.primary}` (#1770E5)** — Blue is interaction, not wallpaper. Use it for hover, active states, links, and selective emphasis; making every CTA blue collapses the Contentful distinction.

**`{colors.border}` (#C4D1DE)** — The system's quiet structure. It supports disabled states, input edges, soft dividers, and card boundaries without resorting to heavy shadow.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `space-2xs` | `0.4rem` | icon/detail nudges |
| `space-xs` | `0.8rem` | eyebrow gaps, compact internal spacing |
| `space-sm` | `1.6rem` | mobile gutters, component padding, row gaps |
| `space-md` | `2.4rem` | grid gaps, section internals |
| `space-lg` | `3.2rem` | desktop grid gap, CTA clusters |
| `space-xl` | `4rem` | vertical section padding |
| `space-2xl` | `5.2rem` | expanded row rhythm |
| `space-3xl` | `6.4rem` | large section rhythm |
| `space-hero` | `7.2rem` / `8.4rem` | high-air marketing bands |
| `space-mega` | `12.8rem` | rare large vertical separation |

**Major aliases**:
- `main-grid gap` -> `3.2rem` on desktop
- `mobile grid column-gap` -> `1.6rem`
- `section vertical` -> usually `6.4rem 0`, with `7.2rem 0` for bigger story bands

### Whitespace Philosophy
<!-- SOURCE: manual -->

Contentful uses generous vertical air around marketing claims but keeps component internals compact enough to preserve product density. The homepage hero has a large rounded field, but the nav above it is precise and economical. That contrast matters: open top, structured taxonomy below.

The spacing system is rem-based and repetitive. If a rebuild starts using 13px, 27px, or ad hoc values, it immediately stops feeling like this site. The correct rhythm is 1.6 / 2.4 / 3.2 for components and 5.2 / 6.4 / 7.2 for section movement.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `radius-sm` | `0.4rem` / `0.6rem` | small fields, compact UI |
| `radius-md` | `1.2rem` | cards and small panels |
| `radius-lg` | `1.6rem` | larger content blocks |
| `radius-xl` | `2rem` | buttons, hero pills, major cards |
| `radius-2xl` | `2.4rem` | large featured modules |
| `radius-pill` | `10rem` / `100px` / `1000px` | capsule CTAs and icon pills |
| `radius-circle` | `50%` | round icons |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none | `none` | default chrome and most cards |
| subtle | `0 2px 4px 0 rgba(0,0,0,.05)` | light elevation when needed |
| card | `0 5px 10px 0 rgba(0,0,0,.15)` | raised content cards |
| overlay | `0 4px 24px rgba(0,0,0,.16)` | floating menus / overlays |
| dark glow | `0 0 20px 0 rgba(0,0,0,.25)` | special dark/overlay context |

Pattern: Contentful does not build its main identity from elevation. Use shadow sparingly and let radius + tint + border do the daily structural work.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| hover-color | color/background transition | button and link feedback |
| accordion-height | `rah-static` / height-zero classes | mobile nav and accordion panels |
| carousel/swiper | swiper library markers | logo or content carousel behavior |
| reduced-motion | `prefers-reduced-motion: reduce` present | accessibility fallback |

Motion is present but not brand-dominant. Recreate it as quick color and panel transitions; avoid large parallax or scroll theatricality unless a specific Contentful campaign page proves it.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `1320px`
- **Container width**: `82.5%` on large desktop, with `calc(100vw - 4rem)` and `calc(100vw - 6.4rem)` on smaller ranges
- **Grid type**: CSS Grid
- **Column count**: 4 columns mobile, 12 columns desktop
- **Gutter**: `1.6rem` mobile, `2.4rem` intermediate, `3.2rem` desktop
- **Container behavior**: several component grids set `container-type: inline-size`

### Hero

- **Pattern Summary**: rounded pastel panel + left large H1 + right simplified product/analytics diagram + dark CTA.
- **Layout**: desktop two-zone composition; text occupies left side, illustration/diagram occupies right.
- **Background**: pale mint / mist panel inside a white page chrome.
- **Background Treatment**: solid/tinted surface, no loud gradient mesh; rounded container edge is the atmospheric device.
- **H1**: `72px` observed in CSS scale / weight `600` / tracking `0`.
- **Max-width**: aligns to the 1320px grid family with inset rounded panel.

### Section Rhythm

```css
section {
  padding: 6.4rem 0;
  max-width: 1320px;
}
.main-grid {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: 3.2rem;
}
```

### Card Patterns

- **Card background**: usually `#FFFFFF` or pale `#EFF2F6`.
- **Card border**: soft neutral lines using #C4D1DE / #DDE5EC range.
- **Card radius**: commonly `1.2rem`, `2rem`, or larger featured values.
- **Card padding**: `1.6rem`, `2.4rem`, or `3.2rem`.
- **Card shadow**: none by default; raised variants use `0 5px 10px 0 rgba(0,0,0,.15)`.

### Navigation Structure

- **Type**: desktop horizontal nav with mega-menu taxonomy; mobile nav switches to accordion/panel behavior.
- **Position**: top page chrome, white background.
- **Height**: around 80px for mobile nav marker; desktop header visually sits around a compact 74-80px band.
- **Background**: `#FFFFFF`.
- **Border**: soft or absent; hierarchy mostly from spacing and text weight.
- **Content**: product, solution, resource, developer, partner, pricing sections with icon-rich panels.

### Content Width

- **Prose max-width**: approximately 560-680px for hero/body text clusters.
- **Container max-width**: `1320px`.
- **Sidebar width**: not a homepage pattern; mega menu panels behave as wide dropdown surfaces rather than fixed sidebars.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `< 768px` | 4-column grid, mobile nav, tighter gutters |
| Tablet | `min-width: 768px` | major breakpoint; many CSS rules start here |
| Desktop | `min-width: 1024px` | 12-column desktop grid and desktop nav behavior |
| Wide | `min-width: 1440px` | expanded spacing and max container behavior |

### Touch Targets

- **Minimum tap size**: target 44px+; button classes and nav controls visually satisfy this in the hero/header.
- **Button height mobile**: use 48-56px for primary CTAs.
- **Input height mobile**: not fully observed in the homepage flow; assume 48px+ based on input class presence.

### Collapsing Strategy

- **Navigation**: desktop mega nav becomes mobile nav / accordion panel.
- **Grid columns**: 12 desktop columns collapse to 4 mobile columns.
- **Sidebar**: no persistent sidebar in homepage; panels collapse into stacked sections.
- **Hero layout**: two-zone desktop hero stacks or simplifies; illustration should not squeeze text below readable width.

### Image Behavior

- **Strategy**: responsive assets and SVG/product diagrams; object-fit use was not fully audited.
- **Max-width**: preserve `max-width: 100%` behavior for illustrations.
- **Aspect ratio handling**: hero diagram should keep its horizontal relationship to the H1 on desktop and become secondary on mobile.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

Primary button:

```html
<a class="button_markup_root__sACGr button_markup_primary__SBfwO">
  Explore Contentful Platform
</a>
```

| Property | Value |
|---|---|
| Default bg | `#2B2D31` |
| Default text | `#FFFFFF` |
| Hover bg | `#1770E5` |
| Radius | `2rem` / pill family |
| Weight | 600 |
| Disabled bg | `#C4D1DE` |

Secondary outline:

```html
<a class="button_markup_root__sACGr button_markup_secondary__F_qxS">
  Contact sales
</a>
```

| Property | Value |
|---|---|
| Background | transparent or `#FFFFFF` in table/header contexts |
| Border | `#2B2D31` |
| Text | `#2B2D31` |
| Hover border/text | `#1770E5` |
| Radius | pill / `2rem` family |

States observed: hover, disabled, icon wrapper, small button, icon button. Loading/error states were not surfaced in the homepage capture.

### Badges

Badges are compact semantic labels such as `New`, `Beta`, and eyebrow pills like `Explore Contentful`.

| Property | Value |
|---|---|
| Font | Avenir Next W01 |
| Size | 12-14px |
| Weight | 600 |
| Radius | pill / circular when icon-led |
| Background | `#FFFFFF` or soft neutral/tinted surfaces |
| Text | `#2B2D31`, `#55575B`, or contextual accent |

### Cards & Containers

Contentful card surfaces prefer a rounded, bordered, lightly tinted chassis.

```html
<article class="promo_card_content__xI52l">
  <p class="promo_card_eyebrow__deVrs">Customer story</p>
  <h3 class="typography_heading04__PFAbm">Increase content production</h3>
</article>
```

| Property | Value |
|---|---|
| Background | `#FFFFFF`, `#EFF2F6`, or section-specific pale tint |
| Border | `1px solid #C4D1DE` / #DDE5EC family when used |
| Radius | `1.2rem` to `2rem` |
| Padding | `1.6rem` to `3.2rem` |
| Hover | color shift to `#1770E5` on article heading/eyebrow in observed rules |

### Navigation

Mega-navigation is a first-class component, not simple links.

```html
<nav class="navigation_navBarDesktop__QOP93">
  <div class="nav_item_container__EiPAy">
    <span class="nav_item_title__pkA_C">Products</span>
    <span class="nav_item_description__lxy1t">Deliver intelligent experiences</span>
  </div>
</nav>
```

| Property | Value |
|---|---|
| Desktop display | flex, centered |
| Mobile display | separate mobile navbar and accordion items |
| Link size | 14px range |
| Title weight | 600 |
| Description color | `#6D7682` / `#55575B` |
| Icon size | 12px / 24px icon classes recur |

### Inputs & Forms

Input CSS was present but not a primary homepage surface.

| Property | Value |
|---|---|
| Label muted | `#6D7682` |
| Dark input label | `#C4D1DE` |
| Focus/ring residue | `--tw-ring-color: rgb(59 130 246/0.5)` |
| Radius | likely `0.6rem` to `1.2rem` family |
| Error state | not observed in homepage |

### Hero Section

```html
<section class="hero">
  <div class="hero-pill">Explore Contentful</div>
  <h1>Sorry, content chaos - your time's up</h1>
  <p>Contentful DXP uses AI-driven analytics...</p>
  <a class="button_markup_primary__SBfwO">Explore Contentful Platform</a>
</section>
```

| Property | Value |
|---|---|
| Panel background | pale mint/mist surface |
| Panel radius | large rounded rectangle, visually around 24-32px |
| H1 color | `#2B2D31` |
| Body color | `#2B2D31` with softer perceived density |
| CTA | dark pill, hover blue |
| Illustration | right-side simplified cards, A/B blocks, metric callout |

### 13-2. Named Variants
<!-- SOURCE: manual -->

#### `button-primary-dark-pill`

- Background: `#2B2D31`
- Text: `#FFFFFF`
- Hover: `#1770E5`
- Radius: `2rem`
- Applied to: main hero CTA and primary action moments.

#### `button-secondary-outline-pill`

- Background: transparent or contextual white.
- Border/text: `#2B2D31`
- Hover: `#1770E5`
- Applied to: sales/contact and secondary navigation actions.

#### `hero-eyebrow-pill`

- Background: `#FFFFFF`
- Text: `#2B2D31`
- Radius: `2rem`
- Structure: circular icon chip plus label plus arrow.

#### `nav-mega-item`

- Title: 14-16px, 600, ink.
- Description: muted text.
- Icon: small colorful or line icon.
- Behavior: grouped in product/solution/resource panels rather than standalone list items.

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
dark-pill-to-blue-hover:
  description: "Primary actions keep enterprise weight at rest, then reveal brand energy only on intent."
  technique: "background-color: #2B2D31 /* {colors.ink} */; color: #FFFFFF; border-radius: 2rem/1000px; hover background-color: #1770E5 /* {colors.primary} */"
  applied_to: ["{components.button-primary}", "{components.button-primary-dark-pill}", "hero CTA"]
  visual_signature: "A dark capsule button that turns Contentful blue only when the user acts."

mist-panel-operating-field:
  description: "The hero uses a pale workbench surface instead of a blue SaaS gradient."
  technique: "large rounded rectangle, background #EFF2F6 /* {colors.mist} */, white #FFFFFF /* {colors.surface} */ page chrome, radius visually around 24-32px"
  applied_to: ["{components.hero-section}", "homepage hero", "major feature bands"]
  visual_signature: "Content chaos appears placed on a calm frosted planning table."

rounded-taxonomy-mega-nav:
  description: "Large navigation complexity is made approachable through compact labels, muted helper copy, and small icon rows."
  technique: "Avenir Next W01; title weight 600; description color #6D7682/#55575B; icon scales 12px/24px; desktop flex nav with mobile accordion fallback"
  applied_to: ["{components.nav-mega-item}", "desktop mega navigation", "mobile nav accordion"]
  visual_signature: "A DXP product library that feels shelved and readable rather than dashboard-dense."

twelve-column-soft-enterprise-grid:
  description: "Friendly SaaS surfaces are locked to a strict enterprise scaffold."
  technique: "display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 3.2rem; width: 82.5%; max-width: 1320px"
  applied_to: ["{components.hero-section}", "main-grid", "section groups", "navigation panels"]
  visual_signature: "Soft rounded modules line up with the precision of an enterprise content archive."

surface-border-before-shadow:
  description: "Hierarchy comes from tint, border, and radius before elevation."
  technique: "background #FFFFFF/#EFF2F6; border 1px solid #C4D1DE/#DDE5EC; radius 1.2rem-2rem; shadow none by default, overlay shadow 0 4px 24px rgba(0,0,0,.16) only when floating"
  applied_to: ["{components.cards-containers}", "promo cards", "mega menu overlays", "feature panels"]
  visual_signature: "Cards feel rimmed and organized, not stacked into a generic shadow wall."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | conversational problem framing, direct payoff | "Sorry, content chaos - your time's up" |
| Primary CTA | product exploration, not vague signup | "Explore Contentful Platform" |
| Secondary CTA | sales-assisted enterprise path | "Contact sales" |
| Nav taxonomy | product nouns plus benefit subtitles | "Personalization - Easily create highly personalized experiences" |
| Tone | marketer-friendly, AI-aware, enterprise-scale | "create standout digital experiences at scale" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Contentful-inspired core tokens */
:root {
  /* Fonts */
  --contentful-font-family: "Avenir Next W01", "Avenir Next", Arial, Helvetica, sans-serif;
  --contentful-font-family-code: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --contentful-font-weight-normal: 400;
  --contentful-font-weight-semibold: 600;
  --contentful-font-weight-bold: 700;

  /* Color */
  --contentful-blue: #1770E5;
  --contentful-ink: #2B2D31;
  --contentful-surface: #FFFFFF;
  --contentful-mist: #EFF2F6;
  --contentful-border: #C4D1DE;
  --contentful-muted: #6D7682;
  --contentful-soft-line: #DDE5EC;

  /* Spacing */
  --contentful-space-xs: 0.8rem;
  --contentful-space-sm: 1.6rem;
  --contentful-space-md: 2.4rem;
  --contentful-space-lg: 3.2rem;
  --contentful-space-xl: 6.4rem;

  /* Radius */
  --contentful-radius-sm: 0.6rem;
  --contentful-radius-md: 1.2rem;
  --contentful-radius-lg: 2rem;
  --contentful-radius-pill: 1000px;
}

.contentful-grid {
  width: 82.5%;
  max-width: 1320px;
  margin-inline: auto;
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: var(--contentful-space-lg);
}

.contentful-hero-panel {
  background: var(--contentful-mist);
  color: var(--contentful-ink);
  border-radius: var(--contentful-radius-lg);
  padding: 6.4rem 5.2rem;
}

.contentful-button-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 48px;
  padding: 0.8rem 1.6rem;
  border-radius: var(--contentful-radius-pill);
  background: var(--contentful-ink);
  color: var(--contentful-surface);
  font-family: var(--contentful-font-family);
  font-weight: var(--contentful-font-weight-semibold);
  transition: background-color 160ms ease, color 160ms ease;
}

.contentful-button-primary:hover {
  background: var(--contentful-blue);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js - Contentful-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        contentful: {
          blue: '#1770E5',
          ink: '#2B2D31',
          surface: '#FFFFFF',
          mist: '#EFF2F6',
          border: '#C4D1DE',
          muted: '#6D7682',
          line: '#DDE5EC',
        },
      },
      fontFamily: {
        sans: ['Avenir Next W01', 'Avenir Next', 'Arial', 'Helvetica', 'sans-serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
        semibold: '600',
        bold: '700',
      },
      borderRadius: {
        contentfulSm: '0.6rem',
        contentfulMd: '1.2rem',
        contentfulLg: '2rem',
        contentfulPill: '1000px',
      },
      spacing: {
        contentfulXs: '0.8rem',
        contentfulSm: '1.6rem',
        contentfulMd: '2.4rem',
        contentfulLg: '3.2rem',
        contentfulXl: '6.4rem',
      },
      maxWidth: {
        contentful: '1320px',
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
| Brand primary | `{colors.primary}` | `#1770E5` |
| Background | `{colors.surface}` | `#FFFFFF` |
| Hero surface | `{colors.mist}` | `#EFF2F6` |
| Text primary | `{colors.ink}` | `#2B2D31` |
| Text muted | `{colors.muted}` | `#6D7682` |
| Border | `{colors.border}` | `#C4D1DE` |
| Soft line | `{colors.soft-line}` | `#DDE5EC` |

### Example Component Prompts

#### Hero Section

```text
Contentful homepage-style hero section을 만들어줘.
- 전체 페이지 배경: #FFFFFF
- hero panel: pale mist/mint surface #EFF2F6, large rounded rectangle around 2rem
- layout: desktop 12-column grid, left copy, right simple analytics/product diagram
- H1: Avenir Next W01, 72px, weight 600, line-height 100%, color #2B2D31
- body: 16px, line-height 26px, color #2B2D31
- CTA: background #2B2D31, text #FFFFFF, border-radius 1000px, hover #1770E5
- keep gradients minimal; use surface tint and rounded boundaries instead
```

#### Card Component

```text
Contentful-style card를 만들어줘.
- background: #FFFFFF or #EFF2F6
- border: 1px solid #C4D1DE or #DDE5EC
- radius: 1.2rem to 2rem
- padding: 2.4rem or 3.2rem
- title: Avenir Next W01, 600, #2B2D31
- description: #6D7682, 16px, line-height 26px
- hover: text or border shifts to #1770E5; avoid heavy transform
```

#### Badge

```text
Contentful-style badge/pill을 만들어줘.
- font: Avenir Next W01, 12-14px, weight 600
- background: #FFFFFF or soft neutral
- text: #2B2D31
- radius: 1000px
- optional icon chip: 32-40px circle, centered icon
```

#### Navigation

```text
Contentful-style mega navigation을 만들어줘.
- header background #FFFFFF, compact 74-80px visual height
- desktop nav: horizontal labels, Avenir Next W01 14px
- dropdown item: icon 24px, title weight 600 #2B2D31, description #6D7682
- CTA button at right: outline or dark pill
- mobile: accordion groups, not a tiny cramped desktop menu
```

### Iteration Guide

- **색상 변경 시**: #1770E5는 interaction accent로 남기고, 기본 CTA는 #2B2D31을 먼저 쓴다.
- **폰트 변경 시**: Avenir Next가 없으면 Helvetica보다 Nunito Sans가 더 부드럽지만, 너무 둥글어지면 enterprise tone이 약해진다.
- **여백 조정 시**: 1.6rem / 2.4rem / 3.2rem / 6.4rem 중심으로 움직인다.
- **새 컴포넌트 추가 시**: radius와 border를 먼저 적용하고 shadow는 마지막에 최소로 쓴다.
- **다크 섹션 추가 시**: #2B2D31을 base로 쓰고 #1770E5를 작은 accent로 제한한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#2B2D31` as the page's authority color for H1 text and primary CTA rest state.
- Use `#1770E5` for hover, active, link, and interaction emphasis.
- Keep large containers rounded; `2rem` is a repeated signature radius.
- Build layouts on a 12-column desktop grid with `1320px` max-width and `3.2rem` gap.
- Use Avenir Next W01 / Avenir Next with 400 body and 600 headings.
- Let pale surfaces such as `#EFF2F6` create calm section distinction.
- Prefer borders and surface tint before adding heavy shadows.

### ❌ DON'T

- 배경을 `#F8FAFC` 또는 `#F9FAFB` 같은 generic SaaS gray로 두지 말 것 — 대신 `#FFFFFF`와 `#EFF2F6` 조합 사용.
- 본문/헤드라인 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#2B2D31` 사용.
- primary CTA 기본 배경을 `#1770E5`로 두지 말 것 — 기본은 `#2B2D31`, hover/interaction에 `#1770E5` 사용.
- disabled/border 색을 `#E5E7EB`로 대체하지 말 것 — 대신 `#C4D1DE` 또는 `#DDE5EC` 사용.
- hero surface를 `#FFFFFF` 단색 카드로 만들지 말 것 — Contentful hero는 `#EFF2F6` 계열의 tinted panel로 읽힌다.
- headline에 `font-weight: 900` 사용 금지 — Contentful의 display tone은 600 중심이다.
- grid를 1200px / 24px gap으로 단순화하지 말 것 — observed desktop container is `1320px`, gap `3.2rem`.
- card마다 큰 shadow를 넣지 말 것 — shadow는 보조이며 surface/border/radius가 우선이다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- No full-page blue wash: #1770E5 is not a background theme color.
- No black-and-white brutalism: the site uses #2B2D31, #6D7682, #C4D1DE, and #EFF2F6 to soften contrast.
- No ultra-heavy display voice: weight 800/900 is absent from the visible system.
- No default Inter SaaS look: Avenir Next is a meaningful part of the identity.
- No decorative gradient-first hero: the hero mood comes from tinted surface, illustration, radius, and layout.
- No card wall with identical drop shadows: repeated cards should vary by content role, not by elevation gimmicks.
- No sharp rectangular buttons: CTAs belong to pill / 2rem radius family.
- No dense dashboard chrome on the marketing homepage: even product concepts are illustrated in friendly simplified diagrams.
- No arbitrary spacing ladder: 1.6rem, 2.4rem, 3.2rem, 5.2rem, 6.4rem are the rhythm.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-only interpretation** — The analysis reused `insane-design/contentful/index.html`, homepage CSS, and `hero-cropped.png`. Logged-in app UI and product console surfaces were not visited.
- **Cookie banner present in screenshot** — The screenshot includes the cookie consent banner, so lower viewport spacing and bottom chrome are contaminated by that overlay.
- **CSS Modules reduce semantic naming** — Many visual rules are in hashed component classes. The token names in this file are analysis aliases, not official Contentful token names unless explicitly shown as real CSS variables.
- **Limited public custom-property system** — Only sparse variables such as `--font-avenir-next`, `--tw-*`, and swiper defaults were visible. This supports `lv2`, not a fully documented `lv3` design-system claim.
- **Form states incomplete** — Input classes appeared, but validation, loading, and error states were not surfaced in the homepage flow.
- **Motion not deeply executed** — CSS and class markers suggest hover, accordion, and carousel behavior, but JS timing and scroll-trigger logic were not audited.
- **Logo/decorative color pollution possible** — Some chromatic hex values likely come from logos, SVGs, or diagrams. `#1770E5` was chosen because it appears in button/link interaction rules, not only by frequency.
- **Mobile visual not separately captured** — Responsive behavior is inferred from CSS media queries and class structure, not from a fresh mobile screenshot.
- **Exact hero background hex** — The visual hero panel appears pale mint; CSS frequency strongly shows `#EFF2F6`, but the rendered panel may include another nearby tint from inline/asset styles.
