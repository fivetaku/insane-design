---
schema_version: 3.2
slug: twitch
service_name: Twitch
site_url: https://www.twitch.tv
fetched_at: 2026-04-20T19:58:00+09:00
default_theme: mixed
brand_color: "#9147FF"
primary_font: Inter
font_weight_normal: 400
token_prefix: tw

bold_direction: Stream Chrome
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: other
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Runtime CSS exposes consistent Twitch navigation, shell, side-nav, card, social, and theme-state patterns, but almost no exported custom-property token tier."

colors:
  primary: "#9147FF"
  primary-hover: "#772CE8"
  primary-active: "#5C16C5"
  primary-dark-ui: "#A970FF"
  primary-dark-active: "#BF94FF"
  surface-light: "#FFFFFF"
  surface-rail-light: "#EFEFF1"
  surface-dark: "#18181B"
  surface-rail-dark: "#26262C"
  text-light: "#0E0E10"
  text-dark: "#EFEFF1"
  live-red: "#E91916"
  live-red-hover: "#BB1411"
  promo-pink: "#FF75E6"
typography:
  display: "Roobert"
  body: "Inter"
  ladder:
    - { token: body, size: "1.6rem", weight: 400, tracking: "0" }
    - { token: nav, size: "1.4rem-1.6rem inferred", weight: 600, tracking: "0" }
    - { token: shell, size: "1.2rem-1.8rem observed", weight: 400, tracking: "0" }
  weights_used: [400, 500, 600, 700]
  weights_absent: [300, 800, 900]
components:
  nav-logo-link: { color: "{colors.primary-active}", hover: "{colors.primary-hover}" }
  nav-link-active: { color: "{colors.primary-active}", indicator: "0.2rem" }
  shell-signup-button: { radius: "2px", height: "3rem", width: "6.1rem" }
  side-nav-expanded: { width: "24rem", bg: "{colors.surface-rail-light}" }
  side-nav-collapsed: { width: "5rem" }
  video-card-focus-ring: { border: "2px solid {colors.primary}", radius: "var(--border-radius-small)" }
---

# DESIGN.md — Twitch

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Twitch is a live broadcast **arena** where the content is allowed to be loud, but the chrome stays brutally functional. The first impression is a white application shell with a violet command language: `#9147FF` (`{colors.primary}`) owns logo marks, active states, share surfaces, and community calls to action, while the page body keeps enough neutral restraint for streams, avatars, thumbnails, and viewer counts to compete without the product frame collapsing.

The site's strongest move is the contrast between broadcast chaos and rigid UI rails. The left side rail is a **dashboard** operational queue, not decorative chrome. It sits at 24rem when expanded, collapses to 5rem, and uses `#EFEFF1` (`{colors.surface-rail-light}`) or `#26262C` (`{colors.surface-rail-dark}`) to separate live-channel inventory from the content **canvas**. The top shell is exactly 5rem high, search is capped around 40rem, and sign-up/login controls are compact 3rem rectangles. This is interface as **console**, not interface as poster. The multi-bank monitor wall of a broadcast control **studio** is the closest physical reference: each row on the left rail is a feed waiting for the director's cue, the "LIVE" badge is the red tally light on a studio camera, and the chat column behaves like the talkback intercom that never closes.

Twitch violet has two personalities. In light UI it steps down from `#9147FF` to `#772CE8` and `#5C16C5` for hover, logo, active nav, and underlines. In dark UI it lifts to `#A970FF` and `#BF94FF`. That theme-aware violet swap — the single **accent** allowed on the **stage** — is more important than the global brand swatch; use one purple everywhere and the site immediately feels like a fan clone instead of Twitch. The content cards are intentionally image-first and low-chrome: stream thumbnails carry color, badges mark state, hover/focus uses purple borders rather than heavy shadows. The purple is the only **stage** color allowed because the show itself is supposed to be the chroma.

### Key Characteristics

- Light application shell with theme-aware dark equivalents, not a single-theme landing page.
- Twitch violet #9147FF is canonical, with #772CE8 / #5C16C5 for light-state interaction and #A970FF / #BF94FF for dark-state interaction.
- Navigation is dense and operational: 5rem top shell, 24rem side rail, 5rem collapsed rail.
- Video thumbnails dominate; chrome is mostly border, badge, compact text, and small action buttons.
- Radius is small: 2px, 3px, 5px, `var(--border-radius-small)`, plus circular avatars/icons only.
- Motion is quick and physical: social buttons lift `translate3d(0,-.3rem,0)`; nav indicators transform in `.2s`.
- Live state is red #E91916, not brand purple.
- Typography is mostly Inter for UI, with Roobert reserved for display/nav brand expression.
- Search is a centered utility lane with about 40rem maximum width.
- The system uses color for state and identity, not for decorative gradients across the whole page.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Stream Chrome
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **live broadcast grid inside compact violet control chrome**으로 기억된다.
> **Code Complexity**: high — theme-aware color states, dense nav rails, stream-card states, social hover physics, and runtime-loaded application HTML require more than static marketing CSS.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Twitch처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
  font-size: 1.6rem;
}

/* 2. 앱 쉘 */
:root {
  --tw-bg: #FFFFFF;
  --tw-rail: #EFEFF1;
  --tw-text: #0E0E10;
  --tw-brand: #9147FF;
}
.top-shell { height: 5rem; background: var(--tw-bg); color: var(--tw-text); }
.side-rail { width: 24rem; background: var(--tw-rail); }

/* 3. 상태 컬러 */
.is-active { color: #5C16C5; }
.is-live { background: #E91916; color: #FFFFFF; }
```

**절대 하지 말아야 할 것 하나**: Twitch purple을 단일 #9147FF로만 쓰지 말 것. Light hover/active는 #772CE8 / #5C16C5, dark active는 #A970FF / #BF94FF로 갈라야 실제 Twitch chrome에 가까워진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.twitch.tv` |
| Fetched | 2026-04-20T19:58:00+09:00 |
| Extractor | existing phase1 reuse: HTML + CSS + screenshot |
| HTML size | 188434 bytes (runtime app shell with 73 script tags) |
| CSS files | 2 files, 70957 chars |
| Token prefix | `tw` (analysis alias; CSS custom-token tier mostly absent) |
| Method | Existing `insane-design/twitch` phase1 JSON, CSS, HTML, and screenshot reused; no fresh crawl |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Runtime-loaded Twitch web app shell. HTML snapshot exposes a minimal app container, 73 scripts, one stylesheet, and a loader/navigation shell rather than a fully semantic SSR document.
- **Design system**: Twitch internal UI patterns in compiled CSS. The extraction found only one custom property in `resolved_tokens.json`, so this is a system-in-use rather than a clean public token export.
- **CSS architecture**: compiled component classes plus theme scope classes.
  ```text
  shell-*                 app shell, search, auth, logo
  top-nav__*              top navigation and logo states
  navigation-link*        active/hover nav link treatment
  side-nav*               live-channel rail, collapsed/expanded states
  offline-* / social-*    video embed, cards, social controls
  tw-root--theme-dark     dark theme overrides
  tw-root--theme-light    light theme overrides
  ```
- **Class naming**: BEM-like component naming with state modifiers, for example `.shell-nav__user-auth-button--login`, `.side-nav--collapsed`, `.social-button--large`.
- **Default theme**: mixed. The captured screenshot is light UI with purple banner, but CSS includes explicit dark shell and `tw-root--theme-dark` overrides.
- **Font loading**: CSS declarations show Inter as dominant UI font and Roobert as display/brand/navigation font.
- **Canonical anchor**: top navigation + side rail + stream thumbnail grid. Twitch is recognized by application chrome before any one marketing hero.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Roobert` (brand/display use in CSS declarations)
- **Body font**: `Inter` (dominant UI font; 21 declarations in extracted typography)
- **Code font**: `monospace` observed once; no branded code face found
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --tw-font-family:       "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --tw-font-family-display: "Roobert", "Inter", sans-serif;
  --tw-font-family-code:  ui-monospace, SFMono-Regular, Menlo, monospace;
  --tw-font-weight-normal: 400;
  --tw-font-weight-medium: 500;
  --tw-font-weight-semibold: 600;
  --tw-font-weight-bold: 700;
}
body {
  font-family: var(--tw-font-family);
  font-weight: var(--tw-font-weight-normal);
}
```

### Note on Font Substitutes

- **Roobert** — Treat as the brand/display layer. If unavailable, use **Inter Display** or **Inter** at weight 700, but tighten the hierarchy through size and contrast rather than inventing a condensed display face.
- **Inter** — Keep it as the body substitute; the CSS already uses it heavily. Do not replace with Roboto or Arial unless the goal is a deliberately non-Twitch generic web app.
- **Metric correction** — If Roobert is missing, keep nav labels at weight 600 and avoid negative tracking. Twitch's compactness comes from rail geometry and color state, not editorial letter-spacing.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `body` | `1.6rem` observed | 400 | normal / component-controlled | 0 |
| `shell-small` | `1.2rem` observed | 400-600 | compact | 0 |
| `nav-link` | inferred 14-16px from shell density | 600 active/brand | compact | 0 |
| `card-title` | component-controlled, around 14-16px in captured UI | 600-700 | tight | 0 |
| `live-badge` | compact chip text | 700 | tight | 0 |
| `display/brand` | Roobert declarations | 700 | tight | 0 |

> ⚠️ The extractor found no clean scale object. Typography is inferred from CSS declarations plus screenshot density; exact heading ladder was not present in phase1 JSON.

### Principles

1. UI legibility beats editorial drama. The page is a live catalog, so 400/600/700 weights matter more than huge display sizes.
2. Weight 500 exists but is minor. The recognizable Twitch rhythm is mostly 400 body, 600 navigation/title, and 700 badges or emphasis.
3. Roobert is brand flavor, not the whole interface. Inter carries most repeatable product UI.
4. Letter spacing stays neutral. Do not add Apple-like negative tracking; Twitch feels compact through 5rem rails, badges, and thumbnail grids.
5. Live metadata should stay small and hard. Viewer counts, category labels, and language chips should not become large marketing copy.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (5 steps)
<!-- compiled CSS frequency + selector roles -->

| Token | Hex |
|---|---|
| `tw-purple-500` | `#9147FF` |
| `tw-purple-hover` | `#772CE8` |
| `tw-purple-active` | `#5C16C5` |
| `tw-purple-dark-hover` | `#A970FF` |
| `tw-purple-dark-active` | `#BF94FF` |

### 06-2. Brand Dark Variant
<!-- SOURCE: auto -->

| Token | Hex |
|---|---|
| `tw-purple-dark-interactive` | `#A970FF` |
| `tw-purple-dark-active` | `#BF94FF` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light | Dark |
|---|---|---|
| page | `#FFFFFF` | `#18181B` |
| text | `#0E0E10` | `#EFEFF1` |
| rail | `#EFEFF1` | `#26262C` |
| elevated / soft | `#F7F7F8` | `#19171C` |
| hairline / muted | `#D9D8DD` | `#26262C` |

### 06-4. Accent Families
<!-- SOURCE: auto -->

| Family | Key step | Hex |
|---|---|---|
| Live / alert | live badge and banner | `#E91916` |
| Live hover | red hover state | `#BB1411` |
| Promo gradient | side-nav promoted gradient | `#FF75E6` |
| Cyan promo | gradient / special accent | `#00A3A3` |
| Social Reddit | social share icon | `#FF4500` |
| Social Facebook | social share icon | `#3B5998` |

### 06-5. Semantic
<!-- SOURCE: auto+manual -->

| Token | Hex | Usage |
|---|---|---|
| `brand-primary` | `#9147FF` | logo fill, social copy/embed/download icons, primary identity |
| `brand-hover-light` | `#772CE8` | top-nav logo hover, external link hover |
| `brand-active-light` | `#5C16C5` | navigation active, logo light state |
| `brand-hover-dark` | `#A970FF` | hover in dark root |
| `brand-active-dark` | `#BF94FF` | active navigation in dark root |
| `surface-page-light` | `#FFFFFF` | shell nav, schedule panels |
| `surface-rail-light` | `#EFEFF1` | side rail, recommendation segment |
| `surface-page-dark` | `#18181B` | dark shell nav |
| `surface-rail-dark` | `#26262C` | dark side rail hover/background |
| `text-light` | `#0E0E10` | primary text in light UI |
| `text-dark` | `#EFEFF1` | primary text in dark UI |
| `live` | `#E91916` | live banner / beta badge style red |

### 06-6. Semantic Alias Layer
<!-- SOURCE: manual; extractor found no tiered aliases -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--tw-color-action` | `#9147FF` | primary identity and action |
| `--tw-color-action-hover` | `#772CE8` | light hover |
| `--tw-color-action-active` | `#5C16C5` | light active |
| `--tw-color-action-dark-hover` | `#A970FF` | dark hover |
| `--tw-color-action-dark-active` | `#BF94FF` | dark active |
| `--tw-color-live` | `#E91916` | live badge/banner |
| `--tw-bg-shell-light` | `#FFFFFF` | top shell |
| `--tw-bg-shell-dark` | `#18181B` | dark top shell |
| `--tw-bg-rail-light` | `#EFEFF1` | side rail |
| `--tw-bg-rail-dark` | `#26262C` | dark side rail |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---|---|
| neutral-white | `#FFFFFF` | 19 |
| brand-primary | `#9147FF` | 18 |
| neutral-black | `#000000` | 17 |
| text-light | `#0E0E10` | 15 |
| brand-hover | `#772CE8` | 13 |
| brand-active | `#5C16C5` | 11 |
| rail-light | `#EFEFF1` | 11 |
| brand-dark-hover | `#A970FF` | 8 |
| brand-dark-active | `#BF94FF` | 6 |

### 06-8. Color Stories

**`{colors.primary}` (#9147FF)** — Twitch purple is the identity anchor, but it works best as a state system rather than a flood fill. Use it for logo marks, share/action icons, primary CTAs, and selected borders.

**`{colors.surface-light}` (#FFFFFF)** — The captured shell is a white workspace, not a purple page. White gives stream thumbnails room to be noisy and keeps navigation/product controls legible.

**`{colors.text-light}` (#0E0E10)** — The light UI text is near-black but not pure black. It keeps the interface crisp without fighting with thumbnail contrast.

**`{colors.surface-rail-light}` (#EFEFF1)** — The side rail's pale gray is structural. It makes live channels feel like a persistent instrument panel rather than a card section.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `shell-height` | `5rem` | top navigation shell |
| `side-rail-expanded` | `24rem` | live channels rail |
| `side-rail-collapsed` | `5rem` | icon-only rail |
| `search-max-width` | `40rem` | centered top search |
| `search-height` | `3rem` | compact shell search |
| `auth-button-height` | `3rem` | login/sign-up buttons |
| `auth-button-margin` | `1rem` | spacing between auth actions |
| `side-card-sponsored-min` | `6.3rem` | sponsored side-nav card |
| `side-card-promoted-min` | `9.5rem` | promoted followed side-nav card |
| `video-card-border` | `1px / 2px` | thumbnail hover/focus border stack |

**주요 alias**:
- `--tw-shell-h` → `5rem` (global nav height)
- `--tw-rail-w` → `24rem` (expanded side rail)
- `--tw-rail-w-collapsed` → `5rem` (collapsed side rail)
- `--tw-search-w` → `40rem` (search tray maximum)

### Whitespace Philosophy

Twitch does not spend whitespace like a luxury brand. It allocates it like an operations console: enough to separate live inventory, search, account actions, and content streams, but never so much that the feed stops feeling active. The left rail is dense by design; avatars, streamer names, categories, red live dots, and viewer counts sit in a tight scan pattern.

The big breathing room belongs around the hero carousel and content rows, not inside each component. Cards need tight gutters because the product promise is abundance. When recreating the style, preserve the difference: open canvas around media, compressed metadata inside rails and cards.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| `radius-button` | `2px` | shell auth buttons, search |
| `radius-loader` | `3px` | shell skeleton shimmer |
| `radius-card-small` | `var(--border-radius-small)` | video card borders and focus rings |
| `radius-legacy` | `5px` | isolated compiled rule |
| `radius-avatar` | `50%` | avatars and circular icons |
| `radius-rounded` | `var(--border-radius-rounded)` | pill/circular system cases |

Twitch radius is small and pragmatic. Use hard rectangles for shell controls and thumbnails, then reserve full circles for avatars, icons, and live presence markers.

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `social-under-shadow` | `0 3px 10px -2px` | pseudo-element under social buttons |
| `hero-card-shadow` | visual shadow observed in screenshot | large carousel card floats above page |
| `chrome-shadow` | mostly absent | shell and rail rely on surface contrast/borders |

Twitch does not use multi-layer SaaS elevation as a primary language. The media card can float, but most controls use color, border, and density.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `social-lift` | `transform .1s ease-out, opacity .2s ease-out, width .2s ease-in` | social button hover |
| `social-hover-transform` | `translate3d(0,-.3rem,0)` | social button lift |
| `nav-indicator` | `transform .2s ease` | active navigation underline |
| `side-card-drop-in` | `height .25s` | side-nav drop-in card |
| `spinner` | `spin .5s linear infinite` | loading/settings spinner |

Motion is fast, short, and stateful. Avoid long parallax or scroll choreography; Twitch UI should feel instantly reactive.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: stream content uses broad fluid canvas; extracted snippets show `max-width: 120rem`, `80rem`, `40rem`, and thumbnail-specific widths rather than one universal container.
- **Grid type**: Flexbox-heavy compiled layout. CSS snippets show repeated `display:flex`, `flex-direction`, `flex-basis`, `flex-grow`.
- **Column count**: content rows are responsive thumbnail grids; side rail is fixed-width plus flexible main content.
- **Gutter**: tight card gutters in content rows; shell controls use 1rem increments.

### Hero
- **Pattern Summary**: `top banner + 5rem shell + 24rem side rail + centered stream carousel + content rows`
- Layout: app dashboard/content browser, not traditional centered landing hero.
- Background: #FFFFFF light page with #EFEFF1 left rail; purple alert/community bars appear as bands.
- **Background Treatment**: solid surfaces plus media thumbnails. No full-page gradient mesh.
- H1: no marketing H1 in captured shell; page title treatment appears as compact row headings like "Live on Twitch".
- Max-width: carousel media panel sits centered; search max-width is 40rem.

### Section Rhythm
```css
.shell-nav { height: 5rem; display: flex; }
.side-nav { width: 24rem; background-color: #EFEFF1; }
.side-nav--collapsed { width: 5rem; }
.top-nav__search-container { flex-basis: 40rem; }
```

### Card Patterns
- **Card background**: stream cards mostly image/media; metadata sits below on page background.
- **Card border**: default transparent, hover/focus purple border stack.
- **Card radius**: `var(--border-radius-small)` for video borders.
- **Card padding**: minimal around media; side-nav cards use `.3rem 1rem` in sponsored case.
- **Card shadow**: hero carousel has visible floating shadow; feed cards rely on image and hover border.

### Navigation Structure
- **Type**: horizontal top shell + vertical live-channel side rail.
- **Position**: shell nav compiled as absolute in the captured loader shell; top nav z-index reaches 1000.
- **Height**: 5rem.
- **Background**: #FFFFFF light, #18181B dark.
- **Border**: not dominant; state shown through color and active indicator.

### Content Width
- **Prose max-width**: N/A. Twitch is not prose-led.
- **Container max-width**: mixed; search 40rem, content snippets show 80rem/120rem anchors.
- **Sidebar width**: 24rem expanded, 5rem collapsed.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `max-width: 767px` | shell/search adjustments from inline CSS |
| Tablet | `max-width: 768px` | component responsive rules in compiled CSS |
| Nav switch | `max-width: 919px` / `min-width: 920px` | top/side navigation behavior split |
| Wide constraint | `width <= 55rem` | compact layout rule found in compiled CSS |
| Medium desktop | `max-width: 1023px` | shell layout reduction from inline CSS |

### Touch Targets
- **Minimum tap size**: not fully measured; shell nav blocks are 5rem high, auth buttons 3rem high.
- **Button height (mobile)**: 3rem shell auth buttons in captured CSS.
- **Input height (mobile)**: 3rem search shell.

### Collapsing Strategy
- **Navigation**: side rail can collapse from 24rem to 5rem; shell links hide/reflow at tablet/mobile breakpoints.
- **Grid columns**: media grid should reduce columns while preserving thumbnail-first hierarchy.
- **Sidebar**: collapsed icon rail is an explicit state.
- **Hero layout**: carousel/media area remains central; side content should compress before media loses prominence.

### Image Behavior
- **Strategy**: media thumbnails and embed backgrounds use `background-size: cover`, `background-position: 50%`, and `max-width: 100%`.
- **Max-width**: card images use width 100%; component snippets show 50%, 75%, 100%, 250px, 450px constraints.
- **Aspect ratio handling**: inferred from stream thumbnail cards; exact aspect-ratio token not extracted.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Shell auth button**

```html
<button class="shell-nav__user-auth-button shell-nav__user-auth-button--singup">Sign Up</button>
```

| Spec | Value |
|---|---|
| Height | `3rem` |
| Login width | `5.2rem` |
| Signup width | `6.1rem` |
| Padding | `.8rem` |
| Radius | `2px` |
| Layout | flex center |
| State | compact hover/focus should use Twitch violet, not large shadow |

### Badges

**Live badge**

```html
<span class="tw-live-badge">LIVE</span>
```

| Spec | Value |
|---|---|
| Background | `#E91916` |
| Text | `#FFFFFF` |
| Weight | 700 |
| Radius | small rectangle |
| Usage | stream thumbnails and live state only |

**Viewer count chip**

Use dark translucent overlays on thumbnails. Keep copy short: `357 viewers`, `31.5K viewers`. Do not replace with colorful pills.

### Cards & Containers

**Stream video card**

```html
<a class="offline-recommendations-video-card" href="#">
  <span class="offline-recommendations-video-card-border-2">
    <img class="offline-recommendations-video-card-img" alt="" />
  </span>
</a>
```

| Spec | Value |
|---|---|
| Default border | transparent |
| Hover/focus border | `2px solid #9147FF` on inner border layer |
| Inner border | `1px solid #451093` in deeper border layer |
| Radius | `var(--border-radius-small)` |
| Image | `width: 100%`, transform transition `.15s ease-out` |
| Shadow | minimal; media carries visual weight |

### Navigation

**Top shell**

```html
<nav class="shell-nav">
  <a class="shell-nav__logo">...</a>
  <div class="shell-nav__search"></div>
  <div class="shell-nav__user-auth"></div>
</nav>
```

| Spec | Value |
|---|---|
| Height | `5rem` |
| Background light | `#FFFFFF` |
| Background dark | `#18181B` |
| Logo fill | `#9147FF` |
| Search max-width | `40rem` |
| Search height | `3rem` |

**Navigation link**

| State | Light | Dark |
|---|---|---|
| Default | `#0E0E10` | `#EFEFF1` |
| Hover | `#5C16C5` / `#772CE8` depending selector | `#BF94FF` / `#A970FF` |
| Active indicator | `#5C16C5`, height `.2rem` | `#BF94FF`, height `.2rem` |

### Inputs & Forms

**Search**

```html
<div class="top-nav__search-container">
  <input class="tw-search" placeholder="Search" />
</div>
```

| Spec | Value |
|---|---|
| Container basis | `40rem` |
| Shell search height | `3rem` |
| Radius | `2px` |
| Background | light input surface; inline shell loader uses `rgba(255,255,255,.4)` |
| Focus | should use purple outline/border, not blue browser default |

### Hero Section

Twitch's homepage "hero" is a stream carousel, not a static brand headline.

| Spec | Value |
|---|---|
| Main object | large live video thumbnail/card |
| Support panel | channel avatar, title, category, viewer count, tags |
| Rail context | side live-channel list remains visible |
| Arrows | simple chevrons on page canvas |
| Background | #FFFFFF / app canvas |
| Emphasis | media first, text second |

### 13-2. Named Variants

**nav-logo-link** — Logo mark in top navigation. Light state uses #5C16C5, hover #772CE8; dark state uses #BF94FF, hover #A970FF.

**side-nav-expanded** — 24rem live-channel rail with #EFEFF1 light background and #26262C dark background. It is a persistent navigation surface, not a card.

**side-nav-collapsed** — 5rem icon rail. Preserve the width exactly; arbitrary 64px sidebars lose Twitch's product rhythm.

**video-card-focus-ring** — stream cards use purple border layers on focus/hover, not large elevation. The focus/hover cue should be `2px solid #9147FF` with small radius.

**social-icon-lift** — 3rem or 5rem square social controls that lift by `.3rem` on hover and reveal a small shadow pseudo-element.

**live-state-chip** — #E91916 rectangle for live/beta/alert state. This must stay red; do not brand-color live status.

### 13-3. Signature Micro-Specs

#### theme-aware-purple-swap

```yaml
theme-aware-purple-swap:
  description: "Twitch purple is not one hex — it shifts brightness across light shell vs dark player."
  technique: "#5C16C5 / #772CE8 inside light navigation states; #BF94FF / #A970FF inside .tw-root--theme-dark; same hue family, lifted lightness for dark contexts."
  applied_to: ["{component.logo-hover}", "{component.navigation-link}", "{component.active-indicator}", "social embed/copy icons"]
  visual_signature: "the same brand 'voltage' survives both the white marketing shell and the dark live-stream player."
  intent: "video products live in two worlds; a single static purple would feel either dim on dark or harsh on light."
```

#### rail-width-identity

```yaml
rail-width-identity:
  description: "The side rail is a measured broadcast object, not a generic sidebar."
  technique: "expanded width 24rem, collapsed width 5rem, rail surfaces #EFEFF1 (light) / #26262C (dark) with sticky 5rem top shell."
  applied_to: ["{component.side-rail}", "live channel list", "followed/promoted cards"]
  visual_signature: "even before a single thumbnail loads, Twitch already looks like a control deck — never a content portal."
  intent: "the rail is the platform's spine; codifying its width prevents marketing pages from drifting toward generic SaaS layout."
```

#### video-card-border-stack

```yaml
video-card-border-stack:
  description: "Stream cards earn focus through stacked borders, not soft drop shadows."
  technique: "transparent default border, `2px solid #9147FF` on focus/hover, `1px solid #451093` deeper card frame."
  applied_to: ["{component.video-card-offline}", "recommendation grid", "category card"]
  visual_signature: "focus reads as a game-UI selection ring — direct and performative, never SaaS-haze."
  intent: "gaming audiences expect crisp affordances; soft elevation would soften the broadcast energy."
```

#### social-button-lift-shadow

```yaml
social-button-lift-shadow:
  description: "Small share controls answer the cursor with a physical nudge instead of a colour fade."
  technique: "transform: translate3d(0, -0.3rem, 0) with `.1s ease-out`; ::after pseudo-element shadow `0 3px 10px -2px rgba(0,0,0,.6)` synced with lift."
  applied_to: ["{component.social-share-button}", "copy/download/embed icons"]
  visual_signature: "tiny controls feel mechanical and responsive without ever animating into spectacle."
  intent: "Twitch microinteractions stay short — the spectacle belongs to the streamer, never to the chrome."
```

#### live-status-as-color-not-icon

```yaml
live-status-as-color-not-icon:
  description: "Live state is signalled by a dedicated red token, not by a generic 'recording' icon."
  technique: "#E91916 (var(--tw-live)) used as a 6px circle / pill border on thumbnails, viewer counters, and channel headers; never substituted by emoji or sparkle motion."
  applied_to: ["{component.live-indicator}", "{component.viewer-counter}", "channel header dot"]
  visual_signature: "the platform whispers 'we are on air right now' through one calibrated red — calm, not blinking."
  intent: "live video has one universal tell; turning it into chrome (steady red dot) lets viewers scan the grid in milliseconds."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Platform descriptor | direct, broad, entertainment-category language | "interactive livestreaming service" |
| Primary CTA | short imperative account action | "Sign Up" |
| Secondary CTA | utility/account action | "Log In" |
| Row heading | literal content category | "Live on Twitch" |
| Metadata | compact, scan-first | "31.5K viewers", "Counter-Strike" |
| Alert banner | specific operational notice | shutdown/reminder/help message |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Twitch — copy into your root stylesheet */
:root {
  /* Fonts */
  --tw-font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --tw-font-family-display: "Roobert", "Inter", sans-serif;
  --tw-font-family-code: ui-monospace, SFMono-Regular, Menlo, monospace;
  --tw-font-weight-normal: 400;
  --tw-font-weight-semibold: 600;
  --tw-font-weight-bold: 700;

  /* Brand */
  --tw-color-brand-500: #9147FF;
  --tw-color-brand-hover: #772CE8;
  --tw-color-brand-active: #5C16C5;
  --tw-color-brand-dark-hover: #A970FF;
  --tw-color-brand-dark-active: #BF94FF;

  /* Surfaces */
  --tw-bg-page: #FFFFFF;
  --tw-bg-rail: #EFEFF1;
  --tw-bg-dark: #18181B;
  --tw-bg-rail-dark: #26262C;
  --tw-text: #0E0E10;
  --tw-text-dark: #EFEFF1;
  --tw-live: #E91916;

  /* Key geometry */
  --tw-shell-height: 5rem;
  --tw-side-rail-width: 24rem;
  --tw-side-rail-collapsed: 5rem;
  --tw-search-max-width: 40rem;
  --tw-control-height: 3rem;

  /* Radius */
  --tw-radius-control: 2px;
  --tw-radius-card: 4px;
  --tw-radius-round: 50%;
}

.tw-shell {
  height: var(--tw-shell-height);
  background: var(--tw-bg-page);
  color: var(--tw-text);
  display: flex;
  align-items: stretch;
}

.tw-side-rail {
  width: var(--tw-side-rail-width);
  background: var(--tw-bg-rail);
}

.tw-side-rail.is-collapsed {
  width: var(--tw-side-rail-collapsed);
}

.tw-search {
  height: var(--tw-control-height);
  max-width: var(--tw-search-max-width);
  border-radius: var(--tw-radius-control);
}

.tw-nav-link {
  color: var(--tw-text);
  font-family: var(--tw-font-family-display);
  font-weight: var(--tw-font-weight-semibold);
}

.tw-nav-link:hover,
.tw-nav-link.is-active {
  color: var(--tw-color-brand-active);
}

.tw-live-badge {
  background: var(--tw-live);
  color: #FFFFFF;
  border-radius: var(--tw-radius-control);
  font-weight: var(--tw-font-weight-bold);
}

.tw-video-card {
  border: 2px solid transparent;
  border-radius: var(--tw-radius-card);
  overflow: hidden;
}

.tw-video-card:hover,
.tw-video-card:focus-visible {
  border-color: var(--tw-color-brand-500);
}

.tw-theme-dark {
  background: var(--tw-bg-dark);
  color: var(--tw-text-dark);
}

.tw-theme-dark .tw-side-rail {
  background: var(--tw-bg-rail-dark);
}

.tw-theme-dark .tw-nav-link:hover,
.tw-theme-dark .tw-nav-link.is-active {
  color: var(--tw-color-brand-dark-active);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Twitch-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        twitch: {
          purple: '#9147FF',
          hover: '#772CE8',
          active: '#5C16C5',
          darkHover: '#A970FF',
          darkActive: '#BF94FF',
          live: '#E91916',
          page: '#FFFFFF',
          rail: '#EFEFF1',
          dark: '#18181B',
          darkRail: '#26262C',
          ink: '#0E0E10',
          inkDark: '#EFEFF1',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['Roobert', 'Inter', 'sans-serif'],
      },
      spacing: {
        shell: '5rem',
        rail: '24rem',
        railCollapsed: '5rem',
        search: '40rem',
      },
      borderRadius: {
        twitch: '2px',
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
| Brand primary | `tw-purple-500` | `#9147FF` |
| Brand hover light | `tw-purple-hover` | `#772CE8` |
| Brand active light | `tw-purple-active` | `#5C16C5` |
| Brand active dark | `tw-purple-dark-active` | `#BF94FF` |
| Background | `tw-surface-light` | `#FFFFFF` |
| Rail background | `tw-rail-light` | `#EFEFF1` |
| Text primary | `tw-text-light` | `#0E0E10` |
| Dark background | `tw-surface-dark` | `#18181B` |
| Live/error | `tw-live-red` | `#E91916` |

### Example Component Prompts

#### Hero / Stream Carousel
```text
Twitch 스타일의 홈 스트림 캐러셀을 만들어줘.
- 전체 구조: 5rem top shell + 24rem left live-channel rail + centered stream carousel.
- 배경: page #FFFFFF, rail #EFEFF1.
- 대표 스트림 카드는 media thumbnail first, channel detail panel second.
- LIVE badge는 #E91916, viewer chip은 dark translucent overlay.
- CTA/active/focus color는 #9147FF, hover는 #772CE8 또는 #5C16C5.
```

#### Card Component
```text
Twitch 스타일의 stream card를 만들어줘.
- thumbnail image가 카드의 80%를 차지.
- default border transparent, hover/focus에서 2px solid #9147FF.
- radius는 2px-4px 수준, 큰 rounded-xl 금지.
- title은 Inter 600/700, metadata는 작고 compact.
- shadow는 거의 쓰지 말고 thumbnail/content contrast로 구분.
```

#### Badge
```text
Twitch LIVE badge를 만들어줘.
- background #E91916, text #FFFFFF.
- font-weight 700, uppercase LIVE.
- radius 2px, padding은 작게.
- purple을 live state에 쓰지 말 것.
```

#### Navigation
```text
Twitch 스타일 상단 네비게이션을 만들어줘.
- height 5rem, background #FFFFFF, dark mode #18181B.
- logo/action purple #9147FF.
- nav link default #0E0E10, hover #772CE8, active #5C16C5.
- dark mode에서는 hover #A970FF, active #BF94FF.
- search는 max-width 40rem, height 3rem, radius 2px.
```

### Iteration Guide

- **색상 변경 시**: light/dark purple pair를 같이 바꿔라. #9147FF만 바꾸고 #A970FF/#BF94FF를 방치하면 dark UI가 깨진다.
- **폰트 변경 시**: Inter를 유지하고 Roobert만 display 대체 대상으로 본다.
- **여백 조정 시**: 5rem shell, 24rem rail, 5rem collapsed rail은 건드리지 않는 편이 Twitch 인식률이 높다.
- **카드 추가 시**: shadow보다 border/focus state를 먼저 설계한다.
- **라이브 상태 추가 시**: #E91916 red를 사용한다. Brand purple은 live status가 아니다.
- **다크 모드**: #18181B / #26262C / #EFEFF1 / #BF94FF 조합을 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #9147FF as the canonical Twitch action/identity purple.
- Split interaction purple by theme: #772CE8 / #5C16C5 in light UI, #A970FF / #BF94FF in dark UI.
- Keep the top shell at 5rem and the side rail at 24rem expanded / 5rem collapsed.
- Let thumbnails carry visual richness; keep chrome compact and mostly neutral.
- Use #E91916 for live/alert badges.
- Prefer small radius values around 2px-5px, with 50% only for avatars and circular icons.
- Use border/focus rings for video cards instead of heavy card shadows.
- Preserve dense metadata: viewer counts, category labels, language chips, and live dots belong close to the thumbnail.

### ❌ DON'T

- 배경을 `#F5F5F7` 또는 warm Apple gray로 두지 말 것 — Twitch captured shell은 `#FFFFFF`, rail은 `#EFEFF1` 사용.
- 텍스트를 `#000000`만으로 통일하지 말 것 — light primary text는 `#0E0E10`, dark primary text는 `#EFEFF1` 사용.
- Purple hover를 전부 `#9147FF`로 고정하지 말 것 — light hover/active는 `#772CE8` / `#5C16C5`, dark는 `#A970FF` / `#BF94FF` 사용.
- Live badge를 `#9147FF`로 두지 말 것 — live state는 `#E91916` 사용.
- Rail background를 `#FFFFFF`로 평평하게 만들지 말 것 — left rail은 `#EFEFF1`, dark rail은 `#26262C` 사용.
- Dark shell을 pure `#000000`으로 만들지 말 것 — dark shell은 `#18181B` 사용.
- CTA/control radius를 `999px` pill로 만들지 말 것 — shell controls는 `2px` 중심의 squared Twitch geometry.
- Video cards에 큰 `box-shadow`를 기본값으로 넣지 말 것 — hover/focus border `#9147FF`가 먼저다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- No luxury whitespace. Twitch does not create calm gallery pages; it keeps live inventory dense.
- No single universal purple. The brand has theme-aware and state-aware purple steps.
- No large rounded SaaS pills in the main chrome. Auth/search controls are compact rectangles.
- No marketing hero H1 as the primary identity. The stream carousel and rails are the hero.
- No decorative full-page gradient background. Gradients appear in specific promoted/social contexts, not as the page shell.
- No soft pastel palette. Purple, red live state, and hard neutrals do the work.
- No heavy editorial typography. UI copy stays compact and scannable.
- No shadow-first card system. Thumbnail, border, and live metadata define cards.
- No invented second brand color. Pink/cyan/social colors are contextual accents, not co-primary brand colors.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single captured surface** — Analysis reused the existing `insane-design/twitch` homepage capture. Login, creator dashboard, stream watch page, chat, settings, and checkout/subscription flows were not visited.
- **Token tier is weakly observable** — `resolved_tokens.json` contained only `--writing-dir-flip`; the named token layer in this document is a guide alias over real extracted hex/classes, not proof of exported Twitch CSS variables.
- **Typography scale incomplete** — `typography.json` found families and weights but no clean size scale. Exact heading/body ladder is inferred from CSS snippets and screenshot density.
- **Runtime HTML is app-shell heavy** — The HTML snapshot exposes scripts and shell loader classes, with no semantic `main`, `section`, `nav`, `button`, or `input` tags in static markup. Component interpretation relies on compiled CSS class names and screenshot observation.
- **Mobile behavior not visually re-captured** — Breakpoints were extracted from CSS, but no separate mobile screenshot was inspected in this pass.
- **Motion JS not analyzed** — CSS transitions were captured, but React/runtime interaction logic, carousel behavior, and player/chat animation are outside the phase1 data used here.
- **Color contamination risk** — Social share colors (#3B5998, #FF4500, etc.) and special promo gradients are present in CSS. They are documented as contextual accents, not brand palette.
- **Korea shutdown banner in screenshot** — The captured screenshot includes a regional business shutdown notice dated February 27, 2024 KST. That banner is treated as a captured state, not the universal Twitch homepage baseline.
