---
schema_version: 3.2
slug: google
service_name: Google
site_url: https://google.com
fetched_at: 2026-05-03T06:33:41Z
default_theme: light
brand_color: "#1A73E8"
primary_font: "Google Sans"
font_weight_normal: 400
token_prefix: glue

bold_direction: Search Minimalism
aesthetic_category: refined-minimalism
signature_element: minimal_extreme
code_complexity: medium

medium: web
medium_confidence: high
archetype: landing-utility
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "Glue/Material-derived CSS tokens are extensive and production-used, but this capture is not a full public design-system specification."

colors:
  primary: "#1A73E8"
  surface-base: "#FFFFFF"
  text-primary: "#202124"
  text-muted: "#5F6368"
  border-hairline: "#DADCE0"
  surface-soft: "#F8F9FA"
  logo-blue: "#4285F4"
  logo-red: "#EA4335"
  logo-yellow: "#FBBC04"
  logo-green: "#34A853"

typography:
  display: "Product Sans, Google Sans, Arial, Helvetica, sans-serif"
  body: "Google Sans Text, Arial, Helvetica, sans-serif"
  ladder:
    - { token: search-logo, size: "92px visual asset", weight: 400, tracking: "logo drawing" }
    - { token: page-link, size: "14px", weight: 400, tracking: "0" }
    - { token: button, size: "14px", weight: 400, tracking: "0" }
    - { token: utility-link, size: "13px", weight: 400, tracking: "0" }
  weights_used: [300, 400, 500, 700]
  weights_absent: [600, 800, 900]

components:
  search-box: { bg: "{colors.surface-base}", radius: "24px", height: "46px", shadow: "0 1px 6px rgba(32,33,36,.28)" }
  button-primary: { bg: "{colors.primary}", radius: "48px", padding: "9px 23px", color: "#FFFFFF" }
  button-neutral: { bg: "{colors.surface-soft}", radius: "4px", padding: "0 16px", color: "{colors.text-primary}" }
  app-grid-icon: { size: "40px target / 24px glyph", radius: "50%", hover: "#F1F3F4" }
---

# DESIGN.md - Google

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Google's homepage is less a page than a calibrated pause. The main screen is mostly air: white surface, one multicolor wordmark, one rounded input, two quiet buttons, and a few utility links pushed to the edges. It feels like a freshly cleared desk before the first sentence is written: the paper is #FFFFFF (`{colors.surface-base}`), the pencil line is #DADCE0 (`{colors.border-hairline}`), and the search rail is the only object allowed to cast a shadow.

The color system is not "Google colors everywhere." The logo is a sealed stamp: red, yellow, green, and bright blue stay inside the identity mark like ink on a letterhead. Product UI chrome is mostly #FFFFFF (`{colors.surface-base}`), #202124 (`{colors.text-primary}`), #5F6368 (`{colors.text-muted}`), and #DADCE0 (`{colors.border-hairline}`). The operational brand color is #1A73E8 (`{colors.primary}`), used for high-emphasis buttons and focus rings, while the famous logo blue #4285F4 appears as identity material rather than the default interaction color. No second brand color leaks into the controls.

Typography is intentionally plain. Google Sans gives buttons and links a friendly geometric voice, but the page never turns typography into spectacle. The biggest "type" on the screen is the logo drawing itself; everything else behaves like small labels on a map. There is no newspaper headline, no poster title, no product manifesto. Links and buttons sit at 13-14px, weight 400, with no editorial display hierarchy.

The signature is the search chassis: a pill with a very soft gray border, subtle shadow, and icon controls inside the same horizontal rail. It is not a card; it is closer to a shallow slot cut into a white counter. On hover, the `0 1px 6px rgba(32,33,36,.28)` shadow does just enough to say "this is an instrument," then disappears back into the room. Shadow belongs to the search rail only, not to nav, footer, or decorative chrome.

The system's restraint is also its identity. There is no hero headline, no CTA stack, no marketing paragraph, no feature grid, and no decorative illustration. Site-as-website almost vanishes; the frame evacuates itself so the input can become the product. Google does not ask you to read the page. It hands you an empty field and waits.

If the page were a physical object, it would be a librarian's reference card filled in with one pencil stroke: the only furniture is the index slip, and everything else is empty stacks waiting for a query. The four wordmark colors behave like a wax seal on otherwise blank correspondence — identification, not decoration. The doodle slot above the search rail is a single picture frame on a clean lobby wall, swapped daily but never enlarged. Even the "I'm Feeling Lucky" button is dressed like a coat-check ticket: small, paper-quiet, almost forgettable next to the main desk. There is no second brand color in the chrome because the building itself is the silence around the index card.

조금 더 풀면, Google 홈은 **흰 작업대 위에 단 하나 놓인 도구**처럼 작동한다. search rail은 손에 쥐기 좋은 단일 도구 — 도구함 전체를 펼치지 않고 가장 자주 쓰는 한 자루만 책상에 올려둔 풍경이다. 그 양옆 두 버튼은 도구 손잡이 옆에 달린 작은 스위치 두 개, 누르면 즉시 결과로 흘러간다. 우상단 utility links는 작업대 끝에 정리된 보조 도구 라벨, footer는 도구함의 닫힌 뚜껑 — 굳이 열어 보이지 않는 부속 도구판이다. logo 네 컬러는 도구 손잡이에 새겨진 brand 각인일 뿐, 작업대 전체를 칠하는 페인트가 아니다. 두 번째 brand color가 없는 이유: 잘 만들어진 도구 한 자루는 색이 둘일 필요가 없다.

### Key Characteristics

- White-first composition: #FFFFFF dominates and is not tinted warm or cool.
- Search box is the primary object: centered, pill-shaped, shadowed, and wider than every other control.
- Logo colors are identity-only; UI actions use Material/Glue blue #1A73E8.
- Typography stays small and utility-grade: 13-14px, mostly weight 400.
- Footer is a soft gray band (#F2F2F2/#F8F9FA family), visually separate from the search surface.
- Hairline borders use #DADCE0 and #E8EAED rather than heavy black outlines.
- Button radii split by intent: login is a 48px pill, search buttons are 4px rectangles.
- Focus states are explicit blue rings, not hover-only decorative treatments.
- Motion is negligible; interaction changes are color, shadow, or focus-ring deltas.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Search Minimalism
> **Aesthetic Category**: refined-minimalism
> **Signature Element**: 이 사이트는 **minimal_extreme**으로 기억된다.
> **Code Complexity**: medium — broad Glue/Material token coverage plus responsive chrome, but the visible homepage uses a deliberately small component set.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Google처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Google Sans Text", Arial, Helvetica, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #202124; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #1A73E8; }
```

**절대 하지 말아야 할 것 하나**: logo palette를 UI 전체에 흩뿌리지 말 것. Google 홈페이지의 UI는 다색이 아니라 거의 무채색이며, blue CTA/focus만 통제해서 쓴다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://google.com` |
| Fetched | 2026-05-03T06:33:41Z |
| Extractor | reused phase1 artifacts; no fresh crawl |
| HTML size | 104528 bytes |
| CSS files | 2 external CSS files, 573037 chars |
| Token prefix | `glue` |
| Method | existing phase1 JSON + CSS token/frequency inspection + screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: static/SSR marketing and utility HTML; capture includes `about.google` metadata and Google homepage screenshot.
- **Design system**: Google Glue + Material-derived token layer - prefix `glue`, plus `--md-*` Material text-field/select variables.
- **CSS architecture**:
  ```text
  core       (--glue-grey-*, --glue-blue-*, --g-logo-*) raw hex values
  component  (--md-outlined-text-field-*, --marquee-*) component-scoped values
  utility    class selectors such as .glue-button, .glue-header, .glue-footer
  ```
- **Class naming**: Glue BEM-like selectors (`.glue-button--high-emphasis`, `.glue-header__bar`, `.glue-footer__link`).
- **Default theme**: light (bg = `#FFFFFF`).
- **Font loading**: CSS declarations reference Google Sans, Google Sans Text, Product Sans, localized Google Sans families, Noto fallbacks, Arial/Helvetica.
- **Canonical anchor**: homepage screenshot centers search; HTML capture has About Google content, so component guidance favors shared Google/Glue primitives rather than article-specific modules.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Product Sans, Google Sans, Arial, Helvetica, sans-serif` (proprietary Google brand/display face)
- **Body font**: `Google Sans Text, Arial, Helvetica, sans-serif`
- **Code font**: `Roboto Mono, monospace`
- **Weight normal / bold**: `400` / `500` for visible UI; CSS also contains `300` and `700` in broader Glue modules.

```css
:root {
  --glue-font-family:       "Google Sans Text", Arial, Helvetica, sans-serif;
  --glue-font-family-display: "Google Sans", Arial, Helvetica, sans-serif;
  --glue-font-family-code:  "Roboto Mono", monospace;
  --glue-font-weight-normal: 400;
  --glue-font-weight-medium: 500;
}
body {
  font-family: var(--glue-font-family);
  font-weight: var(--glue-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Google Sans / Product Sans** - proprietary; do not assume it is available outside Google-controlled surfaces.
- **Open-source substitute**: `Inter` or `Roboto` at weight 400 for UI, with `font-size: 14px`, `line-height: 20px`, and `letter-spacing: 0`.
- **Display substitute**: use `Inter` 400 for headline-like utility copy; avoid weight 700 unless recreating About Google editorial cards, not the search homepage.
- **Correction**: if `Inter` looks too dense, increase line-height by 1-2px rather than adding letter-spacing. Google's visible homepage copy has no decorative tracking.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Logo mark | asset, approx 272px wide on desktop capture | drawn | N/A | N/A |
| Top nav link | 14px | 400 | 24px target area | 0 |
| Search input text | 16px implied | 400 | 34-46px control rhythm | 0 |
| Neutral search button | 14px | 400 | 36px control | 0 |
| Login pill | 14px | 500 | 36-40px control | 0 |
| Footer link | 14px | 400 | 40px row rhythm | 0 |
| About-page headings | 48-60px range in Glue CSS modules | 400/500/700 depending module | tight display | 0 to slight negative not confirmed |

> ⚠️ Key insight: the homepage does not use typographic hierarchy to sell the product. The logo and search input are the hierarchy; text is utility chrome.

### Principles

1. Keep visible homepage typography at 13-16px; large display text belongs to Google marketing pages, not the search start page.
2. Use weight 400 as the default. Weight 500 is for high-emphasis account/action controls; weight 700 is not part of the homepage feel.
3. Do not add negative tracking to body, buttons, or nav. The system relies on neutral readability.
4. Treat the logo as artwork, not text. Recreating it with live text will immediately lose the optical character.
5. Localized fallbacks matter: Google Sans Korean / Noto Sans KR appear in the font stack for non-Latin contexts.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (9 steps)
<!-- glue-color-core-blue-* / --glue-blue-* -->

| Token | Hex |
|---|---|
| `--glue-blue-50` | `#E8F0FE` |
| `--glue-blue-100` | `#D2E3FC` |
| `--glue-blue-200` | `#AECBFA` |
| `--glue-blue-300` | `#8AB4F8` |
| `--glue-blue-400` | `#669DF6` |
| `--glue-blue-500` | `#4285F4` |
| `--glue-blue-600` | `#1A73E8` |
| `--glue-blue-700` | `#1967D2` |
| `--glue-blue-800` | `#185ABC` |
| `--glue-blue-900` | `#174EA6` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--glue-blue-800` | `#185ABC` |
| `--glue-blue-900` | `#174EA6` |
| `--md-ref-palette-primary80` | `#8AB4F8` |
| `--md-ref-palette-primary90` | `#AECBFA` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light (`glue-grey`) | Dark / text |
|---|---|---|
| 0 | `#FFFFFF` | `#000000` |
| 25 | `#F1F1F1` | N/A |
| 50 | `#F8F9FA` | N/A |
| 100 | `#F1F3F4` | N/A |
| 200 | `#E8EAED` | N/A |
| 300 | `#DADCE0` | hairline |
| 400 | `#BDC1C6` | disabled stroke |
| 500 | `#9AA0A6` | muted icon |
| 600 | `#80868B` | secondary |
| 700 | `#5F6368` | muted text |
| 800 | `#3C4043` | strong body |
| 900 | `#202124` | primary text |

### 06-4. Accent Families
<!-- SOURCE: auto -->

| Family | Key step | Hex |
|---|---|---|
| Google red | `--g-logo-red` / `--glue-red-500` | `#EA4335` |
| Google yellow | `--g-logo-yellow` / `--glue-yellow-500` | `#FBBC04` |
| Google green | `--g-logo-green` / `--glue-green-500` | `#34A853` |
| Google blue logo | `--g-logo-blue` / `--glue-blue-500` | `#4285F4` |

### 06-5. Semantic
<!-- SOURCE: auto+manual -->

| Token | Hex | Usage |
|---|---|---|
| `{colors.primary}` | `#1A73E8` | login button, high-emphasis Glue button, focus ring |
| `{colors.surface-base}` | `#FFFFFF` | body background, search box, primary chrome |
| `{colors.text-primary}` | `#202124` | main links and copy |
| `{colors.text-muted}` | `#5F6368` | footer/meta text, secondary copy |
| `{colors.border-hairline}` | `#DADCE0` | search box border, footer separators, outlined controls |
| `{colors.surface-soft}` | `#F8F9FA` | neutral search buttons, subtle section surface |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--glue-blue-600` | `#1A73E8` | high-emphasis button bg |
| `--glue-blue-800` | `#185ABC` | pressed/focus darker blue |
| `--glue-grey-0` | `#FFFFFF` | base surface |
| `--glue-grey-300` | `#DADCE0` | dividers and hairlines |
| `--glue-grey-700` | `#5F6368` | secondary text/icon |
| `--glue-grey-900` | `#202124` | primary text |
| `--md-filled-select-text-field-input-text-color` | `#3C4043` | Material input text |
| `--md-outlined-select-text-field-input-text-color` | `#3C4043` | Material outlined input text |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---|---|
| white/surface | `#FFFFFF` | 153 |
| primary text | `#202124` | 125 |
| hairline | `#DADCE0` | 71 |
| muted text | `#5F6368` | 60 |
| soft surface | `#F8F9FA` | 57 |
| action blue | `#1A73E8` | 56 |
| dark action blue | `#174EA6` | 38 |
| black | `#000000` | 30 |
| light gray | `#F1F3F4` | 27 |
| gray 800 / 500 | `#3C4043` / `#9AA0A6` | 19 each |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.surface-base}` (`#FFFFFF`)** - The main design material. Google search starts from an almost unmarked surface so the input reads as the first real object. Do not tint this surface unless recreating a footer or secondary band.

**`{colors.text-primary}` (`#202124`)** - Google's near-black. It keeps links and utility copy readable without the harshness of `#000000`. Use it for primary text and avoid pure black for interface copy.

**`{colors.primary}` (`#1A73E8`)** - The operational brand blue. It is the login/high-emphasis/focus color, not the logo's brighter blue. This distinction is one of the easiest ways to avoid a fake Google clone.

**`{colors.border-hairline}` (`#DADCE0`)** - The structural line. It defines the search pill, footer separators, and outlined states without becoming visual content.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `page-edge-sm` | 16px | mobile/compact page edge |
| `nav-inline` | 15-24px | top utility link spacing |
| `control-gap` | 8-12px | icons inside search rail |
| `button-inline` | 16px | neutral search button padding |
| `search-width-desktop` | 584px approx | centered search input max width |
| `hero-top-air` | 180-220px approx in screenshot | air above logo/search group |
| `footer-row` | 46-52px | country row and link row height |
| `grid-gap-lg` | 24px | Glue cards/marketing modules |

**주요 alias**:
- `--glue-page-margin` -> 24px style page gutters in Glue modules.
- `--slides-gap` -> carousel/media modules, not homepage search.

### Whitespace Philosophy
<!-- SOURCE: manual -->

Google's homepage uses whitespace as a product promise: the page starts empty so the user can ask anything. The logo-search cluster occupies the vertical center, while nav and footer are pushed to the edges as thin utility rails.

This is not a standard 4-8-16 rhythm page. The important spacing is relational: huge vertical air around the search task, compact 8-16px spacing inside controls, and a footer band that anchors geography/legal links without entering the main task area.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `search-pill` | 24px | search input rail, 46px height |
| `login-pill` | 48px | top-right login button |
| `icon-circle` | 50% / 100% | app grid hover, icon targets |
| `button-neutral` | 4px | "Google Search" / "I'm Feeling Lucky" |
| `glue-card-sm` | 8px | utility/cards in Glue modules |
| `glue-card-md` | 12px | 3-up card modules |
| `media-card` | 16px/24px/28px | broader marketing components |
| `capsule` | 999px | pill groups and segmented edges |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| Search hover/focus | `0 1px 6px rgba(32,33,36,.28)` inferred from homepage pattern | search pill lift |
| Glue elevation 1 | `0 1px 2px 0 rgba(60,64,67,.3), 0 1px 3px 1px rgba(60,64,67,.15)` | low elevation cards/buttons |
| Glue elevation 2 | `0 1px 2px 0 rgba(60,64,67,.3), 0 2px 6px 2px rgba(60,64,67,.15)` | raised cards |
| Glue elevation 3 | `0 1px 3px 0 rgba(60,64,67,.3), 0 4px 8px 3px rgba(60,64,67,.15)` | higher panels |
| Focus ring | `0 0 0 2px #1A73E8` / `#185ABC` | accessible focus |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `--animation-duration-transition` | `300ms` | carousel/media modules in Glue CSS |
| focus/hover color | short CSS transition, exact timing not isolated | buttons and links |
| search box lift | hover/focus shadow change | homepage search affordance |
| reduced motion | `prefers-reduced-motion` media query present | accessibility branch |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: homepage search rail approx 584px; broader About/Glue modules include 1024px carousel widths and responsive containers.
- **Grid type**: homepage is simple flex/absolute distribution; Glue marketing modules use flex/grid/card modules.
- **Column count**: homepage main task is 1-column centered; footer links are horizontal groups on desktop.
- **Gutter**: 24px desktop page edge, 16px compact edge, 8-16px control internals.

### Hero

- **Pattern Summary**: 100vh utility canvas + solid white background + centered logo/search object + edge-mounted nav/footer.
- Layout: one-column centered search cluster.
- Background: `#FFFFFF`.
- **Background Treatment**: solid white only; no gradient, no image, no texture.
- H1: logo asset, not live type; surrounding copy 13-14px / weight 400 / tracking 0.
- Max-width: search rail approx 584px; buttons centered below.

### Section Rhythm

```css
main.search-home {
  min-height: calc(100vh - footer-height);
  display: flex;
  flex-direction: column;
  align-items: center;
}
.search-shell {
  max-width: 584px;
  margin-inline: auto;
}
```

### Card Patterns

- **Card background**: homepage has no content cards; search rail behaves as a control surface.
- **Card border**: `1px solid #DADCE0` for outlined controls.
- **Card radius**: 24px for search rail, 4px for neutral search buttons.
- **Card padding**: search rail 8-14px internal rhythm; neutral buttons 0 16px.
- **Card shadow**: subtle search rail elevation only; no editorial card shadow on homepage.

### Navigation Structure

- **Type**: horizontal utility nav with left informational links and right product/account links.
- **Position**: top static/edge-mounted; visually independent from search cluster.
- **Height**: approx 48-60px.
- **Background**: transparent white over body `#FFFFFF`.
- **Border**: none in top nav; footer uses gray separators.

### Content Width

- **Prose max-width**: N/A for homepage; About HTML modules use wider editorial containers.
- **Container max-width**: 584px for search input; 1024px+ in Glue modules.
- **Sidebar width**: none.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `max-width: 599px` | compact nav/footer, reduced horizontal margins |
| Tablet | `min-width: 600px` | Glue tablet layout begins |
| Desktop | `min-width: 1024px` | full header/footer and marketing modules |
| Large | `min-width: 1440px` / `1600px` / `1920px` | large-screen media/carousel tuning in Glue CSS |

### Touch Targets

- **Minimum tap size**: 40-48px visual targets; login pill and app-grid icon meet common mobile target expectations.
- **Button height (mobile)**: 36-40px for visible action buttons.
- **Input height (mobile)**: search rail around 44-46px.

### Collapsing Strategy

- **Navigation**: homepage keeps only essential utility links; broader Glue header has drawer behavior.
- **Grid columns**: homepage remains 1-column; marketing card grids collapse from multi-column to stacked.
- **Sidebar**: none.
- **Hero layout**: logo/search stay centered; width becomes fluid with side gutters.

### Image Behavior

- **Strategy**: homepage logo is an asset/SVG-like identity mark; About pages use responsive `<picture>`/`source`.
- **Max-width**: search rail and logo scale within viewport; images use responsive sources.
- **Aspect ratio handling**: not relevant to homepage content; About capture includes cropped social image metadata.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**High-emphasis pill**

```html
<a class="google-login-pill" href="/login">로그인</a>
```

| Property | Value |
|---|---|
| background | `#1A73E8` |
| color | `#FFFFFF` |
| border-radius | `48px` |
| padding | `9px 23px` |
| font | Google Sans, 14px, weight 500 |
| hover | darker blue family (`#185ABC` / `#174EA6`) |
| focus | `0 0 0 2px #1A73E8` or high-contrast ring |

**Neutral search button**

```html
<button class="google-search-action">Google 검색</button>
```

| Property | Value |
|---|---|
| background | `#F8F9FA` |
| color | `#3C4043` / `#202124` |
| border | `1px solid #F8F9FA`, hover becomes `#DADCE0`-family |
| border-radius | `4px` |
| height | 36px |
| padding | `0 16px` |
| font | 14px, weight 400 |

### Badges

Homepage search has no badge system. In Glue marketing modules, badge-like chips should inherit neutral surfaces (`#F8F9FA`) or blue-tinted surfaces (`#E8F0FE`) with 999px radius only when the content is filter/status-like.

### Cards & Containers

**Search rail**

```html
<form class="google-search-rail">
  <button class="search-plus" type="button"></button>
  <input type="search" />
  <button class="search-icon" type="button"></button>
</form>
```

| Property | Value |
|---|---|
| width | min(584px, calc(100vw - 32px)) |
| height | 46px |
| background | `#FFFFFF` |
| border | `1px solid #DADCE0` |
| radius | 24px |
| shadow | hover/focus `0 1px 6px rgba(32,33,36,.28)` |
| icon color | `#3C4043` / `#5F6368` |
| focus | ring/outline blue, input keeps chrome restrained |

### Navigation

```html
<nav class="google-top-nav">
  <a>Google 정보</a>
  <a>스토어</a>
  <span class="nav-spacer"></span>
  <a>Gmail</a>
  <a>이미지</a>
  <button class="app-grid"></button>
  <a class="login-pill">로그인</a>
</nav>
```

| Property | Value |
|---|---|
| background | transparent over `#FFFFFF` |
| link color | `#202124` |
| link size | 14px |
| spacing | 15px-ish link gaps, 24px edge padding |
| app grid | 40px circular target, 24px glyph |
| hover | underline for text links; soft gray circular hover for icon |

### Inputs & Forms

| Property | Value |
|---|---|
| input background | transparent inside search rail |
| input border | none; rail supplies border |
| input font | 16px, weight 400 |
| input text | `#202124` |
| placeholder/icon | `#5F6368` / `#3C4043` |
| focus | no heavy inner outline; exterior rail/focus ring carries state |
| error | not observed on homepage |

### Hero Section

The hero is a utility form, not a marketing composition. It uses the logo asset, search rail, and two neutral buttons in a centered vertical stack. There is no headline, paragraph, product image, feature proof, or CTA hierarchy beyond the search task.

### 13-2. Named Variants

| Variant | Spec | State Notes |
|---|---|---|
| `search-box` | `#FFFFFF`, 24px radius, 46px height, approx 584px width | hover/focus adds subtle shadow, not colored fill |
| `button-primary-login` | `#1A73E8`, white text, 48px pill | hover darkens, focus ring stays blue |
| `button-neutral-search` | `#F8F9FA`, 4px radius, 36px height | hover gets visible border and slightly darker text |
| `icon-circle-apps` | 40px target, 50% radius | hover `#F1F3F4`, glyph remains dark gray |
| `footer-link` | muted text, gray footer band | underline/link affordance only, no cards |

### 13-3. Signature Micro-Specs

```yaml
search-rail-soft-elevation:
  description: "Search input reads as a touchable instrument without becoming a content card."
  technique: "height 46px; width min(584px, calc(100vw - 32px)); border 1px solid #DADCE0; border-radius 24px; hover/focus box-shadow 0 1px 6px rgba(32,33,36,.28); border-color transparent on lift"
  applied_to: ["{component.search-box}", "{component.search-rail}"]
  visual_signature: "A single shallow pill floats out of the white canvas while the rest of the page stays flat."

logo-palette-quarantine:
  description: "Logo color is identity artwork, not a UI palette."
  technique: "logo uses #4285F4, #EA4335, #FBBC04, #34A853; interactive high-emphasis blue resolves to #1A73E8; neutrals stay #FFFFFF, #202124, #5F6368, #DADCE0"
  applied_to: ["{component.logo-mark}", "{component.button-primary-login}", "{component.search-box}"]
  visual_signature: "The rainbow is locked inside the wordmark; controls remain blue-plus-neutral instead of multicolor."

radius-intent-split:
  description: "Control shape communicates intent before copy does."
  technique: "account CTA border-radius 48px with padding 9px 23px; search rail border-radius 24px at 46px height; neutral search buttons border-radius 4px with height 36px and padding 0 16px"
  applied_to: ["{component.button-primary}", "{component.button-neutral}", "{component.search-box}"]
  visual_signature: "Login is a friendly capsule, search is a soft rail, and secondary actions remain small rectangles."

edge-utility-frame:
  description: "Navigation and footer frame the empty center instead of competing with the search task."
  technique: "top nav transparent over #FFFFFF with 14px links and 15px-ish gaps; app grid 40px circular target with 24px glyph; footer uses soft gray band #F8F9FA/#F2F2F2 family plus #DADCE0 separator"
  applied_to: ["{component.top-nav}", "{component.app-grid-icon}", "{component.footer-link}"]
  visual_signature: "Utility chrome hugs the edges, leaving the center to feel almost unclaimed until the user types."

focus-ring-blue-only-instrument:
  description: "Keyboard focus is treated as a first-class blue instrument cue, not a hover afterthought."
  technique: "focus state resolves to a clean #1A73E8 ({colors.primary}) outline/ring at 2px; no extra glow, drop-shadow, or color blending; rest of the chrome stays in greyscale (#202124, #5F6368, #DADCE0) so the blue ring is the only chromatic event when tabbing"
  applied_to: ["{component.button-primary-login}", "{component.search-box}", "{component.button-neutral}"]
  visual_signature: "Tabbing through the page lights up exactly one blue ring at a time — search, login, or app — like a single backlit key on an otherwise unlit board."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Primary task | noun/verb minimalism; the input is the copy | "Google 검색" |
| Primary account CTA | short action label | "로그인" |
| Secondary action | playful but old-product-specific microcopy | "I'm Feeling Lucky" |
| Utility link | product nouns, no sentence casing burden | "Gmail", "이미지" |
| Footer | institutional/legal labels | "개인정보처리방침", "약관", "설정" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Google homepage-inspired primitives */
:root {
  /* Fonts */
  --glue-font-family: "Google Sans Text", Arial, Helvetica, sans-serif;
  --glue-font-family-display: "Google Sans", Arial, Helvetica, sans-serif;
  --glue-font-family-code: "Roboto Mono", monospace;
  --glue-font-weight-normal: 400;
  --glue-font-weight-bold: 500;

  /* Brand */
  --glue-color-brand-50: #E8F0FE;
  --glue-color-brand-300: #8AB4F8;
  --glue-color-brand-500: #4285F4;
  --glue-color-brand-600: #1A73E8; /* canonical UI blue */
  --glue-color-brand-900: #174EA6;

  /* Surfaces */
  --glue-bg-page: #FFFFFF;
  --glue-bg-soft: #F8F9FA;
  --glue-text: #202124;
  --glue-text-muted: #5F6368;
  --glue-border: #DADCE0;

  /* Key spacing */
  --glue-space-sm: 8px;
  --glue-space-md: 16px;
  --glue-space-lg: 24px;

  /* Radius */
  --glue-radius-sm: 4px;
  --glue-radius-md: 24px;
  --glue-radius-pill: 48px;
}

.google-search-rail {
  width: min(584px, calc(100vw - 32px));
  height: 46px;
  border: 1px solid var(--glue-border);
  border-radius: var(--glue-radius-md);
  background: var(--glue-bg-page);
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 14px;
}

.google-search-rail:hover,
.google-search-rail:focus-within {
  box-shadow: 0 1px 6px rgba(32, 33, 36, .28);
  border-color: transparent;
}

.google-login-pill {
  background: var(--glue-color-brand-600);
  color: #FFFFFF;
  border-radius: var(--glue-radius-pill);
  padding: 9px 23px;
  font: 500 14px/20px var(--glue-font-family-display);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js - Google-inspired utility primitives
module.exports = {
  theme: {
    extend: {
      colors: {
        google: {
          blue: '#1A73E8',
          logoBlue: '#4285F4',
          red: '#EA4335',
          yellow: '#FBBC04',
          green: '#34A853',
        },
        neutral: {
          0: '#FFFFFF',
          50: '#F8F9FA',
          100: '#F1F3F4',
          200: '#E8EAED',
          300: '#DADCE0',
          700: '#5F6368',
          900: '#202124',
        },
      },
      fontFamily: {
        sans: ['Google Sans Text', 'Arial', 'Helvetica', 'sans-serif'],
        display: ['Google Sans', 'Arial', 'Helvetica', 'sans-serif'],
        mono: ['Roboto Mono', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
      },
      borderRadius: {
        search: '24px',
        pill: '48px',
        button: '4px',
      },
      boxShadow: {
        search: '0 1px 6px rgba(32, 33, 36, .28)',
        glue1: '0 1px 2px 0 rgba(60,64,67,.3), 0 1px 3px 1px rgba(60,64,67,.15)',
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
| Brand primary | `{colors.primary}` | `#1A73E8` |
| Background | `{colors.surface-base}` | `#FFFFFF` |
| Text primary | `{colors.text-primary}` | `#202124` |
| Text muted | `{colors.text-muted}` | `#5F6368` |
| Border | `{colors.border-hairline}` | `#DADCE0` |
| Soft surface | `{colors.surface-soft}` | `#F8F9FA` |
| Error/red identity | `{colors.logo-red}` | `#EA4335` |

### Example Component Prompts

#### Hero/Search Section

```text
Google homepage style search section을 만들어줘.
- 배경: #FFFFFF, full viewport utility canvas
- 중앙 오브젝트: Google-style logo artwork above a 584px max-width search rail
- Search rail: #FFFFFF, border #DADCE0, radius 24px, height 46px, hover shadow 0 1px 6px rgba(32,33,36,.28)
- 텍스트: Google Sans Text or Arial fallback, #202124, 14-16px, weight 400
- 아래 버튼: #F8F9FA, #202124 text, 4px radius, 36px height
- 장식/카드/hero paragraph 없이 검색 작업만 남겨줘
```

#### Account Button

```text
Google-style login button을 만들어줘.
- background #1A73E8, text #FFFFFF
- font Google Sans 14px weight 500
- border-radius 48px, padding 9px 23px
- hover는 #185ABC 계열로 어둡게, focus는 2px blue ring
```

#### Search Rail

```text
Google search rail 컴포넌트를 만들어줘.
- width min(584px, calc(100vw - 32px)), height 46px
- background #FFFFFF, border 1px solid #DADCE0, radius 24px
- icon color #5F6368, input text #202124
- hover/focus shadow만 추가하고 fill color는 바꾸지 마
```

#### Footer

```text
Google homepage footer를 만들어줘.
- background #F2F2F2 또는 #F8F9FA 계열
- text #5F6368 / #202124, 14px
- top border #DADCE0
- 링크를 얇은 horizontal rail로 배치하고 카드처럼 만들지 마
```

### Iteration Guide

- **색상 변경 시**: logo colors와 UI blue를 분리한다. CTA/focus는 `#1A73E8`, logo artwork는 `#4285F4/#EA4335/#FBBC04/#34A853`.
- **폰트 변경 시**: 400을 기본으로 유지하고 500은 account/action 강조에만 사용한다.
- **여백 조정 시**: 중앙부 공백을 먼저 지킨다. 검색 rail 주변을 카드 섹션처럼 채우면 Google다움이 사라진다.
- **새 컴포넌트 추가 시**: `#FFFFFF`, `#F8F9FA`, `#DADCE0`, 4px/24px/48px radius 중 하나로 의도를 분리한다.
- **반응형**: 599px/600px/1024px breakpoints를 우선 사용하고 임의 breakpoint를 늘리지 않는다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- `#FFFFFF`를 주 surface로 두고 중앙 검색 작업 외의 시각 요소를 줄인다.
- UI primary blue는 `#1A73E8`로 잡고, logo blue `#4285F4`와 구분한다.
- 텍스트는 `#202124`, secondary는 `#5F6368`, border는 `#DADCE0`로 계층을 만든다.
- 검색 rail은 24px pill + thin border + subtle hover shadow 조합으로 만든다.
- 버튼 intent를 radius로 구분한다: account pill 48px, neutral search button 4px.
- footer는 soft gray band로 낮게 처리하고 본문 영역과 확실히 분리한다.

### ❌ DON'T

- 배경을 `#F5F5F5` 또는 `#FAFAFA`로 두지 말 것 — 대신 homepage main surface는 `#FFFFFF` 사용.
- 본문 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#202124` 사용.
- muted text를 `#777777` 또는 `#666666`으로 두지 말 것 — 대신 `#5F6368` 사용.
- border를 `#CCCCCC` 또는 `#E0E0E0`으로 두지 말 것 — 대신 `#DADCE0` 사용.
- CTA/focus blue를 `#4285F4`로 두지 말 것 — 대신 UI action은 `#1A73E8` 사용.
- neutral button fill을 `#FFFFFF`로 두지 말 것 — 대신 `#F8F9FA` 사용.
- search rail을 8px/12px radius 카드로 만들지 말 것 — 24px pill shape가 핵심이다.
- 모든 버튼을 999px pill로 만들지 말 것 — Google search buttons는 4px rectangle이다.
- homepage hero에 headline paragraph나 feature grid를 넣지 말 것 — 검색 input 자체가 hero다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- Brand gradient: absent. No `linear-gradient(135deg, #667eea, #764ba2)` or rainbow UI backgrounds.
- Second UI brand color: none. Logo has four colors, but interactive UI resolves to blue plus neutrals.
- Decorative cards: absent on the homepage. The search rail is a control, not a content card.
- Heavy shadows: absent. Only the search rail receives a subtle hover/focus lift.
- Display headline: absent. The logo is the only large visual language.
- Dense nav: absent. Top links are utility fragments, not a product navigation bar.
- Icon color variety: absent. Icons stay gray/dark, not logo-colored.
- Animated delight: essentially absent. No parallax, no particle system, no scroll-triggered hero.
- Weight 600/800/900: absent from the visible homepage identity; 400/500 do the work.
- Marketing proof blocks: absent from the homepage. No testimonials, logo wall, stats, or feature cards.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Mixed artifact source** — `hero-cropped.png` shows the localized `google.com` search homepage, while `index.html` metadata/title points to `about.google`. This guide prioritizes the Google homepage screenshot and shared Glue/CSS tokens; About-only editorial modules are treated as secondary.
- **No fresh crawl performed** — per request, existing phase1 artifacts were reused. If Google changed the live homepage after the cached capture, this file reflects the cached artifacts rather than a new fetch.
- **Homepage interaction states are partially inferred** — focus/hover values are grounded in CSS token/shadow patterns, but no live browser interaction trace was captured in this run.
- **Search autocomplete/results not included** — dropdown suggestions, results page, ads modules, and AI mode expanded states were not visited.
- **Dark mode mapping not complete** — CSS contains dark/primary variants, but the visible homepage capture is light mode only.
- **Exact logo geometry not reproduced** — the logo should remain artwork/SVG. This guide does not provide vector paths or optical corrections for the wordmark.
- **Localized typography may vary** — screenshot includes Korean UI text; CSS includes localized Google Sans/Noto stacks. Exact glyph metrics differ by locale.
- **Motion code not deeply inspected** — CSS shows transition/reduced-motion hooks, but JavaScript-driven UI motion was not analyzed.
- **Form validation and error states not surfaced** — the search field is a single neutral task field; error/loading states belong to other Google surfaces and are not specified here.
