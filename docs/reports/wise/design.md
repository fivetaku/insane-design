---
schema_version: 3.2
slug: wise
service_name: Wise
site_url: https://wise.com
fetched_at: 2026-04-14T01:14:00+09:00
default_theme: light
brand_color: "#9FE870"
primary_font: "Wise Sans"
font_weight_normal: 400
token_prefix: "wise"

bold_direction: "Friendly Fintech"
aesthetic_category: "other"
signature_element: "typo_contrast"
code_complexity: high

medium: web
medium_confidence: high

archetype: landing-utility
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "559 CSS variables, resolved token chains, WDS/EDS button and layout classes, and repeated component aliases are present in production CSS."

colors:
  primary: "#9FE870"
  ink: "#163300"
  display-ink: "#0E0F0C"
  content-primary: "#37517E"
  content-secondary: "#5D7079"
  accent-blue: "#00A2DD"
  surface: "#FFFFFF"
  border: "#C9CBCE"
  warning: "#FFD11A"
  negative: "#E74848"
typography:
  display: "Wise Sans"
  body: "Inter"
  ladder:
    - { token: hero, size: "clamp(6rem, calc(3.38571rem + 3.42857vw), 7.5rem)", weight: 900, tracking: "0" }
    - { token: h2, size: "clamp(3.125rem, calc(-9.38377rem + 20.17544vw), 6rem)", weight: 900, tracking: "0" }
    - { token: body, size: "1rem", weight: 400, tracking: "0" }
    - { token: small, size: "0.875rem", weight: 400, tracking: "0" }
  weights_used: [400, 500, 600, 700, 900]
  weights_absent: [300, 800]
components:
  button-primary-lime: { bg: "{colors.primary}", color: "{colors.ink}", radius: "9999px", height: "48px", padding: "12px 24px" }
  button-accent-blue: { bg: "{colors.accent-blue}", color: "#FFFFFF", radius: "3px", height: "48px", padding: "12px 24px" }
  button-secondary: { bg: "#FFFFFF", color: "{colors.ink}", border: "inset 0 0 0 1px #C9CBCE" }
  nav-pill-signup: { bg: "{colors.primary}", color: "{colors.ink}", radius: "9999px" }
---

# DESIGN.md - Wise

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Wise reads like a currency exchange rendered in monumental display type — a white canvas stripped bare so the headline can land like a billboard, with a lime-green accent as the sole instrument of action.

The homepage keeps the canvas almost brutally plain: a #FFFFFF (`{colors.surface}`) page, a fixed calm header, and a massive black-green headline in #0E0F0C (`{colors.display-ink}`). The emotional move is not decoration. It is scale. "MONEY FOR HERE, THERE AND EVERYWHERE" lands as a billboard, then the product earns softness through a lime pill CTA and a world/coin visual below the fold.

The system's signature accent is not the common blue finance color. The remembered color is #9FE870 (`{colors.primary}`), a high-energy lime used for signup and account-opening actions. It sits against #163300 (`{colors.ink}`), a deep green-black that makes the button feel proprietary rather than neon. Blue still exists in the CSS as #00A2DD (`{colors.accent-blue}`), but it behaves like an older action accent and link layer, not the homepage's emotional anchor.

Typography carries most of the brand. Display copy uses "Wise Sans" with black weight behavior around 900, while body and utility text sit in Inter at 400/600. The contrast is deliberate: a gigantic display face for confidence, plain body text for financial trust. Letter-spacing stays at 0; Wise gets density from weight and uppercase mass, not tracking tricks.

The layout philosophy is "open exchange canvas, operational dashboard underneath." The first viewport gives the headline room to dominate, then immediately exposes concrete actions: open an account, send money, currency controls, app QR, country/currency claims. Every visual flourish is tied to movement of money — a currency exchange that refuses to look like a bank, because the instrument is the product.

Wise는 결국 **money flow의 단일 exchange 입구**다. centered canvas hero는 거대한 스위치 한 개를 누르기 전의 단순 입구이고, 거대한 black-green 카피는 그 스위치 위에 새겨진 라벨, 라임 pill은 손가락이 닿는 단 하나의 버튼이다. currency calculator와 country grid는 dashboard의 옆 칸 다이얼들이지, 메인 도구가 아니다. white canvas는 수리 매트, 라임은 켜진 단일 LED, deep forest ink는 도구 손잡이의 무광 마감이다.

### Key Characteristics

- Huge uppercase display headline, centered, black-weight, no negative tracking.
- Lime #9FE870 (`{colors.primary}`) is the modern Wise CTA color; it pairs with #163300 (`{colors.ink}`), not white text.
- White page surface dominates; color appears in controls, illustration, and utility states.
- Navigation is quiet, horizontal, and product-led: Personal, Business, Platform, language, Help, Log in, Sign up.
- CTA hierarchy is asymmetric: filled lime pill for the main action, underlined text link for secondary intent.
- CSS exposes a real system layer: WDS/EDS classes, `--color-*`, `--size-*`, `--radius-*`, and button aliases.
- Rounded pills coexist with squarer legacy blue buttons; this split is part of the production system.
- Hero imagery is literal finance-world imagery, not abstract SaaS gradients.
- Motion exists as small entrance/drop patterns and carousel controls, not as background spectacle.
- Product density increases after the hero through calculators, cards, country coverage, QR, and app prompts.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Friendly Fintech
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **oversized black display type softened by a lime money-action pill**으로 기억된다.
> **Code Complexity**: high — production CSS includes multiple design-system layers, container queries, responsive clamps, WDS/EDS components, and motion utilities.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Wise처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter", Helvetica, Arial, sans-serif;
  font-weight: 400;
}
h1,
.display {
  font-family: "Wise Sans", "Inter", sans-serif;
  font-weight: 900;
  letter-spacing: 0;
  text-transform: uppercase;
}

/* 2. 배경 + 텍스트 */
:root {
  --wise-bg: #FFFFFF;
  --wise-ink: #163300;
  --wise-display: #0E0F0C;
}
body { background: var(--wise-bg); color: var(--wise-ink); }

/* 3. 브랜드 컬러 */
:root { --wise-lime: #9FE870; }
.primary-cta {
  background: var(--wise-lime);
  color: var(--wise-ink);
  border-radius: 9999px;
  min-height: 48px;
  padding: 12px 24px;
}
```

**절대 하지 말아야 할 것 하나**: Wise를 파란 핀테크 SaaS처럼 만들지 말 것. #00A2DD는 존재하지만, 현재 homepage의 기억점은 #9FE870 lime CTA와 #0E0F0C display headline이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://wise.com` |
| Fetched | 2026-04-14T01:14:00+09:00 |
| Extractor | Existing phase1 reuse: HTML + CSS + screenshot |
| HTML size | 1,109,283 bytes (Next.js SSR/hydrated page) |
| CSS files | 3 external + 1 inline, total 1,738,901 chars |
| Token prefix | `wise` (CSS variables use generic `--color-*`, `--size-*`, WDS/EDS/MW component namespaces) |
| Method | CSS custom properties, resolved token samples, frequency candidates, HTML structure, and desktop screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js production page (`__NEXT_DATA__` present, hashed CSS bundles)
- **Design system**: Wise/WDS/EDS/MW production system - tokens and classes include `wds-Button`, `eds-*`, `mw-*`, `np-*`, `btn-*`
- **CSS architecture**:
  ```text
  core       (--color-*, --size-*, --radius-*)       raw values and semantic roles
  system     (wds-Button, eds-flex, mw-container)    layout and component APIs
  legacy     (btn, np-btn, np-theme-personal)        older TransferWise-era controls
  app/page   (NavigationDesktop_*, Section_*)        module-scoped page composition
  ```
- **Class naming**: mixed utility + component classes; CSS modules for page sections, BEM-like WDS button modifiers, Bootstrap-like spacing/display utilities.
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: production CSS references `"Wise Sans","Inter",sans-serif` for display and `"Inter",Helvetica,Arial,sans-serif` for regular text.
- **Canonical anchor**: homepage hero in the screenshot: centered uppercase display headline, lime account CTA, secondary underlined send-money link, and finance/world imagery below.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `"Wise Sans"` (brand font; production CSS token `--font-family-display`)
- **Body font**: `"Inter"` (production CSS token `--font-family-regular`)
- **Code font**: `ui-monospace, SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace`
- **Weight normal / bold / black**: `400` / `700` / `900`

```css
:root {
  --wise-font-family-display: "Wise Sans", "Inter", sans-serif;
  --wise-font-family-regular: "Inter", Helvetica, Arial, sans-serif;
  --wise-font-weight-regular: 400;
  --wise-font-weight-semi-bold: 600;
  --wise-font-weight-bold: 700;
  --wise-font-weight-black: 900;
}
body {
  font-family: var(--wise-font-family-regular);
  font-weight: var(--wise-font-weight-regular);
}
.display {
  font-family: var(--wise-font-family-display);
  font-weight: var(--wise-font-weight-black);
}
```

### Note on Font Substitutes

- **Wise Sans** is the display signature. If unavailable, use **Inter Tight Black** or **Archivo Black** only for hero/display text, with `letter-spacing: 0` and `text-transform: uppercase`.
- Keep body text on **Inter 400/600**. Do not use the substitute display font for paragraphs; the Wise contrast depends on display/body separation.
- If using Inter instead of Wise Sans for display, push weight to `900` and reduce line-height to roughly `0.9-0.95`; otherwise the all-caps headline becomes too polite.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Hero display | `clamp(6rem, calc(3.38571rem + 3.42857vw), 7.5rem)` | `900` | ~`0.9` | `0` |
| Large display | `clamp(4.375rem, calc(2.41429rem + 2.57143vw), 5.5rem)` | `900` | ~`0.95` | `0` |
| Section h2 | `clamp(3.125rem, calc(-9.38377rem + 20.17544vw), 6rem)` | `900` | ~`1.0` | `0` |
| Body large | `clamp(1.125rem, calc(.58114rem + .87719vw), 1.25rem)` | `400` / `600` | ~`1.4` | `0` |
| Body | `1rem` | `400` | ~`1.5` | `0` |
| Small utility | `0.875rem` | `400` / `600` | ~`1.4` | `0` |

> ⚠️ Wise does not get its tone from delicate tracking. It gets it from black display weight, uppercase scale, and ordinary readable body text.

### Principles

1. Display type is a brand asset, not just a heading style: use `"Wise Sans"` at 900 for the hero and major campaign lines.
2. Body text remains operational: Inter 400 carries explanations, legal-ish clarity, and product details without competing with the display face.
3. Weight 600 is the utility emphasis weight for nav, buttons, and compact labels; 700 exists but should not become the default.
4. Letter-spacing stays at `0`. Adding negative tracking makes Wise feel like Apple; adding positive tracking makes it feel like generic editorial.
5. The scale jump from body text to hero headline is intentionally extreme. Replacing the hero with a 48-64px SaaS headline loses the brand immediately.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (lime/action)

| Token | Hex |
|---|---|
| `--color-interactive-accent` (dark/personal context sample) | `#9FE870` |
| lime hover | `#80E142` |
| lime active | `#65CF21` |
| lime pale surface | `#E2F6D5` |
| lime mid surface | `#D3F2C0` |
| lime muted | `#C5EDAB` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--color-interactive-primary` | `#163300` |
| primary hover | `#0D1F00` |
| primary active / display ink | `#0E0F0C` |
| dark green secondary | `#1C3108` |

### 06-3. Neutral Ramp

| Step | Light | Dark / Ink |
|---|---|---|
| Screen | `#FFFFFF` | `#0E0F0C` |
| Border / secondary interactive | `#C9CBCE` | `#5D7079` |
| Border hover | `#B5B7BA` | `#37517E` |
| Border active | `#A7A9AB` | `#21231D` |
| Muted content | `#768E9C` | `#121511` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Blue action / legacy accent | accent | `#00A2DD` |
| Blue hover | hover | `#008FC9` |
| Blue active | active | `#0081BA` |
| Teal celebration | celebration content | `#A0E1E1` |
| Yellow warning | warning primary | `#FFD11A` |
| Red negative | negative interactive | `#E74848` |
| Green positive | positive interactive | `#2EAD4B` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--color-background-screen` | `#FFFFFF` | default page/surface |
| `--color-background-elevated` | `#FFFFFF` | raised panels and cards |
| `--color-content-primary` | `#37517E` / contextual `#0E0F0C` | primary content depending theme/context |
| `--color-content-secondary` | `#5D7079` | supporting copy, secondary links |
| `--color-interactive-accent` | `#00A2DD` / contextual `#9FE870` | primary action accent by theme generation |
| `--color-interactive-secondary` | `#C9CBCE` | secondary borders and controls |
| `--color-interactive-negative` | `#E74848` | destructive/error action |
| `--color-interactive-warning` | `#DF8700` | warning action |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--btn-height` | `--input-height-base` / `48px` | medium CTA and form control height |
| `--btn-padding` | `--input-padding` / `12px 24px` | default button horizontal rhythm |
| `--btn-radius-base` | `9999px` or `3px` | theme-dependent pill vs legacy square button |
| `--input-height-base` | `48px` / `--size-32` | forms and currency selectors |
| `--input-padding` | `12px 16px` | text inputs and select-like controls |
| `--mw-space-4` | `clamp(1rem, calc(0.94231rem + 0.25641vw), 1.25rem)` | marketing spacing unit |

### 06-7. Dominant Colors (actual CSS frequency)

| Token | Hex | Frequency |
|---|---|---|
| Surface | `#FFFFFF` | 164 CSS occurrences |
| Content primary | `#37517E` | 137 |
| Blue accent | `#00A2DD` | 63 |
| Deep green | `#163300` | 58 |
| Content secondary | `#5D7079` | 55 |
| Border | `#C9CBCE` | 52 |
| Blue semantic | `#0097C7` | 48 |
| Negative | `#E74848` | 37 |
| Display dark | `#21231D` | 34 |
| Lime | `#9FE870` | 28 |

### 06-8. Color Stories

**`{colors.primary}` (`#9FE870`)** - The remembered Wise action color on the homepage. Use it for account-opening and signup pills where the user is moving forward; pair with `#163300`, not white, so it reads as Wise lime instead of generic neon.

**`{colors.display-ink}` (`#0E0F0C`)** - The display headline ink. It is warmer and greener than pure black; using `#000000` makes the hero harsher and less branded.

**`{colors.surface}` (`#FFFFFF`)** - The page floor. Wise uses clean white to make finance tasks feel simple, then relies on type scale and lime action rather than tinted panels.

**`{colors.content-primary}` (`#37517E`)** - The older/utility primary content blue. It shows up heavily in CSS frequency and semantic text roles, but should not replace the homepage display ink or lime CTA.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--side-margin` | `24px` | base page side margin |
| `--mw-space-3` | `clamp(0.75rem, calc(0.70673rem + 0.19231vw), 0.9375rem)` | compact marketing gaps |
| `--mw-space-4` | `clamp(1rem, calc(0.94231rem + 0.25641vw), 1.25rem)` | default row/section micro gap |
| `--mw-space-6` | `clamp(1.5rem, calc(1.41346rem + 0.38462vw), 1.875rem)` | column gap and CTA group rhythm |
| `--size-32` | `32px` | nav/action primitive |
| `--size-48` | `48px` | button/input height primitive |
| `--size-64` | `64px` | icon/media and larger rhythm |
| `--size-96` | `96px` | large display/section rhythm |
| `--size-120` | `120px` | oversized marketing scale |

**주요 alias**:
- `--btn-height` -> `48px` / `--input-height-base` (medium CTA height)
- `--column-gap` -> `16px` or `--mw-space-3` (marketing grid gap)
- `--row-gap` -> `16px` or `--mw-space-3` (stacked grid rhythm)

### Whitespace Philosophy

Wise gives the first viewport a lot of white air, but not a luxury amount of emptiness. The whitespace is there to make the huge all-caps headline legible and memorable before the product widgets arrive. The CTA group is close enough to the copy that the page still feels transactional.

Below the hero, the spacing compresses into product grids, calculators, coverage blocks, and app prompts. The pattern is not "minimal everywhere"; it is "big breath for the promise, tighter rhythm for the money task."

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--radius-small` | `10px` | prompt/card/control base radius |
| `--radius-medium` | `16px` | larger panel and marketing blocks |
| `--radius-large` | `24px` | large rounded containers |
| `--radius-full` | `9999px` | lime CTA pill, sign-up pill, round controls |
| `--mw-radius-1` | `clamp(0.625rem, calc(0.58894rem + 0.16026vw), 0.78125rem)` | marketing card radius |
| `--mw-radius-2` | `clamp(1rem, calc(0.94231rem + 0.25641vw), 1.25rem)` | larger responsive card radius |
| `--mw-radius-3` | `clamp(1.5rem, calc(1.41346rem + 0.38462vw), 1.875rem)` | big image/card radius |
| legacy `--btn-radius-base` | `3px` | older blue `.btn-accent` buttons |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none | `none` | most chrome and navigation |
| hairline inset | `inset 0 0 0 1px #C9CBCE` | secondary controls and borders |
| focus/error ring | `inset 0 0 0 3px var(--color-sentiment-negative)` | validation and state emphasis |
| card shadow | `0 10px 32px 0 rgba(0,0,0,.15), 0 40px 40px 0 rgba(0,0,0,.04)` | elevated cards/media |
| soft media glow | `0 0 40px rgba(69,71,69,.2)` | image/illustration depth |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `--animation-duration` | `400ms` | default entrance/simple motion |
| `--animation-duration-long` | `800ms` | longer campaign/hero motion |
| `--animation-delay` | `100ms` | stagger setup |
| `--transition-timing` | `0.3s ease-out` | carousel/control motion |
| button transition | `.15s ease-in-out` | legacy `.btn-accent` color/background changes |
| navigation transition | `var(--navigation-animation-duration) var(--navigation-transition-timing-function)` | desktop navigation color/background/border transitions |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `1440px` via `.mw-container { --container-width: 1440px; }`
- **Grid type**: CSS Grid for `.mw-cluster*`, flex for CTA sets and nav groups
- **Column count**: responsive clusters; homepage coverage blocks use dense repeated card grids
- **Gutter**: `--mw-space-6` for columns, `--mw-space-8` / marketing row gaps where available

### Hero

- **Pattern Summary**: `large white hero + centered uppercase H1 + lime pill CTA + underlined secondary link + finance/world imagery below`
- Layout: one-column centered copy at top, visual/product layer appears below; nav remains horizontal above.
- Background: `#FFFFFF` solid.
- **Background Treatment**: solid white, no gradient mesh, no atmospheric blur.
- H1: `clamp(6rem, calc(3.38571rem + 3.42857vw), 7.5rem)` / weight `900` / tracking `0`
- Max-width: visually around the central hero column; page container max-width is `1440px`.

### Section Rhythm

```css
.mw-container {
  --container-width: 1440px;
  --container-margin: var(--mw-space-4);
  max-width: var(--container-width);
  margin-inline: var(--container-margin);
}
@media (min-width: 992px) {
  .mw-container { --container-margin: 80px; }
}
@media (min-width: 1200px) {
  .mw-container { --container-margin: 100px; }
}
```

### Card Patterns

- **Card background**: mostly `#FFFFFF`, sometimes colored semantic/prompt surfaces.
- **Card border**: inset hairline `#C9CBCE` for secondary/control states.
- **Card radius**: `10px`, `16px`, `24px`, or responsive `--mw-radius-*`.
- **Card padding**: built from `--size-16`, `--size-24`, and marketing space clamps.
- **Card shadow**: restrained; when present, two-layer shadow `0 10px 32px rgba(0,0,0,.15)` plus `0 40px 40px rgba(0,0,0,.04)`.

### Navigation Structure

- **Type**: horizontal desktop navigation with grouped product links.
- **Position**: relative in captured CSS; sticky/fixed behavior not proven from static analysis.
- **Height**: `var(--navigation-desktop-primary-height)` with 32px button primitives.
- **Background**: `#FFFFFF` via `--color-background-screen`.
- **Border**: not a heavy divider; state changes are color/background/border transitions.

### Content Width

- **Prose max-width**: hero paragraph is visually narrow, centered, around 520-600px.
- **Container max-width**: `1440px`.
- **Sidebar width**: no persistent sidebar on homepage; footer/nav panels use grouped columns.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `max-width: 575px` / `max-width: 767px` | compact buttons and grid collapse |
| Small | `min-width: 576px` | container margin increases to `32px` |
| Tablet | `min-width: 768px` | grid and cluster patterns expand |
| Desktop | `min-width: 992px` | nav/CTA desktop behavior, container margin `80px` |
| Large | `min-width: 1200px` | container margin `100px`, larger layout variants |
| Wide | `min-width: 1440px` / `1640px` | large visual and centered max-width behavior |

### Touch Targets

- **Minimum tap size**: 48px is the practical base (`--btn-height`, `--input-height-base`).
- **Button height (mobile)**: `48px`.
- **Input height (mobile)**: `48px` base; some theme contexts resolve to `--size-32`.

### Collapsing Strategy

- **Navigation**: desktop nav classes exist; mobile collapse not fully verified in static screenshot.
- **Grid columns**: `.mw-cluster*` starts one-column and expands through `min-width` breakpoints.
- **Sidebar**: no homepage sidebar.
- **Hero layout**: copy remains centered; visual layer stacks below the headline and CTA group.

### Image Behavior

- **Strategy**: responsive marketing imagery below hero text; object-fit behavior not fully isolated.
- **Max-width**: images appear constrained by `.mw-container` and section wrappers.
- **Aspect ratio handling**: CSS includes large figure heights such as `--contentFigureHeight: 538px/632px`.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary lime pill**

```html
<button class="primary-cta">Open an account</button>
```

| Spec | Value |
|---|---|
| Background | `#9FE870` |
| Text | `#163300` |
| Radius | `9999px` |
| Height | `48px` |
| Padding | `12px 24px` |
| Weight | `600` |
| Hover | use `#80E142` when using the lime ramp |
| Active | use `#65CF21` when using the lime ramp |

**Legacy/accent blue button**

```html
<button class="btn btn-accent btn-md">Send money</button>
```

| Spec | Value |
|---|---|
| Background | `#00A2DD` |
| Hover | `#008FC9` |
| Active | `#0081BA` |
| Text | `#FFFFFF` |
| Transition | `color, background-color .15s ease-in-out` |
| Radius | `3px` in legacy theme contexts |

### Badges

Wise does not make the homepage identity out of decorative badges. Compact labels should inherit utility type: Inter, 14px, weight 600, deep green/neutral text, and avoid saturated chip colors unless tied to product status.

```html
<span class="wise-utility-label">with fees as low as 0.1%</span>
```

| Spec | Value |
|---|---|
| Font | `Inter` |
| Size | `0.875rem` |
| Weight | `600` |
| Color | `#163300` or semantic content |
| Decoration | underline only when it acts as a link |

### Cards & Containers

```html
<section class="mw-container wise-product-card">
  <h2>Send money globally for less</h2>
  <p>No hidden fees.</p>
</section>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Border | `inset 0 0 0 1px #C9CBCE` when framed |
| Radius | `10px` / `16px` / `24px` depending scale |
| Padding | `16px`, `24px`, or clamp-based marketing spacing |
| Shadow | none by default; elevated cards may use two-layer shadow |
| Hover | restrained color/border change; no bounce required |

### Navigation

```html
<nav class="NavigationDesktop_navigation_primary">
  <a>Personal</a>
  <a>Business</a>
  <a>Platform</a>
  <a class="signup-pill">Sign up</a>
</nav>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Link color | `#163300` |
| Link weight | `600` |
| Logo | left aligned, green-black |
| CTA | lime pill on the right |
| Transition | color/background/border only |

### Inputs & Forms

Currency selectors and transfer widgets use the same 48px control chassis as buttons.

```html
<label class="wise-input">
  <span>USD</span>
  <input value="1000" />
</label>
```

| Spec | Value |
|---|---|
| Height | `48px` |
| Padding | `12px 16px` |
| Border | `#C9CBCE` inset hairline or semantic border |
| Radius | `10px` or contextual control radius |
| Focus | 2-3px inset semantic ring |
| Error | `#E74848` / negative semantic ring |

### Hero Section

```html
<header class="wise-hero">
  <h1>Money for here, there and everywhere</h1>
  <p>160 countries and territories. 40 currencies.</p>
  <div class="mw-cta-set">
    <a class="primary-cta">Open an account</a>
    <a class="text-link">Send money now</a>
  </div>
</header>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| H1 | Wise Sans, 900, uppercase, centered |
| H1 color | `#0E0F0C` |
| Body | Inter 400, muted dark gray/green |
| CTA group | centered flex wrap |
| Secondary CTA | underlined text link, not an outline button |
| Media | concrete money/world/app imagery below copy |

### 13-2. Named Variants

- **button-primary-lime** - `#9FE870` background, `#163300` text, 9999px pill, 48px height. Use for Sign up and Open an account.
- **button-primary-lime-hover** - `#80E142` background, same ink text. Use only as interactive state, not a separate brand color.
- **button-primary-lime-active** - `#65CF21` background, same ink text. Pressed state only.
- **button-accent-blue-legacy** - `#00A2DD` background, `#FFFFFF` text, legacy `3px` radius. Use for older transfer/product widgets where CSS already exposes `.btn-accent`.
- **button-secondary-hairline** - white background with `#C9CBCE` inset ring. Use for utility secondary actions, never as the main homepage action.
- **nav-signup-pill** - compact lime pill in desktop nav, same color logic as primary CTA but smaller visual weight.
- **currency-control** - 48px form/select chassis with 12px/16px padding and semantic focus/error rings.

### 13-3. Signature Micro-Specs

#### display-billboard-softened-by-pill

```yaml
display-billboard-softened-by-pill:
  description: "Wise turns a financial promise into an oversized all-caps billboard, then softens the risk with a friendly lime pill."
  technique: "Wise Sans at weight 900, letter-spacing 0, centered hero text; CTA pill at #9FE870 background + #163300 ink, radius 9999px."
  applied_to: ["{component.hero-headline}", "{components.button-primary}", "account-opening CTA"]
  visual_signature: "loud confidence without corporate coldness — the headline shouts, the action smiles."
  intent: "fintech must signal both credibility (huge type) and approachability (warm pill); separating them across two elements is the trick."
```

#### dual-action-color-system

```yaml
dual-action-color-system:
  description: "Two parallel action ramps coexist: legacy blue (utility transfers) and modern lime (brand entry)."
  technique: "legacy .btn-accent uses #00A2DD / #008FC9 / #0081BA; modern homepage CTA uses #9FE870 / #80E142 / #65CF21; same DOM, different layer."
  applied_to: ["{components.button-accent-legacy}", "{components.button-primary-modern}", "transfer widget vs hero CTA"]
  visual_signature: "Wise reads as both a utility product and a friendly consumer brand on the same page — never one or the other."
  intent: "rebrands take years in financial product surfaces; codifying both ramps prevents accidental snap-back to legacy blue in the hero."
```

#### container-margin-ratcheting

```yaml
container-margin-ratcheting:
  description: "The page breathes by ratcheting side margins at fixed breakpoints while keeping a 1440px container."
  technique: ".mw-container margin steps from var(--mw-space-4) → 32px → 40px → 80px → 100px → auto at ≥1600px."
  applied_to: ["{component.marketing-section}", "{component.product-grid}", "page container"]
  visual_signature: "open hero on desktop, efficient product density below — the same container performs two moods."
  intent: "global money product needs to feel calm at the top and operational underneath; one container, two pacings."
```

#### inset-ring-control-depth

```yaml
inset-ring-control-depth:
  description: "Wise expresses control depth through inset rings, not outer chrome shadows."
  technique: "box-shadow: inset 0 0 0 1px #C9CBCE for default, inset 0 0 0 2px for hover, semantic 3px rings for validation states."
  applied_to: ["{components.button-secondary}", "{components.input-field}", "validation states"]
  visual_signature: "precise financial controls that feel etched rather than elevated — never floating."
  intent: "money handling demands trust; floating elevation suggests fragility, etched rings suggest commitment."
```

#### forest-green-as-financial-floor

```yaml
forest-green-as-financial-floor:
  description: "Body ink is a deep forest green (#163300), never neutral black — the brand's emotional grounding colour."
  technique: "color #163300 on body and headlines; this dark forest is also the CTA ink, creating a closed-loop palette with lime."
  applied_to: ["{typography.body}", "{typography.display}", "CTA pill ink"]
  visual_signature: "the page reads warm and organic — closer to a Patagonia annual report than a fintech dashboard."
  intent: "consumer fintech must distance itself from cold blue/grey banks; forest is the calmest 'not-corporate' ink available."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Plain promise, global scope, no jargon | "Money for here, there and everywhere" |
| Primary CTA | Direct account/action verb | "Open an account" |
| Secondary CTA | Utility action as text link | "Send money now" |
| Subheading | Numbers create trust and scope | "160 countries and territories. 40 currencies." |
| Tone | Direct, low-hype, consumer-finance clarity | "Never pay a hidden fee again" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Wise - copy into your root stylesheet */
:root {
  /* Fonts */
  --wise-font-family-display: "Wise Sans", "Inter", sans-serif;
  --wise-font-family-regular: "Inter", Helvetica, Arial, sans-serif;
  --wise-font-weight-regular: 400;
  --wise-font-weight-semi-bold: 600;
  --wise-font-weight-bold: 700;
  --wise-font-weight-black: 900;

  /* Brand/action */
  --wise-lime-300: #C5EDAB;
  --wise-lime-400: #9FE870;
  --wise-lime-500: #80E142;
  --wise-lime-600: #65CF21;
  --wise-ink: #163300;

  /* Secondary action ramp */
  --wise-blue-500: #00A2DD;
  --wise-blue-600: #008FC9;
  --wise-blue-700: #0081BA;

  /* Surfaces */
  --wise-bg-page: #FFFFFF;
  --wise-display-ink: #0E0F0C;
  --wise-text-primary: #37517E;
  --wise-text-muted: #5D7079;
  --wise-border: #C9CBCE;

  /* Key spacing */
  --wise-space-sm: 16px;
  --wise-space-md: 24px;
  --wise-space-lg: clamp(1.5rem, calc(1.41346rem + 0.38462vw), 1.875rem);

  /* Radius */
  --wise-radius-sm: 10px;
  --wise-radius-md: 16px;
  --wise-radius-lg: 24px;
  --wise-radius-pill: 9999px;
}

.wise-display {
  font-family: var(--wise-font-family-display);
  font-weight: var(--wise-font-weight-black);
  color: var(--wise-display-ink);
  letter-spacing: 0;
  line-height: .92;
  text-transform: uppercase;
}

.wise-primary-cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 48px;
  padding: 12px 24px;
  border-radius: var(--wise-radius-pill);
  background: var(--wise-lime-400);
  color: var(--wise-ink);
  font-family: var(--wise-font-family-regular);
  font-weight: var(--wise-font-weight-semi-bold);
  text-decoration: none;
}
.wise-primary-cta:hover { background: var(--wise-lime-500); }
.wise-primary-cta:active { background: var(--wise-lime-600); }
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js - Wise-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        wise: {
          lime: '#9FE870',
          limeHover: '#80E142',
          limeActive: '#65CF21',
          ink: '#163300',
          display: '#0E0F0C',
          blue: '#00A2DD',
          border: '#C9CBCE',
          muted: '#5D7079',
          surface: '#FFFFFF',
        },
      },
      fontFamily: {
        display: ['Wise Sans', 'Inter', 'sans-serif'],
        sans: ['Inter', 'Helvetica', 'Arial', 'sans-serif'],
      },
      fontWeight: {
        regular: '400',
        semibold: '600',
        bold: '700',
        black: '900',
      },
      borderRadius: {
        wiseSm: '10px',
        wiseMd: '16px',
        wiseLg: '24px',
        wisePill: '9999px',
      },
      boxShadow: {
        wiseRing: 'inset 0 0 0 1px #C9CBCE',
        wiseCard: '0 10px 32px 0 rgba(0,0,0,.15), 0 40px 40px 0 rgba(0,0,0,.04)',
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
| Brand primary | `{colors.primary}` | `#9FE870` |
| Background | `{colors.surface}` | `#FFFFFF` |
| Display text | `{colors.display-ink}` | `#0E0F0C` |
| Action ink | `{colors.ink}` | `#163300` |
| Text muted | `{colors.content-secondary}` | `#5D7079` |
| Border | `{colors.border}` | `#C9CBCE` |
| Legacy accent | `{colors.accent-blue}` | `#00A2DD` |
| Error | `{colors.negative}` | `#E74848` |

### Example Component Prompts

#### Hero Section

```text
Wise 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: Wise Sans, 96-120px clamp, weight 900, uppercase, tracking 0, color #0E0F0C
- 서브텍스트: Inter 20px, color #5D7079, max-width 600px, centered
- CTA 버튼: background #9FE870, text #163300, radius 9999px, min-height 48px, padding 12px 24px
- 보조 액션: outline button이 아니라 underlined text link
- 최대 너비: 1440px container, desktop side margin 80-100px
```

#### Card Component

```text
Wise 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF
- border: inset 0 0 0 1px #C9CBCE
- radius: 16px 또는 24px
- padding: 24px 이상
- shadow: 기본 none, 강조 카드만 0 10px 32px rgba(0,0,0,.15) + 0 40px 40px rgba(0,0,0,.04)
- 제목: Wise Sans 또는 Inter, weight 700/900 depending scale
- 본문: Inter 16px, color #37517E 또는 #5D7079
```

#### Badge

```text
Wise 스타일 utility label을 만들어줘.
- font: Inter, 14px, weight 600
- color: #163300
- background chip을 남발하지 말고 텍스트/underline 중심
- 상태나 경고가 필요할 때만 #FFD11A, #E74848 같은 semantic color 사용
```

#### Navigation

```text
Wise 스타일 상단 네비게이션을 만들어줘.
- 배경: #FFFFFF
- 로고 좌측, product nav는 Personal / Business / Platform
- 링크: Inter 16px, weight 600, color #163300
- 우측: language, Help, Log in, Sign up
- Sign up은 #9FE870 pill, text #163300, radius 9999px
- hover는 color/background/border만 바꾸고 transform은 쓰지 마
```

### Iteration Guide

- **색상 변경 시**: `#9FE870` primary CTA와 `#163300` text pairing을 함께 유지한다.
- **폰트 변경 시**: display와 body를 분리한다. display substitute를 body까지 확장하지 않는다.
- **여백 조정 시**: hero는 넓게, product/control 영역은 조밀하게. 전체를 같은 spacing scale로 평평하게 만들지 않는다.
- **새 컴포넌트 추가 시**: secondary controls에는 outer shadow보다 `#C9CBCE` inset ring을 우선한다.
- **다크/colored section**: lime and teal tokens may invert contextually; static homepage analysis did not prove a complete dark theme map.
- **반응형**: 576/768/992/1200/1440 breakpoints and 48px control height are the safest anchors.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #9FE870 for the primary homepage/account CTA and pair it with #163300 text.
- Keep the hero background #FFFFFF and let typography carry the impact.
- Use "Wise Sans" at 900 for huge display moments; use Inter 400/600 for readable product copy.
- Keep secondary actions as underlined text links when they sit beside the primary hero CTA.
- Use 48px as the default button/input chassis.
- Use `9999px` pill radius for modern lime CTAs and sign-up pills.
- Use inset rings like `inset 0 0 0 1px #C9CBCE` for secondary controls.
- Keep motion small: color/background transitions, simple fade/drop, carousel controls.

### ❌ DON'T

- 배경을 `#F5F5F7` 또는 gray app chrome으로 두지 말 것 — Wise homepage는 `#FFFFFF` surface를 사용.
- Hero headline을 `#000000` pure black으로 두지 말 것 — 대신 `#0E0F0C` 사용.
- Primary CTA를 `#00A2DD` 파란 버튼으로 만들지 말 것 — homepage account action은 `#9FE870` 사용.
- Lime CTA 텍스트를 `#FFFFFF`로 두지 말 것 — 대신 `#163300` 사용.
- Body text를 `#000000`으로 두지 말 것 — semantic content는 `#37517E`, `#5D7079`, 또는 contextual `#163300` 사용.
- Secondary border를 `#E5E7EB` generic gray로 두지 말 것 — 대신 `#C9CBCE` 사용.
- Hero를 보라 그라디언트 `#667EEA` / `#764BA2`로 장식하지 말 것 — Wise hero는 solid `#FFFFFF`.
- 모든 버튼을 8px radius로 통일하지 말 것 — modern CTA는 `9999px`, legacy blue controls may be `3px`.
- Hero H1을 56px SaaS heading으로 축소하지 말 것 — Wise identity requires oversized 96-120px display scale on desktop.
- Display에 negative tracking을 넣지 말 것 — Wise captured CSS/visual identity uses `letter-spacing: 0`.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No purple SaaS gradient** - no `#667EEA` to `#764BA2` style hero background.
- **No second homepage brand color** - blue exists, but the remembered hero action is lime.
- **No pure black hero ink** - display is green-black #0E0F0C, not generic #000000.
- **No white text on lime CTA** - the button remains readable and branded through #163300.
- **No decorative card confetti** - the page uses concrete money/currency/app imagery instead.
- **No universal rounded-card aesthetic** - pills, 3px legacy buttons, 10px controls, and 24px cards coexist.
- **No heavy chrome shadow on nav** - navigation is flat, white, and text-led.
- **No ultra-light body copy** - Inter 400 is the readable floor; financial copy should not become thin.
- **No abstract dashboard framing in the hero** - product utility appears through transfer/account/app affordances, not generic analytics cards.
- Decorative dashboard widget grid as a hero substitute: absent. One switch beats one panel.
- Multi-tool combo CTA stack (compare, learn more, sign up, try): never. The hero hands the user one button.
- Skeuomorphic switch chrome / illustrated dial knobs: zero. The tool is flat green ink on white paper.
- Branded background pattern around the entry door: none.
- Loading-state spinner inside the primary lime button: absent. The tool is silent until pressed.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single desktop homepage screenshot** - visual interpretation is anchored to `hero-cropped.png` at 1280x800. Mobile rendering was inferred from CSS breakpoints, not visually inspected in this run.
- **Existing phase1 data reused** - fetched assets are dated 2026-04-14. Wise may have changed after that date; this file reflects the provided local capture, not a fresh live crawl.
- **Contextual token duplication** - `--color-content-primary` and `--color-interactive-accent` appear with different resolved values across theme contexts. The guide separates homepage lime from legacy blue, but full theme matrix was not exhaustively mapped.
- **Navigation mobile behavior not proven** - desktop nav classes and breakpoints were observed, but hamburger/open panel states were not interacted with.
- **Form validation and loading states incomplete** - negative/focus rings exist in CSS, but actual checkout/send-money subflows were not visited.
- **Motion JavaScript not audited** - CSS durations and simple motion class names were captured; IntersectionObserver or app-specific animation orchestration was not analyzed.
- **Image treatment partially observed** - hero/world/coin imagery was seen in screenshot, but asset pipeline, object-fit rules, and responsive crops were not fully traced.
- **Official design-system documentation not consulted** - level is classified as `lv2` from production CSS evidence, not from a public Wise DS guidebook.
