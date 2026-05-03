---
schema_version: 3.2
slug: nike
service_name: Nike
site_url: https://nike.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: light
brand_color: "#111111"
primary_font: "Helvetica Now Text"
font_weight_normal: 400
token_prefix: podium-cds

bold_direction: Athletic Editorial
aesthetic_category: editorial-product
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: editorial-product
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Podium CDS token namespace is present in production CSS, with typography, color, button, motion, radius, and breakpoint variables in use."

colors:
  ink: "#111111"
  surface: "#FFFFFF"
  muted-text: "#707072"
  focus: "#1151FF"
  cool-slate: "#73859F"
  volt: "#D5FF44"
  orange-action: "#FF5000"
  error: "#EE0005"
typography:
  display: "Nike Futura ND"
  title: "Helvetica Now Display Medium"
  body: "Helvetica Now Text"
  editorial: "Palatino LT Pro Light"
  ladder:
    - { token: "oversize1-1920", size: "11.625rem", weight: 500, line_height: "1", tracking: "0" }
    - { token: "display1-1920", size: "7.5rem", weight: 500, line_height: ".9", tracking: "0" }
    - { token: "title1-1920", size: "3rem", weight: 500, line_height: "1.2", tracking: "0" }
    - { token: "body1", size: "1rem", weight: 400, line_height: "1.5", tracking: "0" }
    - { token: "body2", size: ".875rem", weight: 400, line_height: "1.5", tracking: "0" }
  weights_used: [300, 400, 500, 700]
  weights_absent: [600, 800, 900]
components:
  button-primary: { bg: "{colors.ink}", fg: "{colors.surface}", radius: "999px", padding: "var(--podium-cds-button-padding-top-l) var(--podium-cds-button-padding-sides-l)" }
  button-secondary: { bg: "{colors.surface}", fg: "{colors.ink}", radius: "999px", border: "1px solid transparent" }
  nav-link: { font: "{typography.body}", size: "16px", weight: 500, color: "{colors.ink}" }
  focus-ring: { color: "{colors.focus}", shadow: "0 0 0 2px #1151FF" }
---

# DESIGN.md — Nike

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Nike.com is not a chromatic brand site. It behaves like a stadium tunnel opened into a retail floor: white concrete, black signage, product photography, and a few utility colors that only appear when the system needs state or feedback. The most important color decision is almost anti-color: #111111 (`{colors.ink}`) and #FFFFFF (`{colors.surface}`) carry the brand experience before any campaign palette enters. There is no second brand color holding the page together; the swoosh does not need one.

The typography is the site's strongest design system signal. Nike does not rely on generic geometric display type. It keeps a sharp split between Nike Futura ND for compressed athletic display, Helvetica Now Display Medium for large commercial titles, Helvetica Now Text for the shopping surface, and Palatino LT Pro Light for occasional editorial conversation. The effect is closer to a race bib pinned over a magazine cover than a normal ecommerce header: the display face arrives tight, vertical, and athletic, while the product UI underneath stays plain enough to scan at speed.

The layout behaves like a store with magazine instincts. Navigation is practical and dense, but hero and campaign zones are allowed to become full-width visual moments. Product chrome mostly disappears the way track markings disappear once the race starts: buttons are black capsules, dividers are hairlines, and shadow belongs to photography rather than panels. The page is not trying to look like a dashboard; it is trying to clear a lane for shoes, athletes, drops, and campaign copy.

The signature metaphor is a training facility turned into an editorial wall. Everything is clean enough to make products legible, but the headline system still lands with athlete-poster force. At its best, Nike.com feels like a locker-room wall where the motivational poster, the product rack, and the checkout button have been made from the same black-and-white kit: #111111 (`{colors.ink}`), #FFFFFF (`{colors.surface}`), pill CTAs, and display type that hits before it explains.

### Key Characteristics

- Production namespace is `--podium-cds-*`, with 351 custom properties and 284 resolved tokens in the phase1 sample.
- Dominant UI palette is black/white, specifically #111111 and #FFFFFF rather than pure browser defaults as semantic intent.
- Primary body face is `"Helvetica Now Text", Helvetica, Arial, sans-serif`.
- Display identity splits across `"Nike Futura ND"` for brand display and `"Helvetica Now Display Medium"` for commercial oversized/title tiers.
- Body copy uses 400; strong body and title tiers use 500; editorial conversation tiers use 300.
- Pill/capsule controls dominate buttons through `--podium-cds-button-border-radius` and 999px-style behavior.
- Focus treatment is explicit and blue: #1151FF with 2px ring shadows.
- Product and editorial imagery carry depth; UI chrome mostly avoids decorative shadow.
- Breakpoints are named in CDS: 320, 600, 960, 1440, and 1920px.
- Motion exists but is functional: 250ms normal transitions plus a few 800ms transform/opacity campaign reveals.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Athletic Editorial
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **black-and-white athletic editorial commerce with oversized Nike display type**으로 기억된다.
> **Code Complexity**: high — responsive typography, component tokens, navigation states, motion timings, and multiple brand font families are all present in production CSS.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Nike처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Helvetica Now Text", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #111111; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #111111; --focus: #1151FF; }
```

**절대 하지 말아야 할 것 하나**: Nike를 "검정 로고 + 아무 산세리프"로 환원하지 말 것. `Nike Futura ND`, `Helvetica Now Display Medium`, `Helvetica Now Text`의 역할 분리가 핵심이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://nike.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | reused existing phase1 + CSS artifacts |
| HTML size | 813187 bytes (Next/React surface detected by `__NEXT_DATA__`) |
| CSS files | 6 files, total 429706 chars |
| Token prefix | `podium-cds` |
| Method | existing phase1 JSON, production CSS token summary, and screenshot artifact reuse |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next/React-style production page (`__NEXT_DATA__` present in captured HTML)
- **Design system**: Nike Podium CDS — prefix `--podium-cds`
- **CSS architecture**:
  ```css
  core        (--podium-cds-color-*)          raw colors and scale tokens
  typography  (--podium-cds-typography-*)    responsive type shorthands
  component   (--podium-cds-button-*)        button radius, padding, focus, motion
  motion      (--podium-cds-motion-*)        duration/easing primitives
  breakpoint  (--podium-cds-breakpoint-*)    responsive thresholds
  ```
- **Class naming**: generated CSS module/hash class names plus `nds-*` component classes.
- **Default theme**: light (`#FFFFFF` page/surface, `#111111` text).
- **Font loading**: custom Nike font family declarations found in CSS; fallback chain includes Helvetica and Arial.
- **Canonical anchor**: global retail navigation and product/editorial home surface.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Nike Futura ND` (brand display)
- **Commercial title font**: `Helvetica Now Display Medium`
- **Body font**: `Helvetica Now Text`
- **Editorial alternate**: `Palatino LT Pro Light`
- **Icon font**: `nike-glyphs`
- **Weight normal / bold**: `400` / `500` for most UI, with `700` appearing sparsely.

```css
:root {
  --podium-cds-font-family: "Helvetica Now Text", Helvetica, Arial, sans-serif;
  --podium-cds-font-family-display: "Nike Futura ND", "Helvetica Now Text Medium", Helvetica, Arial, sans-serif;
  --podium-cds-font-family-title: "Helvetica Now Display Medium", Helvetica, Arial, sans-serif;
  --podium-cds-font-weight-normal: 400;
  --podium-cds-font-weight-medium: 500;
}

body {
  font-family: var(--podium-cds-font-family);
  font-weight: var(--podium-cds-font-weight-normal);
}
```

### Note on Font Substitutes

- **Nike Futura ND** — proprietary brand display. Open-source substitute: use **Futura PT Condensed Extra Bold** if licensed, otherwise **Anton** with restrained sizing. Keep line-height near `.9` for display tokens; a generic Inter headline will look too soft.
- **Helvetica Now Text** — proprietary/commercial. Open-source substitute: **Inter** or **Roboto Flex** at 400/500. Do not increase body weight to 600 to compensate; Nike's UI rests on 400/500, not heavy body copy.
- **Palatino LT Pro Light** — editorial voice. Substitute with **Libre Baskerville** or **Cormorant Garamond** at 300/400 only for campaign/editorial quote surfaces, never for product grid labels.
- **Nike glyphs** — do not replace with emoji or decorative symbols. Use neutral SVG/icons with 1.5-2px strokes if the glyph font is unavailable.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `--podium-cds-typography-1920-plus-oversize1` | `11.625rem` | `500` | `1` | `0` |
| `--podium-cds-typography-1920-plus-oversize2` | `9.375rem` | `500` | `1` | `0` |
| `--podium-cds-typography-1920-plus-display1` | `7.5rem` | implied/brand display | `.9` | `0` |
| `--podium-cds-typography-960-to-1919-display1` | `6rem` | implied/brand display | `.9` | `0` |
| `--podium-cds-typography-320-to-959-display1` | `3rem` | implied/brand display | `.9` | `0` |
| `--podium-cds-typography-1920-plus-title1` | `3rem` | `500` | `1.2` | `0` |
| `--podium-cds-typography-320-to-1919-title1` | `2.5rem` | `500` | `1.2` | `0` |
| `--podium-cds-typography-960-plus-editorial-body1` | `1.25rem` | `400` | `1.5` | `0` |
| `--podium-cds-typography-body1` | `1rem` | `400` | `1.5` | `0` |
| `--podium-cds-typography-body1-strong` | `1rem` | `500` | `1.5` | `0` |
| `--podium-cds-typography-body2` | `.875rem` | `400` | `1.5` | `0` |
| `--podium-cds-typography-body3` | `.75rem` | `400` | `1.5` | `0` |

> Nike's type system is not a single scale. It is a responsive type stack with separate oversize, display, conversation, title, editorial-body, and body families.

### Principles

1. Display type gets compressed and athletic before it gets heavy. `Nike Futura ND` at `.9` line-height creates the brand poster voice.
2. UI body copy stays disciplined at 400, with 500 used for labels, nav, title, and strong body variants.
3. Weight 600 is absent from the extracted scale. Do not "modern SaaS" the site with semibold everywhere.
4. `Palatino LT Pro Light` is an editorial exception, not a global serif layer.
5. The system changes sizes by breakpoint rather than fluid `clamp()` in the captured tokens.
6. Letter-spacing is not the hero trick here; font selection and line-height carry the compression.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (Nike core)

| Token | Hex |
|---|---|
| `--podium-cds-color-black` | `#111111` |
| `--podium-cds-color-white` | `#FFFFFF` |

### 06-2. Brand Dark Variant

> N/A — captured homepage artifacts show a light default commerce surface; no full dark-theme token mapping was verified.

### 06-3. Neutral Ramp

| Step | Token | Hex |
|---|---|---|
| Ink | `--podium-cds-color-black` | `#111111` |
| White | `--podium-cds-color-white` | `#FFFFFF` |
| Muted UI text | observed neutral | `#707072` |
| Black utility | raw legacy shorthand | `#000000` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Focus blue | `--podium-cds-color-blue-500` | `#1151FF` |
| Blue dark | `--podium-cds-color-blue-700` | `#061DBB` |
| Red error | `--podium-cds-color-red-500` | `#EE0005` |
| Orange action/ramp | `--podium-cds-color-orange-400` | `#FF5000` |
| Green success/ramp | `--podium-cds-color-green-500` | `#1EAA52` |
| Yellow warning/ramp | `--podium-cds-color-yellow-400` | `#FDC400` |
| Campaign volt | observed chromatic | `#D5FF44` |
| Cool slate | observed chromatic | `#73859F` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--podium-cds-color-text-primary-on-light` | `#111111` | primary text on light surface |
| `--podium-cds-color-focus-ring` | `#1151FF` | keyboard/focus ring |
| `--podium-cds-color-box-focus-ring` | `#1151FF` | focus box shadow |
| `--podium-cds-color-white` | `#FFFFFF` | page, card, and inverse text surfaces |
| `--podium-cds-color-red-500` | `#EE0005` | error/destructive semantic ramp anchor |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--podium-cds-button-border-width` | `--podium-cds-size-border-width-m` | button stroke width |
| `--podium-cds-button-border-radius` | component radius token | capsule button shape |
| `--animation-duration` | `--podium-cds-transition-duration-normal` → `250ms` | shared animation duration |
| `--podium-cds-color-text-primary-on-light` | `--podium-cds-color-black` → `#111111` | default readable text |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---|---:|
| white/surface | `#FFFFFF` / `#fff` | 21 |
| cool slate campaign | `#73859F` | 13 |
| raw black utility | `#000000` / `#000` | 12 |
| focus blue | `#1151FF` | 6 |
| ink | `#111111` | 3+ |
| muted gray | `#707072` | 3 |
| volt campaign | `#D5FF44` | 2+ |
| orange campaign | `#FF623A` / `#FF5000` | 2+ |

### 06-8. Color Stories

**`{colors.ink}` (#111111)** — Nike's true UI brand color in this capture. It is text, logo-adjacent utility, button fill, and the anchor for the black/white store experience. Use this instead of `#000000` for primary interface text.

**`{colors.surface}` (#FFFFFF)** — The product floor. Nike lets photography and product color do the emotional work, so the commerce shell stays white and direct.

**`{colors.focus}` (#1151FF)** — Accessibility blue. It appears as a 2px focus ring, not as a marketing accent or CTA color.

**`{colors.cool-slate}` (#73859F)** — Campaign/runtime chromatic color. It appears frequently enough to register, but it should not be promoted into a global brand primary without page-specific evidence.

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token / Pattern | Value | Use case |
|---|---:|---|
| repeated utility | `4px` | smallest nudge, icon/inline offsets |
| repeated utility | `8px` | compact gaps |
| repeated utility | `12px` | small control padding |
| repeated utility | `16px` | baseline retail spacing |
| repeated utility | `20px` | nav/product item inner spacing |
| repeated utility | `24px` | common card/control section spacing |
| repeated utility | `28px` | product/nav rhythm |
| repeated utility | `32px` | section and grid rhythm |
| repeated utility | `36px` | large nav/section rhythm |
| repeated utility | `40px` | mid-large spacing |
| repeated utility | `44px` | touch-size adjacent spacing |
| repeated utility | `48px` | campaign/section spacing |

**주요 alias**:
- `--podium-cds-button-padding-top-l` + `--podium-cds-button-padding-sides-l` → large pill button padding
- `--podium-cds-breakpoint-m` → `960px` transition between compact and desktop typography

### Whitespace Philosophy

Nike's spacing is retail-functional before it is decorative. The system repeats 24, 36, and 48px often, which creates a store rhythm: enough air for photography and headlines to breathe, but not so much that product discovery slows down.

The hero/editorial layer gets the most air. Navigation, menus, and product links compress around 16-24px units. That contrast is important: campaign surface feels broad; shopping surface feels fast.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token / Value | Value | Context |
|---|---:|---|
| `--podium-cds-button-border-radius` | variable | primary capsule buttons |
| `--podium-cds-size-border-radius-s` | variable | small surfaces |
| circular controls | `50%` | icon buttons, round affordances |
| pill/capsule | `24px` | buttons and rounded controls |
| small radius | `2px` | utility/chrome |
| small card | `4px` | compact cards |
| card/media | `8px` | product/media containers |
| medium card | `12px` | occasional panel container |
| large capsule | `20px`, `30px` | prominent rounded UI |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| none | `none` | dominant chrome treatment |
| focus-ring | `0 0 0 2px #1151FF` | keyboard focus and accessible outline |
| inset divider | `var(--podium-cds-color-border-tertiary) 0 -1px 0 0 inset` | structural hairline/divider |
| special inset | `inset 0 0 0 10px` | exceptional state/chrome effect |

Nike does not create brand depth through layered app shadows. Depth is mostly photographic; component shadows are state/accessibility tools.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---:|---|
| `--podium-cds-transition-duration-normal` | `250ms` | normal UI transition duration |
| opacity/visibility | `opacity 250ms, visibility 0s linear 250ms` | menu and overlay show/hide |
| campaign reveal | `transform 0.8s, opacity 1s` | hero/editorial entry motion |
| quick interaction | `all .1s ease` | small control feedback |
| medium transition | `all .4s` / `all .5s` | richer UI or campaign states |
| expressive underline/rail | `width var(--podium-cds-motion-duration-400) var(--podium-cds-motion-easing-expressive)` | nav/indicator movement |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: N/A from captured token summary; homepage HTML/CSS was reused but layout measurement was not re-run.
- **Grid type**: editorial hero + commerce navigation/listing grid hybrid.
- **Column count**: responsive, not asserted from current evidence.
- **Gutter**: 16-24px for retail density; 32-48px for campaign/editorial bands.

### Hero

- **Pattern Summary**: full-width campaign/product imagery + oversized display/title type + black/white pill CTAs.
- Layout: image-led editorial product surface, with campaign areas behaving wider than product navigation.
- Background: primarily photography/video or white product floor.
- **Background Treatment**: image/video first; solid #FFFFFF for store chrome; no default decorative gradient mesh.
- H1: `Nike Futura ND` or `Helvetica Now Display Medium`, responsive from `3rem` to `7.5rem+`, display line-height `.9` or title line-height `1.2`.
- Max-width: N/A from current artifacts; avoid inventing an exact container.

### Section Rhythm

```css
section {
  padding-block: 32px 48px;
  padding-inline: 24px;
}

@media (min-width: 960px) {
  section {
    padding-block: 48px;
  }
}
```

### Card Patterns

- **Card background**: `#FFFFFF` or product image surface.
- **Card border**: minimal; dividers/hairlines appear more than decorative borders.
- **Card radius**: `8px` common, with buttons using pill radius.
- **Card padding**: 16-24px range for commerce modules.
- **Card shadow**: mostly none; product imagery carries visual weight.

### Navigation Structure

- **Type**: global retail navigation with dense category menus and utility links.
- **Position**: top navigation, with secondary/dropdown structures.
- **Height**: not asserted; extracted links show dense commerce navigation.
- **Background**: `#FFFFFF`.
- **Border**: minimal hairline/inset divider behavior.

### Content Width

- **Prose max-width**: not measured.
- **Container max-width**: not measured.
- **Sidebar width**: N/A for homepage surface.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| XS | `320px` | smallest supported CDS threshold |
| S | `600px` | compact/tablet transition |
| M | `960px` | desktop typography and layout threshold |
| L | `1440px` | large desktop type and spacing |
| XL | `1920px` | oversize display typography tier |

### Touch Targets

- **Minimum tap size**: use 44px as implementation floor; 44px appears frequently in spacing data.
- **Button height (mobile)**: infer 44-48px range from spacing and capsule button patterns.
- **Input height (mobile)**: not verified.

### Collapsing Strategy

- **Navigation**: dense global navigation collapses into dropdown/menu structures.
- **Grid columns**: product/editorial modules should collapse from multi-column to single/stacked cards.
- **Sidebar**: N/A for homepage.
- **Hero layout**: keep imagery first; reduce display type from desktop 6-7.5rem tiers to 3rem mobile display tier.

### Image Behavior

- **Strategy**: photography/video as primary brand surface.
- **Max-width**: full-bleed for hero/editorial, contained for product cards.
- **Aspect ratio handling**: preserve product/campaign media; do not crop into abstract decorative backgrounds.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

Primary buttons are black capsules with white text on light backgrounds. Secondary buttons invert or soften the fill but preserve the capsule shape. Button specs are tokenized through `--podium-cds-button-*`.

```html
<button class="nds-btn nds-button nike-button-primary">Shop</button>
```

| Property | Value |
|---|---|
| Background | `#111111` |
| Text | `#FFFFFF` |
| Radius | `--podium-cds-button-border-radius` / pill |
| Border width | `--podium-cds-button-border-width` |
| Padding | `--podium-cds-button-padding-top-l` `--podium-cds-button-padding-sides-l` |
| Focus | `0 0 0 2px #1151FF` |

### Badges

Badges were not surfaced as a dominant component in the captured summary. If needed, use 12-14px Helvetica Now Text, 500 weight, black/white or muted gray only. Do not introduce neon labels unless the campaign CSS supplies them.

### Cards & Containers

Cards are product/editorial surfaces rather than framed SaaS panels.

| Property | Value |
|---|---|
| Background | `#FFFFFF` or product image |
| Border | none or subtle hairline |
| Radius | `8px` for media/card; pill only for controls |
| Padding | 16-24px |
| Shadow | none |
| Hover | image/text affordance, not heavy elevation |

### Navigation

Navigation is a core component. Captured links include utility links (`Help`, `Order Status`, `Join Us`, `Sign In`) and commerce categories (`Men`, `Best Sellers`, `Latest Drops`, `SNKRS Launch Calendar`, `Sale`, `Shoes`).

| Property | Value |
|---|---|
| Font | `Helvetica Now Text` |
| Size | commonly 14-16px |
| Weight | 400/500 |
| Color | `#111111` primary, `#707072` muted |
| Background | `#FFFFFF` |
| Interaction | dropdown indicators with transform transition |

### Inputs & Forms

The homepage capture did not expose full form validation states. Search/AI entry surfaces appear in navigation, but validation, error, loading, and disabled input states are listed as gaps.

### Hero Section

Hero sections should be image-led and typographically assertive.

```html
<section class="nike-hero">
  <img class="nike-hero-media" src="campaign.jpg" alt="">
  <div class="nike-hero-copy">
    <h1>JUST DO IT</h1>
    <a class="nike-button-primary">Shop</a>
  </div>
</section>
```

| Property | Value |
|---|---|
| Media | full-width product/campaign photography or video |
| Display face | `Nike Futura ND` or `Helvetica Now Display Medium` |
| Display size | mobile `3rem`, desktop `6rem+`, large `7.5rem+` |
| Line-height | `.9` for Nike display, `1.2` for title |
| CTA | black/white pill |

### 13-2. Named Variants

#### `button-primary-black-pill`

- Background: `#111111`
- Foreground: `#FFFFFF`
- Radius: pill / `--podium-cds-button-border-radius`
- State: focus ring `0 0 0 2px #1151FF`
- Use: main commerce CTA on white or image-light surfaces.

#### `button-secondary-white-pill`

- Background: `#FFFFFF`
- Foreground: `#111111`
- Radius: pill
- Border: transparent or minimal
- Use: secondary CTA over dark image/video or paired action.

#### `nav-commerce-link`

- Font: `"Helvetica Now Text"`
- Size: 14-16px
- Weight: 500 for primary categories, 400 for utility links
- Color: `#111111` primary, `#707072` muted
- Use: dense retail navigation and category menus.

#### `focus-ring-blue`

- Shadow: `0 0 0 2px #1151FF`
- Color role: accessibility only
- Use: buttons, icon buttons, boxes, search affordances.

### 13-3. Signature Micro-Specs

```yaml
podium-responsive-display-stack:
  description: "Breakpoint-specific display/title tokens preserve Nike scale from mobile commerce to 1920-plus campaign surfaces."
  technique: "--podium-cds-typography-320-to-959-display1: 3rem/.9; --podium-cds-typography-960-to-1919-display1: 6rem/.9; --podium-cds-typography-1920-plus-display1: 7.5rem/.9; --podium-cds-typography-1920-plus-oversize1: 11.625rem/1"
  applied_to: ["{component.hero}", "{component.campaign-title}", "{component.editorial-moment}"]
  visual_signature: "The same campaign collapses into a shoppable mobile page without losing the compressed athlete-poster impact."

futura-nd-athletic-compression:
  description: "Brand force comes from Nike Futura ND and tight line-height, not from generic heavy sans weight."
  technique: "font-family: 'Nike Futura ND', 'Helvetica Now Text Medium', Helvetica, Arial, sans-serif; line-height: .9; letter-spacing: 0; weight around 500"
  applied_to: ["{component.hero}", "{component.display-headline}"]
  visual_signature: "Headlines feel like race signage or a training-poster block: dense, vertical, and fast."

black-white-pill-commerce-cta:
  description: "Commerce actions use a black/white capsule system instead of color-coded button hierarchy."
  technique: "background: #111111 /* {colors.ink} */; color: #FFFFFF /* {colors.surface} */; border-radius: var(--podium-cds-button-border-radius); padding: var(--podium-cds-button-padding-top-l) var(--podium-cds-button-padding-sides-l); border: 1px solid transparent"
  applied_to: ["{component.button-primary}", "{component.hero-cta}", "{component.commerce-cta}"]
  visual_signature: "Every primary action reads like a small piece of Nike equipment: black capsule, white type, no decorative gradient."

blue-accessibility-ring-only:
  description: "The vivid blue is reserved for interaction state rather than brand expression."
  technique: "box-shadow: 0 0 0 2px #1151FF /* {colors.focus} */; used on focus-visible button/icon/control states"
  applied_to: ["{component.focus-ring}", "{component.button-primary}", "{component.icon-button}", "{component.search-affordance}"]
  visual_signature: "A sharp blue ring appears only when the interface needs accessibility clarity, then the black/white Nike surface returns."

photography-depth-no-ui-elevation:
  description: "Depth is assigned to product and campaign media while UI chrome stays flat."
  technique: "component box-shadow mostly none; structural depth via inset divider `var(--podium-cds-color-border-tertiary) 0 -1px 0 0 inset`; media/card radius around 8px"
  applied_to: ["{component.hero-media}", "{component.product-tile}", "{component.editorial-section}", "{component.navigation}"]
  visual_signature: "The page feels dimensional through shoes, athletes, and campaign imagery, not through SaaS-style elevated panels."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | short, imperative, athlete-oriented | `Just Do It` |
| Primary CTA | one or two words | `Shop`, `Join Us` |
| Navigation | category-first commerce vocabulary | `Men`, `Shoes`, `Latest Drops` |
| Utility | service verbs, plain wording | `Order Status`, `Returns` |
| Tone | direct, retail-clear, campaign-capable | no long SaaS-style explanations |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Nike — copy into your root stylesheet */
:root {
  /* Fonts */
  --nike-font-body: "Helvetica Now Text", Helvetica, Arial, sans-serif;
  --nike-font-title: "Helvetica Now Display Medium", Helvetica, Arial, sans-serif;
  --nike-font-display: "Nike Futura ND", "Helvetica Now Text Medium", Helvetica, Arial, sans-serif;
  --nike-font-editorial: "Palatino LT Pro Light", Georgia, serif;
  --nike-font-weight-normal: 400;
  --nike-font-weight-medium: 500;

  /* Core colors */
  --nike-ink: #111111;
  --nike-surface: #FFFFFF;
  --nike-muted: #707072;
  --nike-focus: #1151FF;
  --nike-cool-slate: #73859F;
  --nike-volt: #D5FF44;

  /* Semantic colors */
  --nike-bg-page: var(--nike-surface);
  --nike-text: var(--nike-ink);
  --nike-text-muted: var(--nike-muted);
  --nike-button-bg: var(--nike-ink);
  --nike-button-fg: var(--nike-surface);

  /* Spacing */
  --nike-space-xs: 8px;
  --nike-space-sm: 12px;
  --nike-space-md: 24px;
  --nike-space-lg: 36px;
  --nike-space-xl: 48px;

  /* Radius */
  --nike-radius-card: 8px;
  --nike-radius-pill: 999px;
}

body {
  margin: 0;
  background: var(--nike-bg-page);
  color: var(--nike-text);
  font-family: var(--nike-font-body);
  font-weight: var(--nike-font-weight-normal);
}

.nike-display {
  font-family: var(--nike-font-display);
  font-size: clamp(3rem, 8vw, 7.5rem);
  line-height: .9;
  font-weight: var(--nike-font-weight-medium);
  letter-spacing: 0;
}

.nike-title {
  font-family: var(--nike-font-title);
  font-weight: var(--nike-font-weight-medium);
  line-height: 1.2;
}

.nike-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 12px 24px;
  border-radius: var(--nike-radius-pill);
  border: 1px solid transparent;
  background: var(--nike-button-bg);
  color: var(--nike-button-fg);
  font: 500 16px/1 var(--nike-font-body);
}

.nike-button:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2px var(--nike-focus);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Nike-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        nike: {
          ink: '#111111',
          surface: '#FFFFFF',
          muted: '#707072',
          focus: '#1151FF',
          slate: '#73859F',
          volt: '#D5FF44',
        },
      },
      fontFamily: {
        nikeBody: ['Helvetica Now Text', 'Helvetica', 'Arial', 'sans-serif'],
        nikeTitle: ['Helvetica Now Display Medium', 'Helvetica', 'Arial', 'sans-serif'],
        nikeDisplay: ['Nike Futura ND', 'Helvetica Now Text Medium', 'Helvetica', 'Arial', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
      },
      borderRadius: {
        nikeCard: '8px',
        nikePill: '999px',
      },
      boxShadow: {
        nikeFocus: '0 0 0 2px #1151FF',
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
| Brand primary | `{colors.ink}` | `#111111` |
| Background | `{colors.surface}` | `#FFFFFF` |
| Text primary | `{colors.ink}` | `#111111` |
| Text muted | `{colors.muted-text}` | `#707072` |
| Border/focus | `{colors.focus}` | `#1151FF` |
| Campaign cool | `{colors.cool-slate}` | `#73859F` |
| Campaign volt | `{colors.volt}` | `#D5FF44` |
| Error | `{colors.error}` | `#EE0005` |

### Example Component Prompts

#### Hero Section

```text
Nike 스타일 히어로 섹션을 만들어줘.
- 배경: 제품/캠페인 photography 또는 #FFFFFF product floor
- H1: Nike Futura ND, mobile 3rem / desktop 6rem+, line-height .9, weight 500
- 대체 title: Helvetica Now Display Medium, line-height 1.2
- CTA: black pill, bg #111111, text #FFFFFF, min-height 44px, radius 999px
- Focus: 0 0 0 2px #1151FF
- UI chrome: shadow 없이 사진과 타입으로 위계 만들기
```

#### Card Component

```text
Nike 스타일 product/editorial card를 만들어줘.
- 배경: #FFFFFF 또는 실제 product image surface
- border: none 또는 아주 얇은 hairline
- radius: 8px
- padding: 16px 또는 24px
- shadow: none
- 제목: Helvetica Now Text 또는 Display Medium, weight 500
- 본문: Helvetica Now Text, 14-16px, weight 400, color #111111 또는 #707072
```

#### Navigation

```text
Nike 스타일 상단 네비게이션을 만들어줘.
- 배경: #FFFFFF
- 링크: Helvetica Now Text, 14-16px, weight 400/500
- primary link color: #111111
- muted utility color: #707072
- dropdown/indicator transition: transform 250-300ms
- focus-visible ring: #1151FF 2px
```

### Iteration Guide

- **색상 변경 시**: primary CTA는 `#111111`을 유지한다. 캠페인 색은 섹션 한정으로만 쓴다.
- **폰트 변경 시**: body는 400, nav/title emphasis는 500. 600을 기본값으로 쓰지 않는다.
- **여백 조정 시**: 12/16/24/36/48px 리듬을 우선 사용한다.
- **새 컴포넌트 추가 시**: pill controls + minimal chrome + photography-led hierarchy를 따른다.
- **포커스 상태**: `#1151FF` 2px ring을 유지한다.
- **히어로 구현 시**: gradient mesh나 decorative blobs 대신 실제 product/campaign media를 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#111111` as Nike's primary ink and CTA fill.
- Use `#FFFFFF` as the default retail/product floor.
- Preserve the font roles: Nike Futura ND for display, Helvetica Now Display Medium for large titles, Helvetica Now Text for UI/body.
- Keep body copy at 400 and primary labels/title emphasis at 500.
- Use pill buttons with black/white contrast and minimal borders.
- Use `#1151FF` for focus rings and accessibility state.
- Let product photography/video carry emotional depth.
- Treat chromatic colors like `#73859F` and `#D5FF44` as campaign/runtime colors, not global brand defaults.

### ❌ DON'T

- 배경을 `#F7F7F5` 또는 warm cream으로 두지 말 것 — 대신 `#FFFFFF` 사용.
- primary text를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#111111` 사용.
- focus ring을 `#000000` 또는 invisible outline으로 두지 말 것 — 대신 `#1151FF` 2px ring 사용.
- primary CTA를 `#1151FF` 또는 `#D5FF44`로 두지 말 것 — 대신 `#111111` fill 사용.
- muted text를 `#999999`로 두지 말 것 — 대신 `#707072` 사용.
- body에 `font-weight: 600` 사용 금지 — Nike UI body는 400, strong/title 계열은 500 중심이다.
- hero display를 generic `Inter`로 대체하지 말 것 — `Nike Futura ND` 역할을 별도 display face로 보존한다.
- component chrome에 heavy multi-layer shadow 사용 금지 — Nike chrome은 mostly none이고 focus만 `0 0 0 2px #1151FF`가 명확하다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Brand gradient: none as a global identity layer. Campaign media may be colorful, but the UI system is not gradient-led.
- Second global brand color: absent. Black/white carries the Nike shell; chromatic colors are contextual.
- Weight 600 as default emphasis: absent from the extracted typography scale.
- Heavy app shadows: absent. Product imagery creates depth; chrome stays flat.
- Decorative border-accent cards: absent. Retail cards are media/content surfaces, not SaaS panels.
- Warm editorial cream background: absent in the captured default shell.
- Emoji/icon novelty: absent. Use Nike glyphs or neutral icons, never playful emoji placeholders.
- Blue CTA language: absent. `#1151FF` is focus/accessibility, not the brand button color.
- Dense paragraph marketing copy: absent. Voice is short, imperative, and category-led.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage artifact reuse** — This guide reused existing `insane-design/nike` phase1/CSS/HTML/screenshot artifacts instead of live refetching Nike.com during this run.
- **Single-surface bias** — The captured HTML is the Nike.com homepage/global retail surface. Checkout, account, member, SNKRS, product-detail, and size-selection flows were not separately visited.
- **Screenshot not re-rendered** — `hero-cropped.png` existed and was reused, but no fresh browser screenshot comparison was performed in this workflow.
- **Exact layout measurements missing** — Container max-width, hero pixel bounds, nav height, and grid column counts were not remeasured from a live viewport.
- **Form states incomplete** — Search/AI entry controls are visible in HTML snippets, but validation, error, loading, disabled, and success states for forms were not fully observed.
- **Dark theme not mapped** — No full dark-mode counterpart palette was verified from the captured artifacts.
- **Campaign color ambiguity** — Colors such as `#73859F`, `#D5FF44`, `#FF623A`, and `#2B333F` appear in CSS frequency data, but may belong to campaign, video, or SVG assets rather than stable global UI tokens.
- **Typography parser limitation** — Phase1 `typography.scale` was empty, so type scale rows were reconstructed from resolved token samples rather than a complete parsed ladder object.
- **Motion behavior partial** — CSS transition values were summarized, but JavaScript-driven scroll triggers, video behavior, and IntersectionObserver choreography were not analyzed.
- **Component variant floor avoided** — Only observed or strongly token-supported variants are listed; absent components were intentionally left as gaps rather than invented.
