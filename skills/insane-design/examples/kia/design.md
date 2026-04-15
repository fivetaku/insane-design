---
slug: kia
service_name: Kia
site_url: https://www.kia.com/kr/
fetched_at: 2026-04-13
default_theme: light
brand_color: "#05141F"
primary_font: Kia Signature
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Kia (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Kia의 디자인은 클린한 밝은 배경 위에 브랜드 컬러 `#05141F`를 절제적으로 배치하는 미니멀 접근을 취한다. 여백과 타이포그래피의 힘으로 콘텐츠를 전달하며, 불필요한 장식을 배제한 실용적 우아함이 특징이다.

색상 전략은 철저히 절제적이다. 주요 컬러는 #05141F, #37434B, #005CB2, #FFFFFF이며, 뉴트럴 톤이 대부분의 UI 표면을 차지한다. 브랜드 컬러는 CTA 버튼과 핵심 강조 요소에만 사용되어 사용자의 시선을 정확히 유도한다.

타이포그래피는 `Kia Signature`을 중심으로 구축된다. weight 400이 기본으로, 안정적이고 균형 잡힌 가독성을 제공한다. 제목과 본문 사이의 weight 대비로 시각적 계층을 명확히 한다.

레이아웃은 넉넉한 여백과 명확한 섹션 구분으로 콘텐츠에 호흡을 부여한다. 전반적으로 정보 밀도보다 시각적 여유를 우선시하며, 이는 Kia 브랜드의 자신감과 품격을 반영한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Kia처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Kia Signature Regular", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #05141F; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #05141F; }
```

**절대 하지 말아야 할 것 하나**: `Kia Signature Bold`와 `Kia Signature Regular`를 하나의 family weight로 처리하는 것. Kia는 bold/regular를 **완전히 다른 font-family 이름**으로 선언한다(`Kia Signature Bold` vs `Kia Signature Regular`). `font-weight: bold`로 변환하면 폰트 렌더링이 깨진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.kia.com/kr/` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | 다수 외부 CSS |
| Token prefix | `--dp-primary-color` (날짜 피커 전용) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: 전통 HTML + CSS (글로벌 자동차 브랜드 사이트)
- **Design system**: Kia 전용 — `Kia Signature` 폰트 패밀리 중심
- **CSS architecture**: 컴포넌트별 플랫 CSS
  ```
  global reset + base
  component (btn, pnlm 파노라마 뷰어 등)
  page-specific overrides
  ```
- **Class naming**: BEM (`.btn-primary`, `.btn-primary:hover`, `.btn-primary:disabled`)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 자체 호스팅 (`Kia Signature Bold`, `Kia Signature Regular`, `Kia Signature Light`)
- **Canonical anchor**: `#05141F` — primary 버튼 배경, Kia의 near-black navy

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Kia Signature Bold` (기아 전용, 유료)
- **Body font**: `Kia Signature Regular` (기아 전용, 유료)
- **Light variant**: `Kia Signature Light`
- **Weight normal / bold**: `400` (Regular) / N/A (Bold = 별도 family)

```css
:root {
  --kia-font-bold: "Kia Signature Bold", Arial, sans-serif;
  --kia-font-regular: "Kia Signature Regular", Arial, sans-serif;
  --kia-font-light: "Kia Signature Light", Arial, sans-serif;
}
body {
  font-family: var(--kia-font-regular);
}
h1, h2, .btn-primary {
  font-family: var(--kia-font-bold);
}
```

> **중요**: Kia Signature는 별도 family명으로 weight를 구분. `font-weight` 속성이 아닌 `font-family` 변경으로 굵기 전환.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> ⚠️ CSS에 명시적 타이포 스케일 토큰이 없음. 컴포넌트별 리터럴 값 사용.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| btn-primary | 14px | Bold (family) | 1 | N/A |

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| brand-primary | `#05141F` |
| brand-hover | `#37434B` |
| dp-primary | `#005CB2` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white | `#FFFFFF` | — |
| text | `#05141F` | — |
| hover-dark | `#37434B` | — |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| --dp-primary-color | `#005CB2` | 날짜 피커 primary |
| --dp-primary-disabled-color | `#61A8EA` | 날짜 피커 disabled |
| btn-primary-bg | `#05141F` | 기본 CTA 버튼 배경 |
| btn-primary-hover-after | `#37434B` | 호버 슬라이드 효과 배경 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| btn-px | 24px | 버튼 좌우 패딩 |
| btn-min-w | 88px | 버튼 최소 너비 |

**주요 alias**:
- 버튼 패딩: `1pc 24px` (16px 세로, 24px 가로)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| pnlm-button | 3px | 파노라마 뷰어 버튼 |

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

### Button — Primary (`.btn-primary`)

```html
<button class="btn-primary">시승 신청</button>
```

| 속성 | 값 |
|---|---|
| background-color | `#05141F` |
| border | 1px solid `#05141F` |
| color | `#FFFFFF` |
| font-family | `Kia Signature Bold`, Arial, sans-serif |
| font-size | 14px |
| line-height | 1 |
| min-width | 88px |
| padding | 1pc 24px |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Kia — copy into your root stylesheet */
:root {
  /* Fonts */
  --kia-font-bold: "Kia Signature Bold", Arial, sans-serif;
  --kia-font-regular: "Kia Signature Regular", Arial, sans-serif;
  --kia-font-light: "Kia Signature Light", Arial, sans-serif;

  /* Brand */
  --kia-color-brand: #05141F;
  --kia-color-hover: #37434B;
  --kia-color-dp-primary: #005CB2;

  /* Surfaces */
  --kia-bg-page: #FFFFFF;
  --kia-text: #05141F;

  /* Key spacing */
  --kia-btn-min-w: 88px;
  --kia-btn-px: 24px;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#05141F` |
| Background | bg-page | `#FFFFFF` |
| Text primary | text | `#05141F` |
| Text muted | text-muted | `#666666` |
| Border | border | `#05141F` |

### Example Component Prompts

#### Hero Section
```
Kia 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: Kia Signature, weight 400
- CTA 버튼: 배경 #05141F, radius 4px
```

#### Card Component
```
Kia 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF, border: 1px solid #05141F
- 제목: Kia Signature, weight bold
- 본문: color #05141F, line-height 1.6
```

#### Button
```
Kia 스타일 버튼을 만들어줘.
- 배경: #05141F, 텍스트: white
- font: Kia Signature, weight 500-600
- padding: 12px 24px, radius: 4px
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

### ✅ DO
- 버튼 굵기는 `font-family: "Kia Signature Bold"`로 지정 (weight 속성 아님)
- CTA 버튼 배경은 `#05141F` near-black navy
- 버튼 hover에 `#37434B` slide 효과 사용 (::after 슬라이드 패턴)
- 최소 너비 88px 이상 버튼 사이즈 유지

### ❌ DON'T
- `font-weight: bold`로 기아 폰트 굵게 만들기 — `Kia Signature Bold`를 별도 family로 선언해야 함
- CTA에 파란색 버튼 사용 — 기아 primary는 near-black
- `--dp-primary-color`(`#005CB2`)를 전체 브랜드 색으로 사용 — 날짜 피커 전용
