---
schema_version: 3.2
slug: adidas
service_name: adidas US
site_url: https://adidas.com
fetched_at: 2026-04-14T01:23:00+09:00
default_theme: light
brand_color: "#000000"
primary_font: AdihausDIN
font_weight_normal: 400
token_prefix: gl

bold_direction: Retail Monochrome
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: commerce-marketplace
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "8801 CSS variables, 5933 resolved tokens, and component-scoped button/card/navigation tokens show a system in use."

colors:
  primary: "#000000"
  surface: "#FFFFFF"
  surface-muted: "#ECEFF1"
  text-muted: "#767677"
  sale: "#E32B2B"
  campaign-yellow: "#FFD200"
  membership: "#408267"

typography:
  display: "adidasFG"
  body: "AdihausDIN"
  fallback: "Helvetica, Arial, sans-serif"
  ladder:
    - { token: campaign-display, size: "image-led oversized", weight: 700, tracking: "tight uppercase" }
    - { token: section-heading-mobile, size: "30px", weight: 700, tracking: "3px" }
    - { token: story-heading-desktop, size: "24px", weight: 700, tracking: "2.5px" }
    - { token: nav-label, size: "16px", weight: 700, tracking: "0px" }
    - { token: product-text, size: "12px-16px", weight: 400, tracking: "0px" }
  weights_used: [100, 400, 500, 700]
  weights_absent: [300, 600, 800, 900]

components:
  button-primary-onlight: { bg: "{colors.primary}", fg: "{colors.surface}", min_height: "48px", radius: "0", shadow_offset: "outerbox" }
  button-secondary-onlight: { bg: "{colors.surface}", fg: "{colors.primary}", border: "1px #000000", radius: "0" }
  membership-badge: { bg: "{colors.membership}", fg: "{colors.surface}", radius: "50%" }
  product-card: { bg: "{colors.surface}", gap: "2px-8px", radius: "0" }
---

# DESIGN.md - adidas US

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

adidas.com is not built around a soft lifestyle palette. It behaves like a retail shelf with a sports newspaper headline pasted over it: the permanent system is black, white, square, uppercase, and fast; the campaign layer brings the noise through photography. The screenshot hero is a three-panel image wall, with the yellow SPEZIAL campaign type sitting directly on the photo rather than inside a polite marketing card.

The site's strongest identity is the absence of a second UI brand color. The UI brand is #000000 (`{colors.primary}`), and #FFFFFF (`{colors.surface}`) does the other half of the work. #FFD200 appears as campaign ink inside the current hero artwork, not as the everyday CTA system. This is the main trap: treating the campaign yellow as the product interface color would make the site look like an ad remix, not adidas commerce. There is no permanent yellow button language, no soft blue helper brand, no decorative gradient safety net; the chrome is a black-and-white shop counter and the campaign has to earn every color it brings.

Typography is physical and compressed. The system alternates between AdihausDIN for functional retail text and adidasFG for hard uppercase display. Headings are not friendly SaaS headings; they are block labels, closer to shoe-box side labels and stadium wayfinding than editorial headlines. Letter spacing is often positive, such as 2px, 2.5px, or 3px on section/story headings, which makes the words feel stamped onto cardboard rather than typeset into a magazine spread.

The component language is almost anti-rounded. Buttons are rectangular, black or white, bordered, and often use the adidas offset-box shadow construction; the shadow is not atmosphere but a misregistered print plate, a second slab peeking from behind the CTA. Navigation is dense: shipping bar, utility links, logo, category links, search, account, wishlist, and bag all live in the first 120px. The header works like the front wall of a flagship store: sale sign, category aisle markers, checkout basket, and search desk all visible before the shopper has time to drift.

The hero does not behave like a web hero trying to explain itself. It is a wall of campaign posters sliced into panels, with the page stepping back so the product photography can become the architecture. The site has very little "site" self-consciousness: no floating glass card over the image, no rounded lifestyle module, no separate brand stage. Photography carries the spectacle; the reusable UI stays square, monochrome, and operational.

비유로 풀자면 adidas.com은 SaaS 진열대가 아니라 도시 한가운데의 운동화 마켓과 물류센터를 그대로 옮겨놓은 카탈로그다. 상단 검정 shipping bar는 창고 입구의 안내판이고, 카테고리 nav는 매장 내 통로 표지판이며, 검정 사각 CTA는 카운터 위에 찍힌 도장이다. 캠페인 yellow는 매대 위의 손글씨 가격표처럼 그 자리에서만 빛나고, 장바구니 카운터는 carbon-paper receipt처럼 단순하다. 페이지는 종이 카탈로그처럼 펼쳐지지만 실제로는 굴러가는 시장의 동선 그대로 — 진열대 폭, 매대 간격, 카운터 높이가 모두 운영 단위로 굳어 있다.

### Key Characteristics

- Black/white is the interface identity; campaign color is content-specific.
- Hero photography is full-bleed and grid-sliced, not placed inside decorative cards.
- The CTA is a square-edged block with a directional arrow, not a pill.
- Uppercase display labels and nav categories carry the adidas retail voice.
- Product and category grids use density after the hero breathes.
- Membership green #408267 is functional status color, not a general accent.
- Sale red #E32B2B is price semantics only.
- Radius is mostly zero; circular shapes are reserved for counters and icons.
- Shadows are rare and mechanical, often offset-box treatment rather than soft elevation.
- The search field is a utilitarian gray slab, not a rounded input.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Retail Monochrome
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **three-panel campaign photography over a black-white commerce chassis**으로 기억된다.
> **Code Complexity**: high — large token graph, component-scoped states, responsive retail navigation, and dense commerce variants.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 adidas US처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Font + weight */
body {
  font-family: "AdihausDIN", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  letter-spacing: 0;
}

/* 2. Interface colors */
:root {
  --adi-bg: #FFFFFF;
  --adi-fg: #000000;
  --adi-muted-surface: #ECEFF1;
  --adi-muted-text: #767677;
}

/* 3. CTA chassis */
.adi-cta {
  min-height: 48px;
  padding: 12px 16px;
  border: 1px solid #000000;
  border-radius: 0;
  background: #000000;
  color: #FFFFFF;
  font-weight: 700;
  text-transform: uppercase;
}
```

**절대 하지 말아야 할 것 하나**: #FFD200 campaign yellow를 primary UI color로 쓰지 말 것. adidas UI의 primary는 #000000이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://adidas.com` |
| Fetched | 2026-04-14 01:23 KST phase reuse |
| Extractor | existing `insane-design/adidas` phase1 reuse |
| HTML size | 1,420,592 bytes |
| CSS files | 6 files, about 1,347,190 CSS chars |
| Token prefix | `gl` plus component namespaces such as `button-*`, `card-*`, `banner-*` |
| Method | Existing phase JSON, CSS token sampling, HTML structure sample, and hero screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: commerce web app with server-rendered HTML payload and componentized CSS bundles.
- **Design system**: adidas Global / Stripes token system in use; CSS variables include `--gl-*`, `--button-*`, `--card-*`, `--banner*`, `--chipselection*`, and `--navigation*`.
- **CSS architecture**:
  ```text
  core        (--color-fill-*, --spacing-*, --sizing-*, --borderradius-*)        primitive values
  component   (--button-*, --card-*, --banner*, --navigation*)                 component contracts
  role/state  (*-onlight, *-ondark, *-hover, *-disabled, *-loading, *-active)   theme and state layer
  ```
- **Class naming**: bundled component classes such as `stripes_v7_gl-cta--primary`, plus hashed module classes for page sections.
- **Default theme**: light; first viewport uses #FFFFFF chrome and image-led hero.
- **Font loading**: CSS references branded font families including `AdihausDIN` and `adidasFG`, with `Helvetica, Arial, sans-serif` fallbacks.
- **Canonical anchor**: homepage retail header and SPEZIAL hero screenshot, not product detail or checkout flows.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `adidasFG` for campaign and section display labels.
- **Functional font**: `AdihausDIN` for nav, buttons, body retail text.
- **Fallback**: `Helvetica, Arial, sans-serif`.
- **Weight normal / bold**: `400` / `700`.

```css
:root {
  --adi-font-body: "AdihausDIN", "Helvetica", "Arial", sans-serif;
  --adi-font-display: "adidasFG", "AdihausDIN", "Helvetica", "Arial", sans-serif;
  --adi-font-weight-normal: 400;
  --adi-font-weight-bold: 700;
}

body {
  font-family: var(--adi-font-body);
  font-weight: var(--adi-font-weight-normal);
}

.campaign-heading,
.section-heading {
  font-family: var(--adi-font-display);
  font-weight: 700;
  text-transform: uppercase;
}
```

### Note on Font Substitutes

- **AdihausDIN** is the signature functional voice. If unavailable, use **DIN 2014**, **Barlow Condensed**, or **Arial Narrow** depending on license constraints; keep uppercase labels at 700 and avoid rounded geometric substitutes.
- **adidasFG** carries the stamped display feeling. A practical open substitute is **Oswald** at 700, with letter spacing increased to `2px-3px` for section headings. Do not use Inter as a direct replacement; it loses the compressed sports-retail edge.
- **Body fallback correction**: keep body text at 400 and line-height around `20px-24px`; compensating with weight 500 makes product metadata too heavy.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Campaign image headline | artwork-sized | 700 | tight | uppercase, visually tight |
| Section heading mobile | 30px | 700 | 32px | 3px |
| Story snippet heading mobile | 20px | 700 | 24px | 2px |
| Story snippet heading desktop | 24px | 700 | 28px | 2.5px |
| Navigation heading | 16px | 700 | 24px | 0px |
| Product/card text | 12px-16px | 400 | 20px-24px | 0px |
| Button label | functional token | 700 typical | about 22px | uppercase |

> ⚠️ adidas typography is not "large friendly retail." It is compressed, uppercase, and label-driven. The system uses positive tracking on many display labels, not negative display tracking.

### Principles

1. Display is uppercase first, size second. The stamped feeling comes from case, condensed forms, and letter spacing, not just font size.
2. Body retail text stays functional. Product metadata should remain 12px-16px and mostly weight 400 so the grid stays scannable.
3. 700 is the decisive voice for headings and CTA labels. 600 is not a visible middle tier in the captured system.
4. Letter spacing is positive on display labels: 2px, 2.5px, and 3px are part of the adidas look.
5. Navigation labels are heavy but compact: 16px, 700, 24px line-height, 0px tracking.
6. Campaign text can be embedded in imagery; do not force every hero word into live DOM typography.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (monochrome)

| Token | Hex | Usage |
|---|---|---|
| `{colors.primary}` | #000000 | primary CTA, nav text, borders, icon strokes, badges |
| `{colors.surface}` | #FFFFFF | page chrome, inverse CTA text, hero label blocks |
| `{colors.surface-muted}` | #ECEFF1 | muted bars, utility surfaces, alert/message backgrounds |
| `{colors.text-muted}` | #767677 | old price, secondary text |

### 06-2. Brand Dark Variant

| Token | Hex | Usage |
|---|---|---|
| `button-primary-ondark-bg` | #FFFFFF | dark-context primary action background |
| `button-primary-ondark-text` | #000000 | dark-context primary action label |
| `button-secondary-ondark-bg` | #000000 | dark-context secondary/action surface |
| `button-secondary-ondark-text` | #FFFFFF | dark-context secondary/action label |

### 06-3. Neutral Ramp

| Step | Light | Dark / Inverse |
|---|---|---|
| page | #FFFFFF | #000000 |
| hover / soft | rgb(245, 245, 245) | rgb(30, 30, 30) |
| secondary fill | #ECEFF1 | rgb(59, 59, 60) |
| disabled | rgb(217, 219, 221) | rgba(255, 255, 255, 0.3) |
| border hover | rgb(146, 147, 150) | rgb(146, 147, 150) |

### 06-4. Accent Families

| Family | Key step | Hex | Usage |
|---|---|---|---|
| Sale / error | sale text | #E32B2B | sale price and error semantics |
| Membership | adiClub status | #408267 | membership badge / innerbox |
| Campaign | SPEZIAL artwork | #FFD200 | current hero image typography, not UI chrome |
| Link / notification | blue notification | #0081C7 | notification and secondary signal |
| Focus | focus ring | #91C7ED | keyboard focus outline |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--color-fill-primary` | #000000 | primary fill |
| `--color-fill-primary-inverse` | #FFFFFF | inverse fill |
| `--color-fill-secondary` | #ECEFF1 | secondary surface |
| `--tagprice-sale-onlight-color-text-saleprice` | #E32B2B | sale price |
| `--tagprice-sale-onlight-color-text-oldprice` | #767677 | old price |
| `--badge-membership-onlight-color-background` | #408267 | membership badge |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--button-primary-onlight-color-background` | rgb(0, 0, 0) | primary CTA on light |
| `--button-primary-onlight-color-background-hover` | rgb(30, 30, 30) | primary CTA hover on light |
| `--button-primary-ondark-color-background` | rgb(255, 255, 255) | primary CTA on dark |
| `--button-secondary-onlight-color-background` | rgb(255, 255, 255) | secondary button on light |
| `--button-secondary-onlight-color-border` | rgb(0, 0, 0) | secondary button border |
| `--color-fill-page` | rgb(255, 255, 255) | page base |

### 06-7. Dominant Colors (actual CSS frequency)

| Token | Hex | Frequency signal |
|---|---|---|
| primary black | #000000 / #000 | highest, 600+ total black pattern hits in phase summary |
| surface white | #FFFFFF / #FFF | major neutral surface and inverse text |
| surface muted | #ECEFF1 | repeated secondary fill |
| focus blue | #91C7ED | repeated focus outline |
| muted text | #767677 | old-price and secondary text |
| sale red | #E32B2B | sale/error role |
| campaign yellow | #FFD200 | campaign artwork / visual asset color |

### 06-8. Color Stories

**`{colors.primary}` (#000000)** — The actual adidas interface brand color. It owns CTA backgrounds, borders, nav labels, bag/account icon logic, and badge counters. Use it with square geometry; softening it into charcoal reduces the retail punch.

**`{colors.surface}` (#FFFFFF)** — The commercial floor. It keeps navigation, product grids, and text blocks clean so campaign photography can carry saturation and texture.

**`{colors.surface-muted}` (#ECEFF1)** — Utility softness, not brand expression. It appears in secondary fills and alert/message surfaces when the system needs a slab behind content without introducing a color personality.

**`campaign-yellow` (#FFD200)** — A content color in the captured SPEZIAL hero. It is visually loud, but it belongs to the campaign artwork layer, not the reusable button or navigation system.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--spacing-none` | 0px | reset / dense retail layout |
| `--spacing-3xs` | 2px | micro gaps |
| `--spacing-2xs` | 4px | icon/card internals |
| `--spacing-xs` | 8px | common gap |
| `--spacing-s` | 16px | button leading/trailing, icon-text rhythm |
| `--spacing-m` | 24px | paragraph and section sub-gaps |
| `--spacing-l` | 32px | grid and larger module rhythm |
| `--spacing-xl` | 40px | vertical editorial breath |
| `--spacing-2xl` | 48px | section top/bottom in order-management tokens |
| `--spacing-3xl` | 64px | major vertical spacing |
| `--spacing-4xl` | 80px | large section spacing |

**Key aliases**:
- `--spacing-button-top` / `--spacing-button-bottom` -> 12px for CTA vertical padding.
- `--button-primary-label-onlight-spacing-leading-innerbox` -> 16px for button horizontal rhythm.
- `--recommendations-grid-item-card-desktop-spacing` -> `0 4px 8px 4px`, proving product cards are dense.

### Whitespace Philosophy

adidas uses a split rhythm: campaign bands can breathe, but shopping modules compress quickly. The hero is visually large because the image grid owns the viewport, yet the header above it is dense and operational. This tension is the site: wide campaign impact, then retail scanning.

The spacing scale is not decorative. Values such as 2px, 4px, 8px, 16px, 24px, 32px, 48px, 64px, and 80px form a practical commerce ladder. Product cards and recommendations lean into tiny gutters; editorial modules and heading sections step up to 40px-80px.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| default rectangular chrome | 0 | buttons, nav slabs, hero text label blocks |
| `--borderradius-0100` | 8px | limited controls / internal UI |
| `--borderradius-0125` | 12px | radio innerbox |
| `--borderradius-0150` | 16px | radio outerbox, progress stepper |
| circular | 50% | bag counter, icon counter, status bubbles |
| percentage full | 100% | circular media/control internals |

The public homepage impression is square. Rounded tokens exist in the system for form controls and status widgets, but the brand-facing retail surface avoids friendly pill softness.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: full-bleed hero at viewport width; common containers include 1232px, 1600px, 848px, and 580px in CSS samples.
- **Grid type**: CSS Grid and Flexbox mixed; phase layout recorded 366 grid/flex selector hits.
- **Column count**: hero acts as a 3-panel visual grid in the captured screenshot; product and recommendation grids collapse by breakpoint.
- **Gutter**: 2px-8px for product cards, 16px-24px for content modules, 40px+ for editorial section space.

### Hero

- **Pattern Summary**: `large viewport image wall + 3 editorial panels + overprinted campaign type + black square CTA`.
- Layout: full-width image grid, with live text block on lower-left panel and campaign lettering embedded in imagery.
- Background: photography as the dominant surface.
- **Background Treatment**: image-grid, no overlay card; high-contrast white label block sits directly over image.
- H1: campaign lettering is image-level oversized; live title block uses uppercase adidas display voice.
- Max-width: viewport-bound full bleed.

### Section Rhythm

```css
section {
  padding: 40px 0 64px;
  max-width: 1600px;
}
```

The exact values vary per module, but the captured system shows the larger rhythm living in `--spacing-xl`, `--spacing-3xl`, and container values up to 1600px.

### Card Patterns

- **Card background**: #FFFFFF for product cards; #ECEFF1 for some promotional/message surfaces.
- **Card border**: mostly none by default; hover states can use #000000 outer/inner border tokens.
- **Card radius**: 0 for commerce cards in the captured homepage language.
- **Card padding**: dense, with recommendation card spacing as low as `0 4px 8px 4px`.
- **Card shadow**: usually none; the system relies on image edges and grid spacing rather than elevation.

### Navigation Structure

- **Type**: multi-row retail navigation: shipping banner, utility links, main logo/category row, search, account, wishlist, bag.
- **Position**: top header chrome; captured screenshot shows static top at scroll origin.
- **Height**: about 120px total first-viewport chrome; individual interactive targets around 40px-48px.
- **Background**: #FFFFFF main nav, #000000 shipping bar.
- **Border**: minimal; black icon strokes and typography create structure.

### Content Width

- **Prose max-width**: short retail copy blocks, often under 580px.
- **Container max-width**: 1232px-1600px for grid modules.
- **Sidebar width**: no homepage sidebar observed; commerce subflows likely use overlay/drawer widths such as 351px, 600px, 760px, and 960px from sizing tokens.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

Primary on light:

```html
<a class="stripes_v7_gl-cta stripes_v7_gl-cta--primary stripes_v7_gl-cta--dropshadow">
  <span>SHOP NOW</span>
  <span aria-hidden="true">-></span>
</a>
```

| Property | Value |
|---|---|
| background | #000000 |
| text | #FFFFFF |
| min-height | 48px |
| border | 1px solid #000000 |
| radius | 0 |
| padding | 12px vertical, 16px leading/trailing |
| case | uppercase |
| hover | rgb(30, 30, 30) background or mechanical offset shift |
| disabled | rgb(217, 219, 221) background, rgba(0, 0, 0, 0.3) text/icon |

Secondary on light:

| Property | Value |
|---|---|
| background | #FFFFFF |
| text/icon | #000000 |
| border | 1px solid #000000 |
| hover background | rgb(245, 245, 245) |
| hover border | rgb(146, 147, 150) or #000000 depending component family |

### Badges

| Variant | Background | Text | Shape | Use |
|---|---|---|---|---|
| Badge main | #000000 | #FFFFFF | rectangular / compact | status label |
| Badge counter | #000000 | #FFFFFF | circular | bag count |
| Membership badge | #408267 | #FFFFFF | circular/status | adiClub/account state |
| Sale label | #FFFFFF surface | #E32B2B text | text only | sale price |

### Cards & Containers

Product cards should feel like commerce cells rather than editorial cards. Use image-first layout, zero radius, no default drop shadow, and small metadata text below. For hover, prefer border or image treatment instead of soft floating elevation.

```css
.adi-product-card {
  background: #FFFFFF;
  border-radius: 0;
  box-shadow: none;
  padding: 0 4px 8px;
}

.adi-product-card:hover {
  outline: 1px solid #000000;
}
```

### Navigation

Navigation has three distinct levels:

- Shipping banner: #000000 background, #FFFFFF uppercase message.
- Utility links: small text on #FFFFFF, right aligned.
- Main nav: logo, category links, search field, account, wishlist, bag.

Search is a rectangular gray utility field, not a rounded search capsule. Category labels are uppercase-ish retail labels with strong weight.

### Inputs & Forms

| Property | Value |
|---|---|
| search background | light gray utility slab, close to #ECEFF1 |
| text | #000000 |
| border | minimal / none until focus |
| focus | #91C7ED ring or outline in captured CSS |
| touch target | 44px-48px target sizes via sizing tokens |
| radius | 0 or near-square unless form-specific token overrides |

### Hero Section

The hero section is a campaign container, not a generic landing hero. Build it as a full-width grid of photography, with one live label block and one square CTA. Keep CTA anchored over the image, preserve the arrow, and allow campaign text to live inside the image asset when needed.

### 13-2. Named Variants

| Variant | Spec |
|---|---|
| `button-primary-onlight` | #000000 background, #FFFFFF text, 48px min-height, square edge, uppercase label |
| `button-primary-ondark` | #FFFFFF background, #000000 text, same square chassis |
| `button-secondary-onlight` | #FFFFFF background, #000000 border/text, rectangular |
| `button-secondary-ondark` | #000000 background, #FFFFFF border/text, rectangular |
| `button-membership-icon-onlight` | #408267 innerbox for adiClub/member affordance |
| `badgecounter-main-onlight` | #000000 circular counter with #FFFFFF text |
| `search-utility-slab` | light gray rectangular input with black search icon |
| `hero-campaign-cta` | white label block plus black outlined/offset CTA over photography |

### 13-3. Signature Micro-Specs

```yaml
offset-box-cta-shadow:
  description: "Square retail CTAs get a mechanical offset edge instead of soft elevation."
  technique: "border-radius: 0; min-height: 48px; border: 1px solid #000000; component token references --button-main-onlight-spacing-all-offset-outerbox"
  applied_to: ["{component.button-primary-onlight}", "{component.hero-campaign-cta}"]
  visual_signature: "A stamped black/white button with a print-plate slab peeking behind it, not a floating SaaS shadow."

positive-tracked-display-labels:
  description: "Uppercase display text is spaced like athletic signage and shoe-box labeling."
  technique: "font-family: adidasFG; font-weight: 700; text-transform: uppercase; letter-spacing: 2px, 2.5px, or 3px"
  applied_to: ["{typography.ladder.section-heading-mobile}", "{typography.ladder.story-heading-desktop}"]
  visual_signature: "Words look stamped onto the retail surface, with opened-up DIN-like spacing rather than optical tightening."

campaign-as-image-type:
  description: "Campaign typography can live inside photography instead of becoming reusable DOM headline style."
  technique: "three-panel full-bleed image grid; #FFD200 campaign lettering embedded in hero artwork; live UI remains #000000/#FFFFFF"
  applied_to: ["{component.hero-campaign-cta}"]
  visual_signature: "The SPEZIAL yellow reads as poster ink inside the image wall, while the commerce controls stay monochrome."

monochrome-state-inversion:
  description: "Button states invert strictly by light/dark context rather than introducing a second brand accent."
  technique: "onlight primary bg #000000 text #FFFFFF; ondark primary bg #FFFFFF text #000000; secondary variants keep 1px #000000/#FFFFFF borders"
  applied_to: ["{component.button-primary-onlight}", "{component.button-primary-ondark}", "{component.button-secondary-onlight}", "{component.button-secondary-ondark}"]
  visual_signature: "A black-white checkout-counter system: no permanent yellow CTA, no blue utility accent, no tinted button family."

dense-header-commerce-stack:
  description: "The first viewport compresses every retail job into a multi-row operational header."
  technique: "about 120px total header chrome; 40px-48px interactive targets; #000000 shipping bar over #FFFFFF utility/main nav; rectangular #ECEFF1 search slab"
  applied_to: ["{component.search-utility-slab}", "{component.badgecounter-main-onlight}"]
  visual_signature: "A flagship-store front wall: shipping notice, aisle markers, search desk, account, wishlist, and bag all visible at once."
```

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* adidas US - copy into your root stylesheet */
:root {
  /* Fonts */
  --adi-font-body: "AdihausDIN", "Helvetica", "Arial", sans-serif;
  --adi-font-display: "adidasFG", "AdihausDIN", "Helvetica", "Arial", sans-serif;
  --adi-font-weight-normal: 400;
  --adi-font-weight-bold: 700;

  /* Core colors */
  --adi-color-primary: #000000;
  --adi-color-surface: #FFFFFF;
  --adi-color-surface-muted: #ECEFF1;
  --adi-color-text-muted: #767677;
  --adi-color-sale: #E32B2B;
  --adi-color-campaign-yellow: #FFD200;
  --adi-color-membership: #408267;

  /* Spacing */
  --adi-space-2xs: 4px;
  --adi-space-xs: 8px;
  --adi-space-s: 16px;
  --adi-space-m: 24px;
  --adi-space-l: 32px;
  --adi-space-xl: 40px;
  --adi-space-3xl: 64px;

  /* Radius */
  --adi-radius-none: 0;
  --adi-radius-control: 8px;
  --adi-radius-circle: 50%;
}

.adi-button-primary {
  min-height: 48px;
  min-width: 80px;
  padding: 12px 16px;
  border: 1px solid var(--adi-color-primary);
  border-radius: var(--adi-radius-none);
  background: var(--adi-color-primary);
  color: var(--adi-color-surface);
  font-family: var(--adi-font-body);
  font-weight: 700;
  text-transform: uppercase;
}

.adi-button-primary:hover {
  background: rgb(30, 30, 30);
}

.adi-button-secondary {
  min-height: 48px;
  padding: 12px 16px;
  border: 1px solid var(--adi-color-primary);
  border-radius: 0;
  background: var(--adi-color-surface);
  color: var(--adi-color-primary);
  font-weight: 700;
  text-transform: uppercase;
}

.adi-section-heading {
  font-family: var(--adi-font-display);
  font-size: 30px;
  line-height: 32px;
  font-weight: 700;
  letter-spacing: 3px;
  text-transform: uppercase;
}

.adi-product-grid {
  display: grid;
  gap: 8px;
}

.adi-product-card {
  background: #FFFFFF;
  border-radius: 0;
  box-shadow: none;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `{colors.primary}` | #000000 |
| Background | `{colors.surface}` | #FFFFFF |
| Muted surface | `{colors.surface-muted}` | #ECEFF1 |
| Text muted | `{colors.text-muted}` | #767677 |
| Sale / error | `{colors.sale}` | #E32B2B |
| Membership | `{colors.membership}` | #408267 |
| Campaign yellow | `campaign-yellow` | #FFD200 |

### Example Component Prompts

#### Hero Section

```text
Create an adidas.com-style commerce hero.
- Use a full-width three-panel photography grid.
- Keep UI chrome monochrome: #000000 and #FFFFFF.
- Add one white label block with uppercase adidasFG-style heading.
- CTA: square black button, #FFFFFF label, 48px min-height, uppercase, arrow at the right.
- Do not use rounded cards or gradient backgrounds.
```

#### Product Card

```text
Create an adidas product-grid card.
- Background #FFFFFF, radius 0, no soft shadow.
- Image first, product text below at 12px-16px, weight 400.
- Sale price uses #E32B2B; old price uses #767677.
- Hover may add a #000000 outline, not floating elevation.
```

#### Badge

```text
Create adidas-style badges.
- Main badge: #000000 background, #FFFFFF text.
- Membership badge/counter: #408267 background, #FFFFFF text, circular if it is a count/status marker.
- Do not use campaign yellow for system badges.
```

#### Navigation

```text
Create the adidas retail header.
- Top shipping bar: #000000 background, #FFFFFF uppercase text.
- Main nav: #FFFFFF background, black logo/category links.
- Search field: rectangular muted slab near #ECEFF1 with black icon.
- Include account, wishlist, and bag icons; keep target sizes around 44px-48px.
```

### Iteration Guide

- **Color changes**: preserve #000000 / #FFFFFF as the interface spine. Add campaign color only inside imagery or temporary campaign modules.
- **Font changes**: if branded fonts are unavailable, use condensed DIN-like replacements and keep display labels uppercase with positive tracking.
- **Spacing changes**: product grids can be tight; hero/editorial modules need 40px-80px vertical breath.
- **Component changes**: keep buttons rectangular. A pill button will immediately break the adidas retail chassis.
- **State changes**: model onlight/ondark inversion explicitly; do not tint black buttons with arbitrary accent colors.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #000000 and #FFFFFF as the main UI system.
- Treat #FFD200 as campaign artwork color unless the page-specific campaign proves otherwise.
- Keep primary CTAs square, uppercase, and at least 48px high.
- Use product photography as the saturated visual layer.
- Let product grids become dense after the hero.
- Use #E32B2B only for sale/error semantics.
- Use #408267 only for membership/adiClub style signals.
- Preserve positive tracking on display labels.

### ❌ DON'T

- 배경을 `#ECEFF1` 같은 utility gray로 전체 page에 깔지 말 것 — 대신 primary commerce chrome은 `#FFFFFF` 사용.
- 텍스트를 `#767677` 같은 muted text로 primary UI에 쓰지 말 것 — 대신 key UI text and borders use `#000000`.
- Primary CTA를 `#FFD200`으로 두지 말 것 — 대신 reusable CTA background는 `#000000` 사용.
- Sale price를 `#E9A6A6` 같은 pale error tint로 두지 말 것 — 대신 sale/error role은 `#E32B2B` 사용.
- Muted text를 `#A0A0A0` 같은 generic gray로 두지 말 것 — 대신 old-price/secondary text는 `#767677` 사용.
- Membership badge를 blue signal `#0066FF`로 두지 말 것 — 대신 membership surface는 `#408267` 사용.
- CTA에 `border-radius: 999px` 사용 금지 — adidas primary retail CTA는 `border-radius: 0`에 가깝다.
- Product card에 soft elevation `box-shadow: 0 12px 30px rgba(...)` 사용 금지 — captured card language is flat/image-led.
- Body 전체를 `font-weight: 500` 이상으로 밀지 말 것 — product metadata must remain scannable at 400.
- Campaign hero를 centered SaaS text block으로 만들지 말 것 — image grid and over-photo label/CTA are the captured pattern.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second permanent brand color: **absent** — interface needs zero blue/yellow/red companion to #000000 / #FFFFFF.
- Soft SaaS gradient background: **none** — campaign energy comes from photography, never from page-wide gradient mesh.
- Pill-first CTA system: **absent** — rounded softness is reserved for counters; primary commerce CTA radius is zero.
- Decorative card chrome around hero photography: **zero** — image panels are the frame; floating glass cards are never used.
- Heavy product-card shadows: **zero** — flat product cells and image edges do the structural work.
- Friendly lowercase button voice: **never** — CTA labels are uppercase retail commands.
- Universal high-radius system: **absent** — radius tokens exist, but public commerce chrome stays square.
- Arbitrary rainbow accents: **never** — sale/membership/focus/campaign colors each have narrow roles.
- Relaxed magazine typography for nav: **absent** — category labels are compact, bold, operational.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-focused evidence** — The analysis reused existing homepage phase assets and the captured first viewport. Product detail, checkout, account, and returns subflows may expose additional component states.
- **Campaign-specific hero** — The SPEZIAL screenshot contains #FFD200 artwork. This is treated as campaign color, not global UI color, because reusable button/nav tokens are monochrome.
- **Font resolution limit** — CSS references branded font families and tokenized font sets, but exact downloadable font-face declarations were not confirmed in the sampled CSS output.
- **Motion not exhaustively traced** — CSS transition values were sampled, including `.3s cubic-bezier(.3,0,0,1)` and opacity/transform transitions, but JavaScript-driven carousel or menu motion was not executed.
- **Responsive behavior inferred from CSS and screenshot** — Breakpoints such as 389px, 479px, 767px, 959px, 960px, 1024px, 1366px, 1440px, and 1920px were observed in CSS, but mobile screenshots were not captured in this run.
- **Logo/artwork color contamination** — Hex frequency includes SVG/image/campaign values. #FFD200 is explicitly kept out of UI primary despite being prominent in the screenshot.
- **Form validation states not surfaced** — Input error/loading/success states are represented by tokens, but live validation surfaces were not visited.
- **Exact live H1 CSS unavailable** — The dominant hero "SPEZIAL" lettering appears to be in image artwork, so the guide preserves it as campaign-image typography rather than inventing a DOM H1 token.
