---
schema_version: 3.2
slug: kia
service_name: Kia Korea
site_url: https://www.kia.com/kr/
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#05141F"
primary_font: "Kia Signature"
font_weight_normal: 400
token_prefix: kia

bold_direction: Automotive Editorial
aesthetic_category: editorial-product
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: automotive
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "AEM page with Kia Signature font families, reusable button/header/key-visual components, 31 CSS variables, and consistent neutral-first component rules."

colors:
  ink-primary: "#05141F"
  ink-secondary: "#37434B"
  text-muted: "#697278"
  surface-base: "#fff"
  surface-soft: "#F8F8F8"
  hairline: "#DADBDC"
  disabled: "#9FA5A9"
  focus: "#000"
  utility-blue: "#005CB2"
  utility-red: "#EA0029"

typography:
  display: "Kia Signature Bold"
  body: "Kia Signature Regular"
  light: "Kia Signature Light"
  ladder:
    - { token: hero-title, size: "52px", weight: 400, line_height: "1.23", tracking: "normal" }
    - { token: hero-title-mobile, size: "34px", weight: 400, line_height: "1.29", tracking: "normal" }
    - { token: hero-pretitle, size: "18px", weight: 400, line_height: "1.67", tracking: "normal" }
    - { token: body, size: "16px", weight: 400, line_height: "1.43", tracking: "normal" }
    - { token: button, size: "14px", weight: 400, line_height: "1", tracking: "normal" }
  weights_used: [300, 400, 700]
  weights_absent: [500, 600, 800, 900]

components:
  button-primary: { bg: "{colors.ink-primary}", fg: "{colors.surface-base}", border: "{colors.ink-primary}", radius: "0", padding: "16px 24px" }
  button-secondary: { bg: "{colors.surface-base}", fg: "{colors.ink-primary}", border: "{colors.disabled}", radius: "0", padding: "16px 24px" }
  hero-visual: { height: "100vh", media: "full-bleed object-fit cover", content_grid: "9.5fr 2fr 1.25fr / 140px 1fr 130px" }
  quick-link-card: { bg: "{colors.surface-soft}", hover_bg: "{colors.ink-primary}", radius: "0", padding: "24px", transition: "all .4s" }
---

# DESIGN.md - Kia Korea

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Kia Korea stages each vehicle like a **showroom** hero with the walls removed. The first viewport is a 100vh photography bay: the car occupies every pixel of depth while the navigation and copy reduce themselves to white labels etched on glass — caption plates in a **gallery** room rather than an application shell. `#05141F` (`{colors.ink-primary}`) functions less like a brand swatch than a panel of blackened metal riveted over the photograph.

The **showroom** logic extends to every interaction. Buttons are squared with zero radius, hover states wipe in horizontally over 0.4 seconds like a mechanical shutter passing across a **cockpit** instrument placard. Quick-link cards below the fold operate as the service counter after the **gallery** room: `#F8F8F8` (`{colors.surface-soft}`) slabs that invert to `#05141F` (`{colors.ink-primary}`) only on touch. Carousel dots are small rings rather than loud indicators, behaving like the fine-pitch alignment marks on a precision instrument.

The negative identity is the architecture. Kia Korea carries no rainbow EV palette, no luxury serif drama, no rounded consumer-app softness. `Kia Signature Bold/Regular/Light` are mapped to CSS `font-weight: 400`, so hierarchy moves through family choice and size rather than numeric weight ladders — a custom type system that acts as a **cockpit** labeling standard rather than a consumer display typeface. There is no second brand color. Utility-blue `#005CB2` and utility-red `#EA0029` stay in service roles only. The **showroom** floor stays dark and clear so the vehicle can be the exhibit, and the UI chrome withdraws to become the small caption plate beside it.

### Key Characteristics

- Full-viewport automotive photography is the first design token.
- #05141F (`{colors.ink-primary}`) carries primary CTA, body text, dark hover, and structural identity.
- White nav and hero copy float directly over photography; no opaque nav bar in the first viewport.
- Buttons are square-edged rectangles with a left-to-right `:after` wipe hover.
- Kia Signature font families replace numeric weight hierarchy.
- Display tracking remains `normal`; the system avoids fashionable tight letter-spacing.
- Hero content is low-left and grid-positioned, not center-marketing copy.
- Carousel pagination uses small white ring dots with filled active state.
- Cards below the fold use #F8F8F8 (`{colors.surface-soft}`) and invert to #05141F on hover.
- Motion is functional and linear: slide-in text, hover wipe, icon swap.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Automotive Editorial
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **100vh 차량 사진 위에 얹힌 midnight-ink UI chrome**으로 기억된다.
> **Code Complexity**: high — AEM + Swiper + responsive hero media + component hover overlays + reusable global navigation.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Kia Korea처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Kia Signature Regular", "Arial", sans-serif;
  font-weight: 400;
  letter-spacing: normal;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #fff;
  --fg: #05141F;
  --muted: #697278;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #05141F; }
.btn-primary { background: var(--brand); color: #fff; border: 1px solid var(--brand); }
```

**절대 하지 말아야 할 것 하나**: Kia를 파란 EV/모빌리티 브랜드처럼 만들지 말 것. UI primary는 `#005CB2`가 아니라 `#05141F`다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.kia.com/kr/` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | existing phase1 reuse: HTML + CSS + screenshot |
| HTML size | 88,131 bytes (AEM runtime page) |
| CSS files | 4 non-empty external CSS files, about 2,022,164 chars |
| Token prefix | `kia` |
| Method | existing `phase1/*.json`, CSS excerpts, HTML structure, and `hero-cropped.png` observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Adobe Experience Manager style runtime (`aem-Grid`, `cmp-container`, `data-cmp-is`) with clientlib bundles.
- **Design system**: Kia site component system — prefix is not deeply tokenized; most values are class-level CSS plus a small `--dp-*` and `--bs-*` variable set.
- **CSS architecture**:
  ```css
  @font-face           Kia Signature font families
  .btn-*               action components with :after wipe layer
  .global-header__*    navigation and subnav shell
  .key-visual__*       hero media, grid placement, carousel
  .pdp-link__*         quick-link card system
  --dp-* / --bs-*      datepicker/bootstrap utility variables, not main brand DS
  ```
- **Class naming**: BEM-like component classes (`global-header__navigation`, `key-visual__media`, `pdp-link__btn`).
- **Default theme**: mixed. The global page is light, but the first viewport is white text on darkened photography.
- **Font loading**: `@font-face` with `font-display: swap`, `.eot`, `.woff`, `.woff2` sources.
- **Canonical anchor**: `body { color: #05141f }`, `.btn-primary { background-color:#05141f; border:1px solid #05141f; color:#fff }`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Kia Signature Bold` (brand font, bundled by site)
- **Body font**: `Kia Signature Regular` (brand font, bundled by site)
- **Light font**: `Kia Signature Light` (brand font, bundled by site)
- **Code font**: N/A — no code UI role observed on homepage
- **Weight normal / bold**: `400` / family switch to `Kia Signature Bold`

```css
@font-face {
  font-display: swap;
  font-family: "Kia Signature Bold";
  font-style: normal;
  font-weight: 400;
  src: url(clientlib-site/resources/fonts/KiaSignatureBold.woff2) format("woff2");
}

@font-face {
  font-display: swap;
  font-family: "Kia Signature Regular";
  font-style: normal;
  font-weight: 400;
  src: url(clientlib-site/resources/fonts/KiaSignatureRegular.woff2) format("woff2");
}

@font-face {
  font-display: swap;
  font-family: "Kia Signature Light";
  font-style: normal;
  font-weight: 400;
  src: url(clientlib-site/resources/fonts/KiaSignatureLight.woff2) format("woff2");
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Kia Signature Bold** — if unavailable, use `Arial` or `Pretendard` at weight 700 but keep `letter-spacing: normal`; do not add tight tracking.
- **Kia Signature Regular** — substitute with `Arial` or `Pretendard` at 400, line-height `1.43` for base UI.
- **Kia Signature Light** — substitute with `Pretendard` 300 or 350 for pre-title copy; keep hero pre-title at 18px / 1.67 desktop.
- **Family-switch hierarchy** — do not collapse all text to one font family and use only numeric weights. Kia's CSS uses separate font-family names for optical tone.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---|
| `hero-title` | 52px | 400 via `Kia Signature Bold` | 1.23 | normal |
| `hero-title-mobile` | 34px | 400 via `Kia Signature Bold` | 1.29 | normal |
| `hero-pretitle` | 18px | 400 via `Kia Signature Light` | 1.67 | normal |
| `hero-pretitle-mobile` | 14px | 400 via `Kia Signature Light` | 1.71 | normal |
| `button` | 14px | 400 via `Kia Signature Bold` | 1 | normal |
| `body-base` | 16px | 400 | 1.43 | normal |
| `compact-label` | 12px / 9pt | 400 | 1.43 | normal |
| `large-number` | 40px | 400 via `Kia Signature Bold` | 48px | normal |

> ⚠️ Typography insight: the site has many `font-weight: 400` declarations because weight is encoded in the font-family name, not the numeric CSS weight.

### Principles

1. Use font-family as hierarchy. `Kia Signature Bold` at weight 400 is a different voice from `Kia Signature Regular` at weight 400.
2. Keep letter-spacing normal. Kia Korea does not use the negative tracking common in premium tech landing pages.
3. Hero text is large but not ultra-display. 52px / 1.23 is big enough to sit over a car image without becoming a fashion headline.
4. Light copy is intentionally tall. The 18px pre-title at line-height 1.67 creates air above the product name.
5. Numeric weight 500 and 600 are absent from the observed scale. Do not introduce a middle-weight typographic mush.
6. Buttons use the bold family, not heavier CSS weight. The black rectangle supplies emphasis; the text does not need extra weight.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (5 steps)

| Token | Hex |
|---|---|
| `kia-ink-primary` | `#05141F` |
| `kia-ink-secondary` | `#37434B` |
| `kia-text-muted` | `#697278` |
| `kia-disabled` | `#9FA5A9` |
| `kia-hairline` | `#DADBDC` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `kia-dark-bg` | `#05141F` |
| `kia-dark-hover` | `#37434B` |
| `kia-dark-disabled-bg` | `#828A8F` |
| `kia-dark-disabled-text` | `#B4B9BC` |

### 06-3. Neutral Ramp

| Step | Light | Dark / Text |
|---|---|---|
| 0 | `#fff` | `#000` |
| 50 | `#F8F8F8` | `#05141F` |
| 100 | `#F0F1F1` | `#37434B` |
| 200 | `#E6E6E6` | `#697278` |
| 300 | `#DADBDC` | `#9FA5A9` |
| 400 | `#D2D2D2` | `#B4B9BC` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Datepicker primary | `--dp-primary-color` | `#005CB2` |
| Datepicker primary alt | `--dp-primary-color` | `#1976D2` |
| Utility danger / red | observed chromatic | `#EA0029` |
| Swiper library default | library active bullet | `#007AFF` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `primary-action` | `#05141F` | CTA background, border, text ink |
| `primary-hover` | `#37434B` | `.btn-primary:after`, hover border |
| `surface-base` | `#fff` | body, secondary button, dark-type primary button |
| `surface-soft` | `#F8F8F8` | secondary hover, quick-link cards |
| `border-muted` | `#9FA5A9` | secondary button border |
| `border-light` | `#DADBDC` | disabled and hairline states |
| `text-muted` | `#697278` | muted utility and disabled dark button text |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--dp-background-color` | `#fff` | datepicker surface, not primary site surface token |
| `--dp-border-color` | `#ddd` | datepicker border |
| `--dp-primary-color` | `#005CB2` / `#1976D2` | datepicker selected state |
| `--bs-table-striped-color` | `#212529` | bootstrap table utility |
| `--bs-table-hover-color` | `#212529` | bootstrap table utility |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| `kia-ink-primary` | `#05141F` | 1334 |
| `kia-text-muted` | `#697278` | 736 |
| `surface-base` | `#fff` | 491 |
| `hairline` | `#DADBDC` | 374 |
| `surface-soft` | `#F8F8F8` | 241 |
| `kia-ink-secondary` | `#37434B` | 174 |
| `neutral-300` | `#D2D2D2` | 90 |
| `disabled` | `#9FA5A9` | 52 |
| `utility-red` | `#EA0029` | 48 |

### 06-8. Color Stories

**`{colors.ink-primary}` (`#05141F`)** — This is the real Kia Korea UI brand color. It is text ink, CTA fill, primary border, dark hover destination, and the color that makes the product photography feel engineered rather than lifestyle-soft.

**`{colors.surface-base}` (`#fff`)** — White is used as a clean interface plane and secondary button surface. In the first viewport it appears mostly as text and logo over image, so it reads like light over photography, not a flat page background.

**`{colors.text-muted}` (`#697278`)** — Muted gray is common enough to be structural. Use it for supporting utility text, disabled-dark labels, and secondary metadata; do not use it as headline color.

**`{colors.hairline}` (`#DADBDC`)** — The light gray border system keeps controls legible without adding decorative shadows. It is the quiet separator for disabled states and light chrome.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `hero-box-x` | 48px | desktop hero overlay horizontal padding |
| `hero-box-bottom` | 64px | desktop hero overlay bottom padding |
| `hero-info-top-row` | 140px | desktop hero grid top row |
| `hero-info-bottom-row` | 130px | desktop hero grid bottom row |
| `mobile-page-gutter` | 16px | mobile hero and cards |
| `button-x` | 24px | primary/secondary horizontal padding |
| `button-y` | 16px | primary/secondary vertical padding |
| `quick-card-gap` | 24px | PDP quick-link card gap |
| `quick-card-padding` | 24px | PDP quick-link card inner padding |
| `pagination-bottom` | 40px | desktop hero carousel dots |

**주요 alias**:
- `1pc` → 16px, used heavily for component padding and button gap.
- `3pc` → 48px, used for hero overlay horizontal breathing room.
- `5pc` → 80px, used as tablet/mobile visual bottom clearance in hero contexts.

### Whitespace Philosophy

Kia's whitespace is not a delicate editorial grid; it is a showroom staging system. The first viewport spends almost all available space on the vehicle image, then pins information low enough that the car can dominate the center of gravity.

Below the hero, card systems become denser: quick-link cards use 24px gaps and fixed 244px height. The rhythm is "open hero, operational links below" rather than "spacious everywhere."

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `button-radius` | 0 | `.btn-primary`, `.btn-secondary`, form reset |
| `quick-card-radius` | 0 | PDP quick-link cards |
| `carousel-dot-radius` | 50% | swiper pagination bullets |
| `chat-radius` | 50% | circular chat button |
| `toggle-track-radius` | 30px | toggle switch track |
| `small-control-radius` | 3px / 4px | secondary utility widgets |
| `modal-radius` | 8px / 10px | less prominent utility surfaces |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `none` | `none` | primary buttons, secondary buttons, hero chrome, quick-link cards |
| `toggle-knob` | `1px 3px 4px rgba(0,0,0,.2)` | toggle knob only |
| `chat-float` | `1px 1px 10px 0 #4E4E4E` | circular chat button over image |

> Shadow pattern: Kia Korea keeps chrome mostly flat. Shadow is allowed for floating utility controls, not for the main CTA or cards.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `button-wipe` | `transition: all .4s` | `.btn-primary:after`, `.btn-secondary:after` width expansion |
| `hero-pretitle-in` | `opacity + translateX(30%)`, duration `.5s/.6s`, delay `.1s` | inactive to active hero slide |
| `hero-title-in` | `opacity + translateX(30%)`, duration `.8s/.6s`, delay `.15s/.1s` | main title reveal |
| `pagination-fade` | `transition: opacity .3s` | swiper pagination |
| `quick-card-hover` | `transition: all .4s` | quick-link card inversion |
| `icon-shift` | `transition: .3s ease-in`, delay `.4s` | quick-link arrow movement |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `1344px` / `84pc` for quick-link inner content; hero media is full viewport.
- **Grid type**: AEM 12-column wrapper plus component-level CSS Grid/Flexbox.
- **Column count**: AEM `aem-Grid--12`; hero overlay grid uses `9.5fr 2fr 1.25fr`.
- **Gutter**: 24px in quick cards; 48px hero overlay side padding on desktop; 16px mobile gutter.

### Hero
- **Pattern Summary**: `100vh + full-bleed vehicle photography + low-left H1 + dual CTA below`
- Layout: media fills the viewport; text overlay sits in `.key-visual__box` and `.key-visual__info`.
- Background: `<picture>` switches desktop/mobile vehicle imagery; image uses `object-fit: cover`.
- **Background Treatment**: image-overlay by content placement. No CSS gradient overlay was captured for the main Niro slide; contrast comes from image tonality and white typography.
- H1: `52px` / family `Kia Signature Bold` / CSS weight `400` / tracking `normal`.
- Max-width: hero image is `100%`; text block variants generally use `width: 80%` when positioned.

### Section Rhythm

```css
.kwp-runtime .key-visual .big-visual { height: 100vh; }
.kwp-runtime .key-visual .big-visual .key-visual__media { padding-top: 100vh; }
.key-visual__box { padding: 0 48px 64px; }
.key-visual__info {
  display: grid;
  grid-template-columns: 9.5fr 2fr 1.25fr;
  grid-template-rows: 140px 1fr 130px;
}
```

### Card Patterns
- **Card background**: `#F8F8F8` for quick-link cards.
- **Card border**: none observed for quick-link cards; structure comes from fill contrast.
- **Card radius**: `0`.
- **Card padding**: `24px` desktop, `16px` mobile.
- **Card shadow**: none.
- **Hover**: background inverts to `#05141F`, icon swaps to white asset, arrow moves with delayed transition.

### Navigation Structure
- **Type**: horizontal global nav with dropdown/subnav; utility links on the right.
- **Position**: absolute over hero in `body.overwrap`; fixed overlay states exist for menu-open.
- **Height**: not a single token; visual height is driven by logo/nav content and top overlay.
- **Background**: transparent over first viewport; white text via `body.header--white`.
- **Border**: none in first hero state.

### Content Width
- **Prose max-width**: N/A — homepage is component and product-card oriented.
- **Container max-width**: `1344px` / `84pc` for quick-link rows.
- **Sidebar width**: N/A on homepage.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `max-width: 768px` | Most component compression: hero title 34px, card width 100%, 16px gutters. |
| Tablet | `max-width: 1024px` | Navigation and hero overlay switch to absolute/block handling. |
| Desktop-narrow | `max-width: 1366px` | Container and spacing adjustments for large but constrained screens. |
| Large | `min-width: 1367px` | Full desktop hero and 1344px content rows. |

### Touch Targets
- **Minimum tap size**: primary controls usually 40-48px high; mobile `.btn-small` is 40px.
- **Button height (mobile)**: about 40px for small buttons; hero buttons keep 13px/16px padding patterns.
- **Input height (mobile)**: form-specific states not fully observed from homepage.

### Collapsing Strategy
- **Navigation**: desktop horizontal GNB collapses around `1024px`; mobile menu button appears.
- **Grid columns**: quick-link rows change from thirds/quarters to full-width cards at `768px`.
- **Sidebar**: no homepage sidebar.
- **Hero layout**: desktop grid becomes block/absolute on tablet; mobile uses dedicated `<source media="(max-width: 768px)">` images.

### Image Behavior
- **Strategy**: responsive `<picture>` with separate mobile/desktop assets.
- **Max-width**: hero image fills container.
- **Aspect ratio handling**: `object-fit: cover`; portrait/landscape CSS uses viewport formulas for small visual variants.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**`.btn-primary`**

```html
<a class="btn-primary" href="/kr/buy/build-your-car/build">견적 내기</a>
```

| Spec | Value |
|---|---|
| Background | `#05141F` |
| Border | `1px solid #05141F` |
| Text | `#fff` |
| Font | `Kia Signature Bold`, 14px, weight 400 |
| Padding | `16px 24px` |
| Radius | `0` |
| Hover | border `#37434B`; `:after` layer expands width from 0 to 100% |
| Disabled | `#9FA5A9` bg/border, white at 0.6 alpha |
| Focus | `outline: 3px dashed #000`, offset 1px / -3px depending selector |

**`.btn-secondary`**

```html
<a class="btn-secondary no-border" href="/kr/vehicles/niro/features">자세히 보기</a>
```

| Spec | Value |
|---|---|
| Background | `#fff` |
| Border | `1px solid #9FA5A9` or no-border variant |
| Text | `#05141F` |
| Font | `Kia Signature Bold`, 14px, weight 400 |
| Padding | `16px 24px` |
| Hover | `:after` expands with `#F8F8F8` |
| Dark variant | bg `#05141F`, border/text `#fff` |

### Badges

Homepage badge data is limited, but shared CSS includes tag patterns:

| Spec | Value |
|---|---|
| Font | `Kia Signature Bold`, 12px / 9pt |
| Height | 32px desktop, 24px mobile |
| Radius | 16px style for middle tags |
| Text | usually white on dark or dark on light depending context |

### Cards & Containers

**`.pdp-link__btn` quick-link cards**

```html
<a class="pdp-link__btn type-left" href="/kr/buy/build-your-car/vehicle-lineup">
  <div class="pdp-link__btn-icon">...</div>
  <div class="pdp-link__btn-txt"><span class="pdp-link__txt-tit">견적 내기</span></div>
  <span class="pdp-link__more">자세히 보기</span>
</a>
```

| Spec | Value |
|---|---|
| Background | `#F8F8F8` |
| Height | 244px desktop, 143px mobile |
| Width | 25%, 33.333%, or 50% variant; 100% mobile |
| Padding | 24px desktop, 16px mobile |
| Radius | 0 |
| Hover | background `#05141F`; white hover icon; white more text |
| Motion | `transition: all .4s`; arrow transition `.3s ease-in` delayed `.4s` |

### Navigation

**`.global-header__navigation`**

| Spec | Value |
|---|---|
| Placement | absolute over hero when `body.overwrap` |
| Logo | centered Kia wordmark area; h1 text visually hidden |
| Links | white over hero through `body.header--white` |
| Primary links | 차량, 구매, 체험, 이벤트, 고객 지원, Discover Kia |
| Utility links | PBV, KR dropdown, 통합검색, 로그인 |
| Mobile | hamburger bars turn from white to `#05141F` when active |

### Inputs & Forms

Observed homepage form elements are mostly utility/library states rather than primary search fields.

| Spec | Value |
|---|---|
| Reset | `appearance: none; border-radius: 0` |
| Focus | dashed black outline pattern in components |
| Datepicker primary | `#005CB2` / `#1976D2` in `--dp-primary-color` |
| Datepicker border | `#ddd`, hover `#AAAEB7` |
| Error / danger | `#FF6F60` in datepicker vars; `#EA0029` appears as chromatic utility red |

### Hero Section

```html
<div class="key-visual main-visual">
  <div class="big-visual">
    <div class="key-visual__inner key-visual-runtime">
      <div class="swiper full-swiper-big">
        <div class="key-visual__media">
          <picture>
            <source media="(max-width: 768px)" srcset="..._mo.jpg" />
            <img src="..._pc.jpg" alt="" />
          </picture>
        </div>
        <div class="key-visual__box">
          <div class="visual-tit type-left type-bottom type-white">
            <div class="pre-title">이루어질 거예요, 바라는 대로</div>
            <div class="main-title">The new Niro</div>
            <div class="visual-btn">...</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```

| Spec | Value |
|---|---|
| Height | 100vh |
| Media | `object-fit: cover`, full viewport |
| Text color | `#fff` |
| Title | 52px desktop, 34px tablet/mobile |
| Pre-title | 18px desktop, 14px tablet/mobile |
| Position | low-left by grid row 3 and bottom type positioning |
| Pagination | white ring bullets, 18px hitbox, 12px/9pt dot visual |

### 13-2. Named Variants

- **`button-primary`** — `#05141F` fill, white text, square edge, 0.4s dark wipe.
- **`button-secondary`** — white fill, `#05141F` text, muted border, 0.4s pale wipe.
- **`button-primary-type-dark`** — white fill on dark surface, `#05141F` text, `#B4B9BC` hover layer.
- **`button-secondary-type-dark`** — `#05141F` fill with white border/text, white-alpha hover layer.
- **`quick-link-card`** — `#F8F8F8` rectangular tile that inverts to `#05141F`.
- **`hero-carousel-dot`** — transparent 18px bullet with white ring pseudo-element and filled active state.
- **`visual-chat-circle`** — 56px white circular chat launcher with `1px 1px 10px 0 #4E4E4E`.

### 13-3. Signature Micro-Specs

```yaml
hero-grid-showroom-stage:
  description: "The hero overlay is a showroom-stage grid rather than ordinary centered marketing copy."
  technique: "grid-template-columns: 9.5fr 2fr 1.25fr; grid-template-rows: 140px 1fr 130px; padding: 0 48px 64px"
  applied_to: ["{component.hero-visual}", ".key-visual__info", ".visual-tit.type-left.type-bottom"]
  visual_signature: "The car remains central while text sits low-left like a product label in a dark showroom."

midnight-ink-button-wipe:
  description: "Primary actions darken by a horizontal overlay, not a color swap or opacity fade."
  technique: ".btn-primary:after { background-color:#37434B; width:0; transition:all .4s } + hover width:100%; border-color:#37434B"
  applied_to: ["{component.button-primary}", "{component.button-secondary}", ".btn-primary", ".btn-secondary"]
  visual_signature: "A mechanical shutter passes across a square midnight-ink label."

family-as-weight-typography:
  description: "Kia encodes optical hierarchy through font-family choice while CSS numeric weights stay mostly 400."
  technique: "@font-face Kia Signature Bold/Regular/Light all declared with font-weight:400; hero title 52px/1.23; pre-title 18px/1.67"
  applied_to: ["body", ".main-title", ".pre-title", ".btn-primary", ".btn-secondary"]
  visual_signature: "The voice changes from light caption to product title without adding heavy numeric weight."

ring-dot-carousel:
  description: "Carousel controls stay as small white rings over photography, with active state filling the ring."
  technique: "transparent 18px swiper bullet + :before white border ring; active bullet uses white fill"
  applied_to: [".full-swiper-big .swiper-pagination-bullet", ".key-visual"]
  visual_signature: "Slide state reads like a tiny instrument mark, not a colored interface layer."

quick-link-hard-inversion-card:
  description: "Operational cards remain flat pale slabs until hover turns the whole tile into Kia midnight ink."
  technique: ".pdp-link__btn { background:#F8F8F8; height:244px; padding:24px; border-radius:0; transition:all .4s } + hover background:#05141F"
  applied_to: ["{component.quick-link-card}", ".pdp-link__btn", ".pdp-link__more"]
  visual_signature: "Below the hero, the page shifts from showroom exhibit to squared service-counter tiles."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Product name as literal hero title; no abstract SaaS claim | "The new Niro" |
| Pre-title | Emotional promise or performance phrase, short and cinematic | "이루어질 거예요, 바라는 대로" |
| Primary CTA | Purchase action, direct verb phrase | "견적 내기" |
| Secondary CTA | Exploration action | "자세히 보기" |
| Navigation | Functional Korean category labels | "차량", "구매", "체험", "고객 지원" |
| Tone | Confident, showroom-clean, product-first | "Movement that inspires" in metadata |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Kia Korea — copy into your root stylesheet */
:root {
  /* Fonts */
  --kia-font-display: "Kia Signature Bold", "Arial", sans-serif;
  --kia-font-body: "Kia Signature Regular", "Arial", sans-serif;
  --kia-font-light: "Kia Signature Light", "Arial", sans-serif;
  --kia-font-weight-normal: 400;

  /* Brand / neutrals */
  --kia-color-ink: #05141F;
  --kia-color-ink-hover: #37434B;
  --kia-color-muted: #697278;
  --kia-color-surface: #fff;
  --kia-color-surface-soft: #F8F8F8;
  --kia-color-border: #DADBDC;
  --kia-color-border-strong: #9FA5A9;

  /* Utility accents */
  --kia-color-utility-blue: #005CB2;
  --kia-color-utility-red: #EA0029;

  /* Spacing */
  --kia-space-1: 8px;
  --kia-space-2: 16px;
  --kia-space-3: 24px;
  --kia-space-6: 48px;
  --kia-space-8: 64px;

  /* Radius */
  --kia-radius-none: 0;
  --kia-radius-round: 50%;
}

.kia-hero {
  min-height: 100vh;
  position: relative;
  color: #fff;
  overflow: hidden;
}

.kia-hero img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.kia-hero__content {
  position: absolute;
  left: 48px;
  bottom: 64px;
  width: 80%;
}

.kia-hero__eyebrow {
  font-family: var(--kia-font-light);
  font-size: 18px;
  line-height: 1.67;
}

.kia-hero__title {
  margin-top: 16px;
  font-family: var(--kia-font-display);
  font-size: 52px;
  line-height: 1.23;
  font-weight: 400;
  letter-spacing: normal;
}

.kia-btn {
  display: inline-block;
  position: relative;
  z-index: 1;
  min-width: 88px;
  padding: 16px 24px;
  border-radius: 0;
  font-family: var(--kia-font-display);
  font-size: 14px;
  line-height: 1;
  text-align: center;
  overflow: hidden;
}

.kia-btn::after {
  content: "";
  position: absolute;
  inset: 0 auto 0 0;
  width: 0;
  transition: all .4s;
  z-index: -1;
}

.kia-btn--primary {
  background: #05141F;
  border: 1px solid #05141F;
  color: #fff;
}

.kia-btn--primary::after { background: #37434B; }
.kia-btn--primary:hover { border-color: #37434B; }
.kia-btn--primary:hover::after { width: 100%; }

.kia-btn--secondary {
  background: #fff;
  border: 1px solid #9FA5A9;
  color: #05141F;
}

.kia-btn--secondary::after { background: #F8F8F8; }
.kia-btn--secondary:hover::after { width: 100%; }
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `{colors.ink-primary}` | `#05141F` |
| Background | `{colors.surface-base}` | `#fff` |
| Soft surface | `{colors.surface-soft}` | `#F8F8F8` |
| Text primary | `{colors.ink-primary}` | `#05141F` |
| Text muted | `{colors.text-muted}` | `#697278` |
| Border | `{colors.hairline}` | `#DADBDC` |
| Utility blue | `{colors.utility-blue}` | `#005CB2` |
| Error / red utility | `{colors.utility-red}` | `#EA0029` |

### Example Component Prompts

#### Hero Section

```text
Kia Korea 스타일 히어로 섹션을 만들어줘.
- 100vh 풀블리드 차량 사진을 배경으로 쓰고, 이미지는 object-fit: cover.
- 상단 네비게이션은 투명 오버레이, 텍스트와 로고는 #fff.
- 히어로 카피는 좌하단 배치: left 48px, bottom 64px, width 80%.
- pre-title: Kia Signature Light, 18px, line-height 1.67, color #fff.
- title: Kia Signature Bold, 52px, line-height 1.23, weight 400, letter-spacing normal.
- CTA 두 개: secondary white button + primary #05141F button, 둘 다 square edge.
```

#### Card Component

```text
Kia Korea 스타일 quick-link 카드를 만들어줘.
- 배경 #F8F8F8, radius 0, shadow 없음, padding 24px, height 244px.
- hover 시 배경을 #05141F로 반전하고 텍스트/아이콘을 #fff로 변경.
- transition은 all .4s.
- grid에서는 24px gap, desktop 3-4열, mobile 1열.
```

#### Badge

```text
Kia Korea 스타일 작은 라벨을 만들어줘.
- font: Kia Signature Bold, 12px 또는 9pt, weight 400.
- height 32px desktop / 24px mobile.
- 색은 #05141F, #fff, #DADBDC 중에서만 선택.
- rounded pill을 쓰더라도 핵심 CTA에는 radius 0을 유지.
```

#### Navigation

```text
Kia Korea 스타일 상단 네비게이션을 만들어줘.
- hero 위에서는 transparent overlay, position absolute top 0.
- 좌측: 차량/구매/체험/이벤트/고객 지원/Discover Kia.
- 중앙: Kia 로고.
- 우측: PBV, KR dropdown, 통합검색, 로그인.
- hero 상태에서는 모든 nav text #fff, 메뉴 활성/모바일 상태에서는 #05141F로 전환.
```

### Iteration Guide

- **색상 변경 시**: primary CTA와 본문 ink는 `#05141F`를 유지. `#005CB2`는 datepicker/utility 계열로만 제한.
- **폰트 변경 시**: numeric weight를 올리기 전에 font-family를 `Bold`, `Regular`, `Light`로 나눈다.
- **여백 조정 시**: hero는 48px/64px의 큰 stage spacing, card는 24px의 operational spacing으로 분리한다.
- **새 컴포넌트 추가 시**: radius 0, shadow 없음, hover wipe 또는 hard inversion을 우선한다.
- **사진 위 텍스트**: 텍스트 박스 배경을 새로 깔지 말고 이미지 톤과 white typography로 해결한다.
- **반응형**: 1024px에서 nav/hero overlay 구조를 바꾸고, 768px에서 card를 1열로 접는다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#05141F` as the core UI brand color for CTA fill, text, and dark hover systems.
- Let product photography dominate the first viewport; UI chrome should feel applied, not dominant.
- Keep buttons square and mechanical: `border-radius: 0`, `padding: 16px 24px`, `transition: all .4s`.
- Use `Kia Signature Bold`, `Regular`, and `Light` as separate optical voices.
- Keep display `letter-spacing: normal`; Kia does not rely on tight editorial tracking.
- Use `#F8F8F8` for operational cards and `#fff` for clean UI surfaces.
- Use image-specific mobile/desktop assets through `<picture>`, not one cropped bitmap for every viewport.
- Keep focus visible: dashed black outlines are part of the control contract.

### ❌ DON'T

- 배경 전체를 `#000` 또는 pure black으로 두지 말 것 — Kia의 dark UI는 `#05141F` 사용.
- 본문 텍스트를 `#000` 또는 `black`으로 두지 말 것 — 기본 ink는 `#05141F` 사용.
- primary CTA를 `#005CB2`로 두지 말 것 — `#005CB2`는 utility/datepicker 계열이고 CTA는 `#05141F` 사용.
- secondary card 배경을 `#fff`만으로 두지 말 것 — quick-link 카드 계열은 `#F8F8F8` 사용.
- muted text를 `#999` 같은 임의 회색으로 두지 말 것 — 관측된 muted는 `#697278` 사용.
- border를 `#ccc`로 일반화하지 말 것 — light hairline은 `#DADBDC`, strong border는 `#9FA5A9` 사용.
- button hover를 단순 opacity 처리로 만들지 말 것 — `#37434B` wipe layer를 사용.
- CTA 버튼에 `border-radius: 999px` 사용 금지 — Kia primary/secondary action은 square edge.
- hero title에 `font-weight: 700`만 적용하고 브랜드 폰트를 생략하지 말 것 — `Kia Signature Bold` family가 핵심.
- hero를 center-aligned SaaS headline으로 만들지 말 것 — low-left product-label placement를 유지.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **Second brand color: absent** — the homepage UI does not need a second chromatic brand color; `#05141F` carries the system.
- **Gradient identity: none** — no purple-blue AI gradient, no EV neon mesh, no decorative color wash over the hero.
- **Rounded CTA softness: absent** — primary and secondary CTAs are square-edged, not pill buttons.
- **Heavy chrome shadows: absent** — buttons and cards do not float; only utility controls such as chat/toggle receive shadow.
- **Weight 500/600 hierarchy: absent** — most hierarchy is family-based, not numeric mid-weight based.
- **Tight display tracking: absent** — hero text keeps `letter-spacing: normal`.
- **Opaque first-viewport nav: absent** — the nav floats over photography rather than sitting in a white app bar.
- **Generic app card layout: absent** — the hero is not a centered text card; the car photo is the layout.
- **Decorative illustration: absent** — product photography and icons carry the visual system.
- **Rainbow vehicle-category palette: absent** — even EV and mobility content remains inside the neutral Kia shell.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-only scope** — this analysis used the Kia Korea homepage artifacts. Configurator, vehicle detail pages, checkout/reservation, login, and dealer search flows may introduce additional component states.
- **Existing phase1 reuse** — no fresh crawl was performed in this run because reusable `insane-design/kia/phase1`, CSS, HTML, and screenshot artifacts were present.
- **Dynamic Vue/AEM components** — several homepage blocks are mounted through `data-cmp-is="application"` and JSON props; their fully rendered DOM states may differ from static HTML.
- **Form validation states incomplete** — datepicker variables and input reset/focus rules were observed, but complete error/loading/success form flows were not visited.
- **Dark-mode mapping unavailable** — the site has dark-on-image and dark component variants, but no full alternate dark theme token map was verified.
- **Image contrast is slide-dependent** — the first captured hero is The new Niro. Other carousel slides may use different image brightness, but the typography/control rules appear shared.
- **Exact nav dimensions not fully isolated** — header height is distributed across component rules and runtime state; this report describes visible structure rather than a single token.
- **Motion JavaScript not audited** — CSS transitions and Swiper patterns were inspected, but runtime timing from JavaScript initialization was not deeply traced.
- **Logo SVG internals excluded** — brand color selection intentionally ignores logo file colors and relies on CSS/UI usage; this avoids logo-wall and SVG contamination.
- **Report HTML skipped by request** — Step 6 RENDER-HTML was intentionally omitted; this file is the requested `design.md` guidebook only.
