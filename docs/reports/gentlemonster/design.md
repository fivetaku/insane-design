---
schema_version: 3.2
slug: gentlemonster
service_name: Gentle Monster
site_url: https://gentlemonster.com
fetched_at: 2026-05-03T06:33:38Z
default_theme: mixed
brand_color: "#F35C2D"
primary_font: "ABC Favorit / Gentle Sans Regular"
font_weight_normal: 400
token_prefix: gm

bold_direction: Cinematic Luxury
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: luxury-brand
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Next.js CSS bundle exposes 78 CSS variables, custom brand fonts, Tailwind utility layers, Swiper motion, and repeated product-commerce component patterns."

color_system: monochrome-plus-campaign-accent
colors:
  campaign-accent: "#F35C2D"
  surface-light: "#F3F4F6"
  surface-base: "#FFFFFF"
  text-primary: "#111111"
  text-inverse: "#FFFFFF"
  hairline: "#D8D8D8"
  disabled: "#858585"
  focus-blue: "#005FCC"
  swiper-blue: "#007AFF"
  product-blue: "#4798F5"

typography:
  display: "Gentle Monster Serif"
  body: "ABC Favorit / Gentle Sans Regular"
  system_fallback: "Arial, sans-serif"
  ladder:
    - { token: hero-title, size: "visual 32-36px in captured hero", weight: 400, tracking: "normal" }
    - { token: campaign-title, size: "24-28px", weight: 400, tracking: "-0.01em to -0.02em" }
    - { token: nav, size: "13-14px", weight: 400, tracking: "0" }
    - { token: product-meta, size: "12-14px", weight: 350, tracking: "0" }
  weights_used: [350, 400, 500, 600, 700]
  weights_absent: [800, 900]

components:
  button-outline-hero: { bg: "transparent", color: "{colors.text-inverse}", border: "1px solid {colors.text-inverse}", radius: "999px", padding: "approx 10px 24px" }
  button-disabled-solid: { bg: "{colors.disabled}", color: "{colors.text-inverse}", border: "1px solid {colors.disabled}" }
  header-blur: { bg: "rgba(243,244,246,.6)", blur: "15px", shadow: "0 2px 5px rgba(0,0,0,.05)" }
  swiper-pagination-line: { inactive: "8px x 1px hsla(0,0%,7%,.3)", active: "24px x 1px {colors.text-primary}" }
---

# DESIGN.md - Gentle Monster (Designer Guidebook v3.2)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Gentle Monster is not a conventional ecommerce homepage. It behaves like a luxury campaign film that happens to let you buy sunglasses. The captured hero opens with a night-race city scene, a red Disney x F1 object suspended in motion, and the brand name sitting above it like a gallery title. The commercial layer is present, but it is quiet: two outline pills, thin line pagination, and a navigation bar that refuses to compete with the image.

This is a midnight showroom with the lights turned toward one impossible object. The page does not feel like a shop aisle; it feels like a dark museum room where the product is allowed to become the exhibit, the prop, and the poster at once. The site chrome behaves like stage tape on a black floor: useful if you look for it, invisible if you are watching the performance.

The system is fundamentally monochrome. The dependable UI grammar is #111111 (`{colors.text-primary}`), #FFFFFF (`{colors.surface-base}`), #F3F4F6 (`{colors.surface-light}`), and #D8D8D8 (`{colors.hairline}`). Color enters as campaign material, not as a general interface language. #F35C2D (`{colors.campaign-accent}`) is memorable in this capture because the product itself carries it; the UI does not spread that orange-red into every CTA, chip, or hover state. There is no second brand color waiting in the interface. The orange-red is quarantined inside the image like a flare reflected in glass, never converted into button paint.

The typography is split between retail clarity and editorial theater. Utility text uses ABC Favorit / Gentle Sans Regular at small sizes and mostly 400 or 350 weight. The display face is a Gentle Monster serif, used sparingly for the logo and campaign title. This is important: the brand does not make everything serif. Serif is a title instrument, not a body font.

The most distinctive craft is not a component library with many decorated states. It is the discipline around absence: almost no card chrome in the hero, almost no border radius except functional controls, almost no shadow except overlays/dialogs, and a strict refusal to invent a second brand color. Navigation becomes glass only when it must remain legible over content. The header is not a bar so much as a pane of showroom glass: #F3F4F6 (`{colors.surface-light}`) thinned to translucency, blurred just enough to keep the product film readable underneath.

The carousel language is equally specific. Instead of friendly dots, the pagination uses hairline marks, like edit points on a film strip or timing ticks under a title sequence. The result is luxury-commerce without catalogue bulk: photography does the shouting, the interface whispers in #FFFFFF (`{colors.text-inverse}`), and every border seems to ask whether it has earned the right to exist.

### Key Characteristics

- Full-bleed cinematic hero imagery anchors the first viewport.
- Monochrome UI system with campaign color restricted to product/image content.
- Centered brand wordmark and quiet horizontal navigation.
- White outline pill CTAs on dark hero imagery.
- Header uses #F3F4F6 translucent blur when scrolled or opened.
- Thin 1px swiper pagination lines replace dot-heavy carousel language.
- Product grid patterns use even columns, dense image-first commerce, and minimal text.
- Custom brand fonts are loaded through Next.js generated font families.
- Motion comes from Swiper and controlled opacity/transform transitions, not decorative page effects.
- Forms and disabled states are utilitarian: #858585 disabled fill, #005FCC focus outline.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Cinematic Luxury
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **night-race product cinema with restrained commerce chrome**으로 기억된다.
> **Code Complexity**: high - full-bleed media, Swiper behavior, responsive header states, blur overlays, and commerce components require coordinated CSS/JS.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Gentle Monster처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "ABC Favorit", "Gentle Sans Regular", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #111111; }
body { background: var(--bg); color: var(--fg); }

/* 3. 캠페인 컬러는 UI가 아니라 이미지/제품에만 */
:root { --campaign-accent: #F35C2D; }
.hero-cta { border: 1px solid #FFFFFF; color: #FFFFFF; background: transparent; }
```

**절대 하지 말아야 할 것 하나**: #F35C2D를 사이트 전체 primary button 색으로 뿌리지 말 것. Gentle Monster의 브랜드는 색상 토큰이 아니라 흑백 chrome + 캠페인 이미지의 긴장으로 만들어진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://gentlemonster.com` |
| Captured page title | `Home | Gentle Monster US Official Site` |
| Fetched | 2026-04-14 phase1 artifacts reused; guidebook regenerated 2026-05-03 |
| Extractor | Existing phase1 JSON + existing CSS/HTML + existing hero screenshot |
| HTML size | 890607 bytes |
| CSS files | 12 external CSS files, 479579 total CSS characters |
| Token prefix | `gm` analytical alias; source variables are mixed (`--font-*`, `--tw-*`, `--swiper-*`, `--fill-*`) |
| Method | CSS custom properties, frequency candidates, screenshot observation, and targeted CSS/HTML inspection |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js application shell. CSS links are emitted under `/_next/static/css/`.
- **Design system**: brand-local system in use, not a public named DS. It combines generated Next font families, Tailwind utility output, Swiper carousel CSS, and custom header/product classes.
- **CSS architecture**:
  ```css
  :root                      /* header, footer, font, Swiper, Tailwind variables */
  .text-color-* / .bg-color-* /* semantic utility classes */
  .header-*                  /* responsive navigation states */
  .swiper-*                  /* carousel runtime components */
  .module_hash__class        /* Next CSS module surfaces */
  ```
- **Class naming**: mix of Tailwind utilities, global utility names, and CSS-module names such as `_reactive_dialog-mobile__fuEAC`.
- **Default theme**: mixed. Hero is dark image-led; commerce surfaces below use #FFFFFF and #F3F4F6.
- **Font loading**: Next.js generated `@font-face` families such as `__gentleSansRegularEn_bbeda3`, `__gentleMonsterSerif_66f77e`, and fallback companions.
- **Canonical anchor**: the captured hero screenshot at `insane-design/gentlemonster/screenshots/hero-cropped.png`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Gentle Monster Serif` via `--font-gentle-monster-serif` and generated `__gentleMonsterSerif_66f77e`.
- **Body / utility font**: `ABC Favorit / Gentle Sans Regular` via `--font-abc-favorit` and generated `__gentleSansRegularEn_bbeda3`.
- **Light utility font**: `--font-abc-favorit-book` maps to generated `__gentleSansLightEn_162c6d`.
- **Locale fonts**: Korean and CJK variants exist, including `--font-sd-gothic-neo` and generated serif variants for CN/TW/JP/KO.
- **Weight normal / bold**: `400` / `700`, with `350` used heavily for lighter retail text.

```css
:root {
  --gm-font-family: "ABC Favorit", "Gentle Sans Regular", Arial, sans-serif;
  --gm-font-family-display: "Gentle Monster Serif", Georgia, serif;
  --gm-font-weight-light: 350;
  --gm-font-weight-normal: 400;
  --gm-font-weight-bold: 700;
}

body {
  font-family: var(--gm-font-family);
  font-weight: var(--gm-font-weight-normal);
}
```

### Note on Font Substitutes

- **ABC Favorit / Gentle Sans Regular** is a licensed brand-like grotesk. Use **Arial** only as the technical fallback, but tighten the result: keep body at `400`, use `350` only where variable or custom font support exists, and avoid synthetic `600` body copy.
- **Gentle Monster Serif** should be substituted with **Georgia** only for wordmark/campaign title mockups. Reduce letter-spacing to `-0.01em` on larger campaign titles so the fallback does not look bookish.
- **CJK pages** need a separate fallback. Use `Noto Sans KR` or `Noto Serif KR` depending on the source context; do not reuse the English serif for Korean UI labels.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `hero-wordmark` | visual 32-36px in 1280px capture | 400 | normal | 0 |
| `campaign-title` | 24-28px | 400 | 28-36px | `-0.01em` to `-0.02em` |
| `section-heading` | 18-24px | 400 | 24-32px | 0 to `-0.0094em` |
| `body-retail` | 13-16px | 350/400 | 17-24px | 0 |
| `nav-label` | 13-14px | 400 | normal | 0 |
| `micro-meta` | 11-12px | 350/400 | 13-17px | 0 |
| `strong-price/status` | 14-16px | 500/600 | 17-20px | 0 |

> Key insight: the CSS uses a generated utility ladder with many `font-size: calc(Npx - 1px)` declarations, but the visible brand expression is simpler: small retail type plus occasional serif campaign titles.

### Principles

1. Serif is reserved for identity and campaign moments. Body commerce text stays sans.
2. Weight `350` is a real part of the site texture. Replacing it with default `400` everywhere makes product metadata too loud.
3. Display tracking is negative only in selected larger text. Body and navigation keep neutral tracking.
4. `700` exists but is rare. Heavy type is not the brand voice; cinematic imagery carries emphasis.
5. Logo scale is dramatic because it floats over the image, not because the entire page uses oversized type.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand / Campaign Ramp

| Token | Hex |
|---|---|
| `gm-campaign-accent` | `#F35C2D` |
| `gm-product-blue` | `#4798F5` |
| `gm-swiper-blue` | `#007AFF` |
| `gm-focus-blue` | `#005FCC` |

### 06-2. Dark Variant

| Token | Hex |
|---|---|
| `gm-dark-bg` | `#111111` |
| `gm-black` | `#000000` |
| `gm-inverse-text` | `#FFFFFF` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 | `#FFFFFF` | `#000000` |
| 50 | `#F3F4F6` | `#111111` |
| 100 | `#F2F4F5` | `#343434` |
| 200 | `#E2E4E5` | `#525252` |
| 300 | `#D8D8D8` | `#6D6D6D` |
| 500 | `#ABABAB` | `#858585` |
| 700 | `#BFBFBF` | `#111111` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Campaign red-orange | product/campaign image accent | `#F35C2D` |
| Product blue | product/photo color | `#4798F5` |
| Success | status utility | `#008F0E` |
| Focus | accessibility outline | `#005FCC` |
| Swiper default | library token, not brand | `#007AFF` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `gm-text-primary` | `#111111` | default text, active pagination, black utility surfaces |
| `gm-text-inverse` | `#FFFFFF` | hero text and outline CTA on dark media |
| `gm-surface-page` | `#FFFFFF` | product and commerce surfaces |
| `gm-surface-soft` | `#F3F4F6` | scrolled/blurred header fill and light background |
| `gm-border-filter` | `#D8D8D8` | filter lines and light separators |
| `gm-disabled` | `#858585` | disabled button fill/border and muted disabled text |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--fill-gnb-scrolled-bgblur` | `#F3F4F6` | translucent global navigation background |
| `.text-color-primary` | `#111111` | utility text color |
| `.text-color-white` | `#FFFFFF` | inverse text utility |
| `.bg-color-dark` | `#111111` | dark utility surface |
| `.bg-color-light` | `#F3F4F6` | light utility surface |
| `.border-color-filter-line` | `#D8D8D8` | filter/hairline separators |
| `.border-color-menu-bubble` | `#DFE3E8` | menu bubble border |
| `--swiper-theme-color` | `#007AFF` | Swiper library default, not brand primary |

### 06-7. Dominant Colors (actual CSS frequency)

| Token | Hex | Frequency |
|---|---:|---:|
| white | `#FFFFFF` / `#fff` | 57 combined candidate count; 55 CSS literal occurrences |
| ink | `#111111` / `#111` | 61 candidate count; 53 CSS literal occurrences |
| black | `#000000` / `#000` | 50 candidate count; 37 CSS literal occurrences |
| disabled gray | `#858585` | 32 |
| hairline gray | `#D8D8D8` | 30 |
| soft surface | `#F3F4F6` | 14 |
| product blue | `#4798F5` | 11 |
| campaign accent | `#F35C2D` | 10 |

### Color Stories

**`{colors.text-primary}` (`#111111`)** - The actual UI anchor. It is used for default text, dark utility fills, active pagination, and the site's retail clarity. Treat it as the brand's interface voice.

**`{colors.surface-base}` (`#FFFFFF`)** - The commerce floor. Product grids and transactional screens need this neutrality so product photography and campaign media can carry the theatrical load.

**`{colors.surface-light}` (`#F3F4F6`)** - The glass-navigation substrate. It appears in scrolled GNB states as translucent fill rather than a full background personality.

**`{colors.campaign-accent}` (`#F35C2D`)** - A campaign object color, not a UI primary. It can sell the Disney x F1 moment, but it should not become the default CTA background.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `gm-gap-xxs` | `2px` | thin carousel/pagination rhythm |
| `gm-gap-xs` | `4px` | compact text/control clusters |
| `gm-gap-sm` | `8px` | repeated micro spacing |
| `gm-gap-md` | `12px` | small retail groupings |
| `gm-gap-lg` | `24px` | common block spacing and mobile gutters |
| `gm-gap-xl` | `30px` | navigation/content separation |
| `gm-gap-2xl` | `48px` | larger vertical group separation |
| `gm-gap-3xl` | `80px` | editorial/product section air |
| `gm-gap-hero` | `120px` | large campaign separation |

**주요 alias**:
- `--header-pc-height` -> `90px` (desktop navigation height)
- `--header-mo-height` -> `56px` (mobile navigation height)
- `--heading-area-pc-height` -> `60px`
- `--heading-area-mo-height` -> `56px`

### Whitespace Philosophy

Gentle Monster uses air as a camera lens rather than a productivity grid. The hero reserves the first viewport for one image, one logo, one campaign title, and two small CTAs. The empty space around those controls matters because the product is staged like an object in a film frame.

Below the hero, commerce becomes denser. CSS frequencies show repeated `8px`, `12px`, `24px`, and product grid widths like `327px`, `375px`, and `648px`. The rhythm is "open campaign, precise retail": wide cinematic entry, then disciplined product browsing.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `gm-radius-none` | `0` | pagination bars, image boundaries, many layout edges |
| `gm-radius-tight` | `2px` | small controls and technical UI |
| `gm-radius-sm` | `4px` | select/input details |
| `gm-radius-md` | `8px` | common modal/control radius |
| `gm-radius-lg` | `16px` | mobile bottom sheet top corners |
| `gm-radius-circle` | `50%` | circular icon/avatar controls |
| `gm-radius-pill` | `999px` inferred from hero pills | outline CTA capsules |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `gm-shadow-none` | `none` | default cards and hero chrome |
| `gm-shadow-header` | `0 2px 5px 0 rgba(0,0,0,.05)` | scrolled header over content |
| `gm-shadow-dialog-mobile` | `0 0 8px 0 rgba(0,0,0,.1), 0 0 16px 0 rgba(0,0,0,.05)` | mobile reactive dialog |
| `gm-overlay-dim` | `rgba(31,30,29,.6)` | fixed backdrop behind modal surfaces |

Pattern: shadow is modal/header infrastructure. It is not a card decoration language.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `gm-transition-menu` | `right 1s ease-in-out` | large navigation/menu panel movement |
| `gm-transition-dialog` | `transform .24s ease-in-out` | mobile bottom sheet entrance |
| `gm-transition-product` | `transform .42s ease-out` / `opacity .42s ease-out` | product/media reveal behavior |
| `gm-transition-compact` | `transform .2s, top .2s` | small icon/control adjustments |
| `gm-swiper` | `transition-property: transform` | carousel slide movement |

Motion is controlled and mechanical. It supports image browsing and menu reveal; it does not turn the page into a decorative animation surface.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: mixed. Product/detail patterns include `1232px`; module widths include `327px`, `375px`, `648px`, and `100%`.
- **Grid type**: CSS Grid and Flexbox.
- **Column count**: `repeat(1)`, `repeat(2)`, `repeat(3)`, `repeat(4)`, `repeat(5)`, `repeat(6)`, `repeat(8)`, plus detail layouts like `375px 1fr` and `1fr 648px 1fr`.
- **Gutter**: repeated `8px`, `12px`, `24px`, `30px`, `48px`, `80px`.

### Hero

- **Pattern Summary**: `100vh image/video-like campaign scene + centered logo + centered campaign title + dual outline CTA`.
- Layout: full-bleed media, centered overlay text, top navigation over image.
- Background: dark cinematic city/race image from Gentle Monster campaign assets.
- **Background Treatment**: image-overlay by composition; UI text relies on contrast and limited outline controls, not colored panels.
- H1: visual wordmark about 32-36px in captured 1280px hero, serif, white, centered.
- Max-width: viewport-bound media, text grouping centered.

### Section Rhythm

```css
section {
  padding: 48px 24px; /* typical retail/editorial band */
  max-width: 1232px;  /* observed large content anchor */
}

.hero {
  min-height: calc(100vh - var(--header-pc-height));
}
```

### Card Patterns

- **Card background**: usually `#FFFFFF`; hero cards are absent.
- **Card border**: minimal, often `#D8D8D8` only for filter/control separators.
- **Card radius**: `0` for image/product rectangles; `8px` and `16px` appear in controls/dialogs.
- **Card padding**: repeated `0 24px`, `24px`, and `48px 36px` in larger panels.
- **Card shadow**: none by default; mobile dialog has layered shadow.

### Navigation Structure

- **Type**: horizontal desktop GNB with left category links, centered wordmark, right utility icons.
- **Position**: fixed/relative states exist; header interacts with `#main-container` and empty-space spacer.
- **Height**: `90px` desktop, `56px` mobile.
- **Background**: transparent over hero; scrolled/open states use translucent `#F3F4F6` with blur.
- **Border**: generally none; menu/filter contexts use `#D8D8D8` / `#DFE3E8`.

### Content Width

- **Prose max-width**: not a prose-led site; product/campaign modules dominate.
- **Container max-width**: `1232px` for large content, `648px` for focused modules, `375px` for mobile/product-detail lanes.
- **Sidebar width**: detail/filter layouts include fixed lanes such as `185px 1fr` and `375px 1fr`.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `max-width: 767px` | header drops to 56px; main container height becomes auto; mobile dialogs activate |
| Wide mobile | `max-width: 893px` | special header empty-space behavior |
| Tablet | `min-width: 768px and max-width: 1196px` | intermediate product/grid layouts |
| Desktop | `min-width: 1197px` | desktop header and larger grids |
| Large desktop | `min-width: 1621px` and `min-width: 1921px` | large viewport refinements |

### Touch Targets

- **Minimum tap size**: observed controls include `48px!important` heights for mobile/control contexts.
- **Button height (mobile)**: expected around 48px for transactional surfaces; hero pills are visually smaller on desktop.
- **Input height (mobile)**: form CSS uses normal text inputs with transparent background; exact mobile validation state not captured.

### Collapsing Strategy

- **Navigation**: desktop horizontal GNB collapses to mobile header/menu behavior at `767px` and related wide-mobile thresholds.
- **Grid columns**: responsive CSS shifts from 4/5/6/8 column grids to 1/2 column patterns.
- **Sidebar**: detail/filter sidebars collapse or become overlay/mobile panels.
- **Hero layout**: stays image-first; mobile height is recalculated using `--header-mo-height`.

### Image Behavior

- **Strategy**: full-bleed hero media plus product imagery in fixed-width grid modules.
- **Max-width**: many image/container utilities use `100%`.
- **Aspect ratio handling**: product images are structured by module widths; hero is viewport crop, not contained image.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Hero outline pill**

```html
<a class="gm-button gm-button--hero-outline">Shop Now</a>
```

| Spec | Value |
|---|---|
| Background | transparent |
| Text | `#FFFFFF` |
| Border | `1px solid #FFFFFF` |
| Radius | pill / capsule |
| Padding | approx `10px 24px` |
| State | hover should stay restrained; avoid filled campaign color |

**Disabled solid**

```css
button.btn-common:disabled {
  border: 1px solid #858585;
  background-color: #858585;
  color: #fff;
}
```

| State | Value |
|---|---|
| disabled background | `#858585` |
| disabled border | `#858585` |
| disabled text | `#FFFFFF` |
| focus visible | `outline: 2px auto #005FCC` on check/radio label controls |

### Badges

Badges are not a core brand signature in the captured hero. If needed, use monochrome utility chips:

```html
<span class="gm-badge">New</span>
```

| Spec | Value |
|---|---|
| Background | `#F3F4F6` |
| Text | `#111111` |
| Border | `1px solid #D8D8D8` |
| Radius | `999px` |
| Weight | 400 |

### Cards & Containers

Product containers are image-first and low-chrome.

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Border | none by default; `#D8D8D8` only for filters/separators |
| Radius | mostly `0`; use `8px` only for UI panels |
| Padding | `24px` common, `48px 36px` for larger panels |
| Shadow | none for product cards |
| Hover | subtle opacity/transform only; no colored border glow |

### Navigation

```html
<header class="header-wrapper">
  <nav class="gm-gnb">
    <a>Sunglasses</a>
    <a>Glasses</a>
    <strong>GENTLE MONSTER</strong>
    <button aria-label="Search"></button>
  </nav>
</header>
```

| Spec | Value |
|---|---|
| Desktop height | `90px` |
| Mobile height | `56px` |
| Hero state | transparent over image |
| Scrolled state | `linear-gradient(...), rgba(243,244,246,.6)` |
| Blur | `backdrop-filter: blur(15px)` |
| Strong blur | `backdrop-filter: blur(30px)` |

### Inputs & Forms

```css
input[type=text] {
  background-color: transparent;
  outline: none;
}

input[type=text]::placeholder {
  color: #b4b4b4;
}
```

| Spec | Value |
|---|---|
| Background | transparent |
| Focus | explicit outline removed on text input; select focus uses `1px solid #111111` |
| Placeholder | `#B4B4B4` observed in CSS, not in top palette |
| Error | exact validation surface not observed in homepage capture |

### Hero Section

| Spec | Value |
|---|---|
| Background | campaign image, full viewport |
| Wordmark | centered serif, white |
| Campaign title | white serif, centered |
| CTA | two white outline pills |
| Pagination | 1px line bullets, active width expands to 24px |
| Overlay | no visible card; text sits directly on media |

### 13-2. Named Variants

| Variant | Specs |
|---|---|
| `button-outline-hero` | transparent bg, `#FFFFFF` text, `1px solid #FFFFFF`, pill radius, paired CTAs |
| `button-disabled-solid` | `#858585` bg/border, `#FFFFFF` text |
| `header-transparent-hero` | no solid fill, white nav/text over media |
| `header-blur-scrolled` | `rgba(243,244,246,.6)` + `blur(15px)` + subtle shadow |
| `header-blur-strong` | `blur(30px)` for stronger menu/overlay separation |
| `swiper-line-pagination` | inactive `8px x 1px`, active `24px x 1px`, no circular dots |
| `mobile-bottom-dialog` | fixed bottom, `16px 16px 0 0` radius, blur and two-layer shadow |

### Signature Micro-Specs

```yaml
glass-gnb-blur-stack:
  description: "Hero navigation becomes showroom glass only when the image needs legibility protection."
  technique: "linear-gradient(...) over rgba(243,244,246,.6), backdrop-filter: blur(15px), box-shadow: 0 2px 5px rgba(0,0,0,.05); strong overlay state uses blur(30px)"
  applied_to: ["{component.header-blur}", "{component.header-blur-scrolled}", "{component.header-blur-strong}"]
  visual_signature: "A pale frosted strip floats over campaign media without becoming a heavy app bar."

one-pixel-swiper-lines:
  description: "Carousel state is expressed as editorial timing marks, not friendly product dots."
  technique: "inactive bullet: 8px x 1px hsla(0,0%,7%,.3); intermediate: 12px x 1px; active: 24px x 1px {colors.text-primary}; border-radius: 0"
  applied_to: ["{component.swiper-pagination-line}", "{component.swiper-line-pagination}"]
  visual_signature: "The slider reads like a film-strip cue under a campaign title."

campaign-color-quarantine:
  description: "The campaign accent stays inside photography/product material instead of becoming UI paint."
  technique: "UI chrome remains #FFFFFF/{colors.text-inverse}, #111111/{colors.text-primary}, #D8D8D8/{colors.hairline}; #F35C2D/{colors.campaign-accent} is not used as global CTA fill"
  applied_to: ["{component.button-outline-hero}", "{component.header-transparent-hero}", "{component.hero-section}"]
  visual_signature: "The orange-red object feels like a flare in the image, while controls stay monochrome."

bottom-sheet-luxury-modal:
  description: "Mobile overlays get material depth without giving product cards a shadow system."
  technique: "fixed bottom sheet, border-radius: 16px 16px 0 0, backdrop-filter: blur(15px), two-layer soft shadow"
  applied_to: ["{component.mobile-bottom-dialog}"]
  visual_signature: "A controlled glass-material layer rises from the bottom while the commerce grid remains flat."

lightweight-retail-weighting:
  description: "Transactional text is deliberately under-loud, using lighter retail weights against cinematic media."
  technique: "utility/product metadata uses font-weight: 350/400; campaign and wordmark display stay 400; heavy 700 is rare"
  applied_to: ["{component.product-meta}", "{component.nav-label}", "{component.hero-wordmark}"]
  visual_signature: "Commerce metadata feels like small gallery labeling rather than sale signage."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Brand headline | all-caps or title case, sparse, object-led | `GENTLE MONSTER` |
| Campaign title | collaboration name, not benefit copy | `DISNEY x F1 COLLECTION` |
| Primary CTA | direct commerce verb | `Shop Now` / `구매하기` |
| Secondary CTA | campaign exploration | `View Campaign` / `캠페인 보기` |
| Tone | gallery-retail hybrid: minimal words, high visual confidence | "Discover latest sunglasses, glasses, collaborations, and stories" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Gentle Monster - copy into your root stylesheet */
:root {
  /* Fonts */
  --gm-font-family: "ABC Favorit", "Gentle Sans Regular", Arial, sans-serif;
  --gm-font-family-display: "Gentle Monster Serif", Georgia, serif;
  --gm-font-weight-light: 350;
  --gm-font-weight-normal: 400;
  --gm-font-weight-bold: 700;

  /* Core colors */
  --gm-color-campaign-accent: #F35C2D;
  --gm-color-product-blue: #4798F5;
  --gm-bg-page: #FFFFFF;
  --gm-bg-soft: #F3F4F6;
  --gm-text: #111111;
  --gm-text-inverse: #FFFFFF;
  --gm-border: #D8D8D8;
  --gm-disabled: #858585;
  --gm-focus: #005FCC;

  /* Spacing */
  --gm-space-xs: 8px;
  --gm-space-sm: 12px;
  --gm-space-md: 24px;
  --gm-space-lg: 48px;
  --gm-space-xl: 80px;

  /* Radius */
  --gm-radius-control: 8px;
  --gm-radius-dialog: 16px;
  --gm-radius-pill: 999px;
}

body {
  margin: 0;
  background: var(--gm-bg-page);
  color: var(--gm-text);
  font-family: var(--gm-font-family);
  font-weight: var(--gm-font-weight-normal);
}

.gm-hero {
  min-height: calc(100vh - 90px);
  color: var(--gm-text-inverse);
  background: #111111 center / cover no-repeat;
}

.gm-hero__cta {
  border: 1px solid var(--gm-text-inverse);
  color: var(--gm-text-inverse);
  background: transparent;
  border-radius: var(--gm-radius-pill);
  padding: 10px 24px;
}

.gm-header--blur {
  background:
    linear-gradient(180deg, rgba(255,255,255,.25), rgba(242,242,242,0)),
    rgba(243,244,246,.6);
  backdrop-filter: blur(15px);
  box-shadow: 0 2px 5px rgba(0,0,0,.05);
}

.gm-swiper-line {
  width: 8px;
  height: 1px;
  background: rgba(17,17,17,.3);
  border-radius: 0;
}

.gm-swiper-line[aria-current="true"] {
  width: 24px;
  background: var(--gm-text);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js - Gentle Monster analytical theme
module.exports = {
  theme: {
    extend: {
      colors: {
        gm: {
          campaign: '#F35C2D',
          productBlue: '#4798F5',
          page: '#FFFFFF',
          soft: '#F3F4F6',
          text: '#111111',
          inverse: '#FFFFFF',
          border: '#D8D8D8',
          disabled: '#858585',
          focus: '#005FCC',
        },
      },
      fontFamily: {
        sans: ['ABC Favorit', 'Gentle Sans Regular', 'Arial', 'sans-serif'],
        display: ['Gentle Monster Serif', 'Georgia', 'serif'],
      },
      fontWeight: {
        lightRetail: '350',
        normal: '400',
        bold: '700',
      },
      borderRadius: {
        control: '8px',
        dialog: '16px',
        pill: '999px',
      },
      spacing: {
        gmXs: '8px',
        gmSm: '12px',
        gmMd: '24px',
        gmLg: '48px',
        gmXl: '80px',
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
| Campaign accent | `gm-campaign-accent` | `#F35C2D` |
| Background | `gm-bg-page` | `#FFFFFF` |
| Soft surface | `gm-bg-soft` | `#F3F4F6` |
| Text primary | `gm-text` | `#111111` |
| Text inverse | `gm-text-inverse` | `#FFFFFF` |
| Border | `gm-border` | `#D8D8D8` |
| Disabled | `gm-disabled` | `#858585` |
| Focus | `gm-focus` | `#005FCC` |

### Example Component Prompts

#### Hero Section

```text
Gentle Monster style hero section을 만들어줘.
- Full-bleed campaign image/video frame, dark cinematic crop
- Centered wordmark in Gentle Monster Serif / Georgia fallback, white
- Campaign title below product, white, 24-28px, weight 400
- Two transparent outline pill CTAs: border #FFFFFF, text #FFFFFF
- Do not fill the CTA with #F35C2D; keep campaign color inside imagery
- Add thin line pagination: inactive 8px x 1px, active 24px x 1px
```

#### Card Component

```text
Gentle Monster product card를 만들어줘.
- Background #FFFFFF, no shadow, no decorative border
- Product image owns the card; text is small 13-14px ABC Favorit style
- Use #111111 primary text and #858585 only for disabled/muted states
- Keep radius 0 for product image; use 8px only for functional panels
```

#### Badge

```text
Gentle Monster utility badge를 만들어줘.
- Background #F3F4F6, text #111111, border 1px solid #D8D8D8
- Radius 999px, weight 400, compact horizontal padding
- No bright accent fill unless the source campaign itself uses it
```

#### Navigation

```text
Gentle Monster top navigation을 만들어줘.
- Desktop height 90px, mobile height 56px
- Hero state transparent over media with white text/icons
- Scrolled state rgba(243,244,246,.6) + blur(15px) + subtle 0 2px 5px shadow
- Left category links, centered wordmark, right utility icons
```

### Iteration Guide

- **Color changes**: start from #111111/#FFFFFF/#F3F4F6. Add #F35C2D only when the concept is campaign-specific.
- **Typography changes**: preserve the split between sans utility and serif identity.
- **Spacing changes**: keep hero spacious and product grid compact. Do not normalize everything to the same card rhythm.
- **Component additions**: prefer transparent/outline chrome over filled colored UI.
- **Motion**: use carousel transform and restrained opacity/transform transitions; avoid decorative scroll parallax unless campaign media requires it.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #111111 as the primary UI ink and #FFFFFF as the main commerce surface.
- Treat #F35C2D as campaign/product accent, not a universal brand button.
- Keep hero CTAs transparent with #FFFFFF border and #FFFFFF text over dark media.
- Use #F3F4F6 plus `backdrop-filter: blur(15px)` for scrolled glass header states.
- Preserve 1px line pagination with active width expansion to 24px.
- Use custom brand font fallbacks carefully: sans for UI, serif for wordmark/campaign.
- Let product/campaign imagery provide drama; keep chrome minimal.

### ❌ DON'T

- 배경을 `#000000` 또는 generic black floor로 두지 말 것 - commerce surface는 `#FFFFFF`, header soft fill은 `#F3F4F6` 사용.
- 텍스트를 `#000000` 단독으로 두지 말 것 - 기본 UI ink는 `#111111` 사용.
- CTA 배경을 `#F35C2D`로 채우지 말 것 - hero CTA는 `#FFFFFF` outline/text + transparent fill 유지.
- hairline을 `#BFBFBF`로 일반화하지 말 것 - 관찰된 separator는 `#D8D8D8` 또는 `#DFE3E8` 사용.
- disabled state를 `#ABABAB`로 만들지 말 것 - 실제 disabled fill/border는 `#858585` 사용.
- focus outline을 Swiper 기본 파란색 `#007AFF`로 바꾸지 말 것 - 관찰된 접근성 focus는 `#005FCC` 계열 사용.
- product card에 heavy shadow를 넣지 말 것 - shadow는 header/modal infrastructure에만 제한.
- 모든 큰 제목을 serif로 만들지 말 것 - serif는 wordmark/campaign title 중심, retail body는 sans.
- Swiper pagination을 동그란 `#007AFF` dot로 강조하지 말 것 - Gentle Monster captured UI는 1px monochrome line pagination을 쓴다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **Second UI brand color: none** - the system does not maintain a friendly secondary accent for general actions.
- **Gradient brand buttons: absent** - campaign imagery can be colorful, but buttons stay outline/monochrome.
- **Card chrome: nearly zero** - product cards do not need border, glow, and shadow to feel clickable.
- **Heavy display weights: rare** - weight 800/900 is absent from the observed brand texture.
- **Rounded-card marketing sections: not the default** - radius belongs to controls, dialogs, and pills.
- **Decorative icon language: minimal** - utility icons are functional, not expressive illustrations.
- **Generic SaaS purple/blue accent system: absent** - #007AFF exists as Swiper default and #005FCC as focus, not as brand mood.
- **Body copy serif: never as the default** - serif is identity punctuation.
- **Dense explanatory hero copy: absent** - campaign title and CTAs are enough.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage/campaign capture only** - the analysis reuses existing phase1 artifacts and the captured hero screenshot. Checkout, account, search-result, and product-detail flows were not freshly navigated.
- **Desktop screenshot bias** - the visual interpretation is anchored in a 1280x800 hero capture. Mobile behavior is inferred from CSS breakpoints, not a fresh mobile screenshot.
- **Campaign-specific accent** - #F35C2D is treated as the visible campaign accent in the captured Disney x F1 hero and CSS frequency data. It should not be interpreted as a permanent global brand primary.
- **Font family names are generated** - CSS exposes Next.js generated names (`__gentleSansRegularEn_*`, `__gentleMonsterSerif_*`). Human-readable names in this guide are analytical labels mapped from source variables.
- **Form states incomplete** - disabled and focus snippets were observed, but full validation, loading, and error states were not exercised through a real form flow.
- **Motion timing partial** - CSS transition values and Swiper behavior were inspected, but JavaScript-driven campaign timing and autoplay settings were not deeply traced.
- **Color frequency contamination** - #007AFF and some chromatic colors are library/product artifacts. They are documented but intentionally excluded from core brand identity.
- **No HTML report generated** - requested Step 6 RENDER-HTML was skipped; this guidebook produces `design.md` only.
