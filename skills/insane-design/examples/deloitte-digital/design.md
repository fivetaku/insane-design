---
schema_version: 3.1
slug: deloitte-digital
service_name: Deloitte Digital
site_url: https://www.deloittedigital.com
fetched_at: 2026-04-23
default_theme: mixed
brand_color: "#86BC25"
primary_font: Open Sans
font_weight_normal: 300
token_prefix: "--tw-* + .cmp-* / .dd-*"

bold_direction: "Industrial Minimalism"
aesthetic_category: "Industrial Minimalism"
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
---

# DESIGN.md — Deloitte Digital (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: auto+manual -->

Deloitte Digital의 현재 AEM 홈페이지는 겉으로 보면 흑백 컨설팅 사이트처럼 보이지만, 실제 CSS를 열어보면 구조가 더 복합적이다. `#000000`과 `#FFFFFF`가 가장 많이 등장하고, 그 사이를 `#D0D0CE` 경계선과 `#F3F3F3` / `#F6F6F6` 표면이 메운다. 그 위에 Deloitte green `#86BC25`가 hover/active 상태를 담당하고, dark gray `#53565A` / `#75787B`가 탭·비활성 상태·보조 텍스트를 지배한다.

히어로는 정적인 컨설팅 배너가 아니라 **100vh marquee carousel**이다. `.dd-marquee-carousel`은 모바일에서 `630px`, 데스크톱에서 `100vh`를 차지하고, white headline + black overlay + video/image background를 조합한다. 여기에 `#A0DCFF`, `#9DD4CF`, `#E3E48D`, `#007680` 같은 campaign color가 CTA와 mosaic tile에서 튀어나오면서, 전형적인 corporate mono에서 한 단계 벗어난다.

타이포그래피는 전면적으로 `Open Sans`를 쓴다. 실제 CSS에는 `@font-face`로 `300 / 400 / 500 / 600 / 700 / 800`의 normal/italic이 모두 로드된다. 하지만 UI 인상은 `.font-light`(`300`)가 만든다. marquee title은 `desktop:text-desktop-h2`의 `80px / 94px`, mobile에서는 `text-mobile-h1-regular`의 `36px / 46px`로 떨어지고, eyebrow/CTA는 `.tracking-letter-2`(`0.12em`)와 `.tracking-letter-1`(`0.2em`)로 강한 uppercase 리듬을 만든다.

레이아웃은 Adobe Experience Manager의 `.aem-Grid--default--12`와 `.cmp-*` 컴포넌트 계층 위에 Tailwind-style utility가 얹힌 구조다. 그래서 표면상 semantic component site처럼 보이지만, 실제 구현은 `desktop:text-desktop-h2`, `font-light`, `transition`, `duration-200` 같은 utility 조합으로 미세 조정을 한다. 버튼은 `border-radius:9999px` pill, mosaic tile은 `0.4s ease-out` gradient shift, sticky nav는 다층 shadow를 써서 "딱딱한 enterprise"보다 조금 더 dynamic한 agency tone을 만든다.

### Key Characteristics

- `#000000` / `#FFFFFF` / `#D0D0CE`가 기본 구조를 만드는 mixed monochrome
- Deloitte green `#86BC25`는 active tab, CTA hover, icon hover에만 집중 배치
- dark gray `#53565A` / `#75787B`가 state 컬러로 분명하게 분리됨
- `Open Sans` + `font-light(300)` 중심의 얇은 headline/body 인상
- `100vh` marquee hero + full-bleed image/video background
- `border-radius:9999px` uppercase CTA
- `#007680` / `#A0DCFF` / `#9DD4CF` / `#E3E48D` campaign surface가 black/white에 리듬 추가
- AEM semantic class와 Tailwind utility가 동시에 존재하는 하이브리드 구조

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Industrial Minimalism
> **Aesthetic Category**: Industrial Minimalism
> **Signature Element**: 이 사이트는 **100vh marquee hero와 Deloitte green hover state가 붙은 pill CTA**로 기억된다.
> **Code Complexity**: high — AEM component tree + utility layer + carousel/mosaic/state variants가 동시에 작동한다.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Deloitte Digital처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트와 무게 */
body {
  font-family: "Open Sans", Arial, sans-serif;
  font-weight: 300;
}

.eyebrow,
.cta {
  text-transform: uppercase;
  letter-spacing: 0.12em;
}
```

```css
/* 2. 실제 팔레트 */
:root {
  --dd-black:      #000000;
  --dd-white:      #FFFFFF;
  --dd-border:     #D0D0CE;
  --dd-green:      #86BC25;
  --dd-green-deep: #43B02A;
  --dd-gray-dark:  #53565A;
  --dd-gray-mid:   #75787B;
  --dd-teal:       #007680;
  --dd-sky:        #A0DCFF;
  --dd-aqua:       #9DD4CF;
  --dd-lime:       #E3E48D;
}
```

```css
/* 3. 히어로와 CTA */
.dd-marquee {
  height: 630px;
}

.dd-cta {
  display: flex;
  width: fit-content;
  align-items: center;
  gap: 8px;
  border: 2px solid #000000;
  border-radius: 9999px;
  padding: 13px 26px;
  background: #ffffff;
  color: #000000;
  font-size: 10px;
  line-height: 12px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.dd-cta:hover {
  border-color: #86BC25;
  color: #86BC25;
}

@media (min-width: 1024px) {
  .dd-marquee { height: 100vh; }
  .dd-cta {
    padding: 18px 60px;
    font-size: 14px;
    line-height: 24px;
    letter-spacing: 0.2em;
  }
}
```

**절대 하지 말아야 할 것 하나**: Deloitte Digital을 순수 흑백 corporate site로 단순화하지 마라. 실제 CSS는 black/white 뼈대 위에 `#86BC25` hover, `#53565A` state tab, `#007680` / `#A0DCFF` / `#E3E48D` campaign surface를 반드시 남겨 둔다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.deloittedigital.com` |
| Final HTML | `https://www.deloittedigital.com/kr/en.html` |
| Fetched | `2026-04-23` |
| Extractor | `curl_cffi.requests.Session(impersonate="chrome")` + homepage DOM/CSS direct parse |
| HTML size | `210,023 bytes` |
| CSS files | `clientlib-critical` (`193,475 bytes`), `clientlib-dynamic-fetcher` (`900,632 bytes`), `static-fixes-dd.css` (`21 bytes`) |
| CSS URLs | `/etc.clientlibs/digital/clientlibs/clientlib-template/clientlib-critical.lc-eb83c615ab1de7d97084dbab73db7bc6-lc.min.css`, `/etc.clientlibs/digital/clientlibs/clientlib-template/clientlib-dynamic-fetcher.lc-673398a92ec223f8ddeae3d91f2d4585-lc.min.css` |
| Token prefix | runtime utility는 `--tw-*`, explicit site prop는 `--swiper-theme-color`; 구조는 `.cmp-*` / `.dd-*` semantic class 중심 |
| Method | 실제 CSS 선언, `@font-face`, DOM class 조합만 사용 · 추측 배제 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Adobe Experience Manager (AEM) — `etc.clientlibs`, `.aem-Grid--default--12`, `.cmp-*` 계층으로 확인
- **Design system shape**: semantic component (`.cmp-*`, `.dd-*`) + Tailwind-style utility (`.font-light`, `.desktop:text-desktop-h2`, `.transition`) 하이브리드
- **Carousel / interaction**: `Swiper` (`.swiper`, `.swiper-slide`, `--swiper-theme-color`)
- **CSS architecture**: large minified bundle + component variants (`cmp-tabs`, `cmp-modal`, `cmp-mosaic-grid`, `dd-button`)
- **Default theme**: mixed — black/video hero + white/light-gray body + teal/sky/lime campaign panels
- **Font loading**: self-hosted `@font-face` Open Sans 300–800 normal/italic, `font-display: swap`
- **Canonical anchor**: `#86BC25` active/hover green
- **State neutrals**: `#53565A` dark gray active panel, `#75787B` disabled/secondary, `#D0D0CE` border rail

---

## 04. Font Stack
<!-- SOURCE: auto -->

- **Body / UI / display**: `"Open Sans", Arial, sans-serif`
- **Icon font**: `"icon"`
- **Weight normal / bold**: `300` / `700`
- **Loaded weights**: `300 / 400 / 500 / 600 / 700 / 800` (normal + italic 전부 로드)
- **Loading behavior**: `font-display: swap`
- **Fallback**: `Arial, sans-serif`

```css
body {
  font-family: "Open Sans", Arial, sans-serif;
  font-weight: 300;
}

.font-light  { font-weight: 300; }
.font-normal { font-weight: 400; }
.font-extrabold { font-weight: 800; }
```

> **라이선스 주의**: Open Sans는 오픈 라이선스 폰트지만, 실제 사이트는 self-hosted `woff2` 세트를 직접 서빙한다.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> Deloitte Digital의 타입 시스템은 utility 조합형이다. 크기 class와 weight class를 분리해서 조합하며, marquee/eyebrow/CTA에서 tracking이 강하게 들어간다.

| Token / usage | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `desktop:text-desktop-h1` | `116px` | `300` with `.font-light` | `126px` | `0` |
| `desktop:text-desktop-h2` | `80px` | `300` with `.font-light` | `94px` | `0` |
| `desktop:text-desktop-h3` | `56px` | `300` with `.font-light` | `70px` | `0` |
| `desktop:text-desktop-h4` | `40px` | `300` with `.font-light` | `50px` | `0` |
| `desktop:text-desktop-h5` | `24px` | `300` or `600` by context | `36px` | `0` |
| `text-mobile-h1-regular` | `36px` | `300` | `46px` | `0` |
| `text-mobile-h2` | `26px` | context-dependent | `34px` | `0` |
| `text-mobile-h3` | `18px` | context-dependent | `28px` | `0` |
| `text-mobile-h4` | `16px` | context-dependent | `26px` | `0` |
| `cmp-text__regular` | `14px` mobile / `18px` desktop | `300` or `400` | `24px` mobile / `30px` desktop | `0` |
| `cmp-text__regular-tight` | `14px` mobile / `18px` desktop | `300` or `400` | `20px` mobile / `26px` desktop | `0` |
| `text-mobile-body-2-regular` | `12px` | `300` or `400` | `22px` | `0` |
| `tracking-letter-2` | N/A | N/A | N/A | `.12em` |
| `tracking-letter-1` | N/A | N/A | N/A | `.2em` |

### Live DOM example

```html
<h2 class="cmp-title text-white desktop:text-desktop-h2 mobile:text-mobile-h1 font-light main_text_padding">
  5 questions to ask before integrating Gen AI into your marketing strategy
</h2>
```

이 조합이 Deloitte Digital 히어로의 실제 시각 언어다. headline size는 utility가, 얇은 인상은 `.font-light`가 만든다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Core Neutrals

| Token | Hex | Usage |
|---|---|---|
| `black` ★ | `#000000` | hero overlay, text, outlines, tabs icon bg |
| `white` | `#FFFFFF` | button fill, body sections, text on dark |
| `grey-10` | `#D0D0CE` | border rail, tab hover line, separators |
| `grey-12 utility` | `#F7F7F7` | light surface utility (`rgb(247 247 247)` in CSS rule) |
| `light surface` | `#F3F3F3` | text block background |
| `lightest grey` | `#F6F6F6` | page/surface utility |

### 06-2. Deloitte Green + State Grays

| Token | Hex | Usage |
|---|---|---|
| `green active` ★ | `#86BC25` | active tab background, CTA hover border/text, icon hover |
| `green border` | `#43B02A` | vertical tab active left rail |
| `green hover fill` | `#EBF4DC` | inactive tab hover fill |
| `dark gray active` | `#53565A` | grey tab active background, metadata text |
| `mid gray disabled` | `#75787B` | disabled secondary button text/icon |

### 06-3. Campaign Surface Palette

| Token | Hex | Usage |
|---|---|---|
| `teal core` | `#007680` | teal mosaic tile base |
| `teal bright` | `#0097A9` | teal gradient start |
| `teal alt` | `#0D8390` | active teal tab |
| `aqua` | `#9DD4CF` | aqua primary CTA fill |
| `sky` | `#A0DCFF` | CTA hover / gradient transition |
| `lime` | `#E3E48D` | green-1 campaign surface |
| `blue` | `#0076A8` | blue tile gradient start |
| `blue deep` | `#005587` | blue tile base |
| `blue deeper` | `#005E86` | blue gradient end |

### 06-4. Utility Rules Confirmed in CSS

```css
.bg-teal-6   { background-color: rgb(0 118 128 / var(--tw-bg-opacity)); }
.text-grey-10{ color: rgb(208 208 206 / var(--tw-text-opacity)); }
.text-grey-11{ color: rgb(89 89 89 / var(--tw-text-opacity)); }
.text-grey-16{ color: rgb(142 142 142 / var(--tw-text-opacity)); }
.border-grey-10 { border-color: rgb(208 208 206 / var(--tw-border-opacity)); }
```

### 06-5. Dominant Colors (normalized CSS frequency)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#000000` | `442` | primary text, hero, outlines |
| 2 | `#FFFFFF` | `352` | section and CTA fills |
| 3 | `#D0D0CE` | `268` | borders, rails, muted UI |
| 4 | `#A0DCFF` | `28` | hover / gradient accent |
| 5 | `#86BC25` | `28` | Deloitte green interaction state |
| 6 | `#F3F3F3` | `23` | neutral surface |
| 7 | `#007680` | `22` | teal campaign tile |
| 8 | `#F6F6F6` | `21` | page/background surface |
| 9 | `#E3E48D` | `19` | lime campaign surface |
| 10 | `#9DD4CF` | `18` | aqua CTA fill |

---

## 07. Spacing
<!-- SOURCE: auto -->

> Deloitte Digital은 generic 4px scale보다 "컴포넌트별 고정 값"이 더 중요하다. 특히 hero, pill CTA, text block, modal spacing이 반복된다.

| Selector / token | Value | Use case |
|---|---|---|
| `.dd-button` | `padding: 10px 16px` | base pill CTA |
| `.dd-button.button-white-bg` / `.on-white-secondary-template` | `13px 26px` mobile | white secondary CTA |
| same desktop | `18px 60px` | marquee/section CTA |
| `.dd-button` | `gap: 8px` | icon + label spacing |
| `.text-v2-homepage-default` | `padding-top: 8px; padding-bottom: 64px` mobile | homepage text block rhythm |
| same desktop | `padding-top: 16px; padding-bottom: 32px` | desktop text block rhythm |
| `.main_text_padding` | `margin-top: 24px; margin-bottom: 24px` mobile | hero title breathing room |
| same desktop | `margin-top: 40px; margin-bottom: 40px` | hero title breathing room |
| `.dd-marquee-carousel .swiper-container` | `bottom: 40px; right: 24px` mobile | hero controls |
| same desktop | `bottom: 50px; padding-left: 8.33333333%` | hero controls aligned to content grid |
| `.cmp-modal__content.modal-content` | `padding: 32px` | modal inner spacing |

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `pill` | `9999px` | `.dd-button` base CTA |
| `circle` | `50%` | `.button-circle` icon button |
| `panel` | `8px` | `.cmp-modal__content.modal-content` |
| `hard edge` | `0` | many tabs, text panels, rails remain square |

```css
.dd-button {
  border-radius: 9999px;
}

.button-circle button,
.button-circle .button-container {
  border-radius: 50%;
}
```

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| `nav` | `0 100px 80px #00000012, 0 41.7776px 33.4221px #0000000d, 0 22.3363px 17.869px #0000000b, 0 12.5216px 10.0172px #00000009, 0 6.6501px 5.32008px #00000007, 0 2.76726px 2.21381px #00000005` | `.cmp-navbar.nav-container.nav-shadowed` |
| `modal` | `0 3px 16px #00000029` | `.cmp-modal__content.modal-content` |
| `sticky in-page nav` | `0 2px 8px #00000014` | `.dd-in-page-navigation` |
| `floating mobile CTA` | `0 3px 6px #00000029` | `.cmp-btn--clone--full-width .button-container` |

---

## 10. Motion
<!-- SOURCE: auto -->

| Primitive | Value | Context |
|---|---|---|
| utility transition | `.15s cubic-bezier(.4,0,.2,1)` | `.transition` |
| header shift | `.2s` | `.duration-200` in sticky header |
| mosaic hover | `.4s ease-out` | `.cmp-mosaic-grid__panel.with-animation` |
| gradient slide | `background-position: top -> bottom` | mosaic tile hover at `min-width:1201px` |

```css
.transition {
  transition-property: color, background-color, border-color, text-decoration-color,
    fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter;
  transition-timing-function: cubic-bezier(.4, 0, .2, 1);
  transition-duration: .15s;
}

.cmp-mosaic-grid__cell .cmp-mosaic-grid__panel.with-animation {
  transition: .4s ease-out;
}
```

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Marquee Hero

- `.dd-marquee-carousel` — `height:630px` mobile, `height:100vh` desktop
- white headline over video/image background
- control cluster pinned bottom-right on mobile, grid-aligned left on desktop
- hero title uses `desktop:text-desktop-h2` + `font-light`

### AEM 12-column Shell

- HTML class에서 `.aem-Grid--default--12` 확인
- semantic component block들이 grid child로 배치됨
- utility class가 inner text/spacing/typography를 덮어쓴다

### Text Module Rhythm

- `.text-v2-homepage-default`가 홈 본문 리듬을 결정
- mobile: `pt 8 / pb 64`
- desktop: `pt 16 / pb 32`
- `.cmp-text__regular`와 `font-weight__light` 조합이 기본 본문 톤

### Mosaic Grid

- 기본 panel은 black 또는 brand color surface
- desktop `min-width:1201px`에서 gradient + hover slide 활성화
- teal tile은 `#0097A9 -> #007680`, blue tile은 `#0076A8 -> #005E86`

---

## 12. Responsive
<!-- SOURCE: auto -->

| Breakpoint | Role |
|---|---|
| `max-width:767px` | mobile-specific type/layout overrides |
| `min-width:768px` | tablet typography variants 시작 |
| `min-width:1024px` | desktop hero, larger type scale, CTA expansion |
| `min-width:1201px` | mosaic hover animation / gradient slide 활성화 |
| `min-width:1400px` | large display typography / extended spacing |

---

## 13. Components
<!-- SOURCE: auto+manual -->

### White Secondary CTA

```css
.dd-button.on-white-secondary-template {
  border-width: 2px;
  border-color: #000000;
  background-color: #FFFFFF;
  color: #000000;
  padding: 13px 26px;
  font-size: 10px;
  line-height: 12px;
  font-weight: 600;
  letter-spacing: .12em;
  border-radius: 9999px;
}

.dd-button.on-white-secondary-template:hover,
.dd-button.on-white-secondary-template:focus,
.dd-button.on-white-secondary-template:active {
  border-color: #86BC25;
  color: #86BC25;
}
```

### Aqua Primary CTA

```css
.dd-button.on-black-primary-template {
  column-gap: 8px;
  background-color: #9DD4CF;
  font-size: 16px;
  line-height: 26px;
}

.dd-button.on-black-primary-template:hover {
  background-color: #A0DCFF;
}

.dd-button.on-black-primary-template:active {
  background-color: #80CDFA;
}
```

### Tabs

```css
.cmp-tabs-v2__active--green .cmp-tabs__tab--active {
  background: #86BC25;
  color: #000000;
}

.cmp-tabs-v2__active--grey .cmp-tabs__tab--active {
  background: #53565A;
  color: #FFFFFF;
}

.cmp-tabs-v2__vertical-slidedown .cmp-tabs__tab--active:before {
  border-inline-start: 4px solid #43B02A;
}
```

### Teal Mosaic Tile

```css
.cmp-mosaic-grid__cell--text-tile.cmp-mosaic-grid__cell--teal .cmp-mosaic-grid__panel {
  background: #007680;
}

@media screen and (min-width:1201px) {
  .cmp-mosaic-grid__cell--text-tile.cmp-mosaic-grid__cell--teal .cmp-mosaic-grid__panel {
    background: linear-gradient(180deg, #0097A9 0%, #007680 50%);
    background-size: 1px 200%;
    background-position: top;
  }
}
```

---

## 15. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  --dd-black: #000000;
  --dd-white: #FFFFFF;
  --dd-border: #D0D0CE;
  --dd-green: #86BC25;
  --dd-green-deep: #43B02A;
  --dd-gray-dark: #53565A;
  --dd-gray-mid: #75787B;
  --dd-teal: #007680;
  --dd-sky: #A0DCFF;
  --dd-aqua: #9DD4CF;
  --dd-lime: #E3E48D;
  --dd-font: "Open Sans", Arial, sans-serif;
}

body {
  margin: 0;
  font-family: var(--dd-font);
  font-weight: 300;
  color: var(--dd-black);
  background: var(--dd-white);
}

.dd-marquee {
  min-height: 630px;
  background: var(--dd-black);
  color: var(--dd-white);
}

.dd-kicker {
  font-size: 14px;
  line-height: 24px;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.dd-title {
  font-size: 36px;
  line-height: 46px;
  font-weight: 300;
}

.dd-cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 2px solid var(--dd-black);
  border-radius: 9999px;
  padding: 13px 26px;
  background: var(--dd-white);
  color: var(--dd-black);
  font-size: 10px;
  line-height: 12px;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.dd-cta:hover {
  border-color: var(--dd-green);
  color: var(--dd-green);
}

@media (min-width: 1024px) {
  .dd-marquee { min-height: 100vh; }
  .dd-title {
    font-size: 80px;
    line-height: 94px;
  }
  .dd-cta {
    padding: 18px 60px;
    font-size: 14px;
    line-height: 24px;
    letter-spacing: .2em;
  }
}
```

---

## 16. Tailwind / Utility Mapping
<!-- SOURCE: auto -->

```html
<section class="dd-marquee-carousel">
  <p class="cmp-title uppercase tracking-letter-2 text-white text-mobile-body-1-regular font-light">
    DIGITAL TRANSFORMATION
  </p>
  <h2 class="cmp-title text-white desktop:text-desktop-h2 mobile:text-mobile-h1 font-light main_text_padding">
    How we helped Maserati drive a new customer experience
  </h2>
  <button class="dd-button z-40 uppercase m-0 on-white-secondary-template">
    READ MORE
  </button>
</section>
```

### Useful utility translations

- `font-light` — `font-weight:300`
- `desktop:text-desktop-h2` — `80px / 94px`
- `mobile:text-mobile-h1` — `36px / 46px`
- `tracking-letter-2` — `.12em`
- `tracking-letter-1` — `.2em`
- `transition duration-200` — `.15s base transition + .2s duration override`

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO

- `Open Sans`를 유지하고 headline/body에 `300` weight를 적극 사용하라
- CTA는 `9999px` pill + uppercase tracking + `8px` icon gap으로 만든다
- black/white base 위에 `#86BC25` hover와 `#53565A` / `#75787B` state gray를 분리해 쓴다
- campaign section에서는 `#007680`, `#9DD4CF`, `#A0DCFF`, `#E3E48D`를 과감하게 섞는다
- desktop hero는 `100vh`, mobile hero는 `630px` 비율감을 유지한다

### DON'T

- Deloitte Digital을 pure monochrome 흑백 사이트로 축소하지 마라
- body/headline을 기본 `400`~`600` 위주로 올려서 무게를 두껍게 만들지 마라
- CTA를 사각형 버튼으로 바꾸지 마라
- teal/sky/lime campaign surface를 제거하고 모든 섹션을 같은 흰 박스로 만들지 마라
- tab state를 green/gray 대신 같은 neutral hover로 통일하지 마라
