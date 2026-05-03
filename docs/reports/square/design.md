---
schema_version: 3.2
slug: square
service_name: Square
site_url: https://squareup.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#006AFF"
primary_font: "Square Sans Text VF"
font_weight_normal: 400
token_prefix: "square"

bold_direction: Editorial Commerce
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: commerce-marketplace
archetype_confidence: medium
design_system_level: lv3
design_system_level_evidence: "866 CSS variables, layered component CSS, action/component/core token tiers, and named typographic variants are present in the captured homepage."

colors:
  primary: "#006AFF"
  primary-hover: "#0055CC"
  surface-base: "#FFFFFF"
  surface-contrast: "#F7F6F5"
  text-primary: "#030303"
  text-secondary: "#737373"
  border-default: "#D9D9D9"
  dark-surface: "#000000"
  success: "#00B23B"
typography:
  display: "Square Sans Display VF"
  body: "Square Sans Text VF"
  mono: "Square Sans Mono VF"
  editorial_serif_proxy: "Cash Sans / exact-block display layer"
  ladder:
    - { token: body-small, size: "14px", weight: 400, line_height: "21px", tracking: "0" }
    - { token: body, size: "16px", weight: 400, line_height: "24px", tracking: "0" }
    - { token: h3, size: "28px", weight: 400, line_height: "38px", tracking: "-0.01em" }
    - { token: title, size: "40px", weight: 400, line_height: "50px", tracking: "-0.02em" }
    - { token: display-800, size: "74px", weight: 400, line_height: "1", tracking: "-1.48px" }
    - { token: display-900, size: "90px", weight: 400, line_height: "1", tracking: "-1.8px" }
  weights_used: [300, 400, 500, 600, 700]
  weights_absent: [800, 900]
components:
  button-primary: { bg: "{colors.primary}", fg: "#FFFFFF", radius: "5rem", padding: "1rem 2rem", min_width: "120px" }
  button-secondary-white: { bg: "#FFFFFF", fg: "{colors.primary}", radius: "5rem", border: "1px solid {colors.primary}" }
  link-button-standard: { bg: "{colors.primary}", fg: "#FFFFFF", radius: ".6rem", min_height: "5rem", padding: "1.3rem 1.6rem" }
  nav-link: { fg_light: "#030303", fg_dark: "#FFFFFF", weight: 500 }
  container-card: { radius: "1.6rem", alt_radius: "2.4rem", bg: "#FFFFFF" }
---

# DESIGN.md — Square

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Square's homepage behaves like a neighborhood commerce poster that has been typeset by a product-system team. The first viewport is not a sterile SaaS dashboard: it is a gritty, sunlit business image with a massive editorial headline laid directly over it. The page sells infrastructure, but it starts from place, shopfront, sidewalk, and local mythology.

The system underneath that image is strict. Almost every reusable UI decision collapses to black, white, gray, and one decisive blue, `#006AFF` (`{colors.primary}`). The blue is not decorative. It is transactional: CTA fill, link, focus outline, and action state. It works like the blue stamp on a paid invoice: one mark, one promise, no second brand color competing for the till.

Typography carries the personality split. Product UI uses `Square Sans Text VF` and `Square Sans Display VF`, with ordinary body copy at 400 and navigation at 500. The hero introduces a large editorial face through the Cash Sans / exact-block display layer, letting the homepage feel like a campaign without sacrificing the component system below it. The headline is not placed in a SaaS hero card; it is pasted across the storefront window, as if the glass itself were the layout grid.

The craft signature is scale contrast: 90px display type, 50px pill buttons, 1400px extra-large containers, and muted gray ramps that make photography do the emotional work. Shadow does not become chrome; the depth lives in the photo, like a countertop scene where the card reader, receipt, hand, and light carry the atmosphere while the interface stays flat and countable.

Square's strongest move is that the operating system hides under the counter. The homepage looks merchant-first, almost like a block-party poster or a shop-window campaign, but every CTA, focus ring, nav state, and container radius snaps back to the same product-system ledger. It is "local business, global operating system" rather than "developer platform."

조금 더 풀면, Square 홈은 **골목 시장의 매대 위에 세워진 카운터**처럼 작동한다. hero photography는 매대 너머 보이는 마켓 풍경이고, 그 위에 얹힌 oversized editorial type은 시장 입구 차양에 걸린 카탈로그 헤드라인처럼 손글씨에 가까운 표정으로 페이지 전체를 가른다. pill CTA는 카운터 위 결제 단말의 한 번의 탭 — 장바구니에 SKU가 떨어지는 순간이다. 우측 product card 행은 진열대 옆에 줄지어 놓인 상품 리스트, footer link 묶음은 매대 뒤편의 영수증 출력기 같은 부속 도구다. 두 번째 브랜드 컬러가 없는 이유는, 영수증에 찍히는 도장은 단 하나면 충분하기 때문이다.

### Key Characteristics

- Full-bleed hero photography with white editorial display type over the image.
- One interactive chromatic anchor: `#006AFF`, with `#0055CC` as hover/active darkening.
- Black/white/gray UI chassis, including `#030303`, `#1A1A1A`, `#737373`, `#D9D9D9`, and `#FFFFFF`.
- Large pill CTAs with `5rem` radius and scale/translate active behavior.
- A layered token model: base colors, action variants, component variants, and generated Svelte classes.
- Mobile-first container progression from 300px to 1400px.
- Strong focus-outline contract: 2px outline, 8px radius, 2px offset.
- Minimal chrome shadow; depth is mainly photographic or popover-specific.
- Homepage voice mixes local-business aspiration with operational verbs: sell, streamline, manage, get paid.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Editorial Commerce
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **full-bleed local-business photography plus oversized editorial commerce type**으로 기억된다.
> **Code Complexity**: high — layered CSS variables, tokenized action variants, responsive containers, animated nav and CTA states.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Square처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Square Sans Text VF", "Square Sans Text", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #030303; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #006AFF; --brand-hover: #0055CC; }
```

**절대 하지 말아야 할 것 하나**: Square를 파란 그라디언트 SaaS처럼 만들지 말 것. `#006AFF`는 버튼과 링크의 action color이고, 배경 장식 컬러가 아니다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://squareup.com` |
| Canonical | `https://squareup.com/us/en` |
| Fetched | 2026-04-14 local phase1 assets reused; v3.2 rewrite on 2026-05-03 |
| Extractor | cached HTML/CSS + phase1 JSON + screenshot |
| HTML size | 1,961,421 bytes |
| CSS files | 16 captured CSS files including `_inline.css` |
| Token prefix | `square` / native variables mostly unprefixed (`--color-*`, `--action-*`, `--text-*`) |
| Method | CSS custom properties, frequency candidates, screenshot, and homepage HTML structure |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Svelte-generated public web renderer with layered CSS output.
- **Design system**: Square public web design system; CSS layers include `reset`, `base`, `design-system`, `theme`, `design-system-components`, `standard-components`, `custom-components`, `generated-styles`, `utilities`, and `overrides`.
- **CSS architecture**:
  ```text
  core        --color-*, --font-size-*, --line-height-*, --space-*       raw scale values
  action      --action-variant-button-*, --action-size-*                 CTA/link behavior
  component   --container-*, tooltip, nav, link component variables       component chassis
  generated   .svelte-* classes, layout dynamic styles                    page-specific assembly
  ```
- **Class naming**: Svelte scoped classes plus semantic component names (`PublicWebNav`, `Action`, `LinkComponent--button`, `CtaSubnav`).
- **Default theme**: mixed; homepage hero and footer use dark/photo surfaces while content and system components define light/dark token branches.
- **Font loading**: `@font-face` from `square-fonts-production-f.squarecdn.com`, with `font-display: swap`.
- **Canonical anchor**: Square.com US English homepage with commerce platform positioning.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Square Sans Display VF`, `Square Sans Display`; hero also uses a Cash Sans / exact-block display layer.
- **Body font**: `Square Sans Text VF`, `Square Sans Text`, Helvetica, Arial, sans-serif.
- **Code font**: `Square Sans Mono VF`, `Square Sans Mono`, `ui-monospace`, Menlo, Courier New.
- **Weight normal / bold**: `400` / `700`; medium and semibold are used for navigation/actions.

```css
:root {
  --square-sans-text: "Square Sans Text VF", "Square Sans Text", helvetica, arial, sans-serif;
  --square-sans-display: "Square Sans Display VF", "Square Sans Display", helvetica, arial, sans-serif;
  --square-sans-mono: "Square Sans Mono VF", "Square Sans Mono", ui-monospace, menlo, "Courier New", monospace;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
}
body {
  font-family: var(--square-sans-text);
  font-weight: var(--font-weight-regular);
}
```

### Note on Font Substitutes

- **Square Sans Text VF** — proprietary Square font.
  - Open-source substitute: **Inter** at 400/500/600, with `line-height` kept close to Square's 1.5 body rhythm.
  - Adjustment: Square's body scale is 10px-root based (`1.6rem` = 16px). Do not shrink to 14px default body.
- **Square Sans Display VF** — proprietary display face.
  - Open-source substitute: **Inter Display** or **Helvetica Neue** at 400/500.
  - Adjustment: apply tighter tracking on display: `-0.02em` around 44-56px, `-0.03em` to `-0.04em` above 72px.
- **Cash Sans / exact-block hero display** — homepage campaign layer.
  - Substitute: a high-contrast editorial serif such as **Georgia** only for the hero if the serif campaign look is required.
  - Adjustment: keep `line-height: 1` and avoid bold weights; the Square hero relies on size and contrast, not heavy weight.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `--font-size-body-small` | 14px | 400 | 21px | 0 |
| `--font-size-body` | 16px | 400 | 24px | 0 |
| `--font-size-body-large` | 20px / 22px desktop | 400 | 30px / 34px | 0 |
| `--font-size-h3` | 28px | 400 | 38px | -0.01em |
| `--font-size-title` | 40px | 400 | 50px | -0.02em |
| `--text-variant-700` | 44px | 400/500 | 1 | -0.03em |
| `--text-variant-800` | 48px / 56px / 72px / 74px | 400/500 | 1 | -0.04em to -1.48px |
| `--text-variant-900` | 56px / 72px / 90px | 400/500 | 1 | -0.04em to -1.8px |
| `--font-size-button` | 16px | 500 | 22px | 0 |

> ⚠️ Square's display type should feel large but not heavy. The common mistake is using 700+ display weight; the captured system uses regular/medium display with tight tracking.

### Principles

1. Body copy stays at 16px / 24px. Square does not use tiny SaaS body text as the default.
2. Display contrast comes from size and letter-spacing, not from blackletter weight.
3. Navigation and CTA text use weight 500 to read as operational controls.
4. The 10px root scale makes `1rem` equal 10px; token values like `5rem` are 50px, not browser-default 80px.
5. The homepage can switch into an editorial display face for campaign impact, but components return to Square Sans.
6. Negative tracking increases with size: around `-.01em` at 18-20px, `-.02em` at 28-40px, and `-.04em` or pixel equivalents at hero scale.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| `--color-blue-light` | `#CEE7F3` |
| `--color-blue` / `--color-link-theme-white` | `#006AFF` |
| `--color-blue-dark` / hover-active | `#0055CC` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--color-blue-color-mode-dark` | `#1379F3` |
| `--color-link-theme-black` | `#1379F3` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white | `#FFFFFF` | `#FFFFFF` |
| gray-03 | `#F7F7F7` | N/A |
| gray-05 | `#F2F2F2` | N/A |
| gray-13 | `#E0E0E0` | N/A |
| gray-15 / border | `#D9D9D9` | N/A |
| gray-55 / muted | `#737373` | N/A |
| gray-80 | `#333333` | `#333333` |
| gray-90 / text | `#1A1A1A` | `#1A1A1A` |
| gray-99 / charcoal | `#030303` | `#030303` |
| black surface | `#000000` | `#000000` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| success | `--color-success` | `#00B23B` |
| red | `--color-red` | `#DF3320` |
| green | `--color-green` | `#0BB634` |
| plum | `--color-plum` | `#A1499C` |
| rose | `--color-rose` | `#C14F70` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--color-background-base-color-mode-light` | `#FFFFFF` | light page background |
| `--color-background-accent-color-mode-light` | `#F7F6F5` | warm contrast band |
| `--color-background-base-color-mode-dark` | `#000000` | dark page background |
| `--color-background-accent-color-mode-dark` | `#1F1F1F` | dark contrast band |
| `--color-text` | `#1A1A1A` | body text |
| `--color-heading-theme-white` | `#030303` | heading on light surface |
| `--color-border` | `#D9D9D9` | default hairline |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--color-link` | `--color-link-theme-white` → `#006AFF` | default light-mode link |
| `--color-link-hover` | `--color-blue-dark` → `#0055CC` | hover/active link |
| `--action-variant-button-background-color` | `--color-blue-fill` → `#006AFF` | primary button fill |
| `--action-variant-button-alt-background-color` | `#FFFFFF` | secondary pill background |
| `--action-variant-button-alt-text-color` | `#006AFF` | secondary pill text |
| `--accessibility-focus-outline-color` | `--color-link` → `#006AFF` | focus ring |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| black | `#000000` | 488 |
| white | `#FFFFFF` | 258 |
| gray-90 | `#1A1A1A` | 158 |
| blue | `#006AFF` | 86 |
| gray-80 | `#333333` | 68 |
| gray-15 | `#D9D9D9` | 65 |
| gray-20-ish | `#CCCCCC` | 30 |
| blue-dark | `#0055CC` | 25 |

### 06-8. Color Stories

**`{colors.primary}` (`#006AFF`)** — The single action blue. It marks primary CTAs, links, focus rings, and button states; it should not spill into decorative washes.

**`{colors.surface-base}` (`#FFFFFF`)** — The operational surface. Square's component system expects crisp white for forms, nav dropdowns, and CTA pills even when the hero photography is dark.

**`{colors.text-primary}` (`#030303`)** — The near-black editorial anchor. It gives headings a sharper tone than generic `#111111`, but the homepage can invert it to white over photography.

**`{colors.border-default}` (`#D9D9D9`)** — Quiet structure. Hairlines separate form and nav elements without introducing card-heavy SaaS chrome.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--space-none` | 0px | reset / no gap |
| `--space-5` | 5px | micro adjustment |
| `--space-10` | 10px | compact nav/button vertical rhythm |
| `--space-20` | 20px | standard gutter / card internal padding |
| `--space-30` | 30px | grouped nav sections |
| `--space-40` | 40px | section interior rhythm |
| `--space-60` | 60px | responsive section spacing |
| `--space-80` | 80px | large band rhythm |
| `--space-120` | 120px | button min width / large vertical spacing |
| `--space-160` | 160px | high-impact landing bands |
| `--space-200` | 200px | very large editorial air |

**주요 alias**:
- `--space-responsive-80` → `--space-60` on smaller viewports, expanding through responsive rules.
- `--action-variant-button-min-width` → `--space-120` (120px).

### Whitespace Philosophy

Square's whitespace is not airy luxury minimalism. It is marketplace-operational: large enough to make business photography and oversized headlines breathe, then compact enough for product/navigation choice surfaces. The hero takes the full visual field, but nav, CTA clusters, and footer columns stay dense and practical.

The spacing ladder is decimal and blunt: 10, 20, 30, 40, 60, 80, 120, 160, 200. That gives Square a retail-system feel rather than a delicate 4px software grid. Use big vertical bands for story, but keep controls and category lists close enough to scan.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `--action-variant-button-border-radius` | `5rem` / 50px | primary and alt pill buttons |
| `--container-border-radius-base` | `1.6rem` / 16px | standard containers/cards |
| `--container-border-radius-medium` | `2.4rem` / 24px | larger modules |
| `--accessibility-focus-outline-border-radius` | 8px | focus ring radius |
| `LinkComponent--button` | `.6rem` / 6px | older standard link button component |
| tooltip trigger | 100% | circular icon focus area |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| reset | `box-shadow: none` | inputs, buttons, tertiary nav reset |
| popover | `--tooltip-popover-box-shadow-primary`, `--tooltip-popover-box-shadow-ambient` | tooltip/popover surfaces |
| hero depth | image/video contrast, not CSS shadow | homepage visual depth |
| card chrome | mostly border/radius/surface | avoid generic card elevation |

Square uses shadow sparingly. The visible homepage relies on photography, contrast, and surface switching rather than stacked elevation. Do not add Linear-style multi-layer shadows to Square cards.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---:|---|
| `--duration-quick` | 125ms | hover color/background transitions |
| `--duration-leave` | 195ms | leaving state |
| `--duration-complex` | 375ms | larger UI movement |
| `--easing-standard` | `cubic-bezier(.4, 0, .2, 1)` | default motion |
| `--easing-decelerate` | `cubic-bezier(0, 0, .2, 1)` | button scale hover/settle |
| `--easing-accelerate` | `cubic-bezier(.4, 0, 1, 1)` | exit acceleration |
| `--easing-sharp` | `cubic-bezier(.4, 0, .6, 1)` | fast link color changes |

Button mechanics include `--action-variant-button-hover-scale: 1.05`, `--action-variant-button-active-scale: .95`, and `--action-variant-button-active-translate-y: 5%`. The motion is tactile, but only on controls.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: current container moves from 300px to 354px, 680px, 960px, 1200px, and 1400px.
- **Grid type**: flex-wrap grid utilities plus CSS Grid for image/category lists.
- **Column count**: 12-column generated layout classes appear in the captured HTML.
- **Gutter**: tokenized with `--grid-column-gap`, often `--space-none` in generated wrappers and explicit `20px` in tile grids.

### Hero

- **🆕 Pattern Summary**: `800px first viewport + full-bleed business photography + centered oversized white H1 + dual pill CTA`.
- Layout: one-column centered hero content over image/video background.
- Background: business photography, darkened by natural image contrast rather than a visible gradient system.
- **🆕 Background Treatment**: image-overlay/photo-as-surface. The hero image itself supplies grit, shadow, and color; UI chrome remains clean.
- H1: approximately 90px desktop display, weight 400, line-height 1, tracking around `-1.8px`.
- Max-width: centered hero headline spans wide, roughly 900-1000px visual width.

### Section Rhythm

```css
section {
  padding: var(--space-responsive-80) var(--space-20);
  max-width: var(--container-width-current);
}
```

### Card Patterns

- **Card background**: usually `#FFFFFF`; contrast sections may use `#F7F6F5` or `#000000`.
- **Card border**: `1px solid #D9D9D9` when structure is needed.
- **Card radius**: 16px or 24px containers; 50px for action pills.
- **Card padding**: 20px to 40px depending on density.
- **Card shadow**: none by default; use border/surface separation.

### Navigation Structure

- **Type**: horizontal desktop nav with mega/category behavior; mobile nav collapses category headings.
- **Position**: top overlay on hero, with CTA subnav hidden until scroll.
- **Height**: visually around 72px on desktop; exact height varies by nav state.
- **Background**: transparent/dark over hero, tokenized light/dark modes for component states.
- **Border**: transparent border token in top hero state; hairline in scrolled/subnav states.

### Content Width

- **Prose max-width**: text variants define `55ch` body and `40ch` larger text.
- **Container max-width**: 1400px extra large.
- **Sidebar width**: no fixed homepage sidebar observed; dropdown/nav structures are component controlled.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Extra small container | 374px | container becomes 354px |
| Mobile nav split | 480px | nav category headings switch display behavior |
| Tablet container | 740px | container becomes 680px |
| Desktop container | 1024px | container becomes 960px; larger typography tokens activate |
| Large container | 1280px | container becomes 1200px |
| Extra large container | 1680px | container becomes 1400px |

### Touch Targets

- **Minimum tap size**: primary button min-height is 50px in `LinkComponent--button`.
- **Button height (mobile)**: regular pill padding resolves around 10px/20px; link button min-height 50px.
- **Input height (mobile)**: forms inherit reset then field components define their own size; exact homepage input height not surfaced in hero.

### Collapsing Strategy

- **Navigation**: category headings collapse around 480px; mobile nav exposes button-style category headings.
- **Grid columns**: generated grid uses 12-column spans; tile lists use `repeat(auto-fit, minmax(124px, 1fr))`.
- **Sidebar**: no homepage sidebar; nav/dropdown modules replace sidebar layout.
- **Hero layout**: remains centered overlay; typography and container width adjust across breakpoints.

### Image Behavior

- **Strategy**: full-bleed hero image/video as atmosphere, with responsive crop.
- **Max-width**: component images generally respect container width or full viewport.
- **Aspect ratio handling**: hero prioritizes cover/crop effect over full asset visibility.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary Action Pill**

```html
<a class="Action Action--button Action--regular" href="/signup/en-US">
  <span class="Action__content-wrapper">Get started</span>
</a>
```

| Property | Value |
|---|---|
| background | `#006AFF` |
| color | `#FFFFFF` |
| radius | `5rem` |
| min-width | `120px` |
| padding | `1rem 2rem` regular, `.6rem 1.8rem` small |
| hover | scale to `1.05`, background/link hover darkens to `#0055CC` |
| active | scale `.95`, translate-y `5%`, opacity `.6` |
| focus | 2px `#006AFF` outline, 8px or pill radius, 2px offset |

### Badges

No strong homepage badge system is visible in the captured hero. If needed, keep badges monochrome: 12-14px Square Sans, medium weight, white/gray surface, and no decorative color family beyond `#006AFF` for action state.

### Cards & Containers

Containers use radius rather than elevation. The default Square card should be a `#FFFFFF` or `#F7F6F5` surface, `1px solid #D9D9D9` when separation is necessary, `16px` or `24px` radius, and 20-40px padding. Avoid nested card piles.

### Navigation

The nav is content-rich and operational. It uses 500-weight links, dark/light mode token inversion, transparent hero chrome, and a scrolled CTA subnav. Icons are minimal: square mark, search, cart, caret/chevron.

### Inputs & Forms

Inputs begin from a full reset: native appearance removed, inherited font/line-height/weight, transparent background, no border, no shadow. Field components then apply border/radius/focus states. This means Square forms should feel custom but not ornamental.

### Hero Section

The hero combines a full-bleed business image, top overlay nav, centered display headline, and two CTAs: white secondary `Get started` and blue primary `Contact sales` in the captured screenshot. Text is white, huge, and regular weight.

### 13-2. Named Variants

**button-primary-blue-pill** — Main action.

| Property | Value |
|---|---|
| token | `--action-variant-button-*` |
| bg | `#006AFF` |
| fg | `#FFFFFF` |
| radius | `5rem` |
| behavior | hover scale `1.05`, active scale `.95` |

**button-alt-white-pill** — Secondary action on photo/dark surfaces.

| Property | Value |
|---|---|
| bg | `#FFFFFF` |
| fg | `#006AFF` |
| border | `1px solid #006AFF` in light mode; `#FFFFFF` border in dark mode |
| radius | `5rem` |

**link-button-standard** — Older/standard button component.

| Property | Value |
|---|---|
| class | `LinkComponent--button` |
| min-height | `5rem` |
| padding | `1.3rem 1.6rem` |
| radius | `.6rem` |
| bg | `var(--color-link)` |

**nav-hero-link** — Transparent hero navigation link.

| Property | Value |
|---|---|
| color | `#FFFFFF` over hero, `#030303` in light mode |
| weight | 500 |
| hover | color transition only |

### 13-3. Signature Micro-Specs

#### photo-editorial-commerce-hero

```yaml
photo-editorial-commerce-hero:
  description: "Full-bleed local-business photography acts as the emotional surface, not as a framed asset."
  technique: "cover/cropped hero image or video; white 72-90px display type; line-height: 1; tracking around -1.8px; no text card or chrome shadow behind the headline"
  applied_to: ["{component.hero}", "{component.nav-link}"]
  visual_signature: "Square feels like a real storefront or sidewalk business before it reads as software."
```

#### single-action-blue-contract

```yaml
single-action-blue-contract:
  description: "One blue owns every interactive promise across the page."
  technique: "#006AFF for primary fill, links, alt-button text, and 2px focus outline; #0055CC for hover/active darkening; no secondary decorative brand color"
  applied_to: ["{component.button-primary}", "{component.button-secondary-white}", "{component.link-button-standard}"]
  visual_signature: "The eye always knows where the business action is, like a single paid stamp on a receipt."
```

#### fifty-rem-pill-scale-mechanics

```yaml
fifty-rem-pill-scale-mechanics:
  description: "Action controls feel tactile through scale and translate rather than elevation."
  technique: "border-radius: 5rem; min-width: 120px; padding: 1rem 2rem; hover transform scale(1.05); active scale(.95) translate-y(5%) with opacity .6"
  applied_to: ["{component.button-primary}", "{component.button-secondary-white}"]
  visual_signature: "Buttons press like physical checkout controls while the surrounding UI remains flat."
```

#### transparent-hero-nav-inversion

```yaml
transparent-hero-nav-inversion:
  description: "Navigation floats over photography in white, then returns to the black-on-white product system."
  technique: "nav links use #FFFFFF over dark/photo hero and #030303 in light mode; font-weight: 500; transparent hero border with hairline/scrolled state only"
  applied_to: ["{component.nav-link}", "{component.hero}"]
  visual_signature: "The nav behaves like signage painted on the storefront glass, then becomes ordinary interface chrome on scroll."
```

#### radius-not-shadow-commerce-cards

```yaml
radius-not-shadow-commerce-cards:
  description: "Containers separate by surface, border, and radius instead of multi-layer elevation."
  technique: "#FFFFFF or #F7F6F5 surface; 1px solid #D9D9D9 when needed; border-radius: 1.6rem or 2.4rem; box-shadow: none by default"
  applied_to: ["{component.container-card}"]
  visual_signature: "Square cards feel like clean countertop trays, not floating SaaS panels."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | local aspiration + scale jump | "Local legend or global icon. Make it big on your block." |
| Primary CTA | short action verb | "Get started" |
| Secondary CTA | sales path for larger business | "Contact sales" |
| Subheading | operational benefits in plain verbs | "Sell anywhere. Diversify revenue streams. Streamline operations." |
| Tone | practical, merchant-first, confident | business infrastructure without developer jargon |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Square — copy into your root stylesheet */
:root {
  /* Fonts */
  --square-font-family: "Square Sans Text VF", "Square Sans Text", Helvetica, Arial, sans-serif;
  --square-font-family-display: "Square Sans Display VF", "Square Sans Display", Helvetica, Arial, sans-serif;
  --square-font-family-code: "Square Sans Mono VF", "Square Sans Mono", ui-monospace, Menlo, monospace;
  --square-font-weight-normal: 400;
  --square-font-weight-medium: 500;
  --square-font-weight-bold: 700;

  /* Brand */
  --square-color-brand-25: #CEE7F3;
  --square-color-brand-300: #1379F3;
  --square-color-brand-500: #006AFF;
  --square-color-brand-600: #006AFF;
  --square-color-brand-900: #0055CC;

  /* Surfaces */
  --square-bg-page: #FFFFFF;
  --square-bg-contrast: #F7F6F5;
  --square-bg-dark: #000000;
  --square-text: #030303;
  --square-text-muted: #737373;
  --square-border: #D9D9D9;

  /* Key spacing */
  --square-space-sm: 10px;
  --square-space-md: 20px;
  --square-space-lg: 40px;
  --square-space-xl: 80px;

  /* Radius */
  --square-radius-sm: 6px;
  --square-radius-md: 16px;
  --square-radius-lg: 24px;
  --square-radius-pill: 50px;

  /* Motion */
  --square-duration-quick: 125ms;
  --square-easing-sharp: cubic-bezier(.4, 0, .6, 1);
  --square-easing-decelerate: cubic-bezier(0, 0, .2, 1);
}

.square-button {
  min-width: 120px;
  padding: 10px 20px;
  border: 1px solid #006AFF;
  border-radius: 50px;
  background: #006AFF;
  color: #FFFFFF;
  font: 500 16px/22px var(--square-font-family);
  transition: transform 125ms var(--square-easing-decelerate),
              background-color 125ms var(--square-easing-sharp);
}
.square-button:hover { background: #0055CC; transform: scale(1.05); }
.square-button:active { transform: translateY(5%) scale(.95); opacity: .6; }
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Square-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        square: {
          blue: '#006AFF',
          blueHover: '#0055CC',
          blueLight: '#CEE7F3',
          ink: '#030303',
          text: '#1A1A1A',
          muted: '#737373',
          border: '#D9D9D9',
          warm: '#F7F6F5',
        },
      },
      fontFamily: {
        sans: ['Square Sans Text VF', 'Square Sans Text', 'Helvetica', 'Arial', 'sans-serif'],
        display: ['Square Sans Display VF', 'Square Sans Display', 'Helvetica', 'Arial', 'sans-serif'],
        mono: ['Square Sans Mono VF', 'Square Sans Mono', 'ui-monospace'],
      },
      borderRadius: {
        square: '16px',
        'square-lg': '24px',
        'square-pill': '50px',
      },
      transitionTimingFunction: {
        'square-sharp': 'cubic-bezier(.4, 0, .6, 1)',
        'square-out': 'cubic-bezier(0, 0, .2, 1)',
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
| Brand primary | `{colors.primary}` | `#006AFF` |
| Brand hover | `{colors.primary-hover}` | `#0055CC` |
| Background | `{colors.surface-base}` | `#FFFFFF` |
| Contrast background | `{colors.surface-contrast}` | `#F7F6F5` |
| Text primary | `{colors.text-primary}` | `#030303` |
| Text muted | `{colors.text-secondary}` | `#737373` |
| Border | `{colors.border-default}` | `#D9D9D9` |
| Success | `{colors.success}` | `#00B23B` |

### Example Component Prompts

#### Hero Section

```text
Square 스타일 히어로 섹션을 만들어줘.
- 배경: full-bleed local business photography, dark/photo contrast, no text card
- H1: editorial display, 72-90px desktop, weight 400, line-height 1, tracking about -0.02em
- 텍스트: white
- CTA: two 50px pill buttons; secondary white with blue text, primary #006AFF with white text
- Nav: transparent hero overlay, 500-weight links, white icons
```

#### Card Component

```text
Square 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF or #F7F6F5
- border: 1px solid #D9D9D9 only when structure is needed
- radius: 16px or 24px
- padding: 20px to 40px
- shadow: none by default
- title: Square Sans Display/Text, 28-40px, weight 400 or 500, tight tracking
```

#### Badge

```text
Square 스타일 배지를 만들어줘.
- 12-14px Square Sans, weight 500
- monochrome surface only
- if interactive, use #006AFF text or focus outline
- no gradient, no secondary accent family
```

#### Navigation

```text
Square 스타일 상단 네비게이션을 만들어줘.
- desktop horizontal nav, transparent over hero
- links: 16px, weight 500, white on photo / #030303 on light surface
- right utility links: Sign in, Support, search/cart icons
- scrolled state may introduce CTA subnav and hairline
```

### Iteration Guide

- **색상 변경 시**: `#006AFF`를 action에만 쓴다. 장식용 blue wash를 만들지 않는다.
- **폰트 변경 시**: body 400, nav/action 500, display 400/500을 유지한다.
- **여백 조정 시**: 10px-root scale을 유지한다. 8px-only SaaS scale로 바꾸면 Square 느낌이 사라진다.
- **새 컴포넌트 추가 시**: shadow보다 radius, border, surface contrast를 우선한다.
- **다크/사진 히어로**: 흰색 텍스트와 white/blue pill CTA 조합을 우선한다.
- **반응형**: 374/740/1024/1280/1680 container ladder를 기준으로 잡는다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#006AFF` as the single primary action color.
- Keep backgrounds mostly `#FFFFFF`, `#F7F6F5`, `#000000`, or photographic.
- Use 50px pill CTAs for hero-level actions.
- Preserve the 10px-root spacing feel: 10, 20, 40, 80, 120.
- Let photography and oversized display type carry the campaign moments.
- Keep body text at 16px/24px and weight 400.
- Use focus outlines: 2px, `#006AFF`, 2px offset.

### ❌ DON'T

- 배경을 `#F8FAFC` 또는 generic cool SaaS gray로 두지 말 것 — 대신 `#FFFFFF` 또는 `#F7F6F5` 사용.
- 텍스트를 `#000000` pure black만으로 평면화하지 말 것 — 대신 heading은 `#030303`, body는 `#1A1A1A` 계열 사용.
- primary CTA를 `#2563EB` Tailwind blue로 바꾸지 말 것 — 대신 `#006AFF` 사용.
- CTA hover를 `#1D4ED8`로 만들지 말 것 — 대신 `#0055CC` 사용.
- border를 `#E5E7EB`로 일반화하지 말 것 — 대신 Square의 `#D9D9D9` 사용.
- hero를 흰 카드 안에 넣지 말 것 — full-bleed photo 위에 직접 white display type을 둔다.
- button radius를 `8px`로 낮추지 말 것 — hero/action pill은 `5rem` / 50px가 맞다.
- display heading에 `font-weight: 800` 사용 금지 — Square hero/display는 크기와 tracking으로 힘을 만든다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **Decorative blue gradients: zero** — `#006AFF`는 action color일 뿐 atmosphere로는 absent. brand wash는 never.
- **Multicolor fintech palette: none** — red/green/plum/rose는 utility accent로만 존재하고, 마켓 진열대 위 brand expression으로는 absent.
- **Heavy card elevation: zero** — default container는 surface, border, radius에 기댄다. shadow chrome은 never.
- **Tiny SaaS typography: absent** — 12px는 utility 한구석에 있고, body는 16px, hero는 매대 차양처럼 크게 점프. 작은 글자 일변도는 none.
- **800/900 display weights: never** — large type는 regular나 medium에 머문다. heavyweight 카탈로그 글자는 zero.
- **Rounded-rectangle card behind hero text: absent** — headline은 photography 위에 직접 앉는다. card frame은 none.
- **Generic 8px radius for primary actions: zero** — action button은 pill, 8px 사각 카운터 버튼은 absent.
- **Second brand color: none** — 영수증 도장은 단 하나. 두 번째 chromatic action은 zero.
- **App-dashboard first impression: absent** — homepage는 매대와 골목 마켓에서 시작, 표/메트릭 진열장은 never.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-only read** — this analysis uses the captured Square homepage, not checkout, dashboard, payroll, POS setup, or logged-in app surfaces.
- **Screenshot state is one hero variant** — Square may rotate campaign imagery/headlines; the current interpretation is anchored to the captured "Local legend or global icon" hero.
- **CSS is captured and large** — `_inline.css` is the dominant source; component CSS was sampled for action/nav/form patterns, but every generated Svelte class was not manually audited.
- **Exact font rendering depends on proprietary files** — Square Sans and Cash Sans are loaded from Square CDN; substitutes are approximations.
- **Motion JS not fully traced** — CSS duration/easing/scale tokens are captured, but scroll-triggered JavaScript behavior and personalization experiments were not deeply inspected.
- **Dark-mode mapping is partial** — light/dark token branches exist, but full dark-mode page coverage was not traversed.
- **Form validation states are inferred from component CSS** — specific live error/loading states were not exercised through a submitted form.
- **Logo wall contamination filtered manually** — frequency candidates include many whites/neutrals from logos and nav/footer; brand selection prioritizes semantic/action variables over raw frequency alone.
