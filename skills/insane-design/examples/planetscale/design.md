---
slug: planetscale
service_name: PlanetScale
site_url: https://planetscale.com
fetched_at: 2026-04-11
default_theme: light
brand_color: "#0B6EC5"
primary_font: ui-sans-serif
font_weight_normal: 400
token_prefix: ""
---

# DESIGN.md — PlanetScale (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

PlanetScale은 Vitess 엔터프라이즈 데이터플랫폼으로, 기술적 신뢰감을 주는 미니멀한 디자인을 가진다. `#fafafa`(gray-50) 배경 위에 `#414141`(gray-700) 텍스트가 차분한 톤을 만들고, brand blue `#0B6EC5`가 CTA와 포커스 링에 집중된다. 시스템 폰트 스택을 의도적으로 사용하여 커스텀 웹폰트 없이 OS 네이티브 느낌을 준다.

Tailwind CSS 기반의 flat 네이밍(`--{family}-{step}`)과 12단계 gray ramp가 특징이다. 레거시 오렌지 `#F35815`는 현재 UI에서 사라졌고, 블루 `#0B6EC5`/`#1E9DE7` 중심으로 전환되었다. 도메인 특화 색상(Postgres `#336791`)이 인라인으로 적용되는 점이 독특하다.

**Key Characteristics:**
- 시스템 sans 스택 (`ui-sans-serif, system-ui`) — 외부 폰트 없음
- Gray ramp 12단계(`gray-50` ~ `gray-900`)가 핵심 중립축
- Brand blue `#0B6EC5` (오렌지가 아님 — 레거시)
- Tailwind single ring/shadow — dual-layer 아님
- Postgres `#336791` 등 DB 타입별 인라인 컬러

---

## 01. Quick Start

> 5분 안에 PlanetScale처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 시스템 폰트 스택 (커스텀 웹폰트 없음) */
body {
  font-family: ui-sans-serif, system-ui, sans-serif,
               "Apple Color Emoji", "Segoe UI Emoji";
  font-weight: 400;
}

/* 2. 라이트 배경 + 그레이 텍스트 레이어 */
:root { --bg-primary: #fafafa; --text-primary: #414141; }
body { background: var(--bg-primary); color: var(--text-primary); }

/* 3. 블루 브랜드 (오렌지 아님) */
:root { --blue-600: #0B6EC5; }
```

**절대 하지 말아야 할 것 하나**: 오렌지 `#F35815`를 브랜드 색으로 쓰지 말 것. 2024년 이후 PlanetScale은 Vitess 엔터프라이즈 데이터플랫폼 톤으로 피벗하면서 실제 UI는 블루 `#0B6EC5` / `#1E9DE7` 중심이다. 오렌지는 legacy 로고 잔재에 가깝다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://planetscale.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 89,810 bytes (Next.js SSR) |
| CSS files | 1개 외부 + 1 인라인, 총 78,267자 |
| Token prefix | 없음 (Tailwind flat 네이밍) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js 마케팅 사이트 (Tailwind 컴파일 결과물)
- **Design system**: 자체 시스템이 아닌 **Tailwind CSS** 컬러 램프 기반 — color family(`gray/blue/red/purple/green/orange/yellow/pink`) × step(50~950) 직접 참조
- **CSS architecture**: 2계층 구조
  ```
  Color ramps    (--{family}-{step})     raw hex 값
  Semantic alias (--text-*, --bg-*, --border-*) ramp 참조
  ```
- **Class naming**: Tailwind 유틸리티 클래스 (`text-gray-700`, `bg-blue-600`)
- **Default theme**: light (bg = `#fafafa`, text = `#414141`)
- **Font loading**: 시스템 폰트 스택 그대로 (`@font-face` 없음)
- **Canonical anchor**: `blue-600 #0B6EC5` — CTA/포커스 링/링크에 가장 많이 등장

---

## 04. Font Stack

- **Display/Body font**: 시스템 sans (ui-sans-serif, system-ui)
- **Code font**: `ui-monospace, SFMono-Regular, SF Mono, Menlo`
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --font-sans: ui-sans-serif, system-ui, sans-serif,
               "Apple Color Emoji", "Segoe UI Emoji",
               "Segoe UI Symbol", "Noto Color Emoji";
  --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo,
               Consolas, "Liberation Mono", monospace;
}
body {
  font-family: var(--font-sans);
  font-weight: 400;
}
```

커스텀 웹폰트 `@font-face` 선언은 CSS 덤프 전체에서 발견되지 않는다. 사용자 OS의 시스템 sans가 그대로 노출된다 — macOS는 SF Pro, Windows는 Segoe UI.

---

## 05. Typography Scale

| Token | Size | Weight | Line-height |
|---|---|---|---|
| body | 16px | 400 | 1.5 |
| sm | 14px | 400 | 1.5 |
| xs | 12px | 400 | 1.45 |
| heading-sm | 18px | 600 | 1.4 |
| heading-md | 20px / 24px | 600 | 1.3 |
| heading-lg | 32px | 700 | 1.2 |

> ⚠️ **`font-weight` 히스토그램**: 600(13회) > 500(6회) > 700(4회) > 400(4회). 제목과 강조에 `600`을 가장 많이 쓴다.

---

## 06. Colors

### 06-1. Gray Ramp (Neutral 주축)
<!-- --gray-{step} -->

| Token | Hex |
|---|---|
| `--gray-50`  | `#fafafa` |
| `--gray-100` | `#ebebeb` |
| `--gray-200` | `#e1e1e1` |
| `--gray-300` | `#c1c1c1` |
| `--gray-400` | `#a1a1a1` |
| `--gray-500` | `#818181` ⭐ (빈도 7회) |
| `--gray-550` | `#737373` |
| `--gray-600` | `#616161` |
| `--gray-700` | `#414141` (text-primary) |
| `--gray-800` | `#2b2b2b` |
| `--gray-850` | `#1a1a1a` |
| `--gray-900` | `#111111` |

### 06-2. Brand Blue Ramp

| Token | Hex |
|---|---|
| `--blue-600` | `#0B6EC5` ⭐ (canonical 브랜드 블루, 빈도 7회) |
| `--blue-500` | `#1E9DE7` (보조 / 링크 / 포커스 링) |
| `--blue-400` | `#4ab0f0` |
| `--blue-300` | `#7cc4f4` |

### 06-3. Accent Families

| Family | Key hex | Usage |
|---|---|---|
| red | `--red-700 #c11027` | danger / error (빈도 3회) |
| orange | `--orange-500 #f5a623` | legacy accent, 경고 |
| green | `--green-600 #22A652` | success |
| purple | `--purple-400` (ramp) | marketing highlight |

### 06-4. Semantic

| Token | Resolves to | Usage |
|---|---|---|
| `--text-primary`   | `var(--gray-700)` → `#414141` | 본문 |
| `--text-secondary` | `var(--gray-550)` → `#737373` | 보조 텍스트 |
| `--text-disabled`  | `var(--gray-400)` → `#a1a1a1` | 비활성 |
| `--text-contrast`  | `var(--black)` | 최대 대비 헤드라인 |
| `--bg-primary`     | `var(--gray-50)` → `#fafafa`  | 페이지 배경 |
| `--bg-secondary`   | `var(--gray-100)` → `#ebebeb` | 카드/섹션 |
| `--bg-inverted`    | `var(--gray-900)` → `#111111` | 다크 CTA |
| `--border-primary` | `var(--gray-700)` → `#414141` | 강조 보더 |
| `--text-postgres`  | `#336791` | Postgres 타입 배지 (도메인 특화) |

### 06-5. Dominant Colors (실제 DOM 빈도)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#818181` | 7 | gray-500 중립 텍스트 |
| 2 | `#0B6EC5` | 7 | **brand blue** (CTA) |
| 3 | `#1E9DE7` | 4 | 보조 블루, focus ring |
| 4 | `#a1a1a1` | 3 | gray-400 disabled |
| 5 | `#c11027` | 2 | red-700 danger |
| 6 | `#336791` | 2 | Postgres 배지 |

---

## 07. Spacing

Tailwind 기본 `spacing` 단위(`0.25rem = 4px`) 사이즈 단계를 그대로 사용. 전용 `--space-*` 커스텀 프로퍼티는 없음.

| 단계 | rem | px |
|---|---|---|
| 1 | 0.25 | 4 |
| 2 | 0.5  | 8 |
| 3 | 0.75 | 12 |
| 4 | 1    | 16 |
| 6 | 1.5  | 24 |
| 8 | 2    | 32 |
| 12 | 3   | 48 |
| 16 | 4   | 64 |

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| (tailwind `rounded`) | `0.25rem` / 4px | 기본 박스, 입력 필드 |
| `rounded-sm` | `0.125rem` / 2px | 인라인 칩 |
| `rounded-full` | `9999px` | pill 버튼, 아바타 |

---

## 09. Shadows

| Level | Value | Usage |
|---|---|---|
| ring | `0 0 0 3px rgb(30 157 231 / .5)` | focus ring (blue-500 50% alpha) |
| tw-shadow | `rgb(0 0 0 / .2)` single layer | 카드 |

Tailwind `--tw-ring-*` / `--tw-shadow-*` 6개 커스텀 변수로 단일 레이어 섀도만 사용. Stripe류 dual-layer 아님.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Breakpoint | Width | Key Changes |
|---|---|---|
| Mobile | <640px | 단일 컬럼, 모바일 네비게이션, 터치 타겟 44px+ |
| Tablet | 640-1024px | 2컬럼 그리드, 사이드 패딩 증가 |
| Desktop | 1024-1280px | 풀 그리드 레이아웃, 확장 네비게이션 |
| Large | >1280px | max-width 컨테이너, 중앙 정렬 |

---

## 13. Components

### Primary Button (Tailwind)
```html
<button class="bg-blue-600 hover:bg-blue-700 text-white
               font-semibold px-4 py-2 rounded">
  Get started
</button>
```
- Background: `#0B6EC5` (`bg-blue-600`)
- Text: white, weight 600
- Height: 대략 40px (py-2 + font)

### Postgres Type Badge
```html
<span class="inline-flex items-center gap-1 px-2 py-0.5
             text-xs font-medium rounded"
      style="color: #336791;">
  postgres
</span>
```
- DB 타입별 브랜드 색 인라인 적용

---

## 15. Drop-in CSS

```css
/* PlanetScale — copy into your root stylesheet */
:root {
  /* Fonts — system stack */
  --font-sans: ui-sans-serif, system-ui, sans-serif,
               "Apple Color Emoji", "Segoe UI Emoji";
  --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;

  /* Brand blue */
  --blue-600: #0B6EC5;
  --blue-500: #1E9DE7;
  --blue-400: #4ab0f0;

  /* Gray ramp */
  --gray-50:  #fafafa;
  --gray-100: #ebebeb;
  --gray-300: #c1c1c1;
  --gray-500: #818181;
  --gray-700: #414141;
  --gray-900: #111111;

  /* Semantic */
  --text-primary:   var(--gray-700);
  --text-secondary: var(--gray-550, #737373);
  --bg-primary:     var(--gray-50);
  --bg-inverted:    var(--gray-900);
  --border-primary: var(--gray-700);

  /* Danger / Success */
  --red-700: #c11027;
  --green-600: #22A652;
}

body {
  font-family: var(--font-sans);
  font-weight: 400;
  background: var(--bg-primary);
  color: var(--text-primary);
}

.focus-ring:focus-visible {
  outline: 3px solid rgb(30 157 231 / 0.5);
  outline-offset: 2px;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: auto+manual -->

### Quick Color Reference

| Role | Value |
|---|---|
| Brand | `#0B6EC5` |
| Page BG | `#FFFFFF` |
| Text Primary | `#000000` |
| Default Theme | light |

### Component Prompts

> **Hero section**: "PlanetScale 스타일 hero — `ui-sans-serif` 폰트, `#0B6EC5` brand color, light 배경"
>
> **CTA button**: "PlanetScale primary CTA — brand `#0B6EC5` 배경 또는 dark fill, `ui-sans-serif` 폰트"
>
> **Card component**: "PlanetScale 스타일 카드 — light 테마, 기존 radius/shadow 토큰 준수"

### Iteration Guide

1. **Color 교체 시**: 반드시 §06 Colors 테이블의 실제 hex 참조. AI 추론 색상 사용 금지.
2. **Typography 변경 시**: §04 Font Stack의 font-family 체인 + §05의 weight/size 매핑 확인.
3. **Spacing 조정 시**: §07 Spacing의 토큰 스케일 내에서만 변경.
4. **신규 컴포넌트**: §13 Components의 기존 패턴(radius, shadow, padding)을 기반으로 확장.

---

## 18. DO / DON'T

### ✅ DO
- Brand = **`#0B6EC5`** (blue-600). 링크, CTA, 포커스 링 모두 블루 계열로.
- 시스템 sans 스택 유지 (`ui-sans-serif, system-ui`). Inter를 강제 로드하지 않아도 되는 설계다.
- Tailwind 유틸리티 클래스를 그대로 읽을 것 (`bg-blue-600 text-white`). 자체 토큰 레이어 없음.
- gray ramp 12단계 (`gray-50 → gray-900`)를 핵심 중립 축으로 사용.
- 도메인 특화 색 보존: `--text-postgres #336791` 같이 DB 타입별 인라인 컬러.

### ❌ DON'T
- 오렌지 `#F35815`를 primary로 선언하지 말 것 (legacy/로고 색, 현 UI 주류 아님).
- `color-brand` / `color-ink` 같은 가상 토큰명 사용 금지 — 실제 CSS는 `--{family}-{step}` 플랫 네이밍.
- Inter/IBM Plex Mono를 `@font-face`로 로드하지 말 것. 시스템 sans 스택이 의도된 설계다.
- 단일 5색 팔레트로 환원 금지. 실제는 8 family × 10 step = 80개 ramp 기반이다.
- Dual-layer 카드 섀도(Stripe식) 적용 금지. Tailwind single ring/shadow가 기본.
