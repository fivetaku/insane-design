---
schema_version: 3.2
slug: mintlify
service_name: Mintlify
site_url: https://mintlify.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#0C8C5E"
primary_font: Inter
font_weight_normal: 400
token_prefix: color

bold_direction: Atmospheric Docs
aesthetic_category: Refined SaaS
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Tailwind v4 theme tokens, 253 custom properties, semantic color variables, and repeated component utility patterns are present, but no official public DS tier naming is exposed."

colors:
  brand: "#0C8C5E"
  brand-bright: "#18E299"
  surface-main: "#FFFFFF"
  ink-main: "#08090A"
  hero-accent: "#FF5A00"
  prose-heading: "#101828"
  prose-body: "#364153"
  border-gray: "#E5E7EB"
  dark-surface: "#151616"
typography:
  display: "Inter"
  body: "Inter"
  mono: "Geist Mono"
  ladder:
    - { token: hero-title, size: "max(2.5rem, min(4vw, 4rem))", weight: 600, line_height: "115%", tracking: "-0.02em" }
    - { token: text-lg, size: "1.125rem", weight: 400, line_height: "1.75/1.125", tracking: "0" }
    - { token: text-base, size: "1rem", weight: 400, line_height: "1.5", tracking: "0" }
    - { token: text-sm, size: ".875rem", weight: 500, line_height: "1.25/.875", tracking: "0" }
  weights_used: [100, 400, 500, 600, 700]
  weights_absent: [300, 800, 900]
components:
  button-primary-pill: { bg: "{colors.ink-main}", color: "{colors.surface-main}", radius: "9999px", padding: "4.5px 12px" }
  glass-email-capsule: { bg: "rgba(8,9,10,.15)", border: "rgba(8,9,10,.15)", blur: "12px", radius: "9999px" }
  feature-card-shadow: { shadow: "5-layer transparent-to-soft black stack", radius: "1.5rem" }
  hero-title: { size: "max(2.5rem, min(4vw, 4rem))", tracking: "-.02em", line_height: "115%" }
---

# DESIGN.md — Mintlify Designer Guidebook

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Mintlify's marketing surface is teal-sky canvas holding editorial documentation precision in a pill-and-panel grid. The homepage does not sell documentation with a dry docs-site visual language; it wraps a precise parchment-white product interface in a cinematic atmospheric field, making the knowledge base feel like infrastructure already running in the cloud layer. The hero uses atmosphere first and terminal proof second: the docs UI floats in front of a painterly teal sky like a cockpit window cut into the weather.

The system is built on a strong split identity. The marketing shell is illustrative and almost impressionistic, while the product chrome stays white, rounded, and exact. The canvas carries the emotion; the parchment UI card carries the proof. Below the hero, the page returns to clean SaaS structure: Inter-type surfaces, tight pill CTAs, green accent (#0C8C5E, `{colors.brand}`), and documentation-first information hierarchy.

The dominant functional color is #0C8C5E (`{colors.brand}`), but the remembered impression is broader: deep blue-green canvas atmosphere, pale cloud yellows, and a bright AI-era mint accent (#18E299, `{colors.brand-bright}`) inside brand contexts. #FF5A00 (`{colors.hero-accent}`) is a contained flare in gradient utility effects, not a second brand. The actual interface contract remains white surfaces, near-black ink, soft borders, and pill controls — the parchment register of a documentation surface, not a startup splash.

Typography is modern but not ornamental. Inter handles the page, Geist Mono handles developer-credibility moments that feel like a terminal receipt, and the hero headline gets the only aggressive optical correction: `letter-spacing: -.02em`, weight 600, line-height 115%. The glass email capsule works like an airlock between marketing canvas and product proof: `backdrop-blur-[12px]` softens the sky while the inner black pill keeps conversion grounded in #08090A (`{colors.ink-main}`). The editorial balance — atmospheric above, exact below — is the Mintlify signature.

### Key Characteristics

- Cinematic teal-to-blue hero atmosphere with painterly cloud imagery.
- Floating documentation product surface below the headline, with large rounded chassis.
- Pill navigation and CTA buttons using compact 15px text and `9999px` radius.
- Inter as primary face, Geist Mono as developer/code credibility face.
- Hero title uses `max(2.5rem, min(4vw, 4rem))`, `font-weight: 600`, `line-height: 115%`, `letter-spacing: -.02em`.
- Tailwind v4 token shape: `--spacing: .25rem`, `--color-*`, `--radius-*`, `--font-weight-*`, and utility-driven component classes.
- Brand green #0C8C5E is the UI accent; #18E299 is a brighter brand-light/AI glow counterpart.
- Shadows are multi-layer and low-alpha, especially on feature cards and navbar surfaces.
- Forms use translucent glass capsules: `backdrop-blur-[12px]`, soft border, and dark inner CTA.
- The page alternates emotional hero imagery with clean, documentation-like product proof.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Atmospheric Docs
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **teal sky hero with floating documentation chrome**으로 기억된다.
> **Code Complexity**: high — Tailwind v4 utilities, multi-layer shadows, atmospheric image treatment, conic/linear gradients, mask-image utilities, and glass form treatment are all present.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Mintlify처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter", "inter Fallback", -apple-system, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #FFFFFF;
  --fg: #08090A;
}
body {
  background: var(--bg);
  color: var(--fg);
}

/* 3. 브랜드 컬러 */
:root {
  --brand: #0C8C5E;
  --brand-light: #18E299;
}
```

**절대 하지 말아야 할 것 하나**: hero를 평범한 흰 배경 SaaS 섹션으로 만들지 말 것. Mintlify의 첫인상은 teal atmospheric image + floating docs chrome 조합이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://mintlify.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | reused existing phase1 artifacts |
| HTML size | 542694 bytes |
| CSS files | 4 files, 223790 CSS characters |
| Token prefix | `color` / Tailwind v4 theme variables |
| Method | existing `insane-design/mintlify` phase1 JSON + CSS + homepage screenshot |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js-style static output with hashed CSS chunks and font module classes.
- **Design system**: Tailwind v4 token layer in active use; no public official DS tier name observed in the analyzed artifacts.
- **CSS architecture**:
  ```css
  theme tokens    (--color-*, --font-*, --radius-*, --text-*)    design primitives
  semantic layer  (--color-background-main, --color-text-main)   UI roles
  utilities       (.bg-*, .text-*, .shadow-*, .rounded-*)        component composition
  custom craft    (.hero-title, .footer-cta-gradient)            signature overrides
  ```
- **Class naming**: Tailwind utility classes plus small semantic helpers such as `.hero-title`, `.bg-image-hero`, `.footer-cta-gradient`, `.shadow-feature-card`, `.shadow-navbar-bg`.
- **Default theme**: mixed. The root token set is light, while the hero block explicitly uses `dark` class treatment.
- **Font loading**: Next/font-like generated module classes for Inter and Geist Mono.
- **Canonical anchor**: homepage hero screenshot, because it contains the brand atmosphere, headline, primary form, navigation, and product chrome in one frame.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Inter` via `--font-inter: "inter", "inter Fallback"`.
- **Body font**: `Inter` via `--default-font-family: var(--font-inter)`.
- **Code font**: `Geist Mono` via `--font-geist-mono: "Geist Mono", "Geist Mono Fallback"`.
- **Weight normal / medium / semibold / bold**: `400` / `500` / `600` / `700`.

```css
:root {
  --font-inter: "inter", "inter Fallback";
  --font-geist-mono: "Geist Mono", "Geist Mono Fallback";
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
}

body {
  font-family: var(--font-inter);
  font-weight: var(--font-weight-normal);
}
```

### Note on Font Substitutes

- **Inter** is replaceable with `Geist Sans` or `IBM Plex Sans` only if display tracking is corrected. Keep hero tracking at `-.02em` and preserve `line-height: 115%`.
- **Geist Mono** should not be replaced with a decorative monospace. If unavailable, use `ui-monospace` or `SFMono-Regular` and keep code-like text compact; the site uses mono as a trust signal, not as a visual gimmick.
- **Do not simulate Mintlify with system-ui alone**. The shape will become too generic unless the hero atmospheric image, pill controls, and shadow stack are also reproduced.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `.hero-title` | `max(2.5rem, min(4vw, 4rem))` | 600 | 115% | `-.02em` |
| `--text-3xl` | `1.875rem` | variable | `2.25 / 1.875` | inherited |
| `--text-2xl` | `1.5rem` | variable | `2 / 1.5` | inherited |
| `--text-xl` | `1.25rem` | variable | `1.75 / 1.25` | inherited |
| `--text-lg` | `1.125rem` | 400 | `1.75 / 1.125` | inherited |
| `--text-base` | `1rem` | 400 | `1.5` | inherited |
| `--text-sm` | `.875rem` | 500 common in controls | `1.25 / .875` | inherited |
| `--text-xs` | `.75rem` | 500 common in badges | `1 / .75` | inherited |

> ⚠️ The extractor found no complete heading scale object, so the hero class and Tailwind text tokens are the reliable measured ladder.

### Principles

1. Hero display text is optically tightened: `-.02em` only on `.hero-title`, not as a global body rule.
2. The page relies on 600 for display authority and 500 for controls; 700 exists but should stay rare.
3. Body copy stays 400 with generous line-height; the "AI-native" feel comes from scene composition, not heavy typography.
4. Mono is contextual. Use Geist Mono for code, keyboard hints, or developer UI; never use mono for the main marketing headline.
5. Navigation and pill buttons are compact but not tiny: 15px button text and `.875rem` utility text keep the chrome precise.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (2 observed brand steps)

| Token | Hex |
|---|---|
| `--color-brand` | `#0C8C5E` |
| `--color-brand-light` | `#0C8C5E` |
| observed bright brand candidate | `#18E299` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| Hero/background dark surface | `#151616` |
| Text invert | `#FFFFFF` |
| Bright mint accent candidate | `#18E299` |

### 06-3. Neutral Ramp

| Step | Light | Dark / Invert |
|---|---|---|
| page | `#FFFFFF` | `#08090A` |
| ink | `#08090A` | `#FFFFFF` |
| prose heading | `#101828` | `#FFFFFF` |
| prose body | `#364153` | `#D1D5DC` |
| border | `#E5E7EB` | `#364153` |
| gray surface | `#F9F8F7` | `#151616` |
| warm gray emphasis | `#E6E5E3` | not fully mapped |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Orange gradient utility | gradient accent | `#FF5A00` |
| Blue utility | `--color-blue-500` | `#3080FF` |
| Green utility | `--color-green-800` | `#016630` |
| Red utility | `--color-red-600` | `#E40014` |

### 06-5. Semantic

| Token | Hex / Value | Usage |
|---|---|---|
| `--color-background-main` | `#FFFFFF` | primary page/product surface |
| `--color-text-main` | `#08090A` | main ink |
| `--color-text-soft` | `rgba(8,9,10,.8)` | softened copy |
| `--color-text-sub` | `rgba(8,9,10,.6)` | secondary copy |
| `--color-muted` | `rgba(8,9,10,.5)` | muted UI |
| `--color-border-sub` | `rgba(8,9,10,.07)` | hairline/subtle separator |
| `--color-background-soft` | `rgba(8,9,10,.03)` | soft fill |
| `--color-border-surface` | `rgba(8,9,10,.05)` | surface border |
| `--color-border-soft` | `rgba(8,9,10,.15)` | stronger glass/form border |
| `--color-brand` | `#0C8C5E` | brand action/accent |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `bg-background-main` | `--color-background-main` | page and product chrome |
| `text-text-main` | `--color-text-main` | primary copy and hero title |
| `text-text-invert` | `--color-text-invert` | dark button text |
| `border-border-soft` | `--color-border-soft` | translucent form capsule border |
| `bg-background-invert` | `--color-background-invert` / `--color-text-main` | primary dark pill CTA |
| `focus-visible:outline-brand` | `--color-brand` | focus ring |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| white | `#FFFFFF` / `#FFF` | 62+ |
| near black / logo ink | `#231F20` | 46 |
| warm chromatic neutral | `#F1EFED` | 22 |
| orange gradient accent | `#FF5A00` | 10 |
| blue accent | `#5984F2` | 7 |
| prose heading | `#101828` | 6 |
| page ink | `#08090A` | 5 |
| brand green | `#0C8C5E` | 5 |

### 06-8. Color Stories

**`{colors.brand}` (#0C8C5E)** — The real UI brand color. Use it for focus, brand marks, small emphasis, and controlled CTA accents. It should not flood the page; Mintlify lets atmosphere carry more visual area than the brand swatch.

**`{colors.surface-main}` (#FFFFFF)** — The product proof surface. The docs mockup, cards, and page chrome need white to read as trustworthy documentation infrastructure against the hero sky.

**`{colors.ink-main}` (#08090A)** — The main UI ink and invert-button anchor. It gives the pill buttons their crisp contrast and prevents the atmospheric hero from becoming too soft.

**`{colors.hero-accent}` (#FF5A00)** — A contained gradient/utility accent. Treat it like an effect color, not a brand color; using it for primary CTAs would misread Mintlify.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Use case |
|---|---:|---|
| `--spacing` | `.25rem` | Tailwind v4 base unit |
| hero top padding | `pt-[6.5rem]` | clears fixed navbar and centers the hero composition |
| hero desktop bottom | `md:pb-24` | creates room above product mockup |
| hero mobile bottom | `pb-[4.5rem]` | compressed mobile hero |
| hero horizontal mobile | `max-md:px-6` | safe side gutters |
| hero subtitle margin | `mt-6` | headline-to-copy separation |
| hero form margin | `mt-8` | copy-to-form separation |
| form padding | `p-1` | inner pill padding around input + button |
| form gap | `gap-1.5` | compact input/button separation |
| mobile nav panel | `p-4`, `gap-2` | stacked menu controls |

**주요 alias**:
- `--spacing` → `.25rem` (all utility spacing compounds from this unit)
- `px-3` → `12px` (compact pill button)
- `py-[4.5px]` → 4.5px vertical CTA compensation

### Whitespace Philosophy

Mintlify spends its largest vertical air in the hero, not in generic section padding. The top padding (`6.5rem`) and the large bottom space before the docs surface let the atmospheric background breathe; then the product chrome intrudes as evidence. The rhythm says "look up, then inspect."

Inside controls the spacing is tight. Pills, nav links, and the email capsule use compact padding and small gaps. This contrast is the system: cinematic outer air, precise inner chrome.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `--radius-sm` | `.25rem` | small UI edges |
| `--radius-md` | `.375rem` | default controls/cards |
| `--radius-lg` | `.5rem` | medium surfaces |
| `--radius-xl` | `.75rem` | larger cards |
| `--radius-2xl` | `1rem` | modal/product surfaces |
| `--radius-3xl` | `1.5rem` | large feature cards |
| `--radius-4xl` | `2rem` | hero product mockup scale |
| `rounded-full` | `9999px` | buttons, badges, email capsule |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| `shadow-button-sm` | `0px 2px 4px 0px var(--color-background-soft)` | compact CTA depth |
| `shadow-feature-card` | `0 192px 54px transparent, 0 123px 49px transparent, 0 69px 41px rgba(0,0,0,.01), 0 31px 31px rgba(0,0,0,.03), 0 8px 17px rgba(0,0,0,.03)` | large feature card lift |
| `shadow-navbar-bg` | `0px 164px 46px transparent, 0px 105px 42px transparent, 0px 59px 36px rgba(0,0,0,.01), 0px 26px 26px rgba(0,0,0,.02), 0px 7px 14px rgba(0,0,0,.02)` | fixed nav soft backing |
| general surface | `0 1px 4px rgba(9,9,11,.05)` | subtle card/chrome separation |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| button transition | `transition-[color,background-color] duration-100` | primary CTA hover |
| reduced motion query | `@media (prefers-reduced-motion: reduce)` | accessibility fallback present |
| carousel controls | Previous / Next slide buttons in HTML | customer story carousel behavior inferred from DOM |
| hover media query | `@media (hover:hover)` | hover-only treatment guarded by capability |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: hero title `max-w-[43rem]`; hero subtitle `max-w-[29.5rem]`; hero form `max-w-[22.5rem]`.
- **Grid type**: flex-driven hero and utility composition, with product/documentation mockup as a large anchored visual surface.
- **Column count**: hero is single-column centered above a full-width product mockup.
- **Gutter**: mobile horizontal gutter is `px-6`; nav/header uses `px-6`.

### Hero

- **Pattern Summary**: `teal atmospheric image + centered H1 + email capsule CTA + floating documentation mockup`.
- Layout: single-column centered marketing copy, followed by large docs UI preview.
- Background: image-based atmospheric hero via `.bg-image-hero`, with light/dark background image variants.
- **Background Treatment**: image overlay style, painterly clouds, deep teal/blue gradient feel; not CSS-only gradient mesh.
- H1: `max(2.5rem, min(4vw, 4rem))` / weight `600` / tracking `-.02em`.
- Max-width: `43rem` for H1, `29.5rem` for supporting text.

### Section Rhythm

```css
.hero-copy {
  padding-top: 6.5rem;
  padding-bottom: 4.5rem;
}

@media (min-width: 48rem) {
  .hero-copy {
    padding-bottom: 6rem;
  }
}
```

### Card Patterns

- **Card background**: white or semantic `--color-background-main`.
- **Card border**: soft rgba border, usually `rgba(8,9,10,.07)` or `.15` depending on glass/solid context.
- **Card radius**: large product surfaces live near `1.5rem` to `2rem`; controls use full pill.
- **Card padding**: utility-defined; feature surfaces use spacious padding while controls stay compact.
- **Card shadow**: multi-layer, very low-alpha, transparent upper layers before visible near shadows.

### Navigation Structure

- **Type**: horizontal fixed top navigation with dropdown-capable Resources/Documentation buttons.
- **Position**: `fixed`, `top-0`, `left-0`, `right-0`, `z-50`.
- **Height**: content-driven; header uses `py-4`.
- **Background**: transparent over hero with shadow/backing utility available.
- **Border**: not dominant in hero nav; structure comes from contrast and pill CTAs.

### Content Width

- **Prose max-width**: product/doc content inside mockup follows docs-style narrower reading widths.
- **Container max-width**: hero copy maxes at `43rem`; form at `22.5rem`.
- **Sidebar width**: product mockup includes left docs sidebar; exact CSS width not separately extracted.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | default | utility-first base styles, single-column hero |
| Small | `min-width: 40rem` | Tailwind `sm` tier observed |
| Medium | `min-width: 48rem` | `md` tier observed; hero bottom spacing expands |
| Large | `min-width: 64rem` | desktop navigation/product composition |
| XL | `min-width: 80rem` | large layout expansion |
| 2XL | `min-width: 96rem` | wide viewport refinement |
| Custom | `380px` through `1080px` | several bespoke art/mockup alignment thresholds |

### Touch Targets

- **Minimum tap size**: not fully measured; pill buttons are visually compact but padded.
- **Button height (mobile)**: content-driven with `py-[4.5px]`, `px-3`; likely below 44px for some nav controls.
- **Input height (mobile)**: form capsule height is content-driven by `p-1`, input, and inner CTA.

### Collapsing Strategy

- **Navigation**: desktop horizontal nav; mobile hidden full-height panel exists (`hidden h-dvh`, `z-50`) with stacked controls.
- **Grid columns**: hero remains centered; product mockup likely scales/crops rather than becoming a multi-column layout.
- **Sidebar**: product mockup sidebar is part of the image/UI preview and may crop on small screens.
- **Hero layout**: single-column at all observed sizes; spacing and art scale change at breakpoints.

### Image Behavior

- **Strategy**: atmospheric image background + product mockup visual.
- **Max-width**: image/product surface constrained by viewport and mockup container.
- **Aspect ratio handling**: screenshot shows a wide desktop hero optimized for 1280x800; mobile art crop not verified.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary pill CTA**

```html
<a class="inline-flex items-center rounded-full font-medium shadow-button-sm bg-background-invert text-text-invert border border-background-invert hover:bg-background-invert/85 text-[15px] py-[4.5px] px-3">
  Start for free
</a>
```

| State | Spec |
|---|---|
| default | near-black fill, white text, full pill radius |
| hover | `hover:bg-background-invert/85` |
| focus | `focus-visible:outline-2 focus-visible:outline-brand` |
| active | no separate measured active token |
| disabled/loading | not observed in homepage artifacts |

### Badges

**Announcement badge**

```html
<a class="rounded-full">
  <span>NEW</span>
  <span>We raised a $45M Series B...</span>
</a>
```

| State | Spec |
|---|---|
| default | compact pill, brand-green "NEW" chip, dark translucent strip in hero |
| icon | right arrow circle at end of announcement |
| behavior | link-like announcement bar above H1 |

### Cards & Containers

**Product documentation mockup**

```html
<div class="rounded-[large] bg-background-main shadow-feature-card">
  <!-- docs sidebar + guide tabs + search/ask AI controls -->
</div>
```

| Property | Spec |
|---|---|
| background | `#FFFFFF` |
| radius | large, visually close to `1.5rem`-`2rem` |
| shadow | multi-layer feature-card shadow |
| border | very soft neutral hairline |
| visual role | proof of docs product inside atmospheric scene |

### Navigation

```html
<header class="w-full py-4 px-6 z-50 mx-auto fixed top-0 left-0 right-0">
  <nav>
    <button>Resources</button>
    <button>Documentation</button>
    <a>Customers</a>
    <a>Blog</a>
    <a>Pricing</a>
    <a class="rounded-full">Contact sales</a>
    <a class="rounded-full">Start for free</a>
  </nav>
</header>
```

| Property | Spec |
|---|---|
| position | fixed top |
| spacing | `py-4 px-6` |
| link typography | Inter, compact, medium/normal |
| CTAs | right aligned pill pair |
| mobile | full-screen hidden panel present |

### Inputs & Forms

**Hero email capsule**

```html
<form class="mt-8 p-1 max-w-[22.5rem] w-full rounded-full border border-border-soft backdrop-blur-[12px] bg-border-soft flex items-center gap-1.5 dark">
  <input placeholder="Email address" />
  <button class="rounded-full bg-background-invert text-text-invert">Start now</button>
</form>
```

| Property | Spec |
|---|---|
| radius | full pill |
| background | translucent semantic border/soft fill |
| blur | `backdrop-blur-[12px]` |
| border | `border-border-soft` |
| CTA | compact dark pill inside capsule |
| focus/error | focus outline exists on button; form error state not observed |

### Hero Section

```html
<section class="relative isolate">
  <div class="flex flex-col items-center justify-center pt-[6.5rem] md:pb-24 pb-[4.5rem] max-md:px-6 dark">
    <h1 class="w-full max-w-[43rem] text-center text-text-main hero-title font-semibold leading-[115%] text-balance">
      The Intelligent Knowledge Platform
    </h1>
  </div>
</section>
```

| Property | Spec |
|---|---|
| background | `.bg-image-hero`, light/dark image variants |
| alignment | centered |
| title | `.hero-title`, 600, `-.02em`, 115% |
| copy width | `29.5rem` |
| product visual | large docs UI mockup anchored below copy |

### 13-2. Named Variants

| Variant | Spec |
|---|---|
| `button-primary-pill` | `bg-background-invert`, `text-text-invert`, `rounded-full`, `text-[15px]`, `py-[4.5px]`, `px-3` |
| `button-secondary-sales` | translucent/darker pill in nav, same compact radius logic |
| `glass-email-capsule` | `backdrop-blur-[12px]`, `border-border-soft`, `bg-border-soft`, `rounded-full`, inner dark CTA |
| `announcement-new-pill` | green "NEW" chip embedded inside long rounded announcement link |
| `docs-preview-card` | white product surface, oversized radius, multi-layer low-alpha shadow |
| `navbar-fixed-transparent` | fixed top, no heavy border, pill CTAs define action zone |

### 13-3. Signature Micro-Specs

```yaml
atmospheric-docs-hero:
  description: "A documentation UI preview staged inside a painterly teal sky rather than a plain SaaS hero."
  technique: ".bg-image-hero with light/dark image variants, centered copy, max-w-[43rem] hero title, and floating white docs chrome"
  applied_to: ["{component.Hero Section}", "{component.docs-preview-card}"]
  visual_signature: "documentation becomes weather: a precise product surface suspended in teal cloud-light."

tight-knowledge-platform-title:
  description: "Display headline optical tightening that keeps the category claim large but not heavy."
  technique: "font-size: max(2.5rem, min(4vw, 4rem)); line-height: 115%; letter-spacing: -.02em; font-weight: 600"
  applied_to: ["{component.hero-title}", "{typography.ladder.hero-title}"]
  visual_signature: "the H1 lands like product positioning, not a blog-docs masthead."

frosted-email-airlock:
  description: "Lead-capture form that mediates between the atmospheric hero and the grounded black CTA."
  technique: "rounded-full; p-1; border-border-soft; bg-border-soft; backdrop-blur-[12px]; inner bg-background-invert pill"
  applied_to: ["{component.glass-email-capsule}", "{component.Inputs & Forms}"]
  visual_signature: "a translucent capsule in the sky with a small near-black conversion core."

transparent-first-altitude-shadow:
  description: "Depth stack where early shadow layers are transparent and only the lowest layers carry soft alpha."
  technique: "0 192px 54px transparent, 0 123px 49px transparent, 0 69px 41px rgba(0,0,0,.01), 0 31px 31px rgba(0,0,0,.03), 0 8px 17px rgba(0,0,0,.03)"
  applied_to: ["{component.feature-card-shadow}", "{component.docs-preview-card}"]
  visual_signature: "the docs surface appears to have altitude, not a visible drop-shadow outline."

contained-conic-brand-ring:
  description: "Brand color appears as a controlled conic accent instead of a page-wide green wash."
  technique: "conic-gradient(from 0deg, var(--color-border-surface) 0deg, var(--color-brand) 60deg, var(--color-brand) 270deg, var(--color-border-surface) 270deg)"
  applied_to: ["{colors.brand}", "{component.decorative/interactive accents}"]
  visual_signature: "a small intelligence/agent signal around otherwise neutral documentation chrome."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Big category claim, not feature list | "The Intelligent Knowledge Platform" |
| Subheading | Human + AI dual audience | "built for both humans and AI" |
| Primary CTA | Direct, low-friction start | "Start now", "Start for free" |
| Enterprise CTA | Sales/demo language stays secondary | "Contact sales", "Get a demo" |
| Proof | Customer stories frame documentation as operational leverage | "See how Anthropic accelerates AI development..." |
| Tone | Developer-serious, AI-native, less playful than the hero art might suggest | concise, confident |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Mintlify — copy into your root stylesheet */
:root {
  /* Fonts */
  --mint-font-family: "Inter", "inter Fallback", -apple-system, sans-serif;
  --mint-font-family-code: "Geist Mono", "Geist Mono Fallback", ui-monospace;
  --mint-font-weight-normal: 400;
  --mint-font-weight-medium: 500;
  --mint-font-weight-semibold: 600;
  --mint-font-weight-bold: 700;

  /* Brand */
  --mint-color-brand: #0C8C5E;
  --mint-color-brand-light: #18E299;
  --mint-color-hero-effect: #FF5A00;

  /* Surfaces */
  --mint-bg-page: #FFFFFF;
  --mint-bg-dark: #151616;
  --mint-text: #08090A;
  --mint-text-prose: #364153;
  --mint-text-heading: #101828;
  --mint-border: #E5E7EB;

  /* Spacing */
  --mint-space-unit: .25rem;
  --mint-hero-top: 6.5rem;
  --mint-hero-copy-gap: 1.5rem;
  --mint-hero-form-gap: 2rem;

  /* Radius */
  --mint-radius-md: .375rem;
  --mint-radius-xl: .75rem;
  --mint-radius-3xl: 1.5rem;
  --mint-radius-pill: 9999px;
}

.mint-hero-title {
  font-family: var(--mint-font-family);
  font-size: max(2.5rem, min(4vw, 4rem));
  font-weight: var(--mint-font-weight-semibold);
  line-height: 115%;
  letter-spacing: -.02em;
  color: var(--mint-text);
  text-align: center;
  text-wrap: balance;
}

.mint-primary-pill {
  border-radius: var(--mint-radius-pill);
  background: var(--mint-text);
  color: var(--mint-bg-page);
  border: 1px solid var(--mint-text);
  padding: 4.5px 12px;
  font-size: 15px;
  font-weight: 500;
  transition: color 100ms, background-color 100ms;
  box-shadow: 0 2px 4px rgba(8, 9, 10, .03);
}

.mint-email-capsule {
  display: flex;
  align-items: center;
  gap: .375rem;
  width: 100%;
  max-width: 22.5rem;
  padding: .25rem;
  border-radius: var(--mint-radius-pill);
  border: 1px solid rgba(8, 9, 10, .15);
  background: rgba(8, 9, 10, .15);
  backdrop-filter: blur(12px);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Mintlify-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        mint: {
          brand: '#0C8C5E',
          brandLight: '#18E299',
          ink: '#08090A',
          surface: '#FFFFFF',
          darkSurface: '#151616',
          proseHeading: '#101828',
          proseBody: '#364153',
          border: '#E5E7EB',
          heroEffect: '#FF5A00',
        },
      },
      fontFamily: {
        sans: ['Inter', 'inter Fallback', 'system-ui'],
        mono: ['Geist Mono', 'Geist Mono Fallback', 'ui-monospace'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
        semibold: '600',
        bold: '700',
      },
      borderRadius: {
        sm: '.25rem',
        md: '.375rem',
        lg: '.5rem',
        xl: '.75rem',
        '2xl': '1rem',
        '3xl': '1.5rem',
        '4xl': '2rem',
        full: '9999px',
      },
      boxShadow: {
        'button-sm': '0 2px 4px rgba(8,9,10,.03)',
        'feature-card': '0 192px 54px transparent, 0 123px 49px transparent, 0 69px 41px rgba(0,0,0,.01), 0 31px 31px rgba(0,0,0,.03), 0 8px 17px rgba(0,0,0,.03)',
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
| Brand primary | `{colors.brand}` | `#0C8C5E` |
| Brand bright | `{colors.brand-bright}` | `#18E299` |
| Background | `{colors.surface-main}` | `#FFFFFF` |
| Text primary | `{colors.ink-main}` | `#08090A` |
| Text heading | `{colors.prose-heading}` | `#101828` |
| Text body | `{colors.prose-body}` | `#364153` |
| Border | `{colors.border-gray}` | `#E5E7EB` |
| Hero effect | `{colors.hero-accent}` | `#FF5A00` |

### Example Component Prompts

#### Hero Section

```text
Mintlify 스타일 히어로 섹션을 만들어줘.
- 배경: teal/blue atmospheric hero image, not a plain gradient.
- H1: Inter, max(2.5rem, min(4vw, 4rem)), weight 600, line-height 115%, tracking -.02em.
- 텍스트: #08090A on dark hero context as token-inverted copy; subtitle max-width 29.5rem.
- CTA form: max-width 22.5rem, rounded-full, border rgba(8,9,10,.15), backdrop-blur 12px.
- Product proof: large white docs UI mockup below headline with 1.5rem-2rem radius and multi-layer soft shadow.
```

#### Card Component

```text
Mintlify 스타일 feature/product card를 만들어줘.
- 배경: #FFFFFF.
- border: 1px solid rgba(8,9,10,.07) or #E5E7EB.
- radius: 1.5rem for feature cards, 2rem for large product mockups.
- shadow: transparent-first multi-layer stack, visible alpha no stronger than .03 for normal chrome.
- 제목: Inter 600, body copy Inter 400, color #364153.
```

#### Badge

```text
Mintlify 스타일 announcement badge를 만들어줘.
- shape: rounded-full.
- "NEW" chip: #0C8C5E or bright mint accent, compact uppercase.
- container: dark translucent pill when placed over hero.
- avoid: square badge, loud border, or orange as brand color.
```

#### Navigation

```text
Mintlify 스타일 상단 네비게이션을 만들어줘.
- fixed top, px-6, py-4, z-50.
- logo left, Resources/Documentation dropdown buttons, Customers/Blog/Pricing links.
- right side: Contact sales pill + Start for free primary pill.
- buttons: Inter 15px, weight 500, rounded-full, compact padding.
```

### Iteration Guide

- **색상 변경 시**: #0C8C5E is the brand anchor. Do not promote #FF5A00 into CTA primary.
- **폰트 변경 시**: preserve Inter-like geometry and hero `-.02em` tracking.
- **여백 조정 시**: maintain cinematic outer air and compact inner controls.
- **새 컴포넌트 추가 시**: use pill radius for controls and 1.5rem-2rem radius for product surfaces.
- **다크 모드**: hero can be dark/atmospheric while product chrome stays white; do not force the whole page into a dark dashboard.
- **반응형**: keep hero centered; scale/crop art rather than turning it into a two-column marketing layout.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use an atmospheric hero image treatment before showing the docs product UI.
- Keep the hero H1 centered, tight, and semibold: `-.02em`, 600, `115%`.
- Use #0C8C5E as the real brand anchor and #18E299 only as a brighter accent.
- Keep buttons pill-shaped with compact 15px typography.
- Use white product surfaces over the hero atmosphere to make the documentation UI feel tangible.
- Use multi-layer low-alpha shadows for product surfaces instead of a single heavy shadow.
- Let Geist Mono appear in developer/code contexts only.
- Preserve the product narrative: docs for people and AI, not generic SaaS productivity.

### ❌ DON'T

- 배경을 `#FFFFFF` 단독 hero로 두지 말 것 — 대신 atmospheric teal/blue image treatment 위에 product chrome을 올릴 것.
- 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#08090A` 또는 prose용 `#101828` / `#364153` 사용.
- primary brand를 `#FF5A00`로 설정하지 말 것 — 대신 `#0C8C5E` 사용; orange는 gradient/effect accent로만 제한.
- product card border를 `#000000`로 두지 말 것 — 대신 `#E5E7EB` 또는 `rgba(8,9,10,.07)` 사용.
- hero title에 `font-weight: 800` 또는 `900` 사용 금지 — Mintlify hero는 600이 맞다.
- hero title tracking을 `0`으로 두지 말 것 — `.hero-title`은 `letter-spacing: -.02em`이 핵심이다.
- CTA를 `border-radius: 8px` 사각 버튼으로 만들지 말 것 — `9999px` pill shape 사용.
- docs mockup에 강한 `rgba(0,0,0,.20)` 단일 그림자를 쓰지 말 것 — low-alpha multi-layer shadow 사용.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- No plain white SaaS hero. White exists as product chrome, not as the emotional first viewport.
- No second CTA brand color. #FF5A00 is present, but not promoted into the main action system.
- No heavy black typography. Even the main ink is #08090A and display weight stops at 600.
- No square primary buttons. Controls are pill-first, especially nav and hero CTA.
- No decorative card borders as identity. Structure comes from soft shadows, radius, and surface contrast.
- No global monospace aesthetic. Geist Mono is a developer accent, not the brand voice.
- No loud rainbow AI gradient. The hero is painterly atmospheric art, not generic purple/blue mesh.
- No dense dashboard first impression. The docs UI is shown as proof after a cinematic knowledge-platform claim.
- No visible over-animation in the captured hero. Motion exists in transitions/carousel controls, but the signature is composition.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-only analysis** — The report uses the captured `https://mintlify.com` homepage artifacts. Product subflows, pricing, login, editor, and generated documentation sites were not visited.
- **Desktop screenshot bias** — The visual reading is anchored on a 1280x800 hero screenshot. Mobile art crop and tap target measurements are inferred from CSS classes, not visually verified.
- **CSS utility indirection** — Tailwind utilities and CSS variables are heavily compiled. Some component semantics are reconstructed from class combinations rather than named source components.
- **Logo/customer colors filtered imperfectly** — Frequency candidates include chromatic values that may come from customer logos or illustrations. #0C8C5E is selected because it appears as `--color-brand`, not merely because of frequency.
- **Exact hero art colors are image-derived, not tokenized** — The teal sky and cloud palette dominate the screenshot but are not all represented as CSS hex tokens.
- **Form validation states not surfaced** — Input error, loading, success, disabled, and autocomplete states were not visible in the homepage capture.
- **Dark mode is partial** — Hero uses a `dark` class context and dark image variant, but a full site-wide dark token mapping was not proven.
- **JavaScript motion not audited** — Carousel and interaction hints are visible in HTML/CSS, but animation curves and JS-driven behavior were not inspected.
- **Official design-system status not claimed** — The artifacts show a coherent system in use (`lv2`), but not a public Mintlify designer guidebook or named DS documentation.
