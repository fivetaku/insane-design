---
schema_version: 3.2
slug: posthog
service_name: PostHog
site_url: https://posthog.com
fetched_at: 2026-04-20T20:00:00+09:00
default_theme: light
brand_color: "#F54E00"
primary_font: "IBM Plex Sans Variable"
font_weight_normal: 400
token_prefix: posthog

bold_direction: Desktop Cartoon
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Tailwind utility layer plus 128 CSS variables, data-scheme theme aliases, and repeated desktop-window/navigation/card patterns."

colors:
  primary: "#F54E00"
  primary-warm: "#F7A501"
  paper: "#EEEFE9"
  cream-highlight: "#F5E2B2"
  text-primary: "#1E1F23"
  ink: "#000000"
  white: "#FFFFFF"
  dark-surface: "#151515"
  success: "#36C46F"
  error: "#E92F2F"

typography:
  display: "IBM Plex Sans Variable"
  body: "IBM Plex Sans Variable"
  code: "Source Code Pro"
  ladder:
    - { token: hero-h1, size: "approx 24-32px", weight: 700, tracking: "0" }
    - { token: section-h2, size: "approx 22-28px", weight: 700, tracking: "0" }
    - { token: body, size: "15-16px", weight: 400, tracking: "0" }
    - { token: utility, size: "12-14px", weight: 600, tracking: "0" }
  weights_used: [100, 300, 400, 500, 600, 700, 800, 900]
  weights_absent: []

components:
  button-primary: { bg: "{colors.primary}", radius: "6px", border: "#000000", shadow: "1px hard-edge implied by border" }
  button-secondary: { bg: "#FFFFFF", radius: "6px", border: "#F54E00", color: "#4D4F46" }
  desktop-window: { bg: "#FFFFFF", border: "#BFC1B7", radius: "0-6px", shadow: "flat desktop chrome" }
  tab-active: { bg: "#F35454", color: "#FFFFFF", radius: "6px 6px 0 0" }
---

# DESIGN.md — PostHog (Designer Guidebook)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

PostHog does not present itself like a polished analytics SaaS. It stages the homepage as a slightly chaotic product engineer's desktop: wallpaper texture, draggable-looking file icons, a central document window, toolbar chrome, and a mascot illustration that behaves like a coworker who has made the office its habitat. The first impression is not "enterprise dashboard"; it is "open the project folder and start building." The page has almost no interest in looking like a website; it behaves like a workspace that accidentally became public.

The central hero is a `.mdx` file pinned open on a messy engineering desktop. The document window is the white sheet, the toolbar is the ruler, the side icons are loose files on the desk, and the hedgehog illustration is not decoration so much as the office mascot wandering into the spec. PostHog's best metaphor is not a gallery or showroom; it is a product team's shared machine after a long build day, with `home.mdx`, `demo.mov`, and `Trash` still visible because nobody cleaned the desktop before the demo.

The system is built on warm utility colors rather than pristine whites. The visible hero uses cream paper, off-gray panels, and orange controls. The interaction color is #F54E00 (`{colors.primary}`), but the broader page personality comes from #F5E2B2 (`{colors.cream-highlight}`), #EEEFE9 (`{colors.paper}`), black outlines, and hand-drawn iconography. Color is used like office supplies: labels, tabs, buttons, sticky notes, warning strips, and document highlights. There is no second equal brand color; orange owns action, while red tabs, mint status, navy strokes, and cream callouts behave like items pulled from the same utility drawer.

Typography is deliberately legible and workmanlike. `IBM Plex Sans Variable` carries most UI and editorial text; `Source Code Pro` appears for technical/code surfaces. The weights are not luxury-light. PostHog likes sturdy labels, bold nav affordances, and compact explanatory body copy. The type supports the desktop metaphor: headings feel like document titles, not cinematic campaign headlines.

The signature move is the collision between utilitarian product architecture and playful low-fi illustration. A central white window frames the primary pitch, while side icons ("home.mdx", "demo.mov", "Trash") and the hedgehog scene create a product OS fantasy. Below the hero, the tabbed feature area keeps the same physicality: active red tab, thick border, and a document-like content panel. It is closer to a stickered laptop screen than a SaaS landing page: every object is flat enough to be UI, but specific enough to feel handled.

This is a design system where polish comes from constraint, not gloss. It uses flat surfaces, hard borders, compact chrome, and mascot craft. Shadows do not create a soft premium atmosphere; they only help objects read as props. It avoids generic glass, purple gradients, and floating SaaS cards. If you remove the desktop frame and the orange-black utility controls, the site immediately becomes unrecognizable.

### Key Characteristics

- Desktop OS metaphor: wallpaper, file icons, top menu bar, document window, toolbar controls, trash icon.
- Product-editor hero: the homepage pitch lives inside a `home.mdx` editing window rather than a normal marketing section.
- Orange as action color: #F54E00 / #F7A501 appears on CTA buttons, swiper tokens, and product accents.
- Warm paper neutrals: #EEEFE9, #F5E2B2, #FFFFFF, and black outlines create a printable office feel.
- Cartoon technicality: hand-drawn icons and hedgehog illustration sit next to serious product-development language.
- Dense navigation: top nav plus desktop side icons makes the page feel like a usable environment.
- Hard-edge components: borders and tabs matter more than soft elevation.
- Humor in microcopy: "Legally-required cookie banner" and "so proud" voice break SaaS solemnity.
- Mixed product surfaces: docs, pricing, changelog, support, and product OS are treated as desktop artifacts.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Desktop Cartoon
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **desktop product OS hero with cartoon engineering artifacts**으로 기억된다.
> **Code Complexity**: high — Tailwind utility density, data-scheme variables, desktop-window composition, tab states, icon wallpaper, and illustration layers all have to align.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 PostHog처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "IBM Plex Sans Variable", "IBM Plex Sans", -apple-system, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #EEEFE9;
  --fg: #1E1F23;
}
body {
  background: var(--bg);
  color: var(--fg);
}

/* 3. 브랜드 컬러 */
:root {
  --brand: #F54E00;
  --brand-warm: #F7A501;
}
```

**절대 하지 말아야 할 것 하나**: 일반 SaaS처럼 순백 배경 위 중앙 정렬 히어로와 둥근 그라디언트 카드를 놓지 말 것. PostHog는 "웹페이지"가 아니라 "제품 엔지니어의 데스크톱 작업실"로 보일 때 살아난다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://posthog.com` |
| Fetched | 2026-04-20T20:00:00+09:00 |
| Extractor | phase1 reuse: existing HTML/CSS/screenshots |
| HTML size | 1,054,660 bytes |
| CSS files | 1 external CSS file, 641,269 chars |
| Phase1 JSON | `brand_candidates.json`, `resolved_tokens.json`, `typography.json`, `alias_layer.json` |
| Token prefix | `posthog` (guidebook alias); source CSS uses Tailwind + scheme variables |
| Method | Existing phase1 token summaries + CSS regex sampling + hero screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React/SSR marketing site, likely Gatsby/React Helmet from HTML metadata and hydrated page structure.
- **Design system**: Tailwind utility layer plus PostHog-specific `data-scheme` theme variables.
- **CSS architecture**:
  ```css
  [data-scheme=primary] {
    --bg: 253 253 248;
    --accent: 229 231 224;
    --border: 191 193 183;
    --text-primary: 77 79 70;
    --text-secondary: 101 103 94;
    --text-muted: 158 160 150;
  }

  [data-scheme=secondary] {
    --bg: 238 239 233;
    --accent: 210 211 204;
    --border: 182 183 175;
    --text-primary: 35 37 29;
  }
  ```
- **Class naming**: Tailwind-style atomic utilities (`bg-primary`, `border-primary`, `text-primary`, `grid-cols-*`) plus semantic scheme wrappers.
- **Default theme**: light (`body class="light" data-wallpaper="keyboard-garden"`).
- **Font loading**: custom webfont usage via CSS declarations for `IBM Plex Sans Variable`, `Source Code Pro`, and playful display fonts.
- **Canonical anchor**: central desktop/document hero plus orange CTA and side desktop icon rails.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `IBM Plex Sans Variable` for main product/editorial surfaces.
- **Body font**: `IBM Plex Sans Variable`, with `IBM Plex Sans`, Apple/system UI, and common sans fallbacks.
- **Code font**: `Source Code Pro`, with Menlo/Consolas/Monaco fallbacks.
- **Specialty fonts detected**: `Open Runde`, `Impact`, `Charter`, `Squeak`, `Comic Sans MS`, `Computer Modern`, `Fairytale`. These support PostHog's playful sub-surfaces, not the default UI.
- **Weight normal / bold**: 400 / 700, with broad utility support from 100 through 900.

```css
:root {
  --posthog-font-family: "IBM Plex Sans Variable", "IBM Plex Sans", -apple-system, sans-serif;
  --posthog-font-family-code: "Source Code Pro", Menlo, Consolas, monaco, monospace;
  --posthog-font-weight-normal: 400;
  --posthog-font-weight-bold: 700;
}
body {
  font-family: var(--posthog-font-family);
  font-weight: var(--posthog-font-weight-normal);
}
```

### Note on Font Substitutes

- **IBM Plex Sans Variable** is the important substitute target. If the exact variable font is unavailable, use **IBM Plex Sans** first, then **Inter** only as a last resort. Keep body at 400 and labels/buttons at 600-700; do not make the page feel like thin enterprise SaaS.
- **Source Code Pro** should remain for code/editor affordances. A system monospace fallback is acceptable, but reduce letter-spacing to `0` and keep line-height compact so toolbars and docs snippets retain their utility feel.
- **Playful specialty fonts** should be used sparingly. Do not replace the whole page with `Comic Sans MS` or `Impact`; those fonts are local jokes, not the base design system.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---:|---|---|
| Hero product title | approx 24-32px | 700 | 1.15-1.25 | 0 |
| Section title | approx 22-28px | 700 | 1.2 | 0 |
| Body paragraph | 15-16px | 400 | 1.45-1.6 | 0 |
| Navigation label | 13-14px | 500-600 | 1.2 | 0 |
| Button label | 13-14px | 700 | 1 | 0 |
| Desktop icon label | 12-14px | 400-500 | 1.15 | 0 |
| Code/editor text | 13-15px | 400 | 1.45 | 0 |

> ⚠️ PostHog's typography is compact, sturdy, and UI-native. The mistake is to over-scale it into cinematic landing-page type.

### Principles

1. Headings are document titles, not luxury headlines. Keep them bold and compact instead of ultra-large.
2. Body copy stays readable and plain. The personality comes from environment and illustration, not expressive paragraph typography.
3. Button labels are heavier than body text. The orange CTA must feel like a real OS control, not a soft marketing pill.
4. Monospace is contextual. Use `Source Code Pro` for technical/editor surfaces only.
5. Specialty fonts are accent materials. They can label a playful asset, but they must not take over product copy.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed chromatic anchors)

| Token | Hex |
|---|---|
| `posthog-orange` | `#F54E00` |
| `posthog-orange-alt` | `#F7A501` |
| `posthog-orange-muted` | `#EB9D2A` |
| `posthog-orange-dark` | `#C23D00` |
| `posthog-orange-deep` | `#802700` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `posthog-dark-surface` | `#151515` |
| `posthog-dark-panel` | `#1E1F23` |
| `posthog-dark-ink` | `#000000` |
| `posthog-dark-text-invert` | `#FFFFFF` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| Page / paper | `#EEEFE9` | `#1E1F23` |
| Warm highlight | `#F5E2B2` | `#151515` |
| White surface | `#FFFFFF` | `#000000` |
| Muted utility | `#8D8D8D` | `#333333` |
| Tailwind gray | `#D1D5DB` | `#374151` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Product orange | CTA / action | `#F54E00` |
| Warm yellow | highlight / pagination | `#F7A501` |
| Red | active tab / error emphasis | `#E92F2F` |
| Mint | success / positive data | `#36C46F` |
| Cyan | focus / link utility | `#29DBBB` |
| Navy | icon fill/stroke | `#1E2F46` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `{colors.primary}` | `#F54E00` | CTA, active controls, strongest brand action |
| `{colors.primary-warm}` | `#F7A501` | warmer accent, carousel/swiper and illustration-adjacent emphasis |
| `{colors.paper}` | `#EEEFE9` | desktop/window/panel neutral |
| `{colors.cream-highlight}` | `#F5E2B2` | callout strips, warm highlight regions |
| `{colors.text-primary}` | `#1E1F23` | dark UI text / dark panel anchor |
| `{colors.white}` | `#FFFFFF` | document/editor surface |
| `{colors.success}` | `#36C46F` | success indicators |
| `{colors.error}` | `#E92F2F` | error and active red tab family |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--bg` | `253 253 248` or `238 239 233` | scheme background, rendered as near-paper light surfaces |
| `--accent` | `229 231 224` / `210 211 204` | secondary surface and hover accents |
| `--border` | `191 193 183` / `182 183 175` | hairline and container borders |
| `--text-primary` | `77 79 70` / `35 37 29` | primary text in data-scheme surfaces |
| `--text-secondary` | `101 103 94` | secondary text |
| `--squeak-button-color` | `245,78,0` | Squeak/chat button orange = #F54E00 |

### 06-7. Dominant Colors (CSS frequency signal)

| Token | Hex | Frequency note |
|---|---|---|
| Transparent | `#00000000` / `#0000` | high utility frequency; not brand |
| White | `#FFFFFF` / `#FFF` | document and inverted text surfaces |
| Black | `#000000` / `#000` | outlines, icon ink, utility reset |
| Warm cream | `#F5E2B2` | repeated warm highlight |
| Dark panel | `#1E1F23` | dark UI/code surfaces |
| Action orange | `#F54E00` | strongest chromatic action |

### 06-8. Color Stories

**`{colors.primary}` (`#F54E00`)** — This is the action orange. Use it for "Get started", product emphasis, and the elements that need to feel clickable or active. Do not spread it across every decorative surface; it works because the page is otherwise warm-neutral and inked.

**`{colors.paper}` (`#EEEFE9`)** — This is the office-paper atmosphere. It keeps the desktop metaphor from becoming sterile white and gives black outlines and cartoon assets a physical base.

**`{colors.text-primary}` (`#1E1F23`)** — This is the hard UI ink. It should feel closer to a printed interface than a soft gray marketing page.

**`{colors.cream-highlight}` (`#F5E2B2`)** — This is the warm sticky-note layer. Use it for callouts and inset emphasis, not as a full brand replacement for orange.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `posthog-gap-xs` | 4px | toolbar/icon micro gaps |
| `posthog-gap-sm` | 8px | nav items, small controls |
| `posthog-gap-md` | 16px | button groups, desktop icon grid, card internals |
| `posthog-gap-lg` | 24px | hero paragraph blocks and panel breathing room |
| `posthog-gap-xl` | 32px | section grouping |
| `posthog-container` | 1024-1280px | main marketing/content width |
| `posthog-wallpaper-rail` | approx 110-150px | side desktop icon lanes around central window |

**주요 alias**:
- `--viewport-padding` → `25px` (toast/viewport padding)
- `grid-cols-*` → Tailwind repeat grid utilities for product rows, nav menus, and content panels.

### Whitespace Philosophy

PostHog's whitespace is not luxurious empty air. It is desktop working space. The central white document window has enough padding to read like an editor, while the surrounding wallpaper is intentionally busy with icons, navigation, cookie banner, and illustration. The page earns density by making every object feel like part of an OS.

The rhythm alternates between framed and unframed zones: top menu bar, document window, tabbed panel, then product sections. Spacing should therefore be measured in "desktop object distance" rather than editorial bands. Tight icon labels and toolbar controls are correct; giant 96px marketing gaps are not.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `posthog-radius-none` | `0` | window edges, hard panels, tab joins |
| `posthog-radius-sm` | `4px` | small utility controls |
| `posthog-radius-md` | `6px` | CTA buttons, toolbar controls |
| `posthog-radius-lg` | `8px` | cards and modal-like surfaces |
| `posthog-radius-xl` | `10px-15px` | playful callouts, illustration containers |
| `posthog-radius-pill` | `9999px` | badges or pill utilities only |
| `posthog-radius-round` | `50%` / `100%` | icon avatar/circular controls |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| Ring | `0 0 0 1px var(--tw-border-primary,#000)` | hard-outline chrome |
| Small | `0 1px 2px #0000001a` | subtle utility elevation |
| Panel | `0 1px 4px 1px rgba(0,0,0,.08)` | light popover/card depth |
| Focus blue | `0 0 2px 2px #0096ff` | accessibility/focus ring |
| Orange glow | `0 0 12px 2px rgba(255,165,0,.4)` | accent emphasis, use sparingly |
| Heavy object | `0 4px 12px rgba(0,0,0,.25)` | illustration/object-style depth |

PostHog's chrome should primarily be border-led. Shadows are supporting detail, not the main structure.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `hover-invert` | theme variable swap on hover/open/highlighted | menu and interactive surface inversion |
| `--tw-blur` | `blur(8px)` | utility blur effects |
| `--tw-backdrop-blur` | `blur(4px)` | lightweight overlay/backdrop |
| `--tw-drop-shadow` | two-layer drop shadow | object/image utility |

Motion is implied more than cinematic. Use hover state changes, active tab shifts, and small variable swaps. Avoid long parallax or generic reveal animations unless a specific PostHog page section proves it.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: central hero window approx 960px within a 1280px viewport; utility max-width classes include 640, 768, 900, 1024, 1160, 1280, 1536px.
- **Grid type**: CSS Grid and Flexbox, with Tailwind repeat columns from 1 to 16.
- **Column count**: marketing/product areas use 2-4 columns; navigation/dropdown structures include 3-4 column grids; comparison/product grids can use larger repeat counts.
- **Gutter**: 8-24px depending on desktop-object density.

### Hero
- **Pattern Summary**: desktop wallpaper + central document editor window + side file icons + orange CTA.
- Layout: a centered OS/document frame with left text, right mascot illustration, side desktop icon rails, and top menu bar.
- Background: warm speckled wallpaper plus illustrated garden/desktop artifacts.
- **Background Treatment**: texture/image wallpaper, not a CSS gradient mesh.
- H1: compact bold product headline, approx 24-32px / weight 700 / tracking 0.
- Max-width: central window approx 960px, page viewport framed by desktop icon rails.

### Section Rhythm

```css
section {
  padding: 32px 24px;
  max-width: 1280px;
}
```

Actual rhythm is object-led: the hero window, tab bar, and panels define spacing more than uniform marketing sections.

### Card Patterns
- **Card background**: #FFFFFF document panels or #EEEFE9 / scheme surfaces.
- **Card border**: 1px solid warm gray/black-adjacent border; active panels may use red/orange border.
- **Card radius**: 6-8px for controls/cards; 0px where window/tab joins need hard edges.
- **Card padding**: 16-24px typical.
- **Card shadow**: light only; border is the structural line.

### Navigation Structure
- **Type**: horizontal top menu plus desktop icon links around the viewport.
- **Position**: top menu reads fixed/sticky desktop menubar; hero icons are positioned like desktop files.
- **Height**: approx 40px top bar.
- **Background**: warm gray/cream surface.
- **Border**: thin bottom separator and black/icon ink.

### Content Width
- **Prose max-width**: 640-768px for readable docs/product copy.
- **Container max-width**: 1024-1280px for primary content.
- **Sidebar width**: desktop icon rails approx 110-150px when visible.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Compact | 425px / 482px | small custom max-width utility thresholds |
| Mobile | 640px | first Tailwind responsive tier |
| Tablet | 768px | nav/grid expansion and desktop layout begins |
| Desktop | 1024px | multi-column product sections |
| Wide | 1280px / 1536px | full desktop/window composition |

### Touch Targets
- **Minimum tap size**: target 40-44px for mobile controls; top hero CTA appears approx 36-40px high on desktop.
- **Button height (mobile)**: should preserve at least 40px, especially orange CTAs.
- **Input height (mobile)**: scheme variables define input backgrounds/borders; exact form states were not surfaced in the hero.

### Collapsing Strategy
- **Navigation**: top product nav compresses; side desktop icons should collapse or become secondary on small widths.
- **Grid columns**: `grid-cols-1` to `grid-cols-2/3/4` through Tailwind breakpoints.
- **Sidebar**: desktop icon rails are decorative/navigation chrome and should not crowd mobile.
- **Hero layout**: central document window should become single-column; illustration can move below/behind or be cropped.

### Image Behavior
- **Strategy**: illustrative assets and icons are object-like; keep pixel/hand-drawn clarity.
- **Max-width**: CSS includes `max-width:100%`.
- **Aspect ratio handling**: preserve original illustration proportions; do not stretch mascot or desktop icons.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA**

| Property | Value |
|---|---|
| Background | `#F54E00` or warm orange token |
| Text | `#000000` or dark ink when on orange |
| Border | hard black/dark border or darker orange edge |
| Radius | 6px |
| Padding | approx 10-14px x 16-20px |
| Weight | 700 |
| State | hover should darken/press like a desktop button, not glow softly |

```html
<button class="posthog-button posthog-button-primary">Get started - free</button>
```

**Secondary CTA**

| Property | Value |
|---|---|
| Background | `#FFFFFF` / transparent paper |
| Text | `#4D4F46`-style scheme text |
| Border | `#F54E00` or warm border |
| Radius | 6px |
| Use | "Install with AI", lower-priority actions |

### Badges

Badges are utility labels rather than pill-heavy SaaS tags. Keep them compact with 12-13px type, warm paper backgrounds, and strong text contrast. Use pill radius only when the source component is genuinely a pill; otherwise small rectangles fit the desktop metaphor better.

### Cards & Containers

**Desktop document window**

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Border | 1px warm gray / dark outline |
| Radius | top window chrome may use 6px; internal panels can be square |
| Header | filename-centered toolbar (`home.mdx`) |
| Interior | document-like content with left text and right illustration |

**Tabbed feature panel**

| Property | Value |
|---|---|
| Active tab | red/orange family, screenshot shows active red tab |
| Border | thick active outline around content |
| Background | white/cream document surface |
| Behavior | tab selected state is physical, not just underline text |

### Navigation

Top nav uses compact text links and a right-side action cluster: orange CTA, search icon, help/question icon, small counters, account icon. Side navigation uses desktop files with icons and labels. The two systems must coexist: one is product-site navigation, the other is desktop-world navigation.

### Inputs & Forms

Observed scheme variables:

```css
--input-bg: 238 239 233;
--input-bg-hover: 238 239 233;
--input-border: 210 211 204;
--input-border-hover: 210 211 204;
```

Inputs should use warm off-white fills, subdued borders, and direct focus rings. Avoid floating labels and glass fields.

### Hero Section

Hero components:

- desktop wallpaper background
- top OS-like menubar
- left/right desktop file icons
- central document editor window
- toolbar row with undo/redo, zoom, bold/italic/underline, alignment, link/comment controls
- orange CTA inside window toolbar and content body
- mascot illustration on right
- cookie banner overlay in lower-right

### 13-2. Named Variants

**`button-primary`**

| Property | Value |
|---|---|
| bg | `#F54E00` |
| radius | 6px |
| border | hard dark edge |
| typography | IBM Plex Sans Variable, 13-14px, 700 |
| state | hover/active should read as pressed desktop control |

**`button-secondary-outline`**

| Property | Value |
|---|---|
| bg | `#FFFFFF` or paper |
| border | `#F54E00` |
| color | scheme text |
| radius | 6px |

**`desktop-window`**

| Property | Value |
|---|---|
| bg | `#FFFFFF` |
| chrome | warm gray toolbar |
| title | centered filename, bold small text |
| border | hard 1px outline |

**`feature-tab-active`**

| Property | Value |
|---|---|
| bg | red/orange active surface |
| color | white |
| border relationship | tab visually attaches to content panel |

### 13-3. Signature Micro-Specs

```yaml
keyboard-garden-desktop-wallpaper:
  description: "The first viewport is treated as an operating-system desktop instead of a centered SaaS hero."
  technique: "body data-wallpaper=\"keyboard-garden\" + #EEEFE9 warm paper field + approx 110-150px side icon rails + approx 40px top menubar"
  applied_to: ["{component.hero}", "{component.navigation}", "{component.desktop-file-icons}"]
  visual_signature: "A user feels they landed inside a PostHog product workspace, with files left around the wallpaper."

home-mdx-editor-window:
  description: "The value proposition lives inside a named document/editor surface, not a generic marketing card."
  technique: "#FFFFFF document canvas + 1px warm gray/dark outline + 6px outer chrome radius + centered filename titlebar + toolbar controls"
  applied_to: ["{component.desktop-window}", "{component.hero}", "{component.button-primary}"]
  visual_signature: "The homepage pitch reads like an editable `home.mdx` file opened on the team's machine."

orange-black-desktop-control:
  description: "Primary actions behave like physical desktop controls rather than soft gradient pills."
  technique: "#F54E00 fill (`{colors.primary}`) + #000000 hard border + 6px radius + 13-14px / 700 IBM Plex Sans label + pressed hover darkening"
  applied_to: ["{component.button-primary}", "{component.hero-toolbar}", "{component.active-controls}"]
  visual_signature: "The CTA looks playful but mechanically decisive, like a real button in a retro productivity app."

red-tab-attached-panel:
  description: "Feature navigation uses attached document tabs instead of underline-only SaaS navigation."
  technique: "#E92F2F active tab surface + #FFFFFF text + 6px 6px 0 0 radius + hard border relationship to white/cream content panel"
  applied_to: ["{component.feature-tab-active}", "{component.tabbed-feature-panel}"]
  visual_signature: "The selected state feels like a folder tab physically clipped to the panel below it."

cartoon-engineering-prop-layer:
  description: "Friendliness is carried by object illustration while the UI typography stays sturdy and utilitarian."
  technique: "hand-drawn file icons + hedgehog/office props + object-style depth up to 0 4px 12px rgba(0,0,0,.25), with chrome still border-led"
  applied_to: ["{component.hero-illustration}", "{component.desktop-file-icons}", "{component.cookie-banner}"]
  visual_signature: "Engineering tooling avoids enterprise coldness by looking like a desk covered in specific product-team props."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | direct product-engineering claim | "The new way to build products" |
| Primary CTA | plain, low-friction, free-start language | "Get started - free" |
| Secondary CTA | technical workflow action | "Install with AI" |
| Subheading | explains product development pain in concrete workflow terms | "manually writing code, running analysis, diagnosing bugs..." |
| Humor | legal/required moments get a wink | "Legally-required cookie banner" |
| Tone | product-engineer informal, not sales-polished | "Talk to a human", "Ask a question" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* PostHog — copy into your root stylesheet */
:root {
  /* Fonts */
  --posthog-font-family: "IBM Plex Sans Variable", "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --posthog-font-family-code: "Source Code Pro", Menlo, Consolas, monaco, monospace;
  --posthog-font-weight-normal: 400;
  --posthog-font-weight-bold: 700;

  /* Brand */
  --posthog-color-brand-500: #F54E00;
  --posthog-color-brand-600: #F54E00;
  --posthog-color-brand-warm: #F7A501;
  --posthog-color-brand-muted: #EB9D2A;
  --posthog-color-brand-dark: #C23D00;

  /* Surfaces */
  --posthog-bg-page: #EEEFE9;
  --posthog-bg-paper: #FFFFFF;
  --posthog-bg-highlight: #F5E2B2;
  --posthog-bg-dark: #1E1F23;
  --posthog-text: #1E1F23;
  --posthog-text-muted: #8D8D8D;
  --posthog-border: #D1D5DB;

  /* Key spacing */
  --posthog-space-xs: 4px;
  --posthog-space-sm: 8px;
  --posthog-space-md: 16px;
  --posthog-space-lg: 24px;
  --posthog-space-xl: 32px;

  /* Radius */
  --posthog-radius-sm: 4px;
  --posthog-radius-md: 6px;
  --posthog-radius-lg: 8px;
}

.posthog-button-primary {
  background: var(--posthog-color-brand-600);
  color: #000000;
  border: 1px solid #000000;
  border-radius: var(--posthog-radius-md);
  padding: 10px 16px;
  font-weight: var(--posthog-font-weight-bold);
}

.posthog-window {
  background: var(--posthog-bg-paper);
  border: 1px solid var(--posthog-border);
  border-radius: var(--posthog-radius-md);
  color: var(--posthog-text);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — PostHog-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        posthog: {
          orange: '#F54E00',
          yellow: '#F7A501',
          paper: '#EEEFE9',
          cream: '#F5E2B2',
          ink: '#1E1F23',
          white: '#FFFFFF',
          success: '#36C46F',
          error: '#E92F2F',
        },
      },
      fontFamily: {
        sans: ['IBM Plex Sans Variable', 'IBM Plex Sans', 'system-ui', 'sans-serif'],
        mono: ['Source Code Pro', 'ui-monospace', 'monospace'],
      },
      borderRadius: {
        posthog: '6px',
      },
      boxShadow: {
        'posthog-ring': '0 0 0 1px var(--tw-border-primary, #000)',
        'posthog-panel': '0 1px 4px 1px rgba(0,0,0,.08)',
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
| Brand primary | `{colors.primary}` | `#F54E00` |
| Brand warm | `{colors.primary-warm}` | `#F7A501` |
| Background | `{colors.paper}` | `#EEEFE9` |
| Highlight | `{colors.cream-highlight}` | `#F5E2B2` |
| Text primary | `{colors.text-primary}` | `#1E1F23` |
| Border / gray | `posthog-border` | `#D1D5DB` |
| Success | `{colors.success}` | `#36C46F` |
| Error | `{colors.error}` | `#E92F2F` |

### Example Component Prompts

#### Hero Section

```text
PostHog 스타일 히어로 섹션을 만들어줘.
- 전체 배경은 데스크톱 wallpaper처럼 #EEEFE9 기반의 warm neutral texture로 보이게 한다.
- 중앙에는 흰색 document/editor window를 놓고 titlebar에는 "home.mdx"를 둔다.
- H1은 IBM Plex Sans Variable, 24-32px, weight 700, tracking 0.
- CTA는 #F54E00 배경, black text, 6px radius, hard border, label은 "Get started - free".
- 오른쪽에는 hand-drawn mascot/product illustration을 넣고, 주변에는 file icon labels를 배치한다.
- 일반 SaaS hero card나 purple gradient는 쓰지 않는다.
```

#### Card Component

```text
PostHog 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF 또는 #EEEFE9
- border: 1px solid warm gray, hard outline 중심
- radius: 6px 또는 8px
- padding: 16-24px
- shadow는 약하게만 사용하고 border가 구조를 만들게 한다.
- 제목: IBM Plex Sans Variable, 16px, weight 700
- 본문: 15px, color #1E1F23, line-height 1.5
```

#### Badge

```text
PostHog 스타일 배지를 만들어줘.
- font: IBM Plex Sans Variable, 12-13px, weight 600
- padding: 2px 8px
- radius: 4-6px. pill은 꼭 필요한 경우에만.
- 배경: #F5E2B2 또는 #EEEFE9
- border: 1px solid #D1D5DB
- 색상은 utility label처럼 절제한다.
```

#### Navigation

```text
PostHog 스타일 상단 네비게이션을 만들어줘.
- 높이 약 40px, warm gray background, thin bottom border.
- 좌측에는 compact logo와 Product OS / Pricing / Docs / Community / Company / More 링크.
- 우측에는 #F54E00 CTA, search icon, help icon, small counter, account icon을 둔다.
- 링크는 13-14px, weight 500, 검정/짙은 neutral.
- 모바일에서는 desktop side icon rails를 접고 핵심 링크와 CTA만 남긴다.
```

### Iteration Guide

- **색상 변경 시**: action은 #F54E00에 고정한다. 보조 warm accent는 #F7A501 / #F5E2B2로 제한한다.
- **폰트 변경 시**: `IBM Plex Sans Variable`의 sturdy product tone을 유지한다. 얇은 300 중심의 luxury SaaS 느낌으로 바꾸지 않는다.
- **여백 조정 시**: desktop object 간격처럼 8/16/24/32px를 우선한다.
- **새 컴포넌트 추가 시**: border-led chrome, hard controls, document/window metaphor를 우선한다.
- **일러스트 추가 시**: hand-drawn object/mascot language와 맞춰야 한다. 추상 3D blobs는 금지.
- **반응형**: hero desktop chrome은 모바일에서 단순화하되 orange CTA와 document metaphor는 유지한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- 데스크톱 OS 메타포를 유지하라: 파일 아이콘, window chrome, toolbar, document frame 같은 물리적 단서를 사용.
- CTA와 active action에는 #F54E00을 사용하라.
- 배경은 #EEEFE9 / #F5E2B2 같은 warm neutral로 시작하라.
- 타이포는 `IBM Plex Sans Variable` 중심으로 compact하고 sturdy하게 둔다.
- 구조는 shadow보다 border와 tab attachment로 만든다.
- 만화/hand-drawn asset을 제품 기능과 연결하라. 단순 장식으로 흩뿌리지 않는다.
- 문구는 제품 엔지니어가 바로 이해하는 워크플로우 언어로 쓴다.

### ❌ DON'T

- 배경을 `#FFFFFF` 순백 page로 두지 말 것 — 대신 `#EEEFE9` 또는 warm scheme background 사용.
- 텍스트를 `#000000`만으로 납작하게 두지 말 것 — 대신 UI 본문은 `#1E1F23` / scheme text를 사용하고 black은 outline/ink에 제한.
- CTA를 `#007AFF` 또는 generic blue로 두지 말 것 — 대신 `#F54E00` 사용.
- warm callout을 `#FFFF00` 같은 순수 노랑으로 두지 말 것 — 대신 `#F5E2B2` 또는 `#F7A501` 사용.
- active/error tab을 `#FF0000` 순색으로 두지 말 것 — 대신 `#E92F2F` / orange-red family 사용.
- 다크 패널을 `#000000` full black으로 채우지 말 것 — 대신 `#151515` 또는 `#1E1F23` 사용.
- 모든 카드를 24px radius의 floating SaaS card로 만들지 말 것 — PostHog는 6-8px hard chrome이 맞다.
- hero에서 generic purple gradient (`#667EEA` → `#764BA2`)를 쓰지 말 것 — PostHog hero는 desktop wallpaper + document window다.
- 버튼 label을 light 400으로 두지 말 것 — primary action은 bold, compact, physical control이어야 한다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **No generic SaaS gradient hero** — PostHog does not use purple-blue mesh as identity.
- **No luxury minimalism** — empty white galleries and ultra-thin type fight the product-engineer tone.
- **No glass-first UI** — blur utilities exist, but the brand surface is border/window/paper, not glassmorphism.
- **No second equal brand color** — orange owns action. Other colors are product/status/illustration support.
- **No soft floating-card monoculture** — cards must feel like desktop objects or documents.
- **No stock corporate illustration** — mascot/object drawings are specific and humorous.
- **No all-center landing pattern** — the hero is spatial and environmental, with side icons and window chrome.
- **No pure black dark theme as default** — dark surfaces are nuanced (#151515 / #1E1F23), not empty black.
- **No over-polished enterprise voice** — copy keeps practical, slightly irreverent phrasing.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single capture basis** — this guide reuses the existing `posthog` phase1 capture and hero screenshot. It does not prove every current subpage on 2026-05-03 still matches the same visual surface.
- **RGB scheme variables converted for readability** — source CSS stores several core theme values as RGB triplets (`--bg: 253 253 248` etc.). The frontmatter uses human-readable hex aliases only where the color relationship is clear.
- **Homepage-first interpretation** — product app internals, logged-in dashboards, billing flows, and form validation states were not visited.
- **Motion logic not fully executed** — CSS utilities for blur/drop-shadow/hover were sampled, but JS-driven transitions or scroll behavior were not exhaustively traced.
- **Logo/illustration color contamination** — chromatic frequency includes SVGs, mascot art, and docs/product illustrations. Brand selection prioritizes CTA/action orange over raw frequency.
- **Exact hero typography is screenshot-estimated** — generated CSS is utility-heavy and minified; H1 sizes are described as observed ranges rather than a single authoritative token.
- **Current-session plugin loading unaffected** — this file is written to `plugins/insane-design/docs/reports/posthog/design.md`; Codex plugin cache/runtime reload was not part of this task.
