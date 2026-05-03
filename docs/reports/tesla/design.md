---
schema_version: 3.2
slug: tesla
service_name: Tesla
site_url: https://www.tesla.com
fetched_at: 2026-05-03
default_theme: mixed
brand_color: "#3E6AE1"
primary_font: "Tesla/TDS base display"
font_weight_normal: "var(--tds-font-weight-regular)"
token_prefix: tds

bold_direction: "Automotive Minimalism"
aesthetic_category: "other"
signature_element: "hero_impact"
code_complexity: "medium"

medium: web
medium_confidence: high
archetype: automotive
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "TDS/TCL class system is visible across nav, carousel, buttons, layout, scrims, and charging-map component variables, but only a small public token subset was exposed in fetched CSS."

colors:
  primary: "#3E6AE1"
  surface-light: "#F4F4F4"
  surface-white: "#FFFFFF"
  text-primary: "#171A20"
  text-muted: "#5C5E62"
  overlay-soft: "#00000040"
typography:
  display: "Tesla/TDS base display"
  body: "Tesla/TDS base display"
  ladder:
    - { token: hero-h1, size: "48px observed", weight: "var(--tds-font-weight-bold)", tracking: "tight optical, exact value not surfaced" }
    - { token: nav-label, size: "14px observed", weight: "var(--tds-font-weight-medium)", tracking: "0" }
    - { token: body, size: "16px assumed from TDS default", weight: "var(--tds-font-weight-regular)", tracking: "0" }
  weights_used: ["var(--tds-font-weight-regular)", "var(--tds-font-weight-medium)", "var(--tds-font-weight-bold)"]
  weights_absent: [300, 800, 900]
components:
  button-primary: { bg: "{colors.primary}", radius: "pill / TDS button radius", padding: "block 12px observed-equivalent" }
  button-secondary-light: { bg: "{colors.surface-white}", fg: "{colors.text-primary}", radius: "pill / TDS button radius" }
  hero-carousel: { bg: "full-bleed media", scrim: "tds-scrim--black", height: "viewport" }
  mega-menu-product: { layout: "image + title + secondary links", class: "dx-mega-menu-product" }
---

# DESIGN.md - Tesla

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Tesla stages each vehicle like a showroom hero on a floor-to-ceiling gallery canvas. The page opens with a viewport-sized automotive media field where `Model Y` sits in white over a pale sky — less like a web banner and more like a showroom delivery door opening onto concrete and daylight. The chrome is deliberately ordinary so the object can look inevitable.

The palette is showroom negative space. #F4F4F4 (`{colors.surface-light}`) and #FFFFFF (`{colors.surface-white}`) are the gallery concrete and glass. #171A20 (`{colors.text-primary}`) is the printed ink on a specification placard, not theatrical black. #3E6AE1 (`{colors.primary}`) is the cashier's order button at the showroom counter, not a brand mural. There is no second UI brand color: red belongs to paint, tail lights, and assets — not to the cockpit control system.

Typography follows the same industrial restraint. The model name reads like badging on the rear of a vehicle: short, centered, mechanically clean, and confident because it has almost no sentence around it. Navigation labels behave like signage above showroom bays, small enough to disappear until needed. Tesla avoids editorial serif contrast, playful weights, and expressive type detail because any flourish would compete with the canvas — the vehicle and the sky are the editorial.

The craft is in controlled staging: full viewport gallery sections, dark or light scrims, carousel dots, small square arrow controls, and CTA groups that remain stable while media changes underneath. Shadow is not a chrome language; depth comes from the photograph. The cockpit of decisions — "Order Now" + "View Inventory" — stays anchored below the headline as the only two instruments on an otherwise cleared showroom floor. The site has almost no self-consciousness as a site: the page machinery keeps running, but the visitor remembers the vehicle, the sky, and the two decisions waiting below.

### Key Characteristics

- Full-bleed automotive media owns the first viewport.
- White top nav creates a clean showroom header above the image field.
- CTA pairing is stable: primary blue order action + white/neutral inventory action.
- Text is centered in hero modules and kept short enough to behave like model badging.
- TDS/TCL class system drives repeated layout, carousel, scrim, and component behavior.
- Neutral surfaces dominate; chromatic UI color is deliberately scarce.
- Section rhythm alternates viewport hero, product card carousel, and constrained two-column modules.
- Rounded corners appear on cards/maps/buttons, but the page avoids bubbly softness.
- Shadows are not a chrome language; depth comes from photography and media layering.
- Navigation is product-category first: Vehicles, Energy, Charging, Discover, Shop.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Automotive Minimalism
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **viewport vehicle media with restrained transactional chrome**으로 기억된다.
> **Code Complexity**: medium — carousel sections, scrims, responsive layout classes, and TDS components are present, but the visible aesthetic avoids heavy custom effects.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Tesla처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Tesla/TDS base display", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: var(--tds-font-weight-regular);
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #F4F4F4;        /* {colors.surface-light} */
  --fg: #171A20;        /* {colors.text-primary} */
}
body {
  background: var(--bg);
  color: var(--fg);
}

/* 3. 브랜드 컬러 */
:root { --brand: #3E6AE1; } /* {colors.primary} */
```

**절대 하지 말아야 할 것 하나**: Tesla를 "red car brand"로 해석해 #CC0000을 primary UI color로 쓰지 말 것. Red appears in vehicle photography/assets; the observed transactional CTA color is #3E6AE1.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.tesla.com` |
| Fetched | 2026-05-03 |
| Extractor | reused phase1 artifacts from `insane-design/tesla` |
| HTML size | 1,606,092 bytes |
| CSS files | 6 files, 24,986 characters combined |
| Token prefix | `tds`, `tcl`, `dx` |
| Method | Existing phase1 JSON + CSS frequency + HTML class structure + hero screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Tesla web shell with server-rendered HTML and component islands; exact framework not proven from allowed artifacts.
- **Design system**: Tesla Design System / TDS visible through `tds-*` classes and CSS variables.
- **CSS architecture**:
  ```text
  tds-*   design-system primitives and components: nav, text, buttons, layout, tabs, scrims
  tcl-*   Tesla content/layout modules: homepage hero carousel, flex modules, dynamic sections
  dx-*    mega-menu/product navigation layer
  cua-*   chat assistant surface and modal component layer
  hmc-*   home/charging map component variables
  ```
- **Class naming**: prefix-scoped utility/component classes such as `tds-site-nav-item-text`, `tcl-flex-module__component`, `dx-mega-menu-product`.
- **Default theme**: mixed. The screenshot begins with white nav + image hero; class names include `tds-scrim--black`, `tds-scrim--white`, and `tds-scrim--light`.
- **Font loading**: CSS references `var(--tds-font-family-base-display)`; concrete font-face file name was not surfaced in the permitted extract.
- **Canonical anchor**: viewport hero carousel with centered model label and paired CTA buttons.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `var(--tds-font-family-base-display)` (Tesla/TDS proprietary or bundled system; exact family unresolved)
- **Code font**: `ui-monospace` fallback only; no code UI is central to the homepage.
- **Weight normal / bold**: `var(--tds-font-weight-regular)` / `var(--tds-font-weight-bold)`

```css
:root {
  --tds-font-family:       var(--tds-font-family-base-display);
  --tds-font-family-code:  ui-monospace, SFMono-Regular, Menlo, monospace;
  --tds-font-weight-normal: var(--tds-font-weight-regular);
  --tds-font-weight-bold:   var(--tds-font-weight-bold);
}
body {
  font-family: var(--tds-font-family);
  font-weight: var(--tds-font-weight-normal);
}
```

### Note on Font Substitutes

- **Tesla/TDS base display** — exact family was not exposed in the permitted CSS summary. Use **Inter** or **SF Pro Display/System UI** as the closest open substitute.
- **Display correction** — use Inter/SF Pro at weight 700 for model names, but keep the line-height compact at about `1.05-1.12`; loose headline line-height makes the label feel like marketing copy instead of product badging.
- **Navigation correction** — use weight 600 or medium equivalent for top nav labels. Weight 400 makes the header too weak against full-bleed photography.
- **Letter spacing** — keep body/nav tracking at `0`; use subtle negative tracking only on large hero labels if the substitute font spreads too wide.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `hero-h1` | 48px observed in screenshot | `var(--tds-font-weight-bold)` | ~1.1 | tight optical, exact value not surfaced |
| `hero-subtitle` | 20px observed | `var(--tds-font-weight-medium)` | ~1.35 | 0 |
| `nav-label` | 14px observed | `var(--tds-font-weight-medium)` | ~1.25 | 0 |
| `button-label` | 14px observed | `var(--tds-font-weight-medium)` | 1 | 0 |
| `body` | 16px assumed TDS default | `var(--tds-font-weight-regular)` | ~1.5 | 0 |

> ⚠️ Typography extractor returned no scale entries, so this table combines screenshot observation, visible class names, and exposed `tds-font-weight-*` references. Exact CSS font sizes for global TDS tokens were not surfaced in the permitted extract.

### Principles

1. Hero text is a product label, not an editorial headline. Keep it short, centered, and mechanically clean.
2. Medium weight is structural. Navigation, CTA labels, and secondary hero lines rely on medium weight rather than color.
3. Weight 300 is absent from the visible page posture. Do not make Tesla feel airy or fashion-editorial.
4. Weight 800/900 is also absent. Tesla's boldness comes from media scale, not extra-black type.
5. Body typography should never compete with the image. If copy grows, reduce density before adding type contrast.
6. Links and CTAs should preserve exact casing and compact labels: `Order Now`, `View Inventory`, `Learn`, `Shop`.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed sparse ramp)

| Token | Hex |
|---|---|
| `{colors.primary}` | `#3E6AE1` |
| `vehicle/photo accent - red` | `#CC0000` |
| `system/svg yellow` | `#FBB01B` |
| `system/svg green` | `#12BB00` |

### 06-2. Brand Dark Variant

> N/A - no dark brand ramp was exposed in the permitted CSS/phase1 artifacts. Dark sections appear through scrims and photography rather than a separate blue ramp.

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| `surface-white` | `#FFFFFF` | N/A |
| `surface-light` | `#F4F4F4` | N/A |
| `text-muted` | `#5C5E62` | N/A |
| `text-primary` | `#171A20` | N/A |
| `black-overlay` | `#00000040` | N/A |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| CTA blue | primary | `#3E6AE1` |
| Vehicle red | media/asset only | `#CC0000` |
| Charging/system green | SVG/system asset | `#12BB00` |
| Warning/system yellow | SVG/system asset | `#FBB01B` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `{colors.primary}` | `#3E6AE1` | Primary order CTA |
| `{colors.surface-white}` | `#FFFFFF` | Top nav, secondary CTA, light chrome |
| `{colors.surface-light}` | `#F4F4F4` | Page/section neutral floor |
| `{colors.text-primary}` | `#171A20` | High-contrast dark text |
| `{colors.text-muted}` | `#5C5E62` | Muted supporting text |
| `{colors.overlay-soft}` | `#00000040` | Overlay/scrim-like shadow or SVG opacity candidate |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--tds-theme-background` | unresolved in allowed CSS | chat/modal/theme backgrounds |
| `--tds-theme-background-container` | unresolved in allowed CSS | chat footer/container surfaces |
| `--tds-theme-background-container-alt` | unresolved in allowed CSS | response bubble alternate surface |
| `--tds-size--1x` | unresolved in allowed CSS | button/map/card radius and spacing |
| `--tds-size--2x` | unresolved in allowed CSS | component padding and chat spacing |

### 06-7. Dominant Colors (실제 DOM/CSS 빈도 순)

| Token | Hex | Frequency / role |
|---|---|---|
| `surface-white` | `#FFFFFF` | 15, mostly SVG/pattern assets |
| `surface-light` | `#F4F4F4` | 10, neutral |
| `black` | `#000000` | 7, SVG/pattern assets |
| `system-yellow` | `#FBB01B` | 4, SVG/pattern assets |
| `system-green` | `#12BB00` | 3, SVG/pattern assets |
| `text-primary` | `#171A20` | 3, SVG/pattern assets / TDS ink candidate |
| `vehicle-red` | `#ED4E3B` | 3, SVG/pattern assets |
| `cta-blue` | `#3E6AE1` | 2, SVG/pattern assets / CTA candidate |

### 06-8. Color Stories

**`{colors.primary}` (#3E6AE1)** — The transactional blue. Use it for `Order Now` and other primary actions only. Do not wash sections or gradients with it; Tesla's brand presence comes from vehicle media, not blue decoration.

**`{colors.surface-light}` (#F4F4F4)** — The showroom floor. It is close to white but not pure white, allowing cards and media modules to sit in a softer industrial environment.

**`{colors.text-primary}` (#171A20)** — Tesla's high-contrast ink. It reads black at a glance but is slightly softened, matching the low-noise product-label posture.

**`{colors.surface-white}` (#FFFFFF)** — Chrome and secondary action surface. It is appropriate for the nav bar and white pill buttons, especially over photography, but it should not become the whole page background by default.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--tds-size--half` | unresolved | small radius/padding fragments |
| `--tds-size--1x` | unresolved, appears frequently | button radius, map radius, gap |
| `--tds-size--2x` | unresolved, appears frequently | component padding and chat spacing |
| `--tds-size--3x` | unresolved | larger radius/padding |
| `--tds-size--4x` | unresolved | medium section gaps |
| `--tds-size--5x` | unresolved | larger component padding/gaps |
| `--tds-size--6x` | unresolved | wide CTA/button horizontal padding candidate |

**주요 alias**:
- `--hmc-charging-map-component__map-button-margin` -> `10px` (map button offset)
- `--hmc-charging-map-component__desktop-height` -> `550px` (charging map desktop height)
- `--hmc-charging-map-component__tablet-height` -> `450px` (charging map tablet height)
- `--hmc-charging-map-component__phone-height` -> `400px` (charging map phone height)

### Whitespace Philosophy

Tesla spacing is not a tiny 4px craft system in the visible homepage. It is a viewport staging system. The first decision is "give the vehicle the entire screen," then place the headline and CTAs in a stable center lane. The empty sky in the screenshot is not wasted space; it is the top margin that makes the vehicle feel large without making the UI loud.

Below the hero, the HTML shows product card carousels and constrained two-column modules. That means Tesla alternates cinematic air with tighter shopping modules: open reveal, then structured comparison, then another media-forward card. Do not make every section equally padded. The rhythm should move from full-screen impact to compact product decisions.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--tds-size--1x` | unresolved | most common radius for map/card-like modules |
| `--tds-size--half` | unresolved | small control radius |
| `--tds-border-radius--pill` | unresolved | pill CTA and compact button form |
| `50%` | exact | circular icon buttons / carousel controls |
| `--tds-size--3x` | unresolved | larger card/container radius |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| overlay-soft | `#00000040` | soft overlay/opacity candidate found in CSS frequency |
| chrome-shadow | N/A | no clear multi-layer shadow token surfaced |
| media-depth | photography/video only | perceived depth comes from image composition, not UI box-shadow |

---

## 10. Motion
<!-- SOURCE: manual -->

| Token | Value | Usage |
|---|---|---|
| carousel-slide | JS/CSS behavior not fully surfaced | homepage hero carousel and freeflow product carousel |
| tab-dots | `tds-tab-list--dots` | carousel pagination |
| video-hero | `tds-video-player` / `tcl-react-video` classes | moving hero media |
| chat-typing | typing bullet classes | assistant/chat surface, not core homepage visual language |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `1440px` appears in CSS; `800px` appears for close confirmation/modal surface.
- **Grid type**: mixed Flexbox/Layout classes; visible HTML includes `tds-layout`, `tds-layout-2col`, `tds-layout-2col-has_main`, and `tcl-layout--one-column`.
- **Column count**: one-column hero, two-column constrained modules, freeflow carousel card lanes.
- **Gutter**: based on TDS size variables; `gap: var(--tds-size--1x)` is most frequent, with `--tds-size--4x` and `--tds-size--5x` for larger gaps.

### Hero

- **🆕 Pattern Summary**: `100vh + full-bleed vehicle media/video + centered H1/subtitle + dual CTA below`.
- Layout: centered overlay content on a full viewport media carousel.
- Background: product photography/video, not gradient or abstract illustration.
- **🆕 Background Treatment**: `image/video overlay + tds-scrim--black` on dark/media slides; screenshot shows pale sky with white text and vehicle composition below the fold.
- H1: `48px observed` / weight `var(--tds-font-weight-bold)` / tracking `tight optical`.
- Max-width: content is visually centered; exact hero text max-width not surfaced.

### Section Rhythm

```css
section {
  padding: var(--tds-size--5x) var(--tds-size--6x);
  max-width: 1440px;
}
```

The snippet above is a practical reconstruction from observed CSS values, not a single canonical Tesla rule. The actual page uses viewport modules, `tds-content_container`, `tcl-section-padding`, constrained layout classes, and carousel containers.

### Card Patterns

- **Card background**: image/media first; light cards use `tds-scrim--light` or white/neutral surfaces.
- **Card border**: no strong card border language surfaced.
- **Card radius**: `var(--tds-size--1x)` for many module/map-like surfaces; rounded dynamic sections are visible in class names.
- **Card padding**: `var(--tds-size--2x)` and `var(--tds-size--3x)` appear repeatedly.
- **Card shadow**: no clear shadow token; use image contrast and surface separation.

### Navigation Structure

- **Type**: horizontal product-category nav with mega-menu panels.
- **Position**: top shell navigation; screenshot shows fixed/stable white bar at top.
- **Height**: 56px observed in screenshot.
- **Background**: `#FFFFFF`.
- **Border**: no visible bottom border in screenshot.

### Content Width

- **Prose max-width**: not a core homepage pattern; copy is short and module-bound.
- **Container max-width**: `1440px` surfaced in CSS.
- **Sidebar width**: N/A for homepage; aside appears in two-column layout classes, not as persistent sidebar navigation.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `<600px` | CSS contains `max-width: 599px` portrait rule and mobile carousel/card handling. |
| Tablet | `min-width: 600px` | repeated media query; charging map height rises to 450px. |
| Desktop | `min-width: 900px` | layout enhancement breakpoint surfaced once. |
| Large | `min-width: 1200px` | repeated media query; desktop layout/carousel tuning. |

### Touch Targets

- **Minimum tap size**: visually at least 40px for CTA buttons; exact TDS token unresolved.
- **Button height (mobile)**: not directly surfaced; screenshot desktop buttons are ~40px tall.
- **Input height (mobile)**: not observed on homepage.

### Collapsing Strategy

- **Navigation**: likely collapses product nav into mobile menu; desktop screenshot shows horizontal categories.
- **Grid columns**: `tds-layout-2col` / `tcl-layout--vertical-tablet` imply two-column modules collapse vertically.
- **Sidebar**: no persistent sidebar on homepage.
- **Hero layout**: content remains centered over media; CTA group likely stacks or full-widths on narrow viewports.

### Image Behavior

- **Strategy**: full-bleed responsive media, with video/image background modules.
- **Max-width**: media owns viewport width; contained modules use TDS containers.
- **Aspect ratio handling**: hero is viewport-based; product cards crop media through module containers.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA - `tcl-button tds-btn tds-btn--primary`**

| Property | Value |
|---|---|
| Background | `#3E6AE1` |
| Text | `#FFFFFF` |
| Radius | pill / TDS button radius |
| Height | ~40px observed |
| Padding | wide horizontal, equal pair with secondary |
| State | hover/focus not surfaced; preserve stable fill rather than animated color shifts |

```html
<a class="tcl-button tds-btn tds-btn--primary">Order Now</a>
```

**Secondary CTA - light inventory button**

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#171A20` |
| Radius | pill / TDS button radius |
| Height | matches primary |
| Padding | same width family as primary |

```html
<a class="tcl-button tds-btn">View Inventory</a>
```

### Badges

Tesla homepage does not foreground badge components in the captured hero. Treat badge-like labels as compact product/status text, not colored pills.

| Property | Value |
|---|---|
| Background | usually none |
| Text | `#171A20` or white over scrim |
| Weight | medium |
| Radius | avoid unless the badge is a functional control |

### Cards & Containers

**Product card carousel - `tcl-flex-module--product_card_carousel_slide`**

| Property | Value |
|---|---|
| Background | full image/video media |
| Overlay | `tds-scrim--black` on dark media cards |
| Radius | section/card radius visible through dynamic rounded sections |
| Copy position | title/top container + bottom heading/CTA container |
| Shadow | none as chrome; image contrast supplies depth |

**Light dynamic section - `tcl-dynamic-section tcl-dynamic-section--rounded-corners`**

| Property | Value |
|---|---|
| Background | `tds-scrim--light` / neutral |
| Radius | rounded corners via dynamic-section class |
| Layout | image container + card text container |
| CTA | one or two TDS buttons |

### Navigation

**Top nav - `tds-site-nav` family**

| Property | Value |
|---|---|
| Background | `#FFFFFF` in screenshot |
| Height | ~56px |
| Center links | Vehicles, Energy, Charging, Discover, Shop |
| Right icons | help, globe, account |
| Label class | `tds-site-nav-item-text` |
| Mega menu | `dx-mega-menu` panels with product cards and secondary links |

```html
<nav class="tds-site-nav">
  <a class="tds-site-nav-item-text">Vehicles</a>
  <a class="tds-site-nav-item-text">Energy</a>
  <a class="tds-site-nav-item-text">Charging</a>
</nav>
```

### Inputs & Forms

Homepage form states were not surfaced. The fetched CSS includes chat form/modal variables such as `--cua-chat-max-form-width: 500px`, `--cua-chat-bubble-padding`, and theme background aliases. Do not invent Tesla form validation colors from this homepage extract.

| State | Observed |
|---|---|
| Default input | not observed |
| Focus | not observed |
| Error | not observed |
| Loading | chat typing classes observed, not general forms |

### Hero Section

**Homepage hero carousel - `tcl-flex-module-carousel--homepage_hero_carousel`**

| Property | Value |
|---|---|
| Height | viewport |
| Media | `tcl-react-video`, background image/video |
| Scrim | `tds-scrim--black` on media modules |
| Alignment | centered text and CTAs |
| CTA group | `tcl-button-group tcl-button-group--flex` |
| Pagination | `tds-tab-list--dots` |
| Controls | square arrow buttons at left/right in screenshot |

### 13-2. Named Variants

**button-primary-order** — Blue transactional CTA for purchase intent.

| Property | Value |
|---|---|
| Class | `tcl-button tds-btn tds-btn--primary` |
| Background | `#3E6AE1` |
| Foreground | `#FFFFFF` |
| Copy | short verb phrase: `Order Now` |
| Scope | hero and product decision modules |

**button-secondary-inventory** — White/neutral companion CTA.

| Property | Value |
|---|---|
| Class | `tcl-button tds-btn` or related secondary button class |
| Background | `#FFFFFF` |
| Foreground | `#171A20` |
| Copy | `View Inventory`, `Learn`, `Shop` |
| Scope | paired with primary CTA, never more visually dominant |

**hero-carousel-slide** — Full media product reveal module.

| Property | Value |
|---|---|
| Class | `tcl-flex-module-carousel__slide` |
| Media | background video/image |
| Content | centered heading/subheading/button group |
| State | active slide class: `tcl-flex-module-carousel__slide--active` |

**mega-menu-product-card** — Navigation product chooser.

| Property | Value |
|---|---|
| Class | `dx-mega-menu-product` |
| Structure | asset + title + product links |
| Count | panels show product counts such as 7, 4, 5 |
| Visual role | fast product browsing, not marketing decoration |

### 13-3. Signature Micro-Specs

#### viewport-media-showroom

```yaml
viewport-media-showroom:
  description: "The homepage hero behaves like a full-scale vehicle reveal, not a cropped marketing banner."
  technique: "viewport-height media carousel using tcl-flex-module-carousel--homepage_hero_carousel, tcl-react-video/background media, centered copy, and stable tcl-button-group tcl-button-group--flex"
  applied_to: ["{component.hero-carousel}", "tcl-flex-module-carousel--homepage_hero_carousel"]
  visual_signature: "The car becomes the interface; text and buttons read like a minimal caption layer on a showroom wall."
```

#### scrim-controlled-legibility

```yaml
scrim-controlled-legibility:
  description: "Media contrast is handled by system scrim classes instead of decorative text shadows."
  technique: "tds-scrim--black, tds-scrim--white, and tds-scrim--light applied per slide/card context; soft overlay candidate #00000040 /* {colors.overlay-soft} */"
  applied_to: ["{component.hero-carousel}", "tcl-flex-module--product_card_carousel_slide"]
  visual_signature: "White or dark product text stays readable while the photography remains the depth system."
```

#### transactional-blue-pill-pair

```yaml
transactional-blue-pill-pair:
  description: "Buying and browsing actions share geometry while color alone marks purchase intent."
  technique: "paired tcl-button tds-btn controls, primary fill #3E6AE1 /* {colors.primary} */, secondary fill #FFFFFF /* {colors.surface-white} */, pill/TDS radius, approximately 40px observed height"
  applied_to: ["{component.button-primary}", "{component.button-secondary-light}", "tcl-button-group"]
  visual_signature: "Two calm showroom decisions sit below the model name; the blue button feels transactional, not decorative."
```

#### product-menu-gallery

```yaml
product-menu-gallery:
  description: "The top navigation opens as a compact product chooser rather than a text sitemap."
  technique: "dx-mega-menu-product groups with asset + title + secondary product links inside product-category panels; desktop nav shell observed at approximately 56px height"
  applied_to: ["{component.mega-menu-product}", "tds-site-nav", "dx-mega-menu"]
  visual_signature: "Vehicles, Energy, and Charging become a small catalog wall embedded in the navigation."
```

#### charging-map-fixed-heights

```yaml
charging-map-fixed-heights:
  description: "Charging modules use explicit responsive map heights rather than letting embedded map content determine rhythm."
  technique: "--hmc-charging-map-component__desktop-height: 550px; --hmc-charging-map-component__tablet-height: 450px; --hmc-charging-map-component__phone-height: 400px; map button margin 10px"
  applied_to: ["hmc-charging-map-component", "charging map modules"]
  visual_signature: "The map keeps the same appliance-like block presence across breakpoints instead of collapsing into a generic embed."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Product name or product capability, extremely short | `Model Y`, `Full Self-Driving (Supervised)` |
| Primary CTA | Direct purchase/intent verb | `Order Now` |
| Secondary CTA | Exploration or inventory action | `View Inventory`, `Learn` |
| Subheading | Offer/status statement, short and numeric when possible | `0% APR Available` |
| Tone | confident, sparse, product-forward | no decorative adjectives needed |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Tesla - copy into your root stylesheet */
:root {
  /* Fonts */
  --tds-font-family:       var(--tds-font-family-base-display, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif);
  --tds-font-family-code:  ui-monospace, SFMono-Regular, Menlo, monospace;
  --tds-font-weight-normal: var(--tds-font-weight-regular, 400);
  --tds-font-weight-medium: var(--tds-font-weight-medium, 600);
  --tds-font-weight-bold:   var(--tds-font-weight-bold, 700);

  /* Brand */
  --tds-color-brand-25:  #F4F4F4;
  --tds-color-brand-300: #A2A3A5;
  --tds-color-brand-500: #3E6AE1;
  --tds-color-brand-600: #3E6AE1;   /* canonical CTA */
  --tds-color-brand-900: #171A20;

  /* Surfaces */
  --tds-bg-page:   #F4F4F4;
  --tds-bg-white:  #FFFFFF;
  --tds-text:      #171A20;
  --tds-text-muted:#5C5E62;
  --tds-overlay:   #00000040;

  /* Key spacing */
  --tds-space-sm:  var(--tds-size--1x, 8px);
  --tds-space-md:  var(--tds-size--2x, 16px);
  --tds-space-lg:  var(--tds-size--5x, 40px);

  /* Radius */
  --tds-radius-sm: var(--tds-size--half, 4px);
  --tds-radius-md: var(--tds-size--1x, 8px);
  --tds-radius-pill: var(--tds-border-radius--pill, 999px);
}

.tesla-hero {
  min-height: 100vh;
  display: grid;
  place-items: start center;
  padding-top: 88px;
  color: #FFFFFF;
  background: #171A20;
  position: relative;
  overflow: hidden;
}

.tesla-hero__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.tesla-hero__content {
  position: relative;
  z-index: 1;
  text-align: center;
}

.tesla-hero__title {
  margin: 0;
  font-family: var(--tds-font-family);
  font-size: clamp(40px, 5vw, 56px);
  line-height: 1.08;
  font-weight: var(--tds-font-weight-bold);
}

.tesla-button-group {
  display: flex;
  justify-content: center;
  gap: var(--tds-space-sm);
  margin-top: 24px;
}

.tesla-button {
  min-width: 200px;
  min-height: 40px;
  border-radius: var(--tds-radius-pill);
  border: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font: inherit;
  font-size: 14px;
  font-weight: var(--tds-font-weight-medium);
}

.tesla-button--primary {
  background: #3E6AE1;
  color: #FFFFFF;
}

.tesla-button--secondary {
  background: #FFFFFF;
  color: #171A20;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js - Tesla-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        tesla: {
          blue: '#3E6AE1',
          ink: '#171A20',
          muted: '#5C5E62',
          floor: '#F4F4F4',
          white: '#FFFFFF',
          overlay: '#00000040',
        },
      },
      fontFamily: {
        sans: ['Inter', 'SF Pro Display', 'system-ui', 'sans-serif'],
      },
      fontWeight: {
        regular: '400',
        medium: '600',
        bold: '700',
      },
      borderRadius: {
        tds: '8px',
        pill: '999px',
      },
      maxWidth: {
        tds: '1440px',
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
| Brand primary | `{colors.primary}` | `#3E6AE1` |
| Background | `{colors.surface-light}` | `#F4F4F4` |
| Text primary | `{colors.text-primary}` | `#171A20` |
| Text muted | `{colors.text-muted}` | `#5C5E62` |
| Border | `neutral hairline` | `#A2A3A5` |
| Success | system/asset green | `#12BB00` |
| Error | system/vehicle red | `#CC0000` |

### Example Component Prompts

#### Hero Section

```text
Tesla 스타일 히어로 섹션을 만들어줘.
- 배경: full-bleed vehicle image/video, viewport height
- H1: Tesla/TDS-like sans, 48-56px, bold, centered, white
- 서브텍스트: white, 20px, medium, short offer copy
- CTA 버튼: primary #3E6AE1 with #FFFFFF text, secondary #FFFFFF with #171A20 text
- 버튼 형태: equal-width pill buttons, about 40px high
- 최대 너비: content centered; media fills width
```

#### Card Component

```text
Tesla 스타일 product card를 만들어줘.
- 배경: vehicle/product image as the card surface
- radius: 8px equivalent or TDS rounded dynamic-section radius
- padding: 16-40px TDS scale
- shadow: none; use media contrast and scrim for separation
- 제목: compact bold sans, white over dark media or #171A20 over light surface
- CTA: small paired TDS buttons, never decorative gradient buttons
```

#### Badge

```text
Tesla 스타일 badge가 필요하면 colored pill 대신 compact product/status label로 처리해줘.
- font: TDS-like sans, 12-14px, medium
- background: none or #FFFFFF only if it is a functional control
- color: #171A20 on light, #FFFFFF on dark media
- radius: only for real controls, not decorative labels
```

#### Navigation

```text
Tesla 스타일 상단 네비게이션을 만들어줘.
- 높이: 약 56px, 배경 #FFFFFF, border 없음
- 로고: 좌측, 검정 단색
- 중앙 링크: Vehicles, Energy, Charging, Discover, Shop
- 링크: 14px, medium, #171A20
- 우측 아이콘: help, globe, account
- mega menu는 product image card + title + secondary links 구조
```

### Iteration Guide

- **색상 변경 시**: #3E6AE1은 CTA에만 사용한다. 섹션 배경이나 장식 그라디언트로 확장하지 말 것.
- **폰트 변경 시**: Inter/SF fallback을 쓰되 hero는 bold, nav/button은 medium, body는 regular로 유지한다.
- **여백 조정 시**: hero는 viewport scale, product modules는 TDS size scale로 구분한다.
- **새 컴포넌트 추가 시**: card chrome보다 media/scrim/CTA geometry를 먼저 맞춘다.
- **다크 모드**: 별도 dark palette를 만들지 말고 media 위 scrim + white text 조합으로 처리한다.
- **반응형**: 600px, 900px, 1200px 근처의 breakpoint를 우선 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use full-bleed vehicle or energy product media as the primary brand carrier.
- Keep CTA geometry stable: paired pill buttons with equal visual weight.
- Use #3E6AE1 only for primary transactional action.
- Keep top navigation white, compact, and product-category oriented.
- Use scrims for media legibility instead of heavy text shadows.
- Preserve short product-label copy: model name, offer, two actions.
- Treat TDS/TCL prefixes as real system evidence; do not rename them into generic tokens.
- Let neutral space and photography do the emotional work.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로만 두지 말 것 — 페이지/섹션 floor에는 `#F4F4F4` 사용.
- 텍스트를 `#000000` 또는 `black`으로 고정하지 말 것 — Tesla ink는 `#171A20`를 기준으로 사용.
- Primary CTA를 `#CC0000`으로 만들지 말 것 — 구매 CTA는 `#3E6AE1` 사용.
- Hero secondary button을 `#F4F4F4`로 흐리게 만들지 말 것 — media 위에서는 `#FFFFFF` button이 맞다.
- Overlay를 완전 black `#000000`으로 덮지 말 것 — 필요한 경우 `#00000040` 같은 soft overlay를 사용.
- Product media를 카드 안의 작은 썸네일로 축소하지 말 것 — hero/product reveal은 full-bleed 또는 large media가 핵심.
- CTA 버튼을 sharp rectangle로 만들지 말 것 — pill/TDS radius 계열을 유지.
- Headline에 serif, playful script, 900 weight를 쓰지 말 것 — TDS-like geometric sans + bold/medium 제한.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second UI brand color: none. Red belongs to vehicles/assets, not the primary interface system.
- Decorative gradients: absent. The site uses real sky, vehicle paint, and photography instead.
- Heavy chrome shadows: absent. Depth is photographic, not box-shadow driven.
- Editorial serif contrast: never. Tesla speaks in product labels and compact sans typography.
- Busy card borders: nearly none in the homepage language. Surface, radius, and media define modules.
- Long marketing paragraphs: absent from the hero. Copy is compressed into model, offer, action.
- Cute illustrations: none. Product rendering/photography is the illustration system.
- Weight 300 and 900 extremes: absent from observed posture. Medium and bold carry hierarchy.
- Decorative badges: absent. Status is expressed as plain compact text or functional controls.
- Brand-wide blue wash: absent. #3E6AE1 is a button/action color, not a wallpaper color.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Token exposure is incomplete** — `typography.json` returned zero scale entries and `brand_candidates.json` had no semantic vars. Typography and sizing include screenshot observation plus visible TDS variable names.
- **CSS custom properties are sparse** — only 23 variables were found in resolved token extraction, many unresolved because global TDS definitions were not present in the fetched CSS subset.
- **Hero screenshot is desktop only** — the observed `Model Y` hero is a 1280x800 desktop capture. Mobile CTA stacking and nav behavior were inferred from breakpoints/classes, not directly viewed.
- **Motion curves not measured** — carousels, video player, tab dots, and chat typing classes are visible, but JS timing/easing was not analyzed.
- **Form states not surfaced** — homepage artifacts exposed chat/modal variables but not full checkout, account, validation, loading, or error form states.
- **Dark palette mapping absent** — dark presentation appears through scrims/media rather than an exposed dark token ramp.
- **Color candidates include SVG/pattern noise** — phase1 marked several frequent colors as `svg_pattern`; UI color decisions therefore prioritize CTA/surface/text roles over raw frequency.
- **Exact proprietary font unresolved** — CSS references `var(--tds-font-family-base-display)` but the concrete font-face name was not available in the permitted extract.
- **Configurator/checkout not included** — vehicle configurator, inventory details, payment flow, and account surfaces may use additional components beyond this homepage analysis.
- **Output path differs from skill default** — user requested `plugins/insane-design/docs/reports/tesla/design.md`; this report intentionally writes there instead of `insane-design/tesla/design.md`.
