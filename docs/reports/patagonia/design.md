---
schema_version: 3.1
slug: patagonia
service_name: Patagonia
site_url: https://www.patagonia.com/home/
fetched_at: 2026-04-23
default_theme: light
brand_color: "#FA4616"
primary_font: Ridgeway Sans
font_weight_normal: 300
token_prefix: --pata-*, --bs-*

bold_direction: "Outdoor Utility Minimalism"
aesthetic_category: "Utility Brutalism"
signature_element: section_transition
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Patagonia (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: auto+manual -->

2026-04-23 기준 Patagonia 홈은 "환경 브랜드 = 초록 UI" 공식을 따르지 않는다. 현재 Demandware/Salesforce Commerce Cloud 프런트는 오히려 **`#000` / `#fff` / `#f5f5f5` / `#121212`** 로 짜인 강한 흑백 베이스 위에, 필요한 순간에만 색을 꽂는 **outdoor utility system** 에 가깝다. 상단 네비게이션, 기본 CTA, dark wrapper, 카드 배경이 모두 검정과 흰색의 반전으로 운영되고, 브랜드 개성은 사진과 섹션 테마, 그리고 소량의 accent 팔레트에서 뒤늦게 드러난다.

색상 전략의 핵심은 **"모노크롬 UI + 자연계 팔레트의 spot usage"** 다. CSS 전역의 가장 큰 축은 `#000`(primary/dark) 과 `#fff`(page/light), `#f5f5f5`(card surface), `#121212`(dark surface)다. 하지만 같은 CSS 안에는 `red-brand #FA4616`, `campfire-orange #F47B29`, `yellow-utility #FEB904`, `green-utility #32B67A`, `steppe-green #61845B`, `industrial-green #485643` 같은 named color family가 살아 있다. 즉 Patagonia의 색은 "초록 메인 브랜드"가 아니라, **기본 UI는 흑백으로 정리하고 자연색은 상태/캠페인/테마에만 쓰는 방식**으로 작동한다.

타이포그래피도 기존 예시의 Avenir 가설과 다르다. 현재 live HTML/CSS는 **`Ridgeway Sans`를 body/UI 기본체로, `Copernicus`를 serif accent로 로드**한다. 본문은 `font-weight: 300`, `line-height: 1.5`의 가벼운 산세리프이고, serif 계층은 `font-weight: 500`, `letter-spacing: -0.03em ~ -0.05em`, `line-height: 1.1`로 확실히 끊는다. hero headline은 size variant에 따라 `4rem → 6.4rem`, `6.4rem → 9.6rem`, `8rem → 12.8rem`까지 확장되지만, 여전히 weight는 500 하나로 유지된다. Patagonia가 힘을 주는 방식은 굵기 난사가 아니라 **큰 크기 + tight tracking + 흑백 대비**다.

여백과 인터랙션은 Bootstrap 5 유틸리티를 그대로 흡수한 리듬을 따른다. 기본 gutter는 `1.6rem`, 스케일은 `.8rem` 단위로 `8rem`까지 확장되고, hero·slider·navigation·card content가 모두 이 8px rhythm 위에 놓인다. 카드 radius는 `8px`, 버튼 radius는 `3rem`, overlay card는 `1.6rem`, feature pill은 `2rem`으로 분화되어 있다. 즉 Patagonia는 "hard square"가 아니라 **soft card + pill CTA** 조합이다.

모션도 절제돼 있지만 정적이지는 않다. 버튼 hover는 `transform .2s cubic-bezier(.235,0,.05,.95)` 와 `scale(1.044)`, 카드와 hero는 `.3s ~ .6s cubic-bezier(.38,.41,.27,1)`, 제품 이미지 교차 전환은 `.75s`, slider arrow는 `scale(1.05)`까지 사용한다. 전반적으로 **기술적이거나 화려한 motion이 아니라, 물리적인 반응감만 남긴 tactile motion** 이다.

### Key Characteristics

- 기본 UI 축은 `#000` / `#fff` / `#f5f5f5` / `#121212`
- `Ridgeway Sans` 300 body + `Copernicus` 500 serif accent
- named outdoor palette: `#FA4616`, `#F47B29`, `#FEB904`, `#32B67A`, `#61845B`, `#485643`
- button radius `3rem`, card radius `8px`, overlay card radius `1.6rem`
- hero split layout: `50/50`, desktop 확장 시 `40/60` 또는 `60/40`
- `.8rem` spacing rhythm과 Bootstrap gutter scale 기반
- hover scale은 작게, easing은 cubic-bezier로 묵직하게

### 🆕 BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Outdoor Utility Minimalism
> **Aesthetic Category**: Utility Brutalism
> **Signature Element**: 이 사이트는 **흑백 UI wrapper 위에 Patagonia named palette를 섹션 단위로만 꽂는 light/dark theme 전환**으로 기억된다.
> **Code Complexity**: medium — Bootstrap 5 토큰층과 Demandware 모듈층이 공존하지만, 핵심 디자인 문법은 비교적 명확하다.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Patagonia처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Ridgeway Sans", system-ui, -apple-system, "Segoe UI",
    Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans",
    sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol", "Noto Color Emoji";
  font-weight: 300;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #fff;
  --fg: #000;
  --surface: #f5f5f5;
  --surface-dark: #121212;
}
body {
  background: var(--bg);
  color: var(--fg);
}

/* 3. accent palette */
:root {
  --brand: #FA4616;
  --warning: #FEB904;
  --success: #32B67A;
  --earth-dark: #485643;
}
```

**절대 하지 말아야 할 것 하나**: 페이지 전체를 `#32B67A`나 `#61845B` 톤으로 칠하지 말 것. 현재 live Patagonia UI는 **`#000` / `#fff`가 기본이고**, `#FA4616`, `#F47B29`, `#FEB904`, `#32B67A`, `#61845B`, `#485643`는 상태색·테마색·캠페인 accent다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.patagonia.com/home/` |
| Fetched | 2026-04-23 |
| Extractor | `curl_cffi.requests.Session(impersonate="safari")` + Demandware CSS regex |
| HTML size | `384855` bytes (Demandware SSR) |
| CSS files | 외부 `8`개 + 인라인 `<style>` `3`개, 총 `1757209`자 |
| Token prefix | `--pata-*`, `--bs-*` |
| Method | live HTML/CSS 직접 파싱 · hex/selector 실측 · Avenir 존재 여부 재검증 |

> 확인 메모: 현재 live HTML/CSS에서는 `Avenir Next W02 Light` 문자열이 나오지 않았다. 예시 폴더의 기존 `_inline.css`는 site failover용 legacy 조각으로 보인다.

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Salesforce Commerce Cloud / Demandware SSR (`/on/demandware.static/Sites-patagonia-us-Site/-/en_US/v1776882045978/`)
- **Design system**: Patagonia theme vars (`--pata-*`) 위에 Bootstrap 5 vars (`--bs-*`) 를 얹은 구조
- **CSS architecture**: Bootstrap foundation + Demandware component modules + inline theme wrapper
  ```text
  foundation  (--bs-*)              color / spacing / radius / breakpoints
  brand       (--pata-*)            font family / theme aliases
  modules     (.hero-main__*, .card-tile__*, .primary-navigation__*)
  ```
- **Class naming**: BEM-유사 semantic naming (`hero-main__headline`, `card__inner`, `primary-navigation__container`) + theme wrapper (`page-wrapper.is-light`, `.is-dark`)
- **Default theme**: light (`bg = #fff`)
- **Font loading**: HTML head의 `@font-face` + Demandware static font files (`RidgewaySans`, `GalaxieCopernicus`)
- **Canonical anchor**: `#000` / `#fff` 모노크롬이 앵커, `#FA4616`·`#FEB904`·`#32B67A`·`#91ABE9`는 semantic accent
- **Animation primitives**: `.2s` tactile hover, `.3s ~ .6s` content reveal, `.75s` image swap, reduced-motion 대응 포함

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Body/UI font**: `Ridgeway Sans` (HTML inline `@font-face`, Patagonia self-hosted woff/woff2)
- **Serif accent**: `Copernicus` (`GalaxieCopernicus-Book.woff2`, italic variant 포함)
- **Special variable**: `BT Belwe W01`가 `--pata-font-special`로 정의되지만 2026-04-23 홈 CSS 사용처는 확인되지 않음
- **Code/System monospace**: `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`
- **Weight normal / bold**: `300` / `500` (UI emphasis), `strong`는 `700`

```css
:root {
  --pata-font-sans: "Ridgeway Sans", system-ui, -apple-system, "Segoe UI",
    Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans",
    sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol", "Noto Color Emoji";
  --pata-font-serif: "Copernicus", "Palatino Linotype", Palatino, Palladio,
    "URW Palladio L", "Book Antiqua", Baskerville, "Bookman Old Style",
    "Bitstream Charter", "Nimbus Roman No9 L", Garamond, "Apple Garamond",
    "ITC Garamond Narrow", "New Century Schoolbook", "Century Schoolbook",
    "Century Schoolbook L", Georgia, serif;
  --pata-font-monospace: SFMono-Regular, Menlo, Monaco, Consolas,
    "Liberation Mono", "Courier New", monospace;
}

body {
  font-family: var(--pata-font-sans);
  font-weight: 300;
}

.font__serif {
  font-family: var(--pata-font-serif) !important;
  font-weight: 500 !important;
}
```

> `Avenir Next W02 Light`는 현재 live Patagonia 홈의 기준 폰트가 아니다. legacy failover CSS에만 남아 있으며, 실제 홈 UI를 재현하려면 `Ridgeway Sans`를 써야 한다.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `hero-headline-xl` | `8rem -> 12.8rem` | `500` | `1.1` | `-0.02em` |
| `hero-headline-l` | `6.4rem -> 9.6rem` | `500` | `1.1` | `-0.02em` |
| `hero-headline-m` | `4rem -> 6.4rem` | `500` | `1.1` | `-0.02em` |
| `hero-headline-s` | `3.2rem -> 4.8rem` | `500` | `1.1` | `-0.02em` |
| `bootstrap-h1` | `calc(1.375rem + .9375vw) -> 2.5rem` | `500` | `1.2` | `0` |
| `bootstrap-h2` | `calc(1.325rem + .5625vw) -> 2rem` | `500` | `1.2` | `0` |
| `bootstrap-h3` | `calc(1.3rem + .375vw) -> 1.75rem` | `500` | `1.2` | `0` |
| `serif-snippet` | `1.5rem` | `500` | `1.1` | `-0.03em` |
| `body / p-md` | `1.4rem -> 1.6rem` | `300` | `1.5` | `0` |
| `small / p-sm` | `1.2rem -> 1.4rem` | `300` | `1.5` | `0` |
| `button-label` | `calc(1.285rem + .2625vw) -> 1.6rem` | `500` | `1.2` | `0` |

> ⚠️ Patagonia의 현재 টাই포 핵심은 `Avenir`가 아니라 `Ridgeway Sans 300` + `Copernicus 500` 조합이다. serif를 켜는 순간 tracking이 `-0.03em ~ -0.05em`으로 더 조여지고, 본문은 끝까지 300을 유지한다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Core UI Ramp

| Token | Hex | Usage |
|---|---|---|
| `--bs-black` | `#000` | primary text, dark CTA, nav, dark theme background |
| `dark-surface` | `#121212` | dark card tiles, popover surfaces |
| `meta-copy` | `#4A4A4A` | secondary text, quiet metadata |
| `--bs-gray-100` | `#F5F5F5` | card tile surface, light neutral panels |
| `--bs-white` | `#FFF` | page background, light CTA, light theme foreground pair |

### 06-2. Patagonia Named Accent Palette

| Token | Hex | Usage |
|---|---|---|
| `red-brand` | `#FA4616` | `.text-red-brand`, `.btn-orange`, sale price accent |
| `campfire-orange` | `#F47B29` | themed page wrapper accent |
| `yellow-utility` | `#FEB904` | warning/low inventory, volunteer card theme |
| `green-utility` | `#32B67A` | success/in-stock, validation, petition card theme |
| `blue-utility` | `#91ABE9` | focus border, info, button focus ring |
| `blue-brand` | `#003DA5` | secondary branded wrapper |
| `purple-brand` | `#500778` | secondary branded wrapper |

### 06-3. Earth-Tone Supporting Palette

| Family | Key step | Hex |
|---|---|---|
| `salvia-green` | pale sage | `#A8B197` |
| `bloom-green` | fresh green | `#76B583` |
| `steppe-green` | mid dark green | `#61845B` |
| `hemlock-green` | dark sage | `#536657` |
| `industrial-green` | deepest green | `#485643` |
| `dried-mango` | muted amber | `#CA9456` |
| `surfboard-yellow` | dusty amber | `#DAB965` |
| `shrub-green` | olive accent | `#A19436` |

### 06-4. Semantic System Colors

| Token | Hex | Usage |
|---|---|---|
| `--bs-primary` | `#000` | primary button, dark theme anchor |
| `--bs-secondary` | `#6C757D` | muted system text |
| `--bs-success` | `#32B67A` | in-stock, pristine-valid, success fill |
| `--bs-warning` | `#FEB904` | low stock dot, warning fill |
| `--bs-danger` | `#E10000` | checkout, out-of-stock, destructive state |
| `--bs-info` | `#91ABE9` | focus ring, info emphasis |

### 06-5. Theme Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--pat-theme-back` | `#FFF` or `#000` | section background theme |
| `--pat-theme-fore` | `#000` or `#FFF` | section foreground text |
| `--pat-theme-cta-back` | `#FFF` or `#000` | overlay blurb text color / CTA contrast source |
| `--pat-theme-cta-fore` | `#000` or `#FFF` | overlay card background / CTA inverse |

### 06-6. Dominant Colors (raw CSS frequency)

| Rank | Hex | Count | Role |
|---|---|---|---|
| `1` | `#FFF` | `746` | page bg, light button, inverse foreground |
| `2` | `#000` | `721` | text, nav, dark CTA, dark theme |
| `3` | `#91ABE9` | `284` | focus/info/outline accent |
| `4` | `#CCC` | `106` | light hover border, outlined light states |
| `5` | `#E10000` | `88` | checkout/danger/out-of-stock |
| `6` | `#F5F5F5` | `68` | card tiles and neutral surfaces |
| `7` | `#32B67A` | `56` | success/in-stock |
| `8` | `#FA4616` | `52` | red-brand, orange CTA, sale value |
| `9` | `#4A4A4A` | `44` | secondary copy |
| `10` | `#FEB904` | `42` | warning/low inventory |

> Patagonia의 현재 홈은 색이 없는 것이 아니라, **색을 늦게 보여주는** 구조다. 흑백이 1차 레이어, 자연 팔레트는 2차 레이어다.

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| `g-1` | `0.8rem (8px)` | micro gap, nav grid gap, CTA margin unit |
| `g-2` | `1.6rem (16px)` | default gutter, base layout padding, overlay inset |
| `g-3` | `2.4rem (24px)` | nav desktop vertical padding, hero inner mobile padding |
| `g-4` | `3.2rem (32px)` | card content horizontal padding, slider nav figure mobile size |
| `g-5` | `4rem (40px)` | slider container side padding multiplier |
| `g-8` | `6.4rem (64px)` | hero desktop vertical padding, slider container tablet padding |
| `g-10` | `8rem (80px)` | off-image hero side padding, on-image hero desktop, slider container desktop |

**주요 alias**:

- `--bs-gutter-x` — `1.6rem`; Patagonia 레이아웃 대부분이 여기서 출발한다.
- spacing scale — `.8rem` 증분으로 증가하며, hero·slider·navigation·card 모두 같은 리듬을 공유한다.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--bs-border-radius-sm` | `4px` | small system control |
| `--bs-border-radius` | `8px` | 기본 카드, card tile |
| `--bs-border-radius-lg` | `12px` | larger panel shell |
| `hero-overlay-info` | `1.6rem` | floating info card |
| `feature-pill` | `2rem` | feature/filter pill |
| `--bs-border-radius-xl` | `22px` | large system panel |
| `--bs-btn-border-radius` | `3rem` | 모든 주요 CTA / pill button |
| `circle` | `50%` | slider arrow figure, availability dot |

> Patagonia는 button은 pill, card는 soft-rect, overlay는 medium-round로 분리한다. 하나의 radius 값으로 전부 통일하지 않는다.

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| `--bs-box-shadow-sm` | `0 .125rem .25rem #00000013` | 시스템 미세 elevation |
| `--bs-box-shadow` | `0 .5rem 1rem #00000026` | bootstrap 기본 elevation |
| `nav / slider figure` | `0 4px 5px #00000024, 0 1px 10px #0000001f, 0 2px 4px -1px #0003` | sticky nav, slider arrow, active press state |
| `popover` | `0 3rem 6rem #0000004d` | large floating helper surface |
| `dark slider figure` | `0 4px 5px #99999924, 0 1px 10px #9999991f, 0 2px 4px -1px #9993` | dark themed slider arrow |

---

## 10. Motion
<!-- SOURCE: auto -->

| Pattern | Value | Use |
|---|---|---|
| `button hover` | `transform .2s cubic-bezier(.235,0,.05,.95)` | hover scale `1.044` |
| `button active shadow` | `0 4px 5px #00000024, 0 1px 10px #0000001f, 0 2px 4px -1px #0003` | press feedback |
| `hero content reveal` | `opacity .6s cubic-bezier(.38,.41,.27,1) .4s`, `transform .6s ... .4s` | hero load-in |
| `hero overlay` | `opacity .4s cubic-bezier(.38,.41,.27,1)` | on-image dimming / overlay info |
| `card tile` | `transform .3s cubic-bezier(.38,.41,.27,1)` | tile hover movement |
| `product image swap` | `transform .75s cubic-bezier(.38,.41,.27,1), opacity .75s ...` | product hover swap |
| `slider nav hover` | `transform .2s cubic-bezier(.235,0,.05,.95)` | hover scale `1.05` |

> `prefers-reduced-motion` 분기가 넓게 들어가 있어서, motion이 있어도 강제로 몰아붙이지 않는다.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Primary Navigation

- `primary-navigation` background는 `var(--pat-theme-back)` (`#FFF` 또는 `#000`)
- padding: mobile `0.8rem 0`, desktop `2.4rem 0`, sticky pinned `1.2rem 0`
- `primary-navigation__container`: `grid-template-columns: 1fr 2fr 1fr`, gap `0.8rem`
- logo width: `12rem` (min `10.8rem`, max `12rem`)

### Hero Main v2

- base hero: CSS grid + positioned overlay
- split hero: `50% / 50%` at `992px+`, `40% / 60%` or `60% / 40%` at `1200px+`
- content max width: `40em` at `768px+`
- on-image vertical padding: mobile `5.6rem`, tablet+ `8rem`
- default overlay dim: `opacity: .4` for `hero-main--on-image`
- overlay info card max-width: `34.3rem`, border-radius `1.6rem`

### Card Tile

```css
.card-tile .card__inner {
  border-radius: 8px;
  padding-top: 120.482%;
  background-color: #F5F5F5;
  transition: transform .3s cubic-bezier(.38,.41,.27,1);
}

.card-tile .card__content {
  padding: 3rem 3.2rem 2rem;
}
```

- content wrapper height: `67%`
- image wrap padding-top: `58.2524%`
- dark theme tile surface: `#121212`

### Slider / Page Designer

- container padding: `4rem var(--bs-gutter-x)` base
- `768px+`: left/right `calc(var(--bs-gutter-x) * 4)` = `6.4rem`
- `992px+`: left/right `calc(var(--bs-gutter-x) * 5)` = `8rem`
- nav figure size: mobile `3.2rem`, tablet+ `6rem`

---

## 12. Responsive Behavior
<!-- SOURCE: auto -->

| Breakpoint | Value | Behavior |
|---|---|---|
| `sm` | `576px` | bootstrap grid entry |
| `md` | `768px` | nav padding increase, hero content max-width 활성화, slider nav `6rem` |
| `lg` | `992px` | split hero, larger body copy, slider container `8rem`, vertical product tile ratio |
| `xl` | `1200px` | bootstrap type scale cap, hero split `40/60` or `60/40` |
| `xxl` | `1400px` | wide grid continuation |
| `xxxl` | `1600px` | extra-wide spacing utility tier |
| `xxxxl` | `1800px` | max utility expansion tier |

**패턴 요약**:

- typography는 `992px` 또는 `1200px`에서 확정값으로 올라간다.
- layout은 `768px`에서 breathing room, `992px`에서 구조 분할, `1200px`에서 hero ratio fine-tune이라는 3단계다.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Primary Button (`.btn-dark`, `.btn-light`, `.btn-orange`)

```html
<button class="btn btn-dark">Shop Men’s</button>
<button class="btn btn-light">Read Stories</button>
<button class="btn btn-orange">Sale</button>
```

| Spec | Value |
|---|---|
| padding | `0.9rem 2.8rem` |
| font-size | `calc(1.285rem + .2625vw) -> 1.6rem` |
| font-weight | `500` |
| line-height | `1.2` |
| border-radius | `3rem` |
| dark bg | `#000` |
| light bg | `#FFF` |
| orange bg | `#FA4616` |
| hover | scale `1.044`, dark hover `#262626`, light hover `#D9D9D9 / #CCC` |

### Primary Navigation (`.primary-navigation`)

```html
<nav class="primary-navigation">
  <div class="primary-navigation__container">
    <a class="primary-navigation__logo">Patagonia</a>
  </div>
</nav>
```

| Spec | Value |
|---|---|
| grid | `1fr 2fr 1fr` |
| gap | `0.8rem` |
| padding | `0.8rem` mobile / `2.4rem` desktop / `1.2rem` pinned |
| shadow when pinned | `0 4px 5px #00000024, 0 1px 10px #0000001f, 0 2px 4px -1px #0003` |
| logo width | `12rem` |

### Card Tile (`.card-tile`)

```html
<article class="card-tile">
  <div class="card__inner">
    <div class="card__content">...</div>
  </div>
</article>
```

| Spec | Value |
|---|---|
| surface | `#F5F5F5` light / `#121212` dark |
| border-radius | `8px` |
| ratio | `padding-top: 120.482%` |
| content padding | `3rem 3.2rem 2rem` |
| content wrapper height | `67%` |
| transition | `transform .3s cubic-bezier(.38,.41,.27,1)` |
| serif title | `Copernicus`, `500`, `-0.05em`, `1.1` |

### Product Tile (`.product-tile-simple`)

```html
<div class="product-tile-simple">
  <div class="product-tile-simple__image"></div>
  <div class="sales"><span class="value">$179</span></div>
</div>
```

| Spec | Value |
|---|---|
| image size | `9.6rem × 9.6rem` |
| vertical desktop ratio | `315 / 380` |
| hover image swap | `.75s cubic-bezier(.38,.41,.27,1)` |
| sale value color | `#FA4616` |

### Hero Overlay Info (`.hero-main__overlay-info-content`)

| Spec | Value |
|---|---|
| border-radius | `1.6rem` |
| width | `calc(100% - 1.6rem)` mobile / `max-width: 34.3rem` tablet+ |
| padding | `1.6rem 2.4rem 1.6rem 1.6rem` |
| background | `var(--pat-theme-cta-fore)` (`#FFF` or `#000`) |
| motion | scale from `.1` to `1`, opacity staged reveal |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Patagonia 2026-04-23 live CSS distilled */
:root {
  --pata-font-sans: "Ridgeway Sans", system-ui, -apple-system, "Segoe UI",
    Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans",
    sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol", "Noto Color Emoji";
  --pata-font-serif: "Copernicus", "Palatino Linotype", Palatino, Palladio,
    "URW Palladio L", "Book Antiqua", Baskerville, "Bookman Old Style",
    "Bitstream Charter", "Nimbus Roman No9 L", Garamond, "Apple Garamond",
    "ITC Garamond Narrow", "New Century Schoolbook", "Century Schoolbook",
    "Century Schoolbook L", Georgia, serif;

  --pata-bg: #fff;
  --pata-fg: #000;
  --pata-surface: #f5f5f5;
  --pata-surface-dark: #121212;
  --pata-meta: #4a4a4a;
  --pata-brand: #FA4616;
  --pata-campfire: #F47B29;
  --pata-warning: #FEB904;
  --pata-success: #32B67A;
  --pata-steppe: #61845B;
  --pata-industrial: #485643;
  --pata-info: #91ABE9;

  --pata-radius-card: 8px;
  --pata-radius-panel: 12px;
  --pata-radius-pill: 3rem;
  --pata-shadow-elevated:
    0 4px 5px #00000024,
    0 1px 10px #0000001f,
    0 2px 4px -1px #0003;
  --pata-ease: cubic-bezier(.38, .41, .27, 1);
  --pata-ease-hover: cubic-bezier(.235, 0, .05, .95);
}

body {
  font-family: var(--pata-font-sans);
  font-size: 1rem;
  font-weight: 300;
  line-height: 1.5;
  color: var(--pata-fg);
  background: var(--pata-bg);
}

.pata-shell {
  background: var(--pata-bg);
  color: var(--pata-fg);
}

.pata-shell.is-dark {
  background: #000;
  color: #fff;
}

.pata-nav {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: .8rem;
  padding: .8rem 1.6rem;
}

@media (min-width: 768px) {
  .pata-nav {
    padding-top: 2.4rem;
    padding-bottom: 2.4rem;
  }
}

.pata-hero {
  padding: 5.6rem 1.6rem;
  position: relative;
}

@media (min-width: 992px) {
  .pata-hero {
    padding-top: 8rem;
    padding-bottom: 8rem;
  }
}

.pata-hero h1 {
  margin: 0 0 .8rem;
  font-size: 4rem;
  font-weight: 500;
  line-height: 1.1;
  letter-spacing: -.02em;
}

@media (min-width: 992px) {
  .pata-hero h1 {
    font-size: 6.4rem;
  }
}

.pata-hero .serif {
  font-family: var(--pata-font-serif);
  letter-spacing: -.05em;
}

.pata-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 0;
  padding: .9rem 2.8rem;
  border: 0;
  border-radius: var(--pata-radius-pill);
  font-size: calc(1.285rem + .2625vw);
  font-weight: 500;
  line-height: 1.2;
  transition: transform .2s var(--pata-ease-hover),
    opacity .2s var(--pata-ease-hover);
}

.pata-btn:hover {
  transform: scale(1.044);
}

.pata-btn.is-dark {
  background: #000;
  color: #fff;
}

.pata-btn.is-light {
  background: #fff;
  color: #000;
}

.pata-card {
  border-radius: var(--pata-radius-card);
  background: var(--pata-surface);
  overflow: hidden;
  transition: transform .3s var(--pata-ease);
}

.pata-card.is-dark {
  background: var(--pata-surface-dark);
  color: #fff;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### 이 디자인을 재현할 때 에이전트에게 줄 지시

- `Ridgeway Sans`를 body/UI 기본체로, `Copernicus`를 display/serif accent로만 사용하라.
- body는 `font-weight: 300`, hero/headline/button은 `500`, 과한 bold는 `strong` 한정으로만 쓰라.
- 기본 페이지 톤은 `#000` / `#FFF` / `#F5F5F5` / `#121212` 네 축으로 잡아라.
- accent는 소량만 써라: `#FA4616`, `#F47B29`, `#FEB904`, `#32B67A`, `#61845B`, `#485643`.
- 버튼은 `3rem` pill radius, 카드는 `8px`, hero overlays는 `1.6rem`로 분리하라.
- hero는 `50/50` 또는 `40/60` split, content max-width `40em`, on-image overlay opacity `.4`를 기준으로 잡아라.
- motion은 `.2s` hover / `.3s ~ .6s` reveal / `.75s` image swap 정도로만 제한하라.
- `Avenir Next W02 Light`를 현재 Patagonia 홈 기준 폰트라고 가정하지 말 것.

### 바로 붙여 넣는 프롬프트

```text
Build a Patagonia-like marketing surface using a black/white-first outdoor utility system.
Use Ridgeway Sans 300 for all body/UI text and Copernicus 500 only for editorial display or serif accents.
Anchor the palette in #000, #FFF, #F5F5F5, and #121212, then add very small accents from #FA4616, #F47B29, #FEB904, #32B67A, #61845B, and #485643.
Buttons must be pill-shaped with 3rem radius, cards 8px, hero overlays 1.6rem.
Use split hero compositions (50/50 or 40/60), 0.8rem spacing rhythm, and tactile motion with .2s hover and .3s-.6s panel transitions.
Do not use Avenir as the main font unless reproducing Patagonia's old failover page.
```

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO

- 배경/전경 기본쌍은 `#FFF` + `#000`으로 잡고, neutral surface는 `#F5F5F5`를 우선 사용한다.
- dark insert는 `#121212`를 쓰고, pure black `#000`는 CTA·nav·dark wrapper에 집중시킨다.
- accent는 의미가 있을 때만 쓴다: `#FA4616`(brand/sale), `#FEB904`(warning), `#32B67A`(success), `#61845B` / `#485643`(earth-tone campaign).
- body는 `Ridgeway Sans` 300, serif title/snippet은 `Copernicus` 500과 `-0.03em ~ -0.05em` tracking을 유지한다.
- 버튼은 `border-radius: 3rem`, 카드는 `8px`, overlay panel은 `1.6rem`로 계층별 radius를 분리한다.

### DON'T

- 페이지 배경을 `#32B67A`, `#61845B`, `#485643`로 두지 말 것 — 기본 페이지는 `#FFF`, dark section만 `#000` 또는 `#121212`를 쓴다.
- primary CTA를 `#32B67A`나 `#FEB904`로 두지 말 것 — 기본 CTA는 `#000` 또는 `#FFF`, 강한 브랜드 포인트가 필요할 때만 `#FA4616`을 쓴다.
- 본문 텍스트를 `#4A4A4A`로 통일하지 말 것 — body는 `#000`, `#4A4A4A`는 meta/secondary copy에만 둔다.
- body에 `font-weight: 400`을 기본값으로 두지 말 것 — 현재 live body는 `300`이 맞다.
- body에 `font-family: "Avenir Next W02 Light"`를 쓰지 말 것 — 2026-04-23 live HTML/CSS 기준 메인 폰트는 `Ridgeway Sans`다.
- 버튼과 카드에 모두 `border-radius: 0`을 적용하지 말 것 — 현재 Patagonia UI는 pill CTA `3rem` + card `8px` 조합이다.
