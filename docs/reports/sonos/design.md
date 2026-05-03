---
schema_version: 3.2
slug: sonos
service_name: Sonos
site_url: https://www.sonos.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#000000"
primary_font: aktiv-grotesk
font_weight_normal: 400
token_prefix: sonos

bold_direction: Editorial Product
aesthetic_category: other
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high
archetype: editorial-product
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Production site exposes real color variables and Tailwind utility structure, but semantic alias coverage is thin."

colors:
  brand-black: "#000000"
  surface-white: "#FFFFFF"
  text-charcoal: "#2E2E2E"
  muted-gray: "#737373"
  hairline: "#E0E0E0"
  surface-soft: "#F4F4F4"
  promo-navy: "#1F355A"
  accent-red: "#DE8579"
  accent-gold: "#C59C6E"
typography:
  display: "aktiv-grotesk"
  body: "aktiv-grotesk"
  ladder:
    - { token: hero, size: "clamp(56px, 7.5vw, 96px)", weight: 700, tracking: "0" }
    - { token: h2, size: "clamp(36px, 4.8vw, 72px)", weight: 700, tracking: "0" }
    - { token: body, size: "16px", weight: 400, tracking: "0" }
    - { token: nav, size: "16px", weight: 400, tracking: "0" }
    - { token: eyebrow, size: "12px", weight: 700, tracking: "0.1em" }
  weights_used: [300, 400, 500, 600, 700]
  weights_absent: [800, 900]
components:
  button-primary-black: { bg: "{colors.brand-black}", fg: "{colors.surface-white}", radius: "9999px", padding: "14px 32px" }
  button-secondary-white: { bg: "{colors.surface-white}", fg: "{colors.brand-black}", radius: "9999px", padding: "14px 32px" }
  sticky-nav: { bg: "{colors.surface-white}", shadow: "inset 0 -1px 0 #E0E0E0", height: "64px" }
  promo-bar: { bg: "{colors.promo-navy}", fg: "{colors.surface-white}", height: "52px" }
---

# DESIGN.md — Sonos Designer Guidebook

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Sonos stages each speaker like a **gallery** artifact in a **showroom** with the walls painted out of the photograph. The 64px sticky nav is the white service counter at the **store** entrance: flat, retail-practical, easy to scan — a **showroom** reception desk that does not compete with what is displayed beyond it. Under it, the page drops into a full-bleed domestic scene where the speaker sits the way a featured object sits in a **gallery** vitrine: the room is dim, the product is present, and the copy floats in white display type as if attached to a **museum** label that has no frame.

The dominant palette is almost binary. `#FFFFFF` (`{colors.surface-white}`) carries retail clarity; `#000000` (`{colors.brand-black}`) carries authority; `#2E2E2E` (`{colors.text-charcoal}`) carries dense product copy. The few chromatic tokens — `#DE8579` (`{colors.accent-red}`) and `#C59C6E` (`{colors.accent-gold}`) — behave like finish samples on a speaker grille or campaign lighting in an **atelier**: they are not the interface's everyday voice. There is no second brand color. The **gallery** operates in monochrome, and the product photography is the only chroma allowed on the floor.

`aktiv-grotesk` carries both display and body, so Sonos relies on acoustic scale and scene composition rather than font contrast — a **showroom** decision, not an **atelier** one. The hero headline keeps a living-room confidence rather than luxury compression. The CTA pair is a black/white volume knob: one white pill for the named product, one black pill for the broader catalog. Commerce hierarchy happens through inversion, not color decoration. The **stage** is the product scene; the nav is just the door. Shadows are sparse; separation comes from photography, hairlines, and surface changes rather than elevation.

### Key Characteristics

- Full-bleed product/lifestyle photography or video owns the first viewport.
- Navigation is white, flat, and retail-practical, with a 64px sticky bar rhythm.
- Brand identity is mostly black/white; chromatic tokens exist but are not primary UI.
- Hero type is very large, centered, and white over darkened imagery.
- CTA buttons are high-contrast pills with black/white inversion.
- The page alternates cinematic hero moments with clean ecommerce product sections.
- Shadows are sparse; separation comes from photography, hairlines, and surface changes.
- `aktiv-grotesk` is the single voice across navigation, display, and body.
- Grid behavior is Tailwind-driven with 1, 2, 3, and 4-column product/content layouts.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Editorial Product
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **cinematic home-audio hero with black-white pill commerce**으로 기억된다.
> **Code Complexity**: medium — Tailwind utility scale, video/image hero treatment, responsive grids, and sparse interaction states.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Sonos처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "aktiv-grotesk", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; --muted: #737373; }
body { background: var(--bg); color: var(--fg); }

/* 3. Hero commerce contrast */
.hero {
  min-height: 80vh;
  color: #FFFFFF;
  background: #000000 center / cover no-repeat;
}
.button { border-radius: 9999px; padding: 14px 32px; font-weight: 700; }
```

**절대 하지 말아야 할 것 하나**: Sonos를 파란 SaaS UI나 컬러풀한 앱 대시보드처럼 만들지 말 것. 실제 UI의 핵심은 #000000 / #FFFFFF 대비와 제품 장면이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.sonos.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | reused phase1 artifacts from `insane-design/sonos/` |
| HTML size | 660074 bytes |
| CSS files | 1 external CSS file, 167196 chars |
| Token prefix | `sonos` |
| Method | Existing phase1 JSON + CSS frequency + screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: SSR ecommerce site with compiled utility CSS. The captured HTML contains multiple title fragments and rich rendered content, consistent with server-rendered commerce pages.
- **Design system**: Sonos custom variables plus Tailwind utilities. Color tokens use plain names such as `--color-black`, `--color-white`, `--color-greyLight`, and campaign/material names such as `--color-accentRed`.
- **CSS architecture**:
  ```text
  core        (--color-*)              raw brand, neutral, material, and campaign hex
  utility     (.tw-*, responsive)      Tailwind utility layout and state classes
  component   (--menu-*, --grid-*)     local sizing, grid, and menu component variables
  ```
- **Class naming**: Tailwind-like `tw-` utilities plus arbitrary variants, for example sticky nav and button shadow utilities.
- **Default theme**: mixed. Navigation and retail sections are light; hero and media moments use dark imagery with white text.
- **Font loading**: custom `aktiv-grotesk` with Helvetica/Arial fallback.
- **Canonical anchor**: black/white commerce shell plus cinematic home-audio imagery.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `aktiv-grotesk` (commercial/custom webfont)
- **Body font**: `aktiv-grotesk, Helvetica, Arial, sans-serif`
- **Code font**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace`
- **Weight normal / bold**: `400` / `700`
- **Observed weights**: `300`, `400`, `500`, `600`, `700`; variable declaration also exposes `100 900`.

```css
:root {
  --sonos-font-family: "aktiv-grotesk", "Helvetica", "Arial", sans-serif;
  --sonos-font-family-code: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --sonos-font-weight-normal: 400;
  --sonos-font-weight-bold: 700;
}
body {
  font-family: var(--sonos-font-family);
  font-weight: var(--sonos-font-weight-normal);
}
```

### Note on Font Substitutes

- **aktiv-grotesk** — If unavailable, use `Helvetica Neue` or `Arial` before `system-ui`. Do not substitute with Inter unless you also reduce the "startup SaaS" feel through stronger black/white contrast and larger hero type.
- **Display correction** — Keep hero text broad and uncompressed. Use `letter-spacing: 0`, not `-0.03em`, because the observed CSS only shows small positive `.2px` and uppercase `.1em` cases.
- **Weight correction** — Use `700` for large hero/headline moments, `400` for body and nav, and reserve `500/600` for mid-emphasis labels. Avoid making the whole page medium-weight.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Hero display | `clamp(56px, 7.5vw, 96px)` | `700` | `0.95-1.05` | `0` |
| Section display | `clamp(36px, 4.8vw, 72px)` | `700` | `1.0-1.1` | `0` |
| Product title | `24-32px` | `700` | `1.15` | `0` |
| Body | `16px` | `400` | `1.45-1.6` | `0` |
| Navigation | `16px` | `400` | `1` | `0` |
| Eyebrow / micro label | `12px` | `700` | `1` | `0.1em` |

> Key insight: Sonos does not need a second typeface. The contrast is scale + weight + photographic context.

### Principles

1. Display type is huge but not luxury-tight. Keep `letter-spacing: 0` for the main consumer headline.
2. The body voice is plain retail clarity: 16px, weight 400, generous enough line-height to sit under product claims.
3. Uppercase microcopy can use positive tracking (`0.1em`), but this is not the default for headings.
4. Use weight 700 for hero and decisive product names; do not create a 900-weight tech poster style.
5. Navigation should stay readable and unforced. It is a shopping shell, not a typographic statement.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (monochrome anchor)

| Token | Hex |
|---|---|
| `--color-black` / `--color-main` | `#000000` |
| `--color-grayDarkest` | `#2E2E2E` |
| `--color-greyDark` | `#333333` |
| `--color-greyMedium` | `#737373` |
| `--color-greyLight` | `#E0E0E0` |
| `--color-greyLighter` | `#F4F4F4` |
| `--color-white` / `--color-base` | `#FFFFFF` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--color-dgc-d1` | `#000000` |
| `--color-dgc-d2` | `#FFFFFF` |
| `--color-shadow-black` | `#454749` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| Page | `#FFFFFF` | `#000000` |
| Soft surface | `#F4F4F4` | `#2E2E2E` |
| Hairline | `#E0E0E0` | `#454749` |
| Muted text | `#737373` | `#BCBCBC` |
| Primary text | `#000000` | `#FFFFFF` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Red/coral | `--color-accentRed` | `#DE8579` |
| Gold/walnut | `--color-accentGold` | `#C59C6E` |
| Product green | `--color-greenDarkest` | `#1C5F4A` |
| Promo/navy | `--color-purpleDark` | `#1F355A` |
| Cobalt | `--color-cobaltDark` | `#1F30CA` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `surface-white` | `#FFFFFF` | nav, content sections, white CTA pill |
| `brand-black` | `#000000` | logo, primary text, black CTA pill |
| `text-charcoal` | `#2E2E2E` | dense copy and dark surfaces |
| `muted-gray` | `#737373` | secondary copy and understated metadata |
| `hairline` | `#E0E0E0` | sticky-nav separator and light borders |
| `promo-navy` | `#1F355A` | top promotional bar / dark notice surface |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--color-base` | `#FFFFFF` | base surface |
| `--color-main` | `#000000` | main foreground |
| `--color-soft-white` | `#EEEEEE` | soft off-white blocks |
| `--color-greyLighter` | `#F4F4F4` | subtle section background |
| `--tw-shadow-color` | `#E0E0E0` | nav/hairline shadow color |

### 06-7. Dominant Colors (actual CSS frequency order)

| Token | Hex | Frequency |
|---|---|---|
| white | `#FFFFFF` | 372 |
| black | `#000000` | 87 |
| dark charcoal | `#2E2E2E` | 71 |
| transparent black | `#00000000` | 52 |
| mid charcoal | `#4C4C4C` | 43 |
| overlay black | `#000000A0` | 34 |
| light gray | `#BCBCBC` | 32 |
| gray | `#424242` | 26 |
| muted gray | `#7F7F7F` | 26 |
| hairline gray | `#E0E0E0` | 17 |

### 06-8. Color Stories

**`{colors.surface-white}` (`#FFFFFF`)** — The retail floor. Sonos uses white for navigation and shopping clarity so lifestyle imagery can do the emotional work. It should feel clean, not sterile, because the page quickly pairs it with warm home photography.

**`{colors.brand-black}` (`#000000`)** — The brand anchor and commerce action. It appears in the wordmark, icons, text, and black CTA pill. There is no louder UI color competing with it.

**`{colors.text-charcoal}` (`#2E2E2E`)** — The dense copy alternative to pure black. Use it when a long product explanation needs slightly less glare while still reading premium and precise.

**`{colors.hairline}` (`#E0E0E0`)** — Structural quietness. It separates nav and panels without turning into card decoration. Do not make it a full gray theme; it is a boundary, not a mood.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--tw-xGrid-x0p5` | `26.666666666666668px` | half-grid offset |
| `--tw-xGrid-x1` | `53.333333333333336px` | small grid rhythm |
| `--tw-xGrid-x1p5` | `80px` | common vertical block air |
| `--tw-xGrid-x2` | `106.66666666666667px` | large section rhythm |
| `--tw-xGrid-x3` | `160px` | major editorial spacing |
| `--tw-xGrid-x6` | `320px` | wide composition offset |
| `--tw-xGrid-x12` | `640px` | split-panel / large grid measure |

**주요 alias**:
- `--tw-xGrid-x1` → `53.333333333333336px` (base grid unit)
- `--tw-xGrid-x1p5` → `80px` (editorial breathing unit)
- `--tw-xGrid-x2` → `106.66666666666667px` (major section gap)

### Whitespace Philosophy

Sonos spacing behaves like a product film cut into ecommerce modules. The hero gives the image almost all available space, then places copy and CTAs in a tight central stack. Below, content becomes more modular: product claims, cards, and commerce rows use Tailwind grid steps rather than ornamental containers.

The grid values are unusually fractional because the system appears to derive layout from a wide xGrid rather than a simple 4/8px token ladder. Preserve this feeling by using broad 53.333px/80px/106.666px rhythm for section composition, then use smaller conventional padding only inside buttons and compact product controls.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| pill | `9999px` / `200px` | primary and secondary CTA buttons |
| large media | `48px`, `50px`, `80px` | rounded product/media modules where used |
| card/module | `20px`, `30px`, `32px`, `36px`, `40px` | larger commerce surfaces |
| control | `8px`, `10px`, `15px`, `21px` | compact controls and small cards |
| micro | `3px`, `4px`, `6px` | small technical controls |
| none | `0` | flat nav and full-bleed media edges |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| nav hairline | `inset 0 -1px 0 #E0E0E0` | sticky navigation separation |
| product/control glow | `0 0 24px rgba(0,0,0,0.25)` | scoped button/media emphasis |
| default Tailwind shadow pipeline | `var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow)` | utility-composed shadows |
| absent surface elevation | `none` | most white chrome, text blocks, and hero overlay |

Pattern: shadow is not a main brand material. Sonos uses image contrast and black/white surfaces first; elevation appears only when a component needs tactile affordance.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| video hero | observed visually | first viewport uses motion/video-like domestic scene |
| hover fades | likely CSS utility transitions | nav links and CTAs should fade color/background, not bounce |
| media playback control | circular pause control | hero video control in bottom-right |

Motion rule: keep it cinematic, not playful. Use slow media, direct fades, and no decorative physics.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: observed values include `1280px`, `42rem`, `500px`, and xGrid values up to `640px` and beyond.
- **Grid type**: CSS Grid and Flexbox through Tailwind utilities.
- **Column count**: 1, 2, 3, and 4-column layouts are present; complex layouts include `3fr 2fr`, `2fr 1fr`, and `1fr 40%`.
- **Gutter**: driven by xGrid and Tailwind gap utilities; use 24-32px for card grids and 53.333px+ for editorial composition.

### Hero

- **Pattern Summary**: `80vh+ + dark full-bleed lifestyle media + centered huge H1 + dual pill CTA below`
- Layout: centered single-column text stack over full-bleed media.
- Background: lifestyle/product video or image, darkened enough for white text.
- **Background Treatment**: image/video overlay. Use black overlay or naturally dark frame; the page relies on legible white type over scene depth.
- H1: `clamp(56px, 7.5vw, 96px)` / weight `700` / tracking `0`
- Max-width: approximately `900-1000px` for headline block.

### Section Rhythm

```css
section {
  padding: 80px 24px;
  max-width: 1280px;
}
@media (min-width: 1024px) {
  section { padding-block: 106.66666666666667px; }
}
```

### Card Patterns

- **Card background**: `#FFFFFF` or media-driven surface; soft gray `#F4F4F4` for section alternation.
- **Card border**: sparse; use `1px solid #E0E0E0` only where structural separation is needed.
- **Card radius**: 20-40px for big modules; 8-10px for compact controls.
- **Card padding**: 24-40px inside product/content cards.
- **Card shadow**: generally none; if needed, very scoped utility shadow.

### Navigation Structure

- **Type**: horizontal retail nav with left wordmark, category links, and right account/search/cart icons.
- **Position**: sticky/static top shell depending scroll state.
- **Height**: promo bar `52px`, nav `64px`.
- **Background**: promo `#1F355A`, nav `#FFFFFF`.
- **Border**: bottom hairline/shadow `#E0E0E0`.

### Content Width

- **Prose max-width**: `42rem` for explanatory copy.
- **Container max-width**: `1280px` for major sections.
- **Sidebar width**: not a dominant homepage pattern; ecommerce drawers/menus are likely separate subflows.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `<640px` | single-column stacks, compact nav/menu behavior |
| Small | `640px` | first Tailwind `sm` breakpoint |
| Tablet | `768px` | two-column opportunities and larger media modules |
| Desktop | `1024px` | desktop nav/grid behavior |
| Wide | `1440px` | larger xGrid and editorial spacing |
| XL | `1536px` | very wide viewport refinements |

### Touch Targets

- **Minimum tap size**: target 44px+ for icon buttons and nav controls.
- **Button height (mobile)**: 48-58px for pill CTAs.
- **Input height (mobile)**: not directly observed on homepage; assume ecommerce standard 44px+.

### Collapsing Strategy

- **Navigation**: desktop horizontal category links collapse toward menu/search/cart icon flow on narrow screens.
- **Grid columns**: 4/3/2-column sections collapse to 1 column on mobile.
- **Sidebar**: not a homepage pattern; drawers likely overlay.
- **Hero layout**: remains centered over media; headline size clamps down, CTA buttons may stack or reduce padding.

### Image Behavior

- **Strategy**: full-bleed hero media plus responsive product/lifestyle assets.
- **Max-width**: `100%` and viewport-based media widths.
- **Aspect ratio handling**: hero uses cover/crop; product modules should preserve image focal point rather than letterbox.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary black pill**

| Property | Value |
|---|---|
| Background | `#000000` |
| Text | `#FFFFFF` |
| Radius | `9999px` |
| Padding | `14px 32px` |
| Weight | `700` |
| Border | `1px solid #000000` |
| Hover | subtle opacity or inverse emphasis, no color flourish |

```html
<a class="sonos-button sonos-button--black" href="#">Shop all</a>
```

**Secondary white pill**

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#000000` |
| Radius | `9999px` |
| Padding | `14px 32px` |
| Border | `1px solid #000000` or transparent over dark hero |
| Hover | slight gray tint or text underline only when needed |

```html
<a class="sonos-button sonos-button--white" href="#">Shop Sonos Play</a>
```

### Badges

Badges are not a primary homepage signature. If needed, keep them retail-functional:

| Property | Value |
|---|---|
| Font | `aktiv-grotesk`, 12px |
| Weight | `700` |
| Tracking | `0.1em` for uppercase |
| Background | `#F4F4F4` |
| Text | `#2E2E2E` |
| Radius | `9999px` |

### Cards & Containers

Product/content cards should stay clean and photography-led.

| Property | Value |
|---|---|
| Background | `#FFFFFF` or `#F4F4F4` |
| Border | optional `1px solid #E0E0E0` |
| Radius | `20px-40px` for editorial/product modules |
| Padding | `24px-40px` |
| Shadow | none by default |
| Hover | image scale/fade or link underline, not heavy elevation |

### Navigation

| Element | Spec |
|---|---|
| Promo bar | `52px`, `#1F355A`, centered white message, right "Shop now" link |
| Main nav | `64px`, `#FFFFFF`, black logo and icons |
| Links | 16px, weight 400, black; sale link can use muted/navy emphasis |
| Icons | account, search, basket; 24px optical size |
| Divider | bottom `#E0E0E0` hairline or inset shadow |

### Inputs & Forms

Homepage forms were not surfaced. For search/email forms, use:

| Property | Value |
|---|---|
| Height | `48px` minimum |
| Border | `1px solid #BCBCBC` |
| Focus | `2px solid #000000` or clear black outline |
| Radius | `8px-10px`, not pill unless search overlay uses a rounded capsule |
| Error | use `#D92F18` / `#B30911` tokens if validation appears |

### Hero Section

| Property | Value |
|---|---|
| Height | `80vh` to first-viewport-filling |
| Background | lifestyle/product media, cover crop |
| Overlay | black/scene darkness enough for white text |
| H1 | centered, white, huge, 2 lines acceptable |
| CTA stack | two pill buttons centered below H1 |
| Video control | small circular control at bottom-right |

### 13-2. Named Variants

- **button-primary-black** — black commerce pill for broad catalog action. Use `#000000` background, `#FFFFFF` text, and full pill radius.
- **button-secondary-white** — white hero pill for named product action. Use `#FFFFFF` background and `#000000` text.
- **sticky-nav** — 64px white retail nav with wordmark, category links, and icon cluster.
- **promo-bar** — 52px dark navy promotional strip with centered savings copy.
- **hero-video-control** — small circular pause/play control, white ring over media.

### 13-3. Signature Micro-Specs

```yaml
cinematic-media-legibility:
  description: "Hero media is selected or darkened so enormous white type remains readable without a visible caption panel."
  technique: "full-bleed cover media, dark frame/overlay using observed #000000A0 frequency, #FFFFFF display type, min-height around 80vh"
  applied_to: ["{component.hero-section}", "{component.hero-video-control}"]
  visual_signature: "a living-room product film paused on a legible frame, with the interface disappearing into the sound scene"

black-white-pill-commerce:
  description: "Commerce actions use direct black/white inversion instead of a colored brand ramp."
  technique: "border-radius: 9999px or 200px capsule, padding 14px 32px, min-height around 58px, #000000/#FFFFFF pair"
  applied_to: ["{component.button-primary-black}", "{component.button-secondary-white}"]
  visual_signature: "two pill controls read like hardware buttons: one white for the named product, one black for catalog action"

white-retail-shelf-over-cinema:
  description: "A practical white shopping shelf sits above a dark cinematic product scene."
  technique: "52px #1F355A promo bar, 64px #FFFFFF nav, inset 0 -1px 0 #E0E0E0 divider, black logo/icons"
  applied_to: ["{component.promo-bar}", "{component.sticky-nav}"]
  visual_signature: "retail chrome stays flat and quiet while the hero below carries the emotional volume"

xgrid-editorial-air:
  description: "Section spacing follows a wide fractional xGrid rather than a simple 8px utility ladder."
  technique: "layout measures include 53.333333px, 80px, 106.666667px, 160px, and 640px xGrid offsets"
  applied_to: ["{component.hero-section}", "{component.product-content-card}"]
  visual_signature: "broad editorial breathing room that still snaps to a measured commerce grid"

dual-radius-commerce-vs-media:
  description: "Two distinct radius languages run in parallel — pill capsules signal a commerce action while large 48–80px curves frame a media bay — so visual function is legible at a glance."
  technique: "commerce CTA: border-radius 9999px or 200px; media/product modules: border-radius 48px / 50px / 80px; large product cards: 30–40px; never blend the two (no 16–24px middle radius on either system)."
  applied_to: ["{component.button-primary-black}", "{component.button-secondary-white}", "media-frame", "product-content-card"]
  visual_signature: "buttons read as physical hardware capsules; surrounding panels read as soft, rounded film stages — the page never collapses to a single SaaS card-radius rhythm."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Plain product benefit, short and cinematic | "The whole-home sound system" |
| Primary CTA | Shopping action, concrete object or catalog | "Shop Sonos Play" |
| Secondary CTA | Broad browse action | "Shop all" |
| Subheading | Clear explanation of sound/product experience | "Rich stereo sound and deep bass in a go-anywhere design." |
| Tone | Confident consumer electronics, warmer than enterprise SaaS | "Hear how sound should sound" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Sonos — copy into your root stylesheet */
:root {
  /* Fonts */
  --sonos-font-family: "aktiv-grotesk", "Helvetica", "Arial", sans-serif;
  --sonos-font-family-code: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --sonos-font-weight-normal: 400;
  --sonos-font-weight-bold: 700;

  /* Brand / surfaces */
  --sonos-color-brand-25: #FFFFFF;
  --sonos-color-brand-300: #737373;
  --sonos-color-brand-500: #2E2E2E;
  --sonos-color-brand-600: #000000;
  --sonos-color-brand-900: #000000;

  --sonos-bg-page: #FFFFFF;
  --sonos-bg-soft: #F4F4F4;
  --sonos-bg-dark: #000000;
  --sonos-bg-promo: #1F355A;
  --sonos-text: #000000;
  --sonos-text-charcoal: #2E2E2E;
  --sonos-text-muted: #737373;
  --sonos-border: #E0E0E0;

  /* Spacing */
  --sonos-space-sm: 24px;
  --sonos-space-md: 53.333333px;
  --sonos-space-lg: 80px;
  --sonos-space-xl: 106.666667px;

  /* Radius */
  --sonos-radius-sm: 8px;
  --sonos-radius-md: 20px;
  --sonos-radius-lg: 40px;
  --sonos-radius-pill: 9999px;
}

body {
  font-family: var(--sonos-font-family);
  font-weight: var(--sonos-font-weight-normal);
  color: var(--sonos-text);
  background: var(--sonos-bg-page);
}

.sonos-hero {
  min-height: 80vh;
  display: grid;
  place-items: center;
  padding: 80px 24px;
  color: #FFFFFF;
  background: #000000 center / cover no-repeat;
  text-align: center;
}

.sonos-hero h1 {
  max-width: 980px;
  margin: 0;
  font-size: clamp(56px, 7.5vw, 96px);
  line-height: 1;
  font-weight: 700;
  letter-spacing: 0;
}

.sonos-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 58px;
  padding: 14px 32px;
  border-radius: var(--sonos-radius-pill);
  font-weight: 700;
  text-decoration: none;
}

.sonos-button--black {
  color: #FFFFFF;
  background: #000000;
}

.sonos-button--white {
  color: #000000;
  background: #FFFFFF;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Sonos-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        sonos: {
          black: '#000000',
          white: '#FFFFFF',
          charcoal: '#2E2E2E',
          muted: '#737373',
          hairline: '#E0E0E0',
          soft: '#F4F4F4',
          promo: '#1F355A',
          accentRed: '#DE8579',
          accentGold: '#C59C6E',
        },
      },
      fontFamily: {
        sans: ['aktiv-grotesk', 'Helvetica', 'Arial', 'sans-serif'],
      },
      spacing: {
        xgrid1: '53.333333px',
        xgrid15: '80px',
        xgrid2: '106.666667px',
        xgrid3: '160px',
      },
      borderRadius: {
        sonos: '20px',
        sonosLg: '40px',
        pill: '9999px',
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
| Brand primary | `{colors.brand-black}` | `#000000` |
| Background | `{colors.surface-white}` | `#FFFFFF` |
| Text primary | `{colors.brand-black}` | `#000000` |
| Text secondary | `{colors.text-charcoal}` | `#2E2E2E` |
| Text muted | `{colors.muted-gray}` | `#737373` |
| Border | `{colors.hairline}` | `#E0E0E0` |
| Promo surface | `{colors.promo-navy}` | `#1F355A` |

### Example Component Prompts

#### Hero Section

```text
Sonos 스타일 히어로 섹션을 만들어줘.
- 배경: 어두운 full-bleed 라이프스타일/제품 이미지 또는 영상
- H1: aktiv-grotesk, clamp(56px, 7.5vw, 96px), weight 700, tracking 0, color #FFFFFF
- CTA: 두 개의 pill button. 첫 번째 #FFFFFF/#000000, 두 번째 #000000/#FFFFFF
- nav: 위쪽은 #FFFFFF 64px retail nav, promo bar는 #1F355A
- 카드 장식보다 제품 장면과 큰 타이포 대비를 우선
```

#### Card Component

```text
Sonos 스타일 제품 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF 또는 #F4F4F4
- border: 필요할 때만 1px solid #E0E0E0
- radius: 20px-40px, 큰 제품 모듈은 넓게
- shadow: 기본 없음
- 제목: aktiv-grotesk, 24px, weight 700
- 본문: 16px, #2E2E2E, line-height 1.5
- hover: heavy shadow 대신 이미지 scale/fade 또는 link underline
```

#### Navigation

```text
Sonos 스타일 상단 네비게이션을 만들어줘.
- promo bar: 52px, background #1F355A, white text
- main nav: 64px, background #FFFFFF, bottom hairline #E0E0E0
- 왼쪽 SONOS wordmark, 중앙 category links, 오른쪽 account/search/cart icons
- 링크는 16px, weight 400, black
```

### Iteration Guide

- **색상 변경 시**: `#000000`, `#FFFFFF`, `#2E2E2E`, `#E0E0E0` 축을 유지한다.
- **폰트 변경 시**: `aktiv-grotesk`가 없으면 Helvetica/Arial 계열로 유지한다. Inter로 바꾸면 SaaS처럼 보일 위험이 있다.
- **여백 조정 시**: 큰 섹션은 53.333px/80px/106.666px 리듬을 우선한다.
- **버튼 추가 시**: pill + black/white inversion을 유지한다.
- **이미지 추가 시**: 제품 렌더보다 실제 생활 공간, 청취 상황, 어두운 장면 대비를 우선한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#FFFFFF` retail surfaces and `#000000` brand/action contrast as the default interface contract.
- Put large white display type over darkened full-bleed lifestyle media for hero moments.
- Keep CTAs pill-shaped with black/white inversion.
- Use `aktiv-grotesk` or a close Helvetica/Arial substitute across display and body.
- Let photography and product context provide warmth instead of adding random accent colors.
- Use hairline separation (`#E0E0E0`) for nav and structure instead of heavy cards.
- Preserve broad editorial spacing with xGrid-like measures around 53.333px, 80px, and 106.666px.

### ❌ DON'T

- 배경을 `#F8FAFC` 또는 cool SaaS gray로 두지 말 것 — 대신 retail surface `#FFFFFF` 사용.
- 본문 텍스트를 `#111827` Tailwind slate로 두지 말 것 — 대신 Sonos black/charcoal `#000000` 또는 `#2E2E2E` 사용.
- 브랜드 CTA를 `#2563EB`, `#0066FF`, `#1D4ED8` 같은 파란색으로 두지 말 것 — 대신 `#000000` / `#FFFFFF` pill inversion 사용.
- hero 텍스트를 `#000000`으로 두고 밝은 제품 배경 위에 올리지 말 것 — dark media 위 `#FFFFFF` 텍스트를 사용.
- nav hairline을 `#CBD5E1` 또는 높은 채도의 blue-gray로 두지 말 것 — 대신 `#E0E0E0` 사용.
- soft section 배경을 `#FAF7EF` 같은 beige editorial tone으로 고정하지 말 것 — 필요하면 Sonos neutral `#F4F4F4` 사용.
- body 전체에 `font-weight: 500`을 사용 금지 — 기본은 `400`, hero/display는 `700`.
- hero CTA를 8px radius rectangle로 만들지 말 것 — `9999px` pill 또는 200px급 capsule 사용.
- 모든 카드에 heavy `box-shadow`를 넣지 말 것 — Sonos는 대부분 shadow 없이 사진과 hairline으로 분리한다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second primary brand color: none. Chromatic tokens exist, but the commerce UI is black/white.
- Gradient-first identity: absent. Do not replace product photography with decorative gradients.
- SaaS purple/blue hero: never. Sonos is product/editorial retail, not developer-tool marketing.
- Dense dashboard chrome: absent. No sidebars, data tables, or complex app controls in the core page language.
- Heavy card elevation: mostly absent. Shadows do not define the layout.
- Tight luxury tracking: absent on hero. The large headline stays broad and readable.
- Rounded-rectangle generic buttons: avoid. CTA identity is the pill.
- Icon-heavy feature cards: not the signature. Use product scenes, product names, and direct benefits.
- Full rainbow palette: absent. Material/accent colors are occasional and contextual.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-biased capture** — Analysis reuses existing `insane-design/sonos/` phase1 artifacts and the captured first-page screenshot. Checkout, account, configurator, support, and search flows were not inspected.
- **Typography scale extraction gap** — `typography.json` reported families and weights but no concrete scale entries. H1 and section sizes are inferred from screenshot + CSS patterns rather than a complete selector-level type map.
- **Semantic token layer is thin** — `alias_layer.json` mostly found core `--color-*` variables and few semantic aliases. The guide therefore names practical aliases in frontmatter but marks them as derived usage labels, not official Sonos token names.
- **Motion not deeply instrumented** — The hero appears video/media-driven, but JavaScript timelines, scroll triggers, and easing curves were not measured.
- **Responsive behavior inferred from CSS breakpoints** — Breakpoints `640`, `768`, `1024`, `1440`, and `1536` were observed, but mobile screenshots were not captured in this pass.
- **Forms and validation states not surfaced** — Search, newsletter, account login, and checkout inputs were not opened, so focus/error/loading specs are conservative.
- **Accent color usage may be campaign-specific** — `#DE8579` and `#C59C6E` are real CSS variables, but the homepage UI does not use them as everyday brand actions.
- **Image asset focal rules not exhaustively mapped** — The hero screenshot confirms dark lifestyle media with centered copy, but all product category image crops were not reviewed.
