---
schema_version: 3.2
slug: discord
service_name: Discord
site_url: https://discord.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: dark
brand_color: "#5865F2"
primary_font: Abcgintodiscord
font_weight_normal: 400
token_prefix: discord

bold_direction: Playful Console
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: landing-utility
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "Marketing Webflow layer plus extensive app token corpus: 4167 custom properties, 203 resolved tokens, and component aliases for buttons, cards, and inputs."

colors:
  brand: "#5865F2"
  focus-primary: "#4D65FF"
  not-quite-black: "#23272A"
  white: "#FFFFFF"
  old-brand: "#7289DA"
  hero-deep-plum: "#1F1D5D"
  success: "#43B581"
  warning: "#FAA61A"
  error: "#F04747"
  link: "#00AFF7"
  surface-soft: "#F6F6F6"
  dark-panel: "#2C2F33"
typography:
  display: "Abcgintonord 800"
  body: "Abcgintodiscord"
  ui: "Ggsans"
  code: "Ggsansmono"
  ladder:
    - { token: hero-h1, size: "clamp(48px, 6vw, 76px)", weight: 800, tracking: "0em" }
    - { token: section-title, size: "clamp(32px, 4vw, 56px)", weight: 800, tracking: "0em" }
    - { token: body-large, size: "20px", weight: 400, tracking: "0em" }
    - { token: nav, size: "16px", weight: 600, tracking: "0em" }
    - { token: small-ui, size: "14px", weight: 400, tracking: "0em" }
  weights_used: [300, 400, 500, 600, 700, 800]
  weights_absent: [200, 900]
components:
  hero-button-white: { bg: "{colors.white}", color: "{colors.not-quite-black}", radius: "16px", padding: "16px 32px" }
  hero-button-blurple: { bg: "{colors.brand}", color: "{colors.white}", radius: "16px", padding: "16px 32px" }
  app-button-brand: { bg: "{colors.brand}", color: "{colors.white}", radius: "3px", padding: "15px 25px" }
  app-button-dark: { bg: "{colors.not-quite-black}", color: "{colors.white}", radius: "3px", padding: "15px 25px" }
---

# DESIGN.md — Discord (Claude Code Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Discord stages its homepage like a midnight theater where the monitors have replaced the stage lights: a deep blue-violet gradient occupies the arena, a large angled app mockup anchors center-left, mascot characters and floating doodles fill the wings, and blunt white type runs the marquee. The first impression is theatrical, but the system underneath is more disciplined than the illustrations suggest.

The key accent is blurple, but it is not sprayed everywhere. There is no second equal brand color. The hero lets the atmosphere move from near-black into saturated blue-violet, then reserves #5865F2 (`{colors.brand}`) for the browser CTA and system states. White is the real workhorse: logo, nav, headline, body copy, and the download CTA all sit on the same dark field. The white CTA is almost a lit keyboard key on the desk; the blurple CTA is the only glowing system button on stage. This is why a Discord-like page fails quickly when the background becomes plain #FFFFFF or when blurple becomes a generic gradient wash.

Typography is the main voice. The hero headline uses the heavy Nord/Ginto family as a compressed poster face, with all-caps words stacked in short hard lines. It reads less like a SaaS value proposition and more like the title card of a co-op game trailer: big, blunt, white, and impossible to demote. Body copy relaxes into Abcgintodiscord/Ginto proportions, but it remains bright and friendly. Navigation is also unusually chunky for a marketing site: 16px-ish labels at 600 weight, not tiny gray SaaS links.

The layout metaphor is "chat room as theater stage." The product UI is visible as a real dark app surface, but it is embedded among props: controller, characters, device mockups, stickers, soft stars, and floating objects. Shadow is not the hero's depth engine; the room is built from layered illustration, tilted screens, and the not-quite-black app shell #23272A (`{colors.not-quite-black}`). The mockup behaves like a broadcast overlay from a friends-only stream rather than a polished enterprise screenshot.

The page sells belonging and play before it sells features. The technical contract is simple: build one immersive dark theater, put heavy white type on the left, place product imagery and characters on the right, and let rounded pill CTAs sit below as the conversion controls. No editorial parchment, no dashboard — this is a concert-hall arena where the product is always live.

### Key Characteristics

- Deep blue-violet hero field anchored by near-black edges and saturated blurple center light.
- Heavy all-caps Ginto/Nord display type, stacked in compact short lines.
- White foreground dominates the hero: nav, logo, headline, copy, and download button.
- Product UI appears as a tilted dark desktop app mockup, not as abstract screenshots.
- Mascot/character props are part of the composition, not decorative side icons.
- Primary interaction color is #5865F2 (`{colors.brand}`); legacy #7289DA appears in older app/button CSS but is not the modern homepage anchor.
- Buttons are large rounded rectangles in the hero, while older app-style buttons remain small-radius 3px controls.
- Motion hooks exist through Webflow `data-w-id` transforms, opacity staging, and a 0.5px blur treatment on hero imagery.
- The design accepts playful illustration, but rejects pastel softness: contrast stays high and the stage stays dark.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Playful Console
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **dark blurple game-room hero with chunky white Nord headline and tilted Discord UI tableau**으로 기억된다.
> **Code Complexity**: high — Webflow marketing CSS is layered on top of a large Discord token corpus with 4167 custom properties and app component aliases.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Discord처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Abcgintodiscord", "Ggsans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}

.hero-title {
  font-family: "Abcgintonord 800", "ABC Ginto Nord", "Arial Black", sans-serif;
  font-weight: 800;
  text-transform: uppercase;
  line-height: .9;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #050614; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #5865F2; }
.button-primary { background: var(--brand); color: #FFFFFF; }
```

**절대 하지 말아야 할 것 하나**: Discord를 흰 SaaS 랜딩으로 바꾸지 말 것. 이 홈페이지의 80%는 #FFFFFF 텍스트가 dark blurple stage 위에 놓이는 관계다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://discord.com` |
| Fetched | 2026-05-03T00:00:00+09:00 |
| Extractor | reused phase1 assets: HTML + CSS + screenshot |
| HTML size | 157609 bytes (Webflow marketing page) |
| CSS files | 3 files, total 3163497 bytes |
| Token prefix | `discord` |
| Method | CSS custom properties, phase1 JSON, HTML head metadata, and hero screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Webflow marketing layer (`data-wf-domain="prod-wf1.discord.com"`, `w-mod-js`, `data-w-id` animation hooks)
- **Design system**: Discord token corpus — mixed root names rather than one clean namespace
- **CSS architecture**:
  ```text
  marketing layer   (.nav_*, .hero_*, .language_*)        Webflow page CSS
  app token layer   (--brand, --neutral-*, --blurple-*)   Discord UI tokens
  component aliases (--button-*, --card-*, --input-*)     reusable app component semantics
  ```
- **Class naming**: Webflow readable classes mixed with generated app selectors such as `.buttonBrand-24ECS3`
- **Default theme**: dark hero marketing page (visual bg = deep blue/plum, app bg = #23272A / #2C2F33)
- **Font loading**: Webflow font definitions plus Google WebFont loader for decorative Poppins / Press Start 2P side assets
- **Canonical anchor**: Homepage hero screenshot: left all-caps headline, right angled Discord app mockup, bottom dual CTA row

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Abcgintonord 800` / `ABC Ginto Nord` family (proprietary brand face)
- **Body font**: `Abcgintodiscord`, `ABC Ginto Normal`, `Ggsans`
- **Code font**: `Ggsansmono`, with `Source Code Pro` appearing in CSS
- **Weight normal / bold**: `400` / `800` for hero display, `600` for nav and emphasis

```css
:root {
  --discord-font-family:       "Abcgintodiscord", "Ggsans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --discord-font-family-code:  "Ggsansmono", "Source Code Pro", ui-monospace, SFMono-Regular, monospace;
  --discord-font-display:      "Abcgintonord 800", "ABC Ginto Nord", "Arial Black", sans-serif;
  --discord-font-weight-normal: 400;
  --discord-font-weight-bold:   800;
}
body {
  font-family: var(--discord-font-family);
  font-weight: var(--discord-font-weight-normal);
}
```

### Note on Font Substitutes

- **Display substitute** — Use `Arial Black` or `Archivo Black` only for the hero headline, not for body text. Keep `text-transform: uppercase`, `line-height: .88-.94`, and avoid negative tracking; the screenshot reads chunky rather than tightly kerned.
- **Body substitute** — Use `Inter` or `Noto Sans` at 400/600 when Ginto/GG Sans is unavailable. Raise line-height slightly to `1.35-1.45` because the brand face is wide and open.
- **UI substitute** — Use `system-ui` for nav and buttons at 600. Do not use a thin 400 navigation; Discord's nav labels are part of the friendly weight of the header.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `hero-h1` | `clamp(48px, 6vw, 76px)` | 800 | `.88-.94` | `0em` |
| `section-title` | `clamp(32px, 4vw, 56px)` | 800 | `.95-1.05` | `0em` |
| `hero-body` | `20px` | 400 | `1.35-1.45` | `0em` |
| `nav-link` | `16px` | 600 | `1.2` | `0em` |
| `button-label` | `18px` | 400-600 | `1.2` | `0em` |
| `small-ui` | `14px` | 400 | `18px` | `0em` |

> ⚠️ Discord's hero voice comes from weight, casing, and line stacking; do not fake it with negative tracking or condensed generic fonts.

### Principles

1. Hero display is poster typography: uppercase, heavy, short lines, and deliberately blunt rhythm.
2. Body copy stays friendly and large enough to read on a dark stage; 16px SaaS body text looks too timid here.
3. Navigation is part of the brand voice, so links stay white and semibold rather than muted gray.
4. The system uses multiple brand faces (`Abcgintodiscord`, Ginto, Ggsans) because marketing and app UI coexist.
5. Decorative fonts such as `Press Start 2P` are incidental; they are not the main Discord voice.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed anchors)

| Token | Hex |
|---|---|
| `--brand` | `#5865F2` |
| legacy brand button | `#7289DA` |
| brand hover legacy | `#697EC4` |
| button hover | `#8891F2` |
| focus outline | `#4D65FF` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--not-quite-black` | `#23272A` |
| app dark panel | `#2C2F33` |
| hero gradient shadow | `#1F1D5D` |
| dark button hover | `#3B3B3B` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| text-on-dark | `#FFFFFF` | `#23272A` |
| soft section | `#F6F6F6` | `#2C2F33` |
| hairline alpha | `#FFFFFF10` | `#0000001A` |
| muted runtime | `#B2B2B2` | `#747F8D` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| success | button success | `#43B581` |
| warning | button warning | `#FAA61A` |
| error | button error | `#F04747` |
| link | inline link | `#00AFF7` |
| premium pink | decorative/runtime | `#FF6AEF` |
| premium purple | decorative/runtime | `#B377F3` |
| mint | decorative/runtime | `#15F5BA` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--brand` | `#5865F2` | primary CTA, brand button, hover color on white button |
| `--white` | `#FFFFFF` | hero text, nav text, white button background |
| `--not-quite-black` | `#23272A` | dark button, text on white button, app surface |
| `--button-hover` | `#8891F2` | lighter blurple hover |
| `--dark-button-hover` | `#3B3B3B` | dark utility button hover |
| `focus-visible` | `#4D65FF` | keyboard outline |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--button-outline-brand-background-hover` | `--brand-500` | outline brand hover |
| `--button-outline-brand-border-active` | `--brand-560` | outline active border |
| `--button-outline-primary-text` | `--white` | outline button text |
| `--card-background-default` | `--neutral-64` / `--neutral-79` family | app card surface |
| `--input-border-active` | `--blurple-50` | active input focus |
| `--input-border-default` | `--neutral-29` | default input border |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| black shorthand | `#000` | 1154 |
| white shorthand | `#FFF` | 568 |
| brand | `#5865F2` | 229 |
| white alpha | `#FFFFFF1A` | 136 |
| transparent black | `#0000` | 135 |
| not-quite-black | `#23272A` | 127 |
| soft surface | `#F6F6F6` | 92 |
| transparent white | `#FFF0` | 82 |

### Color Stories

**`{colors.brand}` (`#5865F2`)** — Modern Discord blurple. It is the primary interaction anchor, especially on the browser CTA and app brand button. Use it as a decisive button/background color, not as a low-opacity haze across the whole UI.

**`{colors.white}` (`#FFFFFF`)** — The hero's actual foreground system. Logo, nav, headline, body copy, and the Mac download button all rely on bright white to keep the dark stage crisp.

**`{colors.not-quite-black}` (`#23272A`)** — The app and dark utility anchor. It appears as button/background/text contrast in the app-layer CSS and keeps the UI recognizably Discord rather than generic navy.

**`{colors.hero-deep-plum}` (`#1F1D5D`)** — The shadow color behind the playful stage. It appears in a hero button overlay gradient and matches the screenshot's dark violet depth. Treat it as atmosphere, not a brand replacement.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `hero-outer-x` | `40px-100px` | desktop hero content inset |
| `hero-top` | `96px-128px` | stage breathing room below nav |
| `hero-gap` | `48px-80px` | copy/image separation |
| `cta-gap` | `24px` | dual hero buttons |
| `section-lg` | `88px-120px` | large marketing bands |
| `section-md` | `56px-72px` | content sections |
| `component-md` | `16px-24px` | cards, nav dropdowns, buttons |
| `tiny-control` | `8px-12px` | dropdown rows and small UI |

**주요 alias**:
- `--mobile-messages-header-button-gap` → app mobile header button spacing (value not resolved in phase1)
- `--chat-input-icon-size` → app input control sizing (value not resolved in phase1)
- `--control-input-height-md` → form control height alias (value not resolved in phase1)

### Whitespace Philosophy

Discord's homepage gives the hero a lot of stage space, but it is not quiet whitespace. The air is filled with soft stars, floating shapes, character props, and product imagery. The left text block remains clean because the visual density is pushed right and upward.

Below the hero, spacing should stay chunky rather than delicate. Think 24px button gaps, 56px+ section rhythm, and large visual modules. A tight enterprise dashboard rhythm makes the page feel wrong because Discord is selling hangout energy, not efficiency.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| `hero-button-radius` | `16px` | homepage hero CTAs |
| `language-dropdown-radius` | `8px` | locale dropdown |
| `legacy-app-button-radius` | `3px` | older app-style `.button` controls |
| `card-radius-sm` | `8px` | repeated app/card surfaces |
| `card-radius-md` | `12px-16px` | modern cards and containers |
| `pill-radius` | `60px / 1000px / 2147483647px` | fully rounded pills and avatar/icon circles |
| `circle` | `50%` | avatar, icon, radial props |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| language-dropdown | `0 1px 1px rgb(0 0 0 / 10%)` | small menu elevation |
| focus ring | `0 0 0 3px #00B0F4` in app CSS, outline `0.125rem solid #4D65FF` in marketing CSS | keyboard navigation |
| hero depth | image composition + dark gradient rather than box-shadow | product mockup and characters |
| white/black alpha | `#FFFFFF1A`, `#0000001A` | separators and soft overlays |

Discord does not rely on SaaS card shadows in the hero. Depth comes from illustration layering, angled product mockups, and dark-to-blurple atmosphere.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| Webflow opacity staging | `opacity: 0` initial states on many `data-w-id` elements | entrance/reveal choreography |
| hero image soften | `filter: blur(0.5px)` on a hero asset state | depth/atmosphere |
| translate staging | `translate3d(0, -10px, 0)` and `translate3d(0%, 0, 0)` | hero object animation |
| button color transition | `transition: color 0.3s ease`, `.12s ease-out` legacy buttons | hover affordance |
| transform preserve | `transform-style: preserve-3d` | Webflow 3D-ish staged objects |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: roughly `1180px-1280px` visual hero content
- **Grid type**: asymmetric two-column hero: left text, right product tableau
- **Column count**: 2 major hero zones, then modular section bands
- **Gutter**: `48px-80px` in hero, `24px` in CTA groups

### Hero
- **Pattern Summary**: `~100vh + dark blurple illustrated stage + left stacked H1 + product tableau right + dual CTA below`
- Layout: header above, left headline/copy, right large app mockup with characters, CTA row centered/lower across the hero
- Background: deep blue-violet gradient with near-black edge, soft star/doodle assets
- **Background Treatment**: image/illustration overlay on dark gradient; not a pure CSS gradient-only hero
- H1: `clamp(48px, 6vw, 76px)` / weight `800` / tracking `0em`
- Max-width: visual content around `1180px-1280px`

### Section Rhythm

```css
section {
  padding: 88px 40px;
  max-width: 1280px;
}
```

### Card Patterns
- **Card background**: app surfaces use `#23272A`, `#2C2F33`, or neutral token aliases; marketing light cards may use `#F6F6F6`
- **Card border**: often absent in hero; app/input states use tokenized borders like `--neutral-29`
- **Card radius**: `8px`, `12px`, `16px`, with big illustrated modules going larger
- **Card padding**: `16px-32px`
- **Card shadow**: minimal; depth is usually imagery or overlay alpha

### Navigation Structure
- **Type**: horizontal marketing nav with dropdown labels
- **Position**: absolute/top overlay on dark hero
- **Height**: visually around `72px-88px`
- **Background**: transparent over hero
- **Border**: none; mobile burger content uses `#FFFFFF10` separators

### Content Width
- **Prose max-width**: `420px-520px` in hero
- **Container max-width**: `1180px-1280px`
- **Sidebar width**: not applicable for homepage; app mockup contains its own sidebar visual

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `< 768px` | stack hero, collapse nav into burger |
| Tablet | `768px-991px` | Webflow tablet animation branch visible in inline CSS |
| Desktop | `>= 992px` | full hero tableau and desktop nav |
| Large | `>= 1280px` | maintain centered content, avoid stretching headline |

### Touch Targets
- **Minimum tap size**: `44px+` for mobile nav/buttons
- **Button height (mobile)**: `52px-56px`
- **Input height (mobile)**: app aliases exist, but exact resolved values were not captured

### Collapsing Strategy
- **Navigation**: desktop horizontal links collapse to burger/menu; mobile menu rows use 24px vertical padding and `#FFFFFF10` separators
- **Grid columns**: hero becomes stacked, with illustration reduced or reordered
- **Sidebar**: no page sidebar; product mockup remains image content
- **Hero layout**: text remains first, CTA buttons stack or wrap below

### Image Behavior
- **Strategy**: responsive Webflow assets and staged absolute/relative illustration layers
- **Max-width**: product image should be capped so it does not crush left copy
- **Aspect ratio handling**: preserve product mockup ratio; crop atmosphere before cropping app UI

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

| Variant | Background | Text | Radius | Padding | Notes |
|---|---|---|---:|---:|---|
| hero download | `#FFFFFF` | `#23272A` | `16px` | `16px 32px` | includes download icon, primary install action |
| hero browser | `#5865F2` | `#FFFFFF` | `16px` | `16px 32px` | browser/open action, main blurple CTA |
| app brand | `#5865F2` | `#FFFFFF` | `3px` | `15px 25px` | `.buttonBrand-24ECS3` / legacy app button style |
| app white | `#FFFFFF` | `#23272A` | `3px` or local radius | component CSS hover turns text `#5865F2` |
| app dark | `#23272A` | `#FFFFFF` | `3px` | `15px 25px` | dark utility action |
| state success | `#43B581` | `#FFFFFF` | `3px` | `15px 25px` | older app state button |
| state warning | `#FAA61A` | `#FFFFFF` | `3px` | `15px 25px` | older app state button |
| state error | `#F04747` | `#FFFFFF` | `3px` | `15px 25px` | older app state button |

```html
<a class="discord-hero-button discord-hero-button--download" href="#">
  <span class="icon-download"></span>
  Download for Mac
</a>
<a class="discord-hero-button discord-hero-button--browser" href="#">
  Open Discord in your browser
</a>
```

### Badges

Discord's current homepage hero does not use badge-first SaaS labeling. Avoid eyebrow chips above the hero headline. When badge-like UI is needed in app surfaces, keep radius high, text 12px-14px, and use brand/accent tokens sparingly.

### Cards & Containers

| Pattern | Background | Border | Radius | Shadow |
|---|---|---|---:|---|
| product mockup panel | `#23272A` / dark UI screenshot | none or embedded UI hairlines | screenshot-native | image depth |
| app card | tokenized neutral surface (`--card-background-default`) | tokenized neutral | `8px-16px` | minimal |
| light marketing band | `#F6F6F6` | none | `16px-32px` | none/soft |
| dropdown | `#FFFFFF` | none | `8px` | `0 1px 1px rgb(0 0 0 / 10%)` |

### Navigation

Navigation uses white text directly over the dark hero. Labels are semibold and simple: Download, Nitro, Discover, Safety, Quests, Support, Blog, Developers, Careers. Dropdown indicators are small chevrons; do not add boxed nav items or gray pill backgrounds.

### Inputs & Forms

The homepage hero does not expose form fields. App-layer CSS shows input aliases:

| Alias | Purpose |
|---|---|
| `--input-background-default` | default input surface |
| `--input-background-error-default` | error state surface |
| `--input-border-default` | neutral border |
| `--input-border-active` | blurple active border |
| `--form-input-height` | form height alias, unresolved in phase1 |

### Hero Section

The hero is the signature component. Build it as a dark full-width stage with the nav inside the same visual world. Keep the H1 left aligned, max it around 500px, and place the product tableau to the right. CTAs should be visually lower than the text block and large enough to feel consumer-app friendly.

### 13-2. Named Variants

#### `hero-button-white-download`

| Property | Value |
|---|---|
| bg | `#FFFFFF` |
| color | `#23272A` |
| radius | `16px` |
| min-height | `56px` |
| affordance | icon + label |
| hover | slight lift or text/opacity change only |

#### `hero-button-blurple-browser`

| Property | Value |
|---|---|
| bg | `#5865F2` |
| color | `#FFFFFF` |
| radius | `16px` |
| min-height | `56px` |
| affordance | text label |
| hover | lighter blurple, compatible with `#8891F2` |

#### `app-button-brand-compact`

| Property | Value |
|---|---|
| bg | `#5865F2` |
| color | `#FFFFFF` |
| radius | `3px` |
| padding | `15px 25px` |
| source | `.buttonBrand-24ECS3`, `section .button.brand` lineage |

### 13-3. Signature Micro-Specs

```yaml
blurple-night-stage:
  description: "Immersive dark hero field that makes the page feel like a shared game room."
  technique: "near-black edge field plus saturated blue-violet/plum center; anchor interaction remains #5865F2 /* {colors.brand} */ rather than a full-page purple wash"
  applied_to: ["{component.hero-section}", "{component.hero-button-blurple}"]
  visual_signature: "the homepage opens as a dark social stage, not a white SaaS canvas"

nord-stack-title-card:
  description: "Poster-like Discord headline voice built from weight and line stacking."
  technique: "Abcgintonord 800 / ABC Ginto Nord, text-transform: uppercase, line-height .88-.94, letter-spacing: 0, color #FFFFFF /* {colors.white} */"
  applied_to: ["{component.hero-section}", "{typography.ladder.hero-h1}"]
  visual_signature: "a co-op game trailer title card: blunt white blocks, short lines, no thin gray marketing type"

dual-radius-cta-language:
  description: "Homepage CTAs are friendly large controls while app-layer buttons stay compact and rectangular."
  technique: "hero buttons use border-radius: 16px, min-height ~56px, padding 16px 32px; app buttons use border-radius: 3px with padding 15px 25px"
  applied_to: ["{component.hero-button-white}", "{component.hero-button-blurple}", "{component.app-button-brand}", "{component.app-button-dark}"]
  visual_signature: "consumer-app invitation in the hero, Discord app utility in the embedded UI layer"

not-quite-black-app-tableau:
  description: "Product depth comes from Discord's charcoal app shell, not generic card elevation."
  technique: "use #23272A /* {colors.not-quite-black} */ and #2C2F33 /* {colors.dark-panel} */ surfaces; avoid pure #000000 app panels and avoid SaaS card-shadow stacks"
  applied_to: ["{component.product-mockup-panel}", "{component.app-card}"]
  visual_signature: "tilted Discord UI reads as a real chat surface inside the illustrated room"

webflow-prop-choreography:
  description: "Hero props are staged as suspended objects around the app mockup."
  technique: "Webflow data-w-id reveal hooks with initial opacity: 0, translate3d(...) transforms, transform-style: preserve-3d, and filter: blur(0.5px) on a hero asset state"
  applied_to: ["{component.hero-section}", "{component.product-mockup-panel}"]
  visual_signature: "controller, characters, stars, and device layers feel spatially hung around the product rather than pasted as icons"
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Direct, playful, group-oriented, often all caps | "GROUP CHAT THAT'S ALL FUN & GAMES" |
| Primary CTA | concrete action, platform-specific when possible | "Download for Mac" |
| Secondary CTA | instant-use promise | "Open Discord in your browser" |
| Subheading | explains play, friends, community, customization | "playing games and chilling with friends..." |
| Tone | social, casual, energetic; not enterprise productivity language | "talk, play, and hang out" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Discord — copy into your root stylesheet */
:root {
  /* Fonts */
  --discord-font-family:       "Abcgintodiscord", "Ggsans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --discord-font-family-code:  "Ggsansmono", "Source Code Pro", ui-monospace, monospace;
  --discord-font-display:      "Abcgintonord 800", "ABC Ginto Nord", "Arial Black", sans-serif;
  --discord-font-weight-normal: 400;
  --discord-font-weight-bold:   800;

  /* Brand */
  --discord-color-brand-500: #5865F2;
  --discord-color-brand-hover: #8891F2;
  --discord-color-focus: #4D65FF;
  --discord-color-old-brand: #7289DA;
  --discord-color-hero-plum: #1F1D5D;

  /* Surfaces */
  --discord-bg-page:   #050614;
  --discord-bg-dark:   #23272A;
  --discord-bg-panel:  #2C2F33;
  --discord-bg-soft:   #F6F6F6;
  --discord-text:      #FFFFFF;
  --discord-text-dark: #23272A;
  --discord-border-on-dark: #FFFFFF10;

  /* Key spacing */
  --discord-space-sm:  12px;
  --discord-space-md:  24px;
  --discord-space-lg:  56px;
  --discord-space-xl:  88px;

  /* Radius */
  --discord-radius-app: 3px;
  --discord-radius-sm: 8px;
  --discord-radius-md: 16px;
  --discord-radius-pill: 1000px;
}

.discord-hero {
  min-height: 100vh;
  color: var(--discord-text);
  background:
    radial-gradient(circle at 78% 34%, rgba(88, 101, 242, .55), transparent 34rem),
    linear-gradient(135deg, #02030B 0%, #121069 48%, #3036D6 100%);
  overflow: hidden;
}

.discord-hero__title {
  font-family: var(--discord-font-display);
  font-size: clamp(48px, 6vw, 76px);
  line-height: .9;
  text-transform: uppercase;
  letter-spacing: 0;
}

.discord-hero__button--download {
  background: #FFFFFF;
  color: #23272A;
  border-radius: 16px;
  padding: 16px 32px;
}

.discord-hero__button--browser {
  background: #5865F2;
  color: #FFFFFF;
  border-radius: 16px;
  padding: 16px 32px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Discord-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        discord: {
          brand: '#5865F2',
          hover: '#8891F2',
          focus: '#4D65FF',
          black: '#23272A',
          panel: '#2C2F33',
          white: '#FFFFFF',
          soft: '#F6F6F6',
          plum: '#1F1D5D',
          success: '#43B581',
          warning: '#FAA61A',
          error: '#F04747',
          link: '#00AFF7',
        },
      },
      fontFamily: {
        sans: ['Abcgintodiscord', 'Ggsans', 'system-ui', 'sans-serif'],
        display: ['Abcgintonord 800', 'ABC Ginto Nord', 'Arial Black', 'sans-serif'],
        mono: ['Ggsansmono', 'Source Code Pro', 'ui-monospace'],
      },
      fontWeight: {
        normal: '400',
        semibold: '600',
        black: '800',
      },
      borderRadius: {
        app: '3px',
        sm: '8px',
        md: '16px',
        pill: '1000px',
      },
      boxShadow: {
        dropdown: '0 1px 1px rgb(0 0 0 / 10%)',
        focus: '0 0 0 3px #00B0F4',
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
| Brand primary | `{colors.brand}` | `#5865F2` |
| Background | `hero night stage` | `#050614` |
| Text primary | `{colors.white}` | `#FFFFFF` |
| Text dark | `{colors.not-quite-black}` | `#23272A` |
| Border | `on-dark hairline` | `#FFFFFF10` |
| Success | `{colors.success}` | `#43B581` |
| Error | `{colors.error}` | `#F04747` |

### Example Component Prompts

#### Hero Section

```text
Discord 스타일 히어로 섹션을 만들어줘.
- 배경: dark blurple stage, near-black edge + saturated blue/violet center
- H1: Abcgintonord 800, clamp(48px, 6vw, 76px), uppercase, line-height .9, white
- 서브텍스트: #FFFFFF, 20px, max-width 520px
- 우측: tilted dark Discord app mockup with playful character/prop composition
- CTA: white Download button (#23272A text) + blurple Browser button (#5865F2 bg)
- 네비게이션: transparent, white 16px semibold links
```

#### Card Component

```text
Discord app-style card를 만들어줘.
- 배경: #23272A 또는 #2C2F33
- border: 필요할 때만 #FFFFFF10
- radius: 8px 또는 16px
- padding: 16px-24px
- shadow: 거의 없음. depth는 nested surface contrast로 만든다.
- 제목: Ggsans/Abcgintodiscord, 16px, weight 600, color #FFFFFF
- 본문: 14px, muted light gray, line-height 1.4
```

#### Badge

```text
Discord 스타일 badge가 필요하면 hero 위 eyebrow로 쓰지 말고 app UI 안에 넣어줘.
- font: Ggsans, 12px-14px, weight 600
- padding: 4px 8px
- radius: 1000px
- bg: #5865F220 또는 dark panel
- color: #FFFFFF 또는 #5865F2
```

#### Navigation

```text
Discord 홈페이지 상단 네비게이션을 만들어줘.
- 높이: 72px-88px
- 배경: transparent over dark hero
- 로고: white
- 링크: white, 16px, weight 600
- dropdown chevron: small, white/alpha
- login button: white pill, #23272A text
```

### Iteration Guide

- **색상 변경 시**: brand CTA는 `#5865F2`를 유지하고, stage 분위기는 dark blue/plum에서 조절한다.
- **폰트 변경 시**: display/body를 분리한다. 한 폰트로 전부 통일하면 Discord 특유의 포스터성이 사라진다.
- **여백 조정 시**: hero는 넓게, CTA는 24px gap, mobile은 stacked controls를 유지한다.
- **새 컴포넌트 추가 시**: app surfaces는 `#23272A` / `#2C2F33` 계열, marketing controls는 16px radius를 우선한다.
- **다크 모드**: 이 homepage는 dark-first다. light theme을 기본값으로 뒤집지 않는다.
- **반응형**: product tableau를 먼저 줄이고, H1의 line breaks를 보존한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#5865F2` as the current brand interaction color.
- Keep hero text `#FFFFFF` on a dark blurple/night-stage background.
- Use heavy uppercase display typography for the first hero statement.
- Pair a white download CTA with a blurple browser/open CTA.
- Let product UI imagery carry real Discord context: channels, chat, voice/video, friends.
- Keep navigation transparent and white on the hero.
- Use playful illustrated props only when they interact with the product tableau.
- Preserve app dark surfaces with `#23272A` / `#2C2F33` rather than pure black.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 hero stage는 dark blue/plum field와 `#050614` 계열을 사용.
- 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — hero foreground는 `#FFFFFF`, white button text-on-light는 `#23272A` 사용.
- primary brand CTA를 `#7289DA`로 고정하지 말 것 — 현대 anchor는 `#5865F2`, legacy `#7289DA`는 오래된 app/button CSS에서만 보조.
- app dark surface를 `#000000`으로 두지 말 것 — Discord dark UI는 `#23272A` / `#2C2F33` 계열 사용.
- focus outline을 임의의 `#0000FF`로 두지 말 것 — observed focus colors are `#4D65FF` and app focus `#00B0F4`.
- hero CTA radius를 `4px`로 줄이지 말 것 — homepage hero buttons need `16px` rounded rectangles.
- hero display를 `font-weight: 400`으로 만들지 말 것 — headline is heavy `800`-class display.
- nav links를 `#6B7280` gray로 낮추지 말 것 — hero nav uses white over the dark stage.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Minimal white SaaS canvas: absent in the hero. The page opens on a dark social stage, not a productivity dashboard.
- Thin neutral typography: never for the main hero. The headline needs heavy Ginto/Nord energy.
- Generic purple gradient-only hero: insufficient. Discord needs product UI plus playful props on top of the color field.
- Muted gray nav: absent. Header links stay white and confident.
- Sharp enterprise buttons: not in the homepage hero. CTAs are large and rounded.
- Decorative badge eyebrow above H1: not part of the observed hero. The headline starts directly.
- Second equal brand color: none. Accents exist, but blurple owns primary interaction.
- Card-shadow-heavy layout: not the homepage language. Illustration layering and dark surfaces create depth.
- Pure black app surfaces: avoided. The Discord dark identity is not-quite-black and charcoal.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage capture** — This report is based on the captured `https://discord.com` homepage phase1 assets, not every localized route or logged-in app surface.
- **Marketing vs app layer mixed CSS** — The CSS includes Webflow marketing styles and large Discord app token bundles. Component tokens such as `--card-background-default` may describe app UI more than the homepage hero.
- **HSL token resolution incomplete** — phase1 recorded 4167 variables but only 203 resolved values. Many `hsl(var(...))` aliases remain unresolved, so this guide favors observed terminal hex and role evidence.
- **Motion not replayed live** — Webflow `data-w-id` animation hooks were observed in CSS/HTML, but scroll timing and runtime easing were not captured through an interactive browser replay.
- **Responsive visual checks limited** — The hero screenshot is desktop. Tablet/mobile behavior is inferred from CSS breakpoints and Webflow branches, not from fresh mobile screenshots.
- **Image asset palette not fully sampled** — The hero illustration contributes additional purples, pinks, blues, and character colors. This guide treats them as artwork, not core UI tokens.
- **Forms and validation states not surfaced in homepage** — Input aliases exist in CSS, but the homepage hero does not expose form validation, loading, or error flows.
- **Exact proprietary font metrics unavailable** — Ginto/GG Sans family names are observed, but fallback compensation is approximate because the proprietary font files were not measured directly.
