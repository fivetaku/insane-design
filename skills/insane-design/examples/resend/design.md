---
schema_version: 3.2
slug: resend
service_name: Resend
site_url: https://resend.com
fetched_at: 2026-04-20T20:00:00+09:00
default_theme: dark
brand_color: "#FFFFFF"
primary_font: "domaine"
font_weight_normal: 400
token_prefix: "--"

bold_direction: "Monochrome Precision"
aesthetic_category: "Industrial Minimalism"
signature_element: "hero_impact"
code_complexity: "high"

medium: web
medium_confidence: high
archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "CSS variables 513 total, Tailwind v4 utility output, custom font stack, dark neutral ramps, and repeated component classes across hero, nav, code panels, tabs, cards, editor mocks."

colors:
  background: "#000000"
  gray-1: "#141517"
  gray-10: "#F0F0F0"
  text-on-dark: "#FFFFFF"
  text-muted: "#A1A4A5"
  hairline: "#D7EFF847"
  rainbow-cyan: "#02FCEF70"
  rainbow-amber: "#FFB52B70"
  rainbow-purple: "#A02BFE70"

typography:
  display: "domaine"
  ui: "aBCFavorit"
  body: "inter"
  mono: "commitMono"
  ladder:
    - { token: hero-h1, size: "4rem -> 6rem", weight: 400, line_height: "100%", tracking: "-0.01em" }
    - { token: section-h2, size: "3rem -> 3.5rem", weight: 400, line_height: "120%", tracking: "tighter" }
    - { token: body, size: "16px", weight: 400, line_height: "1.5" }
    - { token: nav, size: "14px", weight: 500, line_height: "58px control height" }
  weights_used: [100, 400, 500, 700]
  weights_absent: [800, 900]

components:
  button-primary-dark: { bg: "#FFFFFF", fg: "#000000", radius: "1rem", padding: "12px 24px" }
  button-secondary-outline: { bg: "transparent", fg: "#FFFFFF", border: "1px solid var(--color-slate-6)", radius: "1rem" }
  rainbow-pill: { bg: "linear-gradient(var(--angle), #02FCEF70 0%, #FFB52B70 50%, #A02BFE70 100%)", radius: "999px", height: "32px" }
  code-panel: { bg: "#141517", border: "1px solid var(--color-slate-6)", radius: "1.5rem" }
---

# DESIGN.md - Resend (Designer Guidebook v3.2)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Resend is not a colorful email SaaS page. It behaves like a black-box developer instrument placed under studio lighting: the page starts from #000000 (`{colors.background}`), lets white typography become the product signal, and uses color only as a controlled electrical trace. The hero cube is almost product photography, but it is also a metaphor for email infrastructure: modular, dark, engineered, and slightly impossible. It feels less like a homepage and more like a sealed mail relay sitting on a lab bench, with the UI acting as the diagnostic readout around it.

The defining contrast is typographic. "Email for developers" is set in Domaine, huge and delicate, with 100% line-height and -0.01em tracking. Around it, navigation, buttons, tabs, and code examples fall back to the more mechanical `aBCFavorit`, `inter`, and `commitMono` stack. That split keeps the brand from becoming another generic developer dashboard: editorial display face on top, utilitarian product UI beneath. The serif headline is the label on the black instrument case; the mono panels are the screws, ports, and oscilloscope traces that prove it actually works.

Color has a negative identity. There is no stable blue, green, or purple primary. No second brand color steps forward. The "brand" is mostly black, white, gray, and hairline translucency: #000000 (`{colors.background}`), #FFFFFF (`{colors.text-on-dark}`), #141517 (`{colors.gray-1}`), and #A1A4A5 (`{colors.text-muted}`). The single expressive move is the Launch Week / Forward pill: a rotating rainbow edge using #02FCEF70 (`{colors.rainbow-cyan}`), #FFB52B70 (`{colors.rainbow-amber}`), and #A02BFE70 (`{colors.rainbow-purple}`), blurred by 20px and slowed to a 30s loop. It is a signal wire glowing inside a server rack, not a palette.

The page rhythm is built from dense engineering surfaces inside generous black air. Hero content sits left in a max 80rem shell, code examples and product mocks use rounded dark panels, and sections repeat a 48px to 96px vertical cadence. The black field behaves like a darkroom: the page disappears so the instrument, code, and status events can develop under controlled light. This is not "friendly email marketing"; it is developer confidence staged as cinematic restraint.

The chrome is intentionally quiet. Shadows do not build a card hierarchy; translucent hairlines and inset glints do the work. Product panels read like rack-mounted modules behind smoked glass, while the rainbow pill remains the tiny LED that says the system is alive. Resend's craft is this refusal: no full-page gradient, no blue SaaS CTA, no confetti of feature colors, no playful bounce. The site keeps its hand steady and lets the infrastructure object carry the drama.

### Key Characteristics

- Black-first surface: #000000 page background, #141517 panels, and near-white text create the main brand impression.
- Domaine display headline: 4rem mobile to 6rem desktop, 100% leading, -0.01em tracking.
- Monochrome CTA logic: primary action is white-on-black or white-on-dark, not a chromatic brand button.
- Rainbow pill is the exception: rotating cyan/amber/purple border with 20px blur and hover acceleration.
- Tailwind v4 utility output: `--spacing: .25rem`, `--container-7xl: 80rem`, `--radius-2xl: 1rem`.
- Dark translucent hairlines: slate alpha tokens and P3 slate values carry borders instead of heavy outlines.
- Product surfaces look like tools: code panes, event cards, tabs, editor mockups, webhook logs.
- Motion is restrained but technical: 150-300ms UI transitions plus a 30s linear rainbow loop.
- Decorative imagery is narrow: the hero cube carries the drama; the UI chrome stays quiet.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Monochrome Precision
> **Aesthetic Category**: Industrial Minimalism
> **Signature Element**: 이 사이트는 **black infrastructure object plus editorial developer headline**으로 기억된다.
> **Code Complexity**: high — Tailwind v4 utilities, custom font faces, scroll fades, rotating gradient border, dark product mockups, and many stateful component classes.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Resend처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Domaine headline, utility UI */
:root {
  --rs-font-display: "domaine", Georgia, serif;
  --rs-font-ui: "aBCFavorit", "Inter", system-ui, sans-serif;
  --rs-font-mono: "commitMono", ui-monospace, monospace;
}

/* 2. Black floor, not light SaaS */
body {
  background: #000000;
  color: #FFFFFF;
  font-family: var(--rs-font-ui);
  font-weight: 400;
}

/* 3. Hero headline */
.hero-title {
  font-family: var(--rs-font-display);
  font-size: clamp(4rem, 7vw, 6rem);
  line-height: 100%;
  letter-spacing: -0.01em;
  background: linear-gradient(to bottom right, #FFFFFF 30%, #FFFFFF80);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
```

**절대 하지 말아야 할 것 하나**: CTA와 hero를 일반 파란 SaaS 팔레트로 바꾸지 말 것. Resend의 중심 색은 chromatic blue가 아니라 #000000 / #FFFFFF의 압축된 대비다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://resend.com` |
| Fetched | 2026-04-20T20:00:00+09:00 |
| Extractor | reused phase1 artifacts from `insane-design/resend/` |
| HTML size | 448792 bytes |
| CSS files | 6 external CSS files, total 803664 chars |
| Token prefix | `--` |
| Method | phase1 JSON reuse + CSS custom property parsing + screenshot/manual interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next-style static/SSR HTML artifact with Tailwind v4 output and utility class hydration.
- **Design system**: Resend site system — generic `--color-*`, `--gray-*`, `--slate-*`, `--font-*`, `--radius-*`, `--container-*`, `--spacing`.
- **CSS architecture**:
  ```text
  core        --gray-*, --slate-a*, --color-*       raw color / display-p3 / alias values
  utility     Tailwind v4 generated classes         `.text-slate-12`, `.rounded-2xl`, `.max-w-7xl`
  component   semantic class islands                `.rainbow-border`, `.effect-font-gradient`, `.scrollarea`
  product     markup-level compositions             hero, nav, code panel, editor mock, event cards
  ```
- **Class naming**: Tailwind utilities plus a few explicit effect classes; no BEM system observed.
- **Default theme**: dark (bg = `#000000`, panels = `#141517`, text = `#FFFFFF` / `#F0F0F0`).
- **Font loading**: self-hosted `@font-face` WOFF2 with `font-display: swap`.
- **Canonical anchor**: first viewport hero: sticky nav, left-aligned giant Domaine headline, dark cube image, dual CTA, rainbow announcement pill.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `domaine` (self-hosted serif display; regular, medium, bold observed)
- **UI font**: `aBCFavorit` (self-hosted grotesk; 400 and 500 observed)
- **Body/system font**: `inter` variable 100-900 available
- **Code font**: `commitMono` (self-hosted mono; regular and italic observed)
- **Weight normal / bold**: `400` / `700`, with `500` used for navigation and compact controls

```css
:root {
  --font-inter: "inter";
  --font-abc-favorit: "aBCFavorit";
  --font-domaine-src: "domaine";
  --font-commit-mono: "commitMono";
  --font-sans: var(--font-inter), ui-sans-serif, system-ui, sans-serif;
  --font-display: var(--font-abc-favorit), ui-sans-serif, system-ui, sans-serif;
  --font-domaine: var(--font-domaine-src), ui-sans-serif, system-ui, sans-serif;
  --font-mono: var(--font-commit-mono), ui-monospace, monospace;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;
}
```

### Note on Font Substitutes

- **Domaine substitute** — use `Cormorant Garamond` or `DM Serif Display` only for the hero headline, then tighten tracking to `-0.01em` and keep line-height at `1`. Do not use it for navigation or body.
- **aBCFavorit substitute** — use `Inter` at 400/500 with normal tracking. Keep nav links at 14px and controls at 58px height to preserve the original density.
- **commitMono substitute** — use `JetBrains Mono` or `IBM Plex Mono` at 13-14px. Keep code samples compact; do not enlarge mono text to compensate.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `hero-h1` | `4rem` mobile, `6rem` desktop | 400 | `100%` | `-0.01em` |
| `section-h2` | `3rem` mobile, `3.5rem` desktop | 400 | `120%` | `tighter` |
| `card-title` | `20px` / `text-xl` | 400-500 | `130%` | normal |
| `nav-link` | `14px` / `text-sm` | 500 | `58px` control height | inherited |
| `body` | `16px` | 400 | `1.5` | normal |
| `small-ui` | `12px-14px` | 400-500 | compact | normal |
| `code` | `13px-14px` | 400 | compact | tabular where needed |

> ⚠️ Key insight: the brand is not "Inter everywhere." Resend's first impression depends on Domaine for the hero and section drama, while the product interface uses Favorit/Inter/CommitMono to feel engineered.

### Principles

1. Display type is serif and oversized, not a geometric SaaS sans. The hero uses Domaine at 4rem -> 6rem with 100% line-height.
2. The gradient text treatment is part of the type system: #FFFFFF to #FFFFFF80, clipped into the heading.
3. UI text is deliberately smaller. Navigation holds at 14px with a 58px interactive row, which keeps the header technical instead of promotional.
4. Weight 900 is absent from the visible brand voice. Contrast comes from size and color, not ultra-bold text.
5. Mono is a product proof surface. Code blocks should feel real, dense, and copyable, not decorative.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (monochrome anchor)

| Token | Hex |
|---|---|
| `--background` | `#000000` |
| `--color-black` | `#000000` |
| `--color-white` | `#FFFFFF` |
| `--gray-1` | `#141517` |
| `--gray-10` | `#F0F0F0` |

### 06-2. Brand Dark Variant

| Token | Hex / Value |
|---|---|
| `--canvas` | `#14151799` |
| `--gray-a1` | `#16171AEB` |
| `--gray-a10` | `#FDFDFDED` |
| `--slate-a12` | `color(display-p3 .988 .992 1/.937)` |

### 06-3. Neutral Ramp

| Step | Dark gray | Use |
|---|---|---|
| `--gray-1` | `#141517` | deep panel base |
| `--gray-2` | `#191B1E` | elevated panel |
| `--gray-3` | `#212629` | gradient start / darker field |
| `--gray-4` | `#293034` | soft container |
| `--gray-5` | `#333B3E` | hover surface |
| `--gray-6` | `#3B4345` | border / low contrast line |
| `--gray-7` | `#434A4D` | stronger border |
| `--gray-8` | `#52595B` | subdued icon / text |
| `--gray-9` | `#A1A4A5` | muted body text |
| `--gray-10` | `#F0F0F0` | high-emphasis text |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Rainbow cyan | `--rainbow-cyan` | `#02FCEF70` |
| Rainbow amber | `--rainbow-amber` | `#FFB52B70` |
| Rainbow purple | `--rainbow-purple` | `#A02BFE70` |
| Success green | utility / event UI | `#22C55E` |
| Orange glow | product effects | `#F76004` |

### 06-5. Semantic

| Token | Hex / Value | Usage |
|---|---|---|
| `--color-background` | `var(--background)` -> `#000000` | page floor |
| `--color-canvas` | `var(--canvas)` -> `#14151799` | translucent product canvas |
| `--color-slate-11` | display-p3 alpha | muted nav/body text |
| `--color-slate-12` | display-p3 alpha | high-emphasis text |
| `--tw-ring-color` | `#131313` | focus/ring fallback |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `.bg-background` | `#000000` | page and dark sections |
| `.text-white` | `#FFFFFF` | CTA / hero foreground |
| `.text-slate-11` | `var(--color-slate-11)` | secondary nav and body copy |
| `.text-slate-12` | `var(--color-slate-12)` | headings and important labels |
| `.border-slate-6` | `var(--color-slate-6)` | product panels and section dividers |
| `.rounded-2xl` | `1rem` | CTA and larger buttons |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency |
|---|---|---|
| raw transparent | `#0000` | 178 |
| white shorthand | `#FFF` | 168 |
| black shorthand | `#000` | 123 |
| translucent white | `#FFF3` | 46 |
| shadow black | `#0000001A` | 41 |
| hairline white | `#FFFFFF0D` | 36 |
| transparent white | `#FFF0` | 35 |
| white alpha | `#FFFFFF1A` | 24 |
| product green | `#62FFB3` | 20 |

### 06-8. Color Stories

**`--background` (`#000000`)** — The actual brand floor. It makes the email platform feel like infrastructure, not a newsletter tool, and it gives the hero cube enough darkness to read as a physical object.

**`--color-white` (`#FFFFFF`)** — The interaction color and display contrast. Primary CTAs and hero typography use white as the active brand signal instead of blue.

**`--gray-1` (`#141517`)** — The product-panel black. Code editors, mock dashboards, and inset surfaces should sit here so the page can differentiate chrome from the pure black background.

**`--gray-9` (`#A1A4A5`)** — Muted explanation text. It lets subcopy be readable without stealing from Domaine headlines or CTA whites.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--spacing` | `.25rem` | Tailwind v4 base unit |
| `px-6` | `24px` | section horizontal padding |
| `py-12` | `48px` | mobile section vertical rhythm |
| `sm:py-24` | `96px` | desktop section vertical rhythm |
| `gap-4` | `16px` | small button/icon stacks |
| `max-w-5xl` | `64rem` | inner content / mobile-wide shell |
| `max-w-7xl` | `80rem` | hero and main section shell |
| `mb-10` | `40px` | hero announcement-to-headline gap |
| `h-[58px]` | `58px` | nav dropdown/button hit row |

**주요 alias**:
- `--container-7xl` -> `80rem` (hero and main content)
- `--container-5xl` -> `64rem` (narrower section shell)
- `--spacing` -> `.25rem` (all utility spacing ladders)

### Whitespace Philosophy

Resend uses black air as a material. The first viewport leaves a wide quiet band around the H1 and cube, but individual product modules are dense: code, event logs, tabs, and editor mockups compress into technical panels. This contrast says "large idea, exact implementation."

The repeatable section rhythm is `px-6 py-12 sm:py-24`, not a custom hand-authored art layout for every block. The craft is in where the system breaks: the hero gets `md:h-screen`, `md:max-h-[950px]`, and the rainbow pill sits 40px above the headline as a tiny signal before the massive serif statement.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--radius-xs` | `.125rem` | tiny form/editor details |
| `--radius-sm` | `.25rem` | compact controls |
| `--radius-md` | `.375rem` | default utility radius |
| `--radius-lg` | `.5rem` | small panels |
| `--radius-xl` | `.75rem` | cards / controls |
| `--radius-2xl` | `1rem` | primary CTA and large buttons |
| `--radius-3xl` | `1.5rem` | large product/demo containers |
| `--radius-4xl` | `2rem` | oversized surfaces |
| `rounded-full` | effectively infinite | rainbow pill / capsule affordances |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| reset | `0 0 #0000` | base Tailwind shadow reset |
| small | `0 1px 2px 0 #0000000D` | subtle UI elevation |
| panel | `0 4px 20px 0 #00000026` | dark product card depth |
| inset chrome | `inset .5px -.5px 0 0 #00000080, inset -1px 1px 1px 0 #FFFFFF1C` | metallic/inset product detail |
| glow white | `0 0 .5rem .1rem #FFFFFF20` | light accents on dark |
| orange glow | `0 0 1.125rem .125rem #EB761699` | warm product effect |

Pattern: Resend does not rely on card shadows for marketing depth. Most structure comes from hairline borders and dark surface contrast; glow shadows appear only on special product/effect moments.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| `.duration-150` | `150ms` | nav / focus transitions |
| `.duration-200` | `200ms` | hover controls |
| `.duration-300` | `300ms` | toast / larger transitions |
| `.duration-360` | `360ms` | custom UI polish |
| `.rainbow-border` | `30s linear infinite` | rotating announcement edge |
| `.rainbow-border:hover` | `15s` | hover accelerates the loop |
| scroll fades | `animation-timeline: --scroller` | horizontal/vertical scroll area edge fades |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `64rem` (`max-w-5xl`) for tighter content, `80rem` (`max-w-7xl`) for hero and major sections.
- **Grid type**: Tailwind flex/grid utilities; product sections mix flex rows, grids, and panel compositions.
- **Column count**: hero behaves as a left text / right object composition on desktop; feature sections use repeatable card/panel arrangements.
- **Gutter**: `px-6` shell padding, `gap-4` / `gap-6` / `gap-8` inside panels.

### Hero
- **Pattern Summary**: `md:h-screen + black cinematic object background + left Domaine H1 + dual CTA below`
- Layout: left-aligned text stack inside `mx-auto max-w-5xl md:max-w-7xl`; dark cube imagery occupies the right half visually.
- Background: pure black with subtle light streak and dark product cube.
- **Background Treatment**: image-overlay / product-render on #000000, no full-page gradient mesh.
- H1: `4rem` / desktop `6rem`, weight `400`, tracking `-0.01em`, leading `100%`.
- Max-width: `80rem` container with `md:max-h-[950px]`.

### Section Rhythm

```css
section {
  padding: 48px 24px;
  max-width: 80rem;
}
@media (min-width: 40rem) {
  section { padding-top: 96px; padding-bottom: 96px; }
}
```

### Card Patterns
- **Card background**: #141517 / gray alpha canvas, often with translucent overlays.
- **Card border**: `1px solid var(--color-slate-6)` or white alpha hairlines such as #FFFFFF0D.
- **Card radius**: `1.5rem` for large demos, `1rem` for buttons, `.25rem-.75rem` for internal controls.
- **Card padding**: `24px` common outer rhythm; compact product controls use 4-12px.
- **Card shadow**: minimal; inset and glow shadows used as craft details rather than global elevation.

### Navigation Structure
- **Type**: sticky horizontal nav with dropdown buttons and right-side login/CTA.
- **Position**: `sticky top-0 z-40`.
- **Height**: nav controls use `h-[58px]`; header is visually around 58-64px.
- **Background**: transparent-to-dark feel over the black page; border starts transparent.
- **Border**: bottom border/hairline behavior via slate/transparent classes.

### Content Width
- **Prose max-width**: no long editorial prose width token observed; marketing copy stays in short blocks.
- **Container max-width**: `80rem`.
- **Sidebar width**: not homepage-primary; docs/product flows may differ and are marked as a gap.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `<40rem` | compressed section padding, stacked content |
| Small | `min-width: 40rem` | `sm:py-24` activates larger vertical rhythm |
| Tablet | `min-width: 48rem` | hero height/sizing and desktop typography begin |
| Desktop | `min-width: 64rem` | wider nav and multi-column compositions |
| Large | `min-width: 80rem` / `96rem` | full container polish and large-screen adjustments |
| XL monitor | `min-width: 1920px` | a few large viewport rules observed |

### Touch Targets
- **Minimum tap size**: primary nav rows around `58px`; buttons visually exceed 44px.
- **Button height (mobile)**: primary CTA appears around 44-48px with `rounded-2xl`.
- **Input height (mobile)**: homepage forms not directly measured; product/editor mocks imply compact 32-48px controls.

### Collapsing Strategy
- **Navigation**: mobile menu exists (`Open main menu` text present) with desktop dropdown nav.
- **Grid columns**: sections collapse from wider desktop product compositions to stacked blocks.
- **Sidebar**: not homepage-primary.
- **Hero layout**: desktop object/text composition collapses to text-first with image/object secondary.

### Image Behavior
- **Strategy**: hero product render/visual object, not generic stock photo.
- **Max-width**: container-bound; visual object can dominate right side.
- **Aspect ratio handling**: screenshot shows fixed 1280x800 crop with object centered right; exact CSS object-fit not fully mapped.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA**

```html
<a class="relative inline-flex items-center justify-center rounded-2xl text-white">
  Get Started
</a>
```

| Property | Value |
|---|---|
| Shape | `rounded-2xl` (`1rem`) |
| Color | white text or white-filled variant depending surface |
| State | hover/focus via transition and focus-visible ring |
| Motion | `ease-in-out`, commonly 150-200ms |

**Secondary CTA**

```html
<a class="relative inline-flex items-center border justify-center rounded-2xl">
  Documentation
</a>
```

| Property | Value |
|---|---|
| Border | slate / white alpha hairline |
| Background | transparent or dark translucent |
| Text | muted to white on hover |
| Use | docs, React Email, secondary navigation |

### Badges

**Rainbow announcement pill**

```html
<a class="rainbow-border inline-flex items-center justify-center rounded-full">
  <span>Announcing Resend Forward</span>
</a>
```

| Property | Value |
|---|---|
| Height | `32px` |
| Border effect | rotating `#02FCEF70 -> #FFB52B70 -> #A02BFE70` gradient |
| Blur | `filter: blur(20px)` on pseudo element |
| Hover | loop speeds from `30s` to `15s`, after scale increases |

### Cards & Containers

```html
<section class="relative rounded-3xl border-t border-slate-6">
  <header class="flex h-12 items-center border-b border-slate-6"></header>
</section>
```

| Property | Value |
|---|---|
| Background | #141517 / black alpha surfaces |
| Border | `border-slate-6`, `border-white/5`, `border-white/10` |
| Radius | `rounded-3xl` for large product surfaces |
| Shadow | sparse; glow/inset only for special moments |
| Hover | subtle border/background shifts, not large transform cards |

### Navigation

```html
<header class="sticky top-0 z-40 border-b border-transparent transition duration-200 ease-in-out">
  <button class="h-[58px] text-sm font-medium text-gray-9 hover:text-gray-10">Features</button>
  <a class="rounded-2xl">Get Started</a>
</header>
```

| Property | Value |
|---|---|
| Position | sticky top |
| Link size | 14px, 500 weight |
| Hit row | 58px |
| State | hover raises muted gray to brighter gray/white |

### Inputs & Forms

Homepage primary forms are not exposed, but editor/product mocks reveal compact input/control styling:

| Property | Value |
|---|---|
| Control radius | `.25rem` to `.75rem` |
| Focus | `focus-visible:ring-2` with slate/ring token |
| Placeholder/editor selection | editor accent `59 130 246` with 10% overlay |
| Density | compact, product-like, not oversized marketing forms |

### Hero Section

```html
<section class="mx-auto max-w-5xl px-6 pb-8 md:h-screen md:max-h-[950px] md:max-w-7xl">
  <a class="rainbow-border mb-10 rounded-full">Announcing Resend Forward</a>
  <h1 class="font-domaine text-[4rem] md:text-[6rem] tracking-[-0.01em] leading-[100%] effect-font-gradient">
    Email for developers
  </h1>
</section>
```

| Property | Value |
|---|---|
| Container | `max-w-5xl`, desktop `max-w-7xl` |
| Height | desktop screen-height, capped at 950px |
| H1 | Domaine, huge, gradient clipped |
| CTA layout | dual action row: Get Started + Documentation |
| Imagery | black cube object on right, not a card preview |

### 13-2. Named Variants

- **button-primary-dark** — rounded-2xl CTA on black hero; white emphasis, compact horizontal padding, 150-200ms transition.
- **button-secondary-outline** — rounded-2xl bordered link for Documentation / Check the Docs; no filled chromatic background.
- **rainbow-pill** — Launch Week / Forward capsule with `@property --angle` rotation and blurred pseudo-element.
- **code-panel-tab** — compact `h-8` rounded tabs in product/code panels, hover text brightening.
- **product-panel-large** — `rounded-3xl border-slate-6` containers with dark canvas, used for integration/editor/webhook examples.

### 13-3. Signature Micro-Specs

```yaml
rotating-rainbow-edge:
  description: "The only chromatic brand flare, held to the announcement edge instead of the page surface."
  technique: "@property --angle + linear-gradient(var(--angle), #02FCEF70 0%, #FFB52B70 50%, #A02BFE70 100%); animation 30s linear infinite; hover duration 15s"
  applied_to: ["{component.rainbow-pill}", "{component.hero-announcement}"]
  visual_signature: "A thin cyan-amber-purple signal trace on an otherwise black-and-white infrastructure page."

blurred-gradient-afterglow:
  description: "Duplicates the rainbow edge as a compressed glow so color reads as electrical leakage, not a filled badge."
  technique: ":after uses the same gradient, filter: blur(20px), transform: scale(.95,.6), hover transform: scale(1.1,.9)"
  applied_to: ["{component.rainbow-pill}:after"]
  visual_signature: "The pill has a soft neon undercurrent while the interior stays dark and controlled."

domaine-clipped-display:
  description: "Turns the hero headline into the editorial label for the developer instrument."
  technique: "font-family: domaine; font-size: 4rem -> 6rem; line-height: 100%; letter-spacing: -0.01em; background: linear-gradient(to bottom right, #FFFFFF 30%, #FFFFFF80); background-clip: text"
  applied_to: ["{component.hero-section}", "{typography.hero-h1}"]
  visual_signature: "A delicate serif headline glows against #000000 without becoming a bold SaaS shout."

dark-hairline-paneling:
  description: "Uses translucent lines and dark canvas steps as product chrome instead of elevation."
  technique: "background #141517 / #191B1E; border-slate-6; white alpha hairlines #FFFFFF0D and #FFFFFF1A; sparse inset/glow shadows only for special details"
  applied_to: ["{component.code-panel}", "{component.product-panel-large}", "{component.navigation}"]
  visual_signature: "Rack-mounted dark modules separated by precise hairlines, with almost no card shadow hierarchy."

scrollarea-edge-fade:
  description: "Makes overflow feel engineered and bounded, like data moving behind a viewport mask."
  technique: "scroll fades using animation-timeline: --scroller, paired with restrained 150-300ms UI transitions"
  applied_to: ["{component.scrollarea}", "{component.code-panel}", "{component.product-panel-large}"]
  visual_signature: "Panel edges softly reveal motion without introducing playful or bouncy animation."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Short, declarative, developer-first | "Email for developers" |
| Primary CTA | Direct action, no cleverness | "Get Started" |
| Secondary CTA | Documentation as equal proof | "Documentation", "Check the Docs" |
| Subheading | Plain product outcome with human stakes | "The best way to reach humans instead of spam folders." |
| Tone | Engineer-to-engineer, polished but not playful | "A simple, elegant interface..." |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Resend — copy into your root stylesheet */
:root {
  /* Fonts */
  --rs-font-display: "domaine", Georgia, serif;
  --rs-font-ui: "aBCFavorit", "Inter", system-ui, sans-serif;
  --rs-font-body: "Inter", system-ui, sans-serif;
  --rs-font-mono: "commitMono", ui-monospace, monospace;
  --rs-font-weight-normal: 400;
  --rs-font-weight-medium: 500;
  --rs-font-weight-bold: 700;

  /* Monochrome brand */
  --rs-bg-page: #000000;
  --rs-surface-panel: #141517;
  --rs-surface-panel-2: #191B1E;
  --rs-text-primary: #FFFFFF;
  --rs-text-soft: #F0F0F0;
  --rs-text-muted: #A1A4A5;
  --rs-border-soft: #D7EFF847;

  /* Signature accent */
  --rs-rainbow-cyan: #02FCEF70;
  --rs-rainbow-amber: #FFB52B70;
  --rs-rainbow-purple: #A02BFE70;

  /* Layout */
  --rs-space-unit: .25rem;
  --rs-container: 80rem;
  --rs-section-y: 96px;
  --rs-radius-button: 1rem;
  --rs-radius-panel: 1.5rem;
}

body {
  background: var(--rs-bg-page);
  color: var(--rs-text-primary);
  font-family: var(--rs-font-ui);
}

.rs-hero-title {
  font-family: var(--rs-font-display);
  font-size: clamp(4rem, 7vw, 6rem);
  line-height: 100%;
  letter-spacing: -0.01em;
  background: linear-gradient(to bottom right, #FFFFFF 30%, #FFFFFF80);
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  background-clip: text;
}

.rs-rainbow-pill {
  position: relative;
  height: 32px;
  border-radius: 999px;
  background: linear-gradient(var(--angle), #02FCEF70 0%, #FFB52B70 50%, #A02BFE70 100%);
  animation: rs-rotate 30s linear infinite;
}

@keyframes rs-rotate {
  to { --angle: 360deg; }
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Resend approximation
module.exports = {
  theme: {
    extend: {
      colors: {
        resend: {
          black: '#000000',
          panel: '#141517',
          panel2: '#191B1E',
          text: '#FFFFFF',
          muted: '#A1A4A5',
          hairline: '#D7EFF847',
          cyan: '#02FCEF70',
          amber: '#FFB52B70',
          purple: '#A02BFE70',
        },
      },
      fontFamily: {
        display: ['domaine', 'Georgia', 'serif'],
        ui: ['aBCFavorit', 'Inter', 'system-ui', 'sans-serif'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['commitMono', 'ui-monospace', 'monospace'],
      },
      borderRadius: {
        '2xl': '1rem',
        '3xl': '1.5rem',
      },
      maxWidth: {
        '7xl': '80rem',
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
| Brand primary | `--background` / `--color-white` contrast | `#000000` / `#FFFFFF` |
| Background | `--background` | `#000000` |
| Surface | `--gray-1` | `#141517` |
| Text primary | `--color-white` | `#FFFFFF` |
| Text muted | `--gray-9` | `#A1A4A5` |
| Border | `--gray-a6` / slate alpha | `#D7EFF847` |
| Success | utility green | `#22C55E` |
| Error | `--color-red-500` | `#FB2C36` |

### Example Component Prompts

#### Hero Section

```text
Resend 스타일 히어로 섹션을 만들어줘.
- 배경: #000000
- 레이아웃: max-width 80rem, px 24px, desktop height 100vh capped near 950px
- H1: Domaine serif, 4rem -> 6rem, weight 400, line-height 100%, tracking -0.01em
- H1 fill: linear-gradient(to bottom right, #FFFFFF 30%, #FFFFFF80), background-clip text
- 서브텍스트: #A1A4A5, 16px, max 2 lines
- CTA: rounded 1rem, white/black contrast, 150-200ms transition
- 장식: right side dark product cube/object, not a colorful illustration
```

#### Card Component

```text
Resend 스타일 제품 카드/패널을 만들어줘.
- 배경: #141517 또는 #191B1E
- border: 1px solid #D7EFF847 or #FFFFFF0D
- radius: 1.5rem for large panel, 1rem for controls
- shadow: minimal; use inset hairline or tiny dark shadow only
- typography: aBCFavorit/Inter 14-16px for UI, commitMono for code
- hover: border/text brightening, no large scale transform
```

#### Badge

```text
Resend 스타일 발표 pill을 만들어줘.
- height: 32px, rounded-full
- border/background: rotating gradient #02FCEF70 -> #FFB52B70 -> #A02BFE70
- pseudo-element glow: same gradient, blur(20px), scale(.95,.6)
- inner span: #0B0E14, width calc(100% - 2px), height 30px
- hover: animation duration 30s -> 15s
```

#### Navigation

```text
Resend 스타일 상단 네비게이션을 만들어줘.
- sticky top-0 z-40, black/transparent dark surface
- logo left, nav center, login + CTA right
- links: 14px, weight 500, #A1A4A5 -> #F0F0F0 on hover
- row height: 58px
- focus: focus-visible ring 2px with slate/ring token
```

### Iteration Guide

- **색상 변경 시**: chromatic primary를 새로 만들지 말고 #000000 / #FFFFFF / gray ramp 안에서 해결한다.
- **폰트 변경 시**: hero serif와 UI sans를 분리한다. 모든 텍스트를 Inter 하나로 통합하면 Resend 느낌이 사라진다.
- **여백 조정 시**: `--spacing: .25rem` 기반 4px ladder와 `48px / 96px` section rhythm을 유지한다.
- **새 컴포넌트 추가 시**: radius는 1rem 또는 1.5rem, border는 translucent hairline, shadow는 최소화한다.
- **모션 추가 시**: 150-300ms UI transition 또는 very slow technical loop만 사용한다. bouncy motion 금지.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #000000 as the page floor and let white typography carry the brand.
- Keep hero display type in Domaine or a serif substitute with 100% line-height.
- Use `aBCFavorit` / Inter style sans for navigation, buttons, and product UI.
- Treat code panels and editor mocks as real product surfaces: compact, dark, bordered, and mono.
- Reserve chromatic color for the rainbow pill or status/event accents only.
- Use rounded-2xl buttons and rounded-3xl product panels rather than sharp enterprise boxes.
- Keep section rhythm spacious outside and dense inside product panels.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#000000` 사용.
- 기본 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#FFFFFF` 또는 `#F0F0F0` 사용.
- 제품 패널을 `#FFFFFF` 카드로 만들지 말 것 — 대신 `#141517` 또는 `#191B1E` 사용.
- muted text를 `#6B7280` 같은 기본 Tailwind gray로 두지 말 것 — 대신 `#A1A4A5` 사용.
- border를 `#E5E7EB` light gray로 두지 말 것 — 대신 `#D7EFF847`, `#FFFFFF0D`, 또는 slate alpha 사용.
- primary CTA를 `#3080FF` 또는 `#155DFC` blue fill로 만들지 말 것 — Resend homepage CTA는 monochrome contrast가 중심이다.
- hero H1을 Inter 700/800으로 만들지 말 것 — Domaine 400 + huge size + tight tracking이 핵심이다.
- rainbow gradient를 full-page background로 확장하지 말 것 — `#02FCEF70`, `#FFB52B70`, `#A02BFE70`은 pill edge flare에 머문다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No stable chromatic brand color** — blue/green/purple are utilities or one-off effects, not the core brand.
- **No light SaaS page shell** — the homepage identity is dark, not white-card-on-gray.
- **No generic Inter-only typography** — Domaine is required for the main emotional signal.
- **No rainbow everywhere** — the rainbow treatment is a tiny announcement edge, never a section background.
- **No heavy elevation system** — shadows are sparse; hairlines and surface contrast do the structural work.
- **No rounded marketing blobs** — the hero object is a hard black cube, not soft abstract decoration.
- **No oversized friendly forms** — controls and product mocks stay compact and developer-tool dense.
- **No playful bounce motion** — motion is technical: quick fades or slow mechanical loops.
- **No 800/900 weight hero shouting** — scale and serif contrast replace weight.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage-oriented capture** — analysis reused existing `insane-design/resend` phase1 files and hero screenshot. Deep docs, dashboard, signup, and settings flows were not navigated.
- **Exact hero image CSS not fully mapped** — screenshot confirms black cube object and light streak, but the source image asset and object-fit rules were not separately traced.
- **CSS includes product/editor code** — some tokens come from editor or dashboard components bundled into the same CSS; homepage-only usage was manually filtered where obvious.
- **P3 slate values are not converted to final sRGB** — display-p3 alpha tokens were preserved as observed; hex equivalents are only used where CSS also contained hex.
- **Form validation/loading states not surfaced** — homepage mockups show controls and editor states, but real validation/error/loading flows were not exercised.
- **Dark mode counterpart is not a separate theme** — default capture is already dark; a complete light theme mapping was not observed.
- **Motion JS not analyzed** — CSS keyframes and transition utilities were captured, but scroll-triggered JS or React state timing was not inspected.
- **Customer/logo color contamination risk** — frequency candidates include many chromatic values; brand color selection intentionally favors CTA/hero behavior and monochrome system identity.
