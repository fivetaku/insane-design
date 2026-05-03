---
schema_version: 3.2
slug: dior
service_name: Dior
site_url: https://www.dior.com
fetched_at: 2026-05-03
default_theme: mixed
brand_color: "#33383C"
primary_font: "Atacama VAR"
font_weight_normal: 352
token_prefix: "ot"

bold_direction: "Monochrome Luxury"
aesthetic_category: "other"
signature_element: "hero_impact"
code_complexity: "high"

medium: web
medium_confidence: high

archetype: luxury-brand
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "CSS exposes a compact token layer, variable fonts, MUI-generated components, glass header states, and consistent editorial commerce patterns, but no public formal DS naming beyond runtime tokens."

colors:
  ink-primary: "#33383C"
  white: "#FFFFFF"
  image-black: "#000000"
  surface-soft: "#F8F8F8"
  hairline: "#D8D8D8"
  text-muted: "#7B8487"
  text-soft: "#ACB2B4"
  cookie-green: "#468254"
typography:
  display: "Atacama VAR"
  body: "Hellix"
  icon: "ABCDiorIcons"
  ladder:
    - { token: hero-logo, size: "30px svg mark", weight: "logo-outline", line_height: "1", tracking: "N/A" }
    - { token: headline-m-desktop, size: "2rem", weight: 352, line_height: "42px", tracking: "-0.04rem" }
    - { token: headline-m-mobile, size: "1.5rem", weight: 352, line_height: "34px", tracking: "-0.03rem" }
    - { token: body-control, size: "0.875rem", weight: 500, line_height: "17px", tracking: "normal" }
    - { token: editorial-copy, size: "1rem", weight: 300, line_height: "22px", tracking: "normal" }
  weights_used: [100, 300, 352, 400, 500, 600, 700]
  weights_absent: [800, 900]
components:
  button-contained-ink: { bg: "{colors.ink-primary}", fg: "{colors.white}", radius: "4px", padding: "6px 16px" }
  button-outline-ink: { bg: "transparent", fg: "{colors.ink-primary}", border: "rgba(51,56,60,0.5)", radius: "4px" }
  header-glass: { bg: "transparent to rgba surface", blur: "blur(calc(var(--blur-medium, 3.125rem) / 2))", height: "4rem / 5rem" }
  category-tile: { bg: "image", overlay: "linear-gradient(180deg, #00000000 50%, #0000007F 100%)", typography: "Atacama VAR 352" }
---

# DESIGN.md — Dior (Claude Code Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Dior's homepage reads like a museum-grade store where two boutique salons open side by side. The first viewport is split between fashion and beauty, each tile filled by photography, with the Dior wordmark floating across the seam as a house plaque. The interface chrome almost disappears; the product world, models, packaging, and light carry the brand. The page does not announce luxury through gold UI or ornamental borders. It lets the image take the risk, then anchors it with severe monochrome restraint.

The operating palette is not a perfume-box pink or a couture metallic. The UI's actual anchor is #33383C (`{colors.ink-primary}`), a cool charcoal used for content, outlines, and contained controls. White #FFFFFF (`{colors.white}`) appears as boutique light on image, not as a generic SaaS canvas. Black #000000 (`{colors.image-black}`) is mostly photographic material and overlay gauze. There is no second brand color waiting in the system: the maison refuses the expected gold clasp, and lets neutral ink behave like the stitching inside a couture garment.

Typography is the couture layer. Display text uses Atacama VAR with a deliberately unusual `wght` axis around 352, while everyday controls use Hellix at 500. The result is a soft serif-adjacent fashion headline over a modern commerce skeleton. It reads like a runway card pinned beside the garment: small, exact, and never louder than the dress. Headline tracking tightens slightly at larger sizes (`-0.03rem` to `-0.04rem`), enough to feel composed without becoming tech-brand optical compression.

The main craft is the disappearing frame. The split hero works like double doors opening into two salons, with the white Dior SVG suspended as a house plaque across the threshold. The bottom gradient is not a caption box; it is a theater scrim pulled up from the floor so the labels can sit inside the photograph. The glass header behaves like a vitrine edge: present only when light catches it, then gone again when the image needs the room.

Luxury here is a subtraction discipline: no broad accent palette, no heavy elevation, no product-card confetti, no generic "premium" gradient. Shadow belongs to modal or third-party surfaces, not to the category photography. The system remembers the maison by image, wordmark, and air; the page has very little site-self, because the chrome keeps stepping back to let the campaign world occupy the wall.

조금 더 풀면, Dior 홈은 **메종의 매장윈도우 두 짝과 부티크 안쪽 진열대**처럼 작동한다. split hero는 부티크 입구의 양쪽 매장윈도우 — 한쪽은 패션 컬렉션 진열대, 다른 한쪽은 향수와 뷰티의 큐레이션박스다. 흰 Dior SVG는 두 윈도우 사이 유리 위에 새겨진 메종 각인, 헤더의 glass 상태는 부티크 카운터 위 투명 진열장 가장자리 같은 존재감이다. 카테고리 라벨은 진열대 발치에 놓인 이름표, hover/sticky 상태 변화는 공방 안쪽에서 조명이 한 번씩 들어오는 호흡이다 — 두 번째 brand color가 없는 이유는, 메종의 큐레이션박스 안에는 옷감과 빛 외의 색이 들어가지 않기 때문이다.

### Key Characteristics

- Full-viewport editorial commerce split: Fashion & Accessories and Fragrance & Beauty share the first screen as equal image portals.
- Floating Dior SVG logo in white over photography, positioned as a brand seal rather than a nav label.
- Cool charcoal UI anchor #33383C (`{colors.ink-primary}`), with white and black behaving as photographic support.
- Atacama VAR display text with non-standard `wght` 352 and tight negative tracking on headlines.
- Hellix for controls, cookie UI, buttons, and functional commerce copy.
- Header state system: transparent overlay, fixed glass mode, sticky solid mode, and forced icon color variants.
- Category tiles rely on `object-fit: cover`, absolute image placement, and bottom gradient legibility.
- Radius is mostly modest: 4px/6px for controls, 999px only for pill or circular utility forms.
- Shadows are intentionally sparse; depth belongs to imagery and modal surfaces, not cards.
- Motion favors slow, polished state transitions with cubic-bezier `0.31,0,0.13,1`.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Monochrome Luxury
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **hero_impact**으로 기억된다.
> **Code Complexity**: high — transparent/glass/sticky header states, variable-font axes, image overlays, and MUI-generated variant controls require more than static token copying.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Dior처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Hellix", "ABCDiorIcons", arial, sans-serif;
  font-weight: 400;
}

.dior-display {
  font-family: "Atacama VAR", "ABCDiorIcons", arial, sans-serif;
  font-weight: normal;
  font-variation-settings: "wght" 352, "wdth" 100, "CNTR" 28, "XHGT" 0;
  letter-spacing: -0.04rem;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #33383C; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #33383C; }
```

**절대 하지 말아야 할 것 하나**: Dior를 금색 luxury palette로 번역하지 말 것. 실제 UI anchor는 #33383C charcoal이고, chromatic 색은 cookie/third-party/form states를 제외하면 브랜드 코어가 아니다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.dior.com` |
| Fetched | 2026-05-03 |
| Extractor | reused `insane-design/dior` phase1 artifacts from prior capture |
| HTML size | 546138 bytes (Next/MUI-style SSR + hydrated commerce shell) |
| CSS files | 3 files, total 244456 chars |
| Token prefix | `ot` for OneTrust/cookie token layer; generated MUI classes for main surface |
| Method | Existing HTML/CSS/phase1 JSON + screenshot interpretation; no new network fetch |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js-style SSR with MUI generated classes and React commerce shell.
- **Design system**: Dior runtime system — prefix `ot` appears for consent layer tokens; core page components use MUI class generation and product-specific CSS modules.
- **CSS architecture**:
  ```text
  OT tokens        (--ot-*)                 cookie/consent semantic tokens
  Variant tokens   (--variant-*)            MUI button/control state values
  CSS modules      Header_* / MainNavigation_* page chrome and nav state classes
  MUI classes      .mui-latin-*             generated layout, hero, typography, media classes
  ```
- **Class naming**: Mixed CSS modules (`Header_header__d1Ndh`) + MUI runtime classes (`mui-latin-3xoi18`) + third-party namespaces (`ot-*`, `swiper-*`, `PhoneInput-*`).
- **Default theme**: mixed. Homepage hero is dark-over-image in the first viewport; commerce and consent surfaces include white and #F8F8F8 floors.
- **Font loading**: CSS `@import` loads `/static/fashion/fontsv3/AtacamaVAR/AtacamaVAR.css` and `/static/fashion/fontsv3/Hellix/Hellix.css`.
- **Canonical anchor**: white Dior logo over split photography, with category labels bottom-centered over image gradients.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Atacama VAR` (custom Dior fashion font, site-hosted)
- **Body/control font**: `Hellix` (site-hosted)
- **Icon font**: `ABCDiorIcons`
- **Weight normal / bold**: `352 display axis / 400 body` / `500 control emphasis, 600-700 rare utility`

```css
:root {
  --ot-font-primary:   "Atacama VAR", arial, sans-serif;
  --ot-font-secondary: "Hellix", arial, sans-serif;
}

body {
  font-family: "Hellix", "ABCDiorIcons", arial, sans-serif;
  font-weight: 400;
}

.headline {
  font-family: "Atacama VAR", "ABCDiorIcons", arial, sans-serif;
  font-weight: normal;
  font-variation-settings: "wght" 352, "wdth" 100, "CNTR" 28, "XHGT" 0;
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Atacama VAR** is the signature display voice. If unavailable, use **Cormorant Garamond** or **Libre Baskerville** only for editorial headings, then tighten tracking by `-0.02em` to `-0.03em` and keep line-height around `1.30`.
- **Hellix** should fall back to **Inter** or **Arial** for controls, but do not let Inter become the entire brand. Keep display and control families separated.
- For Dior-like headings, avoid heavy 600+ serif display. The observed headline axis is lighter: `font-variation-settings: "wght" 352`.
- The Dior wordmark should remain SVG/artwork. Do not replace it with typed text in Atacama.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| hero-logo-svg | SVG viewBox 106x30 | artwork | 1 | N/A |
| headline-m-mobile | 1.5rem | Atacama `wght` 352 | 34px | -0.03rem |
| headline-m-desktop | 2rem | Atacama `wght` 352 | 42px | -0.04rem |
| editorial-copy | 1rem | Atacama `wght` 300 | 22px | normal |
| editorial-copy-desktop | 1.25rem | Atacama `wght` 300 | 28px | normal |
| control | 0.875rem | Hellix 500 | 17px | normal |
| small-control | 0.75rem / 0.8125rem | Hellix 400-500 | 1.2-1.4 | normal |

> ⚠️ Dior's typography is not "luxury = high contrast serif everywhere." The split is Atacama for editorial presence and Hellix for functional commerce.

### Principles
<!-- SOURCE: manual -->

1. Display weight is an axis setting, not a standard CSS weight. The signature observed value is `"wght" 352`, which sits between common 300 and 400.
2. Headline tracking tightens only at display sizes. Mobile headline uses `-0.03rem`; desktop uses `-0.04rem`; controls keep `letter-spacing: normal`.
3. Body control density is compact: 0.875rem, 17px line-height, Hellix 500. This keeps commerce UI crisp over photographic luxury.
4. The wordmark is not typography in the layout system. It is SVG brand artwork filled #FFFFFF over image.
5. Weight 700 appears in utility or third-party contexts, not as the default couture voice.
6. Atacama and Hellix must remain separated. Collapsing the whole page into one fallback font removes the Dior tension between fashion editorial and retail function.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (neutral anchor)
<!-- SOURCE: auto -->

| Token | Hex |
|---|---|
| `--ot-black-100` | `#ACB2B4` |
| `--ot-black-200` | `#7B8487` |
| `--ot-black-300` | `#5D676C` |
| `--ot-black-400` | `#33383C` |

### 06-2. Brand Dark Variant
<!-- SOURCE: auto+manual -->

| Token | Hex |
|---|---|
| hero overlay start | `#00000000` |
| hero overlay end | `#0000007F` |
| image black | `#000000` |
| sticky/header icon dark | `#33383C` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light | Dark |
|---|---|---|
| white | `#FFFFFF` | `#000000` |
| surface-soft | `#F8F8F8` | `#33383C` |
| surface-muted | `#F3F3F3` | `#5D676C` |
| border-light | `#E5E5E5` | `#7B8487` |
| hairline | `#D8D8D8` | `#ACB2B4` |

### 06-4. Accent Families
<!-- SOURCE: auto+manual -->

| Family | Key step | Hex |
|---|---|---|
| Dior UI accent | charcoal | `#33383C` |
| Cookie/consent accept | green | `#468254` |
| Cookie/consent pressed | deep green | `#2C6415` |
| Error/destructive utility | red | `#C53929` |
| Third-party focus | blue | `#03B2CB` |
| Browser/mobile focus outline | blue | `#1574C3` |

### 06-5. Semantic
<!-- SOURCE: auto+manual -->

| Token | Hex | Usage |
|---|---|---|
| `{colors.ink-primary}` | `#33383C` | Text, contained buttons, outlines, active states |
| `{colors.white}` | `#FFFFFF` | Logo fill over image, contained text, light surfaces |
| `{colors.surface-soft}` | `#F8F8F8` | Loading and neutral commerce surface |
| `{colors.hairline}` | `#D8D8D8` | Structural dividers and pale UI borders |
| `{colors.text-muted}` | `#7B8487` | Secondary links, consent copy, muted UI |
| `{colors.text-soft}` | `#ACB2B4` | Disabled or low-emphasis UI |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--ot-color-content-primary` | `--ot-black-400` -> `#33383C` | Primary consent/UI content |
| `--ot-color-content-primary-alt-1` | `--ot-black-200` -> `#7B8487` | Secondary links |
| `--ot-color-outline-primary` | `--ot-black-400` -> `#33383C` | Primary outlines |
| `--ot-color-outline-primary-alt` | `--ot-white-100` -> `#E5E5E5` | Light outline |
| `--ot-color-state-primary-alt-hover` | `--ot-black-300` -> `#5D676C` | Hover state |
| `--ot-color-state-disable-content` | `--ot-black-100` -> `#ACB2B4` | Disabled state |
| `--variant-containedBg` | `#33383C` / `rgba(35,39,42,1)` | MUI contained button background |
| `--variant-outlinedBorder` | `rgba(51,56,60,0.5)` / `#33383C` | MUI outline border |

### 06-7. Dominant Colors (실제 DOM/CSS 빈도 순)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---|---|
| ink-primary | `#33383CFF` | 114 |
| white short | `#FFF` | 84 |
| black short | `#000` | 44 |
| hairline | `#D8D8D8` | 40 |
| text-soft | `#ACB2B4FF` | 38 |
| text-muted | `#7B8487FF` | 36 |
| white full alpha | `#FFFFFFFF` | 24 |
| third-party blue | `#3860BE` | 24 |

### Color Stories
<!-- SOURCE: manual -->

**`{colors.ink-primary}` (`#33383C`)** — Dior's practical brand color in the captured UI. It is used for content, outlines, variant controls, and state anchors. Treat it as the system's charcoal ink, not as a fallback black.

**`{colors.white}` (`#FFFFFF`)** — White is the over-photography luxury signal: logo fill, label text, and contained-button text. It should appear as light on image or clean commerce surface, not as a generic empty landing-page canvas.

**`{colors.image-black}` (`#000000`)** — Black is mostly photographic and overlay material. The important use is the 50% to 100% bottom-gradient legibility layer on image tiles, not a flat black page background.

**`{colors.hairline}` (`#D8D8D8`)** — Hairline gray supplies structure where Dior refuses decorative color. Use it for dividers and borders only; do not promote it into large backgrounds.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--ot-small-s` | `0.125rem` | Tiny link underline / micro offset |
| `--ot-small-m` | `0.25rem` | Focus/link padding bottom |
| `--ot-small-l` | `0.5rem` | Compact consent spacing |
| `--ot-small-xl` | `0.75rem` | Compact content spacing |
| `--ot-small-xxl` | `1rem` | Edge inset and mobile padding unit |
| `--ot-medium-xs` | `1.25rem` | Consent/header offset |
| `--ot-medium-s` | `1.5rem` | Modal/header spacing |
| `--ot-medium-m` | `2rem` | Larger block spacing |
| hero/content gap | `32px` | Desktop margin-top and content grouping |
| editorial column gap | `48px` | Mobile stacked commerce/editorial gap |
| category grid gap | `16px` | Desktop 4-column listing gap |

**주요 alias**:
- `--desktop-min-width` -> `18.3125rem` / `19.75rem` / `22.9375rem` / `28.75rem` by viewport, used to tune desktop minimum columns.

### Whitespace Philosophy
<!-- SOURCE: manual -->

Dior's whitespace is not a geometric 4-8-16 SaaS ladder. The page alternates between full photographic occupation and very exact UI insets. The first viewport has almost no framed whitespace because photography owns the canvas; the visible "air" comes from the dark overlay and the quiet placement of labels near the bottom.

Inside functional UI, spacing becomes compact and retail-oriented: 16px edge padding, 32px rhythm, 48px stacked gaps, 4rem/5rem header heights. The luxury is created by removing chrome around the image, then using small, measured controls when commerce appears.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| zero | `0` | Inputs and some reset surfaces |
| sharp-small | `1px` / `2px` | Fine utility surfaces |
| control-small | `4px` | Buttons, consent boxes, compact controls |
| `--ot-border-radius-m` | `0.375rem` / `6px` | Consent surface and medium controls |
| image/modal | `10px` / `20px` / `26px` / `30px` | Special surfaced components and modal shapes |
| pill | `999px` | Pill or circular utility forms only |
| circle | `50%` | Icon/circular controls |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none | `none` | Dominant chrome rule: most UI avoids elevation |
| subtle modal | `0px 2px 10px -3px #999` | Cookie/overlay-style surfaces |
| soft glow | `0px 0px 12px 2px #C7C5C7` | Special third-party/modal emphasis |
| MUI elevation 1 | `0px 2px 1px -1px rgba(0,0,0,0.2), 0px 1px 1px 0px rgba(0,0,0,0.14), 0px 1px 3px 0px rgba(0,0,0,0.12)` | MUI Paper/control surfaces |
| modal backdrop | `0 0 18px rgba(0,0,0,.2)` | Overlay containers |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `--ot-motion-easy-both` | `cubic-bezier(0.31,0,0.13,1)` | Dior/consent link and state transitions |
| MUI transition | `250ms cubic-bezier(0.4,0,0.2,1)` | Button background, shadow, border-color, color |
| header glass reveal | `opacity .5s var(--animation-easy-both) 1s` | Header backdrop-filter visibility |
| input autofill | `background-color 50000s ease-in-out` | Browser autofill suppression |
| modal fade | `opacity .2s ease` | Third-party modal/backdrop |
| reduced motion | `@media (prefers-reduced-motion: reduce)` | Motion accessibility hook present |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: First viewport is full browser width; later grids use responsive min widths and CSS grid.
- **Grid type**: Flex column on smaller screens; CSS Grid at desktop and wide breakpoints.
- **Column count**: 2 primary hero/category split; 4-column product/category grid at `min-width:1033px`; 1fr 2fr or 1fr 1fr wide editorial layouts at `1680px` and `1920px`.
- **Gutter**: 0px in the split hero/grid moments, 16px in category/product grids, 48px in mobile stacked editorial sections.

### Hero
- **Pattern Summary**: `100vh impression + split editorial photography + centered SVG wordmark + bottom category labels`
- Layout: Two equal image portals in the captured viewport, left Fashion & Accessories, right Fragrance & Beauty.
- Background: Absolute image media with `object-fit: cover`.
- **Background Treatment**: `image-overlay` with `linear-gradient(180deg, #00000000 50%, #0000007F 100%)` for bottom label legibility.
- H1: White Dior SVG wordmark, viewBox `106 30`, centered over the split image seam.
- Max-width: Full viewport for hero; image assets observed at 1080x1350 ratios with `aspect-ratio:1080/1350`.

### Section Rhythm
```css
section {
  padding: 16px;
  max-width: 100vw;
}

@media (min-width: 1033px) {
  section { margin-top: 32px; }
}
```

### Card Patterns
- **Card background**: Photography or white commerce surface. No generic card tinting.
- **Card border**: Usually absent on image cards; UI controls use `rgba(51,56,60,0.5)` or #D8D8D8-like hairlines.
- **Card radius**: Image/category hero is effectively square/edge-to-edge; control surfaces use 4px/6px.
- **Card padding**: Image tiles place text over media; commerce panels use 16px/24px/32px units.
- **Card shadow**: Mostly none. Modal/consent layers may use subtle shadows, but category cards do not.

### Navigation Structure
- **Type**: Header with left menu/back affordance, centered Dior logo, right nav/search/account utilities.
- **Position**: Absolute transparent over hero, fixed glass state, fixed sticky solid state.
- **Height**: 4rem mobile/base, 5rem desktop at `64.5625rem+`.
- **Background**: Transparent over imagery; sticky state uses `var(--color-content-secondary)`; glass state uses backdrop-filter surface.
- **Border**: Generally none; glass state relies on blur and radius.

### Content Width
- **Prose max-width**: Not surfaced in homepage capture; editorial content appears image-led.
- **Container max-width**: Full viewport for hero, grid breakpoints at 1033px/1280px/1680px/1920px.
- **Sidebar width**: Not applicable on captured homepage.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `0px` / `max-width:37.5rem` | Compact stacking, 16px padding, bottom/content adjustments |
| Tablet | `max-width:49.9375rem` / `max-width:64.0625rem` | Input and consent layout adjustments, stacked button groups |
| Desktop | `min-width:1033px` / `64.5625rem` | Header height 5rem, desktop margins, 4-column grid activation |
| Large | `min-width:1280px` / `1440px` / `1680px` / `1920px` | Desktop min-width tuning and wide editorial grid changes |

### Touch Targets
- **Minimum tap size**: Buttons carry 0.875rem text with 6px 16px padding; icon targets require surrounding header area rather than large visible buttons.
- **Button height (mobile)**: Compact MUI-style controls; modal/consent actions expand in mobile layouts.
- **Input height (mobile)**: Form controls are reset; exact checkout/search input heights not fully observed in homepage capture.

### Collapsing Strategy
- **Navigation**: Overlay header compresses to icons/menu; sticky/fixed state preserves brand center.
- **Grid columns**: Flex column on smaller widths; desktop switches to 4-column or wide split grids.
- **Sidebar**: No homepage sidebar observed.
- **Hero layout**: Captured desktop/wide hero uses split image portals; mobile likely stacks or carouselizes category entry, but exact mobile screenshot was not captured in this run.

### Image Behavior
- **Strategy**: Absolute positioned media, `object-fit: cover`, full tile coverage.
- **Max-width**: `width:100%; height:100%`.
- **Aspect ratio handling**: 1080/1350 assets with CSS `aspect-ratio:1080/1350`, object-position top or center depending tile.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<button class="MuiButtonBase-root dior-button dior-button-contained">Continue</button>
```

| Property | Value |
|---|---|
| Font | Hellix, ABCDiorIcons, arial, sans-serif |
| Size / line-height | 0.875rem / 17px |
| Weight | 500 |
| Padding | 6px 16px |
| Radius | 4px or 6px in consent/control surfaces |
| Contained bg | `#33383C` or `rgba(35,39,42,1)` |
| Contained fg | `#FFFFFF` |
| Transition | background-color, box-shadow, border-color, color over 250ms cubic-bezier(0.4,0,0.2,1) |

**States**:
- hover: `--variant-textBg: rgba(51,56,60,0.04)` or darkened contained bg.
- focus: outline/color state tokens present in consent layer.
- active/pressed: `--ot-color-state-primary-alt-pressed` -> `#33383C`.
- disabled: `--ot-color-state-disable-content` -> `#ACB2B4`.
- loading: not directly observed for homepage button.
- error: destructive red exists in CSS frequency (`#C53929`) but form error state not fully observed.

### Badges

> N/A — no brand-critical badge system was visible in the captured homepage first viewport. Do not invent colored luxury tags.

### Cards & Containers

```html
<a class="dior-category-tile">
  <img class="dior-category-media" />
  <h2 class="dior-category-title">Fashion &amp; Accessories</h2>
</a>
```

| Property | Value |
|---|---|
| Background | Full image, absolute media |
| Overlay | `linear-gradient(180deg, #00000000 50%, #0000007F 100%)` |
| Radius | 0 for hero/category tiles |
| Title color | `#FFFFFF` |
| Title font | Atacama VAR, `wght` 352 |
| Title placement | Bottom-centered over gradient |
| Shadow | none |

### Navigation

```html
<header class="Header_header__d1Ndh Header_transparent__aI1lo">
  <button id="menuburger"></button>
  <h1 id="dior-logo">DIOR SVG</h1>
  <nav id="mainrightnav"></nav>
</header>
```

| Property | Value |
|---|---|
| Base height | 4rem |
| Desktop height | 5rem |
| Transparent state | absolute, left/right 0, background transparent |
| Sticky state | fixed top 0, width 100%, z-index 300 |
| Glass state | fixed, 1rem margins, 4rem height, radius medium |
| Backdrop | `blur(calc(var(--blur-medium, 3.125rem) / 2))` |

### Inputs & Forms

```html
<input type="search" class="dior-input" />
```

| Property | Value |
|---|---|
| Reset | `appearance: none`, `border-radius: 0` |
| Placeholder | `#757575`, opacity 100% |
| Autofill | inset white box-shadow and long background-color transition |
| Focus | third-party phone input focus uses `#03B2CB`; native focus exact Dior search state not fully observed |
| Invalid | `box-shadow: none` |

### Hero Section

```html
<main class="dior-home-hero">
  <section class="dior-category dior-category-fashion">...</section>
  <section class="dior-category dior-category-beauty">...</section>
  <h1 class="dior-wordmark">DIOR</h1>
</main>
```

| Property | Value |
|---|---|
| Layout | Split image portals |
| Media | absolute, full cover, top/center object-position |
| Wordmark | White SVG, centered across split |
| Category labels | Atacama VAR 1.5rem mobile, 2rem desktop |
| Overlay | bottom black alpha gradient |
| Chrome | transparent header overlay |

### 13-2. Named Variants
<!-- SOURCE: manual -->

#### `button-contained-ink`
- bg: `#33383C`
- fg: `#FFFFFF`
- radius: `4px` or `6px`
- use: primary control, consent action, dark utility CTA.

#### `button-outline-ink`
- bg: transparent
- fg: `#33383C`
- border: `rgba(51,56,60,0.5)` or `#33383C`
- hover: `rgba(51,56,60,0.04)` surface.

#### `header-transparent`
- position: absolute
- background: transparent
- icon/logo color: forced white over hero photography.

#### `header-glass`
- position: fixed
- margin: `0 1rem`
- height: `4rem`
- radius: medium
- backdrop: blur half of `--blur-medium`.

#### `category-tile-split`
- media: full cover image
- overlay: bottom black alpha gradient
- title: Atacama VAR white headline at bottom.

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
couture-axis-display:
  description: "Dior's heading softness comes from a non-standard variable font axis, not a common 300/400 weight."
  technique: "font-variation-settings: \"wght\" 352, \"wdth\" 100, \"CNTR\" 28, \"XHGT\" 0; letter-spacing -0.03rem to -0.04rem"
  applied_to: ["{component.category-tile}", "{component.hero-section}", "{typography.display}"]
  visual_signature: "Fashion lettering feels lighter than 400 but more stable than 300, like a runway card beside the garment."

split-photography-gate:
  description: "The homepage entry is made from two equal photographic portals instead of a centered hero CTA."
  technique: "two full-viewport media surfaces; absolute img; width 100%; height 100%; object-fit: cover; category labels in #FFFFFF"
  applied_to: ["{component.hero-section}", "{component.category-tile-split}"]
  visual_signature: "A double-door maison entrance where category choice is made by crossing into photography."

bottom-legibility-veil:
  description: "Category text stays readable without adding a visible caption card."
  technique: "linear-gradient(180deg, #00000000 50%, #0000007F 100%) over full image tile"
  applied_to: ["{component.category-tile}", "{component.hero-section}"]
  visual_signature: "A dark theater scrim rises from the bottom of the image while the label remains inside the photograph."

vanishing-glass-header:
  description: "Navigation shifts between transparent, glass, and sticky states while preserving the same quiet brand posture."
  technique: "transparent absolute header; fixed sticky state; glass variant with backdrop-filter: blur(calc(var(--blur-medium, 3.125rem) / 2)); height 4rem / 5rem"
  applied_to: ["{component.header-glass}", "{component.navigation}"]
  visual_signature: "The header reads like a vitrine edge: visible only when the page needs utility, otherwise dissolved into photography."

charcoal-only-control-ink:
  description: "Control UI avoids expected luxury gold and consolidates action, outline, and text into one cool charcoal ink."
  technique: "contained bg #33383C; outlined border rgba(51,56,60,0.5); hover bg rgba(51,56,60,0.04); radius 4px/6px; padding 6px 16px"
  applied_to: ["{component.button-contained-ink}", "{component.button-outline-ink}"]
  visual_signature: "Buttons feel like black atelier labels, not decorative luxury badges."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: auto+manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Category as maison department, title-case with ampersand | "Fashion & Accessories" |
| Primary CTA | Minimal commerce verb; no playful phrasing | N/A in captured hero |
| Secondary CTA | Utility labels stay functional | "Search", "Back" |
| Subheading | Product/editorial detail likely appears below fold; not captured in first viewport |
| Tone | Formal, sparse, noun-led luxury retail |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Dior — copy into your root stylesheet */
:root {
  /* Fonts */
  --dior-font-display: "Atacama VAR", "ABCDiorIcons", arial, sans-serif;
  --dior-font-body: "Hellix", "ABCDiorIcons", arial, sans-serif;
  --dior-font-weight-display-axis: 352;
  --dior-font-weight-body: 400;
  --dior-font-weight-control: 500;

  /* Brand neutrals */
  --dior-ink-primary: #33383C;
  --dior-ink-muted: #7B8487;
  --dior-ink-soft: #ACB2B4;
  --dior-white: #FFFFFF;
  --dior-black: #000000;
  --dior-surface-soft: #F8F8F8;
  --dior-hairline: #D8D8D8;

  /* Spacing */
  --dior-space-xs: 0.25rem;
  --dior-space-sm: 0.5rem;
  --dior-space-md: 1rem;
  --dior-space-lg: 2rem;
  --dior-space-xl: 3rem;

  /* Radius */
  --dior-radius-control: 4px;
  --dior-radius-medium: 6px;
}

.dior-display {
  font-family: var(--dior-font-display);
  font-weight: normal;
  font-variation-settings: "wght" 352, "wdth" 100, "CNTR" 28, "XHGT" 0;
  letter-spacing: -0.04rem;
}

.dior-category-tile {
  position: relative;
  overflow: hidden;
  color: var(--dior-white);
  background: var(--dior-black);
}

.dior-category-tile::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, #00000000 50%, #0000007F 100%);
  pointer-events: none;
}

.dior-category-tile img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.dior-button {
  font-family: var(--dior-font-body);
  font-size: 0.875rem;
  line-height: 17px;
  font-weight: var(--dior-font-weight-control);
  padding: 6px 16px;
  border-radius: var(--dior-radius-control);
  transition:
    background-color 250ms cubic-bezier(0.4, 0, 0.2, 1),
    border-color 250ms cubic-bezier(0.4, 0, 0.2, 1),
    color 250ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `{colors.ink-primary}` | `#33383C` |
| Background | `{colors.white}` | `#FFFFFF` |
| Hero overlay black | `{colors.image-black}` | `#000000` |
| Text primary | `{colors.ink-primary}` | `#33383C` |
| Text muted | `{colors.text-muted}` | `#7B8487` |
| Border | `{colors.hairline}` | `#D8D8D8` |
| Error | destructive utility | `#C53929` |

### Example Component Prompts

#### Hero Section
```text
Dior 스타일 히어로 섹션을 만들어줘.
- 구조: 첫 화면을 좌우 2분할한 editorial image portals
- 배경: 각 portal은 실제 제품/패션 사진, object-fit: cover
- 오버레이: linear-gradient(180deg, #00000000 50%, #0000007F 100%)
- 중앙: 흰색 Dior SVG wordmark 또는 이미지 로고
- 카테고리 제목: Atacama VAR, 2rem desktop / 1.5rem mobile, wght axis 352, color #FFFFFF
- UI chrome: header는 투명하게 올리고, sticky 상태에서만 #FFFFFF/#33383C surface로 전환
```

#### Card Component
```text
Dior 스타일 category tile을 만들어줘.
- 배경: full-bleed photography, border와 shadow 없음
- radius: 0
- 텍스트: bottom centered, #FFFFFF, Atacama VAR, font-variation-settings "wght" 352
- legibility: caption box 대신 #00000000 -> #0000007F bottom gradient
- hover: 과한 scale/bounce 없이 250-500ms opacity 또는 media crop 변화만
```

#### Badge
```text
Dior 스타일 배지는 기본적으로 만들지 마라.
필요하면 색 배지가 아니라 #33383C 텍스트와 #D8D8D8 hairline만 사용하고,
radius 4px, Hellix 0.75rem/0.875rem로 조용하게 처리한다.
```

#### Navigation
```text
Dior 스타일 상단 네비게이션을 만들어줘.
- 높이: 4rem base, desktop 5rem
- first viewport: transparent absolute header over photography
- sticky: fixed top 0, background #FFFFFF, text/icon #33383C
- glass state: backdrop-filter blur(calc(3.125rem / 2)), radius 6px, 1rem horizontal margin
- center: Dior wordmark; left menu/back; right search/account utilities
```

### Iteration Guide

- **색상 변경 시**: gold/pink를 brand primary로 만들지 말고 #33383C charcoal을 기준으로 한다.
- **폰트 변경 시**: Atacama replacement는 heading에만 쓰고 controls는 Hellix-like sans로 분리한다.
- **여백 조정 시**: hero는 image-full, UI는 compact. 모든 섹션에 동일한 card padding을 강제하지 않는다.
- **새 컴포넌트 추가 시**: shadow를 먼저 추가하지 말고 photography, hairline, typography 순으로 구조를 만든다.
- **다크/이미지 모드**: 흰색 텍스트는 반드시 image overlay 위에 두고, pure black overlay는 alpha gradient로만 사용한다.
- **반응형**: 1033px 전후에서 desktop grid/header behavior가 바뀌는 것을 기준으로 삼는다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #33383C (`{colors.ink-primary}`) as the UI anchor for text, outlines, and contained controls.
- Let photography carry the first impression; place UI chrome over it rather than framing it in cards.
- Use Atacama VAR for editorial/category display and Hellix for functional controls.
- Preserve the heading axis feel: `"wght" 352` with tight tracking on display sizes.
- Use black alpha gradients for image legibility instead of caption boxes.
- Keep radius restrained: 4px/6px for controls, 0 for hero image portals.
- Make header states explicit: transparent, glass, sticky, and forced icon colors.
- Treat shadows as exceptions for modals/third-party surfaces, not as a general layout language.

### ❌ DON'T

- 배경을 `#FAF3E6` 또는 cream luxury tint로 두지 말 것 — Dior captured UI는 `#FFFFFF` / `#F8F8F8` / photography 기반이다.
- 텍스트를 `#000000` 또는 `black`으로 고정하지 말 것 — 기본 UI ink는 `#33383C` 사용.
- 브랜드 primary를 `#D4AF37` gold로 만들지 말 것 — 실제 UI anchor는 `#33383C`이다.
- Category label을 `#33383C`로 두지 말 것 — hero/image labels는 `#FFFFFF`가 맞다.
- Hero overlay를 flat `#000000` layer로 덮지 말 것 — `#00000000` to `#0000007F` gradient를 사용.
- Hairline을 `#CCCCCC`로 임의 대체하지 말 것 — observed structural gray는 `#D8D8D8` 계열이다.
- body 전체를 `font-weight: 500`으로 올리지 말 것 — body/control과 display axis를 분리한다.
- 모든 이미지를 rounded card로 만들지 말 것 — hero/category image portals는 radius 0에 가깝다.
- 버튼을 pill-only 시스템으로 만들지 말 것 — 기본 control radius는 4px/6px이다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- **Gold UI primary: zero** — gold는 product imagery에는 있어도, brand action color로는 absent. 메종 UI 위에 `#D4AF37`은 never 사용.
- **Decorative card chrome on hero: none** — category choice는 image portal, 진열대 사진 자체가 카드. border/shadow/label 카드 chrome은 absent.
- **Broad chromatic palette: zero** — 가장 빈도 높은 색은 neutral 다섯(#33383C / #FFFFFF / #000000 / #D8D8D8 / #7B8487). 큐레이션박스 밖 컬러 family는 absent.
- **Heavy display weights as the couture default: never** — Atacama display axis는 `wght 352` 부근. 700/900 무게는 zero.
- **Generic gradient-mesh luxury: absent** — gradient는 black alpha 가독성 레이어로만 작동. mesh decoration은 none.
- **Universal pill buttons: zero** — 999px radius는 utility에 한정, 기본 control은 4px/6px. 부티크 전체가 pill로 둘리는 일은 never.
- **Card shadows for category tiles: absent** — shadow는 modal/third-party 한정, 매장윈도우 진열대에는 zero.
- **Typed Dior wordmark replacement: never** — 로고는 SVG artwork, live text replacement는 absent.
- **12-column SaaS hero structure: none** — 첫 인상은 editorial split photography, hero copy + feature grid는 absent.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single captured homepage state** — this guide uses the existing `insane-design/dior` HTML/CSS/phase1 artifacts and one desktop/wide hero screenshot. Checkout, product detail, search overlay, account, and regional flows were not navigated live in this turn.
- **Main CSS includes third-party systems** — OneTrust, PhoneInput, Swiper, and MUI values are present. Colors such as `#468254`, `#03B2CB`, `#3860BE`, and `#C53929` are treated as utility/third-party states, not Dior brand colors.
- **Token prefix ambiguity** — `--ot-*` is the clearest tokenized layer but belongs largely to consent UI. Main Dior page styling relies on generated MUI/CSS-module classes, so frontmatter `token_prefix: ot` is a practical extraction anchor, not a complete Dior design-token namespace.
- **Mobile hero behavior not visually verified** — CSS breakpoints were present, but no fresh mobile screenshot was captured during this run. Mobile stacking/carousel behavior is inferred from CSS and should be verified before building a mobile-perfect clone.
- **Font licensing and exact metrics** — Atacama VAR and Hellix are site-hosted. Open-source substitutes are approximations and will not reproduce the Dior wordmark or variable axis metrics exactly.
- **Interaction states incomplete** — hover/focus/disabled tokens were observed, but loading/error states for Dior-native commerce forms were not fully surfaced in the homepage capture.
- **Motion JS not audited** — CSS transitions and keyframes were inspected, but scroll-triggered React/JS interaction code was not deeply analyzed.
- **Image asset color contamination** — frequency data contains photographic and SVG colors. Brand color selection deliberately prioritizes UI role and token usage over raw chromatic frequency.
