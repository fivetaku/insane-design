---
slug: ferrari
service_name: Ferrari
site_url: https://ferrari.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#DA0000"
primary_font: N/A
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Ferrari (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Ferrari의 디자인은 클린한 밝은 배경 위에 브랜드 컬러 `#DA0000`를 절제적으로 배치하는 미니멀 접근을 취한다. 여백과 타이포그래피의 힘으로 콘텐츠를 전달하며, 불필요한 장식을 배제한 실용적 우아함이 특징이다.

색상 전략은 철저히 절제적이다. 주요 컬러는 #DA0000이며, 뉴트럴 톤이 대부분의 UI 표면을 차지한다. 브랜드 컬러는 CTA 버튼과 핵심 강조 요소에만 사용되어 사용자의 시선을 정확히 유도한다.

타이포그래피는 시스템 폰트를 전략적으로 활용한다. `font-weight: 400`을 기본으로 두어 정보 전달에 최적화된 가독성을 확보하며, 폰트 로딩 없이도 크로스 플랫폼 일관성을 유지한다.

레이아웃은 넉넉한 여백과 명확한 섹션 구분으로 콘텐츠에 호흡을 부여한다. 전반적으로 정보 밀도보다 시각적 여유를 우선시하며, 이는 Ferrari 브랜드의 자신감과 품격을 반영한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Ferrari처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Neue Haas Grotesk", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #1A1A1A; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #DA0000; }
```

**절대 하지 말아야 할 것 하나**: Ferrari 레드를 UI 전반에 과용하는 것. Ferrari 마케팅 사이트는 극도로 절제된 레이아웃을 사용하며 레드는 로고와 핵심 accent에만 나타난다. CSS 파싱에서 어떤 chromatic 컬러도 감지되지 않을 만큼 레드는 절제되어 있다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://ferrari.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | N/A |
| Token prefix | N/A — 커스텀 프로퍼티 시스템 미감지 |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

> **참고**: Ferrari 사이트의 CSS 파싱 결과 어떤 chromatic 후보도, font-family도 감지되지 않음. 사이트가 고도로 인라인화 또는 JS 렌더링 방식이라 정적 CSS 파싱이 제한됨.

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (자체 플랫폼)
- **Design system**: Ferrari 내부 디자인 시스템 (미공개)
- **CSS architecture**: N/A (토큰 시스템 미노출)
- **Class naming**: N/A
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: N/A (CSS에서 미감지)
- **Canonical anchor**: N/A (CSS 데이터 없음)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: N/A (CSS에서 미감지)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

> **참고**: CSS 파싱에서 font-family가 전혀 감지되지 않음. 시각적으로 Ferrari 사이트는 sans-serif 계열을 사용하는 것으로 관찰되나 CSS 데이터 기반 확인 불가.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> N/A — CSS에서 typography scale 토큰이 추출되지 않음.

---

## 06. Colors
<!-- SOURCE: auto -->

> N/A — CSS 파싱에서 어떤 color 후보도 감지되지 않음.

> **참고**: Ferrari 마케팅 사이트의 CSS는 정적 파싱으로 컬러 정보를 추출할 수 없었음. 브랜드 레드는 Rosso Corsa(`#DA0000`)로 알려져 있으나 이는 CSS 데이터가 아닌 공개 브랜드 정보.

---

## 07. Spacing
<!-- SOURCE: auto -->

> N/A — spacing 토큰이 CSS에서 추출되지 않음.

---

## 08. Radius
<!-- SOURCE: auto -->

> N/A — radius 토큰이 CSS에서 추출되지 않음.

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
<!-- SOURCE: manual -->

### Hero Section

```html
<section class="hero">
  <div class="hero__media">
    <!-- 차량 전체 폭 영상 또는 사진 -->
  </div>
  <div class="hero__overlay">
    <h1>Ferrari SF90 Stradale</h1>
    <a href="#" class="cta">Discover</a>
  </div>
</section>
```

| 속성 | 값 |
|---|---|
| hero 배경 | 차량 전체 폭 영상/사진 |
| 오버레이 | 그라디언트 (어두운 → 투명) |
| H1 색상 | `#FFFFFF` |
| CTA 배경 | `#DA0000` 또는 `transparent + white border` |

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 모델명 전체, 이탤릭 없이 | "Ferrari SF90 Stradale" |
| Primary CTA | 발견 유도 | "Discover" / "Configure" |
| Secondary CTA | 탐색 | "Find a Dealer" |
| Subheading | 퍼포먼스 수치 | "1000 hp · V8 hybrid" |
| Tone | 열정적이나 절제됨, 이탈리안 프리미엄 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Ferrari — copy into your root stylesheet */
/* ⚠️ CSS 파싱 데이터 없음. 브랜드 가이드라인 기반 추정값 */
:root {
  /* Fonts (CSS 미감지 — 시각 관찰 기반) */
  --ferrari-font-family: "Neue Haas Grotesk", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --ferrari-font-weight-normal: 400;
  --ferrari-font-weight-bold: 700;

  /* Brand (공개 브랜드 가이드 — CSS 미확인) */
  --ferrari-color-rosso-corsa: #DA0000;

  /* Surfaces */
  --ferrari-bg-page: #FFFFFF;
  --ferrari-bg-dark: #1A1A1A;
  --ferrari-text: #1A1A1A;
  --ferrari-text-on-dark: #FFFFFF;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#DA0000` |
| Background | bg-page | `#FFFFFF` |
| Text primary | text | `#1A1A1A` |
| Text muted | text-muted | `#666666` |
| Border | border | `#E0E0E0` |

### Example Component Prompts

#### Hero Section
```
Ferrari 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: N/A, weight 400
- CTA 버튼: 배경 #DA0000, radius 4px
```

#### Card Component
```
Ferrari 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF, border: 1px solid #E0E0E0
- 제목: N/A, weight bold
- 본문: color #1A1A1A, line-height 1.6
```

#### Button
```
Ferrari 스타일 버튼을 만들어줘.
- 배경: #DA0000, 텍스트: white
- font: N/A, weight 500-600
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
- Ferrari 레드를 로고, 주요 CTA에만 절제적으로 사용
- Hero는 차량 전체 폭 고화질 사진/영상으로 채우기
- 레이아웃 최대한 여백 넓게, 그리드 정교하게
- 모델명을 그대로 headline으로 사용

### ❌ DON'T
- Ferrari 레드를 배경 전체에 쓰지 말 것
- 과장된 마케팅 문구 쓰지 말 것
- CSS 데이터 없는 값을 확정적으로 사용하지 말 것
- 레이아웃을 복잡하게 만들지 말 것 — 미니멀이 핵심
