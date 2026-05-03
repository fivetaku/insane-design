---
schema_version: 3.2
slug: github
service_name: GitHub
site_url: https://github.com
fetched_at: 2026-05-03T00:00:00+09:00
default_theme: dark
brand_color: "#0FBF3E"
primary_font: Mona Sans VF
font_weight_normal: 400
token_prefix: --base-*, --brand-*, --fgColor-*, --bgColor-*, --borderColor-*, --button-*

bold_direction: "Industrial Collaboration"
aesthetic_category: "Cool Productivity"
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv3
design_system_level_evidence: "Primer primitives, accessibility theme matrices, marketing components, and brand-specific tokens are all present in the captured CSS."

colors:
  canvas-deep: "#050650"
  text-on-emphasis: "#FFFFFF"
  primary: "#0FBF3E"
  accent: "#0377FF"
  ink: "#191F1B"
  border-muted: "#21262D"
typography:
  display: "Mona Sans VF"
  body: "Mona Sans VF"
  code: "ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace"
  ladder:
    - { token: h00, size: "3rem", mobile: "2.5rem", weight: 700, tracking: "0" }
    - { token: h0, size: "2.5rem", mobile: "2rem", weight: 700, tracking: "0" }
    - { token: h1, size: "2rem", mobile: "1.625rem", weight: 600, tracking: "0" }
    - { token: body, size: ".875rem", mobile: ".875rem", weight: 400, tracking: "0" }
  weights_used: [100, 400, 450, 500, 550, 600, 700]
  weights_absent: [300, 800, 900]
components:
  button-primary: { bg: "{colors.primary}", color: "{colors.text-on-emphasis}", radius: ".375rem", min_height: "2.5rem" }
  button-secondary-dark: { bg: "transparent", color: "{colors.text-on-emphasis}", border: "1px solid #FFFFFF52", radius: ".375rem" }
  nav-dropdown: { bg: "var(--brand-color-canvas-default)", shadow: "var(--shadow-floating-small)", radius: ".375rem" }
  focus-ring: { outline: "2px solid var(--focus-outlineColor)", offset: "-.125rem" }
---

# DESIGN.md — GitHub (Designer Guidebook Edition)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

GitHub의 홈은 개발자 도구의 랜딩 페이지라기보다 거대한 공동 작업 인프라의 야간 로비처럼 작동한다. 첫 화면은 깊은 네이비 `#050650` (`{colors.canvas-deep}`) 위에 흰 로고, 흰 타이포, 초록 CTA 하나를 올린다. 검은색이 아니라 거의 우주항만 같은 남색을 쓰기 때문에, 화면은 빈 배경이 아니라 수많은 저장소와 에이전트가 뒤에서 돌아가는 관제실처럼 느껴진다. 이 구조의 핵심은 장식이 아니라 신뢰다. 표면은 어둡고 조용하지만, 모든 인터랙션은 Primer 토큰으로 규격화되어 있다.

이 사이트는 "개발자가 이미 알고 있는 GitHub"와 "Copilot 이후의 플랫폼 GitHub"를 한 화면에 묶는다. 헤드라인은 설명하지 않고 출발 안내판처럼 선언한다. "The future of building happens together"라는 큰 문장은 `Mona Sans VF`의 부드러운 둥근 획으로 세워지고, 아래의 입력창과 버튼은 제품 가입 플로우를 즉시 시작한다. 과장된 카드 쇼케이스가 아니라, 검색창과 터미널을 다뤄본 사람이 바로 이해하는 밀도다. 박물관식 여백이 아니라 서버 랙 앞 통로 같은 여백이다. 조용하지만 언제든 손을 뻗으면 포트와 케이블이 있는 구조다.

색은 두 축으로 갈라진다. 시스템 UI에서는 `--fgColor-*`, `--bgColor-*`, `--borderColor-*` 같은 의미론적 토큰이 우선이고, 마케팅 홈에서는 초록 `#0FBF3E` (`{colors.primary}`)와 파랑 `#0377FF` (`{colors.accent}`)가 행동과 링크를 나눈다. 초록은 거대한 터미널에서 딱 하나 켜진 탑승 게이트 조명이다. 가입/시작의 문은 하나이고, 파랑은 활주로 가장자리의 유도등처럼 탐색과 포커스를 맡는다. no second brand color: 파랑은 문이 아니라 길 표시다. 흰색 `#FFFFFF` (`{colors.text-on-emphasis}`)은 로고, nav, headline을 묶는 신뢰층으로 쓰인다.

GitHub의 craft는 "많이 보여주기"가 아니라 "이미 모든 상태를 고려했다"는 감각이다. 드롭다운은 광고판이 아니라 정밀 공구함 서랍처럼 열리고, 메뉴 안의 monospace label은 개발자 색인 카드처럼 작게 붙는다. shadow는 chrome 전체를 부풀리는 데 쓰이지 않고, floating overlay가 책상 위로 살짝 들리는 순간에만 등장한다. 보라 glow는 일부 hero craft에만 머물며 브랜드 팔레트의 중심으로 올라오지 않는다.

GitHub의 정체성은 단순함의 뒤쪽에 있다. light, dark, colorblind, tritanopia, high contrast, dimmed 테마가 같은 체계 안에 있고, pointer coarse에서는 터치 타겟이 `2.75rem`로 커진다. 겉으로는 단일한 첫 화면이지만 내부는 접근성 모드와 컴포넌트 상태가 촘촘하게 배선된 switchboard다. 사이트라는 자의식이 강하게 나서지 않고, 협업 인프라가 이미 켜져 있다는 감각만 남긴다.

비유로 다시 정리하면 GitHub 홈은 마케팅 광고판이 아니라 **엔지니어링다이어그램이 펼쳐진 시연 실험실**이다. deep navy canvas는 야간 조명이 들어온 lab bench, 흰 nav links는 공구함 위에 정렬된 라벨된 서랍, 초록 CTA는 실험실 문 옆에 단 하나만 켜진 유도등이다. dropdown은 정밀 공구함 서랍이 슬라이드되며 열리는 동작 그대로이고, monospace menu label은 blueprint 도면 한구석에 인쇄된 부품 색인이다. Mona Sans VF로 짠 hero headline은 실험 결과가 적힌 시연 보드의 caption처럼 균질하고, 보라 glow는 고전압 케이블 끝에서 잠깐 새어 나오는 라이트일 뿐 — 메인 도면을 덮지 않는다.

### Key Characteristics

- Deep navy hero canvas: screenshot 기준 `#050650` 계열의 거의 검은 남색이 첫 인상을 지배한다.
- Mona Sans VF first: HTML에서 `MonaSansVF-wdth-wght-opsz`가 preload되고 Primer primitives는 `--fontStack-sansSerif`를 `Mona Sans VF`로 둔다.
- Green action, blue navigation: CTA는 `#0FBF3E`, 링크/포커스/액센트는 `#0377FF`/`#1F6FEB` 계열을 쓴다.
- Primer token lattice: `--base-*` raw scale 위에 `--brand-*`, `--fgColor-*`, `--bgColor-*`, `--button-*` semantic alias가 놓인다.
- Accessibility is visible in CSS: light/dark뿐 아니라 colorblind, tritanopia, high contrast, dimmed 테마 CSS가 함께 로드된다.
- Rounded but not soft: 기본 radius는 `.375rem`, 작은 radius는 `.1875rem`; pill보다 엔지니어링 도구의 물성이 강하다.
- Motion is restrained: dropdown과 reveal은 `.2s`~`.8s`, cubic-bezier 기반으로 짧게 끝난다.
- Marketing hero borrows product trust: 가입 form, search icon, nav dropdown이 제품 UI처럼 정리되어 있다.
- Monospace labels are selective: nav group title과 code 영역에만 monospace를 넣어 개발자 맥락을 만든다.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Industrial Collaboration
> **Aesthetic Category**: Cool Productivity
> **Signature Element**: 이 사이트는 **deep navy collaboration lobby with one decisive green action**으로 기억된다.
> **Code Complexity**: high — theme matrices, Primer token layers, responsive marketing modules, and animated hero craft coexist.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 GitHub처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Mona Sans VF", -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
  font-weight: 400;
  letter-spacing: 0;
}

/* 2. 배경 + 텍스트 */
:root {
  --github-canvas: #050650;
  --github-fg: #FFFFFF;
}
body {
  background: var(--github-canvas);
  color: var(--github-fg);
}

/* 3. 행동 색상 */
:root {
  --github-action: #0FBF3E;
  --github-accent: #0377FF;
}
```

**절대 하지 말아야 할 것 하나**: GitHub을 "검정 배경 + 파란 버튼"으로 단순화하지 말 것. GitHub 홈의 첫 CTA는 초록이고, 파랑은 링크/포커스/보조 강조 역할이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://github.com` |
| Fetched | `2026-05-03T00:00:00+09:00` |
| Phase1 reused | `insane-design/github/phase1/*.json`, `insane-design/github/css/*`, `insane-design/github/index.html`, `insane-design/github/screenshots/hero-cropped.png` |
| HTML size | `564567` bytes |
| CSS files observed | 25 files in `insane-design/github/css/` |
| Primary CSS evidence | `home`, `landing-pages`, `marketing-navigation`, `primer`, `primer-primitives` |
| Extracted variables | `2236` total vars, `1996` resolved |
| Token prefix | `--base-*`, `--brand-*`, `--fgColor-*`, `--bgColor-*`, `--borderColor-*`, `--button-*` |
| Method | phase1 JSON reuse + targeted CSS/HTML/screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: GitHub production web stack with asset-bundled CSS/JS and Primer React modules.
- **Design system**: Primer + Primer Brand. Evidence includes `primer-primitives`, `primer`, `primer-react-css`, `marketing-navigation`, and theme-specific CSS.
- **CSS architecture**:
  ```text
  --base-*        raw color, size, radius, duration, easing, breakpoint, z-index scales
  --brand-*       marketing semantic layer and Primer Brand components
  --fgColor-*     foreground semantic aliases
  --bgColor-*     canvas/background semantic aliases
  --borderColor-* border semantic aliases
  --button-*      stateful component aliases
  ```
- **Class naming**: Mix of stable Primer utilities and CSS-module classes such as `NavDropdown-module__button__PEHWX`.
- **Default theme**: dark first in the captured hero, while HTML includes both light and dark theme data attributes.
- **Font loading**: `MonaSansVF-wdth-wght-opsz` is preloaded as a `.woff2`.
- **Accessibility architecture**: separate CSS files for colorblind, tritanopia, high contrast, and dimmed modes.
- **Canonical anchor**: top marketing nav plus centered signup hero.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

Primary UI typography is `Mona Sans VF`, exposed through `--fontStack-sansSerif`, `--fontStack-sansSerifDisplay`, and `--fontStack-system`. The fallback chain is:

```css
font-family:
  "Mona Sans VF",
  -apple-system,
  BlinkMacSystemFont,
  "Segoe UI",
  "Noto Sans",
  Helvetica,
  Arial,
  sans-serif,
  "Apple Color Emoji",
  "Segoe UI Emoji";
```

Code and technical labels use:

```css
font-family:
  ui-monospace,
  SFMono-Regular,
  SF Mono,
  Menlo,
  Consolas,
  Liberation Mono,
  monospace;
```

### Note on Font Substitutes

If `Mona Sans VF` is unavailable, use `Inter` only as a temporary measurement substitute, not as the final visual substitute. The GitHub feeling comes from Mona Sans' wide, friendly, engineered grotesk shape; plain system `Arial` makes the hero look cheaper. For a close open fallback, use `Mona Sans` from GitHub's public font release, then system stack. For code snippets, keep `SF Mono`/`Menlo`/`Consolas`; do not switch code to the body font.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

GitHub uses a moderate engineering scale in Primer and a larger marketing scale in the hero. The extracted Primer core scale includes:

```css
:root {
  --h00-size: 3rem;
  --h0-size: 2.5rem;
  --h1-size: 2rem;
  --h2-size: 1.5rem;
  --h3-size: 1.25rem;
  --h4-size: 1rem;
  --h5-size: .875rem;
  --h6-size: .75rem;
  --body-font-size: .875rem;
}
```

Marketing hero typography exceeds this base scale visually, with a large center-aligned headline around the 64px range in the screenshot. Body copy sits around 20px and is kept short enough to preserve the hero's central mass.

### Principles

1. Use Mona Sans for both product trust and marketing warmth; do not mix in decorative display fonts.
2. Keep `letter-spacing: 0`; GitHub's captured CSS does not rely on negative tracking as a brand trick.
3. Use 400 for normal body, 500 for nav and medium labels, 600 for emphasis, 700 for large headings.
4. Let size, not font family contrast, create hierarchy.
5. Use monospace only for code, command-like labels, or developer-context metadata.
6. Keep line-height generous enough for scanning: body defaults to `1.5`, headings tighten by size.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

GitHub's color system is not a small brand palette. It is a semantic accessibility matrix. The top-level base scales include gray, blue, green, yellow, orange, red, purple, pink, coral, lemon, lime, teal, and indigo. For the captured homepage, only a few colors define the visual identity.

### Core Tokens

```css
:root {
  --github-hero-canvas: #050650;
  --github-text-on-emphasis: #FFFFFF;
  --github-action-green: #0FBF3E;
  --github-link-blue: #0377FF;
  --github-border-dark: #21262D;
  --github-ink: #191F1B;
}
```

### Semantic Roles

- **Hero canvas** — `#050650`, the screenshot's deep navy field.
- **Primary action** — `#0FBF3E`, green CTA in the captured hero and aligned with the green action scale.
- **Accent/link/focus** — `#0377FF` and `#1F6FEB` family.
- **Text on emphasis** — `#FFFFFF`, used for nav, headline, and CTA text.
- **Muted border** — `#21262D`, used by dark landing sections and Primer defaults.

### 06-8 Color Stories

- **Deep navy lobby** — `#050650` is the first viewport's emotional base. It says infrastructure, not entertainment.
- **One green door** — `#0FBF3E` marks the signup action. Keep it rare and decisive.
- **Blue as system light** — `#0377FF`/`#1F6FEB` is for links, focus, and product affordance, not the main CTA.
- **White as trust layer** — `#FFFFFF` carries logo, nav, headline, and major contrast. Do not tint it cream.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

Primer primitives provide a strict 4px-based size system:

```css
--base-size-4: .25rem;
--base-size-8: .5rem;
--base-size-12: .75rem;
--base-size-16: 1rem;
--base-size-24: 1.5rem;
--base-size-32: 2rem;
--base-size-48: 3rem;
--base-size-64: 4rem;
--base-size-80: 5rem;
--base-size-96: 6rem;
--base-size-128: 8rem;
```

Landing page spacers grow responsively:

```css
.lp-Spacer {
  height: var(--Spacer-size, 80px);
}
@media (min-width: 768px) { /* 112px default path */ }
@media (min-width: 1012px) { /* 128px default path */ }
@media (min-width: 1280px) { /* 156px default path */ }
```

### Whitespace Philosophy

GitHub whitespace is not luxury whitespace. It is operational whitespace. The hero centralizes a compact signup cluster, then lets the deep canvas and glow breathe below it. Section spacing is large, but borders and grid lines keep the page from becoming airy or editorial. Use whitespace to make dense systems feel calm, not to make the brand feel precious.

---

## 08. Radius
<!-- SOURCE: auto -->

Primer primitives define a pragmatic radius ladder:

```css
--borderRadius-small: .1875rem;   /* 3px */
--borderRadius-medium: .375rem;   /* 6px */
--borderRadius-large: .75rem;     /* 12px */
--borderRadius-full: 624.938rem;
--borderRadius-default: var(--borderRadius-medium);
```

Use `.375rem` for most controls and dropdowns. Use `.75rem` only when the component is larger and needs softer containment. Do not make every card a 24px rounded rectangle; GitHub's surface is engineered and compact.

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

Shadows are not a decorative brand motif on the hero; they appear mainly in overlays, dropdowns, and product surfaces. The marketing navigation dropdown uses `var(--shadow-floating-small)` with `.375rem` radius. The captured hero relies more on contrast, glow, and depth from the lower visual element than on card shadows.

Use shadows sparingly:

- Dropdowns and popovers may use floating shadows.
- Cards should prefer border lines and dark surface contrast.
- CTA buttons should shift color, not gain large glow.
- Hero objects may glow, but controls should stay crisp.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

Motion is short and functional. Primer primitives define durations from `50ms` through `1s`, and the nav dropdown uses `.3s` with `cubic-bezier(.16,1,.3,1)`. Marketing sections use reveal motion such as opacity + `translateY(24px)` over `.8s`.

```css
--base-duration-100: .1s;
--base-duration-200: .2s;
--base-duration-300: .3s;
--base-easing-easeOut: cubic-bezier(.3,.8,.6,1);
```

Respect `prefers-reduced-motion`. The captured CSS explicitly disables smooth scroll under reduced motion.

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

GitHub's marketing layout uses constrained central content rather than an exposed 12-column marketing grid. `lp-SectionBlock-content` centers content and, above `1012px`, uses `max-width: var(--brand-Section-container-maxWidth)`. Customer story grids become three columns at desktop via border logic such as `:not(:nth-child(3n))`.

### Hero

The captured hero is center-aligned:

- Top nav spans the width with logo, dropdown groups, search icon, sign-in, and sign-up.
- H1 sits centered with large Mona Sans text.
- Supporting copy is a short two-line paragraph.
- Signup form and secondary Copilot button form one horizontal control cluster.
- Lower hero area introduces a glow/visual universe but keeps the first CTA visually dominant.

### Section Rhythm

Landing sections use large responsive spacers and border-separated blocks. On desktop, section content may receive vertical side borders to create a subtle architecture-grid feeling. This is why GitHub feels organized even when the page contains many marketing modules.

### Card Patterns

Cards and customer story cells are usually border-defined rather than heavily shadowed. Border color is dark and thin. Hover states rely on opacity, transform, background, and link affordance rather than loud elevation.

### Navigation Structure

Navigation is horizontal on desktop and dropdown-driven. Dropdowns are CSS-module components with opacity/visibility/transform transitions, `.375rem` radius, and floating shadow. The link typography is medium weight, with icon and subtitle variants inside dropdown groups.

### Content Width

Hero copy is intentionally narrow. CTA inner content uses max widths such as `980px` and descriptions around `720px`. This prevents the page from feeling like a documentation site even though it is built on a documentation-grade design system.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

Key breakpoints are defined in Primer primitives:

```css
--breakpoint-xsmall: 20rem;
--breakpoint-small: 34rem;
--breakpoint-medium: 48rem;
--breakpoint-large: 63.25rem;
--breakpoint-xlarge: 80rem;
--breakpoint-xxlarge: 87.5rem;
```

Marketing CSS uses practical pixel equivalents:

- `544px` — small spacing shifts.
- `768px` — tablet layout and centered section content.
- `1012px` — desktop nav/dropdown behavior and large section borders.
- `1280px` — wider nav typography and larger dropdown spacing.

Touch targets are pointer-aware. For coarse pointers, `--control-minTarget-auto` becomes `2.75rem`. For fine pointers it can shrink to `1rem`, preserving desktop density.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### 13-1 Component Categories

- **Primary CTA** — green filled button, white text, `.375rem` radius, strong contrast against dark canvas.
- **Secondary CTA** — transparent/dark button with white border, white text, and no fill.
- **Email input** — white surface, dark placeholder, paired with the primary button as a single signup unit.
- **Top nav link** — medium-weight text, icon gap `--base-size-4`, hover/focus color shifts to focus/accent.
- **Nav dropdown** — absolute desktop overlay, `.375rem` radius, `var(--shadow-floating-small)`, grid list columns.
- **Focus ring** — explicit 2px outline using focus token; offset varies by component.

### 13-2 Named Variants

```yaml
button-primary:
  bg: "#0FBF3E"
  fg: "#FFFFFF"
  radius: ".375rem"
  behavior: "hover darkens within green scale"

button-secondary-dark:
  bg: "transparent"
  fg: "#FFFFFF"
  border: "1px solid #FFFFFF52"
  behavior: "stays quiet; works as comparison action"

nav-link:
  font_weight: 500
  gap: "var(--base-size-4)"
  hover: "var(--brand-color-focus, var(--fgColor-accent))"

nav-dropdown:
  radius: ".375rem"
  shadow: "var(--shadow-floating-small)"
  transform: "scale(.99) translateY(-.7em) -> scale(1) translateY(0)"
```

### 13-3. Signature Micro-Specs

```yaml
one-green-door-cta:
  description: "Primary signup is the only filled action; the Copilot action stays outlined."
  technique: "background #0FBF3E /* {colors.primary} */; color #FFFFFF /* {colors.text-on-emphasis} */; border-radius .375rem; secondary border 1px solid #FFFFFF52"
  applied_to: ["{component.button-primary}", "{component.button-secondary-dark}", "hero signup form"]
  visual_signature: "A single green gate light in a dark infrastructure lobby; blue never becomes the main door."

primer-floating-dropdown-fold:
  description: "Desktop navigation opens like an engineered drawer, not a glossy mega-menu."
  technique: "border-radius .375rem; box-shadow var(--shadow-floating-small); transform scale(.99) translateY(-.7em) -> scale(1) translateY(0); transition around .3s cubic-bezier(.16,1,.3,1)"
  applied_to: ["{component.nav-dropdown}", "desktop marketing navigation"]
  visual_signature: "Dropdowns feel mechanically precise: shallow lift, small radius, quick fold-out."

monospace-menu-index-labels:
  description: "Menu group headings borrow code-index language without turning the whole nav into monospace."
  technique: "font-family var(--brand-fontStack-monospace); text-transform uppercase; letter-spacing .5px"
  applied_to: ["{component.nav-dropdown}", "nav group title"]
  visual_signature: "Tiny developer index labels sit inside otherwise friendly Mona Sans navigation."

accessibility-theme-switchboard:
  description: "Theme variants are treated as first-class visual infrastructure, not optional skins."
  technique: "parallel CSS/theme paths for light, dark, colorblind, tritanopia, high contrast, and dimmed; semantic aliases via --fgColor-*, --bgColor-*, --borderColor-*"
  applied_to: ["Primer primitives", "theme matrix", "{component.focus-ring}"]
  visual_signature: "The page looks simple, but the color system behaves like a control-room switchboard."

coarse-pointer-target-expansion:
  description: "Touch affordance expands from the same token system while desktop density remains compact."
  technique: "pointer coarse sets --control-minTarget-auto to 2.75rem; fine pointer can compress to 1rem; focus outline 2px with tokenized offset"
  applied_to: ["{component.focus-ring}", "buttons", "navigation controls"]
  visual_signature: "Controls stay engineered on desktop and become visibly tappable on touch without changing brand shape."
```

---

## 14. Content Voice
<!-- SOURCE: manual -->

GitHub's voice is declarative, collaborative, and infrastructure-minded. It avoids startup hyperbole and usually speaks in platform terms: build, collaborate, code, agents, platform. The home headline is broad but not whimsical. Supporting copy names the users and objects directly: developers, agents, code, one platform.

Use short verbs. Use nouns developers recognize. Avoid poetic abstraction unless it points back to collaboration or shipping software.

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
:root {
  --gh-canvas: #050650;
  --gh-fg: #FFFFFF;
  --gh-primary: #0FBF3E;
  --gh-primary-hover: #08872B;
  --gh-accent: #0377FF;
  --gh-border: #FFFFFF52;
  --gh-radius: .375rem;
  --gh-font: "Mona Sans VF", -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
  --gh-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
}

.github-like {
  min-height: 100vh;
  background: var(--gh-canvas);
  color: var(--gh-fg);
  font-family: var(--gh-font);
  font-weight: 400;
  letter-spacing: 0;
}

.github-like__nav {
  height: 72px;
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 0 32px;
}

.github-like__hero {
  max-width: 760px;
  margin: 0 auto;
  padding: 96px 24px 48px;
  text-align: center;
}

.github-like__hero h1 {
  margin: 0;
  font-size: clamp(48px, 6vw, 72px);
  line-height: 1.05;
  font-weight: 700;
}

.github-like__hero p {
  max-width: 620px;
  margin: 24px auto 0;
  font-size: 20px;
  line-height: 1.5;
}

.github-like__actions {
  display: flex;
  justify-content: center;
  gap: 16px;
  margin-top: 32px;
}

.github-like__button {
  min-height: 48px;
  padding: 0 28px;
  border-radius: var(--gh-radius);
  font-weight: 600;
  border: 1px solid transparent;
}

.github-like__button--primary {
  background: var(--gh-primary);
  color: var(--gh-fg);
}

.github-like__button--primary:hover {
  background: var(--gh-primary-hover);
}

.github-like__button--secondary {
  background: transparent;
  color: var(--gh-fg);
  border-color: var(--gh-border);
}

.github-like :focus-visible {
  outline: 2px solid var(--gh-accent);
  outline-offset: 2px;
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
        github: {
          canvas: "#050650",
          fg: "#FFFFFF",
          primary: "#0FBF3E",
          primaryHover: "#08872B",
          accent: "#0377FF",
          border: "#FFFFFF52"
        }
      },
      borderRadius: {
        github: ".375rem"
      },
      fontFamily: {
        github: ["Mona Sans VF", "-apple-system", "BlinkMacSystemFont", "Segoe UI", "Noto Sans", "Helvetica", "Arial", "sans-serif"],
        githubMono: ["ui-monospace", "SFMono-Regular", "SF Mono", "Menlo", "Consolas", "Liberation Mono", "monospace"]
      }
    }
  }
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

- Canvas: `#050650`
- Text on emphasis: `#FFFFFF`
- Primary CTA: `#0FBF3E`
- CTA hover: `#08872B`
- Accent/focus/link: `#0377FF`
- Dark border: `#21262D`

### Prompt

Build a GitHub-inspired SaaS landing page with a deep navy hero canvas, Mona Sans style typography, centered collaborative headline, compact signup form, green primary CTA, outlined secondary CTA, and Primer-like component discipline. Use semantic tokens, 6px radius controls, explicit focus rings, restrained dropdown motion, and accessible contrast. Keep the page engineered and calm, not glossy or playful.

### Guardrails

- Preserve the green CTA hierarchy.
- Keep blue for links/focus/accent, not the main action.
- Use tokenized CSS, not one-off utility colors.
- Keep controls crisp with `.375rem` radius.
- Include visible focus states and reduced-motion handling.

---

## 18. DO / DON'T
<!-- SOURCE: auto+manual -->

### DO

- Use `#050650` or a very close deep navy for the captured hero background.
- Use `#FFFFFF` for the hero headline/nav text on the dark first viewport.
- Use `#0FBF3E` for the primary signup action.
- Use `#0377FF`/`#1F6FEB` for focus, links, and accent states.
- Use `Mona Sans VF` or the closest available Mona Sans stack.
- Use `.375rem` as the default control radius.
- Use semantic token names for foreground, background, border, and button states.
- Respect pointer coarse touch target expansion around `2.75rem`.

### DON'T

- 배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — captured GitHub hero는 `#050650` deep navy를 사용.
- 주요 CTA를 `#0377FF` 또는 `#1F6FEB` 파랑으로 두지 말 것 — primary signup은 `#0FBF3E` green 사용.
- hero 텍스트를 `#000000` 또는 `black`으로 두지 말 것 — dark hero에서는 `#FFFFFF` 사용.
- border를 `#E5E7EB` 같은 generic gray로 두지 말 것 — dark chrome에는 `#21262D` 또는 `#FFFFFF52` 계열 사용.
- green CTA hover를 임의의 neon `#00FF00`으로 만들지 말 것 — `#08872B`/green scale 안에서 낮춘다.
- body font를 `Arial` 단독으로 두지 말 것 — `Mona Sans VF` 중심 stack 사용.
- 모든 카드를 `24px` radius로 만들지 말 것 — 기본은 `.375rem`, large도 `.75rem` 수준.
- dropdown hover에 긴 `1s` 애니메이션을 쓰지 말 것 — `.2s`~`.3s` 계열의 짧은 motion 사용.
- hero 전체를 보라 그라디언트로 덮지 말 것 — 보라 glow는 lower visual craft에만 제한.

### What This Site Doesn't Use (Negative-Space Identity)

- Beige/cream/editorial paper backgrounds: **absent** — 실험실 lab bench는 deep navy 또는 white, warm paper는 zero.
- Neumorphic shadows on controls: **none** — 정밀 공구함 surface는 hairline + low-alpha drop only, never 부풀린 elevation.
- Rainbow brand gradients as primary surface: **never** — blueprint은 단색이지 무지개가 아니다.
- Decorative serif display typography: **absent** — 시연 보드는 Mona Sans VF 단일 family, 두 번째 폰트는 없다.
- Oversized pill buttons as default: **absent** — control radius는 `.375rem` 엔지니어링다이어그램 표준, pill grammar는 zero.
- Dense dashboard tables in first viewport: **never** — hero는 시연 한 장면이지 운영 콘솔이 아니다.
- Hand-drawn illustration as main identity: **none** — 도면 위에 일러스트 도장은 찍히지 않는다.
- Negative tracking as visible type trick: **absent** — 시연 caption은 `letter-spacing: 0`을 유지한다.
- Card-heavy feature grid above the fold: **zero** — 첫 화면은 비어 있는 lab bench + 단 하나의 초록 게이트로 단순화된다.
- Emoji-led marketing copy: **never** — 공구함 라벨은 짧은 명사 + 동사로만 구성된다.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- The hero canvas `#050650` is inferred from the captured screenshot, while many CSS tokens route through semantic variables and image/gradient layers; exact rendered pixel sampling was not performed in this run.
- The phase1 typography extractor did not produce a full scale map beyond CSS declarations, so marketing hero size is estimated visually and cross-checked against Primer scale tokens.
- Only targeted CSS files were read from the reused phase1 folder: `primer`, `primer-primitives`, `home`, `landing-pages`, and `marketing-navigation`. Other component-specific CSS may contain additional variants.
- The captured page includes duplicate-looking `data-color-mode` attributes in the saved HTML snippet; this guide treats the visible first viewport as dark and the CSS matrix as multi-theme.
- The report intentionally skips Step 6 RENDER-HTML per request; this file is the final artifact.
- Signature Micro-Specs are based on homepage/marketing evidence, not logged-in GitHub app surfaces.
