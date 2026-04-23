---
schema_version: 3.1
slug: lego
service_name: LEGO
site_url: https://www.lego.com/en-us
fetched_at: 2026-04-23
default_theme: light
brand_color: "#E3000B"
primary_font: Cera Pro
font_weight_normal: 400
token_prefix: --ds-*

bold_direction: Structured Play
aesthetic_category: Friendly Fintech
signature_element: action_color_split
code_complexity: high

medium: web
medium_confidence: high
---

# DESIGN.md — LEGO (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: auto+manual -->

2026-04-23 기준 `lego.com/en-us`의 CSS는 "로고 레드가 모든 인터랙션을 지배한다"는 인상을 주지 않는다. 실제 UI는 `#FFFFFF` / `#F7F7F7` / `#F2F2F2`의 밝은 레이어를 기본 바닥으로 깔고, 본문 텍스트를 `#141414`, 보조 텍스트를 `#636363`으로 고정한 뒤, 클릭 가능한 기본 액션을 **파란색 `#005AD2` 계열**로 처리한다. LEGO의 유명한 로고 레드 `#E3000B`는 분명 CSS 안에 존재하지만, 현재 글로벌 액션 토큰의 기본값은 아니다.

색상 구조는 세 층으로 나뉜다. 첫 번째는 로고/브랜드 층으로, `--ds-color-brand-logo-corporate-red: #e3000b`, `--ds-color-brand-logo-yellow: #ffed00`, `--ds-color-brand-bright-blue: #006cb7`가 있다. 두 번째는 실제 제품 UI 층으로, 기본 버튼과 링크가 `--ds-color-interactive-primary-enabled: #005ad2`, hover `#0045b7`, pressed `#011c58`를 사용한다. 세 번째는 브랜드성 액센트 층으로, 노랑이 `--ds-color-interactive-brand-enabled: #ffd502`에서 시작하는 4단 액션 램프로 재정의된다. 즉 LEGO는 "로고 팔레트"와 "UI 액션 팔레트"를 분리해서 운영한다.

타이포그래피도 이중 구조다. 기본 UI는 `html:not([lang=ko],[lang=zh],[lang=ja])>body { font-family: Cera Pro, sans-serif; }`로 `Cera Pro`를 쓴다. 반면 브랜드 모드에서는 `--ds-font-font-family: LEGO Typewell`이 적용된다. `LEGO Typewell`은 캠페인성 브랜드 헤드라인용이고, 일반 전자상거래 UI는 `Cera Pro`가 맡는다. 현재 CSS의 display/heading 계층은 대부분 `font-weight: 700`, 본문은 `400/500/700` 3단으로 관리되며, 기존 문서에 있던 "LEGO는 기본적으로 900 uppercase headline" 해석은 현재 글로벌 UI CSS와 맞지 않는다.

레이아웃과 간격 역시 일반적인 8pt grid보다 더 특이하다. spacing scale은 `11 / 18 / 22 / 25 / 29 / 43 / 50 / 58 / 66 / 86 / 100px`처럼 비등간격 토큰으로 정의되고, 최대 콘텐츠 폭은 `--ds-breakpoint-xl: 100em` 즉 `1600px`에서 멈춘다. 버튼은 기본적으로 `999px` pill radius를 쓰지만, 카드/레이어는 `4 / 8 / 12 / 16px` 단위로 차분하게 관리된다. 그래서 LEGO의 현재 웹 미학은 "장난감 브랜드답게 무조건 둥글고 알록달록"이 아니라, **정리된 commerce shell 위에 제한된 브랜드 컬러를 꽂는 구조적 플레이**에 가깝다.

### Key Characteristics

- 로고 레드 `#E3000B`는 존재하지만 기본 CTA 색이 아니다
- 기본 인터랙션은 블루 `#005AD2 → #0045B7 → #011C58`
- 브랜드성 액센트는 노랑 `#FFD502 → #FAC400 → #EF9F00`
- 기본 UI 폰트는 `Cera Pro`, 브랜드 모드는 `LEGO Typewell`
- surface는 `#FFFFFF / #F7F7F7 / #F2F2F2` 3층 구조
- spacing은 8pt가 아니라 `11 / 18 / 22 / 25 / 29 / 43...` 비정형 scale
- 버튼 radius는 pill `999px`, 레이어/카드는 `4~16px`
- global container max-width는 `1600px`

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Structured Play
> **Aesthetic Category**: Friendly Fintech
> **Signature Element**: 이 사이트는 **로고 레드와 실제 액션 블루를 분리한 palette split**으로 기억된다.
> **Code Complexity**: high — `--ds-*` 토큰 986개, locale/brand mode 폰트 분기, semantic alias layer가 동시에 존재한다.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 LEGO처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 기본 폰트 */
html:not([lang="ko"], [lang="zh"], [lang="ja"]) > body {
  font-family: "Cera Pro", sans-serif;
  font-weight: 400;
}

/* 2. surface + text */
:root {
  --bg: #FFFFFF;
  --bg-subdued: #F7F7F7;
  --fg: #141414;
  --fg-subtle: #636363;
}

/* 3. 로고와 액션을 분리 */
:root {
  --logo-red: #E3000B;
  --action-primary: #005AD2;
  --action-primary-hover: #0045B7;
  --action-brand: #FFD502;
}
```

**절대 하지 말아야 할 것 하나**: LEGO 사이트를 본다고 해서 모든 CTA를 `#E3000B`로 칠하지 마라. 2026-04-23에 수집한 실제 CSS에서 기본 버튼 `.sk-button`은 블루 액션 토큰(`--ds-color-action-primary-*`)을 쓴다. 로고 레드는 브랜드/로고 레이어에 남겨 둬야 LEGO답다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.lego.com/en-us` |
| Fetched | `2026-04-23` |
| Extractor | `curl_cffi.requests.Session(impersonate="chrome")` + Chrome Referer |
| HTML size | `948369` bytes |
| CSS files | `12`개 · 총 `309769` bytes |
| Unique custom properties | `1128`개 (`--ds-*`만 `986`개) |
| Main DS bundle | `/_next/static/css/1bc34d511a435e5f.css` · `216321` bytes |
| Token prefix | `--ds-*` |
| Method | CSS 직접 파싱 · 수집 실패 값은 `N/A` 처리 |

### CSS Collection URLs

- `https://www.lego.com/_next/static/css/1bc34d511a435e5f.css` — `216321` bytes
- `https://www.lego.com/_next/static/css/d80a510ada61d8f7.css` — `21959` bytes
- `https://www.lego.com/_next/static/css/476653c009098383.css` — `20678` bytes
- `https://www.lego.com/_next/static/css/aa6fcd107f606ec8.css` — `12649` bytes
- `https://www.lego.com/_next/static/css/c1bc796e3fb4a2d5.css` — `12430` bytes
- `https://www.lego.com/_next/static/css/43341d25485cc380.css` — `12107` bytes
- `https://www.lego.com/_next/static/css/c614d264da0c42e3.css` — `8629` bytes
- `https://www.lego.com/_next/static/css/98c752df3e9c3ab6.css` — `2247` bytes
- `https://www.lego.com/_next/static/css/1331829dd8dc9072.css` — `1065` bytes
- `https://www.lego.com/_next/static/css/7e5af1acad2f2c5e.css` — `970` bytes
- `https://www.lego.com/_next/static/css/ef07c4b2488ac61d.css` — `584` bytes
- `https://www.lego.com/_next/static/css/b9fbca678ed9d6f1.css` — `130` bytes

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js pages router 기반 SSR/SSG hybrid
  - 스크립트에서 `/_next/static/chunks/pages/_app-*.js`, `/_next/static/chunks/pages/[locale]-*.js`, build id `61J2ChArm3qW-yBdCy2Nz` 확인
- **Design system**: LEGO in-house shared design system (`--ds-*`)
- **CSS architecture**: 글로벌 DS bundle 1개 + 페이지/모듈별 CSS Modules
  - raw ramps: `--ds-color-core-*`
  - brand palette: `--ds-color-brand-*`
  - semantic alias: `--ds-color-content-*`, `--ds-color-layer-*`, `--ds-color-action-*`
  - layout/type: `--ds-layout-*`, `--ds-spacing-*`, `--ds-screen-text-*`, `--ds-misc-*`
- **Class naming**: 두 계층 혼합
  - DS utilities — `.sk-button`, `.heading-*`, `.display-*`
  - component modules — `.ContentCard_*__hash`, `.QuickLinksWrapper_*__hash`, `.Layout_*__hash`
- **Default theme**: light
- **Font loading**: `assets.lego.com/fonts/...` self-hosted `woff2`
- **Canonical anchor**: 로고 팔레트와 UI 액션 팔레트를 분리하는 구조

---

## 04. Font Stack
<!-- SOURCE: auto -->

- **Default UI font**: `Cera Pro`
- **Brand/display mode**: `LEGO Typewell`
- **Locale overrides**: `Noto Sans KR`, `Noto Sans JP`, `Noto Sans SC`
- **Weight normal / medium / bold / black**: `400 / 500 / 700 / 900`

```css
:root {
  --ds-font-font-family: "Cera Pro";
}

[data-mode="brand"] {
  --ds-font-font-family: LEGO Typewell;
}

html[lang="ko"] {
  --ds-font-font-family: "Noto Sans KR";
}

html:not([lang="ko"], [lang="zh"], [lang="ja"]) > body {
  font-family: Cera Pro, sans-serif;
}
```

### Loaded Font Files

- `Cera Pro` — `100 / 400 / 500 / 700 / 900` + italic variants
- `LEGO Typewell` — `300 / 400 / 500 / 700 / 900` + italic variants
- `Noto Sans KR` — `400 / 500 / 700`

> **라이선스 주의**: `Cera Pro`와 `LEGO Typewell`은 self-hosted 상용 폰트다. 외부 프로젝트에서 재배포 가능한 오픈 라이선스로 간주하면 안 된다.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing | Usage |
|---|---|---|---|---|---|
| `display-lg` | `clamp(3.875rem, 1.08163rem + 11.9184vi, 13rem)` | `700` | `1.15` | `-0.02em` | 대형 캠페인 hero |
| `display-md` | `clamp(3.625rem, 1.17602rem + 10.449vi, 11.625rem)` | `700` | `1.15` | `-0.015em` | 대형 campaign display |
| `display-sm` | `clamp(3.1875rem, 1.3125rem + 8vi, 9.3125rem)` | `700` | `1.15` | `-0.02em` | 큰 브랜드 headline |
| `heading-6xl` | `clamp(2.5rem, 1.4477rem + 4.4898vi, 5.9375rem)` | `700` | `1.15` | `-0.01em` | 섹션 hero |
| `heading-3xl` | `clamp(1.75rem, 1.34821rem + 1.71429vi, 3.0625rem)` | `700` | `1.35` | `0` | 대형 section title |
| `heading-xl` | `clamp(1.375rem, 1.20281rem + 0.734694vi, 1.9375rem)` | `700` | `1.35` | `0` | 카드/섹션 헤더 |
| `heading-md` | `clamp(1.125rem, 1.08674rem + 0.163265vi, 1.25rem)` | `700` | `1.5` | `0` | 작은 heading |
| `body-lg` | `1.125rem` | `400 / 500 / 700` | `1.5` | `0` | 긴 본문 / promo text |
| `body-md` | `1rem` | `400 / 500 / 700` | `1.5` | `0` | 기본 body |
| `body-sm` | `0.875rem` | `400 / 500 / 700` | `1.62` | `0.01em` | 메타 / 카드 보조 |
| `label-xs` | `0.75rem` | `400 / 500 / 700` | `1.75` | `0.01em` | 태그 / micro label |

> 핵심은 "모든 큰 텍스트를 900 uppercase로 밀어붙이는 것"이 아니다. 현재 global UI CSS는 **700 weight 중심의 display/heading scale**을 쓰고, 매우 큰 크기 변화는 `clamp()`로 해결한다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Requested Brand Color Verification

| Requested Hex | CSS status | Verified token / observed value | Note |
|---|---|---|---|
| `#E3000B` | confirmed | `--ds-color-brand-logo-corporate-red: #e3000b` | exact match |
| `#FFCF00` | `N/A` | `N/A` | exact token not found in fetched CSS |
| `#006DB7` | `N/A` | `N/A` | exact token not found in fetched CSS |

### 06-2. Closest Verified Tokens For Missing Requests

| Purpose | Token | Hex |
|---|---|---|
| logo yellow | `--ds-color-brand-logo-yellow` | `#FFED00` |
| bright yellow | `--ds-color-brand-bright-yellow` | `#FFD400` |
| UI brand accent | `--ds-color-interactive-brand-enabled` | `#FFD502` |
| bright blue | `--ds-color-brand-bright-blue` | `#006CB7` |
| primary action blue | `--ds-color-interactive-primary-enabled` | `#005AD2` |

### 06-3. Logo / Brand Palette

| Token | Hex | Usage |
|---|---|---|
| `--ds-color-brand-logo-corporate-red` | `#E3000B` | logo red |
| `--ds-color-brand-logo-yellow` | `#FFED00` | logo yellow |
| `--ds-color-brand-bright-blue` | `#006CB7` | brand palette blue |
| `--ds-color-brand-bright-yellow` | `#FFD400` | brand palette yellow |
| `--ds-color-brand-bright-red` | `#DD1A22` | secondary brand red |

### 06-4. Primary Action Palette

| Token | Hex | Usage |
|---|---|---|
| `--ds-color-interactive-primary-enabled` | `#005AD2` | default button / primary link |
| `--ds-color-interactive-primary-hovered` | `#0045B7` | hover |
| `--ds-color-interactive-primary-pressed` | `#011C58` | pressed |
| `--ds-color-interactive-primary-selected` | `#003290` | selected / visited emphasis |
| `--ds-color-support-focused-default` | `#4695F0` | focus outline |

### 06-5. Brand Accent (Yellow) Action Palette

| Token | Hex | Usage |
|---|---|---|
| `--ds-color-interactive-brand-enabled` | `#FFD502` | yellow action / promotional emphasis |
| `--ds-color-interactive-brand-hovered` | `#FAC400` | hover |
| `--ds-color-interactive-brand-pressed` | `#EF9F00` | pressed |
| `--ds-color-interactive-brand-selected` | `#F5B200` | selected |

### 06-6. Neutrals and Semantic Content

| Token | Hex | Usage |
|---|---|---|
| `--ds-color-surface-background-base-default` | `#FFFFFF` | page bg |
| `--ds-color-surface-background-base-layer-1` | `#F7F7F7` | subdued layer |
| `--ds-color-surface-background-base-layer-2` | `#F2F2F2` | muted layer |
| `--ds-color-content-default` | `#141414` | body text |
| `--ds-color-content-subtle` | `#636363` | secondary text |
| `--ds-color-stroke-default` | `#B0B0B0` | border default |
| `--ds-color-stroke-subtle` | `#CBCBCB` | light border |
| `--ds-color-content-positive` | `#007133` | positive text |
| `--ds-color-content-negative` | `#BD0000` | negative text |
| `--ds-color-support-warning-default` | `#F68226` | warning layer |

---

## 07. Spacing
<!-- SOURCE: auto -->

LEGO DS의 spacing은 전형적인 8pt scale이 아니다. 실제 토큰은 `11px`부터 시작하는 비등간격 체계다.

| Token | Value | Usage |
|---|---|---|
| `--ds-layout-spacing-100` | `11px` | 3xs |
| `--ds-layout-spacing-150` | `18px` | 2xs |
| `--ds-layout-spacing-200` | `22px` | xs |
| `--ds-layout-spacing-250` | `25px` | sm |
| `--ds-layout-spacing-300` | `29px` | md |
| `--ds-layout-spacing-400` | `43px` | lg |
| `--ds-layout-spacing-500` | `50px` | xl |
| `--ds-layout-spacing-600` | `58px` | 2xl |
| `--ds-layout-spacing-700` | `66px` | 3xl |
| `--ds-layout-spacing-800` | `86px` | 4xl |
| `--ds-layout-spacing-1000` | `100px` | 5xl |

### Fluid Spacing Tokens

| Token | Value |
|---|---|
| `--ds-screen-spacing-fluid-100-150` | `clamp(.5rem, .423469rem + .326531vi, .75rem)` |
| `--ds-screen-spacing-fluid-250-400` | `clamp(1.25rem, 1.02041rem + .979592vi, 2rem)` |
| `--ds-screen-spacing-fluid-500-1000` | `clamp(2.5rem, 1.73469rem + 3.26531vi, 5rem)` |

> layout spacing을 임의로 `8 / 16 / 24 / 32`로 정규화하면 LEGO의 리듬이 무너진다.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Usage |
|---|---|---|
| `--ds-layout-radius-25` | `2px` | hairline rounding |
| `--ds-layout-radius-50` | `4px` | small controls |
| `--ds-layout-radius-75` | `6px` | intermediate chips |
| `--ds-layout-radius-100` | `8px` | default UI corner |
| `--ds-layout-radius-150` | `12px` | card rounding |
| `--ds-layout-radius-200` | `16px` | large surfaces |
| `--ds-layout-radius-400` | `32px` | oversized panel |
| `--ds-layout-radius-600` | `48px` | extra rounded shell |
| `--ds-layout-radius-pill` | `999px` | buttons / pills |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Token level | Shadow |
|---|---|
| `xs` | `0 1px 3px 0 #0003, 0 1px 2px -1px #00000052` |
| `sm` | `0 3px 6px 0 #0003, 0 2px 4px -2px #00000052` |
| `md` | `0 6px 12px 1px #0003, 0 4px 8px -3px #00000052` |
| `lg` | `0 12px 24px 0 #0003, 0 8px 16px 0 #00000052` |
| `xl` | `0 16px 40px 4px #0003, 0 12px 24px 0 #00000052` |

색상 자체는 거의 늘 `#0003` / `#00000052` 조합이다. LEGO는 섀도우보다 레이어 색과 pill shape로 컴포넌트를 구분한다.

---

## 10. Motion
<!-- SOURCE: auto -->

| Pattern | Value | Where observed |
|---|---|---|
| accordion | `height .25s linear` | expandable blocks |
| transform | `transform .25s linear` | simple slide/drag states |
| tray | `transform var(--sk-tray-animation-speed) ease-out` | tray / drawer |
| tray speed token | `--sk-tray-animation-speed: .5s` | global tray timing |
| toggle token | `--_toggle-animation-duration: .4s` | toggle / switch controls |
| overlay fade | `opacity .2s ~ .35s` | overlays / modals |
| menu | `.3s` | menu show/hide |
| promo cycle | `--_display-duration: 5s`, `--_slide-in-duration: .5s`, `--_slide-out-duration: .3s` | rotating banners |

모션은 있는 편이지만, 전역적인 "브랜드 모션 시스템"보다 컴포넌트 로컬 타이밍 토큰에 가깝다.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

- **Global container**: `.Layout_layout__7aSvA { max-width: var(--ds-breakpoint-xl); width: 100%; margin: 0 auto; }` → 최대 `1600px`
- **Quick links wrapper**: `.QuickLinksWrapper_wrapper__zhc3F`는 중앙 정렬 + fluid padding, `75em` 이상에서 `14% / 86%` grid variant 사용
- **Content cards**: `.ContentCard_standard__WGdOH`는 `display:flex`, `flex-direction:column`, `gap: var(--ds-spacing-xs)` 구조
- **Card content padding**: editorial card content는 모바일 `var(--ds-spacing-xs) var(--ds-spacing-2xs)`, `75em` 이상 `var(--ds-spacing-lg) var(--ds-spacing-md)`
- **Buttons**: `.sk-button`는 고정 height token + pill radius + min-width `max-content`

---

## 12. Responsive
<!-- SOURCE: auto -->

| Breakpoint token | Value | Approx px |
|---|---|---|
| `--ds-breakpoint-xs` | `23.4375em` | `375px` |
| `--ds-breakpoint-sm` | `36.25em` | `580px` |
| `--ds-breakpoint-md` | `56.25em` | `900px` |
| `--ds-breakpoint-lg` | `75em` | `1200px` |
| `--ds-breakpoint-xl` | `100em` | `1600px` |

실제 모듈 CSS는 `580px`, `900px`, `1200px`에서 레이아웃 전환이 자주 나타난다. spacing은 media query보다 `clamp()` 기반 fluid token을 먼저 쓰고, 큰 구조 전환만 breakpoint에서 처리한다.

---

## 13. Components
<!-- SOURCE: auto -->

### Primary Pill Button

```css
.sk-button {
  background-color: var(--ds-color-action-primary-enabled);
  border-radius: var(--ds-border-radius-round);
  color: var(--ds-color-text-on-primary);
  height: var(--_button-height);
  padding: 0 var(--_button-padding);
}

.sk-button--medium {
  --_button-height: var(--ds-layout-size-500);
  --_button-padding: var(--ds-layout-spacing-200);
  font-size: 1rem;
  font-weight: 500;
}
```

### Heading Utility

```css
.display-sm,
.display-md,
.display-lg,
.heading-sm,
.heading-md,
.heading-lg,
.heading-xl,
.heading-2xl,
.heading-3xl,
.heading-4xl,
.heading-5xl,
.heading-6xl {
  font-family: var(--ds-font-font-family);
  font-weight: 700;
}
```

### Content Card Shell

```css
.ContentCard_contentCard__RaobR.ContentCard_standard__WGdOH {
  display: flex;
  flex-direction: column;
  gap: var(--ds-spacing-xs);
  max-width: 756px;
}
```

---

## 14. Content Voice
<!-- SOURCE: auto+manual -->

- **명령형 navigation**: `Shop`, `Discover`, `Help`, `Gift finder`
- **taxonomy-first**: `Sets by theme`, `Age`, `Price ranges`, `Interests`
- **명시적 qualifier**: `1.5+`, `18+`, `Under $25`, `Over $100`
- **브랜드/라이선스 표기 유지**: `LEGO® Animal Crossing™`, `Nike x LEGO® Collection`

카피 톤은 감성적인 슬로건보다 **분류와 탐색**에 더 무게가 있다. LEGO 브랜드의 즐거움은 언어보다 palette와 이미지에서 오고, 텍스트는 전자상거래 구조를 우선한다.

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
:root {
  --lego-logo-red: #E3000B;
  --lego-logo-yellow: #FFED00;
  --lego-brand-blue: #006CB7;

  --lego-ui-primary: #005AD2;
  --lego-ui-primary-hover: #0045B7;
  --lego-ui-primary-pressed: #011C58;

  --lego-ui-brand: #FFD502;
  --lego-ui-brand-hover: #FAC400;
  --lego-ui-brand-pressed: #EF9F00;

  --lego-surface-base: #FFFFFF;
  --lego-surface-subdued: #F7F7F7;
  --lego-surface-muted: #F2F2F2;
  --lego-text-default: #141414;
  --lego-text-subtle: #636363;
  --lego-stroke-default: #B0B0B0;
  --lego-stroke-subtle: #CBCBCB;

  --lego-space-3xs: 11px;
  --lego-space-2xs: 18px;
  --lego-space-xs: 22px;
  --lego-space-sm: 25px;
  --lego-space-md: 29px;
  --lego-space-lg: 43px;

  --lego-radius-sm: 4px;
  --lego-radius-md: 8px;
  --lego-radius-lg: 16px;
  --lego-radius-pill: 999px;
}

body {
  font-family: "Cera Pro", sans-serif;
  font-weight: 400;
  color: var(--lego-text-default);
  background: var(--lego-surface-base);
}

.lego-button {
  align-items: center;
  background: var(--lego-ui-primary);
  border: 0;
  border-radius: var(--lego-radius-pill);
  color: #FFFFFF;
  display: inline-flex;
  font-size: 1rem;
  font-weight: 500;
  height: 60px;
  padding: 0 var(--lego-space-xs);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
export default {
  theme: {
    extend: {
      colors: {
        lego: {
          logoRed: "#E3000B",
          logoYellow: "#FFED00",
          brandBlue: "#006CB7",
          primary: "#005AD2",
          primaryHover: "#0045B7",
          primaryPressed: "#011C58",
          accent: "#FFD502",
          accentHover: "#FAC400",
          accentPressed: "#EF9F00",
          surface: "#FFFFFF",
          subdued: "#F7F7F7",
          muted: "#F2F2F2",
          text: "#141414",
          subtle: "#636363",
          stroke: "#B0B0B0",
          strokeSubtle: "#CBCBCB",
        },
      },
      fontFamily: {
        sans: ['"Cera Pro"', "sans-serif"],
        display: ['"LEGO Typewell"', '"Cera Pro"', "sans-serif"],
      },
      spacing: {
        "lego-3xs": "11px",
        "lego-2xs": "18px",
        "lego-xs": "22px",
        "lego-sm": "25px",
        "lego-md": "29px",
        "lego-lg": "43px",
      },
      borderRadius: {
        lego: "8px",
        "lego-lg": "16px",
        "lego-pill": "999px",
      },
    },
  },
};
```

---

## 17. Agent Prompt
<!-- SOURCE: manual -->

`lego.com/en-us`의 2026-04-23 CSS를 기준으로 재현한다. 배경은 `#FFFFFF / #F7F7F7 / #F2F2F2` light layer 체계, 본문 텍스트는 `#141414`, 보조 텍스트는 `#636363`을 사용한다. 기본 UI 폰트는 `Cera Pro`, 브랜드용 대형 display에만 `LEGO Typewell`을 쓴다. 기본 CTA는 로고 레드가 아니라 블루 `#005AD2`이고 hover는 `#0045B7`, pressed는 `#011C58`이다. 노랑 액센트는 `#FFD502` 계열을 쓰고, 로고 레드 `#E3000B`는 브랜드 식별 요소에만 제한한다. spacing은 8pt로 재정규화하지 말고 `11 / 18 / 22 / 25 / 29 / 43 / 50 / 58 / 66 / 86 / 100px` 리듬을 유지한다. 버튼은 pill radius, cards는 `8~16px` radius, 최대 콘텐츠 폭은 `1600px`.

---

## 18. DO / DON'T
<!-- SOURCE: auto+manual -->

### DO

- 로고 팔레트(`#E3000B`, `#FFED00`)와 UI 액션 팔레트(`#005AD2`, `#FFD502`)를 분리한다
- 기본 UI는 `Cera Pro`, 브랜드성 display만 `LEGO Typewell`로 나눈다
- 버튼은 pill radius를 유지하고, cards는 `8~16px` 반경에서 멈춘다
- spacing은 `11 / 18 / 22 / 25 / 29 / 43...` 실제 토큰을 사용한다
- light surface 3층(`white / subdued / muted`)을 유지한다

### DON'T

- 모든 CTA를 `#E3000B`로 칠하지 않는다
- 요청값이라고 해서 CSS에 없는 `#FFCF00`, `#006DB7`를 사실처럼 쓰지 않는다
- spacing을 임의의 8pt grid로 정규화하지 않는다
- body까지 `LEGO Typewell`로 밀어붙이지 않는다
- dark background를 기본 페이지 톤으로 바꾸지 않는다
