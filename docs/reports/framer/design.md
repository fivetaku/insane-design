---
schema_version: 3.2
slug: framer
service_name: Framer
site_url: https://www.framer.com
fetched_at: 2026-05-03T06:31:26Z
default_theme: dark
brand_color: "#0099FF"
primary_font: "Inter Display"
font_weight_normal: 400
token_prefix: framer

bold_direction: Monochrome Launchpad
aesthetic_category: Refined SaaS
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Framer-generated page with 154 CSS variables, 93 resolved tokens, repeated component classes, and consistent dark SaaS marketing patterns."

colors:
  primary: "#0099FF"
  surface-dark: "#000000"
  surface-card: "#080808"
  text-primary: "#FFFFFF"
  text-muted: "#999999"
  hairline-dark: "#FFFFFF1A"
  ink-card: "#2B2B2B"
typography:
  display: "Inter Display"
  body: "Inter"
  mono: "JetBrains Mono"
  ladder:
    - { token: hero, size: "clamp(72px, 9vw, 112px)", weight: 700, tracking: "-0.05em" }
    - { token: headline, size: "48px", weight: 700, tracking: "-0.04em" }
    - { token: body-large, size: "24px", weight: 400, tracking: "-0.01px" }
    - { token: nav, size: "14px", weight: 400, tracking: "0" }
  weights_used: [100, 200, 300, 400, 500, 600, 700, 800, 900]
  weights_absent: []
components:
  button-primary: { bg: "#FFFFFF", fg: "#000000", radius: "100px", padding: "10px 16px" }
  button-secondary-dark: { bg: "#2B2B2B", fg: "#FFFFFF", radius: "100px", padding: "10px 16px" }
  nav-link-muted: { fg: "#999999", hover: "#FFFFFF" }
  dark-card: { bg: "#080808", border: "#FFFFFF1A", radius: "10px" }
---

# DESIGN.md - Framer

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Framer's homepage behaves like a black launch stage, not a conventional product landing page. The first screen is almost entirely #000000 (`{colors.surface-dark}`), and the product promise lands through huge white typography rather than illustration. It is closer to a midnight product keynote than a SaaS brochure: one hard message under a spotlight, with the surrounding chrome reduced to near silence.

The brand color is present, but it does not lead the first impression. #0099FF (`{colors.primary}`) appears in the token set and selection/link system, yet the visible homepage identity is closer to monochrome confidence: white headline, gray body, black field, small pill CTAs. There is no second brand-color performance in the hero. The blue is backstage wiring, not the stage light; do not turn Framer into a blue SaaS page just because the chromatic token exists.

Typography carries the drama. `Inter Display` and `Inter` dominate the extracted font families, while the hero uses extremely compressed display rhythm: oversized text, heavy weight, and negative tracking around `-0.05em`. The letters feel pressed into one block of white vinyl on black acrylic. The subcopy falls back to muted #999999 (`{colors.text-muted}`), so the paragraph behaves like a caption under a gallery title: useful, quiet, and never allowed to steal the wall.

The below-the-fold preview strip is the second signature. It brings site thumbnails and product examples up from the bottom edge, so the hero is not an abstract claim. The page says "build better sites" and immediately opens a light table of miniature websites under the black stage, like a studio desk where finished mockups are waiting to be inspected.

The structural craft is almost negative space. Borders are not really borders; they are #FFFFFF1A (`{colors.hairline-dark}`) scratches in the dark. Shadows belong to preview evidence, not to loud interface chrome. Framer's page has very little "site" self-consciousness: the frame disappears, the claim lands, and the product examples do the proof work.

### Key Characteristics

- Black-first hero surface: #000000 is the primary atmosphere, not a dark-mode variant.
- White oversized display headline: #FFFFFF on black with tight tracking.
- Muted gray supporting copy: #999999 keeps the body text secondary.
- Pills over rectangles: CTAs use rounded capsule geometry, commonly 100px radius.
- Brand blue is restrained: #0099FF exists as accent/selection/link color, not broad page wash.
- Preview-strip storytelling: site examples appear as a horizontal product shelf below the hero.
- Framer-generated CSS signature: hashed component classes plus `--framer-*` rich text variables.
- Thin dark dividers: #FFFFFF1A and similar alpha whites define edges without visible chrome.
- Motion/craft bias: blur, dark shadows, and reveal-like composition matter more than color ramps.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Monochrome Launchpad
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **black-stage hero impact**으로 기억된다.
> **Code Complexity**: high — Framer runtime CSS, many generated component classes, blur/shadow craft, responsive variants, and rich preview surfaces.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Framer처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Font + weight */
body {
  font-family: "Inter", "Inter Variable", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
}

h1 {
  font-family: "Inter Display", "Inter", sans-serif;
  font-weight: 700;
  letter-spacing: -0.05em;
}

/* 2. Background + text */
:root {
  --framer-bg: #000000;
  --framer-fg: #FFFFFF;
  --framer-muted: #999999;
}
body { background: var(--framer-bg); color: var(--framer-fg); }

/* 3. Accent: keep it narrow */
:root { --framer-accent: #0099FF; }
::selection { background: color-mix(in srgb, var(--framer-accent) 30%, transparent); }
```

**절대 하지 말아야 할 것 하나**: Framer를 #0099FF 중심의 파란 SaaS 페이지로 만들지 말 것. 실제 첫인상은 #000000 / #FFFFFF / #999999의 monochrome hero다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.framer.com` |
| Fetched | 2026-05-03T06:31:26Z |
| Extractor | reused existing phase1 assets from `insane-design/framer/` |
| HTML size | 2,922,973 bytes (Framer generated site, generator `Framer e1ab3a2`) |
| CSS files | 1 inline CSS file, 478,309 chars |
| Custom properties | 1,097 declarations observed in inline CSS scan |
| Resolved tokens | 93 resolved / 154 total variables |
| Token prefix | `framer` plus generated `--token-*` UUID variables |
| Method | phase1 JSON + inline CSS summary + hero screenshot inspection |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Framer-generated marketing site (`generator: Framer e1ab3a2`)
- **Design system**: Framer runtime tokens — prefix `--framer-*` for rich text, UUID `--token-*` for site tokens
- **CSS architecture**:
  ```css
  --framer-*          rich text, link, code, blockquote, selection variables
  --token-uuid        generated site color tokens, mostly core values
  .framer-xxxxx       generated component/layout classes
  [data-framer-*]     runtime and component-state hooks
  ```
- **Class naming**: generated `.framer-*` hashes and responsive `hidden-*` utilities
- **Default theme**: dark (`#000000` hero field)
- **Font loading**: embedded `@font-face` and external font declarations; top families are `Inter`, `Inter Display`, `Inter Variable`
- **Canonical anchor**: centered homepage hero with "Build better sites, faster" and a bottom preview strip of real site cards

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Inter Display`
- **Body font**: `Inter`
- **Variable/body fallback**: `Inter Variable`, `Inter Variable Placeholder`, `sans-serif`
- **Code font**: `JetBrains Mono` appears in CSS; `Geist Mono`, `Azeret Mono`, and other demo fonts appear in preview/site examples
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --framer-font-family: "Inter", "Inter Variable", sans-serif;
  --framer-display-family: "Inter Display", "Inter", sans-serif;
  --framer-code-font-family: "JetBrains Mono", ui-monospace, monospace;
  --framer-font-weight-normal: 400;
  --framer-font-weight-bold: 700;
}

body {
  font-family: var(--framer-font-family);
  font-weight: var(--framer-font-weight-normal);
}

.hero-title {
  font-family: var(--framer-display-family);
  font-weight: var(--framer-font-weight-bold);
  letter-spacing: -0.05em;
}
```

### Note on Font Substitutes

- **Inter Display** — If exact display metrics are unavailable, use `Inter` or `Inter Variable` with tighter optical compensation.
  - Open-source 대안: **Inter** at weight `700` with `letter-spacing: -0.05em` for hero-scale text.
  - 보정: line-height should stay compact, around `0.92-1.02`, because the screenshot headline stacks large words tightly.
  - 보정: body copy may keep near-zero tracking (`-0.01px` appears frequently), but display text needs stronger negative tracking.
- **JetBrains Mono** — Use only for code/demo surfaces. It is not the homepage voice.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---:|---|---|
| hero-display | `clamp(72px, 9vw, 112px)` | 700 | `0.92-1.02` | `-0.05em` |
| hero-body | `22-26px` | 400 | `1.28-1.38` | `-0.01px` |
| section-heading | `44-64px` | 700 | `1.0-1.08` | `-0.04em` |
| card-title | `16-24px` | 500 / 700 | `1.2-1.35` | `0` to `-0.01px` |
| nav-link | `14px` | 400 | `1` | `0` |
| small-label | `13-14px` | 500 | `1.2` | `0` |

> ⚠️ Typography key insight: Framer's homepage is not "Inter generic". It is Inter with display-scale compression, large white mass, and muted gray subcopy.

### Principles

1. Hero type is built from mass and compression: huge white letters, tight line-height, and `-0.05em` style optical tightening.
2. Body copy does not compete with the headline. #999999 and regular weight keep it quiet.
3. Navigation is intentionally low-contrast. Links read as gray system chrome until action is needed.
4. Weight 500 is used in interface moments, but the main hero relies on the 400/700 split.
5. Demo/preview cards may introduce other fonts, but those are content examples, not the homepage system voice.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed accent steps)

| Token | Hex |
|---|---|
| `--selection-color` | `#0099FF` |
| `--token-7caf96a9-3685-4995-95cd-92a16705da21` | `#0099FF` |
| `--token-bd71055c-0a2c-4476-8cc9-4310acba652d` | `#0099FF` |
| `--token-eb0d9e00-7216-491c-99d5-7c1c2f3d0dbe` | `#0055FF` |
| `--token-0245ad54-dffa-4280-9b49-9d43ad68acaa` | `#6600FF` |

### 06-2. Brand Dark Variant

> N/A — the homepage uses a dark base, but not a separate named dark brand ramp. The dark identity comes from neutral surfaces.

### 06-3. Neutral Ramp

| Step | Light / Alpha | Dark / Solid |
|---|---|---|
| white | `#FFFFFF` | `#FFFFFF` |
| white-alpha-10 | `#FFFFFF1A` | `#FFFFFF1A` |
| white-alpha-08 | `#FFFFFF14` | `#FFFFFF14` |
| muted | `#999999` | `#999999` |
| card-ink | `#2B2B2B` | `#2B2B2B` |
| deep-card | `#080808` | `#080808` |
| near-black | `#1A1A1A` | `#1A1A1A` |
| base | `#000000` | `#000000` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Blue | primary selection/link | `#0099FF` |
| Blue deep | secondary accent | `#0055FF` |
| Purple | demo/accent token | `#6600FF` |
| Magenta | demo/accent token | `#FF0066` |
| Orange | demo/accent token | `#FD7702` |
| Yellow | demo/accent token | `#FFBB00` |
| Cyan | demo/accent token | `#00CCFF` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `{colors.surface-dark}` | `#000000` | page/hero background |
| `{colors.text-primary}` | `#FFFFFF` | hero headline, primary CTA surface |
| `{colors.text-muted}` | `#999999` | subcopy, nav links, secondary copy |
| `{colors.primary}` | `#0099FF` | selection, link/accent token, brand accent |
| `{colors.hairline-dark}` | `#FFFFFF1A` | dark borders and subtle separators |
| `{colors.surface-card}` | `#080808` | deep cards / preview regions |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--selection-color` | `#0099FF` | selected text color |
| `--selection-background-color` | `#0099FF4D` | selected text background |
| `--framer-link-hover-text-color` | `#FFFFFF99` fallback observed | hover text system |
| `--framer-code-text-color` | `#000000` fallback observed | rich text code fallback |
| `--token-c534b380-e14e-4ddc-9802-ad88d1f94f8e` | `#FFFFFF1A` | dark alpha surface/border token |
| `--token-5e0b3b72-9a97-43f8-96f2-85d741f3d8ca` | `#1D1D1D` | dark surface token |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---|---:|
| black | `#000000` | 134 |
| white | `#FFFFFF` | 85 |
| accent blue | `#0099FF` | 56 |
| white alpha | `#FFFFFF1A` | 56 |
| transparent black | `#00000000` | 50 |
| white alpha low | `#FFFFFF14` | 32 |
| white muted alpha | `#FFFFFF99` | 20 |
| card gray | `#2B2B2B` | 16 |
| muted gray | `#999999` | 14 |

### 06-8. Color Stories

**`{colors.surface-dark}` (`#000000`)** — The homepage stage. It lets the headline feel like a product launch title rather than a typical SaaS hero. Do not lighten it to dark gray unless a specific card surface calls for it.

**`{colors.text-primary}` (`#FFFFFF`)** — The main typographic material. It is used as mass, not decoration: hero H1, primary white CTA, and key contrast surfaces.

**`{colors.primary}` (`#0099FF`)** — A restrained system accent. It appears in selection/link/token data, but the homepage does not let it flood the hero.

**`{colors.hairline-dark}` (`#FFFFFF1A`)** — The dark-mode structural line. It creates edges while staying below the visible threshold of a conventional border.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `space-xs` | `8px` | small component gaps, icon/text pairing |
| `space-sm` | `10-16px` | pill padding, compact nav rhythm |
| `space-md` | `20-24px` | CTA groups, card inner spacing |
| `space-lg` | `40-48px` | hero copy to CTA separation |
| `space-xl` | `80-120px` | hero vertical breathing room |
| `container` | `1200px` | common max-width found repeatedly in CSS |

**주요 alias**:
- `container-max` -> `1200px` (dominant max-width)
- `desktop-break` -> `1200px` (desktop responsive threshold)
- `tablet-break` -> `810px` (tablet/mobile threshold)

### Whitespace Philosophy

Framer uses whitespace as theatrical delay. The hero keeps the nav small and high, then lets the headline occupy the center with enough black air that the words feel projected. The bottom preview strip begins within the first viewport, but it is pushed down far enough to read as evidence after the claim, not as clutter around it.

The page alternates between open stage and dense product shelf. Above the fold is sparse; below the fold can be crowded with thumbnails, cards, and examples because the black hero has already established control.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `radius-card-sm` | `8px` | small dark cards and preview chrome |
| `radius-card-md` | `10px` | repeated card/container radius |
| `radius-panel` | `15px` | larger panels |
| `radius-pill` | `100px` | CTAs, sign-up pill, capsule buttons |
| `radius-soft` | `20px` | larger marketing panels |
| `radius-inherit` | `inherit` | generated nested Framer component surfaces |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| ring-dark | `0 0 0 2px #090909` | dark UI rim |
| ring-light-alpha | `0 0 0 1px #FFFFFF1A` | subtle border on dark surfaces |
| card-low | `0 2px 4px #00000026, 0 1px #0000000D` | compact card depth |
| card-mixed | `0 2px 4px #0000001A, 0 1px #0000000D, 0 0 0 1px #FFFFFF26` | dark card separation |
| heavy-drop | `0 20px 30px #00000080` | large preview/image depth |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `color-transition-fast` | `color .2s cubic-bezier(.44,0,.56,1)` | text/link hover |
| `color-transition-base` | `color .3s cubic-bezier(.44,0,.56,1)` | slower nav/link color shift |
| `blur-soft` | `backdrop-filter: blur(5px)` | soft overlay surfaces |
| `blur-medium` | `backdrop-filter: blur(8px)` | floating dark chrome |
| `blur-strong` | `backdrop-filter: blur(10px)` | stronger overlay treatment |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `1200px`
- **Grid type**: generated Framer layout using flex and CSS grid; observed grids include `repeat(2,minmax(50px,1fr))` and 4-column variants
- **Column count**: hero is centered 1-column; product/example regions use 2- and 4-column grids
- **Gutter**: visually compact in preview strip, wider in content bands

### Hero

- **Pattern Summary**: `near-100vh + solid #000000 + centered H1 + dual pill CTA + bottom preview strip`
- Layout: one-column centered editorial hero
- Background: `#000000`
- **Background Treatment**: solid black stage; no gradient mesh in the hero screenshot
- H1: `clamp(72px, 9vw, 112px)` / weight `700` / tracking `-0.05em`
- Max-width: roughly `820-900px` for headline/copy stack

### Section Rhythm

```css
section {
  padding: 80px 20px;
  max-width: 1200px;
}
```

### Card Patterns

- **Card background**: `#080808`, `#1A1A1A`, or preview-image content
- **Card border**: `1px solid #FFFFFF1A` style alpha hairline
- **Card radius**: `8px` / `10px`
- **Card padding**: `16-24px`
- **Card shadow**: dark layered drops, typically black alpha
- **Hover effect**: color transitions are explicit; larger transform choreography was not fully measured in this pass

### Navigation Structure

- **Type**: horizontal desktop nav with logo left, center links, account actions right
- **Position**: top overlay/static visual placement in screenshot
- **Height**: compact, roughly `64px`
- **Background**: transparent over `#000000`
- **Border**: none visible in hero

### Content Width

- **Prose max-width**: `600-700px` for body copy zones
- **Container max-width**: `1200px`
- **Sidebar width**: N/A for homepage hero; no persistent sidebar observed

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `0-809.98px` | mobile hidden utilities and stacked layouts |
| Tablet | `810-1199.98px` | tablet-specific hidden utility range |
| Desktop | `1200px+` | full desktop nav and wide preview composition |
| Large | `1200px` container | repeated max-width anchor rather than a separate ultra-wide breakpoint |

### Touch Targets

- **Minimum tap size**: CTAs visually meet 44px target through pill padding and line-height.
- **Button height (mobile)**: not separately measured; desktop pills appear around `36-44px`.
- **Input height (mobile)**: not observed on homepage hero.

### Collapsing Strategy

- **Navigation**: hidden utility classes indicate separate desktop/tablet/mobile visibility variants.
- **Grid columns**: observed 4-column and 2-column grids collapse through media-specific generated classes.
- **Sidebar**: none in homepage surface.
- **Hero layout**: remains centered; type and preview strip scale down rather than converting to split layout.

### Image Behavior

- **Strategy**: preview tiles crop website screenshots and product examples into card frames.
- **Max-width**: `100%` appears frequently.
- **Aspect ratio handling**: image/card aspect ratios are controlled through Framer generated wrappers; exact aspect tokens were not isolated.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

| Component | Background | Text | Radius | Notes |
|---|---|---|---|---|
| Primary pill | `#FFFFFF` | `#000000` | `100px` | "Start for free" hero CTA |
| Secondary dark pill | `#2B2B2B` | `#FFFFFF` | `100px` | "Start with AI" CTA |
| Header signup | `#FFFFFF` | `#000000` | `100px` | compact nav action |
| Text login | transparent | `#999999` / `#FFFFFF` hover | none | quiet account action |

```html
<a class="framer-button framer-button-primary" href="/signup">Start for free</a>
<a class="framer-button framer-button-secondary" href="/ai">Start with AI</a>
```

States:
- hover: color transition around `.2s-.3s cubic-bezier(.44,0,.56,1)`
- focus: generated Framer focus outlines present in CSS, including transparent outline resets
- disabled/loading/error: not observed in homepage hero

### Badges

| Component | Background | Text | Radius | Notes |
|---|---|---|---|---|
| Announcement text link | transparent | `#FFFFFF` | none | "State of Sites '26 • Unlock the report now" |
| Small capsule labels | dark/alpha surfaces | `#FFFFFF` / `#999999` | pill or `8px` | appears in preview/demo surfaces |

### Cards & Containers

| Component | Background | Border | Radius | Shadow |
|---|---|---|---|---|
| Preview card | screenshot/image content | `#FFFFFF1A` | `10px` | black alpha drop |
| Dark tool card | `#080808` / `#1A1A1A` | `#FFFFFF1A` | `8-10px` | ring or low shadow |
| Cookie modal | `#FFFFFF` | none visible | `10px` | light modal over dark hero |

The cards are not generic white SaaS cards. They are either product screenshots or dark surfaces with subtle alpha structure.

### Navigation

| Element | Spec |
|---|---|
| Logo | white mark on black, compact left anchor |
| Center links | `14px`, `#999999`, regular weight |
| Active/hover | white or brighter gray via color transition |
| Right actions | "Log in" text + white "Sign up" pill |
| Mobile | inferred separate visibility classes, not screenshot-verified |

### Inputs & Forms

Homepage hero does not expose a canonical input field. Avoid inventing a form style from the hero. If an input is needed, derive it from the dark-card system:

| Property | Value |
|---|---|
| Background | `#080808` |
| Border | `1px solid #FFFFFF1A` |
| Text | `#FFFFFF` |
| Placeholder | `#999999` |
| Radius | `8px` or `10px` |
| Focus | narrow #0099FF accent, not a thick blue glow |

### Hero Section

| Property | Value |
|---|---|
| Background | `#000000` |
| Eyebrow | small centered white text |
| H1 | huge white `Inter Display`, weight 700, tight tracking |
| Body | muted #999999, centered, medium-width paragraph |
| CTA group | two pills: white primary, dark secondary |
| Evidence strip | website preview cards rising from bottom viewport |

### 13-2. Named Variants

#### `button-primary`

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Color | `#000000` |
| Radius | `100px` |
| Padding | `10px 16px` |
| Use | primary signup / start action |

#### `button-secondary-dark`

| Property | Value |
|---|---|
| Background | `#2B2B2B` |
| Color | `#FFFFFF` |
| Radius | `100px` |
| Padding | `10px 16px` |
| Use | secondary AI/product path |

#### `nav-link-muted`

| Property | Value |
|---|---|
| Color | `#999999` |
| Hover | `#FFFFFF` |
| Weight | `400` |
| Transition | `color .2s-.3s cubic-bezier(.44,0,.56,1)` |

#### `dark-preview-card`

| Property | Value |
|---|---|
| Background | `#080808` or screenshot media |
| Border | `1px solid #FFFFFF1A` |
| Radius | `10px` |
| Shadow | black alpha layered shadow |

### 13-3. Signature Micro-Specs

```yaml
black-stage-hero:
  description: "Pure black turns the homepage into a product launch stage instead of a normal SaaS landing page."
  technique: "background: #000000; centered single-column hero; transparent nav over the same field; no decorative gradient in the captured first viewport"
  applied_to: ["{component.hero-section}", "{component.navigation}"]
  visual_signature: "The first impression reads like a keynote title card: white claim, black room, almost no chrome."

compressed-inter-display-mass:
  description: "The hero headline is tightened until the words behave as one dense white object."
  technique: "font-family: Inter Display; font-weight: 700; font-size: clamp(72px, 9vw, 112px); line-height: .94; letter-spacing: -0.05em"
  applied_to: ["{component.hero-section}", "large marketing headlines"]
  visual_signature: "\"Build better sites, faster\" feels pressed into a single block rather than set as loose text."

alpha-white-hairline-chrome:
  description: "Dark surfaces are separated by translucent white scratches, not visible gray borders."
  technique: "border/ring colors use #FFFFFF1A and #FFFFFF14; card shadow can add 0 0 0 1px #FFFFFF26 only when needed"
  applied_to: ["{component.dark-preview-card}", "{component.dark-card}", "generated UI chrome"]
  visual_signature: "Edges exist only when the eye needs them, then disappear back into the black field."

preview-shelf-evidence-strip:
  description: "The product proof arrives as a bottom-edge shelf of real site previews."
  technique: "preview cards use radius around 10px, image/screenshot content, black alpha shadow such as 0 20px 30px #00000080, and first-viewport bottom overlap"
  applied_to: ["{component.hero-section}", "{component.dark-preview-card}"]
  visual_signature: "The claim is immediately followed by a studio desk of miniature websites instead of an explanatory feature grid."

restrained-blue-system-accent:
  description: "Framer blue is kept as system wiring, not the dominant hero surface."
  technique: "#0099FF appears as selection/link/accent token; selection background uses #0099FF4D; hero primary CTA remains #FFFFFF on #000000"
  applied_to: ["selection", "links", "focus/accent moments", "{component.button-primary}"]
  visual_signature: "The page is remembered as monochrome, with blue appearing only in narrow interactive flashes."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | short imperative/product outcome, no clever metaphor | "Build better sites, faster" |
| Primary CTA | direct creation verb | "Start for free" |
| Secondary CTA | product capability path | "Start with AI" |
| Subheading | trusted-by + capability list in one compact paragraph | "trusted by leading startups and Fortune 500 companies" |
| Tone | confident, designer-facing, practical | no long explainer in hero |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Framer-inspired dark SaaS launch surface */
:root {
  /* Fonts */
  --framer-font-family: "Inter", "Inter Variable", -apple-system, BlinkMacSystemFont, sans-serif;
  --framer-display-family: "Inter Display", "Inter", sans-serif;
  --framer-code-font-family: "JetBrains Mono", ui-monospace, monospace;
  --framer-font-weight-normal: 400;
  --framer-font-weight-bold: 700;

  /* Core colors */
  --framer-color-primary: #0099FF;
  --framer-bg-page: #000000;
  --framer-bg-card: #080808;
  --framer-bg-elevated: #2B2B2B;
  --framer-text: #FFFFFF;
  --framer-text-muted: #999999;
  --framer-border-dark: #FFFFFF1A;

  /* Spacing */
  --framer-space-sm: 12px;
  --framer-space-md: 24px;
  --framer-space-lg: 48px;
  --framer-space-xl: 96px;

  /* Radius */
  --framer-radius-card: 10px;
  --framer-radius-pill: 100px;
}

body {
  margin: 0;
  background: var(--framer-bg-page);
  color: var(--framer-text);
  font-family: var(--framer-font-family);
  font-weight: var(--framer-font-weight-normal);
  -webkit-font-smoothing: antialiased;
}

.framer-hero {
  min-height: 92vh;
  display: grid;
  place-items: center;
  text-align: center;
  padding: 96px 20px 40px;
  background: #000000;
}

.framer-hero h1 {
  max-width: 900px;
  margin: 0;
  font-family: var(--framer-display-family);
  font-size: clamp(72px, 9vw, 112px);
  line-height: .94;
  letter-spacing: -0.05em;
  font-weight: 700;
  color: #FFFFFF;
}

.framer-hero p {
  max-width: 620px;
  margin: 24px auto 0;
  color: #999999;
  font-size: clamp(20px, 2vw, 24px);
  line-height: 1.32;
}

.framer-button-row {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 24px;
}

.framer-button {
  border-radius: 100px;
  padding: 10px 16px;
  font: 500 14px/1 var(--framer-font-family);
  text-decoration: none;
  transition: color .2s cubic-bezier(.44,0,.56,1), background .2s cubic-bezier(.44,0,.56,1);
}

.framer-button-primary {
  background: #FFFFFF;
  color: #000000;
}

.framer-button-secondary {
  background: #2B2B2B;
  color: #FFFFFF;
}

.framer-card {
  background: #080808;
  border: 1px solid #FFFFFF1A;
  border-radius: 10px;
  box-shadow: 0 2px 4px #00000026, 0 1px #0000000D;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        framer: {
          blue: "#0099FF",
          black: "#000000",
          white: "#FFFFFF",
          muted: "#999999",
          card: "#080808",
          elevated: "#2B2B2B",
          hairline: "#FFFFFF1A",
        },
      },
      fontFamily: {
        sans: ["Inter", "Inter Variable", "system-ui", "sans-serif"],
        display: ["Inter Display", "Inter", "sans-serif"],
        mono: ["JetBrains Mono", "ui-monospace", "monospace"],
      },
      borderRadius: {
        framer: "10px",
        pill: "100px",
      },
      boxShadow: {
        "framer-card": "0 2px 4px #00000026, 0 1px #0000000D",
        "framer-heavy": "0 20px 30px #00000080",
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
| Brand primary | `{colors.primary}` | `#0099FF` |
| Background | `{colors.surface-dark}` | `#000000` |
| Text primary | `{colors.text-primary}` | `#FFFFFF` |
| Text muted | `{colors.text-muted}` | `#999999` |
| Border | `{colors.hairline-dark}` | `#FFFFFF1A` |
| Card | `{colors.surface-card}` | `#080808` |
| Elevated pill | `{colors.ink-card}` | `#2B2B2B` |

### Example Component Prompts

#### Hero Section

```text
Framer 스타일의 hero section을 만들어줘.
- 배경: #000000, gradient 없이 solid black stage
- H1: Inter Display, clamp(72px, 9vw, 112px), weight 700, line-height .94, letter-spacing -0.05em
- 본문: Inter 22-24px, color #999999, max-width 620px
- CTA: white pill primary (#FFFFFF text #000000) + dark pill secondary (#2B2B2B text #FFFFFF), radius 100px
- 하단: preview card shelf를 첫 viewport 하단에 일부 노출
```

#### Card Component

```text
Framer dark preview card를 만들어줘.
- background #080808 또는 실제 preview image
- border 1px solid #FFFFFF1A
- radius 10px
- shadow 0 2px 4px #00000026, 0 1px #0000000D
- 내부 텍스트는 #FFFFFF / #999999만 사용하고, blue accent는 링크나 focus에만 제한
```

#### Badge

```text
Framer announcement badge를 만들어줘.
- capsule을 과하게 만들지 말고, hero 위 작은 centered text로 처리
- font Inter 14px, weight 500
- color #FFFFFF 또는 #999999
- link accent는 필요할 때만 #0099FF
```

#### Navigation

```text
Framer homepage nav를 만들어줘.
- 배경은 transparent over #000000
- 좌측 white logo, 중앙 14px #999999 nav links, 우측 Log in + white Sign up pill
- hover는 color만 .2s cubic-bezier(.44,0,.56,1)
- border/shadow는 넣지 말 것
```

### Iteration Guide

- **색상 변경 시**: #0099FF를 전체 배경이나 큰 카드에 확장하지 말고 link/selection/focus로 제한.
- **폰트 변경 시**: Inter 계열을 유지하고 hero tracking 보정을 먼저 맞출 것.
- **여백 조정 시**: hero는 넓게, preview shelf는 밀도 있게. 둘을 같은 density로 만들지 말 것.
- **새 컴포넌트 추가 시**: card radius는 8-10px, button radius는 100px로 역할을 분리.
- **다크 모드**: 이 페이지는 이미 dark-first다. light palette로 뒤집지 말 것.
- **반응형**: 810px / 1200px threshold를 우선 사용하고 임의 breakpoint를 늘리지 말 것.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #000000 as the hero/page stage and let typography carry the brand.
- Keep hero headline white, huge, and tightly tracked.
- Use #999999 for supporting copy and nav links.
- Use #0099FF sparingly for selection, link, focus, or small accent moments.
- Use 100px pill radius for CTA buttons.
- Use #FFFFFF1A style alpha hairlines for dark cards.
- Let real preview/site imagery prove the product claim below the hero.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 hero/page base는 `#000000` 사용.
- 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — dark hero의 primary text는 `#FFFFFF` 사용.
- muted copy를 `#CCCCCC` 이상으로 밝히지 말 것 — Framer식 보조 텍스트는 `#999999`에 가깝게 둔다.
- primary surface를 `#0099FF` full button/background로 남발하지 말 것 — hero primary CTA는 `#FFFFFF` button이 맞다.
- dark card border를 `#FFFFFF`로 긋지 말 것 — 대신 `#FFFFFF1A` 같은 alpha hairline 사용.
- card background를 `#FFFFFF`로 만들지 말 것 — dark preview card는 `#080808` / `#1A1A1A` 계열 사용.
- CTA radius를 `8px` 카드처럼 만들지 말 것 — CTA는 `100px` pill, card는 `8-10px`.
- display heading에 `letter-spacing: 0`을 쓰지 말 것 — hero scale은 `-0.05em` 수준의 tight tracking 필요.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Broad blue brand wash: absent. #0099FF exists, but not as a hero flood.
- Light SaaS card grid: absent in the first impression. The hero is not a white dashboard landing page.
- Decorative gradient hero: absent in the captured first viewport. Solid black owns the stage.
- Heavy borders: absent. Structure uses #FFFFFF1A-style alpha hairlines.
- Square CTA buttons: never in the hero. CTAs are pill geometry.
- Loud navigation: absent. Nav links stay gray and secondary.
- Long explanatory hero copy: absent. One outcome headline plus compact capability sentence.
- Persistent sidebar: absent on homepage. This is marketing, not app-dashboard layout.
- Cartoon illustration: absent. Product evidence comes from website previews, not generic SVG scenes.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage pass** — This guide is based on the captured Framer homepage assets under `insane-design/framer/`, not every product, pricing, CMS, or enterprise sub-flow.
- **Desktop hero screenshot bias** — The screenshot evidence is desktop 1280x800. Mobile values are inferred from CSS breakpoints and hidden utility classes, not visually re-captured in this pass.
- **Generated token names** — Many tokens are UUID-style `--token-*`; semantic names in frontmatter are guide aliases mapped to observed values, not claimed official Framer token names.
- **Preview-card contamination** — Several fonts and accent colors come from embedded demo/preview sites. They are recorded as observed CSS values but not treated as Framer's core homepage identity.
- **Motion not fully executed** — CSS transition and blur values were observed, but scroll-triggered runtime choreography and Framer animation timelines were not instrumented.
- **Form states not surfaced** — Hero/homepage did not expose canonical input validation, loading, or error states. Input guidance is extrapolated from dark card tokens.
- **Dark theme mapping only** — The first impression is dark-first. A complete light-mode counterpart palette was not established.
- **Exact hero type size** — Screenshot-derived hero size is represented as a practical clamp, not a direct source token.
