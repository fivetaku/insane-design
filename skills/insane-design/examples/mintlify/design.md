---
slug: mintlify
service_name: Mintlify
site_url: https://mintlify.com
fetched_at: 2026-04-11
default_theme: light
brand_color: "#0C8C5E"
primary_font: Inter
font_weight_normal: 400
token_prefix: color
---

# DESIGN.md — Mintlify (Claude Code Edition)

---

## 01. Quick Start

> 5분 안에 Mintlify처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — Inter (body) + Geist Mono (code), next/font 변수 방식 */
body {
  font-family: var(--font-inter), "Inter", "Inter Fallback", -apple-system, sans-serif;
  font-weight: 400;
}
code, pre {
  font-family: var(--font-geist-mono), "Geist Mono", "Geist Mono Fallback", ui-monospace, monospace;
}

/* 2. Warm light palette — cool gray 금지 */
:root {
  --color-background-main: #FFFFFF;
  --color-background-soft: #F1EFED;  /* warm off-white */
  --color-text-main:       #231F20;  /* warm black */
  --color-text-soft:       #4A5565;
  --color-border-solid:    #D1D5DC;
}
body { background: var(--color-background-main); color: var(--color-text-main); }

/* 3. 브랜드 teal */
:root {
  --color-brand:       #0C8C5E;
  --color-brand-light: #20808D;
}
```

**절대 하지 말아야 할 것 하나**: 홈페이지에 표시되는 고객 로고(PayPal `#003087`, Braintrust `#FF5A00`, Coinbase `#4B73FF`, PayPal blue `#009CDE` 등)의 hex를 Mintlify 브랜드 팔레트로 착각하지 말 것. 이 값들은 customer logo wall의 SVG 로고 색이며 Mintlify와 무관하다. 진짜 브랜드는 **teal `#0C8C5E`** 단일이다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://mintlify.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| Framework | Next.js + **Tailwind CSS v4** |
| Custom props | 253 (color: 54 · shadow: 16 · radius: 24 unique values) |
| Token prefix | `--color-*`, `--tw-*`, `--tw-prose-*`, `--twoslash-*`, `--font-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 |

---

## 03. Tech Stack

- **Framework**: Next.js + `next/font` (`--font-inter`, `--font-geist-mono` 변수 주입)
- **Design system**: **Tailwind v4 + 자체 semantic 레이어 하이브리드**
- **CSS architecture**:
  ```
  Tailwind v4 @theme              --color-{name}-{50..950} 팔레트 주입
  자체 semantic 레이어            --color-background-main / --color-text-main / --color-brand
  다크 모드: invert 패턴           --color-background-invert: var(--color-text-main)
  Prose (Tailwind Typography)     --tw-prose-*, --tw-prose-invert-*
  Twoslash (TS hover popup)       --twoslash-popup-bg, --twoslash-code-font
  ```
- **Class naming**: Tailwind 유틸리티 (`flex gap-4 rounded-lg bg-white ...`) + semantic 컴포넌트 클래스
- **Default theme**: **Light** (docs 페이지 기본)
- **Theme switch**: Invert 패턴 — `--color-background-invert`는 `var(--color-text-main)`을 참조. 두 값을 flip하면 다크 모드.
- **Font loading**: `next/font/google`로 Inter + Geist Mono 로드, **metric-matched fallback** (`Inter Fallback`, `Geist Mono Fallback`)

---

## 04. Font Stack

- **Display / Body**: `Inter` (via `var(--font-inter)`, Next.js `next/font/google`)
- **Code / Mono**: **`Geist Mono`** (via `var(--font-geist-mono)`, Vercel OSS)
- **Twoslash code**: `var(--twoslash-code-font)` — TS 타입 호버 팝업용 전용 변수
- **Metric fallback**: `Inter Fallback`, `Geist Mono Fallback` — 웹폰트 로딩 중 layout shift 방지

```css
:root {
  --font-inter:      "Inter", "Inter Fallback", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-geist-mono: "Geist Mono", "Geist Mono Fallback", ui-monospace, SFMono-Regular, Menlo, monospace;
}
body      { font-family: var(--font-inter); font-weight: 400; }
code, pre { font-family: var(--font-geist-mono); }
```

> ⚠️ Mintlify는 **Fira Code를 쓰지 않는다**. Vercel Geist Mono가 공식 코드 폰트. OSS 라이선스라 자유롭게 사용 가능.

---

## 05. Typography Scale

Mintlify는 `@tailwindcss/typography` (Prose) 플러그인 + `hero/section/card` 전용 스케일 혼합.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| hero-display | 40px (2.5rem) | 700 | 1.1  | -0.02em |
| hero-h1      | 34px          | 700 | 1.15 | -0.018em|
| h2           | 28px          | 600 | 1.25 | -0.014em|
| h3           | 20px          | 600 | 1.3  | -0.01em |
| h4           | 18px          | 600 | 1.4  | 0em     |
| body-lg      | 17px          | 400 | 1.6  | 0em     |
| body         | 15px          | 400 | 1.6  | 0em     |
| body-sm      | 13px          | 400 | 1.55 | 0em     |
| code-inline  | `0.875em`     | 500 | 1.5  | 0em     |
| prose-body   | em 기반       | 400 | 1.75 | 0em     |

> ⚠️ 문서 본문은 **em/% 기반** (Tailwind Prose convention). 16-18px base에 `.875em` / `1em` / `.888em` 같은 비율로 스케일.

---

## 06. Colors

### 06-1. Semantic Layer (Mintlify 자체)

| Token | Hex / Reference | Usage |
|---|---|---|
| `--color-background-main`     | `#FFFFFF`           | 페이지 bg |
| `--color-background-soft`     | `#F1EFED`           | **warm off-white** surface |
| `--color-background-gray-subtle`| `#F9FAFB`         | subtle surface |
| `--color-background-gray-emphasis`| `#F3F4F6`       | emphasized surface |
| `--color-background-invert`   | `var(--color-text-main)` | 다크 모드 bg (invert) |
| `--color-text-main`           | `#231F20`           | **warm black** primary text |
| `--color-text-soft`           | `#4A5565`           | secondary text |
| `--color-text-sub`            | `#6B7280`           | muted text |
| `--color-text-base-tertiary`  | `#9CA3AF`           | tertiary |
| `--color-text-invert`         | `var(--color-background-main)` | 다크 모드 text |
| `--color-border-sub`          | `#E5E7EB`           | subtle border |
| `--color-border-solid`        | `#D1D5DC`           | input border |
| `--color-border-soft`         | `#EEF0F2`           | soft divider |
| `--color-border-surface`      | `#E5E7EB`           | surface border |
| `--color-muted`               | `#6B7280`           | muted text (general) |
| `--color-muted-invert`        | `#9CA3AF`           | 다크 muted |

### 06-2. Brand

| Token | Hex | Usage |
|---|---|---|
| `--color-brand`       | `#0C8C5E` | 주 브랜드 teal (11회 실사용) |
| `--color-brand-light` | `#20808D` | 보조 teal / hover |
| `--color-accent-lime` | `#18E299` | 밝은 accent (다크 모드 CTA 가능성) |

### 06-3. Tailwind v4 Palette (inherited)

Mintlify는 Tailwind 기본 팔레트 (gray, red, blue, green 등)를 `--color-gray-100` 등으로 주입받는다. 주요 사용:

| Token | Hex |
|---|---|
| `--color-gray-100` | `#F3F4F6` |
| `--color-gray-200` | `#E5E7EB` |
| `--color-gray-300` | `#D1D5DC` |
| `--color-gray-600` | `#4A5565` |
| `--color-gray-900` | `#101828` |
| `--color-red-400`  | `#F87171` |

### 06-4. Prose / Twoslash

| Token | Hex | Usage |
|---|---|---|
| `--tw-prose-pre-bg`           | `#1E2939`  | code block bg (light mode) |
| `--tw-prose-quote-borders`    | `#E5E7EB`  | blockquote border |
| `--tw-prose-th-borders`       | `#D1D5DC`  | table header border |
| `--tw-prose-td-borders`       | `#E5E7EB`  | table cell border |
| `--tw-prose-invert-pre-bg`    | `rgba(0,0,0,0.5)` | 다크 모드 code bg |
| `--tw-prose-invert-quote-borders` | `#364153` | 다크 모드 blockquote |
| `--tw-prose-invert-th-borders`| `#4A5565`  | 다크 모드 table header |
| `--twoslash-popup-bg`         | `#F3F7F6`  | TS hover popup bg |
| `--twoslash-border-color`     | `#DBDFDE`  | popup border |
| `--twoslash-popup-shadow`     | `rgba(0,0,0,0.08) 0px 1px 4px` | popup shadow |

### 06-5. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 62 | page bg |
| 2 | `#231F20` | 46 | primary text (warm) |
| 3 | `#F1EFED` | 22 | warm off-white surface |
| 4 | `#003087` | 14 | PayPal logo (customer wall) |
| 5 | `#0C8C5E` | 11 | **brand teal** |
| 6 | `#FF5A00` | 10 | Braintrust logo |
| 7 | `#009CDE` | 10 | PayPal logo |
| 8 | `#0070E0` |  8 | PayPal logo |
| 9 | `#4B73FF` |  8 | Coinbase logo |
| 10| `#101828` |  6 | dark bg (invert) |

> **주의**: #4/6/7/8/9는 모두 customer logo wall의 제3자 로고 색이다. Mintlify 브랜드가 아니다.

---

## 07. Spacing

Tailwind v4 단일 base 패턴 (`--spacing: 0.25rem` = 4px) + 문서 플랫폼 특화 spacing.

| Token | Value | Use case |
|---|---|---|
| `--spacing`  | 0.25rem (4px) | base unit |
| p-2  | 8px  | tight |
| p-3  | 12px | inline |
| p-4  | 16px | card inner |
| p-6  | 24px | section inner |
| p-8  | 32px | block gap |
| p-12 | 48px | section gap |
| p-16 | 64px | hero padding |
| p-20 | 80px | major block |
| doc-sidebar-width | 280px | 좌측 네비 |
| doc-content-max   | 768px | 본문 가독폭 |

---

## 08. Radius

Mintlify는 24개의 고유 radius 값을 Tailwind 유틸로 사용. 최빈은 10px (5회).

| Token | Value | Context |
|---|---|---|
| rounded-xs | 2px  | inline code |
| rounded-sm | 4px  | small button |
| rounded-md | 6px  | input |
| rounded    | 8px  | button |
| rounded-lg | 10px | card (**최빈** — 5회) |
| rounded-xl | 12px | large card |
| rounded-2xl| 16px | modal |
| rounded-3xl| 20px | hero card |
| rounded-full| 9999px | pill, avatar |

---

## 09. Shadows

| Token | Value | Usage |
|---|---|---|
| shadow-sm | `0 1px 2px 0 #0000000d`                           | subtle card |
| shadow-md | `0 4px 6px -1px #0000001a, 0 2px 4px -2px #0000001a` | card |
| shadow-lg | `0 10px 15px -3px #0000001a, 0 4px 6px -4px #0000001a` | popover |
| `--twoslash-popup-shadow` | `rgba(0,0,0,0.08) 0px 1px 4px` | TS hover popup |
| prose-kbd-shadow | `0 0 0 1px #1018281a, 0 3px 0 #1018281a` | keyboard key |

> **시그너처**: Twoslash TypeScript hover popup 그림자는 Mintlify의 문서 플랫폼 차별점. 일반 Tailwind docs와 다르게 느껴지는 핵심 디테일.

---

## 11. Layout Patterns

### Docs Layout
- Left sidebar: 280px, `#F1EFED` 또는 `#FFFFFF` + border `#E5E7EB`
- Main content: max-width 768px, 중앙 정렬
- Right TOC: 240px, `sticky top`

### Hero (marketing)
- Background: `#FFFFFF` + teal 그라디언트
- H1: 40px / weight 700 / tracking -0.02em
- Customer logo wall: 그레이스케일 filter 적용 권장

```css
.docs-layout { display: grid; grid-template-columns: 280px 1fr 240px; max-width: 1440px; margin-inline: auto; }
.docs-content { max-width: 768px; padding: 48px 32px; }
.logo-wall { filter: grayscale(1) opacity(0.5); }
```

---

## 12. Components

### 12.1 Primary CTA (Teal)

```html
<a class="btn-primary">Start for free</a>
```

| Spec | Value |
|---|---|
| Background | `#0C8C5E` |
| Hover | `#20808D` |
| Text | `#ffffff` |
| Padding | `10px 20px` |
| Radius | `8px` |
| Font weight | 500 |

### 12.2 Code Block (with language tabs)

```html
<div class="code-block">
  <div class="code-block__tabs">
    <button class="tab active">TypeScript</button>
    <button class="tab">Python</button>
  </div>
  <pre><code class="language-ts">// hover 시 --twoslash-popup 표시</code></pre>
</div>
```

| Spec | Value |
|---|---|
| Background | `#1E2939` (prose-pre-bg) |
| Text | `#F3F4F6` |
| Padding | `20px 24px` |
| Radius | `10px` |
| Font | `var(--font-geist-mono)` |

### 12.3 Twoslash Popup (TS hover)

```html
<span class="twoslash">type Result = {...}</span>
```

| Spec | Value |
|---|---|
| Background | `#F3F7F6` |
| Border | `1px solid #DBDFDE` |
| Shadow | `rgba(0,0,0,0.08) 0px 1px 4px` |
| Font size | `0.8rem` |

### 12.4 Doc Card

```html
<a class="doc-card">
  <div class="doc-card__icon"></div>
  <h3>Quickstart</h3>
  <p>Start documenting in minutes.</p>
</a>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Border | `1px solid #E5E7EB` |
| Radius | `10px` |
| Padding | `24px` |
| Hover border | `#0C8C5E` |

---

## 14. Drop-in CSS

```css
/* Mintlify — copy into your root stylesheet */
:root {
  /* Fonts (next/font 변수 방식) */
  --font-inter:      "Inter", "Inter Fallback", -apple-system, BlinkMacSystemFont, sans-serif;
  --font-geist-mono: "Geist Mono", "Geist Mono Fallback", ui-monospace, monospace;

  /* Semantic — Mintlify layer */
  --color-background-main:        #FFFFFF;
  --color-background-soft:        #F1EFED;
  --color-background-gray-subtle: #F9FAFB;
  --color-background-gray-emphasis:#F3F4F6;
  --color-text-main:              #231F20;
  --color-text-soft:              #4A5565;
  --color-text-sub:               #6B7280;
  --color-text-base-tertiary:     #9CA3AF;
  --color-border-sub:             #E5E7EB;
  --color-border-solid:           #D1D5DC;
  --color-border-soft:            #EEF0F2;

  /* Brand */
  --color-brand:       #0C8C5E;
  --color-brand-light: #20808D;

  /* Semantic invert (다크 모드 — 변수 flip) */
  --color-background-invert: var(--color-text-main);
  --color-text-invert:       var(--color-background-main);

  /* Prose */
  --tw-prose-pre-bg:          #1E2939;
  --tw-prose-quote-borders:   #E5E7EB;
  --tw-prose-th-borders:      #D1D5DC;
  --tw-prose-td-borders:      #E5E7EB;

  /* Twoslash */
  --twoslash-popup-bg:      #F3F7F6;
  --twoslash-border-color:  #DBDFDE;
  --twoslash-popup-shadow:  rgba(0,0,0,0.08) 0px 1px 4px;
  --twoslash-code-font:     var(--font-geist-mono);

  /* Spacing */
  --spacing: 0.25rem;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 10px;
  --radius-xl: 16px;

  /* Shadow */
  --shadow-sm: 0 1px 2px 0 #0000000d;
  --shadow-md: 0 4px 6px -1px #0000001a, 0 2px 4px -2px #0000001a;
  --shadow-lg: 0 10px 15px -3px #0000001a, 0 4px 6px -4px #0000001a;
}

body {
  background: var(--color-background-main);
  color: var(--color-text-main);
  font-family: var(--font-inter);
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
}

code, pre { font-family: var(--font-geist-mono); }

@media (prefers-color-scheme: dark) {
  :root {
    --color-background-main: #101828;
    --color-text-main:       #F9FAFB;
  }
}
```

---

## 15. Tailwind Config

```js
// tailwind.config.js — Mintlify (Tailwind v4 + @tailwindcss/typography)
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        bg: {
          main: 'var(--color-background-main)',
          soft: '#F1EFED',
          'gray-subtle': '#F9FAFB',
        },
        text: {
          main: '#231F20',
          soft: '#4A5565',
          sub:  '#6B7280',
        },
        brand: {
          DEFAULT: '#0C8C5E',
          light:   '#20808D',
        },
        border: {
          sub:   '#E5E7EB',
          solid: '#D1D5DC',
          soft:  '#EEF0F2',
        },
      },
      fontFamily: {
        sans: ['var(--font-inter)', 'Inter', 'Inter Fallback', '-apple-system', 'sans-serif'],
        mono: ['var(--font-geist-mono)', 'Geist Mono', 'Geist Mono Fallback', 'monospace'],
      },
      borderRadius: {
        sm: '4px', md: '8px', lg: '10px', xl: '12px', '2xl': '16px',
      },
      boxShadow: {
        sm: '0 1px 2px 0 #0000000d',
        md: '0 4px 6px -1px #0000001a, 0 2px 4px -2px #0000001a',
        lg: '0 10px 15px -3px #0000001a, 0 4px 6px -4px #0000001a',
        'twoslash': 'rgba(0,0,0,0.08) 0px 1px 4px',
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
```

---

## 16. DO / DON'T

### ✅ DO
- 브랜드 teal은 **`#0C8C5E`** (primary), **`#20808D`** (secondary). 밝은 lime `#18E299`는 accent.
- Primary text는 **warm black `#231F20`** — pure black 아님.
- Surface는 **warm off-white `#F1EFED`** — cool gray 아님.
- 폰트는 **`Inter` (body) + `Geist Mono` (code)**. `next/font` 변수 방식 (`var(--font-inter)`).
- **Metric fallback** (`Inter Fallback`, `Geist Mono Fallback`) 포함 필수.
- 다크 모드는 **invert 변수 패턴**으로. `--color-background-invert: var(--color-text-main)` 참조.
- Prose 토큰 (`--tw-prose-pre-bg`, `--tw-prose-quote-borders`) 사용해 문서 본문 스타일링.
- **Twoslash popup** (`--twoslash-popup-bg`)을 TS 코드 블록 hover에 사용 — Mintlify 시그너처.

### ❌ DON'T
- ❌ **Fira Code** 쓰지 말 것 → **Geist Mono**.
- ❌ **`#0D9373`** 쓰지 말 것 → 실제는 **`#0C8C5E`** (CSS에 직접 등장).
- ❌ **pure black `#000`** text 쓰지 말 것 → warm `#231F20`.
- ❌ **cool gray surface** (`#F5F6F8`) 쓰지 말 것 → warm `#F1EFED`.
- ❌ Customer logo wall의 hex (`#003087 PayPal`, `#FF5A00 Braintrust`, `#4B73FF Coinbase`)를 Mintlify 브랜드로 착각하지 말 것.
- ❌ 다크 모드를 **두 세트 hex 나열**로 구현하지 말 것 → invert 변수 flip 패턴.
- ❌ **일반 Tailwind docs 템플릿** 느낌 금지 → Twoslash / Prose 문서 특화 토큰 포함.
- ❌ 본문 폰트를 **px 절대값**으로 고정 금지 → Prose em/% 사용.
