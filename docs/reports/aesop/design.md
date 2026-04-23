---
schema_version: 3.1
slug: aesop
service_name: Aesop
site_url: https://www.aesop.com/us/
fetched_at: 2026-04-23
default_theme: light
brand_color: "#333333"
primary_font: SuisseIntl
font_weight_normal: 400
token_prefix: "N/A"

bold_direction: "Warm Apothecary Minimalism"
aesthetic_category: "Refined Minimalism"
signature_element: warm_paper_ink_contrast
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Aesop (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Aesop처럼 만들기 — 3가지만 하면 80%

```css
/* 1. Warm paper + dark ink */
body {
  background: #fffef2;
  color: #333333;
  font: normal 0.75rem/1.5 "SuisseIntl", sans-serif;
}

/* 2. Editorial serif is reserved for hero/section titles */
.aesop-title {
  font-family: "Zapf-Humanist", sans-serif;
  font-size: clamp(1.5625rem, 2vw, 1.9375rem);
  line-height: 1.2;
}

/* 3. CTA stays square, quiet, and high-contrast */
.aesop-cta {
  background: transparent;
  border: 1px solid #fffef2;
  color: #fffef2;
  padding: 0.8125rem 1.5rem 0.75rem;
  transition: background-color 0.25s ease-out, color 0.25s ease-out;
}
```

**절대 하지 말아야 할 것 하나**: 배경을 순백 `#ffffff`로 바꾸고 버튼에 큰 라운드를 주지 마라. Aesop의 인상은 `#fffef2` 종이색 배경, `#333333` 잉크색 텍스트, 직각 버튼의 긴장감에서 나온다.

---

## 02. Provenance
<!-- SOURCE: css -->

| | |
|---|---|
| Source URL | `https://www.aesop.com/us/` |
| HTML title | `Formulations for Skin, Hair & Body Care of the Finest Quality - Aesop` |
| Fetched | `2026-04-23` |
| Extractor | `python3` + `curl_cffi` Safari impersonation |
| HTML size | `926663` bytes |
| CSS files | `5` external bundles, `0` inline bundles |
| CSS total size | `865944` bytes |
| CSS custom properties | `0` |
| Token prefix | `"N/A"` — site ships raw declarations instead of `--*` variables |
| Method | Live CSS download, selector/declaration parsing, no guessed colors or fonts |

### CSS Sources

- `commons.css` — `536337` bytes  
  `https://www.aesop.com/on/demandware.static/Sites-aesop-us-Site/-/en_US/v1776853715160/dist/css/commons.css`
- `category.css` — `73136` bytes  
  `https://www.aesop.com/on/demandware.static/Sites-aesop-us-Site/-/en_US/v1776853715160/dist/css/category.css`
- `product.css` — `157643` bytes  
  `https://www.aesop.com/on/demandware.static/Sites-aesop-us-Site/-/en_US/v1776853715160/dist/css/product.css`
- `pagedesigner.css` — `69790` bytes  
  `https://www.aesop.com/on/demandware.static/Sites-aesop-us-Site/-/en_US/v1776853715160/dist/css/pagedesigner.css`
- `header-transparent.css` — `29038` bytes  
  `https://www.aesop.com/on/demandware.static/Sites-aesop-us-Site/-/en_US/v1776853715160/dist/css/header-transparent.css`

---

## 03. Tech Stack
<!-- SOURCE: css -->

- **Framework**: Salesforce Commerce Cloud / Demandware SSR (`on/demandware.static/Sites-aesop-us-Site/...`)
- **Design system**: bespoke helper-class system, no exported CSS token namespace
- **CSS architecture**: layout + helper + component layering
  ```text
  layout   .l-section / .l-row / .l-column
  helper   .h-color-* / .h-bgcolor-* / .h-text-size-*
  comp     .c-button / .c-content-hero / .c-product-tile / .c-simple-search
  ```
- **Class naming**: `l-` layout, `c-` component, `h-` helper, `m-` modifier
- **Default theme**: light (`body { background: #fffef2; color: #333; }`)
- **Font loading**: self-hosted `woff2` / `woff` / `ttf` bundles from Aesop CDN
- **Canonical anchor**: `#333333` dark ink is the real brand anchor; `#ca432f` is reserved for alert/error states
- **Implementation note**: because there are no `--*` variables, any reusable token layer must be synthesized from repeated declarations

---

## 04. Font Stack
<!-- SOURCE: css -->

| Role | Family | Weight(s) | Evidence |
|---|---|---|---|
| Primary UI / body | `"SuisseIntl", sans-serif` | `400`, `700` | `body`, nav, inputs, descriptions |
| Primary medium UI | `"SuisseIntl-Medium", sans-serif` | `500` | buttons, labels, product names |
| Editorial serif | `"Zapf-Humanist", sans-serif` | `400` | hero title span, section titles, quotes |
| Code / system fallback | `monospace, monospace` | N/A | normalize only, not part of the visual system |

```css
@font-face {
  font-family: "SuisseIntl";
  font-style: normal;
  font-weight: 400;
  src: url("https://www.aesop.com/on/demandware.static/Sites-aesop-us-Site/-/en_US/v1776853715160/dist/fonts/SuisseIntl-Regular-WebXL.woff2") format("woff2");
}
@font-face {
  font-family: "SuisseIntl-Medium";
  font-style: normal;
  font-weight: 500;
  src: url("https://www.aesop.com/on/demandware.static/Sites-aesop-us-Site/-/en_US/v1776853715160/dist/fonts/SuisseIntl-Medium-WebXL.woff2") format("woff2");
}
@font-face {
  font-family: "Zapf-Humanist";
  font-style: normal;
  font-weight: 400;
  src: url("https://www.aesop.com/on/demandware.static/Sites-aesop-us-Site/-/en_US/v1776853715160/dist/fonts/Zapf-Humanist.woff2") format("woff2");
}
```

핵심은 sans/serif의 역할 분리다. 대부분의 UI는 `SuisseIntl`가 맡고, 감정이 필요한 헤드라인만 `Zapf-Humanist`가 맡는다.

---

## 05. Typography Scale
<!-- SOURCE: css -->

| Token | Selector evidence | Size | Weight | Line-height | Font |
|---|---|---|---|---|---|
| `body` | `body` | `0.75rem` | `400` | `1.5` | SuisseIntl |
| `nav` | `.c-navigation__item-title.m-level-1` | `0.875rem` | `400` | `1.2` | SuisseIntl |
| `body-md` | `.c-content-hero__description`, `.c-product-tile__description` | `0.875rem` | `400` | `1.5` | SuisseIntl |
| `label-md` | `.c-content-hero__label`, `.c-content-tile__label` | `0.875rem` | `500` | `1.5` | SuisseIntl-Medium |
| `button` | `.c-button` | `0.875rem` | `500` | `1.3125rem` | SuisseIntl-Medium |
| `section-title-sm` | `.c-section__title,.c-section__title.m-secondary` | `1.5625rem` | `400` | `1.33` | Zapf-Humanist |
| `section-title-lg` | `.c-section__title` large rule | `1.9375rem` | `400` | `1.33` | Zapf-Humanist |
| `hero-title-sm` | `.h-text-size-25` on hero title span | `1.5625rem` | `400` | `1.2` | Zapf-Humanist |
| `hero-title-lg` | `.h-text-size-31-for-large` on hero title span | `1.9375rem` | `400` | `1.2` | Zapf-Humanist |
| `category-cover` | `.c-category-cover__title` | `1.875rem` | `400` | `1.25` | SuisseIntl |

> 핵심 인사이트: 감성은 serif가 만들지만, 시스템의 대부분은 `0.75rem` / `0.875rem`의 절제된 sans UI가 유지한다. 과장된 display scale보다 “작고 정제된 문장”이 Aesop답다.

---

## 06. Colors
<!-- SOURCE: css -->

### 06-1. Brand Ramp

| Token | Hex | Role |
|---|---|---|
| `paper` | `#fffef2` | body / hero light text counterpart |
| `paper-alt` | `#f6f5e8` | muted surface, cards, countdown background |
| `panel` | `#ebeade` | soft panel / muted block background |
| `ink-muted` | `#666666` | secondary copy |
| `ink` | `#333333` | primary text, buttons, navigation |
| `ink-strong` | `#000000` | active / pressed / deepest contrast |

### 06-2. Neutral Ramp

| Step | Hex | Usage |
|---|---|---|
| `0` | `#fffef2` | main paper background |
| `50` | `#f6f5e8` | secondary surface |
| `100` | `#f3f3f3` | utility light panel |
| `200` | `#ebeade` | content panel / muted block |
| `300` | `#d5d5cb` | light divider |
| `400` | `#bcbbb4` | tertiary neutral |
| `500` | `#999999` | disabled state |
| `600` | `#666666` | secondary text |
| `700` | `#4f4f4c` | deeper supporting neutral |
| `800` | `#333333` | default ink |
| `900` | `#252525` | hover/pressed dark |
| `950` | `#000000` | primary active |

### 06-3. Accent Families

| Family | Values | Usage |
|---|---|---|
| `alert-earth` | `#ca432f`, `#ff816b` | error, alert, discontinuation |
| `herbal` | `#6b6b60`, `#5f5f5f`, `#4f4f4c` | success / earthy utility |
| `ochre` | `#e1be5e`, `#ead290`, `#bf900d` | warning / promotional highlights |
| `warm-brown` | `#965d34`, `#945c26` | editorial accent / detail |

### 06-4. Semantic

| Token | Value | Selector evidence |
|---|---|---|
| `bg-page` | `#fffef2` | `body`, `.h-bgcolor-light` |
| `bg-surface` | `#f6f5e8` | `.c-minicart__recommendation`, `.c-countdown` |
| `bg-panel` | `#ebeade` | `.c-product-promotion` |
| `fg-primary` | `#333333` | `body`, `.h-color-primary`, `.c-button` |
| `fg-secondary` | `#666666` | `.c-content-hero__description`, placeholders |
| `fg-disabled` | `#999999` | `.h-color-disabled` |
| `border-default` | `rgba(51,51,51,.2)` | inputs, secondary buttons, search frames |
| `accent-active` | `#000000` | `.h-bgcolor-primary-active` |
| `accent-success` | `#6b6b60` | `.h-bgcolor-success` |
| `accent-alert` | `#ca432f` | `.h-bgcolor-alert`, error states |

### 06-5. Semantic Alias Layer

| Helper class | Value |
|---|---|
| `.h-color-dark`, `.h-color-primary` | `#333333` |
| `.h-color-primary-active` | `#000000` |
| `.h-color-secondary` | `#666666` |
| `.h-color-success` | `#6b6b60` |
| `.h-color-alert` | `#ca432f` |
| `.h-color-disabled` | `#999999` |
| `.h-color-light` | `#fffef2` |
| `.h-bgcolor-light` | `#fffef2` |
| `.h-bgcolor-primary` | `#333333` |
| `.h-bgcolor-primary-active` | `#000000` |
| `.h-bgcolor-secondary` | `#666666` |
| `.h-bgcolor-success` | `#6b6b60` |
| `.h-bgcolor-alert` | `#ca432f` |
| `.h-bgcolor-disabled` | `#999999` |

### 06-6. Dominant Colors (hex frequency in live CSS)

| Rank | Hex | Count | Role |
|---|---|---|---|
| `1` | `#333333` | `762` | ink / button / nav / icon |
| `2` | `#fffef2` | `557` | paper / light text on dark hero |
| `3` | `#000000` | `268` | active/pressed depth |
| `4` | `#666666` | `180` | muted text |
| `5` | `#252525` | `92` | dark hover / pressed |
| `6` | `#999999` | `70` | disabled |
| `7` | `#f6f5e8` | `68` | muted surface |
| `8` | `#ebeade` | `46` | soft panel |

---

## 07. Spacing
<!-- SOURCE: css -->

Aesop은 4px grid보다 **5px 계열(`0.3125rem`) 리듬**이 더 강하다. 가장 자주 반복되는 값은 `5px / 10px / 15px / 20px / 30px / 40px` 축이다.

| Token | Value | Typical use |
|---|---|---|
| `space-1` | `0.3125rem` (`5px`) | micro label gap, text margin |
| `space-2` | `0.625rem` (`10px`) | inline gap, icon/text spacing |
| `space-3` | `0.9375rem` (`15px`) | section gutters, caption padding |
| `space-4` | `1.25rem` (`20px`) | default horizontal padding |
| `space-5` | `1.5rem` (`24px`) | button horizontal balance |
| `space-6` | `1.875rem` (`30px`) | component separation |
| `space-7` | `2.5rem` (`40px`) | hero body padding, input height system |
| `space-8` | `5rem` (`80px`) | standard section rhythm |
| `space-9` | `6.25rem` (`100px`) | large section rhythm variant |

```css
.l-section:not(.m-full-width) > .l-section__row {
  max-width: 75rem;
  padding-left: 0.9375rem;
  padding-right: 0.9375rem;
}
.l-section:not(.m-plain) > .l-section__row {
  margin-top: 5rem;
  margin-bottom: 5rem;
}
```

---

## 08. Radius
<!-- SOURCE: css -->

| Token | Value | Usage |
|---|---|---|
| `radius-none` | `0` | buttons, inputs, selects, cards |
| `radius-sm` | `0.25rem` (`4px`) | alerts, sticky refinement CTA, select badges |
| `radius-md` | `0.3125rem` (`5px`) | small media tiles, comparison labels |
| `radius-lg` | `0.625rem` (`10px`) | rounded media variants, scrollbar thumbs |
| `radius-pill` | `1.875rem` (`30px`) | switch rails |
| `radius-full` | `50%` | icon buttons, radio controls, back-to-top, video play badges |

정체성은 `radius-none` 쪽에 가깝다. 둥근 corners는 보조 요소나 utility에만 허용된다.

---

## 09. Shadows
<!-- SOURCE: css -->

| Token | Value | Usage |
|---|---|---|
| `shadow-focus-ink` | `0 0 0 0.0625rem #333` | inputs / selects / active outlines |
| `shadow-hover-soft` | `0 0 0.25rem 0 rgba(51,51,51,.2)` | hoverable controls, video play badge |
| `shadow-raised-soft` | `0 0 0.25rem 0 rgba(51,51,51,.1)` | sticky refinement CTA |
| `shadow-switch-knob` | `0 0 0.125rem 0 rgba(51,51,51,.5)` | toggle knob |
| `shadow-paper-glow` | `0 0.125rem 0.25rem 0 rgba(255,254,242,.2)` | floating circular controls on dark media |

전반적으로 그림자보다 **색 대비와 보더**를 선호한다. shadow는 깊이 연출이 아니라 컨트롤 가독성 보조용이다.

---

## 10. Motion
<!-- SOURCE: css -->

| Pattern | Value | Where |
|---|---|---|
| `ui-color` | `background-color .25s ease-out, color .25s ease-out` | `.c-button`, icon pseudo-elements |
| `form-focus` | `box-shadow .2s, border-color .2s ease-in-out` | inputs, selects, radio / checkbox |
| `media-transform` | `transform .3s ease-in-out` | animated carousel product tile / image |
| `header-fade` | `background .5s ease-out` | transparent header states |
| `switch` | `all .2s ease-in-out` | toggle rail / knob |

`@media (prefers-reduced-motion: reduce)`가 실제로 존재한다. Aesop의 모션은 시각적 과시보다 상태 전환을 조용히 연결하는 쪽이다.

---

## 11. Layout Patterns
<!-- SOURCE: css -->

### Fullscreen Hero

```css
.c-content-hero.m-fullscreen {
  height: calc(var(--dvh, var(--vh, 1vh)) * 100);
}
.c-content-hero__caption {
  margin: 0 auto;
  max-width: 75rem;
  padding-left: 0.9375rem;
  padding-right: 0.9375rem;
}
.c-content-hero__body {
  display: inline-block;
  padding: 2.5rem 0 1.5625rem;
}
```

### Section Rhythm

```css
.l-section:not(.m-full-width) > .l-section__row {
  margin: 0 auto;
  max-width: 75rem;
  padding-left: 0.9375rem;
  padding-right: 0.9375rem;
  width: 100%;
}
.l-section:not(.m-plain) > .l-section__row {
  margin-top: 5rem;
  margin-bottom: 5rem;
}
```

### Split Editorial Tile

```css
.c-content-tile {
  display: flex;
  align-items: flex-start;
  margin-bottom: 0.9375rem;
}
.c-content-tile.m-large .c-content-tile__section:last-child {
  padding-left: 1.25rem;
}
```

레이아웃은 “넓은 종이 위에 올린 콘텐츠 블록” 구조다. hero와 section 모두 `75rem` 컨테이너를 기준으로 움직이고, 이미지가 시선을 끌더라도 텍스트는 늘 조용한 인쇄물처럼 정렬된다.

---

## 12. Components
<!-- SOURCE: css -->

### Hero CTA

```html
<a class="c-button c-button m-secondary m-readmore-light m-expand-for-medium-down">
  Discover Solais
</a>
```

| Spec | Value |
|---|---|
| background | `transparent` |
| border | `1px solid #fffef2` |
| color | `#fffef2` |
| font | `0.875rem / 1.3125rem` `SuisseIntl-Medium` |
| min-width | `14.375rem` |
| padding | `0.8125rem 1.5rem 0.75rem` |
| icon | `1rem` masked arrow with `margin-left: 1rem` |

### Product Tile

```html
<article class="c-product-tile m-color-dark">
  <h3 class="c-product-tile__name">Replenishing Hand Serum</h3>
  <p class="c-product-tile__description">Meticulously assembled...</p>
</article>
```

| Spec | Value |
|---|---|
| wrapper background | `.c-product-tile__wrapper.m-dark { background: #fffef2; }` |
| root text color | `#333333` |
| name font | `1rem / 1.5` `SuisseIntl-Medium` |
| description font | `0.875rem / 1.5` `SuisseIntl` |
| description clamp | `-webkit-line-clamp: 2` |
| selection border | `#333333` on active / hover |

### Editorial Content Tile

```html
<a class="c-content-tile m-large">
  <div class="c-content-tile__section">
    <p class="c-content-tile__label">Featured</p>
    <h3 class="c-content-tile__title">Aesop title</h3>
    <p class="c-content-tile__description">Quiet explanatory copy.</p>
  </div>
</a>
```

| Spec | Value |
|---|---|
| layout | `display: flex; align-items: flex-start;` |
| title font | `1.5625rem / 1.2` `Zapf-Humanist` |
| label font | `0.875rem / 1.5` `SuisseIntl-Medium` |
| description font | `0.875rem / 1.5` `SuisseIntl` |
| inter-column gap | `1.25rem` base, `2.5rem` larger rule |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Live example |
|---|---|---|
| Eyebrow | 짧고 시적인 한 줄로 mood를 연다 | `A striking show of hands` |
| Product title | 기능보다 제품명을 먼저 세운다 | `New Solais Replenishing Hand Serum` |
| Description | 감각적이되 성분과 효능을 정확히 적는다 | `Meticulously assembled, Niacinamide, LHA and Dandelion Root...` |
| CTA | 조용한 동사 하나로 마무리한다 | `Discover Solais` |

문장은 짧지만 장식적이지 않다. 광고 톤보다 박물관 wall text나 제품 노트에 가깝고, 과장 대신 촉감·성분·사용 감각을 정제된 문장으로 전달한다.

---

## 14. Drop-in CSS
<!-- SOURCE: css -->

사이트 자체는 custom property를 노출하지 않지만, 아래 블록은 **실제 선언값을 그대로 이름 붙인 재사용 레이어**다.

```css
:root {
  --aesop-color-paper: #fffef2;
  --aesop-color-paper-alt: #f6f5e8;
  --aesop-color-panel: #ebeade;
  --aesop-color-ink: #333333;
  --aesop-color-ink-strong: #000000;
  --aesop-color-muted: #666666;
  --aesop-color-disabled: #999999;
  --aesop-color-success: #6b6b60;
  --aesop-color-alert: #ca432f;
  --aesop-color-border: rgba(51, 51, 51, 0.2);

  --aesop-font-sans: "SuisseIntl", sans-serif;
  --aesop-font-sans-medium: "SuisseIntl-Medium", sans-serif;
  --aesop-font-serif: "Zapf-Humanist", sans-serif;

  --aesop-space-1: 0.3125rem;
  --aesop-space-2: 0.625rem;
  --aesop-space-3: 0.9375rem;
  --aesop-space-4: 1.25rem;
  --aesop-space-5: 1.875rem;
  --aesop-space-6: 2.5rem;
  --aesop-space-7: 5rem;

  --aesop-radius-none: 0;
  --aesop-radius-sm: 0.25rem;
  --aesop-radius-md: 0.3125rem;
  --aesop-radius-lg: 0.625rem;

  --aesop-shadow-focus: 0 0 0 0.0625rem #333333;
  --aesop-shadow-soft: 0 0 0.25rem 0 rgba(51, 51, 51, 0.2);
  --aesop-transition-ui: background-color 0.25s ease-out, color 0.25s ease-out;
}

body {
  background: var(--aesop-color-paper);
  color: var(--aesop-color-ink);
  font: normal 0.75rem/1.5 var(--aesop-font-sans);
}

.aesop-title {
  font-family: var(--aesop-font-serif);
  font-size: clamp(1.5625rem, 2vw, 1.9375rem);
  line-height: 1.2;
}

.aesop-button {
  background: transparent;
  border: 1px solid var(--aesop-color-border);
  border-radius: var(--aesop-radius-none);
  color: var(--aesop-color-ink);
  font: normal 0.875rem/1.3125rem var(--aesop-font-sans-medium);
  min-width: 14.375rem;
  padding: 0.8125rem 1.5rem 0.75rem;
  transition: var(--aesop-transition-ui);
}

.aesop-button--light {
  border-color: var(--aesop-color-paper);
  color: var(--aesop-color-paper);
}
```

---

## 15. Tailwind Config
<!-- SOURCE: css -->

```js
export default {
  theme: {
    extend: {
      colors: {
        aesop: {
          paper: "#fffef2",
          paperAlt: "#f6f5e8",
          panel: "#ebeade",
          ink: "#333333",
          inkStrong: "#000000",
          muted: "#666666",
          disabled: "#999999",
          success: "#6b6b60",
          alert: "#ca432f",
        },
      },
      fontFamily: {
        aesopSans: ["SuisseIntl", "sans-serif"],
        aesopSansMedium: ["SuisseIntl-Medium", "sans-serif"],
        aesopSerif: ["Zapf-Humanist", "sans-serif"],
      },
      spacing: {
        "aesop-1": "0.3125rem",
        "aesop-2": "0.625rem",
        "aesop-3": "0.9375rem",
        "aesop-4": "1.25rem",
        "aesop-5": "1.875rem",
        "aesop-6": "2.5rem",
        "aesop-7": "5rem",
      },
      borderRadius: {
        aesop: "0",
        "aesop-sm": "0.25rem",
        "aesop-md": "0.3125rem",
        "aesop-lg": "0.625rem",
      },
      boxShadow: {
        "aesop-focus": "0 0 0 0.0625rem #333333",
        "aesop-soft": "0 0 0.25rem 0 rgba(51,51,51,0.2)",
      },
      maxWidth: {
        "aesop-content": "75rem",
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### DO

- `#fffef2` 종이색 배경과 `#333333` 잉크색 대비를 기본값으로 유지한다.
- `Zapf-Humanist`는 hero / editorial headline에만 제한적으로 사용한다.
- 버튼과 입력은 대부분 `border-radius: 0`로 두고 보더와 간격으로 정체성을 만든다.
- 섹션 폭은 `75rem`, 기본 좌우 패딩은 `0.9375rem`로 유지한다.

### DON'T

- 순백 `#ffffff` 배경, 12px 이상 라운드 버튼, 과장된 gradient를 넣지 마라.
- `#ca432f`를 브랜드 CTA 메인 컬러로 올리지 마라. 이 값은 alert/error 계층이다.
- 본문까지 serif로 확장하지 마라. serif는 포컬 포인트일 때만 힘이 생긴다.
- 4px 그리드 감각으로 지나치게 촘촘하게 맞추지 마라. Aesop은 5px 계열 리듬이 더 자연스럽다.
