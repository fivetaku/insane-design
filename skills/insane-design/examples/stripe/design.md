---
schema_version: 3.2
slug: stripe
service_name: Stripe
site_url: https://stripe.com
fetched_at: 2026-05-03T07:15:28Z
default_theme: mixed
brand_color: "#533AFD"
primary_font: sohne-var
font_weight_normal: 300
token_prefix: hds

bold_direction: Gradient Infrastructure
aesthetic_category: Refined SaaS
signature_element: typo_contrast
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv3
design_system_level_evidence: "HDS namespace, 320 CSS variables, 315 resolved tokens, tiered core/util/action/component aliases, and explicit component states."

colors:
  hds-color-core-brand-600: "#533AFD"
  hds-color-core-brand-500: "#665EFD"
  hds-color-core-neutral-25: "#F8FAFD"
  hds-color-core-neutral-990: "#061B31"
  hds-color-core-neutralDark-990: "#0D1738"
  hds-color-core-neutral-50: "#E5EDF5"
  hds-color-core-orange-350: "#FF6118"
  hds-color-core-success-400: "#00B261"
  hds-color-core-error-400: "#F3432A"
typography:
  display: "sohne-var"
  body: "sohne-var"
  code: "SourceCodePro"
  ladder:
    - { token: hds-font-heading-xxl, size: "2.125rem|3.5rem", weight: 300, line_height: "1.03", tracking: "-0.02em" }
    - { token: hds-font-heading-xl, size: "1.75rem|2.125rem|3rem", weight: 300, line_height: "1.07", tracking: "-0.01em" }
    - { token: hds-font-text-md, size: "1rem", weight: 300, line_height: "1.4", tracking: "0em" }
    - { token: hds-font-input-label-md, size: "0.875rem", weight: 400, line_height: "1.3", tracking: "0px" }
  weights_used: [300, 400, 425, 450, 500, 550, 600, 700]
  weights_absent: []
components:
  hds-button-primary: { bg: "{colors.hds-color-core-brand-600}", radius: "4px", padding_block: "15.5px 16.5px", padding_inline: "24px" }
  hds-button-secondary: { bg: "transparent", border: "1px", radius: "4px", padding_block: "calc button padding minus 1px" }
  hds-navigation-menu: { max_width: "1349px", radius: "6px", gap: "28px", padding: "16px 24px" }
  hds-textinput: { height: "48px", radius: "4px", border: "1px" }
---

# DESIGN.md — Stripe Designer Guidebook

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Stripe is not a generic fintech landing page. It is a glass-walled payment terminal room: bright enough for institutional trust, technical enough for developers, and constantly threaded with motion, product UI fragments, and chromatic energy. The visual system starts on a near-white technical floor, but the page is remembered through compressed gradients and the canonical violet #533AFD (`{colors.hds-color-core-brand-600}`), as if the circuitry beneath the surface is briefly visible.

The typography is the tell. Stripe's page does not rely on heavy SaaS boldness; there is no poster-weight founder manifesto voice. Headings sit at weight 300 with tight optical tracking, so the H1 feels machined rather than shouted, like engraved labeling on precision equipment. Body copy also stays light. This lets dense product diagrams, bento panels, stats, and navigation behave like an operations console whose labels are calm even when the system behind them is busy.

Color works in two registers. The product chrome uses cool neutrals like #F8FAFD (`{colors.hds-color-core-neutral-25}`), #E5EDF5 (`{colors.hds-color-core-neutral-50}`), and dark ink #0D1738 (`{colors.hds-color-core-neutralDark-990}`): not white paper, but the pale blue-gray enamel of financial infrastructure. The brand moments are concentrated: #533AFD for action, focus, and gradient terminals; #FF6118 and hot magentas appear as current inside illustrations and bento graphics, not as a second general UI color. No second brand color gets equal citizenship.

The craft signature is layered infrastructure: 12-column grids, small-radius controls, dual shadows, blurred overlays, gradient orbs, and many responsive breakpoints. Navigation behaves like a translucent control-room visor rather than a flat dropdown. Shadows belong to panels and product graphics like depth cues on stacked hardware, while the chrome itself stays disciplined. Nothing is rustic, soft editorial, or playful-card casual. Stripe's surface is polished but busy: a financial operating system being staged as a marketing site, with the page trying to disappear just enough for the machinery to feel inevitable.

To pull the picture tighter: the gradient orb behind the hero behaves like a magnetometer reading rendered into wallpaper, the bento product cards act like instrument cluster panels lifted out of an aircraft cockpit, and the dashboard previews look like oscilloscope traces pinned to a glass wall. The customer logo strip is the row of port stickers on a payment terminal — proof of throughput, not decoration. The compressed `weight: 300` headlines arrive like serial numbers etched into chrome, never shouting. There is no second brand color competing with `#533AFD` because the room is already lit by violet edge-light.

### Key Characteristics

- HDS namespace throughout: `--hds-*` core, util, action, component, and surface aliases.
- Canonical brand action is #533AFD, not the older public-logo purple alone.
- Default text is light-weight `sohne-var`; headings use weight 300 with negative tracking at larger sizes.
- Neutral surfaces are cool blue-gray, especially #F8FAFD and #E5EDF5, rather than plain beige or warm off-white.
- Hero structure uses a 12-column grid and min-height `min(68svh, 826px)` on tablet/desktop.
- Buttons are compact 4px-radius HDS controls, not oversized rounded pills.
- Motion is mostly compositional: gradient graphics, carousel progress, menu overlays, and state transitions with `.3s cubic-bezier(.25,1,.5,1)`.
- Shadows are multi-layered and directional, frequently mixing `rgba(50,50,93,...)` with black alpha.
- Navigation is a serious component: `max-width: 1349px`, menu viewport, overlay blur, and responsive hamburger behavior.
- Negative space is systematic but not empty; Stripe uses space to separate dense modules, not to create luxury minimalism.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Gradient Infrastructure
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **lightweight typography stretched over gradient infrastructure diagrams**으로 기억된다.
> **Code Complexity**: high — HDS tokens, 390 media queries, multi-layer shadows, gradient graphics, overlay blur, and stateful navigation all interact.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Stripe처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "sohne-var", "SF Pro Display", -apple-system, sans-serif;
  font-weight: 300;
  color: #0D1738;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #F8FAFD;
  --fg: #0D1738;
  --muted: #64748D;
}

/* 3. 브랜드 컬러 */
:root {
  --brand: #533AFD;
  --brand-hover: #4032C8;
  --border: #E5EDF5;
}
```

**절대 하지 말아야 할 것 하나**: Stripe를 `font-weight: 400`의 평범한 Inter SaaS로 만들지 말 것. 실제 인상은 `sohne-var` 300 + tight tracking + violet action tokens에서 나온다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://stripe.com` |
| Fetched | 2026-05-03T07:15:28Z |
| Extractor | reused existing phase1 + CSS + index.html artifacts |
| HTML size | 573555 bytes |
| CSS files | 7 external CSS files, total 427883 chars |
| Token prefix | `hds` |
| Phase1 evidence | `brand_candidates.json`, `typography.json`, `alias_layer.json`, `resolved_tokens.json` |
| Method | CSS custom property parsing + HTML/CSS structural interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: SSR marketing site with generated bundled CSS and componentized HTML.
- **Design system**: Stripe HDS — prefix `hds`.
- **CSS architecture**:
  ```text
  core       (--hds-color-core-*)       raw ramps and primitives
  util       (--hds-color-util-*)       semantic utility aliases
  action     (--hds-color-action-*)     interactive actions and focus
  component  (--hds-button-*, etc.)     component-level values
  surface    (--hds-color-surface-*)    page and container semantics
  ```
- **Class naming**: BEM-like component names such as `.hds-button`, `.hero-section__layout-grid`, `.hds-navigation-menu__trigger`.
- **Default theme**: mixed. Light marketing surface first, dark adaptive tokens for selected sections and overlays.
- **Font loading**: custom `sohne-var`, `SourceCodePro`, and system fallback declarations.
- **Canonical anchor**: Primary action and focus settle on `--hds-color-core-brand-600: #533AFD`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `sohne-var` (commercial/custom brand font)
- **Body font**: `sohne-var`, fallback `"SF Pro Display"`, then system sans.
- **Code font**: `SourceCodePro`
- **Weight normal / bold**: `300` / `500-700` depending on component and locale.

```css
:root {
  --hds-font-family: "sohne-var", "SF Pro Display", sans-serif;
  --hds-font-family-code: SourceCodePro;
  --hds-font-weight-normal: 300;
  --hds-font-weight-bold: 500;
}

body {
  font-family: "sohne-var", "SF Pro Display", sans-serif;
  color: #0D1738;
}
```

### Note on Font Substitutes

- **Sohne substitute** — Use **Inter** only with restraint: body at 300, headings at 300, and avoid default Inter 400 density. Inter's x-height and rhythm will feel louder than Sohne, so reduce headline letter-spacing only where Stripe already does it (`-0.01em` to `-0.02em`).
- **Display fallback** — `SF Pro Display` is the closer macOS substitute for the hero and HDS headings. Keep line-height tight: `1.03` for XXL and `1.07` for XL.
- **Code fallback** — If `SourceCodePro` is unavailable, use `ui-monospace` or `SFMono-Regular`; keep it visually secondary and never let monospace become the brand voice.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `hds-font-heading-xs` | `1rem` | 400 | `1.2` | `0em` |
| `hds-font-heading-sm` | `1.125rem / 1.25rem / 1.375rem` | 300 | `1.25` | `0em` |
| `hds-font-heading-md` | `1.25rem / 1.375rem / 1.625rem` | 300 | `1.2` | `-0.01em` |
| `hds-font-heading-lg` | `1.375rem / 1.75rem / 2rem` | 300 | `1.2` | `-0.01em` |
| `hds-font-heading-xl` | `1.75rem / 2.125rem / 3rem` | 300 | `1.07` | `-0.01em` |
| `hds-font-heading-xxl` | `2.125rem / 3.5rem` | 300 | `1.03` | `-0.02em` |
| `hds-font-heading-hero-sm` | `1.625rem / 2rem / 2.25rem` | 300 | `1.12` | `-0.01em` |
| `hds-font-heading-hero-lg` | `1.75rem / 3rem` | 300 | `1.1` | `-0.01em` |
| `hds-font-text-md` | `1rem` | 300 | `1.4` | `0em` |
| `hds-font-input-label-md` | `0.875rem` | 400 | `1.3` | `0px` |

> ⚠️ Stripe's visual identity is not only the size ladder; it is the combination of light weights, compact line-height, and negative display tracking.

### Principles

1. Body and most prose sit at weight 300. This is the main Stripe correction; using 400 immediately turns the page into generic SaaS.
2. Display sizes get optical compression. The largest heading token uses `letter-spacing: -0.02em`; mid-large headings use `-0.01em`; body keeps `0em`.
3. Inputs and labels are slightly sturdier than prose. Label tokens use weight 400 while surrounding copy remains 300.
4. Locale-specific overrides exist. Japanese and Chinese selectors lift weight to 400/500/600, so the system is not a single universal weight map.
5. Hero does not need huge 72px typography. The captured scale tops at `3.5rem` for XXL and `3rem` for hero/lg contexts; authority comes from layout and graphics.
6. Monospace is a supporting technical accent, not the main brand font.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (15 steps)

| Token | Hex |
|---|---|
| `--hds-color-core-brand-25` | `#F5F5FF` |
| `--hds-color-core-brand-50` | `#E8E9FF` |
| `--hds-color-core-brand-75` | `#E2E4FF` |
| `--hds-color-core-brand-100` | `#D6D9FC` |
| `--hds-color-core-brand-200` | `#B9B9F9` |
| `--hds-color-core-brand-300` | `#9A9AFE` |
| `--hds-color-core-brand-400` | `#7F7DFC` |
| `--hds-color-core-brand-500` | `#665EFD` |
| `--hds-color-core-brand-600` | `#533AFD` |
| `--hds-color-core-brand-700` | `#4032C8` |
| `--hds-color-core-brand-800` | `#2E2B8C` |
| `--hds-color-core-brand-900` | `#1C1E54` |
| `--hds-color-core-brand-950` | `#161741` |
| `--hds-color-core-brand-975` | `#0F1137` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--hds-color-core-brandDark-25` | `#F6F7FF` |
| `--hds-color-core-brandDark-100` | `#C3D3FF` |
| `--hds-color-core-brandDark-300` | `#92ADFF` |
| `--hds-color-core-brandDark-500` | `#5D64FE` |
| `--hds-color-core-brandDark-600` | `#533AFD` |
| `--hds-color-core-brandDark-700` | `#362BAA` |
| `--hds-color-core-brandDark-800` | `#2C2484` |
| `--hds-color-core-brandDark-975` | `#171055` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 / 25 | `#FFFFFF` / `#F8FAFD` | `#F2F7FE` |
| 50 / 100 | `#E5EDF5` / `#D4DEE9` | `#E3ECF7` / `#D4DEEF` |
| 200 / 300 | `#BAC8DA` / `#95A4BA` | `#C0CEE6` / `#A3B5D6` |
| 500 / 600 | `#64748D` / `#50617A` | `#6480B2` / `#45639D` |
| 800 / 900 | `#273951` / `#1A2C44` | `#23356E` / `#182659` |
| 975 / 990 | `#0D253D` / `#061B31` | `#101D4E` / `#0D1738` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Orange | `--hds-color-core-orange-350` | `#FF6118` |
| Lemon | `--hds-color-core-lemon-200` | `#F9B900` |
| Success | `--hds-color-core-success-400` | `#00B261` |
| Error | `--hds-color-core-error-400` | `#F3432A` |
| Gradient stop | `--accent-gradient-color-stop-1` | `#BDB4FF` |
| Gradient stop | `--accent-gradient-color-stop-2` | `#643AFD` |

### 06-5. Semantic

| Token | Resolves to | Usage |
|---|---|---|
| `--hds-color-action-bg-solid` | `#533AFD` | primary action background |
| `--hds-color-action-bg-solidHover` | `#4032C8` | primary hover |
| `--hds-color-action-focus-outer` | `#533AFD` | focus ring |
| `--hds-color-surface-bg-subdued` | `#F8FAFD` or dark adaptive | subdued sections |
| `--hds-color-surface-border-quiet` | `#E5EDF5` or dark adaptive | hairline borders |
| `--hds-color-text-solid` | `#061B31` / `#FFFFFF` adaptive | text on current theme |
| `--hds-color-input-border-error` | `#F3432A` family | invalid state |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--hds-color-button-primary-bg` | `--hds-color-action-bg-solid` | primary button |
| `--hds-color-button-secondary-border` | action border aliases | secondary button border |
| `--hds-color-input-bg-default` | translucent neutral values | input field base |
| `--hds-color-input-border-default` | neutral border values | input chrome |
| `--hds-color-shadow-xs-top` | `#0037700F` / `#0D173826` | elevation top layer |
| `--hds-color-shadow-xs-bottom` | `#003B890A` / `#0D173833` | elevation bottom layer |

### 06-7. Dominant Colors (실제 DOM/CSS 빈도 순)

| Hex | Frequency | Role |
|---|---:|---|
| `#FFFFFF` / `#fff` | 43 combined approx | white surfaces and text |
| `#0D1738` | 15 in phase1 selector/frequency evidence | body text / dark neutral |
| `#F8FAFD` | 11 | subdued surface |
| `#533AFD` | 10 | brand action |
| `#FF6118` | 8 | illustration/accent energy |
| `#061B31` | 7 | deep neutral |
| `#FB76FA` | 6 | gradient/graphic accent |
| `#7232F1` | 6 | gradient/graphic accent |

### 06-8. Color Stories

**`--hds-color-core-brand-600` (`#533AFD`)** — The canonical Stripe action violet. It owns primary buttons, focus, gradient terminals, and the interactive confidence of the page. Use it as the action anchor, not as a page-wide wash.

**`--hds-color-core-neutral-25` (`#F8FAFD`)** — The cool infrastructure floor. It is close to white but carries enough blue-gray temperature to make white cards, diagrams, and browser chrome separate cleanly.

**`--hds-color-core-neutralDark-990` (`#0D1738`)** — The ink color that prevents the light-weight type from disappearing. It is deep navy, not black, and keeps Stripe away from stark monochrome minimalism.

**`--hds-color-core-neutral-50` (`#E5EDF5`)** — The quiet hairline and divider color. Stripe leans on this more than heavy borders; it lets dense sections remain readable without boxed-card clutter.

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---:|---|
| `--hds-space-core-50` | `4px` | icon/link micro gaps |
| `--hds-space-core-100` | `8px` | common compact gap |
| `--hds-space-core-150` | `12px` | input and list rhythm |
| `--hds-space-core-200` | `16px` | layout gap, mobile content margin |
| `--hds-space-core-300` | `24px` | button inline padding, larger gaps |
| `--hds-space-core-400` | `32px` | section row gap |
| `--hds-space-core-550` | `44px` | button/input height anchor |
| `--hds-space-core-700` | `56px` | mobile section gap |
| `--hds-space-core-800` | `64px` | tablet section gap |
| `--hds-space-core-1200` | `96px` | desktop section top/bottom gap |
| `--hds-space-core-2500` | `200px` | large-scale graphic spacing |

**주요 alias**:
- `--hds-space-layout-columns` → `4 / 8 / 12` responsive grid columns.
- `--hds-space-layout-gap` → `16px`, reused by grids and section headers.
- `--hds-space-section-gap-top` → `56px / 64px / 96px` across breakpoints.
- `--hds-space-button-height` → `44px`, matching touch-target minimum.

### Whitespace Philosophy

Stripe uses whitespace as routing infrastructure. The page is not sparse; it is densely illustrated and information-heavy. The air appears in section boundaries, grid gutters, and content-column separation so the system can carry dashboards, stats, bento modules, and nav menus without collapsing into noise.

The spacing ladder is unusually explicit: 2px increments at the bottom, then 8px rhythm, then 56/64/96px section scales. That lets Stripe make compact UI controls and large marketing bands feel like one system.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `--hds-space-core-radius-xs` | `2px` | checkbox/small marks |
| `--hds-space-core-radius-sm` | `4px` | primary buttons, inputs, most controls |
| `--hds-space-core-radius-md` | `6px` | navigation menu, popovers |
| `--hds-space-core-radius-lg` | `16px` | larger cards or media modules |
| `--hds-space-core-radius-xl` | `32px` | oversized graphic containers |
| `--hds-space-core-radius-round` | `99999px` | circular/fully round exceptions |

Stripe's default control radius is small. Recreating it with 999px pill buttons is one of the fastest ways to lose the HDS feel.

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| `xs` | top `0 2px 10px #0037700F`, bottom `0 1px 4px #003B890A` | subtle UI elevation |
| `sm` | top `0 5px 14px #00377014`, bottom `0 2px 8px #003B890D` | small popovers/cards |
| `md` | top `0 6px 22px #0037701A`, bottom `0 4px 8px #003B8905` | medium panels |
| `lg` | top `0 15px 40px -2px #0037701A`, bottom `0 5px 20px -2px #003B890A` | prominent modules |
| `xl` | top `0 20px 80px -16px #00377024`, bottom `0 10px 60px -16px #003B890F` | hero/product graphics |
| graphic | `0 30px 60px -12px rgba(50,50,93,.25), 0 18px 36px -18px rgba(0,0,0,.3)` | diagram depth |

Pattern: Stripe's elevation is almost never a single generic shadow. It pairs colored navy top/bottom layers or the classic `rgba(50,50,93)` plus black-alpha stack.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / pattern | Value | Usage |
|---|---|---|
| button transition | `.3s cubic-bezier(.25,1,.5,1)` | background/color/border on HDS buttons |
| reduced motion | `prefers-reduced-motion` branches | accessible animation gating |
| navigation overlay | opacity + blur transition | menu open/close |
| carousel state | `--carousel-card-scale`, progress clamp | card scaling |
| bento reveal | `.5s cubic-bezier(.33,1,.68,1)` | dialog/graphic reveal |

Motion is precise and component-scoped. Avoid decorative global page animations that are not tied to a real component state.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: navigation `1349px`; other content uses HDS section containers and CSS variables.
- **Grid type**: CSS Grid with responsive HDS columns.
- **Column count**: `4` mobile, `8` tablet, `12` desktop via `--hds-space-layout-columns`.
- **Gutter**: `--hds-space-layout-gap: 16px` and component-specific gaps.

### Hero

- **Pattern Summary**: `min(68svh, 826px) + 12-column grid + lightweight H1 + gradient/product graphics`.
- Layout: `.hero-section__layout-grid` uses `grid-template-columns: repeat(12, minmax(0, 1fr))`.
- Background: light/cool surface with full-bleed divider lines and chromatic graphic layers.
- **Background Treatment**: gradient-mesh/product-ui composition, not a plain gradient hero.
- H1: `sohne-var`, hero tokens up to `3rem`, weight `300`, tracking `-0.01em`.
- Max-width: grid-bounded, not a centered single text column.

### Section Rhythm

```css
.section-container {
  padding-block-start: var(--section-container-pbs-dt, var(--hds-space-core-1200));
  padding-block-end: var(--section-container-pbe-dt, var(--hds-space-core-800));
}

.hero-section__layout-grid {
  display: grid;
  column-gap: var(--hds-space-core-200);
  row-gap: var(--hds-space-core-400);
  grid-template-columns: repeat(12, minmax(0, 1fr));
}
```

### Card Patterns

- **Card background**: mostly #FFFFFF or #F8FAFD-adjacent surfaces, sometimes translucent.
- **Card border**: quiet #E5EDF5 / dark adaptive hairline.
- **Card radius**: 6px for menus and many panels; 16px/32px for larger graphic containers.
- **Card padding**: 16px to 32px common, larger bento modules use 48px+ equivalents.
- **Card shadow**: dual shadow or no shadow; never a generic single 0 4 12 shadow.

### Navigation Structure

- **Type**: horizontal desktop navigation with stateful menu viewport; collapses below desktop.
- **Position**: page-top marketing nav; menu overlay/viewport is componentized.
- **Height**: `--navigation-height: 76px`.
- **Background**: transparent until menu/open contexts; overlay uses gradient + blur.
- **Border**: radius `6px`; open menu removes lower radius.

### Content Width

- **Prose max-width**: content-specific `ch` limits appear, e.g. 42ch, 36ch, 32ch.
- **Container max-width**: navigation `1349px`; section/graphic modules use variable constraints.
- **Sidebar width**: no fixed app-sidebar pattern on homepage; bento/dialog modules create local side columns.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `<640px` | 4-column layout, extra hero vertical padding, collapsed nav |
| Tablet | `640px` | 8-column HDS layout, row gaps increase |
| Desktop | `940px` | 12-column HDS layout, desktop section padding, full nav/menu behavior |
| Wide | `1264px+ / 1300px+` | graphic and carousel refinements |

### Touch Targets

- **Minimum tap size**: `44px` from `--hds-space-button-height`.
- **Button height mobile**: mobile padding `13.5px / 14.5px` yields approximately 44px.
- **Input height mobile**: text input uses `height: var(--hds-space-core-600)` = 48px.

### Collapsing Strategy

- **Navigation**: desktop menu becomes hamburger/collapsed menu below desktop.
- **Grid columns**: 4 → 8 → 12 HDS columns.
- **Sidebar**: no global sidebar; dialog and bento side columns collapse locally.
- **Hero layout**: mobile adds large block padding (`72px`/`88px`) while desktop relies on min-height and grid.

### Image Behavior

- **Strategy**: product graphics and illustrations are component-scoped with grid placement.
- **Max-width**: frequent `100%`, `min(...)`, and fixed graphic constraints.
- **Aspect ratio handling**: handled per component; no single global image rule was proven.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<a class="hds-button" href="#">
  Start now
  <span class="hds-icon-hover-arrow"></span>
</a>
```

| Property | Value |
|---|---|
| font | `var(--hds-font-family)`, `1rem`, weight `var(--hds-font-weight-bold)` |
| base bg | `--hds-color-button-primary-bg` → `#533AFD` |
| hover bg | `--hds-color-button-primary-bgHover` → `#4032C8` |
| radius | `--hds-space-core-radius-sm` = `4px` |
| padding | `15.5px 16.5px` block, `24px` inline |
| focus | `outline: 2px solid var(--hds-color-action-border-solid); outline-offset: 3px` |
| transition | `.3s cubic-bezier(.25,1,.5,1)` |
| disabled | disabled bg/text tokens, cursor default |

### Badges

Badges are not the primary homepage signature in the extracted evidence. When needed, use HDS text scales (`0.75rem` to `0.875rem`), small radius (`2px` or `4px`), and semantic action/surface aliases rather than inventing a new saturated badge system.

### Cards & Containers

```html
<article class="stripe-infra-card">
  <h3 class="hds-heading hds-heading--md">Reliable infrastructure</h3>
  <p class="hds-text hds-text--md">Dense product content on a cool neutral surface.</p>
</article>
```

| Property | Value |
|---|---|
| background | `#FFFFFF`, `#F8FAFD`, or translucent `rgba(248,250,253,.45)` |
| border | `1px solid #E5EDF5` or adaptive surface border |
| radius | 6px for chrome, 16px+ for larger visual modules |
| shadow | dual HDS shadow or graphic shadow stack |
| hover | border/color/transform only where component evidence exists |

### Navigation

```html
<nav class="hds-navigation-menu">
  <button class="hds-navigation-menu__trigger">Products</button>
  <a class="hds-button hds-button--transparent">Sign in</a>
</nav>
```

| Property | Value |
|---|---|
| max-width | `1349px` |
| padding | `16px 24px` |
| gap | `28px` |
| radius | `6px`, lower radius removed when open |
| overlay | `linear-gradient(transparent, rgba(236,239,241,.8))` + `backdrop-filter: blur(5px)` |
| trigger font | `0.875rem` |

### Inputs & Forms

```html
<label class="hds-field">
  <span class="hds-label">Email</span>
  <input class="hds-textinput" type="email" />
</label>
```

| Property | Value |
|---|---|
| height | `48px` (`--hds-space-core-600`) |
| border | `1px solid var(--hds-color-input-border-default)` |
| radius | `4px` |
| padding | around `16px` vertical and `16px/24px` horizontal depending component |
| focus | `3px` focus outline on relevant controls |
| invalid | `--hds-color-input-border-error` |

### Hero Section

The hero is a grid/graphic system, not a text-only center stack. Keep the H1 light, compress tracking, place CTA(s) in the grid, and let product/gradient composition create the memorable mass.

### 13-2. Named Variants

| Variant | Spec | Notes |
|---|---|---|
| `hds-button-primary` | #533AFD bg, #4032C8 hover, 4px radius | action anchor |
| `hds-button-secondary` | transparent bg, 1px border, hover border | secondary on subdued surfaces |
| `hds-button-transparent` | transparent bg, text color changes on hover | nav and low-emphasis actions |
| `hds-button-compact` | `11.5px / 12.5px` block padding | dense nav/util actions |
| `hds-navigation-menu` | 1349px max, 6px radius, menu viewport | desktop global nav |
| `hds-textinput` | 48px height, 4px radius, focus/invalid states | form controls |

### 13-3. Signature Micro-Specs

#### stripe-lightweight-display-compression

```yaml
stripe-lightweight-display-compression:
  description: "Large headings stay engineered and calm instead of becoming heavy SaaS display type."
  technique: "font-family: sohne-var; font-weight: 300; line-height: 1.03-1.07; letter-spacing: -0.01em to -0.02em"
  applied_to: ["{typography.ladder.hds-font-heading-xl}", "{typography.ladder.hds-font-heading-xxl}", "{component.hero-section}"]
  visual_signature: "A financial-infrastructure H1 that feels engraved and precise, not shouted or poster-bold."
```

#### hds-dual-shadow-elevation

```yaml
hds-dual-shadow-elevation:
  description: "Depth is built from layered blue/navy shadow tokens rather than a single generic drop shadow."
  technique: "box-shadow stacks such as 0 6px 22px #0037701A, 0 4px 8px #003B8905; graphic depth mixes rgba(50,50,93,.25) with rgba(0,0,0,.3)"
  applied_to: ["{component.cards-containers}", "{component.hero-section}", "{component.stripe-infra-card}"]
  visual_signature: "Panels read like stacked interface hardware with directional depth, never like flat SaaS cards floating on gray."
```

#### blurred-navigation-veil

```yaml
blurred-navigation-veil:
  description: "The desktop navigation opens as a translucent system layer, not a conventional dropdown box."
  technique: "linear-gradient(transparent, rgba(236,239,241,.8)) with backdrop-filter: blur(5px); navigation height 76px; menu radius 6px with lower radius removed when open"
  applied_to: ["{components.hds-navigation-menu}", "{component.navigation.overlay}", "{component.navigation.menu-viewport}"]
  visual_signature: "A control-room visor effect: page content remains present, but softened behind the menu plane."
```

#### cool-neutral-infrastructure-floor

```yaml
cool-neutral-infrastructure-floor:
  description: "The page floor keeps Stripe's graphics and violet actions vivid without turning the UI into a purple site."
  technique: "surface #F8FAFD /* {colors.hds-color-core-neutral-25} */; border #E5EDF5 /* {colors.hds-color-core-neutral-50} */; ink #0D1738 /* {colors.hds-color-core-neutralDark-990} */"
  applied_to: ["{component.page-surface}", "{component.cards-containers}", "{component.inputs-forms}"]
  visual_signature: "A pale blue-gray infrastructure enamel where gradients feel like live current inside the product layer."
```

#### small-radius-precision-controls

```yaml
small-radius-precision-controls:
  description: "Interactive chrome stays rectangular and precise, avoiding consumer-fintech pill softness."
  technique: "button radius 4px; input radius 4px; navigation/menu radius 6px; button padding 15.5px 24px 16.5px; compact padding 11.5px/12.5px"
  applied_to: ["{components.hds-button-primary}", "{components.hds-button-secondary}", "{components.hds-textinput}", "{components.hds-navigation-menu}"]
  visual_signature: "Controls feel like exact infrastructure switches rather than friendly rounded payment-app buttons."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Infrastructure promise + business outcome | "Financial infrastructure to grow your revenue." |
| Primary CTA | direct action, short | "Start now" |
| Secondary CTA | product exploration | "Contact sales" / "Explore payments" |
| Subheading | expands audience and capability | "Accept payments, offer financial services..." |
| Tone | confident, technical, revenue-oriented | global commerce, reliable infrastructure, extensible stack |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Stripe-inspired HDS baseline */
:root {
  /* Fonts */
  --hds-font-family: "sohne-var", "SF Pro Display", -apple-system, sans-serif;
  --hds-font-family-code: SourceCodePro, ui-monospace, SFMono-Regular, monospace;
  --hds-font-weight-normal: 300;
  --hds-font-weight-bold: 500;

  /* Brand */
  --hds-color-brand-25:  #F5F5FF;
  --hds-color-brand-300: #9A9AFE;
  --hds-color-brand-500: #665EFD;
  --hds-color-brand-600: #533AFD;
  --hds-color-brand-900: #1C1E54;

  /* Surfaces */
  --hds-bg-page:    #F8FAFD;
  --hds-bg-quiet:   #FFFFFF;
  --hds-bg-dark:    #0D1738;
  --hds-text:       #0D1738;
  --hds-text-muted: #64748D;
  --hds-border:     #E5EDF5;

  /* Key spacing */
  --hds-space-sm:  8px;
  --hds-space-md:  16px;
  --hds-space-lg:  24px;
  --hds-space-xl:  64px;
  --hds-space-section: 96px;

  /* Radius */
  --hds-radius-sm: 4px;
  --hds-radius-md: 6px;
  --hds-radius-lg: 16px;
}

body {
  font-family: var(--hds-font-family);
  font-weight: var(--hds-font-weight-normal);
  background: var(--hds-bg-page);
  color: var(--hds-text);
}

.stripe-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 15.5px 24px 16.5px;
  border-radius: var(--hds-radius-sm);
  background: var(--hds-color-brand-600);
  color: #FFFFFF;
  font-weight: var(--hds-font-weight-bold);
  line-height: 1;
  transition:
    background-color .3s cubic-bezier(.25,1,.5,1),
    color .3s cubic-bezier(.25,1,.5,1),
    border .3s cubic-bezier(.25,1,.5,1);
}

.stripe-button:hover {
  background: #4032C8;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Stripe-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        stripe: {
          brand: '#533AFD',
          brandHover: '#4032C8',
          bg: '#F8FAFD',
          ink: '#0D1738',
          border: '#E5EDF5',
          muted: '#64748D',
          orange: '#FF6118',
        },
      },
      fontFamily: {
        sans: ['sohne-var', 'SF Pro Display', 'system-ui', 'sans-serif'],
        mono: ['SourceCodePro', 'ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal: '300',
        medium: '500',
        bold: '600',
      },
      borderRadius: {
        sm: '4px',
        md: '6px',
        lg: '16px',
      },
      boxShadow: {
        hds: '0 6px 22px #0037701A, 0 4px 8px #003B8905',
        graphic: '0 30px 60px -12px rgba(50,50,93,.25), 0 18px 36px -18px rgba(0,0,0,.3)',
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
| Brand primary | `--hds-color-core-brand-600` | `#533AFD` |
| Brand hover | `--hds-color-core-brand-700` | `#4032C8` |
| Background | `--hds-color-core-neutral-25` | `#F8FAFD` |
| Text primary | `--hds-color-core-neutralDark-990` | `#0D1738` |
| Text muted | `--hds-color-core-neutral-500` | `#64748D` |
| Border | `--hds-color-core-neutral-50` | `#E5EDF5` |
| Success | `--hds-color-core-success-400` | `#00B261` |
| Error | `--hds-color-core-error-400` | `#F3432A` |

### Example Component Prompts

#### Hero Section

```text
Stripe 스타일 히어로 섹션을 만들어줘.
- 배경: #F8FAFD, 텍스트: #0D1738
- H1: sohne-var, 3rem~3.5rem, weight 300, line-height 1.03~1.1, tracking -0.01em
- 레이아웃: 12-column CSS Grid, min-height min(68svh, 826px)
- CTA: #533AFD 배경, #FFFFFF 텍스트, 4px radius, 15.5px 24px 16.5px padding
- 그래픽: product UI + violet/orange gradient accents, not generic abstract blobs
```

#### Card Component

```text
Stripe HDS 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF 또는 #F8FAFD
- border: 1px solid #E5EDF5
- radius: 6px for chrome, 16px for larger graphic modules
- shadow: 0 6px 22px #0037701A, 0 4px 8px #003B8905
- 제목: sohne-var, weight 300, letter-spacing -0.01em
- 본문: 1rem, weight 300, color #0D1738, line-height 1.4
```

#### Badge

```text
Stripe 스타일 배지를 만들어줘.
- font: sohne-var, 0.75rem~0.875rem
- radius: 4px 이하
- bg: #F5F5FF 또는 #F8FAFD
- color: #533AFD 또는 #0D1738
- border: 1px solid #E5EDF5
```

#### Navigation

```text
Stripe 스타일 상단 네비게이션을 만들어줘.
- height: 76px
- nav max-width: 1349px
- menu padding: 16px 24px, gap 28px, radius 6px
- links: 0.875rem, lightweight text, hover to #0D1738
- dropdown overlay: transparent-to-rgba gradient + backdrop-filter blur(5px)
- CTA: compact HDS button with #533AFD
```

### Iteration Guide

- **색상 변경 시**: #533AFD를 액션 앵커로 유지하고, #FF6118은 illustration/graphic accent 범위에 둔다.
- **폰트 변경 시**: `font-weight: 300`을 먼저 맞춘 뒤 크기를 조정한다.
- **여백 조정 시**: 8px core ladder와 56/64/96px section ladder를 섞어 쓴다.
- **새 컴포넌트 추가 시**: 4px/6px radius, quiet border, dual shadow 원칙을 따른다.
- **다크 섹션 추가 시**: dark adaptive neutral/brandDark tokens를 써라. light palette에 opacity만 얹지 않는다.
- **반응형**: 640px, 940px, 1264px 계열 breakpoints를 우선 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #533AFD as the canonical action color and #4032C8 for primary hover.
- Keep body and headings light: `font-weight: 300` is the default Stripe read.
- Use cool blue-gray neutrals: #F8FAFD, #E5EDF5, #0D1738, #061B31.
- Build with a 4/8/12 responsive grid and 16px HDS layout gap.
- Use 4px buttons and 6px menu/panel radius before reaching for large radii.
- Apply dual shadows for elevation; use `rgba(50,50,93,...)` style depth on graphics.
- Gate decorative motion with reduced-motion awareness.
- Treat the navigation menu as a real component with overlay, blur, and state.

### ❌ DON'T

- 배경을 `#FFFFFF` 단독 또는 `white` 전체 페이지로 두지 말 것 — 대신 `#F8FAFD`를 기본 surface로 사용.
- 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#0D1738` 또는 `#061B31` 사용.
- Primary CTA를 `#635BFF`만으로 고정하지 말 것 — 현재 action anchor는 `#533AFD`, hover는 `#4032C8`.
- Orange `#FF6118`을 primary button color로 쓰지 말 것 — illustration/accent energy로 제한.
- Border를 `#DDDDDD` 같은 warm gray로 두지 말 것 — 대신 `#E5EDF5` 또는 HDS adaptive border 사용.
- body에 `font-weight: 400` 사용 금지 — Stripe의 기본 인상은 `font-weight: 300`.
- CTA 버튼을 `border-radius: 999px` pill로 만들지 말 것 — 기본 HDS control은 `4px`.
- 단층 `box-shadow: 0 4px 12px rgba(0,0,0,.1)`로 대체하지 말 것 — Stripe는 dual shadow/elevation stack을 쓴다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Warm beige system: absent. Stripe neutrals are cool blue-gray, not cream/tan.
- Heavy display weight: never the default. Big type is light and compressed, not bold and loud.
- Pill-first controls: absent from default HDS buttons. The system starts at 4px radius.
- Single flat brand color everywhere: no. #533AFD is concentrated in actions and gradient endpoints.
- Generic purple-blue AI gradient: no. Stripe gradients are tied to product graphics and accent families, not full-page decoration.
- Black typography: absent. The ink is navy (#0D1738 / #061B31), not #000000.
- Card-only SaaS layout: no. The page uses bento graphics, stats, carousels, and product UI fragments beyond feature cards.
- Warm drop shadows: absent. Elevation uses blue/navy shadow tokens and `rgba(50,50,93,...)`.
- Static brochure nav: no. The nav is stateful, overlay-based, and component-rich.
- Over-rounded friendly fintech tone: absent. Stripe is precise infrastructure, not bubbly consumer finance.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-only scope** — This guidebook reused the existing `stripe` homepage HTML/CSS/phase1 artifacts. Checkout, dashboard, docs, and authenticated product surfaces were not visited.
- **Screenshot not reinterpreted in-browser** — Existing `hero-cropped.png` was available, but this run skipped Step 6 HTML rendering and did not perform a fresh browser screenshot comparison.
- **CSS bundle ambiguity** — Seven CSS files were present and parsed together. Some selectors may belong to below-the-fold modules or shared HDS components rather than the first viewport only.
- **Component extraction partial** — Phase1 `components.json`, `layout.json`, and `responsive.json` carried "No CSS files found" warnings from an older extractor; component analysis was therefore interpreted from raw CSS snippets and HTML counts.
- **Dark-mode mapping incomplete** — Dark adaptive tokens are present, but a full light/dark semantic matrix was not exhaustively mapped.
- **Motion logic not fully traced** — CSS transitions, keyframes, and reduced-motion media queries were observed; JavaScript scroll triggers, carousel timing internals, and menu state logic were not executed.
- **Exact font metrics unavailable** — `sohne-var` was detected, but precise variable font axes and license details were not measured from font binaries.
- **Logo/graphic color contamination possible** — Frequency candidates include illustration and gradient colors such as #FF6118, #FB76FA, and #7232F1. They are intentionally treated as accents, not primary UI tokens.
- **Form-state coverage limited** — Input focus/invalid/disabled styles are present in CSS, but live form validation flows were not exercised.
