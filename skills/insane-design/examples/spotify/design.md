---
schema_version: 3.2
slug: spotify
service_name: Spotify
site_url: https://spotify.com
fetched_at: 2026-05-03
default_theme: dark
brand_color: "#1ED760"
primary_font: SpotifyMixUI
font_weight_normal: 400
token_prefix: encore

bold_direction: Streaming Utility
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: other
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "Encore CSS variables, SpotifyMix font loading, button action tokens, plan-card component tokens, and consistent dark-theme semantic aliases are present in the captured CSS."

colors:
  spotify-green: "#1ED760"
  green-hover: "#3BE477"
  green-press: "#1ABC54"
  surface-black: "#000000"
  surface-card: "#1F1F1F"
  surface-deep: "#121212"
  text-primary: "#FFFFFF"
  text-secondary: "#B3B3B3"
  text-on-light: "#000000"
  plan-pink: "#FFD2D7"
  plan-mint: "#96F0B6"
  plan-blue: "#C8E0FC"
typography:
  display: SpotifyMixUITitle
  body: SpotifyMixUI
  ladder:
    - { token: marginal, size: "0.625rem-0.75rem", weight: 400 }
    - { token: body, size: "1rem", weight: 400 }
    - { token: body-bold, size: "1rem", weight: 700 }
    - { token: large, size: "1.25rem", weight: 700 }
    - { token: display-xl, size: "3rem desktop / 2rem mobile", weight: 900 }
  weights_used: [100, 400, 700, 800, 900]
  weights_absent: [500, 600]
components:
  button-primary-green: { bg: "{colors.spotify-green}", hover: "{colors.green-hover}", press: "{colors.green-press}", radius: "9999px", hover_scale: "1.04" }
  button-light-pill: { bg: "{colors.text-primary}", fg: "{colors.text-on-light}", radius: "9999px" }
  premium-plan-card: { bg: "{colors.surface-card}", radius: "24px", shadow: "0 4px 20px rgba(0,0,0,.25)" }
  top-search-pill: { bg: "#1F1F1F", fg: "{colors.text-secondary}", radius: "9999px" }
---

# DESIGN.md — Spotify

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Spotify's captured surface is not a polished marketing postcard. It is a dark listening cockpit: dense, black, rounded, and designed to make album art feel like the only true color in the room. The UI chrome recedes into #000000 (`{colors.surface-black}`), #121212 (`{colors.surface-deep}`), and #1F1F1F (`{colors.surface-card}`); imagery and the single green action system do the emotional work. It behaves like a recording studio after the overhead lights are cut: walls still exist, but the eye only catches illuminated controls, cover art, and the one live signal.

The brand color is exact and narrow: #1ED760 (`{colors.spotify-green}`). It is not a general wash across the page. It appears as the canonical Premium CTA, plan-standard marker, selected border/checkmark, and key action state. The system protects this green by surrounding it with black, white, and muted gray rather than inventing a second brand family. No second brand color enters the booth; pink, mint, blue, and yellow are plan labels, not a rival identity.

Typography is utility with a stage voice. Body text sits in SpotifyMixUI at 400/700, while hero or promotional display moves to SpotifyMixUITitle/Variable with heavy 900 weight and even `font-stretch: 156.25%` in the captured Premium hero HTML. The result is not delicate editorial type; it is compressed, confident signage inside a player shell, closer to a venue marquee over a queue of tracks than to magazine typography.

The craft is in the product motion rather than decorative layout. Buttons are pill forms with a precise `--encore-button-hover-scale: 1.04`, active states snap back to scale 1, and surfaces use hairline separation, rounded cards, and strong image crops. Spotify does not decorate the frame; it lets rows of square covers and circular artist portraits create rhythm. The page is less "website" than turntable cabinet: the furniture stays matte black, while the records provide the color.

Premium sections add a second, more cinematic layer without abandoning the shell. The scrolling hero's fixed `100vh` video/mask plane works like a stage scrim in a dark venue: motion sits behind the copy, but the black mask keeps the scene inside Spotify's room. Even plan cards are not paper pricing sheets; with `24px` radius, `48px 24px 24px` padding, and `0 4px 20px rgba(0,0,0,.25)`, they feel like thick product blocks pulled from the same audio-console material.

### Key Characteristics

- Dark-first shell with #000000 and #121212 as the main environment.
- One chromatic brand anchor: #1ED760 green for action and selection.
- White text is dominant, with #B3B3B3 for secondary metadata.
- Album covers and artist portraits are the real color field.
- Black chrome acts like a studio booth: present, useful, and deliberately unshowy.
- Large rounded controls: 9999px pills for primary buttons and search surfaces.
- Component hover is physical: `scale(1.04)` on buttons, not a color-only state.
- Cards are practical, dark, and dense; plan cards use 24px radius and a heavy shadow.
- Typography jumps from 1rem utility body to 3rem/900 promotional display.
- Spacing is an 8/12/16/20/24/32/48/64 style Encore ladder.
- Premium hero motion is masked and theatrical, but still anchored to the dark player environment.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Streaming Utility
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **dark player shell with one electric green action language**으로 기억된다.
> **Code Complexity**: high — Encore tokens, responsive token branches, masked scrolling hero CSS, image-heavy shelves, and animated button states all need coordinated implementation.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Spotify처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "SpotifyMixUI", "CircularSp", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --sp-bg: #000000; --sp-surface: #121212; --sp-card: #1F1F1F; --sp-fg: #FFFFFF; }
body { background: var(--sp-bg); color: var(--sp-fg); }

/* 3. 브랜드 컬러 */
:root { --sp-green: #1ED760; --sp-green-hover: #3BE477; --sp-green-press: #1ABC54; }
```

**절대 하지 말아야 할 것 하나**: Spotify를 초록색 배경 사이트로 만들지 말 것. #1ED760은 전체 배경이 아니라 CTA, selected, checkmark, plan-standard 같은 좁은 액션 표식이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://spotify.com` |
| Fetched | 2026-05-03 |
| Extractor | reused existing phase1 artifacts from `insane-design/spotify/` |
| HTML size | 158,836 bytes |
| CSS files | 6 CSS files plus `_urls.txt`, 635,514 CSS bytes excluding `_urls.txt` |
| Token prefix | `encore` plus local plan-card variables |
| Method | Existing CSS + phase1 JSON + screenshot interpretation; no fresh full-site crawl |
| Screenshot | `insane-design/spotify/screenshots/hero-cropped.png` |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js/Svelte-hybrid rendered surface. HTML includes `__next`, `data-sentry-source-file`, Svelte-scoped masthead classes, and React-style component names for Premium sections.
- **Design system**: Spotify Encore-style token layer — prefix `encore`, plus local variables such as `--color-spotify-green`, `--card-border-radius`, and `--card-padding`.
- **CSS architecture**:
  ```text
  core      (--background-*, --text-*, --essential-*)     semantic dark theme aliases
  encore    (--encore-spacing-*, --encore-text-size-*)     platform scale tokens
  action    (--encore-button-*)                            button-specific behavior tokens
  component (--card-*, --color-plan-*)                     plan/card local component API
  ```
- **Class naming**: Mixed scoped hashes and BEM-ish component names: `.e-1050-button-primary`, `.button-primary__inner`, `.ScrollingHero_container__Vajti`, `.PremiumLiteCard_premiumLiteCard__u5rVj`.
- **Default theme**: dark; captured CSS uses `.encore-dark-theme` and primary text #FFFFFF.
- **Font loading**: `@font-face` from `https://encore.scdn.co/fonts/`, `font-display: swap`, with SpotifyMixUI, SpotifyMixUITitle, CircularSp, and script-specific CircularSp subsets.
- **Canonical anchor**: Green CTA/button states and dark app shell. The screenshot shows the player shell; the HTML title and hero sections show Spotify Premium.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `SpotifyMixUITitle` / `SpotifyMixUITitleVariable` (Spotify proprietary web font)
- **Body font**: `SpotifyMixUI`, then `CircularSp`, `Helvetica`, `Arial`, `sans-serif`
- **Script fallback fonts**: `CircularSp-Arab`, `CircularSp-Cyrl`, `CircularSp-Deva`, `CircularSp-Grek`, `CircularSp-Hebr`
- **Weight normal / bold**: `400` / `700`; promotional display reaches `800` and `900`

```css
:root {
  --encore-font-family: "SpotifyMixUI", "CircularSp", Helvetica, Arial, sans-serif;
  --encore-font-family-title: "SpotifyMixUITitle", "SpotifyMixUI", Helvetica, Arial, sans-serif;
  --encore-font-weight-normal: 400;
  --encore-font-weight-bold: 700;
  --encore-font-weight-black: 900;
}

body,
button,
input,
textarea {
  font-family: var(--encore-font-family);
}
```

### Note on Font Substitutes

- **SpotifyMixUI unavailable** — use **Inter** only as a mechanical fallback, not as the aesthetic target. Set body weight to 400, labels/buttons to 700, and avoid 500/600 as the default middle ground.
- **SpotifyMixUITitle unavailable** — use **Inter Tight** or **Archivo** at 800/900 for large display. The Premium hero used `font-stretch: 156.25%`; if the substitute has no width axis, increase size slightly and keep line-height tight rather than using letter-spacing tricks.
- **CircularSp fallback** — Helvetica/Arial is already present in the captured stack. Keep it for parity with the actual fallback path.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `--encore-text-size-smaller-3` | `0.625rem` desktop / `0.5625rem` mobile | 400 | N/A | 0 |
| `--encore-text-size-smaller-2` | `0.75rem` desktop / `0.6875rem` mobile | 400/700 | N/A | 0 |
| `--encore-text-size-smaller` | `0.875rem` desktop / `0.8125rem` mobile | 400/700 | N/A | 0 |
| `--encore-text-size-base` | `1rem` | 400/700 | N/A | 0 |
| `--encore-text-size-large` | `1.25rem` desktop / `1.125rem` mobile | 700 | N/A | 0 |
| `--encore-text-size-larger` | `1.5rem` desktop / `1.25rem` mobile | 700/800 | N/A | 0 |
| `--encore-text-size-larger-2` | `2rem` desktop / `1.5rem` mobile | 800/900 | N/A | 0 |
| `--encore-text-size-larger-3` | `3rem` desktop / `2rem` mobile | 900 | N/A | 0 |
| `--encore-text-size-larger-4` | N/A desktop from snippet / `2.5rem` mobile | 900 | N/A | 0 |
| `--encore-text-size-larger-5` | N/A desktop from snippet / `3rem` mobile | 900 | N/A | 0 |

> ⚠️ The extracted typography script found no single complete scale object, but CSS snippets and inline hero styles expose the Encore text-size ladder and actual weights.

### Principles

1. Body is utility-first: `1rem` and weight 400 carry the everyday player/search/list surface.
2. Weight 700 is the main emphasis weight; do not replace it with 600 just because most SaaS sites do.
3. Promotional display uses heavy 900, not a gentle 600/700 editorial headline.
4. SpotifyMixUI is multilingual and operational; the stack carries Arabic, Cyrillic, Devanagari, Greek, and Hebrew subsets rather than a single Latin-only webfont.
5. Letter-spacing is not the signature move. Density comes from font family, weight, crop, and spacing.
6. Weight 500 is effectively absent in the captured extraction; using 500 everywhere makes the UI feel less Spotify.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (4 observed action steps)

| Token | Hex |
|---|---|
| `--color-spotify-green` | `#1ED760` |
| primary hover observed in `button-primary` | `#3BE477` |
| primary active observed in `button-primary` | `#1ABC54` |
| Premium hero inline hover/press family | `#2DE26D`, `#43E57D` |

### 06-2. Brand Dark Variant

> N/A — the captured system keeps the brand green stable across dark surfaces rather than defining a separate dark-mode green ramp.

### 06-3. Neutral Ramp

| Step | Light / Text | Dark / Surface |
|---|---|---|
| foreground primary | `#FFFFFF` | `#000000` |
| surface deep | N/A | `#121212` |
| surface card | N/A | `#1F1F1F` |
| badge/elevated neutral | N/A | `#2A2A2A` |
| secondary text | `#B3B3B3` | `#343434` |
| subdued legacy gray | `#919496` | `#141414` |
| light UI chip | `#F0F0F0` | N/A |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Standard / Spotify Green | plan-standard, CTA, checkmark | `#1ED760` |
| Pink plan/accent | plan color | `#FFD2D7` |
| Mint plan/accent | premium-basic | `#96F0B6` |
| Lite blue | plan-lite | `#C8E0FC` |
| Platinum yellow | plan-platinum | `#F6F609` |
| Warning/orange | support accent | `#FFA42B` |
| Negative/red | error/promo accent | `#E91429` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--color-spotify-green` | `#1ED760` | canonical brand/action |
| `--color-text-primary` | `#FFFFFF` | primary dark-theme text |
| `--color-text-secondary` | `#B3B3B3` | metadata and muted text |
| `--color-text-on-light` | `#000000` | green/white/light-pill text |
| `--color-bg-card` | `#1F1F1F` | premium plan cards and panels |
| `--color-bg-badge` | `#2A2A2A` | dark badges |
| `--color-border-default` | `#1F1F1F` | plan table borders |
| `--color-border-selected` | `#1ED760` | selected plan/table state |
| `--color-checkmark` | `#1ED760` | positive feature marks |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--background-base` | `rgba(0,0,0,.54)` in resolved sample | dark overlay/elevated base |
| `--background-highlight` | `rgba(0,0,0,.58)` | hover/highlight overlay |
| `--background-press` | `rgba(0,0,0,.68)` | pressed overlay |
| `--text-base` | `#fff` | primary dark text |
| `--text-subdued` | `#fff` in sample, secondary variants elsewhere | subdued text semantic |
| `--essential-base` | `#fff` | icon/essential foreground |
| `--decorative-subdued` | `hsla(0,0%,100%,.13)` | subtle dividers/chrome |
| `--encore-button-hover-scale` | `1.04` | button interaction behavior |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---|---|
| neutral/text | `#FFFFFF` | 510 |
| neutral/surface/text-on-light | `#000000` | 454 |
| Spotify Green | `#1ED760` | 81 |
| plan pink | `#FFD2D7` | 51 |
| plan mint | `#96F0B6` | 48 |
| plan blue | `#C8E0FC` | 44 |
| deep blue accent | `#052A56` | 40 |
| deep green accent | `#073116` | 40 |

### Color Stories
<!-- §06-8 -->

**`{colors.text-primary}` (#FFFFFF)** — White is the real dominant foreground. It gives the black player shell enough contrast to keep album art readable and makes navigation labels, list titles, and CTA text instantly scannable.

**`{colors.surface-black}` (#000000)** — Black is not a decorative luxury background here; it is the utility floor of the player. It lets cover art and plan accents become the variable color system.

**`{colors.spotify-green}` (#1ED760)** — The only brand action color. It marks Premium CTAs, selected plan states, checkmarks, and canonical Spotify ownership; it should be used sparingly and never diluted into a general green theme.

**`{colors.plan-pink}` (#FFD2D7)** — A plan/accent color, not the brand. Use it only as a product-tier or campaign panel color when the UI needs secondary categorization.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--encore-spacing-tighter-5` | `2px` | micro alignment |
| `--encore-spacing-tighter-4` | `4px` | tiny icon/text offsets |
| `--encore-spacing-tighter-3` | `6px` | compact inline gaps |
| `--encore-spacing-tighter-2` | `8px` | dense control spacing |
| `--encore-spacing-tighter` | `12px` | compact component padding |
| `--encore-spacing-base` | `16px` | default component unit |
| `--encore-spacing-looser` | `20px` | button/icon offset |
| `--encore-spacing-looser-2` | `24px` | card/chunk padding |
| `--encore-spacing-looser-3` | `32px` | sidebar/mobile nav padding |
| `--encore-spacing-looser-4` | `40px` | section chunk |
| `--encore-spacing-looser-5` | `48px` | large card padding |
| `--encore-spacing-looser-6` | `64px` | broad section breathing |

**주요 alias**:
- `--encore-button-icon-offset` → `--encore-spacing-tighter` (12px)
- `--encore-button-icon-padding` → `--encore-spacing-looser` (20px)
- `--card-padding` → `48px 24px 24px`
- `--card-padding-mobile` → `40px 24px 24px`

### Whitespace Philosophy

Spotify's spacing is compact where the product behaves like a player and generous where the page sells Premium. The screenshot shell uses tight 8-16px rhythms around shelves and controls, while Premium plan cards jump to 40-48px top padding and 24px horizontal padding.

The system is not airy minimalism. It is dense browsing with controlled pockets of breath: a sidebar card can sit close to another card, but every clickable pill keeps a large tactile hit area.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| `--encore-corner-radius-smaller` | `2px` | minor UI corners |
| `--encore-corner-radius-base` | `4px` | contextual banners |
| `--encore-corner-radius-larger` | `6px` | small panels |
| `--encore-corner-radius-larger-2` | `8px` | overlays |
| `--encore-corner-radius-larger-3` | `16px` | larger panels |
| `--encore-border-radius-rounded` | `9999px` | pills, primary buttons, search |
| `--card-border-radius` | `24px` | Premium plan cards |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| overlay | `0 4px 12px 0 rgba(0,0,0,.3)` | Encore overlays/popovers |
| plan card | `0 4px 20px rgba(0,0,0,.25)` | Premium plan card depth |
| focus | `0 3px 0 0` | focus box-shadow token |

Spotify uses shadows as dark-surface separation, not soft lifestyle depth. The strongest depth belongs to cards and overlays; ordinary shelves rely more on background contrast and imagery.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `--encore-button-hover-scale` | `1.04` | hover lift/physical affordance |
| `--encore-productive-enter` | `var(--encore-short-1) var(--encore-productive-decelerate)` | productive enter transitions |
| `--encore-productive-exit` | `var(--encore-shortest-4) var(--encore-productive-accelerate)` | productive exit transitions |
| primary button hover | background + transform | green CTA interaction |
| primary button active | `transform: scale(1)` | snap back on press |

Motion is functional and tactile. The key interaction is the 1.04 hover scale on buttons, guarded by `prefers-reduced-motion: no-preference`.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: player screenshot uses a viewport-filling app shell; Premium plan cards include fixed `420px` desktop card widths.
- **Grid type**: Flexbox-heavy rows and shelves, with card grids/plan tables in Premium sections.
- **Column count**: observed player shelf behaves as horizontal carousel; Premium card width suggests 2-3 cards depending on viewport.
- **Gutter**: 16-24px for cards and shelves; dense nav/search gaps.

### Hero
- **🆕 Pattern Summary**: `150vh scrolling hero + fixed 100vh video/mask layer + heavy 900 title + green pill CTA`.
- Layout: Premium HTML exposes a `ScrollingHero_container__Vajti` with content over a fixed video/mask layer; screenshot capture shows a logged-out player shell instead.
- Background: dark base, `var(--background-base)`, with black masked video area in the Premium hero CSS.
- **🆕 Background Treatment**: `fixed-video-mask` — `.ScrollingHero_videoContainer__RMUh6` is fixed at 100vh, and `.ScrollingHero_mask__YCnyA` uses mask-image/mask-composite over black.
- H1: `--encore-text-size-larger-5` / weight `900` / tracking `0`, with `font-stretch:156.25%` in inline hero style.
- Max-width: not reliably extracted; hero content is centered within full-width sections.

### Section Rhythm

```css
section {
  padding: 64px 16px; /* broad Premium sections inferred from Encore/ComparisonTable */
}

.ComparisonTable_wrapper__n6PFJ {
  padding: 120px 16px 48px;
}
```

### Card Patterns
- **Card background**: `#1F1F1F`
- **Card border**: default border `#1F1F1F`; selected border uses `#1ED760`
- **Card radius**: 24px for Premium plan cards; 8-16px for smaller UI panels
- **Card padding**: `40px 24px 24px` mobile, `48px 24px 24px` desktop
- **Card shadow**: `0 4px 20px rgba(0,0,0,.25)`

### Navigation Structure
- **Type**: fixed masthead in Premium HTML; player screenshot uses top app rail with home/search and right auth/app controls.
- **Position**: `.mh-fixed` for masthead; player top nav is visually fixed within app shell.
- **Height**: approximately 64px visual shell in screenshot; Encore control base is 48px.
- **Background**: #000000 / #121212 dark surfaces.
- **Border**: minimal; separation comes from rounded dark containers and contrast.

### Content Width
- **Prose max-width**: not directly measured.
- **Container max-width**: app shell fills viewport; Premium cards fixed at 420px on tablet/desktop snippets.
- **Sidebar width**: captured player sidebar is roughly 294px; Encore has `--encore-sidebar-base-width:200px` for system sidebars.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `max-width: 767px` | smaller text ladder, compact layout margins, overflow buttons hidden |
| Tablet | `min-width: 768px` | desktop text ladder begins, dialogs/card dimensions increase |
| Desktop | `min-width: 1024px` | scrolling hero mask sizing changes |
| Wide | `min-width: 1200px` | Premium cards expand to full grid allocation in snippets |

### Touch Targets
- **Minimum tap size**: Encore control base is `48px`; smaller is `32px`, larger is `56px`.
- **Button height (mobile)**: implied by `--encore-control-size-base:48px`.
- **Input height (mobile)**: search pill in screenshot visually matches large control height around 48px.

### Collapsing Strategy
- **Navigation**: Premium masthead exposes mobile menu button and mobile CTA.
- **Grid columns**: plan cards move from full-width mobile to fixed 420px cards at `min-width:768px`.
- **Sidebar**: player shell sidebar likely collapses/changes outside captured desktop viewport; not directly measured.
- **Hero layout**: hero mask changes at `min-width:1024px`; text scale changes at 767/768 boundary.

### Image Behavior
- **Strategy**: album art square crops; artist images circular; Premium hero video uses `object-fit: cover`.
- **Max-width**: media containers fill shelf/card slots.
- **Aspect ratio handling**: square album covers, circular artist portraits, fixed full-viewport video background.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary green pill**

```html
<a class="e-1050-focus-border e-1050-button-primary e-1050-button">
  <span class="e-1050-button-primary__inner">Try 1 month for $0</span>
</a>
```

| Property | Value |
|---|---|
| bg | `#1ED760` |
| hover bg | `#3BE477` or Premium inline `#2DE26D` |
| active/press bg | `#1ABC54` or Premium inline `#43E57D` |
| text | `#000000` |
| radius | `9999px` |
| hover transform | `scale(1.04)` |
| disabled | opacity `.3`, transform scale 1 |

**Light auth/search pill**

| Property | Value |
|---|---|
| bg | `#FFFFFF` |
| text | `#000000` |
| radius | `9999px` |
| role | Log in, Create playlist, Browse podcasts, sign-up CTA in capture |

### Badges

| Property | Value |
|---|---|
| bg | `#2A2A2A` / `#1A1A1A` |
| text | `#FFFFFF` |
| radius | likely pill or small rounded token |
| usage | Premium plan labels, compact metadata |

### Cards & Containers

**Player sidebar prompt card**

| Property | Value |
|---|---|
| bg | dark elevated panel near `#1F1F1F` |
| radius | 8px visual |
| padding | 16-20px visual |
| shadow | none; separation through contrast |

**Premium plan card**

| Property | Value |
|---|---|
| bg | `#1F1F1F` |
| radius | `24px` |
| padding | `40px 24px 24px` mobile, `48px 24px 24px` desktop |
| shadow | `0 4px 20px rgba(0,0,0,.25)` |
| width | `420px` from tablet breakpoint |

### Navigation

| Property | Value |
|---|---|
| masthead fg | `#FFFFFF` |
| nav bg | dark/black |
| logo | white Spotify glyph on black |
| links | white/secondary gray, bold utility labels |
| mobile | hamburger with CTA retained |
| player top rail | icon buttons + large rounded search pill |

### Inputs & Forms

**Search pill**

| Property | Value |
|---|---|
| bg | `#1F1F1F` visual |
| text | `#B3B3B3` placeholder |
| radius | `9999px` |
| height | around 48px |
| icon | search at left, secondary action icon at right |
| border | none visible; dark surface contrast |

### Hero Section

| Property | Value |
|---|---|
| container | `.ScrollingHero_container__Vajti` |
| min-height | `150vh` |
| video layer | fixed, `100vh`, `object-fit: cover` |
| mask | black background with CSS mask-image and mask-composite |
| title | `--encore-text-size-larger-5`, 900, `font-stretch:156.25%` |
| CTA | green pill primary |

### 13-2. Named Variants

**button-primary-green**

| Property | Value |
|---|---|
| default | `#1ED760` bg, `#000000` text |
| hover | `#3BE477`, transform `scale(1.04)` |
| active | `#1ABC54`, transform `scale(1)` |
| focus | Encore focus border/box-shadow token |

**button-light-pill**

| Property | Value |
|---|---|
| default | `#FFFFFF` bg, `#000000` text |
| usage | auth, playlist creation, podcast browse, sign-up free |
| radius | `9999px` |

**premium-plan-card**

| Property | Value |
|---|---|
| bg | `#1F1F1F` |
| radius | `24px` |
| padding | `48px 24px 24px` desktop |
| shadow | `0 4px 20px rgba(0,0,0,.25)` |

**top-search-pill**

| Property | Value |
|---|---|
| bg | dark elevated search field |
| fg | `#B3B3B3` placeholder, `#FFFFFF` active text |
| shape | 9999px rounded capsule |

### 13-3. Signature Micro-Specs
<!-- §13-3 -->

#### encore-physical-pill-hover

```yaml
encore-physical-pill-hover:
  description: "Spotify's button affordance is a tiny physical expansion, not a shadow lift."
  technique: "--encore-button-hover-scale: 1.04; hover transform: scale(1.04); active transform: scale(1); gated by prefers-reduced-motion: no-preference"
  applied_to: ["{components.button-primary-green}", "primary and tertiary Encore buttons"]
  visual_signature: "Pill controls feel tactile and playable without adding ornamental shadow choreography."
```

#### dark-shell-image-color-field

```yaml
dark-shell-image-color-field:
  description: "The chrome stays nearly monochrome so album covers, artist portraits, and plan accents become the color system."
  technique: "surface stack #000000 / #121212 / #1F1F1F with #FFFFFF primary text, #B3B3B3 metadata, square album crops, and circular artist crops"
  applied_to: ["player home shelves", "library prompt area", "artist rows"]
  visual_signature: "The product frame reads as matte-black audio equipment while content supplies the saturation."
```

#### premium-scrolling-video-mask

```yaml
premium-scrolling-video-mask:
  description: "Premium hero uses a fixed video plane and black mask instead of a static marketing hero image."
  technique: ".ScrollingHero_container__Vajti min-height: 150vh; video layer position: fixed; height: 100vh; object-fit: cover; mask-image / mask-composite: exclude"
  applied_to: [".ScrollingHero_container__Vajti", ".ScrollingHero_videoContainer__RMUh6", ".ScrollingHero_mask__YCnyA"]
  visual_signature: "Motion sits behind the headline like a dark venue scrim, keeping spectacle inside the Spotify shell."
```

#### plan-card-heavy-chassis

```yaml
plan-card-heavy-chassis:
  description: "Premium plan cards are thick dark product blocks, not light SaaS pricing sheets."
  technique: "background #1F1F1F; border-radius: 24px; padding: 48px 24px 24px desktop / 40px 24px 24px mobile; box-shadow: 0 4px 20px rgba(0,0,0,.25); width: 420px at tablet breakpoint"
  applied_to: ["{components.premium-plan-card}", "Premium plan cards"]
  visual_signature: "Subscription offers feel like hardware tiles lifted from the same dark player material."
```

#### single-green-action-contract

```yaml
single-green-action-contract:
  description: "Spotify green is a narrow action contract, not a decorative atmosphere."
  technique: "#1ED760 across primary CTA, selected border, checkmark, and plan-standard markers; hover #3BE477; press #1ABC54"
  applied_to: ["{components.button-primary-green}", "plan comparison", "feature confirmation"]
  visual_signature: "One electric green means go, selected, or Spotify-owned; there is no second brand color."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Big, direct, benefit-first, occasionally hyperbolic | "The ultimate home for music" |
| Primary CTA | Price/trial concrete, action immediate | "Try 1 month for $0" |
| Secondary CTA | Utility verbs, no elaborate phrasing | "Create playlist", "Browse podcasts" |
| Subheading | Plain product promise | "Spotify Premium is a digital music service..." |
| Tone | confident, consumer-simple, not enterprise formal | "It's easy, we'll help you" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Spotify — copy into your root stylesheet */
:root {
  /* Fonts */
  --sp-font-family: "SpotifyMixUI", "CircularSp", Helvetica, Arial, sans-serif;
  --sp-font-family-title: "SpotifyMixUITitle", "SpotifyMixUI", Helvetica, Arial, sans-serif;
  --sp-font-weight-normal: 400;
  --sp-font-weight-bold: 700;
  --sp-font-weight-black: 900;

  /* Brand */
  --sp-color-brand-500: #1ED760;
  --sp-color-brand-hover: #3BE477;
  --sp-color-brand-press: #1ABC54;

  /* Surfaces */
  --sp-bg-page: #000000;
  --sp-bg-surface: #121212;
  --sp-bg-card: #1F1F1F;
  --sp-bg-badge: #2A2A2A;
  --sp-text: #FFFFFF;
  --sp-text-muted: #B3B3B3;
  --sp-text-on-light: #000000;

  /* Key spacing */
  --sp-space-xs: 8px;
  --sp-space-sm: 12px;
  --sp-space-md: 16px;
  --sp-space-lg: 24px;
  --sp-space-xl: 48px;
  --sp-space-2xl: 64px;

  /* Radius */
  --sp-radius-sm: 4px;
  --sp-radius-md: 8px;
  --sp-radius-lg: 16px;
  --sp-radius-card: 24px;
  --sp-radius-pill: 9999px;

  /* Motion */
  --sp-button-hover-scale: 1.04;
}

.spotify-button-primary {
  border: 0;
  border-radius: var(--sp-radius-pill);
  background: var(--sp-color-brand-500);
  color: var(--sp-text-on-light);
  font: 700 1rem/1 var(--sp-font-family);
  padding: 14px 28px;
  transition: background-color 0.15s ease, transform 0.15s ease;
}

@media (prefers-reduced-motion: no-preference) {
  .spotify-button-primary:hover {
    background: var(--sp-color-brand-hover);
    transform: scale(var(--sp-button-hover-scale));
  }
}

.spotify-button-primary:active {
  background: var(--sp-color-brand-press);
  transform: scale(1);
}

.spotify-card {
  background: var(--sp-bg-card);
  color: var(--sp-text);
  border-radius: var(--sp-radius-card);
  padding: 48px 24px 24px;
  box-shadow: 0 4px 20px rgba(0,0,0,.25);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Spotify-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        spotify: {
          green: '#1ED760',
          hover: '#3BE477',
          press: '#1ABC54',
          black: '#000000',
          deep: '#121212',
          card: '#1F1F1F',
          badge: '#2A2A2A',
          white: '#FFFFFF',
          muted: '#B3B3B3',
          pink: '#FFD2D7',
          mint: '#96F0B6',
          blue: '#C8E0FC',
        },
      },
      fontFamily: {
        sans: ['SpotifyMixUI', 'CircularSp', 'Helvetica', 'Arial', 'sans-serif'],
        display: ['SpotifyMixUITitle', 'SpotifyMixUI', 'Helvetica', 'Arial', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        bold: '700',
        black: '900',
      },
      borderRadius: {
        spotify: '24px',
        pill: '9999px',
      },
      boxShadow: {
        'spotify-card': '0 4px 20px rgba(0,0,0,.25)',
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
| Brand primary | `{colors.spotify-green}` | `#1ED760` |
| Brand hover | `{colors.green-hover}` | `#3BE477` |
| Background | `{colors.surface-black}` | `#000000` |
| Surface | `{colors.surface-deep}` | `#121212` |
| Card | `{colors.surface-card}` | `#1F1F1F` |
| Text primary | `{colors.text-primary}` | `#FFFFFF` |
| Text muted | `{colors.text-secondary}` | `#B3B3B3` |
| Text on light | `{colors.text-on-light}` | `#000000` |
| Plan accent | `{colors.plan-pink}` | `#FFD2D7` |

### Example Component Prompts

#### Hero Section

```text
Spotify 스타일의 dark hero를 만들어줘.
- 배경: #000000 / #121212 dark shell
- H1: SpotifyMixUITitle, 3rem 이상, weight 900, letter-spacing 0
- 서브텍스트: #B3B3B3 또는 #FFFFFF with opacity, 1rem
- CTA 버튼: 배경 #1ED760, 텍스트 #000000, radius 9999px, hover scale 1.04
- 미디어: 앨범 커버나 영상이 실제 색상 필드가 되게 하고, UI chrome은 거의 monochrome으로 유지
```

#### Card Component

```text
Spotify Premium plan card 스타일로 만들어줘.
- 배경: #1F1F1F, 텍스트 #FFFFFF, secondary #B3B3B3
- radius: 24px
- padding: desktop 48px 24px 24px, mobile 40px 24px 24px
- shadow: 0 4px 20px rgba(0,0,0,.25)
- 선택 상태: border/checkmark에 #1ED760만 사용
```

#### Badge

```text
Spotify dark badge를 만들어줘.
- bg #2A2A2A 또는 #1A1A1A
- text #FFFFFF
- radius는 pill 또는 8px 이내
- 브랜드 green을 badge 배경으로 남발하지 말고 plan/status에만 제한
```

#### Navigation

```text
Spotify top navigation을 만들어줘.
- 배경 #000000, controls #1F1F1F, text #FFFFFF / #B3B3B3
- 왼쪽에는 white glyph/icon, 중앙에는 9999px search pill
- search placeholder는 #B3B3B3, active text는 #FFFFFF
- 오른쪽 auth CTA는 #FFFFFF pill with #000000 text
```

### Iteration Guide

- **색상 변경 시**: #1ED760은 CTA/selected/checkmark 전용으로 남긴다. 배경으로 확장하지 않는다.
- **폰트 변경 시**: SpotifyMixUI가 없으면 Inter를 쓰되 500/600 중간 weight를 기본값으로 만들지 않는다.
- **여백 조정 시**: 8/12/16/20/24/32/48/64 중심으로 조절한다.
- **새 컴포넌트 추가 시**: dark surface, white text, muted metadata, pill controls, image-driven color hierarchy를 유지한다.
- **모션 추가 시**: hover scale 1.04 이상으로 과장하지 않는다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#000000`, `#121212`, and `#1F1F1F` as the main surface stack.
- Use `#1ED760` for primary action, selected state, checkmark, and plan-standard markers.
- Keep buttons pill-shaped with `border-radius:9999px`.
- Use `scale(1.04)` for hover affordance when motion is allowed.
- Let album covers, artists, and plan art supply the page's broader color.
- Use SpotifyMixUI/CircularSp-style font stacks and strong 700/900 weights.
- Build dense shelves and side panels; avoid over-spaced SaaS marketing rhythm in player-like surfaces.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#000000` / `#121212` dark shell 사용.
- 본문 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — dark surface에서는 `#FFFFFF` 사용.
- primary CTA를 `#0D72EA` blue로 두지 말 것 — Spotify action은 `#1ED760` 사용.
- secondary text를 `#FFFFFF` full strength로만 두지 말 것 — metadata에는 `#B3B3B3` 사용.
- card background를 `#FFFFFF`로 두지 말 것 — Premium/player cards는 `#1F1F1F` 계열 사용.
- 버튼 radius를 `8px` 이하로 두지 말 것 — primary/button controls는 `9999px` pill 사용.
- body 기본 weight를 `500` 또는 `600`으로 두지 말 것 — captured system은 400/700 중심.
- hover를 box-shadow만으로 표현하지 말 것 — Encore signature는 `transform: scale(1.04)`.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second brand color: none. #1ED760 is the only real brand action color; pink, mint, blue, and yellow are plan/campaign accents.
- Light-page neutrality: absent in the captured shell. White appears as text or auth pills, not the environmental floor.
- Pastel SaaS gradients: none in the core shell. Plan colors exist as flat product-tier accents.
- Decorative border cards: minimal. Cards separate through dark surfaces, radius, and media, not ornate borders.
- Weight 500/600 defaulting: absent from extracted weights; 400, 700, 800, and 900 do the work.
- Over-explained hover states: no elaborate shadow choreography. The button scale is enough.
- Thin-outline primary buttons: never for main action. The CTA is filled green or filled white.
- Generic stock illustration: absent from the player shell; real album/artist art is the visual payload.
- Wide airy whitespace as identity: absent. Spotify compresses shelves and controls so browsing feels continuous.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **HTML/screenshot mismatch** — `index.html` identifies "Spotify Premium - Spotify (USA)" and contains Premium hero/plan sections, while the available screenshot shows a Spotify web-player home shell. This guide prioritizes CSS/phase1 tokens and calls out where evidence comes from each surface.
- **Single viewport screenshot** — visual interpretation is based on one 1280x800 cropped screenshot. Mobile player behavior was inferred from CSS breakpoints, not visually rechecked.
- **No fresh crawl by request** — existing phase1 artifacts were reused. Current live Spotify.com may differ from this cached capture.
- **Token extraction incomplete for typography** — `typography.json` reported an empty `scale`; text sizes were recovered from CSS snippets and inline hero styles.
- **CSS duplicated files** — the CSS folder contains repeated hash pairs (`00/03`, `01/04`, `02/05` pattern by size). Counts may double some frequency values.
- **Dark overlay aliases are contextual** — several resolved samples map to rgba overlays rather than simple hex. This guide uses those as behavioral aliases, not standalone brand colors.
- **Form validation states not surfaced** — search input visual state is observed, but error/loading/validation form states were not present in the captured surface.
- **Player internals not exhaustively mapped** — album row hover overlays, playback bar, queue, settings, and logged-in flows were not separately captured.
- **Motion curves partially observed** — button scale and productive enter/exit tokens were present, but scroll-triggered Premium hero JS behavior was not executed for timing analysis.
