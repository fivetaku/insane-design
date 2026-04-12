---
slug: axiom
service_name: Axiom
site_url: https://axiom.co
fetched_at: 2026-04-11
default_theme: dark
brand_color: "#DA5C2C"
primary_font: BerkeleyMono
font_weight_normal: 400
token_prefix: tw
---

# DESIGN.md — Axiom (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Axiom처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — monospace brand */
body {
  font-family: "BerkeleyMono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-weight: 400;
}

/* 2. 다크 배경 + 화이트 텍스트 */
:root { --bg: #111827; --fg: #FFFFFF; --muted: #9CA3AF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 오렌지 액센트 (CTA / chart lines) */
:root { --accent: #DA5C2C; }
```

**절대 하지 말아야 할 것 하나**: Axiom의 브랜드는 **monospace 타이포그래피** (`BerkeleyMono`)다. `Inter` 같은 sans-serif로 본문을 쓰면 옵저버빌리티 도구 특유의 "터미널 / SRE 감성"이 완전히 사라진다. 그리고 브랜드 CTA는 보라가 아니라 오렌지 `#DA5C2C`.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://axiom.co` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| CSS files | 1개 (Tailwind dist, 114,462자) |
| Custom properties | 211개 (대부분 `--tw-*` prose 유틸) |
| Color vars | 10개 (tw-prose 기반) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js marketing site + Tailwind CSS v3
- **Design system**: Tailwind prose/typography 플러그인 기반 — 별도 커스텀 DS 없음
- **CSS architecture**: 유틸리티-퍼스트
  ```
  tailwind tier   (.bg-neutral-900, .text-gray-500)  실제 스타일링 API
  prose tier      (--tw-prose-*, --tw-prose-invert-*) long-form 콘텐츠
  custom props    (--tw-ring-*, --tw-shadow, --tw-space-*) 유틸 내부 바인딩
  ```
- **Class naming**: 순수 Tailwind 유틸 클래스 (`bg-neutral-900 text-white font-mono`)
- **Default theme**: **다크** (페이지 배경 `#111827` / `#171717` — Tailwind neutral-900)
- **Font loading**: self-hosted BerkeleyMono variable font (woff2)
- **Canonical anchor**: 단일 브랜드 컬러 없음. 오렌지 `#DA5C2C`가 가장 두드러진 accent (hero CTA / chart data points)
- **이 문서의 스코프**: `axiom.co` 마케팅 페이지 기준. `app.axiom.co` dashboard는 별개 앱으로 더 풍부한 Radix UI 기반 DS 보유 (본 문서 스코프 밖)

---

## 04. Font Stack
<!-- SOURCE: auto -->

- **Primary font**: `BerkeleyMono` (U.S. Graphics Company, paid license) — 브랜드 핵심 monospace
- **Fallback sans**: `Inter`
- **Code in prose**: 동일 `BerkeleyMono` (브랜드 통일)

```css
:root {
  --font-mono: "BerkeleyMono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --font-sans: "Inter", ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
body {
  font-family: var(--font-mono); /* Axiom = monospace brand */
  font-weight: 400;
}
```

> Berkeley Mono는 유료 폰트. 대체 후보: `JetBrains Mono`, `IBM Plex Mono`, `Fira Code`. 시각 근접도는 `JetBrains Mono > Fira Code > IBM Plex Mono`.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Class (Tailwind) | Size | Weight | Usage |
|---|---|---|---|
| `text-6xl` | 3.75rem (60px) | 700 | 히어로 디스플레이 |
| `text-5xl` | 3rem (48px)    | 700 | 섹션 헤드 |
| `text-4xl` | 2.25rem (36px) | 600 | 피처 제목 |
| `text-3xl` | 1.875rem (30px)| 600 | 서브섹션 |
| `text-2xl` | 1.5rem (24px)  | 600 | 카드 제목 |
| `text-xl`  | 1.25rem (20px) | 500 | lead body |
| `text-lg`  | 1.125rem (18px)| 500 | sub-heading |
| `text-base`| 1rem (16px)    | 400 | body |
| `text-sm`  | 0.875rem (14px)| 400 | 보조 text |
| `text-xs`  | 0.75rem (12px) | 400 | caption / meta |

> ⚠️ 전체 스케일이 **monospace**라 equivalent size에서 sans-serif보다 x-height가 낮고 폭이 일정. hero에서 매우 독특한 리듬. weight 축은 `400 / 500 / 600 / 700 / 900` 5단계 사용.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-3. Neutral Ramp (Tailwind neutral + gray 혼합)
<!-- SOURCE: auto -->

| Step | neutral (실제 bg) | gray (실제 text) |
|---|---|---|
| 950 | `#0a0a0a` | `#030712` |
| 900 | `#171717` ⭐ | `#111827` ⭐ |
| 800 | `#262626` | `#1f2937` |
| 700 | `#404040` | `#374151` |
| 600 | `#525252` | `#4b5563` |
| 500 | `#737373` | `#6b7280` |
| 400 | `#a3a3a3` | `#9ca3af` |
| 300 | `#d4d4d4` | `#d1d5db` |
| 200 | `#e5e5e5` | `#e5e7eb` |
| 100 | `#f5f5f5` | `#f3f4f6` |

> Axiom은 Tailwind의 `neutral` (warm gray) + `gray` (cool gray) 두 램프를 모두 사용. 페이지 bg는 `#111827` (gray-900, cool tone), 카드/코드블록 bg는 `#171717` (neutral-900, 더 중립).

### 06-4. Accent Families
<!-- SOURCE: auto -->

| Family | Key step | Hex | Usage |
|---|---|---|---|
| **orange** ⭐ | 600 | `#DA5C2C` | hero CTA, chart highlight |
| **blue** | 600 | `#2563EB` | link / button secondary |
| **red** | severity | `#E5484D` | error / critical log |
| **green** | severity | `#29A383` | success / healthy |
| **blue-severity** | info | `#0090FF` | info badge |

### 06-5. Semantic (VS Code syntax — code blocks)
<!-- SOURCE: auto -->

Axiom은 옵저버빌리티 도구라 code highlighting 자체가 브랜드 자산. 실제 CSS에 등장하는 syntax 컬러:

| Token | Hex | Syntax role |
|---|---|---|
| keyword | `#569CD6` | `if`, `return` (VS Code blue) |
| type | `#4EC9B0` | class/type name (VS Code teal) |
| variable | `#9CDCFE` | identifier (VS Code light blue) |
| string | `#CE9178` | string literal |
| comment | `#6A9955` | comment |
| number | `#B5CEA8` | numeric literal |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto -->

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 22 | text on dark |
| 2 | `#6B7280` | 6 | gray-500 text-muted |
| 3 | `#111827` | 6 | gray-900 page bg |
| 4 | `#171717` | 6 | neutral-900 card bg |
| 5 | `#D4D4D4` | 6 | neutral-300 border-subtle |
| 6 | `#9CA3AF` | 5 | gray-400 text-subtle |
| 7 | `#E8E8E8` | 4 | hairline border |
| 8 | `#2563EB` | 4 | blue-600 link |
| 9 | `#DA5C2C` | 4 | **brand orange** |
| 10 | `#569CD6` | 4 | VS Code syntax blue |

---

## 07. Spacing
<!-- SOURCE: auto -->
<!-- Tailwind 기본 spacing 스케일 사용 · 커스텀 토큰 없음 -->

| Token | Value | Use case |
|---|---|---|
| `.p-1` / `.gap-1` | 0.25rem (4px) | hairline |
| `.p-2` | 0.5rem (8px) | button inner |
| `.p-3` | 0.75rem (12px) | dense list |
| `.p-4` | 1rem (16px) | card padding |
| `.p-6` | 1.5rem (24px) | section internal |
| `.p-8` | 2rem (32px) | section gap |
| `.p-12` | 3rem (48px) | hero padding |
| `.p-16` | 4rem (64px) | page rhythm |
| `.p-24` | 6rem (96px) | large hero |

> 실제 `--tw-*` spacing custom property는 5개 (`--tw-space-x-reverse`, `--tw-border-spacing-*` 등). Axiom은 spacing을 유틸 클래스로 전부 처리하고 토큰 변수로 노출하지 않는다.

---

## 08. Radius
<!-- SOURCE: auto (raw px frequency) -->

| Value | Count | Context |
|---|---|---|
| `4px` | 13 | button · card · input (거의 전부) |
| `3px` | 1  | input inner |
| `2.5px`| 1 | badge |
| `2px` | 1  | hairline accent |
| `8px` | 1  | modal / large card |
| `9999px` | 1 | pill / avatar |

> Axiom은 라운드를 거의 쓰지 않는다. `4px` 일관 사용 — terminal/dashboard 감성 유지.

---

## 09. Shadows
<!-- SOURCE: auto -->

| Value | Usage |
|---|---|
| `0 0 0 1px rgb(17 24 39 / 10%), 0 3px 0 rgb(17 24 39 / 10%)` | kbd (키 캡 표시) |
| `none` | **기본값** — Axiom은 대부분 shadow 없는 flat 디자인 |
| `var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow)` | Tailwind ring 유틸 (focus state만) |

> **패턴**: Axiom은 elevation 없이 border만으로 레이어를 구분. terminal 감성 유지를 위한 의도적 선택.

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary CTA
- **Background**: `#DA5C2C` (orange-600)
- **Hover**: 더 짙은 오렌지 (Tailwind orange-700 `#C2410C`)
- **Text**: `#FFFFFF`
- **Radius**: `4px`
- **Font**: `BerkeleyMono` 14px / 500
- **Padding**: `0.5rem 1rem` (py-2 px-4)

```html
<button class="bg-orange-600 text-white font-mono px-4 py-2 rounded">
  Start free
</button>
```

### Code block (signature component)
- **Background**: `#171717` (neutral-900)
- **Text**: `#D4D4D4` (neutral-300)
- **Border**: `1px solid #262626` (neutral-800)
- **Syntax colors**: VS Code 계열 (`#569CD6` / `#4EC9B0` / `#9CDCFE` / `#CE9178`)
- **Font**: `BerkeleyMono` 14px / 400 / line-height 1.6

### Severity badge
- **red** (critical): `#E5484D` bg, white text
- **green** (healthy): `#29A383` bg, white text
- **blue** (info): `#0090FF` bg, white text
- **Radius**: `4px`, Font: BerkeleyMono 12px / 500

### Link
- **Color**: `#2563EB` (blue-600)
- **Hover**: underline + `#1D4ED8` (blue-700)

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Axiom — copy into your root stylesheet */
:root {
  /* Brand fonts (monospace-first) */
  --font-mono: "BerkeleyMono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --font-sans: "Inter", ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;

  /* Backgrounds (dark-first) */
  --bg-page:   #111827; /* gray-900 */
  --bg-card:   #171717; /* neutral-900 */
  --bg-raise:  #262626; /* neutral-800 */

  /* Text */
  --fg:         #FFFFFF;
  --fg-subtle:  #D4D4D4; /* neutral-300 */
  --fg-muted:   #9CA3AF; /* gray-400 */
  --fg-dim:     #6B7280; /* gray-500 */

  /* Borders */
  --border-soft: #262626;
  --border:      #404040;

  /* Accents */
  --accent-orange: #DA5C2C; /* brand CTA */
  --accent-blue:   #2563EB; /* link */

  /* Severity (Radix-ish) */
  --sev-red:   #E5484D;
  --sev-green: #29A383;
  --sev-blue:  #0090FF;

  /* Radius */
  --radius:      4px;
  --radius-pill: 9999px;
}

body {
  font-family: var(--font-mono);
  font-weight: 400;
  background: var(--bg-page);
  color: var(--fg);
}

code, pre { font-family: var(--font-mono); }
a { color: var(--accent-blue); }
.btn-primary { background: var(--accent-orange); color: #fff; border-radius: var(--radius); padding: 0.5rem 1rem; }
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Axiom
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#DA5C2C', // hero CTA orange
          600:     '#DA5C2C',
          700:     '#C2410C',
        },
        severity: {
          red:   '#E5484D',
          green: '#29A383',
          blue:  '#0090FF',
        },
        // Axiom uses Tailwind's built-in neutral + gray ramps;
        // no overrides needed, just rely on neutral-{900,800,300} and gray-{900,500,400}.
      },
      fontFamily: {
        mono: ['"BerkeleyMono"', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'monospace'],
        sans: ['"Inter"', 'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
      },
      fontWeight: {
        normal:  '400',
        medium:  '500',
        semibold:'600',
        bold:    '700',
      },
      borderRadius: {
        DEFAULT: '4px',
        sm:      '2px',
        md:      '4px',
        lg:      '8px',
        full:    '9999px',
      },
      boxShadow: {
        // Axiom is largely shadow-free. Only ring on focus.
        none: 'none',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- `BerkeleyMono`를 **본문 폰트**로 사용. Axiom의 브랜드 핵심 차별 요소.
- 다크 배경 `#111827` (gray-900) + 카드 `#171717` (neutral-900) 투톤 구분.
- 오렌지 `#DA5C2C`를 hero CTA와 차트 데이터 포인트에 액센트로 사용.
- 코드 블록은 `#171717` bg + VS Code 계열 syntax colors (`#569CD6`, `#4EC9B0`, `#9CDCFE`).
- shadow-less flat 디자인. 레이어는 border로만 구분 — terminal 감성 유지.
- radius는 `4px` 일관 사용. 라운드 거의 없음.
- severity badge는 Radix 컬러 계열 (`#E5484D`, `#29A383`, `#0090FF`).
- Tailwind 유틸 클래스 (`.bg-neutral-900`, `.text-gray-500`)를 직접 사용 — 토큰 변수 레이어 없음.

### ❌ DON'T
- ❌ `Inter`나 sans-serif 본문 — Axiom은 monospace 브랜드. sans로 바꾸면 "또 하나의 YC 스타트업 랜딩"처럼 보인다.
- ❌ 보라색 브랜드 (`#AE4DFF` 같은 건 axiom.co CSS에 0회). 오렌지 `#DA5C2C`가 유일한 브랜드 accent.
- ❌ 화려한 그라디언트 / glow — Axiom은 의도적으로 flat.
- ❌ `color-brand`, `color-surface` 같은 semantic 토큰 변수 기대 — Axiom 마케팅은 순수 Tailwind 유틸만 사용.
- ❌ 라이트 테마 기본값 — Axiom은 다크 퍼스트 (`#111827`이 bg).
- ❌ sans-serif와 monospace 혼용 — 전체가 mono여야 Axiom 특유의 질감이 나온다.
- ❌ `app.axiom.co` dashboard의 Radix/shadcn 요소를 마케팅 페이지에 가져오기 — 별개 앱이다.
- ❌ Shadow-heavy 카드 — Axiom은 shadow 거의 0 (`kbd` 제외).
