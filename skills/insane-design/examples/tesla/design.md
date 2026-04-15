---
slug: tesla
service_name: Tesla
site_url: https://tesla.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#CC0000"
primary_font: N/A
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Tesla (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Tesla의 디지털 인터페이스는 라이트 테마를 기본으로 한다. 밝은 배경 위에 브랜드 컬러 `#CC0000`가 절제적으로 사용되어 깔끔하고 신뢰감 있는 시각적 인상을 만든다.

색상 전략은 `#CC0000`, `#F4F4F4`, `#000000` 등을 중심으로 구성된다. 브랜드의 canonical 컬러인 `#CC0000`가 CTA와 주요 인터랙션 요소에 사용되며, 나머지 뉴트럴 팔레트가 배경과 텍스트 계층을 형성한다.

타이포그래피는 시스템 폰트를 활용하여 로딩 성능과 플랫폼 일관성을 우선시한다. weight 400을 기본으로 하며, heading과 body 사이 명확한 위계를 유지한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Tesla처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Gotham SSm A", "Gotham SSm B", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #F4F4F4; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #CC0000; }
```

**절대 하지 말아야 할 것 하나**: 배경을 순백 `#FFFFFF`로 두는 것. Tesla의 마케팅 사이트 배경은 `#F4F4F4`(밝은 회색)이고 차량 사진이 hero를 채운다. 순백 배경은 즉시 "일반 전자상거래" 느낌을 준다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://tesla.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | 인라인 중심 (토큰 시스템 미확인) |
| Token prefix | N/A — 커스텀 프로퍼티 시스템 미감지 |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React (Next.js 추정)
- **Design system**: 자체 내부 디자인 시스템 (토큰 prefix 미공개)
- **CSS architecture**: 인라인 스타일 + 최소 글로벌 CSS
- **Class naming**: N/A
- **Default theme**: light (bg = `#F4F4F4`)
- **Font loading**: N/A (CSS에서 font-family 미감지)
- **Canonical anchor**: `#CC0000` — 유일한 chromatic 후보

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: N/A (CSS에서 감지되지 않음)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

> **참고**: Tesla 마케팅 사이트의 CSS에서 font-family가 감지되지 않았다. 시각적으로는 Gotham SSm 계열로 관찰되나 CSS 파싱 데이터 기반으로 확인 불가.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> N/A — CSS에서 typography scale 토큰이 추출되지 않음.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp

| Token | Hex |
|---|---|
| 브랜드 레드 (chromatic 유일) | `#CC0000` |

### 06-3. Neutral Ramp

| Step | Hex | Count |
|---|---|---|
| 페이지 배경 | `#F4F4F4` | 8회 |
| 텍스트 / 배경 다크 | `#000000` | 1회 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| 페이지 배경 | `#F4F4F4` | body background |
| 텍스트 / 다크 배경 | `#000000` | 텍스트, 다크 섹션 배경 |
| 브랜드 레드 | `#CC0000` | accent, 로고 |

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
<!-- SOURCE: manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | 0–767px | 단일 컬럼, 스택 레이아웃 |
| Tablet | 768–1023px | 2컬럼 그리드, 축소된 네비게이션 |
| Desktop | 1024–1439px | 풀 레이아웃, 사이드바 표시 |
| Large | 1440px+ | 최대 너비 제한, 중앙 정렬 |

### Collapsing Strategy
- **Navigation**: 데스크톱 수평 메뉴 → 모바일 햄버거 메뉴
- **Grid columns**: 데스크톱 다중 컬럼 → 모바일 단일 컬럼 스택
- **Hero layout**: 데스크톱 가로 배치 → 모바일 세로 스택

---

## 13. Components
<!-- SOURCE: manual -->

### Hero Section

```html
<section class="hero">
  <div class="hero__media">
    <img src="vehicle.jpg" alt="Tesla Model S" />
  </div>
  <div class="hero__content">
    <h1>Model S</h1>
    <div class="hero__ctas">
      <a href="#" class="btn btn--order">주문하기</a>
      <a href="#" class="btn btn--demo">시승 신청</a>
    </div>
  </div>
</section>
```

| 속성 | 값 |
|---|---|
| 배경 | 차량 전체 폭 사진 |
| H1 색상 | `#FFFFFF` (다크 배경 위) 또는 `#000000` |
| CTA 배경 | `#000000` (주문하기) |
| CTA 색상 | `#FFFFFF` |

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 모델명만, 최소한의 수식 | "Model S" |
| Primary CTA | 직접 행동, 간결 | "주문하기" |
| Secondary CTA | 체험 유도 | "시승 신청" |
| Subheading | 스펙 수치 나열 | "제로백 1.99초" |
| Tone | 미니멀, 수치 중심, 과장 없음 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Tesla — copy into your root stylesheet */
:root {
  /* Fonts — CSS에서 미감지, 시각 관찰 기반 */
  --tesla-font-family: "Gotham SSm A", "Gotham SSm B", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --tesla-font-weight-normal: 400;
  --tesla-font-weight-bold: 700;

  /* Brand */
  --tesla-color-brand-red: #CC0000;

  /* Surfaces */
  --tesla-bg-page: #F4F4F4;
  --tesla-bg-dark: #000000;
  --tesla-text: #000000;
  --tesla-text-on-dark: #FFFFFF;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#CC0000` |
| Background | bg-page | `#F4F4F4` |
| Text primary | text | `#000000` |
| Text muted | text-muted | `#666666` |
| Border | border | `#E0E0E0` |

### Example Component Prompts

#### Hero Section
```
Tesla 스타일 히어로 섹션을 만들어줘.
- 배경: #F4F4F4
- H1: N/A, weight 700
- 서브텍스트: #666666
- CTA 버튼: 배경 #CC0000, 텍스트 white
```

#### Card Component
```
Tesla 스타일 카드 컴포넌트를 만들어줘.
- 배경: #F4F4F4, border: 1px solid #E0E0E0
- radius: 8px
- 제목: N/A, 16px, weight 700
- 본문: 14px, color #000000
```

### Iteration Guide

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight 400이 기본. heading에만 더 무거운 weight.
- **여백 조정 시**: §07의 spacing scale 단위로만. 임의 값(13px, 27px 등) 금지.
- **새 컴포넌트 추가 시**: §13의 기존 패턴(radius, shadow, border 스타일)을 따를 것.
- **반응형**: §12의 breakpoint를 그대로 사용. 커스텀 breakpoint 추가 금지.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 페이지 배경에 `#F4F4F4` 사용 (순백 아님)
- Hero는 차량 전체 폭 사진으로 채우기
- CTA 텍스트 최소화 ("주문하기", "시승 신청")
- H1은 모델명만, 수식어 없이
- 스펙 표현 시 실제 수치 명시 (초, km, kWh)

### ❌ DON'T
- 배경을 순백 `#FFFFFF`으로 쓰지 말 것
- 과장형 마케팅 문구 사용하지 말 것 ("혁신적인", "놀라운")
- CTA 버튼 색으로 레드 `#CC0000`을 쓰지 말 것 — 버튼은 블랙
- 레이아웃을 복잡하게 만들지 말 것 — 최대한 단순하게
