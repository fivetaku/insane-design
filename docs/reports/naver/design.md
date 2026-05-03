---
schema_version: 3.2
slug: naver
service_name: NAVER
site_url: https://www.naver.com/
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: light
brand_color: "#03C75A"
primary_font: "-apple-system / BlinkMacSystemFont / Malgun Gothic"
font_weight_normal: 400
token_prefix: naver

bold_direction: Portal Utility
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: other
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "1605 CSS variables, resolved light/dark token pairs, breakpoint tokens, and repeated search/widget/card component patterns."

colors:
  primary: "#03C75A"
  primary-active: "#03A94D"
  surface: "#FFFFFF"
  page: "#F0F0F0"
  text: "#101010"
  text-muted: "#8C8C8C"
  hairline: "#E5E5E5"
  link-blue: "#0147B5"
typography:
  display: "-apple-system / BlinkMacSystemFont / Malgun Gothic"
  body: "-apple-system / BlinkMacSystemFont / Malgun Gothic"
  specialty: "NanumSquare"
  ladder:
    - { token: search-placeholder, size: "22px", weight: 400, tracking: "0" }
    - { token: card-title, size: "16px", weight: 700, tracking: "-0.3px" }
    - { token: body, size: "14px", weight: 400, tracking: "0" }
    - { token: caption, size: "12px", weight: 500, tracking: "-0.28px" }
  weights_used: [300, 400, 500, 600, 700, 800, 900]
  weights_absent: []
components:
  search-pill: { border: "1px solid #03C75A", radius: "30px", height: "58px" }
  login-primary: { bg: "{colors.primary}", radius: "4px", height: "56px" }
  portal-card: { bg: "{colors.surface}", border: "1px solid #E5E5E5", radius: "8px" }
  shortcut-icon: { bg: "{colors.surface}", radius: "14px", shadow: "0 1px 2px rgba(0,0,0,.06)" }
---

# DESIGN.md - NAVER

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

NAVER reads like a civic **dashboard** built on a public-utility **canvas**. Search is the ceremonial center, and the surrounding surface is a dense utility grid — closer to the front desk of a very busy public building than to a branded **editorial** spread. The broad white **canvas** gives every visitor one calm counter, then the `#03C75A` (`{colors.primary}`) search pill tells the entire city where to speak first. That single outline-and-icon color does nearly all brand work while the rest of the page stays procedural.

The site's craft is in compression. Shortcuts sit as small square icons, cards have thin hairlines, and news/shop/widget modules stack without dramatic section breaks. It is closer to a newspaper kiosk wired into a control panel than to a **broadsheet** cover: many doors are visible at once, but the signage is disciplined. The page avoids **editorial** spectacle because the product is not one story; it is a daily command surface. Every module is allowed to be visible at once, but almost none is allowed to shout louder than search.

The palette is mostly administrative: `#FFFFFF` (`{colors.surface}`), `#F0F0F0` (`{colors.page}`), `#101010` (`{colors.text}`), and gray captions around `#8C8C8C` (`{colors.text-muted}`). Chromatic color appears in service identity chips and topic filters like subway line colors on a neutral station map — a **gallery** of route labels rather than mood lighting. News blue `#0147B5` (`{colors.link-blue}`), entertainment magenta, shopping yellow, and webtoon green are section identifiers, not global accents. There is no second global brand color.

The page's **dashboard** identity matters as much as its visible parts. No cinematic hero, no full-bleed photography, no manifesto headline, no luxury whitespace. The white cards are panels, hairlines are seams, and the green command ring is the one lit button you cannot miss. The search placeholder is intentionally large and pale, like a blank form field waiting at the counter; news and widget labels are smaller, darker, and tightly tracked. The page does not ask to be admired as a composition — it gets out of the way by becoming infrastructure. Its atmosphere is not minimalism, but regulated abundance: a portal city block where every storefront is small, labeled, and open.

### Key Characteristics

- Search-first composition: a 58px high central pill is the visual anchor.
- One brand color: #03C75A performs logo, search action, and login emphasis.
- Dense service grid: shortcut icons, newsstand logos, widgets, ads, and login sit in one viewport.
- Card chassis: white rounded rectangles with #E5E5E5 hairlines and light shadows.
- Local chromatic categories: blue, magenta, yellow, red, and green are section identifiers, not global accents.
- Korean readability stack: system UI plus Malgun Gothic and occasional NanumSquare.
- Tiny optical corrections: frequent -0.28px to -0.6px tracking on compact labels.
- Motion is functional: easing/duration tokens exist, but homepage identity is static and scannable.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Portal Utility
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **central green search command surface**으로 기억된다.
> **Code Complexity**: high — many tokenized color states, dark/light mappings, widgets, and dense component variants.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 NAVER처럼 만들기 - 3가지만 하면 80%

```css
/* 1. Font + Korean portal density */
body {
  font-family: -apple-system, BlinkMacSystemFont, "Malgun Gothic", "맑은 고딕",
    Helvetica, "Apple SD Gothic Neo", sans-serif;
  font-weight: 400;
  letter-spacing: 0;
}

/* 2. Page floor + card chassis */
:root {
  --naver-page: #F0F0F0;
  --naver-surface: #FFFFFF;
  --naver-text: #101010;
  --naver-hairline: #E5E5E5;
}

/* 3. Search and primary action green */
:root { --naver-green: #03C75A; }
.search-pill {
  height: 58px;
  border: 1px solid var(--naver-green);
  border-radius: 30px;
  background: #FFFFFF;
}
```

**절대 하지 말아야 할 것 하나**: NAVER를 generic SaaS hero처럼 만들지 말 것. 중앙 H1/CTA 랜딩 페이지가 아니라, search pill + shortcut rail + card grid가 첫 화면의 본체다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.naver.com/` |
| Fetched | phase1 cache from 2026-04-14, screenshot refreshed 2026-04-23, guidebook written 2026-05-03 |
| Extractor | cached HTML/CSS + phase1 token JSON + screenshot observation |
| HTML size | 209096 bytes |
| CSS files | 2 files, 791546 characters |
| Token prefix | `naver` |
| Method | CSS variable parsing, frequency count, screenshot interpretation; no invented hex values |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: server-rendered portal HTML with module-scoped CSS class names.
- **Design system**: NAVER home token layer - prefix-like variables include `--color-*`, `--core-color-*`, `--sizes-*`, `--breakpoints-*`, `--duration-*`, and `--easing-*`.
- **CSS architecture**:
  ```text
  core       (--core-color-*)                 raw hex values and alpha colors
  semantic   (--color-neutral-* / primary-*)  role aliases for light and dark themes
  component  local module classes             search, shortcut, newsstand, widget, login
  motion     (--duration-* / --easing-*)      shared timing contracts
  ```
- **Class naming**: mixed readable globals (`search_area`, `shortcut_area`) and CSS module hashes (`EventBannerView-module__...`).
- **Default theme**: light. Dark token pairs exist, but the captured homepage renders light.
- **Font loading**: system stack plus Korean OS fonts; `NanumSquare` appears in limited specialty declarations.
- **Canonical anchor**: central search pill and NAVER green action color.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `-apple-system / BlinkMacSystemFont / Malgun Gothic` (platform/system)
- **Code font**: not part of observed homepage UI
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --naver-font-family:
    -apple-system, BlinkMacSystemFont, "Malgun Gothic", "맑은 고딕",
    Helvetica, "Apple SD Gothic Neo", sans-serif;
  --naver-font-family-special: "NanumSquare";
  --naver-font-weight-normal: 400;
  --naver-font-weight-bold: 700;
}
body {
  font-family: var(--naver-font-family);
  font-weight: var(--naver-font-weight-normal);
}
```

### Note on Font Substitutes

- **Malgun Gothic / Apple SD Gothic Neo** - keep the OS Korean stack first. A generic Inter-only substitute will make Korean labels too Latin-product-like.
- **Open-source substitute**: use **Pretendard** at 400/500/700 only when cross-platform rendering must be normalized.
- **Correction**: keep compact labels at `letter-spacing: -0.28px` to `-0.4px`; Pretendard without this correction reads wider than the captured NAVER UI.
- **NanumSquare fallback**: if unavailable, use Pretendard 700 for promo/widget headlines, but do not apply it to the whole document.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| Search placeholder | 22px | 400 | 58px container | 0 |
| Promo banner headline | 28-32px visual | 700 | 38-40px | -0.6px to -1px |
| Card title | 16px | 700 | 22px | -0.3px |
| Navigation/category label | 14px | 500-700 | 20px | -0.28px |
| Body/link text | 13-14px | 400-500 | 19-22px | 0 to -0.28px |
| Caption/micro label | 10-12px | 500-700 | 14-16px | -0.28px |

> ⚠️ The page uses a broad weight range, but the visible rhythm is compact: many labels are 12-14px with optical negative tracking.

### Principles

1. The search input is visually oversized relative to the rest of the UI; it is the only calm, large text field in the first viewport.
2. Most portal content lives between 12px and 16px. NAVER density comes from line-height and grid structure, not from big display type.
3. Weight 700 appears frequently for labels, card titles, and service names; it should not be reserved only for page headlines.
4. Negative tracking is local and small. Use `-0.28px`, `-0.3px`, or `-0.4px`, not broad `-0.02em` editorial tracking everywhere.
5. Do not replace the Korean system stack with a single Latin-first font; Korean glyph metrics are part of the layout.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (5 steps)

| Token | Hex |
|---|---|
| `--core-color-light-green-100` | `#E6F9EE` |
| `--core-color-light-green-200` | `#D9F7E6` |
| `--core-color-light-green-700` | `#03C75A` |
| `--core-color-light-green-800` | `#03A94D` |
| `--core-color-light-green-900` | `#00893D` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--core-color-dark-green-600` | `#05AC4F` |
| `--color-primary-background-default` dark mapping | `#05AC4F` |
| `--color-primary-stroke-default` dark mapping | `#05AC4F` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| page base | `#F0F0F0` | `#131313` |
| surface | `#FFFFFF` | `#2D2D2D` |
| raised | `#F8F9FA` | `#2D2D2D` |
| text default | `#000000` / `#101010` | `#FFFFFF` |
| text subtle | `#8C8C8C` | `#BDBDBD` |
| hairline | `#E5E5E5` | `#FFFFFF1A` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| News / sports blue | service accent | `#0147B5` |
| Entertainment magenta | service accent | `#E65DA0` |
| Shopping yellow | service accent | `#EBAA00` |
| Live / warning red | badge accent | `#F4361E` |
| Webtoon green | service accent | `#00C855` |
| Link blue | semantic link | `#0C43B7` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--color-primary-background-default` | `#03A94D` / dark `#05AC4F` | primary action backgrounds |
| `--color-primary-background-decorative` | `#03C75A` | search/logo decorative green |
| `--color-neutral-background-base-basic` | `#F0F0F0` | page floor |
| `--color-neutral-background-raised-1` | `#F8F9FA` | raised sections and pale modules |
| `--color-neutral-foreground-default` | `#000000` | main text |
| `--color-neutral-stroke-subtle-1` | `#0000001A` | subtle stroke |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--color-primary-background-default` | `--core-color-light-green-800` -> `#03A94D` | pressed/default primary fill |
| `--color-primary-background-decorative` | `--core-color-light-green-700` -> `#03C75A` | brand decorative green |
| `--color-neutral-background-base-main-home` | `--core-color-main-home-gray` -> `#EDF0F4` | home base token |
| `--color-neutral-background-raised-1` | `--core-color-raised-gray` -> `#F8F9FA` | raised neutral panels |
| `--color-function-specific-search-green` | `--core-color-light-pale-green-700` | search-specific accent |
| `--color-function-specific-news-blue` | `--core-color-news-blue` | news module accent |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency |
|---|---|---:|
| surface white | `#FFFFFF` | 51 |
| caption gray | `#B5B5B5` | 25 |
| muted gray | `#8C8C8C` | 17 |
| secondary gray | `#8C8C8C` | 17 |
| light gray | `#BDBDBD` | 14 |
| sports/news blue | `#0147B5` | 13 |
| entertainment magenta | `#E65DA0` | 13 |
| shopping yellow | `#EBAA00` | 13 |
| teal service accent | `#008F76` | 12 |
| primary green | `#03C75A` | 4 direct occurrences plus token aliases |

### 06-8. Color Stories

**`{colors.primary}` (`#03C75A`)** - NAVER green is not spread as a wash. It appears where command intent matters: the search mark, search icon, outline, and primary login CTA.

**`{colors.surface}` (`#FFFFFF`)** - The page is a white-card portal. Cards, search field, shortcuts, login, and news modules depend on white as a reusable chassis against a pale page floor.

**`{colors.text}` (`#101010`)** - The visible text black is slightly softened in component snippets. It keeps the portal readable without turning every card into high-contrast editorial copy.

**`{colors.hairline}` (`#E5E5E5`)** - Borders do more structural work than shadows. NAVER's grid stays organized through thin dividers, not through big elevation.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--sizes-mobile` | 320px | smallest responsive floor |
| `--sizes-tablet` | 830px | tablet breakpoint token |
| `--sizes-pc` | 1300px | desktop shell token |
| `--sizes-lg` | 1072px | central content region |
| shortcut icon | 40px visual / 86px slot | compact app shortcut rhythm |
| card padding | 16px / 20px / 24px patterns | widget and module interiors |
| section gap | 12px / 16px / 20px | dense portal stacking |

**주요 alias**:
- `--breakpoints-mobile` -> 320px
- `--breakpoints-tablet` -> 830px
- `--breakpoints-pc` -> 1300px

### Whitespace Philosophy

NAVER's whitespace is not luxurious; it is traffic control. The search area gets the broadest breath so the user knows where to begin, while shortcut icons and content cards compress quickly below it. The result is "open command, dense portal" rather than an evenly airy page.

Inside modules, white space is measured in small increments: 12px, 16px, 20px, and 24px. The page gives each service enough room to be identified, then immediately returns to grid economy.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| Search pill | 30px / pill | search field outer shape |
| Circle | 50% | icon buttons, notification, floating controls |
| Micro radius | 4px | login button, small labels, rectangular controls |
| Card radius | 8px | newsstand/widget cards |
| Shortcut radius | 14px | app shortcut icon tile |
| Large chip | 20px / 100px | capsule filters and rounded utility buttons |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| subtle | `0 1px 2px 0 rgba(0,0,0,.06)` | shortcut and small raised controls |
| default | `0 2px 4px 0 rgba(0,0,0,.12)` | cards/popovers |
| strong | `0 2px 4px 0 rgba(0,0,0,.2)` | overlay or darkened surfaces |
| raised card | `0 3px 6px 0 rgba(0,0,0,.06)` | widget lift |
| focus shell | `0 0 0 1px var(--color-neutral-stroke-subtle-1), 0 1px 2px rgba(0,0,0,.04)` | bordered card with embedded elevation |

---

## 10. Motion
<!-- SOURCE: auto -->

| Token | Value | Usage |
|---|---|---|
| `--duration-acc` | 300ms | accelerated state transition |
| `--duration-in-acc` | 200ms | entrance/pressed transition |
| `--easing-standard` | `cubic-bezier(0.15, 0, 0.15, 1)` | default state easing |
| `--easing-out` | `cubic-bezier(0.33, 1, 0.68, 1)` | outward reveal |
| `--easing-spring` | `cubic-bezier(0.34, 1.5, 0.54, 1)` | springy micro interaction |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: approximately 1280-1300px desktop shell.
- **Grid type**: flex/grid hybrid; central left content column plus right rail.
- **Column count**: 2 primary columns in the captured desktop viewport.
- **Gutter**: about 28-30px between main content and right rail.

### Hero

- **🆕 Pattern Summary**: top utility strip + centered search pill + shortcut rail + two-column portal cards.
- Layout: one centered search command stacked above dense content grid.
- Background: white page top, pale neutral lower page, white cards.
- **🆕 Background Treatment**: solid neutral surfaces; no hero image/video background.
- H1: no conventional marketing H1. Search placeholder is the hero text at about 22px, weight 400.
- Max-width: search group visually around 708px; page shell around 1280px.

### Section Rhythm

```css
section {
  padding: 0 0 12px;
  max-width: 1300px;
}
.portal-card {
  padding: 16px 20px;
  border: 1px solid #E5E5E5;
  border-radius: 8px;
}
```

### Card Patterns

- **Card background**: `#FFFFFF`
- **Card border**: `1px solid #E5E5E5` or alpha black subtle stroke
- **Card radius**: 8px common, 4px for tighter internal controls
- **Card padding**: 16px to 24px depending on module density
- **Card shadow**: light and usually secondary to border; common values include `0 1px 2px rgba(0,0,0,.06)`

### Navigation Structure

- **Type**: portal utility navigation plus shortcut icon rail.
- **Position**: static top shell in captured homepage.
- **Height**: top promotion strip around 37px; search area plus shortcuts occupy the main top block.
- **Background**: `#FFFFFF`
- **Border**: subtle horizontal separators with `#E5E5E5` / alpha black strokes.

### Content Width

- **Prose max-width**: not applicable; homepage is modular, not article prose.
- **Container max-width**: 1280-1300px.
- **Sidebar width**: right rail approximately 390px in captured desktop layout.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | 320px | token floor and very small device support |
| Small mobile | 375px | explicit max-width branch appears |
| Tablet | 830px | tokenized tablet boundary |
| Desktop | 1280px / 1300px | desktop shell and media branch |
| Legacy large | 2560px | upper token for wide environments |

### Touch Targets

- **Minimum tap size**: shortcut and icon buttons visually target 40px+.
- **Button height (mobile)**: not fully measured; desktop login CTA is 56px.
- **Input height (mobile)**: desktop search field is 58px; mobile-specific measured value not confirmed.

### Collapsing Strategy

- **Navigation**: top hamburger/pay/notification utility controls remain icon-first.
- **Grid columns**: desktop two-column portal likely collapses to single-column feed below tablet.
- **Sidebar**: right rail should stack or hide under main content on mobile.
- **Hero layout**: search remains top command; shortcut rail compresses before content cards.

### Image Behavior

- **Strategy**: promo/banner images are embedded in bounded rounded modules.
- **Max-width**: module-constrained rather than full-bleed.
- **Aspect ratio handling**: banner modules crop to fixed-height rectangles; icon tiles remain square/circular.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary login button**

```html
<button class="naver-login-primary">NAVER 로그인</button>
```

| Property | Value |
|---|---|
| Background | `#03C75A` |
| Text | `#FFFFFF` |
| Height | 56px |
| Radius | 4px |
| Font | system Korean stack, 700 |
| Hover/active | darker green token such as `#03A94D` |

**Search submit icon button**

```html
<button class="naver-search-submit" aria-label="search"></button>
```

| Property | Value |
|---|---|
| Shape | icon-only button inside search pill |
| Color | `#03C75A` |
| Hit area | about 40px |
| State | color/opacity transition using 200-300ms tokens |

### Badges

**Live / alert badge**

| Property | Value |
|---|---|
| Background | `#F4361E` |
| Text | `#FFFFFF` |
| Height | 14px class of micro badge |
| Radius | small capsule |
| Usage | news/sports live state, not primary brand identity |

**Recommendation chip**

| Property | Value |
|---|---|
| Background | service-local blue or green |
| Radius | 100px / pill |
| Font | 10-12px, 700 |

### Cards & Containers

**Portal module card**

```html
<section class="naver-portal-card">
  <header class="naver-card-tabs">뉴스스탠드 · 언론사편집</header>
  <div class="naver-card-body">...</div>
</section>
```

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Border | `1px solid #E5E5E5` |
| Radius | 8px |
| Padding | 16px to 24px |
| Shadow | none or subtle `0 1px 2px rgba(0,0,0,.06)` |
| Hover | border/shadow lift only for interactive tiles |

### Navigation

**Shortcut rail**

```html
<nav class="naver-shortcut-rail">
  <a class="naver-shortcut"><span class="icon"></span><span>메일</span></a>
</nav>
```

| Property | Value |
|---|---|
| Icon tile | white square/circle hybrid |
| Radius | 14px tile, 50% for circular controls |
| Label | 14px or smaller, 500 |
| Spacing | compact 40px icon inside wider 80px slot |

### Inputs & Forms

**Search pill**

```html
<form class="naver-search-pill">
  <span class="naver-logo-mark">N</span>
  <input placeholder="검색어를 입력해 주세요." />
  <button aria-label="keyboard"></button>
  <button aria-label="search"></button>
</form>
```

| Property | Value |
|---|---|
| Height | 58px |
| Width | about 708px desktop |
| Border | `1px solid #03C75A` |
| Radius | 30px |
| Placeholder | pale gray, about 22px |
| Focus | keep green outline; do not add blue browser-like glow |

### Hero Section

NAVER's hero section is the search command surface, not a promotional visual. It contains the green logo mark, input, keyboard affordance, search icon, and the shortcut rail immediately below. The hero should feel usable before it feels expressive.

### 13-2. Named Variants

| Variant | Spec | Notes |
|---|---|---|
| `search-pill` | `height: 58px; border: 1px solid #03C75A; border-radius: 30px` | central command component |
| `login-primary` | `background: #03C75A; color: #FFFFFF; height: 56px; radius: 4px` | right-rail login action |
| `shortcut-icon` | `40px icon inside ~86px slot; radius 14px / 50%` | app/service launcher |
| `portal-card` | `#FFFFFF + #E5E5E5 border + 8px radius` | news, widgets, login containers |
| `live-badge` | `#F4361E; 14px height` | local alert, not brand primary |

### 13-3. Signature Micro-Specs

```yaml
search-pill-command-ring:
  description: "The homepage identity is a single green bordered command pill instead of a hero headline."
  technique: "height: 58px; width: about 708px desktop; border: 1px solid #03C75A; border-radius: 30px; background: #FFFFFF; green logo/search icons"
  applied_to: ["{component.search-pill}"]
  visual_signature: "Immediate type-here command surface with no marketing copy competing above it."

portal-hairline-card-chassis:
  description: "Repeated portal modules are organized by thin borders more than dramatic elevation."
  technique: "background: #FFFFFF; border: 1px solid #E5E5E5 or alpha black subtle stroke; border-radius: 8px; shadow: none to 0 1px 2px rgba(0,0,0,.06)"
  applied_to: ["{component.portal-card}", "{component.login-primary}"]
  visual_signature: "Dense white panels remain scan-friendly because the chassis is hairline-first, not shadow-first."

shortcut-icon-tile-slot:
  description: "Service entry points use compact icon tiles inside wider portal slots."
  technique: "40px icon visual inside roughly 80-86px slot; background: #FFFFFF; border-radius: 14px for tile controls, 50% for circular controls; shadow: 0 1px 2px rgba(0,0,0,.06)"
  applied_to: ["{component.shortcut-icon}"]
  visual_signature: "A small app-launcher rail directly under search, reading as utility infrastructure rather than decorative icons."

service-local-color-wayfinding:
  description: "Non-green color is reserved for service identity and state, not page atmosphere."
  technique: "news blue #0147B5; entertainment magenta #E65DA0; shopping yellow #EBAA00; live red #F4361E; webtoon green #00C855; kept to badges, filters, and category markers"
  applied_to: ["{component.live-badge}", "{component.portal-card}"]
  visual_signature: "A neutral portal map where accent color behaves like transit-line labeling."

compact-korean-label-tracking:
  description: "Small Korean portal labels use optical negative tracking to keep dense modules crisp."
  technique: "font-size: 10-16px; font-weight: 500-700; letter-spacing: -0.28px, -0.3px, -0.4px, occasionally -0.6px"
  applied_to: ["{component.portal-card}", "{component.shortcut-icon}"]
  visual_signature: "Tight native Korean UI rhythm that would feel loose if rendered as generic Latin-first spacing."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Search prompt | polite direct instruction | "검색어를 입력해 주세요." |
| Module labels | noun-first, compact | "뉴스스탠드", "쇼핑투데이" |
| CTA | utility verb, low ceremony | "로그인" |
| Promo copy | benefit and event timing | "봄~여름 옷 똑똑하게 살 타이밍" |
| Tone | serviceable, everyday, dense | avoids manifesto language |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* NAVER-inspired portal shell */
:root {
  /* Fonts */
  --naver-font-family:
    -apple-system, BlinkMacSystemFont, "Malgun Gothic", "맑은 고딕",
    Helvetica, "Apple SD Gothic Neo", sans-serif;
  --naver-font-family-special: "NanumSquare", var(--naver-font-family);
  --naver-font-weight-normal: 400;
  --naver-font-weight-bold: 700;

  /* Brand */
  --naver-color-brand-25:  #E6F9EE;
  --naver-color-brand-300: #D9F7E6;
  --naver-color-brand-500: #03C75A;
  --naver-color-brand-600: #03A94D;
  --naver-color-brand-900: #00893D;

  /* Surfaces */
  --naver-bg-page:    #F0F0F0;
  --naver-bg-surface: #FFFFFF;
  --naver-text:       #101010;
  --naver-text-muted: #8C8C8C;
  --naver-border:     #E5E5E5;

  /* Key spacing */
  --naver-space-xs: 8px;
  --naver-space-sm: 12px;
  --naver-space-md: 16px;
  --naver-space-lg: 24px;

  /* Radius */
  --naver-radius-sm: 4px;
  --naver-radius-md: 8px;
  --naver-radius-icon: 14px;
  --naver-radius-pill: 30px;
}

.naver-shell {
  max-width: 1300px;
  margin: 0 auto;
  font-family: var(--naver-font-family);
  color: var(--naver-text);
  background: var(--naver-bg-page);
}

.naver-search-pill {
  width: min(708px, calc(100vw - 32px));
  height: 58px;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 0 24px;
  border: 1px solid var(--naver-color-brand-500);
  border-radius: var(--naver-radius-pill);
  background: var(--naver-bg-surface);
}

.naver-portal-card {
  background: var(--naver-bg-surface);
  border: 1px solid var(--naver-border);
  border-radius: var(--naver-radius-md);
  box-shadow: 0 1px 2px 0 rgba(0,0,0,.06);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js - NAVER-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        naver: {
          green: "#03C75A",
          greenActive: "#03A94D",
          page: "#F0F0F0",
          surface: "#FFFFFF",
          text: "#101010",
          muted: "#8C8C8C",
          hairline: "#E5E5E5",
          news: "#0147B5",
          live: "#F4361E",
        },
      },
      fontFamily: {
        sans: [
          "-apple-system",
          "BlinkMacSystemFont",
          "Malgun Gothic",
          "Apple SD Gothic Neo",
          "sans-serif",
        ],
      },
      borderRadius: {
        naverCard: "8px",
        naverIcon: "14px",
        naverPill: "30px",
      },
      boxShadow: {
        naverSubtle: "0 1px 2px 0 rgba(0,0,0,.06)",
        naverCard: "0 2px 4px 0 rgba(0,0,0,.12)",
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
| Brand primary | `{colors.primary}` | `#03C75A` |
| Brand active | `{colors.primary-active}` | `#03A94D` |
| Background | `{colors.page}` | `#F0F0F0` |
| Surface | `{colors.surface}` | `#FFFFFF` |
| Text primary | `{colors.text}` | `#101010` |
| Text muted | `{colors.text-muted}` | `#8C8C8C` |
| Border | `{colors.hairline}` | `#E5E5E5` |
| Error/live | live badge | `#F4361E` |

### Example Component Prompts

#### Hero Search

```text
NAVER 스타일 검색 히어로를 만들어줘.
- 구조: 중앙 58px high search pill, 바로 아래 shortcut icon rail
- search pill: width 708px, background #FFFFFF, border 1px solid #03C75A, radius 30px
- placeholder: "검색어를 입력해 주세요.", 22px, system Korean stack, color pale gray
- icons: NAVER N/logo and search icon in #03C75A
- 주변에는 큰 H1이나 SaaS CTA를 넣지 말 것
```

#### Portal Card

```text
NAVER 스타일 포털 카드 컴포넌트를 만들어줘.
- background #FFFFFF, border 1px solid #E5E5E5, radius 8px
- padding 16px 20px
- shadow는 없거나 0 1px 2px rgba(0,0,0,.06)
- 제목은 16px/700, label은 12-14px/500 with -0.28px tracking
- 내부는 뉴스/위젯처럼 촘촘한 grid로 배치
```

#### Badge

```text
NAVER 스타일 상태 배지를 만들어줘.
- live/error badge: background #F4361E, text #FFFFFF, height 14px
- service badge는 module-local color 사용: news #0147B5, entertainment #E65DA0, shopping #EBAA00
- brand green #03C75A는 primary command에만 쓰고 모든 badge에 남발하지 말 것
```

#### Navigation

```text
NAVER 스타일 shortcut navigation을 만들어줘.
- icon tile: white surface, 40px visual target, radius 14px or circle
- label: 13-14px, weight 500, Korean system stack
- rail spacing은 compact하게, icon group은 search 바로 아래 위치
- hover는 큰 transform 없이 border/shadow만 살짝 변경
```

### Iteration Guide

- **색상 변경 시**: #03C75A는 search/login/primary action에 남기고, service colors는 지역 accent로만 둔다.
- **폰트 변경 시**: Korean system metrics를 우선한다. Inter-only UI는 NAVER처럼 보이지 않는다.
- **여백 조정 시**: search top block만 넓게, cards/widgets는 12-24px compact rhythm을 유지한다.
- **새 컴포넌트 추가 시**: white card + hairline + 8px radius를 기본 chassis로 사용한다.
- **다크 모드**: dark tokens exist, but captured homepage analysis is light-first; direct inversion은 금지.
- **반응형**: 320/830/1300 breakpoint logic을 유지하고 right rail은 모바일에서 stack/hide 처리한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #03C75A as the central command color for search and primary action.
- Build the first viewport around search, shortcut rail, news/card modules, login, and widgets.
- Keep most surfaces #FFFFFF on a pale neutral page floor such as #F0F0F0.
- Use hairline borders and compact radii before heavy shadows.
- Preserve Korean system font metrics and small negative tracking for labels.
- Treat non-green chromatic colors as service-local wayfinding.

### ❌ DON'T

- 배경을 `#FFFFFF` 단일 full-page white로만 두지 말 것 — 대신 page floor `#F0F0F0`와 card surface `#FFFFFF`를 분리.
- 텍스트를 `#000000`만으로 강하게 밀지 말 것 — 주요 UI 텍스트는 `#101010`, 보조 텍스트는 `#8C8C8C` 계열 사용.
- primary green을 `#03A94D` active tone으로만 고정하지 말 것 — NAVER command green은 `#03C75A`.
- 모든 border를 `#DADCDF`로 통일하지 말 것 — search/control border와 card hairline `#E5E5E5`를 구분.
- CTA를 12px radius SaaS button으로 만들지 말 것 — login은 4px rectangle, search는 30px pill로 역할이 다르다.
- body 전체를 Inter 400으로 고정하지 말 것 — Korean system stack과 500/700 label weights가 필요하다.
- hero에 large marketing H1 + centered CTA를 넣지 말 것 — search input이 hero다.
- 카드마다 colorful gradient를 깔지 말 것 — service colors는 badge/filter/local accent에만 둔다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No marketing hero manifesto** - there is no oversized value-prop headline above the fold.
- **No global gradient atmosphere** - gradient tokens exist locally, but the homepage mood is solid surface and card structure.
- **No second global brand color** - blue/magenta/yellow/red are service markers, not alternate brand primaries.
- **No luxurious whitespace system** - the portal compresses information immediately after the search command.
- **No heavy elevation language** - borders and light shadows organize the page.
- **No universal pill buttons** - only search and some chips are pill-shaped; login remains rectangular.
- **No illustration-led identity** - icons and ads exist, but the UI identity is search plus modules.
- **No generic western SaaS typography** - Korean OS font metrics are part of the design.
- Photographic city skyline hero behind the desk: absent. The counter does not advertise the city.
- Floating "concierge" mascot illustration: zero. The desk is unmanned by characters.
- Branded loading animation on the search pill: never. The counter is always-on.
- Welcome banner / personalized greeting modal at first viewport: none on the unauthenticated portal.
- Decorative section dividers between modules: absent. Hairlines do all separating work; no ornamental rule lines.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Cached phase1 data** - HTML/CSS/JSON came from the existing `insane-design/naver` cache rather than a fresh network fetch in this turn.
- **Single homepage viewport** - the screenshot covers the desktop homepage first viewport only; search results, mail, shopping, login flows, and account states were not visited.
- **Dark mode not visually confirmed** - dark token mappings were present in CSS, but the captured screenshot is light theme.
- **CSS variable order ambiguity** - some variables have light and dark definitions; this guide reports observed light homepage behavior and cites dark mappings only where explicit.
- **Component states incomplete** - hover/focus/active/loading/error states were inferred from CSS token patterns where visible state screenshots were unavailable.
- **Ad and partner imagery excluded** - banner and ad colors are treated as content, not design-system palette anchors.
- **Mobile behavior partially inferred** - breakpoint tokens and media queries were observed, but mobile screenshots were not captured in this run.
- **Exact logo geometry not extracted** - this guide describes the visible NAVER mark behavior but does not provide vector logo construction specs.
