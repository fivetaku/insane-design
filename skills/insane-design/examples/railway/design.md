---
slug: railway
service_name: Railway
site_url: https://railway.com
fetched_at: 2026-04-11
default_theme: dark
brand_color: "#381dbd"
primary_font: IBM Plex Serif
font_weight_normal: 400
token_prefix: mantine
---

# DESIGN.md — Railway (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Railway의 웹사이트는 딥 퍼플(`#13111C`) 다크 배경에 serif 디스플레이 폰트(`IBM Plex Serif`)의 조합이라는 독특한 시각 전략을 취한다. 개발자 도구이면서도 문학적이고 세련된 인상을 동시에 전달한다.

타이포그래피는 `IBM Plex Serif`(디스플레이/헤딩)와 `Inter`(본문)의 혼합 시스템을 사용한다. serif 헤딩은 Railway의 가장 독특한 시각적 시그니처이며, 본문 weight는 **400**이다.

브랜드 딥 퍼플 `#381dbd`가 accent로 사용되며, oatmeal `#f1f0ef` 라이트 섹션 브레이크가 다크 배경과 교차하며 시각적 리듬을 만든다.

**Key Characteristics:**
- **IBM Plex Serif**를 hero headline / section title에 적용. Railway 시그니처.
- Body는 Inter/Inter Tight. 혼합 타이포가 editorial 느낌.
- 다크 배경 = `#08070c`(ultra) + `#13111c`(card). 순검정 금지.
- Light 섹션 브레이크에는 oatmeal `#f1f0ef` 사용 (warm cream).
- Button height는 `--button-height-{xs..xl}` 5단계 사이즈별 토큰 유지.
---

## 01. Quick Start

> 5분 안에 Railway처럼 만들기 — 3가지만 하면 80%

```css
/* 1. IBM Plex Serif 디스플레이 + Inter 본문 (혼합) */
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Serif:wght@400;500;600&family=Inter:wght@400;500;600&display=swap');

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont,
               'Segoe UI', Roboto, sans-serif;
  font-weight: 400;
}
h1, h2, h3, .display {
  font-family: 'IBM Plex Serif', ui-serif, Georgia, serif;
}

/* 2. 딥 퍼플 다크 배경 + 화이트 텍스트 */
:root {
  --background: hsl(250, 24%, 9%);   /* #13111c 계열 */
  --foreground: hsl(0, 0%, 100%);
}
body { background: var(--background); color: var(--foreground); }

/* 3. 퍼플 accent (딥/oatmeal 대비) */
:root {
  --accent-purple: #381dbd;
  --bg-oatmeal:    #f1f0ef;   /* light 섹션 브레이크 */
}
```

**절대 하지 말아야 할 것 하나**: Railway를 일반적인 dark SaaS처럼 Inter-only로 만들지 말 것. **Railway의 디스플레이 타이포는 IBM Plex Serif**다 (빈도 45회 최다). Hero headline, section title, quote가 모두 세리프로 가고, body만 Inter/Inter Tight. 이 혼합이 Railway의 editorial 느낌을 만든다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://railway.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 229,934 bytes (Next.js SSR) |
| CSS files | 17개 (Mantine + 커스텀 + `style-*`), 총 **1,387,053자** |
| Custom props | 2,077 고유 `--*` 변수 |
| `@font-face` | 72 (Inter · Inter Tight · IBM Plex Serif · JetBrains Mono) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js + **Mantine UI** component library
- **Design system**: Mantine (`--mantine-*` 토큰 471개) + 자체 커스텀 (`--train-*`, `--sl-*`, `--flip-*`)
- **CSS architecture**: Mantine 표준 3계층
  ```
  --mantine-color-{family}-{0-9}   raw ramp (dark, gray, blue, ...)
  --mantine-color-body / -text     semantic body/text
  --mantine-radius-{xs|sm|md|lg|xl} · --mantine-shadow-*
  ```
- **Class naming**: Mantine BEM (`.mantine-Button-root`, `.mantine-Paper-root`)
- **Default theme**: **dark** · `--background: hsl(250, 24%, 9%)` (퍼플 기운 있는 딥 차콜)
- **Font loading**: 72개 `@font-face`, self-hosted 4 family × 다중 weight
- **Canonical anchor**: `#08070c` / `#13111c` (실빈도 top-2, 딥 다크 표면) + 퍼플 `#381dbd` accent
- **Editorial detail**: IBM Plex Serif를 display에, Inter를 body에 → fintech/editorial 혼합 무드

---

## 04. Font Stack

- **Display (serif)**: `IBM Plex Serif` (OFL) — 45회 최다
- **Body (sans)**: `Inter` / `Inter Tight`
- **Mono**: `JetBrains Mono` (OFL)
- **Mantine default**: `-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif`

```css
:root {
  --font-inter: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-ibm-plex-serif: 'IBM Plex Serif', ui-serif, Georgia,
                         'Times New Roman', Times, serif;
  --font-jetbrains-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo;

  --mantine-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
                         Roboto, Helvetica, Arial, sans-serif;
  --mantine-font-family-monospace: ui-monospace, SFMono-Regular, Menlo,
                                   Monaco, Consolas, 'Liberation Mono', Courier;
  --mantine-font-family-headings: -apple-system, BlinkMacSystemFont, 'Segoe UI',
                                  Roboto, Helvetica, Arial, sans-serif;
  --mantine-heading-font-weight: 700;
}
```

---

## 05. Typography Scale

Mantine 표준 `xs/sm/md/lg/xl` × `--mantine-scale` 곱셈:

| Token | rem (scale=1) | px |
|---|---|---|
| `--mantine-font-size-xs` | 0.75rem | 12 |
| `--mantine-font-size-sm` | 0.875rem | 14 |
| `--mantine-font-size-md` | 1rem | 16 |
| `--mantine-font-size-lg` | 1.125rem | 18 |
| `--mantine-font-size-xl` | 1.25rem | 20 |

> 실측 CSS `font-size` 빈도 top-5: 18px(11) · 20px(10) · 14px(9) · 16px(7) · 12px(5). Hero 헤드라인은 대체로 `clamp(48px, 6vw, 80px)` 클래스 범위.

Weight 히스토그램: 600(26) · 700(26) · 400(23) · 500(21) · 100(20). `--mantine-heading-font-weight: 700`이 기본.

---

## 06. Colors

### 06-1. Surface (dark)

| Token | Hex | Usage |
|---|---|---|
| `--background` | `hsl(250, 24%, 9%)` → `#13111c` | 페이지 배경 |
| page ultra-dark | `#08070c` | 헤더/시작 영역 (빈도 14회 top) |
| surface elev 1 | `#13111c` | 카드 기본 (빈도 10회) |
| surface elev 2 | `#131415` | 중첩 패널 |
| `--foreground` | `hsl(0, 0%, 100%)` → `#ffffff` | 본문 |
| `--bg-oatmeal` | `#f1f0ef` | ⭐ light 섹션 브레이크 (warm cream) |
| alt-light | `#f9f3e9` | warm oat variant |
| neutral-light | `#e7e5e3` | warm gray light |

### 06-2. Purple Accents (브랜드 레이어)

| Token | Hex | Count |
|---|---|---|
| purple-deep    | `#381dbd` | 4 |
| purple-navy    | `#2c0a5c` | 4 |
| purple-plum    | `#59497a` | 5 |
| purple-charcoal| `#4a3d66` | 4 |
| purple-black   | `#16093b` | 3 |
| purple-violet  | `#221228` | 3 |

### 06-3. Secondary Accents (magenta · blue)

| Token | Hex | Usage |
|---|---|---|
| magenta | `#5e084d` | 이벤트/highlight |
| tw gray | `#e5e7eb` | light divider |
| cool gray | `#9ca3af` | muted text |
| cool slate | `#6b7280` | secondary |

### 06-4. Button System

Railway는 사이즈별 button height를 전용 토큰화:

```css
--button-height-xs: 30px;
--button-height-sm: 36px;
--button-height-md: 42px;   /* default */
--button-height-lg: 50px;
--button-height-xl: 60px;

--button-padding-x-sm: 18px;
--button-padding-x-md: 22px;
--button-padding-x-lg: 26px;

--button-color: var(--mantine-color-white);
--button-border-width: 1px;
```

### 06-5. Dominant Colors

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#08070c` | 14 | 초다크 페이지 배경 |
| 2 | `#13111c` | 10 | 카드/paper |
| 3 | `#e5e7eb` | 6  | divider light |
| 4 | `#9ca3af` | 5  | muted text |
| 5 | `#59497a` | 5  | 퍼플 plum |
| 6 | `#f9f3e9` | 5  | oatmeal light |
| 7 | `#e7e5e3` | 5  | warm gray light |

---

## 07. Spacing

Mantine + 자체 `--button-*` / `--section-*` padding 토큰:

| Token | Value |
|---|---|
| `--button-padding-x-xs` | 14px |
| `--button-padding-x-sm` | 18px |
| `--button-padding-x-md` | 22px |
| `--button-padding-x-lg` | 26px |
| `--button-padding-x-xl` | 32px |
| `--section-padding-x-sm` | 18px |
| `--section-padding-x-md` | 22px |
| compact xs~xl | 7/8/10/12/14 px |

Mantine spacing: `--mantine-spacing-{xs..xl} = calc(rem × scale)`. xs 0.625rem, sm 0.75rem, md 1rem, lg 1.25rem, xl 2rem.

---

## 08. Radius

| Token | Value |
|---|---|
| `--mantine-radius-xs`      | `calc(0.125rem × scale)` |
| `--mantine-radius-sm`      | `calc(0.25rem × scale)` |
| `--mantine-radius-md`      | `calc(0.5rem × scale)` |
| `--mantine-radius-default` | `calc(0.25rem × scale)` ⭐ |
| `--badge-radius`           | `1000px` (full pill) |
| `--slider-radius`          | `1000px` |

`--cb-radius` / `--paper-radius` / `--input-radius` / `--tooltip-radius`는 모두 `var(--mantine-radius-default)`를 참조.

---

## 09. Shadows

Mantine 4-level:

```css
--mantine-shadow-xs: 0 0.0625rem 0.1875rem #0000000d,
                     0 0.0625rem 0.125rem #0000000d;
--mantine-shadow-sm: 0 0.0625rem 0.1875rem #0000000d,
                     0 0.625rem 1.5rem  #0000000d;
--mantine-shadow-md: 0 0.0625rem 0.1875rem #0000000d,
                     0 1.25rem 2.5rem   #0000000d;
--mantine-shadow-lg: 0 0.0625rem 0.1875rem #0000000d,
                     0 1.75rem 3rem     #0000000d;
--mantine-shadow-xl: 0 0.0625rem 0.1875rem #0000000d,
                     0 2.25rem 3.5rem   #0000000d;
```

+ 커스텀: `--nested-canvas-shadow: 0 0 0 1px #00000014, 0 2px 8px -2px #00000014, 0 4px 16px -4px #00000014;`

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Breakpoint | Width | Key Changes |
|---|---|---|
| Mobile | <640px | 단일 컬럼, 헤딩 축소, 카드 스택 |
| Tablet | 640-1024px | 2열 그리드, 중간 패딩 |
| Desktop | 1024-1280px | 풀 레이아웃, 3열 그리드 |
| Large | >1280px | 중앙 정렬 max-width 1200px, 넉넉한 마진 |

> ⚠️ Railway는 모바일 퍼스트 반응형 디자인을 채택하며, 브레이크포인트별로 그리드와 타이포그래피가 유동적으로 조정된다.

---

## 13. Components

### Mantine Button (primary)
```html
<button class="mantine-Button-root mantine-UnstyledButton-root"
        style="--button-height: var(--button-height-md);
               --button-padding-x: var(--button-padding-x-md);
               --button-color: #fff;">
  Start a project
</button>
```

### Editorial Hero
```html
<section style="background:#08070c;padding:120px 64px;color:#fff;">
  <h1 style="font-family:'IBM Plex Serif', serif;
             font-size:clamp(48px,6vw,88px);
             font-weight:400;line-height:1.05;
             letter-spacing:-0.02em;max-width:14ch;">
    Deploy your code. Forget the rest.
  </h1>
  <p style="font-family:'Inter', sans-serif;
            color:#9ca3af;max-width:52ch;margin-top:24px;">
    Railway handles everything from source to production.
  </p>
</section>
```

---

## 15. Drop-in CSS

```css
/* Railway — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-display: 'IBM Plex Serif', ui-serif, Georgia, 'Times New Roman', serif;
  --font-body:    'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono:    'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;

  /* Surfaces (dark) */
  --background:       hsl(250, 24%, 9%);   /* #13111c */
  --bg-ultra-dark:    #08070c;
  --bg-surface:       #13111c;
  --bg-oatmeal:       #f1f0ef;              /* light break */
  --foreground:       #ffffff;
  --text-muted:       #9ca3af;

  /* Purple accents */
  --accent-purple:    #381dbd;
  --accent-plum:      #59497a;
  --accent-navy:      #2c0a5c;

  /* Button sizes */
  --button-height-sm: 36px;
  --button-height-md: 42px;
  --button-height-lg: 50px;
  --button-padding-x-md: 22px;

  /* Radius */
  --radius-default: 0.25rem;
  --radius-badge:   1000px;
}

body {
  font-family: var(--font-body);
  background: var(--background);
  color: var(--foreground);
}

h1, h2, h3 {
  font-family: var(--font-display);
  font-weight: 400;
  letter-spacing: -0.01em;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference
| Role | Hex |
|---|---|
| Primary CTA | `#381dbd` |
| Heading text | `#FFFFFF` |
| Body text | `#A0A0A0` |
| Background | `#13111C` |
| Border | `#2A2A2A` |
| Link | `#381dbd` |
| Dark section | `#13111C` |

### Example Component Prompts
- "Create a hero section on `#13111C` background. Headline at 3rem `IBM Plex Serif` weight 400. CTA button `#381dbd` with white text."
- "Design a card: `#FFFFFF` background, `#2A2A2A` border, 12px radius. Body text `#A0A0A0` at weight 400."

### Iteration Guide
1. 폰트: `IBM Plex Serif` 패밀리, 본문 weight 400
2. 컬러: 브랜드 `#381dbd`는 CTA/링크에만 집중. 배경 `#13111C`, 텍스트 `#FFFFFF`
3. 그림자: 딥 퍼플 다크 테마에서 border + surface로 elevation 표현
---

## 18. DO / DON'T

### ✅ DO
- **IBM Plex Serif**를 hero headline / section title에 적용. Railway 시그니처.
- Body는 Inter/Inter Tight. 혼합 타이포가 editorial 느낌.
- 다크 배경 = `#08070c`(ultra) + `#13111c`(card). 순검정 금지.
- Light 섹션 브레이크에는 oatmeal `#f1f0ef` 사용 (warm cream).
- Button height는 `--button-height-{xs..xl}` 5단계 사이즈별 토큰 유지.
- Mantine <code>--mantine-*</code> 네임스페이스 준수.

### ❌ DON'T
- Inter-only 로 가지 말 것 — Plex Serif가 없으면 즉시 평범한 dark SaaS가 됨.
- 순검정 `#000000` 배경 금지. 퍼플 기운 있는 `hsl(250 24% 9%)`.
- Tailwind naming (`bg-gray-900`)으로 대체 금지 — Mantine 토큰이 진짜 소스.
- Purple accent를 네온 violet(`#7c3aed`)으로 덮지 말 것. Railway는 **딥/다크 purple** (`#381dbd`, `#2c0a5c`).
- 단일 섀도 atom 사용 금지 — Mantine의 5-level `xs/sm/md/lg/xl` 단계를 유지.

---

