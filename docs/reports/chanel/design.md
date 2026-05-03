---
schema_version: 3.2
slug: chanel
service_name: CHANEL
site_url: https://www.chanel.com
fetched_at: 2026-05-03T06:19:40Z
default_theme: light
brand_color: "#000000"
primary_font: abchanel-2022
font_weight_normal: 300
token_prefix: chanel

bold_direction: Monochrome Luxury
aesthetic_category: Refined Minimalism
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high

archetype: luxury-brand
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Real CHANEL CSS exposes a working component system, typography stack, nav states, search tokens, and product-grid rules, but not a public design-token API."

colors:
  primary: "#000000"
  text-primary: "#1D1D1D"
  surface-base: "#FFFFFF"
  surface-variant: "#F9F9F9"
  hover-surface: "#F1F1F1"
  text-muted: "#767676"
  hairline: "#ECECEC"
  disabled: "#D8D8D8"
  error: "#CD0000"
typography:
  display: "abchanel-2022"
  body: "abchanel-2022"
  corporate: "abchanel-corpo"
  ladder:
    - { token: copy-xl, size: "18px", weight: 300, line_height: "27px", tracking: "0" }
    - { token: copy-l, size: "15px", weight: 300, line_height: "23px", tracking: "0" }
    - { token: copy-m, size: "13px", weight: 300, line_height: "20px", tracking: "0" }
    - { token: copy-s, size: "11px", weight: 300, line_height: "17px", tracking: "0" }
    - { token: button, size: "11-14px", weight: "500-700", line_height: "16-22px", tracking: "0.01875-0.04375rem" }
  weights_used: [300, 400, 500, 600, 700]
  weights_absent: [800, 900]
components:
  button-primary-black: { bg: "{colors.primary}", color: "{colors.surface-variant}", radius: "0px", padding: "16px 24px", text_transform: "uppercase" }
  button-primary-white: { bg: "{colors.surface-base}", color: "{colors.text-primary}", radius: "0px", padding: "16px 24px", text_transform: "uppercase" }
  button-disabled: { bg: "{colors.surface-variant}", color: "#949494", border: "1px solid {colors.disabled}" }
  nav-horizontal: { height: "50px", bg: "{colors.surface-base}", border_bottom: "1px solid {colors.hairline}", gap: "18px" }
  product-card: { bg: "transparent", image_bg: "{colors.surface-variant}", radius: "0px", shadow: "none" }
---

# DESIGN.md — CHANEL (Designer Guidebook v3.2)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

CHANEL's web interface behaves like a white gallery with the brand name engraved above the door. The UI does not compete with the product photograph; it frames it. The screenshot shows the house mark centered at the top, a long uppercase navigation rail below it, then an oversized N°5 visual that is allowed to crop brutally at the viewport edge. The page is not trying to be friendly. It is trying to feel inevitable.

The usable color system is nearly monochrome: `#000000` (`{colors.primary}`) for brand force, `#1D1D1D` (`{colors.text-primary}`) for readable black, `#FFFFFF` (`{colors.surface-base}`) for the gallery floor, and `#ECECEC` (`{colors.hairline}`) for just enough structure. Product amber and red appear in photography, not in UI chrome. CHANEL operates like a glass perfume vitrine where the object may be gold, skin, red lacquer, or black ribbon, but the case itself refuses tint. No second brand color enters the interface; the season is allowed to live only inside the image.

Typography is the second lock. CHANEL uses the custom `abchanel-2022` stack heavily, with thin body copy at weight 300 and compact uppercase controls with deliberate letter-spacing. The logo and nav are not merely text; they are alignment devices. They behave like boutique signage engraved into a white stone lintel: small, centered, exact, and unforgiving. A one-pixel error in spacing or a casual lowercase label makes the system collapse into generic fashion e-commerce.

The hero crop is the other signature. The N°5 campaign image is treated less like a responsive banner and more like a magazine spread laid under a precision-cut mat: the browser edge slices the bottle and model instead of politely fitting them. That crop is not accidental drama. It tells the user the campaign is larger than the viewport, while the header remains a quiet institutional plaque above it.

The component language is severe: square buttons, hairline dividers, no decorative card elevation, almost no radius, restrained transitions, and a navigation system that slides and masks rather than bounces. Shadow belongs only to photography; UI chrome stays flat. The craft is negative. CHANEL gets its luxury by refusing most of the moves modern consumer sites use to look rich.

### Key Characteristics

- Monochrome UI discipline: `#000000`, `#1D1D1D`, `#FFFFFF`, `#ECECEC` dominate the interface.
- Centered uppercase CHANEL wordmark is the page anchor, with category navigation acting as a second baseline.
- Product photography carries color; UI tokens stay neutral.
- Body copy uses light 300 weight; controls use uppercase 500-700 with positive tracking.
- Navigation height is compact at `3.125rem` with a `#ECECEC` hairline.
- Buttons are square-edged, uppercase, and high-contrast, not pill-shaped.
- Product/card surfaces avoid drop shadows; structure comes from spacing, cropping, and image scale.
- Interaction motion is restrained: `300ms` navigation height/transform transitions and `200ms` underline color fades.
- Accessibility/high-contrast variants are present in CSS, but still use the same monochrome grammar.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Monochrome Luxury
> **Aesthetic Category**: Refined Minimalism
> **Signature Element**: 이 사이트는 **hero_impact**으로 기억된다.
> **Code Complexity**: medium — monochrome tokens are simple, but navigation masks, responsive product grids, locale font stacks, and stateful buttons require careful implementation.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 CHANEL처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "abchanel-2022", "helvetica-adjusted-abchanel-2022", helvetica, sans-serif;
  font-weight: 300;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #1D1D1D; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #000000; --hairline: #ECECEC; }
```

**절대 하지 말아야 할 것 하나**: CHANEL UI를 beige/gold luxury palette로 재해석하지 말 것. 금색은 제품 사진의 물성이지 인터페이스 토큰이 아니다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.chanel.com` |
| Fetched | 2026-05-03T06:19:40Z |
| Extractor | reused existing phase1 artifacts + captured HTML/CSS/screenshot |
| HTML size | 1,857,212 bytes |
| CSS files | 2 external + 1 inline, approx 1,420,424 CSS bytes |
| Token prefix | `chanel` |
| Method | CSS custom property parsing, HTML structure sampling, screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: enterprise commerce CMS front end with hashed CSS modules and a large inline CSS payload.
- **Design system**: CHANEL component CSS, exposed through classes such as `.cc-button`, `.cc-copy-*`, `.Navigation_*`, `.Product_*`, and search token variables.
- **CSS architecture**:
  ```css
  core        (--search-*, --active-text-color)     terminal colors and state values
  component   (.cc-button, .cc-copy-*, .Product_*)  component class contracts
  module      (.Navigation_wrapper__*)              hashed layout modules
  ```
- **Class naming**: mixed global `cc-*` components plus CSS-module hashes such as `.Navigation_wrapper__drj8y`.
- **Default theme**: light (`#FFFFFF` page surface).
- **Font loading**: external `@font-face` file with CHANEL-owned font names, including `abchanel-2022`, `abchanel-corpo`, and locale-specific fallbacks.
- **Canonical anchor**: centered CHANEL wordmark + horizontal category navigation.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `abchanel-2022` (proprietary CHANEL web font)
- **Corporate/support font**: `abchanel-corpo` (proprietary CHANEL web font)
- **Code font**: N/A — no code UI observed
- **Weight normal / bold**: `300` / `600-700`

```css
:root {
  --chanel-font-family: "abchanel-2022", "helvetica-adjusted-abchanel-2022", helvetica, sans-serif;
  --chanel-font-family-corpo: "abchanel-corpo", "arial-adjusted-abchanel-corpo", arial, sans-serif;
  --chanel-font-weight-normal: 300;
  --chanel-font-weight-bold: 600;
}
body {
  font-family: var(--chanel-font-family);
  font-weight: var(--chanel-font-weight-normal);
}
```

### Note on Font Substitutes

- **`abchanel-2022`** is not an open font. Use **Helvetica Neue / Helvetica** as the closest system substitute, then compensate with strict uppercase, wider tracking on controls, and lighter body weight.
- **Body substitute**: Helvetica at `300` or `400` with `line-height` kept close to CHANEL's scale. Do not use Inter's default 400 if it makes paragraphs look too software-like.
- **Navigation substitute**: Helvetica uppercase at `600`, `letter-spacing: 0.04em`, and a hard 50px nav line. This matters more than matching glyph geometry exactly.
- **Logo substitute**: do not recreate the CHANEL logo as live text unless legally and visually appropriate. Use the official wordmark asset in production.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `cc-copy-xl` | 18px | 300 | 27px | 0 |
| `cc-copy-l` | 15px | 300 | 23px | 0 |
| `cc-copy-m` | 13px | 300 | 20px | 0 |
| `cc-copy-s` | 11px | 300 | 17px | 0 |
| `cc-button` small | 11px | 600 | 16px | 0.04375rem |
| `cc-button` standard | 12px | 600-700 | 18px | 0-0.01875rem |
| `cc-button` large | 14px | 500-700 | 18-22px | 0.03125rem |
| Navigation labels | approx 13px | 600 | 50px rail | positive tracking |

> ⚠️ CHANEL's density is built from small type, low body weight, uppercase controls, and exact line-height. Enlarging text to generic SaaS sizes breaks the luxury ratio.

### Principles

1. Body copy is light, not casual — weight `300` gives the interface air while the logo supplies authority.
2. Controls are uppercase with positive tracking. This is not optional decoration; it is how CHANEL turns links into house signage.
3. Display contrast comes more from image scale and wordmark placement than from giant marketing H1 text.
4. Locale fallbacks are part of the system. The CSS carries Arabic, Chinese, Japanese, Korean, Thai, and Vietnamese font branches to keep the brand voice consistent.
5. Heavy weights exist, but they are reserved for controls and emphatic labels. Paragraphs should not drift into 500/600.
6. Underlines use a measured offset (`0.125rem`) and `200ms` text-decoration-color transition, keeping links precise rather than animated.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (4 steps)

| Token | Hex |
|---|---|
| `--chanel-color-brand-25` | `#F9F9F9` |
| `--chanel-color-brand-300` | `#767676` |
| `--chanel-color-brand-600` | `#000000` |
| `--chanel-color-brand-900` | `#1D1D1D` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--chanel-inverted-bg` | `#000000` |
| `--chanel-inverted-text` | `#FFFFFF` |
| `--chanel-inverted-hover` | `#F1F1F1` |

### 06-3. Neutral Ramp

| Step | Light | Dark / Text |
|---|---|---|
| 0 | `#FFFFFF` | `#000000` |
| 25 | `#F9F9F9` | `#1D1D1D` |
| 50 | `#F1F1F1` | `#333333` |
| 100 | `#ECECEC` | `#454545` |
| 200 | `#D8D8D8` | `#767676` |
| 300 | `#B6B6B6` | `#949494` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Error | alert | `#CD0000` |
| Error bright | alert emphasis | `#FF2A2A` |
| Success | positive state | `#00D03A` |
| Green support | alternate positive | `#68B631` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--search-background-color` | `#FFFFFF` | search and overlay base |
| `--search-text-color` | `#333333` | search body text |
| `--search-black-color` | `#000000` | black control state |
| `--search-primary-button-text` | `#F9F9F9` | black button text |
| `--search-dark-gray` | `#767676` | muted state |
| `--search-light-gray-color` | `#ECECEC` | dividers and boundaries |
| `--search-disabled-color` | `#D8D8D8` | disabled borders |
| `--search-caret-color` | `#1D1D1D` | input caret |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--active-text-color` | `#1D1D1D` | active navigation text |
| `--inactive-text-color` | `#767676` | inactive navigation text |
| `--background-color` | `#FFFFFF` | nav background |
| `--bottom-line-color` | `#ECECEC` | nav divider |
| `--title-color` | `#1D1D1D` | navigation title |
| `--underline-transition-duration` | `300ms` | link underline behavior |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency signal |
|---|---|---:|
| Surface | `#FFFFFF` | very high |
| Text / active | `#1D1D1D` | very high |
| Brand black | `#000000` | high |
| Muted | `#767676` | high |
| Hover surface | `#F1F1F1` | high |
| Disabled | `#D8D8D8` | high |
| Hairline | `#ECECEC` | high |
| Error | `#CD0000` | medium |

### 06-8. Color Stories

**`{colors.primary}` (`#000000`)** — The brand's authority color. It belongs to the wordmark, black primary buttons, and hard contrast states. Use it sparingly and flat; no gradients, glow, or alpha wash.

**`{colors.surface-base}` (`#FFFFFF`)** — The gallery floor. It is not warm cream and not gray. White allows product photography to define the season while the interface remains seasonless.

**`{colors.text-primary}` (`#1D1D1D`)** — The readable black. CHANEL avoids pure `#000000` for many text states, giving labels slightly less glare while preserving the monochrome look.

**`{colors.hairline}` (`#ECECEC`)** — The quiet structure color. It appears as navigation bottom lines and subtle separation, doing the work that borders, shadows, and cards would do on less disciplined sites.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `nav-height` | `3.125rem` / 50px | horizontal category rail |
| `nav-x-padding` | `1.125rem` / 18px | nav edge padding |
| `nav-gap` | `1.125rem` / 18px | category spacing |
| `underline-offset` | `0.125rem` / 2px | text link underlines |
| `product-max-width-sm` | `20.313rem` | product card width |
| `product-max-width-md` | `20.938rem` | eyewear/product module width |
| `product-max-width-lg` | `30.438rem` | larger product module width |
| `icon-button` | `1.875rem` / 30px | circular product action buttons |

**주요 alias**:
- `--gap` → `0px` for tight carousel/grid repetitions.
- `--oab-btn-width` → `calc(100% - 20px)` for bottom action button width.

### Whitespace Philosophy

CHANEL whitespace is not generous in a soft lifestyle way. It is architectural. The header is compact and controlled, while the hero photograph is allowed to fill and crop with almost no explanatory framing. The page gives air to brand and product, not to UI furniture.

Below the hero, grids compress more aggressively. Product modules cap their widths, actions sit directly on image surfaces, and gaps can be zero in carousel contexts. The rhythm is "ceremonial entry, commercial precision."

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `button-radius` | `0px` | primary/secondary rectangular buttons |
| `card-radius` | `0px` | product/card chrome |
| `icon-circle` | `50%` | eyewear try-on and wishlist buttons |
| `form-radius` | `0px` | square input geometry unless native control overrides |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| Chrome | `none` | navigation, cards, buttons |
| Product image | photography-defined | depth comes from the asset, not CSS box-shadow |
| Overlay icon | `none` + translucent `rgba(255,255,255,.6)` | product action buttons |

Pattern: CHANEL avoids elevation shadows in UI chrome. If depth is needed, it is embedded in campaign photography or produced by white/black contrast.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `nav-height-transition` | `height .3s cubic-bezier(0.65, 0, 0.35, 1)` | hide/reveal navigation rail |
| `nav-transform-transition` | `transform .3s ease .05s` | slide category nav vertically |
| `link-underline` | `text-decoration-color .2s ease` | link hover/focus treatment |
| `underline-duration` | `300ms` | navigation underline timing |

Motion principle: transitions are functional and quiet. No bounce, parallax, cursor gimmicks, or animated gradients.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: product modules observed around `20.313rem`, `20.938rem`, and `30.438rem`; global hero is full-bleed.
- **Grid type**: CSS Grid for utility/product grid (`repeat(var(--grid-columns, 5), 1fr)`), Flexbox for nav and product card internals.
- **Column count**: default grid variable `5`, with responsive CSS altering layout by viewport.
- **Gutter**: variable `--gap`, often `0px` in carousel-like contexts.

### Hero
- **🆕 Pattern Summary**: full-width campaign image crop + centered wordmark + compact horizontal nav + minimal/no copy above the fold.
- Layout: one dominant image plane with top institutional header.
- Background: product/campaign photography on `#FFFFFF`/pale neutral field.
- **🆕 Background Treatment**: image crop, not CSS decoration. In the screenshot, the N°5 bottle and model crop past the right edge while the left side leaves large pale space.
- H1: campaign image text, not HTML H1 in the sampled hero; brand wordmark acts as visual title.
- Max-width: viewport-wide hero image plane.

### Section Rhythm
```css
section {
  padding: 0;
  max-width: 100%;
}
.Navigation_nav__O161B {
  height: 3.125rem;
  padding: 0 1.125rem;
  gap: 1.125rem;
}
```

### Card Patterns
- **Card background**: transparent chrome; product image surface usually carries the visible panel.
- **Card border**: none by default; hairlines are used in navigation and form boundaries.
- **Card radius**: `0px`.
- **Card padding**: minimal; product cards rely on image geometry and caption alignment.
- **Card shadow**: none.

### Navigation Structure
- **Type**: two-tier institutional header: centered wordmark + horizontal category nav.
- **Position**: header/nav at top of document; nav module supports hide/reveal transitions.
- **Height**: category rail `3.125rem`.
- **Background**: `#FFFFFF`.
- **Border**: bottom `1px solid #ECECEC`.

### Content Width
- **Prose max-width**: compact text modules; no broad editorial paragraph measured in homepage sample.
- **Container max-width**: product/card modules cap around `325px-487px`; hero is full viewport.
- **Sidebar width**: N/A for homepage; navigation drawers/menus replace sidebar behavior.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `< 600px` | compact navigation, mobile search/input label backgrounds |
| Tablet | `>= 600px and < 960px` | transitional layout, tablet-specific labels |
| Desktop | `> 960px` | full horizontal category navigation |
| Large | `> 960px` plus module-specific widths | product and nav modules expand while preserving strict caps |

### Touch Targets
- **Minimum tap size**: explicit icon actions around `30px`; header buttons likely supplemented by surrounding hit area.
- **Button height (mobile)**: not fully surfaced; infer from `cc-button` line-height and padding patterns.
- **Input height (mobile)**: search variables present, exact rendered input height not captured.

### Collapsing Strategy
- **Navigation**: menu button/drawer exists; desktop exposes horizontal category rail.
- **Grid columns**: `--grid-columns` variable drives repeat count; breakpoints pivot around 600px and 960px.
- **Sidebar**: no persistent sidebar on homepage.
- **Hero layout**: image crop changes by viewport; preserve crop drama rather than fitting the whole product.

### Image Behavior
- **Strategy**: campaign and product imagery dominate; UI should use `object-fit: cover` / controlled crop.
- **Max-width**: product cards have explicit max widths; hero is viewport-wide.
- **Aspect ratio handling**: eyewear product variable `512 / 598` observed; other campaigns likely asset-specific.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

| Variant | Background | Text | Border | Type |
|---|---|---|---|---|
| Primary black | `#000000` | `#F9F9F9` | `#000000` | uppercase rectangular CTA |
| Primary black hover/active | `#767676` | `#FFFFFF` | `#767676` | softened black state |
| Primary white | `#FFFFFF` | `#1D1D1D` | `#FFFFFF` | CTA over dark/image contexts |
| Primary white hover | `#F1F1F1` | `#1D1D1D` | `#F1F1F1` | subtle inversion state |
| Disabled | `#F9F9F9` | `#949494` | `#D8D8D8` | noninteractive |

```html
<button class="cc-button cc-button--primary cc-button--black">
  Discover
</button>
```

Implementation notes:
- Use uppercase.
- Keep border radius at `0px`.
- Use 11-14px type with 500-700 weight and positive tracking.
- Hover should change color, not scale the button.

### Badges

Badges are not a dominant homepage primitive. If needed, make them typographic labels rather than colored pills:

```css
.chanel-label {
  font: 600 11px/16px "abchanel-2022", helvetica, sans-serif;
  letter-spacing: 0.04375rem;
  text-transform: uppercase;
  color: #1D1D1D;
}
```

### Cards & Containers

Product cards are image-led:
- Container: flex column, `max-width` around `20.313rem-30.438rem`.
- Background: transparent or image surface.
- Border: none.
- Radius: `0px`.
- Shadow: none.
- Actions: circular overlay buttons can use `rgba(255,255,255,.6)` with `border-radius: 50%`.

### Navigation

```css
.chanel-nav {
  height: 3.125rem;
  display: flex;
  align-items: center;
  gap: 1.125rem;
  padding: 0 1.125rem;
  background: #FFFFFF;
  border-bottom: 1px solid #ECECEC;
}
.chanel-nav a {
  font: 600 13px/1 "abchanel-2022", helvetica, sans-serif;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #1D1D1D;
}
```

State notes:
- Active text: `#1D1D1D`.
- Inactive text: `#767676` where hierarchy is needed.
- Hide/reveal: height and transform transitions around `300ms`.

### Inputs & Forms

Search/form tokens indicate a monochrome input system:
- Background: `#FFFFFF` or mobile label `#F6F6F6`.
- Text: `#333333`.
- Placeholder: `#707070` or `rgba(142,142,142,1)`.
- Caret: `#1D1D1D`.
- Disabled: `#D8D8D8` / `#949494`.
- Focus axis: `#000000`.

### Hero Section

Hero construction:
- Place the official wordmark in the institutional header, not as a decorative hero caption.
- Use a campaign image large enough to crop.
- Keep UI chrome white and flat.
- Avoid overlay text unless the campaign asset already contains typography.
- Let the first viewport feel like a magazine spread with commerce navigation attached.

### 13-2. Named Variants

| Variant | Spec | State notes |
|---|---|---|
| `button-primary-black` | `#000000` bg, `#F9F9F9` text, square geometry | hover/active `#767676` bg with `#FFFFFF` text |
| `button-primary-white` | `#FFFFFF` bg, `#1D1D1D` text, square geometry | hover `#F1F1F1` |
| `button-disabled` | `#F9F9F9` bg, `#949494` text, `#D8D8D8` border | pointer events disabled |
| `nav-horizontal-category` | 50px rail, `#FFFFFF`, `#ECECEC` bottom hairline | hide/reveal via height + transform |
| `product-overlay-icon` | 30px circle, `rgba(255,255,255,.6)`, black icon | used over product imagery only |
| `search-monochrome-input` | `#FFFFFF` bg, `#333333` text, `#1D1D1D` caret | mobile label may use `#F6F6F6` |

### 13-3. Signature Micro-Specs

```yaml
monochrome-gallery-chrome:
  description: "CHANEL keeps reusable UI chrome in black, white, and hairline gray so campaign photography owns all sensual color."
  technique: "#FFFFFF page surface, #1D1D1D primary text, #ECECEC divider, #000000 brand and CTA states."
  applied_to: ["{component.nav-horizontal}", "{component.button-primary-black}", "{component.button-primary-white}", "{component.product-card}"]
  visual_signature: "A luxury retail interface that feels like gallery signage around a photographed object, with no second brand color in the chrome."

uppercase-house-signage:
  description: "Navigation and controls become house architecture through uppercase, compact type, and measured tracking."
  technique: "11-14px type, 500-700 weight, text-transform: uppercase, positive letter-spacing up to 0.04375rem."
  applied_to: ["{component.nav-horizontal}", "{component.button-primary-black}", "{component.button-primary-white}"]
  visual_signature: "Every clickable label reads as engraved boutique signage rather than ordinary web copy."

campaign-crop-hero:
  description: "The hero treats product photography as a campaign spread that can exceed the browser frame."
  technique: "Viewport-wide image plane, object-fit: cover behavior, minimal overlay UI, centered wordmark/header separated above the image."
  applied_to: ["{component.hero-section}", "{component.nav-horizontal}"]
  visual_signature: "The bottle and model feel larger than the viewport, as if the browser edge is a precision crop mark."

hairline-not-shadow:
  description: "CHANEL separates structure with hairlines and spacing instead of card elevation."
  technique: "border-bottom: 1px solid #ECECEC; card shadow: none; button/card radius: 0px; product image depth remains photography-defined."
  applied_to: ["{component.nav-horizontal}", "{component.product-card}", "{component.search-monochrome-input}"]
  visual_signature: "Luxury appears through the absence of elevation effects; the interface is flat while the image carries depth."

translucent-product-action-disc:
  description: "Product actions sit on photography as quiet utility discs without becoming decorative badges."
  technique: "30px circular icon action, border-radius: 50%, rgba(255,255,255,.6) surface, black icon, no box-shadow."
  applied_to: ["{component.product-overlay-icon}", "{component.product-card}"]
  visual_signature: "A small frosted white control floats on the product image, useful but visually subordinate."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | product/collection name, often terse and uppercase or title case | `THE CHANEL HANDBAG` |
| Primary CTA | direct retail or discovery verb | `Discover`, `Book an Appointment` |
| Navigation | category-first, institutional taxonomy | `Haute Couture`, `Fashion`, `High Jewelry` |
| Subheading | descriptive but brief | `Enter the world of CHANEL...` |
| Tone | ceremonious, controlled, product-led | no playful microcopy |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* CHANEL — copy into your root stylesheet */
:root {
  /* Fonts */
  --chanel-font-family: "abchanel-2022", "helvetica-adjusted-abchanel-2022", helvetica, sans-serif;
  --chanel-font-family-corpo: "abchanel-corpo", "arial-adjusted-abchanel-corpo", arial, sans-serif;
  --chanel-font-weight-normal: 300;
  --chanel-font-weight-bold: 600;

  /* Brand */
  --chanel-color-brand-25:  #F9F9F9;
  --chanel-color-brand-300: #767676;
  --chanel-color-brand-500: #1D1D1D;
  --chanel-color-brand-600: #000000;
  --chanel-color-brand-900: #000000;

  /* Surfaces */
  --chanel-bg-page:    #FFFFFF;
  --chanel-bg-variant: #F9F9F9;
  --chanel-bg-hover:   #F1F1F1;
  --chanel-text:       #1D1D1D;
  --chanel-text-body:  #333333;
  --chanel-text-muted: #767676;
  --chanel-border:     #ECECEC;
  --chanel-disabled:   #D8D8D8;

  /* Key spacing */
  --chanel-nav-height: 3.125rem;
  --chanel-space-sm:   0.625rem;
  --chanel-space-md:   1.125rem;
  --chanel-space-lg:   3.125rem;

  /* Radius */
  --chanel-radius-sm: 0px;
  --chanel-radius-md: 0px;
  --chanel-radius-circle: 50%;
}

body {
  margin: 0;
  font-family: var(--chanel-font-family);
  font-weight: var(--chanel-font-weight-normal);
  color: var(--chanel-text);
  background: var(--chanel-bg-page);
}

.chanel-button {
  min-height: 44px;
  padding: 14px 24px;
  font: 600 12px/18px var(--chanel-font-family);
  letter-spacing: 0.01875rem;
  text-transform: uppercase;
  border-radius: 0;
  transition: color .2s ease, background-color .2s ease, border-color .2s ease;
}

.chanel-button--black {
  color: #F9F9F9;
  background: #000000;
  border: 1px solid #000000;
}

.chanel-button--black:hover {
  color: #FFFFFF;
  background: #767676;
  border-color: #767676;
}

.chanel-nav {
  display: flex;
  align-items: center;
  height: var(--chanel-nav-height);
  gap: var(--chanel-space-md);
  padding: 0 var(--chanel-space-md);
  overflow-x: auto;
  background: #FFFFFF;
  border-bottom: 1px solid #ECECEC;
}

.chanel-nav a {
  font: 600 13px/1 var(--chanel-font-family);
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #1D1D1D;
  text-decoration: none;
  white-space: nowrap;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — CHANEL-inspired token subset
module.exports = {
  theme: {
    extend: {
      colors: {
        chanel: {
          black: '#000000',
          ink: '#1D1D1D',
          body: '#333333',
          muted: '#767676',
          line: '#ECECEC',
          disabled: '#D8D8D8',
          surface: '#FFFFFF',
          surfaceVariant: '#F9F9F9',
          hover: '#F1F1F1',
        },
      },
      fontFamily: {
        sans: ['abchanel-2022', 'Helvetica', 'Arial', 'sans-serif'],
      },
      borderRadius: {
        none: '0px',
        circle: '50%',
      },
      letterSpacing: {
        chanel: '0.04em',
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
| Brand primary | `{colors.primary}` | `#000000` |
| Background | `{colors.surface-base}` | `#FFFFFF` |
| Text primary | `{colors.text-primary}` | `#1D1D1D` |
| Text muted | `{colors.text-muted}` | `#767676` |
| Border | `{colors.hairline}` | `#ECECEC` |
| Disabled | `{colors.disabled}` | `#D8D8D8` |
| Error | `{colors.error}` | `#CD0000` |

### Example Component Prompts

#### Hero Section
```text
CHANEL 스타일 히어로 섹션을 만들어줘.
- 상단: 중앙 CHANEL wordmark, 그 아래 50px 높이의 uppercase category nav
- 배경: #FFFFFF, nav 하단 border #ECECEC
- 이미지: full-bleed campaign photograph, object-fit cover, viewport edge에서 과감하게 crop
- UI 텍스트: 최소화. 제품 사진이 컬러와 감정을 담당하게 둘 것
- 버튼이 필요하면: #000000 bg, #F9F9F9 text, radius 0, uppercase 12px/18px, letter-spacing 0.01875rem
```

#### Card Component
```text
CHANEL 스타일 product card를 만들어줘.
- 배경: transparent 또는 #F9F9F9 image surface
- border/shadow/radius: none / none / 0
- product image가 카드의 80% 이상을 차지
- caption: abchanel-2022, 11-13px, weight 300 또는 600, color #1D1D1D
- action icon: 30px circle, rgba(255,255,255,.6), black icon
```

#### Navigation
```text
CHANEL 스타일 navigation을 만들어줘.
- 전체 배경 #FFFFFF
- wordmark centered, nav rail height 3.125rem
- nav labels uppercase, 13px, weight 600, letter-spacing 0.04em
- category gap 1.125rem
- bottom border 1px solid #ECECEC
- hover는 underline/color change 정도로 제한하고 transform/scale은 쓰지 말 것
```

### Iteration Guide

- **색상 변경 시**: product/campaign color와 UI token을 섞지 말 것. UI는 monochrome이어야 한다.
- **폰트 변경 시**: substitute를 쓰더라도 uppercase tracking과 light body weight를 먼저 맞춘다.
- **여백 조정 시**: nav 50px, 18px gap, product max-width caps를 유지한다.
- **새 컴포넌트 추가 시**: radius/shadow를 추가하기 전에 hairline과 spacing으로 해결한다.
- **다크 모드**: homepage default는 light다. dark surface는 campaign/image context에 한정한다.
- **반응형**: 600px/960px breakpoint rhythm을 따른다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#FFFFFF` as the main interface floor and let product photography carry color.
- Use `#000000` only for hard brand/CTA moments, not as a blanket text color.
- Use `#1D1D1D` for primary readable text and active nav states.
- Use `#ECECEC` hairlines for structure instead of shadows or tinted cards.
- Keep buttons square, uppercase, and high contrast.
- Preserve the 50px category navigation rail and the centered wordmark hierarchy.
- Let hero imagery crop confidently at the viewport edge.
- Use hover states that change color or underline only; keep motion quiet.

### ❌ DON'T

- 배경을 `#FAF4E8` 또는 beige luxury cream으로 두지 말 것 — 대신 `#FFFFFF` 사용.
- 본문 텍스트를 `#000000` 또는 pure black only로 두지 말 것 — 대신 `#1D1D1D` 또는 `#333333` 사용.
- hairline을 `#CCCCCC`처럼 진한 회색으로 두지 말 것 — 대신 `#ECECEC` 사용.
- muted text를 `#999999`로 흐리게 두지 말 것 — 대신 `#767676` 사용.
- primary button hover를 `#222222`로 거의 안 보이게 두지 말 것 — 대신 `#767676` 사용.
- disabled border를 `#EEEEEE`로 너무 약하게 두지 말 것 — 대신 `#D8D8D8` 사용.
- body를 `font-weight: 400`으로 고정하지 말 것 — CHANEL body rhythm은 `300` 중심이다.
- button/nav에 `border-radius: 999px` pill을 쓰지 말 것 — CHANEL controls는 `0px` square geometry다.
- product cards에 `box-shadow`를 넣지 말 것 — depth는 photography가 담당한다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No gold UI palette** — gold/amber exists in fragrance photography, not in reusable interface tokens.
- **No decorative gradients** — there is no gradient-based brand chrome.
- **No pill-button language** — square buttons are the default luxury posture.
- **No card elevation system** — shadows do not define product containers.
- **No playful iconography** — icons are thin utility marks, not expressive illustrations.
- **No rounded SaaS panels** — panels, if present, should be flat and strict.
- **No loud hover animation** — transforms, bounce, and spring motion are absent.
- **No second brand color** — monochrome carries the system; campaign colors stay inside assets.
- **No casual lowercase navigation** — category labels are house signage.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single public homepage capture** — this guide uses the available CHANEL homepage HTML/CSS/screenshot artifacts. Checkout, account, boutique appointment, and full product detail flows were not visited.
- **Campaign asset colors excluded** — amber, red, skin tones, and other photographic colors were intentionally not promoted into UI tokens. They are content, not system color.
- **Exact logo geometry not specified** — the CHANEL wordmark should be treated as an official asset. This document does not recreate its proprietary letterform metrics.
- **Motion JavaScript not fully traced** — CSS transitions were sampled, but scroll-triggered or menu JavaScript choreography was not exhaustively profiled.
- **Mobile rendered screenshot not captured in this pass** — breakpoints come from CSS media query evidence around 600px and 960px plus component inference.
- **Form validation depth limited** — search/input variables and error colors were observed, but full validation, loading, and checkout error states were not walked.
- **Token names are partially inferred** — CHANEL exposes many CSS variables, but not a clean public design-token package. Frontmatter object names are guide aliases mapped to observed hex values.
- **Locale typography is summarized** — many language-specific font stacks exist; this guide captures the core pattern rather than every locale branch.
