---
schema_version: 3.2
slug: dyson
service_name: Dyson
site_url: https://www.dyson.com
fetched_at: 2026-04-14T01:23:00+09:00
default_theme: mixed
brand_color: "#0F70F0"
primary_font: system-ui
font_weight_normal: 400
token_prefix: yxt

bold_direction: Industrial Retail
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: editorial-product
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "301 CSS variables, 273 resolved tokens, and 65 action/component aliases observed in the Yext-powered search/support layer plus consistent commerce components."

colors:
  brand-primary: "#0F70F0"
  brand-hover: "#0C5ECB"
  surface-base: "#FFFFFF"
  surface-black: "#000000"
  text-primary: "#212121"
  text-secondary: "#757575"
  border-default: "#DCDCDC"
  badge-promo: "#0066CC"
  badge-popular: "#FFCC00"
  alert-error: "#940000"

typography:
  display: "system-ui"
  body: "system-ui, Segoe UI, Roboto, Oxygen-Sans, Ubuntu, Cantarell, Helvetica Neue, sans-serif"
  ladder:
    - { token: xs, size: "0.625rem", weight: 400, line_height: 1 }
    - { token: sm, size: "0.75rem", weight: 400, line_height: 1.2 }
    - { token: md, size: "0.875rem", weight: 400, line_height: 1.4 }
    - { token: md-lg, size: "1rem", weight: 400, line_height: 1.5 }
    - { token: lg, size: "1.125rem", weight: 600, line_height: 1.5 }
    - { token: xlg, size: "1.25rem", weight: 600, line_height: 1.6666666667 }
    - { token: xxlg, size: "2.5rem", weight: 600, line_height: 1.7 }
  weights_used: [300, 400, 500, 600, 700]
  weights_absent: [800, 900]

components:
  button-green-hero: { bg: "observed hero CTA green", radius: "0", padding: "large rectangular block" }
  button-transactional: { bg: "{colors.surface-black}", radius: "0", padding: "commerce card CTA" }
  searchbar-form: { bg: "{colors.surface-base}", radius: "calc(var(--yxt-base-spacing) * 0.4)", shadow: "0 0 0.625rem rgba(0,0,0,.1) on focus" }
  nav-dark-mega: { bg: "{colors.surface-black}", text: "{colors.surface-base}", border: "1px dark divider" }
---

# DESIGN.md — Dyson

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Dyson.com is not a soft lifestyle shop. It behaves like a black technical showroom bolted onto a retail engine: the chrome is dark, the product photography is oversized, and the page lets machines, price, and proof do the persuasive work. The first viewport feels like entering a demo bay through a black equipment rack; the two-tier navigation is the rigging, and the full-width product-video hero is the machine being tested under lights.

The visual identity is built on a hard absence: no second brand color, no decorative gradient skin, no friendly SaaS softness. Black and white carry the store shell, product photography carries the emotion, and bright accents are kept in locked compartments. The most explicit named brand token is #0F70F0 (`{colors.brand-primary}`), but on the observed homepage it behaves like a service-desk blue for search/support/link systems, not the hero's main theatrical color. The homepage CTA is a green rectangular block, while retail markers split into #0066CC (`{colors.badge-promo}`), #FFCC00 (`{colors.badge-popular}`), and chroma that belongs to the product image itself.

The page has the strange confidence of an appliance lab where the walls disappear only when the product needs room. Hero photography is a pale test environment, almost a wet-floor demonstration chamber, while the black nav remains overhead like a suspended rail of instruments. Below the hero, the mood snaps from showroom to inventory tray: product cards line up like sealed parts in a service catalog, each one carrying badge, rating, price, saving, promotion, and CTA without pretending to be editorial.

Typography is deliberately normal. The detected stack is system-ui, Segoe UI, Roboto, Oxygen-Sans, Ubuntu, Cantarell, Helvetica Neue, sans-serif; Dyson's distinctiveness does not come from a boutique typeface. It comes from weight discipline and physical product context. The hero headline is large but not precious, closer to a label on a precision demo than a magazine title; the card copy becomes operational labeling, the way a showroom placard turns into a parts sheet once price enters the frame.

The strongest craft move is the collision between black infrastructure and pale photographic environments. Shadow is mostly not a chrome effect; depth belongs to photography, video, and the object bodies. Use radius and elevation lightly. Dyson's surfaces do not need softness because the machines already provide form, and the interface knows when to step aside.

### Key Characteristics

- Two-tier black global navigation with white links, utility links, search, account, and cart.
- Full-width hero image/video using real product action instead of abstract illustration.
- Rectangular CTA blocks; pill softness is not the dominant gesture.
- System font stack with utilitarian weights: 400 body, 500/600 controls, 700 only in isolated emphasis.
- Large white and black surfaces with chromatic accents constrained to CTAs, badges, prices, search/support UI, and product imagery.
- Commerce density appears immediately below the hero through product cards, prices, savings, badges, and "Shop now" actions.
- Search/support layer uses a formal `--yxt-*` token system with 301 custom properties and clear component aliases.
- Photography is the emotional layer; UI chrome stays mostly flat, high contrast, and functional.
- Motion is product/video-first; CSS interface animation is light and mostly opacity/focus-state related.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Industrial Retail
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **black technical showroom plus product-video hero**으로 기억된다.
> **Code Complexity**: high — large commerce HTML, rich content/video modules, mega navigation, carousel commerce cards, Yext search/support tokens, and third-party embedded messaging are all present.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Dyson처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: system-ui, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell,
    "Helvetica Neue", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #212121; --nav: #000000; }
body { background: var(--bg); color: var(--fg); }
.global-nav { background: var(--nav); color: #FFFFFF; }

/* 3. 시스템 브랜드 컬러 */
:root { --brand: #0F70F0; --brand-hover: #0C5ECB; }
```

**절대 하지 말아야 할 것 하나**: Dyson을 둥근 SaaS 랜딩처럼 만들지 말 것. 검정 장비형 내비게이션, 실제 제품 사진, 각진 CTA, 가격/혜택 정보 밀도가 핵심이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.dyson.com` |
| Fetched | 2026-04-14T01:23:00+09:00 |
| Extractor | reused phase1 assets from `insane-design/dyson/` |
| HTML size | 733,328 bytes |
| CSS files | 4 files: `_inline.css`, `answers.css`, `bootstrap.min.css`, `slick.min.css` |
| CSS total chars | 213,729+ bytes observed |
| Token prefix | `yxt` |
| Method | existing phase1 JSON + CSS/HTML/screenshot interpretation; report HTML render skipped by request |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Adobe/enterprise commerce page with rich-content modules, responsive image loaders, carousel recommendations, OneTrust cookie UI, Salesforce embedded messaging, and Yext Answers search/support CSS.
- **Design system**: Dyson retail shell + Yext Answers token layer — prefix `--yxt-*`.
- **CSS architecture**:
  ```text
  core        (--yxt-color-*, --yxt-font-*, --yxt-base-*)       raw values and primitives
  action      (--yxt-searchbar-*, --yxt-button-*)               interactive search/button aliases
  component   (--yxt-accordion-*, --yxt-direct-answer-*)        module-specific compositions
  embedded    (.rich-content, .global-nav, .trade-up-item)      commerce and hero page modules
  ```
- **Class naming**: BEM-like commerce classes (`rich-content__button`, `trade-up-item__price`, `reasons-to-buy__btn`) plus Yext component prefixes (`.yxt-SearchBar-*`).
- **Default theme**: mixed; navigation and some rich-content assets are #000000, main commerce surfaces and cards are #FFFFFF.
- **Font loading**: system stack; no custom display font detected in phase1 typography.
- **Canonical anchor**: observed homepage hero for Dyson PencilWash plus product carousel and "Buy from Dyson.com" reason tiles.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `system-ui` (platform native)
- **Code font**: `ui-monospace` fallback only; no branded code surface observed
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --yxt-font-family: system-ui, Segoe UI, Roboto, Oxygen-Sans, Ubuntu,
    Cantarell, Helvetica Neue, sans-serif;
  --yxt-font-weight-light: 300;
  --yxt-font-weight-normal: 400;
  --yxt-font-weight-medium: 500;
  --yxt-font-weight-semibold: 600;
  --yxt-font-weight-bold: 700;
}

body {
  font-family: var(--yxt-font-family);
  font-weight: var(--yxt-font-weight-normal);
}
```

### Note on Font Substitutes

Dyson's observed stack already uses open platform fonts. Use `system-ui` on Apple platforms and keep Segoe UI/Roboto in the fallback chain for Windows/Android parity. The substitute problem is not font licensing; it is weight discipline. Do not replace this with Inter-heavy SaaS typography unless the rest of the chrome is also rebuilt.

- **Display substitute**: `system-ui` at 400/500 for hero copy, 600 for navigation and compact control labels.
- **Body substitute**: `Segoe UI` or `Roboto` through the native stack; keep line-height around 1.4-1.5 in UI modules.
- **Correction**: avoid heavy 800/900 display weights. Product photography should carry drama, not blackletter-thick type.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `--yxt-font-size-xs` | 0.625rem | 400 | 1 | 0 |
| `--yxt-font-size-sm` | 0.75rem | 400/500 | 1.2 | 0 |
| `--yxt-font-size-md` | 0.875rem | 400/600 | 1.4 | 0 |
| `--yxt-font-size-md-lg` | 1rem | 400/600 | 1.5 | 0 |
| `--yxt-font-size-lg` | 1.125rem | 600 | 1.5 | 0 |
| `--yxt-font-size-xlg` | 1.25rem | 600 | 1.6666666667 | 0 |
| `--yxt-font-size-xxlg` | 2.5rem | 600 | 1.7 | 0 |
| Filter/apply button | 0.875rem | 600 | 1 | 0.03125rem |
| Hero headline observed | visually ~30px desktop | 400 | loose | 0 |

> ⚠️ Typography extraction found no full editorial scale from homepage CSS; the strongest formal ladder is the Yext search/support module. Hero and commerce text are inferred from HTML/screenshot observation.

### Principles

1. Dyson typography is functional before expressive. Use the native stack, then make the product image do the brand work.
2. Navigation and filters prefer 500/600 for operational clarity; body and hero supporting text stay closer to 400.
3. Weight 800/900 is absent from the observed system. Heavy display drama would fight the precision-product tone.
4. The `--yxt-*` ladder tops out at `2.5rem`; very large type should be used sparingly and only when paired with photographic product context.
5. Letter-spacing is mostly zero, with uppercase controls using small positive tracking (`0.03125rem`) rather than condensed fashion-brand spacing.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (2 steps)
<!-- yxt-color-brand-* -->

| Token | Hex |
|---|---|
| `--yxt-color-brand-primary` | `#0F70F0` |
| `--yxt-color-brand-hover` | `#0C5ECB` |
| `--yxt-color-brand-white` | `#FFFFFF` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light | Dark |
|---|---|---|
| page / card surface | `#FFFFFF` | `#000000` |
| background highlight | `#FAFAFA` | `#A8A8A8` |
| text primary | `#212121` | `#FFFFFF` |
| text secondary | `#757575` | `#C5CACE` |
| text neutral | `#616161` | `#333333` |
| border | `#DCDCDC` | `#696969` |
| legacy border | `#E9E9E9` | `#2E2E2E` |

### 06-4. Accent Families
<!-- SOURCE: auto+manual -->

| Family | Key step | Hex |
|---|---|---|
| search/link action | primary | `#0F70F0` |
| search/link hover | hover | `#0C5ECB` |
| promotion badge | blue | `#0066CC` |
| popular badge | yellow | `#FFCC00` |
| alert/error | deep red | `#940000` |
| SweetAlert info | sky | `#7CD1F9` |
| SweetAlert warning | amber | `#F8BB86` |

### 06-5. Semantic
<!-- SOURCE: auto -->

| Token | Hex | Usage |
|---|---|---|
| `--yxt-color-link-primary` | `#0F70F0` | links and active states |
| `--yxt-color-borders` | `#DCDCDC` | default borders |
| `--yxt-color-error` | `#940000` | error states |
| `--yxt-direct-answer-title-background-color` | `#0F70F0` | direct-answer header surface |
| `--yxt-searchbar-button-background-color-hover` | `#E9E9E9` | search button hover |
| `--yxt-nav-text-focus-background-color` | `#E9E9E9` | nav focus surface |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--yxt-searchbar-button-text-color-base` | `--yxt-color-text-primary` → `#212121` | search icon/text color |
| `--yxt-searchbar-form-outline-color-base` | `--yxt-color-borders` → `#DCDCDC` | search outline |
| `--yxt-nav-text-active-color` | `--yxt-color-brand-primary` → `#0F70F0` | active nav |
| `--yxt-nav-text-active-border` | `0.125rem solid #0F70F0` | active nav underline |
| `--yxt-border-hover` | `0.0625rem solid #0C5ECB` | hover border |
| `--yxt-direct-answer-title-color` | `#FFFFFF` | text on blue title blocks |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---:|---:|
| white / surface | `#FFFFFF` | 128 |
| black / shell | `#000000` | 36 |
| SVG/pattern contaminant | `#116600` | 33 |
| dark neutral | `#333333` | 24 |
| chromatic contaminant | `#EEAACC` | 20 |
| promotion/action blue | `#0066CC` | 14 |
| border neutral | `#D7D7D7` | 12 |
| legacy border | `#DADADA` | 12 |
| brand hover | `#0C5ECB` | 7 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.surface-black}` (`#000000`)** — The header is a black equipment bar, not a decorative dark section. Use it for navigation, utility chrome, and high-contrast product-store framing; do not spread it into soft cards.

**`{colors.surface-base}` (`#FFFFFF`)** — White is the commerce floor. Product cards, search fields, and reason tiles use white so photography, prices, and badges stay legible.

**`{colors.brand-primary}` (`#0F70F0`)** — The named brand/action blue belongs to the Yext/search/support layer and active/link states. It is not the visible hero CTA color in the captured homepage, so treat it as a system action token, not the whole Dyson mood.

**`{colors.text-primary}` (`#212121`)** — Primary text is near-black, not pure `#000000`, in the tokenized support layer. On the black global nav, text flips to `#FFFFFF`.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--yxt-base-spacing-sm` | `0.75rem` | compact gaps, citation spacing |
| `--yxt-base-spacing` | `1rem` | module default spacing |
| `--yxt-module-footer-height` | `1.5rem` | module footer rhythm |
| `--yxt-module-container-height` | `1.25rem` | compact module height |
| `--yxt-cards-min-width` | `13.125rem` | answer/support cards |
| `--yxt-container-desktop-base` | `25rem` | base desktop container |
| hero asset desktop | 1920 x 673 source crop | full-width photographic band |
| hero asset tablet | 1025 x 533 source crop | shallower responsive crop |
| hero asset mobile | 320 x 401 source crop | vertical crop preserving product/person |

**주요 alias**:
- `--yxt-base-spacing` → `1rem` (the primitive unit for the search/support module)
- `--yxt-searchbar-focus-shadow-height` → `0.625rem` (focus halo size)

### Whitespace Philosophy

Dyson alternates between showroom air and retail compression. The hero gives the product-video image most of the viewport width, while text and CTA sit over the photograph with enough left-side air to feel like a demo scene rather than a banner ad.

Immediately below, the product carousel compresses information: cards, prices, savings, badges, and CTAs appear in a tight horizontal sequence. The rule is "open demonstration, dense purchase path." Do not keep every section equally airy.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `--yxt-searchbar-form-border-radius` | `calc(var(--yxt-base-spacing) * 0.4)` → about 6.4px | search field shell |
| `.swal-button` | `5px` | SweetAlert actions |
| embedded messaging frame | `8px 8px 0 0` | Salesforce frame |
| minimized messaging button | `50%` | round floating chat launcher |
| hero CTA observed | `0` / rectangular | green shop block |
| product card image tiles observed | about 6-8px visually | carousel product cards |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| search focus | `0 0 0.625rem 0 rgba(0,0,0,.1)` | Yext search container focus/hover |
| Salesforce frame | `2px 2px 20px rgba(0,0,0,0.2)` | embedded messaging frame |
| promotion outline | `inset 0 0 0 1px #0066CC` | blue promotion badge outline |
| product chrome | none dominant | photography rather than UI elevation carries depth |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| search mic/listening icons | `opacity .2s ease-in-out` | search input micro states |
| SweetAlert success/error | `.5s` to `.75s` keyframes | modal feedback |
| rich content hero | inline video / fallback image | product demonstration hero |
| carousel | slick slider / horizontal cards | product recommendation strip |
| embedded chat hover | background-image swap | floating service launcher |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: hero asset is full-width; inner navigation uses container-style rows; support module exposes `--yxt-container-desktop-base: 25rem`.
- **Grid type**: enterprise mix of Bootstrap-like `container-fluid`, `row`, `col-xs-*`, flex search modules, carousel list items.
- **Column count**: product/reasons sections use 4-up desktop patterns (`col-xs-6 col-md-3` for reason tiles).
- **Gutter**: visual grid gaps around 24-32px in commerce cards; tokenized support layer uses 0.75rem/1rem primitives.

### Hero

- **Pattern Summary**: ~673px desktop image/video band + black two-tier nav + left text overlay + rectangular green CTA + centered play affordance.
- Layout: full-width image/video with text overlay on the left and product action photography spanning the viewport.
- Background: responsive image/video fallback for Dyson PencilWash product scene.
- **Background Treatment**: image/video; pale photographic environment with no decorative gradient mesh.
- H1: visually about 30px / weight `400` / tracking `0`.
- Max-width: image source up to 1920px desktop crop; page shell uses full viewport.

### Section Rhythm

```css
.dyson-section {
  padding: 40px 0;
  max-width: 100%;
}

.yxt-module {
  gap: var(--yxt-base-spacing);
}
```

### Card Patterns

- **Card background**: `#FFFFFF` product card surface, often on a light gray/white page.
- **Card border**: subtle neutral or none; promotion badge uses inset blue outline.
- **Card radius**: small, visually 6-8px on image/card tiles.
- **Card padding**: compact retail padding; enough for badge, image, reviews, price, promo message, CTA.
- **Card shadow**: minimal; product cutouts and photography provide object depth.

### Navigation Structure

- **Type**: two-tier horizontal global nav with mega-menu secondary panels.
- **Position**: captured as static/sticky-like top shell; black nav occupies the first 178px of screenshot.
- **Height**: top utility row about 50px, category/search row about 128px total.
- **Background**: `#000000`.
- **Border**: dark divider line between rows; white nav text.

### Content Width

- **Prose max-width**: hero text block approximately 520px on desktop.
- **Container max-width**: commerce modules vary; `container-fluid--upto-lg` appears in rich content.
- **Sidebar width**: none on homepage; mega menu columns use thirds.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `max-width: 767px` | hero switches to mobile crop; rich-content text can overlay on mobile |
| Tablet | `768px-1024px` | tablet crop and text/background handling |
| Desktop | `min-width: 1025px` | desktop hero crop, full nav, wide carousel |
| Support mobile | `max-width: 47.9375rem` | Yext search title margin adjustment |

### Touch Targets

- **Minimum tap size**: not fully measured; visible CTAs and nav buttons appear larger than 44px in the captured desktop layout.
- **Button height (mobile)**: not measured from screenshot; Yext/SweetAlert actions use 40px-ish controls.
- **Input height (mobile)**: search input appears about 34px desktop; mobile value not directly observed.

### Collapsing Strategy

- **Navigation**: hamburger/submenu button classes exist; desktop capture shows full horizontal nav.
- **Grid columns**: reason tiles use `col-xs-6 col-md-3`, implying 2-up mobile and 4-up desktop.
- **Sidebar**: no homepage sidebar.
- **Hero layout**: responsive image crops use mobile/tablet/desktop breakpoint-specific `cropPathE` values.

### Image Behavior

- **Strategy**: responsive image loader with preloaded breakpoint-specific JPGs.
- **Max-width**: full-width hero image, `height: auto`.
- **Aspect ratio handling**: distinct mobile/tablet/desktop crops instead of relying on a single object-fit rule.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Hero CTA `.button.rich-content__button.green`**

| Spec | Value |
|---|---|
| Shape | rectangular block, not pill |
| Background | observed green CTA; exact token not present in parsed CSS |
| Text | black |
| Padding | large touch target, visually about 28px x 24px |
| State | linked image/CTA analytics attributes; hover not measured |

```html
<a class="button rich-content__button green" href="/floor-cleaners/wet/pencilwash/copper">
  <span class="rich-content__button-text">Shop now</span>
</a>
```

**Transactional product CTA `.button--transactional`**

| Spec | Value |
|---|---|
| Context | product carousel/card purchase action |
| Shape | rectangular commerce button |
| Label | "Shop now" |
| State | add-to-basket/form button class observed |

### Badges

| Variant | Background | Text | Notes |
|---|---|---|---|
| promotion | `#0066CC` | `#FFFFFF` | deals/promotions badge |
| promotion outline | `#FFFFFF` | `#0066CC` | `box-shadow: inset 0 0 0 1px #0066CC` |
| popular/new | `#FFCC00` | `#000000` | "Best Seller", "Latest technology" style family |

### Cards & Containers

**Product carousel card**

| Spec | Value |
|---|---|
| Surface | `#FFFFFF` |
| Image | product photography on quiet neutral crop |
| Content | badge, product name, rating row, price, was price, savings, promo message, CTA |
| Density | high; designed for comparison and purchase, not editorial reading |
| Hover | not fully captured; carousel arrow uses circular dark affordance |

### Navigation

```html
<li class="global-nav__item primary-link__li js-drawer-item js-dropdown-item">
  <a class="nav__linkbtn" href="/vacuum-cleaners">Vacuums & floor cleaners</a>
</li>
```

| Spec | Value |
|---|---|
| Shell | `#000000` |
| Text | `#FFFFFF` |
| Structure | utility row + category row + mega-menu dropdowns |
| Search | white rectangular search field inside black nav |
| Icon system | account and cart icons in white |

### Inputs & Forms

**Search field / Yext searchbar**

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#212121` |
| Border | `#DCDCDC` |
| Radius | `calc(var(--yxt-base-spacing) * 0.4)` |
| Font size | `1rem` |
| Focus | `0 0 0.625rem rgba(0,0,0,.1)` shadow |

### Hero Section

| Spec | Value |
|---|---|
| Asset | Dyson PencilWash product action image/video |
| Text alignment | left overlay |
| Main headline | "For the things formerly known as chores" |
| Subcopy | "Hygienic cleaning, stain removal, quick drying - in our slimmest design." |
| Primary action | green rectangular "Shop now" |
| Secondary action | centered play button over video asset |

### 13-2. Named Variants

**button-green-hero**

| Spec | Value |
|---|---|
| Applied to | homepage hero purchase CTA |
| Visual role | high-contrast action against pale photographic hero |
| Radius | square/rectangular |
| Copy | "Shop now" |

**button-transactional-card**

| Spec | Value |
|---|---|
| Applied to | product cards and recommendation modules |
| Visual role | conversion action in dense retail context |
| Radius | low |
| State | add-to-basket / shop action |

**searchbar-nav-white**

| Spec | Value |
|---|---|
| Applied to | black global navigation |
| Background | `#FFFFFF` |
| Text | `#212121` |
| Focus | soft neutral shadow |

**badge-promotion-outline**

| Spec | Value |
|---|---|
| Applied to | promotion labels |
| Border | `inset 0 0 0 1px #0066CC` |
| Text | `#0066CC` |
| Background | `#FFFFFF` |

### 13-3. Signature Micro-Specs

```yaml
black-equipment-rack-nav:
  description: "Two-row black navigation acts like the page's technical chassis."
  technique: "#000000 full-width shell, #FFFFFF text/icons, dark row dividers, and a #FFFFFF search input embedded into the second navigation row."
  applied_to: ["{component.nav-dark-mega}", "global category links", "account/cart utility"]
  visual_signature: "The store feels engineered before it feels decorative, like product demos are being launched from a black control rack."

responsive-product-demo-crop:
  description: "Hero imagery uses viewport-specific product-action crops rather than one image stretched with cover."
  technique: "responsive cropPathE mobile/tablet/desktop image URLs; observed desktop source 1920 x 673, tablet 1025 x 533, mobile 320 x 401."
  applied_to: ["Dyson PencilWash homepage hero", "responsive image/video fallback"]
  visual_signature: "The product demonstration remains legible as the viewport changes, preserving the machine-in-use moment instead of generic banner cropping."

retail-density-card-stack:
  description: "Product cards compress comparison, proof, and purchase into one repeated commerce unit."
  technique: "#FFFFFF card surface with compact badge + image + rating slot + price + was-price + savings + promo message + rectangular CTA sequence."
  applied_to: ["product recommendation carousel", "{component.button-transactional}"]
  visual_signature: "The page snaps from open demo floor into a purchase matrix immediately below the hero."

yxt-tokenized-support-island:
  description: "The search/support layer is more formally tokenized than the bespoke hero chrome."
  technique: "--yxt-* variables define colors, font sizes, line heights, borders, radius, searchbar focus shadow 0 0 0.625rem rgba(0,0,0,.1), nav states, direct answers, and cards."
  applied_to: ["{component.searchbar-form}", "Yext direct answers", "support/search modules"]
  visual_signature: "Operational UI stays mechanically consistent while the retail and hero modules remain more photographic and bespoke."

dyson-green-single-action-signal:
  description: "Brand green is reserved for the one decisive product CTA inside an editorial hero, not spread across the chrome."
  technique: "background #008558 ({colors.dyson-green}); color #FFFFFF; rectangular pill with generous horizontal padding; sentence-case label; positioned low-left in the hero composition; never used for nav, badges, or surface fills."
  applied_to: ["{component.button-green-hero}", ".button.rich-content__button.green", "homepage hero command"]
  visual_signature: "A single green block lights up the dark/photographic hero like an engineered start switch — the rest of the page can be black, white, or photography, but the buy/learn moment is always the same green rectangle."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Reframe chores as engineered product moments | "For the things formerly known as chores" |
| Product naming | Product family + technical variant | "Dyson PencilWash", "Dyson Purifier Cool De-NOx PC2" |
| Primary CTA | direct purchase language | "Shop now" |
| Proof copy | benefit stack and guarantee language | "Price match promise", "Free shipping", "2 or 5 Year Limited Warranty" |
| Tone | confident, technical, commerce-ready | product specs and savings sit near lifestyle imagery |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Dyson — copy into your root stylesheet */
:root {
  /* Fonts */
  --dyson-font-family: system-ui, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu,
    Cantarell, "Helvetica Neue", sans-serif;
  --dyson-font-weight-normal: 400;
  --dyson-font-weight-medium: 500;
  --dyson-font-weight-semibold: 600;
  --dyson-font-weight-bold: 700;

  /* System action */
  --dyson-color-brand-500: #0F70F0;
  --dyson-color-brand-600: #0C5ECB;

  /* Surfaces */
  --dyson-bg-page: #FFFFFF;
  --dyson-bg-nav: #000000;
  --dyson-text: #212121;
  --dyson-text-muted: #757575;
  --dyson-border: #DCDCDC;

  /* Commerce accents */
  --dyson-promo-blue: #0066CC;
  --dyson-popular-yellow: #FFCC00;
  --dyson-error: #940000;

  /* Spacing */
  --dyson-space-sm: 0.75rem;
  --dyson-space-md: 1rem;
  --dyson-space-lg: 2rem;

  /* Radius */
  --dyson-radius-sm: 5px;
  --dyson-radius-md: 6.4px;
}

.dyson-nav {
  background: var(--dyson-bg-nav);
  color: #FFFFFF;
  font-family: var(--dyson-font-family);
}

.dyson-search {
  background: #FFFFFF;
  color: #212121;
  border: 1px solid #DCDCDC;
  border-radius: var(--dyson-radius-md);
}

.dyson-hero {
  min-height: 520px;
  background: #FFFFFF center / cover no-repeat;
}

.dyson-cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 64px;
  padding: 0 24px;
  border-radius: 0;
  font-weight: 600;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand/system primary | `{colors.brand-primary}` | `#0F70F0` |
| Brand/system hover | `{colors.brand-hover}` | `#0C5ECB` |
| Background | `{colors.surface-base}` | `#FFFFFF` |
| Navigation background | `{colors.surface-black}` | `#000000` |
| Text primary | `{colors.text-primary}` | `#212121` |
| Text muted | `{colors.text-secondary}` | `#757575` |
| Border | `{colors.border-default}` | `#DCDCDC` |
| Promo badge | `{colors.badge-promo}` | `#0066CC` |
| Popular badge | `{colors.badge-popular}` | `#FFCC00` |
| Error | `{colors.alert-error}` | `#940000` |

### Example Component Prompts

#### Hero Section

```text
Dyson 스타일 히어로 섹션을 만들어줘.
- 상단은 #000000 검정 2단 내비게이션, 흰색 링크, 우측 흰색 검색 필드
- 히어로는 실제 제품 사용 장면의 풀폭 사진/비디오 배경
- H1은 system-ui, 약 30-36px, weight 400, letter-spacing 0
- 서브텍스트는 #212121, 16px, line-height 1.5
- CTA는 pill이 아니라 각진 직사각형 블록, 높이 64px 안팎
- 제품 사진이 감정선을 맡고 UI 장식은 최소화
```

#### Card Component

```text
Dyson 스타일 제품 카드 컴포넌트를 만들어줘.
- 배경 #FFFFFF, radius 6-8px, shadow 거의 없음
- 상단은 제품 사진, 아래는 badge / product name / rating slot / price / was price / savings / promo message / CTA 순서
- promo badge는 #0066CC 또는 #FFFFFF + inset 1px #0066CC
- popular badge는 #FFCC00 배경 + #000000 텍스트
- CTA는 직사각형 transactional button으로 처리
```

#### Badge

```text
Dyson 스타일 배지를 만들어줘.
- 프로모션: #0066CC 배경, #FFFFFF 텍스트
- outline 프로모션: #FFFFFF 배경, #0066CC 텍스트, inset 0 0 0 1px #0066CC
- Best Seller / Latest technology 계열: #FFCC00 배경, #000000 텍스트
- radius는 과하게 둥글게 하지 말고 compact retail label로 유지
```

#### Navigation

```text
Dyson 스타일 상단 네비게이션을 만들어줘.
- 배경 #000000, 텍스트 #FFFFFF
- 1행: Dyson 로고 + utility links
- 2행: category links + white search input + cart icon
- 링크는 system-ui 14px 전후, weight 400/500
- 검색 필드는 #FFFFFF 배경, #212121 텍스트, border #DCDCDC, radius 약 6px
```

### Iteration Guide

- **색상 변경 시**: #0F70F0은 시스템 action/link 계열로 제한하고, nav shell은 #000000 유지.
- **폰트 변경 시**: custom display font를 억지로 넣지 말고 native stack의 기능성을 보존.
- **여백 조정 시**: hero는 넓고, 제품 카드 영역은 조밀하게. 모든 섹션을 같은 density로 만들지 않는다.
- **새 컴포넌트 추가 시**: radius와 shadow를 줄이고 제품/정보/가격의 위계를 먼저 정한다.
- **다크 모드**: 전체 다크모드가 아니라 black chrome + white commerce floor의 혼합 구조로 생각한다.
- **반응형**: hero 이미지는 단순 scale이 아니라 mobile/tablet/desktop crop 전략을 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- 검정 내비게이션은 `#000000`으로 강하게 유지하고, 링크는 `#FFFFFF`로 선명하게 둔다.
- 제품 사진/비디오를 첫 번째 감정 레이어로 사용한다. UI 장식이 아니라 기계의 형태가 브랜드를 만든다.
- 검색/support 계열 action에는 `#0F70F0`과 hover `#0C5ECB`를 사용한다.
- 제품 카드에는 가격, savings, badge, CTA를 압축적으로 넣어 retail density를 만든다.
- CTA는 둥근 SaaS pill보다 각진 retail block에 가깝게 설계한다.
- white commerce floor `#FFFFFF`와 near-black text `#212121`의 기능적 대비를 유지한다.
- responsive hero는 viewport별 crop을 설계한다. 단일 이미지를 무작정 cover로 늘리지 않는다.

### ❌ DON'T

- 내비게이션 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#000000` 사용.
- 본문/지원 모듈의 primary text를 `#000000` 또는 `black`으로 고정하지 말 것 — 대신 `#212121` 사용.
- Yext/search action blue를 `#0066CC`로 통일하지 말 것 — 기본 action은 `#0F70F0`, promotion badge는 `#0066CC`로 분리.
- hover action을 `#0F70F0` 그대로 두지 말 것 — hover에는 `#0C5ECB` 사용.
- card border를 `#CCCCCC` 같은 임의 회색으로 만들지 말 것 — 추출된 border는 `#DCDCDC` 또는 legacy `#E9E9E9`.
- popular badge를 `#0F70F0` 파랑으로 만들지 말 것 — observed popular/new badge family는 `#FFCC00` + `#000000`.
- Dyson을 pastel SaaS 배경 `#F7F7FF`나 purple gradient로 재해석하지 말 것 — 검정 shell + white floor + product photography가 원형이다.
- hero CTA를 모든 곳에서 pill `999px`로 만들지 말 것 — captured hero CTA는 각진 rectangular block이다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Decorative gradient system: absent. No brand-gradient background is needed for the homepage identity.
- Boutique display font: none detected. The site relies on system typography rather than a custom editorial face.
- Soft SaaS cards everywhere: absent. Product cards exist, but they are retail containers, not floating feature cards.
- Heavy UI shadow: minimal. Product photography supplies depth; chrome stays flat.
- Universal blue branding: false. `#0F70F0` exists as a system action token, while the visible hero CTA and retail badges use separate accent logic.
- Oversized rounded pills: not the dominant shape. CTA and commerce controls are more rectangular.
- Playful illustration layer: none. Real machines and real product scenes carry the visual story.
- Weight 800/900 display type: absent in the detected typography; keep weights below that range.
- Single-density page rhythm: absent. The page moves from open hero demonstration to dense product commerce.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage snapshot only** — the analysis reuses existing `insane-design/dyson/` phase1 assets and the captured homepage screenshot. Checkout, account, configurator, and support subflows were not visited.
- **Hero CTA green exact hex not extracted** — the screenshot clearly shows a green hero CTA, but the parsed CSS snippets did not expose a stable token for that color. It is described visually, not invented as a hex.
- **Yext token layer may overrepresent support/search UI** — the most structured token system is `--yxt-*`; it may not govern all bespoke Dyson commerce modules.
- **Logo/SVG color contamination present** — frequency candidates include likely SVG/pattern values such as `#116600` and `#EEAACC`; these were not treated as brand colors.
- **Mobile behavior inferred from markup/CSS breakpoints** — responsive image crops and `col-xs` classes were observed, but no fresh mobile screenshot was captured in this run.
- **Motion depth not fully measured** — video hero and carousel behavior are identified from HTML/classes, but JS timing, autoplay rules, and interaction curves were not profiled.
- **Exact nav stickiness not confirmed** — screenshot shows the header at top; CSS/JS scroll behavior was not interacted with.
- **Report HTML skipped by instruction** — Step 6 RENDER-HTML was intentionally not executed; this file is the requested design.md-only output.
