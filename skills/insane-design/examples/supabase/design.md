---
slug: supabase
service_name: Supabase
site_url: https://supabase.com
fetched_at: 2026-04-11
default_theme: dark
brand_color: "#3ECF8E"
primary_font: Custom (self-hosted "Circular" fallback)
font_weight_normal: 400
token_prefix: "--brand-*, --background-*, --foreground-*"
---

# DESIGN.md — Supabase (Claude Code Edition)

---

## 01. Quick Start

> 5분 안에 Supabase처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트: custom 변수 + Circular 폴백 */
body {
  font-family: var(--font-custom), "Circular", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}
code, pre {
  font-family: var(--font-source-code-pro), "Source Code Pro", "Office Code Pro", Menlo, monospace;
}

/* 2. 배경 + 텍스트 (dark 기본, HSL 2-theme system) */
:root {
  --background-default: 0deg 0% 7.1%;    /* #121212 */
  --foreground-default: 0deg 0% 98%;     /* #FAFAFA */
}
body { background: hsl(var(--background-default)); color: hsl(var(--foreground-default)); }

/* 3. 브랜드 그린 */
:root { --brand-default: 153.1deg 60.2% 52.7%; }  /* #3ECF8E — Supabase signature */
.btn-primary { background: hsl(var(--brand-default)); }
```

**절대 하지 말아야 할 것 하나**: Supabase 의 브랜드 그린을 `#00D874` 또는 Spotify 의 `#1ED760` 처럼 채도 높은 네온 그린으로 쓰지 말 것. 실제 CSS 에는 `#3ECF8E`(HSL `153deg 60% 53%`) — 채도 60% 의 <b>민트 톤</b> 이 canonical. 기본 페이지는 dark 이지만 light theme 도 완전 별도로 정의돼 있어 <code>hsl(var(--brand-default))</code> 래핑 패턴을 깨지 말 것.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://supabase.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | SSR marketing |
| CSS files | 2개 외부, 총 406,816자 |
| Primary bundle | `c5273c74d5406792.css` (Next.js hashed) |
| Token count | 788 custom properties · 512 color · 12 spacing · 8 shadow |
| Token prefix | `--brand-*`, `--background-*`, `--foreground-*`, `--border-*` (shadcn-style) |
| Method | HSL 값 + hex 빈도 카운트 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js + Tailwind CSS
- **Design system**: shadcn/ui + 자체 확장 token layer. Tailwind utilities + `hsl(var(--*))` 래핑.
- **CSS architecture**: HSL-based 2-theme (light + dark)
  ```
  --brand-{200..600, link, default, accent, button}    brand ramp (HSL)
  --background-{default, surface-75..400, alternative, selection}
  --foreground-{default, light, lighter, muted, contrast}
  --border-{default, strong, stronger, muted, alternative, control, overlay}
  --colors-{family}-{light|dark}-{100..1200}            Radix UI color 12-step
  ```
- **Class naming**: Tailwind arbitrary + shadcn `data-*` 속성. 시멘틱 클래스 `.bg-default`, `.text-foreground` 등.
- **Default theme**: **dark**. `--background-default: 0deg 0% 7.1%` ≈ `#121212`.
- **Font loading**: Next.js font loader. <code>--font-custom</code> CSS 변수(self-hosted Circular variant) + <code>--font-source-code-pro</code> code.
- **Canonical anchor**: `#3ECF8E` (HSL `153.1deg 60.2% 52.7%`) — `--brand-default`.

---

## 04. Font Stack

- **Display/body font**: Custom self-hosted via `--font-custom` CSS var (Circular clone)
- **Fallback chain**: `Circular`, `"Helvetica Neue"`, `Helvetica`, `Arial`, `sans-serif`
- **Code font**: `Source Code Pro` → `Office Code Pro` → `Menlo` (Ubuntu 4회 등장은 코드 블록 전용)
- **Weight normal / bold**: `400` / `700` (UI 에는 500/600 도 사용)

```css
:root {
  --font-custom: "Circular", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-source-code-pro: "Source Code Pro", "Office Code Pro", Menlo, monospace;
}
body {
  font-family: var(--font-custom);
  font-weight: 400;
}
code, pre, kbd {
  font-family: var(--font-source-code-pro);
}
```

> ⚠️ **Custom font 는 라이선스 폰트.** Supabase 는 Circular 또는 그 변형을 self-host 하며 폰트 파일은 공개되지 않음. 복제 시 <code>Inter</code> 또는 <code>Inter Tight</code> 를 fallback 으로 쓰되, x-height/자간에서 미묘한 차이가 있음을 인지할 것.

---

## 05. Typography Scale

| Size rem | px | Weight | Use case |
|---|---|---|---|
| `.75rem` | 12px | 400 | 캡션 · 코드 인라인 |
| `.875rem` | 14px | 400/500 | 본문 small · UI label |
| `1rem` | 16px | 400 | 본문 기본 (11회, 1위) |
| `1.125rem` | 18px | 500 | 본문 large |
| `1.25rem` | 20px | 600 | 카드 타이틀 |
| `1.5rem` | 24px | 600/700 | H4 (10회) |
| `1.875rem` | 30px | 700 | H3 |
| `2.25rem` | 36px | 700 | H2 (9회) |
| `3rem` | 48px | 700 | H1 |
| `3.75rem` | 60px | 800 | 대형 hero H1 |
| `4.5rem` | 72px | 800 | 풀블리드 hero |
| `6rem` | 96px | 900 | 랜딩 페이지 디스플레이 |

> ⚠️ **1rem + 1.5rem 2단이 본문 리듬.** Supabase 는 Tailwind 의 <code>text-*</code> 유틸리티를 그대로 쓰며, <code>text-base</code>(16px) 와 <code>text-2xl</code>(24px) 가 전체의 70% 가까이 차지합니다. H1 은 <code>text-5xl</code>(48px) 이상, 최대 <code>text-9xl</code>(96px) 까지.

---

## 06. Colors

### 06-1. Brand Green Ramp (HSL — dark theme)

| Token | HSL | Approx Hex | Role |
|---|---|---|---|
| `--brand-200` | `162deg 100% 2%` | `#000F07` | 최저 (배경 오버레이) |
| `--brand-300` | `155.1deg 100% 8%` | `#00291B` | |
| `--brand-400` | `155.5deg 100% 9.6%` | `#003124` | |
| `--brand-500` | `154.9deg 100% 19.2%` | `#006227` | |
| `--brand-600` | `154.9deg 59.5% 70%` | `#87E3B3` | hover (light) |
| `--brand-default` ★ | `153.1deg 60.2% 52.7%` | `#3ECF8E` | canonical |
| `--brand-link` | `155deg 100% 38.6%` | `#00C56F` | 링크 전용 (dark) |
| `--brand-accent` | (brand-accent 152) | — | accent variant |

### 06-2. Brand Green Ramp (HSL — light theme)

| Token | HSL | Approx Hex |
|---|---|---|
| `--brand-200` | `147.6deg 72.5% 90%` | `#D6F7E6` |
| `--brand-300` | `147.5deg 72% 80.4%` | `#ACEFCE` |
| `--brand-400` | `151.3deg 66.9% 66.9%` | `#74E0A9` |
| `--brand-500` | `155.3deg 78.4% 40%` | `#16B867` |
| `--brand-600` | `156.5deg 86.5% 26.1%` | `#098F4F` |
| `--brand-default` | `152.9deg 60% 52.9%` | `#3ECF8E` (동일) |
| `--brand-link` | `153.4deg 100% 36.7%` | `#00BB5D` |

### 06-3. Background (Surface tiers — dark)

| Token | HSL | Approx Hex | Usage |
|---|---|---|---|
| `--background-default` ★ | `0deg 0% 7.1%` | `#121212` | 페이지 배경 |
| `--background-surface-75` | `0deg 0% 9%` | `#171717` | 카드 base |
| `--background-surface-100` | `0deg 0% 12.2%` | `#1F1F1F` | 카드 elevated |
| `--background-surface-200` | `0deg 0% 12.9%` | `#212121` | 카드 highlight |
| `--background-surface-300` | `0deg 0% 16.1%` | `#292929` | 카드 hover |
| `--background-surface-400` | `0deg 0% 16.1%` | `#292929` | alternative |
| `--background-selection` | `0deg 0% 19.2%` | `#313131` | 선택 하이라이트 |

### 06-4. Background (Surface tiers — light)

| Token | HSL | Approx Hex |
|---|---|---|
| `--background-default` | `0deg 0% 100%` (gray-light-100) | `#FFFFFF` |
| `--background-surface-75` | `0deg 0% 100%` | `#FFFFFF` |
| `--background-surface-100` | `0deg 0% 98.8%` | `#FCFCFC` |
| `--background-surface-200` | `0deg 0% 95.3%` | `#F3F3F3` |
| `--background-surface-300` | `0deg 0% 92.9%` | `#EDEDED` |
| `--background-surface-400` | `0deg 0% 89.8%` | `#E5E5E5` |

### 06-5. Foreground (Text)

| Token | Dark HSL | Light HSL | Usage |
|---|---|---|---|
| `--foreground-default` | `0deg 0% 98%` (`#FAFAFA`) | gray-light-1200 | primary text |
| `--foreground-light` | `0deg 0% 70.6%` | `0deg 0% 32.2%` | secondary |
| `--foreground-lighter` | `0deg 0% 53.7%` | `0deg 0% 43.9%` | tertiary |
| `--foreground-muted` | `0deg 0% 30.2%` | `0deg 0% 69.8%` | muted · disabled |
| `--foreground-contrast` | `0deg 0% 8.6%` | `0deg 0% 98.4%` | 버튼 위 텍스트 (반전) |

### 06-6. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 28 | light surface |
| 2 | `#3ECF8E` | 8 | **브랜드** |
| 3 | `#1C1C1C` | 6 | dark surface variant |
| 4 | `#030A0C` | 5 | darker variant |
| 5 | `#1E1E1E` | 4 | surface hover |
| 6 | `#DFFFF1` | 4 | brand-200 light |
| 7 | `#EDEDED` | 3 | light surface-300 |
| 8 | `#0070F3` | 2 | accent blue (Vercel link 카피) |
| 9 | `#8B949E` | 2 | neutral text |
| 10 | `#F6F8FA` | 2 | github-style surface |

---

## 07. Spacing

> Tailwind 기본 스케일 사용 (`rem` 기반 0.25 배수). 커스텀 토큰 12 개는 `--xxl: 128`, `--content-width-screen-xl: 1128` 등 레이아웃 전용.

| Token | Value |
|---|---|
| space-1 | `.25rem` / 4px |
| space-2 | `.5rem` / 8px |
| space-3 | `.75rem` / 12px |
| space-4 | `1rem` / 16px |
| space-6 | `1.5rem` / 24px |
| space-8 | `2rem` / 32px |
| space-12 | `3rem` / 48px |
| space-16 | `4rem` / 64px |
| space-24 | `6rem` / 96px |
| `--xxl` | 128px (layout) |
| `--content-width-screen-xl` | 1128px |

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| `rounded-none` | 0 | — |
| `rounded-sm` | 2px | 미세 |
| `rounded` | 4px | 기본 |
| `rounded-md` | 6px | 버튼 · 인풋 |
| `rounded-lg` | 8px | 카드 |
| `rounded-xl` | 12px | 큰 카드 |
| `rounded-2xl` | 16px | hero 이미지 |
| `rounded-3xl` | 24px | 대형 feature card |
| `rounded-full` | 9999px | avatar · pill |

---

## 09. Shadows

| Token | Value | Usage |
|---|---|---|
| `shadow-sm` | `0 1px 2px 0 rgba(0,0,0,0.05)` | 미세 |
| `shadow` | `0 1px 3px 0 rgba(0,0,0,0.1), 0 1px 2px -1px rgba(0,0,0,0.1)` | 기본 |
| `shadow-md` | `0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)` | 카드 hover |
| `shadow-lg` | `0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1)` | 드롭다운 |
| `shadow-xl` | `0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1)` | 모달 |
| `shadow-2xl` | `0 25px 50px -12px rgba(0,0,0,0.25)` | 대형 오버레이 |

> 표준 Tailwind shadow 스케일 그대로. 8 개의 `--shadow-*` 토큰이 별도로 있지만 Tailwind 유틸리티로 주로 적용.

---

## 12. Components

### Button (primary)

```html
<button data-size="medium" class="bg-brand text-brand-accent hover:bg-brand-400 border-brand-500">
  Start your project
</button>
```

```css
/* 실제 스타일은 Tailwind 유틸 기반 */
button.bg-brand {
  background: hsl(var(--brand-default));     /* #3ECF8E */
  color: hsl(var(--foreground-contrast));    /* #0D0D0D 또는 #FAFAFA */
  border: 1px solid hsl(var(--brand-500));
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;  /* 6px */
  font-weight: 500;
}
button.bg-brand:hover {
  background: hsl(var(--brand-400));
}
```

### Card

```html
<div class="bg-surface-100 border border-default rounded-xl p-6">
  <h3 class="text-foreground font-medium">Authentication</h3>
  <p class="text-foreground-light">User sign-in built in.</p>
</div>
```

### Code block

```html
<pre class="bg-surface-200 border border-default rounded-lg p-4 font-mono text-sm">
  <code class="text-foreground-light">CREATE TABLE users ...</code>
</pre>
```

---

## 14. Drop-in CSS

```css
/* Supabase — dark theme default */
:root {
  /* Fonts */
  --font-custom: "Circular", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-source-code-pro: "Source Code Pro", "Office Code Pro", Menlo, monospace;

  /* Brand (anchor + 4 steps, HSL) */
  --brand-200: 162deg 100% 2%;
  --brand-300: 155.1deg 100% 8%;
  --brand-500: 154.9deg 100% 19.2%;
  --brand-default: 153.1deg 60.2% 52.7%;   /* ← canonical #3ECF8E */
  --brand-600: 154.9deg 59.5% 70%;

  /* Surfaces (dark default) */
  --background-default: 0deg 0% 7.1%;        /* #121212 */
  --background-surface-100: 0deg 0% 12.2%;   /* #1F1F1F */
  --background-surface-200: 0deg 0% 12.9%;   /* #212121 */
  --background-surface-300: 0deg 0% 16.1%;   /* #292929 */

  /* Foreground */
  --foreground-default: 0deg 0% 98%;          /* #FAFAFA */
  --foreground-light: 0deg 0% 70.6%;          /* #B4B4B4 */
  --foreground-muted: 0deg 0% 30.2%;          /* #4D4D4D */
  --foreground-contrast: 0deg 0% 8.6%;        /* 버튼 위 (반전) */
}

body {
  font-family: var(--font-custom);
  font-weight: 400;
  background: hsl(var(--background-default));
  color: hsl(var(--foreground-default));
}
.bg-brand { background: hsl(var(--brand-default)); }
.text-brand { color: hsl(var(--brand-default)); }
```

---

## 15. Tailwind Config

```js
// tailwind.config.js — Supabase (shadcn-style)
module.exports = {
  darkMode: ['class'],
  theme: {
    extend: {
      colors: {
        brand: {
          200:     'hsl(var(--brand-200) / <alpha-value>)',
          300:     'hsl(var(--brand-300) / <alpha-value>)',
          400:     'hsl(var(--brand-400) / <alpha-value>)',
          500:     'hsl(var(--brand-500) / <alpha-value>)',
          600:     'hsl(var(--brand-600) / <alpha-value>)',
          DEFAULT: 'hsl(var(--brand-default) / <alpha-value>)',
          link:    'hsl(var(--brand-link) / <alpha-value>)',
          accent:  'hsl(var(--brand-accent) / <alpha-value>)',
        },
        background: {
          DEFAULT:      'hsl(var(--background-default) / <alpha-value>)',
          alternative:  'hsl(var(--background-alternative-default) / <alpha-value>)',
          selection:    'hsl(var(--background-selection) / <alpha-value>)',
          'surface-75': 'hsl(var(--background-surface-75) / <alpha-value>)',
          'surface-100':'hsl(var(--background-surface-100) / <alpha-value>)',
          'surface-200':'hsl(var(--background-surface-200) / <alpha-value>)',
          'surface-300':'hsl(var(--background-surface-300) / <alpha-value>)',
          'surface-400':'hsl(var(--background-surface-400) / <alpha-value>)',
        },
        foreground: {
          DEFAULT:  'hsl(var(--foreground-default) / <alpha-value>)',
          light:    'hsl(var(--foreground-light) / <alpha-value>)',
          lighter:  'hsl(var(--foreground-lighter) / <alpha-value>)',
          muted:    'hsl(var(--foreground-muted) / <alpha-value>)',
          contrast: 'hsl(var(--foreground-contrast) / <alpha-value>)',
        },
        border: {
          DEFAULT:     'hsl(var(--border-default) / <alpha-value>)',
          strong:      'hsl(var(--border-strong) / <alpha-value>)',
          stronger:    'hsl(var(--border-stronger) / <alpha-value>)',
          muted:       'hsl(var(--border-muted) / <alpha-value>)',
          alternative: 'hsl(var(--border-alternative) / <alpha-value>)',
          control:     'hsl(var(--border-control) / <alpha-value>)',
          overlay:     'hsl(var(--border-overlay) / <alpha-value>)',
        },
      },
      fontFamily: {
        sans: ['var(--font-custom)', 'Circular', 'Helvetica Neue', 'sans-serif'],
        mono: ['var(--font-source-code-pro)', 'Source Code Pro', 'monospace'],
      },
    },
  },
};
```

---

## 16. DO / DON'T

### ✅ DO
- 브랜드 그린 `#3ECF8E`(HSL `153deg 60% 53%`). 채도 60% 의 민트 톤이지 네온 그린 아님.
- `hsl(var(--token) / <alpha-value>)` 래핑 패턴 사용 — shadcn/ui 컨벤션.
- Dark theme 기본. Light theme 도 완전 정의돼 있어 `.dark` 클래스로 토글 가능.
- 2-theme 기준으로 <code>--brand-*</code> 가 theme 에 따라 다른 HSL 값을 가짐 — 하드코딩 금지.
- Tailwind utilities 그대로 사용: `bg-surface-100`, `text-foreground-light`, `border-default`.
- Code 블록에는 `var(--font-source-code-pro)` — Source Code Pro 체인.
- Surface tiers 3단계 이상 사용: `surface-100`(카드) → `-200`(hover) → `-300`(active).

### ❌ DON'T
- ❌ `#00D874` / `#1ED760` / `#00FF88` 같은 네온 그린 (실제는 채도 60% 민트)
- ❌ `#3ECF8E` 를 raw hex 로만 써서 light/dark 테마 토글 무시 (HSL 래핑 필수)
- ❌ `Inter` 를 primary 로 (실제는 <code>--font-custom</code> = Circular variant. Inter 는 최후의 fallback)
- ❌ 단일 `--background` 토큰 가정 — 실제는 `default` + `surface-75/100/200/300/400` + `alternative` + `selection` 7단계
- ❌ `bg-gray-*` Tailwind 기본 grey 사용 — 실제는 `bg-foreground-muted` / `bg-surface-*` 시멘틱 토큰
- ❌ Shadow 단일 레이어 — Tailwind 기본 shadow 스케일 그대로 사용해야 함
- ❌ `--primary` / `--accent` / `--secondary` (shadcn default) 가정 — Supabase 는 `--brand-*` prefix
- ❌ HSL 래퍼 없이 `background: var(--background-default)` 쓰기 — HSL 단편이라 반드시 `hsl()` 함수 래핑
