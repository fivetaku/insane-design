---
schema_version: 3.2
slug: patagonia
service_name: Patagonia
site_url: https://www.patagonia.com/home/
fetched_at: 2026-04-23T11:49:00+09:00
default_theme: mixed
brand_color: "#000000"
primary_font: "Ridgeway Sans"
font_weight_normal: 300
token_prefix: "pata"

bold_direction: "Outdoor Editorial"
aesthetic_category: "other"
signature_element: "hero_impact"
code_complexity: "high"

medium: web
medium_confidence: high

archetype: commerce-marketplace
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "Large Bootstrap-derived component layer plus pata font tokens and repeated hero/product/nav patterns; no extracted color token tier."

colors:
  bs-btn-primary-bg: "#000000"
  bs-btn-primary-color: "#FFFFFF"
  bs-focus-ring: "#91ABE9"
  pata-sale-red: "#E10000"
  pata-badge-orange: "#FA4616"
  pata-neutral-soft: "#F5F5F5"
  pata-text-muted: "#4A4A4A"
  pata-border-soft: "#CCC"

typography:
  display: "Ridgeway Sans"
  serif: "Copernicus"
  body: "Ridgeway Sans"
  ladder:
    - { token: body-sm, size: "1.2rem", weight: 300, line_height: "1.5", tracking: "0" }
    - { token: body, size: "1.4rem", weight: 300, line_height: "1.5", tracking: "0" }
    - { token: body-lg, size: "1.6rem", weight: 300, line_height: "1.5", tracking: "0" }
    - { token: heading, size: "2rem", weight: 500, line_height: "1.2", tracking: "0" }
    - { token: display, size: "calc(1.625rem + 2.8125vw)", weight: 300, line_height: "1.2", tracking: "0" }
    - { token: serif-special, size: "contextual", weight: 500, line_height: "1.1", tracking: "-.03em" }
  weights_used: [300, 500, 700, 850]
  weights_absent: [200, 800]

components:
  button-primary: { bg: "#000000", color: "#FFFFFF", radius: "3rem", padding: ".9rem 2.8rem" }
  button-light: { bg: "#FFFFFF", color: "#000000", radius: "3rem", padding: ".9rem 2.8rem" }
  checkout-button: { bg: "#E10000", color: "#FFFFFF", radius: "3rem", focus: "#91ABE9" }
  product-tag: { bg: "#F5F5F5", color: "#000000", radius: "2px", padding: ".8rem" }
  marketing-tile: { bg: "image", radius: ".8rem", overlay: "photo-led" }
---

# DESIGN.md - Patagonia

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Patagonia reads like an outdoor store where the canvas is documentary photography and the editorial voice is an activist field report. The homepage system is built around image-first surfaces, black-and-white utility chrome, and a deliberately plain retail chassis. The brand color is effectively black: `#000000` (`{colors.bs-btn-primary-bg}`) for primary buttons, nav weight, badge inversions, overlay text, and the loading mountain stroke. When chromatic colors appear, they are operational rather than decorative: sale red `#E10000` (`{colors.pata-sale-red}`), pickup orange `#FA4616` (`{colors.pata-badge-orange}`), focus blue `#91ABE9` (`{colors.bs-focus-ring}`).

The visual identity is a field-station store that learned commerce. The page does not pretend to be a glossy boutique; it behaves like a gear wall beside a field station, where the landscape is outside the window and the labels are black tape, white paper, and clipped inventory tags. Product surfaces are not polished into luxury. They are organized into durable, simple modules, as if the catalog has been packed into weatherproof bins: photo first, tag second, action last.

Photography is the weather system here. UI chrome does not create atmosphere; it straps itself over the image like a map case on top of a pack. A full-bleed hero can carry snow, rock, trees, or cloud, but the controls remain blunt: black pill CTAs, white reverse buttons, compact tags, and restrained hover scale. Shadow mostly stays out of the chrome. Depth comes from the photograph, not from a SaaS elevation stack.

Typography is the second signature. `Ridgeway Sans` carries the commercial UI with a light 300 body and a 500 heading rhythm. `Copernicus` appears as the editorial voice: weight 500, line-height 1.1, and `letter-spacing: -.03em`. It is the caption style of an activist field report dropped into a retail page: not decorative heritage, not newspaper nostalgia, but dense editorial pressure where the brand needs a point of view. Do not rebuild this with Inter and a mountain photo; the personality will collapse.

The observed screenshot is a waiting/maintenance state rather than the full live homepage: white header, black Patagonia wordmark, full-bleed outdoor image, and a translucent white information panel. I treat that as an important brand surface, but not as the only homepage state. The CSS and HTML show the broader commerce system: `hero-main`, `marketing-tile`, `product-tile`, `primary-navigation`, Bootstrap-style button variables, and a heavy responsive layer. Even in the waiting state, the site acts like a temporary ranger-station sign placed over the landscape: service message in a pale panel, brand mark overhead, nature carrying the emotional load.

Negative identity matters here. There is no second brand color trying to become Patagonia green. There is no glossy gradient pretending to be a sunset. There is no card-shadow ladder turning the outdoors into a dashboard. The craft is quieter and more stubborn: image-first surfaces, `#000000`/`#FFFFFF` controls, `#91ABE9` focus affordances, small hover scale on buttons, and serif editorial accents placed sparingly.

### Key Characteristics

- Monochrome core: `#000000` and `#FFFFFF` carry most brand interaction.
- Photography does the emotional work; UI chrome stays plain and durable.
- `Ridgeway Sans` for retail structure, `Copernicus` for editorial emphasis.
- Body text often sits at weight 300; headings and links move to 500.
- Primary CTAs are black pill buttons with `3rem` radius and `.2rem` border.
- Button hover uses scale `1.044`, not color fireworks.
- Product and marketing tiles use image crops with compact overlays.
- Focus visibility is explicit: `#91ABE9` appears as a repeat focus border.
- Breakpoints are Bootstrap-like but expanded through 1600px and 1800px.
- There is no rich brand color ramp; color accents are functional states.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Outdoor Editorial
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **full-bleed outdoor photography restrained by black-and-white commerce controls**으로 기억된다.
> **Code Complexity**: high — large responsive commerce CSS with hero, product, nav, tile, focus, and motion variants.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Patagonia처럼 만들기 - 3가지만 하면 80%

```css
/* 1. Font + weight */
:root {
  --pata-font-sans: "Ridgeway Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --pata-font-serif: "Copernicus", Georgia, serif;
}
body {
  font-family: var(--pata-font-sans);
  font-weight: 300;
}

/* 2. Monochrome commerce floor */
:root {
  --pata-bg-page: #FFFFFF;
  --pata-text: #000000;
  --pata-muted: #4A4A4A;
  --pata-focus: #91ABE9;
}

/* 3. Pill CTA */
.btn {
  border-radius: 3rem;
  border: .2rem solid transparent;
  padding: .9rem 2.8rem;
  font-weight: 500;
}
.btn-primary {
  background: #000000;
  color: #FFFFFF;
}
.btn:not(.btn-text-only):hover {
  transform: perspective(1px) scale(1.044) translate(0, 0);
}
```

**절대 하지 말아야 할 것 하나**: Patagonia를 green/earth-tone palette 사이트로 만들지 말 것. 실제 UI의 canonical interaction color는 `#000000`이고, green/brown은 사진 안에 머문다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.patagonia.com/home/` |
| Fetched | 2026-04-23T11:49:00+09:00 |
| Extractor | reused phase1 assets from `insane-design/patagonia/` |
| HTML size | 384942 bytes |
| CSS files | 9 CSS files, roughly 1.75 MB combined |
| Token prefix | `pata` |
| Method | existing CSS/HTML/screenshot reuse, phase1 JSON, manual interpretation |
| Screenshot | `insane-design/patagonia/screenshots/hero-cropped.png` |
| Caveat | Screenshot captured a waiting state, not a fully interactive retail homepage |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: server-rendered commerce page with large compiled CSS bundle.
- **Design system**: Patagonia local layer over Bootstrap-style variables.
- **CSS architecture**:
  ```css
  :root                       --pata-font-* and --bs-breakpoint-*
  .btn / .btn-primary          Bootstrap-like component variables
  .hero-main / .marketing-tile Patagonia-specific experience components
  .product-tile / .card        commerce listing components
  ```
- **Class naming**: BEM-like retail classes: `hero-main__overlay-info`, `product-tile__meta`, `primary-navigation-overflow`.
- **Default theme**: mixed. Most UI surfaces are light, but hero/media components support dark and on-image modes.
- **Font loading**: custom brand families exposed through CSS custom properties, with system fallbacks.
- **Canonical anchor**: photography-first commerce, not abstract brand illustration.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Ridgeway Sans` for core UI, `Copernicus` for editorial/serif emphasis.
- **Code font**: `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`.
- **Weight normal / bold**: `300` / `700`, with `500` as the dominant heading/link weight and `850` for heavy display cases.

```css
:root {
  --pata-font-sans: "Ridgeway Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --pata-font-serif: "Copernicus", "Palatino Linotype", Palatino, Georgia, serif;
  --pata-font-special: "BT Belwe W01", system-ui, -apple-system, "Segoe UI", sans-serif;
  --pata-font-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

body {
  font-family: var(--pata-font-sans);
  font-weight: 300;
}

.font__serif,
.font__secondary {
  font-family: var(--pata-font-serif) !important;
  font-weight: 500 !important;
  letter-spacing: -.03em !important;
  line-height: 1.1 !important;
}
```

### Note on Font Substitutes

- **Ridgeway Sans** is brand-specific. If unavailable, use `Avenir Next` first, then `Helvetica Neue`, then system UI. Keep body at 300 and links/headings at 500; do not compensate by making everything 400.
- **Copernicus** can be approximated with `Georgia` or `Palatino`, but only with Patagonia's correction: `font-weight: 500`, `line-height: 1.1`, and `letter-spacing: -.03em`.
- **BT Belwe W01** appears as a special voice token. If missing, avoid inventing a decorative replacement; fall back to the sans stack unless the exact editorial surface calls for it.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `body-sm` | `1.2rem` | `300` | `1.5` | `0` |
| `body` | `1.4rem` | `300` | `1.5` | `0` |
| `body-lg` | `1.6rem` | `300` | `1.5` | `0` |
| `text-link` | `1.6rem` | `500` | inherited | underline on hover |
| `heading` | `2rem` common | `500` | `1.2` | `0` |
| `display-1` | `calc(1.625rem + 2.8125vw)` | `300` | `1.2` | `0` |
| `serif-special` | contextual | `500` | `1.1` | `-.03em` |

> ⚠️ Key insight: Patagonia's typography is not heavy outdoor shouting. The commercial UI is light and functional, while editorial personality enters through `Copernicus` and tight negative tracking.

### Principles

1. Body is intentionally light at `300`; defaulting to `400` makes the commerce layer feel heavier than Patagonia's CSS.
2. `500` is the structural weight: headings, links, serif accents, and button labels use it to create firmness without going corporate-bold.
3. `Copernicus` is not a generic serif flourish. It uses `letter-spacing: -.03em` and `line-height: 1.1`, giving editorial density.
4. Heavy `850` exists, but as a special case, not as the default hero voice.
5. Text links are simple: no permanent decorative underline, but clear underline on hover where pointer devices exist.
6. Japanese font stacks are explicitly specified, showing that localization is part of the system rather than an afterthought.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (monochrome anchor)

| Token | Hex |
|---|---|
| `--bs-btn-bg` in `.btn-primary` | `#000000` |
| `--bs-btn-color` in `.btn-primary` | `#FFFFFF` |
| `--bs-btn-hover-bg` | `black` / `#000000` |
| `--bs-btn-active-bg` | `black` / `#000000` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `.btn-light --bs-btn-bg` | `#FFFFFF` |
| `.btn-light --bs-btn-color` | `#000000` |
| `.btn-dark --bs-btn-hover-bg` | `#262626` |
| `.btn-dark --bs-btn-active-bg` | `#333333` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| page | `#FFFFFF` | `#000000` |
| soft surface | `#F5F5F5` | `#121212` |
| border | `#CCC` | `#4A4A4A` |
| muted text | `#4A4A4A` | `#999999` |
| transparent overlay | `#0000004D` | `#FFFFFF26` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Focus | visible border | `#91ABE9` |
| Checkout / sale | primary danger commerce | `#E10000` |
| Pickup / backorder | operational badge | `#FA4616` |
| Success | Bootstrap success action | `#32B67A` |
| Warning | Bootstrap warning | `#FEB904` |
| Link/bootstrap blue | third-party/system residue | `#003DA5` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `bs-btn-primary-bg` | `#000000` | primary CTA, dark button, brand utility |
| `bs-btn-primary-color` | `#FFFFFF` | primary CTA text, reverse surfaces |
| `bs-focus-ring` | `#91ABE9` | focus-visible border across buttons and CTA circles |
| `pata-sale-red` | `#E10000` | checkout and sale-related urgency |
| `pata-badge-orange` | `#FA4616` | pickup/backorder badges |
| `pata-neutral-soft` | `#F5F5F5` | product tags and pale utility surfaces |
| `pata-text-muted` | `#4A4A4A` | disabled and muted text |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `.btn-primary --bs-btn-bg` | `#000000` | canonical CTA background |
| `.btn-light --bs-btn-bg` | `#FFFFFF` | reverse CTA on dark/image surfaces |
| `.btn-checkout --bs-btn-bg` | `#E10000` | commerce conversion state |
| `.badge-pickup, .badge-backorder` | `#FA4616` | stock/shipping notices |
| `.product-tag` | `#F5F5F5` | compact attribute chips |
| focus-visible border | `#91ABE9` | keyboard accessibility |

### 06-7. Dominant Colors (actual CSS frequency)

| Token | Hex | Frequency signal |
|---|---|---|
| black shorthand | `#000` | highest CSS count |
| white shorthand | `#FFF` | second major CSS count |
| transparent black | `#0000` | frequent transparent/reset state |
| focus blue | `#91ABE9` | repeated focus-visible color |
| full black | `#000000` | repeated canonical CTA/text color |
| border gray | `#CCC` | common chrome/hairline color |
| checkout red | `#E10000` | repeated commerce urgency color |
| soft neutral | `#F5F5F5` | utility surface and tags |

### 06-8. Color Stories

**`{colors.bs-btn-primary-bg}` (`#000000`)** - Patagonia's real UI brand anchor. It is used for primary CTA backgrounds, button hover/active states, logo-like weight, overlay controls, loading mountain strokes, and dark badges. The site does not need a second chromatic brand color.

**`{colors.bs-btn-primary-color}` (`#FFFFFF`)** - The reverse surface. It carries text on black controls and keeps on-image commerce readable without inventing translucent color systems.

**`{colors.bs-focus-ring}` (`#91ABE9`)** - The accessibility accent. It appears repeatedly on `focus-visible` button and CTA states, acting as a functional blue rather than a decorative brand blue.

**`{colors.pata-neutral-soft}` (`#F5F5F5`)** - The quiet utility floor. It appears in product tags and pale support surfaces, separating metadata from photography without turning the page into gray SaaS.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `.4rem` | 4px if root is 10px | heading margin, card title spacer |
| `.8rem` | 8px | card padding, tag padding, mobile nav gaps |
| `1.6rem` | 16px | row gutter, badge margin, tag gap, section micro rhythm |
| `2.4rem` | 24px | overlay spacing, mobile top action padding |
| `2.8rem` | 28px | button horizontal padding |
| `3.2rem` | 32px | offcanvas nav padding |
| `4rem` | 40px | hero caption padding, desktop content rhythm |
| `5.6rem` | 56px | primary nav overflow gap |
| `8rem` | 80px | desktop off-image hero side padding |
| `13vw` | viewport-relative | hero caption side breathing room |

**주요 alias**:
- `--bs-gutter-x` -> `1.6rem` for grid rows.
- `--primary-nav-offcanvas-padding-x` -> `3.2rem` for mobile menu.
- `--bs-btn-padding-x` -> `2.8rem` for pill CTAs.

### Whitespace Philosophy

Patagonia's spacing is field-practical, not gallery-luxury. Compact retail modules use `8px` and `16px` rhythms so product cards, badges, and tags remain scannable. Hero and image surfaces get larger viewport-relative breathing room because photography needs to carry narrative.

The important contrast is "open image, compact commerce." A hero can sit full-bleed with wide air around captions, but a product tag is only `.8rem` padded and a nav offcanvas is measured in exact `3.2rem` rails. That tension keeps the brand rugged rather than precious.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| `0` | `0` | resets, raw media edges, non-card primitives |
| `2px` | `2px` | product tags and tiny utility chips |
| `4px` | `4px` | small form/chrome elements |
| `8px` / `.8rem` | `8px` | cards, marketing tile containers |
| `1rem` | `10px` | medium component rounding |
| `3rem` | `30px` | primary pill buttons |
| `4rem` | `40px` | larger rounded CTA variants |
| `50%` / `100%` | circular | icon buttons, media masks, CTA circles |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none | `box-shadow: none` | default buttons and most chrome |
| active-button | `0 4px 5px #00000024, 0 1px 10px #0000001F, 0 2px 4px -1px #0003` | button active press state |
| focus | border-color `#91ABE9`, focus box shadow often zeroed | accessible focus state without glow-heavy styling |
| image depth | photography itself | depth is from image content, not card shadow |

Patagonia avoids the soft multi-layer card shadow language common in SaaS. Shadow is stateful and limited: active press feedback, occasional overlays, and image composition.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `button-hover-scale` | `scale(1.044)` | non-text buttons hover |
| `button-transition` | `color/background/border/box-shadow .15s ease-in-out` | Bootstrap-like button state changes |
| `overlay-info-enter` | `.6s cubic-bezier(.38,.41,.27,1)` | hero overlay content reveal |
| `overlay-fade` | `.1s` to `.2s cubic-bezier(.38,.41,.27,1)` | information overlays |
| `nav-overflow` | `.25s cubic-bezier(.22,.61,.36,1)` | dropdown/overflow visibility |
| `product-hover-image` | `scale(1.0362)` | product tile image hover |
| `reduced-motion` | transitions removed | `prefers-reduced-motion` respected |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `.container` starts at `672px`; nav overflow content uses `86.4rem`; large screens add 1200/1400/1600/1800 breakpoints.
- **Grid type**: Bootstrap flex rows plus component-specific CSS grid.
- **Column count**: hero off-image variants use 50/50, 40/60, or 60/40 splits at desktop.
- **Gutter**: `--bs-gutter-x: 1.6rem`.

### Hero

- **Pattern Summary**: full-width media or 2-column hero + image/photo treatment + overlay/foreground content + pill CTA.
- Layout: `.v2.hero-main` is a grid container; off-image left/right variants become two-column at `992px`.
- Background: image/video capable, with `.hero-main__bg`, `.hero-main__overlay`, and `.hero-main__video-overlay`.
- **Background Treatment**: image-led, not gradient-led. Overlay layers exist for readability and information reveals.
- H1: variable by content; base headings use weight `500`, line-height `1.2`; display can use `calc(1.625rem + 2.8125vw)` at weight `300`.
- Max-width: hero foreground uses grid columns and side padding up to `8rem`.

### Section Rhythm

```css
section {
  padding: 2.4rem 1.6rem;
  max-width: context-dependent;
}

@media only screen and (min-width: 992px) {
  .hero-main--off-image-left .hero-main__foreground-container {
    padding-left: 8rem;
    padding-right: 4rem;
  }
}
```

### Card Patterns

- **Card background**: `var(--bs-body-bg)` / usually `#FFFFFF`.
- **Card border**: Bootstrap default exists, but local `.card{border:none}` appears in global layer.
- **Card radius**: `var(--bs-border-radius)` and `.8rem` marketing tile radius.
- **Card padding**: `.8rem` default card spacer.
- **Card shadow**: generally none; image/product content carries depth.

### Navigation Structure

- **Type**: horizontal primary navigation with overflow dropdown and offcanvas mobile variant.
- **Position**: sticky behavior appears inside offcanvas top actions; primary overflow is absolute under nav.
- **Height**: content-driven; offcanvas top action padding is `2.4rem 0 .8rem`.
- **Background**: `#FFFFFF` for offcanvas top actions and light nav surfaces.
- **Border**: minimal; focus and state borders matter more than persistent nav dividers.

### Content Width

- **Prose max-width**: not globally fixed; retail modules use component-level constraints.
- **Container max-width**: `672px` base, with breakpoint variants from Bootstrap-style system.
- **Sidebar width**: mobile offcanvas `33.6rem`, max `100%`.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `0-575px` | base styles, offcanvas nav, compact card/tag behavior |
| Small | `576px` | Bootstrap small breakpoint |
| Tablet | `768px` | product tags become visible; many grid shifts begin |
| Desktop | `992px` | hero split layouts, primary nav overflow, desktop hover rules |
| XL | `1200px` | hero columns shift to 40/60 or 60/40 |
| XXL | `1400px` | large layout expansion |
| XXXL | `1600px` | high-width responsive tuning |
| XXXXL | `1800px` | extra-large viewport adjustments |

### Touch Targets

- **Minimum tap size**: buttons are roughly `calc(1.285rem + .2625vw)` text plus `.9rem` vertical padding, producing comfortable tap height.
- **Button height mobile**: content-driven pill, visually around 44px+ depending root scale.
- **Input height mobile**: not fully observed in homepage state; Bootstrap/form layer present.

### Collapsing Strategy

- **Navigation**: primary navigation switches to offcanvas with `33.6rem` width and sticky top actions.
- **Grid columns**: flex/grid modules collapse before `768/992px`; desktop hero split begins at `992px`.
- **Sidebar**: offcanvas maxes at `100%`, preventing overflow on narrow screens.
- **Hero layout**: off-image hero becomes single flow below desktop, then 50/50 or 40/60 at large widths.

### Image Behavior

- **Strategy**: media-first with `object-fit: cover` or `contain`.
- **Max-width**: common responsive image rules, product images capped by component.
- **Aspect ratio handling**: images fill product/hero containers; object-position utility classes provide crop control.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<a class="btn btn-primary" href="#">
  <span>Shop now</span>
</a>
```

| Spec | Value |
|---|---|
| Padding | `.9rem 2.8rem` |
| Radius | `3rem` |
| Border | `.2rem solid transparent` |
| Font | `var(--bs-body-font-family)` |
| Size | `calc(1.285rem + .2625vw)` |
| Weight | `500` |
| Primary bg | `#000000` |
| Primary text | `#FFFFFF` |
| Hover | `scale(1.044)` for non-text buttons |
| Active | multi-layer black alpha shadow |
| Focus | `#91ABE9` border |
| Disabled | opacity `.5`, pointer events none |
| Loading | spinner with `border: 2px solid #fff` |

### Badges

```html
<span class="badge badge-pickup">Pickup</span>
```

| Variant | Background | Text | Notes |
|---|---|---|---|
| `badge-pickup` | `#FA4616` | `#FFFFFF` | operational inventory status |
| `badge-backorder` | `#FA4616` | `#FFFFFF` | same urgent badge color |
| `badge--generic` | `#FFFFFF` | `#000000` | neutral badge |
| `hero-main.is-light .badge` | `#000000` | `#FFFFFF` | on-light hero inversion |

### Cards & Containers

```html
<article class="card product-tile">
  <div class="product-tile__image"></div>
  <div class="product-tile__meta"></div>
</article>
```

| Spec | Value |
|---|---|
| Card bg | `var(--bs-body-bg)` |
| Local border | often removed via `.card{border:none}` |
| Base padding | `.8rem` |
| Marketing tile radius | `.8rem` |
| Product image | `object-fit: cover` |
| Product hover | image scale `1.0362` or overlay opacity |
| Overlay | black overlay with opacity transition |

### Navigation

```html
<nav class="primary-navigation">
  <div class="primary-navigation-overflow"></div>
</nav>
```

| Spec | Value |
|---|---|
| Desktop overflow | absolute below nav, hidden until active |
| Overflow transition | `.25s cubic-bezier(.22,.61,.36,1)` |
| Tile in overflow | `30.5rem` wide, marketing tile max height `36.7rem` |
| Offcanvas width | `33.6rem`, max `100%` |
| Offcanvas padding | `3.2rem` x-axis |
| Top actions | sticky, `#FFFFFF`, grid columns `auto auto 3.2rem` |

### Inputs & Forms

| Spec | Value |
|---|---|
| Reset | inputs remove native border/radius/outline |
| Focus | global focus handling uses explicit `#91ABE9` for interactive controls |
| Radio tile inventory | quantity/discount and waitlist messaging patterns exist |
| Error motion | `btn-error` keyframe shakes horizontally `15px` |

Inputs are present in the commerce system, but the provided homepage/waiting screenshot does not expose full validation states.

### Hero Section

```html
<section class="v2 hero-main hero-main--on-image">
  <div class="hero-main__bg"></div>
  <div class="hero-main__overlay-info"></div>
</section>
```

| Spec | Value |
|---|---|
| Layout | grid, image/on-image or off-image variants |
| Desktop split | `50% 50%`, then `40% 60%` or `60% 40%` |
| Overlay info | absolute, bottom aligned, opacity gated |
| Overlay transition | `.6s cubic-bezier(.38,.41,.27,1)` |
| Caption padding | `4rem 13vw` |
| Foreground desktop padding | up to `8rem` on the outer side |

### 13-2. Named Variants

#### `button-primary`

- Background `#000000`, text `#FFFFFF`, radius `3rem`.
- Hover preserves black; interaction is scale, not hue shift.
- Focus border uses `#91ABE9`.

#### `button-light`

- Background `#FFFFFF`, text `#000000`.
- Used for reverse surfaces and on-image/dark contexts.
- Hover moves toward `#D9D9D9` / `#CCC`.

#### `button-checkout`

- Background `#E10000`, text `#FFFFFF`.
- Focus keeps checkout red but exposes `#91ABE9` border.
- Use only for transactional checkout urgency, not brand decoration.

#### `product-tag`

- Background `#F5F5F5`, color `#000000`, radius `2px`.
- Padding `.8rem`, size `1.2rem`, weight `300`.
- Mobile shows first child; tablet+ can show more tags.

#### `marketing-tile`

- Image-led tile, radius `.8rem`, max height in nav overflow `36.7rem`.
- Tile CTAs become smaller pills: radius `3rem`, padding `.5rem 2rem`, font size `1.2rem`.

### 13-3. Signature Micro-Specs

```yaml
black-pill-scale-click:
  description: "Primary CTAs feel like durable gear hardware rather than glossy ecommerce chrome."
  technique: "background: #000000; color: #FFFFFF; border-radius: 3rem; border: .2rem solid transparent; padding: .9rem 2.8rem; hover transform: perspective(1px) scale(1.044) translate(0, 0)"
  applied_to: ["{component.button-primary}", ".btn:not(.btn-text-only)", ".btn:not(.btn-underline)"]
  visual_signature: "A black utility pill that subtly pushes forward on hover without changing brand hue."

editorial-serif-tightening:
  description: "Activism/editorial language gets a denser voice than the retail UI."
  technique: "font-family: var(--pata-font-serif); font-weight: 500; letter-spacing: -.03em; line-height: 1.1"
  applied_to: [".font__serif", ".font__secondary", ".font-special-sentinel"]
  visual_signature: "A compact field-report caption texture dropped into otherwise plain sans commerce."

functional-blue-focus-border:
  description: "Accessibility color is functional, not a secondary brand palette."
  technique: "focus-visible border-color: #91ABE9 with focus box-shadow frequently zeroed; used across black, light, dark, checkout, and circular CTA variants"
  applied_to: ["{component.button-primary}", "{component.button-light}", "{component.checkout-button}", ".cta-circle"]
  visual_signature: "A clear blue edge appears only when interaction needs it, cutting through the monochrome UI."

photo-overlay-information-reveal:
  description: "Hero and media modules let photography lead until supporting information is intentionally exposed."
  technique: "absolute bottom-aligned overlay info; opacity/transform gates; transition: .6s cubic-bezier(.38,.41,.27,1); overlay fade .1s to .2s cubic-bezier(.38,.41,.27,1)"
  applied_to: [".hero-main__overlay-info", ".hero-main__overlay", ".hero-main__video-overlay", "product overlay wrappers"]
  visual_signature: "Text and controls rise out of the image instead of sitting in permanent decorative cards."

compact-product-tag-chip:
  description: "Product metadata is treated as clipped inventory labeling, not badge decoration."
  technique: "background: #F5F5F5; color: #000000; border-radius: 2px; padding: .8rem; font-size: 1.2rem; font-weight: 300; first child visible on mobile, expanded tags from tablet"
  applied_to: ["{component.product-tag}", ".product-tag", ".product-tile__meta"]
  visual_signature: "Small pale rectangular chips sit close to product imagery like utilitarian catalog labels."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Direct noun or activism/product topic, little ornament | "Activism" |
| Primary CTA | Short retail command | "Shop now" style CTA expected |
| Secondary CTA | Link-like, underline on hover | learn/read/explore actions |
| Subheading | Plain explanation, not hype copy | outdoor sports, gear, activism |
| Tone | Field-practical, advocacy-aware, commerce-capable | brand values and product utility coexist |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Patagonia - copy into your root stylesheet */
:root {
  /* Fonts */
  --pata-font-sans: "Ridgeway Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --pata-font-serif: "Copernicus", "Palatino Linotype", Palatino, Georgia, serif;
  --pata-font-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --pata-font-weight-normal: 300;
  --pata-font-weight-heading: 500;
  --pata-font-weight-bold: 700;

  /* Brand / UI colors */
  --pata-color-black: #000000;
  --pata-color-white: #FFFFFF;
  --pata-color-focus: #91ABE9;
  --pata-color-sale: #E10000;
  --pata-color-pickup: #FA4616;
  --pata-color-soft: #F5F5F5;
  --pata-color-muted: #4A4A4A;
  --pata-color-border: #CCC;

  /* Key spacing */
  --pata-space-xs: .8rem;
  --pata-space-sm: 1.6rem;
  --pata-space-md: 2.4rem;
  --pata-space-lg: 4rem;
  --pata-space-xl: 8rem;

  /* Radius */
  --pata-radius-chip: 2px;
  --pata-radius-tile: .8rem;
  --pata-radius-pill: 3rem;
}

body {
  font-family: var(--pata-font-sans);
  font-weight: var(--pata-font-weight-normal);
  background: var(--pata-color-white);
  color: var(--pata-color-black);
}

.pata-btn {
  border: .2rem solid transparent;
  border-radius: var(--pata-radius-pill);
  padding: .9rem 2.8rem;
  font-weight: 500;
  line-height: 1.2;
  transition: color .15s ease-in-out, background-color .15s ease-in-out,
    border-color .15s ease-in-out, box-shadow .15s ease-in-out;
}

.pata-btn-primary {
  background: var(--pata-color-black);
  color: var(--pata-color-white);
}

.pata-btn-primary:hover {
  transform: perspective(1px) scale(1.044) translate(0, 0);
}

.pata-btn-primary:focus-visible {
  border-color: var(--pata-color-focus);
}

.pata-serif {
  font-family: var(--pata-font-serif);
  font-weight: 500;
  letter-spacing: -.03em;
  line-height: 1.1;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `{colors.bs-btn-primary-bg}` | `#000000` |
| Background | `{colors.bs-btn-primary-color}` | `#FFFFFF` |
| Text primary | `{colors.bs-btn-primary-bg}` | `#000000` |
| Text muted | `{colors.pata-text-muted}` | `#4A4A4A` |
| Border | `{colors.pata-border-soft}` | `#CCC` |
| Focus | `{colors.bs-focus-ring}` | `#91ABE9` |
| Success | Bootstrap success | `#32B67A` |
| Error / checkout | `{colors.pata-sale-red}` | `#E10000` |

### Example Component Prompts

#### Hero Section

```text
Patagonia 스타일 히어로 섹션을 만들어줘.
- 배경: full-bleed outdoor photography, gradient mesh 금지
- H1: Ridgeway Sans, responsive display size, weight 300 or 500, line-height 1.2
- editorial accent가 필요하면 Copernicus, weight 500, tracking -.03em, line-height 1.1
- CTA: #000000 background, #FFFFFF text, 3rem radius, .9rem 2.8rem padding
- Focus: #91ABE9 border
- 레이아웃: mobile single flow, desktop 50/50 or on-image overlay
```

#### Card Component

```text
Patagonia 스타일 product/marketing tile을 만들어줘.
- 사진이 주인공: object-fit cover, image crop utilities
- 카드 chrome은 최소화: border none or #CCC hairline, shadow none
- radius: marketing tile .8rem, product tag 2px
- tag: #F5F5F5 bg, #000000 text, .8rem padding, 1.2rem, weight 300
- hover: image scale 1.0362 or overlay opacity transition, 큰 shadow 금지
```

#### Badge

```text
Patagonia 스타일 badge를 만들어줘.
- generic badge: #FFFFFF bg, #000000 text
- on-light hero badge: #000000 bg, #FFFFFF text
- operational pickup/backorder: #FA4616 bg, #FFFFFF text
- sale/checkout urgency는 #E10000, brand color로 남용하지 말 것
```

#### Navigation

```text
Patagonia 스타일 navigation을 만들어줘.
- desktop: horizontal primary nav + overflow dropdown
- mobile: offcanvas width 33.6rem max 100%, x padding 3.2rem
- overflow transition: .25s cubic-bezier(.22,.61,.36,1)
- overflow tile: image marketing tile radius .8rem, CTA pill radius 3rem
- nav surface: #FFFFFF with black text, heavy decorative borders 금지
```

### Iteration Guide

- **색상 변경 시**: green/brown outdoor palette를 UI brand로 만들지 말 것. 사진 안의 자연색과 UI token을 분리한다.
- **폰트 변경 시**: `Ridgeway Sans` unavailable이면 `Avenir Next`로, `Copernicus` unavailable이면 `Georgia/Palatino`로 가되 `-.03em` serif correction을 유지한다.
- **여백 조정 시**: small commerce modules use `.8rem/1.6rem`; hero/photography surfaces can use `4rem/8rem/13vw`.
- **컴포넌트 추가 시**: black/white pill, explicit blue focus, no decorative gradient.
- **모션 추가 시**: use `.15s` UI transitions and existing cubic-bezier curves. Do not introduce bouncy SaaS animation.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#000000` as the canonical interactive brand anchor.
- Let photography carry atmosphere and color; keep UI chrome black, white, gray, and functional.
- Keep body weight at `300` and headings/links/buttons at `500` unless a component explicitly uses `700` or `850`.
- Use `Ridgeway Sans` for UI and `Copernicus` for editorial emphasis.
- Preserve `#91ABE9` focus-visible affordances on interactive controls.
- Use `3rem` pill radius for primary buttons and `2px` radius for product tags.
- Use image overlay reveals and restrained scale transforms instead of large decorative animation.
- Respect `prefers-reduced-motion` for hero/nav transitions.

### ❌ DON'T

- 배경을 `#F4F4F4` 또는 cream으로 두지 말 것 - 대신 core page surfaces use `#FFFFFF`.
- primary CTA를 `#2E7D32`, `#006B3F`, 또는 earth green으로 두지 말 것 - 대신 `#000000` 사용.
- primary CTA 텍스트를 `#000000`으로 두지 말 것 - black CTA에는 `#FFFFFF` 사용.
- body text를 `#333333`으로 통일하지 말 것 - primary text is `#000000`, muted states use `#4A4A4A`.
- focus state를 `#006B3F` 또는 brand green으로 바꾸지 말 것 - observed focus border is `#91ABE9`.
- checkout/action urgency를 `#FF0000`으로 재해석하지 말 것 - Patagonia commerce red is `#E10000`.
- pickup/backorder badge를 `#E10000`로 합치지 말 것 - observed operational orange is `#FA4616`.
- product tag background를 `#FFFFFF`로 비워두지 말 것 - compact tag surface uses `#F5F5F5`.
- body에 `font-weight: 400`을 기본값으로 두지 말 것 - Patagonia body rhythm is weight `300`.
- CTA를 `border-radius: 8px` 카드 버튼으로 만들지 말 것 - primary buttons use `3rem` pill radius.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **Second brand color: none** - there is no Patagonia green/blue UI ramp in the observed CSS system.
- **Decorative gradients: zero** - outdoor imagery provides atmosphere; gradient backgrounds would be synthetic.
- **SaaS card shadow language: absent** - most chrome has no shadow, and active shadow is state feedback only.
- **Inter default typography: never** - `Ridgeway Sans` and `Copernicus` are central to the brand.
- **Rounded card abundance: absent** - radius exists, but cards do not become a soft dashboard.
- **Permanent underline links: limited** - text links underline on hover, not as constant decoration.
- **Bouncy motion: none** - transitions are short, cubic-bezier controlled, and reduce-motion aware.
- **High-saturation accent palette: absent** - red/orange/blue are operational states, not palette decoration.
- **Generic mountain illustration: none** - use actual photography or the real Patagonia mark, not hand-drawn SVG scenery.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Waiting state screenshot** - `hero-cropped.png` shows a "Sit tight" waiting/maintenance panel over outdoor photography. The full live homepage hero may differ.
- **Single URL scope** - analysis is limited to `https://www.patagonia.com/home/` and reused local phase1 assets. Checkout, account, search, PDP, and cart flows were not visited.
- **Color token extraction gap** - phase1 found `total_vars: 0` in resolved color tokens, even though compiled CSS contains many custom properties and Bootstrap-like component variables. Color interpretation is therefore CSS-pattern based, not full token-tier based.
- **No official DS documentation** - `lv2` is inferred from CSS consistency and component classes, not from a public Patagonia design system guide.
- **Form validation states not fully surfaced** - form/reset and radio inventory classes exist, but the provided homepage state does not expose complete input, error, success, and loading flows.
- **Motion JS not audited** - CSS transitions and keyframes were observed, but JavaScript-driven scroll, carousel, and lazy-load behavior was not deeply traced.
- **Logo/SVG color contamination possible** - CSS frequency includes icon, Bootstrap, and operational colors. Brand color was selected by interaction role, not raw frequency alone.
- **Mobile visual measurement not screenshot-verified** - responsive behavior is derived from media queries and component CSS, not a fresh mobile screenshot.
- **Exact root rem scale assumed** - CSS uses rem heavily and `font-size: var(--bs-root-font-size)`; pixel conversions assume the common 10px-style commerce root where applicable.
