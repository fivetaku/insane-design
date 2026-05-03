---
schema_version: 3.2
slug: dji
service_name: DJI
site_url: https://www.dji.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: light
brand_color: "#1E9DF7"
primary_font: "Open Sans"
font_weight_normal: 400
token_prefix: dui

bold_direction: "Airborne Minimalism"
aesthetic_category: "editorial-product"
signature_element: "hero_impact"
code_complexity: "high"

medium: web
medium_confidence: high
archetype: editorial-product
archetype_confidence: high
design_system_level: lv1
design_system_level_evidence: "CSS custom properties are absent; consistency comes from selector-level DUI classes, repeated homepage modules, and shared header/base styles."

colors:
  dui-surface-white: "#FFFFFF"
  dui-text-carbon: "#303233"
  dui-buy-blue-start: "#1E9DF7"
  dui-buy-blue-end: "#1392ED"
  dui-home-ice: "#F7F9FA"
  dui-module-gray: "#EDEDED"
  dui-hairline: "#F0F1F2"
  dui-muted: "#6C7073"
typography:
  display: "Open Sans"
  body: "Open Sans"
  icon: "Dji"
  ladder:
    - { token: hero-title, size: "40px", weight: 700, tracking: "0" }
    - { token: nav-link, size: "14px", weight: 400, tracking: "0" }
    - { token: cta, size: "16px", weight: 600, tracking: "0" }
  weights_used: [300, 400, 500, 600, 700, 800]
  weights_absent: []
components:
  dui-btn-primary: { bg: "#3C3E40", gradient_to: "#303233", radius: "2px", padding: "15px 32px" }
  dui-btn-buy: { bg: "#1E9DF7", gradient_to: "#1392ED", radius: "2px", padding: "15px 32px" }
  store-pill: { bg: "#0070D5", radius: "999px", padding: "8px 16px" }
---

# DESIGN.md — DJI

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

DJI의 웹사이트는 전자제품 쇼핑몰이라기보다 실내 비행 테스트장과 제품 발표 무대 사이에 있다. 첫 화면은 넓은 하늘색 표면 위에 제품 오브젝트를 띄우고, 내비게이션과 카피는 그 위를 방해하지 않는 얇은 조종석 계기판처럼 앉는다. 배경은 #F7F9FA(`{colors.dui-home-ice}`)에 가까운 차갑고 밝은 공기층이며, 검정 텍스트는 순흑보다 #303233(`{colors.dui-text-carbon}`) 계열로 낮춰져 있다. 순백 갤러리가 아니라, 드론이 이륙하기 직전의 밝은 격납고 공기다.

시그니처는 색상이 아니라 거리감이다. 히어로의 제품 이미지는 화면 중앙에서 넓은 빈 공간을 차지하고, 텍스트는 제품보다 앞서지 않는다. "More Than Sound" 같은 제목은 크지만 과장된 editorial display는 아니며, Open Sans의 안정적인 굵기로 제품을 설명하는 도구 역할을 한다. 제품 사진은 카드 안에 놓이지 않고 활주로 위에 떠 있는 기체처럼 다뤄진다. 사이트라는 자의식이 작다 — 페이지는 자기 장식을 지우고 렌더된 제품이 공중에 머무를 시간을 준다.

컬러 시스템은 거의 monochrome 기반이다. 구매 행동만 #1E9DF7 -> #1392ED(`{colors.dui-buy-blue-start}` to `{colors.dui-buy-blue-end}`)의 선명한 파랑으로 튀어나오고, 일반 CTA는 #3C3E40 -> #303233의 검은 금속성 그라디언트를 쓴다. 이 파랑은 하늘 전체가 아니라 계기판의 활성 표시등이다. no second brand color: 로고나 hero artwork의 다채로운 색은 브랜드 팔레트가 아니라 캠페인 소재이며, UI chrome 자체는 훨씬 조용하다.

공간은 Apple식 초미니멀과 다르다. DJI는 완전한 white gallery가 아니라 제품 라인업, 배너, 서비스 모듈을 계속 이어 붙이는 상업적 리듬을 갖는다. 다만 각 모듈이 충분히 큰 이미지와 넓은 상단 여백을 갖기 때문에 사이트 전체가 빽빽한 커머스로 보이지 않는다. `section.homepage-banner .banner-content`의 112px top padding과 800px background-size는 "제품을 먼저 띄우고, UI는 뒤로 물러난다"는 규칙을 만든다. shadow only on navigation: 드롭다운이 열릴 때만 깊이가 생기고, 제품 모듈은 그림자 대신 공기와 스케일로 떠 있는 느낌을 만든다.

모션도 장난감처럼 튀지 않는다. opacity와 transform의 0.6s reveal은 제품 런칭 영상의 컷 전환에 가깝다. Swiper는 쇼핑몰 배너 회전이 아니라 격납고에서 다음 기체가 조용히 앞으로 미끄러져 나오는 장면처럼 작동한다. DJI다움은 큰 효과 하나가 아니라, `{colors.dui-home-ice}`의 공기층, `{colors.dui-text-carbon}`의 낮은 검정, 2px control radius, 그리고 구매 순간에만 켜지는 `{colors.dui-buy-blue-start}`가 함께 만드는 정밀한 비행 전 점검표에 있다.

### Key Characteristics

- Product-first hero: 800px급 배경 이미지와 중앙 정렬 카피가 첫 인상을 만든다.
- Cool bright surfaces: #F7F9FA, #EDEDED, #FFFFFF가 사진과 3D 렌더를 받치는 밝은 공기층이다.
- Carbon text, not pure black: 본문과 UI 텍스트는 #303233/#3B3E40/#535759 계열을 반복한다.
- Blue only for purchase/action: #1E9DF7, #1392ED, #0070D5는 store/buy/focus에 제한된다.
- Selector-level system: CSS 변수나 토큰 계층 대신 `.dui-btn`, `.homepage-banner`, `.dui-navbar` 같은 클래스가 시스템 역할을 한다.
- Small-radius controls: 기본 버튼은 2px radius, store pill만 999px 계열로 분리된다.
- Header as instrument panel: 상단 nav는 48-64px 높이의 얇은 조작면이며, hero 위에서 제품을 가리지 않는다.
- Motion is reveal-based: opacity/transform 0.6s와 Swiper 전환이 제품 슬라이드를 다룬다.
- Shadows are scoped: dropdown과 overlay에만 shadow가 있고, homepage product tiles는 `box-shadow:none`에 가깝다.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Airborne Minimalism
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **공중에 띄운 제품 오브젝트와 얇은 계기판형 내비게이션**으로 기억된다.
> **Code Complexity**: high — Swiper, large responsive hero modules, selector-level nav/dropdown states, staged opacity/transform transitions are present without a custom-property token layer.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 DJI처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Open Sans", "PingFang SC", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #F7F9FA; --fg: #303233; }
body { background: var(--bg); color: var(--fg); }

/* 3. 구매 액션만 파랑 */
:root { --buy: #1E9DF7; --buy-to: #1392ED; }
.buy { background: linear-gradient(-180deg, var(--buy) 0%, var(--buy-to) 100%); }
```

**절대 하지 말아야 할 것 하나**: 모든 CTA와 링크를 DJI blue로 칠하지 말 것. DJI의 UI는 대부분 carbon/white이고, 파랑은 구매·스토어·focus ring 같은 높은 의도에만 등장한다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.dji.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | reused `insane-design/dji` phase1 assets |
| HTML size | 149008 bytes |
| CSS files | 3 external files, approx. 293053 chars |
| Token prefix | `dui` |
| Method | existing CSS/HTML/screenshot + phase1 JSON interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: server-rendered marketing site with SSI-style partials and CDN-hosted CSS/JS.
- **Design system**: DUI selector library, not tokenized CSS variables.
- **CSS architecture**:
  ```text
  v3.base.min.css        base grid, buttons, font-face, shared DUI primitives
  www.header-v4.min.css  navbar, dropdown, search, store pill, global header states
  www.homepage.min.css   homepage hero, product banners, story modules, responsive overrides
  ```
- **Class naming**: `.dui-*` shared primitives plus `homepage-*` module classes and `navbar-*` header classes.
- **Default theme**: light, with hero module `theme-dark` meaning dark text on light image.
- **Font loading**: CDN-hosted Open Sans woff2 preload; icon fonts include `Dji` and FontAwesome.
- **Canonical anchor**: the homepage hero uses `section.homepage-banner .banner-content` as the visual grammar source.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Open Sans` via DJI CDN.
- **Icon font**: `Dji` for brand/icon glyphs, plus `FontAwesome`.
- **Weight normal / bold**: `400` / `600`, with observed 300, 500, 700, 800 in supporting text and campaign modules.

```css
:root {
  --dui-font-family: "Open Sans", "PingFang SC", "Microsoft YaHei",
                     "Helvetica Neue", "Hiragino Sans GB",
                     "WenQuanYi Micro Hei", Arial, sans-serif;
  --dui-font-family-icon: "Dji";
  --dui-font-weight-normal: 400;
  --dui-font-weight-bold: 600;
}
body {
  font-family: var(--dui-font-family);
  font-weight: var(--dui-font-weight-normal);
}
```

### Note on Font Substitutes

- **Open Sans** is the safest substitute target because the site already ships it. If the CDN font is unavailable, use the local/system Open Sans first, then Arial.
- **Korean fallback** should stay in the order shown by CSS: `PingFang SC`, `Microsoft YaHei`, `Helvetica Neue`, `Hiragino Sans GB`, `WenQuanYi Micro Hei`, Arial. Do not replace this with a purely Korean display face; DJI's interface tone depends on global sans neutrality.
- **Display correction**: if using Inter instead of Open Sans, reduce hero title weight from 700 to 650/600 and keep letter-spacing at 0. Inter at 700 becomes more startup-SaaS than DJI.
- **CTA correction**: keep CTA text at 16px/600. Raising it to 700 makes the small 2px-radius buttons feel heavier than DJI's original controls.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| Hero title | 40px observed in screenshot | 700 | ~1.2 | 0 |
| Hero date/subtitle | 16px | 600 | ~1.4 | 0 |
| CTA button | 16px | 600 | 16px in `.dui-btn` | 0 |
| Learn more link | 16px | 600 | 46px | 0 |
| Nav link | 14px | 400 | compact | 0 |
| Small button | 14px | 400/500 | 14px in `.dui-btn-sm` | 0 |

> ⚠️ Key insight: DJI does not use expressive typography to carry brand emotion. The product image carries the emotion; type is a precision label.

### Principles

1. Hero type is large enough to announce, not large enough to dominate. Product imagery must remain the biggest visual object.
2. Letter-spacing stays neutral. Do not add luxury-style negative tracking unless a specific campaign image requires it.
3. Weight 600 is the operational emphasis weight for CTAs and learn-more links; 700+ appears in title moments, not in nav chrome.
4. The same sans stack spans product marketing and utility UI. Visual hierarchy comes from spacing, module scale, and image size.
5. Icon fonts are part of the typography system. The `Dji` icon font should be treated as a brand glyph source, not replaced with generic outline icons.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand / Action Ramp

| Token | Hex |
|---|---|
| `dui-buy-blue-start` | `#1E9DF7` |
| `dui-buy-blue-end` | `#1392ED` |
| `dui-buy-blue-hover` | `#4CB5FF` |
| `dui-store-blue` | `#0070D5` |
| `dui-store-blue-hover` | `#2490E3` |
| `dui-store-blue-pressed` | `#0058B0` |

### 06-2. Brand Dark Variant

> N/A — no dark theme token ramp was found. Dark behavior is selector/theme based rather than a complete palette.

### 06-3. Neutral Ramp

| Step | Light | Dark/Text |
|---|---|---|
| page/surface | `#FFFFFF` | `#303233` |
| homepage ice | `#F7F9FA` | `#3B3E40` |
| module gray | `#EDEDED` | `#535759` |
| divider | `#F0F1F2` | `#6C7073` |
| disabled/rail | `#C2C8CC` | `#919699` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Store / focus blue | primary | `#1890FF` |
| Buy CTA blue | start | `#1E9DF7` |
| Regional activity orange | campaign only | `#FA8C16` |
| Campaign artwork chroma | asset only | `#BBAACC` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `dui.action.buy` | `#1E9DF7` | Buy button gradient start |
| `dui.action.buy-end` | `#1392ED` | Buy button gradient end |
| `dui.action.store` | `#0070D5` | Store pill / header action |
| `dui.text.primary` | `#303233` | Main body, dark text hero |
| `dui.text.secondary` | `#6C7073` | Secondary nav/content text |
| `dui.surface.base` | `#FFFFFF` | Header/dropdown/base surface |
| `dui.surface.product` | `#F7F9FA` | Homepage product atmosphere |
| `dui.border.soft` | `#F0F1F2` | Header/dropdown separators |

### 06-6. Semantic Alias Layer

> N/A — phase1 found 0 CSS custom properties and 0 alias tiers. These semantic names are guidebook labels for actual CSS values, not discovered `var()` aliases.

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency / role |
|---|---|---|
| surface white | `#FFFFFF` | 89, neutral |
| carbon end | `#303233` | 16, neutral |
| black | `#000000` | 9, neutral |
| focus blue | `#1890FF` | 8, chromatic |
| header carbon | `#3B3E40` | 6, neutral |
| muted gray | `#6C7073` | 6, neutral |
| secondary gray | `#919699` | 6, neutral |
| hairline | `#F0F1F2` | 4, neutral |

### 06-8. Color Stories

**`dui-buy-blue-start` (`#1E9DF7`)** — The real action blue. It belongs to purchase and high-intent action, not general decoration. Use it as a gradient start with `#1392ED`, not as a flat brand wash.

**`dui-surface-white` (`#FFFFFF`)** — Header, dropdown, and base chrome surface. DJI uses white as an instrument-panel material: clean, thin, and secondary to the product image.

**`dui-text-carbon` (`#303233`)** — The default dark UI voice. It avoids the brittle contrast of pure black while keeping technical precision.

**`dui-home-ice` (`#F7F9FA`)** — The homepage product atmosphere. This pale cool surface lets renderings feel airborne; replacing it with flat white loses the "sky studio" effect.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `hero-top-air` | `112px` | `section.homepage-banner .banner-content` top padding |
| `compact-header` | `48px` | responsive `#site-header` height under 1300px |
| `desktop-dropdown-top` | `64px` | nav dropdown/mask top offset |
| `banner-card-padding-top` | `48px` | product banner text block |
| `module-gap-large` | `64px` | max-height responsive module spacing |
| `button-x` | `32px` | `.dui-btn` horizontal padding |
| `small-button-x` | `16px` | `.dui-btn-sm` horizontal padding |

**주요 alias**:
- `hero-top-air` -> 112px: product image has room before the title and controls.
- `module-gap-large` -> 64px: repeated commercial modules breathe without becoming editorial blankness.

### Whitespace Philosophy

DJI's whitespace is not an empty gallery. It is launch-stage air: enough room above and around the product render for motion, glow, and shadow to read. The hero text starts high, but the central object occupies the real visual center.

Below the hero, spacing becomes more commercial. Product banners and service modules compress into repeatable blocks with 48-64px text offsets and flexible two-column grids. The shift is intentional: open announcement first, browsable product ecosystem second.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `dui-radius-control` | `2px` | `.dui-btn` primary and buy buttons |
| `dui-radius-field` | `4px` | header/search/dropdown controls |
| `dui-radius-card` | `8px` | dropdown/card surfaces |
| `dui-radius-media` | `10px` | homepage media module detail |
| `dui-radius-pill` | `100px` / `999px` | store pill, rounded utility controls |
| `dui-radius-round` | `50%` / `100%` | circular buttons, swiper controls |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| Dropdown heavy | `0 16px 16px rgba(0,0,0,.1)` | main nav menu wrapper |
| Dropdown medium | `0 8px 16px rgba(0,0,0,.1)` | secondary menu surfaces |
| Popover | `0 2px 8px rgba(0,0,0,.2)` | floating header UI |
| Low card | `0 2px 4px 0 rgba(0,0,0,.05)` | subtle utility surfaces |
| Focus ring | `#1890ff 0 0 0 3px` / `0 0 0 4px rgba(24,144,255,.2)` | form/control focus |
| Homepage product modules | `none` | product imagery should carry depth |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `dui-control-transition` | `all .3s ease` | buttons, nav controls |
| `dui-bg-transition` | `background-color .3s ease` / `.4s` | nav and swiper hover |
| `dui-dropdown-transition` | `all .3s ease!important` | header menu open/close |
| `homepage-reveal` | `opacity .6s linear, transform .6s cubic-bezier(.215,.61,.355,1)` | staggered homepage reveal |
| `homepage-reveal-delay` | `.1s` to `.3s` delays | sequential content entrance |
| `long-pan` | `transform 6s linear` | product/background motion moments |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: 1200px in `.dui-navbar .row .container`; homepage modules use full-width sections with inner text max-widths.
- **Grid type**: flexbox for product banner lists and navbar; Swiper for hero carousel.
- **Column count**: 12-column base grid in shared CSS; homepage product banners collapse into two-up cards where available.
- **Gutter**: 16px page/product banner padding; 8px grid cell side padding in header grid.

### Hero

- **Pattern Summary**: 800px full-width product image stage + centered H1/date + small outline CTA + left slide index.
- Layout: one-column centered text layered above full-width background/product render.
- Background: cool pale image surface, often close to `#F7F9FA` or `#EDEDED`.
- **Background Treatment**: image-overlay/product-render; CSS uses `background-position:center center`, `background-repeat:no-repeat`, `background-size:auto 800px`, `background-color:#ededed`.
- H1: approx. `40px` / weight `700` / tracking `0`.
- Max-width: visual asset fills viewport; text block stays centered and compact.

### Section Rhythm

```css
section.homepage-banner .banner-content {
  padding-top: 112px;
  text-align: center;
  background-position: center center;
  background-size: auto 800px;
}
section.homepage-products-banner {
  padding: 0 16px;
}
```

### Card Patterns

- **Card background**: mostly image-backed surfaces with `#FFFFFF`, `#F7F9FA`, or `#EDEDED`.
- **Card border**: minimal; structure comes from image boundaries and spacing.
- **Card radius**: 0 for full-bleed hero, 8-10px for certain cards/dropdowns.
- **Card padding**: product banner text starts at 48px top, inner max-width around 520px.
- **Card shadow**: homepage cards avoid shadow; nav/dropdowns use shadow.

### Navigation Structure

- **Type**: horizontal desktop nav with category dropdowns, icons, region selector, account icon, store pill.
- **Position**: header overlays/occupies top region; dropdowns absolute from 64px.
- **Height**: 64px desktop grammar, 48px under 1300px responsive rule.
- **Background**: white/light translucent impression over hero, with collapsed and theme-dark variants.
- **Border**: subtle or absent; dropdown depth uses shadow and white surface.

### Content Width

- **Prose max-width**: hero copy remains narrow, product banner text max-width 520px.
- **Container max-width**: 1200px for header container.
- **Sidebar width**: not a homepage pattern; dropdown mega-menu uses full-width overlay.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `max-width: 767px` | header/mobile dropdown branch appears in header CSS |
| Tablet | `min-width: 768px` | desktop-ish header/menu behavior starts |
| Desktop compact | `max-width: 1300px` | header height becomes 48px; navbar container shrinks |
| Product banner narrow | `max-width: 1230px` | homepage product banner items force 591px width |
| Large desktop adjustment | `max-width: 1600px` / `1334px` | header/product menu refinements |
| Short viewport | `max-height: 900px` | hero/module heights reduce to 696px / 576px |

### Touch Targets

- **Minimum tap size**: primary button height 46px, small button 30px.
- **Button height (mobile)**: not fully measured; base `.dui-btn` remains 46px.
- **Input height (mobile)**: not surfaced in homepage capture.

### Collapsing Strategy

- **Navigation**: desktop horizontal categories move into compact 48px header rules under 1300px; mobile branch exists at 767px.
- **Grid columns**: product banners use flex-wrap and fixed-width adjustments around 1230px.
- **Sidebar**: no persistent sidebar on homepage.
- **Hero layout**: keeps centered hero grammar; height/background-size adjusts for short screens.

### Image Behavior

- **Strategy**: background image as product stage, not inline responsive `<img>` for hero.
- **Max-width**: full viewport section; background-size `auto 800px` / `auto 696px`.
- **Aspect ratio handling**: controlled by section height and background-size, not CSS `aspect-ratio`.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**`.dui-btn` base**

```html
<a class="dui-btn dui-btn-primary">더 알아보기</a>
```

| Spec | Value |
|---|---|
| Display | inline-block |
| Height | 46px |
| Font | 16px / 600-ish usage, 16px line-height |
| Padding | 15px 32px |
| Radius | 2px |
| Transition | all .3s ease |
| Hover | color stays #FFFFFF, background gradient may lighten |

**`.dui-btn-buy`**

```css
.dui-btn-buy {
  background: #1E9DF7;
  background-image: linear-gradient(-180deg, #1E9DF7 0%, #1392ED 100%);
}
.dui-btn-buy:hover {
  background-image: linear-gradient(-180deg, #4CB5FF 0%, #1392ED 100%);
}
```

States observed: hover/active for color and gradient; focus ring appears elsewhere in header/form CSS as #1890FF rings.

### Badges

> N/A — no homepage badge system was clearly surfaced in the captured CSS/HTML. Do not invent promotional chips unless a campaign module provides one.

### Cards & Containers

**Homepage product banner item**

```html
<li class="products-banner-item">
  <div class="products-banner-text theme-dark">
    <div class="subhead">Product title</div>
    <a class="link-box"><span class="text">더 알아보기</span></a>
  </div>
</li>
```

| Spec | Value |
|---|---|
| Layout | flex-wrap list, two-up where width allows |
| Text block | max-width 520px, padding-top 48px |
| Surface | image-backed, white/ice/gray |
| Border | none by default |
| Shadow | none for homepage product modules |
| Hover | full-card link overlay, not card lift |

### Navigation

**Header category**

```html
<nav id="site-header" class="dui-navbar site-header collapsed">
  <ul class="navbar-category">
    <li class="category-item">
      <a class="nav-item-title font-opensans">카메라 드론</a>
      <div class="dui-dropdown-menu"></div>
    </li>
  </ul>
</nav>
```

| Spec | Value |
|---|---|
| Desktop height | 64px grammar, 48px compact rule |
| Container | max-width 1200px / calc(100% - 48px) in compact state |
| Dropdown top | 64px |
| Dropdown shadow | 0 16px 16px rgba(0,0,0,.1) |
| Dropdown background | #FFFFFF |
| Mask | rgba(0,0,0,.6) full viewport |

### Inputs & Forms

Search and subscription/form surfaces are present, but homepage capture does not expose full field markup. Focus ring colors are visible in CSS:

```css
box-shadow: #1890FF 0 0 0 3px !important;
box-shadow: 0 0 0 4px rgba(24,144,255,.2);
```

Use 4px radius, #FFFFFF surface, and #F0F1F2/#EBEFF2 hairlines for fields.

### Hero Section

```html
<section class="homepage-banner homepage-big-banner">
  <div class="banner-content theme-dark">
    <h2 class="banner-title">More Than Sound</h2>
    <div class="banner-time">2026년 4월 28일 | 오후 9시(KST)</div>
    <a class="banner-button">더 알아보기</a>
  </div>
</section>
```

| Spec | Value |
|---|---|
| Background | centered no-repeat product render |
| Background size | auto 800px |
| Top padding | 112px |
| Alignment | centered |
| CTA | outline pill in hero, stronger blue for store/buy elsewhere |
| Slide support | Swiper with left index and product list |

### 13-2. Named Variants

**`dui-btn-primary`**

- Background: `linear-gradient(-180deg, #3C3E40 0%, #303233 100%)`
- Hover: `linear-gradient(-180deg, #545759 0%, #303233 100%)`
- Use: general dark action where buy intent is not explicit.

**`dui-btn-buy`**

- Background: `linear-gradient(-180deg, #1E9DF7 0%, #1392ED 100%)`
- Hover: `linear-gradient(-180deg, #4CB5FF 0%, #1392ED 100%)`
- Use: purchase or high-intent commerce action only.

**`dui-learn-more`**

- Text color: `#303233`
- Height/line-height: 46px
- Weight: 600
- Hover: `#616466`
- Use: lower-commitment product exploration link.

**`store-pill`**

- Background: `#0070D5` family
- Radius: 999px / 100px family
- Use: header store entry; visually distinct from squared DUI buttons.

### 13-3. Signature Micro-Specs

```yaml
airborne-product-stage:
  description: "The homepage hero turns product imagery into an airborne centerpiece instead of a card object."
  technique: "background-position:center center; background-repeat:no-repeat; background-size:auto 800px; background-color:#EDEDED; padding-top:112px"
  applied_to: ["section.homepage-banner .banner-content"]
  visual_signature: "A drone or camera product appears suspended in pale launch-stage air, with UI chrome kept behind the object."

carbon-gradient-control:
  description: "Primary non-buy buttons read as small graphite hardware controls."
  technique: "linear-gradient(-180deg, #3C3E40 0%, #303233 100%); hover linear-gradient(-180deg, #545759 0%, #303233 100%); border-radius:2px; padding:15px 32px"
  applied_to: [".dui-btn-primary", ".dui-btn-normal"]
  visual_signature: "The CTA feels like a precise equipment button, not a rounded SaaS pill."

buy-blue-activation-gradient:
  description: "Purchase intent is isolated into one high-saturation blue activation state."
  technique: "linear-gradient(-180deg, #1E9DF7 0%, #1392ED 100%); hover linear-gradient(-180deg, #4CB5FF 0%, #1392ED 100%)"
  applied_to: [".dui-btn-buy"]
  visual_signature: "The buy action lights up like the only active indicator on an otherwise neutral flight panel."

dropdown-depth-only:
  description: "Elevation belongs to navigation overlays, while product modules stay flat and image-led."
  technique: "box-shadow:0 16px 16px rgba(0,0,0,.1) and 0 8px 16px rgba(0,0,0,.1); mask rgba(0,0,0,.6)"
  applied_to: [".dui-navbar .nav-menu-wrapper", ".dui-dropdown-menu"]
  visual_signature: "Depth appears only when the header opens; homepage product tiles keep their clean launch-stage surface."

staged-product-reveal:
  description: "Homepage motion uses measured launch timing instead of bounce or decorative play."
  technique: "transition:opacity .6s linear, transform .6s cubic-bezier(.215,.61,.355,1); transition-delay:.1s/.2s/.3s"
  applied_to: ["homepage reveal elements", "Swiper-supported homepage modules"]
  visual_signature: "Content enters like a product reveal sequence, with controlled fade and glide rather than elastic motion."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Short product/event statement, often in English even on Korean page | "More Than Sound" |
| Date/subtitle | Precise launch information | "2026년 4월 28일 \| 오후 9시(KST)" |
| Primary CTA | Plain utility phrase | "더 알아보기" |
| Store CTA | Direct commerce command | "스토어", "앱 다운로드" |
| Tone | Technical, calm, product-led | Features are named through product families: Mavic, Osmo, Ronin |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* DJI — copy into your root stylesheet */
:root {
  /* Fonts */
  --dui-font-family: "Open Sans", "PingFang SC", "Microsoft YaHei",
                     "Helvetica Neue", "Hiragino Sans GB",
                     "WenQuanYi Micro Hei", Arial, sans-serif;
  --dui-font-family-icon: "Dji";
  --dui-font-weight-normal: 400;
  --dui-font-weight-bold: 600;

  /* Action colors */
  --dui-color-buy-start: #1E9DF7;
  --dui-color-buy-end: #1392ED;
  --dui-color-buy-hover: #4CB5FF;
  --dui-color-store: #0070D5;

  /* Surfaces */
  --dui-bg-page: #FFFFFF;
  --dui-bg-product: #F7F9FA;
  --dui-bg-module: #EDEDED;
  --dui-text: #303233;
  --dui-text-muted: #6C7073;
  --dui-border-soft: #F0F1F2;

  /* Key spacing */
  --dui-space-hero-top: 112px;
  --dui-space-module: 64px;
  --dui-space-card-text-top: 48px;

  /* Radius */
  --dui-radius-control: 2px;
  --dui-radius-field: 4px;
  --dui-radius-card: 8px;
  --dui-radius-pill: 999px;
}

body {
  font-family: var(--dui-font-family);
  color: var(--dui-text);
  background: var(--dui-bg-page);
}

.dui-stage {
  min-height: 800px;
  padding-top: var(--dui-space-hero-top);
  text-align: center;
  background: var(--dui-bg-product) center / auto 800px no-repeat;
}

.dui-btn {
  display: inline-block;
  height: 46px;
  padding: 15px 32px;
  border: 0;
  border-radius: var(--dui-radius-control);
  color: #FFFFFF;
  font-size: 16px;
  line-height: 16px;
  cursor: pointer;
  transition: all .3s ease;
}

.dui-btn-primary {
  background: #3C3E40;
  background-image: linear-gradient(-180deg, #3C3E40 0%, #303233 100%);
}

.dui-btn-buy {
  background: var(--dui-color-buy-start);
  background-image: linear-gradient(-180deg, #1E9DF7 0%, #1392ED 100%);
}

.dui-btn-buy:hover {
  background-image: linear-gradient(-180deg, #4CB5FF 0%, #1392ED 100%);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — DJI-inspired values
module.exports = {
  theme: {
    extend: {
      colors: {
        dji: {
          buy: '#1E9DF7',
          buyEnd: '#1392ED',
          store: '#0070D5',
          carbon: '#303233',
          muted: '#6C7073',
          ice: '#F7F9FA',
          module: '#EDEDED',
          hairline: '#F0F1F2',
        },
      },
      fontFamily: {
        sans: ['Open Sans', 'PingFang SC', 'Microsoft YaHei', 'Arial', 'sans-serif'],
      },
      borderRadius: {
        dji: '2px',
        'dji-card': '8px',
        'dji-pill': '999px',
      },
      boxShadow: {
        'dji-dropdown': '0 16px 16px rgba(0,0,0,.1)',
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
| Brand/action primary | `dui-buy-blue-start` | `#1E9DF7` |
| Buy gradient end | `dui-buy-blue-end` | `#1392ED` |
| Header store | `dui-store-blue` | `#0070D5` |
| Background | `dui-surface-white` | `#FFFFFF` |
| Product atmosphere | `dui-home-ice` | `#F7F9FA` |
| Text primary | `dui-text-carbon` | `#303233` |
| Text muted | `dui-muted` | `#6C7073` |
| Border | `dui-hairline` | `#F0F1F2` |

### Example Component Prompts

#### Hero Section

```text
DJI 스타일 히어로 섹션을 만들어줘.
- 배경: #F7F9FA 또는 #EDEDED 위에 중앙 product render를 크게 배치
- H1: Open Sans, 약 40px, weight 700, tracking 0, color #303233
- 서브텍스트: 16px, weight 600, color #303233
- CTA: 얇은 outline pill 또는 낮은 위계의 learn-more
- 제품 이미지가 텍스트보다 더 큰 시각 중심이 되게 할 것
```

#### Card Component

```text
DJI 스타일 제품 배너 카드를 만들어줘.
- 배경은 이미지 중심, UI surface는 #FFFFFF/#F7F9FA/#EDEDED 중 하나
- 텍스트 블록은 max-width 520px, padding-top 48px, 중앙 정렬
- card shadow는 쓰지 말고 이미지/공간으로 깊이를 만들 것
- 링크는 #303233 텍스트 + angle icon, hover는 #616466 정도로만
```

#### Badge

```text
DJI에는 강한 badge 시스템이 없으므로 꼭 필요할 때만 작은 neutral label을 만들어줘.
- bg #F0F1F2, color #535759
- radius 100px
- font Open Sans 12px/500
- blue badge를 남발하지 말 것
```

#### Navigation

```text
DJI 스타일 상단 네비게이션을 만들어줘.
- 높이 64px 데스크톱, compact에서는 48px
- 배경 #FFFFFF 또는 hero 위의 밝은 translucent 느낌
- 링크는 Open Sans 14px/400, color #303233
- 우측 store 버튼만 #0070D5 pill
- dropdown은 #FFFFFF + box-shadow 0 16px 16px rgba(0,0,0,.1)
```

### Iteration Guide

- **색상 변경 시**: #1E9DF7/#1392ED는 buy action에만 사용한다. 일반 링크와 nav를 모두 파랗게 만들지 않는다.
- **폰트 변경 시**: Open Sans의 기계적 중립성을 유지한다. Pretendard나 Inter를 쓸 경우 weight를 낮춰 과도한 SaaS 느낌을 줄인다.
- **여백 조정 시**: hero top air 112px, module gap 64px, product text top 48px의 세 리듬을 우선 보존한다.
- **새 컴포넌트 추가 시**: 2px control radius와 8px dropdown/card radius를 분리한다.
- **모션 추가 시**: bounce/spring보다 opacity + transform 0.6s launch reveal을 쓴다.
- **이미지 배치 시**: product render를 카드 안에 가두지 말고 넓은 pale surface 위에 띄운다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- 제품 이미지가 첫 시각 중심이 되도록 hero를 구성한다.
- 대부분의 UI chrome은 #FFFFFF, #F7F9FA, #EDEDED, #303233, #6C7073 계열로 유지한다.
- 구매 CTA에는 #1E9DF7 -> #1392ED 그라디언트를 사용한다.
- 일반 CTA는 #3C3E40 -> #303233 carbon gradient 또는 outline/learn-more 형태로 둔다.
- header/dropdown shadow는 허용하되 homepage product module shadow는 억제한다.
- Open Sans와 동아시아 fallback stack을 유지한다.
- Swiper/reveal motion은 opacity와 transform 중심으로 차분하게 만든다.

### ❌ DON'T

- 배경을 `#FFFFFF`만으로 평평하게 두지 말 것 — hero/product atmosphere에는 `#F7F9FA` 또는 `#EDEDED` 사용.
- 텍스트를 `#000000` 또는 `black`으로 과하게 세우지 말 것 — 기본 UI 텍스트는 `#303233` 사용.
- 모든 primary action을 `#0070D5`로 통일하지 말 것 — 구매 CTA는 `#1E9DF7` -> `#1392ED`, header store는 `#0070D5`.
- hover blue를 `#1890FF`로 무조건 덮지 말 것 — buy hover는 `#4CB5FF` -> `#1392ED` 패턴.
- 버튼 radius를 `999px`로 전부 pill 처리하지 말 것 — 기본 `.dui-btn`은 `2px`, store pill만 `999px` 계열.
- product card에 `box-shadow: 0 16px 16px rgba(0,0,0,.1)`를 넣지 말 것 — 이 shadow는 dropdown chrome용이다.
- body를 `font-weight: 300`으로 두지 말 것 — 기본 본문은 `400`, CTA/learn-more는 `600`.
- hero background-size를 작은 cover thumbnail처럼 만들지 말 것 — DJI hero는 `auto 800px`급 product stage가 필요하다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- No full brand rainbow in UI chrome. Campaign imagery can be colorful, but controls remain neutral/blue.
- No second persistent brand color. Orange `#FA8C16` appears as campaign/regional activity, not a system accent.
- No heavy editorial serif. Typography stays global sans, technical, and quiet.
- No soft SaaS cards with large rounded corners. Radius is small for controls and restrained for cards.
- No universal pill language. Pills are reserved for store/utility moments.
- No decorative border-left accent cards. Structure comes from product modules, image scale, and spacing.
- No broad page-level gradient background. Gradients are control-level, not page atmosphere.
- No product module elevation stack. Shadows belong to overlays/dropdowns, not every tile.
- No playful bounce motion. Motion is reveal, carousel, fade, and controlled transform.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-only evidence**: this guide is based on the reused `insane-design/dji` homepage capture, not product detail, checkout, support, account, or repair flows.
- **No custom-property token layer**: phase1 found `total_vars: 0`, so semantic token names in this document are guidebook labels mapped to real CSS values, not discovered CSS variable names.
- **Korean locale capture**: HTML points to `https://www.dji.com/kr` metadata and Korean nav/copy. Other locales may change campaign modules, product ordering, or store CTA treatment.
- **Hero campaign volatility**: screenshot shows "More Than Sound" and a dated launch hero. DJI frequently rotates campaign imagery; the underlying stage grammar matters more than this one asset.
- **Mobile visual QA not performed here**: CSS breakpoints were read, but no fresh mobile screenshot was captured in this turn.
- **Form states incomplete**: focus/error ring colors appear in CSS, but real form validation, loading, and disabled markup were not exercised.
- **JS behavior not deeply traced**: Swiper/reveal transitions are visible in CSS, but JavaScript timing and scroll-trigger logic were not audited.
- **Logo/artwork color filtering**: chromatic values from campaign images or embedded assets may appear in frequency candidates; UI color decisions intentionally prioritize selectors and controls.
- **Exact typography sizes limited**: phase1 typography scale returned no structured scale entries, so hero/nav/CTA sizes combine CSS snippets and screenshot observation.
