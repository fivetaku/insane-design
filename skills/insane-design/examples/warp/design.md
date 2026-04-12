---
slug: warp
service_name: Warp
site_url: https://warp.dev
fetched_at: 2026-04-11
default_theme: light
brand_color: "#000000"
primary_font: Inter
font_weight_normal: 400
token_prefix: --framer-*
---

# DESIGN.md -- Warp (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Warp 마케팅 사이트처럼 만들기 -- 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #FAF9F6;      /* cream ivory -- 순백이 아님 */
  --fg: #000000;      /* 순수 검정 */
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #000000; }
```

**절대 하지 말아야 할 것 하나**: 배경을 `#FFFFFF` 순백이나 `#0E0E10` 다크로 두는 것. Warp **마케팅 사이트**는 따뜻한 크림 아이보리 `#FAF9F6` 이다. 터미널 앱과 마케팅 사이트를 혼동하면 전체 톤이 정반대가 된다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://warp.dev` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 768,998 bytes (Next.js SSR, Framer 호스팅) |
| CSS files | 0개 외부 + 1 인라인, 총 252,569자 |
| Token prefix | `--framer-*` (Framer 기반 CSS 변수 네임스페이스) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 -- AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (Framer 호스팅 -- framerusercontent.com 에셋 서빙)
- **Design system**: 없음 (커스텀) -- prefix `--framer-*` (Framer 플랫폼 기본 변수)
- **CSS architecture**: 단일 계층 인라인
  ```
  framer   (--framer-text-*, --framer-link-*, --framer-input-*)   플랫폼 기본 변수
  inline   style 속성 + 컴포넌트별 직접 값                          Framer 빌드 산출물
  ```
- **Class naming**: Framer 자동 생성 해시 클래스 (`framer-*`, `.ssr-variant-*`)
- **Default theme**: light (bg = `#FAF9F6` cream ivory)
- **Font loading**: Google Fonts + Framer CDN woff2 (`Inter`, `Geist Mono`, `Matter` 패밀리)
- **Canonical anchor**: `#000000` -- Warp 마케팅 사이트의 모든 CTA, 텍스트, 버튼이 검정을 기반으로 한다. 브랜드 고유 색상 악센트 없이 **monochrome** 으로 운영.

> **중요**: warp.dev 는 Warp 터미널 앱의 **마케팅 사이트**이다. 터미널 앱 UI(다크, cyan `#01A4FF`)와 마케팅 사이트(라이트, cream `#FAF9F6`)는 완전히 다른 디자인 표면이다. 이 문서는 **마케팅 사이트만** 다룬다.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Inter` (Google Fonts, 오픈소스)
- **Display headline font**: `Matter Regular` / `Matter Medium` (Displaay, 유료 라이선스)
- **Code font**: `Geist Mono` (Vercel, 오픈소스)
- **Additional mono**: `Fragment Mono`, `DM Mono`, `Matter Mono Regular`
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --warp-font-family:       "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
  --warp-font-family-display: "Matter Regular", "Matter Regular Placeholder", sans-serif;
  --warp-font-family-code:  "Geist Mono", "Fragment Mono", "DM Mono", ui-monospace, monospace;
  --warp-font-weight-normal: 400;
  --warp-font-weight-medium: 500;
  --warp-font-weight-bold:   600;
}
body {
  font-family: var(--warp-font-family);
  font-weight: var(--warp-font-weight-normal);
}
```

> **라이선스 주의**: `Matter Regular` / `Matter Medium` 은 Displaay.co 의 유료 라이선스 폰트다. 자체 프로젝트에서 대체하려면 `Inter` 를 그대로 쓰거나, geometric sans 계열에서 `DM Sans` 또는 `Satoshi` 가 비교적 가까운 대체재. `Matter SQ` (Square variant) 도 사이트에서 사용 중이다.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Role | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Hero H1 | clamp(56px, 9vw, 120px) | 400 | 1.1 | -0.02em |
| Section heading | 24px | 500 | 1.3 | -0.01em |
| Subheading | 20px | 400 | 1.4 | 0em |
| Body / nav | 16px | 400 | 1.5 | 0em |
| Caption / label | 12px | 500 | 1.45 | 0em |
| Code | 16px | 400 | 1.5 | 0em |

> Framer 빌드라 고정 px 값보다 인라인 스타일 + clamp/vw 단위를 혼용한다. Hero 헤드라인은 Matter Regular 400 + 큰 fluid type, 본문은 Inter 400 이 기본이다. weight 500 은 내비게이션과 라벨, 600 이상은 CTA 버튼에 사용된다. weight 700/900 은 Matter 블랙 등 디스플레이 장식 용도에 제한적으로 쓰인다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Core Palette (monochrome)
<!-- Warp 마케팅 사이트는 monochrome. 브랜드 컬러 ramp 없음. -->

> Warp 마케팅 사이트는 **near-monochrome** 디자인이다. 명시적인 브랜드 컬러 ramp 가 없고, 검정-회색-크림의 grayscale 스펙트럼만 사용한다.

| Step | Hex | Role |
|---|---|---|
| Black | `#000000` | primary text, CTA bg, headings |
| Near-black | `#121212` | dark section bg, product demo area |
| Dark gray | `#1A1A1A` | footer bg, dark card bg |
| Charcoal | `#232224` | link current color, code area |
| Dark charcoal | `#2B2B2B` | link hover decoration |
| Mid-dark | `#353534` | secondary text |
| Gray | `#454545` | link decoration color |
| Mid-gray | `#666469` | link text, muted body text |
| Warm gray | `#868584` | disabled / quiet text |
| Silver | `#999999` | input icon, placeholder |
| Light gray | `#AFAEAC` | border, divider |
| Pale gray | `#E3E2E0` | subtle border, separator |
| Cream variant | `#FAF9F5` | page bg variant (near `#FAF9F6`) |
| Cream | `#FAF9F6` | **page background (canonical)** |
| White | `#FFFFFF` | card surface, CTA text on dark |

### 06-5. Semantic (Framer CSS vars)
<!-- SOURCE: auto -->

| Token | Value | Usage |
|---|---|---|
| `--framer-text-color` | `#000` | 기본 텍스트 |
| `--framer-link-text-color` | `#666469` | 링크 텍스트 |
| `--framer-link-hover-text-color` | `#fff` | 링크 호버 (다크 섹션) |
| `--framer-link-current-text-color` | `#232224` | 현재 링크 |
| `--framer-link-text-decoration-color` | `#454545` | 링크 밑줄 |
| `--framer-link-hover-text-decoration-color` | `#2B2B2B` | 링크 호버 밑줄 |
| `--framer-input-font-color` | `#fff` | 다크 섹션 인풋 텍스트 |
| `--framer-input-placeholder-color` | `#999` | 인풋 플레이스홀더 |
| `--framer-input-icon-color` | `#999` | 인풋 아이콘 |
| `--framer-input-background` | `#FFFFFF0D` | 인풋 배경 (투명) |
| `--framer-input-border-color` | `#87878700` | 인풋 보더 (투명) |
| `--border-color` | `#FFFFFF29` | 다크 섹션 보더 |

### 06-6. Alpha / Overlay 컬러
<!-- SOURCE: auto -->

| Hex | Usage |
|---|---|
| `#FFFFFFE6` (90%) | 크림 배경 위 반투명 white overlay |
| `#FFFFFF99` (60%) | 반투명 텍스트 |
| `#FFFFFF29` (16%) | 다크 섹션 보더 |
| `#FFFFFF0D` (5%) | 인풋 배경 |
| `#87878700` (0%) | 투명 인풋 보더 |
| `#3636321A` (10%) | 라이트 섹션 미세 보더 |
| `#FAF9F6E6` (90%) | 크림 반투명 overlay |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto (CSS frequency count) -->

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#000000` | 74 | primary text, CTA bg, icons |
| 2 | `#FAF9F6` | 33 | page background (cream) |
| 3 | `#FFFFFF` | 10 | card surface, CTA text |
| 4 | `#FAF9F5` | 6 | page bg variant |
| 5 | `#FFFFFFE6` | 6 | alpha white overlay |
| 6 | `#121212` | 4 | dark section bg |
| 7 | `#999999` | 4 | placeholder, icon |
| 8 | `#E3E2E0` | 2 | light border |
| 9 | `#353534` | 2 | secondary text |
| 10 | `#FFFFFF99` | 2 | alpha text |
| 11 | `#AFAEAC` | 2 | muted border |
| 12 | `#232224` | 2 | link current |
| 13 | `#2B2B2B` | 2 | link hover decoration |
| 14 | `#666469` | 2 | link text, muted body |
| 15 | `#454545` | 2 | link decoration |

> Hex 분류 히스토그램: gray 12, white 8, black 2. **채도 있는 컬러가 하나도 없다** -- Warp 마케팅은 철저히 monochrome light 디자인이다. 앱 스크린샷 속 cyan 등은 이미지 에셋이지 CSS 컬러가 아니다.

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| `--framer-input-padding` | 12px | 인풋 내부 여백 |
| `--framer-paragraph-spacing` | 0px | 문단 간격 (Framer 기본) |
| `--framer-font-size` | 16px | 기본 폰트 크기 |

> Warp 마케팅 사이트는 Framer 빌드라 spacing 토큰이 CSS 변수로 체계화되어 있지 않다. 대부분 인라인 스타일로 직접 지정된다. 관측된 주요 spacing 패턴: 섹션 패딩 `80px~120px`, 카드 패딩 `24px~32px`, 요소 간격 `16px~24px`, 인라인 gap `8px~12px`.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-xs | 5px | 작은 버튼, 태그 |
| radius-sm | 6px | CTA 버튼, 인풋 |
| radius-md | 8px | 카드, 패널 |
| radius-lg | 10px | 큰 카드, 모달 |
| radius-xl | 20px | 히어로 카드, 제품 데모 컨테이너 |

> Warp 의 radius 는 상대적으로 작고 절제되어 있다. 5px~10px 범위가 주력이고, 20px 는 제품 데모 영역 같은 대형 컨테이너에만 사용된다.

---

## 09. Shadows
<!-- SOURCE: auto -->

> Warp 마케팅 사이트에는 CSS 변수로 정의된 shadow 토큰이 없다 (shadow_custom_props_total = 0). Framer 플랫폼 변수 `--framer-input-box-shadow` 와 `--framer-input-focused-box-shadow` 만 존재하며, 이들은 인풋 포커스 상태 전용이다.
>
> 시각적으로 페이지에서 elevation 은 거의 사용되지 않는다. Warp 마케팅 사이트는 **flat/borderless** 디자인으로, 깊이 표현 대신 배경색 대비(`#FAF9F6` vs `#121212` vs `#FFFFFF`)로 계층을 구분한다.

---

## 10. Motion
<!-- SOURCE: manual -->

CSS 에 별도 motion 토큰 변수는 없지만, 관측된 인터랙션 패턴:

| Pattern | Value | Usage |
|---|---|---|
| hover transition | `200ms ease` | 링크, 버튼 호버 색상 전환 |
| page scroll | Framer 내장 | 섹션 간 스크롤 기반 reveal |
| hero animation | Framer Motion | 제품 데모 영역 fade-in + scale |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

### Hero
- **Layout**: 중앙 정렬 -- 큰 헤드라인 상단, 아래에 2-column 제품 카드 (Warp Terminal / Oz)
- **Background**: cream `#FAF9F6`
- **H1**: fluid `clamp(56px, 9vw, 120px)` / weight `400` / tracking `-0.02em` / Matter Regular or Inter
- **Subheading**: `16px~18px` / weight `400` / color `#000000`
- **Max-width**: 약 1200px

### Section Rhythm
```css
section {
  padding: 80px 24px;
  max-width: 1200px;
  margin-inline: auto;
}
```

### 페이지 구조
Hero (cream) --> 제품 데모 (embedded dark screenshots) --> Social proof ("Don't take our word for it") --> 다크 섹션 (testimonials/features, `#121212` bg) --> Footer (dark) --> Downloads CTA (cream)

> **스크린샷 참고**: `screenshots/light-hero.png` 에 hero 영역이 캡처되어 있다. cream 배경 위에 검은 텍스트, 제품 스크린샷 2장이 카드 형태로 배치.

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary CTA Button

```html
<a class="framer-button" href="/download">Download for Mac</a>
```

| Property | Value |
|---|---|
| background | `#000000` |
| color | `#FAF9F6` (cream text on black) |
| border | none |
| height | ~44px |
| radius | 6px |
| weight | 500 |
| padding | 12px 24px |
| hover | opacity 또는 약간 밝아짐 |

### Secondary CTA / Link Button

| Property | Value |
|---|---|
| background | transparent |
| color | `#000000` |
| border | 1px `#E3E2E0` |
| radius | 6px |
| weight | 500 |

### Navigation Bar

| Property | Value |
|---|---|
| background | `#FAF9F6` (cream, 스크롤 시 blur) |
| height | ~56px |
| font | Inter 14px weight 400 |
| link color | `#666469` |
| link hover | `#232224` |
| CTA (right) | black bg pill |

### Product Card (Hero)

| Property | Value |
|---|---|
| background | `#FFFFFF` |
| border | subtle (near-transparent) |
| radius | 10px~20px |
| shadow | minimal or none |
| inner | 다크 제품 스크린샷 embedded |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 선언문, 짧고 강렬, 2줄 이내 | "Warp is the agentic development environment" |
| Primary CTA | 동사 + 플랫폼 | "Download for Mac" |
| Secondary CTA | 동사 2단어 | "Learn More" / "Sign Up" |
| Subheading | 제품 설명 한 문장, 기능 중심 | "A modern terminal for agentic coding" |
| Tone | 기술적 자신감, 미니멀, 형용사 최소화 | -- |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Warp (marketing site) -- 프로젝트 루트 스타일시트에 복사 */
:root {
  /* Fonts */
  --warp-font-family:       "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
  --warp-font-family-display: "Matter Regular", "Inter", sans-serif;
  --warp-font-family-code:  "Geist Mono", "Fragment Mono", ui-monospace, monospace;
  --warp-font-weight-normal: 400;
  --warp-font-weight-medium: 500;
  --warp-font-weight-bold:   600;

  /* Surfaces */
  --warp-bg-page:    #FAF9F6;   /* cream ivory */
  --warp-bg-card:    #FFFFFF;   /* card surface */
  --warp-bg-dark:    #121212;   /* dark section */
  --warp-text:       #000000;   /* primary text */
  --warp-text-muted: #666469;   /* muted text */
  --warp-text-quiet: #999999;   /* placeholder */

  /* Borders */
  --warp-border:       #E3E2E0;
  --warp-border-muted: #AFAEAC;
  --warp-border-dark:  rgba(255,255,255,0.16);   /* #FFFFFF29 */

  /* Key spacing */
  --warp-space-xs:  8px;
  --warp-space-sm:  12px;
  --warp-space-md:  16px;
  --warp-space-lg:  24px;
  --warp-space-xl:  32px;

  /* Radius */
  --warp-radius-sm: 6px;
  --warp-radius-md: 8px;
  --warp-radius-lg: 10px;
}

body {
  font-family: var(--warp-font-family);
  font-weight: var(--warp-font-weight-normal);
  background: var(--warp-bg-page);
  color: var(--warp-text);
}

h1, h2, h3 {
  font-weight: var(--warp-font-weight-normal);   /* 400 -- Matter/Inter 기반 */
  letter-spacing: -0.01em;
}
h1 { letter-spacing: -0.02em; }
strong, b { font-weight: var(--warp-font-weight-bold); }   /* 600 */
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js -- Warp (marketing site)
module.exports = {
  theme: {
    extend: {
      colors: {
        cream: {
          DEFAULT: '#FAF9F6',
          50: '#FAF9F5',
        },
        neutral: {
          0:   '#FFFFFF',
          100: '#E3E2E0',
          200: '#AFAEAC',
          300: '#999999',
          400: '#868584',
          500: '#666469',
          600: '#454545',
          700: '#353534',
          800: '#2B2B2B',
          850: '#232224',
          900: '#1A1A1A',
          950: '#121212',
          1000: '#000000',
        },
      },
      fontFamily: {
        sans: ['"Inter"', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
        display: ['"Matter Regular"', '"Inter"', 'sans-serif'],
        mono: ['"Geist Mono"', '"Fragment Mono"', '"DM Mono"', 'ui-monospace'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
        semibold: '600',
        bold: '700',
        black: '900',
      },
      borderRadius: {
        xs: '5px',
        sm: '6px',
        md: '8px',
        lg: '10px',
        xl: '20px',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO
- 페이지 배경을 `#FAF9F6` 따뜻한 크림 아이보리로. 순백 `#FFFFFF` 가 아니다.
- 본문 텍스트를 순수 `#000000` 검정으로. 네이비나 다크 그레이가 아니다.
- CTA 버튼: 검은 배경 `#000000` + 크림 텍스트 `#FAF9F6`, radius 6px
- 헤드라인은 `Matter Regular` 400 or `Inter` 400 -- 볼드(700)가 아님
- Mono 폰트는 `Geist Mono` -- Hack 이나 Fira Code 가 아님
- 전체 디자인을 **monochrome** (흑백+회색)으로 유지. 채도 있는 색은 제품 스크린샷 안에서만.
- 다크 섹션은 `#121212` 로. 순수 `#000` 이 아니다.
- radius 는 작게: 버튼 6px, 카드 8~10px, 대형 컨테이너만 20px
- Framer CSS 변수 네임스페이스 `--framer-*` 를 사용할 수 있다 (호스팅 플랫폼)
- Matter 폰트 라이선스 없으면 Inter 로 통일 -- fallback chain 에 맡기면 FOUT 발생

### DON'T
- 배경을 다크(`#0E0E10`) 로 두지 마라 -- 터미널 앱 UI 와 마케팅 사이트를 혼동하는 가장 흔한 실수
- cyan `#01A4FF` 를 브랜드 악센트로 쓰지 마라 -- 이 색은 앱 UI 전용이고 마케팅 CSS 에는 존재하지 않는다 (0회)
- 코드 폰트를 `Hack` 으로 두지 마라 -- 실제 사이트에 0회 등장. Geist Mono 가 정답
- 헤드라인을 `font-weight: 700` 이상으로 두지 마라 -- Warp 헤드라인은 400~500 이 기본
- 버튼에 그래디언트나 섀도우를 넣지 마라 -- Warp CTA 는 flat black/white, 장식 없음
- 카드에 두꺼운 보더나 큰 shadow 를 넣지 마라 -- flat/borderless 디자인
- 채도 높은 컬러 팔레트를 만들지 마라 -- Warp 마케팅은 22개 hex 중 채도 있는 색이 0개
- 순백 `#FFFFFF` 를 페이지 배경으로 쓰지 마라 -- warm cream `#FAF9F6` 과 시각적으로 다르다
