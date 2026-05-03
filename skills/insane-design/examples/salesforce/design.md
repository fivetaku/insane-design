---
schema_version: 3.2
slug: salesforce
service_name: Salesforce
site_url: https://www.salesforce.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#0176D3"
primary_font: "ITC Avant Garde"
font_weight_normal: 400
token_prefix: sds

bold_direction: Enterprise Cloud
aesthetic_category: Refined SaaS
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv3
design_system_level_evidence: "CSS contains 1450 custom properties, 1363 resolved tokens, SDS/PBC/C360 namespaces, and component-level button/nav variables."

colors:
  brand-primary: "#0176D3"
  brand-deep: "#032D60"
  brand-sky: "#1B96FF"
  surface-cloud: "#EAF5FE"
  surface-base: "#FFFFFF"
  text-primary: "#181818"
  text-muted: "#747474"
  border-muted: "#E5E5E5"
  success-cta: "#2E844A"
typography:
  display: "ITC Avant Garde"
  body: "Salesforce Sans"
  ladder:
    - { token: display-1, size: "80px", weight: 700, line_height: "88px", tracking: "-0.018em" }
    - { token: display-2, size: "56px", weight: 700, line_height: "64px", tracking: "-0.012em" }
    - { token: display-3, size: "48px", weight: 700, line_height: "56px", tracking: "-0.01em" }
    - { token: display-4, size: "40px", weight: 700, line_height: "48px", tracking: "-0.008em" }
    - { token: body-2, size: "16px", weight: 400, line_height: "24px", tracking: "0" }
  weights_used: [400, 500, 600, 700, 750]
  weights_absent: [300, 800, 900]
components:
  button-primary: { bg: "#0176D3", color: "#FFFFFF", radius: "100px", padding: "8px 24px" }
  button-free-trial: { bg: "#2E844A", color: "#FFFFFF", radius: "4px", padding: "12px 24px" }
  nav-fixed: { bg: "#FFFFFF", height: "96px", z_index: 20000 }
  cloud-card: { bg: "#1f3d8f33", border: "1px solid rgba(255,255,255,.18)", radius: "16px" }
---

# DESIGN.md — Salesforce

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Salesforce's public site behaves like an enterprise product stage built inside a cloud-blue control room. The first screen is not a neutral SaaS hero: it opens with a fixed white navigation shelf, a saturated announcement strip, then a deep navy theater where the H1 sits in oversized white type. `#032D60` (`{colors.brand-deep}`) is not black with a blue tint; it is the Salesforce night sky, a command-center wall where every product card becomes an illuminated console.

The visual metaphor is "trusted cloud command center," but the craft is warmer than a dashboard. The cloud logo makes the room feel approachable, while the dense nav and mega-menu grammar keep reminding you this is a platform with many doors. The page has no second general brand color: green `#2E844A` (`{colors.success-cta}`) is a cashier's button reserved for conversion, not a decorative accent, and the rest of the interface keeps returning to the blue authority plane.

Salesforce uses blue like a building material. `#0176D3` (`{colors.brand-primary}`) is the clickable circuitry, `#1B96FF` (`{colors.brand-sky}`) is the lit annotation on the dark hero wall, and `#EAF5FE` (`{colors.surface-cloud}`) is the soft service corridor outside the theater. It is closer to an airport control tower than a startup landing page: the view is friendly, but the traffic system is always visible.

Typography is the hinge. Display type uses ITC Avant Garde through `--pbc-g-font-display`, while body text uses Salesforce Sans through `--pbc-g-font-sans`. The H1 feels like a keynote title stamped onto the blue stage, not a scaled paragraph; negative tracking pulls the big rounded letters into one confident CRM billboard. Then the body copy steps down into operational Salesforce Sans, like the manual attached to the promise.

The color system is expansive but disciplined. There are many ramps under `--sds-g-color-palette-*`, but the homepage funnels attention through four main roles: white enterprise shell, deep blue hero ground, vibrant blue interaction, and green conversion CTA. Product/industry colors stay in their lanes; they are catalog tabs inside the Salesforce warehouse, not confetti across the page.

Motion and depth are secondary craft. The CSS exposes C360 motion tokens from 75ms to 600ms and SDS multi-layer shadows, but the homepage screenshot leans more on hierarchy than spectacle. Shadow does not become the brand; card borders and blue-on-blue surfaces do the work, so the hero reads like a row of product consoles glowing inside the same control room rather than floating glass panels.

### Key Characteristics

- Fixed white navigation bar with high z-index and compact enterprise link density.
- Deep hero surface `#032D60` with oversized white display typography.
- Interaction blue `#0176D3` anchors links, focus rings, and primary SDS buttons.
- Green `#2E844A` is reserved for high-intent "Start for free" conversion.
- ITC Avant Garde display face gives the brand a rounded, confident SaaS voice.
- Salesforce Sans body text keeps content operational and readable.
- Product-suite cards use dark translucent blue panels with 16px rounding.
- Spacing is generous in hero copy but denser in navigation/menu ecosystems.
- Token namespaces are explicit: `--sds-*`, `--pbc-*`, `--c360-*`, and `--hgf-*`.
- Shadows are multi-layer and scoped; the hero screenshot relies more on color planes than elevation.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Enterprise Cloud
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **deep-blue AI command-center hero with cloud product cards**으로 기억된다.
> **Code Complexity**: high — SDS/PBC/C360 token layers, responsive menu states, motion tokens, and multi-namespace component variables require careful mapping.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Salesforce처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Salesforce Sans", system-ui, -apple-system, sans-serif;
  font-weight: 400;
}
h1, h2, .display {
  font-family: "ITC Avant Garde", "Salesforce Sans", system-ui, sans-serif;
  font-weight: 700;
  letter-spacing: -0.012em;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #181818; --hero: #032D60; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #0176D3; --cloud: #EAF5FE; --conversion: #2E844A; }
```

**절대 하지 말아야 할 것 하나**: Salesforce를 일반적인 하얀 B2B 랜딩으로 만들지 말 것. 첫 인상은 `#032D60`의 깊은 cloud-blue hero와 oversized Avant Garde display가 만들어야 한다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.salesforce.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | phase1 reuse: existing HTML/CSS/screenshots + token JSON |
| HTML size | 555306 bytes |
| CSS files | 9 CSS files including `_inline.css`, total 827638 chars |
| Token prefix | `sds` plus `pbc`, `c360`, `hgf` |
| Method | Existing phase1 JSON + CSS token summaries + screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Salesforce marketing stack with generated blade data and C360 navigation (`wpdata`, `c360-nav`, `pbc` component CSS).
- **Design system**: Salesforce Design System / PBC / C360 hybrid — prefixes `--sds-*`, `--pbc-*`, `--c360-*`, `--hgf-*`.
- **CSS architecture**:
  ```text
  sds core      (--sds-g-color-*, --sds-g-spacing-*, --sds-g-radius-*) raw/global tokens
  pbc pattern   (--pbc-g-text-*, --pbc-g-font-*, --pbc-g-blue-*) page building blocks
  c360 nav      (--c360-nav-*, --c360-g-*) navigation and motion layer
  hgf brand     (--hgf-g-*) brand family and themed button backgrounds
  sds component (--sds-c-button-*) component-level state API
  ```
- **Class naming**: BEM-like enterprise classes such as `.c360-nav__nav-items`, `.c360-panel-linkedlist__hero-headline`, `.hgf-button`.
- **Default theme**: mixed. Navigation and most page surfaces use `#FFFFFF`; the signature hero uses `#032D60`.
- **Font loading**: custom brand fonts referenced through CSS variables; `ITC Avant Garde` for display and `Salesforce Sans` for body.
- **Canonical anchor**: the homepage hero at `screenshots/hero-cropped.png`, showing nav, announcement bar, and Agentic Enterprise card group.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `ITC Avant Garde` (brand/commercial display face)
- **Body font**: `Salesforce Sans` (brand sans)
- **Code font**: `monospace` / system fallback in extracted CSS
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --pbc-g-font-display: "ITC Avant Garde", system-ui, -apple-system, sans-serif;
  --pbc-g-font-sans: "Salesforce Sans", system-ui, -apple-system, sans-serif;
  --sds-g-font-family-sans: var(--pbc-g-font-sans);
  --sds-g-font-weight-bold: bold;
}
body {
  font-family: var(--pbc-g-font-sans);
  font-weight: 400;
}
h1, h2 {
  font-family: var(--pbc-g-font-display);
  font-weight: 700;
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **ITC Avant Garde** is the display personality. If unavailable, use **Montserrat** or **Avenir Next** at weight 700, then tighten display tracking by roughly `-0.012em` to `-0.018em`. Do not use plain Inter for the H1; it loses Salesforce's rounded geometric confidence.
- **Salesforce Sans** can fall back to **Inter** or system-ui for body text. Keep body at 400 and line-height near `1.5`; the substitute should not inherit the headline's tight tracking.
- If building in a Korean environment, keep Korean copy on system sans/Pretendard but preserve the same hierarchy: display blocks heavy and tight, body blocks regular and open.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `--pbc-g-text-display-1` | `80px` | 700 | `88px` | `-0.018em` |
| `--pbc-g-text-display-2` | `56px` | 700 | `64px` | `-0.012em` |
| `--pbc-g-text-display-3` | `48px` | 700 | `56px` | `-0.01em` |
| `--pbc-g-text-display-4` | `40px` | 700 | `48px` | `-0.008em` |
| `--pbc-g-text-display-5` | `32px` | 700 | `40px` | `-0.004em` |
| `--pbc-g-text-display-6` | `24px` | 700 | `32px` | `-0.004em` |
| `--pbc-g-text-body-1` | `20px` | 400 | `30px` / `1.5` | `0` |
| `--pbc-g-text-body-2` | `16px` | 400 | `24px` | `0` |
| `--pbc-g-text-body-3` | `14px` | 400 | `20px` | `0` |
| `--pbc-g-text-body-4` | `12px` | 400 | `18px` | `0` |

> ⚠️ Key insight: Salesforce separates display and body families. The hero is not just big Salesforce Sans; it is a display-font, high-weight, negative-tracking statement.

### Principles
<!-- SOURCE: manual -->

1. Display copy is geometrically heavy: the 80/56/48/40px ladder uses high weight and negative tracking so large words stay compact.
2. Body copy returns to Salesforce Sans at 400 with roughly `1.5` line-height, making dense enterprise copy readable.
3. Weight 700 is dominant in headings and buttons; 500/600 appear as support weights, not the primary voice.
4. Display letter-spacing is always tightened. Body copy should keep normal tracking to avoid making paragraphs feel compressed.
5. The hero subhead uses bright blue on dark blue, creating a second typographic tier without changing the font family.
6. Use 14/16/20px body sizes for operational content. Do not invent a 15px body scale.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (8 steps)
<!-- `--sds-g-color-brand-*` / `--pbc-g-blue-*` -->

| Token | Hex |
|---|---|
| `--sds-g-color-brand-inverse-1` | `#001639` |
| `--sds-g-color-brand-inverse-2` | `#032D60` |
| `--sds-g-color-brand-inverse-3` | `#014486` |
| `--sds-g-color-brand-inverse-4` | `#0B5CAB` |
| `--sds-g-color-brand-base-contrast-1` | `#1B96FF` |
| `--sds-g-color-brand-base-contrast-2` | `#0176D3` |
| `--sds-g-color-brand-base-3` | `#D8E6FE` |
| `--sds-g-color-brand-base-2` | `#EEF4FF` |

### 06-2. Brand Dark Variant
<!-- SOURCE: auto -->

| Token | Hex |
|---|---|
| `--pbc-g-blue-vibrant-20` | `#032D60` |
| `--pbc-g-blue-vibrant-40` | `#0B5CAB` |
| `--pbc-g-blue-vibrant-50` | `#0176D3` |
| `--pbc-g-blue-vibrant-60` | `#0D9DDA` |
| `--hgf-g-cloud-blue-vibrant-10` | `#001A28` |
| `--hgf-g-cloud-blue-vibrant-20` | `#023248` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light / Neutral | Dark / Text |
|---|---|---|
| Surface | `#FFFFFF` | `#181818` |
| Soft surface | `#F3F3F3` | `#242424` |
| Border | `#E5E5E5` | `#444444` |
| Muted text | `#939393` | `#747474` |
| Ink | `#181818` | `#000000` |

### 06-4. Accent Families
<!-- SOURCE: auto -->

| Family | Key step | Hex |
|---|---|---|
| Green / success | `--sds-g-color-palette-green-50` | `#2E844A` |
| Green / light | `--sds-g-color-palette-green-95` | `#EBF7E6` |
| Yellow / event | palette candidate | `#FCC003` |
| Orange / warning | `--sds-g-color-palette-orange-65` | `#F38303` |
| Hot orange | `--sds-g-color-palette-hot-orange-65` | `#FF784F` |
| Purple / product | `--sds-g-color-palette-purple-50` | `#9050E9` |
| Violet / product | `--sds-g-color-palette-violet-50` | `#BA01FF` |
| Teal / product | `--sds-g-color-palette-teal-50` | `#0B827C` |

### 06-5. Semantic
<!-- SOURCE: auto+manual -->

| Token | Hex | Usage |
|---|---|---|
| `--sds-c-button-color-background` | `#0176D3` | Primary SDS button background |
| `--sds-c-button-color-background-hover` | `#0B5CAB` | Primary hover / active blue |
| `--sds-c-button-text-color` | `#FFFFFF` | Text on filled blue buttons |
| `--pbc-g-text-body-color` | `#181818` or `#FFFFFF` by theme | Body copy |
| `--pbc-g-text-link-color` | `#0176D3` | Link color on light surfaces |
| `--pbc-g-text-display-color` | `#032D60` or `#FFFFFF` by section | Heading color |
| `--pbc-g-text-error` | red palette token | Error text |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--sds-c-button-color-background-hover` | `#0B5CAB` | Filled button hover |
| `--sds-c-button-color-border-focus` | `#0176D3` | Button focus ring / border |
| `--sds-c-button-color-background-disabled` | `#A0A0A0` | Disabled filled button |
| `--pbc-g-text-link-color` | `#0176D3` | Inline links |
| `--pbc-g-blue-vibrant-95` | `#EAF5FE` | Light blue panel surfaces |
| `--hgf-g-cloud-blue-vibrant-95` | `#EAF5FE` | Global promo/cloud surface |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---|---|
| neutral surface | `#FFFFFF` | 90 + 15 shorthand/full occurrences |
| deep blue | `#032D60` | 46 |
| primary blue | `#0176D3` | 37 |
| cloud surface | `#EAF5FE` | 35 |
| border neutral | `#E5E5E5` | 19 |
| hover blue | `#0B5CAB` | 16 |
| text ink | `#181818` | 15 |
| sky blue | `#1B96FF` | 14 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.brand-primary}` (`#0176D3`)** — the active Salesforce blue. It belongs on primary buttons, active nav states, link accents, and focus rings. Use it as the interface action color, not as a full-page wash.

**`{colors.brand-deep}` (`#032D60`)** — the authority plane. It carries the Agentic Enterprise hero and dark display surfaces, replacing generic black with a Salesforce-specific blue-black.

**`{colors.surface-base}` (`#FFFFFF`)** — the enterprise shell. Navigation, menus, and most content surfaces start here so the deep hero and blue controls read as deliberate contrast.

**`{colors.surface-cloud}` (`#EAF5FE`)** — the light cloud tint. Use it for informational panels, mobile menu messages, and hover/soft emphasis when white would feel too plain.

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| `--sds-g-spacing-1` | `4px` | micro gap |
| `--sds-g-spacing-2` | `8px` | button vertical rhythm |
| `--sds-g-spacing-3` | `12px` | compact inline padding |
| `--sds-g-spacing-4` | `16px` | card interior / mobile gutters |
| `--sds-g-spacing-5` | `24px` | button horizontal padding / nav spacing |
| `--sds-g-spacing-6` | `32px` | standard section/card gap |
| `--sds-g-spacing-7` | `40px` | large card padding |
| `--sds-g-spacing-8` | `48px` | editorial block padding |
| `--sds-g-spacing-9` | `56px` | large vertical rhythm |
| `--sds-g-spacing-10` | `64px` | hero/section vertical air |
| `--sds-g-spacing-11` | `72px` | large section air |
| `--sds-g-spacing-12` | `80px` | maximum standard vertical air |

**주요 alias**:
- `--sds-c-button-spacing-inline` → `24px` (primary button horizontal padding)
- `--sds-c-button-spacing-block` → `8px` (button vertical padding)
- `--c360-nav-c-header-height` → `56px` (mobile/header menu shell)

### Whitespace Philosophy
<!-- SOURCE: manual -->

Salesforce uses two spacing speeds. The hero breathes like a keynote slide: large display copy sits with generous vertical room, and the card row begins only after the message has landed. The navigation and menu system move at the opposite speed: dense link clusters, compact button spacing, and fixed header mechanics make the site feel like a product catalog.

Do not flatten this into a generic 32px-everywhere rhythm. The Salesforce pattern is "wide hero, dense enterprise chrome": 64/80px vertical air for narrative bands, 24/32px gaps for product groups, and 8/24px button padding for action controls.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--sds-g-radius-border-1` | `2px` | hairline controls / small focus surfaces |
| `--sds-g-radius-border-2` | `4px` | default SDS button radius |
| `--sds-g-radius-border-3` | `8px` | small cards / menus |
| `--sds-g-radius-border-4` | `16px` | large cards and cloud panels |
| `--sds-g-radius-border-circle` | `100%` | icon circles |
| explicit pill | `100px` / `1000px` | nav pills, rounded controls |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| `--sds-g-shadow-1` | `0 0 2px 0 #18181814, 0 2px 4px 1px #18181828` | subtle component lift |
| `--sds-g-shadow-2` | `0 2px 8px -2px #18181814, 0 8px 12px -2px #18181828` | card and menu elevation |
| `--sds-g-shadow-3` | `0 12px 24px -4px #18181814, 0 16px 32px -4px #18181828` | larger overlays |
| `--sds-g-shadow-4` | `0 24px 48px -4px #18181833` | high elevation |
| custom panel | `0px 24px 48px -4px rgba(24, 24, 24, 0.2)` | promo/card depth |

Shadow pattern: multi-layer neutral shadows, not colored glow. On the screenshoted hero, depth mostly comes from contrast and bordered card panels rather than visible drop shadows.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `--c360-g-kx-duration-x-short-init` | `75ms` | quick state changes |
| `--c360-g-kx-duration-short-init` | `150ms` | hover / menu micro transitions |
| `--c360-g-kx-duration-normal-init` | `250ms` | nav panel movement |
| `--c360-g-kx-duration-long-init` | `400ms` | larger reveal |
| `--c360-g-kx-duration-x-long-init` | `600ms` | extended transitions |
| `--c360-g-kx-ease-out-init` | `cubic-bezier(0, 0.3, 0.15, 1)` | Salesforce easing-out motion |
| `--c360-g-kx-ease-over-init` | `cubic-bezier(0.3, 1.75, 0.3, 1)` | overshoot motion where enabled |

The CSS includes a `prefers-reduced-motion` branch, so motion should be treated as an enhancement layer. Use color, typography, and layout to carry the identity before adding movement.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: common caps include `1280px`, with generated responsive caps around `1398px`, `1439px`, and `1814px`.
- **Grid type**: CSS Grid and Flexbox mix; hero cards appear as a 4-column row on desktop.
- **Column count**: 4-card product suite in the screenshot; menu panels use multi-column link lists.
- **Gutter**: `24px`, `32px`, and `40px` are the dominant gaps.

### Hero
- **Pattern Summary**: fixed nav + announcement bar + deep-blue hero + centered H1 + supporting copy + 4 product cards.
- Layout: one-column centered narrative followed by horizontal card group.
- Background: `#032D60` deep blue, with `#FFFFFF` text and `#1B96FF`/bright blue emphasis.
- **Background Treatment**: solid deep-blue field; card panels add translucent/bordered depth rather than gradient mesh.
- H1: approximately `80px` desktop display, weight `700`, tight tracking.
- Max-width: headline visually constrained near the center; body text sits narrower than the full card row.

### Section Rhythm
```css
section {
  padding: 64px 32px;
  max-width: 1280px;
}
```

Use this as a reconstruction baseline, then tighten or expand based on component density. Menu panels and cards use smaller interior padding than narrative hero bands.

### Card Patterns
- **Card background**: deep blue translucent or related blue panel on dark hero; white/soft-blue panels elsewhere.
- **Card border**: subtle blue/white alpha border in hero cards; neutral `#E5E5E5` on light cards.
- **Card radius**: `16px` is the large-card signature.
- **Card padding**: `32px 32px 40px` and `40px` recur.
- **Card shadow**: minimal in dark hero; SDS shadows available for light overlays.

### Navigation Structure
- **Type**: horizontal top navigation with product mega-menu behavior.
- **Position**: fixed.
- **Height**: screenshot shell is about 96px including top nav; mobile/internal header token `--c360-nav-c-header-height` is `56px`.
- **Background**: `#FFFFFF`.
- **Border**: no heavy visible border; separation is mostly whitespace and fixed placement.

### Content Width
- **Prose max-width**: hero paragraph visually around 760-820px.
- **Container max-width**: `1280px` practical reconstruction anchor.
- **Sidebar width**: not present on homepage hero; mega-menu panels replace sidebars.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `max-width: 767px` | mobile nav panels and single-column content |
| Tablet | `min-width: 768px` / `max-width: 1023px` | intermediate card/menu layout |
| Desktop | `min-width: 1024px` | full horizontal navigation and multi-column hero cards |
| Large | `min-width: 1440px` | wide layout caps and expanded spacing |

### Touch Targets
- **Minimum tap size**: treat as `44px+`; extracted button/nav shell uses `56px` header and padded controls.
- **Button height (mobile)**: reconstruct at `44-48px` minimum.
- **Input height (mobile)**: not observed on homepage hero; use SDS default with 44px minimum.

### Collapsing Strategy
- **Navigation**: fixed desktop nav collapses into C360 mobile overlay/panel navigation.
- **Grid columns**: 4 hero cards should collapse to 2 columns on tablet and 1 column on mobile.
- **Sidebar**: no persistent sidebar in the analyzed homepage.
- **Hero layout**: centered copy remains first; card row stacks underneath.

### Image Behavior
- **Strategy**: homepage hero screenshot is mostly text/card UI, not photo-led.
- **Max-width**: use `max-width: 100%` for any media.
- **Aspect ratio handling**: card icons are circular/square; product images in other sections should preserve intrinsic ratio.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary SDS button**

```html
<a class="sfdc-button sfdc-button--primary" href="#">Start for free</a>
```

| Property | Value |
|---|---|
| Background | `#0176D3` |
| Hover / active | `#0B5CAB` |
| Text | `#FFFFFF` |
| Radius | `4px` SDS default, `100px` pill in nav/menu contexts |
| Padding | `8px 24px` baseline; nav CTA screenshot uses larger vertical feel |
| Focus | blue focus ring / border using `#0176D3` |

**Conversion green button**

```html
<a class="sfdc-button sfdc-button--trial" href="#">Start for free</a>
```

| Property | Value |
|---|---|
| Background | `#2E844A` |
| Text | `#FFFFFF` |
| Radius | `4px` |
| Padding | `12px 24px` |
| Usage | top-right high-intent CTA only |

### Badges

Salesforce uses announcement bars and label-like links more than decorative badge clouds.

```html
<div class="sfdc-announcement">Get started with the #1 AI CRM for small business.</div>
```

| Property | Value |
|---|---|
| Background | `#1B96FF` or related bright blue |
| Text | `#FFFFFF` |
| Link | underlined white |
| Height | compact band above hero |

### Cards & Containers

```html
<article class="sfdc-cloud-card">
  <div class="sfdc-cloud-card__icon"></div>
  <h3>Agentforce</h3>
  <p>Delivers always-on agents for customers and employees.</p>
</article>
```

| Property | Value |
|---|---|
| Background | dark blue panel over `#032D60` |
| Border | subtle alpha stroke, visually blue-white |
| Radius | `16px` |
| Padding | `32px 32px 40px` |
| Shadow | none or very subtle; rely on border/contrast in hero |
| Hover | use border-color/brightness shift, not large lift |

### Navigation

```html
<header class="c360-nav" role="banner">
  <nav class="container-nav c360-nav__nav-items" aria-label="Salesforce Main Menu"></nav>
</header>
```

| Property | Value |
|---|---|
| Position | `fixed` |
| Background | `#FFFFFF` |
| Z-index | `20000` |
| Link color | `#032D60` |
| Active color | `#0176D3` |
| Logo area | compact cloud mark on left |
| Utility links | contact, globe, login, green CTA on right |

### Inputs & Forms

Full form states were not present in the hero screenshot. Reconstruct from SDS button/control grammar:

| State | Rule |
|---|---|
| Default | white surface, neutral border `#E5E5E5`, text `#181818` |
| Focus | `#0176D3` ring/border |
| Error | use SDS red palette; do not invent a custom red |
| Disabled | neutral `#A0A0A0` equivalent from SDS disabled button token |
| Placeholder | muted neutral `#747474` / `#939393` |

### Hero Section

```html
<section class="sfdc-hero sfdc-hero--agentic">
  <p>Salesforce. The #1 AI CRM. <a>Start for free.</a></p>
  <h1>Welcome to the Agentic Enterprise.</h1>
  <h2>Where humans and agents drive customer success together.</h2>
  <p>Salesforce brings together Slack, Agentforce, Customer 360, and Data 360...</p>
</section>
```

| Property | Value |
|---|---|
| Background | `#032D60` |
| H1 | ITC Avant Garde, about `80px`, `700`, white |
| Subhead | bright blue, about `24px`, `700` |
| Body | white, about `20px`, regular |
| Layout | centered text plus 4-card product row |
| CTA placement | inline link above H1 plus nav CTA |

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-primary-blue** — SDS filled action button.

| Property | Value |
|---|---|
| bg | `#0176D3` |
| hover | `#0B5CAB` |
| text | `#FFFFFF` |
| radius | `4px` or tokenized SDS radius |

**button-trial-green** — high-intent commercial CTA.

| Property | Value |
|---|---|
| bg | `#2E844A` |
| text | `#FFFFFF` |
| radius | `4px` |
| usage | top nav and conversion moments, not general links |

**button-nav-link** — low-chrome navigation action.

| Property | Value |
|---|---|
| bg | transparent |
| text | `#032D60` |
| active | `#0176D3` |
| padding | compact horizontal spacing |

**cloud-product-card** — hero suite card.

| Property | Value |
|---|---|
| bg | deep blue panel on `#032D60` |
| border | subtle blue-white alpha |
| radius | `16px` |
| icon | white line glyph or brand product mark |

### Signature Micro-Specs
<!-- SOURCE: manual -->
<!-- §13-3 -->

```yaml
deep-blue-command-hero:
  description: "A saturated enterprise hero field that replaces generic black with Salesforce blue authority."
  technique: "background: #032D60 /* {colors.brand-deep} */; color: #FFFFFF; support accent #1B96FF /* {colors.brand-sky} */; cards remain in the same blue family."
  applied_to: ["{component.Hero Section}", "{component.cloud-product-card}"]
  visual_signature: "The AI message feels like a cloud command center, not a generic dark SaaS hero."

cloud-console-card-stroke:
  description: "Hero cards sit as blue-on-blue product consoles instead of lifted white cards."
  technique: "background: rgba(27,150,255,0.12); border: 1px solid rgba(255,255,255,0.18); border-radius: 16px; padding: 32px 32px 40px; shadow minimized."
  applied_to: ["{component.cloud-product-card}", "{component.Hero Section}"]
  visual_signature: "Cards read as illuminated panels embedded in the same dark Salesforce cloud surface."

dual-font-trust-ladder:
  description: "Display and body typography are split by role, not merely size."
  technique: "ITC Avant Garde via --pbc-g-font-display at 700 with -0.018em to -0.008em tracking; Salesforce Sans via --pbc-g-font-sans at 400 with 1.5 line-height."
  applied_to: ["{component.Hero Section}", "{component.Navigation}", "{component.Cards & Containers}"]
  visual_signature: "Promotional language lands as a rounded keynote billboard while CRM detail remains readable and operational."

sds-stateful-button-api:
  description: "Buttons expose component-level state variables rather than one-off CSS classes."
  technique: "--sds-c-button-color-background: #0176D3; --sds-c-button-color-background-hover: #0B5CAB; --sds-c-button-color-border-focus: #0176D3; disabled aliases use neutral gray."
  applied_to: ["{component.button-primary-blue}", "{component.button-trial-green}", "{component.Navigation}"]
  visual_signature: "Interaction states stay consistent across a large enterprise marketing ecosystem."

fixed-enterprise-nav-shell:
  description: "The page begins with a persistent product-navigation control surface."
  technique: ".c360-nav { position: fixed; top: 0; width: 100%; background-color: #FFFFFF; z-index: 20000; } with dense product, utility, login, and CTA zones."
  applied_to: ["{component.Navigation}", "{component.Badges}"]
  visual_signature: "Salesforce feels like a platform with many doors before it feels like a single landing page."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Large, declarative, category-owning | "Welcome to the Agentic Enterprise." |
| Primary CTA | Direct commercial action | "Start for free" |
| Secondary CTA | Contact/demo utility | "Contact Us" |
| Subheading | Human + AI collaboration promise | "Where humans and agents drive customer success together." |
| Tone | Confident enterprise optimism; AI framed as trusted productivity, not novelty | "CRM + AI + Data + Trust" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Salesforce — copy into your root stylesheet */
:root {
  /* Fonts */
  --sf-font-display: "ITC Avant Garde", "Salesforce Sans", system-ui, sans-serif;
  --sf-font-body: "Salesforce Sans", system-ui, -apple-system, sans-serif;
  --sf-font-weight-normal: 400;
  --sf-font-weight-bold: 700;

  /* Brand */
  --sf-color-brand-900: #001639;
  --sf-color-brand-800: #032D60;
  --sf-color-brand-700: #014486;
  --sf-color-brand-600: #0B5CAB;
  --sf-color-brand-500: #0176D3;
  --sf-color-brand-400: #1B96FF;
  --sf-color-brand-100: #EAF5FE;

  /* Surfaces */
  --sf-bg-page: #FFFFFF;
  --sf-bg-hero: #032D60;
  --sf-bg-cloud: #EAF5FE;
  --sf-text: #181818;
  --sf-text-muted: #747474;
  --sf-border: #E5E5E5;
  --sf-conversion: #2E844A;

  /* Spacing */
  --sf-space-xs: 4px;
  --sf-space-sm: 8px;
  --sf-space-md: 16px;
  --sf-space-lg: 24px;
  --sf-space-xl: 32px;
  --sf-space-2xl: 64px;

  /* Radius */
  --sf-radius-sm: 4px;
  --sf-radius-md: 8px;
  --sf-radius-lg: 16px;
  --sf-radius-pill: 100px;
}

body {
  margin: 0;
  background: var(--sf-bg-page);
  color: var(--sf-text);
  font-family: var(--sf-font-body);
  font-weight: var(--sf-font-weight-normal);
  line-height: 1.5;
}

.sf-hero {
  background: var(--sf-bg-hero);
  color: #FFFFFF;
  text-align: center;
  padding: 64px 32px 80px;
}

.sf-hero h1 {
  font-family: var(--sf-font-display);
  font-size: clamp(48px, 6.25vw, 80px);
  line-height: 1.1;
  letter-spacing: -0.012em;
  font-weight: 700;
  margin: 0 auto 32px;
  max-width: 980px;
}

.sf-button-primary {
  background: var(--sf-color-brand-500);
  color: #FFFFFF;
  border: 1px solid var(--sf-color-brand-500);
  border-radius: var(--sf-radius-sm);
  padding: 8px 24px;
  font-weight: 700;
}

.sf-button-primary:hover {
  background: var(--sf-color-brand-600);
  border-color: var(--sf-color-brand-600);
}

.sf-button-trial {
  background: var(--sf-conversion);
  color: #FFFFFF;
  border-radius: var(--sf-radius-sm);
  padding: 12px 24px;
  font-weight: 700;
}

.sf-cloud-card {
  background: rgba(27, 150, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: var(--sf-radius-lg);
  padding: 32px 32px 40px;
  color: #FFFFFF;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Salesforce-inspired reconstruction
module.exports = {
  theme: {
    extend: {
      colors: {
        salesforce: {
          100: '#EAF5FE',
          400: '#1B96FF',
          500: '#0176D3',
          600: '#0B5CAB',
          700: '#014486',
          800: '#032D60',
          900: '#001639',
        },
        neutral: {
          50: '#FFFFFF',
          100: '#F3F3F3',
          200: '#E5E5E5',
          500: '#747474',
          900: '#181818',
        },
        conversion: '#2E844A',
      },
      fontFamily: {
        display: ['ITC Avant Garde', 'Montserrat', 'system-ui', 'sans-serif'],
        sans: ['Salesforce Sans', 'Inter', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        sf: '4px',
        'sf-card': '16px',
        'sf-pill': '100px',
      },
      boxShadow: {
        sf1: '0 0 2px 0 #18181814, 0 2px 4px 1px #18181828',
        sf2: '0 2px 8px -2px #18181814, 0 8px 12px -2px #18181828',
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
| Brand primary | `{colors.brand-primary}` | `#0176D3` |
| Hero background | `{colors.brand-deep}` | `#032D60` |
| Bright accent | `{colors.brand-sky}` | `#1B96FF` |
| Background | `{colors.surface-base}` | `#FFFFFF` |
| Cloud surface | `{colors.surface-cloud}` | `#EAF5FE` |
| Text primary | `{colors.text-primary}` | `#181818` |
| Text muted | `{colors.text-muted}` | `#747474` |
| Border | `{colors.border-muted}` | `#E5E5E5` |
| Conversion CTA | `{colors.success-cta}` | `#2E844A` |

### Example Component Prompts

#### Hero Section
```text
Salesforce 스타일 히어로 섹션을 만들어줘.
- 배경: #032D60
- H1: ITC Avant Garde, clamp(48px, 6.25vw, 80px), weight 700, tracking -0.012em, color #FFFFFF
- 서브헤드: #1B96FF, 24px, weight 700
- 본문: #FFFFFF, 20px, Salesforce Sans, line-height 1.5
- 카드: 4-column desktop, bg rgba(27,150,255,.12), border rgba(255,255,255,.18), radius 16px
- CTA: primary #0176D3 or conversion #2E844A, radius 4px
```

#### Card Component
```text
Salesforce cloud product card를 만들어줘.
- 배경: #032D60 위의 translucent blue panel
- border: 1px solid rgba(255,255,255,.18)
- radius: 16px
- padding: 32px 32px 40px
- icon: white line icon in 32px square
- 제목: ITC Avant Garde or Salesforce Sans, 24px, weight 700, color #FFFFFF
- 본문: 16px, color #FFFFFF, line-height 24px
- hover: large transform 대신 border/brightness만 살짝 변경
```

#### Badge / Announcement
```text
Salesforce announcement bar를 만들어줘.
- 배경: #1B96FF
- 텍스트: #FFFFFF, 16px, weight 700
- 링크: white underline
- 높이: compact horizontal band
- nav 아래, hero 위에 배치
```

#### Navigation
```text
Salesforce top navigation을 만들어줘.
- position: fixed; top: 0; z-index: 20000
- 배경: #FFFFFF
- 로고: 좌측 cloud mark
- 링크: #032D60, 16px, weight 600
- active/focus: #0176D3
- 우측: Contact Us, globe icon, Login, #2E844A Start for free button
- 데스크톱은 horizontal, 모바일은 full-height overlay panel로 접기
```

### Iteration Guide

- **색상 변경 시**: blue ramp를 유지한다. `#0176D3`는 action, `#032D60`은 hero/authority, `#EAF5FE`는 soft cloud surface다.
- **폰트 변경 시**: display/body 분리를 유지한다. H1을 body font 하나로 처리하면 Salesforce 느낌이 약해진다.
- **버튼 추가 시**: blue primary와 green conversion의 역할을 분리한다. 모든 버튼을 초록으로 만들지 않는다.
- **카드 추가 시**: 16px radius와 disciplined border를 사용한다. 과한 shadow/gradient로 depth를 만들지 않는다.
- **반응형 작업 시**: 767/768/1024/1440px breakpoint 체계를 따른다.
- **AI 테마 적용 시**: 어두운 hero는 black이 아니라 `#032D60`이어야 한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#032D60` as the signature hero/authority background when recreating the homepage impression.
- Use `#0176D3` for primary blue actions, active links, and focus states.
- Keep `#2E844A` reserved for conversion CTA moments such as "Start for free."
- Pair ITC Avant Garde-style display headings with Salesforce Sans-style body text.
- Preserve the fixed white navigation shell and dense enterprise menu behavior.
- Use 16px radius for product cards and 4px/SDS radius for most buttons.
- Use SDS-style multi-layer shadows only for overlays/cards that need elevation.
- Keep dark hero cards within the same blue family instead of making them generic gray cards.

### ❌ DON'T

- 배경 hero를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#032D60` 사용.
- 기본 page surface를 `#F8FAFC` 같은 generic cool gray로 두지 말 것 — 대신 `#FFFFFF` 사용.
- primary action을 `#2563EB` 또는 `#0066FF`로 대체하지 말 것 — 대신 `#0176D3` 사용.
- hero highlight를 `#60A5FA`로 임의 보정하지 말 것 — 대신 실제 bright blue `#1B96FF` 사용.
- soft info panel을 `#EFF6FF`로 일반화하지 말 것 — 대신 `#EAF5FE` 사용.
- body text를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#181818` 사용.
- muted text를 `#6B7280`로 Tailwind화하지 말 것 — 대신 `#747474` 또는 `#939393` 사용.
- conversion CTA를 brand blue로만 통일하지 말 것 — Salesforce는 `#2E844A` green CTA를 별도 역할로 쓴다.
- H1을 Inter 800으로 처리하지 말 것 — ITC Avant Garde 계열 700 + negative tracking이 핵심이다.
- hero card에 24px+ radius와 glass blur를 과하게 넣지 말 것 — 실제 패턴은 16px card with subtle stroke다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- **Generic black hero: absent** — Salesforce dark surfaces are blue-black (`#032D60`), not `#000000`.
- **Purple AI gradient: none** — AI messaging is carried by cloud blue hierarchy, not a violet mesh background.
- **Second general brand color: none** — green exists for conversion/success, but the interface brand is still blue.
- **Monochrome startup minimalism: never** — the site is dense with platform navigation, product cards, and enterprise affordances.
- **Body font as display: absent** — display and body are deliberately separated.
- **Decorative heavy shadows on hero cards: minimal** — dark card separation comes from border and tone, not floating elevation.
- **12px pill-only UI: absent** — Salesforce mixes squared 4px action buttons with pill nav controls; not every control is a capsule.
- **Random product palette use: forbidden** — purple/orange/teal/yellow ramps exist, but they are not global page chrome.
- **Logo-wall color contamination: excluded** — chromatic customer/logo colors should not become brand tokens.
- **One-page startup CTA hierarchy: absent** — navigation, contact, login, product menu, and conversion CTA coexist.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-focused evidence** — the screenshot and extracted HTML/CSS represent the public Salesforce homepage/marketing shell. Product app UI, admin console, and authenticated CRM screens are not covered.
- **Korea-localized content** — the captured HTML contains Korean Salesforce content and event modules. The core token system is global, but copy rhythm and some page modules may vary by locale.
- **Form states not fully observed** — input validation, loading, and error states were inferred from SDS token conventions rather than a visited form flow.
- **Exact hero runtime CSS not fully isolated** — CSS was summarized from 827638 chars across multiple files. Values listed here prioritize recurring tokens and visible screenshot behavior.
- **Animation behavior not executed end-to-end** — C360 motion tokens were extracted, but JS-triggered menu transitions and scroll interactions were not visually profiled.
- **Responsive screenshot coverage limited** — breakpoints are extracted from CSS, but mobile/tablet screenshots were not part of this run.
- **Dark-mode mapping is section-specific** — Salesforce has dark hero surfaces and light shell surfaces; this is not a full site-wide dark theme inventory.
- **Logo and icon treatments are not exhaustively cataloged** — hero card icons were visually observed, but full SVG/icon token mapping was not extracted.
- **Brand font availability may vary** — ITC Avant Garde and Salesforce Sans are brand/commercial assets; substitutes require optical correction.
- **Output path differs from default skill path** — user requested `plugins/insane-design/docs/reports/salesforce/design.md`, so this report was written there instead of `insane-design/salesforce/design.md`.
