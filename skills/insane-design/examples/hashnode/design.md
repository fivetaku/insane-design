---
slug: hashnode
service_name: Hashnode
site_url: https://hashnode.com
fetched_at: 2026-04-11
default_theme: light
brand_color: "#1D52DE"
primary_font: Suisse International
font_weight_normal: 400
token_prefix: tw
---

# DESIGN.md — Hashnode (Claude Code Edition)

---

## 01. Quick Start

> 5분 안에 Hashnode처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — Suisse International (next/font/local) */
body {
  font-family: var(--font-suisse-intl), system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}
code, pre {
  font-family: var(--font-suisse-mono), ui-monospace, "SF Mono", monospace;
}

/* 2. 배경 + 텍스트 — Tailwind slate 팔레트 */
:root {
  --bg: #ffffff;
  --fg: #101828;  /* slate-900 */
  --fg-muted: #4a5565; /* gray-600 */
  --border: #e5e7eb;   /* gray-200 */
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 블루 */
:root { --brand: #1D52DE; --brand-soft: #F5F9FF; }
a { color: var(--brand); }
```

**절대 하지 말아야 할 것 하나**: `Inter`나 `Fira Code`를 Hashnode 폰트로 쓰지 말 것. 실제로는 **Suisse International** (유료 Swiss Typefaces)와 **Suisse Mono**를 `next/font/local`로 로드한다. Inter는 비슷해 보이지만 Grotesque 계열 중에서도 완전히 다른 폰트여서 바로 티가 난다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://hashnode.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| Framework | Next.js + Tailwind CSS v4 |
| Custom props | 320 (color: 104 · spacing: 4 · shadow: 31 via `--tw-*`) |
| Token prefix | Tailwind v4 `@theme` — `--color-*`, `--spacing`, `--tw-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · Tailwind v4 `@theme` 기반 |

---

## 03. Tech Stack

- **Framework**: Next.js (`next/font/local` 로컬 폰트 + Tailwind v4)
- **Design system**: 자체 브랜드 토큰 없음. **Tailwind CSS v4** 기본 팔레트에 얇은 브랜드 레이어.
- **CSS architecture**: Tailwind v4 `@theme` 디렉티브
  ```
  :root에 전체 Tailwind 팔레트가 CSS 변수로 주입됨
  --color-{name}-{50..950}      slate/gray/red/green/emerald/blue... 104개
  --tw-{utility}                --tw-shadow, --tw-ring-shadow, --tw-space-y-reverse
  --spacing: 0.25rem             단일 base spacing (Tailwind v4 convention)
  ```
- **Class naming**: Tailwind 유틸리티 (`flex items-center gap-3 rounded-lg border border-gray-200 ...`). Semantic BEM 없음 — 컴포넌트는 유틸 클래스 조합으로 표현.
- **Default theme**: Light (bg `#ffffff`, fg `#101828`)
- **Font loading**: `next/font/local` + `--font-suisse-intl`, `--font-suisse-mono` CSS 변수 노출
- **Body typography**: `@tailwindcss/typography` (Prose 플러그인). 블로그 본문은 `.prose` 클래스가 em/% 단위 스케일을 주입.

---

## 04. Font Stack

- **Display / Body**: `Suisse International` (유료, Swiss Typefaces)
- **Code**: `Suisse Mono`
- **Icon**: `Font Awesome 7 Brands/Pro/Jelly/Jelly Fill`
- **Loading**: Next.js `next/font/local` → `--font-suisse-intl` / `--font-suisse-mono` CSS 변수

```css
:root {
  --font-suisse-intl: "suisseIntl";
  --font-suisse-mono: "suisseMono";
}
body {
  font-family: var(--font-suisse-intl), system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}
code, pre, kbd {
  font-family: var(--font-suisse-mono), ui-monospace, "SF Mono", Menlo, monospace;
}
```

> ⚠️ Suisse International은 라이선스가 있는 폰트다. OSS 대체로는 **Inter Tight**가 가장 가깝지만 그래도 다른 폰트다. 실제 Hashnode 룩을 원하면 Suisse를 구입하거나 `Söhne`/`GT America` 같은 다른 Swiss grotesque를 사용.

---

## 05. Typography Scale

Hashnode는 Tailwind Prose 플러그인의 em/% 기반 타이포를 쓴다. 블로그 본문의 모든 사이즈가 부모 폰트 사이즈에 비례.

| Token (Prose) | Size | Weight | Line-height |
|---|---|---|---|
| h1        | `2.25em`   | 800 | 1.1   |
| h2        | `1.5em`    | 700 | 1.25  |
| h3        | `1.25em`   | 600 | 1.35  |
| h4        | `1em`      | 600 | 1.5   |
| lead      | `1.25em`   | 400 | 1.6   |
| body      | `1em` (base 16-18px) | 400 | 1.75 |
| small     | `0.875em`  | 400 | 1.45  |
| kbd       | `0.875em`  | 500 | 1     |
| code      | `0.888889em` | 500 | 1.45 |

UI 사이즈 (마케팅 홈 관찰):

| Role | Size | Weight |
|---|---|---|
| hero-h1    | 56px | 700 |
| hero-h2    | 44px | 700 |
| nav-item   | 14px | 500 |
| button     | 14px | 600 |
| card-title | 18px | 600 |
| meta       | 12px | 500 |

> ⚠️ Weight 분포: 600 (15회), 700 (14회), 400 (13회) — semi-bold 강조 패턴. Inter 기본 400/500 조합보다 묵직한 느낌.

---

## 06. Colors

Hashnode는 **Tailwind v4 기본 팔레트**에 `#1D52DE` 브랜드 블루만 덮어쓴 구조. 독자적 컬러 시스템이 없다.

### 06-1. Brand

| Token | Hex | Usage |
|---|---|---|
| brand-primary  | `#1D52DE` | link / CTA (4회 실사용) |
| brand-soft-bg  | `#F5F9FF` | hero subtle bg / link hover |
| blue-600 (tw)  | `#155dfc` | 대체 파랑 (tailwind default) |

### 06-2. Neutral (Tailwind slate + gray 혼합)

| Token | Hex | Usage |
|---|---|---|
| bg-page       | `#ffffff`              | 페이지 배경 |
| bg-surface    | `#f1f5f9` (slate-100)  | 카드 배경 |
| bg-hover      | `#f5f9ff`              | 링크/버튼 hover 배경 |
| fg-primary    | `#101828` (slate-900)  | 본문 주 텍스트 |
| fg-deep       | `#0f172b` (slate-950)  | 헤딩 강조 |
| fg-secondary  | `#364153` (slate-700)  | 서브텍스트 |
| fg-muted      | `#4a5565` (gray-600)   | 메타 텍스트 |
| fg-tertiary   | `#62748e`              | placeholder |
| fg-disabled   | `#99a1af` (gray-400)   | 비활성 텍스트 |
| border-soft   | `#e5e7eb` (gray-200)   | 카드 경계 |
| border-strong | `#d1d5dc` (gray-300)   | 입력 경계 |
| hairline      | `#0000001a`            | 1px 알파 검정 (21회) |

### 06-3. Accent Families (Tailwind v4 default palette, 104 variables)

| Family | 50 | 500 | 900 |
|---|---|---|---|
| red     | `#fef2f2` | — | `#82181a` |
| orange  | — | — | `#9e320c` |
| amber   | `#fffbeb` | — | `#461901` |
| green   | `#f0fdf4` | — | `#0d4f1c` |
| emerald | `#ecfdf5` | — | `#064e3b` |
| blue    | — | `#155dfc` | — |
| slate   | — | `#62748e` | `#0f172b` |

**Key insight**: 전체 Tailwind 팔레트가 CSS 변수로 `:root`에 들어가 있어 Tailwind 유틸 클래스 없이도 `var(--color-green-500)` 형태로 참조 가능.

### 06-4. Semantic

| Token | Hex | Usage |
|---|---|---|
| link          | `#1D52DE` | 본문 링크 |
| success       | `#16a34a` (green-600) | check 아이콘 |
| danger        | `#dc2626` (red-600)   | error |
| warning       | `#d97706` (amber-600) | caution |
| selection-bg  | `#b3d4fc`             | 텍스트 선택 |

### 06-5. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#00000000` | 36 | 투명 |
| 2 | `#FFFFFF`   | 24 | bg |
| 3 | `#0000001A` | 21 | hairline (α10 검정) |
| 4 | `#101828`   | 12 | slate-900 text |
| 5 | `#364153`   |  8 | slate-700 |
| 6 | `#D1D5DC`   |  8 | gray-300 border |
| 7 | `#E5E7EB`   |  8 | gray-200 border |
| 8 | `#0F172B`   |  7 | slate-950 |
| 9 | `#4A5565`   |  6 | gray-600 |
| 10| `#99A1AF`   |  6 | gray-400 |

---

## 07. Spacing

Tailwind v4의 **단일 base spacing 패턴**: `--spacing: 0.25rem` (4px) 하나만 정의되고, 나머지는 유틸 클래스 `p-{n}`이 `calc(var(--spacing) * n)`으로 계산한다.

| Token | Value | Use case |
|---|---|---|
| `--spacing` | 0.25rem (4px) | base unit |
| `p-1`   | 4px   | tight |
| `p-2`   | 8px   | compact |
| `p-3`   | 12px  | button padding |
| `p-4`   | 16px  | card inner |
| `p-6`   | 24px  | section inner |
| `p-8`   | 32px  | block gap |
| `p-12`  | 48px  | section gap |
| `p-16`  | 64px  | large block |
| `p-24`  | 96px  | hero padding |

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| `rounded-xs`   | 2px  | 인라인 코드 |
| `rounded-sm`   | 4px  | 작은 버튼 |
| `rounded`      | 5px  | 기본 |
| `rounded-lg`   | 8px  | 카드, 버튼 |
| `rounded-xl`   | 12px | 모달 |
| `rounded-pill` | 38px | pill badge, avatar |

---

## 09. Shadows

Hashnode는 Tailwind v4의 `--tw-shadow` 내부 변수를 사용. 실제 elevation은 Tailwind 유틸 `shadow-sm/md/lg`로 대부분 표현.

| Level | Value | Usage |
|---|---|---|
| shadow-xs | `0 1px 2px 0 #0000000d`                         | subtle card |
| shadow-sm | `0 1px 3px 0 #0000001a, 0 1px 2px -1px #0000001a` | card |
| shadow-md | `0 4px 6px -1px #0000001a, 0 2px 4px -2px #0000001a` | popover |
| shadow-lg | `0 10px 15px -3px #0000001a, 0 4px 6px -4px #0000001a` | modal |
| kbd shadow| `0 0 0 1px #1018281a, 0 3px 0 #1018281a`        | keyboard key |

---

## 11. Layout Patterns

### Hero (marketing)
- Layout: 중앙 정렬, h1 단일 컬럼 + 아래 이메일 입력 CTA
- Background: `#ffffff` + `#F5F9FF` soft 그라디언트 오브
- H1: 56px / weight 700 / tracking -0.02em
- Max-width: 1200px

### Article (Prose)
- Max-width: `65ch` (prose default)
- Font-size: 18px base → em 단위로 스케일
- Line-height: 1.75

### Section Rhythm
```css
section { padding: 80px 24px; max-width: 1280px; margin-inline: auto; }
.prose { max-width: 65ch; font-size: 18px; line-height: 1.75; }
```

---

## 12. Components

### 12.1 Primary Button (Tailwind utility로 구성)

```html
<button class="inline-flex items-center gap-2 rounded-lg bg-[#1D52DE] px-5 py-2.5 text-sm font-semibold text-white hover:bg-blue-700 transition">
  Start writing
</button>
```

| Spec | Value |
|---|---|
| Background | `#1D52DE` |
| Hover | `#155dfc` (blue-600) |
| Text | `#ffffff` |
| Padding | `10px 20px` |
| Radius | 8px (rounded-lg) |
| Font weight | 600 |

### 12.2 Card

```html
<div class="rounded-lg border border-gray-200 bg-white p-6 shadow-sm">
  <h3 class="text-lg font-semibold text-slate-900">Post title</h3>
  <p class="mt-2 text-sm text-gray-600">meta · description</p>
</div>
```

### 12.3 Prose (Article body)

```html
<article class="prose prose-lg max-w-prose">
  <h1>...</h1>
  <p>...</p>
  <pre><code>...</code></pre>
  <kbd>⌘K</kbd>
</article>
```

Prose 플러그인이 em/% 기반 타이포 + kbd shadow + code 스타일을 자동 주입.

---

## 14. Drop-in CSS

```css
/* Hashnode — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-suisse-intl: "suisseIntl";
  --font-suisse-mono: "suisseMono";

  /* Brand */
  --color-brand:      #1D52DE;
  --color-brand-soft: #F5F9FF;

  /* Neutral (Tailwind slate + gray) */
  --color-bg:          #ffffff;
  --color-bg-surface:  #f1f5f9;
  --color-fg:          #101828;
  --color-fg-deep:     #0f172b;
  --color-fg-muted:    #4a5565;
  --color-fg-tertiary: #62748e;
  --color-border:      #e5e7eb;
  --color-border-strong:#d1d5dc;
  --color-hairline:    #0000001a;

  /* Spacing (Tailwind v4 pattern) */
  --spacing: 0.25rem;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 5px;
  --radius-lg: 8px;
  --radius-xl: 12px;
  --radius-pill: 38px;

  /* Shadow */
  --shadow-sm: 0 1px 3px 0 #0000001a, 0 1px 2px -1px #0000001a;
  --shadow-md: 0 4px 6px -1px #0000001a, 0 2px 4px -2px #0000001a;
  --shadow-lg: 0 10px 15px -3px #0000001a, 0 4px 6px -4px #0000001a;
}

body {
  background: var(--color-bg);
  color: var(--color-fg);
  font-family: var(--font-suisse-intl), system-ui, -apple-system, sans-serif;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
}
a { color: var(--color-brand); }
```

---

## 15. Tailwind Config

```js
// tailwind.config.js — Hashnode (Tailwind v4 @theme 대체)
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#1D52DE',
          soft: '#F5F9FF',
          600: '#155dfc',
        },
        // Tailwind slate + gray 팔레트를 그대로 사용
      },
      fontFamily: {
        sans: ['var(--font-suisse-intl)', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['var(--font-suisse-mono)', 'ui-monospace', 'SF Mono', 'Menlo', 'monospace'],
      },
      fontWeight: {
        normal:   '400',
        medium:   '500',
        semibold: '600',
        bold:     '700',
        black:    '800',
      },
      borderRadius: {
        sm: '4px', md: '5px', lg: '8px', xl: '12px', pill: '38px',
      },
      boxShadow: {
        sm: '0 1px 3px 0 #0000001a, 0 1px 2px -1px #0000001a',
        md: '0 4px 6px -1px #0000001a, 0 2px 4px -2px #0000001a',
        lg: '0 10px 15px -3px #0000001a, 0 4px 6px -4px #0000001a',
        kbd:'0 0 0 1px #1018281a, 0 3px 0 #1018281a',
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
```

---

## 16. DO / DON'T

### ✅ DO
- **Suisse International + Suisse Mono** 폰트를 사용. `next/font/local`로 로드하고 `--font-suisse-intl` CSS 변수로 노출.
- **Tailwind CSS v4** `@theme` 디렉티브를 쓰는 것이 기본. `--color-*-{N}` 팔레트가 전부 `:root`에 주입됨.
- 브랜드 블루는 **`#1D52DE`** (진한 블루) + `#F5F9FF` soft bg.
- Neutral은 Tailwind **slate/gray 팔레트**를 섞어서 사용. `#101828` (slate-900) / `#4a5565` (gray-600) / `#e5e7eb` (gray-200).
- 블로그 본문에 **Tailwind Prose 플러그인** 사용. em/% 단위 타이포.
- Hairline은 `#0000001a` (α10 검정). 21회 실사용 — 2번째로 많은 hex.
- Weight 600 (semibold)을 강조 기본값으로. 700/400과 섞어서 사용.

### ❌ DON'T
- ❌ `Inter`를 Hashnode 폰트로 쓰지 말 것 → 실제는 **Suisse International**. 실제 CSS에 Inter는 0회 등장.
- ❌ `Fira Code`를 코드 폰트로 쓰지 말 것 → 실제는 **Suisse Mono**.
- ❌ `#2962FF`를 Hashnode 브랜드 블루로 쓰지 말 것 → 실제는 `#1D52DE` (완전 허구 주장). 톤이 다르다.
- ❌ `#1C1C1C` / `#F5F5F5` / `#6C6C6C` 같은 허구 neutral 쓰지 말 것 → 실제는 Tailwind slate/gray.
- ❌ 본문 폰트를 **18px 절대값**으로 고정하지 말 것 → Prose의 em/% 컨벡션을 사용.
- ❌ 자체 브랜드 토큰 시스템을 만들지 말 것 → Hashnode는 **Tailwind 기본 팔레트 + 얇은 브랜드 덮기**가 설계 철학.
- ❌ BEM semantic 클래스 (`button-primary-bg`)를 찾지 말 것 → 없다. 모든 스타일은 **Tailwind 유틸리티 클래스**로 직접 주입.
