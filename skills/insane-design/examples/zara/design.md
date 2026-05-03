---
schema_version: 3.2
slug: zara
service_name: ZARA
site_url: https://www.zara.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#000000"
primary_font: "Helvetica Now Text"
font_weight_normal: 300
token_prefix: zds

bold_direction: Monochrome Luxury
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: luxury-brand
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "phase1 found 1069 CSS variables, 885 resolved tokens, mds/zds component tokens, and consistent commerce UI patterns."

colors:
  brand-black: "#000000"
  brand-white: "#FFFFFF"
  surface-page: "#FFFFFF"
  surface-inverse: "#000000"
  text-primary: "#000000"
  text-inverse: "#FFFFFF"
  text-muted: "#666666"
  text-soft: "#949494"
  hairline: "#D8D8D8"
  surface-soft: "#F2F2F2"
  action-hover: "#C9C9C9"
  focus-blue: "#348DED"
  sale-green: "#23F444"
  danger-red: "#FF3E33"
typography:
  display: "Helvetica Now Text"
  body: "Helvetica Now Text"
  editorial_alt: "Times New Roman"
  ladder:
    - { token: body-s, size: "0.625rem", weight: 300, line_height: "1rem", tracking: "0" }
    - { token: body-m, size: "0.75rem", weight: 300, line_height: "1.125rem", tracking: "0" }
    - { token: body-l, size: "0.8125rem", weight: 300, line_height: "1.25rem", tracking: "0" }
    - { token: label-m-highlight, size: "0.75rem", weight: 500, line_height: "1rem", tracking: "0.05rem" }
    - { token: title-l, size: "1rem", weight: 300, line_height: "1.5rem", tracking: "0" }
    - { token: menu-universe, size: "2.5rem", weight: 400, line_height: "2.5rem", tracking: "-0.1875rem" }
  weights_used: [300, 400, 500, 600, 700]
  weights_absent: []
components:
  button-primary: { bg: "{colors.brand-white}", color: "{colors.brand-black}", radius: "0rem", height: "2.5rem", padding: "0.75rem 0.75rem" }
  button-secondary: { bg: "{colors.brand-black}", color: "{colors.brand-white}", radius: "0rem", height: "2rem", padding: "0.75rem 0.75rem" }
  nav-link: { color: "{colors.brand-black}", size: "0.75rem", weight: 300, tracking: "0" }
  product-card: { bg: "transparent", radius: "0", shadow: "none", media_fit: "cover" }
  form-input: { border: "{colors.text-soft}", focus: "{colors.brand-black}", radius: "0" }
---

# DESIGN.md — ZARA (Designer Guidebook)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

ZARA stages its collection like a museum-grade vitrine after closing time — a monochrome canvas where photography is the exhibit, and the UI chrome clings to the edges like frame annotations on a silent gallery wall.

The palette is deliberately anti-palette. The working identity is black, white, gray, and photography. `#000000` (`{colors.brand-black}`) and `#FFFFFF` (`{colors.brand-white}`) are not merely neutral defaults here; they are the brand system. Chromatic colors exist, but they are operational states: focus `#348DED`, sale/status `#23F444`, error `#FF3E33`, and cookie/privacy UI. None of those colors should be promoted into brand mood.

The typography is where the system becomes recognizably Zara. Most UI copy sits small, light, and narrow: 10-13px equivalents, weight 300, almost no ornament. Then the menu universe and campaign layer can snap into large compressed editorial words with negative tracking, including `--letter-spacing-menu-universe: -0.1875rem` at the widest tier. This jump from quiet commerce parchment to billboard-scale fashion type is the signature tension.

Spacing is also editorial, not dashboard-like. The homepage lets photography occupy nearly the whole viewport while side utilities cling to the edge. Product and category structures become dense only after the campaign surface; the brand gives air to images, then compresses buying choices into disciplined lists, carousels, and square-edged controls.

The correct metaphor is a storefront vitrine: the canvas is reflective, the mannequins are lit, and the price tags are tiny. Implementation should preserve that restraint. If the UI starts looking colorful, rounded, shadowed, or friendly, it stops being Zara — the museum does not add signage where the artifact speaks for itself.

To stretch the picture: the menu universe drawer behaves like the brass-handled doors of a couture atelier swinging open onto a marble corridor, the campaign type lands like the runway show title projected onto the back wall in 4K silence, and the product carousel scrolls like a sample rack on wheels rolled past a stylist's station. The login and bag controls are dressmaker's pins along the margin — present, never decorative. The hairline border between thumbnails is the chalk line a tailor leaves on dark fabric. There is no second brand color because a luxury showroom's lighting plan is reserved for the garments, not the signage.

### Key Characteristics

- Monochrome identity: `#000000` / `#FFFFFF` carry almost every brand decision.
- Full-bleed editorial photography leads the page; UI chrome stays subordinate.
- Huge brand/editorial lettering can coexist with 10-13px utility copy.
- Buttons and inputs are square, not pill-shaped; radius tokens resolve to `0rem`.
- Body and navigation copy often use weight `300`; emphasis uses `500` or `700` sparingly.
- Category/menu systems are dense and list-like, not card-heavy.
- Shadows are effectively absent from primary commerce chrome.
- Motion is restrained: opacity/transform transitions, not playful bounce.
- Semantic colors are state colors only, never secondary brand colors.
- Product imagery does the emotional work that color would do on many marketplaces.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Monochrome Luxury
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **full-bleed campaign photography plus almost-invisible commerce chrome**으로 기억된다.
> **Code Complexity**: high — CSS includes a large mds/zds token system, responsive grids, carousels, media panels, form controls, and stateful commerce components.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 ZARA처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Helvetica Now Text", "Helvetica", "Arial", sans-serif;
  font-weight: 300;
  letter-spacing: 0;
}

/* 2. 배경 + 텍스트 */
:root {
  --zds-bg-page: #FFFFFF;
  --zds-fg: #000000;
  --zds-muted: #666666;
}
body {
  background: var(--zds-bg-page);
  color: var(--zds-fg);
}

/* 3. 브랜드 컬러 */
:root {
  --zds-brand: #000000;
  --zds-inverse: #FFFFFF;
}
```

**절대 하지 말아야 할 것 하나**: Zara를 "검정 로고가 있는 일반 쇼핑몰"로 만들지 말 것. 카드, 그림자, 둥근 CTA, 컬러 배지를 늘리는 순간 editorial luxury가 사라진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.zara.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Reused artifacts | `insane-design/zara/phase1/*.json`, `insane-design/zara/css/*`, `insane-design/zara/index.html`, `insane-design/zara/screenshots/hero-cropped.png` |
| HTML size | 1,946,653 bytes |
| CSS files | 13 external/inline CSS files, 919,039 combined CSS bytes |
| Token prefix | `zds`, `mds`, plus legacy `color-*` aliases |
| Method | Existing phase1 token extraction + targeted CSS/HTML/screenshot interpretation |
| Token extraction | 1,069 CSS variables, 885 resolved tokens, 184 unresolved tokens |
| Top runtime hex | `#FFFFFF`, `#000000`, `#D8D8D8`, `#6B6B6B`, `#C9C9C9` |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Server-rendered ecommerce application with large client runtime payloads and SDUI-style classes (`sdui-layout`, `sdui-media`, `sdui-carousel-item`).
- **Design system**: Zara/ZDS + MDS token layers — prefixes `--zds-*`, `--mds-*`, `--color-*`, `--font-*`, `--spacing-*`.
- **CSS architecture**:
  ```text
  core       (--color-*, --mds-color-*)          raw color and semantic state values
  typography (--font-*, --mds-typo-*)           font, size, line-height, weight, tracking
  component  (--mds-button-*, --input-*)        button, field, dialog, dropdown, switch
  layout     (--grid-*, --spacing-*)            grid spacing, responsive columns, category/menu rhythm
  ```
- **Class naming**: mixed BEM + generated SDUI classes. Examples: `layout-categories-category`, `slider-spot__slide`, `media-panel__media`, `ecs-media-image__image`.
- **Default theme**: mixed. The extracted app shell contains both `#FFFFFF` page surfaces and dark/inverse control mappings.
- **Font loading**: custom commercial font family names appear in CSS: `"Helvetica Now Text"`, `"Neue Helvetica for Zara"`, plus editorial alternates like `"Times New Roman"`, `"Apercu"`, `"Gilroy"`, `"ZaraAthleticz"`.
- **Canonical anchor**: homepage hero/campaign carousel with full-bleed image/video and side utility nav.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Helvetica Now Text` (commercial/proprietary; not safe to assume available)
- **Editorial alternate**: `Times New Roman` via `--font-family-alt`, mostly for campaign/editorial title variants
- **Special campaign families**: `Apercu`, `XXemeEtageRegular`, `ZaraAthleticz`, `Gilroy` appear as collection-specific overlays
- **Code font**: no brand code font observed; use `ui-monospace` only for implementation docs
- **Weight normal / bold**: `300` / `500` or `700` depending on component tier

```css
:root {
  --zds-font-family-main: "Helvetica Now Text", "Helvetica", "Arial", sans-serif;
  --zds-font-family-alt: "Times New Roman";
  --zds-font-weight-light: 300;
  --zds-font-weight-regular: 400;
  --zds-font-weight-medium: 500;
  --zds-font-weight-bold: 700;
}
body {
  font-family: var(--zds-font-family-main);
  font-weight: var(--zds-font-weight-light);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Helvetica Now Text** — closest substitute is `Helvetica Neue` on Apple systems, then `Arial`. Keep the default weight at `300`; using `400` everywhere makes the chrome too heavy.
- **Menu universe display** — if the exact Zara campaign font is unavailable, use `Helvetica Neue Condensed` or `Arial Narrow` only for oversized category/menu words, then apply `letter-spacing: -0.12rem` to `-0.1875rem` depending on viewport.
- **Editorial serif alternates** — use `Times New Roman` directly where `--font-family-alt` appears. Do not replace it with a fashionable web serif; the slightly plain system serif is part of the contrast.
- **Line-height correction** — body-m should stay around `0.75rem / 1.125rem`; increasing to common `16px / 24px` breaks Zara's compact commerce rhythm.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `--font-size-body-s` | `0.625rem` | `300` | `1rem` | `0` |
| `--font-size-body-m` | `0.75rem` | `300` | `1.125rem` | `0` |
| `--font-size-body-l` | `0.8125rem` | `300` | `1.25rem` | `0` |
| `--font-size-label-s` | `0.6875rem` | `300` | `1rem` | `0` |
| `--font-size-label-m` | `0.75rem` | `300` | `1rem` | `0` |
| `--font-size-label-m-highlight` | `0.75rem` | `500` | `1rem` | `0.05rem` |
| `--font-size-title-m` | `0.8125rem` | `300` | `1.25rem` | `0` |
| `--font-size-title-l` | `1rem` | `300` | `1.5rem` | `0` |
| `--font-size-menu-index` | `0.8125rem` | `300` | `1.25rem` | `0` |
| `--font-size-menu-item` | `1.125rem` | `300` | `1.25rem` | `0` |
| `--font-size-menu-universe` | `2.5rem` | `400` | `2.5rem` | `-0.1875rem` |
| `--font-size-srpls-name` | `1.375rem` | observed normal | `1.5rem` | collection-specific |

> ⚠️ 핵심: Zara의 UI는 일반 16px 본문 기반이 아니다. 쇼핑 chrome은 10-13px 등급으로 작게 유지되고, campaign/menu 순간에만 타이포가 커진다.

### Principles
<!-- SOURCE: manual -->

1. Body chrome begins at 10-12px equivalents, not 16px. The site earns luxury by making utility text quiet.
2. Weight `300` is not decorative; it is the baseline for body, label, title, menu index, and menu item tokens.
3. `500` and `700` are emphasis tools, not the default. Use them for highlighted labels, selected category states, and semantic UI states.
4. Negative tracking belongs to oversized menu/campaign typography. Body and label copy mostly keep `0` or tiny positive tracking.
5. Serif and special families are collection accents. Do not spread them across the interface.
6. Large type should be image-adjacent or menu-specific; generic section headings should remain compact.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (monochrome)
<!-- SOURCE: auto -->

| Token | Hex |
|---|---:|
| `--color-basic-black` | `#000000` |
| `--color-basic-white` | `#FFFFFF` |
| `--color-main-000` | `#000000` |
| `--color-main-005` | `#333333` |
| `--color-main-010` | `#666666` |
| `--color-main-020` | `#999999` |
| `--color-main-040` | `#CCCCCC` |
| `--color-main-060` | `#E5E5E5` |
| `--color-main-080` | `#F2F2F2` |

### 06-2. Brand Dark Variant
<!-- SOURCE: auto -->

| Token | Hex |
|---|---:|
| `--mds-color-bg-default` | `#000000` |
| `--mds-color-bg-inverse` | `#FFFFFF` |
| `--mds-color-content-default` | `#FFFFFF` |
| `--mds-color-content-inverse` | `#000000` |
| `--color-background-low` | `#141414` |
| `--color-background-low-alt` | `#262626` |
| `--color-background-mid` | `#595959` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light / white-side | Dark / black-side |
|---|---:|---:|
| 000 | `#FFFFFF` | `#000000` |
| 100 | `#F8F8F8` | `#0D0D0D` |
| 200 | `#F2F2F2` | `#1B1B1B` |
| 300 | `#E5E5E5` | `#262626` |
| 400 | `#D8D8D8` | `#333333` |
| 500 | `#C9C9C9` | `#363636` |
| 600 | `#949494` | `#5E5E5E` |
| 700 | `#6B6B6B` | `#797979` |

### 06-4. Accent Families
<!-- SOURCE: auto -->

| Family | Key step | Hex | Usage |
|---|---|---:|---|
| Blue | `--mds-color-blue-500` / focus | `#0170E9`, `#348DED` | focus/info states, not brand |
| Green | `--color-sales`, `--color-done` | `#23F444`, `#34C759` | sale, done, success |
| Red | `--mds-color-danger-mid`, `--color-emphasis` | `#FF3E33`, `#FF3B30` | error, emphasis |
| Orange | `--mds-color-orange-500` | `#FF9500` | warning/notification |
| Wonder club blue | `--wonder-club-blue` | `#4354DF` | specific loyalty/feature surface |

### 06-5. Semantic
<!-- SOURCE: auto -->

| Token | Hex | Usage |
|---|---:|---|
| `--color-semantic-danger-high` | `#FF453A` | high danger |
| `--color-semantic-danger-low` | `#330E0C` | low danger background |
| `--color-semantic-info-high` | `#0084FF` | info |
| `--color-semantic-info-low` | `#002140` | info background |
| `--color-semantic-sales` | `#23F444` | sales indicator |
| `--color-semantic-success-high` | `#30D158` | success |
| `--color-semantic-success-low` | `#0A2A12` | success background |
| `--color-semantic-warning-high` | `#FF9F0A` | warning |
| `--color-semantic-warning-low` | `#332002` | warning background |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--chat-button-primary-background-color` | `--color-basic-white` | dark chat primary background |
| `--chat-button-primary-color` | `--color-basic-black` | dark chat primary text |
| `--chat-button-secondary-background-color` | `--color-basic-black` | secondary dark button |
| `--chat-button-secondary-color` | `--color-basic-white` | secondary dark button text |
| `--form-input-label-border-color-unfocused` | `--color-content-mid` | unfocused input border |
| `--zds-input-base-focus-color` | `--color-content-high` | input focus state |
| `--zds-input-base-state-color` | `--color-semantic-danger-high` | input error state |
| `--mds-color-border-focus` | `#348DED` | focus ring |

### 06-7. Dominant Colors (실제 DOM/CSS 빈도 순)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---:|---:|
| white | `#FFFFFF` / `#FFF` | 103 combined CSS hits |
| black | `#000000` / `#000` | 78 combined CSS hits |
| hairline | `#D8D8D8` | 16 |
| muted border | `#6B6B6B` | 15 |
| hover pale gray | `#C9C9C9` | 14 |
| soft gray | `#CCCCCC` / `#CCC` | 13+ |
| content hover | `#949494` | 11 |
| muted text | `#999999` / `#999` | 10 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.brand-black}` (`#000000`)** — Zara's real brand anchor. It is logo, typography, dark controls, overlay contrast, and the absence of chromatic persuasion. Use it as the final word, not as a decorative fill.

**`{colors.brand-white}` (`#FFFFFF`)** — The clean commerce surface and inverse text color. It should feel like empty gallery wall or product-page paper, not a rounded card background.

**`{colors.text-muted}` (`#666666`)** — The quiet utility voice. It keeps secondary text visible without creating a second hierarchy color.

**`{colors.hairline}` (`#D8D8D8`)** — The structural boundary. Use it for separators and subtle edges instead of shadows, tinted panels, or thick borders.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--spacing-00` | `0.125rem` / `0.25rem` | micro offsets |
| `--spacing-01` | `0.25rem` / `0.5rem` | compact gaps |
| `--spacing-02` | `0.5rem` / `0.75rem` | common UI gap |
| `--spacing-03` | `0.75rem` / `1rem` | field and list padding |
| `--spacing-04` | `1rem` / `1.25rem` | standard component spacing |
| `--spacing-05` | `1.25rem` / `1.5rem` | medium vertical rhythm |
| `--spacing-07` | `2rem` / `2.5rem` | large component gap |
| `--spacing-10` | `3.5rem` / `4rem` | section-level spacing |
| `--spacing-13` | `5rem` / `6rem` | editorial breathing room |
| `--grid-template-spacing-01` | `0.625rem` / `3.75rem` | grid template offsets by breakpoint |
| `--grid-template-spacing-12` | `7.5rem` / `45rem` | large grid template endpoint |

**주요 alias**:
- `--mds-button-space-padding-l-l` → `0.75rem` (square button horizontal padding)
- `--mds-button-space-padding-m-l` → `0.75rem` (medium button horizontal padding)
- `--zds-action-cell-icon-x-margin` → `--spacing-02` (action-cell icon spacing)

### Whitespace Philosophy
<!-- SOURCE: manual -->

Zara uses two different kinds of whitespace. The campaign layer gives images almost everything: viewport height, edge proximity, and minimal text interruptions. The commerce layer then compresses sharply into category lists, 2rem-ish gaps, and 0.75rem button padding. That contrast is the rhythm: "editorial first, transactional second."

Do not normalize the page into even SaaS sections. A Zara-like layout should allow a hero image to feel oversized and slightly dominant, while the navigation and product controls remain small enough to feel almost provisional.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `--mds-button-size-radius-l` | `0rem` | large button |
| `--mds-button-size-radius-m` | `0rem` | medium button |
| `--mds-button-size-radius-s` | `0rem` | small button |
| `--mds-button-size-radius-only-icon-l` | `0rem` | icon button |
| common raw radius | `0` | layout chrome and many containers |
| common raw radius | `2px` | small utility/detail controls |
| common raw radius | `3px` / `4px` | minor form or third-party surfaces |
| circular | `50%` | indicators, icons, toggles |

The brand-facing rule is square. Rounded values exist in secondary widgets and system controls, but product cards, campaign media, and primary buttons should not become soft pills.

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| chrome | `none` / transparent elevation tokens | main commerce UI |
| imagery | not tokenized as UI elevation | depth comes from photography |
| switch/knob utility | `rgba(0, 0, 0, 0.08)` style utility shadow | form controls only |
| overlay | `rgba(0, 0, 0, 0.7)` | modal/overlay dimming |

Zara does not use a card-elevation vocabulary for the main page. If a card needs separation, prefer image crop, whitespace, and `#D8D8D8` hairline.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| common quick fade | `.1s ease` | micro state changes |
| common state transition | `all .2s ease` / `all .2s ease-in` | controls |
| media reveal | `opacity .3s ease-in-out` | image/video reveal |
| carousel/overlay fade | `opacity 450ms ease-in-out` | campaign panels |
| reduced motion | `@media (prefers-reduced-motion: reduce)` | accessibility branch present |

Motion should feel editorial and mechanical. Use fades, controlled transforms, and carousel movement. Avoid springy card lift, playful button bounce, and shadow animation.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: fluid/full viewport for campaign surfaces; constrained product and dialog content appears in component-specific widths such as `600px`, `750px`, and percentage limits.
- **Grid type**: CSS Grid and Flexbox mixed. Extracted grid templates include `repeat(var(--zds-layout-columns), minmax(0, 1fr))`, `1fr 1fr`, `auto 1fr`, and `auto 1fr auto`.
- **Column count**: tokenized layout columns through `--zds-layout-columns`; visible campaign/product structures rely heavily on carousel/media panels.
- **Gutter**: common gaps map to `--spacing-02`, `--spacing-04`, `--spacing-05`, with grid-specific values from `0.625rem` to large editorial offsets.

### Hero

- **🆕 Pattern Summary**: near-full viewport + editorial campaign image/video + oversized brand/category typography + edge utility navigation.
- Layout: full-bleed image/video carousel with overlay/editorial content and side utility controls.
- Background: photography/video, often darkened by actual image tone or overlay.
- **🆕 Background Treatment**: image/video-led, not gradient-led; screenshot shows duplicated campaign photography and giant `ZARA` letterforms under a cookie overlay.
- H1 / campaign type: variable. Menu universe can reach `2.5rem` with `letter-spacing: -0.1875rem`; campaign imagery can carry much larger embedded type outside CSS text.
- Max-width: hero media is viewport-driven; controls and text are edge-aligned.

### Section Rhythm

```css
section {
  padding: var(--spacing-04) var(--spacing-04);
  max-width: 100%;
}

.campaign-surface {
  min-height: 100vh;
  display: grid;
  grid-template-columns: repeat(var(--zds-layout-columns), minmax(0, 1fr));
}
```

### Card Patterns

- **Card background**: transparent or image-dominant; product surface does not read as a raised card.
- **Card border**: none by default; hairlines/separators appear where needed.
- **Card radius**: `0`.
- **Card padding**: compact; list/card gaps use `--spacing-02` to `--spacing-05`.
- **Card shadow**: none.
- **Hover**: subtle opacity, text decoration, or color shift; no large transform/lift.

### Navigation Structure

- **Type**: horizontal/edge utility nav plus deep category menu tree.
- **Position**: visually fixed or persistent at viewport edge in the captured homepage; exact sticky behavior not fully measured.
- **Height**: not a heavy navbar band; controls are text-like.
- **Background**: transparent/over-media or white depending on route state.
- **Border**: none or hairline; not a boxed header.

### Content Width

- **Prose max-width**: narrow utility/copy blocks; not a blog-style prose measure.
- **Container max-width**: mostly fluid, with product/dialog surfaces constrained ad hoc.
- **Sidebar width**: category/menu and utility columns appear as edge systems rather than thick dashboard sidebars.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `max-width: 767px` / `width <= 47.9375rem` | compact navigation, mobile category/menu behavior |
| Tablet | `min-width: 48rem` / `768px` | major token and layout shift; most frequent breakpoint |
| Desktop | `min-width: 64rem` / `1024px` | desktop menu/media layout expansion |
| Wide | `min-width: 85.4375rem` | additional editorial/grid tuning |
| Large | `min-width: 120rem` / `1920px` | large-screen campaign/grid spacing |
| Ultra | `min-width: 160rem` | very wide viewport spacing adjustments |

### Touch Targets

- **Minimum tap size**: button height tokens include `2rem` and `2.5rem`; icon glyphs often `1rem`, so clickable wrappers must carry the hit area.
- **Button height (mobile)**: medium/small buttons at `2rem`, large at `2.5rem`.
- **Input height (mobile)**: input height aliases resolve through typography line-height and padding; observed fields remain compact rather than 48px material-style controls.

### Collapsing Strategy

- **Navigation**: deep category tree collapses into mobile menu/list states.
- **Grid columns**: layout columns and grid spacing retune at `48rem`, `64rem`, `85.4375rem`, `120rem`.
- **Sidebar**: edge utilities compress into menu/search overlays on small screens.
- **Hero layout**: media remains dominant; controls and copy reposition rather than turning into stacked marketing cards.

### Image Behavior

- **Strategy**: image/video first. Classes like `media__wrapper--fill`, `media__wrapper--by-aspect-ratio`, `ecs-media-image__image`, and `ecs-media-image--fit-vertical` indicate responsive media fitting.
- **Max-width**: media wrappers use viewport/full-container constraints.
- **Aspect ratio handling**: CSS classes explicitly preserve/fill aspect ratios; vertical fashion imagery is a first-class case.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<button class="zds-button zds-button--primary">Continue</button>
<button class="zds-button zds-button--secondary">Cancel</button>
```

| Property | Primary | Secondary |
|---|---|---|
| Height | `2.5rem` large, `2rem` medium/small | `2rem` |
| Padding | `0.75rem` left/right | `0.75rem` left/right |
| Radius | `0rem` | `0rem` |
| Background | `#FFFFFF` on dark / `#000000` on light depending context | inverse pairing |
| Text | inverse black/white | inverse black/white |
| Hover | `#C9C9C9` or `#363636` state colors | muted inverse state |
| Loading | dedicated `--mds-color-bg-loading`, `--mds-color-content-loading` | same token family |
| Disabled | `#797979`, `#1B1B1B`, `#A1A1A1` depending state | same token family |

The square radius is non-negotiable. Buttons should look like precise labels with click area, not pill CTAs.

### Badges

```html
<span class="zds-tag">NEW</span>
<span class="zds-tag zds-tag--sale">SALE</span>
```

| Property | Value |
|---|---|
| Background | transparent or semantic state |
| Border | `#FFFFFF` on inverse contexts, transparent elsewhere |
| Label | `#FFFFFF`, `#000000`, or semantic state |
| Radius | small/none; avoid capsule styling unless observed in a specific subcomponent |
| Typography | label scale, 10-13px equivalent, weight 300/500 |

### Cards & Containers

```html
<article class="product-card">
  <div class="product-card__media">
    <img class="product-card__image" alt="" />
  </div>
  <p class="product-card__name">Product name</p>
</article>
```

| Property | Value |
|---|---|
| Background | transparent / `#FFFFFF` page |
| Border | none by default |
| Radius | `0` |
| Padding | compact, tokenized via `--spacing-*` |
| Shadow | none |
| Hover | subtle media/text state, not lift |

### Navigation

```html
<nav class="zara-nav">
  <a class="zara-nav__link">WOMAN</a>
  <a class="zara-nav__link">MAN</a>
  <a class="zara-nav__link">KIDS</a>
</nav>
```

| Property | Value |
|---|---|
| Typography | `Helvetica Now Text`, 11-13px equivalent for utility nav |
| Weight | `300` normal, `500` highlight |
| Color | `#000000` or `#FFFFFF` depending media background |
| Tracking | mostly `0`, menu universe negative at large sizes |
| Structure | deep nested lists: thousands of `a`/`li` elements in extracted HTML |

### Inputs & Forms

```html
<label class="zds-field">
  <span class="zds-field__label">Email</span>
  <input class="zds-input" />
</label>
```

| State | Border / State Color | Notes |
|---|---|---|
| Default | `#949494` / `#6B6B6B` | thin, monochrome |
| Focus | `#000000` or `#348DED` focus token | do not use colorful glow |
| Error | `#FF453A` / `#FF3E33` | semantic only |
| Disabled | `#797979`, `#A1A1A1` | low contrast but legible |
| Radius | `0` or tiny field radius | square visual rule remains |

### Hero Section

```html
<section class="zara-hero">
  <picture class="zara-hero__media">...</picture>
  <div class="zara-hero__editorial">THE ITEM</div>
  <nav class="zara-hero__utility">...</nav>
</section>
```

| Property | Value |
|---|---|
| Background | full-bleed fashion media |
| Text | campaign-specific huge type or compact utility labels |
| CTA | minimal text/control, not a centered marketing button stack |
| Overlay | media-led, optional darkening; avoid synthetic gradient mesh |
| Layout | edge-aligned controls with media occupying the page |

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-primary-inverse** — White square button on dark/black contexts.

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Color | `#000000` |
| Hover | `#C9C9C9` |
| Radius | `0rem` |
| Height | `2.5rem` large / `2rem` medium |

**button-secondary-dark** — Black square button on light contexts.

| Spec | Value |
|---|---|
| Background | `#000000` |
| Color | `#FFFFFF` |
| Hover | `#363636` |
| Radius | `0rem` |
| Padding | `0.75rem` horizontal |

**menu-universe-link** — Oversized category/universe label.

| Spec | Value |
|---|---|
| Font | `Times New Roman`, `Helvetica Now Text`, or campaign family depending route |
| Size | up to `2.5rem` |
| Weight | `400` |
| Letter spacing | down to `-0.1875rem` |
| Line height | `2.5rem` |

**product-media-tile** — Image-first commerce item.

| Spec | Value |
|---|---|
| Background | media fill |
| Radius | `0` |
| Shadow | none |
| Caption | small Helvetica Now Text |
| Interaction | subtle opacity/text state |

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

#### square-commerce-controls

```yaml
square-commerce-controls:
  description: "Zara's MDS button tokens resolve every radius — large, medium, small — to 0rem."
  technique: "--zds-radius-button: 0rem; --zds-radius-button-md: 0rem; --zds-radius-button-sm: 0rem; same hard 90° corner across all action surfaces."
  applied_to: ["{components.button-primary}", "{components.button-secondary}", "ADD", "LOGIN", "SEARCH"]
  visual_signature: "a sharp transactional layer that sits like a printed receipt under the editorial fashion surface."
  intent: "fashion sites must privilege the photograph; rounded buttons would soften the page into consumer-app warmth and steal attention."
```

#### negative-tracked-menu-universe

```yaml
negative-tracked-menu-universe:
  description: "Universe/category display type compresses through extreme negative tracking — fashion poster, not friendly app heading."
  technique: "letter-spacing down to -0.1875rem on universe headings; Helvetica Now Text at weight 700, line-height 0.95."
  applied_to: ["{typography.universe-display}", "category headline", "lookbook title"]
  visual_signature: "large words feel cropped and printed, like a 1990s magazine masthead — never a soft web heading."
  intent: "Zara's editorial DNA comes from print fashion; negative tracking is the only digital echo of a hot-metal title."
```

#### photo-first-depth-model

```yaml
photo-first-depth-model:
  description: "The system refuses chrome elevation entirely — depth comes from photography, crop, overlay, and scale."
  technique: "no box-shadow tokens on cards or campaign surfaces; depth via 21:9 / 4:5 / 1:1 ratio shifts and full-bleed image overlays."
  applied_to: ["{component.product-card}", "{component.campaign-tile}", "lookbook surface"]
  visual_signature: "every depth cue belongs to the model and the garment — never to the UI scaffold."
  intent: "fashion product pages live or die by photography; UI shadow would compete with studio lighting."
```

#### semantic-color-quarantine

```yaml
semantic-color-quarantine:
  description: "Blue, green, orange, red exist as state tokens but are quarantined to specific UX events — they never become a palette."
  technique: "#348DED focus only; #23F444 sale only; #FF9500 warning only; #FF3E33 error only; black/white/grey carries every other surface."
  applied_to: ["{component.focus-ring}", "{component.sale-tag}", "warning toast", "error inline"]
  visual_signature: "the page reads black and white until a state demands a colour event — colour becomes news, not decoration."
  intent: "luxury-leaning fashion brands must look monochrome by default; quarantining colour preserves editorial silence."
```

#### uppercase-utility-microcopy

```yaml
uppercase-utility-microcopy:
  description: "All commerce microcopy is uppercase — utility labels, links, CTAs, and metadata."
  technique: "text-transform: uppercase + Helvetica Now Text 11-13px + letter-spacing 0.06em on utility labels (LOGIN, BASKET, HELP, ADD)."
  applied_to: ["{components.button-primary}", "{component.utility-link}", "footer link", "metadata label"]
  visual_signature: "the UI speaks in printed tags — never lowercase friendly app voice."
  intent: "uppercase microcopy reads as fashion-poster typography even at 11px; lowercase would warm the page into a different brand entirely."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Campaign or collection name; sparse, uppercase-friendly, image-led | "THE ITEM" |
| Primary CTA | Functional commerce verbs, not enthusiastic marketing | "LOGIN", "SEARCH", "ADD" |
| Secondary CTA | Utility labels at small scale | "HELP", "BASKET" |
| Subheading | Product/category descriptors, short and literal | category and collection names |
| Tone | Editorial restraint + transaction clarity | no playful microcopy |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* ZARA — copy into your root stylesheet */
:root {
  /* Fonts */
  --zds-font-family-main: "Helvetica Now Text", "Helvetica", "Arial", sans-serif;
  --zds-font-family-alt: "Times New Roman";
  --zds-font-weight-light: 300;
  --zds-font-weight-regular: 400;
  --zds-font-weight-medium: 500;
  --zds-font-weight-bold: 700;

  /* Brand / neutral */
  --zds-color-brand-000: #000000;
  --zds-color-brand-040: #CCCCCC;
  --zds-color-brand-060: #E5E5E5;
  --zds-color-brand-080: #F2F2F2;
  --zds-color-brand-900: #FFFFFF;

  /* Surfaces */
  --zds-bg-page: #FFFFFF;
  --zds-bg-inverse: #000000;
  --zds-text: #000000;
  --zds-text-inverse: #FFFFFF;
  --zds-text-muted: #666666;
  --zds-border: #D8D8D8;
  --zds-border-mid: #949494;

  /* Semantic only */
  --zds-focus: #348DED;
  --zds-sale: #23F444;
  --zds-error: #FF3E33;
  --zds-warning: #FF9500;

  /* Spacing */
  --zds-space-xs: 0.25rem;
  --zds-space-sm: 0.5rem;
  --zds-space-md: 0.75rem;
  --zds-space-lg: 1.25rem;
  --zds-space-xl: 2rem;

  /* Radius */
  --zds-radius-button: 0rem;
  --zds-radius-card: 0;
}

body {
  margin: 0;
  background: var(--zds-bg-page);
  color: var(--zds-text);
  font-family: var(--zds-font-family-main);
  font-weight: var(--zds-font-weight-light);
}

.zds-button {
  min-height: 2rem;
  padding-inline: 0.75rem;
  border-radius: 0;
  border: 1px solid currentColor;
  font: inherit;
  font-size: 0.75rem;
  letter-spacing: 0;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — ZARA-inspired token mapping
module.exports = {
  theme: {
    extend: {
      colors: {
        zara: {
          black: '#000000',
          white: '#FFFFFF',
          muted: '#666666',
          hairline: '#D8D8D8',
          soft: '#F2F2F2',
          focus: '#348DED',
          sale: '#23F444',
          danger: '#FF3E33',
        },
      },
      fontFamily: {
        sans: ['Helvetica Now Text', 'Helvetica', 'Arial', 'sans-serif'],
        editorial: ['Times New Roman', 'serif'],
      },
      fontWeight: {
        light: '300',
        regular: '400',
        medium: '500',
        bold: '700',
      },
      borderRadius: {
        none: '0',
        zara: '0',
      },
      boxShadow: {
        none: 'none',
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
|---|---|---:|
| Brand primary | `{colors.brand-black}` | `#000000` |
| Background | `{colors.surface-page}` | `#FFFFFF` |
| Text primary | `{colors.text-primary}` | `#000000` |
| Text muted | `{colors.text-muted}` | `#666666` |
| Border | `{colors.hairline}` | `#D8D8D8` |
| Focus | `{colors.focus-blue}` | `#348DED` |
| Sale | `{colors.sale-green}` | `#23F444` |
| Error | `{colors.danger-red}` | `#FF3E33` |

### Example Component Prompts

#### Hero Section

```text
ZARA 스타일 히어로 섹션을 만들어줘.
- 배경: full-bleed fashion photography or video; gradient mesh 금지
- 레이아웃: media가 viewport 대부분을 차지하고, utility navigation은 edge에 작게 배치
- 타이포: Helvetica Now Text 또는 campaign serif, utility text 0.75rem/300
- 색상: #000000 / #FFFFFF 중심, semantic color 사용 금지
- CTA: square text control, radius 0, no pill button
- 전체 인상: editorial storefront window, not SaaS landing hero
```

#### Card Component

```text
ZARA 스타일 product media tile을 만들어줘.
- 배경: transparent 또는 #FFFFFF
- media: image-first, cover/fill, radius 0
- border/shadow: none; 필요하면 #D8D8D8 hairline만
- caption: Helvetica Now Text, 0.75rem, weight 300, color #000000
- hover: opacity/text color subtle shift only, transform lift 금지
```

#### Badge

```text
ZARA 스타일 상태 라벨을 만들어줘.
- font: Helvetica Now Text, 0.625rem~0.75rem, weight 300 or 500
- radius: 0 또는 최소값
- default: transparent bg, #000000 text
- sale/error/focus에서만 #23F444 / #FF3E33 / #348DED 사용
- decorative colorful badge 금지
```

#### Navigation

```text
ZARA 스타일 navigation을 만들어줘.
- 링크: Helvetica Now Text, 0.75rem 전후, weight 300
- 배치: page edge에 얇게 붙는 utility nav
- 색상: media 위에서는 #FFFFFF 또는 #000000 중 contrast가 맞는 하나
- active/highlight: weight 500 또는 underline/text state, background chip 금지
- category universe: 큰 경우 negative tracking을 적용
```

### Iteration Guide

- **색상 변경 시**: 새 brand color를 만들지 말고 `#000000`, `#FFFFFF`, neutral ramp 안에서 해결한다.
- **폰트 변경 시**: body/navigation은 weight `300`을 먼저 유지한다.
- **여백 조정 시**: hero는 크게, commerce controls는 compact하게 유지한다.
- **새 컴포넌트 추가 시**: radius `0`, shadow `none`, hairline `#D8D8D8` 우선.
- **상태 색상**: `#348DED`, `#23F444`, `#FF3E33`, `#FF9500`은 semantic state 전용이다.
- **반응형**: `48rem`, `64rem`, `85.4375rem`, `120rem` breakpoints를 먼저 따른다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#000000` and `#FFFFFF` as the brand system, not just defaults.
- Keep body/navigation text small and light: 10-13px equivalents, weight `300`.
- Let photography/video carry emotion, depth, and color.
- Use square controls: button radius `0rem`, card radius `0`.
- Use `#D8D8D8`, `#949494`, and `#666666` for structure and secondary hierarchy.
- Reserve `#348DED`, `#23F444`, `#FF3E33`, and `#FF9500` for semantic states only.
- Use negative tracking on oversized menu/campaign typography when recreating the category universe.
- Prefer opacity/text-decoration/color transitions over transform-heavy motion.

### ❌ DON'T

- 배경을 `#F7F7F5` 또는 cream 계열로 두지 말 것 — 대신 `#FFFFFF` 사용.
- 텍스트를 `#111827` 또는 Tailwind slate로 두지 말 것 — 대신 `#000000` 사용.
- muted text를 `#6B7280`로 두지 말 것 — 대신 `#666666` 또는 `#949494` 사용.
- border를 `#E5E7EB`로 두지 말 것 — 대신 `#D8D8D8` 사용.
- primary CTA를 `#2563EB`, `#533AFD`, `#FF385C` 같은 chromatic brand color로 두지 말 것 — 대신 `#000000` / `#FFFFFF` inverse pairing 사용.
- sale/status를 임의 green `#22C55E`로 두지 말 것 — 실제 sale token `#23F444` 사용.
- error를 generic red `#EF4444`로 두지 말 것 — 실제 danger token `#FF3E33` 또는 semantic `#FF453A` 사용.
- focus를 generic blue `#3B82F6`로 두지 말 것 — 실제 focus token `#348DED` 사용.
- body 기본을 `font-weight: 400`으로 평준화하지 말 것 — Zara chrome은 weight `300`이 핵심이다.
- 버튼을 `border-radius: 999px` pill로 만들지 말 것 — `0rem` square control을 사용.
- product card에 `box-shadow`를 넣지 말 것 — photography와 whitespace로 분리한다.
- hero를 centered headline + two CTA 구조로 만들지 말 것 — media-dominant editorial layout을 유지한다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- Second brand color: none. Chromatic colors are state colors, not brand identity.
- Gradient brand surfaces: absent. The captured system is image/video-led, not gradient-led.
- Pill CTA language: absent from primary brand chrome; button radii resolve to `0rem`.
- Card elevation: none in the main commerce/product surface.
- Friendly SaaS section rhythm: absent. No "hero + feature cards + CTA band" cadence.
- Heavy body typography: mostly absent; weight `300` is a defining baseline.
- Decorative icon palette: absent. Icons and utility marks stay monochrome.
- Rounded product tiles: absent; image geometry remains square/rectangular.
- Colorful navigation states: absent; active states should use weight, underline, or monochrome contrast.
- Copy exuberance: absent. The voice is editorial/functional, not playful.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Phase1 reuse date** — the reused artifacts were present locally from an earlier capture. This guidebook is generated on 2026-05-03, but the underlying CSS/HTML artifacts may not reflect every live Zara change made after capture.
- **Cookie overlay in screenshot** — `hero-cropped.png` includes a cookie consent bar, which occludes the bottom of the hero. Top-level campaign/media reading is still usable, but lower hero controls may be under-observed.
- **Single route bias** — the analysis uses homepage HTML/CSS and extracted shared tokens. Checkout, account, search result filters, product detail pages, and payment flows were not separately visited.
- **Exact sticky behavior unmeasured** — navigation appears edge/persistent in the screenshot and HTML structure, but scroll-state transitions were not replayed in browser for this output.
- **Token aliases can be route-specific** — Zara ships many collection and campaign font families. This document treats `Helvetica Now Text` as the stable UI base and special families as campaign accents.
- **No full visual diff** — Step 6 report rendering was intentionally skipped per request. This file validates structure/content, not an HTML report preview.
- **Semantic colors are real but not brand** — blue/green/red/orange tokens exist in CSS; their interpretation as non-brand state colors is a design judgment based on token names and usage roles.
- **Motion JS not inspected** — CSS transition values and reduced-motion media queries were observed, but carousel runtime timing and JS-driven animation curves were not deeply traced.
- **Mobile screenshots not captured in this pass** — responsive behavior comes from CSS media queries and existing HTML classes, not a fresh mobile visual inspection.
