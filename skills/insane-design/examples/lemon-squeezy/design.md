---
schema_version: 3.2
slug: lemon-squeezy
service_name: Lemon Squeezy
site_url: https://www.lemonsqueezy.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: mixed
brand_color: "#5423E7"
primary_font: Circularpro book
font_weight_normal: 400
token_prefix: ls

bold_direction: Candy SaaS
aesthetic_category: Refined SaaS
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Webflow production CSS exposes a broad token ramp, component classes, responsive rules, and interaction classes, but not a formal public designer guide."

colors:
  primary: "#5423E7"
  accent-yellow: "#FFC233"
  accent-yellow-lighter: "#FFD266"
  surface-light: "#FFFFFF"
  surface-soft: "#F7F7F8"
  text-primary: "#121217"
  text-muted: "#6C6C89"
  border: "#D1D1DB"
  purple-soft: "#F4F1FD"
  purple-strong: "#2B0E81"
  success: "#2DCA72"
  danger: "#F53D6B"
typography:
  display: "Circularpro book"
  body: "Inter"
  code: "Jetbrainsmono"
  ladder:
    - { token: h1, size: "5rem", weight: 400, line_height: "1", tracking: "-0.04em" }
    - { token: h2, size: "3.5rem", weight: 400, line_height: "1.14", tracking: "-0.03em" }
    - { token: body, size: "1.125rem", weight: 400, line_height: "1.6", tracking: "0" }
    - { token: nav, size: "0.9375rem", weight: 400, line_height: "normal", tracking: "0" }
  weights_used: [300, 400, 500, 600, 700, 800]
  weights_absent: [200, 900]
components:
  button-primary: { bg: "{colors.surface-light}", fg: "{colors.text-primary}", radius: "2.5rem", padding: "overlay-driven", motion: "overlay translate(-0.5rem,-0.5rem)" }
  nav-button: { bg: "{colors.surface-light}", fg: "{colors.text-primary}", radius: "999px", height: "40px approx", motion: "arrow translateX(0.5rem)" }
  announcement-banner: { bg: "{colors.accent-yellow}", fg: "{colors.text-primary}", height: "70px" }
  mega-menu-link: { hover_text: "{colors.text-muted}", structure: "header + subcopy + arrow icon" }
---

# DESIGN.md — Lemon Squeezy

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Lemon Squeezy presents financial infrastructure as candy-colored relief. The product category is heavy: merchant of record, tax compliance, failed payments, subscriptions. The visual system refuses that heaviness by turning the first viewport into a bright purple checkout counter: `#5423E7` (`{colors.primary}`) becomes the shop wall, `#FFC233` (`{colors.accent-yellow}`) becomes the lemon shelf label, and the white CTA pill becomes the clean receipt sitting on top. Serious mechanics stay backstage; the wrapper says "easy peasy" before the user has to think about tax.

The hero is the signature squeeze. A large, loose, white Circularpro headline sits on `{colors.primary}`, while a tilted product dashboard enters from the right with a hard diagonal crop. The composition is not a centered SaaS template. It is a candy wrapper pulled open from one corner: copy on the left, proof on the right, and the diagonal product image acting like the tear line in the package. The page does not explain payment infrastructure as a spreadsheet; it shows the dashboard sliding into the purple field as if the operational burden has been folded into a neat product insert.

The brand depends on a strict two-color memory: purple for platform identity and yellow for lemon warmth. There are many ramps in CSS, but the homepage experience is anchored by `{colors.primary}` and `{colors.accent-yellow}`. No second brand color. No equal rainbow palette. The yellow is not another environment; it is citrus punctuation: a 70px announcement strip, a hover underline, a button underlay. Lemon Squeezy is purple infrastructure with yellow zest, not multicolor confetti.

Typography makes the friendliness feel engineered rather than childish. `Circularpro book` at weight 400 gives the headline a round, soft-bottle shape, then `letter-spacing: -0.04em` tightens it like a label wrapped snugly around packaging. Body copy switches to Inter at `1.125rem` and line-height `1.6`, so tax and subscription language reads like product help instead of legal copy. The ink is `#121217` (`{colors.text-primary}`), not generic black; it lands with enough weight for trust without making the candy shell feel harsh.

Micro-interaction carries much of the craft. Primary buttons are not simple pills. The visible white overlay moves `translate(-0.5rem, -0.5rem)` on hover, exposing the yellow underlay like a soft candy button being pressed from below. Arrow icons slide right. Dropdowns get only a `#FFC233` inset underline, not a full color takeover. The site has no glass chrome, no heavy shadow stack, and no dramatic dark-mode theater; its tactility comes from small layered shifts on top of flat, saturated fields.

### Key Characteristics

- Purple full-bleed hero field: `#5423E7` owns the first viewport and nav.
- Yellow announcement bar: `#FFC233` is used as citrus punctuation, not as a second full UI theme.
- Large rounded display typography: `Circularpro book`, weight 400, tight tracking.
- Split hero anatomy: left copy block, right tilted product dashboard image.
- White pill CTAs: high contrast against purple, with dark text instead of white-on-brand buttons.
- Overlay button craft: primary CTA hover shifts the overlay by `-0.5rem`.
- Sticky Webflow nav: purple chrome with white logo, muted links, and white "Get started" pill.
- Friendly fintech copy: tax and payments are explained in low-friction, conversational language.
- Soft neutral support: `#F7F7F8`, `#D1D1DB`, and `#6C6C89` handle structure below the hero.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Candy SaaS
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **purple hero stage with lemon-yellow tactile CTA accents**으로 기억된다.
> **Code Complexity**: high — Webflow layout, token ramps, sticky nav, dropdowns, staged reveal transforms, image-heavy hero, and overlay button motion all need to work together.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Lemon Squeezy처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}
h1, h2, h3 {
  font-family: "Circularpro book", "Inter", sans-serif;
  font-feature-settings: "ss04";
  font-weight: 400;
  letter-spacing: -0.04em;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #5423E7; --fg: #FFFFFF; --ink: #121217; }
body { color: var(--ink); }
.hero { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #5423E7; --lemon: #FFC233; }
```

**절대 하지 말아야 할 것 하나**: CTA를 보라 배경 위에 `#5423E7` 버튼으로 또 칠하지 말 것. Hero CTA는 white pill + dark text + hover overlay motion이 핵심이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.lemonsqueezy.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | existing phase1 reuse: HTML + CSS + screenshot |
| HTML size | 148033 bytes (Webflow published page) |
| CSS files | 2 files, approx 309494 chars |
| Token prefix | `ls` / unprefixed Webflow custom properties |
| Method | Existing `phase1/*.json`, CSS token inspection, HTML structure, and hero screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Webflow production site (`data-wf-site`, `data-wf-page`, `w-nav`, `w-dropdown`, `w-tabs`)
- **Design system**: Webflow class system with Lemon Squeezy custom properties. The strongest brand prefix is `--ls-*`, but many ramps are unprefixed (`--purple-600`, `--grey-50`, `--border-color`).
- **CSS architecture**:
  ```text
  core       (--purple-600, --yellow-500, --grey-50)       raw values
  brand      (--ls-purple, --ls-color-yellow)              brand anchors
  component  (.button-primary, .nav_component, .banner)    component assembly
  utility    (.padding-global, .margin-bottom, .text-*)    Webflow utility layer
  ```
- **Class naming**: Webflow-style semantic classes with modifiers: `.button-primary`, `.button-secondary.is-rounded`, `.nav_component`, `.home-header_component`, `.banner.is-annoucement`.
- **Default theme**: mixed. Homepage opens as a purple/dark chromatic hero, then uses white and soft neutral content bands.
- **Font loading**: CSS `@font-face` plus Webflow-hosted assets; extracted families include `Circularpro book`, `Inter`, and `Jetbrainsmono`.
- **Canonical anchor**: `https://www.lemonsqueezy.com`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Circularpro book` (brand/display; likely licensed or hosted through Webflow asset pipeline)
- **Body font**: `Inter` (open-source fallback-friendly)
- **Code font**: `Jetbrainsmono`
- **Weight normal / bold**: `400` / `700`; important interactive text often uses `500`

```css
:root {
  --ls-font-display: "Circularpro book", "Inter", sans-serif;
  --ls-font-body:    "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --ls-font-code:    "Jetbrainsmono", ui-monospace, SFMono-Regular, monospace;
  --ls-font-weight-normal: 400;
  --ls-font-weight-medium: 500;
  --ls-font-weight-bold:   700;
}
body {
  font-family: var(--ls-font-body);
  font-weight: var(--ls-font-weight-normal);
}
h1, h2, h3 {
  font-family: var(--ls-font-display);
  font-feature-settings: "ss04";
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Circularpro book** — if the hosted brand font is unavailable, use **Inter Display** or **Manrope** at weight 400. Preserve the Lemon Squeezy feel by keeping display tracking tight: `h1 { letter-spacing: -0.04em; line-height: 1; }`.
- **Inter body** — keep Inter at weight 400 for body and 500 for nav/CTA. Do not substitute with Arial for final UI; Arial appears only as a reset/default fallback in the CSS.
- **Jetbrainsmono** — use `JetBrains Mono` for code-like UI or technical snippets. The homepage itself is not code-heavy, so do not overuse monospace as a decorative brand cue.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `h1` | `5rem` | `400` | `1` | `-0.04em` |
| `h2` | `3.5rem` | `400` | `1.14` | `-0.03em` |
| `.heading-style-h1` | `5rem` desktop; `3rem` tablet; `2.5rem` mobile | `400` | `1` | inherited/tight |
| `body` | `1.125rem` | `400` | `1.6` | `0` |
| `.text-size-medium` | `1.25rem` desktop; `1rem` smaller breakpoint | inherited | inherited | `0` |
| `.nav_component` | `0.9375rem` | `400` | normal | `0` |
| `.button-primary` | inherited | `500` | `1.4` | `-0.01em` |

> ⚠️ The display face is intentionally round and loose in form, then optically tightened with negative tracking. Without the tracking, the hero loses its confident compactness.

### Principles
<!-- SOURCE: manual -->

1. Display weight stays light: `400` is the hero voice, not `700`.
2. Display tracking is aggressive: `h1` uses `-0.04em`; this is a brand-critical correction.
3. Body is calmer than the hero: Inter `1.125rem / 1.6` gives tax/payment copy room to breathe.
4. Interactive text uses `500`: nav pills, buttons, announcement copy, and small labels need more firmness than body text.
5. `font-feature-settings: "ss04"` is part of the display texture. Keep it on `h1`, `h2`, and `h3` when the chosen font supports it.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp

| Token | Hex |
|---|---|
| `--purple-50-501` | `#F4F1FD` |
| `--purple-100` | `#E2DAFB` |
| `--purple-200` / `--purple-200-201` | `#C6B6F7` |
| `--purple-300` | `#A991F3` |
| `--purple-400` | `#8D6CEF` |
| `--purple-500` / `--blue-violet` | `#7047EB` |
| `--purple-600` / `--ls-purple` / `--blue` | `#5423E7` |
| `--purple-700` | `#4316CA` |
| `--purple-900` | `#2B0E81` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--black-2` | `#121217` |
| `--dark-mode-bg-lighter` | `#141414` |
| `--dark-grey` / `--light-black` | `#191919` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white | `#FFFFFF` / `white` | N/A |
| soft surface | `#F7F7F8` | N/A |
| line | `#E8E8ED` | `#3F3F50` |
| border | `#D1D1DB` | N/A |
| muted text | `#A9A9BC` / `#6C6C89` | `#6C6C89` |
| ink | `#121217` | `#121217` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Lemon yellow | `--yellow-500` / `--ls-color-yellow` | `#FFC233` |
| Lemon yellow lighter | `--ls-color-yellow-lighter` | `#FFD266` |
| Blue | `--blue-500` | `#00ACFF` |
| Green | `--green-500` | `#2DCA72` |
| Orange | `--orange-500` | `#FF7D52` |
| Pink | `--pink-500` | `#F75FDE` |
| Red | `--red-500` | `#F53D6B` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--ls-purple` | `#5423E7` | Hero background, nav background, brand anchor |
| `--ls-color-yellow` | `#FFC233` | Announcement banner, hover underline, golden CTA state |
| `--button-primary-light` | `#FFFFFFE6` | White translucent primary CTA surface |
| `--black-2` | `#121217` | Primary text on light or white pills |
| `--gray-500` / `--bullet-point-color` | `#6C6C89` | Muted copy, dropdown hover copy, bullet tone |
| `--border-color` | `#D1D1DB` | Hairlines and soft card dividers |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--ls-purple` | `#5423E7` | canonical brand purple |
| `--purple-600` | `#5423E7` | same anchor as brand purple |
| `--button-primary-light` | `#FFFFFFE6` | hero CTA visible overlay |
| `--ls-color-yellow` | `#FFC233` | announcement and hover accent |
| `--ls-color-yellow-lighter` | `#FFD266` | CTA underlay hover/backplate |
| `--border-color` | `#D1D1DB` | content borders |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---|---|
| white | `#FFFFFF` | 63 |
| transparent black | `#00000000` | 39 |
| black | `#000000` | 16 |
| `--black-2` | `#121217` | 14 |
| `--ls-purple` | `#5423E7` | 12 |
| white 20% | `#FFFFFF33` | 12 |
| white 60% | `#FFFFFF99` | 11 |
| `--grey-50` | `#F7F7F8` | 10 |
| soft gray | `#F4F4F4` | 9 |
| Webflow default blue | `#3898EC` | 7 |
| muted violet-gray | `#6C6C89` | 7 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.primary}` (`#5423E7`)** — The stage color. It carries the hero, sticky nav, and brand memory. Use it as a full field or structural block, not as tiny random decoration.

**`{colors.accent-yellow}` (`#FFC233`)** — The lemon cue. It appears in the announcement bar and hover details. It should feel like a flash of product personality, not a full alternate theme.

**`{colors.surface-light}` (`#FFFFFF`)** — The CTA and dashboard relief color. Against purple it creates the clean, payment-product contrast that makes the page trustworthy.

**`{colors.text-primary}` (`#121217`)** — The ink. It keeps white pills, body sections, and product content crisp without dropping into harsh pure black as the main authored token.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token / Class | Value | Use case |
|---|---|---|
| `.nav_component` horizontal padding | `2.5rem`, then `1.25rem` on smaller breakpoints | sticky nav chrome |
| `.home-header_component` gap | `5rem`, then `3rem`, `2rem` | hero split layout |
| `.home-header_component` top/bottom | `6.5rem 4rem`, then `5rem 5rem`, mobile `5rem 0 0` | hero breathing room |
| `.padding-global` | `2.5rem`, `2rem`, `1.25rem` | page gutters |
| `.container-large` | max-width `80rem` | wide content container |
| `.nav_container` | max-width `72rem` | nav content width |
| `.button-secondary` | `1rem 3rem` | large secondary pill/rect button |
| `.button-secondary.is-small` | `.75rem 1.5rem` | compact CTA |

**주요 alias**:
- `--ls-space-hero-gap` → `5rem` (hero grid column/row gap)
- `--ls-space-page-gutter` → `2.5rem` desktop, `1.25rem` smaller screens
- `--ls-space-section-soft` → `4rem` to `6.5rem` hero vertical air

### Whitespace Philosophy
<!-- SOURCE: manual -->

Lemon Squeezy uses generous hero space but not minimalist emptiness. The page opens with enough purple field for the headline to feel big, then immediately fills the right side with a large product image. This is not a quiet luxury layout; it is a friendly SaaS layout with enough air to make complex payment infrastructure feel simple.

The spacing system is strongest at the container level: `72rem` nav, `80rem` content, `2.5rem` page gutters, and `5rem` hero gaps. Inside components, spacing becomes tactile and compact. The contrast is intentional: broad brand stage outside, pill-sized interaction details inside.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token / Selector | Value | Context |
|---|---|---|
| `.button-primary` | `2.5rem` | hero CTA pill |
| `.button-secondary.is-rounded` | `2rem` | rounded secondary CTA |
| `.banner-button` | `20px` | announcement "Read more" capsule |
| `.blog_content img`, `img.changelog_full-image` | `8px` | content imagery |
| `.margin-bottom.margin-medium.rounded-image` | `12px` | bordered content image/card |
| `.nav_menu::-webkit-scrollbar-thumb` | `100px` | scroll thumb capsule |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| slider/nav default | `0 0 3px #33333366` | Webflow slider dot shadow |
| rounded image/card | `4px 0 6px #11112e0d, 0 10px 15px #11112e14` | soft card/media elevation |
| hero product visual | image-rendered shadow/crop rather than CSS token | product dashboard mockup depth |

Shadow is not the main interface language. The page relies on saturated fields, white surfaces, and product imagery. Use shadow sparingly and keep it soft, never heavy neumorphism.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Selector | Value | Usage |
|---|---|---|
| `.button-primary:hover .button-primary-overlay` | `transform: translate(-0.5rem, -0.5rem)` | tactile raised CTA |
| `.button-primary-small:hover .button-primary-overlay-small` | `translate(-0.35rem, -0.35rem)` | compact CTA lift |
| `.button-primary:hover .button-primary-icon` | `translate(0.5rem, 0)` | arrow slide |
| `.button-secondary-icon` | `.28s cubic-bezier(.215,.61,.355,1)` | icon row movement |
| Webflow reveal inline styles | `translate3d(..., 2rem/4rem, 0); opacity:0` | staged entrance animations |
| `.banner.offer-banner` | `transition: all .2s` | announcement interaction |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `80rem` for `.container-large`, `72rem` for `.nav_container`.
- **Grid type**: CSS Grid for hero and nav, Flexbox for buttons and many component internals.
- **Column count**: hero begins as `1fr 1fr`, shifts to `1.25fr 1fr`, then `.75fr .35fr`, then single-column/mobile block.
- **Gutter**: `5rem` desktop hero, reducing to `3rem` and `2rem`.

### Hero

- **Pattern Summary**: `large purple field + two-column split + left oversized H1 + right tilted product dashboard + white pill CTA`.
- Layout: `.home-header_component` grid with copy left and product image right.
- Background: solid `#5423E7` brand purple.
- **Background Treatment**: solid chromatic field. The visual depth comes from the diagonal product image, not from gradient mesh.
- H1: `5rem` / weight `400` / tracking `-0.04em`.
- Max-width: content appears inside a wide centered page container with strong side gutters.

### Section Rhythm

```css
.home-header_component {
  grid-template-columns: 1fr 1fr;
  gap: 5rem;
  padding-top: 6.5rem;
  padding-bottom: 4rem;
}
.padding-global {
  padding-left: 2.5rem;
  padding-right: 2.5rem;
}
```

### Card Patterns

- **Card background**: mostly white or `#F7F7F8`.
- **Card border**: `1px solid #D1D1DB` for structured content, not on the hero CTA.
- **Card radius**: `8px` to `12px` for media/card surfaces; CTA uses large pill radius.
- **Card padding**: utility-driven, commonly rem-based.
- **Card shadow**: soft dual shadow only where media/card depth is needed.

### Navigation Structure

- **Type**: horizontal desktop nav with dropdown mega menus; mobile uses Webflow `w-nav-button`.
- **Position**: sticky at top.
- **Height**: announcement `70px`; nav uses vertical padding `1.5rem`, smaller breakpoint `.8rem`.
- **Background**: `#5423E7`.
- **Border**: no visible nav border; color field defines the chrome.

### Content Width

- **Prose max-width**: content-specific; hero copy is constrained by grid column rather than prose class.
- **Container max-width**: `80rem`.
- **Sidebar width**: N/A on homepage hero; product dashboard imagery acts as the right-side visual column.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Large fluid | `max-width: 1280px` | root font-size begins fluid scaling |
| Tablet | `max-width: 991px` | nav and hero spacing compress; Webflow nav behavior changes |
| Small tablet | `max-width: 768px` | root font-size becomes viewport-based |
| Mobile | `max-width: 480px` | compact type and single-column hero |
| Narrow mobile | `max-width: 390px` | final root type correction |

### Touch Targets

- **Minimum tap size**: CTA pills visually satisfy 44px+ through padding and pill height.
- **Button height (mobile)**: not directly tokenized; `.nav_button` and `.button-primary` retain large capsule ergonomics.
- **Input height (mobile)**: homepage form states not observed.

### Collapsing Strategy

- **Navigation**: desktop links + dropdowns collapse into Webflow mobile menu button.
- **Grid columns**: hero grid collapses from two columns to single-column/block.
- **Sidebar**: no homepage sidebar.
- **Hero layout**: image moves under/after copy; padding changes to `5rem 0 0`.

### Image Behavior

- **Strategy**: responsive Webflow `srcset` images.
- **Max-width**: images use Webflow responsive sizing and grid containment.
- **Aspect ratio handling**: hero product image is composition/crop driven; product dashboard is intentionally oversized and diagonal.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary hero CTA**

```html
<a class="button-primary w-inline-block">
  <div class="button-primary-overlay">
    <div class="button-primary-text">Get started for free</div>
    <div class="button-primary-icon">...</div>
  </div>
</a>
```

| Property | Value |
|---|---|
| background | `#FFFFFFE6` via `--button-primary-light` |
| text | `#121217` |
| radius | `2.5rem` |
| weight | `500` |
| line-height | `1.4` |
| tracking | `-0.01em` |
| hover | overlay moves `translate(-0.5rem, -0.5rem)` |
| icon hover | arrow moves `translate(0.5rem, 0)` |

**Nav CTA**

- White pill on purple nav.
- Text: `Get started`.
- Includes arrow icon with hover translation.
- Must remain visually lighter than the main hero CTA.

### Badges

- `navbar_link-tag.is-new` appears in dropdown items for "new" feature labelling.
- Badge tone should stay small and informational. Use yellow or purple only when the source component already does so.

### Cards & Containers

- Product/feature sections use white and soft neutral surfaces.
- Borders use `#D1D1DB`.
- Rounded image/card surfaces use `8px` to `12px`.
- Soft dual shadows can be used for media cards, not for every content block.

### Navigation

- `.nav_component` is sticky and purple.
- `.nav_container` is grid-based with max-width `72rem`.
- Dropdown links have header, subcopy, and arrow icon.
- Hovering a dropdown toggle adds `box-shadow: inset 0 -2px 0 0 #FFC233`.
- Dropdown subcopy hover can shift to `#6C6C89`.

### Inputs & Forms

Homepage form fields were not surfaced in the first viewport. If implementing form components, inherit Webflow defaults only as a low-confidence base:

- text: `#121217`
- border: `#D1D1DB`
- focus accent: `#5423E7`
- error: `#F53D6B`
- success: `#2DCA72`

### Hero Section

- Purple full-bleed stage.
- Left display headline, 4-line wrap at desktop.
- Muted white subcopy using alpha/soft color, not pure gray on purple.
- White pill CTA with black text.
- Right tilted product dashboard image, clipped by viewport edge.

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-primary-raised-overlay**

| Property | Value |
|---|---|
| base | `#FFD266` underlay when golden wrapper is active |
| overlay | `#FFFFFFE6` / white pill |
| hover | overlay translate `-0.5rem, -0.5rem` |
| signature | tactile "pressed candy" motion |

**button-secondary-rounded**

| Property | Value |
|---|---|
| background | `#FFFFFF` |
| text | `#121217` |
| radius | `2rem` |
| padding | `1rem 3rem` |

**announcement-banner**

| Property | Value |
|---|---|
| background | `#FFC233` |
| height | `70px` |
| text | `14px`, weight `500` |
| optional button | white capsule, `20px` radius |

**nav-mega-link**

| Property | Value |
|---|---|
| structure | title + paragraph + arrow |
| hover copy | `#6C6C89` |
| category label | yellow/golden text |

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
overlay-shift-pill:
  description: "Primary CTA craft that makes the button feel physically layered instead of flat."
  technique: ".button-primary:hover .button-primary-overlay { transform: translate(-0.5rem, -0.5rem); } with #FFFFFFE6 overlay on #FFD266 underlay and 2.5rem radius."
  applied_to: ["{component.button-primary}", "{component.nav-button}"]
  visual_signature: "A white pill appears to lift off a lemon underlayer like a soft candy button."

compact-overlay-shift-pill:
  description: "Small CTA variant that keeps the same raised-overlay behavior at nav scale."
  technique: ".button-primary-small:hover .button-primary-overlay-small { transform: translate(-0.35rem, -0.35rem); } plus arrow translateX motion."
  applied_to: ["{component.nav-button}", "{component.button-primary}"]
  visual_signature: "The compact CTA gives the same tactile squeeze without overpowering the purple nav."

lemon-inset-dropdown-underline:
  description: "Navigation hover cue that adds citrus warmth without recoloring the full nav item."
  technique: ".w-dropdown:hover .w-dropdown-toggle { box-shadow: inset 0 -2px 0 0 #FFC233; } on #5423E7 nav chrome."
  applied_to: ["{component.mega-menu-link}"]
  visual_signature: "A thin yellow squeeze appears under muted purple navigation instead of a full hover block."

circular-tight-display:
  description: "Round display type made more premium through optical compression."
  technique: "Circularpro book, font-weight 400, font-feature-settings 'ss04', h1 5rem/1 with letter-spacing -0.04em; h2 3.5rem/1.14 with letter-spacing -0.03em."
  applied_to: ["{component.hero}", "{typography.ladder.h1}", "{typography.ladder.h2}"]
  visual_signature: "Friendly letterforms are tightened into a confident SaaS label rather than loose playful copy."

lemon-announcement-ribbon:
  description: "A single warm brand band that punctures the purple system before the hero."
  technique: ".banner.is-annoucement / announcement-banner uses #FFC233 background, 70px height, 14px 500 text, optional white 20px-radius capsule."
  applied_to: ["{component.announcement-banner}"]
  visual_signature: "A lemon-yellow shelf label sits above the purple product stage without becoming a second theme."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Functional category first, friendly specificity second | "Payments, tax & subscriptions for software companies" |
| Primary CTA | Direct, low-friction, free-start language | "Get started for free" |
| Secondary CTA | Short and plain | "Read more" |
| Subheading | Merchant-of-record benefit in everyday language | "we handle the tax compliance burden" |
| Tone | Serious backend jobs translated into easy, citrus-branded language | "easy peasy" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Lemon Squeezy — copy into your root stylesheet */
:root {
  /* Fonts */
  --ls-font-display: "Circularpro book", "Inter", sans-serif;
  --ls-font-body: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --ls-font-code: "Jetbrainsmono", ui-monospace, SFMono-Regular, monospace;
  --ls-font-weight-normal: 400;
  --ls-font-weight-medium: 500;
  --ls-font-weight-bold: 700;

  /* Brand */
  --ls-color-brand-25: #F4F1FD;
  --ls-color-brand-300: #A991F3;
  --ls-color-brand-500: #7047EB;
  --ls-color-brand-600: #5423E7;
  --ls-color-brand-900: #2B0E81;

  /* Lemon accent */
  --ls-color-lemon: #FFC233;
  --ls-color-lemon-light: #FFD266;

  /* Surfaces */
  --ls-bg-page: #FFFFFF;
  --ls-bg-soft: #F7F7F8;
  --ls-bg-hero: #5423E7;
  --ls-text: #121217;
  --ls-text-muted: #6C6C89;
  --ls-border: #D1D1DB;

  /* Key spacing */
  --ls-space-sm: 0.75rem;
  --ls-space-md: 1.25rem;
  --ls-space-lg: 2.5rem;
  --ls-space-hero-gap: 5rem;

  /* Radius */
  --ls-radius-image: 8px;
  --ls-radius-card: 12px;
  --ls-radius-pill: 2.5rem;
}

body {
  margin: 0;
  color: var(--ls-text);
  font-family: var(--ls-font-body);
  font-size: 1.125rem;
  font-weight: 400;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h1, h2, h3 {
  font-family: var(--ls-font-display);
  font-feature-settings: "ss04";
  font-weight: 400;
}

.ls-hero {
  background: var(--ls-bg-hero);
  color: #FFFFFF;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--ls-space-hero-gap);
  align-items: center;
  padding: 6.5rem 2.5rem 4rem;
}

.ls-hero h1 {
  max-width: 9ch;
  font-size: 5rem;
  line-height: 1;
  letter-spacing: -0.04em;
}

.ls-button-primary {
  position: relative;
  display: inline-flex;
  align-items: center;
  border-radius: var(--ls-radius-pill);
  background: var(--ls-color-lemon-light);
  color: var(--ls-text);
  text-decoration: none;
}

.ls-button-primary > span {
  display: inline-flex;
  gap: 0.75rem;
  align-items: center;
  border-radius: var(--ls-radius-pill);
  background: #FFFFFFE6;
  padding: 1rem 3rem;
  font-weight: 500;
  line-height: 1.4;
  letter-spacing: -0.01em;
  transition: transform 0.18s cubic-bezier(.215,.61,.355,1);
}

.ls-button-primary:hover > span {
  transform: translate(-0.5rem, -0.5rem);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Lemon Squeezy approximation
module.exports = {
  theme: {
    extend: {
      colors: {
        ls: {
          purple: '#5423E7',
          lemon: '#FFC233',
          lemonLight: '#FFD266',
          ink: '#121217',
          muted: '#6C6C89',
          border: '#D1D1DB',
          soft: '#F7F7F8',
        },
      },
      fontFamily: {
        display: ['Circularpro book', 'Inter', 'sans-serif'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['Jetbrainsmono', 'ui-monospace', 'monospace'],
      },
      letterSpacing: {
        lsDisplay: '-0.04em',
        lsHeading: '-0.03em',
        lsButton: '-0.01em',
      },
      borderRadius: {
        lsImage: '8px',
        lsCard: '12px',
        lsPill: '2.5rem',
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
| Brand primary | `{colors.primary}` | `#5423E7` |
| Lemon accent | `{colors.accent-yellow}` | `#FFC233` |
| Background | `{colors.surface-light}` | `#FFFFFF` |
| Text primary | `{colors.text-primary}` | `#121217` |
| Text muted | `{colors.text-muted}` | `#6C6C89` |
| Border | `{colors.border}` | `#D1D1DB` |
| Success | `{colors.success}` | `#2DCA72` |
| Error | `{colors.danger}` | `#F53D6B` |

### Example Component Prompts

#### Hero Section

```text
Lemon Squeezy 스타일 히어로 섹션을 만들어줘.
- 배경: #5423E7 full-bleed purple field
- H1: Circularpro book, 5rem, weight 400, line-height 1, tracking -0.04em
- 서브텍스트: white with muted alpha 느낌, 1.125rem, line-height 1.6
- CTA 버튼: white translucent pill, text #121217, radius 2.5rem, overlay hover translate(-0.5rem,-0.5rem)
- 우측 비주얼: tilted SaaS dashboard image/mockup, oversized and cropped by viewport edge
- 노란색은 #FFC233 announcement/hover accent로만 사용
```

#### Card Component

```text
Lemon Squeezy 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF 또는 #F7F7F8
- border: 1px solid #D1D1DB
- radius: 8px image, 12px card
- shadow: 4px 0 6px #11112e0d, 0 10px 15px #11112e14 only when elevation is necessary
- 제목: Circularpro book or Inter, weight 400/500, tight but readable
- 본문: Inter, #121217, 1.125rem/1.6
```

#### Badge

```text
Lemon Squeezy 스타일 배지를 만들어줘.
- font: Inter, 12-14px, weight 500
- padding: compact capsule
- brand state: #FFC233 background with #121217 text
- neutral state: #F7F7F8 background with #6C6C89 text
- radius: 999px
```

#### Navigation

```text
Lemon Squeezy 스타일 상단 네비게이션을 만들어줘.
- sticky top nav, background #5423E7
- max-width 72rem, horizontal padding 2.5rem
- logo left, links center, sign-in and white get-started pill right
- dropdown hover underline: inset 0 -2px 0 0 #FFC233
- link text: Inter 0.9375rem, muted white; CTA text #121217
```

### Iteration Guide

- **색상 변경 시**: `#5423E7` and `#FFC233` must remain the memory pair. Add neutrals before adding new chromatic colors.
- **폰트 변경 시**: preserve display `400` and negative tracking. A bold hero breaks the brand.
- **여백 조정 시**: keep the hero wide and open, but keep CTA internals compact.
- **새 컴포넌트 추가 시**: choose between pill/tactile CTA and soft bordered neutral surface. Do not invent glass cards.
- **다크 모드**: not fully mapped. Use `#121217` / `#141414` only where verified.
- **반응형**: respect Webflow breakpoints: `1280`, `991`, `768`, `480`, `390`.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#5423E7` as a field color for hero/nav, not merely as a small accent.
- Use `#FFC233` for announcement and hover punctuation.
- Keep hero H1 weight `400`, line-height `1`, and tracking near `-0.04em`.
- Use white or `#FFFFFFE6` pill CTAs on purple with `#121217` text.
- Preserve the overlay-shift hover on primary CTAs.
- Use `#D1D1DB` for borders and `#6C6C89` for muted copy.
- Let product dashboard imagery provide depth in the hero.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 시작하지 말 것 — hero/nav의 첫 인상은 `#5423E7` 사용.
- 브랜드 보라를 `#7047EB`로 고정하지 말 것 — canonical hero/nav anchor는 `#5423E7` 사용.
- 노란 포인트를 `#FFD266`만으로 쓰지 말 것 — primary lemon accent는 `#FFC233`, lighter underlay는 `#FFD266` 사용.
- 텍스트를 `#000000` 또는 `black`으로만 두지 말 것 — authored ink는 `#121217`, muted copy는 `#6C6C89` 사용.
- border를 `#CCCCCC`로 두지 말 것 — Lemon Squeezy hairline은 `#D1D1DB` 사용.
- CTA 배경을 `#5423E7`로 두지 말 것 — purple field 위 CTA는 `#FFFFFFE6` 또는 `#FFFFFF` pill 사용.
- hero H1에 `font-weight: 700` 사용 금지 — `Circularpro book` weight `400`이 맞다.
- hero H1에 `letter-spacing: 0` 사용 금지 — `-0.04em` 보정이 필요하다.
- generic `border-radius: 4px` CTA 사용 금지 — CTA는 `2.5rem` pill 계열이다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- **No blue SaaS primary** — Webflow default `#3898EC` appears in reset/default `.w-button`, but the brand system is not blue-button SaaS.
- **No black hero** — the dramatic surface is purple `#5423E7`, not dark-mode black.
- **No gradient mesh hero** — the first viewport is a solid chromatic field with product imagery, not a purple-blue AI gradient.
- **No heavy display bold** — 700+ is not the hero voice; the brand relies on round 400 display type.
- **No sharp CTA rectangle** — primary actions are pill/capsule forms.
- **No equal rainbow palette** — pink, orange, green, blue ramps exist, but they do not share brand priority with purple and yellow.
- **No chrome shadow system** — shadows are secondary; color fields and imagery define hierarchy.
- **No dense dashboard UI as page chrome** — the dashboard is proof imagery, not the whole layout language.
- **No second full brand color** — yellow punctuates; it does not replace purple as a page field.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage snapshot** — this analysis reuses existing `lemon-squeezy` phase1 data and the hero screenshot. Checkout, login, pricing subflows, and app dashboard screens were not visited as live interactive flows.
- **Webflow CSS is minified** — selectors and values are available, but some component intent is inferred from class names and rendered hero structure rather than a formal design-token source.
- **Font licensing not verified** — `Circularpro book` is extracted from CSS usage, but the exact license and hosting package are not confirmed here.
- **Motion runtime not fully replayed** — inline Webflow reveal transforms and CSS hover rules were inspected, but Webflow interaction timelines were not exhaustively executed.
- **Form states are low-confidence** — homepage HTML did not surface complete input, validation, loading, and error states. Suggested form tokens use existing colors but should be verified on product or checkout pages.
- **Dark-mode mapping is partial** — `#121217`, `#141414`, and dark gray tokens exist, but a full light/dark semantic map was not observed from this homepage pass.
- **Logo and customer wall colors filtered by judgment** — frequency candidates include many chromatic ramps and SVG/image-adjacent values; brand priority is based on hero/nav/announcement usage, not raw frequency alone.
- **Responsive behavior is CSS-derived** — breakpoint values are extracted from CSS and inferred from Webflow class rules; mobile screenshot was not captured in this pass.
- **Report HTML intentionally skipped** — per request, Step 6 render/report generation was not executed; this artifact is `design.md` only.
