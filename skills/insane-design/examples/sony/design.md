---
slug: sony
service_name: Sony
site_url: https://www.sony.com
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#000000"
primary_font: SST W20 Roman
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Sony (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Sony의 디지털 인터페이스는 다크 테마를 기반으로 한다. 어두운 배경 위에 밝은 텍스트와 브랜드 컬러 `#000000`가 돋보이는 구성으로, 시각적 몰입감과 프리미엄 분위기를 동시에 전달한다.

색상 전략은 브랜드 컬러 `#000000`를 중심으로 미니멀하게 구성된다. 불필요한 장식색 없이 핵심 인터랙션에만 컬러를 집중시킨다.

타이포그래피는 `SST W20 Roman` 폰트를 중심으로 브랜드 고유의 성격을 표현한다. 기본 weight 400으로 본문을 구성하며, heading에서 더 무거운 weight를 사용해 시각적 위계를 만든다.

레이아웃은 풀 너비 히어로 섹션과 콘텐츠 영역의 리듬감 있는 교차로 구성된다. 충분한 여백을 활용하여 콘텐츠에 시각적 호흡 공간을 부여하고, 핵심 메시지와 CTA에 자연스럽게 시선을 유도한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Sony처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "SST W20 Roman", "SST W55 Regular", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #000000; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #000000; }
```

**절대 하지 말아야 할 것 하나**: Sony UI에 파란색(기존 브랜드 컬러 #003087)을 넣는 것. 현재 Sony 마케팅 사이트는 블랙 기반 dark 테마가 주류이며, 파랑은 PlayStation 등 서브브랜드에만 존재한다. 기본 Sony.com UI는 흑백 모노크롬이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.sony.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | SST 폰트 패밀리 다수, FontAwesome, Swiper, OneTrust |
| Token prefix | N/A (CSS 커스텀 프로퍼티 미발견) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (글로벌 제품 사이트)
- **Design system**: Bespoke — SST 전용 폰트 패밀리, dark 테마 중심
- **CSS architecture**: Flat CSS, 폰트 weight를 별도 파일로 분리
  ```
  core  (직접 hex 값)        텍스트·배경·아이콘
  comp  (FontAwesome, Swiper) UI 라이브러리
  ```
- **Class naming**: 기능적 클래스 (Swiper, FontAwesome 혼용)
- **Default theme**: dark (bg = `#000000`)
- **Font loading**: 셀프 호스트 — `SST W20 Roman`, `SST W20 Bold`, `SST W20 Light` 등 8종 이상
- **Canonical anchor**: `#000000` — 기본 다크 배경

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `SST W20 Bold` (Sony 독점 라이선스)
- **Body font**: `SST W20 Roman` (Sony 독점)
- **Light font**: `SST W20 Light`
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-body:    "SST W20 Roman", "SST W55 Regular", Arial, sans-serif;
  --font-bold:    "SST W20 Bold", "SST W55 Bold", Arial, sans-serif;
  --font-light:   "SST W20 Light", Arial, sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold:   700;
}
body {
  font-family: var(--font-body);
  font-weight: var(--font-weight-normal);
}
```

> **라이선스 주의**: `SST` (Sharp Sans Text) 시리즈는 Sony 독점 폰트. 대체재로 `Sharp Grotesk` 또는 `Helvetica Neue` 사용.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| display | 4rem | 700 | 1.05 | -0.02em |
| heading-l | 2.5rem | 700 | 1.1 | -0.01em |
| heading-m | 1.75rem | 700 | 1.2 | 0 |
| heading-s | 1.25rem | 600 | 1.3 | 0 |
| body | 1rem | 400 | 1.6 | 0 |
| small | 0.875rem | 400 | 1.55 | 0 |
| caption | 0.75rem | 400 | 1.5 | 0.02em |
| spec | 0.8125rem | 500 | 1.4 | 0 |

> ⚠️ Sony는 SST 폰트를 weight별 별도 파일로 관리한다. `font-weight: 700`이 아니라 `font-family: "SST W20 Bold"`로 굵기를 제어하는 패턴.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp — Monochrome (5 steps)
<!-- color_system: monochrome — Sony의 기본 컬러는 흑백 -->

| Token | Hex |
|---|---|
| brand-black | #000000 |
| brand-dark | #1A1A1A |
| brand-mid | #555555 |
| brand-light | #CCCCCC |
| brand-white | #FFFFFF |

### 06-3. Neutral Ramp

| Step | Dark theme | Light theme |
|---|---|---|
| 0 | #000000 | #FFFFFF |
| 100 | #1A1A1A | #F5F5F5 |
| 200 | #2A2A2A | #E0E0E0 |
| 400 | #555555 | #9E9E9E |
| 700 | #9E9E9E | #555555 |
| 900 | #CCCCCC | #1A1A1A |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| bg-dark | #000000 | 기본 dark 배경 |
| bg-surface | #1A1A1A | 카드·섹션 배경 |
| fg-primary | #FFFFFF | 주 텍스트 |
| fg-secondary | #CCCCCC | 보조 텍스트 |
| border | #2A2A2A | dark 구분선 |
| btn-primary-bg | #FFFFFF | 주 CTA 배경 (dark bg에서) |
| btn-primary-fg | #000000 | 주 CTA 텍스트 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | #FFFFFF | 높음 | 텍스트 (dark bg에서) |
| 2 | #555555 | 높음 | 보조 텍스트 |
| 3 | #000000 | 높음 | 배경·CTA |
| 4 | #BBBBBB | 낮음 | OneTrust 테두리 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| space-xs | 4px | 미세 간격 |
| space-sm | 8px | 컴포넌트 내부 |
| space-md | 16px | 섹션 내 |
| space-lg | 32px | 섹션 간 |
| space-xl | 64px | 페이지 레벨 |
| space-xxl | 96px | 대형 영역 |

**주요 alias**:
- `space-lg` → 32px (기본 섹션 패딩)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-none | 0px | 기본 버튼·카드 |
| radius-sm | 4px | 배지·태그 |
| radius-md | 8px | 모달·드롭다운 |
| radius-full | 999px | 원형 아이콘 버튼 |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| shadow-sm | 0 1px 4px rgba(0,0,0,0.30) | dark 카드 (높은 불투명도) |
| shadow-md | 0 4px 16px rgba(0,0,0,0.40) | dark 드롭다운 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

### Hero
- Layout: 전체폭 dark, 중앙 또는 좌측 텍스트 + 제품 이미지
- Background: #000000
- H1: `4rem` / weight `700` / tracking `-0.02em`
- Max-width: 1440px

### Section Rhythm
```css
section {
  padding: 64px 40px;
  max-width: 1440px;
  background: #000000;
}
```

---

## 12. Responsive Behavior
<!-- SOURCE: manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | 0–767px | 단일 컬럼, 스택 레이아웃 |
| Tablet | 768–1023px | 2컬럼 그리드, 축소된 네비게이션 |
| Desktop | 1024–1439px | 풀 레이아웃, 사이드바 표시 |
| Large | 1440px+ | 최대 너비 제한, 중앙 정렬 |

### Collapsing Strategy
- **Navigation**: 데스크톱 수평 메뉴 → 모바일 햄버거 메뉴
- **Grid columns**: 데스크톱 다중 컬럼 → 모바일 단일 컬럼 스택
- **Hero layout**: 데스크톱 가로 배치 → 모바일 세로 스택

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Primary Button (Dark Theme)

```html
<button class="btn btn--primary">
  Buy Now
</button>
```

| Spec | Value |
|---|---|
| background | #FFFFFF |
| color | #000000 |
| padding | 14px 28px |
| border-radius | 0px |
| font-family | "SST W20 Bold" |
| font-weight | 700 |
| text-transform | none |

### Product Card (Dark)

```html
<div class="product-card">
  <div class="product-card__image">
    <img src="camera.jpg" alt="Alpha 7R V">
  </div>
  <div class="product-card__info">
    <p class="product-card__category">Cameras</p>
    <h3 class="product-card__name">Alpha 7R V</h3>
    <p class="product-card__price">$3,499.99</p>
  </div>
</div>
```

| Spec | Value |
|---|---|
| background | #1A1A1A |
| border | 1px solid #2A2A2A |
| border-radius | 0px |
| category color | #9E9E9E |
| name weight | 700 |
| price weight | 600 |

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 제품 중심, 기술 명세 강조 | "Unparalleled image quality." |
| Primary CTA | 동사구, 간결 | "Buy Now" |
| Secondary CTA | 소문자, 링크형 | "Learn more" |
| Subheading | 기술 스펙 설명 | |
| Tone | 기술적 권위, 간결 명료, 과장 적절히 허용 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Sony — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: "SST W20 Roman", "SST W55 Regular", Arial, sans-serif;
  --font-family-bold: "SST W20 Bold", "SST W55 Bold", Arial, sans-serif;
  --font-family-code: ui-monospace, monospace;
  --font-weight-normal: 400;
  --font-weight-bold:   700;

  /* Brand (anchor + 4 steps) — monochrome */
  --color-brand-25:  #F5F5F5;
  --color-brand-300: #9E9E9E;
  --color-brand-500: #555555;
  --color-brand-600: #000000;   /* ← canonical */
  --color-brand-900: #000000;

  /* Surfaces (dark default) */
  --bg-page:   #000000;
  --bg-surface:#1A1A1A;
  --bg-dark:   #000000;
  --text:      #FFFFFF;
  --text-muted:#CCCCCC;

  /* Key spacing */
  --space-sm:  8px;
  --space-md:  16px;
  --space-lg:  32px;

  /* Radius */
  --radius-sm: 0px;
  --radius-md: 4px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Sony
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '#F5F5F5',
          300: '#9E9E9E',
          500: '#555555',
          600: '#000000',
          900: '#000000',
        },
        neutral: {
          0:   '#000000',
          100: '#1A1A1A',
          200: '#2A2A2A',
          400: '#555555',
          700: '#9E9E9E',
          900: '#CCCCCC',
        },
      },
      fontFamily: {
        sans: ['"SST W20 Roman"', '"SST W55 Regular"', 'Arial', 'sans-serif'],
        bold: ['"SST W20 Bold"', '"SST W55 Bold"', 'Arial', 'sans-serif'],
        mono: ['ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        bold:   '700',
      },
      borderRadius: {
        'none': '0px',
        'sm':   '4px',
        'md':   '8px',
      },
      boxShadow: {
        'sm': '0 1px 4px rgba(0,0,0,0.30)',
        'md': '0 4px 16px rgba(0,0,0,0.40)',
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
| Brand primary | brand | `#000000` |
| Background | bg-page | `#000000` |
| Text primary | text | `#FFFFFF` |
| Text muted | text-muted | `#CCCCCC` |
| Border | border | `#E0E0E0` |

### Example Component Prompts

#### Hero Section
```
Sony 스타일 히어로 섹션을 만들어줘.
- 배경: #000000
- H1: SST W20 Roman, weight 700
- 서브텍스트: #CCCCCC
- CTA 버튼: 배경 #000000, 텍스트 white
```

#### Card Component
```
Sony 스타일 카드 컴포넌트를 만들어줘.
- 배경: #000000, border: 1px solid #E0E0E0
- radius: 0px
- 제목: SST W20 Roman, 16px, weight 700
- 본문: 14px, color #FFFFFF
```

### Iteration Guide

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight 400이 기본. heading에만 더 무거운 weight.
- **여백 조정 시**: §07의 spacing scale 단위로만. 임의 값(13px, 27px 등) 금지.
- **새 컴포넌트 추가 시**: §13의 기존 패턴(radius, shadow, border 스타일)을 따를 것.
- **반응형**: §12의 breakpoint를 그대로 사용. 커스텀 breakpoint 추가 금지.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 기본 배경은 `#000000`(pure black)으로 설정한다
- dark 배경에서 primary CTA는 `background: #FFFFFF`, `color: #000000`
- heading은 `font-family: "SST W20 Bold"`로 별도 지정한다
- 제품 이미지 배경은 `#000000` 또는 `#1A1A1A` 유지
- 그림자는 불투명도를 30% 이상으로 설정한다 (dark 배경에서 가시성)

### ❌ DON'T
- 파란색을 기본 Sony.com UI에 넣지 않는다 — PlayStation 서브브랜드 전용
- `font-weight: 700`만으로 굵기를 조절하지 않는다 — SST Bold 폰트 파일 사용
- 배경을 밝은 회색(`#F5F5F5`)으로 두지 않는다 — Sony는 dark 테마 기본
- 불필요한 색상 악센트를 UI에 추가하지 않는다 — 모노크롬 시스템
- `border-radius`에 큰 값(16px 이상)을 버튼에 쓰지 않는다
