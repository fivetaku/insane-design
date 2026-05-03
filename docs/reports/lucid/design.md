---
schema_version: 3.2
slug: lucid
service_name: Lucid
site_url: https://lucid.app
fetched_at: 2026-05-03T06:46:26Z
default_theme: light
brand_color: "#3C41C2"
primary_font: "Graphik LC Web"
font_weight_normal: 400
token_prefix: lucid

bold_direction: "Structured Collaboration"
aesthetic_category: "other"
signature_element: "minimal_extreme"
code_complexity: "medium"

medium: web
medium_confidence: high

archetype: app-dashboard
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Live login surface exposes a consistent product UI system, but not a public token catalog."

colors:
  brand-primary: "#3C41C2"
  ink-primary: "#282C33"
  text-muted: "#6F7681"
  surface-base: "#FFFFFF"
  surface-cookie: "#F2F3F5"
  border-subtle: "#CED4DB"
  link-secondary: "#3A414A"

typography:
  display: "Graphik LC Web"
  body: "Graphik LC Web"
  fallback: "sans-serif"
  ladder:
    - { token: h1, size: "32px", weight: 600, line_height: "40px", tracking: "normal" }
    - { token: card-title, size: "18px", weight: 600, line_height: "24px", tracking: "normal" }
    - { token: body, size: "16px", weight: 400, line_height: "20px", tracking: "normal" }
    - { token: control, size: "14px", weight: 400, line_height: "20px", tracking: "normal" }
    - { token: action, size: "14px", weight: 500, line_height: "20px", tracking: "normal" }
  weights_used: [400, 500, 600, 700]
  weights_absent: [300, 800, 900]

components:
  button-primary: { bg: "{colors.ink-primary}", fg: "{colors.surface-base}", radius: "4px", height: "44px", font: "18px / 600" }
  button-brand-small: { bg: "{colors.brand-primary}", fg: "{colors.surface-base}", radius: "2px", height: "40px", font: "14px / 500" }
  button-sso: { bg: "{colors.surface-base}", fg: "{colors.ink-primary}", radius: "2px", height: "40px", border: "1px solid #CED4DB" }
  input-text: { bg: "{colors.surface-base}", fg: "{colors.ink-primary}", radius: "2px", border: "1px solid #9AA1AB", height: "48px" }
  integration-card: { bg: "{colors.surface-base}", border: "1px solid #CED4DB", radius: "5px", width: "384px" }
---

# DESIGN.md - Lucid

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Lucid's `lucid.app` login page is not a marketing splash. It behaves like the clean reception desk before a shared drafting room: white floor, dark ink, compact form controls, and one small violet-blue entry point. The site does not try to sell collaboration with spectacle; it asks the user to pass through a precise work threshold. Almost everything is either #FFFFFF (`{colors.surface-base}`), #282C33 (`{colors.ink-primary}`), or #6F7681 (`{colors.text-muted}`), with #3C41C2 (`{colors.brand-primary}`) held back like the single illuminated "enter" key on an otherwise neutral console.

The composition uses a measured split. A 1040px content rail starts at x=120 on a 1280px viewport. The form column is 528px wide, the integration/benefit card is 384px wide, and the right column starts at x=776. This makes the page feel operational rather than promotional: left side is task completion, right side is reassurance. It has the negative space of a blank Lucidchart canvas, but before any diagram exists: the page is not the board, it is the quiet access gate to the board.

Typography is plain on purpose. `Graphik LC Web` holds every major product element, with `32px / 600` for the page title, `18px / 600` for major action labels, and `14px / 400-500` for controls and links. There is no negative tracking, no display-serif flourish, and no decorative typographic moment. The words feel like labels on a workflow panel, not captions in an ad campaign. Lucid's identity here is precision and legibility under repeated use.

The craft is in the small corrections: 68px header, 44px primary button, 48px text-field hit area, 40px SSO buttons, 4px primary radius, 5px card radius, and one faint 1px card border. The right card reads like a pinned note beside a diagram, not a second hero. There is no second brand color, no gradient wash, no rounded SaaS pillow, and almost no shadow; containment comes from hairline geometry and disciplined spacing. Even the cookie banner follows the same dark-action vocabulary: #282C33 (`{colors.ink-primary}`) buttons with white labels and low-radius corners.

Lucid의 화면은 결국 **공유 작업대 옆에 세워진 계기판 한 칸**처럼 작동한다. 528px form 컬럼은 엔지니어가 손을 얹는 작업대(workbench)이고, 384px context card는 그 작업대 위에 핀으로 꽂힌 설계도 한 장이다. 조종실의 콘솔처럼 `Next` 한 칸이 다음 게이트를 연다 — 로비 광고 무대가 아니라, Lucidchart 캔버스로 들어가기 직전의 엔지니어링 도구판이다. 스튜디오는 비어 있고 계기판만 켜져 있다. brand violet `#3C41C2`는 그 작업대 위 단 하나의 LED등이고, 나머지 모든 표면은 무광 도면지로 깔린다. 마케팅 쇼룸이 아니라, 다음 다이어그램을 시작하기 전의 공유 스튜디오 작업대다.

### Key Characteristics

- White application floor with almost no surface tint outside the cookie banner.
- Dark neutral action color #282C33 is more visually dominant than the brand blue.
- Brand blue #3C41C2 appears as a precise accent, not a page-wide theme.
- Header is functional: logo left, Join ID right, thin divider beneath.
- Login form is wide and quiet: 528px column, 48px input, 44px primary button.
- SSO options are stacked utility rows, not social-brand colored blocks.
- Right-side card uses a single #CED4DB hairline and 5px radius.
- Typography uses Graphik LC Web with normal letter-spacing throughout.
- UI depth is nearly flat; shadows are absent except a minor cookie close affordance.
- The page keeps product trust copy inside a bordered card instead of a marketing hero.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Structured Collaboration
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **minimal_extreme**으로 기억된다.
> **Code Complexity**: medium — runtime app styles and third-party cookie UI require computed-style extraction, but the visual system itself is flat and token-light.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Lucid처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Graphik LC Web", Arial, sans-serif;
  font-weight: 400;
  letter-spacing: normal;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #FFFFFF;
  --fg: #282C33;
  --muted: #6F7681;
}
body {
  background: var(--bg);
  color: var(--fg);
}

/* 3. 브랜드 컬러 */
:root { --brand: #3C41C2; }
```

**절대 하지 말아야 할 것 하나**: 브랜드 컬러 #3C41C2를 배경, 카드, 그라디언트, 대형 hero 장식에 펼치지 말 것. Lucid의 로그인 화면에서 brand는 작은 action accent이고, 주인공은 #282C33 ink다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://lucid.app` |
| Final URL | `https://lucid.app/users/login#/login` |
| Fetched | 2026-05-03T06:46:26Z |
| Extractor | curl Chrome UA + Playwright computed style |
| HTML size | 144261 bytes |
| CSS files | external CSS link 0개, inline style 843 chars, runtime/app styles via computed DOM |
| Token prefix | `lucid` |
| Method | live DOM computed style, screenshot, visible component measurement |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Client-rendered web app login surface. Public HTML shell is large, but CSS is not exposed as conventional `.css` links.
- **Design system**: Lucid product UI system - no public token namespace observed in the fetched login surface.
- **CSS architecture**: runtime/app styles rather than a static token file.
  ```text
  live DOM          computed styles from rendered controls
  app shell         login route HTML + JS-controlled UI
  third-party UI    cookie preference banner with its own Helvetica/Arial stack
  ```
- **Class naming**: not relied on; visual analysis uses rendered components and computed values.
- **Default theme**: light (page bg = `#FFFFFF`)
- **Font loading**: `Graphik LC Web` on product UI; cookie banner falls back to Helvetica/Arial multilingual stack.
- **Canonical anchor**: Login surface for Lucid Visual Collaboration Suite, not Lucid Motors automotive marketing.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Graphik LC Web` (proprietary/web-served product font)
- **Code font**: N/A - no code UI observed
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --lucid-font-family:       "Graphik LC Web", Arial, sans-serif;
  --lucid-font-family-code:  ui-monospace, SFMono-Regular, Menlo, monospace;
  --lucid-font-weight-normal: 400;
  --lucid-font-weight-medium: 500;
  --lucid-font-weight-bold:   600;
}
body {
  font-family: var(--lucid-font-family);
  font-weight: var(--lucid-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Graphik LC Web** is the product voice. If unavailable, use **Inter** or **IBM Plex Sans** only as an operational substitute, not as a visual upgrade.
- Keep the substitute at `400 / 500 / 600`. Do not introduce `300` for elegance; Lucid's login page is sturdy, not airy.
- Keep `letter-spacing: normal`. Display compression or negative tracking makes the `32px` H1 feel like a marketing headline, which is wrong here.
- If Inter is used, reduce body line-height pressure by keeping control labels at `14px / 20px`; do not let default browser `normal` create uneven form rows.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `h1-login-title` | 32px | 600 | 40px | normal |
| `card-title` | 18px | 600 | 24px | normal |
| `primary-button-label` | 18px | 600 | normal | normal |
| `body-copy` | 16px | 400 | 20px | normal |
| `control-label` | 14px | 400 | 20px | normal |
| `link-action` | 14px | 500 | 20px | normal |
| `cookie-action` | 16px | 700 | normal | normal |

> ⚠️ Typography key insight: the page gets hierarchy from weight and column geometry, not from a large type scale. The H1 is only 32px.

### Principles
<!-- SOURCE: manual -->

1. The `32px / 600` H1 is deliberately modest. It names the task, then gets out of the way.
2. `14px` is the control language. Labels, SSO options, utility links, and header actions live there.
3. Weight `500` is reserved for secondary actions like "Log in with password" and account links.
4. Weight `600` marks primary decision points: H1, primary button, and right-card heading.
5. Letter-spacing stays `normal`; this system avoids display-type optical tricks.
6. Cookie UI is typographically louder (`16px / 700`) because it is a separate consent widget, not the product surface.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed anchor)

| Token | Hex |
|---|---|
| `--lucid-color-brand-primary` | `#3C41C2` |

### 06-2. Brand Dark Variant

> N/A - no dark-mode brand ramp observed on this login surface.

### 06-3. Neutral Ramp

| Step | Light | Usage |
|---|---|---|
| 0 | `#FFFFFF` | page surface, nav surface, SSO button fill, card fill |
| 50 | `#F2F3F5` | cookie banner surface |
| 200 | `#CED4DB` | right card border |
| 500 | `#6F7681` | muted form labels and divider text |
| 700 | `#3A414A` | secondary cookie links |
| 900 | `#282C33` | primary ink and dark action fills |
| black | `#000000` | native checkbox/input fallback only |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Lucid action blue | primary | `#3C41C2` |
| Cookie/system dark | action | `#282C33` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `color.action.brand` | `#3C41C2` | Join ID, password link, checkbox selected state |
| `color.action.primary` | `#282C33` | Next button, cookie action buttons |
| `color.text.primary` | `#282C33` | H1, card heading, body links |
| `color.text.muted` | `#6F7681` | form labels, SSO button base color, divider |
| `color.surface.base` | `#FFFFFF` | application page and controls |
| `color.surface.consent` | `#F2F3F5` | cookie banner |
| `color.border.card` | `#CED4DB` | integration/benefit card border |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--lucid-bg-page` | `#FFFFFF` | body and main app shell |
| `--lucid-fg` | `#282C33` | default product copy |
| `--lucid-muted` | `#6F7681` | helper/control text |
| `--lucid-brand` | `#3C41C2` | small brand action |
| `--lucid-border-subtle` | `#CED4DB` | card edge |
| `--lucid-consent-bg` | `#F2F3F5` | cookie module only |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---|---:|
| `surface-base` | `#FFFFFF` | high |
| `ink-primary` | `#282C33` | high |
| `text-muted` | `#6F7681` | medium |
| `brand-primary` | `#3C41C2` | low |
| `surface-cookie` | `#F2F3F5` | low |
| `border-subtle` | `#CED4DB` | low |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.surface-base}` (`#FFFFFF`)** - The work floor. It lets the form and integration card feel like product UI rather than campaign material. No warmth, no cream, no tinted SaaS background.

**`{colors.ink-primary}` (`#282C33`)** - The actual dominant action color. It carries H1 text, product copy, the `Next` button, and cookie actions. This is the color that makes the page feel enterprise-ready.

**`{colors.text-muted}` (`#6F7681`)** - The control voice. It appears on labels, helper rows, and secondary UI, keeping the form quiet while still readable.

**`{colors.brand-primary}` (`#3C41C2`)** - A precise brand spark. Use it for small product actions and selected states only. It is not a background system.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--lucid-space-4` | 4px | checkbox/radius micro corrections |
| `--lucid-space-8` | 8px | internal button/content rhythm |
| `--lucid-space-12` | 12px | compact horizontal button padding |
| `--lucid-space-16` | 16px | label/control stack |
| `--lucid-space-24` | 24px | cookie/banner grouping |
| `--lucid-space-40` | 40px | major row and card title block |
| `--lucid-space-48` | 48px | input height and card inner offset |
| `--lucid-space-120` | 120px | desktop page rail inset |

**주요 alias**:
- `--lucid-rail-x` -> 120px (desktop content left/right rail)
- `--lucid-form-width` -> 528px (login form column)
- `--lucid-side-card-width` -> 384px (integration/benefit card)

### Whitespace Philosophy
<!-- SOURCE: manual -->

Lucid's whitespace is task-oriented. The top navigation consumes exactly 68px, then the title begins around y=108, leaving a clear 40px breath without turning the screen into a landing-page hero. The form begins at y=188; the page lets the user understand the task before presenting input.

The split layout is asymmetric but controlled. The left column is wider because authentication is the job. The right card is narrower and set apart by a 128px gutter from the form column, so it reads as context rather than distraction. This is "work first, reassurance second."

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `--lucid-radius-none` | 0px | page shell, nav, most structural wrappers |
| `--lucid-radius-control` | 2px | compact utility controls, SSO rows |
| `--lucid-radius-action` | 4px | primary dark buttons, cookie buttons |
| `--lucid-radius-card` | 5px | right-side integration/benefit card |
| `--lucid-radius-round` | 50% | cookie close button / circular affordance |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none | `none` | primary UI chrome, cards, form controls |
| minor-widget | `0 0 5px 0 rgb(128,128,128)` | cookie close affordance only |

Lucid's login page is intentionally flat. Depth is expressed by spacing, borders, and color contrast, not by elevation.

---

## 10. Motion
<!-- SOURCE: manual -->

| Token | Value | Usage |
|---|---|---|
| `--lucid-transition-basic` | `150ms-300ms ease` | assumed for hover/focus only; not visible in static capture |
| `--lucid-motion-page` | none observed | no hero animation or decorative motion captured |

> Motion is a known gap. The captured login state did not expose transition CSS in static stylesheets, and runtime interaction was not exhaustively tested.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: 1040px content rail inside 1280px viewport.
- **Grid type**: explicit two-column app composition.
- **Column count**: 2 primary columns.
- **Gutter**: approximately 128px between 528px form column and 384px context card.

### Hero
- **Pattern Summary**: 68px nav + 32px H1 + split login/form layout + right reassurance card.
- Layout: application login, not marketing hero. H1 spans above the form column.
- Background: `#FFFFFF` solid.
- **Background Treatment**: solid white with subtle abstract shape visible in screenshot, but no color-heavy treatment.
- H1: `32px` / weight `600` / tracking `normal`.
- Max-width: H1 content observed at 818px; main rail 1040px.

### Section Rhythm

```css
.lucid-login-shell {
  padding: 0 120px;
  max-width: 1280px;
}
.lucid-login-title {
  margin-top: 40px;
  margin-bottom: 40px;
}
.lucid-login-main {
  display: grid;
  grid-template-columns: 528px 384px;
  column-gap: 128px;
}
```

### Card Patterns
- **Card background**: `#FFFFFF`
- **Card border**: `1px solid #CED4DB`
- **Card radius**: `5px`
- **Card padding**: approximately 48px horizontal / 48px vertical in the observed card.
- **Card shadow**: none

### Navigation Structure
- **Type**: horizontal utility header.
- **Position**: static at page top.
- **Height**: 68px.
- **Background**: `#FFFFFF`.
- **Border**: bottom divider line visible beneath header.

### Content Width
- **Prose max-width**: 528px on login side; 286px heading inside right card.
- **Container max-width**: 1040px.
- **Sidebar width**: 384px context card, not a persistent sidebar.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | < 768px | likely single-column form-first layout; not visually recaptured in this run |
| Tablet | 768px | expected start of wider product shell |
| Desktop | 1280px | observed 1040px rail and two-column split |
| Large | > 1280px | likely centered max-width rail rather than expanded form controls |

### Touch Targets
- **Minimum tap size**: 40px for SSO rows and Join ID; 44px for primary Next.
- **Button height (mobile)**: not directly captured; desktop observed 40px / 44px.
- **Input height (mobile)**: not directly captured; desktop observed 48px input area.

### Collapsing Strategy
- **Navigation**: utility action should remain top-right or collapse under logo.
- **Grid columns**: two columns should collapse to form-first single column.
- **Sidebar**: right context card should move below auth options or disappear on narrow screens.
- **Hero layout**: no hero media; title stays above form.

### Image Behavior
- **Strategy**: logo and partner marks are small inline assets.
- **Max-width**: fixed-size marks within card.
- **Aspect ratio handling**: preserve SVG/logo aspect ratio; no cropping pattern observed.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary action (`button-primary`)**

| Property | Value |
|---|---|
| Text | `Next` |
| Size | 524px x 44px |
| Background | `#282C33` |
| Foreground | `#FFFFFF` |
| Radius | 4px |
| Font | `18px`, weight `600` |
| Border | none / invisible |

```html
<button class="lucid-button lucid-button--primary">Next</button>
```

**Brand utility (`button-brand-small`)**

| Property | Value |
|---|---|
| Text | `Enter Join ID` |
| Size | 140px x 40px |
| Background | `#3C41C2` |
| Foreground | `#FFFFFF` |
| Radius | 2px |
| Font | `14px`, weight `500` |

**SSO row (`button-sso`)**

| Property | Value |
|---|---|
| Text | `Log in with Google/Microsoft/Slack/SSO` |
| Size | 528px x 40px |
| Background | `#FFFFFF` |
| Foreground | `#282C33` label, muted wrapper |
| Radius | 2px |
| Border | `1px solid #CED4DB` equivalent visual edge |
| Font | `14px`, weight `400` |

### Badges

> N/A - no badge component observed on the login screen. Do not synthesize one.

### Cards & Containers

**Integration/benefit card**

| Property | Value |
|---|---|
| Position | x=776, y=188 |
| Size | 384px x 290px |
| Background | `#FFFFFF` |
| Border | `1px solid #CED4DB` |
| Radius | 5px |
| Shadow | none |
| Heading | `18px / 600`, 286px wide |

### Navigation

**Header**

| Property | Value |
|---|---|
| Height | 68px |
| Inner rail | 1040px, x=120 |
| Logo | left, 193px x 30px anchor area |
| Utility action | right, 140px x 40px |
| Background | `#FFFFFF` |
| Divider | subtle bottom line |

### Inputs & Forms

**Email / username input**

| Property | Value |
|---|---|
| Outer slot | 528px x 64px |
| Field body | 496px x 32px inside 48px label/input frame |
| Text | `14px / 400`, `#282C33` |
| Placeholder/label | `18px / 600`, `#6F7681` |
| Border | subtle gray input frame |
| Radius | 2px |

**Remember me**

| Property | Value |
|---|---|
| Checkbox | 24px visual hit |
| Label | `14px / 400`, `#6F7681` |
| Selected color | `#3C41C2` visual fill in screenshot |

### Hero Section

The login title is the hero. There is no oversized graphic hero, no product screenshot, and no CTA pair. Implement the hero as a compact product task header:

```html
<main class="lucid-login">
  <h1>Log in to access the Lucid Visual Collaboration Suite</h1>
  <div class="lucid-login__grid">
    <form class="lucid-login__form">...</form>
    <aside class="lucid-login__context-card">...</aside>
  </div>
</main>
```

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-primary-auth**

| Property | Value |
|---|---|
| Use | main progression in authentication |
| Background | `#282C33` |
| Text | `#FFFFFF`, `18px / 600` |
| Radius | 4px |
| Height | 44px |
| State note | hover should darken only slightly; do not add lift |

**button-brand-join-id**

| Property | Value |
|---|---|
| Use | top-right Join ID entry |
| Background | `#3C41C2` |
| Text | `#FFFFFF`, `14px / 500` |
| Radius | 2px |
| Height | 40px |
| State note | focus ring can reuse brand blue with alpha, but keep the fill solid |

**button-sso-provider**

| Property | Value |
|---|---|
| Use | third-party auth rows |
| Background | `#FFFFFF` |
| Text | `#282C33`, `14px / 400` |
| Border | light gray edge |
| Height | 40px |
| State note | logos provide color; button shell stays neutral |

**card-context-integrations**

| Property | Value |
|---|---|
| Use | right-side reassurance/partner card |
| Background | `#FFFFFF` |
| Border | `1px solid #CED4DB` |
| Radius | 5px |
| Shadow | none |

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
auth-split-rail:
  description: "Product-login layout that treats authentication as the primary work object."
  technique: "1040px desktop rail at x=120, 528px form column, 384px context card, ~128px column gap."
  applied_to: ["{component.login-shell}", "{component.login-form}", "{component.integration-card}"]
  visual_signature: "The form feels like the working surface; the right card reads as optional context, not a competing hero."

ink-first-primary-action:
  description: "Primary progression uses Lucid's dark neutral instead of the brand blue."
  technique: "background #282C33 /* {colors.ink-primary} */, color #FFFFFF /* {colors.surface-base} */, height 44px, radius 4px, font 18px / 600."
  applied_to: ["{component.button-primary}", "{component.cookie-action}"]
  visual_signature: "The main action lands like product ink on a white canvas; #3C41C2 never becomes the main button."

violet-blue-small-signal:
  description: "Brand color is compressed into utility actions and selected states."
  technique: "#3C41C2 /* {colors.brand-primary} */ on 140px x 40px Join ID button, password link emphasis, and selected checkbox; no panel fill or gradient."
  applied_to: ["{component.button-brand-small}", "{component.password-link}", "{component.checkbox-selected}"]
  visual_signature: "A single violet-blue spark sits inside a mostly neutral workflow surface."

hairline-context-card:
  description: "Right-side reassurance is contained by border geometry, not elevation."
  technique: "width 384px, min-height 290px, background #FFFFFF /* {colors.surface-base} */, border 1px solid #CED4DB /* {colors.border-subtle} */, radius 5px, box-shadow none, padding ~48px."
  applied_to: ["{component.integration-card}"]
  visual_signature: "The card feels like a pinned note beside the login task rather than a floating marketing module."

neutral-sso-stack:
  description: "Third-party auth choices are utility rows whose shells stay Lucid-neutral."
  technique: "528px x 40px rows, background #FFFFFF /* {colors.surface-base} */, text #282C33 /* {colors.ink-primary} */, border 1px solid #CED4DB /* {colors.border-subtle} */, radius 2px, font 14px / 400."
  applied_to: ["{component.button-sso}"]
  visual_signature: "Provider logos carry the only extra color while the button system remains flat and operational."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Task-first, explicit product-suite access | "Log in to access the Lucid Visual Collaboration Suite" |
| Primary CTA | One-word progression | "Next" |
| Secondary CTA | Authentication method, direct and unornamented | "Log in with password" |
| Utility CTA | Noun-driven product action | "Enter Join ID" |
| SSO labels | Provider-specific, parallel grammar | "Log in with Google" |
| Tone | Operational, trusted, low flourish | "Share your work via Lucid to enjoy:" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Lucid - copy into your root stylesheet */
:root {
  /* Fonts */
  --lucid-font-family: "Graphik LC Web", Arial, sans-serif;
  --lucid-font-family-code: ui-monospace, SFMono-Regular, Menlo, monospace;
  --lucid-font-weight-normal: 400;
  --lucid-font-weight-medium: 500;
  --lucid-font-weight-bold: 600;

  /* Brand and neutrals */
  --lucid-color-brand-500: #3C41C2;
  --lucid-bg-page: #FFFFFF;
  --lucid-bg-consent: #F2F3F5;
  --lucid-text: #282C33;
  --lucid-text-muted: #6F7681;
  --lucid-link-secondary: #3A414A;
  --lucid-border-subtle: #CED4DB;

  /* Key spacing */
  --lucid-space-xs: 4px;
  --lucid-space-sm: 8px;
  --lucid-space-md: 16px;
  --lucid-space-lg: 24px;
  --lucid-space-xl: 40px;
  --lucid-space-rail: 120px;

  /* Radius */
  --lucid-radius-control: 2px;
  --lucid-radius-action: 4px;
  --lucid-radius-card: 5px;
}

body {
  margin: 0;
  background: var(--lucid-bg-page);
  color: var(--lucid-text);
  font-family: var(--lucid-font-family);
  font-size: 16px;
  font-weight: var(--lucid-font-weight-normal);
  letter-spacing: normal;
}

.lucid-login-shell {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 var(--lucid-space-rail);
}

.lucid-login-nav {
  height: 68px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--lucid-border-subtle);
  background: #FFFFFF;
}

.lucid-login-title {
  margin: 40px 0;
  max-width: 818px;
  font-size: 32px;
  line-height: 40px;
  font-weight: 600;
}

.lucid-login-grid {
  display: grid;
  grid-template-columns: 528px 384px;
  column-gap: 128px;
  align-items: start;
}

.lucid-input {
  width: 100%;
  height: 48px;
  border: 1px solid #9AA1AB;
  border-radius: var(--lucid-radius-control);
  padding: 0 16px;
  color: var(--lucid-text);
  font: 400 14px / 20px var(--lucid-font-family);
}

.lucid-button-primary {
  width: 100%;
  height: 44px;
  border: 0;
  border-radius: var(--lucid-radius-action);
  background: #282C33;
  color: #FFFFFF;
  font: 600 18px / 20px var(--lucid-font-family);
}

.lucid-button-brand-small {
  height: 40px;
  padding: 0 12px;
  border: 0;
  border-radius: var(--lucid-radius-control);
  background: #3C41C2;
  color: #FFFFFF;
  font: 500 14px / 20px var(--lucid-font-family);
}

.lucid-sso-button {
  width: 100%;
  height: 40px;
  border: 1px solid var(--lucid-border-subtle);
  border-radius: var(--lucid-radius-control);
  background: #FFFFFF;
  color: var(--lucid-text);
  font: 400 14px / 20px var(--lucid-font-family);
}

.lucid-context-card {
  width: 384px;
  min-height: 290px;
  border: 1px solid #CED4DB;
  border-radius: var(--lucid-radius-card);
  background: #FFFFFF;
  box-shadow: none;
  padding: 48px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js - Lucid login surface
module.exports = {
  theme: {
    extend: {
      colors: {
        lucid: {
          brand: '#3C41C2',
          ink: '#282C33',
          muted: '#6F7681',
          surface: '#FFFFFF',
          consent: '#F2F3F5',
          border: '#CED4DB',
        },
      },
      fontFamily: {
        sans: ['Graphik LC Web', 'Arial', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
        semibold: '600',
      },
      borderRadius: {
        lucidControl: '2px',
        lucidAction: '4px',
        lucidCard: '5px',
      },
      spacing: {
        lucidRail: '120px',
        lucidForm: '528px',
        lucidCard: '384px',
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
| Brand primary | `{colors.brand-primary}` | `#3C41C2` |
| Background | `{colors.surface-base}` | `#FFFFFF` |
| Text primary | `{colors.ink-primary}` | `#282C33` |
| Text muted | `{colors.text-muted}` | `#6F7681` |
| Border | `{colors.border-subtle}` | `#CED4DB` |
| Consent surface | `{colors.surface-cookie}` | `#F2F3F5` |
| Secondary link | `{colors.link-secondary}` | `#3A414A` |

### Example Component Prompts

#### Login Shell

```text
Lucid 스타일의 앱 로그인 화면을 만들어줘.
- 배경: #FFFFFF, 전체 rail은 desktop에서 좌우 120px
- 폰트: Graphik LC Web, fallback Arial/sans-serif
- H1: 32px, weight 600, line-height 40px, color #282C33
- 레이아웃: 528px form column + 384px context card + 128px gutter
- 브랜드 컬러 #3C41C2는 Join ID와 작은 link에만 사용
```

#### Primary Auth Button

```text
Lucid 로그인의 primary button을 만들어줘.
- width: 100%, height: 44px
- background #282C33, text #FFFFFF
- radius 4px
- font Graphik LC Web, 18px, weight 600
- hover에서 shadow나 translate를 추가하지 말고 색만 아주 약하게 조정
```

#### Context Card

```text
Lucid 스타일의 오른쪽 context card를 만들어줘.
- width 384px, min-height 290px
- background #FFFFFF
- border 1px solid #CED4DB
- radius 5px, shadow none
- heading 18px / 600, color #282C33
- 내부 로고/아이콘은 작은 row로 배치하고 card 자체에는 brand fill 금지
```

### Iteration Guide

- **색상 변경 시**: `#3C41C2`를 primary fill로 확장하지 말고 small action으로 제한.
- **폰트 변경 시**: Graphik 부재 시 Inter/IBM Plex Sans를 쓰되 scale과 weight를 유지.
- **여백 조정 시**: form width 528px, right card 384px, desktop rail 120px 관계를 먼저 보존.
- **새 컴포넌트 추가 시**: radius는 2px/4px/5px 중 하나만 사용.
- **다크 모드**: 관측되지 않았으므로 임의 생성 금지.
- **반응형**: mobile에서는 right context card보다 form completion을 우선.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#282C33` as the main ink and primary action fill.
- Keep the page background `#FFFFFF` and let structure come from spacing.
- Reserve `#3C41C2` for Join ID, secondary action links, selected checkbox states, and focus accents.
- Use `Graphik LC Web` with 400/500/600 weights and normal tracking.
- Keep form controls wide and low-drama: 528px column, 48px input, 44px primary action.
- Use 1px borders and tiny radii instead of shadows for containment.
- Treat third-party provider logos as the only colorful elements inside SSO buttons.
- Keep the right card optional and quieter than the form column.

### ❌ DON'T

- 배경을 `#F7F7F5`, `#F5F5F7`, 또는 `#F2F3F5`로 두지 말 것 — page surface는 `#FFFFFF` 사용.
- 텍스트를 `#000000` 또는 pure black으로 두지 말 것 — primary text는 `#282C33` 사용.
- primary auth button을 `#3C41C2`로 두지 말 것 — `Next`는 `#282C33` fill 사용.
- muted label을 `#8A8F98`처럼 더 흐리게 두지 말 것 — observed muted text는 `#6F7681`.
- card border를 `#E5E7EB` generic gray로 두지 말 것 — right card edge는 `#CED4DB`.
- cookie/action dark button을 `#111111`로 두지 말 것 — Lucid action dark는 `#282C33`.
- body에 `font-weight: 300` 사용 금지 — observed product UI baseline은 400.
- H1에 `font-size: 56px` 이상 사용 금지 — login H1은 `32px`.
- controls에 `border-radius: 12px` 이상 사용 금지 — Lucid auth controls stay at 2px-5px.
- card에 `box-shadow: 0 10px 30px rgba(...)` 사용 금지 — right card shadow는 none.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- Brand gradient: none. No `#3C41C2` gradient mesh, no purple-blue marketing wash.
- Large brand surface: absent. Brand blue never becomes a hero panel or form background.
- Decorative card shadow: absent. The right card uses a hairline border only.
- Rounded SaaS pills: absent. Radius stays tight at 2px, 4px, and 5px.
- Oversized hero type: absent. The H1 is 32px, not a landing-page display headline.
- Multi-color UI palette: absent. Provider logos may be colorful; Lucid's own UI is not.
- Negative tracking: absent. Letter-spacing is normal across observed product text.
- Serif display moment: absent on `lucid.app` login even if other Lucid properties use different brand typography.
- Dense dashboard chrome: absent. No sidebar, table, toolbar, or canvas UI appears before login.
- Animated delight layer: absent in the captured state. No parallax, particles, or scroll reveal.
- Splash illustration scene over the workbench: zero. The work-surface is empty paper, not narrated.
- Gradient-filled login panel: never. Form column stays #FFFFFF, action column stays #282C33.
- Branded keyboard art / SSO collage decoration: absent. Provider logos carry their own color, the console stays neutral.
- Decorative LED indicator beyond the brand spark: none. Only `#3C41C2` lights up; no second console light pretends to be on.
- Drop-shadow under the form column: zero — the workbench is bolted flat, not floating.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Login-only surface** - Analysis is based on `https://lucid.app/users/login#/login`. Authenticated Lucidchart/Lucidspark canvas UI may use a richer component system.
- **Runtime CSS extraction** - The page did not expose conventional external `.css` links in the fetched HTML. Key values come from Playwright computed styles and screenshot inspection.
- **Cookie banner contamination** - Cookie consent UI uses a separate Helvetica/Arial stack and dark buttons. Its colors are documented but not treated as core product-auth tokens except where they mirror `#282C33`.
- **Mobile not visually recaptured** - Breakpoint behavior is inferred from desktop geometry and common app patterns. Exact mobile layout should be verified separately.
- **Hover/focus states incomplete** - Static capture did not exercise hover, focus, error, disabled, loading, or validation states.
- **Icon/logo internals excluded** - Google/Microsoft/Slack/Salesforce style marks are third-party assets and should not pollute Lucid's palette.
- **Dark mode not observed** - No dark-mode counterpart palette was visible on this unauthenticated login route.
- **Form error language absent** - Validation colors, helper copy, and field error borders were not triggered.
- **Old phase1 collision avoided** - Existing `insane-design/lucid` data included Lucid Motors automotive tokens; those were rejected because the requested URL is `lucid.app`.
