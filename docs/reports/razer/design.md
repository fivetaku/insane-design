---
schema_version: 3.2
slug: razer
service_name: Razer
site_url: https://www.razer.com
fetched_at: 2026-04-14T01:14:00+09:00
default_theme: dark
brand_color: "#44D62C"
primary_font: RazerF5
font_weight_normal: 400
token_prefix: cx

bold_direction: Neon Hardware
aesthetic_category: retro-futuristic
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: editorial-product
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "CSS 변수 1123개, resolved token 842개, cx token layer와 반복 컴포넌트 CSS가 실제 페이지에서 사용됨"

colors:
  primary: "#44D62C"
  primary-dark: "#008900"
  surface-black: "#000000"
  surface-panel: "#303030"
  text-primary: "#FFFFFF"
  text-secondary: "#EEEEEE"
  text-muted: "#999999"
  danger: "#F44336"
  info: "#28AADC"
  focus-ring: "#44D62C40"

typography:
  display: "RazerF5"
  body: "RazerF5"
  fallback: "Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif"
  ladder:
    - { token: hero-title, size: "56px approx", weight: 700, tracking: "0 to 0.4px" }
    - { token: section-title, size: "24px", weight: 700, tracking: "0" }
    - { token: nav-link, size: "16px", weight: 400, tracking: "0" }
    - { token: body, size: "14px", weight: 400, tracking: "0" }
    - { token: microcopy, size: "12px", weight: 400, tracking: "0.2px" }
  weights_used: [100, 300, 400, 500, 600, 700, 900]
  weights_absent: []

components:
  button-primary: { bg: "{colors.primary}", color: "#000000", radius: "0 to 5px", padding: "12px 16px" }
  nav-link: { color: "#999999", active: "#FFFFFF", size: "16px", weight: 400 }
  cookie-panel: { bg: "#303030", color: "#FFFFFF", radius: "5px", shadow: "soft modal elevation" }
  focus-ring-green: { shadow: "0 0 0 .2rem #44D62C40" }
---

# DESIGN.md - Razer (Designer Guidebook)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Razer stages each product like a midnight hardware showroom: a black canvas where `#44D62C` (`{colors.primary}`) cuts across navigation, CTAs, focus rings, and brand moments like a hardware status LED. The green is not decorative. It behaves as the system's power indicator.

The hero language is built like a gaming peripheral shot: dark field, product mass, metallic gray highlights, and uppercase display type. The background disappears into `#000000` (`{colors.surface-black}`) so the product silhouette can do the dimensional work. It is a black-box product store where the lights are killed, the glass shelf vanishes, and only the edge-lit equipment remains. Razer does not soften the page with warm neutrals or lifestyle beige; it wants equipment, voltage, speed, and black glass.

Typography is blunt and compressed by attitude rather than by extreme optical math. `RazerF5` carries the brand voice, with most utility UI sitting at 14-16px and weight 400, then jumping hard to 700 for headings and conversion copy. The site does not chase airy editorial refinement. It uses a merchandised gaming cadence: category nav, product hero, short hype line, two-link CTA. The copy behaves like labels on an equipment rack: short, bright, functional, and close to the object it activates.

The component system is sharper than the neon suggests. Radius is usually small (`0`, `3px`, `4px`, `5px`) with occasional circular/icon exceptions. Shadows are mostly functional focus rings and overlays, not card elevation. There is no second brand color waiting in the wings: `#28AADC`, `#F44336`, and `#FFC107` are system accents, while `{colors.primary}` owns the brand voltage alone.

The dominant visual craft is contrast: black surfaces, gray product photography, and green interaction states. Razer's chrome tries to stay flat so photography can become the metal. The nav line, link color, button fill, and focus halo all feel like one circuit trace running across the chassis; when the user tabs through a control, the interface does not politely outline it, it powers it on.

### Key Characteristics

- Near-black page atmosphere anchored by `#000000`, `#111`, and `#222` surfaces.
- Single high-voltage brand accent: `#44D62C` is the top chromatic color in CSS frequency.
- Product photography/video carries depth; UI chrome stays comparatively flat.
- Header uses dark horizontal mega-menu structure with gray inactive links and white active links.
- CTA styling favors green fills, black text, compact padding, and minimal radius.
- Focus and active states use neon green rings such as `0 0 0 .2rem #44D62C40`.
- Typography is brand-face first: `RazerF5` over generic system fonts where the marketing shell matters.
- Color hierarchy is severe: green for action, white for primary text, gray for everything else.
- Component corners are restrained, mostly 0-5px, not soft SaaS pills.
- The site is product-stage commerce: editorial hero first, category navigation immediately available.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Neon Hardware
> **Aesthetic Category**: retro-futuristic
> **Signature Element**: 이 사이트는 **black hardware stage with a neon-green power trace**으로 기억된다.
> **Code Complexity**: high — Angular/SSR markup, dense responsive CSS, mega-menu CSS, focus rings, modal overlays, and product-media hero layers require more than static token copying.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Razer처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "RazerF5", "Roboto", "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #000000;
  --fg: #FFFFFF;
  --muted: #999999;
}
body {
  background: var(--bg);
  color: var(--fg);
}

/* 3. 브랜드 컬러 */
:root { --brand: #44D62C; }
.cta-primary {
  background: var(--brand);
  color: #000000;
  border-radius: 5px;
  font-weight: 700;
}
```

**절대 하지 말아야 할 것 하나**: Razer를 "초록색 SaaS"로 만들지 말 것. 배경을 `#FFFFFF` 중심으로 열거나 둥근 카드/부드러운 gradient를 깔면 Razer의 hardware-stage tension이 사라진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.razer.com` |
| Fetched | 2026-04-14T01:14:00+09:00 |
| Extractor | cached phase1 reuse from `insane-design/razer/` |
| HTML size | 1,294,504 bytes |
| CSS files | 9 files, approx 4,066,339 chars |
| Token prefix | `cx` |
| Phase1 JSON | `brand_candidates.json`, `resolved_tokens.json`, `typography.json` |
| Screenshot | `insane-design/razer/screenshots/hero-cropped.png` |
| Method | CSS custom properties + CSS frequency + screenshot interpretation; no live refetch in this v3.2 pass |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Angular/SSR-style rendered commerce shell. Evidence: repeated `_ngcontent-*` attributes and large hydrated HTML.
- **Design system**: Razer commerce token layer using `--cx-*` plus Angular Material form tokens and product/menu CSS.
- **CSS architecture**:
  ```text
  core      (--cx-color-*, --cx-font-*)       semantic system variables
  utility   (.razer-mega-menu, layout CSS)    site-level chrome
  component (buttons, modals, forms)          repeated commerce UI
  vendor    (--mat-*, FontAwesome, icons)     framework support layer
  ```
- **Class naming**: mixed component selectors and Angular-scoped selectors, including `.razer-mega-menu` and generated `_ngcontent-*`.
- **Default theme**: dark. The screenshot and CSS frequency both center on `#000`, `#111`, `#222`, and `#303030`.
- **Font loading**: custom brand font `RazerF5` appears in CSS; fallbacks include Roboto, Helvetica Neue, Arial, Noto Sans.
- **Canonical anchor**: black global navigation with green top/bottom brand line and green interaction states.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `RazerF5` (brand font; assume proprietary unless bundled by site CSS)
- **Body font**: `RazerF5`, with Roboto and common sans fallbacks in utility/vendor layers
- **Code font**: N/A for the public storefront
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --cx-font-family: "RazerF5", "Roboto", "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  --cx-font-family-code: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --cx-font-weight-normal: 400;
  --cx-font-weight-semi: 600;
  --cx-font-weight-bold: 700;
}

body {
  font-family: var(--cx-font-family);
  font-weight: var(--cx-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **RazerF5** is the voice. If unavailable, use **Roboto Condensed** for headline-like display blocks and **Roboto** for navigation/body, not Inter. Inter makes the page feel like a SaaS dashboard.
- Keep body at `400`, section titles at `700`, and avoid making nav links heavy. The header works because inactive links are gray and regular, not because they are bold.
- Use tracking sparingly. CSS evidence shows many `0` / `0px` letter-spacing declarations, with occasional `0.2px` or `0.4px` compensation. Do not apply blanket negative tracking.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| hero-title | approx 56px | 700 | 1.0-1.2 | 0 to 0.4px |
| section-title | 24px | 700 | 32px | 0 |
| product-title | 21px | 700 | 24px | 0 |
| nav-link | 16px | 400 | 21px | 0 |
| body | 14px / .875rem | 400 | 20px / 1.5 | 0 |
| microcopy | 12px / .75rem | 400 | 16px | 0.2px |

> ⚠️ Key insight: Razer is not a delicate typography system. It is a contrast system: regular gray utility text, then hard uppercase-ish display and green CTA emphasis.

### Principles
<!-- SOURCE: manual -->

1. Body defaults to `14px` / `.875rem` often enough that 16px-only body copy will feel too roomy.
2. Navigation is regular weight `400`; active hierarchy comes from color (`#FFFFFF` over `#999999`) more than weight.
3. Display blocks jump to `700` quickly. Use bold for product naming and hero claims, not for every UI label.
4. Letter-spacing mostly stays neutral. Add `0.2px` / `0.4px` for small optical tightening, not broad negative tracking.
5. The font substitute must preserve the angular gaming voice. Generic Inter makes the same colors read like developer tooling.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed)

| Token | Hex |
|---|---|
| `{colors.primary}` | `#44D62C` |
| `{colors.primary-dark}` | `#008900` |
| focus translucent | `#44D62C40` |
| focus stronger | `#44D62C80` |

### 06-2. Brand Dark Variant

> N/A - Razer's primary brand color is already used on dark surfaces. The variation is opacity/ring treatment, not a separate dark-mode ramp.

### 06-3. Neutral Ramp

| Step | Dark surface / text role | Hex |
|---|---|---|
| black-stage | page and hero floor | `#000000` |
| dark-panel | modal/panel support | `#303030` |
| inverse-text | primary foreground | `#FFFFFF` |
| secondary-text | link/body secondary | `#EEEEEE` |
| muted-text | inactive nav / support copy | `#999999` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| danger/error | form/system error | `#F44336` |
| info | utility/info accent | `#28AADC` |
| blue support | secondary system accent | `#6D9DF7` |
| warning | system warning | `#FFC107` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--cx-color-primary` | `#44D62C` | primary action / brand |
| `--cx-color-primary-accent` | `#44D62C` | accent alias for same green |
| `--cx-color-background` | `#000000` / dark aliases | page and dark UI contexts |
| `--cx-color-text` | `#FFFFFF` / light text aliases | primary foreground |
| danger semantic | `#F44336` | validation/error |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--cx-color-primary` | `#44D62C` | CTA, links, focus accents |
| `--cx-color-primary-accent` | `#44D62C` | same brand green in accent contexts |
| `--cx-color-inverse` | inverse surface/text token | component state contrast |
| `--mat-*` color aliases | Material form state tokens | vendor form controls |

### 06-7. Dominant Colors (actual CSS frequency)

| Token | Hex | Frequency |
|---|---:|---:|
| brand green | `#44D62C` | 439 in phase1 candidates / 437 CSS count |
| white foreground | `#FFFFFF` | 385 normalized candidates |
| muted gray | `#999999` | 150 normalized candidates |
| dark surface | `#000000` / `#111` / `#222` | dominant background family |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.primary}` (`#44D62C`)** - The voltage line. It is used for brand identity, links, CTA fills, focus rings, and interactive accents. Do not introduce a second chromatic brand color; this green must stay lonely and loud.

**`{colors.surface-black}` (`#000000`)** - The product stage. Razer's page uses black not as "dark mode" but as a showroom condition where hardware can glow. White or light-gray pages break the theatrical contrast.

**`{colors.text-primary}` (`#FFFFFF`)** - Primary copy on black. It is reserved for active, important, or headline text; inactive navigation and secondary copy step down to grays.

**`{colors.focus-ring}` (`#44D62C40`)** - The accessibility version of the brand. The ring makes focus feel like an energy field around the component, not a generic blue browser outline.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| tight-inline | 2px / 5px | small controls and menu details |
| control-x | 8px / 16px | compact buttons, utility blocks |
| panel-padding | 12px 16px / 16px | modals and card-like containers |
| section-small | 24px | product/module internal space |
| container | 90% / 100% / 1200px | responsive page width |

**주요 alias**:
- `--cx-page-width-max` -> container max-width token used by the commerce layout.

### Whitespace Philosophy
<!-- SOURCE: manual -->

Razer does not use whitespace as luxury breathing room. It uses empty black as stage depth. The hero can feel vast because the product shot sits in darkness, but the commerce shell itself is compact: nav links at 16px, body UI at 14px, dense menu categories, and strong top-level navigation.

The correct rhythm is "open black hero, compressed equipment catalog below." Do not translate the black into extra padding everywhere. Keep the UI chassis tight, and let media panels create the large moments.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| square | `0` | hard-edge product/commercial panels |
| micro | `3px` / `4px` | small controls, chips, framework elements |
| default-control | `5px` | buttons, cookie modal controls |
| soft | `10px` / `1rem` | occasional modal/card support |
| circular | `50%` | icon buttons, round affordances |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none | `none` | default chrome, cards, nav |
| green-focus | `0 0 0 .2rem #44D62C40` | focus ring / active field |
| green-focus-strong | `0 0 0 .2rem #44D62C80` | stronger focus/selected state |
| modal-soft | overlay shadow around dark cookie panel | blocking dialogs |
| thin-outline | `0 0 0 1px #44D62C` | accent outline state |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| transition-common | observed `transition` rules in CSS | hover/focus state changes |
| reduced-motion | `@media (prefers-reduced-motion: reduce)` present | accessibility fallback |
| hero-media | likely image/video media swap | product hero treatment; exact JS not inspected |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `1200px` and tokenized `--cx-page-width-max` patterns; several responsive max-width rules.
- **Grid type**: mixed flex/grid commerce layout, plus Angular component structure.
- **Column count**: product/category grids collapse around Bootstrap-like breakpoints.
- **Gutter**: compact utility gaps, commonly `16px` / `24px` ranges.

### Hero
- **Pattern Summary**: full-width dark product stage + centered title stack + dual CTA + product media below.
- Layout: single-column centered text over dark product media.
- Background: black/dark product photography or video.
- **Background Treatment**: image/video overlay on `#000000`; product surfaces supply gray highlights.
- H1: approx `56px` / weight `700` / tracking neutral to slight positive.
- Max-width: text stack centered; media spans wide viewport.

### Section Rhythm

```css
section {
  padding: 24px 16px;
  max-width: 1200px;
}
```

Use this as an implementation approximation. The real site has many component-specific sections, so this is a compositional guide rather than a single global rule.

### Card Patterns
- **Card background**: dark surface family, often `#000000`, `#111`, `#222`, or media-backed.
- **Card border**: minimal; borders appear more in controls/modals than product cards.
- **Card radius**: mostly small (`0` to `5px`), with occasional `10px`.
- **Card padding**: compact `12px 16px` / `16px` ranges.
- **Card shadow**: usually none; product media and black contrast create depth.

### Navigation Structure
- **Type**: horizontal global navigation + mega-menu.
- **Position**: top global header.
- **Height**: approx 60px header band in screenshot.
- **Background**: `#000000`.
- **Border**: green horizontal accent line; inactive links `#999999`, active `#FFFFFF`.

### Content Width
- **Prose max-width**: narrow centered hero copy.
- **Container max-width**: `1200px` common.
- **Sidebar width**: N/A on homepage hero; mega-menu dropdown is the main navigation expansion pattern.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `max-width: 575.98px` / `767.98px` | dense mobile collapse and single-column product sections |
| Tablet | `min-width: 768px` | larger grid and menu layouts start |
| Desktop | `min-width: 992px` / `1200px` | full nav and larger product modules |
| Large | `min-width: 1367px` / `1400px` | wide-screen refinements |

### Touch Targets
- **Minimum tap size**: inferred target should stay at least 44px for header icons and CTAs.
- **Button height (mobile)**: use 44-48px implementation target; exact mobile runtime not inspected.
- **Input height (mobile)**: Material form tokens imply framework-managed control heights; exact forms not visited.

### Collapsing Strategy
- **Navigation**: horizontal desktop nav likely collapses into icon/menu treatment on small screens.
- **Grid columns**: Bootstrap-like breakpoints collapse from multi-column to single-column under `767.98px`.
- **Sidebar**: no persistent sidebar on homepage.
- **Hero layout**: centered text remains; media crops/reflows by viewport.

### Image Behavior
- **Strategy**: product imagery/video owns the hero; use responsive `object-fit: cover` style behavior.
- **Max-width**: `100%`.
- **Aspect ratio handling**: preserve product silhouette; crop darkness before cropping hardware.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA**

```html
<a class="rz-button rz-button--primary" href="#">Buy</a>
```

| Property | Value |
|---|---|
| background | `#44D62C` |
| color | `#000000` |
| font | `RazerF5`, 14-16px, weight 700 |
| radius | `5px` or small radius token |
| padding | `12px 16px` approximation |
| hover/focus | green ring or intensified green state |

**Secondary CTA**

```html
<a class="rz-link rz-link--green" href="#">Learn More ></a>
```

| Property | Value |
|---|---|
| color | `#44D62C` |
| background | transparent |
| font | `RazerF5`, 16px, weight 400-700 depending context |
| decoration | minimal; arrow/chevron text common |

### Badges

Razer homepage evidence does not require a badge-heavy system. If needed, use compact rectangular badges, not rounded SaaS pills.

| Property | Value |
|---|---|
| background | `#222` or `#303030` |
| color | `#EEEEEE` |
| accent | `#44D62C` only for selected/highlight |
| radius | `3px` / `4px` |

### Cards & Containers

```html
<article class="rz-product-panel">
  <img src="product.jpg" alt="">
  <h3>Razer Blade</h3>
  <a>Learn More ></a>
</article>
```

| Property | Value |
|---|---|
| background | media-backed dark surface |
| border | none or very subtle dark divider |
| radius | `0` to `5px` |
| padding | compact inner text stack |
| shadow | none; product image contrast supplies depth |
| hover | color transition on CTA/link rather than card lift |

### Navigation

```html
<nav class="razer-mega-menu">
  <a>Store</a>
  <a>PC</a>
  <a>Console</a>
  <a>Mobile</a>
</nav>
```

| Property | Value |
|---|---|
| background | `#000000` |
| inactive link | `#999999`, 16px, weight 400 |
| active link | `#FFFFFF` |
| accent | thin `#44D62C` line |
| icons | search/cart as outline utility icons |

### Inputs & Forms

Razer inherits a substantial Angular Material form layer. Keep forms dark and ring-focused.

| State | Spec |
|---|---|
| default | dark surface, light text, subtle border |
| focus | `0 0 0 .2rem #44D62C40` |
| error | `#F44336` |
| disabled | gray text on dark surface |
| loading | no distinctive evidence in homepage capture |

### Hero Section

```html
<section class="rz-hero">
  <h1>RAZER ATLAS PRO</h1>
  <p>SKATING ON THIN GLASS</p>
  <p><a>Learn More ></a><a>Buy ></a></p>
</section>
```

| Property | Value |
|---|---|
| background | black product media |
| title | large uppercase, `RazerF5`, weight 700 |
| subtitle | gray, uppercase, lighter weight |
| CTA | green text links or green fill buttons depending module |
| media | product image below/behind title stack |

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-primary-green** - `#44D62C` fill, black text, compact rectangular radius. Use for purchase/accept/confirm actions.

**button-outline-dark** - transparent or `#303030` surface, `#FFFFFF` text, gray border. Seen in modal/action contexts such as cookie customization/reject.

**nav-link-muted** - `#999999` inactive header link, 16px, weight 400, no pill background.

**nav-link-active** - `#FFFFFF` active header link; state is color, not a bulky underline tab.

**focus-ring-green** - `0 0 0 .2rem #44D62C40` around controls; use instead of default browser blue.

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
neon-focus-ring:
  description: "Brand-color accessibility state that keeps the Razer voltage identity even in forms."
  technique: "box-shadow: 0 0 0 .2rem #44D62C40; stronger selected/focus variant uses #44D62C80."
  applied_to: ["{components.focus-ring-green}", "form controls", "buttons", "selected states"]
  visual_signature: "Focus feels energized like a powered device edge, not like a generic browser outline."

black-product-stage:
  description: "Hero and product panels let the page disappear so hardware geometry emerges from darkness."
  technique: "background/surface #000000 with dark product imagery or video, centered title stack, gray hardware highlights, no decorative gradient blobs."
  applied_to: ["{components.hero-section}", "{components.product-panel}"]
  visual_signature: "Midnight hardware-showroom atmosphere where product silhouette creates the depth."

green-circuit-nav-line:
  description: "The global header uses a thin green trace to bind category navigation to the brand power color."
  technique: "navigation background #000000, inactive links #999999 at 16px/400, active links #FFFFFF, thin #44D62C horizontal accent line."
  applied_to: ["{components.nav-link}", "{components.navigation}", ".razer-mega-menu"]
  visual_signature: "A flat black equipment rail with one neon circuit trace running through it."

single-accent-power-vocabulary:
  description: "One chromatic color owns brand interaction while every other color stays neutral or semantic."
  technique: "#44D62C for CTA fills, links, focus rings, and border accents; #28AADC/#F44336/#FFC107 reserved for system roles only."
  applied_to: ["{components.button-primary}", "{components.nav-link}", "{components.focus-ring-green}"]
  visual_signature: "Every clickable brand moment feels connected to the same electrical system; no second brand color competes."

hardware-catalog-square-radius:
  description: "Commerce controls stay near-square (0–5px) so the equipment chassis reads as machined hardware, not as soft consumer-app SaaS."
  technique: "border-radius: 0 for product/commercial panels, 3–4px for chips/framework, 5px default-control on buttons and cookie modal controls; soft 10px/1rem only on rare modal/card support; circular 50% reserved for icon buttons. Never apply pill (9999px) to hardware catalog rows."
  applied_to: ["{components.button-primary}", "{components.product-panel}", "{components.nav-link}", "spec/configurator chips"]
  visual_signature: "Catalog rows feel like rack-mounted equipment with hard edges and tiny corner reliefs; the only round shape is a power icon, never a button."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | product name, uppercase or title-case, short and hardware-forward | "RAZER ATLAS PRO" |
| Subheadline | sharp performance phrase | "SKATING ON THIN GLASS" |
| CTA | direct commercial verbs | "Learn More >", "Buy >" |
| Navigation | category-first commerce taxonomy | Store, PC, Console, Mobile |
| Tone | gamer-performance retail, not friendly SaaS | "For Gamers. By Gamers." |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Razer - copy into your root stylesheet */
:root {
  /* Fonts */
  --rz-font-family: "RazerF5", "Roboto", "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  --rz-font-family-code: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --rz-font-weight-normal: 400;
  --rz-font-weight-bold: 700;

  /* Brand */
  --rz-color-brand-25:  #44D62C40;
  --rz-color-brand-300: #44D62C80;
  --rz-color-brand-500: #44D62C;
  --rz-color-brand-600: #44D62C;
  --rz-color-brand-900: #008900;

  /* Surfaces */
  --rz-bg-page:    #000000;
  --rz-bg-panel:   #303030;
  --rz-text:       #FFFFFF;
  --rz-text-soft:  #EEEEEE;
  --rz-text-muted: #999999;

  /* System accents */
  --rz-danger: #F44336;
  --rz-info:   #28AADC;

  /* Key spacing */
  --rz-space-xs: 5px;
  --rz-space-sm: 8px;
  --rz-space-md: 16px;
  --rz-space-lg: 24px;

  /* Radius */
  --rz-radius-none: 0;
  --rz-radius-sm: 3px;
  --rz-radius-md: 5px;
}

body {
  background: var(--rz-bg-page);
  color: var(--rz-text);
  font-family: var(--rz-font-family);
  font-weight: var(--rz-font-weight-normal);
}

.rz-nav {
  background: #000000;
  border-bottom: 1px solid #44D62C;
}

.rz-nav a {
  color: #999999;
  font-size: 16px;
  font-weight: 400;
}

.rz-nav a[aria-current="page"],
.rz-nav a:hover {
  color: #FFFFFF;
}

.rz-button-primary {
  background: #44D62C;
  color: #000000;
  border: 0;
  border-radius: 5px;
  padding: 12px 16px;
  font-weight: 700;
}

.rz-button-primary:focus-visible {
  outline: 0;
  box-shadow: 0 0 0 .2rem #44D62C40;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `{colors.primary}` | `#44D62C` |
| Background | `{colors.surface-black}` | `#000000` |
| Panel | `{colors.surface-panel}` | `#303030` |
| Text primary | `{colors.text-primary}` | `#FFFFFF` |
| Text muted | `{colors.text-muted}` | `#999999` |
| Danger | `{colors.danger}` | `#F44336` |
| Info | `{colors.info}` | `#28AADC` |

### Example Component Prompts

#### Hero Section

```text
Razer style hero section:
- Background: #000000 with dark product photography/video, product silhouette visible.
- H1: RazerF5, approx 56px, weight 700, uppercase product naming.
- Subtitle: #999999 or #EEEEEE, 24px, weight 300-400, short performance phrase.
- CTAs: green text links or #44D62C filled button with #000000 text.
- Layout: centered stack over black product-stage media, no decorative gradient blobs.
```

#### Product Card

```text
Build a Razer product panel:
- Background: #000000 or media-backed dark panel.
- Text: #FFFFFF title, #999999 support copy.
- Link: #44D62C with chevron/arrow text.
- Radius: 0-5px, no soft SaaS card shell.
- Shadow: none; use product image contrast for depth.
```

#### Modal / Cookie Panel

```text
Build a Razer dark modal:
- Panel background: #303030, text #FFFFFF.
- Buttons: primary #44D62C with #000000 text; secondary outline with #FFFFFF text.
- Radius: 5px.
- Focus ring: 0 0 0 .2rem #44D62C40.
```

#### Navigation

```text
Build Razer global navigation:
- Height about 60px, background #000000, thin #44D62C accent line.
- Links: RazerF5, 16px, weight 400, inactive #999999, active #FFFFFF.
- Category labels: Store, PC, Console, Mobile style taxonomy.
- Icons: search/cart as thin outline utilities.
```

### Iteration Guide

- **색상 변경 시**: `#44D62C`를 다른 green으로 "개선"하지 말 것. 이 색이 브랜드 기억점이다.
- **폰트 변경 시**: Inter 단독 금지. RazerF5가 없으면 Roboto Condensed + Roboto 조합으로 angular voice를 보존한다.
- **여백 조정 시**: hero는 크게 열어도 UI chrome은 compact하게 유지한다.
- **새 컴포넌트 추가 시**: radius 0-5px, dark surface, green focus ring을 우선 적용한다.
- **다크 모드**: light/dark toggle처럼 생각하지 말 것. Razer의 기본 상태가 dark product stage다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- `#44D62C`를 primary CTA, link, focus, selected state의 단일 chromatic anchor로 사용한다.
- 배경은 `#000000` 중심으로 시작하고, `#303030` 같은 panel gray는 보조 표면에만 쓴다.
- navigation은 compact horizontal category bar로 유지한다.
- product imagery/video가 depth를 만들게 하고, UI chrome에는 shadow를 남발하지 않는다.
- `RazerF5` 또는 angular condensed substitute를 써서 gaming hardware voice를 유지한다.
- focus-visible state에는 green ring을 명시해 접근성과 brand memory를 동시에 잡는다.
- hero copy는 짧고 제품명 중심으로 쓴다.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#000000` 사용.
- primary CTA를 `#28AADC` 또는 generic blue로 두지 말 것 — 대신 `#44D62C` 사용.
- 본문/제목 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — dark surface 위 `#FFFFFF` 사용.
- muted navigation을 `#EEEEEE`로 너무 밝게 두지 말 것 — inactive links는 `#999999` 계열로 낮춘다.
- error/action warning을 brand green으로 처리하지 말 것 — error는 `#F44336`처럼 분리한다.
- body를 `font-weight: 300` 중심으로 만들지 말 것 — 기본 UI는 `400`, 강한 제품명은 `700`.
- CTA와 cards를 16px 이상의 soft rounded SaaS shape로 만들지 말 것 — Razer는 `0`-`5px`의 작은 radius가 맞다.
- hero에 pastel gradient나 purple-blue AI gradient를 깔지 말 것 — black product-stage가 핵심이다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- **Second brand color: absent.** `#44D62C` alone carries the chromatic identity.
- **Warm neutral palette: none.** No cream, beige, sand, or editorial warmth should enter the system.
- **Soft SaaS cards: absent.** Rounded 16px cards with low-contrast borders are the wrong chassis.
- **Decorative gradient blobs: zero.** Dark product media replaces abstract decoration.
- **Light default theme: never for the main storefront memory.** White surfaces are not the brand's first read.
- **Heavy chrome shadows: rare.** Shadow is mostly focus/modal support, not card elevation language.
- **Friendly illustration tone: absent.** Use real product/hardware imagery instead of playful SVG scenes.
- **Rainbow accent palette: absent.** System colors exist for errors/info, but brand expression remains green-on-black.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Cached phase1 reuse** — This v3.2 pass reused `insane-design/razer/` captures from 2026-04-14 rather than live-refetching `https://www.razer.com`.
- **Cookie modal occlusion** — The available hero screenshot includes a privacy modal over the center of the hero, so some hero spacing and CTA placement are inferred from visible surroundings plus HTML/CSS.
- **Homepage-only scope** — Product detail pages, checkout, account, configurator, and support flows were not navigated in this pass.
- **CSS exactness vs normalized hex** — Phase1 normalized some shorthand colors (`#fff`, `#999`, `#222`) to six-digit roles. This guide uses six-digit tokens for apply readability where exact CSS frequency supported the role.
- **Motion JS not inspected** — CSS transition and reduced-motion evidence exists, but scroll-trigger, carousel, and video behavior were not reverse-engineered from JavaScript.
- **Form states partial** — Angular Material tokens reveal form/focus/error systems, but real validation/loading states were not exercised.
- **Responsive behavior derived from CSS** — Breakpoints were extracted from CSS media queries; mobile screenshot verification was not repeated for this output file.
- **Brand font licensing unknown** — `RazerF5` is observed in CSS, but distribution/licensing details were not independently verified.
