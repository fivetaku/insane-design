---
schema_version: 3.2
slug: kakaocorp
service_name: Kakao Corp
site_url: https://www.kakaocorp.com/
fetched_at: 2026-05-03T15:37:49+0900
default_theme: light
brand_color: "#FFCD00"
primary_font: KakaoBig
font_weight_normal: 400
token_prefix: kakao

bold_direction: Soft Utility Stage
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: other
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "A coherent production system is visible in custom Kakao fonts, repeated radii, spacing variables, and responsive breakpoints, but the CSS exposes few named semantic design tokens."

colors:
  brand-yellow: "#FFCD00"
  kakao-yellow: "#FEE500"
  surface-white: "#FFFFFF"
  ink-primary: "#333333"
  ink-black: "#000000"
  ink-muted: "#666666"
  hero-gray: "#8E8E8E"
  surface-soft: "#F9F9F9"
  line-light: "#E5E5E5"
  alert-red: "#FF0919"

typography:
  display: "KakaoBig"
  body: "KakaoSmall"
  digit: "KakaoDigitLatin"
  ladder:
    - { token: hero-title, size: "60px", weight: 700, line_height: "1.18", tracking: "-2px" }
    - { token: section-title, size: "42px", weight: 700, line_height: "1.38", tracking: "-1px" }
    - { token: card-title, size: "26px", weight: 700, line_height: "34px", tracking: "-0.6px" }
    - { token: body-large, size: "18px", weight: 400, line_height: "28px", tracking: "-0.2px" }
    - { token: body, size: "16px", weight: 400, line_height: "24px", tracking: "-0.2px" }
    - { token: nav, size: "14px", weight: 700, line_height: "1.5", tracking: "0" }
  weights_used: [300, 400, 700, 800]
  weights_absent: [500, 600, 900]

components:
  button-kakao-download: { bg: "{colors.brand-yellow}", color: "{colors.ink-black}", radius: "999px", border: "2px solid #000000", padding: "7px 13px" }
  button-glass-utility: { bg: "rgba(255,255,255,.18)", color: "{colors.surface-white}", radius: "999px", border: "none", padding: "14px 30px" }
  search-speech-bubble: { bg: "#2F2F2F", color: "{colors.surface-white}", radius: "24px", border: "3px solid #FFFFFF", height: "64px" }
  card-soft-surface: { bg: "{colors.surface-soft}", radius: "24px", shadow: "4px 12px 40px 6px rgba(0,0,0,.09)" }
---

# DESIGN.md - Kakao Corp

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Kakao Corp's homepage behaves less like a conventional corporate brochure and more like a public utility stage that has been temporarily converted into a KakaoTalk room. The hero is a wide gray field, populated by full-body people using phones, with a centered headline floating over them. It does not shout with brand yellow; it lets the people and the product action carry the scene, then reserves `#FFCD00` (`{colors.brand-yellow}`) for the specific KakaoTalk download action.

The visual system is built on a deliberately soft collision: friendly consumer product language wrapped in public-company navigation. The header is a white civic lobby: logo, categories, utility icons, no ceremony. Immediately below it, the page becomes a muted gray plaza where people are staged like a public-service campaign, not a product mockup wall. The site is not showing software behind glass; it is showing the social situation the software wants to occupy.

Color is mostly neutral. `#FFFFFF` (`{colors.surface-white}`), `#333333` (`{colors.ink-primary}`), and `#000000` (`{colors.ink-black}`) dominate the CSS, while `#FFCD00` (`{colors.brand-yellow}`) and `#FEE500` (`{colors.kakao-yellow}`) are rationed to brand-specific actions. Yellow works like a small call button on a public counter, not wallpaper. The screenshot's most memorable color is actually the muted gray stage behind the people; Kakao refuses the obvious yellow flood and makes the logo color more powerful by withholding it.

Typography supplies the authority that color refuses to overperform. KakaoBig headlines land with compact Hangul pressure, as if the letters have been optically squeezed into a poster rather than typed into a web template. The heavy negative tracking is the difference between a corporate announcement and a message bubble enlarged to billboard scale.

The signature craft is not a complex token architecture. It is the combination of native Kakao typefaces, heavy negative tracking, capsule controls, and a dark speech-bubble search bar that feels like a chat input scaled into a corporate navigation object. The search field is not an input box; it is a chat balloon parked at the front desk of the company site. That is the system's personality: a company page that keeps behaving like a messenger.

### Key Characteristics

- White 73px desktop header with black Kakao wordmark and compact navigation.
- Hero uses a gray photographic stage with multiple human cutouts rather than a product mockup.
- Main headline is white, very large, and tightly tracked over a dimmed hero background.
- Kakao yellow appears as an action accent, not a full-page brand wash.
- Search becomes a speech-bubble object: dark fill, thick white outline, rounded tail.
- Controls are circular or pill-shaped; rectangular corporate buttons are mostly avoided.
- Typography uses KakaoBig for display and KakaoSmall for interface/body.
- Letter-spacing is aggressively negative across many sizes (`-.5px`, `-.6px`, `-1px`, `-2px`).
- Shadows are present on content cards but absent from the hero people/chrome relationship.
- Responsive breakpoints are explicit at `1439px`, `1023px`, `767px`, and `411px`.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Soft Utility Stage
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **gray people-stage hero plus messenger-like speech-bubble search**으로 기억된다.
> **Code Complexity**: high — large compiled CSS, custom font families, multiple responsive variable overrides, and rich homepage modules despite sparse semantic token naming.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Kakao Corp처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Kakao type pairing */
body {
  font-family: "KakaoSmall", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
  font-weight: 400;
  color: #333333;
}

h1,
h2,
.display {
  font-family: "KakaoBig", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
  font-weight: 700;
  letter-spacing: -0.5px;
}

/* 2. Neutral corporate floor */
:root {
  --kakao-bg: #FFFFFF;
  --kakao-fg: #333333;
  --kakao-muted: #666666;
  --kakao-line: #E5E5E5;
}

/* 3. Brand accent as a rationed action color */
:root {
  --kakao-brand: #FFCD00;
  --kakao-talk: #FEE500;
}
```

**절대 하지 말아야 할 것 하나**: 카카오를 노란 배경 사이트로 만들지 말 것. 실제 메인은 흰색/회색/검정 구조 위에 `#FFCD00` CTA를 좁게 얹는다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.kakaocorp.com/` |
| Fetched | 2026-05-03T15:37:49+0900 |
| Extractor | reused phase1 artifacts: HTML, CSS, screenshot, JSON summaries |
| HTML size | 156542 bytes |
| CSS files | 1 external CSS file, 625287 bytes |
| Screenshot | `insane-design/kakaocorp/screenshots/hero-cropped.png` |
| Token prefix | `kakao` (synthetic documentation prefix; source CSS uses sparse generic variables) |
| Method | CSS frequency + phase1 JSON + screenshot observation; no new full-site crawl |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: SSR-rendered JavaScript site; HTML includes a JavaScript-required message and Nuxt-style `data-n-head="ssr"` meta attributes.
- **Design system**: Kakao production web system. The source exposes custom Kakao fonts and layout variables, but not a deep semantic color-token API.
- **CSS architecture**: large compiled stylesheet with component selectors, repeated responsive overrides, and a small number of root/layout variables.
  ```css
  --viewport-height: 100dvh;
  --navigation-height: 47px;
  --wrap-tit-width: 405px;
  --wrap-info-width: 618px;
  --breakpoint-width: 1023px;
  ```
- **Class naming**: component-scoped descriptive classes, not Tailwind utility output.
- **Default theme**: light. Header and most content surfaces are `#FFFFFF`; hero uses a muted gray photographic stage.
- **Font loading**: custom Kakao font families referenced in CSS: `KakaoBig`, `KakaoSmall`, `KakaoDigitLatin`.
- **Canonical anchor**: homepage hero and corporate navigation, not logged-in product UI.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `KakaoBig`
- **Body/UI font**: `KakaoSmall`
- **Digit font**: `KakaoDigitLatin`
- **Fallbacks**: `Apple SD Gothic Neo`, `Malgun Gothic`, `맑은 고딕`, `sans-serif`
- **Weight normal / bold**: `400` / `700`
- **Observed weights**: `300`, `400`, `700`, `800`

```css
:root {
  --kakao-font-display: "KakaoBig", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
  --kakao-font-body: "KakaoSmall", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
  --kakao-font-digit: "KakaoDigitLatin", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
}

body,
button,
input,
select,
td,
textarea,
th {
  font-size: 14px;
  line-height: 1.5;
  font-family: var(--kakao-font-body);
  font-weight: 400;
  color: #333333;
}
```

### Note on Font Substitutes

- **KakaoBig substitute** — Use `Pretendard` or `SUIT` at weight `700`, then tighten display tracking by roughly `-0.02em`. KakaoBig has a compact Hangul headline presence; leaving tracking at `0` makes the hero feel too loose.
- **KakaoSmall substitute** — Use `Pretendard` at `400` for body and `700` for navigation. Keep Korean body line-height around `1.5`; do not switch to a Latin-first 1.25 rhythm.
- **KakaoDigitLatin substitute** — Use `Inter` only for digits or metric labels. Do not use Inter as the entire Korean UI face unless no Korean-first font is available.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `hero-title` | `60px` | `700` | `1.18` | `-2px` |
| `section-title-xl` | `42px` | `700` | `1.38` | `-1px` |
| `section-title` | `36px` | `700` | `40px` | `-.8px` |
| `card-title-lg` | `30px` | `700` | `36px` | `-.6px` |
| `card-title` | `26px` | `700` | `34px` | `-.6px` |
| `body-lg` | `18px` | `400` | `28px` | `-.2px` |
| `body` | `16px` | `400` | `24px` | `-.2px` |
| `caption/nav` | `14px` | `700` | `1.5` | `0` |
| `micro` | `12px` | `400/700` | `18px` | `0` |

> ⚠️ Kakao Corp's typography is not a generic system-font stack. The visual identity depends on KakaoBig's heavy display face and persistent negative tracking.

### Principles

1. Display text uses KakaoBig first; body and controls use KakaoSmall first.
2. The system prefers weight `700` for clear labels and headlines; `500` and `600` are effectively absent in the observed CSS.
3. Negative letter-spacing is a core identity marker, especially `-.5px`, `-.6px`, `-1px`, and `-2px`.
4. Korean body copy stays readable through `24px` to `28px` line-height rather than by using lighter text color.
5. Navigation is small but bold; it relies on white space and alignment rather than oversized text.
6. Digit-specific typography exists, so numeric content should not be treated as ordinary body text.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp

| Token | Hex | Role |
|---|---|---|
| `{colors.kakao-yellow}` | `#FEE500` | Kakao service yellow, close to KakaoTalk product identity |
| `{colors.brand-yellow}` | `#FFCD00` | homepage CTA/action yellow observed in CSS frequency |
| `yellow-soft` | `#FFF5B3` | pale supporting yellow |
| `yellow-warm` | `#FFD600` | stronger yellow variant |
| `yellow-logo` | `#FFE500` | single observed yellow variant |

### 06-2. Brand Dark Variant

> N/A — no complete dark-mode brand ramp was confirmed from the reused phase1 artifacts. The header includes a dark-mode toggle, but this analysis does not claim a full dark palette mapping.

### 06-3. Neutral Ramp

| Step | Hex | Usage |
|---|---|---|
| `surface-white` | `#FFFFFF` | header, most page surfaces, text on dark areas |
| `surface-soft` | `#F9F9F9` | light content blocks |
| `line-light` | `#E5E5E5` | separators and low-contrast borders |
| `line-mid` | `#D2D2D2` | stronger line |
| `ink-muted` | `#666666` | secondary text |
| `ink-primary` | `#333333` | body text |
| `ink-deep` | `#111111` | high-emphasis text/chrome |
| `ink-black` | `#000000` | icons, button borders, logo-like elements |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| red | alert/news accent | `#FF0919` |
| blue | service accent | `#2439DF` |
| blue-light | service accent | `#489FF8` |
| peach | illustration/support | `#FAC6AC` |
| green | illustration/support | `#C7FBC4` |
| sky | illustration/support | `#B7ECFF` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--kakao-bg-page` | `#FFFFFF` | default page background |
| `--kakao-text` | `#333333` | body/UI text |
| `--kakao-text-strong` | `#000000` | logo, icons, button stroke |
| `--kakao-text-muted` | `#666666` | secondary labels |
| `--kakao-border` | `#E5E5E5` | separators |
| `--kakao-action` | `#FFCD00` | primary Kakao-branded action |
| `--kakao-chat-action` | `#FEE500` | KakaoTalk/service action |

### 06-6. Semantic Alias Layer

> N/A — `phase1/alias_layer.json` reports no `util`, `semantic`, `action`, `component`, or `core` tiers. The aliases above are documentation aliases, not source CSS variable names.

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Hex | Frequency | Interpretation |
|---|---:|---|
| `#FFFFFF` | 78 | white surface and inverse text |
| `#000000` | 72 | black icons/chrome/strong contrast |
| `#666666` | 15 | muted text |
| `#E5E5E5` | 13 | hairline/separator |
| `#888888` | 12 | secondary neutral |
| `#111111` | 11 | strong neutral |
| `#8E8E8E` | 9 | gray tone, consistent with hero stage feel |
| `#A1A1A1` | 7 | light gray support |
| `#FFCD00` | 7 | brand/action yellow |
| `#333333` | 6 | body text |

### 06-8. Color Stories

**`{colors.surface-white}` (`#FFFFFF`)** — The corporate shell is white. It gives the header, navigation, and lower content blocks an institutional calm, preventing the brand from turning into a yellow novelty surface.

**`{colors.ink-black}` (`#000000`)** — Black carries the Kakao wordmark, icons, and the outline of the hero's yellow CTA. It gives the otherwise soft system enough snap to remain legible and branded.

**`{colors.ink-primary}` (`#333333`)** — Body text does not sit at pure black. `#333333` is the practical Korean reading color, especially with KakaoSmall at normal weight.

**`{colors.brand-yellow}` (`#FFCD00`)** — Yellow is used as a signpost, not a field. In the hero, it marks the KakaoTalk download action; if overused as a background, the page loses its corporate balance.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--navigation-height` | `47px` | compact navigation state in responsive overrides |
| `--naviHegihtSmall` | `60px` | small navigation height variable |
| `--naviHegihtLarge` | `73px` | desktop header height visible in screenshot |
| `--wrap-tit-width` | `405px / 570px / 808px` | title wrapper widths across breakpoints |
| `--wrap-info-width` | `618px / 869px / 1112px` | information wrapper widths across breakpoints |
| `--list-column-gap` | `16px / 28px / 34px` | card/list grid gaps |
| `hero search width` | `~670px` | central speech-bubble search bar on desktop screenshot |

**주요 alias**:
- `container-tight` -> `405px` title wrapper at smaller desktop/tablet contexts.
- `container-wide` -> `1112px` information wrapper at large desktop contexts.
- `grid-gap-md` -> `28px` list column gap.

### Whitespace Philosophy

Kakao Corp uses whitespace as a switch between two modes. The header is sparse and administrative: logo, five navigation groups, and three utility icons spread across a white bar. The hero, by contrast, spends most of its width on people and empty gray stage, leaving the headline to sit in a theatrical center.

Below the hero, the system becomes more card-like and information-dense. The spacing variables show wrapper widths rather than a clean 4/8 scale, which fits the site: this is a composition system for editorial corporate modules, not a primitive token library.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `radius-xs` | `4px` | small controls/supporting UI |
| `radius-sm` | `6px` | compact chips |
| `radius-md` | `8px` | small cards/buttons |
| `radius-lg` | `12px` | general rounded module |
| `radius-xl` | `16px` | larger cards |
| `radius-2xl` | `20px` | content panels |
| `radius-3xl` | `24px` | major cards and search bubble feel |
| `radius-pill` | `999px` | CTA pills |
| `radius-circle` | `50%` | arrow/pause/search/language/theme icons |

Most frequent observed radii: `12px` (33), `16px` (22), `24px` (20), `20px` (20), `8px` (15), `6px` (12), `50%` (12).

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| `card-float-lg` | `4px 12px 40px 6px rgba(0,0,0,.09)` | primary floating content cards |
| `card-float-md` | `4px 12px 30px 6px rgba(0,0,0,.09)` | smaller raised cards |
| `media-heavy` | `14px 14px 40px rgba(0,0,0,.2)` | heavier media/object shadow |
| `utility-soft` | `0 2px 10px rgba(0,0,0,.1)` | utility overlay |
| `button-lite` | `0 4px 8px 0 rgba(0,0,0,.15)` | small elevated control |

Kakao's shadow system is not global elevation chrome. It appears on cards and specific modules; the hero stage itself remains flat and photographic.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `fade-standard` | `opacity .4s ease` | standard fade |
| `fade-fast` | `opacity .3s ease` | quicker UI reveal |
| `menu-top` | `top .2s ease-in-out` | navigation/menu positioning |
| `transform-snap` | `transform .3s cubic-bezier(.54,.01,.47,1)` | slide/transform motion |
| `layout-flex` | `flex-basis .35s ease, flex-grow .35s ease, opacity .25s ease, transform .35s ease` | responsive/interactive panels |
| `slow-reveal` | `all .75s ease-in` | larger content reveal |

Motion is present but not the main identity. The visible homepage hero relies more on staged composition and static people cutouts than on a kinetic canvas.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: `1112px` observed as a wide information wrapper variable.
- **Grid type**: responsive editorial modules with explicit wrapper widths.
- **Column count**: variable by section; list gap tokens imply multi-card grids below the hero.
- **Gutter**: `16px`, `28px`, `34px` via `--list-column-gap`.

### Hero

- **Pattern Summary**: full-width gray people-stage + centered white H1 + pill CTA + speech-bubble search.
- **Layout**: white header above, hero stage below; people distributed across the viewport, headline centered.
- **Background**: gray photographic field with dimmed overlay and human cutouts.
- **Background Treatment**: image-overlay / muted gray stage; not a gradient mesh.
- **H1**: approximately `60px`, weight `700`, tight negative tracking.
- **CTA**: yellow KakaoTalk pill plus secondary dark/outlined pill.
- **Search**: dark rounded speech bubble, white stroke, search icon left, close button right, small tail on lower-right.
- **Controls**: circular arrows left/right and pause control; light translucent fills.

### Section Rhythm

```css
section {
  max-width: var(--wrap-info-width);
  column-gap: var(--list-column-gap);
}
```

### Card Patterns

- **Card background**: `#FFFFFF` or `#F9F9F9`.
- **Card border**: usually light neutral (`#E5E5E5`) or absent.
- **Card radius**: `20px` to `24px` for major modules.
- **Card padding**: section-specific; large enough to read as friendly consumer cards.
- **Card shadow**: `4px 12px 40px 6px rgba(0,0,0,.09)` on raised modules.

### Navigation Structure

- **Type**: horizontal global corporate navigation.
- **Position**: top header, white surface.
- **Height**: visually `73px` desktop; responsive variable includes `60px` and `47px`.
- **Background**: `#FFFFFF`.
- **Border**: no heavy divider in the screenshot; separation comes from the hero stage boundary.
- **Utilities**: search, language/globe, theme toggle icons.

### Content Width

- **Title max-width**: `405px`, `570px`, `808px` depending on breakpoint.
- **Container max-width**: `618px`, `869px`, `1112px` depending on breakpoint.
- **Sidebar width**: not observed on homepage hero.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Large desktop guard | `1902px` | extra-wide composition adjustments |
| Desktop | `1439px` | large-to-standard desktop switch |
| Tablet | `1023px` | navigation and wrapper compression |
| Mobile | `767px` | mobile layout switch |
| Small mobile | `411px` | narrow-device correction |

### Touch Targets

- **Minimum tap size**: icons are circular; target should stay at least `44px`.
- **Button height (mobile)**: infer `44px+` from pill/circle control language.
- **Input height (mobile)**: hero search is much taller on desktop; mobile should remain a large tap target, not collapse to a thin input.

### Collapsing Strategy

- **Navigation**: desktop horizontal menu collapses to menu controls; HTML includes "메인 메뉴 열기/닫기".
- **Grid columns**: card/list gaps step down from `34px` to `28px` to `16px`.
- **Hero layout**: people-stage must crop/reflow; headline and search remain the interaction focus.
- **Utilities**: search/language/theme remain icon-based.

### Image Behavior

- **Strategy**: art-directed hero people cutouts; preserve visible human silhouettes.
- **Max-width**: viewport-driven.
- **Aspect ratio handling**: crop rather than stretch; people must not distort.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**KakaoTalk Download Pill**

| Property | Value |
|---|---|
| Background | `#FFCD00` / Kakao yellow family |
| Text | `#000000` |
| Border | `2px solid #000000` |
| Radius | `999px` |
| Typography | KakaoSmall, bold, compact |
| Icon | circular download icon at left |

```html
<a class="button-kakao-download" href="#">
  <span class="icon-download"></span>
  카카오톡 다운로드
</a>
```

**Glass Detail Pill**

| Property | Value |
|---|---|
| Background | translucent white over hero gray |
| Text | `#FFFFFF` |
| Radius | `999px` |
| Padding | generous horizontal pill |

### Badges

The hero includes a small dark pill reading like a hash tag (`#Kannana`). This badge uses dark fill, white text, rounded pill shape, and high contrast against the gray stage.

### Cards & Containers

Cards use soft radii (`20px` / `24px`) and optional shadows. The most repeated heavy card shadow is `4px 12px 40px 6px rgba(0,0,0,.09)`. Avoid hard 1px bordered SaaS cards as the default; Kakao cards should feel more consumer-friendly and rounded.

### Navigation

Navigation is compact and black-on-white. Menu labels are short Korean categories: 소개, 기술과 서비스, 약속과 책임, 소식, 투자정보. Utility actions are icons, not text buttons.

### Inputs & Forms

The homepage search is not a standard input. It is a conversational speech bubble:

| Property | Value |
|---|---|
| Background | dark neutral near `#2F2F2F` / black |
| Text | `#FFFFFF` |
| Border | thick `#FFFFFF` outline |
| Radius | about `24px` |
| Shape detail | small bubble tail at lower-right |
| Iconography | search icon left, close circle right |

### Hero Section

The hero is the main component. It combines gray field, people imagery, white display headline, translucent controls, CTA pills, and the search bubble. The composition should feel like a messenger product campaign embedded inside a corporate site.

### 13-2. Named Variants

**button-kakao-download** — yellow service CTA.

| State | Spec |
|---|---|
| default | `#FFCD00` fill, `#000000` border/text, pill radius |
| hover | keep yellow identity; use subtle brightness or underline, not dramatic transform |
| focus | visible black or white focus ring depending on background |

**button-glass-utility** — translucent hero utility button.

| State | Spec |
|---|---|
| default | translucent light fill over gray image, white text |
| hover | raise opacity slightly |
| disabled | reduce opacity without changing shape |

**search-speech-bubble** — oversized conversational search control.

| State | Spec |
|---|---|
| default | dark fill, white border, rounded bubble with tail |
| focus | maintain white stroke; add inner or outer focus treatment without losing bubble silhouette |
| active | keep height and radius stable; do not collapse to a plain input |

**card-soft-surface** — rounded content module.

| State | Spec |
|---|---|
| default | `#FFFFFF` or `#F9F9F9`, radius `20px-24px` |
| hover | optional `rgba(0,0,0,.09)` shadow, no aggressive color wash |

### 13-3. Signature Micro-Specs

```yaml
messenger-search-bubble:
  description: "Corporate search reinterpreted as a KakaoTalk-like chat object."
  technique: "height 64px; background #2F2F2F; border 3px solid #FFFFFF; border-radius 24px; lower-right speech tail; search icon left and close control right."
  applied_to: ["{component.search-speech-bubble}", "{component.hero-section}"]
  visual_signature: "A utility control reads as an oversized chat message instead of a rectangular site search field."

gray-people-stage-hero:
  description: "Hero communicates Kakao's public reach through human cutouts rather than app screenshots."
  technique: "muted gray stage near #8E8E8E; dim image overlay; full-body people distributed across the viewport; white display headline layered over the scene."
  applied_to: ["{component.hero-section}", "{component.button-glass-utility}"]
  visual_signature: "The page feels like a public plaza or service campaign, with people carrying the product story."

kakao-tight-hangul-display:
  description: "KakaoBig display text is optically compressed until Korean headlines feel product-native."
  technique: "font-family KakaoBig; font-weight 700; letter-spacing values around -.5px, -.6px, -1px, and hero -2px; line-height near 1.18 for hero scale."
  applied_to: ["{component.hero-section}", "{component.card-soft-surface}"]
  visual_signature: "Large Hangul has poster-like pressure rather than loose system-font spacing."

yellow-black-download-pill:
  description: "Brand yellow is concentrated into one service action instead of becoming the page background."
  technique: "background #FFCD00; color #000000; border 2px solid #000000; border-radius 999px; padding 7px 13px; compact icon-and-label layout."
  applied_to: ["{component.button-kakao-download}"]
  visual_signature: "A small yellow-black capsule becomes the brand flare while the surrounding page stays white and gray."

soft-consumer-card-lift:
  description: "Corporate content cards borrow consumer-app softness without becoming glossy."
  technique: "background #FFFFFF or #F9F9F9; border-radius 20px-24px; optional box-shadow 4px 12px 40px 6px rgba(0,0,0,.09)."
  applied_to: ["{component.card-soft-surface}"]
  visual_signature: "Information modules float gently, keeping Kakao friendly rather than hard SaaS-like."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | short declarative Korean, product/social benefit first | "AI로 새로워지는 카카오톡" |
| Subheading | one-line clarification under the headline | "쓰는이에 집중. 쓰기좋게 맞춤." |
| Primary CTA | plain utility wording | "자세히 보기", "카카오톡 다운로드" |
| Navigation | institutional category nouns | "소개", "기술과 서비스", "약속과 책임" |
| Tone | friendly public utility, not luxury, not developer-first SaaS | "그 어떤 목소리도 소외되지 않도록" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Kakao Corp — copy into your root stylesheet */
:root {
  /* Fonts */
  --kakao-font-display: "KakaoBig", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
  --kakao-font-body: "KakaoSmall", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
  --kakao-font-digit: "KakaoDigitLatin", "Apple SD Gothic Neo", "Malgun Gothic", sans-serif;
  --kakao-font-weight-normal: 400;
  --kakao-font-weight-bold: 700;

  /* Brand */
  --kakao-color-brand-25: #FFF5B3;
  --kakao-color-brand-300: #FFE500;
  --kakao-color-brand-500: #FEE500;
  --kakao-color-brand-600: #FFCD00;
  --kakao-color-brand-900: #000000;

  /* Surfaces */
  --kakao-bg-page: #FFFFFF;
  --kakao-bg-soft: #F9F9F9;
  --kakao-bg-hero: #8E8E8E;
  --kakao-text: #333333;
  --kakao-text-strong: #000000;
  --kakao-text-muted: #666666;
  --kakao-border: #E5E5E5;

  /* Key spacing */
  --kakao-nav-height: 73px;
  --kakao-nav-height-small: 60px;
  --kakao-wrap-title-sm: 405px;
  --kakao-wrap-title-lg: 808px;
  --kakao-wrap-info-lg: 1112px;
  --kakao-grid-gap-sm: 16px;
  --kakao-grid-gap-md: 28px;
  --kakao-grid-gap-lg: 34px;

  /* Radius */
  --kakao-radius-sm: 8px;
  --kakao-radius-md: 12px;
  --kakao-radius-lg: 24px;
  --kakao-radius-pill: 999px;

  /* Shadow */
  --kakao-shadow-card: 4px 12px 40px 6px rgba(0,0,0,.09);
}

body {
  margin: 0;
  background: var(--kakao-bg-page);
  color: var(--kakao-text);
  font-family: var(--kakao-font-body);
  font-weight: var(--kakao-font-weight-normal);
  line-height: 1.5;
}

.kakao-display {
  font-family: var(--kakao-font-display);
  font-weight: var(--kakao-font-weight-bold);
  letter-spacing: -0.02em;
}

.kakao-download-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  border: 2px solid var(--kakao-text-strong);
  border-radius: var(--kakao-radius-pill);
  background: var(--kakao-color-brand-600);
  color: var(--kakao-text-strong);
  font-weight: 700;
  padding: 7px 13px;
}

.kakao-search-bubble {
  min-height: 64px;
  border: 3px solid #FFFFFF;
  border-radius: 24px;
  background: #2F2F2F;
  color: #FFFFFF;
  box-sizing: border-box;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Kakao Corp inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        kakao: {
          yellow: '#FFCD00',
          talk: '#FEE500',
          white: '#FFFFFF',
          ink: '#333333',
          black: '#000000',
          muted: '#666666',
          line: '#E5E5E5',
          soft: '#F9F9F9',
          hero: '#8E8E8E',
        },
      },
      fontFamily: {
        kakaoDisplay: ['KakaoBig', 'Apple SD Gothic Neo', 'Malgun Gothic', 'sans-serif'],
        kakaoBody: ['KakaoSmall', 'Apple SD Gothic Neo', 'Malgun Gothic', 'sans-serif'],
        kakaoDigit: ['KakaoDigitLatin', 'Apple SD Gothic Neo', 'Malgun Gothic', 'sans-serif'],
      },
      fontWeight: {
        kakaoNormal: '400',
        kakaoBold: '700',
      },
      borderRadius: {
        kakao: '24px',
        kakaoPill: '999px',
      },
      boxShadow: {
        kakaoCard: '4px 12px 40px 6px rgba(0,0,0,.09)',
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
| Brand primary | `{colors.brand-yellow}` | `#FFCD00` |
| KakaoTalk yellow | `{colors.kakao-yellow}` | `#FEE500` |
| Background | `{colors.surface-white}` | `#FFFFFF` |
| Text primary | `{colors.ink-primary}` | `#333333` |
| Text strong | `{colors.ink-black}` | `#000000` |
| Text muted | `{colors.ink-muted}` | `#666666` |
| Border | `{colors.line-light}` | `#E5E5E5` |
| Soft surface | `{colors.surface-soft}` | `#F9F9F9` |

### Example Component Prompts

#### Hero Section

```text
Kakao Corp 스타일 히어로 섹션을 만들어줘.
- 배경: muted gray stage around #8E8E8E with photographic people cutouts.
- H1: KakaoBig, about 60px desktop, weight 700, white #FFFFFF, tight tracking around -0.02em.
- 서브텍스트: white #FFFFFF, 16-18px, centered.
- CTA: yellow #FFCD00 pill with black #000000 text/border.
- Search: oversized dark #2F2F2F speech-bubble input with thick #FFFFFF outline and bubble tail.
- Header: white #FFFFFF bar, black logo/icons, compact Korean nav.
```

#### Card Component

```text
Kakao Corp 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF or #F9F9F9.
- radius: 20px-24px.
- shadow: 4px 12px 40px 6px rgba(0,0,0,.09) only when the card needs lift.
- 제목: KakaoBig, 26px, weight 700, letter-spacing -0.6px.
- 본문: KakaoSmall, 16px, color #333333, line-height 24px.
```

#### Navigation

```text
Kakao Corp 스타일 상단 네비게이션을 만들어줘.
- 높이: 73px desktop, white #FFFFFF background.
- 로고: left, black #000000 wordmark.
- 링크: Korean category labels, 14px, weight 700, black.
- 우측: search, globe/language, dark-mode icons as circular icon buttons.
- Avoid large colored nav CTAs; yellow belongs to service action buttons.
```

### Iteration Guide

- **색상 변경 시**: Yellow must stay accent-only. Do not flood the page with `#FFCD00`.
- **폰트 변경 시**: Replace KakaoBig/KakaoSmall with Korean-first fonts and preserve negative tracking.
- **여백 조정 시**: Keep the contrast between sparse header/hero and denser card modules.
- **새 컴포넌트 추가 시**: Prefer pills, circles, and 20-24px cards over sharp SaaS rectangles.
- **모션 추가 시**: Use opacity/transform easing around `.3s-.4s`; avoid bouncy playful animation unless it is a Kakao product illustration.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `KakaoBig` for display and `KakaoSmall` for interface/body.
- Keep main surfaces white or neutral: `#FFFFFF`, `#F9F9F9`, `#333333`, `#000000`.
- Use `#FFCD00` and `#FEE500` as action/service yellow, not as a full background system.
- Make primary action buttons pill-shaped with strong black contrast.
- Preserve tight Hangul tracking on large text.
- Use rounded search/input objects when the control should feel Kakao-like.
- Use card shadows sparingly, mainly for content modules.
- Keep corporate navigation quiet, white, and icon-driven.

### ❌ DON'T

- 배경 전체를 `#FFCD00` 또는 `#FEE500`으로 두지 말 것 — 대신 기본 표면은 `#FFFFFF`, hero stage는 muted gray 계열 사용.
- 본문 텍스트를 `#000000`으로만 두지 말 것 — 대신 기본 본문은 `#333333` 사용.
- muted text를 `#999999`로 약하게 밀지 말 것 — 대신 관측된 `#666666` 중심으로 사용.
- hero headline을 `#333333`으로 두지 말 것 — screenshot hero에서는 `#FFFFFF` 사용.
- card border를 `#CCCCCC` 같은 차가운 기본선으로 두지 말 것 — 대신 `#E5E5E5` 또는 borderless surface 사용.
- CTA 노란색을 `#FFC400` 같은 임의 yellow로 바꾸지 말 것 — 대신 `#FFCD00` 또는 `#FEE500` 계열 사용.
- body에 `font-weight: 500`을 기본으로 쓰지 말 것 — 관측 기본은 `400`, 강조는 `700`.
- display letter-spacing을 `0`으로 두지 말 것 — KakaoBig headline은 negative tracking 필요.
- 검색창을 평범한 `#FFFFFF` rectangular input으로 만들지 말 것 — hero search는 dark speech bubble 구조.
- 모든 카드에 강한 shadow를 넣지 말 것 — shadow는 `4px 12px 40px 6px rgba(0,0,0,.09)` 같은 부드러운 모듈 lift에 한정.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Full yellow brand field: absent. Yellow is a controlled action accent, not the homepage canvas.
- Gradient hero background: absent. The hero uses photographic gray staging, not purple/blue AI gradients.
- Generic Inter-only typography: absent. Kakao-specific Korean font families define the voice.
- Weight 500/600 hierarchy: effectively absent in the observed CSS; `400`, `700`, and occasional `800` do the work.
- Sharp enterprise rectangles: absent from hero-level identity; pills, circles, and rounded cards dominate.
- Heavy border-first SaaS card system: absent. Cards rely more on radius, surface, and soft shadow.
- Dense developer-dashboard layout: absent. Even corporate information is staged with editorial modules.
- Multi-brand rainbow UI: absent. Chromatic colors exist but do not define the interface hierarchy.
- Product mockup wall: absent in the hero. People using phones replace device-frame screenshots.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single-page scope** — This analysis reuses the available homepage HTML/CSS/screenshot artifacts. Subpages such as AI, ESG, news, investor relations, and service detail pages were not newly crawled.
- **Dark-mode mapping incomplete** — The header exposes a dark-mode control in text/HTML, but the reused artifacts did not provide enough evidence for a complete dark palette table.
- **Semantic token scarcity** — `phase1/alias_layer.json` reports zero semantic/core/component token tiers. Documentation aliases in this guide are therefore normalized names for application, not claimed source CSS variables.
- **Hero color measurement approximate** — The gray hero stage is taken from screenshot observation and CSS frequency context. Exact overlay alpha and image-processing values were not isolated.
- **Interactive states under-observed** — Hover, focus, active, loading, and disabled states are inferred from CSS patterns and component behavior, not exhaustively exercised in a browser interaction pass.
- **Motion runtime not fully traced** — CSS transition values were extracted, but JavaScript carousel timing, autoplay logic, and scroll-trigger behavior were not reverse-engineered.
- **Typography scale is frequency-derived** — The CSS contains many declarations and no clean exported scale object. The ladder above groups repeated sizes into practical design tokens.
- **Logo/service chromatic noise possible** — Some chromatic hex values may come from service icons, illustrations, or content assets rather than the interface design system.
- **Mobile visual verification skipped** — Breakpoints are CSS-derived; mobile screenshots were not inspected in this run.
