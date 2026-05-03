---
schema_version: 3.2
slug: bain
service_name: Bain & Company
site_url: https://www.bain.com
fetched_at: 2026-04-23T11:49:20+0900
default_theme: mixed
brand_color: "#CC0000"
primary_font: Graphik
font_weight_normal: 400
token_prefix: bain

bold_direction: Executive Editorial
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: editorial-magazine
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "Large production CSS with repeated navigation, hero, carousel, button, card, and typography patterns; very few CSS custom properties."

colors:
  primary: "#CC0000"
  primary-hover: "#9D1B22"
  career-red: "#BB271A"
  surface: "#FFFFFF"
  ink: "#000000"
  muted-text: "#767676"
  hairline: "#D8D8D8"
  dot-neutral: "#979797"

typography:
  display: "Graphik"
  editorial: "TiemposHeadline"
  serif: "Tiempos"
  expressive: "RecklessNeue"
  ladder:
    - { token: hero-title, size: "3.75rem", weight: 500, line_height: "1.2", tracking: "-0.5px" }
    - { token: narrative-heading, size: "3.5rem", weight: 500, line_height: "1.2" }
    - { token: section-title, size: "2.5rem", weight: 500, line_height: "1.2" }
    - { token: body-lg, size: "1.125rem", weight: 400, line_height: "1.44" }
    - { token: nav-utility, size: ".68rem", weight: 500, line_height: "1", tracking: ".06em" }
  weights_used: [100, 200, 300, 400, 500, 600, 700, 900]
  weights_absent: [800]

components:
  button-primary: { bg: "{colors.primary}", color: "#FFFFFF", border: "1px solid #CC0000", padding: "1.25rem 2rem", radius: "0" }
  button-secondary: { bg: "#FFFFFF", color: "{colors.primary}", border: "1px solid #D8D8D8", padding: "1.25rem 2rem", radius: "0" }
  textlink-cta: { color: "{colors.primary}", weight: 500, after_icon: "long arrow", transition: "right 200ms" }
  homepage-hero: { bg: "full-bleed image + multi-gradient overlay", color: "#FFFFFF", min_height: "95vh desktop / 21.25rem base" }
  primary-navigation: { font: "Graphik", display: "flex", padding_y: "1rem", utility_tracking: ".06em" }
---

# DESIGN.md - Bain & Company

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Bain's homepage reads like an executive briefing staged on the cover of a business newspaper, with the newsroom lights turned down and the city tower glass left visible behind the headline. The page does not open with a software gradient, product UI, or illustrated mascot; it opens with full-bleed corporate architecture, white overlaid type, and a small red progress rule. The visual contract is simple: photography carries institutional authority, Graphik carries navigation discipline, and #CC0000 (`{colors.primary}`) cuts through only where the interface needs command.

The strongest motif is vertical corporate scale. The hero photograph looks upward through towers, so the headline feels pinned to a glass high-rise lobby rather than placed on a flat brand panel. Bain does not put a red carpet under the entire page; it lets the building become the stage, then marks the next decision with a Bain-red blade. The effect is a boardroom laser pointer held still: one sharp line of `{colors.primary}`, surrounded by black, white, and executive silence.

Color is intentionally narrow. #CC0000 (`{colors.primary}`) is not spread as a decorative wash; it appears as the Bain red in icons, button fills, CTA arrows, active carousel progress, and category emphasis. There is no second brand color waiting in the wings, no friendly gradient family, no chromatic mood board. The rest of the system is black, white, #767676 (`{colors.muted-text}`), and #D8D8D8 (`{colors.hairline}`), like a printed annual report where the only red ink is the editor's decisive mark.

Typography is the real operating system. Graphik is overwhelmingly dominant in the CSS and carries nav, body, buttons, and most headings. TiemposHeadline, Tiempos, and RecklessNeue exist as editorial accents, but the homepage hero screenshot shows the main identity through large, confident Graphik rather than a luxury serif. It behaves like a consulting deck that has been typeset by a magazine art desk: uppercase micro-navigation sits like the index tabs of a research binder, while stacked headlines take the scale of a front-page lead story.

The interaction craft is small but specific. Bain uses arrow movement, carousel progress bars, off-canvas mega-menu layers, and image overlays instead of heavy component chrome. Shadow belongs mostly to photography and occasional content depth; the chrome itself stays square, flat, and procedural. It avoids neumorphism, glass cards, rounded SaaS pills, and dense dashboard panels. The interface feels like a serious editorial front door for a global advisory firm: not a product demo, not a magazine for leisure, but a controlled briefing room where every red mark says "this is the next decision."

### Key Characteristics

- Full-bleed photographic hero with a multi-layer dark overlay, not a flat color hero.
- Bain red #CC0000 (`{colors.primary}`) used as a command accent, not a background theme.
- Graphik-first typography with uppercase utility navigation and medium-weight CTAs.
- Large stacked hero headline in white over photography.
- Two-tier navigation: tiny uppercase utility nav above a larger primary mega-menu.
- Strong off-canvas and mega-menu information architecture for industries, services, insights, and careers.
- Editorial CTA language: "READ MORE" plus long-arrow icon, not pill-heavy conversion copy.
- Mostly square component geometry; primary buttons use radius 0.
- Hairline gray separators (#D8D8D8) and muted text (#767676) do structural work.
- Carousel identity: red active progress rule, white topic labels, and image-led transitions.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Executive Editorial
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **full-bleed boardroom photography with a Bain-red progress blade**으로 기억된다.
> **Code Complexity**: high — large production CSS, carousel/off-canvas navigation, image overlays, responsive breakpoints, and icon-font interactions.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Bain처럼 만들기 - 3가지만 하면 80%

```css
/* 1. Font discipline */
body {
  font-family: "Graphik", Helvetica, sans-serif, "Lucida Sans Unicode";
  font-weight: 400;
  line-height: 1.44;
}

/* 2. Executive editorial color contract */
:root {
  --bain-red: #CC0000;
  --bain-red-hover: #9D1B22;
  --bain-ink: #000000;
  --bain-muted: #767676;
  --bain-hairline: #D8D8D8;
  --bain-surface: #FFFFFF;
}

/* 3. Hero anatomy */
.hero {
  min-height: 95vh;
  color: #FFFFFF;
  background:
    linear-gradient(to right, rgba(0,0,0,.07), rgba(0,0,0,.07)),
    linear-gradient(to right, rgba(0,0,0,.25), rgba(0,0,0,0) 50%),
    linear-gradient(to bottom, rgba(0,0,0,.2), rgba(0,0,0,0) 160px),
    linear-gradient(to top, rgba(0,0,0,.1), rgba(0,0,0,0) 100px);
}
```

**절대 하지 말아야 할 것 하나**: Bain red #CC0000을 페이지 전체 배경이나 gradient wash로 확장하지 말 것. 이 사이트에서 red는 blade/accent/CTA 역할이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.bain.com` |
| Fetched | 2026-04-23T11:49:20+0900 |
| Extractor | existing phase1 reuse |
| HTML size | 222249 bytes |
| CSS files | 3 files, 1812840 bytes |
| Token prefix | `bain` |
| Method | phase1 JSON + CSS frequency + screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: production CMS / server-rendered corporate site (exact platform not asserted from available evidence)
- **Design system**: Bain production CSS, not token-heavy CSS custom-property system
- **CSS architecture**: large compiled stylesheet with BEM-like component classes
  ```text
  base grid      .row / .column / breakpoint utilities
  navigation     .primary-nav / .utility-navigation / .off-canvas-menu
  hero           .hero--homepage / .hero__slide / .hero__overlay
  components     .btn / .btn--secondary / .textlink--cta / card patterns
  ```
- **Class naming**: BEM-ish component naming with modifier classes, e.g. `.hero--homepage`, `.hero__cta`, `.primary-nav__level-two`
- **Default theme**: mixed. Homepage hero is dark-over-image; below-page surfaces are primarily white.
- **Font loading**: custom brand fonts detected in CSS: Graphik, TiemposHeadline, Tiempos, RecklessNeue, bainicon.
- **Canonical anchor**: Bain red #CC0000 plus Graphik navigation and full-bleed editorial hero.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Graphik` for most homepage hero and UI display surfaces.
- **Editorial fonts**: `TiemposHeadline`, `Tiempos`, and `RecklessNeue` appear in CSS as editorial/expressive accents.
- **Icon font**: `bainicon` powers arrows, search, folder, and UI glyphs.
- **Weight normal / bold**: `400` / `500-600`; CSS also contains 100, 200, 300, 700, and 900 in smaller quantities.

```css
:root {
  --bain-font-family: "Graphik", Helvetica, sans-serif, "Lucida Sans Unicode";
  --bain-font-editorial: "Tiempos", Georgia, serif;
  --bain-font-headline: "TiemposHeadline";
  --bain-font-expressive: "RecklessNeue", "Tiempos", Georgia, serif;
  --bain-font-weight-normal: 400;
  --bain-font-weight-strong: 500;
  --bain-font-weight-bold: 600;
}
```

### Note on Font Substitutes

- **Graphik** — Proprietary brand sans. Open-source fallback: **Inter** at 400/500/600 with `letter-spacing: 0` for body and `letter-spacing: -0.01em` only on large display headlines. Helvetica fallback is already present in Bain CSS, but Inter better preserves Graphik's contemporary consulting tone.
- **Tiempos / TiemposHeadline** — Commercial editorial serif. Open-source fallback: **Source Serif 4** at 400/600 with line-height tightened from 1.44 to 1.35 for headings.
- **RecklessNeue** — Expressive serif accent. Open-source fallback: **Fraunces** should be used sparingly and only for editorial pull elements, never primary nav or buttons.
- **bainicon** — Replace with lucide-style line icons only if icon font is unavailable; preserve long-arrow behavior and small utility glyph scale.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `hero-title` | `3.75rem` observed frequently | 500 | 1.2 | `-0.5px` / occasional negative tracking |
| `narrative-heading` | `3.5rem` | 500 | 1.2 | 0 |
| `section-title` | `2.5rem` | 500 | 1.2 | 0 |
| `article-title` | `2rem` | 500 | 1.2-1.33 | 0 |
| `body-lg` | `1.125rem` | 400 | 1.44 | 0 |
| `body` | `1rem` | 400 | 1.44 | 0 |
| `small` | `.875rem` | 400-500 | 1.44 | 0 |
| `utility-nav` | `.68rem` | 500 | 1 | `.06em` |
| `button` | `.875rem` | 500 | 1.2 | uppercase |

> ⚠️ Typography key insight: Bain is not a serif-led luxury site. Graphik appears hundreds of times and defines the interface; serif families are supporting editorial instruments.

### Principles

1. Graphik owns the product surface: nav, body, CTAs, labels, and many headings.
2. Utility navigation is tiny, uppercase, and tracked `.06em`; do not enlarge it into standard 14px menu text.
3. Body rhythm sits around line-height `1.44`, giving editorial readability without looking like a blog.
4. CTAs use weight `500`, uppercase, and arrow motion; they do not rely on rounded pill geometry.
5. Display type can be very large but remains direct and corporate. Avoid playful optical sizes or bubbly weights.
6. Serif fonts are accent layers; overusing them will make Bain feel like a magazine brand rather than a consulting firm.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp

| Token | Hex |
|---|---|
| `{colors.primary}` | `#CC0000` |
| `{colors.primary-hover}` | `#9D1B22` |
| `{colors.career-red}` | `#BB271A` |
| `{colors.deep-red}` | `#902928` |
| `{colors.pale-red}` | `#FCE3E3` |

### 06-2. Brand Dark Variant

> N/A — dark mode counterpart palette was not established in the phase1 evidence. Hero darkness comes from image overlays, not a parallel dark token system.

### 06-3. Neutral Ramp

| Step | Hex | Usage |
|---|---|---|
| white | `#FFFFFF` / `#FFF` | surface, secondary buttons, panels |
| near-white | `#F9F9F9` / `#F5F5F5` | subtle page areas and backgrounds |
| hairline | `#D8D8D8` / `#D9D9D9` | separators, secondary borders |
| gray-500 | `#979797` | carousel dots, secondary UI |
| muted text | `#767676` / `#717171` | nav text, muted copy |
| charcoal | `#424242` / `#333333` | dark secondary surfaces |
| black | `#000000` / `#0A0A0A` | ink, overlays, deep contrast |

### 06-4. Accent Families

| Family | Key Hex | Usage |
|---|---|---|
| Bain red | `#CC0000` | primary brand, active states, progress, CTA |
| hover red | `#9D1B22` | button and link hover |
| careers red | `#BB271A` | careers-specific secondary theme |
| cool blue | `#0484E7` | rare external/system accent; not core brand |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--bain-action-primary` | `#CC0000` | primary button, active icons, progress rule |
| `--bain-action-hover` | `#9D1B22` | hover/focus red |
| `--bain-surface` | `#FFFFFF` | default content surface |
| `--bain-ink` | `#000000` | primary copy |
| `--bain-muted` | `#767676` | utility nav, muted labels |
| `--bain-border` | `#D8D8D8` | borders and separators |

### 06-6. Semantic Alias Layer

> N/A — `resolved_tokens.json` found only one CSS custom property (`--size`). Bain's available CSS is compiled and selector-driven rather than custom-property-token-driven.

### 06-7. Dominant Colors

| Hex | Frequency | Interpretation |
|---|---:|---|
| `#CC0000` | 1853 | true brand/action red |
| `#C00` | 584 | shorthand duplicate of Bain red |
| `#FFF` | 521 | dominant white surface |
| `#000` | 353 | ink and overlays |
| `#D8D8D8` | 337 | hairlines and secondary borders |
| `#767676` | 157 | muted text |
| `#BB271A` | 92 | careers red |
| `#979797` | 89 | carousel/dot/secondary UI |

### 06-8. Color Stories

**`{colors.primary}` (`#CC0000`)** — Bain red is a blade, not a wash. It marks decisions: active carousel progress, button fills, folder icons, CTA arrows, and key action emphasis. Use it in narrow, high-confidence strokes.

**`{colors.surface}` (`#FFFFFF`)** — White is the working canvas below the hero. It keeps dense consulting navigation and editorial content legible while letting photography and red accents carry identity.

**`{colors.ink}` (`#000000`)** — Black is both type and atmosphere. It appears as direct text and as transparent overlay layers across hero imagery; do not replace it with soft navy.

**`{colors.hairline}` (`#D8D8D8`)** — Gray lines provide quiet structure. Secondary buttons, borders, and dividers depend on this corporate neutral rather than on card shadows or colored backgrounds.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `gutter-small` | `.5625rem` | base column gutter |
| `gutter-medium` | `.75rem` | tablet grid gutter |
| `gutter-large` | `1.25rem` | desktop grid gutter |
| `nav-y` | `1rem` | primary nav vertical padding |
| `hero-base-y` | `2.5rem` | base hero slide padding |
| `button-y` | `1.25rem` | primary/secondary button vertical padding |
| `button-x` | `2rem` | primary/secondary button horizontal padding |
| `content-stack` | `2rem` | common button rows and content rhythm |
| `main-content-y` | `8rem` | `.main-content` vertical margin |

**주요 alias**:
- `.row` → max-width `85rem`
- `.main-content` → max-width `60rem`
- `.column` → responsive gutter `.5625rem` → `.75rem` → `1.25rem`

### Whitespace Philosophy

Bain uses two spacing modes: editorial air for major content and compressed information architecture for navigation. The top navigation is dense because it must expose a global consulting taxonomy; the hero, by contrast, uses a large image field and stacked headline to slow the page down.

The grid is not a modern CSS Grid showcase. It is a Foundation-like row/column system with restrained gutters and broad max-widths. That older corporate-grid discipline is part of the look: reliable, modular, and more newsroom than startup landing page.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `square` | `0` | primary buttons, nav bars, editorial panels |
| `small` | `3px` / `4px` | small utility UI and embedded widgets |
| `input-ish` | `6px` / `10px` | chat/form-related UI, not core homepage identity |
| `capsule` | `50px` / `5000px` | occasional pill/capsule controls |
| `circle` | `50%` | icons, carousel dots, circular controls |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none | `none` | dominant chrome behavior |
| low utility | `0 2px 7px 0 rgba(0,0,0,.07)` | light UI elevation |
| widget | `0 3px 6px rgba(0,0,0,.1607843137)` | embedded/chat style utility |
| image/card | `.75rem .75rem 1.5rem #D8D8D8` | occasional content/card depth |

> Bain's homepage identity is not shadow-led. Depth comes from photography, overlays, and structural hierarchy.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `fast` | `200ms` | button/link transitions |
| `medium` | `.25s` | carousel dot track movement |
| `hero-cta-reveal` | `.5s`, delay `.6s` | homepage CTA text slides from left and fades in |
| `off-canvas-level` | `400ms-600ms` | menu level transitions |
| `arrow-nudge` | `right -0.25rem -> -0.5rem` or `left 0 -> .75rem` | CTA arrow motion |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `.row` max-width `85rem`; `.main-content` max-width `60rem`.
- **Grid type**: float-based row/column system plus flex in navigation and hero.
- **Column count**: Foundation-style responsive columns; exact column classes vary by page.
- **Gutter**: `.5625rem` base, `.75rem` tablet, `1.25rem` desktop.

### Hero

- **Pattern Summary**: `95vh desktop + full-bleed image + multi-gradient overlay + left stacked H1 + lower carousel topic nav`.
- Layout: full-width carousel slide; text block positioned over image, screenshot shows left-aligned stacked hero.
- Background: editorial photography, object-fit cover.
- **Background Treatment**: image overlay with multiple black transparent gradients:
  `rgba(0,0,0,.07)` full veil, `rgba(0,0,0,.25)` left-to-transparent, `rgba(0,0,0,.2)` top fade, `rgba(0,0,0,.1)` bottom fade.
- H1: large Graphik, white, approximately `3.75rem` desktop pattern, weight `500`, tight stacked lines.
- Max-width: hero text uses row/column grid, not a centered narrow card.

### Section Rhythm

```css
.row { max-width: 85rem; margin-right: auto; margin-left: auto; }
.column { width: 100%; padding-right: .5625rem; padding-left: .5625rem; }
.main-content { max-width: 60rem; margin: 8rem auto; }
```

### Card Patterns

- **Card background**: mostly `#FFFFFF`; imagery usually leads.
- **Card border**: light gray hairlines such as `#D8D8D8`.
- **Card radius**: often `0`; utility widgets may use small radius.
- **Card padding**: content-dependent, commonly `1rem-2rem`.
- **Card shadow**: usually none; occasional image/card depth uses gray shadow.

### Navigation Structure

- **Type**: two-tier horizontal desktop navigation with mega-menu and off-canvas mobile/menu states.
- **Position**: header overlays hero in screenshot; CSS evidence includes `site-header`, `primary-nav`, and off-canvas structures.
- **Height**: primary nav uses `padding-top: 1rem; padding-bottom: 1rem`; utility nav is smaller.
- **Background**: transparent/dark over hero, white in off-canvas panels.
- **Border**: subtle separators; utility and off-canvas rely on gray hairlines.

### Content Width

- **Prose max-width**: `60rem` for `.main-content`.
- **Container max-width**: `85rem` for `.row`.
- **Sidebar width**: not established from homepage evidence; mega-menu columns create temporary navigation side structures.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `<48em` / `<47.9375rem` | off-canvas behavior, single-column grid, smaller hero min-height |
| Tablet | `48em` / `48rem` | medium column gutter `.75rem`, expanded row behavior |
| Desktop | `67.5625em` / `67.5625rem` | large nav and desktop hero rhythm |
| Wide | `80.0625em`, `90em`, `120em` | high-width refinements and carousel/dot behavior |

### Touch Targets

- **Minimum tap size**: not fully guaranteed from extracted CSS; some widget controls are smaller than 44px.
- **Button height (mobile)**: primary buttons use generous `1.25rem 2rem` padding, but exact computed height was not measured.
- **Input height (mobile)**: not surfaced in homepage evidence.

### Collapsing Strategy

- **Navigation**: desktop horizontal mega-menu collapses into off-canvas menu with nested level transitions.
- **Grid columns**: row/column gutters scale by breakpoint; mobile columns become full width.
- **Sidebar**: no persistent sidebar observed on homepage.
- **Hero layout**: full-bleed image persists; base slide min-height `21.25rem`, desktop can reach `95vh`.

### Image Behavior

- **Strategy**: full-width image containers with `object-fit: cover`.
- **Max-width**: hero images override default with `max-width: none`.
- **Aspect ratio handling**: hero clips/covers rather than letterboxes.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary button**

| Property | Value |
|---|---|
| Selector | `.btn` |
| Background | `#CC0000` |
| Color | `#FFFFFF` |
| Border | `1px solid #CC0000` |
| Padding | `1.25rem 2rem` |
| Font | Graphik, `.875rem`, weight `500`, uppercase |
| Radius | `0` |
| Hover/focus | background/border `#9D1B22`, text `#FFFFFF` |

```html
<a class="btn" href="#">Read more</a>
```

**Secondary button**

| Property | Value |
|---|---|
| Selector | `.btn--secondary` |
| Background | `#FFFFFF` |
| Color | `#CC0000` |
| Border | `1px solid #D8D8D8` |
| Hover/focus | background `#9D1B22`, border transparent, color `#FFFFFF` |

### Badges

> N/A — homepage evidence did not surface a signature badge system. Do not fabricate badge variants.

### Cards & Containers

Bain cards are image/editorial containers more than boxed SaaS cards. Use white surfaces, hairline separators, square edges, and photography-first composition. Avoid nested card chrome. When depth is needed, use restrained gray shadows or image contrast rather than colorful elevation.

### Navigation

Navigation is a core component. It combines:

- uppercase utility links at `.68rem`, weight `500`, tracking `.06em`, muted #767676;
- primary nav at Graphik, flex row, `1rem` vertical padding;
- icon font glyphs for search, folder, menu, bookmark, and arrows;
- multi-column mega-menu with `.primary-nav__level-two`, `.primary-nav__level-three`, and off-canvas mobile layers.

### Inputs & Forms

> Limited homepage evidence. Use square or lightly rounded fields, Graphik labels, #D8D8D8 borders, and #CC0000 focus/accent only after confirming form-specific CSS in a deeper flow.

### Hero Section

The homepage hero is the signature component:

- full-bleed image/video surface;
- white title text;
- editorial category tag;
- uppercase "READ MORE" CTA with long-arrow icon;
- lower carousel navigation with red active progress bar;
- dark overlay made from multiple directional gradients.

### 13-2. Named Variants

**button-primary** — Bain red action block.

```css
.btn {
  background: #CC0000;
  color: #FFFFFF;
  border: 1px solid #CC0000;
  padding: 1.25rem 2rem;
  text-transform: uppercase;
  border-radius: 0;
}
.btn:hover,
.btn:focus {
  background: #9D1B22;
  border-color: #9D1B22;
}
```

**button-secondary** — white action block with gray border and red text.

```css
.btn--secondary {
  background: #FFFFFF;
  color: #CC0000;
  border: 1px solid #D8D8D8;
}
```

**textlink-cta** — editorial link with arrow nudge.

```css
.textlink--cta {
  font-weight: 500;
  color: #CC0000;
  border-bottom: none;
}
.textlink--cta:after {
  transition: all 200ms;
  right: -.25rem;
}
.textlink--cta:hover:after { right: -.5rem; }
```

**homepage-carousel-topic** — lower hero topic navigation.

```css
.hero--homepage .hero__slide-nav-item {
  color: #FFFFFF;
  font-size: .9375rem;
  font-weight: 500;
  opacity: .5;
}
.hero--homepage .hero__slide-nav-progress {
  background-color: #CC0000;
  height: 5px;
}
```

### 13-3. Signature Micro-Specs

```yaml
bain-red-progress-blade:
  description: "Active carousel state becomes a flat decision rule rather than a decorative tab."
  technique: "background-color: #CC0000; height: 5px; transition: width linear"
  applied_to: ["{component.homepage-carousel-topic}", ".hero--homepage .hero__slide-nav-progress"]
  visual_signature: "A Bain-red horizontal blade under white topic labels, giving the hero a consulting-editorial pulse."

executive-photo-overlay-stack:
  description: "Hero readability is built from directional black veils over corporate photography."
  technique: "linear-gradient rgba(0,0,0,.07) full veil + rgba(0,0,0,.25) left fade + rgba(0,0,0,.2) top fade + rgba(0,0,0,.1) bottom fade"
  applied_to: ["{component.homepage-hero}", ".hero__overlay", ".hero--homepage"]
  visual_signature: "White boardroom-scale headlines stay legible while the tower photograph still feels full-bleed and physical."

graphik-utility-taxonomy:
  description: "Navigation reads as a consulting taxonomy, not generic menu text."
  technique: "font-family Graphik; font-size .68rem; font-weight 500; line-height 1; letter-spacing .06em; text-transform uppercase; color #767676"
  applied_to: ["{component.primary-navigation}", ".utility-navigation", ".primary-nav"]
  visual_signature: "Tiny uppercase business categories sit like research binder tabs above the heavier primary menu."

arrow-nudge-cta:
  description: "Editorial continuation is signaled by lateral arrow motion rather than button bounce."
  technique: "transition: all 200ms; right: -.25rem -> -.5rem on text links; left: 0 -> .75rem on hero arrow hover"
  applied_to: ["{component.textlink-cta}", ".textlink--cta", ".hero__cta .icon-long-arrow-right"]
  visual_signature: "READ MORE feels like turning to the next article in an executive briefing."

square-red-action-block:
  description: "Primary actions stay rectangular and procedural."
  technique: "background #CC0000; border 1px solid #CC0000; padding 1.25rem 2rem; border-radius 0; text-transform uppercase; hover #9D1B22"
  applied_to: ["{component.button-primary}", "{component.button-secondary}", ".btn", ".btn--secondary"]
  visual_signature: "Corporate decisiveness: no friendly pill softness, just a square Bain-red command block."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | declarative executive insight, often stacked | "CFOs Funded the AI Revolution. Now They're Joining It." |
| Primary CTA | short uppercase action | "READ MORE" |
| Navigation | taxonomy-first business categories | "Industries", "Consulting Services", "Insights" |
| Topic labels | consulting practice or sector labels | "Performance Improvement", "Private Equity", "Technology" |
| Tone | boardroom direct, editorial, evidence-oriented | no playful slogans observed |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Bain & Company - copy into your root stylesheet */
:root {
  /* Fonts */
  --bain-font-family: "Graphik", Helvetica, sans-serif, "Lucida Sans Unicode";
  --bain-font-editorial: "Tiempos", Georgia, serif;
  --bain-font-weight-normal: 400;
  --bain-font-weight-strong: 500;
  --bain-font-weight-bold: 600;

  /* Brand */
  --bain-color-brand-25: #FCE3E3;
  --bain-color-brand-300: #BB271A;
  --bain-color-brand-500: #CC0000;
  --bain-color-brand-600: #CC0000; /* canonical */
  --bain-color-brand-900: #9D1B22;

  /* Surfaces */
  --bain-bg-page: #FFFFFF;
  --bain-bg-dark: #000000;
  --bain-text: #000000;
  --bain-text-muted: #767676;
  --bain-border: #D8D8D8;

  /* Key spacing */
  --bain-space-sm: .5625rem;
  --bain-space-md: 1rem;
  --bain-space-lg: 2rem;
  --bain-space-xl: 2.5rem;

  /* Radius */
  --bain-radius-sm: 0;
  --bain-radius-md: 0;
  --bain-radius-circle: 50%;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js - Bain-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        bain: {
          red: '#CC0000',
          redHover: '#9D1B22',
          career: '#BB271A',
          ink: '#000000',
          muted: '#767676',
          hairline: '#D8D8D8',
          surface: '#FFFFFF',
        },
      },
      fontFamily: {
        sans: ['Graphik', 'Inter', 'Helvetica', 'sans-serif'],
        editorial: ['Tiempos', 'Source Serif 4', 'Georgia', 'serif'],
      },
      borderRadius: {
        bain: '0',
        bainCircle: '50%',
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
| Brand primary | `{colors.primary}` | `#CC0000` |
| Brand hover | `{colors.primary-hover}` | `#9D1B22` |
| Background | `{colors.surface}` | `#FFFFFF` |
| Hero text | white | `#FFFFFF` |
| Text primary | `{colors.ink}` | `#000000` |
| Text muted | `{colors.muted-text}` | `#767676` |
| Border | `{colors.hairline}` | `#D8D8D8` |

### Example Component Prompts

#### Hero Section

```text
Bain & Company 스타일 홈페이지 히어로를 만들어줘.
- 배경: full-bleed corporate architecture photography
- overlay: black transparent multi-gradient, left side readability 강화
- H1: Graphik, 3.75rem desktop, weight 500, white, stacked lines
- category label: Graphik 1.125rem, white or red depending on image contrast
- CTA: uppercase READ MORE, long arrow icon, white text, arrow moves on hover
- 하단 carousel nav: topic labels in white, active item has 5px #CC0000 progress rule
```

#### Button

```text
Bain primary button을 만들어줘.
- font: Graphik .875rem, weight 500, uppercase
- bg #CC0000, color #FFFFFF, border 1px solid #CC0000
- padding 1.25rem 2rem, radius 0
- hover/focus: bg and border #9D1B22
```

#### Navigation

```text
Bain style navigation을 만들어줘.
- 2-tier header: tiny uppercase utility nav + larger primary nav
- utility links: .68rem, weight 500, letter-spacing .06em, color #767676
- primary nav: Graphik, flex row, 1rem vertical padding
- support hamburger/off-canvas and mega-menu columns
- use #CC0000 only for active folder/indicator states
```

### Iteration Guide

- **색상 변경 시**: #CC0000은 accent/action으로만 사용. 배경 전체를 red로 덮지 않는다.
- **폰트 변경 시**: Graphik 대체는 Inter/Helvetica 계열로; serif를 nav나 buttons에 쓰지 않는다.
- **여백 조정 시**: row max-width `85rem`, main content `60rem`, desktop gutter `1.25rem`을 기준으로 한다.
- **새 컴포넌트 추가 시**: square geometry, hairline separators, and Graphik uppercase actions.
- **이미지 사용 시**: corporate/editorial photography with overlay, not abstract illustrations.
- **반응형**: 48em and 67.5625em breakpoints are the main rhythm.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use Graphik as the dominant font for nav, body, buttons, and core headings.
- Use #CC0000 as a precise action/accent color: buttons, active progress, icons, CTA arrows.
- Build the hero around full-bleed photography plus black overlay gradients.
- Keep primary button corners square with `border-radius: 0`.
- Use muted #767676 utility text and #D8D8D8 hairlines for structure.
- Preserve the two-tier navigation hierarchy and off-canvas/mega-menu depth.
- Use uppercase CTAs with arrow motion for editorial continuation.
- Let photography and typography create authority; keep decorative chrome minimal.

### ❌ DON'T

- 배경을 `#CC0000` 전체 면으로 두지 말 것 — 대신 `#FFFFFF` surface와 image overlay 위 accent로 `#CC0000` 사용.
- primary text를 `#333333`으로 약하게 두지 말 것 — 대신 `#000000` 또는 hero에서는 `#FFFFFF` 사용.
- muted utility nav를 `#000000`으로 두지 말 것 — 대신 `#767676` 사용.
- secondary borders를 `#CCCCCC` 일반 gray로만 두지 말 것 — Bain hairline은 `#D8D8D8`가 더 정확하다.
- primary hover를 밝은 red `#FF0000`으로 만들지 말 것 — 대신 dark hover `#9D1B22` 사용.
- button에 `border-radius: 999px` pill을 기본값으로 쓰지 말 것 — core `.btn`은 `border-radius: 0`.
- hero를 flat `#FFFFFF` background로 시작하지 말 것 — homepage signature는 full-bleed image + black overlay.
- CTA를 lowercase casual text로 만들지 말 것 — Bain CTA는 uppercase Graphik + arrow.
- nav letter-spacing을 `0`으로 풀지 말 것 — utility nav는 `.06em` tracking이 필요하다.
- page-wide purple gradient `#667EEA` / `#764BA2`를 쓰지 말 것 — Bain에는 그런 SaaS gradient identity가 없다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second brand color: none observed. #CC0000 carries the brand/action role.
- Gradient brand palette: absent. Gradients are black readability overlays, not colorful identity.
- Rounded SaaS pills: not core. Primary `.btn` is square.
- Glassmorphism: absent. No frosted cards or blur-heavy chrome in the observed homepage.
- Dashboard density: absent. Bain is editorial/navigation-heavy, not app-dashboard UI.
- Friendly illustration system: absent from the hero identity; real/corporate photography dominates.
- Heavy card shadows: mostly absent. Structure comes from layout, hairlines, and imagery.
- Playful motion: absent. Motion is arrow nudge, carousel progress, and menu transitions.
- Token-rich CSS variables: absent in available CSS. System is compiled selector CSS, not a custom-property API.
- Casual lowercase conversion copy: absent in CTAs; uppercase action language dominates.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage snapshot** — The analysis reuses `insane-design/bain` phase1 assets and the captured homepage hero. Consulting service pages, insights articles, careers pages, and office pages may contain additional component variants.
- **Compiled CSS limits token certainty** — `resolved_tokens.json` found only one custom property, so named tokens in this guidebook are pragmatic aliases over observed CSS values, not real Bain CSS variable names.
- **Form states not fully observed** — Inputs, validation, loading, and error states were not materially surfaced in the homepage evidence.
- **Dark mode not established** — The site uses dark hero overlays, but a complete dark theme token map was not observed.
- **Computed font metrics not measured** — Font families and CSS values were extracted, but browser-computed exact hero H1 size/line-height was inferred from CSS frequency and screenshot.
- **Navigation behavior not interactively replayed** — Off-canvas and mega-menu classes are present in HTML/CSS, but this guide does not claim a full JS state-machine audit.
- **Logo/customer color filtering** — Frequency counts may include icon font, embedded widgets, and page modules beyond the visible hero. #CC0000 remains the clear brand anchor despite this noise.
- **Motion curves partially inferred** — CSS transition durations were read from stylesheets; scroll-triggered or carousel JS timing beyond visible CSS was not audited.
