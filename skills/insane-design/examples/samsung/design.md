---
schema_version: 3.1
slug: samsung
service_name: Samsung Electronics
site_url: https://www.samsung.com/sec/
fetched_at: 2026-04-23
default_theme: light
brand_color: "#2189FF"
primary_font: Samsung Sharp Sans
font_weight_normal: 400
token_prefix: --cpCarousel-

bold_direction: "Clean Tech Light"
aesthetic_category: "Consumer Electronics"
signature_element: samsung_blue_gradient
code_complexity: medium

medium: web
medium_confidence: high
---

# DESIGN.md — Samsung Electronics (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere

Samsung Electronics 한국 공식 사이트는 **"글로벌 테크 브랜드의 클린 쇼룸"**이다. 압도적인 흰 배경, 풍부한 제품 이미지, 절제된 타이포그래피로 제품 자체가 주인공이 되도록 설계되어 있다.

색상 전략은 **"흰 배경 + 삼성 블루 accent + 광범위한 회색 ramp"**다. 페이지의 95%는 `#ffffff` / `#F7F7F7` / `#FAFAFA` 의 밝은 서피스로 채워지고, 브랜드 컬러 `#2189FF`(삼성 블루)는 CTA 버튼, 링크, active state에만 등장한다. 이 절제된 블루가 오히려 강하게 눈에 들어온다.

타이포그래피는 **Samsung Sharp Sans**가 전 영역을 담당한다. 한국어는 `SamsungOneKorean`이 매핑된다. 폰트 무게는 `bold`와 `700`이 압도적으로 많이(2,500+ 횟수) 쓰여 헤드라인과 강조 요소에 무게감을 부여한다. 본문은 `400` normal.

레이아웃은 **vw 기반 유동 스케일링**이 특징이다. `border-radius: 1.3889vw`, `gap: 1.9975vw` 등 뷰포트 비율 값이 광범위하게 쓰여 다양한 화면 크기에서 일관된 비율감을 유지한다. 대형 carousel 컴포넌트 중심의 페이지 구성.

인터랙션은 Swiper.js 기반 carousel이 핵심이다. `--swiper-navigation-color: #ffffff`, `--swiper-pagination-color: #ffffff` 토큰으로 carousel 컨트롤이 관리된다. hover는 subtle하며, 제품 이미지 자체가 visual 대화를 담당한다.

### Key Characteristics

- 브랜드 블루 `#2189FF` — CTA, 링크, active badge에만 (배경 면적 사용 금지)
- `#ffffff` 압도적 흰 배경 + 제품 이미지 중심
- Samsung Sharp Sans + SamsungOneKorean 2폰트 시스템
- vw 단위 기반 유동 레이아웃 (1.3889vw, 1.9975vw 등)
- `border-radius: 20px` (408x) — 부드러운 카드 모서리
- Swiper.js carousel 컴포넌트 중심 레이아웃
- `--cpCarousel-*` 13개 토큰으로 carousel 시스템 통제
- 에러/경고 레드 `#FA2337`, 딥 네이비 `#1428A0` 보조 accent

### BOLD Direction Summary (apply Lv3 입력점)

> **BOLD Direction**: Clean Tech Light
> **Aesthetic Category**: Consumer Electronics
> **Signature Element**: 이 사이트는 **흰 쇼룸 위에 삼성 블루 `#2189FF`의 절제된 CTA accent + Swiper carousel 제품 진열**로 기억된다.
> **Code Complexity**: medium — --cpCarousel-* 13개 토큰 + Swiper.js 변수. 폰트와 vw 스케일이 복잡성의 핵심.

---

## 01. Quick Start

> 5분 안에 Samsung처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 */
body {
  font-family: 'Samsung Sharp Sans', 'SamsungOneKorean', Dotum, 'Apple SD Gothic Neo', Arial, sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.5;
}

/* 2. 배경 + 텍스트 */
:root {
  --bg:           #ffffff;
  --fg:           #212425;
  --surface:      #F7F7F7;
  --border:       #D9D9D9;
  --text-muted:   #707070;
  --text-subtle:  #8F8F8F;
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 블루 */
:root {
  --brand:      #2189FF;
  --brand-navy: #1428A0;
  --error:      #FA2337;
}
a, .cta-primary { color: var(--brand); }
```

**절대 하지 말아야 할 것 하나**: 브랜드 블루 `#2189FF`를 배경 면적으로 쓰지 마라. Samsung 블루는 버튼, 링크, active indicator에만 등장한다. 블루 섹션 배경을 쓰는 순간 Samsung이 아니라 정보 안내 페이지가 된다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.samsung.com/sec/` |
| Fetched | 2026-04-23 |
| Extractor | curl_cffi + Chrome TLS 우회 + CSS 직접 파싱 |
| CSS files | 16개 파일, 총 5.5MB (common.css 434KB, component.css 635KB, layout.css 210KB) |
| Token prefix | `--cpCarousel-` (carousel 컴포넌트 시스템, 13개 토큰) |
| Method | CSS 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: 서버 사이드 렌더링 (삼성 자체 플랫폼)
- **Design system**: `--cpCarousel-*` 네이밍 기반 컴포넌트 토큰
- **CSS architecture**: 컴포넌트별 네임스페이스 클래스 (.cp-carousel-*, .rvmp-cmpnt 등)
- **Class naming**: `.cp-carousel-*`, `.rvmp-cmpnt`, `.cp-hd-line-block` 등 semantic + namespace
- **Default theme**: light (페이지 전체 밝은 bg)
- **Font loading**: 삼성 자체 CDN — Samsung Sharp Sans, SamsungOneKorean
- **Carousel**: Swiper.js (--swiper-* 변수 사용)
- **Canonical anchor**: `#2189FF` — CTA 버튼, 링크, active state
- **Animation primitives**: Swiper transition + 일반 hover (명시적 duration 토큰 없음)

---

## 04. Font Stack

- **Primary/Body**: `'Samsung Sharp Sans', 'SamsungOneKorean', Dotum, 'Apple SD Gothic Neo', Arial, sans-serif`
- **Korean UI**: `'SamsungOneKorean', dotum, sans-serif`
- **Fallback**: `Dotum, '돋움', sans-serif`
- **Weight normal**: `400`
- **Weight bold**: `700` (또는 `bold`)
- **Available weights**: `300 / 400 / 500 / 600 / 700 / 800`

```css
:root {
  --font-primary: 'Samsung Sharp Sans', 'SamsungOneKorean', Dotum, 'Apple SD Gothic Neo', Arial, sans-serif;
  --font-korean:  'SamsungOneKorean', dotum, sans-serif;
}
body {
  font-family: var(--font-primary);
  font-weight: 400;
}
```

> **라이선스 주의**: Samsung Sharp Sans와 SamsungOneKorean은 삼성전자 독점 폰트 — 공식 프로젝트 외 사용 불가. 대체 시 영문 `Inter` 또는 `DM Sans`, 한국어 `Noto Sans KR` 권장.

---

## 05. Typography Scale

> Samsung 타이포는 헤드라인에 bold/700이 집중된다. vw 단위와 px의 혼용이 특징.

| Step | Size | Weight | Notes |
|---|---|---|---|
| `component-title` | `40px` (--cpCarousel-title-component) | bold | 섹션 타이틀 |
| `list-title` | `22px` (--cpCarousel-title-list) | bold | 제품 리스트 제목 |
| `sub-title` | `20px` (--cpCarousel-title-sub) | bold | 서브 타이틀 |
| `price` | `20px` (--cpCarousel-fontsize-price) | bold | 가격 표시 |
| `description` | `16px` (--cpCarousel-fontsize-description) | 400 | 제품 설명 |
| `flag` | `16px` (--cpCarousel-fontsize-flag) | bold | 배지/플래그 |
| `date` | `12px` (--cpCarousel-fontsize-date) | 400 | 날짜/메타 |

---

## 06. Colors

### 06-1. Brand Blue

| Token | Hex | Usage |
|---|---|---|
| `--samsung-brand` ★ | `#2189FF` | CTA 버튼, 링크, active state (574회) |
| `--samsung-brand-alt` | `#2188FF` | 브랜드 블루 variant (67회) |
| `--samsung-brand-navy` | `#1428A0` | 딥 네이비, dark CTA (39회) |
| `--samsung-brand-link` | `#006BEA` | 링크 hover (14회) |
| `--samsung-brand-dark` | `#0370FF` | 블루 강조 (13회) |

### 06-2. Neutral Text Ramp

| Hex | Count | Usage |
|---|---|---|
| `#212425` | 88x | 본문 텍스트, near-black |
| `#1C1C1C` | 21x | 제목 텍스트 |
| `#313131` | 26x | 강조 텍스트 |
| `#000000` | 24x | pure black (아이콘, border) |

### 06-3. Mid Gray Ramp

| Hex | Count | Usage |
|---|---|---|
| `#707070` | 1019x | 본문 secondary — 최다 등장 중립 |
| `#757575` | 53x | label, caption |
| `#8F8F8F` | 98x | text muted |
| `#A6A6A6` | 43x | disabled text |
| `#B2B2B2` | 214x | muted, inactive |
| `#8E8E8E` | 18x | icon muted |

### 06-4. Light Gray Ramp (border/surface)

| Hex | Count | Usage |
|---|---|---|
| `#D9D9D9` | 449x | border, divider — 핵심 |
| `#DDDDDD` | 118x | light border |
| `#E4E4E4` | 19x | subtle border |
| `#EBEBEB` | 327x | surface border |
| `#EDEDED` | 14x | bg border |
| `#E5E5E5` | 16x | card border |
| `#E7E7E7` | 13x | rule |

### 06-5. Surface / Background

| Hex | Count | Usage |
|---|---|---|
| `#F4F4F4` | 17x | alt bg |
| `#F5F5F5` | 18x | surface |
| `#F7F7F7` | 344x | 기본 surface bg (--cateBgColor) |
| `#F9F9F9` | 39x | light bg |
| `#FAFAFA` | 98x | near white |
| `#FFFFFF` | 13x+ | page bg (CSS 명시 외 기본값) |

### 06-6. Semantic / Accent Colors

| Family | Hex | Count | Use |
|---|---|---|---|
| Error red | `#FA2337` | 54x | 오류, 경고, 할인 배지 |
| Swiper white | `#FFFFFF` | — | carousel nav/pagination |
| Theme active | `#000000` | — | --themeColorActive |
| Theme inactive | `#FFFFFF` | — | --themeColorinActive |

### 06-7. Dominant Colors (실제 CSS 빈도 기준)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#707070` | 1019x | 중립 gray — 본문 secondary |
| 2 | `#2189FF` | 574x | 삼성 블루 — CTA, 링크 ★ |
| 3 | `#D9D9D9` | 449x | border, divider |
| 4 | `#F7F7F7` | 344x | surface bg |
| 5 | `#EBEBEB` | 327x | surface border |
| 6 | `#B2B2B2` | 214x | muted |
| 7 | `#DDDDDD` | 118x | light border |
| 8 | `#8F8F8F` | 98x | text muted |
| 9 | `#FAFAFA` | 98x | near white surface |
| 10 | `#212425` | 88x | near-black body text |
| 11 | `#2188FF` | 67x | brand blue variant |
| 12 | `#FA2337` | 54x | error/warning red |

---

## 07. Spacing

| Token | Value | Use case |
|---|---|---|
| `--cpCarousel-gap-price` | `8px` | 가격 요소 간격 |
| `--cpCarousel-gap-flag` | `16px` | 플래그 간격 |
| `--cpCarousel-gap-innr` | `60px` | carousel 내부 여백 |
| `--cpCarousel-gap-swiper` | `1.9975vw` | swiper 슬라이드 간격 (유동) |
| padding (관찰 최다) | `24px` | 194x — 기본 섹션 padding |
| padding (2위) | `12px` | 92x — 인라인 gap |
| padding (2위) | `36px` | 92x — 대형 섹션 |
| padding-bottom | `24px` | carousel title area 기본 |

---

## 08. Radius

Samsung은 부드러운 모서리를 일관되게 사용한다.

| Token | Value | Count | Context |
|---|---|---|---|
| `radius-xl` | `20px` | 408x | 카드, 이미지 컨테이너 — 주력 |
| `radius-lg` | `10px` | 315x | 버튼, UI 요소 |
| `radius-full` | `50%` | 216x | 아이콘 버튼, avatar |
| `radius-fluid` | `1.3889vw` | 189x | vw 기반 유동 radius |
| `radius-none` | `0` | 188x | 풀블리드 이미지 |
| `radius-fluid-sm` | `1.8182vw` | 158x | 소형 vw radius |
| `radius-sm` | `6px` | 84x | 소형 컴포넌트 |
| `radius-md` | `8px` | 68x | 중간 요소 |

> 관찰: Samsung의 카드 radius는 `20px`이 압도적이다. Apple의 sharp edge와 달리 부드러운 소비자 친화적 모서리가 시그니처.

---

## 09. Carousel System (--cpCarousel-*)

Samsung 홈페이지의 핵심 컴포넌트. 13개 토큰으로 완전 통제.

```css
:root {
  /* 사이즈 */
  --cpCarousel-size-picture:    312px;    /* 제품 이미지 영역 크기 */

  /* 타이포그래피 */
  --cpCarousel-title-component: 40px;     /* 섹션 타이틀 */
  --cpCarousel-title-list:      22px;     /* 리스트 항목 제목 */
  --cpCarousel-title-sub:       20px;     /* 서브 타이틀 */
  --cpCarousel-title-minHeight: 5.9925vw; /* 타이틀 최소 높이 (유동) */
  --cpCarousel-fontsize-description: 16px;
  --cpCarousel-fontsize-price:  20px;
  --cpCarousel-fontsize-flag:   16px;
  --cpCarousel-fontsize-date:   12px;

  /* 간격 */
  --cpCarousel-gap-innr:   60px;      /* 내부 좌우 여백 */
  --cpCarousel-gap-swiper: 1.9975vw;  /* 슬라이드 간격 (유동) */
  --cpCarousel-gap-price:  8px;       /* 가격 요소 간격 */
  --cpCarousel-gap-flag:   16px;      /* 플래그 간격 */
}
```

### Swiper.js 변수

```css
:root {
  --swiper-navigation-color: #ffffff;
  --swiper-navigation-size:  44px;
  --swiper-pagination-color: #ffffff;
  --swiper-preloader-color:  #fff;
  --swiper-theme-color:      #007aff;
}
```

---

## 10. Motion

| Pattern | Value | Use |
|---|---|---|
| Swiper transition | CSS transform (Swiper.js 기본) | carousel 슬라이드 |
| hover (일반) | transition 없음 또는 subtle | 링크, 버튼 |
| GNB overlay | --gnb04-top 토큰 제어 | 네비게이션 슬라이드 |

---

## 11. Layout Patterns

### Grid System

- **Content max-width**: `1920px` (carousel 기준)
- **Container pattern**: `max-width: 1920px; margin: 0 auto`
- **Grid type**: CSS Flex + Swiper carousel 혼합
- **Gutter**: `24px` 기본, 대형 섹션 `60px`

### Hero / Carousel Pattern

- **Pattern Summary**: 풀블리드 Swiper carousel + 제품 이미지 중심 + 삼성 블루 CTA
- Background: `#ffffff` 또는 제품 배경 이미지
- Title: `Samsung Sharp Sans bold 40px color #212425`
- Sub: `Samsung Sharp Sans 400 16px color #707070`
- CTA: `bg #2189FF color #fff radius 10px`
- Picture area: `312px` 고정 (--cpCarousel-size-picture)

### Navigation Structure

- **Type**: sticky GNB (`position: sticky; --gnb04-top: 0`)
- **Background**: `#ffffff`
- **Active**: `--themeColorActive: #000` (active 탭)
- **Utility height**: `--gnb04-utility-user-height: 0` (로그인/유틸리티 바)

---

## 12. Responsive Behavior

### Breakpoints (관찰)

| Name | Behavior |
|---|---|
| Mobile (`< 768px`) | 1-column, 햄버거 GNB |
| Tablet (`≥ 768px`) | 2-column carousel |
| Desktop (`≥ 1024px`) | full GNB, 3+ column |
| Wide (`≥ 1440px`) | max layout, vw 스케일 |

### vw 기반 유동 값

- `border-radius: 1.3889vw` → 20px at 1440px
- `border-radius: 1.8182vw` → 26px at 1440px
- `gap: 1.9975vw` → 29px at 1440px
- `min-height: 5.9925vw` → 86px at 1440px

---

## 13. Components

### CTA Buttons

| Variant | background | color | radius | padding |
|---|---|---|---|---|
| primary | `#2189FF` | `#ffffff` | `10px` | `12px 24px` |
| outline | `transparent` | `#2189FF` | `10px` | `11px 23px` + `1px solid #2189FF` |
| text link | `transparent` | `#2189FF` | `0` | `0` |

### Product Card (Carousel)

```html
<div class="rvmp-cmpnt cp-carousel-*">
  <div class="txt-area">
    <h3 class="title">제품명</h3>
    <p class="description">설명</p>
    <span class="price">₩1,290,000</span>
  </div>
  <div class="img-area" style="height: var(--cpCarousel-size-picture)">
    <img src="..." />
  </div>
</div>
```

- bg: `#ffffff` 또는 `#F7F7F7`
- radius: `20px`
- padding: `24px`
- title: `Samsung Sharp Sans bold 22px color #212425`
- price: `Samsung Sharp Sans bold 20px color #212425`

### Navigation (GNB)

- 배경: `#ffffff`
- 높이: sticky, `--gnb04-top: 0`
- 링크: `Samsung Sharp Sans 400 color #707070` → active `color #000000`
- 하단 active indicator: `--themeColorActive: #000`

### Forms / Input

- height: `44px`
- border: `1px solid #D9D9D9`
- radius: `10px`
- bg: `#ffffff`
- focus: `border-color: #2189FF`
- placeholder: `color: #8F8F8F`

---

## 14. Drop-in CSS

```css
/* Samsung Electronics — copy into your root stylesheet */
:root {
  /* Fonts */
  --samsung-font-primary: 'Samsung Sharp Sans', 'SamsungOneKorean', Dotum, 'Apple SD Gothic Neo', Arial, sans-serif;
  --samsung-font-korean:  'SamsungOneKorean', dotum, sans-serif;

  /* Brand Blue */
  --samsung-brand:        #2189FF;
  --samsung-brand-navy:   #1428A0;
  --samsung-brand-link:   #006BEA;
  --samsung-error:        #FA2337;

  /* Text */
  --samsung-fg:           #212425;
  --samsung-fg-muted:     #707070;
  --samsung-fg-subtle:    #8F8F8F;
  --samsung-fg-disabled:  #B2B2B2;

  /* Surfaces */
  --samsung-bg:           #ffffff;
  --samsung-surface:      #F7F7F7;
  --samsung-surface-alt:  #FAFAFA;
  --samsung-border:       #D9D9D9;
  --samsung-border-light: #EBEBEB;

  /* Carousel tokens */
  --cpCarousel-size-picture:    312px;
  --cpCarousel-title-component: 40px;
  --cpCarousel-title-list:      22px;
  --cpCarousel-title-sub:       20px;
  --cpCarousel-title-minHeight: 5.9925vw;
  --cpCarousel-fontsize-description: 16px;
  --cpCarousel-fontsize-price:  20px;
  --cpCarousel-fontsize-flag:   16px;
  --cpCarousel-fontsize-date:   12px;
  --cpCarousel-gap-innr:        60px;
  --cpCarousel-gap-swiper:      1.9975vw;
  --cpCarousel-gap-price:       8px;
  --cpCarousel-gap-flag:        16px;

  /* Radius */
  --samsung-radius-none: 0;
  --samsung-radius-sm:   6px;
  --samsung-radius-md:   10px;
  --samsung-radius-lg:   20px;
  --samsung-radius-full: 50%;
  --samsung-radius-fluid: 1.3889vw;

  /* Spacing */
  --samsung-space-xs:  4px;
  --samsung-space-sm:  12px;
  --samsung-space-md:  24px;
  --samsung-space-lg:  36px;
  --samsung-space-xl:  60px;
}
```

---

## 15. Tailwind Config

```js
// tailwind.config.js — Samsung Electronics
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#2189FF',
          navy:    '#1428A0',
          link:    '#006BEA',
          dark:    '#0370FF',
        },
        neutral: {
          0:    '#ffffff',
          50:   '#FAFAFA',
          100:  '#F7F7F7',
          150:  '#F5F5F5',
          200:  '#EBEBEB',
          250:  '#E4E4E4',
          300:  '#D9D9D9',
          350:  '#DDDDDD',
          400:  '#B2B2B2',
          450:  '#A6A6A6',
          500:  '#8F8F8F',
          550:  '#757575',
          600:  '#707070',
          700:  '#313131',
          800:  '#1C1C1C',
          900:  '#212425',
          1000: '#000000',
        },
        error:   '#FA2337',
      },
      fontFamily: {
        sans:   ["'Samsung Sharp Sans'", "'SamsungOneKorean'", 'Dotum', "'Apple SD Gothic Neo'", 'Arial', 'sans-serif'],
        korean: ["'SamsungOneKorean'", 'dotum', 'sans-serif'],
      },
      borderRadius: {
        'none':  '0',
        'sm':    '6px',
        DEFAULT: '10px',
        'lg':    '20px',
        'full':  '50%',
      },
      screens: {
        sm:  '768px',
        md:  '1024px',
        lg:  '1280px',
        xl:  '1440px',
        '2xl': '1920px',
      },
    },
  },
};
```

---

## 16. Agent Prompt Guide

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | `--samsung-brand` | `#2189FF` |
| Background | `--samsung-bg` | `#ffffff` |
| Surface | `--samsung-surface` | `#F7F7F7` |
| Text heading | `--samsung-fg` | `#212425` |
| Text muted | `--samsung-fg-muted` | `#707070` |
| Text subtle | `--samsung-fg-subtle` | `#8F8F8F` |
| Border | `--samsung-border` | `#D9D9D9` |
| Error | `--samsung-error` | `#FA2337` |
| Navy accent | `--samsung-brand-navy` | `#1428A0` |

### Example Component Prompts

#### Hero Carousel

```
Samsung 스타일 히어로 carousel 섹션.
- 배경: #ffffff (흰 배경, 제품 이미지가 주인공)
- 타이틀: Samsung Sharp Sans bold 40px color #212425
- 서브: Samsung Sharp Sans 400 16px color #707070
- 제품 이미지 영역: 312px (--cpCarousel-size-picture)
- Primary CTA: bg #2189FF color #fff radius 10px padding 12px 24px
- Swiper carousel: --swiper-navigation-color #ffffff
- max-width 1920px margin 0 auto
```

#### Product Card

```
Samsung 제품 카드.
- bg #ffffff, border 1px solid #D9D9D9, radius 20px
- padding 24px
- 이미지: aspect-ratio 1/1, radius 10px
- 제품명: Samsung Sharp Sans bold 22px color #212425
- 설명: 400 16px color #707070
- 가격: bold 20px color #212425
- CTA: bg #2189FF color #fff radius 10px
```

#### Navigation (GNB)

```
Samsung 상단 GNB.
- position sticky top 0
- bg #ffffff
- 링크: Samsung Sharp Sans 400 color #707070
  active: color #000000
- 하단 active indicator 2px solid #000000
```

### Iteration Guide

- **색상 변경 시**: `--samsung-*` semantic token 사용. 블루 `#2189FF`는 CTA/링크에만.
- **폰트 변경 시**: Samsung Sharp Sans 대체 → `Inter` 또는 `Pretendard`. 한국어 → `Noto Sans KR`.
- **carousel 조정 시**: `--cpCarousel-*` 토큰만 수정. 직접 값 하드코딩 금지.
- **radius 조정 시**: `20px`(카드) / `10px`(버튼) / `50%`(아이콘) 3단계.
- **반응형**: 768 / 1024 / 1280 / 1440 / 1920 5단계. vw 단위 적극 활용.

---

## 17. DO / DON'T

### DO

- 배경은 `#ffffff` 또는 `#F7F7F7` — 제품 이미지가 주인공.
- 브랜드 블루 `#2189FF`는 CTA 버튼, 링크, active badge에만.
- 카드 radius는 `20px` — Samsung의 부드러운 소비자 친화적 모서리.
- carousel 시스템은 `--cpCarousel-*` 토큰으로만 제어.
- vw 단위 사용 (`1.3889vw`, `1.9975vw`) — 다양한 화면 일관성.
- body text `#707070` / heading `#212425`.
- 버튼 height `44px` — 터치 타겟 최소 기준.
- 폰트 bold/700은 헤드라인과 가격에만.

### DON'T

- `#2189FF`를 배경 면적으로 쓰지 말 것 — 정보 페이지가 된다.
- 에러 레드 `#FA2337`을 디자인 accent로 쓰지 말 것 — 오류 상태 전용.
- radius를 `0`으로 모든 요소에 적용하지 말 것 — Samsung은 항상 부드럽다.
- Swiper.js 없이 carousel 직접 구현 시 `--swiper-*` 변수 참조 금지.
- 딥 네이비 `#1428A0`을 primary CTA에 쓰지 말 것 — dark 섹션 accent 전용.
- `border-radius: 100px` 이상 사용 금지 — `50%` 또는 `20px`이 상한.
- 중간 회색 `#707070`을 헤드라인 텍스트에 쓰지 말 것 — body/caption 전용.
