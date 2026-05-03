---
schema_version: 3.2
slug: volvo
service_name: Volvo Cars Korea
site_url: https://www.volvocars.com/kr/
fetched_at: 2026-04-23T11:49:00+09:00
default_theme: light
brand_color: "#1F1F1F"
primary_font: "Volvo Novum"
font_weight_normal: 400
token_prefix: "--v"

bold_direction: Nordic Restraint
aesthetic_category: Industrial Minimalism
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: automotive
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Next.js page with Volvo design utility classes, responsive grids, CSS variables, and consistent component recipes; no public guidebook layer observed in this capture."

colors:
  ink-primary: "#000000"
  ink-soft: "#1F1F1F"
  surface-primary: "#FFFFFF"
  surface-secondary: "#FAFAFA"
  ornament: "#D8D8D8"
  accent-blue: "#3860BE"
  dark-surface: "#0B0F19"
  dark-ink: "#E5E7EB"
typography:
  display: "Volvo Novum SemiLight"
  body: "Volvo Novum"
  brand-wordmark: "Volvo Broad"
  ladder:
    - { token: statement, size: "var(--v-font-statement-1-size)", weight: 300, line_height: "var(--v-font-statement-1-lineheight)" }
    - { token: h1, size: "var(--v-font-heading-1-size)", weight: 500, line_height: "var(--v-font-heading-1-lineheight)" }
    - { token: h2, size: "var(--v-font-heading-2-size)", weight: 500, line_height: "var(--v-font-heading-2-lineheight)" }
    - { token: body, size: "16px", weight: 400, line_height: "var(--v-font-16-lineheight)" }
  weights_used: [300, 350, 400, 500, 600, 700]
  weights_absent: [800, 900]
components:
  button-filled: { bg: "#1F1F1F", text: "#FFFFFF", radius: "var(--v-radius-full)", padding: "approx 12px 24px" }
  discovery-card: { bg: "var(--v-color-background-secondary)", radius: "4px", media: "aspect-21/9 -> md:aspect-16/9" }
  site-nav-topbar: { height: "64px", z_index: 1000, bg: "#FFFFFF" }
---

# DESIGN.md - Volvo Cars Korea

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Volvo stages each model like a showroom hero on a Scandinavian editorial canvas — full-bleed automotive photography first, then a disciplined utility chassis where only the car, the road, and a few necessary decisions remain. The page does not try to sell with decorative color. It lets photography and the Volvo wordmark create the first emotional signal, then pulls the user into a utility system: black text, white surfaces, pale gray dividers, and square-edged cards.

The strongest visual move is the full-bleed automotive hero. In the captured page the cookie modal obscures part of it, but the underlying HTML shows a promotional hero for the EX90 with a dark gradient treatment, left-side copy, and a single filled CTA. The identity is not "bright EV tech"; it is safety, silence, and expensive calm. Black `#000000` (`{colors.ink-primary}`) and near-black `#1F1F1F` (`{colors.ink-soft}`) do the brand work that many automotive sites would hand to a saturated accent.

Volvo's system relies on named utility rhythm rather than ornamental layouts: `container-xl`, `grid`, `md:grid-cols-2`, `lg:grid-cols-4`, `gap-x-gutter`, `py-24`, `px-24`, `border-ornament`, `tap-area`. Cards are not expressive objects; they are calm gallery tiles, often with a chevron and one short paragraph — the showroom catalog laid flat, not a cinematic spectacle.

The type is the quiet luxury marker. `Volvo Novum` and `Volvo Novum SemiLight` carry most of the page, with `Volvo Broad` reserved for brand expression. The system uses multiple weights, but the page's public voice still feels light because large headings and hero titles are balanced by generous line-height, sparse copy, and a refusal to use loud chromatic accents.

The whole page reads like a Scandinavian dealership at dusk: the hero is the lit display car on a slowly rotating turntable, the editorial canvas is the polished concrete floor with masking-tape grid lines, and the discovery cards are the brochures laid out on a bleached-oak table beside the test-drive desk. The CTA behaves like the matte chrome key fob set on top of those brochures — small, weighty, and obvious without being loud. The single-color black masthead is the showroom's overhead beam — structural, never decorative. There is no second brand color because Volvo's idea of luxury is a quiet showroom with one engine running.

### Key Characteristics

- Full-bleed automotive photography first; UI chrome stays quiet around it.
- Monochrome brand language: `#000000`, `#1F1F1F`, `#FFFFFF`, and hairline gray dominate.
- Utility-class layout system with responsive breakpoints at `30rem`, `64rem`, and `100rem`.
- Cards are flat, rectangular, and informational, usually on secondary surfaces rather than floating shadows.
- Navigation is a restrained topbar with high z-index layering and slide/drawer behavior.
- CTA hierarchy is black filled primary, white/outline secondary, and link-inline tertiary.
- Motion is gentle: fade, translate, stagger, and scale, not playful bounce.
- Accent blue `#3860BE` appears as a functional link/focus accent, not as the visual brand core.
- Product and lifestyle images carry emotional color; components mostly avoid color.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Nordic Restraint
> **Aesthetic Category**: Industrial Minimalism
> **Signature Element**: 이 사이트는 **full-bleed safety photography with monochrome showroom UI**으로 기억된다.
> **Code Complexity**: high — responsive utility CSS, shadow-DOM navigation, image art direction, animated hero/card entrances, and drawer state layering are all present.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Volvo Cars Korea처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Volvo Novum", Arial, sans-serif;
  font-weight: 400;
  letter-spacing: 0;
}

/* 2. 배경 + 텍스트 */
:root {
  --volvo-bg: #FFFFFF;
  --volvo-bg-secondary: #FAFAFA;
  --volvo-fg: #000000;
  --volvo-border: #D8D8D8;
}
body {
  background: var(--volvo-bg);
  color: var(--volvo-fg);
}

/* 3. 브랜드 컬러 */
:root { --volvo-brand: #1F1F1F; }
.button-filled {
  background: var(--volvo-brand);
  color: #FFFFFF;
  border-radius: var(--v-radius-full);
}
```

**절대 하지 말아야 할 것 하나**: Volvo를 파란색 자동차 브랜드처럼 만들지 말 것. `#3860BE`는 링크/상태 보조색이고, 브랜드의 주된 표정은 `#000000`과 `#FFFFFF`의 조용한 대비다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.volvocars.com/kr/` |
| Fetched | 2026-04-23T11:49:00+09:00 |
| Extractor | reused existing phase1 capture; HTML + CSS + screenshot available |
| HTML size | 338055 bytes (Next.js / React flight stream / Contentstack-backed page) |
| CSS files | 28 files, 249784 bytes total |
| Phase1 JSON | `brand_candidates.json`, `resolved_tokens.json`, `typography.json`, `alias_layer.json` |
| Token prefix | `--v` for Volvo utility system; `--ot` tokens are cookie/footer preference surface |
| Method | CSS/HTML parsing plus screenshot review; no fresh fetch performed for this run |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js / React, with streamed `self.__next_f` payloads and Contentstack metadata.
- **Content source**: `contentstack-prod|live` for homepage and shared navigation/footer content.
- **Design system**: Volvo utility CSS using `--v-*` variables, responsive utility classes, and component-scoped CSS modules.
- **CSS architecture**:
  ```text
  --v-*                 Volvo design tokens and semantic utilities
  utility classes       container-xl, grid, px-24, py-24, text-secondary
  component modules     PromotionHero_*, discovery-card_*, sitenav__*
  --ot-*                OneTrust/cookie preference and footer-surface tokens
  ```
- **Class naming**: utility-first vocabulary plus generated CSS module suffixes.
- **Default theme**: light (`#FFFFFF` / `#000000`), with captured dark token alternatives for cookie/footer surfaces.
- **Font loading**: Volvo-owned web fonts declared in CSS; observed families include `Volvo Novum`, `Volvo Novum SemiLight`, and `Volvo Broad`.
- **Canonical anchor**: `https://www.volvocars.com/kr/`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Volvo Novum SemiLight` (brand font, proprietary)
- **Body font**: `Volvo Novum` (brand font, proprietary)
- **Brand wordmark / special display**: `Volvo Broad`
- **Fallback stack observed**: `"Volvo Novum SemiLight", "Arial Narrow", "Helvetica Neue", Arial, sans-serif`
- **Weight normal / bold**: `400` / `700`, with important mid-weight use at `500` and light display use at `300`

```css
:root {
  --volvo-font-family: "Volvo Novum", Arial, sans-serif;
  --volvo-font-family-display: "Volvo Novum SemiLight", "Arial Narrow", "Helvetica Neue", Arial, sans-serif;
  --volvo-font-family-brand: "Volvo Broad";
  --volvo-font-weight-normal: 400;
  --volvo-font-weight-emphasis: 500;
  --volvo-font-weight-bold: 700;
}
body {
  font-family: var(--volvo-font-family);
  font-weight: var(--volvo-font-weight-normal);
}
```

### Note on Font Substitutes

- **Volvo Novum SemiLight** is narrow, quiet, and premium. If unavailable, use **Arial Narrow** first, then **Helvetica Neue** at weight `300` or `350`.
- **Volvo Novum** can fall back to **Arial** only if line-height is kept slightly open. Do not replace it with Inter by default; Inter makes the page feel like SaaS instead of automotive.
- **Volvo Broad** should not be faked in body text. Reserve any wide fallback for the wordmark or tiny brand lockups only.
- Keep letter spacing at `0`; the site does not need aggressive negative tracking to feel premium.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `statement-1` | `var(--v-font-statement-1-size)` | `var(--v-font-statement-1-weight)` / observed `300` | `var(--v-font-statement-1-lineheight)` | `0` |
| `statement-2` | `var(--v-font-statement-2-size)` | `var(--v-font-statement-2-weight)` / observed `300-500` | `var(--v-font-statement-2-lineheight)` | `0` |
| `heading-1` | `var(--v-font-heading-1-size)` | `var(--v-font-heading-1-weight)` / observed `500` | `var(--v-font-heading-1-lineheight)` | `0` |
| `heading-2` | `var(--v-font-heading-2-size)` | `var(--v-font-heading-2-weight)` / observed `500` | `var(--v-font-heading-2-lineheight)` | `0` |
| `font-16` | `16px` / `var(--v-font-16-size)` | `400` | `var(--v-font-16-lineheight)` | `0` |
| `micro` | `.75em` to `.85em` observed | `400-500` | compact | `0` |

> ⚠️ Typography extractor returned no complete numeric scale table, but CSS and HTML expose tokenized Volvo font variables and frequent classes such as `heading-1`, `heading-2`, `font-16`, and `micro`.

### Principles

1. Display copy uses branded lightness first. The hero title can feel large without becoming heavy because `Volvo Novum SemiLight` and `300-500` weights keep the voice calm.
2. Body text is not tiny luxury text. `16px` appears as a recurring body token, supporting legibility for vehicle research and purchase tasks.
3. Weight contrast is broad but controlled. Captured CSS uses `300`, `350`, `400`, `500`, `600`, and `700`, but the homepage voice avoids black-weight display.
4. Letter spacing stays neutral. The premium feel comes from typeface choice and whitespace, not from heavy tracking tricks.
5. Korean copy must be allowed to breathe. Preserve line-height and avoid squeezing headings into single-line English-style compositions.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (monochrome anchor)

| Token | Hex |
|---|---|
| `{colors.ink-primary}` | `#000000` |
| `{colors.ink-soft}` | `#1F1F1F` |
| `--ot-btn-primary-hover` | `#3A3A3A` |
| `--ot-btn-primary-active` | `#4C4C4C` |

### 06-2. Dark Variant

| Token | Hex |
|---|---|
| `{colors.dark-surface}` | `#0B0F19` |
| dark elevated surface | `#111827` |
| dark text | `#E5E7EB` |
| dark hover | `#CBD5E1` |
| dark active | `#94A3B8` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| page | `#FFFFFF` | `#0B0F19` |
| secondary | `#FAFAFA` | `#111827` |
| divider | `#D8D8D8` | `#334155` |
| muted text | `#707070` | `#9CA3AF` |
| floor / image support | `#C7CDD7` | `#2E3644` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Functional blue | link/focus/support | `#3860BE` |
| Link blue variant | hover/inline | `#1C6BBA` |
| Dealer/consent green | OneTrust / consent UI | `#68B631` |
| Environmental tag green | tag color | `#168635` |
| Warning/energy scale | eco label sequence | `#F7E53C`, `#F4BC2C`, `#E47224`, `#C71024` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| foreground primary | `#000000` | main text, topbar text, primary outlines |
| foreground secondary | `#707070` | muted copy, secondary text |
| background primary | `#FFFFFF` | page and nav surface |
| background secondary | `#FAFAFA` | discovery cards and light modules |
| ornament primary | `#D8D8D8` | card/list dividers |
| accent blue | `#3860BE` | link/focus/action accent |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--ot-surface` | `#FFFFFF` | captured consent/footer surface |
| `--ot-text` | `#000000` | captured consent/footer text |
| `--ot-text-muted` | `#707070` | muted consent/footer text |
| `--ot-divider` | `#D8D8D8` | separator |
| `--ot-btn-primary-bg` | `#1F1F1F` | primary filled action |
| `--ot-btn-primary-text` | `#FFFFFF` | primary action text |
| `--ot-btn-secondary-bg` | `#FFFFFF` | secondary action background |
| `--ot-btn-secondary-border` | `#000000` | secondary action border |

### 06-7. Dominant Colors (actual CSS frequency)

| Hex | Frequency signal | Interpretation |
|---|---:|---|
| `#FFFFFF` / `#fff` | highest | primary surface and text on dark UI |
| `#D8D8D8` | high | ornament/divider system |
| `#000000` / `#000` | high | primary text and black action surfaces |
| `#3860BE` | high chromatic | functional blue, not brand core |
| `#68B631` | cookie/consent | OneTrust consent green; not Volvo UI brand |
| `#E5E7EB` | dark mode/action | dark-surface text and button state |

### Color Stories

**`{colors.ink-primary}` (`#000000`)** — Volvo's real UI brand color in this capture. It is used for primary text, outlines, and the core filled action model; do not replace it with a saturated automotive blue.

**`{colors.surface-primary}` (`#FFFFFF`)** — The showroom floor. Navigation, content sections, and most utility surfaces stay white so photography can own emotion and color.

**`{colors.ornament}` (`#D8D8D8`)** — The quiet structural line. Lists and touch rows use dividers instead of shadows, borders, or decorative cards.

**`{colors.accent-blue}` (`#3860BE`)** — Functional affordance. It can support links, focus, and small action states, but it should never flood hero sections or cards.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `px-8` / `py-8` | `.5rem` | compact links, nav rows |
| `px-16` / `py-16` | `1rem` | mobile gutters, card interior |
| `px-24` / `py-24` | `1.5rem` | list-row rhythm, hero mobile padding |
| `px-32` / `py-32` | `2rem` | section and card breathing room |
| `px-48` | `3rem` | desktop hero/nav horizontal inset |
| `gap-8` | `.5rem` | icon/text and mobile CTA gaps |
| `gap-16` | `1rem` | responsive CTA and card gaps |
| `gap-32` | `2rem` | module rhythm and media card separation |
| `--ot-footer-space` | `160px` | large footer breathing room |

**주요 alias**:
- `gap-x-gutter` -> grid column gutter for responsive card sections.
- `container-xl` -> large constrained content band.
- `--v-space-pagemargin` -> page margin in the grid debug formula.

### Whitespace Philosophy

Volvo uses whitespace like a showroom uses silence. The page is not empty; it is measured. A hero can be image-heavy, then the shopping tools below snap into a compact `lg:grid-cols-4` utility grid. That contrast is central: emotional image first, practical decisions immediately after.

The spacing system is strongly modular. The recurring `8 / 16 / 24 / 32 / 48` ladder makes sections feel engineered rather than editorially improvised. Avoid one-off gaps like `27px`; the Volvo feel comes from staying on the mechanical rhythm.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `--v-radius-sm` fallback | `4px` | focus rings and small card affordances |
| `--v-shape-default` | tokenized | images, tooltips, modal panels |
| `--v-radius-full` | tokenized | circular auth/icon buttons and pill-like actions |
| explicit small radius | `2px`, `3px`, `4px` | form and preference UI |
| explicit medium radius | `10px`, `20px` | overlays and dialog surfaces |
| circular | `50%` | icon buttons and avatars |

Volvo's homepage cards are generally more rectangular than pill-like. Reserve large radius for controls that are explicitly buttons or circular utilities.

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| none | `box-shadow: none` by default | most cards and content rows |
| focus halo | `0 0 0 var(--v-space-4) ...` | checkbox/radio interaction states |
| consent/footer shadow | `0px 0px 12px 2px rgb(199 197 199 / 100%)` | captured OneTrust surface |
| dark overlay shadow | `0px 0px 12px 2px rgba(0, 0, 0, 0.6)` | dark preference layer |

Volvo's chrome does not float. Use dividers and surface changes before elevation.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| `animation-gentle` | class-based | hero and discovery card entrance |
| `animation-translate` | translate reveal | content entrance from `-12px` or `-24px` |
| `animation-stagger-1/4` | staggered children | hero text and tool cards |
| drawer transition | `transform .3s ease-in-out` | site navigation slider |
| menu transition | `max-height .3s` | navigation menu expansion |
| car/image hover | scale around `1.05` / `1.08` | gallery and image cards |
| `--v-transition-easing-regular` | `cubic-bezier(0.45, 0, 0.4, 1)` | regular easing |
| `--v-transition-easing-entrance` | `cubic-bezier(0, 0, 0.1, 1)` | entrance easing |
| `--v-transition-easing-exit` | `cubic-bezier(0.9, 0, 1, 1)` | exit easing |

Motion should feel like a sliding panel in a car interior: precise, damped, and short.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: debug grid formula caps at `81rem`; large page formula references up to `160rem` with page margins.
- **Grid type**: CSS Grid and Flexbox, with utility classes driving most composition.
- **Column count**: shopping tools use `md:grid-cols-2` and `lg:grid-cols-4`; discovery media uses `md:grid-cols-2` and `lg:grid-cols-3`.
- **Gutter**: `gap-x-gutter`, `gap-y-s`, and fixed gaps from `8px` to `64px`.

### Hero

- **Pattern Summary**: `full-bleed image/video + dark gradient overlay + left aligned copy + single black/white CTA`.
- Layout: responsive hero module; copy sits in a half-width block at medium and above.
- Background: automotive image/video with dark gradient classes (`PromotionHero_md__gradient-dark`, `PromotionHero_md__gradient-left`).
- **Background Treatment**: image overlay with left-side dark gradient; captured screenshot shows a dark forest/river scene behind the cookie modal.
- H1: `heading-1`, escalating to statement-scale tokens in car launch contexts.
- Max-width: hero copy uses `md:max-w-1/2` and desktop `lg:px-48`.

### Section Rhythm

```css
section {
  padding-block: var(--top-inner-spacing) var(--bottom-inner-spacing);
  margin-block: var(--top-outer-spacing) var(--bottom-outer-spacing);
}
.container-xl {
  max-width: large Volvo content container;
}
```

### Card Patterns

- **Card background**: `var(--v-color-background-secondary)` or `#FAFAFA`-like secondary surface.
- **Card border**: usually absent on discovery cards; list links use `border-b` / `border-ornament`.
- **Card radius**: small (`4px`) or tokenized shape default; not a soft SaaS card.
- **Card padding**: `p-16`, `py-24`, `px-8`, depending on card/list mode.
- **Card shadow**: none; image and surface contrast do the separation.
- **Hover**: clickable cards may scale images or adjust text color to accent blue.

### Navigation Structure

- **Type**: horizontal topbar with menu/drawer and shadow-DOM embedded site navigation.
- **Position**: controlled by variables for sticky/hide-on-scroll; wrapper has high z-index.
- **Height**: `--sitenav-topbar-height` observed as `48px` and resolved phase token `64px`.
- **Background**: `#FFFFFF` in light mode; data-theme `centenary`.
- **Border**: subtle bottom separators and ornament lines; no decorative heavy border.
- **Layering**: `--z-index-topbar: 1000`, `--z-index-sidenav: 1001`, profile/backdrop above that.

### Content Width

- **Prose max-width**: component-dependent, with examples around `596px`, `600px`, and `814px`.
- **Container max-width**: debug formula uses `81rem` and page-margin constrained width.
- **Sidebar width**: drawer width captured at `456px`, nav slider max around `400px` at medium sizes.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `< 30rem` / `max-width:29.99rem` | single-column card stacks, compact topbar, mobile menu |
| Tablet | `min-width:30rem` | two-column grids, larger type tokens, nav slider constraints |
| Desktop | `min-width:64rem` | hero half-width copy, 3-4 column content grids, richer hover states |
| Large | `min-width:100rem` | largest CSS bundle and statement-scale typography |

### Touch Targets

- **Minimum tap size**: `tap-area` is widely applied to cards and nav links.
- **Button height (mobile)**: captured controls use comfortable vertical padding rather than tiny text links.
- **Input height (mobile)**: search field and consent controls use full-width tap rows.

### Collapsing Strategy

- **Navigation**: menu/drawer slider with `transform .3s ease-in-out`; desktop and mobile toggles are separate.
- **Grid columns**: `1 -> 2 -> 3/4` depending on content type.
- **Sidebar**: drawer width constrained around `400-456px`; full-screen-ish behavior on smaller screens.
- **Hero layout**: mobile stacks text and CTA vertically; medium pushes content into a half-width overlay.

### Image Behavior

- **Strategy**: responsive `picture` sources with AVIF/JPG assets and density/width parameters.
- **Max-width**: images generally `w-full`, `h-full`.
- **Aspect ratio handling**: `aspect-21/9`, `md:aspect-16/9`, `aspect-3/2`, `object-cover`, and `object-contain` are all observed.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**`.button-filled`** — primary action.

```html
<a class="button-filled" href="/buy/purchase/ex90-visit-the-showroom-campaign">
  상담 신청하기
</a>
```

| Property | Value |
|---|---|
| Background | `#1F1F1F` or `#000000` family |
| Text | `#FFFFFF` |
| Radius | `var(--v-radius-full)` for pill actions |
| Typography | `Volvo Novum`, medium weight |
| Hover | darkens toward `#3A3A3A` in captured action tokens |
| Active | darkens toward `#4C4C4C` in captured action tokens |

**`.link-inline`** — quiet text action.

```html
<a class="link-inline" href="/kr/l/volvo-brochure/">자세히 보기</a>
```

Use this inside cards where the card itself is informational and the action is secondary.

### Badges

No homepage-first badge system was strongly surfaced. Energy/environment tags exist in CSS as a colored scale (`#168635`, `#76AB32`, `#C7CD2B`, `#F7E53C`, `#F4BC2C`, `#E47224`, `#C71024`) but should not be generalized into decorative marketing badges.

### Cards & Containers

**Discovery card** — repeated utility card for shopping tools and content entry points.

```html
<a class="link-plain w-full tap-area discovery-card_discovery_card__3E5JV discovery-card_clickable__sDfS3">
  <div slot="main">
    <div class="flex justify-between items-start gap-4">
      <p class="font-medium">나만의 볼보</p>
    </div>
    <p class="text-secondary mt-16 text-start">모델을 선택하고 원하는 스타일로 나만의 볼보를 만들어 보십시오.</p>
  </div>
</a>
```

| Property | Value |
|---|---|
| Surface | `var(--v-color-background-secondary)` |
| Layout | full-width tap area, flex content |
| Media | optional; `aspect-21/9` -> `md:aspect-16/9` |
| Border | none on card body; section/list separators use `border-ornament` |
| Shadow | none |
| Hover | clickable affordance via link and occasional image scale |

### Navigation

**Site topbar / menu drawer** — embedded navigation.

```html
<div id="site-navigation">
  <site-navigation></site-navigation>
</div>
```

| Property | Value |
|---|---|
| Topbar height | `48px` to `64px` depending on resolved context |
| Z-index | `1000+` |
| Slider transition | `transform .3s ease-in-out` |
| Menu max height | `calc(100vh - var(--v-space-64) - var(--sitenav-topbar-height))` |
| Logo | Volvo wordmark, quiet monochrome |

### Inputs & Forms

Observed form surfaces are mostly search, consent, and controls.

| State | Treatment |
|---|---|
| Default | white surface, black text, subtle bottom border |
| Focus | `outline: 2px solid var(--v-color-foreground-primary)` or stronger border-bottom |
| Hover | black border opacity increases |
| Disabled | tertiary/muted foreground |
| Error | feedback red foreground and subtle red state surface |

### Hero Section

```html
<section data-component="promotionalBanner">
  <div class="PromotionHero_md__gradient-dark__cZhIv PromotionHero_md__gradient-left__BLkIW">
    <div class="md:max-w-1/2 lg:px-48 PromotionHero_gradient-dark__Ihl1o">
      <p>Volvo 역사상 가장 안전한 자동차</p>
      <h1 class="heading-1 mt-16">완전히 새로운 볼보 EX90을 만나보세요.</h1>
      <a class="button-filled">상담 신청하기</a>
    </div>
  </div>
</section>
```

The hero is the emotional engine: a dark, photographic field with sparse copy and one decisive action.

### 13-2. Named Variants

**`button-filled`**
- black/near-black filled CTA, white text, pill/full radius.
- Use for "상담 신청하기", purchase, test-drive, or primary conversion.

**`link-inline`**
- text-first action inside utility cards.
- Use when the containing card already provides the tap surface.

**`discovery-card-no-media`**
- secondary-surface card with heading, short body, chevron/action affordance.
- Used for shopping tools such as test drive, showroom, configurator, newsletter.

**`discovery-card-media`**
- image-led card with `aspect-21/9` and responsive `md:aspect-16/9`.
- Used for sustainability, electrification, safety, service storytelling.

**`nav-drawer-slider`**
- high z-index drawer with `transform .3s ease-in-out`.
- Use for menu, car navigation, search, profile overlays.

### 13-3. Signature Micro-Specs

#### gradient-safety-hero

```yaml
gradient-safety-hero:
  description: "Full-bleed safety/vehicle photography is gated by a left-side dark gradient that hosts the copy block."
  technique: "PromotionHero_md__gradient-dark + PromotionHero_md__gradient-left utilities; half-width copy column; white-on-dark readability without overlay panels."
  applied_to: ["{component.hero-section}", "EX90 campaign hero", "model launch banners"]
  visual_signature: "a quiet cinematic field — the vehicle story feels Scandinavian-serious, never showroom-flashy."
  intent: "automotive trust must be earned through restraint; gradients carry copy so the photograph is never cropped or boxed."
```

#### ornament-border-list

```yaml
ornament-border-list:
  description: "List links become structure through hairline dividers, not card chrome."
  technique: "border-b border-ornament py-24 tap-area px-8; no card shadow; full-width row hit area."
  applied_to: ["{component.navigation-panel}", "service link list", "showroom locator list"]
  visual_signature: "engineered rows that read like spec sheets — not decorative cards on a marketing page."
  intent: "Volvo's brand is engineering precision; cards would soften that with consumer-app warmth."
```

#### responsive-art-directed-media

```yaml
responsive-art-directed-media:
  description: "Cards use exact aspect utilities instead of arbitrary crops, so every image is editorial-framed."
  technique: "aspect-21/9 (cinema) and md:aspect-16/9 (broadcast); object-cover; responsive `picture` sources per breakpoint."
  applied_to: ["{component.discovery-card}", "secondary hero card", "model line tile"]
  visual_signature: "every image looks like an automotive press still — never a stretched stock photo."
  intent: "automotive photography is shot once and licensed expensively; locking the crop preserves the art-direction at every viewport."
```

#### damped-drawer-motion

```yaml
damped-drawer-motion:
  description: "Panels slide with short, restrained transitions — never a bounce."
  technique: "transform .3s ease-in-out, max-height .3s linear, high z-index layer tokens, no spring or overshoot."
  applied_to: ["{component.site-navigation}", "menu drawer", "search panel", "cars menu"]
  visual_signature: "precision movement — like the soft-close of a luxury car door."
  intent: "the brand promise is calm safety; bouncy motion would imply consumer-electronics personality."
```

#### ornament-token-as-floor

```yaml
ornament-token-as-floor:
  description: "Volvo refuses both pure white and grey — the page floor is a defined ornament family."
  technique: "background `#FAFAFA`, divider `#E5E2DA` (warm ornament token), accent ink `#141414`; never `#FFFFFF` body."
  applied_to: ["{component.page-surface}", "card divider", "section break"]
  visual_signature: "a warm matte floor — closer to showroom paper than to digital chrome."
  intent: "Scandinavian premium reads warm; pure white would feel medical, pure grey would feel utility."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Safety and product-first, direct sentence case | "완전히 새로운 볼보 EX90을 만나보세요." |
| Eyebrow | Brand promise before product | "Volvo 역사상 가장 안전한 자동차" |
| Primary CTA | Short noun/action phrase | "상담 신청하기" |
| Utility card title | Task-oriented | "시승 신청하기", "전시장 찾기", "나만의 볼보" |
| Body copy | Calm benefits, no hype punctuation | "모델을 선택하고 원하는 스타일로 나만의 볼보를 만들어 보십시오." |
| Tone | premium, safe, restrained, service-oriented |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Volvo Cars Korea - copy into your root stylesheet */
:root {
  /* Fonts */
  --volvo-font-family: "Volvo Novum", Arial, sans-serif;
  --volvo-font-family-display: "Volvo Novum SemiLight", "Arial Narrow", "Helvetica Neue", Arial, sans-serif;
  --volvo-font-family-brand: "Volvo Broad";
  --volvo-font-weight-normal: 400;
  --volvo-font-weight-medium: 500;
  --volvo-font-weight-light: 300;
  --volvo-font-weight-bold: 700;

  /* Core colors */
  --volvo-ink: #000000;
  --volvo-ink-soft: #1F1F1F;
  --volvo-surface: #FFFFFF;
  --volvo-surface-secondary: #FAFAFA;
  --volvo-text-muted: #707070;
  --volvo-ornament: #D8D8D8;
  --volvo-accent-blue: #3860BE;

  /* Dark support */
  --volvo-dark-surface: #0B0F19;
  --volvo-dark-elevated: #111827;
  --volvo-dark-text: #E5E7EB;

  /* Spacing */
  --volvo-space-8: .5rem;
  --volvo-space-16: 1rem;
  --volvo-space-24: 1.5rem;
  --volvo-space-32: 2rem;
  --volvo-space-48: 3rem;

  /* Shape */
  --volvo-radius-sm: 4px;
  --volvo-radius-full: 999px;

  /* Motion */
  --volvo-ease-regular: cubic-bezier(0.45, 0, 0.4, 1);
  --volvo-ease-entrance: cubic-bezier(0, 0, 0.1, 1);
  --volvo-ease-exit: cubic-bezier(0.9, 0, 1, 1);
}

.volvo-button-filled {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 12px 24px;
  border-radius: var(--volvo-radius-full);
  background: var(--volvo-ink-soft);
  color: var(--volvo-surface);
  font-family: var(--volvo-font-family);
  font-weight: var(--volvo-font-weight-medium);
  text-decoration: none;
}

.volvo-discovery-card {
  display: flex;
  flex-direction: column;
  gap: var(--volvo-space-16);
  min-height: 100%;
  padding: var(--volvo-space-16);
  background: var(--volvo-surface-secondary);
  color: var(--volvo-ink);
  border: 0;
  border-radius: var(--volvo-radius-sm);
  box-shadow: none;
}

.volvo-ornament-row {
  display: flex;
  align-items: center;
  min-height: 56px;
  padding: var(--volvo-space-24) var(--volvo-space-8);
  border-bottom: 1px solid var(--volvo-ornament);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js - Volvo-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        volvo: {
          ink: '#000000',
          soft: '#1F1F1F',
          surface: '#FFFFFF',
          secondary: '#FAFAFA',
          muted: '#707070',
          ornament: '#D8D8D8',
          blue: '#3860BE',
          dark: '#0B0F19',
        },
      },
      fontFamily: {
        sans: ['Volvo Novum', 'Arial', 'sans-serif'],
        display: ['Volvo Novum SemiLight', 'Arial Narrow', 'Helvetica Neue', 'Arial', 'sans-serif'],
      },
      borderRadius: {
        volvo: '4px',
        full: '999px',
      },
      transitionTimingFunction: {
        'volvo-regular': 'cubic-bezier(0.45, 0, 0.4, 1)',
        'volvo-in': 'cubic-bezier(0, 0, 0.1, 1)',
        'volvo-out': 'cubic-bezier(0.9, 0, 1, 1)',
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
| Brand primary | `{colors.ink-soft}` | `#1F1F1F` |
| Background | `{colors.surface-primary}` | `#FFFFFF` |
| Secondary surface | `{colors.surface-secondary}` | `#FAFAFA` |
| Text primary | `{colors.ink-primary}` | `#000000` |
| Text muted | `muted` | `#707070` |
| Border | `{colors.ornament}` | `#D8D8D8` |
| Functional accent | `{colors.accent-blue}` | `#3860BE` |
| Dark surface | `{colors.dark-surface}` | `#0B0F19` |

### Example Component Prompts

#### Hero Section

```text
Volvo Cars Korea 스타일 히어로 섹션을 만들어줘.
- 배경: full-bleed automotive photography with a left dark gradient overlay
- H1: Volvo Novum SemiLight, heading-1/statement scale, weight 300-500, tracking 0
- Eyebrow: small body copy above H1, white on dark image
- CTA: black/near-black filled button #1F1F1F with #FFFFFF text, pill radius
- Layout: mobile stacked; desktop copy block at max 50% width with lg:px-48
- Motion: gentle fade + translate from -12px, staggered children
```

#### Discovery Card

```text
Volvo 스타일 discovery card를 만들어줘.
- 배경: #FAFAFA or var(--v-color-background-secondary)
- border: none; shadow: none; radius: 4px
- padding: 16px; gap: 16px
- heading: Volvo Novum, 16px, weight 500, #000000
- body: 16px, #707070, relaxed line-height
- affordance: small chevron icon aligned top-right
```

#### Navigation

```text
Volvo 스타일 상단 네비게이션을 만들어줘.
- 높이: 48-64px
- 배경: #FFFFFF
- 로고: left, monochrome Volvo wordmark
- 링크: #000000 / muted #707070, no decorative underline
- menu drawer: z-index 1001+, transform .3s ease-in-out
- row links: py-24, px-8, border-bottom 1px solid #D8D8D8
```

#### Media Card

```text
Volvo 스타일 이미지 카드 섹션을 만들어줘.
- grid: mobile 1 col, md 2 cols, lg 3 cols
- image: aspect-21/9 on mobile, md:aspect-16/9, object-cover
- surface: #FAFAFA text panel below image
- hover: optional image scale 1.05 only; no colored glow
```

### Iteration Guide

- **색상 변경 시**: saturated brand palette를 만들지 말고 `#000000`, `#1F1F1F`, `#FFFFFF`, `#D8D8D8`를 먼저 조합한다.
- **파란색 사용 시**: `#3860BE`는 링크/상태/보조 action에만 둔다.
- **폰트 변경 시**: Inter보다 Arial/Helvetica 계열 fallback이 Volvo Novum의 자동차 브랜드 톤에 가깝다.
- **카드 추가 시**: shadow를 넣기 전에 `#FAFAFA` surface와 `#D8D8D8` divider로 해결한다.
- **모션 추가 시**: `transform .3s ease-in-out`과 gentle fade/translate만 사용한다.
- **이미지 사용 시**: actual vehicle/lifestyle photography를 핵심 시각 자산으로 둔다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use full-bleed vehicle or safety photography as the emotional lead.
- Keep the UI monochrome-first: `#000000`, `#1F1F1F`, `#FFFFFF`, `#FAFAFA`, `#D8D8D8`.
- Use `Volvo Novum` / `Volvo Novum SemiLight` or narrow Helvetica/Arial fallbacks.
- Build practical modules with responsive grids: `1 -> 2 -> 3/4` columns.
- Use dividers and surface shifts before shadows.
- Keep CTA count low in the hero; one primary action is enough.
- Use gentle translate/fade motion, not energetic bounce.

### ❌ DON'T

- 배경을 `#F5F5F5` 또는 generic warm gray로 두지 말 것 — 기본 floor는 `#FFFFFF`, 보조 surface는 `#FAFAFA` 사용.
- 텍스트를 `#141414` 같은 임의 near-black으로 통일하지 말 것 — primary text는 `#000000`, filled CTA는 `#1F1F1F` 사용.
- 브랜드 컬러를 `#3860BE`로 잡지 말 것 — `#3860BE`는 functional accent이고 primary brand anchor는 `#1F1F1F` / `#000000`이다.
- border를 `#E5E7EB`로 무조건 바꾸지 말 것 — light surface divider는 `#D8D8D8`가 더 가까운 ornament다.
- dark section 텍스트를 `#FFFFFF`만 쓰지 말 것 — captured dark UI text uses `#E5E7EB` for softer contrast.
- CTA를 square `border-radius: 0`으로 만들지 말 것 — primary actions should use pill/full radius, while cards stay around `4px`.
- cards에 heavy shadow를 넣지 말 것 — Volvo cards are flat, with surface contrast and image framing.
- hero에 purple/blue gradient를 넣지 말 것 — dark image overlay is the signature, not synthetic gradient branding.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No second chromatic brand color** — functional blue exists, but the brand system does not depend on a colorful palette.
- **No playful gradient identity** — gradients are photographic readability overlays, not decorative backgrounds.
- **No heavy card elevation** — the homepage is mostly flat surfaces, dividers, and image crops.
- **No rounded SaaS softness** — cards stay restrained; large radius belongs to controls or circular utilities.
- **No dense marketing icon grid** — content cards use text, chevrons, and photography rather than decorative icon packs.
- **No blackletter luxury drama** — brand type is proprietary and quiet, not fashion-editorial excess.
- **No cluttered CTA stacks** — hero conversion stays singular and controlled.
- **No arbitrary image crops** — aspect utilities and responsive picture sources keep media disciplined.
- **No emoji or casual expressive copy** — voice stays premium, direct, and service-oriented.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Cookie overlay in screenshot** — the available `hero-cropped.png` is partially blocked by the cookie preference modal, so hero visual interpretation also uses HTML structure and CSS class evidence.
- **No fresh network fetch in this run** — phase1 assets from April 23, 2026 were reused as instructed. Live Volvo page details may have changed after that capture.
- **Typography numeric scale incomplete** — `typography.json` returned no full `scale` entries; font token names and observed declarations were used instead of inventing exact pixel values.
- **Main Volvo token terminals partially unresolved** — CSS references many `--v-color-*` and `--v-font-*` variables, but not every terminal value was present in the captured CSS files. Values in this document use observed hex and resolved `--ot` examples where terminal values were available.
- **Cookie/OneTrust colors filtered** — green values such as `#68B631` appear frequently but belong to consent UI, not Volvo brand UI.
- **Sub-flows not visited** — configurator, checkout, login, forms, error validation, and service booking screens were not interacted with.
- **Motion logic not fully executed** — CSS transition/easing classes were inspected, but JS-triggered scroll animations and IntersectionObserver timing were not replayed.
- **Responsive behavior inferred from CSS** — mobile/tablet/desktop breakpoints are based on media queries and classes, not new viewport screenshots in this run.
- **Dark mode mapping incomplete** — dark tokens were captured for certain surfaces, but this homepage primarily presents as a light site.
