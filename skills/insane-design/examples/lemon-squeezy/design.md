---
slug: lemon-squeezy
service_name: Lemon Squeezy
site_url: https://www.lemonsqueezy.com
fetched_at: 2026-04-11
default_theme: mixed
brand_color: "#5423E7"
primary_font: Circular Pro Book
font_weight_normal: 400
token_prefix: ls
---

# DESIGN.md — Lemon Squeezy (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Lemon Squeezy는 디지털 제품 판매 플랫폼으로, 다크 히어로와 라이트 피처 섹션이 교차하는 혼합 테마를 사용한다. 히어로는 다크 `#121217` 배경에 보라/핑크 그라디언트 orb가 드라마틱한 임팩트를 만들고, 피처 섹션은 라이트(`#F7F7F8`, `#F4F4F4`)로 전환되어 실용적 정보를 전달한다.

브랜드 보라 `#5423E7`과 레몬 옐로우 `#FFC233`의 대비가 핵심이다. 특히 노란 inset 밑줄(`inset 0 -2px 0 0 #FFC233`)은 Lemon Squeezy의 시그니처 디테일로, 일반 `text-decoration` 대신 box-shadow로 구현된다. Circular Pro Book의 둥근 terminal 획이 friendly-premium 톤을 만든다.

**Key Characteristics:**
- 다크/라이트 혼합 테마 — 히어로 다크, 피처 라이트 (라이트가 dominant)
- 브랜드 보라 `#5423E7` + 레몬 옐로우 `#FFC233` 시그니처 대비
- 노란 inset shadow 밑줄 — 링크/강조의 핵심 패턴
- Weight 500이 기본 강조값 (800/900은 거의 미사용)
- Radius 20px가 feature card 기본 (Webflow 빌더 출력)

---

## 01. Quick Start

> 5분 안에 Lemon Squeezy처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — Webflow Cloud Font로 Circular Pro Book 로드 */
body {
  font-family: "Circularpro book", "Circular Pro", "Inter", -apple-system, sans-serif;
  font-weight: 400;
}

/* 2. 라이트/다크 혼합 — 라이트 surface가 dominant */
:root {
  --bg-light:  #ffffff;
  --bg-soft:   #f7f7f8;
  --bg-dark:   #121217;
  --fg-dark:   #121217;
  --fg-muted:  #6c6c89;
  --border:    #d1d1db;
}

/* 3. 브랜드 — 진한 보라 + 레몬 노랑 */
:root {
  --brand-purple: #5423E7;
  --brand-purple-2: #7047eb;
  --brand-yellow: #ffc233;
  --brand-yellow-2: #ffd266;
}
```

**절대 하지 말아야 할 것 하나**: 브랜드 보라를 `#7C3AED` (Tailwind Violet-600)로 쓰지 말 것. 실제 Lemon Squeezy 보라는 훨씬 더 진한 **`#5423E7`** (12회 실사용)다. 둘 다 보라처럼 보이지만 L* 차이가 15 이상이라 나란히 놓으면 완전 다른 브랜드로 보인다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.lemonsqueezy.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| Framework | **Webflow** builder output |
| CSS custom props | 89 (color vars: 6 · spacing: 0 · shadow: 0) |
| Token prefix | `--ls-*` (제한적), 대부분 hardcoded |
| Method | CSS 커스텀 프로퍼티 + 인라인 hex 빈도 파싱 |

---

## 03. Tech Stack

- **Framework**: **Webflow** visual builder (자동 생성 클래스 `w-button`, `w-form`, `w-container`)
- **Design system**: 없음. Webflow editor에서 디자이너가 직접 지정한 값 + 6개의 수동 CSS 변수가 전부.
- **CSS architecture**: 하이브리드 — Webflow 유틸(`w-*`) + 디자이너 semantic 클래스(`button-primary`, `hero-headline`) 혼합
  ```
  --ls-color-*            디자이너가 만든 색 변수 (6개뿐)
  var(--ls-color-yellow)  var(--yellow-500)  노란색 계열
  나머지 색은 모두 hardcoded hex — 변수화 안 됨
  ```
- **Class naming**: `.w-button`, `.w-container`, `.button-primary`, `.hero-headline` 등 semantic + Webflow 유틸 혼합
- **Default theme**: **Mixed** — 홈 히어로는 다크 (`#121217`), 기능 섹션은 라이트 (`#f7f7f8`, `#f4f4f4`). 라이트 surface가 다크보다 빈도 더 높음
- **Font loading**: Webflow **Cloud Fonts** → Lineto Circular Pro Book (유료). 선언 형식은 `"Circularpro book,sans-serif"` (Webflow editor 저장 포맷)
- **Canonical anchor**: `#5423E7` 보라 (12회) + `#FFC233` 노랑 (5회)

---

## 04. Font Stack

- **Display / Body**: `Circular Pro Book` (Lineto 유료 폰트, Webflow Cloud Font로 로드)
- **Secondary / Form**: `Inter` — 폼 필드와 label에 한정적으로 사용
- **Code**: `JetBrains Mono`
- **Icon**: `webflow-icons` (Webflow 내장 아이콘 폰트)

```css
:root {
  --ls-font-display: "Circularpro book", "Circular Pro", "Inter", -apple-system, sans-serif;
  --ls-font-code:    "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;
}
body {
  font-family: var(--ls-font-display);
  font-weight: 400;
}
input, textarea, select {
  font-family: "Inter", var(--ls-font-display);
}
code, pre {
  font-family: var(--ls-font-code);
}
```

> ⚠️ **Circular Pro는 유료 Lineto 폰트**다. OSS 대체로는 **`Circular Std`** (비슷한 라이선스 이슈), 또는 **`TT Commons Pro`**, **`Visby CF`** 같은 geometric grotesque가 가장 가깝다. Inter로는 재현 불가 — Circular은 round terminal(터미널 획이 둥근 형태)이 시그너처.

---

## 05. Typography Scale

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| display-xl | `2.5rem` (40px) | 700 | 1.1  | -0.02em |
| display-lg | `2rem` (32px)   | 700 | 1.15 | -0.015em |
| display-md | `1.5rem` (24px) | 500 | 1.2  | -0.01em |
| body-lg    | `1rem` (16px)   | 500 | 1.5  | 0em |
| body-md    | `.9375rem` (15px) | 400 | 1.55 | 0em |
| body-sm    | `.875rem` (14px) | 400 | 1.5  | 0em |
| caption    | `14px`          | 400 | 1.4  | 0em |

> ⚠️ Weight 실제 분포: 500 (35회) > 400 (31회) > 700 (11회) > 600 (7회) > 300 (3회). **500 weight를 기본 강조**로 쓰는 패턴이 Lemon Squeezy 시그너처다. 800/900 heavy weight는 거의 없다.

---

## 06. Colors

### 06-1. Brand

| Token | Hex | Usage |
|---|---|---|
| brand-purple       | `#5423E7` | 주 브랜드 보라 (12회 실사용) |
| brand-purple-alt   | `#7047EB` | 보조 보라 (5회) |
| brand-pink         | `#F42AD3` | hero 그라디언트 강조 |
| `--ls-color-yellow`| `#FFC233` | 레몬 옐로우 (5회) |
| `--ls-color-yellow-lighter` | `#FFD266` | 밝은 옐로우 |

### 06-2. Dark Surface (hero section)

| Token | Hex |
|---|---|
| dark-bg            | `#121217` |
| `--dark-mode-bg-lighter` | `#141414` |
| dark-ink           | `#000000` |
| onDark-muted       | `#FFFFFF99` (α60) |
| onDark-hairline    | `#FFFFFF33` (α20) |

### 06-3. Light Surface (feature sections — dominant)

| Token | Hex |
|---|---|
| bg-page      | `#FFFFFF` |
| surface-1    | `#F7F7F8` |
| surface-2    | `#F4F4F4` |
| surface-3    | `#FAFAFA` |
| `--border-color` | `#D1D1DB` |
| `--bullet-point-color` | `#6C6C89` |
| ink          | `#121217` |

### 06-4. Semantic

| Token | Hex | Usage |
|---|---|---|
| button-primary-bg   | `#121217` | 다크 CTA |
| `--button-primary-light` | `#FFFFFFE6` | 라이트 모드 반전 CTA |
| link-underline      | `inset 0 -2px 0 0 #FFC233` | 링크 노랑 밑줄 |
| highlight-block     | `inset 0 -6px 0 -4px #FFD266` | 텍스트 하이라이트 |
| form-focus-blue     | `#3898EC` | Webflow 기본 focus (제거 권장) |

### 06-5. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF`   | 63 | bg / text onDark |
| 2 | `#00000000` | 39 | 투명 |
| 3 | `#000000`   | 16 | fg primary |
| 4 | `#121217`   | 14 | deep ink / dark bg |
| 5 | `#5423E7`   | 12 | **brand purple** |
| 6 | `#FFFFFF33` | 12 | α20 hairline onDark |
| 7 | `#FFFFFF99` | 11 | α60 muted onDark |
| 8 | `#F7F7F8`   | 10 | light surface-1 |
| 9 | `#FFFFFF00` |  9 | transparent white |
| 10| `#F4F4F4`   |  9 | light surface-2 |
| 11| `#6C6C89`   |  7 | muted text / bullet |
| 12| `#3898EC`   |  7 | Webflow default (non-brand) |

---

## 07. Spacing

Lemon Squeezy는 Webflow editor에서 디자이너가 직접 px/rem으로 지정. **spacing 커스텀 프로퍼티 0개**. 홈페이지 빈도 기반 권장 scale:

| Token | Value | Use case |
|---|---|---|
| space-1  | 4px   | tight |
| space-2  | 8px   | compact |
| space-3  | 12px  | button gap |
| space-4  | 16px  | card inner |
| space-5  | 20px  | list gap |
| space-6  | 24px  | section inner |
| space-7  | 32px  | block gap |
| space-8  | 48px  | section gap |
| space-9  | 64px  | hero padding |
| space-10 | 96px  | major section |

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| radius-sm   | 6px  | button, input |
| radius-md   | 8px  | small card |
| radius-lg   | 12px | card |
| radius-xl   | 20px | feature card (**가장 많음** — 7회) |
| radius-2xl  | 96px | hero blob |
| radius-3xl  | 200px | decorative circle |
| radius-pill | 100px | pill button |

---

## 09. Shadows

Webflow 빌더는 shadow를 변수화하지 않는다 (**0개**). 모든 그림자는 인라인.

| Level | Value | Usage |
|---|---|---|
| shadow-card      | `4px 0 6px #11112e0d, 0 10px 15px #11112e14` | 카드 elevation |
| highlight-underline | `inset 0 -2px 0 0 #FFC233`              | 링크 노랑 밑줄 |
| highlight-block  | `inset 0 -6px 0 -4px #FFD266`              | 텍스트 블록 하이라이트 |
| form-focus       | `0 0 3px 1px #3898ec`                      | Webflow 기본 focus (교체 권장) |

> ⚠️ **노란 inset underline**은 Lemon Squeezy의 시그너처 디테일이다. 링크나 강조 텍스트 하단에 2px 노랑 줄이 inset box-shadow로 그려진다. 일반 `text-decoration: underline` 대신 반드시 `inset 0 -2px 0 0 #FFC233` 형태로 구현할 것.

---

## 11. Layout Patterns

### Hero (마케팅 홈)
- Layout: 중앙 정렬, 다크 배경 (`#121217`) + 보라/핑크 그라디언트 orb
- H1: `2.5rem (40px)` ~ `3.5rem (56px)` / weight 700 / tracking -0.02em
- CTA: 노란 fill 또는 화이트 fill
- Max-width: 1280px

### Feature Section
- Layout: 라이트 배경 (`#F7F7F8`) + 3-column feature grid
- 카드: `#FFFFFF` + `1px solid #D1D1DB` + `radius 20px`
- 섹션 패딩: `96px 24px`

### Section Rhythm
```css
section { padding: 96px 24px; max-width: 1280px; margin-inline: auto; }
.feature-card { background: #fff; border: 1px solid #D1D1DB; border-radius: 20px; padding: 32px; }
```

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Breakpoint | Width | Key Changes |
|---|---|---|
| Mobile | <640px | 단일 컬럼, 모바일 네비게이션, 터치 타겟 44px+ |
| Tablet | 640-1024px | 2컬럼 그리드, 사이드 패딩 증가 |
| Desktop | 1024-1280px | 풀 그리드 레이아웃, 확장 네비게이션 |
| Large | >1280px | max-width 컨테이너, 중앙 정렬 |

---

## 13. Components

### 12.1 Primary CTA (Dark Fill)

```html
<a class="button-primary w-button">Start for free</a>
```

| Spec | Value |
|---|---|
| Background | `#121217` |
| Text | `#ffffff` |
| Padding | `16px 28px` |
| Radius | `12px` |
| Font weight | 500 |
| Hover | `#000000` |

### 12.2 Secondary CTA (Yellow Highlight)

```html
<a class="button-secondary w-button">Learn more</a>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` or `#F7F7F8` |
| Border | `1px solid #D1D1DB` |
| Text | `#121217` |
| Inset underline | `inset 0 -2px 0 0 #FFC233` |
| Radius | `12px` |

### 12.3 Feature Card

```html
<div class="feature-card">
  <div class="feature-card__icon"></div>
  <h3>Sell digital products</h3>
  <p>Get paid. Fast.</p>
</div>
```

| Spec | Value |
|---|---|
| Background | `#FFFFFF` |
| Border | `1px solid #D1D1DB` |
| Radius | `20px` |
| Padding | `32px` |
| Shadow | `4px 0 6px #11112e0d, 0 10px 15px #11112e14` |

### 12.4 Link with Yellow Underline

```html
<a class="link-highlight">learn more</a>
```
```css
.link-highlight {
  color: #121217;
  box-shadow: inset 0 -2px 0 0 #FFC233;
  transition: box-shadow 0.15s ease;
}
.link-highlight:hover {
  box-shadow: inset 0 -6px 0 -1px #FFD266;
}
```

---

## 15. Drop-in CSS

```css
/* Lemon Squeezy — copy into your root stylesheet */
:root {
  /* Fonts */
  --ls-font-display: "Circularpro book", "Circular Pro", "Inter", -apple-system, sans-serif;
  --ls-font-code:    "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;

  /* Brand */
  --ls-color-purple:       #5423E7;
  --ls-color-purple-alt:   #7047EB;
  --ls-color-pink:         #F42AD3;
  --ls-color-yellow:       #FFC233;
  --ls-color-yellow-lighter:#FFD266;

  /* Surface — light dominant */
  --ls-bg-page:    #FFFFFF;
  --ls-bg-soft:    #F7F7F8;
  --ls-bg-alt:     #F4F4F4;
  --ls-bg-muted:   #FAFAFA;

  /* Surface — dark hero */
  --ls-bg-dark:     #121217;
  --dark-mode-bg-lighter: #141414;

  /* Text */
  --ls-fg-ink:     #121217;
  --bullet-point-color: #6C6C89;
  --border-color:  #D1D1DB;

  /* onDark alpha stack */
  --ls-onDark-max:    #FFFFFF;
  --ls-onDark-muted:  #FFFFFF99;
  --ls-onDark-hairline:#FFFFFF33;

  /* Button tokens */
  --button-primary-bg:    #121217;
  --button-primary-light: #FFFFFFE6;

  /* Radius */
  --ls-radius-sm:  6px;
  --ls-radius-md:  8px;
  --ls-radius-lg:  12px;
  --ls-radius-xl:  20px;
  --ls-radius-pill:100px;

  /* Shadow */
  --ls-shadow-card: 4px 0 6px #11112e0d, 0 10px 15px #11112e14;
  --ls-underline-yellow: inset 0 -2px 0 0 #FFC233;
  --ls-highlight-block:  inset 0 -6px 0 -4px #FFD266;
}

body {
  background: var(--ls-bg-page);
  color: var(--ls-fg-ink);
  font-family: var(--ls-font-display);
  font-weight: 400;
}

.link-highlight {
  color: inherit;
  box-shadow: var(--ls-underline-yellow);
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Lemon Squeezy
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          purple:    '#5423E7',
          'purple-2':'#7047EB',
          pink:      '#F42AD3',
          yellow:    '#FFC233',
          'yellow-2':'#FFD266',
        },
        ink:      '#121217',
        surface:  { 1: '#F7F7F8', 2: '#F4F4F4', 3: '#FAFAFA' },
        border:   { DEFAULT: '#D1D1DB' },
        muted:    { DEFAULT: '#6C6C89' },
      },
      fontFamily: {
        sans: ['Circularpro book', 'Circular Pro', 'Inter', '-apple-system', 'sans-serif'],
        mono: ['JetBrains Mono', 'ui-monospace', 'SF Mono', 'monospace'],
      },
      fontWeight: {
        normal:   '400',
        medium:   '500',
        bold:     '700',
      },
      borderRadius: {
        sm: '6px', md: '8px', lg: '12px', xl: '20px', '2xl': '96px', pill: '100px',
      },
      boxShadow: {
        card: '4px 0 6px #11112e0d, 0 10px 15px #11112e14',
        'underline-yellow': 'inset 0 -2px 0 0 #FFC233',
        'highlight-block': 'inset 0 -6px 0 -4px #FFD266',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: auto+manual -->

### Quick Color Reference

| Role | Value |
|---|---|
| Brand | `#5423E7` |
| Page BG | `#FFFFFF` |
| Text Primary | `#000000` |
| Default Theme | mixed |

### Component Prompts

> **Hero section**: "Lemon Squeezy 스타일 hero — `Circular Pro Book` 폰트, `#5423E7` brand color, mixed 배경"
>
> **CTA button**: "Lemon Squeezy primary CTA — brand `#5423E7` 배경 또는 dark fill, `Circular Pro Book` 폰트"
>
> **Card component**: "Lemon Squeezy 스타일 카드 — mixed 테마, 기존 radius/shadow 토큰 준수"

### Iteration Guide

1. **Color 교체 시**: 반드시 §06 Colors 테이블의 실제 hex 참조. AI 추론 색상 사용 금지.
2. **Typography 변경 시**: §04 Font Stack의 font-family 체인 + §05의 weight/size 매핑 확인.
3. **Spacing 조정 시**: §07 Spacing의 토큰 스케일 내에서만 변경.
4. **신규 컴포넌트**: §13 Components의 기존 패턴(radius, shadow, padding)을 기반으로 확장.

---

## 18. DO / DON'T

### ✅ DO
- 브랜드 보라는 **`#5423E7`** (진한 보라). 보조로 `#7047EB`.
- 폰트는 **`Circular Pro Book`** (Webflow Cloud Font). Inter는 폼 필드 보조 역할만.
- 링크/강조에 **노란 inset 밑줄** (`inset 0 -2px 0 0 #FFC233`) 사용. 기본 `text-decoration` 대신.
- **라이트/다크 혼합** 디자인. 히어로는 다크 (`#121217`), 피처 섹션은 라이트 (`#F7F7F8`). 라이트 surface가 dominant.
- Radius는 **20px가 기본** (feature card). 버튼은 12px, 히어로 blob은 96-200px.
- Weight **500을 강조 기본값**으로. 800/900은 거의 쓰지 않음.
- 노란색 **`#FFC233`**을 액센트로, **`#FFD266`** (밝은)을 하이라이트 블록으로 구분해서 사용.

### ❌ DON'T
- ❌ 브랜드 보라를 **`#7C3AED`** (Tailwind Violet)로 쓰지 말 것 → 실제는 `#5423E7`, 톤이 훨씬 진하다.
- ❌ **Inter 단일**을 주 폰트로 쓰지 말 것 → Circular Pro가 주, Inter는 폼 보조.
- ❌ **Dark-only** 디자인으로 만들지 말 것 → 라이트 surface가 실제로 더 많이 쓰인다.
- ❌ `#1E1E2E` / `#2D2D3F` 허구 다크 값 사용 금지 → 실제 다크는 `#121217` / `#000000` / `#141414`.
- ❌ `#3898EC` (Webflow 기본 focus)를 브랜드 색으로 쓰지 말 것 → Webflow editor 디폴트, 브랜드 의도 아님.
- ❌ 단일 `text-decoration: underline` 금지 → 반드시 노란 inset shadow 패턴 사용.
- ❌ Display weight를 **800**으로 고정 금지 → 실제 빈도는 700/500 주도.
- ❌ BEM semantic 토큰 시스템을 기대하지 말 것 → Webflow 빌더 출력이라 토큰 0개, 대부분 hardcoded.
