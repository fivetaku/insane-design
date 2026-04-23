---
schema_version: 3.1
slug: sony
service_name: Sony
site_url: https://www.sony.com/en/
fetched_at: 2026-04-23
default_theme: mixed
brand_color: "#000000"
primary_font: SST W20 Roman
font_weight_normal: 400
token_prefix: N/A

bold_direction: "Industrial Minimalism"
aesthetic_category: "Industrial Minimalism"
signature_element: hero_impact
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Sony (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere

Sony의 `https://www.sony.com/en/` 홈은 "올블랙 전자상거래"가 아니라, **검은 프레임으로 페이지를 감싸고 흰 컨텐츠 섹션을 끼워 넣는 기업 포털형 레이아웃**이다. 상단 글로벌 헤더(`.tmpl-header_head`)와 메인 히어로(`.hero`), 스크롤 가이드(`.scroll-guide`), 풀스크린 플라이아웃 내비게이션(`.tmpl-flickNav`), 푸터(`.tmpl-footer-wrap`)는 모두 `#000000` 또는 `#1F2024` 계열의 검은 축 위에 놓인다. 반대로 뉴스, 패널, 링크 모음은 `#FFFFFF`와 `#EFEFEF`를 기반으로 돌아간다. 그래서 페이지 인상은 dark이지만 실제 기본 운영 모드는 **mixed**다.

색상 전략도 이 구조를 그대로 따른다. 홈 런타임에서 반복적으로 보이는 핵심값은 `#000000`, `#FFFFFF`, `#656565`, `#BFBFBF`, `#EFEFEF`, `#262626`, `#1F2024`다. Sony-owned CSS만 놓고 보면 **브랜드의 주 언어는 사실상 모노크롬**이며, 뉴스/패널 카테고리 태그에서만 `#BC5B00`, `#B83744`, `#186FA4`, `#5B2C6E` 같은 분류용 포인트 컬러가 등장한다. 추가로 공식 브랜드 페이지 CSS(`includeStyleCMS.css`)에는 `fCoRed { color: #CC0000; }`가 남아 있어 Sony의 레거시 레드 유틸리티를 확인할 수 있었지만, 홈 런타임 CSS에는 `#FF0000`이나 `#CC0000`가 핵심 surface/token으로 쓰이지 않았다.

타이포그래피는 전형적인 Sony SST 계열이다. 기본 본문은 `.main { font-family: "SST W20 Roman", "SST W55 Regular", "Yu Gothic Medium", YuGothic, sans-serif; font-size: .875rem; }`로 시작하고, 강조 텍스트는 `.b { font-family: "SST W20 Bold"; font-weight: 700; }`로 분리된다. 즉 굵기를 weight만으로 조절하기보다, **family 교체와 weight를 함께 쓰는 패턴**이 명확하다. 헤더/푸터는 `Arial`, `"Helvetica Neue"` fallback을 사용하고, 브랜드 v2 CSS에서는 `"SST W20 Light"`도 검증된다.

레이아웃은 1190px 고정 프레임이 핵심이다. `@media screen and (min-width:641px)`에서 `.inner { width: 1190px; }`가 선언되고, 헤더/푸터도 `max-width: 1190px`에 맞춰 정렬된다. 여백은 20px, 40px, 64px, 80px처럼 몇 개의 값으로 반복되고, 카드는 `border-radius: 4px`를 넘지 않는다. 즉 Sony의 인상은 화려한 토큰 시스템이 아니라 **엄격한 프레임, 얇은 보더, compact SST 타입, 절제된 모션**에서 나온다.

인터랙션 역시 절제되어 있다. 히어로 배경 이미지 fade(`opacity .3s ease-out`), 히어로 카피 reveal(`z-index .38s ease-out, opacity .38s ease-out`), 헤더 배경 fade(`0.48s cubic-bezier(0.165, 0.84, 0.44, 1)`), 플라이아웃 메뉴 slide(`.3s ease-out`) 정도가 전부다. 과장된 parallax나 glass 효과는 없고, 애니메이션은 콘텐츠 진입을 정돈하는 수준에 머문다.

### Key Characteristics

- 검은 프레임 + 흰 컨텐츠 섹션의 mixed theme 구조
- `SST W20 Roman` 14px 본문 + `SST W20 Bold` 강조 패턴
- 데스크톱 `1190px` 고정 컨테이너 + `20px` 외곽 gutter
- `#656565` body text, `#BFBFBF` border, `#EFEFEF` sitemap background
- `4px` 카드 radius, 실질적으로 거의 없는 drop shadow
- hero는 `#000000` shell + `#262626` base + `rgba(0,0,0,.4)` overlay
- taxonomy color는 존재하지만 브랜드 primary가 아니라 섹션 분류용
- 공식 브랜드 CSS에서만 검증되는 레거시 red utility `#CC0000`

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Industrial Minimalism
> **Aesthetic Category**: Industrial Minimalism
> **Signature Element**: 이 사이트는 **검은 글로벌 프레임 위에 compact SST 카피를 얹은 full-bleed hero carousel**로 기억된다.
> **Code Complexity**: medium — 공개 토큰 시스템은 없지만 `tmpl-*` 글로벌 템플릿, `hero-*`/`panel-*` 홈 전용 CSS, Swiper hero, fixed flyout nav가 함께 움직인다.

---

## 01. Quick Start

> 5분 안에 Sony처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 */
body {
  font-family: "SST W20 Roman", "SST W55 Regular",
    "Yu Gothic Medium", YuGothic, Arial, sans-serif;
  font-size: 0.875rem;
  color: #656565;
}
.strong {
  font-family: "SST W20 Bold", "SST W55 Bold", Arial, sans-serif;
  font-weight: 700;
}

/* 2. 프레임 컬러 */
:root {
  --frame: #000000;
  --surface: #ffffff;
  --surface-subtle: #efefef;
  --surface-dark: #1f2024;
  --text: #656565;
  --text-strong: #000000;
  --border: #bfbfbf;
  --accent-red: #cc0000; /* 공식 브랜드 CSS의 legacy utility */
}

/* 3. 레이아웃 */
.page-shell {
  max-width: 1190px;
  margin: 0 auto;
  padding-inline: 20px;
}
```

**절대 하지 말아야 할 것 하나**: Sony를 "올블랙 대형 카드 UI"로 구현하지 마라. 실제 홈은 헤더/히어로/푸터만 검은 프레임이고, 뉴스/패널/사이트맵은 `#FFFFFF`와 `#EFEFEF`로 환기된다. 즉 Sony의 핵심은 dark 일변도가 아니라 **검은 frame과 흰 content의 대비**다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.sony.com/en/` |
| Fetched | `2026-04-23` |
| Extractor | `curl_cffi.requests.Session(impersonate="chrome")` + `Referer: https://www.sony.com/` |
| CSS files | `gnavi.css` (37.5KB), `footer.css` (3.0KB), `sitemap.css` (3.8KB), `top/2021/css/sitemap.css` (2.6KB), `flick-nav.css` (7.3KB), `styles.css` (31.7KB), `template/2023/css/search_resp.css` (5.7KB), `search/css/search_resp.css` (5.6KB) |
| Supporting verification | `brand/shared/v2/css/common.css` (1.6KB) for `SST W20 Light`, `brand/shared/css/includeStyleCMS.css` (67.9KB) for `fCoRed { color: #CC0000; }` |
| Token prefix | `N/A` — Sony-owned layer는 literal value 중심. public namespace는 사실상 `--ot-footer-space`, `--swiper-*` 정도만 확인됨 |
| Method | Sony-owned CSS literal value + HTML selector 매칭. Swiper / Marsflag / OneTrust는 존재하더라도 core palette 판정에서는 분리 |

---

## 03. Tech Stack

- **Framework**: 서버 렌더링 corporate portal + 정적 CSS 경로(`/template/2023`, `/template/2024`, `/top/2021`)
- **Design system**: 공개 토큰형 DS 없음. `tmpl-*` 글로벌 템플릿 + `hero-*` / `panel-*` / `news-*` / `panels-new-*` 페이지 전용 모듈
- **CSS architecture**: semantic class naming + fixed-width layout + third-party CSS 조합
- **Class naming**: `.tmpl-header_*`, `.tmpl-footer_*`, `.hero-item-*`, `.panel-*`, `.panels-new-*`, `.news-*`
- **Default theme**: `mixed` — header/hero/footer는 black, content/news/panels는 white, sitemap은 light gray
- **Font loading**: SST W20/W55 계열을 직접 참조. home bundle은 Roman/Bold, brand bundle은 Light까지 검증
- **Canonical anchor**: `#000000` — `.tmpl-header_head`, `.hero`, `.scroll-guide`, flyout nav의 프레임 컬러
- **Animation primitives**: `.3s ease-out`, `.38s ease-out`, `.48s cubic-bezier(0.165, 0.84, 0.44, 1)`, `.8s cubic-bezier(.215,.61,.355,1)`

---

## 04. Font Stack

- **Body/UI**: `"SST W20 Roman", "SST W55 Regular", "Yu Gothic Medium", YuGothic, sans-serif`
- **Strong/Bold**: `"SST W20 Bold", "SST W55 Bold", Arial, sans-serif`
- **Light variant**: `"SST W20 Light", sans-serif` (brand v2 common.css)
- **Locale helper**: `"SST Japanese"`
- **Fallbacks**: `Arial`, `"Helvetica Neue"`, `sans-serif`
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-body: "SST W20 Roman", "SST W55 Regular",
    "Yu Gothic Medium", YuGothic, Arial, sans-serif;
  --font-strong: "SST W20 Bold", "SST W55 Bold", Arial, sans-serif;
  --font-light: "SST W20 Light", sans-serif;
}

body {
  font-family: var(--font-body);
  font-size: 0.875rem;
}

.b,
.hero-item-title,
.hero-item-category {
  font-family: var(--font-strong);
  font-weight: 700;
}
```

> **라이선스 주의**: `SST`는 Sony 고유 폰트다. 대체가 필요하면 `Helvetica Neue` / `Arial` 계열로 좁고 compact한 sans를 맞추는 편이 가장 안전하다.

---

## 05. Typography Scale

| Token | Size | Weight | Line-height | Selector / Context |
|---|---|---|---|---|
| `ui-xs` | `.75rem (12px)` | not overridden | `1` | `.language-select a, .language-select span` |
| `body` | `.875rem (14px)` | browser default (`400`) | not overridden | `.main` |
| `hero-kicker` | `.875rem (14px)` | `700` | `1` | `.hero-item-category` |
| `hero-title` | `1rem (16px)` | `700` via `.b` | `1.625rem` | `html[lang=en] .hero-item-title` |
| `hero-body` | `.875rem (14px)` | browser default | `1.3125rem` | `.hero-item-description` |
| `news-time` | `.6875rem (11px)` | browser default | `1.5rem` | `.news-table a > time` |
| `news-title` | `1.5rem → 1.875rem (24px → 30px)` | `700` | `1` | `.news h2` |
| `section-lead` | `1.125rem (18px)` | not overridden | not overridden | `.panels-new-lead` |
| `campaign-display` | `2.5rem (40px)` | element default | not overridden | `.panels-new-heading` |

> Sony 홈의 타입 스케일은 과장된 display 시스템이 아니라 **14px body + 16px hero card title + 30px news heading + 40px campaign heading**의 compact ladder다.

---

## 06. Colors

### 06-1. Core Frame & Surface

| Token | Hex | Usage |
|---|---|---|
| `--sony-frame` ★ | `#000000` | `.tmpl-header_head`, `.hero`, `.scroll-guide`, flyout nav |
| `--sony-surface-white` | `#FFFFFF` | news/panel/card surfaces |
| `--sony-text-body` | `#656565` | `.main`, body links, metadata |
| `--sony-border` | `#BFBFBF` | section dividers, CTA border, news-more border |
| `--sony-surface-subtle` | `#EFEFEF` | sitemap / link menu background |
| `--sony-hero-floor` | `#262626` | `.hero-bg` |
| `--sony-footer-surface` | `#1F2024` | `.tmpl-footer-wrap` |
| `--sony-header-divider` | `#363636` | header bottom border |

### 06-2. Taxonomy Accents (home page panel categories)

| Category class | Hex | Meaning |
|---|---|---|
| `.panel-category-gaming`, `.panel-category-network-services` | `#BC5B00` | Games / Network Services |
| `.panel-category-music` | `#B83744` | Music |
| `.panel-category-movies-and-tv` | `#916A20` | Movies & TV |
| `.panel-category-audio`, `.panel-category-cameras`, `.panel-category-electronics`, `.panel-category-mobile`, `.panel-category-professional`, `.panel-category-tv` | `#186FA4` | Electronics family |
| `.panel-category-brand`, `.panel-category-corporate`, `.panel-category-design`, `.panel-category-sustainability` | `#036` | Brand / Corporate / Design |
| `.panel-category-financial-services` | `#5B2C6E` | Financial Services |
| `.panel-category-technology` | `#614C63` | Technology |

### 06-3. Legacy Brand Utility

| Token | Hex | Usage |
|---|---|---|
| `fCoRed` | `#CC0000` | 공식 브랜드 CSS(`includeStyleCMS.css`)에 남아 있는 red text utility |

> **주의**: user requirement에 있던 `#FF0000`는 2026-04-23 기준 Sony-owned CSS에서 확인되지 않았다. 확인 가능한 red는 `#CC0000` 하나뿐이었다.

### 06-4. Dominant Colors by Sony-owned CSS Frequency

| Rank | Hex | Notes |
|---|---|---|
| `1` | `#FFF / #FFFFFF` | white surface / reverse text |
| `2` | `#000 / #000000` | frame, hero, scroll guide |
| `3` | `#656565` | default body text |
| `4` | `#BFBFBF` | border / divider |
| `5` | `#EFEFEF` | sitemap background |

---

## 07. Spacing

| Token | Value | Use case |
|---|---|---|
| `space-1` | `10px` | sitemap item padding, compact module spacing |
| `space-2` | `20px` | `.inner` side gutters, desktop gap base |
| `space-3` | `40px` | `calc(100% - 40px)` containers, larger horizontal gutter |
| `space-4` | `64px` | `.panels-new-contents` top padding |
| `space-5` | `80px` | `.panels-new-contents` bottom padding |
| `space-6` | `88px` | `.container` bottom padding |

**주요 alias**

- `desktop-container` → `1190px` fixed width + `20px` external gutter
- `news-cta-padding` → `0 38px`
- `panel-gap` → `20px` desktop / `24px` mobile

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| `radius-none` | `0` | default blocks, buttons, most frame elements |
| `radius-sm` | `4px` | `.panels-new-block`, small interactive elements |
| `radius-full` | `50%` | hero dots, circular close controls |

> Sony-owned CSS는 8px 이상 soft radius를 거의 사용하지 않는다. 둥근 느낌보다 **flat edge + thin border**가 기본이다.

---

## 09. Shadows

| Token | Value | Usage |
|---|---|---|
| `focus-halo` | `0 0 8px #dddddd` | search / focus state halo |

> drop shadow는 사실상 비주얼 언어가 아니다. Sony 홈의 depth는 그림자보다 **black frame, border, blur overlay**로 만든다.

---

## 10. Motion

| Token | Value | Usage |
|---|---|---|
| `hero-image-fade` | `opacity .3s ease-out` | `.hero-bg-image img` |
| `hero-copy-reveal` | `z-index .38s ease-out, opacity .38s ease-out` | `.hero-item-detail` |
| `header-bg-fade` | `opacity 0.48s cubic-bezier(0.165, 0.84, 0.44, 1)` | `.tmpl-header_bg` |
| `flyout-slide` | `.3s ease-out` | `.tmpl-flickNav` transform |
| `scroll-guide-bounce` | `.8s cubic-bezier(.215,.61,.355,1) 0s 7 alternate` | `.scroll-guide svg` |

---

## 11. Layout Patterns

### Grid System

- **Content max-width**: `1190px`
- **Grid type**: fixed desktop frame + full-bleed hero wrapper
- **Column count**: 1-column article flow + 2-column `panels-new-wrap` + 3-column sitemap
- **Gutter**: `20px` desktop, `24px` in stacked mobile panels

### Hero

- **Pattern Summary**: black shell + blurred background image + 40% black cover + bottom-left copy
- **Layout**: full-width carousel, slide width `74.66667vw`, copy block sits at lower area of each item
- **Background**: `#000000` shell / `#262626` hero floor
- **Background Treatment**: `filter: blur(10px)` hero image + `rgba(0,0,0,.4)` overlay
- **H1**: `1rem` / weight `700` / tracking `N/A`
- **Max-width**: full bleed; desktop content frame aligns to `1190px`

### Section Rhythm

```css
section {
  padding: 64px 0 80px;
  max-width: 1190px;
}
```

### Card Patterns

- **Card background**: `#FFFFFF`
- **Card border**: `1px solid #BFBFBF` or no border + clipped image
- **Card radius**: `4px`
- **Card padding**: `0` outer shell, inner CTA paddings `20px`/`38px`
- **Card shadow**: none in the normal state

### Navigation Structure

- **Type**: global black masthead + full-screen flyout
- **Position**: top frame (`70px`) + fixed overlay nav
- **Height**: `70px` header, `60px` footer, `30px` flyout close button
- **Background**: `#000000`
- **Border**: `1px solid #363636` on header bottom

### Content Width

- **Prose max-width**: `N/A` — content is module-based, not article prose-based
- **Container max-width**: `1190px`
- **Sidebar width**: `N/A` on the home page; only `info-box` left rail appears at `min-width:1540px`

---

## 12. Responsive Behavior

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | `max-width: 640px` | panels stack, scroll guide hides, footer/layout become vertical |
| Tablet Fluid | `min-width: 641px and max-width: 1190px` | fixed desktop logic 유지하되 width만 fluid |
| Desktop | `min-width: 641px` | `.inner { width: 1190px; }`, desktop-only utilities visible |
| Large Rail | `min-width: 1540px` | `info-box`가 175px left rail로 확장 |

### Touch Targets

- **Minimum tap size**: `30px` (`.tmpl-flickNav_closeBtn`)
- **Button height (mobile)**: `48px` (`.panels-new-btn`)
- **Input height (mobile)**: `N/A` — search input height는 external Marsflag CSS가 담당

### Collapsing Strategy

- **Navigation**: black masthead + hamburger/flyout overlay
- **Grid columns**: `panels-new-wrap` 2-column → 1-column, gap `20px` → `24px`
- **Sidebar**: none by default; `info-box`는 desktop rail ↔ mobile bottom bar로 전환
- **Hero layout**: scroll guide 숨김, copy spacing 축소, icon size `20px`

### Image Behavior

- **Strategy**: `object-fit: cover` + blur background duplication
- **Max-width**: `100%`
- **Aspect ratio handling**: hero는 cover / content cards는 width-driven image blocks

---

## 13. Components

### Buttons

- **`news-more`** — `height: 57px`, `font-size: 1rem`, `border: 1px solid #BFBFBF`, `padding: 0 38px`, white background
- **`panels-new-btn`** — media trigger / play button, mobile `48px` square

### Badges

- **`panel-category`** — `font-size: .875rem`, `font-weight: 700`, `line-height: 1`, white background, color comes from taxonomy class

### Cards & Containers

- **`.panels-new-block`** — `display: flex`, `flex-direction: column`, `border-radius: 4px`, `overflow: hidden`
- **`.panel`** — block card with `padding-bottom: 6.66667vw`, relative positioning

### Navigation

- **`#tmpl-header`** — black 70px masthead, border-bottom `#363636`
- **`.tmpl-flickNav`** — full-screen overlay, `transform: translate(100%)` → `translate(0)`

### Inputs & Forms

- Sony-owned layer only defines the **search container frame**: `margin-left/right: 20px`, `width: calc(100% - 40px)`.
- Actual search form skin, results list, and input controls are delegated to external Marsflag CSS.

### Hero Section

- `.hero` — `background: #000`
- `.hero-item-detail` — white text, flex column-reverse, reveal animation
- `.hero-bg` — `#262626`
- `.hero-bg-cover` — `rgba(0,0,0,.4)`
- `.hero-bg-image img` — blurred, cover, opacity transition

---

## 14. Content / Copy Voice

| Pattern | Rule | Example |
|---|---|---|
| Headline | 비전형 동사 + 미래 지향 명사 | `"Create the Future of Entertainment"` |
| Primary CTA | 설명형 탐색 문장도 허용 | `"Explore the Initiatives Shaping the Future and the Passion That Fuels the Creators Behind Them"` |
| Secondary CTA | 짧은 utility label | `"view index"` |
| Subheading | 1문장으로 가치 제안 정리 | `"With our technology, we empower creators to express themselves in new ways wherever they are in the world"` |
| Tone | 기업적, 조용한 자신감, creator-facing | `Brand / Technology / Sustainability` 카테고리 구조 자체가 tone을 만든다 |

---

## 15. Drop-in CSS

```css
/* Sony — copy into your root stylesheet */
:root {
  /* Fonts */
  --sony-font-family: "SST W20 Roman", "SST W55 Regular",
    "Yu Gothic Medium", YuGothic, Arial, sans-serif;
  --sony-font-family-strong: "SST W20 Bold", "SST W55 Bold", Arial, sans-serif;
  --sony-font-family-light: "SST W20 Light", sans-serif;
  --sony-font-weight-normal: 400;
  --sony-font-weight-bold: 700;

  /* Core frame */
  --sony-color-brand-25: #ffffff;
  --sony-color-brand-300: #bfbfbf;
  --sony-color-brand-500: #656565;
  --sony-color-brand-600: #000000; /* canonical */
  --sony-color-brand-900: #1f2024;
  --sony-color-accent-red: #cc0000; /* verified in official brand CSS only */

  /* Surfaces */
  --sony-bg-page: #ffffff;
  --sony-bg-frame: #000000;
  --sony-bg-subtle: #efefef;
  --sony-bg-footer: #1f2024;
  --sony-bg-hero-floor: #262626;
  --sony-text: #656565;
  --sony-text-strong: #000000;
  --sony-border: #bfbfbf;

  /* Spacing */
  --sony-space-sm: 10px;
  --sony-space-md: 20px;
  --sony-space-lg: 40px;
  --sony-space-xl: 64px;

  /* Radius */
  --sony-radius-none: 0;
  --sony-radius-sm: 4px;
  --sony-radius-full: 9999px;
}

body {
  font-family: var(--sony-font-family);
  font-size: 0.875rem;
  color: var(--sony-text);
  background: var(--sony-bg-page);
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Sony
module.exports = {
  theme: {
    extend: {
      colors: {
        sony: {
          25: "#ffffff",
          300: "#bfbfbf",
          500: "#656565",
          600: "#000000",
          900: "#1f2024",
        },
        accent: {
          red: "#cc0000",
        },
        taxonomy: {
          gaming: "#bc5b00",
          music: "#b83744",
          electronics: "#186fa4",
          finance: "#5b2c6e",
          brand: "#003366",
          technology: "#614c63",
        },
      },
      fontFamily: {
        sans: ['"SST W20 Roman"', '"SST W55 Regular"', '"Yu Gothic Medium"', "Arial", "sans-serif"],
        strong: ['"SST W20 Bold"', '"SST W55 Bold"', "Arial", "sans-serif"],
        light: ['"SST W20 Light"', "sans-serif"],
      },
      fontSize: {
        body: "0.875rem",
        hero: "1rem",
        news: "1.875rem",
        display: "2.5rem",
      },
      borderRadius: {
        none: "0",
        sm: "4px",
        full: "9999px",
      },
      boxShadow: {
        focus: "0 0 8px #dddddd",
      },
      maxWidth: {
        shell: "1190px",
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Frame | `sony-600` | `#000000` |
| Surface | `sony-25` | `#FFFFFF` |
| Text body | `sony-500` | `#656565` |
| Text strong | `text-strong` | `#000000` |
| Border | `sony-300` | `#BFBFBF` |
| Hero floor | `hero-floor` | `#262626` |
| Legacy accent | `accent-red` | `#CC0000` |

### Example Component Prompts

#### Hero Section

```
Sony 홈 스타일 hero carousel을 만들어줘.
- 프레임 배경: #000000
- 이미지 처리: blur(10px)된 cover 배경 + rgba(0,0,0,0.4) overlay
- 카피: "SST W20 Bold", 16px, line-height 1.625rem, color #FFFFFF
- category label: 14px, bold, white 배경이 아니라 텍스트형 kicker
- outer shell은 full width, inner frame은 1190px 기준으로 정렬
```

#### News CTA

```
Sony 스타일 'view more' CTA를 만들어줘.
- 배경: #FFFFFF
- border: 1px solid #BFBFBF
- height: 57px
- padding: 0 38px
- font: "SST W20 Roman", 16px
- hover는 색을 바꾸기보다 underline이나 subtle color shift로 처리
```

#### Category Badge

```
Sony 홈의 panel-category 스타일 배지를 만들어줘.
- font: "SST W20 Bold", 14px, line-height 1
- background: transparent or white shell
- gaming은 #BC5B00, music은 #B83744, electronics는 #186FA4
- radius는 크게 주지 말고 flat하게 유지
```

#### Global Navigation

```
Sony 글로벌 헤더처럼 상단 내비게이션을 만들어줘.
- 높이: 70px
- 배경: #000000
- 하단 border: 1px solid #363636
- 로고는 좌측, 오른쪽은 hamburger
- 모바일 메뉴는 full-screen overlay로 우측에서 slide-in
```

### Iteration Guide

- **색상 변경 시**: black/white/gray frame을 먼저 유지하고, taxonomy accent는 분류 라벨에만 제한한다.
- **red 요청이 들어오면**: 홈 런타임 primary로 쓰지 말고 `#CC0000` legacy utility 수준에서만 검토한다.
- **폰트 변경 시**: bold는 weight만 올리지 말고 `SST W20 Bold` family로 분리한다.
- **여백 조정 시**: `20 / 40 / 64 / 80px` 축 안에서 움직인다.
- **새 카드 추가 시**: radius는 `4px`를 넘기지 말고 shadow보다 border로 구조를 만든다.
- **반응형 수정 시**: `640 / 641 / 1190 / 1540` breakpoint를 그대로 따른다.

---

## 18. DO / DON'T

### ✅ DO

- `70px` black masthead + `1px solid #363636` divider를 유지한다.
- 본문은 `14px` `SST W20 Roman` + `#656565`를 기본으로 둔다.
- hero는 black shell + blurred image + dark overlay 구조로 만든다.
- desktop에서는 `1190px` 고정 프레임과 `20px` gutter를 유지한다.
- 카드와 모듈의 roundness는 `4px` 이하로 억제한다.

### ❌ DON'T

- Sony를 full-dark 하나의 surface로 단순화하지 마라. 실제 홈은 mixed theme다.
- `.b` 계열 없이 weight만 700으로 올려 Sony의 bold를 흉내 내지 마라.
- `16px+` soft radius, glass shadow, neon gradient를 넣지 마라.
- taxonomy 색을 primary brand color처럼 넓게 퍼뜨리지 마라.
- `#FF0000`를 검증 없이 primary token으로 쓰지 마라. 2026-04-23 기준 Sony-owned CSS에서 확인되지 않았다.
