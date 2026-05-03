---
schema_version: 3.2
slug: warp
service_name: Warp
site_url: https://www.warp.dev
fetched_at: 2026-05-03T16:30:00+09:00
default_theme: dark
brand_color: "#FAF9F5"
primary_font: "Matter Regular"
font_weight_normal: 400
token_prefix: framer

bold_direction: "Terminal Theater"
aesthetic_category: "other"
signature_element: "hero_impact"
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Framer-generated token surface with real font, color, input, and component variables, but without a fully named public DS namespace."

colors:
  page-dark: "#121212"
  surface-cream: "#FAF9F5"
  text-primary-dark: "#FFFFFFE6"
  text-link-light: "#232224"
  text-muted: "#AFAEAC"
  border-soft-dark: "#FFFFFF29"
  input-dark: "#FFFFFF0D"
  warm-hairline: "#E3E2E0"

typography:
  display: "Matter Regular"
  body: "Inter"
  mono: "Geist Mono"
  ladder:
    - { token: hero, size: "clamp(48px, 5.5vw, 80px)", weight: 400, line_height: "1.1em", tracking: "-0.04em" }
    - { token: product-title, size: "24px", weight: 400, line_height: "1.2em", tracking: "0" }
    - { token: body, size: "16px", weight: 400, line_height: "1.2em", tracking: "0" }
    - { token: nav, size: "16px", weight: 500, line_height: "1.2em", tracking: "0" }
    - { token: mono-label, size: "12px", weight: 500, line_height: "1.2em", tracking: "0" }
  weights_used: [400, 500, 600, 700, 900]
  weights_absent: [300, 800]

components:
  button-download: { bg: "{colors.surface-cream}", color: "{colors.text-link-light}", radius: "5px", padding: "12px 18px" }
  button-outline-dark: { bg: "transparent", color: "{colors.text-primary-dark}", border: "1px solid #FFFFFF", radius: "6px", padding: "10px 14px" }
  product-card-media: { bg: "image", radius: "20px", shadow: "none", overflow: "hidden" }
  announcement-bar: { bg: "{colors.surface-cream}", color: "#666469", height: "34px" }
---

# DESIGN.md — Warp

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Warp's marketing surface is not trying to look like a terminal screenshot stretched into a website. It behaves more like a dark demo stage: the page floor is almost black at #121212 (`{colors.page-dark}`), the main headline sits in soft off-white #FFFFFFE6 (`{colors.text-primary-dark}`), and the product cards are presented as two large instruments under quiet stage lighting. The terminal identity is there, but it is translated into scale, restraint, and contrast rather than green monospace nostalgia.

The most important visual decision is the inversion called out in the pitfall list: this is not the old light cream Warp marketing page. The captured homepage is dark-first. Warm cream survives as a precise UI material, not as the whole canvas: the announcement bar, the primary "Download for Mac" button, and selected light surfaces use #FAF9F5 / #FAF9F6 (`{colors.surface-cream}`), while the main page remains black and charcoal.

Typography carries the brand more than color does. The hero headline uses a Matter-like face with large optical tightening: `letter-spacing: -0.04em` and `line-height: 1.1em`. That makes "Warp is the agentic development environment" feel compressed and deliberate, like a product nameplate rather than a generic SaaS H1. Inter appears heavily in extracted CSS, but the visible brand voice depends on Matter Regular / Matter Medium and monospaced accents from Geist Mono, Fragment Mono, DM Mono, and Matter Mono.

The composition is a split product promise: "Warp Terminal" and "Oz" sit as paired modules beneath one shared claim. This is the site's signature choreography. It does not make the terminal product and the cloud agent product fight for attention; it gives each a framed screenshot panel and aligns both under the same dark operating-room atmosphere.

### Key Characteristics

- Dark-first marketing canvas: body background is explicitly `rgb(18, 18, 18)` / #121212.
- Warm cream is used as a control and surface accent, not as the global background.
- Huge centered H1 with tight `-0.04em` tracking and `1.1em` line-height.
- Navigation is quiet, horizontal, and top-loaded, with a separate cream announcement strip above.
- Product architecture is communicated through two side-by-side cards: Warp Terminal and Oz.
- Media cards have large 20px rounded corners and no obvious chrome shadow.
- Buttons are small, tactile, and mostly rectangular: 5px / 6px radii, not pill-first.
- Framer-generated CSS supplies token hashes and component variables rather than a hand-authored semantic DS.
- Monospace fonts appear as supporting texture, but the primary site voice is proportional.
- The strongest brand move is contrast discipline: black stage, cream controls, soft gray text.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Terminal Theater
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **dark stage hero with paired terminal/cloud-agent product frames**으로 기억된다.
> **Code Complexity**: high — Framer output, multiple custom fonts, hashed tokens, large inline CSS, and image-heavy product panels require careful extraction.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Warp처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Matter Regular", "Inter", -apple-system, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #121212; --fg: #FFFFFFE6; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컨트롤 컬러 */
:root { --brand: #FAF9F5; }
```

**절대 하지 말아야 할 것 하나**: Warp를 밝은 cream SaaS 랜딩으로 재현하지 말 것. 현재 홈페이지의 주 무대는 `#121212`이고, cream은 버튼/announcement/media surface에만 절제해 들어간다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.warp.dev` |
| Fetched | 2026-05-03T16:30:00+09:00 |
| Extractor | phase1 reuse from `insane-design/warp/` |
| HTML size | 812063 bytes (Framer-rendered marketing page) |
| CSS files | 1 inline-combined CSS file, 270250 bytes |
| Token prefix | `framer` plus hashed `--token-*` variables |
| Method | Existing phase1 JSON + inline CSS + captured hero screenshot; report HTML generation skipped by request |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Framer export / Framer Sites runtime.
- **Design system**: Framer token surface — prefix `framer`, plus UUID-like `--token-*` variables.
- **CSS architecture**:
  ```text
  core        (--token-*, --framer-text-color)       raw hex and font values
  component   (--framer-input-*)                    input/form component variables
  runtime     (.framer-* generated classes)          layout, rich text, media, responsive behavior
  ```
- **Class naming**: Generated `.framer-*` classes with component and variant hashes.
- **Default theme**: dark (bg = `#121212`).
- **Font loading**: Google-hosted fonts plus Framer CDN `@font-face` assets.
- **Canonical anchor**: Homepage hero: announcement bar, dark nav, centered H1, paired product panels.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Matter Regular` / `Matter Medium` (Framer CDN custom font)
- **Body font**: `Inter` appears most often in extracted CSS
- **Code font**: `Geist Mono`, `Fragment Mono`, `DM Mono`, `Matter Mono Regular`
- **Weight normal / bold**: `400` / `700`; visible nav and button emphasis often use `500`

```css
:root {
  --framer-font-family: "Matter Regular", "Matter Regular Placeholder", sans-serif;
  --framer-code-font-family: "Geist Mono", "Fragment Mono", "DM Mono", ui-monospace;
  --framer-font-weight: 400;
  --framer-font-weight-bold: 700;
}
body {
  font-family: var(--framer-font-family);
  font-weight: var(--framer-font-weight);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Matter Regular / Matter Medium** — proprietary-looking Framer CDN font pair; do not replace with plain Arial.
  - Open-source fallback: **Inter** at weight 400/500 for body and navigation, with tighter headline tracking.
  - Display correction: if Matter is unavailable, use `Inter` weight 400 and keep `letter-spacing: -0.04em`.
  - Line-height correction: preserve `1.1em` on the hero; relaxing to `1.2` makes the H1 feel generic.
- **Geist Mono / Fragment Mono** — use for terminal-coded fragments and compact labels only.
  - Open-source fallback: **Geist Mono** or **DM Mono** at 400/500.
  - Do not set the whole page in monospace; Warp's website is not a terminal emulator skin.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| Hero H1 | `clamp(48px, 5.5vw, 80px)` | 400 | `1.1em` | `-0.04em` |
| Product title | `24px` | 400 | `1.2em` | `0` |
| Body / card copy | `16px` | 400 | `1.2em` | `0` |
| Nav link | `16px` | 500 | `1.2em` | `0` |
| Small mono / input | `12px` | 500 | `1.2em` | `0` |

> ⚠️ Warp's visible brand feel depends on the display tracking. The extracted CSS repeatedly resolves `--framer-letter-spacing` to `-.04em`; skipping that turns the hero into ordinary SaaS type.

### Principles

1. Display copy is large but not heavy — use scale and tight spacing before using weight.
2. `-0.04em` tracking belongs to headline/display contexts; body copy should stay at `0`.
3. Matter gives the brand warmth; mono fonts are supporting texture, not the main voice.
4. Weight 500 is functional, used for navigation, controls, and compact labels.
5. Weight 900 appears in CSS, but should not become the default visual voice of the homepage hero.
6. Keep line-height compact: `1.1em` for display and `1.2em` for normal text are part of the product-tool density.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (5 steps)
<!-- framer/token derived -->

| Token | Hex |
|---|---|
| `--warp-bg-dark` | `#121212` |
| `--warp-surface-cream` | `#FAF9F5` |
| `--warp-surface-cream-alt` | `#FAF9F6` |
| `--warp-text-primary-dark` | `#FFFFFFE6` |
| `--warp-text-link-light` | `#232224` |

### 06-2. Brand Dark Variant
<!-- SOURCE: auto+manual -->

| Token | Hex |
|---|---|
| `--framer-text-color` | `#FFFFFFE6` |
| `--border-color` | `#FFFFFF29` |
| `--framer-input-background` | `#FFFFFF0D` |
| `--framer-input-border-color` | `#87878700` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light / warm | Dark / charcoal |
|---|---|---|
| 0 | `#FFFFFF` | `#000000` |
| 50 | `#FAF9F6` | `#121212` |
| 100 | `#FAF9F5` | `#1A1A1A` |
| 200 | `#E3E2E0` | `#232224` |
| 300 | `#AFAEAC` | `#2B2B2B` |
| 400 | `#868584` | `#353534` |
| 500 | `#666469` | `#454545` |
| 600 | `#999999` | `#000000` |

### 06-4. Accent Families
<!-- SOURCE: auto+manual -->

| Family | Key step | Hex |
|---|---|---|
| Cream CTA | primary control | `#FAF9F5` |
| White overlay | translucent text/surface | `#FFFFFFE6` |
| Soft border | dark hairline | `#FFFFFF29` |
| Input fill | dark translucent field | `#FFFFFF0D` |

### 06-5. Semantic
<!-- SOURCE: auto+manual -->

| Token | Hex | Usage |
|---|---|---|
| `surface.page` | `#121212` | Global body and hero stage |
| `surface.control` | `#FAF9F5` | Download button and announcement material |
| `text.primary.dark` | `#FFFFFFE6` | Hero and dark-section readable text |
| `text.muted.dark` | `#AFAEAC` | Secondary copy and subdued labels |
| `text.on.control` | `#232224` | Dark text on cream button |
| `border.dark.soft` | `#FFFFFF29` | Low-contrast dark hairlines |
| `field.dark` | `#FFFFFF0D` | Dark input background |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--framer-text-color` | `#FFFFFFE6` | Default text in dark surfaces |
| `--framer-link-current-text-color` | `#232224` | Current/link text on light material |
| `--framer-link-text-color` | `#868584` | Muted links |
| `--framer-input-font-color` | `#FFFFFF` | Input text |
| `--framer-input-placeholder-color` | `#999999` | Placeholder |
| `--border-color` | `#FFFFFF29` | Dark border token |
| `--k346qs` | `#FAF9F5` | Warm cream surface token |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---|---:|
| raw black | `#000000` | 74 |
| warm pattern cream | `#FAF9F6` | 33 |
| white | `#FFFFFF` | 10 |
| warm surface | `#FAF9F5` | 6 |
| translucent white text | `#FFFFFFE6` | 6 |
| body dark | `#121212` | 4 |
| placeholder gray | `#999999` | 4 |
| deep charcoal | `#1A1A1A` | 2 |
| link ink | `#232224` | 2 |
| muted warm gray | `#AFAEAC` | 2 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.page-dark}` (#121212)** — The stage floor. This is the most important correction for Warp: current homepage reproduction should start in dark mode, not cream. Use it for body, hero, nav, and large dark sections.

**`{colors.surface-cream}` (#FAF9F5)** — Warm control material. It makes the Download button and announcement strip feel physical without turning the whole page beige.

**`{colors.text-primary-dark}` (#FFFFFFE6)** — Soft white, not harsh white. The alpha-like off-white keeps the huge H1 readable without making the black stage brittle.

**`{colors.text-link-light}` (#232224)** — The ink used when text sits on cream/light UI. It is warmer and softer than pure black, which keeps light controls consistent with the dark-site tone.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `space-nav-x` | `30px` | Logo/nav left start in desktop screenshot |
| `space-nav-gap` | `28px` | Main navigation rhythm |
| `space-hero-top` | `104px` | Nav-to-H1 breathing room |
| `space-product-gap` | `20px` | Gap between paired product panels |
| `space-card-copy` | `12px` | Title-to-description spacing |
| `space-section-y` | `80px` | Marketing section vertical rhythm |
| `space-container` | `min(78vw, 990px)` | Hero content and product-pair width |

**주요 alias**:
- `--warp-hero-gap` → `56px` (H1 to product selector row)
- `--warp-card-gap` → `20px` (Terminal/Oz panels)

### Whitespace Philosophy
<!-- SOURCE: manual -->

Warp uses whitespace as a stage cue, not as airy lifestyle branding. The top announcement is compressed, the nav is compact, and then the hero gives the H1 a large centered field before the product cards appear. That rhythm says "tool, not brochure" while still giving the core claim room to land.

Below the H1, spacing tightens into a two-product operating surface. The cards are wide and image-led, but the copy above each card is compact. This contrast is intentional: broad claim first, dense product proof immediately after.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `--warp-radius-button-small` | `5px` | Cream Download button |
| `--warp-radius-button-outline` | `6px` | Dark outlined Sign Up button |
| `--warp-radius-chip` | `8px` | Small UI group / badge candidate |
| `--warp-radius-card-soft` | `10px` | Secondary container candidate |
| `--warp-radius-media` | `20px` | Product screenshot cards |
| `inherit` | inherited | Framer nested image wrappers |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| Chrome | `none` | Nav, hero text, and main controls do not rely on shadow |
| Media depth | image contrast only | Product panels read through screenshot imagery, not elevation |
| Input focus | `var(--framer-input-focused-box-shadow, var(--framer-input-box-shadow))` | Available in Framer form surface, value not resolved in phase1 |

Warp's page avoids the common SaaS floating-card shadow stack. Use contrast, image edges, and radius first. If a shadow is necessary in an implementation, keep it local to media or overlays and avoid applying it to every card.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `--framer-will-change-override` | `transform` | Framer animation/performance hint |
| `--framer-will-change-filter-override` | `filter` | Framer animation/performance hint |
| Link hover | color/decoration variable swap | Navigation and rich text links |

Observed CSS contains Framer motion hooks but the phase1 reuse does not include interaction recordings. Treat motion as restrained: small hover changes and possible Framer section transitions, not large bouncing or parallax unless verified in a live browser pass.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: approximately `990px` for the hero product-pair cluster in the screenshot.
- **Grid type**: centered single-column claim, then two-column product grid.
- **Column count**: 2 for desktop product cards.
- **Gutter**: about `20px` between media cards.

### Hero
- **Pattern Summary**: `dark full-width stage + centered tight H1 + paired product cards`.
- Layout: Announcement strip, top nav, centered hero headline, then two product modules.
- Background: `#121212` solid.
- **Background Treatment**: solid dark, with product image panels providing color and glow.
- H1: `clamp(48px, 5.5vw, 80px)` / weight `400` / tracking `-0.04em`.
- Max-width: about `720px` for headline; about `990px` for product modules.

### Section Rhythm
```css
section {
  padding: 80px 24px;
  max-width: 1120px;
  margin-inline: auto;
}
```

### Card Patterns
- **Card background**: image/screenshot surface; no generic white content card in hero.
- **Card border**: none visible on the two hero media cards.
- **Card radius**: `20px`.
- **Card padding**: copy sits outside/above media, not inside a padded card shell.
- **Card shadow**: none visible; depth comes from screenshot content and dark contrast.

### Navigation Structure
- **Type**: horizontal desktop nav with logo left, product/resource dropdown labels, CTA right.
- **Position**: top, under announcement bar.
- **Height**: around `72px`.
- **Background**: `#121212`.
- **Border**: none visible; separation comes from color boundary with the cream announcement strip.

### Content Width
- **Prose max-width**: `640px`.
- **Container max-width**: `1120px`.
- **Sidebar width**: N/A on homepage hero.

---

## 12. Responsive Behavior
<!-- SOURCE: manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `<= 767px` | Expected Framer single-column collapse |
| Tablet | `768px` | Product cards likely stack or compress |
| Desktop | `1024px` | Two-column product hero becomes stable |
| Large | `1200px` | Screenshot-matched desktop layout |

### Touch Targets
- **Minimum tap size**: `44px` recommended; CTA appears around 40px tall on desktop.
- **Button height (mobile)**: target `44px`.
- **Input height (mobile)**: unresolved; Framer input variables exist but no mobile form state was captured.

### Collapsing Strategy
- **Navigation**: desktop horizontal nav should collapse to menu on mobile.
- **Grid columns**: product cards collapse from 2 columns to 1.
- **Sidebar**: N/A for homepage.
- **Hero layout**: centered H1 remains; paired Terminal/Oz modules stack vertically.

### Image Behavior
- **Strategy**: media cards crop screenshots inside rounded containers.
- **Max-width**: fill card width.
- **Aspect ratio handling**: fixed visual ratio with overflow hidden and large radius.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Download Button**

| Property | Value |
|---|---|
| Background | `#FAF9F5` |
| Text | `#232224` / near-black |
| Radius | `5px` |
| Height | about `40px` |
| Padding | `12px 18px` |
| Font | Matter/Inter, `500` |

```html
<a class="warp-button warp-button-download">Download for Mac</a>
```

**Outline Sign Up Button**

| Property | Value |
|---|---|
| Background | `transparent` |
| Text | `#FFFFFFE6` |
| Border | `1px solid #FFFFFF` |
| Radius | `6px` |
| Padding | `10px 14px` |

```html
<a class="warp-button warp-button-outline">Sign Up</a>
```

### Badges

The hero does not use decorative badge pills. The top announcement bar is the closest badge-like surface: a full-width warm strip with compact centered copy and an underlined "Learn more." link.

```html
<div class="warp-announcement">
  Introducing first-class support for Claude Code, Codex, Gemini CLI and OpenCode.
  <a>Learn more.</a>
</div>
```

### Cards & Containers

**Product Media Card**

| Property | Value |
|---|---|
| Background | screenshot image / product UI |
| Radius | `20px` |
| Border | none visible |
| Shadow | none |
| Overflow | hidden |
| Width | about `486px` each on desktop screenshot |

```html
<article class="warp-product">
  <header>
    <h3>Warp Terminal</h3>
    <p>A modern terminal for agentic coding</p>
  </header>
  <figure class="warp-product-media">
    <img src="terminal-screenshot.webp" alt="">
  </figure>
</article>
```

### Navigation

Desktop nav has three zones: logo at left, product/resource links in the center-left, and action links on the right. It does not use a visible bordered header shell.

```html
<nav class="warp-nav">
  <a class="warp-logo">warp</a>
  <a>Products</a>
  <a>Oz</a>
  <a>Resources</a>
  <a>Pricing</a>
  <a>Careers</a>
  <a>Enterprise</a>
  <span class="warp-nav-spacer"></span>
  <a>Contact sales</a>
  <a class="warp-button-download">Download for Mac</a>
</nav>
```

### Inputs & Forms

Framer input variables exist even though the hero does not show a form:

| Token | Value |
|---|---|
| `--framer-input-background` | `#FFFFFF0D` |
| `--framer-input-border-color` | `#87878700` |
| `--framer-input-font-color` | `#FFFFFF` |
| `--framer-input-placeholder-color` | `#999999` |
| `--framer-input-icon-color` | `#999999` |

Use these only for dark-form surfaces; do not infer a light form system from the hero.

### Hero Section

The hero is a product selector disguised as a launch statement. It starts with one large line-broken H1, then splits into two product promises:

- **Warp Terminal** — local/terminal coding product, with "Learn More" and "Download for Mac".
- **Oz** — cloud-agent orchestration product, with "Learn More" and "Sign Up".

The two cards are equal citizens. Avoid making one a tiny secondary feature card unless a later section explicitly does that.

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-download** — Cream filled CTA for primary desktop install action.

| Property | Value |
|---|---|
| bg | `#FAF9F5` |
| color | `#232224` |
| radius | `5px` |
| role | high-confidence primary action |

**button-outline-dark** — Dark-stage secondary signup action.

| Property | Value |
|---|---|
| bg | `transparent` |
| color | `#FFFFFFE6` |
| border | `1px solid #FFFFFF` |
| radius | `6px` |
| role | cloud product signup next to Oz |

**announcement-bar** — Warm full-width status strip.

| Property | Value |
|---|---|
| bg | `#FAF9F5` / `#FAF9F6` |
| color | `#666469` |
| link | underlined dark gray |
| role | current product/platform announcement |

**product-card-media** — Large rounded screenshot container.

| Property | Value |
|---|---|
| radius | `20px` |
| border | none |
| shadow | none visible |
| role | product proof surface |

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

#### dark-stage-cream-control

```yaml
dark-stage-cream-control:
  description: "Warp splits the page into 'stage' (dark) and 'control' (cream) materials — never one continuous floor."
  technique: "body/nav at #121212; CTA buttons and top announcement bar at #FAF9F5 (warm cream); ratio enforced ~80:20."
  applied_to: ["{component.page-surface}", "{components.button-primary}", "{component.top-announcement}", "Download button"]
  visual_signature: "terminal seriousness without retro green-on-black — the cream patches read like physical buttons on a black machine."
  intent: "developer-tool brands need to feel serious; cream actions stop the page from collapsing into nightclub black."
```

#### matter-tight-display

```yaml
matter-tight-display:
  description: "The hero compresses by optics, never by weight."
  technique: "Matter (or close substitute) at font-weight 400, line-height 1.1em, letter-spacing -0.04em on H1; never 600+."
  applied_to: ["{typography.h1}", "main hero statement", "large marketing claim"]
  visual_signature: "the headline feels engineered, not inflated — a calm declaration on a serious machine."
  intent: "agentic-coding tools must whisper, not shout; bold display weight would feel consumer-SaaS."
```

#### paired-product-theater

```yaml
paired-product-theater:
  description: "Two product surfaces are staged as equal panels under one claim — Warp Terminal + Oz."
  technique: "two-column grid, equal card widths, 20px media radius, copy block sits OUTSIDE the screenshot shell so each product photo stays unaltered."
  applied_to: ["Warp Terminal hero module", "Oz hero module", "{component.dual-product-block}"]
  visual_signature: "product strategy is legible in the layout itself — two pillars, never a hero + sidekick."
  intent: "a multi-product company must visually commit to both; offset sizing would imply hierarchy and split the brand."
```

#### shadowless-media-depth

```yaml
shadowless-media-depth:
  description: "Depth comes from screenshot imagery and edge radius — never from card shadows."
  technique: "no box-shadow on hero cards; overflow-hidden image panels with 20px radius sit directly on the dark floor."
  applied_to: ["{component.product-media-card}", "demo panel", "screenshot frame"]
  visual_signature: "crisp demo panels that look milled into the page, not floating SaaS cards."
  intent: "shadow on dark surfaces always reads as gloss; Warp's promise is engineering precision, so depth must be earned by content."
```

#### monospace-as-brand-not-code

```yaml
monospace-as-brand-not-code:
  description: "Warp uses monospace as a brand voice, not just inside code blocks."
  technique: "Berkeley Mono (or fallback IBM Plex Mono) used for nav labels, eyebrow tags, and CTA secondary text — not just `<pre>`."
  applied_to: ["{typography.eyebrow}", "{component.nav-label}", "secondary CTA text"]
  visual_signature: "the chrome itself speaks 'terminal' — the tool's worldview leaks into the marketing page."
  intent: "developer tools earn trust by living in the fixture (mono); using mono only for code would feel like decoration."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Category-defining, direct, product-led | "Warp is the agentic development environment" |
| Primary CTA | Specific platform/action | "Download for Mac" |
| Secondary CTA | Enterprise/sales motion kept plain | "Contact sales" |
| Subheading | Functional product promise | "A modern terminal for agentic coding" |
| Tone | Developer-infrastructure confidence, not playful consumer SaaS | "The orchestration platform for cloud agents" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Warp — copy into your root stylesheet */
:root {
  /* Fonts */
  --warp-font-family: "Matter Regular", "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
  --warp-font-family-code: "Geist Mono", "Fragment Mono", "DM Mono", ui-monospace, monospace;
  --warp-font-weight-normal: 400;
  --warp-font-weight-medium: 500;
  --warp-font-weight-bold: 700;

  /* Brand / surfaces */
  --warp-color-brand-25:  #FAF9F6;
  --warp-color-brand-300: #E3E2E0;
  --warp-color-brand-500: #AFAEAC;
  --warp-color-brand-600: #FAF9F5;   /* canonical control surface */
  --warp-color-brand-900: #232224;

  /* Surfaces */
  --warp-bg-page:    #121212;
  --warp-bg-dark:    #121212;
  --warp-bg-control: #FAF9F5;
  --warp-text:       #FFFFFFE6;
  --warp-text-muted: #AFAEAC;
  --warp-text-on-control: #232224;
  --warp-border-soft: #FFFFFF29;

  /* Key spacing */
  --warp-space-sm:  12px;
  --warp-space-md:  20px;
  --warp-space-lg:  56px;
  --warp-space-xl:  80px;

  /* Radius */
  --warp-radius-button: 5px;
  --warp-radius-outline: 6px;
  --warp-radius-media: 20px;
}

body {
  margin: 0;
  background: var(--warp-bg-page);
  color: var(--warp-text);
  font-family: var(--warp-font-family);
  font-weight: var(--warp-font-weight-normal);
}

.warp-hero-title {
  font-size: clamp(48px, 5.5vw, 80px);
  line-height: 1.1em;
  letter-spacing: -0.04em;
  font-weight: 400;
  color: var(--warp-text);
}

.warp-button-download {
  background: var(--warp-bg-control);
  color: var(--warp-text-on-control);
  border-radius: var(--warp-radius-button);
  padding: 12px 18px;
  font-weight: 500;
}

.warp-product-media {
  border-radius: var(--warp-radius-media);
  overflow: hidden;
  box-shadow: none;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Warp
module.exports = {
  theme: {
    extend: {
      colors: {
        warp: {
          page: '#121212',
          cream: '#FAF9F5',
          creamAlt: '#FAF9F6',
          text: '#FFFFFFE6',
          muted: '#AFAEAC',
          ink: '#232224',
          border: '#FFFFFF29',
          input: '#FFFFFF0D',
        },
      },
      fontFamily: {
        sans: ['Matter Regular', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['Geist Mono', 'Fragment Mono', 'DM Mono', 'ui-monospace'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
        bold: '700',
        black: '900',
      },
      borderRadius: {
        warpButton: '5px',
        warpOutline: '6px',
        warpMedia: '20px',
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
| Brand primary | `--warp-bg-control` | `#FAF9F5` |
| Background | `--warp-bg-page` | `#121212` |
| Text primary | `--warp-text` | `#FFFFFFE6` |
| Text muted | `--warp-text-muted` | `#AFAEAC` |
| Border | `--warp-border-soft` | `#FFFFFF29` |
| Success | N/A | N/A |
| Error | N/A | N/A |

### Example Component Prompts

#### Hero Section
```text
Warp 스타일 히어로 섹션을 만들어줘.
- 배경: #121212
- H1: Matter Regular, clamp(48px, 5.5vw, 80px), weight 400, tracking -0.04em, line-height 1.1em
- 서브텍스트: #AFAEAC, 16px
- CTA 버튼: 배경 #FAF9F5, 텍스트 #232224, radius 5px, padding 12px 18px
- 구조: 중앙 H1 아래 Warp Terminal / Oz 두 개의 동등한 제품 카드
- 카드: media radius 20px, shadow none, screenshot image가 깊이를 담당
```

#### Card Component
```text
Warp 스타일 제품 카드 컴포넌트를 만들어줘.
- 배경: 카드 shell을 만들지 말고 어두운 #121212 위에 copy와 media를 배치
- media: border-radius 20px, overflow hidden, shadow none
- 제목: Matter Regular, 24px, weight 400, color #FFFFFFE6
- 본문: 16px, color #AFAEAC, line-height 1.2em
- hover 시: 큰 transform 대신 링크/버튼 상태만 절제해서 변경
```

#### Badge
```text
Warp 스타일 announcement bar를 만들어줘.
- full width, background #FAF9F5
- text #666469, 14-16px, centered
- link는 같은 줄에서 underline 처리
- pill badge처럼 둥글게 만들지 말 것
```

#### Navigation
```text
Warp 스타일 상단 네비게이션을 만들어줘.
- 높이: 약 72px, 배경 #121212, border 없음
- 로고: 좌측, 흰색
- 링크: Matter/Inter, 16px, weight 500, color #FFFFFFE6 또는 muted gray
- 우측: Contact sales 텍스트 링크 + #FAF9F5 Download button
- nav 위에는 #FAF9F5 announcement bar 배치
```

### Iteration Guide

- **색상 변경 시**: `#121212`와 `#FAF9F5`의 역할을 바꾸지 말 것.
- **폰트 변경 시**: Matter가 없으면 Inter를 쓰되 H1 `-0.04em` tracking은 유지.
- **여백 조정 시**: hero는 크게, product cards는 촘촘하게. 전부 같은 spacing scale로 평평하게 만들지 말 것.
- **새 컴포넌트 추가 시**: shadow보다 radius, contrast, screenshot/image material을 우선.
- **다크 모드**: 기본이 dark다. light variant를 기본값으로 간주하지 말 것.
- **반응형**: 2-column product layout은 mobile에서 반드시 1-column으로 내려야 한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- `#121212`를 global page/hero/nav background로 먼저 깔 것.
- H1은 `font-weight: 400`, `line-height: 1.1em`, `letter-spacing: -0.04em`로 압축할 것.
- `#FAF9F5`는 announcement, CTA, light product surface처럼 제한된 material에만 사용할 것.
- Product proof는 screenshot/media card로 보여주고, copy는 카드 안에 과하게 가두지 말 것.
- Media card radius는 `20px`로 크게 잡고, 버튼 radius는 `5px`/`6px`로 작게 구분할 것.
- Mono font는 code/terminal texture에만 쓰고, main marketing copy는 proportional font로 유지할 것.
- Navigation은 dark background 위에서 조용하게 두고, cream CTA만 action hierarchy를 만들게 할 것.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#121212` 사용.
- 현재 홈페이지를 전체 `#FAF9F5` cream background로 두지 말 것 — cream은 CTA/announcement에만 사용.
- 본문 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — dark surface에서는 `#FFFFFFE6` 사용.
- CTA 텍스트를 `#FFFFFF`로 두지 말 것 — cream CTA 위에는 `#232224` 사용.
- border를 진한 `#E3E2E0`로 dark card에 남발하지 말 것 — dark hairline은 `#FFFFFF29` 수준으로 얇게 사용.
- input dark surface를 opaque `#FFFFFF`로 만들지 말 것 — Framer input background는 `#FFFFFF0D`.
- H1에 `letter-spacing: 0`을 쓰지 말 것 — hero display는 `-0.04em`가 핵심.
- hero card에 generic `box-shadow: 0 20px 60px #000000`를 바르지 말 것 — media depth는 shadowless에 가깝다.
- 버튼을 전부 `border-radius: 999px` pill로 만들지 말 것 — Warp CTA는 `5px`/`6px` 계열이다.
- 전체 페이지를 monospace로 만들지 말 것 — mono는 terminal/code texture에만 제한한다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- **Retro terminal green**: none. The terminal brand does not use `#00FF00` hacker nostalgia as its UI identity.
- **Global light theme**: absent on the captured homepage. The current hero is dark-first, not cream-first.
- **Rainbow agent palette**: none in the core hero. Product differentiation happens through layout and screenshots, not many brand colors.
- **Pill-first SaaS buttons**: absent. CTA corners are small (`5px`/`6px`), while media corners are large (`20px`).
- **Heavy card elevation**: not part of the hero chrome. Media panels rely on image content and radius.
- **Decorative gradient mesh background**: not used as the main page background. Color comes from product images.
- **All-monospace branding**: absent. The site talks like a polished developer platform, not a raw CLI.
- **Dense bordered dashboard shell**: absent on the marketing hero. It shows product screenshots but does not turn the whole page into app chrome.
- **Second saturated brand color**: none established by the extracted CSS. Warm cream and dark neutrals carry the identity.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Phase1 reuse only** — This report used existing `insane-design/warp/` phase1 JSON, CSS, HTML, and hero screenshot. No fresh live browser crawl was performed in this pass.
- **Single captured surface** — The strongest observations come from the homepage hero. Pricing, docs, download modal, account flows, and enterprise pages may introduce additional component states.
- **Motion not replayed** — CSS contains Framer `will-change` hints, but scroll-triggered or interaction-driven animations were not recorded or measured.
- **Responsive behavior inferred** — Mobile stacking and navigation collapse are expected from the structure, but no mobile screenshot was inspected in this pass.
- **Semantic names are normalized** — `--warp-*` names in this guide are implementation aliases for clarity. The actual extracted CSS uses Framer variables and hashed `--token-*` identifiers.
- **Success/error colors not confirmed** — The homepage extraction did not surface a reliable form validation palette. Do not invent green/red tokens from generic UI assumptions.
- **Shadows unresolved** — Framer input shadow variables exist, but concrete values were not resolved in phase1. Hero media cards visually read as shadowless in the screenshot.
- **Logo wall contamination possible** — The frequency list includes raw black/white and SVG-pattern colors; top colors were interpreted with hero screenshot context to avoid over-weighting embedded logos.
- **Font hierarchy is mixed** — Inter appears most frequently in CSS, while Matter is the stronger visible brand display voice. Treat `primary_font` as display/brand, not the only font on the page.
