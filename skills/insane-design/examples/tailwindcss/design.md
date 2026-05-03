---
schema_version: 3.2
slug: tailwindcss
service_name: Tailwind CSS
site_url: https://tailwindcss.com
fetched_at: 2026-05-03T07:15:55Z
default_theme: mixed
brand_color: "#00d2ef"
primary_font: Inter
font_weight_normal: 400
token_prefix: tw

bold_direction: Technical Aurora
aesthetic_category: Refined SaaS
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: documentation-site
archetype_confidence: high
design_system_level: lv3
design_system_level_evidence: "Tailwind v4 theme layer exposes 569 custom properties, full color ramps, typography variables, radius tokens, breakpoints, utilities, and documented component/search behavior."

colors:
  primary: "#00d2ef"
  primary-deep: "#00b7d7"
  accent-indigo: "#625fff"
  accent-sky: "#00a5ef"
  surface-light: "#ffffff"
  surface-soft: "#fafafa"
  surface-dark: "#030712"
  text-dark: "#020618"
  text-muted: "#62748e"
  hairline-dark: "#e5e7eb"
  overlay-dark: "#0000001a"
typography:
  display: "Inter"
  body: "Inter"
  mono: "IBM Plex Mono"
  ladder:
    - { token: text-xs, size: ".75rem", weight: 500, tracking: "0" }
    - { token: text-sm, size: ".875rem", weight: 500, tracking: "0" }
    - { token: text-base, size: "1rem", weight: 400, tracking: "0" }
    - { token: text-2xl, size: "1.5rem", weight: 600, tracking: "0" }
    - { token: text-7xl, size: "4.5rem", weight: 600, tracking: "0" }
    - { token: text-8xl, size: "6rem", weight: 600, tracking: "0" }
  weights_used: [100, 400, 500, 600, "bold"]
  weights_absent: [700, 800, 900]
components:
  button-primary: { bg: "{colors.primary}", radius: "3.40282e38px", padding: "10px 16px" }
  button-utility-dark: { bg: "#000000bf", radius: "3.40282e38px", padding: "8px 12px" }
  docsearch-modal: { bg: "{colors.surface-light}", overlay: "#0000001a", backdrop: "blur(var(--blur-sm))" }
  code-chip: { font: "{typography.mono}", radius: "var(--radius-md)", bg: "#0307120d" }
---

# DESIGN.md — Tailwind CSS

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Tailwind CSS의 마케팅 표면은 흰 canvas 위에 terminal-grade 컬러 토큰을 올려둔 구조다 — "utility-first"를 시각 언어로 번역한 사이트가 자기 몸으로 그 증거를 보여준다. 색상은 흰 바닥 #ffffff (`{colors.surface-light}`)와 거의 검정에 가까운 #030712 (`{colors.surface-dark}`) 사이에서 왕복하고, 그 사이를 cyan #00d2ef (`{colors.primary}`), sky #00a5ef (`{colors.accent-sky}`), indigo #625fff (`{colors.accent-indigo}`)가 전기 신호처럼 통과한다.

이 사이트의 시그니처는 "utility-first"를 시각 언어로 번역한 것이다. 한 덩어리의 브랜드 컬러가 모든 것을 덮는 대신, 작은 토큰들이 정확한 위치에 꽂힌다. 브랜드 컬러 하나가 왕좌에 앉아 있는 구조가 아니라, console처럼 cyan/sky/indigo 회로가 필요한 컴포넌트에만 전류를 보낸다. 그래서 no second brand color라는 말조차 정확하지 않다. Tailwind에서는 두 번째 색이 없는 게 아니라, 색상 ramp 전체가 제품의 말투다.

첫 화면은 소프트웨어 박람회의 부스보다 실험실의 조명 테이블에 가깝다. 흰 표면 위에 놓인 텍스트와 코드 조각은 종이 위 인쇄물이 아니라, utility class가 바로 아래에서 발광하는 샘플처럼 보인다. hero gradient는 장식용 aurora가 아니라 "이 프레임워크는 색상 공간까지 다룬다"는 시연 장치다. oklab/oklch gradient는 포스터의 배경이 아니라 도구 설명서 안에 꽂힌 네온 테스트 스트립처럼 작동한다.

Tailwind답게 색은 naming ramp 자체가 디자인 언어다. cyan/sky/indigo/purple 계열이 hero와 gradient에서 에너지를 만들고, slate/gray/zinc/neutral ramp가 문서의 정보 밀도를 안정시킨다. 색상 팔레트가 부록에 들어간 카탈로그가 아니라, 벽 전체가 swatch drawer인 기술 쇼룸이다. 이 브랜드는 단일 로고색보다 "색상 시스템을 다룰 줄 아는 제품"으로 기억된다.

공간은 넓지만 빈 듯 보이지 않는다. 큰 hero와 넓은 container가 먼저 프레임을 만들고, 아래로 내려가면 문서 링크, 컴포넌트, search, code block이 촘촘해진다. 즉 첫 화면은 영감이고, 두 번째 화면부터는 작업대다. DocSearch가 열릴 때도 페이지는 완전히 사라지지 않는다. #0000001a (`{colors.overlay-dark}`)와 blur는 유리판을 내려놓듯 현재 문맥을 잠깐 얼리고, 사용자는 다른 방으로 이동하지 않은 채 문서의 색인 서랍을 연다.

Tailwind의 검정도 단순한 검정이 아니다. #030712 (`{colors.surface-dark}`)는 OLED 구멍처럼 빠지는 black이 아니라, 코드 샘플을 올려두는 어두운 납땜 매트에 가깝다. 그 위에서 mono text와 cyan accent가 작은 LED처럼 읽힌다. shadow가 브랜드를 만들지 않는다. 이 사이트에서 깊이는 과장된 elevation보다 border, alpha surface, radius, token contrast가 만드는 조립 정밀도에서 나온다.

### Key Characteristics

- Tailwind v4 theme layer가 그대로 드러나는 token-first 사이트.
- Primary chroma는 cyan #00d2ef, 보조 에너지는 sky #00a5ef와 indigo #625fff.
- Light 문서 표면과 dark code/search 표면을 모두 쓰는 mixed theme.
- Inter가 본문과 display를 통합하고, IBM Plex Mono 계열이 코드성 요소를 분리한다.
- 둥근 CTA는 `rounded-full`의 극단값 3.40282e38px로 완전한 pill을 만든다.
- gradient는 장식 배경이 아니라 "CSS color space / modern utility"의 데모로 쓰인다.
- `@media (prefers-color-scheme: dark)`가 매우 강하게 나타나 dark 대응이 부가 기능이 아니다.
- DocSearch는 overlay + backdrop blur + modal chassis로 문서 사이트의 핵심 컴포넌트 역할을 한다.
- 색상 팔레트는 브랜드 킷이 아니라 제품 그 자체다. Tailwind 색상 ramp가 곧 브랜드 언어다.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Technical Aurora
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **cyan/sky/indigo token aurora over a precise documentation chassis**으로 기억된다.
> **Code Complexity**: high — Tailwind v4 token layer, modern color-space gradients, masks, DocSearch overlay, dark-mode media blocks, and utility-composed responsive patterns are all active.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Tailwind CSS처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter", system-ui, sans-serif;
  font-weight: 400;
  letter-spacing: 0;
}

/* 2. 배경 + 텍스트 */
:root {
  --tw-bg: #ffffff;
  --tw-fg: #020618;
  --tw-muted: #62748e;
}
body { background: var(--tw-bg); color: var(--tw-fg); }

/* 3. 브랜드 에너지 */
:root {
  --tw-brand: #00d2ef;
  --tw-brand-deep: #00b7d7;
  --tw-accent-sky: #00a5ef;
  --tw-accent-indigo: #625fff;
}
```

**절대 하지 말아야 할 것 하나**: Tailwind를 "파란 SaaS 랜딩"으로 만들지 마라. 핵심은 단일 blue가 아니라 cyan/sky/indigo/purple ramp와 neutral ramp가 함께 작동하는 token demo다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://tailwindcss.com` |
| Fetched | 2026-05-03T07:15:55Z |
| Extractor | Existing phase1 reuse: stored HTML/CSS/JSON |
| HTML size | 936147 bytes |
| CSS files | 2개 CSS, 총 730548자 |
| Token prefix | `tw` / Tailwind v4 theme variables |
| Method | Existing `insane-design/tailwindcss/phase1` JSON + CSS token inspection |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Tailwind CSS site bundle, likely modern React/Next-style static/SSR output based on large compiled HTML and utility CSS.
- **Design system**: Tailwind v4 theme layer — prefix `--tw-*` for runtime utilities and `--color-*`, `--font-*`, `--radius-*`, `--container-*`, `--breakpoint-*` for theme tokens.
- **CSS architecture**:
  ```css
  @layer theme      /* --font-sans, --color-cyan-400, --radius-lg, --breakpoint-* */
  @layer base       /* resets, transparent form defaults, inherited type */
  @layer utilities  /* .text-sky-500, .rounded-full, .grid-cols-*, .bg-linear-* */
  component scopes  /* .DocSearch-* modal/search behavior */
  ```
- **Class naming**: utility-first atomic classes with escaped arbitrary values and state variants.
- **Default theme**: mixed. Light homepage/documentation surface, dark-aware blocks via `prefers-color-scheme: dark`.
- **Font loading**: CSS variables `--font-inter`, `--font-plex-mono`, fallback metric fonts including `inter Fallback` and `plexMono Fallback`.
- **Canonical anchor**: Tailwind v4 color and utility engine. The site is both marketing surface and live spec for the framework.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Inter` (open, variable-friendly system)
- **Body font**: `Inter`
- **Code font**: `IBM Plex Mono` via `--font-plex-mono`, plus monospace fallback
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --tw-font-family:       var(--font-inter), system-ui;
  --tw-font-family-code:  var(--font-plex-mono), monospace;
  --tw-font-weight-normal: 400;
  --tw-font-weight-medium: 500;
  --tw-font-weight-bold:   600;
}
body {
  font-family: var(--tw-font-family);
  font-weight: var(--tw-font-weight-normal);
}
code, pre, kbd {
  font-family: var(--tw-font-family-code);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Inter substitute** — Use `system-ui` only when Inter is unavailable. Keep `font-weight: 400` for body, `500` for nav/search labels, and `600` for display. Do not compensate by jumping to 700.
- **IBM Plex Mono substitute** — Use `ui-monospace` or `SFMono-Regular`, but reduce visual noise by keeping code chips at 12-13px and weight 400/500. The mono layer should feel technical, not terminal-heavy.
- **Metric fallback** — Keep the `Inter Fallback` idea if implementing in Next/font. Tailwind's layout relies on stable text rhythm; font swap movement makes the page feel less precise.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `text-xs` | `.75rem` | 500 | approx 1.4 | `0` |
| `text-sm` | `.875rem` | 500 | approx 1.5 | `0` |
| `text-base` | `1rem` | 400 | approx 1.6 | `0` |
| `text-lg` | `1.125rem` | 400/500 | approx 1.55 | `0` |
| `text-2xl` | `1.5rem` | 600 | tight | `0` |
| `text-4xl` | `2.25rem` | 600 | tight | `0` |
| `text-7xl` | `4.5rem` | 600 | compressed | `0` |
| `text-8xl` | `6rem` | 600 | compressed | `0` |
| code / chip | `.8125rem` | 400/500 | compact | `0` |

> ⚠️ Tailwind CSS는 과한 negative tracking으로 "프리미엄"을 만들지 않는다. 크기와 weight, color contrast, code/mono 분리로 위계를 만든다.

### Principles
<!-- SOURCE: manual -->

1. Display weight is 600, not 700+ — the brand avoids startup-boom heaviness.
2. Body stays 400 with Inter; hierarchy comes from size, color, and spacing rather than weight stacking.
3. Weight 500 is a utility state for nav/search/labels, not a default paragraph weight.
4. Mono is a functional accent. It marks code, keyboard, and utility examples; it should not become the whole voice.
5. Letter-spacing is deliberately neutral. Tailwind's precision comes from token rhythm, not optical tightening.
6. The largest display sizes are allowed only with generous whitespace; dense docs fall back to `text-sm` and `text-base`.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (cyan / sky / indigo anchors)

| Token | Hex |
|---|---|
| `--color-cyan-50` | `#ecfeff` |
| `--color-cyan-100` | `#cefafe` |
| `--color-cyan-200` | `#a2f4fd` |
| `--color-cyan-300` | `#53eafd` |
| `--color-cyan-400` | `#00d2ef` |
| `--color-cyan-500` | `#00b7d7` |
| `--color-cyan-600` | `#0092b5` |
| `--color-sky-400` | `#00bcfe` |
| `--color-sky-500` | `#00a5ef` |
| `--color-indigo-500` | `#625fff` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--color-cyan-700` | `#007492` |
| `--color-cyan-800` | `#005f78` |
| `--color-cyan-900` | `#104e64` |
| `--color-cyan-950` | `#053345` |
| `--color-indigo-800` | `#372aac` |
| `--color-indigo-950` | `#1e1a4d` |

### 06-3. Neutral Ramp

| Step | Slate | Gray | Zinc |
|---|---|---|---|
| 50 | `#f8fafc` | `#f9fafb` | `#fafafa` |
| 100 | `#f1f5f9` | `#f3f4f6` | `#f4f4f5` |
| 200 | `#e2e8f0` | `#e5e7eb` | `#e4e4e7` |
| 300 | `#cad5e2` | `#d1d5dc` | `#d4d4d8` |
| 500 | `#62748e` | `#6a7282` | `#71717b` |
| 700 | `#314158` | `#364153` | `#3f3f46` |
| 900 | `#0f172b` | `#101828` | `#18181b` |
| 950 | `#020618` | `#030712` | `#09090b` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| cyan | 400 | `#00d2ef` |
| sky | 500 | `#00a5ef` |
| indigo | 500 | `#625fff` |
| purple | 500 | `#ac4bff` |
| teal | 400 | `#00d3bd` |
| blue | 500 | `#3080ff` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `{colors.primary}` | `#00d2ef` | Primary chromatic energy, cyan anchor |
| `{colors.primary-deep}` | `#00b7d7` | Darker cyan state / gradient continuation |
| `{colors.accent-sky}` | `#00a5ef` | Links, gradient, product energy |
| `{colors.accent-indigo}` | `#625fff` | Modern CSS/gradient counterpoint |
| `{colors.surface-light}` | `#ffffff` | Main document and homepage surface |
| `{colors.surface-soft}` | `#fafafa` | Quiet band / card floor |
| `{colors.surface-dark}` | `#030712` | Dark code/docs/search surfaces |
| `{colors.text-dark}` | `#020618` | Dense near-black text |
| `{colors.text-muted}` | `#62748e` | Muted slate text |
| `{colors.hairline-dark}` | `#e5e7eb` | Light border, especially low-opacity dark variants |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--font-sans` | `var(--font-inter), system-ui` | Global UI type |
| `--font-mono` | `var(--font-plex-mono), monospace` | Code and utility examples |
| `--color-cyan-400` | `#00d2ef` | Brand cyan |
| `--color-sky-500` | `#00a5ef` | Blue-sky accent |
| `--color-indigo-500` | `#625fff` | Indigo gradient counterpoint |
| `--color-gray-950` | `#030712` | Dark chassis |
| `--color-slate-950` | `#020618` | Near-black text |
| `--color-white` | `#fff` | Surface and reversed text |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token / raw value | Hex | Frequency |
|---|---:|---:|
| white alpha | `#ffffff1a` | 103 |
| transparent black | `#0000` | 60 |
| black alpha | `#0000001a` | 53 |
| white | `#fff` | 42 |
| gray-950 alpha | `#0307120d` | 41 |
| white alpha | `#ffffff0d` | 35 |
| black alpha | `#0000000d` | 24 |
| white 20% | `#fff3` | 20 |
| cyan translucent | `#00b7d780` | 6 |
| indigo | `#625fff` | 5 |
| sky translucent | `#00a5ef80` | 4 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.primary}` (`#00d2ef`)** — Tailwind의 cyan anchor. CTA 하나를 칠하기 위한 색이라기보다, utility-first 색상 시스템이 살아 있다는 신호다. 단독 brand blue로 쓰지 말고 sky/indigo와 함께 modern CSS 느낌을 만든다.

**`{colors.surface-light}` (`#ffffff`)** — 문서와 마케팅을 받치는 가장 큰 바닥. 하지만 이 흰색은 비어 있는 배경이 아니라, code/dark surface와 cyan gradient가 더 선명하게 보이도록 만드는 실험실 조명이다.

**`{colors.text-dark}` (`#020618`)** — slate-950 계열의 거의 검정. 순수 #000000보다 차갑고 기술적인 인상을 주며, Inter 400 본문과 600 display의 대비를 안정시킨다.

**`{colors.hairline-dark}` (`#e5e7eb`)** — border는 선명한 카드 장식이 아니라 구조 표시다. Tailwind는 border를 큰 스타일 요소로 과시하지 않고, opacity와 dark-mode 변형으로 문서 레이어를 정리한다.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--spacing` | `.25rem` | Tailwind v4 base unit; `calc(var(--spacing)*N)` pattern |
| `gap-2` | `.5rem` | Inline utilities, small controls |
| `gap-4` | `1rem` | Nav/search/control groups |
| `gap-6` | `1.5rem` | Docs card/internal rhythm |
| `gap-8` | `2rem` | Feature rows and section internals |
| `p-4` | `1rem` | Mobile/compact panel padding |
| `p-6` | `1.5rem` | Search modal and card padding |
| `max-w-7xl` | `80rem` class-family | Wide documentation/marketing container |
| `--breakpoint-2xl` | referenced in grid container | Full-width centered layout with gutters |

**주요 alias**:
- `calc(var(--spacing)*4)` -> 16px-class rhythm for modal/card padding.
- `calc(var(--spacing)*6)` -> 24px-class rhythm for wider search/container padding.
- `var(--gutter-width)` -> full-width layout grid gutter control.

### Whitespace Philosophy
<!-- SOURCE: manual -->

Tailwind의 whitespace는 "넓은 landing page"와 "좁은 docs UI"를 한 화면 안에서 오간다. Hero에서는 큰 headline과 gradient가 숨 쉴 수 있게 넓은 공기를 주지만, 실제 문서/검색/코드 영역은 `text-sm`, `gap-4`, `p-4/p-6`으로 빠르게 압축된다.

이 리듬은 제품 철학과 같다. 사용자는 먼저 가능성을 보고, 곧바로 utility를 조합한다. 따라서 spacing을 무작정 넓히면 Tailwind답지 않고, 무작정 촘촘하게 만들면 hero의 modern CSS 에너지가 사라진다.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `.rounded-xs` | `var(--radius-xs)` | Small code/control details |
| `.rounded-sm` | `var(--radius-sm)` | Compact UI |
| `.rounded-md` | `var(--radius-md)` | Inputs, code chips, small panels |
| `.rounded-lg` | `var(--radius-lg)` | Cards, search surfaces |
| `.rounded-xl` | `var(--radius-xl)` | Large cards |
| `.rounded-2xl` | `var(--radius-2xl)` | Feature modules |
| `.rounded-3xl` | `var(--radius-3xl)` | Hero/large containers |
| `.rounded-4xl` | `var(--radius-4xl)` | Oversized marketing panels |
| `.rounded-full` | `3.40282e38px` | Pill buttons, circular icon buttons |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| reset | `0 0 #0000` | Tailwind shadow variable baseline |
| utility stack | `var(--tw-inset-shadow), var(--tw-inset-ring-shadow), var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow)` | Standard Tailwind shadow composition |
| inset highlight | `inset 0 1px #ffffff0d` | Dark surface subtle top highlight |
| large | `var(--shadow-lg)` | Occasional elevated modal/card |

Tailwind does not rely on heavy elevation. Shadow is mostly an implementation variable, while contrast, border, transparency, and blur do the visible separation.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| `--tw-duration` | `initial` / utility controlled | Transition utility baseline |
| `@media (prefers-reduced-motion: reduce)` | present | Accessibility branch |
| hover media | `@media (hover:hover)` | Hover-only refinements for desktop pointers |
| backdrop blur | `blur(var(--blur-sm))` | Search overlay depth rather than animated spectacle |

Motion should feel utility-fast. Use short color/opacity transitions; avoid bouncy product animations unless the underlying Tailwind demo specifically calls for it.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `max-w-7xl` / `var(--breakpoint-2xl)` style centered layout.
- **Grid type**: CSS Grid and Flexbox mixed. Utility classes include fixed repeat grids and custom template grids.
- **Column count**: `grid-cols-1`, `2`, `3`, `4`, `6`, `11`, `15`, `30` plus arbitrary templates like `1fr var(--gutter-width) minmax(0,var(--breakpoint-2xl))`.
- **Gutter**: `var(--gutter-width)` for page shell, `gap-4` to `gap-8` for content modules.

### Hero
- **Pattern Summary**: large technical hero + light surface + cyan/sky/indigo gradient energy + CTA/documentation routes.
- Layout: primarily centered or asymmetric marketing-doc hybrid, then collapses into denser docs navigation.
- Background: solid #ffffff with gradient and dark/code surfaces used as focal material.
- **Background Treatment**: modern gradient utilities using `linear-gradient(... in oklab/oklch)` and mask utilities; not a static bitmap hero.
- H1: `text-7xl` / `text-8xl` family, weight `600`, tracking `0`.
- Max-width: wide container, commonly `max-w-7xl`/2xl-grid shell.

### Section Rhythm

```css
section {
  padding: calc(var(--spacing) * 16) calc(var(--spacing) * 4);
  max-width: var(--breakpoint-2xl);
}
```

### Card Patterns
- **Card background**: #ffffff in light mode, #030712 / alpha overlays in dark/code contexts.
- **Card border**: low-contrast neutral, often #e5e7eb or alpha variants like #e5e7eb0d.
- **Card radius**: `var(--radius-lg)` to `var(--radius-2xl)`.
- **Card padding**: `p-4`, `p-6`, sometimes wider feature padding.
- **Card shadow**: minimal; more often ring/border/contrast than deep box-shadow.

### Navigation Structure
- **Type**: horizontal top navigation with documentation/search/product links; mobile collapses.
- **Position**: page-header / sticky-like behavior may be present, but phase1 did not fully exercise scrolling.
- **Height**: compact SaaS-doc nav, approximately 56-64px.
- **Background**: #ffffff or transparent-to-solid light surface; dark-aware states exist.
- **Border**: subtle neutral hairline rather than heavy divider.

### Content Width
- **Prose max-width**: documentation text stays narrower than the hero container.
- **Container max-width**: `max-w-7xl` and `var(--breakpoint-2xl)` shells.
- **Sidebar width**: docs sidebar likely fixed/utility-driven; exact runtime width not measured in this pass.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | base / below `40rem` | Single-column, compact nav/search affordances |
| Small | `40rem` | `sm` branch; modal/search padding increases |
| Medium | `48rem` | `md` branch; docs/content layout starts widening |
| Large | `64rem` | `lg` branch; navigation and multi-column layouts stabilize |
| Extra Large | `80rem` | `xl` branch; wide feature grids and max containers |
| 2XL | `96rem` | `2xl` branch; maximum shell/gutter behavior |

### Touch Targets
- **Minimum tap size**: not fully measured from DOM interaction; use 44px minimum for any recreated mobile control.
- **Button height (mobile)**: implement 40-44px for CTA/search buttons.
- **Input height (mobile)**: DocSearch/search should stay at least 40px high.

### Collapsing Strategy
- **Navigation**: desktop horizontal nav becomes compact mobile menu/search entry.
- **Grid columns**: base single-column, then `sm/md/lg/xl` progressive grid expansion.
- **Sidebar**: docs sidebar likely collapses/overlays on mobile; exact state not captured.
- **Hero layout**: large display shrinks by breakpoint rather than preserving desktop proportions.

### Image Behavior
- **Strategy**: CSS/gradient/code-demo driven more than photography driven.
- **Max-width**: utility controlled with `w-full`, `max-w-*`, and responsive containers.
- **Aspect ratio handling**: no single hero image ratio defines the page; components use layout utilities.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<a class="inline-flex items-center rounded-full bg-cyan-400 px-4 py-2 text-sm font-semibold text-slate-950 hover:bg-cyan-300">
  Get started
</a>
```

| Property | Value |
|---|---|
| Background | `#00d2ef` for cyan primary; dark utility can use `#000000bf` |
| Text | `#020618` on cyan, `#ffffff` on dark |
| Radius | `3.40282e38px` (`rounded-full`) |
| Padding | 8-10px vertical, 12-16px horizontal |
| Weight | 600 for CTA, 500 for utility |
| Hover | chroma or opacity shift, not large transform |

### Badges

```html
<span class="inline-flex rounded-full bg-gray-950/5 px-2 py-1 text-xs font-medium text-slate-700">
  v4.0
</span>
```

Badges should be small, token-like, and technical. Avoid marketing pill overload. Use neutral alpha backgrounds such as #0307120d or subtle cyan/sky tint only when the label is product-critical.

### Cards & Containers

```html
<article class="rounded-2xl border border-gray-200 bg-white p-6">
  <h3 class="text-sm font-semibold text-slate-950">Utility-first workflow</h3>
  <p class="mt-2 text-sm text-slate-500">Compose states directly in markup.</p>
</article>
```

| Property | Value |
|---|---|
| Background | `#ffffff` / `#fafafa`; dark examples use `#030712` |
| Border | `#e5e7eb`, often alpha-adjusted |
| Radius | `var(--radius-lg)` to `var(--radius-2xl)` |
| Padding | `p-4` or `p-6` |
| Shadow | minimal, use ring/border first |
| Hover | subtle border/color/opacity; no dramatic lift |

### Navigation

```html
<nav class="flex h-16 items-center justify-between border-b border-gray-200 bg-white">
  <a class="text-sm font-semibold text-slate-950">Tailwind CSS</a>
  <div class="flex items-center gap-6 text-sm font-medium text-slate-500"></div>
</nav>
```

Nav is compact and information-forward. Links should feel like documentation controls, not glossy landing buttons. Active state can move to #020618 while inactive links sit in #62748E-like slate.

### Inputs & Forms

```html
<button class="DocSearch-Button rounded-full border border-gray-200 bg-white px-4 text-sm text-slate-500">
  Search documentation
</button>
```

Search is the main input component. Focus states should use ring/outline with cyan/sky tokens. Avoid thick blue browser-default outlines; use Tailwind ring composition.

### Hero Section

```html
<section class="mx-auto max-w-7xl px-4 py-24 text-center">
  <h1 class="text-7xl font-semibold text-slate-950">Rapidly build modern websites.</h1>
  <p class="mx-auto mt-6 max-w-2xl text-lg text-slate-500"></p>
</section>
```

Hero should make the product feel technical and immediate. Use large Inter 600 display, cyan/sky/indigo gradient detail, and a code/demo surface nearby. Do not rely on generic dashboard mockups.

### 13-2. Named Variants
<!-- SOURCE: manual -->

#### `button-primary-cyan`

| Spec | Value |
|---|---|
| bg | `#00d2ef` |
| text | `#020618` |
| radius | `3.40282e38px` |
| weight | 600 |
| state | hover moves lighter/deeper in cyan ramp |

#### `button-utility-dark`

| Spec | Value |
|---|---|
| bg | `#000000bf` |
| text | `#ffffff` |
| radius | `3.40282e38px` |
| state | group-hover opacity/black overlay pattern |

#### `docsearch-modal`

| Spec | Value |
|---|---|
| overlay | `#0000001a` / color-mix black 20% |
| backdrop | `blur(var(--blur-sm))` |
| container | fixed, full viewport, z-index 200 |
| padding | `calc(var(--spacing)*4)` -> `*6` from `40rem` |

#### `code-chip`

| Spec | Value |
|---|---|
| font | `var(--font-plex-mono), monospace` |
| size | `.8125rem` or `text-xs/text-sm` |
| bg | `#0307120d` or dark code surface |
| radius | `var(--radius-md)` |

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

#### oklab-gradient-utility

```yaml
oklab-gradient-utility:
  description: "Tailwind v4의 modern color-space capability를 장식이 아니라 제품 데모로 드러낸다."
  technique: "linear-gradient(var(--tw-gradient-stops)) with `to right in oklab` / `oklch increasing hue` variants"
  applied_to: ["{component.Hero Section}", "{component.code-chip}", "framework capability surfaces"]
  visual_signature: "gradient가 배경 무드가 아니라 브라우저-native color syntax를 보여주는 네온 테스트 스트립처럼 읽힌다."
```

#### docsearch-blur-chassis

```yaml
docsearch-blur-chassis:
  description: "문서 검색을 별도 페이지 이동이 아니라 현재 문맥 위의 command surface로 만든다."
  technique: "fixed 100vw/100vh overlay, z-index: 200, background-color: #0000001a, backdrop-filter: blur(var(--blur-sm))"
  applied_to: ["{component.docsearch-modal}", ".DocSearch-Container"]
  visual_signature: "페이지가 꺼지지 않고 유리판 아래로 한 겹 밀리며, 검색 모달이 문서 색인 서랍처럼 열린다."
```

#### rounded-full-infinity-pill

```yaml
rounded-full-infinity-pill:
  description: "CTA와 utility control을 Tailwind식 완전 pill로 압축한다."
  technique: ".rounded-full { border-radius: 3.40282e38px }, padding: 8-10px 12-16px"
  applied_to: ["{component.button-primary}", "{component.button-utility-dark}", "nav utility controls"]
  visual_signature: "일반 rounded button이 아니라 radius가 사실상 무한대인 token capsule로 보인다."
```

#### alpha-neutral-hairline

```yaml
alpha-neutral-hairline:
  description: "그림자보다 alpha neutral surface와 hairline으로 문서 구조를 조립한다."
  technique: "background/border alpha values including #0307120d, #0000001a, #ffffff0d, #e5e7eb0d"
  applied_to: ["{component.docsearch-modal}", "{component.code-chip}", "dark panels", "separators"]
  visual_signature: "구조는 선명하지만 장식적 선은 거의 없고, UI가 token grid 위에 얇게 조립된 느낌을 만든다."
  intent: "Tailwind의 정체성은 'utility token이 곧 디자인'이다. shadow 토큰을 남발하면 framework가 이 메시지를 스스로 어긴다."
```

#### token-as-prose-in-code-blocks

```yaml
token-as-prose-in-code-blocks:
  description: "Tailwind 문서의 코드블록은 syntax highlighting이 아니라 token 분류 그 자체로 색이 입혀진다."
  technique: "token type (utility class / variant / breakpoint)에 따라 다른 alpha-neutral 색을 부여; 변수 이름이 시각적 grammar의 일부."
  applied_to: ["{component.code-block}", "documentation example", "playground snippet"]
  visual_signature: "코드가 읽히는 동시에 'token 가족'이 색으로 분류되어 한눈에 보인다 — 글이자 시스템 다이어그램."
  intent: "tutorial 사이트가 아니라 design system reference이므로, 코드는 데이터 시각화로 기능해야 한다."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 결과 중심, 빠른 제작 속도를 직접 말한다 | "Rapidly build modern websites..." |
| Primary CTA | 명령형, 짧게 | "Get started" |
| Secondary CTA | 학습/문서 경로 | "Read the docs" |
| Subheading | utility-first 개념을 구체적으로 설명 | "without ever leaving your HTML" |
| Tone | technical, confident, teaching-oriented | framework creator voice |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Tailwind CSS — copy into your root stylesheet */
:root {
  /* Fonts */
  --tw-font-family:       var(--font-inter), system-ui, sans-serif;
  --tw-font-family-code:  var(--font-plex-mono), monospace;
  --tw-font-weight-normal: 400;
  --tw-font-weight-medium: 500;
  --tw-font-weight-bold:   600;

  /* Brand / accent */
  --tw-color-cyan-400:  #00d2ef;
  --tw-color-cyan-500:  #00b7d7;
  --tw-color-sky-500:   #00a5ef;
  --tw-color-indigo-500:#625fff;
  --tw-color-purple-500:#ac4bff;

  /* Surfaces */
  --tw-bg-page:   #ffffff;
  --tw-bg-soft:   #fafafa;
  --tw-bg-dark:   #030712;
  --tw-text:      #020618;
  --tw-text-muted:#62748e;
  --tw-border:    #e5e7eb;

  /* Key spacing */
  --tw-space-unit: .25rem;
  --tw-space-sm:  calc(var(--tw-space-unit) * 2);
  --tw-space-md:  calc(var(--tw-space-unit) * 4);
  --tw-space-lg:  calc(var(--tw-space-unit) * 6);

  /* Radius */
  --tw-radius-md: var(--radius-md);
  --tw-radius-lg: var(--radius-lg);
  --tw-radius-pill: 3.40282e38px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Tailwind CSS-inspired theme subset
module.exports = {
  theme: {
    extend: {
      colors: {
        cyan: {
          400: '#00d2ef',
          500: '#00b7d7',
          600: '#0092b5',
          950: '#053345',
        },
        sky: {
          400: '#00bcfe',
          500: '#00a5ef',
        },
        indigo: {
          500: '#625fff',
          800: '#372aac',
        },
        slate: {
          500: '#62748e',
          950: '#020618',
        },
        gray: {
          200: '#e5e7eb',
          950: '#030712',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['IBM Plex Mono', 'ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
        semibold: '600',
      },
      borderRadius: {
        pill: '3.40282e38px',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `{colors.primary}` | `#00d2ef` |
| Brand deep | `{colors.primary-deep}` | `#00b7d7` |
| Accent sky | `{colors.accent-sky}` | `#00a5ef` |
| Accent indigo | `{colors.accent-indigo}` | `#625fff` |
| Background | `{colors.surface-light}` | `#ffffff` |
| Dark surface | `{colors.surface-dark}` | `#030712` |
| Text primary | `{colors.text-dark}` | `#020618` |
| Text muted | `{colors.text-muted}` | `#62748e` |
| Border | `{colors.hairline-dark}` | `#e5e7eb` |

### Example Component Prompts

#### Hero Section

```text
Tailwind CSS 스타일 히어로 섹션을 만들어줘.
- 배경: #ffffff, 텍스트: #020618
- H1: Inter, text-7xl~text-8xl, weight 600, letter-spacing 0
- 서브텍스트: #62748e, 18px, line-height 1.55
- CTA: bg #00d2ef, text #020618, radius 3.40282e38px, padding 10px 16px
- 보조 액센트: #00a5ef + #625fff gradient, 가능하면 oklab/oklch gradient syntax 사용
- 코드/검색 표면: #030712 또는 #0307120d, mono는 IBM Plex Mono
```

#### Card Component

```text
Tailwind CSS 스타일 카드 컴포넌트를 만들어줘.
- 배경: #ffffff, border: 1px solid #e5e7eb, radius: var(--radius-xl)
- padding: 24px
- shadow는 최소화하고 border/ring으로 레이어를 구분
- 제목: Inter, 14~16px, weight 600, color #020618
- 본문: 14px, color #62748e, line-height 1.6
- hover: border/color/opacity만 미세 조정. 큰 translate나 heavy shadow 금지.
```

#### Badge

```text
Tailwind CSS 스타일 배지를 만들어줘.
- font: Inter, 12px, weight 500
- padding: 4px 8px, radius: 999px
- 기본: bg #0307120d, color #314158 또는 #62748e
- 브랜드형: bg #00d2ef alpha tint, color #007492
```

#### Navigation

```text
Tailwind CSS 스타일 상단 네비게이션을 만들어줘.
- 높이: 56~64px, 배경 #ffffff, 하단 border #e5e7eb
- 링크: Inter 14px weight 500, inactive #62748e, active #020618
- 검색 버튼은 DocSearch처럼 pill/rounded surface로 만들고, overlay는 #0000001a + backdrop blur
- CTA는 #00d2ef pill button으로 작게 배치
```

### Iteration Guide

- **색상 변경 시**: cyan/sky/indigo/purple ramp 중 하나로 움직여라. 임의의 generic royal blue 하나로 통일하지 마라.
- **폰트 변경 시**: Inter 400/500/600 구조를 유지한다. display에 700+를 쓰면 Tailwind의 가벼운 기술감이 사라진다.
- **여백 조정 시**: `.25rem` base unit과 `calc(var(--spacing)*N)` 리듬을 유지한다.
- **새 컴포넌트 추가 시**: `rounded-full`, `rounded-lg`, `border/ring`, alpha neutral surface를 먼저 조합한다.
- **다크 모드**: #030712 계열 dark chassis와 white alpha token을 같이 써라. 단순 black background만 깔지 마라.
- **반응형**: `40rem`, `48rem`, `64rem`, `80rem`, `96rem` 계열을 유지한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use cyan #00d2ef as the primary chromatic signal, supported by sky #00a5ef and indigo #625fff.
- Keep the main document surface #ffffff and the dark/code/search chassis #030712 in active contrast.
- Build components from Tailwind-like primitives: radius, alpha surface, border/ring, utility spacing.
- Use Inter 400/500/600 and reserve IBM Plex Mono for code/search/utility-specific details.
- Let gradients demonstrate modern CSS color spaces (`oklab`, `oklch`) rather than generic decoration.
- Use subtle alpha neutrals such as #0307120d, #0000001a, and #ffffff0d for layering.
- Treat DocSearch/search as a first-class component, not a small input afterthought.

### ❌ DON'T

- 배경을 `#F8FAFC`만으로 두지 말 것 — Tailwind main surface는 `#FFFFFF`가 기본이고 soft neutral은 보조다.
- 본문 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#020618` 계열을 사용한다.
- 브랜드 컬러를 `#3B82F6` 하나로 단순화하지 말 것 — 대신 `#00D2EF`, `#00A5EF`, `#625FFF` 조합을 사용한다.
- dark surface를 `#000000`으로 두지 말 것 — 대신 `#030712`를 사용한다.
- border를 `#CCCCCC` 같은 중립 회색으로 두지 말 것 — 대신 `#E5E7EB` 또는 alpha neutral을 사용한다.
- CTA radius를 `8px`로 두지 말 것 — Tailwind CTA/utility pill은 `3.40282e38px`급 rounded-full이다.
- display headline에 `font-weight: 800` 사용 금지 — Tailwind는 600 중심의 technical confidence다.
- 모든 카드에 heavy `box-shadow`를 주지 말 것 — border/ring/alpha surface가 우선이다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- **Single brand blue**: absent. Tailwind is not one blue; it is cyan/sky/indigo/purple ramp behavior.
- **Photography-led hero**: none. Product identity comes from CSS, code, gradients, and documentation UI.
- **Heavy elevation**: never the main separator. Shadows exist as utility machinery, but visual hierarchy comes from contrast and rings.
- **Rounded rectangle monotony**: avoided. The system distinguishes `rounded-md`, `rounded-lg`, `rounded-2xl`, and full pill.
- **Weight 800/900 display branding**: deliberately absent from the primary voice.
- **Decorative illustration as core brand**: absent. Diagrams/code/examples do the expressive work.
- **Warm beige/cream palette**: none. The neutral temperature is cool slate/gray/zinc.
- **Generic purple-blue AI gradient**: not the pattern. Gradients must be tied to Tailwind color ramps and modern color-space syntax.
- **Pure black dark mode**: avoided. Use #030712 and alpha overlays instead.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Existing phase1 reuse** — This report reused the stored `insane-design/tailwindcss` HTML/CSS/JSON from 2026-04-20 rather than refetching live assets on 2026-05-03. Tailwind's live site may have changed.
- **Homepage-centered capture** — The available HTML/CSS appears to cover the public site bundle, but not every docs subpage interaction was manually exercised.
- **Screenshot not reinterpreted in this pass** — The report is primarily token/CSS/HTML-grounded. Visual observations are inferred from the existing artifact set, not a fresh browser walkthrough.
- **Component states incomplete** — Hover/focus/active states are documented where CSS patterns surfaced, but form validation, loading, and error states were not fully visited.
- **Dark-mode mapping partial** — `prefers-color-scheme: dark` is heavily present, but the report does not enumerate every light/dark token pair.
- **Framework inference** — The exact app runtime is described conservatively from compiled output. No package files were inspected because the run intentionally avoided extra repo exploration.
- **Color frequency caveat** — Top frequency colors include alpha overlays and utility resets; brand color selection prioritizes chromatic product tokens over raw frequency.
- **No HTML report regeneration** — Per user instruction, Step 6 RENDER-HTML was skipped and only `design.md` was overwritten.
