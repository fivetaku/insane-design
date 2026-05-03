---
schema_version: 3.2
slug: spotify-main
service_name: Spotify Web Player
site_url: https://open.spotify.com
fetched_at: 2026-04-14T01:20:00+09:00
default_theme: dark
brand_color: "#1ED760"
primary_font: SpotifyMixUI
font_weight_normal: 400
token_prefix: encore

bold_direction: Immersive Utility
aesthetic_category: other
signature_element: app-dashboard
code_complexity: very_high

medium: web
medium_confidence: high

archetype: app-dashboard
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Encore tokens are present in production CSS and drive button, list-row, image, link, radius, spacing, and motion primitives."

colors:
  ink-black: "#000000"
  surface-base: "#121212"
  surface-elevated: "#282828"
  text-base: "#FFFFFF"
  text-subdued: "#B3B3B3"
  brand-green: "#1ED760"
  focus-blue: "#3673D4"
  overlay-white-10: "#FFFFFF1A"
  scrollbar-white-30: "#FFFFFF4D"

typography:
  display: "SpotifyMixUITitle"
  body: "SpotifyMixUI"
  mono: "SpotifyMixMono"
  ladder:
    - { token: marginal-small, size: ".5625rem", weight: 400, tracking: "0" }
    - { token: marginal, size: ".6875rem", weight: 400, tracking: "0" }
    - { token: body-small, size: ".8125rem", weight: 400, tracking: "0" }
    - { token: body, size: "1rem", weight: 400, tracking: "0" }
    - { token: title-small, size: "1.25rem", weight: 700, tracking: "0" }
    - { token: title-large, size: "2rem", weight: 700, tracking: "0" }
    - { token: headline-large, size: "3rem", weight: 800, tracking: "0" }
  weights_used: [100, 300, 400, 600, 700, 800]
  weights_absent: [500]

components:
  shell-grid: { bg: "{colors.ink-black}", gap: "var(--panel-gap)", left_sidebar: "232px", min_width: "800px" }
  library-panel: { bg: "{colors.ink-black}", radius: "8px", width: "232px" }
  main-panel: { bg: "{colors.surface-base}", radius: "8px", max_width: "1955px" }
  list-row: { bg: "transparent", hover: "var(--background-highlight)", radius: "6px", padding: "8px" }
  button-primary: { min_height: "48px", large_height: "56px", padding: "12px 32px", radius: "calc(infinity * 1px)" }
  album-image: { aspect: "1 / 1", radius: "4px", transition: "opacity var(--encore-productive-enter)" }
---

# DESIGN.md — Spotify Web Player

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Spotify Web Player is not a page trying to sell music. It is a listening room pretending to be software: almost everything recedes into #000000 (`{colors.ink-black}`) and #121212 (`{colors.surface-base}`) so album art can become the actual palette. The interface behaves like a midnight record shop where the lights are off but every sleeve is still lit from the shelf.

The system's most important move is the pane architecture. The screenshot shows a compact home rail, a 232px library column, a rounded main canvas, and a fixed bottom signup bar. Each surface is separated by black gutters and 8px panel corners rather than borders. It is not a dashboard of cards; it is a set of dark rooms cut into one viewport, with the gaps doing the architectural work.

Spotify green #1ED760 (`{colors.brand-green}`) is a brand memory, not the page's dominant color. There is no second brand wallpaper moment, and no green wash over the product. In the captured unauthenticated web player, green mostly lives in tokens and potential accent states while the visible screen relies on white CTAs, gray labels, album art, and the purple-blue signup band. The famous color is held back like a stage light waiting off-cue.

The album and artist imagery are the chroma engine. UI chrome stays matte, black, and noncompetitive so covers can act like tiny illuminated posters on a theater wall. #000000 (`{colors.ink-black}`) is not just "dark mode"; it is the velvet around the frame, making every square cover feel brighter than it is.

The typography is blunt and readable. SpotifyMixUI carries dense operational labels; SpotifyMixUITitle appears where the interface needs a section headline. The key absence is weight 500: the system jumps from regular 400 to confident 700/800, like skipping a polite speaking voice and going straight from catalog label to section sign.

Motion is functional rather than decorative. There are opacity fades, list-row state transitions, scroll behavior, view-transition names for major panels, and resizer affordances. The craft is not a hero animation; it is the way the shell keeps moving parts predictable while music content changes constantly. The page has almost no "website" self-consciousness — it erases itself into an app shell and lets the library feel already in use.

To press the picture further: the player bar at the bottom is the mixing console permanently bolted under the screen, the library column is the long row of vinyl crates against the back wall, and the queue acts like a turntable spindle waiting for the next sleeve. The Now Playing panel behaves like the listening booth of a record store with the door half-closed. The sticky signup bar is the velvet rope at the entrance, polite but unmistakable. There is no second brand color performing on the dark stage because the spotlight is reserved for the album art.

### Key Characteristics

- Dark app shell: #000000 outside, #121212 inside, #282828 for elevated utility.
- Modular pane system: left sidebar, main view, optional right sidebar, and now-playing/signup bottom zone.
- 8px panel radius is the structural signature; smaller 4px radius belongs to artwork and small controls.
- Album and artist imagery supply chroma; UI surfaces stay neutral.
- White primary CTAs are visible in unauthenticated flows; green is reserved for brand/accent semantics.
- Subdued labels use #B3B3B3, not low-opacity white guessing.
- Focus uses #3673D4 browser/OS-style blue outlines, not Spotify green.
- Content spacing clamps from 16px to 24px based on container width.
- The app has desktop minimums: body min-width 800px and min-height 600px.
- Motion is short and productive: 50ms, .1s, .15s, .2s tokens plus cubic-bezier(.3,0,0,1).

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Immersive Utility
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **dark pane architecture around vivid music artwork**으로 기억된다.
> **Code Complexity**: very_high — production web-player CSS includes container queries, view transitions, resizers, overlay scrollbars, component variants, and multi-state Encore primitives.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Spotify Web Player처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "SpotifyMixUI", "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
}

/* 2. 앱 셸 */
:root {
  --bg-shell: #000000;
  --bg-panel: #121212;
  --fg: #FFFFFF;
  --fg-subdued: #B3B3B3;
}
body {
  background: var(--bg-shell);
  color: var(--fg-subdued);
  min-width: 800px;
  min-height: 600px;
  overflow: hidden;
}

/* 3. Spotify accent */
:root { --brand: #1ED760; }
.panel { background: var(--bg-panel); border-radius: 8px; }
```

**절대 하지 말아야 할 것 하나**: 전체 배경을 #1ED760 또는 브랜드 그린 그라디언트로 채우지 말 것. Spotify Web Player의 실제 기본 인상은 black shell + dark panels + artwork color다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://open.spotify.com` |
| Fetched | 2026-04-14 phase1 reuse |
| Extractor | existing phase1 artifacts + captured `index.html` + `web-player.28b9193f.css` |
| HTML size | 5,928 bytes (Spotify Web Player shell) |
| CSS files | 1 external + 1 tiny inline, main CSS 446,329 bytes |
| Token prefix | `encore` |
| Method | CSS custom properties, frequency candidates, screenshot observation, and production component snippets |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Spotify Web Player production bundle (`web-player.a9293410.js`, vendor bundle, Encore bundle).
- **Design system**: Encore — prefix `--encore-*` for spacing, radius, control size, text scale, motion, component primitives.
- **CSS architecture**:
  ```css
  :root                             /* shell-level app variables */
  --encore-*                        /* design-system primitives */
  --background-* / --text-*         /* theme aliases */
  .e-10180-*                        /* Encore component classes */
  hashed app classes                /* layout and feature-specific composition */
  ```
- **Class naming**: mixed production hashes plus stable Encore component namespace (`.e-10180-button`, `.e-10180-list-row`, `.e-10180-image`).
- **Default theme**: dark (`html.encore-dark-theme`, `html { background-color: #121212 }`).
- **Font loading**: preloaded WOFF2 from `encore.scdn.co` for SpotifyMixUI, SpotifyMixMono, and SpotifyMixUITitleVariable.
- **Canonical anchor**: `https://open.spotify.com/`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `SpotifyMixUITitle` / `SpotifyMixUITitleVariable` (Spotify-hosted brand font).
- **Body font**: `SpotifyMixUI`.
- **Code font**: `SpotifyMixMono`.
- **Fallback families**: `CircularSp-Arab`, `CircularSp-Hebr`, `CircularSp-Cyrl`, `CircularSp-Grek`, `CircularSp-Deva`, then generic fallback.
- **Weight normal / bold**: `400` / `700`; display headline can hit `800`.

```css
:root {
  --encore-body-font-stack: SpotifyMixUI, CircularSp-Arab, CircularSp-Hebr,
    CircularSp-Cyrl, CircularSp-Grek, CircularSp-Deva, var(--fallback-fonts, sans-serif);
  --encore-bodyMono-font-stack: SpotifyMixMono, CircularSp-Arab, CircularSp-Hebr,
    CircularSp-Cyrl, CircularSp-Grek, CircularSp-Deva, var(--fallback-fonts, monospace);
  --encore-title-font-stack: SpotifyMixUITitle, CircularSp-Arab, CircularSp-Hebr,
    CircularSp-Cyrl, CircularSp-Grek, CircularSp-Deva, var(--fallback-fonts, sans-serif);
}
```

### Note on Font Substitutes

- **SpotifyMixUI** is proprietary-hosted in the captured page. If rebuilding without those assets, use **Inter** at 400/700/800 and keep letter-spacing at `0`; do not add negative tracking to imitate editorial brands.
- **SpotifyMixUITitle** can be approximated by **Inter Tight** or **Arial** only if section heads remain heavy and compact. Preserve the 400 -> 700/800 jump and keep weight 500 absent.
- **SpotifyMixMono** can fall back to **Roboto Mono** or `ui-monospace`, but use it sparingly. The web player is not code-forward.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| marginal-small | `.5625rem` / alternate `.625rem` | 400 | normal | 0 |
| marginal | `.6875rem` / alternate `.75rem` | 400 | normal | 0 |
| body-small | `.8125rem` / alternate `.875rem` | 400 / 700 | normal | 0 |
| body | `1rem` | 400 / 700 | normal | 0 |
| large | `1.125rem` / alternate `1.25rem` | 700 | normal | 0 |
| title-small | `1.25rem` / alternate `1.5rem` | 700 | balanced | 0 |
| title-medium | `1.5rem` / alternate `2rem` | 700 | balanced | 0 |
| title-large | `2rem` / alternate `3rem` | 700 | balanced | 0 |
| headline-medium | `2.5rem` / alternate `4rem` | 700 | balanced | 0 |
| headline-large | `3rem` / alternate `6rem` | 800 | balanced | 0 |

> ⚠️ The captured CSS exposes two scale ranges, likely compact and larger responsive/theme variants. Use the compact values for dense app panes and the larger values only for full-width editorial/player states.

### Principles

1. Body text is operational, not editorial: `1rem` at 400 for readable labels and metadata.
2. Section titles jump to 700 or 800. Weight 500 is deliberately absent and should not be inserted as a middle tone.
3. Letter-spacing stays at `0`; Spotify's density comes from weight and dark contrast, not optical tracking.
4. Metadata hierarchy is color-led: #B3B3B3 separates artist names and secondary labels from #FFFFFF titles.
5. `text-wrap: balance` appears on title/headline classes, so large headings should wrap cleanly rather than raggedly.
6. The type stack is multilingual first; do not collapse it to a single Latin-only custom font in global CSS.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp

| Token | Hex |
|---|---|
| `--text-bright-accent` | `#1ED760` |
| `--essential-bright-accent` | `#1ED760` |
| `--background-base` accent variant | `#1ED760` |
| hover/positive supporting green | `#1ABC54` |
| high green highlight | `#3BE477` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| green dark text/accent variant | `#073116` |
| green dark alternate | `#107434` |
| green dark alternate | `#127E38` |
| green essential alternate | `#159542` / `#169F47` |

### 06-3. Neutral Ramp

| Step | Dark |
|---|---|
| shell | `#000000` |
| base panel | `#121212` |
| near panel | `#141414` |
| elevated card | `#181818` |
| tooltip/elevated utility | `#282828` |
| subdued text | `#B3B3B3` |
| primary text | `#FFFFFF` |
| transparent overlay | `#00000000` |
| white overlay low | `#FFFFFF1A` |
| scrollbar/handle | `#FFFFFF4D` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| focus | browser/OS focus ring | `#3673D4` |
| blue | announcement/variant | `#0D72EA` / `#052A56` / `#C8E0FC` |
| red | negative/error family | `#E91429` / `#590810` / `#FFD2D7` |
| yellow/orange | warning family | `#FFA42B` / `#491E00` / `#FFD97E` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--background-base` | `#121212` | default main app surface |
| `--background-base` dark shell variant | `#000000` | outer frame / sidebar / grid gaps |
| `--text-base` | `#FFFFFF` | primary labels, song names, CTA text |
| `--text-subdued` | `#B3B3B3` | metadata, muted links, secondary buttons |
| `--text-bright-accent` | `#1ED760` | inline accent and positive/brand state |
| `--decorative-subdued` | `#FFFFFF21` | hairline/inset decoration |
| `--generic-tooltip-background-color` | `#282828` | tooltip surface |
| focus outline | `#3673D4` | keyboard focus ring |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--background-base` | theme-dependent, default `#121212` | base panel surfaces |
| `--background-elevated-base` | dark elevated alpha | menus, overlays, elevated rows |
| `--background-highlight` | dark hover alias | list row and button hover |
| `--background-press` | dark press alias | active state |
| `--background-tinted-base` | translucent dark/white mix | secondary surfaces |
| `--text-base` | `#FFFFFF` in dark theme | primary copy |
| `--text-subdued` | `#B3B3B3` in dark theme | muted copy |
| `--essential-subdued` | subdued essential token | resize bars, icons, separators |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Hex | Frequency | Kind |
|---|---:|---|
| `#FFFFFF` | 279 | neutral |
| `#000000` | 193 | neutral |
| `#00000000` | 119 | transparent |
| `#FFFFFF1A` | 44 | neutral alpha |
| `#1ED760` | 37 | chromatic brand |
| `#FFFFFFB3` | 27 | neutral alpha |
| `#121212` | 24 | neutral |
| `#282828` | 23 | neutral |
| `#B3B3B3` | 17 | neutral |

### 06-8. Color Stories

**`{colors.ink-black}` (`#000000`)** — The outer shell. It frames the app, fills gutters, supports the left library panel, and makes every album cover feel illuminated. Use it as the page floor, not as a decorative overlay.

**`{colors.surface-base}` (`#121212`)** — The main listening surface. This is the perceived background of the player canvas and the correct default for panels that hold content lists, cards, and scroll regions.

**`{colors.text-base}` (`#FFFFFF`)** — The decisive foreground. Song titles, main headings, important links, and primary button labels use white because the interface is already low-light.

**`{colors.brand-green}` (`#1ED760`)** — The memory color, not the wallpaper. It should appear in brand/accent/positive states and selected moments. When rebuilding the captured unauthenticated screen, let imagery and neutral surfaces dominate first.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--encore-spacing-tighter-5` | `2px` | micro offsets |
| `--encore-spacing-tighter-4` | `4px` | icon padding, tight gaps |
| `--encore-spacing-tighter-3` | `6px` | tiny inline separations |
| `--encore-spacing-tighter-2` | `8px` | list row padding, condensed controls |
| `--encore-spacing-tighter` | `12px` | list gaps, tooltip padding |
| `--encore-spacing-base` | `16px` | primary app rhythm |
| `--encore-spacing-looser` | `20px` / alternate `24px` | medium button padding |
| `--encore-spacing-looser-2` | `24px` / alternate `32px` | large button padding |
| `--encore-spacing-looser-3` | `32px` / alternate `48px` | section/footer rhythm |
| `--encore-spacing-looser-6` | `64px` / alternate `128px` | large layout spacing |
| `--content-spacing` | `clamp(16px,16px + (var(--main-view-grid-width) - 600px)/424*8,24px)` | main view horizontal padding |

**주요 alias**:
- `--content-spacing` -> 16px to 24px, tied to main-view container width.
- `--left-sidebar-width` -> 232, then used as `calc(var(--left-sidebar-width) * 1px)`.
- `--content-max-width` -> 1955px for content bands inside the main view.

### Whitespace Philosophy

Spotify's whitespace is compressed at the chrome level and generous at the content rail level. The shell uses tiny black gutters and 8px panel corners to conserve every pixel, then lets album cards sit in wide horizontal lanes. The feeling is "dense controls, relaxed browsing."

The main view does not use a marketing max-width like 1120px. It allows `--content-max-width: 1955px`, then pads content with a container-aware 16px-to-24px clamp. That choice keeps wide screens full of music rather than centered copy.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| `--encore-corner-radius-smaller` | `2px` | micro controls and fine UI |
| `--encore-corner-radius-base` | `4px` | album images, small links, focus shapes |
| `--encore-corner-radius-larger` | `6px` | list rows, tooltips |
| `--encore-corner-radius-larger-2` | `8px` | major panels, app cards, sidebars |
| `--encore-corner-radius-larger-3` | `16px` | large containers or soft promotional surfaces |
| button pill | `calc(infinity * 1px)` / full pill | primary rounded CTAs |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none/default | none | most panels; dark surface separation does the work |
| inset hairline | `inset 0 0 0 var(--encore-border-width-hairline) var(--decorative-subdued)` | bordered list rows / selected states |
| overlay shadow | `var(--encore-overlay-box-shadow)` | popover navigation and overlay menus |
| alpha scrim | `#000000B3`, `#000000E6` | dialogs and modal overlays |

Spotify's web player is not a shadow-heavy product. It gets depth from surface color, rounded panel seams, artwork brightness, and alpha scrims. Heavy material shadows would make it feel like a generic admin app.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| `--encore-shortest-1` | `50ms` | instant active feedback |
| `--encore-shortest-2` | `.1s` | fast control feedback |
| `--encore-shortest-3` | `.15s` | hover/list-row transition |
| `--encore-shortest-4` | `.2s` | short exit |
| `--encore-productive` | `cubic-bezier(.3,0,0,1)` | general state transitions |
| `--encore-productive-decelerate` | `cubic-bezier(0,0,.2,1)` | entering/settling panels |
| `--encore-productive-accelerate` | `cubic-bezier(.8,0,1,1)` | exit transitions |
| root background | `.5s cubic-bezier(.3,0,.4,1)` | app background transitions |
| reduced motion | `prefers-reduced-motion: reduce` disables view-transition animations | accessibility |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `1955px`.
- **Grid type**: CSS Grid shell with named areas plus flexbox inside panels.
- **Column count**: shell grid defines `left-sidebar main-view right-sidebar`; active columns depend on right-sidebar visibility.
- **Gutter**: `var(--panel-gap)` between shell areas; captured screenshot visually reads as tight black gutters.
- **Minimum viewport**: `body { min-width: 800px; min-height: 600px; overflow: hidden; }`.

### Hero

- **Pattern Summary**: `100vh app shell + left library pane + main music rails + fixed bottom signup CTA`.
- Layout: not a conventional marketing hero. The first viewport is the complete app: global nav/search, library rail, trending songs, popular artists, and signup bar.
- Background: black shell `#000000`, main panel `#121212`, elevated cards around `#181818` / `#282828`.
- **Background Treatment**: solid dark surfaces plus a low-opacity noise variable (`--background-noise`) available in root; no large decorative gradient in the app body.
- H1/section title: section titles around `2rem`/700 in screenshot-like density.
- Max-width: main content constrained by `--content-max-width: 1955px`, not by a narrow marketing container.

### Section Rhythm

```css
.contentSpacing {
  max-width: var(--content-max-width);
  padding: 0 var(--content-spacing);
  width: 100%;
}

.main-view {
  --content-spacing: clamp(16px, 16px + (var(--main-view-grid-width) - 600px) / 424 * 8, 24px);
}
```

### Card Patterns

- **Card background**: base music panels use `#121212`; library prompt cards read as `#1f1f1f`/near-`#282828`.
- **Card border**: usually none; separation is color and radius.
- **Card radius**: 8px for app panels, 4px for album covers, circular for artist imagery.
- **Card padding**: library prompt cards around 20px; list rows 8px; main content lanes 16px-24px.
- **Card shadow**: none by default.

### Navigation Structure

- **Type**: horizontal global controls + left library sidebar.
- **Position**: fixed app shell within viewport; body overflow hidden; internal scroll nodes handle content.
- **Height**: nav/search row visually about 56px-64px; bottom signup/now-playing zone about 64px.
- **Background**: `#000000` shell, with pill controls around `#1f1f1f` and white login CTA.

### Content Width

- Main view can stretch to 1955px.
- Left sidebar uses `--left-sidebar-width: 232`.
- Search field and nav controls use pill geometry.
- Horizontal media rails overflow and crop at viewport edges rather than wrapping into a masonry grid.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Behavior | Evidence | Interpretation |
|---|---|---|
| Desktop floor | `min-width: 800px`, `min-height: 600px` | The captured web player is optimized as an app viewport, not a fully fluid mobile page. |
| Container-aware spacing | `@container main-view-grid-area (width>0)` and `100cqw` | Main content reacts to panel width rather than global viewport alone. |
| Internal scroll | body overflow hidden, scroll nodes inside main view | The app keeps chrome fixed while content panes scroll. |
| Reduced motion | `prefers-reduced-motion` rules remove view-transition animations | Motion is opt-out aware. |
| Touch manipulation | `a, button { touch-action: manipulation; }` | Controls are optimized for responsive pointer behavior. |

Breakpoints are not expressed as a simple marketing set (`640/768/1024`). The design is more application-native: container queries, minimum desktop dimensions, panel width variables, and shell state flags do the responsive work.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### 13-1. Core Component Categories

**Buttons** — Encore buttons expose small/medium/large sizes. Medium uses `--encore-control-size-base: 48px`; large uses `--encore-control-size-larger: 56px`. Primary CTAs in the screenshot are white pills with black text, not green blocks.

**Icon Buttons** — Icon-only controls map to 32px, 48px, and 56px control sizes. Home, library add, install, and player controls should remain circular or pill-contained.

**List Rows** — `.e-10180-list-row` is flex, `gap: 12px`, `padding: 8px`, `border-radius: 6px`, and changes background through hover/active aliases. Rows are the core browsing primitive.

**Images** — `.e-10180-image` uses `object-fit: cover`, aspect-ratio tokens, max dimensions, and opacity transitions. Album covers are square with small radius; artists are circular.

**Links** — Inline links underline; standalone links inherit color and underline on hover/active. Subtle links begin at #B3B3B3 and move to #FFFFFF.

**Tooltips / Popovers** — Tooltip max-inline-size is 240px, radius 6px, with 8px/12px padding. Desktop popovers use elevated backgrounds and overlay shadow; mobile popover nav fixes to the bottom.

### 13-2. Named Variants

- **`shell-grid`** — `display: grid`, named app areas, black background, `var(--panel-gap)`, full height.
- **`library-panel`** — width `232px`, black surface, 8px radius, vertical flex.
- **`main-view-panel`** — grid-area `main-view`, #121212-like background, 8px radius, internal scroll.
- **`button-primary-white`** — pill radius, white background, black text, strong login/signup use.
- **`button-secondary-bordered`** — currentColor or `--essential-subdued` outline, hover changes outline to text base.
- **`list-row-interactive`** — transparent base, alias-driven hover/press, 6px radius.
- **`artist-avatar`** — 1:1 image, circular mask, object-fit cover.
- **`album-cover`** — 1:1 image, 4px radius, opacity fade on load.
- **`bottom-signup-bar`** — high-chroma promotional strip sitting outside the dark panel grammar.

### 13-3. Signature Micro-Specs

#### black-gutter-pane-rounding

```yaml
black-gutter-pane-rounding:
  description: "Major app regions read as dark rooms separated by black negative space, not by strokes."
  technique: "shell bg #000000 /* {colors.ink-black} */ + panel bg #121212 /* {colors.surface-base} */ + 8px major radius + var(--panel-gap)"
  applied_to: ["{component.shell-grid}", "{component.library-panel}", "{component.main-panel}"]
  visual_signature: "Rounded dark panes float inside a pure black viewport floor; the gutter is the separator."
```

#### artwork-as-palette-rail

```yaml
artwork-as-palette-rail:
  description: "Music imagery supplies the chroma while UI chrome stays neutral and matte."
  technique: "album/artist image aspect-ratio 1 / 1, object-fit: cover, album radius 4px, opacity transition var(--encore-productive-enter)"
  applied_to: ["{component.album-image}", "{component.main-panel}"]
  visual_signature: "Rows of saturated album covers become the only loud color field against #121212."
```

#### subdued-to-white-link-lift

```yaml
subdued-to-white-link-lift:
  description: "Secondary labels become actionable by lifting from metadata gray to full white."
  technique: "base color #B3B3B3 /* {colors.text-subdued} */ -> hover/focus #FFFFFF /* {colors.text-base} */ with .2s linear color transition"
  applied_to: ["{component.list-row}", "{component.main-panel}"]
  visual_signature: "Muted artist names and utility links brighten without changing layout or adding decoration."
```

#### blue-focus-honesty

```yaml
blue-focus-honesty:
  description: "Keyboard focus remains system-like instead of being recolored into Spotify green."
  technique: "outline: 5px auto #3673D4 /* {colors.focus-blue} */; outline-offset: 2px"
  applied_to: ["{component.button-primary}", "{component.list-row}"]
  visual_signature: "A browser-blue accessibility ring cuts through the dark shell as a functional signal."
```

#### no-medium-weight-snap

```yaml
no-medium-weight-snap:
  description: "Hierarchy avoids a soft middle voice; it jumps from regular labels to bold section signage."
  technique: "weights_used: 100/300/400/600/700/800; weights_absent: 500; title weights 700-800; letter-spacing 0"
  applied_to: ["{component.main-panel}", "{component.list-row}"]
  visual_signature: "Titles snap against subdued metadata because there is no 500-weight intermediary."
```

## 14. Content Voice
<!-- SOURCE: manual -->

Spotify's UI voice is direct and action-oriented: "Create playlist", "Browse podcasts", "Show all", "Install App", "Log in". It avoids whimsical onboarding copy inside the app shell. The tone is confident but compact, with short verbs and object nouns.

The unauthenticated page uses friendly prompts in the library column, but the surrounding player remains utilitarian. Do not let marketing voice leak into controls; controls should read like software.

---

## 15. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  --sp-shell: #000000;
  --sp-panel: #121212;
  --sp-panel-elevated: #282828;
  --sp-text: #FFFFFF;
  --sp-text-subdued: #B3B3B3;
  --sp-green: #1ED760;
  --sp-focus: #3673D4;

  --sp-radius-panel: 8px;
  --sp-radius-row: 6px;
  --sp-radius-art: 4px;
  --sp-sidebar: 232px;
  --sp-content-max: 1955px;
  --sp-content-pad: clamp(16px, 2cqw, 24px);

  --sp-ease: cubic-bezier(.3, 0, 0, 1);
  --sp-fast: .15s;
}

body.spotify-like {
  margin: 0;
  min-width: 800px;
  min-height: 600px;
  overflow: hidden;
  background: var(--sp-shell);
  color: var(--sp-text-subdued);
  font-family: "SpotifyMixUI", "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
}

.sp-shell {
  display: grid;
  grid-template:
    "top top top"
    "left main right" 1fr
    "bottom bottom bottom"
    / var(--sp-sidebar) 1fr auto;
  gap: 8px;
  height: 100vh;
  padding: 8px;
  background: var(--sp-shell);
}

.sp-panel {
  background: var(--sp-panel);
  border-radius: var(--sp-radius-panel);
  overflow: hidden;
}

.sp-content {
  width: 100%;
  max-width: var(--sp-content-max);
  padding-inline: var(--sp-content-pad);
}

.sp-title {
  color: var(--sp-text);
  font-family: "SpotifyMixUITitle", "Inter", sans-serif;
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: 0;
}

.sp-meta {
  color: var(--sp-text-subdued);
  font-size: .875rem;
}

.sp-button-primary {
  min-height: 48px;
  padding: 12px 32px;
  border: 0;
  border-radius: 999px;
  background: #FFFFFF;
  color: #000000;
  font-weight: 700;
}

.sp-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px;
  border-radius: var(--sp-radius-row);
  background: transparent;
  color: var(--sp-text);
  transition: background-color var(--sp-fast) var(--sp-ease);
}

.sp-row:hover {
  background: rgba(255, 255, 255, .1);
}

.sp-art {
  aspect-ratio: 1 / 1;
  width: 100%;
  object-fit: cover;
  border-radius: var(--sp-radius-art);
  transition: opacity .2s var(--sp-ease);
}

.sp-link-subtle {
  color: var(--sp-text-subdued);
  transition: color .2s linear;
}

.sp-link-subtle:hover,
.sp-link-subtle:focus {
  color: var(--sp-text);
}

.sp-focus:focus-visible {
  outline: 5px auto var(--sp-focus);
  outline-offset: 2px;
}
```

---

## 16. Tailwind Mapping
<!-- SOURCE: manual -->

```js
export const spotifyTheme = {
  colors: {
    shell: "#000000",
    panel: "#121212",
    elevated: "#282828",
    text: "#FFFFFF",
    subdued: "#B3B3B3",
    green: "#1ED760",
    focus: "#3673D4",
  },
  borderRadius: {
    art: "4px",
    row: "6px",
    panel: "8px",
    pill: "999px",
  },
  spacing: {
    tighter2: "8px",
    tighter: "12px",
    base: "16px",
    looser: "20px",
    looser2: "24px",
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

- Shell: `#000000`
- Panel: `#121212`
- Elevated surface: `#282828`
- Primary text: `#FFFFFF`
- Subdued text: `#B3B3B3`
- Brand accent: `#1ED760`
- Focus ring: `#3673D4`

### Build Prompt

Build a Spotify Web Player inspired app shell, not a generic music landing page. Use a #000000 viewport floor, #121212 rounded panels, 8px major panel radius, a 232px left library sidebar, a main content panel with horizontal album and artist rails, and a fixed bottom signup or now-playing bar. Keep typography in a SpotifyMixUI-like sans stack at 400/700/800 with no weight 500. Use #1ED760 only as a restrained accent or selected state; let album artwork provide most color. Primary unauthenticated CTAs should be white pills with black text. Use #B3B3B3 for metadata and #3673D4 for focus outlines.

### Avoid Prompt

Do not create a bright green hero page, a centered marketing headline, a purple-blue AI gradient background, glassmorphism cards, or oversized decorative music notes. The reference is a dark production web app with dense, pane-based utility and artwork-driven chroma.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO

- Use #000000 as the shell floor and #121212 as the main panel surface.
- Keep major app panels at 8px radius and list rows around 6px.
- Use #FFFFFF for primary text and button labels; use #B3B3B3 for secondary metadata.
- Let album covers and artist images introduce most color.
- Preserve the 232px left sidebar logic for desktop app-like layouts.
- Use short productive motion tokens: 50ms, .1s, .15s, .2s.
- Keep keyboard focus visible with #3673D4 outlines.
- Use white pill CTAs for unauthenticated login/signup moments.

### DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 app shell은 `#000000`, main panel은 `#121212` 사용.
- 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — dark player primary text는 `#FFFFFF`, secondary text는 `#B3B3B3` 사용.
- 브랜드 컬러를 `#1ED760` 전체 배경으로 깔지 말 것 — green은 accent/positive state로 제한하고 surface는 `#000000`/`#121212` 유지.
- 카드 표면을 `#FFFFFF`로 만들지 말 것 — elevated dark card는 `#181818` 또는 `#282828` 계열 사용.
- muted text를 `#777777` 같은 임의 회색으로 추정하지 말 것 — 실제 subdued 기준은 `#B3B3B3`.
- focus ring을 `#1ED760`으로 바꾸지 말 것 — keyboard focus evidence는 `#3673D4`.
- body에 `font-weight: 500` 사용 금지 — Spotify hierarchy는 400에서 700/800으로 점프한다.
- shell을 `min-width: 320px` 모바일 랜딩처럼 풀지 말 것 — captured app CSS has `min-width: 800px` and `min-height: 600px`.
- panel radius를 `24px` 이상으로 키우지 말 것 — major panels are 8px, artist images are circular, buttons are pills.
- UI 전체에 box-shadow elevation을 추가하지 말 것 — depth는 dark surfaces, alpha overlays, and artwork contrast가 만든다.

### 🚫 What This Site Doesn't Use

- No white document canvas as the default experience.
- No green brand wallpaper despite Spotify's famous brand color.
- No broad marketing hero with centered H1 and CTA stack.
- No glassmorphism blur cards.
- No beige, cream, or editorial paper warmth.
- No 12-column marketing card grid as the primary first viewport.
- No heavy drop-shadow hierarchy on panels.
- No visible decorative icons unrelated to playback, search, library, install, or account actions.
- No weight-500 typography middle layer.
- No negative letter-spacing display treatment.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- The reused `index.html` is an app shell and script bootstrap, not a fully hydrated DOM snapshot. Layout and component analysis relies on the captured screenshot plus production CSS snippets.
- The screenshot captures an unauthenticated Korea-market web player state on April 23, 2026. Logged-in, premium, mobile, and locale-specific states may expose different panels and accent usage.
- `--panel-gap` is referenced in production CSS, but its resolved numeric value was not present in the sampled phase1 token resolver output. The guide treats it as an 8px-like tight black gutter based on screenshot geometry and adjacent CSS.
- The CSS contains many theme variants where aliases such as `--background-base` resolve to multiple colors. This guide uses the visible dark default and frequency evidence as the canonical recreation target.
- Motion specs are extracted from CSS tokens and snippets, but no live interaction trace was recorded in this run.
- The bottom signup bar uses a promotional purple-blue treatment visible in the screenshot; its exact gradient stops were not extracted from the sampled CSS snippets, so it is described as a state-specific promotional exception rather than a core color token.
