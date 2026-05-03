---
schema_version: 3.2
slug: tinybird
service_name: Tinybird
site_url: https://www.tinybird.co
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: dark
brand_color: "#27F795"
primary_font: "Roboto Mono"
font_weight_normal: 400
token_prefix: tb

bold_direction: Terminal SaaS
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "194 CSS variables, Tailwind v4 tokens, named type/radius/color variables, and repeated nav/button/card patterns; no official public DS layer observed."

colors:
  primary: "#27F795"
  primary-dark: "#008060"
  surface-dark: "#0A0A0A"
  surface-panel: "#151515"
  border-dark: "#262626"
  text-primary: "#FFFFFF"
  text-muted: "#999999"
  code-identifier: "#00C1FF"
  code-value: "#FC9F5B"
  error: "#FF8389"
typography:
  display: "Roboto"
  body: "Roboto"
  mono: "Roboto Mono"
  ladder:
    - { token: h1, size: "64px", weight: 400, line_height: "72px", tracking: "-0.08rem" }
    - { token: h1-mobile, size: "56px", weight: 400, line_height: "64px", tracking: "-0.105rem" }
    - { token: h2, size: "64px", weight: 400, line_height: "72px", tracking: "-0.08rem" }
    - { token: h3, size: "40px", weight: 400, line_height: "48px", tracking: "0.025rem" }
    - { token: body-1, size: "18px", weight: 400, line_height: "32px", tracking: "0" }
    - { token: body-2, size: "16px", weight: 400, line_height: "24px", tracking: "0" }
    - { token: caption, size: "12px", weight: 400, line_height: "20px", tracking: "0" }
  weights_used: [300, 400, 500, 700]
  weights_absent: [600]
components:
  button-primary: { bg: "{colors.primary}", color: "{colors.surface-dark}", radius: "0px", padding: "16px 24px" }
  button-primary-hover: { bg: "{colors.primary-dark}", color: "{colors.text-primary}" }
  button-link: { bg: "transparent", color: "{colors.primary}", decoration: "hover underline" }
  nav-dark-grid: { bg: "{colors.surface-dark}", height: "64px mobile / 72px desktop", max_width: "1440px" }
  tab-terminal-chip: { bg: "rgba(53,53,53,0.3)", border: "1px solid #353535", radius: "4px" }
---

# DESIGN.md — Tinybird (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Tinybird's homepage is not the usual soft SaaS gradient room. It is closer to a midnight operations room where the wall monitor has gone black and only the executable signal remains. The page opens on #0A0A0A (`{colors.surface-dark}`), a white wordmark, and a centered product promise; #27F795 (`{colors.primary}`) does not behave like decoration, but like the cursor after a command has returned successfully.

The visual metaphor is "managed infrastructure as a live console." Navigation, category tabs, CTA copy, and footer details all borrow terminal habits: mono type, square edges, bracket punctuation, compact line rhythm, and green-on-black contrast. The brackets are not ornamental chrome; they make the page feel like a selector waiting for input. A user is not strolling through a product gallery, but choosing a pipe, a query, a route.

Tinybird splits its voice like a control plane attached to a public announcement system. Large hero copy stays in Roboto so the promise can read cleanly at billboard scale, while operational surfaces switch into Roboto Mono as if the page has dropped into shell mode. It is the opposite of a glassy demo dashboard: the machinery is not hidden behind frosted cards, it is exposed through type, syntax, and rectangular controls.

The brand color has a strict job description. There is no second brand color competing for memory; #27F795 (`{colors.primary}`) is the run button, active tab, success wire, and hover voltage. Blue (#00C1FF / `{colors.code-identifier}`) and orange (#FC9F5B / `{colors.code-value}`) stay inside the code/data palette, like syntax highlighting behind the glass. The site would lose its identity if those colors escaped into general marketing chrome.

Depth is drawn like circuit-board etching rather than floated like SaaS cards. #151515 (`{colors.surface-panel}`) panels sit on the #0A0A0A (`{colors.surface-dark}`) floor, and #262626 (`{colors.border-dark}`) hairlines act like routed traces between modules. Shadow is not the storytelling device; the border is. Even the CTA refuses the rounded pill grammar, landing as a square terminal key instead of a friendly lozenge.

The craft is in this refusal. No pastel aurora hero, no glossy product illustration doing the credibility work, no cheerful rounded dashboard furniture. Motion exists as short Tailwind transitions and a long logo-scroll loop, more status light than performance. It is a SaaS marketing site, but its strongest signal is that it keeps deleting ordinary SaaS softness until the page feels executable.

### Key Characteristics

- Dark-first marketing surface: #0A0A0A dominates the first viewport.
- Neon green action anchor: #27F795 is CTA, active state, success/code color, and brand memory.
- Roboto for readable display; Roboto Mono for navigation, buttons, tabs, and operational UI.
- Square CTA geometry: no pill radius, no rounded SaaS softness.
- Bracket syntax in nav/tabs makes the UI feel like a CLI selector.
- 1440px max-width shell with 12-column hero content and wide but controlled gutters.
- Thin dark borders (#262626 / #353535) replace elevation.
- Code palette supports the brand: #00C1FF identifiers, #FC9F5B values, #FF8389 errors.
- Motion is mostly utility: 150ms color/transform transitions and 50s logo marquee.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Terminal SaaS
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **dark terminal hero with neon execution green**으로 기억된다.
> **Code Complexity**: high — Tailwind v4 utility system, Next.js font plumbing, CSS token layer, responsive nav, dropdowns, tabs, and animated logo strips.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Tinybird처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Roboto", "Roboto Fallback", system-ui, sans-serif;
  font-weight: 400;
}
.ui, nav, button, .chip {
  font-family: "Roboto Mono", "Roboto Mono Fallback", ui-monospace, monospace;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #0A0A0A; --fg: #FFFFFF; --muted: #999999; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #27F795; --brand-dark: #008060; }
.button-primary { background: var(--brand); color: #0A0A0A; }
.button-primary:hover { background: var(--brand-dark); color: #FFFFFF; }
```

**절대 하지 말아야 할 것 하나**: Tinybird를 둥근 파란 SaaS UI로 만들지 말 것. `#27F795` on `#0A0A0A`와 mono interaction layer가 정체성이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.tinybird.co` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | cached phase1 reuse: existing HTML/CSS/screenshots |
| HTML size | 296670 bytes (Next.js SSR / React flight payload) |
| CSS files | 3 external CSS files, total 173598 chars |
| Token prefix | `tb` (report alias; source CSS uses global custom properties) |
| Method | CSS custom properties + HTML class inspection + screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js application router (React flight chunks, `/_next/static/*`, `next-size-adjust`)
- **Design system**: Tailwind v4 utility tokens over custom CSS variables. Source variables are global, not namespaced.
- **CSS architecture**:
  ```text
  core     (--primary, --gray-950, --text-h1, --radius-card)  raw values
  utility  (.text-h1, .bg-primary, .max-w-[1440px])           Tailwind v4 utilities
  component (button/link/nav/card class compositions)         composed in HTML
  ```
- **Class naming**: Tailwind utility composition with arbitrary values (`max-w-[1440px]`, `grid-cols-[1fr_auto_1fr]`, `text-[clamp(...)]`).
- **Default theme**: dark (`html.dark`, first viewport #0A0A0A / #151515 family).
- **Font loading**: Next font self-hosted WOFF/WOFF2 with metric fallback classes (`Roboto Fallback`, `Roboto Mono Fallback`, `Fira Mono Fallback`, `sevenSegment Fallback`).
- **Canonical anchor**: Homepage hero and nav. Product dropdown and footer reveal the same dark panel grammar.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Roboto` (self-hosted via Next font)
- **UI/code font**: `Roboto Mono` and `Fira Mono`
- **Special numeric font**: `sevenSegment` appears as a loaded family for display/metric moments.
- **Weight normal / bold**: `400` / `700`; `300` and `500` are also present.

```css
:root {
  --tb-font-family:       "Roboto", "Roboto Fallback";
  --tb-font-family-mono:  "Roboto Mono", "Roboto Mono Fallback";
  --tb-font-family-code:  "Fira Mono", "Fira Mono Fallback";
  --tb-font-weight-normal: 400;
  --tb-font-weight-bold:   700;
}
body {
  font-family: var(--tb-font-family);
  font-weight: var(--tb-font-weight-normal);
}
nav, button, .terminal-chip {
  font-family: var(--tb-font-family-mono);
}
```

### Note on Font Substitutes

- **Roboto / Roboto Mono** are both open-source and safe to reproduce. Use the actual Google families where possible rather than substituting Inter.
- **Roboto Mono substitute**: use `IBM Plex Mono` at weight 400 with unchanged line-height when Roboto Mono is unavailable. Avoid JetBrains Mono unless you tighten letter spacing; it reads more programmer-editor than Tinybird terminal.
- **Display correction**: if substituting `Inter`, set hero tracking close to `-0.02em` to approximate Tinybird's `--text-h1--letter-spacing: -0.08rem` at 64px.
- **Body correction**: keep body copy at 18px / 32px. Do not compress it to generic 16px / 24px SaaS body rhythm.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `--text-h1` | 64px | 400 | 72px | -0.08rem |
| `--text-h1-mobile` | 56px | 400 | 64px | -0.105rem |
| `--text-h2` | 64px | 400 | 72px | -0.08rem |
| `--text-h2-mobile` | 40px | 400 | 44px | -0.075rem |
| `--text-h3` | 40px | 400 | 48px | 0.025rem |
| `--text-h3-mobile` | 32px | 400 | 40px | -0.02rem |
| `--text-h4` | 32px | 400 | 40px | -0.0625rem |
| `--text-h5` | 24px | 400 | 32px | -0.02rem |
| `--text-body-1` | 18px | 400 | 32px | 0 |
| `--text-body-2` | 16px | 400 | 24px | 0 |
| `--text-body-3` | 14px | 400 | 22px | 0 |
| `--text-button` | 16px | 400 | 24px | inherited |
| `--text-caption` | 12px | 400 | 20px | 0 |

> ⚠️ Tinybird's display scale is large but not heavy. The hero feels sharp because it is 64px with negative tracking, not because it uses 700 weight.

### Principles

1. Display type is regular-weight: 64px / 72px at weight 400 creates calm technical authority.
2. Mono is interaction language: nav, buttons, chips, and links should feel typed, not merely labeled.
3. Body lead is generous: 18px / 32px makes dense infrastructure messaging readable on a dark floor.
4. Negative tracking is display-only. Body and mono UI keep neutral spacing for terminal clarity.
5. Weight 600 is effectively absent from extracted tokens; use 500/700 only when the source pattern demands stronger hierarchy.
6. Mobile display remains oversized at 56px, so the brand keeps its large-console feel even below desktop.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (2 steps)

| Token | Hex |
|---|---|
| `--primary` | `#27F795` |
| `--primary-dark` | `#008060` |

### 06-2. Brand Dark Variant

> N/A — Tinybird uses the same green identity on dark surfaces; hover/darkening is handled by `--primary-dark`.

### 06-3. Neutral Ramp

| Step | Light/Dark token | Hex |
|---|---|---|
| white | `--white` | `#FFFFFF` |
| gray-50 | `--gray-50` | `#F6F7F9` |
| gray-100 | `--gray-100` | `#E8E9ED` |
| gray-200 | `--gray-200` | `#D9D9D9` |
| gray-300 | `--gray-300` | `#999999` |
| gray-400 | `--gray-400` | `#8D8D8D` |
| gray-500 | `--gray-500` | `#636679` |
| gray-600 | `--gray-600` | `#3C3C3C` |
| gray-700 | `--gray-700` | `#353535` |
| gray-800 | `--gray-800` | `#262626` |
| gray-900 | `--gray-900` | `#151515` |
| gray-950 | `--gray-950` | `#0A0A0A` |
| black | `--black` | `#000000` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Secondary blue | `--secondary` | `#2D27F7` |
| Secondary cyan | `--secondary-light` | `#00C1FF` |
| Warning/value orange | `--warning`, `--color-code-value` | `#FC9F5B` |
| Error red | `--error`, `--color-code-error` | `#FF8389` |
| Success/code invocation | `--color-code-success`, `--color-code-invocation` | `#27F795` |
| Diff added | `--color-code-diff-added` | `#008060` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--primary` | `#27F795` | primary CTA, active tabs, links, logo hover, code invocation |
| `--primary-dark` | `#008060` | CTA hover, darker success/diff tone |
| `--gray-950` | `#0A0A0A` | page background / hero floor |
| `--gray-900` | `#151515` | panels, dropdown surfaces, footer panels |
| `--gray-800` | `#262626` | borders and dark dividers |
| `--gray-300` | `#999999` | muted body text |
| `--white` | `#FFFFFF` | primary foreground on dark |
| `--error` | `#FF8389` | error/code red |
| `--warning` | `#FC9F5B` | warning/code value orange |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `.bg-primary` | `--primary` → `#27F795` | main CTA and active UI |
| `.hover:bg-primary-dark` | `--primary-dark` → `#008060` | primary button hover |
| `.text-primary` | `--primary` → `#27F795` | links, nav hover, tab active |
| `.text-gray-950` | `--gray-950` → `#0A0A0A` | text on green button |
| `.border-gray-800` | `--gray-800` → `#262626` | dropdown/card borders |
| `.bg-gray-950` | `--gray-950` → `#0A0A0A` | first viewport / mobile menu |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| `--primary-dark` | `#008060` | 48 |
| legacy/diff removed | `#800000` | 34 |
| transparent black | `#00000000` | 30 |
| `--white` | `#FFFFFF` | 12 |
| `--gray-800` | `#262626` | 5 |
| green status | `#61C454` | 5 |
| red status | `#EC6D62` | 5 |
| yellow status | `#F5C451` | 5 |
| `--primary` | `#27F795` | 3 |

### 06-8. Color Stories

**`{colors.primary}` (`#27F795`)** — Tinybird's execution green. It is used where the interface says "run this": primary CTA, active category, links, success/code invocation, and logo hover. Do not invent a softer brand tint as the main action color.

**`{colors.surface-dark}` (`#0A0A0A`)** — The page floor. It lets the green read like terminal output and makes white display type feel bright without needing a gradient.

**`{colors.text-primary}` (`#FFFFFF`)** — The hero and navigation foreground. Tinybird uses true white on black for confidence; muted explanatory copy steps down to #999999 rather than lowering opacity blindly.

**`{colors.border-dark}` (`#262626`)** — The structural hairline. Cards, dropdowns, footer blocks, and terminal chips rely on dark borders instead of elevated shadows.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token / Utility | Value | Use case |
|---|---:|---|
| `--spacing` | 4px | Tailwind v4 base spacing unit |
| `px-5` | 20px | mobile container inset |
| `md:px-6` | 24px | tablet container inset |
| `lg:px-10` | 40px | desktop container inset |
| `gap-4` | 16px | mobile CTA stack / small controls |
| `gap-6` | 24px | main grid gutter |
| `gap-8` | 32px | desktop CTA row |
| `mt-8` | 32px | first hero offset after nav |
| `md:mt-12` | 48px | section separation |
| `mb-10` | 40px | hero copy to CTA gap |
| `max-w-[1440px]` | 1440px | outer shell |
| `max-w-[720px]` | 720px | hero headline |
| `max-w-[500px]` | 500px | hero supporting text |

**주요 alias**:
- `--container-5xl` → 64rem (wide content)
- `--container-7xl` → 80rem (large content)
- `max-w-[1440px]` → homepage shell, navigation, footer, hero grid

### Whitespace Philosophy

Tinybird's whitespace is not airy luxury spacing; it is console spacing scaled up for marketing. The top shell is wide at 1440px, but hero content is tightened into 720px headline and 500px supporting copy, keeping the message centered like a command output block.

The page alternates between spacious hero breathing room and compressed terminal chips. That contrast matters: the brand sells speed and infrastructure, so large empty zones should always resolve into dense operational modules, tabs, code panes, logo strips, or feature grids.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `.rounded` | 4px | terminal chips, active category tabs |
| `--radius-md` | 6px | small UI controls |
| `--radius-lg` | 8px | standard rounded container |
| `--radius-xl` | 12px | larger panels |
| `--radius-2xl` | 16px | larger marketing cards |
| `--radius-card` | 8px | card chassis |
| `--radius-asset` | 16px | media/assets |
| `--radius-pill` | 24px | available token, not the hero CTA default |
| `.rounded-full` | extreme | icon/circular cases only |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| default | `box-shadow: none` | most chrome and cards |
| Tailwind shadow utility | `0 0.625rem 0.9375rem -0.1875rem #0000001A, 0 0.25rem 0.375rem -0.25rem #0000001A` | available utility, not dominant in hero chrome |
| focus/ring layer | Tailwind ring/shadow variables | browser-like interaction support |

Tinybird's visible structure is mostly border and contrast. Do not use a soft multi-layer SaaS shadow system as the default card language.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `--default-transition-duration` | `.15s` | standard utility transition |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | default Tailwind easing |
| `--ease-out` | `cubic-bezier(0,0,.2,1)` | nav/background transition |
| `--ease-in-out` | `cubic-bezier(.4,0,.2,1)` | hover/transform interactions |
| `.transition-colors` | color/background/border | links, nav, buttons |
| `.transition-transform` | transform/translate/scale/rotate | sticky nav, dropdown icon |
| `--animate-home-logos` | `slide 50s linear infinite` | logo strip |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: 1440px outer shell.
- **Grid type**: Tailwind CSS Grid + Flexbox.
- **Column count**: hero and repeated sections use `grid-cols-1 lg:grid-cols-12`; nav uses `grid-cols-2 lg:grid-cols-[1fr_auto_1fr]`.
- **Gutter**: `gap-6` (24px) in main grids; nav menu gap is `gap-10` (40px).

### Hero
- **Pattern Summary**: dark 1-column centered hero + 64px display + dual CTA + terminal category tabs below.
- Layout: full-width section, 12-column grid, content spans all columns and shifts to centered 10-column span on very large screens.
- Background: solid #0A0A0A / near-black; no hero image in first viewport.
- **Background Treatment**: solid dark surface with bright foreground and green execution accent. No mesh, no bokeh, no illustration-first composition.
- H1: `--text-h1` 64px / weight 400 / tracking -0.08rem; mobile 56px / tracking -0.105rem.
- Max-width: 720px headline, 500px supporting copy.

### Section Rhythm
```css
section {
  padding-inline: 20px mobile / 24px tablet / 40px desktop through container utilities;
  max-width: 1440px for inner shell;
}
#hero {
  margin-top: 32px mobile / 64px small+;
  margin-bottom: 0;
}
```

### Card Patterns
- **Card background**: #151515 / #0A0A0A family, occasionally transparent overlays.
- **Card border**: 1px solid #262626 or #353535.
- **Card radius**: 4px for terminal chips, 8px for card chassis, 16px for assets.
- **Card padding**: utility-driven, commonly 16px to 40px depending on density.
- **Card shadow**: none by default; border and surface contrast carry depth.

### Navigation Structure
- **Type**: sticky horizontal nav with centered product links and right-aligned auth CTAs.
- **Position**: sticky top shell.
- **Height**: 64px mobile / 72px desktop minimum.
- **Background**: #0A0A0A / transparent dark; dropdown uses #151515 / #262626 border layers.
- **Border**: dropdown panels use 2px dark borders; main nav relies on contrast, not a visible bottom line.

### Content Width
- **Prose max-width**: 500px for hero supporting copy.
- **Container max-width**: 1440px.
- **Sidebar width**: no homepage sidebar; footer uses multi-column grid.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | default | stacked CTA, left-aligned hero text, hamburger nav |
| Tablet | `md` / approx 768px | hero text centers, CTA row becomes horizontal |
| Desktop | `lg` / approx 1024px | nav full menu, 12-column grid, 40px container padding |
| Wide | `2lg` / source custom breakpoint | hero content becomes 10 columns centered |
| Extra wide | `96rem` observed | large footer/layout refinements |

### Touch Targets
- **Minimum tap size**: mobile sign-up button uses `h-10` (40px); hero CTA uses `py-4` (about 56px).
- **Button height (mobile)**: 40px in nav, larger primary hero CTA.
- **Input height (mobile)**: `--text-input-mobile` 24px font / 32px line-height; actual form controls not fully surfaced on homepage.

### Collapsing Strategy
- **Navigation**: full desktop menu collapses to hamburger plus sign-up button on mobile.
- **Grid columns**: `grid-cols-1` by default, `lg:grid-cols-12` on desktop.
- **Sidebar**: none on homepage.
- **Hero layout**: left-aligned on mobile, centered on md+.

### Image Behavior
- **Strategy**: responsive Next image assets, SVG logo, decorative bars in dropdown, wordmark footer crop.
- **Max-width**: constrained by 1440px shell and asset-specific widths.
- **Aspect ratio handling**: explicit image dimensions in HTML, Next image layout.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA**

```html
<a class="text-button font-mono px-6 py-4 bg-primary text-gray-950 hover:bg-primary-dark hover:text-white">
  Try for free
</a>
```

| Property | Value |
|---|---|
| Font | Roboto Mono, `--text-button` 16px / 24px |
| Background | #27F795 |
| Text | #0A0A0A |
| Hover | #008060 background + #FFFFFF text |
| Radius | none / square by default |
| Padding | 24px horizontal, 16px vertical |
| Disabled | primary bg + gray-950 text + opacity 40% |

**Link CTA**

```html
<a class="text-button font-mono bg-transparent text-primary hover:underline px-0 py-0">
  Contact sales
</a>
```

| Property | Value |
|---|---|
| Background | transparent |
| Text | #27F795 |
| Hover | underline |
| Geometry | no box, no border |

### Badges

**Terminal category chip**

```html
<button class="px-1 py-0.5 text-body-3 font-mono border rounded transition-colors">
  [Crypto / Finance]
</button>
```

| Property | Value |
|---|---|
| Font | Roboto Mono, 14px / 22px |
| Background | dark translucent panel |
| Border | 1px solid #353535 / #262626 family |
| Active | #27F795 text and border emphasis |
| Radius | 4px |

### Cards & Containers

```html
<div class="bg-gray-900 border border-gray-800 rounded-card p-6">
  <h3 class="text-h5">...</h3>
  <p class="text-body-3 text-gray-400">...</p>
</div>
```

| Property | Value |
|---|---|
| Background | #151515 / #0A0A0A family |
| Border | 1px solid #262626 |
| Radius | 8px card / 16px asset |
| Padding | 24px baseline, wider in feature sections |
| Shadow | none by default |
| Hover | color/border/background transition rather than lift |

### Navigation

```html
<nav class="sticky z-header font-mono transition-transform">
  <div class="min-h-[64px] lg:min-h-[72px] grid grid-cols-2 lg:grid-cols-[1fr_auto_1fr]">
    ...
  </div>
</nav>
```

| Property | Value |
|---|---|
| Height | 64px mobile / 72px desktop |
| Font | Roboto Mono |
| Shell | 1440px max-width, 20/24/40px horizontal padding |
| Links | white default, #27F795 hover |
| Dropdown | #151515 panel, #262626 border, 3-column groups |
| Mobile | hamburger menu + sign-up button |

### Inputs & Forms

> Homepage does not expose a full form field system in the visible hero. Extracted input typography tokens still define the expected scale.

| Property | Value |
|---|---|
| `--text-input` | 36px / 40px |
| `--text-input-mobile` | 24px / 32px |
| Reset background | transparent (`#00000000`) |
| Focus/error states | not surfaced in homepage capture |

### Hero Section

```html
<section id="hero" class="w-full mb-0 mt-8 sm:mt-16">
  <h1 class="max-w-[720px] text-h1-mobile md:text-h1 md:mx-auto">
    Ship fast over a <br /> Managed ClickHouse
  </h1>
</section>
```

| Property | Value |
|---|---|
| Background | #0A0A0A |
| H1 | 64px desktop / 56px mobile, weight 400 |
| Copy | 18px / 32px, #999999 |
| CTA row | stacked mobile, horizontal md+ |
| Below-hero module | terminal-style category tabs |

### 13-2. Named Variants

- **button-primary** — #27F795 square CTA, #0A0A0A text, 24px x 16px padding.
- **button-primary-hover** — #008060 background with white text; do not lighten the green on hover.
- **button-link-green** — transparent, #27F795 text, underline on hover.
- **nav-dropdown-item** — dark row, sans body title, mono/gray section labels, border-left green hover indicator.
- **tab-terminal-chip** — bracketed label, mono 14px, #353535 border, active #27F795.
- **social-square-button** — footer icon square, white/10 background, white/20 hover.

### 13-3. Signature Micro-Specs

#### terminal-bracket-selector

```yaml
terminal-bracket-selector:
  description: "Terminal punctuation turns navigation and category tabs into executable selectors."
  technique: "Roboto Mono 14px/22px labels, literal '[' and ']' punctuation, 1px #353535/#262626 border, 4px radius, active color/border #27F795"
  applied_to: ["{component.tab-terminal-chip}", "{component.nav-dark-grid}"]
  visual_signature: "The UI reads like a CLI choice list rather than a marketing filter bar."
```

#### green-to-dark-execution-button

```yaml
green-to-dark-execution-button:
  description: "The primary CTA behaves like a run command that deepens on hover instead of glowing brighter."
  technique: "background #27F795 with #0A0A0A text, padding 16px 24px, radius 0px, transition .15s cubic-bezier(.4,0,.2,1), hover #008060 + #FFFFFF"
  applied_to: ["{component.button-primary}", "{component.button-primary-hover}"]
  visual_signature: "A square neon-green terminal key that becomes darker and more operational on interaction."
```

#### border-routed-dark-depth

```yaml
border-routed-dark-depth:
  description: "Depth is created through routed hairlines and near-black surface steps, not card elevation."
  technique: "page #0A0A0A, panel #151515, border 1px solid #262626 or #353535, card radius 8px, shadow none by default"
  applied_to: ["{component.nav-dark-grid}", "{component.tab-terminal-chip}", "{component.social-square-button}"]
  visual_signature: "Panels feel etched into a circuit board instead of floating above the page."
```

#### mono-control-plane

```yaml
mono-control-plane:
  description: "Interaction chrome switches into Roboto Mono while prose remains Roboto."
  technique: "nav/button/chip font-family Roboto Mono, body/display font-family Roboto, button scale 16px/24px, chip scale 14px/22px"
  applied_to: ["{component.nav-dark-grid}", "{component.button-primary}", "{component.tab-terminal-chip}"]
  visual_signature: "The page visibly separates public marketing copy from developer-owned controls."
```

#### tight-regular-hero-display

```yaml
tight-regular-hero-display:
  description: "Hero scale stays large and regular-weight, but compressed enough to feel engineered."
  technique: "Roboto 64px/72px desktop or 56px/64px mobile, font-weight 400, letter-spacing -0.08rem desktop / -0.105rem mobile, max-width 720px"
  applied_to: ["{component.hero-section}"]
  visual_signature: "The headline feels like a precise system banner, not a heavy startup slogan."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | direct shipping promise + concrete infrastructure noun | "Ship fast over a Managed ClickHouse" |
| Primary CTA | low-friction action, short verb phrase | "Try for free" |
| Secondary CTA | enterprise route, plain wording | "Contact sales" |
| Subheading | describes data infrastructure and business outcome in one sentence | "The data infrastructure and tooling to ship enterprise grade analytical features..." |
| Tone | developer-first, concrete, infrastructure-literate, low fluff | Product nav items name real capabilities: Managed ClickHouse, Kafka Connector, Branches |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Tinybird — copy into your root stylesheet */
:root {
  /* Fonts */
  --tb-font-family:       "Roboto", "Roboto Fallback", system-ui, sans-serif;
  --tb-font-family-mono:  "Roboto Mono", "Roboto Mono Fallback", ui-monospace, monospace;
  --tb-font-family-code:  "Fira Mono", "Fira Mono Fallback", ui-monospace, monospace;
  --tb-font-weight-normal: 400;
  --tb-font-weight-bold:   700;

  /* Brand */
  --tb-color-brand-500: #27F795;
  --tb-color-brand-700: #008060;

  /* Surfaces */
  --tb-bg-page:    #0A0A0A;
  --tb-bg-panel:   #151515;
  --tb-border:     #262626;
  --tb-border-2:   #353535;
  --tb-text:       #FFFFFF;
  --tb-text-muted: #999999;

  /* Code accents */
  --tb-code-identifier: #00C1FF;
  --tb-code-value:      #FC9F5B;
  --tb-code-error:      #FF8389;

  /* Type */
  --tb-h1: 4rem;
  --tb-h1-leading: 4.5rem;
  --tb-h1-tracking: -0.08rem;
  --tb-body-1: 1.125rem;
  --tb-body-1-leading: 2rem;

  /* Space and shape */
  --tb-space-unit: 0.25rem;
  --tb-container: 1440px;
  --tb-radius-chip: 0.25rem;
  --tb-radius-card: 0.5rem;
  --tb-radius-asset: 1rem;
}

body {
  margin: 0;
  background: var(--tb-bg-page);
  color: var(--tb-text);
  font-family: var(--tb-font-family);
  font-weight: var(--tb-font-weight-normal);
}

.tb-shell {
  max-width: var(--tb-container);
  margin-inline: auto;
  padding-inline: 20px;
}
@media (min-width: 768px) { .tb-shell { padding-inline: 24px; } }
@media (min-width: 1024px) { .tb-shell { padding-inline: 40px; } }

.tb-hero-title {
  max-width: 720px;
  font-size: var(--tb-h1);
  line-height: var(--tb-h1-leading);
  letter-spacing: var(--tb-h1-tracking);
  font-weight: 400;
}

.tb-button-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 16px 24px;
  border: 0;
  border-radius: 0;
  background: var(--tb-color-brand-500);
  color: var(--tb-bg-page);
  font-family: var(--tb-font-family-mono);
  font-size: 1rem;
  line-height: 1.5rem;
  transition: all .15s cubic-bezier(.4,0,.2,1);
}
.tb-button-primary:hover {
  background: var(--tb-color-brand-700);
  color: var(--tb-text);
}

.tb-chip {
  border: 1px solid var(--tb-border-2);
  border-radius: var(--tb-radius-chip);
  color: var(--tb-text-muted);
  background: rgba(53, 53, 53, .3);
  font-family: var(--tb-font-family-mono);
}
.tb-chip[aria-selected="true"] {
  color: var(--tb-color-brand-500);
  border-color: var(--tb-color-brand-500);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Tinybird-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#27F795',
        'primary-dark': '#008060',
        secondary: '#2D27F7',
        'secondary-light': '#00C1FF',
        gray: {
          50: '#F6F7F9',
          100: '#E8E9ED',
          200: '#D9D9D9',
          300: '#999999',
          400: '#8D8D8D',
          500: '#636679',
          600: '#3C3C3C',
          700: '#353535',
          800: '#262626',
          900: '#151515',
          950: '#0A0A0A',
        },
      },
      fontFamily: {
        sans: ['Roboto', 'Roboto Fallback', 'system-ui'],
        mono: ['Roboto Mono', 'Roboto Mono Fallback', 'ui-monospace'],
      },
      borderRadius: {
        DEFAULT: '0.25rem',
        card: '0.5rem',
        asset: '1rem',
        pill: '1.5rem',
      },
      transitionDuration: {
        DEFAULT: '.15s',
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
| Brand primary | `{colors.primary}` | `#27F795` |
| Brand hover | `{colors.primary-dark}` | `#008060` |
| Background | `{colors.surface-dark}` | `#0A0A0A` |
| Panel | `{colors.surface-panel}` | `#151515` |
| Text primary | `{colors.text-primary}` | `#FFFFFF` |
| Text muted | `{colors.text-muted}` | `#999999` |
| Border | `{colors.border-dark}` | `#262626` |
| Code identifier | `{colors.code-identifier}` | `#00C1FF` |
| Code value | `{colors.code-value}` | `#FC9F5B` |
| Error | `{colors.error}` | `#FF8389` |

### Example Component Prompts

#### Hero Section
```text
Tinybird 스타일 히어로 섹션을 만들어줘.
- 배경: #0A0A0A, gradient 없음
- H1: Roboto, 64px/72px, weight 400, tracking -0.08rem, max-width 720px
- 서브텍스트: #999999, 18px/32px, max-width 500px
- CTA 버튼: Roboto Mono, 배경 #27F795, 텍스트 #0A0A0A, hover #008060 + #FFFFFF
- 버튼 radius: 0px, padding 16px 24px
- 아래에는 mono terminal chip row를 두고 active chip만 #27F795
```

#### Card Component
```text
Tinybird 스타일 카드 컴포넌트를 만들어줘.
- 배경: #151515 또는 #0A0A0A, border: 1px solid #262626
- radius: 8px, shadow 없음
- 제목: Roboto, 24px/32px 또는 16px/24px, weight 400/500
- 메타/컨트롤: Roboto Mono
- hover 시 transform 대신 border-color/background/color만 150ms 전환
```

#### Badge
```text
Tinybird 스타일 탭 배지를 만들어줘.
- font: Roboto Mono, 14px/22px
- label은 [SaaS / Dashboards]처럼 bracket syntax 사용
- padding: 2px 4px, radius: 4px
- 기본: bg rgba(53,53,53,.3), border #353535, text #999999
- active: color #27F795, border #27F795
```

#### Navigation
```text
Tinybird 스타일 상단 네비게이션을 만들어줘.
- 높이: 64px mobile / 72px desktop
- max-width: 1440px, padding 20/24/40px
- font: Roboto Mono, 링크는 white, hover #27F795
- Product와 Resources는 [+] bracket toggle로 표현
- 우측 Sign in은 green text link, Sign up은 #27F795 square button
```

### Iteration Guide

- **색상 변경 시**: #27F795와 #008060의 관계를 유지한다. hover를 밝게 하지 말고 더 깊은 green으로 내린다.
- **폰트 변경 시**: Roboto Mono interaction layer를 보존한다. 전체를 Inter로 바꾸면 Tinybird가 사라진다.
- **여백 조정 시**: 4px base unit과 1440px shell을 유지한다.
- **카드 추가 시**: shadow보다 #262626 border를 먼저 사용한다.
- **다크 모드**: default가 dark다. light theme을 기본으로 뒤집지 않는다.
- **반응형**: mobile에서는 CTA stack + hamburger, md+에서 centered hero and CTA row.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #0A0A0A as the dominant page floor for first-viewport work.
- Use #27F795 for executable actions: CTA, active state, code invocation, and key hover states.
- Keep buttons square or nearly square; Tinybird's CTA is not a pill.
- Split fonts by role: Roboto for display/body, Roboto Mono for controls/nav/chips.
- Use #262626 and #353535 hairlines to create depth.
- Keep display type regular-weight and tightly tracked.
- Use bracket syntax in terminal-like selectors where appropriate.
- Let code colors (#00C1FF, #FC9F5B, #FF8389) appear only in code/data surfaces.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#0A0A0A` 사용.
- 본문/hero 바닥을 `#151515` panel tone으로 두지 말 것 — hero floor는 더 깊은 `#0A0A0A` 사용.
- CTA를 `#2D27F7` secondary blue로 두지 말 것 — 대신 `#27F795` 사용.
- CTA hover를 `#61C454` status green으로 두지 말 것 — 대신 `#008060` 사용.
- primary CTA 텍스트를 `#FFFFFF`로 시작하지 말 것 — 기본 상태는 `#0A0A0A` on `#27F795`, hover에서만 white.
- border를 `#E8E9ED` 같은 light gray로 두지 말 것 — dark chrome에서는 `#262626` 또는 `#353535` 사용.
- hero H1에 `font-weight: 700`을 기본으로 쓰지 말 것 — Tinybird hero는 400과 tight tracking이 맞다.
- 모든 UI를 sans-serif로 만들지 말 것 — nav/button/chip은 Roboto Mono 계열이어야 한다.
- CTA를 `border-radius: 999px` pill로 만들지 말 것 — hero primary button은 square-edge grammar다.
- 카드에 큰 `box-shadow`를 넣지 말 것 — border/surface contrast로 깊이를 만든다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No soft SaaS blue** — blue exists as code/secondary accent, not as the brand action color.
- **No default light-mode homepage** — first-viewport identity is dark-first.
- **No pill CTA as hero default** — square buttons keep the terminal/control-plane mood.
- **No pastel gradient hero** — the hero is solid dark, not mesh or aurora.
- **No heavy display weight** — the main headline avoids 700+ bravado.
- **No broad decorative shadows** — chrome is drawn with borders and dark fills.
- **No playful illustration-first composition** — the homepage leads with type and operational UI.
- **No second competing brand color** — #27F795 carries action and recognition.
- **No generic marketing nav typography** — mono nav is part of the brand, not an implementation detail.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Cookie banner present in screenshot** — the captured hero includes the cookie consent bar at the bottom. Hero interpretation is based on the visible area above it plus HTML structure.
- **Homepage-only capture** — product, docs, signup, dashboard, and app surfaces were not navigated. Form validation, loading, and complex product UI states remain unmeasured.
- **CSS source is bundled Tailwind output** — class composition is observable, but source component names and design-token ownership are not.
- **Some chromatic frequency is contaminated by code/demo/status colors** — #61C454, #EC6D62, #F5C451, #00C1FF, and #FC9F5B are treated as code/status accents, not brand colors.
- **Dark theme mapping is strong, light counterpart is incomplete** — light grays exist in tokens, but the captured first viewport is dark and does not prove a full light theme.
- **Dropdown behavior observed through HTML/CSS, not interactive browser stepping** — open-state animation and precise clip-path timing are inferred from inline styles/classes.
- **Exact breakpoint names are Tailwind/custom-class inferred** — concrete `md/lg/2lg` behavior is visible in classes, but the project config file was not read.
- **Motion JS not audited** — CSS transition and animation tokens were inspected, but scroll-triggered or React runtime animation logic was not traced.
