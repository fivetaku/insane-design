---
schema_version: 3.1
slug: mercedes-benz
service_name: Mercedes-Benz
site_url: https://www.mercedes-benz.com/en/
fetched_at: 2026-04-23
default_theme: mixed
brand_color: "#9F9F9F"
primary_font: MBCorpoSText
font_weight_normal: 400
token_prefix: --wb-*

bold_direction: "Monochrome Luxury"
aesthetic_category: "Monochrome Luxury"
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Mercedes-Benz (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: auto+manual -->

Mercedes-Benz의 현재 `www.mercedes-benz.com/en/` 프런트는 예전 문서에 적혀 있던 "초경량 100 weight 실버 사이트"라기보다, **Workbench 토큰 레이어 위에 얹힌 흑백 스테이지 시스템**에 가깝다. `brandhub-article-stage-text--background-black`와 `--background-white` 두 변형이 동시에 존재하고, 동일한 컴포넌트가 배경만 검정/흰색으로 뒤집히면서 텍스트와 breadcrumb 색도 함께 반전된다. 화면 경험의 핵심은 검은 스테이지와 흰 스테이지가 교차하는 장면 전환이다.

색상 전략도 추측보다 훨씬 구체적이다. 루트 토큰에는 `--wb-grey-05: #0D0D0D`, `--wb-grey-60: #9F9F9F`, `--wb-grey-70: #BBBBBB`, `--wb-grey-90: #F4F4F4`, `--wb-black: #000000`, `--wb-white: #FFFFFF`가 선언되어 있다. 실제 컴포넌트에서는 검은 스테이지의 breadcrumb가 `#9F9F9F`, 흰 스테이지의 breadcrumb가 `#767676`, 풋노트 텍스트가 `#919191`, overview breadcrumb가 `#CCCCCC`를 사용한다. 요청 메모에 있던 `#BABABA`와 `#0A0A0A`는 **current live CSS에 정확히 등장하지 않았고**, 가장 가까운 선언값은 `#BBBBBB`와 `#0D0D0D`다.

타이포그래피도 기존 기록과 다르다. 현재 CSS는 `font-family: "MBCorpo Text"`와 `font-family: "MBCorpo Title"`을 직접 선언하며, body 축 폰트 파일은 `MBCorpoSText-Regular-Web.woff2`, display 축은 `MBCorpoATitleCond-Regular-Web.woff2`로 로드된다. 즉 **본문 family alias는 `MBCorpo Text`지만, 실제 자산명으로는 `MBCorpoSText`가 확인된다.** weight는 `400`과 `700`만 감지되며, 기존 문서의 `font-weight: 100` 가정은 current CSS 기준으로 성립하지 않는다.

레이아웃은 자동차 브랜드 특유의 "거대한 장면 + 절제된 텍스트" 쪽이다. `brandhub-article-stage-text__text-wrapper`가 모바일 `repeat(6, 2fr)`에서 태블릿 `repeat(8, 2fr)`, 데스크톱 `repeat(12, 2fr)`로 확장되고, headline은 `3.5714285714rem`에서 `7.1428571429rem`, `8.5714285714rem`까지 커진다. radius는 입력 필드의 `0.0714285714rem` 1px 헤어라인과 버튼의 `1.75rem` pill 정도만 드러나고, 모션은 `background-color .5s, color .25s` 수준으로 매우 절제되어 있다.

### Key Characteristics

- Workbench 토큰 레이어 `--wb-*` + `brandhub-*` 커스텀 엘리먼트 조합
- 검정/흰 스테이지를 오가는 mixed theme 구조
- operational chrome tone `#9F9F9F` + muted grey `#767676` + footer grey `#919191`
- body alias `MBCorpo Text` / display alias `MBCorpo Title`
- 실제 폰트 자산명으로 `MBCorpoSText-Regular-Web.woff2` 확인
- 모바일 6열 → 태블릿 8열 → 데스크톱 12열 grid
- hero headline `3.5714285714rem` → `7.1428571429rem` → `8.5714285714rem`
- 모서리는 거의 1px 헤어라인, CTA만 `1.75rem` pill

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Monochrome Luxury
> **Aesthetic Category**: Monochrome Luxury
> **Signature Element**: 이 사이트는 **검정/흰 스테이지 전환 위에 `MBCorpo Title` 대형 헤드라인과 chrome breadcrumb `#9F9F9F`를 얹는 hero 구조**로 기억된다.
> **Code Complexity**: medium — `--wb-*` 토큰, `brandhub-*` 컴포넌트, 6/8/12열 반응형 grid가 있지만 CSS 파일 수 자체는 2개로 제한적이다.

---

## 01. Quick Start
<!-- SOURCE: auto+manual -->

> 5분 안에 Mercedes-Benz처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 실제 body/UI 폰트 + weight */
body {
  font-family: "MBCorpo Text", "DaimlerCS-Regular", "DaimlerCSArab-Regular", sans-serif;
  font-weight: 400;
}

/* 2. 스테이지는 black / white 두 상태를 오간다 */
:root {
  --page-dark: #000000;
  --page-light: #FFFFFF;
  --chrome: #9F9F9F;
  --muted: #767676;
}
.stage--dark {
  background: var(--page-dark);
  color: var(--page-light);
  --breadcrumb-color: var(--chrome);
}
.stage--light {
  background: var(--page-light);
  color: var(--page-dark);
  --breadcrumb-color: var(--muted);
}

/* 3. hero는 6/8/12 grid + oversized title */
.hero-copy {
  display: grid;
  grid-template-columns: repeat(6, 2fr);
  gap: 1.1428571429rem;
  padding-top: 12.8571428571rem;
}
@media (min-width: 768px) {
  .hero-copy {
    grid-template-columns: repeat(8, 2fr);
    gap: 2.2857142857rem;
  }
}
@media (min-width: 1024px) {
  .hero-copy {
    grid-template-columns: repeat(12, 2fr);
    gap: 1.7142857143rem;
  }
}
```

**절대 하지 말아야 할 것 하나**: body를 `font-weight: 100`으로 두지 마라. current live CSS에서 감지된 normal/bold는 `400 / 700`뿐이며, `MBCorpo Text` alias + `MBCorpoSText-Regular-Web.woff2`가 현재 기준이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.mercedes-benz.com/en/` |
| Fetched | 2026-04-23 |
| Extractor | `curl_cffi` Safari impersonation + Google referer |
| HTML size | `52449` bytes |
| CSS files | `2` external, `0` inline, total `31021` chars |
| CSS URL 1 | `https://www.mercedes-benz.com/static/frontend/mbcom-frontend/3.1.7/assets/index.css` |
| CSS URL 2 | `https://www.mercedes-benz.com/system/css/mb-main.css` |
| Token prefix | `--wb-*` |
| Method | live HTML/CSS 직접 수집 · 추측값 제거 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework / markup layer**: Mercedes-Benz Workbench + Brandhub custom elements
- **Evidence**: `--wb-*` root tokens, `brandhub-*` selectors, font assets under `assets.oneweb.mercedes-benz.com/plugin/workbench/fonts/2.1.0/`
- **Design system**: Workbench token namespace — `--wb-grey-*`, `--wb-font-*`, `--wb-spacing-*`
- **CSS architecture**: root token palette + component selectors (`brandhub-*`, `.wb-*`, `.page--*`, `.footnotes__*`)
- **Class naming**: token layer는 `--wb-*`, page patch layer는 `.page .breadcrumb`, component layer는 `.brandhub-article-stage-text__*`
- **Default theme**: `mixed` — black stage / white stage 변형 둘 다 current CSS에 존재
- **Font loading**: self-hosted `@font-face` WOFF2
- **Canonical anchor**: `#9F9F9F` operational chrome + `#000000 / #FFFFFF` stage inversion

---

## 04. Font Stack
<!-- SOURCE: auto -->

- **Display font family**: `MBCorpo Title`
- **Display asset**: `MBCorpoATitleCond-Regular-Web.woff2`
- **Body/UI font family**: `MBCorpo Text`
- **Body asset**: `MBCorpoSText-Regular-Web.woff2`
- **Body bold asset**: `MBCorpoSText-Bold-Web.woff2`
- **Fallbacks**: `DaimlerCAC-Regular`, `DaimlerCACArab-Regular`, `DaimlerCS-Regular`, `DaimlerCSArab-Regular`
- **Weight normal / bold**: `400 / 700`

```css
:root {
  --wb-font-title: "MBCorpo Title", "DaimlerCAC-Regular", "DaimlerCACArab-Regular", serif;
  --wb-font-text: "MBCorpo Text", "DaimlerCS-Regular", "DaimlerCSArab-Regular", sans-serif;
  --wb-font-text-bold: "MBCorpo Text", "DaimlerCS-Regular", "DaimlerCSArab-Regular", sans-serif;
}

body {
  font-family: var(--wb-font-text);
  font-weight: 400;
}
```

> 참고: frontmatter의 `primary_font: MBCorpoSText`는 실제 WOFF2 자산명을 기준으로 적었고, CSS family alias는 `MBCorpo Text`다.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token / selector | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `.brandhub-article-stage-text__headline` mobile | `3.5714285714rem` | `400` | `4.2857142857rem` | N/A |
| `.brandhub-article-stage-text__headline` tablet+ | `7.1428571429rem` | `400` | `7.1428571429rem` | N/A |
| `.brandhub-article-stage-text__headline` 1440+ | `8.5714285714rem` | `400` | `8.5714285714rem` | N/A |
| `.brandhub-article-stage-text__subheadline` mobile | `1.1428571429rem` | `400` | `1.7142857143rem` | N/A |
| `.brandhub-article-stage-text__subheadline` 1024+ | `1.2857142857rem` | `400` | `2rem` | N/A |
| `.page .breadcrumb .wb-breadcrumb` | `1.1428571429rem` | `inherit` | N/A | N/A |
| `.footnotes__wrapper` | `1rem` | `inherit` | N/A | N/A |

> 핵심 인사이트: current Mercedes-Benz CSS의 시그니처는 ultra-light 100이 아니라, **400 weight display/body 위에 hero size를 50px → 100px → 120px로 키우는 스케일링**이다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Declared Neutral Ramp (`--wb-grey-*`)

| Token | Hex | Note |
|---|---|---|
| `--wb-grey-05` | `#0D0D0D` | deepest declared grey, requested `#0A0A0A`와 가장 가까운 선언값 |
| `--wb-grey-45` | `#767676` | light stage breadcrumb / muted text |
| `--wb-grey-55` | `#919191` | footer text |
| `--wb-grey-60` | `#9F9F9F` | dark stage breadcrumb, operational chrome |
| `--wb-grey-70` | `#BBBBBB` | chrome ramp step, requested `#BABABA`와 가장 가까운 선언값 |
| `--wb-grey-80` | `#DBDBDB` | light border / soft neutral |
| `--wb-grey-90` | `#F4F4F4` | light surface |

### 06-2. Stage Surfaces

| Token | Hex | Usage |
|---|---|---|
| `--wb-black` | `#000000` | `.brandhub-article-stage-text--background-black` |
| `--wb-white` | `#FFFFFF` | `.brandhub-article-stage-text--background-white` |

### 06-3. Component-Level Semantics

| Selector / alias | Hex | Usage |
|---|---|---|
| `--breadcrumb-color` on black stage | `#9F9F9F` | chrome breadcrumb on dark hero |
| `--breadcrumb-color` on white stage | `#767676` | muted breadcrumb on white stage |
| `.page .breadcrumb .wb-breadcrumb` | `#CCCCCC` | overview breadcrumb text |
| `.page--content .breadcrumb .wb-breadcrumb` | `#767676` | content breadcrumb text |
| `.footnotes__wrapper` text | `#919191` | footer / footnotes copy |

### 06-4. Requested Hex Check

| Requested | Live CSS result | Closest actual token |
|---|---|---|
| `#BABABA` | 미검출 | `--wb-grey-70: #BBBBBB` |
| `#0A0A0A` | 미검출 | `--wb-grey-05: #0D0D0D` + actual stage bg `#000000` |

> 주의: current CSS에는 blue/red/green/yellow 토큰 패밀리도 선언돼 있지만, 실제 Mercedes-Benz homepage mood를 결정하는 건 monochrome grey ramp와 black/white stage 전환이다.

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value |
|---|---|
| `--wb-spacing-3xs` | `.25rem` |
| `--wb-spacing-xxs` | `.5rem` |
| `--wb-spacing-xs` | `1rem` |
| `--wb-spacing-s` | `1.5rem` |
| `--wb-spacing-m` | `2rem` |
| `--wb-spacing-l` | `3rem` |
| `--wb-spacing-xl` | `4rem` |
| `--wb-spacing-xxl` | `5rem` |

> Stage wrapper는 token scale 위에 별도 layout padding을 추가한다. 예: `padding-top: 12.8571428571rem`, `17.8571428571rem`, `10.7142857143rem`.

---

## 08. Radius
<!-- SOURCE: auto -->

| Selector | Radius | Note |
|---|---|---|
| `.salesforcediplomats input` | `.0714285714rem` | 사실상 1px hairline corner |
| `.salesforcediplomats button` | `1.75rem` | pill CTA |

> 대부분의 Mercedes-Benz current CSS는 sharp edge 쪽이고, 실제 rounded emphasis는 CTA pill에서만 강하게 드러난다.

---

## 09. Shadows
<!-- SOURCE: auto -->

> N/A — `index.css`와 `mb-main.css` 두 live CSS 파일에서는 `box-shadow` 선언이 검출되지 않았다.

---

## 10. Motion
<!-- SOURCE: auto -->

| Selector | Transition |
|---|---|
| `.salesforcediplomats button` | `background-color .5s, color .25s` |

> 모션은 매우 절제되어 있고, 상태 변화도 transform보다 색 전환 중심이다.

---

## 11. Layout Patterns
<!-- SOURCE: auto -->

- `brandhub-article-stage-text__text-wrapper`는 기본 `repeat(6, 2fr)` grid + `1.1428571429rem` gap
- `768px` 이상에서 `repeat(8, 2fr)` + `2.2857142857rem` gap
- `1024px` 이상에서 `repeat(12, 2fr)` + `1.7142857143rem` gap
- headline grid span: `1 / span 6` → `1 / span 8` → `1 / span 10`
- subheadline grid span: `1 / span 6` → `1 / span 8` → `1 / span 6` → `1 / span 5`
- stage wrapper side padding: `1.1428571429rem` → `2.2857142857rem` → `6.5714285714rem` → `8.2857142857rem` → `8.5714285714rem`

---

## 12. Responsive
<!-- SOURCE: auto -->

| Breakpoint | Wrapper columns | Column gap | Headline | Subheadline | Padding |
|---|---|---|---|---|---|
| base | `6` | `1.1428571429rem` | `3.5714285714rem / 4.2857142857rem` | `1.1428571429rem / 1.7142857143rem` | `1.1428571429rem` LR / `12.8571428571rem` top |
| `768px+` | `8` | `2.2857142857rem` | `7.1428571429rem / 7.1428571429rem` | same size, `padding-top: 1.7142857143rem` | `2.2857142857rem` LR / `17.8571428571rem` top |
| `1024px+` | `12` | `1.7142857143rem` | same size, span `10` | `1.2857142857rem / 2rem`, span `8` | `6.5714285714rem` LR / `10.7142857143rem` top |
| `1440px+` | `12` | `2.8571428571rem` | `8.5714285714rem / 8.5714285714rem` | span `6` | `8.2857142857rem` LR / `12.8571428571rem` top |
| `1920px+` | `12` | `3.4285714286rem` | wide stage 유지 | span `5` | `8.5714285714rem` LR / `17.1428571429rem` top |

---

## 13. Components
<!-- SOURCE: auto -->

### Stage Hero (`.brandhub-article-stage-text-*`)

```css
.brandhub-article-stage-text--background-black {
  --breadcrumb-color: #9F9F9F;
  background: rgb(0, 0, 0);
}

.brandhub-article-stage-text__headline {
  font-family: MBCorpo Title, sans-serif;
  font-weight: 400;
  font-size: 3.5714285714rem;
  line-height: 4.2857142857rem;
}
```

### Breadcrumb

```css
.page .breadcrumb .wb-breadcrumb {
  color: #CCCCCC !important;
  font-size: 1.1428571429rem;
}

.page--content .breadcrumb .wb-breadcrumb {
  color: #767676 !important;
}
```

### Footnotes

```css
.footnotes__wrapper {
  background-color: black;
  color: #919191;
  font-size: 1rem;
  --spacer-s: 2.2857142857rem;
  --spacer-m: 4.5714285714rem;
  --spacer-l: 6.8571428571rem;
}
```

### Form Controls (`.salesforcediplomats`)

```css
.salesforcediplomats input {
  background-color: var(--wb-white);
  border: .0714285714rem solid var(--wb-grey-60);
  border-radius: .0714285714rem;
  color: var(--wb-grey-20);
  font-family: MBCorpo Text, DaimlerCS-Regular, Helvetica, Arial, sans-serif;
}

.salesforcediplomats button {
  border-radius: 1.75rem;
  font-family: MBCorpo Text, sans-serif;
  transition: background-color .5s, color .25s;
}
```

---

## 14. Content / Copy Voice
<!-- SOURCE: auto+manual -->

| Pattern | Evidence from live HTML | Interpretation |
|---|---|---|
| Main nav taxonomy | `Vehicles`, `Art & Culture`, `Sustainability`, `Design`, `Innovation`, `Exclusive` | 카테고리명 자체를 짧고 무게감 있게 유지 |
| Editorial link title | `Welcome home` | 감성적이지만 과장되지 않은 짧은 문장 |
| CTA | `Explore more` | imperative지만 부드럽고 럭셔리 톤 |
| Tone | noun-heavy navigation + editorial article titles | 판매형 과장보다 큐레이션형 문체 |

---

## 15. Drop-in CSS
<!-- SOURCE: auto -->

```css
:root {
  --mb-font-display: "MBCorpo Title", "DaimlerCAC-Regular", "DaimlerCACArab-Regular", serif;
  --mb-font-text: "MBCorpo Text", "DaimlerCS-Regular", "DaimlerCSArab-Regular", sans-serif;
  --mb-font-text-bold: "MBCorpo Text", "DaimlerCS-Regular", "DaimlerCSArab-Regular", sans-serif;

  --mb-black: #000000;
  --mb-white: #FFFFFF;
  --mb-chrome: #9F9F9F;
  --mb-chrome-soft: #BBBBBB;
  --mb-muted: #767676;
  --mb-footer: #919191;

  --mb-space-3xs: .25rem;
  --mb-space-xxs: .5rem;
  --mb-space-xs: 1rem;
  --mb-space-s: 1.5rem;
  --mb-space-m: 2rem;
  --mb-space-l: 3rem;
  --mb-space-xl: 4rem;
  --mb-space-xxl: 5rem;

  --mb-radius-hairline: .0714285714rem;
  --mb-radius-pill: 1.75rem;
  --mb-transition-ui: background-color .5s, color .25s;
}

body {
  font-family: var(--mb-font-text);
  font-weight: 400;
  background: var(--mb-white);
  color: var(--mb-black);
}

.mb-stage--dark {
  background: var(--mb-black);
  color: var(--mb-white);
  --mb-breadcrumb: var(--mb-chrome);
}

.mb-stage--light {
  background: var(--mb-white);
  color: var(--mb-black);
  --mb-breadcrumb: var(--mb-muted);
}
```

---

## 16. Tailwind
<!-- SOURCE: auto -->

> N/A — live Mercedes-Benz CSS에서 Tailwind utility layer는 감지되지 않았다.

---

## 17. Agent Prompt
<!-- SOURCE: manual -->

Mercedes-Benz current homepage style을 재현하라. body/UI는 `MBCorpo Text` 계열 400, display는 `MBCorpo Title` 400을 사용한다. 배경은 하나의 단색이 아니라 black stage `#000000`와 white stage `#FFFFFF`를 번갈아 쓴다. chrome neutral은 `#9F9F9F`, muted neutral은 `#767676`, footer neutral은 `#919191`를 사용한다. hero copy는 6/8/12-column grid 위에 놓고, headline은 mobile `3.5714285714rem`, tablet `7.1428571429rem`, wide `8.5714285714rem`까지 키운다. 라디우스는 대부분 1px 수준으로 얇고, CTA만 `1.75rem` pill을 허용한다. `font-weight: 100`이나 source에 없는 `#BABABA`, `#0A0A0A`를 "Mercedes 공식값"처럼 하드코딩하지 마라.

---

## 18. DO / DON'T
<!-- SOURCE: auto+manual -->

### ✅ DO

- `MBCorpo Text` / `MBCorpoSText-Regular-Web.woff2` 기준으로 body 400 사용
- hero display는 `MBCorpo Title` 400 + oversized scale 유지
- black stage에서는 breadcrumb를 `#9F9F9F`, white stage에서는 `#767676`로 전환
- 6/8/12-column responsive grid와 큰 padding-top rhythm 유지
- 대부분 sharp edge, CTA만 pill radius 허용

### ❌ DON'T

- stale 문서처럼 `font-weight: 100`을 핵심 규칙으로 되살리지 말 것
- current CSS에 없는 `#BABABA` / `#0A0A0A`를 source-exact 값처럼 적지 말 것
- Workbench의 blue/red/yellow palette를 Mercedes homepage core palette처럼 과용하지 말 것
- 모든 카드와 필드를 12px 이상 radius로 둥글게 만들지 말 것
