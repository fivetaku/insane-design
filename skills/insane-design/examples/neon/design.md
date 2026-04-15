---
slug: neon
service_name: Neon
site_url: https://neon.com
fetched_at: 2026-04-11
default_theme: dark
brand_color: "#00E599"
primary_font: Inter
font_weight_normal: 400
token_prefix: color
---

# DESIGN.md — Neon (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Neon의 웹사이트는 깊은 다크 배경(`#0A0A0A`) 위에 네온 그린 `#00E599`의 글로우 이펙트가 돋보이는 디자인이다. 서버리스 Postgres로서의 기술적 정교함을 미래적이고 세련된 시각 언어로 표현한다.

타이포그래피는 기본 시스템 서체를 사용한다. 본문 weight는 **400**이며, 코드 블록과 기술 문서에 모노스페이스 서체가 적극 활용된다.

브랜드 그린 `#00E599`는 네온 글로우 이펙트의 중심 컬러로, CTA 버튼과 주요 accent에 사용된다. 다크 배경에서 발광하는 듯한 시각적 효과가 Neon의 이름과 정체성을 직접적으로 연결한다.

**Key Characteristics:**
- 브랜드 네온 그린 **#00E599** + hover **#34D59A**. 연한 tint **#E4F1EB**.
- **다크 캔버스 #0C0D0D** + surface 9-tier (`#131415` → `#494B50`).
- Mono 폰트는 **GeistMono** (Vercel OSS), via `var(--font-geist-mono)`.
- Inter는 `var(--font-inter)` + **Inter Fallback** metric fallback.
- **Radius 38-40px pill** 스타일. 일반 `rounded-md` 대신 `rounded-[38px]`.
---

## 01. Quick Start

> 5분 안에 Neon처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — Inter + GeistMono, next/font 변수 */
body {
  font-family: var(--font-inter), "Inter", "Inter Fallback", ui-sans-serif, system-ui, sans-serif;
  font-weight: 400;
}
code, pre {
  font-family: var(--font-geist-mono), GeistMono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}

/* 2. 다크 캔버스 */
:root {
  --bg-canvas: #0C0D0D;
  --surface-1: #131415;
  --surface-2: #18191B;
  --surface-3: #242628;
  --surface-4: #303236;
  --border:    #494B50;
  --text:      #FFFFFF;
  --text-muted:#AFB1B6;
}
body { background: var(--bg-canvas); color: var(--text); }

/* 3. 브랜드 네온 그린 */
:root {
  --brand:       #00E599;
  --brand-hover: #34D59A;
  --brand-tint:  #E4F1EB;
  --decor-deep:  #2C6D4C;
}
```

**절대 하지 말아야 할 것 하나**: "Flat, no gradients" 원칙을 따르지 말 것. 실제 Neon 사이트는 `#2C6D4C` (짙은 네온 그린)이 **3,602회** 반복되는 decorative SVG pattern/gradient로 hero와 섹션 배경을 채운다. halftone/gradient 텍스처는 Neon 브랜드의 핵심 시그너처다. 완전 평평한 다크 UI로 만들면 Neon 느낌이 안 난다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://neon.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| Framework | Next.js (App Router) + **Tailwind CSS v4** + Shiki |
| Custom props | 189 (color: 11 · spacing: 6 · shadow: 17 · radius: 10 unique) |
| Token prefix | `--tw-*`, `--font-*`, `--spacing`, `shiki-color-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 + SVG pattern 빈도 분석 |

---

## 03. Tech Stack

- **Framework**: Next.js App Router + `next/font/google` (`var(--font-inter)`, `var(--font-geist-mono)`)
- **Design system**: Tailwind CSS v4 기본 팔레트 + 최소 브랜드 덮기 (색 변수 11개)
- **CSS architecture**:
  ```
  Tailwind v4 @theme              --color-*-{50..950} 팔레트
  --spacing: 0.25rem              v4 단일 base spacing
  --tw-prose-*                    Tailwind Typography 플러그인
  shiki-color-text: #131415       Shiki 코드 하이라이터 (VSCode dark+)
  ```
- **Class naming**: 순수 Tailwind 유틸리티. 특히 arbitrary values (`rounded-[38px]`, `bg-[#00E599]`)가 많음.
- **Default theme**: **Dark** (bg `#0C0D0D`, text `#FFFFFF`)
- **Font loading**: `next/font/google`로 Inter + GeistMono + metric fallback (`Inter Fallback`, `GeistMono Fallback`)
- **Legacy artifact**: 일부 섹션에 `IBM Plex Sans` 폰트가 남아있음 — 과거 Neon 브랜드의 흔적, 현재는 Inter로 리브랜드 중.
- **Canonical anchor**: brand `#00E599` · canvas `#0C0D0D` · decorative `#2C6D4C`

---

## 04. Font Stack

- **Display / Body**: `Inter` (via `var(--font-inter)`)
- **Code / Mono**: **`GeistMono`** (Vercel OSS)
- **Legacy**: `IBM Plex Sans` — 리브랜드 과도기, 일부 페이지에 잔존
- **Metric fallback**: `Inter Fallback`, `IBM Plex Sans Fallback` — 웹폰트 로딩 시 layout shift 방지

```css
:root {
  --font-inter:      "Inter", "Inter Fallback", ui-sans-serif, system-ui, sans-serif;
  --font-geist-mono: "GeistMono", ui-monospace, SFMono-Regular, "SF Mono", Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}
body      { font-family: var(--font-inter); font-weight: 400; }
code, pre { font-family: var(--font-geist-mono); }
```

> ⚠️ Mono 폰트는 **JetBrains Mono가 아니라 GeistMono**. Vercel 생태계에서 밀고 있는 OSS 등가물. x-height와 metric이 JetBrains와 다르므로 교체 시 코드 블록 느낌이 바뀐다.

---

## 05. Typography Scale

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| hero-mega     | 72px / 4rem  | 700 | 1.0  | -0.025em |
| hero-display  | 48px / 3rem  | 700 | 1.05 | -0.02em  |
| h1            | 36px         | 600 | 1.15 | -0.018em |
| h2            | 28px         | 600 | 1.2  | -0.014em |
| h3            | 1.5rem (24px)| 600 | 1.25 | -0.012em |
| h4            | 1.25rem (20px)| 600 | 1.3 | -0.01em  |
| body-lg       | 1.125rem (18px)| 500| 1.55 | 0em     |
| body          | 1rem (16px)  | 400 | 1.55 | 0em      |
| body-sm       | .875rem (14px)| 400| 1.5  | 0em      |

> ⚠️ Weight 분포: 500/600이 지배적. DB 관리 플랫폼의 정보 밀도에 맞춰 body는 500 semibold를 기본 강조로 쓴다. 히어로만 700.

---

## 06. Colors

### 06-1. Brand

| Token | Hex | Usage |
|---|---|---|
| brand-primary   | `#00E599` | 네온 그린 CTA (45회) |
| brand-hover     | `#34D59A` | hover / active (14회) |
| brand-tint      | `#E4F1EB` | 연한 민트 배경 (12회) |
| **decor-deep**  | `#2C6D4C` | **halftone/SVG pattern green (3,602회)** |

### 06-2. Dark Surface (9 tiers)

| Token | Hex |
|---|---|
| bg-canvas  | `#0C0D0D` |
| surface-0  | `#131415` (shiki bg) |
| surface-1  | `#18191B` |
| surface-2  | `#1A1A1A` |
| surface-3  | `#242628` |
| surface-4  | `#303236` |
| surface-5  | `#494B50` (border-strong) |
| inset-overlay | `#1c1d1e` (massive `inset 0 0 0 1000px` trick) |
| pure-black | `#000000` |

### 06-3. Text (onDark)

| Token | Hex |
|---|---|
| text-max      | `#FFFFFF` |
| text-high     | `#C9CBCF` |
| text-muted    | `#AFB1B6` |
| text-secondary| `#94979E` |
| text-faint    | `#494B50` |

### 06-4. Semantic

| Token | Hex | Usage |
|---|---|---|
| success  | `#00E599` | CTA / success state |
| warning  | — (Tailwind yellow-500) | 경고 |
| danger   | (Tailwind red-500) | error |
| info     | (Tailwind blue-400) | info |

### 06-5. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#2C6D4C` | 3602 | **decorative SVG pattern** |
| 2 | `#FFFFFF` |  189 | text onDark |
| 3 | `#00000000` |  87 | transparent |
| 4 | `#94979E` |  65 | muted text |
| 5 | `#000000` |  63 | pure black |
| 6 | `#00E599` |  45 | **brand neon green** |
| 7 | `#303236` |  40 | card surface |
| 8 | `#242628` |  38 | deeper surface |
| 9 | `#494B50` |  35 | border |
| 10| `#AFB1B6` |  31 | muted 2 |
| 11| `#C9CBCF` |  31 | text high |
| 12| `#0C0D0D` |  29 | canvas bg |

> **Outlier 경고**: `#2C6D4C`의 3,602회는 SVG `<pattern>` fill 또는 globally 반복되는 gradient stop. dominant로 쓰되 **전경 text로는 사용하지 말 것**. decorative 전용.

> **Customer logo 오염**: `#FF3621` (Databricks red, 16회), `#0055FF` (vendor blue, 10회)는 logo wall SVG 색. Neon 브랜드 아님.

---

## 07. Spacing

Tailwind v4 단일 base (`--spacing: 0.25rem`) + 6개 수동 변수.

| Token | Value | Use case |
|---|---|---|
| `--spacing`       | 4px   | base |
| p-2 | 8px  | tight |
| p-3 | 12px | inline |
| p-4 | 16px | card inner |
| p-6 | 24px | section inner |
| p-8 | 32px | block gap |
| `gap-20` (5rem)   | 80px  | major gap |
| `viewport-padding`| 25px  | page outer |
| p-12 | 48px | section gap |
| p-20 | 80px | hero padding |

---

## 08. Radius

Neon은 **sharp 4-8px가 아니라 soft 38-40px** 스타일. editorial/rounded 분위기.

| Token | Value | Context |
|---|---|---|
| radius-xs | 1-2px  | divider |
| radius-sm | 10px   | small button (3회) |
| radius-md | 11px   | — |
| radius-lg | 14px   | card (2회) |
| radius-xl | 33px   | large card |
| **radius-pill** | **38px** | **기본 pill button (6회 — 최빈)** |
| radius-pill-alt | 40px | alternative pill (3회) |
| radius-hero | 50px   | hero block |
| radius-blob | 60-80px | decorative blob |

> ⚠️ Neon은 `rounded-[38px]` / `rounded-[40px]`로 soft pill을 만든다. 일반적인 `rounded-md (6px)`로는 안 된다.

---

## 09. Shadows

| Token | Value | Usage |
|---|---|---|
| tw-shadow-sm | `0 1px 2px 0 #0000000d` | subtle |
| tw-shadow-md | `0 4px 6px -1px #0000001a, 0 2px 4px -2px #0000001a` | card |
| tw-shadow-lg | `0 10px 15px -3px #0000001a, 0 4px 6px -4px #0000001a` | popover |
| massive-inset | `inset 0 0 0 1000px #1c1d1e` | **반투명 오버레이 트릭** (3회) |
| prose-kbd-shadows | `0 0 0 1px #1018281a, 0 3px 0 #1018281a` | keyboard key |

> **철학**: Neon의 "glowing" 느낌은 shadow에서 오지 않는다. **saturated `#00E599` + deep `#0C0D0D` 대비**에서 나온다. Drop shadow는 거의 사용하지 않음.

---

## 11. Layout Patterns

### Hero
- Background: `#0C0D0D` + `#2C6D4C` SVG halftone 패턴 오버레이
- H1: 48-72px / weight 700 / tracking -0.025em
- CTA: `#00E599` fill + `#0C0D0D` text, radius 38px

### Section Rhythm
```css
section {
  padding: 80px 25px;
  max-width: 1280px;
  margin-inline: auto;
}
.hero {
  background: #0C0D0D url('/patterns/halftone.svg') center/cover;
}
```

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Breakpoint | Width | Key Changes |
|---|---|---|
| Mobile | <640px | 단일 컬럼, 헤딩 축소, 카드 스택 |
| Tablet | 640-1024px | 2열 그리드, 중간 패딩 |
| Desktop | 1024-1280px | 풀 레이아웃, 3열 그리드 |
| Large | >1280px | 중앙 정렬 max-width 1280px, 넉넉한 마진 |

> ⚠️ Neon는 모바일 퍼스트 반응형 디자인을 채택하며, 브레이크포인트별로 그리드와 타이포그래피가 유동적으로 조정된다.

---

## 13. Components

### 12.1 Primary CTA (Neon Green Pill)

```html
<a class="btn-primary">Sign up free</a>
```

| Spec | Value |
|---|---|
| Background | `#00E599` |
| Hover | `#34D59A` |
| Text | `#0C0D0D` (**짙은 배경 텍스트**) |
| Padding | `16px 32px` |
| Radius | `38px` (**pill**) |
| Font weight | 500 |

### 12.2 Secondary Button (Outline)

```html
<a class="btn-secondary">Read docs</a>
```

| Spec | Value |
|---|---|
| Background | transparent |
| Border | `1px solid #494B50` |
| Text | `#FFFFFF` |
| Radius | `38px` |

### 12.3 Card

```html
<div class="card">
  <h3>Branching</h3>
  <p>Database branches in milliseconds.</p>
</div>
```

| Spec | Value |
|---|---|
| Background | `#18191B` (surface-1) |
| Border | `1px solid #303236` |
| Radius | `14px` |
| Padding | `32px` |

### 12.4 Code Block (Shiki VSCode dark+)

```html
<pre class="shiki"><code>SELECT * FROM users;</code></pre>
```

| Spec | Value |
|---|---|
| Background | `#131415` (`shiki-color-text`) |
| Text | shiki syntax colors |
| Padding | `20px 24px` |
| Radius | `10px` |
| Font | `var(--font-geist-mono)` |

---

## 15. Drop-in CSS

```css
/* Neon — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-inter:      "Inter", "Inter Fallback", ui-sans-serif, system-ui, sans-serif;
  --font-geist-mono: "GeistMono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;

  /* Brand */
  --color-brand:       #00E599;
  --color-brand-hover: #34D59A;
  --color-brand-tint:  #E4F1EB;
  --color-decor-deep:  #2C6D4C;

  /* Surface */
  --color-bg-canvas:  #0C0D0D;
  --color-surface-0:  #131415;
  --color-surface-1:  #18191B;
  --color-surface-2:  #242628;
  --color-surface-3:  #303236;
  --color-border:     #494B50;

  /* Text */
  --color-text-max:       #FFFFFF;
  --color-text-high:      #C9CBCF;
  --color-text-muted:     #AFB1B6;
  --color-text-secondary: #94979E;

  /* Tailwind v4 base */
  --spacing: 0.25rem;

  /* Radius — soft pill */
  --radius-sm:   10px;
  --radius-md:   14px;
  --radius-lg:   33px;
  --radius-pill: 38px;

  /* Shiki */
  --shiki-color-text: #131415;
}

body {
  background: var(--color-bg-canvas);
  color: var(--color-text-max);
  font-family: var(--font-inter);
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
}

code, pre { font-family: var(--font-geist-mono); }

.btn-primary {
  background: var(--color-brand);
  color: var(--color-bg-canvas);
  padding: 16px 32px;
  border-radius: var(--radius-pill);
  font-weight: 500;
}
.btn-primary:hover { background: var(--color-brand-hover); }
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Neon (Tailwind v4)
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#00E599',
          hover:   '#34D59A',
          tint:    '#E4F1EB',
          decor:   '#2C6D4C',
        },
        bg: {
          canvas: '#0C0D0D',
          'surface-0': '#131415',
          'surface-1': '#18191B',
          'surface-2': '#242628',
          'surface-3': '#303236',
        },
        text: {
          max:       '#FFFFFF',
          high:      '#C9CBCF',
          muted:     '#AFB1B6',
          secondary: '#94979E',
        },
        border: { DEFAULT: '#494B50' },
      },
      fontFamily: {
        sans: ['var(--font-inter)', 'Inter', 'Inter Fallback', 'ui-sans-serif', 'sans-serif'],
        mono: ['var(--font-geist-mono)', 'GeistMono', 'ui-monospace', 'SFMono-Regular', 'monospace'],
      },
      borderRadius: {
        sm: '10px', md: '14px', lg: '33px', pill: '38px', 'pill-alt': '40px',
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference
| Role | Hex |
|---|---|
| Primary CTA | `#00E599` |
| Heading text | `#FFFFFF` |
| Body text | `#A0AEC0` |
| Background | `#0A0A0A` |
| Border | `#1F2937` |
| Link | `#00E599` |
| Dark section | `#0A0A0A` |

### Example Component Prompts
- "Create a hero section on `#0A0A0A` background. Headline at 3.5rem `Inter` weight 400. CTA button `#00E599` with white text."
- "Design a card: `#FFFFFF` background, `#1F2937` border, 12px radius. Body text `#A0AEC0` at weight 400."

### Iteration Guide
1. 폰트: `Inter` 패밀리, 본문 weight 400
2. 컬러: 브랜드 `#00E599`는 CTA/링크에만 집중. 배경 `#0A0A0A`, 텍스트 `#FFFFFF`
3. 그림자: neon 글로우 이펙트 + subtle box-shadow
---

## 18. DO / DON'T

### ✅ DO
- 브랜드 네온 그린 **#00E599** + hover **#34D59A**. 연한 tint **#E4F1EB**.
- **다크 캔버스 #0C0D0D** + surface 9-tier (`#131415` → `#494B50`).
- Mono 폰트는 **GeistMono** (Vercel OSS), via `var(--font-geist-mono)`.
- Inter는 `var(--font-inter)` + **Inter Fallback** metric fallback.
- **Radius 38-40px pill** 스타일. 일반 `rounded-md` 대신 `rounded-[38px]`.
- CTA 텍스트는 **`#0C0D0D`** (다크 색) — 네온 그린 위에 흰색이 아닌 검정 텍스트.
- **Decorative `#2C6D4C` halftone** gradient를 hero 배경으로. Neon 시그너처.
- Shiki로 코드 블록 하이라이팅 (`--shiki-color-text: #131415`).

### ❌ DON'T
- ❌ **JetBrains Mono** 금지 → **GeistMono**.
- ❌ **"No gradients" 원칙** 따르지 말 것 → 실제는 `#2C6D4C` halftone이 3,602회.
- ❌ **Sharp 4-8px radius** 금지 → soft 38-40px pill이 기본.
- ❌ **CTA 텍스트 색을 흰색**으로 하지 말 것 → 네온 그린 배경 위에는 `#0C0D0D` 다크 텍스트.
- ❌ `#FF3621` (Databricks) / `#0055FF` 같은 **customer logo hex**를 브랜드로 착각 금지.
- ❌ **Pure black #000** canvas 금지 → `#0C0D0D` (살짝 탁한 블랙).
- ❌ Display weight 700을 **본문에도** 적용 금지 → 본문은 500/600.
- ❌ IBM Plex Sans를 **주 폰트**로 쓰지 말 것 → 레거시 잔존, Inter가 현재 주.

---

