---
schema_version: 3.2
slug: toss
service_name: Toss
site_url: https://toss.im
fetched_at: 2026-04-20
default_theme: light
brand_color: "#3182F6"
primary_font: Toss Product Sans
font_weight_normal: 400
token_prefix: toss

bold_direction: "Friendly Fintech"
aesthetic_category: "Soft-Fintech Minimal"
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high

archetype: landing-utility
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "874 CSS variables, Toss Product Sans, color/radius/shadow tokens, and p-* component classes show a production design system in use."

colors:
  primary: "#3182F6"
  primary-soft: "#E8F3FF"
  primary-hover: "#1B64DA"
  surface: "#FFFFFF"
  surface-muted: "#F2F4F6"
  text-primary: "#191F28"
  text-secondary: "#4E5968"
  text-muted: "#6B7684"
  border: "#E5E8EB"
  error: "#F04452"

typography:
  display: "Toss Product Sans"
  body: "Toss Product Sans"
  emoji: "Tossface"
  ladder:
    - { token: display, size: "56-72px", weight: 700, line_height: "1.15", tracking: "0" }
    - { token: h1, size: "56px", weight: 700, line_height: "1.3", tracking: "0" }
    - { token: h2, size: "48px", weight: 700, line_height: "1.3", tracking: "0" }
    - { token: h3, size: "36px", weight: 700, line_height: "1.3", tracking: "0" }
    - { token: body, size: "15px", weight: 400, line_height: "1.6", tracking: "0" }
    - { token: small, size: "13px", weight: 400, line_height: "1.6", tracking: "0" }
  weights_used: [300, 400, 500, 600, 700, 800, 900, 950]
  weights_absent: []

components:
  button-primary: { bg: "{colors.primary}", fg: "#FFFFFF", radius: "8px", padding: "11px 18px" }
  button-primary-large: { bg: "{colors.primary}", fg: "#FFFFFF", radius: "8px", padding: "14px 24px" }
  button-weak-primary: { bg: "{colors.primary-soft}", fg: "{colors.primary-hover}", radius: "8px" }
  card-shadow-outline: { bg: "{colors.surface}", radius: "16-20px", shadow: "var(--shadow-s) -> var(--shadow-l)" }
  navbar: { height: "varies, desktop horizontal", bg: "{colors.surface}", fg: "{colors.text-secondary}" }
---

# DESIGN.md - Toss (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Toss reads like a consumer dashboard rendered in app-grade canvas — finance made tangible before it feels institutional. The screen opens on a full-viewport light-blue financial miniature set, then drops the user into generous white sections, large Korean headlines, and simple app-store CTAs. The emotional contract is clear: the ledger should feel welcoming before it feels powerful.

The visual center is Toss Blue #3182F6 (`{colors.primary}`), but the page does not flood itself blue. Blue appears as a precise active state, CTA color, link accent, and logo signal. The actual page mass is #FFFFFF (`{colors.surface}`), pale blue imagery, and the grey-mauve text ladder from #191F28 (`{colors.text-primary}`) through #6B7684 (`{colors.text-muted}`). This restraint is why the page feels trustworthy rather than promotional.

Typography carries more brand weight than decoration. `Toss Product Sans` appears overwhelmingly across the CSS; `Tossface` is reserved for emoji/pictogram surfaces, and Basier Square is only a small English-title helper. The Korean display type is large, blunt, and calm: no negative tracking tricks, no editorial serif contrast, no luxury thinness. Toss chooses legibility and warmth.

The craft lives in the app-like chassis: 100vh hero image, 250px desktop section padding, 100px mobile section padding, rounded product cards, soft multi-layer shadows, and component classes like `.p-button`, `.p-cardV2`, `.p-navbar`, `.p-container`. It behaves like a mobile design system translated to the web, not like a generic SaaS landing page.

좀 더 풀어 그리면, Toss 홈은 **아침 햇살 든 은행 창구**처럼 작동한다. 흰 표면은 새 입금 봉투의 종이결이고, Toss Blue는 창구 직원의 이름표 색이며, 둥근 카드는 카운터에 놓인 안내 책자처럼 모서리가 다 깎여 있다. 큰 hero 이미지는 ATM 화면이 아니라 어린이 은행 체험 부스의 입체 모형 같다 — 위협적이지 않은 축소된 도시 풍경. CTA 버튼은 신권 지폐처럼 깨끗하고, 입력 필드는 동전 분류기처럼 정확하게 슬롯이 잘려 있다. 두 번째 브랜드 컬러가 없는 이유: 은행 카운터는 산만한 색을 허용하지 않는다.

### Key Characteristics

- Single-primary Toss Blue #3182F6 with a complete blue ramp.
- Near-black text is #191F28, never raw #000000.
- White and pale grey surfaces dominate; color is used as action, not wallpaper.
- Toss Product Sans is the brand voice; Tossface is a separate pictogram layer.
- Large Korean hero typography, centered over a soft 3D financial scene.
- Desktop sections breathe at 250px vertical padding; mobile compresses to 100px.
- Radius ladder is practical: 4px, 8px, 16px, 20px, 24px.
- Shadows are layered and low-opacity, built from grey opacity tokens.
- Component system is visible through `.p-*` classes and CSS variables.
- Motion and hover are short, app-like, and tactile.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Friendly Fintech
> **Aesthetic Category**: Soft-Fintech Minimal
> **Signature Element**: 이 사이트는 **100vh pale-blue hero world + Toss Blue action system**으로 기억된다.
> **Code Complexity**: medium — CSS token system, Emotion runtime styles, app-like components, and soft motion require disciplined implementation.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Toss처럼 만들기 - 3가지만 하면 80%

```css
/* 1. Font + weight */
body {
  font-family: "Toss Product Sans", "Apple SD Gothic Neo", "Noto Sans KR",
    -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
  line-height: 1.6;
}

/* 2. Background + text */
:root {
  --toss-bg: #FFFFFF;
  --toss-fg: #191F28;
  --toss-muted: #6B7684;
}
body {
  background: var(--toss-bg);
  color: var(--toss-fg);
}

/* 3. Brand action */
:root {
  --toss-blue: #3182F6;
  --toss-blue-hover: #1B64DA;
  --toss-blue-soft: #E8F3FF;
}
```

**절대 하지 말아야 할 것 하나**: 본문과 헤드라인을 `#000000`으로 두지 말 것 — Toss의 기준 텍스트는 #191F28이고, 이 약간 푸른 near-black이 금융의 딱딱함을 줄인다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://toss.im` |
| Fetched | 2026-04-20 |
| Extractor | existing phase1 reuse: HTML + CSS + screenshot |
| HTML size | 99,561 bytes |
| CSS files | 7 external/combined CSS files, about 884,209 CSS characters |
| Token prefix | `toss` / raw CSS variables such as `--blue500`, `--grey900`, `--radius-m` |
| Method | CSS custom properties, component class inspection, screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js-like SSR with Emotion runtime style tags.
- **Design system**: Toss UI in production use — `.p-button`, `.p-cardV2`, `.p-navbar`, `.p-container`, `.pAlert`, `.p-tab`.
- **CSS architecture**:
  ```text
  core tokens       --blue500 / --grey900 / --radius-m / --shadow-s
  component vars    --btn-bg-base / --btn-border-radius / --pButton-background-color
  runtime classes   .p-button / .p-cardV2 / .css-* emotion classes
  ```
- **Class naming**: hybrid of stable `.p-*` product-system classes and generated Emotion `.css-*` classes.
- **Default theme**: light, with dark token counterparts present but not dominant on the homepage.
- **Font loading**: custom web fonts (`Toss Product Sans`, `Tossface`, Basier Square) plus Korean/system fallbacks.
- **Canonical anchor**: the hero image and App Store / Google Play buttons establish the homepage as app acquisition plus trust brand.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Toss Product Sans` (proprietary/self-hosted Toss brand font).
- **Body font**: `Toss Product Sans`.
- **Emoji/Pictogram font**: `Tossface`.
- **English helper**: `Basier Square`.
- **Korean fallback**: `Apple SD Gothic Neo`, `Noto Sans KR`, `SF Pro KR`.
- **Code font**: `SFMono-Regular`, `Menlo`, `Consolas`, `Monaco`, `Andale Mono`, `Ubuntu Mono`, monospace.
- **Weight normal / bold**: `400` / `700`, with 300, 500, 600, 800, 900, 950 also present.

```css
:root {
  --toss-font-family: "Toss Product Sans", "Tossface", -apple-system,
    BlinkMacSystemFont, "Apple SD Gothic Neo", "Noto Sans KR", "Segoe UI",
    Roboto, "Helvetica Neue", Arial, sans-serif;
  --toss-font-family-code: SFMono-Regular, Menlo, Consolas, Monaco,
    "Andale Mono", "Ubuntu Mono", monospace;
  --toss-font-weight-normal: 400;
  --toss-font-weight-bold: 700;
}
body {
  font-family: var(--toss-font-family);
  font-weight: var(--toss-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Toss Product Sans** — if unavailable, use **Pretendard** or **Noto Sans KR** at the same nominal weight. Keep line-height at `1.6` for body and `1.3` for section headings; do not tighten Korean copy to an English SaaS rhythm.
- **Display compensation** — Toss does not rely on negative tracking. Keep `letter-spacing: 0`; compensate by using weight 700 and generous vertical spacing.
- **Tossface** — if unavailable, do not replace it with random emoji art. Use simple monochrome icons or app screenshots instead.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| xsmall | 11px | 400 | 1.6 | 0 |
| small | 13px | 400 | 1.6 | 0 |
| body | 15px | 400 | 1.6 | 0 |
| body-large | 17px | 400/500 | 1.6 | 0 |
| h6 | 20px | 600/700 | 1.6 | 0 |
| h5 | 24px | 600/700 | 1.6 | 0 |
| h4 | 32px | 700 | 1.3 | 0 |
| h3 | 36px | 700 | 1.3 | 0 |
| h2 | 48px | 700 | 1.3 | 0 |
| h1 | 56px | 700 | 1.3 | 0 |
| hero-display | 60-72px | 700/800 | 1.15-1.4 | 0 |

> ⚠️ Toss looks wrong when recreated with default 16px/24px SaaS typography. Its body base is often 15px with line-height 1.6, while Korean display headings jump to 56px+ without letter-spacing tricks.

### Principles
<!-- SOURCE: manual -->

1. Body text is often 15px, not the generic 16px default — density is app-like.
2. Korean display type depends on weight and line-height, not negative tracking.
3. The 500/600 weights are real functional middle states for nav, labels, and product UI.
4. Huge hero text can coexist with warm friendliness because the color is #191F28, not #000000.
5. Tossface is a separate symbolic layer; do not mix emoji decoration into normal text.
6. Typography is system-wide, not campaign-specific. Reuse the ladder instead of inventing per-section sizes.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (10 steps)
<!-- --blue* -->

| Token | Hex |
|---|---|
| `--blue50` | `#E8F3FF` |
| `--blue100` | `#C9E2FF` |
| `--blue200` | `#90C2FF` |
| `--blue300` | `#64A8FF` |
| `--blue400` | `#4593FC` |
| `--blue500` | `#3182F6` |
| `--blue600` | `#2272EB` |
| `--blue700` | `#1B64DA` |
| `--blue800` | `#1957C2` |
| `--blue900` | `#194AA6` |

### 06-2. Brand Dark Variant
<!-- SOURCE: auto -->

| Token | Hex |
|---|---|
| `--darkThemeBlue50` | `#202C4D` |
| `--darkThemeBlue100` | `#23386A` |
| `--darkThemeBlue200` | `#25478C` |
| `--darkThemeBlue300` | `#265AB3` |
| `--darkThemeBlue400` | `#2970D9` |
| `--darkThemeBlue500` | `#3485FA` |
| `--darkThemeBlue600` | `#449BFF` |
| `--darkThemeBlue700` | `#61B0FF` |
| `--darkThemeBlue800` | `#8FCDFF` |
| `--darkThemeBlue900` | `#C8E7FF` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light (`grey`) | Dark (`inverseGrey`) |
|---|---|---|
| 50 | `#F9FAFB` | `#202027` |
| 100 | `#F2F4F6` | `#2C2C35` |
| 200 | `#E5E8EB` | `#3C3C47` |
| 300 | `#D1D6DB` | `#4D4D59` |
| 400 | `#B0B8C1` | `#62626D` |
| 500 | `#8B95A1` | `#7E7E87` |
| 600 | `#6B7684` | `#9E9EA4` |
| 700 | `#4E5968` | `#C3C3C6` |
| 800 | `#333D4B` | `#E4E4E5` |
| 900 | `#191F28` | `#FFFFFF` |

### 06-4. Accent Families
<!-- SOURCE: auto -->

| Family | Key step | Hex |
|---|---|---|
| Red | 500 | `#F04452` |
| Red hover | 600 | `#E42939` |
| Red active | 700 | `#D22030` |
| Orange | observed family | `#DD7D02` |
| Green | observed family | CSS token family present |
| Teal | observed family | CSS token family present |
| Purple | observed family | CSS token family present |

### 06-5. Semantic
<!-- SOURCE: auto+manual -->

| Token | Hex | Usage |
|---|---|---|
| `--background` | `#FFFFFF` | page background |
| `--greyBackground` | `#F2F4F6` | muted section background |
| `--blue500` | `#3182F6` | active link, primary CTA, focus ring |
| `--grey900` | `#191F28` | primary text |
| `--grey700` | `#4E5968` | secondary text |
| `--grey600` | `#6B7684` | muted text, nav links |
| `--grey200` | `#E5E8EB` | border/divider |
| `--red500` | `#F04452` | destructive/error |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--btn-bg-base` | `--grey100` | default button background |
| `--btn-color-base` | `--greyOpacity700` | default button text |
| `--btn-danger-bg` | `--red500` | destructive button fill |
| `--btn-danger-weak-bg` | `--red50` | weak destructive background |
| `--btn-danger-weak-color` | `--red700` | weak destructive text |
| `--btn-border-radius` | literal / `--radius-m` | button radius |
| `--pButton-background-color` | theme-specific | product button skin |

### 06-7. Dominant Colors (actual CSS frequency)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---|---|
| surface | `#FFFFFF` | 205 |
| grey-800 | `#333D4B` | 93 |
| blue-500 | `#3182F6` | 90 |
| grey-700 | `#4E5968` | 83 |
| grey-100 | `#F2F4F6` | 73 |
| grey-500 | `#8B95A1` | 66 |
| grey-900 | `#191F28` | 56 |
| grey-600 | `#6B7684` | 56 |

### Color Stories
<!-- SOURCE: manual -->

**`{colors.primary}` (#3182F6)** — Toss Blue is the action signal, not a background wash. Use it for primary CTA, active anchor states, focus rings, and brand moments; avoid turning whole sections into solid blue.

**`{colors.surface}` (#FFFFFF)** — White is the trust floor. It lets the pale blue 3D hero and app UI imagery feel fresh while keeping financial content sober.

**`{colors.text-primary}` (#191F28)** — The text is near-black with a blue-grey undertone. It is the difference between friendly fintech and old financial software.

**`{colors.border}` (#E5E8EB)** — Hairlines stay soft and structural. They separate controls without creating heavy enterprise tables.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

Toss uses a practical 4px base for component spacing, then jumps to large editorial bands for homepage rhythm.

| Token | Value | Use case |
|---|---|---|
| `space-1` | 4px | icon nudge, compact gap |
| `space-2` | 8px | button/icon gap, radius-m sibling |
| `space-3` | 12px | button vertical padding |
| `space-4` | 16px | card inner gap |
| `space-6` | 24px | card padding, stack gap |
| `space-8` | 32px | section inner grouping |
| `space-12` | 48px | large cluster gap |
| `section-mobile` | 100px | mobile vertical section padding |
| `section-desktop` | 250px | desktop vertical section padding |

**주요 alias**:
- `--btn-addon-margin` -> 6px / 8px depending size.
- `.css-8vb2wj` -> `padding: 250px 0`, mobile `100px 0`.
- `.css-1ot8705` -> `padding: 250px 0 165px 0`, mobile `100px 0`.

### Whitespace Philosophy
<!-- SOURCE: manual -->

Toss does not use whitespace as luxury minimalism; it uses it as anxiety reduction. Financial claims need room to become simple, so desktop sections often get 250px of vertical air and one dominant sentence before the next product scene appears.

The system compresses inside components but expands between stories. Buttons, nav links, and labels are app-dense; homepage bands are almost cinematic. That contrast is central: "simple app in the hand, calm financial world around it."

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--radius-s` | 4px | tiny controls, table buttons |
| `--radius-m` | 8px | standard button, input, medium control |
| `--radius-l` | 16px | card, thumbnail, container |
| `--radius-xl` | 20px | large card / marketing surface |
| `--radius-xxl` | 24px | hero card / oversized container |
| component height 32 | 8px | tokenized component radius |
| component height 40 | 10px | tokenized component radius |
| component height 48 | 12px | tokenized component radius |
| component height 56 | 14px | tokenized component radius |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| `--shadow-s` | `0 0 4px 0 rgba(2,32,71,.05), 0 4px 16px 0 rgba(2,32,71,.05)` | subtle card/default elevation |
| `--shadow-m` | `0 8px 16px 0 rgba(0,27,55,.1), 0 4px 8px 0 rgba(2,32,71,.05)` | active card / pressed elevation |
| `--shadow-l` | `0 24px 40px 0 rgba(0,23,51,.02), 0 16px 24px 0 rgba(0,27,55,.1), 0 0 8px 0 rgba(2,32,71,.05)` | hover card / modal feel |
| focus outline | `inset 0 0 0 2px #3182F6` | focus/selected state |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| basic transition | `.2s ease` | breadcrumb, cards, thumbnails |
| page fade | `.3s ease-in-out` | opacity transition |
| card hover | shadow-s -> shadow-l | `.p-cardV2--shadow-outline:hover` |
| thumbnail hover | `transform: scale(1.1)` | image reveal inside card |
| press state | shadow-l -> shadow-m | active card response |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `.p-container--default` with fixed inner container; observed special section max-width 800px.
- **Grid type**: Flexbox and positioned marketing scenes; Emotion classes handle per-section composition.
- **Column count**: mostly single-column narrative sections with occasional two-column/flex product layouts.
- **Gutter**: 24-48px inside product clusters; very large vertical gutters between homepage stories.

### Hero
- **Pattern Summary**: `100vh + full-bleed pale-blue 3D image + centered Korean H1 + App Store / Google Play CTA`.
- Layout: one-column centered overlay on full-viewport image.
- Background: image `new_main.png`, object-fit cover, pale blue financial miniature scene.
- **Background Treatment**: image-overlay by composition, not CSS gradient; light blue 3D scene supplies depth and shadow.
- H1: `60-72px` visual range / weight `700-800` / tracking `0`.
- Max-width: centered text stack over viewport, not a boxed hero card.

### Section Rhythm
```css
section .p-container {
  padding: 250px 0;
}
@media (max-width: 639px) {
  section .p-container {
    padding: 100px 0;
  }
}
```

### Card Patterns
- **Card background**: #FFFFFF or #F9FAFB on muted bands.
- **Card border**: often none; when needed, soft #E5E8EB / rgba(0,27,55,.1).
- **Card radius**: 16px, 20px, 24px depending scale.
- **Card padding**: 24-48px for marketing cards; tighter in product-system tables.
- **Card shadow**: low-opacity greyOpacity layers, strongest on hover.

### Navigation Structure
- **Type**: horizontal desktop nav with logo left, links center/right, language switch.
- **Position**: top static/sticky-style marketing nav in screenshot.
- **Height**: compact app-bar density, visually about 64px.
- **Background**: #FFFFFF.
- **Border**: visually none or extremely soft; separation comes from whitespace.

### Content Width
- **Prose max-width**: about 800px on bottom CTA section.
- **Container max-width**: `.p-container--default`, with inner wrapper.
- **Sidebar width**: N/A on homepage.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Small mobile | 360px / 384px | special narrow-screen adjustments present |
| Mobile | max-width 639px / 640px | section padding compresses to 100px, type scales down |
| Tablet | min-width 640px / 768px | progressive layout widening |
| Desktop | min-width 1024px | desktop nav and section rhythm |
| Large | min-width 1280px | large marketing composition |

### Touch Targets
- **Minimum tap size**: product buttons are size-tokenized; large buttons use 17px font and 26-27px line-height plus padding.
- **Button height (mobile)**: inferred 44px+ for large app CTAs.
- **Input height (mobile)**: component token family includes height-based radius from 16 to 56px; homepage input not surfaced.

### Collapsing Strategy
- **Navigation**: desktop links collapse into mobile right-side menu/hamburger area.
- **Grid columns**: product scenes collapse from positioned/flex compositions into vertical story blocks.
- **Sidebar**: none.
- **Hero layout**: maintains full-bleed image but text and CTA stack scale down.

### Image Behavior
- **Strategy**: `object-fit: cover` for hero image.
- **Max-width**: responsive width 100% patterns present.
- **Aspect ratio handling**: hero fills 100vh; marketing images are positioned rather than framed in fixed cards.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<a class="p-button p-button--primary p-button--large" href="#">
  App Store
</a>
```

| Spec | Value |
|---|---|
| Base font | 15px default, 17px large/xlarge |
| Radius | 7px default, 8px large/xlarge via `--radius-m` |
| Primary bg | #3182F6 |
| Primary hover | #1B64DA / tokenized hover skin |
| Danger bg | #F04452 |
| Weak primary bg | #E8F3FF |
| Focus | inset 0 0 0 2px #3182F6 |

States observed or tokenized: hover, focus-visible, active, disabled, danger, weak.

### Badges

Badges inherit the same color discipline as buttons: small radius, 13px-ish type, semantic color families only. Do not introduce decorative rainbow badges; use blue weak, grey weak, or red weak states.

| Spec | Value |
|---|---|
| Font | Toss Product Sans, 12-13px |
| Radius | 999px or 6-8px depending component |
| Blue weak | #E8F3FF background with #1B64DA text |
| Grey weak | #F2F4F6 background with #4E5968 text |

### Cards & Containers

```html
<article class="p-cardV2 p-cardV2--shadow-outline">
  <div class="p-cardV2__thumbnail"></div>
  <h3 class="p-cardV2__title">금융을 쉽게</h3>
</article>
```

| Spec | Value |
|---|---|
| Background | #FFFFFF |
| Radius | 16px / 20px |
| Border | none or 1px rgba(0,27,55,.1) |
| Shadow default | `--shadow-s` |
| Shadow hover | `--shadow-l` |
| Shadow active | `--shadow-m` |
| Thumbnail hover | scale(1.1) inside clipped surface |

### Navigation

```html
<nav class="p-navbar">
  <a class="p-navbar__logo-icon" aria-label="toss"></a>
  <a class="p-navbar__link">회사 소개</a>
  <a class="p-navbar__link">고객센터</a>
</nav>
```

| Spec | Value |
|---|---|
| Background | #FFFFFF |
| Link color | #4E5968 / #6B7684 |
| Active color | #191F28 or #3182F6 for anchor states |
| Structure | logo left, product/company links, language switch |
| Mobile | right-side compact controls |

### Inputs & Forms

Homepage forms are not the main surface, but the component system exposes input-style states.

| Spec | Value |
|---|---|
| Border | rgba(0,27,55,.1) / #E5E8EB |
| Focus | 2px blue inset outline |
| Radius | 8-12px by height |
| Placeholder | #8B95A1 |
| Error | #F04452 / #D22030 |

### Hero Section

```html
<section class="toss-hero">
  <img src="new_main.png" alt="" class="toss-hero__image" />
  <div class="toss-hero__content">
    <h1>금융의 모든 것<br />토스에서 쉽고 간편하게</h1>
    <div class="toss-hero__stores">...</div>
  </div>
</section>
```

| Spec | Value |
|---|---|
| Height | 100vh |
| Image | object-fit cover, width/height 100% |
| Text | centered, #000 visual in screenshot but system text token should map to #191F28 |
| CTA | dark app-store buttons, compact radius |
| Scroll cue | small down chevron at bottom center |

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-primary** — #3182F6 fill, #FFFFFF text, 8px-ish radius, used for direct action. Hover should deepen toward #1B64DA, not brighten.

**button-weak-primary** — #E8F3FF surface, #1B64DA text, used for low-pressure blue action. It preserves the Toss blue identity without turning the whole UI into blue.

**button-danger** — #F04452 fill with red weak variants. It is semantic, not decorative.

**card-shadow-outline** — white card that uses shadow escalation from `--shadow-s` to `--shadow-l`; structural border stays soft or absent.

**navbar-link-active** — #3182F6 active indicator/title for anchor-style nav; normal nav stays grey.

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

#### blue-inset-focus-ring

```yaml
blue-inset-focus-ring:
  description: "Selected/focus state feels native to Toss UI through an inset blue ring instead of an outer glow."
  technique: "box-shadow: inset 0 0 0 2px #3182F6 (var(--blue500)); never combined with outline."
  applied_to: ["{components.button-primary}", "checkable controls", "table row select", "active interactive states"]
  visual_signature: "the ring sits flush inside the control — accessibility without the SaaS halo."
  intent: "Toss's worldview is calm financial precision; outer glow rings would feel consumer-app fluffy."
```

#### grey-opacity-layered-shadow

```yaml
grey-opacity-layered-shadow:
  description: "Soft elevation built from transparent blue-grey shadows, never warm or pure black."
  technique: "rgba(2,32,71,.05) + rgba(0,27,55,.1) multi-layer stacks across .shadow--s / .shadow--m / .shadow--l."
  applied_to: [".shadow--s", ".shadow--m", ".shadow--l", ".p-cardV2--shadow-outline"]
  visual_signature: "surfaces float gently and stay financial-cool — never luxury-drop-shadow heavy."
  intent: "Korean fintech needs a calm sense of trust; warm shadow tones would suggest consumer e-commerce instead of money handling."
```

#### mobile-app-section-breathing

```yaml
mobile-app-section-breathing:
  description: "Extreme homepage vertical air around app-like product scenes — each feature is a self-contained story."
  technique: "desktop padding 250px 0, mobile padding 100px 0 on major homepage sections."
  applied_to: ["{component.feature-section}", "homepage product showcase"]
  visual_signature: "each scroll feels like opening a new app screen, not scrolling a feature grid."
  intent: "Toss is fundamentally a mobile-app brand; the marketing site reproduces that one-screen-per-thought rhythm."
```

#### toss-product-sans-neutral-korean

```yaml
toss-product-sans-neutral-korean:
  description: "Korean display type stays large and plain — no editorial flourish, no startup hype."
  technique: "Toss Product Sans at weight 700/800, line-height 1.15-1.4, letter-spacing 0; H1 ~48-64px desktop."
  applied_to: ["{typography.h1}", "hero headline", "section headline"]
  visual_signature: "friendly clarity — neither bank-formal nor startup-loud, just plainly readable Korean."
  intent: "Korean financial users distrust ornate type; calm weight 700 with zero tracking is the most-trusted register."
```

#### card-radius-as-product-promise

```yaml
card-radius-as-product-promise:
  description: "Toss commits to a generous 20-24px card radius across every product surface — radius IS the brand."
  technique: "card border-radius 20px (mobile) / 24px (desktop); never reduced for compactness, never increased for cuteness."
  applied_to: ["{component.product-card}", "{component.feature-tile}", "homepage app preview"]
  visual_signature: "every card looks like a phone-app tile — soft, touchable, and consistent across every scroll position."
  intent: "Toss brand recognition lives in the corner radius; codifying it prevents marketing pages from drifting toward web-card aesthetics."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | plain Korean benefit, short line breaks | "금융의 모든 것 / 토스에서 쉽고 간편하게" |
| Primary CTA | app acquisition / direct action | "App Store", "Google Play" |
| Secondary CTA | low-pressure info link | company/customer/support nav |
| Subheading | simple declarative service promise | short, low-jargon |
| Tone | confident, warm, non-institutional | financial but consumer-friendly |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Toss - copy into your root stylesheet */
:root {
  /* Fonts */
  --toss-font-family: "Toss Product Sans", "Apple SD Gothic Neo",
    "Noto Sans KR", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --toss-font-family-code: SFMono-Regular, Menlo, Consolas, Monaco,
    "Andale Mono", "Ubuntu Mono", monospace;
  --toss-font-weight-normal: 400;
  --toss-font-weight-bold: 700;

  /* Brand */
  --toss-color-brand-50: #E8F3FF;
  --toss-color-brand-200: #90C2FF;
  --toss-color-brand-500: #3182F6;
  --toss-color-brand-600: #2272EB;
  --toss-color-brand-700: #1B64DA;

  /* Surfaces */
  --toss-bg-page: #FFFFFF;
  --toss-bg-muted: #F2F4F6;
  --toss-text: #191F28;
  --toss-text-secondary: #4E5968;
  --toss-text-muted: #6B7684;
  --toss-border: #E5E8EB;
  --toss-error: #F04452;

  /* Spacing */
  --toss-space-sm: 8px;
  --toss-space-md: 16px;
  --toss-space-lg: 24px;
  --toss-section-mobile: 100px;
  --toss-section-desktop: 250px;

  /* Radius */
  --toss-radius-sm: 4px;
  --toss-radius-md: 8px;
  --toss-radius-lg: 16px;
  --toss-radius-xl: 20px;

  /* Shadow */
  --toss-shadow-s: 0 0 4px 0 rgba(2,32,71,.05),
    0 4px 16px 0 rgba(2,32,71,.05);
  --toss-shadow-l: 0 24px 40px 0 rgba(0,23,51,.02),
    0 16px 24px 0 rgba(0,27,55,.1),
    0 0 8px 0 rgba(2,32,71,.05);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js - Toss inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        toss: {
          blue50: "#E8F3FF",
          blue200: "#90C2FF",
          blue500: "#3182F6",
          blue600: "#2272EB",
          blue700: "#1B64DA",
        },
        tossGrey: {
          50: "#F9FAFB",
          100: "#F2F4F6",
          200: "#E5E8EB",
          600: "#6B7684",
          700: "#4E5968",
          900: "#191F28",
        },
      },
      fontFamily: {
        sans: ["Toss Product Sans", "Apple SD Gothic Neo", "Noto Sans KR", "system-ui"],
      },
      borderRadius: {
        toss: "8px",
        "toss-card": "20px",
      },
      boxShadow: {
        toss: "0 0 4px 0 rgba(2,32,71,.05), 0 4px 16px 0 rgba(2,32,71,.05)",
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
| Brand primary | `{colors.primary}` | `#3182F6` |
| Background | `{colors.surface}` | `#FFFFFF` |
| Muted background | `{colors.surface-muted}` | `#F2F4F6` |
| Text primary | `{colors.text-primary}` | `#191F28` |
| Text muted | `{colors.text-muted}` | `#6B7684` |
| Border | `{colors.border}` | `#E5E8EB` |
| Error | `{colors.error}` | `#F04452` |

### Example Component Prompts

#### Hero Section
```text
Toss 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF 위에 pale-blue 3D 금융 오브젝트 이미지를 full-bleed로 배치
- 높이: 100vh
- H1: Toss Product Sans, 60-72px, weight 700/800, line-height 1.15-1.3, letter-spacing 0
- 텍스트 색상: #191F28
- CTA: App Store / Google Play dark compact buttons, 가운데 정렬
- 섹션 아래에는 작은 down chevron만 둔다
```

#### Card Component
```text
Toss 스타일 카드 컴포넌트를 만들어줘.
- 배경 #FFFFFF, radius 20px, border 없음 또는 1px solid #E5E8EB
- shadow: 0 0 4px rgba(2,32,71,.05), 0 4px 16px rgba(2,32,71,.05)
- hover: shadow를 더 큰 grey-opacity layer로만 강화, 색상은 바꾸지 않음
- 제목: Toss Product Sans 20-24px weight 700 color #191F28
- 본문: 15px line-height 1.6 color #6B7684
```

#### Badge
```text
Toss 스타일 배지를 만들어줘.
- font: Toss Product Sans 13px weight 500
- primary weak: bg #E8F3FF, color #1B64DA
- neutral: bg #F2F4F6, color #4E5968
- radius: 999px 또는 8px, 장식용 그라디언트 금지
```

#### Navigation
```text
Toss 스타일 상단 네비게이션을 만들어줘.
- 배경 #FFFFFF, 하단 border는 없거나 #E5E8EB 1px
- 로고 좌측, 링크는 #4E5968 / #6B7684
- active link 또는 anchor indicator만 #3182F6
- 언어 스위치는 우측에 작게 배치
- 모바일에서는 링크를 숨기고 오른쪽 compact menu로 접는다
```

### Iteration Guide

- **색상 변경 시**: #3182F6 하나를 primary로 유지하고, 보조 색은 grey ramp에서 해결한다.
- **폰트 변경 시**: Pretendard 대체는 가능하지만 letter-spacing은 0을 유지한다.
- **여백 조정 시**: 컴포넌트 안은 4/8/16/24px, 섹션은 100/250px 계열로 움직인다.
- **새 컴포넌트 추가 시**: 8px control radius와 16-20px card radius를 분리한다.
- **다크 모드**: darkThemeBlue/darkThemeGrey 토큰을 사용하고 light token opacity hack을 피한다.
- **반응형**: 639/640px 모바일 기준과 1024px desktop 기준을 우선 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #3182F6 as the single primary action color.
- Use #191F28 for primary text and #6B7684 / #4E5968 for secondary copy.
- Keep homepage sections very airy: 250px desktop, 100px mobile is a real Toss rhythm.
- Use Toss Product Sans or a Korean UI substitute with line-height 1.6.
- Use grey-opacity multi-layer shadows instead of hard black shadows.
- Let white and pale grey surfaces carry most of the page.
- Keep CTA surfaces simple, tactile, and app-like.
- Preserve the difference between component radius (8px) and card radius (16-20px).

### ❌ DON'T

- 배경을 `#F8FAFF` 같은 임의 pale blue로 전부 칠하지 말 것 — 대신 기본 바닥은 `#FFFFFF` 사용.
- 본문/헤드라인을 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#191F28` 사용.
- muted text를 `#999999`로 두지 말 것 — 대신 `#6B7684` 또는 `#4E5968` 사용.
- border를 `#DDDDDD`로 두껍게 만들지 말 것 — 대신 `#E5E8EB` 또는 rgba(0,27,55,.1) 사용.
- primary CTA를 `#0066FF` 또는 `#007AFF`로 대체하지 말 것 — 대신 `#3182F6` 사용.
- hover blue를 `#0051CC`처럼 과하게 어둡게 만들지 말 것 — 대신 `#1B64DA` 사용.
- error를 `#FF0000`으로 두지 말 것 — 대신 `#F04452` 사용.
- card shadow를 `rgba(0,0,0,.25)` 단층 그림자로 만들지 말 것 — 대신 rgba(2,32,71,.05) 계열 multi-layer 사용.
- button radius를 999px pill로 통일하지 말 것 — Toss 기본 control은 7-8px, card는 16-20px.
- hero를 gradient mesh로 대체하지 말 것 — Toss hero는 full-bleed pale-blue 3D image scene이다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- Second brand color: none. Blue carries action; grey carries hierarchy; red is only semantic error/destructive.
- Decorative gradient tokens: absent. The hero's depth comes from image craft, not CSS gradient wallpaper.
- Raw black typography: never as the system default. #191F28 is the trusted near-black.
- Serif contrast: none. Toss avoids editorial/luxury typography.
- Heavy borders: absent on marketing cards. Space and soft shadow do the structural work.
- Aggressive neumorphism: none. Shadows are low-opacity blue-grey layers, not embossed surfaces.
- Pill-everything UI: absent. Radius is tokenized by component height.
- Dense enterprise tables on the homepage: none. The homepage sells simplicity, not operational density.
- Rainbow fintech palette: none. Additional color families exist in the system, but the homepage identity is blue/grey.
- Long explanatory microcopy blocks: rare. Copy is short, direct, and app-store friendly.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage snapshot** — this guide reuses the existing `toss` phase1 homepage artifacts. Logged-in app, product detail flows, forms, and support flows were not visited.
- **Screenshot is desktop hero only** — mobile visual verification was inferred from CSS breakpoints, not newly captured.
- **Exact font licensing and file metrics** — Toss Product Sans is identified from CSS frequency, but font file metrics were not measured directly.
- **Emotion class volatility** — `.css-*` classes are runtime-generated and should not be treated as stable implementation API.
- **Dark mode is token-present, not homepage-proven** — darkTheme tokens exist, but the homepage default visual is light.
- **Accent families beyond blue/red** — green, teal, yellow, orange, and purple families appear in CSS, but homepage usage was not deeply mapped.
- **Motion JS not fully traced** — CSS transitions and hover states were inspected; IntersectionObserver or scroll-triggered JavaScript timing was not decomposed.
- **Form validation states not surfaced** — input/error specs come from token/component CSS, not a live form journey.
- **Hero imagery asset dependency** — the signature pale-blue 3D scene is an image asset; recreating Toss without equivalent imagery will miss much of the brand feel.
