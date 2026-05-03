---
schema_version: 3.2
slug: notion
service_name: Notion
site_url: https://www.notion.so
fetched_at: 2026-04-20T19:30:00+09:00
default_theme: mixed
brand_color: "#097FE8"
primary_font: NotionInter
font_weight_normal: 400
token_prefix: notion

bold_direction: Warm Productivity
aesthetic_category: refined-saas
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "1107 CSS variables, named typography/color/radius/motion tokens, and component-level aliases are present, but the public page is a composed marketing surface rather than a published designer guidebook."

colors:
  background-base: "#FFFFFF"
  surface-neutral: "#F6F5F4"
  text-primary: "#191918"
  text-secondary: "#615D59"
  text-muted: "#78736F"
  border-soft: "#DFDCD9"
  accent-blue: "#097FE8"
  hero-night: "#050A35"
  hero-cta: "#4F63D9"
  teal-accent: "#03C1BA"
typography:
  display: "NotionInter"
  body: "NotionInter"
  serif: "Lyon Text"
  mono: "iA Writer Mono"
  ladder:
    - { token: "sans-200", size: "1rem", weight: 400, line_height: "1.5", tracking: "0" }
    - { token: "sans-600", size: "2rem", weight: 700, line_height: "2.5rem", tracking: "-0.046875rem" }
    - { token: "sans-800", size: "3.375rem", weight: 700, line_height: "3.5rem", tracking: "-0.1171875rem" }
    - { token: "sans-1000", size: "4.75rem", weight: 700, line_height: "5rem", tracking: "-0.15625rem" }
  weights_used: [400, 500, 600, 700]
  weights_absent: [300, 800]
components:
  button-primary: { bg: "{colors.hero-cta}", color: "#FFFFFF", radius: "0.5rem", padding: "8px 16px" }
  button-secondary-dark: { bg: "#2B3C9B", color: "#FFFFFF", radius: "0.5rem", padding: "8px 16px" }
  workspace-window: { bg: "#FFFFFF", radius: "12px", shadow: "var(--shadow-level-300)" }
  bento-card: { bg: "{colors.surface-neutral}", radius: "12px", padding: "24px" }
---

# DESIGN.md - Notion

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Notion's marketing surface is a midnight canvas holding a centered product promise in a night-shift workspace — a stage set for AI-era work that refuses to become a generic blue dashboard. The first viewport is theatrical: a deep midnight plane, a huge centered headline, a glowing product window, and hand-drawn companion icons orbiting the workspace like small signals on a late-night editorial board.

The old Notion identity still sits underneath. Its neutral system remains warm: `#F6F5F4` (`{colors.surface-neutral}`), `#191918` (`{colors.text-primary}`), `#615D59` (`{colors.text-secondary}`), and soft hairlines from the gray ramp. That warmth matters because it keeps the AI story from becoming a parchment of generic tech blue. The public hero can go dark, but the product chrome returns to the familiar paper-and-ink workspace — less "AI dashboard" than a desk lamp left on over a shared notebook.

The signature move is the contrast between "night canvas" and "daylight document." A deep blue hero field carries the AI narrative, then a white workspace mockup lands in the middle with board columns, side navigation, small agents, task pills, comments, and app badges. The contrast says: AI is active in the background, but work still resolves into readable documents, databases, and tasks. The site has the rhythm of a theater after closing: the room is dark, the crew is still moving, and the only fully lit object is the work table.

Typography is dense and engineered. `NotionInter` is used as the primary sans, with large headings pulled tight through negative tracking tokens. Body text stays calm and legible, while display text gets compressed enough to feel like a product launch editorial headline. The display text has ink pressure rather than poster gloss: letters feel pressed into the midnight canvas, while the product UI returns to small document labels and database chips. The illustrated accents are deliberately loose around a disciplined workspace frame — no second brand color show; `{colors.accent-blue}` handles action while paper neutrals do the organizing. Shadow belongs to the workspace window, the one object that must feel touchable.

### Key Characteristics

- Dark midnight hero field with white centered display type and blue CTAs.
- Warm Notion neutrals under the marketing layer: `#F6F5F4`, `#DFDCD9`, `#191918`.
- Product-window hero mockup with a database board, sidebar, and floating comments.
- Hand-drawn AI/agent icons used as orbiting detail, not as full-page illustration.
- `NotionInter` variable sans with tight display tracking and normal-weight body copy.
- Radius scale clusters around `0.375rem`, `0.5rem`, `0.75rem`, and `12px`.
- Multi-layer elevation is used for product surfaces; flat color handles most page structure.
- Breakpoints are tokenized and dense: `600px`, `840px`, `1080px`, `1280px`, `1440px`.
- The system favors useful component states over decorative color variety.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Warm Productivity
> **Aesthetic Category**: refined-saas
> **Signature Element**: 이 사이트는 **midnight AI stage wrapped around a warm document workspace**으로 기억된다.
> **Code Complexity**: high — tokenized typography/color/radius/motion plus hero illustration choreography and layered product-window elevation.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Notion처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "NotionInter", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
  letter-spacing: 0;
}

/* 2. warm workspace neutrals */
:root {
  --notion-bg: #FFFFFF;
  --notion-surface: #F6F5F4;
  --notion-fg: #191918;
  --notion-muted: #615D59;
}

/* 3. public marketing accent */
:root {
  --notion-accent: #097FE8;
  --notion-hero-night: #050A35;
  --notion-hero-cta: #4F63D9;
}
```

**절대 하지 말아야 할 것 하나**: Notion을 순수 흰색/검정/파란색만 있는 generic SaaS로 만들지 말 것. `#F6F5F4` warm neutral과 tight-tracked NotionInter display가 빠지면 Notion의 종이 같은 업무감이 사라진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.notion.so` |
| Fetched | 2026-04-20T19:30:00+09:00 |
| Extractor | reused phase1 HTML/CSS/screenshots |
| HTML size | 264160 bytes |
| CSS files | 15 external files, 793895 aggregate chars |
| Token prefix | `notion` |
| Method | existing phase1 JSON + CSS variable/token inspection + screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React/Next-style static application shell inferred from hashed CSS assets and serialized page payload.
- **Design system**: Notion marketing/product token layer - prefix appears as direct variables rather than a single namespace (`--color-*`, `--font-*`, `--typography-*`, `--spacing-*`, `--shadow-*`, `--motion-*`).
- **CSS architecture**:
  ```css
  --color-gray-*          warm neutral ramp
  --color-blue-*          action/accent ramp
  --font-size-*           type ladder
  --typography-sans-*     font shorthand + tracking aliases
  --spacing-*             4px/rem scale plus section aliases
  --shadow-level-*        layered elevation
  --motion-*              duration/easing aliases
  ```
- **Class naming**: CSS Modules style with semantic component fragments plus hashes, for example `footer_button__vbjiT`.
- **Default theme**: `mixed`; the first viewport is dark marketing, the product surface is light.
- **Font loading**: custom brand fonts are referenced as `NotionInter`, `Lyon Text`, and `iA Writer Mono`, with explicit fallback stacks.
- **Canonical anchor**: the hero workspace mockup, not the logo. It is the visible proof that Notion AI still lands inside the familiar workspace.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `NotionInter` (custom brand build)
- **Body font**: `NotionInter`
- **Serif font**: `Lyon Text`
- **Code font**: `iA Writer Mono`
- **Weight normal / bold**: `400` / `700`
- **Observed weights**: `400`, `500`, `600`, `700`; variable aliases also define `420`, `520`, `620`, `680`.

```css
:root {
  --notion-font-family: "NotionInter", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  --notion-font-family-serif: "Lyon Text", Georgia, serif;
  --notion-font-family-code: "iA Writer Mono", Menlo, Courier, monospace;
  --notion-font-weight-normal: 400;
  --notion-font-weight-medium: 500;
  --notion-font-weight-semibold: 600;
  --notion-font-weight-bold: 700;
}
```

### Note on Font Substitutes

- **NotionInter substitute**: use `Inter` with `font-weight: 400/600/700`. Keep body letter-spacing at `0`; apply negative tracking only on large display sizes.
- **Display compensation**: for H1/H2, use `letter-spacing: -0.04em` to `-0.03em` when using Inter. Notion's tokens are absolute rem values, but the visual intent is tight display compression.
- **Lyon Text substitute**: use `Georgia` only for editorial callouts or quote-like content. Do not make the main homepage serif.
- **iA Writer Mono substitute**: use `Menlo` or `ui-monospace` for code/technical labels, not for product navigation.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `font-size-100` | `0.875rem` | 400/500 | `1.25rem` | `0` |
| `font-size-150` | `0.9375rem` | 400/600 | `1.25rem` | `0` |
| `font-size-200` | `1rem` | 400/600/700 | `1.5rem` | `0` |
| `font-size-300` | `1.125rem` | 600/700 | `1.75rem` | `-0.0078125rem` |
| `font-size-500` | `1.625rem` | 700 | `2rem` | `-0.0390625rem` |
| `font-size-700` | `2.625rem` | 700 | `3rem` | `-0.09375rem` |
| `font-size-800` | `3.375rem` | 700 | `3.5rem` | `-0.1171875rem` |
| `font-size-1000` | `4.75rem` | 700 | `5rem` | `-0.15625rem` |

> Key insight: Notion's display type is not just bold; it is optically tightened. The headline works because large sizes compress while body copy remains neutral.

### Principles

1. Display text gets the compression; body text does not. This preserves document readability under marketing scale.
2. Weight `500` exists for UI affordances, but the main emotional jump is from `400` body to `700` display.
3. Serif is a supporting texture, not the homepage voice. `Lyon Text` should appear as editorial relief only.
4. The scale is product-native: many sizes cluster around `14px`, `15px`, `16px`, `18px`, and `20px` for dense UI text.
5. Large marketing headlines should keep line-height tight enough to feel engineered, not poster-loose.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (9 steps)

| Token | Hex |
|---|---|
| `--color-blue-100` | `#F2F9FF` |
| `--color-blue-200` | `#E6F3FE` |
| `--color-blue-300` | `#93CDFE` |
| `--color-blue-400` | `#62AEF0` |
| `--color-blue-500` | `#097FE8` |
| `--color-blue-600` | `#0075DE` |
| `--color-blue-700` | `#005BAB` |
| `--color-blue-800` | `#00396B` |
| `--color-blue-900` | `#002A4F` |

### 06-2. Brand Dark Variant

| Token | Hex | Usage |
|---|---|---|
| `hero-night` | `#050A35` | first viewport night field |
| `hero-cta` | `#4F63D9` | captured primary hero button |
| `button-secondary-dark` | `#2B3C9B` | darker secondary CTA plane |

### 06-3. Neutral Ramp

| Step | Light warm neutral | Usage |
|---|---|---|
| 100 | `#F9F9F8` | faint canvas |
| 200 | `#F6F5F4` | neutral surface |
| 300 | `#DFDCD9` | borders / hairlines |
| 400 | `#A39E98` | disabled / low emphasis |
| 500 | `#78736F` | muted text |
| 600 | `#615D59` | secondary text |
| 700 | `#494744` | strong secondary |
| 800 | `#31302E` | near-primary |
| 900 | `#191918` | primary ink |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Teal | `--color-teal-500` | `#27918D` |
| Green | `--color-green-500` | `#1AAE39` |
| Yellow | `--color-yellow-500` | `#FFB110` |
| Orange | `--color-orange-500` | `#FF6D00` |
| Red | `--color-red-500` | `#F64932` |
| Purple | `--color-purple-500` | `#9849E8` |
| Pink | `--color-pink-500` | `#FF64C8` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--color-background-base` | `#FFFFFF` | default workspace/card base |
| `--color-background-surface-neutral` | `#F6F5F4` | warm panels |
| `--color-background-surface-accent` | `#62AEF0` | accent surfaces |
| `--color-accent-strong` | `#097FE8` | primary links/actions |
| `--color-gray-900` | `#191918` | primary text |
| `--color-gray-600` | `#615D59` | secondary text |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--color-accent` | `--color-blue-400` | general accent |
| `--color-accent-strong` | `--color-blue-500` | stronger action |
| `--color-accent-soft` | `--color-blue-200` | soft action surface |
| `--color-background-base-hover` | `--color-alpha-black-100` | hover overlay |
| `--color-background-surface-neutral-hover` | `--color-gray-300` | neutral hover |

### 06-7. Dominant Colors (actual CSS frequency order)

| Token | Hex | Frequency |
|---|---|---|
| transparent black | `#0000` | 104 |
| white | `#FFFFFF` / `#FFF` | 44+ |
| black | `#000000` / `#000` | 38+ |
| alpha black 10 | `#0000001A` | 8 |
| alpha black 75 | `#000000BF` | 8 |
| warm neutral | `#F6F5F4` | 4 |
| warm canvas | `#F7F7F5` | 3 |
| teal special | `#03C1BA` | 3 |

### 06-8. Color Stories

**`{colors.hero-night}` (`#050A35`)** — This is the marketing-stage color, not the whole brand. Use it for the AI "night shift" story and first-viewport drama; return to warm light surfaces for actual workspace UI.

**`{colors.surface-neutral}` (`#F6F5F4`)** — The warm paper floor. It keeps Notion from feeling like sterile enterprise software and should replace cold `#F5F5F5` wherever a product panel needs softness.

**`{colors.text-primary}` (`#191918`)** — Warm ink, almost black but not pure black. It belongs on document-like surfaces and keeps the product layer readable without harsh contrast.

**`{colors.accent-blue}` (`#097FE8`)** — Functional action blue. Use it for semantic action states, links, and selected accents; do not flood the page with it because Notion's identity is carried by neutral workspace structure.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--spacing-4` | `0.25rem` | tiny icon/link gaps |
| `--spacing-8` | `0.5rem` | compact UI gap |
| `--spacing-12` | `0.75rem` | button internal rhythm |
| `--spacing-16` | `1rem` | dense card/UI block |
| `--spacing-24` | `1.5rem` | common component gap |
| `--spacing-32` | `2rem` | card/block padding |
| `--spacing-64` | `4rem` | section inner breath |
| `--spacing-80` | `5rem` | major vertical spacing |
| `--spacing-160` | `10rem` | large section rhythm |
| `--spacing-section` | `var(--spacing-160)` | primary section cadence |

**주요 alias**:
- `--spacing-card-padding-inline` -> `var(--spacing-16)` for compact cards.
- `--spacing-card-padding-inline-block` -> `var(--spacing-32)` for block cards.
- `--spacing-block-s/m/l` -> `20px / 24px / 32px` for composed content modules.

### Whitespace Philosophy

Notion's whitespace is not a luxury-site void. It alternates between theatrical hero air and dense product utility. The hero leaves enough room for a large headline and a glowing product window, but the mock workspace itself is intentionally busy: sidebar, tabs, task cards, comments, avatars, app badges, and columns all coexist.

The spacing system therefore needs two modes: `64px`-plus breathing room for marketing bands and `8px`/`16px`/`24px` utility spacing inside product surfaces. If everything is spacious, it stops feeling like Notion; if everything is dense, the AI story loses its stage.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| `--border-radius-200` | `0.25rem` | tiny controls |
| `--border-radius-300` | `0.3125rem` | compact UI |
| `--border-radius-400` | `0.375rem` | standard UI radius |
| `--border-radius-500` | `0.5rem` | buttons / panels |
| `--border-radius-700` | `0.75rem` | larger cards |
| `--border-radius-round` | `624.9375rem` | circular/pill forms |
| observed literal | `12px` | hero/product window cards |
| observed literal | `50%` / `100%` | avatars, circular badges |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `--shadow-level-100` | `0px 3px 9px #00000008, 0px 0.7px 1.4625px rgba(0,0,0,.015)` | light lift |
| `--shadow-level-200` | `0px 4px 18px #0000000A, 0px 2.025px 7.84688px rgba(0,0,0,.027), 0px 0.8px 2.925px #00000005, 0px 0.175px 1.04062px rgba(0,0,0,.013)` | card/product chrome |
| `--shadow-level-300` | `0px 20px 50px #00000014, 0px 6px 16px #0000000A` | hero window / elevated panel |
| focus ring | `0 0 0 2px #000000, 0 0 0 4px #FFFFFF` | accessibility emphasis |

Shadow is multi-layer and low-opacity. It should look like a product surface is lit by the page, not like a generic card floating with a single heavy blur.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `--motion-duration-100` | `100ms` | small response |
| `--motion-duration-150` | `150ms` | fade-in |
| `--motion-duration-200` | `200ms` | fade-out |
| `--motion-duration-300` | `300ms` | transform |
| `--motion-timing-function-ease-in-out-quint` | `cubic-bezier(0.86,0,0.07,1)` | stronger transform curve |
| `--motion-global-transform-duration` | `var(--motion-duration-300)` | illustration/product movement |

Motion should be felt as gentle task routing and UI response. Avoid springy consumer-app bounce unless it is tied to the hand-drawn agent motif.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `1252px` appears as a repeated wide container; `1200px`, `1184px`, `960px`, `839px`, and `600px` appear as local widths.
- **Grid type**: CSS Grid and Flexbox mix; marketing rows use responsive column counts while product UI uses flex/table-like database layouts.
- **Column count**: observed responsive values include `1`, `2`, `3`, `4`, `6`, and logo wall counts up to `9`.
- **Gutter**: common gaps are `8px`, `12px`, `16px`, `24px`, `32px`, `64px`, and `80px`.

### Hero

- **Pattern Summary**: `dark theatrical hero + centered H1 + dual CTA + large floating workspace mockup`.
- **Layout**: centered marketing stack above a full-width product-window composition.
- **Background**: dark midnight blue with illustrated orbit paths and small app/agent icons.
- **Background Treatment**: `solid/dark-gradient stage + glowing workspace screenshot + hand-drawn orbit details`.
- **H1**: large NotionInter bold, tight tracking; visually around `64px` on desktop.
- **Max-width**: headline and copy are centered, while the product mockup spans most of the viewport width.

### Section Rhythm

```css
section {
  padding-block: var(--spacing-80) var(--spacing-160);
  padding-inline: var(--spacing-24);
  max-width: 1252px;
}
```

### Card Patterns

- **Card background**: `#FFFFFF` for product chrome, `#F6F5F4` for neutral panels.
- **Card border**: warm gray hairline, typically `#DFDCD9` or alpha black.
- **Card radius**: `8px` to `12px`; product window is a larger `12px`.
- **Card padding**: `16px`, `24px`, or `32px` depending on density.
- **Card shadow**: `--shadow-level-200`/`--shadow-level-300` for hero and elevated cards.

### Navigation Structure

- **Type**: horizontal desktop nav with dropdown indicators; compact login/CTA group on the right.
- **Position**: top-of-page header under announcement bar in the capture.
- **Height**: visually about `72px` header plus a separate slim announcement bar.
- **Background**: transparent/dark in hero context.
- **Border**: none in the hero; separation comes from contrast and vertical placement.

### Content Width

- **Prose max-width**: `600px` appears as a common text width.
- **Container max-width**: `1252px` for wide marketing compositions.
- **Sidebar width**: product mockup sidebar is visually about `165px`, compact enough to keep the board dominant.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `375px` / `400px` / `440px` | small-device adjustments |
| Tablet | `600px` / `668px` | first layout expansion |
| Desktop | `840px` / `1080px` | main marketing layout changes |
| Large | `1280px` / `1440px` | full hero/container expression |

### Touch Targets

- **Minimum tap size**: use at least `44px`; header CTAs in the screenshot are visually above this.
- **Button height (mobile)**: target `40px`-`48px`.
- **Input height (mobile)**: target `40px`-`48px` for product-like forms.

### Collapsing Strategy

- **Navigation**: desktop horizontal nav should collapse into a menu before content crowds.
- **Grid columns**: multi-column marketing rows collapse toward 1 column below `600px`/`840px`.
- **Sidebar**: product mockups should crop or simplify, not shrink all text to illegibility.
- **Hero layout**: preserve headline/CTA first, then reduce the workspace screenshot height and peripheral doodle density.

### Image Behavior

- **Strategy**: product-window media should keep a stable aspect ratio and crop from the edges if needed.
- **Max-width**: `100%`.
- **Aspect ratio handling**: variables such as `--mobile-hero-media-aspect-ratio` and `--desktop-hero-media-aspect-ratio` indicate explicit responsive media ratios.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

Primary CTAs are rounded rectangles with enough radius to feel soft but not pill-only. In the captured hero, the primary button uses a saturated periwinkle-blue surface with white text; the secondary uses a darker blue plane.

```html
<a class="notion-button notion-button--primary">Get Notion free</a>
<a class="notion-button notion-button--secondary-dark">Request a demo</a>
```

| State | Spec |
|---|---|
| default | `background: #4F63D9; color: #FFFFFF; border-radius: 0.5rem; padding: 8px 16px` |
| hover | slightly deepen surface or apply `--color-alpha-white-100` overlay |
| focus | use dual focus ring, `0 0 0 2px #000000, 0 0 0 4px #FFFFFF` |
| disabled | reduce opacity and avoid changing radius |

### Badges

Badges appear more as product/database pills than marketing capsules. They carry status color softly: lavender for to-do, yellow for in-progress, blue for review, green for complete.

```html
<span class="notion-status notion-status--review">In review</span>
```

| State | Spec |
|---|---|
| default | small type, low-saturation background, compact horizontal padding |
| active | keep text readable; do not increase saturation dramatically |

### Cards & Containers

Containers are warm, light, and useful. The hero workspace window has the strongest elevation; internal cards stay flatter.

```html
<section class="notion-window">
  <aside class="notion-sidebar"></aside>
  <div class="notion-board-card">Weekly sales status report</div>
</section>
```

| Part | Spec |
|---|---|
| product window | `#FFFFFF`, `12px`, `--shadow-level-300` |
| board card | `#FFFFFF`, `8px`, subtle alpha shadow |
| neutral panel | `#F6F5F4`, `12px`, low or no shadow |

### Navigation

Navigation is text-led and compact. Dropdown arrows are small; the CTA on the right is the most visible item.

```html
<nav class="notion-nav">
  <a>Product</a>
  <a>AI</a>
  <a>Solutions</a>
  <a class="notion-nav__cta">Get Notion free</a>
</nav>
```

| Part | Spec |
|---|---|
| link | white or warm ink depending on background, medium weight |
| dropdown | small chevron, 4px-8px gap |
| CTA | filled blue rounded rectangle |

### Inputs & Forms

The homepage capture does not foreground form fields, but the token system includes Marketo/form focus shadows. Use product-style inputs: white surface, warm gray border, blue focus ring.

```html
<input class="notion-input" placeholder="Search docs, projects, and people" />
```

| State | Spec |
|---|---|
| default | `background: #FFFFFF; border: 1px solid #DFDCD9; border-radius: 0.5rem` |
| focus | `box-shadow: inset 0 0 0 1px #2383E291, 0 0 0 2px #2383E259` |
| error | use red ramp, not generic browser red |

### Hero Section

The hero component is a two-layer composition: narrative stack plus product proof.

```html
<section class="notion-hero notion-hero--night">
  <h1>Meet the night shift.</h1>
  <p>Notion agents keep work moving 24/7.</p>
  <div class="notion-hero__actions">...</div>
  <div class="notion-hero__workspace-window">...</div>
</section>
```

| Part | Spec |
|---|---|
| hero background | `#050A35` dark stage |
| headline | `NotionInter`, `700`, tight tracking, white |
| subcopy | muted white, centered, max `600px` |
| media | large white workspace window with layered shadow |
| accents | hand-drawn orbit icons around the window |

### 13-2. Named Variants

| Variant | Spec | Notes |
|---|---|---|
| `button-primary-hero` | `#4F63D9` bg, `#FFFFFF` text, `0.5rem` radius | captured "Get Notion free" hero CTA |
| `button-secondary-dark` | darker blue bg, `#FFFFFF` text, `0.5rem` radius | captured "Request a demo" CTA |
| `button-nav-primary` | compact blue rounded rectangle | top-right acquisition CTA |
| `workspace-window` | `#FFFFFF`, `12px`, `--shadow-level-300` | hero product proof |
| `database-status-pill` | soft colored background + compact label | board columns and task states |
| `agent-orbit-icon` | small illustrated tile/badge | use sparingly around hero only |

### 13-3. Signature Micro-Specs

```yaml
midnight-ai-workbench:
  description: "Dark AI theater wraps a familiar light workspace instead of turning the product UI dark."
  technique: "hero field #050A35 /* {colors.hero-night} */ + white display type + #FFFFFF workspace window with 12px radius"
  applied_to: ["{component.hero-section}", "{component.workspace-window}"]
  visual_signature: "A night-shift stage where the only fully lit object is the Notion work table."

warm-paper-ink-ramp:
  description: "Workspace neutrals stay warm and document-like under the marketing layer."
  technique: "#F6F5F4 /* {colors.surface-neutral} */ + #DFDCD9 /* {colors.border-soft} */ + #191918 /* {colors.text-primary} */"
  applied_to: ["{component.bento-card}", "{component.workspace-window}", "{component.database-status-pill}"]
  visual_signature: "The interface reads as paper, ink, and soft gray dividers rather than cold SaaS chrome."

notion-tight-display-compression:
  description: "Large sans headlines are optically compressed while body copy remains neutral."
  technique: "NotionInter 700 with tracking tokens -0.1171875rem and -0.15625rem on display sizes"
  applied_to: ["{component.hero-section}", "{component.marketing-heading}"]
  visual_signature: "Big words feel pressed and engineered, not airy or editorial."

low-opacity-product-window-elevation:
  description: "Product proof lifts through stacked faint shadows rather than a single card shadow."
  technique: "--shadow-level-300: 0px 20px 50px #00000014, 0px 6px 16px #0000000A; --shadow-level-200 uses four low-alpha layers"
  applied_to: ["{component.workspace-window}", "{component.elevated-card}"]
  visual_signature: "The hero mockup feels like a real app surface lit by the page."

black-white-accessible-focus-ring:
  description: "Focus treatment uses a stark two-ring system instead of brand-blue glow."
  technique: "box-shadow: 0 0 0 2px #000000, 0 0 0 4px #FFFFFF"
  applied_to: ["{component.button-primary}", "{component.button-secondary-dark}", "{component.button-nav-primary}"]
  visual_signature: "Keyboard focus appears as a precise ink-and-paper outline, consistent with Notion's document identity."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | short operational metaphor | "Meet the night shift." |
| Primary CTA | direct free-start action | "Get Notion free" |
| Secondary CTA | sales path, plain language | "Request a demo" |
| Subheading | explain capability in one sentence | "Notion agents keep work moving 24/7." |
| Tone | confident, plain, work-centered | "You assign the tasks. Notion Agent does the work." |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Notion-inspired core tokens */
:root {
  /* Fonts */
  --notion-font-family: "NotionInter", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  --notion-font-family-serif: "Lyon Text", Georgia, serif;
  --notion-font-family-code: "iA Writer Mono", Menlo, Courier, monospace;
  --notion-font-weight-normal: 400;
  --notion-font-weight-medium: 500;
  --notion-font-weight-semibold: 600;
  --notion-font-weight-bold: 700;

  /* Brand/action */
  --notion-color-brand-100: #F2F9FF;
  --notion-color-brand-300: #93CDFE;
  --notion-color-brand-500: #097FE8;
  --notion-color-brand-600: #0075DE;
  --notion-color-brand-900: #002A4F;

  /* Surfaces */
  --notion-bg-page: #FFFFFF;
  --notion-bg-neutral: #F6F5F4;
  --notion-bg-hero: #050A35;
  --notion-text: #191918;
  --notion-text-muted: #615D59;
  --notion-border: #DFDCD9;

  /* Spacing */
  --notion-space-xs: 0.5rem;
  --notion-space-sm: 1rem;
  --notion-space-md: 1.5rem;
  --notion-space-lg: 4rem;
  --notion-space-xl: 10rem;

  /* Radius */
  --notion-radius-sm: 0.375rem;
  --notion-radius-md: 0.5rem;
  --notion-radius-lg: 0.75rem;
  --notion-radius-round: 624.9375rem;

  /* Shadows */
  --notion-shadow-100: 0px 3px 9px #00000008, 0px 0.7px 1.4625px rgba(0,0,0,.015);
  --notion-shadow-200: 0px 4px 18px #0000000A, 0px 2.025px 7.84688px rgba(0,0,0,.027), 0px 0.8px 2.925px #00000005, 0px 0.175px 1.04062px rgba(0,0,0,.013);
  --notion-shadow-300: 0px 20px 50px #00000014, 0px 6px 16px #0000000A;
}

.notion-hero {
  background: var(--notion-bg-hero);
  color: #FFFFFF;
  font-family: var(--notion-font-family);
  text-align: center;
  padding: 80px 24px 0;
}

.notion-hero h1 {
  margin: 0;
  font-size: clamp(3.375rem, 7vw, 4.75rem);
  line-height: 1.05;
  font-weight: var(--notion-font-weight-bold);
  letter-spacing: -0.04em;
}

.notion-window {
  background: #FFFFFF;
  color: var(--notion-text);
  border-radius: 12px;
  box-shadow: var(--notion-shadow-300);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        notion: {
          ink: '#191918',
          muted: '#615D59',
          paper: '#FFFFFF',
          warm: '#F6F5F4',
          border: '#DFDCD9',
          blue: '#097FE8',
          night: '#050A35',
        },
      },
      fontFamily: {
        sans: ['NotionInter', 'Inter', 'system-ui', 'sans-serif'],
        serif: ['Lyon Text', 'Georgia', 'serif'],
        mono: ['iA Writer Mono', 'Menlo', 'monospace'],
      },
      borderRadius: {
        notion: '0.5rem',
        'notion-lg': '0.75rem',
      },
      boxShadow: {
        notion: '0px 4px 18px #0000000A, 0px 2.025px 7.84688px rgba(0,0,0,.027), 0px 0.8px 2.925px #00000005',
      },
    },
  },
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: auto+manual -->

### Quick Color Reference

| Role | Hex |
|---|---|
| Hero night | `#050A35` |
| Primary action | `#097FE8` |
| Hero CTA | `#4F63D9` |
| Workspace base | `#FFFFFF` |
| Warm neutral | `#F6F5F4` |
| Primary text | `#191918` |
| Secondary text | `#615D59` |
| Hairline | `#DFDCD9` |

### Example Component Prompts

**Hero Section**: Build a Notion-like AI workspace hero with a dark `#050A35` background, centered `NotionInter` headline at `clamp(3.375rem, 7vw, 4.75rem)`, tight negative tracking, two blue CTAs, and a large white `12px` radius workspace window with layered soft shadow.

**Workspace Card**: Create a warm document-style product card using `#FFFFFF` on `#F6F5F4`, `#191918` text, `#615D59` secondary text, `#DFDCD9` border, `8px` to `12px` radius, and low-opacity multi-layer shadow.

**Navigation**: Use compact horizontal links in `NotionInter` with small chevrons, a right-side filled CTA, and no heavy border when over the dark hero.

**Status Pill**: Use small rounded database pills with low-saturation background colors. Keep labels compact and product-like; never make them marketing badges.

### Iteration Guide

- Preserve the warm neutral ramp before tuning accent colors.
- Keep display tracking tight and body tracking at `0`.
- Put dark-blue drama in hero/marketing zones only; product surfaces should remain light and readable.
- Use layered shadows for elevated product windows, not single heavy card shadows.
- Let illustrated/doodle accents orbit the workspace; do not turn them into full-page decoration.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO

- Use `#F6F5F4` and `#191918` to recreate the warm workspace layer.
- Use `#050A35` only when the page needs the AI night-stage mood.
- Use `NotionInter` or Inter with tight display tracking for large headings.
- Keep product UI dense enough to show real work: sidebars, tabs, columns, cards, and comments.
- Use `8px`-`12px` radius for most surfaces and reserve pill/circle radius for badges or avatars.
- Use low-opacity multi-layer shadows for product windows.
- Keep CTA copy plain and direct.

### DON'T

- 배경을 `#FFFFFF` 하나로만 두지 말 것 — 대신 workspace sections에는 `#F6F5F4`, hero에는 `#050A35` 사용.
- 텍스트를 `#000000` 또는 `black`으로 고정하지 말 것 — 대신 primary ink는 `#191918`, secondary는 `#615D59` 사용.
- warm border를 `#E5E7EB`로 대체하지 말 것 — 대신 `#DFDCD9` 사용.
- primary action을 generic purple `#7C3AED`로 만들지 말 것 — 대신 semantic action에는 `#097FE8`, hero CTA에는 `#4F63D9` 사용.
- hero dark를 flat `#000000` 또는 `#111827`로 만들지 말 것 — 대신 `#050A35` 계열 night field 사용.
- body에 `font-weight: 300` 사용 금지 — Notion body는 `400`이 기본이다.
- 모든 heading에 letter-spacing `0` 사용 금지 — large display는 negative tracking을 적용한다.
- product window에 단일 `box-shadow: 0 20px 40px #00000040` 사용 금지 — low-opacity layered shadow를 쓴다.

### 🚫 What This Site Doesn't Use

- No cold gray SaaS floor as the main identity; the neutral ramp is warm.
- No all-over gradient mesh; the first viewport is primarily a dark stage with controlled accents.
- No neon cyberpunk AI treatment; the AI story stays work-centered.
- No heavy glassmorphism for core product chrome.
- No oversized rounded-card dashboard cliche; cards remain product-dense.
- No pure monochrome identity; action blue and small accent families are present but controlled.
- No serif-led homepage voice; serif is a supporting asset.
- No decorative shadows on every container; elevation is scoped to product proof and interactive surfaces.
- No emoji-first tone; illustrated icons are brand-crafted and restrained.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- The analysis reuses existing phase1 assets from `insane-design/notion/`; no live refetch was performed in this run.
- The screenshot captures a specific Notion homepage state focused on "Meet the night shift." Notion may A/B test hero copy, imagery, CTA color, and announcement bars.
- CSS Modules hashes identify component fragments, but exact React component names are not recoverable from the static CSS alone.
- Some colors in frequency output come from SVGs, badges, logo walls, illustrations, and alpha utility tokens; they were filtered manually for design significance.
- The first viewport is dark, but the broader Notion design system is mixed/light. `default_theme: mixed` is intentional.
- `brand_color: #097FE8` reflects semantic action blue in the extracted token ramp, while the captured hero CTA visually uses a periwinkle-blue marketing button.
- Signature micro-specs are inferred from screenshot + CSS token behavior; they are not official Notion naming.
