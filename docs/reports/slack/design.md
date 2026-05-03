---
schema_version: 3.2
slug: slack
service_name: Slack
site_url: https://slack.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: light
brand_color: "#611F69"
primary_font: "Salesforce-Avant-Garde"
font_weight_normal: 400
token_prefix: "slack"

bold_direction: "Enterprise Play"
aesthetic_category: "Refined SaaS"
signature_element: "hero_impact"
code_complexity: "high"

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Homepage CSS exposes a small but consistent variable layer plus repeated c-button, c-nav, o-section, o-block-grid, utility, shadow, and localization patterns."

colors:
  primary: "#611F69"
  primary-dark: "#4A154B"
  link: "#1264A3"
  accent-cyan: "#36C5F0"
  surface: "#FFFFFF"
  surface-soft: "#F5F4F5"
  border: "#EBEAEB"
  text: "#1D1C1D"
  text-muted: "#696969"
  success: "#007A5A"
  danger: "#C01343"
typography:
  display: "Salesforce-Avant-Garde"
  body: "Salesforce-Sans"
  code: "Monaco, Menlo, Consolas, Courier New"
  ladder:
    - { token: hero, size: "clamp-derived / 56px observed hero", weight: 700, tracking: "-0.02em to -0.05em" }
    - { token: section-title, size: "clamp(2rem, 1.92308vw + 1.51923rem, 2.75rem)", weight: 700, tracking: "-0.02em" }
    - { token: h3, size: "clamp(1.5rem, 1.28205vw + 1.17949rem, 2rem)", weight: 700, tracking: "-0.008em" }
    - { token: body, size: "1rem", weight: 400, tracking: "0" }
    - { token: small, size: ".875rem", weight: 400, tracking: "0" }
  weights_used: [200, 300, 400, 500, 600, 700, 800, 900]
  weights_absent: []
components:
  button-primary: { bg: "{colors.primary}", color: "{colors.surface}", radius: "4px", padding: "19px 40px 20px" }
  button-secondary-outline: { bg: "{colors.surface}", color: "{colors.primary}", radius: "4px", border: "inset 0 0 0 1px #611F69" }
  arrow-link-default: { color: "{colors.link}", underline: "2px solid #1264A3" }
  section-card-shadow: { shadow: "0 5px 20px #0000001a", hover: "0 5px 40px #0003" }
---

# DESIGN.md — Slack

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Slack's current homepage is not the old playful chat-product poster. It is an enterprise AI work platform page wearing the familiar Slack face: clean white air, heavy black headlines, and a precise purple command layer. The page keeps the logo's multi-color symbol in the corner, but the interface itself mostly refuses that rainbow. The logo is the confetti at the door; once inside, the room is run by #611F69 (`{colors.primary}`), #4A154B (`{colors.primary-dark}`), #1264A3 (`{colors.link}`), white, black, and a few pale support surfaces. There is no second brand color conducting the UI.

The hero behaves like a boardroom pitch with consumer-product confidence. Navigation is compact and practical, then the H1 arrives as a huge centered statement: "All your people and AI agents working together." The weight is heavy, the tracking is tight, and the line breaks are editorially controlled. It reads like a keynote slide projected onto a white conference wall: the page nearly disappears so the claim can stand upright. Under it, CTAs are rectangular, uppercase, and almost severe; this is Slack moving from friendly team chat into Salesforce-grade workflow infrastructure.

The signature visual move is the product-window mockup that appears below the logos. It is not an ornamental illustration. It is a Slack client surface: dark purple title bar, left rail, message list, Slackbot panel, rounded app chrome, and soft gray skeleton rows. The mockup works like a glass-walled operations room dropped into the marketing page: you can see the agents, messages, search, and workflow machinery through the window, but the surrounding page keeps its hands off the controls.

Slack's craft is in contrast management rather than decorative novelty. The typography is loud, but the page is quiet. Color is chromatic only when it indicates action or platform identity. Shadows are used for product UI and lifted cards, not for every section; shadow belongs to evidence, not decoration. The blue link #1264A3 (`{colors.link}`) acts like a marginal note in a business newspaper, while purple remains the command ink. White space does most of the persuasive work: the H1 gets a full breath before logos, then the product mockup anchors the promise in an actual interface.

### Key Characteristics

- White-first enterprise SaaS composition with a strong black display headline.
- Slack purple #611F69 (`{colors.primary}`) is the action color; logo colors are not the UI palette.
- Deep article/platform purple #4A154B (`{colors.primary-dark}`) appears in hero/product surfaces and themed bands.
- Links use blue #1264A3 (`{colors.link}`), with cyan #36C5F0 (`{colors.accent-cyan}`) reserved for reverse/dark link emphasis.
- CTAs are uppercase, 14px, 700, letter-spaced, and rectangular at 4px radius.
- Display type is tight and heavy; body copy remains plain and centered.
- Layout alternates open editorial bands with dense product UI modules.
- Shadows are large and soft: #0000001a and #0003 support product surfaces, not decorative cards everywhere.
- Navigation is horizontal, information-heavy, and dropdown-oriented.
- Localization is built into the CSS: CJK font stacks and tracking overrides are first-class.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Enterprise Play
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **white-boardroom hero plus purple product chrome**으로 기억된다.
> **Code Complexity**: high — multiple localized font stacks, responsive utility grids, product-surface shadows, dropdown navigation, and animated transition primitives are present.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Slack처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Salesforce-Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  font-weight: 400;
}
h1, h2, .display {
  font-family: "Salesforce-Avant-Garde", "Salesforce-Sans", system-ui, sans-serif;
  font-weight: 700;
  letter-spacing: -0.02em;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #1D1C1D; --muted: #696969; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #611F69; --brand-dark: #4A154B; --link: #1264A3; }
.cta { background: var(--brand); color: #FFFFFF; border-radius: 4px; }
```

**절대 하지 말아야 할 것 하나**: Slack 로고의 빨강/노랑/초록/파랑을 UI 팔레트 전체에 뿌리지 말 것. 실제 홈페이지 UI는 #611F69, #4A154B, #1264A3, #FFFFFF, #1D1C1D 중심이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://slack.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | Reused existing phase1 assets from `insane-design/slack/` |
| HTML size | 229228 bytes |
| CSS files | 9 CSS files, about 943441 characters |
| Token prefix | `slack` |
| Method | Existing CSS/HTML/screenshot phase1 reuse; no report HTML render step |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Marketing site with compiled CSS chunks and server-rendered HTML.
- **Design system**: Slack/Salesforce marketing layer — compact CSS variables plus BEM-like component classes.
- **CSS architecture**:
  ```text
  core/component variables   --article-theme-primary, --sidebar-color, --font-family-*
  component classes          .c-button, .c-nav__cta, .o-section, .o-block-grid
  utility classes            .u-padding-*, .u-box-shadow-*, .u-border-radius-*
  locale overrides           :lang(ja), :lang(ko), :lang(zh-*), :lang(ru)
  ```
- **Class naming**: CUBE-ish/BEM-ish prefixes: `c-` for components, `o-` for objects, `u-` for utilities, `v--` for variants.
- **Default theme**: light (page bg = `#FFFFFF`).
- **Font loading**: custom Salesforce and Slack/Noto family declarations in CSS; locale-specific fallbacks are explicit.
- **Canonical anchor**: homepage hero and AI-agent positioning, not the Slack app chrome alone.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Salesforce-Avant-Garde` (proprietary Salesforce/Slack marketing face)
- **Body font**: `Salesforce-Sans` (proprietary Salesforce/Slack marketing face)
- **Code font**: `Monaco`, `Menlo`, `Consolas`, `Courier New`
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --slack-font-family-heading:
    "Salesforce-Avant-Garde", system-ui, -apple-system, blinkmacsystemfont,
    "Segoe UI", roboto, "Helvetica Neue", arial, "Noto Sans", sans-serif;
  --slack-font-family-body:
    "Salesforce-Sans", system-ui, -apple-system, blinkmacsystemfont,
    "Segoe UI", roboto, "Helvetica Neue", arial, "Noto Sans", sans-serif;
  --slack-font-family-code: "Monaco", "Menlo", "Consolas", "Courier New", monospace;
  --slack-font-weight-normal: 400;
  --slack-font-weight-bold: 700;
}
body { font-family: var(--slack-font-family-body); font-weight: 400; }
h1, h2, h3 { font-family: var(--slack-font-family-heading); font-weight: 700; }
```

### Note on Font Substitutes

- **Salesforce-Avant-Garde** — if unavailable, use `Arial Black` only for quick internal mockups; for production-feeling work use `Inter Tight` at 700 with `letter-spacing: -0.03em`.
- **Salesforce-Sans** — use `Inter` or `Aptos` at 400/600. Keep body line-height around 1.5; Slack's body copy is readable but not loose.
- **CJK fallback** — Slack does not simply reuse the Latin stack. Korean uses `NotoSansKR`/`SeolSansHeavy`-style overrides and tighter tracking. If localizing, do not force Latin negative tracking onto Korean paragraphs.
- **Button text** — preserve uppercase, 700, `.057em` tracking for English CTAs. This matters more than the exact substitute font.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Hero H1 | approx 56px observed; CSS has display clamps | 700 | ~1.12 to 1.25 | tight, often `-.02em` to `-.05em` |
| Section title | `clamp(2rem, 1.92308vw + 1.51923rem, 2.75rem)` | 700 | 1.2 to 1.25 | `-.02em` |
| Feature headline | `clamp(1.75rem, .641026vw + 1.58974rem, 2rem)` | 700 | 1.25 | `-.008em` |
| Body | `1rem` | 400 | 1.5 | `0` |
| Small / nav / button | `.875rem` | 700 for CTAs, 400/600 for links | 1.286 to 1.429 | button `.057em` |
| Micro / labels | `12px` to `13px` | 400/700 | 1.3 to 1.5 | mixed |

> ⚠️ Typography key insight: Slack's homepage is display-heavy, but the control surface is compact. The danger is making it feel like a friendly consumer app with rounded soft type; the actual page uses heavy editorial headlines and uppercase enterprise CTAs.

### Principles

1. Display headlines are heavy and tightly tracked; do not use a soft 500-weight SaaS headline.
2. Body copy is neutral at 400; weight 700 is concentrated in headings, CTAs, and product labels.
3. English buttons use uppercase with `.057em` tracking. This is a major part of the Salesforce-era marketing tone.
4. Locale handling is part of the type system. Korean/Japanese/Chinese receive separate font-family and letter-spacing rules.
5. The system tolerates many weights in CSS, but the visible homepage identity is mostly 400 and 700.
6. Hero copy should break across 2 lines at desktop scale; a single long line loses the Slack composition.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed anchors)

| Token | Hex |
|---|---|
| `{colors.primary}` | `#611F69` |
| `{colors.primary-dark}` | `#4A154B` |
| sidebar dark | `#400D40` |
| deep purple variant | `#481A54` |
| pale purple surface | `#F9F0FF` |
| pale purple alternate | `#F2DEFE` |
| saturated purple accent | `#730394` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--article-theme-primary` | `#4A154B` |
| `--sidebar-color` | `#400D40` |
| dark product chrome | `#481A54` |

### 06-3. Neutral Ramp

| Step | Light | Dark/Text |
|---|---|---|
| page | `#FFFFFF` | `#1D1C1D` |
| soft section | `#F5F4F5` | `#454245` |
| border | `#EBEAEB` | `#696969` |
| hairline | `#E8E8E8` | `#717274` |
| black | `#000000` / `#000` | `#1D1D1D` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Link blue | default arrow links | `#1264A3` |
| Reverse cyan | dark/reverse links | `#36C5F0` |
| Success green | status/support | `#007A5A` |
| Error rose | danger/support | `#C01343` |
| Google blue | integration button/support | `#4285F4` |
| Slack logo red | logo/accent only | `#E01E5A` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| primary action | `#611F69` | CTA background, secondary outline color, active button surface |
| article/platform primary | `#4A154B` | themed bands, hero product chrome, article surfaces |
| link | `#1264A3` | default text links and arrow-link underline |
| reverse link | `#36C5F0` | dark/reverse link color and underline |
| page surface | `#FFFFFF` | dominant homepage background |
| soft surface | `#F5F4F5` | light gray section background |
| border | `#EBEAEB` | section and component hairlines |
| primary text | `#1D1C1D` | main copy |
| muted text | `#696969` | logo-wall and secondary copy |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--article-theme-primary` | `#4A154B` | article/themed primary surface |
| `--article-theme-secondary` | `#FFFFFF` | article/themed secondary surface |
| `--sidebar-color` | `#400D40` | Slack app/product sidebar |
| `--sidebar-highlight-color` | `#1264A3` | sidebar highlight/link |
| `--attachment-color` | `#000000` | attachment accent fallback |
| `--swiper-theme-color` | `#007AFF` | carousel/swiper default |

### 06-7. Dominant Colors (actual CSS frequency order)

| Token | Hex | Frequency note |
|---|---|---|
| white | `#FFFFFF` / `#fff` | most common |
| link blue | `#1264A3` | high chromatic frequency |
| primary purple | `#611F69` | CTA/outline/action frequency |
| black | `#000000` / `#000` | text and masks |
| soft border | `#EBEAEB` | repeated hairline |
| article purple | `#4A154B` | theme variable and product surfaces |
| cyan | `#36C5F0` | reverse links |
| dark text | `#1D1C1D` / `#1D1D1D` | primary copy |

### Color Stories
<!-- §06-8 -->

**`{colors.primary}` (`#611F69`)** — This is the CTA and enterprise action purple. It is used for filled buttons, outlined secondary buttons, active button states, and the strongest Slack-marketing commitment points. It should not be replaced by the logo's brighter red, yellow, green, or blue.

**`{colors.primary-dark}` (`#4A154B`)** — This is Slack's deep platform purple: article themes, hero product chrome, and darker product surfaces. It carries the "inside Slack" feeling without making the whole page dark.

**`{colors.link}` (`#1264A3`)** — Link blue is the information/action bridge. It appears in arrow links and sidebar highlight contexts, which keeps non-primary actions from competing with the purple CTAs.

**`{colors.surface}` (`#FFFFFF`)** — The page floor is plain white. Slack lets the giant headline and product mockup create drama; the background itself stays quiet so the AI/platform message reads as credible.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `space-xs` | `.25rem` | utility padding top x-small |
| `space-sm` | `.5rem` | small utility gaps |
| `space-md` | `1rem` | default gap/padding |
| `space-lg` | `1.5rem` | card/content padding |
| `space-xl` | `2rem` | hero/section module padding |
| `space-2xl` | `4rem` | large vertical section breathing |
| `section` | `3rem 0` | base `.o-section` padding |
| `hero-mobile` | `7rem 0 3rem` | base hero spacing |
| `hero-desktop` | `10rem 0 5rem` | larger hero spacing |
| `container-gutter` | `4vw` / `8vw` | page horizontal gutters |

**주요 alias**:
- `.u-padding-top--medium` → `1rem`
- `.u-padding-top--xx-large` → `4rem`
- `.o-section` → `padding: 3rem 0`

### Whitespace Philosophy

Slack uses white space as a credibility device. The hero headline is allowed to dominate the first viewport, then the CTA row and customer logos sit in compressed but orderly layers underneath. The page does not need decorative gradients above the fold because the space itself creates importance.

Below the hero, spacing tightens around product UI. Cards and interface panels can become dense, but section boundaries keep a clean rhythm with `3rem` base vertical padding and larger desktop hero padding. The rule is "open promise, dense proof."

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| square/control | `0` | flush utilities and edge cases |
| button/control | `4px` | primary `.c-button` radius |
| small surface | `6px` | compact UI details |
| card/surface | `8px` / `.5rem` | product media, small cards |
| medium panel | `10px` / `12px` | lifted modules |
| large panel | `16px` | heavier product surfaces |
| circular | `50%` / `100%` | avatars, icon buttons, dots |
| pill | `60px` / `999px`-style equivalents | occasional capsules |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| none | `none` | most chrome and flat sections |
| card | `0 5px 20px #0000001a` | utility card elevation |
| card hover | `0 5px 40px #0003` | stronger hover lift |
| spread halo | `0 0 2rem #0000001a` | product/window surfaces |
| dense halo | `0 0 2rem #0003` | darker/reverse surface lift |
| large simple | `0 4px 40px #00000014` | soft oversized module depth |
| inset outline | `inset 0 0 0 1px #611F69` | outline button state |
| active outline | `inset 0 0 0 2px #611F69` | hover/active outline state |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| main ease | `.42s cubic-bezier(.165,.84,.44,1)` | button color/background/box-shadow and transforms |
| quick transform | `.1s cubic-bezier(.165,.84,.44,1)` | small interaction feedback |
| soft all | `.22s ease-in-out` | general state transitions |
| opacity reveal | `opacity 1s ease-in .4s` | delayed reveal-style surfaces |
| reduced motion | `@media (prefers-reduced-motion: reduce)` | accessibility branch present |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: repeated `76.875rem`, `1280px`, `54rem`, `760px`, `700px`, and percentage split widths.
- **Grid type**: flexbox object grid plus utility classes; `.o-block-grid` uses flex-wrap.
- **Column count**: 1 column mobile, 2-column object grid at tablet/desktop, richer marketing sections by percentage widths.
- **Gutter**: `2.43902%`, `1rem`, `2rem`, and larger `3rem calc(2 * 1rem)` patterns.

### Hero

- **Pattern Summary**: open white hero + centered two-line H1 + dual CTA row + customer logo strip + product mockup below.
- Layout: centered one-column content with product interface preview below.
- Background: solid `#FFFFFF`.
- **Background Treatment**: solid white; no mesh, no gradient, no hero photography.
- H1: approx `56px` visible desktop / weight `700` / tight tracking.
- Max-width: content visually constrained around the central headline; product mockup wider below.

### Section Rhythm

```css
section,
.o-section {
  padding: 3rem 0;
  border-top: 1px solid #EBEAEB;
  overflow: hidden;
}
.o-hero {
  padding-top: 7rem;
  padding-bottom: 3rem;
}
@media screen and (width >= 48rem) {
  .o-hero {
    padding-top: 10rem;
    padding-bottom: 5rem;
  }
}
```

### Card Patterns

- **Card background**: `#FFFFFF` dominant, with soft section surfaces such as `#F5F4F5`.
- **Card border**: `1px solid #EBEAEB` or inset outlines for controls.
- **Card radius**: 8px to 16px for panels; 4px for buttons.
- **Card padding**: commonly `1rem`, `1.5rem`, `2rem`.
- **Card shadow**: `0 5px 20px #0000001a`, hover to `0 5px 40px #0003` when a card is intentionally lifted.

### Navigation Structure

- **Type**: horizontal desktop navigation with dropdown groups.
- **Position**: top page header, visually static in the captured hero.
- **Height**: nav controls and CTA align around a compact top bar; mobile CTA rule shows `height: 60px`.
- **Background**: `#FFFFFF`.
- **Border**: not dominant in the captured header; internal nav separators use values like `#C9C9C9`.

### Content Width

- **Prose max-width**: section prose often constrained around 700px to 760px.
- **Container max-width**: `1280px` and `76.875rem` appear as large layout anchors.
- **Sidebar width**: product mockup sidebar is visual, not a page layout sidebar; Slack app chrome uses a narrow left rail.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `0-479px`, `0-559px`, `0-615px`, `0-767px` | multiple mobile-specific collapse ranges |
| Tablet | `48rem` / `768px` | major jump for grid and hero spacing |
| Desktop | `64rem` / `1024px` | desktop navigation/layout density |
| Large | `80rem`, `84.875rem`, `116.25rem` | wide marketing page refinements |

### Touch Targets

- **Minimum tap size**: `44px` appears via swiper navigation size; CTAs are larger than 44px.
- **Button height (mobile)**: `60px` nav CTA rule; pricing buttons minimum `42px`.
- **Input height (mobile)**: not directly surfaced in homepage CSS summary.

### Collapsing Strategy

- **Navigation**: desktop horizontal menu becomes mobile-oriented CTA/header structure; detailed mobile menu behavior not fully measured.
- **Grid columns**: `.o-block-grid.v--two` starts at 100% and shifts to about `48.781%` with `2.43902%` gutter.
- **Sidebar**: product mockup sidebar is illustrative and should scale/crop, not become functional navigation.
- **Hero layout**: remains centered; product mockup moves below text and should be allowed to crop or scale.

### Image Behavior

- **Strategy**: product UI screenshots/mockups behave as anchored proof modules below text.
- **Max-width**: frequent `100%`, `80%`, `90%`, `1280px`, and percentage split values.
- **Aspect ratio handling**: screenshot-like product windows should maintain fixed aspect ratio and rounded chrome.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA**

```html
<a class="c-button v--primary" href="#">Get started</a>
```

| Property | Value |
|---|---|
| background | `#611F69` |
| color | `#FFFFFF` |
| radius | `4px` |
| padding | `19px 40px 20px` |
| font | `.875rem`, `700`, uppercase |
| letter-spacing | `.057em` |
| transition | `box-shadow/color/background .42s cubic-bezier(.165,.84,.44,1)` |

States: hover should stay in the purple family and may deepen or outline; focus/active must remain visibly purple with adequate contrast.

**Secondary Outline CTA**

```html
<a class="c-button v--secondary" href="#">Request a demo</a>
```

| Property | Value |
|---|---|
| background | `#FFFFFF` |
| color/fill | `#611F69` |
| outline | `inset 0 0 0 1px #611F69` |
| hover outline | `inset 0 0 0 2px #611F69` |
| active background | `#611F69` |
| active color | `#FFFFFF` |

### Badges

Slack's homepage does not rely on generic pill badges above the fold. When label-like UI is needed, it should be compact, text-led, and subordinate to the CTA/link system.

| Property | Recommended Slack-like value |
|---|---|
| font | `Salesforce-Sans`, 12px to 14px |
| weight | 600 or 700 only when acting as a control |
| radius | 4px to 999px depending on chip role |
| color | neutral text or #611F69 for action-bearing labels |

### Cards & Containers

```html
<article class="slack-card">
  <h3>Knowledge</h3>
  <p>Find answers and context inside Slack.</p>
</article>
```

| Property | Value |
|---|---|
| background | `#FFFFFF` or `#F5F4F5` |
| border | `1px solid #EBEAEB` when structure is needed |
| radius | `8px` to `16px` |
| padding | `1.5rem` to `2rem` |
| shadow | none by default; `0 5px 20px #0000001a` for lifted cards |
| hover | shadow can deepen to `0 5px 40px #0003`; avoid bouncey transforms |

### Navigation

```html
<header class="slack-nav">
  <a class="logo">slack</a>
  <nav>
    <button>Features</button>
    <button>Solutions</button>
    <a>Enterprise</a>
    <button>Resources</button>
    <a>Pricing</a>
  </nav>
  <a class="c-button v--secondary">Request a demo</a>
  <a class="c-button v--primary">Get started</a>
</header>
```

| Property | Value |
|---|---|
| background | `#FFFFFF` |
| text | `#1D1C1D` |
| link weight | 600-ish visual weight in nav |
| CTA placement | right aligned |
| mobile CTA | full-width/60px pattern appears in CSS |

### Inputs & Forms

Homepage form states were not prominent in the captured first viewport. Use Slack's control language when creating inputs:

| Property | Value |
|---|---|
| border | `1px solid #EBEAEB` or stronger focus outline |
| focus | `#1264A3` for informational focus, `#611F69` for conversion forms |
| radius | `4px` to `8px` |
| error | `#C01343` |
| success | `#007A5A` |

### Hero Section

```html
<section class="slack-hero">
  <h1>All your people and AI agents working together.</h1>
  <p>Slack connects your team. Slackbot multiplies what they can do.</p>
  <div class="cta-row">
    <a class="c-button v--primary">Get started</a>
    <a class="c-button v--secondary">Find your plan</a>
  </div>
  <div class="trusted-row">Trusted by top teams ...</div>
  <div class="product-window">...</div>
</section>
```

| Property | Value |
|---|---|
| background | `#FFFFFF` |
| alignment | centered |
| H1 | very large, weight 700, tight tracking |
| subcopy | centered, `#1D1C1D`, 1rem-ish |
| CTA row | primary filled + secondary outline |
| proof | customer logo row before product mockup |
| product mockup | deep purple chrome, rounded panel, soft lower-page anchor |

### 13-2. Named Variants

**button-primary-purple**

| Property | Value |
|---|---|
| bg | `#611F69` |
| text | `#FFFFFF` |
| radius | `4px` |
| casing | uppercase |
| state | keep purple identity; do not introduce logo-rainbow hover |

**button-secondary-purple-outline**

| Property | Value |
|---|---|
| bg | `#FFFFFF` |
| text | `#611F69` |
| outline | `inset 0 0 0 1px #611F69` |
| hover | `inset 0 0 0 2px #611F69` |
| active | bg `#611F69`, text `#FFFFFF` |

**arrow-link-default**

| Property | Value |
|---|---|
| text | `#1264A3` |
| underline | `2px solid #1264A3` via pseudo-element |
| reverse | `#36C5F0` on dark/reverse contexts |

**product-window-purple-chrome**

| Property | Value |
|---|---|
| top bar | deep purple family, visually near `#4A154B`/`#481A54` |
| body | white panels with pale gray skeleton rows |
| radius | around `8px` to `10px` |
| role | concrete proof of AI/agent workflow |

### 13-3. Signature Micro-Specs

```yaml
purple-command-cta:
  description: "Slack turns conversion actions into compact enterprise commands rather than soft SaaS pills."
  technique: "font-size: .875rem; font-weight: 700; text-transform: uppercase; letter-spacing: .057em; border-radius: 4px; padding: 19px 40px 20px; background: #611F69 /* {colors.primary} */"
  applied_to: ["{component.button-primary}", "{component.c-nav__cta}", "{component.hero-cta}"]
  visual_signature: "friendly Slack logo beside severe rectangular purple commands"

purple-outline-inversion:
  description: "Secondary actions stay in the same purple command system and invert instead of becoming neutral gray controls."
  technique: "background: #FFFFFF; color: #611F69; box-shadow: inset 0 0 0 1px #611F69; hover box-shadow: inset 0 0 0 2px #611F69; active background: #611F69; active color: #FFFFFF"
  applied_to: ["{component.button-secondary-outline}", "{component.demo-cta}", "{component.plan-cta}"]
  visual_signature: "a white button that still reads as purple infrastructure before it is clicked"

blue-editorial-arrow-link:
  description: "Informational movement is separated from conversion by a newspaper-like blue link lane."
  technique: "color: #1264A3 /* {colors.link} */; underline: 2px solid #1264A3 via pseudo-element; reverse color: #36C5F0 /* {colors.accent-cyan} */ on dark contexts"
  applied_to: ["{component.arrow-link-default}", "{component.reverse-link}", "{component.feature-link}"]
  visual_signature: "blue marginal-note links that never compete with the purple CTA system"

single-step-product-shadow:
  description: "Elevation is reserved for proof surfaces and selected cards, with one large soft jump rather than a full depth ladder."
  technique: "box-shadow: 0 5px 20px #0000001a; hover box-shadow: 0 5px 40px #0003; no bouncey transform"
  applied_to: ["{component.section-card-shadow}", "{component.product-window}", "{component.lifted-card}"]
  visual_signature: "product evidence floats just enough to feel real, while surrounding sections remain flat white"

localized-display-density:
  description: "The homepage keeps headline compression across languages instead of letting localized copy loosen the layout."
  technique: ":lang(ko), :lang(ja), :lang(zh-*), :lang(ru) font-stack overrides; display tracking around -.02em to -.05em; heading weights held at 700"
  applied_to: ["{component.hero-heading}", "{component.section-title}", "{component.nav-cta}"]
  visual_signature: "global marketing type that remains dense and keynote-like after localization"
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | broad platform promise, direct and declarative | "All your people and AI agents working together." |
| Primary CTA | short uppercase imperative | "GET STARTED" |
| Secondary CTA | plan/demo-oriented enterprise action | "REQUEST A DEMO", "FIND YOUR PLAN" |
| Subheading | explanatory but compact | "Slack connects your team. Slackbot multiplies what they can do." |
| Tone | enterprise confidence with familiar product nouns | AI agents, Slackbot, teams, work, platform |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Slack-inspired homepage system */
:root {
  /* Fonts */
  --slack-font-family-heading:
    "Salesforce-Avant-Garde", "Inter Tight", system-ui, -apple-system, "Segoe UI", sans-serif;
  --slack-font-family-body:
    "Salesforce-Sans", "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
  --slack-font-family-code: "Monaco", "Menlo", "Consolas", "Courier New", monospace;
  --slack-font-weight-normal: 400;
  --slack-font-weight-bold: 700;

  /* Brand */
  --slack-color-brand-25:  #F9F0FF;
  --slack-color-brand-300: #730394;
  --slack-color-brand-500: #611F69;
  --slack-color-brand-600: #4A154B;
  --slack-color-brand-900: #400D40;

  /* Surfaces */
  --slack-bg-page:    #FFFFFF;
  --slack-bg-soft:    #F5F4F5;
  --slack-border:     #EBEAEB;
  --slack-text:       #1D1C1D;
  --slack-text-muted: #696969;
  --slack-link:       #1264A3;
  --slack-link-dark:  #36C5F0;

  /* Key spacing */
  --slack-space-sm:  .5rem;
  --slack-space-md:  1rem;
  --slack-space-lg:  1.5rem;
  --slack-space-xl:  2rem;
  --slack-section-y: 3rem;

  /* Radius + shadow */
  --slack-radius-control: 4px;
  --slack-radius-card: 8px;
  --slack-shadow-card: 0 5px 20px #0000001a;
  --slack-shadow-card-hover: 0 5px 40px #0003;
}

body {
  background: var(--slack-bg-page);
  color: var(--slack-text);
  font-family: var(--slack-font-family-body);
  font-weight: var(--slack-font-weight-normal);
}

.slack-display {
  font-family: var(--slack-font-family-heading);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.12;
}

.slack-button {
  appearance: none;
  border: 0;
  border-radius: var(--slack-radius-control);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 19px 40px 20px;
  font-size: .875rem;
  font-weight: 700;
  line-height: 1.286;
  letter-spacing: .057em;
  text-transform: uppercase;
  transition:
    box-shadow .42s cubic-bezier(.165,.84,.44,1),
    color .42s cubic-bezier(.165,.84,.44,1),
    background .42s cubic-bezier(.165,.84,.44,1);
}

.slack-button-primary {
  background: var(--slack-color-brand-500);
  color: #FFFFFF;
}

.slack-button-secondary {
  background: #FFFFFF;
  color: var(--slack-color-brand-500);
  box-shadow: inset 0 0 0 1px #611F69;
}

.slack-button-secondary:hover {
  box-shadow: inset 0 0 0 2px #611F69;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Slack-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        slack: {
          purple: '#611F69',
          purpleDark: '#4A154B',
          sidebar: '#400D40',
          link: '#1264A3',
          cyan: '#36C5F0',
          surface: '#FFFFFF',
          soft: '#F5F4F5',
          border: '#EBEAEB',
          text: '#1D1C1D',
          muted: '#696969',
          success: '#007A5A',
          danger: '#C01343',
        },
      },
      fontFamily: {
        sans: ['Salesforce-Sans', 'Inter', 'system-ui', 'sans-serif'],
        display: ['Salesforce-Avant-Garde', 'Inter Tight', 'system-ui', 'sans-serif'],
        mono: ['Monaco', 'Menlo', 'Consolas', 'monospace'],
      },
      borderRadius: {
        slackControl: '4px',
        slackCard: '8px',
      },
      boxShadow: {
        slackCard: '0 5px 20px #0000001a',
        slackCardHover: '0 5px 40px #0003',
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
| Brand primary | `{colors.primary}` | `#611F69` |
| Brand dark | `{colors.primary-dark}` | `#4A154B` |
| Background | `{colors.surface}` | `#FFFFFF` |
| Text primary | `{colors.text}` | `#1D1C1D` |
| Text muted | `{colors.text-muted}` | `#696969` |
| Border | `{colors.border}` | `#EBEAEB` |
| Link | `{colors.link}` | `#1264A3` |
| Reverse link | `{colors.accent-cyan}` | `#36C5F0` |
| Success | `{colors.success}` | `#007A5A` |
| Error | `{colors.danger}` | `#C01343` |

### Example Component Prompts

#### Hero Section

```text
Slack homepage style hero를 만들어줘.
- 배경: #FFFFFF
- H1: Salesforce-Avant-Garde 계열, 매우 큰 2-line centered headline, weight 700, tracking -0.02em
- 본문: #1D1C1D, 1rem, centered
- CTA: primary #611F69 filled uppercase button + secondary #611F69 outline button
- 버튼: radius 4px, padding 19px 40px 20px, letter-spacing .057em
- 아래에는 customer logo row와 deep purple Slack product-window mockup을 배치
```

#### Card Component

```text
Slack marketing card를 만들어줘.
- 배경: #FFFFFF 또는 #F5F4F5
- border: 1px solid #EBEAEB
- radius: 8px 또는 16px
- padding: 1.5rem-2rem
- shadow: 기본 none, lifted card만 0 5px 20px #0000001a
- hover: 필요할 때만 0 5px 40px #0003
- 제목: display/sans 700, tight tracking
- 본문: #1D1C1D 또는 #696969, line-height 1.5
```

#### Badge

```text
Slack style label/chip을 만들어줘.
- 기본은 badge를 남발하지 말고 텍스트 링크나 버튼으로 해결
- 필요하면 12-14px, weight 600, radius 4px-999px
- 색상은 neutral 또는 #611F69만 사용
- Slack 로고 색 4개를 badge 팔레트로 확장하지 말 것
```

#### Navigation

```text
Slack homepage navigation을 만들어줘.
- 배경 #FFFFFF, 좌측 Slack logo, 중앙 Features/Solutions/Enterprise/Resources/Pricing
- 우측 search icon, Sign in, REQUEST A DEMO outline, GET STARTED filled
- 링크는 #1D1C1D, compact, 600-ish visual weight
- CTA는 uppercase, #611F69, radius 4px
- 모바일에서는 full-width 60px CTA 패턴을 고려
```

### Iteration Guide

- **색상 변경 시**: #611F69과 #4A154B의 역할을 분리한다. 전자는 action, 후자는 product/platform chrome.
- **폰트 변경 시**: heading/body를 같은 generic sans로 평평하게 만들지 말고 display는 더 압축된 대체 폰트를 쓴다.
- **여백 조정 시**: hero는 넓게, product proof는 밀도 있게. 전부 같은 카드 간격으로 만들면 Slack 느낌이 사라진다.
- **새 컴포넌트 추가 시**: 4px button radius, 8-16px card radius, soft shadow only for lifted proof modules.
- **로고 컬러 사용 시**: 로고/아이콘 외 사용은 보조 accent 수준으로 제한한다.
- **반응형**: 48rem과 64rem 전환을 기준으로 hero spacing과 grid density를 조정한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#611F69` for primary action and enterprise CTA surfaces.
- Use `#4A154B` or `#400D40` for deep Slack product/platform chrome.
- Keep the page floor mostly `#FFFFFF`; let typography and product UI carry the drama.
- Use `#1264A3` for default informational links and `#36C5F0` only in reverse/dark contexts.
- Keep CTAs uppercase, 700, tightly tracked, and rectangular at `4px` radius.
- Use large soft shadows only on cards/product windows that are meant to float.
- Preserve localization-aware font and tracking behavior for non-English surfaces.
- Ground AI/agent claims in Slack UI mockups, not abstract decorative AI visuals.

### ❌ DON'T

- 배경을 `#F9F0FF` 또는 임의의 purple-tinted page wash로 두지 말 것 — 대신 `#FFFFFF` 사용.
- primary CTA를 `#E01E5A`, `#ECB22E`, `#2EB67D`, `#36C5F0` 같은 로고 색으로 두지 말 것 — 대신 `#611F69` 사용.
- 기본 링크를 `#611F69`으로 전부 칠하지 말 것 — 일반 링크는 `#1264A3`, primary action만 `#611F69`.
- 본문 텍스트를 `#000000` pure black으로 고정하지 말 것 — 대신 `#1D1C1D` 사용.
- muted copy를 `#454245`로 과하게 진하게 만들지 말 것 — 대신 `#696969` 또는 `#717274` 사용.
- hairline border를 `#C9C9C9`로 일반화하지 말 것 — 대신 `#EBEAEB` 또는 `#E8E8E8` 사용.
- 버튼을 `border-radius: 999px` pill로 만들지 말 것 — Slack CTA는 `border-radius: 4px`.
- CTA text를 lowercase sentence case로 만들지 말 것 — homepage CTA는 uppercase + `letter-spacing: .057em`.
- 모든 카드에 `box-shadow: 0 10px 30px #00000033`을 주지 말 것 — 기본은 flat, lifted proof만 `#0000001a`/`#0003`.
- 로고 컬러 4개를 feature-card palette로 확장하지 말 것 — Slack homepage UI는 logo-rainbow가 아니라 enterprise purple system이다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- No full-page purple gradient hero. The first viewport is white, not a decorative color field.
- No rainbow UI system. Logo colors exist, but they do not become a general component palette.
- No pill-first CTA language. Primary buttons are compact 4px rectangles.
- No glassmorphism. Product UI is crisp app chrome, not blurred translucent panels.
- No heavy border-card grid above the fold. The hero uses open space, logos, and one product mockup.
- No playful emoji-led AI metaphor. AI is expressed through Slackbot/product actions.
- No generic blue SaaS primary. Blue is link/informational; purple is conversion.
- No universal shadow. Shadow appears when a module needs proof/elevation.
- No single-language typography assumption. Locale-specific type rules are built into the system.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual / REQUIRED -->

- **Single homepage surface** — this analysis reused the existing Slack homepage phase1 assets. Logged-in Slack app, admin, billing, and workspace settings surfaces were not analyzed.
- **Desktop screenshot bias** — the inspected screenshot is a desktop hero crop. Mobile menu behavior is inferred from CSS breakpoints and mobile CTA rules, not visually verified in this run.
- **CSS chunks are large and compiled** — class/function names are reliable where repeated, but some values are chunk artifacts or legacy patterns. The guide prioritizes visible homepage patterns.
- **Logo wall color pollution** — customer logo SVG/color values may contribute to CSS frequency. Brand selection therefore prioritizes CTA and component roles over raw color count.
- **Form states incomplete** — homepage first viewport did not surface full form validation, loading, error, or disabled states. Input specs are constrained recommendations from observed semantic colors.
- **Motion logic not fully executed** — CSS transition values were extracted, but JS-triggered reveal, dropdown, carousel, and scroll timing were not traced.
- **Exact font licensing unavailable** — Salesforce font names are present in CSS; substitute guidance is practical rather than license advice.
- **Dark mode mapping absent** — homepage is light-first. Deep purple product surfaces are not a complete dark-mode token system.
