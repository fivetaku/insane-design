---
schema_version: 3.2
slug: hashnode
service_name: Hashnode
site_url: https://hashnode.com
fetched_at: 2026-04-20T19:56:00+09:00
default_theme: light
brand_color: "#1D52DE"
primary_font: suisseIntl
font_weight_normal: 400
token_prefix: "--"

bold_direction: Builder Editorial
aesthetic_category: other
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: editorial-magazine
archetype_confidence: medium
design_system_level: lv2
design_system_level_evidence: "Tailwind v4 theme tokens plus shadcn-style semantic aliases are actively used across navigation, feed cards, hero, and author actions."

colors:
  background: "#F8FAFC"
  foreground: "#020618"
  primary: "#1D52DE"
  primary-foreground: "#F5F9FF"
  muted: "#F1F5F9"
  muted-foreground: "#62748E"
  border: "#CAD5E2"
  card: "#FFFFFF"
  success: "#399E43"
  destructive: "#DB4241"
typography:
  display: "suisseIntl"
  body: "suisseIntl"
  mono: "suisseMono"
  ladder:
    - { token: text-xs, size: "12px", line_height: "16px", weight: 400, tracking: "0" }
    - { token: text-sm, size: "14px", line_height: "20px", weight: 400, tracking: "0" }
    - { token: text-base, size: "16px", line_height: "24px", weight: 400, tracking: "0" }
    - { token: text-lg, size: "18px", line_height: "28px", weight: 400, tracking: "0" }
    - { token: text-2xl, size: "24px", line_height: "32px", weight: 700, tracking: "-0.025em" }
    - { token: text-3xl, size: "30px", line_height: "36px", weight: 700, tracking: "-0.025em" }
  weights_used: [200, 400, 500, 600, 700, 800, 900]
  weights_absent: [300]
components:
  button-primary: { bg: "{colors.primary}", fg: "{colors.primary-foreground}", radius: "8px", padding: "10px 20px", weight: 500 }
  sidebar-item: { bg_active: "{colors.muted}", fg: "{colors.foreground}", radius: "6px", height: "32px" }
  feed-card: { bg: "{colors.card}", border: "{colors.border}", radius: "14px", shadow: "subtle token shadow" }
  status-pill: { bg: "{colors.success}", fg: "#FFFFFF", radius: "9999px", padding: "4px 10px" }
---

# DESIGN.md — Hashnode

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Hashnode now reads less like a generic SaaS landing page and more like a writing desk that has been opened to the street. The page starts inside the product surface: a left rail, a top feed label, real counts, real navigation, and a hero that sits inside the same bordered content shell as the feed. The metaphor is not "blogging platform brochure." It is a developer newspaper front page pinned inside an app window, where the masthead has become navigation and the lead story is an invitation to write.

The dominant material is cool slate: #F8FAFC (`{colors.background}`) for the app shell, #FFFFFF (`{colors.card}`) for cards, #CAD5E2 (`{colors.border}`) for edges, and #020618 (`{colors.foreground}`) for serious text. The blue #1D52DE (`{colors.primary}`) is held back for author intent: Start your blog, Write, Sign in, selected metrics, and small live dots. Because the blue is sparse, every blue object feels actionable rather than decorative.

Typography is built around suisseIntl with a Tailwind v4 scale. It does not chase dramatic editorial display type. The hero headline is compact at `text-2xl` to `text-3xl`, bold, tight, and deliberately close to interface scale. That makes the sentence "Write to think. Publish to connect." feel like a product command, not a billboard. Hashnode treats its headline like a commit message that somehow made it to page one: brief, active, and meant to start a public record.

The signature craft is the combination of a persistent app sidebar and a soft editorial hero. The hero background uses a dotted grid plus a blue-to-purple translucent diagonal wash, then pairs it with a hand-drawn illustration tile. It feels like graph paper under a drafting lamp: the dots imply structure, the pale wash implies an idea forming, and the illustration keeps the scene from becoming a cold admin console. The page has no second brand color fighting `{colors.primary}`; the purple exists only as a low-opacity weather pattern inside the hero.

The sidebar is not a navigation accessory; it is the spine of the page. Like a newsroom rail beside a live wire feed, it makes every marketing sentence feel already connected to a working publishing product. The main panel then behaves like a broadsheet folded into a dashboard: border first, shadow second, cards stacked for scanning rather than spectacle.

Negative identity matters here. Hashnode does not use a dark hacker palette, does not flood the page with gradients, and does not turn developer blogging into terminal cosplay. The system is quiet, carded, and feed-first: a place where writing becomes a visible practice.

비유로 한 번 더 정리하면 Hashnode는 매거진 편집국의 책상 위에 펼쳐진 잡지 1면이다. 좌측 sidebar는 편집자가 매일 손대는 칼럼 목차, 가운데 bordered panel은 갓 인쇄된 사설 지면, 점묘 grid hero는 편집자가 사설 옆에 끼워둔 그래프 용지, 그리고 Write/Sign in CTA는 편집장이 머리기사 옆에 두는 빨간 도장이다. live 카운트와 status pill은 매거진 후미의 발행 표지처럼 호수와 발행일을 알리고, feed 카드는 같은 잡지 안의 칼럼-사설-스토리북 페이지가 차례로 묶인 모양새다. 즉, 마케팅 splash가 아니라 진짜 매거진 편집실의 작업판이 그대로 화면에 옮겨와 있다.

### Key Characteristics

- App-shell landing page with persistent left sidebar, not a detached marketing hero.
- Cool slate neutrals dominate: #F8FAFC, #FFFFFF, #020618, #CAD5E2.
- Primary blue #1D52DE is reserved for author actions and live/status emphasis.
- suisseIntl is the main voice; suisseMono exists for code-adjacent contexts only.
- Hero type is interface-sized and tight, not oversized display typography.
- Bordered feed containers and rounded cards create a product-dashboard rhythm.
- A dotted grid plus pale blue/purple wash gives the hero a thinking-canvas feel.
- Illustration is human and sketch-like, while chrome remains strict and utilitarian.
- Navigation labels use 14px text, 32px item height, 6px active radius.
- Shadows are tokenized and subtle; borders do most of the spatial work.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Builder Editorial
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **app-shell editorial hero with restrained blue author actions**으로 기억된다.
> **Code Complexity**: high — Tailwind v4 tokens, semantic aliases, dark-mode branches, Font Awesome assets, and Next.js streamed markup are intertwined.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Hashnode처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "suisseIntl", "suisseIntl Fallback", system-ui, -apple-system, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #F8FAFC; --fg: #020618; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #1D52DE; }
.primary-action { background: var(--brand); color: #F5F9FF; border-radius: 8px; }
```

**절대 하지 말아야 할 것 하나**: 전체 페이지를 파란색 브랜드 사이트처럼 만들지 말 것. Hashnode의 파란색은 넓은 배경이 아니라 행동 지점에만 쓰인다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://hashnode.com` |
| Fetched | 2026-04-20T19:56:00+09:00 |
| Extractor | reused phase1 artifacts: HTML/CSS/tokens/screenshot |
| HTML size | 472002 bytes (Next.js streamed app markup) |
| CSS files | 3 external files, total 394173 chars |
| Token prefix | mixed Tailwind v4 + shadcn semantic aliases (`--`) |
| Method | CSS custom properties, token JSON, HTML stream, and hero screenshot observation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js app-style streamed HTML (`self.__next_f.push` payloads present)
- **Design system**: Tailwind v4 theme with shadcn-like semantic aliases
- **CSS architecture**:
  ```css
  core       (--color-slate-*, --color-blue-*, --font-*) raw Tailwind theme values
  semantic   (--background, --foreground, --primary, --muted, --border) UI role aliases
  component  (--sidebar-*, --card-*, --popover-*) surface-specific aliases
  utility    (.text-sm, .rounded-lg, .bg-primary, .tracking-tight) compiled utility classes
  ```
- **Class naming**: Tailwind utilities plus data-slot/data-sidebar component markers.
- **Default theme**: light (bg = `#F8FAFC` via `--background: var(--color-slate-50)`).
- **Font loading**: custom `@font-face` for `suisseIntl`, `suisseMono`, and fallback metric fonts.
- **Canonical anchor**: product shell: sidebar + content panel + feed cards.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `suisseIntl` (custom webfont)
- **Body font**: `suisseIntl`, `suisseIntl Fallback`, `system-ui`, `-apple-system`, `BlinkMacSystemFont`, `"Segoe UI"`, `sans-serif`
- **Code font**: `suisseMono`, `suisseMono Fallback`, `ui-monospace`, `SFMono-Regular`, `Menlo`, `Monaco`, `Consolas`, `"Liberation Mono"`, `"Courier New"`, `monospace`
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-sans: var(--font-suisse-intl), system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-heading: var(--font-suisse-intl), system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-suisse-intl: "suisseIntl", "suisseIntl Fallback";
  --font-suisse-mono: "suisseMono", "suisseMono Fallback";
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
}
```

### Note on Font Substitutes

If suisseIntl is unavailable, use `Inter` only as a practical substitute, then tighten headings with `letter-spacing: -0.025em`. Do not replace it with a geometric display face. Hashnode's voice depends on a neutral grotesk that can sit inside app navigation, long body copy, and feed metadata without changing personality between zones.

For monospace, `SFMono-Regular` or `Menlo` can stand in for suisseMono. Keep mono usage scoped to code, shortcuts, or technical metadata. The main page does not use mono as a brand gesture.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

### Principles

1. Keep display type close to product scale; hero H1 is `24px` to `30px`, not `64px`.
2. Use weight contrast more than size contrast: `700` headline, `600` inline emphasis, `400` paragraph.
3. Let muted text carry rhythm: secondary copy uses slate gray instead of smaller opacity tricks.
4. Tighten large headings with `--tracking-tight: -0.025em`.
5. Preserve generous paragraph leading around `1.6` to `1.75` for editorial credibility.
6. Keep labels and navigation at `14px`; the product frame should scan quickly.

| Token | Size | Line-height | Weight | Use |
|---|---:|---:|---:|---|
| `--text-xs` | 12px | 16px | 400/500 | tiny metadata, counts, hints |
| `--text-sm` | 14px | 20px | 400/500/600 | sidebar labels, buttons, feed metadata |
| `--text-base` | 16px | 24px | 400/600 | default prose and card descriptions |
| `--text-lg` | 18px | 28px | 400/600 | hero paragraph on wider screens |
| `--text-2xl` | 24px | 32px | 700 | mobile/tablet hero headline |
| `--text-3xl` | 30px | 36px | 700 | desktop hero headline |
| `--text-4xl` | 36px | 40px | 700/800 | rare section-level emphasis |
| `--text-5xl` | 48px | tight | 800/900 | available token, not the homepage signature |

Observed weights: `200`, `400`, `500`, `600`, `700`, `800`, `900`. The absence of `300` is important: Hashnode does not get its softness from light typography; it gets it from slate color, spacing, and low-contrast borders.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Core Semantic Tokens

```css
:root {
  --background: #F8FAFC;          /* var(--color-slate-50) */
  --foreground: #020618;          /* var(--color-slate-950) */
  --card: #FFFFFF;
  --primary: #1D52DE;
  --primary-foreground: #F5F9FF;
  --muted: #F1F5F9;               /* var(--color-slate-100) */
  --muted-foreground: #62748E;    /* var(--color-slate-500) */
  --border: #CAD5E2;              /* var(--color-slate-300) */
  --success: #399E43;
  --destructive: #DB4241;
}
```

### 06-2. Dominant Neutrals

| Role | Hex | Notes |
|---|---|---|
| Page shell | `#F8FAFC` | cool slate-50, not pure white |
| Cards | `#FFFFFF` | white cards sit inside slate shell |
| Primary text | `#020618` | slate-950, stronger than generic near-black |
| Secondary text | `#62748E` | slate-500, used for paragraph and metadata |
| Border | `#CAD5E2` | slate-300, visible enough to structure the feed |

### 06-3. Accent System

Hashnode's brand blue is `#1D52DE`. It appears as `--primary`, `--sidebar-primary`, `--chart-3`, and primary CTA fill. A lighter foreground `#F5F9FF` is paired against it. Blue is not used as a page wash except in the hero's translucent gradient layer, where it is lowered to around 10% opacity.

### 06-4. Status Colors

`#399E43` marks live/status moments, such as the live hackathon pill and small green activity dot. `#DB4241` exists as destructive red but is not a main homepage color. Charts use a blue ramp from `#8FB6FF` to `#092B89`.

### 06-5. Dark Mode Branch

CSS includes a `.dark` branch that inverts `--background` to slate-950 and surfaces to slate-900. The captured page is light, and the homepage screenshot uses light as the default identity. Do not infer a dark-first developer brand from the product category.

### 06-6. Transparency

Transparent black values are common: `#0000`, `#0000001A`, `#00000080`. These are utility/shadow/overlay values, not brand neutrals. Avoid counting them as palette leaders.

### 06-7. Brand Candidate Filter

Logo or syntax-highlight colors should not be promoted to brand colors. CSS contains code-highlighting values like `#A5D6FF` and `#7EE787`; they belong to prose/code rendering, not the homepage chrome.

### 06-8. Color Stories

- **Slate Paper** — `#F8FAFC` is the page material. It gives the product shell a soft, cold paper feel while keeping white cards legible.
- **Ink Black** — `#020618` carries headlines and primary navigation. The tone is firm, technical, and less glossy than pure `#000000`.
- **Author Blue** — `#1D52DE` is the action color. It says "write, start, sign in" rather than "decorate."
- **Structural Line** — `#CAD5E2` is the quiet architecture. Borders separate sidebar, hero, feed, and cards without heavy shadow.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

### Whitespace Philosophy

Hashnode uses product whitespace, not luxury whitespace. The left rail is dense and predictable, while the hero gets breathing room through `gap-5`, `gap-8`, and large horizontal padding. This creates an editorial pause without abandoning the dashboard frame.

The base spacing unit is Tailwind v4 `--spacing: .25rem`, so most gaps land on 4px increments. Nav rows are compact at 32px height. Primary buttons use 10px vertical and 20px horizontal padding. The main content shell keeps `px-5` on smaller screens and `sm:px-8` on wider screens.

```css
:root { --spacing: .25rem; }
.sidebar-item { height: 2rem; padding: .5rem; gap: .5rem; }
.hero-inner { padding: 2rem; gap: 2rem; }
.primary-action { padding: .625rem 1.25rem; }
```

Spacing should make the feed feel immediately usable. Avoid giant hero margins that hide the first content card below the fold.

---

## 08. Radius
<!-- SOURCE: auto -->

Hashnode's radius system starts at `--radius: .625rem` (`10px`) and composes around it.

| Pattern | Value | Use |
|---|---:|---|
| Sidebar active item | `6px` | `rounded-md` active row |
| Primary button | `8px` | `rounded-lg` CTA |
| Base token | `10px` | `--radius` |
| Feed/event cards | `14px` to `16px` | bordered cards and hero media |
| Pills | `9999px` | status chips, compact badges |

The system is rounded, but not bubbly. Cards should stay below heavy consumer-app softness; the product frame still needs editorial seriousness.

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

Shadows are secondary. Borders define most surfaces. The CSS token path relies on Tailwind shadow variables:

```css
box-shadow:
  var(--tw-inset-shadow),
  var(--tw-inset-ring-shadow),
  var(--tw-ring-offset-shadow),
  var(--tw-ring-shadow),
  var(--tw-shadow);
```

The most visible shadow in the captured UI is a soft navigation/menu or card lift similar to `0 1px 3px 0 #0000001A, 0 1px 2px -1px #0000001A`. Use it sparingly. A Hashnode clone with heavy floating cards will feel more like a generic AI dashboard than the source.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

Motion is quiet and state-based. Buttons and sidebar rows use `transition-colors`; menu surfaces include data-state classes and transform/opacity tokens from Tailwind. There is no large hero animation in the captured page.

```css
.interactive {
  transition-property: color, background-color, border-color;
  transition-duration: 150ms;
}
```

Keep hover feedback immediate and understated: blue darkens to `primary/90`, sidebar items shift to slate-100, and focus rings use slate/primary tokens.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### App Shell First

The page opens with a fixed-feeling sidebar and a central content panel. The brand mark, primary navigation, author actions, What's New box, Explore, Sign in, and footer links all live in the left rail. This makes the homepage feel like the product, not a disconnected acquisition page.

### Feed Container

The main area uses a rounded top content shell with a header row: "Popular posts" on the left, live activity counts on the right. The hero is nested below this header and separated by borders. This is a strong pattern: hero content belongs to the feed, not above it.

### Editorial Hero

The hero is a two-column composition on desktop: text left, illustration tile right. It uses `flex flex-col sm:flex-row sm:items-center gap-8`. On small screens, the illustration can disappear or stack; the message stays first.

### Content Cards

Post and hackathon cards use a thumbnail on the left, metadata and CTA on the right, with rounded image corners and compact status chips. The card is information-dense, but the border and white fill keep it calm.

### Sidebar Utility Box

The "What's New" item is a small bordered card inside the sidebar. It provides a secondary announcement without stealing the primary content stage.

---

## 12. Responsive
<!-- SOURCE: auto+manual -->

Hashnode's responsive behavior is utility-driven:

- `text-2xl sm:text-3xl` for hero headline.
- `text-sm sm:text-lg` for hero paragraph.
- `flex flex-col sm:flex-row` for hero content.
- `hidden sm:block` for the hero illustration tile.
- `px-5 sm:px-8` for main horizontal gutters.

The mobile priority should be: navigation access, headline, author CTA, then feed cards. Do not preserve the illustration at the cost of readable text.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### 13-1. Component Inventory

- **Sidebar navigation**: icon + 14px label + active slate background, 32px height.
- **Primary CTA**: #1D52DE fill, #F5F9FF text, 8px radius, medium weight.
- **Hero panel**: bordered section, dotted grid, diagonal translucent gradient, copy and illustration.
- **Feed card**: white surface, slate border, rounded media, dense metadata.
- **Status pill**: green live state with white text and pill radius.
- **Announcement card**: small sidebar card with border, close affordance, muted text.
- **Shortcut hint**: tiny gray keycap style for search command.

### 13-2. Named Variants

```yaml
button-primary:
  background: "#1D52DE"
  color: "#F5F9FF"
  radius: "8px"
  padding: "10px 20px"
  font-size: "14px"
  font-weight: 500

sidebar-item-active:
  background: "#F1F5F9"
  color: "#020618"
  radius: "6px"
  height: "32px"
  padding: "8px"

hero-shell:
  background: "#F8FAFC"
  border-bottom: "1px solid #CAD5E2"
  overlay: "radial dot grid + blue/purple translucent diagonal wash"
  padding: "32px"

feed-card:
  background: "#FFFFFF"
  border: "1px solid #CAD5E2"
  radius: "14px"
  shadow: "subtle #0000001A token shadow only when needed"

live-pill:
  background: "#399E43"
  color: "#FFFFFF"
  radius: "9999px"
  padding: "4px 10px"
```

### 13-3. Signature Micro-Specs

```yaml
thinking-grid-hero:
  description: "Hero를 마케팅 배너가 아니라 글쓰기 캔버스처럼 보이게 하는 점묘 grid + 낮은 채도 wash."
  technique: "background: radial-gradient(currentColor 1.25px, transparent 1.25px) 0 0 / 16px 16px, linear-gradient(to bottom right, rgb(96 165 250 / .10), transparent 50%, rgb(192 132 252 / .15)); color: rgb(2 6 24 / .05)"
  applied_to: ["{component.hero-shell}"]
  visual_signature: "파란 면이 아니라, 슬레이트 종이 위에 희미한 기술 노트 격자가 깔린다."

app-shell-broadsheet-frame:
  description: "Homepage를 상단 navbar 랜딩이 아니라 sidebar가 붙은 live editorial product로 고정한다."
  technique: "grid-template-columns: 256px minmax(0, 1fr); sidebar border-right: 1px solid #CAD5E2; main panel margin: 8px 16px; border: 1px solid #CAD5E2; radius: 14px"
  applied_to: ["{component.sidebar-item}", "{component.hero-shell}", "{component.feed-card}"]
  visual_signature: "뉴스레터 첫 장이 아니라, 실제 publishing app 안에서 열린 개발자 신문 1면처럼 보인다."

author-blue-discipline:
  description: "Brand blue를 장식색이 아니라 작성/로그인/상태 같은 author intent에만 배치한다."
  technique: "#1D52DE fill with #F5F9FF text for primary actions; decorative blue only as rgb(96 165 250 / .10); live/status separated with #399E43"
  applied_to: ["{component.button-primary}", "{component.status-pill}", "{component.hero-shell}"]
  visual_signature: "파란색을 보면 브랜드 분위기가 아니라 즉시 누를 수 있는 행동 지점으로 읽힌다."

product-scale-editorial-headline:
  description: "Hero headline을 billboard가 아니라 product command에 가까운 editorial instruction으로 유지한다."
  technique: "font-size: clamp(24px, 2.4vw, 30px); line-height: 1.2; font-weight: 700; letter-spacing: -0.025em"
  applied_to: ["{component.hero-shell}"]
  visual_signature: "큰 외침 대신 짧은 commit message 같은 밀도로 'Write to think'가 박힌다."

border-first-feed-cards:
  description: "공간 분리는 elevation progression보다 slate border가 담당하고, shadow는 보조로만 둔다."
  technique: "border: 1px solid #CAD5E2; background: #FFFFFF; radius: 14px; optional shadow: 0 1px 3px 0 #0000001A, 0 1px 2px -1px #0000001A"
  applied_to: ["{component.feed-card}", "{component.hero-shell}"]
  visual_signature: "카드가 떠오르지 않고 종이처럼 접혀 있으며, feed를 읽는 리듬이 먼저 보인다."
```

---

## 14. Content Voice
<!-- SOURCE: manual -->

Hashnode's copy is direct, writerly, and builder-specific. It avoids broad creator-economy language. "Write to think. Publish to connect." is concise and philosophical, then the paragraph anchors the audience as "builders, engineers, and tech leaders." The tone is motivational but not breathless.

Use:

- Short declarative headline sentences.
- Concrete audience nouns: builders, engineers, tech leaders.
- Reputation and craft framing.
- Product verbs: write, publish, share, grow.

Avoid:

- Generic "create content faster" AI productivity language.
- Neon developer slang.
- Over-explaining blogging as a feature set.

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
:root {
  --hn-bg: #F8FAFC;
  --hn-fg: #020618;
  --hn-card: #FFFFFF;
  --hn-muted: #F1F5F9;
  --hn-muted-fg: #62748E;
  --hn-border: #CAD5E2;
  --hn-primary: #1D52DE;
  --hn-primary-fg: #F5F9FF;
  --hn-success: #399E43;
  --hn-radius: 10px;
  --hn-font: "suisseIntl", "suisseIntl Fallback", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

body {
  margin: 0;
  background: var(--hn-bg);
  color: var(--hn-fg);
  font-family: var(--hn-font);
  font-weight: 400;
}

.hn-shell {
  display: grid;
  grid-template-columns: 256px minmax(0, 1fr);
  min-height: 100vh;
  background: var(--hn-bg);
}

.hn-sidebar {
  border-right: 1px solid var(--hn-border);
  padding: 16px;
}

.hn-nav-item {
  display: flex;
  align-items: center;
  gap: 8px;
  height: 32px;
  padding: 0 8px;
  border-radius: 6px;
  color: var(--hn-fg);
  font-size: 14px;
}

.hn-nav-item[data-active="true"] {
  background: var(--hn-muted);
}

.hn-main-panel {
  margin: 8px 16px;
  overflow: hidden;
  border: 1px solid var(--hn-border);
  border-radius: 14px;
  background: var(--hn-card);
}

.hn-hero {
  position: relative;
  display: flex;
  align-items: center;
  gap: 32px;
  padding: 56px 32px;
  border-bottom: 1px solid var(--hn-border);
  background:
    radial-gradient(currentColor 1.25px, transparent 1.25px) 0 0 / 16px 16px,
    linear-gradient(to bottom right, rgb(96 165 250 / .10), transparent 50%, rgb(192 132 252 / .15)),
    var(--hn-bg);
  color: rgb(2 6 24 / .05);
}

.hn-hero-copy {
  position: relative;
  color: var(--hn-fg);
  max-width: 680px;
}

.hn-hero h1 {
  margin: 0 0 20px;
  font-size: clamp(24px, 2.4vw, 30px);
  line-height: 1.2;
  letter-spacing: -0.025em;
  font-weight: 700;
}

.hn-hero p {
  margin: 0 0 24px;
  color: var(--hn-muted-fg);
  font-size: 18px;
  line-height: 1.65;
}

.hn-button-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 40px;
  padding: 10px 20px;
  border: 0;
  border-radius: 8px;
  background: var(--hn-primary);
  color: var(--hn-primary-fg);
  font-size: 14px;
  font-weight: 500;
}

.hn-card {
  border: 1px solid var(--hn-border);
  border-radius: 14px;
  background: var(--hn-card);
}
```

---

## 16. Tailwind Mapping
<!-- SOURCE: auto+manual -->

```js
export default {
  theme: {
    extend: {
      fontFamily: {
        sans: ["suisseIntl", "suisseIntl Fallback", "system-ui", "sans-serif"],
        mono: ["suisseMono", "suisseMono Fallback", "ui-monospace", "monospace"]
      },
      colors: {
        background: "#F8FAFC",
        foreground: "#020618",
        card: "#FFFFFF",
        primary: {
          DEFAULT: "#1D52DE",
          foreground: "#F5F9FF"
        },
        muted: {
          DEFAULT: "#F1F5F9",
          foreground: "#62748E"
        },
        border: "#CAD5E2",
        success: "#399E43"
      },
      borderRadius: {
        md: "6px",
        lg: "8px",
        xl: "10px",
        "2xl": "14px"
      },
      letterSpacing: {
        tight: "-0.025em",
        tighter: "-0.05em"
      }
    }
  }
}
```

Use Tailwind v4 assumptions: `--spacing: .25rem`, CSS theme variables, and utility-first component assembly. Do not convert the system into hand-authored BEM components unless the target app lacks Tailwind.

---

## 17. Agent Prompt
<!-- SOURCE: manual -->

Build a Hashnode-inspired product homepage for technical writers. Start with an app shell: a left sidebar, compact navigation rows, a bordered main content panel, a feed header, and an editorial hero inside the product surface. Use `suisseIntl` or a close neutral sans substitute. Set the page background to #F8FAFC, primary text to #020618, cards to #FFFFFF, borders to #CAD5E2, muted text to #62748E, and primary actions to #1D52DE with #F5F9FF text.

Keep the headline product-scaled: 24px on small screens and 30px on desktop, bold, tight, with line-height near 1.2. Use blue sparingly for Start/Write/Sign in actions and live highlights. Add a subtle dotted grid and a low-opacity blue/purple diagonal wash in the hero, but do not make the whole page a gradient. Let borders carry layout structure before shadows. Make the first feed card visible below the hero so the page feels like a live writing community, not a marketing splash.

---

## 18. What This Site Doesn't Use
<!-- SOURCE: manual -->

- 배경을 `#FFFFFF` 단독으로 깔지 말 것 — 대신 페이지 shell은 `#F8FAFC`, 카드만 `#FFFFFF` 사용.
- 텍스트를 `#000000` 또는 pure black으로 두지 말 것 — 대신 primary text는 `#020618` 사용.
- 브랜드 블루를 `#0866FF` 같은 generic social blue로 바꾸지 말 것 — Hashnode CTA는 `#1D52DE` 사용.
- muted copy를 `#808080` 회색으로 처리하지 말 것 — slate muted text는 `#62748E` 사용.
- border를 `#E5E7EB`만으로 너무 흐리게 만들지 말 것 — 주요 panel/card border는 `#CAD5E2`가 맞다.
- body에 display font나 serif를 쓰지 말 것 — `suisseIntl` 계열의 neutral sans가 정체성이다.
- hero H1을 56px 이상의 SaaS billboard로 키우지 말 것 — captured hero는 `24px` to `30px` product scale이다.
- 전체 section을 파란/보라 gradient 배경으로 만들지 말 것 — gradient는 hero 내부의 낮은 opacity wash로만 사용.
- 카드마다 큰 shadow를 넣지 말 것 — Hashnode는 border-first이고 shadow는 `#0000001A` 수준으로 얕다.
- sidebar를 제거하고 상단 navbar만 남기지 말 것 — app-shell sidebar가 homepage identity의 절반이다.

### 🚫 Negative-Space Identity

- Second brand color: **none** — 매거진은 단일 author blue로만 운영되고, 두 번째 칼럼 색은 등장하지 않는다.
- Dark hacker palette: **absent** — 편집자 책상은 cool slate paper이지 터미널이 아니다.
- Heavy SaaS billboard hero: **zero** — 헤드라인은 사설 한 줄 분량이지 광고 표지판이 아니다.
- Page-wide gradient wash: **never** — gradient는 hero panel 내부의 낮은 opacity 메모지처럼만 깔린다.
- Card box-shadow elevation default: **absent** — 잡지 종이처럼 border-first, shadow는 보조에만 등장.
- Pure black ink: **never** — `#020618` slate가 사설 잉크 역할을 대신한다.
- Generic social blue CTA: **absent** — 편집장의 빨간 도장 자리는 `#1D52DE`가 고정 점유한다.
- Top-only navbar without sidebar: **never** — 매거진 칼럼 목차가 빠지면 정체성이 절반 사라진다.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- The report reuses existing phase1 artifacts from `insane-design/hashnode/`; it does not refetch `https://hashnode.com` live in this run.
- The hero screenshot captures the logged-out homepage state around 2026-04-20; current production content or counts may differ.
- CSS analysis found a `.dark` branch, but the visual guidance is based on the default light screenshot.
- Some CSS frequency candidates are syntax highlighting, Font Awesome, or transparent utility values; these were intentionally filtered out of brand recommendations.
- The `suisseIntl` and `suisseMono` font license/source details are not inferred beyond observed CSS family names.
- Archetype is marked `editorial-magazine` with medium confidence because the page combines a feed/editorial front page with SaaS/product acquisition actions.
- Component dimensions are derived from compiled Tailwind classes and visual screenshot observation, not from a design-system source file.
