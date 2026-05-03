---
schema_version: 3.2
slug: uber
service_name: Uber
site_url: https://uber.com
fetched_at: 2026-04-14T01:14:00+09:00
default_theme: mixed
brand_color: "#000000"
primary_font: UberMove
font_weight_normal: 500
token_prefix: none

bold_direction: Utility Monochrome
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: commerce-marketplace
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "Uber.com exposes a coherent production system through compiled CSS, repeated components, and UberMove typography, but no public custom-property token layer was found."

colors:
  ink: "#000000"
  surface: "#FFFFFF"
  field: "#F3F3F3"
  hairline: "#E8E8E8"
  focus: "#276EF1"
  promotion-mint: "#ADDEC9"
  text-muted: "#5E5E5E"
  text-secondary: "#4B4B4B"
typography:
  display: "UberMove, UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
  body: "UberMoveText, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
  ladder:
    - { token: hero, size: "52px", weight: 700, line_height: "64px", tracking: "0" }
    - { token: h1-mobile, size: "44px", weight: 700, line_height: "52px", tracking: "0" }
    - { token: section-title, size: "36px", weight: 700, line_height: "44px", tracking: "0" }
    - { token: card-title, size: "24px", weight: 700, line_height: "32px", tracking: "0" }
    - { token: body, size: "16px", weight: 500, line_height: "24px", tracking: "0" }
    - { token: nav, size: "14px", weight: 500, line_height: "20px", tracking: "0" }
  weights_used: [200, 400, 500, 600, 700]
  weights_absent: [300, 800, 900]
components:
  button-primary: { bg: "{colors.ink}", color: "{colors.surface}", radius: "8px", padding: "14px 24px" }
  button-secondary-pill: { bg: "{colors.field}", color: "{colors.ink}", radius: "999px", padding: "12px 16px" }
  input-location: { bg: "{colors.field}", color: "{colors.ink}", radius: "8px", height: "56px" }
  promo-pill: { bg: "{colors.promotion-mint}", color: "{colors.ink}", radius: "999px", padding: "14px 22px" }
---

# DESIGN.md — Uber (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Uber.com is not trying to look decorative. It behaves like a dispatch surface that has been widened into a public website: black chrome at the top, white operating floor underneath, gray input machinery, and one decisive black action. The brand color is not a chromatic blue, even though `#276EF1` appears in focus rings. The brand is operational black: `#000000` (`{colors.ink}`) against `#FFFFFF` (`{colors.surface}`).

The hero is a utility split screen. Left side: location, time, pickup, dropoff, price. Right side: an illustration card and a travel prompt. The page does not start with a cinematic city photo or gradient. It starts with the mental model of booking a trip. The site earns personality through product specificity, not decoration.

Typography carries the confidence. `UberMove` gives the H1 a compact, blunt geometry at 52px/64px, while `UberMoveText` handles the service controls at 16px/24px. Letter spacing is deliberately `0`: no luxury tightening, no editorial looseness, no faux-tech tracking. The type sits squarely on the grid.

The system's softness is local. Inputs use `#F3F3F3` fields with 8px corners; promo CTAs use a mint pill `#ADDEC9`; focus uses `#276EF1`. These are not broad brand colors. They are task colors, applied to limited jobs so the black/white structure stays dominant.

If the page were a physical room it would be a 24-hour airport dispatch counter: the black header is the suspended gantry sign, the gray input strip is the routing slip pad bolted to the desk, and the single black "Request now" CTA is the hard pickup-bell at the corner. The illustration card on the right behaves like the wall map of available zones, not like marketing decoration. Even the focus blue acts like the tarmac edge-light around an active gate — a guidance signal, not a paint job. There is no second brand color because dispatch ops are run in monochrome so the call-out colors mean something.

이 사이트는 마켓플레이스 페이지 같지만 실제로는 **dispatch 카운터에 놓인 routing slip pad**다. pickup/dropoff 입력은 매대 위 주문 카드가 아니라 카운터 슬립 한 장이고, 카탈로그 진열대는 비어 있다 — 가능한 trip 한 건만 주문된다. 창고처럼 깊은 검은 nav는 dispatch 천장 사인이고, 회색 input chassis는 카운터에 볼트로 박힌 routing slip pad다. 마켓의 모든 장바구니/진열 동선이 이 한 칸의 카운터 호출로 환원된다 — 시장의 다양한 매대를 줄이고, 단일 카운터만 켜둔 dispatch 마켓이다.

### Key Characteristics

- Black navigation bar with white logo and compact utility links.
- White booking floor: the core task lives on `#FFFFFF`, not on a tinted marketing canvas.
- UberMove display type: heavy, geometric, untracked, and blunt.
- UberMoveText controls: 16px/24px text rhythm with frequent weight 500.
- Form fields are large gray modules (`#F3F3F3`) rather than thin outlined inputs.
- Primary CTA is black rectangle with 8px radius; secondary actions are text links or light pills.
- Focus and accessibility highlight use `#276EF1`, but blue is not the brand surface.
- Promo surface uses pale mint `#EAF6ED` / `#ADDEC9` as a temporary campaign layer.
- Layout alternates dense task controls with high-air content bands.
- Shadows are rare and scoped; structure comes from surfaces, not elevation.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Utility Monochrome
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **black dispatch chrome wrapped around a white booking machine**으로 기억된다.
> **Code Complexity**: high — compiled responsive CSS, repeated component variants, focus rings, and motion/fallback states without a visible custom-property token layer.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Uber처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Font + weight */
body {
  font-family: "UberMoveText", system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 24px;
  font-weight: 500;
  letter-spacing: 0;
}

h1, .display {
  font-family: "UberMove", "UberMoveText", system-ui, sans-serif;
  font-size: 52px;
  line-height: 64px;
  font-weight: 700;
}

/* 2. Background + text */
:root { --bg: #FFFFFF; --fg: #000000; --field: #F3F3F3; }
body { background: var(--bg); color: var(--fg); }

/* 3. Actions */
:root { --brand: #000000; --focus: #276EF1; }
.button-primary { background: var(--brand); color: #FFFFFF; border-radius: 8px; }
.input-location { background: var(--field); border: 0; border-radius: 8px; }
```

**절대 하지 말아야 할 것 하나**: Uber를 “blue tech app”으로 만들지 말 것. `#276EF1`은 focus ring/interactive aid이며, 기본 CTA와 brand surface는 `#000000`이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://uber.com` |
| Fetched | 2026-04-14T01:14:00+09:00 |
| Extractor | reused phase1 artifacts: HTML + inline compiled CSS + screenshot |
| HTML size | 723814 bytes |
| CSS files | 0 external + 1 inline, 115629 chars |
| Token prefix | `none` |
| Method | compiled CSS frequency + typography extraction + screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: SSR/compiled web app; exact framework not asserted from current artifacts.
- **Design system**: Uber production design language surfaced as compiled CSS; no custom-property token layer found.
- **CSS architecture**: generated classnames with repeated atomic/declaration blocks.
  ```text
  no-var-layer          0 custom properties in extracted CSS
  compiled-utility      repeated display/flex/grid/padding/font declarations
  component-pattern     buttons, inputs, nav, promo modules inferred from repeated styles
  ```
- **Class naming**: generated `css-*` classes rather than semantic BEM.
- **Default theme**: mixed. Header is black; primary page surface is white.
- **Font loading**: UberMove / UberMoveText face names referenced in CSS; system Helvetica fallback chain present.
- **Canonical anchor**: hero booking form on Korea-localized Uber homepage: "Uber's global taxi platform".

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `UberMove` (proprietary brand font)
- **Text font**: `UberMoveText` (proprietary brand text font)
- **Code font**: not observed; use `ui-monospace` only for implementation artifacts.
- **Weight normal / bold**: `500` / `700`

```css
:root {
  --uber-font-display: "UberMove", "UberMoveText", system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif;
  --uber-font-body: "UberMoveText", system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif;
  --uber-font-weight-normal: 500;
  --uber-font-weight-bold: 700;
}
body {
  font-family: var(--uber-font-body);
  font-weight: var(--uber-font-weight-normal);
  letter-spacing: 0;
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **UberMove / UberMoveText** are proprietary. When unavailable, use **Helvetica Neue** before generic system UI. This keeps the high x-height and compact service-product tone closer than Inter.
- **Open-source fallback**: `Inter` can work for body controls only if weight 500 is used and letter-spacing remains `0`. Do not add negative tracking to imitate brand sharpness.
- **Display fallback**: if `UberMove` is unavailable, prefer `Arial`/`Helvetica Neue` at 700 over ornamental display fonts. Uber's display voice is blunt and utilitarian, not editorial.
- **Line-height correction**: keep hero text around 52px/64px or 44px/52px. A generic 1.2 line-height often makes the stacked H1 feel too loose.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| hero-display | 52px | 700 | 64px | 0 |
| hero-mobile | 44px | 700 | 52px | 0 |
| section-title | 36px | 700 | 44px | 0 |
| compact-heading | 32px | 700 | 40px | 0 |
| card-title | 24px | 700 | 32px | 0 |
| body-large | 18px | 500 | 28px | 0 |
| body | 16px | 500 | 24px | 0 |
| nav / utility | 14px | 500 | 20px | 0 |
| micro | 12px | 500 | 16px | 0 |

> ⚠️ Key insight: Uber uses weight and scale, not letter-spacing, to create hierarchy. The extracted CSS had `letter-spacing: 0` wherever letter-spacing was declared.

### Principles
<!-- SOURCE: manual -->

1. Display type is blunt: large sizes use 700 weight and keep tracking at `0`.
2. Body controls are not light. Use 500 as the default service-interface weight.
3. The 16px/24px body unit is the operating rhythm for form labels, nav links, and compact descriptions.
4. 52px/64px and 44px/52px are the hero's recognizable stacked headline ratios.
5. Weight 300 is absent from the observed hierarchy; do not soften Uber into a light SaaS look.
6. The display/text split matters: use `UberMove` for the headline voice and `UberMoveText` for controls.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (1 step)
<!-- no custom token prefix found -->

| Token | Hex |
|---|---|
| brand-ink | `#000000` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light | Usage |
|---|---|---|
| surface | `#FFFFFF` | Page background, nav inverse text, primary button text |
| field | `#F3F3F3` | Pickup/dropoff inputs, light modules |
| hairline | `#E8E8E8` | Separators, quiet structure, dominant compiled frequency |
| neutral-300 | `#CBCBCB` | Secondary dividers and disabled-feeling marks |
| neutral-500 | `#A6A6A6` | Muted icon/text support |
| neutral-700 | `#5E5E5E` | Secondary text |
| neutral-800 | `#4B4B4B` | Deeper secondary copy |
| ink | `#000000` | Brand, text, nav background, primary CTA |

### 06-4. Accent Families
<!-- SOURCE: auto+manual -->

| Family | Key step | Hex |
|---|---|---|
| Focus blue | focus ring | `#276EF1` |
| Promotion mint | pill / campaign | `#ADDEC9` |
| Promotion pale | banner surface | `#EAF6ED` |
| Illustration warm | asset-only | `#B4540B` |
| Illustration cyan | asset-only | `#9DCDD6` |

### 06-5. Semantic
<!-- SOURCE: manual -->

| Token | Hex | Usage |
|---|---|---|
| action-primary | `#000000` | See prices, brand action, high-contrast CTA |
| action-primary-text | `#FFFFFF` | Primary button label |
| surface-page | `#FFFFFF` | Booking and content floor |
| surface-field | `#F3F3F3` | Location fields and quiet controls |
| border-subtle | `#E8E8E8` | Dividers and low-emphasis separators |
| focus-visible | `#276EF1` | Accessible focus ring and system highlight |
| campaign-soft | `#ADDEC9` | Promo CTA pill |
| text-muted | `#5E5E5E` | Secondary text |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto+manual -->

| Alias | Resolves to | Usage |
|---|---|---|
| `{colors.ink}` | `#000000` | Brand, primary text, black nav, primary CTA |
| `{colors.surface}` | `#FFFFFF` | Page floor and inverse text |
| `{colors.field}` | `#F3F3F3` | Form fields and low-friction modules |
| `{colors.hairline}` | `#E8E8E8` | Thin separators |
| `{colors.focus}` | `#276EF1` | Focus outline only; not broad brand fill |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---|---|
| hairline | `#E8E8E8` | 504 |
| ink | `#000000` | 126 |
| surface | `#FFFFFF` | 121 |
| field | `#F3F3F3` | 104 |
| focus | `#276EF1` | 40 |
| neutral-500 | `#A6A6A6` | 32 |
| text-muted | `#5E5E5E` | 26 |
| text-secondary | `#4B4B4B` | 12 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.ink}` (`#000000`)** — The real brand color in the UI. It owns logo, nav chrome, primary text, and the "See prices" action. The page should feel like a service console before it feels like a tech campaign.

**`{colors.surface}` (`#FFFFFF`)** — The booking floor. Uber keeps the task area plain so the form and CTA stay legible; white is not an absence here, it is the operating surface.

**`{colors.field}` (`#F3F3F3`)** — The input chassis. Pickup and dropoff are not hairline-bordered fields; they are gray physical modules with enough mass to read as destination machinery.

**`{colors.focus}` (`#276EF1`)** — Accessibility blue, not brand blue. Use it for focus outlines and system state; do not spread it across the hero or CTAs.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| space-4 | 4px | Icon-text micro adjustment |
| space-8 | 8px | Tight inline gaps, small radius pairing |
| space-12 | 12px | Button vertical padding, compact controls |
| space-16 | 16px | Form row gap, text-to-control distance |
| space-24 | 24px | Mobile page inset, card padding |
| space-32 | 32px | Section header separation |
| space-36 | 36px | Frequent grid gap |
| space-40 | 40px | Hero/form vertical rhythm |
| space-64 | 64px | Desktop section and container breathing room |

**주요 alias**:
- `container-desktop-x` -> 64px (wide viewport side padding)
- `container-mobile-x` -> 24px (small viewport side padding)
- `grid-gap-default` -> 36px (dominant compiled gap)
- `section-air` -> 64px (major vertical rhythm)

### Whitespace Philosophy
<!-- SOURCE: manual -->

Uber uses air as a workbench, not as luxury emptiness. The hero gives the booking form enough room to feel trustworthy, then lets dense modules live inside that open field: pickup/dropoff stack, black CTA, login text, and location selector all sit close enough to read as one task.

The spacing contrast is the system. Macro gaps such as 64px and 40px make the page easy to scan; micro gaps such as 8px, 12px, and 16px make the controls feel fast. Do not distribute everything evenly. Keep the task cluster dense and the section bands calm.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-xs | 4px | Tiny state/control details |
| radius-sm | 6px | Secondary utility surfaces |
| radius-md | 8px | Primary CTA, fields, cards; dominant radius |
| radius-lg | 12px | Larger module rounding |
| radius-xl | 16px | Media card / soft content blocks |
| radius-pill | 20px+ / 999px | Pills such as promo and pickup-time controls |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none | `none` | Most chrome and form modules |
| focus-ring | `inset 0 0 0 2px #FFFFFF, 0 0 0 2px #276EF1` | Accessible focus around controls |
| subtle-inset-light | `inset 999px 999px 0px rgba(0, 0, 0, 0.04)` | Hover/pressed tint technique on light surfaces |
| subtle-inset-dark | `inset 999px 999px 0px rgba(255, 255, 255, 0.1)` | Hover/pressed tint technique on dark surfaces |
| floating-card | `0 4px 16px hsla(0, 0%, 0%, 0.16)` | Limited elevated panels |
| bottom-sheet | `rgba(0, 0, 0, 0.08) 0px -8px 20px 0px` | Bottom/overlay affordance |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| motion-fast | 200ms | Common background/state changes |
| motion-standard | all 200ms cubic-bezier(0.4, 0, 0.2, 1) | Material-like control transition |
| motion-transform | transform 200ms ease-out | Lightweight reveal or interaction movement |
| motion-panel | all 500ms cubic-bezier(0.22, 1, 0.36, 1) | Larger panel transitions |
| motion-utility | backgroundSize | Link/background state sweep |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: 1280px core container; 1136px / 1152px also appear in compiled rules.
- **Grid type**: Flexbox for nav/control rows; CSS Grid for content grids.
- **Column count**: 12 columns at desktop, 8 at tablet, 4 at compact, 1 for mobile stacks.
- **Gutter**: 36px frequent grid gap; 24px mobile page inset; 64px desktop container padding.

### Hero
- **Pattern Summary**: 70-80vh task hero + black top chrome + left booking form + right illustration/promo card.
- Layout: two-column desktop split; left task controls, right visual panel.
- Background: white booking surface under black nav; promotion banner uses pale green.
- **Background Treatment**: solid `#FFFFFF` plus content imagery; no page-wide gradient.
- H1: `52px` / weight `700` / tracking `0`.
- Max-width: container around 1280px with desktop side air.

### Section Rhythm
```css
section {
  padding: 64px 64px;
  max-width: 1280px;
}
@media (max-width: 599px) {
  section { padding-left: 24px; padding-right: 24px; }
}
```

### Card Patterns
- **Card background**: `#FFFFFF` or image-backed asset tile.
- **Card border**: usually none; structural separation comes from spacing, image bounds, or hairline only when needed.
- **Card radius**: 8px dominant; 16px for larger visual modules.
- **Card padding**: 24px to 40px depending on density.
- **Card shadow**: mostly none; limited 0 4px 16px overlays.

### Navigation Structure
- **Type**: horizontal desktop nav with utility cluster; compact/mobile collapses into menu.
- **Position**: top site chrome; screenshot shows persistent first-viewport header.
- **Height**: approximately 64px.
- **Background**: `#000000`.
- **Border**: none; contrast alone defines the bar.

### Content Width
- **Prose max-width**: 396px / 400px appear for compact text blocks.
- **Container max-width**: 1280px primary, with 1136px/1152px content bands.
- **Sidebar width**: no persistent sidebar on homepage.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile base | 320px | Compiled rules begin with small viewport guard. |
| Tablet | 600px | Major min-width transition; grid and spacing expand. |
| Desktop | 1136px | Primary desktop layout threshold, most frequent media query. |
| Legacy tablet range | 768px-1119px | Secondary range-specific rules present. |

### Touch Targets
- **Minimum tap size**: 44px observed as recurring height/line-height value.
- **Button height (mobile)**: 44px to 48px expected from extracted heights and screenshot.
- **Input height (mobile)**: 52px to 56px visual field height; 64px appears for larger controls.

### Collapsing Strategy
- **Navigation**: desktop horizontal links and utility actions collapse into compact menu surfaces.
- **Grid columns**: 12 -> 8 -> 4 -> 1 based on media query ladder.
- **Sidebar**: none; content stacks.
- **Hero layout**: two-column hero becomes single-column booking-first stack.

### Image Behavior
- **Strategy**: responsive cropped assets and SVGs served through Uber asset/CDN URLs.
- **Max-width**: `100%` common.
- **Aspect ratio handling**: visual cards use square/cropped media behavior; screenshot hero asset sits in a bounded rectangular tile.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary action**

```html
<button class="button-primary">See prices</button>
```

| Spec | Value |
|---|---|
| Background | `#000000` |
| Text | `#FFFFFF` |
| Font | UberMoveText, 16px, weight 700 or 500 depending context |
| Radius | 8px |
| Padding | 14px 24px |
| Hover | inset tint or background transition, 200ms |
| Focus | `#276EF1` ring with white inner separation |
| Disabled | reduce contrast; do not swap to blue |

**Secondary pill**

```html
<button class="button-secondary-pill">Pickup now</button>
```

| Spec | Value |
|---|---|
| Background | `#F3F3F3` |
| Text | `#000000` |
| Radius | pill / 20px+ |
| Padding | 12px 16px |
| Icon gap | 8px |
| Hover | subtle dark inset tint |

### Badges

Uber does not use decorative marketing badges in the observed hero. Treat badge-like surfaces as utility pills.

```html
<span class="promo-pill">Learn more about the promotion</span>
```

| Spec | Value |
|---|---|
| Background | `#ADDEC9` |
| Text | `#000000` |
| Radius | 999px |
| Padding | 14px 22px |
| Weight | 700 or strong 500 |

### Cards & Containers

```html
<article class="suggestion-card">
  <img alt="" />
  <h3>Suggestion</h3>
  <a>Details</a>
</article>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` or media asset |
| Border | none by default |
| Radius | 8px / 16px depending media scale |
| Padding | 24px / 40px |
| Shadow | none; use 0 4px 16px only for overlays |
| Hover | background transition or link underline; avoid lift-heavy cards |

### Navigation

```html
<nav class="site-nav">
  <a class="logo">Uber</a>
  <a>Ride</a>
  <a>Drive</a>
  <a>About</a>
  <a>Help</a>
  <a>Log in</a>
  <a class="signup-pill">Sign up</a>
</nav>
```

| Spec | Value |
|---|---|
| Background | `#000000` |
| Text | `#FFFFFF` |
| Height | about 64px |
| Logo | white, larger than links |
| Link size | 14px / 20px |
| Link weight | 500-700 |
| Signup | white pill with black text |

### Inputs & Forms

```html
<label class="location-field">
  <span class="location-icon"></span>
  <input placeholder="Pickup location" />
</label>
```

| Spec | Value |
|---|---|
| Background | `#F3F3F3` |
| Border | 0 |
| Radius | 8px |
| Height | 56px visual target |
| Padding | 16px 20px |
| Placeholder | `#5E5E5E` |
| Focus | `#276EF1` ring, not blue fill |
| Error | not surfaced in homepage artifact |

### Hero Section

```html
<section class="booking-hero">
  <div class="booking-copy">
    <p>Seoul, KR</p>
    <h1>Uber's global taxi platform</h1>
    <form>...</form>
  </div>
  <div class="hero-visual">...</div>
</section>
```

| Spec | Value |
|---|---|
| Layout | desktop two-column, mobile stack |
| H1 | 52px/64px, 700, `UberMove` |
| Background | `#FFFFFF` |
| Form stack gap | 16px to 24px |
| Visual | illustration/card module, not abstract gradient |
| CTA | black primary + text secondary link |

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-primary**

| Spec | Value |
|---|---|
| Background | `#000000` |
| Text | `#FFFFFF` |
| Radius | 8px |
| State | hover uses subtle tint/transition; focus uses `#276EF1` outline |

**button-secondary-pill**

| Spec | Value |
|---|---|
| Background | `#F3F3F3` |
| Text | `#000000` |
| Radius | pill |
| State | hover darkens via inset overlay |

**signup-inverse-pill**

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#000000` |
| Context | black nav only |
| Radius | pill |

**input-location**

| Spec | Value |
|---|---|
| Background | `#F3F3F3` |
| Radius | 8px |
| Height | 56px |
| Focus | `#276EF1` ring |

**promo-pill**

| Spec | Value |
|---|---|
| Background | `#ADDEC9` |
| Text | `#000000` |
| Radius | pill |
| Context | temporary taxi promotion banner |

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

#### inset-overlay-state

```yaml
inset-overlay-state:
  description: "Uber creates hover/pressed state by flooding a surface with a giant inset shadow rather than swapping colour tokens."
  technique: "box-shadow: inset 999px 999px 0px rgba(0,0,0,.06) for darken; rgba(255,255,255,.06) for lighten on dark."
  applied_to: ["{components.button-primary}", "{components.button-secondary}", "control state overlays"]
  visual_signature: "the surface darkens or lightens without ever changing its semantic role — same button, more pressure."
  intent: "operational platforms must keep one true colour per role; state changes should look like physical pressure, not new tokens."
```

#### dual-focus-ring

```yaml
dual-focus-ring:
  description: "Focus separates blue from the underlying control with a white inner ring, not a glow."
  technique: "box-shadow: inset 0 0 0 2px #FFFFFF, 0 0 0 2px #276EF1; works on black, white, and grey field controls."
  applied_to: ["{components.input-field}", "{components.button-primary}", "focusable controls"]
  visual_signature: "accessibility ring stays crisp on every Uber surface — never a haloed SaaS glow."
  intent: "a transport product is used in motion and bright sun; focus must survive any contrast condition."
```

#### zero-tracking-geometry

```yaml
zero-tracking-geometry:
  description: "Uber type refuses both luxury negative tracking and spaced-out tech tracking."
  technique: "letter-spacing: 0 across declared text styles; UberMove display + UberMoveText body, weight 500/700."
  applied_to: ["{typography.display}", "{typography.body}", "control text"]
  visual_signature: "type reads blunt and operational — sturdy like a fleet number, never editorial or decorative."
  intent: "global multilingual product: tracking adjustments break across scripts; zero is the only honest default."
```

#### gray-field-chassis

```yaml
gray-field-chassis:
  description: "Input fields are solid grey modules rather than bordered forms."
  technique: "background #F3F3F3, radius 8px, no border, vertical target ≥48px on pickup/dropoff."
  applied_to: ["{components.input-pickup}", "{components.input-dropoff}", "search field"]
  visual_signature: "destination entry feels like a panel slot on a machine — not a web form to be polite about."
  intent: "ride entry is a 4-second task; outlines invite consideration, fills demand action."
```

#### mono-black-cta-on-everything

```yaml
mono-black-cta-on-everything:
  description: "Uber commits to one CTA colour — pure black — across light, dark, and image surfaces."
  technique: "background #000000, color #FFFFFF, radius 8px, padding 16px 24px; no gradient, no hover-shadow."
  applied_to: ["{components.button-primary}", "hero CTA", "card CTA", "footer CTA"]
  visual_signature: "the entire site has one unmistakable 'go' button — recognition is instant from any scroll position."
  intent: "monochrome action removes all interpretive noise; black means do, everything else is read."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Direct product promise, noun-heavy, no poetic flourish | "Uber's global taxi platform" |
| Primary CTA | Task command, short imperative | "See prices" |
| Secondary CTA | Account or context action, text-link style | "Log in to see your recent activity" |
| Promo | Plain benefit with one explicit action | "Take advantage of various taxi fare discounts!" |
| Tone | operational, confident, local, task-first | "Pickup location", "Dropoff location" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Uber — copy into your root stylesheet */
:root {
  /* Fonts */
  --uber-font-display: "UberMove", "UberMoveText", system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif;
  --uber-font-body: "UberMoveText", system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif;
  --uber-font-weight-normal: 500;
  --uber-font-weight-bold: 700;

  /* Brand / utility colors */
  --uber-color-brand-25:  #FFFFFF;
  --uber-color-brand-300: #5E5E5E;
  --uber-color-brand-500: #000000;
  --uber-color-brand-600: #000000;
  --uber-color-brand-900: #000000;

  /* Surfaces */
  --uber-bg-page:    #FFFFFF;
  --uber-bg-dark:    #000000;
  --uber-bg-field:   #F3F3F3;
  --uber-text:       #000000;
  --uber-text-muted: #5E5E5E;
  --uber-border:     #E8E8E8;
  --uber-focus:      #276EF1;
  --uber-promo:      #ADDEC9;

  /* Key spacing */
  --uber-space-sm:  12px;
  --uber-space-md:  24px;
  --uber-space-lg:  64px;

  /* Radius */
  --uber-radius-sm: 4px;
  --uber-radius-md: 8px;
  --uber-radius-lg: 16px;
}

body {
  margin: 0;
  background: var(--uber-bg-page);
  color: var(--uber-text);
  font-family: var(--uber-font-body);
  font-size: 16px;
  line-height: 24px;
  font-weight: var(--uber-font-weight-normal);
  letter-spacing: 0;
}

.uber-hero-title {
  font-family: var(--uber-font-display);
  font-size: clamp(44px, 5vw, 52px);
  line-height: 1.23;
  font-weight: 700;
  letter-spacing: 0;
}

.uber-button-primary {
  min-height: 48px;
  padding: 14px 24px;
  border: 0;
  border-radius: var(--uber-radius-md);
  background: var(--uber-bg-dark);
  color: #FFFFFF;
  font: 700 16px/20px var(--uber-font-body);
  transition: background 200ms cubic-bezier(0.4, 0, 0.2, 1);
}

.uber-button-primary:focus-visible {
  outline: 0;
  box-shadow: inset 0 0 0 2px #FFFFFF, 0 0 0 2px #276EF1;
}

.uber-location-field {
  min-height: 56px;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 20px;
  border-radius: var(--uber-radius-md);
  background: var(--uber-bg-field);
  color: var(--uber-text);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Uber-inspired
module.exports = {
  theme: {
    extend: {
      colors: {
        uber: {
          ink: '#000000',
          surface: '#FFFFFF',
          field: '#F3F3F3',
          hairline: '#E8E8E8',
          focus: '#276EF1',
          promo: '#ADDEC9',
          muted: '#5E5E5E',
        },
      },
      fontFamily: {
        uber: ['UberMoveText', 'system-ui', 'Helvetica Neue', 'Helvetica', 'Arial', 'sans-serif'],
        uberDisplay: ['UberMove', 'UberMoveText', 'system-ui', 'sans-serif'],
      },
      fontWeight: {
        normal: '500',
        bold: '700',
      },
      borderRadius: {
        uber: '8px',
        uberLg: '16px',
      },
      boxShadow: {
        uberFocus: 'inset 0 0 0 2px #FFFFFF, 0 0 0 2px #276EF1',
        uberOverlay: '0 4px 16px hsla(0, 0%, 0%, 0.16)',
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
| Brand primary | `{colors.ink}` | `#000000` |
| Background | `{colors.surface}` | `#FFFFFF` |
| Text primary | `{colors.ink}` | `#000000` |
| Text muted | `{colors.text-muted}` | `#5E5E5E` |
| Border | `{colors.hairline}` | `#E8E8E8` |
| Focus | `{colors.focus}` | `#276EF1` |
| Promo | `{colors.promotion-mint}` | `#ADDEC9` |

### Example Component Prompts

#### Hero Section
```text
Uber 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF, 상단 nav는 #000000
- H1: UberMove, 52px/64px, weight 700, letter-spacing 0
- 위치 줄: 16px/24px, weight 500, icon + "Seoul, KR" + underline link
- booking form: #F3F3F3 filled input blocks, 56px height, 8px radius
- CTA: #000000 background, #FFFFFF text, 8px radius, 14px 24px padding
- layout: desktop two-column, left booking task, right illustration/product card
```

#### Card Component
```text
Uber 스타일 콘텐츠 카드를 만들어줘.
- 배경: #FFFFFF, border 없음, radius 8px 또는 16px
- padding: 24px desktop, 16px mobile
- shadow: 기본 none; overlay가 필요할 때만 0 4px 16px hsla(0,0%,0%,0.16)
- 제목: UberMoveText, 24px/32px, weight 700
- 본문: 16px/24px, weight 500, color #000000 또는 #5E5E5E
```

#### Badge
```text
Uber 프로모션 pill을 만들어줘.
- bg #ADDEC9, text #000000
- radius 999px, padding 14px 22px
- font UberMoveText, 16px, weight 700
- hover는 색 변경이 아니라 subtle inset tint로만 처리
```

#### Navigation
```text
Uber 스타일 상단 네비게이션을 만들어줘.
- 높이 약 64px, 배경 #000000, border 없음
- 로고와 링크는 #FFFFFF
- 링크: 14px/20px, weight 500-700
- 우측 Sign up은 #FFFFFF pill + #000000 text
- focus-visible은 #276EF1 ring
```

### Iteration Guide

- **색상 변경 시**: `#000000`, `#FFFFFF`, `#F3F3F3` 삼각 구조를 먼저 유지한다.
- **파란색 사용 시**: `#276EF1`은 focus/system state로 제한한다.
- **폰트 변경 시**: body 기본 weight를 400으로 내리지 말고 500을 유지한다.
- **여백 조정 시**: 24px mobile inset, 64px desktop section air, 36px grid gap을 우선 사용한다.
- **컴포넌트 추가 시**: outlined input보다 filled gray module을 먼저 선택한다.
- **모션 추가 시**: 200ms state transition 안에서 끝낸다. bounce/parallax는 Uber 톤이 아니다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#000000` as the primary brand/action color.
- Keep the booking task visible in the first viewport.
- Use `UberMove` for display and `UberMoveText` for controls/body.
- Keep letter-spacing at `0` across the type system.
- Build inputs as filled `#F3F3F3` modules with 8px radius.
- Use `#276EF1` for focus rings and accessible state, not hero decoration.
- Let promo colors stay scoped to temporary campaign surfaces.
- Prefer surface contrast and spacing over heavy shadows.

### ❌ DON'T

- 브랜드/primary CTA를 `#276EF1`로 두지 말 것 — 대신 `#000000` 사용.
- 입력 필드 배경을 `#FFFFFF`로 두고 hairline outline만 쓰지 말 것 — 대신 filled `#F3F3F3` 사용.
- 네비게이션 배경을 `#FFFFFF`로 만들지 말 것 — 첫 viewport chrome은 `#000000` 사용.
- 기본 텍스트를 `#333333`로 흐리게 두지 말 것 — primary text는 `#000000`, secondary는 `#5E5E5E` 사용.
- promo pill을 saturated green `#00FF00` 또는 brand blue `#276EF1`로 만들지 말 것 — 대신 soft `#ADDEC9` 사용.
- body에 `font-weight: 400`을 기본값으로 쓰지 말 것 — Uber control rhythm은 500 중심이다.
- H1에 negative letter-spacing `-0.02em`을 넣지 말 것 — Uber는 `letter-spacing: 0`이다.
- primary button을 pill radius `999px`로 만들지 말 것 — core action control은 8px rounded rectangle이다.
- card hover를 큰 translate/scale로 만들지 말 것 — subtle tint/transition만 사용.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- Second brand color: none. `#276EF1` exists, but not as a broad brand fill.
- Page-wide gradient: absent. The homepage uses solid surfaces and assets.
- Decorative outline input style: absent in the booking hero; fields are filled modules.
- Letter-spacing tricks: none. Declared letter spacing is `0`.
- Luxury thin typography: absent. Weight 300 does not define the interface.
- Heavy card elevation: mostly none. Shadow is scoped to overlays/focus, not every card.
- Pastel palette spread: absent. Mint appears as campaign support only.
- Rounded-everything softness: absent. Core radius is 8px, not universal pill.
- Marketing-first hero copy: absent. The first viewport is task-first booking language.
- Catalog product imagery / shelf illustration on the counter: absent. There is no aisle, only the trip slip.
- Logo wall under hero as marketplace trophy shelf: zero. Nothing presents itself as a vendor catalog.
- Second cart counter / inventory badge: never. Uber Eats lives elsewhere; this dispatch counter has none.
- Pickup/dropoff field decorative iconography or shelf labels: absent. Fields are pure gray slip pads.
- Marketing pricing card grid before the counter call: never. Pricing arrives only after the slip is filed.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single captured homepage state** — analysis reused existing `uber` phase1 artifacts and the screenshot state showing Korea-localized taxi promotion. Other geographies may expose different modules.
- **No custom-property token layer** — extracted CSS had 0 resolved custom properties. Token names in this guide are practical aliases, not observed CSS variable names.
- **Framework not asserted** — HTML/CSS indicate a compiled SSR web app, but the exact framework was not inferred beyond available artifacts.
- **Form validation states not surfaced** — pickup/dropoff error, loading, disabled, and autocomplete states were not visited.
- **Mobile visual screenshot not captured in this pass** — responsive behavior is inferred from media queries and existing desktop screenshot, not a fresh mobile screenshot.
- **Motion runtime not executed** — CSS transition values were extracted, but JavaScript-driven scroll or panel animation was not traced.
- **Asset colors may pollute frequency** — warm/cyan illustration colors such as `#B4540B` and `#9DCDD6` are treated as asset-only, not UI palette anchors.
- **Report HTML intentionally skipped** — per request, Step 6 RENDER-HTML was not run; only `design.md` was produced.
