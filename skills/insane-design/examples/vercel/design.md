---
slug: vercel
service_name: Vercel
site_url: https://vercel.com
fetched_at: 2026-04-11
default_theme: light
brand_color: "#000000"
primary_font: Geist
font_weight_normal: 400
token_prefix: "--ds-*, --geist-*"
---

# DESIGN.md — Vercel (Claude Code Edition)

---

## 01. Quick Start

> 5분 안에 Vercel처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트: Geist sans + Geist mono (Vercel 자체 제작) */
:root {
  --font-sans: "Geist", var(--font-sans-fallback), ui-sans-serif, system-ui,
               -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
               "Helvetica Neue", Arial, sans-serif;
  --font-mono: "Geist Mono", var(--font-mono-fallback), ui-monospace,
               SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",
               "Courier New", monospace;
}
body  { font-family: var(--font-sans); font-weight: 400; }
code, pre { font-family: var(--font-mono); }

/* 2. 배경 + 텍스트 — Vercel 의 monochrome 철학 */
:root {
  --ds-background-100: hsl(0, 0%, 100%);    /* #FFFFFF — 페이지 */
  --ds-background-200: hsl(0, 0%, 98%);     /* #FAFAFA — subtle alt */
  --ds-gray-1000:      hsl(0, 0%, 9%);      /* #171717 — ink */
}
body {
  background: var(--ds-background-100);
  color: var(--ds-gray-1000);
}

/* 3. Accent — 공식 브랜드는 흑백. Accent 는 integration 별 */
:root {
  --ds-blue-700:  hsl(212, 100%, 48%);      /* 링크 · Vercel blue */
  --ds-red-700:   hsl(358, 75%, 60%);       /* Next.js → #FF1E56 */
  --ds-success:   #00DC82;                   /* 성공 / deployed */
}
```

**절대 하지 말아야 할 것 하나**: "Vercel 브랜드 색" 을 추측하지 말 것. Vercel 은 **의도적으로 흑백 monochrome** 이다. 공식 브랜드는 <code>#000000</code> / <code>#FFFFFF</code> + 삼각형 로고뿐. Accent 로 보이는 색들 (`#FF1E56` Next.js, `#00DC82` Nuxt, `#FF3E00` Svelte, `#45DEC4` framework 등)은 전부 <b>customer/integration 로고 색</b> — Vercel 자체 브랜드가 아니라 고객사 로고를 hero 캐러셀에 노출할 때 쓰는 것. UI 복제 시 이것들을 "Vercel 브랜드" 로 쓰면 관계가 뒤집힌다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://vercel.com` |
| Fetched | 2026-04-11 |
| CSS files | 12개 외부, 총 861,227자 |
| Token count | **630** custom properties · 89 color · 71 spacing · **33 shadow** |
| Token prefix | `--ds-*` (Design System, 공식) + `--geist-*` (legacy Geist UI) |
| Method | CSS 커스텀 프로퍼티 + OKLCH 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js (self-hosted, dogfood)
- **Design system**: **DS (Design System)** — Vercel 의 내부 DS. 2 세대: `--geist-*`(legacy Geist UI) → `--ds-*`(현 DS).
- **CSS architecture**: 2-layer HSL + OKLCH
  ```
  --ds-{family}-{step}-value       HSL 3-tuple (H, S%, L%) — raw
  --ds-{family}-{step}              hsla(var(--...-value), 1) — 사용 레이어
  --ds-{family}-{step}              oklch(...) — 모던 브라우저용 fallback
  --geist-{token}                   legacy Geist UI (아직 일부 사용)
  ```
- **Class naming**: Tailwind + `.ds-*` 유틸리티. 컴포넌트는 css-in-js (Next.js css modules).
- **Default theme**: **light**. <code>--ds-background-100</code> = white. Dark 테마도 완전 정의돼 있어 media query / class 로 토글.
- **Font loading**: Next.js font loader. `--font-sans` / `--font-mono` 경유 Geist + Geist Mono 로드. KaTeX 수학 폰트도 번들됨.
- **Canonical anchor**: <code>#000000</code> (black) + <code>#FFFFFF</code> (white) — monochrome brand.

---

## 04. Font Stack

- **Primary sans**: `Geist` (Vercel 자체 제작 variable, OFL 오픈 폰트)
- **Primary mono**: `Geist Mono` (오픈소스)
- **Math**: `KaTeX_Main`, `KaTeX_SansSerif`, `KaTeX_Fraktur`, `KaTeX_Math` (docs 전용)
- **Weights used**: 100/200/300/400(87회)/500(135회, <b>1위</b>)/600(108회)/700/800/900

```css
:root {
  --font-sans: var(--font-sans-fallback),
    ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: var(--font-mono-fallback),
    ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
    "Liberation Mono", "Courier New", monospace;
}
/* Next.js font loader 가 실제 로드:
   --font-sans = "Geist" variable
   --font-mono = "Geist Mono" variable
*/
body { font-family: var(--font-sans); font-weight: 400; }
```

> ⚠️ **Weight 500 이 사용 빈도 1위 (135회).** Body 는 400 이지만, UI 라벨/버튼/nav 는 500 이 기본. Medium weight 가 signature. 600 도 108회로 2위.

---

## 05. Typography Scale

| Size | px | Weight | Count | Usage |
|---|---|---|---|---|
| `12px` | 12 | 400/500 | 22 | 캡션 · 작은 label |
| `13px` | 13 | 400/500 | 27 | UI medium |
| `14px` | 14 | 400/500 | **53** (1위) | 본문 기본 |
| `.875rem` | 14 | 400 | 19 | rem 버전 |
| `16px` | 16 | 400/500 | 36 | 본문 large |
| `1rem` | 16 | 400 | 13 | rem 버전 |
| `18px` | 18 | 500/600 | 14 | 카드 타이틀 |
| `20px` | 20 | 600 | 20 | 섹션 서브 |
| `24px` | 24 | 600 | 21 | H3 |
| `40px` | 40 | 600 | 11 | H2 |
| `48px` | 48 | 600 | 11 | H1 |

> ⚠️ **14px 본문 + 500 medium weight 조합이 signature.** 16px 대신 14px 본문은 Vercel 대시보드 DNA. Heading weight 는 600 (Semibold) 이 표준, 700 은 거의 안 씀. `--font-sans-fallback` 은 system font 지만 실제 렌더는 Geist (Next.js loader 주입).

---

## 06. Colors

### 06-1. Gray Ramp (HSL-based, 11 steps)

| Token | Light HSL | Approx Hex | Dark HSL | Dark Hex |
|---|---|---|---|---|
| `--ds-background-100` | `0, 0%, 100%` | `#FFFFFF` | `0, 0%, 4%` | `#0A0A0A` |
| `--ds-background-200` | `0, 0%, 98%` | `#FAFAFA` | `0, 0%, 7%` | `#121212` |
| `--ds-gray-100` | `0, 0%, 95%` | `#F2F2F2` | `0, 0%, 10%` | `#1A1A1A` |
| `--ds-gray-200` | `0, 0%, 92%` | `#EBEBEB` | `0, 0%, 12%` | `#1F1F1F` |
| `--ds-gray-300` | `0, 0%, 90%` | `#E6E6E6` | `0, 0%, 16%` | `#292929` |
| `--ds-gray-400` | `0, 0%, 92%` | `#EBEBEB` | `0, 0%, 18%` | `#2E2E2E` |
| `--ds-gray-500` | `0, 0%, 79%` | `#C9C9C9` | `0, 0%, 27%` | `#454545` |
| `--ds-gray-600` | `0, 0%, 66%` | `#A8A8A8` | `0, 0%, 40%` | `#666666` |
| `--ds-gray-700` | `0, 0%, 56%` | `#8F8F8F` | `0, 0%, 54%` | `#8A8A8A` |
| `--ds-gray-800` | `0, 0%, 49%` | `#7D7D7D` | `0, 0%, 62%` | `#9E9E9E` |
| `--ds-gray-900` | `0, 0%, 30%` | `#4D4D4D` | `0, 0%, 85%` | `#D9D9D9` |
| `--ds-gray-1000` | `0, 0%, 9%` | `#171717` | `0, 0%, 95%` | `#F2F2F2` |

> Light 와 dark 에서 gray ramp 가 <b>완전히 반전</b>된다. `--ds-gray-1000` 은 light 에서 ink (`#171717`), dark 에서 bright (`#F2F2F2`).

### 06-2. Red Ramp (Vercel DS has red/blue/green/amber/purple/pink/teal families)

| Token | OKLCH | Approx Hex |
|---|---|---|
| `--ds-red-100` | `oklch(96.5% .022 13)` | `#FDE7EA` |
| `--ds-red-500` | `oklch(84% .10 18)` | `#EE939B` |
| `--ds-red-700` | `oklch(60% .22 22)` | `#E01E37` |
| `--ds-red-1000` | (deepest) | `#3D0A0F` |

### 06-3. Integration/Framework Colors (customer logos)

> ⚠️ 이 색들은 <b>Vercel 브랜드가 아니다</b>. 고객사 framework 로고 색으로 carousel·다큐에서만 등장.

| Framework | Hex | Count |
|---|---|---|
| Next.js | `#FF1E56` | 10 |
| Nuxt | `#00DC82` | 8 |
| Svelte | `#FF3E00` | 8 |
| Vue / Astro / generic | `#45DEC4` | 9 |
| Info/link blue | `#0096FF` | 7 |
| Shopify | `#95BF47` | 4 |

### 06-4. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--geist-success` | `#00DC82` (Nuxt 녹) 또는 `#0070F3` variant | deployed |
| `--geist-warning` | amber/orange | building |
| `--geist-error` | `#FF1E56` (Next red) | failed |
| `--ds-focus-color` | accent variant | focus ring |
| `--ds-focus-ring` | `0 0 0 2px var(--ds-background-100), 0 0 0 4px var(--ds-focus-color)` | double-ring focus |

### 06-5. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 50+ | 페이지 배경 |
| 2 | `#000000` | 40+ | 브랜드 · ink |
| 3 | `#00000005` / `#0000000A` / `#00000014` | 14/10/5 | subtle overlay |
| 4 | `#333333` | 12 | ink mid |
| 5 | `#FF1E56` | 10 | Next.js brand |
| 6 | `#EAEAEA` | 9 | border |
| 7 | `#45DEC4` | 9 | framework accent |
| 8 | `#00DC82` / `#FF3E00` | 8 each | Nuxt / Svelte |
| 9 | `#0096FF` | 7 | info blue |
| 10 | `#1F1F1F` | 6 | dark surface |

---

## 07. Spacing

Vercel 은 두 개의 spacing 시스템을 병행한다 — 레거시 `--geist-*` + 현행 `--ds-*`.

### Legacy (`--geist-space-*`)

| Token | Value |
|---|---|
| `--geist-space` | `4px` (기본) |
| `--geist-space-small` | `32px` |
| `--geist-space-medium` | `40px` |
| `--geist-space-large` | `48px` |
| `--geist-space-gap` | `24px` |
| `--geist-space-gap-half` | `12px` |
| `--geist-gap` | `var(--geist-space-gap)` — `24px` |

### Current (`--ds-*`)

| Token | Value |
|---|---|
| `--ds-page-width` | `1400px` (일부 페이지 `1080px` / `1200px`) |

주요 layout 값: `4px / 8px / 12px / 16px / 24px / 32px / 40px / 48px`.

---

## 08. Radius

`unique_radius_values = 28` — 매우 다양. 주로 Tailwind 기본 + 커스텀 혼용.

| Key value | Usage |
|---|---|
| `2px` / `4px` | 인풋 · 작은 버튼 |
| `6px` | 기본 버튼 |
| `8px` | 카드 |
| `12px` / `16px` | 큰 카드 |
| `9999px` | pill |

---

## 09. Shadows

Vercel 은 **33 개 shadow 토큰** — Bucket 내에서 가장 많다. 중요한 건 모든 elevation 이 <b>5-layer composite</b> 라는 것.

```css
/* Base: 1px border + subtle 2% shadow */
--ds-shadow-border-base:     0 0 0 1px #00000014;
--ds-shadow-background-border: 0 0 0 1px var(--ds-background-200);
--ds-shadow-border:          var(--ds-shadow-border-base),
                              var(--ds-shadow-background-border);

/* Small — card resting */
--ds-shadow-small:           0px 2px 2px #0000000A;
--ds-shadow-border-small:    var(--ds-shadow-border-base),
                              var(--ds-shadow-small),
                              var(--ds-shadow-background-border);

/* Medium — dropdowns */
--ds-shadow-medium:          0px 2px 2px #0000000A, 0px 8px 8px -8px #0000000A;

/* Large — popover */
--ds-shadow-large:           0px 2px 2px #0000000A, 0px 8px 16px -4px #0000000A;

/* Menu — 4 layers */
--ds-shadow-menu:
  var(--ds-shadow-border-base),
  0px 1px 1px #00000005,
  0px 4px 8px -4px #0000000A,
  0px 16px 24px -8px #0000000F,
  var(--ds-shadow-background-border);

/* Modal — 5 layers */
--ds-shadow-modal:
  var(--ds-shadow-border-base),
  0px 1px 1px #00000005,
  0px 8px 16px -4px #0000000A,
  0px 24px 32px -8px #0000000F,
  var(--ds-shadow-background-border);

/* Focus — double ring */
--ds-focus-ring:             0 0 0 2px var(--ds-background-100),
                              0 0 0 4px var(--ds-focus-color);
```

> ⚠️ **Composite 그림자가 핵심.** Vercel 의 "카드가 미묘하게 떠 있는" 느낌은 단순 box-shadow 가 아니라 <b>5-layer</b> (border-base + 3개의 y-offset blur + background-border) 때문. 단일 `0 4px 8px rgba(0,0,0,0.1)` 으로는 재현 불가.

---

## 10. Motion

```css
--ds-motion-timing-swift:     cubic-bezier(.175, .885, .32, 1.1);
--ds-motion-overlay-scale:    .96;
--ds-motion-overlay-duration: .3s;
--ds-motion-popover-duration: .2s;
```

> ⚠️ **Overshoot easing.** `cubic-bezier(.175, .885, .32, 1.1)` 의 마지막 1.1 값은 목표점을 살짝 넘어갔다 돌아오는 overshoot. Popover/modal 등장 시 "톡" 하는 느낌이 이 easing 때문.

---

## 12. Components

### Button (primary — black)

```html
<button class="ds-button ds-button--primary">Deploy</button>
```

```css
.ds-button--primary {
  background: var(--ds-gray-1000);       /* #171717 */
  color: var(--ds-background-100);       /* #FFFFFF */
  font-family: var(--font-sans);
  font-weight: 500;
  font-size: 14px;
  padding: 0 12px;
  height: 32px;
  border-radius: 6px;
  border: 0;
  box-shadow: var(--ds-shadow-border-small);
}
.ds-button--primary:hover { background: var(--ds-gray-900); }
.ds-button--primary:focus-visible { box-shadow: var(--ds-focus-ring); }
```

### Card

```html
<article class="ds-card">
  <h3>Deployment ready</h3>
  <p>my-app.vercel.app</p>
</article>
```

```css
.ds-card {
  background: var(--ds-background-100);
  border-radius: 12px;
  padding: 24px;
  box-shadow: var(--ds-shadow-border-small);
}
```

### Code block

```html
<pre><code class="shiki"><span class="kw">const</span> app = <span class="fn">next</span>();</code></pre>
```

```css
pre {
  background: var(--ds-gray-100);
  color: var(--ds-gray-1000);
  padding: 16px 20px;
  border-radius: 8px;
  font-family: var(--font-mono);
  font-size: 13px;
  box-shadow: var(--ds-shadow-border);
}
```

---

## 14. Drop-in CSS

```css
/* Vercel — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-sans: "Geist", var(--font-sans-fallback),
    ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: "Geist Mono", var(--font-mono-fallback),
    ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
    "Liberation Mono", "Courier New", monospace;

  /* Gray scale (light) — HSL values */
  --ds-background-100: hsl(0, 0%, 100%);
  --ds-background-200: hsl(0, 0%, 98%);
  --ds-gray-200:  hsl(0, 0%, 92%);
  --ds-gray-500:  hsl(0, 0%, 79%);
  --ds-gray-900:  hsl(0, 0%, 30%);
  --ds-gray-1000: hsl(0, 0%,  9%);

  /* Shadow composite atoms */
  --ds-shadow-border-base:       0 0 0 1px #00000014;
  --ds-shadow-background-border: 0 0 0 1px var(--ds-background-200);
  --ds-shadow-small:             0px 2px 2px #0000000A;
  --ds-shadow-border-small:
    var(--ds-shadow-border-base),
    var(--ds-shadow-small),
    var(--ds-shadow-background-border);

  /* Motion */
  --ds-motion-timing-swift: cubic-bezier(.175, .885, .32, 1.1);
  --ds-motion-overlay-duration: .3s;
}

body {
  font-family: var(--font-sans);
  font-weight: 400;
  background: var(--ds-background-100);
  color: var(--ds-gray-1000);
  font-size: 14px;
}
```

---

## 15. Tailwind Config

```js
// tailwind.config.js — Vercel
module.exports = {
  theme: {
    extend: {
      colors: {
        ds: {
          'background-100': 'hsl(0, 0%, 100%)',
          'background-200': 'hsl(0, 0%, 98%)',
          gray: {
            100:  'hsl(0, 0%, 95%)',
            200:  'hsl(0, 0%, 92%)',
            300:  'hsl(0, 0%, 90%)',
            400:  'hsl(0, 0%, 92%)',
            500:  'hsl(0, 0%, 79%)',
            600:  'hsl(0, 0%, 66%)',
            700:  'hsl(0, 0%, 56%)',
            800:  'hsl(0, 0%, 49%)',
            900:  'hsl(0, 0%, 30%)',
            1000: 'hsl(0, 0%,  9%)',
          },
        },
      },
      fontFamily: {
        sans: ['Geist', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        mono: ['Geist Mono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',   // signature
        semibold: '600',
      },
      boxShadow: {
        'ds-border': '0 0 0 1px #00000014',
        'ds-small': '0px 2px 2px #0000000A',
        'ds-border-small': '0 0 0 1px #00000014, 0px 2px 2px #0000000A, 0 0 0 1px hsl(0, 0%, 98%)',
      },
      transitionTimingFunction: {
        swift: 'cubic-bezier(.175, .885, .32, 1.1)',
      },
    },
  },
};
```

---

## 16. DO / DON'T

### ✅ DO
- 브랜드는 <b>흑백 monochrome</b>. <code>#000000</code> + <code>#FFFFFF</code> + gray ramp.
- Body 폰트 <code>Geist</code> (Vercel 자체 제작 오픈소스, <code>--font-sans</code> 체인).
- Code 는 <code>Geist Mono</code>.
- Body 기본 사이즈 14px, weight 500 medium 이 UI 라벨의 signature.
- Gray 는 HSL 튜플 <code>0, 0%, *</code> 중립 grey — 색온도 없음.
- 그림자는 <b>5-layer composite</b>: border-base + small/medium/large + background-border.
- Motion easing <code>cubic-bezier(.175, .885, .32, 1.1)</code> overshoot 사용.
- Focus 는 <b>double ring</b> (<code>0 0 0 2px var(--ds-background-100), 0 0 0 4px var(--ds-focus-color)</code>).
- Framework logo color (Next/Nuxt/Svelte) 는 caraousel/logo wall 에만 사용, UI 토큰 아님.

### ❌ DON'T
- ❌ <code>#FF1E56</code>(Next.js red) 을 Vercel 브랜드로 — 그건 Next.js 로고 색.
- ❌ <code>#00DC82</code>(Nuxt) / <code>#FF3E00</code>(Svelte) / <code>#45DEC4</code>(Astro) 를 Vercel accent 로.
- ❌ <code>Inter</code> / <code>Roboto</code> 로 Geist 대체 — signature 깨짐.
- ❌ Body 16px + weight 400 — Vercel 은 14px + 500 medium 이 대시보드 DNA.
- ❌ 단일 box-shadow — 5-layer composite 아니면 "vercel 같은 elevation" 재현 불가.
- ❌ Warm gray — Vercel gray 는 완전 중립 (HSL saturation 0%).
- ❌ `--color-primary` / `--primary` 같은 가상 토큰 — 실제는 `--ds-gray-1000` 으로 ink 구현.
- ❌ 과거 Geist UI 토큰 (<code>--geist-foreground</code> 등) 만 사용 — 현 DS 는 <code>--ds-*</code>.
