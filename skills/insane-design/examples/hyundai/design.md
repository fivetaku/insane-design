---
slug: hyundai
service_name: Hyundai
site_url: https://www.hyundai.com/kr/ko/
fetched_at: 2026-04-13
default_theme: light
brand_color: "#007FA8"
primary_font: HyundaiSansTextKR
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Hyundai (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Hyundai의 디자인은 클린한 밝은 배경 위에 브랜드 컬러 `#007FA8`를 절제적으로 배치하는 미니멀 접근을 취한다. 여백과 타이포그래피의 힘으로 콘텐츠를 전달하며, 불필요한 장식을 배제한 실용적 우아함이 특징이다.

색상 전략은 철저히 절제적이다. 주요 컬러는 #007FA8, #FFFFFF, #F4F4F5, #303133이며, 뉴트럴 톤이 대부분의 UI 표면을 차지한다. 브랜드 컬러는 CTA 버튼과 핵심 강조 요소에만 사용되어 사용자의 시선을 정확히 유도한다.

타이포그래피는 `HyundaiSansTextKR`을 중심으로 구축된다. weight 400이 기본으로, 안정적이고 균형 잡힌 가독성을 제공한다. 제목과 본문 사이의 weight 대비로 시각적 계층을 명확히 한다.

레이아웃은 넉넉한 여백과 명확한 섹션 구분으로 콘텐츠에 호흡을 부여한다. 전반적으로 정보 밀도보다 시각적 여유를 우선시하며, 이는 Hyundai 브랜드의 자신감과 품격을 반영한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Hyundai처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "HyundaiSansTextKR", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #303133; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #007FA8; }
```

**절대 하지 말아야 할 것 하나**: Element UI(`el-*`) 기본 파랑(`#409EFF`)을 현대 브랜드 색으로 착각하는 것. `#409EFF`는 Element UI 컴포넌트 라이브러리의 기본값이고, 실제 현대 브랜드 액티브 색은 `#007FA8`이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.hyundai.com/kr/ko/` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | 다수 외부 CSS (Element UI 포함) |
| Token prefix | N/A (Element UI 컴포넌트 기반) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Vue.js + Element UI (CSS 클래스 `el-*` 패턴으로 확인)
- **Design system**: Element UI 기반 커스텀 — `el-*` prefix
- **CSS architecture**: Element UI 컴포넌트 CSS + 현대 커스텀 오버라이드
  ```
  element-ui global (--el-color-primary 등)
  hyundai-custom (브랜드 오버라이드)
  page-specific
  ```
- **Class naming**: Element UI 패턴 (`el-pagination`, `el-dialog`, `el-radio-button`)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 자체 호스팅 (`HyundaiSansTextKR`, `HyundaiSansHeadKR`)
- **Canonical anchor**: `#007FA8` — 페이지네이션 액티브 색, 현대 teal 브랜드

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `HyundaiSansHeadKR` (현대 전용 헤드라인용)
- **Body font**: `HyundaiSansTextKR` (현대 전용 본문용)
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-family-head: "HyundaiSansHeadKR", sans-serif;
  --font-family-text: "HyundaiSansTextKR", sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold: 700;
}
body {
  font-family: var(--font-family-text);
  font-weight: var(--font-weight-normal);
}
```

> 한글 전용 폰트로 한국 현대 사이트에서만 사용. 대체재: `Noto Sans KR` (weight 400/700).

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> ⚠️ CSS에 명시적 타이포 스케일 토큰이 없음. Element UI 기본값과 현대 커스텀이 혼재.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| body | 14px | 400 | 1.5 | N/A |
| heading | N/A | 700 | N/A | N/A |

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| brand-active | `#007FA8` |
| brand-hover | N/A |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| bg-white | `#FFFFFF` | — |
| bg-muted | `#F4F4F5` | — |
| text-primary | `#303133` | — |
| text-secondary | `#606266` | — |
| text-placeholder | `#909399` | — |
| text-disabled | `#C0C4CC` | — |
| border-base | `#DCDFE6` | — |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| el-color-primary | `#409EFF` | Element UI 기본값 (현대 브랜드 아님) |
| hyundai-active | `#007FA8` | 현대 브랜드 액티브 색 |
| el-color-disabled | `#C0C4CC` | 비활성 |
| el-border | `#DCDFE6` | 기본 테두리 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| pager-item-margin | 5px | 페이지네이션 아이템 간격 |
| pager-item-min-w | 30px | 페이지네이션 최소 너비 |

**주요 alias**:
- Element UI 기본 5px 그리드 기반

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| el-pager | 4px | Element UI 페이지네이션 |
| el-dialog | 4px | 다이얼로그 |

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

### Pagination — Active (`.el-pager li.active`)

```html
<ul class="el-pager">
  <li class="active">1</li>
</ul>
```

| 속성 | 값 |
|---|---|
| color | `#007FA8` |
| cursor | default |

### Radio Button — Checked (`.el-radio-button__orig-radio:checked + .el-radio-button__inner`)

```html
<div class="el-radio-button">
  <input class="el-radio-button__orig-radio" type="radio" checked>
  <span class="el-radio-button__inner">선택</span>
</div>
```

| 속성 | 값 |
|---|---|
| color | `#FFFFFF` |
| background-color | `#409EFF` |
| border-color | `#409EFF` |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Hyundai — copy into your root stylesheet */
:root {
  /* Fonts */
  --hyundai-font-head: "HyundaiSansHeadKR", sans-serif;
  --hyundai-font-text: "HyundaiSansTextKR", sans-serif;
  --hyundai-font-weight-normal: 400;
  --hyundai-font-weight-bold: 700;

  /* Brand */
  --hyundai-color-brand: #007FA8;
  --hyundai-color-el-primary: #409EFF;

  /* Surfaces */
  --hyundai-bg-page: #FFFFFF;
  --hyundai-bg-muted: #F4F4F5;
  --hyundai-text: #303133;
  --hyundai-text-muted: #909399;

  /* Borders */
  --hyundai-border: #DCDFE6;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#007FA8` |
| Background | bg-page | `#FFFFFF` |
| Text primary | text | `#303133` |
| Text muted | text-muted | `#F4F4F5` |
| Border | border | `#DCDFE6` |

### Example Component Prompts

#### Hero Section
```
Hyundai 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: HyundaiSansTextKR, weight 400
- CTA 버튼: 배경 #007FA8, radius 4px
```

#### Card Component
```
Hyundai 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF, border: 1px solid #DCDFE6
- 제목: HyundaiSansTextKR, weight bold
- 본문: color #303133, line-height 1.6
```

#### Button
```
Hyundai 스타일 버튼을 만들어줘.
- 배경: #007FA8, 텍스트: white
- font: HyundaiSansTextKR, weight 500-600
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
- 브랜드 액티브 색으로 `#007FA8` 사용
- 헤드라인에 `HyundaiSansHeadKR`, 본문에 `HyundaiSansTextKR` 구분 사용
- Element UI 기반 컴포넌트 패턴 유지 (`el-*` 클래스)
- 중립 텍스트는 `#303133` (Element UI 기본 텍스트색)

### ❌ DON'T
- `#409EFF`를 현대 브랜드 색으로 사용 — Element UI 기본값이며 현대 브랜드 아님
- 헤드라인 폰트와 본문 폰트를 같은 폰트로 통일 — 현대는 Head/Text 명확히 구분
- 현대 웹 컴포넌트에서 라운드 버튼 남발 — 현대 스타일은 절제된 각도
