---
slug: yanolja
service_name: Yanolja
site_url: https://yanolja.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#4154FF"
primary_font: Pretendard
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Yanolja (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Yanolja의 디지털 인터페이스는 라이트 테마를 기본으로 한다. 밝은 배경 위에 브랜드 컬러 `#4154FF`가 절제적으로 사용되어 깔끔하고 신뢰감 있는 시각적 인상을 만든다.

색상 전략은 `#B2BAFF`, `#F5F6FF`, `#7280FF` 등을 중심으로 구성된다. 브랜드의 canonical 컬러인 `#4154FF`가 CTA와 주요 인터랙션 요소에 사용되며, 나머지 뉴트럴 팔레트가 배경과 텍스트 계층을 형성한다.

타이포그래피는 `Pretendard` 폰트를 중심으로 브랜드 고유의 성격을 표현한다. 기본 weight 400으로 본문을 구성하며, heading에서 더 무거운 weight를 사용해 시각적 위계를 만든다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Yanolja처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: Pretendard, 'Apple SD Gothic Neo', Roboto, Arial Helvetica, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #4154FF; }
```

**절대 하지 말아야 할 것 하나**: 브랜드 블루를 `#3C7BFD` 하나로 고정하는 것. Yanolja의 CTA 블루는 `#4154FF`(primary main)이고, 그라디언트와 버블 색은 각각 다른 블루 계열(`#3E5FEA`, `#643EDF`)이 혼용된다. 단일 블루로 통일하면 Yanolja 특유의 다채로운 블루 레이어가 사라진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://yanolja.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | Tailwind v4 기반 Next.js SSR |
| CSS files | Tailwind + 외부 Pretendard |
| Token prefix | N/A (Tailwind 유틸리티 클래스) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js + Tailwind CSS v4
- **Design system**: Tailwind v4 (`--color-*` 시그니처) + 자체 색상 확장
- **CSS architecture**: Tailwind 유틸리티 + 인라인 CSS 변수
  ```
  Tailwind utility classes (색상, 간격, 타이포)
  CSS custom props 일부 (--bubble-fill, --bubble-stroke 등)
  ```
- **Class naming**: Tailwind 유틸리티 클래스 (`fill-[var(--bubble-fill,...)]` 패턴)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: Pretendard (CDN / 셀프 호스트), Tailwind Fallback
- **Canonical anchor**: `#4154FF` — `.pc:outline-line-primary-main` 에서 확인된 primary main

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Pretendard` (오픈소스)
- **Code font**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Courier New, monospace`
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-family: Pretendard, 'Apple SD Gothic Neo', Roboto, Arial Helvetica, sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold: 700;
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
| body | 1rem | 400 | 1.6 | 0 |
| heading | 1.25rem | 700 | 1.3 | 0 |
| caption | 0.75rem | 400 | 1.5 | 0 |

> ⚠️ Pretendard는 가변 폰트가 아니라 weight별 분리 파일로 제공된다. 400, 600, 700이 주로 사용된다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (블루 계열)

| Token | Hex |
|---|---|
| line-primary-weak2 | `#B2BAFF` |
| fill-primary-weak | `#F5F6FF` |
| bubble-stroke | `#B2BAFF` |
| line-primary-weak4 | `#7280FF` |
| gradient-blue-1 | `#3C7BFD` |
| gradient-blue-2 | `#3E5FEA` |
| gradient-blue-3 | `#4052EB` |
| primary-main | `#4154FF` ⭐ **canonical** |
| primary-dark | `#0152CC` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| violet | key | `#643EDF` |
| purple | key | `#8249D8` |
| sky blue | key | `#4AB0F9` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| fill-primary-weak | `#F5F6FF` | 버블 배경 |
| line-primary-weak2 | `#B2BAFF` | 버블 테두리 |
| line-primary-weak4 | `#7280FF` | outline focus |
| primary-main | `#4154FF` | CTA 버튼, 링크 |
| text | `#000000` | 버튼 텍스트 기본 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 14 | 배경 |
| 2 | `#3C7BFD` | 11 | 그라디언트 블루 |
| 3 | `#3E5FEA` | 11 | 그라디언트 블루 |
| 4 | `#4052EB` | 11 | 그라디언트 블루 |
| 5 | `#4BA2F6` | 11 | 그라디언트 블루 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| Tailwind default | 0.25rem 단위 | 모든 여백 |

**주요 alias**:
- Tailwind `p-4` → 1rem (16px)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| bubble | 999px | 버블/배지 컴포넌트 |
| card | 0.5rem | 일반 카드 |

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

### Bubble — 채팅/프로모션 배지

```html
<div class="bubble" style="--bubble-fill:#F5F6FF;--bubble-stroke:#B2BAFF;">
  특가
</div>
```

| Spec | Value |
|---|---|
| --bubble-fill | `#F5F6FF` (기본) |
| --bubble-stroke | `#B2BAFF` (기본) |
| border-radius | 999px |

### CTA Button — Primary

```html
<button class="btn-primary" type="button">지금 예약</button>
```

| Spec | Value |
|---|---|
| background | `#4154FF` |
| color | `#FFFFFF` |
| font-weight | 700 |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Yanolja — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: Pretendard, 'Apple SD Gothic Neo', Roboto, Arial Helvetica, sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold: 700;

  /* Brand (anchor + steps) */
  --brand-weak: #F5F6FF;
  --brand-300: #B2BAFF;
  --brand-400: #7280FF;
  --brand-500: #4154FF;   /* ← canonical */
  --brand-600: #3549FF;
  --brand-900: #0152CC;

  /* Surfaces */
  --bg-page: #FFFFFF;
  --bg-dark: #111111;
  --text: #000000;
  --text-muted: #9CA3AF;

  /* Key spacing */
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 32px;

  /* Radius */
  --radius-sm: 8px;
  --radius-md: 16px;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#4154FF` |
| Background | bg-page | `#FFFFFF` |
| Text primary | text | `#000000` |
| Text muted | text-muted | `#9CA3AF` |
| Border | border | `#E0E0E0` |

### Example Component Prompts

#### Hero Section
```
Yanolja 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: Pretendard, weight 700
- 서브텍스트: #9CA3AF
- CTA 버튼: 배경 #4154FF, 텍스트 white
```

#### Card Component
```
Yanolja 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF, border: 1px solid #E0E0E0
- radius: 999px
- 제목: Pretendard, 16px, weight 700
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

### DO
- CTA 버튼은 `#4154FF`(primary main)을 정확히 써라.
- 버블/배지 배경은 `#F5F6FF`, 테두리는 `#B2BAFF`로 써라.
- Pretendard weight는 400(본문), 700(강조)으로 명확히 구분하라.
- 그라디언트는 `#3C7BFD` → `#643EDF` 방향으로 써라.
- focus outline에 `#4154FF`를 써라 — line-primary-main이다.

### DON'T
- 단일 블루 하나로 모든 색을 통일하지 마라 — Yanolja는 블루 계열 여러 단계를 층위별로 쓴다.
- `#B620E0`(보라)를 브랜드 primary로 착각하지 마라 — 그라디언트 accent 중 하나일 뿐이다.
- `#000000`을 버튼 배경으로 쓰지 마라 — 텍스트 기본값이다.
- Tailwind 클래스에 임의 색상값을 하드코딩하지 마라 — CSS 변수를 통해 써라.
- `font-weight: 600`을 기본으로 두지 마라 — Yanolja 본문은 400이다.
