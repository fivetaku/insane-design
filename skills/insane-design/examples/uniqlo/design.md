---
schema_version: 3.2
slug: uniqlo
service_name: UNIQLO
site_url: https://www.uniqlo.com/us/en
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: light
brand_color: "#E00"
primary_font: "UniqloProRegular"
font_weight_normal: 400
token_prefix: fr-ec

bold_direction: Functional Editorial
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: commerce-marketplace
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "A production commerce UI kit is present in CSS classes and component variants, but custom property token extraction returned 0 resolved vars."

colors:
  brand-red: "#E00"
  surface-base: "#FFFFFF"
  text-primary: "#000000"
  text-secondary: "#6A6A6A"
  surface-muted: "#F4F4F4"
  border-default: "#DADADA"
  border-strong: "#767676"
  link-blue: "#005DB5"
typography:
  display: "UniqloProRegular"
  body: "Twemoji Country Flags, Helvetica Neue, Helvetica, Arial, system-ui, -apple-system, sans-serif"
  ladder:
    - { token: hero-title, size: "32px", weight: 300, line_height: "1.3", tracking: ".36px" }
    - { token: body, size: "16px", weight: 400, line_height: "1.5", tracking: "0" }
    - { token: label, size: "13px", weight: 400, line_height: "1.2", tracking: ".025rem" }
  weights_used: [300, 400, 600]
  weights_absent: [500]
components:
  button-primary: { bg: "{colors.text-primary}", color: "{colors.surface-base}", radius: "0", hover_bg: "#2A2A2A" }
  button-secondary: { bg: "{colors.surface-base}", color: "{colors.text-primary}", border: "1px solid #1B1B1B", radius: "0" }
  search-pill: { bg: "{colors.surface-base}", radius: "999px", height: "44px" }
  card-standard: { bg: "{colors.surface-base}", border: "1px solid #DADADA", padding: "16px-24px" }
---

# DESIGN.md - UNIQLO

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

UNIQLO is the canonical example of catalogue-first commerce marketplace — a retail operating system where editorial photography lives in the window and warehouse precision runs every aisle.

The page lets a full-width lifestyle image create warmth, then immediately returns to disciplined black, white, red, and gray. The brand mark is pure red, but the interface does not flood itself with red. Red is a stamp, a sale/state signal, and a logo memory. The working UI is almost entirely #FFFFFF (`{colors.surface-base}`), #000000 (`{colors.text-primary}`), #DADADA (`{colors.border-default}`), and compact spacing.

The hero is the emotional canvas: large lifestyle photography, white overlaid copy, product price, a small colored topic badge, and a persistent top navigation. Under that, the system becomes a marketplace: categories, product tiles, chips, cards, tabs, and buttons follow a commerce grammar where clarity wins over ornament. This store wants the user to find clothing, compare sizes, and move through shopping flows without noticing the frame.

The distinctive tension is "LifeWear editorial" plus "warehouse precision." Photography supplies season, body, material, and use case. The UI supplies square edges, explicit borders, 44px controls, and unambiguous action states. UNIQLO's craft is the refusal to let commerce chrome compete with product imagery.

Typography is similarly functional. `UniqloProRegular` appears for brand-specific surfaces, while the broader stack falls back through Helvetica/Arial/system fonts and locale-aware CJK stacks. The extracted CSS uses 300, 400, and 600 frequently; the result is lighter than a typical marketplace but less precious than luxury editorial. To press the metaphor: the homepage behaves like a flagship store vitrine — the lookbook poster lives in the window, the price tags live on the rack just inside the door, and the red logo is a folded paper tag pinned to a cotton tee.

비유를 한 단계 더 밀자면 UNIQLO는 단일 boutique가 아니라 catalogue-type marketplace다. 시즌 lookbook은 store 윈도우에 붙은 포스터, 카테고리 nav는 마켓 통로의 사이즈별 매대, 제품 카드는 창고에서 갓 꺼낸 basics가 차곡히 올라간 shelf, 검정 CTA는 카운터 위에 찍힌 결제 도장처럼 작동한다. 페이지가 종이 catalogue처럼 펼쳐지지만, 동선은 물류센터의 화물 라벨처럼 정확하게 끊긴다. no second brand color — store interior는 의도적으로 white canvas에 daylight로만 켜져 있다.

### Key Characteristics

- Red is the brand anchor (`#E00`), not a page-wide decorative wash.
- The UI baseline is monochrome: `#FFFFFF`, `#000000`, `#DADADA`, `#6A6A6A`.
- Product/lifestyle photography carries the emotional weight of the page.
- Primary commerce buttons are black rectangles, not red brand buttons.
- Search is a white 999px pill placed over or near the hero layer.
- Corners are mostly zero-radius; pills and icon circles are deliberate exceptions.
- 44px touch targets appear repeatedly for carousel and commerce controls.
- Layout breaks at 600px and 960px, with desktop commerce density above 960px.
- Motion is utility-level: opacity, transform, and color fades around .18s-.4s.
- Shadows are sparse and functional, mostly for overlays, focus, or image/text legibility.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Functional Editorial
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **full-bleed lifestyle commerce photography held inside a black-white-red retail grid**으로 기억된다.
> **Code Complexity**: high — production commerce UI kit, responsive breakpoints, carousel states, locale typography, and many component variants.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 UNIQLO처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "UniqloProRegular", "Helvetica Neue", Helvetica, Arial, system-ui, -apple-system, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #E00; }
```

**절대 하지 말아야 할 것 하나**: primary CTA를 `#E00` red로 칠하지 말 것. UNIQLO의 commerce CTA는 대체로 black-on-white 또는 white-on-black이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.uniqlo.com/us/en` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | reused local phase1 artifacts: HTML + CSS + screenshot |
| HTML size | 1,624,356 bytes |
| CSS files | 3 external + 1 inline stub, approx. 785,279 CSS chars |
| Token prefix | `fr-ec` / `ito` class utilities |
| Method | local phase1 JSON, CSS frequency summary, screenshot inspection, HTML structure summary |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React commerce storefront with server-rendered metadata.
- **Design system**: `fr-ec` commerce UI kit + `ito-*` utility layer.
- **CSS architecture**:
  ```text
  fr-ec-*        commerce components: button, card, header, footer, links
  ito-*          typography, spacing, color, border, alignment utilities
  media-banner*  editorial/product hero and campaign image bands
  swiper*        carousel behavior and navigation
  ```
- **Class naming**: BEM-like component modifiers (`fr-ec-button--variant-primary`) plus utility classes (`ito-font-size-32`, `ito-border-radius-0`).
- **Default theme**: light (`#FFFFFF` page floor, black text).
- **Font loading**: CSS references `UniqloProRegular`, `UniqloProLight`, and locale-aware system stacks.
- **Canonical anchor**: title and metadata identify the local artifact as UNIQLO US women's clothing/accessories; screenshot artifact is Korean-localized, noted in §19.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `UniqloProRegular` / `UniqloProLight` where brand classes are used.
- **Body font**: `Twemoji Country Flags, Helvetica Neue, Helvetica, Arial, system-ui, -apple-system, sans-serif` for English-like contexts.
- **CJK fallback stack**: `Hiragino Kaku Gothic Pro`, `Hiragino Sans`, `Noto Sans CJK JP`, `Meiryo`, `Yu Gothic`, `Noto Sans`, `Roboto`, `Arial`.
- **Weight normal / bold**: `400` / `600`; 300 appears frequently for light editorial/product text.

```css
:root {
  --uq-font-family: "UniqloProRegular", "Helvetica Neue", Helvetica, Arial, system-ui, -apple-system, sans-serif;
  --uq-font-family-cjk: "Hiragino Kaku Gothic Pro", "Hiragino Sans", "Noto Sans CJK JP", "Meiryo", sans-serif;
  --uq-font-weight-light: 300;
  --uq-font-weight-normal: 400;
  --uq-font-weight-semibold: 600;
}
body {
  font-family: var(--uq-font-family);
  font-weight: var(--uq-font-weight-normal);
}
```

### Note on Font Substitutes

- **UniqloProRegular** — proprietary brand font; do not assume it exists in a user project.
  - Open-source substitute: **Helvetica Neue / Arial / system-ui** at weight 400.
  - Display correction: use weight 300 for campaign title text when the page sits over photography.
  - Tracking correction: preserve small positive tracking such as `.025rem` or `.36px`; do not add negative luxury-style display tracking.
- **CJK surfaces** — use Noto Sans CJK or platform CJK sans fonts.
  - Keep line-height around `1.2`-`1.5` depending on component density.
  - Avoid condensed or geometric substitutes; UNIQLO reads plain, human, and retail-practical.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Hero title | `32px` | 300/400 | `1.3` | `.36px` |
| Product/banner title | `18px`-`22px` | 300/400 | `1.3`-`1.5` | `0` |
| Body | `16px` | 400 | `1.5` | `0` |
| Product tile title | `13px`-`17px` | 300/400 | `1.2`-`1.5` | `0` |
| Label / nav | `13px`-`14px` | 400/600 | `1.2` | `.025rem` |
| Micro label | `11px`-`12px` | 400 | `1.1`-`1.3` | `.12px`-.24px` |

> ⚠️ Extracted `typography.json` did not resolve a token scale, so this table is derived from CSS frequency and class names such as `ito-font-size-32`, `ito-font-size-13`, `ito-font-lh-1-2`, and `ito-font-weight-400`.

### Principles

1. Editorial hero text can be light (`300`) because the image and price provide hierarchy.
2. Commerce text defaults to `400`; use `600` for selected nav, emphasis, and stateful labels.
3. Weight `500` is effectively absent in the observed CSS; do not use it as a generic middle weight.
4. Positive or neutral tracking is the signature. Negative display tracking would make UNIQLO feel too premium-tech.
5. Use locale-aware font stacks. English, Korean, and Japanese surfaces are explicitly separated by CSS language selectors.
6. Keep product tile type small and quiet; tile density is part of the marketplace rhythm.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed)

| Token | Hex |
|---|---|
| `colors.brand-red` | `#E00` |
| `colors.brand-red-dark` | `#C00` |
| `colors.red-feedback` | `#DD3535` |
| `colors.red-light` | `#EF5555` |

### 06-2. Brand Dark Variant

> N/A — no independent dark-theme brand ramp was confirmed in the reused phase1 data.

### 06-3. Neutral Ramp

| Step | Light | Usage |
|---|---|---|
| `white` | `#FFFFFF` | page background, secondary buttons, cards |
| `gray-100` | `#F4F4F4` | muted card background, commerce surface bands |
| `gray-300` | `#DADADA` | borders, disabled button background |
| `gray-500` | `#ABABAB` | disabled text / soft divider |
| `gray-600` | `#767676` | strong border, muted text |
| `gray-700` | `#6A6A6A` | secondary text, active secondary state |
| `gray-900` | `#1B1B1B` / `#2A2A2A` | border/hover/active black variants |
| `black` | `#000000` | primary text and primary button background |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Link blue | default | `#005DB5` |
| iOS blue | utility/focus | `#007AFF` |
| Success green | default | `#00AB0F` |
| Success light | default | `#34BC3F` |
| Pink/red status | default | `#FF728D` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `brand-red` | `#E00` | logo, selected icon/state, warning/sale memory |
| `text-primary` | `#000000` | body, buttons, product information |
| `text-muted` | `#6A6A6A` | secondary labels and de-emphasized states |
| `surface-base` | `#FFFFFF` | page, cards, secondary controls |
| `surface-muted` | `#F4F4F4` | muted panels/card backgrounds |
| `border-default` | `#DADADA` | standard divider and card border |
| `border-strong` | `#767676` | stronger secondary active border |

### 06-6. Semantic Alias Layer

> N/A — `alias_layer.json` returned empty tier counts because the CSS uses class utilities and environment tokens more than extractable custom property aliases.

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency signal |
|---|---|---|
| `surface-base` | `#FFFFFF` / `#FFF` | highest surface and text-over-image usage |
| `text-primary` | `#000000` / `#000` | primary UI text and button fill |
| `border-default` | `#DADADA` | high-frequency border/disabled tone |
| `disabled-muted` | `#ABABAB` | disabled text and light UI detail |
| `brand-red` | `#E00` | repeated brand/status/action accent |
| `surface-muted` | `#F4F4F4` | muted commerce backgrounds |
| `link-blue` | `#005DB5` | link/focus utility |

### 06-8. Color Stories

**`{colors.brand-red}` (`#E00`)** — UNIQLO red is a stamp, not a wash. It belongs to the square logo, status emphasis, sale memory, and small state signals. Using it for every CTA makes the site feel like a discount banner instead of LifeWear retail.

**`{colors.surface-base}` (`#FFFFFF`)** — The page floor is plain white so product photography stays legible and purchasable. White also keeps the commerce UI from fighting lifestyle imagery.

**`{colors.text-primary}` (`#000000`)** — Black is the true action color. Primary buttons use black fills, nav uses black/white contrast, and product information remains uncompromised.

**`{colors.border-default}` (`#DADADA`)** — Gray borders do the structural work. Cards, secondary buttons, disabled states, and separators rely on hairline neutrality instead of decorative color.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--spacing4` | `4px` | tight icon/text offset |
| `--spacing8` | `8px` | small gaps, control internals |
| `--spacing12` | `12px` | compact vertical rhythm |
| `--spacing16` | `16px` | default card/text spacing |
| `--spacing24` | `24px` | common component gap and card padding |
| `--spacing32` | `32px` | section grouping |
| `--spacing40` | `40px` | larger band rhythm |
| `--spacing48` | `48px` | hero/category transitions |
| `--spacing88` | `88px` | large commerce/display separation |

**주요 alias**:
- `gap: 24px` → repeated commerce grid/card rhythm.
- `height: 44px` → carousel and touch controls.
- `padding: 16px` / `24px` → card and panel density.

### Whitespace Philosophy

UNIQLO uses air as a retail sorting tool, not as luxury emptiness. The hero has enough open image space to let clothing and body silhouette register. Immediately below, category and product modules compress into a more operational rhythm where 16px and 24px dominate.

This creates the essential contrast: open photography above, dense marketplace below. The page should never feel like a boutique lookbook all the way down. It should feel like a store that borrowed editorial framing only where it helps the product.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| `radius-none` | `0` | chips, cards, buttons, most commerce frames |
| `radius-circle` | `50%` | icon buttons, circular controls |
| `radius-pill` | `999px` | search bar and select pill controls |
| `radius-small` | `8px`-`10px` | occasional overlays or system panels |
| `radius-large` | `16px`-`20px` | limited app-like components, not the dominant visual language |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `none` | `none` | default chrome; most cards do not float |
| `focus-soft` | `0 0 0 10px #1b1b1b33` | accessibility/focus ring style |
| `overlay-soft` | `0 2px 4px #0003` | overlays and light separation |
| `image-legibility` | text shadow via env tokens | hero/banner text over photography |
| `strong-outline` | `0 1px 1px #0009` | selected/overlay state |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `motion-standard` | `all .4s cubic-bezier(.4,0,.2,1)` | panels, overlays, menu-like transitions |
| `motion-fast-color` | `color .18s cubic-bezier(.4,0,.2,1)` | link/control color state |
| `motion-fast-border` | `border-color .18s cubic-bezier(.4,0,.2,1)` | secondary button and borders |
| `motion-opacity` | `opacity .3s` / `.4s` | carousel, overlays, visibility changes |
| `motion-transform` | `transform .2s` / `.4s` | swipeable and overlay state |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: 1176px and 1200px are common large-container signals; 1248px appears for larger limits.
- **Grid type**: CSS Grid and Flexbox mixed; product/category areas use grid/flex, carousel uses Swiper flex track.
- **Column count**: responsive commerce grids; category tiles observed in 2x/3x image ratios, desktop density above 960px.
- **Gutter**: 16px / 24px / 32px are the main gutters.

### Hero
- **Pattern Summary**: 80-100vh-feeling full-bleed lifestyle image + overlaid nav/search + left-bottom product copy + price.
- Layout: full-width image banner with text overlay and persistent top navigation.
- Background: photography, not gradient or illustration.
- **Background Treatment**: image-overlay through shadow/text legibility utilities (`media-banner__shadow-bottom-2`) rather than a visible color scrim.
- H1: `32px` / weight `300-400` / tracking `.36px` in observed localized hero.
- Max-width: full viewport image; text block sits inside the image area rather than a separate card.

### Section Rhythm

```css
section-like-commerce-band {
  padding: 16px 24px;
  max-width: 1176px;
  gap: 24px;
}
```

### Card Patterns
- **Card background**: `#FFFFFF`, with muted variant `#F4F4F4`.
- **Card border**: `1px solid #DADADA`; strong variant `1px solid #767676`.
- **Card radius**: mostly `0`.
- **Card padding**: `16px` or `24px`.
- **Card shadow**: none by default; separation via border/background.

### Navigation Structure
- **Type**: horizontal top navigation with category links, search field, account/favorite/cart/menu icons.
- **Position**: visually over hero in the captured artifact; treat as sticky/static top chrome depending page state.
- **Height**: controls cluster around 44px; header visual height around 64px-72px.
- **Background**: transparent/over-image on hero, white overlay panels for menus.
- **Border**: minimal; active category uses underline rather than boxed tab.

### Content Width
- **Prose max-width**: narrow text overlays; product/category copy avoids long prose.
- **Container max-width**: 1176px/1200px family.
- **Sidebar width**: not observed on homepage artifact; likely used in listing/filter subflows, not confirmed here.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `max-width: 599px` | dominant mobile cutoff; many rules target small screens. |
| Tablet | `600px-959px` | medium layout, intermediate grid/header behavior. |
| Desktop | `min-width: 960px` | full commerce/navigation layout. |
| Large | `1201px+` / `1249px+` | larger container and desktop refinements. |

### Touch Targets
- **Minimum tap size**: 44px appears repeatedly for carousel/navigation buttons.
- **Button height (mobile)**: 44px/52px family.
- **Input height (mobile)**: search controls around 38px-44px depending variant.

### Collapsing Strategy
- **Navigation**: category links collapse toward icon/menu patterns on smaller screens.
- **Grid columns**: product/category grids reduce at 960px and 600px thresholds.
- **Sidebar**: not confirmed on homepage artifact.
- **Hero layout**: image remains dominant; overlay copy and header controls compress.

### Image Behavior
- **Strategy**: ratio utilities (`image--ratio-1x1`, `2x1`, `3x1`) and full-width responsive imagery.
- **Max-width**: 100% for imagery; container widths handle layout.
- **Aspect ratio handling**: explicit ratio classes rather than arbitrary image cropping.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary button**

| Property | Value |
|---|---|
| Class | `.fr-ec-button--variant-primary` |
| Background | `#000000` |
| Text | `#FFFFFF` |
| Radius | `0` unless a special pill/icon variant is used |
| Hover/active | `#2A2A2A` |
| Disabled | `#DADADA`, no border |

```html
<button class="fr-ec-button fr-ec-button--variant-primary">
  <span class="fr-ec-label">Add to cart</span>
</button>
```

**Secondary button**

| Property | Value |
|---|---|
| Class | `.fr-ec-button--variant-secondary` |
| Background | `#FFFFFF` |
| Text | `#000000` |
| Border | `1px solid #1B1B1B` |
| Active border/text | `#6A6A6A` |
| Disabled text | `#ABABAB` |

### Badges

Badges are compact commerce/editorial labels. In the observed hero, the topic badge is a small filled rectangle over photography, not a rounded marketing pill. Keep typography white, compact, and utility-like. For sale/status badges, prefer `#E00` or red family tokens only when the state genuinely requires urgency.

### Cards & Containers

Cards are flat store modules:

| Property | Value |
|---|---|
| Class | `.fr-ec-card` |
| Background | `#FFFFFF` |
| Padding | `16px` or `24px` |
| Border normal | `1px solid #DADADA` |
| Border strong | `1px solid #767676` |
| Background variant | `#F4F4F4` |
| Radius | `0` |

### Navigation

Navigation combines category text, logo square, search pill, and utility icons. Active top category uses underline/contrast rather than a filled tab. Search is visually larger than the surrounding icon controls and is allowed to be rounded because search is a functional input, not a brand flourish.

### Inputs & Forms

Search input:

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Height | `38px`-`44px` |
| Radius | `999px` |
| Placeholder | muted gray |
| Icon | left-aligned search icon |
| Width | wide desktop pill; responsive constrained widths around 231px/324px/382px appear in CSS vars |

### Hero Section

Hero is a commerce campaign banner:

| Property | Value |
|---|---|
| Image | full-bleed lifestyle/product photography |
| Text placement | lower-left overlay in captured artifact |
| Text color | `#FFFFFF` over image |
| Title | 32px light/regular |
| Price | large, high-contrast, product-commerce explicit |
| Header | overlaid nav/search/icons |

### 13-2. Named Variants

**button-primary-black** — the default transactional action.

| State | Spec |
|---|---|
| default | `background-color: #000000; color: #FFFFFF; border: none` |
| hover | `background-color: #2A2A2A` |
| active | `background-color: #2A2A2A` |
| disabled | `background-color: #DADADA; border: none` |

**button-secondary-outline** — the neutral alternative action.

| State | Spec |
|---|---|
| default | `background-color: #FFFFFF; color: #000000; border: 1px solid #1B1B1B` |
| active | `border-color: #6A6A6A; color: #6A6A6A` |
| disabled | `color: #ABABAB` |

**search-pill-desktop** — the only major rounded chrome element.

| State | Spec |
|---|---|
| default | white pill, `999px` radius, search icon left |
| focus | strong accessible outline/focus ring rather than decorative shadow |
| responsive | width constrained by 231px/324px/382px variable family |

**card-border-normal** — standard commerce panel.

| State | Spec |
|---|---|
| default | `#FFFFFF`, `1px solid #DADADA`, no shadow |
| strong | `1px solid #767676` |
| muted | `background-color: #F4F4F4` |

### 13-3. Signature Micro-Specs

#### red-as-stamp

```yaml
red-as-stamp:
  description: "UNIQLO red (#E00) is a brand stamp, not a CTA palette."
  technique: "#E00 reserved for logo and compact status accents only; never used as button background; commerce controls use black instead."
  applied_to: ["{component.logo}", "status flag", "narrow brand accent line"]
  visual_signature: "the page carries brand memory through a single saturated mark — like a postal seal on a folded shirt."
  intent: "a global retail brand needs one mnemonic colour that survives any photography crop; CTAs are operational and earn black."
```

#### black-transactional-button

```yaml
black-transactional-button:
  description: "Action is a black rectangle. Hover deepens, never softens."
  technique: "background #000000, hover/active #2A2A2A, color #FFFFFF, radius 0, weight 600, padding 12-16px vertical."
  applied_to: ["{components.button-primary}", "Add to cart", "Continue", "Login"]
  visual_signature: "every commerce action looks like a bar code stamp — heavy, square, deliberate."
  intent: "fashion retail competes with editorial whitespace; the action must out-weight the photo without competing for hue."
```

#### square-commerce-chrome

```yaml
square-commerce-chrome:
  description: "Radius 0 dominates the site — UNIQLO is engineered like a paper catalogue, not a rounded SaaS app."
  technique: "border-radius: 0 on cards, chips, product modules, buttons; radius is spent only on search pills (999px) and circular icon controls (50%)."
  applied_to: ["{component.product-card}", "{component.chip}", "{components.button-primary}"]
  visual_signature: "the entire grid feels like printed retail — corners snap to a paper edge, never a screen pillow."
  intent: "fashion identity at scale needs a typographic floor — radius softens type; sharp corners keep the page silent."
```

#### photography-legibility-shadow

```yaml
photography-legibility-shadow:
  description: "Drop shadow exists exclusively to keep banner copy legible over lifestyle imagery."
  technique: "text-shadow / linear-gradient overlay utilities applied only to text rendered on top of photography; chrome cards never receive shadow."
  applied_to: ["{component.hero-banner}", "campaign overlay caption"]
  visual_signature: "shadow is a typographic concession to photography, never a decorative depth move."
  intent: "fashion photography must lead; shadow is borrowed from the image only when type would otherwise vanish."
```

#### locale-typography-switch

```yaml
locale-typography-switch:
  description: "Font stack and base size shift per language context — UNIQLO is not one global marketing page."
  technique: "CSS [lang=\"ja\"] / [lang=\"ko\"] selectors swap to Hiragino Kaku Gothic Pro / Noto Sans CJK; base size lifted ~1px to compensate for ideographic density."
  applied_to: ["{typography.body}", "{typography.display}", "category navigation"]
  visual_signature: "Japanese and Korean shoppers see a page that looks native, not a translated layer."
  intent: "operational international retail must respect script-level legibility; one font globally would feel imported."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Product-first, plain, seasonal/use-case oriented | "Wide Leg Pants" / "Women's Clothing & Accessories" |
| Primary CTA | Direct shopping verbs; no clever phrasing | "Shop now", "Add to cart" |
| Secondary CTA | Category and utility navigation | "Women", "Men", "Kids", "Baby" |
| Subheading | Practical benefit, size, season, material, or offer detail | "stylish and comfortable clothes" |
| Tone | Functional, calm, democratic, product-led | retail clarity over fashion mystique |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* UNIQLO-inspired commerce system */
:root {
  /* Fonts */
  --uq-font-family: "UniqloProRegular", "Helvetica Neue", Helvetica, Arial, system-ui, -apple-system, sans-serif;
  --uq-font-family-cjk: "Hiragino Kaku Gothic Pro", "Hiragino Sans", "Noto Sans CJK JP", "Meiryo", sans-serif;
  --uq-font-weight-light: 300;
  --uq-font-weight-normal: 400;
  --uq-font-weight-semibold: 600;

  /* Brand */
  --uq-color-brand-red: #E00;
  --uq-color-brand-red-dark: #C00;

  /* Surfaces */
  --uq-bg-page: #FFFFFF;
  --uq-bg-muted: #F4F4F4;
  --uq-text: #000000;
  --uq-text-muted: #6A6A6A;
  --uq-border: #DADADA;
  --uq-border-strong: #767676;

  /* Key spacing */
  --uq-space-xs: 4px;
  --uq-space-sm: 8px;
  --uq-space-md: 16px;
  --uq-space-lg: 24px;
  --uq-space-xl: 32px;

  /* Radius */
  --uq-radius-none: 0;
  --uq-radius-pill: 999px;
  --uq-radius-circle: 50%;
}

.uq-button-primary {
  background: var(--uq-text);
  color: var(--uq-bg-page);
  border: 0;
  border-radius: var(--uq-radius-none);
  min-height: 44px;
  padding: 0 24px;
  font-weight: 600;
}

.uq-button-primary:hover,
.uq-button-primary:active {
  background: #2A2A2A;
}

.uq-card {
  background: var(--uq-bg-page);
  border: 1px solid var(--uq-border);
  border-radius: 0;
  box-shadow: none;
  padding: 24px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js - UNIQLO-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        uniqlo: {
          red: '#E00',
          redDark: '#C00',
          black: '#000000',
          ink: '#1B1B1B',
          hover: '#2A2A2A',
          muted: '#6A6A6A',
          border: '#DADADA',
          surface: '#FFFFFF',
          surfaceMuted: '#F4F4F4',
        },
      },
      fontFamily: {
        sans: ['UniqloProRegular', 'Helvetica Neue', 'Helvetica', 'Arial', 'system-ui', 'sans-serif'],
      },
      fontWeight: {
        light: '300',
        normal: '400',
        semibold: '600',
      },
      borderRadius: {
        none: '0',
        pill: '999px',
      },
      boxShadow: {
        none: 'none',
        overlay: '0 2px 4px #0003',
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
| Brand primary | `colors.brand-red` | `#E00` |
| Background | `colors.surface-base` | `#FFFFFF` |
| Text primary | `colors.text-primary` | `#000000` |
| Text muted | `colors.text-secondary` | `#6A6A6A` |
| Border | `colors.border-default` | `#DADADA` |
| Surface muted | `colors.surface-muted` | `#F4F4F4` |
| Link | `colors.link-blue` | `#005DB5` |

### Example Component Prompts

#### Hero Section
```text
UNIQLO-style commerce hero를 만들어줘.
- full-bleed lifestyle/product photography를 배경으로 사용
- 상단에는 빨간 정사각형 로고, category nav, white rounded search pill, utility icons
- H1/product title: UniqloProRegular or Helvetica fallback, 32px, weight 300/400, white
- product price는 large white text로 명확히
- CTA가 필요하면 red가 아니라 black/white commerce button 사용
- decorative gradient, glass card, purple accent는 쓰지 말 것
```

#### Card Component
```text
UNIQLO-style product/category card를 만들어줘.
- background: #FFFFFF
- border: 1px solid #DADADA, radius: 0, shadow: none
- padding: 16px or 24px
- title: 13-17px, weight 400, color #000000
- muted text: #6A6A6A
- product image owns the card; chrome stays quiet
```

#### Navigation
```text
UNIQLO-style navigation을 만들어줘.
- logo: red square #E00 with white UNIQLO lettering area
- nav links: uppercase/simple category labels, 13-14px, white over hero or black on white surface
- active link: underline or stronger contrast, not filled tab
- search: wide #FFFFFF pill with 999px radius and muted placeholder
- icon buttons: 44px touch target, minimal line icons
```

### Iteration Guide

- **색상 변경 시**: red is brand memory; black is primary action.
- **폰트 변경 시**: use 300/400/600. Avoid 500 unless the real flow proves it.
- **여백 조정 시**: stay on 8/16/24/32/48 rhythm.
- **새 컴포넌트 추가 시**: default to square radius and border separation.
- **사진 추가 시**: product/lifestyle image should do the emotional work; UI should stay plain.
- **반응형**: keep 600px and 960px breakpoints unless a target subflow proves otherwise.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#E00` as brand stamp/accent, not as the universal action color.
- Use black primary commerce buttons with `#2A2A2A` hover/active.
- Keep most cards and commerce modules square with `border-radius: 0`.
- Let lifestyle/product photography carry atmosphere.
- Use `#DADADA` and `#767676` borders for structure.
- Preserve 44px touch targets for icon/carousel controls.
- Use locale-aware sans stacks for English/CJK surfaces.
- Keep motion practical: opacity, transform, and color transitions under `.4s`.

### ❌ DON'T

- 배경을 `#FAFAFA` 또는 `#F8F8F8` 중심으로 두지 말 것 — 대신 `#FFFFFF` 사용.
- 기본 텍스트를 `#111111` 또는 `#1D1D1F`로 두지 말 것 — 대신 `#000000` 사용.
- primary CTA 배경을 `#E00`로 두지 말 것 — 대신 `#000000` 사용.
- hover/active black을 `#333333`로 임의 대체하지 말 것 — 대신 `#2A2A2A` 사용.
- standard border를 `#E5E7EB`로 두지 말 것 — 대신 `#DADADA` 사용.
- muted text를 `#9CA3AF`로 두지 말 것 — 대신 `#6A6A6A` 사용.
- product card 배경을 `#F9FAFB`로 두지 말 것 — 기본은 `#FFFFFF`, muted variant는 `#F4F4F4` 사용.
- body에 `font-weight: 500`을 기본으로 쓰지 말 것 — `400` 기본, `600` 강조, `300` editorial light 사용.
- 모든 버튼에 `border-radius: 8px`를 주지 말 것 — 기본 commerce chrome은 `0`, search/icon만 `999px`/`50%`.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Brand gradient: **none** — UNIQLO red is flat and square, never a wash.
- Universal red CTA: **absent** — red is never the transactional default; the carry of the 매대/카운터 stays black.
- Rounded card system: **absent** — commerce cards and chips are square by default; pill softness is zero in the catalog grid.
- Heavy decorative shadows: **zero** — borders and photography create structure inside the marketplace 진열대.
- Purple/blue SaaS accent palette: **absent** — blue appears only as utility/link, never as brand mood.
- Negative luxury tracking: **never** — tracking is neutral or slightly positive across all utilities.
- Weight 500 as a core step: **absent** in observed CSS — 300/400/600 only.
- Illustration-led hero: **none** — real product/lifestyle photography is the only hero material.
- Glassmorphism panels: **absent** — white surfaces are solid, utilitarian, warehouse-grade.
- Overwritten brand palette: **never** — black/white/red/gray is the entire system, no extras.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Custom property extraction gap** — `resolved_tokens.json` reported `total_vars: 0`, so named tokens in this guide are normalized from observed CSS/classes rather than literal CSS custom property names.
- **Locale mismatch in screenshot** — requested URL is `https://www.uniqlo.com/us/en`, but the reused `hero-cropped.png` displays Korean-localized homepage content. The design language appears consistent, but copy and current hero campaign may differ from the live US page.
- **Single-page scope** — homepage/category artifact only. Checkout, account, cart, size selector, store locator, and error states were not visited.
- **Subflow form states unconfirmed** — search input is observed; validation, loading, payment, and address error states are inferred only from shared component CSS.
- **Dark mode not proven** — CSS includes black/white variants, but a complete dark theme was not confirmed.
- **Motion runtime not executed** — CSS transitions and Swiper classes were summarized; JavaScript-driven carousel timing, lazy loading, and menu animation details were not measured live.
- **Exact image treatment may drift** — hero photography, campaign badge, and product price are content-managed and likely change frequently.
- **Frequency contamination possible** — CSS contains utility colors for status, focus, and component libraries; logo/status colors were manually separated from core UI recommendations.
- **Report HTML skipped by instruction** — Step 6 RENDER-HTML was intentionally not run; this file is the only requested output.
