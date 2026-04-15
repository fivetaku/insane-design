---
slug: tinybird
service_name: Tinybird
site_url: https://www.tinybird.co
fetched_at: 2026-04-11
default_theme: light
brand_color: "#008060"
primary_font: Roboto
font_weight_normal: 400
token_prefix: "--primary, --secondary, --dark (unscoped)"
---

# DESIGN.md — Tinybird (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Tinybird는 실시간 데이터 플랫폼으로, 네온 그린과 warm navy의 대비가 특징적이다. Light hero에서는 네온 mint `#27F795`가, dark 섹션에서는 보정된 `#008060`(primary-dark)이 사용되는 듀얼 anchor 패턴을 가진다. Ink는 순수 gray가 아닌 warm navy `#25283D`로, 보라 기가 섞인 독특한 톤이다.

극단적 타이포 스케일이 시그니처다: 본문 13~20px과 display 56~128px 사이에 중간 스케일이 거의 없고, 7-segment decorative 폰트(`sevenSegment`)로 "1.2B rows/sec" 같은 거대 숫자를 표시한다. Radius는 0/4px + pill만 사용하는 의도적 브루탈리즘 스타일이다.

**Key Characteristics:**
- 듀얼 anchor: neon `#27F795`(light) / `#008060`(dark)
- Warm navy ink `#25283D` (순수 gray가 아님)
- Roboto (Inter가 아님!) + sevenSegment(decorative)
- 극단적 타이포 스케일: 13px body ↔ 128px display
- Radius 0/4px + pill — 의도적 브루탈리즘

---

## 01. Quick Start

> 5분 안에 Tinybird처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트: Roboto sans + Roboto Mono (Google Fonts) */
:root {
  --font-roboto: "Roboto", "Roboto Fallback", -apple-system, system-ui, sans-serif;
  --font-roboto-mono: "Roboto Mono", "Roboto Mono Fallback", ui-monospace, monospace;
  --font-sans: var(--font-roboto);
  --font-mono: var(--font-roboto-mono), monospace;
}
body {
  font-family: var(--font-sans);
  font-weight: 400;  /* Roboto 400, 500 medium, 700 bold */
}
code, pre { font-family: var(--font-mono); }

/* 2. 배경 + 텍스트 (light 랜딩, #25283d ink) */
:root { --white: #fff; --dark: #25283d; --black: #000; }
body { background: var(--white); color: var(--dark); }

/* 3. 브랜드 네온 그린 + 다크 네이비 */
:root {
  --primary: #27F795;       /* 네온 mint 그린 — hero 액센트 */
  --primary-dark: #008060;  /* dark surface 위 variant, 48회 dominant */
  --secondary: #2D27F7;     /* 보라-블루 보조 */
}
```

**절대 하지 말아야 할 것 하나**: Tinybird 의 "브랜드 그린 = `#27F795` 단일" 이라고 가정하지 말 것. 실제 CSS 빈도에서 <b>dominant 1위는 `#008060` (48회)</b> — 이건 dark 배경에서 네온 그린이 너무 튀지 않도록 보정한 `--primary-dark` 변형이다. Light hero 에서만 네온 `#27F795` 를 쓰고, dark/서브 섹션에서는 `#008060` 를 써야 실제 사이트와 같아진다. 그리고 두 번째로 중요한 것: "neutral" 은 순수 gray 가 아니라 <b>`#25283d` warm navy ink</b>. `#111827` / `#1F2937` 같은 Tailwind slate 로 대체하면 색온도가 틀린다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.tinybird.co` |
| Fetched | 2026-04-11 |
| CSS files | 3개 외부, 총 156,400자 |
| Primary bundle | `a1b23965c7e116e5.css` (Next.js + Tailwind) |
| Token count | 196 custom properties · 18 color · 12 spacing · 13 shadow |
| Token prefix | 없음 (unscoped: `--primary`, `--secondary`, `--dark`) + `--tw-*` (Tailwind internal) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js + Tailwind CSS
- **Design system**: 이름 없는 자체 토큰 + Tailwind 기본. Tailwind v3 스타일 (`--tw-*` 인터널 프로퍼티 사용).
- **CSS architecture**: Flat — prefix 없이 `--primary`, `--secondary`, `--dark`, `--white` 직접 노출
  ```
  --font-{roboto, roboto-mono, fira-mono, seven-segment}   폰트 체인
  --font-weight-{normal, medium, semibold, bold}          weight scale
  --primary, --primary-dark, --secondary, --secondary-light  brand
  --error, --warning                                       state
  --blog-{product,built,data,engineering,architecture,ai} 블로그 카테고리
  --callout-{note,important,warning,caution,tip}          콜아웃 라벨
  ```
- **Class naming**: Tailwind utilities + 커스텀 클래스 혼합
- **Default theme**: **light**. 페이지 배경 `#FFFFFF`, ink `#25283d` warm navy.
- **Font loading**: Next.js font loader — Roboto + Roboto Mono + Fira Mono + sevenSegment (7-segment display 폰트, 숫자 쇼케이스 전용)
- **Canonical anchor**: `#27F795` (light) / `#008060` (dark) — dual anchor.

---

## 04. Font Stack

- **Primary sans**: `Roboto` (Google Fonts, Next.js loader)
- **Primary mono**: `Roboto Mono`
- **Secondary mono**: `Fira Mono` (22회 등장 — 블로그 코드 블록 전용)
- **Decorative**: `sevenSegment` (3회 — "1.2B rows/sec" 같은 숫자 디스플레이)
- **Weight scale**: 300 / 400 / 500 / 700 (w300 은 light heading 전용, 15회)

```css
:root {
  --font-roboto: "Roboto", "Roboto Fallback", -apple-system, system-ui, sans-serif;
  --font-roboto-mono: "Roboto Mono", "Roboto Mono Fallback", ui-monospace, monospace;
  --font-fira-mono: "Fira Mono", "Fira Mono Fallback", monospace;
  --font-seven-segment: "sevenSegment", "sevenSegment Fallback", monospace;
  --font-sans: var(--font-roboto);
  --font-mono: var(--font-roboto-mono), monospace;

  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
}
body { font-family: var(--font-sans); font-weight: 400; }
code, pre { font-family: var(--font-mono); }
.metric-display { font-family: var(--font-seven-segment); }
```

> ⚠️ **Inter 가 아니다.** Next.js 사이트의 거의 90% 가 Inter 를 쓰는 것과 달리 Tinybird 는 `Roboto` 를 유지한다. 이건 "Google Analytics / Material 2010s" 느낌을 의도적으로 유지하는 것. Mono 체인은 <code>Roboto Mono</code>(기본) + <code>Fira Mono</code>(블로그) 이중화.

---

## 05. Typography Scale

| Size | px | Weight | Usage |
|---|---|---|---|
| `.8125rem` | 13px | 400 | 캡션 · 메타데이터 |
| `.875rem` | 14px | 400 (3회) | UI small |
| `.9375rem` | 15px | 400 | 본문 small |
| `1.25rem` | 20px | 500 | 카드 타이틀 |
| `2.8125rem` | 45px | 700 | H2 |
| `3.5rem` | 56px | 700 | H1 |
| `6.3125rem` | 101px | 700 | hero giant number |
| `8rem` | 128px | 700 | 풀블리드 숫자 디스플레이 |

> ⚠️ **극단적 스케일.** Tinybird 는 본문(13~20px)과 display(56~128px) 사이에 중간 스케일이 거의 없다. Hero 에는 압도적으로 큰 <code>6.3125rem</code>/<code>8rem</code> 숫자 폰트(7-segment decorative 폰트 포함)가 쓰이고, 나머지는 Roboto 14px 본문 위주. "huge metric + tight body" 가 signature.

---

## 06. Colors

### 06-1. Brand Dual Anchor

| Token | Hex | Count | Usage |
|---|---|---|---|
| `--primary` | `#27F795` | 3 | **네온 mint — light hero 전용** |
| `--primary-dark` ★ | `#008060` | **48** | dark 배경 위 variant (실제 dominant) |
| `--secondary` | `#2D27F7` | — | 보라-블루 보조 |
| `--secondary-light` | `#00C1FF` | — | cyan hint |

### 06-2. Neutral / Ink

| Token | Hex | Count |
|---|---|---|
| `--white` | `#FFFFFF` | 11 |
| `--dark` ★ | `#25283D` | — (ink 기본) |
| `--black` | `#000000` | 3 |
| surface alt | `#262626` | 5 |
| surface mid | `#3C3C3C` | 2 |
| surface | `#2E2E2E` | — |

### 06-3. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--error` | `#FF8389` | 에러 (pastel red) |
| `--warning` | `#FC9F5B` | 경고 (peach) |
| `#800000` | `#800000` | 34회! (실제 raw hex 2위) — 레거시 maroon |
| `#61C454` | `#61C454` | success/accent |
| `#EC6D62` | `#EC6D62` | error bright |
| `#F5C451` | `#F5C451` | warning bright |

### 06-4. Blog Category Colors

| Token | Hex | Category |
|---|---|---|
| `--blog-product` | `#00FF00` | product |
| `--blog-built` | `#0000FF` | built with tinybird |
| `--blog-data` | `#FFFF00` | data |
| `--blog-engineering` | `#00DDDD` | engineering |
| `--blog-architecture` | `#FF8040` | architecture |
| `--blog-ai` | `#8080FF` | ai |

### 06-5. Callout Colors (GitHub-style)

| Token | Hex | Type |
|---|---|---|
| `--callout-note` | `#4493F8` | note |
| `--callout-important` | `#AB7DF8` | important |
| `--callout-warning` | `#D29922` | warning |
| `--callout-caution` | (pattern) | caution |
| `--callout-tip` | (pattern) | tip |

### 06-6. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#008060` | 48 | **primary-dark** (dark surface 위 green) |
| 2 | `#800000` | 34 | legacy maroon |
| 3 | `#FFFFFF` | 11 | 페이지 배경 |
| 4 | `#262626` | 5 | dark surface |
| 5 | `#61C454` | 5 | green success |
| 6 | `#EC6D62` | 5 | error bright |
| 7 | `#F5C451` | 5 | warning |
| 8 | `#27F795` | 3 | **primary (hero 네온)** |

> ⚠️ **Dominant 1위가 `#008060` 인 이유.** Light hero 는 `#27F795` 네온을 쓰지만, 페이지 하단 섹션·푸터·다크 카드에서는 그 네온이 눈부시기 때문에 `#008060` 어두운 변형을 쓴다. 그래서 CSS 빈도 카운트에서 어두운 쪽이 훨씬 많다.

---

## 07. Spacing

12 개의 spacing 커스텀 프로퍼티 + Tailwind 기본 스케일. 커스텀은 주로 레이아웃 전용.

| Token | Value |
|---|---|
| `.25rem` | 4px |
| `.5rem` | 8px |
| `.75rem` | 12px |
| `1rem` | 16px |
| `1.5rem` | 24px |
| `2rem` | 32px |
| `3rem` | 48px |
| `4rem` | 64px |

---

## 08. Radius

`unique_radius_values = 2` — 단 두 개의 raw radius 값만 사용!

| Token | Value | Usage |
|---|---|---|
| sharp | `0` / `.25rem` | 대부분의 버튼·카드 (브루탈리즘 영향) |
| pill | `9999px` | 완전 원형 (avatar, chip) |

> ⚠️ **Minimal radius.** Tinybird 는 거의 각진 디자인 (`border-radius: 0` 또는 4px) + 원형 pill 두 모드만 쓴다. 8px/12px/16px 같은 중간값이 거의 없다 — 의도적 브루탈리즘.

---

## 09. Shadows

13 개의 shadow 커스텀 프로퍼티 있지만 실제 사용은 최소한 (minimal brutalism).

| Level | Value | Usage |
|---|---|---|
| shadow-sm | `0 1px 2px 0 rgba(0,0,0,0.05)` | 미세 |
| shadow | `0 1px 3px 0 rgba(0,0,0,0.1), 0 1px 2px -1px rgba(0,0,0,0.1)` | 카드 |
| shadow-md | `0 4px 6px -1px rgba(0,0,0,0.1)` | 카드 hover |
| drop-shadow-brand | `0 0 0 2px #27F795` | 네온 outline (hero 전용) |

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

### Button (primary — hero neon)

```html
<a class="btn btn-primary">Start free</a>
```

```css
.btn-primary {
  background: var(--primary);        /* #27F795 */
  color: var(--dark);                 /* #25283D */
  font-family: var(--font-roboto);
  font-weight: 700;
  padding: 12px 24px;
  border-radius: 4px;
  border: 0;
}
.btn-primary:hover { background: var(--primary-dark); color: #fff; }
```

### Button (secondary — outlined)

```html
<a class="btn btn-secondary">Read docs</a>
```

```css
.btn-secondary {
  background: transparent;
  color: var(--dark);
  border: 1px solid var(--dark);
  padding: 12px 24px;
  border-radius: 4px;
}
```

### Big number display (7-segment)

```html
<div class="metric">
  <span class="metric__value">1.2B</span>
  <span class="metric__label">rows/sec</span>
</div>
```

```css
.metric__value {
  font-family: var(--font-seven-segment);
  font-size: 6.3125rem;     /* 101px */
  color: var(--primary);
  line-height: 1;
}
```

### Code block (Roboto Mono)

```html
<pre><code>SELECT count() FROM events WHERE ...</code></pre>
```

```css
pre {
  background: #25283D;
  color: #27F795;
  padding: 16px 20px;
  border-radius: 0;       /* 각진 */
  font-family: var(--font-mono);
  font-size: 14px;
}
```

---

## 15. Drop-in CSS

```css
/* Tinybird — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-roboto: "Roboto", "Roboto Fallback", system-ui, sans-serif;
  --font-roboto-mono: "Roboto Mono", "Roboto Mono Fallback", monospace;
  --font-sans: var(--font-roboto);
  --font-mono: var(--font-roboto-mono), monospace;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;

  /* Brand dual */
  --primary: #27F795;          /* ← neon — light hero 전용 */
  --primary-dark: #008060;     /* ← dominant — dark 섹션 */
  --secondary: #2D27F7;
  --secondary-light: #00C1FF;

  /* Surfaces */
  --white: #FFFFFF;
  --dark: #25283D;             /* warm navy ink */
  --black: #000000;

  /* Semantic */
  --error: #FF8389;
  --warning: #FC9F5B;
}

body {
  font-family: var(--font-sans);
  font-weight: 400;
  background: var(--white);
  color: var(--dark);
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Tinybird
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#27F795',   // neon (hero)
          dark:    '#008060',   // dominant
        },
        secondary: {
          DEFAULT: '#2D27F7',
          light:   '#00C1FF',
        },
        dark:    '#25283D',     // warm navy ink
        error:   '#FF8389',
        warning: '#FC9F5B',
      },
      fontFamily: {
        sans:  ['Roboto', 'Roboto Fallback', 'system-ui', 'sans-serif'],
        mono:  ['Roboto Mono', 'Roboto Mono Fallback', 'ui-monospace', 'monospace'],
        segment: ['sevenSegment', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
        bold:   '700',
      },
      borderRadius: {
        none: '0',
        sm:   '.25rem',
        full: '9999px',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: auto+manual -->

### Quick Color Reference

| Role | Value |
|---|---|
| Brand | `#008060` |
| Page BG | `#FFFFFF` |
| Text Primary | `#000000` |
| Default Theme | light |

### Component Prompts

> **Hero section**: "Tinybird 스타일 hero — `Roboto` 폰트, `#008060` brand color, light 배경"
>
> **CTA button**: "Tinybird primary CTA — brand `#008060` 배경 또는 dark fill, `Roboto` 폰트"
>
> **Card component**: "Tinybird 스타일 카드 — light 테마, 기존 radius/shadow 토큰 준수"

### Iteration Guide

1. **Color 교체 시**: 반드시 §06 Colors 테이블의 실제 hex 참조. AI 추론 색상 사용 금지.
2. **Typography 변경 시**: §04 Font Stack의 font-family 체인 + §05의 weight/size 매핑 확인.
3. **Spacing 조정 시**: §07 Spacing의 토큰 스케일 내에서만 변경.
4. **신규 컴포넌트**: §13 Components의 기존 패턴(radius, shadow, padding)을 기반으로 확장.

---

## 18. DO / DON'T

### ✅ DO
- 듀얼 anchor 패턴: light hero 는 <code>#27F795</code>, dark 섹션은 <code>#008060</code>.
- Ink 는 warm navy <code>#25283D</code> — 순수 gray 아님.
- Body 는 <code>Roboto</code> (Inter 아님!), mono 는 <code>Roboto Mono</code>.
- 큰 숫자 디스플레이에 <code>sevenSegment</code> decorative 폰트 — "1.2B rows/sec" 식 강조.
- Radius 는 0 또는 4px (각진 브루탈리즘) + 9999px pill 두 모드만.
- 블로그 카테고리별 <code>--blog-*</code> 토큰 사용 (product=green, built=blue, data=yellow 등).
- Callout 은 GitHub-style note/important/warning/caution/tip 5종.

### ❌ DON'T
- ❌ <code>#27F795</code> 하나로 dark/light 모두 — dark 섹션에서 눈 시림. <code>#008060</code> 변형 필수.
- ❌ <code>Inter</code> 로 대체 — Roboto 특유의 Material 2010s 톤이 깨짐.
- ❌ "neutral = slate-900" — Tinybird 는 warm navy <code>#25283D</code> (보라 기가 있음).
- ❌ 8px/12px/16px 라운드 코너 — 실제는 0/4px + pill 만.
- ❌ <code>font-weight: 600</code> — Tinybird 는 400/500/700 주로 쓰고 600 은 거의 안 씀.
- ❌ Gradient 오버레이 기대 — Tinybird 는 거의 flat 색상.
- ❌ Mono 폰트로 <code>JetBrains Mono</code>/<code>Fira Code</code> — 실제는 Roboto Mono (Fira Mono 는 블로그만).
- ❌ 단일 브랜드 컬러 가정 — primary/primary-dark/secondary/secondary-light 4개 체인 필수.
