---
schema_version: 3.2
slug: robinhood
service_name: Robinhood
site_url: https://robinhood.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#CCFF00"
primary_font: Phonic
font_weight_normal: 400
token_prefix: rh

bold_direction: Electric Fintech
aesthetic_category: other
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high

archetype: landing-utility
archetype_confidence: medium
design_system_level: lv1
design_system_level_evidence: "No CSS custom properties were found; the page relies on generated CSS classes, repeated brand colors, and a consistent component grammar."

colors:
  primary: "#CCFF00"
  ink: "#110E08"
  surface: "#FFFFFF"
  muted-ink: "#35322D"
  hairline: "#888784"
  dark-utility: "#000000"

typography:
  display: "Martina Plantijn"
  body: "Phonic"
  alternate-display: "Nib Pro Display"
  ladder:
    - { token: hero-display, size: "72px", weight: 400, line_height: "78px", tracking: "-1px" }
    - { token: hero-tablet, size: "58px", weight: 400, line_height: "63px", tracking: "0" }
    - { token: hero-mobile, size: "44px", weight: 400, line_height: "48px", tracking: "-0.4px" }
    - { token: body, size: "16px", weight: 400, line_height: "24px", tracking: "-0.25px" }
    - { token: nav-small, size: "14px", weight: 400, line_height: "22px", tracking: "-0.1px" }
  weights_used: [300, 400, 500, 600, 700]
  weights_absent: [800, 900]

components:
  button-primary: { bg: "{colors.primary}", color: "{colors.ink}", radius: "36px", height: "44px", padding: "0 32px" }
  button-dark: { bg: "{colors.ink}", color: "{colors.surface}", radius: "36px", height: "44px", padding: "0 32px" }
  promo-strip: { bg: "{colors.primary}", color: "{colors.ink}", position: "sticky below 64px nav" }
---

# DESIGN.md — Robinhood (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Robinhood's marketing surface is not a quiet brokerage dashboard. It behaves like a financial product showroom with the lights turned up: black chrome navigation, acid-green signal bands, and oversized serif headlines placed next to glossy mechanical photography. The page takes the anxiety of investing and gives it a consumer-product stage.

The most important visual move is the collision between #CCFF00 (`{colors.primary}`) and #110E08 (`{colors.ink}`). The green is not a decorative accent sprinkled everywhere; it appears as a high-voltage utility layer: primary CTA, promotional strip, labels, and a few section fills. There is no second brand color waiting in the wings. Robinhood chooses one electric wire and lets the rest of the room go warm black, white, and brown-black.

The black nav and green promo strip act like the lit edge of a trading terminal before the showroom opens. It is not a bank lobby with marble trust cues; it is closer to a consumer electronics counter where the price tag, power cable, and product demo are all visible at once. The acid-green band behaves like a market ticker stripped of numbers: a signal layer, not decoration.

Typography is split into two voices. Display moments use Martina Plantijn at 72px / 78px, a serif that makes retirement and finance feel editorial rather than purely transactional. Product copy, nav, and controls use Phonic, a compact sans face that keeps the interface direct and plain. That contrast is the site: magazine cover promise above, brokerage app control below.

Photography carries the depth that many fintech sites would fake with blue gradients or floating cards. Shadow does not become a universal UI language here; the chrome stays flat while the product/mechanical imagery does the theatrical work. The hero image reads like machinery behind glass, with `{colors.primary}` acting as the warning label on the case.

The homepage avoids the usual fintech blue trust palette. It chooses a sharper identity: almost hazardous green, warm black, and hard-edged product language. It looks less like a bank and more like an access terminal for a consumer investing machine: no soft trust-blue, no confetti accent set, no friendly pastel portfolio illustrations.

### Key Characteristics

- Acid green #CCFF00 (`{colors.primary}`) is the single unmistakable brand signal.
- Warm near-black #110E08 (`{colors.ink}`) replaces pure black for most dark text and dark CTAs.
- Hero display type uses a serif face, not the body sans, giving finance copy an editorial weight.
- Navigation is a black 64px utility bar with white links and a green outline login/action rhythm.
- CTA buttons are 44px high capsules with 36px radius and very little ornament.
- The page uses real product/financial imagery rather than abstract SaaS gradients.
- Body copy stays compact: 16px / 24px with slight negative tracking.
- Section changes are driven by color field shifts, not heavy shadows or card chrome.
- Generated class CSS is consistent, but no reusable CSS variable token layer was found.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Electric Fintech
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **acid-green brokerage showroom hero**으로 기억된다.
> **Code Complexity**: medium — generated CSS classes, responsive media blocks, sticky promo/nav layers, and image-led hero composition without a full public token API.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Robinhood처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Phonic", Helvetica, system-ui, -apple-system, BlinkMacSystemFont, Arial, sans-serif;
  font-weight: 400;
  letter-spacing: -0.25px;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #110E08; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #CCFF00; }
.rh-primary {
  background: var(--brand);
  border: 1px solid var(--brand);
  color: #110E08;
  border-radius: 36px;
  height: 44px;
  padding: 0 32px;
}
```

**절대 하지 말아야 할 것 하나**: Robinhood를 generic fintech blue로 만들지 말 것. 이 페이지의 중심은 `#CCFF00` green + `#110E08` warm ink + serif hero display의 조합이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://robinhood.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | reused local phase1 artifacts |
| HTML size | 260,729 bytes |
| CSS files | 1 inline CSS file, 72,036 chars |
| Token prefix | `rh` (analysis alias only; no CSS custom property prefix found) |
| Method | phase1 JSON + inline CSS + screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next-style generated asset build, inferred from `_next/static/fonts` asset paths.
- **Design system**: private/generated Robinhood brand CSS; no public custom-property token layer surfaced in the captured CSS.
- **CSS architecture**: generated atomic-ish classes with Emotion-like `css-*` selectors.
  ```text
  generated class       (.css-rhrgcq, .css-1w13sxb)   concrete declarations
  repeated values       (#CCFF00, #110E08, 36px)       implicit design tokens
  component grammar     buttons/nav/promo/hero         inferred from recurring declarations
  ```
- **Class naming**: hashed `.css-*` selectors, not semantic BEM or utility classes.
- **Default theme**: mixed; white content surfaces and dark utility navigation, with acid-green promo/action fields.
- **Font loading**: `@font-face` from `cdn.robinhood.com/assets/generated_assets/brand/_next/static/fonts/`.
- **Canonical anchor**: the desktop hero screenshot: black nav, green promo strip, serif IRA headline, mechanical/gold image crop.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Martina Plantijn` for the captured hero headline.
- **Primary UI/body font**: `Phonic`, with Helvetica/system fallbacks.
- **Additional brand fonts found**: `Capsule Sans Text`, `Capsule Sans Display`, `Nib Pro Display`, `Geist`, `ITC Garamond Std`, `Instrument Serif`, `Maison Neue Extended`.
- **Code font**: `Capsule Sans Text Mono` was present in font declarations, but not observed as a homepage UI primitive.
- **Weight normal / bold**: `400` / `700`; medium `500`, light `300`, and one `600` usage were also present.

```css
:root {
  --rh-font-family:       "Phonic", Helvetica, system-ui, -apple-system, BlinkMacSystemFont, Arial, sans-serif;
  --rh-font-family-display: "Martina Plantijn", serif;
  --rh-font-family-code:  "Capsule Sans Text Mono", ui-monospace, monospace;
  --rh-font-weight-normal: 400;
  --rh-font-weight-bold:   700;
}
body {
  font-family: var(--rh-font-family);
  font-weight: var(--rh-font-weight-normal);
}
.rh-hero-title {
  font-family: var(--rh-font-family-display);
  font-size: 72px;
  line-height: 78px;
  letter-spacing: -1px;
}
```

### Note on Font Substitutes

- **Phonic** is a proprietary Robinhood brand sans. Use **Inter** only as a fallback at `400`, with `letter-spacing: -0.25px` on body-sized copy to recover the compactness. Do not use Inter's default roomy tracking.
- **Martina Plantijn** drives the hero's editorial feel. If unavailable, use **Fraunces** or **Source Serif 4** at `400`, then tighten large headlines to about `-1px` and keep line-height close to `1.08`.
- **Capsule Sans Display/Text** should not be substituted blindly across the entire page. The captured homepage uses Phonic more frequently; use Capsule only where matching a legacy Robinhood app surface.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| hero-display-desktop | 72px | 400 | 78px | -1px |
| hero-display-tablet | 58px | 400 | 63px | 0 |
| hero-display-mobile | 44px | 400 | 48px | -0.4px |
| section-title-large | 58px | 400 | 63px | -1px to 0 |
| section-title-medium | 44px | 400 | 48px | -0.4px |
| body-default | 16px | 400 | 24px | -0.25px |
| nav/body-small | 14px | 400 | 22px | -0.1px |
| microcopy | 12px | 400 | 18px | -0.1px |

> ⚠️ The key insight is contrast, not weight. Robinhood lets `400` carry both huge serif hero text and normal body copy, then changes the font family and tracking to create hierarchy.

### Principles

1. Hero type is serif and large, but not heavy. The 72px desktop headline stays at weight 400, which keeps the financial offer from becoming shouty.
2. Body copy uses Phonic at 16px / 24px with `-0.25px` tracking. Without the negative tracking, the page loses its compact brokerage feel.
3. Weight 500 is present but secondary. It should mark navigation emphasis or controls, not become the default body style.
4. Mobile typography compresses by size and line-height, not by changing tone: 72px / 78px becomes 44px / 48px.
5. The page accepts multiple brand fonts, but a faithful recreation should preserve the split: serif for the high-value promise, Phonic for action and explanation.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (1 confirmed anchor)

| Token | Hex |
|---|---|
| rh-color-brand-primary | #CCFF00 |

### 06-3. Neutral Ramp

| Step | Light / Surface | Dark / Ink |
|---|---|---|
| surface-base | #FFFFFF | #000000 |
| ink-primary | #110E08 | #110E08 |
| ink-secondary | #35322D | #4D4A46 |
| muted-ui | #888784 | #808080 |
| hairline-light | #D9D9D9 | #BFBFBF |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| robinhood-green | primary | #CCFF00 |
| warm-brown-black | deep accent | #1C180D |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| rh-action-primary | #CCFF00 | primary CTA, promo strip, label accents |
| rh-text-primary | #110E08 | page text and green-surface foreground |
| rh-surface-base | #FFFFFF | white buttons, content surfaces |
| rh-nav-bg | #000000 | top navigation chrome |
| rh-border-muted | #35322D | border and divider roles in captured CSS |
| rh-text-muted | #888784 | secondary microcopy and subdued UI |

### 06-6. Semantic Alias Layer

> N/A — phase1 found zero CSS custom properties and no resolvable alias layer. The aliases in this guide are analysis names for implementation convenience, not source CSS token names.

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| surface-base | #FFFFFF | 31 |
| ink-primary | #110E08 | 24 |
| ink-secondary | #35322D | 22 |
| brand-primary | #CCFF00 | 17 |
| dark-utility | #000000 | 9 |
| muted-ui | #888784 | 4 |
| brown-black | #1C180D | 2 |
| divider-light | #D9D9D9 | 2 |
| divider-mid | #BFBFBF | 2 |

### 06-8. Color Stories

**`{colors.primary}` (#CCFF00)** — Robinhood's electric green is the action and announcement color. It appears on the primary CTA, the sticky promo strip, and select labels; do not dilute it into pastel green.

**`{colors.ink}` (#110E08)** — Warm ink, not generic black. It gives the green surfaces a slightly physical, almost oil-black contrast that matches the mechanical hero imagery.

**`{colors.surface}` (#FFFFFF)** — White is the neutral floor for utility and content. It should stay plain; photography and green action fields provide the energy.

**`{colors.muted-ink}` (#35322D)** — The muted border/secondary ink color keeps dark separators warmer than gray. It is useful for dividers, fine print, and lower-emphasis copy.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| rh-space-zero | 0 | nav resets, generated layout resets |
| rh-space-xs | 10px | promo strip vertical/horizontal micro padding |
| rh-space-sm | 20px | promo strip horizontal padding |
| rh-space-md | 24px | content padding, bordered rows |
| rh-space-lg | 32px | CTA horizontal padding |
| rh-space-xl | 64px | nav height reference and major vertical rhythm |
| rh-space-hero | 250px / 600px / 800px | responsive image/hero spacer heights found in CSS |

**주요 alias**:
- `rh-space-button-x` → 32px (capsule CTA horizontal padding)
- `rh-space-nav-h` → 64px (desktop nav bar height)
- `rh-space-content` → 24px (content row/card padding)

### Whitespace Philosophy

Robinhood uses spacing as a product-pitch rhythm: a dense 64px black nav, a thin electric promo bar, then a large hero image field. The page does not feel airy in an Apple sense; it feels staged, with the hero copy occupying the left and the product/mechanical image taking the right.

Within controls, space is compressed and utilitarian. Buttons use 44px height and 32px horizontal padding, which makes them easy to tap without turning into oversized SaaS pills. Content rows and bordered modules prefer 24px padding, reinforcing a financial-product density below the hero.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| rh-radius-pill | 36px | primary and secondary capsule buttons |
| rh-radius-tight | 3px | small dots / compact UI elements |

The radius system is intentionally sparse. Robinhood's signature button is a capsule, while structural surfaces stay mostly rectangular or image-led.

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| chrome-shadow | N/A | No dominant UI shadow token surfaced in captured inline CSS |
| image-depth | photographic | hero depth is carried by product imagery, not CSS elevation |

Shadow is not a primary identity layer in the captured homepage. Recreate depth with image composition and section contrast rather than generic card shadows.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| rh-hover-opacity | opacity: 0.85 | CTA hover feedback |
| transition-system | N/A | No recurring transition shorthand surfaced in the CSS summary |

Motion should be minimal and functional. The observed button hover is an opacity reduction, not a lift, bounce, glow, or shadow animation.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: mixed; image and hero elements use `100%`, `90%`, and `75%` constraints in generated rules.
- **Grid type**: primarily Flexbox; only one `display: grid` occurrence surfaced in the CSS summary.
- **Column count**: hero behaves like a split composition on desktop: left editorial copy, right image crop.
- **Gutter**: component-level gaps and padding rather than an exposed 12-column system.

### Hero

- **🆕 Pattern Summary**: `large image-led hero + left serif H1 + green promo strip + capsule CTA`.
- Layout: desktop split hero; text column sits left while mechanical/gold imagery occupies the right and background.
- Background: photographic/product image with muted blue-gray field in the screenshot; CSS identity still centers on `#FFFFFF`, `#110E08`, and `#CCFF00`.
- **🆕 Background Treatment**: image-led hero with no generic gradient mesh; the captured CSS also contains a `linear-gradient(to top, #CCFF00 0px, #CCFF00 80px, transparent 80px)` treatment for a green-backed section.
- H1: `72px` / weight `400` / tracking `-1px` on desktop.
- Max-width: text column visually sits under 50% of the viewport; generated CSS includes `75%`, `90%`, and `100%` max-width values.

### Section Rhythm

```css
section {
  padding: 24px;
  max-width: 100%;
}
.rh-nav { height: 64px; }
.rh-promo { position: sticky; top: 64px; padding: 10px 20px; }
```

### Card Patterns

- **Card background**: #FFFFFF or section-defined color.
- **Card border**: #35322D appears as a 1px row/divider border.
- **Card radius**: no broad card-radius system found; buttons carry the visible radius.
- **Card padding**: 24px in bordered row/container snippets.
- **Card shadow**: no signature card shadow observed.

### Navigation Structure

- **Type**: horizontal desktop nav with dropdown affordances and right-side account/actions.
- **Position**: fixed-like top shell in screenshot; CSS includes sticky promo under the 64px nav.
- **Height**: 64px.
- **Background**: #000000.
- **Border**: none dominant; contrast comes from black field and green outline/action.

### Content Width

- **Prose max-width**: not exposed as a named token; hero copy visually about 560-640px.
- **Container max-width**: generated rules include `100%`, `90%`, `75%`.
- **Sidebar width**: N/A for homepage.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | max-width: 425px | hero type compresses to 44px / 48px |
| Small tablet | min-width: 426px and max-width: 767px | intermediate mobile/tablet layout bucket |
| Tablet | min-width: 768px | many flex/layout rules activate |
| Tablet band | min-width: 768px and max-width: 1023px | dedicated tablet sizing bucket |
| Desktop | min-width: 1024px | desktop nav and hero sizing activate |
| Large | min-width: 1280px | wider desktop refinements |

### Touch Targets

- **Minimum tap size**: primary buttons observed at 44px height, meeting the common touch target floor.
- **Button height (mobile)**: 44px pattern should be preserved unless CSS proves a smaller local variant.
- **Input height (mobile)**: not observed in the captured homepage analysis.

### Collapsing Strategy

- **Navigation**: desktop horizontal nav; CSS includes desktop-only visibility toggles at `1024px`, implying a separate mobile nav pattern.
- **Grid columns**: hero and image blocks collapse through breakpoint-specific heights and max-widths rather than a public grid API.
- **Sidebar**: N/A.
- **Hero layout**: 72px desktop headline becomes 58px tablet and 44px mobile.

### Image Behavior

- **Strategy**: hero photography/product image carries the visual drama.
- **Max-width**: `100%`, `90%`, and `75%` surfaced in CSS.
- **Aspect ratio handling**: fixed responsive heights such as 800px / 600px / 250px appear in generated rules.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

Primary capsule:

```html
<a class="rh-button rh-button-primary">Get started</a>
```

| Property | Value |
|---|---|
| display | inline-flex |
| height | 44px |
| padding | 0 32px |
| radius | 36px |
| background | #CCFF00 |
| border | 1px solid #CCFF00 |
| color | #110E08 |
| hover | opacity: 0.85 |

Dark capsule:

```html
<a class="rh-button rh-button-dark">Get started</a>
```

| Property | Value |
|---|---|
| background | #110E08 |
| border | 1px solid #110E08 |
| color | #FFFFFF |
| radius | 36px |
| height | 44px |

White capsule:

```html
<a class="rh-button rh-button-white">Learn more</a>
```

| Property | Value |
|---|---|
| background | #FFFFFF |
| border | 1px solid #FFFFFF |
| color | #000000 |
| radius | 36px |
| height | 44px |

### Badges

No standalone pill badge system was observed. Badge-like roles should reuse the green/ink pairing and Phonic 14px or 12px copy. Avoid inventing multicolor status chips.

### Cards & Containers

Containers are restrained:

```css
.rh-bordered-row {
  border-color: #35322D;
  border-style: solid;
  border-width: 1px 0;
  padding: 24px;
}
```

Use borders and section backgrounds before shadows. Cards should not become rounded floating panels unless the source flow specifically shows that treatment.

### Navigation

```html
<nav class="rh-nav">
  <a class="rh-logo">Robinhood</a>
  <a>What We Offer</a>
  <a>Crypto</a>
  <a>Predict</a>
  <a>Strategies</a>
  <a>Gold</a>
  <a>Legend</a>
  <a>Learn</a>
  <a>Support</a>
  <a class="rh-login">Log in</a>
</nav>
```

| Property | Value |
|---|---|
| height | 64px |
| background | #000000 |
| link color | #FFFFFF |
| nav type | horizontal desktop |
| action rhythm | outline/green account action at right |

### Inputs & Forms

Homepage input states were not surfaced in the captured phase1 artifacts. For faithful extension, use Phonic, 44px minimum height, #35322D or #D9D9D9 hairline borders, and #CCFF00 only for focused primary action, not every input border.

### Hero Section

```html
<section class="rh-hero">
  <h1>Gear up your IRA<br />with a 2% match</h1>
  <p>With Robinhood Gold ($5/month), earn a 2% match...</p>
  <a class="rh-button rh-button-dark">Get started</a>
</section>
```

| Property | Value |
|---|---|
| headline font | Martina Plantijn |
| headline desktop | 72px / 78px / 400 / -1px |
| body font | Phonic |
| CTA | dark capsule or green capsule depending section |
| image | right-side mechanical/gold product imagery |

### 13-2. Named Variants

`button-primary-green`
: #CCFF00 background, #110E08 text, 36px radius, 44px height. Used for primary account/action CTAs.

`button-dark-capsule`
: #110E08 background, #FFFFFF text, same geometry. Used when the surrounding field is light or image-led.

`button-white-capsule`
: #FFFFFF background, #000000 text. Useful on dark or image-heavy surfaces.

`promo-strip-green`
: sticky #CCFF00 announcement band with #110E08 text, 10px 20px padding, positioned below the 64px nav.

### 13-3. Signature Micro-Specs

```yaml
acid-green-utility-layer:
  description: "Robinhood treats brand green as infrastructure, not accent decoration."
  technique: "background #CCFF00 /* {colors.primary} */ with foreground #110E08 /* {colors.ink} */ on CTA fills, promo strips, labels, and selected section fields"
  applied_to: ["{component.button-primary}", "{component.promo-strip}", "{component.hero-label}"]
  visual_signature: "a brokerage surface that feels live and electrified without using fintech blue"

black-nav-green-promo-stack:
  description: "The first viewport opens as terminal chrome followed by a live signal band."
  technique: "64px #000000 nav stacked above sticky #CCFF00 promo strip with 10px 20px padding and top offset below nav"
  applied_to: ["{component.navigation}", "{component.promo-strip}"]
  visual_signature: "black trading-console header immediately snapped to an acid-green announcement ticker"

serif-finance-hero:
  description: "Financial benefit copy is made editorial without becoming luxury or bank-like."
  technique: "Martina Plantijn headline at 72px / 78px, font-weight 400, letter-spacing -1px; tablet 58px / 63px; mobile 44px / 48px"
  applied_to: ["{component.hero-section}"]
  visual_signature: "IRA and retirement language reads like a magazine cover sitting above plain brokerage controls"

capsule-action-geometry:
  description: "All primary actions converge into one trading-app control shape."
  technique: "inline-flex button, height 44px, border-radius 36px, padding 0 32px, 1px solid matching fill, hover opacity 0.85"
  applied_to: ["{component.button-primary}", "{component.button-dark}", "{component.button-white}"]
  visual_signature: "smooth capsule controls that stay utilitarian even when the surrounding surface is theatrical"

green-floor-gradient:
  description: "A section can gain Robinhood energy from a hard green floor rather than a soft decorative gradient."
  technique: "linear-gradient(to top, #CCFF00 0px, #CCFF00 80px, transparent 80px)"
  applied_to: ["{component.hero-section}", "{component.image-led-section}"]
  visual_signature: "an acid-green platform under product imagery, like a lit base inside a display case"
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | financial benefit phrased as a direct gain | "Gear up your IRA with a 2% match" |
| Primary CTA | short action verbs | "Get started" |
| Secondary CTA | plain utility links | "Learn more" |
| Subheading | benefit + eligibility/terms in compact language | "With Robinhood Gold ($5/month), earn..." |
| Tone | consumer-finance directness, softened by editorial display type | "Retirement blooms. Earn up to $435." |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Robinhood-inspired core tokens */
:root {
  /* Fonts */
  --rh-font-family: "Phonic", Helvetica, system-ui, -apple-system, BlinkMacSystemFont, Arial, sans-serif;
  --rh-font-family-display: "Martina Plantijn", serif;
  --rh-font-family-code: "Capsule Sans Text Mono", ui-monospace, monospace;
  --rh-font-weight-normal: 400;
  --rh-font-weight-bold: 700;

  /* Brand */
  --rh-color-brand-25: #CCFF00;
  --rh-color-brand-300: #CCFF00;
  --rh-color-brand-500: #CCFF00;
  --rh-color-brand-600: #CCFF00;
  --rh-color-brand-900: #1C180D;

  /* Surfaces */
  --rh-bg-page: #FFFFFF;
  --rh-bg-dark: #000000;
  --rh-text: #110E08;
  --rh-text-muted: #35322D;
  --rh-border-muted: #888784;

  /* Key spacing */
  --rh-space-sm: 10px;
  --rh-space-md: 24px;
  --rh-space-lg: 32px;
  --rh-nav-height: 64px;

  /* Radius */
  --rh-radius-sm: 3px;
  --rh-radius-md: 36px;
}

body {
  background: var(--rh-bg-page);
  color: var(--rh-text);
  font-family: var(--rh-font-family);
  font-weight: var(--rh-font-weight-normal);
  letter-spacing: -0.25px;
}

.rh-hero-title {
  font-family: var(--rh-font-family-display);
  font-size: 72px;
  font-weight: 400;
  line-height: 78px;
  letter-spacing: -1px;
}

.rh-button {
  align-items: center;
  border-radius: var(--rh-radius-md);
  box-sizing: border-box;
  display: inline-flex;
  height: 44px;
  justify-content: center;
  overflow: hidden;
  padding: 0 var(--rh-space-lg);
  text-align: center;
  white-space: nowrap;
}

.rh-button-primary {
  background: #CCFF00;
  border: 1px solid #CCFF00;
  color: #110E08;
}

.rh-button-dark {
  background: #110E08;
  border: 1px solid #110E08;
  color: #FFFFFF;
}

.rh-button:hover {
  opacity: 0.85;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Robinhood-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        robinhood: {
          green: '#CCFF00',
          ink: '#110E08',
          muted: '#35322D',
          white: '#FFFFFF',
          black: '#000000',
        },
      },
      fontFamily: {
        sans: ['Phonic', 'Helvetica', 'system-ui', 'sans-serif'],
        display: ['Martina Plantijn', 'serif'],
        mono: ['Capsule Sans Text Mono', 'ui-monospace', 'monospace'],
      },
      borderRadius: {
        rh: '36px',
        'rh-sm': '3px',
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
| Brand primary | `{colors.primary}` | #CCFF00 |
| Background | `{colors.surface}` | #FFFFFF |
| Text primary | `{colors.ink}` | #110E08 |
| Text muted | `{colors.muted-ink}` | #35322D |
| Border | `{colors.hairline}` | #888784 |
| Dark nav | `{colors.dark-utility}` | #000000 |
| Error | N/A | N/A |

### Example Component Prompts

#### Hero Section

```text
Create a Robinhood-style homepage hero.
- Top nav: 64px high, #000000 background, white links, compact Phonic 14-16px text.
- Promo strip: #CCFF00 background, #110E08 text, sticky below nav.
- H1: Martina Plantijn, 72px desktop, weight 400, line-height 78px, letter-spacing -1px.
- Body: Phonic, 16px, line-height 24px, #110E08.
- CTA: #110E08 pill button on light hero, 44px high, 36px radius, 0 32px padding.
- Use product/finance imagery rather than abstract gradients.
```

#### Card Component

```text
Create a Robinhood-style content row/card.
- Background: #FFFFFF or section color, no heavy shadow.
- Border: 1px solid #35322D only when a divider is needed.
- Padding: 24px.
- Radius: avoid card radius unless matching an observed component; use 36px only for CTA capsules.
- Title: Phonic or serif if it is a major editorial promise.
```

#### Badge

```text
Create a Robinhood-style label.
- Use #CCFF00 sparingly as a signal, not as a pastel badge family.
- Text: #110E08, Phonic 12-14px, weight 400 or 500.
- Avoid multi-color status chips unless the source flow provides them.
```

#### Navigation

```text
Create a Robinhood-style top navigation.
- Height: 64px.
- Background: #000000.
- Links: white, Phonic 14-16px, simple horizontal spacing.
- Right action: green or green-outline capsule, 44px height, 36px radius.
- Keep the nav utilitarian; do not add blur, glass, or drop shadows.
```

### Iteration Guide

- **색상 변경 시**: #CCFF00 is the brand signal. Replacing it with blue or a muted green breaks the identity.
- **폰트 변경 시**: preserve the serif/sans split. A full-sans hero becomes generic fintech.
- **여백 조정 시**: keep nav 64px, CTA height 44px, and content padding near 24px/32px.
- **새 컴포넌트 추가 시**: default to border/section contrast before shadows.
- **다크 모드**: do not infer a full dark-mode token map from the homepage; only the nav/dark sections are confirmed.
- **반응형**: use the captured 425px, 768px, 1024px, and 1280px breakpoints.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#CCFF00` as the primary action and promo-strip color.
- Use `#110E08` as warm ink on green and white surfaces.
- Keep primary CTA geometry at 44px height, 36px radius, and `0 32px` padding.
- Pair serif hero display with Phonic body copy.
- Keep desktop nav black at 64px height.
- Let product/finance imagery carry depth instead of generic UI shadows.
- Use slight negative tracking on display and body copy.

### ❌ DON'T

- 배경을 `#F5F5F5` 또는 `#F7F7F7`로 두지 말 것 — 대신 confirmed surface `#FFFFFF` 사용.
- 브랜드 CTA를 `#00C805`, `#22C55E`, 또는 generic green으로 두지 말 것 — 대신 `#CCFF00` 사용.
- 텍스트를 `#000000` 또는 `black`으로만 두지 말 것 — primary page ink는 `#110E08` 사용.
- Green surface foreground를 `#FFFFFF`로 두지 말 것 — `#CCFF00` 위에는 `#110E08` 사용.
- Nav background를 `#110E08`로 바꾸지 말 것 — captured top nav is `#000000`.
- CTA radius를 `8px` 또는 `12px` 카드형으로 만들지 말 것 — Robinhood action geometry is `36px`.
- Hero headline을 sans-only `Inter`로 만들지 말 것 — serif display contrast is part of the page identity.
- 모든 콘텐츠 카드에 shadow를 넣지 말 것 — captured homepage relies on image depth, color fields, and borders.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second brand color: none observed. `#CCFF00` carries the recognizable brand/action role.
- Public token namespace: absent. No CSS custom properties or alias layer surfaced in phase1.
- Generic fintech blue: absent from the captured palette.
- Heavy card elevation: absent as a primary UI language.
- Glassmorphism nav: absent. The nav is flat #000000, not blurred translucent chrome.
- Multicolor badge taxonomy: absent from the homepage evidence.
- Rounded card system: mostly absent. Radius belongs to CTA capsules, not every container.
- Overweight display type: absent. The hero uses weight 400, not 800/900.
- Decorative abstract gradients: not the hero identity. Real product/mechanical imagery carries the visual load.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Cookie overlay in screenshot** — the captured desktop screenshot includes a cookie settings modal over the lower hero. Hero structure, nav, promo strip, and primary type remain visible, but lower hero spacing may be partially occluded.
- **Homepage-only analysis** — trading, account, crypto checkout, login, and onboarding sub-flows were not visited. Form validation, loading, and error states are therefore not confirmed.
- **No custom property layer** — phase1 found `total_vars: 0`. This guide uses analysis aliases like `rh-color-brand-primary` for practical implementation, not as claims about source CSS variable names.
- **Generated class names** — selectors such as `.css-rhrgcq` are build artifacts and should not be treated as stable API names.
- **Motion limited** — only hover opacity was surfaced in the CSS summary. Scroll-triggered or JS-driven animation behavior was not analyzed.
- **Dark-mode mapping absent** — the page contains dark nav/sections, but no full dark-mode semantic palette was proven.
- **Exact image treatment** — the visual hero relies on sourced photography/product imagery. CSS tokens alone cannot recreate the mechanical/gold object or its lighting.
- **Error/success colors** — no dedicated error or success token was surfaced. Do not invent red/green status palettes without visiting flows that show them.
