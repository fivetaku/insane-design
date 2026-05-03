---
schema_version: 3.2
slug: pitch
service_name: Pitch
site_url: https://pitch.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#8D49F7"
primary_font: Mark Pro
font_weight_normal: 400
token_prefix: pitch

bold_direction: Gradient Confidence
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Production CSS exposes real component variables, hashed modules, responsive rules, and motion primitives, but not a complete public token system."

colors:
  brand-purple: "#8D49F7"
  brand-blue-violet: "#6B53FF"
  surface-white: "#FFFFFF"
  text-ink: "#2B2A35"
  border-soft: "#DDDFE5"
  surface-mist: "#F8F8FB"
  deep-stage: "#030B1D"
typography:
  display: "Mark Pro"
  body: "Eina01"
  ladder:
    - { token: hero, size: "clamp-derived / visual 80px+", weight: 800, tracking: "-0.02em" }
    - { token: h1, size: "2.625rem", weight: 800, tracking: "-0.02em" }
    - { token: body-large, size: "1.125rem", weight: 400, tracking: "0" }
    - { token: nav, size: "1rem", weight: 400, tracking: "0" }
    - { token: label-caps, size: ".8125rem", weight: 700, tracking: ".1em" }
  weights_used: [400, 600, 700, 800, 950]
  weights_absent: [300, 500]
components:
  button-primary: { bg: "{colors.surface-white}", fg: "{colors.brand-blue-violet}", radius: "6px", padding: "0 1.5em", shadow: "none" }
  button-secondary-outline: { bg: "transparent", fg: "{colors.surface-white}", radius: "6px", border: "1px solid rgba(255,255,255,.65)" }
  nav-gradient: { bg: "linear-gradient(95.14deg, {colors.brand-purple}, {colors.brand-blue-violet} 103.53%)", height: "4.5rem" }
  tab-caps: { fg: "hsla(0,0%,100%,.8)", active: "{colors.surface-white}", tracking: ".1em" }
---

# DESIGN.md - Pitch (Designer Guidebook)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Pitch does not behave like a neutral productivity app. The homepage opens like a presentation title slide that already won the room: a full-bleed purple stage, oversized white type, soft 3D ribbons at the corners, and two calm CTAs placed exactly where a presenter would pause. The product promise is not "manage decks"; it is "make the moment feel composed."

The signature move is the diagonal violet gradient. `#8D49F7` (`{colors.brand-purple}`) and `#6B53FF` (`{colors.brand-blue-violet}`) are not small accent colors. They are the atmosphere. Pitch lets the hero become the slide canvas, then places the interface preview just low enough that the next section peeks into view. This creates a brand bridge between marketing page and deck editor: the site itself feels like a deck cover. There is no second brand color trying to share the room; the violet field is the keynote lighting, not a decorative stripe.

The page is staged like a rehearsed demo rather than a brochure. The hero is the title slide, the product preview is the projected screen, and the tabbed workflow below behaves like the presenter advancing through sections. The site does not pretend to be an operating system dashboard; it keeps the marketing surface theatrical, then lets the browser mockup supply evidence.

Typography splits personality by role. Display copy uses `Mark Pro`, heavy weights, and negative tracking; navigation and operational copy use `Eina01` with calmer metrics. That split matters. If everything is set in generic Inter, the product becomes a standard SaaS page. Pitch needs the rounded, confident, almost campaign-like display voice paired with a precise product UI voice. The headline has the density of type locked onto a deck cover: not newspaper ink, not app chrome, but a title slide compressed until it feels ready to present.

The system avoids harsh chrome. Cards and browser mockups use soft shadows such as `0 8px 26px rgba(103,110,144,.2)` and `0 20px 90px rgba(10,3,89,.3)`, while nav and hero remain clean. Shadows support product imagery; they do not turn the layout into a dashboard. It is closer to a lit screen floating in a darkened meeting room: the frame recedes, the deck becomes the object, and the purple stage carries the drama.

Pitch's craft is mostly subtraction around one confident gesture. Buttons stay squared at `6px`, not pill-shaped; the nav can wear the same gradient as the hero without becoming a separate banner; uppercase tabs whisper process without turning into enterprise chrome. The site keeps saying "presentation" with layout behavior instead of explaining it in copy.

### Key Characteristics

- Purple gradient stage: `#8D49F7` to `#6B53FF` carries brand recognition.
- White hero typography: massive `Mark Pro`, weight `800`, tight tracking `-.02em`.
- Dual font system: `Mark Pro` for headline confidence, `Eina01` for navigation and body control.
- Centered SaaS hero: headline, supporting copy, two CTAs, then product/browser preview.
- Fixed navigation: `4.5rem` desktop nav with gradient or white states.
- Rounded but not bubbly controls: button and nav radii cluster around `6px`, not 999px.
- Product-story tabs: uppercase labels with `.1em` tracking and white active underline.
- Soft dimensional product mockups: shadow is applied to imagery and browser chrome, not every surface.
- Motion as presentation staging: slide-in, parallax, pulse, cursor, and gradient keyframes exist in CSS.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Gradient Confidence
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **violet presentation-stage hero with tight white display type**으로 기억된다.
> **Code Complexity**: high — hashed CSS modules, responsive tiers, multiple keyframes, and component-specific variables are present.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Pitch처럼 만들기 - 3가지만 하면 80%

```css
/* 1. Font split */
body {
  font-family: "Eina01", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}
h1, h2, .display {
  font-family: "Mark Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 800;
  letter-spacing: -0.02em;
}

/* 2. Purple presentation stage */
:root {
  --pitch-brand-purple: #8D49F7;
  --pitch-brand-blue-violet: #6B53FF;
  --pitch-text-ink: #2B2A35;
  --pitch-surface-white: #FFFFFF;
}
.hero {
  color: #FFFFFF;
  background: #8D49F7 linear-gradient(95.14deg, #8D49F7, #6B53FF 103.53%);
}

/* 3. Button geometry */
.button {
  border-radius: 6px;
  padding: 0 1.5em;
  min-height: 3rem;
  font-weight: 700;
}
```

**절대 하지 말아야 할 것 하나**: hero를 white SaaS section으로 만들지 말 것. Pitch의 첫인상은 보라색 발표 무대다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://pitch.com` |
| Fetched | Existing phase1 reuse; local files dated 2026-04-14, report generated 2026-05-03 |
| Extractor | Reused `insane-design/pitch/` phase1 JSON, CSS, HTML, and screenshot |
| HTML size | 4,063,722 bytes |
| CSS files | 3 external CSS files, 109,706 bytes total |
| Token prefix | `pitch` |
| Method | CSS custom property extraction + CSS frequency count + hero screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next-style production HTML with hashed CSS module class names.
- **Design system**: Pitch site-specific module system. Only a small variable layer is exposed; most values live inside component CSS.
- **CSS architecture**:
  ```text
  component modules      .style_navigation__831Nr / .style_hero__ZOWhV / .style_tabsContainer__aU7Ix
  local variables        --navigation-bar-height / --rest-color / --active-color-1
  direct values          #8d49f7 / #6b53ff / #2b2a35 / font and shadow declarations
  ```
- **Class naming**: CSS Modules with `style_name__hash` pattern.
- **Default theme**: Mixed. Hero and some nav states are purple/negative; content and nav scrolled states use white surfaces.
- **Font loading**: CSS references custom brand fonts `Mark Pro`, `Eina01`, and isolated `Lato-*` faces.
- **Canonical anchor**: Homepage hero and navigation are the strongest anchor; deeper product surfaces may use different densities.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Mark Pro` (commercial brand font; observed in headline CSS)
- **Body / nav font**: `Eina01` (commercial brand font; observed in navigation and body modules)
- **Fallback chain**: `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `roboto`, `helvetica`, `arial`, `sans-serif`
- **Weight normal / bold**: `400` / `800`

```css
:root {
  --pitch-font-display: "Mark Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --pitch-font-body: "Eina01", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --pitch-font-weight-normal: 400;
  --pitch-font-weight-strong: 700;
  --pitch-font-weight-display: 800;
}
body {
  font-family: var(--pitch-font-body);
  font-weight: var(--pitch-font-weight-normal);
}
.display {
  font-family: var(--pitch-font-display);
  font-weight: var(--pitch-font-weight-display);
  letter-spacing: -0.02em;
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Mark Pro substitute**: use `Inter Tight` or `Satoshi` at weight `800`. Keep `letter-spacing: -0.02em`; without tight tracking the headline loses its compact presentation-cover feel.
- **Eina01 substitute**: use `Inter` or `DM Sans` at weight `400` for navigation/body and `700` for buttons. Do not reuse the display face for all UI copy.
- **Metric correction**: if using Inter, reduce hero line-height toward `1.05-1.1` and keep body around `1.6`. Pitch separates display compression from body readability.
- **Avoid**: `font-weight: 500` as the default middle state. The observed system leans on `400`, `700`, and `800`.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| Hero display | visual 80px+ desktop | 800 | tight / about 1.05-1.1 | `-.02em` |
| `.style_heading1___7AKw` | `2.625rem` | 800 | `1.2` | `-.02em` |
| Section title | `1.75rem` to `3.75rem` | 700-800 | `1.1-1.3` | `-.02em` sometimes |
| Body large | `1.125rem` | 400 | `1.6` | `0` |
| Nav link | `1rem` | 400 | inherited | `0` |
| Caps label / tab | `.8125rem` | 700 | `1.4` | `.1em` |
| Small UI | `12px-14px` | 600-700 | `1.4-1.5` | `0` |

> Key insight: Pitch is not a single-font SaaS system. Display compression and body clarity are split between `Mark Pro` and `Eina01`.

### Principles
<!-- SOURCE: manual -->

1. Display copy is heavy and tight: weight `800` plus `-.02em` tracking is a brand behavior, not a decorative tweak.
2. Navigation stays untracked at `1rem`; it should feel usable, not campaign-like.
3. Uppercase process labels and tabs earn their spacing with `.1em` tracking.
4. Body line-height is allowed to breathe around `1.6`, balancing the compressed hero.
5. Weight `500` is effectively absent in the sampled CSS; avoid building a middle-weight interface.
6. `Mark Pro` owns the pitch, `Eina01` owns the product explanation.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed key values)

| Token | Hex |
|---|---|
| `pitch-brand-purple` | `#8D49F7` |
| `pitch-brand-blue-violet` | `#6B53FF` |
| `pitch-brand-deep-purple` | `#5318EB` |
| `pitch-brand-light-purple` | `#AB6EF9` |
| `pitch-accent-electric` | `#1243FD` |
| `pitch-accent-magenta` | `#DF05DA` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `pitch-deep-stage` | `#030B1D` |
| `pitch-dark-ink` | `#1E1D28` |
| `pitch-shadow-ink` | `#2B2A35` |

### 06-3. Neutral Ramp

| Step | Light | Dark / Ink |
|---|---|---|
| 0 | `#FFFFFF` | `#000000` |
| 50 | `#F8F8FB` | `#2B2A35` |
| 100 | `#F6F6F9` | `#3F4250` |
| 200 | `#F0EFF4` | `#545465` |
| 300 | `#DDDFE5` | `#6F7387` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Violet | primary gradient start | `#8D49F7` |
| Blue-violet | primary gradient end | `#6B53FF` |
| Electric blue | illustration / product accent | `#1243FD` |
| Magenta | illustration / gradient accent | `#DF05DA` |
| Yellow | avatar / illustrative accent | `#FFD02C` |
| Orange | illustrative accent | `#FF9E2C` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `surface-white` | `#FFFFFF` | CTA fill, nav scrolled state, product surfaces |
| `text-ink` | `#2B2A35` | dark text and navigation on white |
| `brand-purple` | `#8D49F7` | gradient start, active link state |
| `brand-blue-violet` | `#6B53FF` | gradient end, signup text |
| `border-soft` | `#DDDFE5` | soft hairlines / UI separation |
| `surface-mist` | `#F8F8FB` | light product chrome and cards |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--rest-color` | `#2B2A35` or `hsla(0,0%,100%,.8)` | nav link default by surface |
| `--active-color-1` | `#8D49F7` or `#FFFFFF` | link gradient / negative nav active |
| `--active-color-2` | `#6B53FF` or `#FFFFFF` | link gradient / negative nav active |
| `--navigation-bar-height` | `4.5rem` desktop, `3.75rem` mobile-adjacent | nav sizing |
| `--mobile-transition-duration` | `.15s` / `.3s` | mobile menu and nav animation |

### 06-7. Dominant Colors (CSS frequency count)

| Token | Hex | Frequency / role |
|---|---|---|
| `surface-white` | `#FFFFFF` | highest, CTA and white surfaces |
| `brand-blue-violet` | `#6B53FF` | high, primary gradient end |
| `brand-purple` | `#8D49F7` | high, primary gradient start |
| `black` | `#000000` | rgba/shadow and utility contexts |
| `text-ink` | `#2B2A35` | nav/text/shadow ink |
| `border-soft` | `#DDDFE5` | soft structural borders |

### 06-8. Color Stories
<!-- SOURCE: manual - top 4 colors only -->

**`{colors.brand-purple}` (`#8D49F7`)** — The stage color. It is used as the start of the hero/nav gradient and as one active link color. Treat it as atmosphere first, not merely a button accent.

**`{colors.brand-blue-violet}` (`#6B53FF`)** — The gradient's forward motion. It pushes the hero from static purple into a presentation-light effect and doubles as the CTA text color on white buttons.

**`{colors.surface-white}` (`#FFFFFF`)** — The contrast plane. White appears as CTA fill, logo/nav negative content, and clean product surfaces. It should cut through the purple, not replace it.

**`{colors.text-ink}` (`#2B2A35`)** — The sober product voice. It appears on white navigation and body contexts, preventing the brand from becoming all-purple decoration.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `navigation-bar-height` | `4.5rem` | desktop nav height |
| `navigation-bar-height-mobile` | `3.75rem` | compact nav height |
| `announcement-bar-height` | `2.5rem` / `4.5rem` | announcement + nav calculation |
| `links-gap` | `.75rem` | nav link group rhythm |
| `gap-tight` | `.25rem` | icon / micro UI pairing |
| `gap-ui` | `.9375rem` / `1rem` | button and nav internals |
| `gap-card` | `1.5rem` | card and section group spacing |
| `gap-section` | `2.5rem` | large content grouping |
| `body-side-margin` | `.9375rem` to `1.875rem` | responsive body gutters |
| `container-wide` | `86.25rem` | broad marketing/product layout |

**주요 alias**:
- `--links-gap` -> `.75rem` (first-level navigation spacing)
- `--bodySideMargins` -> `-.5rem` / `-.9375rem` / `-1.875rem` (responsive offset behavior)

### Whitespace Philosophy
<!-- SOURCE: manual -->

Pitch uses generous hero air but compact product storytelling. The first viewport gives the headline a wide center stage, then pulls a product/browser preview up from below so the page does not feel like a static billboard. The white space is presentation timing: title, subtitle, CTA, visual proof.

Below the hero, spacing compresses into tabs, cards, and process blocks. The contrast is intentional. Pitch sells polished decks, so the marketing page alternates between theatrical cover-slide space and dense "how it works" product evidence.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `radius-button` | `6px` | primary/secondary CTA buttons |
| `radius-small` | `8px` | small UI surfaces |
| `radius-card` | `12px` | product cards, smaller containers |
| `radius-large-card` | `24px` | larger media/product modules |
| `radius-pill-like` | `1.25rem` / `1.625rem` | selected rounded modules |
| `radius-circle` | `50%` | avatars, circular visuals |

Pitch is rounded but controlled. The common mistake is to make everything pill-shaped; observed button geometry is closer to `6px` than `999px`.

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| Product soft | `0 8px 26px rgba(103,110,144,.2)` | product surfaces / cards |
| Dark mockup | `0 6px 27px rgba(43,42,53,.5)` | browser-like dark surfaces |
| Hero depth | `0 20px 90px rgba(10,3,89,.3), 0 0 0 1px rgba(0,0,0,.02)` | large media/mockup depth |
| Light card | `0 2px 15px rgba(103,110,144,.2), 0 0 0 1px rgba(103,110,144,.05)` | subtle card lift |
| Purple glow | `0 8px 26px 0 rgba(114,30,205,.3)` | violet accent surface |

Shadow is scoped. Use it for product evidence and floating media; do not add elevation to every marketing block.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / keyframe | Value | Usage |
|---|---|---|
| `--mobile-transition-duration` | `.15s` / `.3s` | mobile nav/menu transitions |
| link gradient movement | `background-position .4s ease` | nav/link hover effect |
| shadow response | `box-shadow .12s ease-in-out` | subtle component feedback |
| `style_title-slide-in__C7mxd` | keyframe | staged headline entrance |
| `style_parallax__W5YVq` | keyframe | hero/product movement |
| `style_pulse__SA_Tq` | keyframe | attention cue |
| `style_gradient1__zln49` to `style_gradient4__NRvXt` | keyframes | animated gradient/illustration system |
| cursor keyframes | `cursor_talking__IiQ96`, `style_cursor-*` | collaborative product storytelling |

Motion should feel like presentation staging: reveal, cursor, pulse, gradient shimmer. Avoid heavy page-wide transforms that feel like a generic interactive agency site.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `86.25rem` for wide marketing/product layouts; `50rem` and `35rem` for narrower copy blocks.
- **Grid type**: responsive marketing grid with CSS module-specific layout rules.
- **Column count**: variable; hero is centered single-column, later product areas split into tabs/cards.
- **Gutter**: common gaps at `1rem`, `1.5rem`, and `2.5rem`.

### Hero

- **Pattern Summary**: full-bleed violet gradient stage + centered white H1 + dual CTA + product preview rising from bottom.
- Layout: centered title stack with navigation above and product/browser screenshot below.
- Background: `#8D49F7` to `#6B53FF` gradient with soft 3D ribbon/orb-like product art at corners.
- **Background Treatment**: gradient-stage plus soft 3D abstract shapes; not a flat color block.
- H1: large `Mark Pro`, weight `800`, tracking `-.02em`, white.
- Max-width: visual copy width around `50rem`; full hero background spans viewport.

### Section Rhythm

```css
section {
  padding: 5rem 1.875rem;
  max-width: 86.25rem;
}
```

### Card Patterns

- **Card background**: mostly `#FFFFFF` or `#F8F8FB`.
- **Card border**: soft `#DDDFE5` / `rgba(103,110,144,.05)` style hairlines.
- **Card radius**: `12px` or `24px`, depending on media scale.
- **Card padding**: `1rem` to `2.5rem`.
- **Card shadow**: soft blue-gray shadows, not hard black elevation.

### Navigation Structure

- **Type**: fixed top marketing nav with dropdown menu groups.
- **Position**: `fixed`; top offset can account for announcement bar.
- **Height**: `4.5rem` desktop, `3.75rem` compact state.
- **Background**: white on general/scrolled states, gradient purple on homepage/negative states.
- **Border**: minimal; structure comes from background and shadow state.

### Content Width

- **Prose max-width**: `35rem` to `50rem`.
- **Container max-width**: `86.25rem`.
- **Sidebar width**: not a homepage-defining pattern.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | inferred under `40em` | nav height and body margins compress |
| Tablet | `60em`-adjacent media rules observed | menus/cards adjust |
| Desktop | default desktop modules | full nav and large hero stage |
| Large | wide containers around `86.25rem` | product sections breathe |

### Touch Targets

- **Minimum tap size**: CTA buttons should stay near `3rem` height.
- **Button height (mobile)**: preserve `3rem` target even if horizontal padding changes.
- **Input height (mobile)**: not directly evidenced on homepage.

### Collapsing Strategy

- **Navigation**: fixed nav with mobile transition variables; dropdown/menu behavior likely module-driven.
- **Grid columns**: marketing content collapses from multi-card/product blocks into stacked flows.
- **Sidebar**: not applicable to homepage.
- **Hero layout**: keep centered order; reduce display size before changing the visual hierarchy.

### Image Behavior

- **Strategy**: product/browser preview anchored under hero copy.
- **Max-width**: `100%` with explicit max-width containers.
- **Aspect ratio handling**: module-specific CSS includes `--aspect-ratio: 1/1` for avatar/visual modules.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

#### Primary CTA

| Property | Value |
|---|---|
| Background | `#FFFFFF` on purple hero |
| Text | `#6B53FF` or brand violet |
| Radius | `6px` |
| Padding | `0 1.5em` / `0 1.5rem` |
| Height | about `3rem` |
| Weight | `700` |
| Shadow | none in hero; rely on contrast |

```html
<a class="pitch-button pitch-button-primary">Sign up for free</a>
```

#### Secondary Outline CTA

| Property | Value |
|---|---|
| Background | transparent |
| Text | `#FFFFFF` |
| Border | `1px solid rgba(255,255,255,.65)` |
| Radius | `6px` |
| Weight | `700` |

```html
<a class="pitch-button pitch-button-secondary">Get a demo</a>
```

### Badges

Pitch uses announcement and tab-like labels more than classic badge chips.

| Property | Value |
|---|---|
| Font | `Eina01` |
| Size | `.8125rem` to `1rem` |
| Weight | `700` |
| Letter spacing | `.1em` for caps labels |
| Active color | `#FFFFFF` on purple |
| Rest color | `hsla(0,0%,100%,.8)` |

### Cards & Containers

| Property | Value |
|---|---|
| Background | `#FFFFFF`, `#F8F8FB`, or dark media surface |
| Radius | `12px` / `24px` |
| Border | `#DDDFE5` or low-alpha blue-gray hairline |
| Shadow | `0 8px 26px rgba(103,110,144,.2)` |
| Hover | subtle shadow/opacity, not strong transform |

### Navigation

```css
.pitch-nav {
  position: fixed;
  height: 4.5rem;
  padding: 0 .9375rem;
  font-family: "Eina01", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 1rem;
  letter-spacing: 0;
}
.pitch-nav.is-gradient {
  color: #FFFFFF;
  background: #8D49F7 linear-gradient(95.14deg, #8D49F7, #6B53FF 103.53%);
}
```

### Inputs & Forms

Homepage evidence is limited. Use the button geometry and soft border system as the safe base:

| Property | Value |
|---|---|
| Height | at least `3rem` |
| Border | `1px solid #DDDFE5` |
| Radius | `6px` to `8px` |
| Focus | violet outline or border using `#8D49F7` |
| Text | `#2B2A35` |

### Hero Section

```html
<section class="pitch-hero">
  <h1>Don't just present.<br>Pitch.</h1>
  <p>Pitch is the AI presentation platform...</p>
  <div class="pitch-hero-actions">
    <a class="pitch-button pitch-button-primary">Sign up for free</a>
    <a class="pitch-button pitch-button-secondary">Get a demo</a>
  </div>
  <div class="pitch-product-preview">...</div>
</section>
```

### 13-2. Named Variants

#### `button-hero-primary`

White filled CTA used on purple. It should feel like a crisp action cut into the gradient.

| State | Spec |
|---|---|
| default | `background: #FFFFFF; color: #6B53FF; border-radius: 6px; min-height: 3rem` |
| hover | subtle opacity/background shift; avoid shadow-heavy lift |
| focus | visible violet/white ring depending on surface |

#### `button-hero-secondary-outline`

Transparent demo CTA for pairing with primary.

| State | Spec |
|---|---|
| default | `background: transparent; color: #FFFFFF; border: 1px solid rgba(255,255,255,.65)` |
| hover | slightly stronger white border/fill tint |

#### `nav-link-gradient-active`

Text link with `--active-color-1` and `--active-color-2`.

| State | Spec |
|---|---|
| rest | `--rest-color: #2B2A35` or `hsla(0,0%,100%,.8)` |
| active | `#8D49F7` to `#6B53FF`, or white in negative nav |
| transition | `background-position .4s ease` |

#### `homepage-product-tab`

Uppercase tab labels under hero.

| State | Spec |
|---|---|
| rest | translucent white, uppercase, `.1em` tracking |
| active | `#FFFFFF` text with white underline |

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
violet-title-slide-stage:
  description: "Hero and negative navigation share one presentation-stage atmosphere."
  technique: "background: #8D49F7 linear-gradient(95.14deg, #8D49F7, #6B53FF 103.53%); color: #FFFFFF"
  applied_to: ["{component.nav-gradient}", "{component.hero-stage}"]
  visual_signature: "The page reads as a branded deck cover before the product screenshot appears."

tight-mark-pro-title-slide:
  description: "Display type is compressed like a finished presentation title."
  technique: "font-family: Mark Pro; font-weight: 800; letter-spacing: -.02em; line-height: ~1.05-1.1; color: #FFFFFF"
  applied_to: ["{component.hero-stage}", "{component.major-heading}"]
  visual_signature: "Large white headline feels locked to the slide canvas instead of floating as generic SaaS copy."

uppercase-workflow-tabs:
  description: "The product story is framed as deck workflow stages."
  technique: "text-transform: uppercase; font-size: .8125rem; font-weight: 700; letter-spacing: .1em; color: hsla(0,0%,100%,.8); active color: #FFFFFF"
  applied_to: ["{component.tab-caps}", "{component.homepage-product-tab}"]
  visual_signature: "Design / Collaborate / Pitch / Analyze reads like section tabs in a live presentation."

bluegray-product-lift:
  description: "Product evidence floats softly while the hero and nav stay clean."
  technique: "box-shadow: 0 8px 26px rgba(103,110,144,.2); large mockup: 0 20px 90px rgba(10,3,89,.3), 0 0 0 1px rgba(0,0,0,.02)"
  applied_to: ["{component.product-preview}", "{component.card-container}"]
  visual_signature: "The mockup feels like a lit projected screen, not a heavy dashboard card."

six-pixel-cta-geometry:
  description: "Buttons stay crisp and presentation-tool-like rather than bubbly."
  technique: "border-radius: 6px; min-height: 3rem; padding: 0 1.5em; font-weight: 700; primary bg #FFFFFF with violet text"
  applied_to: ["{component.button-primary}", "{component.button-secondary-outline}"]
  visual_signature: "CTAs look cut into the violet stage with controlled corners, not pill-shaped consumer app controls."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | short imperative or contrastive phrase, often deck-aware | "Don't just present. Pitch." |
| Primary CTA | direct signup action | "Sign up for free" |
| Secondary CTA | sales/support action | "Get a demo" |
| Subheading | plain product benefit, AI/collaboration/results language | "AI presentation platform..." |
| Tone | confident, polished, team/productivity oriented | "fast-moving teams", "on-brand", "winning slide decks" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Pitch - copy into your root stylesheet */
:root {
  /* Fonts */
  --pitch-font-display: "Mark Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --pitch-font-body: "Eina01", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --pitch-font-weight-normal: 400;
  --pitch-font-weight-strong: 700;
  --pitch-font-weight-display: 800;

  /* Brand */
  --pitch-color-brand-purple: #8D49F7;
  --pitch-color-brand-blue-violet: #6B53FF;
  --pitch-color-brand-deep: #5318EB;
  --pitch-color-brand-light: #AB6EF9;

  /* Surfaces */
  --pitch-bg-page: #FFFFFF;
  --pitch-bg-mist: #F8F8FB;
  --pitch-bg-stage: #8D49F7;
  --pitch-text: #2B2A35;
  --pitch-text-on-stage: #FFFFFF;
  --pitch-border-soft: #DDDFE5;

  /* Spacing */
  --pitch-space-xs: .25rem;
  --pitch-space-sm: .75rem;
  --pitch-space-md: 1rem;
  --pitch-space-lg: 1.5rem;
  --pitch-space-xl: 2.5rem;

  /* Radius */
  --pitch-radius-button: 6px;
  --pitch-radius-card: 12px;
  --pitch-radius-media: 24px;

  /* Shadow */
  --pitch-shadow-soft: 0 8px 26px rgba(103,110,144,.2);
  --pitch-shadow-hero: 0 20px 90px rgba(10,3,89,.3), 0 0 0 1px rgba(0,0,0,.02);
}

.pitch-hero {
  color: var(--pitch-text-on-stage);
  text-align: center;
  background: var(--pitch-color-brand-purple)
    linear-gradient(95.14deg, var(--pitch-color-brand-purple), var(--pitch-color-brand-blue-violet) 103.53%);
}

.pitch-hero h1 {
  font-family: var(--pitch-font-display);
  font-weight: var(--pitch-font-weight-display);
  letter-spacing: -0.02em;
  line-height: 1.05;
}

.pitch-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 3rem;
  padding: 0 1.5em;
  border-radius: var(--pitch-radius-button);
  font-family: var(--pitch-font-body);
  font-weight: var(--pitch-font-weight-strong);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js - Pitch-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        pitch: {
          purple: '#8D49F7',
          violet: '#6B53FF',
          deep: '#5318EB',
          ink: '#2B2A35',
          mist: '#F8F8FB',
          border: '#DDDFE5',
        },
      },
      fontFamily: {
        display: ['Mark Pro', 'Inter Tight', 'system-ui', 'sans-serif'],
        sans: ['Eina01', 'Inter', 'system-ui', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        strong: '700',
        display: '800',
      },
      borderRadius: {
        pitchButton: '6px',
        pitchCard: '12px',
        pitchMedia: '24px',
      },
      boxShadow: {
        pitchSoft: '0 8px 26px rgba(103,110,144,.2)',
        pitchHero: '0 20px 90px rgba(10,3,89,.3), 0 0 0 1px rgba(0,0,0,.02)',
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
| Brand primary | `pitch-brand-purple` | `#8D49F7` |
| Brand gradient end | `pitch-brand-blue-violet` | `#6B53FF` |
| Background | `pitch-surface-white` | `#FFFFFF` |
| Text primary | `pitch-text-ink` | `#2B2A35` |
| Border | `pitch-border-soft` | `#DDDFE5` |
| Light surface | `pitch-surface-mist` | `#F8F8FB` |
| Deep stage | `pitch-deep-stage` | `#030B1D` |

### Example Component Prompts

#### Hero Section

```text
Pitch 스타일 히어로 섹션을 만들어줘.
- 배경: #8D49F7에서 #6B53FF로 이어지는 95.14deg 보라 gradient
- H1: Mark Pro, weight 800, letter-spacing -0.02em, white, center aligned
- 서브텍스트: white with softer opacity, body font Eina01, readable line-height
- CTA: primary는 white fill + #6B53FF text + 6px radius, secondary는 transparent outline white
- 아래쪽에는 product/browser preview가 살짝 걸쳐 보이게 배치
```

#### Card Component

```text
Pitch 스타일 product card를 만들어줘.
- 배경: #FFFFFF 또는 #F8F8FB
- border: 1px solid #DDDFE5 또는 rgba(103,110,144,.05)
- radius: 12px 또는 media-heavy card는 24px
- shadow: 0 8px 26px rgba(103,110,144,.2)
- 제목은 Mark Pro 700/800, 본문은 Eina01 400
```

#### Navigation

```text
Pitch 스타일 상단 네비게이션을 만들어줘.
- fixed top, height 4.5rem, font Eina01 1rem
- hero 위에서는 #8D49F7 -> #6B53FF gradient 배경과 white text
- white state에서는 #FFFFFF background, #2B2A35 text
- active link는 #8D49F7/#6B53FF gradient text 느낌
- 우측 버튼은 Log in outline, Sign up white fill
```

### Iteration Guide

- **Hero를 만들 때**: 보라 gradient stage를 먼저 고정하고, 나머지 요소를 그 위에 올린다.
- **색상 변경 시**: `#8D49F7`와 `#6B53FF`의 관계를 유지한다. 하나만 남기면 Pitch의 움직임이 사라진다.
- **폰트 변경 시**: display/body를 반드시 분리한다.
- **여백 조정 시**: hero는 여유롭게, process/product blocks는 더 촘촘하게 만든다.
- **카드 추가 시**: border보다 soft shadow와 pale surface를 우선한다.
- **모션 추가 시**: reveal, cursor, pulse처럼 발표 진행감을 주는 움직임만 쓴다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#8D49F7` -> `#6B53FF` as a dominant stage gradient for the first impression.
- Set hero/display headlines in `Mark Pro` or a tight substitute at weight `800`.
- Keep display `letter-spacing: -0.02em` for major titles.
- Use `Eina01` or a clean substitute for navigation/body/product explanation.
- Use white CTAs on purple hero with controlled `6px` radius.
- Let product previews carry soft shadows; keep navigation and content chrome clean.
- Preserve uppercase tab labels with `.1em` tracking in workflow/story sections.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white` hero로 두지 말 것 — 대신 hero는 `#8D49F7` -> `#6B53FF` gradient 사용.
- 브랜드 컬러를 `#7C3AED` 같은 generic purple로 대체하지 말 것 — 대신 `#8D49F7`와 `#6B53FF`를 유지.
- 본문 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#2B2A35` 사용.
- soft border를 `#E5E7EB`로 일반화하지 말 것 — 대신 `#DDDFE5` 또는 low-alpha blue-gray 사용.
- hero CTA 배경을 `#6B53FF`로 채우지 말 것 — purple stage 위 primary CTA는 `#FFFFFF` fill이 핵심.
- 버튼을 `999px` pill로 만들지 말 것 — Pitch button 기본은 `6px` radius에 가깝다.
- display headline에 `font-weight: 500` 사용 금지 — Pitch display는 `800`이 핵심이다.
- headline tracking을 `0`으로 두지 말 것 — display에는 `letter-spacing: -0.02em` 적용.
- 모든 카드에 `box-shadow: 0 10px 30px rgba(0,0,0,.2)` 같은 검은 그림자 사용 금지 — 대신 `rgba(103,110,144,.2)` 계열 사용.
- nav 링크를 body와 같은 plain hover color로 처리하지 말 것 — `--active-color-1: #8D49F7`, `--active-color-2: #6B53FF` active behavior를 살린다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No neutral-first hero**: the homepage does not begin with a white SaaS hero; purple owns the first viewport.
- **No single flat brand purple**: the identity is a two-color gradient relationship, not one swatch.
- **No default Inter-only voice**: the design depends on `Mark Pro` plus `Eina01` role separation.
- **No weight-500 middle tone**: observed weights jump from 400 into 600/700/800; the mushy middle is absent.
- **No oversized pill buttons**: controls are rounded, but not capsule-first.
- **No heavy black elevation on chrome**: shadows are blue-gray, soft, and scoped to product/media surfaces.
- **No dense dashboard layout in the hero**: product proof appears after the emotional title-slide moment.
- **No serif editorial mood**: Pitch is polished and campaign-like, but not magazine typography.
- **No brutalist borders**: hairlines stay soft; structure comes from gradient, spacing, and product mockup depth.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage-oriented capture**: this guide reuses existing `pitch` phase1 artifacts and the homepage hero screenshot. Logged-in editor UI and workspace surfaces were not visited.
- **Phase1 date mismatch**: source files appear to be from 2026-04-14 while this guide was generated on 2026-05-03. Pitch may have changed since the local capture.
- **Typography scale is partial**: `phase1/typography.json` did not expose a full tokenized scale, so the ladder combines observed CSS declarations with screenshot interpretation.
- **Token layer is shallow**: only 25 custom properties were extracted and most are component-local. The named frontmatter tokens are guidebook aliases based on real CSS values, not evidence of a public Pitch token API.
- **Motion behavior not visually replayed**: CSS keyframes were identified, but scroll-trigger timing and JavaScript interaction sequencing were not re-executed.
- **Mobile states not screenshot-verified**: CSS contains many media queries, but this guide did not capture separate mobile screenshots.
- **Form/error/loading states are under-evidenced**: homepage artifacts show CTA and navigation patterns better than form validation or app workflow states.
- **Illustration accent colors may include marketing art**: colors such as `#DF05DA`, `#1243FD`, `#FFD02C`, and `#FF9E2C` appear in CSS but should be treated as illustration accents, not core UI colors.
