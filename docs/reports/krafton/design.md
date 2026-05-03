---
schema_version: 3.2
slug: krafton
service_name: KRAFTON
site_url: https://www.krafton.com/
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#FF3B33"
primary_font: "Zalando Sans Expanded"
font_weight_normal: 400
token_prefix: wp

bold_direction: "Blackout Editorial"
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: editorial-product
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "WordPress theme CSS exposes repeated layout, motion, card, and typography patterns, but not a formal public token system."

colors:
  blackout: "#000000"
  white: "#FFFFFF"
  hero-red: "#FF3B33"
  brand-blue: "#0073A8"
  text-muted: "#767676"
  hairline: "#DDDDDD"
typography:
  display: "Zalando Sans Expanded"
  brand: "KRAFTON"
  body: "Noto Sans"
  latin-body: "Poppins"
  ladder:
    - { token: hero-wordmark, size: "7.27vw", weight: 800, tracking: "0" }
    - { token: page-title-large, size: "140px / 10.769vw", weight: 700, tracking: "0" }
    - { token: section-title, size: "36px / 2.7692vw", weight: 600, tracking: "0" }
    - { token: card-title, size: "24px / 1.846vw", weight: 600, tracking: "0" }
    - { token: nav-link, size: "18px", weight: 500, tracking: "0" }
  weights_used: [300, 400, 500, 600, 700, 800, 900]
  weights_absent: []
components:
  header-nav-link: { font: "Zalando Sans Expanded", size: "18px", weight: 500, padding: "31px 30px 29px" }
  hero-visual-box: { height: "30.677vw", inset_x: "4.11458vw", background: "video/image composite" }
  game-card: { bg: "#000000", overlay: "rgba(0,0,0,0.3)", aspect: "67.2%", title: "#FFFFFF" }
  skew-tag: { bg: "#000000", skew: "20deg", padding: "6px 22px 6px 11px" }
  studio-card: { columns: 4, padding: "49px 30px 34px", border_top: "1px solid #000000" }
---

# DESIGN.md — KRAFTON

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

KRAFTON opens like a game publisher stage in the blackout second before the trailer starts. The first viewport is almost entirely #000000 (`{colors.blackout}`), and the brand does not try to soften that darkness with gradients, blur, glass, or decorative UI chrome. It is a cinema screen before projection: no scenery, no side color, only a void with enough physical weight for one huge red statement to hit it.

The homepage behaves less like SaaS marketing and more like a title sequence burned onto a black screen. "PIONEER THE UNDISCOVERED" arrives in a red close to #FF3B33 (`{colors.hero-red}`), not as button color, not as accent system, but as the single flare in the room. There is no second expressive hero color; the WordPress preset blue (`{colors.brand-blue}`) belongs to the underlying corporate machinery, while the public memory of the page is black screen plus red discovery typography.

The top navigation is almost a game launcher shell laid over the film frame. It is clean and corporate, but the hero underneath is cinematic: a `100vh` container, an internal `.KeyVisualBox` centered vertically, a video/image composite behind clipped text rows, and a small animated scroll cue. The page has little "website self-consciousness"; it removes ordinary landing-page furniture so the publisher identity can sit on stage like an opening logo before gameplay footage.

Typography carries most of the force. "Zalando Sans Expanded" makes the nav labels feel like interface text from a franchise menu, while the custom "KRAFTON" face takes over large page titles like a studio masthead. There is almost no optical tracking trick here. The identity is not Apple-like ink precision; it is width, mass, and block pressure, as if the letters were cut from matte black set pieces and lit by the red title card.

The system is blunt but not primitive. Cards slide in, thumbnails reveal upward, tags skew, images scale on hover, and sections move through opacity/transform classes such as `.a-Opacity` and `.MainGameSlide`. Depth does not come from card shadows; shadow is effectively replaced by photography, black overlays, and motion timing. KRAFTON's craft is in choreography and cropping: rectangular media panels, tactical skew tags, white labels over dark imagery, and a stage that keeps returning to `{colors.blackout}` whenever the brand needs impact.

### Key Characteristics

- Blackout first viewport: #000000 stage, white nav, red hero statement.
- Oversized expanded typography: hero and nav rely on width-heavy display shapes.
- Brand-red hero is visual content, not a normal button color system.
- Corporate WordPress structure underneath: menus, news posts, careers, studios, games.
- Motion vocabulary: opacity fades, translateY reveal, translateX slide, image scale hover.
- Skewed category tags: black parallelogram labels over game thumbnails.
- Media cards use dark overlays and white type instead of bordered card chrome.
- Responsive CSS is breakpoint-heavy: 1300px / 1024px / 767px tiers repeat throughout.
- Token system is shallow; repeated component rules matter more than named design tokens.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Blackout Editorial
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **blackout stage plus oversized red discovery typography**으로 기억된다.
> **Code Complexity**: high — 100vh hero, clipped video/image layers, ScrollMagic/TweenMax scripts, Swiper carousels, and multiple transform reveal states.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 KRAFTON처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Wide display nav + sober body */
body {
  font-family: "Noto Sans", "Noto Sans KR", "Poppins", sans-serif;
  font-weight: 400;
}
.nav-link,
.hero-word {
  font-family: "Zalando Sans Expanded", "Poppins", sans-serif;
  font-weight: 800;
  letter-spacing: 0;
}

/* 2. Blackout stage */
:root { --bg: #000000; --fg: #FFFFFF; --hero-red: #FF3B33; }
.hero { min-height: 100vh; background: var(--bg); color: var(--fg); }

/* 3. Huge red title sequence */
.hero-word {
  color: var(--hero-red);
  font-size: clamp(64px, 7.27vw, 140px);
  line-height: .92;
  text-transform: uppercase;
}
```

**절대 하지 말아야 할 것 하나**: 히어로를 흰 배경의 일반 중앙정렬 랜딩 페이지로 바꾸지 말 것. KRAFTON의 첫인상은 #000000 무대와 거대한 red discovery statement다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.krafton.com/` |
| Fetched | 2026-05-03 |
| Extractor | Existing phase1 reused + targeted live CSS URL fetch with Chrome UA |
| HTML size | 91,996 bytes (WordPress theme page) |
| CSS files | 12 linked CSS files observed, live CSS total approx. 626,548 chars |
| Token prefix | `wp` |
| Method | Existing `phase1` JSON + homepage screenshot + theme CSS pattern inspection |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: WordPress theme (`/wp-content/themes/krafton/`) with AIOSEO and cookie-law plugin CSS.
- **Design system**: Theme-level CSS, not a public DS namespace. WordPress preset token `--wp--preset--color--primary: #0073A8` exists, but the homepage hero is driven by custom theme assets and images.
- **CSS architecture**:
  ```css
  wp preset vars        (--wp--preset--*)       WordPress global presets
  theme CSS modules     header/page/component   layout, cards, nav, motion
  page-specific classes  KeyVisual/Main*        homepage visual system
  ```
- **Class naming**: PascalCase/BEM-ish theme classes: `.SiteHeaderMenu1Depth`, `.KeyVisualBoxText`, `.MainGameSlidePostThumbnail`.
- **Default theme**: mixed. Homepage hero is black; internal page components and lists return to white surfaces.
- **Font loading**: Local `@font-face` for Noto Sans KR/SC/JP, plus Google CSS for "Zalando Sans Expanded".
- **Canonical anchor**: homepage hero screenshot, especially the red "PIONEER THE UNDISCOVERED" block on black.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Zalando Sans Expanded` (loaded via Google Fonts CSS)
- **Brand/page display**: `KRAFTON` custom face (used for `.PageHeaderTitle-text.Text-lage`)
- **Body font**: `Noto Sans`, `Noto Sans KR`, `Poppins`, system fallbacks
- **Code font**: N/A — no code UI surface observed
- **Weight normal / bold**: `400` / `700`, with frequent `500`, `600`, and heavy display weights up to `800/900`

```css
:root {
  --wp-font-display: "Zalando Sans Expanded", "Poppins", sans-serif;
  --wp-font-brand: "KRAFTON";
  --wp-font-body: "Noto Sans", "Noto Sans KR", "Poppins", sans-serif;
  --wp-font-weight-normal: 400;
  --wp-font-weight-bold: 700;
}
body {
  font-family: var(--wp-font-body);
  font-weight: var(--wp-font-weight-normal);
}
```

### Note on Font Substitutes

- **Zalando Sans Expanded** — If unavailable, use **Archivo Expanded** or **Roboto Flex Expanded** at weight 800 for the hero/nav layer. Keep tracking at `0`; do not add artificial negative tracking because KRAFTON's width comes from the expanded face itself.
- **KRAFTON custom face** — If unavailable, use **Archivo Black** only for large title blocks, then slightly reduce line-height from `1em` to `.95em` to preserve the compressed block feeling.
- **Noto Sans KR** — Keep Noto Sans for Korean body text. Do not swap the whole site to Inter; the Korean metrics and multilingual fallback are part of the corporate layer.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `hero-wordmark` | `7.27vw` desktop visual text | 800-900 visual mass | `.9-1.0` visual | `0` |
| `page-title-large` | `140px` / `10.769vw` | `bold` | `1em` | `0` |
| `page-title` | `70px` / `5.384vw` | `bold` | `1.3em` | `0` |
| `section-title` | `36px` / `2.7692vw` | `600` | `1.2em` | `0` |
| `game-card-title` | `29px` / `2.2307vw` | `500` | `1.2em` | `0` |
| `studio-card-title` | `24px` / `1.846vw` | `600` | `1.2em` | `0` |
| `nav-link` | `18px` | `500` | `1.3em` | `0` |
| `body` | `16px` | `400` | `1.4-1.7em` | `0` |
| `caption/tag` | `14px` / `1.0769vw` | `500` | `1.2em` | `0` |

> ⚠️ KRAFTON's type identity is not a refined editorial ladder. It is an impact split: very wide, very large display blocks over ordinary corporate body typography.

### Principles

1. Display type gets width before ornament. Use expanded fonts and massive scale before adding gradients, outlines, or shadows.
2. Body copy stays conventional. Noto Sans/Poppins at 400-500 anchors the site after the dramatic hero.
3. Weight 500 is a navigation/card workhorse, not an absent middle. Do not force a minimalist 400/700-only model.
4. Letter-spacing is mostly neutral. The site does not rely on tight Apple-like tracking compensation.
5. Korean/multilingual fallback matters. Keep Noto Sans KR/SC/JP available rather than designing only for English metrics.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed)

| Token | Hex |
|---|---|
| `wp--preset--color--primary` | `#0073A8` |
| `observed-hero-red` | `#FF3B33` |
| `observed-blackout` | `#000000` |
| `observed-white` | `#FFFFFF` |

### 06-2. Brand Dark Variant

> N/A — no formal dark variant ramp was exposed. The homepage uses a black stage, not a documented dark-mode palette.

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| `white` | `#FFFFFF` | N/A |
| `paper-light` | `#F7F7F7` | N/A |
| `hairline` | `#DDDDDD` | N/A |
| `muted` | `#767676` | N/A |
| `ink-soft` | `#222222` | N/A |
| `black` | N/A | `#000000` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Hero red | primary hero statement | `#FF3B33` (screenshot-observed) |
| WordPress primary | preset primary | `#0073A8` |
| Corporate teal | theme frequency | `#00ACAD` |
| Highlight yellow | theme frequency | `#F2A900` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `{colors.blackout}` | `#000000` | hero stage, dark thumbnail bases, selected bars |
| `{colors.white}` | `#FFFFFF` | nav on black, hero support copy, card text over media |
| `{colors.hero-red}` | `#FF3B33` | homepage discovery statement |
| `{colors.text-muted}` | `#767676` | secondary UI/copy in light sections |
| `{colors.hairline}` | `#DDDDDD` | tables and structural borders |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--wp--preset--color--primary` | `#0073A8` | WordPress preset primary, not the hero identity |
| `--krafton-bg-stage` | `#000000` | inferred homepage stage token |
| `--krafton-fg-stage` | `#FFFFFF` | inferred text on black |
| `--krafton-hero-red` | `#FF3B33` | inferred from screenshot because hero wording is image/visual asset |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| CSS black | `#000` | 401 |
| CSS white | `#FFF` | 239 |
| hairline gray | `#DDD` | 55 |
| soft ink | `#222` | 37 |
| full black | `#000000` | 14 |
| light panel | `#F7F7F7` | 14 |
| KRAFTON preset primary | `#0073A8` | 6 |
| teal accent | `#00ACAD` | 6 |

### 06-8. Color Stories

**`{colors.blackout}` (`#000000`)** — The main stage color. KRAFTON uses black not as dark mode but as theatrical control: it removes UI ambience so the red message and media assets feel like a title sequence.

**`{colors.white}` (`#FFFFFF`)** — Utility contrast. It appears in nav, hero support text, thumbnail titles, and tags over dark imagery; it should stay crisp and undecorated.

**`{colors.hero-red}` (`#FF3B33`)** — The homepage memory color. It is not a complete token ramp; it is a single visual shout used for the "PIONEER THE UNDISCOVERED" statement.

**`{colors.hairline}` (`#DDDDDD`)** — The corporate section divider. Once the page leaves the hero, light content uses restrained gray lines rather than colorful panels.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `container-x-desktop` | `40px` / `3.4769vw` | `.site-container` horizontal padding |
| `container-x-mobile` | `6.25vw` | mobile `.site-container` padding |
| `hero-x` | `4.11458vw` | `.KeyVisual-container` and `.KeyVisualBox` left/right inset |
| `hero-min-height` | `43.6893vw` | desktop min-height under 100vh hero |
| `section-bottom-news` | `88px` / `6.7692vw` | `.MainNews` section rhythm |
| `section-bottom-careers` | `94px` / `7.23076vw` | `.MainCareesrs` section rhythm |
| `studio-card-padding` | `49px 30px 34px` | studio card interior |
| `tag-padding` | `6px 22px 6px 11px` | skew thumbnail label |

**주요 alias**:
- `container` → `max-width: 1280px; padding: 0 40px` on desktop.
- `hero-inset` → `4.11458vw`, repeated for hero container and scroll control alignment.

### Whitespace Philosophy

KRAFTON uses space like stage blocking. The hero does not center a small marketing stack; it places a massive internal visual box inside a full viewport and leaves enough black around it for the red type to feel monumental. The empty space is not gentle whitespace; it is pressure.

Below the hero, spacing becomes modular and operational. News, careers, games, and studios sections use repeated viewport-based margins (`6.7vw`, `7.2vw`, `10.7vw`, `15.7vw`) to keep the page responsive without changing the underlying corporate grid.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `none` | `0` | dominant KRAFTON chrome and hero surfaces |
| `circle` | `50%` / `100%` | icon/round utility shapes |
| `small` | `3px-6px` | plugin/modal and minor UI pieces |
| `pill` | `9999px` | WordPress block default, not KRAFTON homepage signature |
| `cookie-button` | `0` | cookie buttons in screenshot are rectangular |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `none` | `box-shadow: none` | primary site chrome and cards |
| `cookie-bar` | `0 -1px 10px 0 rgba(172,171,171,0.3)` | cookie notice overlay |
| `plugin-again` | `#161616 2px 2px 5px 2px` | cookie-law plugin control |

KRAFTON does not build its homepage depth through card elevation. Depth is generated by black overlays, thumbnail crops, reveal motion, and full-bleed media.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `opacity-reveal` | `opacity 1.6s ease-out` | `.a-Opacity` fade-in |
| `vertical-reveal` | `transform/opacity 0.8s ease-out` | `.a-OpacityTop` |
| `title-rise` | `transform 0.6s ease-out` | `.MainInteractionTitle-text` |
| `slide-in` | `transform/opacity 1.2s` | `.MainGameSlide` |
| `thumb-scale` | `transform 0.4s ease-out` | game thumbnails |
| `image-rise` | `transform 0.6s ease-out` | `.ArrowPostThumnail-img` |
| `hero-bg` | `2.37s cubic-bezier(.92,.03,.39,.67)` | `.KeyVisualBoxBG` |
| `scroll-arrow` | `1.8s linear infinite` | hero scroll affordance |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `1280px`, then `98.461vw`, then full width with responsive padding.
- **Grid type**: mixed. Header uses floated menu items; studio cards use 4-column float; carousels use Swiper; cards use absolute-positioned media overlays.
- **Column count**: 4 for studios, 2-ish for careers/news cards, sliding partial widths for game carousel.
- **Gutter**: `40px` desktop card gutters, viewport-scaled to `3.0769vw` and larger mobile values.

### Hero

- **🆕 Pattern Summary**: `100vh + black stage + centered clipped video/image visual box + oversized red title sequence + small scroll cue`
- Layout: full viewport, internal absolute `.KeyVisualBox` centered with `top: 50%; transform: translateY(-50%)`.
- Background: black stage with layered `.KeyVisualBoxBG` media and red visual text.
- **🆕 Background Treatment**: image/video composite with clipped internal regions; not a CSS gradient mesh.
- H1: visual asset / display-word block, approx. `7.27vw` rows, very heavy expanded shape.
- Max-width: visual box spans from `left: 4.11458vw` to `right: 4.11458vw`.

### Section Rhythm

```css
.site-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 40px;
}
.KeyVisual-container {
  height: 100vh;
  padding: 0 4.11458vw;
  min-height: 43.6893vw;
}
```

### Card Patterns

- **Card background**: usually image/media, with black or white supporting areas.
- **Card border**: `1px solid #000000` for studio content top line; tables use `#DDDDDD`.
- **Card radius**: mostly `0`; image cards are rectangular.
- **Card padding**: `49px 30px 34px` for studio cards; thumbnails place text absolutely.
- **Card shadow**: none.

### Navigation Structure

- **Type**: horizontal mega-nav style, with language utility on the right.
- **Position**: absolute/relative header over hero; subdepth backgrounds available.
- **Height**: link padding `31px 30px 29px`, roughly 80px top nav.
- **Background**: transparent/black in hero screenshot; subdepth bars invert between black and white.
- **Border**: animated `.SiteHeaderBar` 5px/0.3846vw underline bar on active/hover states.

### Content Width

- **Prose max-width**: N/A, homepage is component/card driven.
- **Container max-width**: `1280px`.
- **Sidebar width**: N/A for homepage.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `1px-767px` | Repeated mobile rules, larger vw-based type and padding, mobile visual text variant |
| Tablet | `768px-1024px` | Intermediate typography and card sizing |
| Desktop | `1025px-1300px` | Desktop layout scaled with vw units |
| Large | `1301px+` / `1441px+` / `1920px` | Large desktop refinements appear in selected page rules |

### Touch Targets

- **Minimum tap size**: not fully documented; header links are large on desktop, cookie buttons are visibly >44px high.
- **Button height (mobile)**: not reliably extracted from homepage state.
- **Input height (mobile)**: not observed in homepage capture.

### Collapsing Strategy

- **Navigation**: desktop horizontal menu; mobile classes (`Mobile-view`, `.mo`) indicate a separate mobile presentation.
- **Grid columns**: studio/game/news cards shift from fixed/floated desktop widths to larger vw/near-full-width items.
- **Sidebar**: N/A.
- **Hero layout**: `.KeyImgBox.pc` hidden and `.KeyImgBox.mo` displayed on mobile, preserving the title-sequence identity with different assets.

### Image Behavior

- **Strategy**: absolute-positioned images inside ratio boxes.
- **Max-width**: images use width `100%`; containers define aspect via pseudo-element padding.
- **Aspect ratio handling**: game thumbnails use `padding-bottom: 67.2%`; ArrowPost thumbnails use `37.7%`.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

KRAFTON homepage does not foreground a classic CTA button system. The visible cookie controls are rectangular, high-contrast plugin buttons: one white filled settings button and one black/transparent accept button with white border. If recreating the site, keep primary brand actions rectangular and severe unless a subpage shows a different CTA pattern.

### Badges

The signature badge is the skewed black thumbnail tag:

```css
.MainGameSlidePostThumbnail-tag:before {
  background-color: #000000;
  transform: skewX(20deg);
}
.MainGameSlidePostThumbnail-tagbar {
  color: #FFFFFF;
  font-family: "Poppins";
  font-weight: 500;
  padding: 6px 22px 6px 11px;
}
```

### Cards & Containers

Game cards are media-first. The image fills the card, a `rgba(0,0,0,0.3)` overlay protects white titles, and the card uses animation rather than border or shadow for polish. Studio cards are more corporate: four columns, rectangular blocks, `padding: 49px 30px 34px`, and a top border line.

### Navigation

Header links use `Zalando Sans Expanded`, `18px`, `500`, with `31px 30px 29px` padding. The navigation feels like a game launcher shell: wide labels, high confidence, no rounded pills, no icon clutter.

### Inputs & Forms

No main homepage input system was observed. Cookie preference modal/plugin CSS exists, but it should not be treated as KRAFTON's native form system.

### Hero Section

The hero is the primary component. It combines `height: 100vh`, black stage, `.KeyVisualBox` absolute centering, clipped video/image layers, red visual text rows, small support copy, and a scroll arrow animation.

### 13-2. Named Variants

- **header-nav-link** — expanded-font top-level menu link; `18px`, `500`, wide padding, no pill background.
- **hero-visual-box** — 100vh internal title-sequence module with `30.677vw` height and clipped media layers.
- **skew-thumbnail-tag** — black skewed label with white Poppins text, used over game thumbnails.
- **media-overlay-card** — image card with `rgba(0,0,0,0.3)` overlay and white title.
- **studio-grid-card** — four-column corporate card with top rule and arrow reveal.

### 13-3. Signature Micro-Specs

```yaml
blackout-title-sequence:
  description: "Homepage identity system: red discovery typography over a black entertainment-stage void."
  technique: "height: 100vh; min-height: 43.6893vw; padding-inline: 4.11458vw; .KeyVisualBox centered with top:50% + translateY(-50%); hero text approx. 7.27vw in #FF3B33"
  applied_to: ["{component.hero-visual-box}", "KeyVisual first viewport"]
  visual_signature: "A brand film title card rather than a normal web hero."

clipped-media-wordmark-box:
  description: "The hero is built as a contained visual box where media and typography are composited instead of stacked as separate content blocks."
  technique: ".KeyVisualBox height: 30.677vw; left/right inset: 4.11458vw; .KeyVisualBoxBG transition: 2.37s cubic-bezier(.92,.03,.39,.67); video/image composite behind clipped text rows"
  applied_to: ["{component.hero-visual-box}", "KeyVisualBoxBG"]
  visual_signature: "A game trailer frame trapped inside oversized red wordmark choreography."

skewed-game-taxonomy-tag:
  description: "Game/category tags are not rounded badges; they are angled black strips."
  technique: "pseudo-element background #000000 with transform: skewX(20deg); label color #FFFFFF; font-family: Poppins; font-weight: 500; padding: 6px 22px 6px 11px"
  applied_to: ["{component.skew-tag}", "MainGameSlidePostThumbnail"]
  visual_signature: "Sharper and more tactical than a SaaS badge."

media-overlay-card-motion:
  description: "Cards behave as animated media panels, with darkness and movement doing the work normally assigned to borders or elevation."
  technique: "thumbnail base #000000; overlay rgba(0,0,0,0.3); aspect padding-bottom: 67.2%; hover transform 0.4s ease-out; reveal translateY(100%) to translateY(0%) over 0.6s ease-out"
  applied_to: ["{component.game-card}", "{component.media-overlay-card}", "ArrowPostThumnail-img"]
  visual_signature: "Images feel loaded into view like game UI panels rather than placed as static cards."

inverted-mechanical-nav-bar:
  description: "Header state is marked by a thin bar that changes polarity against dark or light surfaces, never by a rounded active pill."
  technique: "header link padding: 31px 30px 29px; nav font: Zalando Sans Expanded 18px/500; .SiteHeaderBar height approx. 5px / 0.3846vw; bar background flips #000000 on light and #FFFFFF on .Bg-black"
  applied_to: ["{component.header-nav-link}", "SiteHeaderBar"]
  visual_signature: "A mechanical underline that reads like interface hardware over the cinematic stage."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Short, uppercase, declarative, mythic | "PIONEER THE UNDISCOVERED" |
| Primary CTA | Low emphasis on homepage hero; navigation carries action | "Careers", "IR", "News" |
| Subheading | Corporate mission phrasing with imaginative language | "Create the original. Connect the world." |
| Section labels | Plain business taxonomy | "News", "Careers", "KRAFTON GAMES", "Studios" |
| Tone | Entertainment-company confidence, not startup cheerfulness | "We pioneer the path to players' dreams." |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* KRAFTON — copy into your root stylesheet */
:root {
  /* Fonts */
  --wp-font-display: "Zalando Sans Expanded", "Poppins", sans-serif;
  --wp-font-brand: "KRAFTON";
  --wp-font-body: "Noto Sans", "Noto Sans KR", "Poppins", sans-serif;
  --wp-font-weight-normal: 400;
  --wp-font-weight-bold: 700;

  /* Brand / stage */
  --wp-color-brand-25:  #FFF4F3;
  --wp-color-brand-300: #FF7A72;
  --wp-color-brand-500: #FF3B33;
  --wp-color-brand-600: #F9423A;
  --wp-color-brand-900: #7A0F0A;

  /* Surfaces */
  --wp-bg-page:   #FFFFFF;
  --wp-bg-dark:   #000000;
  --wp-text:      #000000;
  --wp-text-muted:#767676;
  --wp-hairline:  #DDDDDD;

  /* Key spacing */
  --wp-space-sm:  14px;
  --wp-space-md:  40px;
  --wp-space-lg:  6.25vw;

  /* Radius */
  --wp-radius-sm: 0;
  --wp-radius-md: 0;
}

.krafton-hero {
  min-height: 100vh;
  background: var(--wp-bg-dark);
  color: #FFFFFF;
  padding: 0 4.11458vw;
  position: relative;
  overflow: hidden;
}
.krafton-hero__word {
  font-family: var(--wp-font-display);
  font-size: clamp(64px, 7.27vw, 140px);
  line-height: .92;
  font-weight: 900;
  color: var(--wp-color-brand-500);
  text-transform: uppercase;
}
.krafton-skew-tag {
  position: relative;
  display: inline-block;
  color: #FFFFFF;
  font: 500 14px/1.2 "Poppins", sans-serif;
  padding: 6px 22px 6px 11px;
}
.krafton-skew-tag::before {
  content: "";
  position: absolute;
  inset: 0 -20px 0 -30px;
  z-index: -1;
  background: #000000;
  transform: skewX(20deg);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — KRAFTON-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        krafton: {
          black: '#000000',
          white: '#FFFFFF',
          red: '#FF3B33',
          blue: '#0073A8',
          hairline: '#DDDDDD',
          muted: '#767676',
        },
      },
      fontFamily: {
        display: ['Zalando Sans Expanded', 'Poppins', 'sans-serif'],
        brand: ['KRAFTON', 'Arial Black', 'sans-serif'],
        sans: ['Noto Sans', 'Noto Sans KR', 'Poppins', 'system-ui'],
      },
      borderRadius: {
        krafton: '0px',
      },
      transitionTimingFunction: {
        krafton: 'ease-out',
        'krafton-hero': 'cubic-bezier(.92,.03,.39,.67)',
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
| Brand primary | `{colors.hero-red}` | `#FF3B33` |
| Background | `{colors.blackout}` | `#000000` |
| Text primary | `{colors.white}` on hero / `{colors.blackout}` on light | `#FFFFFF` / `#000000` |
| Text muted | `{colors.text-muted}` | `#767676` |
| Border | `{colors.hairline}` | `#DDDDDD` |
| Success | N/A | N/A |
| Error | N/A | N/A |

### Example Component Prompts

#### Hero Section
```text
KRAFTON 스타일 히어로 섹션을 만들어줘.
- 배경: #000000 full-viewport stage
- H1: Zalando Sans Expanded, clamp(64px, 7.27vw, 140px), weight 900, tracking 0
- H1 색: #FF3B33, uppercase, line-height .92
- 서브텍스트: #FFFFFF, small corporate mission copy
- 레이아웃: 좌우 4.11458vw inset, 100vh, visual box centered vertically
- 모션: opacity 1.6s ease-out + title/media translate reveal
```

#### Game Card
```text
KRAFTON 스타일 게임 카드 컴포넌트를 만들어줘.
- 배경: image thumbnail with #000000 base
- overlay: rgba(0,0,0,0.3)
- aspect ratio: 67.2% padding-bottom
- title: #FFFFFF, Poppins/Noto Sans, 29px desktop, weight 500
- tag: black skewed strip, transform skewX(20deg), white 14px Poppins 500
- hover: image scale via transform .4s ease-out
```

#### Navigation
```text
KRAFTON 스타일 상단 네비게이션을 만들어줘.
- 배경: hero에서는 투명/검정, light section에서는 white
- 로고: 좌측 KRAFTON wordmark
- 링크: Zalando Sans Expanded, 18px, weight 500, padding 31px 30px 29px
- active: filled pill 금지, 5px underline/bar만 사용
- 언어 선택: 우측 compact uppercase labels
```

### Iteration Guide

- **색상 변경 시**: hero identity는 `#000000 + #FF3B33 + #FFFFFF` 삼각형을 유지한다.
- **폰트 변경 시**: nav/hero에는 expanded face를 유지하고, body는 Noto Sans 계열을 유지한다.
- **여백 조정 시**: hero inset `4.11458vw`, container `1280px + 40px` 패턴에서 벗어나지 않는다.
- **새 컴포넌트 추가 시**: radius/shadow를 늘리기보다 media crop, black overlay, transform reveal을 사용한다.
- **반응형**: 1300 / 1024 / 767 breakpoint 체계를 우선 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#000000` as the first-viewport stage and let the hero breathe inside it.
- Keep the hero statement red and massive; it should read as a title sequence, not CTA copy.
- Use expanded display typography for nav and hero, with neutral tracking.
- Treat cards as media panels: dark overlay, white title, reveal/scale motion.
- Use rectangular UI chrome and thin active bars rather than rounded SaaS pills.
- Preserve the multilingual font stack, especially Noto Sans KR/SC/JP.
- Use viewport-based responsive values where the original CSS does: `4.11458vw`, `6.25vw`, `7.27vw`.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두고 히어로를 시작하지 말 것 — 대신 첫 viewport는 `#000000` stage 사용.
- 히어로 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 red statement `#FF3B33` 계열 사용.
- 히어로 primary color를 WordPress preset `#0073A8`로 대체하지 말 것 — KRAFTON homepage memory color는 `#FF3B33`이다.
- 카드 배경을 `#FFFFFF` bordered card로 만들지 말 것 — 대신 media thumbnail + `rgba(0,0,0,0.3)` overlay 사용.
- 구조선을 `#CCCCCC` 위주로 두껍게 깔지 말 것 — 필요한 hairline은 `#DDDDDD` 또는 `#000000` top rule로 제한.
- nav active를 rounded pill로 만들지 말 것 — 대신 `#FFFFFF`/`#000000` 5px bar inversion 사용.
- body 전체를 `font-weight: 300`으로 만들지 말 것 — 본문은 400, nav/card는 500-600, display는 heavy.
- 모든 transition을 `all 0.2s`로 통일하지 말 것 — reveal은 0.6s/0.8s/1.6s 등 목적별 duration을 분리한다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- No pastel ambience: the homepage does not soften itself with cream, beige, lavender, or pale gradients.
- No SaaS hero card: there is no centered headline plus two rounded CTA buttons as the primary identity.
- No soft shadow card system: homepage depth comes from media, black overlays, and motion.
- No rounded product tiles: dominant cards are rectangular image panels.
- No second expressive brand color in the hero: red carries the statement alone.
- No decorative icon grid in the first viewport: nav and logo are restrained; the hero text owns attention.
- No Apple-like micro tracking system: letter-spacing is almost entirely neutral.
- No visible form/input design language on the homepage: plugin cookie UI is not the native brand system.
- No generic Inter-only stack: expanded display type and Noto multilingual body matter.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Hero red is screenshot-derived** — the red statement appears as a visual/image layer, so `#FF3B33` is an observed approximation rather than a named CSS token.
- **Existing phase1 CSS cache was incomplete** — local cached CSS contained WordPress defaults; live linked theme CSS was fetched by exact href for stronger evidence.
- **Homepage only** — subpages such as Games detail, Careers application flows, IR reports, and CSR pages may introduce different UI states.
- **Form states not surfaced** — native input, validation, loading, and error states were not visible in the homepage capture.
- **Cookie UI is plugin UI** — cookie buttons and preference controls were observed but should not be over-weighted as KRAFTON-native components.
- **Motion runtime not fully replayed** — CSS and script references (`ScrollMagic`, `TweenMax`, `Swiper`) were observed, but every scroll-trigger sequence was not interactively audited.
- **Mobile screenshot not captured in this pass** — responsive behavior is based on CSS breakpoints and class rules, not a separate mobile visual inspection.
- **Formal token system absent** — several aliases in this file are guidebook aliases for implementation, not proof of first-party named tokens.
