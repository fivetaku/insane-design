---
schema_version: 3.2
slug: sony
service_name: Sony Group Portal
site_url: https://www.sony.com/en/
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#000000"
primary_font: "SST W20 Roman"
font_weight_normal: 400
token_prefix: sony

bold_direction: Monochrome Entertainment
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: editorial-product
archetype_confidence: medium
design_system_level: lv1
design_system_level_evidence: "Public homepage exposes a production visual language, but reusable semantic design tokens are sparse; CSS evidence is mostly page/template CSS plus SST font declarations."

colors:
  black: "#000000"
  ink: "#111111"
  white: "#FFFFFF"
  hairline: "#D8D8D8"
  muted: "#656565"
  panel: "#F6F6F4"
  link-blue: "#3860BE"
typography:
  display: "SST W20 Bold"
  body: "SST W20 Roman"
  fallback: "SST W55 Regular"
  ladder:
    - { token: hero-title, size: "visual 20-24px in captured desktop overlay", weight: 700, tracking: "0" }
    - { token: nav-link, size: "14px visual", weight: 400, tracking: "0" }
    - { token: news-body, size: "14px visual", weight: 400, tracking: "0" }
  weights_used: [400, 500, 600, 700]
  weights_absent: [300, 800, 900]
components:
  header-black-bar: { bg: "{colors.black}", fg: "{colors.white}", height: "72px visual", radius: "0" }
  hero-carousel-filmstrip: { bg: "{colors.black}", image_gap: "30px inline", overlay: "blurred active-image backdrop" }
  play-button-disc: { bg: "rgba(0,0,0,0.75)", fg: "{colors.white}", size: "45px" }
  headline-news-strip: { bg: "#F6F6F4", border: "1px vertical divider #D8D8D8", radius: "0" }
---

# DESIGN.md - Sony Group Portal

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Sony stages entertainment content like a museum proscenium set on a blackout canvas. The portal is not a bright consumer landing page; it is a monochrome exhibition space where #000000 (`{colors.black}`), #FFFFFF (`{colors.white}`), #111111 (`{colors.ink}`), and #D8D8D8 (`{colors.hairline}`) do all of the interface work while color belongs entirely to content — Spider-Man red, concert light, hardware green, and game footage. The canvas disappears; the exhibits own the light.

The hero is a gallery filmstrip, not a card grid. The active slide sits large in the center, adjacent slides peek at both edges, and a blurred enlargement of the active media becomes the atmospheric floor behind the title. It is closer to a museum screening room where the film projects twice — once as the crisp frame, once as a soft spill of light on the back wall — than to a standard media carousel. The parchment of corporate identity recedes so franchise content can supply its own saturation.

The site has almost no object ego. It does not build a shiny UI showcase; it lowers the house lights and gives the parchment-black frame to the content. Typography is corporate Sony: SST W20/W55 with no decorative display face. Headings are compact labels over image, often 20-24px, with bold weight doing the work instead of scale — small white placards beside a museum gallery screen, identifying the work without competing with the projection.

The rhythm of the page is controlled: entertainment canvas above, a news strip below. The strip — #F6F6F4 (`{colors.panel}`), #111111 (`{colors.ink}`), #D8D8D8 (`{colors.hairline}`) — brings the visitor from the museum atmosphere back to formal institutional register. No shadow floats the strip; the border is a ruler line, not a card edge. There is no second brand color, no rounded marketing CTA stack; the visual signature is a Sony proscenium where the only light belongs to content.

### Key Characteristics

- Black fixed global header with white Sony logotype and slim horizontal navigation.
- Full-width editorial entertainment carousel with center-weighted active slide and visible neighboring slides.
- Blurred active-media backdrop behind hero copy, producing a screening-room atmosphere.
- Compact white overlay text, with category label above headline/description.
- Circular play control at 45px with translucent black disc and white triangle.
- News strip immediately below hero, flat #F6F6F4/#FFFFFF surfaces and thin dividers.
- SST W20/W55 font family stack, including Roman, Bold, Medium, Heavy, Condensed, and localized W55 fallbacks.
- Minimal radius and no card chrome in the first viewport; structure comes from image edges and hairlines.
- Swiper carousel mechanics expose pagination dots, pause/play control, and lateral arrows.
- Color is content-owned: Spider-Man red, stage lighting, hardware green, etc. are imagery, not UI tokens.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Monochrome Entertainment
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **black screening-room carousel with content-owned color**으로 기억된다.
> **Code Complexity**: high — Swiper carousel, video/media controls, blurred media backdrop, responsive header/search, and external template CSS make the interaction layer heavier than the visible UI chrome.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Sony Group Portal처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "SST W20 Roman", "SST W55 Regular", "Yu Gothic Medium", YuGothic, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #111111; --chrome: #000000; }
body { background: var(--bg); color: var(--fg); }
.global-header { background: var(--chrome); color: #FFFFFF; }

/* 3. 히어로 */
.hero {
  background: #000000;
  color: #FFFFFF;
  overflow: hidden;
}
```

**절대 하지 말아야 할 것 하나**: Sony를 파란 CTA 중심의 SaaS 랜딩처럼 만들지 말 것. #3860BE는 링크/search/cookie 계열에 섞인 보조색이지 homepage brand color가 아니다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.sony.com/en/` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | reused existing `insane-design/sony` phase1, CSS, HTML, screenshot artifacts |
| HTML size | 330470 bytes |
| CSS files | existing cache: inline font/cookie CSS + search CSS + Swiper CSS; several Sony template CSS files cached as Access Denied HTML |
| Token prefix | `sony` |
| Method | phase1 JSON + captured screenshot + homepage HTML structure + valid CSS fragments; missing main-template CSS noted in §19 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: server-rendered corporate homepage with Swiper 5.4.5 carousel and Marsflag search integration.
- **Design system**: Sony template CSS, not a public semantic token system. Detected custom properties are mostly Swiper and OneTrust.
- **CSS architecture**:
  ```text
  font-face layer       SST W20/W55 declarations from Monotype/Fast Fonts
  template layer        /en/template/2023 and /en/top/2021 CSS references
  interaction layer     Swiper carousel + custom scripts + search box CSS
  consent/search layer  OneTrust and Marsflag styles, visually separate from homepage brand
  ```
- **Class naming**: BEM-like template names (`tmpl-header`, `tmpl-headerNavItem`, `hero-item`, `headline-news`, `news-table`) with modifier classes (`is-init`, `is-current`, `is-active`, `is-desktop-hide`).
- **Default theme**: mixed. Header and hero are dark; news and content bands are light.
- **Font loading**: Fast Fonts / Monotype stylesheet exposes `SST W20 Roman`, `SST W20 Bold`, `SST W20 Medium`, `SST W20 Heavy`, `SST W20 Condensed`, and localized `SST W55` variants.
- **Canonical anchor**: first viewport is anchored by `main.main > .hero` and the global `header#tmpl-header`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `SST W20 Bold` (Sony corporate/proprietary family surfaced through fetched font-face CSS)
- **Body font**: `SST W20 Roman`, with `SST W55 Regular` and Japanese fallbacks
- **Code font**: N/A - no code surface
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --sony-font-family:       "SST W20 Roman", "SST W55 Regular", "Yu Gothic Medium", YuGothic, sans-serif;
  --sony-font-family-bold:  "SST W20 Bold", "SST W55 Bold", sans-serif;
  --sony-font-weight-normal: 400;
  --sony-font-weight-bold:   700;
}
body {
  font-family: var(--sony-font-family);
  font-weight: var(--sony-font-weight-normal);
}
.b,
strong,
.hero-item-title {
  font-family: var(--sony-font-family-bold);
  font-weight: var(--sony-font-weight-bold);
}
```

### Note on Font Substitutes

- **SST W20/W55** is the signature. If unavailable, use **Noto Sans** or **Inter** only as a mechanical substitute, not as a new personality.
- Open-source substitute: `Noto Sans` at 400/700 with `letter-spacing: 0` and slightly tighter line-height on overlay text (`1.35` instead of generic `1.5`).
- Avoid geometric display substitutes. Sony's homepage is corporate and media-led; the logo and imagery provide character.
- Keep Japanese fallback in the stack (`Yu Gothic Medium`, `YuGothic`) when reproducing the bilingual language switcher and Japan-facing content.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `nav-link` | 14px visual | 400 | ~1 | 0 |
| `hero-category` | 14-16px visual | 700 | ~1.3 | 0 |
| `hero-title` | 20-24px visual in captured desktop overlay | 700 | ~1.25 | 0 |
| `hero-description` | 14-16px visual | 400 | ~1.35 | 0 |
| `news-label` | 16px visual | 700 | ~1.2 | 0 |
| `news-body` | 14px visual | 400 | ~1.4 | 0 |
| `site-map-heading` | 14-16px visual | 700 | ~1.35 | 0 |

> ⚠️ Typography extraction did not produce a full CSS scale because the valid cached CSS is mostly font-face, search, Swiper, and consent CSS. Sizes above are measured from the captured homepage composition and HTML roles.

### Principles

1. Hero text is compact for an entertainment site. The image carries drama; typography labels and clarifies.
2. Bold weight is used for labels, dates, headings, and the `.b` utility. It is a structural marker, not decoration.
3. Body copy keeps neutral 400 weight and zero tracking. No editorial serif, no playful display face, no exaggerated negative tracking.
4. SST is the brand voice. Replacing it with generic Inter makes the page feel like a SaaS dashboard unless the media carousel remains dominant.
5. The Sony logo is the only serif-like typographic object in the first viewport. Do not echo it with serif headlines.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (monochrome anchor)

| Token | Hex |
|---|---|
| `sony.black` | `#000000` |
| `sony.ink` | `#111111` |
| `sony.white` | `#FFFFFF` |
| `sony.hairline` | `#D8D8D8` |
| `sony.muted` | `#656565` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `sony.chrome` | `#000000` |
| `sony.chrome-text` | `#FFFFFF` |
| `sony.hero-scrim` | `rgba(0,0,0,.55-.75)` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 | `#FFFFFF` | `#000000` |
| 10 | `#F8F8F8` | `#111111` |
| 20 | `#F6F6F4` | `#333333` |
| 30 | `#E9E9E9` | `#4D4D4D` |
| 40 | `#D8D8D8` | `#656565` |
| 50 | `#C1C1C1` | `#696969` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Search/link blue | link/search accent | `#3860BE` |
| Secondary link blue | cookie/search link | `#01498E` |
| Consent green | OneTrust, not brand | `#468254` |
| Swiper default blue | library default token, not brand | `#007AFF` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `sony.surface.page` | `#FFFFFF` | page body after hero |
| `sony.surface.news` | `#F6F6F4` | headline news strip / light utility band |
| `sony.text.primary` | `#111111` | light-surface text |
| `sony.text.inverse` | `#FFFFFF` | header and hero overlay |
| `sony.border.soft` | `#D8D8D8` | dividers and light separators |
| `sony.text.muted` | `#656565` | footer icons, secondary text, arrows |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--sony-chrome-bg` | `#000000` | global header, hero stage |
| `--sony-chrome-fg` | `#FFFFFF` | inverse text/icons |
| `--sony-page-bg` | `#FFFFFF` | body and content surfaces |
| `--sony-strip-bg` | `#F6F6F4` | news strip |
| `--sony-divider` | `#D8D8D8` | vertical/horizontal hairlines |

### 06-7. Dominant Colors (actual CSS frequency order, contaminated by consent/search CSS)

| Token | Hex | Frequency |
|---|---|---:|
| neutral-white | `#FFFFFF` | 100 |
| hairline-gray | `#D8D8D8` | 42 |
| neutral-black | `#000000` | 40 |
| search-blue | `#3860BE` | 22 |
| light-gray | `#E2E2E2` | 18 |
| light-gray-2 | `#E9E9E9` | 14 |
| line-gray | `#DDDDDD` | 13 |
| consent-green | `#68B631` | 12 |

### 06-8. Color Stories

**`{colors.black}` (`#000000`)** - The brand chrome. It owns the header and hero stage, making the Sony logotype and entertainment media feel like they are projected in a dark room. Use it for structural chrome, not random cards.

**`{colors.white}` (`#FFFFFF`)** - Inverse text and the post-hero floor. White is both foreground on black and the quiet body background below; the contrast is binary, not soft pastel.

**`{colors.hairline}` (`#D8D8D8`)** - The corporate divider. It separates the news label from the news item and appears as a low-drama interface boundary.

**`{colors.link-blue}` (`#3860BE`)** - Utility blue. It appears in search/link-like contexts but should not be promoted to brand primary for the homepage.

---

## 07. Spacing
<!-- SOURCE: manual -->

| Token | Value | Use case |
|---|---:|---|
| `sony-space-xs` | 8px | nav/icon alignment, small gaps |
| `sony-space-sm` | 16px | news strip inner text gap |
| `sony-space-md` | 30px | captured Swiper slide `margin-right` |
| `sony-space-lg` | 44px | Swiper navigation size token |
| `sony-space-xl` | 72px | visual header height band |
| `sony-space-xxl` | 80-96px | hero text/content offset zones |

**주요 alias**:
- `--swiper-navigation-size` -> `44px` (carousel navigation)
- `--ot-footer-space` -> `160px` (OneTrust footer spacing, not homepage layout)

### Whitespace Philosophy

Sony uses compressed chrome and expansive media. The header is dense: logo, seven nav links, contact link, and search icon all fit on one black bar. The hero then releases that compression into a wide carousel where the gaps between slides are visible and deliberate.

Whitespace is not airy luxury here. It is operational framing. The page reserves breathing room around media and news strips, but it does not create large blank editorial blocks in the first viewport. Content remains close to the top because the portal has corporate navigation duties as well as entertainment promotion duties.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `sony-radius-none` | 0 | header, hero image edges, news strip, footer |
| `sony-radius-control` | 3px | search/go-top utility controls from Marsflag CSS |
| `sony-radius-pill` | 999px visual | circular play/pause controls only |

Sony's first viewport is almost square. Rounded rectangles are not the main language. The circular play button is a media affordance, not a general button style.

---

## 09. Shadows
<!-- SOURCE: manual -->

| Level | Value | Usage |
|---|---|---|
| `none` | `none` | header chrome, news strip, card-like bands |
| `media-depth` | image blur / dark scrim, not box-shadow | hero backdrop depth |
| `control-overlay` | translucent fill, no cast shadow | play/pause media controls |

The homepage avoids SaaS elevation. Depth is created through imagery, blur, crop, and overlay, not through component shadows.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `swiper-transition` | `transform`-based carousel movement | hero slides |
| `media-playback` | video modal / embedded YouTube hooks | hero play action |
| `pause-control` | visible pause button in lower-right of captured viewport | background/video motion control |
| `reduced-motion` | Swiper CSS includes `prefers-reduced-motion` media handling | accessibility fallback |

Motion is content-serving. The carousel and background media move; buttons and cards do not perform playful bounces.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: hero spans viewport; news strip appears constrained inside a broad container with side gutters.
- **Grid type**: header uses horizontal flex-like navigation; hero uses Swiper track; sitemap uses four-column desktop menu.
- **Column count**: header single row; hero center slide with adjacent preview columns; footer sitemap four columns.
- **Gutter**: 30px between Swiper slides from inline captured slide style.

### Hero

- **Pattern Summary**: 65-70vh first-viewport media carousel + black header + blurred active-image backdrop + compact lower-left overlay copy + centered play control.
- Layout: center-weighted carousel with previous/next slide previews visible.
- Background: dark, image-derived blurred backdrop behind copy and controls.
- **Background Treatment**: image-overlay / blurred active media, with dark scrim and black stage.
- H1: `20-24px visual` / weight `700` / tracking `0`.
- Max-width: viewport-width carousel; active slide roughly 55% of desktop width in capture.

### Section Rhythm

```css
section {
  padding: 0 44px;        /* visual approximation for first light strip */
  max-width: none;        /* hero and top bands are viewport-led */
}
.headline-news {
  min-height: 72px;
  background: #F6F6F4;
}
```

### Card Patterns

- **Card background**: N/A for first viewport; media slides are images, not UI cards.
- **Card border**: none on hero media.
- **Card radius**: 0.
- **Card padding**: text overlay sits below active image inside hero detail area.
- **Card shadow**: none; depth comes from media blur and dark overlay.

### Navigation Structure

- **Type**: horizontal desktop global nav with hamburger/search surfaces present in DOM.
- **Position**: fixed/sticky visual header at top in capture.
- **Height**: about 72px visual.
- **Background**: `#000000`.
- **Border**: no visible border; separation by black/hero boundary.

### Content Width

- **Prose max-width**: N/A on homepage first viewport.
- **Container max-width**: broad viewport container; news strip has left/right gutters around 44px in capture.
- **Sidebar width**: N/A for homepage; sitemap footer uses column menu instead of sidebar.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | 425px / 481px / 550px | search and utility CSS mobile thresholds; hero likely switches to mobile image sources below 641px |
| Tablet | 640px / 641px | hero `<source media="(min-width: 641px)">`; Swiper and layout break around this point |
| Desktop | 769px / 897px / 1024px | navigation and desktop presentation thresholds in cached CSS/media list |
| Large | 1280px | wide desktop adjustment observed in media query list |

### Touch Targets

- **Minimum tap size**: carousel navigation token `44px`; play button `45px`.
- **Button height (mobile)**: not fully measured; use 44px minimum for media/search controls.
- **Input height (mobile)**: search CSS present but main template CSS missing; assume Marsflag default control sizing and verify before implementation.

### Collapsing Strategy

- **Navigation**: desktop horizontal nav coexists with hamburger DOM; mobile likely collapses to hamburger menu.
- **Grid columns**: sitemap desktop four-column menu collapses in mobile variant.
- **Sidebar**: no sidebar in first viewport.
- **Hero layout**: image sources switch at 641px; carousel should reduce neighboring slide exposure on small screens.

### Image Behavior

- **Strategy**: `<picture>` with desktop and small image sources, lazyload images, video modal URL per slide.
- **Max-width**: hero images fill slide containers.
- **Aspect ratio handling**: content images are cropped to consistent carousel tiles; active image becomes both tile and backdrop source.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Media play button**

| Property | Value |
|---|---|
| Selector | `.hero-controls-play-button` |
| Shape | circular SVG control |
| Size | 45px |
| Fill | translucent black disc, approx `rgba(0,0,0,.75)` |
| Icon | white triangle |
| State | `.is-active` marks active playable slide |

**Pause control**

| Property | Value |
|---|---|
| Selector | `.panels-new-btn` / captured lower-right pause control |
| Shape | circular |
| Size | visually 58px asset in HTML |
| Purpose | stop background video / media movement |

### Badges

| Pattern | Value |
|---|---|
| Hero category | `.hero-item-category`, bold white text |
| Language state | `.language-select .is-current`, current language as text not pill |
| News date | `time.b`, bold date at start of each news row |

Badges are typographic labels, not filled chips.

### Cards & Containers

| Pattern | Value |
|---|---|
| Hero slide | image tile with square edges, no border, no radius |
| News strip | flat light container with vertical divider |
| News list | row-based table/list, text-first, no cards |
| Sitemap | dense column menu, no card surfaces |

### Navigation

| Property | Value |
|---|---|
| Header selector | `header#tmpl-header.tmpl-header` |
| Logo | SVG image `logo.svg`, white on black |
| Link style | white text, compact spacing |
| Utility | Contact Us text + search icon |
| Mobile affordance | hamburger DOM present with three lines and `menu` label |
| Dropdown | `tmpl-headerNavDropDown` structure present for product/about categories |

### Inputs & Forms

| Property | Value |
|---|---|
| Search provider | Marsflag search (`mf_finder_searchBox`) |
| Search form | hidden selects + query input + submit button |
| Placeholder | "Enter the word you want to search" |
| Visual note | cached search CSS is valid, but header template CSS for final open/closed visual state was not fully available |

### Hero Section

| Property | Value |
|---|---|
| Root | `.hero.is-init` |
| Carousel | `.swiper-container.hero-items` |
| Slide | `.swiper-slide.hero-item` |
| Text | `.hero-item-detail` with category, title, description |
| Media | `.hero-item-image picture`, desktop source at 641px+ |
| Controls | arrows, dots, play/pause, video modal data attributes |
| Atmosphere | blurred current media used as backdrop in captured screenshot |

### 13-2. Named Variants

**header-black-bar**

| Property | Value |
|---|---|
| Background | `#000000` |
| Foreground | `#FFFFFF` |
| Height | about 72px visual |
| Radius | 0 |
| States | dropdown/open state present in DOM; visual CSS not fully cached |

**hero-carousel-filmstrip**

| Property | Value |
|---|---|
| Active slide | large center media |
| Neighbor slides | visible left and right previews |
| Gap | 30px inline slide margin |
| Backdrop | blurred active media + dark scrim |
| States | active, duplicate, next, hidden, video playable |

**headline-news-strip**

| Property | Value |
|---|---|
| Background | `#F6F6F4` / light gray-white |
| Structure | label block + vertical divider + headline link |
| Text | black primary with bold label |
| Radius | 0 |

**footer-sitemap-columns**

| Property | Value |
|---|---|
| Layout | desktop four-column sitemap |
| Content | businesses, technology, sustainability, design, IR categories |
| Treatment | dense text links, no cards |

### 13-3. Signature Micro-Specs

```yaml
screening-room-hero-backdrop:
  description: "The active entertainment asset becomes both the main tile and the atmospheric background."
  technique: "image/video-derived backdrop behind `.hero`; blur treatment approximated at filter: blur(18px), transform: scale(1.08), opacity: .55, over #000000 chrome"
  applied_to: [".hero", ".hero-item", ".hero-item-detail", "{component.hero-carousel-filmstrip}"]
  visual_signature: "Sony reads as a dark screening room where the slide projects a soft spill of light behind itself."

filmstrip-neighbor-reveal:
  description: "The carousel shows a dominant center slide while neighboring entertainment assets remain visible at both sides."
  technique: "Swiper horizontal track with centered active slide, adjacent slide previews, captured inline gap around margin-right: 30px, square image edges, no card border"
  applied_to: [".swiper-container.hero-items", ".hero-wrapper", ".hero-item", "{component.hero-carousel-filmstrip}"]
  visual_signature: "A row of studio frames moves like a filmstrip instead of resolving into a marketing card grid."

monochrome-content-owned-color:
  description: "Interface chrome stays black and white while saturated color is owned by photography, video, and franchise imagery."
  technique: "global/header/hero chrome uses #000000 /* {colors.black} */ and #FFFFFF /* {colors.white} */; utility blue #3860BE remains search/link context only"
  applied_to: ["header#tmpl-header.tmpl-header", ".hero", ".hero-item-image", "{component.header-black-bar}"]
  visual_signature: "No second brand color competes with the media; the UI disappears like unlit theater architecture."

typographic-badge-not-chip:
  description: "Category, language, and news-date markers are text labels, not filled chip components."
  technique: "SST bold/plain text labels, weight 700 for `.b` and `.hero-item-category`; no background fill, no pill radius, no badge shadow"
  applied_to: [".hero-item-category", ".language-select .is-current", ".news time", "{component.headline-news-strip}"]
  visual_signature: "The labels feel like corporate placards beside the image, not decorative marketing stickers."

media-control-circles-only:
  description: "Rounded geometry is reserved for playback controls rather than generalized CTA styling."
  technique: "45px circular `.hero-controls-play-button` with rgba(0,0,0,.75) disc and white triangle; captured pause control visually around 58px; top-experience CTA rectangles remain absent"
  applied_to: [".hero-controls-play-button", ".panels-new-btn", "{component.play-button-disc}"]
  visual_signature: "Round shapes read as media hardware controls, while the rest of the page stays square and matte."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Content-title first, often entertainment property or initiative | "A Brand New Day Starts Now" |
| Category | Business domain label before/near headline | "Movies & TV", "Audio", "Gaming" |
| CTA | Mostly implicit through linked media and play action | "play ... in player" |
| News | Formal corporate headline with exact date | "Sony and TCL Sign Definitive Agreements..." |
| Tone | Corporate portal meets entertainment publisher | concise, informational, brand-neutral |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Sony Group Portal - copy into your root stylesheet */
:root {
  /* Fonts */
  --sony-font-family: "SST W20 Roman", "SST W55 Regular", "Yu Gothic Medium", YuGothic, sans-serif;
  --sony-font-family-bold: "SST W20 Bold", "SST W55 Bold", sans-serif;
  --sony-font-weight-normal: 400;
  --sony-font-weight-bold: 700;

  /* Brand / chrome */
  --sony-color-brand-25:  #FFFFFF;
  --sony-color-brand-300: #D8D8D8;
  --sony-color-brand-500: #111111;
  --sony-color-brand-600: #000000;   /* canonical */
  --sony-color-brand-900: #000000;

  /* Surfaces */
  --sony-bg-page:   #FFFFFF;
  --sony-bg-dark:   #000000;
  --sony-bg-strip:  #F6F6F4;
  --sony-text:      #111111;
  --sony-text-muted:#656565;
  --sony-text-inv:  #FFFFFF;
  --sony-border:    #D8D8D8;
  --sony-link-blue: #3860BE;

  /* Key spacing */
  --sony-space-sm:  16px;
  --sony-space-md:  30px;
  --sony-space-lg:  44px;

  /* Radius */
  --sony-radius-sm: 0;
  --sony-radius-md: 0;
  --sony-radius-control: 999px;
}

body {
  margin: 0;
  background: var(--sony-bg-page);
  color: var(--sony-text);
  font-family: var(--sony-font-family);
  font-weight: var(--sony-font-weight-normal);
  letter-spacing: 0;
}

.sony-header {
  height: 72px;
  background: var(--sony-bg-dark);
  color: var(--sony-text-inv);
  display: flex;
  align-items: center;
  gap: 32px;
  padding: 0 44px;
}

.sony-hero {
  position: relative;
  overflow: hidden;
  background: var(--sony-bg-dark);
  color: var(--sony-text-inv);
}

.sony-hero__backdrop {
  position: absolute;
  inset: 0;
  background: center / cover no-repeat;
  filter: blur(18px);
  transform: scale(1.08);
  opacity: .55;
}

.sony-hero__slide {
  position: relative;
  z-index: 1;
  border-radius: 0;
  box-shadow: none;
}

.sony-play {
  width: 45px;
  height: 45px;
  border-radius: 50%;
  background: rgba(0,0,0,.75);
  color: #FFFFFF;
}

.sony-news-strip {
  min-height: 72px;
  background: var(--sony-bg-strip);
  border: 0;
  display: grid;
  grid-template-columns: 150px 1fr;
  align-items: center;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js - Sony Group Portal approximation
module.exports = {
  theme: {
    extend: {
      colors: {
        sony: {
          black: '#000000',
          ink: '#111111',
          white: '#FFFFFF',
          strip: '#F6F6F4',
          hairline: '#D8D8D8',
          muted: '#656565',
          link: '#3860BE',
        },
      },
      fontFamily: {
        sony: ['SST W20 Roman', 'SST W55 Regular', 'Yu Gothic Medium', 'YuGothic', 'sans-serif'],
        sonyBold: ['SST W20 Bold', 'SST W55 Bold', 'sans-serif'],
      },
      borderRadius: {
        sony: '0',
        media: '999px',
      },
      boxShadow: {
        sony: 'none',
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
| Brand primary | `sony.black` | `#000000` |
| Background | `sony.white` | `#FFFFFF` |
| Hero text | `sony.white` | `#FFFFFF` |
| Text primary | `sony.ink` | `#111111` |
| Text muted | `sony.muted` | `#656565` |
| Border | `sony.hairline` | `#D8D8D8` |
| Utility link | `sony.link-blue` | `#3860BE` |

### Example Component Prompts

#### Hero Section

```text
Sony Group Portal 스타일 히어로 섹션을 만들어줘.
- 배경: #000000 with blurred active-media backdrop, not a gradient
- Layout: Swiper-like filmstrip; center slide dominant, neighboring slides visible
- H1: SST W20 Bold, compact 20-24px visual, weight 700, tracking 0
- Category: bold white text above or near title
- Description: white, 14-16px, line-height around 1.35
- Play control: 45px circular rgba(0,0,0,.75) disc with white triangle
- No rounded CTA cards, no blue primary button
```

#### News Strip

```text
Sony homepage news strip을 만들어줘.
- Background: #F6F6F4 or #FFFFFF
- Left label: "Latest News", bold, separated by #D8D8D8 vertical divider
- Right content: single corporate headline, #111111, 14px
- Radius: 0, shadow: none
- Keep it flat and informational
```

#### Navigation

```text
Sony global header를 만들어줘.
- Height: about 72px
- Background: #000000
- Logo: white Sony wordmark on left
- Links: compact white text, 14px, no pills
- Right utilities: Contact Us + search icon
- Mobile: collapse to hamburger; keep black chrome
```

### Iteration Guide

- **색상 변경 시**: UI chrome is monochrome. Do not make #3860BE the homepage CTA system.
- **폰트 변경 시**: keep SST-like neutral sans proportions. Do not introduce serif headlines except the Sony logo asset.
- **여백 조정 시**: maintain compressed header and wider hero media field; avoid airy SaaS hero spacing.
- **새 컴포넌트 추가 시**: radius 0, shadow none, hairline dividers, typography-first labels.
- **다크 모드**: the first viewport already mixes dark hero with light content below. Do not invert the entire page into a black dashboard.
- **반응형**: preserve 641px image-source switch and 44px minimum media controls.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#000000` as the canonical brand chrome for header and hero stage.
- Keep the post-hero body light with `#FFFFFF` and `#F6F6F4` utility strips.
- Let photography/video supply saturated color; keep UI controls monochrome.
- Use SST W20/W55 or close neutral sans substitutes at 400/700.
- Reserve circular shapes for media controls, especially play/pause.
- Use thin dividers such as `#D8D8D8` rather than card borders and shadows.
- Build the hero as a carousel/filmstrip with neighboring media visible.
- Keep copy formal and content-specific: category, title, description, date.

### ❌ DON'T

- 배경 chrome을 `#FFFFFF` 또는 `white`로 두지 말 것 — header/hero chrome은 `#000000` 사용.
- hero overlay 텍스트를 `#111111` 또는 `#000000`으로 두지 말 것 — dark media 위에서는 `#FFFFFF` 사용.
- homepage primary CTA를 `#3860BE`로 만들지 말 것 — Sony homepage primary identity는 `#000000`/`#FFFFFF` monochrome.
- news strip divider를 `#000000`으로 두껍게 긋지 말 것 — `#D8D8D8` hairline 사용.
- page body를 `#F4F4F4` 같은 generic Apple gray로 덮지 말 것 — Sony captured body/news surfaces are `#FFFFFF` and `#F6F6F4`.
- body에 `font-weight: 300` 사용 금지 — captured SST body behavior is normal 400, with bold labels at 700.
- large rounded cards에 `border-radius: 16px` 사용 금지 — first-viewport media and strips use radius 0.
- component depth에 `box-shadow: 0 20px 40px rgba(0,0,0,.15)` 사용 금지 — Sony depth is media/backdrop, not card elevation.
- CTA pills에 `border-radius: 999px` 남발 금지 — 999px is for circular media controls, not every button.
- purple AI gradient `#667EEA` to `#764BA2` 사용 금지 — no gradient-token UI in the captured Sony homepage.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second brand color: none. Blue appears in search/link/consent contexts but does not define the homepage.
- Gradient-based brand surfaces: absent. The hero atmosphere is image-derived blur, not a synthetic mesh.
- Rounded marketing cards: absent in the first viewport. Media tiles are square-edged.
- SaaS CTA hierarchy: absent. No primary blue pill plus secondary outline pair in the hero.
- Decorative icon rows: absent. Icons are functional: search, arrows, play, pause, sitemap toggles.
- Heavy drop shadows: absent. No elevation stack for news, hero, header, or sitemap.
- Oversized display typography: absent. The hero uses compact overlay copy rather than 64px+ headlines.
- Pastel neutrals: absent. The neutral system is black/white/gray, not cream-beige editorial warmth.
- Friendly illustration style: absent. Real entertainment/product imagery carries the page.
- Playful hover motion: absent from the observed first viewport. Movement belongs to carousel/video systems.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Main Sony template CSS partially unavailable** — cached `styles.css`, `gnavi.css`, `footer.css`, `sitemap.css`, and related template CSS files contain Access Denied HTML. Layout values for those components are therefore visual/HTML-derived, not fully CSS-derived.
- **Homepage single-state capture** — screenshot shows one desktop viewport and one active hero slide. Dropdown, hamburger-open, search-open, and modal video states were not visually measured.
- **Color frequency contamination** — `brand_candidates.json` includes OneTrust consent and Marsflag search CSS. Consent greens (`#468254`, `#68B631`) and Swiper default blue (`#007AFF`) are not treated as Sony brand colors.
- **Typography scale incomplete** — phase1 `typography.json` detected families and weights but no full scale entries. Font sizes are visual approximations from the screenshot and semantic HTML roles.
- **Responsive behavior inferred** — breakpoints are from cached CSS/media attributes, especially 641px image source switching and search CSS media queries. Mobile screenshots were not captured in this run.
- **Motion curves not fully extracted** — Swiper and video controls are identified, but exact carousel duration/easing and custom script behavior were not analyzed.
- **Dark/light token mapping absent** — Sony exposes a mixed dark hero/light content composition, not a formal theme token map.
- **Sub-flow surfaces not visited** — Businesses & Products, Technology, Sustainability, Design, Careers, IR, search results, and cookie preference panels may use additional component rules outside the homepage.
