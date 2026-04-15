---
slug: nike
service_name: Nike
site_url: https://nike.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#111111"
primary_font: Helvetica Now Text
font_weight_normal: 400
token_prefix: --podium-cds-*
---

# DESIGN.md — Nike (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Nike의 디지털 인터페이스는 라이트 테마를 기본으로 한다. 밝은 배경 위에 브랜드 컬러 `#111111`가 절제적으로 사용되어 깔끔하고 신뢰감 있는 시각적 인상을 만든다.

색상 전략은 `#111111`, `#000000`, `#D5FF44` 등을 중심으로 구성된다. 브랜드의 canonical 컬러인 `#111111`가 CTA와 주요 인터랙션 요소에 사용되며, 나머지 뉴트럴 팔레트가 배경과 텍스트 계층을 형성한다.

타이포그래피는 `Helvetica Now Text` 폰트를 중심으로 브랜드 고유의 성격을 표현한다. 기본 weight 400으로 본문을 구성하며, heading에서 더 무거운 weight를 사용해 시각적 위계를 만든다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Nike처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Helvetica Now Text", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #111111; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #111111; }
```

**절대 하지 말아야 할 것 하나**: Nike를 "검정과 흰색의 단순 브랜드"로만 생각하는 것. 실제 Nike 마케팅 사이트는 `#D5FF44`(형광 라임 옐로)를 AI/혁신 기능 highlight에 사용한다. 순수 모노크롬에 이 한 가지 네온 포인트가 Nike의 현재 디지털 아이덴티티다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://nike.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | Podium CDS 토큰 시스템 |
| Token prefix | `--podium-cds-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (자체 마케팅 플랫폼)
- **Design system**: Podium CDS (Nike Commerce Design System) — prefix `--podium-cds-*`
- **CSS architecture**: 토큰 참조 + CSS Module 혼합
  ```
  podium  (--podium-cds-color-text-primary, --podium-cds-typography-body1-strong)  semantic 토큰
  nav     (nav-css-* 해시 패턴)  네비게이션 스타일
  ```
- **Class naming**: BEM + `nav-css-*` 해시 패턴
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 자체 호스트 (`Helvetica Now Text`, `Helvetica Now Display`, `Nike Futura ND`)
- **Canonical anchor**: `#111111` — `--podium-cds-color-text-primary` 폴백값 (7회)

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Nike Futura ND` (Nike 독점, headline 전용)
- **Body font**: `Helvetica Now Text` (Monotype, 유료)
- **Display variant**: `Helvetica Now Display Medium` (headline 대용)
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --podium-cds-font-family: "Helvetica Now Text", Helvetica, Arial, sans-serif;
  --podium-cds-font-weight-normal: 400;
  --podium-cds-font-weight-bold: 700;
}
body {
  font-family: var(--podium-cds-font-family);
  font-weight: var(--podium-cds-font-weight-normal);
}
```

> **라이선스 주의**: `Helvetica Now Text`는 Monotype 유료. 외부 프로젝트에서는 `Inter` 또는 `DM Sans`가 가장 가까운 대체재.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> N/A — CSS에서 typography scale 토큰이 추출되지 않음.
> 감지된 weight: 400(10회), 500(18회), 700(4회), bold(3회), normal(36회).

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp

| Token | Hex |
|---|---|
| 브랜드 near-black | `#111111` |
| 순흑 | `#000000` |

### 06-2. Nike AI / Neon Accent

| Token | Hex |
|---|---|
| neon lime (AI 기능 bg) | `#D5FF44` |
| neon lime border | `#BAD168` |
| AI 텍스트 색 | `#111111` |

### 06-3. Neutral Ramp

| Step | Hex | Count |
|---|---|---|
| 흰 배경 | `#FFFFFF` | 22회 |
| 순흑 | `#000000` | 12회 |
| near-black | `#111111` | 7회 |
| 중간 회색 | `#707072` | 3회 |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Neon Lime (AI) | nav highlight | `#D5FF44` |
| Focus Blue | focus ring | `#1151FF` |
| Success Green | active | `#2EB350` |
| Alert Red | error | `#FF623A` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--podium-cds-color-text-primary` | `#111111` | 주요 텍스트 |
| nav AI highlight bg | `#D5FF44` | Nike AI nav 배경 |
| nav AI highlight border | `#BAD168` | Nike AI nav 테두리 |
| nav focus ring | `#1151FF` | 포커스 링 |
| nav dropdown icon | `#000000` | 드롭다운 아이콘 |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--podium-cds-color-text-primary` | `#111111` | 본문 텍스트 |
| AI highlight | `#D5FF44` | Nike AI nav 섹션 |
| focus | `#1151FF` | 키보드 포커스 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 22 | 배경 / 텍스트 on dark |
| 2 | `#73859F` | 13 | VideoJS player UI |
| 3 | `#000000` | 12 | 텍스트 / 배경 |
| 4 | `#1151FF` | 11 | 포커스 링 |
| 5 | `#111111` | 7 | primary 텍스트 |
| 6 | `#2B333F` | 7 | VideoJS dark |
| 7 | `#D5FF44` | 4 | Nike AI highlight |

---

## 07. Spacing
<!-- SOURCE: auto -->

> N/A — spacing 토큰이 CSS에서 추출되지 않음.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| VideoJS 버튼 | `2px` | `.vjs-track-settings-controls button` |

---

## 09. Shadows
<!-- SOURCE: auto -->

> N/A — shadow 토큰이 CSS에서 추출되지 않음.

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
<!-- SOURCE: auto+manual -->

### Nav AI Highlight

```html
<div class="nav-css-1syi1pm">
  Nike AI
</div>
```

| 속성 | 값 |
|---|---|
| background | `#D5FF44` |
| color | `#111111` |
| border | `1px solid #BAD168` |

### Primary CTA Button

```html
<a href="#" class="nds-btn nds-button--filled">
  Shop Now
</a>
```

| 속성 | 값 |
|---|---|
| background | `#111111` |
| color | `#FFFFFF` |
| font-family | `Helvetica Now Text` |

### Navigation Link

```html
<a class="nav-css-ykqebk" href="#">
  Men
</a>
```

| 속성 | 값 |
|---|---|
| color | `#111111` |
| font | `--podium-cds-typography-body1-strong` |
| cursor | pointer |

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 슬로건형, 대문자, 짧게 | "JUST DO IT." |
| Primary CTA | 행동형 대문자 | "SHOP NOW" |
| Secondary CTA | 카테고리 탐색 | "Men's Running" |
| Subheading | 제품 이름 + 기능 | "Air Max 270 — Maximum Cushioning" |
| Tone | 대담, 직접적, 영감, 대문자 강조 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Nike — copy into your root stylesheet */
:root {
  /* Fonts */
  --podium-cds-font-family: "Helvetica Now Text", Helvetica, Arial, sans-serif;
  --podium-cds-font-weight-normal: 400;
  --podium-cds-font-weight-bold: 700;

  /* Brand */
  --podium-cds-color-brand: #111111;
  --podium-cds-color-brand-neon: #D5FF44;
  --podium-cds-color-focus: #1151FF;

  /* Surfaces */
  --podium-cds-bg-page: #FFFFFF;
  --podium-cds-bg-dark: #111111;
  --podium-cds-text: #111111;
  --podium-cds-text-muted: #707072;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Nike
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          black: '#111111',
          neon: '#D5FF44',
          'neon-border': '#BAD168',
          focus: '#1151FF',
        },
        neutral: {
          900: '#111111',
          700: '#707072',
          100: '#FFFFFF',
        },
      },
      fontFamily: {
        sans: ['"Helvetica Now Text"', 'Helvetica', 'Arial', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
        bold: '700',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#111111` |
| Background | bg-page | `#FFFFFF` |
| Text primary | text | `#111111` |
| Text muted | text-muted | `#707072` |
| Border | border | `#E0E0E0` |

### Example Component Prompts

#### Hero Section
```
Nike 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: Helvetica Now Text, weight 700
- 서브텍스트: #707072
- CTA 버튼: 배경 #111111, 텍스트 white
```

#### Card Component
```
Nike 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF, border: 1px solid #E0E0E0
- radius: 2px
- 제목: Helvetica Now Text, 16px, weight 700
- 본문: 14px, color #111111
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
- 브랜드 컬러로 `#111111` (near-black, 순흑 아님) 사용
- AI/혁신 기능에 `#D5FF44` 네온 라임 포인트 사용
- 포커스 링은 `#1151FF` 블루 사용
- 텍스트에 `--podium-cds-color-text-primary` 변수 사용
- headline은 UPPERCASE, 짧고 임팩트 있게

### ❌ DON'T
- Nike를 순흑/순백만으로 표현하지 말 것 — `#D5FF44` 포인트가 현재 아이덴티티
- 네온 라임 `#D5FF44`를 배경 전체에 쓰지 말 것 — 포인트 전용
- 텍스트를 순흑 `#000000` 대신 `#111111` 사용
- 소문자 headline 쓰지 말 것 — Nike는 UPPERCASE 헤드라인
