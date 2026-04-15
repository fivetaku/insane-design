---
slug: nothing
service_name: Nothing
site_url: https://nothing.tech
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#000000"
primary_font: NType82-Regular
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Nothing (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Nothing의 디지털 인터페이스는 다크 테마를 기반으로 한다. 어두운 배경 위에 밝은 텍스트와 브랜드 컬러 `#000000`가 돋보이는 구성으로, 시각적 몰입감과 프리미엄 분위기를 동시에 전달한다.

색상 전략은 `#000000`, `#FFFFFF`, `#F4F4F4` 등을 중심으로 구성된다. 브랜드의 canonical 컬러인 `#000000`가 CTA와 주요 인터랙션 요소에 사용되며, 나머지 뉴트럴 팔레트가 배경과 텍스트 계층을 형성한다.

타이포그래피는 `NType82-Regular` 폰트를 중심으로 브랜드 고유의 성격을 표현한다. 기본 weight 400으로 본문을 구성하며, heading에서 더 무거운 weight를 사용해 시각적 위계를 만든다.

레이아웃은 풀 너비 히어로 섹션과 콘텐츠 영역의 리듬감 있는 교차로 구성된다. 충분한 여백을 활용하여 콘텐츠에 시각적 호흡 공간을 부여하고, 핵심 메시지와 CTA에 자연스럽게 시선을 유도한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Nothing처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "NType82-Regular", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #000000; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 (검정/흰 대비) */
:root { --brand: #000000; }
```

**절대 하지 말아야 할 것 하나**: 포인트 컬러를 추가하는 것. Nothing의 정체성은 극도의 흑백 대비에 있다. 빨강이든 파랑이든 포인트 컬러를 넣는 순간 Nothing의 미니멀리즘이 무너진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://nothing.tech` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A bytes (Next.js / SSR) |
| CSS files | Tailwind 기반 + 커스텀 폰트 시스템 |
| Token prefix | N/A (Tailwind utility class 중심) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (Tailwind CSS v3 기반)
- **Design system**: 자체 미니멀 시스템 — 토큰 없음, 유틸리티 클래스 중심
- **CSS architecture**: Tailwind utility-first + 커스텀 폰트 `@font-face`
- **Class naming**: Tailwind 유틸리티 (prose, container, grid)
- **Default theme**: dark (검정 배경이 기본)
- **Font loading**: 자체 호스트 `NType82-Regular`, `Ndot-Regular`, `LatteraMonoLL`
- **Canonical anchor**: 흑백 이분법 — `#000000` + `#FFFFFF`. 포인트 컬러 없음

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary font**: `NType82-Regular` (Nothing 전용 커스텀 sans-serif, 7회 사용)
- **Headline font**: `NType82-Headline` (별도 헤드라인용 컷)
- **Dot matrix font**: `Ndot-Regular` (Nothing의 독특한 도트 매트릭스 폰트, 6회)
- **Mono font**: `LatteraMonoLL` (5회 — 제품 스펙, 기술 수치)
- **Weight normal**: `400`, **Thin**: `100`

```css
body {
  font-family: NType82-Regular, sans-serif;
  font-weight: 400;
}

.headline {
  font-family: NType82-Headline, sans-serif;
}

.dot-matrix {
  font-family: Ndot-Regular, sans-serif;
  font-weight: 100; /* ⚠️ Ndot는 100 weight로 쓴다 */
}

.mono {
  font-family: LatteraMonoLL, sans-serif;
}
```

> **라이선스 주의**: `NType82`, `Ndot`, `LatteraMonoLL` 은 Nothing 전용 커스텀 폰트다. 대체재로는 `Helvetica Neue` 계열이나 `Space Mono`가 가장 가깝지만 도트 매트릭스 감은 재현 불가.

---

## 05. Typography Scale
<!-- SOURCE: manual -->

Nothing의 타이포그래피는 극명한 크기 대비 — 거대한 헤드라인과 작은 바디 텍스트.

| 역할 | 폰트 | 크기 | Weight |
|---|---|---|---|
| Hero Display | NType82-Headline | clamp(64px, 10vw, 120px) | 400 |
| Section Heading | NType82-Regular | 40px–56px | 400 |
| Dot Label | Ndot-Regular | 11px–14px | 100 |
| Body | NType82-Regular | 14px–16px | 400 |
| Mono Spec | LatteraMonoLL | 11px–13px | 400 |
| Caption | NType82-Regular | 11px | 400 |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 팔레트 전체

Nothing의 컬러는 흑백 이분법이다. 중간 그레이는 최소한으로.

| Hex | 역할 | 참고 |
|---|---|---|
| `#000000` | 기본 배경 (다크 테마) | |
| `#FFFFFF` | 기본 텍스트, 라이트 섹션 배경 | count 11 |
| `#FFFFFFCC` | 반투명 흰 텍스트 | count 7 |
| `#F4F4F4` | 라이트 섹션 배경 | count 2 |
| `#B1B3B3` | 보조 텍스트 (중성 회색) | count 3 |
| `#9CA3AF` | 더 연한 보조 텍스트 | count 2 |
| `#00000033` | 오버레이 | count 2 |

---

## 07. Spacing
<!-- SOURCE: manual -->

Tailwind 기본 스케일 사용. 주요 값:

| 단계 | Value | 용도 |
|---|---|---|
| 2 | 8px | 타이트 인라인 |
| 4 | 16px | 기본 패딩 |
| 6 | 24px | 컴포넌트 내부 |
| 8 | 32px | 섹션 내부 |
| 12 | 48px | 섹션 간격 |
| 20 | 80px | 히어로 패딩 |
| 32 | 128px | 랜딩 대섹션 |

---

## 08. Radius
<!-- SOURCE: manual -->

| 역할 | Radius |
|---|---|
| Button / Tag | 0px 또는 2px (sharp, 미니멀) |
| Card | 0px (완전한 직각) |
| Image container | 0px |
| Pill (모달) | 999px (rare) |

> Nothing은 라디우스를 거의 쓰지 않는다. 각진 edge가 하드웨어 브랜드 정체성.

---

## 09. Shadows
<!-- SOURCE: manual -->

Nothing은 그림자를 쓰지 않는다. 그림자 = 포스트 모던 디자인 언어. Nothing은 그 이전의 직접적 대비.

| 레이어 | CSS |
|---|---|
| 기본 | none |
| 오버레이 (희귀) | `0 0 0 1px rgba(255,255,255,0.1)` |

---

## 10. Motion
<!-- SOURCE: manual -->

| 패턴 | Duration | Easing |
|---|---|---|
| 기본 트랜지션 | 200ms | ease |
| 페이지 전환 | 300ms | ease-out |
| 호버 | 150ms | ease |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **히어로**: 풀 스크린 (`100vh`), 검정 배경, 텍스트 중앙 정렬, 거대한 폰트
- **그리드**: 미니멀 2-column 또는 asymmetric — 텍스트 왼쪽/이미지 오른쪽
- **섹션 교차**: 검정 섹션 ↔ 흰 섹션 교차 (명확한 테마 전환)
- **Nav**: 투명 배경 → 스크롤 시 `rgba(0,0,0,0.8)` 블러 nav
- **컨테이너**: `max-width: 1280px; padding: 0 24px; margin: 0 auto`

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

### Primary CTA Button

```css
.btn-primary {
  background: #FFFFFF;
  color: #000000;
  border: 1px solid #FFFFFF;
  border-radius: 0;          /* sharp corner */
  padding: 12px 28px;
  font-family: NType82-Regular, sans-serif;
  font-weight: 400;
  font-size: 14px;
  letter-spacing: 0.02em;
  transition: all 150ms ease;
}
.btn-primary:hover {
  background: #000000;
  color: #FFFFFF;
}
```

### Secondary Button (Ghost)

```css
.btn-ghost {
  background: transparent;
  color: #FFFFFF;
  border: 1px solid #FFFFFF;
  border-radius: 0;
  padding: 11px 28px;
}
.btn-ghost:hover {
  background: rgba(255,255,255,0.1);
}
```

### Dot Matrix Label

```css
.dot-label {
  font-family: Ndot-Regular, sans-serif;
  font-weight: 100;
  font-size: 11px;
  letter-spacing: 0.08em;
  color: #B1B3B3;
  text-transform: uppercase;
}
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

- **헤드라인**: 철학적, 추상적. "Nothing is something." 형식
- **바디**: 간결, 직접적. 불필요한 형용사 없음
- **스펙**: 수치 + 단위만. "50MP", "5000 mAh", "165Hz"
- **어조**: 쿨, 무관심한 자신감. 흥분하지 않음

---

## 15. Drop-in CSS
<!-- SOURCE: manual -->

```css
/* Nothing Design System — Drop-in */
:root {
  --color-bg:       #000000;
  --color-fg:       #FFFFFF;
  --color-fg-muted: #FFFFFFCC;
  --color-subtle:   #B1B3B3;
  --color-border:   rgba(255,255,255,0.15);
  --color-overlay:  rgba(0,0,0,0.8);

  --font-primary: "NType82-Regular", sans-serif;
  --font-headline: "NType82-Headline", sans-serif;
  --font-dot:     "Ndot-Regular", sans-serif;
  --font-mono:    "LatteraMonoLL", sans-serif;
}

body {
  font-family: var(--font-primary);
  font-weight: 400;
  background: var(--color-bg);
  color: var(--color-fg);
  -webkit-font-smoothing: antialiased;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        nothing: {
          black: '#000000',
          white: '#FFFFFF',
          gray:  '#B1B3B3',
        },
      },
      fontFamily: {
        ntype:    ['NType82-Regular', 'sans-serif'],
        headline: ['NType82-Headline', 'sans-serif'],
        ndot:     ['Ndot-Regular', 'sans-serif'],
        mono:     ['LatteraMonoLL', 'sans-serif'],
      },
      borderRadius: {
        DEFAULT: '0px',
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
| Brand primary | brand | `#000000` |
| Background | bg-page | `#000000` |
| Text primary | text | `#FFFFFF` |
| Text muted | text-muted | `#FFFFFF` |
| Border | border | `#E0E0E0` |

### Example Component Prompts

#### Hero Section
```
Nothing 스타일 히어로 섹션을 만들어줘.
- 배경: #000000
- H1: NType82-Regular, weight 700
- 서브텍스트: #FFFFFF
- CTA 버튼: 배경 #000000, 텍스트 white
```

#### Card Component
```
Nothing 스타일 카드 컴포넌트를 만들어줘.
- 배경: #000000, border: 1px solid #E0E0E0
- radius: 0px
- 제목: NType82-Regular, 16px, weight 700
- 본문: 14px, color #FFFFFF
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

### DO

- 검정 배경 + 흰 텍스트 — 이것이 Nothing의 정체성
- 버튼 border-radius는 0px — 각진 엣지 유지
- `Ndot-Regular` 도트 폰트를 레이블, 스펙에 활용
- 거대한 헤드라인 대비 작은 바디 (극적인 크기 대비)
- 라이트/다크 섹션 교차를 통해 리듬 만들기
- 스펙은 수치로만 — "50MP" not "50 megapixel camera"

### DON'T

- 포인트 컬러 추가 — 흑백 이분법이 Nothing의 전부
- border-radius 사용 — 각진 엣지가 하드웨어 미학
- 그림자 — Nothing은 flat, direct
- 화려한 애니메이션 — 미니멀 모션
- 과도한 마케팅 카피 — 쿨하게, 간결하게

### 자주 하는 오해 vs 실제

| 오해 | 실제 |
|---|---|
| Nothing은 레드 포인트 컬러 | UI에 레드 없음. 순수 흑백 |
| 다크 테마만 존재 | 흰 배경 라이트 섹션도 자주 교차 사용 |
| 일반 고딕체로 대체 가능 | Ndot 도트 매트릭스 폰트는 Nothing만의 시그니처 |
