---
schema_version: 3.2
slug: microsoft
service_name: Microsoft
site_url: https://www.microsoft.com/en-us
fetched_at: 2026-04-23T11:46:00+09:00
default_theme: light
brand_color: "#0078D4"
primary_font: "Segoe UI Variable Text"
font_weight_normal: 400
token_prefix: "ds"

bold_direction: "Institutional Clarity"
aesthetic_category: "enterprise editorial"
signature_element: "blue-action-on-white-grid"
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "Public Microsoft homepage exposes real --ds-* typography/color/elevation tokens plus --uhf-* global header/footer tokens, but not a complete public designer guide."

colors:
  brilliant-blue-500: "#0078D4"
  uhf-link-blue: "#0067B8"
  surface-white: "#FFFFFF"
  sky-blue-50: "#F4FAFD"
  dark-blue-900: "#0E1726"
  sea-salt-100: "#F8F7F5"
  neutral-footer: "#F2F2F2"
  text-header: "#262626"
typography:
  display: "Segoe UI Variable Display"
  body: "Segoe UI Variable Text"
  small: "Segoe UI Variable Small"
  fallback: "Segoe UI, SegoeUI, Helvetica Neue, Helvetica, Arial, sans-serif"
  ladder:
    - { token: heading-3xl, size: "4.75rem", weight: 400, tracking: "-0.025em" }
    - { token: heading-2xl, size: "3.5rem", weight: 400, tracking: "-0.025em" }
    - { token: heading-xl, size: "3rem", weight: 500, tracking: "-0.025em" }
    - { token: heading-l, size: "2.5rem", weight: 500, tracking: "-0.025em" }
    - { token: heading-m, size: "2rem", weight: 500, tracking: "-0.025em" }
    - { token: body-m, size: "1rem", weight: 400, tracking: "-0.03em" }
    - { token: label-m, size: ".875rem", weight: 600, tracking: "normal" }
  weights_used: [400, 500, 600, 700]
  weights_absent: [800, 900]
components:
  global-header-link: { fg: "#262626", hover: "#D9D9D9", bg: "#FFFFFF", radius: "0" }
  primary-action: { bg: "#0067B8", fg: "#FFFFFF", weight: 600, radius: "2px to 4px" }
  ds-card: { bg: "#FEFEFE", border: "#E0E0E0", radius: "8px", shadow: "level-1 to level-2" }
  ai-assistant-panel: { bg: "#F4FAFD", accent: "#0078D4", radius: "16px", card_radius: "8px" }
---

# DESIGN.md - Microsoft

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Microsoft.com behaves less like a single campaign page and more like the arrivals hall of a large civic institution. Windows buyers, Microsoft 365 teams, Azure builders, Xbox customers, Surface shoppers, and support seekers all enter through the same concourse, but no single product is allowed to repaint the building. The page is a switchboard with daylight on it: white planes, compact labels, rectangular destinations, and blue contacts where the hand should press.

The dominant metaphor is not "blue technology brand"; it is a bright enterprise concourse with a strict wayfinding system. There is no second brand color roaming the UI, and even Microsoft logo colors stay out of the taxonomy. `#0078D4` (`{colors.brilliant-blue-500}`) and `#0067B8` (`{colors.uhf-link-blue}`) behave like airport gate numbers or Windows focus rings: highly visible at decision points, almost absent everywhere else. The brand is not a blue page. The brand is a white grid that knows where every door leads.

Typography is the operating system speaking in public. `Segoe UI Variable Display`, `Segoe UI Variable Text`, and `Segoe UI Variable Small` make the homepage feel like it belongs near Windows settings, Office ribbons, and admin portals rather than beside a boutique SaaS launch. The negative tracking is part of that institutional voice: text sits like tightly set UI chrome, not like loose magazine display type. If Apple removes the wall for the object, Microsoft keeps the wall and labels every room.

The card system feels like a product directory printed on rigid office signage: 8px corners, low system elevation, subtle borders, and enough image variety to separate destinations without turning the shell decorative. Shadow is infrastructure, not atmosphere. It is the faint edge of a tile on a white desk, not a cinematic spotlight.

AI expression is deliberately quarantined. `#F4FAFD` (`{colors.sky-blue-50}`), `#0E1726` (`{colors.dark-blue-900}`), and the blue-to-aqua accent belong inside assistant/product panels, like a lit demo bay inside the larger concourse. The glow never takes over the station. Microsoft lets Copilot have a room, not the whole building.

조금 더 풀면, Microsoft 홈은 **거대한 시연 실험실 옆에 펼쳐 놓은 공구함과 blueprint 도면**처럼 작동한다. 흰 페이지 바닥은 작업대 위 펼쳐진 blueprint 종이, 가로로 정렬된 product 카드들은 공구함의 뚜껑을 열었을 때 한 칸씩 제자리에 박혀 있는 도구 세트다. `#0067B8` 액션 블루는 공구함 위에 인쇄된 작업 라벨 — 어느 도구를 다음에 집어야 하는지 손가락이 먼저 알게 만드는 색이다. Copilot 패널은 실험실 한쪽에 따로 둔 시연 부스, blueprint 위에서 진행되는 라이브 demo이고, footer는 공구함 뒤편의 부속 부품 서랍이다. 두 번째 brand color가 없는 이유는, blueprint 위에는 단 한 가지 잉크 색만 살아 있어야 도면이 흔들리지 않기 때문이다.

### Key Characteristics

- White and very pale blue surfaces dominate; saturated blue is reserved for actions and selected accents.
- `Segoe UI Variable` is the identity carrier; do not swap it for a trendy geometric sans.
- Global header/footer use `--uhf-*` tokens while marketing/product modules expose `--ds-*` tokens.
- Headings use medium-light enterprise weight: 400 for largest display, 500/600 for section labels and controls.
- Cards are restrained: 8px radius, subtle borders, low two-layer elevation, no heavy glassmorphism.
- Navigation is dense but quiet, with many links kept in a strict horizontal product taxonomy.
- Product imagery and tiles create variety; the chrome itself stays plain.
- AI assistant surfaces introduce sky blue `#F4FAFD`, dark-blue ink `#0E1726`, and a blue-to-aqua gradient only inside that subsystem.
- Footer is utilitarian `#F2F2F2` with muted `#616161` text, not a brand finale.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Institutional Clarity
> **Aesthetic Category**: enterprise editorial
> **Signature Element**: 이 사이트는 **blue-action-on-white-grid**으로 기억된다.
> **Code Complexity**: high - multiple Microsoft systems coexist: global UHF header/footer, DS tokenized marketing modules, store modules, and assistant-specific components.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Microsoft처럼 만들기 - 3가지만 하면 80%

```css
/* 1. Font + optical weight */
body {
  font-family: "Segoe UI Variable Text", "Segoe UI", SegoeUI, "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
  letter-spacing: -0.03em;
}

/* 2. Surface + ink */
:root {
  --ms-bg: #FFFFFF;
  --ms-fg: #1A1A1A;
  --ms-muted: #616161;
}
body { background: var(--ms-bg); color: var(--ms-fg); }

/* 3. Action blue, not page blue */
:root { --ms-action: #0067B8; --ms-brand: #0078D4; }
.primary-action {
  background: var(--ms-action);
  color: #FFFFFF;
  font-weight: 600;
  border-radius: 2px;
}
```

**절대 하지 말아야 할 것 하나**: 전체 페이지를 `#0078D4` 그라디언트 브랜드 배경으로 덮지 말 것. Microsoft의 홈 chrome은 흰 표면과 정돈된 선택 구조가 먼저이고, blue는 행동 지점에만 강하게 들어간다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.microsoft.com/en-us` |
| Fetched | 2026-04-23T11:46:00+09:00 |
| Extractor | phase1 reuse: existing HTML/CSS/screenshots |
| HTML size | 362364 bytes |
| CSS files | 14 external files, total 676369 bytes |
| Screenshot | `insane-design/microsoft/screenshots/hero-cropped.png` |
| Token prefix | `ds`, with `uhf` and `sa` secondary systems |
| Method | Existing phase1 JSON + CSS token/frequency inspection; no new network fetch |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Microsoft public web stack with server-rendered HTML and multiple product bundles.
- **Design system**: Microsoft DS in use - prefix `--ds-*`; global shell uses `--uhf-*`; assistant/store modules add `--sa-*` and store-specific CSS.
- **CSS architecture**:
  ```css
  --ds-color-*                 palette ramps and semantic surfaces
  --ds-heading-* / --ds-body-* typography ladder
  --ds-spacing-*               spacing ladder
  --ds-elevation-*             low-elevation shadow system
  --uhf-*                      universal header/footer chrome
  --sa-*                       store assistant panel subsystem
  ```
- **Class naming**: mixed compiled product classes plus tokenized custom properties.
- **Default theme**: light (`#FFFFFF` primary document surface, `#F2F2F2` footer surface).
- **Font loading**: Segoe UI Variable family first, then Segoe UI and system/web fallbacks.
- **Canonical anchor**: Microsoft.com homepage global commerce/product navigation with cards for key consumer and business destinations.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Segoe UI Variable Display`
- **Body font**: `Segoe UI Variable Text`
- **Small text font**: `Segoe UI Variable Small`
- **Global header fallback**: `"Segoe UI", SegoeUI, "Helvetica Neue", Helvetica, Arial, sans-serif`
- **Weight normal / action / label**: `400` / `600` / `600`

```css
:root {
  --ds-font-family-segoe-variable-display: "Segoe UI Variable Display","Segoe UI",segoeui,"Helvetica Neue",helvetica,arial,sans-serif;
  --ds-font-family-segoe-variable-text: "Segoe UI Variable Text","Segoe UI",segoeui,"Helvetica Neue",helvetica,arial,sans-serif;
  --ds-font-family-segoe-variable-small: "Segoe UI Variable Small","Segoe UI",segoeui,"Helvetica Neue",helvetica,arial,sans-serif;
  --uhf-font-family: "Segoe UI", SegoeUI, "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```

### Note on Font Substitutes

If Segoe UI Variable is unavailable, use `"Segoe UI"` first, then `system-ui`, then `Arial`. Do not replace it with Inter as the default substitute unless the whole interface is being intentionally de-Microsofted. Inter's rhythm is cleaner but less Windows-native; it loses the familiar operating-system quality that makes the site feel official.

For Figma or web prototypes on macOS, the best substitute stack is:

```css
font-family: "Segoe UI", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
```

Avoid high-personality display faces, condensed sans faces, and overly rounded fonts. They push the page toward startup marketing rather than Microsoft institutional product navigation.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

### Principles

1. Let Segoe carry brand memory before color does.
2. Use large display type at 400 weight, then step into 500/600 for hierarchy and controls.
3. Keep optical tracking tight: headings around `-0.025em`, body around `-0.03em`.
4. Use labels as navigation instruments, not decorative eyebrow copy.
5. Maintain dense readability: line-height should feel practical, not editorially airy.

### Extracted Ladder

```css
:root {
  --ds-heading-3xl-font-size: 4.75rem;
  --ds-heading-3xl-font-weight: 400;
  --ds-heading-3xl-letter-spacing: -0.025em;

  --ds-heading-2xl-font-size: 3.5rem;
  --ds-heading-2xl-font-weight: 400;
  --ds-heading-2xl-letter-spacing: -0.025em;

  --ds-heading-xl-font-size: 3rem;
  --ds-heading-xl-font-weight: 500;
  --ds-heading-xl-letter-spacing: -0.025em;

  --ds-heading-l-font-size: 2.5rem;
  --ds-heading-l-font-weight: 500;
  --ds-heading-l-letter-spacing: -0.025em;

  --ds-heading-m-font-size: 2rem;
  --ds-heading-m-font-weight: 500;
  --ds-heading-m-letter-spacing: -0.025em;

  --ds-body-m-font-size: 1rem;
  --ds-body-m-font-weight: 400;
  --ds-body-m-letter-spacing: -0.03em;

  --ds-label-m-font-size: .875rem;
  --ds-label-m-font-weight: 600;
  --ds-label-m-letter-spacing: normal;
}
```

### Usage Notes

- `4.75rem` display size is appropriate for hero modules and major campaign bands only.
- Product-card headings should sit closer to `1.25rem` to `2rem`, with 500/600 weight.
- Header nav should remain compact, often 13-15px visual size, not enlarged for drama.
- CTA text should use 600, but not all-caps shouting.
- Body copy can be tighter than generic web defaults because the font was designed for UI density.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Core Palette

```css
:root {
  --ds-color-brilliant-blue-500: #0078D4;
  --uhf-action-blue: #0067B8;
  --ms-surface-white: #FFFFFF;
  --ds-color-sky-blue-50: #F4FAFD;
  --ds-color-dark-blue-900: #0E1726;
  --ds-color-sea-salt-100: #F8F7F5;
  --uhf-footer-background-color: #F2F2F2;
  --uhf-header-link-color: #262626;
}
```

### Frequency Signals

- `#FFF` / `#FFFFFF` - highest-frequency surface color; the homepage reads as a white system.
- `#0078D4` - primary Microsoft brilliant blue, heavily present in DS/assistant tokens.
- `#F4FAFD` - pale sky surface used for soft AI/assistant or blue-tinted modules.
- `#2A446F`, `#17253D`, `#0E1726` - dark blue ink family for AI/product panels.
- `#0067B8` - global UHF action/link blue, especially for header/cart/link behavior.
- `#F2F2F2`, `#E6E6E6`, `#D9D9D9` - footer/header neutral infrastructure.

### 06-8 Color Stories

1. **Action Blue: `#0078D4` / `#0067B8`** - This is the Microsoft interaction spine. Use it for buttons, selected links, and service emphasis. Keep it focused; widespread blue background makes the page feel like a support portal instead of Microsoft.com.
2. **White Surface: `#FFFFFF`** - The primary brand environment. White is not absence here; it is the institutional clearing where many product families can coexist.
3. **Sky Assistant Tint: `#F4FAFD`** - A soft blue-white used when the page needs AI/product warmth without turning saturated. Pair with `#0E1726` for readable dark-blue copy.
4. **Utility Neutral: `#F2F2F2` / `#262626`** - Header/footer and link chrome depend on practical neutrals. They keep the page from becoming a campaign-only layout.

### Color Behavior

Microsoft color usage is modular. The Microsoft four-color logo is not the UI palette. Do not extract red/green/yellow logo colors and spread them through cards. In this homepage surface, the working UI palette is white, neutral gray, Microsoft blue, and occasional product-media color.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

### Extracted Spacing Tokens

```css
:root {
  --ds-spacing-1: .125rem;  /* 2px */
  --ds-spacing-2: .25rem;   /* 4px */
  --ds-spacing-3: .5rem;    /* 8px */
  --ds-spacing-4: .75rem;   /* 12px */
  --ds-spacing-6: 1rem;     /* 16px */
  --ds-spacing-7: 1.5rem;   /* 24px */
  --ds-spacing-8: 2rem;     /* 32px */
  --ds-spacing-9: 3rem;     /* 48px */
  --ds-spacing-10: 3.5rem;  /* 56px */
}
```

### Whitespace Philosophy

Whitespace is functional rather than luxurious. Microsoft.com needs enough air for product scanning, but it cannot become sparse because the homepage is a switchboard for many journeys. Use whitespace to separate product families, not to perform elegance.

The site prefers clean gutters, predictable module rhythm, and restrained internal padding. Cards and product tiles should feel easy to compare side by side. Large blank editorial pauses are off-brand unless a specific hero campaign supplies strong product imagery.

### Layout Rhythm

- **Micro**: 2px/4px for icon alignment, focus correction, compact controls.
- **Component**: 8px/12px/16px for card padding, nav gaps, button padding.
- **Module**: 24px/32px/48px for tile groups and section separation.
- **Hero**: can expand beyond the token ladder, but should remain anchored to a product/content grid.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

### Radius Tokens and Observed Values

```css
:root {
  --border-radius-medium: 4px;
  --sa-border-radius: 16px;
  --sa-card-border-radius: 8px;
}

.ms-card { border-radius: 8px; }
.ms-control { border-radius: 2px; }
.ms-assistant-panel { border-radius: 16px; }
```

### Radius Rules

- Global navigation and classic Microsoft buttons should be squared or lightly rounded: 0-4px.
- Cards should usually use 8px, matching the dominant observed card radius.
- AI assistant or contained chat panels may use 16px outer radius and 8px internal cards.
- Avoid 24px-plus pill cards for core Microsoft homepage modules; they read too consumer-app playful.
- Circular radius is reserved for icons, avatars, and small controls, not product-card architecture.

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

Microsoft's elevation is quiet and systematic. Many declarations are `none`, but the DS includes a six-level elevation ladder built from two rgba layers: a small ambient outline and a vertical depth layer.

```css
:root {
  --ds-elevation-color-1: rgba(0,0,0,0.12);
  --ds-elevation-color-2: rgba(0,0,0,0.14);
  --ds-elevation-level-1:
    0 0 .125rem var(--ds-elevation-color-1),
    0 .063rem .125rem var(--ds-elevation-color-2);
  --ds-elevation-level-2:
    0 0 .125rem var(--ds-elevation-color-1),
    0 .125rem .25rem var(--ds-elevation-color-2);
  --ds-elevation-level-3:
    0 0 .125rem var(--ds-elevation-color-1),
    0 .25rem .5rem var(--ds-elevation-color-2);
}
```

Use shadows to clarify hover/stacking, not to create dramatic floating cards. A Microsoft card should feel physically present but administratively calm.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

Motion is present but not identity-defining in the captured CSS. It supports loading skeletons, hover states, dropdown reveal, and assistant panels. The most concrete motion token in the phase1 data is the skeleton duration:

```css
:root {
  --skeleton-animation-duration: 2s;
}
```

### Motion Rules

- Keep transitions short and utilitarian: hover, focus, dropdown, carousel, and skeleton states.
- Do not use scroll-jacking, large parallax, or cinematic section transitions as default Microsoft language.
- Product media may animate, but the navigation shell should remain dependable.
- Use motion to reduce uncertainty in dense product surfaces, not to entertain.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Global Header / UHF Shell

The Universal Header/Footer layer is a major part of the identity. It uses `--uhf-*` tokens, white header background, dense link groups, and practical hover states. Header links are `#262626`; footer surface is `#F2F2F2`; footer text is `#616161`.

```css
:root {
  --uhf-header-bg-color: #FFFFFF;
  --uhf-header-link-color: #262626;
  --uhf-footer-background-color: #F2F2F2;
  --uhf-footer-text-color: #616161;
}
```

### Product Tile Grid

The homepage uses modular product cards to route users into Microsoft 365, Copilot, Windows, Surface, Xbox, and business destinations. Cards should be scan-first: image or icon, short heading, short copy, clear action. Avoid card interiors that require reading long paragraphs.

### Editorial Hero

Hero sections can carry product photography or campaign imagery, but the surrounding system remains conservative. A Microsoft hero should feel like a product entry point, not a portfolio poster. Keep CTA grouping explicit and use blue action color.

### Footer Taxonomy

The footer is a dense support and legal taxonomy, not a decorative sign-off. Use muted gray, compact text, and multiple columns. This matters because Microsoft.com must service global corporate navigation.

---

## 12. Responsive
<!-- SOURCE: auto+manual -->

The system should collapse by preserving navigation priority and product-tile scan order. On desktop, keep a horizontal global nav plus wide module grids. On tablet, reduce columns and preserve CTA visibility. On mobile, the header becomes a menu/search surface and product modules stack into single-column cards.

```css
.ms-grid {
  display: grid;
  gap: 24px;
  grid-template-columns: repeat(4, minmax(0, 1fr));
}
@media (max-width: 1080px) {
  .ms-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 640px) {
  .ms-grid { grid-template-columns: 1fr; gap: 16px; }
}
```

Keep action buttons visible above the fold when possible. Do not let product imagery consume the only interactive area on mobile.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### 13-1 Core Component Families

**Global Header Link** - Compact text link in the UHF shell. Uses Segoe UI, `#262626`, white background, subtle hover state. It should not be styled as a large pill.

**Primary Action Button** - Blue, practical, 600 weight. Use `#0067B8` for classic UHF/action blue or `#0078D4` when aligned with DS brilliant blue. Radius should be small.

**Product Card** - White or near-white surface, 8px radius, subtle border/elevation, image or icon lead, concise heading, link/action.

**AI Assistant Panel** - Pale sky surface `#F4FAFD`, dark-blue copy `#0E1726`, blue accent `#0078D4`, 16px outer radius, 8px internal cards, optional blue-to-aqua gradient only for AI-specific marks.

**Footer Column** - `#F2F2F2` background, muted text, dense grouped links. The footer is information architecture, not brand decoration.

**Store/Product Module** - Uses retail/product imagery, price/action slots, and more commerce-like density, but should still inherit Microsoft typography and neutral surfaces.

### 13-2 Named Variants

```yaml
global-header-link:
  font: var(--uhf-font-family)
  color: "#262626"
  background: "#FFFFFF"
  hover: "#D9D9D9"
  radius: "0"

primary-action:
  background: "#0067B8"
  color: "#FFFFFF"
  font-weight: 600
  radius: "2px"
  padding: "10px 12px"

ds-card:
  background: "#FEFEFE"
  border: "#E0E0E0"
  radius: "8px"
  shadow: "var(--ds-elevation-level-1)"

assistant-card:
  background: "#F4FAFD"
  ink: "#0E1726"
  accent: "#0078D4"
  radius: "8px"

footer-column:
  background: "#F2F2F2"
  color: "#616161"
  link-color: "#616161"
```

### 13-3. Signature Micro-Specs

```yaml
uhf-blue-action-clamp:
  description: "Keep Microsoft blue as a decision-point affordance, not a page atmosphere."
  technique: "background #0067B8 or #0078D4, color #FFFFFF, font-weight 600, border-radius 2px to 4px, compact 10px-14px control padding"
  applied_to: ["{component.primary-action}", "{component.global-header-link}"]
  visual_signature: "Small rectangular blue actions punctuate an otherwise white enterprise grid."

segoe-optical-tightening-global:
  description: "Make the page feel Windows-native by combining Segoe Variable with dense optical tracking."
  technique: "font-family Segoe UI Variable Text/Display/Small; headings letter-spacing -0.025em; body letter-spacing -0.03em; display weights 400-500"
  applied_to: ["{typography.display}", "{typography.body}", "{component.ds-card}"]
  visual_signature: "Text sits compact and UI-like, as if it belongs beside OS controls rather than startup marketing."

assistant-sky-containment:
  description: "Constrain AI expression to a pale-blue subsystem instead of flooding the homepage chrome."
  technique: "panel background #F4FAFD, ink #0E1726, accent #0078D4, outer radius 16px, internal card radius 8px"
  applied_to: ["{component.ai-assistant-panel}", "{component.assistant-card}"]
  visual_signature: "Copilot-style energy appears as a contained demo bay inside the larger white Microsoft concourse."

low-elevation-card-edge:
  description: "Use card edges as quiet product taxonomy, not dramatic depth."
  technique: "background #FEFEFE, border #E0E0E0, radius 8px, shadow var(--ds-elevation-level-1) or 0 0 2px rgba(0,0,0,.12), 0 1px 2px rgba(0,0,0,.14)"
  applied_to: ["{component.ds-card}", "{component.Product Card}"]
  visual_signature: "Tiles read like rigid office signage on a white desk: visible, orderly, and low-drama."

uhf-zero-radius-link-row:
  description: "The Universal Header Footer keeps every navigation hit area perfectly square — no rounded corners, no pill, no badge geometry."
  technique: ".c-uhfh-actions a / .c-uhfh-link uses border-radius: 0; background #FFFFFF, fg #262626, hover bg #D9D9D9; underline appears only on focus-visible, not on hover; height matches a 48px global rail."
  applied_to: ["{component.global-header-link}", "{component.uhf-rail}"]
  visual_signature: "The top of the page reads like a Windows menu bar imported into the browser: rectangular, dense, and OS-native rather than marketing-soft."
```

---

## 14. Content Voice
<!-- SOURCE: manual -->

Microsoft copy should be direct, benefit-led, and product-specific. It can be aspirational around AI and productivity, but the voice should quickly name the product, audience, or task. Avoid poetic abstractions that could belong to any SaaS brand.

### Voice Rules

- Name concrete destinations: Microsoft 365, Copilot, Windows, Xbox, Surface, Azure.
- Use verbs around productivity and capability: create, protect, organize, build, play, learn.
- Keep CTA labels plain: "Shop now", "Learn more", "Compare plans", "Get started".
- Avoid founder-led personality copy, ironic humor, or boutique editorial fragments.

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
:root {
  --ms-blue: #0078D4;
  --ms-action-blue: #0067B8;
  --ms-bg: #FFFFFF;
  --ms-footer-bg: #F2F2F2;
  --ms-text: #1A1A1A;
  --ms-header-text: #262626;
  --ms-muted: #616161;
  --ms-sky-50: #F4FAFD;
  --ms-dark-blue: #0E1726;
  --ms-border: #E0E0E0;
  --ms-radius-card: 8px;
  --ms-radius-control: 2px;
  --ms-shadow-1: 0 0 2px rgba(0,0,0,.12), 0 1px 2px rgba(0,0,0,.14);
  --ms-font: "Segoe UI Variable Text", "Segoe UI", SegoeUI, "Helvetica Neue", Arial, sans-serif;
  --ms-font-display: "Segoe UI Variable Display", "Segoe UI", SegoeUI, "Helvetica Neue", Arial, sans-serif;
}

body {
  margin: 0;
  background: var(--ms-bg);
  color: var(--ms-text);
  font-family: var(--ms-font);
  font-weight: 400;
  letter-spacing: -0.03em;
}

.ms-shell {
  min-height: 100vh;
  background: var(--ms-bg);
}

.ms-header {
  height: 54px;
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 0 5vw;
  background: #FFFFFF;
  color: var(--ms-header-text);
  font-size: 13px;
}

.ms-hero {
  display: grid;
  grid-template-columns: minmax(280px, 520px) minmax(320px, 1fr);
  gap: 48px;
  align-items: center;
  padding: 56px 5vw;
}

.ms-hero h1 {
  margin: 0 0 20px;
  font-family: var(--ms-font-display);
  font-size: clamp(2.5rem, 6vw, 4.75rem);
  line-height: 1.08;
  font-weight: 400;
  letter-spacing: -0.025em;
}

.ms-hero p {
  max-width: 58ch;
  margin: 0 0 24px;
  font-size: 1.125rem;
  line-height: 1.5;
}

.ms-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 40px;
  padding: 10px 14px;
  border-radius: var(--ms-radius-control);
  background: var(--ms-action-blue);
  color: #FFFFFF;
  font-weight: 600;
  text-decoration: none;
}

.ms-card-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 24px;
  padding: 32px 5vw 56px;
}

.ms-card {
  background: #FEFEFE;
  border: 1px solid var(--ms-border);
  border-radius: var(--ms-radius-card);
  box-shadow: var(--ms-shadow-1);
  padding: 24px;
}

.ms-card h2 {
  margin: 0 0 12px;
  font-size: 1.25rem;
  line-height: 1.25;
  font-weight: 500;
  letter-spacing: -0.01em;
}

.ms-assistant-panel {
  background: var(--ms-sky-50);
  color: var(--ms-dark-blue);
  border-radius: 16px;
  padding: 24px;
}

.ms-footer {
  background: var(--ms-footer-bg);
  color: var(--ms-muted);
  padding: 36px 5vw;
  font-size: 12px;
}

@media (max-width: 900px) {
  .ms-hero { grid-template-columns: 1fr; padding-block: 40px; }
  .ms-card-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

@media (max-width: 640px) {
  .ms-header { padding-inline: 16px; gap: 16px; }
  .ms-card-grid { grid-template-columns: 1fr; padding-inline: 16px; }
}
```

---

## 16. Tailwind Mapping
<!-- SOURCE: manual -->

```js
export default {
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Segoe UI Variable Text"', '"Segoe UI"', 'system-ui', 'sans-serif'],
        display: ['"Segoe UI Variable Display"', '"Segoe UI"', 'system-ui', 'sans-serif'],
      },
      colors: {
        microsoft: {
          blue: '#0078D4',
          action: '#0067B8',
          sky: '#F4FAFD',
          ink: '#0E1726',
          footer: '#F2F2F2',
          headerText: '#262626',
          muted: '#616161',
        },
      },
      borderRadius: {
        ms: '2px',
        'ms-card': '8px',
        'ms-panel': '16px',
      },
      boxShadow: {
        'ms-1': '0 0 2px rgba(0,0,0,.12), 0 1px 2px rgba(0,0,0,.14)',
      },
      letterSpacing: {
        msbody: '-0.03em',
        msheading: '-0.025em',
      },
    },
  },
}
```

---

## 17. Agent Prompt
<!-- SOURCE: manual -->

Build a Microsoft.com-inspired homepage surface, not a generic blue SaaS landing page. Use a white institutional shell, Segoe UI Variable typography, compact global navigation, product-card grids, and blue only for actions or contained product accents. Use `#0067B8` and `#0078D4` as focused interaction colors, not full-page atmosphere. Cards should use 8px radius, subtle borders, and low two-layer elevation. The footer should be a dense `#F2F2F2` taxonomy with muted text. Keep copy direct and product-specific. Avoid logo-color confetti, oversized rounded pills, glass blobs, and decorative gradients.

Must include:

- Segoe UI Variable or Segoe UI fallback stack.
- White primary surface `#FFFFFF`.
- Microsoft blue action `#0067B8` or brilliant blue `#0078D4`.
- Compact header with product navigation.
- Product cards with 8px radius.
- Optional assistant panel using `#F4FAFD`, `#0E1726`, and `#0078D4`.
- Footer taxonomy using `#F2F2F2` and `#616161`.

---

## 18. DO / DON'T
<!-- SOURCE: auto+manual -->

### DO

- Use `Segoe UI Variable Text` / `Segoe UI Variable Display` before generic system fonts.
- Keep the page background primarily `#FFFFFF`.
- Use `#0067B8` and `#0078D4` for clear actions, links, and selected product accents.
- Use 8px card radius and 2px-4px button/control radius.
- Keep body weight at 400 and action/label weight at 600.
- Use negative optical tracking: around `-0.025em` for headings and `-0.03em` for body tokens.
- Treat footer and utility navigation as real information architecture.
- Let product imagery and modular cards provide variety instead of decorative page chrome.

### DON'T

- 배경을 `#0078D4` 또는 `#0067B8` 풀페이지 브랜드 블루로 두지 말 것 - 대신 기본 표면은 `#FFFFFF` 사용.
- 텍스트를 `#000000` 순흑으로 고정하지 말 것 - 대신 header/link에는 `#262626`, dark-blue panel에는 `#0E1726` 사용.
- Footer를 `#FFFFFF`로 방치하지 말 것 - Microsoft utility footer는 `#F2F2F2`와 `#616161` 조합이 맞다.
- Assistant/AI 패널 배경을 `#FFFFFF`만으로 만들지 말 것 - 포함된 AI 표면은 `#F4FAFD`가 핵심 단서다.
- CTA를 보라색 `#7C3AED`나 startup gradient로 바꾸지 말 것 - Microsoft action은 `#0067B8` 또는 `#0078D4` 계열이다.
- Card radius를 `24px` 이상으로 키우지 말 것 - 기본 product card는 `8px`, control은 `2px`-`4px`다.
- body에 `font-weight: 500` 이상을 기본값으로 쓰지 말 것 - 본문 기본은 `400`, action/label만 `600`이다.
- Inter를 기본 brand font로 선언하지 말 것 - Segoe UI 계열이 Microsoft 표면의 핵심이다.
- Microsoft logo의 red/green/yellow를 UI 카드 accent로 흩뿌리지 말 것 - 실제 homepage UI는 white/neutral/blue 중심이다.
- Heavy shadow `0 20px 60px rgba(0,0,0,.25)`를 card 기본값으로 쓰지 말 것 - low elevation `rgba(0,0,0,.12/.14)` 두 레이어를 사용.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **Full-bleed saturated blue background: zero** — page는 blueprint 흰 종이 위에 시연. brand wash는 absent.
- **Purple/indigo SaaS gradients: none** — 보라/인디고 wrapper는 공구함 어디에도 zero. mesh gradient는 absent.
- **Large rounded pill cards everywhere: never** — module 기본 radius는 8px, pill은 utility에 한정되고 일반 카드에는 absent.
- **Boutique editorial serif headlines: absent** — Segoe UI Variable 한 가족이 시연실 전체를 담당. serif 헤드라인은 zero.
- **Logo-color confetti as UI taxonomy: none** — Microsoft logo의 red/green/yellow를 chrome에 흩뿌리는 일은 absent. blueprint 잉크는 단색.
- **Aggressive glassmorphism / floating translucent orbs: zero** — 작업대 위 떠 있는 유리 카드는 absent. surface는 종이처럼 평면.
- **Dark-mode-first marketing chrome: never** — 공개 홈페이지는 흰 시연실 기본, dark-mode landing은 absent.
- **Heavy cinematic parallax: zero** — section transition은 정적 도구함 열림에 가깝다. parallax 시연은 none.
- **Founder/personality microcopy: absent** — 페이지는 인물이 아니라 시연 결과를 말한다. founder voice는 never.
- **Decorative shadows as depth language: zero** — elevation은 두 레이어 low-shadow 인프라일 뿐, 장식 그림자는 absent.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- Phase1 JSON token extraction reported zero resolved variables, but CSS inspection found substantial `--ds-*`, `--uhf-*`, and `--sa-*` custom properties. This guide treats the CSS as the stronger evidence source.
- The existing capture is from 2026-04-23, while this report is authored on 2026-05-03. Microsoft.com is campaign-driven, so hero content and product ordering may have changed.
- The homepage mixes several Microsoft systems. This report describes the public Microsoft.com homepage surface, not Fluent 2 documentation, Azure portal UI, Windows app UI, or Microsoft Learn.
- The screenshot evidence is limited to `hero-cropped.png`; component behavior such as dropdown motion, carousel states, and hover menus was inferred from CSS and HTML structure rather than fresh browser interaction.
- Exact hero imagery and copy are intentionally treated as variable campaign content. The stable system is typography, white/blue/neutral color behavior, header/footer shell, cards, and low-elevation restraint.
- Some CSS belongs to store assistant or retail modules and should not be generalized to the whole site. `--sa-*` tokens are only used for assistant-like contained panels in this guide.
