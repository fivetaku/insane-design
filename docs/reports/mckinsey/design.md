---
schema_version: 3.2
slug: mckinsey
service_name: McKinsey & Company
site_url: https://www.mckinsey.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#2251FF"
primary_font: "McKinsey Sans"
font_weight_normal: 300
token_prefix: mdc

bold_direction: Editorial Authority
aesthetic_category: editorial
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: editorial-magazine
archetype_confidence: high
design_system_level: lv3
design_system_level_evidence: "MDC token namespace with 340 CSS variables, named color/font/spacing/elevation ramps, component action aliases, and consistent mdc-c component classes."

colors:
  primary: "#2251FF"
  secondary-deep-blue: "#051C2C"
  tertiary-cyan: "#00A9F4"
  surface: "#FFFFFF"
  surface-subtle: "#F0F0F0"
  text-primary: "#000000"
  text-muted: "#757575"
  border-subtle: "#D0D0D0"
typography:
  display: "Bower"
  body: "McKinsey Sans"
  ladder:
    - { token: display-xl, size: "7.5rem", weight: 300, line_height: "8.5rem" }
    - { token: display-lg, size: "5.75rem", weight: 300, line_height: "6rem" }
    - { token: h1, size: "4.75rem", weight: 300, line_height: "4.75rem" }
    - { token: h2, size: "4rem", weight: 300, line_height: "4rem" }
    - { token: h3, size: "2.75rem", weight: 300, line_height: "2.75rem" }
    - { token: body, size: "1rem", weight: 300, line_height: "1.5rem" }
  weights_used: [300, 400, 500, 600, 700]
  weights_absent: [800]
components:
  button-primary: { bg: "{colors.surface}", text: "{colors.text-primary}", hover_bg: "{colors.tertiary-cyan}", radius: "0" }
  button-secondary: { bg: "{colors.tertiary-cyan}", text: "{colors.text-primary}", hover_bg: "{colors.surface}", radius: "0" }
  circular-arrow: { bg: "rgba(255,255,255,0.25)", icon: "{colors.surface}", shape: "50%" }
---

# DESIGN.md - McKinsey & Company

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

McKinsey's homepage behaves less like a SaaS landing page and more like an editorial command center. The first screen is built on a deep institutional blue-black field, `#051C2C` (`{colors.secondary-deep-blue}`), with a serif headline that asks a question instead of selling a feature. The surface is calm, but the grid is active: text block, circular arrow, book image, article card, interview card, and chatbot all occupy different weights in the same editorial spread.

The brand's visual memory is not the logo color. It is the collision between consulting gravity and magazine pacing: `Bower` display type for authority, `McKinsey Sans` for utility, and sharp MDC tokens underneath. The page feels like the front table of a global business newspaper after the editor has removed every loose sheet except the lead question. `#2251FF` (`{colors.primary}`) and `#00A9F4` (`{colors.tertiary-cyan}`) appear as controlled electricity: annotation marks, focus sparks, and action states, not a decorative wash.

The deep hero is not a dark mode and not a luxury black stage. `#051C2C` (`{colors.secondary-deep-blue}`) behaves like a midnight strategy room wall: dark enough to make white type and photography sit forward, but blue enough to keep institutional air inside the space. The cards do not float like app widgets; they read like dossiers pinned into a single spread. Photography becomes evidence, not ornament.

The system is intentionally square. Buttons default to `border-radius: 0`; cards are rectangular media planes; navigation is a white institutional bar with black typography. Where the site needs a softer gesture, it uses a circular icon container rather than rounding every component. It is the difference between a boardroom table and a round stamp: most surfaces remain cut and rectilinear, then the circle arrives as a command mark.

The homepage also has a strong negative identity. There is no second brand color trying to decorate the page, no friendly startup gradient, no pill CTA language, no bubbly card grid. Even when cyan enters, it behaves like a highlighter dragged once across a printed briefing. The craft is in editorial hierarchy, sharp component chassis, and the restraint around where color is allowed to speak.

조금 더 풀면, McKinsey 홈은 **글로벌 비즈니스 매거진의 편집실 벽**처럼 작동한다. 첫 dark hero는 마감 직전 편집자가 책상 위에 펼쳐 놓은 사설 한 장 — 헤드라인 하나, 질문 한 줄, 나머지는 인쇄 잉크로 가득 찬 검정. circular arrow는 잡지 칼럼 끝에 찍히는 편집자의 표시이고, book/interview/article card는 칼럼 사이에 끼워진 스토리북 발췌 — 한 spread 안에 매거진 사설과 인터뷰 칼럼이 동시에 펼쳐져 있다. `#2251FF`와 `#00A9F4`는 편집자가 빨간 펜 대신 들고 있는 형광펜 두 자루, 한 번씩만 그어진다. 두 번째 brand color가 없는 이유는, 사설 페이지에 잉크 색이 둘이면 칼럼이 흔들리기 때문이다.

### Key Characteristics

- Deep editorial hero field: `#051C2C` background with white serif display headline.
- Split identity typography: `Bower` for headlines, `McKinsey Sans` for body, navigation, and UI.
- MDC token namespace: `--mdc-color-*`, `--mdc-size-*`, `--mdc-elevation-*`, and component action aliases.
- Chromatic restraint: electric blue `#2251FF` and cyan `#00A9F4` act as interaction signals, not page wash.
- Rectangular component chassis: primary buttons and media cards avoid pill rounding.
- Circle as command: arrow and radial icons use `50%` shape as a specific action motif.
- Magazine-like collage: hero blends article, book, interview, and CTA surfaces in one asymmetric grid.
- Enterprise polish through spacing: 0.5rem base spacing escalates to 4rem and 5rem air.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Editorial Authority
> **Aesthetic Category**: editorial
> **Signature Element**: 이 사이트는 **deep-blue editorial command spread**으로 기억된다.
> **Code Complexity**: high — MDC tokens, responsive grid variants, action aliases, elevation tokens, and mixed editorial media components must be coordinated.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 McKinsey처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "McKinsey Sans", "Helvetica Neue", Calibri, Corbel, Helvetica, Roboto, sans-serif;
  font-weight: 300;
}
h1, h2, .display {
  font-family: "Bower", Georgia, "Times New Roman", serif;
  font-weight: 300;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #051C2C; --fg: #FFFFFF; --ink: #000000; }
body { background: #FFFFFF; color: var(--ink); }
.hero { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #2251FF; --accent: #00A9F4; }
.cta:hover { background: var(--accent); }
```

**절대 하지 말아야 할 것 하나**: McKinsey를 파란 SaaS 랜딩으로 만들지 말 것. 실제 첫 인상은 `#051C2C` editorial field + serif authority이며, `#2251FF`는 전체 배경이 아니라 interaction/token layer다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.mckinsey.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | reused existing phase1 artifacts + local CSS/HTML summary |
| HTML size | 649095 bytes |
| CSS files | 5 external/inline CSS files, total 1430219 chars |
| Token prefix | `mdc` |
| Method | CSS custom properties, resolved tokens, typography extraction, screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: componentized marketing/editorial site with MDC CSS modules and hashed component classes.
- **Design system**: McKinsey Design Components (`mdc`) — prefix `--mdc-*`.
- **CSS architecture**:
  ```css
  core        (--mdc-color-*, --mdc-size-*)       raw color, spacing, font, elevation values
  action      (--button-*)                        component state aliases
  component   (.mdc-c-*)                          hashed component classes and state modifiers
  utility     responsive grid/helper classes      repeat(N, minmax(0, 1fr)) and breakpoint variants
  ```
- **Class naming**: `mdc-c-*` component classes with hashed suffixes, plus modifier forms like `--primary`, `--secondary`, `:hover`, and disabled/action states.
- **Default theme**: mixed. Global page is white, homepage hero uses `#051C2C`, cards frequently overlay image media with white text.
- **Font loading**: custom corporate fonts exposed through CSS variables: `--mdc-font-family-default-primary` and `--mdc-font-family-default-secondary`.
- **Canonical anchor**: the homepage hero at `https://www.mckinsey.com/` with the line "What's your next brilliant move?"

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Bower` (corporate serif)
- **Body font**: `McKinsey Sans` (corporate sans)
- **Code font**: system monospace fallback; no prominent code UI on homepage
- **Weight normal / bold**: `300` / `700`

```css
:root {
  --mdc-font-family-default-secondary: "Bower", Georgia, "Times New Roman", serif;
  --mdc-font-family-default-primary: "McKinsey Sans", "Helvetica Neue", Calibri, Corbel, Helvetica, Roboto, Droid, sans-serif;
  --mdc-font-weight-light: 300;
  --mdc-font-weight-regular: 400;
  --mdc-font-weight-medium: 500;
  --mdc-font-weight-bold: 700;
}
body {
  font-family: var(--mdc-font-family-default-primary);
  font-weight: var(--mdc-font-weight-light);
}
```

### Note on Font Substitutes

- **Bower** is the signature display face. If unavailable, use **Georgia** or **Libre Baskerville** at weight `400`, then tighten the display block by keeping line-height close to `1.0`. Do not replace it with Inter or another neutral sans; the homepage loses the consulting-editorial voice immediately.
- **McKinsey Sans** can be substituted with **Helvetica Neue** or **IBM Plex Sans** at weight `300/400`. Use `font-weight: 300` for body copy where the original uses `--mdc-font-weight-light`; using 400 everywhere makes the site feel heavier and less editorial.
- Keep display letter-spacing conservative. The observed CSS does not depend on extreme negative tracking; authority comes from serif scale and line breaks, not optical compression.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `--mdc-size-font-120` | `7.5rem` | 300 | `8.5rem` | normal |
| `--mdc-size-font-92` | `5.75rem` | 300 | `6rem` | normal |
| `--mdc-size-font-76` | `4.75rem` | 300 | `4.75rem` | normal |
| `--mdc-size-font-64` | `4rem` | 300 | `4rem` | normal |
| `--mdc-size-font-52` | `3.25rem` | 300 | `3.25rem` | normal |
| `--mdc-size-font-44` | `2.75rem` | 300 | `2.75rem` | normal |
| `--mdc-size-font-36` | `2.25rem` | 300 | `2.25rem` | normal |
| `--mdc-size-font-28` | `1.75rem` | 300/400 | `1.75rem` | normal |
| `--mdc-size-font-20` | `1.25rem` | 300/400 | `2rem` | normal |
| `--mdc-size-font-16` | `1rem` | 300/400 | `1.5rem` | normal |
| `--mdc-size-font-14` | `0.875rem` | 400/500 | `1.25rem` | normal |
| `--mdc-size-font-12` | `0.75rem` | 500/700 | `1rem` | caps/label use |

> ⚠️ Key insight: McKinsey's type is not "big Inter." The display voice is serif and light; the UI voice is sans and precise; both are wired through MDC size tokens.

### Principles

1. Display scale is steep: `4.75rem` and above are normal in hero/editorial contexts, so shrinking H1 to 48px destroys the brand posture.
2. Body copy defaults light: `font-weight: 300` appears as a first-class token and must remain available.
3. Serif is reserved for authority. Use `Bower` for headline moments, not badges, nav, or dense UI.
4. Weight 500 exists, but as UI emphasis. Do not make every nav/link medium; the site relies on lighter text fields.
5. Letter-spacing is restrained. McKinsey gets sharpness from typeface selection, line-height, and contrast, not from aggressive tracking.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (9 steps)

| Token | Hex |
|---|---|
| `--mdc-color-electric-blue-50` | `#D9E8FC` |
| `--mdc-color-electric-blue-100` | `#CCE1FF` |
| `--mdc-color-electric-blue-200` | `#99C4FF` |
| `--mdc-color-electric-blue-300` | `#6E9DFF` |
| `--mdc-color-electric-blue-400` | `#2972FF` |
| `--mdc-color-electric-blue-500` | `#2251FF` |
| `--mdc-color-electric-blue-600` | `#1C44DC` |
| `--mdc-color-electric-blue-700` | `#1537BA` |
| `--mdc-color-electric-blue-900` | `#061F79` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--mdc-color-palette-deep-blue` | `#051C2C` |
| `--mdc-color-deep-blue-500` | `#2B5580` |
| `--mdc-color-deep-blue-700` | `#103559` |
| `--mdc-color-deep-blue-800` | `#082644` |
| `--mdc-color-deep-blue-900` | `#051C2C` |
| `--mdc-color-deep-blue-1000` | `#031119` |

### 06-3. Neutral Ramp

| Step | Light/Neutral | Hex |
|---|---|---|
| white | `--mdc-color-neutral-white` | `#FFFFFF` |
| gray-02 | `--mdc-color-neutral-gray-02` | `#FAFAFA` |
| gray-03 | `--mdc-color-neutral-gray-03` | `#F7F7F7` |
| gray-04 | `--mdc-color-neutral-gray-04` | `#F5F5F5` |
| gray-06 | `--mdc-color-neutral-gray-06` | `#F0F0F0` |
| gray-10 | `--mdc-color-neutral-gray-10` | `#E6E6E6` |
| gray-18 | `--mdc-color-neutral-gray-18` | `#D0D0D0` |
| gray-30 | `--mdc-color-neutral-gray-30` | `#B3B3B3` |
| gray-54 | `--mdc-color-neutral-gray-54` | `#757575` |
| gray-80 | `--mdc-color-neutral-gray-80` | `#333333` |
| black | `--mdc-color-neutral-black` | `#000000` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| cyan | `--mdc-color-cyan-500` | `#00A9F4` |
| cyan dark | `--mdc-color-cyan-900` | `#084D91` |
| functional orange | `--mdc-color-functional-mckinsey-orange` | `#FAA082` |
| functional red | `--mdc-color-functional-mckinsey-red` | `#E5546C` |
| functional purple | `--mdc-color-functional-mckinsey-purple` | `#8C5AC8` |
| status green | `--mdc-color-status-green` | `#007F26` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--mdc-color-primary` | `#2251FF` | brand/electric blue action layer |
| `--mdc-color-secondary` | `#051C2C` | deep editorial surface |
| `--mdc-color-tertiary` | `#00A9F4` | hover, focus, secondary action |
| `--mdc-color-status-blue` | `#2251FF` | status/info blue |
| `--mdc-color-status-red` | `#D51F31` | error/destructive states |
| `--mdc-color-status-green` | `#007F26` | success states |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--button-primary-background` | `#FFFFFF` | primary button on dark hero |
| `--button-primary-text` | `#000000` | primary button label |
| `--button-primary-background-hover` | `#00A9F4` | primary hover fill |
| `--button-secondary-background` | `#00A9F4` | secondary filled button |
| `--button-secondary-background-hover` | `#FFFFFF` | secondary hover inversion |
| `--button-tertiary-text` | `#FFFFFF` | tertiary button on dark field |
| `--button-focus-default` | `#666666` | focus outline token |
| `--button-disabled-text` | `#757575` | disabled label |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---|---|
| chromatic editorial accent | `#FC0D9F` | 212 |
| neutral white | `#FFFFFF` / `#FFF` | 169+ |
| neutral black | `#000000` / `#000` | 107+ |
| electric blue | `#2251FF` | 101+ |
| cyan | `#00A9F4` | 64 |
| deep blue | `#051C2C` | 61 |
| gray surface | `#F0F0F0` | 27 |
| gray border | `#D8D8D8` | 20 |

### 06-8. Color Stories

**`{colors.secondary-deep-blue}` (`#051C2C`)** — The homepage's authority field. It is not a generic navy; it is the editorial floor behind the main question, white headline, and media collage.

**`{colors.primary}` (`#2251FF`)** — Electric blue is the system's branded action color, not the whole visual identity. Use it for tokens, links, focus/action emphasis, and high-signal UI.

**`{colors.tertiary-cyan}` (`#00A9F4`)** — Cyan carries hover and secondary action energy. It should feel like a precise interaction spark against dark/neutral surfaces.

**`{colors.surface}` (`#FFFFFF`)** — White is the institutional chrome: top navigation, primary button on dark hero, and clean article surfaces. It is a counterweight to the deep-blue hero, not the only page background.

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| `--mdc-size-spacing-base-unit` | `0.5rem` | base measurement |
| `--mdc-size-spacing-4` | `0.25rem` | micro offsets, small letter spacing-derived values |
| `--mdc-size-spacing-8` | `0.5rem` | icon/text gaps, compact button gap |
| `--mdc-size-spacing-16` | `1rem` | button horizontal padding, card inner padding |
| `--mdc-size-spacing-24` | `1.5rem` | component padding, medium gutters |
| `--mdc-size-spacing-32` | `2rem` | section/card padding |
| `--mdc-size-spacing-40` | `2.5rem` | large module padding |
| `--mdc-size-spacing-48` | `3rem` | editorial block spacing |
| `--mdc-size-spacing-64` | `4rem` | major vertical rhythm |
| `--mdc-size-spacing-80` | `5rem` | hero/section scale air |

**주요 alias**:
- `button gap` → `--mdc-size-spacing-8` (icon/text separation)
- `button padding` → `--mdc-size-spacing-8 --mdc-size-spacing-16`
- `section air` → `--mdc-size-spacing-64` to `--mdc-size-spacing-80`

### Whitespace Philosophy

McKinsey uses whitespace as editorial pacing, not as friendly emptiness. The nav is compact and businesslike, then the hero opens into a large dark field where the headline and article modules have enough air to feel curated rather than stacked.

The grid can be dense below the fold, but the unit system remains sober: 0.5rem increments, 1rem component padding, 2rem module padding, and 4rem-plus section air. Avoid arbitrary 13px/27px offsets; the brand reads best when the spacing math stays institutional.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--mdc-size-border-radius-2` | `0.125rem` | small controls |
| `--mdc-size-border-radius-4` | `0.25rem` | compact UI elements |
| `--mdc-size-border-radius-8` | `0.5rem` | cards/containers where softened corners are needed |
| `--mdc-size-border-radius-10` | `0.625rem` | larger surfaces |
| `--mdc-size-border-radius-20` | `1.25rem` | rare rounded components |
| direct `0` | `0` | buttons and editorial media chassis |
| direct `50%` | `50%` | circular arrow/radial icon containers |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| `--mdc-elevation-2` | `0px 2px 4px -1px rgba(5, 28, 44, 0.2), 0px 0px 1px 0px rgba(5, 28, 44, 0.2)` | subtle raised module |
| `--mdc-elevation-4` | `0px 4px 8px -1px rgba(5, 28, 44, 0.2), 0px 0px 1px 0px rgba(5, 28, 44, 0.15)` | card hover or dropdown |
| `--mdc-elevation-8` | `0px 8px 16px -1px rgba(5, 28, 44, 0.2), 0px 0px 1px 0px rgba(5, 28, 44, 0.15)` | elevated overlays |
| `--mdc-elevation-16` | `0px 16px 32px -1px rgba(5, 28, 44, 0.2), 0px 0px 1px 0px rgba(5, 28, 44, 0.15)` | modal/major elevation |
| button hover | `0 7px 14px 0 #0003` | primary/secondary hover depth |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Pattern | Value | Usage |
|---|---|---|
| hover color swap | background changes to `#00A9F4` or `#FFFFFF` | button inversion |
| hover shadow | `0 7px 14px 0 #0003` | raised button feedback |
| media playback controls | play/mute labels present in hero media | video/interview surfaces |
| chatbot overlay | fixed lower-right widget | assistant entry point |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: common values include `90rem`, `77rem`, `900px`, `624px`, and percentage widths.
- **Grid type**: CSS Grid and Flexbox hybrid.
- **Column count**: responsive utilities include `repeat(1)` through `repeat(12, minmax(0, 1fr))`; hero uses asymmetric editorial placement.
- **Gutter**: spacing tokens from `0.5rem` to `2rem`; larger section air uses `4rem` and `5rem`.

### Hero
- **Pattern Summary**: dark editorial field + large serif question + asymmetric media/article collage + circular arrow command.
- Layout: multi-zone editorial grid; left headline/body, middle action cue, lower-left book/article cards, right large interview card.
- Background: solid `#051C2C`.
- **Background Treatment**: solid deep blue; no decorative gradient mesh behind the hero.
- H1: `Bower`, approximately `4rem` to `4.75rem` desktop, light weight, tight multi-line lockup.
- Max-width: content is visually constrained inside a wide desktop canvas, not full-bleed text.

### Section Rhythm

```css
section {
  padding: var(--mdc-size-spacing-64) var(--mdc-size-spacing-24);
  max-width: 90rem;
}
```

### Card Patterns
- **Card background**: image/media cards with white text overlay, or white/gray editorial surfaces.
- **Card border**: usually none on image cards; structural hairlines use neutral gray tokens.
- **Card radius**: mostly `0`; some UI containers use `--mdc-size-border-radius-8`.
- **Card padding**: `1rem` to `2rem`, depending on density.
- **Card shadow**: restrained; elevation tokens exist but homepage media cards rely more on image contrast.

### Navigation Structure
- **Type**: horizontal desktop nav plus left menu icon.
- **Position**: top page chrome; screenshot shows static/sticky-like white bar at viewport top.
- **Height**: approximately `90px` in captured desktop viewport.
- **Background**: `#FFFFFF`.
- **Border**: minimal; separation comes from hard white-to-dark contrast.

### Content Width
- **Prose max-width**: around `500px` to `624px` for hero copy/article snippets.
- **Container max-width**: `90rem` common upper bound.
- **Sidebar width**: no persistent sidebar on homepage; navigation is top-oriented.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| XS | `320px` | smallest supported viewport token |
| SM | `375px` | small mobile token |
| MD | `480px` | mobile/tablet transition |
| LG | `768px` | tablet and desktop nav/layout transition |
| XL | `1180px` | wide desktop content expansion |
| XXL | `1440px` | large desktop editorial canvas |
| XXXL | `1920px` | ultra-wide ceiling |

### Touch Targets
- **Minimum tap size**: infer 44px+ for nav icons and chatbot surface; exact mobile screenshot not captured.
- **Button height (mobile)**: driven by `--mdc-size-spacing-8 --mdc-size-spacing-16` and text line-height tokens.
- **Input height (mobile)**: not observed on homepage.

### Collapsing Strategy
- **Navigation**: hamburger/menu icon remains available; desktop link list likely collapses at smaller breakpoints.
- **Grid columns**: utility classes support `repeat(1)` through `repeat(12)`, indicating responsive column collapse.
- **Sidebar**: no persistent sidebar.
- **Hero layout**: asymmetric desktop editorial collage should collapse into stacked headline/media modules.

### Image Behavior
- **Strategy**: media-card image fills card surface.
- **Max-width**: frequent `max-width: 100%`.
- **Aspect ratio handling**: image cards preserve editorial crop; exact `object-fit` mapping not fully measured.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<button class="mdc-c-button mdc-c-button--primary">
  <span>Explore</span>
</button>
```

| Property | Value |
|---|---|
| Base display | inline-flex / center aligned |
| Gap | `--mdc-size-spacing-8` |
| Padding | `--mdc-size-spacing-8 --mdc-size-spacing-16` |
| Radius | `0` |
| Primary bg/text | `#FFFFFF` / `#000000` |
| Primary hover | bg `#00A9F4`, border `#00A9F4`, shadow `0 7px 14px 0 #0003` |
| Focus | `--button-focus-default` (`#666666`) |
| Disabled | muted text `#757575`, partially transparent background tokens |

### Badges

Badges are not a dominant homepage primitive. Label-like text appears as editorial metadata such as `INTERVIEW`, `BLOG POST`, and `BOOK`, typically uppercase, white on media, with sans-serif precision rather than rounded badge containers.

| Property | Value |
|---|---|
| Font | `McKinsey Sans` |
| Size | around `0.875rem` to `1rem` |
| Weight | 400/500 |
| Transform | uppercase metadata |
| Container | none or transparent; avoid pill badges |

### Cards & Containers

```html
<article class="mck-c-card mck-c-card--media">
  <img alt="" />
  <div class="mck-c-card__content">
    <p>BLOG POST</p>
    <h3>McKinsey and AI...</h3>
  </div>
</article>
```

| Property | Value |
|---|---|
| Background | media image or `#FFFFFF` / `#F0F0F0` |
| Border | usually none on media cards |
| Radius | `0` for editorial cards; token radius only for utility containers |
| Padding | `1rem` to `2rem` |
| Text overlay | white on darkened image |
| Shadow | optional MDC elevation, not mandatory chrome |

### Navigation

```html
<header class="mck-c-header">
  <button class="mck-c-menu-button"></button>
  <a class="mck-c-logo">McKinsey &amp; Company</a>
  <nav>...</nav>
  <button class="mck-c-search"></button>
</header>
```

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#000000` / neutral dark |
| Height | about `90px` desktop in screenshot |
| Logo | black wordmark |
| Link style | sans-serif, 14-16px, regular |
| Search | large outlined icon at right |

### Inputs & Forms

Homepage evidence is limited to search/chatbot entry points rather than full form fields. Use MDC neutral borders and focus tokens if implementing forms.

| State | Spec |
|---|---|
| default | border `#D0D0D0`, bg `#FFFFFF`, text `#000000` |
| focus | outline/border `#666666` or action blue when context requires |
| error | status red `#D51F31` |
| disabled | text `#757575`, muted gray surface |

### Hero Section

```html
<section class="mck-c-hero">
  <h1>What's your next brilliant move?</h1>
  <p>Game-changing work. People-powered growth...</p>
  <button class="mck-c-hero__arrow">→</button>
  <article class="mck-c-hero-card">...</article>
</section>
```

| Property | Value |
|---|---|
| Background | `#051C2C` |
| Text | `#FFFFFF` |
| H1 font | `Bower`, light |
| Body font | `McKinsey Sans`, light/regular |
| Action motif | circular arrow on muted translucent surface |
| Media | rectangular editorial cards, image overlay |

### 13-2. Named Variants

| Variant | Spec | State notes |
|---|---|---|
| `button-primary-dark-hero` | bg `#FFFFFF`, text `#000000`, radius `0` | hover bg `#00A9F4`, shadow `0 7px 14px 0 #0003` |
| `button-secondary-cyan` | bg `#00A9F4`, text `#000000`, radius `0` | hover inverts to white |
| `button-tertiary-outline-dark` | transparent bg, white text/border | hover white fill with black text |
| `circular-arrow-command` | circle `50%`, large white arrow, muted blue-gray fill | used as hero command cue |
| `media-editorial-card` | rectangular image card, white overlay text | no pill/radius treatment |
| `top-nav-search-icon` | black line search, large hit area | no filled search box on desktop chrome |

### 13-3. Signature Micro-Specs

```yaml
deep-blue-editorial-command-field:
  description: "The homepage authority layer uses deep institutional blue as an editorial room, not as generic dark mode."
  technique: "background-color: #051C2C /* {colors.secondary-deep-blue} */; color: #FFFFFF; solid field with no decorative gradient mesh"
  applied_to: ["{component.Hero Section}", "{component.media-editorial-card}"]
  visual_signature: "A midnight strategy-room spread where white serif type and rectangular media dossiers move forward."

square-cta-cyan-lift:
  description: "McKinsey buttons stay rectangular by default, then reveal chroma and elevation only on interaction."
  technique: "border-radius: 0; padding: var(--mdc-size-spacing-8) var(--mdc-size-spacing-16); hover background-color: #00A9F4 /* {colors.tertiary-cyan} */; hover box-shadow: 0 7px 14px 0 #0003"
  applied_to: ["{component.button-primary}", "{component.button-secondary}"]
  visual_signature: "A hard-edged consulting control that flashes cyan like a single highlighted line in a printed brief."

translucent-circular-arrow-command:
  description: "Roundness is reserved for command icons instead of becoming the default component language."
  technique: "border-radius: 50%; background: rgba(255,255,255,0.25); icon color: #FFFFFF /* {colors.surface} */"
  applied_to: ["{component.circular-arrow}", "{component.Hero Section}"]
  visual_signature: "A circular stamp or direction marker interrupting an otherwise square editorial grid."

bower-question-headline:
  description: "The primary hero voice is a light serif question, giving the page newspaper authority instead of SaaS slogan energy."
  technique: "font-family: Bower, Georgia, 'Times New Roman', serif; font-weight: 300; font-size: clamp(3.25rem, 6vw, 4.75rem); line-height: 1; color: #FFFFFF"
  applied_to: ["{component.Hero Section}", "{typography.display}"]
  visual_signature: "A board-level editorial question typeset like the lead headline of a business paper."

mdc-enterprise-elevation-ramp:
  description: "Elevation exists as a restrained two-layer token ramp rather than universal card chrome."
  technique: "--mdc-elevation-2: 0px 2px 4px -1px rgba(5, 28, 44, 0.2), 0px 0px 1px 0px rgba(5, 28, 44, 0.2); --mdc-elevation-16: 0px 16px 32px -1px rgba(5, 28, 44, 0.2), 0px 0px 1px 0px rgba(5, 28, 44, 0.15)"
  applied_to: ["{component.Cards & Containers}", "{component.button-primary}"]
  visual_signature: "Enterprise depth that appears only when hierarchy needs proof, never as decorative floating cards."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | question or thesis, concise but expansive | "What's your next brilliant move?" |
| Primary CTA | action-oriented, understated | Explore / Learn more style labels |
| Editorial label | uppercase content type before headline | "INTERVIEW", "BLOG POST", "BOOK" |
| Subheading | broad business outcome language | "Game-changing work. People-powered growth." |
| Tone | senior, global, analytical, optimistic without startup cheer |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* McKinsey & Company — copy into your root stylesheet */
:root {
  /* Fonts */
  --mdc-font-family-default-secondary: "Bower", Georgia, "Times New Roman", serif;
  --mdc-font-family-default-primary: "McKinsey Sans", "Helvetica Neue", Calibri, Corbel, Helvetica, Roboto, Droid, sans-serif;
  --mdc-font-weight-light: 300;
  --mdc-font-weight-regular: 400;
  --mdc-font-weight-medium: 500;
  --mdc-font-weight-bold: 700;

  /* Brand */
  --mdc-color-electric-blue-100: #CCE1FF;
  --mdc-color-electric-blue-300: #6E9DFF;
  --mdc-color-electric-blue-500: #2251FF;
  --mdc-color-electric-blue-600: #1C44DC;
  --mdc-color-electric-blue-900: #061F79;
  --mdc-color-palette-cyan: #00A9F4;
  --mdc-color-palette-deep-blue: #051C2C;

  /* Surfaces */
  --mdc-bg-page: #FFFFFF;
  --mdc-bg-dark: #051C2C;
  --mdc-text: #000000;
  --mdc-text-muted: #757575;
  --mdc-border-subtle: #D0D0D0;

  /* Key spacing */
  --mdc-space-sm: 0.5rem;
  --mdc-space-md: 1rem;
  --mdc-space-lg: 2rem;
  --mdc-space-xl: 4rem;

  /* Radius */
  --mdc-radius-sm: 0.25rem;
  --mdc-radius-md: 0.5rem;
}

.mck-hero {
  background: #051C2C;
  color: #FFFFFF;
  padding: 4rem 1.5rem;
}

.mck-hero h1 {
  font-family: var(--mdc-font-family-default-secondary);
  font-size: clamp(3.25rem, 6vw, 4.75rem);
  line-height: 1;
  font-weight: 300;
}

.mck-button {
  border-radius: 0;
  padding: 0.5rem 1rem;
  font-family: var(--mdc-font-family-default-primary);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — McKinsey-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        mck: {
          blue: '#2251FF',
          cyan: '#00A9F4',
          deep: '#051C2C',
          white: '#FFFFFF',
          black: '#000000',
          gray06: '#F0F0F0',
          gray18: '#D0D0D0',
          gray54: '#757575',
        },
      },
      fontFamily: {
        sans: ['McKinsey Sans', 'Helvetica Neue', 'Calibri', 'Roboto', 'sans-serif'],
        serif: ['Bower', 'Georgia', 'Times New Roman', 'serif'],
      },
      fontWeight: {
        light: '300',
        regular: '400',
        medium: '500',
        bold: '700',
      },
      borderRadius: {
        mck0: '0',
        mck4: '0.25rem',
        mck8: '0.5rem',
      },
      boxShadow: {
        mck2: '0px 2px 4px -1px rgba(5,28,44,.2), 0 0 1px rgba(5,28,44,.2)',
        mck8: '0px 8px 16px -1px rgba(5,28,44,.2), 0 0 1px rgba(5,28,44,.15)',
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
| Brand primary | `--mdc-color-electric-blue-500` | `#2251FF` |
| Background dark | `--mdc-color-palette-deep-blue` | `#051C2C` |
| Background light | `--mdc-color-neutral-white` | `#FFFFFF` |
| Text primary | `--mdc-color-neutral-black` | `#000000` |
| Text muted | `--mdc-color-neutral-gray-54` | `#757575` |
| Border | `--mdc-color-neutral-gray-18` | `#D0D0D0` |
| Interaction accent | `--mdc-color-palette-cyan` | `#00A9F4` |
| Error | `--mdc-color-status-red` | `#D51F31` |

### Example Component Prompts

#### Hero Section
```
McKinsey 스타일 히어로 섹션을 만들어줘.
- 배경: #051C2C
- H1: Bower, clamp(3.25rem, 6vw, 4.75rem), weight 300, line-height 1
- 서브텍스트: #FFFFFF, McKinsey Sans, 1rem-1.125rem, line-height 1.5
- CTA/arrow: circular command button or square CTA, hover accent #00A9F4
- 레이아웃: 좌측 텍스트 + 우측/하단 editorial media card collage
- 전체 톤: SaaS hero가 아니라 business editorial spread
```

#### Card Component
```
McKinsey 스타일 미디어 카드 컴포넌트를 만들어줘.
- 배경: image with dark overlay or #FFFFFF editorial surface
- border-radius: 0
- 제목: Bower or McKinsey Sans depending on hierarchy
- metadata label: uppercase, McKinsey Sans, 14px, white on image
- hover 시: optional elevation, avoid playful scale bounce
- 색상: white/black/deep-blue first, #2251FF or #00A9F4 only for action
```

#### Badge
```
McKinsey 스타일 콘텐츠 라벨을 만들어줘.
- pill badge 금지
- font: McKinsey Sans, 12-14px, uppercase
- container 없이 텍스트 라벨로 배치
- 색상: dark media 위 #FFFFFF, light surface 위 #000000 또는 #757575
```

#### Navigation
```
McKinsey 스타일 상단 네비게이션을 만들어줘.
- 높이: 약 90px desktop
- 배경: #FFFFFF
- 로고: 좌측 black wordmark
- 링크: McKinsey Sans, 14-16px, weight 300/400, color #000000
- 검색: 우측 large line icon
- Sign In / Subscribe는 우측 상단 action link로 작게 배치
```

### Iteration Guide

- **색상 변경 시**: `#051C2C`, `#2251FF`, `#00A9F4`, `#FFFFFF`, `#000000` 역할을 섞지 말 것.
- **폰트 변경 시**: display serif와 body sans의 분리를 유지할 것.
- **여백 조정 시**: 0.5rem base에서 `1rem`, `2rem`, `4rem`, `5rem`로 확장할 것.
- **새 컴포넌트 추가 시**: 기본 radius `0`; 둥근 형태는 circular action에만 제한할 것.
- **다크 섹션**: deep blue 위 white text를 우선 사용하고, cyan은 hover/secondary action으로 남길 것.
- **반응형**: `320/375/480/768/1180/1440/1920px` breakpoint 체계를 따를 것.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#051C2C` as the authoritative dark editorial field for hero or major dark bands.
- Pair `Bower` display type with `McKinsey Sans` body/UI type.
- Keep primary editorial cards rectangular; let imagery and hierarchy create drama.
- Use `#00A9F4` as a precise hover/action accent rather than a background wash.
- Preserve MDC token naming when implementing: `--mdc-color-*`, `--mdc-size-*`, `--button-*`.
- Use circular action buttons deliberately for arrow/search/chat-type commands.
- Keep body copy light enough; `font-weight: 300` is part of the visual voice.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`만으로 두지 말 것 — hero/major editorial field는 `#051C2C` 사용.
- 텍스트를 dark hero에서 `#000000` 또는 `black`으로 두지 말 것 — dark field에서는 `#FFFFFF` 사용.
- 브랜드 액션을 `#0066CC` 같은 generic web blue로 바꾸지 말 것 — McKinsey action blue는 `#2251FF`, hover accent는 `#00A9F4`.
- Deep hero를 `#000000` 순흑으로 만들지 말 것 — 대신 `#051C2C` 사용.
- Primary dark-hero button을 `#2251FF` fill로 고정하지 말 것 — 실제 primary는 `#FFFFFF` fill에 hover `#00A9F4`.
- CTA 버튼에 `border-radius: 999px` pill을 쓰지 말 것 — 기본 button chassis는 `border-radius: 0`.
- Body 전체를 `font-weight: 400`으로만 만들지 말 것 — McKinsey Sans light `300`을 기본 rhythm에 포함.
- Display headline을 sans-serif로 만들지 말 것 — hero authority는 `Bower` serif에서 나온다.
- 모든 카드에 `box-shadow: 0 20px 40px rgba(...)`를 넣지 말 것 — media cards는 이미지/overlay 중심, elevation은 제한적으로.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Startup gradient hero: absent. The homepage hero is solid `#051C2C`, not purple/blue gradient.
- Pill-button language: absent from primary identity. Radius `0` is a feature, not a bug.
- Friendly pastel surfaces: none in the main editorial posture. Neutrals and deep blue carry the system.
- Rounded card grid as default: absent. Editorial media cards stay rectangular.
- Emoji/icon confetti: none. Icons are functional: menu, search, arrow, playback, chat.
- Single-font neutrality: absent. Serif/sans split is central.
- Heavy black-only dark mode: avoided. The dark field is deep blue, not pure `#000000`.
- Universal shadow chrome: absent. Elevation exists, but not every surface floats.
- Decorative second brand color: none. Cyan and electric blue have functional roles, not a broad rainbow palette.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual / REQUIRED -->

- **Homepage-only visual capture** — The screenshot and interpretation focus on `https://www.mckinsey.com/`; industry pages, article detail pages, search results, and subscription flows may introduce additional modules.
- **Desktop-first screenshot** — The observed hero crop is desktop width. Mobile layout behavior is inferred from breakpoint tokens and grid utilities, not a fresh mobile capture.
- **CSS token truth, not full JS behavior** — Color, typography, spacing, radius, and elevation values are grounded in CSS; scroll-triggered animation and runtime menu behavior were not fully instrumented.
- **Logo/media color contamination** — Frequency candidates include high chromatic values such as `#FC0D9F`; these may come from editorial imagery or SVG/media assets, so brand_color is anchored to MDC semantic/action tokens instead.
- **Form states under-observed** — Search/chatbot entry points are visible, but full form validation, loading, and error flows were not visited.
- **Dark-mode mapping incomplete** — The site uses dark editorial sections, but a complete alternate dark theme token map was not confirmed.
- **Font licensing not verified** — `Bower` and `McKinsey Sans` are treated as corporate fonts from CSS names; substitute guidance is practical, not license advice.
- **Exact hero dimensions vary** — The screenshot shows a large desktop composition; final H1 clamp and grid dimensions should be tuned against current viewport and live content.
