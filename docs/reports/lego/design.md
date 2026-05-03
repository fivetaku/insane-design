---
schema_version: 3.2
slug: lego
service_name: LEGO.com
site_url: https://www.lego.com/en-us
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: light
brand_color: "#005AD2"
primary_font: "LEGO Typewell"
font_weight_normal: 400
token_prefix: ds

bold_direction: Playful Commerce
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: commerce-marketplace
archetype_confidence: high
design_system_level: lv3
design_system_level_evidence: "CSS exposes a deep --ds token system: breakpoints, core colors, semantic layers, action states, radius, spacing, shadows, badges, buttons, and localized font modes."

colors:
  action-primary: "#005AD2"
  action-primary-hovered: "#0045B7"
  action-accent: "#FFD502"
  logo-red: "#E3000B"
  text-default: "#141414"
  surface-page: "#fff"
  surface-muted: "#F7F7F7"
  border-default: "#B0B0B0"
typography:
  display: "LEGO Typewell"
  body: "LEGO Typewell"
  fallback: "Cera Pro"
  ladder:
    - { token: body, size: "16px", weight: 400, line_height: "1.5" }
    - { token: badge-small, size: "14px", weight: 500, line_height: "1.5" }
    - { token: badge-x-small, size: "12px", weight: 500, line_height: "1.62", tracking: "0.01em" }
    - { token: display, size: "32px-40px inferred", weight: 700 }
  weights_used: [400, 500, 700, 900]
  weights_absent: [600]
components:
  button-primary: { bg: "{colors.action-primary}", hover: "{colors.action-primary-hovered}", radius: "999px", border: "2px transparent solid" }
  button-secondary: { bg: "transparent", border: "{colors.action-primary}", radius: "999px" }
  button-accent: { bg: "{colors.action-accent}", text: "#000000", radius: "999px" }
  product-leaf: { bg: "{colors.surface-page}", frame: "#0000000F", radius: "8px" }
---

# DESIGN.md - LEGO.com

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

LEGO.com is not a quiet retail surface wearing a playful logo. It is a toy-store operating system: a white commerce chassis, a yellow/red brand memory, and a blue action layer that quietly does the conversion work. The page lets product photography and franchise art shout, while the UI itself stays surprisingly disciplined.

The system has two identities that never fully merge. The brand identity is classic LEGO: logo red `#E3000B`, brick yellow `#FFD502`, black outline, product imagery, kids' play-zone energy. The shopping identity is more utilitarian: primary actions use `#005AD2` (`{colors.action-primary}`), text sits at `#141414` (`{colors.text-default}`), and catalog frames rely on white surfaces plus pale gray dividers. It feels like a flagship toy aisle where the shelves are engineered by a serious retail team: the boxes can be riotous, but the shelf rail, price tag, and checkout button all obey one quiet grid.

The most important detail is that LEGO does not turn every control yellow. Yellow is an accent and brand atmosphere; blue is the action grammar. This separation keeps a massive toy catalog usable. A childlike palette is allowed in image tiles, badges, and promotional modules, while search, menus, buttons, filters, and product cards follow the `--ds-*` system. No second conversion color exists: `{colors.action-accent}` can make a promo feel like a LEGO brick, but `{colors.action-primary}` is the route marker to the register.

The page behaves like a white LEGO baseplate under a pile of licensed worlds. Star Wars, Botanicals, DUPLO, offers, membership points, and play content can snap on and off, because the baseplate is mostly `{colors.surface-page}`, `{colors.surface-muted}`, alpha black frames, and pill controls. Product cards are not glass cases; they are small build plates with a faint `#0000000F` outline so the set art supplies the color.

The site is built from chunky, accessible primitives. Pills are genuinely round (`999px`), focus rings are thick, badges use high-contrast color states, and responsive breakpoints are explicit rather than improvised. The craft is not minimalism; it is controlled noisiness: a marketplace that can host many toy universes without losing the checkout path. The UI chrome steps back like the instruction booklet border around a model photo: visible enough to guide, never decorative enough to compete.

### Key Characteristics

- Commerce-first white chassis with loud promotional imagery above and inside it.
- Primary conversion color is blue `#005AD2`, not LEGO yellow or logo red.
- Brand yellow `#FFD502` is reserved for accent, promo, logo memory, and playful emphasis.
- `--ds-*` token namespace is broad and mature: colors, layer, action, layout, spacing, shadow, breakpoints, and component states.
- Round controls dominate: button, search, carousel dots, and icon surfaces lean pill/circle.
- Type system uses LEGO Typewell in brand mode, with Cera Pro as legacy/fallback mode.
- Product cards are modular, frame-based, and image-led; chrome stays neutral so licensed art can vary wildly.
- Navigation is dense but friendly: top categories, mega-menu hierarchy, search, account, wishlist, and cart all live in a compact header.
- Shadows are multi-layer but restrained; product/card elevation is lower than the imagery itself.
- Accessibility states are visible: focus outlines, disabled opacity, large hit areas, and explicit aria patterns.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Playful Commerce
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **disciplined toy-store marketplace, where blue actions steer a red/yellow brand world**으로 기억된다.
> **Code Complexity**: high — deep token system, responsive marketplace components, multi-state buttons/forms, carousel/product modules, and image-heavy campaign slots.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 LEGO.com처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "LEGO Typewell", "Cera Pro", system-ui, sans-serif;
  font-weight: 400;
  line-height: 1.5;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #fff; --fg: #141414; }
body { background: var(--bg); color: var(--fg); }

/* 3. 액션 컬러 */
:root { --action-primary: #005AD2; --accent-yellow: #FFD502; --logo-red: #E3000B; }
.cta { background: var(--action-primary); color: #fff; border-radius: 999px; }
```

**절대 하지 말아야 할 것 하나**: 모든 CTA를 `#FFD502` yellow로 만들지 말 것. LEGO.com의 실제 primary action은 `#005AD2`; yellow는 brand/accent layer다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.lego.com/en-us` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | reused phase1 artifacts: local HTML + CSS + screenshot |
| HTML size | 1,100,878 bytes (Next.js / React commerce app) |
| CSS files | 13 CSS files, total 310,966 chars |
| Token prefix | `--ds-*` plus legacy `--st-*` |
| Method | CSS custom properties, local phase1 JSON, HTML snippets, screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js / React storefront with server-rendered page data and `__NEXT_DATA__`.
- **Design system**: LEGO shopper design system using prefix `--ds-*`; older shop/theme tokens remain under `--st-*`.
- **CSS architecture**:
  ```css
  --ds-color-core-*       raw ramps: gray, slate, red, orange, yellow, green, blue, purple, pink
  --ds-color-brand-*      LEGO brick/logo/extended brand colors
  --ds-color-action-*     interactive states: enabled, hovered, pressed, selected
  --ds-color-layer-*      surface and semantic layer tokens
  --ds-layout-*           size, radius, spacing, stroke width, blur
  --ds-border-*           aliases for radius and stroke
  --ds-shadow-*           multi-layer elevation tokens
  ```
- **Class naming**: CSS Modules plus shopper components: `MainBar_*`, `StaticHero_*`, `ProductLeaf_*`, `AdvancedQuickLink_*`, and shared `sk-button`, `sk-badge`.
- **Default theme**: light (`--ds-color-page-background: #fff`, `--ds-color-layer-default: #fff`).
- **Font loading**: custom brand font declarations (`LEGO Typewell`, `Cera Pro`) with localized Noto Sans modes for KR/JP/SC.
- **Canonical anchor**: homepage commerce shell: global banner, dense navigation, static hero, quick links, product carousel/listing modules.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `LEGO Typewell` (brand font, licensed/proprietary)
- **Body font**: `LEGO Typewell` in brand mode; `Cera Pro` in legacy mode
- **Localized fallback**: `Noto Sans KR`, `Noto Sans JP`, `Noto Sans SC`
- **System fallback**: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial`
- **Weight normal / bold**: `400` / `700`

```css
:root,
[data-mode="brand"] {
  --ds-font-font-family: "LEGO Typewell";
}

[data-mode="legacy"] {
  --ds-font-font-family: "Cera Pro";
}

body {
  font-family: var(--ds-font-font-family), system-ui, sans-serif;
  font-weight: 400;
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **LEGO Typewell** is the true voice. If unavailable, use **Nunito Sans** or **Atkinson Hyperlegible** at weight `400/700` for friendliness, but keep the UI spacing and pill geometry intact. The font substitute should not become the design.
- **Cera Pro fallback** can be approximated with **Inter** only for operational UI, not for hero/brand moments. Use Inter at `400/500/700`, avoid overly tight tracking, and preserve line-height around `1.5`.
- **Localized surfaces** should follow the existing Noto path. Korean/Japanese/Chinese text should not be forced into the Latin brand font; the CSS already exposes `Noto Sans KR/JP/SC`.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Body default | `16px` inferred / browser base | `400` | `1.5` | `0` |
| Navigation item | `14px-16px` inferred | `400/500` | compact | `0` |
| Badge small | `.875rem` | `500` | `1.5` | `0` |
| Badge x-small | `.75rem` | `500` | `1.62` | `.01em` |
| Discount badge x-small | `.75rem` | `700` | `1.62` | `.01em` |
| Hero/display | campaign-dependent | `700` common | image-composition dependent | `0` or tight by asset |
| Heavy promotional emphasis | campaign-dependent | `900` available | N/A | N/A |

> Insight: the local extractor did not recover a full type ladder from computed DOM, but CSS confirms a pragmatic retail ladder: 400 body, 500 navigation/badges, 700 CTA/promo emphasis, 900 rare heavy emphasis.

### Principles

1. Body remains readable and operational at `400`; playfulness comes from imagery, color, and round components, not from eccentric paragraph typography.
2. Weight `500` is a utility weight for badges/nav/micro-labels, while `700` is the durable emphasis weight.
3. `600` is intentionally not central in the captured CSS. Do not invent a semibold middle layer just because many SaaS sites use one.
4. Badge typography is more engineered than decorative: `.75rem`, `1.62` line-height, and `.01em` tracking keep tiny commerce labels legible.
5. Display scale is campaign-led. Static hero text should align to the image composition rather than forcing a universal H1 scale onto every LEGO franchise.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (selected)

| Token | Hex |
|---|---|
| `--ds-color-brand-logo-corporate-red` | `#E3000B` |
| `--ds-color-brand-logo-yellow` | `#FFED00` |
| `--ds-color-brand-bright-yellow` | `#FFD400` |
| `--ds-color-brand-bright-red` | `#DD1A22` |
| `--ds-color-brand-bright-blue` | `#006CB7` |
| `--ds-color-brand-earth-blue` | `#00395D` |
| `--ds-color-brand-bright-orange` | `#F47D20` |
| `--ds-color-brand-bright-green` | `#00AF4D` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--ds-color-core-blue-1300` | `#011C58` |
| `--ds-color-core-red-1300` | `#450302` |
| `--ds-color-core-yellow-1300` | `#3E1700` |
| `--ds-color-core-slate-1300` | `#22242D` |
| `--ds-color-layer-inverse` | `#141414` |

### 06-3. Neutral Ramp

| Step | Gray | Slate |
|---|---|---|
| 10 | `#FAFAFA` | `#F9F9FB` |
| 25 | `#F7F7F7` | `#F6F6F8` |
| 50 | `#F2F2F2` | `#F1F1F4` |
| 100 | `#E5E5E5` | `#E4E5EC` |
| 300 | `#CBCBCB` | `#CACBD5` |
| 700 | `#939393` | `#9192A1` |
| 1000 | `#636363` | `#606274` |
| 1300 | `#242424` | `#22242D` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Blue primary action | `--ds-color-action-primary-enabled` | `#005AD2` |
| Yellow accent action | `--ds-color-action-accent-enabled` | `#FFD502` |
| Orange emphasis action | `--ds-color-action-emphasis-enabled` | `#E96F14` |
| Red negative/action | `--ds-color-action-negative-enabled` | `#BD0000` |
| Green positive | `--ds-color-layer-positive-default` | `#008439` |
| Pink wishlist | `--ds-color-wishlist-default` | `#D72054` inferred from highlight family |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--ds-color-text-default` | `#141414` | Body/UI text |
| `--ds-color-text-strong` | `#3D3D3D` | Strong secondary text |
| `--ds-color-text-subdued` | `#636363` | Muted labels |
| `--ds-color-text-primary` | `#005AD2` | Links/action text |
| `--ds-color-text-accent` | `#FAC400` | Yellow accent text |
| `--ds-color-text-negative` | `#BD0000` | Error/negative |
| `--ds-color-border-default` | `#B0B0B0` | Standard border |
| `--ds-color-layer-default` | `#fff` | Default card/page layer |
| `--ds-color-layer-muted` | `#F7F7F7` | Muted sections |
| `--ds-color-layer-subdued` | `#F2F2F2` | Subdued panels |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--ds-color-action-primary-enabled` | `#005AD2` | Primary CTA/button |
| `--ds-color-action-primary-hovered` | `#0045B7` | Primary hover |
| `--ds-color-action-primary-pressed` | `#011C58` | Primary pressed |
| `--ds-color-action-accent-enabled` | `#FFD502` | Yellow accent CTA |
| `--ds-color-action-secondary-enabled` | `#F2F2F2` | Neutral secondary |
| `--ds-color-layer-primary-enabled` | `#E5F2FF` | Subtle blue layer |
| `--ds-color-focused-default` | `#0DADE4` | Focus ring in newer semantic layer |
| `--ds-color-wishlist-default` | highlight pink family | Wishlist/save affordance |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency signal |
|---|---|---|
| transparent black layers | `#0000000F` / `#0000001A` / `#00000026` | high |
| white and off-white surfaces | `#fff` / `#FCFCFC` / `#FAFAFA` | high |
| text / inverse layer | `#141414` | high |
| primary blue | `#005AD2` | high chromatic action |
| yellow accent | `#FFD502` / `#FAC400` | repeated brand/accent |
| negative red | `#BD0000` / `#E3000B` | repeated brand/error/logo |

### 06-8. Color Stories

**`{colors.action-primary}` (`#005AD2`)** — The conversion blue. It powers primary buttons, text links, active controls, and informative states. Use it when the user must act; do not replace it with logo red.

**`{colors.action-accent}` (`#FFD502`)** — The brick-yellow memory. It belongs in accent CTAs, promos, brand panels, play-zone energy, and selected campaign surfaces. It should feel like LEGO, but it should not carry every control.

**`{colors.text-default}` (`#141414`)** — The commerce ink. It is softer than pure black in practical UI and keeps product pages from feeling like a toy poster. Use it for normal text, nav, and product titles.

**`{colors.border-default}` (`#B0B0B0`)** — The utility hairline. LEGO.com uses border and frame tokens to organize dense shopping content while leaving color free for products, themes, and campaign images.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--ds-layout-spacing-25` | `2px` | micro offsets |
| `--ds-layout-spacing-50` | `4px` | tight icon/text gaps |
| `--ds-layout-spacing-100` | `8px` | small gaps |
| `--ds-layout-spacing-150` | `12px` | badge/button inner rhythm |
| `--ds-layout-spacing-200` | `16px` | card/content baseline |
| `--ds-layout-spacing-300` | `24px` | module padding |
| `--ds-layout-spacing-400` | `32px` | section/card gaps |
| `--ds-layout-spacing-600` | `48px` | large blocks |
| `--ds-layout-spacing-800` | `64px` | hero/section air |
| `--ds-layout-spacing-1600` | `128px` | large campaign rhythm |
| `--ds-layout-spacing-2800` | `224px` | oversized responsive/hero spacing |

**주요 alias**:
- `--ds-spacing-xs` -> `--ds-layout-spacing-200` / `16px`
- `--ds-spacing-sm` -> `--ds-layout-spacing-250` / `20px`
- `--ds-spacing-md` -> `--ds-layout-spacing-300` / `24px`
- `--ds-spacing-lg` -> `--ds-layout-spacing-400` / `32px`

### Whitespace Philosophy

LEGO.com uses space like aisle management. Navigation and product grids are dense because shoppers need scanning speed, but hero/campaign modules get larger image-first blocks where franchise art can breathe. The contrast is intentional: compact retail controls around expansive toy imagery.

The spacing ladder is not a minimalist 4/8/16-only system. It reaches from `1px` strokes to `224px` hero-scale intervals, which matches a marketplace that must handle tiny badges, carousel controls, product leaves, full-bleed campaigns, and modal overlays without leaving the token system.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--ds-layout-radius-25` | `2px` | tiny structural corners |
| `--ds-layout-radius-50` | `4px` | small controls |
| `--ds-layout-radius-75` | `6px` | compact module corners |
| `--ds-layout-radius-100` | `8px` | default card/container radius |
| `--ds-layout-radius-150` | `12px` | larger panels |
| `--ds-layout-radius-200` | `16px` | soft cards |
| `--ds-layout-radius-400` | `32px` | big promotional surfaces |
| `--ds-layout-radius-600` | `48px` | large rounded modules |
| `--ds-layout-radius-pill` | `999px` | pills |
| `--ds-layout-radius-round` | `999px` | buttons, circular controls |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| `--ds-shadow-100` | `0px 1px 1px #0000000F`, `0px 2px 2px -1px #00000017`, `0px 4px 2px -2px #00000026` | small elevation |
| `--ds-shadow-300` | multi-layer up to `16px 16px -8px #00000026` | cards/modals |
| `--ds-shadow-500` | up to `64px 64px -32px #0000004D` | strong overlays |
| `--ds-shadow-down-300` | seven-layer slate shadow using `#22242D` alpha | dropdown/deep panels |
| `--ds-shadow-inset-100` | inset black alpha stack | input/pressed surfaces |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / pattern | Value | Usage |
|---|---|---|
| reduced motion query | `@media (prefers-reduced-motion)` | accessibility guard |
| pointer/hover query | `@media (hover:hover) and (pointer:fine)` | desktop hover affordances |
| button state switch | hover/active CSS variable replacement | avoids one-off colors |
| carousel/navigation controls | stateful dots/bars | promo and product scrollers |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: campaign-dependent; product and carousel sections use constrained list wrappers rather than a single universal max-width.
- **Grid type**: Flexbox/CSS modules for header and carousel, responsive list/grid patterns for product leaves.
- **Column count**: responsive marketplace rows; desktop product carousels show multiple product leaves, mobile collapses toward horizontal scroll.
- **Gutter**: tokenized gaps such as `--column-gap-sm`, `--row-gap-sm`, and `--ds-spacing-sm`.

### Hero
- **Pattern Summary**: campaign static hero + image background + right/left content alignment + CTA over artwork.
- Layout: `StaticHero` wrapper with `StaticHero_right` variant observed; media wrapper plus linked background image.
- Background: inline `background-color: var(--ds-color-core-off-black)` for captured hero, with remote campaign image.
- **Background Treatment**: image-led campaign treatment; not a generated gradient mesh. The CSS layer provides fallback solid color.
- H1: campaign-specific, usually bold display, image composition controls placement.
- Max-width: hero media uses full campaign asset dimensions; HTML captured `1600x700` image source for desktop.

### Section Rhythm

```css
section {
  padding: var(--ds-spacing-lg) var(--ds-spacing-sm);
  max-width: campaign-or-carousel-specific;
}
```

### Card Patterns
- **Card background**: `var(--ds-color-layer-default)` / `#fff`
- **Card border/frame**: `var(--ds-color-transparent-black-50)` and neutral border tokens
- **Card radius**: `--ds-border-radius-md` / `8px` commonly
- **Card padding**: `16px-24px` token range
- **Card shadow**: mostly low or none; stronger shadows are reserved for overlays/dropdowns

### Navigation Structure
- **Type**: horizontal main navigation with mega-menu submenus; mobile header/search variants exist.
- **Position**: header shell at top, with global banner above.
- **Height**: main bar min-height `--ds-size-xl` / `48px`.
- **Background**: `var(--ds-color-neutral-white)` / `#fff`.
- **Border**: subtle neutral borders and focus/active indicators.

### Content Width
- **Prose max-width**: not a prose site; copy is embedded in modules.
- **Container max-width**: module-specific, not single blog-width.
- **Sidebar width**: mega-menu/flyout dependent; no permanent dashboard sidebar.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| XS | `23.4375em` | minimum phone baseline |
| SM | `36.25em` | larger phones / small tablets |
| MD | `56.25em` | tablet / desktop nav transition |
| LG | `75em` | wide desktop |
| XL | `100em` | large display / campaign asset scaling |

### Touch Targets
- **Minimum tap size**: buttons/search/header icons align around `40px-48px` token sizes.
- **Button height (mobile)**: driven by `--_button-height`; header/search uses `--ds-spacing-2xl` / `48px`.
- **Input height (mobile)**: mobile search bar uses `height: var(--ds-spacing-2xl)`.

### Collapsing Strategy
- **Navigation**: desktop menu categories collapse to mobile header/search and drawer-like menu states.
- **Grid columns**: product carousels and quick links reduce columns or become horizontal scroll.
- **Sidebar**: no persistent sidebar; mega menu is transient.
- **Hero layout**: hero media swaps responsive image sources and adjusts alignment around `56.25em` / `900px`.

### Image Behavior
- **Strategy**: responsive `<picture>` sources with width/DPR variants.
- **Max-width**: product/media wrappers constrain image layout; asset URLs include crop/quality/width params.
- **Aspect ratio handling**: campaign images encode fixed dimensions; product leaves maintain image frame consistency.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<button class="sk-button">Learn more</button>
<button class="sk-button sk-button--secondary">Shop all</button>
```

| Property | Primary |
|---|---|
| Background | `var(--ds-color-action-primary-enabled)` / `#005AD2` |
| Hover | `var(--ds-color-action-primary-hovered)` / `#0045B7` |
| Pressed | `var(--ds-color-action-primary-pressed)` / `#011C58` |
| Text | `var(--ds-color-text-on-primary)` / `#fff` |
| Radius | `var(--ds-border-radius-round)` / `999px` |
| Border | `var(--ds-layout-stroke-width-25)` transparent solid |
| Focus | outline `var(--ds-color-focused-default)` with `2px` stroke |
| Disabled | `opacity: var(--ds-misc-opacity-50)` |

### Badges

Badges carry commerce labels, points multipliers, discount states, and category markers. Small badges use `.875rem`, `500`, `1.5`; x-small badges use `.75rem`, `.01em` tracking, and `1.62` line-height. Discount x-small flips to `700`.

| Variant | Background | Text | Note |
|---|---|---|---|
| default small | tokenized layer | default text | compact product metadata |
| discount | negative/red family | inverse or high-contrast | sale state |
| points 5x | `--ds-color-brand-bright-red` | inverse | loyalty promotion |
| accent | yellow/action accent | black | promotional emphasis |

### Cards & Containers

Product leaves use a white layer, neutral text, and an alpha frame (`#0000000F`). The card should not look like a SaaS analytics card. It is a product plinth: image first, title/price/status second, CTA last.

| Property | Product leaf |
|---|---|
| Surface | `--ds-color-layer-default` / `#fff` |
| Text | `--ds-color-text-default` / `#141414` |
| Frame | `--ds-color-transparent-black-50` / `#0000000F` |
| Radius | `8px` default container radius |
| Shadow | usually none or shallow |
| Hover | image/card control changes, not dramatic transform |

### Navigation

Main navigation combines logo, top categories (`Shop`, `Discover`, `Help`, `New`), mega-menu panels, account actions, wishlist, and cart. Menu buttons use `aria-haspopup`, `aria-expanded`, and data analytics labels. Logo is an image asset sized `55x55`.

### Inputs & Forms

Mobile search is a pill container: white background, neutral gray border, `48px` height, horizontal padding, and icon/text alignment. Form states use border and inset shadow tokens rather than large color fills.

### Hero Section

Static hero uses linked responsive images, a fallback background color, and directional variants such as `StaticHero_right`. Campaign assets drive the emotional palette; the UI token layer supplies readable CTA and text treatment.

### 13-2. Named Variants

#### `button-primary`
- `background: #005AD2`
- `hover: #0045B7`
- `pressed: #011C58`
- `color: #fff`
- `border-radius: 999px`

#### `button-secondary`
- `background: transparent`
- `border-color: #005AD2`
- `text: #141414`
- Use for lower-priority actions near primary CTA.

#### `button-accent-yellow`
- `background: #FFD502`
- `hover: #FAC400`
- `pressed: #EF9F00`
- `text: #000000`
- Use sparingly for LEGO-branded promotional moments.

#### `product-leaf`
- `background: #fff`
- `text: #141414`
- `frame: #0000000F`
- Image-led; avoid heavy shadows and decorative borders.

#### `mobile-search-pill`
- `height: 48px`
- `border: 1px solid #BFBFBF`
- `border-radius: 999px`
- `padding: 4px 20px`

### 13-3. Signature Micro-Specs

```yaml
blue-action-yellow-brand-split:
  description: "LEGO brand memory and conversion UI are held as separate layers."
  technique: "#005AD2 {colors.action-primary} for primary action; #0045B7 hover; #011C58 pressed; #FFD502 {colors.action-accent} reserved for accent/promotional action."
  applied_to: ["{component.button-primary}", "{component.button-accent}", "links", "promotional modules"]
  visual_signature: "a red/yellow toy-brand world where the actual route to purchase is always blue."

round-control-chassis:
  description: "Core controls are built as touchable pill/circle primitives instead of squared retail buttons."
  technique: "--ds-layout-radius-pill: 999px; --ds-layout-radius-round: 999px; mobile search height 48px; button border 2px transparent solid."
  applied_to: ["{component.button-primary}", "{component.button-secondary}", "mobile-search-pill", "carousel/icon controls"]
  visual_signature: "soft, graspable controls that echo LEGO tactility without becoming literal brick skeuomorphism."

alpha-frame-product-plinth:
  description: "Product leaves use a quiet alpha frame so franchise artwork carries the color load."
  technique: "background #fff {colors.surface-page}; frame #0000000F; default radius 8px; shadow usually none or shallow."
  applied_to: ["{component.product-leaf}", "carousel list items", "product grid cards"]
  visual_signature: "each product sits on a small white build plate, with the set image doing the shouting."

badge-legibility-microtype:
  description: "Dense marketplace labels stay readable through explicit tiny-type engineering."
  technique: ".875rem small badges at font-weight 500 and line-height 1.5; .75rem x-small badges at font-weight 500/700, letter-spacing .01em, line-height 1.62."
  applied_to: ["discount badges", "loyalty badges", "status badges", "product metadata"]
  visual_signature: "promo and status chips remain legible even when product grids become visually busy."

ds-tokenized-layer-cabinet:
  description: "Loud campaign and franchise surfaces sit inside a neutral tokenized commerce cabinet."
  technique: "--ds-color-layer-default #fff; --ds-color-layer-muted #F7F7F7; --ds-color-border-default #B0B0B0; --ds-shadow-100 low alpha stack for small elevation."
  applied_to: ["navigation", "mega-menu panels", "cards", "section containers"]
  visual_signature: "the shelves, rails, and dividers stay neutral while LEGO worlds change inside them."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Direct retail/play language; campaign-specific | `Star Wars Day offers` |
| Primary CTA | Short action phrase | `Learn more`, `Shop now` |
| Secondary CTA | Utility explanation | `Explore all current special offers and promotions now.` |
| Navigation | Category taxonomy, not brand poetry | `Sets by theme`, `Age`, `Price ranges` |
| Tone | Friendly, retail-clear, family-safe | Product/theme labels over abstract copy |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* LEGO.com-inspired design tokens */
:root {
  /* Fonts */
  --lego-font-family: "LEGO Typewell", "Cera Pro", system-ui, sans-serif;
  --lego-font-family-fallback: "Cera Pro", system-ui, sans-serif;
  --lego-font-weight-normal: 400;
  --lego-font-weight-medium: 500;
  --lego-font-weight-bold: 700;

  /* Brand and action */
  --lego-action-primary: #005AD2;
  --lego-action-primary-hovered: #0045B7;
  --lego-action-primary-pressed: #011C58;
  --lego-action-accent: #FFD502;
  --lego-logo-red: #E3000B;
  --lego-logo-yellow: #FFED00;

  /* Surfaces */
  --lego-bg-page: #fff;
  --lego-bg-muted: #F7F7F7;
  --lego-bg-subdued: #F2F2F2;
  --lego-text: #141414;
  --lego-text-muted: #636363;
  --lego-border: #B0B0B0;

  /* Key spacing */
  --lego-space-xs: 16px;
  --lego-space-sm: 20px;
  --lego-space-md: 24px;
  --lego-space-lg: 32px;
  --lego-space-xl: 40px;

  /* Radius */
  --lego-radius-sm: 4px;
  --lego-radius-md: 8px;
  --lego-radius-lg: 16px;
  --lego-radius-pill: 999px;
}

body {
  background: var(--lego-bg-page);
  color: var(--lego-text);
  font-family: var(--lego-font-family);
  font-weight: var(--lego-font-weight-normal);
}

.lego-button {
  align-items: center;
  background: var(--lego-action-primary);
  border: 2px solid transparent;
  border-radius: var(--lego-radius-pill);
  color: #fff;
  display: inline-flex;
  font-weight: 700;
  justify-content: center;
  min-height: 48px;
  padding: 0 24px;
}

.lego-button:hover { background: var(--lego-action-primary-hovered); }
.lego-button:active { background: var(--lego-action-primary-pressed); }

.lego-product-card {
  background: #fff;
  border: 1px solid #0000000F;
  border-radius: var(--lego-radius-md);
  color: var(--lego-text);
  padding: var(--lego-space-xs);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        lego: {
          blue: '#005AD2',
          blueHover: '#0045B7',
          yellow: '#FFD502',
          red: '#E3000B',
          ink: '#141414',
          muted: '#636363',
          surfaceMuted: '#F7F7F7',
          border: '#B0B0B0',
        },
      },
      fontFamily: {
        sans: ['LEGO Typewell', 'Cera Pro', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        lego: '8px',
        'lego-pill': '999px',
      },
      boxShadow: {
        lego: '0px 1px 1px 0px #0000000F, 0px 2px 2px -1px #00000017, 0px 4px 2px -2px #00000026',
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
| Brand primary action | `{colors.action-primary}` | `#005AD2` |
| Brand accent | `{colors.action-accent}` | `#FFD502` |
| Logo red | `{colors.logo-red}` | `#E3000B` |
| Background | `{colors.surface-page}` | `#fff` |
| Text primary | `{colors.text-default}` | `#141414` |
| Text muted | `--ds-color-text-subdued` | `#636363` |
| Border | `{colors.border-default}` | `#B0B0B0` |
| Error | `--ds-color-action-negative-enabled` | `#BD0000` |

### Example Component Prompts

#### Hero Section
```text
LEGO.com style hero section을 만들어줘.
- 구조: image-led campaign hero, linked responsive media, CTA overlay
- 배경: campaign image + fallback #141414 or #fff
- H1: LEGO Typewell, bold 700, campaign asset에 맞춰 좌/우 정렬
- CTA: #005AD2 primary pill, white text, 999px radius, 48px min-height
- yellow #FFD502는 accent/promo로만 사용
- product/franchise artwork가 주인공이고 UI chrome은 절제
```

#### Card Component
```text
LEGO.com product leaf card를 만들어줘.
- background: #fff
- border/frame: 1px solid #0000000F
- text: #141414
- radius: 8px
- image-first layout, title/price/status below
- badges: .75rem or .875rem, weight 500/700, letter-spacing .01em for tiny labels
- hover는 shadow/transform 과장 금지, product image/control state만 살짝
```

#### Badge
```text
LEGO.com badge를 만들어줘.
- small: .875rem, weight 500, line-height 1.5
- x-small: .75rem, weight 500, line-height 1.62, tracking .01em
- discount/urgent: red family #BD0000 or #E3000B
- loyalty/promo: yellow #FFD502 or brand red only when campaign context exists
```

#### Navigation
```text
LEGO.com style navigation을 만들어줘.
- white header, 48px+ height, LEGO logo left
- categories: Shop, Discover, Help, New
- mega menu with aria-expanded/aria-haspopup states
- mobile search pill: #fff bg, #B0B0B0 border, 999px radius, 48px height
- primary action/link color: #005AD2
```

### Iteration Guide

- **Primary CTA**: use `#005AD2`; yellow is not the universal button color.
- **Brand moments**: use yellow/red through hero art, promo tiles, and logo memory, not through every UI surface.
- **Product cards**: keep chrome neutral; let product imagery supply color.
- **Radius**: pills and circles are correct for controls; default cards can stay `8px`.
- **Typography**: use `400/500/700`; avoid inventing a `600` layer unless a specific component demands it.
- **Responsive**: respect `36.25em`, `56.25em`, `75em`, `100em` breakpoint logic.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#005AD2` for primary interactive actions and link/action emphasis.
- Use `#FFD502` as brand/accent energy, especially in promo or LEGO-memory surfaces.
- Keep the page and product card chassis white or near-white so product photography carries color.
- Use `LEGO Typewell` where available, with `Cera Pro` or localized Noto fallbacks.
- Build buttons as true pills with `border-radius: 999px` and visible focus outlines.
- Keep product cards image-led with subtle alpha frames.
- Preserve the `--ds-*` semantic layer; do not flatten everything into generic `--color-brand`.
- Let campaign modules vary by franchise while keeping commerce controls consistent.

### ❌ DON'T

- 배경을 `#000000` 또는 `black`으로 두지 말 것 — 기본 commerce surface는 `#fff` 또는 `#F7F7F7` 사용.
- 본문 텍스트를 `#000000` 또는 `black`으로 고정하지 말 것 — 대신 `#141414` 사용.
- Primary CTA를 `#FFD502`로 통일하지 말 것 — 대신 `#005AD2` 사용.
- LEGO logo red `#E3000B`를 모든 링크/버튼에 쓰지 말 것 — primary action은 `#005AD2`다.
- Product card frame을 `#B0B0B0` heavy border로 만들지 말 것 — 대신 `#0000000F` alpha frame 또는 subtle neutral 사용.
- Button radius를 `8px`로 낮추지 말 것 — primary controls는 `999px` pill/round다.
- Badge tiny text를 `font-weight: 400`으로 두지 말 것 — captured badges use `500` or `700`.
- Purple/blue AI gradient `#667EEA` 같은 임의 배경을 넣지 말 것 — LEGO.com은 campaign imagery + token colors를 쓴다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- No single-color brand wash: the whole UI is not red, yellow, or blue.
- No universal yellow CTA: yellow appears as accent/brand memory, not as the default conversion rule.
- No generic SaaS card shadow language: product cards are framed and image-led, not glassy analytics panels.
- No invented token names: use `--ds-color-action-primary-enabled`, `--ds-color-layer-default`, `--ds-layout-radius-round`, not `--lego-blue-button` unless making a local adapter.
- No delicate square buttons for primary actions: round/pill controls are part of the tactile identity.
- No typography eccentricity in body copy: play lives in imagery and brand assets, not in unreadable paragraph fonts.
- No permanent dashboard sidebar: this is a marketplace shell with header/mega-menu/carousel patterns.
- No monochrome luxury restraint: LEGO.com accepts bright campaign color, but controls it through neutral commerce structure.
- No decorative gradient mesh as a substitute for real product/franchise imagery.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Screenshot obstruction**: the available `hero-cropped.png` is covered by a regional/cookie selection modal in Korean. Hero judgments therefore rely more heavily on captured HTML/CSS than on a clean visual screenshot.
- **Homepage only**: analysis uses the captured `https://www.lego.com/en-us` homepage. Checkout, product detail, account, wishlist, cart, configurator, and support flows were not visited.
- **Computed typography gap**: phase1 `typography.json` did not extract a full scale. Typography values are based on CSS declarations and component snippets, not browser-computed measurements.
- **Alias resolver gap**: phase1 `resolved_tokens.json` reports zero resolved variables, but direct CSS inspection shows extensive `--ds-*` variables. This guide treats direct CSS variables as source of truth.
- **Campaign volatility**: homepage hero campaigns and quick links change frequently. The token system is stable enough for design guidance; specific Star Wars/offers/Mother's Day modules may be stale.
- **Logo and partner color contamination**: CSS includes LEGO logo colors, partner/franchise colors, social colors, and campaign colors. Brand/action decisions intentionally prioritize UI action tokens over raw chromatic frequency.
- **Motion not fully instrumented**: CSS media queries and state transitions were observed, but JS carousel timing, scroll behavior, and animation curves were not fully replayed.
- **Dark mode incomplete**: CSS includes inverse/static dark layers, but the captured homepage is light commerce. Full dark mapping is not proven.
