---
slug: resend
service_name: Resend
site_url: https://resend.com
fetched_at: 2026-04-11
default_theme: light
brand_color: "#1d1c1b"
primary_font: ABCFavorit
font_weight_normal: 400
token_prefix: ""
---

# DESIGN.md — Resend (Claude Code Edition)

---

## 01. Quick Start

> 5분 안에 Resend처럼 만들기 — 3가지만 하면 80%

```css
/* 1. ABCFavorit sans + Domaine serif + commitMono (모두 유료 커스텀 폰트) */
body {
  font-family: "aBCFavorit", "Inter", -apple-system, sans-serif;
  font-weight: 400;
}
.display {
  font-family: "domaine", "Cormorant Garamond", ui-serif, Georgia, serif;
}

/* 2. 거의 흰색 배경 + 거의 검정 텍스트 */
:root {
  --background: #fdfdfd;  /* pure white는 아님 */
  --foreground: #1d1c1b;  /* warm ink */
}
body { background: var(--background); color: var(--foreground); }

/* 3. Radix Color 시스템 (sand/slate/mauve/violet) */
:root {
  --accent: var(--color-violet-9);  /* 8d54ff */
  --success: #62ffb3;               /* brand mint */
}
```

**절대 하지 말아야 할 것 하나**: Resend를 "Inter-only + indigo CTA"로 만들지 말 것. Resend는 **세 개의 유료 커스텀 폰트**(Domaine serif, ABCFavorit sans, commitMono)를 self-host해서 editorial 느낌을 만든다. 폰트 없이는 완전히 다른 사이트가 된다. 또한 Radix Colors의 sand/slate/mauve/violet **alpha scale(a1-a12)**을 쓰는 게 핵심이다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://resend.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 445,690 bytes (Next.js SSR) |
| CSS files | 6개, 총 740,170자 |
| Custom props | 2,624 고유 `--*` 변수 |
| `@font-face` | 8 (domaine 3, aBCFavorit 2, commitMono 2, inter 1) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js + `next/font` self-host
- **Design system**: **Radix Colors** (sand/slate/mauve/violet/green/red/amber/blue/yellow/pink × 1-12 + a1-a12 alpha) + 자체 semantic layer
- **CSS architecture**: 3계층
  ```
  --{family}-{step}            raw Radix 12-step
  --{family}-a{step}           Radix alpha 12-step (semi-transparent)
  --color-{family}-{step}      semantic alias → raw var
  ```
- **Class naming**: Tailwind utility 주축
- **Default theme**: **light** · `--background: #fdfdfd`, `--foreground: #1d1c1b`
- **Font loading**: 8개 `@font-face` self-host, 유료 폰트 (Klim Type Foundry의 Domaine, Dinamo의 ABCFavorit)
- **Canonical anchor**: warm near-black `#1d1c1b` 본문 + violet accent `#8d54ff` + mint `#62ffb3`

---

## 04. Font Stack

- **Display (serif)**: `domaine` — Klim Type Foundry, 유료. editorial headline
- **Body (sans)**: `aBCFavorit` — Dinamo Typefaces, 유료. grotesk 본문
- **Mono**: `commitMono` — 유료 custom code font
- **Fallback sans**: Inter

```css
:root {
  --font-inter:       "inter";
  --font-abc-favorit: "aBCFavorit";
  --font-domaine:     "domaine";
  --font-commit-mono: "commitMono";
  --font-sans:    var(--font-inter), ui-sans-serif, system-ui, sans-serif;
  --font-display: var(--font-abc-favorit), ui-sans-serif, system-ui, sans-serif;
  --font-mono:    var(--font-commit-mono), ui-monospace, SFMono-Regular,
                  Menlo, Monaco, Consolas, monospace;
  --font-weight-light:    300;
  --font-weight-normal:   400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;
}
```

> **폰트 라이선스 주의**: Domaine + ABCFavorit + commitMono 모두 유료 상업 폰트. 오픈소스 대안은 `Cormorant Garamond` + `Inter` + `JetBrains Mono` 조합이 가장 가깝지만 완전 재현은 불가.

---

## 05. Typography Scale

| Token | rem | px | Line-height |
|---|---|---|---|
| `--text-xs`   | 0.75rem   | 12 | `calc(1 / .75)` ≈ 1.33 |
| `--text-sm`   | 0.875rem  | 14 | `calc(1.25 / .875)` ≈ 1.43 |
| `--text-base` | 1rem      | 16 | `calc(1.5 / 1)` = 1.5 |
| `--text-lg`   | 1.125rem  | 18 | 1.55 |
| `--text-xl`   | 1.25rem   | 20 | 1.4 |
| `--text-2xl`  | 1.5rem    | 24 | 1.33 |
| `--text-3xl`  | 1.875rem  | 30 | 1.2 |
| `--text-4xl`  | 2.25rem   | 36 | 1.1 |
| `--text-5xl`  | 3rem      | 48 | 1.05 |
| display       | `6rem`    | 96 | 1 |

---

## 06. Colors

### 06-1. Surface

| Token | Hex | Usage |
|---|---|---|
| `--background`  | `#fdfdfd` | 거의 화이트 (순백 아님) |
| `--foreground`  | `#1d1c1b` | warm near-black 본문 |
| dark hero bg    | `#05050a` | 다크 섹션 배경 |
| dark surface    | `#1d1c1b` / `#323232` / `#2a2a2a` | 다크 카드 |

### 06-2. Brand Mint

| Token | Hex |
|---|---|
| `--color-green-500` | `#00c758` |
| `--color-green-400` | `#05df72` |
| `--color-green-300` | `#7bf1a8` |
| mint bright         | `#62ffb3` ⭐ (빈도 20회 최상위) |

### 06-3. Radix Colors (12-step × 10 families × alpha)

Resend는 **Radix Colors**를 그대로 도입. 각 family마다:
- `--{family}-1 ~ 12` (solid)
- `--{family}-a1 ~ a12` (alpha, 배경 블렌딩용)
- `--color-{family}-*` (semantic alias layer)

Families: `sand · slate · mauve · violet · green · red · amber · blue · yellow · pink · fuchsia · lime · orange · cyan · emerald · neutral · zinc · gray`.

### 06-4. 주요 Tailwind-스타일 raw hex

| Token | Hex |
|---|---|
| `--color-red-500`    | `#fb2c36` |
| `--color-red-600`    | `#e40014` |
| `--color-orange-500` | `#fe6e00` |
| `--color-amber-500`  | `#f99c00` |
| `--color-yellow-500` | `#edb200` |
| `--color-yellow-300` | `#ffe02a` |
| `--color-green-500`  | `#00c758` |
| `--color-cyan-500`   | `#00b7d7` |
| `--color-blue-500`   | `#3080ff` |
| `--color-blue-600`   | `#155dfc` |
| `--color-violet-500` | `#8d54ff` ⭐ |
| `--color-fuchsia-500`| `#e12afb` |
| `--color-pink-500`   | `#f6339a` |

### 06-5. Dominant Colors

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#62ffb3` | 20 | mint bright (brand accent) |
| 2 | `#22c55e` | 14 | green-500 Tailwind |
| 3 | `#323232` | 12 | warm dark surface |
| 4 | `#9c6b2e` | 12 | tan / amber deep |
| 5 | `#f76004` | 12 | orange accent |
| 6 | `#2a2a2a` | 10 | dark panel |
| 7 | `#fdfdfd` | 9  | background |
| 8 | `#1d1c1b` | 8  | foreground |
| 9 | `#2bf2ff` | 8  | cyan brand secondary |
| 10 | `#05050a` | 8 | dark hero bg |

---

## 07. Spacing

```
--spacing: 0.25rem;  /* Tailwind base */
```

전용 spacing 변수는 `--spacing` 하나뿐. 나머지는 Tailwind `p-{n}` / `m-{n}` 유틸리티로 × `--spacing`.

---

## 08. Radius

| Token | Value |
|---|---|
| `--radius-xs`  | 0.125rem (2px) |
| `--radius-sm`  | 0.25rem (4px) |
| `--radius-md`  | 0.375rem (6px) |
| `--radius-lg`  | 0.5rem (8px) |
| `--radius-xl`  | 0.75rem (12px) |
| `--radius-2xl` | 1rem (16px) |
| `--radius-3xl` | 1.5rem (24px) |
| `--radius-4xl` | 2rem (32px) |

---

## 12. Components

### Editorial Hero
```html
<section style="background:#fdfdfd;padding:120px 64px;">
  <h1 style="font-family:'domaine',ui-serif,Georgia,serif;
             font-size:clamp(48px,7vw,96px);
             font-weight:400;line-height:1.02;
             letter-spacing:-0.025em;
             color:#1d1c1b;max-width:16ch;">
    Email for developers
  </h1>
  <p style="font-family:'aBCFavorit',sans-serif;
            font-size:18px;color:#323232;
            max-width:52ch;margin-top:24px;line-height:1.55;">
    The best email platform for developers.
  </p>
  <button style="font-family:'aBCFavorit',sans-serif;
                 font-weight:500;font-size:14px;
                 padding:12px 24px;margin-top:32px;
                 background:#1d1c1b;color:#fdfdfd;
                 border:none;border-radius:6px;">
    Get started
  </button>
</section>
```

### Code Block (commitMono)
```html
<pre style="font-family:'commitMono',ui-monospace,monospace;
            font-size:13px;background:#1d1c1b;color:#62ffb3;
            padding:20px 24px;border-radius:8px;">
  $ <span style="color:#fdfdfd">resend</span> send
</pre>
```

---

## 14. Drop-in CSS

```css
/* Resend — copy into your root stylesheet */
:root {
  /* Fonts (paid, self-hosted) */
  --font-sans:    "aBCFavorit", "Inter", ui-sans-serif, system-ui, sans-serif;
  --font-display: "domaine", "Cormorant Garamond", ui-serif, Georgia, serif;
  --font-mono:    "commitMono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;

  /* Surface */
  --background: #fdfdfd;
  --foreground: #1d1c1b;
  --dark-hero:  #05050a;
  --dark-panel: #2a2a2a;

  /* Brand accents */
  --accent-mint:   #62ffb3;   /* mint bright anchor */
  --accent-violet: #8d54ff;   /* violet-500 Radix */
  --accent-cyan:   #2bf2ff;
  --accent-orange: #f76004;

  /* Radix semantic shortcuts */
  --color-red-500:   #fb2c36;
  --color-green-500: #00c758;
  --color-blue-500:  #3080ff;
  --color-violet-500:#8d54ff;

  /* Radius */
  --radius-sm:  0.25rem;
  --radius-md:  0.375rem;
  --radius-lg:  0.5rem;
  --radius-xl:  0.75rem;
  --radius-2xl: 1rem;
}

body {
  font-family: var(--font-sans);
  background: var(--background);
  color: var(--foreground);
}

h1, .display {
  font-family: var(--font-display);
  font-weight: 400;
  letter-spacing: -0.02em;
}
```

---

## 16. DO / DON'T

### ✅ DO
- 3-font stack 유지: **Domaine serif** (display) + **ABCFavorit sans** (body) + **commitMono** (code).
- Background = `#fdfdfd` (순백 아님), foreground = `#1d1c1b` (warm near-black).
- Brand accent = `#62ffb3` mint (빈도 1위 20회). CTA highlight / logo glow.
- Radix Colors sand/slate/mauve/violet + alpha scale 12-step 구조 유지.
- `next/font`로 유료 폰트 self-host (라이선스 확인 필수).
- Hero headline은 **Domaine serif 400 weight**로 거대한 사이즈(clamp 48~96px).

### ❌ DON'T
- Inter-only로 대체 금지 — 3-font editorial 믹스가 시그니처.
- 순백 `#ffffff` 배경 금지 — warm `#fdfdfd`.
- 순검정 `#000` 본문 금지 — warm `#1d1c1b`.
- Tailwind color-{family}-500만 사용 금지 — Radix의 alpha scale(`a3`, `a9` 등)이 핵심.
- `indigo-500` CTA 금지 — Resend는 violet `#8d54ff`이나 mint `#62ffb3`이 accent.
- 유료 폰트를 Google Fonts 대체로 무단 치환 금지.
