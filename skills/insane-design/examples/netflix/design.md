---
slug: netflix
service_name: Netflix
site_url: https://netflix.com
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#E50914"
primary_font: Netflix Sans
font_weight_normal: 400
token_prefix: --wct--*
---

# DESIGN.md — Netflix (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Netflix의 디자인은 다크 배경 위에 구축된 몰입형 시각 경험을 추구한다. 브랜드 컬러 `#E50914`를 절제된 포인트로 활용하며, 전반적으로 깊이감 있는 다크 톤이 서비스의 전문성과 프리미엄 감성을 전달한다.

색상 전략은 철저히 절제적이다. 주요 컬러는 #99161D, #E50914, #141414, #1A1A1A이며, 뉴트럴 톤이 대부분의 UI 표면을 차지한다. 브랜드 컬러는 CTA 버튼과 핵심 강조 요소에만 사용되어 사용자의 시선을 정확히 유도한다.

타이포그래피는 `Netflix Sans`을 중심으로 구축된다. weight 400이 기본으로, 안정적이고 균형 잡힌 가독성을 제공한다. 제목과 본문 사이의 weight 대비로 시각적 계층을 명확히 한다.

레이아웃은 넉넉한 여백과 명확한 섹션 구분으로 콘텐츠에 호흡을 부여한다. 전반적으로 정보 밀도보다 시각적 여유를 우선시하며, 이는 Netflix 브랜드의 자신감과 품격을 반영한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Netflix처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Netflix Sans", "Helvetica Neue", Segoe UI, Roboto, Ubuntu, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #141414; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #E50914; }
```

**절대 하지 말아야 할 것 하나**: 배경을 `#000000`(순흑)으로 두는 것. Netflix의 실제 배경은 `#141414`(따뜻한 다크)다. 순흑을 쓰면 Netflix 특유의 깊이감 있는 다크 분위기가 사라지고 단순한 검정 배경처럼 보인다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://netflix.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | Next.js SSR |
| CSS files | 인라인 CSS-in-JS + 셀프 호스트 Netflix Sans |
| Token prefix | `--wct--*` (Web Component Tokens) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js + CSS-in-JS (Emotion/styled-components 추정)
- **Design system**: Netflix Web DS — prefix `--wct--*`
- **CSS architecture**: Web Component Tokens
  ```
  wct  (--wct--focus-ring--color, --wct--focus-ring--width)  컴포넌트 토큰
  ```
- **Class naming**: CSS-in-JS 해시 클래스 (`default-ltr-iqcdef-cache-*`)
- **Default theme**: dark (bg = `#141414`)
- **Font loading**: `Netflix Sans` 셀프 호스트 + `Netflix Sans Variable`(가변 폰트)
- **Canonical anchor**: `#E50914` — frequency_candidates에서 7회 확인된 Netflix red

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Netflix Sans Variable` (가변 폰트, Netflix 전용)
- **Body font**: `Netflix Sans` (Netflix 전용)
- **Code font**: `monospace`
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-family: "Netflix Sans", "Helvetica Neue", "Segoe UI", Roboto, Ubuntu, sans-serif;
  --font-family-variable: "Netflix Sans Variable", "Netflix Sans", sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold: 700;
}
body {
  font-family: var(--font-family);
  font-weight: var(--font-weight-normal);
}
```

> **참고**: `Netflix Sans`는 Dalton Maag이 제작한 Netflix 전용 폰트. 재배포 불가. 대체재로는 `Barlow`나 `Bebas Neue`(heading)가 근접.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| caption | 0.75rem | 400 | 1.33 | 0 |
| body | 1rem | 400 | 1.5 | 0 |
| title | 1.25rem | 700 | 1.3 | 0 |
| heading | 1.5rem | 700 | 1.25 | -0.01em |
| display | 2.5rem | 900 | 1.1 | -0.02em |

> ⚠️ Netflix는 hero 디스플레이에 `font-weight: 900`을 쓴다. weight 100, 900이 모두 CSS에서 사용되는 특이한 구조 — 100은 초경량 메타 텍스트, 900은 히어로 타이틀용.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (Netflix Red)

| Token | Hex |
|---|---|
| brand-dark | `#99161D` |
| brand | `#E50914` ⭐ **canonical** |
| brand-light | N/A |

### 06-3. Neutral Ramp

| Step | Hex |
|---|---|
| bg | `#141414` |
| bg-card | `#1A1A1A` |
| border | `#A9A9A9` |
| fg | `#FFFFFF` |
| fg-muted | `#ECECEC` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--wct--focus-ring--color-default` | `#A9A9A9` | 기본 focus ring |
| brand | `#E50914` | 로고, CTA 버튼 |
| brand-dark | `#99161D` | hover, 다크 variant |
| border | `#ECECEC` | 섹션 구분선 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#A9A9A9` | 64 | focus ring |
| 2 | `#ECECEC` | 12 | 구분선 |
| 3 | `#E50914` | 7 | Netflix red |
| 4 | `#99161D` | 7 | red dark variant |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| focus-ring-width | 0.125rem | focus ring 두께 |
| btn-pad | 1.5rem | 버튼 패딩 |

**주요 alias**:
- `--wct--focus-ring--width` → 0.125rem (2px)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| btn | 4px | 일반 버튼 |
| card | 4px | 콘텐츠 카드 |

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

### Button — CTA (Watch Now)

```html
<button class="btn-cta" type="button">지금 시청하기</button>
```

| Spec | Value |
|---|---|
| background | `#E50914` |
| color | `#FFFFFF` |
| font-weight | 700 |
| border-radius | 4px |
| padding | 1rem 2rem |
| focus-ring | `0.125rem solid #A9A9A9` |

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 감각적이고 직접적. 동사형 | "Unlimited movies, TV shows, and more" |
| Primary CTA | 명확한 가치 제안 | "지금 시작하기" |
| Secondary CTA | 탐색 유도 | "더 알아보기" |
| Tone | 자신감 있고 엔터테인먼트적, 부드러운 urgency | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Netflix — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: "Netflix Sans", "Helvetica Neue", "Segoe UI", Roboto, Ubuntu, sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold: 700;

  /* Brand */
  --brand: #E50914;   /* ← canonical Netflix red */
  --brand-dark: #99161D;

  /* Surfaces */
  --bg-page: #141414;
  --bg-card: #1A1A1A;
  --text: #FFFFFF;
  --text-muted: #ECECEC;
  --border: #A9A9A9;

  /* Key spacing */
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 1.5rem;

  /* Radius */
  --radius-sm: 2px;
  --radius-md: 4px;

  /* Focus */
  --wct--focus-ring--width: 0.125rem;
  --wct--focus-ring--color-default: #A9A9A9;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#E50914` |
| Background | bg-page | `#141414` |
| Text primary | text | `#FFFFFF` |
| Text muted | text-muted | `#ECECEC` |
| Border | border | `#A9A9A9` |

### Example Component Prompts

#### Hero Section
```
Netflix 스타일 히어로 섹션을 만들어줘.
- 배경: #141414
- H1: Netflix Sans, weight 400
- CTA 버튼: 배경 #E50914, radius 4px
```

#### Card Component
```
Netflix 스타일 카드 컴포넌트를 만들어줘.
- 배경: #141414, border: 1px solid #A9A9A9
- 제목: Netflix Sans, weight bold
- 본문: color #FFFFFF, line-height 1.6
```

#### Button
```
Netflix 스타일 버튼을 만들어줘.
- 배경: #E50914, 텍스트: white
- font: Netflix Sans, weight 500-600
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

### DO
- 배경은 `#141414`를 써라 — 순흑이 아닌 Netflix의 따뜻한 다크 베이스다.
- 브랜드 레드는 `#E50914`를 써라 — Netflix canonical red다.
- hero/display 텍스트에 `font-weight: 900`을 써라.
- 버튼에 `focus-ring: 0.125rem`을 유지하라 — 접근성 원칙이다.
- 다크 배경에서 모든 텍스트는 `#FFFFFF`로 써라.

### DON'T
- 배경을 `#000000`으로 두지 마라 — Netflix는 `#141414`다.
- `#FF0000`(순빨강)을 쓰지 마라 — Netflix red는 `#E50914`다.
- 밝은 배경(라이트 테마)으로 구현하지 마라 — Netflix는 다크 테마 우선이다.
- `font-weight: 400`을 heading에 두지 마라 — heading/display는 700~900이다.
- svg pattern 색(`#FFF3EB`, `#E4A1FA`)을 UI 컬러로 쓰지 마라 — 콘텐츠 썸네일 내부 색이다.
