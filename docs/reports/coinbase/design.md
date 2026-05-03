---
schema_version: 3.2
slug: coinbase
service_name: Coinbase
site_url: https://www.coinbase.com
fetched_at: 2026-04-14T01:23:00+09:00
default_theme: light
brand_color: "#0052FF"
primary_font: CoinbaseSans
font_weight_normal: 400
token_prefix: cds

bold_direction: Trust Utility
aesthetic_category: Refined SaaS
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: landing-utility
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Coinbase Design System tokens are present in CSS as --cds-* font variables, --lightColor-* semantic colors, spacing, radius, shadow, and interactable state variables."

colors:
  primary: "#0052FF"
  bg-page: "#FFFFFF"
  text-primary: "#0A0B0D"
  text-muted: "#5B616E"
  line-subtle: "rgba(91,97,110,0.2)"
  bg-secondary: "#EEF0F3"
  positive: "#098551"
  negative: "#CF202F"
  dark-bg: "#0A0B0D"
  dark-primary: "#578BFA"

typography:
  display: "CoinbaseDisplay"
  body: "CoinbaseSans"
  text: "CoinbaseText"
  mono: "CoinbaseMono"
  ladder:
    - { token: display1, size: "4rem", weight: 400, line_height: "4.5rem", tracking: "0" }
    - { token: display2, size: "3rem", weight: 400, line_height: "3.5rem", tracking: "0" }
    - { token: display3, size: "2.5rem", weight: 400, line_height: "3rem", tracking: "0" }
    - { token: title1, size: "1.75rem", weight: 600, line_height: "2.25rem", tracking: "0" }
    - { token: title3, size: "1.25rem", weight: 600, line_height: "1.75rem", tracking: "0" }
    - { token: body, size: "1rem", weight: 400, line_height: "1.5rem", tracking: "0" }
    - { token: label1, size: "0.875rem", weight: 600, line_height: "1.25rem", tracking: "0" }
  weights_used: [400, 500, 600, 700]
  weights_absent: [200, 800, 900]

components:
  button-primary: { bg: "{colors.primary}", color: "{colors.bg-page}", radius: "40px", min_width: "100px", state: "hover rgba(0,72,224,0.88), pressed rgba(0,67,209,0.82)" }
  button-secondary: { bg: "{colors.bg-secondary}", color: "{colors.text-primary}", radius: "40px", min_width: "100px" }
  email-input: { bg: "{colors.bg-page}", border: "1px solid rgba(91,97,110,0.2)", radius: "8px", height: "60px" }
  nav-icon-button: { bg: "{colors.bg-secondary}", color: "{colors.text-primary}", radius: "100000px", size: "44px" }
  market-card: { bg: "{colors.bg-page}", border: "1px solid rgba(91,97,110,0.2)", radius: "16px", shadow: "none by default" }
---

# DESIGN.md - Coinbase

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Coinbase is built as a financial utility that wants to feel obvious before it feels exciting. The homepage is closer to an airport check-in desk for money than a crypto exchange floor: a hard white floor, direct black type, numbered decisions, and one unmistakable blue lane. The page does not perform decentralization as spectacle. It makes finance look like something you can pass through with documents in order.

The hero is the whole argument. A large app mockup sits on the left inside a contained blue field, while the right side says "The future of finance is here." in oversized black type. It behaves like a bank lobby with a live trading terminal under glass: the product screenshot supplies the chart, balance, categories, and proof, while the headline stays almost bureaucratically plain. The page does not need a second poster because the app mockup is the receipt.

Coinbase's color contract is narrow. `#0052FF` (`{colors.primary}`) is the single security-lane color: sign up here, move forward here, this is the path. `#FFFFFF` (`{colors.bg-page}`) is the fluorescent institutional surface, `#0A0B0D` (`{colors.text-primary}`) is ink-black policy authority, and `#5B616E` (`{colors.text-muted}`) is the small-print voice. There is no second brand color. Green `#098551` and red `#CF202F` are allowed only as market state, like digits on an exchange board, not as decoration.

The component language is rounded but not cute. Pills use 40px and token radius `--borderRadius-1000` for action affordance; content containers sit closer to 16px; small UI pieces use 4px and 8px. That hierarchy reads like a security checkpoint: round gates for movement, rectangular forms for verification, bordered cards for evidence. If everything becomes one radius, Coinbase loses the distinction between "tap this now" and "read this safely."

Depth is also rationed. Chrome stays flat, bordered, and white; the product mockup carries the drama. It is the inverse of a shadow-heavy SaaS landing page: the interface does not cast atmosphere around every card, it puts the financial instrument in a blue display case and lets the rest of the page behave like a clean counter. Shadow only belongs where it helps an overlay or mockup feel touchable.

Motion is utility-grade. CSS contains many `0.1s`, `0.2s`, `150ms`, and `300ms` transitions, plus interactable hover/pressed opacity states. The page should feel responsive, not animated. There is no crypto-neon performance, no nightclub gradient mesh, no token confetti. The trust move is speed plus restraint.

비유로 풀자면 Coinbase는 금융 도구함을 한 면에 펼쳐놓은 작업판이다. 헤더는 카운터 위에 일렬로 놓인 라벨된 스위치들 — 카테고리/검색/언어/로그인이 각자의 토글, blue pill CTA는 그 도구함에서 단 하나만 켜져 있는 메인 스위치, 신호등 하나뿐인 버튼판이다. 좌측 app mockup은 도구함 옆에 붙은 디지털 계기판처럼 차트와 잔고 수치를 그대로 보여주고, 이메일 input은 작업판 위에 놓인 raw form blank다. 모든 컨트롤이 "한 번 눌러보면 즉시 결과가 나오는 도구"의 인상으로 통일되어 있고, 장식 스위치나 테마 패널 같은 군더더기 도구는 등장하지 않는다.

### Key Characteristics

- Single canonical brand blue: `#0052FF`, not a rotating crypto palette.
- White page surface with black display type: `#FFFFFF` + `#0A0B0D`.
- Two-column hero: product mockup as proof, headline and email capture as action.
- Coinbase font family split: CoinbaseDisplay for large statements, CoinbaseSans/Text for UI and prose.
- 8px spacing base with named `--space-*` steps from 0px to 80px.
- Rounded action controls: primary CTAs and icon buttons are pill or circular.
- Semantic state colors are present but controlled: positive `#098551`, negative `#CF202F`, warning orange.
- Header is product-navigation dense, not marketing minimal: categories, search, globe, sign in, sign up.
- Shadows are mostly absent on chrome; depth comes from mockup layering and surface contrast.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Trust Utility
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **large product mockup plus single-blue signup path**으로 기억된다.
> **Code Complexity**: high — tokenized CDS variables, interactable state maps, responsive nav, app mockup composition, and multiple semantic color ramps.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Coinbase처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Coinbase typography split */
:root {
  --cb-font-display: CoinbaseDisplay, CoinbaseSans, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --cb-font-body: CoinbaseSans, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
body {
  font-family: var(--cb-font-body);
  font-weight: 400;
}
h1 {
  font-family: var(--cb-font-display);
  font-size: 4rem;
  line-height: 4.5rem;
  font-weight: 400;
  letter-spacing: 0;
}

/* 2. White trust surface + black authority text */
:root {
  --cb-bg: #FFFFFF;
  --cb-fg: #0A0B0D;
  --cb-muted: #5B616E;
}
body {
  background: var(--cb-bg);
  color: var(--cb-fg);
}

/* 3. One blue, pill action */
:root { --cb-brand: #0052FF; }
.cb-button-primary {
  background: var(--cb-brand);
  color: #FFFFFF;
  border-radius: 40px;
  min-width: 100px;
  padding: 0 24px;
  height: 56px;
}
```

**절대 하지 말아야 할 것 하나**: Coinbase를 "crypto neon"으로 만들지 말 것. `#0052FF` 하나와 흰 표면이 브랜드의 신뢰감을 만든다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.coinbase.com` |
| Fetched | 2026-04-14T01:23:00+09:00 |
| Extractor | reused phase1: curl/HTML/CSS/screenshot artifacts |
| HTML size | 917691 bytes |
| CSS files | 10 files plus `_inline.css`, approx. 541567 bytes |
| Token prefix | `cds` plus `lightColor-*`, `darkColor-*`, `space-*`, `borderRadius-*` |
| Method | Phase1 JSON + specified CSS/HTML/screenshot artifacts; Step 6 HTML render skipped per request |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React/Next-style SSR bundle with styled-components class output and Coinbase Design System tokens.
- **Design system**: Coinbase Design System (CDS) — font variables use `--cds-font-*`; token sets include `--lightColor-*`, `--darkColor-*`, `--space-*`, `--borderRadius-*`, and `--shadow-*`.
- **CSS architecture**: tokenized semantic layer plus generated atomic/styled-component classes.
  ```css
  --light-blue60              0,82,255 raw blue ramp step
  --lightColor-bgPrimary      rgb(0,82,255) semantic surface/action
  --color-bgPrimary           active theme alias
  --interactable-hovered-*    component state map
  ```
- **Class naming**: generated styled-components and utility fragments such as `flex-ff5rfy6`, `fgPrimary-*`, `height-*`, `cds-Button`, `cds-Interactable`.
- **Default theme**: light (page background `#FFFFFF`, text `#0A0B0D`).
- **Font loading**: Coinbase proprietary web fonts: CoinbaseDisplay, CoinbaseSans, CoinbaseText, CoinbaseMono, CoinbaseCondensed, CoinbaseIcons.
- **Canonical anchor**: homepage hero, header nav, email signup form, and market/app product mockup.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `CoinbaseDisplay` (proprietary Coinbase brand font)
- **Body/UI font**: `CoinbaseSans` and `CoinbaseText`
- **Code font**: `CoinbaseMono`
- **Icon font**: `CoinbaseIcons`
- **Weight normal / bold**: `400` / `600` for the core UI ladder; `700` appears in some content; `500` appears in button/link states.

```css
:root {
  --cds-font-fallback: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto",
    "Helvetica", "Arial", sans-serif, "Apple Color Emoji", "Segoe UI Emoji",
    "Segoe UI Symbol";
  --cds-font-display: CoinbaseDisplay, var(--cds-font-fallback);
  --cds-font-sans: CoinbaseSans, var(--cds-font-fallback);
  --cds-font-text: CoinbaseText, var(--cds-font-fallback);
  --cds-font-mono: CoinbaseMono, var(--cds-font-fallback);
}
body {
  font-family: var(--cds-font-sans);
  font-weight: 400;
}
```

### Note on Font Substitutes

- **CoinbaseDisplay** — if unavailable, use `Inter` or `SF Pro Display` at weight 400 with no negative tracking. Do not tighten the headline by default; the observed CDS ladder uses `letter-spacing: 0` or `normal`, not Apple-like compression.
- **CoinbaseSans** — use `Inter` at 400/600, line-height 1.5 for body and 1.25 for labels. Keep button labels at 600 when the control must read as product UI.
- **CoinbaseText** — use `Inter` or system sans at 400 for longer legal/prose content. The fallback should preserve a neutral fintech tone, not editorial serif contrast.
- **CoinbaseMono** — use `ui-monospace` only for numbers/code-like readouts. Do not replace the whole UI with mono; market values are proof elements, not the brand voice.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `display1` | `4rem` | `400` | `4.5rem` | `0` |
| `display2` | `3rem` | `400` | `3.5rem` | `0` |
| `display3` | `2.5rem` | `400` | `3rem` | `0` |
| `title1` | `1.75rem` | `600` | `2.25rem` | `0` |
| `title2` | `1.75rem` | `400` | `2.25rem` | `0` |
| `title3` | `1.25rem` | `600` | `1.75rem` | `0` |
| `title4` | `1.25rem` | `400` | `1.75rem` | `0` |
| `headline` | `1rem` | `600` | `1.5rem` | `0` |
| `body` | `1rem` | `400` | `1.5rem` | `0` |
| `label1` | `0.875rem` | `600` | `1.25rem` | `0` |
| `label2` | `0.875rem` | `400` | `1.25rem` | `0` |
| `caption` | `0.8125rem` | `600` | `1rem` | `0` |
| `legal` | `0.8125rem` | `400` | `1rem` | `0` |

> ⚠️ Key insight: the headline is large but not heavy. Coinbase uses scale and line-height, not 800-weight bravado.

### Principles

1. Display sizes are calm: `display1` is 64px equivalent at weight 400. The authority comes from size and whitespace, not boldness.
2. Body text sits at 16px / 24px. This keeps financial copy readable and avoids the tiny SaaS-caption trap.
3. Labels and nav items use 600 when they behave like UI. That gives dense navigation enough structure without adding borders.
4. Letter-spacing is deliberately neutral. The CSS shows `0`, `normal`, and small positive values for some labels; no heavy negative tracking identity.
5. Coinbase separates font roles: Display for statements, Sans for interface, Text for prose/legal, Mono for technical/market contexts.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (light blue)

| Token | Hex / RGB |
|---|---|
| `--light-blue0` | `rgb(245,248,255)` |
| `--light-blue5` | `rgb(211,225,255)` |
| `--light-blue10` | `rgb(176,202,255)` |
| `--light-blue20` | `rgb(115,162,255)` |
| `--light-blue40` | `rgb(38,110,255)` |
| `--light-blue50` | `rgb(16,94,255)` |
| `--light-blue60` | `rgb(0,82,255)` / `#0052FF` |
| `--light-blue70` | `rgb(0,75,235)` |
| `--light-blue80` | `rgb(0,62,193)` |
| `--light-blue90` | `rgb(0,41,130)` |
| `--light-blue100` | `rgb(0,24,77)` |

### 06-2. Brand Dark Variant

| Token | Hex / RGB |
|---|---|
| `--dark-blue0` | `rgb(0,16,51)` |
| `--dark-blue20` | `rgb(5,59,177)` |
| `--dark-blue40` | `rgb(19,84,225)` |
| `--dark-blue60` | `rgb(55,115,245)` |
| `--dark-blue70` | `rgb(87,139,250)` / `#578BFA` |
| `--dark-blue90` | `rgb(185,207,255)` |
| `--dark-blue100` | `rgb(245,248,255)` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 | `#FFFFFF` | `#0A0B0D` |
| 5 | `#F7F8F9` | `#141519` |
| 10 | `#EEF0F3` | `#1E2025` |
| 20 | `#CED2DB` | `#32353D` |
| 40 | `#89909E` | `#89909E` |
| 60 | `#5B616E` | `#B1B7C3` |
| 80 | `#32353D` | `#EEF0F3` |
| 100 | `#0A0B0D` | `#FFFFFF` |

### 06-4. Accent Families

| Family | Key step | Hex / RGB |
|---|---|---|
| Positive green | `--light-green60` | `rgb(9,133,81)` / `#098551` |
| Negative red | `--light-red60` | `rgb(207,32,47)` / `#CF202F` |
| Warning orange | `--light-orange60` | `rgb(207,71,14)` |
| Teal | `--light-teal60` | `rgb(0,123,179)` |
| Indigo | `--light-indigo60` | `rgb(66,91,233)` |
| Purple | `--light-purple60` | `rgb(138,85,233)` |

### 06-5. Semantic

| Token | Hex / RGB | Usage |
|---|---|---|
| `--lightColor-bg` | `#FFFFFF` | page and elevation base |
| `--lightColor-fg` | `#0A0B0D` | primary text |
| `--lightColor-fgMuted` | `#5B616E` | secondary copy, legal text |
| `--lightColor-bgPrimary` | `#0052FF` | primary action surface |
| `--lightColor-fgPrimary` | `#0052FF` | brand links and active affordances |
| `--lightColor-bgPrimaryWash` | `#F5F8FF` | soft blue wash |
| `--lightColor-bgSecondary` | `#EEF0F3` | secondary buttons/chips |
| `--lightColor-bgLine` | `rgba(91,97,110,0.2)` | subtle borders and dividers |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--color-bg` | `rgb(255,255,255)` | active theme page/surface |
| `--color-fg` | `rgb(10,11,13)` | active theme primary text |
| `--color-fgMuted` | `rgb(91,97,110)` | muted text |
| `--color-bgPrimary` | `rgb(0,82,255)` | active primary action |
| `--color-bgSecondary` | `rgb(238,240,243)` | secondary surfaces |
| `--color-bgLine` | `rgba(91,97,110,0.2)` | hairline |

### 06-7. Dominant Colors (actual CSS frequency)

| Hex | Frequency | Role |
|---|---:|---|
| `#FFFFFF` / `#fff` | 175+ | surface and inverse text |
| `#D8D8D8` | 120 | neutral/UI line noise, cookie/vendor UI included |
| `#000000` / `#000` | 84+ | black text/icons, some embedded assets |
| `#0A0B0D` | 72+ | CDS primary text / inverse background |
| `#0052FF` | 70 | canonical Coinbase blue |
| `#3860BE` | 56 | secondary blue, likely embedded/product or vendor contexts |
| `#E2E2E2` | 48 | neutral line/surface |
| `#C7C5C7` | 36 | neutral shadow/vendor UI |

### 06-8. Color Stories

**`{colors.primary}` (`#0052FF`)** — The only brand color that should dominate. It appears as `--light-blue60`, `--lightColor-bgPrimary`, `--lightColor-fgPrimary`, and `--color-bgPrimary`. Use it for signup, active states, brand icons, and chart proof points.

**`{colors.bg-page}` (`#FFFFFF`)** — The trust floor. Coinbase lets white carry most of the homepage because financial products need clarity before mood. Do not tint the entire page blue.

**`{colors.text-primary}` (`#0A0B0D`)** — The authority ink. It is close to black but named through CDS rather than raw `#000000`. Use it for hero type, nav text, and market values.

**`{colors.text-muted}` (`#5B616E`)** — The compliance voice. It belongs to support text, legal notes, and secondary explanations. Keep it readable; do not drop muted copy into low-contrast pale gray.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--space-0` | `0px` | reset, edge alignment |
| `--space-0_25` | `2px` | tiny optical adjustment |
| `--space-0_5` | `4px` | icon/text micro gaps |
| `--space-0_75` | `6px` | compact inner gaps |
| `--space-1` | `8px` | base unit |
| `--space-1_5` | `12px` | compact control padding |
| `--space-2` | `16px` | component padding/gap |
| `--space-3` | `24px` | form and card rhythm |
| `--space-4` | `32px` | section grouping |
| `--space-5` | `40px` | large component separation |
| `--space-6` | `48px` | hero inner rhythm |
| `--space-8` | `64px` | major vertical air |
| `--space-10` | `80px` | large section breathing room |

**주요 alias**:
- `--space-1` -> 8px (base)
- `--space-2` -> 16px (card/input internal rhythm)
- `--space-5` -> 40px (pill radius and larger component spacing echo)

### Whitespace Philosophy

Coinbase spaces like a product interface expanded into a homepage. The header is dense, because the product surface is broad: Cryptocurrencies, Individuals, Businesses, Institutions, Developers, Company, search, language, sign in, sign up. The hero then opens up with large left/right blocks so the financial promise feels understandable rather than crowded.

Whitespace is not luxury here; it is risk reduction. Around the email form and headline, the space prevents the action from feeling like a promotion. Below the hero, market modules can become denser, but the top of the page must stay simple enough for a first-time user to trust the path.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--borderRadius-0` | `0px` | flat resets, edge joins |
| `--borderRadius-100` | `4px` | small UI controls, micro surfaces |
| `--borderRadius-200` | `8px` | input fields, small cards |
| `--borderRadius-300` | `12px` | medium containers |
| `--borderRadius-400` | `16px` | product cards / bookend radius |
| `--borderRadius-500` | `24px` | large panels |
| `--borderRadius-700` | `40px` | pill buttons |
| `--borderRadius-1000` | `100000px` | full pill / circular buttons |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| `--shadow-elevation1` | `0px 8px 12px rgba(0, 0, 0, 0.12)` | elevated menus/cards when needed |
| `--shadow-elevation2` | `0px 8px 24px rgba(0, 0, 0, 0.12)` | stronger overlay depth |
| observed vendor/product shadows | `0px 2px 10px -3px #999`; `0px 0px 12px 2px #c7c5c7`; `-3px -3px 5px -2px #c7c5c7` | mostly non-core/cookie/product-artifact contexts |
| chrome default | `none` | primary Coinbase homepage chrome stays flat |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| quick feedback | `0.1s ease` | small UI state changes |
| standard feedback | `0.2s ease` / `all 0.2s ease-in 0s` | buttons, hoverable controls |
| medium feedback | `all 150ms ease-in 0s` | interactable transitions |
| layout width | `width 0.3s ease-in-out` | expandable/animated widths |
| slow decorative | `1s ease`, `2s ease` | non-critical visual transitions |
| interactable opacity | hover `0.88`, pressed `0.82` | CDS button/menu state system |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: observed values include `575px`, `700px`, `900px`, and `calc(100% - 32px)`; homepage hero behaves as a wide two-column layout within the viewport.
- **Grid type**: Flexbox-heavy generated utility classes (`flex-ff5rfy6`) with component-specific wrappers; CSS Grid may appear in modules but the hero is primarily flex/composition.
- **Column count**: hero is 2-column on desktop: left product image block, right headline/form block.
- **Gutter**: practical rhythm uses 32px-64px on large areas, 16px/24px inside components.

### Hero

- **🆕 Pattern Summary**: `~80vh visible hero + blue product mockup block + right-aligned text/form action`.
- Layout: desktop two-column; app mockup left, copy/form right.
- Background: global white surface with a saturated blue product-art panel.
- **🆕 Background Treatment**: solid white page plus gradient-like app mockup field using Coinbase blue; no page-wide gradient mesh.
- H1: `4rem` / weight `400` / tracking `0`.
- Max-width: right copy behaves around `575px`; form row extends to email input plus pill CTA.

### Section Rhythm

```css
section {
  padding: 64px 32px;
  max-width: 1200px;
}
.hero-copy {
  max-width: 575px;
}
.hero-form {
  gap: 16px;
}
```

### Card Patterns

- **Card background**: `#FFFFFF` or tokenized `--color-bg`.
- **Card border**: `1px solid rgba(91,97,110,0.2)` or neutral `#D8D8D8` in supporting UI.
- **Card radius**: 16px for product cards; 8px for form elements; 40px/100000px for actions.
- **Card padding**: 16px/24px typical; larger hero panels use 32px+.
- **Card shadow**: none by default; depth is reserved for overlays/product art.

### Navigation Structure

- **Type**: horizontal desktop nav with dense product categories.
- **Position**: top header, visually fixed to the top of the initial viewport in the screenshot.
- **Height**: approximately 68px.
- **Background**: `#FFFFFF`.
- **Border**: subtle bottom divider around `#D8D8D8` / line token.

### Content Width

- **Prose max-width**: 575px for hero copy.
- **Container max-width**: 1200px-ish visual layout, with responsive `calc(100% - 32px)` constraints in CSS.
- **Sidebar width**: N/A on homepage hero; mega-menu/dropdown content likely uses multi-column panels but was not fully interacted with.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Small mobile | `max-width: 425px` / `max-width: 500px` | narrow control and consent/modal handling |
| Mobile | `max-width: 576px` / `max-width: 600px` / `max-width: 640px` | mobile layout and button grouping |
| Tablet | `max-width: 767px` / `min-width: 768px` | common page layout shift point |
| Landscape tablet | `426px-896px landscape` | special modal/viewport handling |
| Desktop | `min-width: 550px` appears repeatedly | component expansion threshold |

### Touch Targets

- **Minimum tap size**: primary nav icon buttons appear around 44px; CTA buttons around 56px.
- **Button height (mobile)**: use 48px-56px for primary CTAs.
- **Input height (mobile)**: keep email/search inputs at 48px minimum; desktop hero email field appears closer to 60px.

### Collapsing Strategy

- **Navigation**: dense desktop nav should collapse into menu/search/action priority on smaller screens.
- **Grid columns**: hero should stack image and copy; do not squeeze the two-column composition below tablet width.
- **Sidebar**: no persistent sidebar on homepage.
- **Hero layout**: product mockup first or after headline depending conversion goal; preserve signup CTA near headline.

### Image Behavior

- **Strategy**: product screenshots are proof assets; keep them crisp and inspectable.
- **Max-width**: `100%`.
- **Aspect ratio handling**: use `object-fit: cover` for marketing imagery, but app mockups need contained composition to avoid cropping UI proof.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA**

| Property | Value |
|---|---|
| Background | `#0052FF` |
| Text | `#FFFFFF` |
| Radius | `40px` or `--borderRadius-1000` |
| Min width | `100px` observed inline |
| Height | 48px-56px depending context |
| Hover | `rgba(0,72,224,0.88)` |
| Pressed | `rgba(0,67,209,0.82)` |

```html
<button class="cds-Button cdx-button" data-variant="primary">
  <span>Sign up</span>
</button>
```

**Secondary CTA**

| Property | Value |
|---|---|
| Background | `#EEF0F3` or `rgb(247,247,247)` hover surface |
| Text | `#0A0B0D` |
| Radius | pill / `100000px` |
| Border | transparent |

### Badges

Badges and "New" labels should use compact 12px-14px label scale, 4px-999px radius depending context, and very restrained color. Use blue only when the badge is a primary product marker; use green only for positive financial movement.

### Cards & Containers

Cards are not the primary hero language. When used for markets or product rows, keep them white, bordered by `rgba(91,97,110,0.2)`, and avoid decorative shadows. Market proof cards should prioritize numbers, labels, and line charts over illustration.

### Navigation

Desktop nav contains Coinbase logo, product category links, search icon button, globe/language button, Sign in pill, and Sign up blue pill. Link text should be 14px-16px, weight 600 for primary categories, and black. The nav should not become transparent over media.

### Inputs & Forms

The hero email input is a high-trust form element, not a newsletter field. It uses white fill, subtle gray border, 8px radius, generous height, and muted placeholder text (`satoshi@nakamoto.com` in the captured homepage). Focus should use CDS focused border/shadow tokens, not a custom neon ring.

```html
<input
  id="email-form-input"
  name="email"
  type="email"
  autocomplete="email"
  placeholder="satoshi@nakamoto.com"
  aria-label="Email address"
/>
```

### Hero Section

The hero pairs proof and action. Product mockup left: a trading app screen with price, chart, categories, and small icon controls. Copy right: large display headline, short trust subcopy, email field, and Sign up CTA. The layout must retain the product-proof image; without it the headline becomes generic fintech copy.

### 13-2. Named Variants

**button-primary-blue-pill** — canonical signup CTA. `#0052FF` background, white text, 40px/full radius, min-width 100px, 48px-56px height.

**button-secondary-gray-pill** — Sign in and neutral header actions. Light gray surface, black text, pill radius, no visible border.

**nav-icon-circular** — search and language controls. Circular light gray button, centered CoinbaseIcons glyph, around 44px square.

**email-capture-input** — hero conversion input. White surface, 8px radius, subtle gray line, large horizontal padding, placeholder in muted gray.

**market-proof-card** — financial proof module. White surface, dark numeric type, blue/green chart accents, low or no shadow.

### 13-3. Signature Micro-Specs

```yaml
single-blue-trust-path:
  description: "Every primary conversion path converges on Coinbase blue."
  technique: "--light-blue60: 0,82,255; --lightColor-bgPrimary: rgb(0,82,255); --color-bgPrimary; primary CTA #0052FF with hover rgba(0,72,224,0.88) and pressed rgba(0,67,209,0.82)"
  applied_to: ["{component.button-primary}", "{component.market-card}", "{component.hero-section}"]
  visual_signature: "one unambiguous action color in a high-risk financial context"

radius-hierarchy-control-language:
  description: "Radius encodes role: verification fields, evidence cards, movement gates, and icon utilities each get a different curve."
  technique: "4px/8px for small UI and inputs; 16px for content cards; 40px and --borderRadius-1000 for CTAs; 100000px for circular nav icon controls"
  applied_to: ["{component.email-input}", "{component.market-card}", "{component.button-primary}", "{component.nav-icon-button}"]
  visual_signature: "friendly controls that still read as regulated product UI, not playful crypto decoration"

cds-interactable-opacity-states:
  description: "Feedback is handled through Coinbase Design System interactable state maps instead of ornamental motion."
  technique: "transition timings 0.1s/0.2s/150ms/300ms; hover opacity/background state rgba(0,72,224,0.88); pressed state rgba(0,67,209,0.82); disabled mapped to theme background/border tokens"
  applied_to: ["{component.button-primary}", "{component.button-secondary}", "{component.nav-icon-button}"]
  visual_signature: "fast product response that feels transactional and calm rather than animated"

display-400-authority:
  description: "The hero headline gets authority from scale and spacing, not weight."
  technique: "CoinbaseDisplay display1: font-size 4rem; line-height 4.5rem; font-weight 400; letter-spacing 0"
  applied_to: ["{component.hero-section}"]
  visual_signature: "institutional confidence without startup shouting"

flat-chrome-product-proof:
  description: "Page chrome remains flat so the app mockup and market proof carry the visual evidence."
  technique: "white surface #FFFFFF; border rgba(91,97,110,0.2); market-card shadow none by default; shadow tokens reserved for overlays (0px 8px 12px rgba(0,0,0,0.12), 0px 8px 24px rgba(0,0,0,0.12))"
  applied_to: ["{component.market-card}", "{component.email-input}", "{component.hero-section}"]
  visual_signature: "a clean counter around a blue product display case, with depth rationed to proof objects"
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | short declarative future/trust framing | "The future of finance is here." |
| Primary CTA | direct account/action language | "Sign up" |
| Secondary CTA | product task language | "Start trading", "Trade now", "Learn more" |
| Subheading | trust plus product scope in one sentence | "Trade crypto, stocks, and more on a platform you can trust." |
| Tone | regulated optimism: confident, direct, compliance-aware | legal disclosures sit close to claims |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Coinbase-inspired tokens */
:root {
  /* Fonts */
  --cb-font-display: CoinbaseDisplay, CoinbaseSans, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --cb-font-sans: CoinbaseSans, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --cb-font-text: CoinbaseText, CoinbaseSans, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --cb-font-mono: CoinbaseMono, ui-monospace, SFMono-Regular, Menlo, monospace;
  --cb-font-weight-normal: 400;
  --cb-font-weight-strong: 600;

  /* Brand */
  --cb-blue-0: #F5F8FF;
  --cb-blue-20: #73A2FF;
  --cb-blue-40: #266EFF;
  --cb-blue-60: #0052FF;
  --cb-blue-80: #003EC1;
  --cb-blue-100: #00184D;

  /* Surfaces */
  --cb-bg-page: #FFFFFF;
  --cb-bg-secondary: #EEF0F3;
  --cb-bg-dark: #0A0B0D;
  --cb-text: #0A0B0D;
  --cb-text-muted: #5B616E;
  --cb-line: rgba(91, 97, 110, 0.2);

  /* Semantic */
  --cb-positive: #098551;
  --cb-negative: #CF202F;
  --cb-warning: #CF470E;

  /* Spacing */
  --cb-space-1: 8px;
  --cb-space-2: 16px;
  --cb-space-3: 24px;
  --cb-space-4: 32px;
  --cb-space-6: 48px;
  --cb-space-8: 64px;

  /* Radius */
  --cb-radius-sm: 4px;
  --cb-radius-md: 8px;
  --cb-radius-card: 16px;
  --cb-radius-pill: 40px;
  --cb-radius-full: 100000px;

  /* Shadows */
  --cb-shadow-1: 0px 8px 12px rgba(0, 0, 0, 0.12);
  --cb-shadow-2: 0px 8px 24px rgba(0, 0, 0, 0.12);
}

.cb-page {
  background: var(--cb-bg-page);
  color: var(--cb-text);
  font-family: var(--cb-font-sans);
}

.cb-hero {
  display: flex;
  align-items: center;
  gap: var(--cb-space-6);
  max-width: 1200px;
  margin: 0 auto;
  padding: var(--cb-space-8) var(--cb-space-4);
}

.cb-hero h1 {
  font-family: var(--cb-font-display);
  font-size: 4rem;
  line-height: 4.5rem;
  font-weight: 400;
  letter-spacing: 0;
  margin: 0 0 var(--cb-space-3);
}

.cb-button-primary {
  min-width: 100px;
  height: 56px;
  padding: 0 24px;
  border: 0;
  border-radius: var(--cb-radius-pill);
  background: var(--cb-blue-60);
  color: #FFFFFF;
  font: 600 1rem/1.5rem var(--cb-font-sans);
  transition: background-color 150ms ease-in, opacity 150ms ease-in;
}
.cb-button-primary:hover { background: rgba(0, 72, 224, 0.88); }
.cb-button-primary:active { background: rgba(0, 67, 209, 0.82); }

.cb-email-input {
  height: 60px;
  min-width: 360px;
  padding: 0 18px;
  border: 1px solid var(--cb-line);
  border-radius: var(--cb-radius-md);
  background: #FFFFFF;
  color: var(--cb-text);
  font: 400 1rem/1.5rem var(--cb-font-sans);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js - Coinbase-inspired
module.exports = {
  theme: {
    extend: {
      colors: {
        coinbase: {
          blue: '#0052FF',
          blueWash: '#F5F8FF',
          bg: '#FFFFFF',
          fg: '#0A0B0D',
          muted: '#5B616E',
          line: 'rgba(91,97,110,0.2)',
          secondary: '#EEF0F3',
          positive: '#098551',
          negative: '#CF202F',
        },
      },
      fontFamily: {
        sans: ['CoinbaseSans', 'Inter', 'system-ui', 'sans-serif'],
        display: ['CoinbaseDisplay', 'CoinbaseSans', 'Inter', 'sans-serif'],
        mono: ['CoinbaseMono', 'ui-monospace', 'monospace'],
      },
      fontSize: {
        'cb-display1': ['4rem', { lineHeight: '4.5rem', fontWeight: '400', letterSpacing: '0' }],
        'cb-body': ['1rem', { lineHeight: '1.5rem', fontWeight: '400' }],
        'cb-label': ['0.875rem', { lineHeight: '1.25rem', fontWeight: '600' }],
      },
      borderRadius: {
        'cb-sm': '4px',
        'cb-md': '8px',
        'cb-card': '16px',
        'cb-pill': '40px',
        'cb-full': '100000px',
      },
      boxShadow: {
        'cb-1': '0px 8px 12px rgba(0, 0, 0, 0.12)',
        'cb-2': '0px 8px 24px rgba(0, 0, 0, 0.12)',
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
| Brand primary | `{colors.primary}` | `#0052FF` |
| Background | `{colors.bg-page}` | `#FFFFFF` |
| Text primary | `{colors.text-primary}` | `#0A0B0D` |
| Text muted | `{colors.text-muted}` | `#5B616E` |
| Border | `{colors.line-subtle}` | `rgba(91,97,110,0.2)` |
| Success | `{colors.positive}` | `#098551` |
| Error | `{colors.negative}` | `#CF202F` |

### Example Component Prompts

#### Hero Section

```text
Create a Coinbase-style fintech hero.
- Layout: desktop two-column, product app mockup on the left, headline and email signup on the right.
- Background: page #FFFFFF, product-art panel anchored in #0052FF.
- H1: CoinbaseDisplay or Inter fallback, 4rem, line-height 4.5rem, weight 400, tracking 0.
- Copy: #0A0B0D for headline, #5B616E for support text.
- CTA: blue #0052FF pill, white text, 40px radius, 56px height.
- Email input: white, 1px rgba(91,97,110,0.2), 8px radius, 60px height.
```

#### Card Component

```text
Create a Coinbase-style market proof card.
- Background #FFFFFF, border 1px solid rgba(91,97,110,0.2), radius 16px.
- Use CoinbaseSans/Inter, numeric value in #0A0B0D.
- Positive movement uses #098551; brand chart accent uses #0052FF.
- No decorative shadow by default; use shadow only for overlays.
```

#### Badge

```text
Create a Coinbase-style compact badge.
- Font: CoinbaseSans/Inter, 12-14px, weight 600.
- Radius: full pill.
- Default surface: #EEF0F3 with #0A0B0D text.
- Brand badge: #F5F8FF background with #0052FF text.
- Do not use multicolor crypto gradients.
```

#### Navigation

```text
Create a Coinbase-style desktop nav.
- White header, subtle bottom divider rgba(91,97,110,0.2), height about 68px.
- Left Coinbase mark, then product category links at 14-16px weight 600.
- Right controls: circular search button, circular globe button, gray Sign in pill, blue Sign up pill.
- Keep nav opaque and utility-focused.
```

### Iteration Guide

- **색상 변경 시**: first check whether the change breaks the one-blue contract. `#0052FF` should remain the only dominant action color.
- **폰트 변경 시**: preserve display weight 400. Do not make the hero headline 700/800.
- **여백 조정 시**: stay on the 8px ladder (`8/16/24/32/48/64/80`).
- **새 컴포넌트 추가 시**: choose radius by role: 8px for inputs, 16px for content cards, 40px/full for actions.
- **다크 모드**: use the dark tokens (`#0A0B0D`, `#578BFA`) rather than simply inverting light colors.
- **반응형**: stack the hero before compressing the app mockup; the mockup must remain legible.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#0052FF` as the canonical conversion and brand color.
- Keep the main page background `#FFFFFF` and text `#0A0B0D`.
- Use CoinbaseDisplay-style 400-weight display typography for the hero.
- Keep primary buttons pill-shaped with 40px or full radius.
- Use neutral semantic borders such as `rgba(91,97,110,0.2)`.
- Let product UI screenshots carry visual proof.
- Treat green `#098551` and red `#CF202F` as financial state colors, not decoration.

### ❌ DON'T

- 배경을 `#F5F8FF` 또는 full-page blue wash로 두지 말 것 — 대신 `#FFFFFF` 사용.
- 본문 텍스트를 `#000000` 또는 pure black-only token으로 고정하지 말 것 — 대신 CDS text `#0A0B0D` 사용.
- primary CTA를 `#3860BE` 또는 muted blue로 두지 말 것 — 대신 canonical `#0052FF` 사용.
- muted copy를 `#999999`로 낮추지 말 것 — 대신 `#5B616E` 사용.
- border를 `#D8D8D8`로 모든 곳에 과도하게 쓰지 말 것 — core UI는 `rgba(91,97,110,0.2)` 사용.
- positive financial movement를 generic green `#00FF00`으로 쓰지 말 것 — 대신 `#098551` 사용.
- error/negative state를 generic red `#FF0000`으로 쓰지 말 것 — 대신 `#CF202F` 사용.
- hero headline에 `font-weight: 800` 사용 금지 — Coinbase display authority is weight `400`.
- 모든 컴포넌트에 `border-radius: 16px`를 동일 적용하지 말 것 — input `8px`, card `16px`, CTA `40px/full`로 역할을 나눈다.
- chrome에 heavy `box-shadow: 0 20px 60px rgba(0,0,0,.25)` 사용 금지 — Coinbase chrome is mostly flat.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Crypto-neon identity: **absent** — 도구함은 purple/cyan/black 나이트클럽이 아니다, 단일 스위치판이다.
- Second dominant brand color: **none** — blue owns conversion; green/red 신호등은 시장 상태 지시기일 뿐.
- Page-wide gradient mesh: **never** — blue gradient는 product mockup 도구판 안에 갇혀 있다.
- Decorative serif contrast: **absent** — Coinbase는 sans 도구 라벨만 쓰고 editorial finance serif는 등장하지 않는다.
- Heavy display weights: **zero** — H1은 400-weight authority지 800-weight startup hype 버튼판이 아니다.
- Chrome-heavy shadows: **none** — shadow tokens는 overlay 도구에만, 메인 작업판은 flat.
- Sharp brutalist corners for actions: **never** — primary 스위치는 pill 도구로만 가공된다.
- Tiny 13px body copy for primary messaging: **absent** — body 스케일은 16px/24px 도구 라벨 단위.
- Arbitrary rainbow token display: **zero** on the public page — 많은 ramp가 도구함 안에 있지만 외부 버튼판으로는 나오지 않는다.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-only interpretation** — analysis reuses captured `https://www.coinbase.com` homepage artifacts. Logged-in app, exchange, checkout, staking, and account settings surfaces may use different density and component variants.
- **Desktop screenshot bias** — the visual judgment is anchored on a 1280x800 hero screenshot. CSS breakpoints were extracted, but mobile rendering was not visually verified in this pass.
- **Cookie/vendor UI contamination** — frequency candidates include OneTrust/vendor consent CSS and embedded UI. Core Coinbase tokens were prioritized over raw frequency when those conflicted.
- **Token alias extraction was partial** — `alias_layer.json` found no tiered aliases, while CSS clearly includes token variables. This guide therefore uses observed CSS variables and semantic names directly.
- **CSS-in-JS class semantics are inferred** — generated classes such as `flex-ff5rfy6` and styled-component hashes were interpreted by rendered output, property frequencies, and visible HTML text.
- **Motion not runtime-measured** — transition values were extracted from CSS, but scroll-triggered JavaScript, carousel behavior, and live chart animation were not executed or timed.
- **Mega-menu states not fully interacted** — nav menu content is present in HTML text, but hover/open panel measurements were not captured as separate screenshots.
- **Market data content is dynamic** — numbers, availability notes, and product claims may change after the captured artifact date. Layout and token guidance should be treated as the stable layer.
