---
slug: medium
service_name: Medium
site_url: https://medium.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#1A8917"
primary_font: Sohne
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Medium (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Medium의 디자인은 클린한 밝은 배경 위에 브랜드 컬러 `#1A8917`를 절제적으로 배치하는 미니멀 접근을 취한다. 여백과 타이포그래피의 힘으로 콘텐츠를 전달하며, 불필요한 장식을 배제한 실용적 우아함이 특징이다.

색상 전략은 철저히 절제적이다. 주요 컬러는 #1A8917, #156012, #E6F2E6, #FFFFFF이며, 뉴트럴 톤이 대부분의 UI 표면을 차지한다. 브랜드 컬러는 CTA 버튼과 핵심 강조 요소에만 사용되어 사용자의 시선을 정확히 유도한다.

타이포그래피는 `Sohne`을 중심으로 구축된다. weight 400이 기본으로, 안정적이고 균형 잡힌 가독성을 제공한다. 제목과 본문 사이의 weight 대비로 시각적 계층을 명확히 한다.

레이아웃은 넉넉한 여백과 명확한 섹션 구분으로 콘텐츠에 호흡을 부여한다. 전반적으로 정보 밀도보다 시각적 여유를 우선시하며, 이는 Medium 브랜드의 자신감과 품격을 반영한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Medium처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Sohne", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #242424; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 그린 */
:root { --brand: #1A8917; }
```

**절대 하지 말아야 할 것 하나**: 기사 본문 폰트를 sans-serif로 쓰는 것. Medium 기사는 `Georgia` 또는 `Charter` 계열의 serif가 핵심 가독성 정체성이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://medium.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | CSS 파싱 결과 최소 — Webpack/Parcel 번들 난독화 |
| Token prefix | N/A (토큰 prefix 없음) |
| Method | CSS 커스텀 프로퍼티 파싱 · frequency 분석 · 브랜드 지식 보완 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React SPA (custom bundler, 인하우스 Next.js 이전 아키텍처)
- **Design system**: 인-하우스 (공개 DS 없음)
- **CSS architecture**: CSS Modules (hashed classname) — 토큰 prefix 미노출
- **Default theme**: light (흰 배경 #FFFFFF)
- **Font loading**: 자체 호스트 — Sohne (UI), Charter/GT Sectra (기사 본문)
- **Notable**: CSS 파싱 결과가 매우 희박함 (Webpack 번들링으로 인라인 최소화)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **UI 폰트**: `Sohne` (Klim Type Foundry, 유료) — 일반 UI, nav, label
- **기사 제목**: `Sohne` (weight 700–900)
- **기사 본문**: `Charter` (Bitstream, 유료) 또는 `GT Sectra` — serif, 가독성 중심
- **Code**: 시스템 monospace
- **Weight normal / bold**: `400` / `700`

```css
/* UI / 네비게이션 */
body {
  font-family: "Sohne", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}
/* 기사 본문 */
.article-body {
  font-family: "Charter", "Bitstream Charter", Georgia, "Times New Roman", serif;
  font-size: 20px;
  font-weight: 400;
  line-height: 1.75;
  letter-spacing: -0.003em;
}
```

> **라이선스 주의**: Sohne 유료 라이선스. 대체재: UI → `Inter`, 기사 본문 → `Lora` (Google Fonts) 또는 `Source Serif 4`.

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | font-family | size | weight | line-height | letter-spacing |
|---|---|---|---|---|---|
| Hero Title | Sohne | 46–60px | 700 | 1.1 | -0.02em |
| Article Heading | Sohne | 28–36px | 700 | 1.2 | -0.015em |
| Article Sub | Sohne | 22px | 400 | 1.4 | 0 |
| Article Body | Charter/serif | 20px | 400 | 1.75 | -0.003em |
| UI Body | Sohne | 14–16px | 400 | 1.5 | 0 |
| Caption / Meta | Sohne | 13px | 400 | 1.4 | 0 |
| Label / Tag | Sohne | 12px | 500 | 1 | 0.02em |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand Palette

| 이름 | Hex | 용도 |
|---|---|---|
| Medium Green | `#1A8917` | CTA 버튼, 팔로우 버튼, 링크 악센트 |
| Green Dark | `#156012` | hover 상태 |
| Green Light | `#E6F2E6` | 초록 tint 배경 |
| Page BG | `#FFFFFF` | body 배경 |
| Card BG | `#F9F9F9` | 카드/사이드바 배경 |
| Ink | `#242424` | 본문 텍스트 (warm near-black) |
| Muted | `#757575` | 부제목, 메타 |
| Border | `#E6E6E6` | 경계선 |

### Semantic Roles

| 역할 | Hex | 용도 |
|---|---|---|
| Page BG | `#FFFFFF` | body 기본 배경 |
| Ink (Text Primary) | `#242424` | 헤드라인, 본문 |
| Text Muted | `#757575` | 부제목, 작성자, 날짜 |
| Border Default | `#E6E6E6` | 구분선 |
| CTA Primary | `#1A8917` | Follow · Subscribe 버튼 |
| Tag Tint | `#E6F2E6` | 토픽 태그 배경 |

---

## 07. Spacing
<!-- SOURCE: manual -->

> Medium은 8px 기반 그리드. 기사 본문 최대 너비 740px.

| 이름 | 값 | 용도 |
|---|---|---|
| xs | 4px | 아이콘·아바타 간격 |
| sm | 8px | 인라인 요소 간격 |
| md | 16px | 컴포넌트 내부 패딩 |
| lg | 24px | 카드 패딩 |
| xl | 32px | 섹션 간격 |
| 2xl | 48px | 기사 paragraph 간격 |
| 3xl | 64px | hero 섹션 패딩 |
| article-max | 740px | 기사 본문 최대 너비 |

---

## 08. Radius
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| sm | 2px | 태그·배지 |
| md | 4px | 버튼 |
| lg | 8px | 카드 |
| full | 100px | 아바타, 팔로우 버튼 pill |

---

## 09. Shadows
<!-- SOURCE: manual -->

| 이름 | 값 | 용도 |
|---|---|---|
| card | `0 2px 8px rgba(0,0,0,.06)` | 기사 카드 hover |
| dropdown | `0 4px 16px rgba(0,0,0,.12)` | 드롭다운 메뉴 |
| sticky-nav | `0 1px 0 rgba(0,0,0,.1)` | 스크롤 후 네비게이션 |

---

## 10. Motion
<!-- SOURCE: manual -->

| 속성 | 값 | 용도 |
|---|---|---|
| duration-fast | 150ms | hover · focus 전환 |
| duration-base | 250ms | 카드 트랜지션 |
| easing | `ease` | 대부분 애니메이션 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **기사 본문**: max-width 740px, 좌우 auto margin, serif 폰트
- **홈 피드**: 3-col 카드 그리드 (desktop), 1-col (mobile)
- **사이드바**: 우측 280px — 추천, 태그, 작가 정보
- **네비게이션**: 상단 sticky, 배경 흰색, 1px 하단 보더
- **Tag/Topic 페이지**: 최대 너비 1080px, 좌우 패딩 20px

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | < 768px | 단일 컬럼, 터치 최적화 |
| Tablet | 768px–1024px | 2컬럼 그리드, 축소된 여백 |
| Desktop | 1024px–740px | 전체 레이아웃, 다중 컬럼 |
| Large | > 740px | max-width 고정, 좌우 auto margin |

### Touch Targets
- **Minimum tap size**: 44×44px (WCAG 2.5.5)
- **Button height (mobile)**: 48px
- **Input height (mobile)**: 48px

### Collapsing Strategy
- **Navigation**: 모바일에서 햄버거 메뉴로 전환
- **Grid columns**: desktop 다중 컬럼 → mobile 1컬럼 스택
- **Hero layout**: 이미지+텍스트 분할 → 모바일에서 수직 스택

---

## 13. Components
<!-- SOURCE: manual -->

### CTA 버튼 (팔로우 / 구독)

```css
.btn-follow {
  background: #1A8917;
  color: #FFFFFF;
  font-family: "Sohne", sans-serif;
  font-size: 14px; font-weight: 500;
  padding: 8px 16px;
  border-radius: 100px; /* pill */
  border: none; cursor: pointer;
  transition: background 150ms ease;
}
.btn-follow:hover { background: #156012; }
```

### 기사 카드

```css
.article-card {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 24px;
  padding: 20px 0;
  border-bottom: 1px solid #E6E6E6;
}
.article-card__title {
  font-family: "Sohne", sans-serif;
  font-size: 20px; font-weight: 700;
  line-height: 1.3; color: #242424;
}
.article-card__meta {
  font-family: "Sohne", sans-serif;
  font-size: 13px; color: #757575;
  margin-top: 8px;
}
```

### 토픽 태그

```css
.topic-tag {
  display: inline-block;
  background: #F2F2F2;
  color: #242424;
  font-size: 13px; font-weight: 500;
  padding: 6px 12px;
  border-radius: 100px;
  transition: background 150ms;
}
.topic-tag:hover { background: #E6E6E6; }
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

- **기사 제목**: 명사형 또는 호기심 유발형. "How X changes Y", "The truth about X"
- **서브 타이틀**: 제목 보완, 보다 구체적인 가치 제안 1문장
- **byline**: "Author · 읽기 N분 · 날짜"
- **CTA**: "Follow", "Subscribe", "Sign up" — 단순 동사
- **토픽 태그**: 소문자, 2–3 단어 최대

---

## 15. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  /* Brand */
  --brand: #1A8917;
  --brand-hover: #156012;
  --brand-tint: #E6F2E6;

  /* Surface */
  --bg: #FFFFFF;
  --bg-card: #F9F9F9;

  /* Text */
  --ink: #242424;
  --fg-muted: #757575;

  /* Border */
  --border: #E6E6E6;

  /* Spacing */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;

  /* Radius */
  --radius-sm: 2px;
  --radius-md: 4px;
  --radius-lg: 8px;
  --radius-pill: 100px;
}

body {
  font-family: "Sohne", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.5;
  background: var(--bg);
  color: var(--ink);
  -webkit-font-smoothing: antialiased;
}

.article-body {
  font-family: "Charter", Georgia, "Times New Roman", serif;
  font-size: 20px;
  line-height: 1.75;
  letter-spacing: -0.003em;
  max-width: 740px;
  margin: 0 auto;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: '#1A8917',
        'brand-hover': '#156012',
        'brand-tint': '#E6F2E6',
        ink: '#242424',
        'text-muted': '#757575',
        'bg-card': '#F9F9F9',
        border: '#E6E6E6',
      },
      fontFamily: {
        sans: ['"Sohne"', '"Helvetica Neue"', 'Helvetica', 'Arial', 'sans-serif'],
        serif: ['"Charter"', 'Georgia', '"Times New Roman"', 'serif'],
      },
      borderRadius: {
        DEFAULT: '4px',
        sm: '2px',
        lg: '8px',
        pill: '100px',
      },
      maxWidth: {
        article: '740px',
      },
    },
  },
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#1A8917` |
| Background | bg-page | `#FFFFFF` |
| Text primary | text | `#242424` |
| Text muted | text-muted | `#757575` |
| Border | border | `#E6E6E6` |

### Example Component Prompts

#### Hero Section
```
Medium 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: Sohne, weight 400
- CTA 버튼: 배경 #1A8917, radius 100px
```

#### Card Component
```
Medium 스타일 카드 컴포넌트를 만들어줘.
- 배경: #F9F9F9, border: 1px solid #E6E6E6
- 제목: Sohne, weight bold
- 본문: color #242424, line-height 1.6
```

#### Button
```
Medium 스타일 버튼을 만들어줘.
- 배경: #1A8917, 텍스트: white
- font: Sohne, weight 500-600
- padding: 12px 24px, radius: 100px
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

- **기사 본문은 반드시 serif** (Charter/Georgia) — 가독성이 Medium 브랜드의 핵심
- **CTA 버튼은 pill 형태** (border-radius: 100px) — 팔로우, 구독 버튼 모두
- **텍스트는 #242424** — 순흑(#000) 아닌 warm near-black
- **그린(#1A8917)은 CTA 전용** — 본문 링크는 기본적으로 밑줄 텍스트색
- **기사 본문 max-width 740px** 유지 — 더 넓으면 가독성 저하

### DON'T

- **sans-serif로 기사 본문 쓰지 않는다** — Medium 정체성 완전 파괴
- **그린(#1A8917)을 배경 전면 도배하지 않는다** — CTA 포인트 컬러 역할
- **본문 폰트 size를 16px 이하로 줄이지 않는다** — 기사 본문 최소 20px
- **border-radius 0로 버튼 각지게 만들지 않는다** — Medium은 pill 스타일
- **다크 배경을 기본으로 쓰지 않는다** — 흰 배경 + 그린 CTA가 정체성
