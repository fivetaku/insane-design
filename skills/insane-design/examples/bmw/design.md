---
schema_version: 3.2
slug: bmw
service_name: BMW
site_url: https://bmw.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#1C69D4"
primary_font: "BMW Type Next Latin"
font_weight_normal: 400
token_prefix: pw

bold_direction: "Cinematic Precision"
aesthetic_category: "other"
signature_element: "hero_impact"
code_complexity: "medium"

medium: web
medium_confidence: high
archetype: automotive
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "AEM-generated BMW.com markup exposes consistent pw-* component naming, BMW Type Next font loading, grid-container/grid layout classes, and repeated component modules, but the fetched CSS assets returned only 10 bytes each."

colors:
  brand-blue: "#1C69D4"
  theme-gray: "#8E8E8E"
  hero-black: "#000000"
  surface-white: "#FFFFFF"
  text-dark: "#262626"
  border-light: "#D6D6D6"

typography:
  display: "BMW Type Next Latin"
  editorial: "Playfair"
  body: "BMW Type Next Latin"
  ladder:
    - { token: hero-display, size: "clamp(96px, 14vw, 180px)", weight: 300, tracking: "0" }
    - { token: eyebrow, size: "14px", weight: 400, tracking: "0.42em" }
    - { token: headline-l, size: "40px", weight: 400, tracking: "0" }
    - { token: body, size: "16px", weight: 400, tracking: "0" }
  weights_used: [300, 400, 700]
  weights_absent: [500, 800, 900]

components:
  button-solid-blue: { bg: "{colors.brand-blue}", color: "{colors.surface-white}", radius: "0px", padding: "15px 36px" }
  button-ghost-light: { bg: "transparent", color: "{colors.surface-white}", border: "1px solid rgba(255,255,255,.8)", radius: "0px" }
  header-glass-dark: { bg: "rgba(0,0,0,.28)", border: "1px solid rgba(255,255,255,.42)" }
---

# DESIGN.md - BMW (Designer Guidebook v3.2)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

BMW.com is not built like a generic car catalogue. The page behaves like a cinematic product reveal: the vehicle owns the frame first, the UI recedes into a thin technical layer, and the brand only interrupts when the user needs to act. The first screen is an engineered stage, not a marketing hero card. In the stored screenshot, the iX3 sits centered in a wide road-and-sky composition while the left side holds the enormous model name, a sparse line of copy, and two rectilinear CTAs.

The strongest visual tension is between luxury restraint and utility clarity. BMW does not over-decorate the chrome around the car. It uses dark image overlays, a near-monochrome interface, hard-edged buttons, and one vivid blue action color, #1C69D4 (`{colors.brand-blue}`). That blue is not spread across backgrounds or illustrations; it appears where intent becomes action. There is no second playful brand color: the blue behaves like a cockpit indicator lamp, only lighting up when the driver can make a decision.

The hero is closer to a night test track than a showroom catalogue. The road, sky, and dark overlay form a single asphalt-black stage; the interface does not put the vehicle inside a card or frame. Shadow belongs to photography and lighting, not to chrome. The car is allowed to carry depth, while the navigation, copy, and CTAs stay flat enough to feel like calibrated instrumentation.

Typography is part industrial sign system, part editorial brand magazine. The HTML preloads `BMWTypeNextLatin.woff2` and `playfair.woff2`; the observed hero uses BMW's geometric sans language for navigation and CTAs, while the page retains room for editorial flourishes. The huge "iX3" treatment is the signature move: letters are thin, wide, and calm, not aggressive.

The space is automotive showroom space, but with the walls removed like a wind tunnel opened to the landscape. Large image fields do the emotional work. Grid structure and navigation are precise, but the layout does not feel like a SaaS dashboard. The interface is a measuring instrument wrapped around photography and motion.

The rectangular CTAs feel less like buttons and more like console switches mounted below the model name. Their square edges matter: a `999px` pill would turn the scene into friendly software, while BMW's hard rectangle keeps the mood mechanical and premium. The top navigation is the same kind of object, a dark glass visor with a white hairline rather than a floating app bar.

### Key Characteristics

- Full-bleed vehicle photography/video defines the first viewport.
- Navigation is dark, transparent, and hairline-separated over the image field.
- CTA hierarchy is binary: solid BMW blue primary, transparent outlined secondary.
- Hero display type is oversized and thin rather than heavy or condensed.
- Strong horizontal chrome: top nav, hero CTAs, footer columns, all aligned to a grid.
- Brand color is action-only; image, black, white, and gray carry most of the page.
- Corners are square or nearly square; the brand does not read as pill-soft.
- Icons are line-based and utility-like, with no decorative icon stickers.
- Footer shifts into a dense corporate directory, confirming this is a global brand portal.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Cinematic Precision
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **full-bleed vehicle reveal with action-only BMW blue**으로 기억된다.
> **Code Complexity**: medium — AEM component modules, video hero, consent/geolocation overlays, and responsive navigation create moderate implementation complexity without needing particle or custom-canvas effects.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 BMW처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "BMW Type Next Latin", "Arial", -apple-system, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #000000;
  --fg: #FFFFFF;
  --muted: #8E8E8E;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #1C69D4; }
.cta-primary { background: var(--brand); color: #FFFFFF; border-radius: 0; }
```

**절대 하지 말아야 할 것 하나**: BMW를 둥근 카드형 SaaS 랜딩처럼 만들지 말 것. 이 사이트의 핵심은 카드가 아니라 full-bleed vehicle stage, square CTA, action-only blue다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://bmw.com` |
| Canonical URL in HTML | `https://www.bmw.com/en/index.html` |
| Fetched | 2026-05-03 |
| Extractor | reused existing phase1 + existing HTML + existing screenshot |
| HTML size | 23,204 bytes |
| CSS files | 3 external files present, but each returned 10 bytes on fetch |
| Token prefix | `pw` from `pw-*` component classes |
| Method | HTML structure, preloaded font links, phase1 JSON, screenshot observation; CSS-token extraction was unavailable |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Adobe Experience Manager-style component output (`bmwcom:2.202602.1.0` generator in HTML).
- **Design system**: BMW.com production component system, exposed through `pw-*`, `pwt-*`, `pwv-*`, and `grid-container grid` naming.
- **CSS architecture**: external `clientlib-*` bundles referenced by HTML, but the local fetch produced 10-byte placeholder responses. Treat values below as observed interface specs, not complete CSS-token inventory.
  ```text
  pw-m-*        module components: header, headline teaser, geo checker
  pw-a-*        atoms: button, icon link, video, text
  pw-o-*        organisms/layout objects: media
  pwt-*         theme classes: footer dark theme, surface variants
  grid*         layout primitives: grid-container, grid
  ```
- **Class naming**: BEM-like component names, for example `pw-m-header__menu-link`, `pw-a-button--solid-blue`, `pw-a-button--ghost-dark`.
- **Default theme**: mixed; dark hero/nav and footer, white cookie/overlay surfaces.
- **Font loading**: HTML preloads `/fonts/BMWTypeNextLatin.woff2` and `/fonts/playfair.woff2`.
- **Canonical anchor**: BMW international homepage, with localized alternates for de, ja, it, fr, es.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `BMW Type Next Latin` (brand font, preloaded as WOFF2)
- **Editorial font**: `Playfair` (preloaded as WOFF2, likely used for editorial flourishes or article modules)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --pw-font-family: "BMW Type Next Latin", Arial, -apple-system, sans-serif;
  --pw-font-family-editorial: "Playfair", Georgia, serif;
  --pw-font-weight-normal: 400;
  --pw-font-weight-bold: 700;
}
body {
  font-family: var(--pw-font-family);
  font-weight: var(--pw-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **BMW Type Next Latin** is the real identity carrier. If unavailable, use **Arial** or **Helvetica Neue** rather than Inter. Inter's open apertures and product-SaaS rhythm make BMW feel too software-native.
- For hero display text, lower the fallback weight visually: use `font-weight: 300` or `font-weight: 400` with generous size. Do not compensate by using `font-weight: 700`.
- Keep navigation and CTA text compact and technical: line-height around `1.2` for controls, `1.4-1.5` for copy.
- If Playfair is missing, use **Georgia** only for editorial accents, never for nav, CTAs, or model names.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| hero-display | `clamp(96px, 14vw, 180px)` | 300 | 0.88-0.95 | `0` |
| hero-eyebrow | `14px` | 400 | 1.2 | `0.42em` |
| headline-l | `40px` | 400 | 1.12 | `0` |
| nav-link | `14px` | 400 | 1.2 | `0` |
| body-copy | `16px` | 400 | 1.45 | `0` |
| footer-heading | `14px` | 700 | 1.3 | `0` |
| footer-link | `14px` | 400 | 1.5 | `0` |

> ⚠️ Typography extraction JSON was empty. Scale above is derived from observed screenshot anatomy and HTML class roles, not complete CSS token parsing.

### Principles

1. Hero model typography is display-scale but thin; the BMW feel comes from large geometry plus restraint, not from heavy display weight.
2. Eyebrows can be widely tracked. Body and control text should not receive decorative tracking.
3. Navigation stays small and technical so the vehicle image can dominate the viewport.
4. Weight 500 is not a signature choice in the captured surface; use 400 for normal UI and 700 only for emphasis.
5. Editorial serif is optional and secondary. It should never replace BMW Type Next in CTAs or structural navigation.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed/action ramp)

| Token | Hex |
|---|---|
| `{colors.brand-blue}` | `#1C69D4` |
| `{colors.theme-gray}` | `#8E8E8E` |

### 06-2. Brand Dark Variant

> N/A - no complete CSS token ramp was available. Dark treatment is achieved through photography, overlay, and black/transparent UI surfaces rather than a separate parsed dark token family.

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| surface | `#FFFFFF` | `#000000` |
| text | `#262626` | `#FFFFFF` |
| muted | `#8E8E8E` | `rgba(255,255,255,.72)` |
| hairline | `#D6D6D6` | `rgba(255,255,255,.42)` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| BMW action blue | primary CTA | `#1C69D4` |
| UI gray | theme/meta color | `#8E8E8E` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `action-primary` | `#1C69D4` | Primary CTA, "pre-order" / blue action |
| `surface-light` | `#FFFFFF` | Cookie and geo-checker overlay panels |
| `surface-dark` | `#000000` | Hero overlay floor, dark footer |
| `text-primary-dark` | `#FFFFFF` | Text over vehicle photography |
| `text-primary-light` | `#262626` | Text in white panels |
| `border-light` | `#D6D6D6` | Outlined buttons and panel dividers |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `button-solid-blue` | `#1C69D4` -> white text | Primary action |
| `button-ghost-light` | transparent + white hairline | Secondary hero action |
| `overlay-panel` | `#FFFFFF` + dark text | Cookie / geo overlays |
| `hero-chrome` | transparent black + white hairline | Header over image |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---|---:|
| theme-color meta | `#8E8E8E` | 1 |

> The phase1 `brand_candidates.json` contained only `#8E8E8E`, classified as neutral. The BMW blue is taken from observed component class naming (`pw-a-button--solid-blue`) and screenshot CTA appearance, not from CSS-token frequency.

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.brand-blue}` (`#1C69D4`)** - BMW's action color. Use it for primary CTAs and decisive interactive states only. It should feel like an instrument light, not a decorative background wash.

**`{colors.hero-black}` (`#000000`)** - The cinematic base. It appears through overlays, dark footer surfaces, and image contrast, letting vehicle photography supply depth.

**`{colors.surface-white}` (`#FFFFFF`)** - Functional interruption surface. It is correct for consent, geo, and dense corporate panels, but not for the hero stage itself.

**`{colors.theme-gray}` (`#8E8E8E`)** - Neutral brand interface gray from the HTML theme-color and phase1 frequency candidate. Use as secondary interface tone, not as the primary brand color.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `space-1x` | `8px` | minor icon gaps, fine offsets |
| `space-2x` | `16px` | text/control internal rhythm |
| `space-4x` | `32px` | CTA grouping and nav clusters |
| `space-8x` | `64px` | visible spacer module in HTML: `pw-m-spacer--size-8x` |
| `hero-inset-x` | `clamp(32px, 8vw, 104px)` | left-aligned hero copy and CTA rail |
| `section-y` | `64px-96px` | editorial/module separation |

**주요 alias**:
- `pw-m-spacer--size-8x` -> `64px` conceptual spacer module; confirmed by HTML class naming, not computed CSS.

### Whitespace Philosophy
<!-- SOURCE: manual -->

BMW uses whitespace as road space. The hero does not pack copy around the vehicle; it lets the car occupy a broad center-right volume while the model name sits left in a deep, dark field. The result is not "minimal white space" but cinematic clearance.

Below the hero, spacing becomes more corporate and modular. Footer columns and overlays compress information, but the top-level brand moment remains spacious: image first, decision controls second, text third.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `radius-control` | `0px` | Hero CTAs, BMW-style rectangular controls |
| `radius-panel` | `0px-2px` | Cookie/geolocation panels; keep nearly square |
| `radius-logo` | `50%` | BMW roundel only, not generic UI containers |
| `radius-icon` | `50%` | If circular icon buttons are needed |

> BMW should not inherit the 8px/12px SaaS card default. Hard rectangles are part of the automotive precision.

---

## 09. Shadows
<!-- SOURCE: manual -->

| Level | Value | Usage |
|---|---|---|
| hero-image-depth | `image/lighting only` | Vehicle presence comes from photography, not UI box-shadows |
| overlay-panel | `0 12px 36px rgba(0,0,0,.18)` | Consent/geo modal elevation, if needed |
| nav | `none` | Header separation is hairline + backdrop contrast |
| card | `none or very low` | Do not create ecommerce-style product-card elevation |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| hero-video | loop muted autoplay | HTML includes desktop and mobile video assets with poster image |
| control-hover | `120ms-180ms ease` | Button and nav feedback should be quick and technical |
| overlay-open | `180ms opacity/transform` | Consent and geo overlays |

> JS motion curves were not analyzed. Keep BMW motion disciplined: no bounce, no elastic easing, no decorative parallax unless it is tied to vehicle reveal.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: likely large desktop grid; use `min(100% - 64px, 1184px)` for content modules.
- **Grid type**: HTML exposes `grid-container grid`.
- **Column count**: desktop 12-column conceptual grid; hero content behaves as asymmetric overlay.
- **Gutter**: `24px-32px` desktop, `16px` mobile.

### Hero
- **🆕 Pattern Summary**: `80-100vh + full-bleed vehicle video/photo + left model name + dual CTA below`
- Layout: asymmetric overlay; copy and CTAs left, vehicle centered/right.
- Background: full-bleed video/photo with dark left-side readability overlay.
- **🆕 Background Treatment**: `image-overlay` / `video-poster` with black-to-transparent readability gradient.
- H1: `clamp(96px, 14vw, 180px)` / weight `300` / tracking `0`.
- Max-width: copy rail around `520px`; visual field full width.

### Section Rhythm

```css
section {
  padding: 64px clamp(24px, 6vw, 80px);
  max-width: 1184px;
}
.hero {
  min-height: 80vh;
  max-width: none;
  padding: 96px clamp(32px, 8vw, 104px) 72px;
}
```

### Card Patterns
- **Card background**: `#FFFFFF` for information panels, transparent over hero.
- **Card border**: `1px solid #D6D6D6` or white alpha hairline on dark imagery.
- **Card radius**: `0px-2px`.
- **Card padding**: `24px-40px`.
- **Card shadow**: none for normal chrome; modal shadow only.

### Navigation Structure
- **Type**: horizontal desktop nav with burger/search utility controls; mobile collapses to burger.
- **Position**: top header over hero, visually fixed/sticky-capable.
- **Height**: about `84px` in screenshot.
- **Background**: transparent black/dark image overlay.
- **Border**: white alpha bottom hairline.

### Content Width
- **Prose max-width**: `640px`.
- **Container max-width**: `1184px-1280px`.
- **Sidebar width**: N/A for homepage; footer uses columns instead.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `< 768px` | Burger-first navigation, stacked hero copy, reduced model display size |
| Tablet | `768px-1023px` | Mixed nav; CTAs remain full-width enough for touch |
| Desktop | `1024px+` | Horizontal nav and wide hero composition |
| Large | `1280px+` | Full cinematic crop; vehicle owns center/right visual mass |

### Touch Targets
- **Minimum tap size**: `44px`.
- **Button height (mobile)**: `48px-56px`.
- **Input height (mobile)**: `44px+`.

### Collapsing Strategy
- **Navigation**: hamburger controls exposed in header markup.
- **Grid columns**: `grid-container grid` should collapse to single-column content on mobile.
- **Sidebar**: N/A on homepage.
- **Hero layout**: image remains full bleed; copy moves toward lower/left stacked control rail.

### Image Behavior
- **Strategy**: poster/video with desktop and mobile asset variants.
- **Max-width**: full viewport for hero; content modules constrained.
- **Aspect ratio handling**: HTML uses `--width: 16; --height: 9` in `pw-a-layout`.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary Action - `pw-a-button--solid-blue`**

```html
<a class="pw-a-button pw-a-button--solid-blue">Pre-order</a>
```

| Spec | Value |
|---|---|
| Background | `#1C69D4` |
| Text | `#FFFFFF` |
| Radius | `0px` |
| Padding | `15px 36px` |
| Min height | `52px` |
| Hover | darken blue slightly, no bounce |
| Focus | visible outline outside the rectangular control |

**Secondary Hero Action - ghost light**

```html
<a class="pw-a-button pw-a-button--ghost-light">Model information</a>
```

| Spec | Value |
|---|---|
| Background | transparent |
| Text | `#FFFFFF` |
| Border | `1px solid rgba(255,255,255,.8)` |
| Radius | `0px` |
| Hover | subtle white fill or border brightening |

### Badges

> N/A - captured homepage surface does not expose a badge system. Do not invent pill badges just to fill the component set.

### Cards & Containers

**Overlay Panel**

```html
<dialog class="pw-m-geo-checker">
  <div class="pw-m-geo-checker__container">...</div>
</dialog>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#262626` |
| Radius | `0px-2px` |
| Padding | `32px-48px` desktop |
| Shadow | modal-only, low black alpha |

### Navigation

```html
<header class="pw-m-header">
  <div class="pw-m-header__container">
    <nav class="pw-m-header__nav">...</nav>
  </div>
</header>
```

| Spec | Value |
|---|---|
| Logo | BMW roundel, 100x100 source image rendered smaller |
| Links | 14px BMW Type Next, white/gray over hero |
| Separator | bottom hairline over image |
| Utilities | line icons for account, cart, location, favorite |
| Mobile | burger button with menu/close icons |

### Inputs & Forms

```html
<input id="pw-m-header__search-input" class="pw-m-header__search-input" name="q" type="text" placeholder="Search">
```

| Spec | Value |
|---|---|
| Height | `44px+` |
| Background | dark transparent in header, white in panels |
| Border | hairline, no heavy rounded shell |
| Focus | visible outline; do not rely on color alone |
| Error | not observed |

### Hero Section

```html
<section class="pw-o-media grid grid-container">
  <figure class="pw-a-video">
    <video poster="/content/dam/bmw/.../bmw-OG-image-01.jpg" loop muted autoplay></video>
  </figure>
</section>
```

| Spec | Value |
|---|---|
| Background | video/photo, 16:9 asset behavior |
| Copy position | left overlay rail |
| CTA position | below hero copy, horizontal desktop |
| Overlay | dark left-side readability gradient |

### 13-2. Named Variants

- **button-solid-blue** - rectangular primary action with `#1C69D4` background and white text.
- **button-ghost-light** - transparent rectangular secondary action on image/dark backgrounds.
- **button-ghost-dark** - HTML-observed class for geolocation stay action on light panel.
- **header-glass-dark** - dark transparent navigation layer over full-bleed media.
- **geo-checker-panel** - white modal asking whether to switch regional site.
- **icon-link-inline** - inline text link with paired icons, used for "Find your BMW" style module.

### 13-3. Signature Micro-Specs

```yaml
vehicle-stage-gradient:
  description: "Readability gradient that lets white typography sit over a darkened left side while the vehicle remains visible on the right."
  technique: "background: linear-gradient(90deg, rgba(0,0,0,.72), rgba(0,0,0,.18) 48%, rgba(0,0,0,0)), var(--hero-image) center / cover no-repeat"
  applied_to: ["{component.Hero Section}", "{component.pw-o-media}", "{component.pw-a-video}"]
  visual_signature: "The car is not boxed; it emerges from the same stage as the UI."

rectangular-action-pair:
  description: "Primary and secondary CTAs share one hard-edged geometry, then split by fill and border."
  technique: "border-radius: 0; min-height: 52px; padding: 15px 36px; primary background #1C69D4 /* {colors.brand-blue} */; secondary border 1px solid rgba(255,255,255,.8)"
  applied_to: ["{component.pw-a-button--solid-blue}", "{component.button-ghost-light}"]
  visual_signature: "Precise automotive control switches, not friendly SaaS pills."

header-glass-dark-hairline:
  description: "Dark transparent navigation layer that stays subordinate to full-bleed vehicle media."
  technique: "background: rgba(0,0,0,.28); border-bottom: 1px solid rgba(255,255,255,.42); shadow: none"
  applied_to: ["{component.header-glass-dark}", "{component.pw-m-header}"]
  visual_signature: "A dark glass visor across the image, separated by a white instrument hairline."

thin-display-model-name:
  description: "Oversized model name rendered as a calm engineering label rather than a heavy poster headline."
  technique: "font-family: BMW Type Next Latin; font-size: clamp(96px, 14vw, 180px); font-weight: 300; letter-spacing: 0; text-shadow: none"
  applied_to: ["{component.Hero Section}", "{typography.hero-display}"]
  visual_signature: "Cinema title scale with technical drawing restraint."

duotone-hairline-system:
  description: "Two paired hairline values flip between light surfaces and dark imagery so dividers always feel like instrument lines, never decorative borders."
  technique: "Light scenes use border `1px solid #D6D6D6`; dark/image scenes use `1px solid rgba(255,255,255,0.42)`. Identical 1px weight, alpha-tuned per ground. Never widened, never coloured with brand blue."
  applied_to: ["{component.header-glass-dark}", "{component.button-ghost-light}", "{component.card-light-panel}"]
  visual_signature: "A single instrument-panel hairline that survives any background — the BMW gauge line, applied to UI."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: auto+manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | model name or direct product/category phrase | "iX3" |
| Eyebrow | spaced uppercase category line | "THE NEW BMW" |
| Primary CTA | concrete next action | "Pre-order" / "Take me there" |
| Secondary CTA | information or stay action | "Model information" / "Stay on this page" |
| Tone | premium, direct, sparse | "The first of a new era." |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* BMW - copy into your root stylesheet */
:root {
  /* Fonts */
  --pw-font-family: "BMW Type Next Latin", Arial, -apple-system, sans-serif;
  --pw-font-family-editorial: "Playfair", Georgia, serif;
  --pw-font-weight-normal: 400;
  --pw-font-weight-bold: 700;

  /* Brand */
  --pw-color-brand-25:  #EAF2FD;
  --pw-color-brand-300: #5A9BEF;
  --pw-color-brand-500: #1C69D4;
  --pw-color-brand-600: #1C69D4; /* canonical action blue */
  --pw-color-brand-900: #063970;

  /* Surfaces */
  --pw-bg-page:    #000000;
  --pw-bg-panel:   #FFFFFF;
  --pw-text:       #262626;
  --pw-text-inv:   #FFFFFF;
  --pw-text-muted: #8E8E8E;
  --pw-border:     #D6D6D6;

  /* Spacing */
  --pw-space-sm:  16px;
  --pw-space-md:  32px;
  --pw-space-lg:  64px;

  /* Radius */
  --pw-radius-sm: 0px;
  --pw-radius-md: 0px;
}

.bmw-hero {
  min-height: 88vh;
  color: var(--pw-text-inv);
  background:
    linear-gradient(90deg, rgba(0,0,0,.72), rgba(0,0,0,.18) 48%, rgba(0,0,0,0)),
    var(--hero-image) center / cover no-repeat;
}

.bmw-button-primary {
  background: var(--pw-color-brand-600);
  color: #FFFFFF;
  border: 1px solid var(--pw-color-brand-600);
  border-radius: 0;
  min-height: 52px;
  padding: 15px 36px;
}

.bmw-button-secondary {
  background: transparent;
  color: #FFFFFF;
  border: 1px solid rgba(255,255,255,.8);
  border-radius: 0;
  min-height: 52px;
  padding: 15px 36px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js - BMW-inspired system
module.exports = {
  theme: {
    extend: {
      colors: {
        bmw: {
          blue: '#1C69D4',
          gray: '#8E8E8E',
          ink: '#262626',
          black: '#000000',
          white: '#FFFFFF',
          border: '#D6D6D6',
        },
      },
      fontFamily: {
        sans: ['BMW Type Next Latin', 'Arial', 'system-ui'],
        editorial: ['Playfair', 'Georgia', 'serif'],
      },
      borderRadius: {
        bmw: '0px',
      },
      boxShadow: {
        'bmw-modal': '0 12px 36px rgba(0,0,0,.18)',
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
| Brand primary | `{colors.brand-blue}` | `#1C69D4` |
| Background | `{colors.hero-black}` | `#000000` |
| Panel background | `{colors.surface-white}` | `#FFFFFF` |
| Text primary | `{colors.text-dark}` | `#262626` |
| Text muted | `{colors.theme-gray}` | `#8E8E8E` |
| Border | `{colors.border-light}` | `#D6D6D6` |
| Error | N/A | N/A |

### Example Component Prompts

#### Hero Section

```text
BMW 스타일 히어로 섹션을 만들어줘.
- 배경: full-bleed vehicle photo/video with dark left readability overlay
- H1: BMW Type Next Latin, clamp(96px, 14vw, 180px), weight 300, tracking 0
- eyebrow: 14px uppercase, wide letter spacing
- CTA: primary #1C69D4 rectangle, secondary transparent white-outline rectangle
- max-width: hero visual full-bleed, copy rail about 520px
- 금지: 둥근 카드, pastel gradient, floating SaaS feature cards
```

#### Card Component

```text
BMW 스타일 정보 패널을 만들어줘.
- 배경: #FFFFFF, 텍스트 #262626, border #D6D6D6
- radius: 0px-2px only
- padding: 32px desktop, 24px mobile
- shadow: modal/panel에만 낮게 사용
- 제목: BMW Type Next Latin, 24-32px, weight 400 or 700
```

#### Badge

```text
BMW 스타일에서는 일반적인 pill badge를 만들지 마라.
필요하면 작은 uppercase label로 처리하고, 배경 pill 대신 spacing과 typography로 구분한다.
```

#### Navigation

```text
BMW 스타일 상단 네비게이션을 만들어줘.
- 높이: 약 84px
- 배경: hero 위 transparent dark overlay
- 하단: rgba(255,255,255,.42) hairline
- 로고: 좌측 BMW roundel
- 링크: 14px BMW Type Next Latin, white/soft gray
- 우측: search/account/cart/location/favorite 같은 thin line icons
- 모바일: burger button, square touch target
```

### Iteration Guide

- **색상 변경 시**: `#1C69D4`를 전체 배경에 깔지 말고 CTA/action에만 사용한다.
- **폰트 변경 시**: Inter보다 Arial/Helvetica fallback이 BMW Type Next의 산업적 톤에 가깝다.
- **여백 조정 시**: hero는 큰 공기, footer/overlay는 밀도 있게. 모든 구역을 같은 spacing으로 평준화하지 않는다.
- **새 컴포넌트 추가 시**: radius는 0px 기준. 8px 카드 기본값을 쓰지 않는다.
- **반응형**: 차량 이미지는 crop으로 유지하고, 텍스트 레일만 재배치한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use vehicle photography or video as the dominant visual system.
- Keep BMW blue `#1C69D4` reserved for primary action and intent.
- Build rectangular CTAs with square edges and precise spacing.
- Use dark overlays to preserve readable white hero typography.
- Keep navigation thin, technical, and utility-driven.
- Let the BMW roundel be the only circular brand object unless an icon control genuinely needs a circle.
- Treat overlays and footers as dense corporate surfaces, not marketing cards.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두고 hero를 시작하지 말 것 — 대신 hero는 `#000000` 기반 image/video overlay를 사용.
- 텍스트를 `#000000` 또는 `black`으로 hero 위에 직접 두지 말 것 — 대신 dark overlay 위 `#FFFFFF` 사용.
- primary CTA를 `#8E8E8E`로 만들지 말 것 — 대신 action에는 `#1C69D4` 사용.
- BMW blue `#1C69D4`를 넓은 gradient 배경으로 깔지 말 것 — 대신 버튼/active state에만 사용.
- 카드 border를 `#1C69D4`로 과장하지 말 것 — 대신 neutral hairline `#D6D6D6` 사용.
- 버튼에 `border-radius: 999px` 사용 금지 — BMW CTA는 square/rectangular control이다.
- hero display에 `font-weight: 800` 또는 `900` 사용 금지 — 큰 크기 + 얇은 weight가 핵심이다.
- generic SaaS shadow card (`0 10px 30px rgba(...)`)를 반복하지 말 것 — shadow는 modal/panel에만 제한한다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No second playful brand color** - blue is the action color; do not invent teal, purple, or coral accents.
- **No soft pill-button language** - radius-heavy buttons immediately weaken the automotive precision.
- **No decorative gradient mesh** - visual drama comes from real vehicle imagery, not synthetic blobs.
- **No emoji or sticker iconography** - icons are line utilities, not personality ornaments.
- **No card-first homepage rhythm** - the first viewport is a stage, not a grid of feature cards.
- **No heavy display weight** - the model name should not become a poster-weight shout.
- **No colorful badge taxonomy** - BMW uses labels and links, not multi-color status chips.
- **No chrome shadow system** - navigation and buttons are separated by contrast, fill, and hairline, not elevation.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **CSS token extraction unavailable** - the three referenced CSS files in `insane-design/bmw/css/` were 10 bytes each, and a targeted refetch returned the same size. All CSS-token claims are therefore conservative and marked as observed/manual where needed.
- **Phase1 JSON was sparse** - `resolved_tokens.json` reported `total_vars: 0`, `typography.json` had no families or scale entries, and `alias_layer.json` had zero tier counts.
- **HTML and screenshot locale mismatch** - the stored HTML is BMW international English (`www.bmw.com/en/index.html`), while the stored screenshot shows a Korean BMW hero surface. Shared brand/component patterns were used; locale-specific copy should not be treated as a single canonical source.
- **BMW blue was inferred from component class and screenshot** - `#1C69D4` did not appear in the sparse phase1 frequency JSON. It is included as the observed BMW action-blue spec, not as parsed CSS proof.
- **Motion internals not analyzed** - HTML confirms loop muted autoplay video assets, but JS transition curves, scroll triggers, and video loading behavior were not inspected.
- **Sub-flows not visited** - configurator, model pages, checkout/lead forms, search results, and local market pages can have additional component states not captured here.
- **Form validation states missing** - search input exists, but error, loading, disabled, and validation states were not observed.
- **Exact responsive CSS unavailable** - breakpoint values are designer approximations based on component structure and automotive homepage conventions, not parsed media query output.
