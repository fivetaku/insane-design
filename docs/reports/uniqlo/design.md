---
schema_version: 3.1
slug: uniqlo
service_name: UNIQLO
site_url: https://www.uniqlo.com/us/en
fetched_at: 2026-04-23
default_theme: light
brand_color: "#E00"
primary_font: UniqloProRegular
font_weight_normal: 400
token_prefix: "brand-global-ec-uikit + ec-components (--ec-*)"

bold_direction: "Retail Utility Minimal"
aesthetic_category: "Monochrome Retail System"
signature_element: square_black_cta
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — UNIQLO (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere

UNIQLO의 미국 글로벌 네비게이션 CSS 3개 번들은 `#000` / `#fff` / `#dadada` / `#6a6a6a` 같은 모노크롬 토큰을 기본축으로 두고, `#e00` 계열 red를 `attention`, `promotional`, `error`, `selected-heart` 상태에만 제한적으로 배치한다. primary action 계열 root token도 `--primaryDefaultBackgroundColor: #000`, `--primaryHoverBackgroundColor: #2a2a2a`, `--primaryPressedBackgroundColor: #3e3e3e`처럼 black ramp를 중심으로 잡혀 있다. 즉, 사용자가 체감하는 브랜드 인상은 red·white·black이지만, 실제 UI 작동층은 black/white/gray가 대부분을 담당한다.

타이포그래피도 이 이중 구조가 명확하다. Latin display/UI는 `UniqloProBold`, `UniqloProRegular`, `UniqloProLight` 3개 커스텀 폰트가 잡고, body copy는 영어에서 `"Twemoji Country Flags", "Helvetica Neue", Helvetica, Arial, system-ui, -apple-system, sans-serif`를 사용한다. 일본어는 `:lang(ja)` 전용 CJK stack이 별도로 존재하고, 한국어 selector도 다수 존재하지만 이 3개 CSS 안에서는 `--body-font-ko` 같은 dedicated custom property는 확인되지 않았다.

레이아웃은 매우 기능적이다. `--min-target-size: 44px`, navigation header height `64px` / `56px`, search content max `976px`, centered tabs max `412px`, search bar button width `382px → 324px → 231px` 같은 수치가 먼저 나오고, radius는 button height 32/40/50/52용 token이 모두 `0`이다. rounded retail-card보다 square utility system에 가깝다.

색상 면적 배분도 보수적이다. 다운로드한 CSS에서 literal hex 빈도 상위는 `#FFFFFF`(266), `#000000`(188), `#DADADA`(172), `#ABABAB`(115), `#EE0000`(86) 순이었고, literal `#FF0000`는 이 세 개 CSS 번들 안에서 발견되지 않았다. red는 존재하지만 system root literal은 `#e00`으로 압축돼 있다.

### Key Characteristics

- black primary action ramp — `#000 → #2a2a2a → #3e3e3e`
- white canvas + gray separator — `#fff`, `#f4f4f4`, `#dadada`, `#6a6a6a`, `#ababab`
- red is sparse — `#e00`, `#ee3535`, `#ef5555`, `#dd3535`
- blue is utility, not brand — `#005db5`, `#006ed7`
- custom Latin fonts + system body stack
- square buttons and tabs — button radius tokens `0`
- 44px minimum target, 64/56px navigation header
- 599 / 600 / 959 / 960 responsive thresholds
- `--ec-*` custom props concentrate in navigation/search/product modules

### BOLD Direction Summary

> **BOLD Direction**: Retail Utility Minimal
> **Aesthetic Category**: Monochrome Retail System
> **Signature Element**: `square_black_cta` — black action surfaces, white canvas, red only for promotional/error micro-surfaces
> **Code Complexity**: medium — global semantic root tokens + module-level `--ec-*` variables + locale-scoped typography

---

## 01. Quick Start

> CSS literal 기준으로 UNIQLO 느낌을 재현할 때 가장 먼저 복원해야 하는 축은 typography, monochrome action palette, square layout이다.

```css
/* 1. typography */
:root {
  --font-display: UniqloProRegular, sans-serif;
  --font-display-light: UniqloProLight, system-ui, -apple-system, sans-serif;
  --font-body-en: "Twemoji Country Flags", "Helvetica Neue", Helvetica, Arial, system-ui, -apple-system, sans-serif;
  --font-weight-light: 300;
  --font-weight-regular: 400;
  --font-weight-semi-bold: 600;
  --letter-spacing-uniqlo-pro: 0.025rem;
  --line-height-body: 1.5;
}
```

```css
/* 2. color system */
:root {
  --fg: #000;
  --fg-hover: #2a2a2a;
  --fg-pressed: #3e3e3e;
  --fg-muted: #6a6a6a;
  --fg-disabled: #ababab;
  --bg: #fff;
  --bg-subtle: #f4f4f4;
  --border: #dadada;
  --brand-accent: #e00;
  --brand-accent-hover: #ef5555;
  --utility-link: #005db5;
  --utility-link-hover: #006ed7;
  --positive: #00ab0f;
}
```

```css
/* 3. shape + layout */
:root {
  --radius-ui: 0;
  --radius-pill: 999px;
  --space-4: 4px;
  --space-12: 12px;
  --space-16: 16px;
  --nav-height-lg: 64px;
  --nav-height-sm: 56px;
  --target-min: 44px;
}
.button,
.chip,
.tab {
  border-radius: var(--radius-ui);
  min-height: var(--target-min);
}
```

**절대 하지 말 것 하나**: 다운로드한 CSS 3개를 기준으로 보면 literal red `#FF0000`는 없고, red family token도 primary action 기본값이 아니다. CTA를 빨갛게 채우기보다 `#000` filled action + `#e00` promotional/error accent 조합으로 가야 한다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.uniqlo.com/us/en` |
| Fetched | `2026-04-23` |
| Extractor | `python3 + curl_cffi` (`requests.Session(impersonate="safari")`) |
| Referer | `https://www.uniqlo.com/` |
| CSS bundle 1 | `brand-global-ec-uikit-ece049ccc6d736d49b41.css` — `559,312` bytes |
| CSS bundle 2 | `fr-ito-web-react-ece049ccc6d736d49b41.css` — `136,687` bytes |
| CSS bundle 3 | `ec-components-ece049ccc6d736d49b41.css` — `89,234` bytes |
| Total inspected CSS | `785,233` bytes |
| `@font-face` count | `4` (`UniqloProRegular`, `UniqloProBold`, `UniqloProLight`, `swiper-icons`) |
| Confirmed `--ec-*` props | `11` |
| Literal `#FF0000` in downloaded CSS | `not found` |
| Method | CSS literal / selector / custom property extraction only — AI-generated values 없음 |

---

## 03. Tech Stack

- **Bundle split** — `brand-global-ec-uikit`가 global token과 utility layer를, `ec-components`가 search / navigation / product-table component vars를 담당한다. `fr-ito-web-react`라는 asset name도 함께 배포된다.
- **Class naming** — `.fr-ec-*`, `.ec-*`, `.navigation-*`, `.tab-group-*`, `.product-table*`처럼 기능명 중심.
- **Theme default** — `light`. `--fill-secondary-color: #fff`, `--text-primary-dark-color: #000`, `--fill-background-color: #f4f4f4`.
- **Typography model** — Latin custom font + locale-specific system stacks + `:lang(ja)` / `:lang(ko)` selector 분기.
- **Responsive model** — `599px`, `600px`, `959px`, `960px`, `1249px` 기준. `--grid-size-lg: 1200px`.
- **Interaction palette** — brand-red보다 black primary palette, blue utility palette, green positive state 분리.
- **Shape system** — pill token은 존재하지만 core action/button height radii가 전부 `0`.

---

## 04. Font Stack

- **Title / Latin strong** — `UniqloProBold, system-ui, -apple-system, sans-serif`
- **Regular / Latin UI** — `UniqloProRegular, sans-serif`
- **Light / Latin secondary** — `UniqloProLight, system-ui, -apple-system, sans-serif`
- **Body / English** — `"Twemoji Country Flags", "Helvetica Neue", Helvetica, Arial, system-ui, -apple-system, sans-serif`
- **Title / Japanese** — `"ヒラギノ角ゴ Pro", "Hiragino Kaku Gothic Pro", "Hiragino Sans", "Noto Sans CJK JP", Osaka, Meiryo, メイリオ, "MS PGothic", "ＭＳ Ｐゴシック", YuGothic, "Yu Gothic", "Hiragino Sans GB", Helvetica Neue, HelveticaNeue, Helvetica, Noto Sans, Roboto, Arial, "Arial Unicode MS", sans-serif`
- **Body / Japanese** — `"Twemoji Country Flags", "ヒラギノ角ゴ Pro", "Hiragino Kaku Gothic Pro", "Hiragino Sans", "Noto Sans CJK JP", Osaka, Meiryo, メイリオ, "MS PGothic", "ＭＳ Ｐゴシック", YuGothic, "Yu Gothic", "Hiragino Sans GB", Helvetica Neue, HelveticaNeue, Helvetica, Noto Sans, Roboto, Arial, "Arial Unicode MS", sans-serif`
- **Body / Thai** — `"Twemoji Country Flags", "Leelawadee UI", "Segoe UI", Thonburi, "Helvetica Neue", Helvetica, Arial, -apple-system, system-ui, sans-serif`
- **Body / Vietnamese** — `"Twemoji Country Flags", "Segoe UI", "Helvetica Neue", Helvetica, Arial, -apple-system, system-ui, sans-serif`
- **Korean note** — `:lang(ko)` selector는 다수 존재하지만 이 세 CSS 안에서는 `--body-font-ko` / `--title-font-ko` custom property를 찾지 못했다.
- **Weights** — `300 / 400 / 500 / 600 / 700 / 800`

```css
:root {
  --title-font-en: UniqloProBold, system-ui, -apple-system, sans-serif;
  --regular-font-en: UniqloProRegular, sans-serif;
  --light-font-en: UniqloProLight, system-ui, -apple-system, sans-serif;
  --body-font-en: "Twemoji Country Flags", "Helvetica Neue", Helvetica, Arial, system-ui, -apple-system, sans-serif;
  --font-weight-light: 300;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semi-bold: 600;
  --font-weight-bold: 700;
  --font-weight-extra-bold: 800;
}
```

---

## 05. Typography Scale

### Latin scale

| Token | Value |
|---|---|
| `--type-scale-latin-minus-2` | `0.75rem` |
| `--type-scale-latin-minus-1` | `0.875rem` |
| `--type-scale-latin-base` | `1rem` |
| `--type-scale-latin-plus-1` | `1.125rem` |
| `--type-scale-latin-plus-2` | `1.25rem` |
| `--type-scale-latin-plus-3` | `1.5rem` |
| `--type-scale-latin-plus-4` | `1.75rem` |
| `--type-scale-latin-plus-5` | `2rem` |
| `--type-scale-latin-plus-6` | `2.25rem` |

### CJK scale

| Token | Value |
|---|---|
| `--type-scale-cjk-minus-2` | `0.6875rem` |
| `--type-scale-cjk-minus-1` | `0.8125rem` |
| `--type-scale-cjk-base` | `0.9375rem` |
| `--type-scale-cjk-plus-1` | `1.0625rem` |
| `--type-scale-cjk-plus-2` | `1.1875rem` |
| `--type-scale-cjk-plus-3` | `1.375rem` |
| `--type-scale-cjk-plus-4` | `1.625rem` |
| `--type-scale-cjk-plus-5` | `1.875rem` |
| `--type-scale-cjk-plus-6` | `2.25rem` |

### Line-height and tracking

| Token | Value |
|---|---|
| `--line-height-01` | `1` |
| `--line-height-02` | `1.1` |
| `--line-height-03` | `1.2` |
| `--line-height-04-minus-1` | `1.3` |
| `--line-height-04` | `1.4` |
| `--line-height-05` | `1.5` |
| `--letter-spacing-uniqlo-pro` | `0.025rem` |

### Representative selectors

| Selector | Size | Weight | Line-height |
|---|---|---|---|
| `.body--standard` | `0.9375rem` (`--type-scale-cjk-base`) | `300` | `1.5` |
| `.display--display5` | `1.125rem` (Latin) / `1.0625rem` (JA/KO) | `400` / `300` | `1.2` / `1.5` |
| `.display--display3` | `calc(1.375rem + 2px)` | `400` | `1.2` |
| `.display--display2` | `calc(1.875rem + 2px)` | `400` | `1.4` |
| `.display--display1` | `2.25rem` | `400` | `1.2` |

---

## 06. Colors

### 06-1. Core monochrome

| Token | Value | Usage |
|---|---|---|
| `--fill-primary-color` | `#000` | primary fill |
| `--primaryHoverBackgroundColor` | `#2a2a2a` | primary hover |
| `--primaryPressedBackgroundColor` | `#3e3e3e` | primary pressed |
| `--fill-secondary-color` | `#fff` | inverse / neutral fill |
| `--fill-background-color` | `#f4f4f4` | surface background |
| `--border-lines-color` | `#dadada` | lines / dividers |
| `--text-secondary-color` | `#6a6a6a` | secondary text |
| `--text-disabled-color` | `#ababab` | disabled text |
| `--border-interactive-outline-color` | `#767676` | interactive outline |

### 06-2. Promotional / error red

| Token | Value | Usage |
|---|---|---|
| `--fill-promotional-color` | `#e00` | promo fill |
| `--fill-promotional-hover-color` | `#ee3535` | promo hover |
| `--fill-error-color` | `#e00` | error fill |
| `--fill-error-hover-color` | `#ef5555` | error hover |
| `--fill-selected-heart-color` | `#e00` | selected heart |
| `--fill-selected-heart-hover-color` | `#dd3535` | selected heart hover |

> 참고: 다운로드한 CSS 번들 안에서는 literal `#FF0000`는 발견되지 않았고, red family literal은 `#e00` / `#ee3535` / `#ef5555` / `#dd3535`로 나타난다.

### 06-3. Utility accents

| Token | Value | Usage |
|---|---|---|
| `--fill-noticeable-color` | `#005db5` | noticeable fill |
| `--fill-noticeable-hover-color` | `#006ed7` | noticeable hover |
| `--text-noticeable-color` | `#005db5` | link / text utility |
| `--text-noticeable-hover-color` | `#006ed7` | utility hover |
| `--fill-positive-color` | `#00ab0f` | positive state |

### 06-4. Dominant literal colors in downloaded CSS

| Rank | Hex | Count |
|---|---|---|
| 1 | `#FFFFFF` | 266 |
| 2 | `#000000` | 188 |
| 3 | `#DADADA` | 172 |
| 4 | `#ABABAB` | 115 |
| 5 | `#EE0000` | 86 |
| 6 | `#6A6A6A` | 81 |
| 7 | `#F4F4F4` | 77 |
| 8 | `#005DB5` | 73 |
| 9 | `#767676` | 70 |
| 10 | `#2A2A2A` | 53 |

---

## 07. Spacing

### Root spacing scale

| Token | Value |
|---|---|
| `--spacing0` | `0` |
| `--spacing4` | `4px` |
| `--spacing8` | `8px` |
| `--spacing12` | `12px` |
| `--spacing16` | `16px` |
| `--spacing20` | `20px` |
| `--spacing24` | `24px` |
| `--spacing28` | `28px` |
| `--spacing32` | `32px` |
| `--spacing36` | `36px` |
| `--spacing40` | `40px` |
| `--spacing44` | `44px` |
| `--spacing48` | `48px` |
| `--spacing52` | `52px` |
| `--spacing88` | `88px` |

### Grid margins

| Token | Value |
|---|---|
| `--spacing-grid-margin-at-medium` | `1.5rem` |
| `--spacing-grid-margin-at-large` | `3rem` |

### Observed usages

- `.ec-button--search-bar` — horizontal padding `var(--spacing12)`
- `.product-table` — left padding `var(--spacing16)`
- `.product-table__current-product .product-tile` — bottom margin `var(--spacing8)`
- `.navigation-header__gender-tab__left` — left padding `var(--spacing52)` on large screens

---

## 08. Radius

| Token | Value | Note |
|---|---|---|
| `--border-radius-pill` | `999px` | pill / chip |
| `--border-radius-round` | `0` | core square shape |
| `--border-radius-button-h-32` | `0` | button |
| `--border-radius-button-h-40` | `0` | button |
| `--border-radius-button-h-50` | `0` | button |
| `--border-radius-button-h-52` | `0` | button |
| `--borderRadius4` | `4px` | generic radius token |
| `--borderRadius8` | `8px` | generic radius token |
| `--borderRadius12` | `12px` | generic radius token |
| `--borderRadius16` | `16px` | generic radius token |
| `--borderRadius999` | `999px` | generic pill |
| `--borderRadius50Percent` | `50%` | circular icon / indicator |

> Core action/button layer는 raw button radius token이 전부 `0`이라 square bias가 매우 강하다.

---

## 09. Shadows

| Token | Value | Usage signal |
|---|---|---|
| `--shadow-floating` | `0px 2px 4px #0003` | floating layer |
| `--shadow-floating-er` | `0px 0px 10px #0000001a` | extended floating layer |
| `--shadow-other` | `0px 2px 2px #0009` | dense dark shadow |
| `--shadow-chip` | `0px 0px 4px #000c` | chip edge |
| `--shadowBottom1` | `0px 1px 1px #00000080` | subtle elevation |
| `--shadowBottom4` | `0px 2px 4px #0000001a` | card/flyout |
| `--shadowBevel15` | `0px 0px 15px #0000001a` | large blur |
| `--shadowNone` | `none` | explicit reset |

---

## 10. Motion

| Token | Value |
|---|---|
| `--animate-duration-shortest` | `150ms` |
| `--animate-duration-micro` | `180ms` |
| `--animate-duration-leave` | `195ms` |
| `--animate-duration-shorter` | `200ms` |
| `--animate-duration-enter` | `225ms` |
| `--animate-duration-short` | `250ms` |
| `--animate-duration-normal` | `300ms` |
| `--animate-duration-standard` | `300ms` |
| `--animate-duration-complex` | `375ms` |
| `--animate-duration-macro` | `500ms` |
| `--animate-ease-in-out` | `cubic-bezier(0.4,0,0.2,1)` |
| `--animate-ease-out` | `cubic-bezier(0.0,0,0.2,1)` |
| `--animate-ease-in` | `cubic-bezier(0.4,0,1,1)` |
| `--animate-ease-sharp` | `cubic-bezier(0.4,0,0.6,1)` |

---

## 11. Layout Patterns

- **Root font size** — `16px`
- **Minimum target size** — `44px`
- **Large grid width** — `1200px`
- **Large grid fixed-margin limit** — `1248px`
- **Large grid auto-margin limit** — `1249px`
- **Navigation header height** — `64px` large / `56px` small
- **Navigation logo max size** — `75px × 34px` large / `63px × 28px` small
- **Centered tabs max width** — `412px`
- **Navigation search content max width** — `976px`
- **Product table content gap** — `1px`

```css
.navigation-header__wrapper {
  height: var(--ec-navigation-header-height-lg);
}
.navigation-search__content {
  max-width: var(--ec-search-max-width);
  width: 100%;
}
.navigation-header__gender-tab__center .tab-group-outer-wrapper {
  max-width: var(--ec-tabs-max-width);
  width: 100%;
}
```

---

## 12. Responsive

| Breakpoint | Value | Observed behavior |
|---|---|---|
| small max | `599px` | small header `56px`, logo `63 × 28`, search button height `38px`, search button max `231px` |
| medium min | `600px` | app-download button wrapper hidden |
| medium max | `959px` | centered gender tabs hidden, search bar `324px`, right navigation condensed |
| large min | `960px` | large header `64px`, search button `382px`, centered gender tabs restored |
| extra large auto margin | `1249px` | grid auto margin threshold |

```css
.ec-button--search-bar {
  max-width: var(--ec-search-bar-button-max-width-lg);
  padding: 0 var(--spacing12);
  width: 100vw;
}
@media screen and (max-width:959px) {
  .ec-button--search-bar { max-width: var(--ec-search-bar-button-max-width-md); }
}
@media screen and (max-width:599px) {
  .ec-button--search-bar {
    height: var(--ec-search-bar-button-height-sm);
    max-width: var(--ec-search-bar-button-max-width-sm);
  }
  .ec-button--search-bar:before {
    top: var(--ec-search-bar-button-tappable-offset-sm);
    bottom: var(--ec-search-bar-button-tappable-offset-sm);
  }
}
```

---

## 13. Components

### Navigation header

- background — `#fff`
- wrapper height — `64px` / `56px`
- logo max size — `75px × 34px` / `63px × 28px`
- centered tab wrapper — `412px`
- search content max width — `976px`
- notification dot — `6px × 6px`, `background: #e00`

### Search bar button

- base max width — `382px`
- tablet max width — `324px`
- mobile max width — `231px`
- mobile height — `38px`
- horizontal padding — `12px`
- tappable pseudo offset — `-3px`

### Tab group

- group border bottom — `1px solid #dadada`
- active tab text — `#000`
- active hover text — `#2a2a2a`

```css
.tab-group {
  border-bottom: 1px solid #dadada;
  display: flex;
  padding: 0;
}
.tab--is-active {
  color: #000;
}
.tab--is-active:hover {
  color: #2a2a2a;
}
```

### Product comparison table

- container left padding — `16px`
- inner gap — `1px`
- product tile bottom margin — `8px`

```css
.product-table {
  padding-left: var(--spacing16);
}
.product-table-inner-container {
  gap: var(--ec-product-table-content-gap);
}
.product-table__current-product .product-tile,
.product-table__similar-product .product-tile {
  margin-bottom: var(--spacing8);
}
```

---

## 14. Content Voice

이 리포트는 CSS 기반이므로 marketing copy tone 자체는 추출하지 않았다. 다만 token/selector naming은 매우 utilitarian하다: `primary`, `secondary`, `promotional`, `noticeable`, `positive`, `error`, `selected-heart`, `product-table`, `navigation-search`. 감성적인 naming보다 기능/상태 naming이 우선이며, 이 naming discipline이 UI 인상에도 그대로 반영된다.

---

## 15. CSS Export

```css
:root {
  --uq-font-display: UniqloProRegular, sans-serif;
  --uq-font-display-light: UniqloProLight, system-ui, -apple-system, sans-serif;
  --uq-font-body-en: "Twemoji Country Flags", "Helvetica Neue", Helvetica, Arial, system-ui, -apple-system, sans-serif;

  --uq-fg: #000;
  --uq-fg-hover: #2a2a2a;
  --uq-fg-pressed: #3e3e3e;
  --uq-fg-muted: #6a6a6a;
  --uq-fg-disabled: #ababab;
  --uq-bg: #fff;
  --uq-bg-subtle: #f4f4f4;
  --uq-border: #dadada;

  --uq-brand: #e00;
  --uq-brand-hover: #ef5555;
  --uq-brand-heart-hover: #dd3535;
  --uq-link: #005db5;
  --uq-link-hover: #006ed7;
  --uq-positive: #00ab0f;

  --uq-radius: 0;
  --uq-radius-pill: 999px;
  --uq-shadow-floating: 0px 2px 4px #0003;

  --uq-space-4: 4px;
  --uq-space-8: 8px;
  --uq-space-12: 12px;
  --uq-space-16: 16px;
  --uq-space-24: 24px;
  --uq-space-32: 32px;
  --uq-space-44: 44px;
  --uq-space-52: 52px;

  --uq-nav-h-lg: 64px;
  --uq-nav-h-sm: 56px;
  --uq-search-max: 976px;
  --uq-tabs-max: 412px;
}
```

---

## 16. Tailwind Export

```js
export default {
  theme: {
    extend: {
      colors: {
        uniqlo: {
          black: "#000",
          blackHover: "#2a2a2a",
          blackPressed: "#3e3e3e",
          white: "#fff",
          surface: "#f4f4f4",
          border: "#dadada",
          muted: "#6a6a6a",
          disabled: "#ababab",
          red: "#e00",
          redHover: "#ef5555",
          redHeartHover: "#dd3535",
          blue: "#005db5",
          blueHover: "#006ed7",
          positive: "#00ab0f"
        }
      },
      fontFamily: {
        uniqlo: ["UniqloProRegular", "sans-serif"],
        uniqloLight: ["UniqloProLight", "system-ui", "-apple-system", "sans-serif"],
        body: ["Twemoji Country Flags", "Helvetica Neue", "Helvetica", "Arial", "system-ui", "-apple-system", "sans-serif"]
      },
      borderRadius: {
        none: "0",
        pill: "999px"
      },
      boxShadow: {
        floating: "0px 2px 4px #0003",
        floatingEr: "0px 0px 10px #0000001a"
      },
      spacing: {
        1: "4px",
        2: "8px",
        3: "12px",
        4: "16px",
        5: "20px",
        6: "24px",
        7: "28px",
        8: "32px",
        9: "36px",
        10: "40px",
        11: "44px",
        12: "48px",
        13: "52px",
        22: "88px"
      },
      screens: {
        uqMd: "600px",
        uqLg: "960px"
      }
    }
  }
};
```

---

## 17. Agent Prompt

- white canvas `#fff`, black primary action `#000`, border `#dadada`, muted text `#6a6a6a`를 기본으로 시작할 것
- red accent는 `#e00` family만 사용하고 promotional / error / favorite heart처럼 면적이 작은 상태에 제한할 것
- 링크 / focus / noticeable state는 `#005db5` → hover `#006ed7`로 분리할 것
- 버튼과 탭은 square radius `0`을 기본값으로 둘 것
- 44px minimum target, 64px desktop header, 56px mobile header, 382/324/231px search widths를 그대로 유지할 것
- Latin display가 필요하면 `UniqloProRegular` / `UniqloProLight` 계열을 우선하고, body는 Helvetica/Arial/system stack으로 떨어질 수 있게 둘 것

---

## 18. Do / Don’t

### Do

- black filled action을 기본 동작색으로 사용
- `#fff` / `#f4f4f4` / `#dadada` 위계로 surface를 분리
- `#e00`를 작은 상태 색으로만 사용
- 버튼, 탭, chip의 기본 corner를 square로 유지
- 599 / 959 / 960 breakpoint 체계를 그대로 사용

### Don’t

- `#FF0000` full-fill CTA를 primary button 기본값으로 두지 말 것
- 12px / 16px rounded card를 기본 UI 문법으로 확대하지 말 것
- blue `#005db5`를 브랜드 메인 컬러처럼 확대하지 말 것
- neutral text를 pure black 하나로만 처리하지 말 것 — `#6a6a6a` / `#ababab` 계층을 유지
- search / nav / product table의 실제 max-width 수치를 임의로 바꾸지 말 것
