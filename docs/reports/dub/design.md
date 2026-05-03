---
schema_version: 3.2
slug: dub
service_name: Dub
site_url: https://dub.co
fetched_at: 2026-05-03T06:29:37Z
default_theme: light
brand_color: "#000000"
primary_font: Inter
font_weight_normal: 400
token_prefix: dub

bold_direction: Precision Utility
aesthetic_category: refined-saas
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Next.js marketing page with reusable Tailwind utilities, semantic rgb tokens, tabbed hero product UI, and component states visible in CSS/HTML."

colors:
  bg-default-light: "#FFFFFF"
  bg-muted-light: "#FAFAFA"
  bg-subtle-light: "#F5F5F5"
  bg-emphasis-light: "#E5E5E5"
  bg-inverted-light: "#171717"
  border-default-light: "#D4D4D4"
  border-muted-light: "#F5F5F5"
  content-default-light: "#404040"
  content-emphasis-light: "#171717"
  accent-purple: "#855AFC"
  info-blue: "#1D4ED8"
  success-green: "#15803D"
  attention-orange: "#C2410C"
  error-red: "#B91C1C"

typography:
  display: "satoshi, satoshi Fallback"
  body: "Inter, Inter Fallback"
  mono: "GeistMono, ui-monospace"
  ladder:
    - { token: h1-mobile, size: "36px", weight: 500, line_height: "40px", tracking: "-0.025em" }
    - { token: h1-desktop, size: "48px", weight: 500, line_height: "1.15", tracking: "-0.025em" }
    - { token: body-large, size: "20px", weight: 400, line_height: "28px", tracking: "0" }
    - { token: body, size: "16px", weight: 400, line_height: "24px", tracking: "0" }
    - { token: button, size: "14px", weight: 500, line_height: "20px", tracking: "0" }
  weights_used: [100, 300, 400, 500, 600, 700, 800, 900]
  weights_absent: []

components:
  button-primary: { bg: "#000000", fg: "#FFFFFF", radius: "8px", padding: "8px 20px", hover_ring: "4px #E5E5E5" }
  button-secondary: { bg: "#FFFFFF", fg: "#737373", border: "#E5E5E5", radius: "8px", padding: "8px 20px" }
  hero-tab-active: { bg: "#FFFFFF", fg: "#262626", border: "#E5E5E5", radius: "8px", shadow: "drop-shadow-sm" }
  hero-tab-inactive: { bg: "#F5F5F5", fg: "#525252", border: "transparent", radius: "8px" }
---

# DESIGN.md — Dub (Codex Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Dub is not a purple SaaS billboard; it is a revenue workbench laid on a drafting table. The page is mostly `#FFFFFF` (`{colors.bg-default-light}`), but the white is ruled with faint `#E5E5E5` (`{colors.bg-emphasis-light}`) grid lines like an engineer's cutting mat. Marketing copy does not float in empty air. It sits inside a measured coordinate system, then hands the eye down to the product UI as if the promise has been checked against instrumentation.

The hero is a precision funnel with almost no scenic background. First a tiny announcement pill, then a compact Satoshi headline, then one sentence, then the black primary button. No second brand color arrives to rescue the composition. `#171717` (`{colors.content-emphasis-light}`) and `#000000` do the anchoring, while the chromatic colors are kept in small status capsules. Dub's brand color is less a hue than a rule: black for commitment, muted gray for structure, color only when the product needs to label a job.

The signature move is the bridge from copy to proof. The Short Links, Conversion Analytics, and Affiliate Programs tabs sit over a curved notch like labeled instrument switches above a dashboard bay. The product screenshot below is not a decorative card; it is a receipt. The page has little interest in looking like a "site" for its own sake. It erases the stage just enough that the app surface can become the evidence.

Dub's grid behaves like a subway map for clicks: thin rails, compact labels, and colored route markers that only appear at decision points. Orange, green, purple, and blue are not campaign paint; they are tiny operational tags. Scaling `#855AFC` (`{colors.accent-purple}`) into a hero gradient would break the system because Dub's color is meant to be read at icon-chip scale, not billboard scale.

Typography adds the editorial polish without turning ceremonial. Satoshi at `font-weight: 500` gives the headline an inked, compact weight, while Inter keeps the controls utilitarian. The headline feels pressed into the page rather than shouted from it; negative tracking makes the words lock together like a product label on a precision tool.

Motion is the startup sequence of software, not theater lighting. `animate-slide-up-fade` brings the pill, H1, copy, CTAs, tabs, and product panel online in 100-500ms steps. The site does not perform delight as decoration; it lets the interface wake up in order.

### Key Characteristics

- White-first marketing surface with visible but very low-contrast grid infrastructure.
- Black primary action as the true brand color; chromatic colors are semantic chips.
- Centered hero copy constrained to a narrow column, not a wide editorial spread.
- Product UI proof appears immediately below the fold, framed by a curved notch transition.
- Primary and secondary buttons share geometry but split sharply by surface: black filled vs white bordered.
- Satoshi display + Inter body + GeistMono code stack loaded through Next.js font classes.
- Tailwind utility system with semantic rgb tokens for light and dark themes.
- Rounded `8px` controls dominate; pill radius is reserved for announcement capsules.
- Staggered slide-up fade gives the page a measured launch sequence.
- Logo wall colors and SVG internals are not brand palette evidence.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Precision Utility
> **Aesthetic Category**: refined-saas
> **Signature Element**: 이 사이트는 **grid-backed conversion hero with tabbed product proof**으로 기억된다.
> **Code Complexity**: high — Tailwind utilities, semantic rgb tokens, responsive nav, staggered animation, tabbed hero UI, and layered product screenshot framing combine into a non-trivial system.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Dub처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter", "Inter Fallback", system-ui, sans-serif;
  font-weight: 400;
}
h1 {
  font-family: "satoshi", "satoshi Fallback", system-ui, sans-serif;
  font-weight: 500;
  letter-spacing: -0.025em;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #171717; --muted: #525252; --grid: #E5E5E5; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #000000; --brand-hover: #262626; }
```

**절대 하지 말아야 할 것 하나**: Dub를 보라/파랑 gradient SaaS로 만들지 말 것. 실제 히어로는 `#FFFFFF` 바탕, `#000000` CTA, `#E5E5E5` hairline grid가 핵심이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://dub.co` |
| Fetched | 2026-05-03T06:29:37Z |
| Extractor | cached phase1 reuse; existing HTML/CSS/screenshot |
| HTML size | 698756 bytes (Next.js SSR/RSC payload) |
| CSS files | 2 external CSS files, total 290319 bytes |
| Token prefix | `dub` |
| Method | CSS custom properties, HTML utility classes, screenshot sampling, phase1 JSON reuse |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js app router style output with RSC payload and hashed `_next/static` assets.
- **Design system**: Dub/Tailwind semantic token layer — prefix is not a single namespace, but reusable variables include `--bg-*`, `--border-*`, `--content-*`, `--font-*`, and component aliases such as `--card-foreground`.
- **CSS architecture**:
  ```text
  core semantic rgb     (--bg-default, --content-emphasis)    raw "R G B" triplets
  utility classes       (.text-neutral-600, .rounded-lg)      Tailwind v3.4.4 generated utilities
  component classes     (button/tab/nav/product-preview)      utility-class composition in HTML
  font variables        (--font-inter, --font-satoshi)        Next font variable classes
  ```
- **Class naming**: Tailwind utility composition with arbitrary values such as `max-w-[940px]`, `[--offset:20px]`, and `max-w-[min(700px,calc(100vw-2rem))]`.
- **Default theme**: light (bg = `#FFFFFF`).
- **Font loading**: `@font-face` with Next.js hashed WOFF2 assets; Satoshi, Inter, and GeistMono each include fallback/variable classes.
- **Canonical anchor**: top marketing homepage hero and product proof module.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `satoshi` (loaded from site WOFF2, variable 300-900)
- **Body font**: `Inter` (loaded from site WOFF2, variable 100-900)
- **Code font**: `GeistMono` (loaded from site WOFF2, variable 100-900)
- **Weight normal / bold**: `400` / `600`, with `500` used heavily for buttons and hero display.

```css
:root {
  --font-satoshi: "satoshi", "satoshi Fallback";
  --font-inter: "Inter", "Inter Fallback";
  --font-geist-mono: "GeistMono", ui-monospace, SFMono-Regular, Roboto Mono, Menlo, monospace;
}
.font-default { font-family: var(--font-inter), system-ui, sans-serif; }
.font-display { font-family: var(--font-satoshi), system-ui, sans-serif; }
code, pre { font-family: var(--font-geist-mono, ui-monospace), ui-monospace, monospace; }
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Satoshi** is the display signature. If unavailable, use **Inter Tight** or **Geist** at weight `500`, with `letter-spacing: -0.025em` on H1 to preserve the compact Dub headline.
- **Inter** can be substituted with system `ui-sans-serif`, but keep button text at `14px / 500`; raising it to `600` makes the navigation and CTA feel heavier than the source.
- **GeistMono** is only needed for code/technical UI fragments. Do not use it as decorative marketing type.
- The measured fallback behavior includes metric overrides for `satoshi Fallback` and `Inter Fallback`; a naive Arial fallback will look taller unless line-height is tightened slightly.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Hero H1 mobile | `36px` (`text-4xl`) | `500` | `40px` | `-0.025em` |
| Hero H1 desktop | `48px` (`sm:text-5xl`) | `500` | `1.15` | `-0.025em` |
| Hero body desktop | `20px` (`sm:text-xl`) | `400` | `28px` | `0` |
| Body | `16px` | `400` | `24px` | `0` |
| Nav/control | `14px` | `500` | `20px` | `0` |
| Badge/pill | `12-14px` | `400-500` | compact | `0` |

> ⚠️ Dub's display voice is medium-weight Satoshi, not bold Inter. The most common mistake is making the hero heavier and more generic.

### Principles
<!-- SOURCE: manual -->

1. Display type is compact but not aggressive: `font-weight: 500` plus `letter-spacing: -0.025em` does the work.
2. Body copy stays neutral and readable; it uses Inter at normal weight with muted gray rather than brand color.
3. Buttons and nav labels use `14px / 500`, giving controls precision without making the whole page shout.
4. The typography hierarchy is shallow: hero H1, large body, controls. Dub avoids many intermediate marketing heading levels in the first fold.
5. Code/technical typography is quarantined to product-like details through GeistMono; it does not become the brand voice.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (5 steps)
<!-- SOURCE: auto+manual -->

| Token | Hex |
|---|---|
| `--dub-brand-000` | `#000000` |
| `--dub-brand-171717` | `#171717` |
| `--dub-brand-262626` | `#262626` |
| `--dub-brand-404040` | `#404040` |
| `--dub-brand-white` | `#FFFFFF` |

### 06-2. Brand Dark Variant
<!-- SOURCE: auto -->

| Token | Hex |
|---|---|
| `--bg-default` dark | `#000000` |
| `--bg-muted` dark | `#171717` |
| `--content-default` dark | `#D4D4D4` |
| `--content-emphasis` dark | `#FAFAFA` |
| `--border-default` dark | `#525252` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto -->

| Step | Light | Dark |
|---|---|---|
| bg default | `#FFFFFF` | `#000000` |
| bg muted | `#FAFAFA` | `#171717` |
| bg subtle | `#F5F5F5` | `#262626` |
| bg emphasis | `#E5E5E5` | `#404040` |
| border default | `#D4D4D4` | `#525252` |
| content default | `#404040` | `#D4D4D4` |
| content emphasis | `#171717` | `#FAFAFA` |

### 06-4. Accent Families
<!-- SOURCE: auto+manual -->

| Family | Key step | Hex |
|---|---|---|
| Purple | affiliate chip / frequent chromatic candidate | `#855AFC` |
| Blue | analytics / info | `#3A8BFD` |
| Green | conversion/success | `#15803D` / `#5CFF80` |
| Orange | short-links chip / attention | `#F4950C` / `#C2410C` |
| Red | error/demo artifact | `#B91C1C` / `#F35066` |

### 06-5. Semantic
<!-- SOURCE: auto -->

| Token | Hex | Usage |
|---|---|---|
| `--bg-default` | `#FFFFFF` | page background |
| `--bg-muted` | `#FAFAFA` | subtle surfaces |
| `--bg-subtle` | `#F5F5F5` | tab inactive, grid band |
| `--bg-emphasis` | `#E5E5E5` | hairlines and stronger separators |
| `--bg-inverted` | `#171717` | dark CTA/surface |
| `--content-default` | `#404040` | body copy |
| `--content-subtle` | `#737373` | secondary text |
| `--content-muted` | `#A3A3A3` | muted icons/text |
| `--content-emphasis` | `#171717` | headings and strong labels |
| `--bg-info` | `#BFDBFE` | info background token |
| `--content-info` | `#1D4ED8` | info foreground token |
| `--bg-success` | `#DCFCE7` | success background token |
| `--content-success` | `#15803D` | success foreground token |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--font-inter` | `"Inter", "Inter Fallback"` | body/default UI |
| `--font-satoshi` | `"satoshi", "satoshi Fallback"` | display |
| `--font-geist-mono` | `GeistMono, ui-monospace...` | code/technical |
| `--card-foreground` | component alias, unresolved in phase1 | card text inheritance |
| `--popover-foreground` | component alias, unresolved in phase1 | popover text inheritance |
| `--tw-prose-body` | `#404040` | prose body |
| `--tw-prose-headings` | `#171717` | prose headings |
| `--tw-prose-invert-body` | `#D4D4D4` | dark prose body |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto -->

| Token | Hex | Frequency |
|---|---|---|
| transparent black | `#00000000` | 83 |
| white | `#FFFFFF` | 40 |
| black alpha 67% | `#000000AA` | 36 |
| neutral-200 | `#E5E5E5` | 29 |
| purple accent | `#855AFC` | 23 |
| black alpha 20% | `#00000033` | 22 |
| off-white | `#FAFAFA` | 21 |
| neutral-900 | `#171717` | 20 |
| blue accent | `#3A8BFD` | 19 |
| black | `#000000` | 19 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.bg-default-light}` (`#FFFFFF`)** — The primary field. Dub's homepage depends on white space as an operating surface, then draws the system with borders, grid lines, and product UI rather than colored sections.

**`{colors.content-emphasis-light}` (`#171717`)** — The ink and near-black anchor. It is used for headings, logo treatment, and the inverted CTA family; this is the closest thing Dub has to a brand color.

**`{colors.bg-emphasis-light}` (`#E5E5E5`)** — The hairline infrastructure. It supports the grid, borders, disabled edges, and secondary button outline. Too much contrast here turns Dub into a wireframe.

**`{colors.accent-purple}` (`#855AFC`)** — A semantic accent, not a broad brand wash. It appears alongside orange/green/blue in product-feature chips and SVG details; it should stay small.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `px-3` | `12px` | nav inner horizontal padding |
| `px-4` | `16px` | container and grid-section padding |
| `px-5` | `20px` | primary/secondary CTA horizontal padding |
| `py-2` | `8px` | CTA and tab vertical padding |
| `mt-5` | `20px` | hero headline/body spacing |
| `mt-10` | `40px` | hero copy to CTA group |
| `h-14` | `56px` | desktop nav height |
| `h-16` | `64px` | curved tab bridge height |
| `max-w-screen-lg` | `1024px` | nav/container width |
| `max-w-[940px]` | `940px` | product preview width |
| `max-w-[1200px]` | `1200px` | broader content utilities |

**주요 alias**:
- `grid-section` → full-width bands with `px-4`, border grid, and centered `max-w-grid-width` inner rail.
- `container` → `width:100%; margin auto; padding-left/right:1rem`.

### Whitespace Philosophy
<!-- SOURCE: manual -->

Dub uses whitespace like a measurement grid. The top hero leaves a wide vertical pause after navigation, but the empty area is lightly ruled so it feels intentional rather than blank. The CTA group sits close enough to the H1/body to read as one conversion module, then the product preview begins after a large `mt-10` and a curved transition.

The page alternates between airy marketing copy and dense product evidence. Copy modules are centered and narrow; the app mockup is much wider at roughly `940px`, because it needs to prove the software is real. That ratio is the core spacing move: narrow promise, wide proof.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| `rounded-lg` | `8px` | CTA buttons, tabs, app UI controls |
| `rounded-xl` | `12px` | larger cards/panels |
| `rounded-md` | `6px` | compact inner controls |
| `rounded` | `4px` | tiny icon chips |
| `rounded-full` | `9999px` | announcement pill and circular badges |
| custom | `5px`, `10px`, `11px`, `12px`, `15px` | product screenshot internals and SVG/UI details |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `shadow-sm` | Tailwind ring/shadow variable stack | CTA buttons and hero tab elevation |
| `drop-shadow-sm` | filter drop shadow | active tab shell |
| `drop-shadow-md` | filter drop shadow | colored tab icon chips |
| `shadow-lg/xl` | Tailwind variable stack | larger panels where used |
| inset highlight | `inset 0 1 0 0 #0000001a` | subtle pressed/inset detail |

Dub keeps chrome shadows light. Depth mostly comes from borders, opacity, and the product screenshot itself.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `animate-slide-up-fade` | custom keyframe with `[--offset:*]` | hero pill, H1, body, CTA, tabs |
| `[animation-delay:100ms]` | 100ms | H1 entrance |
| `[animation-delay:200ms]` | 200ms | body entrance |
| `[animation-delay:300ms]` | 300ms | CTA group entrance |
| `[animation-delay:400-500ms]` | 400-500ms | feature tab entrance |
| `duration-100` | 100ms | arrow hover nudge |
| `duration-150` | 150ms | tab color transitions |
| `duration-300` | 300ms | tab panel opacity transition |
| `motion-reduce:animate-fade-in` | reduced motion fallback | accessibility |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: navigation at `1024px`; product proof at `940px`; broader utilities include `1200px` and `1400px`.
- **Grid type**: Tailwind `grid`/`flex` composition. Hero text is centered flex/stack; lower proof uses tabbed absolute panels.
- **Column count**: first fold is one-column centered. Product preview itself simulates a dashboard multi-column layout.
- **Gutter**: common gutters are `16px` (`gap-4`) and `12px` for compact nav/control groups.

### Hero
- **Pattern Summary**: `~60vh + faint grid + centered H1 + dual CTA + tabbed product proof below`.
- Layout: centered announcement pill, H1, paragraph, CTA group; product UI proof begins in the next band.
- Background: `#FFFFFF` top field with low-contrast grid lines; lower proof band uses `#F5F5F5` / `#FAFAFA` surfaces.
- **Background Treatment**: solid white plus hairline grid and curved SVG notch; no hero image, no full-bleed gradient.
- H1: `36px` mobile, `48px` desktop / weight `500` / tracking `-0.025em`.
- Max-width: text block is visually around `640-720px`; product proof is `940px`.

### Section Rhythm

```css
.hero-copy {
  max-width: 720px;
  margin-inline: auto;
  text-align: center;
}
.grid-section {
  padding-inline: 16px;
  border-block: 1px solid #E5E5E5;
  background: #F5F5F5;
}
.product-proof {
  max-width: 940px;
  margin-inline: auto;
  margin-top: 24px;
}
```

### Card Patterns
- **Card background**: `#FFFFFF` or `#FAFAFA`.
- **Card border**: `1px solid #E5E5E5` / `#D4D4D4` depending emphasis.
- **Card radius**: `8px` for controls, `12px` for panels.
- **Card padding**: `12-24px` compact; app mockup internals vary.
- **Card shadow**: usually `shadow-sm` or drop-shadow on small chips; no heavy marketing elevation.

### Navigation Structure
- **Type**: horizontal desktop nav with dropdown triggers; mobile accordion menu appears in HTML.
- **Position**: `sticky inset-x-0 top-0 z-30`.
- **Height**: `56px`.
- **Background**: transparent/white over the page with border transition layer.
- **Border**: bottom border starts transparent, with `border-neutral-*` available for scrolled states.

### Content Width
- **Prose max-width**: hero/body around `640-720px`.
- **Container max-width**: `1024px` for nav; `940px` for product proof; occasional `1200px`.
- **Sidebar width**: not a marketing layout sidebar; sidebar appears only inside the product mockup.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Tiny | `280px`, `281px`, `360px`, `420px`, `450px` | special cases for auth links and small controls |
| Mobile / sm | `640px` | Tailwind small breakpoint |
| Tablet / md | `768px` | hero tabs and mobile nav behavior change |
| Desktop / lg | `1024px` | desktop nav/container behaviors |
| Wide / xl | `1280px`, `1400px` | max-width and larger composition constraints |

### Touch Targets
- **Minimum tap size**: not directly measured across all states; CTA vertical padding gives about `38-40px`, nav height is `56px`.
- **Button height (mobile)**: CTA uses `py-2`, `text-sm`, border; visually just under 44px.
- **Input height (mobile)**: product screenshot inputs are embedded, not live homepage form fields.

### Collapsing Strategy
- **Navigation**: desktop horizontal nav; mobile HTML includes accordion-style list and hides some auth links below `281px`.
- **Grid columns**: first fold remains one-column; product proof width clamps with `max-w-[min(700px,calc(100vw-2rem))]` for tab bridge.
- **Sidebar**: no page sidebar; app mockup side rail is part of image/UI preview.
- **Hero layout**: centered stack stays centered; typography steps from `36px` to `48px` at `sm`.

### Image Behavior
- **Strategy**: product UI preview, logos, and flags are preloaded; hero proof uses absolute tab panels.
- **Max-width**: product preview around `940px`; bridge around `min(700px, calc(100vw - 2rem))`.
- **Aspect ratio handling**: proof panel uses fixed heights `380px` mobile and `580px` desktop.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA**

```html
<a class="border px-5 py-2 text-sm font-medium shadow-sm transition-all hover:ring-4 hover:ring-neutral-200 border-black bg-black text-white hover:bg-neutral-800 rounded-lg">
  Start for free
</a>
```

| Property | Value |
|---|---|
| Background | `#000000` |
| Text | `#FFFFFF` |
| Hover bg | `#262626` / neutral-800 |
| Radius | `8px` |
| Padding | `8px 20px` |
| Font | `14px / 500` |
| Hover | `ring: 4px #E5E5E5` |

**Secondary CTA**

```html
<a class="border px-5 py-2 text-sm font-medium shadow-sm transition-all hover:ring-4 hover:ring-neutral-200 border-neutral-200 bg-white hover:border-neutral-400 hover:text-neutral-800 text-neutral-500 rounded-lg">
  Get a demo
</a>
```

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Border | `#E5E5E5` |
| Text | `#737373` |
| Hover border | `#A3A3A3` approx neutral-400 |
| Radius | `8px` |

### Badges

**Announcement pill**

- `rounded-full`, border, compact segmented content.
- Left message uses `text-neutral-800`; right action uses `text-neutral-500`.
- Arrow sits in a small `bg-neutral-100` circular chip and nudges on hover.

**Feature tab icon chips**

- Small `16px` square-ish chip inside each tab.
- Orange/green/purple backgrounds communicate product categories.
- Icon chip uses `border-black/5`, `drop-shadow-md`, and `group-hover:scale-110`.

### Cards & Containers

- Marketing proof container uses `grid-section` with `border-y`, `border-x` inner rail, `bg-neutral-100`.
- Product UI mockup is a wide white panel with faint app chrome, internal borders, and low opacity background content.
- Active hero tab is a compact white card: `rounded-lg`, `border-neutral-200`, `drop-shadow-sm`.
- Inactive tabs are flat neutral pills: `bg-neutral-100`, transparent border on desktop, muted text.

### Navigation

- Logo left, center nav links, auth buttons right.
- Nav height is `56px`; inner wrapper is `max-w-screen-lg`.
- Dropdown triggers use text labels plus chevron icons.
- Sticky wrapper includes an absolute border layer for scrolled state changes.
- Mobile nav HTML includes accordion-like category buttons and full-width list items.

### Inputs & Forms

- Homepage does not expose a live form, but product UI screenshot shows Dub's app form language:
  - Rectangular inputs with `8px` or slightly smaller radius.
  - Hairline borders around input fields.
  - Label text small and neutral.
  - QR preview card uses a dense dotted texture with a black QR center.

### Hero Section

- Announcement pill at top with segmented "Read more" affordance.
- H1: Satoshi, centered, `text-4xl` to `sm:text-5xl`, medium weight.
- Subtitle: Inter, `text-base` to `sm:text-xl`, neutral-600.
- CTA cluster: two `rounded-lg` buttons with identical geometry but opposing surfaces.
- Proof transition: gray/white grid band with mirrored SVG curves creating a central tab bridge.
- Tabbed product mockup: three tabs, active white, inactive neutral, product screenshot below.

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-primary-black** — filled black conversion CTA. Use for the single highest-value action only.

**button-secondary-white** — white bordered action. Use beside primary CTA, never as a colored alternative.

**announcement-pill-split** — rounded-full micro banner with a left text segment and right read-more segment.

**hero-product-tab-active** — white tab with border, drop-shadow, colored icon chip, dark text.

**hero-product-tab-inactive** — neutral tab with transparent/soft border and muted text.

**grid-section-rail** — full-width band with outer background, inner vertical borders, and low-contrast grid/hairline structure.

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
grid-rail-proof-transition:
  description: "Marketing copy turns into product proof through a gridded rail and curved notch."
  technique: "border-y + inner border-x; bg-neutral-100 / #F5F5F5; 64px bridge; mirrored SVG curves; centered tab group above a 940px proof panel"
  applied_to: ["{component.grid-section-rail}", "{component.hero-product-tab-active}", "{component.hero-product-tab-inactive}"]
  visual_signature: "A clean white promise drops into a measured app surface instead of a generic screenshot card."

black-cta-neutral-ring:
  description: "The primary conversion action stays black and uses neutral pressure feedback instead of brand color."
  technique: "bg-black #000000; hover:bg-neutral-800 / #262626; hover:ring-4; hover:ring-neutral-200 / #E5E5E5; shadow-sm"
  applied_to: ["{component.button-primary}", "{component.button-primary-black}"]
  visual_signature: "The CTA feels tactile and decisive without introducing a blue or purple SaaS accent."

semantic-icon-chip-tabs:
  description: "Product areas are color-coded only at tiny icon scale."
  technique: "size-4 icon chip; rounded 4px; border-black/5; drop-shadow-md; orange/green/purple backgrounds; group-hover:scale-110"
  applied_to: ["{component.hero-product-tab-active}", "{component.hero-product-tab-inactive}"]
  visual_signature: "Color reads as product taxonomy, not decoration or second brand palette."

satoshi-medium-tight-hero:
  description: "Display type is compact and controlled without becoming bold marketing type."
  technique: "font-family: satoshi; font-weight: 500; font-size: 36px mobile / 48px desktop; line-height: 40px / 1.15; letter-spacing: -0.025em"
  applied_to: ["hero H1", "{typography.ladder.h1-mobile}", "{typography.ladder.h1-desktop}"]
  visual_signature: "The headline sits like an inked product label rather than a shouted billboard."

staggered-proof-entrance:
  description: "The first fold comes online as a software startup sequence."
  technique: "animate-slide-up-fade; [--offset:20px] down to [--offset:5px]; animation-delay: 100ms, 200ms, 300ms, 400ms, 500ms; motion-reduce:animate-fade-in"
  applied_to: ["announcement pill", "hero H1", "subcopy", "CTA cluster", "hero tabs", "product proof panel"]
  visual_signature: "The interface feels instrumented and ready rather than flashy."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | concrete conversion outcome, short and verb-led | "Turn clicks into revenue" |
| Primary CTA | direct free-start promise | "Start for free" |
| Secondary CTA | sales/demo path, lower contrast | "Get a demo" |
| Subheading | platform category plus three use cases | "short links, conversion tracking, and affiliate programs" |
| Tone | pragmatic SaaS, revenue-oriented, minimal ornament | announcement about partner payouts |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Dub — copy into your root stylesheet */
:root {
  /* Fonts */
  --dub-font-display: "satoshi", "satoshi Fallback", system-ui, sans-serif;
  --dub-font-body: "Inter", "Inter Fallback", system-ui, sans-serif;
  --dub-font-mono: "GeistMono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --dub-font-weight-normal: 400;
  --dub-font-weight-medium: 500;
  --dub-font-weight-bold: 600;

  /* Brand / neutrals */
  --dub-color-brand-000: #000000;
  --dub-color-brand-800: #262626;
  --dub-color-brand-900: #171717;
  --dub-color-bg-page: #FFFFFF;
  --dub-color-bg-muted: #FAFAFA;
  --dub-color-bg-subtle: #F5F5F5;
  --dub-color-hairline: #E5E5E5;
  --dub-color-border: #D4D4D4;
  --dub-color-text: #171717;
  --dub-color-text-body: #404040;
  --dub-color-text-muted: #737373;

  /* Accents */
  --dub-color-accent-purple: #855AFC;
  --dub-color-accent-blue: #3A8BFD;
  --dub-color-accent-green: #15803D;
  --dub-color-accent-orange: #F4950C;

  /* Key spacing */
  --dub-space-control-x: 20px;
  --dub-space-control-y: 8px;
  --dub-space-hero-gap: 40px;
  --dub-space-section-x: 16px;

  /* Radius */
  --dub-radius-control: 8px;
  --dub-radius-panel: 12px;
  --dub-radius-pill: 9999px;
}

.dub-hero {
  background:
    linear-gradient(to right, rgba(229, 229, 229, .45) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(229, 229, 229, .45) 1px, transparent 1px),
    var(--dub-color-bg-page);
  background-size: 60px 60px;
  color: var(--dub-color-text);
  text-align: center;
}

.dub-hero h1 {
  font-family: var(--dub-font-display);
  font-size: clamp(36px, 5vw, 48px);
  line-height: 1.15;
  letter-spacing: -0.025em;
  font-weight: 500;
}

.dub-button-primary {
  border: 1px solid #000000;
  background: #000000;
  color: #FFFFFF;
  border-radius: 8px;
  padding: 8px 20px;
  font: 500 14px/20px var(--dub-font-body);
  box-shadow: 0 1px 2px rgba(0, 0, 0, .05);
  transition: background-color .15s ease, box-shadow .15s ease;
}
.dub-button-primary:hover {
  background: #262626;
  box-shadow: 0 0 0 4px #E5E5E5;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Dub-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        dub: {
          black: '#000000',
          ink: '#171717',
          body: '#404040',
          muted: '#737373',
          hairline: '#E5E5E5',
          surface: '#FFFFFF',
          subtle: '#F5F5F5',
          purple: '#855AFC',
          blue: '#3A8BFD',
          green: '#15803D',
          orange: '#F4950C',
        },
      },
      fontFamily: {
        display: ['satoshi', 'satoshi Fallback', 'system-ui', 'sans-serif'],
        sans: ['Inter', 'Inter Fallback', 'system-ui', 'sans-serif'],
        mono: ['GeistMono', 'ui-monospace', 'monospace'],
      },
      borderRadius: {
        dub: '8px',
        'dub-panel': '12px',
      },
      boxShadow: {
        'dub-ring-hover': '0 0 0 4px #E5E5E5',
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
| Brand primary | `--dub-color-brand-000` | `#000000` |
| Background | `--dub-color-bg-page` | `#FFFFFF` |
| Subtle surface | `--dub-color-bg-subtle` | `#F5F5F5` |
| Text primary | `--dub-color-text` | `#171717` |
| Text body | `--dub-color-text-body` | `#404040` |
| Text muted | `--dub-color-text-muted` | `#737373` |
| Border/hairline | `--dub-color-hairline` | `#E5E5E5` |
| Purple accent | `--dub-color-accent-purple` | `#855AFC` |
| Success | `--content-success` | `#15803D` |
| Error | `--content-error` | `#B91C1C` |

### Example Component Prompts

#### Hero Section

```text
Dub 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF 위에 아주 옅은 #E5E5E5 grid hairline
- H1: satoshi, 48px desktop / 36px mobile, weight 500, tracking -0.025em
- 서브텍스트: Inter 20px/28px desktop, color #525252 또는 #404040
- CTA: primary는 #000000 배경 + #FFFFFF 텍스트 + 8px radius + hover ring #E5E5E5
- Secondary: #FFFFFF 배경 + #E5E5E5 border + muted gray text
- 아래에는 3개 tab과 제품 UI proof panel을 배치
```

#### Card Component

```text
Dub 스타일 카드/패널을 만들어줘.
- 배경: #FFFFFF 또는 #FAFAFA
- border: 1px solid #E5E5E5
- radius: 8px for controls, 12px for large panels
- shadow: heavy shadow 금지, shadow-sm 또는 drop-shadow-sm만
- 제목: Inter/Satoshi 16px, weight 500 또는 600
- 본문: Inter 14-16px, color #404040, muted는 #737373
```

#### Badge

```text
Dub 스타일 배지를 만들어줘.
- announcement: rounded-full, #FFFFFF background, #E5E5E5 border, segmented read-more area
- feature chip: 16px icon box, rounded 4px, border black/5, small semantic color only
- color accent는 icon chip에만 쓰고 큰 배경으로 확장하지 마
```

#### Navigation

```text
Dub 스타일 상단 네비게이션을 만들어줘.
- sticky top nav, height 56px, max-width 1024px
- logo left, center nav links, auth buttons right
- links: 14px, weight 500, #404040/#171717
- primary signup button: black filled, 8px radius
- mobile에서는 accordion/list nav로 접기
```

### Iteration Guide

- **색상 변경 시**: black/white/neutral 구조를 유지하고 chromatic accent는 작은 semantic chip에만 사용.
- **폰트 변경 시**: H1은 display face at `500`; body/control은 Inter-like sans.
- **여백 조정 시**: CTA와 tabs는 compact, proof panel은 wide. 모든 것을 같은 max-width에 넣지 말 것.
- **새 컴포넌트 추가 시**: `8px` control radius, `#E5E5E5` hairline, muted text hierarchy를 유지.
- **다크 모드**: dark tokens exist, but homepage screenshot is light. Dark redesign must explicitly remap surfaces rather than invert blindly.
- **반응형**: `640/768/1024` breakpoints를 기본으로 하고 tiny auth/nav edge cases는 별도 처리.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#FFFFFF` as the primary page field and let grid/hairline structure create depth.
- Use `#000000` for the main conversion CTA and `#262626` for the hover state.
- Keep secondary CTAs white with `#E5E5E5` border and muted gray text.
- Use Satoshi for display if available; otherwise use a compact display substitute at weight `500`.
- Keep product-category colors small: icon chips, tiny badges, or semantic states only.
- Preserve the hero-to-product transition: centered copy, compact CTA, then tabbed product proof.
- Use staggered slide-up/fade motion with reduced-motion fallback.
- Treat customer logo/SVG colors as contamination unless they appear in UI roles.

### ❌ DON'T

- 배경을 `#F8FAFC` 또는 `#F9FAFB` 같은 generic SaaS off-white로 두지 말 것 — 대신 `#FFFFFF` 사용.
- 텍스트를 `#000000` pure black으로 전부 밀지 말 것 — heading/CTA anchor는 `#171717`, body는 `#404040` 사용.
- Primary CTA를 `#855AFC`, `#3A8BFD`, 또는 gradient로 칠하지 말 것 — 대신 `#000000` 사용.
- Hairline/border를 `#CBD5E1` 같은 blue-gray로 두지 말 것 — 대신 `#E5E5E5` 또는 `#D4D4D4` 사용.
- Hero 배경에 `#667EEA` → `#764BA2` 보라 gradient를 쓰지 말 것 — Dub hero는 `#FFFFFF` + grid다.
- H1을 `font-weight: 700` 이상으로 만들지 말 것 — Dub hero는 `font-weight: 500`이 맞다.
- 모든 accent chip을 같은 브랜드색으로 통일하지 말 것 — short links/orange, analytics/green, affiliate/purple처럼 semantic split 유지.
- 카드에 큰 `box-shadow: 0 20px 50px ...`를 넣지 말 것 — `shadow-sm`, `drop-shadow-sm`, hairline border가 맞다.
- Radius를 전부 `24px` 이상 pill-card로 만들지 말 것 — controls는 `8px`, pill은 announcement에만 사용.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- **Brand gradient**: none in the hero identity. Gradients exist in CSS/assets, but the homepage first impression is not gradient-led.
- **Second brand color**: absent. Purple/blue/green/orange are semantic/product markers, not co-primary brand colors.
- **Heavy display weight**: no 700+ hero headline. The visible hero uses medium-weight display type.
- **Photography hero**: none. Product UI evidence replaces lifestyle or stock imagery.
- **Large decorative illustration**: none in first fold. SVGs are structural curves, icons, logos, or app UI internals.
- **Floating feature-card trio under hero**: absent. Dub uses a tabbed product proof instead of generic three-card marketing.
- **Warm cream palette**: absent. The page is cool white/neutral, not beige or editorial cream.
- **Blue SaaS default CTA**: absent. Signup CTA is black, not blue.
- **Heavy chrome shadow**: absent. Depth is mostly border, grid, opacity, and product preview.
- **Verbose onboarding copy**: absent. Copy stays short, outcome-led, and conversion-focused.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage snapshot** — The analysis reuses cached `https://dub.co` homepage phase1 data. Authenticated app surfaces, pricing subpages, and docs pages may use additional variants.
- **Desktop screenshot bias** — The available screenshot is `1280x800`. Responsive behavior is inferred from CSS breakpoints and HTML classes, not from rendered mobile screenshots.
- **CSS utility compression** — Most component intent is encoded in Tailwind class composition inside HTML. Named component APIs are reconstructed from visible class bundles rather than exported design tokens.
- **Color contamination risk** — Frequency candidates include SVG, logo, flag, and product-demo colors. The report deliberately treats chromatic colors as semantic chips unless they appear in clear UI roles.
- **Motion not runtime-profiled** — CSS classes and animation delays were observed, but JavaScript tab timing, scroll observers, and interaction state machines were not executed.
- **Dark mode incomplete** — `.dark` semantic tokens exist in CSS, but the captured homepage state is light. Dark-mode application rules are token-level, not screenshot-confirmed.
- **Forms are product-preview only** — Input specs are inferred from the embedded app mockup HTML/screenshot, not from a live interactive form flow.
- **Exact grid line implementation** — The visible grid is screenshot-confirmed; CSS source includes many gradients and grid-related classes, but the final rendered composition may involve multiple layered utilities.
- **Satoshi licensing/runtime** — The font is loaded from Dub assets in the captured CSS. External reuse should substitute or license appropriately.
