---
schema_version: 3.2
slug: louisvuitton
service_name: Louis Vuitton
site_url: https://www.louisvuitton.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#19110B"
primary_font: "Louis Vuitton Web"
font_weight_normal: 400
token_prefix: lv

bold_direction: Monochrome Luxury
aesthetic_category: other
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high

archetype: luxury-brand
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Captured CSS shows an in-use LV waiting-page system with proprietary fonts, responsive gutters, masthead image treatment, and sparse component classes, but no exported token layer."

colors:
  brand-ink: "#19110B"
  text-black: "#000000"
  surface-white: "#FFFFFF"
  hairline: "#E1E1E1"
  overlay-black: "#000000"
  overlay-text: "#FFFFFF"

typography:
  display: "Louis Vuitton Web"
  body: "Louis Vuitton Web"
  regional_cyrillic: "Louis Vuitton Cyrillic"
  ladder:
    - { token: body, size: "16px", weight: 400, line_height: "24px", tracking: "0" }
    - { token: heading-s, size: "18px", weight: 400, line_height: "24px", tracking: "0.4px" }
    - { token: heading-m, size: "24px", weight: 400, line_height: "28px", tracking: "0.4px" }
    - { token: masthead-title-desktop, size: "24px", weight: 400, line_height: "32px", tracking: "0.4px" }
  weights_used: [400]
  weights_absent: [300, 500, 600, 700]

components:
  masthead-image: { aspect_mobile: "4/5", aspect_desktop: "16/9", overlay: "rgba(0,0,0,0.2)", max_height: "90vh" }
  logo-header: { width_mobile: "9.625rem", width_desktop: "14.1875rem", fill: "#FFFFFF", position: "absolute" }
  waiting-title-pair: { layout_mobile: "centered stacked", layout_desktop: "two columns", max_width: "70%" }
  gutter-frame: { mobile: "6.4vw", tablet: "3.125vw", desktop: "4.6875vw", wide: "8.3333333333vw" }
---

# DESIGN.md - Louis Vuitton Designer Guidebook

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Louis Vuitton stages even its access-refusal page like a museum storefront after hours: the door is closed, but the window is still lit, polished, and composed for the passerby. This is the guarded waiting surface served by the site when access is denied, and that constraint matters — the page turns a technical refusal into a luxury-brand stage. The system does not apologize with a utility banner.

The page has almost no site-like self-expression. A small white administrative strip carries the reference number, then the interface steps aside and a campaign masthead takes over. It feels less like an error page than a customs desk placed in front of a desert showroom: operational content exists, but the visitor is made to wait inside the brand's photographic atmosphere rather than inside a software state.

The visual language is monochrome first. Black text on #FFFFFF (`{colors.surface-white}`), white logo and white copy over photography, and one dark maison ink #19110B (`{colors.brand-ink}`) reserved for favicon and brand identity. There is no second brand color, no CTA accent, no alert red. The only chroma is smuggled in by the photograph itself: desert blue, pale sky, sun flare, and the warm object glow inside the frame.

Typography behaves like a parchment product label in a vitrined catalogue rather than a marketing shout. `Louis Vuitton Web` stays at weight 400 across body and headings; `font-weight: 500` and `font-weight: 700` are absent. Heading hierarchy is built by small shifts in size, line-height, and 0.4px tracking, not by weight contrast. The refusal message has the manners of a museum wall label: small, formal, and exact, while the image beside it does the emotional speaking.

Space is the signature restraint. The top reference area is bare white utility space, then the masthead cuts in with a hard horizontal edge like a magazine spread trimmed against the page. On desktop, the two language blocks sit apart inside the image, creating a ceremonial bilateral composition. On mobile, the masthead becomes a 4/5 vertical crop, turning the blocked session into a cover image rather than a failure notice.

The component system is minimal, but not careless. Gutters are viewport-proportional, the masthead has explicit aspect ratios, the image uses `object-fit: cover`, and a #000000 overlay at 20% opacity (`{colors.overlay-black}`) keeps white text readable without making the image feel like a dark UI layer. Shadow only exists as photography and scrim; the interface itself refuses elevation. This is a luxury maintenance page: the machine is blocked, but the brand room is still curated.

### Key Characteristics

- Proprietary `Louis Vuitton Web` font is the dominant identity token; the fallback chain is long but secondary.
- Single-weight typography: 400 carries body, headings, logo-adjacent text, and access message.
- Monochrome UI shell: #FFFFFF surface, #000000 text, #FFFFFF overlay text, #E1E1E1 hairline.
- Maison ink #19110B appears as a brand identity dark, not as a broad UI accent.
- Hero masthead is image-led, full-width, and capped at 90vh.
- Mobile masthead uses 4/5 editorial portrait crop; desktop switches to 16/9.
- White SVG wordmark is centered in an absolute header over the masthead system.
- Text over image uses a 20% black overlay rather than drop shadows.
- Desktop title layout splits bilingual messages into two balanced columns.
- Gutters are vw-based and expand again on wide screens, preserving gallery air.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Monochrome Luxury
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **a guarded editorial masthead that makes an access-denied state feel like a maison campaign image**으로 기억된다.
> **Code Complexity**: medium — responsive masthead, proprietary font stacks, image overlay, and breakpoint-specific bilateral layout require more than a static utility page.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Louis Vuitton처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Louis Vuitton Web", "Louis Vuitton", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 24px;
}

/* 2. 표면 + 텍스트 */
:root {
  --lv-surface: #FFFFFF;
  --lv-text: #000000;
  --lv-maison-ink: #19110B;
  --lv-hairline: #E1E1E1;
}

body {
  background: var(--lv-surface);
  color: var(--lv-text);
}

/* 3. masthead image treatment */
.lv-masthead {
  position: relative;
  width: 100%;
  aspect-ratio: 4 / 5;
  max-height: 90vh;
  overflow: hidden;
}
.lv-masthead::after {
  content: "";
  position: absolute;
  inset: 0;
  background: #000000;
  opacity: 0.2;
}
@media (min-width: 48rem) {
  .lv-masthead { aspect-ratio: 16 / 9; }
}
```

**절대 하지 말아야 할 것 하나**: access-denied 상태를 generic error card로 만들지 말 것. LV는 오류를 카드에 넣지 않고 full-bleed editorial image 위에 얹는다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.louisvuitton.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | phase1 reuse: existing HTML + inline CSS + screenshot |
| HTML size | 12541 bytes |
| CSS files | 1 inline CSS file, 5897 bytes |
| Token prefix | `lv` inferred from class prefix `.lv-*` |
| Method | Existing phase1 JSON, captured HTML/CSS, and hero screenshot. No new crawl was performed because reusable phase1 artifacts existed. |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: static guarded waiting page, no app shell detected in captured HTML.
- **Design system**: LV waiting-page CSS classes with prefix `.lv-`; no CSS custom-property token API was exposed.
- **CSS architecture**: small inline CSS block with font faces, base reset, responsive gutters, masthead, and waiting-page components.

```css
/* observed layers */
@font-face                      /* proprietary brand fonts */
html, body, h1, h2, h3, h4       /* base reset */
.heading-s / .heading-m          /* small type ladder */
.lv-gutters                      /* responsive viewport gutters */
.lv-waiting__*                   /* page-specific components */
@media (min-width: 48rem)        /* desktop masthead/title switch */
```

- **Class naming**: BEM-like `.lv-waiting__header`, `.lv-waiting__masthead`, `.lv-waiting__titles`.
- **Default theme**: mixed. Utility area is light #FFFFFF; masthead is image-darkened with #000000 at 20% opacity.
- **Font loading**: two proprietary `@font-face` declarations from `tp.louisvuitton.com`.
- **Canonical anchor**: centered white Louis Vuitton SVG wordmark above an editorial masthead.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Louis Vuitton Web` (proprietary brand font)
- **Regional font**: `Louis Vuitton Cyrillic` for Russian language contexts
- **Code font**: N/A
- **Weight normal / bold**: `400` / N/A. Captured CSS uses normal weight only.

```css
@font-face {
  font-family: "Louis Vuitton Web";
  font-weight: 400;
  font-style: normal;
  src: url("//tp.louisvuitton.com/fonts/bin/LouisVuitton-Regular.woff2") format("woff2"),
       url("//tp.louisvuitton.com/fonts/bin/LouisVuitton-Regular.woff") format("woff");
}

body {
  font-family: "Louis Vuitton Web", "Louis Vuitton", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: 400;
}
```

### Note on Font Substitutes

- **Louis Vuitton Web** is proprietary. For local reproduction, use **Helvetica Neue** first, then Helvetica or Arial, but keep weight 400 and avoid synthetic bold.
- **Optical correction**: if Helvetica Neue feels too heavy at 24px, keep `font-weight: 400` and loosen line-height to 32px rather than switching to 300.
- **Tracking correction**: preserve `letter-spacing: 0.4px` on `.heading-s` and `.heading-m`; do not apply negative display tracking.
- **Regional fallback**: Korean capture path uses `Droid Sans Fallback`, `Malgun Gothic`, `Dotum`, `MS Gothic`, then Georgia and Helvetica. Keep this broad fallback chain if multilingual text is present.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| body | 16px | 400 | 24px | 0 |
| heading-s | 18px | 400 | 24px | 0.4px |
| waiting-title mobile | 14px | 400 | 20px | inherited |
| waiting-top-title mobile | 18px | 400 | 24px | 0.4px |
| heading-m / desktop top-title | 24px | 400 | 28px base / 32px desktop | 0.4px |

> ⚠️ Key insight: LV does not create hierarchy through boldness here. It creates hierarchy through restrained size changes, line-height, and the authority of the proprietary font.

### Principles

1. Weight 400 is the identity. Do not introduce 500, 600, or 700 just to make headings feel more "premium".
2. The display scale is deliberately small: 24px can be the hero message when the image and wordmark carry the drama.
3. Letter-spacing is positive 0.4px on heading classes, a label-like luxury correction rather than a tech-style negative tracking.
4. Body rhythm is 16px / 24px, a classic 1.5 line-height that keeps utility text calm.
5. Multilingual support is part of the font system. The page expects language-specific fallback, not one universal Latin-only stack.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (1 step)

| Token | Hex |
|---|---|
| `brand-ink` | `#19110B` |

### 06-2. Brand Dark Variant

> N/A - captured page exposes one maison dark, not a ramp.

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| surface | `#FFFFFF` | N/A |
| text | N/A | `#000000` |
| hairline | `#E1E1E1` | N/A |

### 06-4. Accent Families

> N/A - no UI accent palette was exposed. Photography carries chroma.

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `surface-white` | `#FFFFFF` | top utility/reference area |
| `text-black` | `#000000` | body text and links on white |
| `overlay-text` | `#FFFFFF` | logo and masthead copy |
| `hairline` | `#E1E1E1` | secondary section divider |
| `overlay-black` | `#000000` at 20% opacity | masthead readability scrim |
| `brand-ink` | `#19110B` | favicon mask and maison identity dark |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--lv-surface` | `#FFFFFF` | page surface |
| `--lv-text` | `#000000` | default text and links |
| `--lv-overlay` | `#000000` / opacity `0.2` | masthead picture overlay |
| `--lv-overlay-text` | `#FFFFFF` | logo and masthead title text |
| `--lv-hairline` | `#E1E1E1` | section separation |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| `text-black / overlay-black` | `#000000` | 6 |
| `surface-white / overlay-text` | `#FFFFFF` | 5 |
| `hairline` | `#E1E1E1` | 2 |
| `brand-ink` | `#19110B` | 1 |

### 06-8. Color Stories

**`{colors.text-black}` (#000000)** - The default utility ink. It appears in base text and links, and it should stay plain black rather than softened into charcoal when the surface is white.

**`{colors.surface-white}` (#FFFFFF)** - The administrative floor. The top reference block is pure white, making the later image cut feel intentional and editorial.

**`{colors.hairline}` (#E1E1E1)** - The only structural grey. It separates secondary content without becoming a card border system.

**`{colors.brand-ink}` (#19110B)** - The maison dark. It is visible in favicon metadata rather than broad page paint, so treat it as brand identity ink, not a CTA fill.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `gutter-mobile` | `6.4vw` | mobile horizontal page gutters |
| `gutter-tablet` | `3.125vw` | tablet gutters at 48rem |
| `gutter-desktop` | `4.6875vw` | desktop gutters at 64rem |
| `gutter-wide` | `8.3333333333vw` | wide-screen gallery air at 90rem |
| `header-top` | `2rem` | logo/header top padding |
| `primary-gap-mobile` | `1rem` | primary grid gap before desktop |
| `primary-gap-desktop` | `2rem` | primary grid gap at 48rem |
| `title-container-gap` | `40px` | separation below title container |
| `secondary-margin-top` | `5rem` | secondary section separation |
| `secondary-padding-y` | `5rem` | secondary section vertical padding |
| `zone-margin-top` | `5rem` | repeated zone spacing |
| `zone-child-gap` | `1.5rem` | child spacing in zone blocks |

**주요 alias**:
- `lv-gutters` -> viewport-based horizontal margins, not a fixed max-width container.

### Whitespace Philosophy

LV's spacing is not a dense commerce interface in this capture. It is a ceremony of interruptions: white utility space, then a hard masthead image, then large section breaks. The page accepts that a technical reference number must exist, but it refuses to let that utility block define the visual tone.

The gutters are especially brand-like because they stay proportional to the viewport. At wide screens the system expands to `8.3333333333vw`, giving the composition more air instead of filling every inch with interface.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| global radius | `0` | no rounded cards, no pill CTA, no soft panels in captured CSS |
| masthead crop | `0` | full-bleed rectangular image crop |
| logo container | `0` | centered SVG without frame |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none | `none` | captured UI does not use box-shadow |
| readability | `background-color: #000000; opacity: 0.2` | image overlay replaces text shadow |

Shadow is intentionally absent. Depth comes from photography, not from UI elevation.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

> N/A - no transition, animation, or motion token was present in the captured CSS. Do not invent fade-in or parallax unless a new capture proves it.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: none exposed; gutters are viewport-based.
- **Grid type**: CSS Grid for `.lv-waiting__primary` and `.lv-waiting__contacts`.
- **Column count**: primary grid 1 column mobile, 4 columns desktop; contacts 2 columns mobile, 6 columns desktop.
- **Gutter**: 1rem mobile primary gap, 2rem desktop grid gap.

### Hero

- **Pattern Summary**: `90vh cap + responsive editorial image + centered absolute logo + bilingual title pair over 20% black overlay`.
- Layout: full-width masthead with absolute text overlay.
- Background: responsive `<picture>` with desktop and mobile maintenance-page imagery.
- **Background Treatment**: image-overlay (`#000000` at opacity `0.2`) over `object-fit: cover` image.
- H1: `18px / 400 / 0.4px` mobile top title, `24px / 400 / 0.4px` desktop top title with 32px line-height.
- Max-width: title area `70%` on desktop; each title container `45%`.

### Section Rhythm

```css
.lv-gutters {
  padding-left: 6.4vw;
  padding-right: 6.4vw;
}

.lv-waiting__secondary {
  border-top: 1px solid #E1E1E1;
  margin-top: 5rem;
  padding-top: 5rem;
  padding-bottom: 5rem;
}
```

### Card Patterns

- **Card background**: N/A, no card system detected.
- **Card border**: N/A, only section-level #E1E1E1 hairline.
- **Card radius**: 0.
- **Card padding**: N/A.
- **Card shadow**: none.

### Navigation Structure

- **Type**: no navigation links in captured page; centered brand wordmark only.
- **Position**: absolute header over the page.
- **Height**: header uses top padding, logo height 1rem mobile and 2.6875rem desktop.
- **Background**: transparent over masthead/white page context.
- **Border**: none.

### Content Width

- **Prose max-width**: title containers max 45% on desktop.
- **Container max-width**: none; viewport gutters set the frame.
- **Sidebar width**: N/A.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `< 48rem` | masthead 4/5, small logo, stacked title logic |
| Tablet | `48rem` | masthead switches to 16/9, primary grid becomes 4 columns |
| Desktop | `64rem` | gutters expand to 4.6875vw |
| Large | `90rem` | gutters expand to 8.3333333333vw |

### Touch Targets

- **Minimum tap size**: not measurable from captured page; no buttons detected.
- **Button height (mobile)**: N/A.
- **Input height (mobile)**: N/A.

### Collapsing Strategy

- **Navigation**: wordmark-only header; no menu collapse observed.
- **Grid columns**: primary grid 1 -> 4, contacts 2 -> 6 at 48rem.
- **Sidebar**: none.
- **Hero layout**: portrait 4/5 mobile image crop -> landscape 16/9 desktop image crop.

### Image Behavior

- **Strategy**: responsive `<picture>` sources with width-based `srcset`.
- **Max-width**: image fills masthead width and height.
- **Aspect ratio handling**: CSS `aspect-ratio` plus `object-fit: cover`.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

> N/A - no button component was present in the captured page. Do not invent a CTA style from the broader brand.

### Badges

> N/A - no badge or chip component was present.

### Cards & Containers

The capture avoids cards entirely. Structure is created through full-width bands, gutters, grid layout, and one hairline divider.

| Component | Background | Border | Radius | Padding | Shadow |
|---|---|---|---:|---|---|
| utility/reference area | `#FFFFFF` | none | 0 | via `.lv-gutters` | none |
| secondary section | inherited | top `1px solid #E1E1E1` | 0 | `5rem 0` | none |
| masthead | image | none | 0 | none | none |

### Navigation

```html
<header class="lv-waiting__header">
  <div class="lv-waiting__logo">
    <svg fill="#FFF" aria-label="Louis Vuitton">...</svg>
  </div>
</header>
```

- Logo is centered, white, and unframed.
- Header is absolute with `z-index: 9`.
- Mobile logo: `9.625rem` wide, `1rem` tall.
- Desktop logo: `14.1875rem` wide, `2.6875rem` tall.

### Inputs & Forms

> N/A - no input, select, checkbox, or form state was present.

### Hero Section

```html
<div class="lv-waiting__masthead">
  <picture>...</picture>
  <div class="lv-waiting__titles">
    <div class="lv-waiting__title-container">
      <h1 class="lv-waiting__top-title heading-m">...</h1>
    </div>
    <div class="lv-waiting__title-container">
      <h1 class="lv-waiting__top-title heading-m">...</h1>
    </div>
  </div>
</div>
```

- Masthead `aspect-ratio: 4/5` on mobile and `16/9` at 48rem.
- Image fills the frame with `object-fit: cover`.
- `picture::after` adds `#000000` at `opacity: 0.2`.
- Titles are absolute centered vertically with `transform: translate(0, -50%)`.
- Desktop title group becomes flex, `justify-content: space-between`, `align-items: center`, `max-width: 70%`.

### 13-2. Named Variants

| Variant | Spec |
|---|---|
| `masthead-image-mobile` | `aspect-ratio: 4/5`, `max-height: 90vh`, `object-fit: cover` |
| `masthead-image-desktop` | `aspect-ratio: 16/9` at `min-width: 48rem` |
| `logo-header-mobile` | centered SVG, `width: 9.625rem`, `height: 1rem` |
| `logo-header-desktop` | centered SVG, `width: 14.1875rem`, `height: 2.6875rem` |
| `waiting-title-pair-desktop` | flex row, `max-width: 70%`, title containers `max-width: 45%` |
| `gutter-frame-wide` | `padding-left/right: 8.3333333333vw` at `90rem` |

### 13-3. Signature Micro-Specs

```yaml
guarded-maison-masthead:
  description: "Access denial is staged as a full-width campaign masthead instead of an error card."
  technique: "position: relative; width: 100%; max-height: 90vh; overflow: hidden; aspect-ratio: 4 / 5 mobile, 16 / 9 at min-width 48rem; image uses position:absolute inset:0 width:100% height:100% object-fit:cover"
  applied_to: ["{component.masthead-image}", "{component.waiting-title-pair}"]
  visual_signature: "A blocked session reads like a maison campaign window: rectangular, image-led, and cardless."

bilingual-gallery-refusal:
  description: "The denial copy is split into two balanced language blocks over the photograph on desktop."
  technique: ".lv-waiting__titles position:absolute top:50% left:0 right:0 margin:auto transform:translate(0,-50%) color:#FFFFFF text-align:center; at 48rem max-width:70% display:flex justify-content:space-between align-items:center; children max-width:45%"
  applied_to: ["{component.waiting-title-pair}", "{component.masthead-image}"]
  visual_signature: "Operational text behaves like paired gallery captions suspended inside the campaign image."

quiet-black-scrim:
  description: "Readability is solved with a global image scrim, not text-shadow or UI elevation."
  technique: ".lv-waiting__masthead picture::after { content:\"\"; position:absolute; inset:0; width:100%; height:100%; background-color:#000000; opacity:0.2; }"
  applied_to: ["{component.masthead-image}", "{colors.overlay-black}", "{colors.overlay-text}"]
  visual_signature: "White logo and copy stay legible while the photograph still feels luminous, not blacked out."

viewport-maison-gutters:
  description: "The frame breathes by viewport percentage instead of a fixed max-width container."
  technique: ".lv-gutters padding-left/right:6.4vw; 3.125vw at 48rem; 4.6875vw at 64rem; 8.3333333333vw at 90rem"
  applied_to: ["{component.gutter-frame}", "{component.gutter-frame-wide}"]
  visual_signature: "Wide screens regain gallery air instead of stretching the utility page edge to edge."

optical-04px-tracking-everywhere:
  description: "A single 0.4px positive letter-spacing carries every operational text size, replacing weight or color hierarchy."
  technique: "letter-spacing: 0.4px applied uniformly to heading-s 18px/24px, heading-m 24px/28px, and masthead-title-desktop 24px/32px; body 16px/24px keeps 0; weight stays at 400 across the entire ladder."
  applied_to: ["{typography.body}", "{typography.display}", "{component.waiting-title-pair}"]
  visual_signature: "Every label sits like engraved capitals on metal: airy, even, never bunched — even though the font weight never escalates."
```

---

## 14. Content Voice
<!-- SOURCE: auto+manual -->

The captured copy is operational but formal: "We invite you to return at a later time to complete your purchase." It avoids casual apologies and avoids aggressive security language. The French parallel copy reinforces global maison formality.

Voice rules:

- Use "invite" rather than "try again" when the brand must refuse an action.
- Keep error text short and centered if it appears on campaign photography.
- Do not expose stack traces or technical WAF detail except the small reference block.
- Let the image and wordmark preserve brand tone when the message itself is utilitarian.

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
:root {
  --lv-brand-ink: #19110B;
  --lv-text: #000000;
  --lv-surface: #FFFFFF;
  --lv-hairline: #E1E1E1;
  --lv-overlay: #000000;
  --lv-overlay-text: #FFFFFF;
  --lv-font: "Louis Vuitton Web", "Louis Vuitton", "Helvetica Neue", Helvetica, Arial, sans-serif;
}

html,
body {
  margin: 0;
  padding: 0;
  font-size: 16px;
  line-height: 24px;
  color: var(--lv-text);
  background: var(--lv-surface);
}

body {
  font-family: var(--lv-font);
  font-style: normal;
  font-weight: 400;
}

h1,
h2,
h3,
h4 {
  font-weight: 400;
  margin: 0 0 0.5rem;
}

a {
  color: var(--lv-text);
}

.heading-m {
  font-size: 1.5rem;
  line-height: 28px;
  letter-spacing: 0.4px;
}

.heading-s {
  font-size: 1.125rem;
  line-height: 24px;
  letter-spacing: 0.4px;
}

.lv-gutters {
  box-sizing: border-box;
  padding-left: 6.4vw;
  padding-right: 6.4vw;
}

.lv-waiting__header {
  position: absolute;
  left: 0;
  right: 0;
  z-index: 9;
  padding: 2rem 0 0;
}

.lv-waiting__logo {
  width: 9.625rem;
  height: 1rem;
  margin: 0 auto;
  display: block;
}

.lv-waiting__masthead {
  aspect-ratio: 4 / 5;
  position: relative;
  width: 100%;
  max-height: 90vh;
  overflow: hidden;
}

.lv-waiting__masthead picture::after {
  content: "";
  display: block;
  background-color: var(--lv-overlay);
  opacity: 0.2;
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.lv-waiting__masthead img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.lv-waiting__titles {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  margin: auto;
  color: var(--lv-overlay-text);
  text-align: center;
  transform: translate(0, -50%);
}

.lv-waiting__top-title {
  padding: 0 1.25rem;
  font-size: 1.125rem;
  line-height: 24px;
}

@media screen and (min-width: 48rem) {
  .lv-gutters {
    padding-left: 3.125vw;
    padding-right: 3.125vw;
  }

  .lv-waiting__masthead {
    aspect-ratio: 16 / 9;
  }

  .lv-waiting__header {
    padding: 2rem 0 1rem;
  }

  .lv-waiting__logo {
    width: 14.1875rem;
    height: 2.6875rem;
  }

  .lv-waiting__titles {
    max-width: 70%;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .lv-waiting__title-container {
    max-width: 45%;
  }

  .lv-waiting__top-title {
    font-size: 1.5rem;
    line-height: 32px;
  }
}

@media screen and (min-width: 64rem) {
  .lv-gutters {
    padding-left: 4.6875vw;
    padding-right: 4.6875vw;
  }
}

@media screen and (min-width: 90rem) {
  .lv-gutters {
    padding-left: 8.3333333333vw;
    padding-right: 8.3333333333vw;
  }
}
```

---

## 16. Tailwind Translation
<!-- SOURCE: manual -->

Tailwind should be treated as an implementation shell only. The brand effect depends on proprietary fonts, exact aspect ratios, and the overlay system.

```js
export default {
  theme: {
    extend: {
      colors: {
        lv: {
          ink: "#19110B",
          text: "#000000",
          surface: "#FFFFFF",
          hairline: "#E1E1E1"
        }
      },
      fontFamily: {
        lv: ['"Louis Vuitton Web"', '"Louis Vuitton"', '"Helvetica Neue"', "Helvetica", "Arial", "sans-serif"]
      },
      letterSpacing: {
        lvHeading: "0.4px"
      }
    }
  }
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

- Surface: `#FFFFFF`
- Text: `#000000`
- Maison ink: `#19110B`
- Hairline: `#E1E1E1`
- Overlay text: `#FFFFFF`
- Image scrim: `#000000` at `opacity: 0.2`

### Build Prompt

Create a Louis Vuitton-inspired guarded waiting page, not a normal SaaS error screen. Use a full-width editorial masthead image with a 20% black overlay, a centered white wordmark, and two bilingual title blocks balanced across the image on desktop. Keep typography in a proprietary-style luxury sans at weight 400 only. Use #FFFFFF for the utility surface, #000000 for text, #E1E1E1 for the only divider, and #19110B only as maison identity ink. Avoid cards, rounded panels, shadows, colorful CTAs, and heavy heading weights.

### Implementation Warnings

- If the design starts to look like a generic 404 page, remove the card and return to the masthead.
- If it starts to look like a fashion campaign page, add the white utility reference block above the image.
- If headings feel weak, adjust line-height or image composition before adding bold weight.
- If text readability is poor, use a global 20% black overlay instead of text shadow.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO

- Use `Louis Vuitton Web` or a close Helvetica Neue fallback at `font-weight: 400`.
- Keep the UI shell monochrome: #FFFFFF surface, #000000 text, #FFFFFF text over image.
- Use #19110B as maison identity ink only where a brand-dark token is needed.
- Let photography provide chroma, atmosphere, and depth.
- Preserve the masthead aspect switch: 4/5 mobile, 16/9 desktop.
- Use a #000000 overlay at 20% opacity for white text over image.
- Keep gutters viewport-relative, especially the wide-screen `8.3333333333vw` frame.
- Use section-level separation like `1px solid #E1E1E1` instead of card borders.

### DON'T

- 배경을 `#F7F7F7`, `#FAFAFA`, 또는 beige 계열로 두지 말 것 - 대신 captured utility surface `#FFFFFF` 사용.
- 텍스트를 `#111111`, `#1D1D1F`, 또는 softened charcoal로 바꾸지 말 것 - 대신 captured base text `#000000` 사용.
- masthead overlay를 `#000000` 50% 이상으로 어둡게 만들지 말 것 - 대신 captured `#000000` at `opacity: 0.2` 사용.
- 흰색 overlay text를 `#F5F5F5`나 `rgba(255,255,255,0.85)`로 낮추지 말 것 - 대신 `#FFFFFF` 사용.
- divider를 `#DDDDDD` 또는 `#CCCCCC`로 진하게 만들지 말 것 - 대신 captured hairline `#E1E1E1` 사용.
- brand ink `#19110B`를 CTA fill이나 large background로 과사용하지 말 것 - captured page에서는 identity dark로만 작동한다.
- body에 `font-weight: 500`, `600`, `700` 사용 금지 - captured LV typography는 400만 사용한다.
- heading에 negative tracking 사용 금지 - captured heading classes use `letter-spacing: 0.4px`.
- rounded card, modal, or alert panel로 access-denied message를 감싸지 말 것 - captured layout is masthead-first and cardless.
- box-shadow나 text-shadow로 luxury depth를 만들지 말 것 - captured system uses photography plus overlay, not elevation.

### What This Site Doesn't Use

- No exposed CSS custom-property token system; values are direct CSS declarations.
- No bright brand accent color for buttons or links.
- No CTA buttons in the captured waiting page.
- No rounded cards, pill controls, or framed alert panels.
- No UI shadows or layered elevation.
- No gradient mesh, decorative blobs, or synthetic background effects.
- No bold heading weights; 500/600/700 are absent.
- No dense ecommerce product grid in this capture.
- No visible navigation menu; the wordmark alone anchors the page.
- No motion tokens, transitions, or scroll effects were captured.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- The captured HTML is an `Access denied` waiting page, not the normal Louis Vuitton homepage or product-commerce experience. This guidebook describes the observed guarded surface only.
- The phase1 extraction found zero CSS custom properties, so token names such as `--lv-surface` in this document are designer-facing aliases, not confirmed production variables.
- The screenshot and HTML show maintenance-page imagery and bilingual denial copy. Product cards, checkout flows, menus, search, account UI, and PDP components were not observed.
- Brand color #19110B is present in favicon mask metadata and treated as maison ink, but the captured page does not use it as a visible large UI fill.
- Typography scale is limited to the captured waiting page classes. Larger campaign headings may exist elsewhere on the site, but they were not present in the reused phase1 data.
- Motion is marked N/A because no animation declarations were visible in the inline CSS. Runtime JavaScript from Dynatrace was present but not interpreted as design motion.
- The analysis reused existing phase1 artifacts as requested. No fresh live browser crawl was performed, so current production homepage changes after the phase1 capture are outside scope.
