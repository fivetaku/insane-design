---
schema_version: 3.2
slug: daangn
service_name: Daangn
site_url: https://www.daangn.com/
fetched_at: 2026-04-14T01:11:00+09:00
default_theme: light
brand_color: "#FF6600"
primary_font: "Pretendard Variable"
font_weight_normal: 400
token_prefix: seed

bold_direction: Friendly Utility
aesthetic_category: other
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high

archetype: commerce-marketplace
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Seed/Carotene CSS variables 674 total, 558 resolved, with semantic aliases for colors, spacing, radius, typography, and component states."

colors:
  primary: "#FF6600"
  primary-pressed: "#E14D00"
  surface-base: "#FFFFFF"
  surface-raised: "#F7F8F9"
  text-primary: "#1A1C20"
  text-muted: "#868B94"
  border-muted: "#DCDEE3"
  blue-accent: "#1E82EB"
typography:
  display: "Pretendard Variable"
  body: "Pretendard Variable"
  ladder:
    - { token: t1, size: "11px", line_height: "15px", weight: 400 }
    - { token: t2, size: "12px", line_height: "16px", weight: 400 }
    - { token: t3, size: "13px", line_height: "18px", weight: 400 }
    - { token: t4, size: "14px", line_height: "19px", weight: 400 }
    - { token: t5, size: "16px", line_height: "22px", weight: 400 }
    - { token: t6, size: "18px", line_height: "24px", weight: 600 }
    - { token: t7, size: "20px", line_height: "27px", weight: 600 }
    - { token: t10, size: "26px", line_height: "35px", weight: 700 }
  weights_used: [400, 500, 600, 700]
  weights_absent: [300, 800, 900]
components:
  button-download: { bg: "{colors.primary}", radius: "6px", padding: "14px 16px", state_pressed: "{colors.primary-pressed}" }
  search-pill: { bg: "{colors.surface-base}", radius: "9999px", border: "1px solid {colors.border-muted}", height: "48px" }
  service-card: { bg: "{colors.surface-raised}", radius: "12px", padding: "20px", hover: "neutral-hover fill" }
  district-chip: { bg: "{colors.surface-raised}", radius: "9999px", padding: "8px 14px" }
---

# DESIGN.md - Daangn (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Daangn is the canonical example of a commerce-marketplace reduced to its civic minimum. The browser becomes a marketplace canvas: white city surface, one carrot-orange coordinate, and a search pill that functions as the neighborhood's single storefront window. The page gives the user one job — "find something near me" — then lets category cards and district chips become the real navigation surface.

The strongest choice is the refusal to decorate the hero. The top 800px are mostly #FFFFFF (`{colors.surface-base}`), a compact logo, one orange download button, a centered search question, and a pill search control. There is no second brand color and no campaign wash. #FF6600 (`{colors.primary}`) is used like a marketplace pin: it marks action, icon, or identity, then immediately gets out of the way.

The search pill is the visual equivalent of a neighborhood boutique front desk — white on white, earning its edge through the #DCDEE3 (`{colors.border-muted}`) hairline, 48px height, and 9999px radius rather than shadow. Below it, the category cards read like a well-organized store directory: identical soft compartments, each holding one everyday errand. #F7F8F9 (`{colors.surface-raised}`) replaces elevation; shadow is absent because the surface is not trying to become furniture.

The district chips are closer to a transit index than to marketing badges. Tight padding, pill radius, and neutral fill let many neighborhoods scan quickly, while carrot remains reserved for the places where the user can actually act. Daangn's editorial restraint is this local compression: it makes density feel browsable, not busy.

Typography is Korean-first product typography. Pretendard Variable carries almost every surface, with 400 as the plain-reading default, 600 for compact labels, and 700 only when the page needs a local-search headline. The absence of display drama is part of the brand: Daangn sounds close, searchable, and everyday, like public signage designed by someone who still cares about touch targets.

### Key Characteristics

- White-first marketplace surface: #FFFFFF dominates the hero, with #F7F8F9 reserved for cards and chips.
- Single carrot anchor: #FF6600 is the brand/action color, supported by #E14D00 pressed state.
- Korean utility typography: Pretendard Variable, compact 11-26px scale, no ornamental display font.
- Rounded but controlled geometry: 9999px pills for search/chips, 12px cards, 6px app-download button.
- Navigation is task-shaped: search, service cards, popular keyword row, and district chips replace marketing sections.
- Dense local content below an airy hero: the first fold breathes, then quickly becomes browsable.
- Icons carry category color, not whole-card chroma: orange, magenta, blue, and yellow live in pictograms.
- State changes are quiet: background-color transitions around .15s, not motion-heavy transforms.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Friendly Utility
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **white local-search hero with carrot utility accents**으로 기억된다.
> **Code Complexity**: medium — mature token system and responsive utility classes, but restrained visual effects.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Daangn처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Pretendard Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #1A1C20; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #FF6600; --brand-pressed: #E14D00; }
.cta { background: var(--brand); border-radius: 6px; }
```

**절대 하지 말아야 할 것 하나**: 전체 화면을 주황색 브랜드 면으로 덮지 말 것. Daangn의 주황은 넓은 배경이 아니라 검색/CTA/아이콘에만 찍히는 생활 신호다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.daangn.com/` |
| Fetched | 2026-04-14T01:11:00+09:00 |
| Extractor | reused phase1 assets from `insane-design/daangn/` |
| HTML size | 139376 bytes |
| CSS files | 5 external CSS files, total 531593 chars |
| Token prefix | `seed` + `carotene` |
| Method | CSS custom properties, resolved token JSON, screenshot, and homepage HTML interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React/Vite-style hashed CSS modules visible in production assets.
- **Design system**: Seed + Carotene — prefixes `--seed-*` and `--carotene-*`.
- **CSS architecture**:
  ```css
  --seed-color-palette-*       raw color ramps and semantic roles
  --carotene-color-*           app-facing semantic alias layer
  --carotene-spacing-*         4px/rem spacing ladder
  --carotene-radius-*          radius ladder up to full pill
  .sprinkles_*                 utility-class layer for layout and spacing
  .seed-action-button*         component-level button contract
  ```
- **Class naming**: mixed hashed modules (`_1p17zxb2`) + Sprinkles atomic utilities (`sprinkles_backgroundColor_neutral__...`).
- **Default theme**: light (`#FFFFFF` surface, `#1A1C20` primary text).
- **Font loading**: Pretendard Variable in CSS; system fallbacks are present for platform resilience.
- **Canonical anchor**: homepage hero search surface: centered question, pill search, category grid, district chips.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Pretendard Variable` (open-source Korean-first variable sans)
- **Body font**: `Pretendard Variable`
- **Code font**: `Fira Code` and `ui-monospace` appear in CSS, not central to homepage UI.
- **Weight normal / semibold / bold**: `400` / `600` / `700`

```css
:root {
  --seed-font-weight-regular: 400;
  --seed-font-weight-medium: 500;
  --seed-font-weight-bold: 700;
  --carotene-font-weight-regular: 400;
  --carotene-font-weight-semibold: 600;
  --carotene-font-weight-bold: 700;
}
body {
  font-family: "Pretendard Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Pretendard Variable** is the real target. If unavailable, use `Noto Sans KR` before generic system UI for Korean rhythm.
- **Open-source substitute**: `Noto Sans KR` at 400/600/700, with body line-height kept near Seed's 16px -> 22px ladder.
- **Adjustment**: avoid Inter-only fallback for Korean pages. Inter makes Hangul spacing feel borrowed; `Noto Sans KR` preserves the compact local-service tone better.
- **Do not compensate with negative tracking**. Daangn's homepage does not rely on display tracking; its density comes from scale and spacing.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `--seed-font-size-t1-static` | 11px | 400 | 15px | 0 |
| `--seed-font-size-t2-static` | 12px | 400 | 16px | 0 |
| `--seed-font-size-t3-static` | 13px | 400/500 | 18px | 0 |
| `--seed-font-size-t4-static` | 14px | 400/600 | 19px | 0 |
| `--seed-font-size-t5-static` | 16px | 400/600 | 22px | 0 |
| `--seed-font-size-t6-static` | 18px | 600 | 24px | 0 |
| `--seed-font-size-t7-static` | 20px | 600 | 27px | 0 |
| `--seed-font-size-t8-static` | 22px | 600/700 | 30px | 0 |
| `--seed-font-size-t9-static` | 24px | 700 | 32px | 0 |
| `--seed-font-size-t10-static` | 26px | 700 | 35px | 0 |
| `--carotene-font-size-50` | .688rem | 400 | inherited | 0 |
| `--carotene-font-size-500` | 1.75rem | 700 | inherited | 0 |

> ⚠️ Key insight: the homepage headline feels large because it is centered in empty space, not because the font scale is huge. The extracted Seed top static size is only 26px.

### Principles
<!-- SOURCE: manual -->

1. Body reading starts at 14-16px, not an editorial 18px. Daangn optimizes for compact search, chips, and local listings.
2. Weight 700 is rare and functional. It marks the hero/search question or category labels, not decorative display copy.
3. Weight 600 is the main emphasis weight for UI labels. It is softer than 700 and keeps cards approachable.
4. Letter-spacing is effectively neutral. Do not add tight tracking just because the layout is minimal.
5. The scale is Korean-product dense: line-height is enough for readability, but not the loose Western SaaS rhythm.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (10 steps)
<!-- seed-color-palette-carrot-* -->

| Token | Hex |
|---|---|
| `--seed-color-palette-carrot-100` | `#FFF2EC` |
| `--seed-color-palette-carrot-200` | `#FFE8DB` |
| `--seed-color-palette-carrot-300` | `#FFD5C0` |
| `--seed-color-palette-carrot-400` | `#FFB999` |
| `--seed-color-palette-carrot-500` | `#FF9364` |
| `--seed-color-palette-carrot-600` | `#FF6600` |
| `--seed-color-palette-carrot-700` | `#E14D00` |
| `--seed-color-palette-carrot-800` | `#B93901` |
| `--seed-color-palette-carrot-900` | `#862B00` |
| `--seed-color-palette-carrot-1000` | `#471601` |

### 06-2. Brand Dark Variant
<!-- SOURCE: auto -->

| Token | Hex |
|---|---|
| `--seed-color-palette-carrot-600` | `#E65200` |
| `--seed-color-palette-carrot-700` | `#FF6600` |
| `--seed-color-palette-carrot-800` | `#FF9E65` |
| `--seed-color-palette-carrot-1000` | `#F4EEEA` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light (`gray`) | Dark (`gray`) |
|---|---|---|
| 00 | `#FFFFFF` | `#000000` |
| 100 | `#F7F8F9` | `#16171B` |
| 200 | `#F3F4F5` | `#1D2025` |
| 300 | `#EEEFF1` | `#2B2E35` |
| 400 | `#DCDEE3` | `#393D46` |
| 500 | `#B0B3BA` | `#5B606A` |
| 600 | `#868B94` | `#868B94` |
| 700 | `#5B606A` | `#B0B3BA` |
| 800 | `#555D6D` | `#DCDEE3` |
| 900 | `#2A3038` | `#E9EAEC` |
| 1000 | `#1A1C20` | `#F3F4F5` |

### 06-4. Accent Families
<!-- SOURCE: auto -->

| Family | Key step | Hex |
|---|---|---|
| Blue | 600/700 | `#1E82EB`, `#41A2F9` |
| Green | 600 | `#1B946D` |
| Red | 600 | `#F73526` |
| Yellow | 600/800 | `#B6720D`, `#DAB156` |
| Warmth | l5/l6 | `#FFB84D`, `#FF6E1D` |

### 06-5. Semantic
<!-- SOURCE: auto -->

| Token | Hex | Usage |
|---|---|---|
| `--seed-color-bg-brand-solid` | `#FF6600` | primary action background |
| `--seed-color-bg-brand-solid-pressed` | `#E14D00` | pressed/active brand action |
| `--seed-color-bg-layer-default` | `#FFFFFF` | default surface |
| `--seed-color-bg-layer-basement` | `#F3F4F5` | page background / low layer |
| `--seed-color-fg-neutral` | `#1A1C20` | primary text |
| `--seed-color-fg-neutral-muted` | `#555D6D` | secondary labels in light mode |
| `--seed-color-stroke-neutral-weak` | `#DCDEE3` | weak border/hairline |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--carotene-color-bg-brand-solid` | `#FF6600` | app-facing brand fill |
| `--carotene-color-fg-brand` | `#FF6600` | brand foreground/icon |
| `--carotene-color-bg-layer-default` | `#FFFFFF` | component surface |
| `--carotene-color-bg-neutral` | `#EEEFF1` / neutral role | service cards and chips |
| `--carotene-color-fg-neutral` | `#1A1C20` | primary text |
| `--carotene-color-fg-neutral-muted` | `#555D6D` | keyword text and subdued links |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---|---:|
| transparent black | `#00000000` | 19 |
| static black | `#000000` | 14 |
| static white | `#FFFFFF` | 10 |
| logo/pattern carrot | `#FF6F0F` | 9 |
| brand carrot | `#FF6600` | 7 |
| blue icon accent | `#1E82EB` | 5 |
| border gray | `#DCDEE3` | 4 |
| neutral muted | `#868B94` | 4 |

### Color Stories
<!-- SOURCE: manual — top 4 colors only -->

**`{colors.primary}` (#FF6600)** — The carrot signal. It should appear on the logo, download CTA, category icons, and primary action fills. It is not a page background color.

**`{colors.surface-base}` (#FFFFFF)** — The homepage floor. White gives search and local categories room to feel trustworthy and utilitarian rather than salesy.

**`{colors.text-primary}` (#1A1C20)** — Near-black with a cool gray cast. Use it for hero text and labels instead of pure `#000000`; the slight softness is part of Daangn's approachable UI.

**`{colors.border-muted}` (#DCDEE3)** — Structural hairline for the search pill and quiet dividers. It should define boundaries without turning cards into outlined boxes.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--seed-dimension-x1` | 4px | atomic gap |
| `--seed-dimension-x2` | 8px | icon/text gap |
| `--seed-dimension-x3` | 12px | compact padding |
| `--seed-dimension-x4` | 16px | default horizontal padding |
| `--seed-dimension-x5` | 20px | nav-title spacing alias |
| `--seed-dimension-x6` | 24px | card inner rhythm |
| `--seed-dimension-x8` | 32px | grid gap / section gap |
| `--seed-dimension-x10` | 40px | small touch control height |
| `--seed-dimension-x12` | 48px | search/input height |
| `--seed-dimension-x16` | 64px | wide section padding |
| `--carotene-spacing-20` | 5rem | large desktop side padding |

**주요 alias**:
- `--seed-dimension-spacing-y-nav-to-title` -> `--seed-dimension-x5` (20px)
- `sprinkles_gap_8_base` -> `--carotene-spacing-8` (2rem)
- `sprinkles_paddingLeft_16_medium` -> `--carotene-spacing-16` (4rem)

### Whitespace Philosophy
<!-- SOURCE: manual -->

The first fold uses whitespace as reassurance. The logo and download button sit high and small, while the question/search group floats in the center with enough empty white around it to feel like a start screen, not a catalog dump.

Below the search bar, whitespace compresses quickly. Category cards use 32px-ish gaps and compact padding, district chips sit closer together, and the page shifts from "breathe" to "browse". That contrast is the Daangn rhythm: open invitation first, dense neighborhood utility second.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `--seed-radius-r0_5` | 2px | micro controls |
| `--seed-radius-r1` | 4px | small tags |
| `--seed-radius-r1_5` | 6px | app download button |
| `--seed-radius-r2` | 8px | compact card/control |
| `--seed-radius-r3` | 12px | service cards |
| `--seed-radius-r4` | 16px | larger containers |
| `--seed-radius-r6` | 24px | soft panels |
| `--seed-radius-full` | 9999px | search pill, chips, circular controls |
| `--carotene-radius-full` | 9999px | Sprinkles full-radius utility |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| chrome | none observed on homepage cards | service/category cards rely on #F7F8F9 fill and radius |
| overlay | `#00000080` / alpha tokens | modal or image-lightbox overlay variables |
| search emphasis | border + white surface, not shadow | pill search reads through shape and hairline |

Daangn's homepage does not use shadow as a primary hierarchy tool. If you add box-shadows to cards, the page becomes a generic listing marketplace instead of a clean neighborhood directory.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| `--carotene-enter-opacity` | `0` | enter animation variable |
| `--carotene-enter-scale` | `.98` | soft scale-in variable |
| `--carotene-enter-translate-y` | `.5rem` | small vertical entrance |
| category card hover | `background-color .15s` | card/chip hover feedback |
| Seed input outline | `var(--seed-duration-d3) var(--seed-timing-function-easing)` | focus/clear button outline |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `1400px` appears on a wrapper (`._1j555bm0`).
- **Grid type**: Flex/Sprinkles utility layout; homepage service cards form a responsive multi-column row.
- **Column count**: 4 cards per row in the captured desktop hero section.
- **Gutter**: `--carotene-spacing-8` (2rem / 32px) for the card grid, tighter chip gaps below.

### Hero
- **🆕 Pattern Summary**: `~70vh + solid #FFFFFF + centered H1/search + category grid below`
- Layout: one-column centered search surface with top logo/download navigation.
- Background: `#FFFFFF` solid surface.
- **🆕 Background Treatment**: solid `#FFFFFF`; no image overlay, no mesh gradient, no decorative illustration.
- H1: captured at large Korean display weight, implemented through Pretendard 700 and compact Seed scale.
- Max-width: search pill and category content centered in an approximate 760-900px visual lane; outer wrapper can extend to 1400px.

### Section Rhythm
```css
section {
  padding-inline: clamp(16px, 4rem, 5rem);
  max-width: 1400px;
}
.service-grid {
  gap: 32px;
}
.search-pill {
  height: 48px;
  border-radius: 9999px;
}
```

### Card Patterns
- **Card background**: `#F7F8F9` / neutral fill via `--carotene-color-bg-neutral`.
- **Card border**: none visible on category cards.
- **Card radius**: `12px` (`--carotene-radius-3`) for service cards.
- **Card padding**: approximately `20px` top/left with label anchored near bottom.
- **Card shadow**: none.
- **Hover**: background-color transition to neutral hover/pressed; no lift.

### Navigation Structure
- **Type**: minimal horizontal top bar.
- **Position**: static in captured homepage.
- **Height**: visually ~64px with logo left and app-download CTA right.
- **Background**: `#FFFFFF`.
- **Border**: none visible in hero.

### Content Width
- **Prose max-width**: not a prose site; search text is centered.
- **Container max-width**: `1400px` global wrapper, narrower search cluster.
- **Sidebar width**: N/A on homepage.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | base | Sprinkles base classes handle stacked and hidden states. |
| Tablet | 768px | `@media screen and (min-width: 768px)` introduces medium spacing/display behavior. |
| Desktop | 992px | `@media screen and (min-width: 992px)` enables larger layout lanes. |
| Large | 1200px | `@media screen and (min-width: 1200px)` expands desktop density. |

### Touch Targets
- **Minimum tap size**: 40px for Seed control base; 48px for search/input-like controls.
- **Button height (mobile)**: use `--seed-dimension-x10` (40px) minimum.
- **Input height (mobile)**: use `--seed-dimension-x12` (48px) for search.

### Collapsing Strategy
- **Navigation**: keep logo/action minimal; hide secondary links instead of wrapping.
- **Grid columns**: service cards collapse from 4 columns to fewer columns while preserving 12px card radius.
- **Sidebar**: no sidebar on homepage.
- **Hero layout**: remains centered one-column; search and chips reduce width before changing hierarchy.

### Image Behavior
- **Strategy**: homepage hero is icon/text-based rather than image-led.
- **Max-width**: icons are fixed-size inside card/chip layout.
- **Aspect ratio handling**: service cards maintain stable rectangle proportions through fixed padding/min-width patterns.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Download CTA**

```html
<button class="download-button">앱 다운로드</button>
```

| Spec | Value |
|---|---|
| Background | `#FF6600` |
| Text | `#FFFFFF` |
| Radius | 6px |
| Padding | approx 14px 16px |
| Weight | 600/700 visual emphasis |
| Hover/active | `#E14D00` pressed direction |

**Search submit circle**

```html
<button class="search-submit" aria-label="검색">→</button>
```

| Spec | Value |
|---|---|
| Background | `#2A3038` / dark neutral |
| Text/icon | `#FFFFFF` |
| Radius | 9999px |
| Size | approx 32px circle inside 48px search pill |

### Badges

Daangn's homepage uses chips more than badges.

```html
<a class="district-chip">송도동</a>
```

| Spec | Value |
|---|---|
| Background | `#F7F8F9` / neutral fill |
| Text | `#1A1C20` |
| Radius | 9999px |
| Padding | 8px 14px |
| State | neutral hover fill, no shadow |

### Cards & Containers

**Service category card**

```html
<a class="service-card">
  <span class="service-card__icon">...</span>
  <strong>중고거래</strong>
</a>
```

| Spec | Value |
|---|---|
| Background | `#F7F8F9` |
| Radius | 12px |
| Border | none |
| Shadow | none |
| Min-width | 100-124px observed across responsive variants |
| Hover | background-color .15s to neutral-hover |

### Navigation

```html
<header class="top-nav">
  <a class="logo">당근</a>
  <button>앱 다운로드</button>
</header>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Layout | horizontal, space-between |
| Logo | carrot icon + orange wordmark |
| CTA | compact orange rectangle, not pill |
| Border | none in hero |

### Inputs & Forms

**Hero search pill**

```html
<form class="search-pill">
  <button type="button">중고거래</button>
  <input placeholder="검색어를 입력해주세요" />
  <button type="submit">검색</button>
</form>
```

| Spec | Value |
|---|---|
| Height | 48px |
| Background | `#FFFFFF` |
| Border | `1px solid #DCDEE3` |
| Radius | 9999px |
| Placeholder | `#B0B3BA` / muted gray |
| Divider | thin vertical hairline between category and input |

### Hero Section

```html
<main class="home-hero">
  <h2>당근에서 맛집 찾고 계신가요?</h2>
  <form class="search-pill">...</form>
  <nav class="popular-keywords">...</nav>
  <section class="service-grid">...</section>
</main>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Alignment | centered |
| Primary question | icon + bold Korean question |
| Search | wide pill, centered |
| Secondary navigation | keyword text links + category cards + chips |

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-download** — compact orange rectangle for app acquisition.

| State | Spec |
|---|---|
| default | bg `#FF6600`, text `#FFFFFF`, radius 6px |
| hover | slightly darker carrot direction |
| active | `#E14D00` pressed token |
| disabled | use Seed disabled bg/text, not opacity-only |

**search-pill-primary** — homepage's dominant interactive object.

| State | Spec |
|---|---|
| default | bg `#FFFFFF`, border `#DCDEE3`, radius 9999px |
| focus | keep border/outline controlled by Seed input focus tokens |
| submit | dark circular arrow, not orange |

**service-card-neutral** — category entry point.

| State | Spec |
|---|---|
| default | bg `#F7F8F9`, radius 12px, no border |
| hover | neutral-hover background, no transform |
| active | neutral-pressed background |

**district-chip** — local region selector.

| State | Spec |
|---|---|
| default | bg `#F7F8F9`, radius 9999px |
| hover | neutral-hover background |
| active | no brand fill unless selected state is explicit |

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
carrot-coordinate-marker:
  description: "Brand orange works as a local coordinate marker, not a surface system."
  technique: "#FF6600 /* {colors.primary} */ on logo, download CTA, and category icons; #E14D00 /* {colors.primary-pressed} */ only for pressed action state; no full-width carrot background."
  applied_to: ["{component.button-download}", "{component.service-card}", "logo"]
  visual_signature: "A mostly white page with small carrot pins at the exact points of action and identity."

white-on-white-search-pill:
  description: "The hero search control is visible through geometry and hairline contrast rather than elevation."
  technique: "height: 48px; background: #FFFFFF /* {colors.surface-base} */; border: 1px solid #DCDEE3 /* {colors.border-muted} */; border-radius: 9999px; no box-shadow."
  applied_to: ["{component.search-pill}"]
  visual_signature: "A front-desk-window search bar that stays quiet even while becoming the hero's main object."

neutral-no-shadow-service-card:
  description: "Category cards build hierarchy with fill, radius, and hover color instead of marketplace-style depth."
  technique: "background: #F7F8F9 /* {colors.surface-raised} */; border-radius: 12px; padding: 20px; box-shadow: none; transition: background-color .15s ease."
  applied_to: ["{component.service-card}"]
  visual_signature: "Soft mailbox-like compartments that group services without lifting off the page."

local-chip-compression:
  description: "Neighborhood names compress into scan-friendly local tags instead of full CTA buttons."
  technique: "background: #F7F8F9 /* {colors.surface-raised} */; border-radius: 9999px; padding: 8px 14px; neutral hover fill; no brand fill unless explicitly selected."
  applied_to: ["{component.district-chip}"]
  visual_signature: "A row of district names that scans like a transit map, dense but not loud."

dark-submit-dot-in-white-pill:
  description: "Search submission is separated from brand orange by a compact neutral action dot."
  technique: "approx 32px circular submit inside 48px pill; background: #2A3038; color: #FFFFFF; border-radius: 9999px."
  applied_to: ["{component.search-pill}"]
  visual_signature: "A small dark punctuation mark at the end of a pale local-search sentence."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | local, question-shaped, immediately useful | "당근에서 맛집 찾고 계신가요?" |
| Primary CTA | practical acquisition, no hype | "앱 다운로드" |
| Search placeholder | polite Korean instruction | "검색어를 입력해주세요" |
| Category labels | noun-first everyday services | "중고거래", "알바/과외", "부동산" |
| Tone | neighborly utility, not campaign copy | popular search and district names |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Daangn — copy into your root stylesheet */
:root {
  /* Fonts */
  --dg-font-family: "Pretendard Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --dg-font-family-code: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  --dg-font-weight-normal: 400;
  --dg-font-weight-semibold: 600;
  --dg-font-weight-bold: 700;

  /* Brand */
  --dg-color-brand-100: #FFF2EC;
  --dg-color-brand-500: #FF9364;
  --dg-color-brand-600: #FF6600;
  --dg-color-brand-700: #E14D00;
  --dg-color-brand-900: #862B00;

  /* Surfaces */
  --dg-bg-page: #FFFFFF;
  --dg-bg-soft: #F7F8F9;
  --dg-text: #1A1C20;
  --dg-text-muted: #868B94;
  --dg-border: #DCDEE3;

  /* Key spacing */
  --dg-space-xs: 4px;
  --dg-space-sm: 8px;
  --dg-space-md: 16px;
  --dg-space-lg: 32px;
  --dg-space-xl: 64px;

  /* Radius */
  --dg-radius-button: 6px;
  --dg-radius-card: 12px;
  --dg-radius-pill: 9999px;
}

body {
  background: var(--dg-bg-page);
  color: var(--dg-text);
  font-family: var(--dg-font-family);
  font-weight: var(--dg-font-weight-normal);
}

.daangn-search-pill {
  height: 48px;
  border: 1px solid var(--dg-border);
  border-radius: var(--dg-radius-pill);
  background: var(--dg-bg-page);
}

.daangn-service-card {
  background: var(--dg-bg-soft);
  border: 0;
  border-radius: var(--dg-radius-card);
  padding: 20px;
  transition: background-color .15s ease;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Daangn-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        carrot: {
          100: '#FFF2EC',
          500: '#FF9364',
          600: '#FF6600',
          700: '#E14D00',
          900: '#862B00',
        },
        daangnGray: {
          0: '#FFFFFF',
          100: '#F7F8F9',
          400: '#DCDEE3',
          600: '#868B94',
          1000: '#1A1C20',
        },
      },
      fontFamily: {
        sans: ['Pretendard Variable', 'Noto Sans KR', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        daangnButton: '6px',
        daangnCard: '12px',
        daangnPill: '9999px',
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
| Brand primary | `{colors.primary}` | `#FF6600` |
| Brand pressed | `{colors.primary-pressed}` | `#E14D00` |
| Background | `{colors.surface-base}` | `#FFFFFF` |
| Soft surface | `{colors.surface-raised}` | `#F7F8F9` |
| Text primary | `{colors.text-primary}` | `#1A1C20` |
| Text muted | `{colors.text-muted}` | `#868B94` |
| Border | `{colors.border-muted}` | `#DCDEE3` |

### Example Component Prompts

#### Hero Section
```text
Daangn 스타일 홈페이지 히어로를 만들어줘.
- 배경: #FFFFFF
- 중앙 질문형 H1/H2: Pretendard Variable, weight 700, color #1A1C20
- 검색 영역: 48px height, #FFFFFF background, 1px solid #DCDEE3, 9999px radius
- CTA: #FF6600 app-download button, 6px radius, white text
- 아래에는 #F7F8F9 카드 8개를 12px radius로 배치하고 shadow는 쓰지 마
```

#### Card Component
```text
Daangn 서비스 카드 컴포넌트를 만들어줘.
- 배경: #F7F8F9
- radius: 12px
- border/shadow 없음
- padding: 20px
- icon은 #FF6600 또는 서비스별 accent, label은 #1A1C20 weight 600
- hover는 background-color .15s만, transform/lift 금지
```

#### Badge / Chip
```text
Daangn 지역 chip을 만들어줘.
- bg #F7F8F9, text #1A1C20
- radius 9999px, padding 8px 14px
- font Pretendard Variable 14px, weight 600
- 선택 상태가 아니면 #FF6600으로 채우지 마
```

#### Navigation
```text
Daangn 상단 네비게이션을 만들어줘.
- 흰 배경 #FFFFFF, border 없음
- 좌측은 carrot orange 로고, 우측은 #FF6600 앱 다운로드 버튼
- 링크가 많아지면 숨기고 hero search를 우선해
```

### Iteration Guide

- **색상 변경 시**: `#FF6600`은 action/icon/brand marker에만 사용. 배경 전체에 깔지 않는다.
- **폰트 변경 시**: Pretendard Variable 또는 Noto Sans KR 계열을 유지한다.
- **여백 조정 시**: 4px ladder를 유지하되 hero top은 넓고 카드/칩 영역은 조밀하게 둔다.
- **컴포넌트 추가 시**: shadow 대신 neutral fill + radius + hover background로 계층을 만든다.
- **다크 모드**: Seed dark ramp가 존재하지만 homepage capture는 light다. light 값을 우선 적용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#FFFFFF` as the main hero and navigation surface.
- Use `#FF6600` as a compact brand/action marker, especially logo, CTA, and icons.
- Keep service cards on `#F7F8F9` with 12px radius and no visible shadow.
- Use Pretendard Variable with 400/600/700 weights.
- Make search the visual anchor: 48px height, 9999px radius, `#DCDEE3` hairline.
- Let local keywords and district chips create density below the airy hero.

### ❌ DON'T

- 배경을 `#FFF2EC` 또는 `#FF6600`으로 두지 말 것 — 대신 hero/page는 `#FFFFFF` 사용.
- 기본 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#1A1C20` 사용.
- 카드 배경을 `#FFFFFF`로 두고 shadow를 붙이지 말 것 — 대신 `#F7F8F9` fill + shadow 없음.
- 검색 pill border를 `#B0B3BA`처럼 진하게 두지 말 것 — 대신 `#DCDEE3` hairline 사용.
- CTA pressed 상태를 `#FF9364`처럼 밝게 만들지 말 것 — 대신 `#E14D00` 방향으로 눌림을 표현.
- body에 `font-weight: 300` 또는 `800` 사용 금지 — Daangn은 400/600/700 중심이다.
- 카드를 hover에서 `transform: translateY(-4px)`로 띄우지 말 것 — background-color .15s 전환만 사용.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- Full-page brand wash: absent. #FF6600 never owns the whole hero background.
- Decorative gradients: zero in the captured homepage hero.
- Chrome shadow on cards: none. Service cards are fill-based.
- Editorial photography: none in the first fold. The homepage is search/icon/chip driven.
- Heavy display typography: absent. No 48-72px marketing headline rhythm.
- Negative tracking: absent from the visible system identity.
- Multi-brand palette: no second primary brand color. Blue/yellow/magenta appear as service icon accents only.
- Complex motion: no parallax, scroll choreography, or large transform-based hover behavior.
- Dense nav menus: absent in hero. Search and local discovery are the navigation.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-only evidence** — analysis reused `insane-design/daangn/index.html`, CSS, phase1 JSON, and the captured hero screenshot. Logged-in flows, chat, item detail, and posting flows were not visited.
- **Light mode is canonical here** — dark Seed tokens exist in CSS, but the provided screenshot and homepage capture are light. Dark-mode component mapping is partial.
- **Typography extractor had empty scale table** — font scale was reconstructed from CSS custom properties (`--seed-font-size-*`, `--seed-line-height-*`) instead of the `typography.json` scale object.
- **Logo SVG color contamination possible** — `#FF6F0F`, `#1E82EB`, and `#DAB156` appear in SVG/pattern or icon contexts. Brand color selection prioritized semantic carrot/action tokens over raw frequency.
- **Exact search/control dimensions are inferred from CSS tokens and screenshot** — 48px and 40px are supported by Seed dimensions, but pixel-perfect DOM layout was not remeasured in a browser during this pass.
- **Motion JavaScript not analyzed** — CSS transition and Carotene enter/exit variables were observed, but runtime animation triggers were not inspected.
- **Form validation states not surfaced** — search field, posting forms, login, and error/loading states are only represented through Seed component tokens, not direct page observation.
- **Output path differs from skill default** — this report is written to `plugins/insane-design/docs/reports/daangn/design.md` per request, not `insane-design/daangn/design.md`.
