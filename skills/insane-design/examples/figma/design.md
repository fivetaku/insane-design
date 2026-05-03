---
schema_version: 3.2
slug: figma
service_name: Figma
site_url: https://www.figma.com
fetched_at: 2026-05-03T06:30:53Z
default_theme: light
brand_color: "#000000"
primary_font: figmaSans
font_weight_normal: 330
token_prefix: f

bold_direction: Canvas Collage
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "CSS custom properties use --f-* tokens, variable fonts, grid columns, button/form aliases, and repeated component patterns."

color_system: monochrome

colors:
  primary: "#000000"
  surface: "#FFFFFF"
  text-primary: "#000000"
  text-inverse: "#FFFFFF"
  error: "#972121"
  canvas-blue: "#00B6FF"
  canvas-green: "#24CB71"
  canvas-purple: "#4D49FC"
  hairline: "rgba(0, 0, 0, 0.08)"

typography:
  display: "figmaSans"
  body: "figmaSans"
  mono: "figmaMono"
  ladder:
    - { token: body, size: "1rem", weight: 330, line_height: "1.45" }
    - { token: nav, size: "1.125rem", weight: 480, line_height: "1.4" }
    - { token: display-sm, size: "2.75rem", weight: 540, line_height: "1.1" }
    - { token: display-lg, size: "4rem", weight: 540, line_height: "1.0-1.1" }
  weights_used: [320, 330, 340, 400, 450, 480, 520, 530, 540, 550]
  weights_absent: [600, 700, 800]

components:
  button-primary: { bg: "{colors.primary}", fg: "{colors.text-inverse}", radius: "8px", padding: "0.75rem 1.3125rem" }
  button-secondary-outline: { bg: "{colors.surface}", fg: "{colors.text-primary}", radius: "8px", border: "1px solid #000000" }
  carousel-control: { bg: "rgba(0, 0, 0, 0.08)", radius: "50%", size: "2.25rem" }
---

# DESIGN.md - Figma

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Figma's homepage is not built from the famous five-color logo as a UI palette. The UI shell is almost entirely black and white: #FFFFFF (`{colors.surface}`) as the working plane, #000000 (`{colors.text-primary}` and `{colors.primary}`) as the decisive action color, and hairline rgba borders for structure. The five-color mark behaves like a stamp left on the edge of the workbench, not like a paint tray poured across the interface. Logo colors appear as identity marks and canvas artifacts, not as the interface's everyday color system.

The core metaphor is a gallery built inside an infinite canvas. The hero does not center a generic SaaS headline over a gradient. It stages a horizontal collage of design fragments, z-indexed screenshots, cropped boards, bright editorial tiles, and carousel controls, then pins a large white prompt card in the middle. It feels less like a brochure and more like a design file accidentally opened to its most photogenic frame: boards sliding past, fragments half-cropped, the prompt card acting as the selected layer. The page sells Figma by showing the mess and possibility of collaborative making, while the chrome around it stays sober.

Typography carries much of the craft. `figmaSans` is variable and heavily tuned: body copy appears at weight 330, CTA text at 480, stronger copy at 540 or 550, with `font-variation-settings` controlling both `"wdth"` and `"wght"`. The black text does not hit like default browser #000; it feels like vector ink set to a precise weight, adjusted until the UI can be inspected without shouting. This makes the site feel softer than a standard Inter SaaS page. It is neither heavy enterprise bold nor thin editorial minimalism.

The motion language is functional and canvas-like. Hover states use short 160ms to 250ms transitions, nav underlines scale into place, button inners translate rather than inflate, and carousel state uses circular controls. There is motion and visual play, but the structural system remains gridded and inspectable. Nothing performs a sales-page flourish; interactions behave like handles, cursors, and layer controls inside a tool.

Figma's negative identity is as important as its visible identity: no invented secondary brand color, no purple-blue SaaS wash, no card-shadow dashboard aesthetic, no 700-weight headline blast. Shadow is not a universal depth language; depth comes from cropping, overlap, and z-indexed artifacts. The page is a whiteboard with a disciplined black UI layer and a constantly changing canvas behind it, a product demo where the site almost removes its own frame so the act of making can occupy the center.

### Key Characteristics

- Black-and-white UI chrome: #000000 and #FFFFFF dominate actions, text, and surfaces.
- Logo colors are identity/collage colors, not the primary UI palette.
- Fixed top navigation with a 1px rgba hairline and large 1rem spacing.
- Variable `figmaSans` weights such as 330, 480, 540, and 550 instead of normal 400/700 rhythm.
- Hero is a horizontal infinite-canvas collage, not a centered abstract gradient.
- Primary CTAs are black filled rectangles with 8px radius, not pill buttons.
- Carousel controls use 2.25rem circular controls with rgba fill and black hover inversion.
- The design grid scales from 12 to 24 to 48 columns as viewport width increases.
- Motion is short and utilitarian: 160ms ease-out for button/chrome, 250ms for nav reveals.
- The overall surface stays clean so screenshots, boards, and product artifacts can carry color.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Canvas Collage
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **black-white product chrome over an infinite-canvas collage hero**으로 기억된다.
> **Code Complexity**: high - variable fonts, responsive grid columns, carousel layering, motion states, and multiple component aliases are required.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Figma처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "figmaSans", "figmaSans Fallback", "SF Pro Display", system-ui, helvetica, sans-serif;
  font-weight: 330;
  font-variation-settings: "wdth" 98, "wght" 330;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 액션 컬러 */
:root { --brand: #000000; }
.primary-action {
  background: var(--brand);
  color: #FFFFFF;
  border-radius: 8px;
  padding: 0.75rem 1.3125rem;
}
```

**절대 하지 말아야 할 것 하나**: Figma 로고의 #FF3737, #FF7237, #00B6FF, #24CB71, #874FFF를 UI 전체의 brand ramp로 확장하지 말 것. 실제 UI action color는 #000000이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.figma.com` |
| Fetched | 2026-05-03T06:30:53Z |
| Extractor | phase1 reuse: existing HTML/CSS/screenshot artifacts |
| HTML size | 1,530,148 bytes |
| CSS files | 3 files, 208,823 chars |
| Token prefix | `--f-*` |
| Method | CSS custom properties, frequency candidates, typography extractor, screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js-style static asset output on Netlify path (`/_netlify/_next/static/...`), with Sanity CDN media.
- **Design system**: Figma marketing system - prefix `--f-*`.
- **CSS architecture**:
  ```css
  --f-font-*                 font family tokens
  --f-bg-color               local section surface
  --f-text-color             local section foreground
  --f-primary-btn-*          action alias
  --f-form-*                 form and control alias
  --f-columns / --f-gutter   responsive layout grid
  ```
- **Class naming**: generated atomic-ish classes such as `.fig-fa3ze6`, `.fig-1jciw8t`, `.fig-1gijkma`.
- **Default theme**: light, bg = `#FFFFFF`, text = `#000000`.
- **Font loading**: preloaded `.woff2` assets plus CSS variables for `figmaSans`, `figmaMono`, and `ABCWhytePlusVariable`.
- **Canonical anchor**: fixed homepage navigation and hero carousel around the line "Make an infinite canvas gallery."

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `figmaSans` (site font, variable)
- **Body font**: `figmaSans`, `figmaSans Fallback`, `SF Pro Display`, system-ui, helvetica, sans-serif
- **Code font**: `figmaMono`, `figmaMono Fallback`, `SF Mono`, menlo, monospace
- **Alternate display family**: `ABCWhytePlusVariable`, `ABCWhytePlusVariable Fallback`, Whyte, sans-serif
- **Weight normal / bold**: `330` / `540-550`

```css
:root {
  --f-font-sans: 'figmaSans', 'figmaSans Fallback', SF Pro Display, system-ui, helvetica, sans-serif;
  --f-font-mono: 'figmaMono', 'figmaMono Fallback', SF Mono, menlo, monospace;
  --f-font-whyte-variable: 'ABCWhytePlusVariable', 'ABCWhytePlusVariable Fallback', Whyte, sans-serif;
}

body {
  font-family: var(--f-font-sans);
  font-weight: 330;
  font-variation-settings: "wdth" 98, "wght" 330;
}
```

### Note on Font Substitutes

- **`figmaSans` substitute**: use `Inter` only as a measured fallback, not as the design identity. Set normal text to `font-weight: 330` if variable support exists; otherwise use `font-weight: 350` or `400` with slightly reduced contrast in surrounding copy.
- **Display compensation**: for large headings, use `Inter Tight` or `Geist` at 540-560 and keep letter-spacing negative. Do not jump to 700.
- **Line-height correction**: body copy should sit around `1.45`; CTA/nav text around `1.4`. If the fallback feels taller, reduce line-height by 0.02-0.04.
- **Mono substitute**: `SF Mono` or `ui-monospace` is acceptable for code-like labels, but keep mono rare. Figma's homepage is not a developer-docs surface.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| body-copy | `1rem` | `330` | `1.45` | `0` |
| nav-link / cta | `1.125rem` | `480` | `1.4` | `-0.005625rem` |
| large-body | `1.25rem` | `480` | `1.4` | `-0.00625rem` |
| feature-copy | `1.375rem` | `330-540` | `1.35` | `-0.006875rem` |
| display-sm | `2.75rem` | `540` | `1.1` | `-0.0275rem` |
| display-md | `4rem` | `540` | `1.0-1.1` | `-0.0525rem` |
| display-lg | `5.375rem` | `540-550` | `1.0` | `-0.09rem` to `-0.1075rem` |

> ⚠️ Figma's type system is variable-weight and optical. The signature is 330/480/540, not the common SaaS 400/600/700 ladder.

### Principles

1. Body copy is light but not fragile: `330` gives the homepage a design-tool softness while keeping black text legible on white.
2. CTA and nav text sit at `480`, not 500 or 600. This preserves confidence without making the chrome feel enterprise-heavy.
3. Display typography relies on negative tracking. Large text without negative letter-spacing will feel loose and un-Figma.
4. Width axis matters. The observed `font-variation-settings: "wdth" 98` keeps labels compact without looking condensed.
5. Heavy weights are deliberately absent. The page avoids 700/800 headline shouting and lets collage scale create drama.
6. The text hierarchy is not just size. Weight, width, line-height, and container placement all change together.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (monochrome action)

| Token | Hex |
|---|---|
| `--f-primary-btn-bg-color` | `#000000` |
| `--f-primary-btn-text-color` | `#FFFFFF` |
| `--f-emphasis-btn-bg-color` | `#000000` |
| `--f-emphasis-btn-text-color` | `#FFFFFF` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| dark section `--f-bg-color` | `#000000` |
| dark section `--f-text-color` | `#FFFFFF` |
| dark badge text | `#FFFFFF` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| page surface | `#FFFFFF` | `#000000` |
| primary text | `#000000` | `#FFFFFF` |
| secondary text | `rgba(0, 0, 0, 0.65)` | `rgba(255, 255, 255, 0.6)` |
| control fill | `rgba(0, 0, 0, 0.08)` | `rgba(255, 255, 255, 0.16)` |
| hover control | `rgba(0, 0, 0, 0.16)` | `rgba(255, 255, 255, 0.24)` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| logo/canvas red | logo artifact | `#FF3737` |
| logo/canvas orange | logo artifact | `#FF7237` |
| logo/canvas blue | section/collage | `#00B6FF` |
| logo/canvas green | section/collage | `#24CB71` |
| logo/canvas purple | collage/accent | `#4D49FC` |
| form error | error background | `#972121` |

### 06-5. Semantic

| Token | Hex / Value | Usage |
|---|---|---|
| `--f-bg-color` | `#FFFFFF` / `#000000` / section accent | section-local background |
| `--f-text-color` | `#000000` / `#FFFFFF` | section-local foreground |
| `--f-text-secondary-color` | `rgba(0, 0, 0, 0.65)` | supporting text |
| `--f-form-error-bg-color` | `#972121` | error state |
| `--f-form-input-bg-color` | `rgba(0, 0, 0, 0.08)` | carousel and input surface |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--f-primary-btn-bg-color` | `#000000` | primary CTA fill |
| `--f-primary-btn-text-color` | `#FFFFFF` | primary CTA label |
| `--f-emphasis-btn-bg-color` | `#000000` | emphasis action |
| `--f-emphasis-btn-text-color` | `#FFFFFF` | emphasis action text |
| `--f-form-input-bg-color` | `rgba(0, 0, 0, 0.08)` | controls and form surfaces |

### 06-7. Dominant Colors (actual CSS frequency)

| Token | Hex | Frequency |
|---|---|---:|
| black | `#000000` | 259 |
| white | `#FFFFFF` | 166 |
| error red | `#972121` | 25 |
| canvas purple | `#4D49FC` | 5 |
| muted slate | `#697485` | 4 |
| canvas blue | `#00B6FF` | 3 |
| canvas green | `#24CB71` | 3 |
| pale cyan | `#C7F8FB` | 3 |

### 06-8. Color Stories

**`{colors.primary}` (`#000000`)** - Figma's real UI action color. It fills primary buttons, emphasis buttons, focus outlines, and hover inversions. It should be treated as the brand color for interface reproduction.

**`{colors.surface}` (`#FFFFFF`)** - The working canvas. White is not empty decoration here; it is the neutral plane that lets product fragments and screenshots feel editable.

**`{colors.text-primary}` (`#000000`)** - Text is high-contrast and matter-of-fact. The softness comes from variable font weight, not from gray primary text.

**`{colors.error}` (`#972121`)** - The strongest recurring chromatic semantic token. It belongs to form error surfaces, not to brand storytelling.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--f-gutter` mobile | `24px` | base page edge spacing |
| `--f-max-content-width` | `1440px` | main content rail |
| `--f-max-content-width` large | `1680px` | extra-wide page rail |
| `--f-col-width` | `calc(min(100vw, var(--f-max-content-width)) / var(--f-columns))` | responsive grid unit |
| `--f-lego-block-padding` | `5rem` | section block padding |
| `--f-lego-block-padding` tablet+ | `7.5rem` | larger section rhythm |
| `--f-lego-block-padding` wide | `10rem` | wide viewport breathing room |
| nav padding block | `1rem` | fixed header vertical rhythm |
| logo marquee section | `2.5rem` | compact trust-band spacing |

**주요 alias**:
- `--f-columns` -> `12 / 24 / 48` by breakpoint
- `--f-gutter` -> `24px`, then column-derived gutters on larger screens
- `.fig-2qv4k` -> `width: calc(min(var(--f-max-content-width), 100vw) - var(--f-gutter) * 2)`

### Whitespace Philosophy

Figma's whitespace is not a luxury-gallery void. It is product-canvas air. The fixed header is dense and practical, the hero is layered and busy, and then the copy below gets a clean centered rail so the eye can rest after the collage.

The spacing system scales through columns rather than arbitrary page margins. At wide viewports the system moves to 48 columns and 1680px max width, which lets the collage feel panoramic without turning text rails into unreadable lines. The page alternates "busy artifact field" and "quiet explanation rail."

---

## 08. Radius
<!-- SOURCE: auto -->

| Token / Pattern | Value | Context |
|---|---:|---|
| primary button | `8px` | filled black CTA |
| generic radius | `0.5rem` | recurring rounded UI |
| carousel control | `50%` | circular media controls |
| small chip/control | `0.25rem` / `0.375rem` | compact UI elements |
| hero prompt card | approx `16px-18px` visual | large floating prompt surface |
| squared collage/image edges | `0` | canvas artifacts and screenshot tiles |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `1440px`, expanding to `1680px` on very wide screens.
- **Grid type**: CSS variable column grid with flex/grid component internals.
- **Column count**: `1` base, `12` at wider breakpoint, then `24`, then `48`.
- **Gutter**: `24px` base; later derived from `--f-col-width`.

### Hero

- **Pattern Summary**: `fixed nav + panoramic carousel collage + centered white prompt card + black/blue CTA`.
- Layout: layered horizontal carousel with slide groups and a central prompt-card overlay.
- Background: product/design-board imagery and colorful canvas artifacts.
- **Background Treatment**: image/collage field, not gradient mesh. The color comes from real screenshot tiles and logo-like fragments.
- H1: large variable sans, visually around `44px-64px` in the hero prompt, weight around `540`, tight tracking.
- Max-width: page rail based on `calc(min(var(--f-max-content-width), 100vw) - var(--f-gutter) * 2)`.

### Section Rhythm

```css
section {
  padding-block: 2.5rem; /* compact bands such as logo marquee */
  max-width: min(1440px, 100vw);
}

.lego-block {
  padding-block: var(--f-lego-block-padding); /* 5rem -> 7.5rem -> 10rem */
}
```

### Card Patterns

- **Card background**: `#FFFFFF` for hero prompt/card surfaces.
- **Card border**: subtle rgba hairline or none; hero prompt uses a visible outline-like edge.
- **Card radius**: 8px for small controls, larger rounded rectangle for hero prompt.
- **Card padding**: hero prompt has generous horizontal/vertical padding; buttons use `0.75rem 1.3125rem`.
- **Card shadow**: not a broad SaaS elevation system. Depth is mostly z-index layering and collage overlap.

### Navigation Structure

- **Type**: horizontal desktop nav with dropdown triggers.
- **Position**: fixed top.
- **Height**: approximately 80px including `padding-block: 1rem`.
- **Background**: `#FFFFFF`.
- **Border**: `box-shadow: 0 1px 0 rgba(0, 0, 0, 0.08)`.
- **Interaction**: dropdown label uses underline reveal via `:after` transform and opacity.

### Content Width

- **Prose max-width**: centered readable rail inside the global content width.
- **Container max-width**: `1440px` normal, `1680px` extra-wide.
- **Sidebar width**: N/A on homepage; no persistent sidebar pattern observed.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Compact | `max-width: 559px` | mobile-specific handling |
| Small+ | `min-width: 560px` | first content expansion |
| Tablet | `min-width: 768px` | larger typography/layout changes |
| Desktop | `min-width: 960px` | desktop nav and grid behavior |
| Wide | `min-width: 1280px` / `1440px` | richer canvas/grid density |
| Ultra | `min-width: 1920px` | font and content scaling |

### Touch Targets

- **Minimum tap size**: primary nav/CTA controls visually clear; carousel controls are `2.25rem` and should be raised to 44px if rebuilding for mobile-first accessibility.
- **Button height (mobile)**: inferred from `0.75rem` vertical padding plus 1rem-1.125rem text.
- **Input height (mobile)**: form-specific states not surfaced on the homepage.

### Collapsing Strategy

- **Navigation**: desktop horizontal nav; mobile state not fully measured from screenshot, but CSS includes compact breakpoints.
- **Grid columns**: columns expand with min-width breakpoints rather than fixed 12-column everywhere.
- **Sidebar**: none.
- **Hero layout**: collage can crop horizontally; central prompt remains the focal layer.

### Image Behavior

- **Strategy**: CDN images and SVG marks, layered as product/canvas fragments.
- **Max-width**: component-scoped, not a single global image rule in the sampled evidence.
- **Aspect ratio handling**: collage tiles preserve source aspect ratios and tolerate cropping/overlap.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA**

```html
<a class="fig-fa3ze6" href="/signup">
  <span class="btn-inner fig-1qhfzz9">
    <span class="btn-text fig-cx0h0r">Get started for free</span>
  </span>
</a>
```

| Property | Value |
|---|---|
| display | `inline-flex` |
| bg | `#000000` |
| color | `#FFFFFF` |
| radius | `8px` |
| padding | `0.75rem 1.3125rem` |
| font | `figmaSans`, `1rem-1.125rem`, weight `480` |
| transition | `border-radius 160ms ease-out`, inner `translate 160ms ease-out` |

States: hover removes text decoration; inner movement is handled through `.btn-inner` translate transitions. Disabled/loading not observed for this homepage CTA.

**Secondary CTA**

```html
<a class="sales-button" href="/contact-sales">Contact sales</a>
```

Spec: white background, black text, black 1px border, 8px radius, similar padding and typographic treatment. It sits immediately before the black primary CTA.

### Badges

Badges are semantic aliases rather than logo-color chips:

| Property | Light value | Dark value |
|---|---|---|
| text | `#000000` | `#FFFFFF` |
| bg | `rgba(0, 0, 0, 0.08)` | `rgba(255, 255, 255, 0.16)` |
| role | small labels, local section metadata | inverse labels on dark sections |

### Cards & Containers

**Hero prompt card**

```html
<article aria-label="Make an infinite canvas gallery">
  <div class="prompt-card">Make an infinite canvas gallery</div>
</article>
```

| Property | Value |
|---|---|
| surface | `#FFFFFF` |
| text | `#000000` |
| radius | large rounded rectangle, visually above 8px |
| role | focal prompt over carousel/collage |
| shadow | restrained; depth comes from overlay/layering |
| visual rule | card floats above imagery, not inside a card grid |

### Navigation

```html
<header class="fig-1jciw8t">
  <nav aria-label="Main">
    <button class="dropdown-label fig-11zdimt">Products</button>
  </nav>
</header>
```

| Property | Value |
|---|---|
| position | `fixed; inset: 0 0 auto` |
| bg | `#FFFFFF` |
| color | `#000000` |
| divider | `box-shadow: 0 1px 0 rgba(0, 0, 0, 0.08)` |
| nav item padding | `0.5rem` |
| hover/focus | underline pseudo-element scales with 250ms transform/opacity |
| focus | `outline: var(--f-text-color, #000000) dashed 2px; outline-offset: 4px` |

### Inputs & Forms

Homepage form fields are not prominent, but form tokens are present:

| Token | Value | Use |
|---|---|---|
| `--f-form-input-bg-color` | `rgba(0, 0, 0, 0.08)` | input/control fill |
| `--f-form-select-hover-bg-color` | `rgba(0, 0, 0, 0.16)` | select hover |
| `--f-form-placeholder-text-color` | `rgba(0, 0, 0, 0.5)` | placeholder |
| `--f-form-error-bg-color` | `#972121` | error bg |
| `--f-form-error-text-color` | `#FFFFFF` | error text |

### Hero Section

The hero combines a fixed header, carousel slide groups, a prompt card, and circular controls:

```html
<section class="homepage-hero">
  <div role="group" aria-roledescription="slide">
    <article aria-label="Make an infinite canvas gallery"></article>
  </div>
  <button aria-label="Next slide" class="fig-1qn7s3f"></button>
</section>
```

| Element | Spec |
|---|---|
| collage field | horizontally overflowing design artifacts and media tiles |
| prompt card | white rounded rectangle centered over the collage |
| carousel control | `2.25rem` circle, rgba fill |
| disabled control | transparent bg + `1px solid rgba(0, 0, 0, 0.08)` |
| hover control | bg `#000000`, color `#FFFFFF` |

### 13-2. Named Variants

**button-primary-black**

| Property | Value |
|---|---|
| bg | `#000000` |
| fg | `#FFFFFF` |
| radius | `8px` |
| padding | `0.75rem 1.3125rem` |
| typography | `figmaSans`, weight `480`, line-height `1.4` |

**button-secondary-outline**

| Property | Value |
|---|---|
| bg | `#FFFFFF` |
| fg | `#000000` |
| border | `1px solid #000000` |
| radius | `8px` |

**carousel-control-circle**

| Property | Value |
|---|---|
| size | `2.25rem` x `2.25rem` |
| bg | `rgba(0, 0, 0, 0.08)` |
| radius | `50%` |
| hover | bg `#000000`, fg `#FFFFFF` |

**nav-dropdown-label**

| Property | Value |
|---|---|
| bg | transparent |
| padding | `0.5rem` |
| underline | pseudo-element, `height: 1px`, currentColor |
| transition | `transform 250ms`, `opacity 250ms` |

### 13-3. Signature Micro-Specs

```yaml
infinite-canvas-collage-hero:
  description: "real product/design artifacts create the hero atmosphere instead of an abstract SaaS background"
  technique: "layered carousel groups with image/SVG fragments, horizontal overflow/crop, central #FFFFFF prompt card above the artifact field"
  applied_to: ["{component.hero-section}", "{component.hero-prompt-card}"]
  visual_signature: "the page opens like a Figma file zoomed out across many boards, with the prompt card acting as the selected layer"

figma-variable-axis-softness:
  description: "soft but precise type density produced by variable axes rather than standard 400/700 weights"
  technique: "font-variation-settings: \"wdth\" 98, \"wght\" 330/480/540; display tracking down to -0.09rem to -0.1075rem"
  applied_to: ["{typography.body}", "{component.button-primary}", "{component.nav-dropdown-label}", "display text"]
  visual_signature: "black text reads like tuned vector ink, confident without enterprise-heavy boldness"

monochrome-tool-chrome:
  description: "the five-color logo is withheld from the interaction system so the UI behaves like product chrome"
  technique: "primary and emphasis action aliases resolve to #000000 on #FFFFFF; secondary surfaces use rgba(0, 0, 0, 0.08) rather than chromatic fills"
  applied_to: ["{component.button-primary-black}", "{component.button-secondary-outline}", "{component.carousel-control-circle}"]
  visual_signature: "color belongs to the canvas artifacts while navigation and actions stay black-and-white"

hairline-fixed-nav:
  description: "fixed navigation is separated by a single measured line, not by shadow elevation"
  technique: "position: fixed; background: #FFFFFF; box-shadow: 0 1px 0 rgba(0, 0, 0, 0.08); nav padding around 0.5rem-1rem"
  applied_to: ["{component.navigation}", "{component.nav-dropdown-label}"]
  visual_signature: "the header feels like a thin tool rail pinned over the canvas, with almost no visual mass"

underline-reveal-nav:
  description: "navigation hover feedback uses a drawn-line reveal instead of a color change"
  technique: "pseudo-element height: 1px; transform: translateY(3px) scaleY(0); transition: transform 250ms, opacity 250ms"
  applied_to: ["{component.nav-dropdown-label}", "dropdown labels and nav highlights"]
  visual_signature: "a precise drafting-line gesture appears under the label, matching Figma's tool-like interaction language"
```

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Figma - copy into your root stylesheet */
:root {
  /* Fonts */
  --f-font-sans: 'figmaSans', 'figmaSans Fallback', SF Pro Display, system-ui, helvetica, sans-serif;
  --f-font-mono: 'figmaMono', 'figmaMono Fallback', SF Mono, menlo, monospace;
  --f-font-weight-normal: 330;
  --f-font-weight-strong: 540;

  /* Monochrome action system */
  --f-color-brand-25:  #FFFFFF;
  --f-color-brand-300: #697485;
  --f-color-brand-500: #000000;
  --f-color-brand-600: #000000;
  --f-color-brand-900: #000000;

  /* Surfaces */
  --f-bg-page: #FFFFFF;
  --f-bg-dark: #000000;
  --f-text: #000000;
  --f-text-inverse: #FFFFFF;
  --f-text-muted: rgba(0, 0, 0, 0.65);
  --f-hairline: rgba(0, 0, 0, 0.08);

  /* Key spacing */
  --f-gutter: 24px;
  --f-max-content-width: 1440px;
  --f-space-sm: 0.5rem;
  --f-space-md: 1rem;
  --f-space-lg: 2.5rem;
  --f-lego-block-padding: 5rem;

  /* Radius */
  --f-radius-sm: 0.375rem;
  --f-radius-md: 8px;
  --f-radius-round: 50%;
}

body {
  background: var(--f-bg-page);
  color: var(--f-text);
  font-family: var(--f-font-sans);
  font-weight: var(--f-font-weight-normal);
  font-variation-settings: "wdth" 98, "wght" 330;
}

.figma-container {
  width: calc(min(var(--f-max-content-width), 100vw) - var(--f-gutter) * 2);
  margin-inline: auto;
}

.figma-primary-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1.3125rem;
  border: 0;
  border-radius: var(--f-radius-md);
  background: #000000;
  color: #FFFFFF;
  font: inherit;
  font-weight: 480;
  font-variation-settings: "wdth" 98, "wght" 480;
  line-height: 1.4;
  text-decoration: none;
  transition: border-radius 160ms ease-out;
}

.figma-nav {
  position: fixed;
  inset: 0 0 auto;
  z-index: 20;
  background: #FFFFFF;
  color: #000000;
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.08);
}

.figma-carousel-control {
  width: 2.25rem;
  height: 2.25rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 0;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.08);
  color: #000000;
}

@media (hover: hover) and (pointer: fine) {
  .figma-carousel-control:hover {
    background: #000000;
    color: #FFFFFF;
  }
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex / Value |
|---|---|---|
| Brand primary | `{colors.primary}` | `#000000` |
| Background | `{colors.surface}` | `#FFFFFF` |
| Text primary | `{colors.text-primary}` | `#000000` |
| Text muted | secondary text | `rgba(0, 0, 0, 0.65)` |
| Border | `{colors.hairline}` | `rgba(0, 0, 0, 0.08)` |
| Success / canvas green | `{colors.canvas-green}` | `#24CB71` |
| Error | `{colors.error}` | `#972121` |

### Example Component Prompts

#### Hero Section

```text
Figma homepage style hero를 만들어줘.
- 배경: #FFFFFF
- 구조: fixed white nav 아래에 horizontally cropped infinite-canvas collage
- 중앙 카드: white rounded rectangle, black text, subtle edge, z-index above imagery
- H1: figmaSans, 44-64px, weight 540, tight negative tracking
- CTA: black #000000 button, white #FFFFFF text, 8px radius, padding 0.75rem 1.3125rem
- 금지: purple-blue gradient background, logo colors as full UI palette
```

#### Card Component

```text
Figma style floating prompt card를 만들어줘.
- surface: #FFFFFF, text: #000000
- radius: larger than 8px, visually soft but not pill
- depth: heavy shadow 대신 layered collage 위 z-index로 떠 보이게
- typography: figmaSans or Inter fallback, weight 540 for prompt, body 330
- surrounding field: cropped screenshots, boards, and artifact tiles
```

#### Badge

```text
Figma style badge를 만들어줘.
- light bg: rgba(0, 0, 0, 0.08), text #000000
- dark bg: rgba(255, 255, 255, 0.16), text #FFFFFF
- radius: compact rounded, not a saturated color pill
- brand logo colors는 badge fill로 확장하지 말 것
```

#### Navigation

```text
Figma style top navigation을 만들어줘.
- fixed top, bg #FFFFFF, text #000000
- bottom divider: 0 1px 0 rgba(0, 0, 0, 0.08)
- links: 1.125rem figmaSans/Inter, weight 480, padding 0.5rem
- dropdown hover: 1px currentColor underline reveal with transform/opacity 250ms
- right CTAs: Contact sales outline, Get started for free black fill
```

### Iteration Guide

- **색상 변경 시**: #000000 action system을 먼저 유지한다. 로고 색은 collage/accent로만 사용한다.
- **폰트 변경 시**: 330/480/540 ladder를 유지한다. 400/700으로 단순화하면 Figma 특유의 부드러운 밀도가 사라진다.
- **여백 조정 시**: 24px gutter와 1440px/1680px content rail을 기준으로 조정한다.
- **새 컴포넌트 추가 시**: 8px button radius, rgba hairline, black-white action contrast를 우선 적용한다.
- **모션 추가 시**: 160ms-250ms 범위의 짧은 transform/opacity 중심으로 유지한다.
- **히어로 변형 시**: 추상 gradient 대신 실제 product/canvas artifact를 배치한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#000000` as the primary UI action color and `#FFFFFF` as the main page surface.
- Keep Figma logo colors confined to logo marks, collage artifacts, and editorial canvas moments.
- Use variable font weights around 330, 480, 540, and 550.
- Build the hero as layered design artifacts with a central prompt/card overlay.
- Use fixed white navigation with a subtle `rgba(0, 0, 0, 0.08)` divider.
- Use short 160ms-250ms transitions for nav underlines, button inner movement, and controls.
- Let screenshots and product fragments carry color while UI chrome remains monochrome.
- Preserve real token names such as `--f-primary-btn-bg-color` and `--f-form-input-bg-color`.

### ❌ DON'T

- main page background를 `#000000`으로 두지 말 것 - dark section이 아닌 기본 page surface는 `#FFFFFF` 사용.
- primary text를 muted accent `#697485`로 두지 말 것 - 대신 실제 primary text `#000000` 사용.
- primary CTA를 canvas accent `#4D49FC`로 두지 말 것 - 대신 `#000000` 사용.
- primary CTA text를 canvas tint `#C7F8FB`로 두지 말 것 - 대신 `#FFFFFF` 사용.
- error state를 logo red `#FF3737`로 두지 말 것 - 대신 실제 form error bg `#972121` 사용.
- Figma logo blue `#00B6FF`를 전체 link color로 두지 말 것 - link/action은 `#000000` 중심이다.
- body에 `font-weight: 400`만 사용 금지 - Figma homepage body signature는 330이다.
- headline에 `font-weight: 700` 사용 금지 - display emphasis는 540/550 계열이다.
- CTA를 999px pill로 만들지 말 것 - observed primary button radius는 8px이다.
- hero background를 `linear-gradient(135deg, #4D49FC, #00B6FF)`로 만들지 말 것 - 실제 hero는 image/canvas collage다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **Second UI brand color**: absent. The interface does not promote a blue/purple secondary action system.
- **Logo palette as UI system**: absent. The five-color mark is not expanded into full UI ramps.
- **Heavy SaaS gradient**: never for the main hero background.
- **700/800 display weight**: absent from the homepage signature. Emphasis is variable and moderate.
- **Pill-first CTA language**: absent. Buttons are rounded rectangles with 8px radius.
- **Card-grid landing page formula**: absent in the first viewport. The hero is a collage carousel, not three feature cards.
- **Deep elevation system**: absent. Depth comes from layering, cropping, and media, not heavy shadow stacks.
- **Persistent sidebar**: absent. This is a marketing homepage, not the app dashboard shell.
- **Muted primary text**: absent. Primary text is #000000; softness comes from font weight.
- **Generic stock illustration**: absent. Visuals are product/canvas artifacts and real creative outputs.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single URL scope**: this guide is based on `https://www.figma.com` homepage artifacts. Product subpages such as Design, FigJam, Dev Mode, pricing, and enterprise pages may use different local section colors.
- **Cookie overlay present in screenshot**: the captured hero includes a cookie notice over the lower-right area. Layout interpretation focuses on the underlying nav/hero/collage system, but that overlay blocks part of the first viewport.
- **Desktop-first visual observation**: screenshot evidence is 1280x800. CSS breakpoints were observed, but mobile screenshots were not manually inspected.
- **Dynamic carousel state**: the exact timing and slide sequencing are partially inferred from HTML/CSS and screenshot. JavaScript runtime state was not deeply profiled.
- **Form states not fully surfaced**: form/input tokens exist, including error colors, but full validation/loading flows were not visited.
- **Exact hero prompt radius**: visual radius is estimated from screenshot because the specific prompt-card class was not isolated as a stable semantic component.
- **Logo wall contamination risk**: chromatic hex frequency includes logo/SVG and customer/media artifacts. Brand color selection intentionally prioritizes CTA/action tokens over chromatic frequency.
- **Font license/substitution**: `figmaSans` and `ABCWhytePlusVariable` availability outside the site is not assumed. Substitute guidance is approximate.
- **Dark mode mapping**: dark section token pairs are present, but a complete dark-mode system map was not validated across subflows.
- **Report HTML skipped by request**: Step 6 RENDER-HTML was intentionally skipped; this artifact is design.md only.
