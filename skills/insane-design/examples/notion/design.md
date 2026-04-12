---
slug: notion
service_name: Notion
site_url: https://www.notion.so
fetched_at: 2026-04-11
default_theme: light
brand_color: "#2383E2"
primary_font: NotionInter
font_weight_normal: 400
token_prefix: color
---

# DESIGN.md — Notion (Claude Code Edition)

---

## 01. Quick Start

> 5분 안에 Notion처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — NotionInter (custom) + 3-way 토글 */
body {
  font-family: "NotionInter", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif;
  font-weight: 400;
}
.serif-block {
  font-family: "Lyon Text", "Lyon-Text", Georgia, ui-serif, serif;
}
.mono-block, code, pre {
  font-family: "iA Writer Mono", "iawriter-mono", "Nitti", Menlo, Courier, monospace;
}

/* 2. Warm ink + warm off-white — pure black 금지 */
:root {
  --color-ink-primary: #37352F;       /* warm ink */
  --color-ink-muted:   #37352FA6;     /* α65 */
  --color-ink-faint:   #37352F99;     /* α60 */
  --color-ink-divider: #37352F29;     /* α16 */
  --color-bg-page:     #FFFFFF;
  --color-bg-soft:     #F7F7F5;
  --color-border:      #E9E9E7;
}
body { background: var(--color-bg-page); color: var(--color-ink-primary); }

/* 3. 링크 블루 */
:root {
  --color-link: #2383E2;
  --color-link-alt: #097FE8;
}
```

**절대 하지 말아야 할 것 하나**: 본문 text 색을 **pure black `#000000`**으로 쓰지 말 것. Notion의 진짜 정체성은 **warm ink `#37352F`** (갈색 섞인 따뜻한 검정)와 그 알파 변종 5단계 (`A6/99/29/17`)다. 순흰색 배경에 순검정 텍스트로 만들면 Notion의 "paper-like" 느낌이 완전히 증발한다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.notion.so` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| Framework | Next.js + 자체 CSS 시스템 |
| Custom props | 1,111 (color: 326 · spacing: 304 · shadow: 8) |
| Token prefix | `--color-*`, `--font-size-*`, `--spacing-*`, `--campaigns-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · 캠페인 네임스페이스 식별 |

---

## 03. Tech Stack

- **Framework**: Next.js marketing (자체 디자인 토큰 시스템, Tailwind 아님)
- **Design system**: Notion 자체 3-layer token indirection
  ```
  semantic role         color-button-primary-background
  palette reference  →  color-campaigns-agents-launch-blue-400
  literal hex        →  #2537B1
  ```
- **CSS architecture**: 전통적 CSS 커스텀 프로퍼티 + BEM-ish 의미있는 클래스 (`.notion-logo-fill`, `.bento-shadow-level`, `.campaign-nav-bg`)
- **Campaign namespace**: 2026-04-11 크롤 시점은 **"AI Agents launch" 캠페인**. `campaigns-agents-launch-*` blue palette가 active. 이는 영구 브랜드가 아니라 캠페인 오버레이.
- **Default theme**: **Light** (warm white bg `#FFFFFF` / `#F7F7F5`)
- **Font loading**: 3-way 토글 (`var(--rich-text-font-config-font-family)`) — Default / Serif / Mono
- **Canonical anchor**: warm ink `#37352F` · link `#2383E2` · campaign navy `#2537B1`

---

## 04. Font Stack

Notion은 **3가지 폰트를 동시에 로드**하는 3-way 토글 시스템이다. 블록별로 `Default / Serif / Mono`를 선택하면 `var(--rich-text-font-config-font-family)`가 동적으로 바뀐다.

- **Default Sans**: `NotionInter` — Inter를 기반으로 Notion이 metric/hinting/OpenType feature를 수정한 커스텀 빌드. 일반 Inter와 x-height · figures · i/l disambiguation이 다르다.
- **Serif option**: `Lyon Text` — Commercial Type의 유료 세리프 폰트.
- **Mono option**: `iA Writer Mono` — iA Writer 브랜드의 typewriter-style mono.

```css
:root {
  --font-family-sans:  "NotionInter", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif;
  --font-family-serif: "Lyon Text", "Lyon-Text", Georgia, ui-serif, serif;
  --font-family-mono:  "iA Writer Mono", "iawriter-mono", "Nitti", Menlo, Courier, monospace;

  --rich-text-font-config-font-family: var(--font-family-sans); /* 블록별 override 가능 */
}

body {
  font-family: var(--font-family-sans);
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
}

.block--serif { --rich-text-font-config-font-family: var(--font-family-serif); }
.block--mono  { --rich-text-font-config-font-family: var(--font-family-mono); }
```

> ⚠️ **NotionInter vs Inter** — Notion은 Inter를 그대로 쓰지 않는다. x-height, tabular figures, dot-on-i가 다르다. 그냥 Inter로 대체하면 미묘하게 "Notion스럽지 않다". OSS 대체 시 `Inter Variable`로 근사치 가능. **Lyon Text와 iA Writer Mono는 유료**이므로, OSS 환경에서는 `Newsreader` / `JetBrains Mono`가 각각의 가장 가까운 대체.

---

## 05. Typography Scale

Notion은 **13단계 font-size 토큰**을 운용한다 (`font-size-50` ~ `font-size-1000`).

| Token | Size (rem) | Size (px) | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|---|
| `font-size-50`   | 0.75rem    | 12px | 400 | 1.5  | +0.0078125rem |
| `font-size-100`  | 0.875rem   | 14px | 400 | 1.5  | 0             |
| `font-size-150`  | 0.9375rem  | 15px | 400 | 1.5  | 0             |
| `font-size-200`  | 1rem       | 16px | 400 | 1.5  | 0             |
| `font-size-300`  | 1.125rem   | 18px | 500 | 1.4  | -0.0078125rem |
| `font-size-350`  | 1.25rem    | 20px | 500 | 1.35 | -0.01em       |
| `font-size-400`  | 1.375rem   | 22px | 550 | 1.3  | -0.015625rem  |
| `font-size-500`  | 1.625rem   | 26px | 600 | 1.25 | -0.015625rem  |
| `font-size-600`  | 2rem       | 32px | 600 | 1.2  | -0.0390625rem |
| `font-size-700`  | 2.625rem   | 42px | 700 | 1.15 | -0.046875rem  |
| `font-size-800`  | 3.375rem   | 54px | 700 | 1.1  | -0.0625rem    |
| `font-size-900`  | 4rem       | 64px | 700 | 1.05 | -0.0625rem    |
| `font-size-1000` | 4.75rem    | 76px | 700 | 1.0  | -0.0625rem    |

### Letter-spacing optical compensation

| Scale | Tracking |
|---|---|
| `sans-50`  | `+0.0078125rem` (작은 사이즈 + tracking) |
| `sans-100` | `0` |
| `sans-300` | `-0.0078125rem` |
| `sans-400` | `-0.015625rem` |
| `sans-500` | `-0.0390625rem` |
| `sans-600-regular`  | `-0.0625rem` |
| `sans-600-semibold` | `-0.046875rem` (같은 사이즈 weight별 미세 보정) |

> ⚠️ Weight별 미세 보정이 특이 — 600-regular과 600-semibold의 tracking이 다르다. Linear와 같은 optical compensation 철학.

---

## 06. Colors

### 06-1. Warm Neutral (Notion identity)

| Token | Hex | Usage |
|---|---|---|
| `--color-ink-primary`  | `#37352F`   | 본문 기본 text (30회) |
| `--color-ink-strong`   | `#37352FCC` | 80% |
| `--color-ink-muted`    | `#37352FA6` | 65% (22회) |
| `--color-ink-faint`    | `#37352F99` | 60% (6회) |
| `--color-ink-divider`  | `#37352F29` | 16% 디바이더 (6회) |
| `--color-ink-hairline` | `#37352F17` | 9% hairline (5회) |
| `--color-bg-page`      | `#FFFFFF`   | page bg (38회) |
| `--color-bg-soft`      | `#F7F7F5`   | warm off-white sidebar/panel (5회) |
| `--color-border-base`  | `#E9E9E7`   | border (6회) |
| `--color-hairline-alpha`| `#0F0F0F1A`| α10 near-black hairline |
| `--color-hairline-light`| `#00000014`| α8 black hairline |

### 06-2. Link / Brand Blue

| Token | Hex | Usage |
|---|---|---|
| `--color-link`       | `#2383E2` | 본문 링크 (9회) |
| `--color-link-alt`   | `#097FE8` | 보조 링크 (3회) |

### 06-3. Campaign — AI Agents Launch (2026 크롤 시점)

| Token | Hex | Usage |
|---|---|---|
| `--color-campaigns-agents-launch-blue-900` | `#2537B1` | campaign navy (16회) |
| `--color-campaigns-agents-launch-blue-400` | — | primary button bg |
| `--color-campaigns-agents-launch-blue-300` | — | button hover |

> ⚠️ 이는 2026-04-11 AI Agents 런칭 캠페인용 **일시적 overlay**다. 영구 브랜드 색이 아니다. Notion Classic 팔레트는 warm neutral + link blue 중심.

### 06-4. Block / Callout Palette

Notion 블록의 tag, callout, highlight에 사용되는 기본 9색. 각 색은 text / background pair로 존재.

| Color | Text | Background |
|---|---|---|
| gray   | `#787774` | `#F1F1EF` |
| brown  | `#976D57` | `#F4EEEE` |
| orange | `#CC782F` | `#FAEBDD` |
| yellow | `#C29343` | `#FBF3DB` |
| green  | `#448361` | `#EDF3EC` |
| blue   | `#337EA9` | `#E7F3F8` |
| purple | `#9065B0` | `#F4EFF9` |
| pink   | `#C14C8A` | `#F9EEF3` |
| red    | `#D44C47` | `#FDEBEC` |

### 06-5. Campaign Rainbow (hero accent)

| Token | Hex |
|---|---|
| `campaign-yellow` | `#FFB110` |
| `campaign-red`    | `#F64932` |
| `campaign-orange` | `#FF8A33` |
| `campaign-teal`   | `#2A9D99` |
| `campaign-blue`   | `#097FE8` |
| `campaign-purple` | `#AD6DED` |
| `campaign-pink`   | `#FF83DD` |

### 06-6. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#00000000` | 98 | transparent |
| 2 | `#FFFFFF`   | 38 | page bg |
| 3 | `#000000`   | 37 | SVG/logo 색 |
| 4 | `#37352F`   | 30 | **warm ink primary** |
| 5 | `#37352FA6` | 22 | α65 warm ink muted |
| 6 | `#2537B1`   | 16 | campaign navy |
| 7 | `#2383E2`   |  9 | link blue |
| 8 | `#000000BF` |  7 | α75 black |
| 9 | `#00000014` |  6 | α8 black hairline |
| 10| `#37352F99` |  6 | α60 warm ink |
| 11| `#37352F29` |  6 | α16 divider |
| 12| `#E9E9E7`   |  6 | warm gray border |

---

## 07. Spacing

Notion은 **304개의 spacing 변수**와 5단계 scale + block-level + nav/marquee 전용 변수.

| Token | Value | Use case |
|---|---|---|
| `--spacing-xs`      | 20px  | tight |
| `--spacing-s`       | 40px  | small |
| `--spacing-m`       | 40px  | medium (same as s intentionally) |
| `--spacing-l`       | 60px  | large |
| `--spacing-xl`      | 60px  | extra-large |
| `--spacing-block-s` | 20px  | 블록 small |
| `--spacing-block-m` | 24px  | 블록 medium |
| `--spacing-block-l` | 32px  | 블록 large |
| `--nav-top-padding` | 14px  | top nav |
| `--base-padding`    | 20px  | base |
| `--marquee-item-gap`| 12px  | logo marquee |
| `--marquee-padding-y`| 50px | marquee vertical |

> ⚠️ Notion은 **8pt 그리드가 아니다**. 20/40/60 같은 20 단위가 주력이며, 블록 inner는 20/24/32 혼용.

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| radius-xs   | 3px    | inline chip (11회) |
| radius-sm   | 4-5px  | small button |
| radius      | 8px    | button (9회) |
| radius-md   | 12px   | card (**최빈** — 13회) |
| radius-lg   | 20px   | large card |
| radius-xl   | 38px   | hero block (2회) |
| radius-pill | 1000px | avatar / pill (2회) |

---

## 09. Shadows

Notion은 **3-level composite shadow 시스템**. 가장 정교한 것은 `shadow-level-200`의 4-layer stack.

| Token | Value | Usage |
|---|---|---|
| `--dropdown-shadow` | `0 4px 4px -2px #00000014` | 드롭다운 |
| `--shadow-level-100`| `0px 3px 9px #00000008, 0px 0.7px 1.4625px rgba(0,0,0,.015)` | subtle card |
| `--shadow-level-200`| 4-layer (아래 참고) | default card |
| `--shadow-level-300`| `0px 20px 50px #00000014, 0px 6px 16px #0000000a` | modal |
| `--shadow-filter`   | `0 4px 18px #0000004d` | backdrop blur |

```css
--shadow-level-200:
  0px 4px 18px #0000000a,
  0px 2.025px 7.84688px rgba(0,0,0,0.027),
  0px 0.8px 2.925px #00000005,
  0px 0.175px 1.04062px rgba(0,0,0,0.013);
```

> ⚠️ Notion의 "flat" 인상은 오해. **실제로는 매우 섬세한 4-layer micro-shadow**로 bento card와 media block에 elevation을 준다. 단일 drop shadow로는 재현 안 됨.

---

## 11. Layout Patterns

### Marketing Hero (캠페인 버전)
- Background: `#FFFFFF` + campaign navy `#2537B1` 그라데이션
- H1: 54-76px / weight 700 / tracking -0.0625rem
- Max-width: 1280px

### Document (Notion block interior)
- Canvas: `#FFFFFF`
- Sidebar: `#F7F7F5` (warm off-white)
- Block padding: `spacing-block-m` = 24px
- Max reading width: 708-900px

```css
.notion-page { background: #FFFFFF; color: #37352F; }
.notion-sidebar { background: #F7F7F5; border-right: 1px solid #E9E9E7; }
.notion-block { padding: 3px 0; border-radius: 3px; }
```

---

## 12. Components

### 12.1 Primary Button (Campaign blue)

```html
<a class="btn-primary">Try Notion free</a>
```

| Spec | Value |
|---|---|
| Background | `#2537B1` (campaign) or `#2383E2` (classic) |
| Text | `#FFFFFF` |
| Padding | `8px 14px` |
| Radius | `5px` |
| Font weight | 500 |

### 12.2 Ghost Button

| Spec | Value |
|---|---|
| Background | transparent |
| Text | `#37352F` |
| Hover bg | `#00000008` (α8 hairline) |
| Padding | `8px 14px` |
| Radius | `5px` |

### 12.3 Block (content)

```html
<div class="notion-block notion-block--heading">
  <h2>Section title</h2>
</div>
```

| Spec | Value |
|---|---|
| Background | transparent |
| Text | `var(--color-ink-primary)` (#37352F) |
| Padding | `3px 2px` |
| Radius | `3px` |
| Hover bg | `#37352F0A` |

### 12.4 Callout (colored block)

```html
<div class="callout callout--blue">
  <span class="icon">💡</span>
  <p>Tip text</p>
</div>
```

Callout은 `06-4` 9색 팔레트에서 text/bg pair를 가져와 적용.

```css
.callout--blue {
  background: #E7F3F8;
  color: #337EA9;
  border-radius: 3px;
  padding: 16px 16px 16px 48px;
}
```

### 12.5 Bento Card (marketing)

```html
<div class="bento-card bento-shadow-level-200">
  <h3>Wiki</h3>
  <p>Build a connected workspace.</p>
</div>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Border-radius | `12px` or `20px` |
| Shadow | `var(--shadow-level-200)` (4-layer) |
| Padding | `32px` |

---

## 14. Drop-in CSS

```css
/* Notion — copy into your root stylesheet */
:root {
  /* Fonts — 3-way toggle */
  --font-family-sans:  "NotionInter", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  --font-family-serif: "Lyon Text", "Lyon-Text", Georgia, ui-serif, serif;
  --font-family-mono:  "iA Writer Mono", "iawriter-mono", "Nitti", Menlo, Courier, monospace;
  --rich-text-font-config-font-family: var(--font-family-sans);

  /* Warm neutral — Notion identity */
  --color-ink-primary:  #37352F;
  --color-ink-strong:   #37352FCC;
  --color-ink-muted:    #37352FA6;
  --color-ink-faint:    #37352F99;
  --color-ink-divider:  #37352F29;
  --color-ink-hairline: #37352F17;
  --color-bg-page:      #FFFFFF;
  --color-bg-soft:      #F7F7F5;
  --color-border-base:  #E9E9E7;

  /* Link */
  --color-link:     #2383E2;
  --color-link-alt: #097FE8;

  /* Campaign (temporary — AI Agents launch) */
  --color-campaign-navy:   #2537B1;
  --color-campaign-yellow: #FFB110;
  --color-campaign-red:    #F64932;

  /* Block palette (callout) */
  --callout-blue-text: #337EA9;  --callout-blue-bg: #E7F3F8;
  --callout-gray-text: #787774;  --callout-gray-bg: #F1F1EF;
  --callout-green-text:#448361;  --callout-green-bg:#EDF3EC;

  /* Radius */
  --radius-xs: 3px;
  --radius-sm: 5px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-pill: 1000px;

  /* Shadow (4-layer composite) */
  --shadow-level-200:
    0px 4px 18px #0000000a,
    0px 2.025px 7.84688px rgba(0,0,0,0.027),
    0px 0.8px 2.925px #00000005,
    0px 0.175px 1.04062px rgba(0,0,0,0.013);
}

body {
  background: var(--color-bg-page);
  color: var(--color-ink-primary);
  font-family: var(--font-family-sans);
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
}

.block--serif { font-family: var(--font-family-serif); }
.block--mono  { font-family: var(--font-family-mono); }
a             { color: var(--color-link); }
```

---

## 15. Tailwind Config

```js
// tailwind.config.js — Notion
module.exports = {
  theme: {
    extend: {
      colors: {
        ink: {
          primary:  '#37352F',
          strong:   '#37352FCC',
          muted:    '#37352FA6',
          faint:    '#37352F99',
          divider:  '#37352F29',
          hairline: '#37352F17',
        },
        bg: {
          page: '#FFFFFF',
          soft: '#F7F7F5',
        },
        border: { base: '#E9E9E7' },
        link:   { DEFAULT: '#2383E2', alt: '#097FE8' },
        campaign: { navy: '#2537B1', yellow: '#FFB110', red: '#F64932' },
        callout: {
          gray: { text: '#787774', bg: '#F1F1EF' },
          blue: { text: '#337EA9', bg: '#E7F3F8' },
          green:{ text: '#448361', bg: '#EDF3EC' },
          red:  { text: '#D44C47', bg: '#FDEBEC' },
        },
      },
      fontFamily: {
        sans:  ['NotionInter', 'ui-sans-serif', '-apple-system', 'sans-serif'],
        serif: ['Lyon Text', 'Lyon-Text', 'Georgia', 'ui-serif', 'serif'],
        mono:  ['iA Writer Mono', 'iawriter-mono', 'Nitti', 'Menlo', 'monospace'],
      },
      fontWeight: { normal: '400', medium: '500', semi: '550', semibold: '600', bold: '700' },
      borderRadius: { xs: '3px', sm: '5px', md: '8px', lg: '12px', pill: '1000px' },
      boxShadow: {
        'level-100': '0px 3px 9px #00000008, 0px 0.7px 1.4625px rgba(0,0,0,0.015)',
        'level-200': '0px 4px 18px #0000000a, 0px 2.025px 7.84688px rgba(0,0,0,0.027), 0px 0.8px 2.925px #00000005, 0px 0.175px 1.04062px rgba(0,0,0,0.013)',
        'level-300': '0px 20px 50px #00000014, 0px 6px 16px #0000000a',
      },
    },
  },
};
```

---

## 16. DO / DON'T

### ✅ DO
- 본문 text는 **warm ink `#37352F`**. 알파 5단계 (`A6/99/29/17/CC`)로 text/muted/divider/hairline 구분.
- Warm off-white **`#F7F7F5`**를 sidebar/panel 배경으로. **`#F7F6F3`**도 **`#F5F5F5`**도 아니다.
- 폰트는 **`NotionInter` + `Lyon Text` + `iA Writer Mono`** 3-way 토글. `var(--rich-text-font-config-font-family)`로 블록별 동적 전환.
- **13단계 font-size 시스템** (`font-size-50` ~ `font-size-1000`) 그대로 사용.
- **Letter-spacing optical compensation** — 사이즈별 + weight별 미세 보정.
- 링크는 **`#2383E2`**. `#2EAADC` 아님.
- Shadow는 **3-level composite**. `shadow-level-200`은 4-layer stacking.
- Callout/tag는 **9색 팔레트** (gray/brown/orange/yellow/green/blue/purple/pink/red)에서 text/bg pair로.
- Radius는 **3px가 블록 기본**, 12px가 카드, 1000px이 pill.

### ❌ DON'T
- ❌ **Pure black `#000`** text 금지 → 반드시 warm ink `#37352F`.
- ❌ **Inter 단일** 폰트 금지 → `NotionInter` + Lyon Text (serif) + iA Writer Mono (mono) 3-way.
- ❌ **`#2EAADC`** 링크 블루 금지 → 실제는 `#2383E2` (tone 확연히 다름).
- ❌ **`#F7F6F3`** cool gray 금지 → warm `#F7F7F5`.
- ❌ **8pt 그리드** 가정 금지 → Notion은 20/24/32/40/60 혼합.
- ❌ "Notion is flat, no shadows" 가정 금지 → 실제는 **4-layer composite micro-shadow** (shadow-level-200).
- ❌ **6단계 type scale** 금지 → 13단계 필수.
- ❌ Letter-spacing 고정값 금지 → 사이즈별 optical 보정.
- ❌ Campaign 색 (`#2537B1` navy, `#FFB110` yellow 등)을 **영구 브랜드**로 착각 금지 — AI Agents 런칭 캠페인 overlay.
