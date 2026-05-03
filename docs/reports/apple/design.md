---
schema_version: 3.2
slug: apple
service_name: Apple
site_url: https://apple.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#0071E3"
primary_font: "SF Pro Text"
font_weight_normal: 400
token_prefix: sk

bold_direction: Product Gallery
aesthetic_category: editorial-product
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: editorial-product
archetype_confidence: high
design_system_level: lv3
design_system_level_evidence: "The CSS exposes a mature --sk token family, component-level button/dotnav/paddlenav tokens, and precise typographic optical compensation."

colors:
  primary: "#0071E3"
  primary-link: "#0066CC"
  surface-canvas: "#F5F5F7"
  surface-raised: "#FFFFFF"
  text-primary: "#1D1D1F"
  text-secondary: "#6E6E73"
  text-tertiary: "#86868B"
  chrome-dark: "#161617"
  chrome-hover: "#272729"
  hairline: "rgba(0, 0, 0, 0.16)"
typography:
  display: "SF Pro Text"
  body: "SF Pro Text"
  fallback: "Helvetica Neue, Helvetica, Arial, sans-serif"
  ladder:
    - { token: display-xl, size: "56px", weight: 600, line_height: "1.071", tracking: "-0.022em" }
    - { token: display-lg, size: "48px", weight: 600, line_height: "1.083", tracking: "-0.022em" }
    - { token: headline, size: "32px", weight: 600, line_height: "1.125", tracking: "-0.01em" }
    - { token: subhead, size: "21px", weight: 400, line_height: "1.381", tracking: "0.011em" }
    - { token: body, size: "17px", weight: 400, line_height: "1.470", tracking: "0em" }
    - { token: nav, size: "12px", weight: 400, line_height: "1", tracking: "0em" }
  weights_used: [400, 500, 600]
  weights_absent: [450, 550]
components:
  button-primary: { bg: "{colors.primary}", color: "#FFFFFF", radius: "980px", padding: "11px 21px" }
  button-dark: { bg: "#1D1D1F", hover: "#272729", active: "#18181A", radius: "980px" }
  tile-icon-button: { bg: "rgba(210, 210, 215, .64)", icon: "rgba(0, 0, 0, .56)", radius: "999px" }
  dotnav: { current: "rgba(0, 0, 0, .8)", rest: "rgba(0, 0, 0, .42)", radius: "999px" }
---

# DESIGN.md — Apple

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Apple's homepage is not a generic minimalist web page. It is a product gallery where the interface keeps stepping backward until the device, headline, and one blue action remain. The page uses the browser as a showroom wall: large planes of #F5F5F7 (`{colors.surface-canvas}`), white tile surfaces, and black or near-black product bands are alternated so each product launch feels like its own exhibit. At its best, the page behaves like a museum gallery where the walls disappear; the chrome does not ask to be admired, it clears the room for the product.

The system's signature is not color abundance. The entire interactive identity concentrates into #0071E3 (`{colors.primary}`) and #0066CC (`{colors.primary-link}`), while most surfaces are carried by #FFFFFF (`{colors.surface-raised}`), #F5F5F7 (`{colors.surface-canvas}`), #1D1D1F (`{colors.text-primary}`), and #6E6E73 (`{colors.text-secondary}`). There is no second brand color waiting in the wings. Blue is a cue for action, not a decorative layer, and that restraint makes product photography do the emotional work.

Typography is engineered to look effortless. SF Pro Text appears simple until the details show: 17px body copy, 12px global navigation, 56px display moments, and display-only negative tracking around -0.022em. Body text keeps normal tracking; headlines tighten. That split is the Apple feeling: the wordmark-like headline has the density of ink placed on paper, while the paragraph copy stays breathable.

The chrome is intentionally quiet. Navigation is translucent/dark or near-white depending on context, links are small, buttons are capsule pills, and shadows almost never belong to UI containers. The page has almost no site-shaped self-consciousness; it keeps erasing its own frame and lending the stage to devices. When depth appears, it is not a card shadow. The measured `3px 5px 30px rgba(0,0,0,.22)` behaves like glass-case lighting around product photography, a controlled drop shadow inside the catalogue image rather than elevation on the interface.

### Key Characteristics

- Product-first editorial bands with one dominant visual per section.
- SF Pro Text stack with localized SF Pro variants and Helvetica fallback.
- Display headings use weight 600 plus negative optical tracking.
- Body copy centers around 17px, weight 400, and relaxed line-height.
- Interactive blue is singular: #0071E3 for focus/primary fills, #0066CC for links.
- Canvas neutrals are cool: #F5F5F7, #FFFFFF, #1D1D1F, #6E6E73.
- Pill buttons use extreme radius values such as 980px and 999px.
- UI shadows are nearly absent; product photography gets the depth.
- Navigation is low-height, low-contrast, and deliberately small.
- Component tokens use the `--sk-*` family with button, fill, glyph, dotnav, paddlenav, and tile aliases.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Product Gallery
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **hero-scale product photography, single-blue interaction, and optical SF Pro typography**으로 기억된다.
> **Code Complexity**: high — mature token families, localized font stacks, component aliases, state tokens, and optical typography rules make the system harder than its visual minimalism suggests.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Apple처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "SF Pro Text", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  font-size: 17px;
  font-weight: 400;
  line-height: 1.47059;
  letter-spacing: 0;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #F5F5F7; --fg: #1D1D1F; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #0071E3; --link: #0066CC; }
a { color: var(--link); }
.button { background: var(--brand); color: #FFFFFF; border-radius: 980px; }
```

**절대 하지 말아야 할 것 하나**: Apple을 "흰 배경 + 검은 텍스트 + 아무 파란 버튼"으로 단순화하지 말 것. 핵심은 #F5F5F7 canvas, 17px SF Pro body, display-only tracking, 그리고 제품 사진 전용 깊이감이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://apple.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | phase1 reuse from `insane-design/apple/` |
| HTML size | 250329 bytes |
| CSS files | 8 external CSS files, total 679498 chars measured |
| Token prefix | `sk` |
| Method | Existing phase1 JSON + CSS token/frequency summaries; no HTML report render step |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Apple marketing stack with static/SSR HTML and large compiled CSS bundles.
- **Design system**: Apple `--sk-*` token layer, plus `--globalnav-*`, `--localnav-*`, `--footer-*`, and gallery-specific aliases.
- **CSS architecture**:
  ```text
  core       (--sk-fill-*, --sk-glyph-*, --sk-focus-*)       semantic base values
  action     (--sk-button-*, --sk-tile-button-*)             interactive state aliases
  component  (--r-globalnav-*, --r-localnav-*)               component-level behavior
  product    home/gallery CSS bundles                         page-specific layout
  ```
- **Class naming**: Apple component prefixes (`ac-`, `sk-`, `r-`) rather than BEM-style product app classes.
- **Default theme**: mixed; homepage alternates light product tiles, dark hero bands, and neutral global/footer surfaces.
- **Font loading**: system/local SF Pro stack with localized SF Pro variants; fallback to Helvetica Neue, Helvetica, Arial.
- **Canonical anchor**: homepage hero and product tile system; not the internal app UI.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `SF Pro Text` / localized SF Pro variants.
- **Code font**: N/A; homepage CSS does not expose a meaningful code typography surface.
- **Weight normal / bold**: `400` / `600`.

```css
:root {
  --sk-font-family: "SF Pro Text", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  --sk-font-family-code: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --sk-font-weight-normal: 400;
  --sk-font-weight-bold: 600;
}
body {
  font-family: var(--sk-font-family);
  font-weight: var(--sk-font-weight-normal);
}
```

### Note on Font Substitutes

- **Primary substitute** — use `Inter` only as a last-resort structural fallback, not as an aesthetic replacement. Set body at 17px / 400 / 1.47 and reduce display tracking to about `-0.018em` to avoid over-tightening.
- **Closer open-source fallback** — `Geist` or `Roboto Flex` can approximate the neutral grotesk quality better than default Arial. Use weight 400 for body and 600 for display; avoid 500 unless matching a real token.
- **Localized stacks** — preserve platform CJK fallbacks when localizing: PingFang for Chinese, Hiragino/Meiryo for Japanese, and Apple Gothic/Malgun Gothic for Korean. The phase1 CSS exposes many localized SF Pro stacks, so replacing all of them with one Latin-only family will break density.
- **Icon font** — `SF Pro Icons` is part of the stack. If unavailable, use inline SVG or a local icon font with matching optical weight; do not let missing icon glyphs inherit a text font.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| display-xl | 56px | 600 | ~1.07 | -0.022em |
| display-lg | 48px | 600 | ~1.08 | -0.022em |
| headline | 40px | 600 | ~1.10-1.20 | -0.01em to -0.022em |
| tile-title | 32px | 600 | 1.125 | -0.01em |
| subhead | 21px | 400 | ~1.38 | 0.011em |
| body-large | 19px | 400 | ~1.42 | 0.012em |
| body | 17px | 400 | ~1.47 | 0em |
| nav | 12px | 400 | 1 | 0em |

> ⚠️ Apple typography is not "just system-ui". The measured CSS is dominated by 17px body text, 12px navigation, weight 400/600, and display-only negative tracking.

### Principles

1. Body starts at 17px, not 16px. This is the base density of Apple marketing copy.
2. Display text tightens; body text does not. Use `-0.022em` on large headings and `0em` on normal copy.
3. Weight 600 is the display voice. Weight 400 is the reading voice. Weight 500 appears rarely and should not become the default.
4. Navigation is intentionally small at 12px, but its low contrast and spacing make it feel precise rather than cramped.
5. SF Pro localized stacks are part of the design system, not an implementation footnote.
6. Line-height ratios are fractional and optical; rounding everything to `1.2` or `1.5` changes the rhythm.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed blue family)

| Token | Hex | Use |
|---|---|---|
| `--sk-focus-color` | `#0071E3` | focus outline and canonical primary blue |
| `--sk-fill-blue` | `#0071E3` | primary fills |
| link blue | `#0066CC` / `#06C` | body links and shop links |
| blue hover/dark-page link | `#2997FF` | dark footer/block links |
| frequency candidate | `#006EDB` | high-frequency chromatic CSS candidate |
| frequency candidate | `#0076DF` | high-frequency chromatic CSS candidate |
| hover/action blue | `#0077ED` | observed single-step action variant |

### 06-2. Brand Dark Variant

| Token | Hex | Use |
|---|---|---|
| dark link | `#2997FF` | links on dark footer or dark surface |
| focus alt | `#FFFFFF` | focus/color alternative on dark surfaces |

### 06-3. Neutral Ramp

| Step | Light | Dark / text |
|---|---|---|
| page canvas | `#F5F5F7` | `#161617` |
| raised tile | `#FFFFFF` | `#1D1D1F` |
| local nav surface | `#FAFAFC` | `#161617` |
| subtle fill | `#E8E8ED` | `#333336` |
| hairline/tile controls | `#D2D2D7` | rgba black/white alpha |
| primary text | `#1D1D1F` | rgba white `.92` |
| secondary text | `#6E6E73` | rgba white `.56` |
| tertiary text | `#86868B` | rgba white `.48` |

### 06-4. Accent Families

| Family | Key step | Hex / value |
|---|---|---|
| Green | `--sk-fill-green` | `rgb(3, 161, 14)` |
| Environmental green | `--sk-enviro-green` | `rgb(0, 217, 89)` |
| Orange | `--sk-fill-orange` | `rgb(245, 99, 0)` |
| Red | `--sk-fill-red` | `rgb(227, 0, 0)` |
| Yellow | `--sk-fill-yellow` | `rgb(255, 224, 69)` |
| Product Red | `--sk-productred` | `rgb(175, 30, 45)` |

### 06-5. Semantic

| Token | Hex / value | Usage |
|---|---|---|
| `--sk-body-background-color` | `rgb(255, 255, 255)` | body/surface default |
| `--sk-body-text-color` | `rgb(29, 29, 31)` | main copy |
| `--sk-body-link-color` | `rgb(0, 102, 204)` | default links |
| `--sk-headline-text-color` | `rgb(29, 29, 31)` | headline text |
| `--sk-glyph-gray-secondary` | `rgb(110, 110, 115)` | muted glyph/text |
| `--footer-background` | `rgb(245, 245, 247)` | global footer surface |
| `--globalnav-background` | `rgba(0, 0, 0, .8)` | dark global nav |
| `--localnav-background` | `rgb(250, 250, 252)` | local nav surface |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--sk-fill` | `rgb(255, 255, 255)` | raised fills |
| `--sk-fill-secondary` | `rgb(250, 250, 252)` | secondary surface |
| `--sk-fill-tertiary` | `rgb(245, 245, 247)` | page/section neutral |
| `--sk-glyph-gray` | `rgb(29, 29, 31)` | primary glyph |
| `--sk-glyph-gray-secondary` | `rgb(110, 110, 115)` | secondary glyph |
| `--sk-button-background-hover` | `#272729` | dark button hover |
| `--sk-button-background-active` | `#18181A` | dark button active |
| `--sk-tile-button-background` | `rgba(210, 210, 215, .64)` | product tile circular control |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency |
|---|---|---:|
| frequency candidate | `#006EDB` | 34 |
| frequency candidate | `#0076DF` | 33 |
| primary/focus | `#0071E3` | 28 |
| dark hover | `#272729` | 24 |
| dark active | `#18181A` | 24 |
| subtle neutral | `#EDEDF2` | 19 |
| globalnav/search dark text | `#333336` | 13 |
| black shorthand | `#000` | 12 |
| white shorthand | `#FFF` | 8 |
| fill gray quaternary | `#E8E8ED` | 8 |
| page canvas | `#F5F5F7` | 7 |
| muted glyph | `#6E6E73` | 7 |
| tertiary glyph | `#86868B` | 6 |
| primary text | `#1D1D1F` | 4 |

### Color Stories
<!-- §06-8 -->

**`{colors.primary}` (#0071E3)** — Apple's interaction blue. It is used as focus color and primary fill, but it does not flood backgrounds. The page feels Apple because blue is scarce and therefore decisive.

**`{colors.surface-canvas}` (#F5F5F7)** — the showroom floor. Footer, buy strip, and neutral sections lean on this cool gray so white tiles and product renders can separate without decorative borders.

**`{colors.text-primary}` (#1D1D1F)** — near-black, never pure typographic black as the main editorial voice. It keeps dense SF Pro headings softer than #000000.

**`{colors.text-secondary}` (#6E6E73)** — muted product-copy gray. It carries captions, secondary nav/search hints, and lower-priority copy without introducing a second brand color.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| nav-height | ~44px | global navigation chrome |
| small-inline | 8px-12px | nav/link/button internal gaps |
| button-x | 21px-22px | pill CTA horizontal padding |
| tile-gap | 12px-24px | product tile and gallery control spacing |
| section-air | 64px-80px | headline-to-content breathing room |
| editorial-band | 96px-128px | hero/product band vertical room |
| content-max | ~980px-1068px | centered content and product message width |

**주요 alias**:
- `--r-localnav-actions-button-space-before` → local navigation action gap.
- `--media-gallery-button-margin-top` → gallery button/control spacing.
- `--sk-button-padding-horizontal` → CTA horizontal optical padding.

### Whitespace Philosophy

Apple spacing is not a generic 4/8/16 ladder. The small scale exists inside chrome, but the page's identity comes from larger editorial breaths: product bands that give the headline its own air before the product image takes over.

The layout repeatedly uses "single object, lots of silence". Adjacent content is not packed to prove density; it is isolated so each product message can land as a launch moment. When recreating this, prioritize vertical air above the headline and around the image before adding extra cards or explanatory copy.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| pill CTA | 980px | primary/secondary rounded buttons |
| circle control | 999px | tile icon buttons, dotnav/paddlenav controls |
| small chip/card | 8px | compact UI surfaces |
| tile radius | 10px-12px | product cards and neutral containers |
| focus/indicator micro | 1.2px-1.3em | small internal indicators |
| none | 0px | page bands, most structural containers |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| product-depth | `3px 5px 30px rgba(0,0,0,.22)` | product imagery only |
| chrome | `none` | nav, most buttons, tiles, footers |
| card elevation | `none` or surface contrast | Apple's marketing page usually separates by surface and image, not shadow |

Apple's shadow rule is a negative rule: do not invent elevation for UI chrome. Depth belongs to the object being sold.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| color state | short fade | button/link hover and active color shifts |
| gallery progress | alpha-based state | dotnav/progress indicator |
| transform motion | minimal / unconfirmed | not part of the extracted token evidence |

Motion was not fully instrumented in this pass. Treat Apple motion as restrained and state-driven unless a specific product page proves otherwise.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: approximately 980px-1068px for product editorial copy.
- **Grid type**: centered editorial bands plus product tile/gallery grids.
- **Column count**: homepage alternates full-width hero, paired promos, and carousel/gallery modules.
- **Gutter**: tight inside product tile systems, generous between editorial bands.

### Hero

- **Pattern Summary**: full-width product band + centered headline + product photography/video + sparse CTA.
- Layout: centered editorial stack, product image as dominant object.
- Background: `#F5F5F7`, `#FFFFFF`, or dark product-led band depending on campaign.
- **Background Treatment**: solid surface or product media; no decorative abstract gradient mesh.
- H1: 48px-56px / weight `600` / tracking `-0.022em`.
- Max-width: about 980px-1068px for copy; imagery may extend wider.

### Section Rhythm

```css
section {
  padding: 64px 24px 80px;
  max-width: 1068px;
  margin-inline: auto;
}
```

### Card Patterns

- **Card background**: `#FFFFFF` on `#F5F5F7`, or dark media surface.
- **Card border**: usually none; hairline only for navigational/footer structures.
- **Card radius**: 10px-12px when tiles are visible.
- **Card padding**: enough to keep the product object dominant; avoid equal card chrome.
- **Card shadow**: none for container; product image can carry shadow.

### Navigation Structure

- **Type**: global top nav plus optional local nav.
- **Position**: top, compact, low-height.
- **Height**: about 44px global nav.
- **Background**: dark translucent `rgba(0,0,0,.8)` or light `#FAFAFC`.
- **Border**: local nav hairline using rgba black around 0.16.

### Content Width

- **Prose max-width**: narrow, centered product copy.
- **Container max-width**: roughly 1068px.
- **Sidebar width**: N/A for homepage.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | <= 734px | stacked product bands, simplified nav/menu |
| Tablet | 735px-1068px | reduced copy/image scale |
| Desktop | >= 1069px | full editorial/product layout |
| Large | >= 1440px | wider media breathing room |

### Touch Targets

- **Minimum tap size**: navigation controls should target at least 44px.
- **Button height (mobile)**: pill CTAs remain large enough for touch.
- **Input height (mobile)**: search/globalnav interactions are compact but touch-safe.

### Collapsing Strategy

- **Navigation**: global nav collapses to compact menu/search/cart behavior.
- **Grid columns**: paired promo grids stack on small screens.
- **Sidebar**: none on homepage.
- **Hero layout**: copy stays centered; product media crops/repositions.

### Image Behavior

- **Strategy**: art-directed responsive product imagery.
- **Max-width**: image may exceed text width.
- **Aspect ratio handling**: crop and focal-point control matter more than generic `object-fit: cover`.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```css
.apple-button-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 11px 21px;
  border-radius: 980px;
  background: #0071E3;
  color: #FFFFFF;
  font: 400 17px/1.176 "SF Pro Text", "Helvetica Neue", Arial, sans-serif;
}
.apple-button-dark {
  border-radius: 980px;
  background: #1D1D1F;
  color: #FFFFFF;
}
.apple-button-dark:hover { background: #272729; }
.apple-button-dark:active { background: #18181A; }
```

| Variant | Background | Text | Radius | Notes |
|---|---|---|---:|---|
| primary blue | `#0071E3` | `#FFFFFF` | 980px | canonical CTA |
| link CTA | transparent | `#0066CC` | none | text link with chevron style |
| dark utility | `#1D1D1F` | `#FFFFFF` | 980px | dark action button |
| tile circular | `rgba(210,210,215,.64)` | rgba black icon | 999px | product tile icon button |

### Badges

| Pattern | Background | Text | Radius |
|---|---|---|---:|
| system badge | `#E8E8ED` | `#424245` | pill |
| environmental | green token | dark/green text | pill |
| product availability | neutral surface | muted glyph | pill or compact label |

### Cards & Containers

Apple cards are better described as product tiles than generic cards. They use large media, flat surfaces, and minimal chrome.

```css
.apple-product-tile {
  background: #FFFFFF;
  color: #1D1D1F;
  border-radius: 12px;
  box-shadow: none;
  overflow: hidden;
}
.apple-product-tile img.product {
  filter: drop-shadow(3px 5px 30px rgba(0,0,0,.22));
}
```

### Navigation

```css
.apple-globalnav {
  height: 44px;
  background: rgba(0, 0, 0, .8);
  color: rgba(255, 255, 255, .8);
  font: 400 12px/1 "SF Pro Text", "SF Pro Icons", sans-serif;
}
.apple-localnav {
  background: #FAFAFC;
  border-bottom: 1px solid rgba(0, 0, 0, .16);
}
```

### Inputs & Forms

Observed homepage evidence is limited to globalnav search color tokens.

| Token | Value | Context |
|---|---|---|
| `--r-globalnav-search-input-placeholder-color` | `rgb(110, 110, 115)` | search placeholder |
| `--r-globalnav-search-input-value-color` | `#333336` | search text |
| search hover background | `#F5F5F7` | search suggestions/list item hover |

### Hero Section

```css
.apple-hero {
  min-height: 70vh;
  display: grid;
  place-items: center;
  text-align: center;
  background: #F5F5F7;
  color: #1D1D1F;
}
.apple-hero h1 {
  font: 600 56px/1.071 "SF Pro Text", "Helvetica Neue", Arial, sans-serif;
  letter-spacing: -0.022em;
  margin: 0;
}
.apple-hero .cta-row {
  display: flex;
  justify-content: center;
  gap: 16px;
  margin-top: 18px;
}
```

### 13-2. Named Variants

| Variant | Spec | State Notes |
|---|---|---|
| `button-primary` | `#0071E3`, white text, 980px radius, 11px 21px padding | focus uses `#0071E3`; keep blue scarce |
| `button-dark-utility` | `#1D1D1F`, white text, 980px radius | hover `#272729`, active `#18181A` |
| `link-chevron` | transparent, `#0066CC`, inline text | do not convert every link to a filled button |
| `tile-icon-circular` | `rgba(210,210,215,.64)`, 999px radius | hover alpha becomes lighter, icon opacity increases |
| `dotnav-current` | current dot `rgba(0,0,0,.8)`, rest `rgba(0,0,0,.42)` | active state is opacity, not color family |
| `localnav-bar` | `#FAFAFC`, hairline `rgba(0,0,0,.16)` | compact product-level navigation |

### Signature Micro-Specs
<!-- §13-3 -->

```yaml
apple-tight-tracking-global:
  description: "Display typography is optically tightened while body copy stays open."
  technique: "letter-spacing: -0.022em / -0.016em / -0.01em on display sizes; letter-spacing: 0em on 17px body copy"
  applied_to: ["{typography.ladder.display-xl}", "{typography.ladder.display-lg}", "{component.hero-section}"]
  visual_signature: "Headlines feel compressed and product-label precise, while paragraphs never look squeezed."

single-blue-action-system:
  description: "All action energy is concentrated into one blue fill and one blue link value."
  technique: "primary fill #0071E3 /* {colors.primary} */; link color #0066CC /* {colors.primary-link} */; no secondary action hue"
  applied_to: ["{components.button-primary}", "{components.link-chevron}", "{component.hero-section}"]
  visual_signature: "The eye finds one blue action per product moment instead of a decorative color system."

product-photography-drop-shadow:
  description: "Depth belongs to product imagery, not to generic cards or chrome."
  technique: "filter/drop-shadow or image shadow: 3px 5px 30px rgba(0,0,0,.22); card containers keep box-shadow: none"
  applied_to: ["{component.product-tile img.product}", "{component.hero-product-media}"]
  visual_signature: "Device renders look lit inside a glass catalogue case while the UI surface remains flat."

capsule-control-radius:
  description: "Buttons and tile controls become true capsules through extreme radii."
  technique: "border-radius: 980px on CTA buttons; border-radius: 999px on circular tile controls and dotnav"
  applied_to: ["{components.button-primary}", "{components.button-dark}", "{components.tile-icon-button}", "{components.dotnav}"]
  visual_signature: "Controls read as Apple hardware-adjacent pills, not ordinary rounded web buttons."

cool-neutral-showroom-field:
  description: "Cool canvas neutrals create the silent gallery field around product launches."
  technique: "background #F5F5F7 /* {colors.surface-canvas} */ with #FAFAFC localnav and #FFFFFF /* {colors.surface-raised} */ tiles"
  applied_to: ["{component.hero-section}", "{component.product-tile}", "{components.localnav-bar}"]
  visual_signature: "The page feels like a bright showroom wall rather than warm beige, pure white, or generic minimalism."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | short product promise; often noun phrase or direct product name | "iPhone", "MacBook", campaign headline |
| Primary CTA | terse action | "Learn more", "Buy" |
| Secondary CTA | link-style action with directional cue | "Watch the film", "Compare models" |
| Subheading | one benefit, no long feature paragraph | product-level value proposition |
| Tone | confident, minimal, launch-like | no dense explanatory marketing copy |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Apple-inspired core tokens */
:root {
  /* Fonts */
  --sk-font-family: "SF Pro Text", "SF Pro Icons", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  --sk-font-family-code: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --sk-font-weight-normal: 400;
  --sk-font-weight-bold: 600;

  /* Brand / interaction */
  --sk-color-brand-25:  #F5FAFF;
  --sk-color-brand-300: #2997FF;
  --sk-color-brand-500: #0071E3;
  --sk-color-brand-600: #0066CC;
  --sk-color-brand-900: #003A75;

  /* Surfaces */
  --sk-bg-page:    #F5F5F7;
  --sk-bg-raised:  #FFFFFF;
  --sk-bg-dark:    #161617;
  --sk-text:       #1D1D1F;
  --sk-text-muted: #6E6E73;
  --sk-text-soft:  #86868B;
  --sk-hairline:   rgba(0, 0, 0, 0.16);

  /* Spacing */
  --sk-space-sm:  12px;
  --sk-space-md:  24px;
  --sk-space-lg:  64px;
  --sk-space-xl:  96px;

  /* Radius */
  --sk-radius-sm:   8px;
  --sk-radius-md:   12px;
  --sk-radius-pill: 980px;
  --sk-radius-round: 999px;

  /* Craft */
  --sk-product-shadow: 3px 5px 30px rgba(0,0,0,.22);
}

body {
  margin: 0;
  background: var(--sk-bg-page);
  color: var(--sk-text);
  font-family: var(--sk-font-family);
  font-size: 17px;
  font-weight: var(--sk-font-weight-normal);
  line-height: 1.47059;
  letter-spacing: 0;
}

.apple-display {
  font-weight: var(--sk-font-weight-bold);
  letter-spacing: -0.022em;
  line-height: 1.071;
}

.apple-cta {
  border: 0;
  border-radius: var(--sk-radius-pill);
  background: var(--sk-color-brand-500);
  color: #FFFFFF;
  padding: 11px 21px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Apple-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        apple: {
          blue: '#0071E3',
          link: '#0066CC',
          canvas: '#F5F5F7',
          raised: '#FFFFFF',
          ink: '#1D1D1F',
          muted: '#6E6E73',
          soft: '#86868B',
          dark: '#161617',
        },
      },
      fontFamily: {
        sans: ['SF Pro Text', 'SF Pro Icons', 'Helvetica Neue', 'Helvetica', 'Arial', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        semibold: '600',
      },
      borderRadius: {
        tile: '12px',
        pill: '980px',
        round: '999px',
      },
      boxShadow: {
        product: '3px 5px 30px rgba(0,0,0,.22)',
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
| Brand primary | `{colors.primary}` | `#0071E3` |
| Link | `{colors.primary-link}` | `#0066CC` |
| Background | `{colors.surface-canvas}` | `#F5F5F7` |
| Raised surface | `{colors.surface-raised}` | `#FFFFFF` |
| Text primary | `{colors.text-primary}` | `#1D1D1F` |
| Text muted | `{colors.text-secondary}` | `#6E6E73` |
| Dark chrome | `{colors.chrome-dark}` | `#161617` |
| Border | `{colors.hairline}` | `rgba(0, 0, 0, 0.16)` |

### Example Component Prompts

#### Hero Section

```text
Apple homepage 스타일 히어로 섹션을 만들어줘.
- 배경: #F5F5F7 또는 product-led dark band
- H1: SF Pro Text, 56px, weight 600, line-height 1.071, letter-spacing -0.022em
- 본문: 21px 또는 17px, weight 400, #1D1D1F/#6E6E73
- CTA: #0071E3 fill, white text, 980px radius, 11px 21px padding
- 링크 CTA: #0066CC text link, filled button으로 만들지 않기
- 제품 이미지는 container shadow가 아니라 image-only shadow 사용
```

#### Product Tile

```text
Apple product tile을 만들어줘.
- 표면: #FFFFFF on #F5F5F7
- radius: 12px, border/shadow 없음
- 제목: SF Pro Text 32px/600, tracking -0.01em
- 설명: 17px/400, #6E6E73
- 제품 이미지에만 3px 5px 30px rgba(0,0,0,.22) 깊이
- circular control은 rgba(210,210,215,.64), radius 999px
```

#### Navigation

```text
Apple global navigation을 만들어줘.
- 높이: 44px
- font: SF Pro Text 12px/400
- dark surface: rgba(0,0,0,.8), text rgba(255,255,255,.8)
- light local nav: #FAFAFC with rgba(0,0,0,.16) hairline
- 링크는 작고 조용하게, CTA보다 눈에 띄지 않게
```

### Iteration Guide

- **색상 변경 시**: #0071E3과 #0066CC 외의 새 브랜드 블루를 만들지 말 것.
- **폰트 변경 시**: body 17px/400/1.47부터 맞추고 display에만 negative tracking을 적용할 것.
- **여백 조정 시**: 64px 이상의 editorial air를 먼저 확보한 뒤 내부 간격을 조정할 것.
- **새 컴포넌트 추가 시**: card chrome을 만들기보다 제품 이미지와 surface contrast로 구조를 만들 것.
- **다크 섹션**: #161617 or media-led dark band를 쓰되 blue link는 #2997FF로 올릴 것.
- **반응형**: hero copy와 product crop을 함께 설계할 것. 단순 `width:100%` 이미지는 Apple처럼 보이지 않는다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#F5F5F7` as the neutral showroom canvas and `#FFFFFF` as raised tile surface.
- Use `#1D1D1F` for primary editorial text and `#6E6E73` for secondary copy.
- Keep primary interaction concentrated in `#0071E3` and links in `#0066CC`.
- Set body copy at 17px / 400 / approximately 1.47 line-height.
- Apply negative tracking only to display/headline sizes.
- Use 980px/999px pill geometry for CTAs and circular controls.
- Let product photography carry depth; keep chrome flat.
- Preserve compact 12px global navigation.

### ❌ DON'T

- 배경을 `#FFFFFF`만으로 두지 말 것 — 대신 page canvas에는 `#F5F5F7`, raised tile에는 `#FFFFFF`를 분리해서 사용.
- 본문 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#1D1D1F` 사용.
- 보조 텍스트를 `#999999`로 두지 말 것 — 대신 `#6E6E73` 또는 `#86868B` 사용.
- primary CTA를 `#0066CC`로 채우지 말 것 — fill은 `#0071E3`, text link는 `#0066CC` 사용.
- dark hover를 임의의 `#333333`으로 두지 말 것 — measured hover는 `#272729`, active는 `#18181A`.
- body를 `font-size: 16px`로 두지 말 것 — Apple homepage density는 `17px`.
- display heading에 `font-weight: 700`을 기본으로 쓰지 말 것 — measured display voice는 주로 `600`.
- 모든 텍스트에 `letter-spacing: -0.022em`을 적용하지 말 것 — body는 `0em`, display만 tight tracking.
- card/container에 `box-shadow: 0 10px 30px rgba(0,0,0,.15)` 같은 generic elevation을 주지 말 것 — product image shadow만 `3px 5px 30px rgba(0,0,0,.22)`.
- 버튼 radius를 `8px` 또는 `12px`로 만들지 말 것 — CTA는 `980px`, circular controls는 `999px`.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Brand Gradient: none. Apple homepage interaction identity is not a gradient token system.
- Second brand color: none. Blue carries interactive meaning; product color belongs to photography and product renders.
- Warm beige/cream canvas: absent. The neutral field is cool `#F5F5F7`, not editorial parchment.
- Heavy UI elevation: absent. Shadows do not define containers.
- Decorative borders around product tiles: rare. Surface contrast and media hierarchy do the structural work.
- Body tracking compression: never. Tight tracking is a display-only optical move.
- Default 16px web body: absent from the core voice. The body system centers on 17px.
- Generic rounded rectangles: avoided. Buttons are capsules; tiles are restrained; controls are circular.
- Long explanatory marketing paragraphs: absent. Copy is launch-like and compressed.
- Rainbow accent palette: absent in core UI. Semantic red/green/orange/yellow exist, but the homepage does not become multicolor chrome.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-only scope** — this guide is based on the existing `insane-design/apple` phase1 homepage assets. Store checkout, product configurators, account flows, and support pages were not visited.
- **No fresh render pass** — Step 6 RENDER-HTML was intentionally skipped per request. Visual observations rely on phase1 artifacts and CSS summaries, not a newly rendered report.
- **Screenshots not remeasured in this pass** — screenshot files existed, but this guide does not claim pixel-perfect image crop coordinates or exact viewport-specific art direction.
- **Motion is under-specified** — CSS state values were available, but scroll-triggered animation, video behavior, and JavaScript-driven gallery timing were not instrumented.
- **Dark-mode mapping is partial** — dark surface/link values such as `#161617` and `#2997FF` are observed, but a complete dark token graph for every component is not established.
- **Form states are limited** — globalnav search tokens were observed; validation, error, loading, and checkout input states were not surfaced.
- **Frequency colors can be polluted by page-specific campaigns** — dominant chromatic candidates like `#006EDB` and `#0076DF` were kept as observed candidates, not promoted above the canonical `#0071E3`.
- **Token naming preserves observed families** — generic aliases in this document are explanatory. Implementation should prefer real `--sk-*`, `--r-globalnav-*`, `--localnav-*`, and `--footer-*` names where available.
