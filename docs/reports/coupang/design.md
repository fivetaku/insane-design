---
schema_version: 3.2
slug: coupang
service_name: Coupang
site_url: https://www.coupang.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: light
brand_color: "#346AFF"
primary_font: "Apple SD Gothic Neo"
font_weight_normal: 400
token_prefix: "--ui"

bold_direction: "Dense Commerce"
aesthetic_category: "other"
signature_element: "hero_impact"
code_complexity: "high"

medium: web
medium_confidence: high

archetype: commerce-marketplace
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "401 CSS custom properties, --ui-b token families, --ui-c button component tokens, and repeated commerce components are present, but this is extracted from production CSS rather than an official public design-system guide."

colors:
  ui-b-color-white: "#FFFFFF"
  ui-action-blue: "#346AFF"
  ui-commerce-red: "#CB1400"
  ui-text-primary: "#212B36"
  ui-border-muted: "#DDDDDD"
  ui-text-strong: "#111111"
typography:
  display: "Apple SD Gothic Neo"
  body: "Apple SD Gothic Neo"
  ladder:
    - { token: compact-caption, size: "11px", weight: 400, line_height: "14px" }
    - { token: category-label, size: "12px", weight: 700, line_height: "17px" }
    - { token: body, size: "14px", weight: 400, line_height: "20px" }
    - { token: section-title, size: "24px", weight: 700, line_height: "32px" }
    - { token: promo-display, size: "56px+", weight: 700, line_height: "1" }
  weights_used: [400, 600, 700, 800]
  weights_absent: [300, 500, 900]
components:
  search-bar: { border: "2px solid #346AFF", height: "40px", radius: "0" }
  category-tile: { bg: "#346AFF", radius: "0", width: "110px" }
  button-blue-md: { bg: "#346AFF", radius: "4px", min_height: "32px" }
  product-card: { bg: "#FFFFFF", border: "1px solid #DDDDDD", radius: "0-4px" }
---

# DESIGN.md - Coupang

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Coupang is the canonical example of high-throughput Korean **marketplace** design. Every surface decision serves throughput: the search bar is 40px with a hard `#346AFF` (`{colors.ui-action-blue}`) border because the **marketplace** entry gate must be instant; the category slab is flat and blue because a **store** directory cannot afford ambiguity; the product grid runs on white **canvas** with `#DDDDDD` hairlines because the inventory must never compete with itself for visual attention.

The interface has no **editorial** mode. There is no hero headline inviting you to dream; there is a search input waiting for a noun. `#346AFF` (`{colors.ui-action-blue}`) is the single action register — button, search rim, category tile, CTA. `#CB1400` (`{colors.ui-commerce-red}`) is the price urgency stamp and discount marker, not a sibling brand color. The white **canvas** of the page background is the commerce floor, kept neutral so the seasonal campaign banners can carry rotating color weather without destabilizing the shell. There is no second brand color for the chrome because a fulfillment-center floor does not need wallpaper.

The typography is equally **marketplace**-economical. The page spends most of its type budget below 14px: compact labels, category names, prices, and utility links — the shelf-tag economy of a large-format **store**. The jump to 56px+ / 700 campaign type happens inside ad creatives only, like a supermarket poster taped over a neutral aisle. The shortcut strip below the search is a color-coded floor guide to **store** aisles, not a navigation menu. The search bar is the barcode scanner gate at the loading dock — tap intent in, SKU stream out. Shadow belongs to dropdowns and floating rails, not to every product card; the **marketplace** floor is separated by hairlines, not by decorative elevation.

### Key Characteristics

- Search-first header: the central product search field is the main interactive object, not a secondary nav utility.
- Rectangular blue category block: #346AFF appears as a strong vertical tile and action color.
- Dense horizontal shortcut strip with small icons and 12px labels.
- White card surfaces with thin #DDDDDD hairlines and little decorative radius.
- Product and promotion imagery carries color variation; the UI shell stays neutral.
- Korean system typography, mostly 11-14px, with frequent 700-weight category and price emphasis.
- Red #CB1400 is reserved for urgency, coupons, discounts, and logo/marketing emphasis.
- Utility shadows appear on floating rails and overlays, not as a general card aesthetic.
- Responsive behavior is breakpoint-heavy, using 600, 768, 1024, and 1500 ranges.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Dense Commerce
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **search-led marketplace header with blue category control**으로 기억된다.
> **Code Complexity**: high — Next.js production markup, Tailwind-style utility classes, Swiper modules, tokenized button/radius/spacing systems, and ad-driven content states combine into a dense page.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Coupang처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Apple SD Gothic Neo", "Noto Sans KR", "Roboto", "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #212B36; }
body { background: var(--bg); color: var(--fg); }

/* 3. 액션 블루 */
:root { --brand: #346AFF; }
.search-shell { border: 2px solid var(--brand); }
.category-tile { background: var(--brand); }
```

**절대 하지 말아야 할 것 하나**: 쿠팡을 "깔끔한 D2C 브랜드 랜딩"처럼 만들지 말 것. 실제 구조는 검색, 카테고리, GNB, 광고 배너, 상품 그리드가 동시에 보이는 밀도 높은 marketplace UI다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.coupang.com` |
| Fetched | 2026-05-03 report generation, phase1 artifacts from existing `insane-design/coupang/` |
| Extractor | reused existing HTML/CSS/screenshot/phase1 JSON |
| HTML size | 373533 bytes (Next.js/React streamed markup) |
| CSS files | 14 external CSS files, about 364773 CSS characters |
| Token prefix | `--ui`, plus Tailwind-style `--tw-*` runtime variables |
| Method | Existing phase1 token extraction + CSS/HTML/screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js / React streamed markup with production CDN assets.
- **Design system**: internal UI token layer using `--ui-b-*` base tokens and `--ui-c-*` component tokens.
- **CSS architecture**:
  ```css
  --ui-b-*      base tokens: color, radius, border, opacity, spacing, typography
  --ui-c-*      component tokens: button color, size, padding, radius, state
  --tw-*        Tailwind runtime utility variables and shadow/ring state
  ```
- **Class naming**: utility-heavy `fw-*`, responsive prefixes such as `s600:`, `s768:`, `s1024:`, and legacy semantic classes such as `gnb-menu-item`, `product-search`, `main-today`.
- **Default theme**: light, with `#FFFFFF` dominant and gray structural bands.
- **Font loading**: system Korean stack centered on `Apple SD Gothic Neo`; no custom display font required for the shell.
- **Canonical anchor**: the top header search module and blue category tile are the strongest reusable UI anchors.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Apple SD Gothic Neo` (system font on Apple platforms)
- **Body font**: `Apple SD Gothic Neo, Noto Sans TC, Noto Sans JP, Noto Sans KR, Noto Sans, Roboto, Helvetica Neue, Arial, sans-serif`
- **Code font**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace`
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --ui-font-family: "Apple SD Gothic Neo", "Noto Sans KR", "Roboto", "Helvetica Neue", Arial, sans-serif;
  --ui-font-family-code: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --ui-font-weight-normal: 400;
  --ui-font-weight-bold: 700;
}
body {
  font-family: var(--ui-font-family);
  font-weight: var(--ui-font-weight-normal);
}
```

### Note on Font Substitutes

- **Apple SD Gothic Neo** is the target for Korean text on macOS/iOS. On Windows or Linux, use **Noto Sans KR** at the same numeric weights.
- If the replacement feels wider, reduce dense nav labels from `14px` to `13px` rather than tightening letter-spacing globally.
- Do not substitute a high-personality display face for the platform shell. Coupang's display energy comes from ad artwork and bold campaign text, not from a branded UI font.
- Keep body letter-spacing at normal or `0`; only large campaign typography can tolerate negative tracking such as `-1px`.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| compact-caption | 11px | 400 / 700 | 14-17px | normal |
| category-label | 12px | 700 | 17px | normal |
| utility-link | 12px | 400 | 15-17px | normal |
| product-body | 14px | 400 | 20px | normal |
| product-emphasis | 14px | 700 | 20px | normal |
| card-title | 16px | 700 | 22px | normal |
| section-title | 24px | 700 | 32px | -0.4px to -1px when used large |
| campaign-display | 56px+ | 700 / 800 | 1 | -1px where artwork demands compression |

> ⚠️ The extracted `typography.json` had no semantic scale map, but raw CSS frequency is clear: 12px, 14px, 11px, 16px, 18px, and 24px dominate. Coupang is a compact commerce typography system, not a spacious editorial scale.

### Principles

1. Body text is 14px, not 16px - marketplace density depends on fitting product titles, price fragments, labels, and utility actions into tight cards.
2. Weight 700 is a structural tool. Category headings, price emphasis, and section titles use bold frequently; weight 500 is not a key identity.
3. UI shell text stays neutral and small so promotion images can be visually loud without fighting the chrome.
4. Letter-spacing is usually normal. Negative spacing appears as a campaign/display correction, not as a global brand style.
5. Korean fallback quality matters more than novelty. A generic Latin-first font will break rhythm in product cards and GNB labels.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed key steps)

| Token | Hex |
|---|---|
| action-blue | `#346AFF` |
| link-blue | `#4285F4` |
| link-blue-alt | `#0073E9` |
| commerce-red | `#CB1400` |
| urgent-red | `#AE0000` |

### 06-2. Brand Dark Variant

> N/A - homepage analysis did not surface a complete dark-mode counterpart palette. The CSS includes dark text and blue-gray ramps, but the visible page is a light marketplace shell.

### 06-3. Neutral Ramp

| Step | Light | Usage |
|---|---|---|
| white | `#FFFFFF` | page, header, cards, search input, floating rail |
| near-white | `#FAFAFA` | subtle surface variation |
| hairline | `#DDDDDD` | product/card borders and dividers |
| muted text | `#888888` | helper and secondary labels |
| body text | `#333333` | legacy body copy and labels |
| strong text | `#111111` | headings and high-emphasis text |
| bluegray text | `#212B36` | newer UI text/tokenized shell |
| deeper gray | `#454F5B` | secondary blue-gray text family |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Coupang action blue | primary interactive | `#346AFF` |
| Coupang urgency red | discount / coupon / logo emphasis | `#CB1400` |
| Link hover blue | nav/category hover | `#4285F4` |
| Darker link blue | legacy link/accent | `#0073E9` |
| Semantic dark blue-gray | text/control family | `#212B36` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `{colors.ui-action-blue}` | `#346AFF` | search border, category block, button token family, focus/ring |
| `{colors.ui-commerce-red}` | `#CB1400` | discount urgency, coupon emphasis, logo red family |
| `{colors.ui-text-primary}` | `#212B36` | modern UI text and button plain token |
| `{colors.ui-border-muted}` | `#DDDDDD` | neutral borders and dividers |
| `{colors.ui-b-color-white}` | `#FFFFFF` | dominant shell and card surface |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--ui-c-Button-Color-Background-Blue-Normal` | HSL equivalent of `#346AFF` | filled blue button background |
| `--ui-c-Button-Color-Border-Blue-Normal` | HSL equivalent of `#346AFF` | outline/filled button border |
| `--ui-c-Button-Color-Text-Blue-Filled-Normal` | white | text on filled blue button |
| `--ui-c-Button-filled-hover` | darker blue HSL | hover state for filled action |
| `--ui-c-Button-outline-hover` | pale blue HSL | hover state for outline action |
| `--ui-c-Button-Color-Background-disabled` | blue-gray 100 | disabled button fill |

### 06-7. Dominant Colors (실제 DOM/CSS 빈도 순)

| Token | Hex | Frequency / role |
|---|---|---|
| surface-white | `#FFFFFF` | highest normalized surface occurrence |
| border-gray | `#DDDDDD` | high-frequency divider/card border |
| action-blue | `#346AFF` | highest chromatic UI/action color |
| commerce-red | `#CB1400` | urgency, coupon, promotion, logo red |
| text-bluegray | `#212B36` | frequent modern UI text family |
| text-dark | `#111111` | heading/high-emphasis text |
| link-blue | `#4285F4` | link/category hover blue |

### 06-8. Color Stories

**`{colors.ui-action-blue}` (`#346AFF`)** - The control color. It owns the category block, search ring, button tokens, and focus/ring behavior. Use it when the user can act, search, submit, or move deeper into the marketplace.

**`{colors.ui-b-color-white}` (`#FFFFFF`)** - The neutral selling floor. Coupang keeps the UI shell white so product photos, ad creatives, and discount colors can rotate without destabilizing the page.

**`{colors.ui-text-primary}` (`#212B36`)** - The newer blue-gray text anchor. It is less blunt than pure black and pairs with the tokenized `--ui-b-color-bluegray-*` ramp.

**`{colors.ui-border-muted}` (`#DDDDDD`)** - The quiet structure. Borders do much of the layout work because cards are not heavily rounded or elevated.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--ui-b-spacing-box-100` | 2px | micro alignment |
| `--ui-b-spacing-box-200` | 4px | small icon/text separation |
| `--ui-b-spacing-box-400` | 8px | compact internal gaps |
| `--ui-b-spacing-box-600` | 12px | controls and card internals |
| `--ui-b-spacing-box-800` | 16px | common gutters |
| `--ui-b-spacing-box-1200` | 24px | larger module separation |
| `--ui-b-spacing-inline-1700` | 44px | touch/control width step |
| `--ui-b-spacing-inline-2000` | 64px | large horizontal rail step |
| `--ui-b-spacing-stack-2600` | 128px | large vertical stack token, rarely visible in dense homepage shell |

**주요 alias**:
- `--ui-b-spacing-box-*` -> compact internal padding ladder.
- `--ui-b-spacing-inline-*` -> horizontal spacing and control sizing.
- `--ui-b-spacing-stack-*` -> vertical rhythm ladder.

### Whitespace Philosophy

Coupang spends whitespace only where it increases scanning speed. The top header is tight but segmented: category tile, logo, search, account, cart, and shortcut strip each get just enough separation to be individually clickable. Below that, the hero/promotion band opens up because campaign artwork needs a billboard moment.

The product grid returns to compression. Cards, price lines, discount labels, and recommendation rows sit closer than a brand site would allow. This is intentional marketplace pressure: the user should always see the next deal, next category, or next action.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--ui-b-radius-none` | 0px | category block, rectangular shell |
| `--ui-b-radius-100` | 2px | tiny utility controls |
| `--ui-b-radius-200` | 3px | small legacy controls |
| `--ui-b-radius-300` | 4px | default button/control radius |
| `--ui-b-radius-500` | 8px | larger modern modules |
| `--ui-b-radius-600` | 16px | occasional larger surface |
| `--ui-b-radius-full` | 999px | circular badges, counters, pills |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| dropdown-heavy | `0 4px 5px rgba(0,0,0,.3)` | overlays and floating menu surfaces |
| side-rail | `5px 0 5px #d1d1d1, -5px 0 5px #d1d1d1, 0 -3px 5px #d1d1d1` | floating side rail style |
| modern-elevation | `0 6px 12px 6px rgba(34,40,46,.2), 0 7px 14px 7px rgba(34,40,46,.1)` | high-elevation tokenized surfaces |
| card-light | `0 1px 4px rgba(0,0,0,0.08)` | subtle product/control elevation |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| opacity-slow | `opacity .6s ease-in-out` | carousel/banner fades |
| all-medium | `all .5s ease-in-out` | broad UI state transition |
| all-slow | `all 1s ease-in-out` | campaign/background transitions |
| transform-medium | `transform .6s ease-in-out` | slider movement |
| border-medium | `border .5s` | focus/selection state |
| shadow-fast | `box-shadow .2s ease` | hover elevation |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: desktop shell is centered around a wide commerce canvas; screenshot indicates roughly 1100-1200px of active header/content width with side rails.
- **Grid type**: mixed Flexbox and utility grid. Header uses flex alignment; product/promotion modules use repeated card/grid structures.
- **Column count**: variable by module. Header is functional zones; today's discovery/product sections form multi-column marketplace grids.
- **Gutter**: 12-16px common internal gutters, with 20-24px module spacing.

### Hero

- **🆕 Pattern Summary**: `about 450px visible promo band + light gray campaign background + centered ad artwork + right coupon rail`
- Layout: marketplace hero carousel/promotion area, not a text-first landing hero.
- Background: pale campaign gray and image-driven promotion backgrounds.
- **🆕 Background Treatment**: solid/light promotional band, overlaid with campaign artwork and right-rail coupon/product stack.
- H1: campaign artwork uses large Korean display type, commonly bold 700/800, visually around 56px+.
- Max-width: content fills the commerce shell; ad image occupies the central stage.

### Section Rhythm

```css
section {
  padding: 20px 16px;
  max-width: approximately 1100px;
}
```

### Card Patterns

- **Card background**: `#FFFFFF`
- **Card border**: `1px solid #DDDDDD` or no visible border when image tile dominates.
- **Card radius**: usually 0-4px; larger radii are not the default shell language.
- **Card padding**: 8-16px depending on product density.
- **Card shadow**: mostly none for grid cards; shadows reserved for floating overlays and side rails.

### Navigation Structure

- **Type**: horizontal utility header + shortcut GNB + category block.
- **Position**: static at top in captured desktop screenshot.
- **Height**: top utility strip about 32px; main header/search about 70px; shortcut row about 40px.
- **Background**: `#FFFFFF` shell, blue category block.
- **Border**: thin gray dividers and search border emphasis.

### Content Width

- **Prose max-width**: N/A - not an editorial/prose page.
- **Container max-width**: about 1100-1200px active desktop commerce canvas.
- **Sidebar width**: right floating rail about 95-102px based on CSS classes.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `max-width: 600px` | mobile-specific header/search and hidden desktop chrome |
| Tablet | `601px-768px` | intermediate layout with tablet search/header variants |
| Desktop | `769px-1024px` | desktop-adjacent tablet state |
| Large | `1025px-1499px` | standard desktop shell |
| Wide | `min-width: 1500px` inferred from adjacent range | large desktop adjustments |

### Touch Targets

- **Minimum tap size**: tokenized buttons include 26, 32, 38, 44, and 56px min-height steps.
- **Button height (mobile)**: at least 32-44px for primary header/control variants.
- **Input height (mobile)**: search field uses full-height header control behavior; captured desktop field is about 40px.

### Collapsing Strategy

- **Navigation**: desktop icon/account/cart and shortcut rail progressively hide or switch at `s600`, `s768`, `s1024`.
- **Grid columns**: product/promo grid collapses by breakpoint and available module width.
- **Sidebar**: right rail appears only at wider states; mobile prioritizes primary content/search.
- **Hero layout**: promotional image carousel remains image-first; auxiliary rails and side modules reduce before the central banner.

### Image Behavior

- **Strategy**: CDN image assets dominate; many modules use fixed creative sizes rather than fully fluid editorial images.
- **Max-width**: images are constrained by their module/card containers.
- **Aspect ratio handling**: ad creatives carry fixed production ratios; product cards rely on image CDN sizing.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Blue filled button**

| Spec | Value |
|---|---|
| Background | `#346AFF` |
| Text | `#FFFFFF` |
| Border | `#346AFF` |
| Radius | 4px |
| Sizes | 26px, 32px, 38px, 44px, 56px min-height token steps |
| Hover | darker tokenized blue via `--ui-c-Button-filled-hover` |
| Pressed | darker tokenized blue via `--ui-c-Button-filled-pressed` |
| Disabled | blue-gray background and muted text |

```html
<button class="coupang-button coupang-button--blue">검색</button>
```

### Badges

**Cart count / new marker**

| Spec | Value |
|---|---|
| Shape | circle or compact pill |
| Background | `#346AFF` for cart count, red family for urgency/new |
| Text | `#FFFFFF` |
| Radius | `999px` / 50% |
| Placement | absolute over icon or inline after shortcut label |

### Cards & Containers

**Product card**

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Border | `1px solid #DDDDDD` when structure is needed |
| Radius | 0-4px |
| Padding | 8-16px |
| Image | product/photo first |
| Title | 12-14px, 400 |
| Price/discount | 14px+, 700, red/black emphasis |
| Hover | link-level hover, not a heavy transform card hover |

### Navigation

**Header search module**

| Spec | Value |
|---|---|
| Container | flex row |
| Search border | `2px solid #346AFF` |
| Category selector | left segment, 12-14px |
| Input | 14px, white bg, no rounded capsule |
| Submit icon | blue search icon area |
| Adjacent icons | My Coupang and cart with 36-44px icon assets |

```html
<form class="product-search search-form">
  <a class="select--category__current">전체</a>
  <input class="headerSearchKeyword coupang-search" placeholder="찾고 싶은 상품을 검색해보세요!" />
  <button class="headerSearchBtn" type="submit">검색</button>
</form>
```

### Inputs & Forms

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Border | inherited from search form, usually `#346AFF` for primary search |
| Radius | 0 |
| Font | 14px Apple SD Gothic Neo |
| Placeholder | muted blue-gray |
| Focus | outline removed; border/ring handled by parent search shell |

### Hero Section

| Spec | Value |
|---|---|
| Type | promotion carousel / marketplace billboard |
| Background | light gray campaign surface |
| Text | embedded in campaign creative, very bold |
| CTA | image or coupon module driven |
| Right rail | coupon/product tiles on white cards |
| Motion | carousel fade/transform transitions |

### 13-2. Named Variants

**search-bar-primary**

| Spec | Value |
|---|---|
| Border | `2px solid #346AFF` |
| Height | about 40px desktop |
| Radius | 0 |
| Internal segments | category selector, keyword input, mic icon, submit icon |
| State | focus remains utility-like; no decorative glow |

**category-tile-blue**

| Spec | Value |
|---|---|
| Background | `#346AFF` |
| Text | `#FFFFFF` |
| Icon | hamburger/category mark |
| Radius | 0 |
| Function | global category entry point |

**right-rail-coupon-card**

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Border | blue top/header line plus gray dividers |
| Width | around 95-102px rail logic |
| Content | small image + two-line label |
| Shadow | floating rail shadow only when separated from content |

### 13-3. Signature Micro-Specs

```yaml
search-border-as-brand:
  description: "The search field is the brand-colored control, more important than generic CTA buttons on the homepage."
  technique: "rectangular segmented shell with border: 2px solid #346AFF /* {colors.ui-action-blue} */; height: about 40px; border-radius: 0"
  applied_to: ["{component.search-bar}", "{component.Navigation.Header search module}"]
  visual_signature: "Coupang reads as searchable inventory before it reads as a campaign page."

blue-category-control-slab:
  description: "A blue category block interrupts the white header as a permanent marketplace entry switch."
  technique: "background: #346AFF /* {colors.ui-action-blue} */; color: #FFFFFF; width: 110px; min-height: 120px; border-radius: 0; font-size: 12px; font-weight: 700"
  applied_to: ["{component.category-tile}", "{component.Navigation}"]
  visual_signature: "A control-room switch, not a polite nav pill."

floating-rail-only-shadow:
  description: "Elevation is reserved for overlays and side rails while product cards stay mostly flat."
  technique: "side rail shadow: 5px 0 5px #d1d1d1, -5px 0 5px #d1d1d1, 0 -3px 5px #d1d1d1; dropdown shadow: 0 4px 5px rgba(0,0,0,.3)"
  applied_to: ["{component.right-rail-coupon-card}", "{component.Navigation dropdowns}"]
  visual_signature: "The marketplace floor is cut by hairlines; only floating utility surfaces cast a visible shadow."

dense-button-size-ladder:
  description: "Buttons behave like an internal operations system with multiple compact height tokens."
  technique: "min-height ladder: 26px, 32px, 38px, 44px, 56px; radius: 4px; filled/outline blue states using #346AFF and tokenized hover/pressed colors"
  applied_to: ["{component.button-blue-md}", "{component.Buttons}"]
  visual_signature: "Operational consistency holds under visually noisy product and promotion modules."

campaign-color-quarantine:
  description: "Seasonal saturation lives inside ad and product imagery, not in the permanent UI shell."
  technique: "shell stays #FFFFFF /* {colors.ui-b-color-white} */ with #DDDDDD borders; hero uses light gray campaign band; saturation comes from CDN banner/product images"
  applied_to: ["{component.Hero Section}", "{component.product-card}", "{component.right-rail-coupon-card}"]
  visual_signature: "Supermarket flyer energy sits on top of a neutral logistics console without recoloring the platform chrome."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Header placeholder | direct task invitation | "찾고 싶은 상품을 검색해보세요!" |
| Promotion headline | urgent, benefit-first, large | "쿠폰이 지급되었습니다!" |
| Section title | discovery framing | "오늘의 발견" |
| Discount copy | numeric savings first | "지금 57% 할인 중" |
| Service copy | logistics promise | "로켓배송", "로켓프레시", "와우회원할인" |
| Tone | fast, practical, deal-oriented | benefit and inventory over brand poetry |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Coupang - copy into your root stylesheet */
:root {
  /* Fonts */
  --ui-font-family: "Apple SD Gothic Neo", "Noto Sans KR", "Roboto", "Helvetica Neue", Arial, sans-serif;
  --ui-font-family-code: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --ui-font-weight-normal: 400;
  --ui-font-weight-bold: 700;

  /* Brand / action */
  --ui-color-action-blue: #346AFF;
  --ui-color-link-blue: #4285F4;
  --ui-color-legacy-link-blue: #0073E9;
  --ui-color-urgency-red: #CB1400;
  --ui-color-danger-red: #AE0000;

  /* Surfaces */
  --ui-bg-page: #FFFFFF;
  --ui-bg-subtle: #FAFAFA;
  --ui-text: #212B36;
  --ui-text-strong: #111111;
  --ui-text-muted: #888888;
  --ui-border: #DDDDDD;

  /* Key spacing */
  --ui-space-2: 2px;
  --ui-space-4: 4px;
  --ui-space-8: 8px;
  --ui-space-12: 12px;
  --ui-space-16: 16px;
  --ui-space-24: 24px;

  /* Radius */
  --ui-radius-none: 0px;
  --ui-radius-sm: 4px;
  --ui-radius-md: 8px;
  --ui-radius-full: 999px;
}

body {
  margin: 0;
  background: var(--ui-bg-page);
  color: var(--ui-text);
  font-family: var(--ui-font-family);
  font-size: 14px;
  font-weight: var(--ui-font-weight-normal);
}

.coupang-header {
  display: flex;
  align-items: center;
  gap: 24px;
  background: #FFFFFF;
  border-bottom: 1px solid #DDDDDD;
}

.coupang-category-tile {
  width: 110px;
  min-height: 120px;
  display: grid;
  place-items: center;
  background: #346AFF;
  color: #FFFFFF;
  border-radius: 0;
  font-size: 12px;
  font-weight: 700;
}

.coupang-search {
  height: 40px;
  display: flex;
  align-items: center;
  flex: 1;
  background: #FFFFFF;
  border: 2px solid #346AFF;
  border-radius: 0;
}

.coupang-product-card {
  background: #FFFFFF;
  border: 1px solid #DDDDDD;
  border-radius: 0;
  padding: 12px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js - Coupang-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        coupang: {
          blue: '#346AFF',
          red: '#CB1400',
          link: '#4285F4',
          text: '#212B36',
          border: '#DDDDDD',
          surface: '#FFFFFF',
        },
      },
      fontFamily: {
        sans: ['Apple SD Gothic Neo', 'Noto Sans KR', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
      },
      borderRadius: {
        coupang: '4px',
        none: '0px',
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
| Brand/action primary | `{colors.ui-action-blue}` | `#346AFF` |
| Background | `{colors.ui-b-color-white}` | `#FFFFFF` |
| Text primary | `{colors.ui-text-primary}` | `#212B36` |
| Text strong | `{colors.ui-text-strong}` | `#111111` |
| Text muted | `{colors.ui-text-muted}` | `#888888` |
| Border | `{colors.ui-border-muted}` | `#DDDDDD` |
| Urgency/error | `{colors.ui-commerce-red}` | `#CB1400` |

### Example Component Prompts

#### Header Search

```text
Coupang style desktop header search module:
- white shell, compact Korean system typography
- left category selector, center input, right search icon
- border: 2px solid #346AFF
- height around 40px, border-radius 0
- input text: 14px Apple SD Gothic Neo, color #212B36
- no decorative shadow, no pill shape
```

#### Product Card

```text
Coupang style product card:
- background #FFFFFF, optional 1px #DDDDDD divider
- radius 0-4px, padding 8-12px
- product image first, title 12-14px weight 400
- price or discount emphasis weight 700
- use #CB1400 only for urgency or discount, not for general navigation
```

#### Marketplace Hero

```text
Coupang style marketplace hero:
- light gray promotional band, not a SaaS hero
- central campaign creative with very bold Korean text
- right rail coupon/product stack on #FFFFFF cards
- surrounding platform chrome remains neutral
- action blue #346AFF is reserved for controls, search, and category entry
```

#### Shortcut GNB

```text
Coupang style shortcut navigation:
- horizontal row of small icon + 12px label items
- compact spacing, white background
- no large rounded nav pills
- active or utility action can use #346AFF, but most labels stay #333333/#212B36
```

### Iteration Guide

- **색상 변경 시**: shell remains white/gray; put campaign color inside promo images or urgency labels only.
- **폰트 변경 시**: keep Korean readability first. Use Noto Sans KR fallback rather than a stylized display font.
- **여백 조정 시**: keep 8/12/16px density in product modules; use 24px+ only for major module breaks.
- **새 컴포넌트 추가 시**: default to rectangular controls and 4px radius, not rounded SaaS cards.
- **다크 모드**: no complete dark homepage mapping was observed; do not infer a dark theme from blue-gray tokens alone.
- **반응형**: honor 600/768/1024 breakpoint families and hide auxiliary rails before reducing the search-first header.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#346AFF` as the primary control/action blue for search, category entry, button states, and focus/ring moments.
- Keep primary marketplace surfaces on `#FFFFFF` with thin `#DDDDDD` borders.
- Let product photography and ad creatives carry most saturation and seasonal color.
- Use compact Korean system typography: 12px and 14px are core sizes, with 700 for category/price emphasis.
- Build the header as a functional control strip: category, logo, search, account, cart, shortcut row.
- Use 0-4px radius for most shell/card elements; reserve full radius for badges and counters.
- Use shadows for dropdowns, floating rails, and overlays rather than every product card.

### ❌ DON'T

- "Primary action을 `#0073E9`만으로 두지 말 것 — 대신 shell/action anchor는 `#346AFF` 사용"
- "Urgency/discount red를 관측된 보조 magenta `#D22E60`로 대체하지 말 것 — 대신 핵심 urgency는 `#CB1400` 또는 `#AE0000` 계열 사용"
- "텍스트를 `#000000` 또는 `black` 중심으로 두지 말 것 — 대신 `#212B36`, `#111111`, `#333333` 계층 사용"
- "border를 `#E5E7EB` 같은 generic Tailwind gray로 두지 말 것 — 대신 관측된 `#DDDDDD` 계열 사용"
- "검색창을 pill radius `999px`로 만들지 말 것 — Coupang primary search는 rectangular shell + `#346AFF` border다"
- "상품 카드 전체에 무거운 shadow를 깔지 말 것 — shadow는 overlay/rail에 집중하고 카드 구조는 border와 image로 만든다"
- "brand palette를 logo multi-color 전체로 UI에 뿌리지 말 것 — logo colors are not general UI tokens"
- "16px body 중심의 여유로운 SaaS scale로 키우지 말 것 — Coupang shell은 12px/14px 밀도 위에서 작동한다"

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **Single-color brand wash: zero** — 페이지 전체가 푸르게 물드는 일은 absent. 파랑은 control color일 뿐 background theme으로는 never 쓰인다.
- **Rounded SaaS capsule header: none** — 검색 컨트롤은 rectangular and segmented. pill chrome은 absent.
- **Editorial whitespace luxury: never** — product sections는 정보를 공격적으로 압축한다. 잡지같은 호흡은 zero.
- **Universal card elevation: absent** — shadow는 most grid cards에서 zero. card box-shadow는 never.
- **Decorative gradient system in shell: none** — gradients는 utility fades나 ad creative 안에서만, shell brand language로는 absent.
- **Weight 300 identity: absent** — system은 400/700 lean, 가끔 600/800. lightweight elegance는 zero, light-air 정체성은 never.
- **Second UI brand color: none** — red는 urgency와 logo support이지 navigation/action peer는 zero.
- **Prose-led storytelling: absent** — labels, prices, benefit fragments가 지배. 긴 문단 카피는 never.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage capture**: this guide is based on the existing `insane-design/coupang/` phase1 homepage artifacts. Checkout, login, seller, customer-service, and order-management flows were not visited.
- **Screenshot is desktop-first**: the visual interpretation used the available desktop hero crop. Mobile screenshots were not re-captured in this run.
- **Ad creative volatility**: hero and product imagery are time-sensitive campaign assets. The shell tokens are stable enough to document, but specific banner colors and copy can change frequently.
- **CSS includes legacy and new systems**: `--ui-b-*`, `--ui-c-*`, `--tw-*`, `fw-*`, and legacy selectors coexist. Some values are production leftovers rather than active visible UI.
- **No official design-system document was read**: `design_system_level: lv2` is inferred from production token structure, not from an official Coupang guidebook.
- **Dark mode incomplete**: no full dark theme mapping was observed on the homepage. Blue-gray/dark tokens should not be treated as a complete dark-mode spec.
- **Form validation states not surfaced**: search input and header controls were visible, but error/loading/success states for transactional forms were not captured.
- **Motion logic partially observed**: CSS transition values and carousel-related structures exist, but JavaScript timing, autoplay rules, and interaction states were not deeply traced.
- **Logo color separation is manual**: Coupang's logo uses multiple colors, but this guide intentionally treats those as brand-mark colors, not general UI colors.
