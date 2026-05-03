---
schema_version: 3.2
slug: raycast
service_name: Raycast
site_url: https://www.raycast.com
fetched_at: 2026-04-20T20:00:00+09:00
default_theme: dark
brand_color: "#FF6363"
primary_font: Inter
font_weight_normal: 400
token_prefix: ray

bold_direction: Command Noir
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Next.js marketing surface with real CSS tokens, component-scoped modules, and a reusable dark token ladder, but not a public designer-facing system."

colors:
  brand-red: "#FF6363"
  surface-black: "#07080A"
  surface-panel: "#111214"
  text-primary: "#FFFFFF"
  text-muted: "#9C9C9D"
  hairline: "#2F3031"
  accent-blue: "#56C2FF"
  success: "#59D499"
  error: "#FF6363"
typography:
  display: "Inter"
  body: "Inter"
  mono: "JetBrains Mono"
  ladder:
    - { token: hero, size: "64px", weight: 600, tracking: "-0.02em" }
    - { token: h2, size: "48px", weight: 600, tracking: "-0.018em" }
    - { token: section-title, size: "32px", weight: 600, tracking: "-0.01em" }
    - { token: body, size: "16px", weight: 400, tracking: "0" }
    - { token: keyboard-label, size: "12px", weight: 600, tracking: "0" }
  weights_used: [100, 300, 400, 500, 550, 600, 650, 700, 900]
  weights_absent: [200, 800]
components:
  button-download: { bg: "#FFFFFF", fg: "#0D0D0D", radius: "12px", padding: "10px 16px" }
  button-primary-red: { bg: "#FF6363", fg: "#FFFFFF", radius: "12px", padding: "12px 40px" }
  keyboard-key: { bg: "#111214", fg: "#FFFFFF", radius: "6px", border: "1px solid #2F3031" }
  dark-card: { bg: "#111214", fg: "#FFFFFF", radius: "12px", border: "1px solid #2F3031" }
---

# DESIGN.md — Raycast

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Raycast reads like a terminal specification photographed in near darkness — not a generic developer dark mode but a command console where the absence of light is the product promise. The page uses darkness as the stage for speed. The base is almost black, with `#07080A` (`{colors.surface-black}`) and `#111214` (`{colors.surface-panel}`) doing the structural work, while white type lands sharply against a surface that never becomes pure monochrome: the hero injects red, cyan, and pale glow into diagonal beams.

The memorable object is the shortcut beam: diagonal, blurred, high-energy strokes behind the headline. This gives the page motion before any animation is considered. The product promise is "shortcut," and the visual language makes it literal: fast diagonal traversal, command-key density, and compressed utility surfaces. The page feels like a launcher appearing above the operating system — the kind of overlay that fires for one decisive keystroke and then gets out of the way. It is a parchment of muscle memory, not a canvas of exploration.

Color is controlled, not democratic. `#FF6363` (`{colors.brand-red}`) is the brand anchor and error/action family, while `#56C2FF` (`{colors.accent-blue}`) appears as a supporting electric edge — flashes against black, like terminal heat caught on glass. There is no second brand color competing for ownership; blue, purple, and green are state or glow actors, never co-leads. Most of the UI is neutral, with muted type around `#9C9C9D` (`{colors.text-muted}`) and low-contrast borders around `#2F3031` (`{colors.hairline}`).

Typography is pragmatic and Mac-native in posture. Inter carries most UI text, SF Pro appears in product-adjacent areas, and JetBrains Mono / Geist Mono support command and developer surfaces. Weight `500` is the workhorse — controls and labels have the editorial density of engraved labels on a black instrument panel: small, exact, designed to be read at speed. Raycast's negative identity matters: no beige warmth, no pastel softness, no large marketing canvas, no rounded-card confetti. The page is a midnight command palette scaled to marketing size — the background is the OS void, the CTA is a single Mac-native affordance, and the diagonal beam is the shortcut blueprint burning across it.

조금 더 풀면, Raycast 홈은 **밤에 불 꺼진 실험실 안에 펼쳐 놓은 한 장의 blueprint와 작업대 위 공구함**처럼 작동한다. 검정 페이지 floor는 실험실 작업대 표면이고, 대각선 hero beam은 blueprint 위에 그어진 단축경로 — 단 하나의 단축키가 회로처럼 도면을 가로지른다. keyboard UI 행은 공구함 안에 가지런히 박힌 도구들 — 각 키캡은 라벨링된 부속 도구다. 빨간 `#FF6363`은 시연용 작업 라벨, 흰 download CTA는 실험실 입구의 단 하나의 스위치 손잡이, ExtensionCard 그리드는 blueprint 모서리에 부착된 부속 모듈 카탈로그다. 두 번째 brand color가 없는 이유는, 실험실 도구함 위에 잉크가 둘이면 단축경로가 흐려지기 때문이다.

### Key Characteristics

- Dark-first marketing surface: page floor is `#07080A`, not white with dark cards.
- Red command accent: `#FF6363` is the dominant branded chroma, used for action/error energy.
- Diagonal hero beam: blurred red/cyan/white streaks behind centered hero copy.
- Keyboard UI vocabulary: command keys, action rows, shortcut labels, and mono type carry product semantics.
- Dense utility rhythm: frequent `8px`, `12px`, `16px`, and `24px` gaps over large decorative spacing.
- Rounded but not bubbly: common radii are `6px`, `8px`, and `12px`; only pills/icons go extreme.
- Component-scoped CSS Modules: many patterns are per-section, not a single universal component library.
- White download CTA: the top nav primary action inverts the page with white-on-black contrast.
- Multiple mono stacks: JetBrains Mono and Geist Mono reinforce developer/command contexts.
- Accent color is a flare, not a theme wash: blue/purple/cyan appear sparingly around glow and technical surfaces.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Command Noir
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **diagonal command-beam hero and keyboard-native product chrome**으로 기억된다.
> **Code Complexity**: high — component CSS modules, dense responsive rules, conic/radial glow treatments, and keyboard/product UI states require more than static token replacement.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Raycast처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Inter", "Inter Fallback", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #07080A; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #FF6363; }
```

**절대 하지 말아야 할 것 하나**: Raycast를 밝은 흰색 SaaS 페이지로 만들지 말 것. 기본 바닥은 `#07080A`이고 CTA/텍스트/키보드 UI가 어둠 위에서 떠야 한다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.raycast.com` |
| Fetched | 2026-04-20T20:00:00+09:00 |
| Extractor | cached phase1 reuse: HTML + CSS + screenshot |
| HTML size | 368051 bytes (Next.js static/SSR marketing surface) |
| CSS files | 12 external files, total 426909 chars |
| Token prefix | `ray` (derived; actual CSS uses mixed tokens such as `--grey-*`, `--spacing-*`, `--rounding-*`) |
| Method | CSS custom properties, frequency extraction, screenshot observation, and HTML structure review |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js marketing build (`/_next/static` assets detected)
- **Design system**: Raycast web tokens — mixed global primitives plus CSS-module component contracts
- **CSS architecture**:
  ```css
  core      (--grey-*, --Base-*, --spacing-*, --rounding-*) raw primitives
  semantic  (--color-bg-*, --color-fg-*, --color-border)   page semantics
  action    (--button-background, --color-button-bg)        control semantics
  component (.Hero*, .Keyboard*, .ExtensionCard*)           section-scoped modules
  ```
- **Class naming**: CSS Modules with hashed suffixes, e.g. `Keyboard_key__QsvDd`, `ExtensionCard_card__g21uG`
- **Default theme**: dark (`#07080A` / `--grey-900`)
- **Font loading**: bundled web fonts and fallbacks: Inter, Inter Fallback, JetBrains Mono, JetBrains Mono Fallback, Geist Mono, SF Pro stacks
- **Canonical anchor**: hero screenshot shows a dark nav shell, centered headline, diagonal red/cyan command beam, and white Mac download CTA.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Inter` (open source; loaded with `Inter Fallback`)
- **Body font**: `Inter`, with SF Pro stacks in product-like UI areas
- **Code font**: `JetBrains Mono`, `Geist Mono`, and SF Mono fallbacks
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --ray-font-family:       "Inter", "Inter Fallback", sans-serif;
  --ray-font-family-code:  "JetBrains Mono", "JetBrains Mono Fallback", Menlo, Monaco, Courier, monospace;
  --ray-font-weight-normal: 400;
  --ray-font-weight-bold:   600;
}
body {
  font-family: var(--ray-font-family);
  font-weight: var(--ray-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Inter** — direct open-source substitute is already the real primary. Keep `font-weight: 500` available because Raycast uses it heavily for controls, labels, and buttons.
- **SF Pro Text / SF Pro** — on non-Apple platforms, substitute Inter at the same optical size, but reduce display letter-spacing by roughly `-0.01em` to preserve the compact Apple-like headline feel.
- **JetBrains Mono / Geist Mono** — if Geist Mono is unavailable, use JetBrains Mono for all keyboard and command snippets; avoid generic `monospace` alone because the command UI loses Raycast's dense terminal polish.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `hero-title` | `64px` desktop observed/estimated | `600` | `1.05` | `-0.02em` |
| `section-title` | `48px` | `600` | `1.08` | `-0.018em` |
| `feature-title` | `32px` | `600` | `1.15` | `-0.01em` |
| `body` | `16px` | `400` | `1.5` | `0` |
| `nav-link` | `14px` | `400` | `1` | `0` |
| `keyboard-label` | `12px` | `600` | `16px` | `0` |

> ⚠️ Raycast's CSS uses `500` more than any other weight. Do not reduce the system to 400/700; the middle weight is part of the product chrome.

### Principles
<!-- SOURCE: manual -->

1. Display type is centered and compact; large copy should feel like a command appearing over an active surface, not like editorial prose.
2. Weight `500` is a first-class UI weight for buttons, labels, and product panels.
3. Body text stays readable but secondary; muted supporting copy should sit around `#9C9C9D` or equivalent, not near-black or over-bright gray.
4. Mono fonts are semantic, not decorative: use them for commands, shortcuts, code, or terminal-like values only.
5. Large headings should use slight negative tracking; small labels keep tracking at `0` for keyboard-legibility.
6. Avoid ultra-light marketing type. Although weight `100` appears in CSS, the Raycast identity is built on firm 500/600 UI text.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed anchor steps)

| Token | Hex |
|---|---|
| `--ray-brand-red` | `#FF6363` |
| `--ray-brand-red-deep` | `#452324` |
| `--ray-brand-red-dark` | `#2C1617` |
| `--ray-brand-red-soft` | `#ECA5A7` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--ray-bg-900` | `#07080A` |
| `--ray-bg-800` | `#0C0D0F` |
| `--ray-bg-700` | `#111214` |
| `--ray-bg-600` | `#1B1C1E` |

### 06-3. Neutral Ramp

| Step | Dark token | Hex |
|---|---|---|
| 50 | `--grey-50` | `#E6E6E6` |
| 100 | `--grey-100` | `#CDCECE` |
| 200 | `--grey-200` | `#9C9C9D` |
| 300 | `--grey-300` | `#6A6B6C` |
| 400 | `--grey-400` | `#434345` |
| 500 | `--grey-500` | `#2F3031` |
| 600 | `--grey-600` | `#1B1C1E` |
| 700 | `--grey-700` | `#111214` |
| 800 | `--grey-800` | `#0C0D0F` |
| 900 | `--grey-900` | `#07080A` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Red / action | action/error | `#FF6363` |
| Blue / electric edge | supporting accent | `#56C2FF` |
| Green / success | success state | `#59D499` |
| Purple / AI command | decorative/AI accent | `#D8ACFF` |
| Yellow / warning | sparse state | `#FFCDCD` / yellow HSL token observed |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--color-bg` | `#07080A` | page background |
| `--color-bg-100` | `rgb(16,17,17)` | subtle raised panel |
| `--color-bg-200` | `rgb(24,25,26)` | card/control surface |
| `--color-fg` | `hsl(240,11%,96%)` | main foreground |
| `--color-fg-200` | `rgb(194,199,202)` | secondary foreground |
| `--color-fg-300` | `#78787C` | tertiary text |
| `--color-border` | `hsl(195,5%,15%)` | low-contrast borders |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--button-background` | component-defined | call-to-action background |
| `--button-hover-background` | `rgba(255,255,255,0.1)` | dark hover lift |
| `--color-button-bg` | `hsla(0,0%,100%,0.815)` | inverted light CTA surface |
| `--color-button-bg-hover` | `hsl(0,0%,100%)` | CTA hover surface |
| `--color-button-fg` | `rgb(24,25,26)` | text on light CTA |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency |
|---|---|---|
| white shorthand | `#FFF` | 122 |
| brand/error | `#FF6363` | 26 |
| white full | `#FFFFFF` | 24 |
| light neutral | `#D9D9D9` | 22 |
| panel | `#111214` | 13 |
| deep panel | `#0C0D0F` | 13 |
| dark red surface | `#452324` | 10 |
| success | `#59D499` | 6 |

### 06-8. Color Stories
<!-- SOURCE: manual — top 4 only -->

**`{colors.surface-black}` (`#07080A`)** — The floor. This is Raycast's actual page atmosphere, closer to a launcher overlay than a webpage canvas. Use it for full-page background and never replace it with generic black unless the surrounding panel ladder is also preserved.

**`{colors.brand-red}` (`#FF6363`)** — The command accent. It carries logo energy, action/error states, and the red side of the hero beam. It should feel sharp and hot, not pastel.

**`{colors.text-primary}` (`#FFFFFF`)** — The high-contrast foreground. Raycast accepts strong white text because the background is deep enough and the hero uses bright light as part of the brand.

**`{colors.text-muted}` (`#9C9C9D`)** — The control-room secondary voice. Navigation, captions, metadata, and supporting text should use muted gray so primary commands remain loud.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--spacing-0-5` | `4px` | tight icon/key internal offset |
| `--spacing-1` | `8px` | inline gaps, nav/control gap |
| `--spacing-1-5` | `12px` | compact card/control padding |
| `--spacing-2` | `16px` | button padding, small block rhythm |
| `--spacing-3` | `24px` | card/grid gaps |
| `--spacing-4` | `32px` | section substructure |
| `--spacing-6` | `48px` | larger feature block spacing |
| `--spacing-8` | `64px` | section breathing room |
| `--spacing-10` | `96px` | major vertical rhythm |
| `--spacing-12` | `168px` | large hero/editorial band |

**주요 alias**:
- `--grid-width` → `min(calc(100vw - 30px * 2),1065px)` (focused grid)
- `--container-width` → `1204px` (marketing container)
- `--grid-gap` → `32px` default, with `24px` at narrower breakpoints

### Whitespace Philosophy
<!-- SOURCE: manual -->

Raycast does not spend whitespace evenly. It gives the hero a cinematic center with huge open darkness, then compresses product proof into command-like cards and keyboard clusters. The contrast is the point: a broad black stage above, dense utility below.

The spacing ladder is still systematic: 4/8/12/16/24/32 form the everyday UI grid, while 64/96/168 are reserved for page rhythm. Avoid random in-between values. Raycast should feel engineered, not manually nudged.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--rounding-none` | `0px` | flush internal pieces |
| `--rounding-xs` | `4px` | small keys and detail chips |
| `--rounding-sm` | `6px` | common controls, keyboard keys |
| `--rounding-normal` | `8px` | compact cards and panels |
| `--rounding-md` | `12px` | primary cards, buttons, nav shell |
| `--rounding-lg` | `16px` | large feature blocks |
| `--rounding-xl` | `20px` | larger decorative/product surfaces |
| `--rounding-xxl` | `24px` | hero/product showcase surfaces |
| `--rounding-full` | `100%` | avatars and circular icon controls |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| nav glow | soft dark outer shadow | top navigation shell separation |
| light CTA | `0 0 0 1px` style border + subtle shadow | Download button on dark nav |
| hero glow | blurred red/cyan image/gradient light | background energy, not card elevation |
| cards | mostly border/surface contrast | panels use `#111214` over `#07080A` rather than heavy elevation |

Raycast shadow philosophy is "glow for atmosphere, borders for UI." Do not add generic SaaS card shadows to every panel.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| hover transition | short color/transform transitions | nav links, external links, cards |
| link icon offset | `translate(2px,-2px)` observed | external link hover direction |
| glow | conic/radial visual treatment | CTA glow and hero beam energy |
| carousel/embla | slider surfaces detected | testimonials and video carousel sections |

Motion should be crisp and command-like. Use quick fades or tiny directional movement; avoid slow floating blobs or springy consumer-app bounce.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `1204px` primary container; `1065px` focused grid; several product modules around `500px` widths.
- **Grid type**: CSS Grid and Flexbox mixed; product cards and extension lists use modular CSS classes.
- **Column count**: common `1`, `2`, and `3` variable column modes.
- **Gutter**: `32px` desktop default, `24px` at narrower widths, with dense internal `8px`/`16px` gaps.

### Hero
- **Pattern Summary**: `~80vh + diagonal red/cyan glow image + centered H1 + compact subcopy + nav download CTA`
- Layout: centered single-column text over full-width atmospheric background.
- Background: near-black base with diagonal blurred command beams.
- **Background Treatment**: image/gradient glow treatment; red, white, cyan, and blue smears over `#07080A`.
- H1: `~64px` / weight `600` / tracking `-0.02em`.
- Max-width: hero copy sits around `650px`; background image spans viewport.

### Section Rhythm

```css
section {
  padding: 64px 30px;
  max-width: var(--container-width); /* often 1204px */
}
```

### Card Patterns
- **Card background**: `#111214` or `rgb(16,17,17)` over `#07080A`.
- **Card border**: low-contrast `#2F3031` / `hsl(195,5%,15%)`.
- **Card radius**: `8px` to `12px`; larger showcases use `16px`/`24px`.
- **Card padding**: `16px`, `24px`, or component-specific.
- **Card shadow**: minimal; most separation is surface and border.

### Navigation Structure
- **Type**: horizontal desktop nav with centered links and right-side account/download actions.
- **Position**: top shell in hero, visually floating.
- **Height**: about `74px` shell with pill-like rounded rectangle.
- **Background**: dark translucent/panel black around `#111214`.
- **Border**: subtle hairline around `#2F3031` family.

### Content Width
- **Prose max-width**: `500px` to `700px` depending section.
- **Container max-width**: `1204px`.
- **Sidebar width**: not a primary homepage pattern; extension/detail pages use navigation panels.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `375px` / `400px` / `480px` | small control and text adjustments |
| Tablet | `640px` / `720px` / `768px` | grid and section shifts |
| Desktop | `980px` / `1024px` / `1064px` | desktop nav and product grid layouts |
| Large | `1200px` / `1204px` | full marketing container widths |

### Touch Targets
- **Minimum tap size**: assume `44px` target for major buttons; keyboard-key visuals can be smaller because they are illustrative.
- **Button height (mobile)**: approximately `34px` to `44px` depending component.
- **Input height (mobile)**: not fully observed on homepage cache.

### Collapsing Strategy
- **Navigation**: desktop horizontal nav collapses or simplifies below tablet/desktop breakpoints.
- **Grid columns**: variable `--column-count` moves from `3` to `2` to `1`.
- **Sidebar**: not homepage-primary; extension/detail pages likely collapse page navigation.
- **Hero layout**: remains centered; background crop and type scale carry responsive adaptation.

### Image Behavior
- **Strategy**: full-width responsive images and product media; hero background is cropped as atmospheric image.
- **Max-width**: frequent `100%`, plus container-bound media.
- **Aspect ratio handling**: product cards and thumbnails use fixed wrappers; exact ratios vary by component.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

Raycast buttons are compact, high-contrast, and command-like.

| Variant | Background | Text | Radius | Notes |
|---|---|---|---|---|
| Download nav button | `#FFFFFF` | `#0D0D0D` | `12px` | includes Apple icon; primary top-nav conversion point |
| Red CTA | `#FF6363` | `#FFFFFF` | `12px` | brand/action path |
| Dark utility button | `#111214` | `#FFFFFF` | `6px`/`8px` | product surfaces and small actions |
| Outline purple AI button | transparent | `#D8ACFF` | component-specific | AI/command feature accent |

States: hover brightens light CTA to full white, dark utilities use subtle white-alpha background, external link icons move diagonally by `translate(2px,-2px)`.

### Badges

Badges should be small and typographic, not pill-confetti. Use `12px`, weight `500` or `600`, `4px` to `8px` horizontal padding, and either a dark panel background or a single accent stroke.

### Cards & Containers

Raycast cards are dark panels, not white feature cards.

| Variant | Background | Border | Radius | Padding | Use |
|---|---|---|---|---|---|
| Product card | `#111214` | `#2F3031` | `12px` | `16px`/`24px` | app/extension/product proof |
| Keyboard key | `#111214` to `#18191A` | low-contrast hairline | `6px` | tight | shortcut and command visuals |
| Showcase frame | `#0C0D0F` | subtle | `16px`/`24px` | section-specific | large feature demos |

### Navigation

Navigation is a floating dark shell with small gray links, left logo, and a right-side inverted CTA. Link text sits muted until hover/active. The shell radius should be visibly larger than internal buttons, around `16px` to `20px` visually even if component internals use `12px`.

### Inputs & Forms

Homepage cache did not expose a full form system. Derive inputs from panel language: dark `#111214` or `rgb(24,25,26)` background, `1px` low-contrast border, `8px` to `12px` radius, white primary input text, muted placeholder around `#78787C`, focus with `#FF6363` or white-alpha ring.

### Hero Section

Hero component contract:

```html
<section class="ray-hero">
  <nav class="ray-nav">...</nav>
  <div class="ray-hero__beam"></div>
  <h1>Your shortcut to everything.</h1>
  <p>A collection of powerful productivity tools all within an extendable launcher.</p>
</section>
```

```css
.ray-hero {
  min-height: 800px;
  background: #07080A;
  color: #FFFFFF;
  text-align: center;
  overflow: hidden;
}
.ray-hero__beam {
  background:
    linear-gradient(135deg, transparent 20%, rgba(255,99,99,.95), rgba(86,194,255,.45), transparent 78%);
  filter: blur(18px);
  transform: rotate(-18deg);
}
```

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-download** — top navigation conversion button. Use white background, near-black text, Apple icon, `12px` radius, and compact horizontal padding. It must read as a Mac-native download affordance, not a generic "Get started" pill.

**keyboard-key** — the product-language primitive. Use dark raised surface, low-contrast border, `6px` radius, `12px` label size, and mono or firm UI weight. This component carries Raycast's shortcut identity.

**extension-card** — app ecosystem card. Use dark panel background, icon area, compact title, muted metadata, and a clean border. Hover can shift border/foreground subtly but should not add large elevation.

**command-action-row** — launcher-style row. Use icon + label + shortcut hint in a dense horizontal layout. Background stays dark; selected/hover state may use white-alpha or red accent.

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
diagonal-command-beam:
  description: "Hero's shortcut metaphor made physical: speed appears as a luminous diagonal path."
  technique: "large diagonal red/white/cyan beam over #07080A, softened with blur/noise-like texture, cropped behind centered type; reproduction baseline: linear-gradient(135deg, transparent 20%, rgba(255,99,99,.95), rgba(86,194,255,.45), transparent 78%) + filter: blur(18px) + transform: rotate(-18deg)"
  applied_to: ["{component.hero-section}"]
  visual_signature: "the headline looks suspended above a command streak, as if the launcher has just been invoked"

keyboard-token-chrome:
  description: "Shortcut keys become the reusable product alphabet rather than decorative badges."
  technique: "dark key surfaces #111214 to #18191A, 1px low-contrast #2F3031 border, 6px radius, 12px label, firm 500/600 weight, 4px-8px internal rhythm"
  applied_to: ["{component.keyboard-key}", "{component.command-action-row}"]
  visual_signature: "the page reads as keyboard-operated chrome, not click-first marketing UI"

white-download-inversion:
  description: "The primary Mac download action cuts through the dark shell with one bright OS-native affordance."
  technique: "#FFFFFF surface, #0D0D0D text, 12px radius, 10px 16px padding, compact Apple icon; keep inversion limited to the nav conversion button"
  applied_to: ["{component.button-download}", "{component.navigation}"]
  visual_signature: "one white key inside the black command palette"

conic-action-glow:
  description: "CTA energy is chromatic heat behind the action, not a site-wide gradient theme."
  technique: "conic-gradient using #0294FE, #FF2136, and #9B4DFF behind action surfaces; keep glow on CTA variants and away from ordinary cards"
  applied_to: ["{component.button-primary-red}", "{component.hero-section}"]
  visual_signature: "red command energy gains blue/purple voltage without becoming rainbow SaaS"

dark-panel-circuit-lines:
  description: "Interface depth is drawn with surface steps and hairlines instead of heavy card elevation."
  technique: "#07080A page floor, #111214 panel fill, #18191A raised key fill, 1px #2F3031 border, 8px-12px standard radius, minimal or no box-shadow on UI chrome"
  applied_to: ["{component.dark-card}", "{component.extension-card}", "{component.command-action-row}"]
  visual_signature: "panels look etched into a dark operating-system layer, with borders acting like circuit traces"
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | short, direct, productivity promise | "Your shortcut to everything." |
| Primary CTA | concrete platform action | "Download" |
| Secondary CTA | product/category exploration | Store, Pro, AI, Developers |
| Subheading | one-sentence utility expansion | "A collection of powerful productivity tools..." |
| Tone | fast, ergonomic, professional, Mac-native | "Take the short way." |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Raycast — copy into your root stylesheet */
:root {
  /* Fonts */
  --ray-font-family:       "Inter", "Inter Fallback", -apple-system, BlinkMacSystemFont, sans-serif;
  --ray-font-family-code:  "JetBrains Mono", "JetBrains Mono Fallback", Menlo, Monaco, Courier, monospace;
  --ray-font-weight-normal: 400;
  --ray-font-weight-medium: 500;
  --ray-font-weight-bold:   600;

  /* Brand */
  --ray-color-brand-300: #ECA5A7;
  --ray-color-brand-500: #FF6363;
  --ray-color-brand-600: #FF6363;
  --ray-color-brand-900: #452324;

  /* Surfaces */
  --ray-bg-page:    #07080A;
  --ray-bg-panel:   #111214;
  --ray-bg-raised:  #18191A;
  --ray-text:       #FFFFFF;
  --ray-text-muted: #9C9C9D;
  --ray-border:     #2F3031;

  /* Accents */
  --ray-blue:    #56C2FF;
  --ray-green:   #59D499;
  --ray-purple:  #D8ACFF;

  /* Spacing */
  --ray-space-xs:  4px;
  --ray-space-sm:  8px;
  --ray-space-md:  16px;
  --ray-space-lg:  24px;
  --ray-space-xl:  32px;
  --ray-space-2xl: 64px;

  /* Radius */
  --ray-radius-xs: 4px;
  --ray-radius-sm: 6px;
  --ray-radius-md: 8px;
  --ray-radius-lg: 12px;
  --ray-radius-xl: 16px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Raycast-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        ray: {
          bg: '#07080A',
          panel: '#111214',
          raised: '#18191A',
          border: '#2F3031',
          text: '#FFFFFF',
          muted: '#9C9C9D',
          red: '#FF6363',
          blue: '#56C2FF',
          green: '#59D499',
          purple: '#D8ACFF',
        },
      },
      fontFamily: {
        sans: ['Inter', 'Inter Fallback', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'JetBrains Mono Fallback', 'Menlo', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        medium: '500',
        semibold: '600',
      },
      borderRadius: {
        raySm: '6px',
        rayMd: '8px',
        rayLg: '12px',
        rayXl: '16px',
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
| Brand primary | `{colors.brand-red}` | `#FF6363` |
| Background | `{colors.surface-black}` | `#07080A` |
| Panel | `{colors.surface-panel}` | `#111214` |
| Text primary | `{colors.text-primary}` | `#FFFFFF` |
| Text muted | `{colors.text-muted}` | `#9C9C9D` |
| Border | `{colors.hairline}` | `#2F3031` |
| Success | `{colors.success}` | `#59D499` |
| Error | `{colors.error}` | `#FF6363` |

### Example Component Prompts

#### Hero Section
```text
Raycast 스타일 히어로 섹션을 만들어줘.
- 배경: #07080A
- 배경 처리: diagonal red/cyan/white command beam, blurred and cropped behind text
- H1: Inter, 64px desktop, weight 600, tracking -0.02em, color #FFFFFF
- 서브텍스트: #FFFFFF with slight opacity or #C2C7CA, 18px
- CTA: top nav Download button uses #FFFFFF background, #0D0D0D text, Apple icon
- 최대 너비: text around 650px, container around 1204px
```

#### Card Component
```text
Raycast 스타일 카드 컴포넌트를 만들어줘.
- 배경: #111214 over page #07080A
- border: 1px solid #2F3031
- radius: 12px
- padding: 16px or 24px
- shadow: heavy card shadow 금지, surface contrast로 분리
- 제목: Inter, 16px, weight 600, #FFFFFF
- 본문: 14px, color #9C9C9D, line-height 1.5
- hover: border/foreground만 미세하게 밝히고 큰 transform은 쓰지 않음
```

#### Keyboard Key
```text
Raycast 스타일 keyboard key를 만들어줘.
- surface: #111214 or #18191A
- border: 1px solid #2F3031
- radius: 6px
- label: 12px, weight 600, #FFFFFF
- gap: 4px to 8px
- mono는 command/code 값에만 사용
```

#### Navigation
```text
Raycast 스타일 상단 네비게이션을 만들어줘.
- dark floating shell, background #111214, border #2F3031
- logo left, muted links center, login + Download right
- links: 14px, #9C9C9D default, #FFFFFF hover
- Download: #FFFFFF bg, #0D0D0D text, 12px radius, Apple icon
```

### Iteration Guide

- **색상 변경 시**: page background는 반드시 `#07080A` 계열에서 시작. `#FFFFFF`를 page background로 쓰지 말 것.
- **폰트 변경 시**: Inter 대체는 가능하지만 weight `500`을 반드시 유지.
- **여백 조정 시**: 4/8/12/16/24/32/64 ladder를 사용. 임의 `13px`, `27px` 금지.
- **새 컴포넌트 추가 시**: dark panel + subtle border + compact typography 조합을 먼저 사용.
- **히어로 재현 시**: red만 쓰면 부족하다. cyan/white light edge가 함께 있어야 Raycast beam이 된다.
- **모션 추가 시**: quick command feedback만 허용. floaty parallax나 slow blob animation은 Raycast가 아니다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#07080A` as the page-level floor and build panels upward with `#0C0D0F`, `#111214`, and `#18191A`.
- Use `#FF6363` as the red command/action anchor, especially for brand heat and error/action energy.
- Keep navigation and product UI compact: 14px links, 12px labels, 8px/16px gaps.
- Preserve keyboard UI as a real component language, not as decorative tags.
- Use white CTA inversion sparingly for the Mac download action.
- Use `500` and `600` weights for UI chrome and controls.
- Use glow/gradient craft only in hero or CTA glow contexts, not as every-section wallpaper.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#07080A` 사용.
- 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#FFFFFF` on dark 또는 `#0D0D0D` on light CTA만 사용.
- 브랜드 레드를 `#FF0000`로 단순화하지 말 것 — 대신 `#FF6363` 사용.
- 패널 배경을 `#1E293B` 같은 generic slate로 두지 말 것 — 대신 `#111214` 또는 `#18191A` 사용.
- muted text를 `#6B7280` Tailwind gray로 대체하지 말 것 — 대신 `#9C9C9D` 또는 `#78787C` 사용.
- border를 `#E5E7EB` light hairline으로 두지 말 것 — 대신 `#2F3031` 계열 사용.
- body 기본을 `font-weight: 300`으로 만들지 말 것 — Raycast UI의 기본은 `400`, control chrome은 `500`.
- 모든 카드를 `border-radius: 24px`로 둥글게 만들지 말 것 — 일반 UI는 `6px`, `8px`, `12px`가 중심.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- Light SaaS canvas: absent. The homepage identity is not a white document with dark cards.
- Beige/warm productivity palette: none. Raycast is cool black, white, gray, red, and electric accent.
- Broad rainbow palette: absent. Multi-color appears as glow or state accents, not equal brand families.
- Heavy card elevation: never as a default. Borders and dark surface steps separate UI.
- Friendly blob illustration: absent. The hero uses sharp diagonal energy, not soft organic shapes.
- Serif editorial branding: not part of the core system. Serif may appear as isolated content flavor, not primary UI.
- Oversized rounded pills everywhere: absent. Pills are limited; normal components keep tighter radii.
- Generic purple-blue AI gradient background: not the page system. Purple appears in specific AI/CTA contexts only.
- Slow whimsical motion: none in the identity. Motion should read as shortcut feedback.
- Decorative icon confetti: absent. Icons serve product, platform, extension, or command meaning.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Cached capture date** — This guidebook reuses the available phase1 cache from April 20, 2026. The live Raycast homepage may have changed after that date.
- **Homepage-focused evidence** — The analysis centers on `https://www.raycast.com` homepage assets. Store, Pro, Teams, Developers, pricing, and extension detail pages may introduce additional component variants.
- **Screenshot scope** — Visual interpretation is based on a desktop hero screenshot at roughly 1280x800. Mobile screenshot behavior was inferred from CSS breakpoints rather than directly inspected.
- **Typography scale extraction gap** — The automated `typography.json` had no normalized `scale` entries, so the type ladder combines CSS weight/family evidence with screenshot-based manual estimation.
- **Form states incomplete** — Full input, validation, loading, and payment states were not all surfaced on the homepage cache. Input specs are derived from adjacent dark control patterns.
- **Motion runtime not fully traced** — CSS transitions and carousel markers were observed, but JavaScript timing, scroll-triggered behavior, and animation curves were not executed in this pass.
- **Token prefix is normalized** — `ray` is a guidebook prefix for reuse. The source CSS itself uses mixed tokens such as `--grey-*`, `--spacing-*`, `--rounding-*`, and component-local aliases.
- **Color frequency contamination possible** — Some chromatic colors may come from illustrations, extension icons, product media, or logo assets. Brand decisions prioritize recurring UI and hero identity over raw frequency alone.
- **Dark-mode counterpart not separate** — The marketing site is dark-first. A complete light-mode application palette was not extracted.
