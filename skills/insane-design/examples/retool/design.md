---
slug: retool
service_name: Retool
site_url: https://retool.com
fetched_at: 2026-04-11
default_theme: dark
brand_color: "#c72844"
primary_font: Saans
font_weight_normal: 300
token_prefix: surface
---

# DESIGN.md — Retool (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Retool은 내부 도구 빌더에서 editorial-dark 감성의 마케팅 사이트로 전환했다. 거의 검정인 ink `#151515`(933회) 배경 위에 cream `#e9ebdf`(908회) 텍스트가 압도적 빈도로 사용되며, 보르도 accent `#c72844`(143회)가 브랜드 포인트를 만든다. 옛 오렌지 `#F05237` builder UI는 제품 UI에만 남은 legacy다.

Saans variable font의 비표준 weight(300/380/570)가 핵심이다. 거대한 헤드라인이 weight 300으로 나와 editorial 세련미를 연출하고, 음수 letter-spacing(`-0.031em` ~ `-0.010em`)이 타이트한 타이포그래피를 만든다. Primary CTA는 cream bg + ink text로 역전된 구조다.

**Key Characteristics:**
- Ink `#151515` + cream `#e9ebdf` 듀오가 사이트 정체성
- 보르도 `#c72844` accent (오렌지가 아님)
- Saans VF 비표준 weight: 300(headline), 380(small title), 570(title)
- Headline weight 300 + 음수 letter-spacing = editorial 감성
- 7 surface-accent family × 4-slot 컬러 시스템

---

## 01. Quick Start

> 5분 안에 Retool처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Saans (Dinamo 유료 variable font) + Px Grotesk 보조 */
body {
  font-family: "saansFont", "saansFont Fallback",
               -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 300;           /* ⚠ 아님 400 — Retool body는 300 */
  letter-spacing: 0.01em;
}

/* 2. 거의 검정 배경 + 크림 텍스트 (다크 테마) */
:root {
  --color-dark: #151515;       /* page bg */
  --color-light: #f7f8f4;      /* light inverted */
  --surface-text-primary: #e9ebdf;  /* cream body */
}
body { background: var(--color-dark); color: var(--surface-text-primary); }

/* 3. 보르도 accent (2년 전의 오렌지 아님) */
:root { --accent-bordeaux: #c72844; }
```

**절대 하지 말아야 할 것 하나**: Retool을 옛날 builder UI의 **오렌지 `#F05237`**로 칠하지 말 것. 현재 Retool 마케팅 사이트는 **다크 테마(ink `#151515`)에 크림 텍스트(`#e9ebdf`) + 보르도 accent(`#c72844`)**가 주류다. 실제 CSS에서 `#151515`는 933회, `#e9ebdf`는 908회로 압도적이고, `#c72844` 보르도는 143회다. 옛 오렌지 builder는 제품 UI에만 남아 있는 legacy.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://retool.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 388,090 bytes (Next.js SSR) |
| CSS files | 7개, 총 653,345자 |
| Custom props | 1,499 고유 `--*` 변수 |
| `@font-face` | 5 (saansFont, pxGroteskFont + Fallback) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js 마케팅 + 제품 UI 섹션 분리
- **Design system**: 자체 DS — `--surface-*`, `--btn-*`, `--raw-*` 프리픽스
- **CSS architecture**: 4계층
  ```
  --raw-{light|dark}-{tone}-{alpha}  raw tone with alpha
  --color-{light|dark}                anchor (2개만)
  --surface-{accent|text}-{variant}-{family}  semantic slot
  --btn-{variant}-{state}-{part}      button 완전 토큰화
  ```
- **Class naming**: BEM-like (`.dvt-card`, `.subnav`, `.nav`, `.btn-primary`)
- **Default theme**: **dark** · `bg = #151515`, `text = #e9ebdf`
- **Font loading**: `next/font` self-host + metric-matched Fallback 쌍
- **Canonical anchor**: ink `#151515`(933회) + cream `#e9ebdf`(908회) + bordeaux `#c72844`(143회)

---

## 04. Font Stack

- **Primary (sans)**: `saansFont` (Dinamo Typefaces, 유료 variable) + `saansFont Fallback`
- **Secondary (sans)**: `pxGroteskFont` (Optimo/내부, 유료) + `pxGroteskFont Fallback`
- **Weight normal / bold**: `300` / **570** (non-standard, VF axis 값)
- **Letter-spacing**: headline ~ body 모두 음수 (tighter)

```css
:root {
  --font-saans:      "saansFont", "saansFont Fallback";
  --font-px-grotesk: "pxGroteskFont", "pxGroteskFont Fallback";

  --font-weight-headline:     300 !important;   /* 거대 제목 */
  --font-weight-headline-xxs: 380 !important;   /* 작은 제목 */
  --font-weight-title:        570 !important;
  --font-weight-body:         300 !important;

  --letter-spacing-headline-xxl: -0.031em !important;
  --letter-spacing-headline-xl:  -0.022em !important;
  --letter-spacing-headline-lg:  -0.020em !important;
  --letter-spacing-headline-md:  -0.010em !important;
  --letter-spacing-title:         0.020em !important;
  --letter-spacing-body:          0.010em !important;
}
```

> **비표준 weight**: `380` / `570`은 Saans의 variable font axis value. 일반적인 500/600과 미세하게 다르다. Variable font 없이는 재현 불가.

---

## 05. Typography Scale

실측 `font-size` 빈도 top-5: `1.125rem(13)` · `1rem(7)` · `0.875rem(7)` · `14px(6)` · `13px(4)`.

| Role | Size | Weight | Letter-spacing |
|---|---|---|---|
| headline-xxl (hero) | ~80-96px | 300 | -0.031em |
| headline-xl | ~64px | 300 | -0.022em |
| headline-lg | ~48px | 300 | -0.020em |
| headline-md | ~32px | 300 | -0.010em |
| headline-xxs | ~18px | 380 | -0.010em |
| title | ~16px | 570 | +0.020em |
| body | 14-16px | 300 | +0.010em |

> ⚠️ **Headline이 weight 300**이라는 점이 핵심. 거대한 제목이 light weight로 나와서 editorial 세련미를 연출한다.

---

## 06. Colors

### 06-1. Anchor Duo

| Token | Hex | Count | Role |
|---|---|---|---|
| `--color-dark`  | `#151515` | 933 | ⭐ page bg (거의 검정) |
| `--color-light` | `#f7f8f4` | 113 | light inverted |
| cream text     | `#e9ebdf` | 908 | ⭐ body text on dark |

### 06-2. Surface Text Layer

```css
--surface-text-primary: #e9ebdf;
--surface-text-muted:   #cbccc4;
--surface-text-opacity-alpha-20: #e9ebdf33;
--surface-text-opacity-alpha-40: #e9ebdf66;
--surface-text-opacity-alpha-60: #e9ebdf99;
--color-surface-opacity-12: #1515151f;
--color-surface-opacity-60: #15151599;
```

### 06-3. Bordeaux Anchor

| Token | Hex | Count |
|---|---|---|
| bordeaux | `#c72844` | 143 ⭐ brand accent |
| deeper | `#8b867f` | 91 (warm gray) |
| khaki | `#f7f8f4` | 113 |

### 06-4. Surface Accent Families (7개, 각 5-slot)

각 family (`blue · gray · green · orange · pink · purple · yellow`)마다:
- `--surface-accent-background-{family}` — 다크 배경
- `--surface-accent-base-{family}` — 베이스 톤
- `--surface-accent-focused-{family}` — focus/active
- `--surface-accent-muted-{family}` — muted text/border

예시 (blue family):
```css
--surface-accent-background-blue: #1b2e44;
--surface-accent-base-blue:       #2d4c71;
--surface-accent-focused-blue:    #518dd2;   /* ★ 257 count top */
--surface-accent-muted-blue:      #b0ccea;
```

다른 family focused color:
| family | background | base | focused | muted |
|---|---|---|---|---|
| blue   | `#1b2e44` | `#2d4c71` | `#518dd2` | `#b0ccea` |
| gray   | `#282522` | `#433e38` | `#8b867f` | `#c8bfb5` |
| green  | `#0e352c` | `#185849` | `#4d9987` | `#afd1c6` |
| orange | `#491f16` | — | `#e8765e` | `#f5c2b2` |
| pink   | `#3d163d` | `#652466` | `#cc64ce` | `#e8bae8` |
| purple | `#3f2a68` | `#53397c` | `#9874d2` | `#d0c1ea` |
| yellow | `#4a2b11` | `#7c481c` | `#eca438` | `#f6d6a0` |

### 06-5. Button Tokens (primary)

```css
--btn-primary-default-background: #e9ebdf;  /* cream bg */
--btn-primary-default-text:       #151515;  /* ink text */
--btn-primary-hover-background:   #ffffff;  /* white on hover */
--btn-primary-active-background:  #ffffff;
```

+ secondary buttons with per-family strokes (blue/gray/green/pink/purple).

### 06-6. Dominant Colors

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#151515` | 933 | ink page bg |
| 2 | `#e9ebdf` | 908 | cream text |
| 3 | `#518dd2` | 257 | blue focused |
| 4 | `#c72844` | 143 | bordeaux accent ⭐ |
| 5 | `#cbccc4` | 135 | surface-text-muted |
| 6 | `#c8bfb5` | 120 | gray-muted |
| 7 | `#f7f8f4` | 113 | color-light |
| 8 | `#242424` | 97  | panel elevation |
| 9 | `#8b867f` | 91  | warm gray |

---

## 07. Spacing

`--mask-spacing: 16px`, `--grid-space: calc(100vw / 26)` (CSS grid system), `--menu-edge-padding: 0.75rem`. Tailwind 유틸리티가 주력.

---

## 08. Radius

| Token | Value |
|---|---|
| `--border-radius` | `1rem` (16px) |
| 주 radii from CSS | `.5rem(11) · 8px(9) · .375rem(4) · 4px(4) · 9999px(3)` |

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

### Primary Button (cream on ink)
```html
<button style="background:#e9ebdf;color:#151515;
               font-family:'saansFont',sans-serif;
               font-weight:570;font-size:14px;
               letter-spacing:0.02em;
               padding:12px 24px;border:none;
               border-radius:9999px;cursor:pointer;">
  Start for free
</button>
```

### Editorial Hero
```html
<section style="background:#151515;padding:140px 64px;color:#e9ebdf;">
  <h1 style="font-family:'saansFont',sans-serif;
             font-weight:300;font-size:clamp(56px,8vw,112px);
             line-height:0.95;letter-spacing:-0.031em;
             max-width:16ch;color:#e9ebdf;">
    Ship software at the speed of thought.
  </h1>
  <p style="font-family:'saansFont',sans-serif;
            font-weight:300;font-size:18px;
            color:#cbccc4;max-width:48ch;
            margin-top:24px;letter-spacing:0.01em;">
    Build internal tools remarkably fast.
  </p>
</section>
```

---

## 15. Drop-in CSS

```css
/* Retool — copy into your root stylesheet */
:root {
  /* Fonts (paid, self-hosted) */
  --font-saans:      "saansFont", "saansFont Fallback",
                     -apple-system, BlinkMacSystemFont, sans-serif;
  --font-px-grotesk: "pxGroteskFont", "pxGroteskFont Fallback", sans-serif;

  /* Non-standard VF weights */
  --font-weight-headline: 300;
  --font-weight-title:    570;
  --font-weight-body:     300;

  /* Anchor duo */
  --color-dark:  #151515;
  --color-light: #f7f8f4;

  /* Surface text */
  --surface-text-primary: #e9ebdf;
  --surface-text-muted:   #cbccc4;

  /* Bordeaux accent */
  --accent-bordeaux: #c72844;

  /* Letter-spacing scale */
  --ls-headline-xxl: -0.031em;
  --ls-headline-xl:  -0.022em;
  --ls-headline-md:  -0.010em;
  --ls-title:         0.020em;
  --ls-body:          0.010em;

  /* Radius */
  --border-radius: 1rem;
}

body {
  font-family: var(--font-saans);
  font-weight: var(--font-weight-body);
  letter-spacing: var(--ls-body);
  background: var(--color-dark);
  color: var(--surface-text-primary);
}

h1, h2, h3 {
  font-weight: var(--font-weight-headline);
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: auto+manual -->

### Quick Color Reference

| Role | Value |
|---|---|
| Brand | `#c72844` |
| Page BG | `#FFFFFF` |
| Text Primary | `#000000` |
| Default Theme | dark |

### Component Prompts

> **Hero section**: "Retool 스타일 hero — `Saans` 폰트, `#c72844` brand color, dark 배경"
>
> **CTA button**: "Retool primary CTA — brand `#c72844` 배경 또는 dark fill, `Saans` 폰트"
>
> **Card component**: "Retool 스타일 카드 — dark 테마, 기존 radius/shadow 토큰 준수"

### Iteration Guide

1. **Color 교체 시**: 반드시 §06 Colors 테이블의 실제 hex 참조. AI 추론 색상 사용 금지.
2. **Typography 변경 시**: §04 Font Stack의 font-family 체인 + §05의 weight/size 매핑 확인.
3. **Spacing 조정 시**: §07 Spacing의 토큰 스케일 내에서만 변경.
4. **신규 컴포넌트**: §13 Components의 기존 패턴(radius, shadow, padding)을 기반으로 확장.

---

## 18. DO / DON'T

### ✅ DO
- Background = ink `#151515` (dark). Light mode 아님.
- Text = cream `#e9ebdf` (body) + `#cbccc4` (muted). 순백 아님.
- Primary CTA = cream `#e9ebdf` bg + ink `#151515` text (역전).
- Brand accent = **보르도 `#c72844`** (143회). 오렌지 아님.
- Saans variable font + 비표준 weight (300 / 380 / 570).
- Headline weight **300** — 거대 제목이 light weight로.
- Letter-spacing 음수 (`-0.031em ~ -0.010em`) on headlines.
- 7 surface-accent family (blue/gray/green/orange/pink/purple/yellow) × 4-slot 보존.

### ❌ DON'T
- 오렌지 `#F05237`를 brand primary로 쓰지 말 것 — 옛 builder UI, 현 마케팅 사이트 아님.
- Light 테마로 전환 금지 — 현재 홈페이지는 dark가 기본.
- Inter/Helvetica로 Saans 대체 금지 — 비표준 VF weight가 복원 불가.
- headline weight 700으로 두지 말 것 — 실제는 300 (굵은 게 아니라 얇은).
- Tailwind `rounded-md`(`6px`) 강제 금지 — Retool default는 `1rem` (16px).
- 단일 accent color 사용 금지 — 7 family 구조 유지해야 product screenshot 재현 가능.
