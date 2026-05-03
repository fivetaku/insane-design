---
schema_version: 3.2
slug: bcg
service_name: BCG
site_url: https://www.bcg.com
fetched_at: 2026-04-14T01:14:00+09:00
default_theme: light
brand_color: "#7EF473"
primary_font: "henderson-bcg-sans"
font_weight_normal: 400
token_prefix: bcg

bold_direction: "Institutional Precision"
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: editorial-magazine
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "CSS variables 460 total, 367 resolved, named button/component state tokens and consistent 12-column layout patterns."

colors:
  accent-primary: "#7EF473"
  accent-hover: "#71DC68"
  green-deep: "#0E3E1B"
  green-action: "#197A56"
  text-primary: "#212427"
  surface-base: "#FFFFFF"
  surface-warm: "#F1EEEA"
  hairline: "#DCD5CE"
typography:
  display: "henderson-bcg-sans"
  body: "henderson-bcg-sans"
  serif: "henderson-bcg-serif"
  headline-alt: "henderson-bcg-headline"
  ladder:
    - { token: hero-h1, size: "96px", weight: 300, line_height: "100%" }
    - { token: section-title, size: "52px", weight: 300, line_height: "110%" }
    - { token: card-title, size: "24px", weight: 400, line_height: "120%" }
    - { token: body, size: "16px", weight: 400, line_height: "140%" }
    - { token: utility, size: "12px", weight: 700, line_height: "100%" }
  weights_used: [100, 200, 300, 400, 600, 700, 800, 900]
  weights_absent: [500]
components:
  button-primary-animated: { bg: "{colors.accent-primary}", fg: "{colors.text-primary}", radius: "15px", padding: "13px 24px", hover_padding_left: "55px" }
  button-secondary-outline: { bg: "{colors.surface-base}", fg: "{colors.text-primary}", border: "{colors.text-primary}", radius: "15px" }
  floating-header-pill: { bg: "translucent white", blur: "20px", radius: "var(--headerRadius)", shadow: "var(--box-shadow)" }
---

# DESIGN.md — BCG (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

BCG reads like a **broadsheet** published by a consultancy that learned design discipline before it learned brand display. The surface opens on a warm `#F1EEEA` (`{colors.surface-warm}`) and `#FFFFFF` (`{colors.surface-base}`) field — closer to the uncoated **parchment** of a research report than the gloss of a financial quarterly. The typography is Henderson BCG Sans across all text families: the hero headline breathes at 96px, weight 300, like the masthead of a broadsheet edition, while the functional labels compress to 12px / 700 / uppercase — the **rhythm** of a print edition where section-jumps and headlines carry the page, not ornamental weight ladders.

The **editorial** discipline is the brand. `#7EF473` (`{colors.accent-primary}`) appears only on action surfaces — the single primary button and the CTA hover fill. It behaves like the single **magazine** color-break rule in a newsprint layout: one deliberate interruption in an otherwise monochrome composition. `#0E3E1B` (`{colors.green-deep}`) is the institutional authority band, the subscription page's **broadsheet** footer block, not a conversion color. Between them sits a hairline system in `#DCD5CE` (`{colors.hairline}`) that acts like printed column rules — almost invisible, entirely structural.

The component that earns the most study is the animated primary button. On hover, the left padding expands to 55px as an arrow travels through the space — not a color shift or a shadow lift but a **rhythm** event: the sentence that finishes a paragraph by moving sideways. BCG's header pill with `backdrop-filter: blur(20px)` does the same job for the chrome tier, placing a translucent **editorial** masthead above the page content rather than a solid opaque bar. The page's identity lives in that blur — the sense that the publication is still happening somewhere behind the navigation, still running on consulting-grade **magazine** cadence. Weight 500 is absent by design: no middle-gray compromise, just the **broadsheet** editor's choice to split thinking and action at a clean typographic break.

### Key Characteristics

- Henderson BCG Sans 중심의 editorial consulting typography.
- Primary CTA는 #7EF473 라임 단일 신호로 제한된다.
- Deep green #0E3E1B는 CTA가 아니라 무게 있는 subscription / institutional band에 쓰인다.
- Warm neutral #F1EEEA와 #DCD5CE가 백서/리포트 같은 배경 온도를 만든다.
- 12-column grid와 module padding으로 홈페이지가 publication index처럼 정렬된다.
- Floating header pill은 translucent white, blur(20px), shadow를 결합한다.
- Buttons are engineered: animated arrow, expanded padding, explicit focus/active/disabled tokens.
- Typography uses light 300 display and bold 700 utility labels, with weight 500 absent.
- Cards rely on photography and content hierarchy more than decorative chrome.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Institutional Precision
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **라임 CTA와 블러 처리된 pill 헤더가 붙은 전략 리포트 편집면**으로 기억된다.
> **Code Complexity**: high — 460 CSS variables, component state tokens, animated CTA padding, backdrop-filter header, 12-column editorial modules.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 BCG처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "henderson-bcg-sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #212427; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 액션 컬러 */
:root { --brand: #7EF473; --deep: #0E3E1B; }
.primary-button {
  background: var(--brand);
  color: #212427;
  border-radius: 15px;
  padding: 13px 24px;
}
```

**절대 하지 말아야 할 것 하나**: BCG를 "딥그린 배경 + 흰색 CTA" 사이트로 단순화하지 말 것. 실제 행동 색은 #7EF473이고, 딥그린 #0E3E1B는 무게 있는 섹션 배경이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.bcg.com` |
| Fetched | 2026-04-14T01:14:00+09:00 (phase1 reused) |
| Extractor | cached HTML/CSS + phase1 JSON reuse |
| HTML size | 799597 bytes (Brightspot-rendered marketing/editorial site) |
| CSS files | 1 external + 1 inline, total 1379806 bytes |
| Token prefix | mixed raw BCG variables; normalized here as `bcg-*` |
| Method | CSS custom properties, frequency candidates, typography JSON, HTML heading structure, screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Brightspot CMS / BCG Global marketing site
- **Design system**: BCG site tokens — global color variables, Henderson font variables, button state variables
- **CSS architecture**:
  ```text
  core       (--gray-*, --neutral-*, --green-*, --accent-*) raw palette
  component  (--primary_button-*, --secondary_button-*, --buttonRadius) stateful component API
  layout     ([data-module], Page-header, subscription-basic--homepage) module and page scaffolding
  ```
- **Class naming**: BEM-ish component classes plus Brightspot module classes (`Page-header`, `Promo-*`, `subscription-basic--homepage`, `[data-module]`)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: custom Henderson BCG font family variables with Helvetica/Arial fallbacks
- **Canonical anchor**: Homepage H1 "Unlocking the Potential of Those Who Advance the World"; navigation and article/promo modules dominate the DOM.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `henderson-bcg-sans` (brand/custom)
- **Body font**: `henderson-bcg-sans` (brand/custom)
- **Serif font**: `henderson-bcg-serif` for editorial alternates
- **Headline alternate**: `henderson-bcg-headline`
- **Code font**: not surfaced as a product-level token in sampled homepage CSS
- **Weight normal / bold**: `400` / `700`; display frequently uses `300`

```css
:root {
  --bcg-font-family: "henderson-bcg-sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --bcg-font-family-serif: "henderson-bcg-serif", "Palatino Linotype", Palatino, Garamond, Georgia, serif;
  --bcg-font-family-headline: "henderson-bcg-headline", Cambria, "Hoefler Text", Times, "Times New Roman", serif;
  --bcg-font-weight-display: 300;
  --bcg-font-weight-normal: 400;
  --bcg-font-weight-utility: 700;
}
body {
  font-family: var(--bcg-font-family);
  font-weight: var(--bcg-font-weight-normal);
}
```

### Note on Font Substitutes

- **henderson-bcg-sans** is a private brand face. Use **Inter** only as a functional fallback, not as the design target.
- Open-source substitute: **Inter** at display weight 300, body 400, utility 700. Tighten display line-height to `100%` or `110%`; do not use Inter's default relaxed marketing line-height.
- For editorial serif moments, use **Source Serif 4** or **Libre Baskerville** instead of Georgia alone. Keep serif usage sparse; BCG's homepage sample is sans-led.
- Preserve the missing middle: avoid `font-weight: 500`. BCG jumps from 400 body to 700 utility labels and uses 300 for large display.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| hero-h1 | `96px` | `300` | `100%` | `0` |
| display-xl | `52px` | `300` | `110%` | `0` |
| display-lg | `48px` | `300` | `110%` | `0` |
| section-title | `40px` | `300/400` | `120%` | `0` |
| card-title | `24px` | `400` | `120%` | `0` |
| body | `16px` | `400` | `140%` | `0` |
| meta | `14px` | `400/700` | `120%` | `0` |
| utility-button | `12px` | `700` | `100%` | `0`, uppercase |

> ⚠️ Key insight: BCG's authority comes from light large type plus very firm small utility labels, not from heavy hero headlines.

### Principles

1. Display weight is 300, not 600. Large BCG headlines should feel strategic and open, not startup-bold.
2. Body defaults to 400 with 140% line-height; it should read like an article index, not a dense dashboard.
3. Utility labels and CTA text use 12px/700/uppercase. Small text is where the system becomes assertive.
4. Weight 500 is deliberately absent in the sampled system; do not insert medium weight as a "safe" compromise.
5. Letter-spacing is not a visible signature here. Keep tracking at 0 unless a specific all-caps utility label needs minor optical correction.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (5 steps)
<!-- raw BCG site tokens -->

| Token | Hex |
|---|---|
| `--green-200` | `#DCF9E3` |
| `--green-300` | `#A8F0B8` |
| `--green-400` | `#21BF61` |
| `--green-500` | `#197A56` |
| `--green-700` | `#0E3E1B` |

### 06-2. Accent / CTA Ramp

| Token | Hex |
|---|---|
| `--accent-200` | `#7EF473` |
| `--accent-300` | `#71DC68` |

### 06-3. Neutral Ramp

| Step | Light / Warm | Dark / Ink |
|---|---|---|
| gray-200 | `#F2F2F2` | |
| gray-300 | `#D4D4D4` | |
| gray-400 | `#B1B1B1` | |
| gray-450 | `#898888` | |
| gray-500 | `#696969` | |
| gray-700 | `#323232` | |
| black | | `#212427` |
| charcoal | | `#232326` |
| white | `#FFFFFF` | |

### 06-4. Warm Neutrals

| Token | Hex | Usage |
|---|---|---|
| `--neutral-200` | `#F1EEEA` | warm editorial backgrounds / dataviz base |
| `--neutral-250` | `#DCD5CE` | disabled button fill / subtle dividers |
| `--neutral-300` | `#DFD7CD` | warm surface step |
| `--neutral-400` | `#C4B5A4` | secondary warm structure |
| `--neutral-500` | `#AB947E` | warm muted accent |
| `--neutral-700` | `#856E57` | dark warm accent |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--alert-200` | `#FCE1DC` | error/negative background |
| `--alert-400` | `#D82216` | error primary |
| `--alert-500` | `#A1150C` | error darker |
| `--alert-700` | `#660F09` | error deepest |
| `--warning-200` | `#FFFBE8` | warning background |
| `--warning-400` | `#FFCF24` | warning primary |
| `--success-200` | `#DCF9E3` | success background |
| `--success-400` | `#21BF61` | success primary |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--primary_button-animated-default_state-background_color` | `--accent-200` / `#7EF473` | animated primary CTA default |
| `--primary_button-non_animated-hover_state-background_color` | `--accent-300` / `#71DC68` | non-animated primary CTA hover |
| `--primary_button-animated-focus_state-background_color` | `--green-700` / `#0E3E1B` | primary CTA focus |
| `--secondary_button-animated-default_state-background_color` | `--white` / `#FFFFFF` | secondary outline surface |
| `--secondary_button-animated-active_state-background_color` | `--gray-200` / `#F2F2F2` | secondary active surface |
| `--primary_button-non_animated-disabled_state-background_color` | `--neutral-250` / `#DCD5CE` | disabled primary surface |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---|---|
| white | `#FFFFFF` | 58 |
| black | `#000000` | 20 |
| BCG ink | `#212427` | 13 |
| video/slate chromatic | `#73859F` | 9 |
| warm neutral | `#F1EEEA` | 8 |
| video dark | `#2B333F` | 7 |
| deep green | `#0E3E1B` | 6 |
| alert red | `#D82216` | 6 |
| accent primary | `#7EF473` | 5 |
| green tint | `#A8F0B8` | 5 |

### 06-8. Color Stories

**`{colors.accent-primary}` (`#7EF473`)** — This is the action color, not a decorative brand wash. Use it for primary CTA backgrounds, audio/action affordances, and moments where BCG wants the page to convert from reading to action.

**`{colors.green-deep}` (`#0E3E1B`)** — The institutional green. It carries subscription bands, focus/active states, and heavier brand fields; it should feel like a boardroom wall, not a generic success color.

**`{colors.text-primary}` (`#212427`)** — The real ink of the site. BCG does not use pure #000000 for the main reading voice; this near-black keeps editorial content warmer and less brittle.

**`{colors.surface-warm}` (`#F1EEEA`)** — The paper tone. Use it when white feels too sterile, especially for research/report modules or dataviz-adjacent backgrounds.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--buttonPaddingBlock` | `13px` | vertical CTA padding |
| `--buttonPaddingInline` | `24px` | default horizontal CTA padding |
| `--cta-button-expanded-padding` | `55px` | animated CTA hover expansion |
| `--modulePaddingTop` | variable | module vertical rhythm |
| `--modulePaddingLarge` | `120px` | large editorial modules |
| `--page-margin-small` | `16px` | mobile page margin |
| subscription content padding | `96px 40px 96px 0` | desktop subscription band |
| small card/button padding | `12px 32px` | compact action/layout controls |

**주요 alias**:
- `--buttonPaddingBlock` → `13px` (CTA vertical rhythm)
- `--buttonPaddingInline` → `24px` (CTA default width)
- `--cta-button-expanded-padding` → `55px` (hover arrow choreography)

### Whitespace Philosophy

BCG spaces like an editorial system with a corporate skeleton underneath. The module grid can be dense, especially where many industries, capabilities, and article cards are indexed, but major bands receive 96px to 120px of vertical breathing room. The result is not minimalist emptiness; it is organized abundance.

The CTA spacing tells the deeper story. Default buttons are compact at 13px/24px, then expand to 55px on hover to make room for directional motion. Space is not only a layout value; it is an interaction state.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| `--button-radius` | `15px` | primary/secondary CTA shape |
| `--radius-5` | `5px` | small utility radius |
| `--radius-10` | `10px` | compact surface radius |
| `--radius-15` | `15px` | default rounded control |
| `--radius-20` | `20px` | larger card / modal radius |
| `--radius-25` | `25px` | large pill/chassis |
| `--radius-30` | `30px` | form/search containers |
| `--radius-70` | `70px` | large capsule / hero image radius |
| header radius | `var(--headerRadius)` | floating blurred header groups |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: responsive module containers; sampled CSS includes `500px`, `767px`, `1023px`, and full-width module modes.
- **Grid type**: CSS Grid for major homepage modules; Flexbox for navigation, sliders, and carousel internals.
- **Column count**: 12 columns on desktop subscription/homepage modules.
- **Gutter**: `var(--gap-spacing-d)` in 12-column desktop contexts.

### Hero
- **Pattern Summary**: large editorial H1 + fixed translucent header + image/article promo field below.
- Layout: one-column editorial statement with dense content index and photography modules following.
- Background: #FFFFFF base, with photography-driven promo modules.
- **Background Treatment**: solid surface plus content imagery; no synthetic mesh gradient in sampled homepage.
- H1: `96px` / weight `300` / tracking `0`
- Max-width: content-led; hero text should remain broad enough for a statement, not a narrow SaaS headline.

### Section Rhythm

```css
section,
[data-module] {
  padding-block: var(--modulePaddingTop) var(--modulePaddingBottom);
}

.subscription-basic--homepage .subscription-basic__content {
  padding: 96px 40px 96px 0;
}
```

### Card Patterns
- **Card background**: primarily #FFFFFF or photography with overlay content cards.
- **Card border**: subtle or absent; warm hairlines such as #DCD5CE appear in disabled/divider contexts.
- **Card radius**: 15px/20px common; hero imagery may move toward 70px.
- **Card padding**: 32px-ish compact cards, larger editorial promo cards.
- **Card shadow**: used sparingly; header and form/search containers rely more on blur/shadow than every card.

### Navigation Structure
- **Type**: fixed global header with left menu/logo cluster and right utility cluster.
- **Position**: fixed top; scroll state controls opacity and header behavior.
- **Height**: `var(--header-height) + 1px`.
- **Background**: translucent white in closed state; #FFFFFF full-width when mega menu opens.
- **Border**: `1px solid var(--headerBorderColor)` when menu state opens.

### Content Width
- **Prose max-width**: content-dependent; cards and article modules often enforce narrower reading widths.
- **Container max-width**: responsive breakpoint-driven, with 12-column desktop modules.
- **Sidebar width**: not a persistent homepage sidebar; mega menu/search surfaces are overlay-driven.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `<768px` | one-column modules, 16px page margins, hamburger/menu-first header |
| Tablet | `768px` | transitional content widths, expanded cards, stronger grid behavior |
| Desktop | `1024px` | 12-column module grid and split subscription content |
| Large | `>1024px` | full editorial modules with larger padding and persistent header clusters |

### Touch Targets
- **Minimum tap size**: CTA padding 13px/24px gives button heights near the 44px target when text is included.
- **Button height (mobile)**: inferred from 13px vertical padding plus 12px/14px utility text.
- **Input height (mobile)**: search/form CSS uses 12px padding and 30px form radius; exact input height not fully surfaced in homepage sample.

### Collapsing Strategy
- **Navigation**: fixed header clusters collapse into menu-led interaction; mega menu opens as a full white state.
- **Grid columns**: desktop `repeat(12, 1fr)` collapses to `1fr` in subscription/homepage module CSS.
- **Sidebar**: no permanent sidebar; overlays handle search/menu.
- **Hero layout**: editorial lead remains text-first; photography modules stack below on smaller screens.

### Image Behavior
- **Strategy**: photography carries article/promo meaning; image modules crop via Brightspot asset transforms.
- **Max-width**: `100%` patterns present in common CSS.
- **Aspect ratio handling**: server-side image crops and module-specific wrappers, not a single universal aspect-ratio token.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

Primary CTA:

```html
<a class="primary-button buttonAnimationStyles" href="#">
  <span>Subscribe</span>
  <svg aria-hidden="true"><use href="#icon-arrow-right"></use></svg>
</a>
```

| Property | Value |
|---|---|
| Background | `#7EF473` default, `#71DC68` non-animated hover |
| Text | `#212427` |
| Radius | `15px` |
| Padding | `13px 24px`; animated hover expands left side to `55px` |
| Focus/active | background `#0E3E1B`, text `#FFFFFF`, border `#FFFFFF` |
| Disabled | background `#DCD5CE`, text `#898888` |

Secondary CTA:

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#212427` |
| Border | `#212427`; disabled border `#898888` |
| Active background | `#F2F2F2` |
| Focus background | `#323232`, text `#FFFFFF` |

### Badges

Badges and metadata behave like editorial labels more than pills. Use 12px or 14px, uppercase where action/category needs emphasis, and keep background minimal unless status semantics are needed.

| Pattern | Spec |
|---|---|
| Article label | 12px/700 uppercase, #212427 |
| Date/meta | 12px/400 or 14px/400, gray family |
| Semantic status | #DCF9E3/#21BF61 or #FCE1DC/#D82216 only when status is real |

### Cards & Containers

Article/promo cards are image-led. The content card may sit on top of photography with rounded corners, but BCG avoids generic "three feature cards with colored icons." Keep the photography meaningful and the text hierarchy editorial.

| Property | Value |
|---|---|
| Surface | `#FFFFFF` or warm neutral `#F1EEEA` |
| Radius | 15px/20px for cards; 70px for selected large image treatments |
| Border | minimal; use #DCD5CE only as a quiet hairline |
| Shadow | restrained; stronger shadow belongs to overlays/header/search containers |
| Hover | content/action change, not playful transform bounce |

### Navigation

```html
<header class="Page-header">
  <div class="Page-headerMenuLeft">...</div>
  <div class="Page-headerMenuRight">...</div>
</header>
```

| State | Spec |
|---|---|
| Default | fixed top, transparent page shell, pill clusters |
| Cluster surface | translucent white + `backdrop-filter: blur(20px)` |
| Mega menu open | full width #FFFFFF, radius reset to 0 in open state |
| Scroll | opacity/visibility changes over ~333ms |
| Login utility | underlined text utility, not a filled button |

### Inputs & Forms

Search/alumni form CSS reveals the form system.

| Property | Value |
|---|---|
| Input border | `#696969` / gray family |
| Form surface | `hsla(0,0%,94.9%,0.5)` equivalent light gray translucency |
| Form radius | `30px` |
| Input padding | `12px` |
| Advanced search button | padding `14px 32px`, radius `15px` |
| Sort/options surface | `#0E3E1B` |

### Hero Section

Hero should be a confident editorial lead, not a center-aligned SaaS promise block. Use the H1 as a brand-level statement, let the navigation float above it, and allow article/promo modules to bring in photography and specificity below.

| Property | Value |
|---|---|
| H1 | Henderson BCG Sans, up to 96px, weight 300, line-height 100% |
| Background | #FFFFFF |
| CTA | #7EF473, #212427 text, radius 15px |
| Follow-on modules | photography cards, topic/industry indexes, subscription band |

### 13-2. Named Variants

**button-primary-animated**

| Property | Value |
|---|---|
| Default | #7EF473 bg, #212427 text |
| Hover | padding-left expands to 55px; arrow animation runs 0.35s |
| Focus | #0E3E1B bg, #FFFFFF text, #FFFFFF border |
| Active | #0E3E1B bg, #FFFFFF text |
| Disabled | #DCD5CE bg, #898888 text |

**button-secondary-outline**

| Property | Value |
|---|---|
| Default | #FFFFFF bg, #212427 text, #212427 border |
| Active | #F2F2F2 bg |
| Focus | #323232 bg, #FFFFFF text |
| Disabled | #FFFFFF bg, #898888 text and border |

**floating-header-pill**

| Property | Value |
|---|---|
| Surface | translucent white |
| Effect | `backdrop-filter: blur(20px)` |
| Shape | `var(--headerRadius)` |
| State | radius/shadow/blur removed or changed when mega menu opens |

### 13-3. Signature Micro-Specs

```yaml
cta-arrow-padding-choreography:
  description: "Primary CTA does not just change color; it reallocates space for directional motion."
  technique: "transition: padding var(--cta-button-animation-timing); --cta-button-animation-timing: 0.35s; --buttonPaddingInline: 24px; --cta-button-expanded-padding: 55px"
  applied_to: ["{component.button-primary-animated}", ".buttonAnimationStyles"]
  visual_signature: "the button opens a visible lane for the arrow before asking the reader to move forward"

blurred-header-pill-clusters:
  description: "Global navigation is split into floating translucent pill clusters instead of one flat corporate bar."
  technique: "translucent white surface + backdrop-filter: blur(20px) + var(--headerRadius) + var(--box-shadow); mega menu open state returns to full #FFFFFF surface"
  applied_to: ["{component.floating-header-pill}", ".Page-headerMenuLeft", ".Page-headerMenuRight"]
  visual_signature: "a strategy-site header that behaves like a glass nameplate hovering above editorial content"

lime-action-deepgreen-focus-split:
  description: "Action lime and institutional green are deliberately separated into default action vs focus/active authority."
  technique: "default CTA #7EF473 /* {colors.accent-primary} */; hover #71DC68 /* {colors.accent-hover} */; focus/active #0E3E1B /* {colors.green-deep} */ with #FFFFFF text/border"
  applied_to: ["{component.button-primary-animated}", "{component.button-secondary-outline}"]
  visual_signature: "BCG stays editorial and serious until the exact action moment flashes bright lime"

henderson-light-display-heavy-utility:
  description: "Large thought-leadership type stays light while small labels and controls become firm."
  technique: "H1 up to 96px / font-weight 300 / line-height 100%; body 16px / 400 / 140%; utility and CTA 12px / 700 / uppercase; weight 500 absent"
  applied_to: ["{typography.ladder.hero-h1}", "{typography.ladder.utility}", "CTA labels", "article metadata"]
  visual_signature: "strategy-report hierarchy where the big thesis whispers and the execution label stamps"

warm-report-surface-hairline:
  description: "Warm neutral report surfaces replace generic gray while hairlines stay quiet and paper-like."
  technique: "#F1EEEA /* {colors.surface-warm} */ editorial background; #DCD5CE /* {colors.hairline} */ disabled fill/divider; #212427 /* {colors.text-primary} */ primary ink instead of pure black"
  applied_to: ["subscription/report modules", "disabled button states", "subtle dividers"]
  visual_signature: "white-page consulting content gains the temperature of a printed research report, not a cold SaaS dashboard"
```

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* BCG — copy into your root stylesheet */
:root {
  /* Fonts */
  --bcg-font-family: "henderson-bcg-sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --bcg-font-family-serif: "henderson-bcg-serif", "Palatino Linotype", Palatino, Garamond, Georgia, serif;
  --bcg-font-weight-display: 300;
  --bcg-font-weight-normal: 400;
  --bcg-font-weight-bold: 700;

  /* Brand / actions */
  --bcg-color-accent-200: #7EF473;
  --bcg-color-accent-300: #71DC68;
  --bcg-color-green-200: #DCF9E3;
  --bcg-color-green-400: #21BF61;
  --bcg-color-green-500: #197A56;
  --bcg-color-green-700: #0E3E1B;

  /* Surfaces */
  --bcg-bg-page: #FFFFFF;
  --bcg-bg-warm: #F1EEEA;
  --bcg-bg-charcoal: #232326;
  --bcg-text: #212427;
  --bcg-text-muted: #696969;
  --bcg-border-warm: #DCD5CE;

  /* Key spacing */
  --bcg-button-padding-block: 13px;
  --bcg-button-padding-inline: 24px;
  --bcg-button-padding-expanded: 55px;
  --bcg-module-padding-large: 120px;

  /* Radius */
  --bcg-radius-button: 15px;
  --bcg-radius-card: 20px;
  --bcg-radius-form: 30px;
  --bcg-radius-large: 70px;
}

body {
  font-family: var(--bcg-font-family);
  font-weight: var(--bcg-font-weight-normal);
  color: var(--bcg-text);
  background: var(--bcg-bg-page);
}

.bcg-primary-button {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  border: 0;
  border-radius: var(--bcg-radius-button);
  padding: var(--bcg-button-padding-block) var(--bcg-button-padding-inline);
  background: var(--bcg-color-accent-200);
  color: var(--bcg-text);
  font-size: 12px;
  font-weight: 700;
  line-height: 100%;
  text-transform: uppercase;
  transition: padding 0.35s ease-in-out, background-color 0.2s ease;
}

.bcg-primary-button:hover {
  background: var(--bcg-color-accent-300);
  padding-left: var(--bcg-button-padding-expanded);
}

.bcg-primary-button:focus,
.bcg-primary-button:active {
  background: var(--bcg-color-green-700);
  color: #FFFFFF;
  outline: 1px solid #FFFFFF;
}

.bcg-floating-header-cluster {
  background: rgba(255, 255, 255, 0.75);
  border-radius: var(--bcg-radius-button);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.12), 0 2px 6px rgba(0, 0, 0, 0.08);
  backdrop-filter: blur(20px);
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand/action primary | `{colors.accent-primary}` | `#7EF473` |
| Action hover | `{colors.accent-hover}` | `#71DC68` |
| Institutional green | `{colors.green-deep}` | `#0E3E1B` |
| Background | `{colors.surface-base}` | `#FFFFFF` |
| Warm background | `{colors.surface-warm}` | `#F1EEEA` |
| Text primary | `{colors.text-primary}` | `#212427` |
| Text muted | `--gray-500` | `#696969` |
| Border / disabled fill | `{colors.hairline}` | `#DCD5CE` |
| Success | `--success-400` | `#21BF61` |
| Error | `--alert-400` | `#D82216` |

### Example Component Prompts

#### Hero Section

```text
BCG 스타일의 전략 리포트형 히어로를 만들어줘.
- 배경: #FFFFFF
- H1: henderson-bcg-sans, 96px desktop, weight 300, line-height 100%, tracking 0
- 본문: #212427, 16px, weight 400, line-height 140%
- CTA: #7EF473 배경, #212427 텍스트, radius 15px, padding 13px 24px
- hover: CTA left padding을 55px로 늘리고 arrow를 0.35s ease-in-out으로 이동
- 톤: 컨설팅 리포트 편집면처럼 차분하고 권위 있게, SaaS식 보라 그라디언트 금지
```

#### Card Component

```text
BCG 스타일 기사/인사이트 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF 또는 #F1EEEA
- 제목: henderson-bcg-sans, 24px, weight 400, line-height 120%
- 메타: 12px, weight 700, uppercase
- border는 최소화하고 필요 시 #DCD5CE hairline만 사용
- radius: 15px 또는 20px
- 이미지는 장식이 아니라 실제 기사/산업 맥락을 보여주는 photography로 배치
```

#### Navigation

```text
BCG 스타일 상단 네비게이션을 만들어줘.
- fixed top header, 좌측 menu/logo cluster와 우측 utility cluster 분리
- cluster surface: translucent white, backdrop-filter blur(20px), radius 15px, subtle shadow
- mega menu open state에서는 #FFFFFF full-width surface로 전환
- login은 filled button이 아니라 underlined utility text
- primary action이 필요할 때만 #7EF473 CTA 사용
```

### Iteration Guide

- **색상 변경 시**: #7EF473는 CTA/action에만 둔다. 브랜드 전체를 라임으로 칠하지 않는다.
- **폰트 변경 시**: Henderson BCG Sans가 없으면 Inter 300/400/700으로 대체하되 weight 500은 넣지 않는다.
- **여백 조정 시**: 큰 섹션은 96px~120px, 버튼은 13px/24px, hover 확장은 55px 패턴을 유지한다.
- **새 컴포넌트 추가 시**: 먼저 editorial module인지, action control인지 구분한다. 둘의 밀도와 weight가 다르다.
- **상태 추가 시**: focus/active는 #0E3E1B + #FFFFFF 조합을 사용해 접근성 신호를 분명히 한다.
- **사진 사용 시**: 추상 SVG 일러스트 대신 실제 산업/리서치 맥락이 드러나는 사진을 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #7EF473 as the primary action surface and keep it rare.
- Use #0E3E1B for institutional green fields, focus/active states, and subscription-like heavy bands.
- Set large editorial headings in Henderson BCG Sans at weight 300.
- Keep body text #212427, not brittle pure black.
- Build major homepage modules on a 12-column grid at desktop.
- Use translucent pill header clusters with blur(20px) when reproducing the global nav.
- Preserve button state engineering: default, hover, focus, active, disabled.
- Let photography and article hierarchy carry cards; avoid decorative icon-card grids.

### ❌ DON'T

- 배경을 `#F7F7F7` 또는 generic off-white로 두지 말 것 — 기본 표면은 `#FFFFFF`, warm editorial surface는 `#F1EEEA` 사용.
- 본문 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#212427` 사용.
- Primary CTA를 `#0E3E1B` 배경으로 두지 말 것 — 기본 action은 `#7EF473`, focus/active만 `#0E3E1B` 사용.
- CTA hover를 같은 `#7EF473`로 정지시키지 말 것 — non-animated hover는 `#71DC68`, animated hover는 padding choreography 사용.
- Disabled button을 `#EEEEEE`로 임의 처리하지 말 것 — 대신 `#DCD5CE` background와 `#898888` text 사용.
- BCG를 `#006400` 같은 일반 dark green 브랜드로 재해석하지 말 것 — 실제 deep green은 `#0E3E1B`.
- Warm report backgrounds를 `#FAFAFA`로 평탄화하지 말 것 — 실제 warm neutral anchor는 `#F1EEEA`.
- body에 `font-weight: 500` 사용 금지 — sampled system은 300/400/700 대비가 핵심이다.
- 모든 카드를 shadow-heavy SaaS card로 만들지 말 것 — BCG 카드는 photography/content hierarchy가 먼저다.
- Header를 평평한 64px white bar로 만들지 말 것 — floating pill cluster + blur(20px)가 시그니처다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No purple-blue AI gradient** — BCG's authority is not made with `linear-gradient(135deg, #667eea, #764ba2)`.
- **No second action color** — #7EF473 carries primary action; red/yellow/social colors are semantic or external, not brand accents.
- **No generic medium weight** — weight 500 is absent from the sampled typographic rhythm.
- **No all-green wash** — deep green exists, but the page is not a dark-green poster.
- **No decorative icon grid as default** — industry and article modules are content/photo-led.
- **No playful bounce motion** — CTA motion is directional padding/arrow choreography, not elastic transform.
- **No permanent dashboard sidebar** — navigation is top/floating/overlay-driven.
- **No heavy chrome on every card** — borders and shadows are restrained; surface and image do the work.
- **No pure black reading tone** — #212427 replaces #000000 for primary ink.
- Magazine cover photography full-bleed hero: absent. The first viewport is text-led editorial, not a poster.
- Decorative pull-quote ribbons or sidebar columns on the front page: zero. The editorial spine stays single-rail.
- Sponsored ad panel masquerading as a column: never. Subscription/lead bands stay distinctly marked.
- Glossy lifestyle photo grid as feature index: absent. Article cards use real industry imagery only.
- Second editorial accent (yellow highlighter, red strikethrough): none. Lime is the only column-margin pen this magazine carries.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual / REQUIRED -->

- **Cookie overlay in screenshot** — the cached hero screenshot is partially obscured by the privacy consent modal. Visual interpretation of the first viewport uses HTML/CSS facts plus visible underlying modules, not a clean hero capture.
- **Phase1 reused** — HTML/CSS/JSON were reused from the existing `insane-design/bcg` cache dated April 2026. This file does not claim a fresh May 3, 2026 crawl.
- **Homepage only** — analysis centers on `https://www.bcg.com` homepage. Careers, article detail pages, client login, search flows, and gated subscription/account states may use additional patterns.
- **Motion logic incomplete** — CSS exposes 0.35s CTA animation and header transitions, but JavaScript scroll/menu choreography was not fully traced.
- **Exact font metrics unavailable** — Henderson BCG font files were identified through CSS family names, but font binary metrics and licensing details were not inspected.
- **Logo/social colors filtered conceptually** — social media hex values exist in CSS but are not treated as BCG brand colors.
- **Form validation states partially observed** — search/alumni form styling surfaced input, form radius, and sort surface tokens; full validation/loading/error UI was not visited.
- **Dark theme mapping not complete** — `#232326`, `#0E3E1B`, and white-on-dark contexts exist, but a full dark-mode token map was not proven from the homepage sample.
