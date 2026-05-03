---
schema_version: 3.2
slug: convex
service_name: Convex
site_url: https://www.convex.dev
fetched_at: 2026-04-20T19:58:00+09:00
default_theme: dark
brand_color: "#8D2676"
primary_font: gtAmerica
font_weight_normal: 400
token_prefix: convex

bold_direction: Developer Atelier
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Tailwind v4 CSS variables plus 69 named core color tokens, custom fonts, editor surfaces, and repeated CTA/nav/card patterns."

colors:
  primary: "#8D2676"
  surface-dark: "#141414"
  surface-hero: "#444435"
  surface-paper: "#F9F7EE"
  text-on-dark: "#FFFFFF"
  text-ink: "#262321"
  text-muted: "#BAB6C0"
  border-muted: "#D6D6D6"
  accent-salmon: "#FF867E"
  accent-orchid: "#E79CD6"
  accent-blue: "#3D72F5"
  code-pink: "#FC618D"
  code-purple: "#948AE3"
  code-green: "#7BD88F"
  code-cyan: "#5AD4E6"

typography:
  display: "gtAmerica"
  body: "gtAmerica"
  serif: "publico"
  mono: "ui-monospace"
  pixel: "vcr"
  ladder:
    - { token: hero-h1, size: "48px desktop observed", weight: 700, tracking: "normal" }
    - { token: section-h2, size: "large display", weight: 700, tracking: "normal" }
    - { token: body, size: "16px", weight: 400, tracking: "normal" }
    - { token: nav, size: "14px", weight: 500, tracking: "normal" }
    - { token: code, size: "14px", weight: 400, tracking: "normal" }
  weights_used: [300, 400, 500, 600, 700, 800, 900]
  weights_absent: []

components:
  button-primary: { bg: "{colors.text-on-dark}", color: "{colors.text-ink}", radius: "9999px", padding: "11px 20px" }
  button-blue-action: { bg: "{colors.accent-blue}", color: "{colors.text-on-dark}", radius: "9999px", padding: "10px 18px" }
  nav-pill: { bg: "rgba(255,255,255,0.06)", radius: "9999px", height: "44px" }
  command-copy: { bg: "rgba(255,255,255,0.14)", border: "1px solid rgba(255,255,255,0.36)", radius: "11px" }
  editor-window: { bg: "{colors.surface-dark}", border: "warm salmon frame", radius: "12px" }
---

# DESIGN.md — Convex (Designer Guidebook v3.2)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Convex reads like a developer workbench set inside a warm studio, not a generic SaaS hero. The page opens on #444435 (`{colors.surface-hero}`), a murky olive surface that feels physical and slightly industrial. On top of it, the product is not explained with abstract blobs; it is staged as working software: code editor, app preview, dashboard table, command line, tabs, and tiny live-state labels.

The brand does not lead with one loud chromatic color. #8D2676 (`{colors.primary}`) exists as the plum interaction family, but the hero identity is carried by material contrast: white type against olive, black code panes against a salmon frame, and a biscuit-colored cookie panel floating over the demo. It is closer to a toolmaker's bench with labeled drawers than a neon launch screen: every color has a job, and there is no second brand color trying to become the protagonist.

The hero demo behaves like a cutaway machine in a workshop manual. The salmon outer shell is the casing, #141414 (`{colors.surface-dark}`) is the engine bay, and the todo app, database table, command line, and code editor are exposed moving parts. Convex does not ask the viewer to imagine the backend; it puts the backend under glass like an operating instrument panel.

Typography is blunt and practical. `gtAmerica` gives the page a wide, confident developer-platform voice; `vcr` and `ui-monospace` give the code surfaces their mechanical counterweight. `publico` appears as a serif option, but the homepage's first impression is not editorial. It is command-line literalness wrapped in product polish, like a terminal prompt printed on heavy studio paper.

The memorable craft is the stacked demo chassis. The right side is a multi-panel app/editor/dashboard object with deep black surfaces, salmon outer casing, colored syntax, and inset table chrome. That object does the work that gradients usually do on SaaS sites: it creates depth, motion expectation, and proof of product. Shadow belongs to the machine, not the room; the page stays mostly flat while the product object lifts off the workbench.

Convex's negative space is as important as its visible chrome. No generic blue-black void, no decorative orb system, no rainbow marketing cards. The high-chroma colors #FC618D, #948AE3, #7BD88F, and #5AD4E6 stay inside code panes like signal LEDs on hardware, while #3D72F5 (`{colors.accent-blue}`) is allowed to be an app action, not a brand takeover.

### Key Characteristics

- Warm dark hero surface: #444435 and #141414, not blue-black SaaS darkness.
- White-on-olive headline with compact, left-aligned hero copy.
- Product proof is literal: code, todo app, database table, and command line are first-viewport objects.
- Plum is the interaction accent, but it is restrained; #8D2676 and #E79CD6 support rather than flood the page.
- Code syntax colors are candy-bright (#FC618D, #948AE3, #7BD88F, #5AD4E6) inside black editor panes only.
- Buttons are pill-shaped and simple, with the first CTA often white on dark rather than brand-filled.
- Navigation is dense but friendly: horizontal links, rounded GitHub star pill, and a login capsule.
- Surface shifts move from dark workbench to pale paper/cream sections rather than one continuous gradient.
- Shadows are used to lift product/demo panels, not to decorate every card.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Developer Atelier
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **warm dark workbench with live code-product demo chassis**으로 기억된다.
> **Code Complexity**: high — Tailwind utility output, custom font stack, multiple editor/app mock surfaces, tab states, cookie overlay, and layered shadows.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Convex처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "gtAmerica", ui-sans-serif, system-ui, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #444435; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #8D2676; }
```

**절대 하지 말아야 할 것 하나**: Convex를 보라/파랑 그라디언트 SaaS로 만들지 말 것. 첫 인상은 #444435 웜 다크 워크벤치 + 실제 코드/앱 데모다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.convex.dev` |
| Fetched | 2026-04-20T19:58:00+09:00 (phase1 reused) |
| Extractor | existing phase1 JSON + captured HTML/CSS/screenshot |
| HTML size | 379823 bytes (Next.js app output) |
| CSS files | 4 CSS files, total 162443 bytes |
| Token prefix | `convex` (report-level alias; source CSS uses Tailwind + named `--color-*`) |
| Method | CSS custom properties, HTML structure, and hero screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js marketing site output, visible through generated HTML and `next-size-adjust` metadata.
- **Design system**: Tailwind v4-style CSS variables plus Convex named color tokens.
- **CSS architecture**:
  ```text
  Core tokens      (--color-neutral-n12, --color-plum-p4, --color-cocoaDarkBrown)
  Utility classes  (bg-neutral-n10, text-plum-p2, rounded-full, shadow-* patterns)
  Component usage  (nav pills, CTA pills, code tabs, editor windows, demo cards)
  ```
- **Class naming**: Tailwind utility classes with custom semantic color namespaces (`neutral`, `plum`, `yellow`, `green`, `red`) and custom object classes for editor/demo regions.
- **Default theme**: dark first impression (`theme-color: #141414`; hero surface #444435).
- **Font loading**: custom font variables exposed as `--font-gt-america`, `--font-vcr`, `--font-publico`.
- **Canonical anchor**: first viewport hero with headline, command copy box, feature accordion, editor/app/dashboard mock.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `gtAmerica` (custom/commercial brand font)
- **Body font**: `gtAmerica`
- **Code font**: `ui-monospace`, Menlo, Monaco, Cascadia Mono, Segoe UI Mono, Consolas, monospace
- **Pixel font**: `vcr`, `vcr Fallback`
- **Serif font**: `publico`, `publico Fallback`
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --convex-font-family:       var(--font-gt-america), sans-serif;
  --convex-font-family-code:  ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  --convex-font-family-pixel: var(--font-vcr), monospace;
  --convex-font-weight-normal: 400;
  --convex-font-weight-bold:   700;
}
body {
  font-family: var(--convex-font-family);
  font-weight: var(--convex-font-weight-normal);
}
```

### Note on Font Substitutes

- **gtAmerica substitute** — use **Inter** or **Suisse Int'l-like system stack** only with slightly heavier headings. Convex's headline weight lands visually closer to Inter 700 than Inter 600.
- **vcr substitute** — use **VT323** only for tiny labels or terminal-style accents, not body copy. Keep it limited to pixel/retro UI details.
- **publico substitute** — use **Source Serif 4** for any editorial callout that needs the `publico` role. Do not introduce it into nav, CTAs, or code surfaces.
- **Code substitute** — use `ui-monospace` with 14px and normal weight. The code panes depend on syntax color and dark surface more than a distinctive programming font.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Hero H1 | ~48px desktop observed | 700 | tight display | normal |
| Section H2 | large display | 700 | compact | normal |
| Feature H3 | 20px range | 600-700 | 1.35-1.45 | normal |
| Body | 16px | 400 | 1.55-1.65 | normal |
| Nav link | 14px | 500 | 44px control height | normal |
| Code | 14px | 400 | editor-like | normal |
| Badge / small label | 12-14px | 500-700 | compact | normal |

> ⚠️ `typography.json` did not recover a full scale map, so size values combine CSS evidence with screenshot observation. Font families and weights are CSS-derived.

### Principles

1. Display type is confident but not oversized; the hero H1 leaves room for the live product demo rather than owning the whole viewport.
2. Body copy stays utilitarian. The page avoids soft SaaS microcopy styling and uses direct developer-platform statements.
3. Code and app UI text are part of the visual system. They are not screenshots pasted into the page; they are styled surfaces with their own font rhythm.
4. Weight 500 is used for navigation/control clarity, while 700/900 are reserved for headings and strong UI labels.
5. Serif is available but deliberately peripheral. Convex's homepage identity is sans + mono + pixel, not editorial serif.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (plum family)
<!-- --color-plum-* -->

| Token | Hex |
|---|---|
| `--color-plum-p1` | `#F4E9F1` |
| `--color-plum-p2` | `#E3D0DF` |
| `--color-plum-p3` | `#D7B3CF` |
| `--color-plum-p4` | `#8D2676` |
| `--color-plum-p5` | `#711E5E` |
| `--color-plum-p6` | `#47133B` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--color-neutral-n12` | `#141414` |
| `--color-neutral-n13` | `#111111` |
| `--color-neutral-black` | `#000000` |
| `--color-neutral-n10` | `#38383A` |
| `--color-neutral-n11` | `#292929` |

### 06-3. Neutral Ramp

| Step | Light (`neutral`) | Dark (`neutral`) |
|---|---|---|
| white / black | `#FFFFFF` | `#000000` |
| n1 / n13 | `#F6F6F6` | `#111111` |
| n2 / n12 | `#F1F1F1` | `#141414` |
| n3 / n11 | `#E5E5E5` | `#292929` |
| n4 / n10 | `#D7D7D7` | `#38383A` |
| n5 / n9 | `#C2C2C2` | `#4F4F52` |
| n6 / n8 | `#A9A9AC` | `#6D6D70` |
| n7 | `#8B8B8E` | `#8B8B8E` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Warm brown | `--color-cocoaDarkBrown` | `#2E1F1F` |
| Salmon | `--color-congoPink` | `#FF867E` |
| Vermillion | `--color-mediumVermillion` | `#DE5D33` |
| Cream | `--color-seashell` | `#F9F7EE` |
| Olive | `--color-rifleGreen` | `#444435` |
| Blue | `--color-ultramarineBlue` | `#3D72F5` |
| Orchid | `--color-orchid` | `#E79CD6` |
| Green | `--color-green-g3` | `#4FB014` |
| Yellow | `--color-yellow-y3` | `#F3B01C` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--color-neutral-n12` | `#141414` | deep page/app surface |
| `--color-neutral-white` | `#FFFFFF` | text and white CTA on dark |
| `--color-rifleGreen` | `#444435` | hero workbench surface |
| `--color-plum-p4` | `#8D2676` | primary brand/plum interaction |
| `--color-plum-p2` | `#E3D0DF` | link/accent text on dark |
| `--color-ultramarineBlue` | `#3D72F5` | app action button / strong action |
| `--color-yellow-y3` | `#F3B01C` | category badge / highlight |
| `--color-green-g3` | `#4FB014` | success/status family |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--convex-surface-dark` | `#141414` | body dark zones, editor surfaces |
| `--convex-surface-hero` | `#444435` | hero background |
| `--convex-primary` | `#8D2676` | brand/link/action accent |
| `--convex-primary-soft` | `#E3D0DF` | muted plum text/accent |
| `--convex-action-blue` | `#3D72F5` | app demo Add button |
| `--convex-paper` | `#F9F7EE` | warm light panels |

> These aliases are report-level names for implementation convenience. The source CSS primarily uses Tailwind utility classes and named `--color-*` variables.

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---|---|
| code pink | `#FC618D` | 65 observed in phase1 |
| code purple | `#948AE3` | 65 observed in phase1 |
| code green | `#7BD88F` | 64 observed in phase1 |
| code neutral | `#BAB6C0` | 64 observed in phase1 |
| code cyan | `#5AD4E6` | 43 observed in phase1 |
| pale lavender | `#F7F1FF` | 42 observed in phase1 |
| yellow | `#F8E67A` | 23 observed in phase1 |
| neutral border | `#D6D6D6` | 21 observed in phase1 |

### 06-8. Color Stories

**`{colors.surface-hero}` (`#444435`)** — The first-viewport workbench color. This is the most important "feel" color: warm, dark, olive, and material. Use it instead of `#0B1020` or navy-black.

**`{colors.surface-dark}` (`#141414`)** — The app/editor darkness. It belongs inside product mockups, code panes, tables, and dark nav surfaces. It should feel like software chrome, not a page-wide void.

**`{colors.primary}` (`#8D2676`)** — Plum is Convex's interaction color, but it is not sprayed across every section. It appears best as links, focus/accent states, selected tabs, and compact brand details.

**`{colors.text-on-dark}` (`#FFFFFF`)** — White is the hero's voice. On the olive surface, it makes the page feel direct and high-contrast; on editor surfaces, it must share space with syntax colors rather than overpower them.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--spacing` base | `.25rem` | Tailwind v4 spacing multiplier |
| `gap-1` | 4px | icon/text gaps in small controls |
| `gap-2` | 8px | menu and compact row gaps |
| `h-9` | 36px | small pill/link controls |
| `h-11` | 44px | nav action controls |
| `px-5` | 20px | login/nav pill horizontal padding |
| `p-3` | 12px | nav trigger/link touch padding |
| hero content gutter | ~48px observed | left hero column and inner page margin |
| section divider rhythm | ~48-64px observed | feature accordion blocks |

**주요 alias**:
- `--convex-space-control-x` → 20px (pill CTAs and login controls)
- `--convex-space-section` → 64px (major vertical breathing room)
- `--convex-space-demo-gap` → 12-16px (inside editor/app mock surfaces)

### Whitespace Philosophy

Convex uses whitespace as a working margin, not luxury air. The hero left column is compact: headline, CTA, command box, then feature accordion. The right side spends its pixels on proof density, packing editor tabs, todo rows, dashboard rows, and cookie overlay into a single product object.

Below the fold, the site can open into lighter marketing bands, but the first viewport teaches the rule: wide gutters around the workbench, dense spacing inside the workbench. Open page, compressed product.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| `--radius-sm` | `.25rem` | small UI corners |
| `--radius-md` | `.375rem` | inputs, small panels |
| `--radius-lg` | `.5rem` | compact cards/buttons |
| `--radius-xl` | `.75rem` | demo panels |
| `--radius-2xl` | `1rem` | large surfaces |
| `--radius-3xl` | `1.5rem` | larger marketing containers |
| `rounded-full` | `9999px` | CTAs, nav pills, login/GitHub capsules |
| command box | `11px observed` | copyable npm command surface |
| editor frame | ~12px observed | salmon-framed mockup shell |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| soft card | `0 1px 3px 0 #0000001A, 0 1px 2px -1px #0000001A` | standard elevation |
| blue glow | `0px 2px 14px #3D72F566` | blue action / active affordance |
| plum glow | `0 0 14px #6F00FF80` | special focus/accent glow |
| panel lift | `0px 8px 8px #00000012, 0px 91px 100px #00000021` | large product/demo float |
| dark overlay | `0px -16px 72px -8px #00000040` | deep overlay/separation |
| subtle product | `0px 14px 15px #05050508` | soft object lift |

Convex's shadow language is product-surface scoped. Do not give every marketing card a glow. Reserve deep shadows for editor/demo/mock surfaces and overlays.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `--default-transition-duration` | `.15s` | Tailwind default state changes |
| `--ease-in` | `cubic-bezier(.4, 0, 1, 1)` | entering/closing state |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | hover/reveal completion |
| `--ease-in-out` | `cubic-bezier(.4, 0, .2, 1)` | general state transitions |
| duration variants | `50ms`, `75ms`, `.1s`, `.2s`, `.3s`, `.5s` | utility-level animation choices |

Motion should feel like interface feedback, not landing-page spectacle: tab changes, hover backgrounds, command-copy affordances, and demo state changes.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: hero spans most of a 1280px viewport with ~48px edge padding.
- **Grid type**: two-column hero using flex/grid composition; left narrative column + right product demo chassis.
- **Column count**: effectively 2 columns in hero, then stacked marketing sections.
- **Gutter**: wide page gutter, tight internal demo gutters.

### Hero

- **Pattern Summary**: `~800px viewport + warm olive dark bg + left H1/CTA/command + right live code/app/dashboard chassis`
- Layout: left-aligned text column paired with large right product mock.
- Background: solid #444435 (`{colors.surface-hero}`).
- **Background Treatment**: solid warm dark surface; no gradient mesh, no decorative orb layer.
- H1: `~48px` / weight `700` / tracking `normal`.
- Max-width: full landing container, product mock takes dominant right-side width.

### Section Rhythm

```css
section {
  padding: 64px 48px;
  max-width: 1280px;
}
```

The exact section rule varies by Tailwind utilities, but the visual rhythm is clear: generous outer bands with dense product/content modules.

### Card Patterns

- **Card background**: dark cards use #141414 / #292929; light cards use #F9F7EE / #FFFFFF.
- **Card border**: subtle neutral borders (`#D6D6D6`, `#0000001A`, or dark neutral equivalents).
- **Card radius**: 12-16px for demo containers; full radius for pills.
- **Card padding**: 12-24px depending on density.
- **Card shadow**: layered product shadows only for floating/demo objects.

### Navigation Structure

- **Type**: horizontal desktop nav with product/developer dropdown triggers.
- **Position**: top hero nav, visually integrated into dark hero surface.
- **Height**: action controls use 44px (`h-11`); text links use 12px vertical padding.
- **Background**: transparent/dark surface, with rounded GitHub and login pills.
- **Border**: no heavy nav border in hero; separation comes from contrast and capsules.

### Content Width

- **Prose max-width**: left hero copy ~320px observed.
- **Container max-width**: 1280px viewport fit.
- **Sidebar width**: N/A for homepage; product demo panels replace sidebar structure.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Small | `400px` | narrow special-case rule observed |
| Mobile/Small | `40rem` | Tailwind small breakpoint |
| Tablet | `48rem` | tablet layout changes |
| Desktop | `64rem` | desktop nav/hero density |
| Wide | `80rem` | wide container tuning |
| Extra Wide | `96rem` | extra-large display tuning |
| Custom wide | `1080px` | site-specific layout breakpoint |

### Touch Targets

- **Minimum tap size**: 44px for nav action buttons (`h-11` observed).
- **Button height (mobile)**: 36-44px depending on compact vs primary action.
- **Input height (mobile)**: app mock input appears around 36-38px; full form states not measured.

### Collapsing Strategy

- **Navigation**: desktop horizontal nav likely collapses behind mobile menu; exact mobile menu state not captured.
- **Grid columns**: hero two-column must stack, with product mock below or simplified.
- **Sidebar**: no homepage sidebar; dropdown content stacks into menu groups.
- **Hero layout**: text/CTA first, demo object second; preserve command box as a signature element.

### Image Behavior

- **Strategy**: product mock is rendered/styled UI rather than a single flat image.
- **Max-width**: responsive max-width utility behavior.
- **Aspect ratio handling**: editor/app panels maintain fixed visual proportions inside the right chassis.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

#### `.convex-button-primary`

```html
<a class="convex-button-primary" href="/start">Start building</a>
```

| State | Spec |
|---|---|
| default | background `#FFFFFF`, color `#262321`, radius `9999px`, padding `11px 20px`, weight `600` |
| hover | slight warm-neutral tint, no scale bounce |
| focus | 2px visible ring, use neutral/black ring depending surface |
| disabled | lower opacity; keep pill silhouette |

#### `.convex-button-action-blue`

```html
<button class="convex-button-action-blue">Add</button>
```

| State | Spec |
|---|---|
| default | background `#3D72F5`, color `#FFFFFF`, radius `9999px`, compact app-control height |
| hover | darker blue or glow, not gradient |
| focus | high-contrast ring on dark app panel |

### Badges

```html
<span class="convex-badge convex-badge-work">Work</span>
<span class="convex-badge convex-badge-chores">Chores</span>
```

| Variant | Spec |
|---|---|
| work | plum/pink badge family; compact pill or rounded rectangle |
| chores | yellow family, e.g. `#F3B01C`, with dark text |
| other | neutral gray badge against dark app surface |

Badges appear inside the product mock, not as decorative marketing chips. Keep them small, functional, and category-like.

### Cards & Containers

```html
<section class="convex-editor-window">
  <div class="convex-editor-tab">convex/todos.ts</div>
  <pre>export const add = mutation(...)</pre>
</section>
```

| Part | Spec |
|---|---|
| editor shell | black/dark #141414 interior with warm salmon/camel frame |
| tab bar | #292929 / #111111 surfaces, 3-dot controls |
| code pane | dark surface + syntax palette #FC618D, #948AE3, #7BD88F, #5AD4E6 |
| dashboard table | dark panel, thin neutral lines, mono rows |
| cookie card | warm paper #F9F7EE / #FFFFFF with rounded corners and shadow |

### Navigation

```html
<nav class="convex-nav">
  <a class="convex-logo">convex</a>
  <button>Product</button>
  <a>Docs</a>
  <a class="convex-nav-pill">GitHub</a>
  <a class="convex-nav-pill">Log in</a>
</nav>
```

| Element | Spec |
|---|---|
| logo | white, heavy, compact custom wordmark |
| links | #FFFFFF on hero, 14px, medium weight |
| dropdown trigger | text + small chevron, no bordered box |
| GitHub pill | 44px height, rounded full, translucent dark surface |
| login pill | 44px height, rounded full, darker translucent surface |

### Inputs & Forms

```html
<div class="convex-app-input-row">
  <input value="Schedule meeting with boss" />
  <button>Add</button>
</div>
```

| State | Spec |
|---|---|
| default | dark input, thin neutral border, white text, compact radius |
| focus | visible caret/outline, no oversized glow |
| error | not observed; use red family `#EE342F` only if validation is explicit |
| loading | not observed; preserve compact app-control geometry |

### Hero Section

```html
<header class="convex-hero">
  <div class="convex-hero-copy">
    <h1>The backend platform that keeps your app in sync</h1>
    <a class="convex-button-primary">Start building</a>
    <div class="convex-command">npm create convex</div>
  </div>
  <div class="convex-demo-chassis">...</div>
</header>
```

| Part | Spec |
|---|---|
| background | #444435 solid |
| headline | white, left aligned, compact width |
| CTA | white pill, warm dark text |
| command | translucent olive/gray box with border and copy icon |
| right object | live product demo composition, not abstract illustration |

### 13-2. Named Variants

#### `button-primary-white-pill`

White CTA on dark hero. Use for "Start building" and primary hero conversion.

| Property | Value |
|---|---|
| bg | `#FFFFFF` |
| color | `#262321` |
| radius | `9999px` |
| weight | `600` |

#### `button-app-blue-add`

App-demo action button, visually separate from marketing CTA.

| Property | Value |
|---|---|
| bg | `#3D72F5` |
| color | `#FFFFFF` |
| radius | `9999px` |
| context | inside dark app mock only |

#### `nav-github-star-pill`

GitHub social proof capsule in the nav.

| Property | Value |
|---|---|
| height | `44px` |
| bg | dark translucent neutral |
| content | GitHub icon, label, small star count |

#### `command-copy-box`

Copyable command surface under the hero CTA.

| Property | Value |
|---|---|
| bg | translucent warm neutral |
| border | pale olive/cream line |
| radius | `11px` observed |
| font | mono |

### 13-3. Signature Micro-Specs

```yaml
warm-olive-workbench-hero:
  description: "First viewport is a physical developer workbench, not a navy SaaS void."
  technique: "solid #444435 surface with #FFFFFF headline text, white pill CTA, and translucent command surface using rgba(255,255,255,0.12) plus 1px rgba(255,255,255,0.34) border"
  applied_to: ["{component.Hero Section}", "{component.command-copy}"]
  visual_signature: "The page feels like a warm studio bench with executable software placed on top."

salmon-cased-demo-chassis:
  description: "The product proof is treated as a cased machine made of nested editor, app, and dashboard panels."
  technique: "12px rounded dark #141414 interior, warm salmon/camel outer frame, #292929/#111111 tab and subpanel surfaces, high internal contrast"
  applied_to: ["{component.editor-window}", "{component.Hero Section}"]
  visual_signature: "A live backend demo reads as a tangible instrument panel instead of a flat screenshot."

deep-product-panel-shadow:
  description: "Elevation is reserved for product/demo machinery rather than applied to every marketing card."
  technique: "box-shadow 0px 8px 8px #00000012, 0px 91px 100px #00000021; overlay separation uses 0px -16px 72px -8px #00000040"
  applied_to: ["{component.editor-window}", "{component.cookie-card}", "{component.demo-chassis}"]
  visual_signature: "Only the working product object lifts from the surface; the page chrome stays comparatively flat."

syntax-leds-on-black:
  description: "High-chroma color is scoped to code and live-state proof, not general brand decoration."
  technique: "#FC618D, #948AE3, #7BD88F, #5AD4E6 syntax colors on #141414/#111111 editor surfaces with 14px ui-monospace"
  applied_to: ["{component.editor-window}", "{component.code-pane}"]
  visual_signature: "Code color behaves like small signal LEDs inside the black machine."

app-state-color-islands:
  description: "Blue, yellow, green, and plum accents appear as app state or actions inside the mock product."
  technique: "#3D72F5 pill action button, #F3B01C category badge, #4FB014 success/status family, #8D2676/#E3D0DF plum interaction accents"
  applied_to: ["{component.button-blue-action}", "{component.Badges}", "{component.dashboard-table}"]
  visual_signature: "Color proves realtime app behavior without turning the marketing page into a rainbow palette."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | direct product promise, no metaphor | "The backend platform that keeps your app in sync" |
| Primary CTA | short imperative | "Start building" |
| Secondary command | executable developer action | `npm create convex` |
| Feature label | capability as plain phrase | "Everything is code", "Always in sync" |
| Tone | confident, developer-literal, product-first | "Not just a database" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Convex — copy into your root stylesheet */
:root {
  /* Fonts */
  --convex-font-family:       "gtAmerica", ui-sans-serif, system-ui, sans-serif;
  --convex-font-family-code:  ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  --convex-font-family-pixel: "vcr", monospace;
  --convex-font-weight-normal: 400;
  --convex-font-weight-bold:   700;

  /* Brand / interaction */
  --convex-color-brand-50:  #F4E9F1;
  --convex-color-brand-200: #E3D0DF;
  --convex-color-brand-300: #D7B3CF;
  --convex-color-brand-600: #8D2676;
  --convex-color-brand-800: #47133B;

  /* Surfaces */
  --convex-bg-hero:   #444435;
  --convex-bg-dark:   #141414;
  --convex-bg-paper:  #F9F7EE;
  --convex-text:      #FFFFFF;
  --convex-text-ink:  #262321;
  --convex-text-muted:#BAB6C0;
  --convex-border:    #D6D6D6;

  /* Code/demo accents */
  --convex-code-pink:   #FC618D;
  --convex-code-purple: #948AE3;
  --convex-code-green:  #7BD88F;
  --convex-code-cyan:   #5AD4E6;
  --convex-action-blue: #3D72F5;
  --convex-badge-yellow:#F3B01C;

  /* Key spacing */
  --convex-space-sm:  8px;
  --convex-space-md:  16px;
  --convex-space-lg:  48px;
  --convex-space-xl:  64px;

  /* Radius */
  --convex-radius-sm: 4px;
  --convex-radius-md: 6px;
  --convex-radius-lg: 12px;
  --convex-radius-xl: 16px;
  --convex-radius-pill: 9999px;
}

.convex-hero {
  background: var(--convex-bg-hero);
  color: var(--convex-text);
  font-family: var(--convex-font-family);
}

.convex-button-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--convex-radius-pill);
  background: #FFFFFF;
  color: #262321;
  padding: 11px 20px;
  font-weight: 600;
}

.convex-command {
  border: 1px solid rgba(255,255,255,.34);
  border-radius: 11px;
  background: rgba(255,255,255,.12);
  color: #FFFFFF;
  font-family: var(--convex-font-family-code);
}

.convex-editor {
  border-radius: 12px;
  background: #141414;
  color: #FFFFFF;
  box-shadow: 0px 8px 8px 0px #00000012, 0px 91px 100px 0px #00000021;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Convex-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        convex: {
          hero: '#444435',
          dark: '#141414',
          paper: '#F9F7EE',
          ink: '#262321',
          plum: '#8D2676',
          plumSoft: '#E3D0DF',
          blue: '#3D72F5',
          yellow: '#F3B01C',
          codePink: '#FC618D',
          codePurple: '#948AE3',
          codeGreen: '#7BD88F',
          codeCyan: '#5AD4E6',
        },
      },
      fontFamily: {
        sans: ['gtAmerica', 'ui-sans-serif', 'system-ui'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
        pixel: ['vcr', 'monospace'],
      },
      borderRadius: {
        convex: '12px',
        pill: '9999px',
      },
      boxShadow: {
        convexPanel: '0px 8px 8px 0px #00000012, 0px 91px 100px 0px #00000021',
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
| Brand primary | `{colors.primary}` | `#8D2676` |
| Background | `{colors.surface-hero}` | `#444435` |
| Dark surface | `{colors.surface-dark}` | `#141414` |
| Text primary | `{colors.text-on-dark}` | `#FFFFFF` |
| Text ink | `{colors.text-ink}` | `#262321` |
| Text muted/code neutral | `{colors.text-muted}` | `#BAB6C0` |
| Border | `{colors.border-muted}` | `#D6D6D6` |
| Success | `--color-green-g3` | `#4FB014` |
| Error | `--color-red-r3` | `#EE342F` |

### Example Component Prompts

#### Hero Section

```text
Convex 스타일 히어로 섹션을 만들어줘.
- 배경: #444435 solid, gradient 없음
- H1: gtAmerica, 약 48px, weight 700, color #FFFFFF, left aligned
- CTA 버튼: #FFFFFF 배경, #262321 텍스트, pill radius 9999px, padding 11px 20px
- CTA 아래에 mono command box: "npm create convex", translucent border, radius 11px
- 오른쪽에는 추상 일러스트 대신 black editor/app/dashboard mockup을 배치
- code syntax는 #FC618D, #948AE3, #7BD88F, #5AD4E6만 editor 내부에 사용
```

#### Card Component

```text
Convex 스타일 product demo card를 만들어줘.
- 배경: #141414, 내부 tab/panel은 #292929와 #111111
- border/radius: 12px rounded shell, subtle neutral border
- shadow: 0px 8px 8px #00000012 + 0px 91px 100px #00000021
- 제목/label: gtAmerica 14-16px, weight 600
- body/code: ui-monospace 14px, syntax accent는 editor 내부에만
```

#### Badge

```text
Convex 스타일 category badge를 만들어줘.
- 작고 기능적인 앱 데이터 배지처럼 보이게 한다
- Work: plum/pink family, Chores: #F3B01C, Other: neutral gray
- radius는 작은 rounded rectangle 또는 pill
- 마케팅 칩처럼 크게 만들지 않는다
```

#### Navigation

```text
Convex 스타일 상단 네비게이션을 만들어줘.
- 배경은 #444435와 통합, 별도 흰색 nav bar 금지
- 링크: #FFFFFF, 14px, weight 500
- GitHub/Log in은 h-11 44px rounded-full dark translucent capsule
- Product/Developers는 text + chevron trigger
- 오른쪽 CTA가 필요하면 white pill을 사용한다
```

### Iteration Guide

- **색상 변경 시**: first viewport의 #444435를 유지. brand plum만 바꾸면 Convex처럼 보이지 않는다.
- **폰트 변경 시**: gtAmerica 대체는 Inter 700/400 조합으로 시작하되 mono/pixel 보조축을 유지한다.
- **여백 조정 시**: 페이지 바깥은 넓게, 제품 mock 내부는 조밀하게. 둘을 같은 spacing으로 평평하게 만들지 않는다.
- **새 컴포넌트 추가 시**: 마케팅 카드보다 "작동하는 앱 조각"처럼 설계한다.
- **다크 모드**: #141414 앱 표면과 #444435 히어로 표면을 구분한다.
- **반응형**: 모바일에서 오른쪽 demo를 단순 이미지처럼 줄이지 말고 핵심 mock panels만 압축/스택한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #444435 as the hero's emotional base; it is the workbench color.
- Keep primary hero CTA white (#FFFFFF) with warm ink #262321.
- Build the hero around an actual code/app/dashboard composition.
- Use #8D2676 / #E3D0DF as restrained plum interaction accents.
- Put bright syntax colors only inside code/editor surfaces.
- Make nav actions rounded capsules with 44px control height.
- Use product shadows on mock/demo surfaces, not all content cards.
- Preserve the contrast between open page gutters and dense demo interiors.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — Convex hero는 `#444435` 사용.
- 히어로 다크 배경을 `#000000` 또는 `black`으로 두지 말 것 — 앱 표면은 `#141414`, 히어로는 `#444435`로 분리.
- 본문/CTA 잉크를 `#000000`으로 두지 말 것 — white CTA 텍스트 색은 `#262321` 사용.
- 브랜드를 `#3D72F5` 파랑으로 잡지 말 것 — 파랑은 앱 mock의 action이고 primary brand는 `#8D2676`.
- 보라 그라디언트 `#667EEA` → `#764BA2` 사용 금지 — Convex는 gradient mesh가 아니라 solid workbench + product mock.
- syntax colors `#FC618D`, `#948AE3`, `#7BD88F`, `#5AD4E6`를 일반 마케팅 카드 배경으로 쓰지 말 것 — editor 내부에만 사용.
- CTA를 각진 rectangle로 만들지 말 것 — primary controls는 pill radius `9999px`.
- 모든 카드에 큰 glow shadow를 주지 말 것 — deep shadow는 editor/demo chassis에만 적용.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No generic blue-black SaaS hero** — the hero is warm olive #444435, not navy.
- **No decorative orb system** — depth comes from product mockups, not floating blobs.
- **No page-wide gradient mesh** — solid surfaces and real UI carry the composition.
- **No second loud brand color** — plum is the brand accent; blue/yellow/green are product-state colors.
- **No huge centered hero stack** — headline is left aligned and shares the viewport with the demo.
- **No abstract SVG mascot as primary proof** — code/app/dashboard surfaces prove the product.
- **No serif-led identity** — `publico` exists, but the homepage voice is sans + mono.
- **No universal rainbow palette** — high-chroma colors are scoped to syntax, badges, and app state.
- **No flat screenshots without chrome** — the demo needs window frames, tabs, borders, and table rows.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual / REQUIRED -->

- **Single-page homepage snapshot** — the analysis reused existing `convex` phase1 homepage assets. Docs, pricing, dashboard, login, and product subflows were not independently visited.
- **Desktop screenshot basis** — visual interpretation used a 1280x800 hero screenshot. Mobile layout is inferred from CSS breakpoints, not visually re-captured.
- **Typography scale incomplete** — `typography.json` did not extract a full size ladder; font families and weights are CSS-derived, while some scale labels are screenshot/manual estimates.
- **Semantic alias layer is shallow** — source CSS exposes many core `--color-*` tokens but few semantic aliases. Report-level `--convex-*` aliases are implementation helpers, not original source token names.
- **Logo/customer color contamination risk** — frequency candidates include bright code and possible SVG/pattern colors. Brand color selection prioritizes interaction/plum tokens over raw frequency.
- **Form validation states not surfaced** — input focus/error/loading states are described conservatively because homepage only shows demo app input, not real form validation flows.
- **Motion logic not executed** — CSS transition tokens were observed, but JavaScript-driven scroll/reveal behavior was not traced.
- **Cookie banner overlay present in screenshot** — it affects first-viewport visual reading but is not treated as a core Convex component except where noted as an overlay/card pattern.
