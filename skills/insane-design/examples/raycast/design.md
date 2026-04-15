---
slug: raycast
service_name: Raycast
site_url: https://raycast.com
fetched_at: 2026-04-11
default_theme: dark
brand_color: "#FF6363"
primary_font: Inter
font_weight_normal: 400
token_prefix: ""
---

# DESIGN.md — Raycast (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Raycast의 웹사이트는 순수 블랙 `#000000` 배경의 다크 퍼스트 디자인이다. macOS 네이티브 앱의 고급스러운 느낌을 웹으로 옮기면서, 개발자 생산성 도구로서의 정밀함과 속도감을 시각적으로 전달한다.

타이포그래피는 기본 시스템 서체를 활용한다. 본문 weight는 **400**이며, 깔끔하고 기능적인 텍스트 스타일이 도구의 효율성을 반영한다.

브랜드 레드-코랄 `#FF6363`은 CTA와 핵심 accent에 사용된다. 순수 블랙 배경 위에서 빛나는 듯한 시각적 효과를 만들며, 그래디언트 accent가 다크 인터페이스에 생동감을 부여한다.

**Key Characteristics:**
- Body weight = **500**. 400 아님. Raycast의 또렷한 텍스트는 여기서 나온다.
- Brand = **`#FF6363`** (`hsl(0,100%,69%)`). CTA/feature highlight에 공격적 사용.
- `Inter` + `Inter Fallback` 메트릭 매치 쌍을 `next/font`로 로드.
- `--grey-900 = #07080a`가 page background. 순검정 아님.
- Body 크기 = **14px**, 코드는 **GeistMono**로 렌더.
---

## 01. Quick Start

> 5분 안에 Raycast처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Inter + Geist Mono (Next.js font loader 스타일) */
body {
  font-family: "Inter", "Inter Fallback",
               -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 500;  /* Raycast 본문 weight는 500이 주류 */
}

/* 2. 딥 그레이 다크 배경 + 밝은 포그라운드 */
:root {
  --background: #07080a;   /* grey-900 */
  --foreground: hsl(240,11%,96%);
}
body { background: var(--background); color: var(--foreground); }

/* 3. Raycast Red (브랜드 시그니처) */
:root { --color-red: hsl(0,100%,69%); /* #FF6363 */ }
```

**절대 하지 말아야 할 것 하나**: Raycast 본문 weight를 400으로 두지 말 것. 실제 CSS에서 `font-weight: 500`이 **211회** 등장해서 가장 많다. 400(53)보다 4배다. Raycast 특유의 또렷하고 컴팩트한 텍스트 느낌은 500이 기본이기 때문이다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://raycast.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 367,727 bytes (Next.js SSR) |
| CSS files | 12개, 총 407,009자 |
| Custom props | 147 고유 `--*` 변수 (매우 컴팩트) |
| `@font-face` | 16 (Inter · Inter Fallback · GeistMono · JetBrains Mono) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js + `next/font` (Geist Mono는 Vercel 패밀리)
- **Design system**: 자체 미니멀 DS — `--grey-{50..900}` + `--color-{family}` + `--spacing-*` + `--rounding-*`
- **CSS architecture**: 플랫 2계층
  ```
  --grey-{step}        raw neutral
  --color-{family}     HSL semantic (yellow/red/blue/green)
  --rounding-*         radius scale
  --spacing-*          spacing scale
  ```
- **Class naming**: kebab-case utility (`.navbar`, `.key-bg`, `.color-step-*`)
- **Default theme**: **dark** · `--background: var(--grey-900) = #07080a`
- **Font loading**: `next/font`로 self-host, fallback pair (`Inter Fallback`, `JetBrains Mono Fallback`) metric-matched
- **Canonical anchor**: `#FF6363` brand red (실빈도 26회 top) + `#d9d9d9` (22회 divider/icon)

---

## 04. Font Stack

- **Body font**: `Inter` / `Inter Fallback` (metric-matched) — self-host via `next/font`
- **Mono**: `GeistMono` (Vercel), `JetBrains Mono` 보조
- **Weight normal / bold**: `500` / `600`

```css
:root {
  --font-inter:         "Inter", "Inter Fallback";
  --font-jetbrains-mono:"JetBrains Mono", "JetBrains Mono Fallback";
  --font-geist-mono:    "GeistMono", ui-monospace, SFMono-Regular,
                        Roboto Mono, Menlo, Monaco, "Liberation Mono";
  --main-font:          var(--font-inter), sans-serif;
  --monospace-font:     var(--font-geist-mono),
                        Menlo, Monaco, Courier, monospace;
}
body { font-family: var(--main-font); font-weight: 500; }
code { font-family: var(--monospace-font); }
```

> `next/font`가 생성하는 `Inter Fallback` 메트릭-매치 폴백을 생략하면 SSR 로딩 시점에 CLS(레이아웃 시프트)가 발생한다. 반드시 쌍으로.

---

## 05. Typography Scale

실측 `font-size` 빈도 top-8:

| px | 빈도 |
|---|---|
| 14px | 137 ⭐ body default |
| 13px | 69 |
| 12px | 71 |
| 16px | 65 |
| 20px | 37 |
| 18px | 28 |
| 15px | 27 |
| 11px | 26 |

Weight 히스토그램: **500(211) ⭐** · 600(67) · 400(53) · 100(14) · 700(12) · 300(5).

> ⚠️ Raycast 본문 사이즈는 **14px**가 기본, weight **500**이 지배적. Tailwind의 `text-sm font-medium`이 출발점.

---

## 06. Colors

### 06-1. Grey Ramp (중립 축, 9단계)

| Token | Hex |
|---|---|
| `--grey-50`  | `#e6e6e6` |
| `--grey-100` | `#cdcece` |
| `--grey-200` | `#9c9c9d` |
| `--grey-300` | `#6a6b6c` |
| `--grey-400` | `#434345` |
| `--grey-500` | `#2f3031` |
| `--grey-600` | `#1b1c1e` |
| `--grey-700` | `#111214` |
| `--grey-800` | `#0c0d0f` |
| `--grey-900` | `#07080a` ⭐ background anchor |

### 06-2. Semantic Colors (HSL)

| Token | HSL | Hex 근사 |
|---|---|---|
| `--color-red`     | `hsl(0,100%,69%)`   | `#FF6363` ⭐ 브랜드 |
| `--color-yellow`  | `hsl(43,100%,60%)`  | `#FFB333` 근사 |
| `--color-blue`    | `hsl(202,100%,67%)` | `#56C2FF` |
| `--color-green`   | `hsl(151,59%,59%)`  | `#59D499` |
| `--color-fg`      | `hsl(240,11%,96%)`  | `#F3F3F4` |
| `--color-border`  | `hsl(195,5%,15%)`   | `#24262A` |

각 색에는 `-transparent` (alpha 0.15) variant가 쌍으로 존재:
```css
--color-red-transparent: hsla(0,100%,69%,0.15);
--color-yellow-transparent: hsla(43,100%,60%,0.15);
```

### 06-3. Background Layers (elevation)

| Token | Value |
|---|---|
| `--color-bg`     | `var(--grey-900)` |
| `--color-bg-100` | `rgb(16,17,17)` |
| `--color-bg-200` | `rgb(24,25,26)` |
| `--color-bg-300` | `rgb(49,49,51)` |
| `--color-bg-400` | `rgb(73,75,77)` |

### 06-4. Step Colors (feature highlight)

`--color-step-1 ~ 5`가 feature sequence에 쓰임:
1. yellow · 2. `#d3b2ff` (lavender) · 3. red-dark · 4. red-dark · 5. blue

### 06-5. Dominant Colors (실제 DOM 빈도)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#ff6363` | 26 | ⭐ brand red |
| 2 | `#ffffff` | 24 | text on dark |
| 3 | `#d9d9d9` | 22 | icon / divider |
| 4 | `#111214` | 13 | grey-700 surface |
| 5 | `#0c0d0f` | 13 | grey-800 surface |
| 6 | `#452324` | 10 | deep red 잠김색 |
| 7 | `#59d499` | 6  | green accent |

---

## 07. Spacing

전용 `--spacing-*` 14단계:

| Token | Value |
|---|---|
| `--spacing-none` | 0px |
| `--spacing-0-5` | 4px |
| `--spacing-1`   | 8px |
| `--spacing-1-5` | 12px |
| `--spacing-2`   | 16px |
| `--spacing-2-5` | 20px |
| `--spacing-3`   | 24px |
| `--spacing-4`   | 32px |
| `--spacing-5`   | 40px |
| `--spacing-6`   | 48px |
| `--spacing-7`   | 56px |
| `--spacing-8`   | 64px |
| `--spacing-9`   | 80px |
| `--spacing-10`  | 96px |
| `--spacing-11`  | 112px |
| `--spacing-12`  | 168px |
| `--spacing-13`  | 224px |

추가: `--grid-gap: 32px`, `--navbar-height: 58px`.

---

## 08. Radius

`--rounding-*` 9단계 (`rounding`이라는 독특한 네이밍):

| Token | Value |
|---|---|
| `--rounding-none`   | 0px |
| `--rounding-xs`     | 4px |
| `--rounding-sm`     | 6px |
| `--rounding-normal` | 8px ⭐ default |
| `--rounding-md`     | 12px |
| `--rounding-lg`     | 16px |
| `--rounding-xl`     | 20px |
| `--rounding-xxl`    | 24px |
| `--rounding-full`   | 100% |

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Breakpoint | Width | Key Changes |
|---|---|---|
| Mobile | <640px | 단일 컬럼, 헤딩 축소, 카드 스택 |
| Tablet | 640-1024px | 2열 그리드, 중간 패딩 |
| Desktop | 1024-1280px | 풀 레이아웃, 3열 그리드 |
| Large | >1280px | 중앙 정렬 max-width 1200px, 넉넉한 마진 |

> ⚠️ Raycast는 모바일 퍼스트 반응형 디자인을 채택하며, 브레이크포인트별로 그리드와 타이포그래피가 유동적으로 조정된다.

---

## 13. Components

### Primary Button (transparent hover bg)
```html
<button style="background:transparent;
               color:#fff;font-weight:500;font-size:14px;
               padding:10px 18px;border-radius:8px;
               border:1px solid rgba(255,255,255,0.1);
               transition:background 160ms ease;"
        onmouseover="this.style.background='rgba(255,255,255,0.1)'"
        onmouseout="this.style.background='transparent'">
  Download
</button>
```

### Keyboard Key (Raycast 시그니처)
```html
<kbd style="display:inline-flex;align-items:center;
            padding:4px 8px;
            font-family:'GeistMono',ui-monospace;
            font-size:12px;font-weight:500;
            color:rgb(194,199,202);
            background:linear-gradient(to right, rgb(18,18,18), rgb(13,13,13));
            border:1px solid rgba(255,255,255,0.1);
            border-radius:6px;">
  ⌘ K
</kbd>
```

---

## 15. Drop-in CSS

```css
/* Raycast — copy into your root stylesheet */
:root {
  /* Fonts */
  --main-font:      "Inter", "Inter Fallback", -apple-system, sans-serif;
  --monospace-font: "GeistMono", ui-monospace, SFMono-Regular, Menlo, monospace;

  /* Grey ramp (9 steps) */
  --grey-50:  #e6e6e6;
  --grey-100: #cdcece;
  --grey-200: #9c9c9d;
  --grey-300: #6a6b6c;
  --grey-400: #434345;
  --grey-500: #2f3031;
  --grey-600: #1b1c1e;
  --grey-700: #111214;
  --grey-800: #0c0d0f;
  --grey-900: #07080a;    /* ★ bg */

  /* Semantic */
  --background:     var(--grey-900);
  --color-bg:       var(--grey-900);
  --color-fg:       hsl(240,11%,96%);
  --color-red:      hsl(0,100%,69%);      /* #FF6363 */
  --color-yellow:   hsl(43,100%,60%);
  --color-blue:     hsl(202,100%,67%);
  --color-green:    hsl(151,59%,59%);
  --color-border:   hsl(195,5%,15%);

  /* Rounding */
  --rounding-sm:     6px;
  --rounding-normal: 8px;
  --rounding-md:     12px;
  --rounding-lg:     16px;

  /* Key gradient (keyboard key component) */
  --key-bg: linear-gradient(to right, rgb(18,18,18), rgb(13,13,13));
}

body {
  font-family: var(--main-font);
  font-weight: 500;           /* Raycast base body weight */
  background: var(--background);
  color: var(--color-fg);
  font-size: 14px;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference
| Role | Hex |
|---|---|
| Primary CTA | `#FF6363` |
| Heading text | `#FFFFFF` |
| Body text | `#ABABAB` |
| Background | `#000000` |
| Border | `#333333` |
| Link | `#FF6363` |
| Dark section | `#000000` |

### Example Component Prompts
- "Create a hero section on `#000000` background. Headline at 3rem `Inter` weight 400. CTA button `#FF6363` with white text."
- "Design a card: `#FFFFFF` background, `#333333` border, 12px radius. Body text `#ABABAB` at weight 400."

### Iteration Guide
1. 폰트: `Inter` 패밀리, 본문 weight 400
2. 컬러: 브랜드 `#FF6363`는 CTA/링크에만 집중. 배경 `#000000`, 텍스트 `#FFFFFF`
3. 그림자: 다크 테마에서 border + 반투명 배경으로 elevation 표현
---

## 18. DO / DON'T

### ✅ DO
- Body weight = **500**. 400 아님. Raycast의 또렷한 텍스트는 여기서 나온다.
- Brand = **`#FF6363`** (`hsl(0,100%,69%)`). CTA/feature highlight에 공격적 사용.
- `Inter` + `Inter Fallback` 메트릭 매치 쌍을 `next/font`로 로드.
- `--grey-900 = #07080a`가 page background. 순검정 아님.
- Body 크기 = **14px**, 코드는 **GeistMono**로 렌더.
- `--rounding-*` 네이밍 유지 — `--radius-*` 아님.
- `color-step-1~5` 시퀀스 (yellow→lavender→red→red→blue)를 feature 영역에 사용.

### ❌ DON'T
- 본문 weight 400 사용 금지 — 211 vs 53, 500이 실제 주류다.
- Inter만 선언하고 Fallback 생략 금지 — metric mismatch로 CLS 발생.
- 순검정 `#000` 배경 금지 — 약간 푸른 기운의 `#07080a`.
- 브랜드 red를 Tailwind `red-500`(`#ef4444`)로 대체 금지 — Raycast는 더 밝은 `#FF6363`.
- `--radius-*` / `--space-*` 네이밍 강제 금지 — Raycast는 `--rounding-*` / `--spacing-*`.

---

