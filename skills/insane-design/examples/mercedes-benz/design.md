---
schema_version: 3.2
slug: mercedes-benz
service_name: Mercedes-Benz
site_url: https://www.mercedes-benz.com/en/
fetched_at: 2026-04-23T11:46:00+09:00
default_theme: dark
brand_color: "#000000"
primary_font: MBCorpoSText
font_weight_normal: 100
token_prefix: wb

bold_direction: Monochrome Luxury
aesthetic_category: luxury-brand
signature_element: hero_impact
code_complexity: high

medium: web
medium_confidence: high
archetype: automotive
archetype_confidence: high
design_system_level: lv2
design_system_level_evidence: "Workbench/Brandhub web components are present, but extractable CSS custom properties were not available in the captured CSS."

colors:
  surface-black: "#000000"
  surface-white: "#FFFFFF"
  text-muted: "#9F9F9F"
  focus-blue: "#0078D6"
typography:
  display: "MBCorpoATitleCond"
  body: "MBCorpoSText"
  ladder:
    - { token: nav, size: "14px", weight: 100, tracking: "0" }
    - { token: search-list, size: "16px", weight: 100, tracking: "0" }
    - { token: search-list-tablet, size: "18px", weight: 100, tracking: "0" }
    - { token: search-list-wide, size: "20px", weight: 100, tracking: "0" }
  weights_used: [100, 1000]
  weights_absent: [400, 500, 600, 700]
components:
  navigation-dark:
    bg: "{colors.surface-black}"
    color: "{colors.text-muted}"
    hover: "{colors.surface-white}"
  search-link-list:
    color: "{colors.text-muted}"
    gap: "20px"
    transition: "color .4s ease-in-out"
  footer-sitemap-link:
    color: "var(--wb-grey-60)"
    hover: "var(--text-color)"
    transition: "color .3s ease-out"
  focus-ring:
    outline: "3px solid rgba(0,120,214,.8)"
---

# DESIGN.md — Mercedes-Benz

---

## 00. Direction & Metaphor
<!-- SOURCE: auto+manual -->

### Narrative

Mercedes-Benz의 글로벌 홈은 자동차를 설명하는 페이지라기보다 자정의 플래그십 쇼룸 입구다. 상단은 거의 완전한 블랙 `#000000` (`{colors.surface-black}`)으로 잠겨 있고, 메뉴 텍스트는 낮은 명도의 회색 `#9F9F9F` (`{colors.text-muted}`)로 물러난다. 사용자는 정보의 격자 안으로 들어가기 전에 먼저 사진의 깊이와 중앙의 스타를 본다. 사이트라는 자의식은 낮다. 페이지는 자기 존재를 지우고, 자동차 사진이 무대 조명 아래 조각처럼 서 있도록 자리를 비운다.

색은 브랜드를 외치지 않는다. Mercedes-Benz는 이 페이지에서 파란색 CTA, 은색 그라디언트, AMG식 빨간 포인트를 주색으로 쓰지 않는다. 실제로 추출된 chromatic UI 색은 접근성 focus outline의 `rgba(0,120,214,.8)`뿐이고, 화면의 기억은 블랙, 화이트, 회색, 그리고 자동차 사진이 만든 저채도 갈색/그림자에 의해 형성된다. no second brand color. 은색은 CSS 그라디언트가 아니라 사진 속 금속 표면과 스타 엠블럼의 문화적 기억에서 온다.

타이포그래피도 장식보다 제스처에 가깝다. HTML은 `MBCorpoATitleCond-Regular-Web.woff2`와 `MBCorpoSText-Regular-Web.woff2`를 preload하고, CSS 추출 결과는 `font-weight: 100`을 반복적으로 보여준다. 일반적인 웹 제품처럼 400/600의 안전한 대비를 만드는 대신, 얇은 체중의 글자가 어두운 이미지 위에서 조용히 떠 있다. 검은 유리 위에 아주 가는 크롬 각인을 얹은 듯한 운용이다. 글자가 힘을 주지 않기 때문에, 사진과 스타가 더 비싸 보인다.

컴포넌트는 Web Component 이름 그대로의 산업적 질서를 가진다. `brandhub-header`, `brandhub-stage`, `brandhub-teaser-tiles`, `brandhub-editorial-highlight`, `brandhub-footer-sitemap`이 화면을 구성한다. 카드와 버튼보다 중요한 것은 full-bleed photography, 어두운 overlay, hover underline, 외부 링크 아이콘의 색 전환, 1024px 이상에서 열리는 하위 내비게이션이다.

이 사이트의 은유는 "black gallery for moving sculpture"다. 박물관 갤러리처럼 벽은 사라지지 않는다. 오히려 벽이 완전히 검어져서 자동차만 떠오른다. 영화관 스크린의 검정처럼 `#000000` (`{colors.surface-black}`)은 빈 공간이 아니라 집중 장치이고, UI chrome은 표지판이 아니라 쇼룸 직원의 낮은 목소리처럼 뒤로 물러난다. 디자인 시스템의 핵심은 무엇을 추가하느냐보다 무엇을 절대 추가하지 않느냐에 있다.

### Key Characteristics

- Full-bleed automotive photography가 첫 화면의 시각 무게를 거의 전부 가져간다.
- Header는 `#000000` 기반의 dark chrome이며, 브랜드 스타는 중앙에 작고 정밀하게 놓인다.
- 메뉴 텍스트는 `#9F9F9F`처럼 낮은 contrast grey로 시작하고 hover에서 white로 올라온다.
- CTA는 loud brand color가 아니라 muted grey pill 위주로 관찰된다.
- Web Component 기반 구조가 강하다: `brandhub-*` 태그가 레이아웃과 컴포넌트의 실질 이름이다.
- Footer와 search navigation은 list density가 높지만 색 대비를 억제해 premium calm을 유지한다.
- Focus visibility만 `rgba(0,120,214,.8)` blue를 허용한다.
- Motion은 transform/opacity reveal과 underline growth 중심이다. 큰 bounce나 elastic motion은 보이지 않는다.
- Custom Mercedes fonts가 preload된다. generic system sans로 대체하면 브랜드 표정이 크게 약해진다.

---

### 🤖 Direction Summary (Machine Interface — DO NOT EDIT)

> **BOLD Direction**: Monochrome Luxury
> **Aesthetic Category**: luxury-brand
> **Signature Element**: 이 사이트는 **black gallery hero with restrained brand chrome**으로 기억된다.
> **Code Complexity**: high — Web Components, responsive media assets, navigation reveal motion, and external CSS dependency create a complex implementation surface.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Mercedes-Benz처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "MBCorpoSText", "Helvetica Neue", Arial, sans-serif;
  font-weight: 100;
}

/* 2. 배경 + 텍스트 */
:root {
  --mb-bg: #000000;
  --mb-fg: #FFFFFF;
  --mb-muted: #9F9F9F;
}
body {
  background: var(--mb-bg);
  color: var(--mb-fg);
}

/* 3. 브랜드 컬러 */
:root {
  --mb-brand: #000000;
  --mb-focus: rgba(0, 120, 214, .8);
}
```

**절대 하지 말아야 할 것 하나**: Mercedes-Benz를 파란 CTA 브랜드나 silver gradient 브랜드로 해석하지 말 것. 이 홈의 UI는 `#000000`, `#FFFFFF`, `#9F9F9F`가 기본이고 색상은 사진과 focus state에만 제한적으로 나타난다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.mercedes-benz.com/en/` |
| Fetched | 2026-04-23T11:46:00+09:00 |
| Extractor | reused phase1 capture |
| HTML size | 47739 bytes |
| CSS files | 1 usable inline CSS file, 2 external CSS files captured as Access Denied |
| CSS total | 68329 usable inline bytes; 116945 bytes including denied HTML placeholders |
| Token prefix | `wb` inferred from `var(--wb-*)` references |
| Method | phase1 JSON + captured HTML + inline CSS + screenshot interpretation |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Mercedes Brandhub frontend with Web Components (`brandhub-*`) and Vue 2.7.15 loaded as module.
- **Design system**: Workbench / Brandhub conventions — prefix `wb` appears in `var(--wb-grey-60)`, `var(--wb-black)`, and `var(--wb-white)`.
- **CSS architecture**: component-scoped custom element selectors plus external Workbench CSS.
  ```css
  brandhub-header[theme=dark] ...
  brandhub-search-link-list-item [slot=link-list-links] ...
  brandhub-sub-navigation-item [slot] ul li ...
  brandhub-footer-sitemap-item [slot=sitemap-content] ...
  ```
- **Class naming**: mixed. Page sections use plain classes (`header`, `teasertiles`, `editorialhighlight`, `footer`), while interactive UI lives in `brandhub-*` custom elements.
- **Default theme**: dark. Body class includes `dark brandhub-theme-default`; header is rendered with `theme="dark"`.
- **Font loading**: direct preload of `MBCorpoATitleCond-Regular-Web.woff2` and `MBCorpoSText-Regular-Web.woff2`.
- **Canonical anchor**: `<link rel="canonical" href="https://www.mercedes-benz.com/en/">`.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `MBCorpoATitleCond` (Mercedes-Benz brand font, loaded from `assets.oneweb.mercedes-benz.com`)
- **Body font**: `MBCorpoSText` (Mercedes-Benz brand font, loaded from `assets.oneweb.mercedes-benz.com`)
- **Code font**: N/A — no code surface observed.
- **Weight normal / bold**: `100` / `1000` observed in captured CSS. `1000` appears only for `.highlighted` navigation list items.

```css
:root {
  --mb-font-display: "MBCorpoATitleCond", "Arial Narrow", sans-serif;
  --mb-font-body: "MBCorpoSText", "Helvetica Neue", Arial, sans-serif;
  --mb-font-weight-normal: 100;
  --mb-font-weight-emphasis: 1000;
}
body {
  font-family: var(--mb-font-body);
  font-weight: var(--mb-font-weight-normal);
}
```

### Note on Font Substitutes
<!-- SOURCE: manual -->

- **MBCorpoATitleCond** — proprietary brand display face. Use **Arial Narrow** only as a structural fallback, then compensate with tighter line-height and larger letter spacing discipline. Do not replace it with Inter Display; Inter removes the condensed automotive editorial tone.
- **MBCorpoSText** — proprietary body face. Use **Helvetica Neue** or **Arial** at a lighter visual weight, but keep body copy restrained. If the fallback renders heavier, reduce perceived density with `font-weight: 300` and keep navigation color at `#9F9F9F`.
- **Optical correction** — captured CSS does not expose full heading sizes. For hero-like display text, use condensed display at large sizes and avoid bold 700. The Mercedes expression is thin, tall, and photographic, not thick SaaS headline typography.

---

## 05. Typography Scale
<!-- SOURCE: auto+manual -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---:|---:|---:|---:|
| Navigation link | `14px` inferred | `100` | N/A | `0` |
| Search link list | `1.1428571429rem` / `16px` | `100` | N/A | `0` |
| Search link tablet | `1.2857142857rem` / `18px` at `768px` | `100` | N/A | `0` |
| Search link wide | `1.4285714286rem` / `20px` at `1440px` | `100` | N/A | `0` |
| Sub-navigation item | `1rem` / `14px` base assumption | `100` | N/A | `0` |
| Highlighted nav item | `1rem` | `1000` | N/A | `0` |

> ⚠️ CSS extractor found no complete heading scale. The reliable typography evidence is font preload plus component-level navigation/search rules.

### Principles
<!-- SOURCE: manual -->

1. Body and navigation should feel lighter than ordinary web UI. A default `font-weight: 400` makes the chrome too present.
2. The site separates display identity from UI identity: `MBCorpoATitleCond` for headline expression, `MBCorpoSText` for readable interface copy.
3. Text color does the hierarchy work before weight does. Muted grey `#9F9F9F` is the first hierarchy level, white is the active/hover level.
4. Weight `1000` is a rare emphasis tool for highlighted sub-navigation, not a general heading rule.
5. Do not introduce dense SaaS typography ladders. Mercedes-Benz relies on photography and sparse text over large visual surfaces.

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### 06-1. Brand Ramp (2 observed core colors)

| Token | Hex |
|---|---|
| `surface-black` | `#000000` |
| `surface-white` | `#FFFFFF` |

### 06-2. Brand Dark Variant

| Token | Hex |
|---|---|
| `dark-chrome-bg` | `#000000` |
| `dark-chrome-fg` | `#FFFFFF` |
| `dark-chrome-muted` | `#9F9F9F` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| black | `#000000` | `#000000` |
| white | `#FFFFFF` | `#FFFFFF` |
| muted grey | `#9F9F9F` | `#9F9F9F` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| Focus blue | accessibility outline | `#0078D6` via `rgba(0,120,214,.8)` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `surface-black` | `#000000` | body dark theme, header chrome, footer black areas |
| `text-primary-inverted` | `#FFFFFF` | active/hover text on dark theme and SVG external-link icon |
| `text-muted` | `#9F9F9F` | search link list and dark-theme external-link icon |
| `focus-ring` | `#0078D6` | focus-visible outline, alpha `.8` |

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `var(--wb-grey-60)` | unresolved in captured CSS | footer sitemap link color |
| `var(--wb-black)` | unresolved in captured CSS | light-theme header/search link color |
| `var(--wb-white)` | unresolved in captured CSS | dark-theme hover color |
| `var(--text-color)` | unresolved in captured CSS | footer link hover color |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Token | Hex | Frequency |
|---|---:|---:|
| muted grey | `#9F9F9F` | 12 |
| black | `#000000` | 2 |

### 06-8. Color Stories
<!-- SOURCE: manual -->

**`{colors.surface-black}` (`#000000`)** — The showroom wall. It owns the header, dark theme body, footer floor, and brand silhouette. It should feel absolute, not charcoal-softened.

**`{colors.surface-white}` (`#FFFFFF`)** — The active/inverted reading color. It appears as the hover destination and SVG icon fill on dark chrome, not as a dominant page background.

**`{colors.text-muted}` (`#9F9F9F`)** — The Mercedes UI whisper. Navigation and search links begin here so photography and the star logo stay dominant.

**`{colors.focus-blue}` (`#0078D6`)** — Accessibility only. The blue is a browser-like focus affordance, not a brand accent or CTA color.

---

## 07. Spacing
<!-- SOURCE: auto+manual -->

| Token | Value | Use case |
|---|---:|---|
| `search-gap` | `1.25rem` / `20px` | vertical gap between search list links |
| `external-icon-gap` | `.3571428571rem` / `5px` | gap between link text and external icon |
| `subnav-li-y` | `.2857142857rem` / `4px` | vertical padding in sub-navigation list item |
| `subnav-desktop-margin-y` | `.4285714286rem` / `6px` | desktop subnav item rhythm at `1024px` |
| `footer-padding-bottom` | `50px` inline style | footer bottom breathing room |

**주요 alias**:
- `search-list gap` → `20px` (search/menu overlay density)
- `subnav item padding` → `4px 0` (compact dropdown list rhythm)

### Whitespace Philosophy
<!-- SOURCE: manual -->

Mercedes-Benz uses whitespace as darkness, not blank white page area. The hero image fills the viewport and the black header consumes a quiet band above it; the empty space is embedded inside the photograph and overlay rather than around cards.

Below the hero, teaser tiles become denser and more catalog-like, but the overall rhythm stays automotive editorial: large 16:9 images, low-copy labels, and enough spacing for each car photograph to be the object rather than a card ornament.

---

## 08. Radius
<!-- SOURCE: auto+manual -->

| Token | Value | Context |
|---|---:|---|
| CTA pill | high / pill-like observed in screenshot | "Explore more" button |
| Cards | N/A | teaser tile components appear image-first; radius not exposed in captured CSS |
| Focus outline | square outline | `outline: 3px solid rgba(0,120,214,.8)` |

---

## 09. Shadows
<!-- SOURCE: manual -->

| Level | Value | Usage |
|---|---|---|
| Chrome shadow | none observed | header remains flat black |
| Photography depth | image-native | car photography carries depth through the image, not box-shadow |
| Card elevation | N/A | captured CSS does not expose teaser tile shadow rules |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Token | Value | Usage |
|---|---|---|
| `link-color-transition` | `color .4s ease-in-out` | search links |
| `footer-link-transition` | `color .3s ease-out` | footer sitemap links |
| `subnav-reveal` | `transform .3s ease-in-out`, `opacity` | sub-navigation list item reveal |
| `search-li-reveal` | `transform .4s ease-out, opacity .8s ease-out` | search link list item reveal |
| `underline-grow` | `width var(--underline-grow-duration) ease-in` | sub-navigation hover underline |
| `external-icon-transition` | `all .4s ease-in-out` | external link icon color/image swap |

---

## 11. Layout Patterns
<!-- SOURCE: auto+manual -->

### Grid System
- **Content max-width**: `20.1875rem` observed for search link list at `1440px`; broader page container not available from captured CSS.
- **Grid type**: Web Component layout. Footer sitemap uses flex-like width behavior (`width: 50%` then `width: auto` at `1024px`).
- **Column count**: teaser tile area contains 5 `brandhub-teaser-tiles-item` entries in captured HTML.
- **Gutter**: explicit search/link gaps (`20px`, `5px`); teaser gutter not exposed.

### Hero
- **🆕 Pattern Summary**: `full-bleed dark photographic hero + centered brand chrome + muted nav + low CTA`.
- Layout: `brandhub-stage` containing one `brandhub-stage-item`.
- Background: responsive 16:9 automotive/lifestyle image.
- **🆕 Background Treatment**: image-overlay. Screenshot shows a strong dark overlay on top of sunset vehicle photography, preserving legibility over the image.
- H1: display font likely `MBCorpoATitleCond`; exact CSS size not exposed in captured CSS.
- Max-width: image spans viewport; text block appears lower-left in screenshot.

### Section Rhythm

```css
/* observed component rhythm */
brandhub-search-link-list-item [slot=link-list-links] {
  display: flex;
  flex-flow: column;
  gap: 1.25rem;
}

brandhub-footer-sitemap-item [slot=sitemap-content] {
  width: 50%;
}
@media (min-width: 1024px) {
  brandhub-footer-sitemap-item [slot=sitemap-content] {
    width: auto;
  }
}
```

### Card Patterns
- **Card background**: image-first; captured teaser tiles use `picture-json` with responsive sources.
- **Card border**: none observed in captured evidence.
- **Card radius**: not exposed.
- **Card padding**: not exposed.
- **Card shadow**: not exposed; photography and aspect ratio carry the tile.

### Navigation Structure
- **Type**: horizontal desktop brand navigation with nested `brandhub-sub-navigation-item`.
- **Position**: top header chrome; exact `position` unavailable from captured CSS.
- **Height**: screenshot suggests a two-row header band: language/search top, navigation below.
- **Background**: `#000000` dark chrome.
- **Border**: none visible; separation from hero is tonal.

### Content Width
- **Prose max-width**: N/A.
- **Container max-width**: N/A for page; search list caps at `11.5rem`, `16.125rem`, `20.1875rem` across breakpoints.
- **Sidebar width**: N/A.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---:|---|
| Small | `480px` | search link list max-width becomes `11.5rem` |
| Tablet | `768px` | search link list font-size increases to `1.2857142857rem` |
| Desktop | `1024px` | footer sitemap content width switches from `50%` to `auto`; subnav margin appears |
| Wide | `1280px` | search link list max-width becomes `16.125rem` |
| Extra Wide | `1440px` | search link list font-size becomes `1.4285714286rem`, max-width `20.1875rem` |

### Touch Targets
- **Minimum tap size**: not directly measurable from captured CSS.
- **Button height (mobile)**: not directly exposed.
- **Input height (mobile)**: N/A on captured homepage.

### Collapsing Strategy
- **Navigation**: desktop horizontal navigation exists; mobile strategy not captured in visible CSS, but `label-mobile` values exist on language switcher items.
- **Grid columns**: footer sitemap starts at 50% width per item and loosens at desktop.
- **Sidebar**: none observed.
- **Hero layout**: responsive image sources use `maxWidth` buckets from `767` through `999999`.

### Image Behavior
- **Strategy**: responsive `picture-json` on stage and teaser components.
- **Max-width**: image source sizes vary by breakpoint; component handles rendering.
- **Aspect ratio handling**: stage and teaser items specify `aspect-ratio="16by9"`.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Buttons

**Primary muted pill**

| Property | Value |
|---|---|
| Label observed | `Explore more` |
| Background | muted grey pill observed in screenshot |
| Text | dark text on grey pill |
| Radius | pill |
| Icon | right arrow/chevron |
| Role | secondary editorial exploration, not loud purchase CTA |

### Badges

No standalone badge component was observed. Section labels such as `Vehicles`, `Milestones`, and overline text are represented as component attributes (`meta-headline`, `overline-text`) rather than generic badge UI.

### Cards & Containers

**Teaser tile**

| Property | Value |
|---|---|
| Element | `brandhub-teaser-tiles-item` |
| Media | responsive 16:9 automotive image through `picture-json` |
| Labeling | `meta-headline`, `headline-text`, `labeling-color="inverted"` |
| Link | full tile link through `link-url` |
| Visual role | editorial/product discovery grid |

**Editorial highlight**

| Property | Value |
|---|---|
| Element | `brandhub-editorial-highlight` |
| Background | `background-color="black"` |
| Aspect ratio | `16by9` |
| Copy | headline, overline, copy text, CTA |
| Visual role | large story module below product teasers |

### Navigation

**Brand header**

| Property | Value |
|---|---|
| Element | `brandhub-header` |
| Theme | `dark` |
| Logo link | `/en/` |
| Main nav | Vehicles, Art & Culture, Sustainability, Design, Innovation, Exclusive |
| Utility | language switcher, search |

**Sub-navigation item**

```css
brandhub-sub-navigation-item [slot] ul li {
  padding: .2857142857rem 0;
  transition: all .3s ease-in-out;
  transform: translateY(-50%);
  opacity: 0;
}
brandhub-sub-navigation-item [slot] ul li.open {
  transform: translateY(0);
  opacity: 1;
}
brandhub-sub-navigation-item [slot] ul li span:after {
  height: 1px;
  background-color: currentColor;
  width: 0;
}
brandhub-sub-navigation-item [slot] ul li:hover span:after {
  width: 100%;
}
```

### Inputs & Forms

Search is present as a header utility label in the screenshot and as `brandhub-search-link-list-item` CSS. A full text input state was not captured, so form control dimensions, borders, validation, loading, and error states remain unmeasured.

### Hero Section

**Stage hero**

| Property | Value |
|---|---|
| Element | `brandhub-stage` + `brandhub-stage-item` |
| Image | 16:9 responsive vehicle/lifestyle photography |
| Text color | `text-color="inverted"` |
| Label color | `labeling-color="inverted"` |
| Link | `link-text="Watch now"` or screenshot CTA `Explore more` depending captured stage state |
| Mood | dark showroom, photographic, subdued text |

### 13-2. Named Variants
<!-- SOURCE: manual -->

**navigation-dark** — black header chrome

| Property | Value |
|---|---|
| Background | `#000000` |
| Default text | `#9F9F9F` or unresolved `var(--wb-grey-60)` |
| Hover text | `#FFFFFF` / `var(--wb-white)` |
| Motion | `.3s` to `.4s` color transition |

**search-link-list** — vertical menu/search result link stack

| Property | Value |
|---|---|
| Element | `brandhub-search-link-list-item [slot=link-list-links]` |
| Layout | flex column |
| Gap | `1.25rem` |
| Font-size | `16px` to `20px` across breakpoints |
| Reveal | `translateY(-2.1428571429rem)` + opacity |

**footer-sitemap-link** — low-contrast footer navigation

| Property | Value |
|---|---|
| Color | `var(--wb-grey-60)` |
| Hover | `var(--text-color)` |
| Transition | `color .3s ease-out` |
| Layout | `width: 50%` until `1024px`, then `auto` |

**external-link-icon** — SVG data URI icon swap

| Property | Value |
|---|---|
| Size | `1.1428571429rem` or `1.7142857143rem` depending context |
| Fill dark theme | `#9F9F9F`, hover `#FFFFFF` |
| Fill light theme | `#000000` |
| Motion | `all .4s ease-in-out` |

### 13-3. Signature Micro-Specs
<!-- SOURCE: manual -->

```yaml
inverted-photography-stage:
  description: "Vehicle photography becomes the showroom object while UI chrome stays dark and subordinate."
  technique: "brandhub-stage-item with aspect-ratio=\"16by9\", responsive picture-json sources, text-color=\"inverted\", labeling-color=\"inverted\", and screenshot-visible dark overlay on the hero image"
  applied_to: ["{component.stage-hero}", "{component.brandhub-stage}", "{component.brandhub-stage-item}"]
  visual_signature: "A black gallery hero where the car reads as sculpture and the page surface almost disappears."

grey-to-white-hover-chrome:
  description: "Navigation starts as muted chrome and only turns fully white when the user engages."
  technique: "default color #9F9F9F /* {colors.text-muted} */ with transition: color .4s ease-in-out; hover resolves to #FFFFFF /* {colors.surface-white} */ or var(--wb-white); external SVG icon fill swaps from %239f9f9f to %23ffffff"
  applied_to: ["{component.navigation-dark}", "{component.search-link-list}", "{component.external-link-icon}"]
  visual_signature: "No second brand color; hierarchy is made by grey becoming white on a black showroom surface."

hairline-subnav-underline:
  description: "Sub-navigation uses a fine mechanical underline instead of button chrome."
  technique: "span:after { height: 1px; background-color: currentColor; width: 0; transition: width var(--underline-grow-duration) ease-in; } and li:hover span:after { width: 100%; }"
  applied_to: ["{component.sub-navigation-item}", "{component.navigation-dark}"]
  visual_signature: "A precision instrument line that slides under the label, closer to dashboard calibration than web decoration."

mechanical-menu-descent:
  description: "Menu lists deploy from above with opacity, giving navigation an engineered reveal."
  technique: "brandhub-sub-navigation-item li starts at transform: translateY(-50%) and opacity: 0, then .open moves to translateY(0) and opacity: 1; search link list uses translateY(-2.1428571429rem) with transform .4s ease-out and opacity .8s ease-out"
  applied_to: ["{component.search-link-list}", "{component.sub-navigation-item}"]
  visual_signature: "The menu feels lowered into place rather than popped open, matching the automotive cockpit tone."

brandhub-dark-footer-sitemap:
  description: "Footer navigation keeps catalog density while staying low-contrast and black-floor premium."
  technique: "brandhub-footer-sitemap-item [slot=sitemap-content] width: 50% until @media (min-width:1024px) switches to width:auto; links use var(--wb-grey-60) with transition: color .3s ease-out and hover var(--text-color)"
  applied_to: ["{component.footer-sitemap-link}", "{component.footer-sitemap}"]
  visual_signature: "A dense dealership catalog wall softened into quiet grey links on a black floor."
```

---

## 14. Content / Copy Voice
<!-- SOURCE: auto+manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | short, editorial, title-case or sentence fragment | "World premiere of the all-new electric C-Class." |
| Primary CTA | restrained verb phrase | "Watch now", "Explore more" |
| Category label | product/editorial taxonomy | "Vehicles", "Innovation", "Milestones" |
| Subheading | concise context, not feature-list copy | "Recording of the live event on April 20, 2026." |
| Tone | premium editorial, cultural, automotive | "Innovative concepts, exceptional collaborations, background stories." |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Mercedes-Benz — copy into your root stylesheet */
:root {
  /* Fonts */
  --mb-font-display: "MBCorpoATitleCond", "Arial Narrow", sans-serif;
  --mb-font-body: "MBCorpoSText", "Helvetica Neue", Arial, sans-serif;
  --mb-font-weight-normal: 100;
  --mb-font-weight-emphasis: 1000;

  /* Brand / surfaces */
  --mb-color-brand-25: #FFFFFF;
  --mb-color-brand-300: #9F9F9F;
  --mb-color-brand-500: #000000;
  --mb-color-brand-600: #000000;
  --mb-color-brand-900: #000000;

  --mb-bg-page: #000000;
  --mb-bg-dark: #000000;
  --mb-text: #FFFFFF;
  --mb-text-muted: #9F9F9F;
  --mb-focus: rgba(0, 120, 214, .8);

  /* Spacing */
  --mb-space-xs: .2857142857rem;
  --mb-space-sm: .3571428571rem;
  --mb-space-md: 1.25rem;
  --mb-space-lg: 3.5714285714rem;

  /* Radius */
  --mb-radius-pill: 999px;
}

.mb-shell {
  min-height: 100vh;
  background: var(--mb-bg-page);
  color: var(--mb-text);
  font-family: var(--mb-font-body);
  font-weight: var(--mb-font-weight-normal);
}

.mb-nav-link {
  color: var(--mb-text-muted);
  text-decoration: none;
  transition: color .4s ease-in-out;
}
.mb-nav-link:hover {
  color: var(--mb-text);
}
.mb-nav-link:focus-visible {
  outline: 3px solid var(--mb-focus);
}

.mb-hero {
  position: relative;
  min-height: 80vh;
  background: #000000 center / cover no-repeat;
}
.mb-hero::after {
  content: "";
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, .46);
}
.mb-hero__content {
  position: relative;
  z-index: 1;
  padding: 64px;
  max-width: 560px;
}
.mb-cta {
  border: 0;
  border-radius: var(--mb-radius-pill);
  padding: 10px 18px;
  background: #9F9F9F;
  color: #000000;
  font: inherit;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Mercedes-Benz inspired tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        mercedes: {
          black: '#000000',
          white: '#FFFFFF',
          grey: '#9F9F9F',
          focus: '#0078D6',
        },
      },
      fontFamily: {
        sans: ['MBCorpoSText', 'Helvetica Neue', 'Arial', 'sans-serif'],
        display: ['MBCorpoATitleCond', 'Arial Narrow', 'sans-serif'],
      },
      fontWeight: {
        normal: '100',
        emphasis: '1000',
      },
      borderRadius: {
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
| Brand primary | `surface-black` | `#000000` |
| Background | `surface-black` | `#000000` |
| Text primary | `surface-white` | `#FFFFFF` |
| Text muted | `text-muted` | `#9F9F9F` |
| Border | N/A | do not add default borders |
| Focus | `focus-ring` | `#0078D6` |
| Error | N/A | not observed |

### Example Component Prompts

#### Hero Section

```text
Mercedes-Benz 스타일 히어로 섹션을 만들어줘.
- 배경: full-bleed 16:9 automotive photography with dark overlay, base #000000
- H1: MBCorpoATitleCond fallback Arial Narrow, thin visual weight, inverted white
- 서브텍스트: #FFFFFF or #9F9F9F depending contrast, short editorial sentence
- CTA: muted grey pill, black text, small right-arrow icon, no bright brand color
- Header: black chrome, centered star, muted nav links #9F9F9F, hover #FFFFFF
```

#### Teaser Tile

```text
Mercedes-Benz 스타일 티저 타일을 만들어줘.
- 16:9 automotive image is the card, not decoration
- overlay label uses inverted white/grey text
- no visible border, no colored accent bar, no generic card shadow
- copy: category label + short product/editorial headline
- click target can be full image tile
```

#### Navigation

```text
Mercedes-Benz 스타일 상단 내비게이션을 만들어줘.
- background #000000
- links #9F9F9F, hover #FFFFFF with color .4s ease-in-out
- subnav items reveal with translateY from above + opacity
- hover underline grows from width 0 to 100%, 1px currentColor
- focus-visible outline is 3px solid rgba(0,120,214,.8)
```

### Iteration Guide

- **색상 변경 시**: UI brand color를 추가하지 말고 `#000000`, `#FFFFFF`, `#9F9F9F` 안에서 해결한다.
- **폰트 변경 시**: Mercedes font가 없으면 condensed display + light body fallback으로 보정한다.
- **여백 조정 시**: hero는 크게, 메뉴 리스트는 조밀하게. 모든 것을 같은 24px 카드 간격으로 맞추지 않는다.
- **새 컴포넌트 추가 시**: 먼저 사진이 주인공인지 확인한다. UI chrome은 검은 배경과 낮은 contrast 텍스트로 물러난다.
- **반응형**: `480`, `768`, `1024`, `1280`, `1440` 단서를 우선 사용한다.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO

- Use `#000000` as the primary chrome and page mood for Mercedes-Benz global home surfaces.
- Keep navigation and utility text muted with `#9F9F9F`, then move to `#FFFFFF` on hover.
- Use full-bleed 16:9 vehicle photography as the dominant visual asset.
- Use Mercedes-specific typography when available: `MBCorpoATitleCond` for display, `MBCorpoSText` for UI/body.
- Preserve Web Component-style component boundaries when porting: header, stage, teaser tiles, editorial highlight, footer sitemap.
- Use restrained motion: color fade, opacity reveal, translateY, underline growth.
- Use `rgba(0,120,214,.8)` only for focus-visible accessibility feedback.

### ❌ DON'T

- 배경을 `#FFFFFF` 또는 `white` 중심으로 두지 말 것 — 대신 dark chrome/page floor `#000000` 사용.
- 텍스트를 `#000000` 또는 `black` 중심으로 두지 말 것 — dark surface 위 primary text는 `#FFFFFF`, muted text는 `#9F9F9F` 사용.
- CTA를 `#0078D6` 파란 브랜드 버튼으로 만들지 말 것 — `#0078D6`은 focus outline 근거이며 CTA brand color가 아니다.
- Mercedes silver 느낌을 `#C0C0C0` 그라디언트로 합성하지 말 것 — 실제 UI 근거는 `#9F9F9F` muted grey와 `#FFFFFF` hover다.
- Body default를 `font-weight: 400`으로 두껍게 만들지 말 것 — captured CSS에서 반복 관찰된 기본 weight는 `100`이다.
- 모든 heading을 `font-weight: 700` 이상으로 만들지 말 것 — `1000`은 highlighted nav item에만 관찰된 예외다.
- 카드에 `box-shadow: 0 10px 30px rgba(0,0,0,.15)` 같은 generic SaaS elevation을 넣지 말 것 — photography가 depth를 담당한다.
- 컴포넌트 카드에 `border: 1px solid #E5E7EB` 같은 밝은 SaaS hairline을 기본 추가하지 말 것 — captured surface는 black/photo first다.

### 🚫 What This Site Doesn't Use (Negative-Space Identity)

- **Second brand color** — none observed. The homepage UI does not establish a blue, red, or silver secondary brand ramp.
- **Gradient brand system** — absent. Silver-metal gradients are tempting but unsupported by captured UI CSS.
- **Bright SaaS CTAs** — absent. Buttons are muted/editorial, not saturated conversion objects.
- **Heavy card chrome** — absent. Teaser components are image-led rather than bordered/shadowed cards.
- **Generic bold typography** — absent as a default. The captured system is thin and proprietary.
- **Icon-heavy feature grids** — absent. Navigation and photography carry the page, not illustrative icons.
- **Warm cream luxury palette** — absent. This is black gallery luxury, not beige editorial luxury.
- **Playful motion** — absent. Motion is mechanical and precise: fade, translate, underline.
- **Rounded rectangle content blocks everywhere** — absent. Radius appears mainly in CTA pill behavior, not as a universal container language.

---

## 19. Known Gaps & Assumptions
<!-- SOURCE: manual -->

- **External CSS access denied** — `index.css` and `mb-main.css` were captured as Akamai Access Denied HTML placeholders. The analysis relies on usable inline CSS plus HTML attributes and screenshot evidence.
- **CSS custom properties unresolved** — `resolved_tokens.json` reports `total_vars: 0`; variables such as `--wb-grey-60`, `--wb-black`, `--wb-white`, and `--text-color` are referenced but their exact definitions were not present in captured CSS.
- **Hero typography incomplete** — font files are preloaded, but exact H1 size, line-height, and display weight rules were not exposed by the available CSS capture.
- **Screenshot state may differ from HTML stage item** — screenshot shows "Welcome home" / "Explore more", while captured HTML includes a stage item for the all-new electric C-Class livestream. Treat hero pattern as stable, copy as state-dependent.
- **Mobile menu not directly observed** — breakpoints and `label-mobile` hints exist, but actual mobile drawer behavior was not visually captured.
- **Form/search input states not captured** — search utility exists, but input border, typing, loading, empty, and error states are unknown.
- **Dark/light theme mapping incomplete** — CSS references `brandhub-header[theme=light]`, but the homepage capture is primarily dark. Full theme token mapping is not proven.
- **Animation implementation partly inferred** — CSS reveals transition values, but JavaScript sequencing, stagger timing variables, and scroll-trigger logic were not inspected.
- **Teaser tile internals unresolved** — HTML exposes `brandhub-teaser-tiles-item` attributes and images, but radius, overlay opacity, and internal text positioning live in unavailable component CSS.
