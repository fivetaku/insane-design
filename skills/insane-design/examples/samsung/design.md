---
schema_version: 3.2
slug: samsung
service_name: Samsung Korea
site_url: https://www.samsung.com/sec/
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: light
brand_color: "#2189FF"
primary_font: "Samsung Sharp Sans"
font_weight_normal: 400
token_prefix: "samsung"

bold_direction: "Consumer Showroom"
aesthetic_category: "editorial-product"
signature_element: "hero_impact"
code_complexity: "high"

medium: web
medium_confidence: high
archetype: editorial-product
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Homepage CSS exposes a broad component system, Samsung font stack, many responsive rules, and consistent pill/card/navigation patterns, but only a small custom-property layer."

colors:
  primary: "#2189FF"
  logo-blue: "#1428A0"
  ink: "#000000"
  ink-soft: "#212425"
  surface: "#FFFFFF"
  surface-muted: "#F7F7F7"
  line: "#DDDDDD"
  line-soft: "#EBEBEB"
  text-muted: "#707070"
  dark-panel: "#313131"

typography:
  display: "Samsung Sharp Sans"
  body: "SamsungOneKorean"
  ladder:
    - { token: hero, size: "54px", weight: 700, line_height: "64px", tracking: "0" }
    - { token: h1, size: "50px", weight: 700, line_height: "59px", tracking: "0" }
    - { token: h2, size: "46px", weight: 700, line_height: "54px", tracking: "0" }
    - { token: subhead, size: "24px", weight: 700, line_height: "28px", tracking: "0" }
    - { token: body-large, size: "22px", weight: 400, line_height: "33px", tracking: "0" }
    - { token: body, size: "18px", weight: 400, line_height: "27px", tracking: "0" }
  weights_used: [300, 400, 500, 600, 700, 800]
  weights_absent: []

components:
  button-primary-pill: { bg: "{colors.ink-soft}", fg: "{colors.surface}", radius: "20px-30px", height: "32px-50px" }
  button-outline-pill: { bg: "{colors.surface}", fg: "{colors.ink-soft}", border: "1px solid #212425", radius: "20px-30px" }
  search-icon-pill: { bg: "{colors.surface-muted}", border: "1px solid #F7F7F7", radius: "40px", size: "36px" }
  product-card-image: { bg: "{colors.surface-muted}", radius: "10px", size: "240px" }
---

# DESIGN.md — Samsung Korea

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Samsung Korea is not a pure blue brand page on the homepage. It behaves like a department-store electronics showroom after the lights have been tuned for launch day: the floors are neutral, the signs are precise, and the products are the only objects allowed to glow. Large product photography owns the first impression, while the UI chrome stays almost invisible. The Samsung wordmark sits small and white over the hero, then the rest of the surface depends on product categories, appliance scenes, and promotional modules rather than a loud global brand skin.

The captured hero is a Bespoke kitchen scene with a saturated blue environment, white typography, and a tiny outline pill. It reads less like a web banner and more like an appliance showroom window: the room supplies the color, the product supplies the lifestyle promise, and the interface behaves like small price tags placed on the glass. This creates the key Samsung pattern: the product world provides color and atmosphere, while the interface uses #000000 (`{colors.ink}`), #FFFFFF (`{colors.surface}`), #F7F7F7 (`{colors.surface-muted}`), and restrained #2189FF (`{colors.primary}`) only when interaction needs emphasis.

Typography is proprietary and blunt. `Samsung Sharp Sans` carries the high-impact English display voice; `SamsungOneKorean` carries Korean UI and body copy. The system prefers bold display weight and direct spacing over delicate editorial contrast. It is crisp, commercial, and engineered for category switching: mobile, TV, appliances, IT, benefits, carts, search, and account flows all need to coexist.

There is no second brand color trying to compete with the products. #2189FF (`{colors.primary}`) is not poured across the page like corporate paint; it is kept as a small interaction accent. The actual Samsung blue field often arrives through photography, as if the catalog ink has moved from the interface into the room itself. Shadow is similarly disciplined: the chrome does not become a floating SaaS surface, because depth is expected to come from product imagery, gray trays, and the photographed scene.

The component language is pill-shaped and utility-heavy. Buttons are not decorative capsules; they are compact purchase/navigation controls with 20px to 30px radii, 32px to 50px heights, and a strong black/white polarity. Cards use pale gray trays, product imagery, and simple type hierarchy. The page is a catalog with showroom lighting: not a dashboard, not a magazine, and not a blue brand poster. The site keeps removing itself until appliances, phones, TVs, search, cart, and account utilities can all sit on the same polished retail floor.

### Key Characteristics

- Large product hero with full-bleed photography/video logic and minimal overlaid UI.
- Proprietary Samsung font stack: `Samsung Sharp Sans` for display, `SamsungOneKorean` for Korean body.
- Neutral-first UI: #000000, #FFFFFF, #F7F7F7, #707070, #DDDDDD dominate measured CSS.
- #2189FF appears as the main chromatic UI accent, while #1428A0 is closer to corporate/logo heritage.
- Pill controls are canonical: 20px, 30px, 40px, and circular icon radii recur.
- Header and global navigation are dense, high-z-index, responsive, and utility-driven.
- Product/card surfaces use pale gray trays and 10px to 20px rounding rather than heavy elevation.
- Responsive system is desktop-first with many max-width breakpoints and hamburger collapse.
- Motion is conservative: opacity, background-color, border-color, and transform transitions, not playful animation.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Consumer Showroom
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **hero_impact**으로 기억된다.
> **Code Complexity**: high — broad legacy-plus-revamp CSS, dense global navigation, many responsive breakpoints, and multiple component systems coexist.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Samsung Korea처럼 만들기 — 3가지만 하면 80%

```css
/* 1. proprietary-feeling Samsung stack */
body {
  font-family: "SamsungOneKorean", "Dotum", "Apple SD Gothic Neo", Arial, sans-serif;
  font-weight: 400;
  letter-spacing: 0;
}
.hero-title,
.display {
  font-family: "Samsung Sharp Sans", "SamsungOneKorean", sans-serif;
  font-weight: 700;
}

/* 2. neutral showroom floor */
:root {
  --samsung-bg: #FFFFFF;
  --samsung-bg-muted: #F7F7F7;
  --samsung-ink: #000000;
  --samsung-muted: #707070;
  --samsung-line: #DDDDDD;
}

/* 3. restrained interaction accent */
:root { --samsung-primary: #2189FF; }
.btn-primary {
  background: #212425;
  color: #FFFFFF;
  border-radius: 30px;
  height: 50px;
  padding: 0 24px;
}
```

**절대 하지 말아야 할 것 하나**: Samsung을 파란 UI 테마로 칠하지 말 것. 홈페이지의 색감은 제품 사진이 담당하고, UI 시스템은 neutral + black/white pill + 소량의 #2189FF로 유지된다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.samsung.com/sec/` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | Existing phase1 reuse: HTML/CSS/screenshot already present |
| HTML size | 434711 bytes |
| CSS files | external CSS + inline CSS, including `common.css`, `component.css`, `newComponent.css`, `layout.css`, `revamp_gnb.css` |
| Token prefix | `samsung` |
| Method | CSS frequency, phase1 component/layout/responsive extraction, screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: server-rendered Samsung commerce/marketing stack with large static CSS bundles.
- **Design system**: Samsung web component layer, not a clean token-first public DS. `bricsModule`, `wrap-component`, global header, product card, app-layer, and GNB CSS coexist.
- **CSS architecture**:
  ```text
  font layer       @font-face for Samsung Sharp Sans, SamsungOneKorean, Samsung Korea Sans
  global layer     reset/common/layout/navigation rules
  module layer     wrap-component and bricsModule data-attribute components
  commerce layer   product cards, options, forms, modal/app flows
  ```
- **Class naming**: mixed legacy utility/component naming: `.wrap-component`, `.bricsModule`, `.btn-type2`, `.card-images`, `#header__navi`, `.navigation-wrap`.
- **Default theme**: light, with white page chrome and gray module trays.
- **Font loading**: self-hosted Samsung web fonts from `/sec/static/_font/`.
- **Canonical anchor**: `https://www.samsung.com/sec/`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Samsung Sharp Sans` (Samsung proprietary web font)
- **Korean/body font**: `SamsungOneKorean`
- **Supplemental Korean font**: `Samsung Korea Sans`
- **Fallbacks observed**: `Dotum`, `돋움`, `Apple SD Gothic Neo`, `Arial`, `sans-serif`
- **Weight normal / bold**: `400` / `700`

```css
@font-face {
  font-family: "Samsung Sharp Sans";
  font-weight: bold;
  src: url("/sec/static/_font/SamsungSharpSans-Bold.woff2") format("woff2");
}
@font-face {
  font-family: "SamsungOneKorean";
  font-weight: normal;
  src: url("/sec/static/_font/SamsungOneKorean-400.woff2") format("woff2");
}
body {
  font-family: "SamsungOneKorean", "Dotum", "Apple SD Gothic Neo", Arial, sans-serif;
  font-weight: 400;
}
.font-sans,
.hero-title {
  font-family: "Samsung Sharp Sans", "SamsungOneKorean", "Dotum", sans-serif;
  font-weight: 700;
}
```

### Note on Font Substitutes

- **Samsung Sharp Sans** is proprietary. Use **Inter Tight** or **Arial** only as a structural fallback, then increase display weight to 700 and keep letter-spacing at `0`; do not add fashionable negative tracking unless a component explicitly does it.
- **SamsungOneKorean** can be approximated with **Noto Sans KR** at 400/700. Keep Korean body line-height near `1.5`; Samsung's Korean UI reads clean but not compressed.
- If replacing both fonts, split roles: one display face for English product headlines and one Korean-optimized body face. A single generic `system-ui` stack makes the page lose the Samsung showroom tone.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `bricsHead veryLarge` | 54px | 700 | 64px | 0 |
| `bricsHead large` | 50px | 700 | 59px | 0 |
| `bricsHead normal` | 46px | 700 | 54px | 0 |
| `bricsHead small` | 42px | 700 | 50px | 0 |
| `bricsHead verySmall` | 38px | 700 | 45px | 0 |
| `bricsSubHead normal` | 24px | 700 | 28px | 0 |
| `bricsDesc large` | 22px | 400 | 33px | 0 |
| `bricsDesc normal` | 20px | 400 | 30px | 0 |
| `bricsDesc small` | 18px | 400 | 27px | 0 |
| `card-desc` | 12px | 400 | 1.4 | 0 |
| `app-pgTitle` | 24px | 700 | 32px | 0 |

> ⚠️ Key insight: Samsung's homepage typography is not an airy editorial system. It is bold, direct, category-safe typography that keeps `letter-spacing: 0` in most extracted rules and uses weight rather than tracking for emphasis.

### Principles

1. Display weight is blunt: `700`/`bold` is the default way to make product headlines feel Samsung, not thin luxury type.
2. English display and Korean UI are separated. Use `Samsung Sharp Sans` for hero/product naming and `SamsungOneKorean` for Korean copy.
3. Body copy breathes through line-height, not letter-spacing. The `18px / 27px`, `20px / 30px`, and `22px / 33px` patterns keep Korean copy readable.
4. Component text is compact. Product card descriptions drop to `12px` with #707070, while card prices/titles hold stronger black hierarchy.
5. Do not invent optical quirks. The observed system prefers `letter-spacing: 0`; only local legal/reference text uses tighter values such as `-0.02em`.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed chromatic anchors)

| Token | Hex |
|---|---|
| `{colors.primary}` | #2189FF |
| `samsung-primary-alt` | #2188FF |
| `{colors.logo-blue}` | #1428A0 |
| `samsung-alert-red` | #FA2337 |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| `surface` | #FFFFFF | #313131 |
| `surface-muted` | #F7F7F7 | #212425 |
| `line-soft` | #EBEBEB | #444444 |
| `line` | #DDDDDD | #555555 |
| `disabled` | #B2B2B2 | #707070 |
| `ink` | #000000 | #FFFFFF |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Interactive blue | primary | #2189FF |
| Corporate blue | logo/corporate | #1428A0 |
| Alert/promo red | alert | #FA2337 |
| Swiper default blue | vendor | #007aff |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `samsung-bg-page` | #FFFFFF | Header, modal, base page chrome |
| `samsung-bg-muted` | #F7F7F7 | Search button, navigation wrap, cards/trays |
| `samsung-text` | #000000 | Primary text, icons, high-contrast UI |
| `samsung-text-soft` | #212425 | Button foreground/borders, dark CTA surfaces |
| `samsung-text-muted` | #707070 | Secondary product copy and descriptions |
| `samsung-border` | #DDDDDD | Section and form separators |
| `samsung-primary` | #2189FF | Main chromatic interaction accent |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--themeColorActive` | #FFFFFF | GNB/theme active surface |
| `--themeColorinActive` | #000000 | GNB/theme inactive foreground |
| `--cateBgColor` | #313131 | Category background token |
| `--swiper-navigation-color` | #000000 | Vendor carousel navigation |
| `--swiper-theme-color` | #007aff | Vendor carousel accent |

### 06-7. Dominant Colors (actual CSS frequency)

| Token | Hex | Frequency |
|---|---|---|
| `ink` | #000000 | 3067 |
| `surface` | #FFFFFF | 1199 |
| `muted-text` | #707070 | 1019 |
| `primary-blue` | #2189FF | 575 |
| `line` | #DDDDDD | 458 |
| `pale-line` | #D9D9D9 | 449 |
| `surface-muted` | #F7F7F7 | 344 |
| `line-soft` | #EBEBEB | 327 |

### Color Stories

**`{colors.ink}` (#000000)** — The real workhorse. Samsung uses black for the logo in light chrome, major text, iconography, separators, and product-card hierarchy; it is the visual spine of the UI.

**`{colors.surface}` (#FFFFFF)** — The default showroom wall. Header, modal, and page chrome stay white so product photography can carry category-specific color without fighting the interface.

**`{colors.text-muted}` (#707070)** — Samsung's secondary information tone. Product descriptions, captions, and dense commerce text use this rather than a softer blue-gray.

**`{colors.primary}` (#2189FF)** — The functional blue accent. It is present and frequent, but it is not painted across the whole UI; use it for interaction emphasis, not for backgrounds everywhere.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `header-x` | 24px | Global header side padding |
| `component-y` | 60px | Default `.wrap-component` vertical padding |
| `component-narrow` | 40px | Narrow module top/bottom padding |
| `component-normal` | 70px | `bricsModule` normal vertical padding |
| `component-wide` | 100px | Wide module vertical padding |
| `component-veryWide` | 140px | High-impact product/editorial modules |
| `product-card-gap` | 40px | Carousel inner gap token |
| `card-padding` | 10px | Product image tray padding |
| `app-content-padding` | 30px 12px 60px | App/modal content flows |

**주요 alias**:
- `--cpCarousel-gap-innr` → 40px (carousel/card inner gap)
- `--cpCarousel-gap-flag` → 12px (flag/label spacing)
- `--cpCarousel-gap-price` → 6px (price grouping)

### Whitespace Philosophy

Samsung uses two kinds of whitespace. Hero and product modules are generous because products need room to look physical: 60px, 100px, and 140px vertical bands create a showroom rhythm. Commerce modules then become much tighter; product cards, prices, flags, and modal forms compress into 6px, 10px, 12px, and 24px increments.

This is not a single 4/8 scale. It is a retail split: big air around photography, dense spacing around choice, price, option, and account flows. Preserve that contrast.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| `button-small-pill` | 20px | `.btn-d`, `.btn-s` compact controls |
| `button-large-pill` | 30px | `.btn-l` primary large button |
| `search-pill` | 40px | 36px circular/rounded search button |
| `product-card-tray` | 10px | `.card-images` gray product tray |
| `brics-round` | 16px | `bricsModule [data-radius="round"]` |
| `card-figure` | 20px | product figure mask/pseudo element |
| `radio` | 50% | custom radio control |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `nav-overlay-dim` | rgba(0,0,0,0.5) / rgba(0,0,0,0.6) masks | Menu overlays and modal dimming |
| `component-elevation` | sparse `box-shadow` usage | Occasional component depth, not dominant |
| `product-depth` | photography-dependent | Product imagery and scene lighting carry most depth |

Samsung does not rely on a deep, named elevation ladder on the homepage CSS. The perceived depth mostly comes from photographed devices/appliances, gradients in the hero image, and modal overlays.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `gnb-color-shift` | `.5s cubic-bezier(0.35,0,0.36,1)` | Header background/border transitions |
| `mask-fade` | `.3s` opacity | Global overlay dimming |
| `button-hover` | color/background change | `.btn-type2:hover` changes to #555 / #eee |
| `nav-transform` | `translateX(-50%)` | Fixed navigation alignment |

Motion supports navigation state and modal state. Avoid bounce, spring, particle, or playful transforms; Samsung's homepage motion should feel like engineered interface feedback.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: 1440px and 1600px are the main desktop anchors; product/editorial modules also expose 1920px and 1680px containers.
- **Grid type**: mixed Flexbox and module-specific layouts. Global header uses flex; cards/carousels use flex and carousel wrappers.
- **Column count**: not a single 12-column grid. Category modules and product cards vary by component.
- **Gutter**: 24px header/container side padding; 40px carousel inner gap; dense 6px/12px commerce spacing.

### Hero

- **Pattern Summary**: full-bleed product scene + top overlay navigation + left-aligned display copy + small pill CTA.
- Layout: image-led editorial product hero, text overlaid on left.
- Background: photographed/retouched product environment, not CSS brand gradient.
- **Background Treatment**: image/video overlay with scene lighting; captured hero uses blue Bespoke kitchen photography.
- H1: `Samsung Sharp Sans` style, visually about 54px / weight 700 / tracking 0.
- Max-width: hero media can extend to 1920px-style full viewport; content sits inside desktop safe area.

### Section Rhythm

```css
.wrap-component {
  margin: 0 auto;
  padding: 60px 0;
}
.wrap-component.w1440px { max-width: 1440px; }
.bricsModule[data-top="wide"] { padding-top: 100px; }
.bricsModule[data-bottom="veryWide"] { padding-bottom: 140px; }
```

### Card Patterns

- **Card background**: #F7F7F7 and #F4F4F4 trays.
- **Card border**: often none; separators use #DDDDDD / #D9D9D9.
- **Card radius**: 10px product image trays, 20px figure masks, 16px rounded brics modules.
- **Card padding**: 10px image trays, 24px item padding, dense 6px/12px product metadata gaps.
- **Card shadow**: minimal. Product imagery and gray trays define depth.

### Navigation Structure

- **Type**: horizontal global navigation with utility icons and hamburger/mobile collapse.
- **Position**: relative/fixed variants, high z-index, overlay masks.
- **Height**: legacy header 80px; revamp GNB wrapper 106px with inner 57px logo row.
- **Background**: #FFFFFF in page chrome; captured hero can invert icons/logo to white over imagery.
- **Border**: #EBEBEB / transparent border-bottom depending state.

### Content Width

- **Prose max-width**: module-specific; not a long-form editorial prose site.
- **Container max-width**: 1440px primary, 1600px/1680px/1920px for wider product modules.
- **Sidebar width**: not central on homepage; overlays, drawers, category panels, and modals matter more.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Narrow mobile | 280px-430px | many defensive max-width rules for small devices |
| Mobile | 480px-600px | dense product/card and text adjustments |
| Tablet | 800px-1100px | fold/navigation/component adjustments |
| Desktop compression | 1280px | header/back button and global layout shifts |
| Desktop container | 1440px-1600px | core content width anchors |

### Touch Targets

- **Minimum tap size**: many controls meet or exceed 44px; extracted values include 44px, 48px, 50px, 56px, 60px, 66px, 70px.
- **Button height (mobile)**: varied; compact controls can be 32px/40px while large CTAs reach 50px+.
- **Input height (mobile)**: varied; forms include 44px, 46px, 48px, 50px, 60px and hidden 1px checkbox/radio accessibility inputs.

### Collapsing Strategy

- **Navigation**: hamburger / icon utility collapse.
- **Grid columns**: component-specific collapse rather than one universal grid rule.
- **Sidebar**: not a homepage primary surface; overlays and drawers are the practical collapse form.
- **Hero layout**: media remains dominant; text and CTA scale/stack within safe areas.

### Image Behavior

- **Strategy**: product imagery is explicit and module-owned.
- **Max-width**: containers govern image scale; product trays often fixed or ratio-like.
- **Aspect ratio handling**: video/product components use `object-fit: cover` on desktop and `object-fit: fill` in a narrow mobile case.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

Samsung buttons are black/white pills first, blue accents second.

| Variant | Background | Text | Border | Radius | Height |
|---|---|---|---|---|---|
| `.btn-type1` | #FFFFFF | #212425 | 1px solid #212425 | 20px-30px | 32px-50px |
| `.btn-type2` | #212425 | #FFFFFF | #212425 | 20px-30px | 32px-50px |
| `.btn-type2:hover` | #555555 | #EEEEEE | inherited | 20px-30px | same |
| `.btn-d` | contextual | contextual | contextual | 20px | 40px |
| `.btn-s` | contextual | contextual | contextual | 20px | 32px |
| `.btn-l` | contextual | contextual | 2px solid | 30px | 50px |

```html
<a class="btn btn-l btn-type2" href="#">Shop</a>
<a class="btn btn-l btn-type1" href="#">Learn more</a>
```

States observed: hover, focus, active, disabled. Disabled uses opacity `0.3`; focus states rely on outline patterns for native controls.

### Badges

Badges/flags are commerce utility elements, not decorative pills. Carousel tokens expose `--cpCarousel-gap-flag: 12px` and `--cpCarousel-fontsize-flag: 14px`; use them near product cards and price blocks.

### Cards & Containers

| Component | Surface | Radius | Padding | Notes |
|---|---|---|---|---|
| `.card-images` | #F7F7F7 | 10px | 10px | 240px product image tray |
| `.card-item-inner` | #F4F4F4 | component-specific | 0 | commerce/card container |
| `.card-desc` | transparent | none | margin 12px 0 | #707070, 12px body |
| `.bricsModule[data-radius="round"]` | contextual | 16px | module-owned | editorial/product modules |

Avoid making cards look like SaaS dashboards. Samsung cards are product shelves: pale tray, product image, black price/type hierarchy, muted description.

### Navigation

Global navigation is a major component system:

- `#header__navi` height 106px, #FFFFFF background, high z-index.
- `.header__inner` max-width 1440px, `display: flex`, `padding: 0 24px`.
- `.search__btn` is 36px square, #F7F7F7 background, 40px radius, 1px #F7F7F7 border, hover border rgba black.
- Overlays use fixed masks with rgba(0,0,0,0.5) to rgba(0,0,0,0.6).

### Inputs & Forms

Inputs are heavily accessibility-wrapped:

- Hidden native checkbox/radio inputs can be `1px` with visible custom labels.
- Radio controls use 20px circular image backgrounds.
- Focus states include `outline: 2px dotted black` or native focus ring.
- Text inputs inherit `SamsungOneKorean`, not the display font.

### Hero Section

Hero section behavior:

- Full-bleed or near full-bleed product media.
- White logo/icons/text when the hero image is dark/saturated.
- Left text block with high-weight Samsung display type.
- Compact outline pill CTA over image, not a large SaaS CTA cluster.

### 13-2. Named Variants

#### `button-primary-pill`

- bg #212425, fg #FFFFFF, radius 20px/30px, height 32px-50px.
- Use for primary commerce action, not for every link.

#### `button-outline-pill`

- bg #FFFFFF, fg #212425, border 1px solid #212425, radius 20px/30px.
- Use for secondary action in neutral page chrome.

#### `search-icon-pill`

- bg #F7F7F7, border 1px solid #F7F7F7, radius 40px, size 36px.
- Hover changes border-color to rgba(0,0,0,0.2).

#### `product-card-image`

- bg #F7F7F7, radius 10px, padding 10px, typical image box 240px.
- Use as a product tray, not as a generic content card.

### 13-3. Signature Micro-Specs

```yaml
showroom-photography-color-field:
  description: "Brand atmosphere is delegated to product photography instead of a global blue UI wash."
  technique: "Neutral chrome uses #000000, #FFFFFF, #F7F7F7, and #707070; #2189FF appears only as restrained interaction accent."
  applied_to: ["{component.hero}", "{component.category-modules}", "{component.product-campaigns}"]
  visual_signature: "The room, appliance, phone, or TV scene becomes the color system while the interface recedes like showroom glass."

black-white-commerce-pill:
  description: "Retail actions use compact black/white pills instead of colorful SaaS CTA blocks."
  technique: "background #212425 with #FFFFFF text, or #FFFFFF with 1px solid #212425; border-radius 20px-30px; height 32px-50px."
  applied_to: ["{component.button-primary-pill}", "{component.button-outline-pill}", "{component.shopping-actions}"]
  visual_signature: "Purchase/navigation controls feel like precise product labels rather than decorative capsules."

gray-product-tray-shelf:
  description: "Product cards create depth with pale trays and imagery, not expressive elevation."
  technique: ".card-images background #F7F7F7, border-radius 10px, padding 10px, typical product image box 240px; description text #707070 at 12px."
  applied_to: ["{component.product-card-image}", "{component.card-images}", "{component.card-desc}"]
  visual_signature: "Products sit on a clean retail shelf: pale gray base, sharp black hierarchy, almost no shadow."

utility-gnb-mask-layer:
  description: "A dense catalog navigation stays controlled through fixed masks, high stacking, and muted motion."
  technique: "#header__navi height 106px, #FFFFFF background, high z-index; .header__inner max-width 1440px with padding 0 24px; overlays use rgba(0,0,0,0.5)-rgba(0,0,0,0.6); transition .5s cubic-bezier(0.35,0,0.36,1)."
  applied_to: ["{component.global-navigation}", "{component.drawers}", "{component.modal-overlays}"]
  visual_signature: "The product catalog can expand without turning into a dashboard; the page dims like a showroom lights-down state."

soft-search-icon-pill:
  description: "Search is presented as a small utility object, not a full search hero."
  technique: ".search__btn is 36px square with #F7F7F7 background, 1px #F7F7F7 border, border-radius 40px; hover border-color rgba(0,0,0,0.2)."
  applied_to: ["{component.search-icon-pill}", "{component.header-utility-icons}"]
  visual_signature: "A quiet circular control sits in the header like a catalog tool, visible but never competing with product media."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | concise product/benefit phrase, often English for campaign hero | "Enabling better living" |
| Supporting copy | direct product category or campaign explanation | "Experience our newest Bespoke appliances" |
| Primary CTA | one-word retail action | "Shop" |
| Category language | concrete product families | mobile, TV, appliances, IT |
| Tone | confident, polished, showroom-commercial | aspirational but not poetic |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Samsung Korea — copy into your root stylesheet */
:root {
  /* Fonts */
  --samsung-font-display: "Samsung Sharp Sans", "SamsungOneKorean", sans-serif;
  --samsung-font-body: "SamsungOneKorean", "Dotum", "Apple SD Gothic Neo", Arial, sans-serif;
  --samsung-font-weight-normal: 400;
  --samsung-font-weight-bold: 700;

  /* Core colors */
  --samsung-color-primary: #2189FF;
  --samsung-color-logo-blue: #1428A0;
  --samsung-bg-page: #FFFFFF;
  --samsung-bg-muted: #F7F7F7;
  --samsung-text: #000000;
  --samsung-text-soft: #212425;
  --samsung-text-muted: #707070;
  --samsung-border: #DDDDDD;
  --samsung-border-soft: #EBEBEB;

  /* Spacing */
  --samsung-space-header-x: 24px;
  --samsung-space-component-y: 60px;
  --samsung-space-wide-y: 100px;
  --samsung-space-card-gap: 40px;

  /* Radius */
  --samsung-radius-card: 10px;
  --samsung-radius-module: 16px;
  --samsung-radius-pill-sm: 20px;
  --samsung-radius-pill-lg: 30px;
  --samsung-radius-search: 40px;
}

body {
  margin: 0;
  background: var(--samsung-bg-page);
  color: var(--samsung-text);
  font-family: var(--samsung-font-body);
  font-weight: var(--samsung-font-weight-normal);
  letter-spacing: 0;
}

.samsung-display {
  font-family: var(--samsung-font-display);
  font-weight: var(--samsung-font-weight-bold);
  letter-spacing: 0;
}

.samsung-btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 50px;
  padding: 0 24px;
  border-radius: var(--samsung-radius-pill-lg);
  background: var(--samsung-text-soft);
  color: var(--samsung-bg-page);
  border: 1px solid var(--samsung-text-soft);
  font-weight: 700;
}

.samsung-product-tray {
  background: var(--samsung-bg-muted);
  border-radius: var(--samsung-radius-card);
  padding: 10px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Samsung Korea inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        samsung: {
          primary: '#2189FF',
          logo: '#1428A0',
          ink: '#000000',
          softInk: '#212425',
          surface: '#FFFFFF',
          muted: '#F7F7F7',
          line: '#DDDDDD',
          softLine: '#EBEBEB',
          mutedText: '#707070',
        },
      },
      fontFamily: {
        samsungDisplay: ['Samsung Sharp Sans', 'SamsungOneKorean', 'sans-serif'],
        samsungBody: ['SamsungOneKorean', 'Dotum', 'Apple SD Gothic Neo', 'Arial', 'sans-serif'],
      },
      borderRadius: {
        samsungCard: '10px',
        samsungModule: '16px',
        samsungPill: '30px',
        samsungSearch: '40px',
      },
      spacing: {
        samsungComponent: '60px',
        samsungWide: '100px',
        samsungVeryWide: '140px',
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
| Brand primary | `{colors.primary}` | #2189FF |
| Logo/corporate blue | `{colors.logo-blue}` | #1428A0 |
| Background | `{colors.surface}` | #FFFFFF |
| Muted surface | `{colors.surface-muted}` | #F7F7F7 |
| Text primary | `{colors.ink}` | #000000 |
| Text muted | `{colors.text-muted}` | #707070 |
| Border | `{colors.line}` | #DDDDDD |
| Dark CTA | `{colors.ink-soft}` | #212425 |

### Example Component Prompts

#### Hero Section

```text
Samsung Korea 스타일 히어로를 만들어줘.
- 전체 화면에 가까운 제품 사진/영상 배경을 사용하고 UI chrome은 최소화
- 텍스트: Samsung Sharp Sans 느낌, 54px, weight 700, tracking 0
- 본문: SamsungOneKorean 느낌, 24px 이하, 흰색 또는 검정색을 이미지 명도에 맞춰 사용
- CTA: 작은 outline 또는 black/white pill, radius 30px, height 40-50px
- #2189FF는 CTA 전체 배경으로 남발하지 말고 보조 interaction accent로만 사용
```

#### Product Card

```text
Samsung Korea 스타일 제품 카드를 만들어줘.
- 제품 이미지는 #F7F7F7 tray 위에 놓고 radius 10px, padding 10px
- 제품명/가격은 #000000, 설명은 #707070
- shadow는 거의 쓰지 말고 이미지와 gray tray로 깊이를 만든다
- CTA는 #212425 배경 + #FFFFFF 텍스트의 pill 형태
```

#### Navigation

```text
Samsung Korea 스타일 GNB를 만들어줘.
- max-width 1440px, padding 0 24px, display flex
- 로고 좌측, 카테고리 중앙, search/cart/account/menu utility 우측
- 기본 배경은 #FFFFFF, border는 #EBEBEB 또는 transparent
- search button은 36px, #F7F7F7, radius 40px, hover border rgba(0,0,0,0.2)
```

### Iteration Guide

- **색상 변경 시**: 제품 사진의 장면색과 UI token을 분리한다. UI 전체를 #2189FF로 칠하지 않는다.
- **폰트 변경 시**: display/body 역할을 분리한다. 한 폰트로 전부 밀면 Samsung 느낌이 약해진다.
- **여백 조정 시**: hero/product modules는 60px-140px, commerce metadata는 6px-24px로 대비를 유지한다.
- **새 컴포넌트 추가 시**: 10px card tray, 16px module, 20px/30px pill radius 중 하나를 선택한다.
- **다크 영역**: #313131 또는 hero photography 위 흰색 UI를 사용하되, full dark app theme으로 확장하지 않는다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use product photography or real product renderings as the main source of atmosphere.
- Keep the base UI neutral: #FFFFFF page chrome, #000000 text, #F7F7F7 trays, #DDDDDD separators.
- Use `Samsung Sharp Sans`-style bold display for campaign/product headlines.
- Use compact black/white pill CTAs with 20px-30px radius.
- Keep navigation dense and utility-aware: search, cart, account, menu are part of the brand surface.
- Let product cards feel like shelves: pale tray, product image, black price/title, muted description.
- Preserve desktop-first responsive behavior with many defensive small-screen adjustments.

### ❌ DON'T

- 배경을 `#F0F6FF` 같은 임의의 pale blue로 두지 말 것 — 기본 chrome은 `#FFFFFF` 또는 `#F7F7F7` 사용.
- 텍스트를 `#111827` 같은 Tailwind slate로 바꾸지 말 것 — Samsung CSS의 주 텍스트는 `#000000` / `#212425`.
- muted text를 `#6B7280`로 대체하지 말 것 — 실제 보조 텍스트 축은 `#707070`.
- border를 `#E5E7EB`로 일반화하지 말 것 — 관측 separator는 `#DDDDDD`, `#D9D9D9`, `#EBEBEB`.
- brand UI를 `#1428A0`로만 칠하지 말 것 — 홈페이지 interaction accent는 `#2189FF`, corporate blue는 보조 단서.
- CTA를 `#2189FF` solid button으로 남발하지 말 것 — primary commerce pill은 `#212425` / `#FFFFFF` polarity가 더 Samsung답다.
- 카드 배경을 `#FFFFFF` only로 평평하게 두지 말 것 — product tray에는 `#F7F7F7` 또는 `#F4F4F4` 사용.
- Hero를 CSS gradient로 대체하지 말 것 — 실제 정체성은 photographed product scene이다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No global blue wash** — Samsung's homepage does not turn the whole UI into brand blue.
- **No single-page SaaS hero formula** — not "headline + paragraph + two CTAs + feature cards"; products and categories lead.
- **No ornamental gradient token system** — hero color comes from imagery, not reusable CSS gradients.
- **No heavy chrome shadows** — elevation is rare; overlays and photography create depth.
- **No rounded card-with-left-accent AI pattern** — Samsung cards are product trays, not note app panels.
- **No generic Inter-only typography** — proprietary Samsung font roles are a core identity cue.
- **No pastel multi-accent palette** — chromatic UI color is restrained; neutrals dominate.
- **No playful hover motion** — transitions support navigation and state, never entertainment.
- **No uniform card radius everywhere** — 10px trays, 16px modules, 20px/30px pills, 40px search controls have separate jobs.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage capture** — this guide uses the existing `/sec/` homepage phase1 data and hero screenshot. Product detail pages, checkout, account, and support flows may expose additional states.
- **Hero content is time-sensitive** — captured hero shows Bespoke appliances and "Enabling better living"; Samsung campaign modules rotate, so photography/color atmosphere can change while the underlying UI chrome stays similar.
- **CSS bundle is broad** — extracted CSS includes legacy app, commerce, GNB, carousel, and component rules. Some selectors are not necessarily active above the fold on the captured homepage.
- **Token system is shallow** — only 25 resolved custom properties and 7 core aliases were observed. Many design decisions are class-rule based, so this is lv2 "system in use", not a clean token API.
- **Motion JS not fully analyzed** — CSS transitions and transform values are captured, but carousel timing, scroll-trigger logic, and dynamic GNB behavior were not executed in this pass.
- **Accessibility state coverage is partial** — focus and hidden input patterns are visible, but validation, loading, error, and checkout-specific states were not visited.
- **Color frequency can include inactive modules** — CSS frequency counts represent loaded bundles, not only currently visible DOM pixels. Customer/logo/promo colors were interpreted conservatively.
- **Mobile visual screenshot not inspected** — responsive CSS says desktop-first with hamburger collapse, but this document does not include a separate mobile screenshot measurement.
