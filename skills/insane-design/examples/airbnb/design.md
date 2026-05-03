---
schema_version: 3.2
slug: airbnb
service_name: Airbnb
site_url: https://airbnb.com
fetched_at: 2026-05-03T15:12:37+0900
default_theme: light
brand_color: "#FF385C"
primary_font: "Airbnb Cereal VF"
font_weight_normal: 400
token_prefix: palette

bold_direction: Marketplace Warmth
aesthetic_category: Refined Marketplace
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: commerce-marketplace
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "1554 custom properties, 919 resolved tokens, named palette/typography/spacing/radius/elevation systems, and repeated search/card/chip/navigation components."

colors:
  primary: "#FF385C"
  product-primary: "#E00B41"
  text-primary: "#222222"
  text-muted: "#6A6A6A"
  surface-base: "#FFFFFF"
  surface-soft: "#F7F7F7"
  border-primary: "#DDDDDD"
  border-soft: "#EBEBEB"
  success: "#008A05"
  error: "#C13515"
typography:
  display: "Airbnb Cereal VF"
  body: "Airbnb Cereal VF"
  ladder:
    - { token: special-display-72, size: "4.5rem", line_height: "4.625rem", weight: 600, tracking: "normal" }
    - { token: special-display-60, size: "3.75rem", line_height: "4.25rem", weight: 600, tracking: "normal" }
    - { token: special-display-48, size: "3rem", line_height: "3.375rem", weight: 600, tracking: "normal" }
    - { token: special-display-40, size: "2.5rem", line_height: "2.75rem", weight: 600, tracking: "normal" }
    - { token: title-32, size: "2rem", line_height: "2.25rem", weight: 600, tracking: "normal" }
    - { token: body-16, size: "1rem", line_height: "1.375rem", weight: 400, tracking: "normal" }
  weights_used: [400, 450, 500, 600, 700, 800]
  weights_absent: [300, 900]
components:
  button-primary: { bg: "{colors.primary}", fg: "#FFFFFF", radius: "8px", weight: 600 }
  search-orb: { bg: "{colors.primary}", fg: "#FFFFFF", radius: "50%", shadow: "none" }
  listing-card: { bg: "{colors.surface-base}", radius: "12px", gap: "12px", shadow: "none" }
  chip-selected: { bg: "{colors.text-primary}", fg: "#FFFFFF", radius: "999px" }
  modal-card: { bg: "{colors.surface-base}", radius: "20px", shadow: "0 6px 20px rgba(0,0,0,0.2)" }
---

# DESIGN.md - Airbnb

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Airbnb reads like a marketplace where host photography has taken full possession of the canvas. White walls, black room labels, soft grey floor lines, and one unmistakable Rausch signal at the place where the guest commits — the site has almost no interest in looking like a "website." Each listing slot is a boutique shelf where a home, cabin, room, or view occupies the frame for a few seconds before the user moves on.

The primary color is Rausch, `#FF385C` (`{colors.primary}`). It is not poured across the page; it appears like a concierge bell on a white desk. Search orb, primary CTA, selected or urgent moments, and brand memory get the color, while the rest of the interface stays in `#FFFFFF` (`{colors.surface-base}`), `#222222` (`{colors.text-primary}`), `#6A6A6A` (`{colors.text-muted}`), and thin `#DDDDDD` dividers. There is no second brand color in the core marketplace. Plus and Luxe have their own side rooms, but the main floor has one red-pink signal and a lot of air.

The neutral system is not decoration; it is scaffolding for other people's interiors. Airbnb keeps metadata compact while giving image cards enough editorial rhythm to be trusted. Listing photography is allowed to be messy, sunny, beige, blue, forested, or marble-heavy; the chrome refuses to add another mood. Shadow belongs to temporary UI and overlays, not to the listing grid.

The typography is Airbnb Cereal VF, with a practical marketplace ladder rather than a dramatic display one. Display sizes reach 72/74, but most operational surfaces live in 14/18, 16/20, 16/22, and 18/24. Weight 600 is the house emphasis, 500 is for dense labels, and 400 carries paragraphs. Letter-spacing stays `normal`, which makes the interface feel like travel logistics handled by a host, not luxury copy set by a fashion magazine.

Airbnb's signature craft is the split between airport-lounge calm and catalog-speed scanning. Search and section headers get 48-80px breathing room; listings collapse into fast grids with 8-16px internal gaps. The canvas breathes at the hero and footer edges, then packs the center with card inventory. The result is a marketplace that inhales before intent and exhales into comparison.

### Key Characteristics

- Rausch `#FF385C` is the single recognizable brand action color.
- Pure white `#FFFFFF` dominates the page so photography can own the mood.
- Primary text anchors at `#222222`, not black, giving the UI a softer consumer tone.
- Grey hierarchy is explicit: `#6A6A6A` muted text, `#DDDDDD` primary hairline, `#EBEBEB` softer division, `#F7F7F7` secondary surface.
- Airbnb Cereal VF carries both display and body; the design does not switch to a contrasting serif or editorial face.
- Radius ladder is rounded but not bubbly: 8px buttons, 12px common cards/inputs, 20-32px modals and large containers, 50% circular icon buttons.
- Elevation exists for overlays, popovers, and modals; listing cards stay visually flat so image grids remain calm.
- Breakpoints cluster around 744px, 1128px, and 1440px, matching a marketplace grid that must scale from phone to wide desktop.
- Search is the hero component: a white pill/surface plus a Rausch circular submit affordance.
- Motion is present in search/view transitions, but brand expression stays in layout and component states rather than animation spectacle.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Marketplace Warmth
> **Aesthetic Category**: Refined Marketplace
> **Signature Element**: 이 사이트는 **white marketplace surface with a Rausch search/action flare**으로 기억된다.
> **Code Complexity**: high — large token graph, responsive marketplace grids, search transitions, overlay elevation tiers, and many component-scoped variables.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Airbnb처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Font + weight */
body {
  font-family: "Airbnb Cereal VF", "Circular", -apple-system, BlinkMacSystemFont,
    "Roboto", "Helvetica Neue", sans-serif;
  font-weight: 400;
  letter-spacing: normal;
}

/* 2. Marketplace floor */
:root {
  --airbnb-bg: #FFFFFF;
  --airbnb-fg: #222222;
  --airbnb-muted: #6A6A6A;
  --airbnb-border: #DDDDDD;
}

/* 3. Rausch action only */
:root { --airbnb-rausch: #FF385C; }
.search-submit,
.primary-cta {
  background: var(--airbnb-rausch);
  color: #FFFFFF;
  font-weight: 600;
}
```

**절대 하지 말아야 할 것 하나**: `#FF385C`를 전체 배경/그라디언트 장식으로 깔지 말 것. Airbnb는 Rausch를 면이 아니라 액션 신호로 쓴다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://airbnb.com` |
| Fetched | 2026-05-03T15:12:37+0900 |
| Reused source | `insane-design/airbnb/phase1`, `css`, `index.html`, `screenshots` |
| Extractor | existing phase1 artifacts + CSS token inspection |
| HTML size | included in reused `index.html`; total HTML+CSS observed 2,295,325 bytes |
| CSS files | 1 external CSS: `client.81b4b87a9b.css` |
| CSS size | 1,705,530 characters |
| Custom properties | 1554 total vars, 919 resolved vars |
| Token prefix | `palette`, `typography`, `spacing`, `corner-radius`, `elevation` |
| Method | CSS custom properties, phase1 JSON, HTML metadata, and direct component-pattern interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Airbnb production web application; HTML includes generated atomic utility classes and hydrated app markup.
- **Design system**: Airbnb DLS-style token system using `--palette-*`, `--typography-*`, `--spacing-*`, `--corner-radius-*`, and `--elevation-*`.
- **CSS architecture**:
  ```text
  palette-*        raw and semantic color values
  typography-*     family, title/body/display sizes, weights, tracking
  spacing-*        macro and micro spacing ladders
  corner-radius-*  named radius tokens from 4px to 32px
  elevation-*      shadow and border recipes for overlays
  component vars   search, card, chip, navigation, input, profile, tab
  ```
- **Class naming**: generated atomic classes such as `atm_*`, plus component-scoped variables like `--card-container_box-shadow`, `--search-input_background`, and `--navigation-bar_min-height`.
- **Default theme**: light, with `#FFFFFF` page/surface base and `#222222` text.
- **Font loading**: custom variable family declaration for `'Airbnb Cereal VF','Circular',-apple-system,'BlinkMacSystemFont','Roboto','Helvetica Neue',sans-serif`.
- **Canonical anchor**: search bar + listings grid; the brand is most visible where a user commits intent.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Airbnb Cereal VF` (Airbnb brand font; not a normal open-source dependency)
- **Body font**: `Airbnb Cereal VF`
- **Fallbacks**: `Circular`, `-apple-system`, `BlinkMacSystemFont`, `Roboto`, `Helvetica Neue`, `sans-serif`
- **Code font**: `monospace` observed only as generic fallback
- **Weight normal / medium / semibold / bold**: `400` / `500` / `600` / `700`

```css
:root {
  --typography-font-family-cereal-font-family:
    'Airbnb Cereal VF','Circular',-apple-system,'BlinkMacSystemFont',
    'Roboto','Helvetica Neue',sans-serif;
  --typography-weight-book400: 400;
  --typography-weight-medium500: 500;
  --typography-weight-semibold600: 600;
  --typography-weight-bold700: 700;
}

body {
  font-family: var(--typography-font-family-cereal-font-family);
  font-weight: var(--typography-weight-book400);
}
```

### Note on Font Substitutes

- **Airbnb Cereal VF** is brand-owned. Use **Circular** where licensed; otherwise use `Inter` or `system-ui` only as a fallback, not as the design identity.
- If substituting with Inter, keep the same weight roles: body 400, label 500, title 600. Avoid Inter 700 for common headings; Airbnb's UI emphasis is firm but not heavy.
- Keep `letter-spacing: normal` for display and body. Do not add negative tracking to imitate Apple or editorial commerce sites.
- Inter tends to look narrower and more technical than Cereal. Compensate with slightly looser line-height on body rows: `16/20` can become `16/22` in dense listing metadata.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---|
| `--typography-special-display-medium_72_74` | `4.5rem` | 600 | `4.625rem` | normal |
| `--typography-special-display-medium_60_68` | `3.75rem` | 600 | `4.25rem` | normal |
| `--typography-special-display-medium_48_54` | `3rem` | 600 | `3.375rem` | normal |
| `--typography-special-display-medium_40_44` | `2.5rem` | 600 | `2.75rem` | normal |
| `--typography-titles-semibold_32_36` | `2rem` | 600 | `2.25rem` | normal |
| `--typography-titles-semibold_26_30` | `1.625rem` | 600 | `1.875rem` | normal |
| `--typography-titles-semibold_22_26` | `1.375rem` | 600 | `1.625rem` | normal |
| `--typography-titles-semibold_18_24` | `1.125rem` | 600 | `1.5rem` | normal |
| `--typography-titles-medium_16_20` | `1rem` | 500 | `1.25rem` | normal |
| `--typography-subtitles-book_16_22` | `1rem` | 400 | `1.375rem` | normal |
| `--typography-body-text_14_18` | `0.875rem` | 400 | `1.125rem` | normal |
| `--typography-body-text_12_16` | `0.75rem` | 400 | `1rem` | normal |

> ⚠️ Key insight: Airbnb's scale is utilitarian and tokenized. It does not rely on negative tracking, serif contrast, or extreme display weights.

### Principles

1. Display sizes are medium/semibold, not ultra-bold. The largest observed display tokens stay at weight 600.
2. Letter-spacing is intentionally `normal` across display, title, subtitle, and body tokens; Airbnb avoids optical-tight luxury styling.
3. Weight 500 is a label/navigation weight, while 600 is the title/action emphasis. Do not collapse both into one generic semibold.
4. Body line-height is compact but not cramped: `14/18`, `16/20`, and `16/22` support dense cards without making metadata feel like a table.
5. The custom font is part of the brand tone. Replacing it with bare `Arial` or default `system-ui` makes the interface colder and more enterprise.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp

| Token | Hex / Value |
|---|---|
| `--palette-rausch` | `#FF385C` |
| `--palette-product-rausch` | `#E00B41` |
| `--palette-rausch-gradient-linear-gradient` | `linear-gradient(to right,#E61E4D 0%,#E31C5F 50%,#D70466 100%)` |
| `--palette-rausch-gradient-radial-gradient` | `radial-gradient(circle at center,#FF385C 0%,#E61E4D 27.5%,#E31C5F 40%,#D70466 57.5%,#BD1E59 75%,#BD1E59 100%)` |

### 06-2. Premium / Secondary Brand Families

| Family | Token | Hex / Value |
|---|---|---|
| Plus | `--palette-plus` | `#92174D` |
| Plus gradient | `--palette-plus-gradient-linear-gradient` | `#BD1E59 -> #92174D -> #861453` |
| Luxe | `--palette-luxe` | `#460479` |
| Luxe gradient | `--palette-luxe-gradient-linear-gradient` | `#59086E -> #460479 -> #440589` |

### 06-3. Neutral Ramp

| Token | Hex | Role |
|---|---|---|
| `--palette-white` | `#FFFFFF` | base surface |
| `--palette-faint` | `#F7F7F7` | secondary/disabled/hover surface |
| `--palette-bebe` | `#EBEBEB` | soft division |
| `--palette-deco` | `#DDDDDD` | primary border/hairline |
| `--palette-bobo` | `#B0B0B0` | disabled/mid grey |
| `--palette-foggy` | `#6A6A6A` | muted text/icon |
| `--palette-hof` | `#222222` | primary text/inverse surface |
| `--palette-black` | `#000000` | inverse hover/deep black |

### 06-4. Accent Families

| Family | Token | Hex | Usage |
|---|---|---|---|
| Error / Arches | `--palette-arches` | `#C13515` | error/destructive |
| Error hover | `--palette-arches2` | `#B32505` | inverse error hover |
| Error surface | `--palette-arches12` | `#FFF8F6` | pale error bg |
| Success | `--palette-spruce` | `#008A05` | success/confirmation |
| Info | `--palette-mykonou5` | `#428BFF` | blue informational |
| Warning | `--palette-ondo` | `#E07912` | warning/accent |

### 06-5. Semantic

| Token | Hex / Value | Usage |
|---|---|---|
| `--palette-bg-primary` | `#FFFFFF` | main page/card surface |
| `--palette-bg-primary-hover` | `#F7F7F7` | hover/selected surface |
| `--palette-bg-primary-core` | `#FF385C` | primary brand surface |
| `--palette-bg-primary-inverse` | `#222222` | selected chip / inverse UI |
| `--palette-bg-secondary` | `#F7F7F7` | subtle grouped surface |
| `--palette-bg-secondary-core` | Rausch linear gradient | premium/action variation |
| `--palette-bg-tertiary` | `#B0B0B0` | disabled/tertiary fill |
| `--palette-text-primary` | `#222222` | main copy |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `{colors.primary}` | `#FF385C` | primary action and search signal |
| `{colors.surface-base}` | `#FFFFFF` | page and card background |
| `{colors.surface-soft}` | `#F7F7F7` | hover, disabled, grouped surfaces |
| `{colors.text-primary}` | `#222222` | titles, body, selected chip bg |
| `{colors.text-muted}` | `#6A6A6A` | secondary metadata |
| `{colors.border-primary}` | `#DDDDDD` | hairlines and input boundaries |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Hex | Frequency | Kind |
|---|---:|---|
| `#FFFFFF` | 71 | neutral/surface |
| `#313131` | 37 | dark neutral |
| `#222222` | 35 | primary text |
| `#000000` | 28 | deep neutral |
| `#FF385C` | 26 | brand |
| `#EFEFEF` | 26 | neutral |
| `#DDDDDD` | 24 | border |
| `#C13515` | 23 | error/accent |
| `#F7F7F7` | 21 | soft surface |
| `#D70466` | 21 | brand gradient stop |
| `#BD1E59` | 21 | plus/gradient stop |
| `#E31C5F` | 20 | brand gradient stop |

### 06-8. Color Stories

**`{colors.primary}` (`#FF385C`)** — Rausch, the single brand action color. It should appear in search submit buttons, primary CTAs, save/heart states, and focused brand moments; it should not become a decorative page wash.

**`{colors.surface-base}` (`#FFFFFF`)** — the marketplace floor. Airbnb uses white because the listings are already visually rich; chrome must stay quiet so photos can differentiate inventory.

**`{colors.text-primary}` (`#222222`)** — softer than black and warmer than slate. This is the default ink for titles, prices, selected labels, and inverse chips.

**`{colors.border-primary}` (`#DDDDDD`)** — the structural hairline. It replaces heavy panels and colored separators, especially around inputs, search surfaces, and quiet component boundaries.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--spacing-micro2px` | `2px` | tight card metadata offsets |
| `--spacing-micro4px` | `4px` | icon/text nudge, tiny gaps |
| `--spacing-micro8px` | `8px` | chip/button internal rhythm |
| `--spacing-micro12px` | `12px` | card content gap, input padding |
| `--spacing-micro16px` | `16px` | default card/sidebar spacing |
| `--spacing-micro24px` | `24px` | outer card spacing, dense section gutters |
| `--spacing-micro32px` | `32px` | large component gap |
| `--spacing-macro16px` | `16px` | small layout rhythm |
| `--spacing-macro24px` | `24px` | mobile section padding |
| `--spacing-macro32px` | `32px` | section spacing |
| `--spacing-macro40px` | `40px` | medium vertical bands |
| `--spacing-macro48px` | `48px` | header/editorial breathing |
| `--spacing-macro64px` | `64px` | major section rhythm |
| `--spacing-macro80px` | `80px` | hero/top-level breathing |

**주요 alias**:
- `micro16px` -> 16px, default card/sidebar spacing.
- `micro24px` -> 24px, roomy card outer spacing.
- `macro64px` -> 64px, editorial vertical breathing.

### Whitespace Philosophy

Airbnb alternates between two spatial modes: open intent and dense inventory. Search, header, and editorial moments use macro spacing in the 48-80px range to make the trip-planning action feel calm. Once the user enters listing territory, the grid compresses to 8-16px gaps so comparison becomes fast.

The whitespace is therefore not luxury emptiness. It is a funnel: breathe before choosing, then scan quickly after choosing. Avoid uniformly spacious layouts; they miss the marketplace rhythm.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `--corner-radius-tiny4px-border-radius` | `4px` | tiny controls, small states |
| `--corner-radius-small8px-border-radius` | `8px` | buttons, compact inputs |
| `--corner-radius-medium12px-border-radius` | `12px` | listing images/cards/input groups |
| `--corner-radius-large16px-border-radius` | `16px` | larger cards and containers |
| `--corner-radius-xlarge20px-border-radius` | `20px` | modal/card containers |
| `--corner-radius-xxlarge24px-border-radius` | `24px` | soft large surfaces |
| `--corner-radius-xxlarge28px-border-radius` | `28px` | large rounded panels |
| `--corner-radius-xxxlarge32px-border-radius` | `32px` | bottom sheets, big containers |
| direct value | `50%` | circular icon/search buttons |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `--elevation-elevation0-box-shadow` | `0px 0px 0px 1px #DDDDDD inset` | border-only inset surfaces |
| `--elevation-elevation1-box-shadow` | `0px 0px 0px 1px rgba(0,0,0,0.02),0px 2px 4px 0px rgba(0,0,0,0.16)` | low popover/card lift |
| `--elevation-elevation2-box-shadow` | `0px 0px 0px 1px rgba(0,0,0,0.02),0px 2px 6px 0px rgba(0,0,0,0.04),0px 4px 8px 0px rgba(0,0,0,0.10)` | floating card |
| `--elevation-elevation3-box-shadow` | `0px 0px 0px 1px rgba(0,0,0,0.02),0px 8px 24px 0px rgba(0,0,0,0.10)` | menu/modal |
| `--elevation-elevation4-box-shadow` | `0px 0px 0px 1px rgba(0,0,0,0.02),0px 4px 8px 0px rgba(0,0,0,0.08),0px 12px 30px 0px rgba(0,0,0,0.12)` | high overlay |
| `--elevation-primary-box-shadow` | `0 6px 20px rgba(0,0,0,0.2)` | primary popover elevation |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| reduced motion media | `@media (prefers-reduced-motion:reduce),(update:slow),(update:none)` | accessibility fallback |
| no-preference media | `@media (prefers-reduced-motion:no-preference)` | enhanced motion only when allowed |
| search button enter | `250ms` with `--motion-springs-standard-easing` fallback | search button view transition |
| trailing button enter | `150ms` with linear curve fallback | search trailing controls |
| trailing/input exit | `75ms` | disappearing search elements |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: variable by surface; wide desktop behavior appears at `1128px` and `1440px`.
- **Grid type**: generated atomic CSS using flex/grid utilities and component-specific variables.
- **Column count**: marketplace listing grids collapse responsively; exact count depends on viewport and card min width.
- **Gutter**: 16-24px in dense card zones; macro section spacing uses 48-80px.

### Hero

- **Pattern Summary**: white marketplace header + prominent search affordance + inventory/category discovery below.
- Layout: centered/top navigation with a search surface rather than a marketing hero block.
- Background: solid `#FFFFFF`.
- **Background Treatment**: solid surface; no atmospheric gradient mesh or decorative bokeh.
- H1: not the dominant homepage pattern in the captured marketplace entry; titles use Cereal semibold ladder.
- Max-width: responsive application shell rather than a fixed prose hero.

### Section Rhythm

```css
section {
  padding: 48px 24px;          /* editorial/open mode */
  gap: 16px;                   /* marketplace/card mode */
  background: #FFFFFF;
}
```

### Card Patterns

- **Card background**: `#FFFFFF`.
- **Card border**: none for listing-card chrome; borders/hairlines appear in inputs and overlay containers.
- **Card radius**: 12px common, 20px for larger elevated containers.
- **Card padding**: image cards rely on grid gap; content gap often 2-12px, outer spacing 16-24px.
- **Card shadow**: none for listing cards; `--elevation-*` reserved for popovers, modals, expandable cards.

### Navigation Structure

- **Type**: horizontal marketplace nav with centered content/search and trailing account/actions.
- **Position**: page header/application shell; may become sticky depending on scroll state.
- **Height**: navigation tokens include 48px minimum and search-header height around 5rem.
- **Background**: `#FFFFFF`.
- **Border**: subtle `#DDDDDD` / `#EBEBEB` hairline where needed.

### Content Width

- **Prose max-width**: not the primary model; content is card/grid based.
- **Container max-width**: breakpoint-driven marketplace shell with wide desktop at 1128/1440.
- **Sidebar width**: not a primary homepage structure in captured data.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Small phone | `375px` | early phone-specific adjustments |
| Tablet | `744px` | major layout expansion and multi-column behavior |
| Search/layout intermediate | `950px` | header/search refinements |
| Desktop | `1128px` | primary desktop marketplace shell |
| Large | `1440px` | wide desktop spacing/column refinements |

### Touch Targets

- **Minimum tap size**: search/profile/icon controls target comfortable mobile hit areas; profile button radius observed at 21px and 30px variants.
- **Button height (mobile)**: infer at least 44-48px for navigation/search controls.
- **Input height (mobile)**: search header has `5rem` context; inner search controls vary by state.

### Collapsing Strategy

- **Navigation**: horizontal shell reduces into compact mobile controls; search becomes the primary action.
- **Grid columns**: listing/card grids collapse by viewport and min-card width rather than a fixed 12-column system.
- **Sidebar**: none in the primary homepage pattern.
- **Hero layout**: search-first marketplace header remains the hero; category/listing discovery stacks below on smaller widths.

### Image Behavior

- **Strategy**: listing imagery carries visual weight; containers use rounded clipping.
- **Max-width**: responsive, card-bound.
- **Aspect ratio handling**: likely card/image ratio controlled by component CSS; exact per-card ratio not fully measured in this pass.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary action**

```html
<button class="airbnb-button airbnb-button--primary">Search</button>
```

| Property | Value |
|---|---|
| Font | `Airbnb Cereal VF`, 600 |
| Background | `#FF385C` or Rausch gradient variant for special states |
| Text | `#FFFFFF` |
| Radius | 8px for normal button; 50% for icon/search orb |
| Hover | darker/product Rausch family such as `#E00B41` or gradient-hover when used |
| Focus | ring pattern `0 0 0 2px #FFFFFF, 0 0 0 4px #222222` observed in CSS |
| Disabled | soft neutral `#F7F7F7` / `#DDDDDD` family |

### Badges

Badges and chips are neutral-first. Selected state flips to inverse `#222222` background with white text, while unselected chips use `#FFFFFF` or `#F7F7F7` with transparent or grey border.

```html
<button class="airbnb-chip" aria-pressed="true">Amazing views</button>
```

| State | Background | Border | Text |
|---|---|---|---|
| default | `#FFFFFF` | `#DDDDDD` | `#222222` |
| hover | `#F7F7F7` or `#EBEBEB` | transparent / `#DDDDDD` | `#222222` |
| selected | `#222222` | `#222222` | `#FFFFFF` |

### Cards & Containers

Listing cards are deliberately quiet:

```html
<article class="airbnb-listing-card">
  <img class="airbnb-listing-card__image" alt="">
  <div class="airbnb-listing-card__content">
    <strong>Listing title</strong>
    <span>Distance or host metadata</span>
    <b>$ price</b>
  </div>
</article>
```

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Image radius | 12px common |
| Content gap | 2-8px metadata, 12px layout gap |
| Shadow | none on regular listing cards |
| Overlay/elevated card | 20-30px radius, `--elevation-primary` or `--elevation-elevation2` |

### Navigation

Navigation uses a three-zone grid token:

```css
--navigation-bar_grid-template-columns:
  [leading-slot] 1fr [content-slot] auto [trailing-slot] 1fr;
--navigation-bar_min-height: 48px;
```

The visual rule is balanced symmetry: logo/leading area, centered search or nav content, trailing user controls. Background stays `#FFFFFF`; borders remain hairline.

### Inputs & Forms

Search inputs are the core form pattern.

| Property | Value |
|---|---|
| Background | `#FFFFFF`, with gradient fallback `linear-gradient(-180deg,#ffffff 39.9%,#f8f8f8 100%)` in one search input path |
| Border | `#DDDDDD` / subtle hairline |
| Placeholder | muted Cereal text |
| Focus | black/white double ring patterns |
| Error | `#C13515` text/border, `#FFF8F6` error surface |

### Hero Section

Airbnb's hero is operational: search first, inventory next.

```html
<header class="airbnb-marketplace-header">
  <nav>...</nav>
  <form class="airbnb-search-surface">
    <button class="airbnb-search-orb" aria-label="Search"></button>
  </form>
</header>
```

| Property | Value |
|---|---|
| Surface | `#FFFFFF` |
| Primary action | circular `#FF385C` search button |
| Typography | semibold Cereal for labels, 400/500 for metadata |
| Shadow | subtle/elevated only when search surface floats |

### 13-2. Named Variants

- **button-primary** — Rausch action button; `#FF385C` background, white text, 600 weight.
- **button-search-orb** — circular search submit; Rausch fill, 50% radius, icon-only target.
- **chip-default** — white/soft neutral pill with grey boundary.
- **chip-selected** — inverse `#222222` chip with `#FFFFFF` text.
- **listing-card-flat** — image-led card with no decorative border or chrome shadow.
- **modal-card-elevated** — 20-30px radius with multi-layer elevation for overlays and expandable cards.
- **profile-button-round** — account/menu affordance using 21px/30px rounded variants.

### 13-3. Signature Micro-Specs

```yaml
rausch-search-orb:
  description: "Commitment is marked by one circular Rausch action, not by a branded page wash."
  technique: "background #FF385C /* {colors.primary} */; color #FFFFFF; border-radius 50%; inline-size/block-size around 48px; optional Rausch gradient variant only for special action states"
  applied_to: ["{component.search-orb}", "{component.button-primary}"]
  visual_signature: "A single warm red-pink dot inside an otherwise white marketplace header."

flat-photo-led-listing-card:
  description: "The photo is the card; the surrounding chrome stays nearly absent."
  technique: "background #FFFFFF /* {colors.surface-base} */; image border-radius 12px; regular card shadow none; content gap 2-8px for metadata and 12px for layout rhythm"
  applied_to: ["{component.listing-card}", "{component.card-image}"]
  visual_signature: "Listings read as a field of rounded photographs rather than boxed UI panels."

overlay-only-elevation:
  description: "Depth is reserved for temporary decision surfaces while the browsing grid remains flat."
  technique: "modal shadow 0 6px 20px rgba(0,0,0,0.2); elevation tiers such as 0px 8px 24px rgba(0,0,0,0.10) and 0px 12px 30px rgba(0,0,0,0.12); regular listing cards use no default shadow"
  applied_to: ["{component.modal-card}", "{component.popover}", "{component.listing-card}"]
  visual_signature: "Menus and modals float clearly, but inventory stays calm and comparison-friendly."

white-black-double-focus-ring:
  description: "Focus is explicit and accessible without adding a colored brand halo."
  technique: "box-shadow 0 0 0 2px #FFFFFF, 0 0 0 4px #222222; no layout shift; works over white and neutral surfaces"
  applied_to: ["{component.button-primary}", "{component.chip-selected}", "{component.search-input}"]
  visual_signature: "A crisp black outer ring with a white buffer, like an ink outline lifted off the surface."

macro-micro-marketplace-rhythm:
  description: "Airbnb alternates between open intent zones and compressed comparison zones."
  technique: "macro spacing 48px/64px/80px for search and editorial headers; micro spacing 2px/4px/8px/12px/16px for card metadata, chips, and inputs"
  applied_to: ["{component.hero-search}", "{component.listing-card}", "{component.chip-default}"]
  visual_signature: "The page breathes before search, then tightens into fast listing comparison."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: auto+manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | direct travel utility, concrete inventory promise | "Vacation Rentals, Cabins, Beach Houses, Unique Homes & Experiences" |
| Primary CTA | action verb, usually search/reserve/continue pattern | "Search" |
| Marketplace metadata | compact, scannable, no flourish | destination, date, price, rating |
| Tone | friendly, plain, consumer-trust oriented | avoids luxury poetry in functional UI |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Airbnb-inspired marketplace tokens */
:root {
  /* Fonts */
  --airbnb-font-family:
    "Airbnb Cereal VF", "Circular", -apple-system, BlinkMacSystemFont,
    "Roboto", "Helvetica Neue", sans-serif;
  --airbnb-font-weight-body: 400;
  --airbnb-font-weight-label: 500;
  --airbnb-font-weight-title: 600;
  --airbnb-font-weight-bold: 700;

  /* Brand */
  --airbnb-rausch: #FF385C;
  --airbnb-product-rausch: #E00B41;
  --airbnb-rausch-1: #E61E4D;
  --airbnb-rausch-2: #E31C5F;
  --airbnb-rausch-3: #D70466;

  /* Surfaces and text */
  --airbnb-bg-page: #FFFFFF;
  --airbnb-bg-soft: #F7F7F7;
  --airbnb-border: #DDDDDD;
  --airbnb-border-soft: #EBEBEB;
  --airbnb-text: #222222;
  --airbnb-muted: #6A6A6A;

  /* Semantic */
  --airbnb-success: #008A05;
  --airbnb-error: #C13515;
  --airbnb-error-bg: #FFF8F6;

  /* Spacing */
  --airbnb-space-1: 4px;
  --airbnb-space-2: 8px;
  --airbnb-space-3: 12px;
  --airbnb-space-4: 16px;
  --airbnb-space-6: 24px;
  --airbnb-space-8: 32px;
  --airbnb-space-12: 48px;
  --airbnb-space-16: 64px;
  --airbnb-space-20: 80px;

  /* Radius */
  --airbnb-radius-sm: 8px;
  --airbnb-radius-md: 12px;
  --airbnb-radius-lg: 16px;
  --airbnb-radius-xl: 20px;
  --airbnb-radius-2xl: 24px;
  --airbnb-radius-3xl: 32px;

  /* Elevation */
  --airbnb-shadow-overlay:
    0 0 0 1px rgba(0,0,0,0.02),
    0 8px 24px 0 rgba(0,0,0,0.10);
}

body {
  margin: 0;
  background: var(--airbnb-bg-page);
  color: var(--airbnb-text);
  font-family: var(--airbnb-font-family);
  font-weight: var(--airbnb-font-weight-body);
  letter-spacing: normal;
}

.airbnb-search-orb {
  inline-size: 48px;
  block-size: 48px;
  border: 0;
  border-radius: 50%;
  background: var(--airbnb-rausch);
  color: #FFFFFF;
}

.airbnb-listing-card {
  display: grid;
  gap: var(--airbnb-space-3);
  background: var(--airbnb-bg-page);
  color: var(--airbnb-text);
}

.airbnb-listing-card img {
  width: 100%;
  border-radius: var(--airbnb-radius-md);
  object-fit: cover;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Airbnb-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        airbnb: {
          rausch: '#FF385C',
          product: '#E00B41',
          text: '#222222',
          muted: '#6A6A6A',
          border: '#DDDDDD',
          soft: '#F7F7F7',
          white: '#FFFFFF',
          error: '#C13515',
          success: '#008A05',
        },
      },
      fontFamily: {
        sans: ['Airbnb Cereal VF', 'Circular', '-apple-system', 'BlinkMacSystemFont', 'Roboto', 'Helvetica Neue', 'sans-serif'],
      },
      fontWeight: {
        book: '400',
        medium: '500',
        semibold: '600',
        bold: '700',
      },
      borderRadius: {
        airbnbSm: '8px',
        airbnbMd: '12px',
        airbnbLg: '16px',
        airbnbXl: '20px',
        airbnb2xl: '24px',
        airbnb3xl: '32px',
      },
      boxShadow: {
        airbnbOverlay: '0 0 0 1px rgba(0,0,0,0.02), 0 8px 24px 0 rgba(0,0,0,0.10)',
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
| Brand primary | `{colors.primary}` | `#FF385C` |
| Product primary | `{colors.product-primary}` | `#E00B41` |
| Background | `{colors.surface-base}` | `#FFFFFF` |
| Soft background | `{colors.surface-soft}` | `#F7F7F7` |
| Text primary | `{colors.text-primary}` | `#222222` |
| Text muted | `{colors.text-muted}` | `#6A6A6A` |
| Border | `{colors.border-primary}` | `#DDDDDD` |
| Success | `{colors.success}` | `#008A05` |
| Error | `{colors.error}` | `#C13515` |

### Example Component Prompts

#### Hero / Search Section

```text
Airbnb 스타일의 marketplace search header를 만들어줘.
- 배경: #FFFFFF
- 폰트: Airbnb Cereal VF fallback stack
- 텍스트: #222222, secondary는 #6A6A6A
- 검색 표면: white pill/card, hairline #DDDDDD, radius 32px 내외
- submit: circular #FF385C button, white icon, 48px hit target
- 레이아웃: mobile first, 744px / 1128px / 1440px breakpoints
- 장식 그라디언트나 큰 hero 카드는 넣지 말고, 검색이 hero 역할을 하게 해줘
```

#### Listing Card

```text
Airbnb 스타일 listing card를 만들어줘.
- 카드 chrome: border/shadow 없음, background #FFFFFF
- 이미지: width 100%, object-fit cover, radius 12px
- content gap: 2-8px metadata, 12px section gap
- title: Airbnb Cereal VF 15-16px, weight 600, color #222222
- metadata: 14-15px, weight 400, color #6A6A6A
- price: #222222, weight 600 for amount only
```

#### Chip

```text
Airbnb 스타일 category chip을 만들어줘.
- default: bg #FFFFFF 또는 #F7F7F7, text #222222, border #DDDDDD
- hover: bg #F7F7F7 또는 #EBEBEB
- selected: bg #222222, text #FFFFFF
- radius: pill, padding은 8px 16px 근처
- focus: #FFFFFF inner ring + #222222 outer ring
```

#### Modal / Overlay

```text
Airbnb 스타일 overlay card를 만들어줘.
- surface: #FFFFFF
- radius: 20px 또는 24px
- shadow: 0 6px 20px rgba(0,0,0,0.2) 또는 multi-layer elevation
- border: rgba(0,0,0,0.04) 1px
- 내부 간격: 24px 기본, 큰 섹션은 32px
```

### Iteration Guide

- **색상 변경 시**: Rausch `#FF385C`는 primary action에만 유지. 링크/배지/배경 전체에 확산하지 말 것.
- **폰트 변경 시**: Cereal이 없으면 Circular 또는 Inter fallback을 쓰되 weight role은 400/500/600으로 유지.
- **카드 추가 시**: listing card에는 shadow/border를 넣지 말고 이미지 radius와 spacing으로 구조를 만든다.
- **오버레이 추가 시**: shadow는 overlay 전용으로 사용한다. regular grid chrome에 elevation을 남발하지 않는다.
- **반응형 추가 시**: 744px, 1128px, 1440px 축을 우선 사용한다.
- **모션 추가 시**: search transition은 75-250ms 범위로 짧게; decorative parallax는 피한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#FFFFFF` as the dominant marketplace surface.
- Use `#FF385C` for primary action moments: search, reserve/continue, save/heart, key brand affordances.
- Keep primary text at `#222222` and secondary metadata at `#6A6A6A`.
- Let listing photography carry color and mood; keep UI chrome neutral.
- Use 12px radius for listing imagery/cards and larger 20-32px radius for overlays.
- Reserve shadows for modals, popovers, expandable cards, and floating search surfaces.
- Use 744px, 1128px, and 1440px as the main responsive anchors.
- Maintain Cereal-like weight hierarchy: 400 body, 500 label, 600 title/action.

### ❌ DON'T

- 배경을 `#F5F5F7` 또는 `#FAFAFA` 중심으로 두지 말 것 — Airbnb의 기본 marketplace floor는 `#FFFFFF` 사용.
- 본문 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 기본 ink는 `#222222` 사용.
- muted 텍스트를 `#999999`로 흐리게 만들지 말 것 — metadata는 `#6A6A6A` 사용.
- hairline을 `#CCCCCC`로 세게 만들지 말 것 — 기본 border는 `#DDDDDD`, soft divider는 `#EBEBEB` 사용.
- primary CTA를 `#E00B41`만으로 고정하지 말 것 — canonical brand signal은 `#FF385C`, `#E00B41`는 product/pressed 계열로 사용.
- 성공 상태를 임의의 초록 `#00AA00`로 만들지 말 것 — observed success token은 `#008A05` 사용.
- 오류 상태를 generic red `#FF0000`으로 만들지 말 것 — Airbnb error family는 `#C13515` / `#B32505` / `#FFF8F6` 사용.
- listing card에 default `box-shadow`를 넣지 말 것 — normal listing grid는 flat image-led card로 유지.
- display heading에 `font-weight: 800`을 남발하지 말 것 — display/title의 핵심은 600이다.
- search/CTA radius를 사각 4px로 만들지 말 것 — normal button은 8px, search orb는 50%, large surfaces는 20-32px.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second brand color: none for core marketplace UI. Rausch carries the action identity; Plus/Luxe colors are sub-brand contexts, not general UI accents.
- Decorative page gradients: absent in the core surface. Gradients exist as Rausch/Plus/Luxe action variants, not as hero background wallpaper.
- Listing-card chrome: no default heavy border, no default shadow, no colored frame.
- Serif contrast: none. Airbnb does not switch to editorial serif typography for travel romance.
- Negative display tracking: effectively absent; typography tokens keep `letter-spacing: normal`.
- Heavy black ink: avoided. `#222222` is the working text anchor, with `#000000` reserved for deeper inverse/hover cases.
- Long animation spectacle: absent from the brand expression. Motion supports search transitions and state changes.
- Purple-blue SaaS gradient: absent from the main marketplace. Purple appears in Luxe/Plus systems only.
- Dense dashboard sidebars: none in the homepage marketplace pattern.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single captured entry surface** — this guide reuses existing `airbnb` phase1/CSS/HTML artifacts. It does not verify checkout, host onboarding, account settings, or post-login flows.
- **Screenshot not visually re-inspected in this pass** — screenshot files exist, but the analysis primarily used CSS/JSON/HTML facts and known marketplace patterns.
- **Component state coverage is partial** — focus, hover, selected, disabled, and search transition patterns were observed in CSS, but loading and error states were not exhaustively mapped per component.
- **Dark-mode mapping incomplete** — dark/inverse elevation and neutral tokens exist in CSS, but the captured homepage default is light. Treat dark values as token availability, not a full dark theme spec.
- **Exact listing grid measurements are inferred** — breakpoints and spacing tokens are measured, but live card counts and image aspect ratios vary by viewport and content.
- **Generated atomic classes reduce semantic certainty** — `atm_*` classes obscure author intent; component interpretation relies on token names and repeated CSS variable patterns.
- **Brand gradients are present but context-sensitive** — Rausch, Plus, and Luxe gradients exist in CSS; this guide treats them as action/sub-brand variants, not page-wide decoration.
- **No report HTML generated** — per user instruction, Step 6 RENDER-HTML was skipped and only `design.md` was produced.
