---
schema_version: 3.2
slug: axiom
service_name: Axiom
site_url: https://axiom.co
fetched_at: 2026-05-03T06:15:29Z
default_theme: dark
brand_color: "#DA5C2C"
primary_font: BerkeleyMono
font_weight_normal: 400
token_prefix: axiom

bold_direction: Terminal Precision
aesthetic_category: Industrial Minimalism
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Tailwind v3 utility build plus 211 CSS variables and explicit Radix-style color ramps are visible in production CSS."

colors:
  surface-black: "#000000"
  surface-raised: "#101010"
  text-primary: "#FFFFFF"
  text-muted: "#9CA3AF"
  border-subtle: "#404040"
  brand-orange: "#DA5C2C"
  action-orange: "#F76B15"
  chart-blue: "#2563EB"
typography:
  display: "BerkeleyMono"
  body: "Inter"
  code: "BerkeleyMono"
  ladder:
    - { token: hero, size: "clamp(32px, 4vw, 56px)", weight: 700, tracking: "0" }
    - { token: h2, size: "40px", weight: 700, tracking: "0" }
    - { token: body, size: "16px", weight: 400, tracking: "0" }
    - { token: micro, size: "12px", weight: 600, tracking: "0.02em" }
  weights_used: [400, 500, 600, 700, 800, 900]
  weights_absent: [300]
components:
  button-primary: { bg: "{colors.action-orange}", color: "{colors.text-primary}", radius: "4px", padding: "14px 18px" }
  button-secondary-terminal: { bg: "transparent", color: "{colors.text-primary}", border: "1px solid #404040", radius: "4px" }
  nav-demo-button: { bg: "{colors.text-primary}", color: "#101010", radius: "4px", padding: "12px 18px" }
  terminal-panel: { bg: "#101010", border: "1px solid #404040", radius: "8px" }
---

# DESIGN.md — Axiom

---

## 00. Direction & Metaphor
<!-- SOURCE: manual -->

### Narrative

Axiom does not sell observability with the usual cloud-SaaS softness. The first viewport behaves like a black terminal wall in a dark operations room: hard edges, a monospace headline, command-line fragments, dense chevron texture, and a product console rising from the bottom. The page is not trying to feel friendly first. It is trying to feel operationally inevitable.

The dominant field is #000000 (`{colors.surface-black}`), not dark navy, not charcoal-blue. That matters. OLED pure black can feel like a hole, but here it is used like an unlit server bay: the hardware disappears, then the command output becomes the room. The white BerkeleyMono headline is not typography laid on top of the page; it is the page behaving like an interface. The page's strongest color is not spread everywhere; #DA5C2C (`{colors.brand-orange}`) and #F76B15 (`{colors.action-orange}`) are reserved for conversion and small heat points. There is no second brand wash. Blue #2563EB (`{colors.chart-blue}`) appears as telemetry inside the product visualization, so the product owns the second chromatic role.

The visual metaphor is an observability cockpit built out of terminal primitives. Copy begins with hash-tagged labels like `#LAUNCHED`, `#PLATFORM`, `#SIGNALS`; sections use code-like language; the hero pattern repeats chevrons like a log printer feeding events sideways across the dark. It is closer to an air-traffic control wall than a SaaS landing page: the field is black, the labels are clipped and procedural, and the colored traces only matter because they are data.

The design keeps the product close to the story. Dashboard chrome, bars, nav rails, and query surfaces are visible instead of hiding behind abstract illustrations. The hero screenshot does not sit politely in a rounded marketing card; it rises from the fold like a rack-mounted console being slid into view. Photography is absent, and that absence is part of the identity: shadow belongs to the product panel, not to lifestyle imagery.

Axiom's craft is mostly negative. No glowing purple gradient, no rounded neumorphic dashboard card, no pastel cloud layer, no friendly blob mascot, no orange section background. When it needs polish, it uses texture, thin borders, clipped panels, and monospace rhythm. The result is a dark engineering stage where product evidence gets the light, and the interface feels less like a brochure than a live oscilloscope trace frozen at the moment the signal becomes legible.

### Key Characteristics

- Black terminal canvas: #000000 page background with #FFFFFF primary text.
- Monospace-first brand voice: BerkeleyMono carries hero, CTAs, labels, and code-like microcopy.
- Orange is conversion heat only: #DA5C2C / #F76B15 should stay scarce and decisive.
- Blue belongs to data: #2563EB and blue ramp colors are chart/product signals, not broad brand wash.
- Chevron flow texture: repeated rightward glyphs create motion without animation-heavy spectacle.
- Product panel emerges from below the fold: dashboard evidence anchors the SaaS promise.
- Small-radius engineering chrome: 4px buttons and 8px panels, never bubbly.
- Thin gray borders: #404040 / #D4D4D4 are structural rails in place of soft shadows.
- Hash-label section language: `#LAUNCHED`, `#SIGNALS`, `#ARCHITECTURE` turn marketing into terminal output.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Terminal Precision
> **Aesthetic Category**: Industrial Minimalism
> **Signature Element**: 이 사이트는 **terminal-black hero with chevron telemetry flow**으로 기억된다.
> **Code Complexity**: high — Tailwind utilities, 211 variables, texture patterns, product screenshots, responsive nav, and multi-section product storytelling combine into a dense implementation.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Axiom처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter", ui-sans-serif, system-ui, -apple-system, sans-serif;
  font-weight: 400;
}
.hero-title,
.terminal-label,
.cta {
  font-family: "BerkeleyMono", ui-monospace, SFMono-Regular, Menlo, monospace;
  font-weight: 700;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #000000; --fg: #FFFFFF; --muted: #9CA3AF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #DA5C2C; --action: #F76B15; --data-blue: #2563EB; }
```

**절대 하지 말아야 할 것 하나**: Axiom을 일반적인 blue-gradient SaaS로 만들지 말 것. 이 사이트의 신뢰감은 #000000 terminal field + BerkeleyMono + sparse orange CTA에서 온다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://axiom.co` |
| Fetched | 2026-05-03T06:15:29Z |
| Extractor | reused existing phase1 artifacts |
| HTML size | 308853 bytes (Next.js SSR/static payload) |
| CSS files | 1 external CSS, 114462 chars |
| Token prefix | `axiom` (derived; production CSS uses unprefixed Radix-style ramps like `--gray-01`) |
| Method | Existing CSS/HTML/phase1 JSON + screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js marketing site with Tailwind CSS v3.4.4 output.
- **Design system**: Radix-style color ramps in production CSS; variables are unprefixed families such as `--gray-*`, `--blue-*`, `--orange-*`, `--purple-*`, `--green-*`, `--red-*`, `--teal-*`.
- **CSS architecture**:
  ```text
  core ramp      (--gray-01, --orange-09, --blue-09)    raw hex values
  utility layer  Tailwind generated classes             spacing/display/state composition
  component      React/Next markup + utility bundles     nav, menu, cards, hero, product panels
  ```
- **Class naming**: Tailwind utility classes plus generated component class composition.
- **Default theme**: dark first in the visible hero, although CSS includes light and dark ramp definitions.
- **Font loading**: local `@font-face` for BerkeleyMono regular/bold/italic; Inter comes from system/web stack declaration.
- **Canonical anchor**: black hero with Axiom logo, product nav, orange demo CTA, and product dashboard screenshot.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `BerkeleyMono` (commercial/proprietary local webfont in site assets)
- **Body font**: `Inter` system/web stack
- **Code font**: `BerkeleyMono`
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --axiom-font-family:       Inter, ui-sans-serif, system-ui, -apple-system, sans-serif;
  --axiom-font-family-code:  BerkeleyMono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  --axiom-font-weight-normal: 400;
  --axiom-font-weight-bold:   700;
}
body {
  font-family: var(--axiom-font-family);
  font-weight: var(--axiom-font-weight-normal);
}
.terminal,
.hero-title,
code {
  font-family: var(--axiom-font-family-code);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **BerkeleyMono** — use **IBM Plex Mono** or **JetBrains Mono** when the commercial font is unavailable.
- **Substitution correction** — keep letter-spacing at `0`; do not add negative tracking. Axiom's mono voice depends on square, explicit terminal spacing.
- **Weight correction** — use 700 for hero and CTA labels. Avoid 600-only mono headings; they lose the blunt operational authority of the source.
- **Body fallback** — Inter can be replaced by system UI only in paragraph copy. Do not replace hero/headline mono with Inter.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| Hero display | `clamp(32px, 4vw, 56px)` | 700 | ~1.12 | `0` |
| Section headline | `40px` | 700 | ~1.15 | `0` |
| Card headline | `24px` | 700 | ~1.2 | `0` |
| Body | `16px` | 400 | 1.5 | `0` |
| Muted body | `14px` | 400 | 1.45 | `0` |
| Terminal label | `12px` | 600/700 | 1.2 | `0.02em` |
| CTA | `14px` | 700 | 1 | `0` |

> ⚠️ Key insight: Axiom's typography is not a neutral Inter SaaS system. BerkeleyMono is the brand surface; Inter is the support layer.

### Principles
<!-- SOURCE: manual -->

1. Hero text must be mono. If the hero is set in Inter, the page stops feeling like Axiom.
2. Use weight 700 for the main mono moments. The site uses blunt emphasis instead of elegant optical tracking.
3. Body copy can be Inter at 400, but labels, tags, CTAs, and code-adjacent UI should return to BerkeleyMono.
4. Keep letter-spacing mostly at `0`. The terminal feel comes from native mono spacing, not designer-tight display typography.
5. Uppercase/hash labels are navigational rhythm, not decoration. Treat `#SIGNALS` and `#ARCHITECTURE` as section anchors.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (orange, 12 steps)
<!-- orange core ramp from CSS -->

| Token | Hex |
|---|---|
| `--orange-01` | `#FEFCFB` |
| `--orange-02` | `#FFF7ED` |
| `--orange-03` | `#FFEFD6` |
| `--orange-04` | `#FFDFB5` |
| `--orange-05` | `#FFD19A` |
| `--orange-06` | `#FFC182` |
| `--orange-07` | `#F5AE73` |
| `--orange-08` | `#EC9455` |
| `--orange-09` | `#F76B15` |
| `--orange-10` | `#EF5F00` |
| `--orange-11` | `#CC4E00` |
| `--orange-12` | `#582D1D` |

### 06-2. Brand Dark Variant
<!-- SOURCE: auto -->

| Token | Hex |
|---|---|
| `--orange-01-dark` | `#17120E` |
| `--orange-02-dark` | `#1E160F` |
| `--orange-03-dark` | `#331E0B` |
| `--orange-09-dark` | `#F76B15` |
| `--orange-11-dark` | `#FF8B3E` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light | Dark / visible hero role |
|---|---|---|
| `00` | `#FFFFFF` | `#000000` page field |
| `01` | `#FCFCFC` | `#111111` raised black |
| `02` | `#F9F9F9` | `#191919` secondary surface |
| `03` | `#F0F0F0` | `#222222` panel fill |
| `04` | `#E8E8E8` | `#2A2A2A` subtle divide |
| `05` | `#E0E0E0` | `#313131` muted border |
| `06` | `#D9D9D9` | `#3A3A3A` border |
| `07` | `#CECECE` | `#484848` strong border |
| `08` | `#BBBBBB` | `#606060` muted glyph |
| `09` | `#8D8D8D` | `#6E6E6E` secondary text |
| `10` | `#838383` | `#7B7B7B` tertiary text |
| `11` | `#646464` | `#B4B4B4` muted-on-dark text |
| `12` | `#202020` | `#EEEEEE` primary-on-dark text |
| `13` | `#0C0C0C` | `#FFFFFF` white text |

### 06-4. Accent Families
<!-- SOURCE: auto -->

| Family | Key step | Hex |
|---|---|---|
| Blue | `--blue-09` | `#0090FF` |
| Blue chart observed | frequency candidate | `#2563EB` |
| Green | `--green-09` | `#29A383` |
| Purple | `--purple-09` | `#6E56CF` |
| Teal | `--teal-09` | `#12A594` |
| Red | `--red-09` | `#E5484D` |

### 06-5. Semantic
<!-- SOURCE: auto+manual -->

| Token | Hex | Usage |
|---|---|---|
| `{colors.surface-black}` | `#000000` | page/hero background |
| `{colors.surface-raised}` | `#101010` | dashboard and dark panel surfaces |
| `{colors.text-primary}` | `#FFFFFF` | hero/nav primary text |
| `{colors.text-muted}` | `#9CA3AF` | muted descriptions and placeholders |
| `{colors.border-subtle}` | `#404040` | buttons, panels, dividers |
| `{colors.brand-orange}` | `#DA5C2C` | observed warm brand/CTA candidate |
| `{colors.action-orange}` | `#F76B15` | orange ramp action anchor |
| `{colors.chart-blue}` | `#2563EB` | product chart/data bars |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto+manual -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--axiom-bg-page` | `#000000` | visible marketing canvas |
| `--axiom-bg-panel` | `#101010` | product surface/chrome |
| `--axiom-text` | `#FFFFFF` | primary on black |
| `--axiom-text-muted` | `#9CA3AF` | descriptive copy |
| `--axiom-border` | `#404040` | thin terminal rails |
| `--axiom-action` | `#F76B15` | primary CTA |
| `--axiom-data-blue` | `#2563EB` | charts, product evidence |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---|---:|
| transparent | `#00000000` | 29 |
| white | `#FFFFFF` | 23 |
| dark slate text | `#111827` | 6 |
| near black | `#171717` | 6 |
| gray muted | `#6B7280` | 6 |
| light gray | `#D4D4D4` | 6 |
| translucent white | `#FFFFFF50` | 6 |
| placeholder gray | `#9CA3AF` | 5 |
| blue data | `#2563EB` | 4 |
| brand warm | `#DA5C2C` | 4 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.surface-black}` (`#000000`)** — The stage. It turns the page into a terminal and lets the product screenshots read as operational evidence instead of decorative mockups.

**`{colors.text-primary}` (`#FFFFFF`)** — The command output. It is used bluntly, with no off-white warmth, because the brand wants crisp legibility and engineering confidence.

**`{colors.action-orange}` (`#F76B15`)** — The conversion heat. Use it for primary CTAs and small high-intent moments; if orange spreads across backgrounds, the system loses discipline.

**`{colors.chart-blue}` (`#2563EB`)** — The data signal. It should appear inside product visuals, charts, and telemetry affordances rather than replacing orange as the brand action color.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--axiom-space-xs` | `8px` | nav gaps, micro controls |
| `--axiom-space-sm` | `12px` | button inner rhythm |
| `--axiom-space-md` | `16px` | card copy, grid gutters |
| `--axiom-space-lg` | `24px` | stacked text blocks |
| `--axiom-space-xl` | `40px` | hero copy to CTA separation |
| `--axiom-space-2xl` | `64px` | section bands |
| `--axiom-space-3xl` | `96px` | major homepage sections |

**주요 alias**:
- `container-x` → `22px` to `32px` responsive page padding.
- `hero-top` → large vertical offset below nav so the headline feels like command output in an empty terminal.
- `dashboard-overlap` → product panel starts near the lower edge of the first viewport.

### Whitespace Philosophy
<!-- SOURCE: manual -->

Axiom uses negative space as terminal silence. The hero leaves a large black field around the headline, then fills the right side with low-contrast chevrons so the emptiness still feels computational. This is not airy lifestyle spacing; it is deliberate operational blankness before the data arrives.

Below the hero, spacing becomes denser. Product panels, customer proof, and use-case cards can sit tighter because the brand has already established confidence. The rhythm is "wide black command line, then dense telemetry."

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `--axiom-radius-button` | `4px` | primary/secondary CTAs, nav demo button |
| `--axiom-radius-panel` | `8px` | product dashboard panels |
| `--axiom-radius-card` | `8px` | use-case and resource cards |
| `--axiom-radius-pill` | `999px` | rare badges only; not the dominant shape |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `none` | `none` | most nav/buttons/cards; border carries structure |
| `panel-depth` | `0 16px 60px rgba(0,0,0,.45)` | product screenshot/panel separation |
| `popover` | `0 20px 60px rgba(0,0,0,.5)` | nav dropdowns or menus |

Pattern: Axiom does not use soft SaaS elevation as a primary visual language. Thin borders, black surfaces, and screenshot contrast do most of the work.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `--axiom-transition-fast` | `150ms ease` | nav links, hover borders |
| `--axiom-transition-base` | `200ms ease` | buttons/cards |
| `--axiom-transition-slow` | `300ms ease` | menu disclosure and panel reveals |

Motion should feel like interface response, not brand entertainment. Prefer opacity, border-color, and subtle transform changes over springy bounces.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: approximately `1240px` for primary marketing content.
- **Grid type**: Tailwind flex/grid utilities; responsive CSS Grid for card/use-case sections.
- **Column count**: 1 column on mobile, 2 columns for narrative/product blocks, 3-4 columns for dense feature/resource groups.
- **Gutter**: `16px` to `24px` in dense grids; larger section gaps at `40px+`.

### Hero
- **🆕 Pattern Summary**: `~80vh + black terminal field + left mono H1 + dual CTA + right chevron telemetry texture + product panel below`
- Layout: left-aligned copy block with visual texture occupying the right half; dashboard panel begins at bottom.
- Background: `#000000` solid, with low-contrast repeating chevrons.
- **🆕 Background Treatment**: `glyph-texture` using repeated rightward chevrons over black; perceived as log/data flow.
- H1: `clamp(32px, 4vw, 56px)` / weight `700` / tracking `0`.
- Max-width: copy block around `720px`, full hero container around `1240px`.

### Section Rhythm
```css
section {
  padding: 64px 22px;
  max-width: 1240px;
}
@media (min-width: 1024px) {
  section { padding-block: 96px; }
}
```

### Card Patterns
- **Card background**: `#101010` or near-black on dark sections; white/light cards appear in lower content contexts.
- **Card border**: `1px solid #404040` on dark chrome.
- **Card radius**: `8px`.
- **Card padding**: `24px` to `32px`.
- **Card shadow**: minimal; product panels may use dark depth shadow.

### Navigation Structure
- **Type**: horizontal desktop nav with dropdown groups; collapsed mobile menu likely below tablet.
- **Position**: top static/sticky marketing header with announcement bar above.
- **Height**: announcement ~40px, nav ~72px.
- **Background**: black in first viewport.
- **Border**: thin low-contrast divider under announcement.

### Content Width
- **Prose max-width**: `640px` to `760px`.
- **Container max-width**: `1240px`.
- **Sidebar width**: not a core homepage pattern; product/docs surfaces may use side navigation separately.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `<640px` | single-column content, compressed nav, stacked CTAs |
| Tablet | `768px` | two-column opportunities begin; larger type and gaps |
| Desktop | `1024px` | full nav, hero texture/product composition, multi-card grids |
| Wide | `1240px` / `1280px` | max-width lock, richer grid density |
| Large | `1440px` / `1536px` | wide-screen polish without stretching prose |

### Touch Targets
- **Minimum tap size**: target `44px` on mobile.
- **Button height (mobile)**: roughly `40px` to `48px`.
- **Input height (mobile)**: insufficient direct evidence on homepage; assume `44px+` from Tailwind form conventions.

### Collapsing Strategy
- **Navigation**: desktop horizontal nav collapses into mobile menu below tablet.
- **Grid columns**: 3-4 column feature grids collapse to 2 and then 1.
- **Sidebar**: not central on homepage.
- **Hero layout**: headline and CTAs remain first; texture/dashboard crop or stack below.

### Image Behavior
- **Strategy**: responsive Next.js optimized images for product/news/customer media.
- **Max-width**: `100%`.
- **Aspect ratio handling**: dashboard/product screenshots are cropped/framed by parent panels; editorial thumbnails use fixed aspect boxes.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA**

| Property | Value |
|---|---|
| Background | `#F76B15` / observed warm `#DA5C2C` |
| Text | `#FFFFFF` |
| Font | `BerkeleyMono`, 14px, 700 |
| Radius | `4px` |
| Padding | `14px 18px` |
| Hover | darker orange or slight brightness shift |

```html
<a class="axiom-button axiom-button-primary">Book a demo</a>
```

**Secondary terminal CTA**

| Property | Value |
|---|---|
| Background | transparent |
| Border | `1px solid #404040` |
| Text | `#FFFFFF` / muted white |
| Radius | `4px` |
| Pattern | label plus right arrow |

### Badges

Hash labels are the real badge system.

| Pattern | Spec |
|---|---|
| Text | `#LAUNCHED`, `#PLATFORM`, `#SIGNALS`, `#ARCHITECTURE` |
| Font | BerkeleyMono |
| Case | uppercase |
| Color | white or muted gray depending context |
| Role | section identity, terminal prompt, announcement anchor |

### Cards & Containers

Cards should feel like panels in an engineering console.

| Property | Value |
|---|---|
| Fill | `#101010` on dark sections |
| Border | `1px solid #404040` |
| Radius | `8px` |
| Shadow | none or dark-only product depth |
| Hover | border-color lift, no playful scale bounce |

### Navigation

Desktop nav uses white logo, compact mono-ish labels, dropdown chevrons, and separated conversion actions. The right side hierarchy is Login, Sign up, then the high-contrast white "Book a demo" button.

### Inputs & Forms

Homepage evidence is limited. Reconstruct forms as terminal-like controls: black or near-black fill, `1px solid #404040`, 4px radius, Inter body text, BerkeleyMono labels where code-adjacent, and blue/orange only for state feedback.

### Hero Section

The hero is the signature component: a command prompt cue (`~/`), a large BerkeleyMono heading, short muted copy, dual CTAs, chevron telemetry texture, and product dashboard proof emerging at the fold. The dashboard must not be a generic abstract SaaS mockup; it needs visible bars, query chrome, and dense telemetry.

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-primary-orange**

| Property | Value |
|---|---|
| Token | `{components.button-primary}` |
| Use | main conversion CTA |
| Background | `#F76B15` or `#DA5C2C` |
| Radius | `4px` |
| State | hover darkens, focus ring should stay accessible on black |

**button-secondary-terminal**

| Property | Value |
|---|---|
| Token | `{components.button-secondary-terminal}` |
| Use | "Sign up for free" secondary hero action |
| Background | transparent |
| Border | `1px solid #404040` |
| State | hover border becomes lighter gray |

**button-nav-demo**

| Property | Value |
|---|---|
| Token | `{components.nav-demo-button}` |
| Use | top-right desktop conversion |
| Background | `#FFFFFF` |
| Text | `#101010` |
| Radius | `4px` |

**panel-terminal-dashboard**

| Property | Value |
|---|---|
| Token | `{components.terminal-panel}` |
| Use | product screenshot frame |
| Background | `#101010` |
| Border | `1px solid #404040` |
| Visual | blue bars, dark chrome, thin rails |

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
chevron-telemetry-field:
  description: "Hero texture turns repeated terminal glyphs into event-flow atmosphere."
  technique: "low-contrast repeated '>' glyph pattern over #000000 /* {colors.surface-black} */, visually denser toward the right side of the hero"
  applied_to: ["{component.hero}", "hero background"]
  visual_signature: "A sideways stream of logs crosses the black field without becoming an illustration or gradient."

hash-prompt-sectioning:
  description: "Marketing section labels behave like terminal prompts instead of editorial eyebrows."
  technique: "uppercase #LABEL copy in BerkeleyMono, ~12px, 600/700 weight, 0.02em tracking, white or muted gray on black"
  applied_to: ["announcement", "nav mega menu", "feature sections"]
  visual_signature: "The page reads as organized machine output: #LAUNCHED, #PLATFORM, #SIGNALS, #ARCHITECTURE."

orange-scarcity-cta:
  description: "Orange is held back as conversion heat, never expanded into a brand wash."
  technique: "#F76B15 /* {colors.action-orange} */ and #DA5C2C /* {colors.brand-orange} */ restricted to primary CTA and small emphasis; no orange section backgrounds"
  applied_to: ["{components.button-primary}", "{components.nav-demo-button}", "conversion states"]
  visual_signature: "One warm action punctures the black terminal interface like a live commit indicator."

fold-rising-terminal-panel:
  description: "The product panel enters as proof at the fold instead of as a decorative mockup."
  technique: "#101010 /* {colors.surface-raised} */ dashboard chrome, 1px solid #404040 /* {colors.border-subtle} */, 8px radius, dark depth shadow, clipped by the hero fold"
  applied_to: ["{components.terminal-panel}", "{component.hero}"]
  visual_signature: "A rack-mounted observability console slides up from the bottom edge before feature copy begins."

blue-as-telemetry-not-brand:
  description: "Blue is reserved for data marks inside the product visualization."
  technique: "#2563EB /* {colors.chart-blue} */ appears in bars/charts/product evidence while CTA ownership stays orange"
  applied_to: ["{components.terminal-panel}", "product charts", "dashboard bars"]
  visual_signature: "Blue reads as signal amplitude, not as the company's marketing color."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | direct engineering promise, mono, no metaphor overload | "Observability re-invented for high-scale engineering teams" |
| Primary CTA | sales-forward, short | "Book a demo" |
| Secondary CTA | developer self-serve | "Sign up for free" |
| Section label | hash-prefixed terminal taxonomy | `#SIGNALS` |
| Tone | operational, infrastructure-literate, scale-oriented | "logs, metrics, traces, and events" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Axiom — copy into your root stylesheet */
:root {
  /* Fonts */
  --axiom-font-family:       Inter, ui-sans-serif, system-ui, -apple-system, sans-serif;
  --axiom-font-family-code:  BerkeleyMono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  --axiom-font-weight-normal: 400;
  --axiom-font-weight-bold:   700;

  /* Brand */
  --axiom-color-brand-25:  #FEFCFB;
  --axiom-color-brand-300: #FFC182;
  --axiom-color-brand-500: #F76B15;
  --axiom-color-brand-600: #DA5C2C;
  --axiom-color-brand-900: #582D1D;

  /* Surfaces */
  --axiom-bg-page:    #000000;
  --axiom-bg-panel:   #101010;
  --axiom-text:       #FFFFFF;
  --axiom-text-muted: #9CA3AF;
  --axiom-border:     #404040;
  --axiom-data-blue:  #2563EB;

  /* Key spacing */
  --axiom-space-sm:  12px;
  --axiom-space-md:  16px;
  --axiom-space-lg:  24px;
  --axiom-space-xl:  40px;

  /* Radius */
  --axiom-radius-sm: 4px;
  --axiom-radius-md: 8px;
}

body {
  background: var(--axiom-bg-page);
  color: var(--axiom-text);
  font-family: var(--axiom-font-family);
}

.axiom-hero-title,
.axiom-terminal-label,
.axiom-button {
  font-family: var(--axiom-font-family-code);
}

.axiom-button-primary {
  background: var(--axiom-color-brand-500);
  color: #FFFFFF;
  border-radius: var(--axiom-radius-sm);
  padding: 14px 18px;
  font-weight: 700;
}

.axiom-panel {
  background: var(--axiom-bg-panel);
  border: 1px solid var(--axiom-border);
  border-radius: var(--axiom-radius-md);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Axiom-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        axiom: {
          black: '#000000',
          panel: '#101010',
          text: '#FFFFFF',
          muted: '#9CA3AF',
          border: '#404040',
          orange: '#F76B15',
          warm: '#DA5C2C',
          blue: '#2563EB',
        },
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui'],
        mono: ['BerkeleyMono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
        semibold: '600',
        bold: '700',
      },
      borderRadius: {
        axiom: '4px',
        panel: '8px',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

- Page background: `#000000`
- Raised panel: `#101010`
- Primary text: `#FFFFFF`
- Muted text: `#9CA3AF`
- Border: `#404040`
- Primary action: `#F76B15`
- Observed warm brand accent: `#DA5C2C`
- Data/chart blue: `#2563EB`

### Prompt

Build a dark terminal-first SaaS marketing page inspired by Axiom. Use a pure black `#000000` canvas, white `#FFFFFF` mono hero typography, sparse orange `#F76B15` primary CTAs, thin gray `#404040` borders, and a product dashboard panel with blue `#2563EB` data bars. The hero should feel like command-line observability: hash labels, a `~/` prompt cue, a right-side chevron telemetry texture, and a product screenshot/panel rising from the fold. Keep radius small at `4px` for buttons and `8px` for panels. Avoid purple gradients, bubbly cards, and generic SaaS illustration.

### Implementation Notes

- Use Inter for body and BerkeleyMono or a close mono substitute for brand surfaces.
- Let black dominate; do not brighten the whole page into slate.
- Use orange only for high-intent actions.
- Make the dashboard/product visual concrete: nav rails, bars, logs, queries, or traces.
- Use thin borders more than shadows.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO

- Use `#000000` as the primary hero/page background.
- Set hero and terminal labels in BerkeleyMono or a close mono substitute.
- Keep primary CTA orange: `#F76B15` or observed warm `#DA5C2C`.
- Use `#FFFFFF` for primary text on the black hero.
- Use `#9CA3AF` / gray ramp values for muted explanatory text.
- Use `#404040` thin borders for terminal panels and secondary buttons.
- Put `#2563EB` in charts/data bars/product evidence.
- Use hash-prefixed labels to structure sections.

### DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 hero/page는 `#000000` 사용.
- 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — dark hero primary text는 `#FFFFFF` 사용.
- primary CTA를 `#2563EB` blue로 두지 말 것 — action은 `#F76B15` 또는 `#DA5C2C` 사용.
- 전체 배경을 `#0F172A` slate/navy로 바꾸지 말 것 — Axiom의 첫인상은 `#000000` terminal black.
- muted copy를 `#6B7280`만으로 낮추지 말 것 — dark hero에서는 `#9CA3AF` 또는 `#B4B4B4` 계열 사용.
- panel border를 `#E5E7EB` light gray로 두지 말 것 — dark chrome에서는 `#404040` / `#3A3A3A` 사용.
- chart/data bars를 `#DA5C2C` orange로 칠하지 말 것 — product data signal은 `#2563EB` blue 사용.
- body 전체를 BerkeleyMono로 만들지 말 것 — body는 Inter, brand/display/control은 BerkeleyMono.
- hero title을 Inter 또는 system sans로 만들지 말 것 — BerkeleyMono 계열이 핵심.
- border-radius를 `16px` 이상으로 키우지 말 것 — buttons `4px`, panels `8px` 유지.

### 🚫 What This Site Doesn't Use
<!-- SOURCE: manual -->

- No purple-blue gradient hero background.
- No pastel SaaS illustration as the primary proof.
- No glassmorphic cards as the main component language.
- No large rounded pill system except rare badges.
- No soft beige/off-white editorial warmth in the first viewport.
- No playful emoji/icon confetti.
- No heavy multi-layer colorful shadows.
- No decorative customer-logo color pollution in the core palette.
- No lifestyle photography as the primary brand signal.
- No smooth luxury serif typography.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- Cookie banner occludes the lower-left hero screenshot, so dashboard panel details were interpreted from visible portions and HTML/CSS evidence rather than a fully clean viewport.
- CSS is minified Tailwind output; exact component ownership is inferred from visual structure and utility patterns, not from source React component names.
- Typography scale values are reconstructed from screenshot proportions and CSS family/weight evidence because phase1 `typography.json` did not extract a complete scale map.
- The CSS includes both light and dark color ramps; this guide prioritizes the visible homepage hero and dominant marketing impression.
- `brand_color: #DA5C2C` is chosen from observed frequency candidates and visual CTA warmth; the formal ramp action anchor is also represented as `#F76B15`.
- Motion behavior was not replayed in-browser during this pass; transition guidance is inferred from CSS counts and typical interaction surfaces.
- Form/input specs are homepage-derived assumptions because the first viewport and extracted text do not expose a full form component.
