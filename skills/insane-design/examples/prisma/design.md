---
slug: prisma
service_name: Prisma
site_url: https://prisma.io
fetched_at: 2026-04-11
default_theme: light
brand_color: "#16a394"
primary_font: Mona Sans VF
font_weight_normal: 400
token_prefix: ""
---

# DESIGN.md — Prisma (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Prisma의 웹사이트는 밝고 깔끔한 배경 위에 기술적 도식과 코드 예시가 결합된 개발자 친화적 디자인이다. ORM/데이터베이스 도구로서의 구조적 명확성이 시각 디자인에 그대로 반영된다.

타이포그래피는 기본 시스템 서체를 사용한다. 본문 weight는 **400**이며, 코드 블록이 시각적으로 많은 비중을 차지하는 개발자 중심 레이아웃이다.

브랜드 다크블루 `#2D3748`가 CTA와 핵심 요소에 사용된다. 배경과 텍스트의 대비가 충분하면서도 부드러운 컬러 팔레트로 기술 문서의 가독성을 확보한다.

**Key Characteristics:**
- Primary = **`#16a394`** (anchor teal). CTA/링크/포커스 모두 teal 계열.
- Mona Sans VF self-host + `cv01/cv02/cv06` feature 설정으로 대문자 형태 맞춤.
- 제품별 color family 활용: Postgres = teal (ppg), ORM = indigo (orm).
- shadcn `--background`/`--foreground`/`--primary` 네이밍 준수 (Fumadocs와 호환).
- 본문 색은 딥 네이비 `#1d242f`로. 순검정 아님.
---

## 01. Quick Start

> 5분 안에 Prisma처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Mona Sans VF (GitHub의 OFL 가변 폰트) */
body {
  font-family: "Mona Sans VF", "Inter", "Roboto",
               "Helvetica Neue", "Arial", sans-serif;
  font-family-settings: "cv01" on, "cv02" on, "cv06" on;
  font-weight: 400;
}

/* 2. 차가운 배경 + 딥 네이비 텍스트 */
:root { --background: #fff; --foreground: #1d242f; }
body { background: var(--background); color: var(--foreground); }

/* 3. Teal 프라이머리 (구 indigo 아님) */
:root {
  --primary: #16a394;          /* Prisma 신 브랜드 teal */
  --primary-foreground: #fff;
  --accent-foreground: #154f47; /* 딥 teal text */
}
```

**절대 하지 말아야 할 것 하나**: Prisma를 indigo/violet `#6366f1`로 칠하지 말 것. Prisma는 Postgres 제품군(Prisma Postgres) 출시 이후 브랜드를 teal 계열로 재편했다. 실제 사이트에서 `--primary: #16a394`, 데이터 viz accent는 `#14b8a6 / #0d9488`이다. 구 indigo(`orm-reverse #6366f1`)는 ORM 제품 색으로 여전히 남지만, primary 브랜드는 teal이다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://prisma.io` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 437,800 bytes (Next.js SSR) |
| CSS files | 2개, 총 238,938자 |
| Custom props | 411 고유 `--*` 변수 |
| `@font-face` | 11 (Mona Sans VF, Mona Sans Mono VF) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Next.js 마케팅 + Fumadocs 기반 문서 시스템
- **Design system**: **shadcn/ui** 파생 (`--color-fd-*` 네임스페이스 = Fumadocs, `--primary`/`--foreground` = shadcn) + 자체 product-color layer
- **CSS architecture**: 3계층
  ```
  Tailwind ramps       (--color-teal-400, --color-gray-500)   raw
  Product semantic     (--color-background-ppg, -orm, -error) 제품별 color 그룹
  shadcn semantic      (--primary, --foreground, --muted)     표면
  ```
- **Product color families**:
  - `ppg` = Prisma Postgres Gateway → **teal** (`#14b8a6`, `#0d9488`, `#99f6e4`)
  - `orm` = ORM → **indigo** (`#4f46e5`, `#6366f1`, `#c7d2fe`)
  - error → red, success → teal, warning → orange
- **Default theme**: light (`bg = #fff`, `fg = #1d242f`) · dark variant 완비
- **Font loading**: 11개 `@font-face`, Mona Sans VF + Mona Sans Mono VF self-host
- **Canonical anchor**: `--primary: #16a394` (anchor teal)

---

## 04. Font Stack

- **Display font**: `Mona Sans VF` (OFL by GitHub, `ss01`, `ss02`, `ss05`, `ss06` features on)
- **Code font**: `Mona Sans Mono VF` (OFL)
- **Fallback chain**: `"Inter", "Roboto", "Helvetica Neue", "Arial Nova", "Nimbus Sans", "Arial", sans-serif`
- **Weights**: 400 / 500 / 600 / 700 / 800 / 900 (full variable axis)

```css
:root {
  --font-sans: "Inter", "Roboto", "Helvetica Neue",
               "Arial Nova", "Nimbus Sans", "Arial", sans-serif;
  --font-mono: "Mona Sans Mono VF", ui-monospace, "Cascadia Code",
               "Source Code Pro", "Menlo", "Consolas", monospace;
  --font-sans-display: "Mona Sans VF", "Inter", "Roboto", sans-serif;
  --font-sans-display-settings: "ss01" on, "ss02" on, "ss05" on, "ss06" on;
  --font-sans-settings: "cv01" on, "cv02" on, "cv06" on, "cv07" on, "cv08" on, "cv10" on;
}
```

> Mona Sans는 GitHub가 OFL로 공개한 가변 폰트다. 자유 사용 가능하지만 OpenType feature 설정(`cv01-cv10`, `ss01-ss06`)까지 맞춰야 Prisma 시각적 느낌이 재현된다.

---

## 05. Typography Scale

| Token | Size | Line-height |
|---|---|---|
| `--text-xs`  | 0.75rem  | 1rem |
| `--text-sm`  | 0.875rem | 1.25rem |
| `--text-base`| 1rem     | 1.5 |
| `--text-lg`  | 1.125rem | 1.75rem |
| `--text-xl`  | 1.25rem  | 1.75rem |
| `--text-2xl` | 1.5rem   | 2rem |
| `--text-3xl` | 1.875rem | 2.25rem |
| `--text-4xl` | 2.5rem   | 3rem |
| `--text-5xl` | 4rem     | 4.5rem |
| `--text-6xl` | 3.75rem  | 1 |
| `--text-7xl` | 4.5rem   | 1 |

Weight: `--font-weight-normal: 400`, `-medium: 500`, `-semibold: 600`, `-bold: 700`, `-extrabold: 800`, `-black: 900`.

---

## 06. Colors

### 06-1. shadcn semantic (top layer)

| Token | Hex | Usage |
|---|---|---|
| `--background`          | `#fff`    | 페이지 배경 |
| `--foreground`          | `#1d242f` | 본문 텍스트 (딥 네이비) |
| `--primary`             | `#16a394` | ⭐ **브랜드 teal** (CTA) |
| `--primary-foreground`  | `#fff`    | teal CTA 위 텍스트 |
| `--secondary-foreground`| `#1d242f` | |
| `--muted-foreground`    | `#718096` | |
| `--accent-foreground`   | `#154f47` | 딥 teal 강조 텍스트 |

### 06-2. Product Family — PPG (Prisma Postgres) = Teal

| Token | Hex |
|---|---|
| `--color-background-ppg`                | `#f0fdfa` (pale) |
| `--color-background-ppg-strong`         | `#ccfbf1` |
| `--color-background-ppg-reverse`        | `#14b8a6` ⭐ |
| `--color-background-ppg-reverse-strong` | `#0d9488` |
| `--color-foreground-ppg`                | `#0d9488` |
| `--color-foreground-ppg-weak`           | `#14b8a6` |
| `--color-foreground-ppg-strong`         | `#0f766e` |
| `--color-foreground-ppg-reverse-weak`   | `#99f6e4` |

### 06-3. Product Family — ORM = Indigo

| Token | Hex |
|---|---|
| `--color-background-orm`         | `#eef2ff` |
| `--color-background-orm-strong`  | `#e0e7ff` |
| `--color-background-orm-reverse` | `#6366f1` |
| `--color-background-orm-reverse-strong` | `#4f46e5` |
| `--color-foreground-orm`         | `#4f46e5` |
| `--color-foreground-orm-strong`  | `#4338ca` |
| `--color-foreground-orm-reverse-weak` | `#c7d2fe` |

### 06-4. Semantic (error / success / warning)

| Family | Key hex |
|---|---|
| error   | `--color-foreground-error #dc2626`, `-reverse #ef4444` |
| success | `--color-foreground-success #0d9488` (teal, 아님 green!) |
| warning | `--color-foreground-warning #ea580c`, `-reverse #f97316` |

### 06-5. Product Accent Families (9 colors)

각 family마다 `background / background-strong / foreground / foreground-strong / foreground-weak / reverse` 6단계 slot. family: `cyan · fuchsia · lime · pink · purple · sky · violet · yellow · blue`.

예시: `--color-foreground-sky: #0284c7`, `--color-background-sky-strong: #0c4a6e`.

### 06-6. Dominant Colors (실제 DOM 빈도)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#1d242f` | 10 | foreground 본문 |
| 2 | `#f9fafb` | 9  | gray-50 배경 |
| 3 | `#16a394` | 9  | **primary teal** |
| 4 | `#0d9488` | 8  | ppg strong / foreground-success |
| 5 | `#14b8a6` | 7  | ppg-reverse |
| 6 | `#2dd4bf` | 6  | foreground-success-strong |
| 7 | `#6366f1` | 4  | orm-reverse (indigo) |

---

## 07. Spacing

| Token | Value |
|---|---|
| `--spacing`          | `0.25rem` (4px) |
| `--spacing-element-2xs` | `0.75rem` |
| `--spacing-element-xs`  | `1rem` |
| `--spacing-element-sm`  | `1.25rem` |
| `--spacing-element-md`  | `1.5rem` |
| `--spacing-element-lg`  | `1.75rem` |
| `--spacing-element-xl`  | `2rem` |
| `--spacing-element-2xl` | `2.25rem` |
| `--spacing-element-3xl` | `2.5rem` |
| `--spacing-element-4xl` | `3rem` |
| `--spacing-element-5xl` | `4rem` |
| `--gap`              | `1rem` |

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| `--radius`            | `0.5rem` | 기본 anchor (shadcn 관례) |
| `--radius-md`         | `calc(var(--radius) - 2px)` | 버튼 |
| `--radius-lg`         | `var(--radius)` | 카드 |
| `--radius-square-low` | `0.1875rem` | 인라인 칩 |
| `--radius-square`     | `0.375rem` | 중간 |
| `--radius-square-high`| `0.75rem` | 큰 카드 |
| `--radius-circle`     | `999px` | 아바타, pill |

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Breakpoint | Width | Key Changes |
|---|---|---|
| Mobile | <640px | 단일 컬럼, 헤딩 축소, 카드 스택 |
| Tablet | 640-1024px | 2열 그리드, 중간 패딩 |
| Desktop | 1024-1280px | 풀 레이아웃, 3열 그리드 |
| Large | >1280px | 중앙 정렬 max-width 1200px, 넉넉한 마진 |

> ⚠️ Prisma는 모바일 퍼스트 반응형 디자인을 채택하며, 브레이크포인트별로 그리드와 타이포그래피가 유동적으로 조정된다.

---

## 13. Components

### Primary CTA
```html
<button class="bg-[#16a394] text-white font-semibold
               px-4 py-2 rounded-md
               hover:bg-[#0d9488] transition">
  Start for free
</button>
```

### Product Badge (PPG / ORM)
```html
<span class="inline-flex items-center px-2 py-0.5
             bg-[#f0fdfa] text-[#0d9488]
             border border-[#99f6e4] rounded">
  Prisma Postgres
</span>

<span class="inline-flex items-center px-2 py-0.5
             bg-[#eef2ff] text-[#4f46e5]
             border border-[#c7d2fe] rounded">
  Prisma ORM
</span>
```

---

## 15. Drop-in CSS

```css
/* Prisma — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-sans-display: "Mona Sans VF", "Inter", "Roboto",
                       "Helvetica Neue", "Arial", sans-serif;
  --font-sans: "Inter", "Roboto", "Helvetica Neue", "Arial", sans-serif;
  --font-mono: "Mona Sans Mono VF", ui-monospace, "Cascadia Code", monospace;
  --font-sans-settings: "cv01" on, "cv02" on, "cv06" on, "cv07" on;
  --font-sans-display-settings: "ss01" on, "ss02" on, "ss05" on, "ss06" on;

  /* shadcn base */
  --background: #fff;
  --foreground: #1d242f;
  --primary: #16a394;              /* brand teal */
  --primary-foreground: #fff;
  --accent-foreground: #154f47;
  --muted-foreground: #718096;

  /* Product: Prisma Postgres (ppg) */
  --ppg-bg: #f0fdfa;
  --ppg-bg-strong: #ccfbf1;
  --ppg-reverse: #14b8a6;
  --ppg-fg: #0d9488;

  /* Product: Prisma ORM */
  --orm-bg: #eef2ff;
  --orm-bg-strong: #e0e7ff;
  --orm-reverse: #6366f1;
  --orm-fg: #4f46e5;

  /* Radius */
  --radius: 0.5rem;
  --radius-md: calc(var(--radius) - 2px);
  --radius-lg: var(--radius);
}

body {
  font-family: var(--font-sans-display);
  font-feature-settings: var(--font-sans-display-settings);
  background: var(--background);
  color: var(--foreground);
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference
| Role | Hex |
|---|---|
| Primary CTA | `#16a394` |
| Heading text | `#1A202C` |
| Body text | `#4A5568` |
| Background | `#FFFFFF` |
| Border | `#E2E8F0` |
| Link | `#2D3748` |
| Dark section | `#1A202C` |

### Example Component Prompts
- "Create a hero section on `#FFFFFF` background. Headline at 3rem `Mona Sans VF` weight 400. CTA button `#16a394` with white text."
- "Design a card: `#1c1c1f` background, `#E2E8F0` border, 8px radius. Body text `#4A5568` at weight 400."

### Iteration Guide
1. 폰트: `Mona Sans VF` 패밀리, 본문 weight 400
2. 컬러: 브랜드 `#16a394`는 CTA/링크에만 집중. 배경 `#FFFFFF`, 텍스트 `#1A202C`
3. 그림자: subtle box-shadow로 카드 elevation 표현
---

## 18. DO / DON'T

### ✅ DO
- Primary = **`#16a394`** (anchor teal). CTA/링크/포커스 모두 teal 계열.
- Mona Sans VF self-host + `cv01/cv02/cv06` feature 설정으로 대문자 형태 맞춤.
- 제품별 color family 활용: Postgres = teal (ppg), ORM = indigo (orm).
- shadcn `--background`/`--foreground`/`--primary` 네이밍 준수 (Fumadocs와 호환).
- 본문 색은 딥 네이비 `#1d242f`로. 순검정 아님.

### ❌ DON'T
- Prisma primary를 `#6366f1` indigo로 선언 금지 — ORM 제품 색이지 브랜드 primary 아님.
- Mona Sans를 Inter로 대체 금지. 시각 정체성의 80%는 Mona Sans `cv/ss` feature에서 나온다.
- 단일 color palette로 환원 금지 — 제품별 color family(ppg/orm/error/success/9 accent) 구조 보존.
- success color를 초록(`#22c55e`)으로 쓰지 말 것. Prisma success는 **teal** (`#0d9488`).
- Fumadocs `--color-fd-*` 네임스페이스를 `--color-*`로 평탄화 금지.

---

