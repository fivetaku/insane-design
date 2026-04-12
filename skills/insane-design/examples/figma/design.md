---
slug: figma
service_name: Figma
site_url: https://www.figma.com
fetched_at: 2026-04-11
default_theme: mixed
brand_color: "#000000"
primary_font: figmaSans
font_weight_normal: 400
token_prefix: f
---

# DESIGN.md — Figma (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Figma처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — figmaSans + figmaMono (Figma 전용 커스텀 폰트) */
:root {
  --f-font-sans: "figmaSans", "figmaSans Fallback", "SF Pro Display", system-ui, helvetica, sans-serif;
  --f-font-mono: "figmaMono", "figmaMono Fallback", "SF Mono", menlo, monospace;
}
body { font-family: var(--f-font-sans); font-weight: 400; }

/* 2. 흑백 극단 — duo-theme (섹션별 bg 반전) */
.section-dark  { background: #000000; color: #FFFFFF; }
.section-light { background: #FFFFFF; color: #000000; }

/* 3. 1px inset border button (Figma 시그니처) */
.btn-outlined {
  background: transparent;
  box-shadow: inset 0 0 0 1px currentColor;
  border: 0;
}
```

**절대 하지 말아야 할 것 하나**: Figma 로고의 **5색** (`#0ACF83` green, `#A259FF` purple, `#F24E1E` red, `#FF7262` peach, `#1ABCFE` blue)은 **로고 전용**이다. UI와 마케팅 사이트는 **흑백 극단 모노크롬**으로 의도적 설계. 로고 5색을 primary palette로 쓰면 colorful playful SaaS가 되고 Figma 브랜드 정체성이 완전히 사라진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.figma.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| CSS files | 3개 번들 · 209,702자 |
| Custom properties | 46개 (color 23 · spacing 4 · shadow 0) |
| Unique hex | 28개 (매우 제한적) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: figma.com marketing site
- **Design system**: 커스텀 — `--f-*` prefix component-slot naming
- **CSS architecture**: semantic-first (core ramp 부재)
  ```
  f-slot tier      --f-bg-color / --f-text-color / --f-primary-btn-bg-color
  f-component tier --f-lego-block-padding / --f-lego-fg-color (재사용 section block)
  f-form tier      --f-form-input-bg-color / --f-form-error-bg-color
  f-badge tier     --f-badge-text-color / --f-badge-bg-color
  ```
- **Class naming**: Figma 내부 BEM
- **Default theme**: **mixed** — 같은 페이지 내 섹션마다 black-on-white / white-on-black 반전
- **Font loading**: Figma 전용 `figmaSans`, `figmaMono`, `ABCWhytePlusVariable`
- **Canonical anchor**: 단일 brand color 없음 — 모노크롬 `#000000` / `#FFFFFF`

> **중요**: Figma의 **공식 brand guide의 5색 로고 컬러** (green/purple/red/peach/blue)는 실제 사이트 CSS에 **0회**. 로고는 로고 한곳에만 SVG로 들어가고, 나머지 UI는 모두 흑백. 이것이 Figma의 디자인 철학: "도구는 invisible, 콘텐츠가 돋보이게".

---

## 04. Font Stack
<!-- SOURCE: auto -->

- **Sans primary**: `figmaSans` (Figma 전용 커스텀 폰트)
- **Mono**: `figmaMono` (Figma 전용 monospace)
- **Fallback/alt**: `ABCWhytePlusVariable` (Dinamo's ABC Whyte — 2회)
- **System fallback**: `SF Pro Display`, `system-ui`, `helvetica`

```css
:root {
  --f-font-sans: "figmaSans", "figmaSans Fallback", "SF Pro Display", system-ui, helvetica, sans-serif;
  --f-font-mono: "figmaMono", "figmaMono Fallback", "SF Mono", menlo, monospace;
}
body { font-family: var(--f-font-sans); font-weight: 400; }
code, .code { font-family: var(--f-font-mono); }
```

> **Variable font weight 특이**: `320`, `330`, `340`, `400`, `450`, `480`, `520`, `530`, `540`, `550` — continuous axis 사용. 표준 `400/500/700`이 아닌 미세 조정값. 특히 `540`/`550`이 최다 빈도 (body 대체).

---

## 05. Typography Scale
<!-- SOURCE: auto (rem frequency) -->

| Size | rem | px | Count | Usage |
|---|---|---|---|---|
| body large | 1.125rem | 18 | 70 | body 기본 (최다) |
| lead | 1.25rem | 20 | 46 | lead text |
| body | 1rem | 16 | 30 | secondary body |
| h4 | 1.375rem | 22 | 22 | card title |
| h3 | 1.5rem | 24 | 17 | sub-heading |
| h3 alt | 1.625rem | 26 | 13 | alternate |
| display sm | 2.25rem | 36 | 5 | section title |
| display md | 2.75rem | 44 | 7 | feature title |
| display lg | 3.5rem | 56 | 4 | large display |
| display xl | 4rem | 64 | 7 | hero display |
| display xxl | 4.5rem | 72 | 2 | mega display |
| display mega | 5.375rem | 86 | 2 | ultra display |
| small | 0.75rem | 12 | 1 | caption |

> **특이점**: 16px (1rem)보다 **18px (1.125rem)이 본문 기본**. body가 한 단계 크다. Weight 축은 variable font로 `540`/`550`이 bold 역할 (표준 `700` 대신).

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Monochrome (실제 브랜드)
<!-- SOURCE: auto -->

| Token | Hex | Count | Role |
|---|---|---|---|
| `--f-bg-color` / black | `#000000` | 542 | ⭐ **primary** — dark section bg, button bg, text |
| `--bg-color` / white | `#FFFFFF` | 342 | ⭐ light section bg, text on dark |
| `#000000A5` (65% alpha) | - | 4 | text secondary |
| `rgba(255,255,255,0.6)` | - | 4 | list header on dark |
| `rgba(255,255,255,0.24)` | - | 4 | icon bg on dark |

### 06-3. Accent Colors (제한적 사용)

| Hex | Count | Role |
|---|---|---|
| `#972121` | 50 | **form error bg** — brownish red |
| `#4D49FC` | 10 | indigo accent |
| `#00B6FF` | 9 | bright blue accent |
| `#24CB71` | 9 | success green |
| `#FF7237` | 5 | orange accent |

### 06-4. Pastel Block Palette
<!-- SOURCE: auto -->
<!-- 마케팅 섹션 배경 블록용 — 실제 Figma.com에서 쓰이는 진짜 시각 요소 -->

| Hex | Count | Role |
|---|---|---|
| `#C7F8FB` | 7 | pale mint block bg |
| `#FFC9C1` | 7 | pastel peach block bg |
| `#CB9FD2` | 7 | pastel lavender block bg |
| `#E4FF97` | 5 | pastel yellow-green block bg |
| `#FADCA2` | 4 | pastel cream block bg |
| `#33DFDF` | 4 | mint cyan block accent |

### 06-5. Logo Colors (⚠️ 로고 전용 — UI에 사용 금지)
<!-- Figma 공식 브랜드 가이드의 5색. 실제 CSS에는 0회. -->

| Hex | Role |
|---|---|
| `#0ACF83` | logo green |
| `#A259FF` | logo purple |
| `#F24E1E` | logo red |
| `#FF7262` | logo peach |
| `#1ABCFE` | logo blue |

> **주의**: 이 5색은 **Figma 로고의 SVG 내부에만** 존재하며 CSS 변수나 UI 컴포넌트에는 단 한 번도 등장하지 않음. 브랜드 가이드를 UI 팔레트로 확대 해석하면 Figma 정체성과 완전히 달라진다.

### 06-6. Semantic Alias Layer

| Slot | Resolves to | Usage |
|---|---|---|
| `--f-bg-color` | `#000000` | dark section bg |
| `--f-text-color` | `#FFFFFF` | text on dark |
| `--f-text-secondary-color` | `rgba(0,0,0,0.65)` | secondary text on light |
| `--f-list-header-color` | `rgba(255,255,255,0.6)` | list header on dark |
| `--f-icon-bg-color` | `rgba(255,255,255,0.24)` | icon chip on dark |
| `--f-badge-text-color` | — | badge text |
| `--f-badge-bg-color` | — | badge bg |
| `--f-primary-btn-bg-color` | `#000000` | primary button |
| `--f-primary-btn-text-color` | `#FFFFFF` | primary button text |
| `--f-emphasis-btn-bg-color` | — | emphasis button |
| `--f-form-input-bg-color` | — | input bg |
| `--f-form-placeholder-text-color` | `rgba(0,0,0,0.5)` | placeholder |
| `--f-form-error-bg-color` | `#972121` | form error bg |
| `--f-link-color` | — | link |
| `--f-lego-fg-color` | - | lego block fg |
| `--f-lego-bg-color` | - | lego block bg |
| `--f-lego-block-padding` | `5rem` | lego block padding |

> "**Lego**" 개념: Figma.com이 재사용 가능한 section component를 "lego block"으로 부르는 컨벤션. `--f-lego-*` slot이 존재.

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#000000` | 542 | page/button bg (dark) |
| 2 | `#FFFFFF` | 342 | page/text bg (light) |
| 3 | `#972121` | 50 | form error bg |
| 4 | `#4D49FC` | 10 | indigo accent |
| 5 | `#00B6FF` | 9 | bright blue accent |
| 6 | `#24CB71` | 9 | success green |
| 7 | `#CB9FD2` | 7 | pastel lavender |
| 8 | `#C7F8FB` | 7 | pastel mint |
| 9 | `#FFC9C1` | 7 | pastel peach |
| 10 | `#FF7237` | 5 | orange accent |

---

## 07. Spacing
<!-- SOURCE: auto -->
<!-- 4개 토큰만 존재. Lego block 특화. -->

| Token | Value | Use case |
|---|---|---|
| `--f-lego-block-padding` | `5rem` | lego block inner padding (80px) |
| `--slide-spacing` | - | carousel slide gap |
| `--slide-size` | - | carousel slide width |
| `--slide-gap` | - | carousel gap |

일반 spacing은 Tailwind 유틸로 추정:
| Step | Estimated px |
|---|---|
| xs | 8 |
| sm | 16 |
| md | 24 |
| lg | 40 |
| xl | 80 (lego-block-padding) |

---

## 08. Radius
<!-- SOURCE: auto -->

**단 2개 값**만 사용:

| Value | Count | Context |
|---|---|---|
| `8px` | 10 | card / button corner |
| `2px` | 8 | chip / badge / form input |

> Figma는 **매우 제한적인 radius 시스템**. 8px 이상을 거의 쓰지 않음. 이는 Figma의 "editor chrome minimal" 철학 — 인터페이스가 장식을 줄이고 콘텐츠에 집중하도록.

---

## 09. Shadows
<!-- SOURCE: auto -->
<!-- 0 shadow custom props. 대신 1px inset border 시그니처. -->

Figma는 **box-shadow 변수를 사용하지 않음**. 대신 특이한 시그니처:

| Pattern | Value | Usage |
|---|---|---|
| **1px inset border** | `inset 0 0 0 1px var(--f-text-color, #000)` | outlined button/card (6회) |
| border instead | `1px solid` | 일반 border |

> **패턴**: Figma는 elevation을 **drop shadow 대신 1px inset border**로 표현. `inset 0 0 0 1px #000` 형태로 button/card의 경계를 그림. 이 outlined 스타일이 Figma의 button 시그니처.

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary button (filled)
- **Background**: `var(--f-primary-btn-bg-color)` = `#000000` (dark section) / `#FFFFFF` (light section)
- **Text**: `var(--f-primary-btn-text-color)` (반전)
- **Radius**: `8px`
- **Font**: figmaSans 16px / 540
- **Padding**: `12px 24px`

### Outlined button (Figma signature)
- **Background**: transparent
- **Box-shadow**: `inset 0 0 0 1px var(--f-text-color)` (1px inset border — 시그니처!)
- **Text**: `currentColor` (context-adaptive)
- **Radius**: `8px`
- **No drop shadow**

```html
<button class="btn btn--outlined">Get Figma free</button>
```

### Form input
- **Background**: `var(--f-form-input-bg-color)` (context-adaptive)
- **Border**: `1px solid`
- **Radius**: `2px` (small)
- **Placeholder**: `rgba(0,0,0,0.5)`
- **Error bg**: `#972121` (brownish red)

### Lego block (재사용 section)
- **Background**: `var(--f-lego-bg-color)` — pastel block one of (peach/lavender/mint/yellow/cream)
- **Foreground**: `var(--f-lego-fg-color)` (context-adaptive)
- **Padding**: `var(--f-lego-block-padding)` = `5rem` (80px)
- **Max-width**: 일반적 container
- **Font**: figmaSans 18-24px

### Badge
- **Background**: `var(--f-badge-bg-color)`
- **Text**: `var(--f-badge-text-color)`
- **Radius**: `2px`
- **Font**: figmaSans 12px / 540

### Duo-theme section pattern
```html
<section style="background: #000; color: #fff"> <!-- dark -->
  <h2>Design, better together</h2>
  <button class="btn-outlined">Learn more</button>
</section>
<section style="background: #fff; color: #000"> <!-- light -->
  <h2>Build faster</h2>
</section>
```

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Figma — copy into your root stylesheet */
:root {
  /* Fonts (Figma 전용 커스텀) */
  --f-font-sans: "figmaSans", "figmaSans Fallback", "SF Pro Display", system-ui, helvetica, sans-serif;
  --f-font-mono: "figmaMono", "figmaMono Fallback", "SF Mono", menlo, monospace;

  /* Monochrome (duo-theme) */
  --f-bg-color:           #000000; /* dark section bg */
  --f-text-color:         #FFFFFF;
  --bg-color:             #FFFFFF; /* light section bg */
  --text-color:           #000000;
  --f-text-secondary-color: rgba(0, 0, 0, 0.65);
  --f-list-header-color:    rgba(255, 255, 255, 0.6);

  /* Lego block (재사용 section component) */
  --f-lego-block-padding: 5rem;

  /* Primary button */
  --f-primary-btn-bg-color:   #000000;
  --f-primary-btn-text-color: #FFFFFF;

  /* Form */
  --f-form-input-bg-color:        transparent;
  --f-form-placeholder-text-color:rgba(0, 0, 0, 0.5);
  --f-form-error-bg-color:        #972121;

  /* Pastel block palette */
  --f-pastel-peach:    #FFC9C1;
  --f-pastel-lavender: #CB9FD2;
  --f-pastel-mint:     #C7F8FB;
  --f-pastel-yellow:   #E4FF97;
  --f-pastel-cream:    #FADCA2;
  --f-pastel-cyan:     #33DFDF;

  /* Accent (제한적) */
  --f-accent-indigo: #4D49FC;
  --f-accent-blue:   #00B6FF;
  --f-accent-green:  #24CB71;
  --f-accent-orange: #FF7237;

  /* Radius */
  --f-radius-sm: 2px;
  --f-radius-md: 8px;
}

body {
  font-family: var(--f-font-sans);
  font-weight: 400;
  background: var(--bg-color);
  color: var(--text-color);
  font-size: 1.125rem; /* 18px base, 16px 아님 */
}

/* Signature outlined button */
.btn-outlined {
  background: transparent;
  color: currentColor;
  box-shadow: inset 0 0 0 1px currentColor;
  border: 0;
  border-radius: var(--f-radius-md);
  padding: 12px 24px;
  font: 540 16px / 1 var(--f-font-sans);
  cursor: pointer;
}

/* Duo-theme section */
.section-dark  { background: var(--f-bg-color); color: var(--f-text-color); }
.section-light { background: var(--bg-color); color: var(--text-color); }
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Figma
module.exports = {
  theme: {
    extend: {
      colors: {
        // Monochrome 만 브랜드
        f: {
          bg: '#000000',
          fg: '#FFFFFF',
        },
        pastel: {
          peach:    '#FFC9C1',
          lavender: '#CB9FD2',
          mint:     '#C7F8FB',
          yellow:   '#E4FF97',
          cream:    '#FADCA2',
          cyan:     '#33DFDF',
        },
        accent: {
          indigo: '#4D49FC',
          blue:   '#00B6FF',
          green:  '#24CB71',
          orange: '#FF7237',
        },
        error: '#972121',
        // Logo colors는 logo 컴포넌트 내부에만 사용
        logo: {
          green:  '#0ACF83',
          purple: '#A259FF',
          red:    '#F24E1E',
          peach:  '#FF7262',
          blue:   '#1ABCFE',
        },
      },
      fontFamily: {
        sans: ['"figmaSans"', '"figmaSans Fallback"', '"SF Pro Display"', 'system-ui', 'helvetica', 'sans-serif'],
        mono: ['"figmaMono"', '"figmaMono Fallback"', '"SF Mono"', 'menlo', 'monospace'],
      },
      fontWeight: {
        // Variable font continuous axis
        '320': '320',
        '330': '330',
        '340': '340',
        'normal': '400',
        '450': '450',
        '480': '480',
        '520': '520',
        '530': '530',
        '540': '540',
        '550': '550',
      },
      borderRadius: {
        sm: '2px',
        md: '8px',
      },
      spacing: {
        'lego': '5rem', // --f-lego-block-padding
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- **Monochrome 흑백 극단**: `#000000` / `#FFFFFF` primary. 섹션마다 bg 반전 (duo-theme).
- **figmaSans + figmaMono** Figma 전용 커스텀 폰트 사용. 폴백은 `SF Pro Display`, `SF Mono`.
- **Variable font weight** `540`/`550`을 bold 역할로 사용 (표준 700 아님).
- Body base font-size **18px** (1.125rem, 최다 빈도) — 16px 아님.
- **1px inset border button**: `box-shadow: inset 0 0 0 1px currentColor` — Figma의 outlined button 시그니처.
- Pastel block palette (`#C7F8FB`, `#FFC9C1`, `#CB9FD2`, `#E4FF97`, `#FADCA2`)을 lego block section bg로.
- Radius 2-step만: `2px` (form/chip) + `8px` (card/button). 이 이상 쓰지 말 것.
- `--f-*` prefix slot 네이밍: `--f-bg-color`, `--f-text-color`, `--f-primary-btn-bg-color`.
- **Lego block** 개념: 재사용 section component를 `--f-lego-block-padding: 5rem`으로 정의.

### ❌ DON'T
- ❌ **로고 5색을 UI에 사용** (`#0ACF83`, `#A259FF`, `#F24E1E`, `#FF7262`, `#1ABCFE`) — 이건 로고 SVG 내부 전용. UI CSS에 0회.
- ❌ `Inter` 단독 사용 — Figma는 `figmaSans` 전용 커스텀 폰트.
- ❌ `color-brand` flat 네이밍 — Figma는 `--f-*` component-slot 체계.
- ❌ 8px 초과 radius — Figma는 2px / 8px 2종만 사용.
- ❌ Drop shadow 기반 elevation — Figma는 `inset 1px border`로만 경계 표현.
- ❌ 단일 theme — Figma는 한 페이지 안에서 dark/light 섹션 반전.
- ❌ 표준 `font-weight: 700` — Figma는 variable font `540`/`550`.
- ❌ 16px base body — Figma는 **18px** base 사용.
