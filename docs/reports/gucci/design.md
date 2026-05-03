---
schema_version: 3.2
slug: gucci
service_name: Gucci
site_url: https://www.gucci.com
fetched_at: 2026-05-03
default_theme: mixed
brand_color: "#000000"
primary_font: Gucci Sans Pro
font_weight_normal: 400
token_prefix: toastify

bold_direction: Monochrome Luxury
aesthetic_category: luxury-brand
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: luxury-brand
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Gucci uses a production design system and brand font in the captured page, but most reusable tokens are bundled in external Next.js and header CSS rather than exposed as a complete public token API."

colors:
  ink: "#000000"
  ivory: "#FFFFFF"
  near-black: "#121212"
  hairline: "#D8D8D8"
  muted-line: "#E2E2E2"
  disabled-text: "#757575"
  cookie-active: "#000000"
  legacy-consent-blue: "#3860BE"

typography:
  display: "Gucci Sans Pro"
  body: "Gucci Sans Pro"
  ladder:
    - { token: hero-label, size: "16px", weight: 400, tracking: "0" }
    - { token: nav-label, size: "12px", weight: 400, tracking: "0.08em" }
    - { token: cookie-title, size: "15px", weight: 700, tracking: "0.02em" }
    - { token: cookie-body, size: "13px", weight: 400, tracking: "0" }
    - { token: cta-label, size: "12px", weight: 700, tracking: "0.08em" }
  weights_used: [100, 300, 400, 500, 600, 700]
  weights_absent: [200, 800, 900]

components:
  hero-full-bleed: { bg: "image-overlay", height: "calc(var(--vh) * 100)", radius: "0", text: "{colors.ivory}" }
  header-transparent: { bg: "transparent", height: "72px", icon: "{colors.ivory}", position: "fixed" }
  cookie-primary-button: { bg: "{colors.ink}", fg: "{colors.ivory}", radius: "0", padding: "16px 32px" }
  cookie-text-button: { bg: "transparent", fg: "{colors.ink}", radius: "0", decoration: "underline" }
---

# DESIGN.md — Gucci

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Gucci's captured homepage behaves like a midnight fashion spread that has learned how to sell handbags without admitting it is a store. The first viewport is not a product grid, not a card stack, and not a marketing explanation. It is a black lacquer vitrine: a near-black monogram field, a model held in shadow, the `GUCCI` wordmark suspended at the top center, and commerce controls reduced to thin utility marks. The useful page is almost hidden behind atmosphere.

The palette is deliberately narrow. The active interface is `#000000` (`{colors.ink}`), `#FFFFFF` (`{colors.ivory}`), and a few quiet divider grays such as `#D8D8D8` (`{colors.hairline}`). There is no second brand color waiting to decorate the interface. Color only decides whether a surface is invisible, legally present, or sharp enough to click. Photography sells the brand; UI color behaves like the edge of a glass display case.

The cookie modal reveals the system with the lights turned on. It is not a soft ecommerce card; it is a white legal document placed over a dark editorial set. `#FFFFFF` (`{colors.ivory}`) becomes paper, `#000000` (`{colors.ink}`) becomes ink, and the zero-radius buttons feel stamped rather than cushioned. Gucci's luxury is not built with gold trim; it is built by making the required machinery look severe.

Typography is proprietary rather than ornamental. `Gucci Sans Pro` is the identity layer, with weights from 100 through 700 available, but the captured page keeps the voice small: uppercase navigation, compact consent copy, and button labels that gain authority through `0.08em` tracking rather than size. The wordmark is the chandelier; the surrounding UI text behaves like tiny gallery labels.

Whitespace is cinematic. The hero lets the image own the viewport and places product intent low in the frame: `Handbags` above a compact `SHOP NOW` CTA. The catalog is not absent; it is backstage. When `MENU` opens, the hidden density appears, but first paint is a controlled fashion-show pause: one photograph, one wordmark, a few tools, no visible warehouse.

The signature lesson is negative restraint. Gucci does not need a saturated accent, rounded comfort UI, friendly product cards, or gradient decoration. Shadow belongs to photography, not chrome. The page has almost no site-like self-consciousness; it clears the stage until the model, monogram darkness, and centered name carry the entire emotional load.

### Key Characteristics

- Full-bleed editorial photography is the dominant brand surface.
- `GUCCI` wordmark is centered and visually larger than utility navigation.
- Transparent fixed header floats over imagery with thin icon strokes.
- Monochrome UI grammar: `#000000`, `#FFFFFF`, and quiet gray hairlines.
- Square-edged buttons and modals; radius is intentionally absent from brand-facing controls.
- Proprietary `Gucci Sans Pro` carries identity across body, nav, and controls.
- Navigation density is hidden inside a drawer, not exposed as a grid on first paint.
- Product CTA is compact and low in the viewport, letting the image breathe.
- Cookie UI reveals the underlying system: hard rectangles, black action, underlined secondary text.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Monochrome Luxury
> **Aesthetic Category**: luxury-brand
> **Signature Element**: 이 사이트는 **shadowed full-bleed fashion photography with a floating centered wordmark**으로 기억된다.
> **Code Complexity**: high — Next.js, styled-components, external header bundles, consent overlays, responsive drawers, and image pipelines all participate in the visible page.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Gucci처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Gucci Sans Pro", "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #000000; --fg: #FFFFFF; --hairline: #D8D8D8; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #000000; }
.primary-action { background: #000000; color: #FFFFFF; border-radius: 0; }
```

**절대 하지 말아야 할 것 하나**: Gucci를 `#B9975B` 금색 럭셔리 키트로 만들지 말 것. 캡처된 UI의 브랜드 컬러는 장식용 금색이 아니라 사진 위의 흑백 절제다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.gucci.com` |
| Fetched | 2026-05-03 |
| Extractor | saved phase1 reuse, existing HTML/CSS/screenshot |
| HTML size | 1,784,723 bytes (Next.js SSR/hydrated storefront) |
| CSS files | 1 inline extraction, 153,230 bytes; HTML references 28 stylesheet links |
| Token prefix | `toastify` for exposed custom properties; Gucci system classes are mostly bundled CSS modules |
| Method | Existing phase1 JSON + saved HTML/CSS + hero screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js storefront. Evidence: `/_next/static/` assets, `_buildManifest.js`, `_ssgManifest.js`, and route chunks.
- **Design system**: Gucci production UI kit/header system. Evidence: header reports `data-react-ds-version="5.16.3"` and `data-ui-kit-version="5.8.2"`.
- **CSS architecture**: CSS Modules + styled-components + third-party consent/toast styles.
  ```text
  exposed vars   (--toastify-*)             toast/notification primitives
  CSS modules    (grbc_* / _nav-button_*)   header, drawer, navigation
  styled classes (FhHeroFullBleed-style__*) hero/editorial modules
  third-party    (#onetrust-*)              cookie consent surfaces
  ```
- **Class naming**: mixed hashed modules (`grbc_Header-module_*`), generated styled-components (`FhHeroFullBleed-style__*`), and vendor IDs (`#onetrust-pc-sdk`).
- **Default theme**: mixed. The hero/header layer is dark image-overlaid UI; consent and commerce control surfaces are white.
- **Font loading**: `@font-face` loads `Gucci Sans Pro` from `https://www.gucci.com/design-system-assets/_static/fonts/`.
- **Canonical anchor**: the homepage hero section `data-testid="FhHeroFullBleed"` with `aria-label="Handbags"`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Gucci Sans Pro` (proprietary brand font)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

```css
@font-face {
  font-family: "Gucci Sans Pro";
  font-weight: 100;
  src: url("https://www.gucci.com/design-system-assets/_static/fonts/GucciSansPro-Light.woff2") format("woff2");
}
@font-face {
  font-family: "Gucci Sans Pro";
  font-weight: 400;
  src: url("https://www.gucci.com/design-system-assets/_static/fonts/GucciSansPro-Book.woff2") format("woff2");
}
@font-face {
  font-family: "Gucci Sans Pro";
  font-weight: 500;
  src: url("https://www.gucci.com/design-system-assets/_static/fonts/GucciSansPro-Medium.woff2") format("woff2");
}
@font-face {
  font-family: "Gucci Sans Pro";
  font-weight: 700;
  src: url("https://www.gucci.com/design-system-assets/_static/fonts/GucciSansPro-Bold.woff2") format("woff2");
}
body {
  font-family: "Gucci Sans Pro", sans-serif;
}
```

### Note on Font Substitutes

- **Gucci Sans Pro** is proprietary and should not be substituted with a geometric SaaS font.
- Open-source fallback: **Manrope** at weights `300/400/500/700`, with uppercase button tracking around `0.08em`.
- System fallback: `"Helvetica Neue", Arial, sans-serif` only when brand fidelity is secondary.
- Compensation: keep UI labels smaller than typical ecommerce labels. If using Manrope, reduce line-height from `1.5` to `1.38` for modal copy so it does not become too friendly.
- Do not use Didot, Playfair Display, Cormorant, or decorative serif as a fake luxury shortcut; the captured Gucci interface is sans-led.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `hero-kicker` | ~16px | 400 | 1.3 | 0 |
| `nav-utility` | ~12px | 400 | 1.2 | 0.06-0.08em |
| `button-label` | ~12px | 700 | 1.2 | 0.08em |
| `cookie-title` | ~15px | 700 | 1.35 | 0.02em |
| `cookie-body` | ~13px | 400 | 1.45 | 0 |
| `drawer-heading` | ~20px | 300-400 | 1.3 | 0 |

> ⚠️ Typography data has no clean extracted scale object; the guide uses observed text sizes and the captured font-weight distribution from `typography.json`.

### Principles

1. Gucci's identity is in font ownership, not in oversized typography. The wordmark and photograph are louder than UI copy.
2. Uppercase labels need tracking. CTA and menu labels should feel engraved, not friendly.
3. Weight `400` is the normal body center; `700` is reserved for action/title emphasis, and `100/300` create the thin luxury layer.
4. Body copy can be compact because white modal surfaces and generous hero air prevent the page from feeling crowded.
5. Do not introduce a serif display face for "luxury." The captured page stays with `Gucci Sans Pro`.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| `colors.ink` | `#000000` |
| `colors.near-black` | `#121212` |
| `colors.ivory` | `#FFFFFF` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `hero-overlay-black` | `#000000` |
| `toastify-color-dark` | `#121212` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 | `#FFFFFF` | `#000000` |
| 1 | `#E2E2E2` | `#121212` |
| 2 | `#D8D8D8` | `#2E3644` |
| 3 | `#C7C5C7` | `#4D4D4D` |
| 4 | `#757575` | `#616161` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Consent legacy blue | focus/link utility | `#3860BE` |
| Consent legacy green | old OneTrust action | `#6CC04A` |
| Toast info | notification | `#3498DB` |
| Toast success | notification | `#07BC0C` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `action-primary` | `#000000` | Cookie accept, hard commerce action |
| `action-on-primary` | `#FFFFFF` | Text on black action |
| `surface-modal` | `#FFFFFF` | Cookie modal / white transactional plane |
| `text-primary` | `#000000` | Modal body and legal copy |
| `line-subtle` | `#D8D8D8` | Consent dividers and list boundaries |
| `image-chrome` | `#FFFFFF` | Header icons and logo over dark hero |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--toastify-color-light` | `#FFFFFF` | Toast light surface |
| `--toastify-color-dark` | `#121212` | Toast dark surface |
| `--toastify-text-color-light` | `#757575` | Toast light text |
| `--toastify-toast-background` | `#FFFFFF` | Toast default background |
| `cookie-primary` | `#000000` | Inferred OneTrust primary action |
| `cookie-secondary-surface` | `#FFFFFF` | Inferred OneTrust secondary action surface |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---|---|
| white shorthand | `#FFF` | 50 |
| black longhand | `#000000` | 23 |
| hairline gray | `#D8D8D8` | 20 |
| black shorthand | `#000` | 16 |
| consent blue | `#3860BE` | 11 |
| white longhand | `#FFFFFF` | 9 |
| muted line | `#E2E2E2` | 8 |
| cool gray | `#C7C5C7` | 6 |

### 06-8. Color Stories

**`{colors.ink}` (`#000000`)** — The real UI brand color in the captured interface. It is used for the cookie primary button, modal text, focus outlines, and the severe ecommerce control language. Use it as authority, not decoration.

**`{colors.ivory}` (`#FFFFFF`)** — The transactional surface. White appears when the site must explain, ask consent, or provide utility. Against the dark hero it feels like a document laid over a fashion photograph.

**`{colors.near-black}` (`#121212`)** — The shadow tone. It appears as the toast dark token and visually matches the hero's photographic blacks. Use it when pure black would flatten image-adjacent UI.

**`{colors.hairline}` (`#D8D8D8`)** — Structural gray. It is not a decorative accent; it separates legal, drawer, and consent content without competing with photography.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `header-base-height` | `72px` | Fixed transparent header base height |
| `toast-offset` | `16px` | Notification safe-area offset |
| `toast-padding` | `14px` | Toast internal padding |
| `toast-min-height` | `64px` | Toast touch/notice block |
| `cookie-button-padding` | ~`16px 32px` | Modal primary action |
| `drawer-section-gap` | `l` to `xxl` utility classes | Navigation grouping |

**주요 alias**:
- `--g-rbc-header-base-height` → `72px` (header reserved height)
- `--toastify-toast-offset` → `16px` (safe-area aware notification offset)

### Whitespace Philosophy

Gucci uses whitespace by hiding density until the user asks for it. The first viewport has a full commerce catalog behind the menu, but the visible surface contains only the wordmark, utility icons, the product label, and one CTA. That emptiness is not minimalism for its own sake; it protects the photograph's authority.

When a transactional surface appears, spacing becomes document-like rather than plush. The cookie modal uses a white rectangle, compact paragraphs, hard button spacing, and no rounded comfort layer. The contrast is the point: cinematic outside, legal inside.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| `brand-button-radius` | `0` | Cookie and square commerce controls |
| `cookie-modal-radius` | `0` observed visually | OneTrust consent dialog |
| `toast-radius` | `6px` | Third-party toast token, not primary brand chrome |
| `filter-toggle-radius` | `17px` | OneTrust filter utility, not Gucci brand surface |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `none` | `none` | Header, brand buttons, hero UI |
| `toast` | `0px 4px 12px rgba(0, 0, 0, .1)` | Toastify notifications |
| `photographic-depth` | image contrast, not CSS shadow | Hero image supplies depth |

Pattern: Gucci does not build luxury with UI elevation. The captured page avoids card shadows and lets the photograph carry all depth.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `toast-transition` | `.3s ease` | Close button opacity, stacked toast transform |
| `toast-animation` | `.5s` | Toast enter/exit presets |
| `hero-image-animation` | `animation="5"` attribute | Image component animation flag in captured hero |
| `drawer-transition` | not fully extracted | Header/menu drawer likely JS-controlled |

Motion should be slow enough to feel editorial. Avoid bouncy ecommerce microinteractions on the hero layer.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: full viewport for hero; modal content around 650px visual width.
- **Grid type**: full-bleed media frame plus hidden drawer/list navigation.
- **Column count**: first viewport is one-column overlay; menu drawer expands into nested multi-level lists.
- **Gutter**: hero has no visible container gutter; drawer/list surfaces use utility margins.

### Hero
- **Pattern Summary**: `100vh + full-bleed fashion image + centered wordmark/header + low centered CTA`
- Layout: single full-bleed image section with absolute media link and overlaid product call-to-action.
- Background: editorial photograph (`HP_Hero-FullBleed-Desktop_16x9_Gucci-HANDBAGS...png`).
- **Background Treatment**: image-overlay; dark photographic treatment with visible monogram texture and near-black edges.
- H1: logo is the dominant display object; product text is smaller (`Handbags`) and placed near the lower center.
- Max-width: viewport-wide media (`sizes="100vw"`, 16:9 responsive asset set).

### Section Rhythm

```css
.hero-single {
  min-height: calc(var(--vh) * 100);
  width: 100%;
}

.gucci-section {
  padding: 64px 24px;
}
```

### Card Patterns
- **Card background**: not used in first viewport; transactional panels use `#FFFFFF`.
- **Card border**: hairline only when legal/consent content needs separation.
- **Card radius**: `0` for brand-facing rectangles.
- **Card padding**: compact document spacing, not plush SaaS cards.
- **Card shadow**: none; do not introduce elevation.

### Navigation Structure
- **Type**: transparent fixed header plus drawer menu.
- **Position**: fixed/overlay header.
- **Height**: `72px` base.
- **Background**: transparent over hero image.
- **Border**: none on first paint; icon strokes carry affordance.

### Content Width
- **Prose max-width**: modal copy around 600-650px.
- **Container max-width**: hero is 100vw; drawer/menu content is controlled by component modules.
- **Sidebar width**: N/A for first viewport; drawer is the main expansion surface.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Small mobile | `max-width: 425px` | Consent and utility surfaces compress. |
| Mobile toast | `max-width: 480px` | Toast containers become full-width with radius removed. |
| Consent mobile | `max-width: 600px` | OneTrust panel becomes full-screen/stacked. |
| Tablet range | `426px-896px` | Header and consent landscape variants appear. |
| Desktop support | `min-width: 768px` | Label visibility and richer consent controls return. |

### Touch Targets
- **Minimum tap size**: inferred 44px+ for header icons and cookie buttons.
- **Button height (mobile)**: cookie/button surfaces visually around 48-52px.
- **Input height (mobile)**: OneTrust search/input rules force mobile `font-size: 1em`.

### Collapsing Strategy
- **Navigation**: visible desktop utilities collapse into menu/drawer hierarchy.
- **Grid columns**: hero stays full-bleed; content density moves into drawer levels.
- **Sidebar**: no persistent sidebar in captured viewport.
- **Hero layout**: image remains viewport-first; CTA remains centered low in frame.

### Image Behavior
- **Strategy**: responsive `srcset` from Gucci media CDN.
- **Max-width**: `100vw`.
- **Aspect ratio handling**: explicit `--aspectRatio: 16/9` and fill image behavior.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<button class="gucci-button gucci-button--primary">ACCEPT ALL COOKIES</button>
<button class="gucci-button gucci-button--text">COOKIES SETTINGS</button>
<a class="gucci-hero-cta" href="/us/en/ca/women/handbags-c-women-handbags">SHOP NOW</a>
```

| Part | Spec |
|---|---|
| Primary background | `#000000` |
| Primary text | `#FFFFFF`, uppercase, letter-spaced |
| Radius | `0` |
| Border | none or `1px solid #000000` |
| Hover | keep monochrome; do not introduce accent color |
| Secondary | transparent, black underlined text |

### Badges

> N/A — captured first viewport does not expose promotional badges. Do not invent sale pills or luxury tags.

### Cards & Containers

```html
<div class="gucci-document-panel">
  <h2>We Use Cookies</h2>
  <p>...</p>
</div>
```

| Part | Spec |
|---|---|
| Surface | `#FFFFFF` |
| Text | `#000000` |
| Radius | `0` |
| Shadow | none |
| Border | optional `1px solid #D8D8D8` only for internal dividers |

### Navigation

```html
<header class="gucci-header" data-transparent="true">
  <button>Contact Us</button>
  <span class="gucci-wordmark">GUCCI</span>
  <button aria-label="my shopping bag"></button>
  <button>MENU</button>
</header>
```

| Part | Spec |
|---|---|
| Position | fixed overlay |
| Height | `72px` |
| Background | transparent over image |
| Text/icon | `#FFFFFF` or light gray over dark hero |
| Wordmark | centered, spaced letters |
| Drawer | nested navigation levels with back buttons and category headings |

### Inputs & Forms

OneTrust consent forms and filters are the observed form-heavy surfaces. They use square buttons, black focus outlines, white backgrounds, and small legal text. Inputs should stay utilitarian; Gucci's brand moment is not in form styling.

### Hero Section

```html
<section class="hero-single" aria-label="Handbags">
  <picture class="hero-media">...</picture>
  <div class="hero-copy">
    <p>Handbags</p>
    <a>SHOP NOW</a>
  </div>
</section>
```

| Part | Spec |
|---|---|
| Media | full viewport editorial image |
| Overlay | dark photographic contrast, not CSS gradient spectacle |
| Copy | centered low in frame |
| CTA | compact square rectangle |
| Product text | small, quiet, not headline-scale |

### 13-2. Named Variants

- **hero-full-bleed** — Full viewport image module with absolute clickable media and low centered CTA.
- **header-transparent** — Fixed header over image with centered wordmark and thin utility icons.
- **drawer-category-button** — Text-first nested navigation row with chevron and back behavior.
- **cookie-primary-button** — Black square action button with uppercase white label.
- **cookie-text-link-button** — Underlined black text action on white modal.

### 13-3. Signature Micro-Specs

```yaml
black-document-consent:
  description: "Required legal UI is treated as a hard white document plane, not a soft ecommerce card."
  technique: "background #FFFFFF /* {colors.ivory} */; color #000000 /* {colors.ink} */; border-radius 0; box-shadow none; divider #D8D8D8 /* {colors.hairline} */"
  applied_to: ["{component.cookie-primary-button}", "{component.cookie-text-button}", "OneTrust consent modal"]
  visual_signature: "A white paper rectangle interrupts the dark fashion frame with black ink, square actions, and underlined text."

transparent-wordmark-chrome:
  description: "Header chrome floats over photography while the centered brand name carries recognition."
  technique: "position fixed; height 72px; background transparent; icon/text color #FFFFFF /* {colors.ivory} */; wordmark centered; utility labels around 12px with 0.06-0.08em tracking"
  applied_to: ["{component.header-transparent}", "hero navigation"]
  visual_signature: "The page reads as a photograph with jewelry-like controls, not as a conventional ecommerce header."

full-bleed-monogram-stage:
  description: "The first viewport is owned by editorial media, with commerce intent pushed low and small."
  technique: "min-height calc(var(--vh) * 100); width 100%; sizes 100vw; aspect-ratio 16/9; image-overlay treatment; radius 0"
  applied_to: ["{component.hero-full-bleed}", "Handbags hero"]
  visual_signature: "A dark monogram fashion image becomes the whole room; product copy appears like a caption near the floor."

uppercase-square-action:
  description: "Commerce actions are compact, monochrome, and stamped rather than pill-shaped."
  technique: "background #000000 /* {colors.ink} */; color #FFFFFF /* {colors.ivory} */; border-radius 0; min-height ~48px; padding 16px 32px; font-size 12px; font-weight 700; letter-spacing 0.08em; text-transform uppercase"
  applied_to: ["{component.cookie-primary-button}", "SHOP NOW CTA"]
  visual_signature: "The call to action feels like black ink pressed onto the interface, with no rounded comfort layer."

text-first-drawer-archive:
  description: "The category menu opens as a text archive drawer, not as a visual mega-menu with imagery."
  technique: "drawer surface #FFFFFF /* {colors.ivory} */; #000000 /* {colors.ink} */ text rows; chevron-suffixed labels with back-button affordance; no thumbnails or category cards; row spacing carries the hierarchy instead of color blocks; underline appears only on hover/active state, never as default decoration"
  applied_to: ["{component.drawer-category-button}", "main navigation drawer", "nested category traversal"]
  visual_signature: "Browsing Gucci feels like turning the pages of a couture catalogue index — quiet black uppercase rows on ivory, with no shop-window thumbnails competing with the photography elsewhere on the site."
```

---

## 14. Content Voice
<!-- SOURCE: manual -->

The captured voice is transactional but restrained. Category labels are plain (`Handbags`, `Women`, `Men`), CTAs are direct (`SHOP NOW`), and legal text is formal. No exclamation marks, no playful microcopy, no persuasive feature bullets. The brand assumes desire rather than explaining it.

---

## 15. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  --gucci-ink: #000000;
  --gucci-ivory: #FFFFFF;
  --gucci-near-black: #121212;
  --gucci-hairline: #D8D8D8;
  --gucci-muted-line: #E2E2E2;
  --gucci-disabled-text: #757575;
  --gucci-header-height: 72px;
  --gucci-font: "Gucci Sans Pro", "Helvetica Neue", Arial, sans-serif;
}

body {
  margin: 0;
  background: var(--gucci-ink);
  color: var(--gucci-ivory);
  font-family: var(--gucci-font);
  font-weight: 400;
  letter-spacing: 0;
}

.gucci-header {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 20;
  width: 100%;
  height: var(--gucci-header-height);
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  padding: 0 32px;
  color: var(--gucci-ivory);
  background: transparent;
}

.gucci-wordmark {
  font-size: 32px;
  font-weight: 300;
  letter-spacing: 0.28em;
  line-height: 1;
}

.gucci-hero {
  min-height: 100vh;
  position: relative;
  display: grid;
  place-items: end center;
  overflow: hidden;
  background: var(--gucci-near-black);
}

.gucci-hero img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.gucci-hero-copy {
  position: relative;
  z-index: 2;
  display: grid;
  justify-items: center;
  gap: 20px;
  padding-bottom: 96px;
}

.gucci-hero-copy p {
  margin: 0;
  font-size: 16px;
  font-weight: 400;
  color: rgba(255, 255, 255, 0.72);
}

.gucci-button {
  min-height: 48px;
  padding: 0 32px;
  border: 0;
  border-radius: 0;
  font-family: var(--gucci-font);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.gucci-button--primary {
  background: var(--gucci-ink);
  color: var(--gucci-ivory);
}

.gucci-button--ghost-light {
  background: rgba(255, 255, 255, 0.68);
  color: var(--gucci-ink);
}

.gucci-document-panel {
  width: min(650px, calc(100vw - 48px));
  padding: 40px 30px;
  border-radius: 0;
  background: var(--gucci-ivory);
  color: var(--gucci-ink);
  box-shadow: none;
}
```

---

## 16. Tailwind
<!-- SOURCE: manual -->

```js
export default {
  theme: {
    extend: {
      colors: {
        gucci: {
          ink: "#000000",
          ivory: "#FFFFFF",
          nearBlack: "#121212",
          hairline: "#D8D8D8",
          mutedLine: "#E2E2E2",
          disabledText: "#757575",
        },
      },
      fontFamily: {
        gucci: ["Gucci Sans Pro", "Helvetica Neue", "Arial", "sans-serif"],
      },
      borderRadius: {
        gucci: "0",
      },
      spacing: {
        header: "72px",
      },
      letterSpacing: {
        gucciCta: "0.08em",
        gucciLogo: "0.28em",
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

- Background/photo chrome: `#000000`, `#121212`
- Modal/document surface: `#FFFFFF`
- Text on modal: `#000000`
- Hairline: `#D8D8D8`
- Muted UI gray: `#757575`

### Prompt

Build a Gucci-inspired luxury commerce homepage. Use a full-bleed editorial fashion photograph as the first viewport, with a transparent fixed header, centered spaced wordmark, and thin utility icons. Keep the UI palette monochrome: black `#000000`, white `#FFFFFF`, near-black `#121212`, and gray hairlines `#D8D8D8`. Use `Gucci Sans Pro` if available, otherwise Manrope or Helvetica Neue with compact uppercase labels. Put one small product label and one square CTA low in the hero. Avoid cards, gradients, colorful accents, and rounded SaaS controls.

### Implementation Notes

- The hero is image-first. Do not replace it with abstract shapes.
- Keep visible ecommerce density low until menu interaction.
- Use square buttons and documentary modal surfaces.
- Header should feel like jewelry over the image: thin, quiet, precise.
- If a cookie or legal modal is needed, make it a hard white document plane, not a soft card.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO

- Use full-bleed editorial photography as the primary emotional surface.
- Use `#000000` and `#FFFFFF` as the core UI pair.
- Keep buttons square, uppercase, and compact.
- Let the centered wordmark carry luxury recognition.
- Hide dense catalog navigation behind drawer/menu behavior.
- Use `Gucci Sans Pro` or a close sans substitute, not a decorative serif.
- Treat gray as hairline structure, not brand accent.

### DON'T

- 배경을 `#FFFFFF`로 시작하지 말 것 — 첫 viewport는 `#000000`/photographic near-black이 기준이다.
- 텍스트를 전부 `#000000`로 두지 말 것 — hero chrome은 `#FFFFFF` 또는 soft white over image가 맞다.
- CTA를 금색 `#B9975B` 또는 `#D4AF37`로 만들지 말 것 — captured Gucci UI action은 `#000000`/`#FFFFFF`다.
- hairline을 파란색 `#3860BE`로 쓰지 말 것 — 이 값은 consent/vendor utility 흔적이고 구조선은 `#D8D8D8` 계열이다.
- surface gray를 `#F5F5F7` Apple식으로 깔지 말 것 — Gucci의 visible transactional surface는 `#FFFFFF` hard plane이다.
- body에 `font-weight: 300`만 고정하지 말 것 — captured system uses `400` body plus `700` action/title emphasis.
- 버튼에 `border-radius: 9999px`를 쓰지 말 것 — Gucci controls are square or nearly square.
- hero를 카드 안에 넣지 말 것 — image must be full-bleed, unframed, and viewport-owning.
- purple/blue gradient such as `#667EEA` to `#764BA2`를 쓰지 말 것 — no AI SaaS gradient language.
- product grid를 첫 화면에 노출하지 말 것 — catalog density is hidden behind navigation.

### 🚫 What This Site Doesn't Use

- No saturated secondary brand color in the captured hero UI.
- No warm gold luxury accent as a working interface color.
- No rounded pill CTA as the default brand control.
- No card-based hero composition.
- No visible 12-column marketing grid above the fold.
- No playful icons, stickers, emojis, or illustration system.
- No heavy UI shadows for luxury depth.
- No explanatory value-prop headline in the first viewport.
- No friendly SaaS gradient background.
- No serif display substitution for the captured sans identity.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- The captured screenshot is partially blocked by the OneTrust cookie modal. Hero interpretation uses visible background, saved HTML around `FhHeroFullBleed`, and the media asset metadata.
- Phase1 color extraction is polluted by Toastify and OneTrust vendor CSS. The guide separates brand-facing Gucci UI from third-party consent/toast tokens where possible.
- External Next.js stylesheet files were referenced in HTML but not all were available as local CSS files in the reused phase1 folder. Layout and component details therefore combine saved HTML structure with screenshot observation.
- Typography scale was not cleanly extracted into `typography.json.scale`; sizes in §05 are observed approximations.
- Product-listing cards below the first viewport were not visually audited in this pass; the guide focuses on homepage hero, header, menu, and consent surfaces.
- Motion timing for the header drawer and hero animation is inferred from attributes/classes, not measured in a live browser replay.
