---
schema_version: 3.2
slug: clerk
service_name: Clerk
site_url: https://clerk.com
fetched_at: 2026-04-20T19:58:00+09:00
default_theme: light
brand_color: "#6C47FF"
primary_font: Suisse
font_weight_normal: 400
token_prefix: clerk

bold_direction: Precision SaaS
aesthetic_category: Refined SaaS
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Production Tailwind/Next CSS with real component tokens, focus states, font variables, and repeated layout primitives; not a public token guidebook."

colors:
  primary: "#6C47FF"
  accent-cyan: "#5DE3FF"
  surface-page: "#FFFFFF"
  surface-soft: "#F7F7F8"
  text-primary: "#131316"
  text-secondary: "#5E5F6E"
  text-muted: "#9394A1"
  border-soft: "#D9D9DE"
  border-hairline: "#0000001A"
  dark-surface: "#212126"

typography:
  display: "Suisse"
  body: "Suisse"
  numeric: "Geist Numbers"
  code: "Soehne Mono"
  ladder:
    - { token: hero, size: "4rem", weight: 600, line_height: "4.5rem", tracking: "-0.035em" }
    - { token: h2, size: "3rem", weight: 600, line_height: "3.5rem", tracking: "-0.035em" }
    - { token: h3, size: "2rem", weight: 600, line_height: "2.5rem", tracking: "-0.025em" }
    - { token: lead, size: "1.125rem", weight: 400, line_height: "1.75rem", tracking: "-0.015em" }
    - { token: body, size: ".9375rem", weight: 400, line_height: "1.5rem", tracking: "0" }
    - { token: label, size: ".8125rem", weight: 500, line_height: "1.25rem", tracking: "0" }
  weights_used: [100, 400, 450, 500, 510, 600, 700, 800]
  weights_absent: [300, 900]

components:
  button-primary: { bg: "{colors.primary}", color: "#FFFFFF", radius: "9999px", padding: ".5rem 1rem", shadow: "0 1px 1px #0000000D" }
  button-secondary: { bg: "#FFFFFF", color: "{colors.text-primary}", radius: "9999px", border: "1px solid #0000001A", padding: ".5rem 1rem" }
  nav-shell: { bg: "#FFFFFF", radius: ".75rem", border: "1px solid #0000001A", shadow: "0 2px 3px #0000000A" }
  focus-ring: { outline: "2px solid {colors.text-primary}", offset: "2px / negative offsets in compact controls" }
  input-dark: { bg: "#2F3037", border: "#FFFFFF1F", focus: "#00000026" }
---

# DESIGN.md — Clerk

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Clerk looks less like an auth vendor and more like a high-precision control surface for identity infrastructure. The page is bright, almost clinical, but not empty: the hero sits over a faint circuit-board drawing, so the white field reads as a technical blueprint rather than a blank SaaS canvas. The user management promise is made in heavy black type first; the product complexity is allowed to whisper through linework behind it.

The first viewport behaves like an architect's vellum sheet laid over an authentication engine. The page does not stage a glossy dashboard screenshot first; it shows the blueprint underneath the promise, as if the product has already been drawn, measured, and cleared for installation. Clerk's white is not gallery emptiness. It is lab-bench white: clean enough that every hairline, node, and pill control becomes evidence.

The visual identity is built from a tight triangle: #131316 (`{colors.text-primary}`) for authority, #FFFFFF (`{colors.surface-page}`) for trust, and #6C47FF (`{colors.primary}`) for the one action that matters. Cyan #5DE3FF (`{colors.accent-cyan}`) appears as a supporting electric accent in gradients and technical details, but it never becomes a second CTA language. Purple owns conversion; cyan owns signal. There is no second brand color competing for the hand; the cyan is a diagnostic glow, not another button.

Typography does the confidence work. Suisse is compact and serious, with display tracking as tight as `-.035em`, while labels and navigation stay small, dense, and practical. The giant headline "More than authentication, Complete User Management" is not decorative hero typography. It is product-scope typography: weight 600, black, wide enough to feel like infrastructure, compressed enough to feel engineered.

The navigation reads like a sealed instrument tray: a white rounded shell, tiny separators, compact labels, and a purple action placed with surgical restraint. Nothing spills out of the tray. The top dark announcement strip is the only black chrome band; below it, the page returns to the white technical sheet and lets `{colors.primary}` puncture it only where conversion happens.

The page's craft lives in tiny construction details: `.5px` ring shadows, pill buttons with sharp micro-shadows, focus outlines that deliberately invert between light and dark, and hero line art that gives depth without using a stock illustration. Clerk avoids the usual AI-SaaS move of flooding the hero with gradients. Instead, it makes the interface itself feel assembled, tested, and ready to embed. Shadow behaves like a caliper mark, not furniture elevation: it measures edges on controls and product islands rather than floating every card into the air.

The logo wall below the hero works like a quiet compliance ledger. Black marks sit inside gridded white panels, almost as if each customer logo has been filed into the system. That restraint is the brand argument: identity infrastructure should not perform chaos. It should make every unknown user, org, session, and permission feel indexed.

### Key Characteristics

- White technical blueprint background, not a plain marketing white.
- Monochrome text hierarchy anchored by #131316 and cooled by #5E5F6E / #9394A1.
- Single conversion color: #6C47FF purple, with cyan #5DE3FF reserved for technical glow and gradient accents.
- Heavy display typography with aggressive negative tracking (`-.035em`) on large headings.
- Pill-shaped controls and nav shell, mostly `9999px` / `.75rem` radius.
- Thin hairlines and half-pixel ring shadows create precision instead of heavy card shadows.
- Top announcement bar uses dark chrome, while the main page returns to white.
- Customer logo wall is intentionally quiet: black marks on gridded white panels.
- Product credibility comes from embedded UI/code/auth surfaces, not lifestyle imagery.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Precision SaaS
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **blueprint hero with pill auth controls**으로 기억된다.
> **Code Complexity**: high — Tailwind/Next utility output, custom font variables, half-pixel shadows, dark/light component branches, and technical background treatments require careful reproduction.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Clerk처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Suisse", "suisse Fallback", ui-sans-serif, system-ui, sans-serif;
  font-weight: 400;
  letter-spacing: 0;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #FFFFFF;
  --fg: #131316;
  --muted: #5E5F6E;
  --hairline: #0000001A;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 액션 */
:root { --brand: #6C47FF; }
.cta {
  background: var(--brand);
  color: #FFFFFF;
  border-radius: 9999px;
  box-shadow: 0 1px 1px #0000000D, 0 0 0 .5px #1313161A;
}
```

**절대 하지 말아야 할 것 하나**: Clerk를 파란/보라 그라디언트 SaaS 히어로로 만들지 마라. 실제 첫 인상은 #FFFFFF 바탕, #131316 대형 타입, 아주 얇은 blueprint line art, 그리고 #6C47FF CTA 하나다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://clerk.com` |
| Fetched | 2026-04-20T19:58:00+09:00 |
| Extractor | reused phase1 artifacts: HTML + CSS + JSON + hero screenshot |
| HTML size | 1,202,105 bytes |
| CSS files | 3 external + 1 inline, total 578,195 CSS chars |
| Token prefix | `clerk` (report alias; source is mostly Tailwind/custom component vars) |
| Method | CSS hex/font/property parsing + screenshot interpretation; no Step 6 HTML report rendered |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js-style production bundle (large hydrated HTML, hashed CSS chunks, Tailwind utility output)
- **Design system**: Internal Clerk marketing/component system — no single public namespace; variables include `--font-*`, `--focus-outline`, `--input-*`, `--tw-*`
- **CSS architecture**: Tailwind utility layer + component-scoped CSS variables
  ```css
  --font-suisse              ("suisse","suisse Fallback")
  --font-geist-numbers       ("geistNumbers")
  --font-soehne-mono         ("soehneMono")
  --focus-outline            (#131316 on light, #fff on dark)
  --input-root-background-color (#fff / #2F3037)
  --input-border-color       (#FFFFFF1F in dark component contexts)
  --tw-*                     generated transform/ring/shadow utilities
  ```
- **Class naming**: Tailwind atomic utilities with escaped arbitrary values plus component variables for auth/input surfaces.
- **Default theme**: light (`#FFFFFF`) with dark product/code islands (`#131316`, `#212126`, `#2F3037`).
- **Font loading**: CSS variables for custom font families: Suisse, Geist Sans/Mono/Numbers, Soehne Mono.
- **Canonical anchor**: hero screenshot shows announcement bar, pill navigation, centered headline, dual CTA row, and logo wall.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Suisse` (`--font-suisse: "suisse","suisse Fallback"`)
- **Body font**: `Suisse`, with occasional `ui-sans-serif` and `Inter` fallback declarations in CSS.
- **Numeric font**: `Geist Numbers` (`--font-geist-numbers`) paired with Suisse.
- **Code font**: `Soehne Mono` (`--font-soehne-mono`) and `Geist Mono` for technical/code surfaces.
- **Weight normal / bold**: `400` / `600`, with `500` heavily used for controls and labels.

```css
:root {
  --clerk-font-family:       "suisse","suisse Fallback",ui-sans-serif,system-ui,sans-serif;
  --clerk-font-family-code:  "soehneMono",ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;
  --clerk-font-family-numbers: "geistNumbers","suisse","suisse Fallback";
  --clerk-font-weight-normal: 400;
  --clerk-font-weight-medium: 500;
  --clerk-font-weight-bold:   600;
}
body {
  font-family: var(--clerk-font-family);
  font-weight: var(--clerk-font-weight-normal);
}
```

### Note on Font Substitutes

- **Suisse substitute** — use **Inter** only if custom font licensing is unavailable, but tighten it. For display sizes, set `font-weight: 600`, `letter-spacing: -0.035em`, and line-height close to `1.08-1.12`. Untuned Inter will look wider and more generic than Clerk.
- **Soehne Mono substitute** — use **Geist Mono** or `ui-monospace`; preserve smaller sizes (`.8125rem` or below) and avoid high-contrast code themes unless the component is explicitly dark.
- **Geist Numbers substitute** — use `font-variant-numeric: tabular-nums` when Geist Numbers is not available. Clerk's numeric/metric UI wants stable alignment, not expressive numerals.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| Hero display | `4rem` | `600` | `4.5rem` | `-.035em` |
| Section display | `3.5rem` / `3rem` | `600` | `3.5rem` | `-.035em` |
| Large title | `2.5rem` / `2.25rem` | `600` | `2.5rem` | `-.025em` |
| Card title | `2rem` | `600` | `2.5rem` | `-.025em` |
| Lead copy | `1.125rem` | `400` | `1.75rem` | `-.015em` |
| Body | `.9375rem` / `1rem` | `400` | `1.5rem` | `0` |
| Nav / control | `.8125rem` | `500` | `1.25rem` | `0` |
| Micro label | `.75rem` / `.6875rem` | `500` | `1rem` | `0` |
| Eyebrow / caps | `.625rem` | `600` | `.75rem` | `.1em` |

> ⚠️ Clerk's typography depends on negative tracking at display sizes. Leaving headings at browser-default tracking makes the hero feel soft and generic.

### Principles

1. Display sizes are compressed: `-.035em` appears repeatedly and is part of the identity, not an incidental optimization.
2. Body copy stays restrained around `.9375rem-1.125rem`; the large feeling comes from headings and air, not oversized paragraphs.
3. Weight `500` is the control language. Buttons, nav labels, and badges often use it; hero headings lean `600`.
4. Numeric and code contexts are treated as product UI, so mono/numeric fonts are functional surfaces rather than decorative developer flair.
5. Uppercase/caps treatment is rare and tiny; Clerk does not build its hierarchy from loud all-caps labels.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed anchors)

| Token | Hex |
|---|---|
| `{colors.primary}` | `#6C47FF` |
| `clerk-purple-gradient` | `#7C3AED` |
| `clerk-cyan-signal` | `#5DE3FF` |
| `clerk-cyan-bright` | `#64E5FF` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| dark action surface | `#131316` |
| dark panel | `#212126` |
| dark input | `#2F3037` |
| dark muted text | `#B7B8C2` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| page | `#FFFFFF` | `#0A0A0B` |
| soft surface | `#F7F7F8` | `#212126` |
| subtle border | `#EEEEF0` | `#2F3037` |
| border | `#D9D9DE` | `#38383B` |
| muted text | `#9394A1` | `#B7B8C2` |
| secondary text | `#5E5F6E` | `#D9D9DE` |
| primary text | `#131316` | `#FFFFFF` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Purple | primary CTA / switch active | `#6C47FF` |
| Cyan | gradient signal / technical glow | `#5DE3FF` |
| Green | syntax link token | `#16A332` |
| Yellow | addon/callout accent | `#FDE047` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| focus light | `#131316` | focus outline on light UI |
| focus dark | `#FFFFFF` | focus outline on dark UI |
| input focus border | `#00000026` | input focus line/ring |
| input ring | `#00000014` | subtle field ring |
| dark input bg | `#2F3037` | embedded auth form fields |
| switch active | `#6C47FF` / `#131316` | active switch states by theme |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--focus-outline` | `#131316` / `#FFFFFF` | accessible ring, theme-swapped |
| `--input-root-background-color` | `#FFFFFF` / `#2F3037` | auth/input surfaces |
| `--input-border-color-focus` | `#00000026` | focused input border |
| `--input-ring-color` | `#00000014` | field ring |
| `--active-text` | `#FFFFFF` | active dark/pill state |
| `--hover-bg` | `#202025` | dark hover state |
| `--bar-bg` | `#5E5F6E` | small internal UI bars |

### 06-7. Dominant Colors (실제 CSS 빈도 순, transparent variants included)

| Token | Hex | Frequency |
|---|---:|---:|
| transparent black | `#0000` | 692 |
| white | `#FFF` | 150 |
| black | `#000` | 82 |
| transparent white | `#FFF0` | 74 |
| primary text / dark ink | `#131316` | 56 |
| soft black alpha | `#0000001A` | 52 |
| dark island | `#2F3037` | 35 |
| muted text | `#9394A1` | 30 |
| primary purple | `#6C47FF` | 26 |

### 06-8. Color Stories

**`{colors.text-primary}` (`#131316`)** — The real brand base. Clerk's authority is black-on-white before it is purple; headlines, logo treatment, focus outlines, and dark chrome all come back to this ink.

**`{colors.surface-page}` (`#FFFFFF`)** — White is an engineered workspace here. It carries faint blueprint line art, logo grids, and thin dividers, so it should remain clean rather than warm or creamy.

**`{colors.primary}` (`#6C47FF`)** — Purple is the conversion token. Use it for primary CTA, active switch states, and carefully scoped emphasis. Do not spread it across every icon or section heading.

**`{colors.accent-cyan}` (`#5DE3FF`)** — Cyan is signal, not brand replacement. It appears in gradients/technical highlights and pairs with purple when the site wants "modern infrastructure" energy.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `clerk-gap-xxs` | `.125rem` / `.25rem` | icon/text nudges, dense UI internals |
| `clerk-gap-xs` | `.375rem` / `.5rem` | button icon gap, menu rows |
| `clerk-gap-sm` | `.75rem` / `1rem` | compact cards, nav clusters |
| `clerk-gap-md` | `1.5rem` / `2rem` | card groups, content columns |
| `clerk-gap-lg` | `3rem` / `4rem` | section groups and hero spacing |
| `clerk-gap-xl` | `5rem` / `8rem` | large editorial bands |
| `clerk-gap-xxl` | `12rem` | major product section separation |

**주요 alias**:
- `--header-mt` → `3rem` (hero/header vertical offset)
- Common CSS gaps: `4rem`, `1.5rem`, `1rem`, `.5rem`, `3rem`

### Whitespace Philosophy

Clerk uses open hero air but compresses the interaction details. The hero has enough vertical space for the headline and line-art background to breathe, while buttons, nav menus, and logo wall panels are tight and sharply measured. That contrast is the point: broad trust at the page level, precision at the component level.

The site is not a 4-8-16-only system. It mixes tiny UI nudges (`.125rem`, `.375rem`) with large editorial jumps (`4rem`, `8rem`, `12rem`). When reproducing it, keep micro-spacing exact around controls and let section spacing be generous. If both layers are averaged into medium spacing, the Clerk feel disappears.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `radius-pill` | `9999px` | primary/secondary buttons, capsules |
| `radius-nav` | `.75rem` | floating nav shell / larger cards |
| `radius-card` | `.625rem` / `.5rem` | compact product cards, embedded panels |
| `radius-control` | `.375rem` | menus, inputs, small controls |
| `radius-tight` | `.25rem` | code chips and dense UI |
| `radius-micro` | `.125rem` / `.0625rem` | inner technical details |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| hairline ring | `0 0 0 .5px #1313161A` | subtle card/control boundary |
| control base | `0 1px 1px #0000000D` | button and small pill lift |
| nav/card soft | `0 2px 3px #0000000A, 0 4px 6px #222A350A` | floating chrome without heavy elevation |
| product panel | `0 16px 36px -6px #191C2133, 0 8px 16px -3px #00000014` | deep product UI islands |
| dark button active | `0 1px 1px #2B2B343D, 0 2px 3px #2B2B3433, inset 0 1px 1px #FFFFFF12` | dark/auth controls |
| full-bleed dark extension | `100vmax 0 0 100vmax #131316` | extending dark bands beyond container |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| micro transform | `transform .1s, opacity .1s` | compact hover/press response |
| micro transform alt | `transform .12s, opacity .12s` | button/menu variants |
| color/background | `.45s cubic-bezier(.33,1,.68,1)` | smoother theme/color transitions |
| accordion dimension | `.25s linear(...)` + `.175s cubic-bezier(.4,0,.2,1)` | expanding/collapsing technical UI |
| fade in | `--fade-in-duration: 1s` | content reveal |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: common caps include `64rem`, `80rem`, `90rem`, with many component-specific caps from `20rem` to `50rem`.
- **Grid type**: CSS Grid + Flexbox; repeated templates include `repeat(3,minmax(0,1fr))`, `repeat(2,minmax(0,1fr))`, `repeat(4,minmax(0,1fr))`, and occasional `repeat(12,minmax(0,1fr))`.
- **Column count**: 1-6 for most sections; 12-column appears as a utility scaffold, not the visible homepage rhythm.
- **Gutter**: common `1rem`, `1.5rem`, `3rem`, `4rem`, with small `.5rem` and `.375rem` inside controls.

### Hero
- **Pattern Summary**: centered hero + white blueprint background + large two-line H1 + dual CTA row + logo wall immediately below.
- Layout: one-column centered content, nav/announcement above, trust grid below.
- Background: `#FFFFFF` with faint line-art/circuit motif and subtle technical nodes.
- **Background Treatment**: image/SVG-like blueprint line pattern on white; no full-bleed photograph, no dominant gradient wash.
- H1: `4rem` class family / weight `600` / tracking around `-.035em`; screenshot shows heavy black, centered, multi-line.
- Max-width: hero text visually around `64rem-80rem`, copy narrower around `42rem-48rem`.

### Section Rhythm

```css
section {
  padding-block: 4rem 6rem;
  padding-inline: 1rem;
  max-width: 80rem;
}
```

### Card Patterns
- **Card background**: `#FFFFFF` for light cards; `#F7F7F8` for soft panels; `#212126` / `#2F3037` for product/auth islands.
- **Card border**: mostly `1px` / `.5px` optical rings using `#0000001A`, `#D9D9DE`, or dark equivalents.
- **Card radius**: `.5rem-.75rem` for panels; pill only for actions.
- **Card padding**: `.75rem-2rem` depending on density.
- **Card shadow**: hairline + small stacked shadows; no big generic blur on ordinary cards.

### Navigation Structure
- **Type**: horizontal desktop nav inside a rounded white shell, with dropdown chevrons.
- **Position**: top of page below black announcement strip; visually floating but compact.
- **Height**: screenshot nav shell around 46px; controls around 32-36px.
- **Background**: `#FFFFFF` with subtle shadow/ring.
- **Border**: `#0000001A` hairline; right separators around logo/menu cluster.

### Content Width
- **Prose max-width**: `40ch` appears in CSS; hero copy visually around 42-48rem.
- **Container max-width**: `80rem` / `90rem` for wide marketing sections.
- **Sidebar width**: not a homepage primary pattern; product/documentation surfaces may use sidebars outside this single-page analysis.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile small | `23.4375em` | very small layout refinements |
| Mobile wide | `27em` / `32.125em` | compact grid and max-width changes |
| Tablet | `40em` | major Tailwind `sm` branch; nav/grid adjustments |
| Medium | `48em` | content/grid upgrades |
| Desktop | `64em` | full desktop layout, larger grids |
| Wide | `80em` | large section caps and spacing |
| Max wide | `96em` | final high-resolution refinements |

### Touch Targets
- **Minimum tap size**: compact controls appear around 32-36px desktop; mobile should raise clickable area toward 44px even if visual pill remains small.
- **Button height (mobile)**: use at least `2.5rem` hit area for primary actions.
- **Input height (mobile)**: embedded auth inputs should preserve generous vertical padding and focus outline visibility.

### Collapsing Strategy
- **Navigation**: desktop horizontal nav collapses into mobile menu; dropdown affordances should remain explicit.
- **Grid columns**: repeated 3/4/5/6-column templates collapse to 1-2 columns below `40em` / `48em`.
- **Sidebar**: not applicable on homepage hero; product/docs surfaces likely have separate responsive sidebar rules.
- **Hero layout**: remains centered; headline size and line breaks must scale down rather than switching to split hero.

### Image Behavior
- **Strategy**: responsive SVG/illustration/UI surfaces with `max-width: 100%`; line-art background can crop softly.
- **Max-width**: product panels and hero content capped; logos are constrained inside grid cells.
- **Aspect ratio handling**: technical UI mockups should keep fixed aspect ratio; logo wall cells keep stable height.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA**

```html
<button class="clerk-button clerk-button--primary">Start building for free</button>
```

| Property | Value |
|---|---|
| Background | `#6C47FF` |
| Text | `#FFFFFF` |
| Radius | `9999px` |
| Font | Suisse, `.8125rem`, weight `500` |
| Padding | approx `.5rem 1rem` |
| Shadow | small black alpha + half-pixel ring |
| Hover | subtle transform/opacity response, not large lift |
| Focus | `2px solid #131316` or theme-swapped `#FFFFFF` |

**Secondary CTA**

```html
<button class="clerk-button clerk-button--secondary">Build with agents</button>
```

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#131316` |
| Border | `1px solid #0000001A` / `#D9D9DE` |
| Radius | `9999px` |
| Icon | small chevron, same optical weight as label |

### Badges

```html
<a class="clerk-announcement" href="/changelog">
  <span>Clerk raises $50m Series C</span>
  <span>Learn more</span>
</a>
```

| Property | Value |
|---|---|
| Background | dark strip around `#0A0A0B` / `#131316` |
| Text | `#FFFFFF` and softened white alpha |
| Divider | subtle vertical hairline |
| Size | `.8125rem` label scale |
| Motion | minimal hover color/opacity |

### Cards & Containers

```html
<article class="clerk-card">
  <h3>User Authentication</h3>
  <p>Everything you need for authentication.</p>
</article>
```

| Property | Value |
|---|---|
| Background | `#FFFFFF` or `#F7F7F8` |
| Border | `#0000001A` or `#EEEEF0` |
| Radius | `.5rem-.75rem` |
| Padding | `1rem-2rem` |
| Shadow | hairline ring; larger stacks only for product UI panels |
| Hover | border/shadow refinement, no bouncy card animation |

### Navigation

```html
<nav class="clerk-nav">
  <a class="clerk-logo">clerk</a>
  <a>Products</a>
  <a>Docs</a>
  <a>Pricing</a>
  <button>Start building</button>
</nav>
```

| Property | Value |
|---|---|
| Shell | rounded white capsule/surface |
| Radius | `.75rem` outer, pill inner controls |
| Border | `#0000001A` |
| Shadow | subtle stacked shadow/ring |
| Links | `.8125rem`, weight `500`, black/muted |
| Active/open | chevron and menu treatment, not underline nav |

### Inputs & Forms

```html
<label class="clerk-field">
  <span>Email address</span>
  <input placeholder="you@example.com" />
</label>
```

| Property | Value |
|---|---|
| Light background | `#FFFFFF` |
| Dark background | `#2F3037` |
| Border focus | `#00000026` |
| Ring | `#00000014` |
| Radius | `.375rem-.5rem` |
| Font | Suisse body; technical values can use Geist Numbers |
| Error | not fully observed; use explicit red token only when sourced from form flow |

### Hero Section

```html
<section class="clerk-hero">
  <h1>More than authentication,<br />Complete User Management</h1>
  <p>Need more than sign-in? Clerk gives you full stack auth and user management.</p>
  <div class="clerk-hero-actions">...</div>
</section>
```

| Property | Value |
|---|---|
| Background | `#FFFFFF` with blueprint/circuit line art |
| H1 | `4rem`, weight `600`, tracking `-.035em`, color `#131316` |
| Copy | `1.125rem`, color `#5E5F6E`, centered |
| CTA layout | centered row, primary purple + secondary white |
| Below fold | logo wall starts immediately after hero, separated by grid hairlines |

### 13-2. Named Variants

**button-primary-purple**

| Property | Value |
|---|---|
| Background | `#6C47FF` |
| Text | `#FFFFFF` |
| Radius | `9999px` |
| Use | "Start building for free", primary conversion only |

**button-secondary-white-pill**

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Border | `#0000001A` |
| Text | `#131316` |
| Use | secondary agent/build choices |

**nav-floating-shell**

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Radius | `.75rem` |
| Border/shadow | hairline + small stacked shadow |
| Use | top-level product navigation |

**auth-input-dark**

| Property | Value |
|---|---|
| Background | `#2F3037` |
| Border | `#FFFFFF1F` |
| Focus | `#00000026` |
| Use | embedded sign-in/product UI panels |

### 13-3. Signature Micro-Specs

```yaml
blueprint-hero-linework:
  description: "히어로를 SaaS 장식이 아니라 인증 인프라 설계도처럼 보이게 하는 저대비 linework."
  technique: "background #FFFFFF with faint circuit/blueprint lines near #EEEEF0, #D9D9DE, or #0000001A; small node details; no neon stroke."
  applied_to: ["{component.hero-section}"]
  visual_signature: "제품 스크린샷보다 먼저 '이미 설계된 시스템'이라는 인상이 깔린다."

half-pixel-ring-stack:
  description: "큰 elevation 대신 .5px optical ring과 미세 alpha shadow로 경계를 재는 Clerk식 표면 공법."
  technique: "box-shadow: 0 0 0 .5px #1313161A, 0 1px 1px #0000000D; dark variants use inset .5px rings and low-alpha highlights."
  applied_to: ["{component.button-primary}", "{component.button-secondary}", "{component.nav-shell}", "{component.product-panel}"]
  visual_signature: "카드가 떠오르는 대신 계측 장비처럼 또렷하게 절단된 모서리."

sealed-white-nav-shell:
  description: "상단 네비게이션을 독립된 white instrument tray처럼 밀봉하는 compact shell."
  technique: "background #FFFFFF; border 1px solid #0000001A; border-radius .75rem; shadow 0 2px 3px #0000000A, 0 4px 6px #222A350A; links at .8125rem/500."
  applied_to: ["{component.nav-shell}"]
  visual_signature: "검은 announcement bar 아래에서 흰 조작 패널 하나만 정밀하게 떠 있는 느낌."

tight-suisse-infrastructure-display:
  description: "제품 범위를 크게 말하되 playful SaaS처럼 풀어지지 않게 압축하는 display typography."
  technique: "font-family Suisse; font-weight 600; letter-spacing -.035em on hero/h2 scale, -.025em on h3; line-height around 1.08-1.12."
  applied_to: ["{component.hero-section}", "{component.section-title}"]
  visual_signature: "헤드라인이 광고 문구가 아니라 인프라 명세 제목처럼 응집된다."

scoped-purple-cyan-signal:
  description: "브랜드 에너지를 CTA와 기술 신호에만 제한하는 no-second-CTA-color 규칙."
  technique: "#6C47FF for primary action/active states; #5DE3FF and #7C3AED only in scoped gradients or technical accents; no page-wide gradient wash."
  applied_to: ["{component.button-primary}", "{component.technical-accent}", "{component.hero-section}"]
  visual_signature: "보라색은 손이 가는 곳, 시안은 회로가 살아 있는 곳에만 나타난다."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Product scope expansion, direct and large | "More than authentication, Complete User Management" |
| Primary CTA | Action-first, free-start framing | "Start building for free" |
| Secondary CTA | Developer/tooling context | "Build with agents" |
| Subheading | Explain operational benefit in one sentence | "launch faster, scale easier..." |
| Tone | Confident infrastructure, not playful consumer copy | "Everything you need for authentication" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Clerk — copy into your root stylesheet */
:root {
  /* Fonts */
  --clerk-font-family: "suisse","suisse Fallback",ui-sans-serif,system-ui,sans-serif;
  --clerk-font-family-code: "soehneMono",ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;
  --clerk-font-family-numbers: "geistNumbers","suisse","suisse Fallback";
  --clerk-font-weight-normal: 400;
  --clerk-font-weight-medium: 500;
  --clerk-font-weight-bold: 600;

  /* Core colors */
  --clerk-color-brand-500: #6C47FF;
  --clerk-color-accent-cyan: #5DE3FF;
  --clerk-bg-page: #FFFFFF;
  --clerk-bg-soft: #F7F7F8;
  --clerk-bg-dark: #131316;
  --clerk-bg-panel-dark: #212126;
  --clerk-text: #131316;
  --clerk-text-secondary: #5E5F6E;
  --clerk-text-muted: #9394A1;
  --clerk-border: #D9D9DE;
  --clerk-hairline: #0000001A;

  /* Spacing */
  --clerk-space-xs: .5rem;
  --clerk-space-sm: 1rem;
  --clerk-space-md: 1.5rem;
  --clerk-space-lg: 4rem;

  /* Radius */
  --clerk-radius-control: .375rem;
  --clerk-radius-card: .75rem;
  --clerk-radius-pill: 9999px;

  /* Effects */
  --clerk-ring-hairline: 0 0 0 .5px #1313161A;
  --clerk-shadow-control: 0 1px 1px #0000000D;
  --clerk-focus-outline: 2px solid #131316;
}

.clerk-hero {
  background: var(--clerk-bg-page);
  color: var(--clerk-text);
  text-align: center;
  position: relative;
  overflow: hidden;
}

.clerk-hero h1 {
  font-family: var(--clerk-font-family);
  font-size: clamp(3rem, 7vw, 4rem);
  line-height: 1.1;
  letter-spacing: -.035em;
  font-weight: 600;
}

.clerk-button-primary {
  border: 0;
  border-radius: var(--clerk-radius-pill);
  background: var(--clerk-color-brand-500);
  color: #FFFFFF;
  font: 500 .8125rem/1.25rem var(--clerk-font-family);
  padding: .5rem 1rem;
  box-shadow: var(--clerk-shadow-control), var(--clerk-ring-hairline);
}

.clerk-button-secondary {
  border: 1px solid var(--clerk-hairline);
  border-radius: var(--clerk-radius-pill);
  background: #FFFFFF;
  color: var(--clerk-text);
  font: 500 .8125rem/1.25rem var(--clerk-font-family);
  padding: .5rem 1rem;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Clerk-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        clerk: {
          purple: '#6C47FF',
          cyan: '#5DE3FF',
          ink: '#131316',
          muted: '#5E5F6E',
          subtle: '#9394A1',
          soft: '#F7F7F8',
          border: '#D9D9DE',
          dark: '#212126',
        },
      },
      fontFamily: {
        sans: ['Suisse', 'suisse Fallback', 'ui-sans-serif', 'system-ui'],
        mono: ['Soehne Mono', 'Geist Mono', 'ui-monospace'],
        numbers: ['Geist Numbers', 'Suisse', 'ui-sans-serif'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
        semibold: '600',
      },
      borderRadius: {
        control: '.375rem',
        card: '.75rem',
        pill: '9999px',
      },
      boxShadow: {
        hairline: '0 0 0 .5px #1313161A',
        control: '0 1px 1px #0000000D, 0 0 0 .5px #1313161A',
        panel: '0 16px 36px -6px #191C2133, 0 8px 16px -3px #00000014',
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
| Brand primary | `{colors.primary}` | `#6C47FF` |
| Accent signal | `{colors.accent-cyan}` | `#5DE3FF` |
| Background | `{colors.surface-page}` | `#FFFFFF` |
| Soft surface | `{colors.surface-soft}` | `#F7F7F8` |
| Text primary | `{colors.text-primary}` | `#131316` |
| Text muted | `{colors.text-muted}` | `#9394A1` |
| Border | `{colors.border-soft}` | `#D9D9DE` |
| Dark panel | `{colors.dark-surface}` | `#212126` |

### Example Component Prompts

#### Hero Section

```text
Clerk 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF, 아주 흐린 blueprint/circuit line art를 뒤에 깔 것
- H1: Suisse, clamp(3rem, 7vw, 4rem), weight 600, tracking -.035em, color #131316
- 서브텍스트: #5E5F6E, 1.125rem, line-height 1.75rem, max-width 48rem
- CTA: primary #6C47FF pill + secondary white pill with #0000001A border
- 그림자: 큰 blur 대신 0 1px 1px #0000000D + .5px hairline ring
```

#### Card Component

```text
Clerk 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF 또는 #F7F7F8
- border: 1px solid #0000001A, radius .75rem
- shadow: 0 0 0 .5px #1313161A plus tiny #0000000D control shadow
- 제목: Suisse, 2rem 이하, weight 600, tracking -.025em
- 본문: #5E5F6E, .9375rem, line-height 1.5rem
- hover는 border/shadow만 미세하게 바꾸고 transform bounce 금지
```

#### Badge

```text
Clerk announcement badge/top bar를 만들어줘.
- dark strip: #0A0A0B 또는 #131316
- text: #FFFFFF with muted white alpha for secondary part
- font: Suisse .8125rem weight 500
- subtle divider, no colorful gradient background
```

#### Navigation

```text
Clerk 스타일 상단 네비게이션을 만들어줘.
- white rounded shell, radius .75rem, border #0000001A
- logo left, menu links .8125rem weight 500, chevrons included
- right side: Sign in text + Start building white pill
- shell shadow is subtle: 0 2px 3px #0000000A, not a large floating card
```

### Iteration Guide

- **색상 변경 시**: purple #6C47FF는 CTA/action에만 남기고, page structure는 #FFFFFF / #131316 / #D9D9DE로 유지한다.
- **폰트 변경 시**: display tracking `-.035em`을 같이 보정한다. 폰트만 바꾸면 Clerk 특유의 압축감이 사라진다.
- **여백 조정 시**: control internals는 `.375rem-.75rem`, section spacing은 `4rem+`로 분리한다.
- **새 컴포넌트 추가 시**: pill, hairline, tiny shadow, accessible focus ring 네 가지를 먼저 맞춘다.
- **다크 모드**: #212126 / #2F3037 기반 product island로 제한한다. 전체 페이지를 dark로 뒤집지 않는다.
- **반응형**: `40em`, `48em`, `64em`, `80em` breakpoint 계단을 우선 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #FFFFFF as the primary page surface and let faint technical line art create depth.
- Use #131316 for primary text and focus authority; it is the real visual anchor.
- Use #6C47FF only for primary conversion and active action states.
- Preserve tight display tracking around `-.035em` for hero-scale headings.
- Use pill buttons (`9999px`) and compact `.8125rem` control typography.
- Build surface depth from `0 0 0 .5px` rings and tiny alpha shadows, not heavy cards.
- Keep dark surfaces as product/auth islands rather than the whole marketing page.
- Pair purple with #5DE3FF only for scoped technical signal moments.

### ❌ DON'T

- 배경을 `#F4F4F4`, `#FAFAFA`, 또는 warm cream으로 두지 말 것 — Clerk homepage는 `#FFFFFF` 기반이다.
- 본문 텍스트를 `#000000` 또는 `black`으로만 두지 말 것 — primary ink는 `#131316`을 사용한다.
- CTA를 `#7C3AED` 또는 generic violet으로 통일하지 말 것 — primary action은 `#6C47FF`가 canonical이다.
- 보조 텍스트를 `#666666`으로 두지 말 것 — `#5E5F6E` 또는 `#9394A1` 계열을 사용한다.
- 경계선을 `#E5E7EB` Tailwind gray로 대체하지 말 것 — `#D9D9DE`, `#EEEEF0`, `#0000001A`를 사용한다.
- Hero에 `linear-gradient(135deg, #667eea, #764ba2)`를 쓰지 말 것 — white blueprint surface + scoped purple CTA가 맞다.
- Headline letter-spacing을 `0`으로 두지 말 것 — large display는 `-.035em` 근처로 조인다.
- 모든 카드를 `box-shadow: 0 20px 40px #00000020`로 띄우지 말 것 — `.5px` ring과 작은 alpha shadow를 우선한다.
- 버튼을 `border-radius: 8px` 사각형으로 만들지 말 것 — primary/secondary actions는 `9999px` pill이다.
- Dark UI의 input background를 `#111111`로 뭉개지 말 것 — observed dark input surface는 `#2F3037`이다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No second CTA color** — cyan exists, but it does not compete with #6C47FF for primary action.
- **No warm editorial palette** — no beige, cream, tan, or paper texture identity on the homepage.
- **No stock SaaS gradient hero** — gradient accents exist in CSS, but the first viewport is white blueprint precision.
- **No lifestyle photography** — trust is built through product surfaces, logo wall, and technical linework.
- **No heavy card elevation** — ordinary UI chrome avoids large diffuse shadows.
- **No playful rounded cards everywhere** — pills are for actions; panels stay controlled with `.5rem-.75rem` radius.
- **No loud multi-color icon system** — chromatic color is scoped; monochrome marks dominate the logo wall.
- **No casual display type** — headings are compressed and serious, not bubbly or handwritten.
- **No full dark marketing theme** — dark appears as announcement/product/auth islands only.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage snapshot** — analysis reused `insane-design/clerk` phase1 artifacts and the hero screenshot. Logged-in dashboard, docs pages, pricing flow, and checkout/account subflows were not visited.
- **CSS bundle is utility-heavy** — many values are generated Tailwind utilities. Some repeated tokens may come from unused or below-the-fold components rather than visible hero elements.
- **Logo wall contamination** — frequency counts include customer logos and SVG/pattern colors. Brand color selection intentionally favors CTA/product usage over raw frequency.
- **Motion not fully exercised** — CSS transitions were parsed, but scroll-triggered JavaScript, dropdown animation timing, and announcement interactions were not run in a browser during this pass.
- **Form validation states not surfaced** — input variables exist, but error/loading/disabled auth states were not visually exercised from an actual sign-in flow.
- **Dark mode mapping partial** — dark panel and input tokens are visible in CSS, but a complete theme-pair map was not proven for every component.
- **Exact hero line-art implementation** — screenshot confirms the blueprint visual; the final drawing source may be SVG/image/CSS composition inside the large HTML bundle.
- **Font availability** — Suisse and Soehne Mono are inferred from CSS variables; licensing and exact font files were not audited.
- **Report HTML skipped by request** — Step 6 RENDER-HTML was intentionally not executed; this file is the deliverable.
