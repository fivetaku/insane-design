---
schema_version: 3.2
slug: aesop
service_name: Aesop
site_url: https://www.aesop.com/us/
fetched_at: 2026-04-23T11:45:00+09:00
default_theme: mixed
brand_color: "#CA432F"
primary_font: SuisseIntl
font_weight_normal: 400
token_prefix: aesop

bold_direction: Warm Apothecary
aesthetic_category: luxury-brand
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: luxury-brand
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "CSS 변수 토큰은 없지만 SuisseIntl/Zapf-Humanist, BEM 컴포넌트, l-section/c-button/c-navigation 계층이 일관되게 운영된다."

colors:
  surface-warm: "#FFFEF2"
  text-primary: "#333"
  text-strong: "#000"
  text-muted: "#666"
  surface-soft: "#F6F5E8"
  surface-alt: "#EBEADE"
  border-warm: "#D5D5CB"
  alert-earth: "#CA432F"
  success-olive: "#6B6B60"

typography:
  display: "Zapf-Humanist"
  body: "SuisseIntl"
  medium: "SuisseIntl-Medium"
  ladder:
    - { token: hero-title, size: "1.875rem", weight: 400, line_height: "1.2" }
    - { token: content-title, size: "1.5625rem", weight: 400, line_height: "1.2" }
    - { token: nav-link, size: ".875rem", weight: 500, line_height: "1.5" }
    - { token: product-copy, size: ".75rem", weight: 400, line_height: "normal" }
  weights_used: [300, 400, 500, 600, 700, 900]
  weights_absent: []

components:
  button-outline-hero: { bg: "transparent", color: "#FFFEF2", border: "1px solid #FFFEF2", radius: "0" }
  button-solid-dark: { bg: "#333", color: "#FFFEF2", border: "1px solid #333", radius: "0" }
  input-warm-field: { bg: "#FFFEF2", color: "#333", border: "1px solid rgba(51,51,51,.2)", radius: "0" }
---

# DESIGN.md — Aesop (Designer Guidebook)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Aesop is a masterclass in product-as-artifact apothecary museography. The browser surface becomes parchment: not a pharmacy shelf but a warm archive where specimen labels, formulation names, and cabinet-index navigation behave like annotations on preserved paper. The dominant ground is #FFFEF2 (`{colors.surface-warm}`), not white — a cream that reads like warm stock, product carton, and limestone counter simultaneously. Pure white would press the site into pharmacy-shelf territory; this tint makes the page feel like a bound catalogue from a herbalist's archive.

The store is disciplined by restraint. The centered wordmark sits high and still above the display case opening; the purchase path waits inside a thin rectangular outline; hero video supplies atmosphere while the interface stays as flat as printed signage on glass. Shadow is not a UI material here. Depth belongs to photography and motion, while the canvas returns to cream silence between every product tile. There is no second brand color doing theatrical work: #CA432F (`{colors.alert-earth}`) appears like a small earth pigment stamp on parchment — identification, not decoration.

Typography orchestrates the museum-grade split. SuisseIntl handles the utilitarian layer — navigation, tiles, buttons, price labels — while Zapf-Humanist appears at gallery scale: content-tile titles and hero editorial lines. The contrast is not size alone; it is the shift from product taxonomy to literary label, like a shelf code turning into a book spine.

The interface avoids softness. Inputs are square, buttons rectangular, product cards surface-and-type arrangements rather than raised surfaces. Rounded shapes exist only for circular controls or thumbnails, never for the core commerce chassis. Aesop's luxury is the refusal of gloss: the page evacuates until what remains is a warm parchment counter, a specimen label, a vessel, and a line inviting discovery — museum authority without museum distance.

비유로 한 단계 더 풀자면 Aesop은 약국과 부티크와 공방이 한 공간에 정렬된 큐레이션 박스다. 중앙 워드마크는 store 입구 위 동판 간판, 카테고리 nav는 museum 캐비닛의 라벨된 서랍, 사각 outline CTA는 gallery 진열대 옆에 끼워둔 작은 안내 카드, warm cream surface는 parchment 작업대의 석회암 카운터다. 제품 타일은 진열장에 정렬된 유리 vessel, 검색 입력창은 공방 카운터의 처방전 받침대처럼 단정하게 놓인다. shadow가 없는 이유는 luxury가 광택이 아니라 정렬된 큐레이션이기 때문.

### Key Characteristics

- Warm cream ground: #FFFEF2 is the site floor, used far more than pure white.
- Editorial-serif display: Zapf-Humanist gives titles a cultivated, printed quality.
- Utility sans body: SuisseIntl keeps commerce, navigation, forms, and product taxonomy precise.
- Centered heritage mark: the logo sits as a visual anchor above a dense category nav.
- Full-bleed sensory hero: video/image ambience supplies warmth while UI chrome stays sparse.
- Rectangular interaction: buttons and inputs use radius 0; luxury is not pill-shaped.
- BEM component architecture: `c-button`, `c-navigation`, `c-product-tile`, `l-section` reveal a mature component layer.
- Neutral-first color strategy: chromatic color is scarce; #CA432F appears as alert/earth accent, not broad branding.
- Product-grid density below editorial air: broad hero and section breathing room collapse into tighter commerce modules.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Warm Apothecary
> **Aesthetic Category**: luxury-brand
> **Signature Element**: 이 사이트는 **warm cream apothecary hero with square editorial commerce chrome**으로 기억된다.
> **Code Complexity**: high — BEM commerce components, responsive flyout navigation, video hero, carousels, form states, and multiple font faces are present.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Aesop처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "SuisseIntl", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}

h1,
.editorial-title {
  font-family: "Zapf-Humanist", "Times New Roman", serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root {
  --aesop-bg: #FFFEF2;
  --aesop-fg: #333;
  --aesop-muted: #666;
}
body {
  background: var(--aesop-bg);
  color: var(--aesop-fg);
}

/* 3. 버튼/입력은 사각형 */
.aesop-button,
.aesop-input {
  border-radius: 0;
  border: 1px solid currentColor;
}
```

**절대 하지 말아야 할 것 하나**: Aesop을 둥근 SaaS 카드 UI로 번역하지 말 것. `border-radius: .625rem`은 보조 썸네일/일부 모듈에만 있고, 핵심 버튼과 입력은 `border-radius: 0`이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.aesop.com/us/` |
| Fetched | 2026-04-23 11:45 KST |
| Extractor | 기존 phase1 재사용: HTML + CSS + screenshot |
| HTML size | 1,008,273 bytes |
| CSS files | 7개 CSS, 약 931,214 characters |
| Token prefix | `aesop` |
| Method | CSS frequency, BEM selector samples, HTML text/classes, hero screenshot interpretation |
| Screenshot | `insane-design/aesop/screenshots/hero-cropped.png` |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: server-rendered commerce site with large hydrated HTML payload.
- **Design system**: Aesop commerce component system; no CSS custom-property token graph detected.
- **CSS architecture**: BEM-style components plus layout/utilities.
  ```text
  l-*       layout chassis: l-section, l-row, l-column, l-footer
  c-*       component layer: c-button, c-navigation, c-product-tile, c-content-hero
  h-*       helpers: h-color-light, h-text-align-center, h-show-for-large
  m-*       modifiers: m-level-1, m-dark, m-full-width, m-caption-center
  ```
- **Class naming**: BEM + modifier classes. Examples: `c-navigation__item`, `c-product-tile__wrapper`, `c-content-hero__caption`, `l-section__row`.
- **Default theme**: mixed. Commerce floor uses #FFFEF2; hero uses warm photographic/video overlay with white text.
- **Font loading**: `@font-face` for `SuisseIntl`, `SuisseIntl-Medium`, and `Zapf-Humanist`.
- **Canonical anchor**: centered Aesop wordmark, category navigation, and square outline CTA over sensory editorial media.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Zapf-Humanist` (brand-proprietary/local asset in CSS)
- **Body font**: `SuisseIntl` (brand-proprietary/local asset in CSS)
- **Medium UI font**: `SuisseIntl-Medium`
- **Code font**: `monospace, monospace` where present
- **Weight normal / bold**: `400` / `500` for signature UI; heavier weights exist in generic/commercial modules but are not the premium voice.

```css
@font-face {
  font-display: swap;
  font-family: SuisseIntl;
  font-style: normal;
  font-weight: 400;
}

@font-face {
  font-display: swap;
  font-family: SuisseIntl-Medium;
  font-style: normal;
  font-weight: 500;
}

@font-face {
  font-display: swap;
  font-family: Zapf-Humanist;
  font-style: normal;
  font-weight: 400;
}

:root {
  --aesop-font-body: "SuisseIntl", sans-serif;
  --aesop-font-medium: "SuisseIntl-Medium", sans-serif;
  --aesop-font-display: "Zapf-Humanist", serif;
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **SuisseIntl** — if the licensed face is unavailable, use `Inter` or `Helvetica Neue` at weight 400, but reduce the feeling of modern SaaS by keeping letter-spacing at `0` and avoiding oversized bold labels.
- **SuisseIntl-Medium** — substitute `Inter` 500 only for navigation and label weight. Do not push navigation to 600/700; that turns Aesop into a generic retail header.
- **Zapf-Humanist** — substitute `Georgia` or `Cormorant Garamond` 400 for editorial titles. Tighten line-height from `1.25` to about `1.2` so the replacement keeps the compact literary posture.
- **System fallback** — the CSS includes a broad `system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif` fallback. Treat it as emergency fallback, not the intended aesthetic.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `hero-title` | `1.875rem` | 400 | `1.2` | `0` |
| `content-title-large` | `1.5625rem` | 400 | `1.2` | `0` |
| `nav-category` | `.875rem` | 500 | `1.5` | `0` |
| `body-copy` | `.875rem` | 400 | `1.5` | `0` |
| `product-copy` | `.75rem` | 400 | `normal` | `0` |
| `form-input` | `.875rem` | 400 | `normal` | `0` |

> ⚠️ Aesop does not win by enormous type scale. It wins by switching voice: SuisseIntl for function, Zapf-Humanist for editorial gravity.

### Principles

1. Display text is literary, not loud. `Zapf-Humanist` at 400 gives product storytelling a printed, humanist tone.
2. Navigation uses `.875rem/1.5` with `SuisseIntl-Medium`; category density is controlled by weight 500, not by uppercase or extra tracking.
3. Product tiles are deliberately small. `.75rem` copy lets the object and formulation name sit in a catalog rhythm.
4. Letter-spacing is not a visible signature in the sampled CSS. Do not invent negative tracking to make it feel more "premium."
5. Weight 700 appears in the CSS corpus, but the signature Aesop surface is lighter: 400 body, 500 labels, 400 editorial display.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (neutral-warm system)

| Token | Hex |
|---|---|
| `aesop-surface-warm` | `#FFFEF2` |
| `aesop-surface-soft` | `#F6F5E8` |
| `aesop-surface-alt` | `#EBEADE` |
| `aesop-border-warm` | `#D5D5CB` |
| `aesop-text-primary` | `#333` |
| `aesop-text-strong` | `#000` |
| `aesop-text-muted` | `#666` |
| `aesop-alert-earth` | `#CA432F` |
| `aesop-success-olive` | `#6B6B60` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `aesop-hero-text-light` | `#FFFEF2` |
| `aesop-dark-text-primary` | `#333` |
| `aesop-dark-text-strong` | `#000` |

### 06-3. Neutral Ramp

| Step | Warm neutral | Usage |
|---|---|---|
| 0 | `#FFFEF2` | page floor, light text on dark hero |
| 50 | `#F6F5E8` | soft surfaces, commerce modules |
| 100 | `#F3F3F3` | cool utility surface where present |
| 150 | `#EBEADE` | alternate warm panel |
| 250 | `#D5D5CB` | warm border/hairline |
| 500 | `#999` | disabled/helper text |
| 700 | `#666` | secondary text |
| 900 | `#333` | primary text and dark UI |
| 1000 | `#000` | active/strong text |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Earth alert | alert | `#CA432F` |
| Warm coral | soft accent | `#FF816B` |
| Brown | product/imagery-adjacent accent | `#965D34` |
| Olive | success/status | `#6B6B60` |
| Gold | merchandising/accent | `#E1BE5E` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `h-color-light` | `#FFFEF2` | text over dark/hero surfaces |
| `h-color-primary` | `#333` | primary text |
| `h-color-primary-active` | `#000` | active/hover strong state |
| `h-color-secondary` | `#666` | secondary text and links |
| `h-color-alert` | `#CA432F` | alert/error messaging |
| `h-color-disabled` | `#999` | disabled text |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `surface.page` | `#FFFEF2` | default page and form input background |
| `surface.soft` | `#F6F5E8` | warm alternate modules |
| `text.primary` | `#333` | commerce and editorial text |
| `text.active` | `#000` | active text, hover emphasis |
| `text.muted` | `#666` | secondary links, category descriptions |
| `border.warm` | `rgba(51,51,51,.2)` / `#D5D5CB` | hairlines and form borders |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency |
|---|---|---|
| `text-primary` | `#333` | 766 |
| `surface-warm` | `#FFFEF2` | 557 |
| `text-strong` | `#000` | 276 |
| `text-muted` | `#666` | 180 |
| `text-dark` | `#252525` | 92 |
| `disabled-muted` | `#999` | 70 |
| `surface-soft` | `#F6F5E8` | 68 |
| `utility-surface` | `#F3F3F3` | 50 |
| `surface-alt` | `#EBEADE` | 46 |
| `border-warm` | `#D5D5CB` | 34 |
| `alert-earth` | `#CA432F` | 29 |

### 06-8. Color Stories

**`{colors.surface-warm}` (#FFFEF2)** — This is the Aesop floor. It is close enough to white for commerce clarity, but warm enough to feel like paper, stone, and product packaging rather than a software canvas.

**`{colors.text-primary}` (#333)** — The core ink. Aesop avoids pure black for most reading surfaces, using #333 to keep dense navigation and product copy calm.

**`{colors.text-muted}` (#666)** — Secondary taxonomy and supporting links. It keeps flyouts and product metadata legible without adding a second brand color.

**`{colors.alert-earth}` (#CA432F)** — The only strong chromatic accent in the top observed system. It should remain alert/status/earth-toned, not become a broad CTA brand fill.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `aesop-space-xxs` | `.0625rem` | hairline-level offsets and focus shadow width |
| `aesop-space-xs` | `.3125rem` | compact inline spacing |
| `aesop-space-sm` | `.625rem` | common small gap, product/card internal rhythm |
| `aesop-space-md` | `.9375rem` | row padding and section gutters |
| `aesop-space-lg` | `1.25rem` | component padding, flyout category padding |
| `aesop-space-xl` | `1.875rem` | larger margins and flyout column gutters |
| `aesop-space-2xl` | `2.5rem` | hero body vertical padding |
| `aesop-section-v` | `5rem` | standard `l-section` top/bottom rhythm |

**주요 alias**:
- `l-section__row` → `padding-left/right: .9375rem`, `max-width: 75rem`
- `c-navigation-flyout__row` → `margin: 0 -1.875rem`, `padding: 1.5625rem 0`
- `c-content-hero__body` → `padding: 2.5rem 0 1.5625rem`

### Whitespace Philosophy

Aesop uses air as a retail deceleration device. The hero can be immersive, but product and category modules return to disciplined `.625rem`, `.9375rem`, and `1.25rem` increments. This produces a controlled alternation: broad sensory opening, then compact catalog operation.

The section rhythm is not a decorative "large whitespace" blanket. `l-section` rows sit inside `75rem` max-width with `5rem` vertical rhythm, while flyouts and product tiles compress into narrower module spacing. The brand feels quiet because the layout knows when to breathe and when to sell.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `aesop-radius-none` | `0` | core buttons, grouped inputs, square UI chassis |
| `aesop-radius-hair` | `.0625rem` | rare tiny rounding |
| `aesop-radius-xs` | `.125rem` | minor UI elements |
| `aesop-radius-sm` | `.25rem` | utility cards or panels where present |
| `aesop-radius-md` | `.3125rem` | secondary surfaces |
| `aesop-radius-lg` | `.625rem` | isolated tile/modal style surfaces |
| `aesop-radius-circle` | `50%` | circular controls, icons, swatches |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `focus-ring` | `0 0 0 .0625rem #333` | input hover/focus emphasis |
| `none-default` | `none` | primary commerce chrome; structure relies on borders/surface contrast |

> Aesop's sampled CSS does not expose a rich elevation system. Do not add multi-layer SaaS shadows. The product imagery and video provide depth; the UI chrome stays flat.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `input-focus` | `box-shadow .2s, border-color .2s ease-in-out` | text fields and search inputs |
| `reduced-motion` | `@media (prefers-reduced-motion: reduce)` | accessibility branch present in CSS |
| `hover-capable` | `@media (hover:hover)` | hover-only refinements |
| `hero-video` | observed in screenshot | sensory full-bleed hero with playback/mute controls |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `75rem` for `l-section__row`; older extraction also saw `.main-content { max-width: 60rem }`.
- **Grid type**: Flexbox/BEM layout. `body` and many commerce modules use flex; dense product and navigation systems are component-driven.
- **Column count**: variable; product/category surfaces use repeated `l-column` and `l-row` classes rather than a single named grid token.
- **Gutter**: `.9375rem` section gutters, `.625rem` common module gap, `1.875rem` flyout column gutter.

### Hero
- **Pattern Summary**: `near-100vh + warm full-bleed video/image + centered logo/nav + centered editorial title + outline CTA`
- Layout: full-width hero media with absolute/overlay caption behavior.
- Background: photographic/video hero with amber-brown tone and dark lower gradient/overlay.
- **Background Treatment**: image/video overlay; the UI text is #FFFEF2 over a warm darkened media field.
- H1: about `1.875rem` / weight `400` / tracking `0`.
- Max-width: caption visually constrained near center; page section max-width uses `75rem` below.

### Section Rhythm

```css
.l-section:not(.m-plain) > .l-section__row {
  margin-top: 5rem;
  margin-bottom: 5rem;
}

.l-section:not(.m-full-width) > .l-section__row {
  max-width: 75rem;
  padding-left: .9375rem;
  padding-right: .9375rem;
}
```

### Card Patterns
- **Card background**: usually `#FFFEF2` or image/product asset; cards are not raised by default.
- **Card border**: sparse; flyout uses `1px solid rgba(51,51,51,.2)`.
- **Card radius**: usually `0`; `.25rem`/`.625rem` appear in secondary contexts only.
- **Card padding**: common `1.25rem` and `.625rem`.
- **Card shadow**: absent by default; focus/field emphasis uses 1px box-shadow.

### Navigation Structure
- **Type**: horizontal desktop mega-navigation with multi-level categories; hamburger/mobile structure present.
- **Position**: sticky behavior present via `.l-header.m-sticked`.
- **Height**: not captured as a single token; visual header is tall because logo, top utility links, category nav, and search are stacked around hero.
- **Background**: transparent/light over hero, `#FFFEF2` in flyouts.
- **Border**: flyout top border `1px solid rgba(51,51,51,.2)`.

### Content Width
- **Prose max-width**: not exposed as a named token; extracted `.main-content` max-width is `60rem`.
- **Container max-width**: `75rem`.
- **Sidebar width**: not observed on homepage sample.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `< 48em` | small-screen branch appears as `screen and (max-width:47.99875em)` |
| Tablet | `48em` | repeated `print,screen and (min-width:48em)` media query |
| Desktop | `64em` | repeated `print,screen and (min-width:64em)` and max-width counterpart |
| Large | `75em` | large-screen branch appears as `screen and (min-width:75em)` |

### Touch Targets
- **Minimum tap size**: not proven from CSS summary; buttons and inputs require visual QA on mobile.
- **Button height (mobile)**: not captured as a single token.
- **Input height (mobile)**: `2.5rem` for text/search inputs.

### Collapsing Strategy
- **Navigation**: desktop horizontal/mega-navigation collapses to hamburger/mobile navigation classes (`c-header-mobile-navigation`, `m-hamburger-active`).
- **Grid columns**: component and row classes adjust across `48em`, `64em`, and `75em`.
- **Sidebar**: not observed.
- **Hero layout**: caption alignment modifiers exist (`m-caption-left`, `m-caption-right`, `m-caption-center`); stack/unstack modifiers exist for hero body.

### Image Behavior
- **Strategy**: product and hero media are componentized; hero uses full-bleed media, product tile images sit inside wrappers.
- **Max-width**: image handling not fully summarized from CSS, but product image classes are dominant in HTML.
- **Aspect ratio handling**: not confidently extracted; treat product imagery as fixed component responsibility.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<a class="c-button aesop-button-outline" href="#">
  <span>Discover Solais</span>
  <span aria-hidden="true">→</span>
</a>
```

| Property | Value |
|---|---|
| Font | `SuisseIntl-Medium`, `.875rem`, weight 500 |
| Radius | `0` |
| Border | `1px solid currentColor` |
| Hero text | `#FFFEF2` |
| Padding | use `1rem` to `1.25rem` horizontal rhythm |
| Hover | invert/strengthen border and text; avoid animated lift |
| Focus | use 1px ring, matching form `box-shadow: 0 0 0 .0625rem #333` |

### Badges

> N/A — homepage sample did not expose a strong badge system. Product labels and category titles exist, but no reusable pill badge should be invented.

### Cards & Containers

```html
<article class="c-product-tile">
  <div class="c-product-tile__wrapper">
    <figure class="c-product-tile__figure"></figure>
    <h3 class="c-product-tile__name">Resurrection Aromatique Hand Wash</h3>
  </div>
</article>
```

| Property | Value |
|---|---|
| Product tile color | `#333` |
| Product tile font | `.75rem`, `SuisseIntl` |
| Wrapper dark modifier | `background: #FFFEF2; padding: 1.25rem .625rem` |
| Layout | flex column, full height |
| Disabled | `opacity: .5`, no pointer invitation |
| Shadow | none by default |

### Navigation

```html
<nav class="c-navigation">
  <ul class="c-navigation__list m-level-1">
    <li class="c-navigation__item">
      <a class="c-navigation__link" href="#">
        <span class="c-navigation__link-name">Skin Care</span>
      </a>
    </li>
  </ul>
</nav>
```

| Property | Value |
|---|---|
| Desktop behavior | horizontal category nav with flyout |
| Flyout background | `#FFFEF2` |
| Flyout border | `1px solid rgba(51,51,51,.2)` |
| Category title | `.875rem/1.5 SuisseIntl-Medium` |
| Category link | `.875rem/1.5 SuisseIntl`, `#666`, underlined |
| Mobile behavior | hamburger/header mobile navigation classes present |

### Inputs & Forms

```html
<label class="c-field">
  <input class="c-text-field__input-text" type="search" placeholder="Search..." />
</label>
```

| Property | Value |
|---|---|
| Background | `#FFFEF2` |
| Text | `#333` |
| Border | `1px solid rgba(51,51,51,.2)` |
| Radius | `0` |
| Height | `2.5rem` |
| Padding | `0 1rem` |
| Font | `normal .875rem/normal SuisseIntl,sans-serif` |
| Hover/focus | `border: 1px solid #333; box-shadow: 0 0 0 .0625rem #333` |

### Hero Section

```html
<section class="c-content-hero m-caption-center m-unstack">
  <div class="c-content-hero__caption">
    <div class="c-content-hero__body">
      <p>A striking show of hands</p>
      <h1>New Solais Replenishing Hand Serum</h1>
      <a class="c-button">Discover Solais</a>
    </div>
  </div>
</section>
```

| Property | Value |
|---|---|
| Media | full-bleed video/image |
| Caption | center alignment in observed hero |
| Body padding | `2.5rem 0 1.5625rem` when unstacked |
| Text color | `#FFFEF2` over darkened media |
| CTA style | transparent square outline with arrow |
| Chrome | top navigation floats over media, logo centered |

### 13-2. Named Variants

#### `button-outline-hero`

| Property | Value |
|---|---|
| Background | transparent |
| Text | `#FFFEF2` |
| Border | `1px solid #FFFEF2` |
| Radius | `0` |
| Context | hero CTA over warm dark media |
| State | hover should remain flat; do not add shadow or transform |

#### `button-solid-dark`

| Property | Value |
|---|---|
| Background | `#333` |
| Text | `#FFFEF2` |
| Border | `1px solid #333` |
| Radius | `0` |
| Context | commerce action on warm light surface |
| State | active may strengthen toward `#000` |

#### `input-warm-field`

| Property | Value |
|---|---|
| Background | `#FFFEF2` |
| Text | `#333` |
| Border | `1px solid rgba(51,51,51,.2)` |
| Radius | `0` |
| Height | `2.5rem` |
| Focus | `0 0 0 .0625rem #333` |

### 13-3. Signature Micro-Specs

```yaml
warm-paper-not-white:
  description: "Aesop's core surface craft is a near-white cream floor rather than browser white."
  technique: "background #FFFEF2 on page, flyout panels, form inputs, and product wrappers; #FFF is not the primary shell."
  applied_to: ["body", "{component.Navigation}", "{component.Inputs & Forms}", "{component.Cards & Containers}"]
  visual_signature: "the interface feels printed on warm stock, not rendered on a cold retail canvas"

square-label-controls:
  description: "Premium interaction is built from straight edges and hairlines, like product labels or shelf placards."
  technique: "border-radius: 0; border: 1px solid currentColor or rgba(51,51,51,.2); min-height/height 2.5rem for controls."
  applied_to: ["{component.button-outline-hero}", "{component.button-solid-dark}", "{component.input-warm-field}"]
  visual_signature: "buttons and fields read as architectural labels, never SaaS pills"

humanist-serum-title-switch:
  description: "Editorial title moments switch from commerce sans to a humanist display voice."
  technique: "font-family Zapf-Humanist; font-weight 400; font-size 1.5625rem to 1.875rem; line-height 1.2; letter-spacing 0."
  applied_to: ["{component.Hero Section}", "{component.Cards & Containers}", "{typography.hero-title}", "{typography.content-title-large}"]
  visual_signature: "formulation copy slows down into a literary product label without becoming ornate"

amber-media-flat-chrome:
  description: "Depth is assigned to full-bleed photography/video while commerce chrome remains flat."
  technique: "hero media full-bleed with #FFFEF2 text over warm dark image/video; UI shadow system remains none-default."
  applied_to: ["{component.Hero Section}", "{colors.surface-warm}", "{colors.text-primary}"]
  visual_signature: "the page feels like a dim apothecary window: sensory media behind, printed UI in front"

hairline-focus-drawing:
  description: "Focus and hover states are drawn as exact ink lines instead of animated elevation."
  technique: "border-color #333 plus box-shadow 0 0 0 .0625rem #333; transition box-shadow .2s, border-color .2s ease-in-out."
  applied_to: ["{component.input-warm-field}", "{component.Inputs & Forms}"]
  visual_signature: "state change appears as a precise black-brown rule tightening around the field"
```

---

## 14. Content / Copy Voice
<!-- SOURCE: auto+manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Product name as editorial object; avoid hype language | "New Solais Replenishing Hand Serum" |
| Kicker | Short poetic or sensory line | "A striking show of hands" |
| Body | formulation-first, ingredient-conscious, precise | "Niacinamide, LHA and Dandelion Root brighten and even the skin..." |
| CTA | direct discovery language, not aggressive conversion | "Discover Solais" |
| Category | taxonomic and calm | "Skin Care", "Hand & Body", "Fragrance" |
| Tone | meticulous, cultivated, sensory, restrained | "formulations... created with meticulous attention to detail" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Aesop — copy into your root stylesheet */
:root {
  /* Fonts */
  --aesop-font-family: "SuisseIntl", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --aesop-font-family-medium: "SuisseIntl-Medium", "SuisseIntl", sans-serif;
  --aesop-font-family-display: "Zapf-Humanist", Georgia, serif;
  --aesop-font-weight-normal: 400;
  --aesop-font-weight-medium: 500;

  /* Warm neutral system */
  --aesop-bg-page: #FFFEF2;
  --aesop-bg-soft: #F6F5E8;
  --aesop-bg-alt: #EBEADE;
  --aesop-border-warm: #D5D5CB;
  --aesop-text: #333;
  --aesop-text-strong: #000;
  --aesop-text-muted: #666;
  --aesop-alert: #CA432F;

  /* Key spacing */
  --aesop-space-xs: .3125rem;
  --aesop-space-sm: .625rem;
  --aesop-space-md: .9375rem;
  --aesop-space-lg: 1.25rem;
  --aesop-space-xl: 1.875rem;
  --aesop-section-v: 5rem;

  /* Radius */
  --aesop-radius-control: 0;
  --aesop-radius-small: .25rem;
  --aesop-radius-circle: 50%;
}

body {
  background: var(--aesop-bg-page);
  color: var(--aesop-text);
  font-family: var(--aesop-font-family);
  font-weight: var(--aesop-font-weight-normal);
}

.aesop-display {
  font-family: var(--aesop-font-family-display);
  font-weight: 400;
  line-height: 1.2;
  letter-spacing: 0;
}

.aesop-button {
  background: transparent;
  border: 1px solid currentColor;
  border-radius: var(--aesop-radius-control);
  color: inherit;
  font-family: var(--aesop-font-family-medium);
  min-height: 2.5rem;
  padding: 0 1.25rem;
}

.aesop-field {
  background: var(--aesop-bg-page);
  border: 1px solid rgba(51, 51, 51, .2);
  border-radius: 0;
  color: var(--aesop-text);
  font: normal .875rem/normal var(--aesop-font-family);
  height: 2.5rem;
  padding: 0 1rem;
}

.aesop-field:hover,
.aesop-field:focus {
  border-color: var(--aesop-text);
  box-shadow: 0 0 0 .0625rem var(--aesop-text);
  outline: none;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Aesop-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        aesop: {
          paper: '#FFFEF2',
          soft: '#F6F5E8',
          alt: '#EBEADE',
          border: '#D5D5CB',
          ink: '#333',
          strong: '#000',
          muted: '#666',
          alert: '#CA432F',
        },
      },
      fontFamily: {
        sans: ['SuisseIntl', 'Helvetica Neue', 'Arial', 'sans-serif'],
        display: ['Zapf-Humanist', 'Georgia', 'serif'],
      },
      borderRadius: {
        aesop: '0',
      },
      spacing: {
        aesopXs: '.3125rem',
        aesopSm: '.625rem',
        aesopMd: '.9375rem',
        aesopLg: '1.25rem',
        aesopXl: '1.875rem',
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
| Brand primary | `aesop.alert-earth` | `#CA432F` |
| Background | `aesop.surface-warm` | `#FFFEF2` |
| Background soft | `aesop.surface-soft` | `#F6F5E8` |
| Text primary | `aesop.text-primary` | `#333` |
| Text strong | `aesop.text-strong` | `#000` |
| Text muted | `aesop.text-muted` | `#666` |
| Border | `aesop.border-warm` | `#D5D5CB` |

### Example Component Prompts

#### Hero Section

```text
Aesop 스타일 히어로 섹션을 만들어줘.
- 배경: 따뜻한 amber/brown 계열 full-bleed product/editorial media, 아래쪽 dark overlay
- 로고/네비게이션: 상단 중앙 Aesop wordmark, 카테고리 링크는 SuisseIntl-Medium .875rem
- H1: Zapf-Humanist, 1.875rem, weight 400, line-height 1.2, color #FFFEF2
- 보조문: SuisseIntl, .875rem~1rem, color #FFFEF2
- CTA: transparent outline, border 1px solid #FFFEF2, radius 0, arrow 포함
- 금지: rounded SaaS pill, colorful gradient, card shadow
```

#### Product Tile

```text
Aesop 스타일 제품 타일을 만들어줘.
- 배경: #FFFEF2 또는 제품 이미지 중심의 warm neutral surface
- 텍스트: SuisseIntl .75rem, color #333
- padding: 1.25rem .625rem
- radius: 0
- shadow: none
- 제품명은 차분한 formulation 이름처럼 길어도 허용
- hover는 색/텍스트 강조 정도로 제한하고 translate/shadow lift는 쓰지 마
```

#### Search Field

```text
Aesop 스타일 검색 필드를 만들어줘.
- background #FFFEF2, color #333
- border 1px solid rgba(51,51,51,.2), radius 0
- height 2.5rem, padding 0 1rem
- font normal .875rem SuisseIntl
- focus/hover: border #333 + box-shadow 0 0 0 .0625rem #333
```

#### Navigation

```text
Aesop 스타일 상단 네비게이션을 만들어줘.
- 로고는 중앙, 보조 링크는 좌우에 분산
- 카테고리 링크: SuisseIntl-Medium .875rem/1.5, color는 hero 위에서는 #FFFEF2, light surface에서는 #333
- flyout 배경은 #FFFEF2, top border는 rgba(51,51,51,.2)
- 모바일은 hamburger로 접고, 사각 검색 박스를 유지
```

### Iteration Guide

- **색상 변경 시**: #FFFEF2를 흰색으로 바꾸면 Aesop의 종이 같은 표면이 사라진다.
- **폰트 변경 시**: body와 nav는 sans, title은 humanist serif/display로 역할을 분리한다.
- **여백 조정 시**: `.625rem`, `.9375rem`, `1.25rem`, `1.875rem`, `5rem` 계열을 우선 사용한다.
- **새 컴포넌트 추가 시**: card shadow나 pill radius를 기본값으로 넣지 말고, line/border/surface contrast로 구조를 만든다.
- **CTA 작성 시**: "Buy now!!!" 같은 강한 전환 문구보다 "Discover", "Explore", "See all"처럼 낮은 온도의 동사를 쓴다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #FFFEF2 as the primary page surface; it is the warm paper ground.
- Use #333 for primary text and #666 for secondary taxonomy.
- Use `SuisseIntl` for commerce and `Zapf-Humanist` for editorial title moments.
- Keep controls square: buttons and inputs should use `border-radius: 0`.
- Let product photography and video carry depth instead of UI shadows.
- Use BEM-like structure: `c-*` components, `l-*` layout, `m-*` modifiers.
- Preserve the dual rhythm: immersive editorial hero, then compact commerce modules.

### ❌ DON'T

- 배경을 `#F3F3F3` 중심의 차가운 회색 UI로 두지 말 것 — 대신 `#FFFEF2` 사용.
- 본문 텍스트를 `#252525`처럼 지나치게 검은 앱 UI 잉크로 밀지 말 것 — 대신 `#333` 사용.
- 보조 텍스트를 `#999`로 과하게 비활성화하지 말 것 — 대신 `#666` 사용.
- 핵심 CTA를 `#CA432F` 배경으로 채우지 말 것 — Aesop에서 #CA432F는 alert/earth accent로 제한하고, CTA는 square outline 또는 #333 계열을 우선한다.
- 버튼을 `.625rem` 둥근 카드형 SaaS 버튼으로 만들지 말 것 — 핵심 컨트롤은 `border-radius: 0`.
- product tile에 box-shadow lift를 주지 말 것 — Aesop은 표면, 사진, 타이포로 위계를 만든다.
- headline을 weight 700 이상으로 밀어붙이지 말 것 — Zapf-Humanist 400의 가벼운 문학성이 핵심이다.
- 섹션마다 새로운 brand color를 발명하지 말 것 — neutral system이 브랜드다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second brand color: **none** in the sampled homepage 부티크 — warm neutrals carry the entire identity.
- Gradient UI token: **absent** — hero media has tonal depth, but CSS color identity is never gradient-based.
- Pill-button commerce: **absent** — core 진열대 interaction language is square; pill softness never appears in CTA.
- Raised card deck: **zero** — product 큐레이션박스 modules are flat, not shadow-stacked.
- Neon accent: **never** — chromatic accents stay earthy and sparse, like 공방 pigment marks.
- Loud uppercase marketing voice: **absent** — category and product language stays taxonomic and composed.
- Heavy display shouting: **zero** signature surfaces — display type is 400 humanist, never 700+ billboard.
- Decorative icon system: **none** — arrows/search/utility glyphs support tasks rather than decorate the 부티크 wall.
- Cold white retail shell: **absent** — the surface wants `#FFFEF2` warmth, never browser white.
- SaaS card elevation: **never** — 진열대 separation lives in line, paper, and warm surface contrast only.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-biased sample** — analysis used the saved `/us/` HTML, CSS, and hero screenshot. Checkout, account, store locator, and product detail flows were not visited live in this pass.
- **CSS token graph absent** — `resolved_tokens.json` reported zero CSS custom properties. The guide therefore names practical aliases in frontmatter, but they are derived from real CSS values rather than native `--aesop-*` variables.
- **Brand color ambiguity** — Aesop is neutral-led. `#CA432F` is the strongest observed chromatic semantic color, but it should not be treated like a conventional CTA primary.
- **Motion logic incomplete** — CSS transition and media-query evidence was summarized, but JavaScript carousel/video behavior and scroll-trigger logic were not deeply inspected.
- **Responsive visual QA limited** — breakpoint values were extracted from CSS, but mobile screenshots were not captured in this turn.
- **Component states partial** — hover/focus for inputs are evidenced; loading, disabled, and error states are only partially visible from CSS/HTML summaries.
- **Hero media source not normalized** — the screenshot proves the visual treatment, but the exact video asset, overlay implementation, and image focal rules were not fully decoded.
- **Existing report HTML intentionally untouched** — Step 6 RENDER-HTML was skipped per request; only this `design.md` was regenerated.
