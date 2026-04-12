---
slug: cal
service_name: Cal.com
site_url: https://cal.com
fetched_at: 2026-04-11
default_theme: light
brand_color: "#6349EA"
primary_font: Cal Sans
font_weight_normal: 400
token_prefix: framer
---

# DESIGN.md — Cal.com (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Cal.com처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — Cal Sans for display, Inter for body */
@font-face { font-family: "Cal Sans"; src: url("https://fonts.cdnfonts.com/s/95168/CalSans-SemiBold.woff") format("woff"); }

:root {
  --font-display: "Cal Sans", "Inter Display", Inter, system-ui, sans-serif;
  --font-body:    "Inter", "Inter Variable", system-ui, -apple-system, sans-serif;
}
body { font-family: var(--font-body); font-weight: 400; }
h1, h2, h3 { font-family: var(--font-display); font-weight: 600; }

/* 2. 라이트 배경 + 진한 텍스트 */
:root { --bg: #FFFFFF; --fg: #141414; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 보라 (link / accent) */
:root { --brand: #6349EA; --link: #0099FF; }
```

**절대 하지 말아야 할 것 하나**: Cal.com은 오렌지 브랜드가 **아니다**. 실제 accent는 `#6349EA` 보라와 `#0099FF` 파랑 2색 페어 (link current / default). 헤드라인에 반드시 **Cal Sans** 커스텀 폰트 사용 — 이것이 Cal.com 브랜드의 핵심.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://cal.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| CSS files | 4개 (framer runtime + 3 route bundles), 총 444,098자 |
| Custom properties | 90개 (`--token-{uuid}` + `--framer-*`) |
| Color vars | 10개 |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: **Framer**-hosted static site (cal.com marketing)
- **Design system**: Framer token system — UUID 기반 (`--token-1707e66c-...`)
- **CSS architecture**: Framer runtime이 디자이너 지정 스타일을 UUID 토큰으로 컴파일
  ```
  token tier      (--token-{uuid})       raw hex 값 (디자이너 Framer 스타일 ID)
  framer tier     (--framer-link-*)      component-level semantic
  layout tier     --framer-font-size / letter-spacing / paragraph-spacing
  ```
- **Class naming**: Framer 생성 클래스 (`.framer-body`, `.framer-text`), 사람이 읽기 어려움
- **Default theme**: **light** (bg `#FFFFFF`, text `#141414`)
- **Font loading**: Framer font manager — Inter + Cal Sans 혼용
- **Canonical anchor**: `#6349EA` (`--framer-link-current-text-color`) — 보라 accent

> **중요**: cal.com은 웹 앱(app.cal.com — React/Next.js with Tailwind)과 마케팅 사이트(cal.com — Framer)가 **다른 스택**. 본 문서는 **마케팅 사이트** 기준.

---

## 04. Font Stack
<!-- SOURCE: auto -->

- **Display font**: `Cal Sans` (Cal.com 전용 오픈소스 폰트 — GitHub: calcom/font)
- **Display alternate**: `Inter Display`
- **Body font**: `Inter` (+ `Inter Variable`)
- **Code font**: `Roboto Mono` / `Fragment Mono` (보조)

```css
:root {
  --font-display:  "Cal Sans", "Inter Display", Inter, system-ui, sans-serif;
  --font-body:     "Inter", "Inter Variable", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono:     "Roboto Mono", "Fragment Mono", ui-monospace, Menlo, monospace;
}
h1, h2, h3 { font-family: var(--font-display); font-weight: 600; }
body       { font-family: var(--font-body);    font-weight: 400; }
```

> **Cal Sans**는 오픈소스. `https://github.com/calcom/font` 에서 다운로드. 주로 semibold (600)로 헤드라인에 사용되며, Inter보다 좀 더 둥글고 geometric한 인상을 준다.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Role | Size | Weight | Family | Usage |
|---|---|---|---|---|
| hero display | 64px | 600 | Cal Sans | landing h1 |
| display xl | 56px | 600 | Cal Sans | 섹션 display |
| h1 | 48px | 600 | Cal Sans / Inter Display | 페이지 제목 |
| h2 | 40px | 600 | Cal Sans / Inter Display | 피처 제목 |
| h3 | 32px | 600 | Inter Display | 카드 제목 |
| h4 | 24px | 600 | Inter Display | 서브섹션 |
| lead | 20px | 400 | Inter | hero 서브헤딩 |
| body large | 18px | 400 | Inter | intro 문단 |
| body | 16px | 400 | Inter | 기본 본문 (최다 빈도: 12회) |
| small | 14px | 400 | Inter | 보조 텍스트 |
| caption | 12px | 400 | Inter | meta / 타임스탬프 |

> ⚠️ Weight axis는 `100 ~ 900` 전 범위 사용 (Inter Variable의 전체 weight). 헤딩은 `600`이 기본. Cal Sans의 semibold가 Inter Display의 semibold보다 시각적으로 훨씬 distinctive — 이것이 Cal.com 브랜드의 포인트.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-3. Neutral Ramp (실제 빈도순)
<!-- SOURCE: auto -->

| Token | Hex | Count | Role |
|---|---|---|---|
| `framer-text (primary)` | `#141414` | 32 | 본문 기본 텍스트 |
| `framer-text (display)` | `#242424` | 57 | 헤딩 (살짝 밝은 검정) |
| `framer-text (inverse)` | `#FFFFFF` | 29 | dark bg 위 텍스트 |
| base true-black | `#000000` | 77 | logo / stroke |
| `framer-text (muted)` | `#898989` | 26 | 서브 텍스트 |
| border light | `#E1E2E3` | 18 | hairline border |
| border subtler | `#F4F4F4` | 6 | 섹션 divider |
| text-alpha-70 | `#242424B3` | 10 | 70% alpha 텍스트 |
| text-alpha-5 | `#2424240D` | 10 | 5% alpha bg tint |
| secondary dark | `#343434` | 6 | subtle dark bg |

### 06-4. Accent
<!-- SOURCE: auto -->

| Token | Hex | Count | Usage |
|---|---|---|---|
| `--framer-link-text-color` | `#0099FF` | 12 | 링크 기본 (파랑) |
| `--framer-link-current-text-color` | `#6349EA` ⭐ | 8 | **active / current 링크 (보라)** |

> **중요**: Cal.com은 **link state 3종 페어**로 accent를 운영. 기본 링크는 파랑 `#0099FF`, 현재 페이지 / active 링크는 보라 `#6349EA`. 오렌지 브랜드는 없다.

### 06-5. Semantic (framer)
<!-- SOURCE: auto -->

| Alias | Value | Usage |
|---|---|---|
| `--framer-text-color` | `#141414` | body text 기본 |
| `--framer-link-text-color` | `#0099FF` | 링크 default |
| `--framer-link-current-text-color` | `#6349EA` | 현재 경로 |
| `--framer-link-hover-text-color` | (inherited) | hover 상태 |
| `--framer-font-size` | `16px` | 기본 body size |
| `--framer-letter-spacing` | `0` | default tracking |
| `--framer-paragraph-spacing` | (variable) | 문단 gap |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto -->

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#000000` | 77 | true black (icons/strokes) |
| 2 | `#242424` | 57 | display heading |
| 3 | `#141414` | 32 | body text primary |
| 4 | `#FFFFFF` | 29 | page bg |
| 5 | `#898989` | 26 | muted text |
| 6 | `#E1E2E3` | 18 | border |
| 7 | `#0099FF` | 12 | link blue |
| 8 | `#242424B3` | 10 | alpha text |
| 9 | `#6349EA` | 8 | **accent purple** |
| 10 | `#F4F4F4` | 6 | section bg |

---

## 07. Spacing
<!-- SOURCE: auto -->
<!-- Framer는 전통적 spacing scale을 쓰지 않는다. letter/paragraph level만 토큰화. -->

| Token | Value | Use case |
|---|---|---|
| `--framer-font-size` | `16px` | base font (최다 빈도 12회) |
| `--framer-letter-spacing` | `0` | default tracking |
| `--framer-paragraph-spacing` | (variable) | 문단 간격 |

> Framer는 Figma처럼 **spacing을 개별 layer의 numeric value로 관리**. `--space-md` 같은 공용 scale 토큰 개념이 없음. Claude로 재현할 때는 다음 heuristic 사용 권장:
> - small gap: 8px
> - medium gap: 16px
> - section padding: 64~80px
> - hero vertical rhythm: 120px

---

## 08. Radius
<!-- SOURCE: auto (raw px frequency) -->

| Value | Context |
|---|---|
| `16px` | card corner (가장 빈번, 4회) |
| `12px` | button / input |
| `8px` | tag / chip |
| `2px` | hairline accent |
| `9999px` | pill button / avatar |

> Cal.com은 카드에 `16px` 라운드를 일관 사용. Linear/Framer 계열 제품들이 공유하는 "생산성 툴 감성"이다.

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Primary CTA (dark)
- **Background**: `#141414` (framer text primary — 검정 버튼)
- **Text**: `#FFFFFF`
- **Radius**: `9999px` (pill) 또는 `12px`
- **Font**: `Inter` 16px / 500
- **Padding**: `12px 24px`

```html
<button class="framer-button framer-button--primary">
  Get started
</button>
```

### Secondary CTA (outlined)
- **Background**: transparent
- **Text**: `#141414`
- **Border**: `1px solid #E1E2E3`
- **Radius**: same as primary
- **Hover**: bg `#F4F4F4`

### Link (3-state)
- **Default**: `#0099FF` (파랑)
- **Current (active route)**: `#6349EA` (보라)
- **Hover**: inherited color + underline

### Calendar booking card (핵심 컴포넌트)
- **Background**: `#FFFFFF`
- **Border**: `1px solid #E1E2E3`
- **Radius**: `16px`
- **Shadow**: none (flat, border-only elevation)
- **Padding**: `24px`
- **Font**: Cal Sans heading + Inter body
- **Time slot chip**: pill shape, border `#E1E2E3`, text `#141414`, hover `#F4F4F4`

### Section rhythm
- Hero: padding 120px top / 80px bottom
- Section: padding 80px vertical
- Max-width: 1200px
- Column gap: 48px

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Cal.com — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-display: "Cal Sans", "Inter Display", Inter, system-ui, sans-serif;
  --font-body:    "Inter", "Inter Variable", system-ui, -apple-system, sans-serif;
  --font-mono:    "Roboto Mono", ui-monospace, Menlo, monospace;

  /* Text colors */
  --text:         #141414; /* framer-text primary */
  --text-display: #242424; /* framer-text display */
  --text-muted:   #898989;
  --text-inverse: #FFFFFF;

  /* Surface */
  --bg:        #FFFFFF;
  --bg-section:#F4F4F4;

  /* Borders */
  --border:    #E1E2E3;

  /* Accents (link state 3) */
  --link:         #0099FF;
  --link-current: #6349EA; /* brand purple */

  /* Radius */
  --radius-card:  16px;
  --radius-btn:   12px;
  --radius-pill:  9999px;
}

body {
  font-family: var(--font-body);
  font-weight: 400;
  background: var(--bg);
  color: var(--text);
}

h1, h2, h3, h4 {
  font-family: var(--font-display);
  font-weight: 600;
  color: var(--text-display);
}

a { color: var(--link); }
a.current, a[aria-current="page"] { color: var(--link-current); }
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Cal.com-ish
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#6349EA', // link-current purple
          link:    '#0099FF', // link default blue
        },
        neutral: {
          0:   '#FFFFFF',
          50:  '#F4F4F4',
          100: '#E1E2E3',
          300: '#898989',
          600: '#343434',
          700: '#242424',
          900: '#141414',
          950: '#000000',
        },
      },
      fontFamily: {
        display: ['"Cal Sans"', '"Inter Display"', 'Inter', 'system-ui', 'sans-serif'],
        sans:    ['"Inter"', '"Inter Variable"', 'system-ui', '-apple-system', 'sans-serif'],
        mono:    ['"Roboto Mono"', 'ui-monospace', 'Menlo', 'monospace'],
      },
      fontWeight: {
        thin:      '100',
        extralight:'200',
        light:     '300',
        normal:    '400',
        medium:    '500',
        semibold:  '600',
        bold:      '700',
        extrabold: '800',
        black:     '900',
      },
      borderRadius: {
        sm:   '2px',
        md:   '8px',
        lg:   '12px',
        xl:   '16px',
        full: '9999px',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- **Cal Sans 폰트**를 display/heading에 사용 — Cal.com 브랜드의 핵심 차별 요소 (오픈소스, GitHub `calcom/font`).
- Body는 `Inter` / `Inter Variable`.
- 텍스트 컬러는 `#141414` (body) + `#242424` (heading) 페어. 순수 `#000000`은 logo/stroke에만.
- 링크는 **2색 state 페어**: 기본 `#0099FF` 파랑, current `#6349EA` 보라.
- 라이트 테마 기본값. 페이지 bg `#FFFFFF`, 섹션 bg `#F4F4F4`.
- 카드 radius `16px` 일관 사용. 버튼은 pill (`9999px`) 또는 `12px`.
- Flat 디자인 — border-only elevation, shadow 최소.
- 16px base font size 고정.

### ❌ DON'T
- ❌ **오렌지 CTA** 사용 — Cal.com CSS에 오렌지 `#FF7A45` 등은 **0회**. 로고의 `@` 장식 색을 브랜드로 착각한 것.
- ❌ 헤딩을 Inter로만 처리 — Cal Sans 누락 시 브랜드 정체성 소실.
- ❌ `color-brand: #000000` 같은 단일 브랜드 컬러 기대 — Cal.com의 브랜드는 **link state 페어**.
- ❌ `color-gray-*` flat 네이밍 — 실제는 `--framer-text-color`, `--token-{uuid}` 기반.
- ❌ Tailwind spacing scale 기대 — Framer는 개별 layer numeric value로 spacing 관리.
- ❌ 단일 shadow 시스템 — Cal.com은 shadow 거의 없는 flat design.
- ❌ Inter Tight / Noto Sans 같은 임의 대체 — Inter + Inter Display 조합이 Framer 기본값.
- ❌ `Cal Sans`를 body로 쓰기 — semibold만 있어서 long-form 가독성 떨어짐.
