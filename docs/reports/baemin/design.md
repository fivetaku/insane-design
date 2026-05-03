---
schema_version: 3.2
slug: baemin
service_name: 배달의민족
site_url: https://www.baemin.com/
fetched_at: 2026-04-14T01:12:00+09:00
default_theme: mixed
brand_color: "#0CEFD3"
primary_font: BAEMINWORK
font_weight_normal: 400
token_prefix: baemin

bold_direction: Food Pop Editorial
aesthetic_category: editorial-product
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high

archetype: editorial-product
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "styled-components class output, BAEMINWORK font, repeated 1240px containers, 600/1024px breakpoints, and consistent teal/photo section choreography are present; named public token tiers are sparse."

colors:
  primary: "#0CEFD3"
  surface-light: "#f6f6f6"
  surface-white: "#FFFFFF"
  surface-dark: "#000000"
  text-primary: "#222222"
  text-inverse: "#FFF"
  text-muted: "#B1B3B5"
  text-subtle: "#7E8082"
  hover-soft: "#f7f7f7"

typography:
  display: "BAEMINWORK"
  body: "-apple-system"
  ladder:
    - { token: hero-title, size: "40px", weight: 800, line_height: "140%", tracking: "-0.04em" }
    - { token: section-display, size: "72px", weight: 800, line_height: "140%", tracking: "-0.04em" }
    - { token: section-title, size: "60px", weight: 800, line_height: "140%", tracking: "-0.04em" }
    - { token: body-large, size: "20px", weight: 600, line_height: "145%", tracking: "-0.1px" }
    - { token: nav-link, size: "16px", weight: 700, line_height: "140%" }
  weights_used: [400, 500, 600, 700, 800]
  weights_absent: [300, 900]

components:
  nav-fixed-transparent: { color: "{colors.text-inverse}", height: "96px", max_width: "1240px" }
  store-button: { bg: "{colors.surface-white}", radius: "12px", size: "152px x 54px" }
  qr-button: { bg: "{colors.surface-white}", hover_bg: "{colors.hover-soft}", radius: "12px" }
  pill-cta: { bg: "{colors.surface-dark}", color: "{colors.text-inverse}", radius: "9999px", height: "58px" }
  teal-section: { bg: "{colors.primary}", container: "1240px", gap: "40px" }
---

# DESIGN.md — 배달의민족 (Designer Guidebook)

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

배달의민족 홈페이지는 "앱 소개 페이지"라기보다 야식 골목 입구에 세워진 거대한 전광 간판에 가깝다. 화면 첫 장에서 음식 사진은 배경이 아니라 매대이고, #0CEFD3 (`{colors.primary}`) 문장은 그 위에 갓 켠 네온처럼 박힌다. 텍스트는 기능을 설명하려고 얹히지 않는다. 닭강정의 윤기, 어두운 조리대, 배달 직전의 속도를 한 번 더 크게 들리게 하는 확성기 역할을 한다.

핵심 색은 하나다. #0CEFD3 (`{colors.primary}`)가 히어로 카피, 다음 섹션의 바닥, 강조 문구를 거의 혼자 맡는다. no second brand color. 팔레트를 풍부하게 만들기 위해 다른 accent를 끌어오지 않고, 사진의 갈색 튀김옷과 #000000 (`{colors.surface-dark}`) 무대, #FFFFFF (`{colors.surface-white}`) 다운로드 버튼이 브랜드 색 주변의 식재료처럼 놓인다. 배민의 컬러 시스템은 여러 잉크를 섞은 포스터가 아니라, 민트 잉크 한 통을 음식 사진 위에 크게 찍는 인쇄물이다.

타이포그래피는 정돈된 SaaS식 계단보다 더 물성 있는 간판 글자다. `BAEMINWORK`는 display에 쓰이고, 큰 문장은 `letter-spacing: -0.04em`으로 꽉 조여 한 덩어리의 스티커처럼 붙는다. 72px까지 올라가는 섹션 display는 읽는 문장이라기보다 가게 셔터에 붙은 대형 시트지에 가깝다. 본문은 system stack으로 조용히 내려가지만, 핵심 문장만큼은 배민 전용 서체가 화면의 목소리를 독점한다.

레이아웃은 스크롤 문서보다 full-screen 음식 광고 릴이다. `body`가 fixed/hidden 계열로 잠기고, 섹션은 `height: 0px`에서 열리며 한 장면씩 무대에 올라온다. 고정 헤더는 흰 종이 메뉴판처럼 사진 위에 얹히되, 별도 바탕을 만들지 않는다. shadow only on photography; UI chrome은 그림자를 거의 쓰지 않고, 깊이는 음식 사진의 조명과 dark overlay가 담당한다.

앱스토어 버튼과 QR 버튼은 CTA 카드가 아니라 사진 위에 붙은 흰 가격표 같은 물건이다. #FFFFFF (`{colors.surface-white}`), 12px radius, 54px height로 실물 라벨처럼 읽히지만, border나 elevation으로 떠오르지는 않는다. 배민답게 세련됨은 "조용한 미니멀"이 아니라 "명확한 과장"에서 나온다. 큰 글자, 한 가지 강한 색, 직접적인 음식 사진, 손에 잡히는 다운로드 라벨. 이 조합이 조금만 흐려져도 배민이 아니라 흔한 배달 앱 랜딩이 된다.

이 사이트는 결국 **푸드 갤러리의 진열장**과 **셔터에 붙은 대형 시트지**가 한 무대 위에 겹쳐진 형태다. full-bleed photography는 쇼룸의 진열장 유리, BAEMINWORK 카피는 그 유리 위에 붙은 전시 라벨이다. white 다운로드 버튼은 갤러리 큐레이터가 옆에 놓아둔 카탈로그 조각, scroll-arrow는 다음 진열실로 안내하는 무대 입구다. 카드 그리드는 카탈로그 책자가 아니라 한 컷씩 넘기는 전시실 패널 — 각 음식 사진이 한 진열장의 주인이 되고, 민트 카피는 그 진열장 안의 조명이다. 박물관 가이드가 외치지 않듯, 텍스트는 작품 옆에 라벨로만 붙는다 — 전시는 페이지가 아니라 장면으로 분절된다.

### Key Characteristics

- #0CEFD3 (`{colors.primary}`) single chromatic brand anchor.
- Full-bleed food photography with dark overlay rather than abstract illustration.
- `BAEMINWORK` display typography with tight `-0.04em` tracking.
- Fixed transparent top navigation, white logo, and external utility links.
- 1240px max-width container repeated across hero and content sections.
- Full-screen scene rhythm: photo section, teal section, black section, teal section.
- Store download buttons are white rounded rectangles, not brand-filled CTAs.
- Primary pill CTA uses black background, white text, and `9999px` radius.
- Sparse component chrome: almost no cards, borders, or decorative shadows.
- Animation is section choreography and scroll arrow motion, not micro-hover flourish.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Food Pop Editorial
> **Aesthetic Category**: editorial-product
> **Signature Element**: 이 사이트는 **큰 민트 카피가 음식 사진 위에 간판처럼 박히는 hero_impact**으로 기억된다.
> **Code Complexity**: high — fixed-body scroll choreography, section reveal animations, image overlays, and responsive scene containers are coupled.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 배달의민족처럼 만들기 — 3가지만 하면 80%

```css
/* 1. display font + tight Korean headline */
@font-face {
  font-family: "BAEMINWORK";
  src: url("/fonts/BAEMINWORK.otf") format("opentype");
  font-display: swap;
}

.hero-title {
  font-family: "BAEMINWORK", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: clamp(32px, 6vw, 72px);
  font-weight: 800;
  line-height: 1.4;
  letter-spacing: -0.04em;
}

/* 2. one chromatic anchor */
:root {
  --baemin-primary: #0CEFD3;
  --baemin-bg: #f6f6f6;
  --baemin-ink: #222222;
}

/* 3. photo-first hero */
.hero {
  color: #FFF;
  background: linear-gradient(90deg, rgba(0,0,0,0.5) 2.52%, rgba(0,0,0,0) 100%), var(--hero-image);
  background-size: cover;
  background-position: center;
}
```

**절대 하지 말아야 할 것 하나**: 히어로를 순백 배경의 중앙정렬 SaaS 랜딩으로 만들지 말 것. 배민의 첫 장면은 음식 사진 + #0CEFD3 대형 카피 + 고정 흰 내비게이션이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.baemin.com/` |
| Fetched | 2026-04-14T01:12:00+09:00 |
| Extractor | existing phase1 reuse: HTML + inline CSS + screenshot |
| HTML size | 75333 bytes |
| CSS files | 1 inline CSS file, 29602 bytes |
| Token prefix | `baemin` |
| Method | phase1 JSON + `_inline.css` + `index.html` + hero screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js-like static output with styled-components class names (`data-styled` CSS, hashed classes such as `.jaUKnG`, `.lnEEkB`, `.eMvtKq`).
- **Design system**: Baemin site-specific system. Only two explicit custom properties were surfaced: `--color-mode-text` and `--color-mode-divider`.
- **CSS architecture**: styled-components output with repeated responsive overrides.
  ```css
  core      (--color-mode-*)             mode-specific text/divider
  hashed    (.jaUKnG, .fHmnqD, .lnEEkB)  component-level generated classes
  sections  (.IntroSection-*, .Section*) full-screen narrative blocks
  ```
- **Class naming**: generated hash classes plus long styled-component display names for section templates.
- **Default theme**: mixed. Body floor is #f6f6f6, hero is dark photographic, content sections switch to #0CEFD3 and #000000.
- **Font loading**: local `@font-face` for `BAEMINWORK` via `/fonts/BAEMINWORK.otf`, `font-display: swap`.
- **Canonical anchor**: #0CEFD3 is the only chromatic brand color in CSS frequency candidates and appears in hero/section emphasis.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `BAEMINWORK` (site-local brand font)
- **Body font**: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, "Helvetica Neue", sans-serif`
- **Code font**: `source-code-pro, Menlo, Monaco, Consolas, "Courier New", monospace`
- **Weight normal / bold**: `400` / `800`

```css
:root {
  --baemin-font-display: "BAEMINWORK";
  --baemin-font-body: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --baemin-font-weight-normal: 400;
  --baemin-font-weight-bold: 800;
}

body {
  font-family: var(--baemin-font-body);
  font-weight: var(--baemin-font-weight-normal);
  background-color: #f6f6f6;
  color: #222222;
}
```

### Note on Font Substitutes

- **BAEMINWORK** is the voice of the site. If unavailable, use a heavy Korean display face with compressed rhythm rather than a neutral Latin-first UI font.
- **Open-source fallback**: `Pretendard` at weight 800 for display, but tighten `letter-spacing` to `-0.04em` and keep `line-height: 1.4`.
- **Do not substitute with plain Inter** for the hero. Inter loses the signboard quality; if Inter must be used, reserve it for utility navigation and body copy only.
- **Body fallback** can remain system UI. The site itself already uses system stack for non-display text.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| `hero-title` | 32px / 40px | 800 | 140% | -0.04em |
| `section-display` | 36px / 56px / 72px | 800 | 140% | -0.04em |
| `section-title` | 32px / 48px / 60px | 800 | 140% | 0 |
| `body-large` | 16px / 18px / 20px | 600 | 145% | -0.1px |
| `nav-link` | 16px | 700 | 140% | 0 |
| `footer-link` | 20px / 24px / 30px | 700 | 130% | 0 |
| `footer-meta` | 11px / 14px | 400 | 140% | 0 |
| `pill-cta` | 17px / 18px | 700 | 140% | 0 |

> ⚠️ Key insight: 배민은 작은 UI 폰트보다 display Korean headline의 압축감이 먼저다. `BAEMINWORK + 800 + -0.04em + 140%` 조합을 놓치면 브랜드 표정이 사라진다.

### Principles

1. Display copy is not merely bigger body text. It switches to `BAEMINWORK` and uses tight `-0.04em` tracking.
2. Large Korean phrases keep generous `140%` line-height even when tracking is tight, so the block feels bold but not cramped.
3. Body/detail copy uses system UI and lower visual personality; hierarchy is created by font family change, not just size.
4. Weight 800 is reserved for billboard-like display. Weight 600 carries explanatory body emphasis. Weight 400 is mostly metadata/detail.
5. There is no thin or elegant typographic mode. The brand voice is heavy, direct, and commercial.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (1 confirmed chromatic step)

| Token | Hex |
|---|---|
| `baemin-primary` | #0CEFD3 |

### 06-2. Brand Dark Variant

> N/A — no separate dark brand ramp was surfaced in the reused CSS. Dark scenes use #000000 plus white/inverse text.

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| Page floor | #f6f6f6 | #000000 |
| Surface | #FFFFFF | #000000 |
| Text primary | #222222 | #FFF |
| Muted text | #7E8082 | #B1B3B5 |
| Hover soft | #f7f7f7 | rgba(0,0,0,0.8) |

### 06-4. Accent Families

> N/A — no secondary chromatic family was found. Do not create one.

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--color-mode-text` | #FFF | Fixed nav and inverse text mode |
| `--color-mode-divider` | rgba(255,255,255,0.3) | Header divider mode |
| `baemin-primary` | #0CEFD3 | Hero headline and teal sections |
| `baemin-body-text` | #222222 | Default input/button/link color |
| `baemin-muted-text` | #B1B3B5 | Footer/detail metadata |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--color-mode-text` | #FFF | Header link/logo in photo/dark mode |
| `--color-mode-divider` | rgba(255,255,255,0.3) | Header separator |

### 06-7. Dominant Colors (실제 CSS 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| `surface-white` | #FFFFFF / #FFF / #fff | 29 combined textual occurrences |
| `surface-dark` | #000000 / #000 | 17 combined textual occurrences |
| `primary` | #0CEFD3 | 5 CSS occurrences, 10 frequency-candidate count |
| `muted-text` | #B1B3B5 | 2 CSS occurrences, 9 frequency-candidate count |
| `page-floor` | #f6f6f6 | 2 CSS occurrences |
| `text-primary` | #222222 | 2 CSS occurrences |

### 06-8. Color Stories

**`{colors.primary}` (#0CEFD3)** — This is not a decorative accent; it is the brand signal. It can become a full section background or giant headline color. Use it loudly, but use it alone.

**`{colors.surface-dark}` (#000000)** — Black is the photographic stage and the contrast partner for teal. It appears in dark sections, carousel indicators, and pill CTA backgrounds.

**`{colors.surface-white}` (#FFFFFF)** — White is for utility surfaces: app-store buttons, QR blocks, inverse logo/link text. It should feel like a small physical label laid on top of food photography.

**`{colors.text-muted}` (#B1B3B5)** — Muted gray belongs to footer and legal/detail copy. It should not compete with the teal headline system.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `container-max` | 1240px | Header, hero, section content |
| `image-stage-max` | 1440px | Full-screen background/image stage |
| `nav-height-mobile` | 80px | Small viewport fixed header |
| `nav-height-tablet` | 88px | Medium viewport fixed header |
| `nav-height-desktop` | 96px | Desktop fixed header |
| `section-padding-mobile` | 48px 20px | Mobile content sections |
| `section-padding-tablet` | 0 32px | Tablet sections |
| `section-padding-desktop` | 0 56px | Desktop sections |
| `hero-padding-desktop` | 120px 55px | Desktop hero content |
| `scene-gap-mobile` | 40px | Mobile hero/section vertical gap |
| `scene-gap-tablet` | 64px | Tablet hero/section vertical gap |
| `scene-gap-desktop` | 80px | Desktop hero/section vertical gap |
| `content-gap-desktop` | 40px | Intro/section content gap |

**주요 alias**:
- `container-max` → 1240px (brand stage width)
- `scene-gap-desktop` → 80px (headline to controls/content rhythm)
- `section-padding-desktop` → 0 56px (desktop side safety)

### Whitespace Philosophy

배민의 여백은 "프리미엄한 침묵"이 아니라 화면 장면을 안전하게 읽히게 하는 완충재다. 사진은 화면 전체를 차지하고, 카피는 좌측에서 크게 들어오며, 버튼은 하단 가까이에 놓인다. 그래서 컨테이너는 1240px로 넓지만 좌우 padding은 desktop에서 56px로 꽤 명확하다.

섹션 간 리듬은 카드 그리드의 조밀함이 아니라 full-screen 장면 전환에서 생긴다. gap 40/64/80px 계단은 정보 간 거리라기보다 무대 위 배우 사이의 거리다. 텍스트와 이미지가 같은 화면에서 겹치지 않게, 한 장면씩 소비되게 만드는 spacing이다.

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---:|---|
| `radius-store-button` | 12px | App Store / Google Play buttons |
| `radius-qr-button` | 12px | QR utility button |
| `radius-tooltip` | 16px | Dark tooltip/dropdown container |
| `radius-pill` | 9999px | Black primary pill CTA |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| Level | Value | Usage |
|---|---|---|
| `shadow-none` | none observed for chrome | Main buttons and containers rely on surface contrast |
| `photo-depth` | photographic only | Depth comes from image lighting, not CSS elevation |

> Pattern: 배민은 UI chrome에 multi-layer shadow를 만들지 않는다. 사진 자체의 명암과 full-screen overlay가 깊이를 맡는다.

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `zoom-in` | 1s linear forwards | Intro background image reveal |
| `scroll-float` | 2s ease-in-out infinite | Fixed bottom scroll arrow |
| `bike` | 0.8s ease forwards | Tada section bike animation |
| `section-reveal` | height/overflow choreography | Sections start at `height: 0px` and open into scenes |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System

- **Content max-width**: 1240px
- **Image/stage max-width**: 1440px
- **Grid type**: Flexbox-driven scene layout; no explicit CSS grid token was found.
- **Column count**: single scene column with positioned image/photo layers; some flex blocks use column direction.
- **Gutter**: 40px mobile, 64px tablet, 80px desktop for major scene gaps.

### Hero

- **Pattern Summary**: full-screen photographic hero + fixed white nav + left-aligned #0CEFD3 display headline + app download controls.
- Layout: left editorial copy over full-bleed food image.
- Background: real food photography from `_next/static/media/main_05...jpeg` and related hero assets.
- **Background Treatment**: image-overlay using `linear-gradient(90deg, rgba(0,0,0,0.5) 2.52%, rgba(0,0,0,0) 100%)` on desktop; vertical gradient appears in base rule.
- H1: `BAEMINWORK`, 32/40px in CSS extraction for the active hero copy; section display reaches 72px.
- Max-width: 1240px content, 1440px image stage.

### Section Rhythm

```css
.section-content {
  max-width: 1240px;
  padding: 48px 20px;
  gap: 20px;
}

@media (min-width: 600px) {
  .section-content {
    padding: 0 32px;
    gap: 32px;
  }
}

@media (min-width: 1024px) {
  .section-content {
    padding: 0 56px;
    gap: 40px;
  }
}
```

### Card Patterns

- **Card background**: #FFFFFF for store/QR utilities only.
- **Card border**: none.
- **Card radius**: 12px for app-store and QR blocks.
- **Card padding**: app-store button uses 14px 19px; QR/utility uses centered flex.
- **Card shadow**: none observed.
- **Hover**: QR utility changes background to #f7f7f7.

### Navigation Structure

- **Type**: horizontal fixed top navigation.
- **Position**: `position: fixed; top: 0; left: 50%; transform: translateX(-50%)`.
- **Height**: 80px mobile, 88px tablet, 96px desktop.
- **Background**: transparent over hero/dark photography.
- **Text**: #FFF via `--color-mode-text`.
- **Border/divider**: `rgba(255,255,255,0.3)` mode divider.
- **Max-width**: 1240px with 20/32/55px horizontal padding.

### Content Width

- **Prose max-width**: not separately tokenized; text blocks live inside the 1240px scene container.
- **Container max-width**: 1240px.
- **Sidebar width**: none.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Mobile | max-width: 599px | 20px side padding, 80px nav, 40px major gap |
| Tablet | min-width: 600px | 32px side padding, 88px nav, 64px major gap |
| Desktop | min-width: 1024px | 55/56px side padding, 96px nav, 80px major gap |
| Large | 1240px / 1440px | Content container and image stage caps |

### Touch Targets

- **Minimum tap size**: Store buttons are 54px tall; black pill CTA is 54/58px tall.
- **Button height (mobile)**: 54px observed for store buttons and pill CTA.
- **Input height (mobile)**: not observed on homepage.

### Collapsing Strategy

- **Navigation**: fixed horizontal header remains; some utility elements are hidden on small screens.
- **Grid columns**: no multi-column grid collapse; scenes remain flex-column/story blocks.
- **Sidebar**: none.
- **Hero layout**: photo remains full bleed while copy/button spacing changes by breakpoint.

### Image Behavior

- **Strategy**: full-bleed background image with `background-size: cover`.
- **Max-width**: 1440px for absolute image stage.
- **Aspect ratio handling**: cover/crop, centered at 50%/50%.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Store button**

```html
<a class="fHDPr" href="#">
  <img src="app-store.svg" alt="Download on the App Store">
</a>
```

| Property | Value |
|---|---|
| Background | #FFFFFF |
| Width / height | 152px / 54px |
| Padding | 14px 19px |
| Radius | 12px |
| Border | none |
| Shadow | none |

**Primary pill CTA**

```html
<a class="gIJSqD" href="#">배민클럽 가입하기</a>
```

| Property | Value |
|---|---|
| Background | #000000 |
| Text | #FFF |
| Height | 54px mobile, 58px desktop |
| Padding | 16px 28px / 16px 32px |
| Radius | 9999px |
| Font | 17px/18px, weight 700 |

### Badges

> N/A — distinct badge tokens were not surfaced in the homepage CSS. Do not invent pill labels unless the target UI needs them.

### Cards & Containers

배민의 homepage chrome is intentionally sparse. The only card-like surfaces are utility buttons:

- App store surfaces: #FFFFFF, radius 12px, fixed dimensions.
- QR utility button: #FFFFFF with #f7f7f7 hover.
- Tooltip/dropdown surface: rgba(0,0,0,0.8), radius 16px, padding 20px 40px.
- No bordered feature cards, no elevation cards, no 3-column marketing cards.

### Navigation

```html
<nav class="jaUKnG">
  <a class="logo">배달의민족</a>
  <a class="fKqvQR">우아한형제들</a>
  <a class="fKqvQR">라이더 모집</a>
  <a class="fKqvQR">For foreigners</a>
</nav>
```

| Property | Value |
|---|---|
| Position | fixed top center |
| Height | 80 / 88 / 96px |
| Max width | 1240px |
| Color | #FFF |
| Link font | 16px, weight 700, line-height 140% |
| Background | transparent |

### Inputs & Forms

> N/A — no form input component was observed on the homepage. The CSS resets `input, textarea, button, select, a` to #222222 and removes native appearance, but no full form state system surfaced.

### Hero Section

```html
<section class="lnEEkB">
  <div class="IntroSection-styles__BackgroundAnimation-sc-d3677b7a-2"></div>
  <div class="IntroSection-styles__ContentContainer-sc-d3677b7a-1">
    <p class="kECbmG">야식의 설렘<br>식지 않도록</p>
    <div class="store-buttons">...</div>
  </div>
</section>
```

| Property | Value |
|---|---|
| Background | cover image + dark gradient overlay |
| Section bg fallback | #0CEFD3 |
| Content max-width | 1240px |
| Copy font | BAEMINWORK |
| Copy color | #0CEFD3 or #FFF depending scene |
| Scroll hint | fixed bottom SVG, #FFF, `scroll-float 2s ease-in-out infinite` |

### 13-2. Named Variants

**`nav-fixed-transparent`**

- Fixed at top, transparent surface, #FFF text, 1240px max-width.
- Used on image/dark scenes; do not add a white nav bar behind it.

**`store-button`**

- White 152px x 54px rounded rectangle with app-store artwork.
- This button is an asset container, not a text CTA.

**`qr-button`**

- White rounded square/utility block with #f7f7f7 hover.
- Keeps the same 12px radius family as store buttons.

**`pill-cta`**

- Black pill, white text, 9999px radius.
- Use for direct action inside bright teal or light sections.

**`teal-section`**

- Full-width #0CEFD3 scene, 1240px inner content, flex-column layout.
- Treat this as a scene surface, not a card background.

### 13-3. Signature Micro-Specs

```yaml
food-photo-teal-billboard:
  description: "Real food photography becomes the stage for oversized Baemin display copy."
  technique: "full-bleed cover image + linear-gradient(90deg, rgba(0,0,0,0.5) 2.52%, rgba(0,0,0,0) 100%) + BAEMINWORK 800 + letter-spacing -0.04em"
  applied_to: ["{component.hero-section}", "{component.teal-section}"]
  visual_signature: "A #0CEFD3 signboard stamped directly onto appetizing food photography."

transparent-white-scene-header:
  description: "Navigation stays present but refuses to become a separate bar."
  technique: "position: fixed; top: 0; left: 50%; transform: translateX(-50%); max-width: 1240px; height: 80/88/96px; color: #FFF; divider rgba(255,255,255,0.3)"
  applied_to: ["{component.nav-fixed-transparent}"]
  visual_signature: "White logo and links float over the scene like menu text printed on glass."

height-zero-scene-reveal:
  description: "Sections open as staged panels instead of ordinary scroll blocks."
  technique: "height: 0px; overflow: hidden; flex centering; zoom-in 1s linear forwards; scroll-float 2s ease-in-out infinite"
  applied_to: ["{component.hero-section}", "{component.teal-section}"]
  visual_signature: "The homepage reads as a sequence of food-ad scenes, not a feature grid."

white-download-price-tags:
  description: "Download and QR controls behave like physical white labels placed on photography."
  technique: "background #FFFFFF; width 152px; height 54px; padding 14px 19px; border-radius 12px; border none; box-shadow none; hover #f7f7f7 for QR utility"
  applied_to: ["{component.store-button}", "{component.qr-button}"]
  visual_signature: "Small white app labels stay tactile and readable without becoming elevated cards."

scene-mode-token-swap:
  description: "Only two custom properties (`--color-mode-text`, `--color-mode-divider`) drive cross-scene chrome — no semantic palette layered on top."
  technique: "var(--color-mode-text) and var(--color-mode-divider) flip per scene; divider stays at rgba(255,255,255,0.3) over teal/photography while text role inverts (white over imagery, near-black on white floor). No 12-step neutral ramp."
  applied_to: ["{component.nav-fixed-transparent}", "{component.scene-section}"]
  visual_signature: "The chrome reads the photograph behind it — one swap, not a palette."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | short Korean phrase, sensory and immediate | "야식의 설렘 식지 않도록" |
| Product claim | concrete benefit, not abstract brand mission | "시켜도 시켜도 배달팁 무료" |
| Service scope | everyday objects and foods listed plainly | "핸드폰, 책, 꽃다발까지" |
| CTA | direct, practical, app/action-oriented | app download buttons, QR |
| Tone | playful but commercially direct | "아낌없이 다- 드립니다." |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Baemin — copy into your root stylesheet */
@font-face {
  font-family: "BAEMINWORK";
  src: url("/fonts/BAEMINWORK.otf") format("opentype");
  font-display: swap;
}

:root {
  /* Fonts */
  --baemin-font-display: "BAEMINWORK";
  --baemin-font-body: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --baemin-font-weight-normal: 400;
  --baemin-font-weight-bold: 800;

  /* Brand */
  --baemin-primary: #0CEFD3;

  /* Surfaces */
  --baemin-bg-page: #f6f6f6;
  --baemin-bg-white: #FFFFFF;
  --baemin-bg-dark: #000000;
  --baemin-text: #222222;
  --baemin-text-inverse: #FFF;
  --baemin-text-muted: #B1B3B5;
  --baemin-hover-soft: #f7f7f7;

  /* Layout */
  --baemin-container: 1240px;
  --baemin-stage: 1440px;
  --baemin-space-section-x: 56px;
  --baemin-space-scene-gap: 80px;

  /* Radius */
  --baemin-radius-button: 12px;
  --baemin-radius-tooltip: 16px;
  --baemin-radius-pill: 9999px;
}

.baemin-hero {
  min-height: 100vh;
  color: var(--baemin-text-inverse);
  background:
    linear-gradient(90deg, rgba(0,0,0,0.5) 2.52%, rgba(0,0,0,0) 100%),
    var(--hero-image) center / cover no-repeat;
}

.baemin-hero__inner {
  max-width: var(--baemin-container);
  margin: 0 auto;
  padding: 120px 55px;
}

.baemin-display {
  margin: 0;
  font-family: var(--baemin-font-display), var(--baemin-font-body);
  color: var(--baemin-primary);
  font-size: clamp(32px, 6vw, 72px);
  font-weight: var(--baemin-font-weight-bold);
  line-height: 1.4;
  letter-spacing: -0.04em;
  white-space: pre-line;
}

.baemin-store-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 152px;
  height: 54px;
  padding: 14px 19px;
  border: 0;
  border-radius: var(--baemin-radius-button);
  background: var(--baemin-bg-white);
}

.baemin-pill-cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 58px;
  padding: 16px 32px;
  border-radius: var(--baemin-radius-pill);
  background: var(--baemin-bg-dark);
  color: var(--baemin-text-inverse);
  font-weight: 700;
  line-height: 1.4;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Baemin-inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        baemin: {
          primary: '#0CEFD3',
          page: '#f6f6f6',
          white: '#FFFFFF',
          dark: '#000000',
          ink: '#222222',
          muted: '#B1B3B5',
          hover: '#f7f7f7',
        },
      },
      fontFamily: {
        baeminDisplay: ['BAEMINWORK', 'Pretendard', 'system-ui', 'sans-serif'],
        sans: ['-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
      },
      letterSpacing: {
        baeminTight: '-0.04em',
      },
      maxWidth: {
        baemin: '1240px',
        baeminStage: '1440px',
      },
      borderRadius: {
        baeminButton: '12px',
        baeminTooltip: '16px',
        baeminPill: '9999px',
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
| Brand primary | `{colors.primary}` | #0CEFD3 |
| Background | `{colors.surface-light}` | #f6f6f6 |
| Dark scene | `{colors.surface-dark}` | #000000 |
| Surface | `{colors.surface-white}` | #FFFFFF |
| Text primary | `{colors.text-primary}` | #222222 |
| Text inverse | `{colors.text-inverse}` | #FFF |
| Text muted | `{colors.text-muted}` | #B1B3B5 |
| Hover soft | `{colors.hover-soft}` | #f7f7f7 |

### Example Component Prompts

#### Hero Section

```text
배달의민족 스타일 히어로 섹션을 만들어줘.
- 배경: full-bleed food photography with 90deg rgba(0,0,0,0.5) overlay
- H1: BAEMINWORK, clamp(32px, 6vw, 72px), weight 800, line-height 140%, tracking -0.04em
- H1 color: #0CEFD3
- Nav: fixed top, transparent, #FFF logo and links, height 96px, max-width 1240px
- Controls: white App Store / Google Play buttons, 152px x 54px, radius 12px
- Avoid cards, gradients, and abstract illustrations.
```

#### Card Component

```text
배달의민족 스타일 utility card를 만들어줘.
- 배경: #FFFFFF
- border: none
- radius: 12px
- shadow: none
- hover: background #f7f7f7 only
- fixed, tactile label feeling rather than elevated SaaS card
```

#### Badge

```text
배민 홈페이지에는 독립 badge 시스템이 거의 없으니, 필요하면 #0CEFD3 filled surface 또는 #000000 pill CTA 중 하나로 흡수해줘.
- Do not invent secondary badge colors.
- Radius should be 9999px for action pills, 12px for utility labels.
```

#### Navigation

```text
배달의민족 스타일 상단 네비게이션을 만들어줘.
- position: fixed; top: 0; left: 50%; transform: translateX(-50%)
- max-width: 1240px; height: 96px; padding: 0 55px
- background: transparent
- logo/link color: #FFF
- links: 16px, weight 700, line-height 140%
- no white nav background, no bottom shadow
```

### Iteration Guide

- **색상 변경 시**: #0CEFD3 하나를 중심으로 유지. 두 번째 brand color를 만들지 말 것.
- **폰트 변경 시**: hero/display는 `BAEMINWORK`의 무게와 좁은 자간을 대체해야 한다. system font만 쓰면 브랜드성이 급격히 약해진다.
- **여백 조정 시**: 1240px container와 desktop 55/56px side padding을 유지한다.
- **새 컴포넌트 추가 시**: card보다 utility label/pill/button으로 생각한다. border와 shadow를 기본값으로 넣지 않는다.
- **사진 처리**: food photography must stay real and appetizing. Abstract blob/gradient hero is off-brand.
- **모션**: scroll-float, reveal, photo zoom처럼 장면 전환에 쓰고, hover bounce 같은 장난은 피한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use #0CEFD3 as the single high-chroma brand signal.
- Put large Korean display copy over real food or delivery-related photography.
- Use `BAEMINWORK` for display text and keep `letter-spacing: -0.04em`.
- Keep the top navigation transparent, fixed, and white on image/dark scenes.
- Use 1240px content max-width and 1440px image stage max-width.
- Treat store buttons as white utility labels with 12px radius and no shadow.
- Use black pills (#000000 bg, #FFF text, 9999px radius) for direct CTAs.
- Let scene transitions and background images carry drama instead of card grids.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white`로만 두지 말 것 — 전체 page floor는 `#f6f6f6`, hero/scene은 사진·`#0CEFD3`·`#000000`을 함께 사용.
- 브랜드 컬러를 `#00C4B3`, `#00D7C3`, 또는 임의 teal로 바꾸지 말 것 — 확인된 anchor는 `#0CEFD3`.
- 본문/기본 텍스트를 `#000000` 또는 `black`으로만 두지 말 것 — 기본 링크/input reset은 `#222222`, inverse scene은 `#FFF`.
- muted text를 `#999999`로 단순화하지 말 것 — footer/detail gray는 `#B1B3B5` 또는 `#7E8082`.
- Hero를 `#FFFFFF` background + centered H1 + generic CTA로 만들지 말 것 — photo overlay + left editorial copy가 핵심.
- Display headline에 `font-weight: 400` 또는 `font-weight: 500`을 쓰지 말 것 — 큰 카피는 800 계열로 밀어야 한다.
- Hero display에 `letter-spacing: 0`을 쓰지 말 것 — `-0.04em` 압축이 간판 느낌을 만든다.
- Store buttons에 box-shadow나 border를 추가하지 말 것 — #FFFFFF surface, 12px radius, no border/shadow.
- Teal section 위에 pastel gradients or purple/blue AI gradients를 얹지 말 것 — #0CEFD3 flat block이 맞다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **Second brand color** — absent. #0CEFD3 carries the chromatic identity alone.
- **Gradient brand ramp** — no multi-stop brand gradient token; photo overlay gradients are functional darkening, not brand decoration.
- **Card grid marketing** — no "feature 3-card" SaaS rhythm. The homepage uses scenes.
- **Decorative shadows** — none on major UI chrome; depth comes from photography.
- **Outlined card borders** — absent for homepage utility surfaces.
- **Thin elegant typography** — no 300-weight premium editorial voice. The brand is heavy and loud.
- **Abstract SVG hero illustration** — no generic geometric hero. Real food/delivery imagery is the visual material.
- **Dense dashboard navigation** — no sidebar, no tabs, no app-dashboard density.
- **Colorful badge taxonomy** — no success/warning/info badge family surfaced.
- Showroom price-grid catalog: absent. The site narrates one display case at a time, not a multi-product index.
- Multi-product gallery wall on the hero stage: never. One scene equals one exhibit.
- Curatorial caption column / serif museum label: zero. Display copy stays mint over photography.
- Secondary exhibit accent (warm orange, ribbon blue) on the showroom shelf: none. The mint signage is the only label color.
- Sticker-style decorative illustration over food photography: absent. Only typography sits on the display case glass.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual / REQUIRED -->

- **Single homepage surface** — this guide uses the reused homepage phase1. Checkout, order flow, store listing, search, login, and payment screens were not visited.
- **Desktop screenshot emphasis** — the hero screenshot is 1280x800. Responsive behavior was inferred from CSS media queries at 599px/600px/1024px, not from fresh mobile screenshots in this turn.
- **Sparse public token layer** — only `--color-mode-text` and `--color-mode-divider` were surfaced as custom properties. The `baemin-*` names in this guide are documentation aliases, not confirmed upstream CSS variable names.
- **Motion logic not fully executed** — CSS animation names (`zoom-in`, `scroll-float`, `bike`) were observed, but the JS scroll/section timing system was not re-run or instrumented.
- **Font metrics not measured** — `BAEMINWORK` is confirmed by CSS, but exact glyph metrics and fallback differences were not rendered side by side.
- **Logo and image asset colors filtered manually** — frequency candidates include neutrals and an SVG-pattern-like #181A1C; the brand decision favors #0CEFD3 because it is the only chromatic page/system anchor.
- **Form states absent** — input validation, loading, disabled, error, and focus styles for forms were not visible on the homepage CSS sample.
- **No HTML report generation** — per request, Step 6 RENDER-HTML was skipped and only `design.md` was regenerated.
