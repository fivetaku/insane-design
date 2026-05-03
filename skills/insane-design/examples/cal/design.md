---
schema_version: 3.2
slug: cal
service_name: Cal.com
site_url: https://cal.com
fetched_at: 2026-05-03T06:19:20Z
default_theme: light
brand_color: "#242424"
primary_font: "Cal Sans UI Variable Light"
font_weight_normal: 300
token_prefix: "--token"

bold_direction: "Scheduling Slate"
aesthetic_category: "industrial minimalism"
signature_element: "dark booking-card chassis on a soft gray scheduling floor"
code_complexity: medium

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Framer-exported production page with real CSS tokens, repeated scheduling components, and Cal-owned font assets, but UUID token names instead of a public semantic token API."

colors:
  surface-dark: "#242424"
  surface-page: "#F4F4F4"
  text-primary: "#000000"
  text-on-dark: "#FFFFFF"
  text-muted: "#898989"
  border-light: "#E1E2E3"
  accent-blue: "#0099FF"
  accent-violet: "#6349EA"
  success: "#19A874"
  error: "#EF4444"

typography:
  display: "Cal Sans UI Variable Light"
  body: "Inter"
  supporting_display: "Inter Display"
  code: "Roboto Mono"
  ladder:
    - { token: hero, size: "64px", weight: 300, line_height: "1.1em", tracking: "0em" }
    - { token: h1, size: "56px", weight: 300, line_height: "1.1em", tracking: "0em" }
    - { token: h2, size: "40px", weight: 400, line_height: "1.1em", tracking: "0em" }
    - { token: h3, size: "32px", weight: 400, line_height: "1.3em", tracking: "0em" }
    - { token: body, size: "16px", weight: 400, line_height: "1.5em", tracking: "0em" }
    - { token: caption, size: "14px", weight: 400, line_height: "1.5em", tracking: "-.2px" }
  weights_used: [100, 200, 300, 400, 500, 600, 700, 800, 900]
  weights_absent: []

components:
  button-dark-primary: { bg: "{colors.surface-dark}", fg: "{colors.text-on-dark}", radius: "9999px", padding: "8px 12px" }
  button-light-secondary: { bg: "{colors.text-on-dark}", fg: "{colors.surface-dark}", radius: "9999px", padding: "8px 12px" }
  booking-card: { bg: "{colors.text-on-dark}", border: "1px solid {colors.border-light}", radius: "16px", shadow: "0 1px 5px -4px #242424b3, 0 4px 8px #2424240d" }
  dark-feature-panel: { bg: "{colors.surface-dark}", fg: "{colors.text-on-dark}", radius: "16px" }
---

# DESIGN.md - Cal.com

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Cal.com reads like a terminal receipt system rendered in consumer-grade scheduling geometry. The page floor is pale utility gray #F4F4F4 (`{colors.surface-page}`), but the identity anchor is the dark scheduling chassis: compact #242424 (`{colors.surface-dark}`) surfaces carry the brand the way a console carries its instrument cluster. The canvas is not a glossy SaaS backdrop; it is a dispatch-desk surface where only the clock, the route, and the confirmation slot survive.

The signature move is deploying dark neutral panels as identity rather than a saturated brand color. #0099FF (`{colors.accent-blue}`) and #6349EA (`{colors.accent-violet}`) behave like small LED state indicators on terminal equipment — not paint on the room. The dark booking previews, nav chrome, and pill buttons compose a repeated object language: rounded but not playful, dense but not enterprise-heavy. Each dark panel is less a hero moment and more a scheduling console chassis pulled onto the parchment-gray page for demonstration.

Typography holds the same register. Cal Sans UI Variable Light is the brand voice; Inter and Inter Display handle the bulk of interface reading. Hero-size type is large and airy but keeps the directness of a command prompt: instructions arrive as short declaratives, not as marketing manifestos. The product promise is infrastructure, and the parchment of the page communicates that promise by refusing ornament.

Shadow is the shallow contact shadow of a device sitting on a desk — `0 1px 5px -4px #242424b3, 0 4px 8px #2424240d` — not a stage effect. Color is scarce because the canvas does the credential work: controlled neutrals, pill CTAs, 16px rounded panels, and simulated calendar UI make the page recognizable as infrastructure before the headline is read.

To complete the picture: the 16px panels behave like appointment slips filed in a steel rack, the pill CTAs read as the green and grey buttons of a desk-mounted intercom, and the dark `#242424` blocks look like the matte housing of a server appliance bolted under the desk. Even the typography acts like terminal numerals on a flight-information board — calm, monospaced in feel, never ornamental. The page performs less like a brochure and more like a terminal instrument panel that already has the next meeting loaded.

### Key Characteristics

- Dark neutral brand chassis: #242424 is the identity anchor, not a vivid chromatic brand swatch.
- Soft gray page floor: #F4F4F4 prevents the marketing page from becoming sterile white.
- Product-first mock UI: booking cards, availability panels, meeting details, reminders, and integrations are used as visual proof.
- Pill actions: CTAs tend toward compact capsule geometry with 9999px radius.
- Rounded panel system: 16px is the dominant card radius for feature and booking surfaces.
- Shallow elevation: one dual shadow appears as a light touch, never as dramatic floating chrome.
- Type pairing: Cal Sans for brand/display moments, Inter and Inter Display for scalable marketing/interface text.
- Dense utility rhythm: content panels and examples are closer to app UI than broad editorial storytelling.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Scheduling Slate
> **Aesthetic Category**: industrial minimalism
> **Signature Element**: 이 사이트는 **dark booking-card chassis on a soft gray scheduling floor**으로 기억된다.
> **Code Complexity**: medium — Framer export with many UUID tokens and repeated component states, but the visual system is built from a small neutral/radius/shadow grammar.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Cal.com처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter", "Inter Display", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
}
.brand-display {
  font-family: "Cal Sans UI Variable Light", "Cal Sans", "Inter Display", sans-serif;
  font-weight: 300;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #F4F4F4; --fg: #000000; --panel: #FFFFFF; --slate: #242424; }
body { background: var(--bg); color: var(--fg); }

/* 3. Cal surface grammar */
.cal-panel {
  border-radius: 16px;
  border: 1px solid #E1E2E3;
  box-shadow: 0 1px 5px -4px #242424b3, 0 4px 8px #2424240d;
}
```

**절대 하지 말아야 할 것 하나**: Cal을 파란 SaaS로 만들지 말 것. #0099FF는 보조 accent이고, 실제 기억점은 #242424 dark scheduling chassis다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://cal.com` |
| Fetched | 2026-05-03T06:19:20Z |
| Extractor | reused existing phase1 artifacts from `insane-design/cal/` |
| HTML size | 2,297,795 bytes (Framer-exported marketing page) |
| CSS files | 1 inline CSS capture, 441,907 chars |
| Token prefix | `--token` plus `--framer-*` runtime variables |
| Method | CSS custom property parsing, frequency candidates, typography extraction, manual interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Framer export / hosted marketing page.
- **Design system**: Cal-owned visual layer expressed through Framer UUID tokens and Cal Sans font assets.
- **CSS architecture**:
  ```text
  --token-*        UUID-like raw color tokens, mostly core values
  --framer-*      runtime typography/link/layout variables
  selectors       Framer component hashes and rich-text presets
  ```
- **Class naming**: Framer-generated classes, not human semantic BEM.
- **Default theme**: light marketing page with #F4F4F4 page background and #242424 dark product panels.
- **Font loading**: Framer-declared families including Cal Sans UI Variable Light, Cal Sans, Inter, Inter Display, Roboto Mono, and several placeholder/fallback names.
- **Canonical anchor**: the homepage scheduling/product story: "The better way to schedule your meetings", booking cards, team-size navigation, and feature modules.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Cal Sans UI Variable Light` for brand/display moments.
- **Body font**: `Inter` dominates declarations, followed closely by `Inter Display`.
- **Code font**: `Roboto Mono` appears in extracted font-family data.
- **Weight normal / bold**: body commonly 400; Cal display/light moments use 300; heavier weights exist across Framer presets and should be used only where the page already implies UI hierarchy.

```css
:root {
  --cal-font-display: "Cal Sans UI Variable Light", "Cal Sans", "Inter Display", sans-serif;
  --cal-font-body: "Inter", "Inter Display", -apple-system, BlinkMacSystemFont, sans-serif;
  --cal-font-code: "Roboto Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --cal-font-weight-light: 300;
  --cal-font-weight-normal: 400;
  --cal-font-weight-semibold: 600;
}
body {
  font-family: var(--cal-font-body);
  font-weight: var(--cal-font-weight-normal);
}
```

### Note on Font Substitutes

- **Cal Sans UI Variable Light** — if the Cal-owned font is unavailable, use open-source **Inter Display** at weight 300, `line-height: 1.1em`, and keep `letter-spacing: 0em`. Do not compensate with negative tracking; extracted Cal text is notably uncompressed.
- **Inter body** — keep Inter as the body fallback. A generic `system-ui` replacement loses the Cal/Framer product texture because the page depends on Inter's neutral interface tone.
- **Roboto Mono** — use only for code/API/developer surfaces. Do not let mono styling leak into scheduling cards unless the content is explicitly technical.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| hero-display | 64px | 300 | 1.1em | 0em |
| page-h1 | 56px | 300 | 1.1em | 0em |
| section-h2 | 40px | 400/600 | 1.1em | 0em |
| module-title | 32px | 400/600 | 1.3em | 0em |
| body | 16px | 400 | 1.5em | 0em |
| nav / label | 14px | 400/500 | 1.5em | -0.2px where present |
| micro | 12px | 500/600 | 1.2em | 0em |

> ⚠️ Cal's typographic identity is not "huge SaaS gradient type"; it is light, balanced display type plus sober Inter interface copy.

### Principles

1. Display lightness matters — hero and brand moments should start from weight 300, not 700.
2. Body copy stays interface-neutral — 16px / 1.5em is the core reading texture.
3. Tracking is mostly zero — do not add fashionable negative letter-spacing to every headline.
4. 14px labels are real interface material — booking previews and settings-like modules rely on small text being legible.
5. Heavy weights exist in the export, but use them as hierarchy accents, not as the default brand voice.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (neutral-led)

| Token | Hex |
|---|---|
| `--token-fe0d69fb-0445-4f97-b1b4-d5035d890a7a` | `#242424` |
| `--token-04285ea8-7979-4c0d-9108-9b979d0dc201` | `#292929` |
| extracted neutral | `#141414` |
| extracted neutral | `#111111` |
| text/link default fallback | `#000000` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--token-ff1e49ba-8f64-4300-83d8-8ab67dfa21d0` | `#0D0C27` |
| `--token-7329240e-3f60-4c53-bf0a-cd65019272a8` | `#15142E` |
| `--token-e8e4663b-49e0-475e-922f-dfe89bd13fdc` | `#352F4B` |

### 06-3. Neutral Ramp

| Step | Light | Dark / Text |
|---|---|---|
| page | `#F4F4F4` | `#242424` |
| panel | `#FFFFFF` | `#141414` |
| raised / subtle | `#FCFCFC` | `#292929` |
| border | `#E1E2E3` | `#242424B3` |
| muted | `#898989` | `#FFFFFFB3` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Blue | action / illustration accent | `#0099FF` |
| Violet | AI / feature accent | `#6349EA` |
| Violet-light | supporting accent | `#875FE0`, `#C292FF` |
| Green | success / calendar-positive | `#19A874`, `#E4F7F3` |
| Red | error / destructive | `#EF4444`, `#FEE2E2` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `{colors.surface-page}` | `#F4F4F4` | body background / page floor |
| `{colors.surface-dark}` | `#242424` | brand chassis, dark feature panels, dark CTAs |
| `{colors.text-primary}` | `#000000` | high-contrast text and default rich-text fallbacks |
| `{colors.text-muted}` | `#898989` | secondary descriptions and low-priority metadata |
| `{colors.border-light}` | `#E1E2E3` | card borders, panel separators |
| `{colors.accent-blue}` | `#0099FF` | limited accent, not brand wash |
| `{colors.success}` | `#19A874` | positive states |
| `{colors.error}` | `#EF4444` | error/destructive states |

### 06-6. Semantic Alias Layer

> N/A — extracted Framer artifacts expose UUID-like core tokens and `--framer-*` runtime variables, but no stable human semantic alias layer such as `--cal-color-primary`.

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| fallback black | `#000000` | 77 |
| dark surface | `#242424` | 57 |
| near-black | `#141414` | 32 |
| white | `#FFFFFF` | 29 |
| muted gray | `#898989` | 26 |
| border gray | `#E1E2E3` | 18 |
| accent blue | `#0099FF` | 12 |
| dark alpha | `#242424B3` | 10 |
| shadow alpha | `#2424240D` | 10 |
| violet | `#6349EA` | 8 |

### 06-8. Color Stories

**`{colors.surface-dark}` (`#242424`)** — Cal's real brand color. It appears as the dark scheduling chassis: panels, CTAs, booking UI, and product-like blocks. Use it when the interface needs to feel like the scheduling engine itself.

**`{colors.surface-page}` (`#F4F4F4`)** — the quiet floor. It keeps the page from looking like plain SaaS white and gives white booking cards a reason to exist.

**`{colors.text-primary}` (`#000000`)** — the direct voice. Cal does not soften primary copy into blue-gray; the typography is plain and high contrast.

**`{colors.border-light}` (`#E1E2E3`)** — structural hairline. This border does more work than decorative color, separating booking modules without making them visually heavy.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `gap-2xs` | 2px | dense icon/text internals |
| `gap-xs` | 4px | tiny stacked UI labels |
| `gap-sm` | 8px | inline controls, button internals |
| `gap-md` | 10px / 12px | repeated Framer stack rhythm |
| `gap-lg` | 16px | card internal grouping |
| `gap-xl` | 24px | module separation |
| `gap-2xl` | 32px | section subgroups |
| `gap-3xl` | 48px | major vertical groups |
| `section-top` | 96px | hero/section breathing room observed in CSS |

**주요 alias**:
- `--cal-space-card` -> 24px (feature and card padding)
- `--cal-space-inline` -> 8px / 12px (button and compact row rhythm)
- `--cal-space-section` -> 48px / 96px (marketing section rhythm)

### Whitespace Philosophy

Cal's whitespace is operational rather than luxurious. The site leaves enough room for the hero and major section headings to read, then compresses inside product cards so the viewer feels scheduling density: times, reminders, participants, availability, and app integrations.

The most important spacing contrast is "open page, dense object." The #F4F4F4 page floor gives sections air, while white and dark rounded modules pull content into compact, app-like surfaces.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `--cal-radius-xs` | 2px | tiny UI fragments and progress/slot marks |
| `--cal-radius-sm` | 8px | compact badges and small containers |
| `--cal-radius-md` | 12px | medium controls |
| `--cal-radius-card` | 16px | dominant card/panel radius |
| `--cal-radius-pill` | 9999px | CTA buttons and capsule controls |

Cal rounds panels enough to feel modern, but never into bubbly consumer softness. The 16px card radius is the default; pills are reserved for actions.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: 1200px / 1224px / 1280px appear as primary outer widths.
- **Grid type**: centered marketing container with Framer stack/grid internals.
- **Column count**: mixed; product cards and feature modules use repeated responsive groupings rather than a visible editorial grid.
- **Gutter**: 16px to 32px for card groups; 48px for major bands.

### Hero
- **Pattern Summary**: soft gray page floor + large centered scheduling proposition + dark/white booking preview object + dual signup CTA.
- Layout: marketing headline with product proof modules, not a split illustration-only composition.
- Background: solid #F4F4F4 with dark/white UI objects.
- **Background Treatment**: solid surface with object contrast; no full-bleed image, no gradient mesh.
- H1: `56px-64px` / weight `300` / tracking `0em`.
- Max-width: 1200px family.

### Section Rhythm

```css
section {
  padding: 96px 12px 0;
  max-width: 1200px;
}
.cal-module {
  gap: 16px;
  padding: 24px;
}
```

### Card Patterns
- **Card background**: #FFFFFF on #F4F4F4, or #242424 for dark product panels.
- **Card border**: 1px solid #E1E2E3.
- **Card radius**: 16px.
- **Card padding**: 20px / 24px.
- **Card shadow**: `0 1px 5px -4px #242424b3, 0 4px 8px #2424240d`.

### Navigation Structure
- **Type**: product marketing nav with grouped dropdown/product taxonomy.
- **Position**: top navigation.
- **Height**: compact app-like bar; infer 48px-64px zone from spacing rhythm.
- **Background**: light/transparent over #F4F4F4 or white panel zones.
- **Border**: light gray separators when framed.

### Content Width
- **Prose max-width**: 640px for readable copy.
- **Container max-width**: 1200px / 1280px.
- **Sidebar width**: N/A on homepage; dropdown/product menus are transient.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary dark pill**

| Property | Value |
|---|---|
| Background | `#242424` |
| Text | `#FFFFFF` |
| Radius | `9999px` |
| Padding | `8px 12px` or `12px 16px` depending context |
| Font | Inter / Cal Sans UI, 14px-16px |

```html
<button class="cal-button cal-button-dark">Sign up with email</button>
```

**Secondary light pill**

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#242424` |
| Border | `1px solid #E1E2E3` |
| Radius | `9999px` |

### Badges

Small labels should stay neutral: #FFFFFF or #F4F4F4 surface, #242424 text, 8px to 9999px radius depending whether it is a tag or CTA-adjacent capsule. Do not invent colorful badge systems unless the product state requires success/error.

### Cards & Containers

**Booking card**

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Border | `1px solid #E1E2E3` |
| Radius | `16px` |
| Padding | `20px` / `24px` |
| Shadow | `0 1px 5px -4px #242424b3, 0 4px 8px #2424240d` |

**Dark feature panel**

| Property | Value |
|---|---|
| Background | `#242424` |
| Text | `#FFFFFF`, secondary `#FFFFFFB3` |
| Radius | `16px` |
| Border | none or transparent |

### Navigation

Navigation is compact and product-taxonomy heavy: "By team size", "For Individuals", "For Organizations", "Developer Documentation", "API", and app integrations. Use neutral link text, subtle separators, and avoid oversized marketing nav typography.

### Inputs & Forms

Forms should inherit the scheduling-card grammar: white or near-white inputs, #E1E2E3 border, 12px-16px radius, 14px-16px Inter text, and focus states that are visible but not neon. Error states may use #EF4444 and #FEE2E2.

### Hero Section

The hero is a scheduling proof surface. Combine a light page floor, a large Cal Sans/Inter Display headline, compact CTAs, and at least one realistic booking card. The booking object must look operational: participant name, meeting type, timezone, time slot, or app integration.

### 13-2. Named Variants

**button-dark-primary** — #242424 pill, white text, primary signup/action. This is the most Cal-like CTA.

**button-oauth-light** — white panel button for "Sign up with Google"; use border #E1E2E3 and restrained icon spacing.

**booking-card-white** — white surface on #F4F4F4, 16px radius, thin border, shallow dual shadow.

**dark-scheduling-panel** — #242424 surface used for high-signal product demos, with white and #FFFFFFB3 text.

**integration-tile** — compact app tile; use neutral surfaces and only let app logos carry color.

### 13-3. Signature Micro-Specs

```yaml
dark-scheduling-chassis:
  description: "Cal's recurring dark product object turns booking UI into a compact instrument panel."
  technique: "background #242424 /* {colors.surface-dark} */; color #FFFFFF /* {colors.text-on-dark} */; secondary text #FFFFFFB3; border-radius 16px"
  applied_to: ["{component.dark-feature-panel}", "{component.dark-scheduling-panel}", "{component.button-dark-primary}"]
  visual_signature: "The scheduling surface reads like a black hardware chassis around availability, routes, and booking state."

soft-gray-scheduling-floor:
  description: "A pale utility floor keeps the page operational instead of gallery-white or SaaS-blue."
  technique: "body background #F4F4F4 /* {colors.surface-page} */; panels #FFFFFF or #242424; borders 1px solid #E1E2E3"
  applied_to: ["{component.booking-card}", "{component.booking-card-white}", "{component.integration-tile}"]
  visual_signature: "White and dark UI objects sit on the page like appointment slips and scheduling devices on a workbench."

shallow-contact-card-shadow:
  description: "Elevation is a restrained contact mark, not a floating-card spectacle."
  technique: "box-shadow 0 1px 5px -4px #242424b3, 0 4px 8px #2424240d; border 1px solid #E1E2E3; border-radius 16px"
  applied_to: ["{component.booking-card}", "{component.booking-card-white}"]
  visual_signature: "Cards feel physically placed on the gray floor while staying flat enough to read as product UI."

compact-pill-action-system:
  description: "Actions are small capsule controls that behave like app chrome rather than marketing banners."
  technique: "border-radius 9999px; padding 8px 12px or 12px 16px; dark variant #242424 on #FFFFFF text; light variant #FFFFFF with #E1E2E3 border"
  applied_to: ["{component.button-dark-primary}", "{component.button-light-secondary}", "{component.button-oauth-light}"]
  visual_signature: "CTAs look like precise scheduling controls, with no oversized gradient buttons or chromatic brand flood."

cal-light-display-command:
  description: "Large display type keeps the dry confidence of a scheduling command, not a hype headline."
  technique: "font-family Cal Sans UI Variable Light or Inter Display; font-size 56px-64px; font-weight 300; line-height 1.1em; letter-spacing 0em"
  applied_to: ["{component.hero-section}", "{component.section-display-copy}"]
  visual_signature: "Headlines feel open and directive, like a clear prompt above an already-working booking object."
```

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Cal.com — copy into your root stylesheet */
:root {
  /* Fonts */
  --cal-font-display: "Cal Sans UI Variable Light", "Cal Sans", "Inter Display", sans-serif;
  --cal-font-body: "Inter", "Inter Display", -apple-system, BlinkMacSystemFont, sans-serif;
  --cal-font-code: "Roboto Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --cal-font-weight-light: 300;
  --cal-font-weight-normal: 400;
  --cal-font-weight-semibold: 600;

  /* Core colors */
  --cal-surface-page: #F4F4F4;
  --cal-surface-panel: #FFFFFF;
  --cal-surface-dark: #242424;
  --cal-text-primary: #000000;
  --cal-text-muted: #898989;
  --cal-text-on-dark: #FFFFFF;
  --cal-text-on-dark-muted: #FFFFFFB3;
  --cal-border-light: #E1E2E3;

  /* Accents */
  --cal-accent-blue: #0099FF;
  --cal-accent-violet: #6349EA;
  --cal-success: #19A874;
  --cal-success-bg: #E4F7F3;
  --cal-error: #EF4444;
  --cal-error-bg: #FEE2E2;

  /* Spacing */
  --cal-space-xs: 4px;
  --cal-space-sm: 8px;
  --cal-space-md: 12px;
  --cal-space-lg: 16px;
  --cal-space-xl: 24px;
  --cal-space-2xl: 32px;
  --cal-space-section: 96px;

  /* Shape + elevation */
  --cal-radius-sm: 8px;
  --cal-radius-md: 12px;
  --cal-radius-card: 16px;
  --cal-radius-pill: 9999px;
  --cal-shadow-card: 0 1px 5px -4px #242424b3, 0 4px 8px #2424240d;
}

body {
  margin: 0;
  background: var(--cal-surface-page);
  color: var(--cal-text-primary);
  font-family: var(--cal-font-body);
  font-weight: var(--cal-font-weight-normal);
}

.cal-display {
  font-family: var(--cal-font-display);
  font-weight: var(--cal-font-weight-light);
  line-height: 1.1em;
  letter-spacing: 0;
}

.cal-card {
  background: var(--cal-surface-panel);
  border: 1px solid var(--cal-border-light);
  border-radius: var(--cal-radius-card);
  box-shadow: var(--cal-shadow-card);
  padding: var(--cal-space-xl);
}

.cal-button-primary {
  background: var(--cal-surface-dark);
  color: var(--cal-text-on-dark);
  border: 0;
  border-radius: var(--cal-radius-pill);
  padding: 8px 12px;
  font: 500 14px/1.5 var(--cal-font-body);
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `{colors.surface-dark}` | `#242424` |
| Background | `{colors.surface-page}` | `#F4F4F4` |
| Panel | `{colors.text-on-dark}` / white panel | `#FFFFFF` |
| Text primary | `{colors.text-primary}` | `#000000` |
| Text muted | `{colors.text-muted}` | `#898989` |
| Border | `{colors.border-light}` | `#E1E2E3` |
| Accent | `{colors.accent-blue}` | `#0099FF` |

### Example Component Prompts

#### Hero Section

```text
Cal.com 스타일 히어로 섹션을 만들어줘.
- 배경: #F4F4F4
- H1: Cal Sans UI Variable Light 또는 Inter Display, 56px-64px, weight 300, line-height 1.1em, tracking 0
- 서브텍스트: #242424 또는 #898989, 16px, line-height 1.5
- CTA: #242424 배경, #FFFFFF 텍스트, 9999px radius, padding 8px 12px
- 제품 증거: 실제 예약 카드처럼 이름, 미팅 타입, 시간대, 시간 슬롯을 포함한 white card
- 카드: #FFFFFF, border #E1E2E3, radius 16px, shallow dual shadow
```

#### Card Component

```text
Cal.com 스타일 booking card를 만들어줘.
- 배경: #FFFFFF on page #F4F4F4
- border: 1px solid #E1E2E3
- radius: 16px
- padding: 24px
- shadow: 0 1px 5px -4px #242424b3, 0 4px 8px #2424240d
- 제목: Inter, 16px, weight 500/600
- 메타: 14px, #898989
- 상태 색은 최소화하고, 성공은 #19A874, 오류는 #EF4444만 사용
```

#### Navigation

```text
Cal.com 스타일 네비게이션을 만들어줘.
- compact SaaS product nav
- 배경은 #F4F4F4 또는 #FFFFFF
- 링크는 Inter 14px, #242424 / #898989
- dropdown은 white card, #E1E2E3 border, 16px radius
- CTA는 #242424 pill로 처리
```

### Iteration Guide

- **색상 변경 시**: blue를 primary brand로 승격하지 말 것. Cal의 primary는 dark neutral이다.
- **폰트 변경 시**: display는 light weight를 유지한다. 굵은 700 headline은 Cal 느낌을 빠르게 잃는다.
- **여백 조정 시**: section은 넓게, card 내부는 촘촘하게 유지한다.
- **새 컴포넌트 추가 시**: 16px card radius, #E1E2E3 hairline, shallow shadow grammar를 먼저 적용한다.
- **다크 표면**: #242424 위에서는 white와 #FFFFFFB3 계층만으로 충분하다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #242424 as the brand chassis for primary action and high-signal product panels.
- Put white booking cards on #F4F4F4, not on a sterile blank white page.
- Keep panels rounded at 16px and actions as pills.
- Use Cal Sans UI / Cal Sans for brand display, with Inter for interface copy.
- Let product UI carry the visual story: booking slots, calendar overlays, reminders, integrations.
- Use #0099FF, #6349EA, #19A874, and #EF4444 only as state/accent colors.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로만 두지 말 것 — 대신 page floor는 `#F4F4F4` 사용.
- primary brand color를 `#0099FF`로 두지 말 것 — 대신 primary chassis는 `#242424` 사용.
- 텍스트를 전부 `#898989` 같은 muted gray로 두지 말 것 — primary copy는 `#000000` 사용.
- card border를 `#CCCCCC` 또는 generic gray로 두지 말 것 — 대신 `#E1E2E3` 사용.
- dark panel 위 secondary text를 `#898989`로 두지 말 것 — 대신 `#FFFFFFB3` 사용.
- error state에 임의 red `#FF0000` 사용 금지 — Cal 계열 error는 `#EF4444` / `#FEE2E2`.
- hero headline에 `font-weight: 700`을 기본값으로 쓰지 말 것 — Cal display는 `font-weight: 300`에서 시작.
- 모든 카드에 큰 shadow를 넣지 말 것 — 검출된 shadow는 `0 1px 5px -4px #242424b3, 0 4px 8px #2424240d`.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Brand gradient: absent. Cal does not need a gradient hero to be recognizable.
- Second primary brand color: none. #0099FF and #6349EA are accents, not co-primary colors.
- Decorative illustration language: minimal. Product UI screenshots and scheduling objects do the work.
- Heavy editorial typography: absent. No magazine-like serif display, no oversized expressive contrast.
- Deep elevation system: absent. Shadow is shallow and scoped, not a multi-level material stack.
- Neon focus aesthetic: absent. Accents are useful state signals, not atmospheric glow.
- Pure white page identity: avoided. #F4F4F4 is the page base that keeps the surface system visible.
- Over-rounded consumer cards: avoided. Cards sit at 16px; only buttons become full pills.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-only evidence** — this guidebook reuses existing `insane-design/cal` homepage phase1 artifacts. Authenticated app surfaces, settings, booking checkout, and team admin flows were not visited.
- **Framer token opacity** — the export exposes UUID-like `--token-*` variables rather than semantic Cal token names. Human-readable names in frontmatter are interpretive aliases mapped to real hex values, not confirmed source token names.
- **Responsive behavior not visually remeasured** — desktop CSS breakpoints and max-widths were observed, but this run did not recapture mobile/tablet screenshots.
- **Motion is under-specified** — CSS contained Framer runtime variables, but scroll-triggered animation timing and JS interaction behavior were not analyzed.
- **Logo/app color contamination possible** — extracted chromatic candidates include app/integration/logo colors. This guide treats #0099FF, #6349EA, #19A874, and #EF4444 as accents/states, not broad palette requirements.
- **Exact component state coverage incomplete** — hover, focus, disabled, loading, and validation states were inferred from available CSS/state colors, not exhaustively exercised in the browser.
- **Font licensing and availability** — Cal Sans UI assets appear in the page, but external implementers may need Cal Sans or Inter Display substitutes depending on licensing and deployment context.
- **Current-site drift** — phase1 artifacts are reused from the existing local capture. If Cal.com has changed after that capture, this file reflects the local evidence, not a fresh network crawl.
