---
slug: contentful
service_name: Contentful
site_url: https://www.contentful.com
fetched_at: 2026-04-11
default_theme: light
brand_color: "#1770E6"
primary_font: Avenir Next
font_weight_normal: 400
token_prefix: f36
---

# DESIGN.md — Contentful (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Contentful처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — Avenir Next + system fallback */
body {
  font-family: "Avenir Next", "Segoe UI", -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
  font-weight: 400;
}

/* 2. 라이트 배경 + dark text */
:root { --bg: #FFFFFF; --bg-muted: #EFF2F6; --fg: #2B2D31; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 royal blue */
:root { --brand: #1770E6; --brand-navy: #2C407D; }
```

**절대 하지 말아야 할 것 하나**: Contentful의 브랜드는 **royal blue `#1770E6`** (HSL 215°)다. cyan-계열 `#0286C3`는 완전히 다른 hue로, 잘못 쓰면 즉시 "Contentful이 아닌 것"처럼 보인다. 또한 **earth-tone accent palette** (`#A86451`, `#587D69`, `#8A724D`)가 일러스트레이션의 브랜드 자산이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.contentful.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| CSS files | 20개 번들 · 108,558자 |
| Custom properties | **0개** (CSS var 시스템 미적용) |
| Unique hex | 48개 |
| Method | 하드코딩 hex 직접 파싱 · AI 추론 없음 |

> **중요**: 이 마케팅 페이지에는 **CSS 변수가 0개**입니다. Contentful의 공식 디자인 시스템은 **Forma 36** (`@contentful/forma-36`)이지만 홈페이지에는 적용되어 있지 않고, 모든 색이 하드코딩 hex로 존재합니다. 앱 UI를 재현하려면 Forma 36 레포를 별도 참조해야 합니다.

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: 정적 마케팅 사이트 (Next.js SSG 추정)
- **Design system**: Forma 36 (앱 전용, `--f36-*` prefix) — **홈페이지에는 미적용**
- **CSS architecture**: 커스텀 프로퍼티 없음. 모든 색/간격이 하드코딩 hex
- **Class naming**: 일반 BEM + CSS module hash
- **Default theme**: light (bg `#FFFFFF`)
- **Font loading**: `Avenir Next` 단 1회 선언 (대부분 system font 폴백)
- **Canonical anchor**: `#1770E6` — royal blue brand color

> **앱 UI vs 마케팅 사이트**: Contentful의 앱(web app.contentful.com)은 Forma 36 기반의 풍부한 토큰 시스템을 사용하지만, 마케팅 홈페이지는 정적 이미지 + 하드코딩 CSS라 토큰 레이어가 없습니다. **본 문서는 마케팅 사이트 기준**.

---

## 04. Font Stack
<!-- SOURCE: auto -->

- **Primary**: `Avenir Next` (Adobe Fonts / 유료)
- **Fallback**: `Segoe UI`, `-apple-system`, `BlinkMacSystemFont`, `Helvetica Neue`, sans-serif
- **Weight observed**: `600` (CSS 내), 실제 랜더링에서 300~700 범위 사용

```css
body {
  font-family: "Avenir Next", "Segoe UI", -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
  font-weight: 400;
}
h1, h2, h3 { font-weight: 600; }
```

> Avenir Next는 유료 폰트. 오픈소스 대체 후보: `Nunito Sans`, `Be Vietnam Pro`, `Mulish` (geometric sans 계열 중 Avenir 인상 가장 가까움).

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Size | px | Freq | Usage |
|---|---|---|---|
| 16px | 16 | 8 | body text (최다) |
| 14px | 14 | 7 | small body / label |
| 32px | 32 | 3 | h1 / feature title |
| 20px | 20 | 3 | h3 / sub-heading |
| 12px | 12 | 3 | caption / meta |
| 26px | 26 | 2 | h2 |
| 22px | 22 | 2 | h3 alternate |
| 40px | 40 | 2 | hero display |
| 72px | 72 | 2 | hero xxl |
| 48px | 48 | 1 | section title |
| 56px | 56 | 1 | feature display |
| 64px | 64 | 1 | hero large |
| 96px | 96 | 1 | mega display |
| 18px | 18 | 1 | lead text |

> ⚠️ 16px base + 14px dense. 헤딩은 20 / 26 / 32 / 40 / 72 / 96px의 **non-modular 스케일** (1.25x 비율 아님 — 마케팅 히어로 중심).

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Blue
| Hex | Count | Role |
|---|---|---|
| `#1770E6` | 84 | ⭐ **primary royal blue** — CTA / link / logo |
| `#1770E5` | 19 | 1-off variant (compression noise) |
| `#2C407D` | 26 | navy — dark variant / footer |
| `#2E3F70` | 8 | navy deeper |
| `#3D4266` | 6 | navy darkest |

### 06-3. Neutral Ramp
| Hex | Count | Role |
|---|---|---|
| `#FFFFFF` | 41 | page bg |
| `#EFF2F6` | 8 | sidebar / section bg |
| `#DDE5EC` | 7 | border light |
| `#C4D1DE` | 6 | border mid |
| `#6D7682` | 3 | text muted |
| `#55575B` | 5 | text subtle |
| `#2B2D31` | 62 | dark text primary |
| `#000000` | 13 | logo / stroke |

### 06-4. Earth-tone Accent Palette
<!-- SOURCE: auto -->
<!-- Contentful의 signature: 일러스트레이션에 사용되는 따뜻한 earth-tone palette -->

| Hex | Count | Category | Usage |
|---|---|---|---|
| `#A86451` | 10 | terracotta | illustration skin / warmth |
| `#965642` | 6 | terracotta deep | illustration shadow |
| `#BA5A3F` | 6 | orange brick | warm accent |
| `#8A724D` | 8 | khaki | muted warm |
| `#877256` | 4 | khaki deep | illustration mid |
| `#587D69` | 8 | sage green | cool accent |
| `#395E4A` | 10 | forest green | deep green |
| `#5F7B7D` | 4 | teal gray | cool muted |
| `#4A6E70` | 20 | teal dark | subtle divider |
| `#54768E` | 10 | slate blue | muted blue |

> **중요**: 이 earth-tone palette는 Contentful의 signature 일러스트레이션 색. 플로렌틴/테라코타/세이지 계열로 "구조화된 웜톤" 인상을 만듭니다. UI에는 거의 안 쓰이고 **히어로 일러스트와 아이콘**에 집중 등장.

### 06-5. Semantic
| Category | Hex | Usage |
|---|---|---|
| success | `#D8F6E7` | 성공 배경 |
| error | `#914040` | 에러 텍스트 |
| purple accent | `#5D4985`, `#6B3B53`, `#9C6580` | tertiary highlight |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#1770E6` | 84 | **brand blue** |
| 2 | `#2B2D31` | 62 | dark text |
| 3 | `#FFFFFF` | 41 | page bg |
| 4 | `#2C407D` | 26 | navy |
| 5 | `#4A6E70` | 20 | teal dark |
| 6 | `#1770E5` | 19 | blue variant |
| 7 | `#000000` | 13 | logo |
| 8 | `#395E4A` | 10 | forest green |
| 9 | `#A86451` | 10 | terracotta |
| 10 | `#54768E` | 10 | slate blue |

---

## 07. Spacing
<!-- SOURCE: auto -->
<!-- 커스텀 프로퍼티 0개. 모든 spacing이 하드코딩. -->

추정 scale (일반 marketing 사이트 기준):

| Step | px | Use case |
|---|---|---|
| xs | 4 | icon gap |
| sm | 8 | button inset |
| md | 16 | card padding |
| lg | 24 | section internal |
| xl | 32 | section gap |
| 2xl | 48 | block rhythm |
| 3xl | 64 | hero padding |
| 4xl | 96 | page rhythm |

---

## 08. Radius
<!-- SOURCE: auto -->

| Value | Count | Context |
|---|---|---|
| `4px` | 1 | button / input |
| `8px` | 1 | card / panel |

> Contentful은 radius 2종만 사용. 매우 conservative한 geometric 감성.

---

## 09. Shadows
<!-- SOURCE: auto -->

| Value | Count | Usage |
|---|---|---|
| `0 0 7px rgba(0,0,0,.35)` | 2 | soft glow |
| `0 5px 10px 0 rgba(0,0,0,.15)` | 1 | card elevation |
| `0 4px 10px 0 rgba(0,0,0,.10)` | 1 | subtle lift |
| `0 0 1px rgba(255,255,255,.5)` | 1 | inner highlight |

> 4개 raw 값만 존재. 모두 단일 레이어. Clerk/Stripe의 dual/triple-layer와 대비되는 simple shadow 시스템.

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary CTA
- **Background**: `#1770E6` (royal blue)
- **Text**: `#FFFFFF`
- **Radius**: `4px` or `8px`
- **Font**: Avenir Next 16px / 600
- **Padding**: `12px 24px`

```html
<a class="cta cta--primary">Start free trial</a>
```

### Secondary CTA
- **Background**: transparent
- **Text**: `#1770E6`
- **Border**: `1px solid #1770E6`
- **Hover**: bg `#EFF2F6`

### Navigation
- **Background**: `#FFFFFF`
- **Border bottom**: `1px solid #DDE5EC`
- **Link**: `#2B2D31` default, `#1770E6` hover
- **CTA slot**: primary blue button

### Content panel (marketing feature card)
- **Background**: `#FFFFFF`
- **Border**: none (shadow only)
- **Shadow**: `0 5px 10px rgba(0,0,0,.15)`
- **Radius**: `8px`
- **Padding**: `32px 40px`

### Hero illustration
- Earth-tone palette 사용: terracotta `#A86451`, sage `#587D69`, khaki `#8A724D`
- 배경: `#EFF2F6` 또는 `#FFFFFF`
- 브랜드 블루 `#1770E6`는 CTA에만

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Contentful — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-sans: "Avenir Next", "Segoe UI", -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;

  /* Brand blue */
  --brand:       #1770E6;
  --brand-navy:  #2C407D;
  --brand-deep:  #2E3F70;

  /* Surface */
  --bg:          #FFFFFF;
  --bg-sunken:   #EFF2F6;
  --bg-section:  #DDE5EC;

  /* Text */
  --text:        #2B2D31;
  --text-subtle: #55575B;
  --text-muted:  #6D7682;

  /* Border */
  --border:      #DDE5EC;
  --border-mid:  #C4D1DE;

  /* Earth-tone (일러스트레이션용) */
  --illu-terracotta:  #A86451;
  --illu-orange:      #BA5A3F;
  --illu-khaki:       #8A724D;
  --illu-sage:        #587D69;
  --illu-forest:      #395E4A;
  --illu-slate:       #54768E;
  --illu-teal:        #4A6E70;

  /* Radius (2-step only) */
  --radius-sm: 4px;
  --radius-md: 8px;

  /* Shadow */
  --shadow-sm: 0 4px 10px rgba(0,0,0,0.10);
  --shadow-md: 0 5px 10px rgba(0,0,0,0.15);
}

body {
  font-family: var(--font-sans);
  background: var(--bg);
  color: var(--text);
}
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Contentful
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#1770E6',
          navy:    '#2C407D',
          deep:    '#2E3F70',
          darkest: '#3D4266',
        },
        neutral: {
          0:   '#FFFFFF',
          50:  '#EFF2F6',
          100: '#DDE5EC',
          200: '#C4D1DE',
          500: '#6D7682',
          600: '#55575B',
          800: '#2B2D31',
          950: '#000000',
        },
        illustration: {
          terracotta: '#A86451',
          brick:      '#BA5A3F',
          khaki:      '#8A724D',
          sage:       '#587D69',
          forest:     '#395E4A',
          slate:      '#54768E',
          teal:       '#4A6E70',
        },
      },
      fontFamily: {
        sans: ['"Avenir Next"', '"Segoe UI"', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
      },
      borderRadius: {
        DEFAULT: '4px',
        sm:      '4px',
        md:      '8px',
      },
      boxShadow: {
        sm: '0 4px 10px rgba(0,0,0,0.10)',
        md: '0 5px 10px rgba(0,0,0,0.15)',
        glow: '0 0 7px rgba(0,0,0,0.35)',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- **Royal blue** `#1770E6` (HSL 215°)을 브랜드 컬러로 사용. CTA, link, logo 모두 이 값.
- Navy `#2C407D` / `#2E3F70`을 darker variant로 사용 (footer, 헤더 텍스트).
- **Earth-tone accent palette**을 일러스트레이션/히어로 이미지에 사용: terracotta `#A86451`, sage `#587D69`, khaki `#8A724D`.
- Dark text는 `#2B2D31` (pure gray, blue-tint 없음).
- Surface는 `#FFFFFF` page + `#EFF2F6` sunken + `#DDE5EC` border 3-step.
- `Avenir Next` 폰트 + system fallback (Segoe UI, -apple-system).
- Radius는 `4px` (button) / `8px` (card) 2종만.
- Simple single-layer shadow (`0 5px 10px rgba(0,0,0,.15)`).

### ❌ DON'T
- ❌ **Cyan-계열 블루** (`#0286C3`, `#00AFCC` 등) — 실제 CSS에 0회. HSL 차이로 즉시 "Contentful 아님"처럼 보인다.
- ❌ Dark text를 `#1B1E28` 같은 blue-tinted로 — 실제는 순수 gray `#2B2D31`.
- ❌ Avenir Next를 Inter/Roboto로 대체 — geometric 인상 다름.
- ❌ Earth-tone을 UI 브랜드 컬러로 사용 — 오직 일러스트레이션/아이콘 전용.
- ❌ Multi-layer dual shadow (Stripe/Clerk 계열) — Contentful은 single-layer.
- ❌ CSS variable 기반 토큰 시스템 기대 — 마케팅 홈페이지는 하드코딩 hex만 사용.
- ❌ `--f36-*` Forma 36 토큰을 마케팅 페이지에서 사용 — 앱 UI 전용. 마케팅은 Forma 36 미적용.
- ❌ 6-step+ radius 시스템 — Contentful은 2-step만 사용.
