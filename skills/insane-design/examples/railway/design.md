---
schema_version: 3.2
slug: railway
service_name: Railway
site_url: https://railway.com
fetched_at: 2026-04-20T20:00:00+09:00
default_theme: dark
brand_color: "#6D4BBC"
primary_font: "Inter"
font_weight_normal: 400
token_prefix: "tw"

bold_direction: "Cosmic Console"
aesthetic_category: "Refined SaaS"
signature_element: "hero_impact"
code_complexity: high

medium: web
medium_confidence: high
archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Production CSS exposes Tailwind utilities, Mantine primitives, app-canvas shadows, and Railway-specific train/hero tokens."

colors:
  night-base: "#13111C"
  night-ink: "#08070C"
  text-primary: "#FFFFFF"
  text-muted: "#FFFFFF80"
  accent-purple: "#6D4BBC"
  accent-deep: "#13044C"
  rail-oatmeal: "#F1F0EF"
  border-ghost: "#FFFFFF1A"
typography:
  display: "IBM Plex Serif"
  body: "Inter"
  tight: "Inter Tight"
  code: "JetBrains Mono"
  ladder:
    - { token: hero-h1, size: "56px", weight: 700, tracking: "-0.02em" }
    - { token: nav, size: "14px", weight: 500, tracking: "0" }
    - { token: body, size: "20px", weight: 400, tracking: "0" }
    - { token: code-ui, size: "12px", weight: 500, tracking: "0" }
  weights_used: [400, 500, 600, 700, 800, 900]
  weights_absent: []
components:
  button-primary: { bg: "{colors.accent-purple}", fg: "{colors.text-primary}", radius: "8px", padding: "14px 24px" }
  button-ghost: { bg: "transparent", fg: "{colors.text-primary}", border: "1px solid {colors.border-ghost}", radius: "8px" }
  app-canvas-frame: { bg: "{colors.night-ink}", border: "1px solid {colors.border-ghost}", shadow: "var(--nested-canvas-shadow)" }
---

# DESIGN.md - Railway

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Railway does not sell cloud infrastructure as a dashboard. It stages deployment as a night journey: the page opens on #13111C (`{colors.night-base}`), then places a soft illustrated sky inside a rounded viewport like a train window. The product UI is not a generic SaaS mockup floating in space; it is a console parked at the bottom of the hero, half visible, as if the visitor is already looking into the platform.

The frame behaves like an overnight observation car: outside is the violet-black weather of #13111C (`{colors.night-base}`), inside is the app surface of #08070C (`{colors.night-ink}`), and the console is cropped as though the train has already pulled into the platform. The page has very little "website" self-consciousness. It removes the brochure wall and gives the deployment scene the stage.

The brand tension is unusual: the headline is calm, almost literary, while the product promise is technical. "Ship software peacefully" uses a serif display face over a dark star field. That one choice prevents the site from becoming another cold developer tool. Railway's voice is infrastructure with bedside manner: a dispatch board written by someone who still believes operations can be quiet.

Color is restrained. The page is essentially dark ink, white type, translucent hairlines, and one purple action color. #6D4BBC (`{colors.accent-purple}`) is used like a signal lamp, not a decorative wash. The deeper #13044C (`{colors.accent-deep}`) appears in train-specific tokens and keeps the railway metaphor from becoming cartoonish.

There is no second brand color waiting in the wings. Purple does not become confetti, aurora, or corporate gradient wallpaper; it stays closer to a platform signal at night. #FFFFFF1A (`{colors.border-ghost}`) is the real architecture: thin rails, window seams, and console edges that let dark surfaces separate without turning into chrome.

The UI chrome borrows from real app surfaces: tab bars, mono labels, dotted grids, sync/create controls, and nested-canvas shadows. These are not ornamental screenshots. They tell the viewer that the marketing layer and product layer share a visual grammar.

Railway's shadow language is also train-window logic, not card-stack logic. Depth sits on the app canvas and product proof, while navigation stays almost weightless. The nested canvas shadow reads like glass reflection on a dark control room panel: present enough to show the pane, restrained enough that the night outside still feels continuous.

### Key Characteristics

- Dark-first marketing surface anchored by #13111C, with white text and translucent borders.
- Serif hero headline over a technical app-console reveal.
- Purple CTA is the only strong chromatic action; secondary actions stay transparent.
- Rounded hero media frame uses a soft border, not a heavy card shell.
- Product UI mockup sits low in the hero and is cropped by the viewport.
- Navigation is quiet, horizontal, and text-led; no oversized marketing nav chrome.
- App details use monospace and tabular microcopy to signal developer tooling.
- Shadows are mostly nested black/white opacity stacks, not large ambient glows.
- Railway-specific train tokens exist, but the homepage hero keeps the metaphor atmospheric.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Cosmic Console
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **night-sky hero with a cropped deployment console**으로 기억된다.
> **Code Complexity**: high — layered Tailwind utilities, Mantine primitives, custom train tokens, nested app shadows, and responsive hero choreography.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Railway처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Font pairing */
body {
  font-family: var(--font-inter), -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}

.hero-title {
  font-family: var(--font-ibm-plex-serif), Georgia, Cambria, "Times New Roman", serif;
  font-weight: 700;
  letter-spacing: -0.02em;
}

/* 2. Night surface */
:root {
  --railway-bg: #13111C;
  --railway-ink: #08070C;
  --railway-fg: #FFFFFF;
  --railway-muted: #FFFFFF80;
}

/* 3. One action color */
:root { --railway-accent: #6D4BBC; }
.button-primary { background: var(--railway-accent); color: #FFFFFF; }
```

**절대 하지 말아야 할 것 하나**: body 전체를 밝은 #FFFFFF SaaS 랜딩으로 바꾸지 말 것. Railway의 인상은 dark stage + calm serif + cropped console에서 나온다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://railway.com` |
| Fetched | 2026-04-20 20:00 KST |
| Extractor | phase1 reuse: existing HTML/CSS/JSON/screenshots |
| HTML size | 230275 bytes |
| CSS files | 11 external CSS files, about 1368894 chars |
| Token prefix | `tw` plus `mantine`, `train`, `flip`, `nested-canvas` custom properties |
| Method | CSS custom property extraction, frequency counts, screenshot observation, targeted HTML metadata parse |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React/Next-style marketing app inferred from generated CSS bundles and app markup.
- **Design system**: Tailwind utility layer + Mantine component primitives + Railway-specific custom tokens.
- **CSS architecture**:
  ```css
  --tw-*                 /* Tailwind runtime utility state */
  --mantine-*            /* component primitives: button/input/badge/tabs */
  --train-*              /* Railway illustration and motion tokens */
  --nested-canvas-shadow /* product-console depth token */
  ```
- **Class naming**: Tailwind atomic utilities with escaped arbitrary values, plus generated Mantine classes.
- **Default theme**: dark (`theme-color` = #13111C).
- **Font loading**: CSS variable families for `Inter`, `Inter Tight`, `IBM Plex Serif`, and `JetBrains Mono`.
- **Canonical anchor**: homepage hero screenshot, 1280x800 crop, dark nav + star field + cropped app console.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `IBM Plex Serif` via `var(--font-ibm-plex-serif)` for the hero's editorial calm.
- **Body font**: `Inter` via `var(--font-inter)` for nav, paragraphs, and UI text.
- **Tight display/support**: `Inter Tight` appears as `var(--font-inter-tight)` for compressed marketing headings.
- **Code/UI font**: `JetBrains Mono` and `ui-monospace` for developer surfaces.
- **Weight normal / bold**: `400` / `700`; supporting UI also uses `500`, `600`, `800`, `900`.

```css
:root {
  --font-sans: var(--font-inter), -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-serif: var(--font-ibm-plex-serif), ui-serif, Georgia, Cambria, "Times New Roman", serif;
  --font-tight: var(--font-inter-tight), var(--font-inter), -apple-system, sans-serif;
  --font-code: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
}
```

### Note on Font Substitutes

- **IBM Plex Serif** — Use `Source Serif 4` or `Georgia` only for the large hero headline. Keep weight at 700 and tighten tracking to about `-0.02em`; otherwise the headline loses the "peaceful" editorial voice.
- **Inter** — Use `system-ui` only if Inter is unavailable. Do not switch to geometric display fonts; Railway needs neutral product clarity under the serif hero.
- **JetBrains Mono** — Use `SF Mono` or `Menlo` for console tabs and micro labels. Keep code text small and steady; do not enlarge mono labels into decoration.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `hero-h1` | ~56px desktop | 700 | ~1.05 | -0.02em |
| `hero-subtitle` | ~20px | 400 | 1.5 | 0 |
| `nav-link` | ~14px | 500 | 1.4 | 0 |
| `cta-label` | ~20px | 600 | 1.2 | 0 |
| `console-tab` | ~12px | 500 | 1.2 | 0 |
| `body` | 16-18px | 400 | 1.5 | 0 |

> ⚠️ Key insight: Railway's typographic identity is the mismatch between a peaceful serif hero and exact product UI text. Do not make everything Inter.

### Principles

1. Hero display uses a serif because the message is emotional, not just operational.
2. Product chrome returns immediately to Inter and monospace, so the page never drifts into lifestyle editorial.
3. Body copy remains normal weight 400; weight 500/600 is saved for navigation, buttons, tabs, and control labels.
4. Large type is optically tight; small UI text keeps neutral tracking to preserve console legibility.
5. Monospace is contextual only. It belongs in logs, tabs, paths, and deployment surfaces, not in the main marketing headline.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed key colors)

| Token | Hex |
|---|---|
| `accent-purple` | #6D4BBC |
| `accent-deep` / `--train-accent` | #13044C |
| `violet-support` | #59497A |
| `purple-glow` | #853BCE |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `night-base` | #13111C |
| `night-ink` | #08070C |
| `flip-bg` | #121118 |
| `dark-ui` | #141414 |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white text | #FFFFFF | #FFFFFF |
| muted text / border | #FFFFFF80 | #FFFFFF1A |
| oatmeal illustration | #F1F0EF | #E7E5E3 |
| gray line | #9CA3AF | #454545 |
| deep stroke | #262626 | #000000 |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Purple CTA | primary action | #6D4BBC |
| Deep rail accent | illustration / metaphor | #13044C |
| Pink utility | glow / ring support | #F9A8D4 |
| Blue utility | ring / gradient support | #93C5FD80 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `theme-color` | #13111C | browser/theme surface |
| `text-primary` | #FFFFFF | hero/nav/button text |
| `text-muted` | #FFFFFF80 | subdued UI labels |
| `border-ghost` | #FFFFFF1A | dark hairlines and frame borders |
| `console-bg` | #08070C | product mockup surface |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--button-color` | `--mantine-color-white` | button foreground |
| `--button-height-sm` | 36px | small Mantine button base |
| `--button-padding-x-sm` | 18px | compact horizontal CTA rhythm |
| `--input-bg` | `--mantine-color-dark-6` / transparent variants | dark app inputs |
| `--nested-canvas-shadow` | multi-layer black/white alpha shadow | deployment canvas depth |

### 06-7. Dominant Colors (실제 DOM/CSS 빈도 순)

| Token | Hex | Frequency note |
|---|---|---|
| transparent reset | #00000000 / #0000 | reset and utility base |
| white | #FFFFFF / #fff | text, inverted utilities |
| night ink | #08070C | dark app/hero surface |
| night base | #13111C | theme and page base |
| translucent white | #FFFFFF1A | borders, overlays |
| translucent black | #0000001A | shadows, outlines |

### 06-8. Color Stories

**`{colors.night-base}` (#13111C)** — This is the page's real floor. It is not pure black; the small violet warmth lets the night-sky illustration and app console feel integrated rather than pasted on.

**`{colors.text-primary}` (#FFFFFF)** — White carries brand confidence. Railway does not tint the primary text blue or purple; it keeps the message readable and lets the action color do less work.

**`{colors.accent-purple}` (#6D4BBC)** — The action signal. Use it for the primary Deploy CTA and small active indicators, not for every card, icon, or heading.

**`{colors.border-ghost}` (#FFFFFF1A)** — The structural color. Most frames are held together by translucent hairlines so the dark UI can stay calm without disappearing.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `gap-tight` | 6px / 8px | nav chevrons, console controls |
| `gap-sm` | 1rem | button groups, small stacks |
| `gap-md` | 1.5rem / 2rem | hero copy and CTA rhythm |
| `gap-lg` | 4rem | major layout separation |
| `gap-xl` | 6rem / 8rem | large marketing sections |
| `container` | 1280px | outer hero/nav width |

**주요 alias**:
- `--button-padding-x-sm` -> 18px (small primary and secondary action rhythm)
- `--button-height-sm` -> 36px (Mantine small control baseline)
- `--input-height-sm` -> 36px (console/form control baseline)

### Whitespace Philosophy

Railway's whitespace is not bright-page spaciousness. It is dark-stage spacing: the nav is compact, the hero headline gets a centered pocket of air, and the app mockup rises from below to occupy the lower third. The empty space above the console matters because it makes the star field feel like atmosphere instead of a background texture.

The system compresses product UI details inside the console while leaving the marketing claim alone in the center. That contrast is the page's rhythm: quiet claim, dense proof.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `radius-sm` | 4px / .25rem | small controls, utility boxes |
| `radius-md` | 6px / .375rem | Mantine defaults, compact surfaces |
| `radius-lg` | 8px / .5rem | hero buttons, console controls |
| `radius-xl` | 12px / .75rem | cards and framed UI blocks |
| `radius-hero` | ~16px | large hero media frame |
| `radius-pill` | 9999px / 1000px | badges, indicators |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `nested-canvas-dark` | `0 0 0 1px #FFFFFF1F, 0 2px 8px -2px #00000040, 0 4px 16px -4px #00000040` | dark app canvas frame |
| `soft-card` | `0 1px 2px 0 #0000000D` | small raised controls |
| `deep-modal` | `0 25px 50px -12px #00000040` | overlays and deep surfaces |
| `purple-glow` | `0px 0px 12px #B428B480, 0px 0px 32px #662BDF80` | rare glow moments |
| `hero-console` | `0 10px 30px #00000059` | dark product mockup depth |

Railway's shadows are mostly structural. The page does not rely on broad blur clouds; it uses thin border plus layered alpha to separate dark surfaces.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `--transition-easing` | `cubic-bezier(.455, .03, .515, .955)` | custom smooth transition curve |
| `--train-scroll-distance` | 210px-640px variants | railway illustration choreography |
| `--train-scroll-distance-mobile` | 76px-440px variants | mobile motion distance tuning |
| `--flip-width` / `--flip-height` | 60px / 70px | flip/ticker component dimensions |
| `prefers-reduced-motion` | present | reduced motion branch in CSS |

Motion identity is implied by the train tokens and console state changes. Keep transitions smooth and short; avoid playful bounce unless it is directly tied to a deployment/train metaphor.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: 1280px is the strongest outer width; supporting widths include 1024px, 1100px, 1200px, 1440px, and 1536px utilities.
- **Grid type**: Tailwind flex/grid utilities, with app-console internals using tab and pane structures.
- **Column count**: hero is visually one-column centered; lower product frame behaves as a wide single canvas.
- **Gutter**: common gaps are 1rem, 1.5rem, 2rem, 4rem, 6rem, and 8rem.

### Hero

- **Pattern Summary**: `dark full-width shell + centered serif H1 + dual CTA + bottom-cropped app console`
- Layout: centered headline and CTA stack over a large framed background, with product UI mockup anchored low.
- Background: illustrated night sky with cloud/star texture inside a rounded frame.
- **Background Treatment**: image/illustration overlay on #13111C, softened by dark tint and translucent frame border.
- H1: `~56px` / weight `700` / tracking `-0.02em`, serif.
- Max-width: content visually centered around 760px; outer frame spans near 1280px.

### Section Rhythm

```css
section {
  padding: clamp(64px, 8vw, 128px) clamp(16px, 4vw, 32px);
  max-width: 1280px;
}
```

### Card Patterns

- **Card background**: dark ink #08070C or translucent dark panels.
- **Card border**: 1px solid #FFFFFF1A / #FFFFFF1F.
- **Card radius**: 8px for controls, 12-16px for large frames.
- **Card padding**: compact controls around 8-18px; product frames use denser internal spacing.
- **Card shadow**: nested canvas shadow, not bright elevation.

### Navigation Structure

- **Type**: horizontal marketing nav with dropdown chevrons.
- **Position**: top aligned, visually integrated with the dark page.
- **Height**: compact; about 72px in the screenshot.
- **Background**: #13111C / near-transparent dark.
- **Border**: none visible in the top nav; hero frame provides the first major line.

### Content Width

- **Prose max-width**: 65ch appears in CSS utilities.
- **Container max-width**: 1280px primary, with wider 1440/1536 utilities available.
- **Sidebar width**: not a homepage marketing primitive; product mockup uses internal tab/pane layout instead.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `width<=40em` / `width<=768px` | compact nav/hero and reduced train distances |
| Tablet | `width>=640px`, `width>=768px` | Tailwind standard utility ramps |
| Desktop | `width>=1024px`, `width>=1080px` | desktop hero/app-canvas layout |
| Large | `width>=1280px`, `width>=1536px`, `width>=1900px` | large container expansion |

### Touch Targets

- **Minimum tap size**: Mantine base controls include 30/36/42/50/60px heights; use 42px+ for primary mobile CTAs.
- **Button height (mobile)**: target 42px or 50px, even though small variants exist.
- **Input height (mobile)**: 42px recommended; CSS has 30-60px input scale.

### Collapsing Strategy

- **Navigation**: desktop horizontal nav should collapse to compact menu; avoid preserving all links on narrow screens.
- **Grid columns**: marketing sections should collapse from multi-column utilities into single column below 768px.
- **Sidebar**: no persistent sidebar in homepage hero; product mockup should crop or simplify.
- **Hero layout**: keep headline and CTA centered; reduce console height and crop more aggressively on mobile.

### Image Behavior

- **Strategy**: images and videos use `max-width: 100%; height: auto`.
- **Max-width**: hero frame fills available container width with stable rounded bounds.
- **Aspect ratio handling**: app canvas should be clipped rather than squeezed; preserve console proportions.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

Primary action is a purple rounded rectangle, roughly 8px radius, with white text and a right arrow. It should feel like a product action, not a glossy marketing pill.

```html
<a class="button button-primary" href="/new">
  Deploy <span aria-hidden="true">-></span>
</a>
```

| State | Background | Border | Text | Notes |
|---|---|---|---|---|
| default | #6D4BBC | transparent | #FFFFFF | primary Deploy CTA |
| hover | slightly brighter purple | transparent | #FFFFFF | subtle lift/brightness only |
| secondary | transparent | #FFFFFF1A | #FFFFFF | Demo button |
| disabled | #FFFFFF1A | transparent | #FFFFFF80 | keep dark-page contrast |

### Badges

Badges are secondary primitives. Use 1000px radius when needed, but keep them small and quiet. Railway's homepage hero does not depend on badge clutter.

### Cards & Containers

The defining container is the app-canvas frame: black-violet surface, thin translucent border, and nested shadow. Avoid white cards on the dark hero.

```css
.app-canvas-frame {
  background: #08070C;
  border: 1px solid #FFFFFF1A;
  border-radius: 8px;
  box-shadow: 0 0 0 1px #FFFFFF1F, 0 2px 8px -2px #00000040, 0 4px 16px -4px #00000040;
}
```

### Navigation

Navigation pairs the Railway mark with text links: Product, Developers, Enterprise, Company, Pricing, Sign in, Book a demo. Dropdown chevrons are small. Do not put nav links into filled pills.

### Inputs & Forms

Inputs inherit Mantine scale: 30px, 36px, 42px, 50px, 60px. Dark variants use #2E2E2E / #3B3B3B style surfaces, transparent borders, and focus color mapped to the primary filled color.

### Hero Section

The hero is the signature component. It combines a framed scenic background, centered serif claim, two CTAs, and cropped product UI. The bottom crop is important: the console is evidence, not the entire composition.

### 13-2. Named Variants

- **button-primary-deploy** — #6D4BBC background, white label, right arrow, 8px radius.
- **button-secondary-demo** — transparent fill, #FFFFFF1A border, white label, same radius.
- **app-canvas-frame** — #08070C surface, #FFFFFF1A border, nested dark/white shadow.
- **console-tab-active** — thin purple underline or accent on dark tab bar.
- **railway-train-illustration** — oatmeal train body, #13044C accent, dark stroke.

### 13-3. Signature Micro-Specs

```yaml
night-window-hero-frame:
  description: "Hero scenery is held inside a rounded viewport instead of becoming a full-bleed wallpaper."
  technique: "max-width: 1280px; min-height: 720px; border: 1px solid #FFFFFF1A; border-radius: 16px; overflow: hidden; background: linear-gradient(180deg, #13111C66 0%, #13111CCC 100%), #13111C"
  applied_to: ["{component.Hero Section}", "{component.app-canvas-frame}"]
  visual_signature: "A nocturnal train-window frame: soft sky above, cropped product console below, no bright SaaS page shell."

cropped-console-proof:
  description: "The product UI is evidence rising from the bottom edge, not a complete centered dashboard card."
  technique: "background: #08070C; border: 1px solid #FFFFFF1A; border-radius: 8px 8px 0 0; box-shadow: 0 0 0 1px #FFFFFF1F, 0 2px 8px -2px #00000040, 0 4px 16px -4px #00000040"
  applied_to: ["{component.app-canvas-frame}", "{component.console-tab-active}"]
  visual_signature: "A dark deployment console clipped by the hero viewport, like a control panel glimpsed through glass."

serif-peace-deployment-headline:
  description: "The central promise is literary and calm while surrounding UI returns to technical sans and mono."
  technique: "font-family: var(--font-ibm-plex-serif), Georgia, Cambria, 'Times New Roman', serif; font-size: clamp(44px, 5vw, 64px); line-height: 1.05; letter-spacing: -0.02em; font-weight: 700"
  applied_to: ["{component.Hero Section}"]
  visual_signature: "The phrase 'Ship software peacefully' feels like a quiet station sign instead of a devtool slogan."

purple-signal-lamp-cta:
  description: "Purple is reserved for action and active product states, never spread across the whole scene."
  technique: "background: #6D4BBC; color: #FFFFFF; min-height: 58px; padding: 0 24px; border-radius: 8px; secondary action remains transparent with border: 1px solid #FFFFFF1A"
  applied_to: ["{component.button-primary}", "{component.button-secondary}", "{component.console-tab-active}"]
  visual_signature: "A single violet platform signal against dark ink, with no secondary brand color or broad purple wash."

railway-train-motion-tokens:
  description: "Train metaphor is encoded as controlled scroll-distance tokens rather than playful generic animation."
  technique: "--train-scroll-distance: 210px-640px variants; --train-scroll-distance-mobile: 76px-440px variants; transition easing: cubic-bezier(.455, .03, .515, .955); prefers-reduced-motion branch present"
  applied_to: ["{component.railway-train-illustration}", "{component.Hero Section}"]
  visual_signature: "Motion feels like a measured rail glide through the hero, not bounce or confetti."
```

---

## 14. Content Voice
<!-- SOURCE: manual -->

Railway's copy is short, plain, and unusually calm for developer infrastructure. "Ship software peacefully" pairs a high-stakes action with a low-anxiety adverb. Supporting copy says "all-in-one intelligent cloud provider" without stacking buzzwords into a paragraph.

Use verbs from deployment and operations: ship, deploy, sync, create, monitor, scale. Keep the sentence length low. The interface labels should feel like a real product, not like a concept deck.

---

## 15. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  --railway-night-base: #13111C;
  --railway-night-ink: #08070C;
  --railway-text: #FFFFFF;
  --railway-muted: #FFFFFF80;
  --railway-border: #FFFFFF1A;
  --railway-purple: #6D4BBC;
  --railway-deep-purple: #13044C;
  --railway-radius-control: 8px;
  --railway-radius-frame: 16px;
  --railway-canvas-shadow:
    0 0 0 1px #FFFFFF1F,
    0 2px 8px -2px #00000040,
    0 4px 16px -4px #00000040;
}

body {
  margin: 0;
  background: var(--railway-night-base);
  color: var(--railway-text);
  font-family: var(--font-inter), -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}

.railway-hero {
  max-width: 1280px;
  margin: 0 auto;
  min-height: 720px;
  border: 1px solid var(--railway-border);
  border-radius: var(--railway-radius-frame);
  background:
    linear-gradient(180deg, #13111C66 0%, #13111CCC 100%),
    #13111C;
  overflow: hidden;
  position: relative;
}

.railway-hero h1 {
  font-family: var(--font-ibm-plex-serif), Georgia, Cambria, "Times New Roman", serif;
  font-size: clamp(44px, 5vw, 64px);
  line-height: 1.05;
  letter-spacing: -0.02em;
  font-weight: 700;
}

.railway-button-primary {
  min-height: 58px;
  padding: 0 24px;
  border-radius: 8px;
  border: 0;
  background: var(--railway-purple);
  color: #FFFFFF;
  font-weight: 600;
}

.railway-button-secondary {
  min-height: 58px;
  padding: 0 24px;
  border-radius: 8px;
  border: 1px solid var(--railway-border);
  background: transparent;
  color: #FFFFFF;
}

.railway-console {
  background: var(--railway-night-ink);
  border: 1px solid var(--railway-border);
  border-radius: 8px 8px 0 0;
  box-shadow: var(--railway-canvas-shadow);
}
```

---

## 16. Tailwind
<!-- SOURCE: auto+manual -->

```js
export default {
  theme: {
    extend: {
      colors: {
        railway: {
          night: "#13111C",
          ink: "#08070C",
          purple: "#6D4BBC",
          deep: "#13044C",
          muted: "#FFFFFF80",
          border: "#FFFFFF1A"
        }
      },
      fontFamily: {
        sans: ["var(--font-inter)", "Inter", "system-ui", "sans-serif"],
        serif: ["var(--font-ibm-plex-serif)", "Georgia", "serif"],
        mono: ["JetBrains Mono", "ui-monospace", "SFMono-Regular", "monospace"]
      },
      boxShadow: {
        "railway-canvas": "0 0 0 1px #FFFFFF1F, 0 2px 8px -2px #00000040, 0 4px 16px -4px #00000040"
      },
      borderRadius: {
        railway: "8px",
        "railway-frame": "16px"
      }
    }
  }
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

- Background: #13111C
- App surface: #08070C
- Primary text: #FFFFFF
- Muted text: #FFFFFF80
- Hairline border: #FFFFFF1A
- Primary action: #6D4BBC
- Deep railway accent: #13044C

### Build Prompt

Build a Railway-inspired SaaS homepage section. Use a dark #13111C page, a rounded hero viewport with a night-sky feeling, a centered serif headline, two CTAs, and a cropped deployment-console mockup rising from the bottom. Use #6D4BBC only for the primary Deploy CTA and active console accents. Use Inter for UI text, IBM Plex Serif or Source Serif for the hero headline, and JetBrains Mono for tiny console labels. Keep borders translucent (#FFFFFF1A), shadows nested and dark, and the navigation compact.

### Avoid Prompt

Do not make a generic white SaaS landing page. Do not use neon gradients as the main background. Do not turn every element purple. Do not replace the serif hero with all-Inter type. Do not show the whole dashboard as a centered card; crop it from below inside the hero frame.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO

- Use #13111C as the page base and #08070C for the app-console surface.
- Use #FFFFFF for primary text and #FFFFFF80 for muted labels.
- Use #6D4BBC for the main Deploy CTA and restrained active accents.
- Pair a serif hero headline with Inter product UI text.
- Frame the hero image/mockup with a rounded border and translucent #FFFFFF1A hairline.
- Crop the product console from the bottom of the hero.
- Use nested alpha shadows instead of broad decorative glow.
- Keep nav compact and horizontally calm.

### DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#13111C` 사용.
- 앱 콘솔 표면을 `#FFFFFF`로 만들지 말 것 — 대신 `#08070C` 사용.
- 기본 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#FFFFFF` 사용.
- muted 텍스트를 `#666666`으로 두지 말 것 — 대신 `#FFFFFF80` 사용.
- primary CTA를 `#000000` 또는 `#2563EB`로 두지 말 것 — 대신 `#6D4BBC` 사용.
- hairline border를 `#E5E7EB`로 두지 말 것 — 대신 dark hero에서는 `#FFFFFF1A` 사용.
- hero headline을 Inter 800만으로 처리하지 말 것 — serif display weight 700을 사용.
- 모든 섹션에 purple glow를 깔지 말 것 — #6D4BBC는 action signal이다.

### 🚫 What This Site Doesn't Use

- It does not use a bright white SaaS page shell as the primary identity.
- It does not use a rainbow palette; the chromatic field is mostly one purple plus rare support accents.
- It does not use large glassmorphism cards for the core hero.
- It does not use bubbly pill buttons as the main action shape.
- It does not use oversized icon grids above the fold.
- It does not use heavy drop shadows on navigation.
- It does not use monospace as a brand-wide display voice.
- It does not use pure black #000000 as the page background.
- It does not use cheerful illustration colors in the hero; the scene stays nocturnal.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- The analysis reused existing phase1 artifacts from `insane-design/railway/`; no fresh network fetch was performed in this run.
- The screenshot was a homepage hero crop with a cookie banner visible at the bottom, so below-the-fold section rhythm is inferred mainly from CSS utilities and not full visual inspection.
- CSS frequency includes framework utilities, Mantine defaults, SVG/illustration colors, and product UI tokens; dominant colors were filtered manually to avoid treating resets and logo/illustration noise as brand colors.
- Exact runtime font files were not re-fetched; font names are based on CSS family declarations found in the existing bundle.
- Component behavior such as hover timing, dropdown contents, and mobile menu animation is inferred from CSS tokens and visible hero structure, not from live interaction.
- Railway may have changed production design after the captured April 2026 phase1 artifacts; this guidebook reflects the local captured snapshot.
