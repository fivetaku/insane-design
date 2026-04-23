---
schema_version: 3.1
slug: volvo
service_name: Volvo Cars
site_url: https://www.volvocars.com/kr/
fetched_at: 2026-04-23
default_theme: light
brand_color: "#0B2DED"
primary_font: Volvo Centum
font_weight_normal: 400
token_prefix: "--v-*, ot-* selectors"

bold_direction: "Scandinavian Utility"
aesthetic_category: "Industrial Minimalism"
signature_element: accent_blue_state
code_complexity: high

medium: web
medium_confidence: high
---

# DESIGN.md — Volvo Cars (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: auto+manual -->

2026-04-23 기준 `https://www.volvocars.com/kr/` 홈은 루트 `<html>`에 `data-theme="centenary"`를 선언하고, 실제 렌더링 토큰도 이 테마 오버라이드에 맞춰 재정의한다. 이 오버라이드는 페이지를 **순백 `#FFFFFF` / 순흑 `#000000` / 전기 블루 `#0B2DED`** 축으로 다시 묶는다. 배경은 거의 전부 흰색이고, 큰 CTA·현재 탭·선택 상태만 검정 또는 블루가 잡는다. 색을 많이 쓰는 대신 상태값을 강하게 쓰는 방식이다.

폰트 계층은 이번 수집의 핵심이다. 공유 폰트 번들 `font-face.8324f4d8.css`에는 **`Volvo Novum`이 실제로 존재**하고, base token도 처음에는 `--v-font-sans-family: "Volvo Novum"...`로 시작한다. 하지만 현재 홈은 `data-theme="centenary"`에서 이 값을 `Volvo Centum`으로 덮어쓴다. 즉, **Volvo Novum은 shared pkg에 남아 있고, 현재 `/kr/` 홈의 active sans는 Volvo Centum**이다. display 계층도 동일하게 `Volvo Broad`에서 `Volvo Broad Pro`로 교체된다.

공간 체계는 느슨한 감성형이 아니라 정교한 시스템형이다. 모바일 기본 grid는 8열, `30rem` 이상부터 12열로 확장되고, 최대 콘텐츠 폭은 `81rem`, 페이지 쉘은 `160rem`까지 허용된다. 여백은 `.125rem` 단위 고정 계단(`--v-space-2`~`--v-space-64`)과 fluid clamp(`--v-space-xs`~`--v-space-2xl`)를 함께 쓴다. 그래서 카드 안쪽 패딩은 명확하게 딱딱 끊기고, 섹션 간 간격은 화면이 커질수록 자연스럽게 벌어진다.

인터랙션의 성격도 명확하다. 이 사이트는 카드 그림자를 크게 올리지 않는다. 대신 `border-ring`, selection ring, blur backdrop, gradient scrim, `0.22s ease` 전환으로 상태를 표현한다. hover와 selection에서 파란색이 드러나지만, 배경 전체가 파랗게 물드는 순간은 거의 없다. Volvo의 현재 UI는 "차분한 흑백 구조 위에 블루 상태 신호만 얹는 방식"으로 읽는 게 정확하다.

### Key Characteristics

- `data-theme="centenary"` active — white page, black neutral surfaces, blue accent state
- `Volvo Novum` confirmed in shared CSS, but current homepage sans = `Volvo Centum`
- `Volvo Broad` / `Volvo Broad Pro` display split
- `--v-*` token layer + utility classes + CSS Modules 3층 구조
- 8-column mobile -> 12-column from `30rem`
- blue is mostly current / selected / focus / info state, not large-area fill
- soft shadow보다 ring, border, blur, scrim에 의존

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Scandinavian Utility
> **Aesthetic Category**: Industrial Minimalism
> **Signature Element**: 이 사이트는 **순백 배경 위 검정 서피스와 전기 블루 상태색이 번쩍이는 selection/focus ring**으로 기억된다.
> **Code Complexity**: high — shared `--v-*` token layer, centenary theme override, utility atom, feature-level CSS Module이 동시에 존재한다.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Volvo Cars처럼 만들기 — 3가지만 하면 80%

```css
/* 1. active sans + weight */
[data-theme="centenary"] {
  --v-font-sans-family:
    "Volvo Centum", "Helvetica Neue", "Helvetica",
    "Noto Sans", "Segoe UI", "Arial", sans-serif;
  --v-font-regular-weight: 400;
  --v-font-emphasis-weight: 600;
}
body {
  font-family: var(--v-font-sans-family);
  font-weight: var(--v-font-regular-weight);
}

/* 2. white page + black text */
[data-theme="centenary"] {
  --v-color-background-primary: #fff;
  --v-color-background-secondary: #fafafa;
  --v-color-foreground-primary: #000;
  --v-color-foreground-secondary: #5e5e5e;
}

/* 3. blue only for state */
[data-theme="centenary"] {
  --v-color-foreground-accent-blue: #0B2DED;
  --v-color-surface-accent-blue: #0B2DED;
  --v-color-state-accent-blue-subtle: #0B2DED0A;
}
```

**절대 하지 말아야 할 것 하나**: shared pkg에 `Volvo Novum`이 있다고 해서 현재 홈 전체를 Novum 300 톤으로 밀지 마라. 실제 `/kr/` 홈의 active theme는 `Volvo Centum` + `400/600` 계층이고, 블루도 대면적 배경이 아니라 current / focus / selected 상태에서만 강하게 나온다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.volvocars.com/kr/` |
| Fetched | 2026-04-23 |
| Extractor | `curl_cffi` Chrome impersonation + 직접 CSS fetch |
| HTML size | `338,055` bytes (Next.js App Router SSR) |
| CSS files | 외부 `22`개 + 인라인 `7`개, 총 `362,468` chars |
| Token prefix | `--v-*` custom properties, `ot-*` / `#onetrust-*` consent selector namespace |
| Method | 실제 CSS / HTML 직접 파싱 · AI 추측값 없음 |

> 참고: 이전 산출물의 `--ot-*` 중심 해석과 달리, 현재 캡처에서는 커스텀 프로퍼티의 중심이 `--v-*`였고 OneTrust는 주로 selector namespace(`ot-*`)로 노출되었다.

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js App Router
  ```
  /static/homepage/_next/static/chunks/app/[siteSlug]/page-*.js
  /static/homepage/_next/static/css/*.css
  ```
- **Design system**: Volvo shared package v1 + centenary theme override
  ```
  token      (--v-color-foreground-primary)      raw design token
  utility    (.text-primary, .rounded-lg)        semantic / atomic alias
  component  (.SubNavigation_*, .PromotionHero_*) feature-level CSS Module
  ```
- **CSS architecture**: shared pkg (`/static/shared/pkg/css/v1/*`) + homepage chunks + site-navigation assets
- **Class naming**: utility atoms (`font-16`, `gap-24`, `border-ring-2`) + hashed CSS Modules (`SubNavigation_*`, `discovery-card_*`, `ChargingTool_*`)
- **Default theme**: light (`data-theme="centenary"` on `/kr/`)
- **Font loading**: self-hosted `@font-face` (`Volvo Novum`, `Volvo Broad`, `Volvo Centum`)
- **Canonical anchor**: active centenary blue `#0B2DED`; non-centenary shared blue `#1C6EBA` still ships in base tokens

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Active body/UI**: `Volvo Centum` — current centenary theme sans
- **Confirmed shared body**: `Volvo Novum` — base `--v-font-sans-family` and `font-face.8324f4d8.css`에 존재
- **Display**: `Volvo Broad`, `Volvo Broad Pro`
- **Code/System**: `monospace`
- **Weight normal / emphasis**: active theme `400 / 600`

```css
:root {
  --v-font-sans-family:
    "Volvo Novum", "Helvetica Neue", "Helvetica",
    "Noto Sans", "Segoe UI", "Arial", sans-serif;
  --v-font-broad-family: "Volvo Broad", "Arial Black", sans-serif;
  --v-font-regular-weight: 300;
  --v-font-emphasis-weight: 500;
}

[data-theme="centenary"] {
  --v-font-sans-family:
    "Volvo Centum", "Helvetica Neue", "Helvetica",
    "Noto Sans", "Segoe UI", "Arial", sans-serif;
  --v-font-broad-family: "Volvo Broad Pro", "Arial Black", sans-serif;
  --v-font-regular-weight: 400;
  --v-font-emphasis-weight: 600;
}
```

### Confirmed `@font-face` Families

| Family | Current capture | Notes |
|---|---|---|
| `Volvo Novum` | weights `300`, `500` + italic | shared sans family |
| `Volvo Broad` | weight `400` | shared display |
| `Volvo Centum` | weights `380`, `570` | centenary sans |

> 핵심은 "Volvo Novum이 사라진 게 아니라, centenary active theme가 Volvo Centum으로 덮어쓴다"는 점이다.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Notes |
|---|---|---|---|---|
| `--v-font-12` | `.75rem` | `400` | `1.667` | micro / caption |
| `--v-font-14` | `.875rem` | `400` | `1.572` | secondary body |
| `--v-font-16` | `1rem` | `400` | `1.5` | base body |
| `--v-font-20` | `1.25rem` | `400` | `1.4` | intro / compact heading |
| `--v-font-24` | `1.5rem` | `400` | `1.334` | small display |
| `--v-font-heading-3` | `round(down, clamp(1.5rem, 1.071vw + 1.179rem, 2.25rem), 2px)` | `400` | `calc(1em + .5rem)` | section heading |
| `--v-font-heading-2` | `round(down, clamp(1.5rem, 1.071vw + 1.179rem, 2.25rem), 2px)` | `400` | `calc(1em + .5rem)` | mid heading |
| `--v-font-heading-1` | `round(down, clamp(2rem, 2.143vw + 1.357rem, 3.5rem), 2px)` | `400` | `calc(1em + .5rem)` | main heading |
| `--v-font-statement-3` | `round(down, clamp(3rem, 2.143vw + 2.357rem, 4.5rem), 2px)` | `400` | `calc(1em + .5rem)` | large numeric / hero |
| `--v-font-statement-2` | `round(down, clamp(3.5rem, 5vw + 2rem, 7rem), 2px)` | `400` | `calc(1em + .5rem)` | large statement |
| `--v-font-statement-1` | `round(down, clamp(4.5rem, 6.786vw + 2.464rem, 9.25rem), 2px)` | `400` | `calc(1em + .5rem)` | biggest statement |
| `--v-font-statement-signature` | `round(down, clamp(2.5rem, 3.929vw + 1.321rem, 5.25rem), 2px)` | `400` | `calc(1em + .5rem)` | `Volvo Broad Pro` |

> 현재 홈의 active type system은 base Novum `300/500`이 아니라 centenary `400/600` 계층으로 정렬된다. 거대한 statement scale이 존재하지만 weight는 과하게 무겁지 않다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Active Centenary Light

| Token | Hex | Usage |
|---|---|---|
| `--v-color-background-primary` | `#FFFFFF` | page background |
| `--v-color-background-secondary` | `#FAFAFA` | secondary section background |
| `--v-color-foreground-primary` | `#000000` | primary text |
| `--v-color-foreground-secondary` | `#5E5E5E` | supporting copy |
| `--v-color-foreground-tertiary` | `#787878` | tertiary text |
| `--v-color-foreground-accent-blue` | `#0B2DED` | links, current state, focus ring |
| `--v-color-surface-neutral` | `#000000` | dark pills / active surfaces |
| `--v-color-surface-gray` | `#E3E3E3` | muted chips / neutral fills |

### 06-2. Active Centenary Dark

| Token | Hex | Usage |
|---|---|---|
| `--v-color-background-primary` | `#000000` | dark theme background |
| `--v-color-background-secondary` | `#171717` | secondary dark section |
| `--v-color-foreground-primary` | `#FFFFFF` | primary text |
| `--v-color-foreground-secondary` | `#969696` | supporting copy |
| `--v-color-foreground-accent-blue` | `#3354FF` | accent blue dark mode |
| `--v-color-surface-neutral` | `#FFFFFF` | inverted pills / active surfaces |
| `--v-color-surface-gray` | `#3B3B3B` | muted fills |

### 06-3. Shared Base / Legacy Accent

| Token | Light | Dark |
|---|---|---|
| `--v-color-foreground-accent-blue` (non-centenary) | `#1C6EBA` | `#378FE1` |
| `--v-color-surface-neutral` (non-centenary) | `#1F1F1F` | `#FFFFFF` |
| `--v-color-foreground-primary` (non-centenary) | `#0A0A0A` | `#FFFFFF` |
| `--v-color-foreground-secondary` (non-centenary) | `#616161` | `#BABABA` |

### 06-4. Accent Families

| Family | Light | Dark | Notes |
|---|---|---|---|
| Safety orange | `#FC6408` | `#FC6408` | centenary safety accent |
| Feedback green | `#048220` | `#048220` / fg `#07CA31` | success / confirmation |
| Feedback red | `#E52715` / fg `#CD2314` | `#E52715` / fg `#EF6658` | error / destructive |
| Feedback orange | `#CE6700` | fg `#F93` | warning / caution |

### 06-5. State Layer

| Token | Hex | Usage |
|---|---|---|
| `--v-color-ornament-primary` | `#0000001F` | default border / dividers |
| `--v-color-state-primary-subtle` | `#0000000A` | subtle hover on light |
| `--v-color-state-primary-medium` | `#0000001F` | medium pressed layer |
| `--v-color-state-primary-strong` | `#0003` | strong pressed layer |
| `--v-color-state-accent-blue-subtle` | `#0B2DED0A` | blue hover fill |
| `--v-color-state-accent-blue-medium` | `#0B2DED1F` | blue focus / selected layer |
| `--v-color-state-accent-blue-strong` | `#0B2DED33` | strong selected layer |

> 색채 구조는 "검정/흰색 surface + 블루 interaction signal"이 핵심이다. 블루는 브랜드 면적색이 아니라 상태색에 가깝다.

---

## 07. Spacing
<!-- SOURCE: auto -->

### 07-1. Fixed Ladder

| Token | Value |
|---|---|
| `--v-space-2` | `.125rem` |
| `--v-space-4` | `.25rem` |
| `--v-space-8` | `.5rem` |
| `--v-space-12` | `.75rem` |
| `--v-space-16` | `1rem` |
| `--v-space-24` | `1.5rem` |
| `--v-space-32` | `2rem` |
| `--v-space-48` | `3rem` |
| `--v-space-64` | `4rem` |

### 07-2. Fluid Section Ladder

| Token | Value |
|---|---|
| `--v-space-xs` | `round(clamp(.5rem, 1.071vw + .179rem, 1.25rem), 2px)` |
| `--v-space-sm` | `round(clamp(1rem, 1.429vw + .571rem, 2rem), 2px)` |
| `--v-space-md` | `round(clamp(1.5rem, 2.143vw + .857rem, 3rem), 2px)` |
| `--v-space-lg` | `round(clamp(2rem, 2.143vw + 1.357rem, 3.5rem), 2px)` |
| `--v-space-xl` | `round(clamp(3rem, 2.143vw + 2.357rem, 4.5rem), 2px)` |
| `--v-space-2xl` | `round(clamp(4rem, 5.714vw + 2.286rem, 8rem), 2px)` |

### 07-3. Layout-Specific

| Token | Value | Role |
|---|---|---|
| `--v-space-gutter` | `clamp(1rem, 2.6vw + .3rem, 1.5rem)` | grid column gap |
| `--v-space-pagemargin` | `round(clamp(1rem, 4.286vw + -.286rem, 4rem), 2px)` | outer page margin |
| `--v-space-gridded-element-gap` | `var(--v-space-2)` | tight grid card gap |

> fixed ladder는 컴포넌트 내부 리듬을, fluid ladder는 섹션 간 호흡을 담당한다.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Usage |
|---|---|---|
| `--v-radius-sm` | `.25rem` | default small rounding |
| `--v-radius-md` | `.5rem` | dialog / card mid rounding |
| `--v-radius-lg` | `1rem` | emphasized cards / modals |
| `--v-radius-full` | `9999px` | pills / circular controls |
| `--v-shape-default` | `var(--v-radius-sm)` | default component shape |
| `--v-shape-emphasis` | `var(--v-radius-sm)` | emphasized shape in non-centenary utilities |

---

## 09. Shadows
<!-- SOURCE: auto -->

Volvo 홈은 큰 blur shadow보다 **ring / outline / drop-shadow 최소치**에 의존한다.

| Selector / Token | Value | Role |
|---|---|---|
| `.border-ring` | `inset 0 0 0 1px var(--v-color-ornament-primary)` | generic outline |
| `.border-ring-2` | `inset 0 0 0 2px var(--_v2c3a00, var(--v-color-ornament-primary))` | selected outline |
| `.SelectionCard_selectionCard__1Ywjv:hover` | `0 0 0 1px var(--v-color-always-black)` | hover emphasis |
| `.SelectionCard_selectionCard__1Ywjv:has(button[aria-checked=true])` | `0 0 0 2px var(--v-color-surface-accent-blue)` | selected state |
| `.sitenav__bottomRight__Ohipw` | `filter: drop-shadow(0px 2px 6px rgb(0 0 0 / 16%))` | chat launcher elevation |

> 이 사이트를 Volvo답게 보이게 하려면 soft card shadow를 쌓기보다 ring과 border contrast를 먼저 맞춰야 한다.

---

## 10. Motion
<!-- SOURCE: auto -->

| Token / Selector | Value | Usage |
|---|---|---|
| `--v-transition-default` | `.22s ease` | 기본 상태 전환 |
| `--v-transition-micro` | `.11s ease` | micro-interaction |
| `--v-transition-notable` | `.8s ease` | larger staged transition |
| `@media (prefers-reduced-motion: reduce)` | `50ms / 25ms / 12ms` | motion reduction |
| `.SubNavigation_backgroundBlur__C2rTe:before` | `backdrop-filter: blur(12px)` | sticky nav glass layer |
| `.MediaDialog_media-dialog__JyYXu :is([open]) [slot=main]` | `.22s` scale / translate transition | modal open |
| `.BentoGallery_galleryItemAnimation__Ul8G5:hover` | `transform: scale(1.05)` | media hover zoom |
| `.ChargingTool_overlayModal__vyivl::backdrop` | `.25s ease` fade | sheet backdrop |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

- **Page shell** — `--v-size-pagemax: min(160rem, 100vw)`로 매우 넓은 캔버스를 허용하지만, 실제 콘텐츠 grid는 `--v-size-grid-maxwidth: min(81rem, 100vw - ...)`에 묶여 있다.
- **Grid column count** — 기본 `8`, `@media (width>=30rem)`에서 `12`.
- **Discovery card** — `grid-template-areas: "top" "media" "main"` 기본, `30rem` 이상에서 `"media main"` horizontal 변형 가능.
- **Promotion hero / display** — 밝은/어두운 gradient scrim을 이미지 위에 얹는 구조. `rgb(255 255 255 / 62%)` 또는 `rgb(0 0 0 / 62%)`를 direction variable로 돌린다.
- **Sticky navigation** — blur backdrop + current link fill 방식. 선택된 링크는 `background: var(--v-color-foreground-primary)`와 inverted text로 처리한다.
- **Form / tool layout** — `ChargingTool`처럼 mobile은 `"info" "media" "cta"` 단일열, tablet 이상에서 2열로 전환.

---

## 12. Responsive
<!-- SOURCE: auto -->

| Breakpoint | Behavior |
|---|---|
| `< 30rem` | mobile default, 8-column grid, stacked cards, dialog/sheet full width 경향 |
| `>= 30rem` | 12-column grid 시작, discovery card horizontal 변형, carousel card width 재계산 |
| `>= 64rem` | larger paddings (`32/48/64` 적극 사용), gallery / dialog / charging tool desktop layout |
| `>= 100rem` | utility visibility helpers (`until-xl:*`) 전환 기준 |

### Concrete Examples

- `.discovery-card_horizontal__V6WqA` — `30rem` 이상에서 `grid-template-columns: 1fr 1fr`
- `.SubNavigation_innerContainer__CVvJ0` — `64rem` 이상에서 3-track layout
- `.styles_card__6z3Hx` — carousel card width가 mobile `66.67%` -> tablet `40%` -> desktop `25%`

---

## 13. Components
<!-- SOURCE: auto -->

### 13-1. SubNavigation

```html
<nav class="SubNavigation_container__7WUT3" data-color-mode="light">
  <div class="SubNavigation_backgroundBlur__C2rTe"></div>
  <a class="SubNavigation_link__haBVG" aria-current="page">Electrification</a>
</nav>
```

| Property | Value |
|---|---|
| current state | `color: var(--v-color-foreground-inverted)` + `background: var(--v-color-foreground-primary)` |
| hover (light) | `background: rgba(0 0 0 / 4%)` |
| backdrop | `blur(12px)` + semi-transparent white/black layer |
| minimum tap width | `2.5rem` |

### 13-2. Discovery Card

```html
<article class="discovery-card_discovery_card__3E5JV discovery-card_horizontal__V6WqA">
  <div slot="media"></div>
  <div slot="main"></div>
</article>
```

| Property | Value |
|---|---|
| base layout | `grid-template-areas: "top" "media" "main"` |
| horizontal layout | `@media (min-width:30rem)` -> `"media main"` |
| main padding | `var(--v-space-24)` / `var(--v-space-32)` / `var(--v-space-64)` depending variant |

### 13-3. Selection / Tool States

```html
<div class="SelectionCard_selectionCard__1Ywjv">
  <button aria-checked="true"></button>
</div>
```

| Property | Value |
|---|---|
| selected ring | `0 0 0 2px var(--v-color-surface-accent-blue)` |
| hover ring | `0 0 0 1px var(--v-color-always-black)` |
| desktop focus affordance | `ChargingTool_selectComponent__f6Ii8:hover { box-shadow: inset 0 0 0 2px var(--v-color-foreground-accent-blue); }` |

---

## 14. Content / Copy Voice
<!-- SOURCE: auto+manual -->

| Pattern | Example | Reading |
|---|---|---|
| Safety-first headline | `Volvo 역사상 가장 안전한 자동차` | 기술보다 안전을 먼저 전면에 둔다 |
| Product intro | `완전히 새로운 볼보 EX90을 만나보세요.` | 직접적이고 설명이 짧다 |
| Brand mission | `개인적이고 지속 가능하며 안전하게 이동할 수 있는 자유` | "personal / sustainable / safe" 3축 반복 |
| Utility CTA | `상담 신청하기`, `시승 신청하기`, `서비스 센터 예약` | 감성 CTA보다 실용 CTA가 많다 |

> 카피 톤은 고조된 럭셔리보다 신뢰, 안전, 실용에 가깝다.

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Volvo Cars /kr/ — centenary active layer */
[data-theme="centenary"] {
  --volvo-bg: #fff;
  --volvo-bg-secondary: #fafafa;
  --volvo-surface: #000;
  --volvo-text: #000;
  --volvo-text-secondary: #5e5e5e;
  --volvo-accent: #0B2DED;
  --volvo-accent-strong: #0B2DED33;
  --volvo-border: #0000001f;
  --volvo-radius-sm: .25rem;
  --volvo-radius-md: .5rem;
  --volvo-radius-lg: 1rem;
  --volvo-space-16: 1rem;
  --volvo-space-24: 1.5rem;
  --volvo-space-32: 2rem;
  --volvo-space-48: 3rem;
  --volvo-font-sans:
    "Volvo Centum", "Helvetica Neue", "Helvetica",
    "Noto Sans", "Segoe UI", "Arial", sans-serif;
  --volvo-font-display: "Volvo Broad Pro", "Arial Black", sans-serif;
}

body {
  font-family: var(--volvo-font-sans);
  color: var(--volvo-text);
  background: var(--volvo-bg);
}

.volvo-pill-current {
  color: #fff;
  background: #000;
  border-radius: 9999px;
}

.volvo-focus {
  box-shadow: inset 0 0 0 2px var(--volvo-accent);
}
```

---

## 16. Tailwind
<!-- SOURCE: auto -->

> N/A — 실사이트는 Tailwind가 아니라 `--v-*` 토큰 + 자체 utility class(`text-primary`, `rounded-lg`, `gap-24`, `border-ring-2`)를 사용한다.

---

## 17. Agent Prompt
<!-- SOURCE: manual -->

```text
Recreate Volvo Cars /kr/ as the current centenary theme, not the legacy Novum-only layer.
Keep the page light by default: white background, black primary text, black neutral surfaces,
and electric blue (#0B2DED) only for current / focus / selected states.
Use Volvo Centum for the active UI, but preserve the fact that Volvo Novum still exists in shared CSS
when reproducing older or shared modules. Prefer ring, border, blur, and scrim over soft card shadows.
Respect the 8-column mobile -> 12-column desktop grid and the spacing ladder built from 16/24/32/48/64px.
```

---

## 18. DO / DON'T
<!-- SOURCE: auto+manual -->

### ✅ DO

- `data-theme="centenary"` 기준으로 구현하고, 기본 배경은 `#FFFFFF`로 유지
- active sans는 `Volvo Centum`, display는 `Volvo Broad Pro`로 맞추기
- `Volvo Novum`이 shared CSS에 실제 존재한다는 사실은 보존하되, 현재 홈 전체 기본 폰트로 오독하지 않기
- 블루 `#0B2DED`는 current / focus / selected 상태에 제한해서 쓰기
- shadow보다 `border-ring`, selection ring, backdrop blur를 우선 사용
- mobile 8열 -> `30rem` 이상 12열 grid 전환을 유지

### ❌ DON'T

- 파란색을 큰 hero 배경이나 카드 배경으로 덮지 말 것
- legacy shared blue `#1C6EBA`와 active centenary blue `#0B2DED`를 섞어서 하나의 레이어처럼 쓰지 말 것
- soft card shadow를 여러 겹 쌓아 Volvo 분위기를 만들려 하지 말 것
- 모든 텍스트를 같은 400 한 단계로 평평하게 만들지 말 것
- OneTrust selector namespace를 Volvo 본체 token system으로 오독하지 말 것
