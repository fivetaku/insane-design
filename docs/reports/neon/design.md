---
schema_version: 3.2
slug: neon
service_name: Neon
site_url: https://neon.com
fetched_at: 2026-05-03T06:52:25Z
default_theme: dark
brand_color: "#00E599"
primary_font: Inter
font_weight_normal: 400
token_prefix: neon

bold_direction: Database Noir
aesthetic_category: Retro-Futuristic
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Tailwind v4 utility build with real recurring brand, neutral, radius, typography, and component classes in production CSS."

colors:
  primary: "#00E599"
  primary-alt: "#00CC88"
  page-dark: "#000000"
  ink-dark: "#131415"
  surface-dark: "#18191B"
  surface-rail: "#242628"
  text-primary: "#FFFFFF"
  text-muted: "#C9CBCF"
  text-subtle: "#AFB1B6"
  border-dark: "#303236"
  section-mint: "#E4F1EB"
  focus: "#38A57D"
typography:
  display: "Inter"
  body: "Inter"
  mono: "GeistMono"
  ladder:
    - { token: hero-h1, size: "72px", weight: 400, tracking: "normal" }
    - { token: section-h2, size: "48px", weight: 400, tracking: "normal" }
    - { token: feature-h3, size: "24px", weight: 500, tracking: "normal" }
    - { token: body, size: "16px", weight: 400, tracking: "normal" }
    - { token: nav, size: "14px", weight: 400, tracking: "normal" }
    - { token: mono-command, size: "16px", weight: 500, tracking: "normal" }
  weights_used: [300, 400, 500, 600, 700, 800]
  weights_absent: []
components:
  button-primary-pill: { bg: "#FFFFFF", fg: "#000000", radius: "999px", padding: "12px 28px" }
  button-secondary-outline: { bg: "transparent", fg: "#FFFFFF", border: "1px solid #303236", radius: "999px" }
  animated-command-button: { bg: "#131415", fg: "#FFFFFF", accent: "#00E599", radius: "10px" }
  nav-dark-bar: { bg: "#000000", fg: "#FFFFFF", border: "1px solid #303236" }
---

# DESIGN.md — Neon (Designer Guidebook)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Neon looks like a database console that learned how to behave like a stage. The homepage opens in near-black, but it is not plain black minimalism: the hero is lit by vertical spectral bars, green-blue scanlines, and a faint city-grid rhythm behind the headline. The effect is a server rack seen through smoked glass, not a generic SaaS gradient. The page does not paint "cloud" as softness; it renders infrastructure as light leaking through a machine room door.

The brand color is a very specific electric mint, `#00E599` (`{colors.primary}`). There is no second brand color trying to share the spotlight. Mint appears as focus color, link hover, border accent, logo geometry, and small proof point: database activity, not decoration. Most of the page is carried by `#000000` (`{colors.page-dark}`), `#131415` (`{colors.ink-dark}`), `#18191B` (`{colors.surface-dark}`), `#242628` (`{colors.surface-rail}`), and cool gray text. This restraint keeps the neon from becoming arcade; the green reads like a terminal cursor in a dark operations room.

Typography is confident but not editorially precious. Inter does the main work, with `GeistMono` reserved for command-line and code moments. The hero H1 is large and plain, not over-weighted, like a command output projected onto a black wall. Neon sells infrastructure, so the page avoids decorative display fonts and lets the product language sound direct: "Fast Postgres Databases for Teams and Agents." The mono moments are not retro cosplay; they are the actual label plates on the machinery.

The strongest craft move is the contrast between cinematic hero darkness and product-section utility. The first screen is theatrical: a midnight data-center stage with one electric mint signal moving through it. The following sections become structured: command snippets, feature bands, comparison-like cards, green-tinted autoscaling panels, and platform proof. It is a noir control room that keeps handing you working controls instead of concept art.

Neon's surfaces also refuse luxury shadow drama. Shadow is secondary; border is the chassis. The `#303236` (`{colors.border-dark}`) hairlines, cool rails, and low-sheen panels make the site feel assembled from database modules. When the pale mint section appears, it does not become a new brand universe; it works like a maintenance bay with the lights on before the page returns to black.

### Key Characteristics

- Black-first marketing shell with `#00E599` as the single memorable chromatic accent.
- Hero background uses vertical scanline/raster bars rather than a soft decorative gradient.
- Pill CTAs invert the dark field: primary action is white on black context, not green-filled.
- Navigation is dense and product-led, with dropdown categories, docs, pricing, community, and account actions visible.
- The color system uses cool neutral steps (`#131415`, `#18191B`, `#242628`, `#303236`, `#494B50`) instead of warm grays.
- Light mint section bands (`#E4F1EB`) appear as structural contrast, not as the default page background.
- Code and CLI moments are real content surfaces, backed by mono typography and command buttons.
- Motion/craft signature concentrates in animated button masks, hero scanning imagery, and hover color transitions.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Database Noir
> **Aesthetic Category**: Retro-Futuristic
> **Signature Element**: 이 사이트는 **black database stage with electric scanline mint**으로 기억된다.
> **Code Complexity**: high — Tailwind v4 utility density plus animated masks, gradient backgrounds, responsive section choreography, and mixed dark/light bands.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Neon처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Font + weight */
body {
  font-family: "Inter", "Inter Fallback", -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
}

/* 2. Dark database floor */
:root {
  --neon-bg-page: #000000;
  --neon-bg-ink: #131415;
  --neon-text: #ffffff;
  --neon-text-muted: #c9cbcf;
}
body {
  background: var(--neon-bg-page);
  color: var(--neon-text);
}

/* 3. Single electric mint accent */
:root {
  --neon-primary: #00e599;
  --neon-focus: #38a57d;
}
a:hover,
.accent {
  color: var(--neon-primary);
}
```

**절대 하지 말아야 할 것 하나**: CTA와 배경 전체를 `#00E599`로 칠하지 말 것. Neon의 mint는 "signal"이고, 무대는 거의 항상 `#000000` / `#131415`다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://neon.com` |
| Fetched | 2026-05-03T06:52:25Z |
| Extractor | phase1 reuse: saved HTML + CSS + screenshot |
| HTML size | 858738 bytes (Next.js app output) |
| CSS files | 2 external CSS files, 494753 total chars |
| Token prefix | `neon` (guidebook alias; production CSS is Tailwind v4 utilities) |
| Method | CSS hex frequency, Tailwind variable extraction, screenshot inspection, HTML section structure |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js-style server-rendered marketing site.
- **Design system**: Tailwind v4 utility build. Production CSS exposes Tailwind tokens such as `--spacing: .25rem`, `--radius-*`, `--container-*`, `--font-weight-*`, and `--text-*--line-height`.
- **CSS architecture**:
  ```css
  Tailwind theme tokens   (--spacing, --radius-lg, --font-weight-semibold)
  Utility classes         (.bg-primary-1, .text-primary-1, .grid-cols-*)
  Component classes       (.animated-button, .hero, .text-with-links)
  Section classes         (.autoscaling, .branching, .backed-by, .cta)
  ```
- **Class naming**: utility-first with a few semantic section/component names.
- **Default theme**: dark marketing shell (`#000000` hero and navigation), with selected light mint bands.
- **Font loading**: `--font-inter`, `--font-geist-mono`, `--font-esbuild` custom properties plus metric fallbacks.
- **Canonical anchor**: hero section: black navigation + Databricks badge + large Inter headline + white pill CTA over scanline database imagery.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Inter` (open-source; loaded with `Inter Fallback`)
- **Code font**: `GeistMono` (loaded through `--font-geist-mono`)
- **Weight normal / bold**: `400` / `600-700`

```css
:root {
  --neon-font-family: "Inter", "Inter Fallback";
  --neon-font-family-code: "GeistMono", ui-monospace, SFMono-Regular, Roboto Mono, Menlo, Monaco, Consolas, monospace;
  --neon-font-weight-normal: 400;
  --neon-font-weight-medium: 500;
  --neon-font-weight-semibold: 600;
  --neon-font-weight-bold: 700;
}

body {
  font-family: var(--neon-font-family);
  font-weight: var(--neon-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **Inter** — Safe substitute is `system-ui`, but keep the weight discipline: body at 400, labels at 500, heavier proof/stat numbers at 600-700. Do not replace it with a geometric display face; Neon needs product-console neutrality.
- **GeistMono** — If unavailable, use `SFMono-Regular` or `Menlo`. Preserve command-button rhythm with `font-size: 16px`, `line-height: 1.5`, and avoid condensed monospace fonts.
- **Fallback correction** — Inter replacement should keep letter-spacing at `0`. The production CSS does not rely on heavy negative tracking; tightening the hero makes it look like a different brand.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `hero-h1` | `72px` observed in CSS frequency | 400 | `1` | `0` |
| `section-h2-xl` | `48px` / `3rem` | 400-500 | `1` to `1.25` | `0` |
| `section-h2-lg` | `36px` / `2.25rem` | 400-600 | `calc(2.5 / 2.25)` | `0` |
| `feature-title` | `24px` / `1.5rem` | 500-600 | `calc(2 / 1.5)` | `0` |
| `body-lg` | `18px` / `1.125rem` | 400 | `calc(1.75 / 1.125)` | `0` |
| `body` | `16px` / `1rem` | 400 | `calc(1.5 / 1)` | `0` |
| `nav-label` | `14px` / `.875rem` | 400-500 | `calc(1.25 / .875)` | `0` |
| `micro-label` | `12px` / `.75rem` | 500-600 | `calc(1 / .75)` | `0` |

> ⚠️ Neon's typography feels technical because it stays plain. The site does not need a special display face; scale, darkness, and precise product copy carry the identity.

### Principles
<!-- SOURCE: manual -->

1. Hero text is large but not heavy. The H1 earns impact from scale and darkness, not from `font-weight: 800`.
2. Body and nav copy stay utilitarian at 14-18px. This preserves the product-console tone.
3. Monospace is contextual, not decorative. Use `GeistMono` for command snippets, code, and database interaction surfaces only.
4. Tracking remains effectively neutral. Do not add luxury-style negative letter-spacing unless a specific production class requires it.
5. Weight 500 is an interface weight for labels, buttons, and compact titles; weight 700+ is reserved for emphasis and stats.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (5 practical steps)

| Token | Hex |
|---|---|
| `neon-primary-bright` | `#00FFAA` |
| `neon-primary` | `#00E599` |
| `neon-primary-2` | `#00CC88` |
| `neon-focus` | `#38A57D` |
| `neon-focus-alt` | `#39A57D` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `neon-ink` | `#131415` |
| `neon-ink-deep` | `#0C0D0D` |
| `neon-surface` | `#18191B` |
| `neon-panel` | `#242628` |

### 06-3. Neutral Ramp

| Step | Dark / Light | Hex |
|---|---|---|
| 0 | pure black | `#000000` |
| 10 | dark page ink | `#131415` |
| 20 | dark surface | `#18191B` |
| 30 | elevated rail | `#242628` |
| 40 | border | `#303236` |
| 50 | secondary text | `#494B50` |
| 60 | muted text | `#797D86` |
| 70 | gray label | `#AFB1B6` |
| 80 | high-muted text | `#C9CBCF` |
| 90 | light hairline | `#E4E5E7` |
| 100 | white | `#FFFFFF` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Database mint | primary | `#00E599` |
| Pale mint band | section bg | `#E4F1EB` |
| Syntax cyan | code token | `#52C9E0` |
| Syntax violet | code token | `#A199FF` |
| Syntax amber | code token | `#FF990A` |
| Error/pink accent | secondary token | `#FF4C79` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `neon-action-primary` | `#FFFFFF` | Hero primary CTA on dark field |
| `neon-link-hover` | `#00E599` | Hover links and primary text accents |
| `neon-focus-ring` | `#38A57D` | Focus-visible outline |
| `neon-page-bg` | `#000000` | Header and hero page floor |
| `neon-section-mint` | `#E4F1EB` | Autoscaling/backed-by contrast sections |
| `neon-border-dark` | `#303236` | Dark nav, cards, dividers |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `bg-primary-1` | `#00E599` | Primary accent backgrounds in limited contexts |
| `text-primary-1` | `#00E599` | Mint text accent |
| `border-primary-1` | `#00E599` | Mint borders |
| `text-with-links a:hover` | `#00E599` | Inline links on dark copy |
| `bg-security-card-link-bg` | `#233632CC`, `#15211ECC`, `#0C0C0D` | Dark radial card treatment |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency |
|---|---|---|
| `white` | `#FFFFFF` | 125 |
| `transparent-black` | `#00000000` | 87 |
| `black` | `#000000` | 55 |
| `primary-mint` | `#00E599` | 43 |
| `border-dark` | `#303236` | 37 |
| `surface-rail` | `#242628` | 36 |
| `gray-30` | `#494B50` | 35 |
| `gray-70` | `#AFB1B6` | 30 |
| `gray-80` | `#C9CBCF` | 30 |
| `gray-90` | `#E4E5E7` | 26 |

### 06-8. Color Stories
<!-- SOURCE: manual — 상위 4 색만 -->

**`{colors.text-primary}` (`#FFFFFF`)** — White is the real first-color by CSS frequency because the site lives on black. It is used for hero text, dark navigation, inverted buttons, and high-confidence product copy. Do not mute it into gray for the hero.

**`{colors.page-dark}` (`#000000`)** — The black floor is not a fallback; it is the stage. It makes the scanline background and white pill buttons feel precise. Replacing it with `#111827` or a blue-black SaaS tint breaks the database-noir mood.

**`{colors.primary}` (`#00E599`)** — Electric mint is a signal color. Use it for hover, focus, logo geometry, borders, and selective brand moments. It should not become the default button fill across the page.

**`{colors.border-dark}` (`#303236`)** — This cool border gray is the quiet chassis. It separates dark panels without introducing heavy shadows. Many AI recreations skip this and lose the product-console discipline.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---|---|
| `--spacing` | `.25rem` | Tailwind v4 base unit, 4px ladder |
| `section-ai-y` | `py-40` / 160px desktop | Large editorial-product feature sections |
| `section-autoscaling-top` | `88px`, then responsive 64/56/36px | Mint section opening rhythm |
| `section-branching-y` | `pt-40 pb-60`, responsive reductions | Long feature narrative band |
| `section-footer-safe` | safe paddings | viewport-safe edge handling |
| `gap-card` | 16-32px inferred utility range | dense product card grids |

**주요 alias**:
- `safe-paddings` → page-edge guard used across hero, sections, and footer.
- `container-7xl` → `80rem` maximum utility container.
- `container-5xl` → `64rem` editorial content width.

### Whitespace Philosophy
<!-- SOURCE: manual -->

Neon uses big vertical section padding to make infrastructure claims feel calm, but it keeps individual product cards and command surfaces dense. The pattern is "large black breath, compact operational module." The hero leaves enough dark field for the scanline image to breathe, then moves into tight proof blocks like commands, stats, and feature rows.

Whitespace is not luxury whitespace. It is server-room clearance: wide enough to separate subsystems, narrow enough that the page still feels engineered.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---|---|
| `--radius-sm` | `.25rem` / 4px | small utility surfaces |
| `--radius-md` | `.375rem` / 6px | compact cards and inputs |
| `--radius-lg` | `.5rem` / 8px | standard panels |
| `--radius-xl` | `.75rem` / 12px | larger cards |
| `--radius-2xl` | `1rem` / 16px | feature containers |
| `pill` | `999px` / generated huge radius | nav/account/hero pill buttons |
| `command-card` | `10px` | CLI-style command surfaces |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `none` | `none` | Most dark chrome; borders do the work |
| `tailwind-shadow-reset` | `0 0 #0000` | Tailwind base shadow variable |
| `button-shadow-light` | `0 8px 20px #0000001f` | elevated interaction surface |
| `button-shadow-dark` | `0 8px 20px #0009` | dark overlay/elevation |
| `inset-fill` | `inset 0 0 0 1000px #1c1d1e` | masked/animated button effect |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `--tw-duration` | `.2s` | link and color transitions |
| `link-hover` | color/background/border transition | `text-with-links a` hover to mint |
| `animated-button-mask` | radial mask + top/bottom strips | command/button craft |
| `group-hover` | text/bg transition | card and nav interactive states |

Motion is mostly hover feedback and masked button craft. The site does not expose broad parallax in the captured CSS/hero crop, but the hero raster treatment implies motion without requiring every component to animate.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: common utility widths include `1216px`, `1280px`, `1472px`, and Tailwind containers up to `80rem`.
- **Grid type**: CSS Grid and Flexbox utilities, with dense `grid-cols-*` usage.
- **Column count**: marketing sections vary between single-column hero narrative, two-column feature/product explanations, and multi-card product grids.
- **Gutter**: 16-32px utility rhythm; section gutters guarded by `safe-paddings`.

### Hero
- **Pattern Summary**: `~700px crop + black scanline database image + left H1 + dual pill CTA below`.
- Layout: left-aligned text block over full-width dark visual field.
- Background: black hero with vertical green/cyan/yellow raster bars.
- **Background Treatment**: image/raster overlay on `#000000`; not a CSS blob gradient. The first viewport reads as an illuminated data-center wall.
- H1: `72px` class family / weight `400` / tracking `0`.
- Max-width: headline is roughly half-to-two-thirds of desktop viewport in the screenshot.

### Section Rhythm
```css
section.ai {
  padding-top: 160px;
  padding-bottom: 160px;
}
section.autoscaling {
  background: #E4F1EB;
  padding-top: 88px;
  padding-bottom: 105px;
}
section.branching {
  padding-top: 160px;
  padding-bottom: 240px;
}
```

### Card Patterns
- **Card background**: dark cards use `#131415` / `#18191B`; light contrast sections use `#E4F1EB`.
- **Card border**: `1px solid #303236` or related gray ramp.
- **Card radius**: mostly 8-16px for panels, 999px for pills.
- **Card padding**: compact product content inside large section bands.
- **Card shadow**: restrained; border, inset fill, and background contrast dominate.

### Navigation Structure
- **Type**: horizontal product nav with dropdowns on desktop, mobile alternate nav present.
- **Position**: top header, `z-50`, desktop relative after announcement bar.
- **Height**: 64px mobile/default top bar, 56px desktop variant in captured class names.
- **Background**: `#000000` dark header in screenshot; CSS includes light/dark variants.
- **Border**: bottom hairline via `after` pseudo-element, dark border family.

### Content Width
- **Prose max-width**: feature text blocks appear in the 500-800px range depending on section.
- **Container max-width**: `1216px`, `1280px`, `1472px`, and Tailwind `80rem` are present.
- **Sidebar width**: no persistent sidebar on marketing homepage; dropdown mega menus act as temporary navigation panels.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Small mobile | `max-width: 413px` | extra tightening for narrow devices |
| Mobile | `max-width: 39.9375rem` (~639px) | hero/sections compress and mobile nav takes over |
| Tablet | `max-width: 47.9375rem` (~767px) | frequent layout collapse breakpoint |
| Laptop | `max-width: 63.9375rem` (~1023px) | desktop nav and large section rhythm reduce |
| Desktop | `min-width: 1280px` | wide layout refinements |
| Ultra-wide | `min-width: 1921px` | special large viewport handling |

### Touch Targets
- **Minimum tap size**: pill CTAs visually target 44px+ height.
- **Button height (mobile)**: captured buttons appear around 44px.
- **Input height (mobile)**: not directly observed on homepage.

### Collapsing Strategy
- **Navigation**: desktop menu gives way to mobile nav below large breakpoints.
- **Grid columns**: grid-heavy sections collapse through max-width media queries.
- **Sidebar**: not applicable on homepage.
- **Hero layout**: keeps brand image field but compresses headline and CTA stack on smaller widths.

### Image Behavior
- **Strategy**: full-width responsive hero asset and section illustrations.
- **Max-width**: CSS includes `max-width: 100%` and fixed container caps.
- **Aspect ratio handling**: hero crop preserves a wide cinematic band; product imagery likely uses object-fit utilities.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary pill CTA**

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#000000` |
| Radius | pill / effectively `999px` |
| Padding | approx `12px 28px` |
| Use | "Get started", "Sign up" on dark header/hero |

**Secondary outline pill**

| Property | Value |
|---|---|
| Background | transparent |
| Text | `#FFFFFF` |
| Border | `1px solid #303236` / gray hairline |
| Radius | pill |
| Use | "Read the docs", "Log in" |

**Animated command button**

| Property | Value |
|---|---|
| Font | `GeistMono` / mono stack |
| Accent | `#00E599` hover/focus signal |
| Technique | `animated-button` with masked top/bottom strips |
| Use | `$ npx neonctl init` command CTA |

### Badges

Badges are small, text-led, and often monochrome. The Databricks badge in the hero uses a small red mark plus uppercase label, with low visual weight so it does not compete with the H1. Do not turn badges into filled green capsules unless the CSS shows that state.

### Cards & Containers

Feature containers alternate between dark panels and pale mint bands. Dark cards rely on `#18191B`/`#242628` surfaces, `#303236` borders, and little to no shadow. Light feature bands use `#E4F1EB` to create a narrative reset. Cards should feel like database modules, not marketing feature tiles.

### Navigation

The header combines a product logo, dropdown product categories, docs/pricing/resources links, Discord/GitHub proof, and account actions. Desktop nav is information-dense; it should not be replaced with a minimal three-link marketing nav. Active/hover behavior moves toward lighter gray or mint depending on link type.

### Inputs & Forms

Homepage form states were not directly surfaced. Use the visible focus contract: `outline-color: #38A57D`, `outline-offset: 2px`, `outline-width: 2px` for interactive elements. Inputs should inherit font, color, and transparent background before explicit styling.

### Hero Section

The hero is a full-width dark product stage with a top announcement strip, dark nav, scanline database visual, Databricks affiliation line, large left-aligned H1, and two pill CTAs. The primary button is white, not green. The secondary button is transparent/dark outline.

### 13-2. Named Variants

| Variant | Spec | State notes |
|---|---|---|
| `button-primary-pill` | `#FFFFFF` bg, `#000000` text, pill radius | hover should stay restrained; avoid mint fill |
| `button-secondary-outline` | transparent bg, white text, gray border | hover can brighten border/text |
| `button-login-dark` | transparent dark header button, pill border | compact account action |
| `animated-command-button` | mono text, masked animated chrome | used for CLI command affordance |
| `nav-dropdown-trigger` | 14px label, inherited color, chevron | hover shifts gray/white state |
| `feature-dark-card` | `#18191B`/`#242628`, border `#303236` | group-hover can alter text/bg subtly |
| `mint-section-panel` | `#E4F1EB` background, black text | used for autoscaling/backed-by contrast |

### 13-3. Signature Micro-Specs

```yaml
scanline-database-hero:
  description: "Hero identity built from luminous database raster bars instead of a product screenshot."
  technique: "image/raster hero treatment over #000000; vertical green/cyan/yellow bars; left-aligned 72px Inter H1; high-contrast dark crop"
  applied_to: ["{component.Hero Section}"]
  visual_signature: "A black data-center wall with electric signal columns behind the product promise."

masked-animated-button-chrome:
  description: "CLI actions are treated like illuminated physical controls."
  technique: ".animated-button with top/bottom pseudo segments, mask-image: radial-gradient(...), animated background-position, inset 0 0 0 1000px #1c1d1e fill"
  applied_to: ["{component.animated-command-button}", "{component.Buttons}"]
  visual_signature: "A command CTA that feels machined, lit, and interactive rather than simply styled."

mint-signal-only:
  description: "The brand mint is a signal state, not a broad surface color."
  technique: "#00E599 for hover links, focus accents, border/text highlights, and logo geometry; #38A57D focus outline; primary CTA remains #FFFFFF on dark"
  applied_to: ["{component.button-primary-pill}", "{component.Navigation}", "{component.Links}", "{component.Focus states}"]
  visual_signature: "Mint flashes like database activity while the page stays black and cool-neutral."

cool-border-chassis:
  description: "Panel structure is carried by cool hairlines and rails instead of layered marketing shadows."
  technique: "1px #303236 borders, #242628 rail surfaces, #18191B dark panels, minimal shadow; Tailwind shadow reset 0 0 #0000"
  applied_to: ["{component.nav-dark-bar}", "{component.feature-dark-card}", "{component.Cards & Containers}"]
  visual_signature: "Dark modules remain legible because their edges are engineered, not floated."

pale-mint-maintenance-bay:
  description: "Light sections create operational contrast without becoming the default brand background."
  technique: "#E4F1EB section band; autoscaling rhythm with padding-top 88px and padding-bottom 105px; black text on pale mint"
  applied_to: ["{component.mint-section-panel}", "{component.autoscaling section}", "{component.backed-by section}"]
  visual_signature: "A brief lights-on maintenance bay between stretches of database noir."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Direct product outcome, no metaphor first | "Fast Postgres Databases for Teams and Agents" |
| Primary CTA | action verbs, short | "Get started" |
| Secondary CTA | documentation trust path | "Read the docs" |
| Subheading | product capability plus operational benefit | "Keep scaling without worrying about capacity." |
| Tone | technical, confident, infrastructure-native | "Storage-compute separation", "Instant branching" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Neon — copy into your root stylesheet */
:root {
  /* Fonts */
  --neon-font-family: "Inter", "Inter Fallback", ui-sans-serif, system-ui, sans-serif;
  --neon-font-family-code: "GeistMono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  --neon-font-weight-normal: 400;
  --neon-font-weight-medium: 500;
  --neon-font-weight-semibold: 600;

  /* Brand */
  --neon-color-primary-bright: #00FFAA;
  --neon-color-primary: #00E599;
  --neon-color-primary-2: #00CC88;
  --neon-color-focus: #38A57D;

  /* Surfaces */
  --neon-bg-page: #000000;
  --neon-bg-ink: #131415;
  --neon-bg-surface: #18191B;
  --neon-bg-rail: #242628;
  --neon-bg-mint-section: #E4F1EB;

  /* Text and borders */
  --neon-text-primary: #FFFFFF;
  --neon-text-muted: #C9CBCF;
  --neon-text-subtle: #AFB1B6;
  --neon-border-dark: #303236;

  /* Spacing / radius */
  --neon-space-unit: .25rem;
  --neon-radius-sm: .25rem;
  --neon-radius-md: .375rem;
  --neon-radius-lg: .5rem;
  --neon-radius-xl: .75rem;
  --neon-radius-pill: 999px;
}

.neon-page {
  background: var(--neon-bg-page);
  color: var(--neon-text-primary);
  font-family: var(--neon-font-family);
  font-weight: var(--neon-font-weight-normal);
}

.neon-primary-button {
  background: #FFFFFF;
  color: #000000;
  border-radius: var(--neon-radius-pill);
  padding: 12px 28px;
}

.neon-secondary-button {
  background: transparent;
  color: #FFFFFF;
  border: 1px solid var(--neon-border-dark);
  border-radius: var(--neon-radius-pill);
  padding: 12px 28px;
}

.neon-link:hover {
  color: var(--neon-color-primary);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Neon-inspired mapping
module.exports = {
  theme: {
    extend: {
      colors: {
        neon: {
          primary: '#00E599',
          primary2: '#00CC88',
          focus: '#38A57D',
          black: '#000000',
          ink: '#131415',
          surface: '#18191B',
          rail: '#242628',
          border: '#303236',
          muted: '#C9CBCF',
          mintSection: '#E4F1EB',
        },
      },
      fontFamily: {
        sans: ['Inter', 'Inter Fallback', 'system-ui', 'sans-serif'],
        mono: ['GeistMono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      },
      borderRadius: {
        sm: '.25rem',
        md: '.375rem',
        lg: '.5rem',
        xl: '.75rem',
        '2xl': '1rem',
        pill: '999px',
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
| Brand primary | `neon-primary` | `#00E599` |
| Background | `neon-page-bg` | `#000000` |
| Dark surface | `neon-ink` | `#131415` |
| Text primary | `neon-text-primary` | `#FFFFFF` |
| Text muted | `neon-text-muted` | `#C9CBCF` |
| Border | `neon-border-dark` | `#303236` |
| Focus | `neon-focus` | `#38A57D` |
| Light section | `neon-section-mint` | `#E4F1EB` |

### Example Component Prompts

#### Hero Section
```text
Neon 스타일 히어로를 만들어줘.
- 배경: #000000
- 배경 처리: vertical scanline/raster database image 느낌, green/cyan bars, no soft purple blob
- H1: Inter, 64-72px desktop, weight 400, line-height 1
- CTA: primary는 #FFFFFF 배경 + #000000 텍스트 pill, secondary는 transparent + #303236 border
- Accent: #00E599 only for logo/link/focus details
- Layout: left-aligned text over dark full-width stage
```

#### Card Component
```text
Neon 스타일 feature card를 만들어줘.
- bg: #18191B 또는 #242628
- border: 1px solid #303236
- radius: 8-16px
- shadow는 거의 쓰지 말고 border와 surface contrast로 구조를 만든다
- 제목: Inter 20-24px, weight 500-600
- 본문: #C9CBCF, 16px, line-height 1.5
- hover: text/border만 #00E599 방향으로 살짝 이동
```

#### Navigation
```text
Neon 스타일 상단 네비게이션을 만들어줘.
- 높이: 56-64px
- bg: #000000
- border-bottom: 1px solid #303236
- 링크: Inter 14px, #FFFFFF 또는 #C9CBCF
- dropdown trigger를 포함한 product-heavy nav
- 우측에 Discord/GitHub proof + Log in + white Sign up pill
```

### Iteration Guide

- **색상 변경 시**: `#00E599`를 넓은 배경색으로 확장하지 말고 signal 역할에 둔다.
- **폰트 변경 시**: Inter의 중립성과 GeistMono의 CLI 맥락을 유지한다.
- **여백 조정 시**: 섹션은 크게, 카드 내부는 촘촘하게 조정한다.
- **새 컴포넌트 추가 시**: shadow보다 `#303236` hairline과 dark surface layering을 우선한다.
- **다크 모드**: Neon homepage의 기본값은 dark다. light mode를 기본으로 뒤집지 말 것.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#000000` / `#131415` as the primary stage for hero and top navigation.
- Use `#00E599` as a sharp signal for links, focus, borders, and brand marks.
- Keep primary hero/account CTAs as white pill buttons on dark surfaces.
- Build structure with cool gray borders like `#303236`, not heavy elevation.
- Use Inter for product copy and GeistMono for command/code moments.
- Preserve the product-heavy navigation density: Product, Solutions, Docs, Pricing, Resources, community proof, account actions.
- Use `#E4F1EB` as a deliberate section reset, not as the whole-page background.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 hero/nav 기본은 `#000000` 사용.
- 본문 dark surface를 `#111827` 또는 navy SaaS black으로 두지 말 것 — 대신 `#131415` / `#18191B` 사용.
- primary accent를 `#22C55E` 같은 generic green으로 바꾸지 말 것 — 대신 `#00E599` 사용.
- CTA 기본 배경을 `#00E599`로 칠하지 말 것 — hero primary CTA는 `#FFFFFF` 배경 + `#000000` 텍스트 사용.
- 텍스트를 `#000000`으로 dark hero에 직접 올리지 말 것 — dark hero text는 `#FFFFFF` 또는 `#C9CBCF` 사용.
- border를 `#E5E7EB` light gray로 dark card에 쓰지 말 것 — dark border는 `#303236` 사용.
- font를 `Roboto` 단독 또는 generic `Arial`로 대체하지 말 것 — `Inter` + mono `GeistMono` 구조 유지.
- 모든 카드에 큰 `box-shadow`를 넣지 말 것 — Neon은 border/surface contrast가 우선이다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second brand color: none. Mint `#00E599` carries the recognizable chromatic identity.
- Purple-blue AI gradient: absent. The hero is raster/scanline database light, not `#667eea` to `#764ba2`.
- Rounded pastel SaaS cards: absent. Cards are dark operational modules or pale mint proof bands.
- Heavy chrome shadows: mostly absent. Borders and inset/masked effects do the structural work.
- Warm beige/tan neutrals: absent. Neutrals are cool black/gray.
- Decorative emoji: absent from the brand surface. Icons are product/community marks, not casual stickers.
- Overweight hero typography: avoided. The H1 stays large and regular, not 900-weight.
- Broad green backgrounds: rare. Green is signal, not wallpaper.
- Persistent sidebar: absent on homepage. Navigation is top-level and dropdown-driven.
- Marketing stock photography: absent in the captured hero. Infrastructure is visualized through abstract database light.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Homepage-only capture** — This guide is based on the saved `https://neon.com` homepage phase1 assets. Product console, docs pages, pricing subflows, and account UI may use different surfaces.
- **Desktop screenshot emphasis** — The visual interpretation relies heavily on the 1280x800 hero crop. Mobile screenshots were not directly inspected in this run.
- **CSS utility indirection** — Production CSS is Tailwind-heavy. Some semantic names in this guide (`neon-primary`, `neon-border-dark`) are guidebook aliases mapped to observed values, not literal production custom properties.
- **Animation runtime not fully measured** — CSS transition and mask techniques were inspected, but JavaScript scroll-trigger timing and runtime animation curves were not profiled.
- **Form states not surfaced** — Focus-visible color was found, but validation, loading, disabled, and error form states were not visible on the captured homepage path.
- **Logo/social color filtering** — Frequency counts include some syntax, social, and decorative colors. Brand identity decisions intentionally prioritize recurring UI roles over raw frequency alone.
- **Light theme scope uncertain** — CSS includes light/dark variants and light mint sections, but the captured first viewport is dark. Full theme mapping was not collected.
- **Exact image asset treatment** — The scanline hero background was visually inspected from screenshot, not decomposed into source image layers.
