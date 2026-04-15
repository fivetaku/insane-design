---
slug: tailwindcss
service_name: Tailwind CSS
site_url: https://tailwindcss.com
fetched_at: 2026-04-11
default_theme: light
brand_color: "#00a5ef"
primary_font: Inter
font_weight_normal: 400
token_prefix: "--color-*, --font-*, --text-*, --radius-*, --spacing"
---

# DESIGN.md — Tailwind CSS (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Tailwind CSS 공식 사이트는 자사 팔레트를 "전시"하는 쇼케이스 역할을 한다. 본문은 중립 zinc/gray + 순백 `#FFFFFF` 라이트 배경만 사용하고, sky/blue/indigo 컬러는 코드 블록과 히어로 악센트에만 등장한다. OKLCH 컬러 공간으로 전환된 v4 팔레트가 22개 family × 11단계로 전개된다.

Inter + IBM Plex Mono 조합이 기본이며, feature settings(`cv02`, `cv03`, `cv04`, `cv11`)가 Inter의 미묘한 typographic 변형을 만드는 핵심이다. Bold는 `font-semibold`(600)이며 700은 거의 미사용이다. `@theme` CSS 블록에서 모든 토큰이 전역 노출되는 v4 구조가 특징적이다.

**Key Characteristics:**
- Sky `#00a5ef`가 브랜드 시그니처 — 페이지는 중립 zinc 기반
- Inter feature settings `cv02/cv03/cv04/cv11`가 시각적 차별점
- IBM Plex Mono + `ss02/zero` feature settings
- Tailwind v4 `@theme` 블록 + OKLCH 컬러 공간
- Weight 400/500/600만 사용 (700은 거의 없음)

---

## 01. Quick Start

> 5분 안에 tailwindcss.com 처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트: Inter sans + IBM Plex Mono */
:root {
  --font-inter: "Inter", ui-sans-serif, system-ui, sans-serif;
  --font-plex-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --default-font-family: var(--font-inter), system-ui;
  --default-font-feature-settings: "cv02", "cv03", "cv04", "cv11";
}
body {
  font-family: var(--default-font-family);
  font-weight: 400;
  font-feature-settings: var(--default-font-feature-settings);
}
code, pre {
  font-family: var(--font-plex-mono), monospace;
  font-feature-settings: "ss02", "zero";
}

/* 2. 배경 + 텍스트 (light 기본) */
:root { --bg: #ffffff; --fg: #0a0a0a; }  /* neutral-950 */
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 — Tailwind signature sky */
:root { --color-sky-500: #00a5ef; }      /* Tailwind 브랜드 하늘색 */
```

**절대 하지 말아야 할 것 하나**: Tailwind CSS v4 는 "OKLCH 컬러 공간" 으로 전환했지만, `--color-*-500` 은 `lab(…)` 과 hex 폴백 **두 가지** 가 함께 선언돼 있다. 단순 hex (`#3080ff`) 만 쓰면 OKLCH 의 감마 보정된 그린/블루/바이올렛의 실제 시각 톤이 재현 안 된다. 브라우저가 lab 을 지원하면 그쪽이 우선이며, 페이지 렌더링 색은 sRGB hex 보다 조금 더 맑고 채도가 높다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://tailwindcss.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| CSS files | 2개 외부, 총 675,050자 |
| Primary bundle | `0aa6f91bf69bba4f.css` (Next.js hashed) |
| Token count | 573 custom properties · 304 color · 9 spacing · 37 shadow |
| Token prefix | `--color-*`, `--font-*`, `--text-*`, `--radius-*`, `--spacing` |
| Method | CSS 커스텀 프로퍼티 + `@theme` 블록 직접 파싱 |

---

## 03. Tech Stack

- **Framework**: Next.js + Tailwind CSS v4 (self-hosted)
- **Design system**: Tailwind v4 default theme = "OKLCH palette" (22 color families × 11 steps = 242 core hues)
- **CSS architecture**: `@theme` 블록에서 모든 토큰 전역 노출
  ```
  @theme {
    --font-sans: var(--font-inter), system-ui;
    --font-mono: var(--font-plex-mono), monospace;
    --color-{family}-{50..950}  // 22 families × 11 steps
    --radius-{xs..4xl}          // 8 steps
    --text-{xs..9xl}            // 13 steps
    --spacing: 0.25rem          // single multiplier
  }
  ```
- **Class naming**: Tailwind utilities 그대로. 커스텀 prefix 없음.
- **Default theme**: **light**. 페이지 배경 `#FFFFFF`. Dark mode 는 `.dark` 클래스 토글 — 본사 사이트는 light 가 기본.
- **Font loading**: Next.js font loader. `--font-inter` + `--font-plex-mono` + `--font-source-sans-pro` + `--font-ubuntu-mono` 네 개 전부 주입됨 (폰트 쇼케이스 용도).
- **Canonical anchor**: `#00a5ef` (`--color-sky-500`) — Tailwind 브랜드 시그니처 sky.

---

## 04. Font Stack

- **Primary sans**: `Inter` (via `--font-inter` Next.js 로더)
- **Primary mono**: `IBM Plex Mono` (via `--font-plex-mono`)
- **Feature settings**: `cv02`, `cv03`, `cv04`, `cv11` (character variants — Inter 의 single-story g, straight l 등)
- **Code feature settings**: `ss02`, `zero` (IBM Plex 의 slashed zero + alt characters)
- **Secondary**: `Source Sans Pro`, `Ubuntu Mono` (font showcase 용)
- **Weight normal / bold**: `400` / `600` (bold 는 600, 700 아님)

```css
:root {
  --font-inter: "Inter", ui-sans-serif, system-ui, sans-serif;
  --font-plex-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --font-source-sans-pro: "Source Sans Pro", ui-sans-serif, system-ui, sans-serif;
  --font-ubuntu-mono: "Ubuntu Mono", ui-monospace, monospace;

  --default-font-family: var(--font-inter), system-ui;
  --default-font-feature-settings: "cv02", "cv03", "cv04", "cv11";

  --default-mono-font-family: var(--font-plex-mono), monospace;
  --default-mono-font-feature-settings: "ss02", "zero";
}
body {
  font-family: var(--default-font-family);
  font-feature-settings: var(--default-font-feature-settings);
}
```

> ⚠️ **Feature settings 가 핵심.** Inter 의 `cv02`/`cv03`/`cv04`/`cv11` 를 켜지 않으면 Tailwind 사이트 특유의 미묘한 typographic 느낌이 안 난다. IBM Plex Mono 의 `ss02`/`zero` 는 slashed zero 와 대체 문자 — 코드 블록에서 필수.

---

## 05. Typography Scale

| Class | Size | Weight | Line-height |
|---|---|---|---|
| `text-xs` | 12px | 400 | 1.33 |
| `text-sm` | 14px | 400 | 1.5 |
| `text-base` | 16px | 400 | 1.5 |
| `text-lg` | 18px | 400 | 1.56 |
| `text-xl` | 20px | 500 | 1.4 |
| `text-2xl` | 24px | 600 | 1.33 |
| `text-3xl` | 30px | 600 | 1.2 |
| `text-4xl` | 36px | 600 | 1.11 |
| `text-5xl` | 48px | 600 | 1.0 |
| `text-6xl` | 60px | 600 | 1.0 |
| `text-7xl` | 72px | 600 | 1.0 |
| `text-8xl` | 96px | 600 | 1.0 |
| `text-9xl` | 128px | 600 | 1.0 |

> ⚠️ **Weight 600 이 bold.** Tailwind 본사 사이트는 weight 400 / 500 / 600 세 개만 사용. `700` (font-bold) 은 거의 등장하지 않고, 대신 `font-semibold` (600) 이 heading 전용. Hero headline 은 `text-6xl` 이상 + `font-semibold`.

---

## 06. Colors

### 06-1. Tailwind v4 Core Palette (22 families × 11 steps)

Tailwind v4 는 아래 22 개 컬러 family 를 기본 제공한다. 각 family 는 `50`, `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`, `950` 11 단계를 가진다.

```
red, orange, amber, yellow, lime, green, emerald, teal, cyan, sky, blue,
indigo, violet, purple, fuchsia, pink, rose,
slate, gray, zinc, neutral, stone, mauve, olive
```

### 06-2. Key mid-steps (`-500`)

| Family | Hex (sRGB) | LAB equiv |
|---|---|---|
| `red-500` | `#fb2c36` | `lab(55.48% 75.07 48.85)` |
| `orange-500` | `#ff6900` | `lab(64% 55 75)` |
| `amber-500` | `#f99c00` | `lab(72.72% 31.87 97.94)` |
| `green-500` | `#00c758` | `lab(70.55% -66.51 45.81)` |
| `cyan-500` | `#00b7d7` | `lab(67.81% -35.40 -30.20)` |
| `sky-500` ★ | `#00a5ef` | Tailwind 브랜드 (signature) |
| `blue-500` | `#3080ff` | `lab(54.17% 13.34 -74.68)` |
| `indigo-500` | `#625fff` | `lab(48.30% 38.31 -81.97)` |
| `violet-500` | `#8d54ff` | `lab(49.94% 55.18 -81.90)` |
| `slate-500` | `#62748e` | |
| `gray-500` | `#6a7282` | |
| `zinc-500` | `#71717b` | |
| `neutral-500` | `#737373` | |
| `stone-500` | `#79716b` | |

### 06-3. Key ramp example — sky (브랜드)

| Token | Hex |
|---|---|
| `--color-sky-50` | `#f0f9ff` |
| `--color-sky-100` | `#dff2fe` |
| `--color-sky-200` | `#b8e6fe` |
| `--color-sky-300` | `#74d4ff` |
| `--color-sky-400` | `#00beff` |
| `--color-sky-500` ★ | `#00a5ef` |
| `--color-sky-600` | `#0084d1` |
| `--color-sky-700` | `#0069a8` |
| `--color-sky-800` | `#00598a` |
| `--color-sky-900` | `#024a70` |
| `--color-sky-950` | `#052f4a` |

### 06-4. Neutral (zinc — 본사 사이트 기본 neutral)

| Token | Hex |
|---|---|
| `zinc-50` | `#fafafa` |
| `zinc-100` | `#f4f4f5` |
| `zinc-200` | `#e4e4e7` |
| `zinc-300` | `#d4d4d8` |
| `zinc-400` | `#9f9fa9` |
| `zinc-500` | `#71717b` |
| `zinc-600` | `#52525c` |
| `zinc-700` | `#3f3f46` |
| `zinc-800` | `#27272a` |
| `zinc-900` | `#18181b` |
| `zinc-950` | `#09090b` |

### 06-5. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF1A` | 103 | 10% white overlay |
| 2 | `#00000000` | 60 | transparent |
| 3 | `#0000001A` | 53 | 10% black overlay |
| 4 | `#FFFFFF` | 47 | 페이지 배경 |
| 5 | `#0307120D` | 41 | border subtle |
| 6+ | 수백 개 | 그 외 | v4 core palette 전부 서빙 |

> ⚠️ **페이지 자체는 중립 톤.** Tailwind 사이트는 자신의 팔레트를 "전시" 하기 위해 본문은 중립(zinc/gray)+light 배경만 쓰고, 코드 블록과 hero 악센트에만 sky/blue/indigo 를 사용.

---

## 07. Spacing

> Tailwind v4 는 <b>단일 `--spacing` 배수</b> 로 모든 간격을 생성한다.

```css
@theme {
  --spacing: 0.25rem;  /* 4px — 모든 spacing utility 의 기본 */
}
```

| Utility | Computed |
|---|---|
| `p-1` | `0.25rem` (4px) |
| `p-2` | `0.5rem` (8px) |
| `p-3` | `0.75rem` (12px) |
| `p-4` | `1rem` (16px) |
| `p-6` | `1.5rem` (24px) |
| `p-8` | `2rem` (32px) |
| `p-12` | `3rem` (48px) |
| `p-16` | `4rem` (64px) |
| `p-24` | `6rem` (96px) |

> ⚠️ **v4 의 spacing 변화:** v3 은 각 스텝을 커스텀 프로퍼티로 하드코딩했지만, v4 는 `--spacing` 단일 값 × 배수로 동적 생성. `p-13` 같은 "존재하지 않던" 값도 `calc(var(--spacing) * 13)` 로 자동 생성됨.

---

## 08. Radius

| Token | Value | Pixels |
|---|---|---|
| `--radius-xs` | `.125rem` | 2px |
| `--radius-sm` | `.25rem` | 4px |
| `--radius-md` | `.375rem` | 6px |
| `--radius-lg` | `.5rem` | 8px |
| `--radius-xl` | `.75rem` | 12px |
| `--radius-2xl` | `1rem` | 16px |
| `--radius-3xl` | `1.5rem` | 24px |
| `--radius-4xl` | `2rem` | 32px |

> ⚠️ **v4 의 unique_radius_values = 2.** 토큰 변수는 8 개이지만 실제 사이트에서 유일하게 쓰이는 raw radius 는 2 종뿐 (라운드 카드 + pill). 토큰을 풀 스케일로 노출하지만 본사 사이트 자체의 사용은 절제적.

---

## 09. Shadows

Tailwind v4 는 37 개의 shadow 커스텀 프로퍼티를 이미 노출한다 (`--shadow-xs` ~ `--shadow-2xl`, `--inset-shadow-*`, `--drop-shadow-*`, `--text-shadow-*`).

| Key | Value |
|---|---|
| `--shadow-xs` | `0 1px rgb(0 0 0 / 0.05)` |
| `--shadow-sm` | `0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)` |
| `--shadow-md` | `0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)` |
| `--shadow-lg` | `0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)` |
| `--shadow-xl` | `0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)` |
| `--shadow-2xl` | `0 25px 50px -12px rgb(0 0 0 / 0.25)` |

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

### Button (brand sky primary)

```html
<button class="inline-flex items-center gap-2 rounded-lg bg-sky-500 px-4 py-2 text-sm font-semibold text-white hover:bg-sky-600">
  Get started
</button>
```

### Code block (본사 사이트 스타일)

```html
<pre class="rounded-xl bg-zinc-950 p-6 font-mono text-sm text-zinc-50 font-feature-settings-[ss02,zero]">
  <code class="language-html">&lt;div class="bg-sky-500"&gt;Hello&lt;/div&gt;</code>
</pre>
```

### Color swatch grid (자체 예시)

```html
<div class="grid grid-cols-11 gap-2">
  <div class="aspect-square rounded bg-sky-50"></div>
  <div class="aspect-square rounded bg-sky-100"></div>
  <div class="aspect-square rounded bg-sky-200"></div>
  <!-- ... up to -950 -->
</div>
```

---

## 15. Drop-in CSS

```css
/* Tailwind CSS v4 — copy into your @theme block */
@theme {
  --font-inter: "Inter", ui-sans-serif, system-ui, sans-serif;
  --font-plex-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --default-font-family: var(--font-inter), system-ui;
  --default-font-feature-settings: "cv02", "cv03", "cv04", "cv11";
  --default-mono-font-family: var(--font-plex-mono), monospace;
  --default-mono-font-feature-settings: "ss02", "zero";

  /* Sky (brand) */
  --color-sky-50:  #f0f9ff;
  --color-sky-300: #74d4ff;
  --color-sky-500: #00a5ef;   /* ← canonical */
  --color-sky-600: #0084d1;
  --color-sky-900: #024a70;

  /* Neutral (zinc) */
  --color-zinc-50:  #fafafa;
  --color-zinc-200: #e4e4e7;
  --color-zinc-500: #71717b;
  --color-zinc-800: #27272a;
  --color-zinc-950: #09090b;

  /* Spacing — single multiplier */
  --spacing: 0.25rem;

  /* Radius */
  --radius-md: 0.375rem;
  --radius-lg: 0.5rem;
  --radius-xl: 0.75rem;
}

body {
  font-family: var(--default-font-family);
  font-feature-settings: var(--default-font-feature-settings);
  background: #ffffff;
  color: #09090b;  /* zinc-950 */
}
```

---

## 16. Tailwind Config

Tailwind v4 는 JS config 를 권장하지 않는다 — 대신 `@theme` CSS 블록을 사용. 하지만 v3 호환 config 를 원한다면:

```js
// tailwind.config.js (v3-style — v4 는 @theme 권장)
module.exports = {
  theme: {
    extend: {
      colors: {
        // Tailwind v4 default palette (일부)
        sky: {
          50:  '#f0f9ff', 100: '#dff2fe', 200: '#b8e6fe', 300: '#74d4ff',
          400: '#00beff', 500: '#00a5ef', 600: '#0084d1', 700: '#0069a8',
          800: '#00598a', 900: '#024a70', 950: '#052f4a',
        },
        zinc: {
          50: '#fafafa', 100: '#f4f4f5', 200: '#e4e4e7', 300: '#d4d4d8',
          400: '#9f9fa9', 500: '#71717b', 600: '#52525c', 700: '#3f3f46',
          800: '#27272a', 900: '#18181b', 950: '#09090b',
        },
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        mono: ['IBM Plex Mono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      },
      fontFeatureSettings: {
        default: ['"cv02"', '"cv03"', '"cv04"', '"cv11"'],
        mono:    ['"ss02"', '"zero"'],
      },
      borderRadius: {
        xs: '.125rem', sm: '.25rem', md: '.375rem', lg: '.5rem',
        xl: '.75rem', '2xl': '1rem', '3xl': '1.5rem', '4xl': '2rem',
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
| Brand | `#00a5ef` |
| Page BG | `#ffffff` |
| Text Primary | `#0a0a0a` |
| Default Theme | light |

### Component Prompts

> **Hero section**: "Tailwind CSS 스타일 hero — `Inter` 폰트, `#00a5ef` brand color, light 배경"
>
> **CTA button**: "Tailwind CSS primary CTA — brand `#00a5ef` 배경 또는 dark fill, `Inter` 폰트"
>
> **Card component**: "Tailwind CSS 스타일 카드 — light 테마, 기존 radius/shadow 토큰 준수"

### Iteration Guide

1. **Color 교체 시**: 반드시 §06 Colors 테이블의 실제 hex 참조. AI 추론 색상 사용 금지.
2. **Typography 변경 시**: §04 Font Stack의 font-family 체인 + §05의 weight/size 매핑 확인.
3. **Spacing 조정 시**: §07 Spacing의 토큰 스케일 내에서만 변경.
4. **신규 컴포넌트**: §13 Components의 기존 패턴(radius, shadow, padding)을 기반으로 확장.

---

## 18. DO / DON'T

### ✅ DO
- Tailwind v4 `@theme` 블록으로 토큰 선언. v3 config 보다 우선.
- 폰트는 `Inter` (sans) + `IBM Plex Mono` (mono). 둘 다 Next.js font loader 경유.
- Feature settings 필수: Inter 에 `"cv02", "cv03", "cv04", "cv11"`, IBM Plex Mono 에 `"ss02", "zero"`.
- Bold 는 `font-semibold` (600). `font-bold` (700) 은 거의 안 씀.
- Heading 은 `text-6xl` ~ `text-9xl` + `font-semibold` 조합.
- Neutral 은 `zinc` family (zinc-950 ink, zinc-50 surface).
- 브랜드 강조 색은 `sky-500` (#00a5ef).
- Spacing 은 `--spacing: 0.25rem` 단일 배수로 — 모든 p-* / m-* / gap-* 가 자동 생성.

### ❌ DON'T
- ❌ Tailwind v3 의 개별 spacing 토큰(`--space-*`) 가정 — v4 는 단일 `--spacing` 배수
- ❌ `text-3xl` + `font-bold` (700) — 본사 사이트는 600 이 최대
- ❌ `#0066cc` 같은 과거 Tailwind 브랜드 블루 — 현재는 `sky-500: #00a5ef`
- ❌ `Roboto` / `Helvetica` 폰트 — `Inter` + feature settings 체인이 signature
- ❌ `Fira Code` / `JetBrains Mono` 코드 폰트 — 본사는 `IBM Plex Mono`
- ❌ Color 를 raw hex 로만 사용 — `lab()` fallback 이 함께 선언돼 있어 브라우저에 따라 시각 톤 다름
- ❌ Radius 를 1px/3px 같은 "비표준 값" 사용 — 토큰 8 단계 준수
- ❌ 본사 사이트를 dark theme 으로 가정 — 기본은 light, `.dark` 는 optional toggle
