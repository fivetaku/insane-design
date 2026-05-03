---
schema_version: 3.2
slug: deloitte-digital
service_name: Deloitte Digital
site_url: https://www.deloittedigital.com
fetched_at: 2026-05-03T15:26:49+0900
default_theme: mixed
brand_color: "#86BC25"
primary_font: Open Sans
font_weight_normal: 300
token_prefix: dd

bold_direction: Corporate Nocturne
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "AEM component system with repeated cmp-* modules, Tailwind-like utility output, and Deloitte color/font primitives in use, but no clean custom-property token graph."

colors:
  black: "#000000"
  white: "#FFFFFF"
  deloitte-green: "#86BC25"
  grey-30: "#D0D0CE"
  grey-10: "#F3F3F3"
  cyan-soft: "#A0DCFF"
  teal: "#007680"
  mint: "#9DD4CF"
typography:
  display: "Open Sans"
  body: "Open Sans"
  ladder:
    - { token: h1-desktop, size: "116px", weight: 300, line_height: "126px", tracking: "0" }
    - { token: h2-desktop, size: "80px", weight: 300, line_height: "94px", tracking: "0" }
    - { token: h3-desktop, size: "56px", weight: 300, line_height: "70px", tracking: "0" }
    - { token: h4-desktop, size: "40px", weight: 300, line_height: "50px", tracking: "0" }
    - { token: body-desktop, size: "14px", weight: 300, line_height: "24px", tracking: "0" }
    - { token: eyebrow, size: "16px", weight: 300, line_height: "36px", tracking: "1.5px" }
  weights_used: [100, 300, 400, 500, 600, 700, 800]
  weights_absent: [200, 900]
components:
  rounded-outline-cta: { bg: "transparent", radius: "6.25em", padding: ".75em 2.5em", border: "1px solid currentColor" }
  large-pill-cta: { bg: "#D0D0CE", radius: "9999px", padding: "18px 60px", text: "#000000" }
  mosaic-tile: { size: "340px", gap: "8px", margin: "20px", title: "2em / 40px" }
  desktop-nav-item: { breakpoint: "1024px", margin_right: "26-40px", display: "flex" }
---

# DESIGN.md - Deloitte Digital (Designer Guidebook)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Deloitte Digital is not a bright agency brochure. It behaves more like a night-time consulting theater: a black glass stage, muted grey type, and one small green signal that says this still belongs to Deloitte. The hero screenshot carries the whole attitude. A dark editorial photograph fills the first viewport, then a translucent black overlay pushes the image back until the headline feels almost whispered rather than shouted.

The brand color is intentionally tiny. `#86BC25` (`{colors.deloitte-green}`) appears as a point of recognition, not as a flood fill. Deloitte Digital has no second brand color on stage; there is the black room, the grey voice, the white utility surface, and the green dot. Most of the UI is built from `#000000` (`{colors.black}`), `#FFFFFF` (`{colors.white}`), and `#D0D0CE` (`{colors.grey-30}`). The effect is corporate, but not sterile: the photography brings motion and atmosphere while the interface remains restrained.

Typography is the main chassis. Open Sans is used with a surprisingly light default weight, and the desktop scale jumps from body sizes into 40px, 56px, 80px, and 116px display classes. The type sits like a consultant's briefing note pinned to a black-box theater wall: large, pale, and deliberate, but never typographically theatrical for its own sake. Deloitte Digital uses wide tracking for uppercase labels and CTAs. That letter-spaced voice matters: without it, the interface becomes a generic dark landing page.

The hero is closer to a strategy film still than to a SaaS billboard. Photography becomes the room lighting; shadow belongs to the image and overlay, not to decorative chrome. The grey headline does not try to cut through like pure white. It behaves more like copy on a dim projection screen: readable, atmospheric, and slightly held back.

The component system is large and AEM-shaped. The visible surface looks minimal, but the CSS underneath carries many modules: navigation dropdowns, rounded CTAs, mosaic grids, carousels, tabs, modals, forms, cookie controls, and Tailwind-like utilities. Reproduction should not chase every module. Capture the black editorial shell, the light Open Sans scale, the pill CTA, and the 340px mosaic/card grammar. Below the theater-like hero, the page turns into an editorial contact sheet: square image tiles, tight gutters, and panel interiors that feel catalogued rather than card-stacked.

### Key Characteristics

- Black editorial hero with image overlay, not a flat dark gradient.
- Deloitte green `#86BC25` used as a small identity marker, not a full UI wash.
- Primary text often lands in muted grey `#D0D0CE`, especially on dark surfaces.
- Open Sans drives both display and body; weight 300 is a real part of the voice.
- Uppercase labels use wide letter spacing, commonly around `1.5px`, `.12em`, or `.2em`.
- CTAs are pill or near-pill forms with strong tracking and generous horizontal padding.
- Component namespace is AEM-style `cmp-*`, mixed with utility classes.
- Breakpoint behavior is explicitly desktop-heavy from `1024px`, with mobile fallbacks below `767px`.
- Mosaic/card modules use fixed square tiles around `340px` and image-backed panels.
- Motion exists, but it is mostly opacity/transform reveal, not playful bounces.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Corporate Nocturne
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **dark editorial photography with a restrained Deloitte-green signal**으로 기억된다.
> **Code Complexity**: high — AEM component CSS, large responsive rules, mosaic grids, carousels, modals, and utility classes all coexist.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Deloitte Digital처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Open Sans", Calibri, Arial, sans-serif;
  font-weight: 300;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #000000; --fg: #D0D0CE; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #86BC25; }
```

**절대 하지 말아야 할 것 하나**: Deloitte green `#86BC25`를 큰 배경색으로 쓰지 말 것. 이 사이트의 green은 작은 신호이고, 주 무대는 black photography + grey typography다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.deloittedigital.com` |
| Fetched | 2026-05-03T15:26:49+0900 |
| Extractor | reused existing phase1 + CSS + HTML + screenshot bundle |
| HTML size | 423,594 bytes |
| CSS files | 18 non-empty files, 3,623,125 chars |
| Token prefix | `dd` inferred; no custom-property token graph found |
| Method | Existing phase1 JSON + CSS frequency + HTML/component inspection + screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Adobe Experience Manager style component site. HTML/CSS expose repeated `cmp-*`, `aem-Grid`, and content module classes.
- **Design system**: Deloitte Digital component layer - no resolved CSS variable token graph in phase1, but repeated color/font/layout primitives are present.
- **CSS architecture**:
  ```text
  AEM components      (.cmp-navbar, .cmp-btn, .cmp-tabs, .cmp-mosaic-grid)
  Utility layer       (desktop:text-*, font-light, tracking-letter-*, bg/text utilities)
  Legacy/bootstrap    (.modal, .modal-dialog, .btn-like patterns)
  Content modules     (hero, video, carousel, mosaic, tabs, forms)
  ```
- **Class naming**: BEM-ish AEM component classes plus Tailwind-escaped utility classes.
- **Default theme**: mixed, but the first-viewport brand impression is dark.
- **Font loading**: CSS declares Open Sans; fallback stack appears as `Open Sans, Calibri, sans-serif` and `Open Sans, Arial, sans-serif`.
- **Canonical anchor**: South Korea localized homepage is present in captured HTML (`/kr/en.html`).

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Open Sans` (open-source)
- **Code font**: system monospace fallback only
- **Weight normal / bold**: `300` / `700`

```css
:root {
  --dd-font-family:       "Open Sans", Calibri, Arial, sans-serif;
  --dd-font-family-code:  ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  --dd-font-weight-normal: 300;
  --dd-font-weight-bold:   700;
}
body {
  font-family: var(--dd-font-family);
  font-weight: var(--dd-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Open Sans** is already a practical open-source choice. Do not replace it with Inter just because Inter is common.
- If Open Sans is unavailable, use **Arial** only as a last fallback and compensate by reducing the luxury of the display scale: keep H1 at `80px` rather than `116px`.
- The important substitute behavior is not the family alone. Preserve `font-weight: 300` for body/editorial copy, wide uppercase tracking for labels, and 14px/24px body rhythm.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `desktop-h1` | 116px | 300 | 126px | 0 |
| `desktop-h2` | 80px | 300 | 94px | 0 |
| `desktop-h3` | 56px | 300 | 70px | 0 |
| `desktop-h4` | 40px | 300 | 50px | 0 |
| `desktop-h5` | 24px | 300 | 36px | 0 |
| `desktop-body-2-regular` | 14px | 300/400 | 24px | 0 |
| `mobile-h1` | 36px | 300 | 42px | 0 |
| `mobile-h2` | 26px | 300 | 34px | 0 |
| `mobile-body-1-regular` | 14px | 300/400 | 24px | 0 |
| `uppercase-label` | 12-16px | 300/700 | 22-36px | 1.5px / .12em / .2em |

> ⚠️ Key insight: the brand voice comes from light Open Sans plus large scale jumps. If body becomes 400 everywhere and labels lose tracking, the page stops feeling like Deloitte Digital.

### Principles
<!-- SOURCE: manual -->

1. Body text is light first. `300` appears as a measured default in phase1 and in many CSS rules.
2. Display sizes are oversized but not heavy. The 116px and 80px classes rely on scale, not black weight.
3. Uppercase labels and CTAs need tracking. The observed system uses `1.5px`, `.12em`, `.2em`, and similar expanded values.
4. The system tolerates many weights, but brand-critical surfaces should stay in 300/700/800 contrast rather than a smooth 400/500 SaaS ladder.
5. Line-height is generous: 14px body often sits at 24px, 56px display at 70px, and 80px display at 94px.
6. Do not compress the hero headline. The dark image needs airy line-height so the text can breathe over photography.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed)

| Token | Hex |
|---|---|
| `dd-green` | `#86BC25` |
| `dd-green-alt` | `#43B02A` |
| `dd-green-dark` | `#7BB421` |

### 06-2. Brand Dark Variant

> N/A - the captured CSS does not expose a clean dark-mode brand ramp. The dark impression is produced by black surfaces and photographic overlays.

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| `white` | `#FFFFFF` | - |
| `grey-10` | `#F3F3F3` | - |
| `grey-20` | `#E7E9E8` / `#E5E5E5` | - |
| `grey-30` | `#D0D0CE` | - |
| `grey-60` | `#75787B` / `#63666A` | - |
| `black` | - | `#000000` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Cyan | soft | `#A0DCFF` |
| Teal | standard | `#007680` |
| Teal | dark | `#005587` / `#005E86` |
| Mint | soft | `#9DD4CF` |
| Yellow-green | soft | `#E3E48D` |
| Aqua wash | pale | `#DDEFE8` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `dd.surface.dark` | `#000000` | hero overlay, dark nav/menu surfaces, high-contrast bands |
| `dd.surface.light` | `#FFFFFF` | cookie banner, modals, form surfaces, light content modules |
| `dd.text.on-dark` | `#D0D0CE` | muted grey typography over dark imagery |
| `dd.text.dark` | `#000000` | text on light surfaces and grey buttons |
| `dd.brand.signal` | `#86BC25` | Deloitte dot/brand accent, small active signals |
| `dd.border.light` | `#D0D0CE` / `#E7E9E8` | hairlines, tabs, dividers |

### 06-6. Semantic Alias Layer

> N/A - phase1 found `total_vars: 0`, so no trustworthy alias layer can be claimed. Use the semantic names above as guidebook aliases, not as extracted CSS variables.

### 06-7. Dominant Colors (actual CSS/HTML frequency)

| Token | Hex | Frequency signal |
|---|---:|---:|
| `black-short` | `#000` | 358 |
| `white-short` | `#fff` | 341 |
| `grey-30` | `#D0D0CE` | 268 |
| `black-long` | `#000000` | 109 |
| `transparent-black` | `#0000` | 66 |
| `cyan-soft` | `#A0DCFF` | 28 |
| `deloitte-green` | `#86BC25` | 28 |
| `grey-10` | `#F3F3F3` | 23 |
| `teal` | `#007680` | 22 |
| `grey-05` | `#F6F6F6` | 21 |

### 06-8. Color Stories
<!-- SOURCE: manual - top 4 only -->

**`{colors.black}` (`#000000`)** - The stage color. It appears as hero overlay, dark modules, dark navigation behavior, and contrast background. Deloitte Digital should feel like a dark editorial environment before it feels like a colorful agency page.

**`{colors.white}` (`#FFFFFF`)** - The service color for utility surfaces. Cookie banners, modals, and form bodies rely on white as a functional interruption rather than a brand mood.

**`{colors.grey-30}` (`#D0D0CE`)** - The real text mood. On dark photography, pure white would be too loud; this grey gives the headline and nav a restrained consultancy tone.

**`{colors.deloitte-green}` (`#86BC25`)** - The identity spark. It should appear as a small dot, a border/state accent, or a focused signal. Large green panels are not the captured homepage language.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `dd-space-8` | 8px | small gaps inside mosaic/card panels |
| `dd-space-16` | 16px | common grid and text spacing |
| `dd-space-20` | 20px | mosaic inner margin |
| `dd-space-24` | 24px | mobile/card/form interior rhythm |
| `dd-space-40` | 40px | desktop nav item spacing, section internals |
| `dd-space-56` | 56px | hero text side padding |
| `dd-space-64` | 64px | tabs and section padding |
| `dd-space-80` | 80px | major vertical section padding |
| `dd-space-100` | 100px | large section air |

**주요 alias**:
- `hero-x` -> 56px (hero text left/right padding)
- `section-y` -> 80px (large content bands)
- `mosaic-gap` -> 8px/20px (panel gap + inner margin)

### Whitespace Philosophy
<!-- SOURCE: manual -->

Deloitte Digital uses whitespace as a contrast device. The hero is visually dense because the image fills the stage, but text placement is sparse: logo, nav, eyebrow, headline, and CTA all float with enough distance to keep the page from becoming a campaign poster.

Below the hero, the system becomes modular and more operational. Mosaic tiles use fixed square dimensions and tight inner spacing, while tabs and content sections reserve 64-80px blocks for structural breathing room. The philosophy is "cinematic top, componentized below."

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `dd-radius-none` | 0 | dark panels, rectangular editorial modules |
| `dd-radius-xs` | .18rem | base AEM button container |
| `dd-radius-sm` | 5-6px | legacy modal/card surfaces |
| `dd-radius-md` | 8px | utility cards and soft containers |
| `dd-radius-lg` | 24px | larger utility modules |
| `dd-radius-pill` | 6.25em / 9999px | rounded CTA buttons |
| `dd-radius-circle` | 50% | icon/circular controls |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `none` | `none` | most brand chrome; dark/editorial surfaces avoid elevation |
| `mobile-fixed-btn` | `0 3px 6px #00000029` | fixed mobile clone button |
| `modal` | `0 3px 9px #00000080` / `0 5px 15px #00000080` | legacy modal surfaces |
| `deep-card` | multi-layer `#00000012` / `#0000000d` / `#0000000b` | rare rich card elevation |
| `inset-panel` | inset shadows with `#F3F3F3` or `#DDEFE8` | framed light/aqua panels |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `modal-rise` | `transform .3s ease-out` | modal entrance from translated state |
| `reveal-soft` | `transform .4s ease-out, opacity .4s ease-out` | content reveal |
| `image-drift` | `transform 1s` | large media transition |
| `opacity-fast` | `opacity .15s linear` | simple fade |
| `hover-background` | `background .2s` | subtle state change |
| `reduced-motion` | `@media (prefers-reduced-motion: reduce)` | accessibility branch present |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: common values include `1400px`, `1670px`, `1280px`, and `1024px`.
- **Grid type**: AEM `aem-Grid--12` plus CSS Grid/Flex utility output.
- **Column count**: 12-column AEM grid in markup; mosaic cells often map to default 3 / tablet 6 / phone 12 columns.
- **Gutter**: common gaps include `16px`, `24px`, `40px`, `56px`, `64px`, and larger editorial gaps.

### Hero

- **Pattern Summary**: first viewport dark image overlay + left editorial headline + uppercase eyebrow + rounded CTA.
- Layout: full-bleed image background with left text block; desktop nav overlays the hero.
- Background: photographic media, darkened by overlay; not a CSS-only gradient hero.
- **Background Treatment**: image-overlay with black atmosphere and mild magenta/cyan lighting from the source image.
- H1: visually around 40-56px in captured hero, while system display classes reach `116px` / weight `300`.
- Max-width: hero text wrapper exposes `max-width: 1512px` with `56px` horizontal padding.

### Section Rhythm

```css
section {
  padding: 80px 56px;
  max-width: 1400px;
}
```

### Card Patterns

- **Card background**: usually image-backed, `#FFFFFF`, `#F3F3F3`, or pale accent surfaces.
- **Card border**: often no border for image tiles; tabs/cards may use `1px solid #E7E9E8` or `#EDEDED`.
- **Card radius**: conservative; square mosaic modules dominate, while utility cards may use 8px.
- **Card padding**: 20px inside mosaic panels; 32-64px in larger modules.
- **Card shadow**: generally absent from brand chrome; shadows appear in modals, fixed mobile controls, and special panels.

### Navigation Structure

- **Type**: horizontal desktop nav with dropdown groups; mobile switches below `1024px`.
- **Position**: overlaid/static depending on hero state; captured hero shows nav over image.
- **Height**: visually around 90px in first viewport.
- **Background**: transparent over hero, black in opened/filter states.
- **Border**: minimal; dropdown/state cues rely on icons and color rather than heavy rules.

### Content Width

- **Prose max-width**: observed content caps around `580px`, `838px`, and `1024px` depending on module.
- **Container max-width**: `1400px` primary, with wider `1670px`/`1920px` responsive bounds.
- **Sidebar width**: not a homepage-defining pattern; dropdown and form panels matter more than persistent sidebars.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `max-width: 767px` | mobile typography, full-width buttons, reduced section padding |
| Tablet | `768px-1023px` | intermediate AEM grid/tablet classes |
| Desktop | `min-width: 1024px` | desktop nav items display, large type scale activates |
| Large | `min-width: 1400px` | larger nav margins and wide container behavior |
| XL | `min-width: 1670px` / `1920px` | oversized content caps and large-screen tuning |

### Touch Targets

- **Minimum tap size**: mobile sliders/buttons expose 44px+ control areas in several modules.
- **Button height (mobile)**: rounded buttons use `.5em-.75em` vertical padding; fixed mobile controls target full-width or 235px max buttons.
- **Input height (mobile)**: form system is present but exact rendered input height was not visually measured.

### Collapsing Strategy

- **Navigation**: `.navitem-d` hidden until `1024px`; `.navitem-m` visible from `0px` and hidden at desktop.
- **Grid columns**: AEM default/tablet/phone classes collapse 3-column desktop cards to 6/tablet and 12/phone spans.
- **Sidebar**: no persistent sidebar on the captured homepage.
- **Hero layout**: hero remains media-led; type and nav density reduce below desktop.

### Image Behavior

- **Strategy**: dynamic media images and video modules dominate; visual identity depends on real photography.
- **Max-width**: many media containers use `100%`.
- **Aspect ratio handling**: video and dynamic media components include 16:9 style containers and fixed crop behavior.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Rounded CTA**

| Property | Value |
|---|---|
| Selector | `.cmp-btn__rounded` |
| Radius | `6.25em` |
| Small padding | `.5em 2.5em` |
| Medium padding | `.75em 2.5em` |
| Large padding | `1em 2.5em` |
| Font weight | `var(--font-weight-bold)` |
| Text style | uppercase/letter-spaced on hero CTA |

```html
<div class="cmp-btn cmp-btn__rounded cmp-btn__rounded__md">
  <a class="button-container" href="#">READ MORE</a>
</div>
```

**Circular Icon Button**

| Property | Value |
|---|---|
| Selector | `.button-circle` |
| Size | `50px` x `50px` |
| Radius | `50%` |
| Border | `2px solid currentColor` |
| Background | `transparent` |

### Badges

Badges are not the homepage signature. When needed, use uppercase text with tracking and neutral/brand color sparingly.

```css
.dd-badge {
  font: 700 12px/22px "Open Sans", sans-serif;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #D0D0CE;
}
```

### Cards & Containers

**Mosaic Tile**

| Property | Value |
|---|---|
| Selector | `.cmp-mosaic-grid__cell` |
| Size | `340px` x `340px` |
| Inner panel | `.cmp-mosaic-grid__panel__inner` |
| Inner gap | `8px` |
| Inner margin | `20px` |
| Title | `2em / 40px` in vertical tab mosaic context |
| Body | `1em / 24px` |

```html
<a class="cmp-mosaic-grid__cell cmp-mosaic-grid__cell--image-tile" href="#">
  <div class="cmp-mosaic-grid__panel color-surface cmp-mosaic-grid__panel--with-gradient">
    <div class="cmp-mosaic-grid__panel__inner">
      <h3 class="cmp-mosaic-grid__title">Work title</h3>
      <p class="cmp-mosaic-grid__text">Short editorial summary.</p>
    </div>
  </div>
</a>
```

### Navigation

Desktop navigation is a horizontal set of text items and dropdown triggers:

- `.cmp-navbar .navitem-d` appears at `min-width: 1024px`.
- Desktop nav items use `margin-right: 26px`, increasing toward `40px` at wider sizes.
- Dropdown arrows rotate `180deg` on desktop open state.
- Mobile nav items are active below `1024px`.

### Inputs & Forms

The contact form exists in the captured HTML and uses AEM guide/form classes:

- Required labels include First Name, Last Name, Email Address, Company, and How can we help.
- Form error class observed: `.guideFieldError`.
- Modal/form surfaces use white backgrounds, black text, and conventional input density rather than the dark hero treatment.

### Hero Section

```html
<section class="hero">
  <nav class="cmp-navbar">...</nav>
  <div class="hero-text">
    <p class="dd-eyebrow">ARTIFICIAL INTELLIGENCE</p>
    <h1>5 questions to ask before integrating Gen AI into your marketing strategy</h1>
    <a class="dd-pill-cta">READ MORE <span aria-hidden="true">-></span></a>
  </div>
</section>
```

Implementation notes:

- Use a real editorial/technology image and dark overlay.
- Keep headline muted grey, not pure white.
- Use one rounded CTA with wide tracking.
- Let the Deloitte dot/green remain tiny.

### 13-2. Named Variants
<!-- SOURCE: manual -->

**rounded-outline-cta**

| Property | Value |
|---|---|
| Background | transparent |
| Radius | `6.25em` |
| Border | `1px solid currentColor` |
| Padding | `.75em 2.5em` |
| Use | hero contact button and secondary outline actions |

**grey-pill-primary**

| Property | Value |
|---|---|
| Background | `#D0D0CE` or related grey |
| Text | `#000000` |
| Radius | `9999px` / pill |
| Padding | approximately `18px 60px` in hero visual |
| Use | primary editorial CTA over dark image |

**mosaic-image-tile**

| Property | Value |
|---|---|
| Size | `340px` square |
| Surface | image-backed with gradient panel |
| Inner margin | `20px` |
| Title | `2em / 40px` |
| Use | work/insight tile grid |

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
black-glass-editorial-hero:
  description: "First viewport behaves like a dark consulting theater, not a flat SaaS hero."
  technique: "full-bleed editorial image + black overlay; foreground text uses #D0D0CE ({colors.grey-30}) over #000000 ({colors.black})"
  applied_to: ["{component.Hero Section}", "{component.Navigation}"]
  visual_signature: "photography supplies the atmosphere while the UI chrome almost disappears into the black stage"

muted-grey-projection-copy:
  description: "Hero and dark-surface copy is intentionally held below pure white."
  technique: "Open Sans weight 300; text color #D0D0CE ({colors.grey-30}) instead of #FFFFFF ({colors.white}); generous line-height such as 56px/70px and 80px/94px"
  applied_to: ["{component.Hero Section}", "{component.Badges}", "{component.Navigation}"]
  visual_signature: "copy reads like pale type on a dim projection screen rather than bright reversed-out marketing text"

letterspaced-pill-command:
  description: "Consulting actions are small typographic commands inside rounded geometry."
  technique: "text-transform uppercase; letter-spacing .12em-.2em or 1.5px; pill radius 6.25em/9999px; CTA padding around .75em 2.5em or 18px 60px"
  applied_to: ["{component.rounded-outline-cta}", "{component.grey-pill-primary}", "{component.Buttons}"]
  visual_signature: "READ MORE and CONTACT US feel measured and procedural, not button-like in a startup sense"

deloitte-green-single-signal:
  description: "Brand recognition is carried by one restrained green signal, never by a green surface system."
  technique: "reserve #86BC25 ({colors.deloitte-green}) for logo dot, small state cues, or selected accents; avoid flood fills"
  applied_to: ["{component.Navigation}", "{component.Badges}", "{component.Hero Section}"]
  visual_signature: "the page stays black/grey/white until a tiny Deloitte green mark confirms the identity"

aem-340-contact-sheet-mosaic:
  description: "Below-hero content turns into a square editorial contact sheet."
  technique: "cmp-mosaic-grid cells at 340px x 340px; 20px inner margin; 8px internal gap; image-backed or gradient panels; title around 2em/40px"
  applied_to: ["{component.mosaic-image-tile}", "{component.Cards & Containers}"]
  visual_signature: "content feels catalogued in fixed editorial tiles rather than arranged as generic three-card feature blocks"
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Advisory question or strategic claim, calm and direct | "5 questions to ask before integrating Gen AI into your marketing strategy" |
| Primary CTA | Short uppercase command with arrow | "READ MORE" |
| Secondary CTA | Direct contact intent | "CONTACT US" |
| Subheading | Service taxonomy language | "Customer Strategy", "Advertising", "Digital Commerce" |
| Tone | consultancy/editorial, not startup-casual | "What We Do", "Who We Are", "DD Insights" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Deloitte Digital - copy into your root stylesheet */
:root {
  /* Fonts */
  --dd-font-family:       "Open Sans", Calibri, Arial, sans-serif;
  --dd-font-family-code:  ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  --dd-font-weight-normal: 300;
  --dd-font-weight-bold:   700;

  /* Brand */
  --dd-color-brand-25:  #DDEFE8;
  --dd-color-brand-300: #9DD4CF;
  --dd-color-brand-500: #86BC25;
  --dd-color-brand-600: #43B02A;
  --dd-color-brand-900: #005587;

  /* Surfaces */
  --dd-bg-page:    #000000;
  --dd-bg-light:   #FFFFFF;
  --dd-bg-soft:    #F3F3F3;
  --dd-text:       #D0D0CE;
  --dd-text-dark:  #000000;
  --dd-text-muted: #75787B;
  --dd-border:     #D0D0CE;

  /* Key spacing */
  --dd-space-sm:  16px;
  --dd-space-md:  40px;
  --dd-space-lg:  80px;
  --dd-hero-x:    56px;

  /* Radius */
  --dd-radius-sm: 6px;
  --dd-radius-md: 8px;
  --dd-radius-pill: 9999px;
}

body {
  margin: 0;
  background: var(--dd-bg-page);
  color: var(--dd-text);
  font-family: var(--dd-font-family);
  font-weight: var(--dd-font-weight-normal);
}

.dd-hero {
  min-height: 800px;
  padding: 90px var(--dd-hero-x) 80px;
  background:
    linear-gradient(90deg, rgba(0,0,0,.78), rgba(0,0,0,.38)),
    var(--hero-image) center / cover no-repeat;
}

.dd-eyebrow,
.dd-pill-cta {
  text-transform: uppercase;
  letter-spacing: .2em;
}

.dd-eyebrow {
  font-size: 16px;
  line-height: 36px;
  color: var(--dd-text);
}

.dd-hero h1 {
  max-width: 760px;
  margin: 12px 0 26px;
  font-size: clamp(36px, 4vw, 56px);
  line-height: 1.18;
  font-weight: 300;
  color: var(--dd-text);
}

.dd-pill-cta {
  display: inline-flex;
  align-items: center;
  gap: 14px;
  min-height: 60px;
  padding: 0 60px;
  border-radius: var(--dd-radius-pill);
  background: var(--dd-border);
  color: var(--dd-text-dark);
  font-weight: 700;
  text-decoration: none;
}

.dd-mosaic-tile {
  width: 340px;
  height: 340px;
  display: grid;
  align-items: end;
  padding: 20px;
  background: #000000 center / cover no-repeat;
  color: #FFFFFF;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js - Deloitte Digital inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        dd: {
          black: '#000000',
          white: '#FFFFFF',
          grey30: '#D0D0CE',
          grey10: '#F3F3F3',
          green: '#86BC25',
          teal: '#007680',
          cyan: '#A0DCFF',
        },
      },
      fontFamily: {
        sans: ['Open Sans', 'Calibri', 'Arial', 'sans-serif'],
      },
      fontWeight: {
        light: '300',
        normal: '400',
        semibold: '600',
        bold: '700',
        extrabold: '800',
      },
      borderRadius: {
        pill: '9999px',
      },
      letterSpacing: {
        dd: '.2em',
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
| Brand primary | `{colors.deloitte-green}` | `#86BC25` |
| Background | `{colors.black}` | `#000000` |
| Text primary on dark | `{colors.grey-30}` | `#D0D0CE` |
| Text primary on light | `{colors.black}` | `#000000` |
| Light surface | `{colors.white}` | `#FFFFFF` |
| Soft surface | `{colors.grey-10}` | `#F3F3F3` |
| Accent cyan | `{colors.cyan-soft}` | `#A0DCFF` |
| Accent teal | `{colors.teal}` | `#007680` |

### Example Component Prompts

#### Hero Section

```text
Deloitte Digital 스타일 히어로 섹션을 만들어줘.
- 배경: full-bleed editorial technology photo + dark black overlay
- H1: Open Sans, 48-56px desktop, weight 300, line-height 1.18, color #D0D0CE
- Eyebrow: uppercase, letter-spacing .2em, 16px, color #D0D0CE
- CTA: pill, background #D0D0CE, text #000000, radius 9999px, padding 18px 60px
- Brand green #86BC25는 작은 dot/accent로만 사용
```

#### Card Component

```text
Deloitte Digital 스타일 mosaic insight tile을 만들어줘.
- 크기: 340px square
- 배경: real image 또는 #000000, 필요 시 dark gradient overlay
- 내부 여백: 20px, gap 8px
- 제목: Open Sans, 32px/40px, weight 300
- 본문: 16px/24px, color #D0D0CE or #FFFFFF
- hover: transform/opacity 정도만, shadow 과장 금지
```

#### Navigation

```text
Deloitte Digital 스타일 상단 네비게이션을 만들어줘.
- desktop 1024px 이상: horizontal nav, transparent over hero
- 링크: Open Sans, 14-16px, weight 300/400, color #D0D0CE
- dropdown arrow는 작은 회전 상태만 사용
- Contact CTA는 outline pill, letter-spaced uppercase
- active/brand accent는 #86BC25를 작게만 사용
```

### Iteration Guide

- **색상 변경 시**: black/white/grey/green의 역할을 분리한다. green을 배경으로 확장하지 않는다.
- **폰트 변경 시**: Open Sans 유지가 우선이다. Inter로 바꾸면 Deloitte Digital 특유의 corporate editorial 톤이 약해진다.
- **여백 조정 시**: hero는 넓게, mosaic은 조밀하게. 모든 섹션을 같은 3-card spacing으로 만들지 않는다.
- **새 컴포넌트 추가 시**: AEM `cmp-*` 식으로 모듈 경계를 분명히 하고, pill CTA와 square mosaic grammar를 우선 재사용한다.
- **다크 모드**: homepage의 dark는 theme toggle이 아니라 editorial photography shell이다. light UI 위에 invert만 하지 않는다.
- **반응형**: `767px`, `1024px`, `1400px`를 우선 기준으로 삼는다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use dark editorial photography as the first visual layer.
- Keep the main foreground text in muted grey `#D0D0CE` over dark hero areas.
- Use Deloitte green `#86BC25` as a small identity signal.
- Preserve Open Sans with light body/display weights.
- Use uppercase labels and CTAs with visible letter spacing.
- Build CTAs as generous pills, not rectangular SaaS buttons.
- Keep card/content grids modular and AEM-like, especially square mosaic tiles.
- Treat white surfaces as utility interruptions: cookie, modal, form, or content modules.

### ❌ DON'T

- 배경 전체를 `#86BC25`로 두지 말 것 - 대신 hero/shell은 `#000000` 또는 dark photo overlay 사용.
- 다크 hero 텍스트를 `#FFFFFF`로만 두지 말 것 - 대신 핵심 headline은 `#D0D0CE` 사용.
- light utility surface를 `#FDFCF8` 같은 warm cream으로 바꾸지 말 것 - 대신 `#FFFFFF` 또는 `#F3F3F3` 사용.
- 본문 텍스트를 전부 `#000000`로 고정하지 말 것 - dark surface에서는 `#D0D0CE`, light surface에서만 `#000000` 사용.
- Deloitte green 대신 generic AI purple `#667EEA` 또는 `#764BA2`를 쓰지 말 것 - brand signal은 `#86BC25` 사용.
- CTA를 sharp rectangle `border-radius: 0`으로 만들지 말 것 - rounded CTA는 `6.25em` 또는 `9999px` 사용.
- body 기본을 `font-weight: 400`으로 평평하게 만들지 말 것 - Deloitte Digital의 light editorial tone은 `font-weight: 300`이 핵심.
- 모든 카드에 `box-shadow: 0 20px 40px #00000040` 같은 큰 그림자를 넣지 말 것 - brand chrome은 대부분 flat이고 shadow는 제한적으로 사용.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No green flood** - Deloitte green is never the main page wash in the captured homepage grammar.
- **No candy gradient hero** - the first viewport is photographic and dark, not purple/blue generated gradient.
- **No bubbly startup cards** - 24px rounded feature cards are not the primary component language.
- **No heavy display default** - the system prefers scale and lightness before 700/800 headline force.
- **No generic 3-feature SaaS section** - content modules are AEM/mosaic/editorial, not symmetric icon cards.
- **No decorative emoji system** - icons are functional arrows, dropdowns, and component controls.
- **No persistent app sidebar** - this is a marketing/editorial consultancy site, not a dashboard.
- **No saturated multi-brand palette** - chromatic accents exist, but black/white/grey/green control the identity.
- **No excessive chrome shadow** - shadows are modal/control exceptions, not the page's depth model.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Cookie banner occlusion** - the available hero screenshot includes a privacy banner covering the lower first viewport, so lower hero CTA and fold spacing are partially inferred.
- **Single localized homepage capture** - captured HTML references the South Korea localized surface (`/kr/en.html`); global pages and regional variants may differ.
- **No custom-property token graph** - phase1 found `total_vars: 0`, so `colors`, `typography`, and `components` objects are guidebook aliases derived from CSS usage, not real CSS variable names.
- **Form states not fully rendered** - form classes and labels are present in HTML, but visual validation, loading, and success states were not interactively exercised.
- **Dark-mode mapping not proven** - dark impression comes from hero/media treatments; no systematic theme toggle or full dark token ramp was verified.
- **Motion behavior partially inferred** - CSS transition values were inspected, but JavaScript-triggered carousel, video, scroll reveal, and interaction timing were not fully replayed.
- **Logo and third-party color pollution** - frequency counts may include logo assets, embeds, and utility/framework output; Deloitte green was selected by brand role, not by raw frequency alone.
- **Responsive visual QA limited** - CSS breakpoints were extracted, but mobile/tablet screenshots were not freshly rendered in this run.
- **Component coverage is homepage-biased** - tabs, mosaic grids, nav, buttons, modals, forms, and cookie UI are visible in the captured bundle; deeper work/case-study templates may add variants.
