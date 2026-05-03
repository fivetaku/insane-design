---
schema_version: 3.2
slug: hyundai
service_name: Hyundai KR
site_url: https://www.hyundai.com/kr/ko/
fetched_at: 2026-05-03 Asia/Seoul; phase1 artifacts reused from insane-design/hyundai
default_theme: light
brand_color: "#002C5F"
primary_font: HyundaiSansTextKR
font_weight_normal: 400
token_prefix: hyundai

bold_direction: Automotive Clarity
aesthetic_category: editorial-product
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: automotive
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "No CSS custom-property token tier was exposed, but HyundaiSans, repeated button/nav/carousel primitives, and consistent blue/neutral usage show a system in use."

colors:
  brand-primary: "#002C5F"
  brand-secondary: "#007FA8"
  interaction-blue: "#409EFF"
  surface-base: "#FFFFFF"
  surface-warm: "#F6F3F2"
  text-primary: "#000000"
  text-secondary: "#666666"
  hairline: "#E5E5E5"
typography:
  display: HyundaiSansHeadKR
  body: HyundaiSansTextKR
  ladder:
    - { token: title-k1, size: "58px", weight: 400, line_height: "70px", tracking: "-0.4px" }
    - { token: title-h1, size: "44px", weight: 400, line_height: "56px", tracking: "-0.4px" }
    - { token: section-title, size: "30px", weight: 400, line_height: "37px", tracking: "-0.4px" }
    - { token: utility-text, size: "14px", weight: 400, line_height: "24px", tracking: "-0.4px" }
  weights_used: [300, 400, 500, 600, 700, 800, 900]
  weights_absent: []
components:
  button-more-blue: { color: "{colors.brand-primary}", width: "auto", role: "text CTA" }
  button-md: { width: "120px to 240px", role: "fixed-width CTA" }
  header-fixed: { bg: "rgba(255,255,255,.9)", border: "1px solid #E5E5E5", blur: "5px" }
  carousel-arrow: { size: "40px x 70px", bg: "transparent", stroke: "#000000" }
---

# DESIGN.md - Hyundai KR (Designer Guidebook)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Hyundai KR is built like a public showroom more than a startup landing page. The page gives the vehicle image first claim on attention, then places navigation, purchase utilities, EV programs, service links, shop content, brand stories, events, and corporate information in a controlled sequence. Its visual language is not decorative futurism; it is institutional automotive clarity.

The homepage behaves like a dealership atrium where the glass walls have been removed: the car is already on the floor, the staff desk is one step below it, and every sign points to a practical next action. Vehicle photography is the stage, but the stagehands are visible as precise service links, purchase flows, search, login, and corporate navigation.

The signature color is Hyundai deep blue, #002C5F (`{colors.brand-primary}`). It behaves less like a loud accent and more like a dealership seal stamped on official paperwork: link CTAs, nav underline bars, utility buttons, and brand affordances return to this same blue. A brighter system blue, #409EFF (`{colors.interaction-blue}`), appears heavily because Element UI primitives are present, but it reads as framework interaction color, not Hyundai's core brand. There is no second brand color trying to compete with the badge.

Typography carries much of the identity. HyundaiSansHeadKR gives headings a proprietary industrial tone without becoming aggressive; HyundaiSansTextKR handles navigation, body, and utility controls. The system repeatedly uses small negative tracking (`-0.4px`) and a broad weight range, so the page feels engineered rather than generic Korean corporate web.

The layout is a sequence of large image-led bands and operational modules. The hero is a carousel with full-width vehicle photography and thin, line-drawn arrows; the arrows feel closer to a dashboard needle than to a web button. Under it, dense action links compress commerce and service workflows. This is the key rhythm: cinematic car surface above, high-utility customer portal below.

The fixed header is not a glassmorphism spectacle. It is frosted dealership glass: `rgba(255,255,255,.9)`, `blur(5px)`, and a #E5E5E5 (`{colors.hairline}`) rule, with shadow deliberately absent. Depth belongs to the photography and modal overlays, not to the chrome.

The screenshot capture includes a launch-event modal overlay. Treat it as a temporary campaign layer, not the permanent homepage chassis. The modal itself is useful evidence: Hyundai is comfortable dropping a square, high-contrast announcement panel over the showroom when a campaign needs priority, like a placard wheeled in front of a display car. The underlying system remains blue/black/white, restrained, and rectangular.

### Key Characteristics

- Vehicle photography owns the first viewport; chrome and UI controls stay thin.
- Hyundai deep blue #002C5F is the real brand anchor, even when brighter framework blue appears more often in CSS.
- Proprietary HyundaiSans font families are central to recognition.
- Navigation is horizontal, dense, and utility-heavy; this is a customer portal, not only a brand ad.
- Carousel controls use transparent backgrounds and line geometry instead of filled icon buttons.
- Warm off-white surfaces such as #F6F3F2 and #E4DCD3 soften the otherwise black/white system.
- Border and divider language is thin: #E5E5E5 hairlines, not heavy panels.
- CTAs are often text-link or fixed-width rectangular controls rather than oversized rounded pills.
- Element UI residues are visible in pagination, carousel, modal, and form primitives.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Automotive Clarity
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **hero_impact**으로 기억된다.
> **Code Complexity**: high — Nuxt/Element UI, modal/carousel states, responsive breakpoints, fixed header blur, and image-led modules require more than static token copying.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Hyundai KR처럼 만들기 - 3가지만 하면 80%

```css
/* 1. proprietary automotive typography */
body {
  font-family: "HyundaiSansTextKR", "Pretendard", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
  letter-spacing: -0.4px;
}
h1, h2, h3, .display {
  font-family: "HyundaiSansHeadKR", "Pretendard", sans-serif;
  font-weight: 400;
}

/* 2. blue + neutral showroom floor */
:root {
  --hyundai-blue: #002C5F;
  --hyundai-aqua: #007FA8;
  --hyundai-bg: #FFFFFF;
  --hyundai-warm: #F6F3F2;
  --hyundai-text: #000000;
  --hyundai-muted: #666666;
  --hyundai-line: #E5E5E5;
}

/* 3. thin operational chrome */
.header {
  background: rgba(255,255,255,.9);
  border-bottom: 1px solid var(--hyundai-line);
  backdrop-filter: blur(5px);
}
.text-cta { color: var(--hyundai-blue); font-weight: 500; }
```

**절대 하지 말아야 할 것 하나**: Hyundai를 밝은 #409EFF framework blue로 브랜딩하지 말 것. 이 색은 Element UI interaction residue이고, 핵심 브랜드 앵커는 #002C5F다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.hyundai.com/kr/ko/` |
| Local source | `insane-design/hyundai/index.html` |
| Phase1 source | `insane-design/hyundai/phase1/*.json`, `insane-design/hyundai/css/_inline.css`, `insane-design/hyundai/screenshots/hero-cropped.png` |
| Fetched / reused | Existing phase1 artifacts, file dates around 2026-04-14 and screenshot from 2026-04-23 |
| Extractor | Reused local phase1; no new URL fetch because phase1 was present |
| HTML size | 702333 bytes |
| CSS files | 1 inline CSS bundle, 629849 bytes |
| Token prefix | `hyundai` (guidebook alias; no native CSS custom-property prefix exposed) |
| Method | CSS hex/font/rule extraction + HTML structure parsing + screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Nuxt/Vue SSR evidence from `_nuxt` asset paths and scoped Vue attributes like `data-v-5dad0028`.
- **Component substrate**: Element UI primitives are visible in classes such as `.el-carousel`, `.el-pagination`, `.el-dialog__wrapper`, and `.el-col-*`.
- **Design system**: Hyundai web system in use, not a public token API. The CSS exposes no custom properties in the reused bundle (`resolved_tokens.total_vars = 0`).
- **CSS architecture**: compiled scoped CSS bundle with repeated component blocks, global utility button classes, and Element UI defaults.
  ```text
  Native custom properties: none exposed in phase1 CSS
  Framework layer: .el-* carousel / pagination / dialog / grid classes
  Hyundai layer: .header, .btn-more-blue, .title-k1, .keyvisual-wrap, .visual-wrap
  Component scope: Vue data-v-* selectors for page modules
  ```
- **Class naming**: hybrid utility/component naming (`btn-md`, `btn-more-blue`, `keyvisual-wrap`) plus Element UI BEM-like classes.
- **Default theme**: light, with white #FFFFFF base, black #000000 text, and warm campaign surfaces.
- **Font loading**: CSS `@font-face` and local HyundaiSans families; exact font files were not enumerated beyond visible CSS declarations.
- **Canonical anchor**: the fixed/global header and hero carousel define the page chassis.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `HyundaiSansHeadKR` / `HyundaiSansHeadKRR` (brand proprietary)
- **Body font**: `HyundaiSansTextKR` / `HyundaiSansTextKRR` (brand proprietary)
- **Icon font**: `element-icons`
- **Weight normal / bold**: `400` / `700`, with 500 also used for UI emphasis

```css
:root {
  --hyundai-font-display: "HyundaiSansHeadKR", "Pretendard", sans-serif;
  --hyundai-font-body: "HyundaiSansTextKR", "Pretendard", -apple-system, sans-serif;
  --hyundai-font-icon: "element-icons";
  --hyundai-font-weight-normal: 400;
  --hyundai-font-weight-medium: 500;
  --hyundai-font-weight-bold: 700;
}
body {
  font-family: var(--hyundai-font-body);
  font-weight: var(--hyundai-font-weight-normal);
  letter-spacing: -0.4px;
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **HyundaiSansHeadKR** is proprietary. Use **Pretendard** or **Noto Sans KR** only as a substitute, not as the design identity.
- Open-source substitute: **Pretendard** at weight 400 for display headings, with `letter-spacing: -0.4px`.
- Compensation: keep heading weight lighter than typical marketing pages. Do not jump directly to 700 for primary hero titles unless the page campaign asset itself does it.
- Body fallback should preserve Korean readability: `Pretendard`, `Noto Sans KR`, then `-apple-system`.
- Keep the body line-height practical and portal-like; do not add editorial looseness that makes dense service modules feel underbuilt.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `title-k1` | 58px | 400 | 70px | -0.4px |
| `title-h1` | 44px | 400 | 56px | -0.4px |
| `section-title` / `.title` | 30px | 400 | 37px | -0.4px |
| `title-k2` | 16px | 400 | 28px | -0.4px |
| `utility-text` | 14px | 400 | 24px | -0.4px |
| `tag-main` | 12-14px | 400 | 24-30px | -0.4px |
| `carousel-arrow-icon` | 12px | 700 | 1 | 0 |

> Key insight: the page does not rely on oversized SaaS-style type contrast. It uses proprietary HyundaiSans, tight tracking, and calm weights to make utility-heavy modules feel official.

### Principles
<!-- SOURCE: manual -->

1. Headings are often lighter than expected. `HyundaiSansHeadKR` at 400 is a brand voice, not an unfinished weight.
2. `letter-spacing: -0.4px` is a recurring optical correction across titles and small UI text; keep it in Korean layouts.
3. Weight 500 is allowed for controls, but not as the universal heading solution.
4. Body and navigation should remain utilitarian. The site reads like a purchase/service portal under a brand showroom.
5. Icon typography is separate. Element icons should not inherit HyundaiSans metrics.
6. Campaign panels may break the calm system with heavy text, but the base chassis should not.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed anchors)

| Token | Hex | Evidence / use |
|---|---|---|
| `hyundai.brand-primary` | `#002C5F` | Hyundai deep blue; `.btn-more-blue`, nav underline bar, official CTA/link color |
| `hyundai.brand-secondary` | `#007FA8` | frequent chromatic blue-green accent in CSS |
| `hyundai.interaction-blue` | `#409EFF` | Element UI hover/pagination interaction color; not the main brand anchor |
| `hyundai.interaction-blue-hover` | `#3A8EE6` | Element UI hover variant |
| `hyundai.aqua-light` | `#66B1FF` | Element UI derived blue |

### 06-2. Brand Dark Variant

> N/A - no complete dark-theme brand ramp was exposed in the reused phase1 CSS.

### 06-3. Neutral Ramp

| Step | Light | Dark / text |
|---|---|---|
| Surface base | `#FFFFFF` | `#000000` |
| Warm surface | `#F6F3F2` | `#1C1B1B` |
| Warm image/campaign field | `#E4DCD3` | `#333333` |
| Hairline | `#E5E5E5` | `#666666` |
| Framework line | `#EBEEF5` | `#303133` |
| Disabled / muted | `#C0C4CC` | `#909399` |
| Soft background | `#F5F7FA` | `#606266` |

### 06-4. Accent Families

| Family | Key step | Hex | Notes |
|---|---|---|---|
| Success | Element UI success | `#67C23A` | Framework state color |
| Warning | Element UI warning | `#E6A23C` | Framework state color |
| Error | Element UI error | `#F56C6C` | Framework state color |
| Warm campaign | beige / clay | `#E4DCD3` | Automotive lifestyle surface |
| Modal campaign red | captured image only | not tokenized | Appears in screenshot as event artwork, not CSS token evidence |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `hyundai.bg.page` | `#FFFFFF` | global page and header surface |
| `hyundai.bg.warm` | `#F6F3F2` | dialog/popup and soft campaign container |
| `hyundai.text.primary` | `#000000` | primary text, arrows, logo-adjacent UI |
| `hyundai.text.secondary` | `#666666` | muted descriptive and utility text |
| `hyundai.border.default` | `#E5E5E5` | fixed header divider and layer borders |
| `hyundai.cta.text-blue` | `#002C5F` | text CTA, "more" link, official navigation emphasis |
| `hyundai.framework.hover` | `#409EFF` | Element UI hover state |

### 06-6. Semantic Alias Layer

> N/A - `alias_layer.json` contains empty tiers. The aliases in this guidebook are interpretation labels, not native CSS variable names.

### 06-7. Dominant Colors (actual CSS frequency order)

| Token | Hex | Frequency evidence |
|---|---:|---:|
| White | `#FFFFFF` / `#FFF` | 816 / 408 shorthand occurrences |
| Black | `#000000` / `#000` | 522 / 261 shorthand occurrences |
| Element interaction blue | `#409EFF` | 250 / 125 shorthand occurrences |
| Hyundai secondary blue | `#007FA8` | 238 / 119 shorthand occurrences |
| Disabled gray-blue | `#C0C4CC` | 194 / 97 shorthand occurrences |
| Neutral gray | `#666666` / `#666` | 184 / 92 shorthand occurrences |
| Hyundai deep blue | `#002C5F` | 174 / 87 shorthand occurrences |
| Soft warm | `#F6F3F2` | 99 / 49 shorthand occurrences |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.brand-primary}` (`#002C5F`)** - Hyundai's real interface anchor. Use it for official CTAs, text links, nav indicators, and brand emphasis. It should feel institutional and permanent, not playful.

**`{colors.surface-base}` (`#FFFFFF`)** - The showroom floor. Hyundai keeps the page clean so vehicle imagery, product names, and service modules can carry the information weight.

**`{colors.text-primary}` (`#000000`)** - Black is used directly and confidently. Do not soften all text into charcoal; the brand tolerates strong black against white.

**`{colors.hairline}` (`#E5E5E5`)** - The structural line color. Header fixation, dividers, and layer boundaries use thin gray instead of cards with heavy shadows.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `header-desktop-height` | 80px | hidden fixed header translates by `-80px` |
| `header-tablet-height` | 64px | tablet hidden header translates by `-64px` |
| `hero-image` | 1800px x 720px | `.img-wrap img.visual` |
| `container-breadcrumb` | `calc(100% - 120px)`, max 1120px | visual breadcrumb width |
| `carousel-arrow-offset` | 60px | left/right hero arrow placement |
| `carousel-arrow-size` | 40px x 70px | `.keyvisual-wrap .el-carousel__arrow` |
| `text-tag-offset` | 20-30px | news/card tag top-left placement |
| `button-md-width` | 120px / 240px | fixed CTA widths |

**Main alias**:
- `hyundai.space.header` -> 80px desktop / 64px tablet
- `hyundai.space.hero-height` -> 720px image asset height
- `hyundai.space.edge` -> 60px hero controls and large page gutters

### Whitespace Philosophy
<!-- SOURCE: manual -->

Hyundai uses whitespace as showroom clearance, not as airy editorial luxury. The hero image is allowed to span wide, while navigation and arrows sit with enough edge distance to feel engineered. The page needs room for vehicle silhouette and product name, then quickly returns to dense utility modules.

Below the hero, whitespace compresses. Purchase, service, EV, shop, event, and news areas need to scan like a portal. The correct rhythm is "wide vehicle stage, efficient customer action grid," not a uniform 12-column marketing page with equal breathing room everywhere.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `framework-carousel-arrow` | 50% | default Element UI circular arrow primitive |
| `hyundai-hero-arrow` | 0 | custom transparent hero arrows rely on line geometry, not filled circles |
| `dialog-panel` | 0-2px visual | captured modal is rectangular with hard official edges |
| `badge/tag` | 0 | news main tag is rectangular |
| `button-md` | mostly rectangular | fixed-width CTA style; do not default to pill |

> Radius identity: Hyundai is much more rectangular than modern SaaS. Rounded controls should appear only where inherited framework primitives require them.

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `header-depth` | none; uses border + blur | Fixed header relies on `#E5E5E5` line and `backdrop-filter: blur(5px)` |
| `card-depth` | minimal / image-led | Cards generally use photography, spacing, and tags rather than heavy elevation |
| `modal-depth` | overlay + rectangular panel | Screenshot shows a campaign modal over dimmed page; depth comes from overlay contrast |

> Shadow pattern: structural depth is mostly absent from chrome. If depth is needed, use overlay/dimming for modal priority or photography contrast, not generic card shadows.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `header-transform` | `transform .3s` | fixed header hide/reveal |
| `gnb-bar` | `left .4s ease, width .4s ease, opacity .4s ease` | nav underline movement |
| `carousel-arrow` | `.3s` | Element UI arrow transition |
| `carousel` | JS-driven | hero and module slides |

> Motion is operational. It clarifies state changes rather than becoming brand spectacle.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: 1120px appears in visual breadcrumb; hero brand mode can reach max 2560px.
- **Grid type**: Flexbox and Element UI grid (`.el-col-*`) rather than a named CSS Grid token system.
- **Column count**: Element UI breakpoint classes imply 24-column grid capability; page modules vary by section.
- **Gutter**: not exposed as a single token; use 60px edge spacing for hero controls and 20-30px internal module tag offsets.

### Hero

- **Pattern Summary**: `720px image-led carousel + transparent arrow controls + header overlay + purchase/service portal below`
- Layout: full-width vehicle photography carousel with text and controls layered over or beside the image.
- Background: image-led; screenshot shows IONIQ 6/9 vehicle hero behind a temporary modal.
- **Background Treatment**: product photography with dim overlay when modal is active; otherwise clean showroom image treatment.
- H1: inferred campaign/product display around `title-k1` scale, 58px / weight 400 / tracking `-0.4px`, with campaign assets allowed to use heavier custom text.
- Max-width: hero image asset 1800px x 720px; brand carousel can allow 2560px.

### Section Rhythm

```css
section-like modules {
  background: #FFFFFF or #F6F3F2;
  border/hairline: #E5E5E5 when structure is needed;
  content rhythm: wide hero first, dense customer modules after;
}
```

### Card Patterns

- **Card background**: mostly `#FFFFFF`; warm surfaces `#F6F3F2` appear for campaign/popup context.
- **Card border**: thin #E5E5E5 or none; photography often replaces border as the visual boundary.
- **Card radius**: rectangular; avoid pill/card over-rounding.
- **Card padding**: section-specific; tags show 20-30px inset in news/card contexts.
- **Card shadow**: minimal; use image contrast and hairlines.

### Navigation Structure

- **Type**: dense horizontal global navigation with logo, primary categories, Trendy Hyundai link, language, login, search, menu.
- **Position**: relative by default; fixed variant exists at top with blur and border.
- **Height**: 80px desktop, 64px tablet evidence from hide transform.
- **Background**: `#FFFFFF`; fixed state `rgba(255,255,255,.9)` plus blur.
- **Border**: `1px solid #E5E5E5` fixed header bottom border.
- **Active indicator**: 4px `#002C5F` bottom bar with `.4s ease` movement.

### Content Width

- **Prose max-width**: not a prose-first site; use module-specific widths.
- **Container max-width**: 1120px for breadcrumb-like content, 1800px/2560px for hero imagery.
- **Sidebar width**: not a homepage pattern; mobile/menus use overlays instead.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | max-width 767px | dominant mobile breakpoint; many module overrides |
| Tablet | min-width 768px / max-width 1024px | header height reduces to 64px; tablet-specific layout |
| Desktop | min-width 1025px | full global nav behavior and wider hero controls |
| Large | min-width 1200px / 1920px | Element grid and large display refinements |

### Touch Targets

- **Minimum tap size**: infer 44px+ for major header/search/menu icons, but exact mobile tap token was not isolated.
- **Button height (mobile)**: not globally tokenized in phase1.
- **Input height (mobile)**: Element UI defaults likely apply, but not treated as Hyundai-specific without sub-flow observation.

### Collapsing Strategy

- **Navigation**: dense desktop nav collapses toward menu/search-heavy mobile behavior.
- **Grid columns**: Element UI `.el-col-xs/sm/md/lg/xl` classes handle breakpoint distribution.
- **Sidebar**: no persistent sidebar on homepage.
- **Hero layout**: hero remains image-led; controls and text adapt around viewport.

### Image Behavior

- **Strategy**: large prepared vehicle imagery, often fixed aspect assets.
- **Max-width**: hero brand carousel can max at 2560px; visual asset evidence 1800px x 720px.
- **Aspect ratio handling**: vehicle/product images are treated as hero assets, not arbitrary responsive thumbnails.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Text CTA / More Blue**

```html
<a class="btn btn-more-blue">자세히 보기</a>
```

| State | Spec |
|---|---|
| Default | color `#002C5F`; Hyundai deep blue link button |
| Size | often content-width; some contexts `height:auto;width:auto` |
| Hover | keep blue identity; do not introduce gradient/fill unless source context has it |
| Role | official secondary CTA, "more" link, service deep link |

**Fixed CTA / Medium**

```html
<a class="btn btn-md">자세히 보기</a>
```

| State | Spec |
|---|---|
| Width | 120px in compact contexts; 240px in broader CTA contexts |
| Max width | `max-width:100%` |
| Shape | rectangular, restrained; not pill-first |

### Badges

**News / Main Tag**

```html
<span class="tag main">MAIN</span>
```

| State | Spec |
|---|---|
| Position | absolute top-left, 20-30px on larger cards; 5px in compressed context |
| Size | 12-14px, line-height 24-30px |
| Color | white text on `rgba(0,0,0,.5)` |
| Hover/focus | border `2px solid #FFFFFF`, transparent background in focused news card context |

### Cards & Containers

**Image-led module card**

```html
<article class="box-news">
  <span class="tag main">News</span>
  <img alt="">
</article>
```

| Property | Value |
|---|---|
| Background | photography or `#FFFFFF` |
| Border | minimal; focus states may use white border on tags |
| Radius | rectangular |
| Shadow | absent or minimal |
| Hover | state emphasis through tag border/background, not heavy transform |

### Navigation

**Global Header**

```html
<header class="header isFixed">
  <button class="logo-link">HYUNDAI</button>
  <nav class="gnb_wrap">...</nav>
</header>
```

| State | Spec |
|---|---|
| Default | relative, width 100%, `#FFFFFF` |
| Transparent | absolute top, transparent background, no bottom border |
| Fixed | fixed top, `rgba(255,255,255,.9)`, `backdrop-filter: blur(5px)`, border `#E5E5E5` |
| Hidden | desktop `translateY(-80px)`, tablet `translateY(-64px)` |
| Active bar | 4px `#002C5F`, animated left/width/opacity `.4s ease` |

### Inputs & Forms

**Search Layer**

```html
<button class="btn_search">검색하기</button>
```

| State | Spec |
|---|---|
| Entry | search icon in header opens layer |
| Utility | auto-complete toggle, history delete, keyword delete controls |
| Color | black/neutral controls; official action may use Hyundai blue |
| Framework | Element UI form defaults may appear in deeper flows |

### Hero Section

**Key Visual Carousel**

```html
<div class="keyvisual-wrap">
  <div class="kv-main el-carousel">...</div>
</div>
```

| Property | Value |
|---|---|
| Image | vehicle hero image, observed 1800px x 720px |
| Arrow | 40px x 70px transparent control |
| Arrow line | 34px x 34px pseudo-element, border `1px solid #000000`; white variant exists |
| Arrow offset | 60px from left/right |
| Dots | centered carousel indicators |
| Control | play/pause button for rotating hero |

### 13-2. Named Variants

**button-more-blue** - text CTA in Hyundai deep blue.

```css
.btn[class*=btn-more].btn-more-blue,
a.btn[class*=btn-more].btn-more-blue {
  color: #002C5F;
}
```

**button-md-fixed** - rectangular fixed-width CTA.

```css
.btn.btn-md,
a.btn.btn-md {
  width: 120px; /* compact */
  max-width: 100%;
}
```

**header-fixed-blur** - official sticky header state.

```css
.header.isFixed {
  position: fixed;
  top: 0;
  background: hsla(0,0%,100%,.9);
  border-bottom: 1px solid #E5E5E5;
  backdrop-filter: blur(5px);
}
```

**hero-line-arrow** - custom carousel arrow that rejects filled-circle SaaS controls.

```css
.keyvisual-wrap .kv-main.el-carousel .el-carousel__arrow {
  width: 40px;
  height: 70px;
  background: transparent;
}
```

### 13-3. Signature Micro-Specs

```yaml
fixed-header-blur-hairline:
  description: "Sticky navigation creates depth with dealership-glass transparency, blur, and a single structural line instead of shadow."
  technique: "background: hsla(0,0%,100%,.9); backdrop-filter: blur(5px); border-bottom: 1px solid #E5E5E5; box-shadow: none"
  applied_to: ["{component.header-fixed}", ".header.isFixed"]
  visual_signature: "A white official header floats like frosted showroom glass while the page remains flat and operational."

gnb-blue-measuring-bar:
  description: "Desktop navigation marks state with a moving Hyundai-blue measuring bar, not with filled tabs or color blocks."
  technique: "height: 4px; background-color: #002C5F; transition: left .4s ease, width .4s ease, opacity .4s ease"
  applied_to: [".header .inner_wrap .gnb_wrap .bar", "{colors.brand-primary}"]
  visual_signature: "A precise instrument-line underline slides under the active nav item."

transparent-hero-line-arrow:
  description: "Hero carousel controls are mechanical line geometry placed over photography, rejecting filled-circle SaaS arrows."
  technique: "width: 40px; height: 70px; background: transparent; pseudo-element arrow approx 34px x 34px with 1px #000000 border"
  applied_to: ["{component.carousel-arrow}", ".keyvisual-wrap .kv-main.el-carousel .el-carousel__arrow"]
  visual_signature: "The vehicle image remains the object; the UI reads as a thin dashboard control."

hyundai-tight-korean-tracking:
  description: "HyundaiSans headings and utility labels are optically tightened across Korean interface text."
  technique: "font-family: HyundaiSansHeadKR / HyundaiSansTextKR; letter-spacing: -0.4px; weight range 400-500 for most UI copy"
  applied_to: [".title-k1", ".title-h1", ".title-s1", ".tag.main", "nav-style utility text"]
  visual_signature: "Korean text feels compact, official, and engineered rather than loose generic web typography."

deep-blue-text-cta-with-arrow:
  description: "Secondary actions reject filled buttons and become a small typographic command in Hyundai deep blue with a thin trailing arrow."
  technique: "color #002C5F ({colors.brand-primary}); background transparent; no border or fill; HyundaiSans weight 400-500; trailing → / 1px line arrow at text height; underline appears only on hover/focus, not default"
  applied_to: ["{component.button-more-blue}", "module 'More' / 'View all' links", "section-end navigation"]
  visual_signature: "Sectional reads end with a quiet blue line of type, like an engineer's marginal note pointing forward, instead of yet another rectangular SaaS button."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Product headline | Short vehicle/model naming, often English alphanumeric | "IONIQ 9" |
| Campaign subline | Imperative or slogan-like English/Korean mix | "Rule the Paradigm" |
| Utility CTA | Direct action noun phrase | "견적내기", "구매상담", "시승신청" |
| Service labels | Clear task language, not playful copy | "정비예약", "내비 업데이트" |
| Corporate links | Institutional taxonomy | "기업정보", "IR 정보", "지속가능 경영" |
| Tone | official, practical, showroom-led | consumer confidence over witty brand voice |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Hyundai KR - copy into your root stylesheet */
:root {
  /* Fonts */
  --hyundai-font-display: "HyundaiSansHeadKR", "Pretendard", sans-serif;
  --hyundai-font-body: "HyundaiSansTextKR", "Pretendard", -apple-system, sans-serif;
  --hyundai-font-weight-normal: 400;
  --hyundai-font-weight-medium: 500;
  --hyundai-font-weight-bold: 700;

  /* Brand */
  --hyundai-color-brand-25: #ECF5FF;
  --hyundai-color-brand-300: #007FA8;
  --hyundai-color-brand-500: #002C5F;
  --hyundai-color-brand-600: #002C5F; /* canonical */
  --hyundai-color-brand-900: #1C1B1B;

  /* Surfaces */
  --hyundai-bg-page: #FFFFFF;
  --hyundai-bg-warm: #F6F3F2;
  --hyundai-bg-warm-deep: #E4DCD3;
  --hyundai-text: #000000;
  --hyundai-text-muted: #666666;
  --hyundai-line: #E5E5E5;

  /* Key spacing */
  --hyundai-header-desktop: 80px;
  --hyundai-header-tablet: 64px;
  --hyundai-hero-arrow-offset: 60px;
  --hyundai-card-tag-inset: 30px;

  /* Radius */
  --hyundai-radius-none: 0;
  --hyundai-radius-framework-round: 50%;
}

body {
  background: var(--hyundai-bg-page);
  color: var(--hyundai-text);
  font-family: var(--hyundai-font-body);
  font-weight: var(--hyundai-font-weight-normal);
  letter-spacing: -0.4px;
}

.hyundai-header-fixed {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background: rgba(255, 255, 255, .9);
  border-bottom: 1px solid var(--hyundai-line);
  backdrop-filter: blur(5px);
}

.hyundai-text-cta {
  color: var(--hyundai-color-brand-600);
  font-weight: var(--hyundai-font-weight-medium);
}

.hyundai-hero-arrow {
  width: 40px;
  height: 70px;
  background: transparent;
  color: #000000;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `hyundai.brand-primary` | `#002C5F` |
| Secondary blue | `hyundai.brand-secondary` | `#007FA8` |
| Framework interaction | `hyundai.interaction-blue` | `#409EFF` |
| Background | `hyundai.bg.page` | `#FFFFFF` |
| Warm background | `hyundai.bg.warm` | `#F6F3F2` |
| Text primary | `hyundai.text.primary` | `#000000` |
| Text muted | `hyundai.text.secondary` | `#666666` |
| Border | `hyundai.border.default` | `#E5E5E5` |
| Success | `element.success` | `#67C23A` |
| Error | `element.error` | `#F56C6C` |

### Example Component Prompts

#### Hero Section
```text
Hyundai KR 스타일의 자동차 히어로를 만들어줘.
- 배경: 1800x720 비율의 차량 사진이 먼저 보이는 full-width carousel
- 상단: 80px white header, fixed 상태는 rgba(255,255,255,.9) + blur(5px) + #E5E5E5 hairline
- H1: HyundaiSansHeadKR, 58px, weight 400, letter-spacing -0.4px
- CTA: 텍스트 링크는 #002C5F, 과한 pill button 금지
- 캐러셀 화살표: 투명한 40x70 hit area, 1px black line arrow
```

#### Card Component
```text
Hyundai KR 스타일의 이미지 카드/뉴스 모듈을 만들어줘.
- 배경: #FFFFFF 또는 실제 사진
- 구조선: 필요할 때만 1px #E5E5E5
- radius: 0에 가깝게, 과한 rounded card 금지
- 태그: top-left 20-30px, 12-14px HyundaiSansTextKR, white on rgba(0,0,0,.5)
- hover/focus: tag border #FFFFFF로 상태를 표시하고 큰 shadow/scale은 쓰지 말 것
```

#### Badge
```text
Hyundai KR 스타일의 상태/분류 배지를 만들어줘.
- font: HyundaiSansTextKR, 12-14px, letter-spacing -0.4px
- rectangular tag, not pill
- dark overlay badge: background rgba(0,0,0,.5), color #FFFFFF
- official link badge: #002C5F text, no decorative gradient
```

#### Navigation
```text
Hyundai KR 스타일 상단 네비게이션을 만들어줘.
- 좌측 HYUNDAI 로고, 중앙 모델/구매/서비스/디지털/브랜드 링크, 우측 언어/로그인/검색/메뉴
- desktop height 80px, tablet 64px
- active indicator: 4px #002C5F bottom bar with .4s ease left/width/opacity transition
- fixed state: rgba(255,255,255,.9), backdrop-filter blur(5px), border-bottom #E5E5E5
```

### Iteration Guide

- **색상 변경 시**: CTA/official accent는 #002C5F를 우선 사용. #409EFF는 framework hover처럼 보이므로 브랜드 주색으로 승격하지 말 것.
- **폰트 변경 시**: HyundaiSans가 없으면 Pretendard로 대체하되 `letter-spacing:-0.4px`를 유지.
- **여백 조정 시**: hero는 넓게, 하단 customer-action modules는 촘촘하게. 모든 섹션을 같은 간격으로 만들지 말 것.
- **새 컴포넌트 추가 시**: radius와 shadow를 줄이고 hairline, image, typography로 구조를 만든다.
- **모션 추가 시**: nav bar, header reveal, carousel control처럼 상태 설명에 쓰고, scroll spectacle은 피한다.
- **모달/캠페인 추가 시**: 페이지를 dim 처리하고 rectangular official panel을 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #002C5F as the official Hyundai blue for CTAs, nav indicators, and authoritative links.
- Preserve HyundaiSansHeadKR / HyundaiSansTextKR hierarchy or compensate with Pretendard plus tight tracking.
- Let vehicle photography carry visual drama; keep UI chrome thin and operational.
- Use #E5E5E5 hairlines and blur for fixed header depth instead of generic shadow.
- Keep desktop navigation dense and task-oriented: model, purchase, service, digital support, brand, certified used cars.
- Use rectangular controls and text CTAs more often than rounded SaaS buttons.
- Treat Element UI colors as framework states, not brand identity.
- Write unknowns as gaps rather than inventing tokens; this CSS exposes no custom-property design token layer.

### ❌ DON'T

- 배경을 `#F8FAFC` 또는 `#FAFAFA`로 두지 말 것 — Hyundai base surface는 `#FFFFFF`, warm campaign surface는 `#F6F3F2` 사용.
- 텍스트를 `#111827` 또는 generic slate로 두지 말 것 — primary text는 `#000000`, muted text는 `#666666` 사용.
- 브랜드 CTA를 `#409EFF`로 두지 말 것 — 대신 Hyundai anchor `#002C5F` 사용.
- hairline을 `#E5E7EB`로 일반화하지 말 것 — 관찰된 header/layer line은 `#E5E5E5` 사용.
- warm surface를 임의의 beige `#F5F0E8`로 만들지 말 것 — 관찰된 warm values는 `#F6F3F2`와 `#E4DCD3`.
- body에 `font-weight: 300`을 기본으로 쓰지 말 것 — HyundaiSansTextKR default는 400 중심이다.
- 모든 버튼을 `border-radius: 999px` pill로 만들지 말 것 — Hyundai CTA는 rectangular/fixed-width/text-link 성향이 강하다.
- generic card shadow `0 10px 30px rgba(0,0,0,.12)`를 남발하지 말 것 — chrome depth는 border/blur/photography로 만든다.
- hero를 gradient mesh로 대체하지 말 것 — 차량 이미지가 핵심 매체다.
- `#007FA8`을 모든 곳에 뿌리지 말 것 — 보조 chromatic으로만 제한하고 official emphasis는 `#002C5F`로 회수한다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No public CSS variable token tier** - phase1 found `total_vars: 0`; do not pretend there is a native `--hyundai-color-brand` API.
- **No second loud brand palette** - blue dominates; success/warning/error colors are framework states, not brand campaign colors.
- **No gradient-led identity** - hero drama comes from vehicle photography and campaign artwork, not background gradients.
- **No soft SaaS pill universe** - rectangular CTAs, text links, and thin line controls are closer to the site.
- **No heavy elevation system** - header fixed state uses blur + hairline; cards do not need layered shadows.
- **No playful illustration system** - real product/vehicle imagery and official icons carry the visual load.
- **No editorial prose-first layout** - content is task-oriented: purchase, service, EV, shop, news, corporate links.
- **No monochrome luxury minimalism** - Hyundai uses practical blue anchors and dense utility navigation.
- **No generic Inter-only typography** - without HyundaiSans or compensated Korean fallback, the page loses its official automotive character.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Screenshot modal overlay** - `hero-cropped.png` contains a launch-event modal that dims the hero. Hero interpretation separates temporary campaign overlay from the base homepage chassis.
- **No fresh network fetch in this run** - existing phase1 artifacts were reused as requested. The live Hyundai homepage on 2026-05-03 may differ from the April phase1 snapshot.
- **CSS custom properties absent** - `resolved_tokens.json` reports zero CSS variables, so named tokens in this guide are guidebook aliases, not native implementation tokens.
- **Single homepage scope** - purchase configurator, login, forms, checkout, map/search, and service reservation flows were not visited.
- **Dark mode not established** - no complete dark-theme palette was observed; dark values in this guide are local text/overlay uses.
- **Element UI contamination** - high-frequency #409EFF, #C0C4CC, #EBEEF5, #67C23A, #F56C6C include framework defaults. They are recorded but not treated as Hyundai brand identity.
- **Exact font files and licensing not audited** - font family names were extracted from CSS, but license and font-file inventory were not independently verified.
- **Motion JS not inspected** - CSS transition values were captured, but carousel timing, pause rules, and modal behavior likely depend on JavaScript not analyzed here.
- **Mobile screenshots not captured** - responsive behavior is inferred from CSS breakpoints, not from a mobile visual capture.
- **Campaign artwork colors excluded** - the modal image includes a deep red block, but it is image content rather than a reusable CSS color token.
