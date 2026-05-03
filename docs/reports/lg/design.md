---
schema_version: 3.2
slug: lg
service_name: LG Electronics
site_url: https://www.lg.com/kr/
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: light
brand_color: "#EA1917"
primary_font: LGEI Headline
font_weight_normal: 400
token_prefix: lg

bold_direction: Warm Commerce
aesthetic_category: editorial-product
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: editorial-product
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "AEM component classes, repeated LG font families, repeated button/card/nav classes, and shared breakpoint system are present; named CSS custom properties are mostly absent."

colors:
  brand-red: "#EA1917"
  brand-heritage: "#A50034"
  surface-base: "#FFFFFF"
  surface-warm: "#F0ECE4"
  surface-soft: "#F6F6F6"
  hairline-warm: "#CBC8C2"
  text-primary: "#000000"
  text-secondary: "#333333"
  text-muted: "#646464"
  text-disabled: "#BBBBBB"
  dark-surface: "#4A4946"

typography:
  display: "LGEI Headline"
  body: "LGEI Text"
  fallback: "Segoe UI, Microsoft Sans Serif, sans-serif"
  ladder:
    - { token: display-xl, size: "5rem", weight: 600, line_height: "5rem", tracking: "-.08rem" }
    - { token: display-lg, size: "3.5rem", weight: 600, line_height: "3.75rem", tracking: "-.0625rem" }
    - { token: title-md, size: "2rem", weight: 600, line_height: "2.25rem", tracking: "-.015rem" }
    - { token: body, size: "1rem", weight: 400, line_height: "1.5rem", tracking: "0" }
    - { token: caption, size: ".875rem", weight: 400, line_height: "1.25rem", tracking: "0" }
  weights_used: [300, 400, 500, 550, 600, 700, 800]
  weights_absent: [200, 900]

components:
  button-primary-red: { bg: "{colors.brand-red}", color: "{colors.surface-base}", radius: "1.75rem", padding: ".75rem 1.25rem" }
  button-outline-warm: { bg: "{colors.surface-base}", border: "1px solid {colors.text-muted}", radius: "1.75rem", padding: ".75rem 1.25rem" }
  nav-global: { bg: "{colors.surface-base}", border: "1px solid {colors.hairline-warm}", height: "desktop sticky shell" }
  card-soft-commerce: { bg: "{colors.surface-soft}", radius: "1.25rem", shadow: "0 .5rem .75rem rgba(0,0,0,.06)" }
---

# DESIGN.md — LG Electronics (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

LG's current web shell is not a minimal technology brochure. It behaves like a warm appliance showroom built on a heavy AEM component system: cream separators, rounded product cards, practical navigation, and a red action layer that appears when a choice needs urgency. The page wants electronics to feel domestic before they feel technical; the chrome is the store floor, not the spectacle.

The palette is mostly black, white, and warm beige, like a white goods aisle lit by softer domestic light rather than a cold SaaS console. The important accent is #EA1917 (`{colors.brand-red}`), used for hover/action states, while the older LG heritage magenta #A50034 (`{colors.brand-heritage}`) remains a secondary brand memory rather than the dominant UI engine. There is no second brand color competing for conversion. The hairline color #CBC8C2 (`{colors.hairline-warm}`) is crucial: it works like the seam between showroom tiles, barely noticed until it is replaced by a colder gray and the whole room becomes wrong.

Typography is a branded corporate system rather than a generic web stack. `LGEI Headline` and `LGEI Text` sit above `Segoe UI` and `Microsoft Sans Serif`, with 600 used aggressively for headings and 400 for body copy. The interesting detail is not exotic type; it is optical restraint: small negative tracking appears on large display sizes, while body copy stays neutral. The headings feel like product placards in a flagship store: firm, tightly set, and built to sit beside appliances without trying to become the appliance.

Component language is round, commerce-ready, and stateful. Buttons are capsules, cards use 1.25rem to 1.75rem radii, and shadows exist but are scoped to cards, overlays, and panels instead of being sprinkled everywhere. Shadow is not the site's atmosphere; it is a small lift under a product tray. The red button is closer to a physical purchase button on the counter than a decorative ribbon: it waits at rest, then becomes unmistakable on interaction.

The global navigation is the site's real machinery. It is not a thin fashion header; it is a layered department-store directory with `c-gnb__*` and `cmp-navigation__*` parts doing the work of aisles, categories, back buttons, and support desks. LG's visual signature comes from that combination: a dense enterprise shell softened by warm retail materials.

The fetched `https://www.lg.com/kr/` route redirected to an LG global 404 shell from this environment. This guide therefore describes the observable LG global AEM design system and its shared CSS, not a fully rendered Korean homepage hero.

### Key Characteristics

- Warm commercial neutrality: #FFFFFF (`{colors.surface-base}`) plus #F0ECE4 (`{colors.surface-warm}`) and #CBC8C2 (`{colors.hairline-warm}`), not sterile white/gray alone.
- Action red is #EA1917 (`{colors.brand-red}`), especially for hover and highlighted CTA states.
- Heritage LG magenta #A50034 (`{colors.brand-heritage}`) appears as brand memory, but the interactive system often prefers brighter red.
- Rounded commerce geometry: 1.25rem and 1.75rem radii dominate cards and buttons.
- Heading voice is `LGEI Headline` at weight 600; body voice is `LGEI Text` or system fallback at weight 400.
- Global navigation is the structural center: many `c-gnb__*` and `cmp-navigation__*` classes show an enterprise mega-nav system.
- Breakpoints pivot around 48rem / 48.0625rem, with desktop rules heavily represented.
- Shadows are present but conservative: mostly card/panel elevation, not atmospheric decoration.
- Component class names are AEM/BEM-like (`c-button`, `c-cta`, `c-card`, `c-gnb`, `cmp-*`) rather than utility-first tokens.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Warm Commerce
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **warm rounded commerce shell with red action states**으로 기억된다.
> **Code Complexity**: high — AEM component CSS, mega navigation, many responsive rules, and multiple stateful component variants require careful reproduction.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 LG Electronics처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "LGEI Text", "Segoe UI", "Microsoft Sans Serif", sans-serif;
  font-weight: 400;
}
h1, h2, h3 {
  font-family: "LGEI Headline", "Segoe UI", "Microsoft Sans Serif", sans-serif;
  font-weight: 600;
  letter-spacing: -0.015rem;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; --muted: #646464; --hairline: #CBC8C2; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #EA1917; --heritage: #A50034; --warm: #F0ECE4; }
```

**절대 하지 말아야 할 것 하나**: LG를 차가운 흑백 SaaS처럼 만들지 말 것. #CBC8C2와 #F0ECE4의 warm retail chassis 없이 #FFFFFF / #000000 / #EA1917만 쓰면 브랜드가 딱딱해진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.lg.com/kr/` |
| Fetch result | `https://www.lg.com/kr/` → `https://www.lg.com/global/kr/` → HTTP 404 shell in this environment |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | curl + Chrome UA + ko-KR Accept-Language; Playwright screenshot attempted |
| HTML size | 235278 bytes |
| CSS files | 2 external + inline remnants, about 4.58M CSS characters |
| Token prefix | `lg` (synthetic output prefix; source CSS does not expose a robust `--lg-*` custom property namespace) |
| Method | CSS declarations, class names, color frequency, and component selectors parsed from fetched shell |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Adobe Experience Manager style component output (`cmp-*`, `aem-Grid`, `c-*` class families)
- **Design system**: LG global component CSS — no strong design-token custom-property namespace detected
- **CSS architecture**: compiled component CSS with BEM-like classes
  ```text
  c-* / cmp-*        component and AEM component layer
  c-gnb__*           global navigation / mega-nav layer
  c-button / c-cta   action layer
  c-footer__*        footer IA layer
  ```
- **Class naming**: mixed AEM component classes and BEM-style LG classes
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: branded LG font declarations in CSS (`LGEI Headline`, `LGEI Text`, `LG Smart`, `LG Smart UI`)
- **Canonical anchor**: fetched document declares `https://www.lg.com/global/errors/404/`, so canonical page-level content is not reliable for KR homepage hero analysis.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `LGEI Headline` (brand/proprietary)
- **Body font**: `LGEI Text` (brand/proprietary)
- **Fallback stack**: `Segoe UI`, `"Microsoft Sans Serif"`, `sans-serif`
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --lg-font-family-display: "LGEI Headline", "Segoe UI", "Microsoft Sans Serif", sans-serif;
  --lg-font-family-body: "LGEI Text", "Segoe UI", "Microsoft Sans Serif", sans-serif;
  --lg-font-weight-normal: 400;
  --lg-font-weight-bold: 600;
}
body {
  font-family: var(--lg-font-family-body);
  font-weight: var(--lg-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **LGEI Headline** is proprietary. Use **Segoe UI** first on Windows-like environments, or **Inter** only with restraint: weight 600 for headings, tracking around `-.015rem` to `-.0625rem` for display sizes.
- **LGEI Text** can be approximated with **Segoe UI** or **Noto Sans KR** for Korean pages. Keep body at 400 and line-height around `1.5rem`; do not make body weight 500 by default.
- **LG Smart / LG Smart UI** appear in the compiled CSS as legacy or regional font layers. If unavailable, keep them as optional aliases before the system fallback rather than replacing the whole stack with Roboto.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| display-xl | `5rem` | `600` | `5rem` | `-.08rem` |
| display-lg | `3.5rem` | `600` | `3.75rem` | `-.0625rem` |
| title-lg | `2.25rem` | `600` | `2.625rem` | `-.015rem` |
| title-md | `2rem` | `600` | `2.25rem` | `-.015rem` |
| title-sm | `1.5rem` | `600` | `1.75rem` | `0` |
| body | `1rem` | `400` | `1.5rem` | `0` |
| body-sm | `.875rem` | `400` | `1.25rem` | `0` |
| caption | `.75rem` | `400` | `1rem` | `0` |

> ⚠️ Typography extractor found many family and weight declarations but no clean tokenized scale map. Scale above is reconstructed from dominant CSS declarations.

### Principles
<!-- SOURCE: manual -->

1. Display text belongs to `LGEI Headline` and generally lands on weight 600, not 700 by default.
2. Body copy stays at weight 400. Weight 500 exists in the CSS but is sparse, so it should not become a general-purpose middle weight.
3. Large headings use negative tracking; body text does not. This preserves corporate tightness without hurting legibility.
4. The system mixes rem-based web sizing with old regional font layers. Reproduction should normalize into a small ladder rather than copying every emitted value.
5. `1rem / 1.5rem` is the reliable body rhythm; the dense mega-nav uses `.875rem` and `.75rem` for utility text.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (4 steps)
<!-- SOURCE: auto+manual -->

| Token | Hex |
|---|---|
| `lg-brand-heritage` | `#A50034` |
| `lg-brand-red` | `#EA1917` |
| `lg-brand-hot` | `#FD312E` |
| `lg-brand-pink` | `#DA0F47` |

### 06-2. Brand Dark Variant
<!-- SOURCE: auto+manual -->

| Token | Hex |
|---|---|
| `lg-dark-surface` | `#4A4946` |
| `lg-dark-ink` | `#262626` |
| `lg-black` | `#000000` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light | Warm / Dark |
|---|---|---|
| 0 | `#FFFFFF` | `#000000` |
| 50 | `#F6F6F6` | `#333333` |
| 100 | `#F0ECE4` | `#4A4946` |
| 200 | `#E6E1D6` | `#646464` |
| 300 | `#CBC8C2` | `#7E7C77` |
| 400 | `#BBBBBB` | `#999999` |

### 06-4. Accent Families
<!-- SOURCE: auto -->

| Family | Key step | Hex |
|---|---|---|
| Success green | primary | `#287D00` |
| Support blue | primary | `#01456A` |
| Purple support | primary | `#411261` |
| Lavender surface | pale | `#ECE6FF` |

### 06-5. Semantic
<!-- SOURCE: auto+manual -->

| Token | Hex | Usage |
|---|---|---|
| `lg-action-primary` | `#EA1917` | CTA hover, highlighted action, red interactive state |
| `lg-brand-heritage` | `#A50034` | LG brand memory / logo-adjacent accent |
| `lg-bg-page` | `#FFFFFF` | default page and component surface |
| `lg-bg-soft` | `#F6F6F6` | card/section soft surface |
| `lg-bg-warm` | `#F0ECE4` | warm shell / breadcrumb / beige UI surfaces |
| `lg-border-warm` | `#CBC8C2` | hairline separators and warm borders |
| `lg-text-primary` | `#000000` | high-emphasis copy |
| `lg-text-secondary` | `#333333` | standard navigation and body labels |
| `lg-text-muted` | `#646464` | secondary copy and borders |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto+manual -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--lg-action` | `#EA1917` | primary interactive color |
| `--lg-surface` | `#FFFFFF` | base canvas |
| `--lg-surface-warm` | `#F0ECE4` | warm retail panels |
| `--lg-hairline` | `#CBC8C2` | separators |
| `--lg-ink` | `#000000` | primary text |
| `--lg-muted` | `#646464` | secondary text and borders |

> Source CSS does not expose these aliases as custom properties. They are normalized output aliases for implementation.

### 06-7. Dominant Colors (실제 CSS 빈도 순)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---|---|
| white | `#FFFFFF` | 1095 |
| black | `#000000` | 915 |
| warm hairline | `#CBC8C2` | 821 |
| dark gray | `#333333` | 723 |
| action red | `#EA1917` | 421 |
| muted gray | `#646464` | 378 |
| disabled gray | `#BBBBBB` | 286 |
| warm beige | `#E6E1D6` | 186 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.brand-red}` (`#EA1917`)** — The action red. It is brighter and more operational than LG's heritage magenta, appearing in hover states and highlighted buttons. Use it when the user can act, not as general decoration.

**`{colors.surface-base}` (`#FFFFFF`)** — The retail floor. White carries the global shell and gives product imagery room, but it needs warm borders and soft panels nearby to avoid becoming generic.

**`{colors.hairline-warm}` (`#CBC8C2`)** — The hidden LG texture. This is the separator that makes the UI feel domestic and appliance-adjacent rather than cold enterprise SaaS.

**`{colors.text-primary}` (`#000000`)** — High-confidence information. LG uses black directly for active breadcrumbs, text, and strong labels; the softness comes from surrounding surfaces, not from weakening the ink.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `lg-space-2xs` | `.25rem` | icon/text micro gaps |
| `lg-space-xs` | `.5rem` | dense nav and chips |
| `lg-space-sm` | `.75rem` | compact buttons and rows |
| `lg-space-md` | `1rem` | default horizontal padding |
| `lg-space-lg` | `1.5rem` | card padding and desktop gaps |
| `lg-space-xl` | `2rem` | section internal spacing |
| `lg-space-2xl` | `3rem` | larger desktop separation |

**주요 alias**:
- `lg-shell-gutter` → `1.5rem` (desktop component rhythm)
- `lg-mobile-gutter` → `1rem` (mobile component rhythm)
- `lg-dense-gap` → `.5rem` (navigation and utility clusters)

### Whitespace Philosophy
<!-- SOURCE: manual -->

LG's spacing is not luxury whitespace. It is retail whitespace: enough air to keep products and service modules legible, but dense enough to support navigation, footer links, carousel controls, and support actions in the same system. The dominant gaps `.5rem`, `.75rem`, `1rem`, and `1.5rem` show a practical component grid.

The warm surfaces do a lot of spatial work. Beige bands and hairlines separate content so vertical spacing can stay moderate. Recreate this by pairing `1.5rem` card padding with #CBC8C2 hairlines instead of pushing every section into oversized 96px marketing gaps.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `lg-radius-xs` | `.25rem` | small form/control details |
| `lg-radius-sm` | `.5rem` | compact cards and utility panels |
| `lg-radius-md` | `.75rem` | common cards and media corners |
| `lg-radius-lg` | `1.25rem` | soft commerce cards |
| `lg-radius-xl` | `1.75rem` | capsule buttons and larger panels |
| `lg-radius-pill` | `62.4375rem` / `999px` | pill controls |
| `lg-radius-circle` | `50%` | icon buttons and circular controls |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| none | `none` | default chrome, nav, flat text blocks |
| panel-soft | `0 .5rem .75rem rgba(0,0,0,.06)` | soft product/card panels |
| panel-medium | `0 .125rem .1875rem rgba(0,0,0,.15)` | small raised controls |
| overlay | `0 .25rem .75rem rgba(0,0,0,.25)` | menus, overlays, stronger panels |
| floating | `.125rem .25rem .75rem rgba(0,0,0,.14)` | floating UI elements |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `lg-motion-fast` | `all .2s` | compact UI state changes |
| `lg-motion-base` | `all .3s` | dominant transition pattern |
| `lg-motion-bg` | `background .3s,color .2s,border-color .3s` | buttons and interactive chrome |
| `lg-motion-slow` | `all .5s` | drawer/panel transitions |
| `lg-motion-opacity` | `opacity .3s` | reveal/fade states |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: common values include `90rem`, `93rem`, `100rem`, and `120rem`; use `90rem` as the practical shell max.
- **Grid type**: AEM `aem-Grid--12` plus component-level flex/grid.
- **Column count**: 12-column AEM base with component-specific card rows.
- **Gutter**: `1.5rem` desktop, `1rem` mobile.

### Hero
- **Pattern Summary**: global shell route returned an error page; use LG editorial-product hero as `large product/media band + warm surface + red CTA + rounded controls`.
- Layout: product/editorial page should use a two-layer composition: navigation shell above, product or message module below.
- Background: `#FFFFFF` base with optional `#F6F6F6` or `#F0ECE4` bands.
- **Background Treatment**: solid/warm surface, not mesh gradient. Product imagery should carry visual energy.
- H1: `3.5rem` to `5rem` / weight `600` / tracking `-.0625rem` to `-.08rem`.
- Max-width: `90rem` shell, with headline content usually narrower than full shell.

### Section Rhythm
```css
section {
  padding: 3rem 1.5rem;
  max-width: 90rem;
}
@media (max-width: 48rem) {
  section { padding: 2rem 1rem; }
}
```

### Card Patterns
- **Card background**: `#FFFFFF` or `#F6F6F6`
- **Card border**: `1px solid #CBC8C2` when structure is needed
- **Card radius**: `1.25rem` for cards, `1.75rem` for large soft panels
- **Card padding**: `1.25rem` to `1.5rem`
- **Card shadow**: `0 .5rem .75rem rgba(0,0,0,.06)` for soft elevation; many surfaces stay flat

### Navigation Structure
- **Type**: global mega-navigation with multiple depth groups
- **Position**: sticky-capable shell (`c-gnb__sticky can-sticky`)
- **Height**: content-dependent desktop shell; reproduce with 72px main row plus expandable layers
- **Background**: `#FFFFFF`
- **Border**: `1px solid #CBC8C2` or warm separator

### Content Width
- **Prose max-width**: `48rem` for readable copy
- **Container max-width**: `90rem`
- **Sidebar width**: not a primary layout primitive on the fetched shell; mega-nav panels replace sidebar behavior

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `max-width: 48rem` | mobile layer and compact component rules |
| Desktop start | `min-width: 48.0625rem` | dominant desktop breakpoint in compiled CSS |
| Large | `min-width: 80rem` | wider desktop refinements |
| XL | `min-width: 90rem` | large shell/container refinements |

### Touch Targets
- **Minimum tap size**: use `44px` minimum; many controls are rem-based and should be normalized for touch.
- **Button height (mobile)**: target `2.75rem` to `3rem`.
- **Input height (mobile)**: target `3rem`.

### Collapsing Strategy
- **Navigation**: mega-nav collapses into mobile layers/back buttons (`c-gnb__mobile-layer`, `c-gnb__mobile-layer--back`).
- **Grid columns**: 12-column AEM grid collapses into stacked component rows.
- **Sidebar**: no persistent sidebar; navigation depth becomes layered menus.
- **Hero layout**: editorial/product hero should stack copy above/alongside media depending on asset crop.

### Image Behavior
- **Strategy**: responsive images inside `cmp-image` / `c-image`.
- **Max-width**: `100%`.
- **Aspect ratio handling**: component-dependent; use fixed aspect ratios for product cards to prevent layout shift.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<a class="c-button c-button--default highlight" href="#">
  <span class="c-button__text">Buy now</span>
</a>
```

| Spec | Value |
|---|---|
| Font | `LGEI Text`, `.875rem` to `1rem`, weight 600 for emphasis |
| Primary bg | `#EA1917` |
| Primary text | `#FFFFFF` |
| Outline border | `1px solid #646464` |
| Radius | `1.75rem` or pill |
| Padding | `.75rem 1.25rem` |
| Hover | red fill `#EA1917`, white text, border-color `#EA1917` |
| Focus | visible black outline `#000000` where available |

### Badges

```html
<span class="c-badge">New</span>
```

| Spec | Value |
|---|---|
| Font | `.75rem`, weight 600 |
| Surface | `#F0ECE4` or `#F6F6F6` |
| Text | `#333333` |
| Radius | `999px` |
| Padding | `.25rem .5rem` |

### Cards & Containers

```html
<article class="c-card">
  <div class="c-image"><img class="cmp-image__image c-image__img" alt="" /></div>
  <div class="c-text-contents">
    <h3 class="title c-text-contents__headline">Product module</h3>
    <p class="text c-text-contents__bodycopy">Supporting copy.</p>
  </div>
</article>
```

| Spec | Value |
|---|---|
| Surface | `#FFFFFF` or `#F6F6F6` |
| Border | optional `1px solid #CBC8C2` |
| Radius | `1.25rem` |
| Padding | `1.25rem` to `1.5rem` |
| Shadow | `0 .5rem .75rem rgba(0,0,0,.06)` when elevated |
| Hover | subtle border or shadow transition; no aggressive transform required |

### Navigation

```html
<nav class="c-gnb__container">
  <a class="c-gnb__logo-link" href="/">LG</a>
  <a class="c-gnb__item-link c-gnb__item-link--depth1" href="#">Shop</a>
</nav>
```

| Spec | Value |
|---|---|
| Structure | `c-gnb__*` global nav with `cmp-navigation__*` nested groups |
| Surface | `#FFFFFF` |
| Text | `#000000` / `#333333` |
| Border | warm hairline `#CBC8C2` |
| Mobile | layered menu with explicit back controls |
| Active | stronger weight 600 or black text |

### Inputs & Forms

```html
<label class="c-input">
  <span class="c-input__label">Email</span>
  <input class="c-input__field" type="email" />
</label>
```

| Spec | Value |
|---|---|
| Height | `3rem` target |
| Border | `1px solid #646464` |
| Background | `#FFFFFF` |
| Text | `#000000` |
| Placeholder | `#646464` |
| Focus | black outline or red action border, but keep accessibility visible |
| Error | use red family; prefer `#EA1917` only for clear action/error emphasis |

### Hero Section

```html
<section class="lg-hero">
  <div class="lg-hero__copy">
    <p class="lg-eyebrow">LG Electronics</p>
    <h1>Life's Good, engineered for home.</h1>
    <a class="c-button c-button--default highlight" href="#">Explore</a>
  </div>
  <div class="lg-hero__media"></div>
</section>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` with warm band `#F0ECE4` or product media |
| H1 | `LGEI Headline`, `3.5rem` to `5rem`, weight 600 |
| Body | `1rem`, line-height `1.5rem`, color `#333333` |
| CTA | red capsule `#EA1917` |
| Layout | desktop split or product/editorial media band; mobile stacked |

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-primary-red**
- bg `#EA1917`, text `#FFFFFF`, radius `1.75rem`, transition `background .3s,color .2s,border-color .3s`.
- Use for the main conversion action. Do not use heritage magenta here unless the source page proves that variant.

**button-outline-warm**
- bg `#FFFFFF`, border `1px solid #646464`, text `#000000`, hover bg `#EA1917`.
- Use for secondary actions in product/support modules.

**button-circle-arrow**
- circular or near-circular icon button, radius `50%`, small/medium sizes.
- Use for carousel, back, next, and utility navigation.

**card-soft-commerce**
- bg `#F6F6F6` or `#FFFFFF`, radius `1.25rem`, optional shadow `0 .5rem .75rem rgba(0,0,0,.06)`.
- Use for product, support, and content modules.

**nav-global-depth**
- `c-gnb__item-link--depth1/2/3` layered navigation links.
- Active state uses stronger text color/weight rather than decorative color bars.

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
warm-hairline-commerce:
  description: "Warm beige separators turn the black/white/red system into a retail appliance shell."
  technique: "border-color:#CBC8C2; warm bands #F0ECE4 and #E6E1D6; flat #FFFFFF base"
  applied_to: ["{component.nav-global}", "{component.card-soft-commerce}", "breadcrumbs", "footer separators"]
  visual_signature: "The page feels like a domestic showroom floor, not a cold grayscale SaaS frame."

red-hover-conversion:
  description: "LG red is reserved for decisive action and often appears through state instead of resting everywhere."
  technique: "background-color:#EA1917; border-color:#EA1917; color:#FFFFFF; transition:background .3s,color .2s,border-color .3s"
  applied_to: ["{component.button-primary-red}", "{component.button-outline-warm}", "arrow controls", "CTA-like controls"]
  visual_signature: "Interaction snaps into a clear red purchase signal without adding a second action color."

rounded-appliance-chassis:
  description: "Large rounded geometry makes modules read like softened appliance surfaces and product trays."
  technique: "border-radius:1.25rem on cards; border-radius:1.75rem or 999px on buttons and pills; circle controls at 50%"
  applied_to: ["{component.card-soft-commerce}", "{component.button-primary-red}", "{component.button-outline-warm}", "carousel controls"]
  visual_signature: "Commerce UI feels physically rounded and showroom-ready rather than sharp enterprise chrome."

soft-panel-lift-only:
  description: "Elevation is scoped to panels and overlays while primary chrome stays mostly flat."
  technique: "box-shadow:0 .5rem .75rem rgba(0,0,0,.06); overlay shadow 0 .25rem .75rem rgba(0,0,0,.25); many surfaces remain shadow:none"
  applied_to: ["{component.card-soft-commerce}", "menus", "overlays", "floating controls"]
  visual_signature: "A product tray lifts subtly off the surface; the whole page never becomes atmospheric."

lgei-display-tightening:
  description: "Display typography is optically tightened while body copy remains neutral and readable."
  technique: "font-family:'LGEI Headline'; font-weight:600; letter-spacing:-.015rem to -.08rem on title/display sizes; body tracking 0"
  applied_to: ["hero headlines", "section titles", "product placards"]
  visual_signature: "Headlines sit dense and corporate beside product modules without inflating to 700/800 everywhere."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Product benefit first, concise, plain | "OLED that brightens the room" |
| Primary CTA | Direct commerce verb | "Shop Now" |
| Secondary CTA | Support/explore verb | "Learn More" |
| Subheading | Feature proof and domestic context | "Designed for brighter rooms and everyday viewing." |
| Tone | Helpful, product-led, not playful | Clear retail guidance with technical proof points |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* LG Electronics — copy into your root stylesheet */
:root {
  /* Fonts */
  --lg-font-family-display: "LGEI Headline", "Segoe UI", "Microsoft Sans Serif", sans-serif;
  --lg-font-family-body: "LGEI Text", "Segoe UI", "Microsoft Sans Serif", sans-serif;
  --lg-font-weight-normal: 400;
  --lg-font-weight-bold: 600;

  /* Brand */
  --lg-color-brand-heritage: #A50034;
  --lg-color-brand-red: #EA1917;
  --lg-color-brand-hot: #FD312E;
  --lg-color-brand-pink: #DA0F47;

  /* Surfaces */
  --lg-bg-page: #FFFFFF;
  --lg-bg-soft: #F6F6F6;
  --lg-bg-warm: #F0ECE4;
  --lg-bg-warm-2: #E6E1D6;
  --lg-bg-dark: #4A4946;

  /* Text + borders */
  --lg-text: #000000;
  --lg-text-secondary: #333333;
  --lg-text-muted: #646464;
  --lg-text-disabled: #BBBBBB;
  --lg-border-warm: #CBC8C2;

  /* Spacing */
  --lg-space-xs: .5rem;
  --lg-space-sm: .75rem;
  --lg-space-md: 1rem;
  --lg-space-lg: 1.5rem;
  --lg-space-xl: 2rem;

  /* Radius */
  --lg-radius-sm: .5rem;
  --lg-radius-md: .75rem;
  --lg-radius-lg: 1.25rem;
  --lg-radius-xl: 1.75rem;
  --lg-radius-pill: 999px;
}

body {
  background: var(--lg-bg-page);
  color: var(--lg-text);
  font-family: var(--lg-font-family-body);
  font-weight: var(--lg-font-weight-normal);
  line-height: 1.5;
}

h1, h2, h3 {
  font-family: var(--lg-font-family-display);
  font-weight: var(--lg-font-weight-bold);
  letter-spacing: -.015rem;
}

.lg-button-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2.75rem;
  padding: .75rem 1.25rem;
  border-radius: var(--lg-radius-pill);
  border: 1px solid var(--lg-color-brand-red);
  background: var(--lg-color-brand-red);
  color: #FFFFFF;
  font-weight: 600;
  transition: background .3s, color .2s, border-color .3s;
}

.lg-card {
  border-radius: var(--lg-radius-lg);
  background: var(--lg-bg-soft);
  border: 1px solid var(--lg-border-warm);
  padding: var(--lg-space-lg);
  box-shadow: 0 .5rem .75rem rgba(0,0,0,.06);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — LG Electronics
module.exports = {
  theme: {
    extend: {
      colors: {
        lg: {
          red: '#EA1917',
          heritage: '#A50034',
          surface: '#FFFFFF',
          soft: '#F6F6F6',
          warm: '#F0ECE4',
          hairline: '#CBC8C2',
          ink: '#000000',
          muted: '#646464',
        },
      },
      fontFamily: {
        sans: ['LGEI Text', 'Segoe UI', 'Microsoft Sans Serif', 'sans-serif'],
        display: ['LGEI Headline', 'Segoe UI', 'Microsoft Sans Serif', 'sans-serif'],
      },
      borderRadius: {
        lgcard: '1.25rem',
        lgpill: '999px',
      },
      boxShadow: {
        lgsoft: '0 .5rem .75rem rgba(0,0,0,.06)',
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
| Brand primary | `lg-action-primary` | `#EA1917` |
| Brand heritage | `lg-brand-heritage` | `#A50034` |
| Background | `lg-bg-page` | `#FFFFFF` |
| Warm surface | `lg-bg-warm` | `#F0ECE4` |
| Text primary | `lg-text-primary` | `#000000` |
| Text muted | `lg-text-muted` | `#646464` |
| Border | `lg-border-warm` | `#CBC8C2` |
| Success | `lg-success` | `#287D00` |
| Error/action | `lg-action-primary` | `#EA1917` |

### Example Component Prompts

#### Hero Section
```text
LG Electronics 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF 위에 #F0ECE4 warm band를 부분적으로 사용
- H1: LGEI Headline, 3.5rem desktop, weight 600, letter-spacing -.0625rem
- 본문: LGEI Text, 1rem, line-height 1.5rem, color #333333
- CTA: #EA1917 배경, #FFFFFF 텍스트, pill radius 999px, padding .75rem 1.25rem
- 전체 컨테이너: max-width 90rem, desktop padding 1.5rem, mobile padding 1rem
- 제품/미디어가 시각 중심이고 장식 그라디언트는 쓰지 않음
```

#### Card Component
```text
LG Electronics 스타일 카드 컴포넌트를 만들어줘.
- 배경: #F6F6F6 또는 #FFFFFF
- border: 1px solid #CBC8C2
- radius: 1.25rem
- padding: 1.5rem
- shadow: 0 .5rem .75rem rgba(0,0,0,.06)
- 제목: LGEI Headline, 1.5rem, weight 600
- 본문: LGEI Text, 1rem, color #333333, line-height 1.5
- hover는 미세한 border/shadow 변화만
```

#### Badge
```text
LG Electronics 스타일 배지를 만들어줘.
- font: LGEI Text, .75rem, weight 600
- padding: .25rem .5rem
- radius: 999px
- bg: #F0ECE4
- text: #333333
- border: 1px solid #CBC8C2
```

#### Navigation
```text
LG Electronics 스타일 상단 네비게이션을 만들어줘.
- 배경: #FFFFFF
- 하단 border: 1px solid #CBC8C2
- 링크: LGEI Text, .875rem 또는 1rem, weight 400, color #333333
- active/depth headline: color #000000, weight 600
- 모바일은 depth layer + back button 구조
- CTA나 hover action에는 #EA1917 사용
```

### Iteration Guide

- **색상 변경 시**: red action은 `#EA1917`, heritage mark는 `#A50034`로 분리한다.
- **폰트 변경 시**: `LGEI Headline` unavailable이면 display만 Segoe UI/Inter 600으로 보정한다.
- **여백 조정 시**: `.5rem`, `.75rem`, `1rem`, `1.5rem` 중심으로 유지한다.
- **새 컴포넌트 추가 시**: 1.25rem rounded surface + warm hairline을 먼저 적용하고, shadow는 필요한 경우에만 추가한다.
- **다크 모드**: fetched shell은 light-first다. dark section은 `#4A4946`부터 시작하고 red를 그대로 과다 사용하지 않는다.
- **반응형**: `48rem` / `48.0625rem` 경계와 90rem shell을 우선 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #EA1917 as the action red for CTA hover and highlighted conversion states.
- Keep #CBC8C2 warm hairlines in navigation, card, breadcrumb, and footer structure.
- Pair #FFFFFF surfaces with #F0ECE4 or #F6F6F6 support bands to keep the retail warmth.
- Use `LGEI Headline` for display and `LGEI Text` for body; fallback to Segoe UI deliberately.
- Use 1.25rem and 1.75rem radii for the soft appliance-commerce chassis.
- Treat the global nav as a serious component system, not a simple row of links.
- Keep body weight 400 and reserve 600 for headings, active labels, and important UI.

### ❌ DON'T

- 배경을 `#FAFAFA` 또는 cold off-white로만 두지 말 것 — 대신 `#FFFFFF`와 `#F0ECE4` / `#F6F6F6` 조합 사용.
- 텍스트를 `#111111` 한 값으로 통일하지 말 것 — 대신 primary `#000000`, secondary `#333333`, muted `#646464` 계층 사용.
- 브랜드 색을 `#A50034` 하나로 모든 CTA에 쓰지 말 것 — action CTA/hover는 `#EA1917`, heritage accent는 `#A50034`로 분리.
- hairline을 `#E5E7EB` 같은 cool gray로 바꾸지 말 것 — 대신 warm separator `#CBC8C2` 사용.
- 카드 배경을 `#FFFFFF`만 반복하지 말 것 — soft commerce modules에는 `#F6F6F6` 또는 `#F0ECE4` 사용.
- body에 `font-weight: 500`을 기본값으로 사용 금지 — LG body rhythm은 `400`, 강조/heading은 `600`.
- 버튼을 4px radius 사각형으로 만들지 말 것 — `1.75rem` 또는 `999px` capsule geometry 사용.
- `linear-gradient(135deg, #667eea, #764ba2)` 같은 generic AI gradient 금지 — LG는 product/media + warm surface 중심.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- No token-rich CSS variable system: source CSS exposes only a few custom properties, mostly Apple Pay related.
- No cold SaaS blue primary: blue appears as support/accent data, not as the brand action color.
- No second dominant action color: red carries conversion and hover states.
- No sharp enterprise rectangles as the default chassis: rounded radii dominate components.
- No universal heavy shadow: many chrome surfaces use flat color and warm borders instead.
- No decorative mesh gradient identity: color is structural, while products/media should supply the visual subject.
- No body-wide weight 500: sparse middle weights exist but are not the normal reading texture.
- No tiny 12px-only utility UI: dense labels exist, but commerce components need touch-scale controls.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual / REQUIRED -->

- **KR URL fetch returned a global 404 shell** — `https://www.lg.com/kr/` redirected to `https://www.lg.com/global/kr/` and returned HTTP 404 in this environment. The guide uses observable LG global shell CSS, not a fully accessible KR homepage route.
- **Playwright screenshot blocked** — browser rendering produced `Access Denied`, so hero visual interpretation is based on CSS/component structure rather than verified KR screenshot.
- **Existing cached screenshot mismatch** — prior `insane-design/lg/screenshots/hero-cropped.png` appeared to show a US commerce hero before refresh; it was not used as KR visual truth.
- **CSS volume is high and compiled** — about 4.58M CSS characters were parsed. Frequency counts may include support, footer, hidden nav, regional, and error-shell styles.
- **Token namespace absent** — source CSS does not provide a robust `--lg-*` token graph. Output aliases are normalized implementation handles, not source variable names.
- **Typography scale reconstructed** — extractor found font families and weights but no clean scale object; scale values are derived from dominant CSS declarations.
- **Component states partially inferred** — hover/focus values were visible for several button/upload/arrow selectors, but loading/error states were not fully surfaced from a live form flow.
- **Dark mode not validated** — dark surface colors exist in CSS, but a complete dark-mode mapping was not observed.
- **Product-page hero not verified** — because the requested route yielded a shell/error result, product imagery, carousel behavior, and KR-specific content modules require a later successful render.
