---
slug: linear
service_name: Linear
site_url: https://linear.app
fetched_at: 2026-04-11
default_theme: dark
brand_color: "#4354B8"
primary_font: Inter Variable
font_weight_normal: 400
token_prefix: color
---

# DESIGN.md — Linear (Claude Code Edition)

---

## 01. Quick Start

> 5분 안에 Linear처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — Inter Variable + Berkeley Mono */
body {
  font-family: "Inter Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-weight: 400;
}
code, pre, kbd {
  font-family: "Berkeley Mono", ui-monospace, SFMono-Regular, "SF Mono", Consolas, monospace;
}

/* 2. 다크 배경 — 거의 순검정 */
:root {
  --color-bg-primary: #08090a;    /* 앱 UI */
  --color-bg-marketing: #010102;  /* 마케팅 (더 검다) */
  --color-text-primary: #f7f8f8;
  --color-text-secondary: #8a8f98;
}
body { background: var(--color-bg-marketing); color: var(--color-text-primary); }

/* 3. 브랜드 — marketing site의 진짜 indigo */
:root {
  --color-brand-marketing: #4354B8;  /* 124회 실사용 */
  --color-brand-app:       #5E6AD2;  /* 앱 UI 변수 */
}
```

**절대 하지 말아야 할 것 하나**: `#5E6AD2` 단일 값을 모든 곳에 쓰지 말 것. Linear는 **앱 UI**와 **마케팅 사이트**가 서로 다른 보라 팔레트를 쓴다. 마케팅 사이트에서는 **`#4354B8`** (훨씬 진한 indigo)이 실제로 124회 쓰이며, 앱 토큰 `--color-indigo: #5e6ad2`는 5회만 등장. 히어로 섹션이 Linear답게 보이려면 진한 `#4354B8`이 기본이어야 한다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://linear.app` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| Framework | Next.js marketing + vanilla-extract / Linaria CSS-in-JS |
| Custom props | 700+ (color: 109 · spacing: 107 · shadow: 7) |
| Token prefix | `--color-*`, `--font-size-*`, `--title-N-*`, `--border-*`, `--x{hash}` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 + CSS-in-JS 해시 변수 식별 |

---

## 03. Tech Stack

- **Framework**: Next.js marketing site
- **Design system**: 자체 토큰 시스템. **App UI**와 **marketing site**가 병렬 팔레트를 운용.
- **CSS architecture**: 하이브리드
  ```
  --color-*            정식 semantic 토큰 (109 color vars)
  --font-size-*        product UI 타이포 스케일 (micro ~ title3)
  --title-N-*          marketing 타이포 스케일 (title-1 ~ title-8)
  --x{hash} (var(--x13sdql6)) vanilla-extract / Linaria 컴파일 해시 변수
  ```
- **Class naming**: semantic + CSS-in-JS 해시 혼합. `class="_1xg8e0u0 _1xg8e0u1"` 같은 해시 클래스가 섞여 있음. 이 해시 부분은 재사용 불가 빌드 아티팩트.
- **Default theme**: **Dark** — marketing bg `#010102` (거의 완전 블랙), app bg `#08090a`
- **Font loading**: `Inter Variable` (body) + `Berkeley Mono` (code, 유료 U.S. Graphics Company 폰트)
- **Canonical anchor**: marketing brand `#4354B8` (indigo) · bg `#010102` / `#08090a`

---

## 04. Font Stack

- **Display / Body**: `Inter Variable` (variable font, non-표준 weight 100-900 전 범위)
- **Code / Mono**: **`Berkeley Mono`** (유료) — JetBrains Mono 아님
- **System fallback**: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`

```css
:root {
  --font-regular: "Inter Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --font-monospace: "Berkeley Mono", ui-monospace, SFMono-Regular, "SF Mono", Consolas, "Liberation Mono", Menlo, monospace;
}
body { font-family: var(--font-regular); font-weight: 400; }
code, pre, kbd { font-family: var(--font-monospace); }
```

> ⚠️ **Berkeley Mono는 유료 폰트**다. U.S. Graphics Company 제작. OSS 대체로는 **`JetBrains Mono`**, **`Commit Mono`**, **`Geist Mono`**가 있지만 x-height와 메트릭이 다르다. Inter Variable은 GitHub의 기본 variable 웹폰트와 동일 계열이지만 Linear는 variable weight `450/550` 같은 non-표준 값을 쓴다.

---

## 05. Typography Scale

Linear는 **두 개의 병렬 타이포 스케일**을 운용한다. Product UI용 (`--font-size-*`)과 marketing 대형 히어로용 (`--title-N-*`).

### Product UI scale

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `--font-size-micro`   | 0.75rem (12px)   | 400 | 1.4  | 0em     |
| `--font-size-mini`    | 0.8125rem (13px) | 400 | 1.4  | 0em     |
| `--font-size-small`   | 0.875rem (14px)  | 400 | 1.45 | 0em     |
| `--font-size-regular` | 1rem (16px)      | 400 | 1.5  | 0em     |
| `--font-size-large`   | 1.125rem (18px)  | 500 | 1.5  | -0.01em |
| `--font-size-title3`  | 1.25rem (20px)   | 550 | 1.3  | -0.012em|
| `--font-size-title2`  | 1.5rem (24px)    | 550 | 1.25 | -0.014em|
| `--font-size-title1`  | 2.25rem (36px)   | 600 | 1.15 | -0.018em|

### Marketing hero scale (`title-1` ~ `title-8`)

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `--title-1-size` | 1.0625rem (17px) | 500 | 1.45 | -0.011em |
| `--title-2-size` | 1.25rem (20px)   | 500 | 1.35 | -0.012em |
| `--title-3-size` | 1.5rem (24px)    | 550 | 1.25 | -0.014em |
| `--title-4-size` | 2rem (32px)      | 550 | 1.2  | -0.016em |
| `--title-5-size` | 2.5rem (40px)    | 600 | 1.15 | -0.018em |
| `--title-6-size` | 3rem (48px)      | 600 | 1.1  | -0.02em  |
| `--title-7-size` | 3.5rem (56px)    | 700 | 1.05 | -0.022em |
| `--title-8-size` | 4rem (64px)      | 700 | 1.0  | -0.022em |

> ⚠️ **Optical letter-spacing compensation** — 제목이 커질수록 tracking이 비례해서 타이트해진다 (-0.011em → -0.022em). 이 규칙 없으면 히어로 타이포가 헐렁해 보인다. Linear 시그너처 디테일.

---

## 06. Colors

### 06-1. Background — 7 tiers

| Token | Hex | Usage |
|---|---|---|
| `--color-bg-marketing`    | `#010102` | marketing 페이지 전용 (더 검게) |
| `--color-bg-primary`      | `#08090a` | 앱 메인 bg |
| `--color-bg-panel`        | `#0f1011` | panel 레이어 |
| `--color-bg-secondary`    | `#1c1c1f` | 카드 |
| `--color-bg-tertiary`     | `#232326` | 호버 상태 |
| `--color-bg-quaternary`   | `#28282c` | 선택 상태 |
| `--color-bg-quinary`      | `#282828` | 강조 |
| `--color-bg-translucent`  | `rgba(255,255,255,0.05)` | 반투명 오버레이 |

### 06-2. Text — on dark

| Token | Hex |
|---|---|
| `--color-text-primary`    | `#f7f8f8` |
| `--color-text-secondary`  | `#E2E4E7` |
| `--color-text-tertiary`   | `#E4E5E9` |
| `--color-text-muted`      | `#8A8F98` |
| `--color-text-faint`      | `#62666D` |

### 06-3. Brand — Marketing vs App

| Token | Hex | Usage |
|---|---|---|
| `--color-brand-marketing` | `#4354B8` | **실제 marketing site 보라** (124회) |
| `--color-brand-soft`      | `#8FA4FF` | 밝은 보조 |
| `--color-indigo` (app)    | `#5E6AD2` | 앱 UI 토큰 (변수만 존재) |

### 06-4. Named Palette (app priority / team colors)

| Token | Hex |
|---|---|
| `--color-white`   | `#ffffff` |
| `--color-black`   | `#000000` |
| `--color-blue`    | `#4ea7fc` |
| `--color-red`     | `#eb5757` |
| `--color-green`   | `#27a644` |
| `--color-orange`  | `#fc7840` |
| `--color-yellow`  | `#f0bf00` |
| `--color-indigo`  | `#5e6ad2` |
| `--color-teal`    | `#00b8cc` |

### 06-5. Linear Tier Colors (product modes)

| Token | Hex | Mode |
|---|---|---|
| `--color-linear-plan`     | `#68cc58` | Plan |
| `--color-linear-build`    | `#d4b144` | Build |
| `--color-linear-security` | `#7a7fad` | Security |

### 06-6. Pastel Highlight Palette (marketing feature sections)

| Token | Hex | Usage |
|---|---|---|
| highlight-pink   | `#F79CE0` | feature badge (51회) |
| highlight-cyan   | `#55CDFF` | feature badge (25회) |
| highlight-green  | `#89D196` | feature badge |
| highlight-peach  | `#FFC47C` | feature badge |
| highlight-teal   | `#02B8CC` | feature badge |
| highlight-purple | `#8FA4FF` | feature badge |
| highlight-orange | `#E5591D` | urgent/priority (76회 실사용) |

### 06-7. Border — 4 tiers

| Token | Hex |
|---|---|
| `--border-solid`      | `#2a2e33` |
| `--border-thin`       | `#24282c` |
| `--border-faint-thin` | `#191d21` |
| `--border-frame`      | `#151616` |
| `--color-border-primary` | `#23252a` |

### 06-8. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#08090A` | 324 | bg-primary (앱 bg) |
| 2 | `#E4E5E9` | 200 | text-tertiary |
| 3 | `#E2E4E7` | 151 | text-secondary |
| 4 | `#4354B8` | 124 | **marketing brand** |
| 5 | `#E5591D` |  76 | orange accent / priority |
| 6 | `#FFFFFF` |  75 | pure white |
| 7 | `#8A8F98` |  71 | text-muted |
| 8 | `#F79CE0` |  51 | pink highlight |
| 9 | `#2E2E32` |  43 | card surface |
| 10| `#62666D` |  35 | text-faint |
| 11| `#55CDFF` |  25 | cyan highlight |
| 12| `#000000` |  25 | pure black |

---

## 07. Spacing

Linear는 **107개 spacing 변수**를 운용. Marketing page-level과 product UI-level로 나뉜다.

### Marketing page spacing

| Token | Value | Use case |
|---|---|---|
| `--page-padding-inline`      | 24px  | 페이지 좌우 패딩 |
| `--page-padding-block`       | 64px  | 페이지 상하 패딩 |
| `--homepage-outer-padding`   | 46px  | 홈 최외곽 |
| `--homepage-padding-inset`   | 32px  | 홈 내부 |
| `--frame-padding`            | 8px   | 프레임 장식 |
| `--min-tap-size`             | 44px  | 터치 영역 최소 |
| marketing-section-pad-bottom | 112px | 섹션 하단 |

### Product UI spacing

| Token | Value | Use case |
|---|---|---|
| space-1 | 4px   | micro |
| space-2 | 8px   | tight |
| space-3 | 12px  | default gap |
| space-4 | 16px  | padding |
| space-5 | 24px  | card |
| space-6 | 32px  | section inner |
| space-7 | 48px  | block gap |

---

## 08. Radius

Linear는 **20개의 고유 radius 값**을 사용한다.

| Token | Value | Context |
|---|---|---|
| radius-1  | 2px  | inline chip |
| radius-2  | 3px  | micro |
| radius-3  | 4px  | small button (45회 — 최빈) |
| radius-4  | 5px  | — |
| radius-5  | 6px  | input |
| radius-6  | 8px  | button, card (43회) |
| radius-7  | 9px  | — |
| radius-8  | 12px | card (30회) |
| radius-9  | 16px | large card |
| radius-10 | 30px | modal/hero card |
| radius-pill | 9999px | avatar, tag |

---

## 09. Shadows

> **철학**: Linear는 **의도적으로 drop shadow를 최소화**한다. `--shadow-low/medium/high`가 실제로는 `shadow-none`으로 alias 되어 있으며, elevation은 **border + 반투명 배경 + 5-layer 미세 stacking**으로 표현한다.

| Token | Value | Usage |
|---|---|---|
| `--shadow-stack-low` | 5-layer 복합 (아래 참고) | 카드 elevation |
| `--shadow-low`       | `none` (alias) | — |
| `--shadow-medium`    | `none` (alias) | — |
| `--shadow-high`      | `none` (alias) | — |

```css
--shadow-stack-low:
  0px 8px 2px 0px rgba(0,0,0,0),
  0px 5px 2px 0px rgba(0,0,0,0.01),
  0px 3px 2px 0px rgba(0,0,0,0.04),
  0px 1px 1px 0px rgba(0,0,0,0.07),
  0px 0px 1px 0px rgba(0,0,0,0.08);
```

> ⚠️ 단일 `box-shadow: 0 4px 16px rgba(0,0,0,0.4)` 같은 거친 drop shadow는 Linear 철학에 반한다. 반드시 5-layer 미세 stacking을 쓰거나, 아예 shadow 없이 border + `rgba(255,255,255,0.05)` 반투명 배경으로 elevation을 표현.

---

## 11. Layout Patterns

### Marketing Hero
- Background: `#010102` (거의 완전 블랙)
- H1: `title-7` ~ `title-8` (56-64px) / weight 700 / tracking -0.022em
- Brand accent: `#4354B8` pixel art 오브 / gradient
- Max-width: 1280px, padding `46px`

### App Shell
- bg: `#08090a`
- Sidebar: `#0f1011`
- Issue row: 12-15px 텍스트, 32-40px high, tight vertical rhythm
- Command palette: `#1c1c1f` + 5-layer shadow-stack-low

```css
.marketing-section { padding: 64px 46px; max-width: 1280px; margin-inline: auto; background: #010102; }
.app-shell { background: #08090a; color: #f7f8f8; }
.sidebar { background: #0f1011; border-right: 1px solid #2a2e33; }
```

---

## 12. Components

### 12.1 Primary CTA (Indigo)

```html
<a class="button button--primary">Start building</a>
```

| Spec | Value |
|---|---|
| Background | `#4354B8` (marketing) or `#5E6AD2` (app) |
| Text | `#ffffff` |
| Padding | `8px 18px` |
| Radius | `6px` |
| Font weight | 500 |

### 12.2 Ghost Button

| Spec | Value |
|---|---|
| Background | `rgba(255,255,255,0.05)` (translucent) |
| Border | `1px solid #2a2e33` |
| Text | `#f7f8f8` |
| Hover | bg `rgba(255,255,255,0.08)` |

### 12.3 Issue Row (app pattern)

```html
<div class="issue-row">
  <span class="issue-row__priority" style="color:#E5591D"></span>
  <span class="issue-row__id">LIN-1234</span>
  <span class="issue-row__title">Fix keyboard nav</span>
  <span class="issue-row__status">In Progress</span>
</div>
```

| Spec | Value |
|---|---|
| Padding | `8px 16px` |
| Font size | 13-14px |
| Hover bg | `#232326` |
| Border-bottom | `1px solid #191d21` (faint-thin) |

### 12.4 Feature Badge (pastel)

```html
<span class="badge badge--pink">Pulse</span>
```

Pastel palette: `#F79CE0` / `#55CDFF` / `#89D196` / `#FFC47C`를 각 feature에 할당.

### 12.5 Command Palette

- Modal center
- Background: `#1c1c1f`
- Border: `1px solid #2a2e33`
- Shadow: `--shadow-stack-low`
- `⌘K` keyboard hint in Berkeley Mono

---

## 14. Drop-in CSS

```css
/* Linear — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-regular:   "Inter Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-monospace: "Berkeley Mono", ui-monospace, SFMono-Regular, "SF Mono", monospace;

  /* Background tiers */
  --color-bg-marketing:  #010102;
  --color-bg-primary:    #08090a;
  --color-bg-panel:      #0f1011;
  --color-bg-secondary:  #1c1c1f;
  --color-bg-tertiary:   #232326;
  --color-bg-quaternary: #28282c;
  --color-bg-translucent: rgba(255,255,255,0.05);

  /* Text */
  --color-text-primary:   #f7f8f8;
  --color-text-secondary: #E2E4E7;
  --color-text-muted:     #8A8F98;
  --color-text-faint:     #62666D;

  /* Brand */
  --color-brand-marketing: #4354B8;
  --color-brand-app:       #5E6AD2;
  --color-brand-soft:      #8FA4FF;

  /* Pastel highlights */
  --highlight-pink:   #F79CE0;
  --highlight-cyan:   #55CDFF;
  --highlight-green:  #89D196;
  --highlight-peach:  #FFC47C;
  --highlight-teal:   #02B8CC;
  --highlight-orange: #E5591D;

  /* Semantic */
  --color-red:    #eb5757;
  --color-green:  #27a644;
  --color-orange: #fc7840;
  --color-yellow: #f0bf00;

  /* Border */
  --border-solid:      #2a2e33;
  --border-thin:       #24282c;
  --border-faint-thin: #191d21;
  --border-frame:      #151616;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
  --radius-xl: 12px;
  --radius-pill: 9999px;

  /* Shadow (5-layer stacking) */
  --shadow-stack-low:
    0px 8px 2px 0px rgba(0,0,0,0),
    0px 5px 2px 0px rgba(0,0,0,0.01),
    0px 3px 2px 0px rgba(0,0,0,0.04),
    0px 1px 1px 0px rgba(0,0,0,0.07),
    0px 0px 1px 0px rgba(0,0,0,0.08);

  /* Spacing */
  --page-padding-inline: 24px;
  --page-padding-block:  64px;
}

body {
  background: var(--color-bg-marketing);
  color: var(--color-text-primary);
  font-family: var(--font-regular);
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
}
code, pre, kbd { font-family: var(--font-monospace); }
```

---

## 15. Tailwind Config

```js
// tailwind.config.js — Linear
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        bg: {
          marketing: '#010102',
          primary:   '#08090a',
          panel:     '#0f1011',
          secondary: '#1c1c1f',
          tertiary:  '#232326',
          quaternary:'#28282c',
        },
        text: {
          primary:   '#f7f8f8',
          secondary: '#E2E4E7',
          muted:     '#8A8F98',
          faint:     '#62666D',
        },
        brand: {
          marketing: '#4354B8',
          app:       '#5E6AD2',
          soft:      '#8FA4FF',
        },
        highlight: {
          pink:   '#F79CE0',
          cyan:   '#55CDFF',
          green:  '#89D196',
          peach:  '#FFC47C',
          teal:   '#02B8CC',
          orange: '#E5591D',
        },
        border: {
          solid: '#2a2e33', thin: '#24282c', 'faint-thin': '#191d21', frame: '#151616',
        },
      },
      fontFamily: {
        sans: ['Inter Variable', '-apple-system', 'sans-serif'],
        mono: ['Berkeley Mono', 'ui-monospace', 'SF Mono', 'monospace'],
      },
      fontWeight: { normal: '400', 'semi': '550', semibold: '600', bold: '700' },
      borderRadius: { sm: '4px', md: '6px', lg: '8px', xl: '12px', pill: '9999px' },
      boxShadow: {
        'stack-low': '0px 8px 2px 0px rgba(0,0,0,0), 0px 5px 2px 0px rgba(0,0,0,0.01), 0px 3px 2px 0px rgba(0,0,0,0.04), 0px 1px 1px 0px rgba(0,0,0,0.07), 0px 0px 1px 0px rgba(0,0,0,0.08)',
      },
    },
  },
};
```

---

## 16. DO / DON'T

### ✅ DO
- 브랜드 보라를 **marketing vs app**으로 분리. marketing은 `#4354B8`, app은 `#5E6AD2`.
- 다크 배경은 **7-tier** (`marketing/primary/panel/secondary/tertiary/quaternary/quinary`). 단일 bg 금지.
- **Berkeley Mono** (유료)가 진짜 코드 폰트. OSS 대체시 JetBrains/Commit/Geist Mono.
- Pastel highlight quartet (`#F79CE0/#55CDFF/#89D196/#FFC47C`)을 feature badge에 할당.
- 타이포는 **product (`--font-size-*`) + marketing (`--title-N-*`)** 병렬 스케일. marketing 히어로는 56-64px.
- Letter-spacing **optical compensation** (-0.011em ~ -0.022em). 제목이 커질수록 타이트.
- Shadow는 **5-layer 미세 stacking**만. 거친 drop shadow 금지.
- Border 4단계 (`solid/thin/faint-thin/frame`)로 카드 hierarchy 표현.
- `#4354B8`(indigo) + `#E5591D`(orange)를 primary + accent pair로.

### ❌ DON'T
- ❌ `#5E6AD2` 단일 값을 marketing hero에 쓰지 말 것 → 실제는 `#4354B8` (124회 vs 5회).
- ❌ **JetBrains Mono**를 Linear 코드 폰트로 쓰지 말 것 → 실제는 Berkeley Mono.
- ❌ **`#171723`** 같은 푸른 기 다크 bg 쓰지 말 것 → Linear는 `#08090a` / `#010102` (거의 완전 블랙).
- ❌ 단일 `box-shadow: 0 4px 16px rgba(0,0,0,0.4)` 금지 → 5-layer stacking 또는 shadow 없음.
- ❌ `#F2994A` orange 쓰지 말 것 → 실제는 `#E5591D` (훨씬 진함, 76회).
- ❌ 배경 단일 톤 금지 → 7-tier 배경 시스템 필수.
- ❌ Pastel highlight 팔레트 무시 금지 → marketing feature section의 색채감이 증발한다.
- ❌ Title 스케일을 `24/32/48`로만 구성하지 말 것 → marketing은 `17/20/24/32/40/48/56/64px` 8단계.
- ❌ Letter-spacing을 고정값 (-0.01em) 금지 → 사이즈별 optical compensation 필수.
