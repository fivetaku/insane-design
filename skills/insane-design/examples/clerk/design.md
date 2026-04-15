---
slug: clerk
service_name: Clerk
site_url: https://clerk.com
fetched_at: 2026-04-11
default_theme: dark
brand_color: "#6C47FF"
primary_font: Suisse Intl
font_weight_normal: 400
token_prefix: clerk
---

# DESIGN.md — Clerk (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Clerk의 웹사이트는 밝은 배경에 보라 accent(`#6C47FF`)가 결합된 인증 플랫폼 디자인이다. 깔끔하면서도 신뢰감 있는 인상이 보안 관련 서비스로서의 전문성을 전달한다.

타이포그래피는 기본 시스템 서체를 사용한다. 본문 weight는 **400**이며, 깔끔하고 균형 잡힌 읽기 경험을 제공한다.

브랜드 퍼플 `#6C47FF`가 CTA와 주요 인터랙션 요소에 사용된다. 밝은 배경 위에서 보라색이 강한 시각적 포인트를 만들며, 인증/보안 맥락에서의 신뢰감을 보조한다.

**Key Characteristics:**
- **Dual-accent 시스템** 사용: 보라 `#6C47FF` interactive + 시안 `#5DE3FF` addon/live.
- 다크 테마 기본값: bg `#131316`, surface `#1A1B1F`, elevated `#2F3037`, 5-step pure gray ramp.
- **Suisse Intl** (body) + **Geist Numbers** (OTP/숫자) + **Söhne Mono** (code) 3-폰트 분리.
- OTP / 숫자 UI에 `font-variant-numeric: tabular-nums` 강제.
- Variable font 특수 weight `450`, `510` 활용 가능.
---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Clerk처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — Suisse Intl 본문 + Geist Numbers 숫자 전용 */
:root {
  --font-sans: "Suisse Intl", "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
  --font-numbers: "Geist", "SF Pro Display", system-ui, sans-serif;
  --font-mono: "Söhne Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
}
body { font-family: var(--font-sans); font-weight: 400; }

/* 2. 다크 배경 + 화이트 */
:root { --root-bg: #131316; --text: #FFFFFF; --muted: #747686; }
body { background: var(--root-bg); color: var(--text); }

/* 3. 브랜드 보라 + 시안 addon */
:root { --brand: #6C47FF; --addon: #5DE3FF; }
```

**절대 하지 말아야 할 것 하나**: Clerk의 브랜드는 **보라 단일색이 아니라 purple + cyan dual-accent**다. `#6C47FF` (primary interactive — switch thumb / focus ring)와 `#5DE3FF` (addon / live indicator)이 페어로 작동한다. 그리고 surface는 **purple-tinted가 아니라 pure gray ramp** (`#131316 → #2F3037 → #42434D`).

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://clerk.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| CSS files | 20개 번들 (Next.js App Router code split) · 총 572,718자 |
| Custom properties | 194개 |
| Color vars | 43개 / Shadow vars | 7개 / Spacing vars | 9개 |
| Unique hex | 533개 (마케팅 + 대시보드 프리뷰 포함) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js App Router (route-level CSS split, 20 bundles)
- **Design system**: 커스텀 내부 DS + Tailwind 혼용 (`--tw-ring-color`, `--typography-*`, `--root-bg`)
- **CSS architecture**: 라이트/다크 dual-slot 패턴
  ```
  root tier       --root-bg: var(--light,#f7f7f8) var(--dark,#131316)
  typography tier --typography-color / --typography-thead-border / --typography-link-icon-bg
  component tier  --switch-thumb-border-color-active, --input-border-color-focus
  ring system     --tw-ring-color 레이어드 shadow 조합
  ```
- **Class naming**: Tailwind 유틸 + 커스텀 (`typography-*`, `root-*`) 혼합
- **Default theme**: **다크** (bg `#131316`, 라이트 테마 toggle 존재)
- **Font loading**: `var(--font-suisse)` + `var(--font-geist-numbers)` Next.js font loader
- **Canonical anchor**: `#6C47FF` — `--switch-thumb-border-color-active`, focus ring brand

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary (body/display)**: `Suisse Intl` (Swiss Typefaces, paid license)
- **Numbers-only**: `Geist` (숫자/OTP 전용 — compose `var(--font-geist-numbers),var(--font-suisse)`)
- **Code/API keys**: `Söhne Mono` (Klim Type Foundry, paid)
- **Weights used**: `100 / 400 / 450 / 500 / 510 / 600 / 700 / 800` — `450`과 `510`은 variable font 비표준 값

```css
:root {
  --font-sans:    "Suisse Intl", "Inter", ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --font-numbers: "Geist", "SF Pro Display", ui-sans-serif, system-ui, sans-serif;
  --font-mono:    "Söhne Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}
body {
  font-family: var(--font-sans);
  font-weight: 400;
}
.otp-code, .timer, .metric {
  /* Clerk는 숫자 전용 폰트 분리 — OTP 6자리 표시에서 고정폭 + 일관된 획 */
  font-family: var(--font-numbers), var(--font-sans);
  font-variant-numeric: tabular-nums;
}
```

> Suisse Intl과 Söhne Mono는 모두 유료 상용 폰트. 오픈소스 대체: Suisse → `Inter` / `Inter Display`, Söhne Mono → `JetBrains Mono` 또는 `IBM Plex Mono`.

---

## 05. Typography Scale
<!-- SOURCE: auto (rem frequency) -->

| Role | rem | px | Weight | Usage |
|---|---|---|---|---|
| display xl | 4rem | 64 | 500 | hero headline |
| display lg | 2rem | 32 | 500~600 | 섹션 H1 (freq 11) |
| h2 | 1.5rem | 24 | 500 | 피처 제목 (freq 7) |
| h3 | 1.25rem | 20 | 500 | 카드 제목 (freq 7) |
| body lg | 1.125rem | 18 | 400 | lead text (freq 17) |
| body | 1rem | 16 | 400 | 기본 본문 (freq 9) |
| body sm | 0.9375rem | 15 | 400 | dense body (freq 16) |
| body xs | 0.875rem | 14 | 500 | UI 라벨 (freq 11) |
| meta | 0.8125rem | 13 | 400 | 표 / 캡션 (freq 25 — 최다) |
| micro | 0.75rem | 12 | 500 | helper text (freq 16) |
| tiny | 0.6875rem | 11 | 500 | badge / tag (freq 15) |
| mini | 0.625rem | 10 | 500 | 극소 라벨 (freq 14) |

> ⚠️ 최다 빈도 size는 `0.8125rem` (13px) — Clerk의 dense UI 감성. 일반 SaaS 16px 기본과 다름. Weight는 variable font 특수 값 `450`, `510`이 실제 4회/1회 사용되어 semibold 근처를 미세 조정.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand (primary interactive purple)
| Token | Hex |
|---|---|
| `--switch-thumb-border-color-active` (anchor) | `#6C47FF` ⭐ |
| brand hover | `#5A3AE0` (유추 step) |
| brand pressed | `#4B2FBC` |
| brand subtle fg | `#9A85FF` |
| brand bg subtle | `#1A1630` (dark-mode tint) |

### 06-2. Addon (cyan — live indicator)
| Token | Hex |
|---|---|
| primary cyan | `#5DE3FF` |
| cyan variant | `#64E5FF` |
| cyan dim | `#3DB8D9` |

> Clerk의 **dual-accent** 시스템: purple은 interactive (버튼/switch/focus), cyan은 passive indicator (연결 상태, 라이브, addon).

### 06-3. Neutral Ramp (dark-first)

| Step | Dark (실제 `--root-bg` 다크 슬롯) | Light (라이트 슬롯) |
|---|---|---|
| 0 | `#000000` | `#FFFFFF` |
| 50 | `#131316` ⭐ (page bg) | `#F7F7F8` |
| 100 | `#212126` | `#EEEEF0` |
| 200 | `#2F3037` (card elev) | `#E4E4E9` |
| 300 | `#42434D` | `#D9D9DE` |
| 400 | `#5E5F6E` (muted text) | `#BABAC4` |
| 500 | `#747686` (subtext) | `#9B9CA8` |
| 700 | `#9A9BA7` | `#5E5F6E` |
| 900 | `#FFFFFF` | `#131316` |

### 06-5. Semantic
| Token | Hex | Usage |
|---|---|---|
| `--typography-color` | `#FFFFFF` (dark) | body text |
| `--typography-thead-border` | `#2F3037` | table header border |
| `--typography-link-icon-bg` | `#6C47FF` subtle | link arrow bg |
| `--input-border-color-focus` | `#6C47FF` | input focused border |
| `--input-root-background-color` | `#1A1B1F` | input bg (dark) |
| `--hover-bg` | `#212126` | row hover |
| `--active-bar-bg` | `#2F3037` | nav active indicator |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--root-bg` | `var(--light,#F7F7F8) var(--dark,#131316)` | 페이지 배경 (dual-slot) |
| `--page-color` | `var(--light,#131316) var(--dark,#FFFFFF)` | 페이지 텍스트 |
| `--switch-thumb-border-color-active` | `#6C47FF` | 활성 스위치 테두리 |
| `--input-border-color-focus` | `#6C47FF` | 폼 포커스 링 |
| `--tw-ring-color` | `#6C47FF` | Tailwind ring 색 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#131316` | 322 | page bg dark |
| 2 | `#FFFFFF` | 208 | primary text |
| 3 | `#000000` | 85 | stroke / logo |
| 4 | `#2F3037` | 52 | surface elevated |
| 5 | `#5E5F6E` | 42 | subtext muted |
| 6 | `#747686` | 38 | secondary text |
| 7 | `#5DE3FF` | 35 | cyan addon |
| 8 | `#64E5FF` | 30 | cyan variant |
| 9 | `#6C47FF` | 29 | **brand purple** |
| 10 | `#212126` | 24 | card bg |

---

## 07. Spacing
<!-- SOURCE: auto -->

Clerk은 Tailwind spacing 유틸을 그대로 사용 + 9개 커스텀 변수만 노출. 실질 스케일:

| Step | rem | px | Use case |
|---|---|---|---|
| 0.5 | 0.125rem | 2 | hairline |
| 1 | 0.25rem | 4 | icon gap |
| 2 | 0.5rem | 8 | dense chip |
| 3 | 0.75rem | 12 | button inset |
| 4 | 1rem | 16 | card padding |
| 5 | 1.25rem | 20 | form stack |
| 6 | 1.5rem | 24 | section internal |
| 8 | 2rem | 32 | card-to-card |
| 10 | 2.5rem | 40 | section gap |
| 12 | 3rem | 48 | large section |
| 16 | 4rem | 64 | hero padding |

---

## 08. Radius
<!-- SOURCE: auto -->

| Value | Context |
|---|---|
| `1.5px` | hairline accent |
| `3px` | chip |
| `4px` | input / tag |
| `5px` | small button |
| `11px` | card corner (signature) |
| `22px` | large card corner |
| `23px` | elevated card |
| `50px` | pill small |
| `999px` / `9999px` | pill full (button, avatar) |

> Clerk의 특이점: **11px / 22px / 23px** 같은 비표준 radius를 카드에 사용. 이는 inset shadow border를 고려한 **"optically correct"** 보정값 — 12px로 보이게 하려면 border 1px 분을 빼야 11px.

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| **glass card** | `inset 0 0 0 .5px #FFFFFFB3, 0 0 0 .5px #1313161A, 0 1px 1px #0000000D` | inset highlight + border + 1px drop |
| **elevated popover** | `0 10px 32px #21212626, 0 1px 1px #0000000D, 0 0 0 1px var(--tw-ring-color), 0 4px 6px #21212614, 0 24px 68px #2121261A` | dropdown, context menu |
| **focus ring brand** | `0 1px 1px #2B2B343D, 0 2px 3px #2B2B3433, inset 0 1px 1px #FFFFFF12, 0 0 0 1px #6C47FF` | focused input with brand outline |
| **modal xl** | `0 24px 68px #2121261A, 0 4px 6px #21212614, 0 10px 32px #21212626` | Sign In 모달 |

> **패턴**: 모든 elevation이 **inset highlight + 1px border + outer drop shadow**의 3-5 레이어 구성. Stripe의 dual-shadow보다 한 단계 복잡 — "glass card + brand ring" 시그니처.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Breakpoint | Width | Key Changes |
|---|---|---|
| Mobile | <640px | 단일 컬럼, 헤딩 축소, 카드 스택 |
| Tablet | 640-1024px | 2열 그리드, 중간 패딩 |
| Desktop | 1024-1280px | 풀 레이아웃, 3열 그리드 |
| Large | >1280px | 중앙 정렬 max-width 1200px, 넉넉한 마진 |

> ⚠️ Clerk는 모바일 퍼스트 반응형 디자인을 채택하며, 브레이크포인트별로 그리드와 타이포그래피가 유동적으로 조정된다.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Sign In Card (Clerk의 flagship 컴포넌트)
- **Background**: `#1A1B1F` (solid dark) 또는 semi-transparent with backdrop-blur
- **Border**: `1px solid #2F3037`
- **Inner highlight**: `inset 0 0 0 .5px #FFFFFFB3`
- **Radius**: `22px` 또는 `23px`
- **Shadow**: glass card atomic (§09)
- **Padding**: `32px 40px`
- **Title**: Suisse Intl 24px / 500
- **Body**: Suisse Intl 15px / 400

```html
<div class="clerk-card">
  <h1>Sign in to Acme</h1>
  <p class="text-muted">Welcome back! Please sign in to continue.</p>
  <form>
    <input type="email" placeholder="Email address" />
    <button class="btn-primary">Continue</button>
  </form>
</div>
```

### Primary button
- **Background**: `#FFFFFF` (dark mode — 반전) 또는 `#131316` (light mode)
- **Text**: 반전 컬러
- **Radius**: `8px` 또는 `11px`
- **Font**: Suisse Intl 14px / 500
- **Padding**: `10px 16px`
- **Focus ring**: brand purple `0 0 0 2px #6C47FF`

### OTP Input (6-digit)
- **Font**: Geist Numbers (숫자 전용 폰트)
- **Size**: 24px / 500
- **Slot bg**: `#1A1B1F`
- **Slot border**: `#2F3037`, focused `#6C47FF`
- **Slot radius**: `11px`
- **Variant**: `tabular-nums` 고정폭

### Switch (signature)
- **Track bg (off)**: `#42434D`
- **Track bg (on)**: `#6C47FF` subtle
- **Thumb**: `#FFFFFF`
- **Thumb border active**: `#6C47FF` (이 변수가 brand anchor)
- **Radius**: `9999px`

### Addon indicator (live / connected)
- **Dot**: `#5DE3FF` (cyan)
- **Pulse**: `0 0 0 4px rgba(93, 227, 255, 0.3)`
- **Text**: "Live", "Connected", "Active"

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Clerk — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-sans:    "Suisse Intl", "Inter", ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --font-numbers: "Geist", "SF Pro Display", ui-sans-serif, sans-serif;
  --font-mono:    "Söhne Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;

  /* Surfaces (dark-first) */
  --root-bg:       #131316;
  --surface:       #1A1B1F;
  --surface-elev:  #2F3037;
  --surface-high:  #42434D;

  /* Text */
  --text:          #FFFFFF;
  --text-muted:    #747686;
  --text-subtle:   #5E5F6E;

  /* Border */
  --border:        #2F3037;
  --border-strong: #42434D;

  /* Brand (dual accent) */
  --brand:         #6C47FF;  /* interactive — buttons, focus, switch */
  --brand-hover:   #5A3AE0;
  --addon:         #5DE3FF;  /* passive — live indicator, addon */
  --addon-var:     #64E5FF;

  /* Radius (optically-corrected) */
  --radius-xs: 4px;
  --radius-sm: 5px;
  --radius-md: 11px;   /* card corner — appears as 12px with 1px border */
  --radius-lg: 22px;   /* large card */
  --radius-xl: 23px;   /* elevated modal */
  --radius-full: 9999px;

  /* Glass card shadow atomic */
  --shadow-glass:
    inset 0 0 0 0.5px rgba(255,255,255,0.7),
    0 0 0 0.5px rgba(19,19,22,0.1),
    0 1px 1px rgba(0,0,0,0.05);

  --shadow-elevated:
    0 10px 32px rgba(33,33,38,0.15),
    0 1px 1px rgba(0,0,0,0.05),
    0 4px 6px rgba(33,33,38,0.08),
    0 24px 68px rgba(33,33,38,0.1);

  --shadow-focus-brand:
    0 1px 1px rgba(43,43,52,0.24),
    0 2px 3px rgba(43,43,52,0.2),
    inset 0 1px 1px rgba(255,255,255,0.07),
    0 0 0 1px #6C47FF;
}

body {
  font-family: var(--font-sans);
  font-weight: 400;
  background: var(--root-bg);
  color: var(--text);
}

.otp-code, .metric, .timer {
  font-family: var(--font-numbers);
  font-variant-numeric: tabular-nums;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Clerk
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#6C47FF',
          hover:   '#5A3AE0',
          pressed: '#4B2FBC',
          subtle:  '#9A85FF',
        },
        addon: {
          DEFAULT: '#5DE3FF',
          bright:  '#64E5FF',
          dim:     '#3DB8D9',
        },
        surface: {
          root:     '#131316',
          base:     '#1A1B1F',
          elevated: '#2F3037',
          high:     '#42434D',
        },
        ink: {
          DEFAULT: '#FFFFFF',
          muted:   '#747686',
          subtle:  '#5E5F6E',
        },
      },
      fontFamily: {
        sans:    ['"Suisse Intl"', '"Inter"', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        numbers: ['"Geist"', '"SF Pro Display"', 'ui-sans-serif', 'sans-serif'],
        mono:    ['"Söhne Mono"', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      },
      fontWeight: {
        thin:     '100',
        normal:   '400',
        'normal+':'450', /* variable font */
        medium:   '500',
        'medium+':'510',
        semibold: '600',
        bold:     '700',
      },
      borderRadius: {
        sm:    '5px',
        DEFAULT:'8px',
        md:    '11px', /* optical 12 */
        lg:    '22px',
        xl:    '23px',
        full:  '9999px',
      },
      boxShadow: {
        glass: 'inset 0 0 0 .5px rgba(255,255,255,0.7), 0 0 0 .5px rgba(19,19,22,0.1), 0 1px 1px rgba(0,0,0,0.05)',
        elevated: '0 10px 32px rgba(33,33,38,0.15), 0 24px 68px rgba(33,33,38,0.1)',
        'focus-brand': '0 0 0 2px #6C47FF',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference
| Role | Hex |
|---|---|
| Primary CTA | `#6C47FF` |
| Heading text | `#131316` |
| Body text | `#5E5F6E` |
| Background | `#FFFFFF` |
| Border | `#EBEBED` |
| Link | `#6C47FF` |
| Dark section | `#131316` |

### Example Component Prompts
- "Create a hero section on `#FFFFFF` background. Headline at 3rem `Suisse Intl` weight 400. CTA button `#6C47FF` with white text."
- "Design a card: `#1c1c1f` background, `#EBEBED` border, 12px radius. Body text `#5E5F6E` at weight 400."

### Iteration Guide
1. 폰트: `Suisse Intl` 패밀리, 본문 weight 400
2. 컬러: 브랜드 `#6C47FF`는 CTA/링크에만 집중. 배경 `#FFFFFF`, 텍스트 `#131316`
3. 그림자: 부드러운 box-shadow로 카드 elevation 표현
---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- **Dual-accent 시스템** 사용: 보라 `#6C47FF` interactive + 시안 `#5DE3FF` addon/live.
- 다크 테마 기본값: bg `#131316`, surface `#1A1B1F`, elevated `#2F3037`, 5-step pure gray ramp.
- **Suisse Intl** (body) + **Geist Numbers** (OTP/숫자) + **Söhne Mono** (code) 3-폰트 분리.
- OTP / 숫자 UI에 `font-variant-numeric: tabular-nums` 강제.
- Variable font 특수 weight `450`, `510` 활용 가능.
- **Glass card** shadow 원자: `inset highlight + 0.5px border + 1px drop` 3-layer.
- Focus ring에 brand purple `0 0 0 1px #6C47FF` (Clerk 시그니처).
- 카드 radius `11px` / `22px` / `23px` (optically-corrected, border 1px 보정).
- `--root-bg: var(--light, ...) var(--dark, ...)` 듀얼 슬롯 패턴.

### ❌ DON'T
- ❌ **Purple-tinted surface** 사용 (`#1F0256` 같은 건 0회) — 실제 surface는 pure gray.
- ❌ 단일 브랜드 컬러 — 보라 없이 시안만, 또는 시안 없이 보라만 쓰면 dual-accent 정체성 소실.
- ❌ `Inter` 단독 본문 — Suisse Intl과 시각적으로 달라 premium 감성 소실.
- ❌ OTP 숫자를 Inter로 — Clerk은 숫자 전용 폰트 분리가 브랜드 포인트.
- ❌ `font-weight: 700` 본문 — Clerk은 `500`/`510`이 일반적인 강조 weight.
- ❌ Flat single-layer shadow — "glass card + brand ring" 시그니처가 flat card로 변질.
- ❌ `color-brand` / `color-gray-*` flat 네이밍 — 실제는 `--root-bg`, `--typography-color` semantic.
- ❌ 짝수 radius (12px, 16px) 사용 — optical 11px / 22px로 보정해야 border 포함 시 12/24로 보인다.

---

