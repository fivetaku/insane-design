---
schema_version: 3.2
slug: theverge
service_name: The Verge
site_url: https://www.theverge.com
fetched_at: 2026-04-14T01:19:00+09:00
default_theme: dark
brand_color: "#3CFFD0"
primary_font: "PolySans"
font_weight_normal: 400
token_prefix: "k492gz"

bold_direction: "Neon Editorial"
aesthetic_category: "editorial-grid"
signature_element: "vertical_masthead"
code_complexity: high

medium: web
medium_confidence: high
archetype: editorial-magazine
archetype_confidence: high
design_system_level: lv3
design_system_level_evidence: "Next/font, custom editorial type stack, dense tokenized CSS variables, recurring feed/card modules, and a highly specific dark-news homepage composition are all present."

colors:
  surface-dark: "#131313"
  ink-light: "#FFFFFF"
  accent-mint: "#3CFFD0"
  accent-purple: "#5200FF"
  border-muted: "#E9E9E9"
  text-muted: "#949494"
  alert-red: "#EE0033"

typography:
  display: "Manuka"
  headline: "PolySans"
  body: "FK Roman Standard"
  mono: "PolySans Mono"
  ladder:
    - { token: display-vertical, size: "hero-scale", weight: 900, line_height: "compressed", tracking: "0" }
    - { token: headline-lg, size: "22px", weight: 700, line_height: "110%", tracking: "0" }
    - { token: headline-md, size: "18px", weight: 500, line_height: "110%", tracking: "0" }
    - { token: body-serif-lg, size: "18px", weight: 400, line_height: "160%", tracking: "-0.01em" }
    - { token: body-serif-md, size: "16px", weight: 400, line_height: "140%", tracking: "-0.01em" }
    - { token: label-mono, size: "14px", weight: 500, line_height: "120%", tracking: "0.02em" }
  weights_used: [300, 400, 500, 600, 700, 900]
  weights_absent: [200, 800]

components:
  masthead-vertical: { font: "Manuka", color: "{colors.ink-light}", orientation: "vertical", scale: "oversized" }
  nav-slash: { color: "{colors.ink-light}", separator: "/", border_bottom: "1px solid #FFFFFF" }
  feed-toggle-active: { bg: "{colors.accent-mint}", fg: "#000000", radius: "20px", padding: "tab-pill" }
  hero-card: { bg: "image-led", fg: "{colors.ink-light}", radius: "0", composition: "collage + editorial crop" }
  article-body-preview: { font: "FK Roman Standard", line_height: "160%", color: "{colors.ink-light}" }
---

# DESIGN.md — The Verge (Designer Guidebook)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

The Verge reads like a dark broadcast editorial — a newsroom that has replaced the fluorescent overhead lights with monitor glow and staged the masthead as a piece of set architecture rather than a polite nav mark. The base is almost black, `#131313` (`{colors.surface-dark}`), but the page refuses luxury silence because the interface keeps firing signal flares: mint `#3CFFD0` (`{colors.accent-mint}`), purple `#5200FF` (`{colors.accent-purple}`), white slash dividers, compressed display type, and illustration-led hero art.

The strongest visual move is the masthead. Instead of treating the logo as a small nav mark, the homepage turns The Verge into a piece of stage architecture: huge, vertical, white, clipped against the left edge like a magazine spine bolted to a live website. It is less a list of links and more like a broadsheet cover on deadline — a chronicle of technology culture formatted as a living front page.

The color system works like a dark broadcast console, not a brand palette spread evenly across the page. Mint is the powered-on switch, purple is the voltage under the line, and `#FFFFFF` (`{colors.ink-light}`) is the hard studio light. `#131313` (`{colors.surface-dark}`) matters because pure black would become an OLED hole; this black has the density of printed ink and the room tone of a late-night edit bay.

The editorial system is built on collision. PolySans carries nav, labels, headlines, and UI controls with compact confidence. FK Roman Standard carries article snippets like a column of magazine copy dropped into a tech console. Manuka appears as the compressed display weapon, more poster stamp than headline font. These roles are separated, not blended: sans for machinery, serif for reading texture, display type for impact.

Whitespace is tactical, not luxury. Large dark fields around the masthead and hero, narrow gutters inside feeds, hard horizontal rules, and tight text blocks. The page breathes at the composition level, then becomes dense at the story level — like a tabloid front page pinned to a black production wall. The rhythm is chaos contained: The Verge's editorial identity lives in the tension between the newsroom's live-broadcast energy and the broadsheet's vertical command.

### Key Characteristics

- Dark editorial shell anchored by `#131313`, not pure black as the main surface.
- Oversized vertical masthead creates a cover-like first impression.
- Mint `#3CFFD0` is the primary UI signal for active state, subscription, and editorial energy.
- Purple `#5200FF` appears as an underline/accent layer, not as a full-page wash.
- Slash-separated nav gives the header a zine/catalog rhythm.
- Serif body excerpts contrast against geometric sans headlines.
- Radius is selective: pills are round, story/image frames stay square.
- Borders and separators do more work than soft shadows.
- The visual tone is tech-culture tabloid, not neutral SaaS dashboard.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Neon Editorial
> **Aesthetic Category**: editorial-grid
> **Signature Element**: 이 사이트는 **oversized vertical masthead against a dark editorial grid**으로 기억된다.
> **Code Complexity**: high — custom font stack, dense hashed token variables, article feed variants, and image-heavy editorial layouts require careful reproduction.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 The Verge처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 역할 분리 */
:root {
  --font-display: "Manuka", Impact, Helvetica, sans-serif;
  --font-sans: "PolySans", Helvetica, Arial, sans-serif;
  --font-serif: "FK Roman Standard", Georgia, serif;
  --font-mono: "PolySans Mono", "Courier New", monospace;
}

/* 2. 어두운 편집 표면 + 흰 텍스트 */
body {
  background: #131313;
  color: #FFFFFF;
  font-family: var(--font-sans);
  font-weight: 400;
}

/* 3. 네온 민트 active signal */
:root { --verge-accent: #3CFFD0; }
.is-active,
.subscribe {
  background: var(--verge-accent);
  color: #000000;
  border-radius: 20px;
}
```

**절대 하지 말아야 할 것 하나**: The Verge를 흰 배경의 평범한 카드형 뉴스 사이트로 만들지 말 것. 첫 화면의 검은 편집실과 세로 masthead가 핵심이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.theverge.com` |
| Fetched | 2026-04-14T01:19:00+09:00 |
| Extractor | phase1 cache reuse: HTML + CSS + screenshot |
| HTML size | 954854 bytes |
| CSS files | 3 external + 1 inline, total 285450 chars |
| Token prefix | `k492gz` |
| Phase1 files | `brand_candidates.json`, `typography.json`, `resolved_tokens.json`, `alias_layer.json` |
| Method | Cached CSS token extraction plus manual screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js-style build output with `/_next/static/media/...` font assets.
- **Design system**: hashed CSS custom property namespace using prefix `--k492gz*`.
- **CSS architecture**:
  ```css
  --k492gz*        /* hashed core/component tokens */
  --font-*         /* Next/font exported families */
  @font-face       /* self-hosted editorial families with metric fallbacks */
  ```
- **Class naming**: generated module/hash class structure; design tokens are more reliable than class names.
- **Default theme**: dark homepage surface, `#131313`.
- **Font loading**: self-hosted `woff2` through Next/font with fallback metric overrides.
- **Canonical anchor**: homepage hero screenshot with vertical masthead, top nav, large story image, and right-side latest feed.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Manuka` via `__manuka_62afb5`, weight 900.
- **Sans headline/UI font**: `PolySans` via `__polySans_9afc27`, weights 300/400/500/700.
- **Serif body font**: `FK Roman Standard` via `__fkRomanStandard_cfceed`, weights 400/700, roman/italic.
- **Mono font**: `PolySans Mono` via `__polySansMono_0b836e`, weights 400/500/700.

```css
:root {
  --font-fkroman: "FK Roman Standard", Georgia, serif;
  --font-manuka: "Manuka", Impact, Helvetica, sans-serif;
  --font-polysans: "PolySans", Helvetica, Arial, sans-serif;
  --font-polysans-mono: "PolySans Mono", "Courier New", monospace;
}

body {
  font-family: var(--font-polysans);
  font-weight: 400;
}

.display-masthead {
  font-family: var(--font-manuka);
  font-weight: 900;
  line-height: .78;
}

.story-excerpt {
  font-family: var(--font-fkroman);
  font-weight: 400;
  line-height: 160%;
  letter-spacing: -0.01em;
}
```

### Note on Font Substitutes

Use substitutes by role, not by generic preference. `Impact` can approximate Manuka's compressed display function, but it will feel heavier and less editorial. `Helvetica` or `Arial` can stand in for PolySans only if spacing is tightened and labels remain compact. `Georgia` is the safest substitute for FK Roman Standard because the site needs visible serif contrast in excerpts; replacing it with another sans collapses the magazine rhythm. Do not replace PolySans Mono labels with a default system mono unless you also preserve uppercase, small size, and tight letter spacing.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

### Principles

1. **Separate editorial voices**: display, sans, serif, and mono each have a job.
2. **Compress the brand, not the body**: Manuka belongs to masthead/display moments, not article paragraphs.
3. **Use serif for reading texture**: FK Roman Standard gives excerpts and body previews a magazine feel.
4. **Keep labels mechanical**: mono or narrow sans labels should stay uppercase, compact, and high contrast.
5. **Use weight as hierarchy**: 500/700 carry headlines; 400 carries body; 900 is reserved for display impact.
6. **Preserve optical tracking**: serif body snippets use `-0.01em`; micro labels can use `0.02em`.

```css
.headline-lg {
  font: 700 22px/110% var(--font-polysans);
}

.headline-md {
  font: 500 18px/110% var(--font-polysans);
}

.body-serif-lg {
  font: 400 18px/160% var(--font-fkroman);
  letter-spacing: -0.01em;
}

.label-mono {
  font: 500 14px/120% var(--font-polysans-mono);
  letter-spacing: 0.02em;
  text-transform: uppercase;
}
```

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Core Palette

| Role | Hex | Use |
|---|---:|---|
| Surface dark | `#131313` | homepage shell, header field, editorial backdrop |
| Ink light | `#FFFFFF` | primary text, masthead, rules on dark |
| Accent mint | `#3CFFD0` | active tab, subscribe CTA, live UI signal |
| Accent purple | `#5200FF` | underline, highlight, secondary brand voltage |
| Border muted | `#E9E9E9` | light dividers and article separation |
| Text muted | `#949494` | metadata, secondary labels |
| Alert red | `#EE0033` | rare urgent/editorial accent |

### 06-2. Frequency Evidence

The phase1 color frequency is dominated by `#FFFFFF`, `#131313`, `#3CFFD0`, `#5200FF`, `#000000`, and `#E9E9E9`. The large counts for white and near-black are structural, not incidental. The chromatic identity comes from mint and purple, while red is a secondary editorial signal.

### 06-3. Brand Color

Use `#3CFFD0` as the operational brand color. It is not a pastel. It should feel electronic, almost over-bright, especially against `#131313`.

### 06-4. Neutral Temperature

The page is dark-neutral rather than blue-black. `#131313` keeps the site from feeling like a generic developer dashboard. Text often uses pure white on the homepage, but secondary blocks can move through `#E9E9E9`, `#BDBDBD`, `#949494`, and `#636363`.

### 06-5. Accent Rules

Mint is for active state and immediate action. Purple is for editorial underline or graphic punctuation. Do not distribute both evenly across every component; the tension works because mint is functional and purple is expressive.

### 06-6. Accessibility Notes

Mint `#3CFFD0` on black has high visibility. Mint on white should be avoided for body copy. White on `#131313` is strong enough for primary text, but serif excerpts need adequate size and line height to avoid glare.

### 06-7. Token Mapping

```css
:root {
  --verge-surface: #131313;
  --verge-ink: #FFFFFF;
  --verge-accent-mint: #3CFFD0;
  --verge-accent-purple: #5200FF;
  --verge-border: #E9E9E9;
  --verge-muted: #949494;
}
```

### 06-8. Color Stories

- **`#FFFFFF` on `#131313`** — the masthead, nav, and story copy use stark editorial contrast.
- **`#3CFFD0` as live signal** — active tabs and subscribe affordances feel powered-on.
- **`#5200FF` as graphic underline** — purple adds magazine electricity without replacing the dark shell.
- **`#E9E9E9` as rule language** — dividers and borders keep dense editorial modules organized.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

### Whitespace Philosophy

The Verge uses macro whitespace as drama and micro spacing as density. The top of the page leaves a large dark field before the content begins, then the story/feed area tightens into grids, slashes, rules, and compact metadata. This is not the airy spacing model of SaaS marketing; it is a cover layout with a live feed attached.

### Common Values

- `8px` / `10px` — micro gaps in labels, icons, and feed details.
- `14px` / `16px` — compact card and text grouping gaps.
- `20px` — dominant module padding and grid gap.
- `30px` / `40px` — section rhythm, image/text separation.
- `60px` — larger editorial section breaks.

```css
.page-shell {
  max-width: 1100px;
  margin: 0 auto;
  padding: 35px 18px 25px;
}

.story-grid {
  display: grid;
  grid-template-columns: 3fr 4fr 3fr;
  gap: 20px;
}

.feed-stack {
  display: grid;
  gap: 30px;
}
```

---

## 08. Radius & Shape
<!-- SOURCE: auto+manual -->

The shape system is intentionally split. Editorial objects stay sharp; controls become pills. This prevents the site from drifting into app-dashboard softness.

| Token | Value | Use |
|---|---:|---|
| `radius-none` | `0` | hero images, editorial frames, masthead area |
| `radius-tight` | `2px` / `4px` | tiny UI affordances |
| `radius-card` | `8px` / `10px` / `12px` | rare contained utility modules |
| `radius-pill` | `20px` / `24px` / `50%` | tabs, avatar circles, subscribe buttons |

```css
.article-card { border-radius: 0; }
.feed-toggle { border-radius: 20px; }
.avatar { border-radius: 50%; }
```

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

Shadows are secondary. The CSS contains shadows, but the visible homepage identity relies more on black fields, hard rules, image contrast, and color blocks. When shadows appear, they are utilitarian or image-depth shadows such as `0 4px 24px rgba(0,0,0,.25)`, not soft SaaS card elevation.

```css
.editorial-panel {
  box-shadow: none;
  border-top: 1px solid currentColor;
}

.media-overlay {
  box-shadow: 0 4px 24px rgba(0,0,0,.25);
}
```

---

## 10. Motion
<!-- SOURCE: manual -->

Motion should feel like interface state, not spectacle. Use quick color changes for active tabs, underline movement, menu reveal, and article hover states. Avoid large parallax, slow gradient morphs, or floating decorative animation. The news product needs to stay scannable.

```css
.feed-toggle,
.nav-link {
  transition: background-color 120ms ease, color 120ms ease, border-color 120ms ease;
}
```

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### 11-1. Cover Header

The first viewport is a cover composition: dark top field, centered nav, giant vertical logo at the left edge, large image-led hero, and a right-side latest feed. The masthead and story grid must be composed together; separating them into independent components weakens the identity.

### 11-2. Slash Navigation

Navigation items are separated by literal slash marks. This gives the header a print/zine rhythm and should be preserved over generic nav spacing.

```css
.nav {
  display: flex;
  align-items: center;
  gap: 16px;
  border-bottom: 1px solid #FFFFFF;
}

.nav-separator::before {
  content: "/";
  color: #FFFFFF;
}
```

### 11-3. Hero + Feed Split

The hero story uses a large visual block; the latest feed compresses author, timestamp, headline, and body preview. The split works because the left side is image-dominant and the right side is text-dense.

```css
.home-hero {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(280px, 1fr);
  gap: 40px;
}
```

### 11-4. Editorial Grid Variants

Observed CSS includes `repeat(3,1fr)`, `repeat(2,1fr)`, `3fr 4fr 3fr`, `340px auto auto`, and `auto 240px 240px`. The site changes grid templates by story type rather than forcing one card layout everywhere.

---

## 12. Responsive Behavior
<!-- SOURCE: manual -->

On narrower screens, preserve the identity by shrinking the masthead behavior before simplifying it away. The nav can collapse into a menu, feed can stack below the hero, and grid columns can become single-column, but the dark surface, mint active state, and logo scale must remain visible.

```css
@media (max-width: 768px) {
  .home-hero {
    grid-template-columns: 1fr;
    gap: 30px;
  }

  .display-masthead {
    writing-mode: horizontal-tb;
    font-size: clamp(56px, 18vw, 112px);
  }
}
```

---

## 13. Components
<!-- SOURCE: auto+manual -->

### 13-1. Component Inventory

- **Masthead vertical** — oversized white logo/type block, often clipped or edge-aligned.
- **Slash nav** — category links separated by `/`, with a thin horizontal rule.
- **Subscribe CTA** — mint pill with black text; compact and loud.
- **Account sign-in** — small icon/text pairing, white on dark.
- **Feed toggle** — segmented pill where active state is mint and inactive state is dark gray.
- **Hero story card** — large image/collage block with square edges.
- **Latest feed item** — avatar, author in mint, timestamp, headline, serif excerpt.
- **Section grid** — 2/3-column editorial modules with hard gutters and rules.

### 13-2. Named Variants

```yaml
masthead-vertical:
  font: Manuka
  color: "#FFFFFF"
  surface: "#131313"
  behavior: edge-clipped vertical cover mark

nav-slash:
  font: PolySans
  separator: "/"
  border-bottom: "1px solid #FFFFFF"
  gap: "16px"

feed-toggle-active:
  background: "#3CFFD0"
  color: "#000000"
  radius: "20px"
  typography: "500 14px/120% PolySans Mono"

latest-item:
  author: "#3CFFD0"
  headline: "700 15px/100% PolySans"
  excerpt: "400 18px/160% FK Roman Standard"
```

### 13-3. Signature Micro-Specs

#### edge-clipped-masthead

```yaml
edge-clipped-masthead:
  description: "The brand mark becomes page architecture, not a small header logo."
  technique: "font-family: Manuka; font-weight: 900; line-height: .78; color: #FFFFFF; oversized edge-aligned placement on #131313"
  applied_to: ["{components.masthead-vertical}"]
  visual_signature: "A white vertical magazine-spine masthead anchors the dark first viewport."
```

#### mint-live-toggle

```yaml
mint-live-toggle:
  description: "Active controls read like a powered-on editorial switch."
  technique: "background: #3CFFD0; color: #000000; border-radius: 20px; font: 500 14px/120% PolySans Mono; letter-spacing: 0.02em; text-transform: uppercase"
  applied_to: ["{components.feed-toggle-active}", "{components.subscribe-cta}"]
  visual_signature: "The mint pill cuts through the black shell as the only functional live signal."
```

#### slash-rule-header

```yaml
slash-rule-header:
  description: "Navigation uses print/zine punctuation instead of neutral menu spacing."
  technique: "display: flex; gap: 16px; separator content: '/'; border-bottom: 1px solid #FFFFFF; color: #FFFFFF"
  applied_to: ["{components.nav-slash}"]
  visual_signature: "White slash marks and a thin rule turn the header into an editorial index strip."
```

#### serif-excerpt-snap

```yaml
serif-excerpt-snap:
  description: "Article previews keep magazine reading texture inside the geometric UI frame."
  technique: "font-family: FK Roman Standard, Georgia, serif; font-weight: 400; font-size: 18px; line-height: 160%; letter-spacing: -0.01em; color: #FFFFFF"
  applied_to: ["{components.article-body-preview}", "{components.latest-item}"]
  visual_signature: "Dense sans headlines snap against softer serif excerpt columns."
```

#### square-image-shock

```yaml
square-image-shock:
  description: "Editorial imagery stays hard-cropped and poster-like instead of becoming soft cards."
  technique: "border-radius: 0; display: block; width: 100%; image-led composition; hierarchy carried by crop/contrast rather than card shadow"
  applied_to: ["{components.hero-card}", "{components.section-grid}"]
  visual_signature: "Hero media lands as a sharp magazine cutout against the dark grid."
```

### 13-4. Component CSS Starter

```css
.verge-toggle {
  display: inline-flex;
  background: #2D2D2D;
  border-radius: 24px;
  padding: 0;
}

.verge-toggle__item {
  padding: 12px 24px;
  border-radius: 20px;
  font: 500 14px/120% var(--font-polysans-mono);
  letter-spacing: 0.02em;
  text-transform: uppercase;
  color: #FFFFFF;
}

.verge-toggle__item[aria-selected="true"] {
  background: #3CFFD0;
  color: #000000;
}
```

---

## 14. Content Voice
<!-- SOURCE: manual -->

The voice is fast, literate, slightly irreverent, and technology-native. Headlines can be direct and witty, but UI copy remains compressed: "Latest", "Following", "Subscribe", "Sign in". Avoid enterprise polish. The tone should feel edited by people who care about culture and gadgets, not optimized by a growth landing page team.

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
:root {
  --verge-surface: #131313;
  --verge-ink: #FFFFFF;
  --verge-ink-inverse: #000000;
  --verge-muted: #949494;
  --verge-rule: #E9E9E9;
  --verge-accent-mint: #3CFFD0;
  --verge-accent-purple: #5200FF;
  --verge-alert: #EE0033;

  --font-display: "Manuka", Impact, Helvetica, sans-serif;
  --font-sans: "PolySans", Helvetica, Arial, sans-serif;
  --font-serif: "FK Roman Standard", Georgia, serif;
  --font-mono: "PolySans Mono", "Courier New", monospace;
}

body {
  margin: 0;
  background: var(--verge-surface);
  color: var(--verge-ink);
  font-family: var(--font-sans);
  font-weight: 400;
}

.verge-shell {
  max-width: 1100px;
  margin: 0 auto;
  padding: 35px 18px 50px;
}

.verge-nav {
  display: flex;
  align-items: center;
  gap: 16px;
  border-bottom: 1px solid var(--verge-ink);
  color: var(--verge-ink);
}

.verge-nav a {
  color: inherit;
  text-decoration: none;
  font: 400 18px/110% var(--font-sans);
}

.verge-nav .slash {
  color: var(--verge-ink);
}

.verge-masthead {
  font-family: var(--font-display);
  font-weight: 900;
  line-height: .78;
  color: var(--verge-ink);
}

.verge-home {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(280px, 1fr);
  gap: 40px;
}

.verge-hero img {
  display: block;
  width: 100%;
  border-radius: 0;
}

.verge-latest {
  border-left: 1px dashed rgba(255,255,255,.18);
  padding-left: 40px;
}

.verge-author {
  color: var(--verge-accent-mint);
  font: 700 12px/110% var(--font-sans);
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

.verge-headline {
  font: 700 15px/100% var(--font-sans);
  color: var(--verge-ink);
}

.verge-excerpt {
  font: 400 18px/160% var(--font-serif);
  letter-spacing: -0.01em;
  color: var(--verge-ink);
}

.verge-pill {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0 24px;
  border-radius: 20px;
  background: var(--verge-accent-mint);
  color: var(--verge-ink-inverse);
  font: 500 14px/120% var(--font-mono);
  letter-spacing: 0.02em;
  text-transform: uppercase;
}
```

---

## 16. Tailwind Mapping
<!-- SOURCE: manual -->

```js
export const vergeTheme = {
  colors: {
    surface: "#131313",
    ink: "#FFFFFF",
    inverse: "#000000",
    mint: "#3CFFD0",
    purple: "#5200FF",
    rule: "#E9E9E9",
    muted: "#949494",
    alert: "#EE0033",
  },
  fontFamily: {
    display: ["Manuka", "Impact", "Helvetica", "sans-serif"],
    sans: ["PolySans", "Helvetica", "Arial", "sans-serif"],
    serif: ["FK Roman Standard", "Georgia", "serif"],
    mono: ["PolySans Mono", "Courier New", "monospace"],
  },
  borderRadius: {
    none: "0",
    pill: "20px",
  },
};
```

---

## 17. Agent Prompt
<!-- SOURCE: manual -->

Build a The Verge-inspired editorial homepage. Use a dark `#131313` surface, pure white editorial text, mint `#3CFFD0` for active controls, and purple `#5200FF` only as a secondary graphic accent. The first viewport must feel like a magazine cover: large masthead presence, slash-separated nav, image-led hero story, and a compact latest feed. Use separate type roles: compressed display for masthead, geometric sans for nav/headlines, serif for excerpts, and mono for small labels. Keep images square-edged, controls pill-shaped, and separators sharp. Avoid SaaS cards, beige editorial calm, blue developer-dashboard styling, and generic newspaper whiteness.

---

## 18. DO / DON'T
<!-- SOURCE: auto+manual -->

### ✅ Do

- Use `#131313` as the dominant homepage surface.
- Use `#FFFFFF` for masthead, nav, and primary text on dark.
- Use `#3CFFD0` as the active/action color, especially for pills and live state.
- Keep `#5200FF` as a secondary graphic accent, not the full theme.
- Preserve the display/sans/serif/mono type separation.
- Use slash-separated navigation and thin rules for editorial structure.
- Keep hero images and article media square-edged.
- Let the masthead be oversized enough to act as composition, not decoration.

### 🚫 Don't

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 homepage shell은 `#131313` 사용.
- 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — dark homepage primary text는 `#FFFFFF` 사용.
- active tab을 `#5200FF`로 칠하지 말 것 — active UI는 `#3CFFD0` 사용.
- mint를 흐린 `#D8F0E8`로 약화하지 말 것 — 핵심 accent는 선명한 `#3CFFD0` 사용.
- 전체 배경을 순수 `#000000`으로 만들지 말 것 — The Verge surface는 더 부드러운 `#131313`가 기준.
- hero/card 이미지에 `20px` 이상의 둥근 모서리를 주지 말 것 — main editorial media는 `border-radius: 0` 사용.
- 모든 본문을 PolySans로 처리하지 말 것 — story excerpt는 FK Roman Standard/Georgia 계열 serif 사용.
- masthead를 24px nav logo처럼 축소하지 말 것 — large display object로 배치.
- feed와 hero를 같은 카드 컴포넌트로 만들지 말 것 — hero는 image-led, feed는 text-dense로 분리.
- soft SaaS shadow `0 20px 60px rgba(...)`에 의존하지 말 것 — separators, contrast, and image composition을 사용.

### 🚫 What This Site Doesn't Use

- Beige/cream editorial calm: `#F5F0E8` 계열 배경 정체성이 아니다.
- Blue SaaS trust palette: `#2563EB` 같은 dashboard primary가 아니다.
- Rounded card wall: story modules are not a grid of soft product cards.
- Gradient-orb decoration: visual energy comes from image collage and neon accent.
- Low-contrast gray text fields: homepage text is deliberately high contrast.
- All-sans article texture: serif excerpts are part of the voice.
- Luxury minimal whitespace: density and collision are intentional.
- App sidebar navigation: this is an editorial front page, not a dashboard.
- Heavy universal shadows: rules and color blocks carry hierarchy.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- Phase1 cache was reused from `insane-design/theverge/*`; Step 1-3 live fetch was not rerun because cached HTML/CSS/screenshots were present.
- The custom font public names are inferred from Next/font hashed families: `__polySans_9afc27`, `__fkRomanStandard_cfceed`, `__manuka_62afb5`, and `__polySansMono_0b836e`.
- The report focuses on the captured homepage first viewport. Article pages, video pages, shop modules, and logged-in states may introduce additional component variants.
- Hashed token names such as `--k492gz0` are real CSS variables but not semantic author-facing names; semantic token labels in this guide are adapter names for reuse.
- Motion guidance is conservative because phase1 evidence captures static CSS and screenshot context, not interaction recordings.
- Color frequency includes structural CSS and may include repeated component states; role assignment was checked against screenshot evidence to avoid logo/wall contamination.
