---
schema_version: 3.2
slug: adobe
service_name: Adobe
site_url: https://adobe.com
fetched_at: 2026-04-14T01:21:00+09:00
default_theme: mixed
brand_color: "#3B63FB"
primary_font: adobe-clean
font_weight_normal: 400
token_prefix: feds

bold_direction: Creative Marketplace
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: commerce-marketplace
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "Adobe homepage exposes a working token/component system across FED global navigation, homepage brick layout, Typekit fonts, and reusable CTA/nav states."

colors:
  brand-red: "#EB1000"
  cta-primary: "#3B63FB"
  cta-primary-hover: "#274DEA"
  nav-background: "#F8F8F8"
  popup-background: "#F3F3F3"
  page-card: "#FFFFFF"
  text-primary: "#292929"
  text-secondary: "#505050"
  border-subtle: "#EAEAEA"
  border-strong: "#DADADA"
  dark-promo: "#000000"
  focus-ring: "#507BFF"
typography:
  display: "adobe-clean-display"
  body: "adobe-clean"
  serif: "adobe-clean-serif"
  ladder:
    - { token: hero-title, size: "48px observed", weight: 700, tracking: "0" }
    - { token: nav-link, size: "14px", weight: 400, tracking: "0" }
    - { token: cta, size: "15px", weight: 700, tracking: "0" }
    - { token: description, size: "12px", weight: 400, tracking: "0" }
  weights_used: [300, 400, 500, 600, 700, 800, 900]
  weights_absent: []
components:
  cta-primary: { bg: "{colors.cta-primary}", hover: "{colors.cta-primary-hover}", radius: "16px", height: "32px", padding: "0 14px" }
  cta-secondary: { bg: "transparent", border: "2px solid {colors.border-strong}", radius: "16px", height: "32px", padding: "0 14px" }
  global-nav: { bg: "{colors.nav-background}", max_width: "1440px", position: "sticky", height: "var(--feds-height-nav)" }
  homepage-brick: { radius: "20px default / 16px large / 4px small", min_height: "450px mobile, 500px tablet+" }
---

# DESIGN.md - Adobe

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Adobe.com is not a red brand page. The red mark is a signature stamp, but the UI behaves like a broad creative marketplace: a neutral commerce shell, a dark cinematic campaign hero, and a grid of rounded promotional product tiles underneath. The operating color is Spectrum blue `#3B63FB` (`{colors.cta-primary}`), while Adobe red `#EB1000` (`{colors.brand-red}`) is reserved for identity, not for most interactions.

The homepage is built like a creative department store after the lights go down: the storefront signage is disciplined, but every display table is allowed to glow with its own product art. Global navigation stays pale and utilitarian at `#F8F8F8` (`{colors.nav-background}`), then the hero drops into a black-box campaign theater where white type and one blue pill CTA do the conversion work. Below that, the layout becomes a modular offer board: white cards, large radii, product art, short commerce copy, and bold little pill buttons.

The strongest craft is the split between quiet infrastructure and expressive content. Navigation, menus, popups, borders, and CTAs are governed by a sober FED token system; they feel like the airport concourse for a suite of creative tools, built to move many kinds of users without drama. Inside the content bricks, Adobe permits more theatrical material: gradient strips, Firefly imagery, illustrated product collages, dark panels, and big promotional offers. That contrast is the brand: enterprise-grade navigation wrapped around creative spectacle.

The site also has a very Adobe-specific hierarchy of color. Blue means action, red means brand, black means campaign theater, and white cards mean offers. `#EB1000` (`{colors.brand-red}`) behaves like a wax seal on the package, not the checkout button; the hand that asks you to buy is `#3B63FB` (`{colors.cta-primary}`). There is no second red interaction system hiding in the page.

Adobe's cards are closer to sample trays in a print shop than to SaaS feature cards. The rounded brick is the tray, the product image is the ink swatch, and the copy stays compact so the offer can be scanned quickly. Shadows mostly step aside; depth comes from radius, artwork, and the move from dark campaign theater to white commerce trays.

Pastel gradients exist, but they are compartmentalized inside nav/product affordances and individual content modules; they do not become a whole-page AI gradient wash. The page refuses the obvious "Adobe equals rainbow creative cloud" move. Color is rationed by role: red mark, blue action, neutral shell, black stage, local product gradient.

### Key Characteristics

- Red logo identity exists, but UI primary action is blue `#3B63FB`.
- Sticky global navigation uses a pale neutral shell `#F8F8F8`, not pure white chrome.
- Hero uses dark illustrated atmosphere with centered headline and a single dominant CTA.
- Homepage content is a masonry marketplace of large rounded bricks, not a linear SaaS feature stack.
- CTA pills are compact: `32px` height, `16px` radius, `0 14px` padding, `700` weight.
- Default text color is dark warm-neutral `#292929`, with secondary copy around `#505050`.
- Product/category menus use tiny icon imagery, two-column mega menu structure, and hover-caret arrows.
- Gradients are local accents for product categories or brick highlights, not the global background system.
- Focus states are explicit blue outlines (`#507BFF` / `#3860FA`), not just hover color.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Creative Marketplace
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **dark creative campaign hero inside a neutral commerce shell**으로 기억된다.
> **Code Complexity**: high — sticky FED navigation, mega menus, Typekit loading, responsive masonry bricks, commerce embeds, and localized personalization all interact on the page.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Adobe처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "adobe-clean", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #F8F8F8; --fg: #292929; }
body { background: var(--bg); color: var(--fg); }

/* 3. 액션 컬러 */
:root { --brand-action: #3B63FB; --brand-mark: #EB1000; }
.primary-cta { background: var(--brand-action); color: #FFFFFF; }
```

**절대 하지 말아야 할 것 하나**: Adobe red `#EB1000`을 모든 CTA와 링크에 뿌리지 말 것. 실제 primary CTA는 Spectrum blue `#3B63FB`이고 red는 로고/브랜드 표식에 머문다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://adobe.com` |
| Fetched | 2026-04-14T01:21:00+09:00 |
| Extractor | reused phase1 artifacts + local CSS/HTML + screenshot |
| HTML size | 80454 bytes (Adobe FED/AEM-style homepage shell) |
| CSS files | 15 external/local CSS files, including global navigation, UniversalNav, homepage brick, text, footer, Typekit |
| Token prefix | `feds` plus `alias-*`, `content-palette-*`, `icon-palette-*` |
| Method | CSS custom properties, component CSS, phase1 JSON, and hero screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Adobe FED homepage shell with AEM/Milo-style blocks, personalization manifests, commerce service embed, Typekit, and UniversalNav.
- **Design system**: FED navigation tokens plus Adobe/Spectrum semantic aliases. Prefixes include `--feds-*`, `--alias-*`, `--content-palette-*`, `--icon-palette-*`.
- **CSS architecture**:
  ```css
  :root                         /* FED nav, CTA, footer, promo, skeleton tokens */
  .global-navigation             /* sticky nav, mega menu, popup, profile, search */
  .homepage-brick                /* masonry offer cards, hero bricks, split backgrounds */
  .text-block                    /* editorial copy blocks and icon/text layouts */
  .universal-nav-container       /* app switcher/profile/notification shell */
  ```
- **Class naming**: FED/BEM hybrid (`.feds-cta--primary`, `.feds-navLink--hoverCaret`, `.homepage-brick.split-background`).
- **Default theme**: mixed. Navigation is light; hero/campaign zones may be dark; cards are mostly white.
- **Font loading**: Adobe Typekit kit `hah7vzn`, `font-display: optional`, with Adobe Clean families.
- **Canonical anchor**: homepage at `https://www.adobe.com/`, meta description "Creative, marketing and document management solutions".

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `adobe-clean-display` (Adobe Typekit licensed)
- **Body font**: `adobe-clean` (Adobe Typekit licensed)
- **Serif font**: `adobe-clean-serif` (Adobe Typekit licensed)
- **Code font**: not surfaced in homepage CSS
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --adobe-font-family: "adobe-clean", sans-serif;
  --adobe-font-family-display: "adobe-clean-display", "adobe-clean", sans-serif;
  --adobe-font-family-serif: "adobe-clean-serif", serif;
  --adobe-font-weight-normal: 400;
  --adobe-font-weight-bold: 700;
}
body {
  font-family: var(--adobe-font-family);
  font-weight: var(--adobe-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Adobe Clean** is licensed through Adobe Typekit. For an open-source substitute, use **Inter** at weight `400/700`, but tighten headline line-height slightly because Inter reads wider and more mechanical than Adobe Clean.
- **Adobe Clean Display** can be approximated with **Inter Display** or **Source Sans 3** at `800/900`; keep letter-spacing at `0` unless the implementation introduces obvious looseness at very large sizes.
- **Adobe Clean Serif** is present in the kit but not central to the observed homepage hero. If a serif moment is needed, use **Source Serif 4** only for editorial or testimonial inserts, never for nav or CTA chrome.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Hero H1 | ~48px observed in screenshot | 700 | tight, about 1.1 | 0 |
| Hero body | ~18px observed | 400 | about 1.4 | 0 |
| Nav link | 14px | 400 | 1.4 | 0 |
| Active nav link | 14px | 700 | 1.4 | 0 |
| CTA | 15px | 700 | 0 in flex-centered FED CTA | 0 |
| Menu description | 12px | 400 | normal | 0 |
| Brick heading | variable heading classes | 700 | tokenized via `--type-*` | 0 |
| Detail label | detail classes | 700 in emphasis contexts | tokenized via `--type-*` | 0 |

> ⚠️ Typography key insight: Adobe's homepage does not rely on exotic tracking. It relies on proprietary Adobe Clean families, bold commerce copy, and compact component typography.

### Principles
<!-- SOURCE: manual -->

1. Body text begins at `400`; commerce emphasis jumps directly to `700`.
2. Navigation is intentionally smaller than hero copy: `14px` nav links keep the shell quiet while product art owns attention.
3. CTA type is compact and bold (`15px`, `700`) because the button height is only `32px`.
4. Display hierarchy is image-led. The type is large and clear, but not aggressively editorial or condensed.
5. Adobe Clean Serif is available but not a default homepage voice; using it broadly would make the page feel like a magazine instead of a creative commerce hub.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed key tokens)

| Token | Hex |
|---|---|
| `--feds-color-adobeBrand` | `#EB1000` |
| `--feds-cta-primary-bg` | `#3B63FB` |
| `--feds-cta-primary-bg--hover` | `#274DEA` |
| `--feds-color-blue-link` | `#274DEA` |
| `--feds-color-link--hover` | `#1D3ECF` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--feds-background-promo--dark` | `#000000` |
| `--feds-background-cloudmenu-v2` | `#111111` |
| `--feds-color-link-dark` | `#DBDBDB` |
| dark secondary CTA hover | `#2C2C2C` |
| dark secondary CTA border | `#393939` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| page/card | `#FFFFFF` | `#000000` |
| nav | `#F8F8F8` | `#111111` |
| popup | `#F3F3F3` | `#2C2C2C` |
| hover | `#E9E9E9` | `#333333` |
| border | `#EAEAEA` / `#E1E1E1` | `#323232` / `#393939` |
| primary text | `#292929` | `#DBDBDB` |
| secondary text | `#505050` | `#C6C6C6` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Spectrum blue | default | `#3B63FB` |
| Spectrum blue | hover | `#274DEA` |
| Express violet | light/default alias | `#5258E4` / `#A7AAFF` |
| Focus blue | focus ring | `#507BFF` / `#3860FA` |
| Product category gradient | photo | `#D0E8FA` to `#CEF4F4` |
| Product category gradient | design | `#FCCBFC` to `#FFE9D0` |
| Product category gradient | AI | `#BCE3FF`, `#FFE9D3`, `#F8D5E4` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--feds-color-adobeBrand` | `#EB1000` | Adobe logo/brand label |
| `--feds-cta-primary-bg` | `#3B63FB` | primary commerce CTA |
| `--feds-cta-primary-bg--hover` | `#274DEA` | primary CTA hover |
| `--feds-background-nav` | `#F8F8F8` | sticky global nav |
| `--feds-background-popup` | `#F3F3F3` | mega menu popup |
| `--feds-borderColor` | `#EAEAEA` | nav and breadcrumb divider |
| `--feds-color-link` | `#292929` | nav/link text |
| `--feds-color-headline` | `#505050` | secondary/headline support |
| `--focus-ring` | `#507BFF` | accessible focus outline |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--alias-background-semantic-accent-default-spectrum-2` | `#3B63FB` / `#4069FD` | Spectrum accent/action |
| `--alias-background-semantic-accent-hover-spectrum-2` | `#274DEA` / `#345BF8` | Spectrum hover |
| `--alias-background-semantic-accent-default-express` | `#5258E4` / `#A7AAFF` | Express accent |
| `--alias-content-neutral-default` | `#292929` | neutral content |
| `--alias-icon-neutral-default` | `#292929` or `#DBDBDB` by theme | icon neutral |
| `--profile-cta-secondary-border` | `#DADADA` / `#393939` | secondary CTA border |

### 06-7. Dominant Colors (actual CSS frequency and role)

| Token | Hex | Frequency / role |
|---|---|---|
| neutral surface | `#FFFFFF` | primary card/surface color |
| text/link | `#292929` | main nav/content text |
| nav background | `#F8F8F8` | global navigation shell |
| popup/hover | `#F3F3F3` / `#E9E9E9` | menu surfaces and hover fills |
| border | `#EAEAEA` / `#E1E1E1` | separators |
| CTA | `#3B63FB` | primary action |
| Adobe mark | `#EB1000` | logo/brand only |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.cta-primary}` (`#3B63FB`)** — This is the true action color. It carries "See all plans" and FED primary CTA states, with `#274DEA` as the hover step. It should feel like Spectrum UI, not like the Adobe logo.

**`{colors.brand-red}` (`#EB1000`)** — Adobe red is a signature stamp. Use it for the logo/brand label and moments of identity, not as the system-wide button color.

**`{colors.nav-background}` (`#F8F8F8`)** — The navigation surface is deliberately off-white. It lets the top bar feel like quiet product infrastructure while the hero below becomes theatrical.

**`{colors.text-primary}` (`#292929`)** — Adobe avoids pure black for most UI text. The result is still high-contrast, but less harsh against the pale neutral shell and white commerce cards.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--feds-gutter` | `8px` | nav internal gutter |
| `--feds-gutter-footer` | `32px` | footer column rhythm |
| `--spacing-xxs` | observed token | tight text/brick margin |
| `--spacing-xs` | observed token | brick heading/body margin |
| `--spacing-s` | observed token | brick padding, action gaps |
| `--spacing-m` | observed token | masonry gap and section padding |
| `--spacing-l` | observed token | hero/above-pods padding |
| `--spacing-xl` | observed token | section horizontal padding |
| `--spacing-xl-static` | observed token | desktop full-grid brick top padding |

**Key aliases**:
- `--feds-maxWidth-nav` -> `1440px` for global nav and menu content.
- `--grid-container-width` -> homepage brick foreground width, observed through layout CSS.

### Whitespace Philosophy
<!-- SOURCE: manual -->

Adobe's spacing is not minimalist-gallery whitespace. It is marketplace spacing: a generous hero breath, then dense modular offer cards with enough radius and padding to keep each promotion distinct. The grid is allowed to be busy because the chrome stays restrained.

The main rhythm is "wide shell, compact components." Navigation uses `8px` gutters and `12px` link padding, CTAs use `0 14px`, while masonry sections use larger `--spacing-m` and `--spacing-xl` values. This produces a page that can sell many products without feeling like a dashboard.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--feds-radius-utilityIcon` | `4px` | profile/sign-in utility buttons |
| `.feds-cta` | `16px` | primary pill CTA |
| `.feds-cta--secondary` | `1rem` | secondary outline CTA |
| `.section.border-radius-s` | `4px` | small radius section/card variant |
| `.section.border-radius-l` | `16px` | large radius section/card variant |
| `.section.masonry default` | `20px` | default homepage brick radius |
| `.selector-popover` | `8px` | popover surface |
| `.search-input-wrapper` | `16px` | search input pill |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| popup | `0 2px 10px rgba(0 0 0 / 10%)` | selector popover |
| sign-in dropdown | `0 3px 3px 0 rgb(0 0 0 / 20%)` | account dropdown |
| hero/cards | mostly none | imagery and radius create depth |
| curtain | `background: rgb(0 0 0 / .5)` + `backdrop-filter: blur(1em)` | mobile/menu overlay depth |

Adobe avoids a heavy card-shadow system on the homepage. The cards read as product tiles through radius, white surface, artwork, and contrast against the dark/neutral page, not through layered elevation.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| caret transition | `transform 0.1s ease` | hover caret / arrow rotation affordance |
| CTA transition | `color, border-color, background-color 130ms ease-out` | primary/secondary CTA hover |
| input border | `border-color 0.2s` | search input wrapper |
| selector link | `background-color 0.2s ease` | selector/menu link hover |

Motion is short and utilitarian. Adobe's expressive energy comes from imagery and gradients, while component transitions stay below the threshold of "playful."

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: nav and menu content use `1440px`; masonry sections can reach `1920px`; hero/above-pods foreground caps around `1000px`.
- **Grid type**: CSS Grid for masonry sections; flexbox for nav, CTA rows, menu links, and utility controls.
- **Column count**: mobile `1`; tablet `2`; desktop `12` with `span 4`, `span 6`, `span 8`, and `span 12` variants.
- **Gutter**: masonry uses `var(--spacing-m)`; nav uses `8px` gutter and `12px` link padding.

### Hero

- **Pattern Summary**: dark illustrated campaign hero + centered H1 + one blue pill CTA + masonry offer cards peeking below.
- Layout: one-column centered hero above a two-card / masonry promotional board.
- Background: dark campaign illustration/photo treatment; screenshot shows navy/black gradient-like field with decorative creative assets.
- **Background Treatment**: image/illustration overlay on dark surface, not a CSS-only purple gradient.
- H1: about `48px` / weight `700` / tracking `0`.
- Max-width: centered headline block, then `1000px` style hero foreground cap for above-pods contexts.

### Section Rhythm

```css
.section.masonry:not([class*="spacing"]) {
  padding: var(--spacing-m) var(--spacing-xl);
  max-width: 1920px;
}
@media screen and (max-width: 1023px) {
  .section.masonry:not([class*="spacing"]) {
    padding: var(--spacing-s) var(--spacing-s);
  }
}
```

### Card Patterns

- **Card background**: mostly `#FFFFFF`; some dark/product campaign modules.
- **Card border**: generally none on homepage bricks; card edge comes from radius and surface contrast.
- **Card radius**: default `20px`, large `16px`, small `4px`.
- **Card padding**: `var(--spacing-s)` inside bricks; full-grid variants get larger top padding.
- **Card shadow**: none or minimal; art and background contrast carry depth.

### Navigation Structure

- **Type**: sticky global nav with hamburger/mobile wrapper, desktop mega menu, app/profile utilities, and UniversalNav overlays.
- **Position**: `position: sticky; top: 0; z-index: 10`.
- **Height**: `var(--feds-height-nav)` for topnav, plus breadcrumb/promo variants.
- **Background**: `#F8F8F8` nav, `#F3F3F3` popup.
- **Border**: `#EAEAEA` / `#E1E1E1` separators.

### Content Width

- **Prose max-width**: body-xl text observed at `840px`, heading-xxxl at `1200px`.
- **Container max-width**: nav `1440px`, masonry `1920px`, hero foreground `1000px`.
- **Sidebar width**: no persistent sidebar on homepage; mega menu columns replace sidebar behavior.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Tiny | `320px max` | ultra-small adjustment threshold |
| Mobile | `599px max` / `600px min` | single-column bricks, column CTA stack, mobile artwork |
| Tablet | `600px-1199px` | two-column masonry, tablet-specific imagery |
| Nav/Desktop | `900px min` | desktop nav link padding and active underline behavior |
| Desktop | `1200px min` | 12-column masonry, desktop artwork, centered above-pods |
| Wide | `1504px min` | wider nav/footer shell behavior |

### Touch Targets

- **Minimum tap size**: validator found `min_height_44px: true`, though individual visual affordances include smaller decorative caret dimensions.
- **Button height (mobile)**: primary FED CTA `32px`; overflowed nav CTA `30px`; mobile nav rows rely on padding for tap area.
- **Input height (mobile)**: search input wrapper `32px`.

### Collapsing Strategy

- **Navigation**: hamburger wrapper below desktop thresholds, with fixed curtain overlay and expanded vertical nav.
- **Grid columns**: `1` column mobile, `2` columns tablet, `12`-column span system desktop.
- **Sidebar**: none; menu columns collapse into the mobile nav wrapper.
- **Hero layout**: centered text remains; action area stacks on mobile and becomes row-aligned at `600px+`.

### Image Behavior

- **Strategy**: responsive `mobileOnly`, `tabletOnly`, `desktopOnly` assets; background images use `object-fit: cover`.
- **Max-width**: product art inside stacked bricks uses max-height constraints (`238px`, `292px`, `308px`) rather than full free scaling.
- **Aspect ratio handling**: CSS switches between absolute backgrounds and static stacked images.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA (`.feds-cta.feds-cta--primary`)**

| Property | Value |
|---|---|
| height | `32px` |
| min-width | `72px` |
| padding | `0 14px` |
| border | `2px solid #3B63FB` |
| radius | `16px` |
| font | `15px`, weight `700` |
| background | `#3B63FB` |
| hover background | `#274DEA` |

```html
<a class="feds-cta feds-cta--primary" href="/creativecloud/plans.html">View plans and pricing</a>
```

**Secondary CTA (`.feds-cta.feds-cta--secondary`)**

| Property | Value |
|---|---|
| background | transparent |
| border | `.125rem solid #DADADA` |
| radius | `1rem` |
| color | `#292929` |
| hover | border `#C6C6C6`, background `#E9E9E9` |
| focus-visible | outline `2px solid #507BFF` |

### Badges

No standalone badge system was central in the observed homepage capture. Detail labels inside bricks behave like compact labels using `detail-*` type classes and bold uppercase-like commerce copy.

### Cards & Containers

**Homepage brick**

| Property | Value |
|---|---|
| selector | `.homepage-brick` |
| position | `relative` |
| default min-height | `450px`, then `500px` at `600px+` |
| default radius | `20px` in masonry sections |
| background | `#FFFFFF`, `#EDEDED`, dark campaign, or product image |
| foreground | `z-index: 2`, max-width `var(--grid-container-width)` |
| hover | clickable bricks underline internal click link; mashup hover can invert outline button |

### Navigation

**Global nav**

| Property | Value |
|---|---|
| selector | `header.global-navigation` |
| position | `sticky` |
| background | `#F8F8F8` |
| max-width | `1440px` topnav |
| nav link | `14px`, `400`, `#292929` |
| active | weight `700` + `2px` underline |
| popup | `#F3F3F3` |
| curtain | `rgb(0 0 0 / .5)` + `backdrop-filter: blur(1em)` |

### Inputs & Forms

**Search input wrapper**

| Property | Value |
|---|---|
| background | `#FFFFFF` |
| border | `2px solid #DADADA` |
| radius | `16px` |
| padding | `0 14px` |
| height | `32px` |
| transition | `border-color 0.2s` |
| input | transparent background, border none, full width |

### Hero Section

Hero is campaign-first: centered headline, dark creative backdrop, one primary blue CTA, then product/offer cards. The key is not a two-column SaaS mockup; it is a large theatrical intro that immediately hands off to a commerce grid.

### 13-2. Named Variants

**button-primary-spectrum**

| Property | Value |
|---|---|
| base | `#3B63FB` fill, white text |
| hover | `#274DEA` fill |
| radius | `16px` |
| height | `32px` |
| use | plan/pricing CTA, hero primary action |

**button-secondary-outline**

| Property | Value |
|---|---|
| base | transparent, `#DADADA` border, `#292929` text |
| hover | `#E9E9E9` bg, `#C6C6C6` border |
| dark | `#393939` border, `#DBDBDB` text |
| use | Learn more, Buy now, secondary promo actions |

**homepage-brick-white-offer**

| Property | Value |
|---|---|
| surface | `#FFFFFF` |
| radius | `20px` default masonry |
| content | bold heading, body copy, pill CTA, product art |
| use | Creative Cloud/Firefly offer tiles |

**nav-product-gradient-link**

| Property | Value |
|---|---|
| radius | `4px` |
| font | `600` |
| examples | photo, design, 3D, PDF, video, AI gradients |
| use | product category emphasis inside mega menu |

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
fed-neutral-commerce-shell:
  description: "The enterprise navigation layer stays pale and tokenized while the content below becomes expressive."
  technique: "header.global-navigation { position: sticky; background-color: #F8F8F8; z-index: 10; } with 1440px max topnav and #F3F3F3 popup surfaces"
  applied_to: ["{component.global-nav}", "mega-menu", "utility-profile-app-switcher"]
  visual_signature: "a quiet product-suite shell that can contain many creative offers without looking chaotic"

spectrum-blue-action-red-seal:
  description: "Adobe red is identity; Spectrum blue is the commerce action."
  technique: "--feds-color-adobeBrand: #EB1000 separated from --feds-cta-primary-bg: #3B63FB and --feds-cta-primary-bg--hover: #274DEA"
  applied_to: ["brand-mark", "{component.cta-primary}", "plan-pricing-actions"]
  visual_signature: "the page reads unmistakably Adobe without turning every button into the logo color"

masonry-brick-offer-board:
  description: "Promotions become chunky rounded offer bricks rather than flat SaaS feature cards."
  technique: "desktop repeat(12, 1fr) masonry with span 4/6/8/12 variants, 20px default brick radius, and 450px mobile / 500px tablet+ minimum heights"
  applied_to: ["{component.homepage-brick}", "product-promotion-modules", "offer-board-sections"]
  visual_signature: "a modular creative storefront where each product tile feels like its own display tray"

local-product-gradient-links:
  description: "Gradients are localized to product/category affordances instead of becoming the page background."
  technique: "4px radius category links with 600-weight labels and observed product gradients such as #D0E8FA to #CEF4F4, #FCCBFC to #FFE9D0, and AI accents #BCE3FF / #FFE9D3 / #F8D5E4"
  applied_to: ["{component.nav-product-gradient-link}", "product-category-menu-items"]
  visual_signature: "small color swatches point to creative product families while the surrounding chrome remains neutral"

curtain-blur-overlay:
  description: "Mobile and menu overlays use a dimmed blurred curtain instead of a plain drawer backdrop."
  technique: "background: rgb(0 0 0 / .5); backdrop-filter: blur(1em);"
  applied_to: [".feds-curtain", "mobile-nav-overlay", "expanded-menu-state"]
  visual_signature: "opened navigation feels like a modal system laid over the marketplace, not just a collapsed list"
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Broad, creator-inclusive promise | "Everything you need to make anything." |
| Primary CTA | Direct commerce action | "See all plans" |
| Secondary CTA | Learn/buy verbs with compact wording | "Buy now", "Learn more" |
| Subheading | Plain explanation of product scope | "Bring any idea to life with products for creators, businesses, and beyond." |
| Tone | confident, commercial, creator-facing, not playful startup slang | product categories and offers are literal |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Adobe homepage-inspired tokens - copy into your root stylesheet */
:root {
  /* Fonts */
  --adobe-font-family: "adobe-clean", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --adobe-font-family-display: "adobe-clean-display", "adobe-clean", sans-serif;
  --adobe-font-weight-normal: 400;
  --adobe-font-weight-bold: 700;

  /* Brand and action */
  --adobe-color-brand-red: #EB1000;
  --adobe-color-action: #3B63FB;
  --adobe-color-action-hover: #274DEA;
  --adobe-color-focus: #507BFF;

  /* Surfaces */
  --adobe-bg-nav: #F8F8F8;
  --adobe-bg-popup: #F3F3F3;
  --adobe-bg-card: #FFFFFF;
  --adobe-bg-card-muted: #EDEDED;
  --adobe-bg-dark: #000000;
  --adobe-bg-cloudmenu: #111111;

  /* Text and borders */
  --adobe-text: #292929;
  --adobe-text-muted: #505050;
  --adobe-text-darkmode: #DBDBDB;
  --adobe-border: #EAEAEA;
  --adobe-border-strong: #DADADA;

  /* Layout */
  --adobe-nav-max-width: 1440px;
  --adobe-section-max-width: 1920px;
  --adobe-hero-content-max-width: 1000px;
  --adobe-gutter: 8px;
  --adobe-card-gap: 24px;

  /* Radius */
  --adobe-radius-utility: 4px;
  --adobe-radius-popover: 8px;
  --adobe-radius-cta: 16px;
  --adobe-radius-brick: 20px;
}

.adobe-cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 72px;
  height: 32px;
  padding: 0 14px;
  border: 2px solid var(--adobe-color-action);
  border-radius: var(--adobe-radius-cta);
  background: var(--adobe-color-action);
  color: #FFFFFF;
  font: 700 15px/1 var(--adobe-font-family);
  transition: color 130ms ease-out, border-color 130ms ease-out, background-color 130ms ease-out;
}

.adobe-cta:hover {
  background: var(--adobe-color-action-hover);
  border-color: var(--adobe-color-action-hover);
}

.adobe-brick {
  position: relative;
  min-height: 450px;
  border-radius: var(--adobe-radius-brick);
  background: var(--adobe-bg-card);
  color: var(--adobe-text);
  overflow: hidden;
}

@media (min-width: 600px) {
  .adobe-brick { min-height: 500px; }
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js - Adobe-inspired
module.exports = {
  theme: {
    extend: {
      colors: {
        adobe: {
          red: '#EB1000',
          action: '#3B63FB',
          actionHover: '#274DEA',
          nav: '#F8F8F8',
          popup: '#F3F3F3',
          text: '#292929',
          muted: '#505050',
          border: '#EAEAEA',
          borderStrong: '#DADADA',
          dark: '#000000',
        },
      },
      fontFamily: {
        sans: ['adobe-clean', 'Inter', 'system-ui', 'sans-serif'],
        display: ['adobe-clean-display', 'adobe-clean', 'sans-serif'],
      },
      borderRadius: {
        adobeUtility: '4px',
        adobeCta: '16px',
        adobeBrick: '20px',
      },
      maxWidth: {
        adobeNav: '1440px',
        adobeSection: '1920px',
        adobeHero: '1000px',
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
| Brand mark | `{colors.brand-red}` | `#EB1000` |
| Primary action | `{colors.cta-primary}` | `#3B63FB` |
| Primary hover | `{colors.cta-primary-hover}` | `#274DEA` |
| Background/nav | `{colors.nav-background}` | `#F8F8F8` |
| Card surface | `{colors.page-card}` | `#FFFFFF` |
| Text primary | `{colors.text-primary}` | `#292929` |
| Text muted | `{colors.text-secondary}` | `#505050` |
| Border | `{colors.border-subtle}` | `#EAEAEA` |
| Focus | `{colors.focus-ring}` | `#507BFF` |

### Example Component Prompts

#### Hero Section

```text
Adobe homepage style hero section을 만들어줘.
- 상단 nav는 #F8F8F8, 1440px max-width, sticky 구조
- hero 배경은 dark creative campaign image/illustration 느낌, CSS-only purple gradient 금지
- H1은 adobe-clean-display 계열, 약 48px, weight 700, white
- subtitle은 white, 18px 정도
- primary CTA는 #3B63FB 배경, #274DEA hover, 32px height, 16px radius, 700 weight
- hero 아래에는 흰색 20px radius offer brick 일부가 보이게 배치
```

#### Card Component

```text
Adobe homepage offer brick을 만들어줘.
- surface: #FFFFFF, radius: 20px, shadow 거의 없음
- min-height: 450px mobile / 500px tablet+
- headline: #292929, weight 700
- body: #292929 or #505050, line-height 1.4-1.5
- CTA는 outline pill 또는 Spectrum blue primary pill
- product art가 시각적 에너지를 담당하고 card chrome은 조용하게 유지
```

#### Navigation

```text
Adobe FED-style global navigation을 만들어줘.
- sticky top nav, background #F8F8F8, border #EAEAEA
- max-width 1440px, nav links 14px weight 400
- active link은 700 weight + 2px underline
- mega menu popup은 #F3F3F3 surface
- hover caret은 6px arrow, transform 0.1s ease
- logo red #EB1000은 brand mark에만 사용
```

### Iteration Guide

- **색상 변경 시**: CTA는 `#3B63FB` 계열을 유지하고, Adobe red `#EB1000`은 identity-only로 제한한다.
- **폰트 변경 시**: Adobe Clean 대체는 Inter/Source Sans 3로 하되 body `400`, CTA/headline `700` 구조를 유지한다.
- **카드 추가 시**: 20px brick radius, minimal/no shadow, product art 중심 구조를 유지한다.
- **메뉴 추가 시**: nav는 pale neutral, popup은 `#F3F3F3`, hover fill은 `#E9E9E9`를 쓴다.
- **다크 섹션 추가 시**: black/navy campaign zone은 허용하지만 전체 사이트를 dark app처럼 바꾸지 않는다.
- **반응형**: masonry는 1 -> 2 -> 12-column span 구조를 따른다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#3B63FB` as the primary action color and `#274DEA` as the hover step.
- Keep Adobe red `#EB1000` as a brand mark, not a general interface fill.
- Use `#F8F8F8` for the sticky nav shell and `#F3F3F3` for mega menu surfaces.
- Build homepage content as rounded commerce bricks with product artwork and short bold offer copy.
- Use compact pill CTAs: `32px` height, `16px` radius, `0 14px`, weight `700`.
- Preserve explicit focus outlines with `#507BFF` or dark-mode `#3860FA`.
- Let imagery and product art create energy; keep component chrome restrained.
- Use responsive asset switching (`mobileOnly`, `tabletOnly`, `desktopOnly`) for product art.

### ❌ DON'T

- CTA 배경을 `#EB1000`으로 두지 말 것 — 대신 primary action은 `#3B63FB` 사용.
- CTA hover를 `#EB1000` 또는 `#FF0000`로 두지 말 것 — 대신 `#274DEA` 사용.
- nav 배경을 `#FFFFFF` 순백으로 두지 말 것 — 대신 `#F8F8F8` 사용.
- popup/mega menu 배경을 `#FFFFFF`로 두지 말 것 — 대신 `#F3F3F3` 사용.
- 본문 텍스트를 `#000000` pure black으로 두지 말 것 — 대신 `#292929` 사용.
- subtle border를 `#CCCCCC` 같은 generic gray로 두지 말 것 — 대신 `#EAEAEA` 또는 `#E1E1E1` 사용.
- primary CTA radius를 `8px` 카드형 버튼으로 낮추지 말 것 — Adobe CTA는 `16px` pill이다.
- homepage brick radius를 `8px` SaaS card처럼 만들지 말 것 — 기본 masonry brick은 `20px`다.
- 모든 카드를 heavy shadow로 띄우지 말 것 — Adobe homepage는 shadow보다 surface/radius/artwork로 구분한다.
- hero를 보라색 AI gradient `#667EEA` to `#764BA2`로 만들지 말 것 — 실제 hero는 dark creative artwork/campaign image treatment다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- **Red-as-CTA system: none** — Adobe red is not the homepage's interaction system.
- **Whole-page gradient wash: absent** — gradients are local product/menu accents, not the page background.
- **Heavy elevation card stack: absent** — offer cards rely on radius, surface, and artwork.
- **Generic 3-card SaaS section: absent** — homepage is a marketplace masonry, not "hero + three features."
- **Rounded 8px SaaS buttons: absent** — CTAs are compact 16px pills.
- **Pure black default text: avoided** — `#292929` is the practical UI ink.
- **Single-product minimalism: absent** — Adobe intentionally shows many product paths and offers.
- **Over-animated components: absent** — transitions are short (`0.1s`, `130ms`, `0.2s`) and utilitarian.
- **Serif-led brand voice: absent** — Adobe Clean Serif exists, but homepage chrome is sans-led.
- **Border-heavy cards: absent** — card boundaries are not drawn like dashboard panels.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage snapshot is from reused phase1 artifacts** — fetch timestamp is April 14, 2026 local artifact time, not a fresh May 3, 2026 crawl.
- **Single URL scope** — analysis covers `https://adobe.com` homepage artifacts, not Creative Cloud product pages, Acrobat checkout, account settings, or logged-in surfaces.
- **Personalization can change the hero** — HTML includes personalization and scheduled campaign manifests. The screenshot captures one campaign state, not every regional/temporal variant.
- **Exact type scale tokens are partially opaque** — typography extractor found families and weights, but not a full `--type-*` scale map. Some H1/body sizes are visual observations from the screenshot and CSS context.
- **CSS token aliases include light/dark collisions** — `--alias-*` values differ by UniversalNav theme. Where collisions exist, this guide records the observed role and notes the theme dependency.
- **Commerce widgets are not deeply parsed** — `mas-commerce-service` and store iframe preload behavior were observed in HTML, but their internal UI tokens were not crawled.
- **Motion JavaScript not analyzed** — CSS transitions were captured; scroll-triggered or personalization-driven JS animations were not executed in this pass.
- **Logo/product SVG colors can pollute frequency** — product icons and menu gradients include many chromatic colors; they are treated as content/product accents, not core UI palette.
- **Mobile visual screenshot not collected in this pass** — responsive behavior is inferred from CSS and phase1 `responsive.json`, not a separate mobile screenshot.
