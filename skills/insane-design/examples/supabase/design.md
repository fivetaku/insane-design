---
schema_version: 3.2
slug: supabase
service_name: Supabase
site_url: https://supabase.com
fetched_at: 2026-04-20T19:57:00+09:00
default_theme: dark
brand_color: "#3ECF8E"
primary_font: custom-font
font_weight_normal: 400
token_prefix: supabase

bold_direction: Developer Dark
aesthetic_category: Refined SaaS
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Semantic Tailwind tokens are clearly in active use across marketing UI, but the public page does not expose a complete designer-facing spec."

colors:
  brand-default: "#3ECF8E"
  background-default: "#121212"
  foreground-default: "#FAFAFA"
  border-default: "#2E2E2E"
  background-surface-100: "#1F1F1F"
  background-surface-300: "#292929"
  foreground-muted: "#4D4D4D"
  brand-500: "#00623A"

typography:
  display: "custom-font"
  body: "custom-font"
  code: "Ubuntu, Droid Sans, Segoe WPC"
  ladder:
    - { token: h1-mobile, size: "36px", weight: 400, tracking: "0" }
    - { token: h1-small, size: "48px", weight: 400, tracking: "0" }
    - { token: h1-large, size: "72px", weight: 400, tracking: "0" }
    - { token: body-large, size: "18px", weight: 400, tracking: "0" }
    - { token: nav-small, size: "12px", weight: 400, tracking: "0" }
  weights_used: [200, 300, 400, 500, 600, 700, 800, 900]
  weights_absent: []

components:
  button-primary: { bg: "{colors.brand-500}", radius: "6px", padding: "8px 16px", height: "38px" }
  button-secondary: { bg: "{colors.background-surface-300}", radius: "6px", padding: "8px 16px", height: "38px" }
  announcement-pill: { bg: "{colors.background-surface-100}", radius: "9999px", border: "{colors.background-surface-300}" }
---

# DESIGN.md — Supabase

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Supabase is not trying to look like a generic cloud landing page. It behaves more like a developer console that has been pulled forward into marketing: dark canvas, terminal-adjacent restraint, crisp white copy, and one confident green. The hero says "Build in a weekend" in white, then lets "Scale to millions" carry the whole brand load in #3ECF8E (`{colors.brand-default}`). There is no second expressive color fighting for attention.

The page's strongest move is the contrast between emotional SaaS promise and utilitarian surface. It is a Postgres control room with the lights turned down: the brand does not arrive as a poster, it arrives as one green terminal prompt on an otherwise disciplined interface. Buttons are small, rectangular, and deliberately dashboard-like. The primary CTA uses the deeper green action tone from `--brand-500` rather than the bright display green; the bright green is reserved for emphasis, links, and brand recognition. That separation keeps the page from becoming neon.

The background is a near-black operating surface, not pure black. The visual floor sits around #121212 (`{colors.background-default}`), with surfaces stepping through #1F1F1F and #292929. Pure black would feel like a hole in an OLED panel; Supabase's #121212 feels more like a dark editor pane that still has air between rows. Borders and hover states are not decorative chrome; they are quiet separators that make the page feel like an app with production-grade controls.

The logo wall behaves like a monitoring feed seen through smoked glass. Customer marks are present, but the edge fade makes them recede into `{colors.background-default}` instead of becoming a trophy shelf. Even the announcement pill is not a banner; it is a tiny translucent command palette chip, with `bg-gradient-to-br` and `backdrop-blur-md` doing just enough to lift it off the console surface.

Supabase's craft is in these refusals: no second brand color, no oversized glossy SaaS button, no decorative hero illustration, no shadow system trying to imitate depth where borders can do the work. The page has almost no "site" self-consciousness. It gives the startup promise a single luminous line, then steps back like an interface that expects to be used.

It feels fast because it avoids theatrical motion. The navigation keeps compact 26px controls, hero CTAs stay at 38px, and the green line does what a progress cursor does in a terminal: it tells you where the action is. The identity is "developer confidence at startup speed."

이 페이지는 dark SaaS 마케팅이지만 실제로는 **dev 실험실의 측정 콘솔**이다. dark canvas는 실험실 책상 위 OLED 디스플레이, 한 줄의 녹색 카피는 측정값을 띄우는 single LED probe, announcement glass pill은 오실로스코프 옆에 끼워둔 작은 메모지다. blueprint를 그리지 않고도, semantic 토큰 사다리가 회로도처럼 정렬되고 logo wall은 모니터링 피드처럼 흐린다. 이 사이트의 시연(demo)은 화려한 무대가 아니라, 공구함에서 막 꺼낸 도구처럼 작고 직접적이다 — Postgres가 켜진 엔지니어링 다이어그램의 측면도이고, 실험실 노트의 첫 줄을 그대로 옮긴 페이지다.

### Key Characteristics

- Dark-first SaaS marketing surface, anchored by #121212 rather than pure #000000.
- Single green brand voice: #3ECF8E for display emphasis, deeper green action tones for CTAs.
- Centered hero with two-line H1; the second line is the chromatic memory hook.
- Compact app-like controls: 6px radius, 26px nav buttons, 38px hero buttons.
- Semantic Tailwind token layer: `--background-*`, `--foreground-*`, `--border-*`, `--brand-*`.
- Logo wall is intentionally muted and edge-faded so customer marks do not compete with the hero.
- Borders and focus rings are functional, not ornamental.
- Motion is mostly opacity/translation refinement, including the announcement chevron and marquee logos.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Developer Dark
> **Aesthetic Category**: Refined SaaS
> **Signature Element**: 이 사이트는 **dark console marketing hero with a single green scaling line**으로 기억된다.
> **Code Complexity**: high — Tailwind utilities, semantic HSL variables, gradient overlays, backdrop blur, marquee motion, and responsive variants are all present.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Supabase처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "custom-font", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
  letter-spacing: 0;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #121212;
  --fg: #FAFAFA;
  --muted: #4D4D4D;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root {
  --brand-display: #3ECF8E;
  --brand-action: #00623A;
}
```

**절대 하지 말아야 할 것 하나**: Supabase를 밝은 흰색 SaaS 페이지로 바꾸지 말 것. 이 사이트의 기본 질감은 dark developer console이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://supabase.com` |
| Fetched | 2026-04-20T19:57:00+09:00 |
| Extractor | reused phase1 artifacts from `insane-design/supabase/` |
| HTML size | 376,938 bytes |
| CSS files | 4 CSS files, about 895 KB total |
| Token prefix | `supabase` |
| Method | CSS custom properties, frequency candidates, screenshot observation, and HTML structure reuse |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js-style static/SSR HTML with Tailwind utility classes.
- **Design system**: Supabase semantic token layer — no single public DS name exposed in the captured page.
- **CSS architecture**:
  ```css
  core       (--colors-gray-dark-*, --colors-green*)    raw HSL ramps
  semantic   (--background-*, --foreground-*, --border-*) role tokens
  action     (--brand-*, --destructive-*, --warning-*)  interactive states
  utility    (.text-foreground, .bg-brand, .rounded-md) Tailwind generated API
  ```
- **Class naming**: Tailwind utility composition with state variants (`dark:`, `hover:`, `focus-visible:`, `data-[state=open]:`).
- **Default theme**: dark (`--background-default: 0deg 0% 7.1%`, approx #121212).
- **Font loading**: captured CSS exposes `custom-font` plus code/editor stacks; exact public font file mapping is not fully proven.
- **Canonical anchor**: centered hero with announcement pill, two-line H1, primary/secondary CTA pair, and muted customer logo wall.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `custom-font` (site-specific loaded font, exact family name not exposed by phase1)
- **Code font**: `Ubuntu, Droid Sans, -apple-system, BlinkMacSystemFont, Segoe WPC, Segoe UI, sans-serif`
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --supabase-font-family:       "custom-font", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --supabase-font-family-code:  Ubuntu, "Droid Sans", "Segoe WPC", "Segoe UI", sans-serif;
  --supabase-font-weight-normal: 400;
  --supabase-font-weight-bold:   600;
}
body {
  font-family: var(--supabase-font-family);
  font-weight: var(--supabase-font-weight-normal);
}
```

### Note on Font Substitutes

- **Display substitute** — use **Inter** at weight 400 for hero/body and 500-600 only for emphasis. Keep `letter-spacing: 0`; adding negative tracking makes Supabase feel more like Apple/Vercel than its captured page.
- **Code/editor substitute** — use **Ubuntu** or **Droid Sans** for embedded editor/browser chrome if matching the captured CSS. Do not force a monospaced-only product UI unless the component is explicitly code-like.
- **Line-height correction** — keep the hero line-height tight only at large breakpoints (`sm:leading-none` appears on the H1). Body copy should stay around 1.55-1.65 for the dense product feature copy.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Hero H1 mobile | 36px (`text-4xl`) | 400 | normal | 0 |
| Hero H1 small | 48px (`sm:text-5xl`) | 400 | 1.0 at `sm` | 0 |
| Hero H1 large | 72px (`lg:text-7xl`) | 400 | tight | 0 |
| Hero body mobile | 14px | 400 | relaxed | 0 |
| Hero body desktop | 18px (`lg:text-lg`) | 400 | relaxed | 0 |
| Nav label | 12px | 400 | compact | 0 |
| CTA medium | 14px desktop / 16px base | 400 | 38px button height | 0 |

> ⚠️ The important Supabase move is not heavy type. The hero is large but stays regular-weight; the green line, not boldness, creates the emphasis.

### Principles

1. Display type is large and regular. Do not compensate with `font-weight: 700`.
2. Letter spacing remains `0`; tightness comes from line-height and short copy, not optical compression.
3. The hero is a two-line semantic split: neutral promise first, green scale promise second.
4. Body copy is centered and readable, but never oversized. It supports the H1 rather than competing with it.
5. UI labels are compact. Navigation and small CTAs use 12px/26px proportions, closer to dashboard chrome than brochure navigation.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (7 steps)
<!-- `--brand-*` -->

| Token | HSL | Approx Hex |
|---|---|---|
| `--brand-link` | `155deg 100% 38.6%` | #00C576 |
| `--brand-default` | `153.1deg 60.2% 52.7%` | #3ECF8E |
| `--brand-600` | `154.9deg 59.5% 70%` | #8DEFC1 |
| `--brand-500` | `154.9deg 100% 19.2%` | #00623A |
| `--brand-400` | `155.5deg 100% 9.6%` | #00311D |
| `--brand-300` | `155.1deg 100% 8%` | #002817 |
| `--brand-200` | `162deg 100% 2%` | #000A07 |

### 06-2. Brand Dark Variant

| Token | Value | Usage |
|---|---|---|
| `dark:bg-brand-500` | approx #00623A | Primary CTA background on dark surfaces |
| `dark:hover:bg-brand/50` | #3ECF8E at 50% mix | Hover softening without neon fill |
| `dark:border-brand/30` | #3ECF8E at 30% | CTA border tint |

### 06-3. Neutral Ramp

| Step | Dark token | Approx Hex |
|---|---|---|
| 100 | `--colors-gray-dark-100` | #161616 |
| 200 | `--colors-gray-dark-200` | #1C1C1C |
| 300 | `--colors-gray-dark-300` | #232323 |
| 400 | `--colors-gray-dark-400` | #282828 |
| 500 | `--colors-gray-dark-500` | #2E2E2E |
| 700 | `--colors-gray-dark-700` | #3E3E3E |
| 1200 | `--colors-gray-dark-1200` | #EDEDED |

### 06-4. Accent Families

| Family | Key step | Hex/HSL |
|---|---|---|
| Green | `--colors-green9` | `hsl(151,55%,41.5%)` |
| Destructive | `--destructive-default` | `10.2deg 77.9% 53.9%` |
| Warning | `--warning-default` | `38.9deg 100% 42.9%` |
| Blue utility | frequency candidate | #0070F3 |

### 06-5. Semantic

| Token | Value | Usage |
|---|---|---|
| `--background-default` | `0deg 0% 7.1%` | Page floor |
| `--background-surface-100` | `0deg 0% 12.2%` | Low surface panels |
| `--background-surface-300` | `0deg 0% 16.1%` | Announcement overlay, elevated surface |
| `--foreground-default` | `0deg 0% 98%` | Primary text |
| `--foreground-muted` | `0deg 0% 30.2%` | Muted logos and secondary text |
| `--border-default` | `0deg 0% 18%` | Default hairline |
| `--border-stronger` | `0deg 0% 27.1%` | Hover/active border |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `.bg-brand` | `hsl(var(--brand-default))` | Bright brand fills |
| `.text-brand` | `hsl(var(--brand-default))` | Hero green line |
| `.text-foreground` | `hsl(var(--foreground-default))` | Main copy |
| `.border-default` | `hsl(var(--border-default))` | Card and chrome separators |
| `.bg-alternative` | background alternative token | Secondary button / muted controls |

### 06-7. Dominant Colors (actual CSS frequency)

| Token | Hex | Frequency clue |
|---|---|---|
| Transparent | #0000 | most frequent utility artifact |
| White | #FFFFFF / #fff | text and SVG utilities |
| Surface black | #030A0C | dark chromatic base candidate |
| Neutral surface | #1C1C1C | repeated dark surface |
| Brand green | #3ECF8E | primary chromatic candidate |
| Pale green | #DFFFF1 | green-tinted highlight surface |

### 06-8. Color Stories

**`{colors.brand-default}` (#3ECF8E)** — the public memory color. It appears as the hero second line and interactive green identity, but the CTA fill often uses deeper green so the page does not turn into a glowing neon poster.

**`{colors.background-default}` (#121212)** — developer-console floor. It is dark enough to feel like an app shell but not pure black; this allows #FAFAFA text and green accents to sit without harsh OLED contrast.

**`{colors.foreground-default}` (#FAFAFA)** — high-confidence text color. Supabase uses it for primary copy and keeps secondary hierarchy through size, opacity, and surface contrast rather than introducing many text colors.

**`{colors.border-default}` (#2E2E2E)** — quiet structure. Borders are present but restrained; they make the UI feel operational and trustworthy without making every card look boxed-in.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token / Utility | Value | Use case |
|---|---|---|
| `px-6` | 24px | Base container horizontal padding |
| `lg:px-16` | 64px | Desktop container padding |
| `xl:px-20` | 80px | Wide desktop container padding |
| `py-16` | 64px | Base hero vertical rhythm |
| `md:py-24` / `lg:py-24` | 96px | Desktop section rhythm |
| `gap-4` | 16px | Hero internal stack |
| `lg:gap-8` | 32px | Desktop hero rhythm |
| `px-4 py-2` | 16px / 8px | Medium CTA padding |
| `px-2.5 py-1` | 10px / 4px | Tiny nav CTA padding |

**주요 alias**:
- `container` → `width: 100%`, then responsive max-width via Tailwind container rules.
- `max-w-2xl` → hero text containment.
- `max-w-4xl` → logo wall containment.

### Whitespace Philosophy

Supabase gives the hero enough vertical air to feel calm, but it does not use luxury-scale emptiness. The captured hero starts after a compact fixed-height nav, then stacks announcement, H1, paragraph, and CTA pair inside a narrow center column. The result is "fast to understand" rather than "gallery-like."

Below the hero, spacing tightens quickly into product modules and logo strips. The system is intentionally app-adjacent: 24/64/80px container gutters create page architecture, while 8/16/32px gaps keep components efficient.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token / Utility | Value | Context |
|---|---|---|
| `--borderradius-xs` | 2px | Fine UI parts |
| `--borderradius-sm` | 4px | Small controls |
| `.rounded-md` | 6px (`.375rem`) | Primary and secondary buttons |
| `.rounded-lg` | 8px (`.5rem`) | Panels/cards |
| `--borderradius-xl` | 16px | Larger surfaces |
| `.rounded-full` | 9999px | Announcement pill and focus shape |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: hero copy sits around `max-w-2xl`; logo wall around `max-w-4xl`.
- **Grid type**: Tailwind flex/grid utilities. Hero is flex-column centered; downstream product sections use grid/flex combinations.
- **Column count**: hero is one-column centered; product content later branches into cards/modules.
- **Gutter**: 24px base, 64px large, 80px extra-large container padding.

### Hero

- **Pattern Summary**: dark 1-column centered hero + announcement pill + two-line H1 + compact dual CTA + faded logo wall.
- Layout: centered stack inside `container relative mx-auto px-6 py-16 md:py-24 lg:px-16`.
- Background: solid dark page surface, no full-bleed image.
- **Background Treatment**: solid #121212 page with local gradient/backdrop-blur only inside the announcement pill and logo fade masks.
- H1: `text-4xl` / `sm:text-5xl` / `lg:text-7xl`, weight 400, tracking 0.
- Max-width: `max-w-2xl` hero text area.

### Section Rhythm

```css
section-like-block {
  padding: 64px 24px;
}
@media (min-width: 768px) {
  section-like-block { padding-top: 96px; padding-bottom: 96px; }
}
@media (min-width: 1024px) {
  section-like-block { padding-left: 64px; padding-right: 64px; }
}
```

### Card Patterns

- **Card background**: semantic dark surfaces (`--background-surface-100/200/300`).
- **Card border**: `1px solid hsl(var(--border-default))`, stronger on hover.
- **Card radius**: usually 8px for panels, 6px for control-like surfaces.
- **Card padding**: utility-driven, commonly 16-24px.
- **Card shadow**: sparse. A multi-layer shadow exists in CSS, but the homepage hero chrome relies more on border/surface contrast.

### Navigation Structure

- **Type**: horizontal desktop nav with collapsible mobile menu.
- **Position**: top page chrome; captured hero offsets content by about 65px.
- **Height**: nav visual height around 64-65px; tiny nav buttons are 26px tall.
- **Background**: same dark floor, giving nav an app shell feeling.
- **Border**: subtle dark border/separator.

### Content Width

- **Prose max-width**: around `max-w-2xl` for hero copy.
- **Container max-width**: Tailwind container with responsive padding; exact max-width not fully exposed by phase1 summary.
- **Sidebar width**: not applicable on the marketing homepage hero.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary CTA**

```html
<a class="inline-flex h-[38px] items-center rounded-md border bg-brand-400 dark:bg-brand-500 px-4 py-2 text-foreground hover:bg-brand/80 dark:hover:bg-brand/50">
  Start your project
</a>
```

| Spec | Value |
|---|---|
| Height | 38px |
| Radius | 6px |
| Padding | 16px horizontal / 8px vertical |
| Background | `dark:bg-brand-500` approx #00623A |
| Border | `border-brand-500/75`, `dark:border-brand/30` |
| Hover | brand tint softens to 50-80% |
| Focus | `focus-visible:outline-brand-600` |

**Secondary CTA**

```html
<a class="inline-flex h-[38px] items-center rounded-md border bg-alternative dark:bg-muted px-4 py-2 text-foreground hover:bg-selection hover:border-stronger">
  Request a demo
</a>
```

| Spec | Value |
|---|---|
| Height | 38px |
| Background | muted dark surface |
| Border | `border-strong`, hover to `border-stronger` |
| Color | foreground text |
| Motion | `transition-all`, `ease-out`, `duration-200` |

### Badges

**Announcement pill**

```html
<a class="rounded-full border border-background-surface-300 shadow-md overflow-hidden">
  <span>State of Startups 2026: Take the survey.</span>
  <span class="announcement-overlay bg-gradient-to-br from-background-surface-100 to-background-surface-300 backdrop-blur-md"></span>
</a>
```

| Spec | Value |
|---|---|
| Radius | 9999px |
| Border | `border-background-surface-300`, hover toward muted foreground |
| Background | gradient surface overlay |
| Blur | `backdrop-blur-md` |
| Hover | overlay opacity 70% to 100%, chevron translate-x |

### Cards & Containers

- Dark cards use semantic surface tokens instead of raw black.
- Borders do more structural work than shadows.
- Product sections should use 8px radius panels, not oversized 20-32px card bubbles.
- Logo-wall containers are edge-masked with gradient fades rather than boxed cards.

### Navigation

- Desktop links are text-only, compact, and horizontally grouped.
- GitHub social proof appears as a compact icon + count, not a large social banner.
- Nav CTAs use tiny 26px height at desktop (`text-xs px-2.5 py-1 h-[26px]`).
- Mobile exposes a simple rounded-md hamburger button with foreground-lighter icon color.

### Inputs & Forms

- The captured homepage contains a form/input count, but the hero does not expose a full form system.
- Use the semantic control tokens when extending:
  - border: `--border-control`
  - background: `--background-control`
  - focus: `--brand-600`
  - error: `--destructive-default`

### Hero Section

- H1 is two spans: first white, second green.
- Paragraph stays centered, readable, and restrained.
- CTA pair sits directly under copy with `gap-2`.
- Customer logos are muted, horizontally scrolling, and fade at both edges.

### 13-2. Named Variants

**button-primary-dashboard**

| Spec | Value |
|---|---|
| Use | Main signup/project CTA |
| Height | 38px hero / 26px nav |
| Radius | 6px |
| Fill | deep brand green (#00623A on dark) |
| Border | green alpha border |
| State | hover reduces intensity through alpha instead of swapping to a new hue |

**button-secondary-muted**

| Spec | Value |
|---|---|
| Use | "Request a demo", sign-in style actions |
| Fill | muted/alternative surface |
| Border | strong to stronger |
| State | surface selection on open/hover |

**announcement-glass-pill**

| Spec | Value |
|---|---|
| Use | top hero announcement |
| Radius | full pill |
| Technique | gradient overlay + `backdrop-blur-md` + opacity transition |
| State | chevron slides from `-translate-x-1` to `translate-x-0` |

### 13-3. Signature Micro-Specs

#### green-terminal-hero-line

```yaml
green-terminal-hero-line:
  description: "The H1 is split into neutral promise and one chromatic scale promise."
  technique: "first span text-foreground (#FAFAFA / {colors.foreground-default}); second span text-brand (#3ECF8E / {colors.brand-default}); both regular weight with tracking 0"
  applied_to: ["{component.hero-section}"]
  visual_signature: "One green phrase behaves like the active terminal prompt and carries the entire brand memory."
```

#### announcement-glass-command-chip

```yaml
announcement-glass-command-chip:
  description: "A SaaS announcement is treated as a translucent app-control chip, not a marketing banner."
  technique: "rounded-full + border-background-surface-300 + bg-gradient-to-br from-background-surface-100 (#1F1F1F) to-background-surface-300 (#292929) + backdrop-blur-md + overlay opacity 70% -> 100%"
  applied_to: ["{component.announcement-pill}", "{component.badges}"]
  visual_signature: "A small smoked-glass command palette chip floating on the dark console surface."
```

#### smoked-logo-wall-fade

```yaml
smoked-logo-wall-fade:
  description: "Customer proof is present but deliberately pushed behind the hero promise."
  technique: "edge gradient mask from hsl(var(--background-default)) / #121212 to transparent and back, with muted foreground treatment"
  applied_to: ["{component.logo-wall}", "{component.hero-section}"]
  visual_signature: "Logos read like a monitoring feed fading into smoked glass rather than a loud trophy shelf."
```

#### dashboard-scale-cta

```yaml
dashboard-scale-cta:
  description: "Marketing calls to action keep product-dashboard proportions."
  technique: "rounded-md 6px radius; hero height 38px with px-4 py-2; nav height 26px with text-xs px-2.5 py-1; duration-200 ease-out; green alpha border on primary"
  applied_to: ["{component.button-primary-dashboard}", "{component.button-secondary-muted}", "{component.navigation}"]
  visual_signature: "The CTA feels ready to be clicked inside a console, not inflated for a generic landing page."
```

#### border-first-dark-surfaces

```yaml
border-first-dark-surfaces:
  description: "Depth is built from semantic dark steps and hairlines before shadow."
  technique: "page #121212 / {colors.background-default}; panels #1F1F1F and #292929; border #2E2E2E with hover toward #454545; sparse shadow usage"
  applied_to: ["{component.cards-containers}", "{component.navigation}", "{component.button-secondary-muted}"]
  visual_signature: "The interface has production-grade separation without chrome-heavy elevation."
```

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Supabase — copy into your root stylesheet */
:root {
  /* Fonts */
  --supabase-font-family: "custom-font", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --supabase-font-family-code: Ubuntu, "Droid Sans", "Segoe WPC", "Segoe UI", sans-serif;
  --supabase-font-weight-normal: 400;
  --supabase-font-weight-bold: 600;

  /* Brand */
  --supabase-brand-display: #3ECF8E;
  --supabase-brand-link: #00C576;
  --supabase-brand-action: #00623A;
  --supabase-brand-action-dark: #00311D;
  --supabase-brand-pale: #DFFFF1;

  /* Surfaces */
  --supabase-bg-page: #121212;
  --supabase-bg-surface-100: #1F1F1F;
  --supabase-bg-surface-300: #292929;
  --supabase-text: #FAFAFA;
  --supabase-text-muted: #4D4D4D;
  --supabase-border: #2E2E2E;
  --supabase-border-stronger: #454545;

  /* Spacing */
  --supabase-space-xs: 8px;
  --supabase-space-sm: 16px;
  --supabase-space-md: 24px;
  --supabase-space-lg: 64px;
  --supabase-space-xl: 96px;

  /* Radius */
  --supabase-radius-control: 6px;
  --supabase-radius-panel: 8px;
  --supabase-radius-pill: 9999px;
}

.supabase-button-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 38px;
  padding: 8px 16px;
  border-radius: var(--supabase-radius-control);
  border: 1px solid color-mix(in srgb, var(--supabase-brand-display) 30%, transparent);
  background: var(--supabase-brand-action);
  color: var(--supabase-text);
  font: 400 14px/1 var(--supabase-font-family);
  transition: background-color 200ms ease-out, border-color 200ms ease-out;
}

.supabase-button-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 38px;
  padding: 8px 16px;
  border-radius: var(--supabase-radius-control);
  border: 1px solid var(--supabase-border);
  background: var(--supabase-bg-surface-100);
  color: var(--supabase-text);
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `{colors.brand-default}` | #3ECF8E |
| Brand action | `{colors.brand-500}` | #00623A |
| Background | `{colors.background-default}` | #121212 |
| Surface | `{colors.background-surface-100}` | #1F1F1F |
| Text primary | `{colors.foreground-default}` | #FAFAFA |
| Text muted | `{colors.foreground-muted}` | #4D4D4D |
| Border | `{colors.border-default}` | #2E2E2E |
| Success | `--colors-green9` | hsl(151,55%,41.5%) |
| Error | `--destructive-default` | hsl(10.2,77.9%,53.9%) |

### Example Component Prompts

#### Hero Section

```text
Supabase 스타일의 dark SaaS hero를 만들어줘.
- 배경: #121212, full dark developer-console surface
- H1: custom-font/system fallback, 72px desktop, weight 400, tracking 0
- H1 구조: 첫 줄 #FAFAFA, 두 번째 줄 #3ECF8E
- 서브텍스트: #FAFAFA, 18px desktop, centered, max-width 672px
- CTA: primary #00623A fill + #3ECF8E alpha border, secondary #1F1F1F surface
- 버튼: height 38px, radius 6px, padding 8px 16px
- 상단 announcement pill: rounded-full, gradient surface, backdrop blur, small chevron motion
```

#### Card Component

```text
Supabase 스타일의 product card를 만들어줘.
- 배경: #1F1F1F 또는 #292929
- border: 1px solid #2E2E2E, hover 시 #454545
- radius: 8px
- padding: 16px 또는 24px
- shadow는 최소화하고 surface contrast로 계층을 만든다
- 제목: 16px, weight 500-600
- 본문: 14px, color #FAFAFA with reduced opacity
```

#### Badge

```text
Supabase announcement pill을 만들어줘.
- radius: 9999px
- border: #292929
- background: #1F1F1F to #292929 subtle gradient
- backdrop-filter: blur(12px) 정도
- text: #FAFAFA, 14px
- hover: overlay opacity만 올리고 chevron을 4px 이동
```

#### Navigation

```text
Supabase 스타일 상단 네비게이션을 만들어줘.
- 높이: 약 64px, 배경 #121212
- 링크: 14px 이하, weight 400, color #FAFAFA
- tiny CTA: height 26px, radius 6px, padding 4px 10px
- Start your project만 green action fill 사용
- GitHub count는 작은 icon+number로 처리
```

### Iteration Guide

- **색상 변경 시**: green은 #3ECF8E 하나를 기억색으로 두고, CTA fill은 더 깊은 #00623A 계열로 분리한다.
- **폰트 변경 시**: Inter fallback 가능하지만 weight 700 hero로 바꾸지 않는다.
- **여백 조정 시**: hero는 64/96px vertical rhythm, 내부 gap은 16/32px를 우선한다.
- **새 컴포넌트 추가 시**: radius 6px controls, 8px panels, border-first hierarchy를 따른다.
- **다크 모드**: dark가 기본이다. light mode를 기본값으로 재해석하지 않는다.
- **반응형**: Tailwind breakpoints 640/768/1024/1280/1536 계열과 모바일 우선 구조를 유지한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #121212 as the page floor and semantic dark surfaces above it.
- Use #3ECF8E as the display brand memory, especially for one decisive phrase or action cue.
- Keep buttons compact: 6px radius, 26px nav height, 38px hero height.
- Use borders and surface steps before shadows.
- Keep hero typography regular-weight and centered.
- Let logo walls and social proof fade into the dark surface rather than shouting.
- Use `focus-visible` green rings for accessible interaction states.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#121212` 사용.
- 본문 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#FAFAFA` 사용.
- Supabase brand green을 `#00FF00` 같은 neon green으로 바꾸지 말 것 — 대신 `#3ECF8E` 사용.
- CTA fill을 밝은 `#3ECF8E` 전체 면으로 과하게 채우지 말 것 — dark CTA에서는 `#00623A` 계열 사용.
- border를 `#CCCCCC` 같은 light gray로 두지 말 것 — 대신 `#2E2E2E` 또는 `#454545` 사용.
- hero에 `font-weight: 700` 이상을 기본 적용하지 말 것 — captured hero는 regular display에 가깝다.
- 버튼 radius를 `16px` 이상 카드형 pill로 키우지 말 것 — 기본 control radius는 `6px`, pill은 announcement에만 사용.
- 보라 AI gradient `#667EEA` to `#764BA2`를 쓰지 말 것 — Supabase의 gradient는 dark surface 안의 미세한 보조 효과다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- Second brand color: absent. Green is the only chromatic brand memory.
- Pure white page chrome: none. White appears as text, not as the page surface.
- Heavy display weights: avoided in the hero. Size and color create hierarchy.
- Decorative illustration hero: absent. No SVG mascot, no abstract blob scene.
- Oversized rounded SaaS cards: absent from the hero language; controls stay compact.
- Loud multi-color gradients: absent. Gradient appears as subtle dark surface treatment.
- Chrome-heavy shadows: minimal. Borders, alpha, and surface steps carry structure.
- Long marketing nav copy: absent. Nav labels are compact product/developer categories.
- Warm beige/cream palette: absent. The neutral system is cool grayscale dark.
- 3D blueprint of database architecture in the hero: absent. The console stays flat.
- Animated lab schematic background: zero. Surfaces step in flat dark tiers.
- Decorative engineering toolbox illustration: never. Tools are inline product nouns.
- Demo video autoplay over the green scaling line: none. The probe-light is a single static phrase.
- Probe-light glow effect under the CTA: absent. Buttons remain dashboard-flat with alpha-only hover.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Phase1 reuse date** — the available artifacts were captured on 2026-04-20/2026-04-23, while this report is regenerated later. Supabase may have changed since the capture.
- **Homepage-biased analysis** — the screenshot and HTML emphasize the marketing homepage. Dashboard, docs, auth flows, pricing forms, and account settings were not deeply visited.
- **Exact display font unresolved** — phase1 exposed `custom-font` but not a definitive public family name. Fallback guidance therefore uses behavior, not a named licensed face.
- **Color hex conversions** — several core tokens are stored as HSL custom properties. Hex values for those tokens are approximate conversions for implementation convenience.
- **Motion behavior limited** — CSS utilities and observed marquee/hover states were considered, but JavaScript-driven scroll animations were not exhaustively traced.
- **Form states incomplete** — the captured homepage has minimal form exposure; validation, disabled, loading, and error input states are inferred from semantic tokens only where explicit tokens exist.
- **Logo wall contamination handled manually** — frequency candidates include customer/SVG colors and transparency artifacts; brand selection prioritizes semantic tokens and observed hero usage.
