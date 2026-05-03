---
schema_version: 3.2
slug: meta
service_name: Meta
site_url: https://meta.com
fetched_at: 2026-04-14T01:14:00+09:00
default_theme: mixed
brand_color: "#0064E0"
primary_font: "Optimistic Display"
font_weight_normal: 400
token_prefix: "stylex/x"

bold_direction: "Immersive Corporate"
aesthetic_category: "editorial-product"
signature_element: "hero_impact"
code_complexity: high

medium: web
medium_confidence: high

archetype: editorial-product
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "StyleX atomic classes, Optimistic font stack, 902 CSS variables, and action/component/core token layers are present, but no public DS namespace is exposed."

colors:
  primary: "#0064E0"
  quest-blue: "#0095F6"
  meta-blue: "#1877F2"
  ink: "#1C2B33"
  secondary-ink: "#465A69"
  surface: "#FFFFFF"
  wash: "#F1F4F7"
  hairline: "#CBD2D9"
  dark: "#0A1317"
typography:
  display: "Optimistic Display"
  body: "Optimistic Text"
  fallback: "Montserrat, Helvetica, Arial, Noto Sans, sans-serif"
  ladder:
    - { token: hero, size: "4rem-8rem", weight: 700, line_height: "1.04-1.15", tracking: "-.01em to -.06em" }
    - { token: h2, size: "2.5rem-4rem", weight: 700, line_height: "1.125-1.2", tracking: "-.01em" }
    - { token: body, size: "1rem-1.125rem", weight: 400, line_height: "1.4-1.5", tracking: "0" }
    - { token: nav, size: "14px", weight: 600, line_height: "20px", tracking: "0" }
  weights_used: [200, 300, 400, 500, 600, 700, 800]
  weights_absent: []
components:
  button-primary: { bg: "{colors.primary}", color: "{colors.surface}", radius: "100px", min_height: "48px" }
  button-secondary-pill: { bg: "{colors.surface}", color: "{colors.ink}", radius: "100px", min_height: "48px" }
  dark-video-hero: { overlay: "rgba/black gradient", text: "{colors.surface}", control: "circular translucent" }
  editorial-card: { bg: "{colors.surface}", radius: "24px-32px", shadow: "10px 10px 34px #0003" }
---

# DESIGN.md — Meta

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Meta's homepage is not a flat corporate brochure. It behaves like a product showroom where the walls are made of video. The first screen is a darkened VR scene, with white type held in the center and the navigation floating above it like a heads-up display. The brand is visible, but it is not treated as a poster color; blue is reserved for decisive action, while the emotional work is carried by immersion, device footage, and human-scale photography.

The visual system is built around a controlled split: cinematic dark hero surfaces on top, clean white editorial sections below. The transition is abrupt and intentional, like walking out of a VR demo room into a bright product catalog. The hero asks for attention with motion and contrast; the next band returns to a practical commerce/editorial rhythm. This is the central Meta pattern: future-facing media first, conventional clarity immediately after.

Typography carries much of the identity. `Optimistic Display` gives the hero a rounded, consumer-tech softness, while `Optimistic Text` keeps supporting copy readable. Display sizes use tight tracking and large jumps; body and nav stay calmer. The headline behaves like keynote title type projected over a black stage, not like a dashboard heading. The site does not rely on a decorative brand palette. Its craft is the pairing of humanistic type, immersive footage, and pill controls.

The color identity is narrower than the logo suggests. The infinity logo may contain a gradient, but the UI does not become a rainbow; there is no second dominant brand color waiting offstage. The working system is #0064E0 (`{colors.primary}`) for action, #1C2B33 (`{colors.ink}`) for core text, #FFFFFF (`{colors.surface}`) for the editorial floor, and video-black overlays for drama. Meta's brand color appears as a tool, not wallpaper: a blue commerce switch inside a dark theater, then a blue link on a white catalog page.

The page has almost no social-network confetti. It does not scatter reactions, gradients, or app icons across the layout to prove the company is Meta. Instead, photography becomes the architecture: the hero media supplies depth, the white sections supply oxygen, and the rounded CTAs sit like physical controls on a headset interface. Shadow is allowed only where media or floating controls need it; the chrome itself stays quiet.

### Key Characteristics

- Full-bleed media hero with dark overlay and centered display type.
- Floating horizontal navigation over the hero, using white icon/text treatment.
- Optimistic Display/Text font pairing rather than generic Inter/system-only typography.
- Primary action blue #0064E0 appears mainly in CTAs and interactive affordances.
- Secondary CTA uses a pale/white pill, not an outline button.
- Editorial sections reset to #FFFFFF and #1C2B33 after the hero.
- Round/pill components are common: 100px CTA radius, circular icons, rounded media cards.
- StyleX atomic CSS produces many generated `--x*` variables, with semantic aliases layered on top.
- Video and product imagery carry the premium atmosphere; chrome remains restrained.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Immersive Corporate
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **dark video showroom hero with Optimistic display type**으로 기억된다.
> **Code Complexity**: high — StyleX atomic output, dense responsive media queries, overlay treatments, backdrop filters, and video-driven hero states all need careful reproduction.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Meta처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Optimistic Text", "Montserrat", Helvetica, Arial, "Noto Sans", sans-serif;
  font-weight: 400;
  color: #1C2B33;
}

h1,
h2,
.display {
  font-family: "Optimistic Display", "Montserrat", Helvetica, Arial, "Noto Sans", sans-serif;
  font-weight: 700;
  letter-spacing: -0.01em;
}

/* 2. 배경 + 텍스트 */
:root { --meta-bg: #FFFFFF; --meta-fg: #1C2B33; --meta-wash: #F1F4F7; }
body { background: var(--meta-bg); color: var(--meta-fg); }

/* 3. 브랜드 컬러 */
:root { --meta-blue: #0064E0; }
.cta-primary { background: var(--meta-blue); color: #FFFFFF; border-radius: 100px; }
```

**절대 하지 말아야 할 것 하나**: Meta 로고의 그라디언트를 전체 UI 배경으로 확장하지 말 것. 실제 UI는 #0064E0 액션, #1C2B33 텍스트, #FFFFFF/#F1F4F7 표면, 그리고 영상 오버레이로 구성된다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://meta.com` |
| Fetched | 2026-04-14T01:14:00+09:00 |
| Extractor | reused phase1 assets from `insane-design/meta/` |
| HTML size | 242467 bytes |
| CSS files | 16 external + 1 inline, total 1667186 characters |
| Token prefix | `stylex/x` plus semantic aliases such as `--primary-button-background` |
| Method | existing phase1 JSON + CSS token parsing + screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React/Meta web stack, rendered with dense StyleX-style atomic class output.
- **Design system**: Internal Meta UI tokens — generated `--x*` variables with semantic aliases such as `--primary-button-background`, `--secondary-button-background`, `--card-background`, `--surface-background`, and `--button-height-medium`.
- **CSS architecture**:
  ```text
  core       (--x*)                         generated raw/resolved values
  semantic   (--primary-text, --wash)        role-level aliases
  action     (--primary-button-background)   button/control API
  component  (--card-background)             component-level surfaces
  ```
- **Class naming**: generated atomic classes (`.x1...`) plus legacy Facebook-style classes in older embedded CSS.
- **Default theme**: mixed. Hero is dark video overlay; editorial content returns to #FFFFFF.
- **Font loading**: custom Optimistic family with fallbacks to Montserrat, Helvetica, Arial, Noto Sans, sans-serif.
- **Canonical anchor**: the current visible homepage hero: "Meta Quest brings the magic of virtual reality" over a VR video still with two pill CTAs.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Optimistic Display` (Meta brand font; not guaranteed on external systems)
- **Body font**: `Optimistic Text`
- **Fallback stack**: `Montserrat, Helvetica, Arial, Noto Sans, sans-serif`
- **Code font**: `Menlo, Consolas, Monaco, monospace`
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --meta-font-display: "Optimistic Display", "Montserrat", Helvetica, Arial, "Noto Sans", sans-serif;
  --meta-font-body: "Optimistic Text", "Montserrat", Helvetica, Arial, "Noto Sans", sans-serif;
  --meta-font-code: Menlo, Consolas, Monaco, monospace;
  --meta-font-weight-normal: 400;
  --meta-font-weight-bold: 700;
}

body {
  font-family: var(--meta-font-body);
  font-weight: var(--meta-font-weight-normal);
}
```

### Note on Font Substitutes

- **Optimistic Display** — If unavailable, use **Montserrat** at weight 700 for display, but tighten tracking by about `-0.01em` to `-0.02em`. Montserrat is a little more geometric and less soft, so keep line-height close to `1.04-1.15` on hero headings.
- **Optimistic Text** — If unavailable, use **Noto Sans** or Helvetica/Arial at 400/600. Avoid Inter as the first substitute: Meta's current homepage leans rounder and more consumer-facing than Inter's neutral SaaS tone.
- **Hero headings** — Preserve the large optical jump. Do not shrink the hero into a 48px SaaS headline; desktop display rules in the CSS reach `4rem`, `8rem`, and related responsive sizes.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Hero display | `4rem-8rem` | `700` | `1.04-1.15` | `-.01em` to `-.06em` |
| Large heading | `2.5rem-4rem` | `700` | `1.125-1.2` | `-.01em` |
| Section heading | `2rem-3rem` | `700` | `1.2` | `-.01em` or `0` |
| Body large | `1.125rem` | `400/500` | `1.4-1.5` | `0` |
| Body base | `1rem` | `400` | `1.4-1.5` | `0` |
| Navigation | `14px` | `600` | `20px` | `0` |
| Label/caption | `.75rem-.875rem` | `500/600` | `1.25-1.4` | `.02em` to `.04em` |

> ⚠️ Meta's typography is not "Inter + 16px body." The signature is Optimistic Display at very large sizes over immersive media, then restrained Optimistic Text in the content bands.

### Principles

1. Hero type is intentionally oversized and centered; the video background needs the text to behave as a broadcast title, not a normal landing-page H1.
2. Display tracking tightens at large sizes. Body copy does not inherit the aggressive negative tracking.
3. Weight 700 is common in display and nav emphasis, while body copy sits at 400/500. The contrast is weight plus size, not weight alone.
4. The font stack is brand-specific. Replacing Optimistic with generic system UI makes the page feel like a dashboard instead of a consumer hardware/editorial site.
5. Labels and navigation stay compact; the page spends typographic volume on hero statements and product/editorial headings.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed anchors)

| Token | Hex |
|---|---|
| `--secondary-button-text` / action blue | `#0064E0` |
| Quest/IG action blue candidate | `#0095F6` |
| Facebook legacy blue | `#1877F2` |
| darker blue action | `#0457CB` |
| link/action shadow blue | `#1D65C1` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| dark overlay floor | `#0A1317` |
| dark ink panel | `#152127` |
| dark text/control background | `#1C2B33` |
| secondary dark CTA surface | `#344854` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| surface | `#FFFFFF` | `#0A1317` |
| wash | `#F1F4F7` | `#152127` |
| soft border | `#E6EBEF` | `#25363F` |
| hairline | `#CBD2D9` | `#313D45` |
| muted text | `#465A69` | `#8696A0` |
| primary ink | `#1C2B33` | `#E9EDEF` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Meta blue | primary action | `#0064E0` |
| Quest/bright blue | product action | `#0095F6` |
| success/positive | status | `#007D1E` |
| warning | status | `#D69804` |
| critical | status | `#F53947` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `{colors.primary}` | `#0064E0` | main CTA/link action |
| `{colors.ink}` | `#1C2B33` | primary text on light surfaces |
| `{colors.secondary-ink}` | `#465A69` | muted text and secondary labels |
| `{colors.surface}` | `#FFFFFF` | editorial surface and secondary CTA |
| `{colors.wash}` | `#F1F4F7` | background wash/cards |
| `{colors.hairline}` | `#CBD2D9` | borders/dividers |
| `{colors.dark}` | `#0A1317` | dark hero/control floor |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--primary-button-background` | `#0064E0` / contextual variants | primary action backgrounds |
| `--primary-button-text` | `#FFFFFF` | primary CTA text |
| `--secondary-button-background` | `#FFFFFF` or `#344854` | secondary pill controls |
| `--secondary-button-text` | `#0064E0` | blue text/action alias |
| `--card-background` | `--dialog-background` / surface values | card/container panels |
| `--surface-background` | surface token | page and component surfaces |
| `--primary-text` | text token | body/headline text |
| `--secondary-text` | muted text token | supporting copy |

### 06-7. Dominant Colors (actual CSS frequency)

| Token | Hex | Frequency |
|---|---|---|
| white/surface | `#FFFFFF` | 64 full hex occurrences plus many `#FFF` shorthand occurrences |
| transparent/black alpha | `#0000001A` | 35 |
| primary ink | `#1C2B33` | 41 |
| Facebook/meta blue | `#1877F2` | 46 |
| wash | `#F1F4F7` | 32 |
| muted ink | `#465A69` | 32 |
| hairline | `#CBD2D9` | 24 |
| action blue | `#0064E0` | 22 |

### 06-8. Color Stories

**`{colors.primary}` (#0064E0)** — The operational Meta blue. It belongs on CTAs, links, and action states, not broad decorative panels. It is the button color you notice after the video has done the emotional work.

**`{colors.surface}` (#FFFFFF)** — The editorial floor. After the cinematic hero, Meta drops back to pure white so product modules and newsroom content can be scanned without visual residue.

**`{colors.ink}` (#1C2B33)** — A cool, blue-leaning ink rather than pure black. It keeps the corporate/product sections softer and more aligned with the Meta palette.

**`{colors.hairline}` (#CBD2D9)** — The structural gray-blue line. Borders and dividers stay cool; they should not become beige, warm gray, or generic `#DDDDDD` unless the source component explicitly does so.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| micro | `4px` | icon/text nudge, tight inline gaps |
| xs | `8px` | compact component gaps |
| sm | `12px` | small button/label rhythm |
| md | `16px` | mobile gutters, card internal gaps |
| lg | `24px` | common grid/card gap |
| xl | `32px` | desktop card gap and section internals |
| 2xl | `40px` | hero/button group and major text rhythm |
| 3xl | `48px` | section spacing, large block gaps |
| 4xl | `64px` | desktop editorial air |
| 5xl | `80px` | large section breathing room |
| giant | `120px` | sparse feature/gallery rhythm |

**주요 alias**:
- `--hzFeaturedCardSpacing` → `16px`, `24px`, `32px`, `38px` depending on breakpoint and carousel/card context.
- `--button-height-medium` → `32px` in compact embedded surfaces; hero CTAs visually use taller pill treatment.
- `--nav-list-cell-min-height-dense` → `42px` for dense navigation/list cells.

### Whitespace Philosophy

Meta uses a split whitespace model: the hero is visually full, almost crowded by video, but the text block itself is centered with enough air to read as a title card. The white sections below open up and become more editorial, with large headings separated from dense product/card rows.

Do not turn the whole page into evenly spaced SaaS bands. The correct rhythm is "immersive hero, hard reset, editorial/product modules." Card grids can be tighter, but section starts need enough vertical air for the content to feel like a corporate/product story rather than an app screen.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| tiny | `2px-4px` | legacy/embedded Facebook surfaces |
| small | `8px` | compact cards, mobile media corners |
| medium | `12px` | button corner variable in some surfaces |
| card | `20px-24px` | cards/dialogs/product modules |
| large card | `32px` | editorial image cards |
| pill | `100px` | hero CTA pills |
| full circle | `50%` | icon controls, video pause button, profile/cart icons |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: observed common values include `600px`, `680px`, `800px`, with wide media/card sections using larger responsive containers.
- **Grid type**: CSS Grid and Flexbox mixed; generated atomic classes handle `display`, `gap`, and breakpoint variants.
- **Column count**: homepage content shifts between single-column hero/editorial copy and multi-card product/news grids.
- **Gutter**: `16px` mobile, `24px-32px` standard desktop cards, up to `38px` in featured card contexts.

### Hero

- **Pattern Summary**: `100vh + full-bleed video/image overlay + centered H1 + dual pill CTA below`
- Layout: centered content over media, with global nav overlaid at the top.
- Background: video/image still with dark overlay and depth blur from the actual footage.
- **Background Treatment**: image/video overlay using dark transparent layers; CSS includes `linear-gradient(180deg,#0000 50%,#00000094)`, `linear-gradient(to top,rgba(0,0,0,.7) 0%,transparent 100%)`, and related overlay patterns.
- H1: `4rem-8rem` class family, weight `700`, tight display tracking.
- Max-width: visually centered title block around the middle of the 1280px viewport, narrower than the video frame.

### Section Rhythm

```css
section {
  padding-block: 64px 80px;
  padding-inline: 16px 32px;
  max-width: 1280px;
}
```

The exact CSS is atomic and component-scoped, so this is the reconstruction contract rather than a literal global rule.

### Card Patterns

- **Card background**: #FFFFFF or image/media surface.
- **Card border**: often none; hairlines appear with #CBD2D9/#E6EBEF in utility surfaces.
- **Card radius**: `24px-32px` for editorial/product cards.
- **Card padding**: `16px-32px` depending on density.
- **Card shadow**: limited and scoped; observed values include `10px 10px 34px #0003`, `0 4px 12px #0000004d`, and `0 2px 8px #00000014`.

### Navigation Structure

- **Type**: horizontal desktop navigation with product categories left and utility links/icons right.
- **Position**: overlay/static-at-top in the hero screenshot; visually floats over the media.
- **Height**: approximately `64px-80px` in the visible homepage hero.
- **Background**: transparent over dark hero media.
- **Border**: none in hero state.
- **Mobile strategy**: responsive CSS contains heavy `max-width: 767px` and `max-width: 1024px` branches; expect collapsed or simplified nav rather than full desktop link set.

### Content Width

- **Prose max-width**: `600px-680px` for readable copy.
- **Container max-width**: `1280px-1366px` for product/editorial sections.
- **Sidebar width**: not a homepage signature; this is not an app-dashboard layout.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary pill CTA**

```html
<a class="meta-button meta-button--primary" href="#">Shop Meta Quest</a>
```

| Property | Value |
|---|---|
| Background | `#0064E0` (`{colors.primary}`) |
| Text | `#FFFFFF` |
| Radius | `100px` |
| Min height | `48px` hero reconstruction; compact surfaces use `--button-height-medium` |
| Padding | `14px 32px` hero reconstruction |
| Weight | `700` in hero CTA |
| Hover | slight brightness/opacity shift; avoid transform-heavy bounce |

**Secondary pill CTA**

```html
<a class="meta-button meta-button--secondary" href="#">Shop apps and games</a>
```

| Property | Value |
|---|---|
| Background | `#FFFFFF` / pale neutral |
| Text | `#1C2B33` |
| Radius | `100px` |
| Border | none in hero screenshot |
| Role | secondary action beside the primary blue CTA |

### Badges

Meta homepage does not use badge-heavy SaaS labeling in the visible hero. If a badge is needed, use small rounded text with #F1F4F7 background, #465A69 text, and avoid neon accent chips.

```html
<span class="meta-badge">Meta Quest</span>
```

| Property | Value |
|---|---|
| Background | `#F1F4F7` |
| Text | `#465A69` |
| Radius | `100px` |
| Font | `Optimistic Text`, `12px-14px`, `500/600` |

### Cards & Containers

```html
<article class="meta-editorial-card">
  <img src="product.jpg" alt="">
  <h3>Ray-Ban Meta AI glasses</h3>
  <p>Capture, share and stay in the moment.</p>
</article>
```

| Property | Value |
|---|---|
| Background | `#FFFFFF` or media thumbnail |
| Radius | `24px-32px` |
| Shadow | optional, scoped to floating/media cards |
| Gap | `16px-32px` |
| Hover | understated opacity/shadow transition, not large lift |

### Navigation

```html
<nav class="meta-nav">
  <a class="meta-logo">Meta</a>
  <a>AI glasses</a>
  <a>Meta Quest</a>
  <a>Apps and games</a>
  <span class="meta-nav__spacer"></span>
  <a>Explore Meta</a>
  <a>Support</a>
</nav>
```

| Property | Value |
|---|---|
| Text on hero | `#FFFFFF` |
| Font | `Optimistic Text`, around `14px`, weight `600` |
| Layout | left product links + right utility links/icons |
| Icon treatment | white stroke icons, circular hit areas |
| Background | transparent over media |

### Inputs & Forms

Forms are not a visible homepage signature in the captured hero. Existing token traces show input aliases (`--input-background`, `--input-border-color`, placeholder aliases), but do not invent a form-heavy visual language for this page.

| Property | Value |
|---|---|
| Background | surface/wash token, not measured from homepage form |
| Border | #CBD2D9 or semantic input border when surfaced |
| Focus | likely blue action ring; exact homepage form state not observed |
| Error | not observed; do not synthesize without product flow evidence |

### Hero Section

```html
<section class="meta-hero">
  <video class="meta-hero__media"></video>
  <div class="meta-hero__overlay"></div>
  <h1>Meta Quest brings the magic of virtual reality</h1>
  <p>Get instant access to 100+ games for 3 months...</p>
  <div class="meta-hero__actions">
    <a class="meta-button meta-button--primary">Shop Meta Quest</a>
    <a class="meta-button meta-button--secondary">Shop apps and games</a>
  </div>
</section>
```

| Property | Value |
|---|---|
| Height | `100vh` visual pattern |
| Media | full-bleed video/image |
| Overlay | dark gradient/alpha layer |
| Text | #FFFFFF, centered |
| CTA group | centered horizontal pills on desktop |
| Control | small circular pause button at lower right |

### 13-2. Named Variants

**button-primary-hero** — blue pill used for the main commerce action.

```css
.button-primary-hero {
  background: #0064E0;
  color: #FFFFFF;
  border-radius: 100px;
  min-height: 48px;
  padding: 14px 32px;
  font-weight: 700;
}
```

**button-secondary-hero** — pale pill used beside the primary CTA.

```css
.button-secondary-hero {
  background: #FFFFFF;
  color: #1C2B33;
  border-radius: 100px;
  min-height: 48px;
  padding: 14px 32px;
  font-weight: 700;
}
```

**nav-hero-link** — white navigation link over media.

```css
.nav-hero-link {
  color: #FFFFFF;
  font-family: "Optimistic Text", sans-serif;
  font-size: 14px;
  font-weight: 600;
}
```

**video-control-circle** — small translucent circular hero control.

```css
.video-control-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(28, 43, 51, .72);
  color: #FFFFFF;
}
```

### 13-3. Signature Micro-Specs

```yaml
immersive-video-title-card:
  description: "Hero를 정적 배너가 아니라 VR 쇼룸의 영상 타이틀 카드로 만드는 공법"
  technique: "full-bleed media; color #FFFFFF; overlay gradients including linear-gradient(180deg,#0000 50%,#00000094) and linear-gradient(to top,rgba(0,0,0,.7) 0%,transparent 100%)"
  applied_to: ["{component.dark-video-hero}", "{component.hero-section}"]
  visual_signature: "검은 영상 무대 위에 Optimistic Display 제목과 CTA만 떠 있는 Meta Quest 데모룸 효과"

optimistic-compressed-broadcast-display:
  description: "둥근 Meta 브랜드 폰트를 방송 타이틀처럼 크게 응축하는 display 처리"
  technique: "font-family: Optimistic Display; font-weight: 700; size 4rem-8rem; line-height 1.04-1.15; letter-spacing -.01em to -.06em"
  applied_to: ["{component.dark-video-hero}", "large editorial headings"]
  visual_signature: "부드러운 글꼴인데도 화면 중앙에서 단단한 제목 덩어리로 읽히는 헤드라인"

blue-white-commerce-pills:
  description: "몰입형 hero 안에서 구매 행동만 즉시 읽히게 하는 이중 pill CTA"
  technique: "primary #0064E0/{colors.surface}; secondary #FFFFFF/#1C2B33; border-radius 100px; min-height 48px; padding 14px 32px; no outline secondary in hero"
  applied_to: ["{component.button-primary}", "{component.button-secondary-pill}", "{component.dark-video-hero}"]
  visual_signature: "검은 영상 위에 파란 실행 버튼과 흰 보조 버튼이 헤드셋 컨트롤처럼 나란히 놓임"

cool-editorial-hard-reset:
  description: "cinematic hero 뒤를 차가운 기업 편집면으로 즉시 되돌리는 표면 전환"
  technique: "hero floor #0A1317/{colors.dark}; next sections #FFFFFF/{colors.surface}; text #1C2B33/{colors.ink}; structure #F1F4F7 and #CBD2D9"
  applied_to: ["post-hero editorial sections", "{component.editorial-card}"]
  visual_signature: "VR 극장에서 나온 직후 흰 제품 카탈로그가 펼쳐지는 듯한 abrupt reset"

scoped-media-depth:
  description: "chrome 전체가 아니라 media/card/control에만 깊이를 허용하는 shadow 규칙"
  technique: "observed shadows include 10px 10px 34px #0003, 0 4px 12px #0000004d, and 0 2px 8px #00000014; avoid universal card lift"
  applied_to: ["{component.editorial-card}", "{component.dark-video-hero}", "floating media/control surfaces"]
  visual_signature: "사진과 영상은 공간을 갖지만 UI chrome은 거의 평면으로 남는 Meta식 restrained depth"
```

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Meta — copy into your root stylesheet */
:root {
  /* Fonts */
  --meta-font-display: "Optimistic Display", "Montserrat", Helvetica, Arial, "Noto Sans", sans-serif;
  --meta-font-body: "Optimistic Text", "Montserrat", Helvetica, Arial, "Noto Sans", sans-serif;
  --meta-font-code: Menlo, Consolas, Monaco, monospace;
  --meta-font-weight-normal: 400;
  --meta-font-weight-bold: 700;

  /* Brand/action */
  --meta-color-brand-25:  #ECF5FF;
  --meta-color-brand-300: #4BA9FE;
  --meta-color-brand-500: #0064E0;
  --meta-color-brand-600: #0457CB;
  --meta-color-brand-900: #004BB9;

  /* Surfaces */
  --meta-bg-page:    #FFFFFF;
  --meta-bg-wash:    #F1F4F7;
  --meta-bg-dark:    #0A1317;
  --meta-text:       #1C2B33;
  --meta-text-muted: #465A69;
  --meta-border:     #CBD2D9;

  /* Spacing */
  --meta-space-sm: 12px;
  --meta-space-md: 16px;
  --meta-space-lg: 24px;
  --meta-space-xl: 32px;
  --meta-space-2xl: 48px;
  --meta-space-3xl: 64px;

  /* Radius */
  --meta-radius-sm: 8px;
  --meta-radius-md: 24px;
  --meta-radius-lg: 32px;
  --meta-radius-pill: 100px;
}

.meta-hero {
  min-height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  color: #FFFFFF;
  overflow: hidden;
}

.meta-hero::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(0, 0, 0, .15), rgba(0, 0, 0, .58));
}

.meta-hero__content {
  position: relative;
  z-index: 1;
  max-width: 900px;
  padding-inline: 24px;
  text-align: center;
}

.meta-hero h1 {
  font-family: var(--meta-font-display);
  font-size: clamp(3rem, 7vw, 8rem);
  line-height: 1.05;
  letter-spacing: -0.02em;
  font-weight: 700;
}

.meta-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 48px;
  padding: 14px 32px;
  border-radius: var(--meta-radius-pill);
  font-family: var(--meta-font-body);
  font-weight: 700;
  text-decoration: none;
}

.meta-button--primary {
  background: #0064E0;
  color: #FFFFFF;
}

.meta-button--secondary {
  background: #FFFFFF;
  color: #1C2B33;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `{colors.primary}` | `#0064E0` |
| Quest/action blue | `{colors.quest-blue}` | `#0095F6` |
| Background | `{colors.surface}` | `#FFFFFF` |
| Wash | `{colors.wash}` | `#F1F4F7` |
| Text primary | `{colors.ink}` | `#1C2B33` |
| Text muted | `{colors.secondary-ink}` | `#465A69` |
| Border | `{colors.hairline}` | `#CBD2D9` |
| Dark hero floor | `{colors.dark}` | `#0A1317` |
| Error | critical status | `#F53947` |

### Example Component Prompts

#### Hero Section

```text
Meta 스타일 히어로 섹션을 만들어줘.
- 전체 화면 비디오/이미지 배경 위에 검정 오버레이를 얹는다.
- H1은 Optimistic Display, clamp(3rem, 7vw, 8rem), weight 700, tracking -0.02em, color #FFFFFF.
- 서브텍스트는 Optimistic Text, 16-18px, color #FFFFFF.
- CTA는 두 개의 pill: primary #0064E0/#FFFFFF, secondary #FFFFFF/#1C2B33, radius 100px.
- 상단 nav는 투명 배경, 흰색 텍스트/아이콘, 좌측 제품 링크와 우측 유틸 링크를 나눈다.
```

#### Editorial Card

```text
Meta 스타일 제품/뉴스 카드를 만들어줘.
- 배경 #FFFFFF, 텍스트 #1C2B33, 보조 텍스트 #465A69.
- 이미지 또는 제품 비주얼이 먼저 오고, 카드 radius는 24px-32px.
- shadow는 필요할 때만 0 2px 8px #00000014 또는 10px 10px 34px #0003 수준으로 제한한다.
- gap은 16px-24px, 제목은 Optimistic Display 또는 Text Bold 600/700.
```

#### Badge

```text
Meta 스타일 배지를 만들어줘.
- bg #F1F4F7, color #465A69, radius 100px.
- font는 Optimistic Text 12-14px, weight 500 또는 600.
- 로고 그라디언트나 무지개 컬러는 사용하지 않는다.
```

#### Navigation

```text
Meta 홈페이지 hero nav를 만들어줘.
- 높이 64px-80px, 배경 transparent.
- hero 위에서는 링크와 아이콘을 #FFFFFF로 둔다.
- 폰트는 Optimistic Text 14px, weight 600.
- 좌측: Meta 로고 + AI glasses / Meta Quest / Apps and games.
- 우측: Explore Meta / Support / search / locale / bag / account icon.
```

### Iteration Guide

- **색상 변경 시**: #0064E0을 primary action으로 유지하고, 로고 그라디언트를 UI 배경으로 확장하지 말 것.
- **폰트 변경 시**: Optimistic Display/Text의 둥근 톤을 보존한다. Montserrat 대체 시 display tracking을 더 조인다.
- **여백 조정 시**: hero는 full-bleed, 이후 section은 64px 이상 호흡을 확보한다.
- **컴포넌트 추가 시**: pill CTA, rounded media cards, cool neutral borders를 우선 사용한다.
- **다크 hero**: #FFFFFF text and controls over video overlay. Light-section token을 opacity로 억지 변환하지 말 것.
- **반응형**: 767px, 1024px, 1920px 전후의 breakpoint가 많다. 모바일은 nav와 CTA stack을 단순화한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `Optimistic Display` for hero and large editorial headings.
- Use `Optimistic Text` for body, nav, and CTA labels.
- Keep the primary CTA at #0064E0 with white text.
- Treat video/product imagery as the main atmospheric layer.
- Reset content sections to #FFFFFF with #1C2B33 text after dark hero media.
- Use large pill radii for hero buttons and circular icon controls.
- Keep shadows scoped to media cards, overlays, or floating controls.
- Use cool gray-blue neutrals such as #F1F4F7, #CBD2D9, and #465A69.

### ❌ DON'T

- 배경 전체를 `#0064E0` 또는 `#1877F2`로 칠하지 말 것 — 대신 hero는 영상 오버레이, 본문은 `#FFFFFF` 사용.
- 본문 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#1C2B33` 사용.
- editorial wash를 `#F7F7F5` 같은 warm neutral로 바꾸지 말 것 — 대신 `#F1F4F7` 사용.
- hairline/border를 `#DDDDDD`로 일반화하지 말 것 — 대신 `#CBD2D9` 또는 `#E6EBEF` 사용.
- primary CTA를 `#0095F6`로 고정하지 말 것 — hero/action primary는 `#0064E0`로 우선 재현.
- hero CTA를 square radius `8px`로 만들지 말 것 — pill radius `100px` 사용.
- H1을 generic `font-weight: 400`으로 두지 말 것 — Meta hero display는 `700` 중심.
- 전체 UI에 로고형 conic/linear gradient를 남발하지 말 것 — gradient는 media/overlay/campaign 특수 효과에만 제한.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No rainbow UI system** — Meta 로고와 일부 campaign gradient는 있어도, 홈페이지 UI 팔레트는 무지개 시스템이 아니다.
- **No beige editorial warmth** — surface identity is cool white/blue-gray, not cream, sand, or warm paper.
- **No black body copy** — primary ink is #1C2B33, keeping the page softer than pure black.
- **No outline-first CTA pattern** — the visible hero uses filled blue and filled pale pills.
- **No universal card shadow** — depth is scoped; most structure comes from media, radius, spacing, and cool borders.
- **No dense dashboard chrome** — this is not Meta Business Suite or an admin tool. Sidebar/data-table patterns are absent from the homepage.
- **No heavy decorative SVG illustration** — actual product imagery/video carries the visual signal.
- **No generic Inter SaaS voice** — Optimistic typography is part of the brand expression.
- **No second dominant brand color** — blue action plus neutrals; accents remain contextual/status-level.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage snapshot** — This guide uses the saved `https://meta.com` homepage capture and phase1 artifacts. Product subflows, checkout, help pages, account pages, and regional campaign variants were not visited.
- **Hero is time-sensitive media** — The visible screenshot shows a Meta Quest VR promotion. Meta frequently rotates hero campaigns, so the structural pattern is stable but exact copy/media may change.
- **CSS includes multiple Meta/Facebook surfaces** — The CSS bundle contains legacy Facebook classes, Instagram/Threads-style aliases, chat variables, and status colors. Brand decisions intentionally prioritize the visible homepage and semantic action tokens over raw frequency alone.
- **No live interaction capture** — Hover, pressed, menu-open, locale switcher, cart/account states, and video pause behavior were inferred from CSS tokens and screenshot, not exercised in browser.
- **Form states not surfaced** — Input aliases exist in CSS, but the homepage screenshot does not expose validation, error, loading, or focus states.
- **Typography scale is reconstructed** — The extractor found font families and weights but no clean semantic scale object. Sizes are derived from CSS frequency and responsive class samples.
- **Dark mode mapping incomplete** — Dark tokens and overlays exist, but this is not evidence of a full site-wide dark theme.
- **Exact video overlay opacity may vary** — CSS contains several gradient overlays; the captured hero likely combines media luminance with overlay rather than one global value.
- **Generated token names are not designer-friendly** — `--x*` variables are real, but not suitable as public API names. This guide uses human aliases only as cross-references to observed values.
