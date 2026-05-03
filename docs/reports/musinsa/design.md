---
schema_version: 3.2
slug: musinsa
service_name: MUSINSA
site_url: https://www.musinsa.com/
fetched_at: 2026-04-14T01:23:00+09:00
default_theme: mixed
brand_color: "#245EFF"
primary_font: Pretendard
font_weight_normal: 400
token_prefix: mds

bold_direction: Dense Commerce
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: commerce-marketplace
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Tailwind utility layer + MDS compatibility typography classes + repeated marketplace component states, but few semantic alias tokens."

colors:
  surface-page: "#FAFAFA"
  surface-section: "#F5F5F5"
  surface-base: "#FFFFFF"
  chrome-dark: "#1A1B1F"
  text-primary: "#000000"
  text-muted: "#666666"
  text-subtle: "#8A8A8A"
  border-default: "#E0E0E0"
  border-soft: "#EBEBEB"
  action-blue: "#245EFF"
  tooltip-blue: "#3A6EFF"

typography:
  display: "Pretendard"
  body: "Pretendard"
  ladder:
    - { token: text-etc-42, size: "42px", weight: 400, line_height: "48px", tracking: "0" }
    - { token: title-26, size: "26px", weight: 500, line_height: "32px", tracking: "0" }
    - { token: title-22, size: "22px", weight: 600, line_height: "28px", tracking: "0" }
    - { token: title-18, size: "18px", weight: 500, line_height: "24px", tracking: "0" }
    - { token: body-14, size: "14px", weight: 400, line_height: "20px", tracking: "0" }
    - { token: body-13, size: "13px", weight: 400, line_height: "18px", tracking: "0" }
    - { token: etc-11, size: "11px", weight: 400, line_height: "14px", tracking: "0" }
  weights_used: [400, 500, 600, 700]
  weights_absent: [300, 800, 900]

components:
  gnb-dark: { bg: "{colors.chrome-dark}", height: "56px", color: "rgba(255,255,255,.8)" }
  appbar-light: { bg: "{colors.surface-section}", height: "52px", padding: "12px 16px" }
  button-confirm: { bg: "{colors.text-primary}", color: "{colors.surface-base}", radius: "4px", height: "40px" }
  badge-count: { bg: "{colors.action-blue}", color: "{colors.surface-base}", radius: "18px", min_width: "16px" }
  fab-segmented-filter: { bg: "{colors.surface-base}", radius: "100px", height: "40px" }
---

# DESIGN.md — MUSINSA (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

MUSINSA is the canonical example of a fashion commerce-marketplace that operates through a monochrome store chassis, never through decorative brand spectacle. The top chrome is dark, compact, and operational; the page below is bright, dense, and image-led — a controlled split between the store counter and the showroom floor. The black header at #1A1B1F (`{colors.chrome-dark}`) frames the service as a management console, while product and campaign imagery carries the seasonal emotion.

The visual system is almost monochrome by default. The main identity is #000000 (`{colors.text-primary}`), #FFFFFF (`{colors.surface-base}`), #F5F5F5 (`{colors.surface-section}`), and #FAFAFA (`{colors.surface-page}`). #245EFF (`{colors.action-blue}`) is not a broad brand wash; it is a high-contrast utility signal for badges, dots, and small attention markers. There is no second brand color for the core store surface. The chromatic identity arrives in inventory, not chrome.

The page feels like a black checkout counter attached to a very bright stockroom. The 56px dark navigation is the cashier's rail: narrow, horizontal, and always in charge. Below it, #F5F5F5 (`{colors.surface-section}`) works like a fitting-room floor and #FFFFFF (`{colors.surface-base}`) becomes the clean shelf where search, cards, and dialogs sit. Campaign photography is the hanging garment; the interface is the rack hardware. The editorial rhythm is consistent: large campaign cards provide the visual pause, then the interface returns immediately to dense commerce.

Spacing is compressed but not sloppy. Navigation, tab rows, product chips, and footer cells use a strict 4px ladder with 13px and 14px body text. The feeling is less "hero page" and more "well-racked store wall": everything is reachable, categorized, and one click away. MUSINSA's craft is in operational consistency: 56px global navigation, 52px appbar, 40px floating buttons, 4px default radius, 1px hairlines, 13/14px list typography, and pill-like counters — a marketplace that keeps clearing space for products, rankings, and campaigns without breaking the store grid.

비유로 풀자면 MUSINSA는 단일 부티크가 아니라 거대한 패션 마켓과 그 뒤의 물류센터를 한 화면에 압축한 카탈로그다. 검정 GNB는 시장 입구의 통제실 카운터, 52px appbar는 매대 사이의 안내 표지판, 흰 카드들은 깔끔하게 정리된 진열대 한 칸, 검정 confirm 버튼은 카운터 위 결제 도장이다. 16px blue badge는 매장 천장에 달린 작은 LED 사이니지처럼 카운트만 알려주고, 캠페인 photography는 매대 위에 잠시 걸린 시즌 포스터 — 다음 주에 떼어내도 진열대 자체는 그대로 굴러가도록 설계됐다. 창고처럼 빽빽하지만 동선은 흐트러지지 않는다.

### Key Characteristics

- Dark global service bar at #1A1B1F with compact category and utility navigation.
- White search field and image-first hero content create the primary contrast against the dark top frame.
- Marketplace density: many tabs, panels, campaign tiles, product chips, and footer links are visible in one viewport.
- Neutral-first palette: #FAFAFA, #F5F5F5, #FFFFFF, #000000, #666666, and #E0E0E0 do nearly all structural work.
- #245EFF appears as a signal color for counts, notification dots, and small badges, not as a large background system.
- Pretendard is used as the Korean-first interface face; letter-spacing stays at 0 across utility classes.
- Radius is pragmatic: 4px for dialogs/buttons/cards, 8px for modals, 18px/100px for counters and segmented filters.
- Hairlines and subtle tinted borders (#8A8A8A1A, #E0E0E0, #EBEBEB) separate content instead of heavy shadows.
- Large campaign photography provides emotional color; UI chrome remains deliberately austere.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Dense Commerce
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **dark operations bar over dense fashion marketplace imagery**으로 기억된다.
> **Code Complexity**: high — Tailwind utilities, MDS compatibility classes, sticky/fixed chrome, modal/dialog/fab states, and multilingual typography variants combine into a broad commerce UI surface.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 MUSINSA처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Pretendard", "Apple SD Gothic Neo", sans-serif;
  font-weight: 400;
  font-size: 14px;
  line-height: 1.5;
  letter-spacing: 0;
}

/* 2. 배경 + 텍스트 */
:root {
  --musinsa-bg-page: #FAFAFA;
  --musinsa-bg-section: #F5F5F5;
  --musinsa-fg: #000000;
}
body { background: var(--musinsa-bg-page); color: var(--musinsa-fg); }

/* 3. 운영형 상단 chrome + 작은 signal blue */
:root {
  --musinsa-chrome: #1A1B1F;
  --musinsa-signal: #245EFF;
  --musinsa-border: #E0E0E0;
}
```

**절대 하지 말아야 할 것 하나**: MUSINSA를 파란 브랜드 UI로 만들지 말 것. #245EFF는 작은 badge/dot/signal에만 쓰이고, 화면의 실제 브랜드성은 black/white/gray와 campaign imagery에서 나온다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.musinsa.com/` |
| Canonical URL | `https://www.musinsa.com/main/musinsa/recommend` |
| Fetched | 2026-04-14T01:23:00+09:00 |
| Extractor | reused local phase1 artifacts; original collection included HTML, CSS, and hero screenshot |
| HTML size | 65,946 bytes (Next.js SSR payload) |
| CSS files | 5 files: `style.css`, `common-mobile.css`, `mds.css`, `4f0acaacad4c7f09.css`, `_inline.css` |
| Token prefix | `mds` plus Tailwind utility classes |
| Method | CSS custom properties, MDS compatibility classes, hex frequency, HTML store payload, and screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js SSR (`__N_SSP`, `page: /main/[[...slug]]`, static asset prefix)
- **Design system**: MDS/Tailwind hybrid — prefix `mds`, utility classes, and backward compatibility layer
- **CSS architecture**:
  ```text
  base reset       Tailwind v3.4.17 preflight + common layout reset
  utility layer    spacing/size/color/radius classes, responsive variants
  compatibility    .text-body_13px_reg, .text-title_22px_semi, .font-pretendard
  component layer  hashed module classes: _gnb_*, _appbar_*, _dialog_*, _menu_*, _fab_*
  ```
- **Class naming**: Tailwind utilities plus CSS module hashes (`._gnb__menu_5pcry_136`)
- **Default theme**: mixed; dark global navigation over light commerce contents
- **Font loading**: self-hosted Pretendard `@font-face` weights 400/500/600/700 from `image.msscdn.net`
- **Canonical anchor**: `main/musinsa/recommend`, a marketplace recommendation surface rather than a marketing landing page

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Pretendard` (self-hosted webfont)
- **Code font**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace`
- **Weight normal / bold**: `400` / `600` for most interface emphasis, with `700` rare

```css
@font-face {
  font-family: Pretendard;
  font-weight: 400;
  src: url("//image.msscdn.net/platform/fonts/Pretendard-Regular.woff2") format("woff2");
}
@font-face {
  font-family: Pretendard;
  font-weight: 500;
  src: url("//image.msscdn.net/platform/fonts/Pretendard-Medium.woff2") format("woff2");
}
@font-face {
  font-family: Pretendard;
  font-weight: 600;
  src: url("//image.msscdn.net/platform/fonts/Pretendard-SemiBold.woff2") format("woff2");
}
body {
  font-family: Pretendard, Apple SD Gothic Neo, sans-serif;
  font-size: 14px;
  color: #000000;
  line-height: 1.5;
}
```

### Note on Font Substitutes

- **Pretendard** is the correct primary substitute for Korean UI reproduction. If the hosted font is unavailable, use `system-ui` only after `Apple SD Gothic Neo` on macOS and keep the 13px/14px text classes intact.
- Do not compensate with negative tracking. MUSINSA's extracted utility classes keep `letter-spacing: 0`, so the substitute should preserve neutral Korean spacing rather than tightening headlines.
- If using Inter for a Latin-only prototype, reduce body weight emphasis: map 500 labels to 500, but keep body at 400 and line-height at 18px/20px for 13px/14px text.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `.text-etc_42px_reg` | 42px | 400 | 48px | 0 |
| `.text-title_26px_med` | 26px | 500 | 32px | 0 |
| `.text-title_22px_semi` | 22px | 600 | 28px | 0 |
| `.text-etc_22px_med` | 22px | 500 | 28px | 0 |
| `.text-title_20px_med` | 20px | 500 | 26px | 0 |
| `.text-title_18px_med` | 18px | 500 | 24px | 0 |
| `.text-title_18px_semi` | 18px | 600 | 24px | 0 |
| `.text-etc_16px_med` | 16px | 500 | 22px | 0 |
| `.text-body_14px_reg` | 14px | 400 | 20px | 0 |
| `.text-body_14px_med` | 14px | 500 | 20px | 0 |
| `.text-body_14px_semi` | 14px | 600 | 20px | 0 |
| `.text-body_13px_reg` | 13px | 400 | 18px | 0 |
| `.text-body_13px_med` | 13px | 500 | 18px | 0 |
| `.text-body_13px_semi` | 13px | 600 | 18px | 0 |
| `.text-etc_11px_reg` | 11px | 400 | 14px | 0 |
| `.text-etc_10px_reg` | 10px | 400 | 12px | 0 |
| `.text-etc_9px_med` | 9px | 500 | 11px | 0 |

> Key insight: the system is not headline-led. MUSINSA gets its identity from dense 13px/14px operational typography and campaign imagery, with large type used sparingly.

### Principles

1. Body density is anchored at 13px/14px, not 16px. This is the marketplace tell.
2. Letter-spacing stays at 0 across extracted text utilities; do not add editorial negative tracking.
3. Weight 500 is a real workhorse for tabs, labels, and navigation, while 600 marks active/current states.
4. 700 exists but should be rare; using it broadly makes the interface feel promotional instead of operational.
5. Multilingual variants adjust size for Japanese and Chinese, but the base Korean rhythm is Pretendard-first.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (signal, not broad brand wash)

| Token | Hex | Usage |
|---|---|---|
| `action-blue` | `#245EFF` | count badges, dots, compact notification signals |
| `tooltip-blue` | `#3A6EFF` | tooltip surfaces and arrow color |
| `legacy-blue` | payload-only blue | store-specific boutique payload / chromatic secondary |
| `sneaker-blue` | payload-only cyan | store-specific kicks/sneaker payload |

### 06-2. Dark Chrome

| Token | Hex | Usage |
|---|---|---|
| `chrome-dark` | `#1A1B1F` | global navigation background |
| `black` | `#000000` | primary text, confirm buttons, active filter cursor |
| `dim` | `rgba(0,0,0,.4)` | translucent dark separators and overlays |
| `hairline-dark` | `#0000001A` | subtle bottom line on dark nav |

### 06-3. Neutral Ramp

| Step | Hex | Usage |
|---|---|---|
| page | `#FAFAFA` | layout container background |
| section | `#F5F5F5` | appbar, menu tabs, light panels |
| footer | `#F0F0F0` | footer background |
| control-disabled | `#EBEBEB` | disabled backgrounds, default Tailwind border |
| border | `#E0E0E0` | button/dialog/menu hairline |
| placeholder | `#ccc` | placeholder and disabled text |
| muted | `#8A8A8A` | tertiary labels and subtle separators |
| secondary-text | `#666666` | descriptions, copyright, secondary links |
| dark-gray | `#4A4A4A` | utility dark gray |
| snackbar | `#2A2A2A` | snackbar surface |
| text | `#000000` | primary interface text |
| base | `#FFFFFF` | content surface, modal, product tiles |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| labelBlue | active signal | `#3A6EFF` |
| labelRed | alert/sale | `#F73C3B` |
| red | error/sale | `#F31110` |
| outlet | store theme | `#B90000` |
| yellow | used/special | `#FA9200` |
| used-store | store theme | `#F7E74B` |
| sports | store theme | `#37B0F4` |
| kids | store theme | payload-only violet |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--layout-bg-color` | `#FAFAFA` | outer layout floor |
| `--layout-bg-contents-color` | `#F5F5F5` / `#FFFFFF` | main content surface, switched by body data attribute |
| `--tw-ring-offset-color` | `#FFFFFF` | Tailwind focus ring offset |
| `--tw-ring-color` | `rgba(59,130,246,.5)` | Tailwind ring fallback; not a MUSINSA brand token |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--layout-bg-color` | `#FAFAFA` | app shell background |
| `--layout-bg-contents-color` | `#F5F5F5` | default contents background |
| `body[data-layout-background=white] --layout-bg-contents-color` | `#FFFFFF` | white content mode |
| `--max-width` | `1440px` | app shell maximum width |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Hex | Frequency | Kind |
|---|---:|---|
| `#000000` | 36 | neutral |
| `#FFFFFF` | 25 | neutral |
| `#0000` | 16 | transparent neutral |
| `#666666` | 15 | neutral |
| `#F5F5F5` | 12 | neutral |
| `#E0E0E0` | 11 | neutral |
| `#245EFF` | 8 | chromatic signal |
| `#8A8A8A` | 7 | neutral |
| `#EBEBEB` | 6 | neutral |
| `#3A6EFF` | 5 | chromatic signal |

### 06-8. Color Stories

**`{colors.text-primary}` (`#000000`)** — The real primary color. It defines active tabs, confirm buttons, filter cursors, text, and the marketplace's practical authority.

**`{colors.surface-section}` (`#F5F5F5`)** — The operating floor. Appbars, menu tab backgrounds, and many utility panels use this off-white gray so white cards and imagery can sit forward.

**`{colors.surface-base}` (`#FFFFFF`)** — The content surface. Dialogs, cards, FAB filters, and search fields use white to stay clean inside a very dense product environment.

**`{colors.action-blue}` (`#245EFF`)** — A small but sharp signal. It should appear as cart counts, dots, or notification markers; using it as a large brand fill misreads the system.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Use case |
|---|---:|---|
| base quantum | 4px | smallest repeated unit across gap/margin/padding utilities |
| `gap-1` | 4px | footer nav, compact button groups |
| `gap-2` | 8px | appbar utils, paired icons/text |
| `gap-3` | 12px | FAB vertical spacing, category grid row gaps |
| `gap-4` | 16px | form groups, side padding, menu sections |
| `gap-6` | 24px | larger commerce groups |
| `gap-8` | 32px | expanded section rhythm |
| appbar padding | 12px 16px | light appbar interior |
| dialog padding | 20px 16px / 24px 16px 20px | dialog title and button stack |
| footer padding | 15px 0 72px | footer top and bottom safe area |
| category body padding | 0 16px | menu category grids |

**주요 alias**:
- `--max-width` → 1440px (app shell width)
- `--min-width` → 744px (desktop shell lower bound)
- `--layout-header-top` → 56px (sticky header offset)
- `--layout-padding-top` → 56px (content offset)

### Whitespace Philosophy

MUSINSA uses whitespace as inventory management, not luxury breathing room. The page lets the hero imagery breathe just enough to sell the campaign, then immediately compresses into tabs, chips, cards, and rows. The system's "air" is measured in 4px, 8px, 12px, and 16px increments because commerce scanning beats editorial pause.

The wide shell is still disciplined: 1440px max-width, 744px min-width, and 1px vertical boundary lines at large desktop sizes. That frame keeps dense content from feeling unbounded while preserving the sense of a full marketplace wall.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Context |
|---|---:|---|
| checkbox micro radius | 1.5px | marketing agreement checkbox |
| default control radius | 4px | dialogs, buttons, tooltip boxes, footer nav blocks |
| modal radius | 8px | modal/dialog shells |
| cart badge radius | 18px | compact count badge |
| circular icon radius | 100% | FAB buttons, dots, icon pills |
| segmented filter radius | 100px | floating global filter shell |
| cursor pill radius | 40px | open segmented filter cursor |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: 1440px via `--max-width`
- **Min-width**: 744px for desktop layout shell
- **Grid type**: hybrid; Tailwind grid utilities plus component-level CSS modules
- **Column count**: product/category modules use 2, 3, and 6-column utilities; footer business info uses 5 columns
- **Gutter**: 4px to 16px in dense commerce modules, 20px for footer SNS row

### Hero

- **Pattern Summary**: compact dark chrome + white search + horizontal tabs + three-column image campaign hero + product chips below
- Layout: marketplace hero, not centered landing hero; primary content is image tiles with text overlays
- Background: hero imagery supplies visual color while UI surfaces remain neutral
- **Background Treatment**: image-led with no decorative gradient mesh in the UI chrome
- H1: campaign copy appears in image modules; UI text is mostly 13px/14px/16px operational typography
- Max-width: 1440px shell

### Section Rhythm

```css
#commonLayoutContainer {
  max-width: 1440px;
  min-width: 744px;
  background-color: #FAFAFA;
}
#commonLayoutGnb { height: 56px; }
._appbar_qtzt1_9 { height: 52px; padding: 12px 16px; background-color: #F5F5F5; }
```

### Card Patterns

- **Card background**: #FFFFFF for true cards, #F5F5F5 for panel sections, image surfaces for campaign tiles
- **Card border**: 1px solid #E0E0E0 or #EBEBEB; subtle #8A8A8A1A for section separators
- **Card radius**: mostly 4px, with image chip cards using small controlled rounding
- **Card padding**: 8px/12px/16px depending on density
- **Card shadow**: generally absent; Tailwind `hover:shadow-xl` exists but MUSINSA's core chrome relies on border and surface contrast

### Navigation Structure

- **Type**: horizontal global nav plus tabbed marketplace nav
- **Position**: global nav sticky at top; common header sticky/fixed/static by body data attribute
- **Height**: 56px global nav, 52px appbar
- **Background**: #1A1B1F global, #F5F5F5 appbar
- **Border**: 1px dark alpha line in global nav; #E0E0E0 / #8A8A8A1A hairlines in menus and footers

### Content Width

- **Prose max-width**: N/A; this is not a prose-first site
- **Container max-width**: 1440px
- **Sidebar width**: 108px menu main column in category menu; modal menu width 600px

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Small | 640px | Tailwind container and basic small-row adjustments |
| Tablet | 768px | Tailwind container step |
| Nav compact lower | 779px max | GNB text/icon sizes compress to 11px/14px |
| Nav compact upper | 780px-1279px | GNB spacing and typography reduce |
| Desktop | 1024px | Tailwind container step |
| Wide | 1280px | utility container step and non-compact nav |
| Shell max | 1440px | fixed shell boundary appears |
| Large | 1536px | Tailwind container step, though app shell remains 1440px |

### Touch Targets

- **Minimum tap size**: 40px for FAB/filter controls; 44px appears in button/marketing agreement contexts.
- **Button height (mobile/compact)**: 36px for error retry, 40px for dialog/FAB/filter, 44px for agreement action.
- **Input height (mobile/compact)**: not fully observed in this page; placeholder styles show 14px body rhythm.

### Collapsing Strategy

- **Navigation**: shrink padding and font sizes before hiding; some icon labels disappear below 1280px.
- **Grid columns**: utility grid supports 2/3/6 columns; menu category grid uses 3 columns inside modal surface.
- **Sidebar**: category menu main column fixed at 108px in observed modal.
- **Hero layout**: screenshot shows desktop multi-column hero; mobile flow not directly measured in this phase.

### Image Behavior

- **Strategy**: product/campaign imagery carries mood and is contained by grid/card modules.
- **Max-width**: Tailwind reset sets `img, video { max-width: 100%; height: auto; }`.
- **Aspect ratio handling**: category image wraps use `aspect-ratio: 5/6` with `object-fit: contain`.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

#### Confirm Button

```html
<button class="_dialog-button_uru6o_70 _dialog-button__confirm_uru6o_93">확인</button>
```

| Property | Value |
|---|---|
| Height | 40px |
| Padding | 0 15px |
| Radius | 4px |
| Border | 1px solid #000000 |
| Background | #000000 |
| Text | #FFFFFF, 14px, weight 500, line-height 20px |
| State | disabled states use #EBEBEB / #ccc in related controls |

#### Secondary / Cancel Button

```html
<button class="_dialog-button_uru6o_70 _dialog-button__cancel_uru6o_90">취소</button>
```

| Property | Value |
|---|---|
| Border | 1px solid #E0E0E0 |
| Background | transparent / #FFFFFF context |
| Text | #000000 |
| Radius | 4px |

### Badges

#### Count Badge

```html
<span class="_gnb__menu-cart_5pcry_170">2</span>
```

| Property | Value |
|---|---|
| Display | inline-flex center |
| Height | 16px |
| Min-width | 16px |
| Padding | 0 4px |
| Background | #245EFF |
| Radius | 18px |
| Text | #FFFFFF, 11px |

#### Dot Badge

```html
<span class="_appbar__button-dot_qtzt1_75"></span>
```

| Property | Value |
|---|---|
| Size | 4px x 4px |
| Background | #245EFF |
| Radius | 100% |
| Position | absolute top/right |

### Cards & Containers

#### Modal Container

```html
<section class="_modal_uru6o_10">...</section>
```

| Property | Value |
|---|---|
| Width | 480px |
| Max-height | 700px |
| Padding-top | 12px |
| Radius | 8px |
| Background | #FFFFFF |
| Position | fixed center |
| Z-index | 230 |

#### Commerce Shell

```html
<div id="commonLayoutContainer">...</div>
```

| Property | Value |
|---|---|
| Width | 100% |
| Min / Max | 744px / 1440px |
| Background | #FAFAFA |
| Layout | flex column, min-height 100% |

### Navigation

#### Global Navigation

```html
<nav class="_gnb_5pcry_2">...</nav>
```

| Property | Value |
|---|---|
| Height | 56px via `#commonLayoutGnb` |
| Background | #1A1B1F |
| Text color | rgba white for muted chrome text |
| Padding | 0 10px 0 4px |
| Separator | 1px #0000001A bottom line |
| Responsive | padding and font-size shrink below 1280px and 780px |

#### Appbar

```html
<header class="_appbar_qtzt1_9">...</header>
```

| Property | Value |
|---|---|
| Height | 52px |
| Padding | 12px 16px |
| Background | #F5F5F5 |
| Title | 16px, weight 500, ellipsis |
| Utils gap | 8px |

### Inputs & Forms

#### Agreement Button Pair

```html
<button class="_marketingAgreement__button_1p4nh_55">동의</button>
```

| Property | Value |
|---|---|
| Height | 44px |
| Border | 1px solid #E0E0E0 |
| Radius | 4px |
| Font | 14px / 20px |
| Confirm state | #000000 background, #FFFFFF text |
| Disabled state | #EBEBEB background, #ccc text |

#### Checkbox

```html
<span class="_marketingAgreement__icon_1p4nh_15"></span>
```

| Property | Value |
|---|---|
| Size | 15px x 15px |
| Border | 1px solid #EBEBEB |
| Radius | 1.5px |
| Checked | #000000 background and border |

### Hero Section

The homepage hero is a marketplace composition rather than a single component class in the captured CSS. Recreate it as:

```html
<section class="musinsa-hero">
  <nav class="musinsa-pan-tabs">콘텐츠 추천 랭킹 세일 ...</nav>
  <div class="musinsa-campaign-grid">
    <article class="musinsa-campaign-card">...</article>
    <article class="musinsa-campaign-card">...</article>
    <article class="musinsa-campaign-card">...</article>
  </div>
  <div class="musinsa-product-chip-grid">...</div>
</section>
```

| Property | Value |
|---|---|
| Hero rhythm | dark top chrome, white search, tabs, then image grid |
| Campaign card text | white overlay text on image, heavy enough for image contrast |
| Product chips | small rectangular product cards below, dense row rhythm |
| Background | neutral page with imagery carrying color |

### 13-2. Named Variants

#### `gnb-dark`

- Background #1A1B1F, height 56px, compact horizontal category links.
- Use muted white text as rgba alpha for secondary links and pure white only for emphasis.
- Keep separators thin; use #0000001A or alpha white rules, not thick borders.

#### `appbar-light`

- Background #F5F5F5, height 52px, padding 12px 16px.
- Title is 16px weight 500 with ellipsis.
- Utility icon buttons are 28px square.

#### `button-confirm-black`

- Height 40px, radius 4px, #000000 fill, #FFFFFF text.
- This is the core action style for dialogs and agreements.

#### `badge-signal-blue`

- #245EFF fill, #FFFFFF text, 16px height or 4px dot depending on information density.
- Use only for small counters/dots; never as a wide CTA fill.

#### `fab-segmented-filter`

- 40px high, #FFFFFF shell, 100px radius, #E0E0E0 outline.
- Active cursor is #000000, circular or pill depending on open state.

### 13-3. Signature Micro-Specs

```yaml
dense-neutral-commerce-chrome:
  description: "Dark operation rail over bright marketplace inventory."
  technique: "#1A1B1F global nav at 56px + #F5F5F5 appbar at 52px + #FFFFFF search/content fields; 1px #0000001A nav separator."
  applied_to: ["{component.gnb-dark}", "{component.appbar-light}", "{component.commerce-shell}"]
  visual_signature: "A black retail control bar sits above a pale product floor instead of becoming a colored brand header."

micro-blue-signal-system:
  description: "Blue is used as a small operational signal, not a brand wash."
  technique: "#245EFF on 16px min-width count badges with 18px radius and 4px absolute notification dots with 100% radius."
  applied_to: ["{component.badge-count}", "{component.badge-signal-blue}", "{component.appbar-light}"]
  visual_signature: "Tiny blue inventory lights flash inside an otherwise black, white, and gray commerce UI."

four-pixel-retail-ladder:
  description: "Dense store-wall spacing held together by a strict 4px rhythm."
  technique: "4px base quantum; repeated 4px/8px/12px/16px gaps, appbar padding 12px 16px, compact button groups, menu rows, and footer nav gaps."
  applied_to: ["{component.appbar-light}", "{component.fab-segmented-filter}", "{component.commerce-shell}"]
  visual_signature: "High item density feels measured like rack spacing rather than cramped like arbitrary packing."

pretendard-zero-tracking-interface:
  description: "Korean commerce readability through small type, neutral tracking, and medium-weight states."
  technique: "Pretendard 13px/14px classes with line-height 18px/20px, weights 400/500/600, and letter-spacing: 0 across extracted utilities."
  applied_to: ["{component.gnb-dark}", "{component.appbar-light}", "{component.button-confirm}"]
  visual_signature: "Operational labels stay crisp and scannable without editorial negative tracking."

pill-filter-black-cursor:
  description: "Floating filters behave like compact retail toggles with a black active cursor."
  technique: "40px high #FFFFFF segmented shell, 100px radius, #E0E0E0 outline, active cursor #000000 with 40px pill/circle radius."
  applied_to: ["{component.fab-segmented-filter}"]
  visual_signature: "A small white pill control with a black selection bead floats over dense product browsing."
```

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* MUSINSA — copy into your root stylesheet */
:root {
  /* Fonts */
  --musinsa-font-family: Pretendard, "Apple SD Gothic Neo", sans-serif;
  --musinsa-font-family-code: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --musinsa-font-weight-normal: 400;
  --musinsa-font-weight-medium: 500;
  --musinsa-font-weight-semibold: 600;

  /* Surfaces */
  --musinsa-bg-page: #FAFAFA;
  --musinsa-bg-section: #F5F5F5;
  --musinsa-bg-base: #FFFFFF;
  --musinsa-bg-footer: #F0F0F0;
  --musinsa-chrome-dark: #1A1B1F;

  /* Text */
  --musinsa-text-primary: #000000;
  --musinsa-text-secondary: #666666;
  --musinsa-text-subtle: #8A8A8A;
  --musinsa-text-disabled: #ccc;

  /* Signal */
  --musinsa-action-blue: #245EFF;
  --musinsa-tooltip-blue: #3A6EFF;

  /* Structure */
  --musinsa-border-default: #E0E0E0;
  --musinsa-border-soft: #EBEBEB;
  --musinsa-hairline-alpha: #8A8A8A1A;
  --musinsa-max-width: 1440px;
  --musinsa-min-width: 744px;

  /* Spacing */
  --musinsa-space-1: 4px;
  --musinsa-space-2: 8px;
  --musinsa-space-3: 12px;
  --musinsa-space-4: 16px;
  --musinsa-space-6: 24px;
  --musinsa-space-8: 32px;

  /* Radius */
  --musinsa-radius-sm: 4px;
  --musinsa-radius-md: 8px;
  --musinsa-radius-pill: 100px;
}

body {
  margin: 0;
  background: var(--musinsa-bg-page);
  color: var(--musinsa-text-primary);
  font-family: var(--musinsa-font-family);
  font-size: 14px;
  line-height: 1.5;
}

.musinsa-shell {
  width: 100%;
  min-width: var(--musinsa-min-width);
  max-width: var(--musinsa-max-width);
  margin: 0 auto;
  background: var(--musinsa-bg-page);
}

.musinsa-gnb {
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 10px 0 4px;
  background: var(--musinsa-chrome-dark);
  color: rgba(255,255,255,.8);
  border-bottom: 1px solid #0000001A;
}

.musinsa-appbar {
  height: 52px;
  display: flex;
  align-items: center;
  padding: 12px 16px;
  background: var(--musinsa-bg-section);
  box-sizing: border-box;
}

.musinsa-button-primary {
  height: 40px;
  padding: 0 15px;
  border: 1px solid #000000;
  border-radius: 4px;
  background: #000000;
  color: #FFFFFF;
  font: 500 14px/20px var(--musinsa-font-family);
}

.musinsa-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 16px;
  height: 16px;
  padding: 0 4px;
  border-radius: 18px;
  background: #245EFF;
  color: #FFFFFF;
  font-size: 11px;
  line-height: 1;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — MUSINSA-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        musinsa: {
          page: '#FAFAFA',
          section: '#F5F5F5',
          base: '#FFFFFF',
          chrome: '#1A1B1F',
          black: '#000000',
          gray600: '#666666',
          gray500: '#8A8A8A',
          gray400: '#ccc',
          gray300: '#E0E0E0',
          gray200: '#EBEBEB',
          blue: '#245EFF',
          tooltipBlue: '#3A6EFF',
        },
      },
      fontFamily: {
        sans: ['Pretendard', 'Apple SD Gothic Neo', 'sans-serif'],
      },
      borderRadius: {
        musinsa: '4px',
        'musinsa-modal': '8px',
        'musinsa-pill': '100px',
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
| Brand/signal | `{colors.action-blue}` | `#245EFF` |
| Background | `{colors.surface-page}` | `#FAFAFA` |
| Section surface | `{colors.surface-section}` | `#F5F5F5` |
| Card/modal surface | `{colors.surface-base}` | `#FFFFFF` |
| Dark chrome | `{colors.chrome-dark}` | `#1A1B1F` |
| Text primary | `{colors.text-primary}` | `#000000` |
| Text muted | `{colors.text-muted}` | `#666666` |
| Border | `{colors.border-default}` | `#E0E0E0` |
| Disabled | `{colors.border-soft}` | `#EBEBEB` |

### Example Component Prompts

#### Hero Section

```text
MUSINSA 스타일 커머스 홈 히어로를 만들어줘.
- 상단 chrome: #1A1B1F, 56px height, compact horizontal nav
- 검색 영역: #FFFFFF input on #F5F5F5 appbar, 52px appbar height
- 탭: 13px/14px Pretendard, active weight 600, inactive #666666 or muted
- 히어로: 3-column campaign image grid, white overlay text, no decorative gradient UI background
- 하단: dense product chip grid with 4px/8px gaps and light #E0E0E0 borders
```

#### Card Component

```text
MUSINSA 스타일 상품/캠페인 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF 또는 이미지 surface
- border: 1px solid #E0E0E0 or subtle #8A8A8A1A separator
- radius: 4px
- padding: 8px to 16px, based on density
- 제목: Pretendard 13px or 14px, weight 500/600
- 본문: #666666, 13px, line-height 18px
- hover: underline or slight opacity change only; avoid heavy shadow as default
```

#### Badge

```text
MUSINSA 스타일 signal badge를 만들어줘.
- background: #245EFF
- color: #FFFFFF
- height: 16px, min-width: 16px, padding 0 4px
- radius: 18px
- font-size: 11px, line-height: 1
- dot variant: 4px by 4px, radius 100%, same #245EFF
```

#### Navigation

```text
MUSINSA 스타일 네비게이션을 만들어줘.
- global nav: #1A1B1F background, height 56px, sticky top
- appbar: #F5F5F5 background, height 52px, padding 12px 16px
- links: Pretendard 13px/14px, weight 500
- active tabs: #000000, weight 600, 2px underline when tabbed
- secondary links: #666666 or rgba white in dark chrome
```

### Iteration Guide

- **색상 변경 시**: neutral structure first. Keep #000000/#FFFFFF/#F5F5F5 dominant and reserve #245EFF for small signals.
- **폰트 변경 시**: preserve the 13px/14px body ladder and `letter-spacing: 0`.
- **여백 조정 시**: stay on 4px increments; arbitrary 13px/27px spacing will break the retail rhythm.
- **새 컴포넌트 추가 시**: start with 4px radius, 1px #E0E0E0 border, and no default shadow.
- **모달/다이얼로그**: use 480px width, 8px shell radius, 40px action buttons where the desktop pattern applies.
- **반응형**: shrink nav typography/padding before removing content; MUSINSA favors persistence over dramatic layout collapse.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #1A1B1F for the global top operation bar and keep it compact.
- Use #FAFAFA and #F5F5F5 as the page and section floor, with #FFFFFF for cards, dialogs, and search fields.
- Use #245EFF as a small attention signal for dots, counters, and badges.
- Keep core type at Pretendard 13px/14px with 18px/20px line-height.
- Use 4px as the default control radius and 100px/100% only for pills and circular controls.
- Separate dense modules with 1px hairlines such as #E0E0E0, #EBEBEB, or #8A8A8A1A.
- Let campaign/product imagery provide color and mood instead of coloring the UI chrome.

### ❌ DON'T

- 배경을 `#FFFFFF` 단독 full-page floor로 두지 말 것 — 대신 shell/page에는 `#FAFAFA`, panels에는 `#F5F5F5`, cards에는 `#FFFFFF`를 분리해 사용.
- 텍스트를 `#2A2A2A` 또는 `#4A4A4A` primary로 승격하지 말 것 — MUSINSA의 primary text and action base는 `#000000`.
- 브랜드 컬러를 `#245EFF` full-width CTA나 hero background로 쓰지 말 것 — 대신 `#245EFF`는 16px badge, 4px dot, compact signal에만 사용.
- neutral border를 `#F5F5F5` 중심으로 일반화하지 말 것 — 관측된 기본 hairline은 `#E0E0E0`, soft border는 `#EBEBEB`, alpha separator는 `#8A8A8A1A`.
- global nav를 `#FFFFFF` light nav로 만들지 말 것 — MUSINSA shell의 첫 인상은 `#1A1B1F` dark chrome.
- body에 `font-weight: 300` 사용 금지 — Pretendard 400/500/600 중심의 운영형 밀도가 맞다.
- display heading에 negative letter-spacing을 넣지 말 것 — 추출된 typography ladder는 `letter-spacing: 0`.
- 카드에 기본 `box-shadow`를 크게 넣지 말 것 — border/surface contrast가 먼저이고 shadow는 hover utility에서만 제한적으로 사용.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second primary brand color: **none** for the main store surface — core UI is monochrome plus a single tiny #245EFF signal.
- Decorative gradient chrome: **absent** — store payloads can carry color, but chrome never becomes a gradient object.
- Editorial oversized typography: **absent** — system rarely depends on giant text; image-led 카탈로그 modules do the selling.
- Rounded lifestyle SaaS cards: **absent** — default radius is 4px, never 12px/16px SaaS rounding.
- Heavy default shadows: **zero** — hairlines and surface steps replace depth.
- Wide blue CTA language: **absent** — black confirm buttons and neutral controls dominate the marketplace 매대.
- Negative tracking: **none** in extracted type utilities — letter-spacing is zero across the board.
- Open whitespace luxury: **never** — MUSINSA spends space on inventory visibility and 진열대 density.
- Generic landing-page centered hero: **absent** — first screen is a functional marketplace stack, not a marketing splash.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage state** — Analysis reused captured `main/musinsa/recommend` artifacts. Ranking, sale, release, checkout, and product detail flows may expose additional states.
- **Desktop screenshot primary** — The provided hero screenshot is desktop-width. Responsive behavior is inferred from CSS media queries and classes, not from a fresh mobile screenshot.
- **CSS module hashes are build-specific** — Component class names such as `._gnb_5pcry_2` are useful evidence, but should not be treated as stable public API.
- **Semantic token layer is shallow** — Only a few custom properties resolve cleanly (`--layout-bg-color`, `--layout-bg-contents-color`, Tailwind ring vars). Many design decisions are encoded as utility classes and module CSS rather than named tokens.
- **Store colors can pollute brand inference** — boutique blue, outlet red, kicks cyan, used yellow, sports blue, and kids violet appear in store payloads. They are documented as store accents, not the main MUSINSA UI brand color.
- **Motion details are incomplete** — CSS keyframes for spin, pulse, accordion, and fillProgress are visible, but JS scroll/interaction timing was not analyzed.
- **Form validation states are partial** — Focus/error/disabled classes are visible, but full login, checkout, and payment validation flows were not visited.
- **Image treatment is screenshot-derived** — Campaign image art direction changes frequently. The stable design rule is image-led color with neutral UI chrome, not the specific photographed campaigns.
