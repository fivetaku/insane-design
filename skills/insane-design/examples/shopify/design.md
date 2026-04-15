---
slug: shopify
service_name: Shopify
site_url: https://shopify.com
fetched_at: 2026-04-11
default_theme: dark
brand_color: "#008060"
primary_font: ShopifySans
font_weight_normal: 420
token_prefix: ""
---

# DESIGN.md — Shopify (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Shopify의 웹사이트는 밝은 배경 위에 따뜻하면서도 전문적인 그린 accent가 결합된 커머스 플랫폼 디자인이다. 판매자(머천트)에게 신뢰감과 접근성을 동시에 전달하는 것이 핵심 전략이다.

타이포그래피는 기본 시스템 서체를 사용한다. 본문 weight는 **400**이며, 마케팅 헤딩은 더 큰 weight로 시각적 임팩트를 강화한다.

브랜드 그린 `#008060`는 CTA와 성공 상태에 집중 사용된다. 따뜻한 그린 톤이 커머스 맥락에서의 성장과 번영을 시각적으로 표현하며, 보조 컬러는 절제되어 그린의 집중도를 유지한다.

**Key Characteristics:**
- Background = rich-black `#02090a` (약간 teal). 순검정 아님.
- Body weight = `420` (VF axis), display = `330` — 둘 다 비표준.
- Brand = Shopify green `#008060` (공식 로고 색).
- Hero accent = mint `#36f4a4` + cyan `#30deee` + pistachio highlight.
- ShopifySans self-host. Noto Sans JP fallback 필수 (국제화).
---

## 01. Quick Start

> 5분 안에 Shopify처럼 만들기 — 3가지만 하면 80%

```css
/* 1. ShopifySans (자체 유료 VF) — fallback은 Inter */
body {
  font-family: "ShopifySans", "Inter", -apple-system,
               BlinkMacSystemFont, "Helvetica Neue", sans-serif;
  font-weight: 420;   /* ⚠ 400 아님 — Shopify body는 420 VF axis */
}

/* 2. 리치 블랙 배경 + 화이트 + shade-10 (거의 흰) */
:root {
  --color-rich-black: #02090a;     /* 순검정 아님, 약간 teal */
  --color-shade-10:   #f4f4f5;     /* 거의 white 카드 */
}
body { background: var(--color-rich-black); color: #fff; }

/* 3. Shopify Green (그리고 밝은 mint/pistachio accent) */
:root {
  --brand-green: #008060;          /* Shopify 공식 그린 */
  --accent-mint: #36f4a4;          /* hero accent */
}
```

**절대 하지 말아야 할 것 하나**: Shopify body weight를 `400`으로 두지 말 것. Shopify는 variable font ShopifySans에서 `--font-weight-body-base: 420`을 쓴다. 비표준 weight (330/420/450/550/650/750)가 진짜 소스고, 일반 Inter 400으로는 미묘하게 다른 글자 굵기가 나온다. 또한 Shopify는 2024-2025 리뉴얼 이후 **다크 테마** (`#02090a` rich-black)가 기본이다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://shopify.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 613,322 bytes (Next.js SSR) |
| CSS files | 1개 (`home.v4-B3yVkUYS.css`), 총 229,832자 |
| Custom props | 944 고유 `--*` 변수 |
| `@font-face` | **52** (ShopifySans · Noto Sans JP · IBMPlexMono · PolySans · Trap · GTSuper · GoodSans · DrukCondSuper 등 23 family) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js 마케팅 홈 (`home.v4`)
- **Design system**: Tailwind v4 (`--color-shade-*`, `--text-*`, `--spacing: .25rem` 등) + 자체 shade/accent
- **CSS architecture**: Tailwind v4 native + 자체 layer
  ```
  --color-shade-{10..100}           Zinc-aligned 중립 (10=#f4f4f5, 100=#000)
  --color-{green|blue|purple}-500   Tailwind OKLCH colors
  --color-{pistachio|aloe}-10       자체 mint highlight
  --font-weight-t1..t8, b1..b6, dsp  VF-aware typography slots
  --letter-spacing-t1..t8           per-slot tracking
  ```
- **Class naming**: Tailwind utility + semantic title/body `t{1..8}` scale
- **Default theme**: **dark** · `bg = #02090a rich-black`
- **Font loading**: 52개 `@font-face` self-host, ShopifySans 6 variants
- **Canonical anchor**: rich-black `#02090a`(10회) + mint `#36f4a4`(8회) + ShopifySans VF

---

## 04. Font Stack

- **Primary (sans)**: `ShopifySans` (variable font, self-host) — 6 variants
- **Japanese**: `Noto Sans JP` (6 variants, CJK support)
- **Mono**: `IBMPlexMono` (4 variants)
- **Accent displays**: `PolySans` · `Trap` · `FeatureDisplay` · `GoodSans` · `GTSuperDisplay` · `NeueHaasGrotesk` (3 each)
- **Editorial**: `DrukCondSuper` · `DrukTextHeavy` · `Roslindale` · `GaramondNovaPro`

```css
:root {
  /* 자체 weight slots — VF axis values */
  --font-weight-normal:    400;
  --font-weight-medium:    450;
  --font-weight-semibold:  600;
  --font-weight-bold:      550;  /* ⚠ 700 아님 */
  --font-weight-extrabold: 650;
  --font-weight-black:     750;

  /* 역할별 weight (dsp = display, t = title, b = body) */
  --font-weight-dsp: 330;          /* hero display — 얇은! */
  --font-weight-t1:  330;
  --font-weight-t4:  330;
  --font-weight-t5:  400;
  --font-weight-t6:  420;
  --font-weight-t7:  450;
  --font-weight-t8:  450;
  --font-weight-body-lg:   400;
  --font-weight-body-base: 420;   /* default body */
  --font-weight-body-sm:   420;
}
```

> **핵심**: `dsp` / `t1-t4` = 330 (얇은 hero headline), `body-base` = 420 (중간). 이 2개 weight가 Shopify 타이포의 정체성.

---

## 05. Typography Scale

Tailwind v4 `--text-*` + Shopify 자체 `t1-t8` (title) + `b1-b6` (body) + `dsp` (display):

| Token | rem | px |
|---|---|---|
| `--text-xs`   | 0.75rem   | 12 |
| `--text-sm`   | 0.875rem  | 14 |
| `--text-base` | 1rem      | 16 |
| `--text-lg`   | 1.125rem  | 18 |
| `--text-xl`   | 1.25rem   | 20 |
| `--text-2xl`  | 1.5rem    | 24 |
| `--text-3xl`  | 1.875rem  | 30 |

Letter-spacing (title slot):
```
--letter-spacing-dsp: -0.01em
--letter-spacing-t1:  -0.005em
--letter-spacing-t5:  -0.005em
--letter-spacing-t7:  -0.05em    /* ⚠ 큰 음수 */
--letter-spacing-body-base: -0.006em
```

---

## 06. Colors

### 06-1. Shade Ramp (Zinc-aligned, 9 steps)

| Token | Hex |
|---|---|
| `--color-shade-10`  | `#f4f4f5` (거의 white) |
| `--color-shade-20`  | `#e4e4e7` |
| `--color-shade-30`  | `#d4d4d8` |
| `--color-shade-40`  | `#a1a1aa` |
| `--color-shade-50`  | `#71717a` |
| `--color-shade-60`  | `#52525b` |
| `--color-shade-70`  | `#3f3f46` |
| `--color-shade-90`  | `#18181b` |
| `--color-shade-100` | `#000` |

### 06-2. Rich Black & Hero Dark

| Token | Hex | Count |
|---|---|---|
| `--color-rich-black` | `#02090a` | 10 ⭐ page bg |
| ultra-dark | `#061a1c` | 16 (hero gradient) |
| deep teal  | `#121c1e` | 10 |

### 06-3. Brand Green

| Token | Hex | Role |
|---|---|---|
| shopify-green | `#008060` | 공식 로고/브랜드 (빈도 6) |
| mint-bright   | `#36f4a4` | 8 — hero accent |
| cyan-electric | `#30deee` | 7 — secondary accent |
| `--color-pistachio-10` | `#d4f9e0` | pale mint highlight |
| `--color-aloe-10`      | `#c1fbd4` | pale aloe highlight |
| deep teal bg  | `#11352d` | 4 — green section bg |

### 06-4. Link System (dark theme)

```css
--color-link-dark:          #9797a2;
--color-link-dark-hover:    #d4d4d8;
--color-link-dark-active:   #a1a1aa;
--color-link-dark-focus:    #fff;
--color-link-dark-disabled: #71717a;
```

### 06-5. Tailwind v4 OKLCH families

Shopify는 Tailwind v4의 OKLCH 컬러를 그대로 사용:
```css
--color-orange-500:  oklch(70.5% .213 47.604);
--color-yellow-500:  oklch(79.5% .184 86.047);
--color-green-500:   oklch(72.3% .219 149.579);
--color-blue-500:    oklch(62.3% .214 259.815);
--color-purple-300:  oklch(82.7% .119 306.383);
--color-purple-500:  oklch(62.7% .265 303.9);
--color-zinc-300:    oklch(87.1% .006 286.286);
--color-zinc-900:    oklch(21% .006 285.885);
```

### 06-6. Dominant Colors

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#d4d4d8` | 17 | shade-30 border |
| 2 | `#71717a` | 16 | shade-50 muted |
| 3 | `#061a1c` | 16 | ultra-dark hero |
| 4 | `#f4f4f5` | 15 | shade-10 surface |
| 5 | `#a1a1aa` | 13 | shade-40 |
| 6 | `#02090a` | 10 | rich-black ⭐ |
| 7 | `#121c1e` | 10 | deep teal |
| 8 | `#36f4a4` | 8  | mint bright ⭐ |
| 9 | `#30deee` | 7  | cyan electric |
| 10 | `#008060` | 6 | Shopify green logo |

---

## 07. Spacing

| Token | rem | px |
|---|---|---|
| `--spacing` (base) | 0.25rem | 4 |
| `--space-xs` | 0.25rem | 4 |
| `--space-sm` | 0.5rem  | 8 |
| `--space-md` | 1rem    | 16 |
| `--space-lg` | 1.5rem  | 24 |
| `--space-xl` | 2rem    | 32 |

---

## 08. Radius

| Token | Value |
|---|---|
| `--radius-md`  | 0.375rem (6px) |
| `--radius-lg`  | 0.5rem (8px) |
| `--radius-xl`  | 0.75rem (12px) |
| `--radius-2xl` | 1rem (16px) |

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Breakpoint | Width | Key Changes |
|---|---|---|
| Mobile | <640px | 단일 컬럼, 헤딩 축소, 카드 스택 |
| Tablet | 640-1024px | 2열 그리드, 중간 패딩 |
| Desktop | 1024-1280px | 풀 레이아웃, 3열 그리드 |
| Large | >1280px | 중앙 정렬 max-width 1200px, 넉넉한 마진 |

> ⚠️ Shopify는 모바일 퍼스트 반응형 디자인을 채택하며, 브레이크포인트별로 그리드와 타이포그래피가 유동적으로 조정된다.

---

## 13. Components

### Hero CTA (Shopify green pill)
```html
<button style="font-family:'ShopifySans',Inter,sans-serif;
               font-weight:450;font-size:16px;
               padding:14px 28px;
               background:#008060;color:#fff;
               border:none;border-radius:9999px;
               letter-spacing:-0.005em;">
  Start free trial
</button>
```

### Editorial Display
```html
<h1 style="font-family:'ShopifySans',sans-serif;
           font-size:clamp(56px,8vw,112px);
           font-weight:330;           /* dsp weight */
           line-height:0.95;
           letter-spacing:-0.01em;
           color:#36f4a4;
           max-width:12ch;">
  The best place to do business.
</h1>
```

---

## 15. Drop-in CSS

```css
/* Shopify — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-sans: "ShopifySans", "Inter", -apple-system,
               BlinkMacSystemFont, "Helvetica Neue", sans-serif;
  --font-mono: "IBMPlexMono", ui-monospace, SFMono-Regular,
               Menlo, Monaco, Consolas, monospace;
  --font-jp:   "Noto Sans JP", "ShopifySans", sans-serif;

  /* VF-aware weights */
  --font-weight-dsp:       330;
  --font-weight-t1:        330;
  --font-weight-t5:        400;
  --font-weight-body-base: 420;
  --font-weight-medium:    450;
  --font-weight-bold:      550;

  /* Surface (dark) */
  --color-rich-black:  #02090a;
  --color-shade-10:    #f4f4f5;
  --color-shade-50:    #71717a;
  --color-shade-90:    #18181b;
  --color-ultra-dark:  #061a1c;

  /* Brand */
  --brand-green:   #008060;
  --accent-mint:   #36f4a4;
  --accent-cyan:   #30deee;
  --pistachio-10:  #d4f9e0;
  --aloe-10:       #c1fbd4;

  /* Links (dark) */
  --color-link-dark:       #9797a2;
  --color-link-dark-hover: #d4d4d8;

  /* Radius */
  --radius-md: 0.375rem;
  --radius-xl: 0.75rem;
}

body {
  font-family: var(--font-sans);
  font-weight: var(--font-weight-body-base);
  background: var(--color-rich-black);
  color: #fff;
}

h1, .display {
  font-weight: var(--font-weight-dsp);
  letter-spacing: -0.01em;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference
| Role | Hex |
|---|---|
| Primary CTA | `#008060` |
| Heading text | `#1A1A1A` |
| Body text | `#474747` |
| Background | `#FFFFFF` |
| Border | `#E3E3E3` |
| Link | `#008060` |
| Dark section | `#1A1A1A` |

### Example Component Prompts
- "Create a hero section on `#FFFFFF` background. Headline at 3.5rem `ShopifySans` weight 420. CTA button `#008060` with white text."
- "Design a card: `#1c1c1f` background, `#E3E3E3` border, 8px radius. Body text `#474747` at weight 420."

### Iteration Guide
1. 폰트: `ShopifySans` 패밀리, 본문 weight 420
2. 컬러: 브랜드 `#008060`는 CTA/링크에만 집중. 배경 `#FFFFFF`, 텍스트 `#1A1A1A`
3. 그림자: subtle box-shadow로 카드 elevation 표현
---

## 18. DO / DON'T

### ✅ DO
- Background = rich-black `#02090a` (약간 teal). 순검정 아님.
- Body weight = `420` (VF axis), display = `330` — 둘 다 비표준.
- Brand = Shopify green `#008060` (공식 로고 색).
- Hero accent = mint `#36f4a4` + cyan `#30deee` + pistachio highlight.
- ShopifySans self-host. Noto Sans JP fallback 필수 (국제화).
- Letter-spacing: display `-0.01em`, title `-0.005em ~ -0.05em`, body `-0.006em`.
- 23 font family 다국어/다중 display 지원 구조 유지.

### ❌ DON'T
- Body weight 400 사용 금지 — 실제 420 (VF axis 중간값).
- Display weight 700 금지 — 실제 **330** (얇은 hero).
- 순검정 `#000` 배경 금지 — `#02090a` rich-black (약간 teal 기운).
- Shopify green을 `#16a34a` Tailwind green-600으로 대체 금지 — 공식은 `#008060`.
- ShopifySans를 Inter로만 대체 금지 — fallback은 OK지만 VF weight이 정체성.
- 단일 폰트로 평탄화 금지 — display/title/body 역할별 분리가 핵심.

---

