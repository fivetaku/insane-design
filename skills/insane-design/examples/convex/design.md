---
slug: convex
service_name: Convex
site_url: https://www.convex.dev
fetched_at: 2026-04-11
default_theme: light
brand_color: "#BC7914"
primary_font: GT America
font_weight_normal: 400
token_prefix: color
---

# DESIGN.md — Convex (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Convex처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — GT America sans + Publico serif + VCR pixel */
:root {
  --font-sans:   "GT America", ui-sans-serif, system-ui, -apple-system, sans-serif;
  --font-serif:  "Publico", Georgia, "Times New Roman", serif;
  --font-pixel:  "VCR", "VT323", monospace;
  --font-mono:   ui-monospace, Menlo, Monaco, Consolas, monospace;
}
body { font-family: var(--font-sans); font-weight: 400; }

/* 2. 크림/아이보리 배경 + 코코아 텍스트 */
:root {
  --bg-milk:   #FFFDF4;  /* primary page bg */
  --bg-lavender: #F7F1FF;
  --text-cocoa: #221F1D;
  --text-muted: #BAB6C0;
}
body { background: var(--bg-milk); color: var(--text-cocoa); }

/* 3. Monokai syntax accents (코드 블록 + 브랜드) */
:root {
  --mk-pink:   #FC618D;
  --mk-purple: #948AE3;
  --mk-green:  #7BD88F;
  --mk-cyan:   #5AD4E6;
  --mk-yellow: #FCE566;
  --brand-tikka: #BC7914;  /* tikka masala — 메인 브랜드 액센트 */
}
```

**절대 하지 말아야 할 것 하나**: Convex는 "amber on dark" 대시보드가 **아니다**. 실제는 **크림/아이보리 warm backgrounds** 위에 **Monokai syntax palette**가 얹힌 **art/magazine 감성**. 배경을 검은색으로 만드는 순간 브랜드 인상이 정반대로 뒤집힌다. 그리고 폰트 조합이 핵심: `GT America` (sans) + `Publico` (serif) + `VCR` (pixel/retro display).

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.convex.dev` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| CSS files | 4개 번들 · 162,621자 |
| Custom properties | 255개 (color 71 · shadow 18 · spacing 6) |
| Unique hex | 195개 |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js marketing site
- **Design system**: 커스텀 — **Crayola crayon 네이밍 컨벤션** 사용 (tikkaMasala, oldLace, majorelleBlue 등)
- **CSS architecture**: descriptive naming + W3C neutral ramp
  ```
  descriptive tier  (--color-tikkaMasala, --color-milk, --color-cocoaDarkBrown)
  neutral tier      (--color-neutral-n1 ... --color-neutral-n10)  10-step ramp
  theme tier        (--color-ebony, --color-rifleGreen, --color-goldFusion)
  syntax tier       (Monokai palette — 코드 블록 + 강조)
  ```
- **Class naming**: Tailwind-ish + 커스텀 유틸
- **Default theme**: **light** (warm cream), dark는 opt-in
- **Font loading**: `GT America` (sans), `Publico` (serif), `VCR` (retro pixel display), `ui-monospace` (code)
- **Canonical anchor**: `--color-tikkaMasala: #BC7914` — warm accent brand

---

## 04. Font Stack
<!-- SOURCE: auto -->

- **Sans primary**: `GT America` (Grilli Type, 유료 — 스위스 geometric)
- **Serif display**: `Publico` (Commercial Type, 유료 — 에디토리얼 감성)
- **Pixel/retro**: `VCR` (VHS-inspired pixel display font)
- **Mono**: `ui-monospace` (system stack)

```css
:root {
  --font-sans:    "GT America", ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
  --font-primary: var(--font-sans);
  --font-serif:   "Publico", Georgia, "Times New Roman", serif;
  --font-pixel:   "VCR", "VT323", monospace;
  --font-mono:    ui-monospace, Menlo, Monaco, "Cascadia Mono", "Segoe UI Mono", "Roboto Mono", Consolas, "Courier New", monospace;
}
body       { font-family: var(--font-sans); font-weight: 400; }
h1, h2, h3 { font-family: var(--font-sans); font-weight: bold; }
blockquote, .editorial { font-family: var(--font-serif); font-weight: 400; }
.terminal, .retro-label { font-family: var(--font-pixel); }
code, pre  { font-family: var(--font-mono); }
```

> Weights used: `300 / 400 / 500 / 600 / 700 / bold (16회) / 800 / 900`. `bold` 키워드가 가장 빈번 (16회) — 명시적 숫자보다 키워드 선호하는 스타일.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Size | em/rem | Usage |
|---|---|---|
| 5.5rem | 88px | mega display (hero) |
| 4.5rem | 72px | display xl |
| 4rem | 64px | display lg |
| 2.25rem | 36px | h1 |
| 1.5rem | 24px | h2 |
| 1.25em | 20px | h3 / lead |
| 1rem | 16px | body |
| 0.9375rem | 15px | body dense |
| 0.875em | 14px | small text (최다) |
| 0.8125rem | 13px | meta |
| 0.6875rem | 11px | tiny |
| 17px | 17 | custom body |
| 15px | 15 | custom dense |
| 13px | 13 | custom meta |
| 11px | 11 | custom tiny |
| 10px | 10 | caption |

> ⚠️ 스케일이 **em 기반** (`.875em` 가장 빈번 6회) — 부모 요소에 반응하는 relative scale. 대부분의 size가 1회만 등장하는 것은 일관성보다 **per-layout custom sizing**을 선호하는 editorial/magazine 스타일.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand (warm earth-tone)
<!-- Convex의 핵심 컨벤션: Crayola crayon names -->

| Token | Hex | Usage |
|---|---|---|
| `--color-tikkaMasala` | `#BC7914` ⭐ | 메인 warm accent (brand) |
| `--color-goldFusion` | `#BF9000` (추정) | secondary warm |
| `--color-cocoaDarkBrown` | `#2E1F1F` | dark text deep |
| `--color-ebony` | `#221F1D` | dark surface |
| `--color-rifleGreen` | `#44462A` | muted dark |
| `--color-mistyMoss` | `#BABA8D` | muted light |

### 06-2. Monokai Syntax Palette
<!-- 실제 빈도 1~5위 — Convex의 진짜 브랜드 컬러 -->

| Token | Hex | Count | Role |
|---|---|---|---|
| Monokai pink | `#FC618D` | 65 | syntax keyword · hot accent |
| Monokai purple | `#948AE3` | 65 | syntax type · cool accent |
| Monokai green | `#7BD88F` | 64 | syntax string · success |
| Monokai cyan | `#5AD4E6` | 43 | syntax fn · info |
| Monokai yellow | `#FCE566` | 21 | syntax number · warning |

> **중요**: 이 5색은 Convex의 **실질 브랜드 컬러**. 코드 샘플이 브랜드 자산이므로 syntax color = brand color. 랜딩에서도 이 5색이 아이콘/카테고리 구분/illustration에 그대로 사용됨.

### 06-3. Neutral Ramp (10-step W3C core tier)

| Token | Hex |
|---|---|
| `--color-neutral-n1` | `#F6F6F6` |
| `--color-neutral-n2` | `#F1F1F1` |
| `--color-neutral-n3` | `#E5E5E5` |
| `--color-neutral-n4` | `#D7D7D7` (→ `#D6D6D6` 빈도 21) |
| `--color-neutral-n5` | `#C2C2C2` |
| `--color-neutral-n6` | `#A9A9AC` |
| `--color-neutral-n7` | `#8B8B8E` |
| `--color-neutral-n8` | `#6D6D70` |
| `--color-neutral-n9` | `#4F4F52` |
| `--color-neutral-n10` | `#38383A` |

### 06-4. Cream / Warm Background Palette
<!-- 라이트 테마의 핵심 — 순수 흰색 대신 warm off-white를 사용 -->

| Token | Hex | Usage |
|---|---|---|
| `--color-milk` | `#FFFDF4` | primary page bg |
| `--color-halfWhite` | `#FFFFF9` | subtle warm bg |
| `--color-oldLace` | `#FAF4E9` | sunken warm |
| `--color-alabaster` | `#F6F3E5` | section bg warm |
| `--color-antiqueWhite` | `#FAEBD7` (추정) | card bg warm |
| `--color-seashell` | `#FFF5EE` (추정) | accent warm |
| `--color-eggshell` | `#F0EAD6` (추정) | muted warm |
| (observed) | `#F7F1FF` | pale lavender (2번째 bg) |
| (observed) | `#F8E67A` | cream yellow |

### 06-5. Color Families (semantic crayon)
<!-- SOURCE: auto -->

- **Blue ramp**: `mayaBlue`, `aero`, `jordyBlue`, `ultramarineBlue`, `majorelleBlue`, `grape`, `orchid`
- **Pink/Red ramp**: `lightSalmonPink` `#F7A4A1`, `congoPink`, `mediumVermillion`, `tikkaMasala` `#BC7914`
- **Cream ramp**: `oldLace`, `antiqueWhite`, `eggshell`, `seashell`, `milk`, `alabaster`, `halfWhite`
- **Green ramp**: `mistyMoss`, `rifleGreen` `#44462A`

> 이 descriptive naming 컨벤션 자체가 Convex의 브랜드 아이덴티티의 일부. 토큰을 수치로 rename하면 브랜드 문화 훼손.

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FC618D` | 65 | Monokai pink |
| 2 | `#948AE3` | 65 | Monokai purple |
| 3 | `#BAB6C0` | 64 | mid gray |
| 4 | `#7BD88F` | 64 | Monokai green |
| 5 | `#5AD4E6` | 43 | Monokai cyan |
| 6 | `#F7F1FF` | 42 | pale lavender bg |
| 7 | `#F8E67A` | 23 | cream yellow |
| 8 | `#FCE566` | 21 | Monokai yellow |
| 9 | `#D6D6D6` | 21 | neutral-n4 |
| 10 | `#FFFFFF` | 10 | pure white |

---

## 07. Spacing
<!-- SOURCE: auto -->
<!-- Convex는 spacing 토큰 6개만 노출. Tailwind 유틸 위주. -->

| Step | Estimated px | Use case |
|---|---|---|
| xs | 4 | icon gap |
| sm | 8 | button inset |
| md | 16 | card padding |
| lg | 24 | section internal |
| xl | 32 | section gap |
| 2xl | 64 | hero padding |

---

## 08. Radius
<!-- SOURCE: auto -->

Convex는 7개 radius 값 사용. 주요 패턴:

| Value | Context |
|---|---|
| `0` | flat / editorial 요소 |
| `2px` | hairline |
| `4px` | input |
| `6px` | chip |
| `8px` | card corner |
| `12px` | large card |
| `9999px` | pill |

---

## 09. Shadows
<!-- SOURCE: auto -->

Convex는 **18개** shadow 변수 (풍부한 shadow 시스템). 주요 패턴:
- **single-layer**: `0 2px 4px rgba(0,0,0,0.08)` 기본
- **warm-tinted**: `0 4px 12px rgba(46, 31, 31, 0.12)` (cocoa-tinted — brand cohesion)
- **retro inset**: `inset 0 0 0 1px #BC7914` — brand outline

> warm-tinted shadow는 Convex의 signature — 순수 검정이 아닌 **cocoa brown** 기반 shadow로 전체 cream palette와 시각적으로 조화.

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary CTA (warm button)
- **Background**: `#BC7914` (tikka masala) 또는 `#221F1D` (ebony)
- **Text**: `#FFFDF4` (milk)
- **Radius**: `8px`
- **Font**: GT America 15px / bold
- **Padding**: `12px 24px`

### Code block (signature)
- **Background**: `#221F1D` (ebony) 또는 `#F7F1FF` (pale lavender for light)
- **Font**: `ui-monospace` 14px / 400
- **Syntax**: Monokai 5색 (`#FC618D` keyword, `#948AE3` type, `#7BD88F` string, `#5AD4E6` fn, `#FCE566` number)
- **Border**: `1px solid #D6D6D6`
- **Radius**: `8px`
- **Padding**: `20px 24px`

### Data Browser (Convex flagship)
- Grid layout with warm cream bg
- Monokai syntax for values
- `GT America` labels + `ui-monospace` values
- Row hover: `#F7F1FF` subtle lavender

### Editorial text block
- Font: `Publico` serif
- Size: 20px / 400 / 1.6 line-height
- Color: `#221F1D` (cocoa)
- Drop cap or pull quote pattern

### Retro label / pixel accent
- Font: `VCR` pixel
- Size: 11-13px
- Color: tikka masala `#BC7914` or Monokai yellow `#FCE566`
- Usage: section labels, terminal prompts, easter eggs

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Convex — copy into your root stylesheet */
:root {
  /* Fonts (4 faces) */
  --font-sans:    "GT America", ui-sans-serif, system-ui, -apple-system, sans-serif;
  --font-primary: var(--font-sans);
  --font-serif:   "Publico", Georgia, "Times New Roman", serif;
  --font-pixel:   "VCR", "VT323", monospace;
  --font-mono:    ui-monospace, Menlo, Monaco, "Cascadia Mono", Consolas, monospace;

  /* Warm cream backgrounds (Crayola naming) */
  --color-milk:         #FFFDF4;
  --color-halfWhite:    #FFFFF9;
  --color-oldLace:      #FAF4E9;
  --color-alabaster:    #F6F3E5;
  --color-paleLavender: #F7F1FF;

  /* Dark texts (cocoa) */
  --color-ebony:          #221F1D;
  --color-cocoaDarkBrown: #2E1F1F;

  /* Brand warm */
  --color-tikkaMasala: #BC7914;

  /* Monokai syntax palette */
  --mk-pink:   #FC618D;
  --mk-purple: #948AE3;
  --mk-green:  #7BD88F;
  --mk-cyan:   #5AD4E6;
  --mk-yellow: #FCE566;

  /* Neutral 10-step ramp */
  --color-neutral-n1:  #F6F6F6;
  --color-neutral-n2:  #F1F1F1;
  --color-neutral-n3:  #E5E5E5;
  --color-neutral-n4:  #D6D6D6;
  --color-neutral-n5:  #C2C2C2;
  --color-neutral-n6:  #A9A9AC;
  --color-neutral-n7:  #8B8B8E;
  --color-neutral-n8:  #6D6D70;
  --color-neutral-n9:  #4F4F52;
  --color-neutral-n10: #38383A;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  /* Shadow (warm-tinted) */
  --shadow-warm: 0 4px 12px rgba(46, 31, 31, 0.12);
}

body {
  font-family: var(--font-sans);
  background: var(--color-milk);
  color: var(--color-ebony);
  font-weight: 400;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Convex
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#BC7914', // tikka masala
        },
        cream: {
          milk:      '#FFFDF4',
          half:      '#FFFFF9',
          lace:      '#FAF4E9',
          alabaster: '#F6F3E5',
          lavender:  '#F7F1FF',
        },
        cocoa: {
          ebony: '#221F1D',
          dark:  '#2E1F1F',
        },
        monokai: {
          pink:   '#FC618D',
          purple: '#948AE3',
          green:  '#7BD88F',
          cyan:   '#5AD4E6',
          yellow: '#FCE566',
        },
        neutral: {
          100: '#F6F6F6',
          200: '#F1F1F1',
          300: '#E5E5E5',
          400: '#D6D6D6',
          500: '#C2C2C2',
          600: '#A9A9AC',
          700: '#8B8B8E',
          800: '#6D6D70',
          900: '#4F4F52',
          950: '#38383A',
        },
      },
      fontFamily: {
        sans:  ['"GT America"', 'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
        serif: ['"Publico"', 'Georgia', '"Times New Roman"', 'serif'],
        pixel: ['"VCR"', '"VT323"', 'monospace'],
        mono:  ['ui-monospace', 'Menlo', 'Monaco', '"Cascadia Mono"', 'Consolas', 'monospace'],
      },
      borderRadius: {
        sm: '4px',
        md: '8px',
        lg: '12px',
        full: '9999px',
      },
      boxShadow: {
        warm: '0 4px 12px rgba(46, 31, 31, 0.12)',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- **Warm cream backgrounds**: `#FFFDF4` (milk) 기본, `#F7F1FF` (lavender) 보조, `#F6F3E5` (alabaster) sunken. 순수 흰색 대신.
- **Monokai syntax palette** 5색을 브랜드 액센트로 활용: pink `#FC618D`, purple `#948AE3`, green `#7BD88F`, cyan `#5AD4E6`, yellow `#FCE566`.
- 3-폰트 조합: `GT America` (sans, body) + `Publico` (serif, editorial) + `VCR` (pixel, retro label).
- Dark text는 `#221F1D` (ebony) 또는 `#2E1F1F` (cocoa dark) — warm-tinted dark.
- `tikka masala #BC7914`를 warm brand accent로 사용 (CTA, 강조).
- **Crayola crayon naming**을 토큰에 보존: `--color-tikkaMasala`, `--color-milk`, `--color-oldLace`.
- 10-step neutral ramp (`n1..n10`) 전체 등재.
- Warm-tinted shadow: `rgba(46, 31, 31, 0.12)` — cocoa 기반, 순수 black 아님.
- Editorial/magazine 레이아웃: 큰 typography (5.5rem), pull quotes, drop caps.

### ❌ DON'T
- ❌ **"amber on dark" 대시보드** 스타일 — 실제는 cream light bg + Monokai 강조의 정반대.
- ❌ 순수 흰색 `#FFFFFF` 페이지 bg — 실제는 warm off-white (`#FFFDF4`).
- ❌ `Inter` / `Fira Code` 사용 — 실제는 `GT America` / `Publico` / `VCR`.
- ❌ Monokai palette 누락 — 이게 Convex의 실질 브랜드 컬러.
- ❌ `color-brand` / `color-gray-*` flat 네이밍 — Crayola descriptive 컨벤션 보존해야 브랜드 문화 유지.
- ❌ 순수 black `#000000` shadow — warm cocoa-tinted를 사용.
- ❌ "generic developer dashboard" 레이아웃 — Convex는 art/editorial 감성.
- ❌ dark theme 기본값 — Convex는 라이트 우선, 다크는 opt-in.
