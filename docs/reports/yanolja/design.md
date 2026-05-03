---
schema_version: 3.2
slug: yanolja
service_name: NOL / Yanolja
site_url: https://yanolja.com
fetched_at: 2026-05-03T07:25:48Z
default_theme: light
brand_color: "#4154FF"
primary_font: Pretendard
font_weight_normal: 400
token_prefix: nol

bold_direction: Travel Utility
aesthetic_category: commerce-marketplace
signature_element: category_icon_marketplace
code_complexity: medium

medium: web
medium_confidence: high

archetype: commerce-marketplace
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Tailwind utility classes expose semantic color, spacing, radius, and interaction tokens, but token names are compiled classes rather than a fully documented public DS."

colors:
  primary: "#4154FF"
  primary-press: "#2432AD"
  primary-weak: "#F5F6FF"
  primary-line-weak2: "#B2BAFF"
  primary-line-weak4: "#7280FF"
  surface-page: "#FFFFFF"
  surface-weak: "#F7F8FB"
  surface-weak1: "#F2F3F7"
  surface-weak2: "#E9EAEF"
  surface-weak3: "#DADBDF"
  text-primary: "#1B1C1F"
  text-secondary: "#6E6F73"
  text-tertiary: "#8B8D92"
  danger: "#E5000F"
  focus-blue: "#007AFF"
typography:
  display: "Pretendard"
  body: "Pretendard, Apple SD Gothic Neo, Roboto, Arial Helvetica, sans-serif"
  ladder:
    - { token: title-xl, size: "4rem", weight: 700, line_height: "4.8rem", tracking: "inherit" }
    - { token: title-lg, size: "3.2rem", weight: 700, line_height: "3.8rem", tracking: "inherit" }
    - { token: title-md, size: "2.4rem", weight: 700, line_height: "2.9rem", tracking: "inherit" }
    - { token: body-lg, size: "1.8rem", weight: 600, line_height: "2.2rem", tracking: "inherit" }
    - { token: body-md, size: "1.6rem", weight: 400, line_height: "1.9rem", tracking: "inherit" }
    - { token: body-sm, size: "1.4rem", weight: 400, line_height: "1.7rem", tracking: "inherit" }
  weights_used: [400, 600, 700]
  weights_absent: [300, 500, 800, 900]
components:
  search-pill: { bg: "{colors.surface-weak1}", radius: "9999px", height: "56px", max_width: "664px" }
  primary-pill-button: { bg: "{colors.primary}", fg: "#FFFFFF", radius: "9999px", padding: "0 16px" }
  category-icon-cell: { bg: "transparent", radius: "none", gap: "10px" }
  promo-strip: { bg: "#EAF2FF", radius: "16px", height: "80px" }
  event-card: { bg: "image + gradient overlay", radius: "16px", shadow: "none" }
---

# DESIGN.md — NOL / Yanolja

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

NOL / Yanolja is not a quiet hotel-booking page. It behaves like a travel mall kiosk: a fixed white counter, a large rounded search slot, a row of pictographic aisles, and promotional tiles that sit close enough to feel transactional. The page is built for repeated scanning, not for slow brand admiration. The visual contract is "find the leisure product fast, then let the deal art do the persuasion."

The identity comes from a sharp blue-violet primary, `#4154FF` (`{colors.primary}`), used with unusually pale blue support surfaces like `#F5F6FF` (`{colors.primary-weak}`) and `#B2BAFF` (`{colors.primary-line-weak2}`). This is not the red/pink travel-commerce palette of many Korean consumer apps. The accent is synthetic and app-like, almost utility SaaS in its hue, but it is softened by big icon illustrations and coupon banners.

Typography is dense Korean commerce typography: Pretendard, mostly 400 for normal labels, 600 for medium emphasis, and 700 for promotional titles. The site does not rely on letter-spacing craft. Instead, it relies on weight contrast, icon scale, rounded containers, and mobile-first rem sizing. Text blocks are short because the product categories and card images do the semantic work.

The homepage spacing is split in two. Header and search have generous white air, then category rows and coupon modules compress into a marketplace cadence. This "open top, dense catalog below" rhythm is the site. It must not be recreated as a hero-centered SaaS landing page or a full-bleed editorial travel page.

조금 더 풀면, NOL의 홈은 **공항 터미널 옆에 세워진 여행 마켓의 카운터**처럼 작동한다. 위쪽 흰 카운터는 체크인 데스크와 시장 입구의 안내 카운터를 겸하고, 둥근 search slot은 시장 한가운데 매대 위에 박힌 가격표 카탈로그 슬릿이다. 카테고리 픽토그램 행은 면세점 통로 위 천장에 매달린 안내 사인이자, 시장 진열대 끝에 꽂혀 있는 색상 표지다. 쿠폰 banner는 게이트 옆 벽면에 붙은 라스트-미닛 카탈로그 포스터, 우측 promotion card는 마켓 카운터 옆 즉석 장바구니 매대다 — 가격이 먼저 보이고 출발 시간은 그 다음. 두 번째 브랜드 컬러가 없는 이유: 시장 안내 시스템은 단일 노선 색만으로 충분히 빠르다.

### Key Characteristics

- White fixed header with a high 100px desktop bar and a 150px mobile header stack.
- Large capsule search field on desktop, light neutral background, icon-first affordance.
- Primary blue `#4154FF` appears as action, focus, outline, and selected-state color.
- Category navigation is icon-led and horizontally scannable, not text-menu led.
- Promotional strip uses a pale blue surface and a centered login/benefit CTA.
- Cards are image-heavy with 16px rounded corners; text sits inside image overlays, not separate feature cards.
- Neutral ramp is cool and utility-like: `#F7F8FB`, `#F2F3F7`, `#E9EAEF`, `#DADBDF`.
- Shadows are sparse and small; structure mostly comes from surface color and radius.
- Breakpoint logic is mobile-first with a hard desktop switch around 801px.
- The brand is "travel marketplace utility", not luxury hospitality.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Travel Utility
> **Aesthetic Category**: commerce-marketplace
> **Signature Element**: 이 사이트는 **icon-led travel marketplace rail**으로 기억된다.
> **Code Complexity**: medium — Tailwind utility scale, responsive desktop/mobile header split, gradients, swiper states, and sparse interaction tokens.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 NOL / Yanolja처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Pretendard", "Apple SD Gothic Neo", Roboto, Arial Helvetica, sans-serif;
  font-weight: 400;
  letter-spacing: inherit;
}

/* 2. 배경 + 텍스트 */
:root {
  --nol-bg: #FFFFFF;
  --nol-surface-weak: #F7F8FB;
  --nol-surface-weak1: #F2F3F7;
  --nol-fg: #1B1C1F;
}
body {
  background: var(--nol-bg);
  color: var(--nol-fg);
}

/* 3. 액션 컬러 */
:root {
  --nol-primary: #4154FF;
  --nol-primary-press: #2432AD;
  --nol-primary-weak: #F5F6FF;
}
```

**절대 하지 말아야 할 것 하나**: `#4154FF`를 전체 배경 그라디언트로 크게 펴지 말 것. NOL의 primary는 CTA, outline, focus, selected state에 쓰이고, 페이지 골격은 white와 cool neutral이 맡는다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://yanolja.com` |
| Fetched | 2026-05-03T07:25:48Z |
| Reused phase1 | `insane-design/yanolja/phase1/*.json`, `css/*`, `index.html`, `screenshots/hero-cropped.png` |
| Extractor | cached curl/phase1 output + manual interpretation |
| HTML size | 370322 bytes |
| CSS files | 6 external CSS files, 151041 combined chars |
| Token prefix | `nol` (derived; source classes use Tailwind semantic utility names) |
| Method | CSS frequency, semantic utility classes, screenshot observation, and DOM structure review |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js-style static app output; body class hash `__className_4ca083` and compiled CSS chunks.
- **Design system**: Tailwind utility system with semantic class names rather than exported CSS custom-property tokens.
- **CSS architecture**:
  ```text
  semantic utilities   .bg-fill-primary-main, .text-fill-neutral-main
  interaction states   .bg-interaction-primary-presshover-strong3
  layout utilities     .pc:*, .max-w-legacy-pc-size, .w-pc-size
  vendor utilities     swiper classes and --swiper-* variables
  ```
- **Class naming**: Tailwind-style utility classes with Korean commerce-specific breakpoint aliases such as `pc:`.
- **Default theme**: light (`#FFFFFF` page, `#F7F8FB` and `#F2F3F7` weak surfaces).
- **Font loading**: Pretendard + `pretendard Fallback`, with system Korean/Roboto fallback chain.
- **Canonical anchor**: NOL logo + search pill + icon category rail.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Pretendard` (open-source Korean UI font)
- **Code font**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace`
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --nol-font-family: "Pretendard", "Apple SD Gothic Neo", Roboto, Arial Helvetica, sans-serif;
  --nol-font-family-code: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace;
  --nol-font-weight-normal: 400;
  --nol-font-weight-medium: 600;
  --nol-font-weight-bold: 700;
}
body {
  font-family: var(--nol-font-family);
  font-weight: var(--nol-font-weight-normal);
}
```

### Note on Font Substitutes

- **Pretendard** is the correct substitute target. If the exact hosted file is unavailable, use the public Pretendard package before falling back to system UI.
- **Apple SD Gothic Neo** works as the first Korean system fallback on macOS/iOS, but it makes labels slightly narrower and more Apple-like. Keep button padding generous when it is used.
- **Roboto / Arial Helvetica** are fallback only. They should not become the visual lead because the Korean glyph rhythm changes and the category rail loses NOL's app-commerce density.
- **No letter-spacing compensation** was found beyond `inherit`; do not add negative tracking to force a premium editorial look.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| title-xl | 4rem | 700 | 4.8rem | inherit |
| title-lg | 3.2rem | 700 | 3.8rem | inherit |
| title-md | 2.4rem | 700 | 2.9rem | inherit |
| body-xl | 2rem | 700 | 2.4rem | inherit |
| body-lg-strong | 1.8rem | 600 | 2.2rem | inherit |
| body-lg | 1.8rem | 400 | 2.2rem | inherit |
| body-md | 1.6rem | 400 | 1.9rem | inherit |
| body-sm | 1.4rem | 400 | 1.7rem | inherit |
| caption | 1.2rem | 400 | 1.4rem | inherit |
| micro | 1.1rem | 400 | 1.3rem | inherit |

> ⚠️ The extractor did not find a named typography token map. The scale above is reconstructed from recurring compiled CSS declarations: `1.6rem`, `1.8rem`, `1.4rem`, `2rem`, `3.2rem`, and their paired line-heights.

### Principles

1. Body labels are compact, not editorial. `1.4rem` to `1.8rem` carries most commerce UI copy.
2. Weight 500 is deliberately absent in the observed CSS; use 600 for medium emphasis and 700 for promotion or section titles.
3. Display type does not use negative tracking. Let Pretendard's default Korean metrics breathe.
4. Promotional cards can jump to 2.4rem or 3.2rem, but navigation labels should stay smaller and denser.
5. Icon category labels should feel like app tabs: short Korean nouns, centered, and paired with generous icon size.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp

| Token | Hex |
|---|---|
| `nol-primary-weak` | `#F5F6FF` |
| `nol-primary-line-weak2` | `#B2BAFF` |
| `nol-primary-line-weak4` | `#7280FF` |
| `nol-primary-main` | `#4154FF` |
| `nol-primary-press` | `#2432AD` |

### 06-2. Brand Dark Variant

> N/A — no full dark theme ramp was surfaced in the homepage CSS. `#2432AD` appears as a pressed/strong primary interaction value, not as a dark-mode brand token.

### 06-3. Neutral Ramp

| Step | Light Token | Hex |
|---|---|---|
| static-white | `nol-static-white` | `#FFFFFF` |
| neutral-weak | `nol-fill-neutral-weak` | `#F7F8FB` |
| neutral-weak1 | `nol-fill-neutral-weak1` | `#F2F3F7` |
| neutral-weak2 | `nol-fill-neutral-weak2` | `#E9EAEF` |
| neutral-weak3 | `nol-fill-neutral-weak3` | `#DADBDF` |
| neutral-weak4 | `nol-text-neutral-weak4` | `#B6B7BB` |
| neutral-medium | `nol-text-neutral-medium` | `#8B8D92` |
| neutral-strong1 | `nol-text-neutral-strong1` | `#6E6F73` |
| neutral-main | `nol-fill-neutral-main` | `#1B1C1F` |
| static-black | `nol-static-black` | `#000000` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| danger | main | `#E5000F` |
| danger | press/strong | `#9C000A` |
| danger | weak | `#FEF5F5` |
| warning | weak | `#FEF8F2` |
| gold | weak | `#FFFAE1` |
| swiper/default blue | vendor | `#007AFF` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `bg-fill-primary-main` | `#4154FF` | primary button, selected state, action fill |
| `border-line-primary-main` | `#4154FF` | primary outline and focus/selection border |
| `text-fill-primary-main` | `#4154FF` | primary text link or selected label |
| `bg-interaction-primary-presshover-strong3` | `#2432AD` | active/pressed primary state |
| `bg-fill-neutral-weak` | `#F7F8FB` | cards, weak panels, input fields |
| `bg-fill-neutral-weak1` | `#F2F3F7` | search bar and hover weak surface |
| `border-line-neutral-weak2` | `#E9EAEF` | dividers and light borders |
| `text-fill-neutral-main` | `#1B1C1F` | primary text |
| `text-fill-neutral-medium` | `#8B8D92` | secondary text and placeholders |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--bubble-fill` | `#F5F6FF` | pale primary decorative bubble fill |
| `--bubble-stroke` | `#B2BAFF` | pale primary decorative outline |
| `--swiper-theme-color` | `#007AFF` | vendor slider control default |
| `--tw-ring-color` | `rgb(59 130 246 / 0.5)` | Tailwind ring fallback |
| `--tw-ring-offset-color` | `#FFFFFF` | focus ring offset |
| `--tw-shadow-color` | `#F7F8FB` | Tailwind shadow color utility fallback |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---|---:|
| transparent utility | `#00000000` | 52 |
| static-white | `#FFFFFF` | 14 |
| gradient-blue | `#3C7BFD` | 11 |
| gradient-blue-2 | `#3E5FEA` | 11 |
| gradient-blue-3 | `#4052EB` | 11 |
| gradient-cyan | `#4BA2F6` | 11 |
| gradient-purple | `#643EDF` | 11 |
| primary-main-near | `#3549FF` | 5 |
| surface-weak | `#F7F8FB` | 5 |
| primary-main | `#4154FF` | 4 |

### Color Stories

**`{colors.primary}` (`#4154FF`)** — The single NOL action blue. It marks login CTA, selected outlines, primary fills, and brand text. Use it as an interaction color, not as a wallpaper.

**`{colors.surface-page}` (`#FFFFFF`)** — The commerce floor. Header, icon rail, and product browsing all start on white so icon art and promotional photography can carry color.

**`{colors.surface-weak1}` (`#F2F3F7`)** — The search and hover utility surface. It is cool, slightly blue-gray, and keeps input chrome visible without adding borders.

**`{colors.text-primary}` (`#1B1C1F`)** — The real text color. Avoid pure black for product labels and UI body; NOL's text is a softened near-black that sits better beside colorful icons.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `gap-2` | 2px | micro label/icon pairing |
| `gap-8` | 8px | compact control spacing |
| `gap-10` | 10px | category label/icon cadence |
| `gap-12` | 12px | button groups, small card internals |
| `gap-16` | 16px | card grid and coupon module separation |
| `gap-20` | 20px | common module spacing |
| `gap-24` | 24px | large row separation |
| `gap-40` | 40px | desktop category/section breathing |
| `gap-100` | 100px | wide desktop decorative separation |
| `gap-140` | 140px | large desktop horizontal air |

**주요 alias**:
- `max-w-mobile-size` → `500px` mobile app-shell width.
- `max-w-legacy-pc-size` → `768px` legacy constrained container.
- `w-pc-size` → `1280px` desktop content width.
- `max-w-[1320px]` → wide desktop container.

### Whitespace Philosophy

NOL uses air at the top to create trust and utility, then switches into density. The 100px desktop header, 56px search pill, and broad white field make the service feel stable before the user hits the icon marketplace.

Below that, spacing compresses into rows: category icons, coupon modules, and image cards sit in a regular retail rhythm. Do not turn every section into a huge editorial band. The correct cadence is "wide control surface, compact shopping grid."

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `rounded-4` | 4px | tiny utility chips |
| `rounded-6` | 6px | compact controls |
| `rounded-8` | 8px | small buttons or badges |
| `rounded-12` | 12px | medium panels |
| `rounded-16` | 16px | promo strips and image cards |
| `rounded-20` | 20px | large soft modules |
| `rounded-24` | 24px | large image/coupon surface |
| `rounded-28` | 28px | large rounded container |
| `rounded-full` / `rounded-capsule` | 9999px | search pill, primary capsule CTA, circular icon buttons |
| `50%` | 50% | circular icon controls |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none | `none` | most page sections and image cards |
| shadow-1 | `0 0 8px 0 rgba(0,0,0,.05)` | subtle panel lift |
| shadow-2 | `0 0 8px 0 rgba(0,0,0,.1)` | stronger floating controls |
| shadow-3 | `0 0 6px 0 rgba(0,0,0,.2)` | high contrast overlay/control |
| header shadow | Tailwind `shadow-sm` + `--tw-shadow` | fixed desktop header separator |
| carousel edge | `0px 6px 8px -6px rgba(0,0,0,.2)` family | slider affordance and edge masks |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| opacity fade | `opacity .3s` | carousel or overlay visibility |
| drawer transform | `transform .2s, top .2s` | mobile sheet/menu movement |
| side transform | `transform .2s, left .2s` / `right .2s` | off-canvas panel movement |
| swiper pagination | vendor-controlled | banner slider index and carousel behavior |

Motion is supportive rather than expressive. The site does not present a scroll storytelling system; it uses short utility transitions around sheets, sliders, and state changes.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `1280px` primary desktop shell, `1320px` wide max, `500px` mobile shell, `768px` legacy container.
- **Grid type**: CSS Grid for nav/category rail (`repeat(auto-fit, minmax(0, 1fr))`), flex for header and horizontal control groups.
- **Column count**: icon/category rail auto-fits into equal cells; card grids use 2-4 columns depending on viewport and module.
- **Gutter**: `16px`, `20px`, and `24px` are the main commercial grid spacings.

### Hero

- **Pattern Summary**: `fixed utility header + pale benefit strip + horizontal category rail + image promotion carousel`.
- Layout: not a single H1 hero. The first viewport is a commerce control surface.
- Background: `#FFFFFF` page with pale blue promo strip and image cards lower in the viewport.
- **Background Treatment**: solid white plus image-card overlays; one observed gradient family uses `linear-gradient(99deg, #8279FF, #819DFF 30.25%, #80C1FE 50%, #79A1FF 80.23%, #4154FF)`.
- H1: no traditional homepage H1 surfaced in the first viewport; promotional cards use large 700-weight Korean text.
- Max-width: desktop header/container around `1280px`; mobile app shell around `500px`.

### Section Rhythm

```css
section {
  padding: 40px 0;          /* desktop observed via pc:py-40 */
  max-width: 1280px;        /* pc:w-pc-size */
}
```

### Card Patterns

- **Card background**: image or `#F7F8FB`/`#F2F3F7` weak neutral.
- **Card border**: usually none; line tokens appear more in controls than in marketing cards.
- **Card radius**: `16px` is the dominant card radius, with larger `20px`/`24px` for soft modules.
- **Card padding**: `16px`, `20px`, `24px`, `32px` depending on density.
- **Card shadow**: mostly none; image and surface contrast do the work.

### Navigation Structure

- **Type**: fixed top header + icon shortcut rail.
- **Position**: fixed header; desktop header is `top: 0; left: 0; right: 0`.
- **Height**: `100px` desktop, `150px` mobile header stack.
- **Background**: `#FFFFFF`.
- **Border**: first viewport uses a sharp blue bottom line under the header in the cached screenshot; CSS also uses shadow-sm for desktop separation.

### Content Width

- **Prose max-width**: not a prose-first site; short UI copy only.
- **Container max-width**: `1280px` primary, `1320px` wide.
- **Sidebar width**: no persistent sidebar in homepage; hamburger/category control acts as local navigation.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Tiny | `320px` max | defensive mobile adjustment |
| Mobile+ | `360px` min | small phone refinement |
| Small | `600px` min | compact tablet / large mobile step |
| Tablet | `640px`, `768px` min | Tailwind default utilities and legacy shell |
| PC switch | `801px` min / `800px` max | main desktop/mobile split point |
| Desktop | `1024px`, `1280px` min | desktop grid and large content shell |
| Wide | `1320px`, `1536px` min | wide layout caps |

### Touch Targets

- **Minimum tap size**: many controls use `44px`, `48px`, `52px`, and `56px` heights, meeting mobile expectations.
- **Button height (mobile)**: `44px` to `52px` common.
- **Input height (mobile/desktop search)**: search pill visually around `56px`.

### Collapsing Strategy

- **Navigation**: desktop uses fixed wide header with search and icon utilities; mobile uses a taller stacked header and app-shell max width.
- **Grid columns**: category rail auto-fits equal cells; card grids collapse by utility classes rather than bespoke JS layout.
- **Sidebar**: none persistent; menu/hamburger is a floating category affordance.
- **Hero layout**: no editorial hero. First viewport collapses around header, category rail, and carousel.

### Image Behavior

- **Strategy**: remote promotional imagery, icon art, and card backgrounds.
- **Max-width**: `100%` plus fixed-width utility caps.
- **Aspect ratio handling**: card art appears clipped into rounded rectangles; object-fit behavior is inferred from image-card presentation, not fully proven from named tokens.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary capsule**

| Spec | Value |
|---|---|
| Background | `#4154FF` |
| Text | `#FFFFFF` |
| Radius | `9999px` |
| Press/active | `#2432AD` |
| Font | Pretendard 600 or 700 depending on CTA density |

```html
<button class="rounded-capsule bg-fill-primary-main text-static-white">
  로그인/가입하기
</button>
```

**Neutral icon button**

| Spec | Value |
|---|---|
| Background | `#FFFFFF` or transparent |
| Text/icon | `#1B1C1F` |
| Radius | `50%` or `9999px` |
| Hover | `#F2F3F7` weak interaction surface |

### Badges

Badges are small, commerce-oriented labels: coupon, discount, event, and promotional state. They should be short Korean phrases, not decorative tags.

| Spec | Value |
|---|---|
| Background | `#F5F6FF`, `#FEF5F5`, or image-overlay contextual color |
| Text | `#4154FF`, `#E5000F`, or white on imagery |
| Radius | `8px` to `9999px` |
| Padding | `2px 8px` or compact rem equivalent |

### Cards & Containers

**Promo image card**

| Spec | Value |
|---|---|
| Background | travel/event image with overlay |
| Radius | `16px` |
| Text | white, 700, large Korean headline |
| Shadow | none |
| Layout | horizontal carousel / two-up desktop row |

**Coupon strip**

| Spec | Value |
|---|---|
| Background | pale blue-tinted surface, close to `#EAF2FF` / weak primary family |
| Radius | `16px` |
| Alignment | centered text + primary capsule CTA |
| Height | visually around `80px` |

### Navigation

The navigation is not a text-only nav. It is a transaction header:

- NOL logo at left.
- Search pill in the center.
- Utility icons for account, wish, cart, and recent products.
- Category icon rail below, with illustrated icons and centered Korean labels.

### Inputs & Forms

**Search pill**

| Spec | Value |
|---|---|
| Background | `#F2F3F7` |
| Text placeholder | `#8B8D92` |
| Radius | `9999px` |
| Height | about `56px` |
| Max width | about `664px` inside desktop header |
| Border | none |

Focus should use a blue ring/outline from the primary family, not a dark border.

### Hero Section

NOL's "hero" is a product-navigation stack:

1. fixed header/search,
2. pale benefit/login strip,
3. category rail with icon illustrations,
4. event tabs/coupon modules,
5. promotional image carousel.

Do not replace this with a single large travel photograph and an H1. That would erase the marketplace behavior.

### 13-2. Named Variants

**search-pill** — rounded search surface

```css
.search-pill {
  height: 56px;
  max-width: 664px;
  border-radius: 9999px;
  background: #F2F3F7;
  color: #8B8D92;
}
```

**primary-pill-button** — login/CTA capsule

```css
.primary-pill-button {
  border-radius: 9999px;
  background: #4154FF;
  color: #FFFFFF;
  font-weight: 700;
}
.primary-pill-button:active {
  background: #2432AD;
}
```

**category-icon-cell** — icon-led marketplace category

```css
.category-icon-cell {
  display: grid;
  justify-items: center;
  gap: 10px;
  color: #1B1C1F;
  background: transparent;
}
```

**promo-strip** — benefit/login banner

```css
.promo-strip {
  min-height: 80px;
  border-radius: 16px;
  background: #EAF2FF;
}
```

**event-card** — image promotion card

```css
.event-card {
  border-radius: 16px;
  overflow: hidden;
  color: #FFFFFF;
  box-shadow: none;
}
```

### 13-3. Signature Micro-Specs

#### icon-led-commerce-rail

```yaml
icon-led-commerce-rail:
  description: "The category row is the page's core recognition device — not a nav, not a hero, but a tile shelf."
  technique: "equal-width grid cells (6-8 across desktop, 4 mobile), large illustrated icons (~56px), short centered Korean labels, no descriptions or counts."
  applied_to: ["{component.category-rail}", "shortcut grid", "homepage primary discovery"]
  visual_signature: "the page reads as an app marketplace before it ever reads as a travel landing — recognition is iconic, not editorial."
  intent: "Korean travel super-app users scan icons in <2 seconds; copy-led nav would slow that scan."
```

#### primary-blue-state-system

```yaml
primary-blue-state-system:
  description: "One blue-violet family handles every interactive state — action, focus, outline, selected, press."
  technique: "#4154FF main, #2432AD press, #F5F6FF weak fill, #B2BAFF pale line, #FFFFFF on-brand text — 5 stops, one hue."
  applied_to: ["{components.button-primary}", "{components.input-focus}", "selected card border", "decorative bubble", "focus ring"]
  visual_signature: "high-saturation utility blue controlled by surrounding white — never spreads, never decorates."
  intent: "super-app surfaces compete with photography; one disciplined hue prevents the UI from fighting the destination."
```

#### capsule-search-counter

```yaml
capsule-search-counter:
  description: "The header works like a retail counter, not a navigation bar."
  technique: "fixed 100px desktop header, 56px rounded search pill (radius 28px) as the dominant control, large utility icons, white surface, 1px separator."
  applied_to: ["{component.top-header}", "{component.search-pill}", "homepage entry"]
  visual_signature: "search dominates the chrome — the page invites a query before it invites browsing."
  intent: "transactional travel intent must be answered first; nav links are demoted because most users arrive with a destination in mind."
```

#### dense-neutral-commerce-ladder

```yaml
dense-neutral-commerce-ladder:
  description: "Cool neutral steps build all non-brand structure with no warm tones."
  technique: "#F7F8FB → #F2F3F7 → #E9EAEF → #DADBDF → #8B8D92 → #1B1C1F (6-step cool-grey ramp)."
  applied_to: ["{component.input-field}", "hover surface", "{component.divider}", "disabled state", "secondary text"]
  visual_signature: "the page stays bright while feeling highly segmented — a clean ledger under colourful brand chips."
  intent: "warm neutrals would soften the commerce intent; cool neutrals keep the page transactional and scannable."
```

#### promo-chip-density-cap

```yaml
promo-chip-density-cap:
  description: "Promotional chips (sale %, coupon, free-pass) follow a hard density cap per row to prevent festival-flyer noise."
  technique: "max 2 promo chips per card, weight 700, 11-12px text, padding 4px 8px, radius 4px; saturated red/yellow tokens reserved for these only."
  applied_to: ["{component.product-card}", "{component.promo-chip}", "search result row"]
  visual_signature: "promotional energy stays bursty but never collapses into Korean-marketplace chaos."
  intent: "K-commerce loves chips; codifying the density cap is what separates Yanolja from looking like a price-comparison page."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | benefit-first, short Korean commerce phrase | "동남아 인기 투어 매일 선착순 50% 할인" |
| Primary CTA | direct action, compact | "로그인/가입하기" |
| Category | noun phrase, no sentence | "항공", "해외숙소", "호텔/리조트" |
| Promotion | number + benefit + product | "13만원 상당 Grab 패스 무료증정" |
| Tone | app-commerce, energetic but not playful-copy heavy | "쿠폰팩", "이벤트더보기" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* NOL / Yanolja — copy into your root stylesheet */
:root {
  /* Fonts */
  --nol-font-family: "Pretendard", "Apple SD Gothic Neo", Roboto, Arial Helvetica, sans-serif;
  --nol-font-family-code: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace;
  --nol-font-weight-normal: 400;
  --nol-font-weight-medium: 600;
  --nol-font-weight-bold: 700;

  /* Brand */
  --nol-color-brand-25: #F5F6FF;
  --nol-color-brand-200: #B2BAFF;
  --nol-color-brand-400: #7280FF;
  --nol-color-brand-600: #4154FF;
  --nol-color-brand-900: #2432AD;

  /* Surfaces */
  --nol-bg-page: #FFFFFF;
  --nol-bg-weak: #F7F8FB;
  --nol-bg-weak1: #F2F3F7;
  --nol-bg-weak2: #E9EAEF;
  --nol-border: #DADBDF;
  --nol-text: #1B1C1F;
  --nol-text-muted: #8B8D92;
  --nol-text-secondary: #6E6F73;

  /* Key spacing */
  --nol-space-xs: 8px;
  --nol-space-sm: 12px;
  --nol-space-md: 16px;
  --nol-space-lg: 24px;
  --nol-space-xl: 40px;

  /* Radius */
  --nol-radius-sm: 8px;
  --nol-radius-md: 16px;
  --nol-radius-lg: 24px;
  --nol-radius-pill: 9999px;
}

body {
  margin: 0;
  background: var(--nol-bg-page);
  color: var(--nol-text);
  font-family: var(--nol-font-family);
  font-weight: var(--nol-font-weight-normal);
}

.nol-search {
  height: 56px;
  max-width: 664px;
  border: 0;
  border-radius: var(--nol-radius-pill);
  background: var(--nol-bg-weak1);
  color: var(--nol-text-muted);
  padding: 0 24px;
}

.nol-primary-button {
  border: 0;
  border-radius: var(--nol-radius-pill);
  background: var(--nol-color-brand-600);
  color: #FFFFFF;
  font-weight: var(--nol-font-weight-bold);
  padding: 10px 16px;
}

.nol-primary-button:active {
  background: var(--nol-color-brand-900);
}

.nol-promo-card {
  border-radius: var(--nol-radius-md);
  overflow: hidden;
  background: var(--nol-bg-weak);
  box-shadow: none;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — NOL / Yanolja inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        nol: {
          primary: '#4154FF',
          primaryPress: '#2432AD',
          primaryWeak: '#F5F6FF',
          primaryLineWeak2: '#B2BAFF',
          primaryLineWeak4: '#7280FF',
          surface: '#FFFFFF',
          weak: '#F7F8FB',
          weak1: '#F2F3F7',
          weak2: '#E9EAEF',
          weak3: '#DADBDF',
          text: '#1B1C1F',
          muted: '#8B8D92',
          secondary: '#6E6F73',
          danger: '#E5000F',
        },
      },
      fontFamily: {
        sans: ['Pretendard', 'Apple SD Gothic Neo', 'Roboto', 'Arial Helvetica', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        medium: '600',
        bold: '700',
      },
      borderRadius: {
        nol: '16px',
        'nol-lg': '24px',
        capsule: '9999px',
      },
      boxShadow: {
        'nol-1': '0 0 8px 0 rgba(0,0,0,.05)',
        'nol-2': '0 0 8px 0 rgba(0,0,0,.1)',
        'nol-3': '0 0 6px 0 rgba(0,0,0,.2)',
      },
      maxWidth: {
        'nol-mobile': '500px',
        'nol-legacy': '768px',
        'nol-pc': '1280px',
        'nol-wide': '1320px',
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
| Brand primary | `nol-primary-main` | `#4154FF` |
| Brand pressed | `nol-primary-press` | `#2432AD` |
| Background | `nol-static-white` | `#FFFFFF` |
| Weak surface | `nol-fill-neutral-weak1` | `#F2F3F7` |
| Text primary | `nol-fill-neutral-main` | `#1B1C1F` |
| Text muted | `nol-text-neutral-medium` | `#8B8D92` |
| Border | `nol-line-neutral-weak3` | `#DADBDF` |
| Danger | `nol-danger-main` | `#E5000F` |

### Example Component Prompts

#### Header/Search

```text
NOL / Yanolja 스타일의 상단 검색 헤더를 만들어줘.
- 배경: #FFFFFF
- 높이: desktop 100px, mobile 150px
- 로고: 좌측, 선명한 blue-violet 브랜드 느낌
- 검색창: #F2F3F7 배경, 9999px capsule, 높이 56px, placeholder #8B8D92
- 우측: 마이/찜/장바구니/최근 본 상품 icon utilities
- 하단 구분: 아주 얇은 #4154FF 또는 subtle shadow
```

#### Category Rail

```text
NOL / Yanolja 스타일의 카테고리 아이콘 레일을 만들어줘.
- equal-width grid 또는 horizontal rail
- 큰 컬러 일러스트 아이콘 + 짧은 한국어 라벨
- 라벨: Pretendard 1.4rem~1.6rem, weight 400~600, color #1B1C1F
- 배경은 #FFFFFF, 카드 배경이나 border를 넣지 말 것
- 전체 리듬은 촘촘하지만 icon 주변은 10px 이상 띄울 것
```

#### Promo Card

```text
NOL / Yanolja 스타일의 여행 프로모션 카드를 만들어줘.
- 카드 radius: 16px
- 배경: 실제 여행/공연 이미지 + 어두운 overlay
- headline: Pretendard 2.4rem~3.2rem, weight 700, white
- body: white, 1.6rem~1.8rem
- shadow는 넣지 말고 image contrast와 radius로 분리
- primary blue #4154FF는 CTA나 small badge에만 사용
```

### Iteration Guide

- **색상 변경 시**: `#4154FF`를 primary action에만 유지하고, 큰 배경은 white/neutral/photography로 둔다.
- **폰트 변경 시**: Pretendard를 우선 사용한다. 500 weight를 새로 추가하지 말고 600 또는 700으로 정리한다.
- **여백 조정 시**: header/search는 여유롭게, category/card grid는 조밀하게 유지한다.
- **새 컴포넌트 추가 시**: 16px radius + cool neutral surface + sparse shadow 원칙을 따른다.
- **반응형**: `801px` 전후의 PC/mobile split을 기준으로 설계한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#4154FF` as the main action/selection color and `#2432AD` for pressed primary states.
- Keep the top surface white and utility-led: logo, search, icon controls, category rail.
- Use Pretendard with weights 400, 600, and 700.
- Build category navigation around colorful icon illustrations and short Korean labels.
- Use `#F2F3F7` and `#F7F8FB` for search, hover, and weak panel surfaces.
- Let promotional imagery carry large emotional color; keep chrome neutral.
- Use 16px radius for image cards and 9999px radius for pills.
- Keep shadows subtle or absent unless a floating control needs separation.

### ❌ DON'T

- 배경을 `#000000` 또는 dark full-screen으로 두지 말 것 — 대신 `#FFFFFF` 사용.
- 본문 텍스트를 `#000000` pure black으로 고정하지 말 것 — 대신 `#1B1C1F` 사용.
- 검색창 배경을 `#FFFFFF`로 두고 border만 넣지 말 것 — 대신 `#F2F3F7` surface 사용.
- primary CTA를 `#007AFF` vendor blue로 두지 말 것 — 대신 `#4154FF` 사용.
- primary pressed state를 같은 `#4154FF`로 유지하지 말 것 — 대신 `#2432AD` 사용.
- weak panel을 warm beige `#F5F0E8`로 만들지 말 것 — 대신 cool neutral `#F7F8FB` 또는 `#F2F3F7` 사용.
- card radius를 `32px` 이상으로 키우지 말 것 — 대신 image cards는 `16px`, large modules는 `24px` 내에서 사용.
- body에 `font-weight: 500`을 기본으로 쓰지 말 것 — observed system은 `400`, `600`, `700` 중심.
- 전체 hero에 보라 그라디언트 `#8279FF` to `#4154FF`를 깔지 말 것 — gradient는 decorative/accent scope에만 제한.
- image promotion cards에 heavy shadow `0 20px 60px rgba(0,0,0,.25)`를 넣지 말 것 — 대신 shadow none 또는 small `0 0 8px rgba(0,0,0,.05)` 사용.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Editorial hero H1: absent. The first viewport is a control surface and marketplace rail.
- Luxury hospitality minimalism: absent. This is benefit-first commerce, not quiet resort branding.
- Second brand color: none. Blue-violet `#4154FF` carries the action identity.
- Warm neutral base: none in the main UI. Neutrals are cool gray-blue, not cream or sand.
- Weight 500: deliberately absent in observed typography extraction.
- Heavy decorative shadow: absent. Structure comes from white, neutral fills, image contrast, and radius.
- Persistent sidebar: absent on homepage. Navigation is header + category rail + hamburger affordance.
- Long paragraph copy: absent. Labels and promotions are short, scannable Korean commerce fragments.
- Dark mode homepage: not surfaced in the cached first-page CSS.
- Border-heavy cards: mostly absent. Cards rely on surface or imagery rather than outlines.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single cached homepage basis** — This guide reuses existing `insane-design/yanolja` phase1 artifacts. It does not prove current production changes after the cached crawl.
- **No live network refetch in this run** — Per instruction, existing phase1 data was reused. `fetched_at` records this guidebook generation time, not a fresh site crawl time.
- **Typography token names not exported** — The extractor found repeated font sizes/weights but no named type scale object. Type tokens are reconstructed from compiled CSS frequency.
- **Dark mode not verified** — Some dark/pressed values exist, but a full dark theme surface was not observed.
- **Subflows not visited** — Checkout, login, search results, product detail, booking, cart, and payment states are outside this guide.
- **Form validation states not surfaced** — Error/focus/loading forms may exist in subflows; only homepage/search/header patterns are represented.
- **Motion JS not analyzed** — CSS transitions and swiper hints were observed, but runtime animation curves and carousel configuration were not inspected from JavaScript.
- **Icon art source not normalized** — Category icons are treated as visual evidence from the screenshot, not as extracted asset tokens.
- **Remote image color contamination** — Some high-frequency chromatic colors come from gradients or promotional imagery, so brand selection prioritizes semantic utility classes over raw frequency alone.
- **Breakpoint behavior inferred from CSS** — The guide records available media queries and visible layout split, but no live responsive screenshot pass was run for this output.
