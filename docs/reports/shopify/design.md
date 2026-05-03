---
schema_version: 3.2
slug: shopify
service_name: Shopify
site_url: https://www.shopify.com
fetched_at: 2026-04-20T20:00:00+09:00
default_theme: mixed
brand_color: "#008060"
primary_font: ShopifySans
font_weight_normal: 420
token_prefix: shopify

bold_direction: Commerce Cinematic
aesthetic_category: editorial-product
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: saas-marketing
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Real Shopify homepage CSS exposes Tailwind v4 theme tokens, ShopifySans weights, button state utilities, spacing ramps, and component classes, but not a complete public token graph."

colors:
  primary: "#008060"
  hero-ink: "#061A1C"
  rich-black: "#02090A"
  surface-light: "#FFFFFF"
  surface-soft: "#F4F4F5"
  text-primary: "#000000"
  text-inverse: "#FFFFFF"
  text-muted: "#71717A"
  hairline: "#D4D4D8"
  accent-mint: "#36F4A4"
  accent-cyan: "#30DEEE"
typography:
  display: ShopifySans
  body: ShopifySans
  mono: IBMPlexMono
  ladder:
    - { token: dsp, size: "6rem", weight: 300, line_height: "6.48rem", tracking: "-0.025em" }
    - { token: t1, size: "3.375rem", weight: 330, line_height: "3.645rem", tracking: "-0.005em" }
    - { token: t2, size: "3rem", weight: 330, line_height: "3.3rem", tracking: "-0.005em" }
    - { token: t3, size: "2.25rem", weight: 330, line_height: "2.52rem", tracking: "-0.005em" }
    - { token: body-base, size: "1rem", weight: 420, line_height: "1.4rem", tracking: "-0.006em" }
  weights_used: [300, 330, 400, 420, 450, 500, 550, 600, 700, 800, 900]
  weights_absent: [200]
components:
  button-dark-primary: { bg: "{colors.surface-light}", text: "{colors.text-primary}", radius: "9999px", padding: "8px 20px", hover_bg: "{colors.hairline}" }
  button-light-primary: { bg: "{colors.text-primary}", text: "{colors.surface-light}", radius: "9999px", padding: "8px 20px", hover_bg: "#3F3F46" }
  input-dark-email: { bg: "#FFFFFF26", text: "{colors.text-inverse}", radius: "9999px", border: "#FFFFFF80" }
  nav-dark: { bg: "transparent over media", text: "{colors.text-inverse}", height: "4.5rem" }
---

# DESIGN.md - Shopify

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Shopify의 현재 홈페이지는 "상거래 플랫폼"을 소프트웨어 대시보드처럼 설명하지 않는다. 첫 화면은 거대한 얼굴 클로즈업 영상 위에 놓인 흰 글자, 낮은 조도의 갈색과 블랙, 그리고 매우 단순한 CTA 구조로 시작한다. 제품 설명보다 창업자의 시선, 카메라, 피부 질감, 어두운 스튜디오 조명이 먼저 들어온다. 이 사이트는 SaaS가 아니라 창업자 다큐멘터리의 오프닝 크레딧처럼 보이게 설계되어 있다. 대시보드 스크린샷은 주연이 아니다. 카메라 앞에 선 상인이 먼저 나오고, 플랫폼은 그 뒤에서 조용히 조명을 잡는다.

색은 두 겹으로 작동한다. 실제 Shopify 브랜드의 운영 색은 #008060 (`{colors.primary}`)이지만, 첫 화면의 기억은 #061A1C (`{colors.hero-ink}`)와 #02090A (`{colors.rich-black}`) 쪽에 더 가깝다. 녹색은 페이지 전체를 덮는 브랜드 페인트가 아니라 로고, 일부 액션, 그래픽 악센트에서 짧게 들어오는 신호다. no second brand color처럼 운용된다. 초록은 벽지가 아니라 결제 단말기의 작은 승인등이고, 대부분의 면은 어두운 스튜디오 세트로 남는다. 텍스트와 버튼은 #FFFFFF (`{colors.surface-light}`)로 떠서, 검은 무대 위 흰 가격표처럼 즉시 읽힌다.

타이포그래피는 ShopifySans의 비표준 weight가 핵심이다. 특히 display는 300 또는 330 근처의 얇은 무게와 큰 크기를 함께 써서, "거대한데 무겁지 않은" 인상을 만든다. body는 420 전후로 더 단단하게 받치고, 버튼과 링크는 550 계열까지 올라간다. 일반적인 400/600 Inter 조합으로 바꾸면 Shopify의 넓고 낮은 압력이 사라진다. 이 헤드라인은 광고판처럼 소리치지 않고, 어두운 촬영장에서 붐 마이크가 낮게 지나가듯 큰데 가볍다.

공간은 넓지만 비어 보이지 않는다. 히어로에서는 좌측 텍스트가 커다란 배경 영상 위에 낮게 걸리고, CTA 입력창은 pill 형태로 하나의 물리적 오브젝트처럼 붙는다. 이 pill은 폼이라기보다 카운터 위에 놓인 카드 리더기 같다. 사용자는 브랜드 영화를 보고 있지만, 손끝에는 바로 판매를 시작하는 흰 캡슐이 닿아 있다. 그 아래 섹션은 `container`와 `grid` 유틸리티로 1600px 근처까지 확장되지만, 카드와 상품 예시는 촘촘한 커머스 편집면을 만든다. "큰 꿈"과 "바로 판매"가 같은 화면 안에서 충돌하지 않게, 초반은 영화처럼, 이후는 플랫폼처럼 전환된다.

모션은 장식용 바운스가 아니라 reveal과 방향감이다. HTML에는 word-by-word heading transition, arrow-animation, reduced-motion 분기, hover 상태가 다수 보인다. 즉 Shopify다운 움직임은 부드러운 판매 유도다. 버튼이 튀어 오르는 대신, 링크 화살표가 살짝 밀리고, headline 단어가 순서대로 들어오며, 영상이 정서를 책임진다. shadow는 chrome의 주연이 아니다. 깊이는 카드 그림자보다 영상의 암부와 흰 UI의 대비에서 만들어진다.

### Key Characteristics

- Full-bleed cinematic hero: dark merchant video/photo treatment under white navigation and white display type.
- Shopify green is not painted everywhere: #008060 is the brand anchor, while #061A1C and #02090A carry the current homepage mood.
- Pill CTAs are the main chrome: radius `9999px`, compact vertical padding, high contrast dark/light state pairs.
- Display type is thin and oversized: ShopifySans around 300/330, tracking down to `-0.025em`.
- Body copy is not default 400: page-level body uses 420 or related token aliases.
- Tailwind v4 signatures are visible: `--spacing: .25rem`, `--color-*`, `@media (width>=...)`, utility-heavy HTML.
- Motion is guided by transition opacity/transform and arrow masks, not playful spring physics.
- Neutral palette is zinc-like and cool: #F4F4F5, #D4D4D8, #A1A1AA, #71717A, #3F3F46.
- Dark hero navigation has almost no visible container: white logo/links float over media.
- The site sells commerce scale through editorial imagery, not through a dense dashboard preview.

---

### 🤖 Direction Summary (Machine Interface - DO NOT EDIT)

> **BOLD Direction**: Commerce Cinematic
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **dark creator-film hero over a commerce platform chassis**으로 기억된다.
> **Code Complexity**: high — Tailwind v4 utilities, video/image hero treatment, word reveal transitions, button state matrices, and responsive breakpoint variants are all present.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Shopify처럼 만들기 - 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "ShopifySans", "Inter-Variable", Helvetica, Arial, sans-serif;
  font-weight: 420;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #061A1C; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #008060; --accent-mint: #36F4A4; }
```

**절대 하지 말아야 할 것 하나**: Shopify를 "초록색 SaaS 카드 랜딩"으로 만들지 말 것. 첫 화면의 핵심은 #008060 면적이 아니라, 어두운 영상 배경 위의 거대한 얇은 흰 타이포와 pill CTA다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.shopify.com` |
| Fetched | 2026-04-20T20:00:00+09:00 |
| Extractor | reused phase1 artifacts from `insane-design/shopify` |
| HTML size | 615274 bytes |
| CSS files | 1 external CSS file, 248103 bytes |
| Phase1 JSON | `brand_candidates.json`, `resolved_tokens.json`, `typography.json`, `alias_layer.json` |
| Token prefix | `shopify` (report alias), native CSS uses Tailwind and unprefixed Shopify custom vars |
| Method | CSS custom properties, frequency candidates, hero screenshot, and homepage HTML structure |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Remix/React style rendered commerce marketing page, with large embedded hydration payload and component metadata.
- **Design system**: Shopify marketing system over Tailwind v4 utility theme, custom fonts, and component utility classes.
- **CSS architecture**:
  ```css
  Tailwind theme     (--color-*, --text-*, --radius-*, --spacing) base utilities
  Shopify tokens     (--font-size-dsp, --space-*, --header-height) page primitives
  Component classes  (.bg-button-*, .text-button-*, .rounded-button) stateful UI variants
  ```
- **Class naming**: utility-first HTML with semantic component utility names for buttons, inputs, navigation, grid, and richtext.
- **Default theme**: mixed. Hero/navigation are dark over media; many downstream sections and cards use white or soft neutral surfaces.
- **Font loading**: `@font-face` for ShopifySans, IBMPlexMono, PolySans, Trap, FeatureDisplay, GoodSans, GTSuperDisplay, Noto Sans JP, and campaign fonts.
- **Canonical anchor**: homepage hero screenshot, title `Shopify: The All-in-One Commerce Platform for Businesses - Shopify`, and CTA `Start for free`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `ShopifySans` (Shopify-owned/site bundled)
- **Body font**: `ShopifySans`, with `Inter-Variable`, Helvetica, Arial fallbacks in parts of the CSS.
- **Code font**: `IBMPlexMono`
- **Weight normal / bold**: `420` / `550` for core marketing copy; display often uses `300` or `330`.

```css
:root {
  --shopify-font-family:       ShopifySans, "Inter-Variable", Helvetica, Arial, sans-serif;
  --shopify-font-family-code:  IBMPlexMono, ui-monospace, SFMono-Regular, Menlo, monospace;
  --shopify-font-weight-normal: 420;
  --shopify-font-weight-bold:   550;
}
body {
  font-family: var(--shopify-font-family);
  font-weight: var(--shopify-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **ShopifySans** is the identity font. If unavailable, use **Inter Variable** only with optical correction: body at `420`, button/link at `550`, display at `330`.
- Do not substitute with default `system-ui` at 400/700. Shopify's headings depend on low-weight display mass, not heavy SaaS headline contrast.
- For the hero H1, set `letter-spacing: -0.025em` at very large sizes if using Inter. ShopifySans appears tighter and lighter than generic browser sans defaults.
- For mono labels or technical content, **IBM Plex Mono** is closer than SF Mono because the CSS explicitly includes `IBMPlexMono` weights 300-600.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `--font-size-dsp` | `6rem` | `300` | `6.48rem` | `-0.025em` |
| `--font-size-dsp` alternate | `4.375rem` | `330` | `4.725rem` | `-0.015em` |
| `--font-size-t1` | `3.375rem` | `330` | `3.645rem` | `-0.005em` |
| `--font-size-t2` | `3rem` | `330` | `3.3rem` | `-0.005em` |
| `--font-size-t3` | `2.25rem` | `330` | `2.52rem` | `-0.005em` |
| `--font-size-t4` | `1.875rem` | `330` | `2.1375rem` | `0` |
| `--font-size-t5` | `1.625rem` | `360` | `1.95rem` | `-0.01em` |
| `--font-size-t6` | `1.375rem` | `400` | `1.65rem` | `-0.005em` |
| `--font-size-t7` | `1.125rem` | `450` | `1.4625rem` | `-0.005em` |
| `--font-size-body-lg` | `1.125rem` | `400` | `1.575rem` | `0` |
| `--font-size-body-base` | `1rem` | `420` | `1.4rem` | `-0.006em` |
| `--font-size-body-sm` | `.875rem` | `420` | `1.1375rem` | `0` |
| `--font-size-button-lg` | `1.125rem` | inherited button weight | `1.75rem` | `0` |

> ⚠️ Shopify's visible signature is not a unique size ladder alone. It is the pairing of huge low-weight display type, 420 body weight, and pill CTA text that feels heavier than the headline.

### Principles
<!-- SOURCE: manual -->

1. Display weight stays unusually light. At hero scale, Shopify uses 300/330 instead of the 600/700 SaaS default.
2. Body weight is deliberately firmer than 400 in key tokens. `420` gives copy a commercial solidity without turning it into bold.
3. Letter-spacing correction appears only where size demands it. Display can reach `-0.025em`; small body text often returns to `0`.
4. Button text is part of the brand voice. It is not tiny utility text; 1rem to 1.125rem button sizing makes the CTA feel like a product control.
5. The font inventory is campaign-rich, but the homepage system should not randomly mix all loaded families. ShopifySans is the default spine.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (observed anchors)

| Token | Hex |
|---|---|
| `{colors.primary}` | `#008060` |
| `{colors.accent-mint}` | `#36F4A4` |
| `{colors.accent-cyan}` | `#30DEEE` |
| `svg-start-green` | `#00E392` |
| `svg-start-cyan` | `#00B4CD` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `{colors.hero-ink}` | `#061A1C` |
| `{colors.rich-black}` | `#02090A` |
| `deep-green` | `#061A1C` |
| `deep-pine` | `#041E18` |
| `medium-green` | `#072720` |
| `deep-navy` | `#000A1E` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 10 | `#F4F4F5` | `#18181B` |
| 20 | `#E4E4E7` | `#02090A` |
| 30 | `#D4D4D8` | `#061A1C` |
| 40 | `#A1A1AA` | `#121C1E` |
| 50 | `#71717A` | `#1C2C30` |
| 60 | `#52525B` | `#3F3F46` |
| 100 | `#000000` | `#FFFFFF` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Shopify green | brand anchor | `#008060` |
| Mint | active/graphic accent | `#36F4A4` |
| Cyan | gradient/SVG accent | `#30DEEE` |
| Purple link focus | outline/link focus | `#751BE9` |
| Campaign purple | illustration/SVG | `#6B26FF` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--color-rich-black` | `#02090A` | dark section background |
| `--color-white` | `#FFFFFF` | inverse text, dark primary button background |
| `--color-black` | `#000000` | light primary button background, text |
| `--color-link-dark` | `#9797A2` | dark-surface link default |
| `--color-link-dark-hover` | `#D4D4D8` | dark-surface link hover |
| `--color-link-dark-active` | `#A1A1AA` | dark-surface link active |
| `--color-link-dark-disabled` | `#71717A` | disabled link |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `.bg-button-dark-primary-bg` | `#FFFFFF` | primary CTA on dark hero |
| `.text-button-dark-primary-text` | `#000000` | primary CTA text on dark hero |
| `.hover:bg-button-dark-primary-bg-hover` | `#D4D4D8` | dark primary hover |
| `.active:bg-button-dark-primary-bg-active` | `#A1A1AA` | dark primary active |
| `.disabled:bg-button-dark-primary-bg-disabled` | `#52525B` | disabled primary on dark |
| `.bg-button-light-primary-bg` | `#000000` | primary CTA on light surfaces |
| `.hover:bg-button-light-primary-bg-hover` | `#3F3F46` | light primary hover |
| `.active:bg-button-light-primary-bg-active` | `#71717A` | light primary active |
| `.bg-input-dark-bg` | `#FFFFFF26` | translucent email input on hero |
| `.bg-section-light-bg` | `#FFFFFF` | light sections |
| `.bg-section-dark-bg` | `#02090A` | dark sections |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| transparent | `#00000000` | 105 |
| white | `#FFFFFF` | 47 |
| hero/deep green | `#061A1C` | 41 |
| black | `#000000` | 26 |
| zinc 40 | `#A1A1AA` | 22 |
| mint accent | `#36F4A4` | 21 |
| dark green-gray | `#121C1E` | 20 |
| soft neutral | `#F4F4F5` | 18 |
| rich black | `#02090A` | 17 |
| hairline | `#D4D4D8` | 17 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.hero-ink}` (`#061A1C`)** - The current homepage mood color. It reads as almost black, but its green undertone keeps the hero in Shopify territory instead of generic cinema black. Use it for full-bleed dark bands and video overlays, not for tiny text.

**`{colors.surface-light}` (`#FFFFFF`)** - The hero's most important UI color. White is the logo, nav, H1, input outline, and dark-surface primary button. On Shopify, white is not a background default in the hero; it is the active commercial layer.

**`{colors.primary}` (`#008060`)** - The canonical commerce green. It should be used as a brand/action reference and in secondary system accents, but not as a large hero wash on this homepage style.

**`{colors.accent-mint}` (`#36F4A4`)** - The electric edge of the palette. It appears as graphic/gradient energy and should stay sparse. Overuse turns Shopify into neon fintech, which the current page avoids.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `--spacing` | `.25rem` | Tailwind v4 base unit |
| `--space-xs` | `.5rem` | tight internal gaps |
| `--space-sm` | `1rem` | mobile/component gap |
| `--space-md` | `1.5rem` | component rhythm |
| `--space-lg` | `2rem` | card/section interior |
| `--space-xl` | `2.5rem` | larger stack spacing |
| `--space-2xl` | `4rem` | section top/bottom |
| `--space-3xl` | `5rem` | large section rhythm |
| `--space-4xl` | `8rem` | major band separation |
| `--space-5xl` | `10rem` | editorial vertical breath |
| `--header-height` | `4.5rem` | top navigation height |
| `--gutter` | `1.5rem` desktop | grid/container gutter |
| `--margin` | `5.625rem` wide desktop | outer page margin |

**주요 alias**:
- `px-button-px` -> `1.25rem` (default pill horizontal padding)
- `py-button-py` -> `.5rem` (default pill vertical padding)
- `px-margin` -> `var(--margin)` (outer container alignment)
- `px-gutter` -> `var(--gutter)` (grid gutters)

### Whitespace Philosophy
<!-- SOURCE: manual -->

Shopify uses whitespace as a scale switch. The hero is not packed with feature proof; it leaves the merchant image and huge display line enough room to feel like a brand film. The CTA is compact, but the surrounding field is wide and dark, so the button feels decisive rather than crowded.

Below the hero, the system compresses into commerce density. `container` can stretch to `1600px`, gutters increase at desktop, and grid/card patterns hold many merchant examples. The important rhythm is "cinematic opening, operational grid after." If every section gets the same airy hero spacing, the page loses the platform proof.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `--radius-md` | `.375rem` | small controls, Tailwind default medium |
| `--radius-lg` | `.5rem` | cards or moderate containers |
| `--radius-xl` | `.75rem` | larger media/cards |
| `--radius-2xl` | `1rem` | large rounded panels |
| `.rounded-button` | `9999px` | all major CTA pills |
| `.rounded-full` | very large/full | circular/toggle/icon shapes |
| `.rounded-t-[20px]` | `20px` | special top media or panel corners |
| `.rounded-t-4xl` | `2rem` | oversized editorial panel tops |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| translucent ring | `#FFFFFF80` or tokenized ring color | hero input/button borders on dark media |
| soft overlay | `#0000001A` | subtle dark separators/shadows |
| medium overlay | `#00000033` | media overlays and depth |
| dark surface separation | color contrast over `#02090A`/`#061A1C` | navigation and hero chrome rely more on contrast than elevation |
| card elevation | measured as sparse in extracted snippets | downstream commerce examples likely use image/card separation rather than heavy SaaS shadows |

> Shopify's first screen is not a shadow-heavy UI. Depth comes from video/image texture, black-green overlay, white chrome, and pill silhouettes.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token / Pattern | Value | Usage |
|---|---|---|
| `--default-transition-duration` | `.15s` | base utility transitions |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | default in/out |
| `.arrow-animation:after` | `opacity .12s, transform .3s cubic-bezier(.66,0,.34,1)` | link arrow reveal |
| heading word reveal | `duration-[0.45s]`, delayed per word | hero headline entrance |
| menu icon transition | `duration-500 ease-out-in` | mobile hamburger lines |
| reduced motion | `prefers-reduced-motion: reduce` branches | disables/reduces transitions |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `1600px` container ceiling, with `max-width: calc(1600px - (var(--margin)*2))` at wide viewports.
- **Grid type**: CSS Grid and Flexbox utilities.
- **Column count**: dev grid tokens show 4, 8, and 12 column patterns; desktop content commonly uses 12-column logic.
- **Gutter**: `1rem` base, `1.5rem` desktop.

### Hero
- **Pattern Summary**: `near-100vh + full-bleed merchant video/image + left oversized H1 + email/pill CTA + secondary video link`.
- Layout: left-aligned text block over full-bleed media. Navigation floats at the top; CTA input/button sits below the subhead.
- Background: dark creator close-up media with black/green-brown visual tone.
- **Background Treatment**: image/video overlay, not a generated gradient mesh. The screenshot shows a human face close-up, heavy shadow, and dark warm-green tint.
- H1: approximately `6rem` display on desktop, weight `300`, tracking down to `-0.025em`.
- Max-width: headline occupies roughly half the desktop viewport; subhead narrows to a smaller column.

### Section Rhythm

```css
section {
  padding-block: var(--space-3xl) var(--space-4xl);
  padding-inline: var(--margin);
  max-width: calc(1600px - (var(--margin) * 2));
}
```

### Card Patterns
- **Card background**: `#FFFFFF`, `#F4F4F5`, or dark surfaces depending on band.
- **Card border**: neutral hairlines such as `#D4D4D8` on light surfaces; dark hero controls use translucent white.
- **Card radius**: `.75rem`, `1rem`, or special `20px`/`2rem` top radii for media panels.
- **Card padding**: `1.5rem` to `2rem` typical; larger editorial bands can reach `4rem+`.
- **Card shadow**: secondary to media contrast; avoid generic multi-layer SaaS elevation unless explicitly visible in a downstream card.

### Navigation Structure
- **Type**: horizontal desktop nav with dropdown labels; mobile hamburger at small widths.
- **Position**: top hero overlay, visually fixed/sticky-like in first viewport but extracted CSS does not prove persistent sticky behavior.
- **Height**: `4.5rem`.
- **Background**: transparent over dark media in the hero.
- **Border**: none visible on hero; contrast is handled with white text/logo.

### Content Width
- **Prose max-width**: hero subhead around one quarter desktop width in observed classes.
- **Container max-width**: `1600px` wide ceiling.
- **Sidebar width**: not a primary homepage structure; no persistent sidebar observed.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | `320px` | smallest container floor |
| Small | `640px` | small layout utilities and container step |
| Tablet | `768px` | tablet container step |
| Nav/Desktop | `900px` | major layout/navigation switch appears repeatedly |
| Desktop | `1200px` | larger grids and desktop rhythm |
| Wide | `1600px` | max container locks to wide canvas |

### Touch Targets
- **Minimum tap size**: mobile menu button uses `h-12 w-12`, i.e. 48px square.
- **Button height (mobile)**: pill CTA uses `py-2`/`py-button-py` plus 1rem text, close to 40-44px depending line-height.
- **Input height (mobile)**: email input appears as pill field paired with CTA; exact computed height not captured, but screenshot shows a tall pill control.

### Collapsing Strategy
- **Navigation**: desktop links and nav groups collapse to `Start for free` link plus hamburger under large breakpoint.
- **Grid columns**: utility classes imply 4/8/12 column progression and `grid-cols` variants.
- **Sidebar**: no persistent sidebar in homepage.
- **Hero layout**: text remains over media; CTA row stacks or wraps via `flex-col`, `sm:flex-row`, and `flex-wrap`.

### Image Behavior
- **Strategy**: full-bleed hero media plus responsive commerce images.
- **Max-width**: utility-driven `w-full`, container constraints, and aspect-ratio classes.
- **Aspect ratio handling**: many explicit `aspect-[...]` utilities, including `26/17`, `600/389`, `800/625`, and square.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Dark Primary Button**

| Property | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#000000` |
| Border | transparent |
| Radius | `9999px` |
| Padding | `.5rem 1.25rem`, larger at desktop |
| Hover | background `#D4D4D8` |
| Active | background `#A1A1AA` |
| Disabled | background `#52525B` |

```html
<a class="rounded-button px-button-px py-button-py bg-button-dark-primary-bg text-button-dark-primary-text">
  Start for free
</a>
```

**Light Primary Button**

| Property | Value |
|---|---|
| Background | `#000000` |
| Text | `#FFFFFF` |
| Border | transparent |
| Radius | `9999px` |
| Hover | background `#3F3F46` |
| Active | background `#71717A` |
| Disabled | background `#D4D4D8` |

### Badges

Shopify's extracted homepage CSS contains tag and shade utilities such as `.bg-tag-shade`, but the hero's visible badge language is minimal. Use badges sparingly and keep them pill-shaped, neutral, and text-led.

| Property | Value |
|---|---|
| Background | `#1B1B1F` on dark or `#F4F4F5` on light |
| Text | `#FFFFFF` dark / `#000000` light |
| Radius | `9999px` |
| Padding | `2px 8px` to `6px 12px` |
| Weight | 450-550 |

### Cards & Containers

Cards are secondary to media. Use the card system to frame merchant examples, platform proof, or content clusters. Avoid generic feature cards with icons unless the source section clearly uses them.

| Property | Value |
|---|---|
| Background | `#FFFFFF`, `#F4F4F5`, or `#02090A` |
| Border | `1px solid #D4D4D8` on light, translucent white on dark |
| Radius | `.75rem`, `1rem`, `20px`, or `2rem` for large panels |
| Padding | `1.5rem` to `2rem` |
| Hover | subtle link/arrow movement or color shift, not dramatic lift |

### Navigation

Desktop navigation is white-on-media in the hero:

- left Shopify logo
- middle dropdown labels such as `Why Shopify`, `Products`, `Pricing`, `Enterprise`
- right `Log in` and pill `Start for free`
- mobile `Start for free` text link plus 48px hamburger button

```html
<nav class="h-[var(--header-height)] text-white">
  <a>Why Shopify</a>
  <a>Products</a>
  <a>Pricing</a>
  <a>Enterprise</a>
  <a class="rounded-button bg-button-dark-primary-bg text-button-dark-primary-text">Start for free</a>
</nav>
```

### Inputs & Forms

The hero email form is a dark translucent pill paired with a white pill button.

| Property | Value |
|---|---|
| Background | `#FFFFFF26` |
| Text | `#FFFFFF` |
| Border/Ring | translucent white, e.g. `#FFFFFF80` |
| Radius | `9999px` |
| Layout | input and CTA visually share one capsule row on desktop |
| Disclaimer | small muted white text above/near input |

### Hero Section

The hero component is the signature surface:

- full viewport media background
- transparent white navigation
- large left-aligned display headline
- subhead `Dream big, build fast, and grow far on Shopify.`
- email field and `Start for free`
- secondary video link `Why we build Shopify`

### 13-2. Named Variants
<!-- SOURCE: manual -->

**button-dark-primary** - White pill used over dark hero media. This is the first viewport CTA and must remain high contrast.

**button-light-primary** - Black pill for light sections. Same radius language, reversed contrast.

**button-dark-secondary** - Transparent dark-surface secondary action with white border/text. Use when CTA hierarchy needs a second action without adding another brand color.

**email-hero-pill** - Dark translucent input capsule with white type and an embedded/adjacent white primary button.

**nav-hero-transparent** - White nav text and logo over media, no visible nav card, no bottom border.

**arrow-link** - Text link with masked arrow pseudo-element that translates on hover.

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
cinematic-merchant-film-hero:
  description: "Full-bleed merchant media turns SaaS marketing into a founder documentary opening."
  technique: "transparent white nav over dark video/photo, #FFFFFF H1, {colors.hero-ink}/{colors.rich-black} mood, 6rem low-weight display, lower-left CTA cluster"
  applied_to: ["{component.nav-hero-transparent}", "{component.homepage-hero}", "{component.arrow-link}"]
  visual_signature: "The page feels like a commerce movement before it feels like a software product."

low-weight-shopify-display-pressure:
  description: "Huge type stays wide and emotional without becoming enterprise-heavy."
  technique: "--font-size-dsp: 6rem; font-weight: 300/330; line-height: 6.48rem; letter-spacing: -0.025em"
  applied_to: ["{component.homepage-hero}", "{component.large-editorial-heading}"]
  visual_signature: "Large words land like film titles, not bold SaaS billboards."

inverted-pill-commerce-control:
  description: "Primary actions read as compact commerce controls rather than brand-colored buttons."
  technique: "border-radius: 9999px; padding: 8px 20px; #FFFFFF button on dark with #000000 text; #000000 button on light with #FFFFFF text; hover through #D4D4D8/#3F3F46"
  applied_to: ["{component.button-dark-primary}", "{component.button-light-primary}", "{component.pricing-action}"]
  visual_signature: "A checkout-like capsule appears without showing an actual checkout UI."

translucent-email-capsule-on-film:
  description: "The hero form is visible enough to act, but translucent enough to stay inside the film frame."
  technique: "background: #FFFFFF26; border/ring: #FFFFFF80; color: #FFFFFF; border-radius: 9999px; paired with white primary pill"
  applied_to: ["{component.email-hero-pill}", "{component.input-dark-email}", "{component.button-dark-primary}"]
  visual_signature: "The signup field feels like a card reader placed on a dark studio counter."

arrow-mask-commerce-momentum:
  description: "Secondary links imply forward motion through an arrow reveal, not through button lift."
  technique: "pseudo-element mask arrow; opacity .12s; transform .3s cubic-bezier(.66,0,.34,1); translate by one spacing unit"
  applied_to: ["{component.arrow-link}", "{component.video-cta}", "{component.content-cta}"]
  visual_signature: "The page nudges the visitor forward with a sales-floor gesture instead of playful bounce."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | direct creator/business ambition, short words, large emotional claim | "Be the next category creator" |
| Subhead | three-part verb rhythm | "Dream big, build fast, and grow far on Shopify." |
| Primary CTA | action begins immediately, no enterprise jargon | "Start for free" |
| Secondary CTA | proof/explanation framed as story | "Why we build Shopify" |
| Tone | ambitious, founder-facing, commerce-native | "The one commerce platform behind it all" |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Shopify-inspired homepage tokens */
:root {
  /* Fonts */
  --shopify-font-family:       ShopifySans, "Inter-Variable", Helvetica, Arial, sans-serif;
  --shopify-font-family-code:  IBMPlexMono, ui-monospace, SFMono-Regular, Menlo, monospace;
  --shopify-font-weight-normal: 420;
  --shopify-font-weight-bold:   550;

  /* Brand and dark hero */
  --shopify-color-brand-25:  #D4F9E0;
  --shopify-color-brand-300: #36F4A4;
  --shopify-color-brand-500: #008060;
  --shopify-color-brand-600: #061A1C;
  --shopify-color-brand-900: #02090A;

  /* Surfaces */
  --shopify-bg-page:   #FFFFFF;
  --shopify-bg-hero:   #061A1C;
  --shopify-bg-dark:   #02090A;
  --shopify-text:      #000000;
  --shopify-text-inverse: #FFFFFF;
  --shopify-text-muted:#71717A;
  --shopify-border:    #D4D4D8;

  /* Key spacing */
  --shopify-space-sm:  1rem;
  --shopify-space-md:  1.5rem;
  --shopify-space-lg:  2rem;
  --shopify-space-xl:  2.5rem;
  --shopify-space-section: 5rem;

  /* Radius */
  --shopify-radius-sm: .375rem;
  --shopify-radius-md: .75rem;
  --shopify-radius-lg: 1rem;
  --shopify-radius-pill: 9999px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js - Shopify-inspired extraction
module.exports = {
  theme: {
    extend: {
      colors: {
        shopify: {
          green: '#008060',
          mint: '#36F4A4',
          cyan: '#30DEEE',
          hero: '#061A1C',
          black: '#02090A',
        },
        shade: {
          10: '#F4F4F5',
          20: '#E4E4E7',
          30: '#D4D4D8',
          40: '#A1A1AA',
          50: '#71717A',
          60: '#52525B',
          70: '#3F3F46',
          90: '#18181B',
        },
      },
      fontFamily: {
        sans: ['ShopifySans', 'Inter-Variable', 'Helvetica', 'Arial', 'sans-serif'],
        mono: ['IBMPlexMono', 'ui-monospace', 'SFMono-Regular', 'monospace'],
      },
      fontWeight: {
        normal: '420',
        display: '330',
        cta: '550',
      },
      borderRadius: {
        button: '9999px',
        md: '.375rem',
        lg: '.5rem',
        xl: '.75rem',
        '2xl': '1rem',
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
| Brand primary | `{colors.primary}` | `#008060` |
| Hero background | `{colors.hero-ink}` | `#061A1C` |
| Dark background | `{colors.rich-black}` | `#02090A` |
| Background | `{colors.surface-light}` | `#FFFFFF` |
| Text primary | `{colors.text-primary}` | `#000000` |
| Text inverse | `{colors.text-inverse}` | `#FFFFFF` |
| Text muted | `{colors.text-muted}` | `#71717A` |
| Border | `{colors.hairline}` | `#D4D4D8` |
| Accent | `{colors.accent-mint}` | `#36F4A4` |

### Example Component Prompts

#### Hero Section

```text
Shopify 스타일 히어로 섹션을 만들어줘.
- 배경: full-bleed merchant video/photo with dark overlay, base #061A1C
- H1: ShopifySans, clamp to desktop 6rem, weight 300, line-height 1.08, tracking -0.025em
- 서브텍스트: #FFFFFF, 1.125rem, weight 400, short three-part verb rhythm
- CTA: email pill with #FFFFFF26 input and #FFFFFF primary button
- 네비게이션: transparent, white logo/text, height 4.5rem, no card background
- 최대 너비: 1600px container, desktop margin about 5.625rem
```

#### Card Component

```text
Shopify 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF or #F4F4F5, not a saturated green card
- border: 1px solid #D4D4D8 when structure is needed
- radius: 0.75rem to 1rem; media panels can use 20px or 2rem top radius
- padding: 1.5rem to 2rem
- hover: subtle arrow or text color motion, no large lift
- 제목: ShopifySans, weight 330-420 depending size
- 본문: ShopifySans, 1rem, weight 420, line-height 1.4
```

#### Badge

```text
Shopify 스타일 배지를 만들어줘.
- font: ShopifySans, 12-14px, weight 450-550
- padding: 2px 8px or 6px 12px
- radius: 9999px
- dark version: bg #1B1B1F, text #FFFFFF
- light version: bg #F4F4F5, text #000000
- brand green is allowed only as a small signal, not the entire component language
```

#### Navigation

```text
Shopify 스타일 상단 네비게이션을 만들어줘.
- 높이: 4.5rem
- 배경: transparent over dark media
- 링크: ShopifySans, 16px, white, weight 420-500
- 좌측 Shopify logo, 중앙 dropdown nav, 우측 Log in + Start for free
- CTA 버튼: white pill, black text, radius 9999px, hover #D4D4D8
- 모바일: Start for free text link + 48px hamburger
```

### Iteration Guide

- **색상 변경 시**: dark hero는 #061A1C 또는 #02090A를 기준으로 잡고, #008060은 작은 브랜드 신호로만 사용한다.
- **폰트 변경 시**: display 300/330과 body 420을 유지한다. 일반 400/700 조합 금지.
- **여백 조정 시**: 4px Tailwind base에서 출발하되, 큰 섹션은 5rem/8rem/10rem 스케일로 과감하게 띄운다.
- **새 컴포넌트 추가 시**: pill radius와 neutral state matrix를 재사용한다.
- **다크 모드**: light token에 opacity를 씌워 대충 만들지 말고, hero/dark surfaces는 #061A1C, #02090A 계열로 분리한다.
- **반응형**: 900px 전후를 nav/layout 전환점으로 보고, 1600px에서 container를 잠근다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use a cinematic dark hero with real merchant/product media and white type.
- Keep Shopify green sparse: #008060 is a brand/action anchor, not a full-page wash.
- Use ShopifySans-like low display weights: 300/330 for large headings, 420 for body.
- Build primary CTAs as pill controls with `border-radius: 9999px`.
- Pair dark hero controls with #FFFFFF surfaces and #000000 text.
- Preserve Tailwind v4 rhythm: 4px base unit, breakpoint utilities, and explicit aspect-ratio media.
- Use subtle arrow/link micro-motion instead of bouncing button animation.
- Let downstream sections become denser and more platform-like after the cinematic hero.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로만 두고 hero를 만들지 말 것 - 대신 hero는 `#061A1C` 또는 실제 dark media overlay를 사용.
- hero 텍스트를 `#000000` 또는 `black`으로 두지 말 것 - 대신 dark hero에서는 `#FFFFFF` 사용.
- Shopify 브랜드를 `#00FF00` 같은 neon green으로 대체하지 말 것 - canonical action anchor는 `#008060`, electric accent는 `#36F4A4`.
- 본문 텍스트를 전부 `font-weight: 400`으로 두지 말 것 - Shopify body token은 `420` 계열이 핵심.
- display heading을 `font-weight: 700` 또는 `800`으로 만들지 말 것 - hero display는 `300` 또는 `330`에 가깝다.
- CTA radius를 `8px` 또는 `12px` 카드 버튼처럼 만들지 말 것 - primary CTA는 `9999px` pill.
- dark primary CTA 배경을 `#008060`으로 칠하지 말 것 - hero primary button은 `#FFFFFF` 배경과 `#000000` 텍스트가 맞다.
- hover를 큰 `transform: translateY(-8px)` 카드 리프트로 만들지 말 것 - 링크/버튼 상태는 neutral color shift와 작은 arrow motion 중심.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)
<!-- SOURCE: manual -->

- **No green hero wash**: Shopify green is present, but the first viewport is not a green gradient or flat green panel.
- **No dashboard-first framing**: the homepage does not open with admin UI screenshots or analytics cards.
- **No heavy display weight**: 700/800 hero typography would break the current soft cinematic pressure.
- **No boxed nav card**: the hero navigation floats over media; it is not a white rounded navbar capsule.
- **No generic purple-blue AI gradient**: colors like `#667eea` to `#764ba2` are alien to this surface.
- **No equal 3-card SaaS hero**: the first viewport is not "headline + three feature cards"; it is media-led.
- **No second dominant brand color**: mint/cyan accents exist, but they do not become a co-primary palette.
- **No decorative emoji/icon clutter**: commerce proof comes from merchant imagery, not cute symbols.
- **No thick chrome shadows**: hero depth is media and contrast, not elevation stacks around UI cards.
- **No arbitrary font mixing**: many fonts are loaded, but ShopifySans remains the system spine for this page.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **Single homepage surface** - This guide is based on the Shopify homepage artifacts in `insane-design/shopify`, not admin, checkout, app store, pricing checkout, or merchant dashboard flows.
- **Phase1 timestamp** - The reused crawl artifacts are dated 2026-04-20/2026-04-23 locally. The live Shopify homepage may have changed after that date.
- **CSS custom property graph is partial** - `resolved_tokens.json` found 245 vars and 172 resolved values, but many utility classes are Tailwind-generated and not named as a canonical Shopify design-token API.
- **Typography scale extraction was sparse** - `typography.json` did not populate a full `scale` object, so the scale table combines CSS variable inspection with manual interpretation of extracted declarations.
- **Screenshot is desktop hero only** - The visible hero analysis comes from a 1280px-wide cropped screenshot. Mobile visual composition was inferred from CSS classes and breakpoints, not visually re-screenshot.
- **Motion runtime not fully executed** - CSS transition values and HTML classes were inspected, but JS timeline behavior, video loading states, and actual scroll-triggered timing were not measured.
- **Color frequency includes SVG and utility noise** - Some chromatic values come from SVG gradients or illustration assets. The guide separates them from core UI colors, but automatic filtering is not perfect.
- **Form error/loading states not surfaced** - The homepage signup field was visible, but validation, loading, and error states were not exercised.
- **Downstream card details are inferred conservatively** - HTML payload contains many merchant/card assets, but this pass did not inspect every later section visually.
- **No HTML report generated** - Per instruction, Step 6 RENDER-HTML was skipped and only `design.md` was produced.
