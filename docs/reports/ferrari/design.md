---
schema_version: 3.2
slug: ferrari
service_name: Ferrari
site_url: https://www.ferrari.com/en-US
fetched_at: 2026-05-03
default_theme: mixed
brand_color: "#DA291C"
primary_font: FerrariSans
font_weight_normal: 400
token_prefix: f

bold_direction: Cinematic Precision
aesthetic_category: editorial-product
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: automotive
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Production CSS exposes a compact --f-* token layer, theme classes, spacing utilities, focus color, gradients, and custom webfont loading."

colors:
  accent: "#DA291C"
  accent-dark: "#B01E0A"
  accent-deep: "#9D2211"
  hypersail-yellow: "#FFF200"
  focus-yellow: "#F6E500"
  background-light: "#FFFFFF"
  background-dark: "#181818"
  background-dark-alt: "#383838"
  ui-light: "#F7F7F7"
  ui-mid: "#8F8F8F"
  ui-muted: "#666666"
  ui-border: "#D2D2D2"
typography:
  display: "FerrariSans"
  body: "FerrariSans"
  ladder:
    - { token: body, size: "13px", weight: 400, line_height: "1.5", tracking: "0.015em" }
    - { token: subtitle, size: "18px", weight: 400, line_height: "1.4", tracking: "0.01em" }
    - { token: title, size: "26px-28px", weight: 500, line_height: "1.23", tracking: "0.015em inherited" }
    - { token: hero-h1-observed, size: "visual approx 38px", weight: 500, line_height: "tight", tracking: "wide uppercase" }
  weights_used: [400, 500]
  weights_absent: [300, 600, 700, 800, 900]
components:
  button-ghost-video: { bg: "transparent", text: "{colors.background-light}", radius: "9999px icon", padding: "inline label plus circular arrow" }
  button-share-icon: { bg: "transparent", text: "{colors.background-light}", radius: "0", padding: "12px" }
  table-technical: { bg: "{colors.background-light}", border: "1px solid {colors.ui-border}", radius: "0", padding: "16px cells" }
  nav-transparent-hero: { bg: "transparent over media", text: "{colors.background-light}", height: "visual 80px" }
---

# DESIGN.md - Ferrari

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Ferrari's web system is not a conventional luxury landing page. It behaves like a cinema title sequence bolted to an engineering manual: first darkness, then a white mark, then a line of uppercase navigation, then the vehicle surface emerging from the frame. The site has almost no self-conscious chrome. It turns the page into a black stage and lets photography become the metal.

The central metaphor is a midnight Maranello showroom: `#181818` (`{colors.background-dark}`) is not pure black as a void, but a cinema-screen black with space inside it. On OLED, pure black can feel like a cut-out hole; Ferrari's dark surface behaves more like a room with the lights down. The car is not placed on a web page; the page clears out until the car/video becomes the architecture.

The brand red is deliberately scarce. `#DA291C` (`{colors.accent}`) exists as the canonical Ferrari accent in CSS, with darker `#B01E0A` and `#9D2211` variants, but the homepage hero is not painted red. No second brand color competes with it. Red functions like ignition, pit-lane light, or a single Rosso Corsa reflection on a black floor: memorable because it is withheld.

The typography is more technical than romantic. `FerrariSans` runs small, wide, and disciplined: body starts at 13px with `letter-spacing: 0.015em`, headings sit at weight 500, and uppercase labels form the navigation rhythm. Ferrari avoids the usual luxury-serif move. Its premium feeling comes from precision, not ornament.

The secondary mode is a wind tunnel display room crossed with a spec sheet. Surfaces are either pure white `#FFFFFF` (`{colors.background-light}`) or near-black `#181818` (`{colors.background-dark}`), with gradients used to shape light rather than decorate. Shadow belongs to media and icons over media, not to friendly cards. When the site becomes informational, it does not become soft; it becomes a flat technical table with careful borders.

The result is cinematic precision: a title sequence, a showroom, and a pit-wall manual sharing one system. Photography is the chrome. UI elements are small labels beside the machine, not furniture in front of it.

### Key Characteristics

- Full-bleed cinematic media as the main brand surface.
- Sparse red usage: `#DA291C` is canonical but rarely floods the UI.
- Mixed light/dark theme tokens via `.f-theme-light` and `.f-theme-dark`.
- FerrariSans only, with 400 and 500 as the meaningful weights.
- Tiny uppercase navigation with wide tracking and high contrast.
- Spacing ladder is explicit and large: 4px, 8px, 16px, 24px, 32px, 48px, 64px, 96px, 128px.
- Radius is almost absent except for `--f-radius-full: 9999px`.
- Focus is bright yellow `#F6E500`, not red.
- Shadows are minimal and functional; media contrast does the depth work.
- CSS namespace is compact and branded: `--f-*`.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Cinematic Precision
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **full-bleed automotive media with almost invisible chrome and scarce Ferrari red**으로 기억된다.
> **Code Complexity**: high — production CSS includes theme remapping, custom web components, media-heavy hero behavior, gradients, focus tokens, and a custom font stack.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Ferrari처럼 만들기 - 3가지만 하면 80%

```css
/* 1. Font + weight */
body {
  font-family: "FerrariSans", "Noto Sans", -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 13px;
  font-weight: 400;
  letter-spacing: 0.015em;
  line-height: 1.5;
}

/* 2. Surface + text */
:root {
  --bg: #FFFFFF;
  --bg-dark: #181818;
  --fg: #181818;
  --fg-inverse: #FFFFFF;
}

/* 3. Accent only as ignition */
:root {
  --brand: #DA291C;
  --focus: #F6E500;
}
```

**절대 하지 말아야 할 것 하나**: Ferrari를 red website로 만들지 말 것. Red is a precision accent; the page identity is media, black/white contrast, and restrained uppercase typography.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.ferrari.com/en-US` |
| Reused local capture | `insane-design/ferrari/` |
| Fetched | 2026-05-03 local phase1 reuse; HTML/CSS snapshot from local artifacts |
| Extractor | existing phase1 JSON + local CSS + local HTML + hero screenshot |
| HTML size | 54390 bytes |
| CSS files | 5 CSS files, total local CSS + HTML chars 71977 |
| Token prefix | `--f-*` |
| Method | CSS custom property parsing, local screenshot observation, and production HTML metadata review |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Adobe/AEM-style component page with custom Ferrari web components (`f-*`) and clientlibs.
- **Design system**: Ferrari production token layer, prefix `--f-*`.
- **CSS architecture**:
  ```css
  :root / :host       --f-color-* / --f-space-* / --f-shadow-* / --f-radius-*
  .f-theme-light      light surface remapping
  .f-theme-dark       dark surface remapping
  utility classes     .f-mt-xs, .f-pb-xl, etc.
  web components      f-table, f-text-content, f-horizontal-slider, f-share
  ```
- **Class naming**: branded BEM-like classes (`.f-share__button`) plus custom element selectors (`f-text-content`).
- **Default theme**: mixed. Root and light theme map background to `#FFFFFF`; dark theme maps background to `#181818`.
- **Font loading**: `@font-face` with FerrariSans regular/medium plus NotoSans unicode-range fallback loaded from Ferrari clientlib resources.
- **Canonical anchor**: captured HTML canonical points to localized Ferrari homepage; target analysis is for `https://www.ferrari.com/en-US` and uses the same Ferrari global web system.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `FerrariSans` (brand webfont)
- **Code font**: N/A - no code UI identity observed
- **Weight normal / bold**: `400` / `500`

```css
:root {
  --f-ferrari-font: "FerrariSans";
}

@font-face {
  font-display: fallback;
  font-family: FerrariSans;
  font-style: normal;
  font-weight: 400;
  src: url("Ferrari-SansRegular.woff2") format("woff2");
}

@font-face {
  font-display: fallback;
  font-family: FerrariSans;
  font-style: normal;
  font-weight: 500;
  src: url("Ferrari-SansMedium.woff2") format("woff2");
}

body {
  font-family: var(--f-ferrari-font);
  font-size: 13px;
  letter-spacing: 0.015em;
  line-height: 1.5;
}
```

### Note on Font Substitutes

- **FerrariSans** is proprietary/brand-specific. If unavailable, use **Noto Sans** or **Inter** only as a mechanical substitute, not as a visual match.
- With **Inter**, reduce apparent modern SaaS softness by keeping weight at 400/500 only, adding `letter-spacing: 0.012em` to body, and using uppercase labels for navigation and CTAs.
- Do not replace FerrariSans with a luxury serif. The actual site uses a technical sans, so a serif substitute changes the brand grammar too much.
- Keep body small: 13px or 14px max. A default 16px body makes Ferrari feel like a generic product site.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| body | 13px | 400 | 1.5 | 0.015em |
| subtitle | 18px | 400 | 1.4 | 0.01em |
| text-content title | 26px | 500 inherited heading rule | 1.23 | 0.015em inherited |
| text-content title tablet+ | 28px | 500 inherited heading rule | 1.23 | 0.015em inherited |
| table text | 11px | 400/500 | 1.5em | normal/inherited |
| table smaller | 9px | 400 | 1.5em | normal/inherited |
| hero h1 observed | approx 38px visual | 500 | tight | wide uppercase |

> ⚠️ The production typography JSON did not expose a full token scale. The reliable values come from CSS rules and the captured hero screenshot.

### Principles

1. Body text is intentionally small: `13px`, not the web default `16px`.
2. The meaningful weight pair is 400 and 500. Heavier display weights are absent from the captured CSS.
3. Uppercase plus tracking creates the premium technical voice; size alone does not.
4. `FerrariSans` is the brand chassis. Substituting a geometric SaaS font without spacing correction breaks the feel.
5. Text is subordinate to image. The hero title is bold enough to anchor the frame, but it does not compete with the car/video.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (3 steps)
<!-- --f-color-accent-* -->

| Token | Hex |
|---|---|
| `--f-color-accent-100` light | `#DA291C` |
| `--f-color-accent-100` dark | `#F13A2C` |
| `--f-color-accent-90` | `#B01E0A` |
| `--f-color-accent-80` | `#9D2211` |

### 06-2. Brand Dark Variant
<!-- SOURCE: auto -->

| Token | Hex |
|---|---|
| `.f-theme-dark --f-color-accent-100` | `#F13A2C` |
| `.f-theme-dark --f-color-accent-90` | `#B01E0A` |
| `.f-theme-dark --f-color-accent-80` | `#9D2211` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light mapping | Dark mapping |
|---|---|---|
| global white | `#FFFFFF` | `#FFFFFF` |
| global black | `#181818` | `#181818` |
| background-0 | `#FFFFFF` | `#181818` |
| background-10 | `#EBEBEB` | `#383838` |
| black-90 | `#303030` | `#303030` |
| black-60 | `#666666` | `#666666` |
| black-55 | `#969696` | `#969696` |
| black-50 | `#8F8F8F` | `#8F8F8F` |
| black-20 | `#D2D2D2` | `#D2D2D2` |
| black-10 | `#F7F7F7` | `#F7F7F7` |

### 06-4. Accent Families
<!-- SOURCE: auto -->

| Family | Key step | Hex |
|---|---|---|
| Ferrari red | accent-100 | `#DA291C` / `#F13A2C` |
| Hypersail yellow | yellow-hypersail | `#FFF200` |
| Focus yellow | focus | `#F6E500` |
| Accessible info | info | `#4C98B9` / dark `#54A7CB` |
| Accessible success | success | `#03904A` / dark `#1DB160` |
| Accessible warning | warning | `#F13A2C` |

### 06-5. Semantic
<!-- SOURCE: auto -->

| Token | Hex | Usage |
|---|---|---|
| `--f-color-background-0` | `#FFFFFF` or `#181818` | primary page surface by theme |
| `--f-color-background-10` | `#EBEBEB` or `#383838` | secondary surface |
| `--f-color-ui-100` | `#181818` or `#FFFFFF` | primary foreground |
| `--f-color-ui-60` | `#666666` or `#D2D2D2` | muted text / table meta |
| `--f-color-ui-20` | `#D2D2D2` or `#666666` | borders and dividers |
| `--f-color-focus` | `#F6E500` | focus outline |
| `--f-color-overlay` | rgba(0,0,0,.3) | media overlay |
| `--f-color-overlay-darker` | hsla(0,0%,7%,.8) | darker overlay |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--f-color-ui-100` light | `--f-color-global-black` -> `#181818` | text on light surfaces |
| `--f-color-ui-100` dark | `--f-color-global-white` -> `#FFFFFF` | text on dark/media surfaces |
| `--f-color-ui-0` light | `--f-color-global-white` -> `#FFFFFF` | base chrome surface |
| `--f-color-ui-0` dark | `--f-color-global-black` -> `#181818` | base dark chrome surface |
| `--f-color-focus` | `#F6E500` | keyboard focus |
| `--f-color-gradient-to-background` | theme background alpha gradient | media-to-surface transition |

### 06-7. Dominant Colors (actual CSS frequency order)
<!-- SOURCE: auto -->

| Token / candidate | Hex | Frequency |
|---|---:|---:|
| neutral black | `#000000` | 9 |
| neutral white | `#FFFFFF` | 5 |
| warning/dark accent | `#F13A2C` | 4 |
| accent deep | `#9D2211` | 3 |
| accent dark | `#B01E0A` | 3 |
| accent canonical | `#DA291C` | 3 |
| focus yellow | `#F6E500` | 3 |
| success green | `#03904A` | 2 |
| info blue | `#4C98B9` | 2 |
| highlight neutral | `#CDCBCB` | 2 |
| background light alt | `#EBEBEB` | 2 |

### 06-8. Color Stories

**`{colors.accent}` (`#DA291C`)** - The canonical Ferrari red. It should mark brand moments and high-confidence action, not flood the page. In the captured hero, the brand is still Ferrari without using a red background.

**`{colors.background-dark}` (`#181818`)** - The dark chassis. It gives video, photography, share overlays, and inverse UI a deep technical base that feels closer to a showroom or pit wall than a fashion campaign.

**`{colors.background-light}` (`#FFFFFF`)** - The specification surface. When the site leaves cinema mode, white carries tables, editorial text, and informational content with a precise engineering tone.

**`{colors.focus-yellow}` (`#F6E500`)** - Accessibility signal, not decorative sunshine. It is reserved for focus outlines and should not become a general highlight color.

---

## 07. Spacing
<!-- SOURCE: auto -->

Ferrari uses a named spacing ladder instead of anonymous Tailwind-like numbers.

| Token | Value | Use case |
|---|---:|---|
| `--f-space-xxxs` | 4px | micro gaps, dense share item adjustments |
| `--f-space-xxs` | 8px | small inline and share list gaps |
| `--f-space-xs` | 16px | paragraph margins, table cell padding |
| `--f-space-s` | 24px | desktop share gaps, fixed popover margins |
| `--f-space-m` | 32px | section-level medium rhythm |
| `--f-space-l` | 48px | large vertical rhythm |
| `--f-space-xl` | 64px | editorial band rhythm |
| `--f-space-xxl` | 96px | major section separation |
| `--f-space-super` | 128px | maximum breathing room |

**주요 alias**:
- `.f-mt-*`, `.f-mb-*`, `.f-pt-*`, `.f-pb-*` -> direct use of the spacing ladder.
- Table cells use `var(--f-space-xs)` -> 16px, keeping dense technical content readable.

### Whitespace Philosophy

Ferrari's spacing is not airy in the soft lifestyle sense. It alternates between full-screen media immersion and tightly controlled technical blocks. The hero uses the whole viewport as a photographic field, then the UI labels sit with exact, small distances so they do not disturb the image.

The ladder climbs from 4px to 128px, but the emotional unit is contrast: tiny navigation and share controls against huge media, then precise tables and text against clean white/black surfaces. Space is used to preserve authority around the car, not to create friendly openness.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `--f-radius-full` | 9999px | circular/pill controls |
| default component radius | 0 | tables, text surfaces, most chrome |
| circular hero CTA observed | approx 42px circle | arrow/play-style motion control |

The radius system is intentionally sparse. Ferrari does not use rounded card stacks as a dominant language. Roundness appears when a control needs to feel mechanical and pressable: circular arrows, icon buttons, or pill-like full-radius controls.

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `--f-shadow-small` | `0px 4px 8px 0px rgba(0,0,0,.1)` | small functional elevation |
| share toggle filter | `drop-shadow(1px 1px 1px rgba(0,0,0,.3))` | icon readability over media |
| gradient shadow dark | `linear-gradient(90deg,#121212,#161616)` | atmospheric surface shading |
| gradient shadow light | `linear-gradient(180deg,hsla(0,0%,9%,0),hsla(0,0%,9%,.85))` | media fade to dark |

Ferrari uses light shaping more than conventional elevation. If implementing from this guide, prefer overlays and gradients attached to media over generic card shadows.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / behavior | Value | Usage |
|---|---|---|
| global scroll | `scroll-behavior: smooth` | anchor and page movement |
| custom elements loading | `:not(:defined){opacity:0}` / `:defined{opacity:1}` | avoid unstyled web component flash |
| hero CTA observed | circular arrow / video discover affordance | invitation to move deeper |
| horizontal slider | `f-horizontal-slider swiper-container` with desktop/mobile split | gallery-like content movement |

Motion is implied by video and content modules more than CSS transition tokens. The captured hero should be treated as moving media with static, precise chrome.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: technical tables max at `961px`; full-bleed media ignores standard container width.
- **Grid type**: mixed full-bleed media + centered technical content.
- **Column count**: not expressed as a single global grid in captured CSS.
- **Gutter**: spacing tokens, especially 16px/24px/64px, drive local gutters.

### Hero

- **🆕 Pattern Summary**: `100vh + full-bleed automotive video/photo + centered uppercase H1 + compact discover CTA`
- Layout: transparent top navigation over media; logo at left; nav items across the top; hero title centered in the lower-middle of the frame.
- Background: dark blue/black photographic surface with a bright vehicle/light band.
- **🆕 Background Treatment**: `image/video-overlay` plus darkness for legibility; production CSS also exposes `--f-color-overlay: rgba(0,0,0,.3)` and gradient-to-background tokens.
- H1: visual approx `38px` / weight `500` / wide uppercase.
- Max-width: hero media full viewport; text centered, not placed in a card.

### Section Rhythm

```css
section {
  padding-block: var(--f-space-xl); /* often 64px or larger */
  padding-inline: var(--f-space-xs);
}
```

### Card Patterns

- **Card background**: usually `#FFFFFF` or theme surface; media modules are full-bleed.
- **Card border**: understated `1px solid var(--f-color-ui-20)` for tables/technical containers.
- **Card radius**: mostly 0; do not invent soft cards.
- **Card padding**: 16px cells for dense data; larger editorial bands use spacing tokens.
- **Card shadow**: minimal; use `--f-shadow-small` only for functional lift.

### Navigation Structure

- **Type**: transparent global top navigation.
- **Position**: top overlay on hero.
- **Height**: visual approx 80px in screenshot; share popover has fixed viewport logic and header offset of 40px when header down.
- **Background**: transparent over media; dark overlay/gradient handles contrast.
- **Border**: none in hero state.

### Content Width

- **Prose max-width**: not globally exposed; text components are narrow compared with full-bleed media.
- **Container max-width**: `961px` observed for tables.
- **Sidebar width**: N/A on homepage capture.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `< 601px` | base/mobile rules |
| Tablet | `601px` | title grows from 26px to 28px |
| Desktop | `961px` | desktop horizontal slider and share layout activate |
| Large | `1281px` | share radial background expands |
| Wide | `1601px` | share radial background expands further |

### Touch Targets

- **Minimum tap size**: not explicitly tokenized; share icon controls use 48px (`3pc`) square in icon mode.
- **Button height (mobile)**: not fully measured; circular hero CTA observed around 42px.
- **Input height (mobile)**: not surfaced in homepage artifacts.

### Collapsing Strategy

- **Navigation**: desktop nav visible in screenshot; mobile strategy not captured.
- **Grid columns**: media is full-bleed; tables remain width 100% with max-width constraints.
- **Sidebar**: N/A.
- **Hero layout**: preserve full-bleed media; center text; controls stay minimal.

### Image Behavior

- **Strategy**: full-bleed cinematic media for hero; AEM dynamic media components (`f-aem-dynamic-media-image`, smart crop video viewer) display as contents.
- **Max-width**: full viewport for hero; technical content maxes around 961px.
- **Aspect ratio handling**: media crop is intentional; screenshot shows abstract car-body/light crop rather than full vehicle inspection.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

Ferrari buttons are not a large rainbow system in the captured CSS. They are mostly transparent, typographic, and media-aware.

```html
<button class="f-hero-discover">
  <span>DISCOVER</span>
  <span class="f-hero-discover__circle">›</span>
</button>
```

| Property | Value |
|---|---|
| Font | `FerrariSans`, uppercase |
| Weight | 500 for label-like emphasis |
| Text color | `#FFFFFF` on hero |
| Background | transparent |
| Shape | circular arrow control, full-radius |
| Focus | `2px solid #F6E500` |

### Badges

No badge system was exposed in the homepage artifacts. If needed, build a badge as uppercase FerrariSans at 11-13px with `#181818`/`#FFFFFF` contrast and no soft colored fills unless a real Ferrari token demands it.

### Cards & Containers

Ferrari containers are either full-bleed media or technical tables.

```html
<f-table>
  <table>
    <thead><tr><th>Model</th><th>Value</th></tr></thead>
    <tbody><tr><td class="allinea-sx">Engine</td><td>V12</td></tr></tbody>
  </table>
</f-table>
```

| Property | Value |
|---|---|
| Background | `var(--f-color-ui-0)` |
| Border | top/bottom `1px solid var(--f-color-ui-20)` |
| Font size | 11px |
| Cell padding | `var(--f-space-xs)` = 16px |
| Header color | `var(--f-color-ui-60)` |
| Header transform | uppercase |

### Navigation

```html
<nav class="f-global-nav">
  <a>RACING</a>
  <a>SPORTS CARS</a>
  <a>COLLECTIONS</a>
  <a>EXPERIENCES</a>
  <a>ABOUT US</a>
</nav>
```

| Property | Value |
|---|---|
| Position | overlay at top of hero |
| Text | uppercase, small, wide tracking |
| Color | `#FFFFFF` over media |
| Background | transparent |
| Logo | white prancing horse at far left |

### Inputs & Forms

Form inputs were not surfaced in the captured homepage CSS beyond focus behavior. Any implementation should use `FerrariSans`, preserve the small type scale, and use `#F6E500` for focus outlines rather than red.

### Hero Section

```html
<section class="f-hero f-theme-dark">
  <video class="f-hero__media"></video>
  <nav class="f-global-nav">...</nav>
  <div class="f-hero__copy">
    <h1>FERRARI HYPERSAIL</h1>
    <p>A bold colour for a new era</p>
    <button>DISCOVER <span>›</span></button>
  </div>
</section>
```

| Property | Value |
|---|---|
| Height | full viewport / cinematic |
| Background | full-bleed media |
| Overlay | dark image/video overlay for legibility |
| H1 | uppercase, centered, white |
| CTA | transparent label + circular arrow |
| Chrome | transparent nav; no hero card |

### 13-2. Named Variants

#### `button-ghost-video`

| State | Spec |
|---|---|
| default | transparent background, `#FFFFFF` text, uppercase label |
| icon | circular outline/white arrow treatment, full radius |
| hover | keep white text; avoid filled red hover unless verified |
| focus | `outline: 2px solid #F6E500` |

#### `button-share-icon`

| State | Spec |
|---|---|
| default | transparent 48px icon target over media |
| shadow variant | `drop-shadow(1px 1px 1px rgba(0,0,0,.3))` |
| fixed popup | high z-index overlay, right aligned |
| focus | `outline: #F6E500 solid 2px; outline-offset: 4px` |

#### `table-technical`

| State | Spec |
|---|---|
| default | 11px table, `#FFFFFF` surface, `#D2D2D2` borders |
| odd row | `var(--f-color-ui-10)` background |
| header | muted color, uppercase, 500 weight |
| emphasized cell | left/right border plus bolder weight |

#### `nav-transparent-hero`

| State | Spec |
|---|---|
| default | white uppercase links over dark media |
| background | none; rely on hero media/overlay |
| spacing | generous horizontal separation; no nav pills |
| active | not captured; do not invent red underline |

### 13-3. Signature Micro-Specs

```yaml
rosso-corsa-ignition:
  description: "Ferrari red is treated as ignition, not page atmosphere."
  technique: "Use #DA291C / #F13A2C / #B01E0A / #9D2211 only for accent, warning, and selected brand moments; keep hero surfaces black/white/photo-first."
  applied_to: ["{colors.accent}", "{components.button-ghost-video}", "{components.nav-transparent-hero}"]
  visual_signature: "The page reads unmistakably Ferrari while refusing to become a red poster."

cinematic-media-dimming:
  description: "Full-bleed automotive media is darkened just enough for white chrome and centered title copy."
  technique: "Layer rgba(0,0,0,.3) overlay with gradient shadows such as linear-gradient(180deg,hsla(0,0%,9%,0),hsla(0,0%,9%,.85))."
  applied_to: ["{components.nav-transparent-hero}", "{components.button-ghost-video}"]
  visual_signature: "Car-body light becomes the room; the UI reads like small labels on a black stage."

media-only-readability-shadow:
  description: "Shadow is reserved for legibility over photography, not for card hierarchy."
  technique: "Use drop-shadow(1px 1px 1px rgba(0,0,0,.3)) on share/icon chrome and minimal 0px 4px 8px rgba(0,0,0,.1) only for functional lift."
  applied_to: ["{components.button-share-icon}"]
  visual_signature: "Icons stay readable over video while the rest of the interface remains flat and disciplined."

ferrari-small-technical-type:
  description: "Small FerrariSans with wide tracking turns luxury into measured engineering."
  technique: "body font-size 13px; line-height 1.5; letter-spacing 0.015em; weights limited to 400 and 500."
  applied_to: ["{components.table-technical}", "{components.nav-transparent-hero}", "{components.button-ghost-video}"]
  visual_signature: "The text feels like instrument labeling or a pit-wall spec sheet, not lifestyle copy."

yellow-focus-instrument:
  description: "Yellow is an accessibility instrument and named product signal, not a second brand CTA color."
  technique: "Reserve #F6E500 for focus outlines with 2px solid / 4px offset; keep #FFF200 scoped to Hypersail color contexts."
  applied_to: ["{colors.focus-yellow}", "{colors.hypersail-yellow}", "{components.button-share-icon}", "{components.button-ghost-video}"]
  visual_signature: "A bright yellow signal appears only at interaction or product-color moments, never as general decoration."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Short uppercase product/event phrase | "FERRARI HYPERSAIL" |
| Subheading | Compact emotional/technical support line | "A bold colour for a new era" |
| Primary CTA | Single imperative verb | "DISCOVER" |
| Navigation | Category nouns in uppercase | "RACING", "SPORTS CARS", "COLLECTIONS" |
| Tone | cinematic, precise, restrained | brand confidence without explanatory clutter |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Ferrari - copy into your root stylesheet */
:root {
  /* Fonts */
  --f-ferrari-font: "FerrariSans", "Noto Sans", -apple-system, BlinkMacSystemFont, sans-serif;
  --f-font-weight-normal: 400;
  --f-font-weight-bold: 500;

  /* Brand */
  --f-color-accent-100: #DA291C;
  --f-color-accent-90: #B01E0A;
  --f-color-accent-80: #9D2211;
  --f-color-yellow-hypersail: #FFF200;
  --f-color-focus: #F6E500;

  /* Surfaces */
  --f-color-global-white: #FFFFFF;
  --f-color-global-black: #181818;
  --f-color-background-0: #FFFFFF;
  --f-color-background-10: #EBEBEB;
  --f-color-ui-100: #181818;
  --f-color-ui-60: #666666;
  --f-color-ui-20: #D2D2D2;
  --f-color-ui-10: #F7F7F7;
  --f-color-ui-0: #FFFFFF;

  /* Key spacing */
  --f-space-xxs: 8px;
  --f-space-xs: 16px;
  --f-space-s: 24px;
  --f-space-m: 32px;
  --f-space-l: 48px;
  --f-space-xl: 64px;
  --f-space-xxl: 96px;
  --f-space-super: 128px;

  /* Radius + shadow */
  --f-radius-full: 9999px;
  --f-shadow-small: 0px 4px 8px 0px rgba(0,0,0,.1);
}

.f-theme-dark {
  --f-color-background-0: #181818;
  --f-color-background-10: #383838;
  --f-color-ui-100: #FFFFFF;
  --f-color-ui-60: #D2D2D2;
  --f-color-ui-20: #666666;
  --f-color-ui-10: #303030;
  --f-color-ui-0: #181818;
  --f-color-accent-100: #F13A2C;
}

body {
  background: var(--f-color-background-0);
  color: var(--f-color-ui-100);
  font-family: var(--f-ferrari-font);
  font-size: 13px;
  font-weight: var(--f-font-weight-normal);
  letter-spacing: 0.015em;
  line-height: 1.5;
}

h1, h2, h3, h4, h5, h6, strong {
  font-weight: var(--f-font-weight-bold);
}

:focus-visible {
  outline: 2px solid var(--f-color-focus);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js - Ferrari inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        ferrari: {
          red: '#DA291C',
          redDark: '#B01E0A',
          redDeep: '#9D2211',
          yellow: '#F6E500',
          hypersail: '#FFF200',
          black: '#181818',
          white: '#FFFFFF',
          surface: '#F7F7F7',
          border: '#D2D2D2',
          muted: '#666666',
        },
      },
      fontFamily: {
        sans: ['FerrariSans', 'Noto Sans', 'system-ui', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
      },
      borderRadius: {
        full: '9999px',
      },
      spacing: {
        'f-xxs': '8px',
        'f-xs': '16px',
        'f-s': '24px',
        'f-m': '32px',
        'f-l': '48px',
        'f-xl': '64px',
        'f-xxl': '96px',
        'f-super': '128px',
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
| Brand primary | `--f-color-accent-100` | `#DA291C` |
| Brand primary on dark | `.f-theme-dark --f-color-accent-100` | `#F13A2C` |
| Background light | `--f-color-background-0` light | `#FFFFFF` |
| Background dark | `--f-color-background-0` dark | `#181818` |
| Text primary light | `--f-color-ui-100` light | `#181818` |
| Text primary dark | `--f-color-ui-100` dark | `#FFFFFF` |
| Border | `--f-color-ui-20` light | `#D2D2D2` |
| Focus | `--f-color-focus` | `#F6E500` |
| Error/warning | `--f-color-accessible-warning` | `#F13A2C` |

### Example Component Prompts

#### Hero Section

```text
Create a Ferrari-style automotive hero.
- Full-viewport background video/photo with dark overlay, no decorative gradient mesh.
- Transparent top navigation with small uppercase FerrariSans links in #FFFFFF.
- Centered H1 in uppercase FerrariSans, weight 500, wide tracking, white.
- CTA is a transparent "DISCOVER" label plus circular arrow, not a filled red button.
- Use #181818 and #FFFFFF as the dominant contrast; reserve #DA291C for rare accent only.
```

#### Technical Table

```text
Create a Ferrari-style technical specification table.
- Surface: #FFFFFF, text #181818, border top/bottom 1px #D2D2D2.
- Font: FerrariSans or Noto Sans, 11px, line-height 1.5.
- Header: uppercase, weight 500, muted #666666.
- Cell padding: 16px.
- Odd rows may use #F7F7F7.
```

#### Navigation

```text
Create Ferrari-style hero navigation.
- Position over full-bleed dark media.
- Use white prancing-horse style logo placeholder at far left.
- Links are uppercase, small, widely spaced, weight 500.
- No pills, no underlines, no red active indicator unless explicitly verified.
- Focus outline must use #F6E500.
```

### Iteration Guide

- **색상 변경 시**: keep the page black/white/media-first; `#DA291C` is not a background default.
- **폰트 변경 시**: use 400/500 only and preserve the small 13px base.
- **여백 조정 시**: stay on the Ferrari ladder: 8, 16, 24, 32, 48, 64, 96, 128.
- **새 컴포넌트 추가 시**: avoid soft card UI; prefer flat surfaces, lines, and full-bleed media.
- **다크 모드**: use `.f-theme-dark` mappings; do not invert colors manually with opacity hacks.
- **반응형**: preserve the hero media crop and central title first; navigation can collapse, but the cinematic field should remain.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `FerrariSans` or a corrected sans fallback with 400/500 weights only.
- Start from cinematic full-bleed media for hero sections.
- Keep body text small: 13px base with `letter-spacing: 0.015em`.
- Use `#DA291C` as a restrained Ferrari accent.
- Use `#F6E500` for focus outlines and accessibility signal.
- Use `#181818` and `#FFFFFF` as the main contrast pair.
- Keep radius mostly zero except circular/full-radius controls.
- Use table borders and muted text for technical information.
- Shape media legibility with dark overlays/gradients rather than UI cards.

### ❌ DON'T

- 배경 전체를 `#DA291C` 또는 `#F13A2C`로 두지 말 것 — 대신 hero media, `#181818`, 또는 `#FFFFFF` 사용.
- 텍스트를 `#000000`로 고정하지 말 것 — light theme primary는 `#181818`, dark/media primary는 `#FFFFFF` 사용.
- Hero 배경을 `#FFFFFF` 빈 화면으로 두지 말 것 — 대신 full-bleed media + dark overlay 사용.
- Focus ring을 `#DA291C`로 두지 말 것 — 대신 `#F6E500` 사용.
- Body에 `font-size: 16px`를 기본값으로 사용 금지 — Ferrari base는 `13px`가 맞다.
- Headline에 `font-weight: 700` 또는 `800` 사용 금지 — captured system uses 500 for headings.
- Card radius를 `12px` 또는 `16px`로 만들지 말 것 — 대부분 `0`, controls only `9999px`.
- SaaS-style purple gradient `#667EEA` / `#764BA2` 사용 금지 — Ferrari uses media gradients and red/neutral tokens.
- Border를 `#E5E7EB`로 일반화하지 말 것 — Ferrari light border is closer to `#D2D2D2`.
- Muted text를 `#9CA3AF`로 Tailwind default 처리하지 말 것 — Ferrari uses `#666666`, `#8F8F8F`, and theme remaps.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second primary brand color: none. Red is the one canonical brand accent; yellow is focus/product-specific, not a second CTA brand.
- Heavy font weights: absent in the captured CSS. No 700, 800, or black display posture.
- Soft SaaS cards: none as a homepage identity. Do not build nested rounded cards.
- Decorative gradient mesh: none. Gradients are shadows, overlays, or Ferrari red/dark-grey ramps.
- Serif luxury typography: none. The premium signal is technical sans precision.
- Broad red backgrounds: avoided. Ferrari can be Ferrari with almost no red on the hero.
- Chrome shadows: nearly none. Depth belongs to media and controlled overlays.
- Friendly oversized body copy: absent. Small, measured labels and technical type dominate.
- Generic blue focus ring: absent. Focus is Ferrari yellow `#F6E500`.
- Form-heavy UI language: not surfaced in homepage artifacts; do not turn the page into a dashboard.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Locale mismatch**: the local `index.html` capture canonicalizes to a Korean Ferrari URL while the requested analysis URL is `https://www.ferrari.com/en-US`. The global design system is shared, but copy examples and some page modules may differ by locale.
- **Typography extraction gap**: `phase1/typography.json` contains no parsed scale entries. Typography values here rely on production CSS rules and visual observation of the hero screenshot.
- **Homepage-only evidence**: configurator, checkout, dealer forms, account flows, and store flows were not visited. Form validation states and purchase components are therefore not specified.
- **Motion not deeply instrumented**: CSS and screenshot imply video/slider behavior, but JavaScript timelines, scroll-trigger curves, and animation easing were not measured.
- **Exact hero text metrics**: hero H1 size is visually estimated from the screenshot because the relevant component CSS was not fully tokenized in phase1 JSON.
- **Token alias layer sparse**: `alias_layer.json` reported empty tier arrays even though CSS contains semantic remaps. This guide treats the CSS theme variables as the reliable source.
- **Color frequency contamination**: frequency counts include raw black/white and gradient internals; they are useful as evidence but not a perfect usage map.
- **Image crop dependency**: the Ferrari feel depends heavily on actual automotive media. Reusing the tokens without strong photography/video will not reproduce the site identity.
- **Mobile navigation not observed**: desktop hero screenshot and CSS breakpoints were available, but a mobile screenshot was not part of the reused phase1 artifacts.
