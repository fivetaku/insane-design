---
schema_version: 3.2
slug: kurly
service_name: Kurly
site_url: https://www.kurly.com
fetched_at: 2026-04-15T14:17:00+09:00
default_theme: light
brand_color: "#5F0080"
primary_font: Pretendard
font_weight_normal: 400
token_prefix: kpds

bold_direction: Purple Commerce
aesthetic_category: other
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high

archetype: commerce-marketplace
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "270 CSS custom properties, a complete light/dark token block, and repeated commerce components are present, but semantic alias names are mostly compiled kpds ids."

colors:
  kpds_ldmw172m: "#5F0080"
  kpds_ldmw172n: "#672091"
  kpds_ldmw173b: "#BD76FF"
  kpds_ldmw172x: "#F5EFFA"
  kpds_ldmw171v: "#FFFFFF"
  kpds_ldmw172a: "#1C1C1C"
  kpds_ldmw172b: "#222222"
  kpds_ldmw172l: "#F2F5F8"
  kpds_ldmw172h: "#BCC4CC"
  kpds_ldmw172y: "#F95019"
  kpds_ldmw1739: "#FFF6F3"
typography:
  display: "Pretendard"
  body: "Pretendard"
  fallback_observed: "Noto Sans KR"
  ladder:
    - { token: kpds_ldmw17s, size: "14px", weight: 400, line_height: "22px" }
    - { token: kpds_ldmw17r, size: "16px", weight: 400, line_height: "22px" }
    - { token: kpds_ldmw17q, size: "18px", weight: 600, line_height: "26px" }
    - { token: kpds_ldmw17p, size: "20px", weight: 600, line_height: "28px" }
    - { token: kpds_ldmw17b, size: "24px", weight: 700, line_height: "32px" }
    - { token: kpds_ldmw17d, size: "36px", weight: 700, line_height: "44px" }
  weights_used: [400, 500, 600, 700]
  weights_absent_in_core: [300, 800, 900]
components:
  search-input: { border: "1px solid #5F0080", radius: "6px", height: "48px" }
  top-banner: { bg: "#5F0080", fg: "#FFFFFF", height: "42px" }
  coupon-card: { bg: "#F5EFFA", accent: "#BD76FF", radius: "6px" }
  product-card: { bg: "#FFFFFF", radius: "8px", shadow: "none" }
---

# DESIGN.md — Kurly Designer Guidebook

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Kurly reads like a refrigerated marketplace where every aisle has been measured with a ruler: clinical white canvas, tightly labeled counters, and one unmistakable house color, deep purple #5F0080 (`{colors.kpds_ldmw172m}`). There is no second brand color competing for attention. The banner, search border, coupon economics, selected states, and cart memory all return to the same purple register, so the store feels edited rather than scattered.

The visible homepage rhythm is a sandwich of dense utility and promotional editorial. The top 200px works like a checkout counter before the aisle begins: coupon strip, logo, membership links, search, location, favorite, cart, category navigation. Below it, the hero turns into a refrigerated display case: photography creates appetite, while a lavender coupon object in #F5EFFA (`{colors.kpds_ldmw172x}`) interrupts the white grid like a clipped paper voucher placed on glass.

Kurly's purple is not atmospheric wallpaper; it is a cashier stamp. It appears where the user can act, save, search, or commit. The rest of the chrome stays #FFFFFF (`{colors.kpds_ldmw171v}`), like a clean market counter that deliberately disappears behind produce photography and product metadata. Shadow does not try to make every product float. Product cards stay flat; appetite comes from the image, not from SaaS-style elevation.

Typography is Korean commerce typography rather than Western SaaS display. Pretendard is the tokenized family, while Noto Sans KR appears as a legacy or fallback layer. The type scale is compact: 14px and 16px do most of the operational work, 20px to 24px handle section labels, and heavier 700 appears only where purchase confidence must rise. It reads less like a campaign poster and more like a well-run grocery ledger: prices, categories, badges, and benefits are all legible at shopping speed.

The site's craft lives in commerce micro-structure: one purple search border, pill delivery badges, coupon rectangles, small icon counters, and product grids that let photography carry the appetizing detail. Kurly does not use decorative gradients as a brand language. Even when gradients appear in datepicker range CSS, the shopping surface is anchored by flat surfaces, hairline borders, and one strong CTA color. The signature is a market shelf with no theatrical lighting: white shelf, purple price tag, product first.

이 페이지는 결국 **푸드 마켓의 진열대와 카운터, 그리고 카탈로그**가 한 화면에 펼쳐진 구조다. 상단 banner는 매대 위 가격 카드, 검색창은 카운터의 호출 마이크, 쿠폰 카드는 진열대 한 칸에 놓인 종이 바우처다. 카테고리 nav는 마켓의 통로 표지판처럼 짧은 명사들로 정렬되고, 장바구니 아이콘은 매대 끝의 카트처럼 항상 우상단에 대기한다. 물류센터의 창고 효율을 닮은 14px 라인 간격이 카탈로그의 가격표를 빠르게 읽게 만든다 — 상품 사진은 매대 위 진열, 보라색은 가격표 잉크, 흰 카드는 진열대 위의 닦인 유리다. 아이쇼핑이 아니라, 카운터까지의 동선을 짧게 만든 마켓이다.

### Key Characteristics

- Single chromatic anchor: #5F0080 (`{colors.kpds_ldmw172m}`) as brand, search, banner, and primary commerce cue.
- White commerce chrome: #FFFFFF (`{colors.kpds_ldmw171v}`) carries the header and product cards.
- Lavender promotion layer: #F5EFFA and #BD76FF appear in coupon/date/benefit contexts, not as a general background system.
- Compact Korean typography: 14px default body, 16px utility labels, 20px-24px section and promo headings.
- 1050px-class marketplace width implied by the desktop screenshot, with dense navigation and product rows.
- Shadow is rare and modest; surfaces separate mostly through white, gray hairlines, and image edges.
- Icons are functional black or purple line glyphs; they are not illustrative decoration.
- Hero is promotional and photographic, but the header remains strict and utility-first.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Purple Commerce
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **single-purple grocery marketplace chrome**으로 기억된다.
> **Code Complexity**: medium — tokenized KPDS variables, light/dark themes, datepicker states, and marketplace components without heavy motion or 3D.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Kurly처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: Pretendard, "Pretendard Variable", "Noto Sans KR", -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
  font-size: 14px;
  font-weight: 400;
  line-height: 22px;
}

/* 2. 배경 + 텍스트 */
:root {
  --kurly-bg: #FFFFFF;
  --kurly-fg: #222222;
  --kurly-muted: #848F9A;
}
body { background: var(--kurly-bg); color: var(--kurly-fg); }

/* 3. 브랜드 컬러 */
:root {
  --kurly-purple: #5F0080;
  --kurly-purple-hover: #672091;
  --kurly-purple-soft: #F5EFFA;
}
```

**절대 하지 말아야 할 것 하나**: primary CTA와 검색창을 파란색이나 검정으로 재해석하지 말 것. Kurly의 인터랙션 기억점은 #5F0080 하나다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.kurly.com` |
| Fetched | 2026-04-15T14:17:00+09:00 |
| Extractor | cached phase1 reuse from `insane-design/kurly` |
| HTML size | 97,360 bytes |
| CSS files | 2 files, 226,372 chars |
| Token prefix | `kpds` |
| Method | CSS custom properties, frequency candidates, screenshot, and cached HTML/CSS interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React/Next-style client bundle inferred from static HTML structure and compiled CSS.
- **Design system**: KPDS token block — prefix `--kpds_*`; ids are compiled, not human semantic names.
- **CSS architecture**:
  ```css
  --kpds_ldmw17*   /* size, type, spacing, radius primitives */
  --kpds_ldmw172*  /* neutral and purple color ramp */
  --kpds_ldmw173*  /* orange, violet, and semantic accent ramps */
  ```
- **Class naming**: generated classes such as `.kpds_9z347w3`, plus third-party `react-datepicker__*`.
- **Default theme**: light, with `[data-theme=light]` and `[data-theme=dark]` token blocks both present.
- **Font loading**: tokenized family starts with Pretendard / Pretendard Variable, followed by system and Korean fallbacks.
- **Canonical anchor**: the desktop homepage header and hero screenshot; checkout, login, and product detail flows were not visited.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Pretendard` / `Pretendard Variable`
- **Body font**: `Pretendard`
- **Observed fallback**: `'Noto Sans KR'`, `"Malgun Gothic"`, `"Apple SD Gothic Neo"`
- **Code font**: `monospace, monospace` only in reset/utility CSS
- **Weight normal / bold**: `400` / `700`; `600` is the important middle emphasis.

```css
:root {
  --kpds-font-family: Pretendard, "Pretendard Variable", -apple-system, BlinkMacSystemFont,
    system-ui, Roboto, "Helvetica Neue", "Segoe UI", "Apple SD Gothic Neo",
    "Noto Sans KR", "Malgun Gothic", sans-serif;
  --kpds-font-weight-normal: 400;
  --kpds-font-weight-semibold: 600;
  --kpds-font-weight-bold: 700;
}
body {
  font-family: var(--kpds-font-family);
  font-weight: var(--kpds-font-weight-normal);
}
```

### Note on Font Substitutes

- **Pretendard unavailable**: use `Noto Sans KR` first, not Inter. Kurly's product/category labels need Korean glyph rhythm more than Latin SaaS geometry.
- **Line-height correction**: keep body at 14px / 22px. If fallback text feels taller, reduce section label line-height from 24px to 22px rather than shrinking font size.
- **Weight correction**: map Pretendard 600 to Noto Sans KR 700 for navigation labels if the Korean text looks too pale. Do not use 800/900 for product or category chrome.
- **Letter-spacing**: keep `0` for body and navigation. The site uses no broad tracking system; added tracking makes the store feel like a brand campaign instead of a marketplace.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `--kpds_ldmw17s` | 14px | 400 | 22px | 0 |
| `--kpds_ldmw17r` | 16px | 400 | 22px | 0 |
| `--kpds_ldmw17q` | 18px | 600 | 26px | 0 |
| `--kpds_ldmw17p` | 20px | 600 | 28px | 0 |
| `--kpds_ldmw17b` | 24px | 700 | 32px | 0 |
| `--kpds_ldmw17d` | 36px | 700 | 44px | 0 |

> ⚠️ Kurly의 타입은 hero-display보다 commerce readability가 우선이다. 14px default와 16px utility label이 시스템의 실제 중심이다.

### Principles

1. Body starts at 14px, not 16px — the store needs high information density in navigation, badges, and product metadata.
2. Weight 600 is the commerce emphasis weight — category tabs and section labels use firmness without jumping to heavy campaign typography.
3. Weight 700 is reserved for promotion, price, and high-attention headings. It should not be applied to every card title.
4. Letter-spacing is essentially absent. Korean legibility comes from clean glyph choice and line-height, not optical tracking.
5. The scale is compact but not cramped: 14/16/18/20/24/36 covers almost all visible surface needs.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (11 steps)

| Token | Hex |
|---|---|
| `--kpds_ldmw172m` | `#5F0080` |
| `--kpds_ldmw172n` | `#672091` |
| `--kpds_ldmw172o` | `#7E3AB0` |
| `--kpds_ldmw172p` | `#8D4CC4` |
| `--kpds_ldmw172q` | `#9A60CA` |
| `--kpds_ldmw172r` | `#A775D2` |
| `--kpds_ldmw172s` | `#B489D8` |
| `--kpds_ldmw172t` | `#C19EDF` |
| `--kpds_ldmw172u` | `#CEB2E6` |
| `--kpds_ldmw172v` | `#DCC7ED` |
| `--kpds_ldmw172w` | `#E8DBF3` |
| `--kpds_ldmw172x` | `#F5EFFA` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--kpds_ldmw172m` | `#9F53E0` |
| `--kpds_ldmw172n` | `#8D4CC4` |
| `--kpds_ldmw172o` | `#8147B2` |
| `--kpds_ldmw172p` | `#7542A1` |
| `--kpds_ldmw172w` | `#2B2232` |
| `--kpds_ldmw172x` | `#231F26` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white/base | `#FFFFFF` | `#222222` |
| ink-900 | `#1C1C1C` | `#FFFFFF` |
| ink-800 | `#222222` | `#F2F5F8` |
| gray-700 | `#393D41` | `#DDE2E8` |
| gray-600 | `#565E67` | `#A7B2BC` |
| gray-500 | `#848F9A` | `#848F9A` |
| gray-300 | `#BCC4CC` | `#505760` |
| gray-100 | `#ECEFF3` | `#303337` |
| gray-050 | `#F2F5F8` | `#222222` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Orange promo/error-adjacent | `--kpds_ldmw172y` | `#F95019` |
| Orange soft | `--kpds_ldmw1739` | `#FFF6F3` |
| Bright violet | `--kpds_ldmw173b` | `#BD76FF` |
| Datepicker hover blue | literal | `#216BA5` |
| Warning yellow | literal | `#FEE500` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--kpds_ldmw172m` | `#5F0080` | brand, search, banner, selected/primary UI |
| `--kpds_ldmw172x` | `#F5EFFA` | purple-tinted soft surface |
| `--kpds_ldmw171v` | `#FFFFFF` | header/page/card base |
| `--kpds_ldmw172b` | `#222222` | primary text / icon ink |
| `--kpds_ldmw172f` | `#848F9A` | muted text |
| `--kpds_ldmw172h` | `#BCC4CC` | border / disabled / hairline |
| `--kpds_ldmw172y` | `#F95019` | urgent promo accent |

### 06-6. Semantic Alias Layer

The extracted `alias_layer.json` classifies 200 variables as `core` and 0 as util/semantic/action/component aliases. In practice, KPDS is a token system in use, but the public CSS is compiled into opaque ids. Preserve the ids when fidelity matters.

| Alias | Resolves to | Usage |
|---|---|---|
| `--kpds_ldmw172m` | `#5F0080` | canonical brand purple |
| `--kpds_ldmw172n` | `#672091` | darker hover/pressed purple |
| `--kpds_ldmw172x` | `#F5EFFA` | soft purple background |
| `--kpds_ldmw171n` | `0px 2px 2px 0px rgba(0,0,0,.03)` | low elevation |
| `--kpds_ldmw171s` | `0px 0px 30px 0px rgba(0,0,0,.25)` | heavier overlay/elevation |

### 06-7. Dominant Colors (actual CSS frequency)

| Token | Hex | Frequency |
|---|---:|---:|
| white | `#FFFFFF` | 37 |
| black | `#000000` | 13 |
| ink | `#222222` | 8 |
| border gray | `#AEAEAE` | 7 |
| bright violet | `#BD76FF` | 7 |
| soft lavender | `#F6F4F9` | 6 |
| gray | `#CCCCCC` | 5 |
| cool surface | `#F2F5F8` | 5 |

### 06-8. Color Stories

**`--kpds_ldmw172m` (#5F0080)** — The single brand memory. It belongs on the top banner, the search outline, primary CTA states, selected tabs, and membership prompts. Do not dilute it with a second primary color.

**`--kpds_ldmw171v` (#FFFFFF)** — The retail floor. It keeps the header, product cards, and product photography neutral so food and beauty images can carry appetite and trust.

**`--kpds_ldmw172b` (#222222)** — Operational ink. Navigation, icons, product labels, and headings use near-black rather than pure black as the main reading color.

**`--kpds_ldmw172h` (#BCC4CC)** — Functional hairline gray. It supports form borders, disabled affordances, datepicker chrome, and separation without becoming a visible brand color.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--kpds_ldmw17t` | 2px | micro offset / icon nudges |
| `--kpds_ldmw17u` | 4px | tight internal gap |
| `--kpds_ldmw17v` | 6px | compact controls |
| `--kpds_ldmw17w` | 8px | badge/card small padding |
| `--kpds_ldmw17y` | 12px | common inline gap |
| `--kpds_ldmw17z` | 16px | default control padding |
| `--kpds_ldmw1710` | 24px | card and section internal padding |
| `--kpds_ldmw1711` | 32px | section cluster gap |
| `--kpds_ldmw1714` | 64px | large vertical space |
| `--kpds_ldmw1717` | 160px | large layout offset / overlay reserve |

**주요 alias**:
- `--kpds_ldmw17z` -> 16px, search/input/card padding default.
- `--kpds_ldmw1710` -> 24px, larger card or section rhythm.
- `--kpds_ldmw1714` -> 64px, editorial spacing between major blocks.

### Whitespace Philosophy

Kurly uses two different spacing moods on the same screen. The header is dense: logo, search, utility icons, category nav, and membership links all sit in a compact commerce machine. That density is intentional because users are expected to search, compare, and buy repeatedly.

Promotion and editorial space below the nav is looser. The hero banner allows a large photo and floating coupon card to breathe, then product ranking cards return to a compressed grid. The rule is "wide breath for campaign, tight rhythm for shopping."

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token / value | Value | Context |
|---|---:|---|
| `--kpds_ldmw171e` | 4px | small controls |
| `--kpds_ldmw171f` | 6px | tooltip, search, coupon card |
| `--kpds_ldmw171g` | 8px | product cards, containers |
| `--kpds_ldmw171i` | 12px | larger soft container |
| literal | 50px | circular datepicker selected state |
| literal | 50% | icon/avatar/circle controls |
| literal | 999px equivalent | delivery pill / capsule badges |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| low | `0px 2px 2px 0px rgba(0,0,0,.03)` | subtle raised surface |
| menu | `0px 0px 4px 0px rgba(0,0,0,.15)` | overlays / popovers |
| card | `2px 2px 10px 0px rgba(0,0,0,.1)` | promotional panels |
| overlay | `0px 0px 30px 0px rgba(0,0,0,.25)` | heavier modal or hero overlay |

Shadow is present as a token family, but the visible homepage chrome uses it sparingly. Product cards and header structure should not become floating SaaS cards.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / pattern | Value | Usage |
|---|---|---|
| quick fade | `all .1s ease-out` | small state changes |
| default transition | `all .25s ease-out` | buttons/tooltips |
| panel transition | `all .3s ease-out` | larger state changes |
| tooltip | `opacity .12s ease, transform .12s ease` | micro overlay reveal |

Motion should remain serviceable. Use opacity/color transitions and small transform shifts; avoid scroll-driven spectacle.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: 1050px-class desktop marketplace container inferred from screenshot; CSS extraction did not expose a clean semantic container token.
- **Grid type**: flex/grid hybrid; header rows use flex alignment, product ranking below uses card rows.
- **Column count**: navigation has 6 primary groups visible; product cards begin as 4-column row in the captured viewport.
- **Gutter**: 16px to 24px for product cards; 32px+ for section separation.

### Hero

- **Pattern Summary**: 370px-480px promotional banner + white commerce header + floating lavender benefit card.
- Layout: full-width campaign image behind/next to a fixed-width centered content area.
- Background: photographic promotional image with a pale gray field in the captured hero.
- **Background Treatment**: image/solid mix; no global gradient mesh. Coupon card carries lavender and purple flat fills.
- H1: approximately 28px-36px / weight 700 / tracking 0 in the floating promotion card.
- Max-width: 1050px-class internal alignment.

### Section Rhythm

```css
section {
  padding: 32px 0 64px;
  max-width: 1050px;
}
.commerce-row {
  gap: 16px;
}
```

### Card Patterns

- **Card background**: `#FFFFFF` for product cards, `#F5EFFA` for promotion/coupon panels.
- **Card border**: minimal or none on product cards; gray hairlines appear in inputs and overlays.
- **Card radius**: 6px-8px default, larger capsules for delivery badges.
- **Card padding**: 16px to 24px; coupon card uses more generous internal spacing.
- **Card shadow**: none or very low; promotional overlay may use tokenized card shadow.

### Navigation Structure

- **Type**: horizontal commerce header with utility strip, logo/search row, and category row.
- **Position**: static/sticky-like header chrome in screenshot; no verified sticky behavior from cached data.
- **Height**: about 200px total including banner and nav; top banner about 42px.
- **Background**: `#FFFFFF` except top coupon strip `#5F0080`.
- **Border**: light gray divider/shadow line between nav and hero.

### Content Width

- **Prose max-width**: not a prose site; product and category containers dominate.
- **Container max-width**: 1050px-class desktop alignment.
- **Sidebar width**: not visible on homepage; category menu likely opens separately.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Compact | `max-width: 400px` | Datepicker small-height/small-width guard appears in CSS. |
| Short viewport | `max-height: 550px` | Datepicker behavior guard. |
| Fine pointer | `(hover:hover) and (pointer:fine)` | Hover-only interactions are gated for pointer devices. |
| Dark preference | `(prefers-color-scheme:dark)` | Theme branch exists but homepage default is light. |

### Touch Targets

- **Minimum tap size**: tokenized 44px appears as `--kpds_ldmw17j`.
- **Button height (mobile)**: 40px-44px family.
- **Input height (mobile)**: search/input patterns use roughly 44px-48px.

### Collapsing Strategy

- **Navigation**: not fully verified from cached desktop screenshot; expect category/search compression and icon retention.
- **Grid columns**: product cards should collapse from 4 columns to 2/1 by viewport.
- **Sidebar**: category drawer behavior not observed.
- **Hero layout**: promotional image/card should stack or crop on mobile.

### Image Behavior

- **Strategy**: product and campaign photography are primary content; preserve aspect ratios.
- **Max-width**: 100% patterns present in CSS.
- **Aspect ratio handling**: product cards should crop with object-fit-like behavior, but exact selector was not isolated.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<button class="kurly-button kurly-button--primary">지금 바로 가입하고 혜택 받기</button>
```

| State | Spec |
|---|---|
| default | bg `#5F0080`, fg `#FFFFFF`, radius 6px or pill by context, weight 600 |
| hover | bg `#672091` or darker purple family |
| focus | purple border/focus ring; do not switch to blue browser-default focus |
| disabled | gray text/border using `#BCC4CC` / `#ECEFF3` |
| loading | preserve button width; avoid spinner color outside purple/white |
| active | pressed purple, no large transform |

### Badges

```html
<span class="kurly-badge kurly-badge--delivery">샛별·하루 배송안내</span>
```

| Variant | Spec |
|---|---|
| delivery pill | white bg, light gray border, purple emphasis text, pill radius |
| coupon flag | bright violet `#BD76FF`, white text, compact 10-12px label |
| cart counter | purple circle, white number, icon-adjacent |

### Cards & Containers

```html
<article class="kurly-product-card">
  <img class="kurly-product-card__image" alt="">
  <h3 class="kurly-product-card__title">상품명</h3>
  <p class="kurly-product-card__price">12,900원</p>
</article>
```

| Part | Spec |
|---|---|
| product card | bg `#FFFFFF`, radius 8px, shadow none, image-first |
| coupon card | bg `#F5EFFA`, purple ticket graphics, radius 6px, mild shadow |
| ranking section | white surface, 20px-24px heading, product row below |
| hover | product image or text state only; avoid floating-card transform language |

### Navigation

```html
<header class="kurly-header">
  <div class="kurly-top-banner">지금 가입하고 최대 1만 2천원 할인 쿠폰 받아가세요!</div>
  <div class="kurly-header__main">
    <a class="kurly-logo">Kurly</a>
    <input class="kurly-search" placeholder="검색어를 입력해주세요">
  </div>
  <nav class="kurly-nav">...</nav>
</header>
```

| Part | Spec |
|---|---|
| top banner | height about 42px, bg `#5F0080`, centered white 14px text |
| logo row | white bg, logo left, search centered, icon cluster right |
| search | 48px height, 400px-class width, border `#5F0080`, radius 6px |
| nav row | category icon left, 6 top categories, medium 16px labels |

### Inputs & Forms

```html
<label class="kurly-search-field">
  <input placeholder="검색어를 입력해주세요">
  <button aria-label="검색"></button>
</label>
```

| State | Spec |
|---|---|
| default | bg `#FFFFFF`, border `#5F0080`, radius 6px, height 48px |
| placeholder | muted gray, 16px |
| focus | keep purple border; do not add blue glow |
| error | use orange/red family such as `#F95019` only for validation |
| disabled | `#F2F5F8` bg and `#BCC4CC` text/border |

### Hero Section

```html
<section class="kurly-hero">
  <div class="kurly-benefit-card">...</div>
  <img class="kurly-hero__image" alt="">
</section>
```

| Part | Spec |
|---|---|
| hero image | full-width campaign photography, pale background, horizontal crop |
| benefit card | lavender `#F5EFFA`, purple tickets, strong 28px-36px discount type |
| hero CTA | bottom strip bg `#8D4CC4` or primary purple family, white text |
| carousel control | dark translucent circular control, small white text |

### 13-2. Named Variants

| Variant | Spec |
|---|---|
| `top-banner-purple` | `#5F0080` strip, white centered message, close icon at right |
| `search-primary-border` | white input, 1px `#5F0080`, 6px radius, purple search icon |
| `coupon-lavender-card` | `#F5EFFA` panel with violet ticket pieces `#BD76FF` |
| `delivery-outline-pill` | white pill, gray hairline, purple emphasized phrase |
| `cart-counter-dot` | purple circle attached to cart icon, white numeric label |
| `product-ranking-card` | image-first white card, no chrome shadow, product text below |

### 13-3. Signature Micro-Specs

```yaml
single-purple-checkout-loop:
  description: "Search, banner, CTA, selected state, and counter feedback all resolve into one Kurly purple loop."
  technique: "#5F0080 primary /* {colors.kpds_ldmw172m} */ + #672091 hover/pressed /* {colors.kpds_ldmw172n} */ + #F5EFFA soft promotion surface /* {colors.kpds_ldmw172x} */"
  applied_to: ["{component.search-input}", "{component.top-banner}", "CTA strips", "selected/promo states", "cart counter"]
  visual_signature: "every buying action carries the same purple cashier-stamp memory without recoloring the whole page"

purple-border-search-instrument:
  description: "The search field is treated as the main commerce instrument, not as a neutral form input."
  technique: "48px height + 400px-class width + 1px #5F0080 border /* {colors.kpds_ldmw172m} */ + 6px radius + 16px placeholder rhythm"
  applied_to: ["{component.search-input}", "header search row"]
  visual_signature: "a white header is punctured by one precise purple rectangle that immediately says 'shop here'"

lavender-coupon-display-case:
  description: "Promotional economics become a hero object through a lavender card layered against campaign photography."
  technique: "#F5EFFA panel /* {colors.kpds_ldmw172x} */ + #BD76FF ticket/accent pieces /* {colors.kpds_ldmw173b} */ + 6px radius + restrained card shadow only on the promo object"
  applied_to: ["{component.coupon-card}", "hero benefit card", "first-viewport promotion"]
  visual_signature: "a clipped paper coupon appears inside the photographic display case rather than becoming a generic grid card"

flat-shelf-product-grid:
  description: "Product cards stay visually flat so food and product photography carry appetite and trust."
  technique: "#FFFFFF card surface /* {colors.kpds_ldmw171v} */ + 8px radius + box-shadow:none + image-first crop + gray metadata hierarchy"
  applied_to: ["{component.product-card}", "product ranking rows", "commerce grid"]
  visual_signature: "market-shelf flatness: no floating SaaS card stack, just product image, price, and compact metadata"

korean-ledger-type-density:
  description: "The store uses compact Korean shopping typography for fast scanning instead of campaign-scale display drama."
  technique: "Pretendard/Noto Sans KR stack + 14px/22px body + 16px utility labels + 600/700 emphasis + letter-spacing:0"
  applied_to: ["navigation labels", "product card text", "input placeholders", "section headings", "badges"]
  visual_signature: "dense but calm Korean commerce ledger where prices, labels, and benefits stay readable at shopping speed"
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Promotional headline | direct benefit + concrete amount | "최대 12,000원 할인" |
| Primary CTA | immediate action + benefit | "지금 바로 가입하고 혜택 받기" |
| Navigation | short noun categories | "베스트", "세일", "패션", "리빙", "신상" |
| Delivery badge | branded delivery phrase plus 안내 | "샛별·하루 배송안내" |
| Tone | practical, benefit-forward, family-safe | "내일 아침 문 앞에서 만나요" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Kurly — copy into your root stylesheet */
:root {
  /* Fonts */
  --kurly-font-family: Pretendard, "Pretendard Variable", -apple-system, BlinkMacSystemFont,
    system-ui, Roboto, "Helvetica Neue", "Segoe UI", "Apple SD Gothic Neo",
    "Noto Sans KR", "Malgun Gothic", sans-serif;
  --kurly-font-weight-normal: 400;
  --kurly-font-weight-semibold: 600;
  --kurly-font-weight-bold: 700;

  /* Brand */
  --kurly-purple-900: #5F0080;
  --kurly-purple-800: #672091;
  --kurly-purple-600: #8D4CC4;
  --kurly-purple-400: #BD76FF;
  --kurly-purple-050: #F5EFFA;

  /* Surfaces */
  --kurly-bg-page: #FFFFFF;
  --kurly-bg-soft: #F2F5F8;
  --kurly-text: #222222;
  --kurly-text-muted: #848F9A;
  --kurly-border: #BCC4CC;
  --kurly-promo-orange: #F95019;

  /* Spacing */
  --kurly-space-xs: 4px;
  --kurly-space-sm: 8px;
  --kurly-space-md: 16px;
  --kurly-space-lg: 24px;
  --kurly-space-xl: 64px;

  /* Radius */
  --kurly-radius-sm: 4px;
  --kurly-radius-md: 6px;
  --kurly-radius-lg: 8px;
  --kurly-radius-pill: 999px;
}

body {
  margin: 0;
  background: var(--kurly-bg-page);
  color: var(--kurly-text);
  font-family: var(--kurly-font-family);
  font-size: 14px;
  font-weight: 400;
  line-height: 22px;
}

.kurly-top-banner {
  height: 42px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--kurly-purple-900);
  color: #FFFFFF;
  font-weight: 600;
}

.kurly-search {
  height: 48px;
  width: min(400px, 100%);
  border: 1px solid var(--kurly-purple-900);
  border-radius: var(--kurly-radius-md);
  padding: 0 44px 0 16px;
  color: var(--kurly-text);
  font-size: 16px;
}

.kurly-primary-button {
  border: 0;
  border-radius: var(--kurly-radius-md);
  background: var(--kurly-purple-900);
  color: #FFFFFF;
  padding: 12px 24px;
  font-weight: 600;
  transition: all .25s ease-out;
}
.kurly-primary-button:hover { background: var(--kurly-purple-800); }

.kurly-product-card {
  background: #FFFFFF;
  border-radius: var(--kurly-radius-lg);
  box-shadow: none;
  overflow: hidden;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Kurly approximation
module.exports = {
  theme: {
    extend: {
      colors: {
        kurly: {
          purple: '#5F0080',
          purpleHover: '#672091',
          violet: '#BD76FF',
          lavender: '#F5EFFA',
          ink: '#222222',
          muted: '#848F9A',
          border: '#BCC4CC',
          surface: '#FFFFFF',
          surfaceSoft: '#F2F5F8',
          orange: '#F95019',
        },
      },
      fontFamily: {
        sans: ['Pretendard', 'Pretendard Variable', 'Noto Sans KR', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        kurly: '6px',
        product: '8px',
        pill: '999px',
      },
      boxShadow: {
        kurlyLow: '0px 2px 2px 0px rgba(0,0,0,.03)',
        kurlyPanel: '2px 2px 10px 0px rgba(0,0,0,.1)',
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
| Brand primary | `--kpds_ldmw172m` | `#5F0080` |
| Brand hover | `--kpds_ldmw172n` | `#672091` |
| Background | `--kpds_ldmw171v` | `#FFFFFF` |
| Soft background | `--kpds_ldmw172l` | `#F2F5F8` |
| Text primary | `--kpds_ldmw172b` | `#222222` |
| Text muted | `--kpds_ldmw172f` | `#848F9A` |
| Border | `--kpds_ldmw172h` | `#BCC4CC` |
| Promo accent | `--kpds_ldmw172y` | `#F95019` |

### Example Component Prompts

#### Hero Section

```text
Kurly 스타일의 커머스 히어로를 만들어줘.
- 상단은 #FFFFFF 기반의 밀도 높은 커머스 헤더
- 최상단 쿠폰 배너는 #5F0080 배경, 흰색 14px/600 텍스트
- 검색창은 48px 높이, 1px #5F0080 border, 6px radius
- 히어로는 프로모션 사진 + #F5EFFA 쿠폰 카드 조합
- 쿠폰 CTA는 purple family, white text, weight 600
```

#### Product Card

```text
Kurly 상품 카드를 만들어줘.
- 배경 #FFFFFF, radius 8px, shadow 없음
- 상품 이미지를 먼저 크게 배치
- 제목은 Pretendard 14px/400, 가격이나 할인은 16px-20px/700
- 보조 정보는 #848F9A
- hover에서 카드 전체를 띄우지 말고 이미지/텍스트 상태만 미세하게 바꿔
```

#### Search Header

```text
Kurly 검색 헤더를 만들어줘.
- 1050px 내외 중앙 컨테이너
- 왼쪽 Kurly 로고, 중앙 400px 검색창, 오른쪽 위치/찜/장바구니 아이콘
- 검색 border와 아이콘은 #5F0080
- nav labels는 16px/600, color #222222
```

#### Promotion Badge

```text
Kurly 프로모션 배지를 만들어줘.
- coupon label은 #BD76FF 배경과 #FFFFFF 텍스트
- soft panel은 #F5EFFA
- radius는 6px 또는 pill
- 주황 #F95019는 긴급 할인/에러성 강조에만 제한적으로 써
```

### Iteration Guide

- **색상 변경 시**: `#5F0080`을 중심으로 두고 hover는 `#672091`, soft panel은 `#F5EFFA`를 사용한다.
- **폰트 변경 시**: Korean-first fallback을 유지한다. Inter 단독 적용은 Kurly 표정을 잃게 만든다.
- **여백 조정 시**: 8/12/16/24/32/64px 계단을 우선한다.
- **새 컴포넌트 추가 시**: 제품/검색/쿠폰/배송안내 중 어느 commerce role인지 먼저 정하고 색을 배정한다.
- **다크 모드**: CSS에 dark token block은 있지만 캡처된 homepage default는 light다. dark 자동 전환을 기본값으로 만들지 않는다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#5F0080` as the single primary brand/action color.
- Keep the header mostly `#FFFFFF` with compact 14px-16px Korean commerce typography.
- Use `#F5EFFA` and `#BD76FF` for coupon/benefit surfaces, not for every section background.
- Preserve the search bar as a hero-level utility component: 48px height, purple border, centered in the header.
- Let product photography carry appetite and category specificity.
- Use low or no shadow for product cards; reserve stronger shadows for overlays or promotional cards.
- Keep navigation labels direct and noun-based.

### ❌ DON'T

- 배경을 `#F5EFFA` 전체 페이지로 두지 말 것 — 기본 페이지와 카드 surface는 `#FFFFFF` 사용.
- 텍스트를 `#000000` 또는 `black` 중심으로 과도하게 두지 말 것 — primary ink는 `#222222` 사용.
- primary CTA를 `#216BA5` 또는 blue 계열로 두지 말 것 — Kurly action은 `#5F0080` 사용.
- border를 `#000000`으로 두껍게 긋지 말 것 — hairline은 `#BCC4CC` 또는 더 연한 gray 사용.
- coupon surface를 `#FFFFFF`만으로 만들지 말 것 — benefit card에는 `#F5EFFA` / `#BD76FF` purple layer가 필요.
- orange `#F95019`를 primary brand로 승격하지 말 것 — promo/error accent에만 제한.
- body에 `font-weight: 700`을 기본값으로 쓰지 말 것 — 기본은 `400`, 강조는 `600`/`700`.
- product card에 큰 `box-shadow`를 일괄 적용하지 말 것 — 제품 그리드는 평평해야 한다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second brand color: none. Purple owns primary action; orange is not a co-brand.
- Gradient brand language: absent on the commerce chrome. Datepicker gradients are utility states, not brand atmosphere.
- Heavy card elevation: absent from product grids. Product photography and spacing do the work.
- Western SaaS hero typography: absent. There is no 64px Latin display headline system on the commerce homepage.
- Rounded mega-cards everywhere: absent. Radius is controlled at 6px-8px except pills/circles.
- Decorative illustration system: absent in the captured page. Photography, coupons, and icons are the visual assets.
- Aggressive motion: absent. Transitions stay around `.1s` to `.3s`, without parallax or scroll spectacle.
- Dark homepage default: absent. Dark tokens exist, but the observed site is light-first.
- Marketplace background photography overlay on chrome: absent. Only the hero panel uses imagery; the counter stays #FFFFFF.
- Decorative aisle lighting / illustrated cart icons: none. Icons stay functional line glyphs on the warehouse counter.
- Second discount color competing with purple price-tag ink: never. Orange `#F95019` is fenced as urgent-only, not a co-brand.
- Floating product-card hover lift on the shelf grid: zero. Shelf flatness is preserved at every breakpoint.
- Brand logo splash over the warehouse counter / banner inflation: absent. The cashier stamp stays a 42px strip.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single cached desktop surface** — Analysis reused `insane-design/kurly` phase1 assets and a desktop hero screenshot. Login, checkout, product detail, category drawer, and mobile interaction flows were not visited in this pass.
- **Compiled token names** — KPDS variables are real but opaque (`--kpds_ldmw172m` etc.). Semantic names in prose such as "brand purple" are interpretation layered over real CSS values, not source token names.
- **HTML hydration gap** — Cached `index.html` contains title/meta text but little semantic body markup, likely because the live app hydrates client-side. Layout/component analysis therefore relies heavily on screenshot and CSS.
- **Responsive behavior incomplete** — Only a few media queries were visible in the extracted CSS summary. Mobile navigation and product grid collapse are inferred from commerce patterns and available token sizes, not directly measured.
- **Motion logic incomplete** — CSS transitions were extracted, but JavaScript carousel timing, pause/play behavior, and scroll-trigger logic were not analyzed.
- **Color frequency contamination** — Datepicker and utility CSS contribute colors such as `#216BA5` and `#BD76FF`; brand selection intentionally prioritizes visible commerce UI and purple ramp over raw frequency alone.
- **Dark theme not applied to screenshot** — Dark token block exists, but the default Kurly homepage capture is light. Dark values are recorded as available tokens, not as observed default UI.
- **Exact container width unverified in CSS** — The 1050px-class container is inferred from the desktop screenshot and Korean marketplace convention; no clean semantic `max-width:1050px` token was isolated in the summarized CSS.
