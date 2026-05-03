---
schema_version: 3.2
slug: prisma
service_name: Prisma
site_url: https://www.prisma.io
fetched_at: 2026-04-20T20:00:00+09:00
default_theme: light
brand_color: "#14B8A6"
primary_font: "Inter"
font_weight_normal: 400
token_prefix: "--color"

bold_direction: "Managed Precision"
aesthetic_category: "Refined SaaS"
signature_element: "hero_impact"
code_complexity: "high"

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "CSS 변수 411개, resolved token 309개, Tailwind v4 theme layer와 Prisma/Fumadocs 계열 semantic token이 동시에 확인됨."

colors:
  primary: "#14B8A6"
  primary-token: "#16A394"
  primary-hover: "#0D9488"
  surface: "#FFFFFF"
  surface-soft: "#F9FAFB"
  surface-ppg: "#F0FDFA"
  text-primary: "#111827"
  text-muted: "#6B7280"
  border: "#E5E7EB"
  dark-surface: "#030712"
  dark-panel: "#131420"
  dark-border: "#1D242F"

typography:
  display: "Inter"
  body: "Inter"
  mono: "Mona Sans Mono VF"
  ladder:
    - { token: hero, size: "40px -> 64px", weight: 900, tracking: "stretch-display / optical wide" }
    - { token: h2, size: "36px", weight: 900, tracking: "stretch-display" }
    - { token: body, size: "16px", weight: 400, line_height: "24px" }
    - { token: nav, size: "16px", weight: 600, line_height: "24px" }
    - { token: code-cta, size: "16px", weight: 400, font: "Mona Sans Mono VF" }
  weights_used: [100, 200, 375, 400, 500, 600, 650, 700, 800, 900]
  weights_absent: []

components:
  button-primary: { bg: "{colors.primary}", hover_bg: "{colors.primary-hover}", radius: "6px", height: "48px", padding: "0 16px" }
  command-button: { bg: "#F3F4F6", color: "{colors.text-muted}", radius: "6px", font: "Mona Sans Mono VF" }
  nav-bar: { bg: "#FFFFFF80", radius: "12px", shadow: "0 1px 3px #0000001A" }
  workflow-card: { bg: "{colors.surface}", border: "1px solid {colors.border}", radius: "12px" }
---

# DESIGN.md - Prisma

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Prisma's marketing surface is white canvas holding terminal-grade database infrastructure in a centered two-line grid. The hero is mostly white, but not empty: tiny `#14B8A6` (`{colors.primary}`) particle marks and a pale `#F0FDFA` (`{colors.surface-ppg}`) atmospheric wash make the canvas read as Postgres infrastructure without becoming a literal database diagram. It is closer to a clean-room console observation window than a SaaS splash page: the database machinery is implied by telemetry specks, not shown as machinery.

The type is the product. "Postgres, perfectly managed." lands in extra-heavy Inter, centered, compressed into two lines, and allowed to dominate the viewport before any product UI appears. It has the weight of a label etched onto a server-room door — short, black, operational. The parchment of the white canvas makes that label legible: the hero phrase reads like blueprint text printed on a bright engineering surface.

The palette is two-track. `--primary: #16A394` (`{colors.primary-token}`) is the semantic system token; the marketing hero's visible CTA and particle signature use `#14B8A6` (`{colors.primary}`) as the remembered color. There is no second brand color fighting for the stage: indigo exists in the system, but the homepage refuses to become purple Prisma again. The teal is not sprinkled as decoration; it marks database creation, selected affordances, and success surfaces — a terminal signal light on a white canvas lab bench.

The page is split between documentation discipline and marketing polish. Fumadocs-style `--color-fd-*` tokens, Tailwind v4 theme variables, and monospace command treatment sit underneath a large SaaS hero. The command chip works like a terminal receipt placed beside the sales counter: `npx prisma init` is the console artifact that immediately backs the marketing promise. Shadows are restrained: chrome lifts just enough to clarify controls, while atmosphere belongs to the `#14B8A6` particle field. The white canvas is not luxury emptiness — it is the lab bench that makes teal particles and command syntax legible.

비유로 한 번 더 풀자면, prisma.io는 **Postgres 시연이 진행 중인 실험실 작업판**이다. 흰 hero는 라미네이트 canvas lab bench, teal particle field는 클린룸의 terminal telemetry pinpoint, 헤드라인은 작업판 위에 인쇄된 parchment 도면 라벨이다. teal CTA는 도면 옆에 놓인 시연 시작 스위치, mono command chip은 console receipt — `npx prisma init`은 시연자가 시연 직전에 손에 쥐는 측정 도구다. 페이지가 마케팅 splash가 아니라, 데이터베이스 인프라의 시연 매뉴얼처럼 정렬되어 있다.

### Key Characteristics

- Teal PPG accent: `#14B8A6` for the hero CTA and particle pattern, with `#16A394` retained as the semantic primary token.
- Heavy centered display type: Inter at black/900 weights, two-line hero, no delicate serif or editorial pairing.
- Command-as-secondary-CTA: the `npx prisma init` control uses mono typography and a neutral chip instead of a second colored button.
- Floating rounded nav: white/transparent surface, 12px-ish corner behavior, soft shadow, and compact product links.
- Workflow card grid below the hero: product benefits are represented as IDE/database UI panels with light borders and constrained shadows.
- Tailwind v4 token ladder: `--spacing: .25rem`, `--text-*`, `--container-*`, and utility classes drive the implementation.
- Fumadocs compatibility layer: `--color-fd-*` aliases map app/documentation colors onto the same theme foundation.
- Dark mode exists in tokens, but the observed homepage screenshot is light-first.
- Motion is subtle but technically rich: 50ms button transitions coexist with particle SVG ambience and multi-layer teal shadows.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Managed Precision
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **developer command chip beside a teal database CTA**으로 기억된다.
> **Code Complexity**: high — Tailwind v4 token layer, Fumadocs aliases, dark token map, particle SVG hero, and multi-layer shadows all need coordinated implementation.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Prisma처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter", "Roboto", "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}
.prisma-display {
  font-family: "Inter", sans-serif;
  font-weight: 900;
  letter-spacing: -0.025em;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #FFFFFF;
  --fg: #111827;
  --muted: #6B7280;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root {
  --brand-visible: #14B8A6;
  --brand-semantic: #16A394;
  --brand-hover: #0D9488;
}
```

**절대 하지 말아야 할 것 하나**: Prisma를 보라색/인디고 SaaS로 되돌리지 말 것. 현재 hero의 기억 색은 `#14B8A6`, semantic primary는 `#16A394`다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.prisma.io` |
| Fetched | 2026-04-20T20:00:00+09:00 |
| Extractor | reused phase1 artifacts from `insane-design/prisma/` |
| HTML size | 437800 bytes (Next.js static/SSR output) |
| CSS files | 2 external CSS files, total 248916 chars |
| Token prefix | `--color`, `--color-fd`, `--background`, `--foreground` |
| Method | CSS custom properties, resolved token JSON, typography JSON, screenshot, and HTML hero structure |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js marketing site output with static chunks and preloaded WOFF2 assets.
- **Design system**: Prisma marketing token layer + Fumadocs-compatible `--color-fd-*` aliases.
- **CSS architecture**:
  ```css
  @layer theme             /* Tailwind v4 primitive tokens */
  --color-background-*     /* Prisma marketing surfaces */
  --color-foreground-*     /* Prisma text and semantic foregrounds */
  --color-fd-*             /* documentation/component compatibility aliases */
  --background / --primary /* shadcn-like app theme tokens */
  ```
- **Class naming**: Tailwind utility classes with arbitrary values (`max-w-[1240px]`, `font-[650]`) and data-state variants.
- **Default theme**: light (`#FFFFFF` page surface, `#111827` foreground).
- **Font loading**: Next/font-like local WOFF2 preloads; CSS reports Inter and Inter Fallback, plus Mona Sans Mono VF for code UI.
- **Canonical anchor**: hero CTA and particles: `#14B8A6`; semantic app primary: `#16A394`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary font**: `Inter` (open-source family, loaded through local assets / next font output)
- **Display font**: `Inter` with `font-black` / 900 and `stretch-display` treatment
- **Code font**: `Mona Sans Mono VF`, fallback to `ui-monospace`, `Cascadia Code`, `Source Code Pro`, `Menlo`, `Consolas`
- **Weight normal / bold**: `400` / `900` for the marketing voice; `650` appears on the primary CTA

```css
:root {
  --font-sans: "Inter","Roboto","Helvetica Neue","Arial Nova","Nimbus Sans","Arial",sans-serif;
  --font-mono: "Mona Sans Mono VF",ui-monospace,"Cascadia Code","Source Code Pro","Menlo","Consolas","DejaVu Sans Mono",monospace;
  --font-weight-normal: 400;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --font-weight-black: 900;
}
body {
  font-family: var(--font-sans);
  font-weight: var(--font-weight-normal);
}
```

### Note on Font Substitutes

- **Inter** is safe to substitute with `Roboto` only for body text. For hero display, Roboto needs stronger tracking compensation: use weight `900`, `letter-spacing: -0.025em`, and a line-height close to `1`.
- **Mona Sans Mono VF** should be kept for the command chip if possible. If unavailable, `Cascadia Code` is the best substitute; keep it at 16px/400 and avoid bolding the command string.
- **CTA weight** is not a generic 600. The observed hero CTA uses `font-[650]`, so a static fallback should use 600 only if variable weights are unavailable.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `hero` | `2.5rem -> 4rem` | `900` | `1 -> 4.5rem` | `-0.025em` / stretch display |
| `section-title` | `36px` | `900` | `1.1-1.2` | stretch display |
| `body` | `16px` | `400` | `24px` | `0` |
| `nav-link` | `16px` | `600` | `24px` | `0` |
| `button-primary` | `16px` | `650` | `48px control` | `0` |
| `code-command` | `16px` | `400` | `48px control` | mono default |
| `small-text` | `14px` | `400/500/600` | `20px` | `0` |
| `caption` | `12px` | `500` | `16px` | optional `.1em` for uppercase contexts |

> ⚠️ Prisma's extracted typography JSON has no semantic scale table, so the scale above is reconstructed from Tailwind tokens and observed hero/component classes.

### Principles

1. Display is heavy, not merely large. The homepage relies on black/900 Inter and a compact line-height to make "Postgres, perfectly managed." feel engineered.
2. Body copy stays plain at 16px/400. The contrast comes from display weight and spacing, not from rich body styling.
3. CTA weight can use variable `650`; do not flatten every button to 500 or 600 if variable font support is available.
4. The secondary command action must remain mono. It is not a marketing button; it is a developer affordance.
5. Negative tracking belongs to display and dense label moments only. Body and nav text keep normal spacing.
6. Prisma permits a wide weight range in CSS, but the observed homepage hierarchy mostly uses 400, 600/650, and 900.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (PPG / teal)

| Token | Hex |
|---|---|
| `--color-background-ppg` | `#F0FDFA` |
| `--color-background-ppg-strong` | `#CCFBF1` |
| `--color-background-ppg-reverse` | `#14B8A6` |
| `--color-background-ppg-reverse-strong` | `#0D9488` |
| `--color-foreground-ppg` | `#0D9488` |
| `--color-foreground-ppg-weak` | `#14B8A6` |
| `--color-stroke-ppg` | `#0D9488` |
| `--color-stroke-ppg-weak` | `#99F6E4` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--color-background-ppg` dark | `#042F2E` |
| `--color-background-ppg-strong` dark | `#134E4A` |
| `--color-background-ppg-reverse-strong` dark | `#2DD4BF` |
| `--color-foreground-ppg-reverse-weak` | `#99F6E4` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| Page | `#FFFFFF` | `#030712` |
| Default text | `#111827` | `#F9FAFB` |
| Muted text | `#6B7280` | `#9CA3AF` |
| Strong neutral bg | `#E5E7EB` | `#374151` |
| Neutral bg | `#F3F4F6` | `#1F2937` |
| Weak neutral bg | `#F9FAFB` | `#111827` |
| Border | `#E5E7EB` | `#1D242F` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| ORM / indigo | reverse | `#6366F1` |
| ORM / indigo strong | reverse-strong | `#4F46E5` |
| Success | reverse | `#14B8A6` |
| Error | reverse | `#EF4444` |
| Warning | reverse-strong | `#EA580C` |
| Blue | token | `#3080FF` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--primary` | `#16A394` | app primary, sidebar primary, chart 1 |
| `--primary-foreground` | `#FFFFFF` | text on primary surfaces |
| `--accent` | `#D9F9F6` | selected/accent soft surfaces |
| `--accent-foreground` | `#154F47` | text on soft accent |
| `--destructive` | `#E53E3E` | destructive/error semantic |
| `--ring` | `#16A394` | focus ring |
| `--border` | `#E2E8F0` | app border |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--color-fd-background` | `--background` | docs/app background compatibility |
| `--color-fd-foreground` | `--foreground` | docs/app foreground compatibility |
| `--color-fd-card` | `--card` | card surface compatibility |
| `--color-fd-border` | `--border` | docs border compatibility |
| `--color-fd-primary` | `--primary` | docs primary compatibility |
| `--sidebar-primary` | `#16A394` | sidebar selected/primary affordances |
| `--sidebar-accent` | `#D9F9F6` | sidebar accent background |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token / source | Hex | Frequency / note |
|---|---|---|
| particle SVG pattern | `#14B8A6` | 308 appearances, mostly SVG pattern |
| transparent utility | `#00000000` | 49 |
| surface | `#FFFFFF` | 30 |
| black alpha shadow | `#0000001A` | 14 |
| black alpha hair shadow | `#0000000A` | 13 |
| dark border / dark panel | `#1D242F` | 10 |
| semantic primary | `#16A394` | 9 |
| soft neutral surface | `#F9FAFB` | 9 |

### 06-8. Color Stories

**`{colors.primary}` (`#14B8A6`)** — The remembered Prisma homepage color. It appears in the hero particles and primary CTA, where the site wants the user to feel "create database" rather than "read docs."

**`{colors.primary-token}` (`#16A394`)** — The semantic primary underneath the marketing skin. It powers `--primary`, `--ring`, sidebar primary, and chart 1, so implementation should keep it as the system token even when visible hero elements use `#14B8A6`.

**`{colors.surface}` (`#FFFFFF`)** — The page floor. White is correct here, but only because teal atmosphere, rounded nav chrome, and card borders give it structure.

**`{colors.text-primary}` (`#111827`)** — The true neutral anchor for marketing text. Avoid pure `#000000`; Prisma's text is a cool near-black that leaves room for borders and shadows.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--spacing` | `.25rem` | Tailwind v4 base unit |
| `gap-2` | `8px` | compact icon/text and menu spacing |
| `gap-4` | `16px` | hero CTA pair, card row rhythm |
| `gap-8` | `32px` | hero content stack |
| `gap-12` | `48px` | larger section grouping |
| `h-element-lg` | `28px` | small nav CTA height |
| `h-element-4xl` | `48px` | hero CTA and command chip |
| `max-w-[1240px]` | `1240px` | main workflow grid container |
| `max-w-224` | `896px` | hero headline width |
| `max-w-2xl` | `672px` | hero supporting copy |

**주요 alias**:
- `--spacing-element-4xl` -> `3rem` (hero button/control height)
- `--container-7xl` -> `80rem` (wide layout ceiling)
- `--container-5xl` -> `64rem` (large prose/content block)

### Whitespace Philosophy

Prisma uses open hero air, then immediately compresses into workflow cards. The first screen lets the headline sit in a broad light field with `gap-8` between message and actions; the section below tightens into 16px card gaps and a 1240px product grid.

This is not luxury whitespace. It is operational whitespace: the top gives confidence, the next band gives evidence. Keep the hero centered and breathable, then make product cards denser and more information-rich.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `--radius` | `.5rem` | base shadcn-like radius |
| `--radius-square-low` | `.1875rem` | very small square-ish controls |
| `--radius-square` | `.375rem` | primary buttons and compact controls |
| `--radius-square-high` | `.75rem` | nav/card rounded surfaces |
| `--radius-circle` | `999px` | circular icon/step counters |
| `rounded-2xl` | `calc(var(--radius) + 8px)` | larger marketing panels |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `shadow-sm` | `0 1px 2px 0 #0000000D` | subtle card/control lift |
| `shadow` | `0 1px 3px 0 #0000001A, 0 1px 2px -1px #0000001A` | nav/menu/card elevation |
| `shadow-md` | `0 4px 6px -1px #0000001A, 0 2px 4px -2px #0000001A` | popover or raised panel |
| `shadow-lg` | `0 10px 15px -3px #0000001A, 0 4px 6px -4px #0000001A` | large floating surfaces |
| `teal glow` | `0 -7px 80px #2DD4BF29, ... 6-layer fade` | special PPG/teal atmospheric glow |
| `box low` | `0 .0625rem .125rem #0000000A` | small button chrome |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / pattern | Value | Usage |
|---|---|---|
| default transition | `.15s` | general Tailwind transition base |
| hero/button micro | `50ms` | primary CTA hover/press transitions |
| menu chevron | `300ms` | navigation menu chevron rotation |
| reveal curve | `cubic-bezier(.22,1,.36,1)` | smoother UI reveal |
| elastic reveal | `cubic-bezier(.34,1.56,.64,1)` | richer opacity/transform/border transitions |
| SVG particles | static/animated SVG marks in `#14B8A6` | hero atmosphere |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `1240px` for the main workflow/product grid.
- **Grid type**: Flex + CSS grid hybrid; mobile card list, `md:grid md:grid-cols-2`, larger desktop-specific layouts.
- **Column count**: observed 2-column intermediate grid and wider card composition below hero.
- **Gutter**: `16px` (`gap-4`) in card/product grid; larger stack gaps in hero.

### Hero

- **Pattern Summary**: full-width light field + teal particle SVG + centered two-line H1 + teal CTA / mono command pair.
- Layout: one-column centered hero with CTA row switching from vertical mobile to horizontal desktop.
- Background: `#FFFFFF` / light neutral with an absolute teal particle SVG and gradient overlay from PPG foreground to page background at 20% opacity.
- **Background Treatment**: particle-field + gradient veil, not a static illustration card.
- H1: `text-4xl sm:text-5xl md:text-6xl`, weight `900`, stretch display, centered, max-width `896px`.
- Max-width: `max-w-224` headline, `max-w-2xl` supporting copy.

### Section Rhythm

```css
section.hero {
  margin-top: -96px;
  padding-top: 160px;
  padding-inline: 16px;
}
.workflow-section {
  margin-block: 48px;
}
.workflow-container {
  max-width: 1240px;
  padding: 16px 16px 0;
}
```

### Card Patterns

- **Card background**: mostly `#FFFFFF`, with soft neutral layers `#F9FAFB` and `#F3F4F6`.
- **Card border**: `1px solid #E5E7EB` / `#E2E8F0`.
- **Card radius**: `12px` for larger marketing cards; `6px` for compact controls.
- **Card padding**: `16px` and `24px` clusters; cards often combine text block and screenshot/SVG illustration.
- **Card shadow**: low alpha black shadows; richer shadows reserved for popovers and large panels.

### Navigation Structure

- **Type**: horizontal desktop nav with dropdown triggers; mobile hamburger icon.
- **Position**: visually floating at top, inside hero overlap.
- **Height**: approximately `64px` nav bar; small CTA uses `h-element-lg`.
- **Background**: translucent/light white surface, rounded high radius, soft shadow.
- **Border**: minimal; structure comes from surface, shadow, and spacing.

### Content Width

- **Prose max-width**: docs layer exposes `--fd-layout-width` / 1400px fallback; marketing copy uses narrower `max-w-2xl`.
- **Container max-width**: 1240px marketing grid, 80rem Tailwind container token.
- **Sidebar width**: not observed on homepage; docs/Fumadocs tokens suggest separate documentation layout exists.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Small | `40rem` / 640px | Tailwind `sm`, typography and card adaptations |
| Medium custom | `720px`, `750px` | marketing layout refinements |
| Desktop custom | `874px`, `940px` | nav/card breakpoint thresholds |
| Large | `64rem` / 1024px | Tailwind `lg`, desktop grid/nav behaviors |
| XL | `80rem` / 1280px | large container behavior |
| 2XL | `96rem` / 1536px | wide viewport polish |

### Touch Targets

- **Minimum tap size**: hero controls are `48px` high; nav CTA is smaller at `28px`, acceptable for desktop but should be expanded on touch surfaces.
- **Button height (mobile)**: hero CTA remains `48px`.
- **Input height (mobile)**: not observed on homepage.

### Collapsing Strategy

- **Navigation**: desktop links collapse to a hamburger icon at small widths.
- **Grid columns**: product cards flow single column, then `md:grid-cols-2`, then desktop-specific composition.
- **Sidebar**: not observed in homepage; docs layout likely uses Fumadocs responsive sidebar.
- **Hero layout**: CTA pair stacks vertically on mobile and becomes horizontal at `md`.

### Image Behavior

- **Strategy**: SVG/product screenshots are preloaded and masked/faded inside cards.
- **Max-width**: images use `min-w-full`, `object-fill`, and explicit dimensions.
- **Aspect ratio handling**: screenshot/SVG illustrations are cropped/masked with top-left object positioning and bottom fade masks.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA**

```html
<a class="rounded-square bg-background-ppg-reverse text-foreground-ppg-reverse hover:bg-background-ppg-reverse-strong shadow-box-low px-4 h-element-4xl gap-3 type-heading-md font-sans-display font-[650]">
  <span>Create database</span>
</a>
```

| Spec | Value |
|---|---|
| Background | `#14B8A6` |
| Hover background | `#0D9488` |
| Text | `#FFFFFF` |
| Radius | `--radius-square` = `6px` |
| Height | `48px` |
| Padding | `0 16px` |
| Font | Inter display, `650` |
| Shadow | low box shadow |

**Command Button**

```html
<button class="rounded-square bg-background-neutral text-foreground-neutral hover:bg-background-neutral-strong px-4 h-element-4xl font-mono">
  <span>$</span><span>npx prisma init</span>
</button>
```

| Spec | Value |
|---|---|
| Background | `#F3F4F6` |
| Hover background | `#E5E7EB` |
| Text | `#6B7280` / `#111827` accents |
| Font | Mona Sans Mono VF |
| Height | `48px` |
| Role | secondary developer proof, not a secondary CTA |

### Badges

Prisma uses badge-like icon wells more than pill badges in the observed homepage. The pattern is a square teal-tinted icon cell beside text.

| Spec | Value |
|---|---|
| Background | `#F0FDFA` |
| Text/Icon | `#0D9488` |
| Radius | `6px` |
| Size | `48px` icon well (`size-element-4xl`) |

### Cards & Containers

Cards are white or near-white panels with light neutral borders and screenshots/illustrations inside. They avoid loud background color except for icon cells.

| Spec | Value |
|---|---|
| Background | `#FFFFFF` / `#F9FAFB` |
| Border | `1px solid #E5E7EB` |
| Radius | `12px` for larger containers |
| Padding | `16px` to `24px` clusters |
| Hover | subtle border/background/low-shadow shifts only |

### Navigation

Desktop nav combines brand mark, dropdown triggers, plain links, GitHub stars, Discord icon, login, and primary CTA.

| Spec | Value |
|---|---|
| Container | floating rounded light bar |
| Link size | 16px |
| Link weight | 600 |
| Hover | soft PPG background (`#CCFBF1` / tokenized background-ppg-strong) |
| CTA | compact teal button, `h-element-lg` |
| Dropdown indicator | chevron rotates over 300ms |

### Inputs & Forms

Homepage forms are not surfaced. Reuse token defaults for implementation:

| Spec | Value |
|---|---|
| Border | `#E2E8F0` / `--input` |
| Focus ring | `#16A394` |
| Radius | `6px` or base `8px` depending on control density |
| Error | `#E53E3E` / `#EF4444` |

### Hero Section

The hero component is the signature structure: particle field, centered display type, supporting copy, primary action, and mono command.

| Spec | Value |
|---|---|
| Surface | `#FFFFFF` with teal/PPG atmospheric overlay |
| H1 | Inter 40-64px, 900, centered |
| Copy | 16px, `#111827`, max-width 672px |
| CTA row | flex column mobile -> row desktop |
| Decorative layer | absolute SVG particles in `#14B8A6` |

### 13-2. Named Variants

**button-primary-database** — hero and nav creation action.

| Property | Value |
|---|---|
| bg | `#14B8A6` |
| hover | `#0D9488` |
| fg | `#FFFFFF` |
| radius | `6px` |
| height | `48px` hero / `28px` nav compact |

**button-command-neutral** — command chip for `npx prisma init`.

| Property | Value |
|---|---|
| bg | `#F3F4F6` |
| hover | `#E5E7EB` |
| fg | `#6B7280` |
| font | `Mona Sans Mono VF` |
| radius | `6px` |

**nav-trigger-soft-ppg** — dropdown/link hover state.

| Property | Value |
|---|---|
| bg-hover | `#CCFBF1` / PPG strong token |
| radius | `6px` on desktop |
| icon motion | chevron rotate 180deg over 300ms |

**workflow-icon-cell** — square product benefit icon well.

| Property | Value |
|---|---|
| bg | `#F0FDFA` |
| fg | `#0D9488` |
| size | `48px` |
| radius | `6px` |

### 13-3. Signature Micro-Specs

```yaml
teal-particle-hero-field:
  description: "The hero is not blank white; it is seeded with teal database-atmosphere particles."
  technique: "absolute full-width SVG layer with repeated rect elements using fill #14B8A6, plus a PPG-to-page gradient veil at 20% opacity"
  applied_to: ["{component.hero-section}"]
  visual_signature: "a clean Postgres control-room field that suggests managed infrastructure without drawing a literal database"

dual-primary-teal-system:
  description: "Marketing teal and semantic app primary remain adjacent but deliberately separate."
  technique: "#14B8A6 for visible CTA/particles; #16A394 for --primary, --ring, sidebar-primary, and chart-1"
  applied_to: ["{component.button-primary}", "{component.nav-bar}", "{component.docs-token-layer}"]
  visual_signature: "Prisma feels brighter in the homepage hero and calmer in app/documentation chrome"

developer-command-secondary:
  description: "The secondary hero action proves developer credibility through command syntax instead of another CTA color."
  technique: "48px neutral chip, background #F3F4F6, hover #E5E7EB, Mona Sans Mono VF at 16px/400, $ prefix, copy affordance"
  applied_to: ["{component.command-button}", "{component.hero-section}"]
  visual_signature: "a terminal receipt sitting beside the teal database action"

square-ppg-icon-cell:
  description: "Feature affordances use a small square teal well rather than decorative badges or rainbow icons."
  technique: "48px square cell, radius 6px, background #F0FDFA, foreground/icon #0D9488"
  applied_to: ["{component.workflow-card}", "{component.badge-icon-cell}"]
  visual_signature: "database features read as system controls, not marketing stickers"

low-alpha-panel-elevation:
  description: "Chrome depth is kept neutral and low while teal glow is reserved for accent atmosphere."
  technique: "box-shadow layers using #0000000A and #0000001A; shadow-sm 0 1px 2px 0 #0000000D; nav shadow 0 1px 3px 0 #0000001A, 0 1px 2px -1px #0000001A"
  applied_to: ["{component.nav-bar}", "{component.workflow-card}", "{component.product-panel}"]
  visual_signature: "surfaces lift like lightweight app chrome instead of glossy marketing cards"
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Short operational promise, product noun first | "Postgres, perfectly managed." |
| Primary CTA | action-oriented, database-specific | "Create database" |
| Secondary CTA | command / developer artifact | "npx prisma init" |
| Subheading | plain benefit sentence, no hype stack | "Real Postgres with the developer experience and infrastructure to ship faster." |
| Tone | confident, infrastructure-oriented, developer-native | "right in your workflow" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Prisma - copy into your root stylesheet */
:root {
  /* Fonts */
  --prisma-font-family: "Inter","Roboto","Helvetica Neue","Arial Nova","Nimbus Sans","Arial",sans-serif;
  --prisma-font-family-code: "Mona Sans Mono VF",ui-monospace,"Cascadia Code","Source Code Pro","Menlo","Consolas",monospace;
  --prisma-font-weight-normal: 400;
  --prisma-font-weight-cta: 650;
  --prisma-font-weight-display: 900;

  /* Brand */
  --prisma-color-brand-visible: #14B8A6;
  --prisma-color-brand-primary: #16A394;
  --prisma-color-brand-hover: #0D9488;
  --prisma-color-brand-soft: #F0FDFA;
  --prisma-color-brand-soft-strong: #CCFBF1;

  /* Surfaces */
  --prisma-bg-page: #FFFFFF;
  --prisma-bg-soft: #F9FAFB;
  --prisma-bg-control: #F3F4F6;
  --prisma-text: #111827;
  --prisma-text-muted: #6B7280;
  --prisma-border: #E5E7EB;

  /* Key spacing */
  --prisma-space-unit: .25rem;
  --prisma-gap-card: 16px;
  --prisma-gap-hero: 32px;
  --prisma-container-wide: 1240px;

  /* Radius */
  --prisma-radius-control: 6px;
  --prisma-radius-card: 12px;
  --prisma-radius-pill: 999px;
}

.prisma-hero {
  position: relative;
  background: var(--prisma-bg-page);
  color: var(--prisma-text);
  padding: 160px 16px 48px;
  text-align: center;
}

.prisma-hero h1 {
  max-width: 896px;
  margin: 0 auto;
  font-family: var(--prisma-font-family);
  font-size: clamp(2.5rem, 6vw, 4rem);
  line-height: 1;
  letter-spacing: -0.025em;
  font-weight: var(--prisma-font-weight-display);
}

.prisma-button-primary {
  height: 48px;
  padding: 0 16px;
  border-radius: var(--prisma-radius-control);
  background: var(--prisma-color-brand-visible);
  color: #FFFFFF;
  font-weight: var(--prisma-font-weight-cta);
  box-shadow: 0 .0625rem .125rem #0000000A;
  transition: background 50ms ease;
}

.prisma-button-primary:hover {
  background: var(--prisma-color-brand-hover);
}

.prisma-command-chip {
  height: 48px;
  padding: 0 16px;
  border-radius: var(--prisma-radius-control);
  background: var(--prisma-bg-control);
  color: var(--prisma-text-muted);
  font-family: var(--prisma-font-family-code);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js - Prisma-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        prisma: {
          teal: '#14B8A6',
          primary: '#16A394',
          hover: '#0D9488',
          soft: '#F0FDFA',
          softStrong: '#CCFBF1',
          text: '#111827',
          muted: '#6B7280',
          border: '#E5E7EB',
          surface: '#FFFFFF',
        },
      },
      fontFamily: {
        sans: ['Inter', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
        mono: ['Mona Sans Mono VF', 'Cascadia Code', 'Menlo', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        cta: '650',
        display: '900',
      },
      borderRadius: {
        prisma: '6px',
        'prisma-card': '12px',
      },
      boxShadow: {
        'prisma-low': '0 .0625rem .125rem #0000000A',
        'prisma-nav': '0 1px 3px 0 #0000001A, 0 1px 2px -1px #0000001A',
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
| Brand primary visible | `--color-background-ppg-reverse` | `#14B8A6` |
| Semantic primary | `--primary` | `#16A394` |
| Brand hover | `--color-background-ppg-reverse-strong` | `#0D9488` |
| Background | `--color-background-default` | `#FFFFFF` |
| Text primary | `--color-foreground-neutral` | `#111827` |
| Text muted | `--color-foreground-neutral-weak` | `#6B7280` |
| Border | `--color-stroke-neutral` | `#E5E7EB` |
| Success | `--color-background-success-reverse` | `#14B8A6` |
| Error | `--color-background-error-reverse` | `#EF4444` |

### Example Component Prompts

#### Hero Section

```text
Prisma 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF, 위에 #14B8A6 작은 particle SVG/점 패턴을 아주 희미하게 배치
- H1: Inter, clamp(2.5rem, 6vw, 4rem), weight 900, line-height 1, tracking -0.025em
- 서브텍스트: #111827, 16px, max-width 672px
- CTA 버튼: background #14B8A6, hover #0D9488, text #FFFFFF, radius 6px, height 48px, padding 0 16px, weight 650
- 보조 액션: #F3F4F6 mono command chip, "npx prisma init"
- 최대 너비: headline 896px, section content centered
```

#### Card Component

```text
Prisma 스타일 workflow 카드를 만들어줘.
- 배경: #FFFFFF, border: 1px solid #E5E7EB, radius: 12px
- 내부 아이콘 셀: #F0FDFA background, #0D9488 icon, 48px square
- padding: 16-24px
- shadow: 0 1px 2px #0000000A 수준으로 낮게
- 제목: Inter 16px weight 700, color #111827
- 본문: 14px, color #111827 또는 #6B7280, line-height 1.5
```

#### Badge / Icon Cell

```text
Prisma 스타일 제품 아이콘 셀을 만들어줘.
- 48px square, radius 6px
- bg #F0FDFA, icon/text #0D9488
- 카드 제목 옆에 배치하고 장식용 pill badge처럼 남발하지 말 것
```

#### Navigation

```text
Prisma 스타일 상단 네비게이션을 만들어줘.
- floating light nav bar, background #FFFFFF 또는 #FFFFFF80, radius 12px, subtle shadow #0000001A
- 링크: Inter 16px, weight 600, color #111827
- hover: #CCFBF1 계열 soft PPG background
- 우측 CTA: #14B8A6 compact button, text #FFFFFF
- Products/Resources는 chevron이 300ms로 회전하는 dropdown trigger
```

### Iteration Guide

- **색상 변경 시**: hero visible teal `#14B8A6`와 semantic primary `#16A394`를 분리해서 유지한다.
- **폰트 변경 시**: Inter 900 hero가 깨지면 Prisma 느낌이 사라진다. body보다 display weight를 먼저 맞춘다.
- **여백 조정 시**: hero는 넓게, workflow cards는 16px gap으로 조밀하게 유지한다.
- **새 컴포넌트 추가 시**: radius는 6px/12px 체계를 우선 사용하고 pill은 icon/circle에만 제한한다.
- **다크 모드**: `#030712`, `#131420`, `#1D242F`, `#2DD4BF` 계열을 사용한다. light token에 opacity만 씌워 만들지 않는다.
- **반응형**: mobile에서 CTA는 stack, desktop에서 row. nav는 hamburger collapse를 유지한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#14B8A6` for visible hero CTA/particle moments and `#16A394` for semantic primary/ring/system tokens.
- Keep the hero centered, two-line, and very heavy: Inter 900 with compact line-height.
- Pair the primary CTA with a neutral mono command chip when speaking to developers.
- Use `#FFFFFF`, `#F9FAFB`, and `#F3F4F6` as the surface stack, separated by `#E5E7EB` borders and low alpha shadows.
- Use square-ish 6px controls and 12px larger panels; reserve 999px for circular counters/icons only.
- Let teal appear as an operational signal, not a decorative wash over every section.
- Keep card/product grids more compact than the hero; the page needs "open promise, dense proof."

### ❌ DON'T

- 배경을 `#F0FDFA` 전체 페이지로 두지 말 것 — hero atmosphere에는 맞지만 기본 페이지는 `#FFFFFF` 사용.
- 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — Prisma marketing text는 `#111827` 사용.
- primary CTA를 `#16A394`로만 고정하지 말 것 — 관찰된 hero CTA/particle 색은 `#14B8A6`, hover는 `#0D9488`.
- 예전 ORM/indigo 느낌으로 CTA를 `#6366F1` 또는 `#4F46E5`로 만들지 말 것 — 현재 Postgres hero는 teal PPG가 주인공.
- 카드 border를 `#CCCCCC`처럼 강하게 두지 말 것 — `#E5E7EB` 또는 `#E2E8F0`의 낮은 대비를 사용.
- hero H1을 `font-weight: 600` 이하로 두지 말 것 — display는 black/900 질감이 핵심.
- secondary action을 또 하나의 teal CTA로 만들지 말 것 — `#F3F4F6` neutral command chip이 맞다.
- 버튼 radius를 `999px` pill로 통일하지 말 것 — primary controls는 `6px`, larger cards/nav는 `12px`.
- shadow를 진하게 `#00000040` 기반 카드 전체에 남발하지 말 것 — 대부분은 `#0000000A`/`#0000001A` 수준이다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Purple-first brand layer: **absent** — indigo는 ORM/accent 도구함에만 남아 있고, 시연 lab bench의 메인 색은 절대 보라가 아니다.
- Serif editorial contrast: **none** — 시연 보드는 Inter + mono 단일 family로만 운영, serif/sans pairing은 zero.
- Full-bleed photography hero: **never** — hero는 blueprint 도면이지 lifestyle 사진이 아니다.
- Second loud CTA color: **absent** — primary action은 teal, secondary action은 neutral command receipt이다.
- Generic pill-button language: **zero** — 공구함 control은 6px 직사각, large pill capsule은 등장하지 않는다.
- Heavy chrome shadows: **none** — depth는 low-alpha + functional, 특수 teal glow 외에는 부재.
- Rainbow feature grid: **never** — accent family가 있어도 카드 셀은 neutral + teal icon mark만.
- Playful illustration overload above the fold: **absent** — SVG/제품 panel은 시연 증거이지 일러스트 장식이 아니다.
- Pure black text anchor: **never** — 잉크는 cool neutral `#111827`, browser black은 zero.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual / REQUIRED -->

- **Homepage-biased sample** — analysis reused the existing `insane-design/prisma/` homepage capture. Console, pricing flow, docs subpages, and auth screens may have additional component states.
- **Screenshot is desktop only** — responsive behavior is inferred from CSS breakpoints and classes, not from fresh mobile screenshots.
- **Motion is CSS/HTML inferred** — particle behavior and transitions were identified from markup/CSS; JS scroll triggers or runtime animation timelines were not deeply executed.
- **Typography scale is reconstructed** — `typography.json` reported no semantic scale entries, so heading/body rows are inferred from Tailwind theme variables and observed classes.
- **Logo/customer SVG color pollution** — frequency count includes SVG pattern and possible illustration colors; brand color was selected from visible CTA/hero context rather than raw frequency alone.
- **Form states not surfaced** — inputs, validation, loading, and error UI are token-derived because the homepage did not expose a complete form flow.
- **Dark mode not visually verified** — dark tokens are present in CSS, but the observed screenshot and main analysis target are light theme.
- **Fumadocs layer scope** — `--color-fd-*` aliases confirm docs-compatible tokens, but the homepage does not exercise the full docs sidebar/content layout.
