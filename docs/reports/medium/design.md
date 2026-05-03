---
schema_version: 3.2
slug: medium
service_name: Medium
site_url: https://medium.com
fetched_at: 2026-05-03T06:48:12Z
default_theme: light
brand_color: "#1A8917"
primary_font: "gt-super"
font_weight_normal: 400
token_prefix: medium-home

bold_direction: Editorial Monochrome
aesthetic_category: other
signature_element: typo_contrast
code_complexity: medium

medium: web
medium_confidence: high
archetype: editorial-magazine
archetype_confidence: high
design_system_level: lv1
design_system_level_evidence: "Homepage CSS exposes almost no custom properties; the system is carried by atomic classes, proprietary fonts, and repeated editorial layout decisions."

colors:
  brand-green: "#1A8917"
  brand-green-hover: "#156D12"
  surface-paper: "#F7F4ED"
  text-primary: "#242424"
  text-muted: "#6B6B6B"
  ink-button: "#000000"
  surface-white: "#FFFFFF"
typography:
  display: "gt-super"
  body: "Sohne"
  editorial-serif: "Charter"
  ladder:
    - { token: nav, size: "14px", weight: 400, line_height: "20px" }
    - { token: hero-body, size: "22px", weight: 400, line_height: "28px" }
    - { token: hero-h1-mobile, size: "70px", weight: 400, line_height: "74px", tracking: "-0.055em" }
    - { token: hero-h1-tablet, size: "80px", weight: 400, line_height: "72px", tracking: "-0.055em" }
    - { token: hero-h1-wide, size: "120px", weight: 400, line_height: "100px", tracking: "-0.055em" }
  weights_used: [300, 400, 500, 700]
  weights_absent: [600, 800, 900]
components:
  button-dark-pill: { bg: "#000000", color: "#FFFFFF", radius: "99em", padding: "8px 16px" }
  button-green-pill: { bg: "#1A8917", color: "#FFFFFF", radius: "99em", padding: "8px 20px" }
---

# DESIGN.md - Medium

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Medium's homepage is not a SaaS landing page wearing editorial copy. It is an editorial front page with the product almost hidden inside the invitation to read. The page spends most of its first viewport on air: a warm paper field, a severe top rule, a black wordmark, and a headline so large it feels typeset rather than laid out. It has no second brand color competing for attention; the page behaves like a broadsheet whose masthead has been replaced by a product wordmark.

The whole identity depends on a single contrast: magazine display type against plain product chrome. The H1 uses `gt-super` at up to 120px with -0.055em tracking, while navigation and buttons sit in Sohne at 14px. That gap is the system. The headline is not a hero slogan so much as a first line pulled from a Sunday literary section, compressed until the letters hold together like ink on absorbent paper.

Color is intentionally under-specified. The real UI is almost monochrome: #F7F4ED (`{colors.surface-paper}`), #242424 (`{colors.text-primary}`), #000000 (`{colors.ink-button}`), and one living accent, #1A8917 (`{colors.brand-green}`). The green is not a broad palette. It is a verb: start reading, proceed, continue. In newspaper terms, `{colors.brand-green}` is the subscription slip tucked into the page, not a second ink running through the whole edition.

The top rule matters because it turns the browser viewport into a sheet. There is no glass header, no shadow, no app-shell blur; just a 1px #242424 (`{colors.text-primary}`) divider that feels like the black rule between masthead and front page. The site almost erases its own interface so the reading promise can occupy the page.

The illustration on the right is not a decorative mascot system. It behaves like old print ephemera placed into the margin: botanical green, diagram lines, and crop fragments. It is less "brand illustration" than marginalia from a magazine archive, cropped so the page looks assembled by an editor instead of decorated by a marketing template. Medium's craft is the collision of literary scale with product restraint.

### Key Characteristics

- Warm paper background #F7F4ED, not pure white.
- Oversized editorial H1 in `gt-super`, not a geometric sans.
- Tight display tracking at -0.055em.
- Body/navigation chrome in Sohne, kept small and quiet.
- One action green #1A8917 with darker hover #156D12.
- Pill buttons with `border-radius: 99em`, never rectangular CTAs.
- A fixed top navigation rule using #242424 as a literal print divider.
- Minimal component shadowing: no elevation language in the homepage CSS.
- Large empty hero field before the content lands near the lower left.
- Illustration is marginalia: cropped, right-biased, and partially off-canvas.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Editorial Monochrome
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **typo_contrast**으로 기억된다.
> **Code Complexity**: medium — atomic CSS plus proprietary font loading and responsive hero scale, but almost no component state machinery.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Medium처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Sohne", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

.hero-title {
  font-family: "gt-super", Georgia, Cambria, "Times New Roman", Times, serif;
  font-size: clamp(70px, 9.4vw, 120px);
  line-height: 0.83;
  letter-spacing: -0.055em;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #F7F4ED; --fg: #242424; }
body { background: var(--bg); color: var(--fg); }

/* 3. CTA */
:root { --brand: #1A8917; --brand-hover: #156D12; }
.cta { background: var(--brand); color: #FFFFFF; border-radius: 99em; }
```

**절대 하지 말아야 할 것 하나**: H1을 Inter/Arial 72px bold로 만들지 말 것. Medium의 첫 인상은 `gt-super` 120px, weight 400, -0.055em tracking에서 나온다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://medium.com` |
| Fetched | 2026-05-03T06:48:12Z |
| Reused phase1 | `insane-design/medium/phase1/*.json`, `css/*`, `index.html`, `screenshots/hero-cropped.png` |
| HTML size | 35,242 bytes |
| CSS files | 2 files, 20,638 chars plus 6,418 chars inline style |
| Token prefix | `medium-home` |
| Extractor | Existing phase1 artifacts; no new fetch executed |
| Method | CSS font-face and inline atomic class analysis, screenshot color sampling, manual interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Medium homepage HTML with generated atomic classes.
- **Design system**: No exposed token system on the captured homepage. `resolved_tokens.json` reports 0 CSS custom properties.
- **CSS architecture**: atomic utility classes with short generated names.
  ```text
  font assets     @font-face for gt-super, sohne, charter, noe, fell, source-serif-pro
  utility classes .dx .dy .em .dc etc. encode single properties
  inline style    carries homepage layout, hero type, CTA, and nav treatment
  ```
- **Class naming**: minified alphabetical classes (`.dx`, `.em`, `.dc`), not semantic BEM.
- **Default theme**: light, warm paper (#F7F4ED) with dark ink (#242424).
- **Font loading**: glyph.medium.com WOFF font-face declarations with `font-display: swap`.
- **Canonical anchor**: the homepage hero: "Human stories & ideas" with right-side cropped green illustration.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `gt-super` (Medium hosted proprietary display serif)
- **Body/UI font**: `Sohne` (Medium hosted proprietary sans)
- **Editorial text fonts present**: `charter`, `source-serif-pro`, `noe`, `fell`, `opendyslexic`
- **Code font**: `source-code-pro`
- **Weight normal / bold**: `400` / `700`; homepage display uses 400, Noe face exposes 500, Sohne exposes 300/400/500/700.

```css
:root {
  --medium-home-font-display: "gt-super", Georgia, Cambria, "Times New Roman", Times, serif;
  --medium-home-font-ui: "Sohne", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --medium-home-font-serif: "Charter", Georgia, Cambria, "Times New Roman", Times, serif;
  --medium-home-font-code: "source-code-pro", ui-monospace, SFMono-Regular, Menlo, monospace;
  --medium-home-font-weight-normal: 400;
  --medium-home-font-weight-bold: 700;
}
body {
  font-family: var(--medium-home-font-ui);
  font-weight: var(--medium-home-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **gt-super** is the identity font. If unavailable, use **Fraunces** only as a directional substitute, set weight 400, and tighten display tracking to around `-0.05em`. Georgia is acceptable for copy prototypes but loses the inflated, poster-like bowl shapes.
- **Sohne** can be approximated with **Inter** or **Helvetica Neue**, but avoid Inter's default crisp SaaS tone by keeping UI text at 14px/20px and never raising nav weight above 400.
- **Charter** is already close to platform/system serif traditions. If unavailable, Georgia works for article body, but keep line-height looser than UI text.
- **Do not use one font for everything**. The site needs a display serif and a quiet sans. A single Inter stack destroys the editorial/product split.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| nav-link | 14px | 400 | 20px | 0 |
| footer-link | 13px | 400 | 20px | 0 |
| hero-body | 22px | 400 | 28px | 0 |
| button | 16px | 400 | 24px | 0 |
| hero-h1-base | 70px | 400 | 74px | -0.055em |
| hero-h1-tablet | 80px | 400 | 72px | -0.055em |
| hero-h1-desktop | 106px | 400 | 95px | -0.055em |
| hero-h1-wide | 120px | 400 | 100px | -0.055em |

> ⚠️ The homepage does not expose a rich token ladder. The visible scale is a deliberate split between tiny product chrome and a huge editorial H1.

### Principles
<!-- SOURCE: manual -->

1. Display type is not bold. The hero gets force from size, compression, and serif shape, not weight 700.
2. The main optical signature is negative tracking at display sizes only. UI copy keeps normal spacing.
3. Product chrome stays at 13-16px while the H1 jumps to 70-120px. The gap is intentionally dramatic.
4. `font-weight: 600` is absent in the captured font-face set. Do not "modern SaaS" the nav with semibold links.
5. Body/editorial fonts are present but not the homepage's first-viewport voice. The homepage sells reading with display type before showing article typography.
6. Line-height gets tighter as the display gets larger: 120px text sits on 100px line-height.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (2 steps)
<!-- SOURCE: auto -->

| Token | Hex |
|---|---|
| `medium-home-brand-green` | `#1A8917` |
| `medium-home-brand-green-hover` | `#156D12` |

### 06-3. Neutral Ramp
<!-- SOURCE: auto+manual -->

| Step | Light | Dark |
|---|---|---|
| paper | `#F7F4ED` | N/A |
| white | `#FFFFFF` | N/A |
| ink | N/A | `#242424` |
| muted | N/A | `#6B6B6B` |
| black-action | N/A | `#000000` |

### 06-5. Semantic
<!-- SOURCE: auto+manual -->

| Token | Hex | Usage |
|---|---|---|
| `surface.paper` | `#F7F4ED` | hero and homepage background |
| `text.primary` | `#242424` | headline, top rule, main ink |
| `text.muted` | `#6B6B6B` | secondary/footer text |
| `action.primary` | `#1A8917` | "Start reading" button |
| `action.primary.hover` | `#156D12` | green CTA hover |
| `action.dark` | `#000000` | "Get started" nav pill hover/dark action |
| `surface.inverse` | `#FFFFFF` | text on dark and green buttons |

### 06-6. Semantic Alias Layer
<!-- SOURCE: manual -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--medium-home-bg-page` | `#F7F4ED` | full hero surface |
| `--medium-home-fg` | `#242424` | primary text and rule color |
| `--medium-home-fg-muted` | `#6B6B6B` | secondary text |
| `--medium-home-cta` | `#1A8917` | green CTA only |
| `--medium-home-cta-hover` | `#156D12` | green CTA hover |
| `--medium-home-cta-dark` | `#000000` | dark pill |

### 06-7. Dominant Colors (actual DOM/CSS + screenshot)
<!-- SOURCE: auto+manual -->

| Token | Hex | Frequency / Evidence |
|---|---|---|
| surface-paper | `#F7F4ED` | inline CSS background and dominant screenshot field |
| text-primary | `#242424` | 8 inline CSS mentions |
| brand-green | `#1A8917` | CTA background, color, and hover pair |
| text-muted | `#6B6B6B` | 3 inline CSS mentions |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.surface-paper}` (#F7F4ED)** - The homepage floor is warm paper. It lets the page feel literary without adding texture, beige decoration, or card surfaces.

**`{colors.text-primary}` (#242424)** - Ink, not pure black. It is used for headline/nav/rule structure and keeps the huge H1 from becoming harsh.

**`{colors.brand-green}` (#1A8917)** - The only action color. It belongs to start/continue actions and should not be sprayed across headings, backgrounds, badges, or illustrations.

**`{colors.text-muted}` (#6B6B6B)** - Secondary utility voice. It appears where the product needs to recede behind the editorial promise.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `nav-padding-y` | 25px | top navigation vertical rhythm |
| `nav-height` | 75px | desktop navigation height |
| `hero-margin-desktop` | 75px 64px 0 | hero content offset |
| `hero-margin-mobile` | 75px 24px 0 | mobile hero content offset |
| `footer-padding-y` | 24px | footer link band |
| `button-padding-small` | 8px 16px | dark nav pill |
| `button-padding-primary` | 8px 20px | green hero CTA |
| `content-max` | 1192px | nav/content outer width |
| `hero-copy-max` | 720px | hero text measure |
| `article-prose-max` | 680px | repeated prose max-width classes |

**주요 alias**:
- `--medium-home-space-edge` -> 64px desktop, 24px mobile (page margin)
- `--medium-home-space-nav-y` -> 25px (nav vertical padding)
- `--medium-home-space-hero-top` -> 75px (distance from nav to hero block)

### Whitespace Philosophy
<!-- SOURCE: manual -->

Medium uses whitespace like a broadsheet uses margin. The first viewport intentionally leaves a large blank upper field between the nav rule and the headline, delaying the pitch until the eye has registered paper, ink, and brand.

The lower-left hero placement matters. Centering the headline would turn it into a generic landing hero. Medium's copy sits like a headline placed on a page, with the illustration acting as cropped marginalia on the right.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `circle` | 50% | circular utility/avatar-like shape in captured CSS |
| `pill` | 99em | navigation and CTA pills |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none | `none` | Homepage chrome uses no elevation system in captured CSS. |

---

## 10. Motion
<!-- SOURCE: auto -->

| Token | Value | Usage |
|---|---|---|
| `button-bg-transition` | `background-color 300ms linear` | dark and green button hover |
| `button-color-transition` | `color 300ms linear` | paired button text transition |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: 1192px for the navigation/content shell; 720px for hero copy; 680px for prose-oriented blocks.
- **Grid type**: flex for navigation; absolute/static positioning for illustration fragments; no visible 12-column marketing grid.
- **Column count**: effectively 1 editorial text column plus right-side illustration.
- **Gutter**: page edge 64px desktop, 24px mobile.

### Hero

- **Pattern Summary**: 100vh warm paper + lower-left huge editorial H1 + cropped right-side print illustration + green CTA.
- Layout: single editorial column with illustration offset to the right.
- Background: #F7F4ED solid.
- **Background Treatment**: solid paper field; no mesh, no noise, no gradient.
- H1: `clamp(70px, 9.4vw, 120px)` / weight `400` / tracking `-0.055em`.
- Max-width: 720px for the text block.

### Section Rhythm

```css
section.hero {
  min-height: 560px;
  margin: 75px 64px 0;
  background: #F7F4ED;
}

@media (narrow) {
  section.hero {
    margin: 75px 24px 0;
  }
}
```

### Card Patterns

- **Card background**: none observed in first-viewport homepage.
- **Card border**: no card border system observed.
- **Card radius**: no card radius system; pills only.
- **Card padding**: N/A for homepage hero.
- **Card shadow**: none.

### Navigation Structure

- **Type**: horizontal desktop nav.
- **Position**: fixed/top in captured class set, visually top-aligned.
- **Height**: 75px.
- **Background**: #F7F4ED/white depending shell segment; hero nav appears on warm paper.
- **Border**: bottom 1px #242424 rule.

### Content Width

- **Prose max-width**: 680px.
- **Container max-width**: 1192px.
- **Sidebar width**: N/A on homepage.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | <= 720px | external CSS has one media rule; inline style exposes reduced hero margin and 70px H1. |
| Tablet | inferred from inline classes | H1 80px/72px appears as intermediate scale. |
| Desktop | inferred from inline classes | H1 106px/95px and 120px/100px variants appear for larger widths. |
| Large | 1192px shell | navigation/content max width. |

### Touch Targets

- **Minimum tap size**: button visual height around 40px from nav utility class; near but below 44px target.
- **Button height (mobile)**: 40px observed for nav pill class.
- **Input height (mobile)**: no input on captured homepage.

### Collapsing Strategy

- **Navigation**: likely hides secondary links on narrow screens; captured HTML includes repeated display-none utility classes, but exact menu state not fully measured.
- **Grid columns**: no grid collapse; hero remains one-column text plus illustration treatment.
- **Sidebar**: N/A.
- **Hero layout**: headline scale drops from 120px to 70px and edge margin drops from 64px to 24px.

### Image Behavior

- **Strategy**: right-side decorative illustration is cropped/off-canvas rather than scaled as content media.
- **Max-width**: illustration not represented as a normal responsive image in extracted summary.
- **Aspect ratio handling**: not measured beyond screenshot.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Dark nav pill**

```html
<a class="button button-dark-pill">Get started</a>
```

| Spec | Value |
|---|---|
| Background | `#000000` / `rgba(25, 25, 25, 1)` |
| Text | `#FFFFFF` |
| Radius | `99em` |
| Padding | `8px 16px` |
| Font | Sohne, 14-16px |
| Transition | `background-color 300ms linear, color 300ms linear` |
| Hover | `#000000` |

**Green hero pill**

```html
<a class="button button-green-pill">Start reading</a>
```

| Spec | Value |
|---|---|
| Background | `#1A8917` |
| Hover background | `#156D12` |
| Text | `#FFFFFF` |
| Radius | `99em` |
| Padding | `8px 20px` |
| Font | Sohne, 16px/24px |

### Badges

> N/A - No badge/chip system appears in the captured homepage.

### Cards & Containers

> N/A - The first-viewport homepage avoids cards. This is part of the identity: paper and type carry the structure.

### Navigation

```html
<nav class="medium-nav">
  <a class="wordmark">Medium</a>
  <a>Our story</a>
  <a>Membership</a>
  <a>Write</a>
  <a>Sign in</a>
  <a class="button-dark-pill">Get started</a>
</nav>
```

| Spec | Value |
|---|---|
| Height | 75px |
| Edge padding | 64px desktop |
| Link font | Sohne 14px/20px |
| Link color | #242424 |
| Divider | 1px #242424 bottom rule |
| CTA | black pill at right |

### Inputs & Forms

> N/A - No inputs or form states are visible in the captured homepage.

### Hero Section

```html
<section class="medium-hero">
  <h1>Human stories & ideas</h1>
  <p>A place to read, write, and deepen your understanding</p>
  <a class="button-green-pill">Start reading</a>
</section>
```

| Spec | Value |
|---|---|
| Background | #F7F4ED |
| Min-height | 560px, with body 100vh |
| H1 font | gt-super |
| H1 max size | 120px/100px |
| H1 tracking | -0.055em |
| Body copy | 22px/28px |
| CTA | #1A8917 pill |
| Illustration | cropped right-side green/ink print graphic |

### 13-2. Named Variants
<!-- SOURCE: manual -->

- `button-dark-pill` - black nav CTA; 99em radius, compact 8px 16px padding, white text, 300ms linear background transition.
- `button-green-pill` - primary reading CTA; #1A8917 background, #156D12 hover, 8px 20px padding, 99em radius.
- `hero-editorial-title` - gt-super display serif, 70-120px, 0.83-1.06 line-height range, -0.055em tracking.
- `nav-print-rule` - fixed top navigation with a literal #242424 hairline, closer to print divider than app chrome.

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
editorial-compression-title:
  description: "Medium's homepage H1 feels typeset, not merely scaled up."
  technique: "font-family: gt-super; font-size: 120px; line-height: 100px; letter-spacing: -0.055em; font-weight: 400"
  applied_to: ["{component.hero-editorial-title}"]
  visual_signature: "letters knit into a dense literary block, like ink pressed into a front-page headline"

paper-ink-divider:
  description: "The nav separates the page with a print rule rather than app chrome."
  technique: "height: 75px; background: #F7F4ED; border-bottom: 1px solid #242424; box-shadow: none"
  applied_to: ["{component.nav-print-rule}", "{component.medium-nav}"]
  visual_signature: "the viewport reads as a sheet of paper with a masthead rule"

single-verb-green-cta:
  description: "Green is reserved for the reading action and never becomes a decorative palette."
  technique: "background: #1A8917; hover background: #156D12; color: #FFFFFF; border-radius: 99em; no green gradient"
  applied_to: ["{component.button-green-pill}"]
  visual_signature: "the only chromatic instruction on the page is begin"

broadsheet-air-field:
  description: "The hero opens with a large warm-paper field before copy lands low on the page."
  technique: "background: #F7F4ED; min-height: 560px; margin: 75px 64px 0; hero max-width: 720px"
  applied_to: ["{component.medium-hero}"]
  visual_signature: "empty paper carries as much identity as the headline itself"

marginalia-illustration-crop:
  description: "The hero artwork enters as cropped print ephemera instead of centered brand illustration."
  technique: "right-biased cropped composition; black diagram lines with green botanical block; no shadow or card frame"
  applied_to: ["{component.medium-hero}", "hero visual only"]
  visual_signature: "a magazine archive fragment sits in the margin without turning into a mascot system"
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Short, human, abstract enough to cover reading and writing. | "Human stories & ideas" |
| Subheading | One sentence, plain verb sequence. | "A place to read, write, and deepen your understanding" |
| Primary CTA | Action starts with reading, not signup mechanics. | "Start reading" |
| Navigation | Product/business links in quiet prose nouns. | "Our story", "Membership", "Write" |
| Tone | Literary confidence with almost no feature explanation. | N/A |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Medium homepage - copy into your root stylesheet */
:root {
  /* Fonts */
  --medium-home-font-display: "gt-super", Georgia, Cambria, "Times New Roman", Times, serif;
  --medium-home-font-ui: "Sohne", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --medium-home-font-serif: "Charter", Georgia, Cambria, "Times New Roman", Times, serif;
  --medium-home-font-code: "source-code-pro", ui-monospace, SFMono-Regular, Menlo, monospace;
  --medium-home-font-weight-normal: 400;
  --medium-home-font-weight-bold: 700;

  /* Colors */
  --medium-home-bg-page: #F7F4ED;
  --medium-home-text: #242424;
  --medium-home-text-muted: #6B6B6B;
  --medium-home-brand: #1A8917;
  --medium-home-brand-hover: #156D12;
  --medium-home-action-dark: #000000;
  --medium-home-on-action: #FFFFFF;

  /* Key spacing */
  --medium-home-edge-desktop: 64px;
  --medium-home-edge-mobile: 24px;
  --medium-home-nav-height: 75px;
  --medium-home-hero-top: 75px;
  --medium-home-prose-max: 680px;
  --medium-home-hero-max: 720px;
  --medium-home-shell-max: 1192px;

  /* Radius */
  --medium-home-radius-pill: 99em;
}

body {
  margin: 0;
  background: var(--medium-home-bg-page);
  color: var(--medium-home-text);
  font-family: var(--medium-home-font-ui);
  font-weight: 400;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}

.medium-hero-title {
  font-family: var(--medium-home-font-display);
  font-size: clamp(70px, 9.4vw, 120px);
  line-height: 0.83;
  letter-spacing: -0.055em;
  font-weight: 400;
  margin: 0;
}

.medium-button-green {
  background: var(--medium-home-brand);
  color: var(--medium-home-on-action);
  border-radius: var(--medium-home-radius-pill);
  padding: 8px 20px;
  transition: background-color 300ms linear, color 300ms linear;
}

.medium-button-green:hover {
  background: var(--medium-home-brand-hover);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js - Medium homepage approximation
module.exports = {
  theme: {
    extend: {
      colors: {
        medium: {
          paper: '#F7F4ED',
          ink: '#242424',
          muted: '#6B6B6B',
          green: '#1A8917',
          greenHover: '#156D12',
          black: '#000000',
          white: '#FFFFFF',
        },
      },
      fontFamily: {
        display: ['gt-super', 'Georgia', 'Cambria', 'Times New Roman', 'serif'],
        sans: ['Sohne', 'Helvetica Neue', 'Helvetica', 'Arial', 'sans-serif'],
        serif: ['Charter', 'Georgia', 'Cambria', 'Times New Roman', 'serif'],
      },
      letterSpacing: {
        mediumDisplay: '-0.055em',
      },
      borderRadius: {
        pill: '99em',
      },
      maxWidth: {
        mediumShell: '1192px',
        mediumHero: '720px',
        mediumProse: '680px',
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
| Brand primary | `--medium-home-brand` | `#1A8917` |
| Brand hover | `--medium-home-brand-hover` | `#156D12` |
| Background | `--medium-home-bg-page` | `#F7F4ED` |
| Text primary | `--medium-home-text` | `#242424` |
| Text muted | `--medium-home-text-muted` | `#6B6B6B` |
| Dark CTA | `--medium-home-action-dark` | `#000000` |
| On action | `--medium-home-on-action` | `#FFFFFF` |

### Example Component Prompts

#### Hero Section

```text
Medium homepage style hero section:
- Background: #F7F4ED
- H1: gt-super, clamp(70px, 9.4vw, 120px), weight 400, line-height 0.83, tracking -0.055em
- Subtext: Sohne, 22px/28px, color #242424
- CTA: #1A8917 background, #FFFFFF text, #156D12 hover, radius 99em, padding 8px 20px
- Layout: lower-left editorial block with large warm paper whitespace and right-side cropped print illustration
```

#### Card Component

```text
Do not create a standard marketing card. Medium homepage style uses paper, type, and rules instead:
- Background: #F7F4ED or #FFFFFF only when content requires a readable surface
- Border: use 1px #242424 for structural print rules, not decorative card outlines
- Radius: no card radius; reserve 99em for action pills
- Shadow: none
- Title: gt-super only if it is editorial display, otherwise Sohne 16px/24px
```

#### Badge

```text
Medium homepage does not use badges. If a label is unavoidable:
- Use Sohne 13px/20px
- Color #6B6B6B
- No border, no filled chip, no icon
- Keep it as quiet inline metadata rather than a pill badge
```

#### Navigation

```text
Medium-style top navigation:
- Height: 75px
- Background: #F7F4ED
- Bottom rule: 1px solid #242424
- Logo: black wordmark at left
- Links: Sohne 14px/20px, weight 400, color #242424
- CTA: right black pill, #000000 background, #FFFFFF text, radius 99em, padding 8px 16px
```

### Iteration Guide

- **색상 변경 시**: #1A8917은 CTA에만 쓴다. heading이나 badge 색으로 확장하지 않는다.
- **폰트 변경 시**: display serif와 UI sans를 분리한다. 하나의 sans로 통일하지 않는다.
- **여백 조정 시**: hero top air를 줄이지 않는다. 첫 viewport의 빈 공간이 브랜드다.
- **컴포넌트 추가 시**: 카드, 그림자, gradient를 만들기 전에 print rule과 type hierarchy로 해결한다.
- **반응형**: H1은 크기만 줄이는 것이 아니라 line-height도 같이 압축한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #F7F4ED as the homepage paper background.
- Use #242424 for primary ink, wordmark, headline, and structural rule.
- Use `gt-super` for hero display type with weight 400.
- Keep H1 tracking tight at about -0.055em.
- Use #1A8917 only for primary reading actions.
- Use 99em pill radius for CTAs.
- Preserve large empty vertical space between nav and hero copy.
- Treat illustration as cropped print marginalia, not a centered hero graphic.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#F7F4ED` 사용.
- 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 기본 본문/헤드라인은 `#242424` 사용.
- CTA를 `#000000`으로만 두지 말 것 — primary reading action은 `#1A8917` 사용.
- CTA hover를 `#1A8917` 그대로 두지 말 것 — hover에는 `#156D12` 사용.
- muted text를 `#999999`나 `#808080`으로 임의 대체하지 말 것 — `#6B6B6B` 사용.
- hero 배경에 `#F5F5F7` 같은 Apple식 cool gray를 쓰지 말 것 — Medium은 warm paper `#F7F4ED`.
- H1에 `font-weight: 700` 사용 금지 — hero display는 400이 맞다.
- H1 letter-spacing을 `0`으로 두지 말 것 — display에는 `-0.055em` 수준의 압축이 필요하다.
- CTA를 8px radius rectangle로 만들지 말 것 — `border-radius: 99em` pill이어야 한다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- Brand gradient: absent. There is no green gradient, mesh, or neon wash.
- Second brand color: none. #1A8917 carries the action role alone.
- Card elevation: none in the homepage hero. No box-shadow language defines the first viewport.
- Rounded cards: absent. Radius belongs to pills, not content containers.
- Semibold SaaS nav: absent. Links stay quiet at 14px/20px and weight 400.
- Blue links as primary action: never for the homepage CTA; green is the action color.
- Dense feature grid: absent. The homepage opens with editorial promise, not a three-card feature section.
- Icon-led UI: absent. Text and type carry meaning before icons.
- Pure white landing surface: absent in the hero. The page starts on warm paper.
- Heavy animation: absent. Captured motion is only a 300ms linear button color transition.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single-page scope** - This guide covers the captured `https://medium.com` homepage. Article pages, member pages, editor flows, and logged-in surfaces can use different typography and component systems.
- **Token system not exposed** - `resolved_tokens.json` reports 0 CSS custom properties. Role names in this document are guide aliases derived from observed CSS values, not official Medium token names.
- **Screenshot color sampling is secondary** - The right-side illustration contains greens beyond #1A8917, but those were treated as artwork colors, not UI tokens.
- **Responsive behavior partially inferred** - The capture includes inline classes for 70/80/106/120px H1 sizes and a `width <= 720px` CSS rule, but not a full viewport matrix.
- **Navigation mobile state not fully observed** - Hidden/display utility classes exist, but no interactive mobile menu was exercised.
- **Form states absent** - Inputs, validation, errors, loading, disabled form states, and editor controls are not present in the captured homepage.
- **Motion analysis is CSS-only** - The observed transition is 300ms linear button color. Scroll-triggered or JS animation behavior was not analyzed.
- **Font licensing not resolved** - Medium-hosted WOFF files identify proprietary family names, but this guide does not grant usage rights. Use substitutes where needed.
- **Illustration asset not decomposed** - The hero artwork was visually inspected from the screenshot; exact SVG/path colors and crop math were not extracted.
