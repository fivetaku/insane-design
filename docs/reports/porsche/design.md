---
schema_version: 3.2
slug: porsche
service_name: Porsche
site_url: https://porsche.com
fetched_at: 2026-04-14T01:14:00+09:00
default_theme: mixed
brand_color: "#0E0E12"
primary_font: "Porsche Next"
font_weight_normal: 400
token_prefix: pcom

bold_direction: Monochrome Performance
aesthetic_category: luxury-brand
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high

archetype: automotive
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Porsche Design System web components are present, with pcom/pds/phn variables for grid, spacing, motion, font loading, and header behavior; semantic color tiers were not exposed in the captured CSS."

color_system: monochrome
colors:
  dark-chrome: "#0E0E12"
  dark-chrome-hover: "#1A1A24"
  surface-light: "#FFFFFF"
  hairline-light: "#EEEFF2"
  text-strong: "#000000"
  error-red-observed: "#CC0000"
typography:
  display: "Porsche Next"
  body: "Porsche Next"
  fallback: "'Arial Narrow', Arial, 'Heiti SC', SimHei, sans-serif"
  base_line_height: "calc(6px + 2.125ex)"
  ladder:
    - { token: body, size: "browser default", weight: 400, tracking: "normal" }
    - { token: emphasized, size: "component-defined", weight: 600, tracking: "normal" }
    - { token: display, size: "component-defined", weight: 700, tracking: "normal" }
  weights_used: [400, 600, 700]
  weights_absent: [300, 500, 800, 900]
components:
  header-hero: { height: "4.125rem to 5.125rem", bg: "transparent over imagery", border: "1px solid #EEEFF2 when standard" }
  dark-devtool-panel: { bg: "{colors.dark-chrome}", hover_bg: "{colors.dark-chrome-hover}", radius: "8px" }
  pds-grid: { max_width: "2560px", gutter: "clamp(16px,1.25vw + 12px,36px)" }
  image-hover: { transform: "scale3d(1.05,1.05,1.05)", duration: ".4s to .6s" }
---

# DESIGN.md — Porsche

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Porsche.com is not built around a loud brand color. It behaves like a dark showroom where the vehicle image owns the page and the interface recedes into black glass. The strongest measured UI color is #0E0E12 (`{colors.dark-chrome}`), but the emotional color in the screenshot comes from photography: taillight red, cool blue metal, and the black surface of the car. The system color does not compete with that imagery.

The page is automotive first, luxury second. Its visible hierarchy starts with a full-width vehicle hero, a centered Porsche wordmark, quiet utility icons, and a CTA that sits on top of the photo instead of in a marketing card. It feels like a night showroom after the doors have closed: the room drops away, the paint catches a thin line of light, and the UI becomes the black trim around the car rather than a second object on the stage. The Korean cookie modal temporarily covers the hero in the captured screenshot, but the underlying structure is still clear: the car image is the canvas, and the chrome is intentionally thin.

Porsche does not paint the interface red. There is no second UI brand color waiting behind the curtain; red appears as taillight, brake heat, or fallback error, not as a button costume. #0E0E12 (`{colors.dark-chrome}`) is closer to an instrument-cluster bezel than to plain black: it has just enough surface to hold icons and panels without punching a hole through the photograph.

Porsche Next gives the site its mechanical voice. The captured CSS uses weights 400, 600, and 700, with `line-height: calc(6px + 2.125ex)` and normal tracking. That line-height formula is a signature detail: rather than a generic 1.5, it ties body rhythm to the font's x-height. The effect is precise, narrow, and engineered, like dashboard typography calibrated to be read at speed rather than typography dressed up for a lifestyle brochure.

The design system exposes far more structure in spacing and layout than in color. Grid variables describe 6-column mobile and 14-column desktop regions, spacing tokens scale with `clamp()`, and motion tokens define .25s, .4s, .6s, and 1.2s durations. Porsche's web system is therefore not a token-heavy color kit; it is a compositional kit for photography, grid, motion, and restrained chrome.

The site has very little "site" self-consciousness. The page behaves like a configurator lobby or a catalog wall in a flagship dealer: named grid regions park content in exact bays, the wordmark hangs like a badge above the hood, and the photograph does the chromatic work that gradients or decorative cards would do elsewhere. Shadow is not the luxury signal here; the luxury signal is that the chrome knows when to disappear.

### Key Characteristics

- Full-bleed automotive photography is the primary visual surface.
- #0E0E12 (`{colors.dark-chrome}`) is the dominant UI dark, used for chrome-like panels and controls.
- #FFFFFF (`{colors.surface-light}`) is used as a clean modal/content surface, not as a decorative brand field.
- Porsche Next is the canonical typeface, loaded through the Porsche Design System CDN.
- Weights are deliberately limited to 400, 600, and 700; weight 500 is absent in captured CSS.
- Grid behavior is explicit: 6-column mobile, expanded desktop grid with named regions and safe zones.
- Spacing is fluid via `clamp()`, with large vertical intervals reaching 200px.
- Motion is restrained and mechanical: .25s/.4s/.6s durations plus `cubic-bezier(.25,.1,.25,1)`.
- Image hover scale is exactly `scale3d(1.05,1.05,1.05)`.
- The site does not expose a red UI brand token in the captured CSS; red belongs to photography and error fallback, not primary chrome.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Monochrome Performance
> **Aesthetic Category**: luxury-brand
> **Signature Element**: 이 사이트는 **dark automotive hero imagery with quiet Porsche Design System chrome**으로 기억된다.
> **Code Complexity**: medium — CSS variables, responsive grid regions, web components, and motion tokens are present, but the captured surface avoids heavy decorative effects.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Porsche처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Porsche Next", "Arial Narrow", Arial, "Heiti SC", SimHei, sans-serif;
  font-weight: 400;
  line-height: calc(6px + 2.125ex);
  letter-spacing: normal;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #FFFFFF;
  --fg: #000000;
  --chrome: #0E0E12;
  --hairline: #EEEFF2;
}

/* 3. Porsche composition */
.hero {
  min-height: 100vh;
  background: #0E0E12 center / cover no-repeat;
}
```

**절대 하지 말아야 할 것 하나**: Porsche를 `#CC0000` 빨간 버튼 브랜드로 만들지 말 것. 캡처된 CSS에서 #CC0000은 403 fallback/error 문맥에만 보이며, 실제 홈 UI의 정체성은 #0E0E12 dark chrome + photography다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://porsche.com` |
| Captured page | `포르쉐코리아 - 공식 웹사이트` |
| Fetched | 2026-04-14T01:14:00+09:00 |
| Extractor | Existing phase1 reuse: HTML + CSS + screenshot |
| HTML size | 130,519 bytes |
| CSS files | 3 captured files; `_inline.css` is the only valid primary CSS for analysis |
| Screenshot | `insane-design/porsche/screenshots/hero-cropped.png` |
| Token prefix | `pcom`, `pds`, `phn` |
| Method | Existing phase1 JSON + direct CSS/HTML/screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Astro islands with Porsche Design System web components.
- **Design system**: Porsche Design System — visible custom elements include `p-button`, `p-grid`, `p-heading`, `p-text`, `p-link-tile`, `p-model-signature`, `p-modal`, `p-popover`, `p-tabs`, and form controls.
- **CSS architecture**: Inline PDS bootstrap CSS + CSS modules for page-local shell behavior.
  ```css
  pds   /* grid regions and internal layout variables */
  pcom  /* spacing, motion, image hover scale */
  phn   /* Porsche header/navigation height */
  ```
- **Class naming**: CSS Modules with component hashes, e.g. `.PcomGrid__grid__f560b`, `.DevToolsSidebar__toggleButton__14360`.
- **Default theme**: mixed. Header/hero is dark over image; content and modal surfaces use #FFFFFF.
- **Font loading**: `@font-face` from `https://cdn.ui.porsche.com/porsche-design-system/fonts/`, with `font-display: swap` and script-specific unicode ranges.
- **Canonical anchor**: automotive hero imagery + centered Porsche wordmark + PDS grid.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Porsche Next` (brand/proprietary, loaded from Porsche Design System CDN)
- **Body font**: `Porsche Next`
- **Fallback stack**: `"Arial Narrow", Arial, "Heiti SC", SimHei, sans-serif`
- **Weight normal / bold**: `400` / `700`
- **Observed middle emphasis**: `600`

```css
:root {
  --pcom-font-family: "Porsche Next", "Arial Narrow", Arial, "Heiti SC", SimHei, sans-serif;
  --pcom-font-weight-normal: 400;
  --pcom-font-weight-semi: 600;
  --pcom-font-weight-bold: 700;
}
body {
  font-family: var(--pcom-font-family);
  font-weight: var(--pcom-font-weight-normal);
  line-height: calc(6px + 2.125ex);
  letter-spacing: normal;
}
```

### Note on Font Substitutes

- **Porsche Next** is the correct production face. If it is unavailable, use **Arial Narrow** before Arial to preserve Porsche's compressed, technical stance.
- Keep body at weight 400. Do not substitute with Inter 400 unless the layout is also widened; Inter will make the same text feel rounder and less engineered.
- Preserve `line-height: calc(6px + 2.125ex)` when possible. If the fallback stack cannot support ex-based rhythm cleanly, use `line-height: 1.45` for body copy and tighten display headings manually.
- Do not introduce negative tracking as a global correction. Captured Porsche CSS uses `letter-spacing: normal`; the single `.05em` occurrence belongs to an uppercase internal rule label, not public brand typography.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| body | browser/default component size | 400 | `calc(6px + 2.125ex)` | `normal` |
| emphasis | component-defined | 600 | component/default | `normal` |
| display | component-defined | 700 | component/default | `normal` |
| internal-label | 12px | 600 | default | `.05em` uppercase |

> ⚠️ The captured typography extractor found families and weights but no explicit public scale entries. Treat exact heading sizes as component-owned by Porsche Design System rather than hardcoded global tokens.

### Principles

1. Porsche's voice comes from **font identity + image hierarchy**, not from a large exposed type scale.
2. Body text stays at weight 400. Use 600 for component emphasis and 700 for strong headings or labels only.
3. Weight 500 is absent in the captured CSS. Do not insert medium weight just because many SaaS systems do.
4. Letter spacing is normal by default. Wide tracking is not a Porsche-wide styling rule.
5. The x-height line-height formula is more important than a generic numeric `line-height: 1.5`.
6. The font stack must remain narrow. Replacing it with a round geometric sans changes the brand posture.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp

> N/A — the captured CSS does not expose a multi-step brand ramp. Porsche's public homepage surface is effectively monochrome in CSS, with photography carrying chromatic brand emotion.

| Token | Hex |
|---|---|
| dark-chrome | #0E0E12 |
| dark-chrome-hover | #1A1A24 |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| dark-chrome | #0E0E12 |
| dark-chrome-hover | #1A1A24 |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| surface | #FFFFFF | #0E0E12 |
| hairline | #EEEFF2 | hsla(0,0%,100%,.6) |
| text | #000000 | #FFFFFF |
| fallback-gray | #EEEEEE | #555555 |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| error/fallback only | server error heading | #CC0000 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `{colors.dark-chrome}` | #0E0E12 | dark utility/control panels, black chrome surfaces |
| `{colors.dark-chrome-hover}` | #1A1A24 | hover state for dark utility panels |
| `{colors.surface-light}` | #FFFFFF | cookie modal, light content surfaces, dark-surface text |
| `{colors.hairline-light}` | #EEEFF2 | header border in standard mode |
| `{colors.text-strong}` | #000000 | strong text on light surfaces |
| `observed-error-red` | #CC0000 | 403 fallback/error page, not brand CTA |

### 06-6. Semantic Alias Layer

> N/A — `alias_layer.json` reported zero util, semantic, action, component, or core color tiers. Use the named frontmatter tokens above as guidebook labels, not as claims that these aliases exist in source CSS.

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---|---|
| white | #FFFFFF | 30 |
| dark chrome | #0E0E12 | 20 |
| black | #000000 | 2 |
| dark hover | #1A1A24 | 2 |
| gray | #555555 | 2 |
| error red | #CC0000 | 2 |
| fallback gray | #EEEEEE | 2 |
| hairline | #EEEFF2 | 2 |
| dark blue-black | #0E1418 | 1 |

### 06-8. Color Stories

**`{colors.dark-chrome}` (#0E0E12)** — Porsche's captured UI dark. It should feel like instrument-panel black, not a decorative brand swatch. Use it for header overlays, dark controls, and utility surfaces that sit above photography.

**`{colors.surface-light}` (#FFFFFF)** — The clean modal/content surface. It appears as the cookie panel and text-bearing containers, where white behaves as editorial paper against the dark vehicle image.

**`{colors.text-strong}` (#000000)** — Strong text on light surfaces. Use it sparingly and plainly; Porsche's premium feel comes from the contrast, not from tinted copy.

**`{colors.hairline-light}` (#EEEFF2)** — Quiet separation. It is a header/hairline color, not a card border style to scatter everywhere.

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| `--pcom-spacing-x-small` | `clamp(4px,.25vw + 3px,8px)` | tiny internal gaps |
| `--pcom-spacing-small` | `clamp(8px,.5vw + 6px,16px)` | compact item gaps |
| `--pcom-spacing-medium` | `clamp(16px,1.25vw + 12px,36px)` | grid gap, standard module rhythm |
| `--pcom-spacing-large` | `clamp(32px,2.75vw + 23px,76px)` | section separation |
| `--pcom-spacing-x-large` | `clamp(48px,3vw + 38px,96px)` | major content bands |
| `--pcom-spacing-xx-large` | `clamp(80px,7.5vw + 56px,200px)` | cinematic vertical air |

**주요 alias**:
- `grid-gap` → `clamp(16px,1.25vw + 12px,36px)` (main PDS grid rhythm)
- `header-height` → `4.125rem` to `5.125rem` (responsive navigation shell)

### Whitespace Philosophy

Porsche spacing is fluid and cinematic. It does not step through a simple 4/8/16/32 ladder; it uses `clamp()` to make small controls remain exact while large sections expand toward 76px, 96px, and 200px. That is the difference between an interface grid and a showroom wall.

The hero can afford darkness and empty space because the car image supplies the focal mass. Below the hero, the PDS grid compresses information into precise columns, so the system alternates between "large photographic breath" and "engineered product catalog density."

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| dark utility radius | 8px | internal dark panels, toggles, selectors |
| sidebar handle radius | 8px 0 0 8px | fixed right-side toggle shape |
| modal/content radius | observed in screenshot as modest rounded panel | cookie panel; exact CSS lives inside component/runtime layer and was not exposed in captured CSS |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

> N/A — no public shadow token was exposed in the captured CSS. The visible screenshot relies on photography, overlay darkness, hairlines, and modal surface contrast rather than a documented elevation stack.

---

## 10. Motion
<!-- SOURCE: auto -->

| Token | Value | Usage |
|---|---|---|
| `--pcom-motion-duration-short` | `.25s` | quick UI transition |
| `--pcom-motion-duration-moderate` | `.4s` | standard component/image motion |
| `--pcom-motion-duration-long` | `.6s` | larger transition |
| `--pcom-motion-duration-very-long` | `1.2s` | cinematic/long transition |
| `--pcom-motion-easing-base` | `cubic-bezier(.25,.1,.25,1)` | base timing curve |
| `--pcom-motion-easing-in` | `cubic-bezier(0,0,.2,1)` | entering motion |
| `--pcom-motion-easing-out` | `cubic-bezier(.4,0,.5,1)` | exiting motion |
| `--pcom-image-hover-scale` | `scale3d(1.05,1.05,1.05)` | image hover zoom |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `2560px` global grid max, with desktop safe zone `min(50vw - 880px,400px)`.
- **Grid type**: CSS Grid with named regions: `full`, `wide`, `extended`, `basic`, `narrow`.
- **Column count**: 6 columns below 760px; expanded desktop grid with outer columns, wide/extended/basic/narrow tracks, and an 8-column narrow center.
- **Gutter**: `clamp(16px,1.25vw + 12px,36px)`.

### Hero

- **Pattern Summary**: full-viewport automotive image/video + dark overlay feel + centered Porsche wordmark + CTA over image.
- Layout: image/video-led hero; nav overlays the photographic stage.
- Background: vehicle photography from Storyblok assets; captured hero shows a rear Porsche detail with dark overlay and taillight red.
- **Background Treatment**: image-overlay. The screenshot is darkened enough that top chrome and modal remain readable.
- H1: component-owned by Porsche Design System; captured HTML hero headline is `Macan 4`.
- Max-width: hero imagery itself is full bleed; content aligns to PDS grid.

### Section Rhythm

```css
.PcomGrid__grid__f560b {
  display: grid;
  grid-gap: clamp(16px,1.25vw + 12px,36px);
  max-width: 2560px;
  min-width: 320px;
}
```

### Card Patterns

- **Card background**: primarily image tiles and light surfaces; explicit card token not exposed.
- **Card border**: #EEEFF2 for light header separation; dark utility panels use `1px solid #FFFFFF` or `hsla(0,0%,100%,.6)`.
- **Card radius**: 8px for captured utility controls.
- **Card padding**: compact utility padding `6px 10px`; larger content padding is component-owned.
- **Card shadow**: not exposed in captured CSS.

### Navigation Structure

- **Type**: Porsche header web component; menu left, centered wordmark, utility icons right in screenshot.
- **Position**: relative by default; `phn-header[mode=hero]` becomes absolute over the hero.
- **Height**: responsive: `4.125rem`, `5rem`, `4.5625rem`, `4.75rem`, `5.125rem`.
- **Background**: transparent over hero mode; standard header uses visible border.
- **Border**: `1px solid #EEEFF2` in non-hero header state.

### Content Width

- **Prose max-width**: not exposed as a standalone token.
- **Container max-width**: grid max `2560px`, desktop safe zone capped at 400px.
- **Sidebar width**: internal/dev sidebar panel observed at `230px`; not a public layout recommendation.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Small mobile | 0-479px | header height `4.125rem` |
| Mobile/tablet | 480px | header height changes to `5rem` |
| Tablet | 760px | grid expands from 6-column mobile to named desktop regions; wordmark appears |
| Desktop | 1000px | header height `4.75rem`; image sizing uses desktop assumptions |
| Large desktop | 1300px | header height `5.125rem` |
| Wide | 1920px | safe zone becomes `min(50vw - 880px,400px)` |

### Touch Targets

- **Minimum tap size**: component-owned; explicit tap token not exposed.
- **Button height (mobile)**: component-owned by PDS web components.
- **Input height (mobile)**: component-owned by PDS form components.

### Collapsing Strategy

- **Navigation**: crest on mobile, wordmark on tablet/desktop; menu stays as icon/text affordance.
- **Grid columns**: 6-column mobile, named multi-region grid from 760px.
- **Sidebar**: no public sidebar on homepage; internal panel collapses width to 0.
- **Hero layout**: separate desktop/mobile image assets are present in HTML.

### Image Behavior

- **Strategy**: responsive imagery via Storyblok assets and explicit desktop/mobile variants.
- **Max-width**: `img { max-width: 100%; vertical-align: top; }`.
- **Aspect ratio handling**: source assets include exact dimensions; hover scale token exists for image tiles.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

Porsche public buttons are mostly PDS web components in shadow/runtime code, so the captured CSS does not expose final button internals. Use component tags where possible.

```html
<p-button variant="primary">더 알아보기</p-button>
```

| Spec | Value |
|---|---|
| Font | Porsche Next |
| Weight | 400 or 600 depending on PDS variant |
| Public CTA color | not exposed in captured CSS |
| Dark utility panel button bg | #0E0E12 |
| Dark utility hover | #1A1A24 |
| Radius observed | 8px on utility controls |
| State notes | hover should be subtle; no bounce or decorative color shift |

### Badges

> N/A — no public badge pattern was visible in captured CSS. Do not invent a pill badge system for Porsche unless the target flow exposes one.

### Cards & Containers

```html
<p-link-tile href="/korea/ko/models/911">
  <img src="..." alt="Porsche 911" />
  <span>911 Carrera GTS</span>
</p-link-tile>
```

| Spec | Value |
|---|---|
| Surface | photography first; light content panels use #FFFFFF |
| Border | #EEEFF2 for quiet separation, or no border over imagery |
| Radius | 8px where exposed on controls; image tiles are component-owned |
| Padding | fluid spacing tokens, not arbitrary one-off values |
| Hover | image scale may use `scale3d(1.05,1.05,1.05)` |

### Navigation

```html
<phn-header mode="hero">
  <button>메뉴</button>
  <p-wordmark></p-wordmark>
  <button aria-label="language"></button>
</phn-header>
```

| Spec | Value |
|---|---|
| Height | 4.125rem to 5.125rem |
| Hero mode | absolute, full inline width |
| Alignment | centered Porsche wordmark |
| Border | #EEEFF2 only in standard header mode |
| Mobile | crest shown below 760px; wordmark from 760px |

### Inputs & Forms

PDS form controls are present in the bootstrap selector list (`p-input-*`, `p-select`, `p-textarea`, `p-checkbox`, `p-radio-group`, `p-switch`) but no public form state CSS was captured on the homepage.

| State | Guidance |
|---|---|
| default | use Porsche Design System web component defaults |
| focus | do not invent blue focus rings unless PDS exposes them in the target flow |
| error | #CC0000 appears in fallback/error page context only; validate actual form flow before using it |
| disabled/loading | not observed |

### Hero Section

```html
<section class="porsche-hero">
  <phn-header mode="hero"></phn-header>
  <picture>
    <source media="(max-width: 759px)" srcset="macan-mobile.jpg" />
    <img src="macan-desktop.jpg" alt="Several dynamic shots of a Macan 4 driving through a city at night." />
  </picture>
  <a class="hero-cta" href="/models/macan/">Macan 4 더 알아보기</a>
</section>
```

| Spec | Value |
|---|---|
| Background | full-bleed automotive image/video |
| Overlay | dark enough for chrome readability |
| CTA | sits over image, not inside a feature card |
| Copy | short model-led headline |
| Responsive | separate desktop and mobile image assets |

### 13-2. Named Variants

| Variant | Spec |
|---|---|
| `header-hero` | `phn-header[mode=hero]`, absolute, transparent over photography, height variable |
| `header-standard` | bordered header with #EEEFF2 hairline |
| `dark-utility-panel` | #0E0E12 bg, #FFFFFF border, 8px radius, compact 6px 10px padding |
| `image-link-tile` | image-led tile, hover scale via `--pcom-image-hover-scale` |
| `model-hero-cta` | model-specific CTA over hero imagery; final styling component-owned |

### 13-3. Signature Micro-Specs

```yaml
porsche-next-xheight-rhythm:
  description: "Body rhythm is tied to Porsche Next's x-height instead of a generic unitless line-height."
  technique: "font-family: Porsche Next; font-weight: 400; line-height: calc(6px + 2.125ex); letter-spacing: normal"
  applied_to: ["html", "body", "{typography.body}"]
  visual_signature: "Copy reads like calibrated instrument text: narrow, exact, and engineered rather than soft or editorial."

pds-showroom-grid-regions:
  description: "The layout parks content in named showroom bays instead of using a plain equal-width landing grid."
  technique: "6-column mobile grid; desktop named regions full/wide/extended/basic/narrow; max-width: 2560px; grid-gap: clamp(16px,1.25vw + 12px,36px); wide safe zone min(50vw - 880px,400px)"
  applied_to: [".PcomGrid__grid__f560b", "{components.pds-grid}"]
  visual_signature: "Content lines up like a dealer catalog wall: expansive around photography, exact around product modules."

hero-mode-transparent-wordmark:
  description: "The navigation chrome overlays the vehicle stage instead of occupying a separate white website bar."
  technique: "phn-header[mode=hero]; position: absolute; inset-inline: 0; height: 4.125rem to 5.125rem; transparent over full-bleed imagery"
  applied_to: ["phn-header[mode=hero]", "{components.header-hero}"]
  visual_signature: "The centered wordmark feels like a badge above the hood while controls stay quiet at the edges."

instrument-black-utility-chrome:
  description: "Dark controls use instrument-panel black, with hover and border values kept close to the same material."
  technique: "background: #0E0E12 /* {colors.dark-chrome} */; hover background: #1A1A24 /* {colors.dark-chrome-hover} */; border: 1px solid #FFFFFF or hsla(0,0%,100%,.6); border-radius: 8px; padding: 6px 10px"
  applied_to: ["{components.dark-devtool-panel}", "utility panels", "internal controls"]
  visual_signature: "Black chrome recedes into the hero without becoming pure #000000 or a decorative card surface."

image-only-105-zoom:
  description: "Motion belongs to vehicle/product imagery, not to ornamental card chrome."
  technique: "--pcom-image-hover-scale: scale3d(1.05,1.05,1.05); transition duration .4s to .6s; easing cubic-bezier(.25,.1,.25,1)"
  applied_to: ["{components.image-hover}", "p-link-tile imagery", "image teasers"]
  visual_signature: "The car photograph advances subtly toward the viewer while borders, shadows, and color stay restrained."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | model-first, short, confident | `Macan 4` |
| Primary CTA | direct Korean action, product specific | `Macan 4 더 알아보기` |
| Navigation | minimal utility language | `메뉴`, country/language, profile |
| Catalog copy | product family + drivetrain/character | `압도적인 퍼포먼스의 전기 스포츠카` |
| Tone | technical luxury, not playful marketing | short labels, premium restraint |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Porsche — copy into your root stylesheet */
:root {
  /* Fonts */
  --pcom-font-family: "Porsche Next", "Arial Narrow", Arial, "Heiti SC", SimHei, sans-serif;
  --pcom-font-weight-normal: 400;
  --pcom-font-weight-semi: 600;
  --pcom-font-weight-bold: 700;
  --pcom-line-height-body: calc(6px + 2.125ex);

  /* Monochrome chrome */
  --pcom-color-dark-chrome: #0E0E12;
  --pcom-color-dark-chrome-hover: #1A1A24;
  --pcom-color-surface-light: #FFFFFF;
  --pcom-color-text-strong: #000000;
  --pcom-color-hairline: #EEEFF2;

  /* Fluid spacing */
  --pcom-spacing-x-small: clamp(4px,.25vw + 3px,8px);
  --pcom-spacing-small: clamp(8px,.5vw + 6px,16px);
  --pcom-spacing-medium: clamp(16px,1.25vw + 12px,36px);
  --pcom-spacing-large: clamp(32px,2.75vw + 23px,76px);
  --pcom-spacing-x-large: clamp(48px,3vw + 38px,96px);
  --pcom-spacing-xx-large: clamp(80px,7.5vw + 56px,200px);

  /* Motion */
  --pcom-motion-duration-short: .25s;
  --pcom-motion-duration-moderate: .4s;
  --pcom-motion-duration-long: .6s;
  --pcom-motion-duration-very-long: 1.2s;
  --pcom-motion-easing-base: cubic-bezier(.25,.1,.25,1);
  --pcom-motion-easing-in: cubic-bezier(0,0,.2,1);
  --pcom-motion-easing-out: cubic-bezier(.4,0,.5,1);
  --pcom-image-hover-scale: scale3d(1.05,1.05,1.05);

  /* Radius */
  --pcom-radius-control: 8px;
}

body {
  margin: 0;
  font-family: var(--pcom-font-family);
  font-weight: var(--pcom-font-weight-normal);
  line-height: var(--pcom-line-height-body);
  letter-spacing: normal;
  color: var(--pcom-color-text-strong);
  background: var(--pcom-color-surface-light);
}

.porsche-hero {
  min-height: 100vh;
  background-color: var(--pcom-color-dark-chrome);
  background-position: center;
  background-size: cover;
}

.porsche-grid {
  display: grid;
  gap: var(--pcom-spacing-medium);
}

.porsche-image-tile img {
  max-width: 100%;
  vertical-align: top;
  transition: transform var(--pcom-motion-duration-moderate) var(--pcom-motion-easing-base);
}

.porsche-image-tile:hover img {
  transform: var(--pcom-image-hover-scale);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Porsche-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        porsche: {
          chrome: '#0E0E12',
          chromeHover: '#1A1A24',
          surface: '#FFFFFF',
          text: '#000000',
          hairline: '#EEEFF2',
        },
      },
      fontFamily: {
        sans: ['Porsche Next', 'Arial Narrow', 'Arial', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        semibold: '600',
        bold: '700',
      },
      borderRadius: {
        porscheControl: '8px',
      },
      transitionDuration: {
        porscheShort: '.25s',
        porsche: '.4s',
        porscheLong: '.6s',
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
| Brand primary | `{colors.dark-chrome}` | #0E0E12 |
| Background | `{colors.surface-light}` | #FFFFFF |
| Text primary | `{colors.text-strong}` | #000000 |
| Text muted | measured fallback gray | #555555 |
| Border | `{colors.hairline-light}` | #EEEFF2 |
| Hover dark | `{colors.dark-chrome-hover}` | #1A1A24 |
| Error | observed fallback only | #CC0000 |

### Example Component Prompts

#### Hero Section
```text
Porsche 스타일 자동차 히어로 섹션을 만들어줘.
- 배경: full-bleed vehicle photography/video over #0E0E12
- 레이아웃: centered Porsche-style wordmark/nav chrome, CTA over image
- 폰트: Porsche Next fallback stack, body weight 400, display weight 700
- 텍스트: white over dark image, but do not invent red UI accents
- 움직임: image hover or reveal uses .4s-.6s and cubic-bezier(.25,.1,.25,1)
- 그리드: PDS-like fluid grid with clamp(16px,1.25vw + 12px,36px) gutter
```

#### Card Component
```text
Porsche 스타일 이미지 링크 타일을 만들어줘.
- 카드는 사진이 주인공: border/shadow를 최소화
- hover: image transform scale3d(1.05,1.05,1.05)
- spacing: clamp 기반 pcom spacing 사용
- 텍스트: Porsche Next, 400/600만 사용
- 배경 chrome이 필요하면 #0E0E12, hover는 #1A1A24
```

#### Navigation
```text
Porsche 스타일 상단 네비게이션을 만들어줘.
- hero mode에서는 position absolute, full width, dark image 위에 얹기
- 높이: 4.125rem~5.125rem 반응형
- 좌측: 메뉴, 중앙: Porsche wordmark, 우측: language/profile utilities
- standard mode border는 #EEEFF2 1px hairline
- 장식적 색상/그라디언트 금지
```

#### Cookie / Modal Surface
```text
Porsche 스타일 쿠키 모달을 만들어줘.
- surface: #FFFFFF
- text: #000000, font Porsche Next, weight 400/600
- button primary: black/dark chrome, not red
- panel radius: modest, content width broad and calm
- background hero remains visible but dimmed
```

### Iteration Guide

- **색상 변경 시**: UI brand red를 만들지 말고 #0E0E12/#FFFFFF/#000000/#EEEFF2 축을 유지한다.
- **폰트 변경 시**: `Porsche Next`가 없으면 `"Arial Narrow"`를 우선 fallback으로 쓴다.
- **여백 조정 시**: `--pcom-spacing-*` clamp 값을 유지한다. 13px, 27px 같은 임의 값은 피한다.
- **이미지 추가 시**: 사진이 주인공이다. 카드 장식보다 crop, overlay, hover scale을 먼저 조정한다.
- **반응형 작업 시**: 760px에서 grid/header 전환이 크다. mobile/desktop image asset을 분리한다.
- **모션 추가 시**: `.25s`, `.4s`, `.6s`, `1.2s` 토큰 중 하나를 선택하고, 과한 bounce/ease-out back은 쓰지 않는다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use full-bleed automotive photography as the visual anchor.
- Keep the UI palette monochrome: #0E0E12, #FFFFFF, #000000, #EEEFF2.
- Use Porsche Next with the exact fallback order `"Arial Narrow", Arial, "Heiti SC", SimHei, sans-serif`.
- Preserve `line-height: calc(6px + 2.125ex)` for body rhythm.
- Use fluid spacing tokens such as `clamp(16px,1.25vw + 12px,36px)`.
- Let images move subtly with `scale3d(1.05,1.05,1.05)` rather than animating card chrome.
- Align layouts to a named-region grid instead of a generic equal card grid.
- Treat red as photography/error context unless a target Porsche flow exposes an actual red UI token.

### ❌ DON'T

- 배경 chrome을 `#000000` 또는 `black`으로만 두지 말 것 — 대신 `#0E0E12` 사용.
- hover dark surface를 `#222222` 또는 `#111111`로 임의 대체하지 말 것 — 대신 `#1A1A24` 사용.
- light surface border를 `#DDDDDD`로 두지 말 것 — 대신 `#EEEFF2` 사용.
- text on light를 `#333333` 중심으로 흐리게 만들지 말 것 — 강한 본문은 `#000000` 사용.
- Porsche primary CTA를 `#CC0000` 빨강으로 만들지 말 것 — 캡처상 #CC0000은 fallback/error 문맥이며, public homepage chrome은 monochrome이다.
- body에 `font-weight: 500` 사용 금지 — 캡처된 weights는 400, 600, 700이다.
- body line-height를 `1.5`로 단순화하지 말 것 — `calc(6px + 2.125ex)`가 Porsche Next의 리듬이다.
- 모든 카드를 12px/16px radius의 SaaS 카드로 만들지 말 것 — 노출된 control radius는 8px이고, 주요 표면은 사진이다.
- hero를 split text/media card layout으로 만들지 말 것 — Porsche hero는 vehicle photography가 full-bleed canvas다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **Second UI brand color: absent.** Captured CSS does not expose a secondary brand palette for UI.
- **Public red CTA system: absent.** #CC0000 appears only in fallback/error CSS, not as the homepage brand action color.
- **Weight 500: absent.** The captured font weights are 400, 600, and 700.
- **Global negative tracking: absent.** Letter spacing is normal except an internal uppercase label.
- **Gradient token system: absent.** The homepage relies on vehicle photography and overlays, not gradient meshes.
- **Heavy shadow elevation: absent.** No public shadow ramp is exposed in captured CSS.
- **Decorative rounded SaaS cards: absent.** Image-led tiles and PDS components carry structure.
- **Generic 12-column-only grid: absent.** Porsche uses named grid regions and safe zones.
- **Playful animation: absent.** Motion tokens are restrained and mechanical.
- **Colorful icon/badge decoration: absent.** The visible language is monochrome chrome + imagery.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual / REQUIRED -->

- **Cookie modal obstruction** — The available hero screenshot is partially covered by the Korean cookie consent modal. Hero anatomy is inferred from the visible background, nav chrome, CTA, and captured HTML.
- **Shadow DOM/component internals** — Porsche Design System web components are present, but many final button, form, modal, and tile styles are encapsulated or runtime-loaded outside the extracted CSS.
- **One page only** — Analysis is based on the captured homepage, not configurator, checkout, dealer finder, finance, login, or model-detail subflows.
- **Color aliases unavailable** — `alias_layer.json` reports zero semantic/action/component/core color tiers. Frontmatter color labels are guidebook aliases over observed CSS hex values, not source token names.
- **External CSS failure** — one captured CSS file is a 403 fallback page. Its #CC0000/#EEEEEE/#555555 values are treated as error/fallback evidence, not Porsche brand UI.
- **Exact public CTA styling unverified** — Button tags are visible in the component list and HTML props, but final PDS button shadow DOM styles were not exposed in the captured phase1 CSS.
- **Motion behavior partially inferred** — CSS exposes durations, easing, and image hover scale; scroll-triggered JS behavior and video timing were not analyzed.
- **Mobile screenshot not inspected** — HTML includes mobile image assets and CSS breakpoints, but the visual read is from the desktop hero crop.
- **Dark mode is contextual** — The site uses dark hero contexts, not a fully mapped app-wide dark mode in the captured CSS.
- **No invented tokens** — Any missing exact size, color, or component value is marked as component-owned or not exposed rather than guessed.
