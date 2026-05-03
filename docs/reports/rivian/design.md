---
schema_version: 3.2
slug: rivian
service_name: Rivian
site_url: https://rivian.com
fetched_at: 2026-05-03T07:04:51Z
default_theme: mixed
brand_color: "#FFAC00"
primary_font: Adventure
font_weight_normal: 400
token_prefix: rivian

bold_direction: Adventure Editorial
aesthetic_category: editorial-product
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: automotive
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Tailwind v3.4 utilities, CSS variables, custom Adventure fonts, navbar/card tokens, and responsive image art direction are present in production CSS."

colors:
  brand-rivian-yellow: "#FFAC00"
  surface-primary: "#FFFFFF"
  surface-primary-alt: "#FAFAFA"
  text-primary: "#151515"
  surface-dark: "#212121"
  text-muted: "#636363"
  stroke-secondary: "#CBCBCB"
  outdoor-sky: "#5D767D"
  adventure-clay: "#E6E5DF"
typography:
  display: "Adventure"
  body: "Adventure"
  mono: "Adventure Mono"
  ladder:
    - { token: display-xl, size: "clamp(96px, 13.54vi + 26.72px, 200px)", weight: 600, tracking: "-0.02em" }
    - { token: display-lg, size: "clamp(72px, 6.25vi + 40px, 120px)", weight: 600, tracking: "-0.02em" }
    - { token: h1, size: "56px", weight: 600, tracking: "-2.5px" }
    - { token: h4, size: "32px", weight: 600, tracking: "-1px" }
    - { token: body, size: "16px", weight: 400, tracking: "0" }
    - { token: label, size: "14px", weight: 600, tracking: "-0.01em" }
  weights_used: [300, 400, 500, 600, 700]
  weights_absent: [800, 900]
components:
  button-primary-pill: { bg: "{colors.brand-rivian-yellow}", fg: "{colors.text-primary}", radius: "40px", min_height: "56px", padding: "0 20px" }
  button-invert-pill: { bg: "{colors.surface-primary}", fg: "#000000", radius: "40px", min_height: "56px", padding: "0 20px" }
  nav-glass-toolbar: { bg: "rgba(255,255,255,0.72)", radius: "12px desktop / 20px open", height: "50px mobile / 56px desktop" }
  image-vehicle-card: { bg: "{colors.surface-primary}", radius: "20px", overlay: "linear-gradient image header + multiply" }
---

# DESIGN.md — Rivian (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: manual -->

### Narrative

Rivian's site behaves like a high-end field journal crossed with an automotive product showroom. The page is not assembled from decorative color blocks first; it opens like a trailhead seen through a windshield. Motion-blurred vehicle photography supplies the weather, terrain, dust, and scale, then the interface arrives as compact expedition equipment: pills, floating nav chrome, video controls, and conversion buttons clipped onto the image rather than replacing it.

The strongest metaphor is a mobile basecamp showroom. The vehicles are not parked on a seamless studio floor; they are staged as if the glass wall of the showroom has been removed and the landscape itself has become the display room. The hero does not say "EV technology" in blue. It says outdoor capability through terrain and restraint, then uses one controlled action signal: #FFAC00 (`{colors.brand-rivian-yellow}`). There is no second loud brand color. Yellow is a dashboard switch, not a paint bucket.

The page keeps two worlds in tension. Marketing surfaces are cinematic and immersive: full-bleed R1 imagery, 100vh panels, video controls, and large display headlines. The interface layer above them is extremely practical: rounded pills, compact nav, 56px tap targets, black/white inversion, and Tailwind utility density. That contrast is the Rivian signature: an adventure film with production-grade checkout ergonomics. The chrome behaves like gear mounted to a roof rack: visible, durable, and small enough to leave the landscape in charge.

Typography is custom but not ornamental. `Adventure` carries almost everything, with `Adventure Mono` reserved for code-like or system-adjacent moments. Display type is large, tight, and slightly industrial; body copy is calm 16px/24px. Big words feel pressed into matte metal rather than printed on a brochure. The repeated negative tracking makes headlines read like vehicle badging, while the mostly neutral copy system keeps the site from drifting into outdoor lifestyle magazine softness.

The design system is intentionally not a rainbow EV palette. Neutrals own the UI. #151515 (`{colors.text-primary}`), #FFFFFF (`{colors.surface-primary}`), #212121 (`{colors.surface-dark}`), and #636363 (`{colors.text-muted}`) do most of the work. Shadow is not a global luxury effect; depth mostly belongs to photography, gradients, and overlays. The white commerce surfaces feel like clean service-bay floors, while dark sections use #212121 (`{colors.surface-dark}`) as a matte night field rather than pure black void.

### Key Characteristics

- Full-bleed automotive photography and video are the first design material.
- #FFAC00 is a controlled action color, not a general brand wash.
- Custom `Adventure` font defines the brand voice more than color does.
- Display type uses tight tracking and large clamp-based scales.
- Navigation is a soft floating toolbar with rounded corners, not a hard header bar.
- The page alternates cinematic dark overlays with clean white commerce surfaces.
- Radius jumps are deliberate: 4px utility, 12px micro, 20px macro, 40px pill.
- Component tokens exist around navbar cards, buttons, inputs, and responsive slots.
- Motion is short and functional: 0.15s to 0.5s opacity/transform, plus video affordances.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Adventure Editorial
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **motion-blurred vehicle hero over restrained utility chrome**으로 기억된다.
> **Code Complexity**: high — Tailwind utility output, responsive image art direction, Radix-style state animations, video player CSS, and navbar card overlays all interact.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Rivian처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Adventure", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
  letter-spacing: 0;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #151515; --dark: #212121; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 액션 컬러 */
:root { --brand: #FFAC00; }
.primary-action { background: var(--brand); color: #151515; border-radius: 40px; }
```

**절대 하지 말아야 할 것 하나**: Rivian을 파란색 EV SaaS처럼 만들지 말 것. 실제 UI의 canonical action color는 #FFAC00이고, 차량 사진/중립/검정 chrome이 분위기를 만든다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://rivian.com` |
| Fetched | 2026-05-03T07:04:51Z |
| Extractor | reused existing `insane-design/rivian` phase1 artifacts |
| HTML size | 904652 bytes (Next.js SSR/hydrated app) |
| CSS files | 2 external + 1 inline, total 341255 CSS bytes |
| Token prefix | `rivian` / production tokens are mostly unprefixed semantic names |
| Method | existing CSS custom properties, frequency candidates, screenshot, and production HTML/CSS interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js production app (`/_next/static/...`, `next-head-count`, route chunks)
- **Design system**: Rivian web UI tokens — unprefixed semantic CSS variables plus Tailwind utilities
- **CSS architecture**:
  ```text
  core       (--surface-*, --text-*, --stroke-*, --spacing-*)     raw semantic values
  utility    Tailwind v3.4.19 utilities and arbitrary selectors
  component  data-slot navbar/card variables and Radix-style state hooks
  media      responsive picture sources and video player CSS
  ```
- **Class naming**: Tailwind utility classes, hashed CSS module/emotion classes (`rivian-css-*`), `data-slot` component slots
- **Default theme**: mixed (white product/commerce surfaces + dark photographic/video sections)
- **Font loading**: `@font-face` from `assets.rivian.com` and `media.rivian.com`; `font-display: swap`
- **Canonical anchor**: `https://rivian.com`

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Adventure` (Rivian proprietary webfont)
- **Code font**: `Adventure Mono` (Rivian proprietary mono)
- **Weight normal / bold**: `400` / `600` primary, with 300 and 700 also loaded

```css
:root {
  --rivian-font-family:       "Adventure", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --rivian-font-family-code:  "Adventure Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  --rivian-font-weight-normal: 400;
  --rivian-font-weight-bold:   600;
}
body {
  font-family: var(--rivian-font-family);
  font-weight: var(--rivian-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Adventure** is the real brand face. If unavailable, use **Aptos** or **Inter Tight** only as an approximation, not as the visual source of truth.
- For display headlines, compensate with `font-weight: 600`, `line-height: 1`, and `letter-spacing: -0.02em`. Plain Inter at 400 reads too SaaS and loses the Rivian showroom feel.
- For body copy, keep `16px / 24px` and normal weight. Do not over-tighten body tracking; the tightness belongs to headings and labels.
- For mono labels or technical details, use `Adventure Mono`; fallback to `ui-monospace` with slightly reduced weight (`400`, not `500`) to avoid developer-tool harshness.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `text-display-xl` | `clamp(96px, 13.54vi + 26.72px, 200px)` | 600 | 1.0 approx | `-0.02em` inferred |
| `text-display-lg` | `clamp(72px, 6.25vi + 40px, 120px)` | 600 | 1.0 approx | `-0.02em` inferred |
| `text-display-base` | `clamp(56px, 5.21vi + 29.28px, 96px)` | 600 | 1.0 approx | tight |
| `h1 legacy` | `8.8rem` desktop / `6.4rem` mobile | 500 normal override | `8.8rem` / `6.8rem` | default |
| `text-h1` | `56px` | 600 | `60px` | `-2.5px` |
| `text-h4` | `32px` | 600 | `36px` | `-1px` |
| `body100` | `16px` | 400 | `24px` | `0` |
| `body25` | `12px` | 400 | `16px` | `0` |
| `label` | `14px` | 600 | `16px` to `20px` | `-0.01em` |

> ⚠️ The scale is not a generic 16/24/32 ladder. Rivian mixes old Emotion heading rules with newer Tailwind clamp tokens and `text-h*` utility tokens.

### Principles
<!-- SOURCE: manual -->

1. Display type is allowed to be huge because photography supplies context; type should not sit in isolated SaaS cards.
2. Tight tracking is a display/label behavior. Body copy remains readable at `16px / 24px`.
3. Weight 600 is the primary emphasis weight. Weight 700 exists, but using it broadly makes the interface feel heavier than Rivian.
4. `Adventure` is part of the brand identity. A generic system stack is only a fallback, not a design choice.
5. The site uses both `vi` and `cqi` clamp scales, so responsive typography follows viewport and container context.
6. Legal/disclaimer text becomes dense, but brand/editorial areas stay large and sparse.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed key steps)
<!-- SOURCE: auto+manual -->

| Token | Hex |
|---|---|
| `brand-rivianYellow` | `#FFAC00` |
| `yellow-400` | HSL equivalent of vivid Rivian yellow |
| `yellow-500` | darker action/active family |
| `amber-500` | secondary warm family |
| `orange-600` | warning/error-adjacent family |

### 06-2. Brand Dark Variant
<!-- SOURCE: auto -->

| Token | Hex |
|---|---|
| `surface-dark` | `#212121` |
| `surface-primaryAlt-dark` | `#151515` |
| `navbar-card-background[data-theme=dark]` | `#000000` |
| `navbar-card-foreground[data-theme=dark]` | `#FFFFFF` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light | Dark |
|---|---|---|
| base | `#FFFFFF` | `#000000` |
| alt | `#FAFAFA` | `#151515` |
| stone-50 | `#F6F6F6` | `#252826` |
| stroke | `#CBCBCB` | `#494949` |
| muted | `#636363` | `#212121` |
| tertiary | `#ECECEC` | `#333333` |

### 06-4. Accent Families
<!-- SOURCE: auto -->

| Family | Key step | Hex |
|---|---|---|
| Rivian yellow | action | `#FFAC00` |
| Outdoor sky | atmospheric overlay | `#5D767D` |
| Adventure clay | editorial text/surface tint | `#E6E5DF` |
| Video blue-gray | media player legacy | `#73859F` |
| Error red | semantic | `#DC3127` |
| Success green | semantic | `#4A8231` |

### 06-5. Semantic
<!-- SOURCE: auto -->

| Token | Hex | Usage |
|---|---|---|
| `--semantic-disabled` | `#8E8E8E` | disabled / unavailable state |
| `--semantic-error` | `#DC3127` | error |
| `--semantic-info` | `#005E7D` | info |
| `--semantic-success` | `#4A8231` | success |
| `--semantic-warning` | `#D58103` | warning |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--surface-primary` | `#FFFFFF` or `#000000` by theme | page or inverted surface |
| `--surface-primaryAlt` | `#FAFAFA` or `#151515` | alternate surface |
| `--text-primary` | `#000000` or `#FFFFFF` by theme | primary text on current theme |
| `--text-secondary` | `#CBCBCB` | muted text on dark |
| `--text-tertiary` | `#494949` | tertiary copy |
| `--stroke-secondary` | `#CBCBCB` | hairline / border |
| `--navbar-card-background` | `#FFFFFF` or `#000000` | navbar card background |
| `--navbar-card-foreground` | `#000000` or `#FFFFFF` | navbar card text |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---|---|
| white | `#FFFFFF` | 70 |
| black | `#000000` | 43 |
| transparent black | `#00000000` | 35 |
| pale surface | `#F2F2F2` | 20 |
| ink | `#151515` | 18 |
| stroke gray | `#CBCBCB` | 13 |
| dark muted | `#494949` | 11 |
| clay tint | `#E6E5DF` | 11 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.brand-rivian-yellow}` (#FFAC00)** — The command color. It appears as the high-confidence action signal, most visibly on demo-drive style CTAs and hover/active brand states. It should be small, warm, and mechanical, not a page-wide wash.

**`{colors.surface-primary}` (#FFFFFF)** — The clean commerce floor. Rivian uses white for cards, modals, forms, and readable product surfaces so vehicle photography can stay expressive without making the interface muddy.

**`{colors.text-primary}` (#151515)** — The practical black. It is softer than pure #000000 in legacy body CSS and gives the UI an industrial print feel instead of a browser-default harshness.

**`{colors.surface-dark}` (#212121)** — The disclaimer/video ground. Dark sections are not neon EV dashboards; they are matte, near-black fields that let white copy and media controls sit quietly.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--spacing-4` / `--small-s1` | `4px` | micro adjustment |
| `--spacing-8` / `--small-s2` / `--gap-xs` | `8px` | compact toolbar/card gap |
| `--spacing-12` / `--small-s3` | `12px` | navbar padding, micro radius |
| `--spacing-16` / `--small-s4` | `16px` | small content rhythm |
| `--spacing-20` / `--medium-m2` | `20px` | card padding, desktop nav |
| `--spacing-24` / `--medium-m3` | `24px` | medium sections |
| `--spacing-32` / `--medium-m4` | `32px` | modal and section interior |
| `--spacing-40` / `--large-l1` | `40px` | large mobile section spacing |
| `--spacing-64` / `--large-l2` | `64px` | desktop vertical/horizontal air |
| `--spacing-80` / `--large-l3` | `80px` | larger editorial air |
| `--spacing-120` | `120px` | x-laptop large rhythm |

**주요 alias**:
- `--gap-xs` → `8px` compact card/nav gaps
- `--large-l2` → `64px` desktop section/nav offset
- `--large-l3` → `80px` or `120px` depending responsive context

### Whitespace Philosophy
<!-- SOURCE: manual -->

Rivian uses whitespace as a switch between two modes. The top of the page is not whitespace-led; it is image-led, with nav and CTAs floating over motion-heavy photography. Once the page drops into product, card, or legal surfaces, spacing becomes systemized: 8px/12px/20px for chrome, 40px/64px/80px for editorial sections.

The system avoids the common "large empty SaaS hero" mistake. Air is not decoration by itself. It either clears space for a vehicle image, creates tap-safe controls, or lets a large Adventure headline sit without becoming cramped.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--radius-nano` / `--radius-s` | `4px` | micro UI, small controls |
| `--radius-micro` / `--radius-m` | `12px` | navbar toolbar, panels |
| `--radius-macro` / `--radius-l` | `20px` | cards and larger containers |
| `--radius-xl` | `32px` | large rounded surfaces |
| `--radius-mega` / `--radius-xxl` | `40px` | primary pill buttons |
| `--radius-none` | `0` | media/image hard edges |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| nav/card popover | `0 10px 38px -10px #0e121659, 0 10px 20px -15px #0e121633` | Radix-like menu/popover depth |
| Tailwind lg | `0 10px 15px -3px rgba(0,0,0,.1), 0 4px 6px -4px rgba(0,0,0,.1)` | hover card elevation |
| video float | `0 3px 10px rgba(0,0,0,.2)` | floating video player |
| hero text | `drop-shadow-sm` utility | white copy over imagery |
| default chrome | `0 0 #0000` | most UI avoids visible shadow |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| fade-in | `0.5s cubic-bezier(0.55,0,0.9,1)` | body content reveal |
| tooltip enter | `0.22s ease-out` | small tooltip directional motion |
| accordion | `0.2s` to `0.3s ease-in-out` | open/closed height animation |
| navbar card overlay | `opacity var(--card-duration,.15s) ease-in-out` | vehicle card hover overlay |
| video opacity | `500ms delay 300ms ease-out` | video layer reveal |
| hover scale | `scale(1.05)` | selected utility/image hover |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `1920px` for navbar/page frame; observed card and content blocks at `1500px`, `720px`, `555px`, `481px`, `320px`
- **Grid type**: Tailwind CSS Grid and Flexbox; component slots use `data-slot`
- **Column count**: responsive 1-column, 2-column, and `1fr 280px`; cards use `lg:col-span-*`
- **Gutter**: `8px` compact nav/card gap; `20px`/`32px` content gaps; `64px`/`80px` editorial spacing

### Hero
- **Pattern Summary**: `100vh + full-bleed moving vehicle image/video + large left display headline + pill CTA/navigation overlay`
- Layout: full-width background media with absolute overlays and carousel affordances
- Background: automotive photography/video, often with motion blur and outdoor terrain
- **Background Treatment**: image/video overlay with darkening; later sections include `linear-gradient(180deg, #5D767D 0%, transparent 100%)`
- H1: `56px` utility / legacy `8.8rem` possible; weight `500/600`; tracking around `-2.5px` or `-0.02em`
- Max-width: hero copy observed around `35.5rem` mobile to `72rem` desktop in editorial sections

### Section Rhythm
```css
section {
  padding: var(--medium-m4, 32px) var(--medium-m1, 20px);
  max-width: 1920px;
}
@media (min-width: 1024px) {
  section {
    padding: var(--large-l2, 64px) var(--large-l2, 64px);
  }
}
```

### Card Patterns
- **Card background**: `#FFFFFF` or `#000000` depending data theme
- **Card border**: generally none; hairline uses `#CBCBCB`
- **Card radius**: `20px` macro; nav toolbar `12px`/open `20px`
- **Card padding**: `12px`/`16px` compact image cards, `20px` vehicle cards
- **Card shadow**: mostly absent; hover may use Tailwind `shadow-lg`

### Navigation Structure
- **Type**: floating horizontal toolbar with dropdown/panel card system
- **Position**: fixed/absolute over hero in screenshot; root uses max width and top padding
- **Height**: `50px` mobile / `56px` desktop
- **Background**: light translucent/gray toolbar in screenshot; panels use `#FFFFFF` or `#000000`
- **Border**: visually soft through radius and surface; no hard brand-colored border

### Content Width
- **Prose max-width**: `320px`, `481px`, `555px` observed in hero/editorial blocks
- **Container max-width**: `1500px` to `1920px`
- **Sidebar width**: `280px` in `lg:grid-cols-[1fr_280px]`

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `<640px` | single column, large media crops, 393/420/520 image sources |
| Tablet | `768px` | heading shifts, image variants, md utilities |
| Desktop | `1024px` | lg grids, desktop nav/card layouts, larger section spacing |
| Nav container | `920px`, `896px`, `1152px` | container-query toolbar and panel padding adjustments |
| Wide | `1440px`, `1920px`, `2560px`, `3500px`, `4200px` | responsive photography source selection |

### Touch Targets
- **Minimum tap size**: observed buttons use `min-h: 56px`, `min-w: 56px`
- **Button height (mobile)**: `56px` for primary pill controls
- **Input height (mobile)**: not directly isolated; input padding token `--input-pt: 16px`

### Collapsing Strategy
- **Navigation**: compact floating toolbar becomes panel/card system; root height limited by `100dvh`
- **Grid columns**: 1-column mobile, `lg:grid-cols-2`, `lg:grid-cols-[1fr_280px]` on desktop
- **Sidebar**: desktop side column at `280px`; mobile stacks into flow
- **Hero layout**: background remains full-bleed; copy and CTA widths shrink from `72rem` to `35.5rem`

### Image Behavior
- **Strategy**: `<picture>` with many width-specific sources and Cloudinary/Contentful transforms
- **Max-width**: `100%`
- **Aspect ratio handling**: mobile `aspect-[2/3]`, tablet square, desktop `aspect-[3/2]`, wide `aspect-[2/1]`; `object-cover object-bottom`

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary pill button**

```html
<button class="rounded-mega bg-brand-rivianYellow text-brand-black min-h-[56px] px-medium-m1">
  Demo drive
</button>
```

| Spec | Value |
|---|---|
| Background | `#FFAC00` / `hsl(var(--brand))` |
| Text | `#151515` or brand black |
| Radius | `40px` |
| Min size | `56px` height / `56px` width |
| Padding | `20px` horizontal plus inner span padding |
| Hover | remains yellow or moves to brand active state |
| Active | `active:bg-brand-rivianYellow` |

**Inverted media button**

```html
<button class="rounded-mega bg-surface-invertPrimary text-text-invertPrimary min-h-[56px]">
  Watch the video
</button>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` on dark/image surfaces or `#000000` in inverse mode |
| Text | inverse token |
| Radius | `40px` |
| State | `hover:bg-surface-invertTertiary`, `active:bg-surface-neutralDark` |

### Badges

Badges are not a dominant homepage component. When label-like UI appears, it uses compact body/label tokens rather than colored chips.

| Spec | Value |
|---|---|
| Font | `Adventure` |
| Size | `12px` to `14px` |
| Weight | 600 for labels |
| Tracking | `-0.01em` |
| Color | neutral/inverted tokens |

### Cards & Containers

**Navbar vehicle/image card**

```html
<article data-slot="navbar-vehicle-card" data-theme="light">
  <div data-slot="title">R1S</div>
</article>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` light / `#000000` dark |
| Foreground | `#000000` light / `#FFFFFF` dark |
| Radius | `20px` or inherited macro radius |
| Padding | `12px` to `20px` responsive |
| Overlay | `linear-gradient(180deg, rgba(0,0,0,.5) 10%, transparent 40%, rgba(0,0,0,.4))` |
| Hover | overlay opacity transitions to 1 when motion is allowed |

### Navigation

**Floating navbar root**

```html
<header data-slot="navbar-root">
  <nav data-slot="navbar-header-content">...</nav>
</header>
```

| Spec | Value |
|---|---|
| Max width | `1920px` |
| Root padding | `12px` |
| Toolbar height | `50px` mobile / `56px` desktop |
| Open radius | `12px` mobile / `20px` desktop |
| Panel max height | `calc(100dvh - padding - toolbar)` |
| Content gap | `8px` |

### Inputs & Forms

Forms are mostly downstream flows, but the CSS exposes input and autofill behavior.

| Spec | Value |
|---|---|
| Font | inherit `Adventure` |
| Control padding top | `--input-pt: 16px` when floating label is active |
| Autofill surface | inset `#F2F2F2` shadow |
| Required marker | `#A15842` asterisk |
| Disabled | `cursor: not-allowed` |
| Error | semantic `#DC3127` |

### Hero Section

```html
<section data-ga-section="hero">
  <picture>...</picture>
  <h1 class="text-display100 tracking-[-1.8px]">...</h1>
  <button class="rounded-mega">...</button>
</section>
```

| Spec | Value |
|---|---|
| Media | full-bleed vehicle image/video |
| Copy | large Adventure display, tight tracking |
| Overlay | dark image treatment; gradient where needed |
| CTA | pill buttons below/near headline |
| Controls | carousel dots and arrow affordance |
| Header | floating toolbar over image |

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-primary-pill** — `#FFAC00` background, `#151515` foreground, 40px radius, minimum 56px height. Use for demo drive and decisive conversion actions only.

**button-invert-pill** — current inverse surface (`#FFFFFF` on dark imagery, `#000000` on light inverse contexts), 40px radius, minimum 56px height. Use for media/action CTAs on photographic panels.

**nav-glass-toolbar** — soft floating toolbar, 50/56px height, 12px root padding, rounded rectangular frame. Avoid hard full-width corporate nav bars.

**navbar-vehicle-card** — image/vehicle panel with macro radius, responsive padding, and hover overlay. The overlay is craft-critical because cards become photographic rather than flat catalog tiles.

**cookie-consent-modal** — 375px max width, `#FFFFFF` panel, 36px title at 600 weight, 14px body, black pill actions. It is not glamorous, but it shows the same typography/radius discipline.

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
motion-blur-vehicle-hero:
  description: "The lead image presents the vehicle as moving through landscape, not parked in a studio."
  technique: "full-bleed responsive image/video, dark image overlay, object-cover object-bottom, carousel affordances, 100vh-style hero framing"
  applied_to: ["{component.Hero Section}", "vehicle/editorial panels"]
  visual_signature: "outdoor motion sells capability before specs do"

rivian-yellow-command-pill:
  description: "#FFAC00 is isolated to decisive command surfaces rather than spread through the page."
  technique: "background-color #FFAC00 / hsl(var(--brand)); color #151515; border-radius 40px; min-height 56px; min-width 56px"
  applied_to: ["{components.button-primary-pill}", "Demo drive", "primary conversion controls"]
  visual_signature: "a small amber dashboard switch against neutral/photo contexts"

navbar-image-gradient-multiply:
  description: "Navigation image cards preserve photography while making compact labels readable."
  technique: "linear-gradient(to bottom, var(--navbar-image-header-gradient-from) 25%, transparent 100%) with mix-blend-mode: multiply; overlay opacity transition around .15s"
  applied_to: ["{components.image-vehicle-card}", "[data-slot=navbar-image-card] [data-slot=header]:before"]
  visual_signature: "vehicle cards read as photographic tiles, not bordered catalog boxes"

adventure-tight-display:
  description: "Custom Adventure display type is tightened until headlines feel like vehicle badging."
  technique: "font-family Adventure; font-weight 600; clamp(96px, 13.54vi + 26.72px, 200px) / clamp(72px, 6.25vi + 40px, 120px); letter-spacing -0.02em or -2.5px; line-height near 1"
  applied_to: ["hero headlines", "navbar card titles", "editorial section headings"]
  visual_signature: "large words feel machined into matte metal rather than typeset as generic marketing copy"

responsive-art-direction-stack:
  description: "Photography swaps source and crop across many breakpoints instead of scaling one hero image."
  technique: "picture/source widths observed at 393, 420, 520, 744, 1024, 1440, 1920, 2560, 3500, and 4200; aspect-[2/3] mobile, square tablet, aspect-[3/2] desktop, aspect-[2/1] wide"
  applied_to: ["homepage hero", "forever/editorial photography sections"]
  visual_signature: "vehicles and landscapes stay intentionally composed from phone viewport to ultra-wide desktop"
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | short, concrete, capability/offer led | "2026 builds, starting at 1.99% APR" |
| Brand mission | outdoor stewardship, future-facing, plainspoken | "Keep the world adventurous forever" |
| Primary CTA | direct noun/verb command | "Demo drive" |
| Secondary CTA | media or learning action | "Watch the video" |
| Subheading | practical EV/product facts, not abstract AI-style benefits | "long-range electric vehicles..." |
| Tone | rugged, calm, utility-premium; avoids hype punctuation |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Rivian — copy into your root stylesheet */
:root {
  /* Fonts */
  --rivian-font-family:       "Adventure", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --rivian-font-family-code:  "Adventure Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  --rivian-font-weight-normal: 400;
  --rivian-font-weight-bold:   600;

  /* Brand (anchor + pragmatic steps) */
  --rivian-color-brand-25:  #FFF4CC;
  --rivian-color-brand-300: #FFD45C;
  --rivian-color-brand-500: #FFAC00;
  --rivian-color-brand-600: #D58103;   /* semantic warning/darker warm */
  --rivian-color-brand-900: #5A3B00;

  /* Surfaces */
  --rivian-bg-page:    #FFFFFF;
  --rivian-bg-alt:     #FAFAFA;
  --rivian-bg-dark:    #212121;
  --rivian-text:       #151515;
  --rivian-text-muted: #636363;
  --rivian-stroke:     #CBCBCB;

  /* Key spacing */
  --rivian-space-sm:  12px;
  --rivian-space-md:  20px;
  --rivian-space-lg:  64px;

  /* Radius */
  --rivian-radius-sm: 4px;
  --rivian-radius-md: 12px;
  --rivian-radius-lg: 20px;
  --rivian-radius-pill: 40px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Rivian-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          rivianYellow: '#FFAC00',
          black: '#000000',
          white: '#FFFFFF',
        },
        rivianStone: {
          50: '#F6F6F6',
          70: '#636363',
          80: '#494949',
          90: '#212121',
        },
        semantic: {
          error: '#DC3127',
          info: '#005E7D',
          success: '#4A8231',
          warning: '#D58103',
        },
      },
      fontFamily: {
        sans: ['Adventure', 'Helvetica Neue', 'Helvetica', 'Arial', 'sans-serif'],
        mono: ['Adventure Mono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      },
      fontWeight: {
        light: '300',
        normal: '400',
        medium: '500',
        semibold: '600',
        bold: '700',
      },
      borderRadius: {
        nano: '4px',
        micro: '12px',
        macro: '20px',
        mega: '40px',
      },
    },
  },
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Hex |
|---|---|
| Brand primary / CTA | `#FFAC00` |
| Page background | `#FFFFFF` |
| Alternate light surface | `#FAFAFA` |
| Primary text | `#151515` |
| Muted text | `#636363` |
| Dark section | `#212121` |
| Border / stroke | `#CBCBCB` |
| Outdoor overlay | `#5D767D` |

### Example Component Prompts

**Hero Section** — Build a Rivian-style automotive hero: full-bleed motion-blurred vehicle photography, dark overlay, floating rounded navigation, large `Adventure` display headline with `letter-spacing: -0.02em`, and one #FFAC00 pill CTA at 56px height.

**Product Card** — Create a vehicle image card with macro 20px radius, photographic image as primary surface, neutral black/white text tokens, subtle gradient multiply overlay on hover, and no colored border.

**Navigation** — Use a floating toolbar 12px from the viewport edge, 50px mobile / 56px desktop height, rounded 12px/20px corners, compact centered links, and a #FFAC00 "Demo drive" pill on the right.

**Form/Input** — Use `Adventure` typography, 16px input top padding for floating labels, `#F2F2F2` autofill surface, semantic `#DC3127` error color, and 56px tap-safe controls.

### Iteration Guide

- Keep yellow scarce. If every section has #FFAC00, the Rivian signal collapses.
- Use real vehicle/outdoor imagery; abstract EV gradients are off-brand.
- Prefer black/white inversion and stone neutrals over blue "technology" palettes.
- Preserve the 40px pill radius and 56px control height for primary actions.
- Keep display type tight and large; do not replace it with generic Inter 400.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO

- Use `Adventure` or a tightly compensated substitute for the entire interface.
- Anchor primary actions in `#FFAC00` with black text and 40px pill radius.
- Let vehicle photography/video carry the emotional load.
- Use `#FFFFFF`, `#151515`, `#212121`, and stone grays as the real UI palette.
- Keep nav chrome compact, floating, and rounded.
- Use responsive image art direction rather than one stretched hero asset.
- Apply shadows sparingly; depth usually comes from photography and overlays.

### DON'T

- 배경을 `#F8FAFC` 또는 generic SaaS off-white로 두지 말 것 — 대신 `#FFFFFF` 또는 `#FAFAFA` 사용.
- 텍스트를 `#0000FF` 또는 tech-blue 계열로 두지 말 것 — 대신 `#151515` / `#FFFFFF` 사용.
- CTA를 `#0071E3` 또는 EV-blue로 두지 말 것 — 대신 `#FFAC00` 사용.
- 다크 섹션을 `#000000` 순흑 평면으로만 두지 말 것 — 대신 `#212121`와 사진/영상 overlay 사용.
- border를 `#E5E7EB` Tailwind 기본 회색으로 방치하지 말 것 — 대신 `#CBCBCB` 또는 토큰 stroke 사용.
- body를 generic `font-weight: 500`으로 올리지 말 것 — Rivian body는 `400`, emphasis는 `600`.
- primary button radius를 `8px`로 줄이지 말 것 — pill action은 `40px` 계열이다.
- hero를 보라/파랑 `linear-gradient(135deg, #667eea, #764ba2)`로 만들지 말 것 — 실제 hero는 차량 사진/비디오 기반이다.

### 🚫 What This Site Doesn't Use
<!-- SOURCE: manual -->

- No broad blue "electric vehicle technology" palette; blue-gray exists mostly in media/player legacy and atmosphere.
- No second loud brand color. Yellow is the command color; the rest is neutral/photo.
- No decorative icon confetti or emoji-led storytelling.
- No flat SaaS feature-card grid as the primary first impression.
- No heavy global box-shadow system; most chrome stays shadow-light.
- No serif-led luxury editorial identity, despite a `Canela` font face being present.
- No square primary buttons; decisive actions are rounded pills.
- No pure illustration hero; the product is shown through real vehicle imagery.
- No dense dashboard UI on the marketing homepage.
- No all-caps shouting except restrained utility labels.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- The screenshot includes a cookie consent modal that occludes part of the hero. Hero interpretation is based on visible regions plus the underlying HTML/CSS.
- `phase1/typography.json` did not extract a full scale table, so typography scale is reconstructed from inline global CSS and Tailwind tokens in the captured CSS.
- The production CSS includes large VideoJS/Cloudinary player styles that inflate color frequency. Video player colors are treated as secondary unless they also appear in Rivian UI tokens.
- Some colors are HSL custom properties in Tailwind output rather than direct hex tokens; hex mappings are recorded where the source exposed concrete values.
- The file intentionally skips Step 6 RENDER-HTML per user instruction; only `design.md` is generated and validated.
- Live post-cookie hero state was not re-captured in this pass; existing `hero-cropped.png` and HTML were reused.
