---
slug: slack
service_name: Slack
site_url: https://slack.com
fetched_at: 2026-04-11
default_theme: light
brand_color: "#611F69"
primary_font: Salesforce-Avant-Garde
font_weight_normal: 400
token_prefix: "(no prefix — unscoped custom properties)"
---

# DESIGN.md — Slack (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Slack의 웹사이트는 밝고 개방적인 배경에 4색 브랜드 팔레트(aubergine, green, blue, red/yellow)가 조화를 이루는 커뮤니케이션 도구 디자인이다. 협업의 에너지와 접근성을 시각적으로 전달한다.

타이포그래피는 기본 시스템 서체를 사용한다. 본문 weight는 **400**이며, 깔끔하고 읽기 편한 텍스트 스타일이 커뮤니케이션 도구의 명확성을 반영한다.

브랜드 aubergine `#4A154B`와 블루 `#1264A3`가 주요 accent이다. 멀티 컬러 팔레트가 Slack의 활기찬 브랜드 정체성을 표현하되, 인터페이스에서는 절제되게 사용된다.

**Key Characteristics:**
- Body는 `Salesforce-Sans`, Heading은 `Salesforce-Avant-Garde` — 둘 다 system-ui 폴백 체인과 함께.
- 링크 · 포커스 · sidebar-highlight에는 `#1264A3`(실제 CSS 1위 non-neutral hex). Aubergine이 아니다.
- Hero/CTA anchor는 `#611F69` — 레거시 `#4A154B`(3위)는 "기사/legacy article theme"에만.
- 버튼/인풋 `border-radius: 4px`. 8px 이상은 카드·모달 전용.
- Ambient shadow `0 0 2rem rgba(0,0,0,0.1)`로 카드 띄우기. 포커스는 `inset 0 0 0 2px #611F69`.
---

## 01. Quick Start

> 5분 안에 Slack처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트: heading은 Avant-Garde, body는 Salesforce-Sans */
:root {
  --font-family-heading: "Salesforce-Avant-Garde", system-ui, -apple-system, sans-serif;
  --font-family-body:    "Salesforce-Sans", system-ui, -apple-system, sans-serif;
}
body  { font-family: var(--font-family-body); font-weight: 400; }
h1,h2 { font-family: var(--font-family-heading); font-weight: 700; }

/* 2. 배경 + 텍스트 (light 랜딩) */
:root { --bg: #FFFFFF; --fg: #1D1C1D; }
body { background: var(--bg); color: var(--fg); }

/* 3. 두 개의 브랜드 anchor */
:root {
  --brand-aubergine: #611F69;  /* 현재 hero/CTA anchor */
  --brand-link:      #1264A3;  /* 링크 · 포커스 · sidebar-highlight */
}
```

**절대 하지 말아야 할 것 하나**: Slack의 "브랜드 색 = aubergine `#4A154B`" 가정 금지. 실제 랜딩 페이지에서 제일 많이 쓰이는 파란색 링크 `#1264A3`(161회)과 aubergine 변형 `#611F69`(130회)가 dominant이고, 레거시 `#4A154B`는 3위(49회). `#4A154B` 하나로 전체 CTA를 칠하면 2019년 Slack처럼 보인다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://slack.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 231,191 bytes (server-rendered marketing) |
| CSS files | 9개 외부, 총 856,587자 |
| Token prefix | 없음 — `--font-family-*`, `--sidebar-*`, `--article-theme-*` 등 언스코프드 변수 109개 |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Static/server-rendered marketing site (`rollup-style-spacesuit.*.min.css` 번들 기반)
- **Design system**: "Spacesuit" — Slack 마케팅 사이트 내부 DS 이름. 토큰 prefix 없음, 시멘틱 변수명만 노출.
- **CSS architecture**: BEMIT (BEM + ITCSS) — `o-object`, `c-component`, `u-utility` 접두어
  ```
  o-*        레이아웃 object (예: o-section--feature)
  c-*        컴포넌트 (예: c-extnav-level__3, c-accordion-carousel)
  u-*        유틸리티 (예: u-margin-bottom--flush)
  nav_*      네비 전용 레거시 스네이크
  ```
- **Class naming**: BEMIT + snake_case legacy navigation (`nav_link_label`, `nav_parent_l3`)
- **Default theme**: **light** (body/bck-color = `#FFFFFF`). Aubergine(`#400d40`)은 **사이드바 전용** — 전체 테마 아님.
- **Font loading**: `@font-face` 정의는 `rollup-style-spacesuit` 번들 내부, `Salesforce-Sans` + `Salesforce-Avant-Garde`. 언어별로 `--font-family-heading` override(`SeolSansHeavy` KR, `Tazugane-Info-Heavy` JP, `MXiangHeHeiSCProBold` zh-CN 등).
- **Canonical anchor**: `#611F69` (bck-color + CTA hover + 로고 변형). Salesforce 합병 후 aubergine 톤이 한 단계 밝아진 버전.

---

## 04. Font Stack

- **Display font**: `Salesforce-Avant-Garde` (Slack 마케팅 heading 전용, Salesforce 라이선스)
- **Body font**: `Salesforce-Sans` (Salesforce Lightning Design System 공용)
- **Legacy fallback**: `Slack-Lato` (레거시 슬랙 Lato variant — 실제 CSS에 3회만 남음, 사용 금지)
- **Code font**: `Monaco` → `Menlo` → `Consolas` → `Courier New`
- **Weight normal / bold**: `400` / `700` (body), heading은 700/900 혼용

```css
:root {
  --font-family-heading:
    "Salesforce-Avant-Garde", system-ui, -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-family-body:
    "Salesforce-Sans", system-ui, -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-family-monospace: "Monaco", "Menlo", "Consolas", "Courier New", monospace;
}
body {
  font-family: var(--font-family-body);
  font-weight: 400;
}
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-family-heading);
}
```

> ⚠️ **Lato가 아니다.** Slack은 Salesforce 인수 후 Salesforce-Sans + Salesforce-Avant-Garde로 이전했다. `Slack-Lato`는 레거시 폴백이며 실제 랜딩에서 거의 렌더되지 않는다. `Lato`로 대체 시 자간·x-height 시각 격차 큼.

---

## 05. Typography Scale

| Token (raw size) | Size | Weight | Line-height | Usage |
|---|---|---|---|---|
| display-xl | `3.625rem` / 58px | 900 / 700 | ~1.1 | Hero H1 |
| display-lg | `3.125rem` / 50px | 900 / 700 | ~1.1 | 섹션 타이틀 |
| display-md | `3rem` / 48px | 700 | 1.15 | 섹션 서브타이틀 |
| display-sm | `2.75rem` / 44px | 700 | 1.15 | |
| heading-xl | `2rem` / 32px | 700 | 1.2 | H2 |
| heading-lg | `1.75rem` / 28px | 700 | 1.25 | H3 |
| heading-md | `1.5rem` / 24px | 700 | 1.3 | H4 (96회) |
| heading-sm | `1.25rem` / 20px | 700 | 1.3 | |
| body-lg | `1.125rem` / 18px | 400 | 1.5 | 인트로 문단 |
| body-md | `1rem` / 16px | 400 | 1.5 | 본문 (303회) |
| body-sm | `.9375rem` / 15px | 400 | 1.5 | 작은 본문 |
| body-xs | `.875rem` / 14px | 400 | 1.5 | 캡션 (295회) |
| micro | `.8rem` / 12.8px | 400 | 1.4 | 레이블 · 푸터 |
| micro-xs | `.72rem` / 11.5px | 400 | 1.4 | |

> ⚠️ **rem 기반 스케일.** `1rem`(303회)과 `.875rem`(295회)가 압도적 1·2위. 16px + 14px 본문 2단 조합이 실제 랜딩의 리듬. `heading-` 계열의 weight는 `700`/`900` 두 값만 존재 — 300/500 같은 중간값 없음.

---

## 06. Colors

### 06-1. Aubergine Family (brand anchor)

| Token | Hex | CSS Count |
|---|---|---|
| `--article-theme-primary` | `#4A154B` | 49 (legacy anchor) |
| `#611F69` (현 aubergine) | `#611F69` | 130 (hero bg, CTA) |
| `--sidebar-color` | `#400D40` | — (앱 사이드바 전용) |
| `#481A54` (중간톤) | `#481A54` | 13 |
| `#730394` (하이라이트) | `#730394` | 12 |
| `#F9F0FF` (pale bg) | `#F9F0FF` | 17 |
| `#F2DEFE` (pale bg) | `#F2DEFE` | 10 |
| `#F9EDFF` (pale bg) | `#F9EDFF` | 8 |

### 06-2. Link / Focus Blue

| Token | Hex | CSS Count | Usage |
|---|---|---|---|
| `--sidebar-highlight-color` | `#1264A3` | 161 (1위) | 링크, 포커스 링, sidebar highlight |
| secondary blue | `#36C5F0` | 39 | Slack 로고 5색 중 cyan, 일러스트 |
| Google blue | `#4285F4` | 7 | Google SSO 버튼 |

### 06-3. Neutral Ramp

| Role | Hex | Count |
|---|---|---|
| white | `#FFFFFF` | 369 (1위) |
| ink / text-primary | `#1D1D1D` / `#1D1C1D` | 37 / 19 |
| text-muted | `#454245` | 26 |
| text-secondary | `#717274` / `#616061` | 20 / 8 |
| border-soft | `#EBEAEB` | 66 |
| border-subtle | `#E8E8E8` | 13 |
| surface-muted | `#F5F4F5` | 30 |
| surface-cream | `#F4EDE4` | 7 |
| black | `#000000` | 122 |
| overlay-10 | `#0000001A` (10% alpha) | 66 |
| overlay-20 | `#00000033` (20% alpha) | 13 |

### 06-4. Slack Logo Accent 5 (illustration only)

| Family | Hex | Count |
|---|---|---|
| cyan | `#36C5F0` | 39 |
| pink / red | `#E01E5A` / `#C01343` | 6 / 22 |
| green | `#007A5A` | 13 |
| green (logo kit) | `#2EB67D` | 3 (거의 0) |
| yellow (logo kit) | `#ECB22E` | 3 (거의 0) |

> ⚠️ **로고 5색은 UI 색이 아니다.** `#2EB67D`(녹)·`#ECB22E`(황)는 CSS에 각 3회만 등장 — 일러스트 전용. CTA/상태 컬러로 이 두 개를 쓰면 실제 Slack과 달라진다. 성공 상태는 `#007A5A`(13회)를 써라.

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--sidebar-color` | `#400D40` | 사이드바 배경 (앱) |
| `--sidebar-highlight-color` | `#1264A3` | 사이드바 활성 · 링크 |
| `--article-theme-primary` | `#4A154B` | 기사 템플릿 테마 앵커 |
| `--article-theme-secondary` | `#FFFFFF` | 기사 템플릿 대비 |
| `--bck-color` (variable) | `#FFFFFF` / `#4A154B` / `#F9F0FF` / `#EBF7E6` / ... | 섹션별 배경 토큰 |
| `--attachment-color` | `#000000` | 파일 첨부 라벨 |

### 06-6. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 369 | 페이지 배경 · 카드 |
| 2 | `#1264A3` | 161 | 링크 · 포커스 |
| 3 | `#611F69` | 130 | 현 aubergine anchor |
| 4 | `#000000` | 122 | 텍스트 |
| 5 | `#696969` | 97 | 보조 텍스트 |
| 6 | `#EBEAEB` | 66 | 보더 |
| 7 | `#4A154B` | 49 | 레거시 aubergine |
| 8 | `#36C5F0` | 39 | 로고 cyan |
| 9 | `#1D1D1D` | 37 | primary ink |
| 10 | `#F5F4F5` | 30 | surface muted |

---

## 07. Spacing

> ℹ️ Slack은 토큰화된 spacing scale이 없다. raw px 값 사용. 관측된 radii/spacing 빈도에서 역산한 실효 scale:

| Alias | Value | 근거 |
|---|---|---|
| `space-1` | 4px | radii top1 (54회) |
| `space-2` | 8px | radii #2 (12회) |
| `space-3` | 12px | radii #3 (9회) |
| `space-4` | 16px | radii #6 (6회) |
| `space-6` | 24px | raw (3회+) |
| `space-8` | 32px | 섹션 패딩 |
| `space-12` | 48px | 섹션 세로 리듬 |
| `space-16` | 64px | hero 패딩 |

**주요 alias**: 없음 — 컴포넌트마다 raw rem/px 직접 사용. 복제 시 4/8/16/32의 4배수 그리드로 정렬하면 일관성 나온다.

---

## 08. Radius

| Token | Value | Count | Context |
|---|---|---|---|
| sm | `4px` | 54 | 버튼, 인풋 (압도적 1위) |
| md | `8px` | 12 | 카드 |
| focus-3 | `3px` | 9 | 포커스 ring 두께 |
| lg | `12px` | 9 | 큰 카드 |
| elevation-5 | `5px` | 6 | 드롭다운 |
| xs | `2px` | 4 | 토글 · 체크박스 |
| pill | `60px` | 3 | 원형 CTA |

> ⚠️ **4px이 기본.** Slack 버튼/인풋 대부분이 `border-radius: 4px`. 8px 이상은 카드·모달 전용.

---

## 09. Shadows

| Level | Value | Count | Usage |
|---|---|---|---|
| sm (ambient) | `0 0 2rem #0000001a` | 26 | 플로팅 카드 |
| md (elevation) | `0 1rem 2rem #0000001a` | 7 | 모달 |
| pop | `0 5px 20px #0000001a` | 7 | 드롭다운 |
| inset-focus | `inset 0 0 0 2px #611f69` | 10 | 포커스 ring (aubergine) |
| inset-focus-white | `inset 0 0 0 1px #fff` | 10 | 라이트 카드 포커스 |
| inset-border | `inset 0 0 0 1px #611f69` | 6 | 테두리 대체 |
| overlay-heavy | `0 0 2rem #0003` | 6 | 20% alpha 그림자 |

> ⚠️ **inset 그림자로 포커스/보더를 구현.** `inset 0 0 0 1-2px #611f69`가 aubergine 포커스 ring 패턴 — `outline` 대신. 일반 박스 그림자는 `#0000001a`(10%) ambient가 기본.

---

## 11. Layout Patterns

### Hero
- Layout: center-aligned single column, max-width ~960px
- Background: `#FFFFFF` (랜딩은 화이트) + aubergine `#611F69` hero block 변형
- H1: `display-xl` (~58px) / weight `700`–`900` / line-height `1.1`
- Max-width: 인라인 텍스트 ~720px, 래퍼 ~1200px

### Section Rhythm
```css
section {
  padding: 64px 32px;
  max-width: 1200px;
  margin: 0 auto;
}
```

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Breakpoint | Width | Key Changes |
|---|---|---|
| Mobile | <640px | 단일 컬럼, 헤딩 축소, 카드 스택 |
| Tablet | 640-1024px | 2열 그리드, 중간 패딩 |
| Desktop | 1024-1280px | 풀 레이아웃, 3열 그리드 |
| Large | >1280px | 중앙 정렬 max-width 1200px, 넉넉한 마진 |

> ⚠️ Slack는 모바일 퍼스트 반응형 디자인을 채택하며, 브레이크포인트별로 그리드와 타이포그래피가 유동적으로 조정된다.

---

## 13. Components

### Button (primary)

```html
<a class="c-button c-button--primary" href="#">Try for free</a>
```

```css
.c-button--primary {
  background: #611F69;
  color: #FFFFFF;
  font-family: var(--font-family-heading);
  font-weight: 700;
  padding: 14px 24px;
  border-radius: 4px;
  border: 0;
}
.c-button--primary:hover { background: #4A154B; }
.c-button--primary:focus { box-shadow: inset 0 0 0 2px #FFFFFF, 0 0 0 3px #611F69; }
```

### Button (secondary)

```html
<a class="c-button c-button--secondary" href="#">Talk to sales</a>
```

```css
.c-button--secondary {
  background: transparent;
  color: #1D1C1D;
  border: 1px solid #1D1C1D;
  border-radius: 4px;
  padding: 14px 24px;
}
```

### Nav link (legacy)

```html
<a class="nav_link nav_link_l2">
  <span class="nav_link_label">Product</span>
  <span class="nav_link_sublabel">What's included</span>
</a>
```

### Section feature

```html
<section class="o-section o-section--feature">
  <div class="o-section__inner">
    <h2 class="c-heading c-heading--lg">Where work happens</h2>
    <a class="o-section--feature__link c-accordion-carousel__text-link">Learn more</a>
  </div>
</section>
```

### Accordion carousel

```html
<div class="c-accordion-carousel">
  <div class="swiper-slide">
    <h3 class="c-accordion-carousel__title">…</h3>
    <p class="c-accordion-carousel__body">…</p>
  </div>
</div>
```

---

## 15. Drop-in CSS

```css
/* Slack — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family-heading:
    "Salesforce-Avant-Garde", system-ui, -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-family-body:
    "Salesforce-Sans", system-ui, -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-family-monospace: "Monaco", "Menlo", "Consolas", "Courier New", monospace;

  /* Aubergine (anchor + 4 steps) */
  --color-aubergine-25:  #F9F0FF;
  --color-aubergine-300: #730394;
  --color-aubergine-500: #611F69;   /* ← canonical (현 브랜드) */
  --color-aubergine-700: #4A154B;   /* legacy anchor */
  --color-aubergine-900: #400D40;   /* sidebar 전용 */

  /* Blue (link · focus) */
  --color-link-500: #1264A3;   /* ← dominant #1 */
  --color-link-300: #36C5F0;

  /* Surfaces */
  --bg-page:      #FFFFFF;
  --bg-dark:      #400D40;
  --text-primary: #1D1C1D;
  --text-muted:   #454245;
  --border-soft:  #EBEAEB;

  /* Key spacing */
  --space-2:  8px;
  --space-4:  16px;
  --space-8:  32px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;

  /* Shadow */
  --shadow-ambient: 0 0 2rem rgba(0,0,0,0.1);
  --shadow-focus:   inset 0 0 0 2px #611F69;
}

body {
  font-family: var(--font-family-body);
  font-weight: 400;
  background: var(--bg-page);
  color: var(--text-primary);
}
h1, h2, h3 {
  font-family: var(--font-family-heading);
  font-weight: 700;
}
a { color: var(--color-link-500); }
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Slack
module.exports = {
  theme: {
    extend: {
      colors: {
        aubergine: {
          25:  '#F9F0FF',
          100: '#F2DEFE',
          300: '#730394',
          500: '#611F69',   // canonical (현)
          700: '#4A154B',   // legacy
          900: '#400D40',   // sidebar 전용
        },
        link: {
          300: '#36C5F0',
          500: '#1264A3',   // dominant #1
        },
        neutral: {
          0:   '#FFFFFF',
          100: '#F5F4F5',
          200: '#EBEAEB',
          300: '#E8E8E8',
          500: '#717274',
          600: '#616061',
          700: '#454245',
          800: '#1D1D1D',
          900: '#1D1C1D',
        },
        logo: {
          cyan:  '#36C5F0',
          pink:  '#E01E5A',
          red:   '#C01343',
          green: '#007A5A',
        },
      },
      fontFamily: {
        sans:     ['"Salesforce-Sans"', 'system-ui', 'sans-serif'],
        heading:  ['"Salesforce-Avant-Garde"', 'system-ui', 'sans-serif'],
        mono:     ['Monaco', 'Menlo', 'Consolas', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        bold:   '700',
        black:  '900',
      },
      borderRadius: {
        sm: '4px',
        md: '8px',
        lg: '12px',
        pill: '60px',
      },
      boxShadow: {
        sm: '0 0 2rem rgba(0,0,0,0.1)',
        md: '0 1rem 2rem rgba(0,0,0,0.1)',
        pop: '0 5px 20px rgba(0,0,0,0.1)',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference
| Role | Hex |
|---|---|
| Primary CTA | `#611F69` |
| Heading text | `#1D1C1D` |
| Body text | `#616061` |
| Background | `#FFFFFF` |
| Border | `#DDDDDD` |
| Link | `#1264A3` |
| Dark section | `#1A1D21` |

### Example Component Prompts
- "Create a hero section on `#FFFFFF` background. Headline at 3rem `Salesforce-Avant-Garde` weight 400. CTA button `#611F69` with white text."
- "Design a card: `#1c1c1f` background, `#DDDDDD` border, 8px radius. Body text `#616061` at weight 400."

### Iteration Guide
1. 폰트: `Salesforce-Avant-Garde` 패밀리, 본문 weight 400
2. 컬러: 브랜드 `#611F69`는 CTA/링크에만 집중. 배경 `#FFFFFF`, 텍스트 `#1D1C1D`
3. 그림자: subtle box-shadow로 modal/popover elevation 표현
---

## 18. DO / DON'T

### ✅ DO
- Body는 `Salesforce-Sans`, Heading은 `Salesforce-Avant-Garde` — 둘 다 system-ui 폴백 체인과 함께.
- 링크 · 포커스 · sidebar-highlight에는 `#1264A3`(실제 CSS 1위 non-neutral hex). Aubergine이 아니다.
- Hero/CTA anchor는 `#611F69` — 레거시 `#4A154B`(3위)는 "기사/legacy article theme"에만.
- 버튼/인풋 `border-radius: 4px`. 8px 이상은 카드·모달 전용.
- Ambient shadow `0 0 2rem rgba(0,0,0,0.1)`로 카드 띄우기. 포커스는 `inset 0 0 0 2px #611F69`.
- 사이드바 전용 다크 테마(`#400D40`)는 **사이드바에만**. 전체 페이지 배경 금지.

### ❌ DON'T
- ❌ `#4A154B` 하나로 전체 CTA 칠하기 (2019년 Slack처럼 보임, 실제 3위)
- ❌ Lato / Slack-Lato (레거시 폴백, 인수 후 거의 미사용)
- ❌ 로고 5색 중 `#2EB67D`(녹), `#ECB22E`(황)를 UI 토큰으로 (각 3회만 등장 — 일러스트 전용)
- ❌ 전체 페이지 aubergine 배경 (랜딩은 light `#FFFFFF`가 기본, aubergine은 사이드바/hero 블록 한정)
- ❌ `outline` 기반 포커스 스타일 (Slack은 `box-shadow inset`으로 구현)
- ❌ `--space-*` 같은 스페이싱 토큰 존재 가정 (실제 CSS에는 없음 — raw rem/px)
- ❌ Success 상태에 `#2EB67D` (실제는 `#007A5A`, 13회)
- ❌ 단일 "aubergine" 테마 가정 — 랜딩(`#611F69`)/기사(`#4A154B`)/앱 사이드바(`#400D40`) 3개 변형 분리 필수

---

