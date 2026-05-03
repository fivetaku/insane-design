---
schema_version: 3.2
slug: vercel
service_name: Vercel
site_url: https://vercel.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: light
brand_color: "#000000"
primary_font: Geist
font_weight_normal: 400
token_prefix: ds

bold_direction: Monochrome Precision
aesthetic_category: minimal_extreme
signature_element: minimal_extreme
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "635 CSS variables, Geist typography, ds/geist token families, and repeatable Geist UI components are present in production CSS."

colors:
  brand: "#000000"
  surface: "#FFFFFF"
  text-primary: "#000000"
  text-muted: "#666666"
  border: "#EAEAEA"
  surface-subtle: "#FAFAFA"
  ink-soft: "#333333"
  ai-blue: "#2C8CE1"
  ai-mint: "#45DEC4"
typography:
  display: "Geist"
  body: "Geist"
  mono: "Geist Mono"
  ladder:
    - { token: hero, size: "48px", weight: 600, line_height: "56px", tracking: "-0.04em" }
    - { token: h2, size: "40px", weight: 600, line_height: "48px", tracking: "-0.03em" }
    - { token: h3, size: "24px", weight: 600, line_height: "32px", tracking: "-0.02em" }
    - { token: body, size: "16px", weight: 400, line_height: "24px", tracking: "0" }
    - { token: small, size: "14px", weight: 400, line_height: "20px", tracking: "0" }
  weights_used: [100, 200, 300, 400, 500, 600, 700, 800, 900]
  weights_absent: []
components:
  button-primary: { bg: "{colors.brand}", fg: "{colors.surface}", radius: "9999px", padding: "0 18px", height: "48px" }
  button-secondary: { bg: "{colors.surface}", fg: "{colors.text-primary}", radius: "9999px", padding: "0 22px", height: "48px", border: "1px solid #EAEAEA" }
  nav-button: { bg: "{colors.surface}", fg: "{colors.text-primary}", radius: "6px", height: "40px", border: "1px solid #EAEAEA" }
  card-system: { bg: "{colors.surface}", fg: "{colors.text-primary}", radius: "12px", border: "1px solid #EAEAEA" }
---

# DESIGN.md — Vercel

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Vercel is not a colorful SaaS page. It is a black-and-white operating surface that allows color to appear only when it behaves like physics: spectral light, deployment energy, or product instrumentation. The page starts as a white canvas, then lets a precise grid and the Vercel triangle create authority before the prism field introduces motion and AI-era warmth.

The main identity is subtraction. Navigation is quiet, buttons are pill-shaped but not playful, copy is short, and most surfaces are built from `#FFFFFF` (`{colors.surface}`), `#000000` (`{colors.text-primary}`), `#666666` (`{colors.text-muted}`), and hairline `#EAEAEA` (`{colors.border}`). The brand color is not blue, purple, or the spectrum in the hero. The brand color is black.

The signature image is architectural: a grid plane, a centered headline, a pair of CTAs, and a triangular prism emitting thin chromatic lines. This is how Vercel reconciles developer infrastructure with AI Cloud positioning. It avoids cute AI gradients; instead, it shows color as a measured optical event.

Typography carries the same discipline. Geist is compact, neutral, and technical, with display text tightened by negative tracking. The hero headline reads heavy because the letterforms are close, not because the weight is extreme. Body copy remains moderate and gray, allowing the black CTA and prism to own the hierarchy.

To extend the picture: the page behaves like a clean physics-lab demonstration table where the prism is the only optical instrument and the rest of the bench is white laminate. The grid plane under the hero is the millimetre paper taped to that bench. Customer logos sit in their cells like glass slides arranged on a microscope tray. The pill CTA is a stainless-steel toggle, not a candy button. The deploy graph and product UI fragments behave like ammeter readings glued to the wall — measurement, not decoration. The triangle wordmark is the engraved certification stamp on the side of the equipment. There is no second brand color because the lab is lit by neutral overhead lights and the prism handles all the spectrum work.

비유를 한 단계 더 압축하면, vercel.com은 **AI Cloud 시연이 진행 중인 흰 작업판 위의 엔지니어링다이어그램**이다. 흰 hero canvas는 lab bench 라미네이트, hairline grid는 그 위에 부착된 blueprint 모눈종이, 검정 pill CTA는 작업판에 박힌 한 개의 toggle 스위치, 흰 secondary CTA는 그 옆 라벨된 보조 스위치다. prism은 실험실의 단일 광학 기기이고 chromatic line은 측정 결과의 spectrum 출력 — 도면 위 색인이 아니라 실험 readout이다. 공구함 nav button은 6px 라벨된 서랍, hero pill button은 시연 시작용 정밀 toggle, 두 control이 같은 검정이지만 서로 다른 도구로 정렬된다.

### Key Characteristics

- Black is the brand action color; chroma is reserved for the prism, data, and product accents.
- Geist is the dominant sans family; Geist Mono handles code and developer surfaces.
- Hero composition is centered, gridded, and symmetrical, with large optical air around the headline.
- Hairlines matter more than shadows; borders define structure without visible heaviness.
- Buttons use pill radii for primary hero actions and tighter 6px radius for nav utility buttons.
- The page is light by default but carries a dark token system for product and modal surfaces.
- Color appears as thin optical bands rather than broad decorative gradients.
- Layout density increases below the hero, but the first viewport stays ceremonial and sparse.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Monochrome Precision
> **Aesthetic Category**: minimal_extreme
> **Signature Element**: 이 사이트는 **grid-bound monochrome hero with a spectral Vercel prism**으로 기억된다.
> **Code Complexity**: high — tokenized Geist UI, Tailwind utilities, dark/light variables, layered shadows, and custom optical hero artwork combine into a detailed production system.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Vercel처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Geist", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
  letter-spacing: 0;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #FFFFFF;
  --fg: #000000;
  --muted: #666666;
  --border: #EAEAEA;
}
body {
  background: var(--bg);
  color: var(--fg);
}

/* 3. 버튼 + hairline */
.primary {
  background: #000000;
  color: #FFFFFF;
  border-radius: 9999px;
  height: 48px;
  padding: 0 18px;
}
```

**절대 하지 말아야 할 것 하나**: Vercel을 파란 SaaS 브랜드처럼 만들지 말 것. `#0070F3`는 legacy/product accent로 보이고, homepage identity는 `#000000` + `#FFFFFF` + hairline grid다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://vercel.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | reused phase1 artifacts |
| HTML size | 910,996 bytes |
| CSS files | 12 external CSS files, 866,702 chars combined |
| Token prefix | `--ds-*`, `--geist-*`, `--accents-*`, `--font-*` |
| Method | Existing phase1 JSON + CSS token summaries + hero screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js / React production page with generated CSS module class names and Tailwind utility output.
- **Design system**: Geist UI + Vercel DS token layer — prefixes `--ds-*`, `--geist-*`, `--accents-*`.
- **CSS architecture**:
  ```css
  --geist-*       foundational brand/system tokens
  --ds-*          design-system color, shadow, motion, page-width tokens
  --accents-*     neutral accent ladder
  --tw-*          Tailwind runtime utility variables
  component CSS   hashed module selectors for buttons, nav, menus, modal surfaces
  ```
- **Class naming**: CSS Modules hashes such as `.button-module__QyrFCa__invert` plus Tailwind generated utilities.
- **Default theme**: light homepage surface, with dark-theme counterparts present in token and component rules.
- **Font loading**: `--font-sans: "Geist"` and `--font-mono: "Geist Mono"` with explicit fallback stacks.
- **Canonical anchor**: Vercel triangle mark + black CTA + spectral prism field.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Geist` (Vercel-owned open-source family)
- **Body font**: `Geist`
- **Code font**: `Geist Mono`
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --font-sans: "Geist", Arial, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol;
  --font-sans-fallback: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI",
    "Roboto", "Helvetica Neue", sans-serif;
  --font-mono: "Geist Mono", ui-monospace, SFMono-Regular, Roboto Mono, Menlo,
    Monaco, Liberation Mono, DejaVu Sans Mono, Courier New, monospace;
}

body {
  font-family: var(--font-sans), var(--font-sans-fallback);
  font-weight: 400;
}
```

### Note on Font Substitutes

- **Geist unavailable** — Use **Inter** as the closest open substitute, but tighten display tracking by one step: hero `letter-spacing: -0.04em`, h2 `-0.03em`, h3 `-0.02em`.
- **Geist Mono unavailable** — Use **Roboto Mono** or **SFMono-Regular**. Keep code at 13-14px and avoid decorative mono fonts.
- **Arial fallback present** — CSS explicitly includes Arial in `--font-sans`; do not use Arial as the design choice unless Geist fails to load.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| Hero display | 48px | 600 | 56px | -0.04em |
| Large heading | 40px | 600 | 48px | -0.03em |
| Section heading | 32px | 600 | 40px | -0.025em |
| Card title | 24px | 600 | 32px | -0.02em |
| Body large | 20px | 400 | 32px | 0 |
| Body | 16px | 400 | 24px | 0 |
| Small / nav | 14px | 400 or 500 | 20px | 0 |
| Micro | 12px | 500 | 16px | 0.02em only when label-like |

> ⚠️ Extractor did not produce a structured scale table, but CSS frequency shows dominant sizes at 14px, 16px, 24px, 40px, 48px, 56px, 64px, and 72px with negative display tracking from `-.01em` through `-.06em`.

### Principles

1. Display type is compact, not loud. The hero earns weight through negative tracking and center placement.
2. Body copy stays gray and moderate. `#666666` text prevents the monochrome system from becoming harsh.
3. Weight `500` is common in UI labels and buttons; weight `600` is the practical heading weight.
4. Geist Mono is functional, not decorative. It belongs in code, SDK labels, counters, and product instrumentation.
5. Large text should never be loose. If Geist is substituted, tighten tracking before increasing weight.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (monochrome)

| Token | Hex |
|---|---|
| `--geist-background` | `#000000` |
| `--geist-foreground` | `#FFFFFF` |
| `--accents-1` | `#111111` |
| `--accents-2` | `#333333` |
| `--accents-4` | `#666666` |
| `--accents-7` | `#EAEAEA` |
| `--accents-8` | `#FAFAFA` |

### 06-2. Brand Dark Variant

| Token | Hex / Value |
|---|---|
| `--geist-background` | `#000000` |
| `--geist-foreground` | `#FFFFFF` |
| `--ds-gray-alpha-100` | `#FFFFFF0F` |
| `--ds-gray-alpha-500` | `#FFFFFF3D` |
| `--ds-gray-alpha-1000` | `#FFFFFFEB` |

### 06-3. Neutral Ramp

| Step | Light | Dark / Alpha |
|---|---|---|
| Surface | `#FFFFFF` | `#000000` |
| Subtle surface | `#FAFAFA` | `#111111` |
| Border | `#EAEAEA` | `#FFFFFF1A` |
| Muted text | `#666666` | `#FFFFFF9C` |
| Primary text | `#000000` | `#FFFFFFEB` |

### 06-4. Accent Families

| Family | Key step | Hex / Value |
|---|---|---|
| Blue | `--ds-blue-600` | OKLCH equivalent of vivid blue, legacy `#0070F3` appears in CSS |
| Green | `--ds-green-700` | OKLCH green ramp for status/product surfaces |
| Red | `--ds-red-600` | OKLCH red ramp for error/destructive states |
| Amber | `--ds-amber-600` | OKLCH amber ramp for warning states |
| Prism cyan/mint | hero artwork | `#2C8CE1`, `#45DEC4` from SVG/pattern candidates |

### 06-5. Semantic

| Token | Hex / Value | Usage |
|---|---|---|
| `--ds-contrast-fg` | `#FFFFFF` | text on black CTA |
| `--geist-error-light` | `#FF3333` | error states |
| `--geist-error-dark` | `#E60000` | dark error states |
| `--geist-violet-background` | `#291D3A` | legacy/product violet surface |
| `--ds-gray-1000` | HSL gray at 93% lightness in dark set | foreground in dark surfaces |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--ds-shadow-border` | `--ds-shadow-border-base`, `--ds-shadow-background-border` | card/menu edge definition |
| `--ds-shadow-menu` | multi-layer black alpha shadow + border | dropdown and navigation menu elevation |
| `--geist-page-width` | `1200px` | older page container |
| `--ds-page-width` | `1400px` | wider marketing/product container |
| `--geist-radius` | `6px` | default compact UI radius |
| `--geist-marketing-radius` | `8px` | softer marketing surface radius |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| transparent black | `#0000` | 260 |
| white | `#FFFFFF` / `#FFF` | 66-70 |
| black | `#000000` / `#000` | 64-69 |
| shadow alpha | `#0000000A` | 37 |
| transparent white | `#FFFFFF00` / `#FFF0` | 26-28 |
| border gray | `#EAEAEA` | 10 |

### 06-8. Color Stories

**`{colors.brand}` (`#000000`)** — The action color and brand color are the same. Use it for the primary CTA, logo triangle, and the strongest text, not as a generic dark background everywhere.

**`{colors.surface}` (`#FFFFFF`)** — The homepage floor. It should stay clean enough for hairline grid structure and prism color to be visible; avoid warm off-white substitutions.

**`{colors.text-muted}` (`#666666`)** — The humanizing gray. It carries subcopy and nav links so black can remain reserved for decisions.

**`{colors.border}` (`#EAEAEA`)** — The structural line. Vercel uses this where other SaaS sites would use shadow, tinted panels, or cards.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--geist-space` | 4px | base increment |
| `--geist-space-2x` | 8px | tight icon/text gap |
| `--geist-space-3x` | 12px | small internal padding |
| `--geist-space-4x` | 16px | button/card padding |
| `--geist-space-6x` | 24px | standard gap |
| `--geist-space-8x` | 32px | small section block |
| `--geist-space-10x` | 40px | form/control height rhythm |
| `--geist-space-16x` | 64px | major vertical air |
| `--geist-space-24x` | 96px | large section separation |
| `--geist-space-32x` | 128px | ceremonial hero/section separation |

**주요 alias**:
- `--geist-page-margin` → `24px` via `--geist-space-gap`
- `--geist-page-width` → `1200px`
- `--ds-page-width` → `1400px`

### Whitespace Philosophy

Vercel uses whitespace as a confidence signal. The hero is not dense: the nav sits lightly, the incident banner is centered above the grid, and the headline gets a large quiet field before the CTAs. This air makes the black CTA feel inevitable rather than aggressive.

Below the fold, spacing tightens into product density. The system moves from 64-128px ceremonial vertical air into 8-24px UI gaps, matching the shift from brand proposition to developer tooling.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `--geist-radius` | 6px | compact controls, nav buttons, small UI |
| `--geist-marketing-radius` | 8px | marketing panels |
| pill / rounded-full | 9999px | hero CTAs and announcement pills |
| card medium | 12px | product cards and larger containers |
| card large | 16px | feature panels |
| expressive | 20-24px | rare large marketing surfaces |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| Border | `0 0 0 1px #FFFFFF25`, plus background border | dark/menu hairline |
| Small | `0px 1px 2px #00000029` | small elevated controls |
| Medium | `0px 2px 2px #00000052, 0px 8px 8px -8px #00000029` | popovers |
| Large | `0px 2px 2px #0000000A, 0px 8px 16px -4px #0000000A` | cards/modals |
| Menu | border + `0px 1px 1px #00000005`, `0px 4px 8px -4px #0000000A`, `0px 16px 24px -8px #0000000F` | dropdown navigation |

Vercel shadow is mostly invisible in the homepage hero. Hairlines and grid geometry do the work; shadows are reserved for menus, modals, and interactive overlays.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| `--ds-motion-popover-duration` | present in token layer | popovers |
| `--ds-motion-popover-timing` | references `--ds-motion-timing-swift` | popovers |
| button transition | `background .2s`, `transform .15s`, `all .15s cubic-bezier(.3,.57,.07,.95)` | hover/active controls |
| color transition | `.1s` to `.2s` | links, icons, subtle hover |
| reduced motion | `prefers-reduced-motion` media queries present | accessibility fallback |

Motion should feel instantaneous and technical. Avoid elastic bounces, long fades, or decorative scroll choreography unless reproducing the prism artwork itself.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `1200px` (`--geist-page-width`) and `1400px` (`--ds-page-width`) both exist.
- **Grid type**: CSS Grid and Flexbox, with Tailwind utility layers.
- **Column count**: common CSS includes 10, 12, 14, and 18-column grids; homepage hero uses a visible rectilinear grid backdrop.
- **Gutter**: 24px base gap, with 8px and 16px micro gaps.

### Hero

- **Pattern Summary**: 70-80vh visible first viewport + white grid plane + centered H1 + dual CTA + spectral Vercel prism.
- Layout: one-column centered hero with top nav and centered incident/announcement pill.
- Background: `#FFFFFF` with thin grid lines and a spectrum prism artwork below the CTA row.
- **Background Treatment**: solid white + hairline grid + SVG/raster optical line burst; not a full-page gradient.
- H1: `48px` observed viewport / weight around `600` / tracking tightened around `-0.04em`.
- Max-width: centered copy around 760-900px, page grid around 1200-1400px.

### Section Rhythm

```css
section {
  padding: 64px 24px;
  max-width: var(--ds-page-width);
}
```

Hero spacing can expand beyond this, with visual breathing room above and below the headline.

### Card Patterns

- **Card background**: `#FFFFFF` or `#FAFAFA`
- **Card border**: `1px solid #EAEAEA`
- **Card radius**: 8px to 16px
- **Card padding**: 16px, 24px, 40px depending on density
- **Card shadow**: usually none on homepage; menu/modal surfaces use `--ds-shadow-*`

### Navigation Structure

- **Type**: horizontal desktop nav with grouped dropdown triggers.
- **Position**: top static/sticky-like marketing nav surface; screenshot shows top-aligned header.
- **Height**: approximately 64px.
- **Background**: `#FFFFFF`.
- **Border**: no heavy bottom rule in hero; dropdown/menu components use `#EAEAEA` or DS hairlines.

### Content Width

- **Prose max-width**: 42rem / 48rem utility values appear in CSS.
- **Container max-width**: `1200px`, `1248px`, `1400px`.
- **Sidebar width**: not a homepage primary pattern; documentation/product pages may differ.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `max-width: 600px` / `not all and (min-width: 601px)` | collapse dense nav and reduce hero typography |
| Tablet | `min-width: 601px` | two-column and medium grid behavior begins |
| Desktop | `min-width: 961px` | desktop nav/grid behavior |
| Wide | `min-width: 1200px`, `1248px`, `max-width: 1600px` | full marketing container and large hero canvas |

### Touch Targets

- **Minimum tap size**: target 40-48px for buttons; hero CTA uses 48px height.
- **Button height (mobile)**: likely 40-48px depending on component variant.
- **Input height (mobile)**: `--geist-form-height: 40px`; large form height `48px`.

### Collapsing Strategy

- **Navigation**: desktop grouped nav becomes compact/mobile menu below tablet.
- **Grid columns**: repeated grids collapse from multi-column to `repeat(1,minmax(0,1fr))` and 2-column variants.
- **Sidebar**: not primary on homepage.
- **Hero layout**: remains centered; typography and artwork crop/scale for smaller screens.

### Image Behavior

- **Strategy**: responsive artwork with fixed hero viewport crop.
- **Max-width**: `100%`, `90vw`, and fixed marketing widths appear.
- **Aspect ratio handling**: prism artwork is center-anchored and allowed to crop below the fold.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary hero CTA**

| Property | Value |
|---|---|
| Background | `#000000` |
| Text | `#FFFFFF` |
| Radius | `9999px` |
| Height | `48px` |
| Padding | `0 18px` to `0 22px` |
| Hover | subtle dark gray / transform or background transition around `.15s-.2s` |

```html
<a class="vercel-button vercel-button-primary">
  <span class="triangle-mark"></span>
  Start Deploying
</a>
```

**Secondary hero CTA**

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#000000` |
| Border | `1px solid #EAEAEA` |
| Radius | `9999px` |
| Height | `48px` |

### Badges

Announcement badge is a centered text line plus black pill CTA. It is not a colored marketing badge.

| Property | Value |
|---|---|
| Label text | `14px`, `#333333` or `#000000` |
| Pill background | `#111111` |
| Pill text | `#FFFFFF` |
| Radius | `9999px` |

### Cards & Containers

Vercel cards should be quiet bordered surfaces, not colorful panels.

| Property | Value |
|---|---|
| Background | `#FFFFFF` / `#FAFAFA` |
| Border | `1px solid #EAEAEA` |
| Radius | 8px / 12px / 16px |
| Shadow | none by default; DS shadow only for overlays |
| Hover | border-color or soft shadow, not scale-heavy animation |

### Navigation

Desktop nav is left-logo, grouped text links, right utility buttons.

| Element | Spec |
|---|---|
| Logo | black triangle + wordmark |
| Links | 14px, `#333333`/`#666666`, weight 400 |
| Dropdown trigger | text + small chevron |
| Utility buttons | 40px height, 6px radius |
| Sign Up | black filled rectangle with 6px radius |

### Inputs & Forms

Observed token layer includes form heights and font sizes even if homepage hero does not foreground forms.

| Token | Value |
|---|---|
| `--geist-form-height` | `40px` |
| `--geist-form-large-height` | `48px` |
| `--geist-form-font` | `.875rem` |
| Border | `#EAEAEA` / DS gray |
| Focus | ring via Tailwind/DS ring variables |

### Hero Section

The hero is a component in itself:

- Top nav with logo and grouped product/resource/solution menus.
- Incident banner: line text plus black pill action.
- Centered H1: tight Geist, high contrast.
- Subcopy: two-line gray text, balanced line breaks.
- CTA row: black primary + white secondary, both pills.
- Prism artwork: centered triangle with thin radiating chromatic lines.

### 13-2. Named Variants

**button-hero-primary** — black pill CTA, white text, optional triangle mark, 48px height.

**button-hero-secondary** — white pill CTA, black text, gray border, 48px height.

**button-nav-utility** — white compact rectangle, 6px radius, 40px height, used for Ask AI / Log In.

**button-nav-signup** — black compact rectangle, 6px radius, 40px height, used for Sign Up.

**announcement-action-pill** — black mini pill attached to a text announcement; smaller than hero CTA.

**grid-prism-hero** — grid-backed hero canvas with centered triangle and spectral line field.

### 13-3. Signature Micro-Specs

#### spectral-prism-grid

```yaml
spectral-prism-grid:
  description: "Vercel's hero turns 'AI Cloud' into a measured optics demo, not a decorative gradient."
  technique: "white background grid field with central triangular prism and dense radiating chromatic spectrum lines (SVG/canvas, hero-only)."
  applied_to: ["{component.hero-section}", "homepage marquee only"]
  visual_signature: "the page opens like a calibration print on a developer workbench — colour as measurement, not mood."
  intent: "infrastructure brands earn trust by performing precision; the prism is proof, not poster art."
```

#### hairline-instead-of-shadow

```yaml
hairline-instead-of-shadow:
  description: "Structural separation is delivered by 1px lines, never by ambient SaaS depth."
  technique: "1px solid #EAEAEA borders on cards/nav/grid; DS shadow tokens reserved exclusively for overlays/menus."
  applied_to: ["{component.cards-containers}", "{component.navigation}", "feature grid", "dropdown menus"]
  visual_signature: "the page reads as a CAD drawing — every cell defined by line, not by haze."
  intent: "Geist DS treats elevation as a finite resource. Spending it on every card cheapens the rare overlay."
```

#### geist-tight-display

```yaml
geist-tight-display:
  description: "Display headlines compress through negative tracking instead of bumping weight."
  technique: "Geist sans at weight 600 with letter-spacing roughly -0.02em (md) → -0.06em (xxl) on H1/H2/H3 only; body keeps 0."
  applied_to: ["{typography.h1}", "{typography.h2}", "{typography.h3}", "{component.hero-section}"]
  visual_signature: "headlines feel engraved, dense but calm — never shouted."
  intent: "developer audiences read negative tracking as authored care; expanded tracking would feel marketing-soft."
```

#### dual-radius-buttons

```yaml
dual-radius-buttons:
  description: "Vercel encodes CTA hierarchy in radius, not in colour."
  technique: "hero CTAs use radius 9999px (full pill); nav/utility buttons use radius 6px rounded rectangles; same black fill across both."
  applied_to: ["{components.button-hero}", "{components.button-nav-utility}"]
  visual_signature: "marketing CTAs feel warm and inviting; nav controls feel like exact tool-tabs — both still unmistakably Vercel-black."
  intent: "monochrome systems must invent non-colour hierarchy; radius is Geist's quiet substitute for accent hue."
```

#### motion-prefers-reduced-default

```yaml
motion-prefers-reduced-default:
  description: "Vercel ships the AI-Cloud spectacle but defers to the user's OS motion preference by default."
  technique: "prism animation + hover transitions wrapped in `@media (prefers-reduced-motion: no-preference)`; static spectrum frame served otherwise."
  applied_to: ["{component.hero-section}", "homepage decorative motion"]
  visual_signature: "even the kinetic moments feel disciplined — motion is opt-in, not assumed."
  intent: "an infrastructure brand cannot ship motion that disrespects accessibility settings; restraint is the brand."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Direct infrastructure promise, one strong noun phrase | "Build and deploy on the AI Cloud." |
| Primary CTA | Verb-led developer action | "Start Deploying" |
| Secondary CTA | Sales/support path | "Get a Demo" |
| Subheading | Developer tools + infrastructure + outcome | "build, scale, and secure..." |
| Tone | confident, technical, short, non-playful | product language, not lifestyle copy |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Vercel — copy into your root stylesheet */
:root {
  /* Fonts */
  --vc-font-family: "Geist", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --vc-font-family-code: "Geist Mono", ui-monospace, SFMono-Regular, Roboto Mono, Menlo, monospace;
  --vc-font-weight-normal: 400;
  --vc-font-weight-strong: 600;

  /* Brand */
  --vc-color-brand: #000000;
  --vc-color-brand-hover: #333333;
  --vc-color-on-brand: #FFFFFF;

  /* Surfaces */
  --vc-bg-page: #FFFFFF;
  --vc-bg-subtle: #FAFAFA;
  --vc-text: #000000;
  --vc-text-muted: #666666;
  --vc-border: #EAEAEA;

  /* Prism accents - use sparingly */
  --vc-prism-blue: #2C8CE1;
  --vc-prism-mint: #45DEC4;

  /* Spacing */
  --vc-space-1: 4px;
  --vc-space-2: 8px;
  --vc-space-3: 12px;
  --vc-space-4: 16px;
  --vc-space-6: 24px;
  --vc-space-8: 32px;
  --vc-space-16: 64px;
  --vc-space-24: 96px;

  /* Radius */
  --vc-radius-control: 6px;
  --vc-radius-marketing: 8px;
  --vc-radius-card: 12px;
  --vc-radius-pill: 9999px;
}

.vc-hero {
  min-height: 720px;
  background:
    linear-gradient(#EAEAEA 1px, transparent 1px),
    linear-gradient(90deg, #EAEAEA 1px, transparent 1px),
    #FFFFFF;
  background-size: 90px 90px;
  color: var(--vc-text);
  text-align: center;
}

.vc-hero h1 {
  font-family: var(--vc-font-family);
  font-size: clamp(40px, 5vw, 72px);
  line-height: .95;
  font-weight: 600;
  letter-spacing: -0.04em;
}

.vc-button-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 48px;
  padding: 0 18px;
  border-radius: var(--vc-radius-pill);
  background: #000000;
  color: #FFFFFF;
  border: 1px solid #000000;
  transition: background .2s, transform .15s;
}

.vc-button-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 48px;
  padding: 0 22px;
  border-radius: var(--vc-radius-pill);
  background: #FFFFFF;
  color: #000000;
  border: 1px solid #EAEAEA;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Vercel-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        vercel: {
          black: '#000000',
          white: '#FFFFFF',
          muted: '#666666',
          border: '#EAEAEA',
          subtle: '#FAFAFA',
          prismBlue: '#2C8CE1',
          prismMint: '#45DEC4',
        },
      },
      fontFamily: {
        sans: ['Geist', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['Geist Mono', 'ui-monospace', 'SFMono-Regular', 'monospace'],
      },
      borderRadius: {
        geist: '6px',
        marketing: '8px',
        card: '12px',
        pill: '9999px',
      },
      boxShadow: {
        'vercel-menu': '0 0 0 1px #ffffff25, 0 1px 1px #00000005, 0 4px 8px -4px #0000000a, 0 16px 24px -8px #0000000f',
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
| Brand primary | `{colors.brand}` | `#000000` |
| Background | `{colors.surface}` | `#FFFFFF` |
| Text primary | `{colors.text-primary}` | `#000000` |
| Text muted | `{colors.text-muted}` | `#666666` |
| Border | `{colors.border}` | `#EAEAEA` |
| Subtle surface | `{colors.surface-subtle}` | `#FAFAFA` |
| Prism accent | `{colors.ai-mint}` | `#45DEC4` |

### Example Component Prompts

#### Hero Section
```text
Vercel 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF 위에 #EAEAEA 1px hairline grid
- H1: Geist, clamp(40px, 5vw, 72px), weight 600, letter-spacing -0.04em
- 서브텍스트: #666666, 20px/32px, 중앙 정렬
- CTA: primary #000000 pill + secondary #FFFFFF pill with #EAEAEA border
- 시그니처: CTA 아래 중앙에 Vercel triangle/prism optical artwork
```

#### Card Component
```text
Vercel 스타일 카드 컴포넌트를 만들어줘.
- 배경 #FFFFFF 또는 #FAFAFA
- border 1px solid #EAEAEA
- radius 12px, shadow 없음
- 제목 Geist 16px/24px weight 600, 본문 #666666 14px/20px
- hover는 border-color 또는 아주 약한 shadow만 사용
```

#### Navigation
```text
Vercel 스타일 상단 네비게이션을 만들어줘.
- 좌측: 검정 Vercel triangle + wordmark
- 링크: 14px Geist, #333333, Products/Resources/Solutions는 chevron 포함
- 우측: Ask AI / Log In은 white 6px button, Sign Up은 black 6px button
- 배경 #FFFFFF, heavy border나 컬러 accent 금지
```

### Iteration Guide

- **색상 변경 시**: brand/action은 `#000000` 유지. chroma는 hero prism 또는 status/product accents에만 허용.
- **폰트 변경 시**: Geist가 없으면 Inter로 대체하되 display tracking을 더 타이트하게 보정.
- **여백 조정 시**: 4px base ladder를 지키고, hero는 64px 이상의 큰 air를 유지.
- **새 컴포넌트 추가 시**: shadow보다 `#EAEAEA` hairline border를 먼저 사용.
- **반응형**: 600px / 961px / 1200px 계열 breakpoint를 우선 사용.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#000000` as the primary action and brand anchor.
- Keep homepage surfaces `#FFFFFF` with `#EAEAEA` hairlines.
- Use Geist/Geist Mono and preserve tight display tracking.
- Reserve chromatic color for prism, status, code/product highlights, or small data accents.
- Build cards with borders and restrained radius before adding shadows.
- Use pill CTAs in hero, but compact 6px-radius buttons in nav utility areas.
- Let the grid and triangle mark do the brand work.

### ❌ DON'T

- 배경을 `#F7F7F5`, `#F5F5F7`, 또는 warm off-white로 두지 말 것 — 대신 `#FFFFFF` 사용.
- 본문 텍스트를 `#111827` 또는 `#1F2937` 같은 Tailwind slate로 두지 말 것 — 대신 `#000000` / `#666666` 사용.
- border를 `#D1D5DB`처럼 진한 gray로 두지 말 것 — 대신 `#EAEAEA` hairline 사용.
- primary CTA를 `#0070F3`로 두지 말 것 — 대신 `#000000` 사용.
- hero 전체 배경을 `#667EEA` → `#764BA2` gradient로 만들지 말 것 — 대신 `#FFFFFF` grid + prism accent 사용.
- 카드를 `box-shadow: 0 20px 40px #0000001A` 같은 큰 SaaS shadow로 띄우지 말 것 — 대신 `1px solid #EAEAEA`를 기본값으로 사용.
- H1에 `letter-spacing: 0`을 쓰지 말 것 — 대신 `-0.03em` ~ `-0.06em` 범위로 조인다.
- hero CTA radius를 `6px`로 만들지 말 것 — 대신 `9999px` pill 사용.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second brand color: **absent** — lab bench는 single instrument lighting으로만 운영되고, 보조 brand hue는 등장하지 않는다.
- Warm neutrals: **none** — 작업판은 cool white laminate, cream/beige/sand surface는 zero.
- Decorative card gradients: **never** — chroma는 prism 시연 결과지 카드 페인트가 아니다.
- Heavy shadows on chrome: **zero** as default — 구조는 blueprint hairline + 공구함 정렬이 만든다.
- Playful illustration language: **absent** — hero의 prism은 optical 측정 기기, 일러스트 cartoon은 등장하지 않는다.
- Loose display typography: **never** — engraved 시연 caption처럼 dense, 자간이 풀어지는 일은 없다.
- Rounded-everything softness: **absent** — hero CTA pill 외 모든 utility 공구는 6px 직사각으로 정렬된다.
- Logo-wall color pollution as brand: **none** — SVG/고객 logo accent는 brand palette를 재정의하지 않는다.
- Generic AI purple gradient: **never** — AI 시연은 prism + copy로 표현, purple fog는 zero.
- Second filled hero CTA color: **absent** — 검정 toggle 하나만 채워지고, 보조는 흰 outline 스위치로만 남는다.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-focused analysis** — The reused artifacts target `https://vercel.com` and the captured hero. Product dashboards, docs, pricing flows, account settings, and checkout-like surfaces may use different density rules.
- **No fresh fetch in this run** — Existing phase1 assets were reused as requested. The screenshot contains a May 2026 security incident banner, so the above reflects that captured homepage state.
- **Typography scale inferred from CSS frequency** — `typography.json` did not include a structured `scale` object; the scale is derived from CSS declarations and hero screenshot observation.
- **OKLCH colors not all converted to hex** — DS blue/red/green/amber ramps are present as OKLCH and HSL variables. Hex values are only listed where the CSS exposed concrete hex or where screenshot/pattern candidates surfaced them.
- **Prism artwork exact implementation not fully decomposed** — The visual is identified from screenshot and CSS/SVG color candidates, but individual line counts, stops, and masks were not exhaustively reverse-engineered.
- **Interactive dropdown states not fully visited** — HTML/CSS shows menu/button/modal rules, but live hover/focus/dropdown screenshots were not collected in this run.
- **Dark theme exists but homepage default is light** — Dark token counterparts are present; this report treats dark mode as supporting system evidence, not the primary homepage theme.
- **Logo/customer colors filtered conceptually** — Top CSS frequency includes SVG/pattern colors. They are treated as artwork/product accents, not brand palette anchors.
