---
schema_version: 3.2
slug: netflix
service_name: Netflix
site_url: https://netflix.com
fetched_at: 2026-04-14T01:23:00+09:00
default_theme: dark
brand_color: "#E50914"
primary_font: "Netflix Sans"
font_weight_normal: 400
token_prefix: "--wct--"

bold_direction: "Cinema Threshold"
aesthetic_category: "other"
signature_element: "hero_impact"
code_complexity: high

medium: web
medium_confidence: high

archetype: editorial-product
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Production CSS exposes --wct-- component tokens and Netflix Sans assets, but page styles are emitted as hashed Emotion-like rules rather than a public token library."

colors:
  brand-red: "#E50914"
  page-black: "#000000"
  hero-wine: "#210E17"
  hero-navy: "#192247"
  focus-gray: "#A9A9A9"
  divider-gray: "#232323"
  text-white: "#FFFFFF"
  text-muted: "rgba(255,255,255,0.7)"
typography:
  display: "Netflix Sans"
  body: "Netflix Sans"
  fallback: "Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif"
  ladder:
    - { token: eyebrow, size: "0.8125rem", weight: 500, line_height: "1.5" }
    - { token: body, size: "1rem", weight: 400, line_height: "1.5" }
    - { token: lead, size: "1.25rem", weight: 400, line_height: "1.5" }
    - { token: section-title, size: "2rem", weight: 700, line_height: "1.25" }
    - { token: hero-title, size: "4rem", weight: 900, line_height: "1" }
    - { token: spectacle-number, size: "7.5rem", weight: 700, line_height: "1" }
  weights_used: [100, 300, 400, 500, 700, 900]
  weights_absent: [200, 600, 800]
components:
  logo-mark: { color: "{colors.brand-red}", desktop_size: "9.25rem x 2.5rem", mobile_size: "5.5625rem x 1.5rem" }
  cta-button: { bg: "{colors.brand-red}", fg: "{colors.text-white}", radius: "0.25rem", weight: 500, transition: "250ms cubic-bezier(0.32,0.94,0.6,1)" }
  secondary-button: { bg: "rgba(128,128,128,0.4)", fg: "{colors.text-white}", radius: "0.25rem", border: "transparent" }
  email-field: { bg: "rgba(22,22,22,0.7)", border: "rgba(128,128,128,0.7)", fg: "{colors.text-white}" }
  faq-row: { bg: "rgb(45,45,45)", hover_bg: "rgb(65,65,65)", radius: "0" }
---

# DESIGN.md - Netflix Designer Guidebook

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Netflix does not present itself as a friendly app shell. It opens like a dark cinema lobby where the screen has not yet lit up. The page is almost entirely built from black surfaces, white type, a single red command color, and deep wine-blue stage lighting. The emotional move is direct: everything except the act of watching is pushed into shadow.

The brand red is not used as decoration. `#E50914` (`{colors.brand-red}`) appears as the logo memory and the conversion action. It is the button, the signal, the exit sign at the end of a dark corridor. There is no second brand color waiting in the wings. The rest of the palette stays low and cinematic: `#000000` (`{colors.page-black}`), `#210E17` (`{colors.hero-wine}`), `#192247` (`{colors.hero-navy}`), gray rails, translucent black input fields, and white text. This restraint makes the red feel louder than its actual surface area.

Typography carries the mass of the page. `Netflix Sans` supplies a compressed, service-owned voice without becoming ornamental. Headings use the heavy end of the family, including 700 and 900, while body copy returns to 400. The result is not luxury minimalism; it is subscription urgency with cinema scale. Large type lands like a trailer title card before the feature starts; smaller copy behaves like the one line of legal-but-readable copy beneath a ticket counter price.

The layout is wide, centered, and poster-like. Containers can reach `120rem`, the hero background stretches wider than the viewport, and the page uses sharp horizontal bands rather than card stacks. The gradients do not behave like decorative aurora; they are the red-wine and navy spill of light on the back wall of a theater. On OLED, pure black can feel like a hole; here the near-black gradients give the screen a room to sit inside.

Radius is modest: `0.25rem` on buttons, `0.5rem` on modal surfaces, `1rem` only on larger media/feature shells. The site is dark, but it is not soft. Edges remain clear, like theater signage and FAQ slabs bolted to the wall rather than cards floating above a dashboard.

Motion and interaction are mostly utility-grade: focus rings, hover surfaces, accordion expansion, and modal scale/opacity transitions. The cinematic feeling comes less from heavy animation and more from contrast choreography: black stage, red action, white headline, dark radial flares, and a few large type moments. Shadow is saved for true overlays; the everyday page does not float because the room itself is already the depth system.

조금 더 풀면, Netflix 홈은 **불 꺼진 박물관 입구의 쇼룸 무대**처럼 작동한다. 검정 페이지 바닥은 갤러리 폐관 직후의 마룻바닥, hero gradient는 진열장 안쪽에 켜진 단 한 줄의 조명이다. 빨간 CTA는 쇼룸 무대 한복판에 세워진 작품 표찰 — 갤러리 카탈로그 첫 페이지의 도장 같은 단 하나의 brand mark다. FAQ row와 plan tier는 박물관 한쪽 벽에 줄지어 걸린 작품 진열장 라벨, 좌우 풀-블리드 band는 무대 뒤편으로 이어지는 갤러리 통로다. 제품사진처럼 큰 헤드라인이 무대 위에 떨어지고, 나머지는 모두 진열장 안 어둠에 잠긴다 — 두 번째 brand color가 없는 이유는, 박물관의 메인 작품에는 단 하나의 스포트라이트만 비추기 때문이다.

### Key Characteristics

- Dominant `#000000` page field with no warm off-white default surface.
- Single conversion red: `#E50914` / `rgb(229,9,20)` for logo and primary action.
- `Netflix Sans` ownership signal with weights spanning 100, 300, 400, 500, 700, and 900.
- Hero scale typography: common 4rem headings and spectacle numerals up to 7.5rem.
- Deep cinematic gradients: `#210E17`, `#192247`, `#461518`, `#6F181D`.
- Translucent black controls: `rgba(22,22,22,0.7)` fields over dark imagery.
- Squared utility components with small radius, usually `0.25rem` or less.
- FAQ rows and dividers use industrial dark grays, especially `rgb(35,35,35)` and `rgb(45,45,45)`.
- Focus treatment is explicit and high contrast through `--wct--focus-ring--*` tokens.
- Layout reads as horizontal broadcast bands rather than modular SaaS cards.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Cinema Threshold
> **Aesthetic Category**: other
> **Signature Element**: 이 사이트는 **black-stage hero with red conversion command**으로 기억된다.
> **Code Complexity**: high — hashed page rules, production font assets, gradient staging, and component-scoped `--wct--` tokens must be preserved together.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Netflix처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Netflix Sans", "Helvetica Neue", "Segoe UI", Roboto, Ubuntu, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #000000; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #E50914; }
.primary-action { background: var(--brand); color: #FFFFFF; border-radius: 0.25rem; }
```

**절대 하지 말아야 할 것 하나**: Netflix를 밝은 SaaS 랜딩처럼 만들지 말 것. 배경을 `#FFFFFF`로 열고 빨간색을 장식 패턴처럼 흩뿌리면 즉시 Netflix가 아니라 generic streaming mockup이 된다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://netflix.com` |
| Fetched | `2026-04-14T01:23:00+09:00` |
| Extractor | reused phase1 assets in `insane-design/netflix/` |
| HTML size | 565,833 bytes |
| CSS files | 2 files, 200,231 bytes |
| Token prefix | `--wct--` |
| Method | existing phase1 JSON + local CSS parsing; Step 6 HTML render skipped by request |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: server-rendered marketing page with hashed generated class names (`default-ltr-iqcdef-cache-*`).
- **Design system**: Netflix web component token layer, prefix `--wct--`.
- **CSS architecture**:
  ```css
  --wct--focus-ring--*                 accessibility interaction tokens
  --wct--local-design--Button-*         local component contract
  --wct--input--date-*                  input component token hooks
  .default-ltr-iqcdef-cache-*           generated per-page presentation rules
  ```
- **Class naming**: generated directional/cache classes with component hash suffixes.
- **Default theme**: dark (`body, html { background: #000; }`).
- **Font loading**: self-hosted Netflix Sans WOFF/WOFF2 plus variable font from Netflix asset hosts; regional overrides include GraphikTH and NKufi.
- **Canonical anchor**: homepage acquisition funnel: logo, hero promise, email entry, CTA, plan/feature bands, FAQ.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Netflix Sans` (self-hosted Netflix brand font)
- **Body font**: `Netflix Sans`
- **Fallback stack**: `Helvetica Neue`, `Segoe UI`, `Roboto`, `Ubuntu`, `sans-serif`
- **Regional alternates**: `GraphikTH`, `NKufi`, `Netflix Sans JA`
- **Weight normal / bold / black**: `400` / `700` / `900`

```css
@font-face {
  font-display: optional;
  font-family: "Netflix Sans";
  font-weight: 700;
  src: url("https://assets.nflxext.com/ffe/siteui/fonts/netflix-sans/v3/NetflixSans_W_Bd.woff2") format("woff2");
}

@font-face {
  font-display: optional;
  font-family: "Netflix Sans";
  font-weight: 900;
  src: url("https://assets.nflxext.com/ffe/siteui/fonts/netflix-sans/v3/NetflixSans_W_Blk.woff2") format("woff2");
}

body {
  font-family: "Netflix Sans", "Helvetica Neue", "Segoe UI", Roboto, Ubuntu, sans-serif;
  font-weight: 400;
}
```

### Note on Font Substitutes

Use `Arial` only as a last-resort system fallback, not as the first substitute. The closest practical substitute stack is `"Helvetica Neue", "Segoe UI", Roboto, Ubuntu, sans-serif`, because Netflix Sans needs a neutral grotesk with strong numerals, compact UI rhythm, and stable 400/500/700/900 behavior. If the brand font is unavailable, compensate with slightly tighter line lengths rather than negative tracking; the captured CSS does not expose a broad tracking system.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

### Principles

1. Lead with mass: hero copy should feel like a title card, not a paragraph headline.
2. Use 400 as the default reading weight and reserve 500 for controls or compact labels.
3. Let 700 and 900 carry brand authority in headings, numerals, and spectacle moments.
4. Keep line-height simple: `1`, `1.25`, and `1.5` cover the page's visible rhythm.
5. Avoid delicate typography. Netflix's landing page is direct, commercial, and high contrast.
6. Do not introduce editorial serif contrast; the identity depends on a sans-only broadcast voice.

| Token | Size | Weight | Line height | Use |
|---|---:|---:|---:|---|
| `micro` | `0.8125rem` | 400/500 | `1.5` | legal, labels, compact support text |
| `body` | `1rem` | 400 | `1.5` | FAQ answers, explanatory copy |
| `lead` | `1.25rem` | 400 | `1.5` | acquisition prompt, section support |
| `section-title` | `2rem` | 700 | `1.25` | FAQ title, feature section title |
| `hero-title` | `4rem` | 900 | `1` | primary acquisition headline |
| `spectacle-number` | `5rem` -> `7.5rem` | 700 | `1` | ranked/visual emphasis numerals |

Observed CSS frequency favors `0.8125rem`, `1rem`, `1.25rem`, `1.5rem`, `2rem`, and `4rem`, with larger responsive stops at `5rem`, `6.25rem`, and `7.5rem`.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

| Token | Value | Role |
|---|---|---|
| `{colors.brand-red}` | `#E50914` / `rgb(229,9,20)` | logo fill, primary CTA, Netflix ownership cue |
| `{colors.page-black}` | `#000000` | body background, image occlusion, stage field |
| `{colors.hero-wine}` | `#210E17` | cinematic background depth and gradient tone |
| `{colors.hero-navy}` | `#192247` | cool dark counterweight in hero/feature fields |
| `{colors.focus-gray}` | `#A9A9A9` | focus-ring fallback color |
| `{colors.divider-gray}` | `#232323` / `rgb(35,35,35)` | separators, dark panels |
| `{colors.text-white}` | `#FFFFFF` | primary text and CTA foreground |
| `{colors.text-muted}` | `rgba(255,255,255,0.7)` | modal/body secondary text |

### 06-1. Dominant Palette

Netflix is a black-first system. The page does not use brand red as a background wash. Red is the action atom. Black, wine, navy, charcoal, and white create the cinema field around that atom.

### 06-2. Brand Red

Use `#E50914` only for moments that need brand ownership or immediate conversion. Good targets: logo, "Get Started", active subscription action. Bad targets: decorative borders, large background gradients, section dividers, icon grids.

### 06-3. Dark Field

`#000000` must remain the body default. Use `rgb(22,22,22)`, `rgb(35,35,35)`, `rgb(45,45,45)`, and `rgb(65,65,65)` to lift interactive panels without leaving the black-stage identity.

### 06-4. Gradient Depth

The captured CSS uses radial and linear gradients with `#461518`, `#6F181D`, `#210E17`, `#192247`, and related near-black chromatics. These colors should feel like light leaking behind a screen, not a decorative aurora.

### 06-5. Text Contrast

Primary text is white. Secondary text can drop to `rgba(255,255,255,0.7)` or `rgba(255,255,255,0.5)`, but never to low-contrast warm gray on black.

### 06-6. Functional Gray

`#A9A9A9` appears repeatedly as focus-ring fallback data. It is a functional accessibility color, not a brand neutral. Do not promote it into a dominant palette color.

### 06-7. SVG Pattern Contamination

Several frequent colors (`#FFF3EB`, `#FFF4EB`, `#F9DDD1`, `#E4A1FA`) are SVG/pattern artifacts from captured assets. They should not be treated as Netflix UI tokens.

### 06-8. Color Stories

- **Red Command** — `#E50914` is reserved for logo and primary action. It turns the dark page from passive browsing into membership conversion.
- **Black Stage** — `#000000` is the main environment. It makes type and media feel projected rather than placed.
- **Wine Depth** — `#210E17` adds cinematic warmth behind feature bands without becoming a second brand color.
- **Navy Shadow** — `#192247` cools the wine gradients and keeps the background from becoming purely red-black.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

Netflix spacing is sectional, not card-based. The page uses wide horizontal bands, centered acquisition forms, and clear vertical rhythm between headline, support copy, and email CTA.

### Whitespace Philosophy

Whitespace is not "airy" here. It is negative stage space. Black margins are used to isolate the sales message and make the next red action feel inevitable. Horizontal space can be very wide (`120rem` max-width shells), while local component spacing stays compact (`0.5rem` icon gaps, `1rem` button horizontal spacing, `1.5rem` common padding).

| Pattern | Value | Use |
|---|---:|---|
| Button x-padding | `1rem` | primary and secondary buttons |
| Icon gap | `0.5rem` | CTA arrow spacing |
| Common local padding | `1.5rem` | button wrappers, modal margins |
| Form max width | `36.625rem` | email capture block |
| Hero text width | around `40.1875rem` to `48.9375rem` | controlled headline/support width |
| Full band max width | `120rem` | large cinematic background systems |

---

## 08. Radius
<!-- SOURCE: auto+manual -->

Netflix radius is small and utilitarian. Buttons and controls usually sit at `0.25rem`; focus geometry uses `0.125rem`; modal surfaces can reach `0.5rem`; larger media shells can use `1rem`.

```css
:root {
  --wct--focus-ring--width: 0.125rem;
  --wct--focus-ring--offset: 0.125rem;
  --wct--local-design--Button-BorderRadius: 0.25rem;
}

.modal {
  border-radius: 0.5rem;
}

.large-media-shell {
  border-radius: 1rem;
}
```

Avoid pill UI unless it comes from a platform control. Netflix's acquisition UI is direct-edged, not bubbly.

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

Box shadow is not a dominant surface language. The captured CSS shows modal-level shadow such as `0 0.25rem 0.5rem 0 rgba(0,0,0,0.8)`, but everyday sections do not float. Depth is produced by black fields, overlays, gradients, and media contrast.

Use shadows only when a surface is literally above the page, such as dialogs. For cards and rows, prefer background changes from `rgb(45,45,45)` to `rgb(65,65,65)`.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

Motion is functional and restrained. The extracted component timing includes `250ms cubic-bezier(0.32,0.94,0.6,1)` for button states and modal transitions around opacity/scale with longer transform durations. This gives controls a responsive feel without turning the page into a motion showcase.

```css
.surface-action {
  transition:
    background-color 250ms cubic-bezier(0.32,0.94,0.6,1),
    color 250ms cubic-bezier(0.32,0.94,0.6,1);
}

.dialog-enter {
  transform: scale(0.88);
  opacity: 0;
  transition:
    opacity 100ms cubic-bezier(0.32,0.94,0.6,1) 100ms,
    transform 533ms cubic-bezier(0.32,0.94,0.6,1) 4ms;
}
```

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### 11-1. Acquisition Hero

The first viewport should behave like a poster plus form. Logo and language/sign-in controls sit above a centered promise. The headline is large and compact; the support copy explains price or membership; the email form and red CTA are the only path forward.

### 11-2. Horizontal Feature Bands

Netflix does not want a grid of equal cards. It wants large bands that feel like scenes: TV, download, watch anywhere, kids. Each band can carry one big image/animation area and one direct text block.

### 11-3. FAQ Stack

FAQ rows are full-width dark strips with no card radius. The row is a command surface: label left, plus icon right, answer expanding below. Use `rgb(45,45,45)` base and `rgb(65,65,65)` hover.

### 11-4. Centered Form Rail

Email capture repeats after persuasion. The form width should be constrained around `36.625rem`, centered, and vertically close to its explanatory prompt.

### 11-5. Wide Background Mechanics

The hero uses wider-than-viewport background geometry. CSS evidence includes `width: 165rem` and `width: 120.5rem` gradient elements, centered through `left: 50%` and transforms. This creates a cinematic field that does not collapse at desktop widths.

---

## 12. Responsive
<!-- SOURCE: auto+manual -->

Netflix uses breakpoint changes around `600px`, `960px`, `1280px`, and `1920px`.

- **Mobile**: logo compresses to `5.5625rem x 1.5rem`; forms stack vertically; headline scale drops; controls remain large enough for touch.
- **Tablet / small desktop**: layout starts opening horizontal spacing; hero and section text gain width.
- **Desktop**: logo reaches `9.25rem x 2.5rem`; headlines can sit at `4rem`; background fields stretch beyond the viewport.
- **Wide desktop**: spectacle numerals and background staging can continue up to `6.25rem` and `7.5rem` where used.

Do not make the mobile version a miniature desktop. The CTA and email form must become a clear vertical sequence.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### 13-1. Core Components

#### Logo

The logo is an SVG/currentColor object using `rgb(229,9,20)`. Keep it red and simple. Do not place it in a white badge or decorative frame.

#### Primary CTA

The primary button is the page's red command. It should use `#E50914`, white text, `font-weight: 500`, `border-radius: 0.25rem`, and a clear arrow/icon affordance when used in the acquisition form.

#### Secondary Button

Secondary actions use translucent gray surfaces such as `rgba(128,128,128,0.4)` with white foreground. Their role is utility, not brand.

#### Email Field

The email field should be translucent black over the dark background: `rgba(22,22,22,0.7)`, white text, visible border/focus states. It must not become a white input unless the whole composition changes.

#### FAQ Accordion

FAQ rows are hard-edged dark blocks. Use full-width rows, large touch targets, plus icons, and hover darkening. Do not wrap each FAQ item in a card with shadow.

#### Dialog

Dialogs can use `rgb(22,22,22)`, `rgba(128,128,128,0.4)` border, `0.5rem` radius, and black shadow. They are one of the few places where elevation is allowed.

### 13-2. Named Variants

```yaml
logo-mark:
  color: "#E50914"
  desktop_size: "9.25rem x 2.5rem"
  mobile_size: "5.5625rem x 1.5rem"

button-primary:
  background: "#E50914"
  color: "#FFFFFF"
  border_radius: "0.25rem"
  font_weight: 500
  padding: "var(--wct--local-design--Button-SpaceVertical) 1rem"

button-secondary:
  background: "rgba(128,128,128,0.4)"
  color: "#FFFFFF"
  border: "rgba(0,0,0,0)"
  border_radius: "0.25rem"

email-field-dark:
  background: "rgba(22,22,22,0.7)"
  color: "#FFFFFF"
  border_color: "rgba(128,128,128,0.7)"

faq-row:
  background: "rgb(45,45,45)"
  hover_background: "rgb(65,65,65)"
  border_radius: "0"
```

### 13-3. Signature Micro-Specs

```yaml
black-stage-red-command:
  description: "Minimum Netflix acquisition signature: black room, white title, one red command."
  technique: "body background #000000; primary CTA background #E50914; foreground #FFFFFF; red reserved for logo and conversion action"
  applied_to: ["{component.logo-mark}", "{component.cta-button}"]
  visual_signature: "The page feels like a dark cinema screen with a single illuminated exit/action sign."

wine-navy-hero-glow:
  description: "Cinematic background depth without introducing a second bright brand color."
  technique: "radial/linear gradients using #210E17, #192247, #461518, #6F181D; background elements observed at 165rem and 120.5rem widths, centered with left: 50% transforms"
  applied_to: ["{component.hero-background}", "{component.feature-band}"]
  visual_signature: "Red-wine and navy light spill behind the hero, like theater wall glow rather than a decorative gradient."

squared-streaming-cta:
  description: "Streaming acquisition button that stays direct-edged and transactional."
  technique: "border-radius 0.25rem; font-weight 500; icon/text gap 0.5rem; transition 250ms cubic-bezier(0.32,0.94,0.6,1)"
  applied_to: ["{component.cta-button}"]
  visual_signature: "A compact red command block, not a pill, badge, or soft SaaS button."

translucent-ticket-email-field:
  description: "Email capture field that sits inside the cinema darkness instead of becoming a white form."
  technique: "background rgba(22,22,22,0.7); border rgba(128,128,128,0.7); foreground #FFFFFF; min-height 3.5rem"
  applied_to: ["{component.email-field}"]
  visual_signature: "A dark glass ticket-window input visible over imagery and gradients."

faq-dark-slab:
  description: "Accordion rows as industrial dark slabs, not cards."
  technique: "background rgb(45,45,45); hover background rgb(65,65,65); border-radius 0; no box-shadow; full-row hit target"
  applied_to: ["{component.faq-row}"]
  visual_signature: "Stacked charcoal bars with hard edges and immediate hover lift through color only."
```

---

## 14. Content Voice
<!-- SOURCE: manual -->

Netflix copy is plain, high-confidence, and transactional. It does not explain the product as a new concept; it states the promise and moves to membership.

- Use direct benefit headlines: "Unlimited movies, TV shows, and more."
- Keep support copy short and concrete: price, cancellation, device availability.
- Use commands for CTAs: "Get Started", "Sign In".
- Repeat email capture after persuasion rather than introducing a different conversion path.
- Avoid playful brand banter. The tone is entertainment access, not social app personality.

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
:root {
  --netflix-red: #E50914;
  --netflix-black: #000000;
  --netflix-white: #FFFFFF;
  --netflix-wine: #210E17;
  --netflix-navy: #192247;
  --netflix-gray-900: rgb(22,22,22);
  --netflix-gray-800: rgb(35,35,35);
  --netflix-gray-700: rgb(45,45,45);
  --netflix-gray-600: rgb(65,65,65);
  --netflix-focus: #A9A9A9;

  --wct--focus-ring--width: 0.125rem;
  --wct--focus-ring--style: solid;
  --wct--focus-ring--color: rgb(255,255,255);
  --wct--focus-ring--offset: 0.125rem;
  --wct--local-design--Button-BorderRadius: 0.25rem;
  --wct--local-design--Button-SpaceBetweenIconText: 0.5rem;
  --wct--local-design--Button-SpaceHorizontal: 1rem;
  --wct--local-design--Button-TextFontWeight: 500;
  --wct--local-design--Button-Duration: 250ms;
}

body {
  margin: 0;
  background: var(--netflix-black);
  color: var(--netflix-white);
  font-family: "Netflix Sans", "Helvetica Neue", "Segoe UI", Roboto, Ubuntu, sans-serif;
  font-weight: 400;
  line-height: 1.5;
}

.netflix-hero {
  position: relative;
  overflow: hidden;
  background:
    radial-gradient(11% 56% at 17% 50%, #461518 0%, transparent 100%),
    radial-gradient(11% 56% at 83% 50%, #461518 0%, transparent 100%),
    linear-gradient(180deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.4) 50%, #000000 100%);
}

.netflix-title {
  max-width: 48.9375rem;
  margin: 0 auto 1rem;
  font-size: clamp(2rem, 6vw, 4rem);
  line-height: 1;
  font-weight: 900;
  text-align: center;
}

.netflix-lead {
  max-width: 40.1875rem;
  margin: 0 auto 1.5rem;
  font-size: 1.25rem;
  line-height: 1.5;
  font-weight: 400;
  text-align: center;
}

.netflix-email-field {
  background: rgba(22,22,22,0.7);
  color: #FFFFFF;
  border: 0.0625rem solid rgba(128,128,128,0.7);
  border-radius: 0.25rem;
  min-height: 3.5rem;
}

.netflix-primary-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: #E50914;
  color: #FFFFFF;
  border: 0;
  border-radius: 0.25rem;
  padding: 0.75rem 1.5rem;
  font-weight: 500;
  transition: background-color 250ms cubic-bezier(0.32,0.94,0.6,1);
}

.netflix-faq-row {
  width: 100%;
  border: 0;
  border-radius: 0;
  background: rgb(45,45,45);
  color: #FFFFFF;
  padding: 1.5rem;
  text-align: left;
}

.netflix-faq-row:hover {
  background: rgb(65,65,65);
}
```

---

## 16. Tailwind Mapping
<!-- SOURCE: manual -->

```js
export default {
  theme: {
    extend: {
      colors: {
        netflix: {
          red: "#E50914",
          black: "#000000",
          white: "#FFFFFF",
          wine: "#210E17",
          navy: "#192247",
          focus: "#A9A9A9",
          slab: "rgb(45,45,45)",
          slabHover: "rgb(65,65,65)"
        }
      },
      fontFamily: {
        netflix: ["Netflix Sans", "Helvetica Neue", "Segoe UI", "Roboto", "Ubuntu", "sans-serif"]
      },
      borderRadius: {
        netflixButton: "0.25rem",
        netflixDialog: "0.5rem",
        netflixMedia: "1rem"
      },
      transitionTimingFunction: {
        netflix: "cubic-bezier(0.32,0.94,0.6,1)"
      }
    }
  }
}
```

---

## 17. Agent Prompt
<!-- SOURCE: manual -->

Build a Netflix-inspired acquisition page with a black cinema-stage identity. Use `#000000` as the body background, `#FFFFFF` for primary text, and reserve `#E50914` for the logo and primary conversion CTA. Use `Netflix Sans` if available, falling back to `"Helvetica Neue", "Segoe UI", Roboto, Ubuntu, sans-serif`. The hero should feel like a dark title card: large 700/900 sans typography, centered copy, an email field with translucent black surface, and a squared red "Get Started" button. Use dark wine/navy gradients (`#210E17`, `#192247`, `#461518`, `#6F181D`) as background depth, not bright decorative gradients. FAQ rows should be full-width dark slabs with no card radius or shadow. Keep radius small (`0.25rem` buttons, `0.5rem` dialogs) and use shadows only for true overlays. Do not turn the page into a bright SaaS landing page, a red gradient poster, or a rounded card dashboard.

---

## 18. What This Site Doesn't Use
<!-- SOURCE: auto+manual -->

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#000000`을 기본 stage로 사용.
- 브랜드 레드를 `#FF0000`으로 대체하지 말 것 — 대신 Netflix action red `#E50914` / `rgb(229,9,20)` 사용.
- 본문 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — dark surface 위에서는 `#FFFFFF` 또는 `rgba(255,255,255,0.7)` 사용.
- CTA를 파란색 `#0066FF` 또는 보라색 `#7C3AED`로 만들지 말 것 — primary action은 `#E50914`.
- Hero gradient를 밝은 pink/orange `#FFBDC0`, `#FFA984`, `#F9DDD1` 중심으로 만들지 말 것 — 이 값들은 SVG/pattern 오염 후보이고, 실제 stage는 `#210E17`, `#192247`, `#461518`.
- FAQ row에 `border-radius: 1rem` 카드 처리를 하지 말 것 — row는 `border-radius: 0` 또는 매우 작은 square slab.
- 모든 카드를 `box-shadow: 0 20px 60px rgba(0,0,0,.2)`로 띄우지 말 것 — Netflix는 section depth를 gradient와 dark slabs로 만든다.
- body 기본 `font-weight: 300`으로 얇게 만들지 말 것 — captured default rhythm은 `font-weight: 400`, controls는 `500`, headings는 `700/900`.
- Primary button을 pill `border-radius: 9999px`로 만들지 말 것 — observed button contract는 `0.25rem`.
- 페이지 전체를 beige `#F5EFE6` 또는 gray `#F5F5F5` surface로 열지 말 것 — Netflix landing은 black-first conversion theater다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **Light SaaS canvas: zero** — 흰 페이지에 다크 카드를 얹는 박물관은 absent. 무대 자체가 검정이고 흰 surface는 never 등장한다.
- **Second brand color: none** — 빨강 `#E50914` 외 chromatic action은 zero. 갤러리 작품 옆 보조 라벨 컬러는 absent.
- **Pill button language: never** — primary action radius는 `0.25rem`, pill은 absent. 진열장 표찰은 둥글게 가공되지 않는다.
- **Friendly pastel surfaces: absent** — pink/orange/peach 톤은 SVG/pattern 오염 후보일 뿐, hero stage palette로는 zero.
- **Heavy card elevation: zero** — FAQ row와 slab은 floating card가 absent. 진열장은 벽에 박혀 있고 떠 있지 않다.
- **Editorial serif headline: none** — Netflix Sans 한 family가 모든 무대 카피를 담당. serif catalog는 never.
- **Beige/cream warm canvas: absent** — landing은 black-first conversion theater. warm productivity 톤은 zero.
- **Decorative gradient orb: never** — gradient는 박물관 벽면 spill light로만 작동, 장식적 mesh는 absent.
- **Universal shadow chrome: zero** — 그림자는 true overlay에만, 쇼룸 진열장 자체는 never 떠 있지 않다.
- **Lightweight `font-weight: 100/200` 본문: absent** — captured rhythm은 400/500/700/900. 가벼운 카탈로그 글자는 zero.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- Phase1 assets are reused from `insane-design/netflix/` and were captured on 2026-04-14. The live Netflix homepage may differ by locale, A/B experiment, authentication state, or date.
- CSS contains SVG/pattern colors with high frequency. This guide treats warm pastel candidates such as `#FFF3EB`, `#FFF4EB`, and `#F9DDD1` as contamination unless they are tied to UI chrome.
- The page exposes many generated hashed classes, so component names in this guide are interpretive wrappers around observed `--wct--` tokens and visible homepage roles.
- Screenshot evidence exists in the phase1 folder, but this requested run skipped Step 6 RENDER-HTML and does not regenerate visual comparison artifacts.
- `design_system_level: lv2` is a judgment call: the system is clearly in production use through tokens and brand fonts, but the public homepage CSS is not a clean exported design-system spec.
- Locale-specific title evidence referenced South Korea in the captured HTML. The design guidance focuses on the global acquisition surface rather than country-specific copy.
