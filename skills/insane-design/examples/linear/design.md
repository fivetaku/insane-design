---
schema_version: 3.2
slug: linear
service_name: Linear
site_url: https://linear.app
fetched_at: 2026-04-20T19:29:00+09:00
default_theme: mixed
brand_color: "#7070FF"
primary_font: "Inter Variable"
font_weight_normal: 400
token_prefix: "color"

bold_direction: "Cool Productivity"
aesthetic_category: "Industrial Minimalism"
signature_element: "hero_impact"
code_complexity: high

medium: web
medium_confidence: high

archetype: app-dashboard
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "721 CSS variables, 355 resolved tokens, action/component aliases, and consistent marketing/app component patterns."

colors:
  primary: "#7070FF"
  primary-dark: "#5E6AD2"
  primary-hover: "#8989F0"
  surface-dark: "#08090A"
  surface-panel: "#0F1011"
  surface-light: "#FFFFFF"
  text-dark-primary: "#F7F8F8"
  text-light-primary: "#282A30"
  text-muted-light: "#6F6E77"
  border-light: "#E9E8EA"
  border-dark: "#23252A"
typography:
  display: "Inter Variable"
  body: "Inter Variable"
  mono: "Berkeley Mono"
  ladder:
    - { token: hero, size: "38px mobile / fluid desktop", weight: 680, tracking: "tight optical" }
    - { token: body, size: "16px", weight: 400, tracking: "0" }
    - { token: label, size: "12px-13px", weight: 510, tracking: "0" }
  weights_used: [300, 400, 510, 590, 680]
  weights_absent: [800, 900]
components:
  button-primary: { bg: "{colors.primary}", radius: "9999px", height: "40px", transition: ".16s var(--ease-out-quad)" }
  button-invert: { bg: "#282A30", hover_bg: "#1F2024", radius: "9999px" }
  command-menu: { bg: "#F8F8F8", radius: "8px", input_height: "62px" }
  header-glass: { bg: "rgba(255,255,255,0.8)", blur: "20px", height: "72px" }
---

# DESIGN.md — Linear (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Linear's marketing surface is near-black canvas holding product dashboard precision in a hairline grid. The page is not a cheerful SaaS homepage with floating illustrations; it is the public face of an internal operating system, where #08090A (`{colors.surface-dark}`) functions as the canvas floor and thin violet signals mark the only actionable instruments.

The dashboard logic governs every decision. Issue rows, command surfaces, label pills, and status dots are not decoration — they are product evidence arranged on the canvas with the same discipline the app applies inside the product. The page reads like a live dashboard with the house lights dimmed: precise, awake, and structured around the work rather than around the selling of work.

The rhythm of the layout is split-personality but controlled. Large cinematic hero zones open the canvas, then snap into 40px issue rows like a project board closing ranks. Strategy is projected in calm display type; execution lives below in compact rows, pills, and hairline surfaces. That rhythm is why Linear feels less like a marketing site and more like a mission-control dashboard you accidentally found publicly accessible.

The signature color is #7070FF (`{colors.primary}`) — a functional signal for CTA, link, status pulse, and selected affordance. There is no second brand color competing for mood. Violet is the runway light on the product floor, not the paint on the walls. The canvas lets dark neutrals carry the weight, then lets violet appear precisely where a product team should act. `Berkeley Mono` appears at developer-credibility touchpoints, reinforcing the dashboard-instrument register rather than the brand-poster register.

Depth is anti-shadow. Linear draws structure with 1px hairline borders and inset rings — precision-machined seams, not stacked glossy cards. Motion enters as blur-and-vertical-offset, as if the interface is focusing a lens rather than performing an animation. The dashboard canvas stays alive without becoming playful.

### Key Characteristics

- Dark-first marketing identity anchored in #08090A and #0F1011.
- Single violet action lane: #7070FF on light surfaces, #5E6AD2 on darker accents, #828FFF/#8989F0 for hover.
- Product UI fragments are part of the visual language: issue rows, labels, command menu, panels, and small status dots.
- Header glass uses `--header-blur: 20px` with translucent white/dark backgrounds.
- 12-column homepage grid collapses through 1024px, 768px, and 640px breakpoints.
- Radius is small for panels (`6px`/`8px`) and fully rounded for controls (`9999px`).
- Shadows are mostly suppressed; structure comes from hairline borders and inset rings.
- Motion is short and utilitarian: `.16s`, `.15s`, `.25s`, plus occasional cubic-bezier reveal.
- Nonstandard font weights `510`, `590`, `680` are part of the optical identity.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Cool Productivity
> **Aesthetic Category**: Industrial Minimalism
> **Signature Element**: 이 사이트는 **dark product cockpit with violet action signals**으로 기억된다.
> **Code Complexity**: high — 721 CSS variables, breakpoint-heavy layouts, blur/glass header, command-menu states, and product-panel micro-interactions.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Linear처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter Variable", "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #08090A;
  --panel: #0F1011;
  --fg: #F7F8F8;
  --muted: #8A8F98;
  --hairline: #23252A;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root {
  --brand: #7070FF;
  --brand-dark: #5E6AD2;
  --brand-hover: #8989F0;
}
```

**절대 하지 말아야 할 것 하나**: violet을 배경 장식으로 넓게 뿌리지 말 것. Linear의 보라색은 액션/상태 신호이며, 넓은 면은 #08090A, #0F1011, #FFFFFF 같은 neutral surface가 맡는다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://linear.app` |
| Fetched | 2026-04-20T19:29:00+09:00 |
| Extractor | reused phase1: HTML/CSS/screenshots already present |
| HTML size | 2,297,234 bytes |
| CSS files | 20 external CSS files, 462,401 CSS chars |
| Token prefix | `--color-*`, `--radius-*`, `--font-*`, `--button-*` |
| Method | CSS custom properties + phase1 JSON + targeted CSS/HTML interpretation |
| Screenshot | `insane-design/linear/screenshots/hero-cropped.png` |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js-style static chunks with CSS modules and hashed class names.
- **Design system**: Linear web system — prefix families include `--color-*`, `--radius-*`, `--font-*`, `--button-*`, `--header-*`.
- **CSS architecture**:
  ```text
  core        --color-bg-primary / --color-text-primary / --radius-8
  action      --button-height / --button-padding / --color-button-invert-bg
  component   --input-height / --inner-card-border / --layer-dialog-overlay
  runtime     CSS module classes such as .Hero_title__sHOGp and .Button_variant__1FJO9
  ```
- **Class naming**: CSS Modules with component prefix + hash suffix: `.Hero_title__sHOGp`, `.CommandMenu_dialog__GVV7m`, `.Button_variant__1FJO9`.
- **Default theme**: mixed. Marketing hero leans dark (#08090A), while product/documentation panels include light tokens (#FFFFFF, #F8F8F8).
- **Font loading**: `@font-face` for `Inter Variable` and `Berkeley Mono` from `https://static.linear.app/fonts/...`.
- **Canonical anchor**: app-dashboard product-development positioning: "The product development system for teams and agents."

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Inter Variable` (self-hosted variable font)
- **Body font**: `Inter Variable`, with `"SF Pro Display"`, `-apple-system`, BlinkMacSystemFont, `"Segoe UI"`, Roboto, Oxygen, Ubuntu, Cantarell, Open Sans, Helvetica Neue fallback chain
- **Code font**: `Berkeley Mono`, then `ui-monospace`, `"SF Mono"`, Menlo, monospace
- **Weight normal / medium / semibold / bold**: `400` / `510` / `590` / `680`

```css
:root {
  --font-regular: "Inter Variable", "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-monospace: "Berkeley Mono", ui-monospace, "SF Mono", "Menlo", monospace;
  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 510;
  --font-weight-semibold: 590;
  --font-weight-bold: 680;
}
body {
  font-family: var(--font-regular);
  font-weight: var(--font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Inter Variable** — Use the real variable font when possible. If substituting with open-source Inter, keep optical density by using `font-weight: 510` for medium UI labels and `590` for semibold labels rather than rounding everything to 500/600.
- **Berkeley Mono** — If unavailable, use `SF Mono` or `JetBrains Mono` at the same size but reduce visual dominance: keep mono snippets at 12px-13px and do not use bold mono for headings.
- **Display compensation** — Do not replace the hero with a geometric display face. Use Inter-like forms, tight line-height, and restrained tracking. Linear's premium feeling comes from precision, not font personality.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Hero title mobile | `38px` | `680` | tight / display | optical tight |
| Body | `16px` | `400` | readable product copy | `0` |
| Button small | `13px` | `510` | `32px` button height | `0` |
| Button mini | `12px` | `510` | `24px` button height | `0` |
| Command input | `18px` | inherited/400 | `62px` input height | `0` |
| Group heading | `12px` | 400/510 | `30px` row height | `0` |
| Issue row | compact UI text | 400/510 | `40px` row height | `0` |

> ⚠️ Linear's typography extractor did not recover a complete named scale, but CSS exposes the important identity: variable Inter, Berkeley Mono, and nonstandard weights `510`, `590`, `680`.

### Principles
<!-- SOURCE: manual -->

1. Body is plain `400`; emphasis is created with calibrated variable weights rather than heavy type.
2. Medium is `510`, not `500` — this keeps labels crisp without the swollen look of default semibold UI.
3. Semibold is `590`, not `600`; bold is `680`, not `700`. Preserve these exact values for Linear-like density.
4. Mono is an accent for tooling surfaces, never a brand-wide display choice.
5. Display type should feel compressed and intentional, but body tracking remains neutral.
6. Small labels are functional. They should sit inside rows, pills, and controls rather than becoming decorative captions.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (5 steps)
<!-- --color-brand / --color-accent -->

| Token | Hex |
|---|---|
| `--color-brand-bg` dark | `#5E6AD2` |
| `--color-brand-bg` light | `#7070FF` |
| `--color-accent` | `#7170FF` |
| `--color-accent-hover` dark | `#828FFF` |
| `--color-accent-hover` light | `#8989F0` |
| `--color-accent-tint` dark | `#18182F` |
| `--color-accent-tint` light | `#F1F1FF` |

### 06-2. Brand Dark Variant
<!-- SOURCE: auto -->

| Token | Hex |
|---|---|
| `--color-bg-primary` dark | `#08090A` |
| `--color-bg-panel` | `#0F1011` |
| `--color-border-primary` dark | `#23252A` |
| `--color-line-primary` dark | `#37393A` |
| `--color-text-primary` dark | `#F7F8F8` |
| `--color-link-primary` dark | `#828FFF` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light | Dark |
|---|---|---|
| Page | `#FFFFFF` | `#08090A` |
| Panel | `#F8F8F8` | `#0F1011` |
| Level 2 | `#F4F4F4` | `#141516` |
| Border primary | `#E9E8EA` | `#23252A` |
| Line primary | `#D4D4D6` | `#37393A` |
| Text primary | `#282A30` | `#F7F8F8` |
| Text secondary | `#3C4149` | `#B4BCD0` |
| Text muted | `#6F6E77` | `#8A8F98` |

### 06-4. Accent Families
<!-- SOURCE: auto -->

| Family | Key step | Hex |
|---|---|---|
| Indigo / brand | primary action | `#7070FF` |
| Indigo / dark action | dark brand | `#5E6AD2` |
| Blue | product signal | `#21B3FF` |
| Green | product signal | `#27A644` |
| Orange | product signal | `#FC7840` |
| Red | error/destructive | `#EB5757` |
| Yellow | warning/status | `#F0BF00` |
| Teal | product signal | `#00B8CC` |

### 06-5. Semantic
<!-- SOURCE: auto -->

| Token | Hex | Usage |
|---|---|---|
| `--color-bg-primary` | `#FFFFFF` / `#08090A` | theme-dependent page background |
| `--color-bg-panel` | `#0F1011` | dark product panel |
| `--color-text-primary` | `#282A30` / `#F7F8F8` | primary readable text |
| `--color-text-tertiary` | `#6F6E77` | secondary labels and muted copy |
| `--color-border-primary` | `#E9E8EA` / `#23252A` | default hairline border |
| `--color-link-primary` | `#7070FF` / `#828FFF` | links and action text |
| `--color-button-invert-bg` | `#282A30` | dark button on light surface |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--btn-highlight-bg` | `--sx-629164` | highlighted button background |
| `--btn-highlight-color` | `--sx-ys2i3t` | highlighted button text |
| `--button-corner-radius` | `--radius-4` / rounded variant | button radius API |
| `--color-button-invert-bg` | `#282A30` | inverse button |
| `--color-button-invert-bg-hover` | `#1F2024` | inverse button hover |
| `--inner-card-border` | component alias | card shell border |
| `--input-height` | component alias | command/input sizing |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto (CSS frequency count) -->

| Token | Hex | Frequency / role |
|---|---|---|
| dark surface | `#08090A` | high in dark hero/SVG patterns |
| surface panel | `#0F1011` | repeated panel/background token |
| brand dark | `#5E6AD2` | CTA/status pulse |
| light surface | `#FFFFFF` | light theme panels and text-on-brand |
| text dark primary | `#F7F8F8` | dark theme text |
| accent hover | `#828FFF` | dark theme link/action |
| light text | `#282A30` | light theme text |
| light border | `#E9E8EA` | light theme hairline |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.primary}` (`#7070FF`)** — Linear's light-surface action color. Use it for primary CTA backgrounds, links, selected states, and agent/product action moments. It should feel like a signal in an otherwise neutral interface.

**`{colors.surface-dark}` (`#08090A`)** — The marketing cockpit floor. It gives the hero its product-operator mood and prevents violet from becoming decorative.

**`{colors.text-light-primary}` (`#282A30`)** — The light-mode ink. It is not pure black; the slight softness keeps dense product copy from looking like a generic admin template.

**`{colors.border-light}` (`#E9E8EA`)** — The structural line. Linear's UI often uses hairlines and inset rings instead of visible shadows, so this border token carries much of the layout discipline.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--header-height` | `72px` | global marketing header height |
| `--page-padding-inline` | `24px` | default page inline padding |
| `--page-padding-block` | `64px` | default vertical section padding |
| `--page-max-width` | `1024px` | standard content container |
| `--prose-max-width` | `624px` | readable prose width |
| `--homepage-outer-padding` | `46px` desktop / `28px` laptop / `10px` large | homepage shell padding |
| `--homepage-padding-inset` | `32px` desktop / `8px` small | inner grid inset |
| card grid gap | `64px` | marketing cards grid separation |
| command menu input padding | `20px` | command input inner spacing |

**주요 alias**:
- `--page-padding-left/right` → `max(env(safe-area-inset-*), var(--page-padding-inline))`
- `--homepage-max-width` → `calc(1344px + var(--homepage-outer-padding) * 2)`
- `--grid-columns` → `12` desktop, `4` mobile

### Whitespace Philosophy
<!-- SOURCE: manual -->

Linear alternates between open strategic space and compact operational density. The hero and pillar sections use large vertical moves (`460px`+ top staging in some hero variants, `128px` bottom padding), then product UI fragments collapse into 40px issue rows and 12px labels. That contrast is intentional: the page sells calm planning, then proves execution density.

The spacing system should not feel like a symmetric landing-page ladder. Use wide air above major messages, exact 24px/32px page insets, and dense card or row interiors. Linear's air is editorial at the section level and utilitarian inside the product panels.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--radius-4` | `4px` | small controls, button corner alias in compact cases |
| `--radius-6` | `6px` | cards and small containers |
| `--radius-8` | `8px` | dialogs, command menu, larger panels |
| `--radius-12` | `12px` | larger containers |
| `--radius-16` | `16px` | large product surfaces |
| `--radius-24` | `24px` | large media/panel rounding |
| `--radius-32` | `32px` | oversized showcase surfaces |
| `--radius-rounded` | `9999px` | pill buttons and labels |
| `--radius-circle` | `50%` | avatars, pulse dots, icon circles |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `1024px` standard, `1344px + outer padding` for homepage shell
- **Grid type**: CSS Grid + Flexbox hybrid
- **Column count**: `12` homepage grid, `4` mobile grid token, specific 2/3-column feature grids
- **Gutter**: page insets `24px`/`32px`, card grid `64px`, responsive collapse at `768px` and `640px`

### Hero
- **🆕 Pattern Summary**: dark product cockpit + centered display message + animated reveal spans + product panel evidence below
- Layout: centered headline with responsive line breaks; supporting product visuals/panels staged around the hero
- Background: dark #08090A / #0F1011 with gradients and product-panel overlays
- **🆕 Background Treatment**: dark solid + radial/linear gradient fades; example CSS uses `linear-gradient(to bottom in oklab, rgba(8,9,10,0) 0, rgba(8,9,10,0) 75%, var(--color-bg-primary) 100%)`
- H1: `38px` mobile override, desktop fluid display inferred from hero class; weight `680`; tight optical tracking
- Max-width: responsive; hero title mobile `max-width: 360px`, description variants `276px`-`378px`

### Section Rhythm
```css
:root {
  --page-padding-inline: 24px;
  --page-padding-block: 64px;
  --page-max-width: 1024px;
  --homepage-max-width: calc(1344px + var(--homepage-outer-padding) * 2);
}
```

### Card Patterns
- **Card background**: dark panels #0F1011 or light panels #FFFFFF/#F8F8F8 depending on section
- **Card border**: `1px` hairline via `--color-border-translucent`, `--color-border-primary`, or inset ring
- **Card radius**: `6px` for small cards, `8px` for dialogs, larger media can reach `16px`+
- **Card padding**: variable; dense product rows use 24px/32px inline rhythm
- **Card shadow**: mostly `--shadow-none`; depth appears through inset border, subtle overlays, occasional `0 4px 32px rgba(8,9,10,.6)`

### Navigation Structure
- **Type**: horizontal marketing nav with responsive visibility helpers
- **Position**: header layer `--layer-header: 100`, commonly sticky/fixed style behavior
- **Height**: `72px`
- **Background**: translucent header background such as `rgba(255,255,255,0.8)` on light surfaces; dark counterpart inferred from theme tokens
- **Border**: `rgba(0,0,0,0.08)` / dark translucent hairline
- **Blur**: `--header-blur: 20px`

### Content Width
- **Prose max-width**: `624px`
- **Container max-width**: `1024px`, homepage `calc(1344px + outer padding * 2)`
- **Sidebar width**: not a primary homepage layout feature; product fragments use dense internal side/row structures

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

Linear buttons are pill-first controls with compact size variants.

```css
.Button_variant__1FJO9 {
  font-weight: var(--font-weight-medium);
  font-size: var(--button-font-size);
  line-height: var(--button-height);
  height: var(--button-height);
  gap: var(--button-gap);
  padding: var(--button-padding);
  border-radius: var(--button-corner-radius);
  transition: .16s var(--ease-out-quad);
  transition-property: border, background-color, color, box-shadow, opacity, filter, transform;
}
```

| Variant | Height | Font | Padding | Radius | State |
|---|---|---|---|---|---|
| mini | `24px` | `12px` / `510` | `0 10px` | rounded | compact utility |
| small | `32px` | `13px` / `510` | `0 12px` | rounded | nav/secondary |
| primary | approx `40px` | `510` | pill padding | `9999px` | CTA |
| invert | variable | `510` | pill padding | `9999px` | `#282A30` to `#1F2024` hover |

### Badges

Badges and labels are operational, not decorative.

- Shape: `9999px` pill.
- Typical height: `24px`-`26px`.
- Font: `12px`, `var(--font-weight-medium)` (`510`).
- Border: `1px solid var(--color-border-primary)`.
- Color: muted text such as `#6F6E77` or dark-theme equivalents.

### Cards & Containers

Cards behave like product surfaces. They avoid heavy drop shadows and rely on border/radius/contrast.

| Pattern | Spec |
|---|---|
| marketing card | `border-radius: 6px`, image aspect ratio `400/225`, hover arrow `translateY(-1px)` |
| command menu dialog | `max-width: 600px`, `top: 15%`, `border-radius: 8px`, `border: 1px solid var(--color-border-translucent)` |
| issue row | `height: 40px`, dense flex alignment, hover overlay `rgba(255,255,255,.025)` |
| product panel | dark surface #0F1011, inset/hairline border, minimal shadow |

### Navigation

The nav should feel like app chrome, not a landing page ornament.

- Header height: `72px`.
- Layer: `--layer-header: 100`.
- Blur: `20px`.
- Links: small Inter labels, muted by default, brighter on active/hover.
- Responsive helpers: `.hide-mobile`, `.show-mobile`, `.hide-tablet`, `.hide-laptop`, `.hide-desktop` classes at 640/768/1024/1280 thresholds.

### Inputs & Forms

The clearest captured input surface is command-menu search.

```css
.CommandMenu_input__Gs5bK {
  height: 62px;
  background: transparent;
  color: var(--color-text-primary);
  border-bottom: 1px solid var(--color-border-translucent);
  padding: 20px;
  width: 100%;
  font-size: 18px;
}
```

- Focus style: no visible outline on command input; surface containment and keyboard navigation carry the state.
- Error/loading states: not observed on homepage capture.
- Overlay: `var(--color-overlay-primary)` and `--layer-dialog-overlay: 699`.

### Hero Section

Hero text uses animated spans with initial `opacity: 0`, `filter: blur(10px)`, and `transform: translateY(20%)`. The visible text is paired with a visually-hidden full sentence for accessibility. This is important: replicate the reveal craft, but keep the semantic text intact.

### 13-2. Named Variants
<!-- SOURCE: manual -->

#### `button-primary`

| Property | Value |
|---|---|
| Background | `#7070FF` on light surfaces / `#5E6AD2` dark accent |
| Text | `#FFFFFF` |
| Radius | `9999px` |
| Weight | `510` |
| Transition | `.16s var(--ease-out-quad)` |

#### `button-invert`

| Property | Value |
|---|---|
| Background | `#282A30` |
| Hover background | `#1F2024` |
| Text | `#FFFFFF` |
| Usage | dark call-to-action on light/neutral surfaces |

#### `header-glass`

| Property | Value |
|---|---|
| Height | `72px` |
| Blur | `20px` |
| Light bg | `rgba(255,255,255,0.8)` |
| Border | `rgba(0,0,0,0.08)` |

#### `command-menu`

| Property | Value |
|---|---|
| Width | `600px` max |
| Top | `15%` |
| Radius | `8px` |
| Input height | `62px` |
| Animation | `175ms var(--ease-out-quad)` |

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
linear-variable-weight-ladder:
  description: "Linear's UI density comes from calibrated variable weights rather than browser-default medium/bold steps."
  technique: "--font-weight-medium: 510; --font-weight-semibold: 590; --font-weight-bold: 680; body weight 400"
  applied_to: ["{component.button-primary}", "{component.button-invert}", "labels", "headings", "dense product UI"]
  visual_signature: "Crisp product text that never swells into generic 500/600/700 SaaS typography."

linear-glass-header-chrome:
  description: "The marketing nav behaves like app chrome floating over the surface."
  technique: "--header-height: 72px; --header-blur: 20px; background rgba(255,255,255,0.8); border rgba(0,0,0,0.08)"
  applied_to: ["{component.header-glass}", "global marketing navigation"]
  visual_signature: "A translucent command-shell header with polish but almost no decorative weight."

hairline-not-shadow-depth:
  description: "Linear builds hierarchy with 1px structure and inset rings instead of stacked card elevation."
  technique: "--shadow-low/medium/high resolve to none; use 1px borders, 0 0 0 1px inset rings, #E9E8EA / #23252A hairlines"
  applied_to: ["{component.command-menu}", "cards", "product panels", "issue rows"]
  visual_signature: "Precise tool-surface depth: flat, machined, and dense rather than shadowy."

blurred-span-hero-reveal:
  description: "Hero language enters like an interface coming into focus, not like marketing animation."
  technique: "per-span opacity: 0; filter: blur(10px); transform: translateY(20%); short reveal timing"
  applied_to: ["hero H1 spans", "visually-hidden semantic hero sentence companion"]
  visual_signature: "A calm focusing motion that signals product intelligence without bounce or playfulness."

violet-action-signal-lane:
  description: "The brand color is constrained to action/status moments instead of atmospheric decoration."
  technique: "primary #7070FF on light actions; #5E6AD2 dark accent; #828FFF/#8989F0 hover/link states; avoid broad violet background washes"
  applied_to: ["{component.button-primary}", "links", "status pulse dots", "selected affordances"]
  visual_signature: "One violet instrument light inside a neutral cockpit, with no competing second brand color."
```

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Linear — copy into your root stylesheet */
:root {
  /* Fonts */
  --linear-font-family: "Inter Variable", "SF Pro Display", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --linear-font-family-code: "Berkeley Mono", ui-monospace, "SF Mono", Menlo, monospace;
  --linear-font-weight-normal: 400;
  --linear-font-weight-medium: 510;
  --linear-font-weight-semibold: 590;
  --linear-font-weight-bold: 680;

  /* Brand */
  --linear-color-brand-500: #7070FF;
  --linear-color-brand-600: #5E6AD2;
  --linear-color-brand-hover: #8989F0;
  --linear-color-brand-dark-hover: #828FFF;
  --linear-color-accent-tint: #F1F1FF;

  /* Surfaces */
  --linear-bg-dark: #08090A;
  --linear-bg-panel: #0F1011;
  --linear-bg-light: #FFFFFF;
  --linear-bg-light-secondary: #F8F8F8;
  --linear-text-dark: #F7F8F8;
  --linear-text-light: #282A30;
  --linear-text-muted: #6F6E77;
  --linear-border-light: #E9E8EA;
  --linear-border-dark: #23252A;

  /* Layout */
  --linear-header-height: 72px;
  --linear-header-blur: 20px;
  --linear-page-max-width: 1024px;
  --linear-prose-max-width: 624px;
  --linear-page-padding-inline: 24px;
  --linear-page-padding-block: 64px;

  /* Radius */
  --linear-radius-sm: 4px;
  --linear-radius-md: 8px;
  --linear-radius-lg: 16px;
  --linear-radius-pill: 9999px;
}

.linear-button {
  height: 40px;
  padding: 0 16px;
  border-radius: var(--linear-radius-pill);
  font-family: var(--linear-font-family);
  font-weight: var(--linear-font-weight-medium);
  background: var(--linear-color-brand-500);
  color: #FFFFFF;
  transition: .16s cubic-bezier(0.25,0.46,0.45,0.94);
  transition-property: border, background-color, color, box-shadow, opacity, filter, transform;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `{colors.primary}` | `#7070FF` |
| Brand dark | `{colors.primary-dark}` | `#5E6AD2` |
| Background dark | `{colors.surface-dark}` | `#08090A` |
| Panel dark | `{colors.surface-panel}` | `#0F1011` |
| Background light | `{colors.surface-light}` | `#FFFFFF` |
| Text dark primary | `{colors.text-dark-primary}` | `#F7F8F8` |
| Text light primary | `{colors.text-light-primary}` | `#282A30` |
| Text muted light | `{colors.text-muted-light}` | `#6F6E77` |
| Border light | `{colors.border-light}` | `#E9E8EA` |
| Border dark | `{colors.border-dark}` | `#23252A` |
| Success | `--color-green` | `#27A644` |
| Error | `--color-red` | `#EB5757` |

### Example Component Prompts

#### Hero Section
```text
Linear 스타일 히어로 섹션을 만들어줘.
- 배경: #08090A, 보조 패널 #0F1011
- H1: Inter Variable, desktop fluid display / mobile 38px, weight 680, tight optical spacing
- 텍스트 reveal: opacity 0 + blur(10px) + translateY(20%)에서 짧게 등장
- CTA: #7070FF 또는 #5E6AD2, white text, pill radius 9999px, weight 510
- 구조: 12-column shell, max-width calc(1344px + outer padding * 2), 제품 UI 패널을 증거처럼 배치
```

#### Card Component
```text
Linear 스타일 카드 컴포넌트를 만들어줘.
- 배경: dark면 #0F1011, light면 #FFFFFF/#F8F8F8
- border: 1px solid #23252A 또는 #E9E8EA
- radius: 6px-8px
- shadow는 거의 쓰지 말고 inset ring/hairline으로 구조를 만든다
- hover 시 arrow/icon만 translateY(-1px), 배경은 미세하게만 바꾼다
- 제목: Inter Variable, weight 590 또는 680
- 본문: 16px, weight 400, muted color #6F6E77 또는 #8A8F98
```

#### Badge
```text
Linear 스타일 배지를 만들어줘.
- height 24px-26px, border-radius 9999px
- font-size 12px, font-weight 510
- border 1px solid #E9E8EA 또는 #23252A
- color는 #6F6E77 계열, 브랜드 강조가 필요할 때만 #7070FF 사용
```

#### Navigation
```text
Linear 스타일 상단 네비게이션을 만들어줘.
- height 72px
- backdrop-filter blur(20px)
- bg rgba(255,255,255,0.8) 또는 dark translucent surface
- 하단 border는 rgba(0,0,0,0.08) 같은 hairline
- 링크는 13px-14px Inter Variable, 기본 muted, active만 primary text
- CTA는 우측 pill button, weight 510
```

### Iteration Guide

- **색상 변경 시**: violet을 넓은 gradient로 확장하지 말고 CTA/link/status에만 둔다.
- **폰트 변경 시**: 510/590/680 weight ladder를 유지한다.
- **여백 조정 시**: section-level air와 product-panel density를 분리한다.
- **새 컴포넌트 추가 시**: shadow보다 hairline/inset ring을 먼저 사용한다.
- **다크 모드**: #08090A와 #0F1011을 구분한다. 둘을 하나의 black으로 합치면 Linear 느낌이 무너진다.
- **반응형**: 640/768/1024/1280 breakpoints를 우선 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `Inter Variable` with `400/510/590/680` weights.
- Use #7070FF or #5E6AD2 as action color, not as ambient decoration.
- Build depth with 1px hairlines, inset rings, and precise neutral contrast.
- Keep product UI fragments dense: 40px rows, 12px labels, compact pills.
- Use `Berkeley Mono` only for tooling/code accents.
- Give major sections large breathing room, then compress internal product panels.
- Preserve header glass: 72px height, 20px blur, translucent background.
- Use short, utilitarian transitions such as `.16s var(--ease-out-quad)`.

### ❌ DON'T

- 배경을 `#000000` 또는 flat black으로 두지 말 것 — 대신 hero/page dark는 `#08090A`, panel은 `#0F1011` 사용.
- 텍스트를 `#FFFFFF`로 과도하게 통일하지 말 것 — dark primary text는 `#F7F8F8`, light primary text는 `#282A30` 사용.
- light border를 `#DDDDDD`나 generic gray로 두지 말 것 — 대신 `#E9E8EA` 또는 `#D4D4D6` 사용.
- brand hover를 임의 보라 `#7B61FF`로 만들지 말 것 — 대신 `#8989F0` 또는 dark link `#828FFF` 사용.
- CTA 배경을 `#5B5BFF` 같은 새 hex로 만들지 말 것 — CSS에서 확인된 `#7070FF`/`#5E6AD2` 사용.
- body에 `font-weight: 500`을 기본 medium으로 쓰지 말 것 — Linear medium은 `510`이다.
- headline bold를 `font-weight: 700`으로 반올림하지 말 것 — Linear bold token은 `680`이다.
- 카드에 큰 shadow를 기본 적용하지 말 것 — `--shadow-low/medium/high`는 사실상 none이며 hairline이 구조를 만든다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- **Second brand color: none** — violet is the action lane; other chromatic colors are product/status signals, not co-brand colors.
- **Decorative gradient wash: absent** — gradients are fades/masks/treatments, not colorful hero wallpaper.
- **Heavy elevation: mostly none** — shadows exist in special panels, but default surfaces use border/ring contrast.
- **Round card blobs: none** — cards stay precise; full rounding is reserved for pills/circles.
- **Playful illustration language: absent** — product screenshots, issue rows, and UI panels carry the visual proof.
- **Emoji-led tone: none** — the voice is product-operational, not friendly mascot SaaS.
- **All-purpose 500/600/700 weight ladder: absent** — the variable ladder is calibrated at 510/590/680.
- **Pure monochrome identity: no** — the site is neutral-heavy, but violet action signals are essential.
- **Long theatrical animations: absent** — motion is short, blurred, and functional.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single public marketing capture** — The analysis reused `linear.app` homepage phase1 assets. Authenticated app screens, settings, billing, issue creation, and workspace configuration surfaces were not visited.
- **Screenshot interpretation limited** — `hero-cropped.png` exists and CSS/HTML hero data were read, but no fresh browser replay was performed in this turn.
- **Typography scale incomplete** — `typography.json` reported no full named scale entries. Sizes above are taken from targeted CSS evidence and component rules, not a complete design-token ladder.
- **CSS variable resolution partial** — `resolved_tokens.json` shows 721 total vars, 355 resolved and 366 unresolved. Any variable-only chain that stayed unresolved is treated as unknown rather than guessed.
- **Form validation states not surfaced** — command menu input structure was visible; error/loading/success form states were not observed in the homepage capture.
- **Dark/light mapping is mixed** — Both dark and light tokens are present. Exact per-component theme switching rules were inferred from tokens and CSS context, not from interacting with every theme state.
- **Motion JS not deeply traced** — CSS transitions, keyframes, and inline reveal styles were captured; scroll-trigger orchestration and runtime animation sequencing were not fully replayed.
- **Logo/media color contamination possible** — `brand_candidates.json` marks several frequent chromatic colors as SVG patterns. Brand selection intentionally prioritizes semantic `--color-brand-*` and action usage over raw frequency.
