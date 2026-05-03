---
schema_version: 3.2
slug: arc
service_name: Arc
site_url: https://arc.net
fetched_at: 2026-04-14T01:14:00+09:00
default_theme: mixed
brand_color: "#3139FB"
primary_font: "Marlin Soft SQ"
font_weight_normal: 400
token_prefix: "--colors"

bold_direction: "Playful Editorial"
aesthetic_category: "other"
signature_element: "hero_impact"
code_complexity: "high"

medium: web
medium_confidence: high

archetype: editorial-product
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "130 CSS variables, named brand tokens, custom font stacks, responsive breakpoints, and reusable button/input primitives are present, but the public page is not a formal design-system catalog."

colors:
  primary: "#3139FB"
  deep-blue: "#2404AA"
  dark-blue: "#000354"
  brand-red: "#FB3A4D"
  brand-offwhite: "#FFFCEC"
  hero-cream: "#FFFCEA"
  text-primary: "#000000"
  text-muted: "#6F6F6F"
  hairline: "#171717"
  focus: "#96C4FF"
typography:
  display: "Marlin Soft SQ"
  body: "InterVariable"
  mono: "ABC Favorit Mono"
  ladder:
    - { token: display-xl, size: "45.51px", weight: 700, line_height: "42.25px", tracking: "-0.04em" }
    - { token: display, size: "36px", weight: 700, line_height: "1.2", tracking: "-0.72px" }
    - { token: headline, size: "30px", weight: 700, line_height: "1", tracking: "-0.01em" }
    - { token: body-lg, size: "20px", weight: 400, line_height: "1.5", tracking: "0" }
    - { token: body, size: "16px", weight: 400, line_height: "1.5", tracking: "0" }
    - { token: micro, size: "12px", weight: 600, line_height: "15px", tracking: "0.025rem" }
  weights_used: [350, 400, 500, 600, 650, 700, 750, 800, 900]
  weights_absent: [300]
components:
  dia-primary-cta: { bg: "#171717", fg: "#FFFFFF", radius: "22px", padding: "14px 22px", shadow: "0 2px 8px rgba(0,0,0,.25)" }
  brand-blue-nav: { bg: "#3139FB", fg: "#FFFFFF", height: "96px", treatment: "textured blue band with scalloped lower edge" }
  white-browser-frame: { bg: "#FFFFFF", radius: "16px", border: "soft gray hairline", shadow: "subtle multi-layer screenshot shadow" }
---

# DESIGN.md — Arc

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Arc's current public face is no longer a sober productivity-browser pitch. The first screen behaves like a bright editorial announcement for Dia: a thick electric-blue stage band, a scalloped paper-cut edge, a warm cream-to-pink wash, and a large browser mockup that sits like a product specimen under a gallery light. The page is selling a browser, but the composition speaks like a launch poster pinned over a software demo.

The visual identity is built on collision rather than neutrality. `#3139FB` (`{colors.primary}`) is not an accent; it is the room, the curtain, and the painted stage floor. `#FFFCEA` (`{colors.hero-cream}`) and `#FFFCEC` (`{colors.brand-offwhite}`) keep the middle from becoming sterile browser chrome, while `#FB3A4D` (`{colors.brand-red}`) works like a tiny red sticker on a blue notebook rather than a second brand system. There is no secondary rainbow and no SaaS gradient mesh; Arc lets one impossible blue carry the atmosphere.

The scalloped divider is the page's most tactile metaphor. A straight rule would make this feel like a web section break; the repeated cut edge makes the blue band feel like construction paper laid over a cream sheet. Arc's hero has the charm of a folded launch poster on a studio wall: intentionally flat, handmade at the boundary, but precise in the center where the product appears.

Typography carries the personality harder than the layout. Marlin Soft SQ gives the hero headline a friendly, almost storybook weight, with `-0.04em` compression keeping it polished instead of cute. InterVariable and ABC Favorit Mono then clean up the smaller language like product labels in a small exhibition: quiet enough to read, never trying to become the show.

The most important craft move is the fake-browser product frame. The page places a specific app screenshot inside a large white chrome shell, then half-submerges it from the cream field into the lower blue band. It feels less like a dashboard card and more like a browser prototype sliding out of a display tray; the screenshot becomes the physical object, while the surrounding page keeps removing itself.

Negative identity matters here. Arc does not use the familiar "gradient mesh plus three feature cards" SaaS formula, does not make the primary CTA blue, and does not spread dense app UI across the marketing page. The top page is theatrical, centered, and almost poster-like, with only enough interface detail to make the Dia promise concrete.

### Key Characteristics

- Electric blue `#3139FB` is a full-width environmental color, not a small CTA accent.
- Hero headline uses a soft, rounded display face rather than a severe productivity sans.
- Warm off-white `#FFFCEA` separates the product story from pure browser chrome.
- Scalloped horizontal edge creates a handmade, playful transition between blue and hero.
- Product screenshot is cropped large and low, making the browser frame the hero object.
- CTA is dark, pill-like, shadowed, and icon-led: it reads like an app launcher.
- Navigation is compact, white-on-blue, and left-weighted around product audiences.
- Red `#FB3A4D` appears as brand energy, not as error/status color.
- The page mixes editorial launch energy with a very concrete UI specimen.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Playful Editorial
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **electric-blue scalloped launch stage around a tangible browser frame**으로 기억된다.
> **Code Complexity**: high — textured hero bands, custom fonts, responsive framing, multi-layer screenshot treatment, and branded component variants must align.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Arc처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "InterVariable", "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
}
h1, .display {
  font-family: "Marlin Soft SQ", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 700;
  letter-spacing: -0.04em;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFCEA; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #3139FB; --brand-red: #FB3A4D; }
.stage-band { background: var(--brand); color: #FFFFFF; }
```

**절대 하지 말아야 할 것 하나**: Arc를 흰 배경의 일반 SaaS 랜딩처럼 만들지 말 것. `#3139FB` 블루 밴드와 `#FFFCEA` warm hero floor가 빠지면 Arc의 현재 launch-poster 성격이 사라진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://arc.net` |
| Fetched | 2026-04-14T01:14:00+09:00 |
| Extractor | reused phase1 artifacts from `insane-design/arc/` |
| HTML size | 641076 bytes |
| CSS files | 2 files, about 222054 chars |
| Token prefix | `--colors`, `--fonts`, `--space`, `--fontSizes` |
| Method | CSS custom property parsing, phase1 JSON summaries, screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React/Next-style static app output with Stitches-like generated classes (`c-*`, `PJLV-*`).
- **Design system**: Arc/The Browser Company token layer — prefix families `--colors-*`, `--fonts-*`, `--space-*`, `--fontSizes-*`.
- **CSS architecture**:
  ```css
  :root                 /* raw brand, font, space, max-width variables */
  .c-* / .PJLV-*         /* generated component classes */
  media queries          /* min-width 580px / 800px plus larger viewport refinements */
  ```
- **Class naming**: generated atomic/component hybrids such as `.c-bCeQxv`, `.c-kXCYdJ`, `.PJLV-ifbylVT-css`.
- **Default theme**: mixed; hero uses warm light surface, navigation and page bands use saturated blue.
- **Font loading**: multiple custom families declared in CSS: Marlin, Marlin Soft SQ, InterVariable, ABC Favorit Mono, ABC Oracle, Exposure VAR.
- **Canonical anchor**: first viewport with blue nav band, scalloped divider, centered Dia hero, and oversized browser screenshot.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Marlin Soft SQ` / `Marlin Soft Basic` / `Marlin`
- **Body font**: `InterVariable`, `Inter`
- **Mono font**: `ABC Favorit Mono`, with `Space Mono` also present
- **Expressive alternates**: `ABC Oracle`, `Exposure VAR`, `Sohne Breit`, `EB Garamond`
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --fonts-sans: Marlin, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --fonts-body: "InterVariable", "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
  --fonts-softSans: Marlin Soft SQ, -apple-system, BlinkMacSystemFont, sans-serif;
  --fonts-mono: ABC Favorit Mono, Menlo, Monaco, "Courier New", monospace;
}

body { font-family: var(--fonts-body); font-weight: 400; }
h1 { font-family: var(--fonts-softSans); font-weight: 700; letter-spacing: -0.04em; }
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Marlin Soft SQ** — licensed/custom; if unavailable, use **Cooper Black only for rough mood tests**, or better **Fraunces Soft/Wonka-like rounded serif at 700** with `letter-spacing: -0.035em`. Do not replace it with plain Inter; the headline loses the friendly, bulbous Arc quality.
- **InterVariable** — safe substitute is **Inter** at 400/500/700 with `line-height: 1.5`. Keep body tracking at `0`; the display face already carries the optical compression.
- **ABC Favorit Mono** — substitute with **Space Mono** at 400/600 and slightly reduced size (`12px` instead of `13px`) for metadata and small UI labels.
- **Exposure VAR / ABC Oracle** — only use when recreating secondary editorial sections. They are not required for the first viewport.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| display-xl | 45.51px | 700 | 42.25px | -0.04em |
| display | 36px | 700 | 1.2 | -0.72px |
| headline | 30px | 700 | 1 | -0.01em |
| body-lg | 20px | 400 | 1.5 | 0 |
| body | 16px | 400 | 1.5 | 0 |
| caption | 14px | 500 | 24px | 0 |
| micro | 12px | 600 | 15px | 0.025rem |
| label | 10px | 600 | 15px | 0.025rem |

> Arc's extracted typography is not a clean single ladder; it is a mixed editorial/product stack. The important signature is the display compression: large text gets negative tracking, body text does not.

### Principles
<!-- SOURCE: manual -->

1. Display type is round and compressed, not neutral and airy. The hero needs `Marlin Soft SQ`-style softness plus negative tracking.
2. Body copy should stay untheatrical. Inter at 400 with line-height around `1.5` keeps the product promise readable.
3. Weight 700 belongs to headlines and strong UI statements; body should not drift into 500 everywhere.
4. Mono is a supporting accent for utility/code-like fragments, not a global voice.
5. The design accepts multiple custom families because the page is editorial-product, not a strict dashboard shell.
6. Large display lines are tight (`42.25px` line-height on `45.51px` type); copying this with default line-height will feel too loose.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (5 steps)

| Token | Hex |
|---|---|
| `--colors-brandDarkBlue` | `#000354` |
| `--colors-brandDeepBlue` | `#2404AA` |
| `--colors-brandBlue` | `#3139FB` |
| `--colors-brandRed` | `#FB3A4D` |
| `--colors-brandOffwhite` | `#FFFCEC` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--colors-brandDarkBlue` | `#000354` |
| `--colors-brandDeepBlue` | `#2404AA` |
| `--colors-highContrast` | `#000000` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| low contrast | `#FFFFFF` | `#000000` |
| gray 1 | `#6F6F6F` | `#171717` |
| warm floor | `#FFFCEA` | `#FFFCEC` |
| pale indigo | `#F0F1FF` | `#0047FF` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Red / Arc mark | brand red | `#FB3A4D` |
| Primary red ramp | primary6 | `rgb(250, 69, 49)` |
| Yellow | yellow fg | `#FFB223` |
| Focus | focus outline | `#96C4FF` |
| Student blue | arc blue | `rgb(12, 80, 255)` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--colors-lowContrast` | `#FFFFFF` | white text and light UI chrome |
| `--colors-highContrast` | `#000000` | primary text |
| `--colors-focusOutline` | `#96C4FF` | keyboard focus outline |
| `--color-indigo-bg` | `#F0F1FF` | pale blue/indigo support surface |
| `--color-indigo-fg` | `#0047FF` | indigo foreground/action color |
| `--color-red-bg` | `#FEF1ED` | pale red support surface |
| `--color-red-fg` | `#E5484D` | red foreground/action color |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--colors-brandBlue` | `#3139FB` | primary environmental band |
| `--colors-brandDeepBlue` | `#2404AA` | darker blue depth and alternate CTA tone |
| `--colors-brandOffwhite` | `#FFFCEC` | brand warm surface |
| `--colors-brandRed` | `#FB3A4D` | logo/brand energy |
| `--colors-focusOutline` | `#96C4FF` | accessible focus ring |

### 06-7. Dominant Colors (actual CSS frequency)

| Token | Hex | Frequency |
|---|---:|---:|
| brand blue | `#3139FB` | 17 |
| warm hero cream | `#FFFCEA` | 11 |
| low contrast white | `#FFFFFF` | 9 |
| deep action blue | `#2702C2` | 6 |
| high contrast black | `#000000` | 5 |
| brand deep blue | `#2404AA` | 3 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.primary}` (`#3139FB`)** — The stage color. It owns the top and bottom bands, frames the page, and tells the viewer this is Arc before any product screenshot is understood. Use it in large confident planes, not as tiny link blue.

**`{colors.hero-cream}` (`#FFFCEA`)** — The warm product floor. It keeps the hero from becoming sterile SaaS white and makes the browser mockup feel printed on soft paper. Use it behind major product storytelling, especially when blue is nearby.

**`{colors.text-primary}` (`#000000`)** — The crisp editorial ink. Arc can use pure black because the surrounding surfaces are soft and colorful. Do not gray the main headline down.

**`{colors.brand-red}` (`#FB3A4D`)** — The brand spark. It belongs in the logo and small personality moments, not as a generic destructive/error color.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--space-4` | 4px | tiny UI separations |
| `--space-8` | 8px | icon/link gaps |
| `--space-12` | 12px | compact controls |
| `--space-16` | 16px | card and nav internal padding |
| `--space-24` | 24px | grouped UI spacing |
| `--space-32` | 32px | small section rhythm |
| `--space-40` | 40px | hero cluster spacing |
| `--space-48` | 48px | vertical content rhythm |
| `--space-56` | 56px | large block separation |
| `--space-64` | 64px | section breathing room |
| `--space-72` | 72px | major editorial spacing |

**주요 alias**:
- `--max-width` → `960px` and `1280px` observed, depending on layout scope.
- `90vw` → repeated responsive containment before fixed max-widths such as `700px`, `864px`, `900px`, `1200px`, `1400px`.

### Whitespace Philosophy
<!-- SOURCE: manual -->

Arc's first viewport uses generous vertical theater around a tight centered message. The headline, subtitle, and CTA form a compact stack, then the browser screenshot begins after a full breath. The page is not dense until the product UI appears inside the mockup; outside the mockup, air and color do the persuasion.

The spacing system alternates between poster-scale bands and small product-detail gaps. Nav items sit close together on the blue band, the CTA has only enough padding to feel like an app launcher, and the mockup gets the large margin. This contrast is the point: public page as stage, screenshot as dense evidence.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Context |
|---|---:|---|
| small control | 4px | compact utility UI |
| medium control | 8px | nav and small buttons |
| soft panel | 10px | grouped product UI blocks |
| browser frame | 16px | large screenshot shell |
| pill CTA | 22px / 25px | primary Dia button and rounded capsules |
| rem radius | 0.5rem | responsive generated class fallback |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none | `box-shadow: none` | reset/focus override |
| soft chrome | `0px 4px 11px rgba(0,0,0,.02), 0px 1px 2px rgba(0,0,0,.03)` | subtle white product containers |
| dark CTA | `0px 2px 8px rgba(0,0,0,.25)` | black Dia CTA button |
| floating object | `0 7px 15px rgba(0,0,0,.2)` | heavier product/object lift |
| light object | `0 2px 6px rgba(0,0,0,.1)` | secondary surfaces |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| CTA affordance | subtle arrow movement implied by icon-led CTA | communicate forward action without heavy animation |
| screenshot reveal | large mockup crop with viewport overflow | product appears to rise from page bands |
| focus outline | `2px solid var(--colors-gray7)` equivalent | keyboard state clarity |

> No full motion-token system was recovered from phase1. Treat motion as supporting polish, not the brand signature.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `960px` default token, with page-specific caps at `700px`, `864px`, `900px`, `1200px`, `1400px`, and `90rem`.
- **Grid type**: flex-first generated components; selective CSS Grid for auto-fit groups.
- **Column count**: hero is centered one-column; secondary grids use `repeat(auto-fit, minmax(140px, 1fr))`.
- **Gutter**: common gaps include `6px`, `10px`, `12px`, `14px`, `1rem`, `1.25rem`, `1.5rem`, `2rem`, and `5rem`.

### Hero

- **Pattern Summary**: blue band + scalloped divider + centered Dia announcement + dark icon CTA + oversized browser-frame screenshot.
- Layout: one-column centered editorial stack above a product mockup.
- Background: saturated `#3139FB` top/bottom bands with warm `#FFFCEA` middle field and faint pink edge tint.
- **Background Treatment**: solid brand blue plus decorative scalloped boundary; warm cream hero surface; product screenshot fades/crops into lower blue band.
- H1: `45.51px` / weight `700` / tracking `-0.04em` observed in CSS; screenshot headline appears large, soft, and centered.
- Max-width: headline cluster visually around `700px`; product frame extends wider, around `90vw` up to large desktop caps.

### Section Rhythm

```css
section {
  padding: 64px 24px;
  max-width: min(90vw, 960px);
}
.hero-product-frame {
  width: min(90vw, 1200px);
  border-radius: 16px;
}
```

### Card Patterns

- **Card background**: `#FFFFFF` for browser/product chrome, warm surfaces for page fields.
- **Card border**: soft gray hairline; screenshot frame uses subtle boundary rather than heavy outline.
- **Card radius**: `16px` for browser frame, `8px` to `10px` for small interior tiles.
- **Card padding**: product UI tiles compress around `12px` to `16px`; page-level spacing is much larger.
- **Card shadow**: soft multi-layer shadow for product frame, heavier `rgba(0,0,0,.25)` for dark CTA.

### Navigation Structure

- **Type**: horizontal semantic nav.
- **Position**: top band; visually static in captured first viewport.
- **Height**: approximately `96px` blue stage area in screenshot.
- **Background**: `#3139FB` with textured/noisy rendering.
- **Border**: no straight border; scalloped lower edge is the signature separation.

### Content Width

- **Prose max-width**: about `700px` for centered hero copy.
- **Container max-width**: `960px` token and broader `1200px`/`1400px` product-frame caps.
- **Sidebar width**: not part of the page layout; sidebar appears only inside the product screenshot.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Small-plus | `580px` | first min-width enhancement for mobile-first layout |
| Tablet / nav fold | `800px` | both min and max queries present; likely key layout transition |
| Desktop enhancement | `1000px` / `1075px` | larger viewport refinements |
| Large height | `1100px+` / `1360px+` | tall-screen hero/frame adjustment |

### Touch Targets

- **Minimum tap size**: not fully confirmed by CSS extraction; phase1 did not find explicit 44px button heights.
- **Button height (mobile)**: infer from CTA visual as roughly 56px+, but exact CSS value was not isolated.
- **Input height (mobile)**: not observed on public hero; input exists only as generic `input { font-family: var(--font-sans) }`.

### Collapsing Strategy

- **Navigation**: likely switches around `800px`; captured desktop shows horizontal nav.
- **Grid columns**: `auto-fit minmax(140px, 1fr)` handles secondary dense groups.
- **Sidebar**: page has no sidebar; product screenshot contains one.
- **Hero layout**: stays centered one-column; product frame scales by `90vw` and max-width caps.

### Image Behavior

- **Strategy**: product screenshot is the primary image object; it is cropped large and anchored low.
- **Max-width**: `90vw` and broad max-width caps.
- **Aspect ratio handling**: browser-frame proportion preserved; lower part intentionally cropped by viewport/band.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Dia primary CTA**

| Property | Value |
|---|---|
| Background | `#171717` / near-black |
| Text | `#FFFFFF` |
| Radius | `22px` to `25px` pill |
| Padding | about `14px 22px` |
| Shadow | `0px 2px 8px rgba(0,0,0,.25)` |
| Anatomy | rounded app icon tile + label + arrow |
| State | focus should use `#96C4FF` outline, not default browser blue |

**Base button reset**

```css
button {
  background: transparent;
  border: 0;
  padding: 0;
  margin: 0;
  font-family: var(--font-sans);
}
button:focus-visible {
  box-shadow: none;
  outline: 2px solid var(--colors-focusOutline);
}
```

### Badges

No conventional marketing badge/pill was observed in the captured hero. Arc prefers the app-icon CTA tile and audience nav labels over small "New" badges.

### Cards & Containers

**Browser product frame**

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Radius | `16px` |
| Border | soft hairline / low-contrast gray |
| Shadow | subtle multi-layer product shadow |
| Layout | large centered screenshot, width close to `90vw` |
| Purpose | make Dia tangible without turning the whole page into dashboard UI |

**Interior app tiles**

| Property | Value |
|---|---|
| Background | pale gray / white tiles inside screenshot |
| Radius | `8px` to `10px` |
| Grid | compact grouped app shortcuts |
| Density | much denser than public page chrome |

### Navigation

| Property | Value |
|---|---|
| Background | `#3139FB` |
| Text | `#FFFFFF` |
| Items | Arc mark, Max, Mobile, Developers, Students, Blog |
| Layout | left-weighted horizontal row |
| Separator | scalloped lower edge instead of a hairline border |

### Inputs & Forms

No public form input is prominent in the first viewport. The extracted CSS only confirms generic input font inheritance:

```css
input { font-family: var(--font-sans); }
```

If recreating a form, keep it visually subordinate: white or cream surface, black text, `8px` to `10px` radius, and `#96C4FF` focus outline.

### Hero Section

| Property | Value |
|---|---|
| H1 | "Meet Dia, the next evolution of Arc" |
| H1 font | `Marlin Soft SQ`-like display |
| Subtitle | centered gray support copy |
| CTA | dark rounded "Try Dia" launcher |
| Product media | large browser frame screenshot |
| Background | `#3139FB` band + `#FFFCEA` field |
| Signature edge | scalloped blue-to-cream transition |

### 13-2. Named Variants
<!-- SOURCE: manual -->

- **dia-primary-cta** — black rounded launcher button with app icon tile, white label, arrow, and dark shadow.
- **brand-blue-nav** — horizontal white-on-`#3139FB` nav embedded in a textured blue band.
- **scalloped-stage-divider** — decorative repeated wave edge between blue band and warm hero field.
- **white-browser-frame** — large product screenshot container with `#FFFFFF` chrome, `16px` radius, and soft shadow.
- **in-screenshot-chat-pill** — pale blue rounded prompt bubble inside the product mockup, used as product evidence rather than page UI.

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
blue-paper-scallop:
  description: "Physical paper-cut transition between brand stage and warm hero floor."
  technique: "repeated scalloped edge separating #3139FB /* {colors.primary} */ from #FFFCEA /* {colors.hero-cream} */; avoid straight border or gradient-only fade"
  applied_to: ["{component.brand-blue-nav}", "{component.scalloped-stage-divider}", "{component.hero-section}"]
  visual_signature: "The top band reads like blue construction paper laid over cream paper, not a standard web section."

launcher-cta-compound:
  description: "Primary action behaves like a small app launcher, not a flat marketing button."
  technique: "background #171717; color #FFFFFF; border-radius 22px-25px; padding about 14px 22px; box-shadow 0px 2px 8px rgba(0,0,0,.25); icon tile + label + arrow in one inline-flex unit"
  applied_to: ["{component.dia-primary-cta}"]
  visual_signature: "The button feels like a clickable Dia app object sitting on the poster surface."

half-submerged-browser-frame:
  description: "Product evidence enters the page as a large white browser object cropped into the blue band."
  technique: "width min(90vw, 1200px); margin-top about 56px; background #FFFFFF; border-radius 16px; border 1px solid rgba(0,0,0,.08); box-shadow 0 4px 11px rgba(0,0,0,.02), 0 1px 2px rgba(0,0,0,.03); low crop into lower #3139FB band"
  applied_to: ["{component.white-browser-frame}", "{component.hero-section}"]
  visual_signature: "The screenshot looks like a physical browser specimen sliding from cream paper into the blue stage."

soft-display-compression:
  description: "Round display type is optically tightened so the friendly voice stays premium."
  technique: "Marlin Soft SQ display; font-weight 700; hero size observed around 45.51px with 42.25px line-height; letter-spacing -0.04em"
  applied_to: ["{component.hero-section}"]
  visual_signature: "The headline feels bulbous and warm but not loose or childish."

warm-cream-edge-wash:
  description: "Cream hero floor receives a faint color wash without becoming a full gradient-mesh SaaS background."
  technique: "linear-gradient(90deg, rgba(251,58,77,.08), rgba(255,252,234,0) 22%, rgba(49,57,251,.06) 100%) layered over #FFFCEA /* {colors.hero-cream} */"
  applied_to: ["{component.hero-section}"]
  visual_signature: "A barely visible red-to-blue atmospheric tint warms the poster field while keeping the surface flat."
```

---

## 14. Content Voice
<!-- SOURCE: manual -->

Arc's copy is calm but not corporate. "Meet Dia" and "a familiar design that weaves AI into everyday tasks" frame AI as a soft continuity story rather than a feature list. The product promise is emotional and practical at once: calmer internet, fewer distractions, familiar design, everyday tasks.

Voice rules:

- Prefer short launch phrases over dense feature claims.
- Use "familiar", "everyday", "calmer", and "personal" style language.
- Avoid enterprise AI terminology in the first viewport.
- Let product UI examples explain utility instead of adding statistics.

---

## 15. Drop-in CSS
<!-- SOURCE: manual -->

```css
:root {
  --arc-blue: #3139FB;
  --arc-deep-blue: #2404AA;
  --arc-dark-blue: #000354;
  --arc-red: #FB3A4D;
  --arc-cream: #FFFCEA;
  --arc-offwhite: #FFFCEC;
  --arc-ink: #000000;
  --arc-muted: #6F6F6F;
  --arc-hairline: #171717;
  --arc-focus: #96C4FF;

  --arc-font-display: "Marlin Soft SQ", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --arc-font-body: "InterVariable", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --arc-font-mono: "ABC Favorit Mono", "Space Mono", Menlo, monospace;

  --arc-radius-sm: 8px;
  --arc-radius-md: 16px;
  --arc-radius-pill: 25px;
  --arc-max: 960px;
}

body {
  margin: 0;
  background: var(--arc-cream);
  color: var(--arc-ink);
  font-family: var(--arc-font-body);
  font-weight: 400;
}

.arc-stage {
  background: var(--arc-blue);
  color: #FFFFFF;
}

.arc-hero {
  background:
    linear-gradient(90deg, rgba(251,58,77,.08), rgba(255,252,234,0) 22%, rgba(49,57,251,.06) 100%),
    var(--arc-cream);
  text-align: center;
  padding: 56px 24px 0;
}

.arc-hero h1 {
  margin: 0 auto 16px;
  max-width: 760px;
  font-family: var(--arc-font-display);
  font-size: clamp(36px, 5vw, 56px);
  line-height: .98;
  letter-spacing: -0.04em;
  font-weight: 700;
}

.arc-hero p {
  margin: 0 auto 32px;
  max-width: 620px;
  color: #6F6F6F;
  font-size: 20px;
  line-height: 1.5;
}

.arc-dia-cta {
  display: inline-flex;
  align-items: center;
  gap: 14px;
  min-height: 64px;
  padding: 8px 22px 8px 10px;
  border-radius: var(--arc-radius-pill);
  background: #171717;
  color: #FFFFFF;
  font-weight: 700;
  font-size: 22px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .25);
}

.arc-browser-frame {
  width: min(90vw, 1200px);
  margin: 56px auto 0;
  border-radius: var(--arc-radius-md);
  background: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, .08);
  box-shadow: 0 4px 11px rgba(0, 0, 0, .02), 0 1px 2px rgba(0, 0, 0, .03);
  overflow: hidden;
}
```

---

## 16. Tailwind Mapping
<!-- SOURCE: manual -->

```js
export default {
  theme: {
    extend: {
      colors: {
        arc: {
          blue: "#3139FB",
          deep: "#2404AA",
          dark: "#000354",
          red: "#FB3A4D",
          cream: "#FFFCEA",
          offwhite: "#FFFCEC",
          ink: "#000000",
          muted: "#6F6F6F",
          focus: "#96C4FF"
        }
      },
      fontFamily: {
        display: ["Marlin Soft SQ", "-apple-system", "BlinkMacSystemFont", "sans-serif"],
        body: ["InterVariable", "Inter", "-apple-system", "BlinkMacSystemFont", "sans-serif"],
        mono: ["ABC Favorit Mono", "Space Mono", "Menlo", "monospace"]
      },
      borderRadius: {
        arc: "16px",
        "arc-pill": "25px"
      },
      boxShadow: {
        "arc-soft": "0 4px 11px rgba(0,0,0,.02), 0 1px 2px rgba(0,0,0,.03)",
        "arc-cta": "0 2px 8px rgba(0,0,0,.25)"
      }
    }
  }
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

- Primary environmental blue: `#3139FB`
- Hero warm surface: `#FFFCEA`
- Brand off-white token: `#FFFCEC`
- Primary text: `#000000`
- Muted text: `#6F6F6F`
- CTA dark: `#171717`
- Brand red spark: `#FB3A4D`
- Focus outline: `#96C4FF`

### Prompt

Build an Arc-inspired editorial-product landing screen for a browser/AI product. Use a saturated `#3139FB` top stage band with white navigation, a scalloped or paper-cut transition into a warm `#FFFCEA` hero floor, and a centered soft display headline using a Marlin Soft SQ-like font. Put the primary CTA in a dark rounded launcher pill with an app-icon tile and arrow. Below the CTA, place a large white browser-frame product screenshot container with `16px` radius and subtle layered shadow, cropped low so it feels embedded into the page. Keep body copy calm and practical; do not use generic SaaS feature cards in the first viewport.

### Avoid

Do not make it a plain white SaaS hero. Do not replace the Arc blue with a violet gradient. Do not use Inter for the hero headline. Do not make the CTA a flat blue button. Do not show a generic dashboard card grid instead of a specific browser frame.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO

- Use `#3139FB` as a large stage/background color, especially above or below the hero.
- Use `#FFFCEA` or `#FFFCEC` as the warm hero floor instead of pure white.
- Keep the primary headline black `#000000` with a soft rounded display face.
- Use negative tracking on display type, around `-0.04em` for the largest headline.
- Make the Dia CTA dark (`#171717`) with white text `#FFFFFF`, icon tile, arrow, and shadow.
- Use white `#FFFFFF` browser chrome for the product frame, with `16px` radius and subtle shadow.
- Let red `#FB3A4D` remain a small brand spark rather than a dominant section color.
- Preserve the scalloped blue-to-cream divider or an equivalent handmade edge detail.

### DON'T

- 배경을 `#FFFFFF` 또는 `white`로만 두지 말 것 — 대신 hero floor는 `#FFFCEA` 또는 `#FFFCEC` 사용.
- primary brand를 `#667EEA`나 `#764BA2` 보라 그라디언트로 바꾸지 말 것 — 대신 `#3139FB` 사용.
- 본문 텍스트를 `#333333` 중심으로 흐리게 만들지 말 것 — 핵심 headline은 `#000000`, 보조 copy는 `#6F6F6F` 사용.
- CTA를 `#3139FB` 파란 버튼으로 만들지 말 것 — Dia primary CTA는 `#171717` 배경과 `#FFFFFF` 텍스트가 맞다.
- warm surface를 `#F8F8F8` 쿨 그레이로 대체하지 말 것 — Arc의 현재 hero는 `#FFFCEA` 계열이다.
- red accent를 `#FF0000` 원색 red로 쓰지 말 것 — 브랜드 spark는 `#FB3A4D`다.
- browser frame border를 `#000000` 두꺼운 stroke로 만들지 말 것 — soft hairline과 white chrome을 유지한다.
- body 전체를 `font-weight: 500`으로 밀지 말 것 — 기본은 `400`, 강조와 headline에만 `600/700`을 쓴다.

### 🚫 What This Site Doesn't Use

- No generic purple-blue SaaS gradient mesh.
- No symmetric "hero + three feature cards + CTA" above the fold.
- No sterile all-white product marketing page.
- No flat blue primary CTA competing with the blue stage band.
- No heavy black outlines around cards or screenshots.
- No dense dashboard UI outside the screenshot container.
- No emoji or playful sticker language in the product claim.
- No neutral single-font system; custom display typography is part of the brand.
- No large red sections; red remains logo/accent energy.
- No formal enterprise AI vocabulary in the first screen.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- Phase1 artifacts were reused from `insane-design/arc/`; no new live fetch was performed in this run because the requested reusable artifacts existed.
- The screenshot reflects a Dia-focused Arc homepage state captured on 2026-04-23. Arc may rotate homepage campaigns, so hero copy and imagery can drift.
- Exact font licensing and file loading details were inferred from CSS family names, not from font binary inspection.
- Touch target heights were not directly isolated by phase1 extraction; mobile behavior is inferred from breakpoints and screenshot structure.
- Motion behavior was not captured as video. Any motion guidance here is limited to visible/static CSS and layout affordances.
- Component coverage is first-viewport heavy. Deeper page sections may contain additional variants not visible in the provided screenshot summary.
- Some values such as CTA padding and nav height are visual/inferred measurements because generated CSS class names obscure semantic component ownership.
