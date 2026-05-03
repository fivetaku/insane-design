---
schema_version: 3.2
slug: nothing
service_name: Nothing
site_url: https://nothing.tech
fetched_at: 2026-05-03T06:55:58Z
default_theme: light
brand_color: "#002F6C"
primary_font: NType82-Regular
font_weight_normal: 400
token_prefix: nothing

bold_direction: Dot Matrix Industrial
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: editorial-product
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Tailwind utility layer plus custom Nothing fonts, frost classes, product widget grid, and 75 CSS variables; token tiers are present but not a full public DS."

colors:
  surface-lightest: "#F4F4F4"
  surface-white: "#FFFFFF"
  accent-blue: "#002F6C"
  grey-official: "#B1B3B3"
  grey-lighter: "#E5E7EB"
  grey-mid: "#999999"
typography:
  display: "NType82-Regular"
  logo: "Ndot-Regular"
  mono: "LatteraMonoLL"
  ladder:
    - { token: type-logo, size: "1.25rem", weight: 55, line_height: "1.35rem" }
    - { token: type-headline, size: "1.5rem", weight: 100, line_height: "1.65rem" }
    - { token: type-product-name, size: "1.25rem", weight: 55, line_height: "1.25rem" }
    - { token: type-callout, size: ".6875rem", weight: 400, line_height: ".75625rem" }
  weights_used: [55, 100, 400, 500, 600, 700]
  weights_absent: [300, 800, 900]
components:
  nav-frost-bar: { bg: "#FFFFFF", opacity: ".8", radius: ".5rem", blur: "45px" }
  product-frost-card: { bg: "#FFFFFF", opacity: ".8", radius: ".5rem", padding: "8px" }
  callout-chip: { bg: "hsl(var(--grey-darker) / .05)", radius: ".5rem", padding: "4px 8px" }
---

# DESIGN.md — Nothing (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Nothing does not behave like a normal electronics store. It turns commerce into a transparent product stage: full-screen product imagery, compressed dot-matrix language, and a floating layer of frosted UI controls. The page feels like a device OS more than a shop page. The browser is treated as a piece of hardware glass, and every label is a tiny status readout.

The visual identity is intentionally near-monochrome. The floor is #F4F4F4 (`{colors.surface-lightest}`), while cards and navigation sit as translucent #FFFFFF (`{colors.surface-white}`) panels with `backdrop-filter: blur(45px)`. There is no second brand color doing retail work; #002F6C (`{colors.accent-blue}`) exists in the token set, but the homepage identity is built from smoke-white glass, cool grey ink, and exposed product hardware.

Nothing's page behaves like a teardown table in a clean lab: the device is the specimen, the grid is the measuring mat, and the UI is only a thin sheet of acrylic hovering above it. Unlike Apple, where the gallery wall disappears behind polish, Nothing keeps the industrial bench visible. The surface is not pure white air; it is a light grey worktop with transparent parts laid out under glass.

Typography is the loudest asset. `Ndot-Regular` creates the signature pixel-dot logo and product-name texture, like silkscreen ink printed on the inside of a transparent shell. `NType82-Regular` carries the large editorial product statements, usually at a surprisingly light `font-weight: 100`, so the words feel etched rather than shouted. `LatteraMonoLL` is reserved for tiny uppercase interface copy, making product buttons read like embedded firmware labels rather than conventional marketing buttons.

The page rhythm is industrial but playful: each product panel is a full-viewport scene with a hidden 3-column mobile to 12-column desktop widget grid, then a bottom-centered frosted product card. The card is not a generic rounded marketing card. It is a small glass control surface pinned above a full-screen object, with a 128px to 148px product image tucked into the right edge, like a retail tag that has learned to behave like an operating-system widget.

The strongest Nothing move is subtraction with hardware residue. No glossy color ribbon, no heavy shadow stack, no inflated CTA pill. Shadow is mostly replaced by blur, brand color by dot glyphs, and hierarchy by the physical contrast between a large photographed object and the tiny control panel that sits over it.

이 페이지는 commerce 카탈로그가 아니라 **하드웨어 갤러리의 진열장 안 쇼룸**처럼 정렬된다. min-h-svh product scene은 천장이 높은 무대 한 칸, frost-white-intense card는 그 무대 앞에 핀으로 꽂힌 박물관식 캡션 카드다. dot-matrix logo는 진열장 라벨, 128px product image는 진열장 안의 단 하나뿐인 전시품이다. 카탈로그식 그리드 대신, 각 제품은 자신의 진열실을 단독으로 차지하고 측정 매트 위에 놓인다 — 셀러가 외치지 않고 큐레이터가 침묵으로 라벨을 붙여 둔다. 갤러리의 분위기가 마케팅 카탈로그를 대체하고, 제품 사진은 쇼룸의 단독 전시처럼 먼저 도착한다.

### Key Characteristics

- Dot-matrix identity is structural: `Ndot-Regular` appears in logo and product names, not just a decorative logo.
- The dominant canvas is #F4F4F4, with pure white used as glass, not as the entire page floor.
- `backdrop-filter: blur(45px)` is the main material effect for nav, product cards, and utility controls.
- Hero/product panels use `min-h-svh`, creating app-like full-screen product chapters.
- Product CTA cards are bottom-centered, max-width `32rem`, and layered over imagery.
- Grid math is explicit: mobile uses 3 columns, desktop uses 12 columns, both tied to viewport units.
- Interface labels are tiny uppercase mono callouts: `.6875rem`, line-height `.75625rem`, weight 400.
- Radius is restrained at `.5rem`; Nothing avoids soft, bubbly consumer-app geometry.
- Saturated accent is nearly absent; #002F6C exists as an accent token, not the page's main identity.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Dot Matrix Industrial
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **frosted product OS layered over full-screen hardware photography**으로 기억된다.
> **Code Complexity**: high — viewport grid math, frosted material classes, animated product panels, and custom font hierarchy must work together.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Nothing처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "NType82-Regular", "Arial Narrow", system-ui, sans-serif;
  font-weight: 400;
}

.nothing-logo,
.nothing-product-name {
  font-family: "Ndot-Regular", monospace;
  font-weight: 55;
  text-transform: lowercase;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #F4F4F4;
  --glass: #FFFFFF;
  --accent-blue: #002F6C;
}
body { background: var(--bg); color: hsl(180 1% 35%); }

/* 3. 브랜드 물성 */
.nothing-frost {
  background-color: rgb(255 255 255 / .8);
  backdrop-filter: blur(45px);
  border-radius: .5rem;
}
```

**절대 하지 말아야 할 것 하나**: Nothing을 파란 CTA 중심 SaaS처럼 만들지 말 것. #002F6C는 실제 CSS에 있지만, 정체성은 색보다 `Ndot` 타이포 + frosted glass + product stage 구조에 있다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://nothing.tech` |
| Fetched | 2026-05-03T06:55:58Z |
| Reuse source | `insane-design/nothing/phase1`, `css`, `index.html`, `screenshots` |
| HTML size | 206,524 bytes |
| CSS files | 2 files: `app-D6o14BgC.css` 5,455 bytes, `tailwind-CMZ1pmgm.css` 54,927 bytes |
| Token prefix | `nothing` (inferred; source variables mostly Tailwind + custom `--grey-*`, `--accent-*`) |
| Method | Existing phase1 JSON + exact CSS/HTML inspection; no Step 6 HTML report render |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Shopify/React-style rendered storefront HTML with Tailwind utility output.
- **Design system**: Nothing custom layer over Tailwind utilities; no public DS namespace found.
- **CSS architecture**:
  ```css
  :root custom vars       --grey-darker, --grey-official, --accent-blue
  Tailwind internals      --tw-ring-color, --tw-shadow, --tw-backdrop-blur
  Branded utilities       .type-logo, .type-headline, .frost-white-intense
  Component composition   utility-heavy class strings in HTML
  ```
- **Class naming**: Tailwind atomic utilities plus branded semantic helpers (`type-logo`, `type-product-name`, `frost-white-intense`, `widget-grid`).
- **Default theme**: light (`bg-grey-lightest`, resolved visually to #F4F4F4).
- **Font loading**: custom brand families referenced directly in CSS: `NType82-Regular`, `Ndot-Regular`, `LatteraMonoLL`.
- **Canonical anchor**: bottom-centered frosted product card over a full-viewport product scene.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `NType82-Regular` and `NType82-Headline` (Nothing proprietary brand fonts)
- **Logo/product font**: `Ndot-Regular` (signature dot-matrix family)
- **Code/control font**: `LatteraMonoLL` (tiny uppercase control copy)
- **Weight normal / bold**: `400` / `700`, but the important display weights are `100` and `55`

```css
:root {
  --nothing-font-body:    "NType82-Regular", sans-serif;
  --nothing-font-logo:    "Ndot-Regular", sans-serif;
  --nothing-font-control: "LatteraMonoLL", sans-serif;
  --nothing-weight-hair:  55;
  --nothing-weight-light: 100;
  --nothing-weight-body:  400;
}

.type-logo {
  font-family: Ndot-Regular, sans-serif;
  font-size: 1.25rem;
  line-height: 1.35rem;
  font-weight: 55;
  text-transform: uppercase;
}

.type-headline {
  font-family: NType82-Regular, sans-serif;
  font-size: 1.5rem;
  line-height: 1.65rem;
  font-weight: 100;
}

.type-callout {
  font-family: LatteraMonoLL, sans-serif;
  font-size: .6875rem;
  line-height: .75625rem;
  font-weight: 400;
  text-transform: uppercase;
}
```

### Note on Font Substitutes

- **Ndot-Regular** is not replaceable with a normal mono. Use a dot-matrix display fallback or keep this as a webfont asset. If unavailable, use a bitmap/dot font at weight 400 and reduce letter density rather than substituting Inter.
- **NType82-Regular** can be approximated with a condensed grotesk such as `Arial Narrow` only for layout testing. Preserve the light display feel by using weight 100-300, not standard 600.
- **LatteraMonoLL** can fall back to `ui-monospace`, but reduce size to `.6875rem` and keep uppercase. The smallness is part of the control-surface feeling.
- Avoid `letter-spacing` inflation as a fake tech aesthetic. The source classes rely more on custom glyph shapes and low weights than tracking tricks.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `.type-logo` | `1.25rem` | `55` | `1.35rem` | normal |
| `.type-headline` | `1.5rem` | `100` | `1.65rem` | normal |
| `.type-product-name` | `1.25rem` | `55` | `1.25rem` | normal |
| `.type-callout` | `.6875rem` | `400` | `.75625rem` | normal |
| body utilities | `1rem` common | `400` | utility-defined | normal |
| larger text utilities | `2rem`, `2.5rem` observed | mixed | utility-defined | normal |

> ⚠️ Key insight: the unusual weights `55` and `100` are not typos. They are Nothing's way of making text feel like hardware labeling rather than web marketing.

### Principles

1. Dot type is identity, not decoration. Use `Ndot-Regular` for logo/product names where the brand should be felt immediately.
2. Display language is light: `.type-headline` uses weight `100`, so recreations that jump to 600 lose the transparent hardware tone.
3. Interface copy becomes small and uppercase through `LatteraMonoLL`; the callout class is only `.6875rem`, so buttons feel like labels on a device.
4. Nothing accepts multiple font families in one component. A product card can pair `NType82-Regular`, `Ndot-Regular`, and `LatteraMonoLL` in a single 160px-tall surface.
5. The system does not depend on heavy negative tracking. The glyph design carries the signal.
6. Weight 800/900 is absent in observed CSS; the page avoids loud, heavy tech-bro typography.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (monochrome-dominant)

| Token | Hex / Value |
|---|---|
| `--accent-blue` | #002F6C |
| `--accent-yellow` | hsl(47 100% 50%) |
| `--accent-red` | hsl(350 85% 42%) |

### 06-2. Brand Dark Variant

> N/A — dark classes exist (`dark:frost-grey-intense`, `dark:text-pure-white`), but full dark-mode palette mapping was not visited as a separate flow.

### 06-3. Neutral Ramp

| Step | Token | Value |
|---|---|---|
| page | `--grey-lightest` | hsl(0 0% 96%) / #F4F4F4 |
| official grey | `--grey-official` | hsl(180 1% 70%) / #B1B3B3 |
| lighter grey | `--grey-lighter` | hsl(180 1% 85%) / #E5E7EB |
| mid grey | literal | #999999 |
| white surface | `--color-light`, Tailwind white | #FFFFFF |
| dark text | `--grey-darker` | hsl(180 1% 35%) |

### 06-4. Accent Families

| Family | Key step | Hex / Value |
|---|---|---|
| Blue | `--accent-blue` | #002F6C |
| Yellow | `--accent-yellow` | hsl(47 100% 50%) |
| Red | `--accent-red` | hsl(350 85% 42%) |

### 06-5. Semantic

| Token | Hex / Value | Usage |
|---|---|---|
| `bg-grey-lightest` | #F4F4F4 | body/page floor |
| `frost-white-intense` | #FFFFFF at alpha | nav and product-card glass |
| `frost-grey-low` | hsl(var(--grey-darker) / .05) | small Discover chip |
| `text-grey-darker` | hsl(180 1% 35%) | nav/icon/body text |
| `--accent-blue` | #002F6C | low-frequency chromatic accent |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--color-light` | `#fff` | aside and base light surface |
| `--color-dark` | `#000` | aside borders and text contrast |
| `--tw-ring-color` | `rgb(255 255 255 / .6)` | focus ring |
| `--tw-backdrop-blur` | `blur(45px)` | frosted material classes |
| `--tw-shadow-color` | `hsl(var(--grey-darker) / .05)` | subtle shadow layer |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency clue |
|---|---|---|
| transparent black | `#0000` family | ring and transparent reset values |
| white glass | #FFFFFF / `#fffc` | nav, cards, surfaces |
| page grey | #F4F4F4 | body and product-stage floor |
| official grey | #B1B3B3 | neutral utility palette |
| accent blue | #002F6C | chromatic accent, low frequency |

### 06-8. Color Stories

**`{colors.surface-lightest}` (#F4F4F4)** — This is the floor, not a fallback. Nothing's product photography and frosted cards need a soft lab background, so pure white is reserved for glass and panels.

**`{colors.surface-white}` (#FFFFFF)** — White is used as material: a translucent control surface with 45px blur. Use it for nav bars and product cards, not as a flat marketing canvas.

**`{colors.accent-blue}` (#002F6C)** — The strongest chromatic token found, but it is not the identity engine. Treat it as a restrained accent, never as a SaaS-style brand wash.

**`{colors.grey-official}` (#B1B3B3)** — This cool neutral supports the industrial palette. It keeps the system technical without adding a second brand color.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--header-height` | `64px` | header/nav vertical system |
| `--aside-width` | `400px` | cart/side panel fixed width |
| `--grid-item-width` | `355px` | product grid width variable |
| `.m-4` / `.p-4` | `1rem` | nav shell and icon button padding |
| `.p-2` | `.5rem` | product frosted card internal shell |
| `.gap-2` | `.5rem` | mobile widget grid gap |
| `.md:gap-4` | `1rem` | desktop widget grid gap |
| `.px-8` | `2rem` | full-screen product panel inner track |
| `.py-8` | `2rem` | product panel vertical rhythm |
| `.pt-20` | `5rem` | first product scene clears fixed header |

**주요 alias**:
- `--header-height` -> `64px` (navigation system)
- `--aside-width` -> `400px` (off-canvas commerce panel)
- `--grid-item-width` -> `355px` (product module sizing)

### Whitespace Philosophy

Nothing's whitespace is viewport-based rather than section-based. Product chapters are `min-h-svh`; the large empty field belongs to the product photograph, not to copy blocks. UI floats above it in a compact bottom card, so the page can feel spacious without turning into a typical centered hero.

The contrast is important: the scene is huge, but controls are small. A `64px` header, `.5rem` card shell, `.6875rem` callout text, and 128px product image create a hardware-console density against a full-screen stage.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `.rounded-lg` | `.5rem` | nav container, frosted product card, callout button |
| `.rounded-md` | `.375rem` | generic Tailwind medium radius |
| `.rounded` | `.25rem` | small utility rounding |
| `.rounded-full` | `9999px` | circular/pill utility where needed |
| `.rounded-none` | `0` | full-bleed product/background images |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: navigation and product CTA use `max-w-lg` (`32rem`) centered at 50%.
- **Grid type**: CSS Grid inside `.widget-grid`; flex for nav/footer/menu composition.
- **Column count**: mobile `--mobile-cols: 3`; desktop `--desktop-cols: 12`.
- **Gutter**: `gap-2 gap-y-4`, upgraded to `md:gap-4` and `md:gap-y-0`.

### Hero
- **Pattern Summary**: `100svh + full-screen product photography + hidden viewport grid + bottom-centered frosted product card`
- Layout: repeated full-screen product panels, each with background imagery and an overlay CTA card.
- Background: absolutely positioned product/background image layer with `object-cover`.
- **Background Treatment**: image-overlay, with base64 legacy placeholder at opacity 1 and remote Sanity/Shopify imagery managed through opacity.
- H1: `Nothing (R)` appears as `type-logo`, 1.25rem / weight 55 / uppercase dot matrix.
- Max-width: key overlay UI uses `max-w-lg`; product grid width is computed from viewport: `calc((100svw - 176px - 32px*2) / 12)` on desktop.

### Section Rhythm

```css
.nothing-product-scene {
  min-height: 100svh;
  padding: 2rem 0;
  overflow: hidden;
}

.nothing-widget-grid {
  grid-template-columns: repeat(var(--desktop-cols), calc((100svw - 176px - 32px*2) / 12));
  grid-template-rows: repeat(6, calc((100svh - 5rem - 4rem) / 6));
  gap: 1rem;
}
```

### Card Patterns
- **Card background**: `frost-white-intense` -> white with alpha (`#fffc` source; represented as #FFFFFF surface token)
- **Card border**: mostly absent; separation is blur, opacity, and soft shadow rather than hard lines.
- **Card radius**: `.5rem`
- **Card padding**: outer anchor `p-4`, card `p-2`, content `p-4`
- **Card shadow**: subtle frosted depth; aside uses `box-shadow: 0 0 50px #0000004d`

### Navigation Structure
- **Type**: fixed top capsule, grid `80px / auto / 80px`, centered max width.
- **Position**: `fixed left-1/2 z-50`, translated back with `-translate-x-1/2-safe`.
- **Height**: wrapper `80px`, inner capsule `48px`; root `--header-height: 64px`.
- **Background**: `frost-white-intense`, dark mode maps to `frost-grey-intense`.
- **Border**: none in primary nav; glass material handles separation.

### Content Width
- **Prose max-width**: not a prose-first site; product CTA max-width is the meaningful constraint.
- **Container max-width**: `max-w-lg` for floating UI, full viewport for product scene.
- **Sidebar width**: `--aside-width: 400px`

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | default | 3-column product grid, `gap-2`, product image 128px |
| Small | `400px` / `640px` | Tailwind utility breakpoints present |
| Tablet | `768px` | `md:` grid, product image changes to 148px/144px utility |
| Desktop | `1024px`, `1280px` | wider Tailwind utilities available |
| Large | `1536px`, `1792px` | high-width Tailwind breakpoints present |

### Touch Targets
- **Minimum tap size**: nav icon buttons use `size-12` (48px).
- **Button height (mobile)**: nav/action controls use `h-12` where explicit.
- **Input height (mobile)**: not surfaced in observed homepage data.

### Collapsing Strategy
- **Navigation**: fixed compact capsule; left/right zones remain 80px each.
- **Grid columns**: 3 mobile columns collapse to 12 desktop columns via CSS variables and `md:`.
- **Sidebar**: cart/aside remains fixed 400px off-canvas when present.
- **Hero layout**: full-screen stacked product chapters; overlay CTA remains bottom centered.

### Image Behavior
- **Strategy**: absolute fill background images, `object-cover`, no rounded corners for full-stage image.
- **Max-width**: product card image group 128px mobile, 148px desktop.
- **Aspect ratio handling**: background is viewport-cropped; product thumbnail uses object-cover.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

#### Product Discover Chip

```html
<button class="type-product-name type-callout frost-grey-low dark:frost-grey-intense absolute bottom-6 right-2 mr-6 rounded-lg px-2 py-1">
  Discover
</button>
```

| Spec | Value |
|---|---|
| Font | `LatteraMonoLL`, `.6875rem`, uppercase |
| Background | `hsl(var(--grey-darker) / .05)` via `frost-grey-low` |
| Radius | `.5rem` |
| Padding | `px-2 py-1` |
| Placement | absolute, bottom/right within product card |
| Hover | product image hover shifts object position, chip remains quiet |

### Badges

> N/A — homepage evidence shows callout chips and utility buttons, not a distinct badge taxonomy.

### Cards & Containers

#### Product Frost Card

```html
<a class="absolute bottom-0 left-1/2 z-[30] w-full max-w-lg -translate-x-1/2 p-4" href="/products/phone-4a">
  <div class="frost-white-intense dark:frost-grey-intense relative flex justify-between rounded-lg p-2">
    <div class="type-headline flex flex-col justify-between p-4">
      <h2>Built different</h2>
      <h3 class="type-product-name">Phone ( 4a )</h3>
    </div>
  </div>
</a>
```

| Spec | Value |
|---|---|
| Container | bottom centered, full width until `max-w-lg` |
| Material | #FFFFFF alpha + `backdrop-filter: blur(45px)` |
| Radius | `.5rem` |
| Layout | flex between text stack and product image |
| Image | 128px mobile, 148px desktop group |
| State | `group-hover:object-center` on image |

### Navigation

```html
<header class="fixed left-1/2 z-50 flex w-full max-w-lg -translate-x-1/2-safe flex-col gap-0.5" style="height:80px">
  <div class="frost-white-intense m-4 flex min-h-12 flex-col overflow-y-auto rounded-lg" style="height:48px">
    <nav class="grid grid-cols-[80px,auto,80px]">...</nav>
  </div>
</header>
```

| Spec | Value |
|---|---|
| Shape | centered floating capsule rectangle |
| Height | 48px inner, 80px wrapper |
| Grid | `80px auto 80px` |
| Material | frosted white |
| Logo | `type-logo`, centered |
| Icon buttons | 48px square tap target |

### Inputs & Forms

> N/A — visible homepage evidence does not expose form inputs. Cookie preference controls exist, but full form validation/error states were not captured.

### Hero Section

| Spec | Value |
|---|---|
| Height | `min-h-svh` |
| Background | absolute image layer, `object-cover`, `rounded-none` |
| Grid | hidden/animated `widget-grid` with 3 mobile / 12 desktop columns |
| CTA | bottom-centered frosted product card |
| Motion | wrapper `transition: transform 0.4s ease`; aside transition `.2s ease-in-out` |

### 13-2. Named Variants

#### `nav-frost-bar`

| Property | Value |
|---|---|
| background | #FFFFFF with alpha (`#fffc` source) |
| blur | `45px` |
| radius | `.5rem` |
| dimensions | `max-w-lg`, 48px inner height |
| purpose | main site navigation as an OS-style floating surface |

#### `product-frost-card`

| Property | Value |
|---|---|
| background | #FFFFFF with alpha |
| blur | `45px` |
| radius | `.5rem` |
| padding | `p-2` shell + `p-4` content |
| purpose | product title, product name, Discover chip, thumbnail |

#### `callout-chip`

| Property | Value |
|---|---|
| font | `LatteraMonoLL`, `.6875rem`, uppercase |
| background | `hsl(var(--grey-darker) / .05)` |
| radius | `.5rem` |
| padding | `4px 8px` |
| purpose | low-volume control CTA |

### 13-3. Signature Micro-Specs

```yaml
dot-matrix-product-language:
  description: "Logo and product names use dot-matrix glyphs as the brand's interface language."
  technique: "font-family: Ndot-Regular; font-weight: 55; font-size: 1.25rem; line-height: 1.25rem to 1.35rem; text-transform switches by role."
  applied_to: ["{component.nav-frost-bar}", "{component.product-frost-card}"]
  visual_signature: "Product names feel silkscreened onto transparent hardware rather than typeset into a web card."

frost-45-control-surface:
  description: "The primary UI material is a hard frosted glass control layer."
  technique: "background-color: #FFFFFFcc / #fffc; backdrop-filter: blur(45px); border-radius: .5rem."
  applied_to: ["{component.nav-frost-bar}", "{component.product-frost-card}"]
  visual_signature: "White controls hover over product photography without hard borders or heavy shadow."

viewport-product-measuring-grid:
  description: "Product stages are choreographed on viewport math instead of a fixed marketing container."
  technique: "mobile repeat(var(--mobile-cols), calc((100svw - 64px - 16px*2)/3)); desktop repeat(var(--desktop-cols), calc((100svw - 176px - 32px*2)/12))."
  applied_to: ["{component.widget-grid}", "{component.product-scene}"]
  visual_signature: "The composition feels like an engineering measuring mat behind the hardware."

bottom-os-product-tag:
  description: "The product CTA is a compact OS widget pinned to the bottom of a full-screen object scene."
  technique: "position absolute; left: 50%; bottom: 0; max-width: 32rem; transform: translateX(-50%); p-2 shell plus p-4 content; 128px to 148px product image."
  applied_to: ["{component.product-frost-card}", "{component.product-scene}"]
  visual_signature: "The purchase surface reads like a floating device-control tag, not a conventional ecommerce card."

tiny-firmware-callout:
  description: "Action labels become small machine labels instead of retail buttons."
  technique: "font-family: LatteraMonoLL; font-size: .6875rem; line-height: .75625rem; font-weight: 400; text-transform: uppercase; padding: 4px 8px; radius: .5rem; background: hsl(var(--grey-darker) / .05)."
  applied_to: ["{component.callout-chip}", "{component.product-frost-card}"]
  visual_signature: "Every command feels embedded in hardware firmware rather than styled as a SaaS CTA."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Brand line | short rebellious tech nostalgia | "building a world where tech is fun again" |
| Product headline | two to four words, imperative/editorial | "Built different", "Find your match" |
| Product name | spaced punctuation, deliberate awkwardness | "Phone ( 4a )" |
| CTA | one-word command | "Discover" |
| Tone | playful industrial minimalism | "Come to Play", "Cut through the noise" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Nothing — copy into your root stylesheet */
:root {
  /* Fonts */
  --nothing-font-body:    "NType82-Regular", "Arial Narrow", system-ui, sans-serif;
  --nothing-font-dot:     "Ndot-Regular", monospace;
  --nothing-font-control: "LatteraMonoLL", ui-monospace, monospace;
  --nothing-weight-dot:   55;
  --nothing-weight-light: 100;
  --nothing-weight-body:  400;
  --nothing-weight-bold:  700;

  /* Core colors */
  --nothing-bg-page:      #F4F4F4;
  --nothing-surface:      #FFFFFF;
  --nothing-accent-blue:  #002F6C;
  --nothing-grey-official:#B1B3B3;
  --nothing-grey-lighter: #E5E7EB;
  --nothing-grey-mid:     #999999;

  /* Key spacing */
  --nothing-header-height: 64px;
  --nothing-aside-width:   400px;
  --nothing-card-pad:      .5rem;
  --nothing-scene-pad:     2rem;

  /* Radius + material */
  --nothing-radius-card: .5rem;
  --nothing-radius-sm:   .375rem;
  --nothing-frost-blur:  45px;
}

body {
  margin: 0;
  min-height: 100svh;
  background: var(--nothing-bg-page);
  color: hsl(180 1% 35%);
  font-family: var(--nothing-font-body);
  font-weight: var(--nothing-weight-body);
  -webkit-font-smoothing: antialiased;
}

.nothing-frost {
  background-color: rgb(255 255 255 / .8);
  -webkit-backdrop-filter: blur(var(--nothing-frost-blur));
  backdrop-filter: blur(var(--nothing-frost-blur));
  border-radius: var(--nothing-radius-card);
}

.nothing-nav {
  position: fixed;
  z-index: 50;
  left: 50%;
  top: 0;
  width: 100%;
  max-width: 32rem;
  transform: translateX(-50%);
  padding: 1rem;
}

.nothing-nav-inner {
  display: grid;
  grid-template-columns: 80px auto 80px;
  min-height: 48px;
}

.nothing-logo {
  font-family: var(--nothing-font-dot);
  font-size: 1.25rem;
  line-height: 1.35rem;
  font-weight: 55;
  text-transform: uppercase;
}

.nothing-product-scene {
  position: relative;
  min-height: 100svh;
  overflow: hidden;
  padding-block: 2rem;
}

.nothing-product-card {
  position: absolute;
  z-index: 30;
  left: 50%;
  bottom: 0;
  width: 100%;
  max-width: 32rem;
  transform: translateX(-50%);
  padding: 1rem;
}

.nothing-product-card__surface {
  display: flex;
  justify-content: space-between;
  padding: .5rem;
}

.nothing-headline {
  font-family: var(--nothing-font-body);
  font-size: 1.5rem;
  line-height: 1.65rem;
  font-weight: 100;
}

.nothing-product-name {
  font-family: var(--nothing-font-dot);
  font-size: 1.25rem;
  line-height: 1.25rem;
  font-weight: 55;
  text-transform: lowercase;
}

.nothing-callout {
  font-family: var(--nothing-font-control);
  font-size: .6875rem;
  line-height: .75625rem;
  font-weight: 400;
  text-transform: uppercase;
  border-radius: .5rem;
  background: hsl(180 1% 35% / .05);
  padding: .25rem .5rem;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Nothing-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        nothing: {
          page: '#F4F4F4',
          surface: '#FFFFFF',
          blue: '#002F6C',
          officialGrey: '#B1B3B3',
          lighterGrey: '#E5E7EB',
          midGrey: '#999999',
        },
      },
      fontFamily: {
        nothing: ['NType82-Regular', 'system-ui', 'sans-serif'],
        ndot: ['Ndot-Regular', 'monospace'],
        control: ['LatteraMonoLL', 'ui-monospace', 'monospace'],
      },
      fontWeight: {
        dot: '55',
        hair: '100',
      },
      borderRadius: {
        nothing: '.5rem',
      },
      backdropBlur: {
        nothing: '45px',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex / Value |
|---|---|---|
| Brand accent | `{colors.accent-blue}` | #002F6C |
| Background | `{colors.surface-lightest}` | #F4F4F4 |
| Surface | `{colors.surface-white}` | #FFFFFF |
| Text primary | `--grey-darker` | hsl(180 1% 35%) |
| Text muted | `{colors.grey-official}` | #B1B3B3 |
| Border/soft neutral | `{colors.grey-lighter}` | #E5E7EB |
| Mid grey | `{colors.grey-mid}` | #999999 |

### Example Component Prompts

#### Hero Section

```text
Nothing 스타일 product hero를 만들어줘.
- 전체 높이: min-height 100svh
- 배경: #F4F4F4 위에 full-bleed product photography, object-cover
- 상단 nav: max-width 32rem, 48px high, #FFFFFF alpha glass, backdrop-filter blur(45px), radius .5rem
- 하단 product card: bottom center, max-width 32rem, frosted #FFFFFF, radius .5rem, padding 8px shell + 16px content
- headline: NType82-Regular, 1.5rem, weight 100
- product name: Ndot-Regular, 1.25rem, weight 55, spaced parentheses
- CTA chip: LatteraMonoLL, .6875rem uppercase, hsl(180 1% 35% / .05), radius .5rem
```

#### Product Card

```text
Nothing product card component:
- Material: translucent #FFFFFF, backdrop-filter blur(45px), radius .5rem
- Layout: flex, text stack left, 128px product image right, desktop 148px
- Text: h2 with NType82-Regular 1.5rem weight 100; product name with Ndot-Regular 1.25rem weight 55
- CTA: tiny uppercase LatteraMonoLL chip, .6875rem, px 8px py 4px
- No hard border; separation comes from glass material and product-stage contrast
```

#### Navigation

```text
Nothing nav:
- fixed top, centered, width 100%, max-width 32rem, z-index 50
- inner height 48px, margin 16px, grid columns 80px auto 80px
- background #FFFFFF with alpha, backdrop-filter blur(45px), radius .5rem
- center logo uses Ndot-Regular, 1.25rem, weight 55, uppercase
- side icon buttons are 48px square tap targets
```

### Iteration Guide

- **색상 변경 시**: #F4F4F4 page floor and #FFFFFF frosted surface must stay separate.
- **폰트 변경 시**: preserve the three-role split: `Ndot` for brand/product, `NType82` for headline/body, `LatteraMonoLL` for controls.
- **여백 조정 시**: keep the product scene huge and the controls compact. Do not inflate chips into normal SaaS buttons.
- **새 컴포넌트 추가 시**: start with frosted glass, `.5rem` radius, tiny uppercase control copy, and minimal border.
- **다크 모드**: use `frost-grey-intense` logic; do not simply invert the whole page.
- **반응형**: maintain 3-column mobile and 12-column desktop product grid math if the component depends on scene choreography.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `Ndot-Regular` for the brand/product identity moments.
- Keep the page floor at #F4F4F4 and use #FFFFFF for frosted surfaces.
- Use `backdrop-filter: blur(45px)` on nav/product control surfaces.
- Keep radius tight at `.5rem`; Nothing's UI is compact hardware glass, not soft lifestyle bubbles.
- Use `min-h-svh` product scenes and bottom-centered overlay cards.
- Keep CTA language short: "Discover", "Support", "Newsletter".
- Let photography and product hardware carry visual weight instead of decorative color blocks.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로만 두지 말 것 — 대신 page floor는 `#F4F4F4`, floating glass는 `#FFFFFF`로 분리.
- 텍스트를 `#000000` 또는 `black` 중심으로 두지 말 것 — 대신 `hsl(180 1% 35%)` 계열의 cool grey text를 사용.
- 브랜드를 `#002F6C` 전체 배경/CTA 시스템으로 확장하지 말 것 — #002F6C는 낮은 빈도의 accent로 제한.
- 회색 중간값을 임의 neutral로 대체하지 말 것 — 실제 cool-neutral 단서는 `#B1B3B3`, `#B3B3B3`, `#E5E7EB`, `#999999`.
- 카드 배경을 불투명 `#FFFFFF` 블록으로만 만들지 말 것 — `#FFFFFF` alpha + `backdrop-filter: blur(45px)`가 핵심.
- body/display에 `font-weight: 600`을 기본값으로 쓰지 말 것 — headline은 weight `100`, dot identity는 weight `55`.
- CTA를 48px high pill primary button으로 만들지 말 것 — Discover는 tiny uppercase chip이다.
- 제품 이미지를 카드 안의 평범한 썸네일로 축소하지 말 것 — full-screen scene + small control surface 대비를 유지.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- No second saturated brand color as a UI system. Accent red/yellow/blue exist, but the homepage identity is near-monochrome.
- No large gradient mesh background. The source evidence is product photography, glass, and neutral fields.
- No heavy display weight. Weight 800/900 is absent from the observed hierarchy.
- No decorative rounded mega-cards. Radius stays around `.5rem` for primary surfaces.
- No universal hard borders around cards. Separation comes from blur, alpha, and photography.
- No generic 3-feature SaaS card grid as the main structure. Product scenes use viewport chapters.
- No emoji or illustrative filler. Product assets and dot icons carry the playful tone.
- No text-heavy editorial prose blocks in the hero. Headlines are short and product-led.
- No warm beige lifestyle palette. Neutrals are cool industrial greys and clean white glass.
- Showroom velvet rope or luxury display pedestal: absent. The product sits on a measuring grid, not on a stage.
- Catalog-style 3-up product grid hero: never. One scene equals one specimen.
- Curator's wall-text manifesto over photography: zero. Captions stay tiny firmware labels.
- Gallery accent color ribbon / exhibition red: none. The room is monochrome glass.
- Decorative spotlight gradient on the display case: absent. Light is replaced by 45px frost.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual / REQUIRED -->

- **Cookie-modal screenshot limitation** — the available `hero-cropped.png` is covered by the consent modal, so visual interpretation relies more heavily on HTML/CSS structure and product image URLs than the rendered hero screenshot.
- **Single-page homepage scope** — analysis reused the existing homepage capture only. Checkout, cart, support, account, and product-detail sub-flows were not visited.
- **Dark mode incomplete** — `dark:frost-grey-intense` and `dark:text-pure-white` classes are present, but a full dark-mode palette state was not rendered.
- **Motion logic partially observed** — CSS shows `transition: transform 0.4s ease` and aside `.2s ease-in-out`; scroll choreography or JS-driven opacity changes were not deeply traced.
- **Form states not surfaced** — inputs, validation, loading, and error states are not part of the captured homepage evidence.
- **Color role inference** — #002F6C is treated as the best chromatic accent because it appears in CSS, but the brand's real homepage identity is monochrome/product-led rather than blue-led.
- **Font licensing** — `NType82`, `Ndot`, and `LatteraMonoLL` are assumed proprietary/brand fonts from CSS names; exact license terms were not verified.
- **Token namespace** — `nothing` token prefix is an authoring prefix for this guidebook. The source CSS itself mostly uses Tailwind variables and custom `--grey-*` / `--accent-*` tokens.
