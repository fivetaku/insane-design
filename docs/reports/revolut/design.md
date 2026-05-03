---
schema_version: 3.2
slug: revolut
service_name: Revolut
site_url: https://www.revolut.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: light
brand_color: "#4F55F1"
primary_font: "Aeonik Pro"
font_weight_normal: 400
token_prefix: rui

bold_direction: "Friendly Fintech"
aesthetic_category: "refined-saas"
signature_element: "hero_impact"
code_complexity: "high"

medium: web
medium_confidence: high
archetype: landing-utility
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "RUI CSS variables found: 237 total, 161 resolved, with color/font/spacing/radius/motion tokens and component aliases."

colors:
  primary: "#4F55F1"
  action-blue: "#EDEEFD"
  surface-base: "#FFFFFF"
  surface-grouped: "#F7F7F7"
  text-primary: "#191C1F"
  text-muted: "#717173"
  border-soft: "#EBEBF0"
  success: "#00B88B"
  danger: "#EE4A59"
typography:
  display: "Aeonik Pro"
  body: "Inter"
  ladder:
    - { token: marketing-display1, size: "3.5rem", weight: 900, line_height: "1", tracking: "calc(0.005em / 56)" }
    - { token: marketing-display2, size: "2.5rem", weight: 900, line_height: "1", tracking: "calc(0.005em / 40)" }
    - { token: heading1, size: "2rem", weight: 700, line_height: "1.1875", tracking: "calc(-0.35em / 32)" }
    - { token: body1, size: "1rem", weight: 400, line_height: "1.375", tracking: "calc(-0.18em / 16)" }
  weights_used: [400, 500, 600, 700, 800, 900]
  weights_absent: [300]
components:
  button-primary-pill: { bg: "#191C1F", color: "#FFFFFF", radius: "9999px", height: "3.25rem" }
  button-signup-pill: { bg: "#FFFFFF", color: "#191C1F", radius: "9999px", height: "2.5rem" }
  cookie-card: { bg: "#FFFFFF", color: "#191C1F", radius: "1.5rem", shadow: "level4" }
  hero-account-outline: { border: "2px solid #C9C9CD", radius: "1.5rem" }
---

# DESIGN.md — Revolut (Designer Guidebook)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Revolut presents finance as a lifestyle utility, not as a bank branch translated to the web. The first screen is built like a fashion-fintech billboard: a large human portrait, a blue-sky photographic field, and an oversized headline that sits over the image instead of being boxed away from it. The product is not explained through dashboards first; it is staged as a personal freedom object.

The system underneath is more disciplined than the hero image suggests. It works like a passport-control desk hidden inside a lifestyle poster: the surface says travel, freedom, and speed, while every button height, radius, and color alias has already been measured by RUI. `--rui-color-accent` at #4F55F1 (`{colors.primary}`), neutral surfaces from #FFFFFF (`{colors.surface-base}`) to #F7F7F7 (`{colors.surface-grouped}`), pill radii, compact spacing, and a full typography ladder keep the emotional hero from becoming loose advertising.

The visual signature is the collision of two shapes: enormous confident type and soft rounded controls. The headline behaves like airport-terminal signage scaled up for a phone-native bank: short, loud, and built to be read while moving. Around it, the interface pieces become boarding-pass fragments: dark pill CTA, white signup capsule, pale account chip, and a rounded account outline that sits over the human image like a transparent card wallet.

This is not a bank lobby and not a spreadsheet cockpit. There is no mahogany, no compliance-grey fortress, and no decorative fintech gradient trying to do the work of brand. Photography is the sky; #191C1F (`{colors.text-primary}`) is the ink; #FFFFFF (`{colors.surface-base}`) is the app shell; #4F55F1 (`{colors.primary}`) is the product-system signal, not a paint bucket for the whole page.

Do not flatten Revolut into generic blue SaaS. Blue exists, but it is often a tokenized action color or photographic atmosphere. The brand system is multi-accent: #4F55F1, #0666EB, #00B88B, #EA035D, and #EE4A59 appear as structured RUI colors. Think of it less as "one brand color everywhere" and more as a travel wallet with several stamped currencies: each accent has a role, but the first viewport still spends only one action at a time.

The page has very little site self-consciousness. It does not stop to show a grid of features before the emotional contract is made; it lets the photograph carry the weather, then drops product-grade controls on top. Revolut's craft is exactly that join: a billboard that has app hardware underneath it.

### Key Characteristics

- Human-led hero with oversized headline layered over photography.
- Primary interactive language uses pill buttons with `--rui-radius-round: 9999px`.
- RUI token namespace is preserved; use `--rui-*`, not invented generic aliases.
- Marketing display typography uses `Aeonik Pro`; product/body copy uses `Inter`.
- Neutral structure is soft: #FFFFFF, #F7F7F7, #EBEBF0, and #C9C9CD carry most chrome.
- Brand accent #4F55F1 is vivid but not spread across every section.
- Button heights are explicit product sizes: 1.875rem, 2.5rem, and 3.25rem.
- Motion has a named curve: `cubic-bezier(0.15, 0.5, 0.5, 1)` for default transitions.
- Shadows exist as tokenized elevation, not arbitrary card glow.
- The marketing screen allows photography to do what gradients would normally do.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Friendly Fintech
> **Aesthetic Category**: refined-saas
> **Signature Element**: 이 사이트는 **human billboard fintech hero**으로 기억된다.
> **Code Complexity**: high — tokenized RUI system plus photographic hero, pill controls, motion tokens, and multi-accent state colors.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Revolut처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}
.marketing-headline {
  font-family: "Aeonik Pro", "Inter", sans-serif;
  font-weight: 900;
  letter-spacing: calc(0.005em / 56);
  line-height: 1;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #FFFFFF;
  --fg: #191C1F;
  --surface: #F7F7F7;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드/액션 컬러 + pill controls */
:root {
  --brand: #4F55F1;
  --action-bg: #EDEEFD;
  --radius-pill: 9999px;
}
.button { border-radius: var(--radius-pill); min-height: 3.25rem; }
```

**절대 하지 말아야 할 것 하나**: Revolut을 flat dashboard SaaS처럼 만들지 말 것. 첫 화면은 product UI가 아니라 human-led billboard여야 한다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.revolut.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | existing phase1 reuse; HTML, inline CSS, screenshot |
| HTML size | 875238 bytes |
| CSS files | 1 inline CSS, 805869 chars |
| Token prefix | `rui` |
| Method | CSS custom properties parsed from existing phase1 JSON; visual interpretation from `hero-cropped.png` |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React / styled-components-like generated classes inferred from class names such as `Box-rui__sc-*`, `Text-rui__sc-*`, and `Navigation__*`.
- **Design system**: RUI — prefix `--rui-*`.
- **CSS architecture**:
  ```css
  --rui-color-*        raw and semantic color values
  --rui-font-*         family, size, weight, line-height, tracking
  --rui-space-*        spacing ladder
  --rui-radius-*       radius ladder and component aliases
  --rui-duration-*     motion duration
  --rui-easing-*       motion curves
  --rui-shadow-*       elevation tokens
  ```
- **Class naming**: generated component classes with RUI component prefixes, for example `Navigation__NavigationBase-*` and `Text-rui__sc-*`.
- **Default theme**: light in document attribute (`data-theme="light"`), with dark token counterparts present in CSS.
- **Font loading**: embedded `@font-face` data URLs for Inter; marketing font token points to `Aeonik Pro`.
- **Canonical anchor**: the homepage hero and navigation screenshot, plus RUI tokens extracted from inline CSS.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Aeonik Pro` (commercial/proprietary marketing font)
- **Body font**: `Inter` plus system fallbacks
- **Code font**: not surfaced in collected homepage CSS
- **Weight normal / bold**: `400` / `700`; marketing display reaches `900`

```css
:root {
  --rui-font-default: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto",
    "Helvetica Neue", Helvetica, Arial, Arimo, sans-serif;
  --rui-font-system: var(--rui-font-default);
  --rui-font-brand: "Inter", var(--rui-font-system);
  --rui-font-marketing: "Aeonik Pro", var(--rui-font-system);
  --rui-font-weight-body1: 400;
  --rui-font-weight-heading1: 700;
  --rui-font-weight-marketing-display1: 900;
}
```

### Note on Font Substitutes

- **Aeonik Pro** — use **Inter Display** or **Satoshi** as a practical substitute at weight 900 for the billboard headline. Keep line-height at `1`; loosening to 1.1 makes the hero feel more like ordinary SaaS.
- **Inter body** — use real Inter where possible. If using system UI, keep `font-weight: 400` for body and reserve 500/700 for emphasis; do not make every paragraph medium.
- **Tracking correction** — preserve the token pattern: large marketing display uses tiny positive tracking `calc(0.005em / 56)`, while product display and headings use negative tracking such as `calc(-0.56em / 56)`.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---|
| `--rui-font-size-marketing-display1` | 3.5rem | 900 | 1 | `calc(0.005em / 56)` |
| `--rui-font-size-marketing-display2` | 2.5rem | 900 | 1 | `calc(0.005em / 40)` |
| `--rui-font-size-marketing-display3` | 2rem | 900 | 1 | `calc(0.005em / 32)` |
| `--rui-font-size-display1` | 3.5rem | 700/800 | 1.2857 or 1.1818 | `calc(-0.56em / 56)` |
| `--rui-font-size-display2` | 2.75rem | 700/800 | N/A | `calc(-0.56em / 44)` |
| `--rui-font-size-heading1` | 2rem | 700/800 | 1.1875 | `calc(-0.35em / 32)` |
| `--rui-font-size-heading2` | 1.5rem | 700/800 | 1.25 | `calc(-0.31em / 24)` |
| `--rui-font-size-heading3` | 1.25rem | 700/800 | 1.4 | `calc(-0.27em / 20)` |
| `--rui-font-size-body1` | 1rem | 400/500 | 1.375 | `calc(-0.18em / 16)` |
| `--rui-font-size-body2` | 0.875rem | 400/500 | 1.4286 | `calc(-0.1em / 14)` |
| `--rui-font-size-body3` | 0.75rem | 400/500 | 1.5 | `0` |

> Key insight: Revolut separates marketing confidence from product density. Marketing display goes to weight 900 with line-height 1; product copy remains more controlled with 400/500 body weights.

### Principles

1. Marketing display is not just bigger; it is a different voice: `Aeonik Pro`, weight 900, line-height 1.
2. Body copy should stay calm at 400. Raising every paragraph to 500 makes the interface feel like a crypto dashboard rather than a consumer banking app.
3. Heading and display tokens use optical tracking corrections. Preserve the negative product tracking and the slight positive marketing display tracking.
4. Revolut tolerates very large hero type because photography sits behind it; do not apply the same scale inside dense cards.
5. Weight 300 is absent from the extracted RUI system. The brand is friendly but not lightweight.
6. Small text remains functional: 0.875rem and 0.75rem sizes are present for product/UI copy, not for decorative captions.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp / Accent Anchors

| Token | Hex |
|---|---|
| `--rui-color-accent` | #4F55F1 |
| `--rui-color-blue` | #4F55F1 |
| `--rui-color-action-photo-header-text` | #4F55F1 |
| `--rui-color-action-blue` | #EDEEFD |
| `--rui-color-action-background` | #EDEEFD |

### 06-2. Dark / Alternate Accent Variants

| Token | Hex |
|---|---|
| `--rui-color-background` dark counterpart | #111112 |
| `--rui-color-foreground` dark counterpart | #F4F4F4 |
| `--rui-color-accent` alternate | #667DFF |
| `--rui-color-action-background` alternate | #1C1D34 |
| `--rui-color-action-photo-header-background` alternate | #667DFF |

### 06-3. Neutral Ramp

| Step | Light | Dark / tone |
|---|---|---|
| White | #FFFFFF | #F4F4F4 |
| Grey 2 | #F7F7F7 | #111112 |
| Grey 5 | #F1F2F4 | #19191A |
| Grey 8 | #EBEBF0 | #1C1C1E |
| Grey 10 | #E2E2E7 | #3B3B3D |
| Grey 20 | #C9C9CD | #525254 |
| Grey 50 | #717173 | #818C96 |
| Black | #191C1F | #191C1F |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Blue | `--rui-color-blue` | #4F55F1 |
| Action blue | `--rui-color-action-photo-header-text` | #0666EB |
| Teal / success | `--rui-color-teal` | #00B88B |
| Green | `--rui-color-green` | #30D158 |
| Pink | `--rui-color-deep-pink` | #EA035D |
| Danger | `--rui-color-danger` | #EE4A59 |
| Orange | `--rui-color-orange` | #DD7904 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--rui-color-background` | #FFFFFF | page and app surface |
| `--rui-color-foreground` | #191C1F | primary foreground in light mode |
| `--rui-color-grouped-background` | #F7F7F7 | grouped app surfaces |
| `--rui-color-popover-background` | #FFFFFF | popovers and cookie card surfaces |
| `--rui-color-search-background` | #EBEBF0 | search/segmented control backing |
| `--rui-color-on-accent` | #FFFFFF | text on accent fills |
| `--rui-color-danger` | #EE4A59 | destructive/error semantics |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--rui-color-action-background` | #EDEEFD | pale action surface |
| `--rui-color-action-label` | #FFFFFF | action label on colored fill |
| `--rui-color-action-photo-header-background` | #EDEEFD | photo-header action background |
| `--rui-color-action-photo-header-text` | #4F55F1 | text/action over photo header |
| `--rui-color-input-error` | #330E0C | dark error input state |
| `--rui-color-popover-background` | #3B3B3D / #FFFFFF | theme-dependent popover surface |
| `--rui-color-swipeable-card-background` | #1C1C1E | dark swipeable card surface |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Hex | Frequency | Kind |
|---|---:|---|
| #FFFFFF | 72 | neutral |
| #F4F4F4 | 20 | neutral |
| #F7F7F7 | 18 | neutral |
| #E23B4A | 14 | chromatic |
| #EE4A59 | 14 | chromatic |
| #13D1A3 | 12 | chromatic |
| #00B88B | 10 | chromatic |
| #0666EB | 10 | chromatic |
| #191C1F | 10 | neutral/ink |
| #1AC097 | 10 | chromatic |

### Color Stories

**`{colors.primary}` (#4F55F1)** — Revolut's clean product accent. It is used as `--rui-color-accent`, `--rui-color-blue`, and photo-header text in the light token set. Treat it as the product-system anchor, not as a page-wide wash.

**`{colors.surface-base}` (#FFFFFF)** — The functional surface. Cookie panels, popovers, and light-mode product UI rely on this white base so the hero photography and black pills can carry contrast.

**`{colors.text-primary}` (#191C1F)** — Near-black rather than pure #000000. It keeps the interface softer and more app-native, especially in body copy and dark primary pills.

**`{colors.border-soft}` (#EBEBF0)** — Revolut's quiet divider color. It appears in search/segmented backing and should be used for pale UI separation instead of heavy strokes.

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---:|---|
| `--rui-space-none` | 0 | reset |
| `--rui-space-s2` | 0.125rem | hairline gaps |
| `--rui-space-s4` | 0.25rem | tight icon/text gaps |
| `--rui-space-s6` | 0.375rem | compact control internals |
| `--rui-space-s8` | 0.5rem | small gaps |
| `--rui-space-s12` | 0.75rem | button horizontal rhythm |
| `--rui-space-s16` | 1rem | default component padding |
| `--rui-space-s20` | 1.25rem | medium gaps |
| `--rui-space-s24` | 1.5rem | cards and modal internals |
| `--rui-space-s32` | 2rem | section groups |
| `--rui-space-s40` | 2.5rem | large stack spacing |
| `--rui-space-s48` | 3rem | hero content rhythm |
| `--rui-space-s56` | 3.5rem | large layout rhythm |
| `--rui-space-s64` | 4rem | major section air |
| `--rui-space-s72` | 4.5rem | largest extracted spacing |

**주요 alias**:
- `--rui-size-layout` -> 94.375rem (wide layout container)
- `--rui-size-layout-menu-lg` -> 6.5rem (menu layout sizing)
- `--rui-size-layout-side-wide` -> 36.5rem (wide side panel)

### Whitespace Philosophy

Revolut uses product-system spacing for controls but billboard spacing for the hero. Buttons and cookie controls are compact and highly measured, while the hero lets large empty photographic areas frame the headline. This contrast is the point: precise app UI floating over lifestyle imagery.

The spacing scale is not an arbitrary 8px-only ladder; it includes small product increments (`s2`, `s4`, `s6`) and large section values up to `s72`. Use small tokens inside controls and reserve `s48` to `s72` for page-level breathing room.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `--rui-radius-none` | unset | no rounding |
| `--rui-radius-r2` | 0.125rem | tiny UI details |
| `--rui-radius-r4` | 0.25rem | small chips |
| `--rui-radius-r6` | 0.375rem | compact controls |
| `--rui-radius-r8` | 0.5rem | standard small cards |
| `--rui-radius-r12` | 0.75rem | medium cards |
| `--rui-radius-r16` | 1rem | widget radius |
| `--rui-radius-r24` | 1.5rem | popups and large cards |
| `--rui-radius-r32` | 2rem | extra-large surfaces |
| `--rui-radius-round` | 9999px | pill buttons |
| `--rui-radius-widget` | `var(--rui-radius-r16)` | widget surfaces |
| `--rui-radius-popup` | `var(--rui-radius-r24)` | cookie/modal surfaces |
| `--rui-radius-app` | 25% | app icon style |
| `--rui-radius-status-popup` | 2.75rem | status popup |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `--rui-size-layout: 94.375rem`.
- **Grid type**: flex/component layout in generated classes; hero visually behaves like layered absolute/flex composition.
- **Column count**: homepage hero is not a conventional 12-column grid; it is an image-led composition with left text and central product/person framing.
- **Gutter**: use RUI spacing tokens; `s24`/`s32` for component gaps and `s48`+ for section air.

### Hero

- **Pattern Summary**: viewport hero + photographic background + oversized left headline + pill CTA + product/account frame.
- Layout: navigation at top, headline and copy left, human figure center/right, product frame overlay around the person.
- Background: photography/video-like hero, not CSS gradient as the primary atmosphere.
- **Background Treatment**: image overlay with darkened/blue photographic field; no tokenized gradient identified for the hero itself.
- H1: marketing display; visually far larger than token `3.5rem` on desktop screenshot, use `clamp(4rem, 7vw, 5.5rem)` if recreating.
- Max-width: wide page composition around `94.375rem`.

### Section Rhythm

```css
section {
  padding-block: var(--rui-space-s64);
  padding-inline: var(--rui-space-s24);
  max-width: var(--rui-size-layout);
}
```

### Card Patterns

- **Card background**: #FFFFFF for cookie/popover, #F7F7F7 for grouped panels, dark #1C1C1E for swipeable dark cards.
- **Card border**: pale #EBEBF0 or #C9C9CD when visible; hero account frame uses a thin pale outline.
- **Card radius**: `--rui-radius-r24` for popups; `--rui-radius-r16` for widgets.
- **Card padding**: typically `--rui-space-s24` or larger for modal-like surfaces.
- **Card shadow**: tokenized `--rui-shadow-level4` for high floating surfaces; avoid arbitrary blur.

### Navigation Structure

- **Type**: horizontal desktop nav.
- **Position**: top overlay/static at hero top in screenshot.
- **Height**: visually compact; use around 4rem to 5rem.
- **Background**: transparent over hero image in the captured first viewport.
- **Border**: none visible in hero state.
- **Links**: muted light text over photography; `Log in` and `Sign up` sit right.

### Content Width

- **Prose max-width**: about 32rem for hero body copy.
- **Container max-width**: 94.375rem from `--rui-size-layout`.
- **Sidebar width**: no sidebar on homepage hero; side layout tokens exist up to 36.5rem.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<button class="rui-button rui-button--primary">Download the app</button>
<button class="rui-button rui-button--light">Sign up</button>
```

| Property | Primary dark pill | Light signup pill |
|---|---|---|
| Background | #191C1F | #FFFFFF |
| Text | #FFFFFF | #191C1F |
| Radius | `--rui-radius-round` / 9999px | 9999px |
| Height | `--rui-size-button-md` / 3.25rem | `--rui-size-button-sm` / 2.5rem |
| Padding | `s16` to `s24` horizontal | `s16` to `s24` horizontal |
| Hover | subtle opacity/background shift | subtle neutral shift |
| Focus | use visible outline; exact token not surfaced | use visible outline |
| Disabled | `--rui-color-button-disabled-text` exists | same semantic token |

### Badges

Revolut's captured hero uses capsule-like labels rather than decorative badges. The account selector inside the product frame reads as a pale rounded chip.

| Property | Account chip |
|---|---|
| Background | #C9C9CD or light neutral treatment |
| Text | #191C1F |
| Radius | 9999px |
| Weight | 400/500 |
| Height | compact, around button-xs to button-sm |

### Cards & Containers

```html
<aside class="rui-cookie-card">
  <h2>Choose your cookies</h2>
  <button>Accept all</button>
  <button>Reject non-essential cookies</button>
</aside>
```

| Property | Cookie / popup card |
|---|---|
| Background | #FFFFFF |
| Text | #191C1F |
| Radius | `--rui-radius-popup` / 1.5rem |
| Padding | 1.5rem to 2rem |
| Shadow | `--rui-shadow-level4` |
| Buttons | stacked pills; primary dark fill, secondary outline |
| Error/loading | not observed in homepage capture |

### Navigation

```html
<header class="rui-nav">
  <a class="rui-logo">Revolut</a>
  <nav>
    <a>Personal</a>
    <a>Business</a>
    <a>Kids & Teens</a>
    <a>Company</a>
  </nav>
  <a>Log in</a>
  <button>Sign up</button>
</header>
```

| Property | Value |
|---|---|
| Structure | logo left, primary nav middle, account actions right |
| Background | transparent over hero |
| Link color | light/muted over photography |
| Active state | not surfaced |
| Mobile menu | not observed; do not invent exact drawer specs |

### Inputs & Forms

No full form surface was visible in the captured homepage hero. RUI exposes error aliases such as `--rui-color-input-error` #330E0C and `--rui-color-input-error-focus` #421210, so form states exist in the system, but the homepage capture does not prove field dimensions or validation choreography.

### Hero Section

```html
<section class="revolut-hero">
  <h1>Banking & Beyond</h1>
  <p>This is your bank, redefined...</p>
  <button>Download the app</button>
  <div class="hero-account-frame">...</div>
</section>
```

| Property | Value |
|---|---|
| Background | photographic blue field with human subject |
| H1 | massive Aeonik Pro, weight 900, line-height 1 |
| Copy | compact, muted light text over image |
| CTA | dark pill, white text |
| Product frame | rounded rectangle outline over portrait |
| Composition | image and product promise fused, not separated into text/media columns |

### 13-2. Named Variants

- **button-primary-pill** — dark fill #191C1F, text #FFFFFF, radius 9999px, used for "Download the app" and cookie "Accept all".
- **button-secondary-outline-pill** — transparent/#FFFFFF surface, #191C1F text, 1px to 2px dark outline, radius 9999px, used for cookie rejection action.
- **button-light-signup-pill** — light surface #FFFFFF over hero image, dark text, compact height around 2.5rem.
- **hero-account-frame** — large rounded outline over photography, pale border around the account promise.
- **cookie-popup-card** — white floating surface, 1.5rem radius, dark/outline stacked actions.

### 13-3. Signature Micro-Specs

```yaml
human-billboard-account-overlay:
  description: "Lifestyle photography and product promise occupy the same plane instead of a split text/media layout."
  technique: "full-bleed photographic hero + oversized Aeonik Pro headline, weight 900, line-height 1, with a rounded account frame overlay using 2px #C9C9CD and radius 1.5rem"
  applied_to: ["{component.hero-section}", "{component.hero-account-frame}"]
  visual_signature: "A human fintech billboard with a transparent card-wallet outline sitting directly over the portrait."

rui-pill-control-system:
  description: "Every decisive action resolves into a capsule, from hero CTA to signup and cookie actions."
  technique: "--rui-radius-round: 9999px; explicit button heights 1.875rem, 2.5rem, and 3.25rem; horizontal padding from --rui-space-s16 to --rui-space-s24"
  applied_to: ["{component.button-primary-pill}", "{component.button-signup-pill}", "{component.cookie-card}"]
  visual_signature: "Controls feel like app-native payment buttons rather than SaaS rectangles."

aeonik-inter-tracking-split:
  description: "Marketing confidence and product density are separated through font family, weight, and optical tracking."
  technique: "marketing display: Aeonik Pro, weight 900, line-height 1, letter-spacing calc(0.005em / 56); product display/headings use negative corrections such as calc(-0.56em / 56) and calc(-0.35em / 32)"
  applied_to: ["{component.hero-section}", "{component.navigation}", "{component.cookie-card}"]
  visual_signature: "The hero reads like bold airport signage while UI copy stays compact and app-like."

tokenized-popup-elevation:
  description: "Floating consent and popup surfaces use system elevation, not decorative glow."
  technique: "--rui-radius-popup: 1.5rem with --rui-shadow-level4 equivalent 0 1rem 4rem rgb(var(--rui-color-channel-black) / 0.12) on #FFFFFF surfaces"
  applied_to: ["{component.cookie-card}", "{component.cookie-popup-card}"]
  visual_signature: "White cards hover softly over photography without becoming glossy fintech glass."

photo-header-action-accent:
  description: "Blue is constrained to action/header semantics rather than washed across the page."
  technique: "--rui-color-action-photo-header-text: #4F55F1 / #0666EB; --rui-color-action-background: #EDEEFD; base surfaces remain #FFFFFF and #F7F7F7"
  applied_to: ["{component.hero-section}", "{component.button-light-signup-pill}", "{component.account-chip}"]
  visual_signature: "A precise product-blue signal appears against neutral app chrome and photographic sky, never as a generic blue SaaS blanket."
```

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Revolut — copy into your root stylesheet */
:root {
  /* Fonts */
  --rui-font-default: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto",
    "Helvetica Neue", Helvetica, Arial, Arimo, sans-serif;
  --rui-font-brand: "Inter", var(--rui-font-default);
  --rui-font-marketing: "Aeonik Pro", var(--rui-font-default);
  --rui-font-weight-normal: 400;
  --rui-font-weight-bold: 700;
  --rui-font-weight-marketing-display: 900;

  /* Brand and action */
  --rui-color-brand-500: #4F55F1;
  --rui-color-action-blue: #EDEEFD;
  --rui-color-action-photo-header-text: #4F55F1;
  --rui-color-success: #00B88B;
  --rui-color-danger: #EE4A59;

  /* Surfaces */
  --rui-bg-page: #FFFFFF;
  --rui-bg-grouped: #F7F7F7;
  --rui-text: #191C1F;
  --rui-text-muted: #717173;
  --rui-border-soft: #EBEBF0;

  /* Spacing */
  --rui-space-sm: 0.5rem;
  --rui-space-md: 1rem;
  --rui-space-lg: 1.5rem;
  --rui-space-xl: 3rem;
  --rui-space-hero: 4rem;

  /* Radius */
  --rui-radius-sm: 0.5rem;
  --rui-radius-widget: 1rem;
  --rui-radius-popup: 1.5rem;
  --rui-radius-pill: 9999px;

  /* Motion */
  --rui-duration-sm: 200ms;
  --rui-duration-md: 300ms;
  --rui-easing-default: cubic-bezier(0.15, 0.5, 0.5, 1);
}

.revolut-hero {
  min-height: 100vh;
  color: #FFFFFF;
  background: #191C1F;
  position: relative;
  overflow: hidden;
}

.revolut-hero__title {
  font-family: var(--rui-font-marketing);
  font-weight: var(--rui-font-weight-marketing-display);
  font-size: clamp(4rem, 7vw, 5.5rem);
  line-height: 1;
  letter-spacing: calc(0.005em / 56);
}

.revolut-button {
  min-height: 3.25rem;
  padding: 0 1.5rem;
  border-radius: var(--rui-radius-pill);
  border: 0;
  font-family: var(--rui-font-brand);
  font-weight: 500;
  transition:
    background-color var(--rui-duration-sm) var(--rui-easing-default),
    color var(--rui-duration-sm) var(--rui-easing-default);
}

.revolut-button--primary {
  background: #191C1F;
  color: #FFFFFF;
}

.revolut-card {
  background: #FFFFFF;
  color: #191C1F;
  border-radius: var(--rui-radius-popup);
  box-shadow: 0 1rem 4rem rgb(25 28 31 / 0.12);
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `{colors.primary}` / `--rui-color-accent` | #4F55F1 |
| Background | `{colors.surface-base}` / `--rui-color-background` | #FFFFFF |
| Grouped background | `{colors.surface-grouped}` / `--rui-color-grouped-background` | #F7F7F7 |
| Text primary | `{colors.text-primary}` / `--rui-color-foreground` | #191C1F |
| Text muted | `{colors.text-muted}` / `--rui-color-grey-50` | #717173 |
| Border | `{colors.border-soft}` / `--rui-color-grey-8` | #EBEBF0 |
| Success | `--rui-color-teal` | #00B88B |
| Error | `--rui-color-danger` | #EE4A59 |

### Example Component Prompts

#### Hero Section

```text
Revolut 스타일 히어로 섹션을 만들어줘.
- 배경: human-led full-bleed photography, 토큰 그라디언트가 아니라 이미지 중심
- H1: Aeonik Pro, clamp(4rem, 7vw, 5.5rem), weight 900, line-height 1
- 서브텍스트: Inter, 1rem, color #FFFFFF with reduced opacity
- CTA 버튼: background #191C1F, text #FFFFFF, radius 9999px, min-height 3.25rem
- 구성: 좌측 copy, 중앙/우측 인물, rounded account frame overlay
```

#### Card Component

```text
Revolut 스타일 popup/card를 만들어줘.
- 배경 #FFFFFF, 텍스트 #191C1F
- radius 1.5rem, padding 1.5rem~2rem
- shadow: 0 1rem 4rem rgb(25 28 31 / 0.12)
- primary action은 dark pill, secondary action은 outline pill
- 장식 색은 최소화하고 neutral border #EBEBF0 사용
```

#### Badge / Chip

```text
Revolut 스타일 pill chip을 만들어줘.
- radius 9999px
- compact height: 1.875rem~2.5rem
- surface는 #EBEBF0 또는 #FFFFFF
- text는 #191C1F, weight 400/500
- brand color #4F55F1은 active/action 상태에만 제한적으로 사용
```

#### Navigation

```text
Revolut 스타일 상단 네비게이션을 만들어줘.
- logo left, Personal/Business/Kids & Teens/Company middle, Log in/Sign up right
- hero 위에서는 transparent background
- Sign up은 light pill, Log in은 plain text link
- links는 Inter 14~16px, weight 400/500
```

### Iteration Guide

- **색상 변경 시**: `--rui-color-*` 토큰을 먼저 보고 바꾼다. `#4F55F1`을 모든 카드 배경으로 번지는 방식은 금지.
- **폰트 변경 시**: hero만 marketing display로 크게 간다. 본문과 UI는 Inter 400/500으로 유지.
- **여백 조정 시**: control 내부는 `s8`~`s24`, section air는 `s48`~`s72`.
- **새 컴포넌트 추가 시**: radius는 먼저 `r16`, `r24`, `round` 중 하나를 고른다. 임의 10px radius를 만들지 않는다.
- **모션 추가 시**: 기본 curve `cubic-bezier(0.15, 0.5, 0.5, 1)`를 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `--rui-*` token names and preserve the RUI namespace.
- Lead with a photographic, human, high-confidence hero when recreating the marketing homepage.
- Use `Aeonik Pro` or a strong substitute for the huge marketing headline.
- Keep primary controls pill-shaped with `border-radius: 9999px`.
- Let neutral surfaces do most of the structural work: #FFFFFF, #F7F7F7, #EBEBF0, #C9C9CD.
- Use #4F55F1 as a precise product accent, not as a full-page blue wash.
- Use tokenized shadows for floating cards; `level4` is the high-elevation popup pattern.

### ❌ DON'T

- 배경 전체를 `#EDEEFD`로 두지 말 것 — 대신 base surface는 `#FFFFFF`, action surface만 `#EDEEFD` 사용.
- 본문 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#191C1F` 사용.
- primary CTA를 `#4F55F1` solid fill로 고정하지 말 것 — captured hero CTA는 dark pill `#191C1F` + `#FFFFFF` 조합이 핵심.
- neutral divider를 `#717173`처럼 텍스트용 grey로 대체하지 말 것 — 대신 `#EBEBF0` 또는 `#C9C9CD` 사용.
- grouped surface를 `#FFFFFF`만으로 평평하게 만들지 말 것 — grouped/app surfaces에는 `#F7F7F7` 사용.
- error/danger를 `#F12587` 같은 pink accent로 만들지 말 것 — 대신 RUI danger `#EE4A59` 사용.
- 버튼을 8px rounded rectangle로 만들지 말 것 — Revolut primary actions are pill controls with `9999px`.
- hero를 text-left/card-right SaaS split으로 만들지 말 것 — photography and product promise must overlap.
- body 전체에 `font-weight: 500`을 사용하지 말 것 — default body should remain 400, emphasis uses 500.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- No generic 12-column SaaS card wall in the first viewport; the homepage opens as a billboard.
- No decorative purple-blue gradient background as the primary hero device; photography carries atmosphere.
- No square primary buttons; pill radius is a defining control grammar.
- No pure black text default; #191C1F is the softer ink.
- No single-accent-only worldview; RUI contains blue, teal, pink, orange, danger, and neutral state families.
- No heavy chrome borders on cards; surface, radius, and tokenized shadow do the structural work.
- No lightweight 300 typography in the extracted system; Revolut prefers confident weights.
- No invented token aliases like `color-brand`; preserve `--rui-color-accent`, `--rui-color-action-background`, and the actual namespace.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Security-check HTML limitation** — the collected `index.html` title/content was a "Just a quick security check" page, not the full marketing DOM. Layout interpretation therefore relies on the existing `hero-cropped.png` plus RUI CSS tokens.
- **Screenshot has cookie overlay** — the captured first viewport includes a cookie dialog covering part of the right hero. Component analysis uses that dialog as a valid Revolut popup pattern, but some underlying hero details are obscured.
- **Hero image color is not tokenized** — the blue photographic atmosphere is visible in the screenshot but not represented as a CSS design token. This guide does not invent a hero-blue hex.
- **Responsive behavior not fully measured** — only existing desktop screenshot evidence was used. Mobile navigation, drawer behavior, and breakpoint-specific hero crops are not asserted as facts.
- **Form states are token-visible but not flow-visible** — input error tokens exist (#330E0C and #421210), but actual form markup and validation states were not observed in the homepage capture.
- **Motion logic not inspected in JS** — duration/easing CSS variables are present, but scroll-triggered or runtime animation behavior was not analyzed.
- **Dark theme mapping is partial** — dark/tone tokens appear in the CSS, but the public homepage capture is light. Do not assume a complete dark homepage spec from this file alone.
- **Exact hero typography size is visual-estimated** — RUI marketing tokens top out at 3.5rem, while the captured hero headline appears larger. The recommended clamp is a recreation estimate grounded in the screenshot, not a parsed CSS declaration.
