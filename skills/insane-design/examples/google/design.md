---
slug: google
service_name: Google
site_url: https://google.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#1A73E8"
primary_font: Google Sans
font_weight_normal: 400
token_prefix: --md-ref-palette-*
---

# DESIGN.md — Google (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Google의 디자인은 클린한 밝은 배경 위에 브랜드 컬러 `#1A73E8`를 절제적으로 배치하는 미니멀 접근을 취한다. 여백과 타이포그래피의 힘으로 콘텐츠를 전달하며, 불필요한 장식을 배제한 실용적 우아함이 특징이다.

색상 전략은 철저히 절제적이다. 주요 컬러는 #00102D, #202124, #002E68, #174EA6이며, 뉴트럴 톤이 대부분의 UI 표면을 차지한다. 브랜드 컬러는 CTA 버튼과 핵심 강조 요소에만 사용되어 사용자의 시선을 정확히 유도한다.

타이포그래피는 `Google Sans`을 중심으로 구축된다. weight 400이 기본으로, 안정적이고 균형 잡힌 가독성을 제공한다. 제목과 본문 사이의 weight 대비로 시각적 계층을 명확히 한다.

레이아웃은 넉넉한 여백과 명확한 섹션 구분으로 콘텐츠에 호흡을 부여한다. 전반적으로 정보 밀도보다 시각적 여유를 우선시하며, 이는 Google 브랜드의 자신감과 품격을 반영한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Google처럼 만들기 — 3가지만 하면 80%

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

**절대 하지 말아야 할 것 하나**: 텍스트를 `#000000`(순흑)으로 두는 것. Google UI 텍스트의 primary 값은 `#202124`(거의 검정이지만 따뜻한 dark gray)다. 순흑으로 쓰면 Google의 부드럽고 명랑한 느낌이 무너진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://google.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | Google 자체 SSR |
| CSS files | Material Design 3 토큰 + Google Sans 폰트 |
| Token prefix | `--md-ref-palette-*` (Material Design 3) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Google 자체 서버 렌더링 (Lit / Polymer 기반 추정)
- **Design system**: Material Design 3 (MD3) — prefix `--md-ref-palette-*`
- **CSS architecture**: Material Design 3 색상 시스템
  ```
  ref-palette  (--md-ref-palette-primary*)   raw hex 팔레트
  sys-color    (--md-sys-color-*)            semantic alias
  component    (--md-comp-*)                 컴포넌트별 조합
  ```
- **Class naming**: 유틸리티 + 컴포넌트 클래스 혼합
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: Google Fonts CDN (Google Sans, Google Sans Text, Product Sans, Roboto Mono)
- **Canonical anchor**: `#1A73E8` — `--md-ref-palette-primary50`에 정의된 Google Blue

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Google Sans` (구글 전용, Google Fonts CDN)
- **Body font**: `Google Sans Text` (본문용 최적화 버전)
- **Code font**: `Consolas, Monaco, Bitstream Vera Sans Mono, Courier New, monospace`
- **Weight normal / bold**: `400` / `500`

```css
:root {
  --font-family: "Google Sans Text", Arial, Helvetica, sans-serif;
  --font-family-display: "Google Sans", Arial, Helvetica, sans-serif;
  --font-family-code: Consolas, Monaco, "Courier New", monospace;
  --font-weight-normal: 400;
  --font-weight-bold: 500;
}
body {
  font-family: var(--font-family);
  font-weight: var(--font-weight-normal);
}
```

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| body-sm | 0.875rem | 400 | 1.43 | 0 |
| body | 1rem | 400 | 1.5 | 0 |
| label | 0.75rem | 500 | 1.33 | 0.025em |
| title-sm | 0.875rem | 500 | 1.43 | 0.0063em |
| title | 1rem | 500 | 1.5 | 0.009375em |
| headline | 1.5rem | 400 | 1.33 | 0 |
| display | 2.8125rem | 400 | 1.13 | -0.015625em |

> ⚠️ Material Design 3의 type scale을 따른다. heading은 weight 400이 많고, label/title 계열만 500이다. 일반적인 "heading = bold" 규칙과 다르다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (Material Design 3 primary palette)

| Token | Hex |
|---|---|
| `--md-ref-palette-primary5` | `#00102D` |
| `--md-ref-palette-primary10` | `#202124` |
| `--md-ref-palette-primary20` | `#002E68` |
| `--md-ref-palette-primary30` | `#174EA6` |
| `--md-ref-palette-primary35` | `#185ABC` |
| `--md-ref-palette-primary40` | `#1967D2` |
| `--md-ref-palette-primary50` | `#1A73E8` ⭐ **canonical** |
| `--md-ref-palette-primary60` | `#4285F4` |
| `--md-ref-palette-primary70` | `#669DF6` |
| `--md-ref-palette-primary80` | `#8AB4F8` |
| `--md-ref-palette-primary90` | `#AECBFA` |
| `--md-ref-palette-primary95` | `#D2E3FC` |
| `--md-ref-palette-primary98` | `#E8F0FE` |

### 06-3. Neutral Ramp

| Step | Hex |
|---|---|
| 100 | `#FFFFFF` |
| 99 | `#FAFAFA` |
| primary10 (dark fg) | `#202124` |
| primary0 | `#000000` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--md-ref-palette-primary50` | `#1A73E8` | CTA 버튼, 링크 |
| `--md-ref-palette-primary60` | `#4285F4` | 보조 강조 |
| fg-primary | `#202124` | 본문 텍스트 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| Material base | 4px grid | MD3 권장 4px 그리드 |
| component-md | 16px | 버튼, 카드 내부 |
| section | 32px | 섹션 간격 |

**주요 alias**:
- MD3 표준 → 4px 배수 (4, 8, 12, 16, 24, 32, 48px)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| btn | 20px | 버튼 (pill-ish) |
| card | 8px | 카드 |
| chip | 8px | 필터 chip |

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | < 768px | 단일 컬럼, 터치 최적화 |
| Tablet | 768px–1024px | 2컬럼 그리드, 축소된 여백 |
| Desktop | 1024px–1440px | 전체 레이아웃, 다중 컬럼 |
| Large | > 1440px | max-width 고정, 좌우 auto margin |

### Touch Targets
- **Minimum tap size**: 44×44px (WCAG 2.5.5)
- **Button height (mobile)**: 48px
- **Input height (mobile)**: 48px

### Collapsing Strategy
- **Navigation**: 모바일에서 축소/햄버거 메뉴 전환
- **Grid columns**: desktop 다중 컬럼 → mobile 단일 컬럼
- **Hero layout**: 이미지+텍스트 분할 → 모바일에서 수직 스택

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Button — Primary (Filled)

```html
<button class="gm3-filled-button" type="button">
  Google 검색
</button>
```

| Spec | Value |
|---|---|
| background | `#1A73E8` |
| color | `#FFFFFF` |
| font-weight | 500 |
| border-radius | 20px |
| height | 40px |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Google — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: "Google Sans Text", Arial, Helvetica, sans-serif;
  --font-family-display: "Google Sans", Arial, Helvetica, sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold: 500;

  /* Brand (MD3 primary ramp) */
  --brand-95: #D2E3FC;
  --brand-80: #8AB4F8;
  --brand-60: #4285F4;
  --brand-50: #1A73E8;   /* ← canonical */
  --brand-40: #1967D2;
  --brand-10: #202124;

  /* Surfaces */
  --bg-page: #FFFFFF;
  --bg-dark: #202124;
  --text: #202124;
  --text-muted: #5F6368;

  /* Key spacing */
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 32px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-btn: 20px;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#1A73E8` |
| Background | bg-page | `#FFFFFF` |
| Text primary | text | `#202124` |
| Text muted | text-muted | `#5F6368` |
| Border | border | `#E0E0E0` |

### Example Component Prompts

#### Hero Section
```
Google 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: Google Sans, weight 400
- CTA 버튼: 배경 #1A73E8, radius 20px
```

#### Card Component
```
Google 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF, border: 1px solid #E0E0E0
- 제목: Google Sans, weight bold
- 본문: color #202124, line-height 1.6
```

#### Button
```
Google 스타일 버튼을 만들어줘.
- 배경: #1A73E8, 텍스트: white
- font: Google Sans, weight 500-600
- padding: 12px 24px, radius: 20px
```

### Iteration Guide

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight 400이 기본. bold는 제목/강조에만.
- **여백 조정 시**: §07의 spacing scale 단위로만. 임의 값(13px, 27px 등) 금지.
- **새 컴포넌트 추가 시**: §13의 기존 패턴(radius, shadow, border 스타일)을 따를 것.
- **반응형**: §12의 breakpoint를 그대로 사용. 커스텀 breakpoint 추가 금지.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO
- 텍스트는 `#202124`를 써라 — 순흑이 아닌 Google의 따뜻한 dark gray다.
- 브랜드 블루는 `#1A73E8`(primary50)을 써라.
- `font-weight: 500`은 label/title 계열에만 써라 — 본문은 400이다.
- MD3 4px 그리드 배수를 지켜라 (4, 8, 12, 16, 24, 32px).
- 버튼은 `border-radius: 20px`(pill-ish)으로 써라.

### DON'T
- 텍스트를 `#000000`으로 두지 마라 — Google은 `#202124`를 쓴다.
- `#4285F4`를 primary로 착각하지 마라 — primary60이며, 실제 CTA anchor는 `#1A73E8`이다.
- heading에 `font-weight: 700`을 쓰지 마라 — MD3 headline은 400이다.
- 버튼 radius를 0으로 두지 마라 — Google 버튼은 둥글다(20px).
- `Roboto`를 기본 폰트로 쓰지 마라 — Google 마케팅 사이트는 `Google Sans Text`가 기본이다.
