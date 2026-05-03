---
schema_version: 3.2
slug: starbucks
service_name: Starbucks
site_url: https://www.starbucks.com
fetched_at: 2026-04-14T01:26:00+09:00
default_theme: light
brand_color: "#00754A"
primary_font: SoDoSans
font_weight_normal: 400
token_prefix: sb

bold_direction: Retail Warmth
aesthetic_category: other
signature_element: section_transition
code_complexity: medium

medium: web
medium_confidence: high
archetype: commerce-marketplace
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "CSS 변수 161개, resolved token 119개, 버튼/카드/필드/글로벌 내비게이션 컴포넌트 패턴이 실제 서비스 CSS에 존재한다."

colors:
  colorGreenAccent: "#00754A"
  colorGreenStarbucks: "#006241"
  colorHouseGreen: "#1E3932"
  colorGreenLight: "#D4E9E2"
  colorNeutralWarm: "#F2F0EB"
  colorCeramic: "#EDEBE9"
  colorGold: "#CBA258"
  colorGoldLightest: "#FAF6EE"
  colorRed: "#C82014"
  colorWhite: "#FFFFFF"
  colorBlack: "#000000"
typography:
  display: "SoDoSans"
  body: "SoDoSans"
  specialty: "Lander Tall"
  ladder:
    - { token: textSize1, size: "1.3rem", weight: 400, line_height: "1.5" }
    - { token: textSize3, size: "1.6rem", weight: 400, line_height: "1.5" }
    - { token: textSize4, size: "1.9rem", weight: 600, line_height: "1.2" }
    - { token: textSize7, size: "2.4rem", weight: 700, line_height: "1.2" }
    - { token: textSize9, size: "3.6rem", weight: 700, line_height: "1.2" }
    - { token: textSize10, size: "5.0rem", weight: 700, line_height: "1.2" }
  weights_used: [400, 600, 700]
  weights_absent: [300, 500, 800]
components:
  button-default: { bg: "transparent", color: "{colors.colorGreenAccent}", radius: "50px", padding: "7px 16px" }
  button-positive: { bg: "{colors.colorGreenAccent}", color: "rgba(255,255,255,1)", radius: "50px", padding: "7px 16px" }
  frap: { bg: "{colors.colorGreenAccent}", radius: "500px", shadow: "0 0 6px rgba(0,0,0,0.24), 0 8px 12px rgba(0,0,0,0.14)" }
  card: { bg: "{colors.colorWhite}", radius: "12px", shadow: "0px 0px .5px rgba(0,0,0,0.14), 0px 1px 1px rgba(0,0,0,0.24)" }
---

# DESIGN.md - Starbucks

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Starbucks.com reads less like a pure restaurant homepage and more like a warm retail board in motion. It has the logic of the menu board behind the counter: seasonal panels can change every few weeks, but the ordering grammar stays fixed. The page uses the store brand as an anchor, while the visible campaign surface is carried by product photography, warm color blocks, and short commerce CTAs. The signature feeling is not minimalism. It is a controlled cafe bulletin board: bold enough to sell a drink, soft enough to remain familiar.

The green system behaves like store signage, not like a decorative palette. #00754A (`{colors.colorGreenAccent}`) is the register button, the thing you press; #006241 (`{colors.colorGreenStarbucks}`) is the siren on the door and the institutional nav voice; #1E3932 (`{colors.colorHouseGreen}`) is the painted wall behind the counter. There is no second action green. If these greens collapse into one color, the site stops feeling like Starbucks and starts looking like generic eco-commerce. Around them, #F2F0EB (`{colors.colorNeutralWarm}`), #EDEBE9 (`{colors.colorCeramic}`), #FAF6EE (`{colors.colorGoldLightest}`), and #CBA258 (`{colors.colorGold}`) act like steamed milk, ceramic tile, and pastry-case warmth rather than neutral SaaS gray.

The typography is blunt and retail-friendly, like printed placards clipped into a menu rail. SoDoSans carries the site with 400, 600, and 700 weights; Lander Tall appears as a rewards-specific accent, not as the everyday voice. Buttons are deliberately pill-shaped, compact, and pressable. The green CTA is rarely a huge rectangle. It is closer to an order sticker placed beside product copy: small, round, and meant to be tapped.

The page alternates between editorial tiles and commerce utility. Hero bands split image and copy like a cafe window display: one side shows the drink, the other side prices the mood in a headline and CTA. The nav stays crisp and white with a multi-layer shadow, like a fixed fascia sign above changing seasonal posters. Product photography does the emotional work; UI chrome remains almost domestic, with simple gutters, rounded controls, and shadows reserved for navigation, cards, floating actions, and service graphics rather than sprayed across every surface.

### Key Characteristics

- Warm retail campaign blocks using #F2F0EB, #EDEBE9, #FAF6EE, and #D4E9E2 around green brand controls.
- Three-green hierarchy: action #00754A, Starbucks institutional #006241, house-green #1E3932.
- Pill buttons everywhere: `border-radius: 50px`, `padding: 7px 16px`, active scale `scale(0.95)`.
- Global nav is white, tall, and shadowed: desktop height 99px with a 3-layer black alpha shadow.
- Cards are modest: white surface, 12px radius, tiny elevation, no heavy glass or neumorphism.
- Product photography does the emotional work; UI color supports rather than competes.
- SoDoSans remains the default voice; Lander Tall is a rewards-specific accent.
- Motion is small and tactile: 200-300ms transitions, fade-in imagery, caret rotation.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Retail Warmth
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **seasonal product tiles stitched together by Starbucks green controls**으로 기억된다.
> **Code Complexity**: medium - tokenized CSS, responsive nav, floating labels, and small interaction states exist, but no heavy parallax or custom rendering layer is required.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Starbucks처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "SoDoSans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
  line-height: 1.5;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: rgba(0,0,0,.87); }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #00754A; --house: #1E3932; --starbucks: #006241; }
.sb-button {
  border-radius: 50px;
  padding: 7px 16px;
  font-weight: 600;
}
```

**절대 하지 말아야 할 것 하나**: Starbucks를 단일 초록 브랜드로 단순화하지 말 것. CTA는 #00754A, institutional green은 #006241, dark surface는 #1E3932로 분리한다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.starbucks.com` |
| Fetched | 2026-04-14T01:26:00+09:00 |
| Extractor | cached phase1 reuse: HTML + CSS + screenshot |
| HTML size | 96576 bytes |
| CSS files | 3 external files, total 171245 chars |
| Token prefix | `sb` / global CSS custom properties |
| Method | CSS custom properties, frequency candidates, HTML landmarks, and hero screenshot review |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js-style compiled CSS modules plus global Starbucks component classes.
- **Design system**: Starbucks web UI tokens - root CSS variables for color, space, typography, nav, forms, buttons, cards, and floating action controls.
- **CSS architecture**:
  ```css
  :root color tokens      (--colorGreenAccent, --colorHouseGreen, --colorNeutralWarm)
  component tokens        (--buttonHeight, --buttonBorderRadius, --cardBoxShadow)
  module classes          (.hero_hero__..., .tile_..., .featured-copy_...)
  global utility classes  (.sb-button, .sb-card, .sb-globalNav, .sb-contentColumn)
  ```
- **Class naming**: mixed global BEM-like `sb-*` and CSS-module hashed suffixes.
- **Default theme**: light, white nav and white/cream page surfaces.
- **Font loading**: SoDoSans plus Helvetica Neue fallback; Lander Tall only for rewards contexts.
- **Canonical anchor**: global nav + product promotion tile + pill CTA.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `SoDoSans` for most UI and campaign copy.
- **Specialty font**: `Lander Tall` for rewards-themed headlines.
- **Code font**: `monospace` appears only as a generic declaration.
- **Weight normal / bold**: `400` / `700`; buttons commonly use `600`.

```css
:root {
  --sb-font-family: "SoDoSans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --sb-font-family-rewards: "Lander Tall", "Iowan Old Style", Georgia, serif;
  --sb-font-weight-normal: 400;
  --sb-font-weight-button: 600;
  --sb-font-weight-bold: 700;
}
body {
  font-family: var(--sb-font-family);
  font-weight: var(--sb-font-weight-normal);
}
```

### Note on Font Substitutes

- **SoDoSans** - Use `Helvetica Neue` first, then Arial/system sans. Keep weight 400 for body and 600 for controls; jumping to 500 makes the nav and buttons feel less Starbucks because the real extraction shows 400/600/700, not 500.
- **Lander Tall** - If unavailable, use `Iowan Old Style` or Georgia only in rewards or editorial accent contexts. Do not replace the full site with a serif.
- **Optical correction** - Body line-height should stay near 1.5; display and button contexts tighten to 1.2. Letter-spacing is not the main craft lever here.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `--textSize1` | 1.3rem | 400 | 1.5 | 0 |
| `--textSize2` | 1.4rem | 400/600 | 1.5 | 0 |
| `--textSize3` | 1.6rem | 400/600 | 1.5 | 0 |
| `--textSize4` | 1.9rem | 600 | 1.2 | 0 |
| `--textSize5` | 2.0rem | 600/700 | 1.2 | 0 |
| `--textSize6` | 2.2rem | 600/700 | 1.2 | 0 |
| `--textSize7` | 2.4rem | 700 | 1.2 | 0 |
| `--textSize8` | 2.8rem | 700 | 1.2 | 0 |
| `--textSize9` | 3.6rem | 700 | 1.2 | 0 |
| `--textSize10` | 5.0rem | 700 | 1.2 | 0 |

> ⚠️ Scale extraction found named text sizes but no full semantic h1/h2 ladder. Treat `--textSize*` as the factual ladder and map headings manually by context.

### Principles

1. Body text is ordinary and stable: SoDoSans 400 with 1.5 line-height.
2. Controls are firmer than body: buttons use 600, not 400.
3. Display weight resolves through 700 for retail emphasis; 500 is deliberately absent in the extracted weight set.
4. Rewards is a typographic sub-brand: Lander Tall appears only where rewards-specific tone is needed.
5. Starbucks avoids extreme tracking craft; brand recognition comes from weight, color, and tile rhythm.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp

| Token | Hex |
|---|---|
| `--colorGreenAccent` | #00754A |
| `--colorGreenStarbucks` | #006241 |
| `--colorHouseGreen` | #1E3932 |
| `--colorGreenUplift` | #2B5148 |
| `--colorGreenLight` | #D4E9E2 |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `--colorHouseGreen` | #1E3932 |
| `--colorGreenUplift` | #2B5148 |
| `--rewardsGreen` | #33433D |

### 06-3. Neutral Ramp

| Step | Token | Hex / Value |
|---|---|---|
| White | `--colorWhite` | #FFFFFF |
| Cool neutral | `--colorNeutralCool` | #F9F9F9 |
| Warm neutral | `--colorNeutralWarm` | #F2F0EB |
| Ceramic | `--colorCeramic` | #EDEBE9 |
| Text black | `--colorTextBlack` | rgba(0,0,0,.87) |
| Soft black | `--colorTextBlackSoft` | rgba(0,0,0,.58) |
| Black | `--colorBlack` | #000000 |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Gold | `--colorGold` | #CBA258 |
| Gold light | `--colorGoldLight` | #DFC49D |
| Gold lightest | `--colorGoldLightest` | #FAF6EE |
| Red | `--colorRed` | #C82014 |
| Yellow | `--colorYellow` | #FBBC05 |
| Gold lightest | `--colorGoldLightest` | #FAF6EE |

### 06-5. Semantic

| Token | Hex / Value | Usage |
|---|---|---|
| `--colorGreenAccent` | #00754A | Positive CTA, hover accents, active nav underline |
| `--colorHouseGreen` | #1E3932 | Dark green brand surfaces |
| `--colorGreenStarbucks` | #006241 | Starbucks institutional green |
| `--colorRed` | #C82014 | Error or warning color family |
| `--colorTextBlack` | rgba(0,0,0,.87) | Primary readable text |
| `--colorTextBlackSoft` | rgba(0,0,0,.58) | Secondary copy |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--frapBgColor` | `--colorGreenAccent` -> #00754A | floating rounded action button |
| `--frapMiniBgColor` | `--colorWhite` -> #FFFFFF | mini floating action surface |
| `--cardBackgroundColor` | #FFFFFF | card surface |
| `--sliderColor` | #006241 | rewards slider/control accent |
| `--validFieldTintBackground` | hsl(`--colorGreenLightHsl` / 33%) | focused valid field tint |
| `--invalidFieldTintBackground` | hsl(`--colorRedHsl` / 5%) | invalid field tint |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| `--colorWhite` | #FFFFFF | 21 |
| `--colorGreenStarbucks` | #006241 | 6 |
| `--colorGreenAccent` | #00754A | 6 |
| `--colorBlack` | #000000 | 4 |
| `--colorGreenLight` | #D4E9E2 | 3 |
| `--colorCeramic` | #EDEBE9 | 3 |
| `--colorNeutralWarm` | #F2F0EB | 3 |
| `--colorGoldLightest` | #FAF6EE | 3 |

### 06-8. Color Stories

**`--colorGreenAccent` (#00754A)** - The action green. It powers positive buttons, text links, hover treatments, and focus affordances. Use it for "do the thing", not as a general background wash.

**`--colorWhite` (#FFFFFF)** - The structural chrome. Nav, cards, and cookie modal surfaces use white so the seasonal drink photography and cream blocks can carry mood.

**`--colorHouseGreen` (#1E3932)** - The deeper brand field. It is for signage-like dark green surfaces and high-contrast white copy, not for every CTA.

**`--colorCeramic` (#EDEBE9)** - The warm utility neutral. It appears as a soft background and hover surface, keeping the site from feeling like a cold SaaS dashboard.

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---:|---|
| `--space-1` | 4px / .4rem | smallest inset and label padding |
| `--space-2` | 8px / .8rem | button group spacing, small gaps |
| `--space-3` | 16px / 1.6rem | mobile outer gutter, logo margin |
| `--space-4` | 24px / 2.4rem | medium gutter, modal padding |
| `--space-5` | 32px / 3.2rem | button height |
| `--space-6` | 40px / 4rem | mini floating action height |
| `--space-7` | 48px / 4.8rem | subnav height neighborhood |
| `--space-8` | 56px / 5.6rem | floating action height |
| `--space-9` | 64px / 6.4rem | large layout offset |

**주요 alias**:
- `--outerGutter` -> 1.6rem (mobile page gutter)
- `--outerGutterMedium` -> 2.4rem (tablet gutter)
- `--outerGutterLarge` -> 4.0rem (desktop gutter)
- `--columnWidthXLarge` -> 1440px (max layout width)
- `--logoOffsetMd` -> 99px and `--logoOffsetLg` -> 131px (logo-aware layout offset)

### Whitespace Philosophy

Starbucks uses spacing like store signage. The nav is tall enough to feel like a fixed retail header, while campaign tiles below can be dense and promotional. The key is contrast: a 99px desktop nav with a strong logo rhythm, then broad content columns that let product photography occupy half the band.

The spacing scale is practical rather than precious. It is a 4/8/16/24/32 ladder extended to 64px, with 1440px as the outer width. Avoid delicate 13px or 27px custom gaps; the site prefers sturdy increments that can survive marketing content changes.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `--buttonBorderRadius` | 50px | default pill buttons |
| `--cardBorderRadius` | 12px | cards and content containers |
| `--frap` radius | 500px | floating action pill/circle |
| skip link radius | 50px | accessibility skip link |
| heading bottom border radius | 12px | green underline treatment |
| tile link radius | 8px | list-image-left hover background |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| `--globalNavBoxShadow` | `0 1px 3px rgba(0,0,0,0.1), 0 2px 2px rgba(0,0,0,0.06), 0 0 2px rgba(0,0,0,0.07)` | global nav elevation |
| `--cardBoxShadow` | `0px 0px .5px 0px rgba(0,0,0,0.14), 0px 1px 1px 0px rgba(0,0,0,0.24)` | card elevation |
| `--frapShadowPrimary` | `0 0 6px rgba(0,0,0,0.24)` | floating action glow |
| `--frapShadowSecondary` | `0 8px 12px rgba(0,0,0,0.14)` | floating action lift |
| `--svcShadowFilter` | `drop-shadow(0px 4px 1px rgba(0,0,0,0.11)) drop-shadow(0px 0px 2px rgba(0,0,0,0.24))` | service/product graphic shadow |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `--buttonTransition` | `all 0.2s ease` | button hover and state transitions |
| `--buttonActiveScale` | `scale(0.95)` | press feedback |
| `--expanderDuration` | `300ms` | expandable panels |
| `--expanderTimingCurve` | `cubic-bezier(0.25,0.46,0.45,0.94)` | expander easing |
| `--imageFadeTransition` | `opacity 0.3s ease-in` | image loading fade |
| `.caret` transition | `transform .3s ease-out` | dropdown caret rotation |
| `.sb-button--loadingCircle` | `.75s linear infinite` | loading spinner |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: 1440px (`--columnWidthXLarge`)
- **Grid type**: flex and module-specific grids; content columns use max-width classes rather than a visible 12-column design language.
- **Column count**: common homepage promo pattern is two equal columns: product image block + copy block.
- **Gutter**: 1.6rem mobile, 2.4rem tablet, 4.0rem desktop.

### Hero

- **Pattern Summary**: `two-column seasonal product tile + white global nav + compact pill CTA`
- Layout: split image/copy band on the visible homepage capture; hero modules also support background-image heroes.
- Background: campaign-specific solid or image-backed surfaces, often warm neutral or green.
- **Background Treatment**: solid campaign color plus product photography; hero module supports `linear-gradient(180deg, hsla(...))` image overlay for background heroes.
- H1: observed campaign headline uses SoDoSans, green, 600/700 weight, centered in copy column.
- Max-width: 1440px page cap, hero card max-width 450px in background-hero mode.

### Section Rhythm

```css
.sb-global-gutters {
  padding-left: 1.6rem;
  padding-right: 1.6rem;
}
@media (min-width: 768px) {
  .sb-global-gutters { padding-left: 2.4rem; padding-right: 2.4rem; }
}
@media (min-width: 1024px) {
  .sb-global-gutters { padding-left: 4.0rem; padding-right: 4.0rem; }
}
```

### Card Patterns

- **Card background**: #FFFFFF (`--cardBackgroundColor`)
- **Card border**: not primary; surface and shadow define cards.
- **Card radius**: 12px.
- **Card padding**: module-specific; button/list spacing uses 8px and 12px aliases.
- **Card shadow**: tiny two-layer shadow, not heavy depth.

### Navigation Structure

- **Type**: horizontal desktop nav with logo, primary links, store link, auth buttons; hamburger on mobile.
- **Position**: relative by default, fixed variant exists.
- **Height**: 64px xs, 72px mobile, 83px tablet, 99px desktop.
- **Background**: #FFFFFF.
- **Border**: no hard border; multi-layer shadow is the separator.

### Content Width

- **Prose max-width**: 500px/720px contexts via `--columnWidthMedium` and `--columnWidthLarge`.
- **Container max-width**: 1440px.
- **Sidebar width**: no persistent sidebar on homepage; footer columns use 190px width.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Small mobile | 375px | additional small-device tuning |
| Mobile landscape | 480px | minor tile and layout adjustments |
| Tablet | 768px | medium gutters and larger nav/logo states |
| Desktop | 1024px | desktop nav and layout offsets |
| Wide desktop | 1280px | large content behavior |
| Max layout | 1520px / 1600px / 1702px | wide-screen refinements |

### Touch Targets

- **Minimum tap size**: global menu button width is 44px; button height resolves to 32px for compact pills, while nav height provides larger tap bands.
- **Button height (mobile)**: `--buttonHeight` -> 3.2rem.
- **Input height (mobile)**: derived from field padding 12px plus label behavior; exact fixed height not surfaced in phase1.

### Collapsing Strategy

- **Navigation**: desktop links collapse to hamburger/menu button below desktop.
- **Grid columns**: two-column product bands collapse to stacked modules on narrower widths.
- **Sidebar**: homepage has no persistent sidebar.
- **Hero layout**: background-hero mode switches content positioning; visible product tile should stack image/copy on small viewports.

### Image Behavior

- **Strategy**: product imagery uses block images with `max-width: 100%` and module-specific object fit.
- **Max-width**: card images are `max-width: 100%`; some tile image rules set `width: 100%` and `max-width: none`.
- **Aspect ratio handling**: module-managed; exact aspect-ratio token not extracted.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

```html
<a class="sb-button sb-button--positive sb-button--rewardsGreen" href="/menu">Give them a try</a>
```

| Property | Value |
|---|---|
| Base class | `.sb-button` |
| Radius | `var(--buttonBorderRadius)` -> 50px |
| Padding | `var(--buttonPadding)` -> 7px 16px |
| Weight | 600 |
| Line-height | 1.2 |
| Transition | `all 0.2s ease` |
| Active | `transform: scale(0.95)` |
| Disabled | `opacity: .5; cursor: not-allowed` |
| Loading | circular spinner, button becomes `--buttonHeight` square |

### Badges

> N/A - no strong badge system surfaced in the homepage CSS slice. Use pill button or text link patterns instead of inventing badges.

### Cards & Containers

```html
<article class="sb-card sb-card-shadow">
  <img class="sb-card__image" alt="" />
  <div class="sb-card__content">...</div>
</article>
```

| Property | Value |
|---|---|
| Surface | #FFFFFF |
| Radius | 12px |
| Shadow | `--cardBoxShadow` |
| Image fit | `object-fit: contain; object-position: center` |
| Layout variants | image left, image right, image small |

### Navigation

```html
<header class="sb-globalNav">
  <nav class="sb-globalNav__nav bg-white" aria-label="Global">...</nav>
</header>
```

| Property | Value |
|---|---|
| Desktop height | 99px |
| Logo size | 32px -> 40px -> 51px across breakpoints |
| Shadow | `--globalNavBoxShadow` |
| Active link | inset bottom 6px #00754A |
| Link hover | color #00754A |
| Menu button | 44px tap width |

### Inputs & Forms

```html
<label class="floatLabel">Email address</label>
<div class="sb-fieldBase__childWrapper">...</div>
```

| Property | Value |
|---|---|
| Field padding | 12px |
| Floating label left | 12px |
| Label active top | -12px |
| Mobile label size | 1.6rem -> active 1.3rem |
| Desktop label size | 1.9rem -> active 1.4rem |
| Focus ring | 2px #00754A box-shadow |
| Invalid focus | 2px #C82014 box-shadow with red tint |

### Hero Section

```html
<section class="hero_hero__yuMFA">
  <div class="hero_content__iFArt">
    <div class="hero_card__9ebAI">...</div>
  </div>
</section>
```

| Property | Value |
|---|---|
| Background mode | solid color, product image, or background image |
| Background hero | optional black surface + gradient overlay |
| Content mode | centered card or split campaign tile |
| Card max-width | 450px |
| Content desktop padding | 11.2rem, card mode 7rem |
| Reveal | inner transforms from translateY(10%) and opacity 0 |

### 13-2. Named Variants

- **button-default-green** - transparent pill, color #00754A, hover #00754A at 10% alpha.
- **button-positive-green** - filled #00754A pill, white text, hover uses 90% alpha.
- **button-positive-black** - filled #000000 pill for account/auth CTAs, hover #000000 at 70% alpha.
- **button-positive-white** - white pill on dark green surfaces, text rgba(0,0,0,.87).
- **button-text-green** - borderless text-style action, hover #00754A at 8% alpha.
- **frap-primary** - large rounded floating action, #00754A, 500px radius, dual shadow.
- **card-shadow** - white 12px card with tiny two-layer elevation.

### 13-3. Signature Micro-Specs

#### green-pill-press

```yaml
green-pill-press:
  description: "Starbucks action controls feel tactile because every pill slightly compresses when pressed."
  technique: "border-radius: 50px; padding: 7px 16px; transition: all 0.2s ease; active transform: scale(0.95)"
  applied_to: ["{component.button-default}", "{component.button-positive}"]
  visual_signature: "A compact cafe-ordering control, closer to an order sticker than a large SaaS CTA."
```

#### nav-signage-shadow

```yaml
nav-signage-shadow:
  description: "The global nav reads as a fixed store sign hovering above changing campaign boards."
  technique: "box-shadow: 0 1px 3px rgba(0,0,0,0.1), 0 2px 2px rgba(0,0,0,0.06), 0 0 2px rgba(0,0,0,0.07); desktop height: 99px; background: #FFFFFF"
  applied_to: ["{component.navigation}"]
  visual_signature: "Crisp white retail fascia with no hard border, only a soft multi-layer separator."
```

#### frap-dual-lift

```yaml
frap-dual-lift:
  description: "Floating rounded actions use the heaviest Starbucks elevation, separating utility from ordinary cards."
  technique: "border-radius: 500px; background: #00754A; box-shadow: 0 0 6px rgba(0,0,0,0.24), 0 8px 12px rgba(0,0,0,0.14)"
  applied_to: ["{component.frap}"]
  visual_signature: "A green floating service button lifted like a small physical puck above the page."
```

#### floating-label-green-tint

```yaml
floating-label-green-tint:
  description: "Form focus states tint the field interior instead of relying only on an outline."
  technique: "padding: 12px; label top: -12px; box-shadow: 0 0 0 2px #00754A; background: hsl(--colorGreenLightHsl / 33%)"
  applied_to: ["{component.inputs}", "{component.forms}"]
  visual_signature: "On-brand soft validation feedback, more like a lit field than a generic browser focus ring."
```

#### service-graphic-double-drop

```yaml
service-graphic-double-drop:
  description: "Service/product graphics get their own filtered shadow while ordinary UI chrome stays restrained."
  technique: "filter: drop-shadow(0px 4px 1px rgba(0,0,0,0.11)) drop-shadow(0px 0px 2px rgba(0,0,0,0.24))"
  applied_to: ["{component.service-graphic}", "{component.product-graphic}"]
  visual_signature: "Photography and service imagery carry the tactile depth; cards and chrome remain comparatively flat."
```

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | Short retail invitation or product news | "New Energy Refreshers just dropped" |
| Primary CTA | Verb phrase, direct and friendly | "Give them a try" |
| Utility CTA | Account/store task language | "Find a store", "Sign in", "Join now" |
| Subheading | Describes benefit in plain customer language | "extra caffeine from nature and a B-vitamin boost" |
| Tone | Familiar, commerce-forward, seasonal | coffee, refreshers, reset, rewards |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Starbucks - copy into your root stylesheet */
:root {
  /* Fonts */
  --sb-font-family: "SoDoSans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --sb-font-family-rewards: "Lander Tall", "Iowan Old Style", Georgia, serif;
  --sb-font-weight-normal: 400;
  --sb-font-weight-button: 600;
  --sb-font-weight-bold: 700;

  /* Brand */
  --sb-color-green-accent: #00754A;
  --sb-color-green-starbucks: #006241;
  --sb-color-house-green: #1E3932;
  --sb-color-green-light: #D4E9E2;
  --sb-color-gold: #CBA258;

  /* Surfaces */
  --sb-bg-page: #FFFFFF;
  --sb-bg-warm: #F2F0EB;
  --sb-bg-ceramic: #EDEBE9;
  --sb-text: rgba(0,0,0,.87);
  --sb-text-muted: rgba(0,0,0,.58);

  /* Spacing */
  --sb-space-2: 8px;
  --sb-space-3: 16px;
  --sb-space-4: 24px;
  --sb-space-5: 32px;
  --sb-outer-gutter: 1.6rem;
  --sb-outer-gutter-md: 2.4rem;
  --sb-outer-gutter-lg: 4rem;

  /* Components */
  --sb-button-radius: 50px;
  --sb-button-padding: 7px 16px;
  --sb-card-radius: 12px;
  --sb-nav-shadow: 0 1px 3px rgba(0,0,0,.1), 0 2px 2px rgba(0,0,0,.06), 0 0 2px rgba(0,0,0,.07);
}

.sb-like-button {
  display: inline-block;
  border: 1px solid currentColor;
  border-radius: var(--sb-button-radius);
  padding: var(--sb-button-padding);
  font-family: var(--sb-font-family);
  font-weight: var(--sb-font-weight-button);
  line-height: 1.2;
  transition: all 0.2s ease;
}
.sb-like-button:active { transform: scale(0.95); }
.sb-like-button--positive {
  background: var(--sb-color-green-accent);
  border-color: var(--sb-color-green-accent);
  color: #FFFFFF;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js - Starbucks-inspired token bridge
module.exports = {
  theme: {
    extend: {
      colors: {
        starbucks: {
          accent: '#00754A',
          green: '#006241',
          house: '#1E3932',
          light: '#D4E9E2',
          warm: '#F2F0EB',
          ceramic: '#EDEBE9',
          gold: '#CBA258',
          red: '#C82014',
        },
      },
      fontFamily: {
        sans: ['SoDoSans', 'Helvetica Neue', 'Helvetica', 'Arial', 'sans-serif'],
        rewards: ['Lander Tall', 'Iowan Old Style', 'Georgia', 'serif'],
      },
      fontWeight: {
        normal: '400',
        button: '600',
        bold: '700',
      },
      borderRadius: {
        button: '50px',
        card: '12px',
        frap: '500px',
      },
      boxShadow: {
        nav: '0 1px 3px rgba(0,0,0,.1), 0 2px 2px rgba(0,0,0,.06), 0 0 2px rgba(0,0,0,.07)',
        card: '0px 0px .5px 0px rgba(0,0,0,.14), 0px 1px 1px 0px rgba(0,0,0,.24)',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex / Value |
|---|---|---|
| Brand primary | `--colorGreenAccent` | #00754A |
| Brand institutional | `--colorGreenStarbucks` | #006241 |
| Dark brand surface | `--colorHouseGreen` | #1E3932 |
| Background | `--colorWhite` | #FFFFFF |
| Warm background | `--colorNeutralWarm` | #F2F0EB |
| Border/soft surface | `--colorCeramic` | #EDEBE9 |
| Text primary | `--colorTextBlack` | rgba(0,0,0,.87) |
| Text muted | `--colorTextBlackSoft` | rgba(0,0,0,.58) |
| Error | `--colorRed` | #C82014 |

### Example Component Prompts

#### Hero Section

```text
Starbucks 스타일의 시즌 프로모션 히어로를 만들어줘.
- 구조: 1440px max-width 안에서 이미지 50%, 카피 50%의 split campaign tile
- 배경: warm campaign surface #FAF6EE 또는 #F2F0EB
- 텍스트: SoDoSans, headline 2.4rem-3.6rem, weight 700, color #00754A 또는 #1E3932
- CTA: pill button, border #00754A, radius 50px, padding 7px 16px, weight 600
- 사진: 음료 제품 사진이 감정의 중심이 되게 크게 배치
```

#### Card Component

```text
Starbucks 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF
- radius: 12px
- shadow: 0px 0px .5px rgba(0,0,0,.14), 0px 1px 1px rgba(0,0,0,.24)
- 이미지: max-width 100%, object-fit contain
- 제목: SoDoSans, 1.9rem 이상, weight 600 또는 700
- CTA는 카드 내부에서도 50px pill로 유지
```

#### Badge

```text
Starbucks는 독립 badge보다 pill CTA와 text link를 우선한다.
작은 상태 표시가 필요하면 #D4E9E2 배경, #1E3932 텍스트, 999px radius를 쓰되
실제 브랜드 핵심 컴포넌트처럼 과장하지 마라.
```

#### Navigation

```text
Starbucks 스타일 상단 네비게이션을 만들어줘.
- 높이: desktop 99px, mobile 64-72px
- 배경: #FFFFFF
- shadow: 0 1px 3px rgba(0,0,0,.1), 0 2px 2px rgba(0,0,0,.06), 0 0 2px rgba(0,0,0,.07)
- 로고: 왼쪽, desktop 51px
- 링크: uppercase 느낌의 짧은 메뉴, hover #00754A
- 우측: Find a store, Sign in outline pill, Join now black filled pill
```

### Iteration Guide

- **색상 변경 시**: #00754A, #006241, #1E3932를 역할별로 분리한다. 하나의 green으로 통합하지 않는다.
- **폰트 변경 시**: SoDoSans가 없으면 Helvetica Neue로 대체하고, body 400/button 600/headline 700 구조는 유지한다.
- **여백 조정 시**: 4/8/16/24/32/40/48/56/64px ladder에서 고른다.
- **새 컴포넌트 추가 시**: 버튼은 50px pill, 카드는 12px radius, nav는 shadow separator를 따른다.
- **다크 그린 섹션**: #1E3932 위에는 white text와 white/outline controls를 사용한다.
- **캠페인 영역**: product photography와 warm surfaces를 우선하고, UI chrome 장식은 줄인다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#00754A` for primary interactive actions and hover accents.
- Keep `#006241` and `#1E3932` as separate institutional/dark surface greens.
- Use SoDoSans with 400/600/700 weight rhythm.
- Make primary controls pill-shaped with `border-radius: 50px`.
- Let drink photography and seasonal blocks carry the campaign color.
- Use the 1440px max-width and 1.6rem/2.4rem/4rem gutter ladder.
- Keep nav white with the multi-layer shadow instead of a hard border.

### ❌ DON'T

- 배경을 전체적으로 `#000000` 또는 `black`으로 두지 말 것 - 대신 기본 chrome은 `#FFFFFF`, dark brand band는 `#1E3932` 사용.
- 텍스트를 순수 `#000000`만으로 고정하지 말 것 - 기본 본문은 `rgba(0,0,0,.87)`, 보조 텍스트는 `rgba(0,0,0,.58)` 사용.
- CTA green을 `#006241`로 통일하지 말 것 - interactive primary는 `#00754A`, institutional green은 `#006241` 사용.
- warm campaign surface를 차가운 `#F9F9F9`만으로 대체하지 말 것 - Starbucks warmth에는 `#F2F0EB`, `#EDEBE9`, `#FAF6EE` 사용.
- 버튼을 4px 또는 8px radius 사각형으로 만들지 말 것 - pill control은 `border-radius: 50px` 사용.
- button body에 `font-weight: 400` 사용 금지 - Starbucks button은 600이 맞다.
- 카드를 큰 neumorphic shadow로 띄우지 말 것 - 실제 card shadow는 `0px 0px .5px rgba(0,0,0,0.14), 0px 1px 1px rgba(0,0,0,0.24)`처럼 작다.
- hover 효과에 큰 translate/bounce를 넣지 말 것 - 실제 tactile state는 `scale(0.95)` active와 subtle background tint다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **Second action green**: none - `#00754A` carries primary action; `#006241` is not a substitute CTA color.
- **Purple/blue SaaS gradient**: absent - no generic violet-to-indigo SaaS visual language.
- **Sharp rectangular primary buttons**: never - core action shape is pill.
- **Weight 500**: absent in extracted set - 400, 600, and 700 define the rhythm.
- **Heavy chrome shadows**: none - depth stays tiny except floating action controls.
- **Cold monochrome dashboard palette**: absent - warm neutrals and campaign surfaces keep the retail tone.
- **Decorative icon swarms**: absent - product photography, not iconography, carries emotion.
- **Glassmorphism cards**: none - no blur-backed translucent UI chassis in the analyzed homepage CSS.
- **Overbuilt motion**: absent - no particle, parallax, custom cursor, or scroll-scrub dependency observed.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Cookie modal occlusion** - the available hero screenshot contains a cookie consent modal over the first viewport. Layout and campaign interpretation use the visible portions plus HTML/CSS facts.
- **Single public homepage snapshot** - this analysis does not visit checkout, account settings, store locator results, rewards subflows, or menu item detail pages.
- **CSS is minified and module-hashed** - component semantics are inferred from stable global classes and readable module prefixes, not from source Sass/React component names.
- **Typography scale lacks semantic h1/h2 tokens** - `--textSize*` variables are factual, but heading mapping is manual.
- **Image dimensions and exact campaign module ratios** - screenshots and CSS confirm split/product patterns, but exact image asset metadata was not exhaustively measured.
- **Dark-mode mapping not present** - dark green sections exist, but a complete light/dark token pair system was not extracted.
- **Form states partially observed from CSS only** - focus, invalid, float label, and tint rules exist; live form validation flows were not exercised.
- **Motion behavior is CSS-level only** - transitions and animation tokens were extracted, but any JavaScript-triggered intersection timing was not traced.
- **Brand candidates may include campaign colors** - warm campaign colors are treated as seasonal surfaces unless they also appear as stable CSS tokens such as #F2F0EB, #EDEBE9, or #FAF6EE.
