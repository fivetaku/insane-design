---
slug: planetfall
service_name: "Age of Wonders: Planetfall"
site_url: https://www.paradoxinteractive.com/games/age-of-wonders-planetfall/about
fetched_at: 2026-04-12
default_theme: dark
brand_color: "#E5D195"
primary_font: Source Sans Pro
font_weight_normal: 400
token_prefix: "--*"
---

# DESIGN.md — Age of Wonders: Planetfall (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Age of Wonders: Planetfall은 SF/판타지 게임 페이지답게 장대하고 서사적인 비주얼을 가진다. 깊은 네이비 블루 `#1A1D48`과 SF-desert 톤 `#122534`가 우주-사막 분위기를 만들고, 골드 악센트 `#E5D195`가 게임 전체를 관통하는 시그니처 컬러로 CTA, 텍스트 하이라이트, 버튼에 통일되어 사용된다.

본문 텍스트는 순백이 아닌 sand `#DED6C1`로, 다크 배경 위에서 따뜻한 아이보리 톤을 만든다. heading에는 `text-shadow: 0 0 24px #040507` 가독성 halo가 필수이며, 호버 효과에는 골드 radial-gradient 글로우가 적용된다. Paradox Design System의 게임별 테마 오버라이드 구조를 사용한다.

**Key Characteristics:**
- Deep navy `#1A1D48` + SF-desert `#122534` 다크 테마 (순수 검정 금지)
- Gold `#E5D195` 단일 악센트로 전체 통일
- Sand `#DED6C1` 본문 텍스트 (순백 금지)
- Text-shadow 가독성 halo + radial-gradient 골드 글로우
- 버튼 radius 2px — SF/밀리터리 느낌의 핵심

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Planetfall 게임 페이지처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Source Sans Pro", sans-serif;
  font-weight: 400;
  color: #DED6C1;   /* sand — 다크 배경 위 본문 색 */
}

/* 2. 다크 배경 */
:root {
  --bg: #1A1D48;      /* 깊은 SF 네이비 — 게임 테마 다크 */
  --bg-surface: #122534; /* body 기본 배경 (인라인 스타일) */
}
body { background: var(--bg-surface); }

/* 3. 골드 악센트 */
:root { --accent: #E5D195; }
```

**절대 하지 말아야 할 것 하나**: 배경을 순수 `#000000` 으로 두는 것. Planetfall 의 다크 테마는 **깊은 네이비 블루 `#1A1D48`** 과 **SF-desert 톤 `#122534`** 의 조합이다. 순수 블랙을 쓰면 게임 특유의 우주-사막 분위기가 완전히 사라진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.paradoxinteractive.com/games/age-of-wonders-planetfall/about` |
| Fetched | 2026-04-12 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 156,481 bytes (Next.js SSR) |
| CSS files | 8개 외부, 총 224,081자 |
| Token prefix | `--*` (Paradox 공통 + 게임별 theme override) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (Paradox Interactive 공통 플랫폼)
- **Design system**: Paradox Design System (PDX) — 게임별 `.theme-*` 클래스로 오버라이드
- **CSS architecture**: 2-tier 토큰 + 게임 테마 계층
  ```
  core     (--color-pdx-*, --color-*)          raw hex 값 (Paradox 공통)
  theme    (.theme-aow, .theme-ck, etc.)       게임별 font/color 오버라이드
  inline   (style="--theme-color-dark:...")     페이지별 미세 조정
  ```
- **Class naming**: CSS Modules BEM-ish (`Button_button__OFOdO`, `Navigation_navbar__9Ztrx`, `heading-module heading-xl`)
- **Default theme**: dark (body bg = `#122534`, 테마 다크 = `#1A1D48`)
- **Font loading**: 셀프 호스트 eot/woff2 (Source Sans Pro, Cities 커스텀)
- **Canonical anchor**: `#E5D195` — 게임 전체를 관통하는 골드/모래빛 악센트. 버튼 테마 컬러, 텍스트 하이라이트, CTA 모두 이 색 하나로 통일

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Body font**: `Source Sans Pro` (Adobe, 오픈소스)
- **Display heading**: `Aow` (게임 커스텀, 비공개 라이선스)
- **Title font**: `SpectralSC` (Google Fonts)
- **Button font**: `SpectralSC` (게임 테마 오버라이드)
- **Content heading**: `Chakra Petch` (Google Fonts)
- **Paradox heading**: `Source Sans Pro` (기본 heading 폰트)
- **Game custom**: `Cities` (Paradox 커스텀)
- **Weight normal / bold**: `400` / `600~700`

```css
:root {
  --font-family:         "Source Sans Pro", sans-serif;
  --font-family-heading: "Source Sans Pro", sans-serif;
  --font-family-body:    "Asul", sans-serif;
  --content-theme-font:  "Chakra Petch", sans-serif;
}

/* theme-aow override (Age of Wonders 전용) */
.theme-aow {
  --font-family-heading: "Aow", sans-serif;
  --font-family-title:   "SpectralSC", sans-serif;
  --font-family-button:  "SpectralSC", sans-serif;
}

body {
  font-family: var(--font-family);
  font-weight: 400;
}
```

> **라이선스 주의**: `Aow` 는 Triumph Studios / Paradox 전용 커스텀 폰트라 재배포 불가. 외부 프로젝트에서는 `Cinzel` 이나 `Spectral SC` 가 SF-판타지 헤딩에 가장 가까운 대체재. `Cities` 도 Paradox 전용이므로 사용 불가.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Scale | Size (mobile) | Size (desktop) | Weight | Line-height |
|---|---|---|---|---|
| `heading-xxl` | 3rem (48px) | 4rem (64px) | 400 | 1.03~1.04 |
| `heading-xl`  | 2.5rem (40px) | 3rem (48px) | 400 | 1.05 |
| `heading-l`   | 2rem (32px) | 2.5rem (40px) | 400 | 1.1~1.19 |
| `heading-m`   | 1.5rem (24px) | 2rem (32px) | 400 | 1.13~1.17 |
| `heading-s`   | 1.25rem (20px) | 1.5rem (24px) | 400 | 1.17~1.2 |
| `heading-xs`  | 1rem (16px) | 1rem (16px) | 400 | 1.25 |
| `title`       | 0.75rem (12px) | 1rem (16px) | 600 | 1.0 |
| `body`        | 1rem (16px) | 18px | 400 | 1.8 (180%) |
| `body-sm`     | 0.875rem (14px) | 0.875rem | 400 | — |
| `caption`     | 0.75rem (12px) | 0.75rem | 600 | 1.0 |

> heading-module 은 게임 테마의 `--heading-theme-font` 를 소비한다. Planetfall 에서는 `Aow` 폰트가 적용되며, 기본 weight 는 `400` 이다. `title` 계열만 `600` + `uppercase` + `letter-spacing: 0.0625rem` 으로 처리한다. body text 는 `text-shadow: var(--text-shadow-readability)` 로 어두운 배경 위 가독성을 확보한다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Game Theme Colors (Planetfall palette)

| Token | Hex | Role |
|---|---|---|
| `--theme-color-dark` | `#1A1D48` | 게임 페이지 다크 배경 (nav, hero) |
| `--theme-color-light` | `#E5D195` | 골드 악센트 (border, 하이라이트) |
| `--theme-text-color` | `#E5D195` | 게임 제목·강조 텍스트 |
| `--button-theme-color` | `#E5D195` | CTA 버튼 외곽선·텍스트 |
| `--button-theme-color-dimmed` | `rgba(229,209,149,0.5)` | 버튼 비활성·hover |
| body background (inline) | `#122534` | 페이지 전체 body 배경 |

### 06-2. Text System (base · contrast · accent)

| Token | Hex | Usage |
|---|---|---|
| `--text-color-primary-base` | `#DED6C1` | 본문 텍스트 (sand) |
| `--text-color-secondary-base` | `#9B998F` | 보조 텍스트 |
| `--text-color-accent-base` | `#A38059` | 악센트 텍스트 (bronze/desert) |
| `--text-color-positive-base` | `#669A55` | 긍정 텍스트 (green) |
| `--text-color-neutral-base` | `#DED953` | 중립 텍스트 (yellow) |
| `--text-color-negative-base` | `#CE4F4F` | 부정 텍스트 (red) |
| `--text-color-announcement-base` | `#819BA3` | 안내 텍스트 (muted cyan) |
| `--text-color-disabled-base` | `#777A87` | 비활성 텍스트 |
| `--text-color-primary-contrast` | `#0E0705` | 라이트 배경 본문 (거의 흑) |
| `--text-color-secondary-contrast` | `#4A3026` | 라이트 보조 (dark brown) |
| `--text-color-accent-contrast` | `#760B18` | 라이트 악센트 (dark red) |

### 06-3. Paradox Platform Colors

| Token | Hex | Usage |
|---|---|---|
| `--color-pdx-black` | `#101010` | 카드 배경, 기본 다크 서피스 |
| `--color-pdx-black-light` | `#363636` | 카드 border, 구분선 |
| `--color-pdx-black-medium` | `#14171F` | 모달·다이얼로그 배경 |
| `--color-pdx-blue-dark` | `#0E1118` | 가장 어두운 배경 |
| `--color-pdx-blue-medium` | `#262E3E` | 중간 다크 서피스 |
| `--color-pdx-blue-medium-dark` | `#131724` | 딥 네이비 서피스 |
| `--color-pdx-grey-light` | `#D8D8D8` | 라이트 텍스트 |
| `--color-pdx-grey-medium` | `#BCBCBC` | 중간 밝기 텍스트 |
| `--color-pdx-grey` | `#717171` | muted 텍스트 |
| `--color-pdx-grey-dark` | `#666666` | dim 텍스트 |
| `--color-pdx-orange` | `#F5A623` | 할인·세일 배지 |
| `--color-pdx-pink` | `#FE0542` | 에러 |
| `--color-pdx-dracula` | `#21222C` | 드라큘라 다크 |
| `--color-valid` | `#5ABE41` | 유효·성공 |

### 06-4. Surface Colors

| Token | Hex | Usage |
|---|---|---|
| `--bg-ck3` | `#1D262C` | 게임 카드 영역 다크 배경 |
| `--color-white` | `#EAE5DE` | "white" (실제로는 warm ivory) |
| `--color-white-alternative` | `#DED6C1` | 대체 white (sand) |
| `--color-black` | `#000000` | 순수 블랙 |
| `--cta-bg-color` | `#2F1213` | CTA 섹션 배경 (deep crimson) |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--color-error` | `var(--color-pdx-pink)` → `#FE0542` | 에러 메시지 |
| `--color-valid` | `#5ABE41` | 유효 상태 |
| `--color-disabled` | `#8C8C8C` | 비활성 |
| `--color-disabled-light` | `#B3B3B3` | 비활성 (라이트) |
| `--color-disabled-dark` | `#5C5C5C` | 비활성 (다크) |

### 06-6. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto (CSS frequency count) -->

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#1D262C` | 21 | 게임 다크 배경 (bg-ck3) |
| 2 | `#FFFFFF` | 18 | 순백 (한정 사용) |
| 3 | `#000000` | 17 | 블랙 서피스 |
| 4 | `#2F323B` | 16 | 카드·패널 배경 |
| 5 | `#E5D195` | 16 | 골드 악센트 (시그너처) |
| 6 | `#DED6C1` | 14 | sand 텍스트 (primary-base) |
| 7 | `#9B8971` | 14 | desert brown |
| 8 | `#1A1D48` | 14 | 딥 블루 테마 배경 |
| 9 | `#EAE5DE` | 7 | warm ivory "white" |
| 10 | `#9B998F` | 7 | 보조 텍스트 |
| 11 | `#A38059` | 7 | bronze 악센트 |
| 12 | `#669A55` | 7 | positive green |
| 13 | `#DED953` | 7 | neutral yellow |
| 14 | `#CE4F4F` | 7 | negative red |
| 15 | `#819BA3` | 7 | announcement cyan |

---

## 07. Spacing
<!-- SOURCE: auto -->

> **네이밍 규칙**: Paradox는 rem 기반 spacing 을 사용하며, 직접 px 값도 혼용한다. 주요 간격은 `16px` (`--gap`, `--grid-padding`), `32px`, `48px`, `64px`.

| Token | Value | Use case |
|---|---|---|
| `--space` | 0.75rem (12px) | toast 내부 패딩, 콤팩트 간격 |
| `--gap` | 16px (64px 게임 섹션) | 그리드 갭 |
| `--grid-padding` | 16px | 그리드 패딩 |
| `--theme-tear-divider-top-padding` | 32px | 게임 테마 디바이더 상단 |
| `--theme-tear-divider-bottom-padding` | 48px | 게임 테마 디바이더 하단 |
| `--navbar-height` | 50px | 네비게이션 바 높이 |
| `--topbar-height-large` | 72px | 탑바 높이 (데스크톱) |
| `--footer-font-size` | 16px | 풋터 기본 글꼴 크기 |
| `--footer-logo-width` | 120px | 풋터 로고 너비 |

**주요 spacing 패턴**:
- Button min-height: `3.5rem` (56px)
- Button padding: `0.5rem 1.5rem`
- Card padding: `1.5rem` (24px)
- Section margin: `4.5rem 0` (72px)
- Modal margin: `2rem` top, `3rem` bottom

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `2px` (기본) | 2px | 버튼, 스토어 링크, 배지 — Planetfall 기본 radius |
| `3px` | 3px | 스켈레톤 로딩 |
| `4px` | 4px | 토너먼트 카드, 인풋 |
| `5px` | 5px | 특수 카드 |
| `9999px` | 9999px / 50% | 원형 버튼 (round) |

> 주의: Planetfall (그리고 Paradox 전반) 의 기본 radius 는 **2px** 로 매우 작다. 이것이 군사적·기술적 SF 느낌을 만드는 핵심. 4px 이상은 거의 쓰지 않는다.

---

## 09. Shadows
<!-- SOURCE: auto -->

> **패턴**: Paradox 게임 페이지는 전통적 `box-shadow` 보다 **text-shadow** 와 **radial-gradient** 를 더 많이 사용한다. 다크 배경 위에서 텍스트 가독성과 골드 빛 글로우 효과를 내기 위해서다.

| Level | Value | Usage |
|---|---|---|
| `--text-shadow-highlight-base` | `0 0 12px var(--text-color-accent-base)` | 골드 글로우 (링크·제목 하이라이트) |
| `--text-shadow-readability-base` | `0 0 24px #040507` | 어두운 halo (본문 가독성) |
| `--radial-shadow-highlight` | `radial-gradient(circle, rgba(163,128,89,.25) ...)` | 호버 시 골드 오라 |
| `--radial-shadow-highlight-hover` | `radial-gradient(circle, rgba(163,128,89,.5) ...)` | 호버 강조 |
| `--radial-shadow-highlight-character` | `radial-gradient(circle, rgba(222,214,193,.5) ...)` | 캐릭터 카드 배경 글로우 |
| box-shadow (카드) | `0 4px 4px 2px rgba(0,0,0,.25)` | 카드 엘리베이션 |
| box-shadow (모달) | `0 4px 8px 0 rgba(var(--color-pdx-black),0.4)` | 모달 오버레이 |
| box-shadow (인셋) | `0 0 16px 0 #000 inset` | 패널 인셋 깊이감 |

---

## 10. Motion
<!-- SOURCE: auto+manual -->

| Pattern | Value | Usage |
|---|---|---|
| 배경 전환 | `600ms ease` | 배경 이미지·색상 전환 |
| 버튼 색상 변경 | `200ms` | background-color, border-color, color 동시 전환 |
| 불투명도 페이드 | `500ms ease` / `150ms ease-out` | 페이드 인/아웃 |
| 트랜스폼 | `200ms` | nav bar translateY (스크롤 히든) |
| 슬라이딩 | `300ms ease-in-out` | 토너먼트 카드 슬라이드 드로어 |
| 일반 트랜지션 | `120ms~450ms ease-out` | 전반적 UI 인터랙션 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

### Hero
- **Layout**: 전체 폭 다크 배경, 중앙 게임 로고 이미지
- **Background**: `#1A1D48` (deep navy) + 게임 아트 배경
- **H1**: "Reclaim Your Future By Exploring The Past" — heading-xl, `Aow` 폰트, weight 400
- **Logo**: Planetfall 로고 이미지 (CTF assets CDN), 반응형 크기

### Section Rhythm
```css
section {
  padding: 2rem 0;
  max-width: var(--screen-width-medium);
  margin-inline: auto;
}
```

### Breakpoints

| Breakpoint | Value | Changes |
|---|---|---|
| Small | 480px | 2열 → 1열, 콤팩트 레이아웃 |
| Medium | 640px | 스토어 링크 3열, 모바일 nav 전환 |
| Large | 860px | 토너먼트 리스트 그리드 전환 |
| Desktop | 1024px | 전체 그리드 활성, nav 확장 |
| Wide | 1320px | 스토어 링크 4열, 최대 너비 |

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
<!-- SOURCE: auto+manual -->

### `.Button_button__*` (button)

```html
<button class="button button-solid Button_button__OFOdO Button_product__sGr9o Button_solid__o62cl">
  Buy now
</button>
<button class="button button-outlined Button_button__OFOdO Button_light__ThQs8 Button_outlined__Ibu3p">
  Watch trailer
</button>
```

| Property | Product Solid | Light Outlined |
|---|---|---|
| background | `var(--button-theme-color-dimmed)` → `rgba(229,209,149,0.5)` | transparent |
| color | `var(--color-pdx-black)` | `#FFFFFF` |
| border | 1px solid `var(--button-theme-color)` → `#E5D195` | 1px solid `#FFFFFF` |
| height | 3.5rem (56px) | 3.5rem (56px) |
| radius | 2px | 2px |
| weight | 600 | 600 |
| font | `"Source Sans Pro", sans-serif` | `"Source Sans Pro", sans-serif` |
| letter-spacing | 1px | 1px |
| text-transform | uppercase (via CSS) | uppercase |
| hover | opacity 변화 | opacity 변화 |

### `.heading-module`

- 6 scales: `xxs · xs · s · m · l · xl · xxl`
- 기본 font: `var(--heading-theme-font)` → Planetfall 에서 `"Aow", sans-serif`
- weight: `400` (heading-module 기본)
- text-shadow: `var(--text-shadow-readability)` — 다크 배경 위 가독성 확보

```html
<h2 class="heading-module heading-xl">Reclaim Your Future By Exploring The Past</h2>
<h3 class="heading-module heading-s">Main features</h3>
```

### `.Navigation_navbar__*`

- 배경: `var(--theme-color-dark)` → `#1A1D48`
- position: fixed, top: 0
- height: `var(--topbar-height-small)` / `var(--topbar-height-large)` (72px)
- 스크롤 숨김: `transform: translateY(-50px)` + `transition: transform .2s`

### `.StorefrontLinks_link-item__*`

- 스토어 버튼 (Steam, PlayStation 등)
- 배경: `var(--color-white)` (다크) / `var(--color-black)` (라이트 변형)
- border: 2px solid
- radius: 2px
- hover: 배경 투명 + SVG fill 반전
- 반응형: 50% → 33.3% → 25% → 15% 열 너비

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 명령문 or 선언문, 게임 테마 용어 사용 | "Reclaim Your Future By Exploring The Past" |
| Primary CTA | 2단어, 직접적 | "Buy now" |
| Secondary CTA | 행동 유도 | "Watch trailer" |
| Section heading | 콘텐츠 카테고리 명사 | "Introduction", "Main features", "Media", "Reviews", "Add-ons" |
| Feature text | 서술형 문단, 게임 메카닉 설명 | "Build your empire with one of six unique factions..." |
| Tone | 장대하고 서사적. SF/판타지 세계관에 맞는 문학적 표현. | — |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Age of Wonders: Planetfall — 프로젝트 루트 스타일시트에 복사 */
:root {
  /* Fonts */
  --pf-font-family:        "Source Sans Pro", sans-serif;
  --pf-font-family-heading: "Aow", sans-serif;  /* 게임 전용, 대체: Cinzel */
  --pf-font-family-title:  "SpectralSC", sans-serif;
  --pf-font-weight-normal: 400;
  --pf-font-weight-bold:   600;

  /* Game Theme */
  --pf-theme-dark:     #1A1D48;   /* 딥 네이비 */
  --pf-theme-light:    #E5D195;   /* 골드 악센트 */

  /* Surfaces */
  --pf-bg-body:        #122534;   /* body 배경 */
  --pf-bg-card:        #1D262C;   /* 카드 영역 */
  --pf-bg-panel:       #2F323B;   /* 패널 */
  --pf-bg-deep:        #101010;   /* 깊은 다크 */

  /* Text */
  --pf-text-primary:   #DED6C1;   /* sand — 본문 */
  --pf-text-secondary: #9B998F;   /* muted */
  --pf-text-accent:    #A38059;   /* bronze */
  --pf-text-disabled:  #777A87;

  /* Semantic */
  --pf-color-positive: #669A55;
  --pf-color-neutral:  #DED953;
  --pf-color-negative: #CE4F4F;
  --pf-color-info:     #819BA3;
  --pf-color-error:    #FE0542;
  --pf-color-valid:    #5ABE41;

  /* Key spacing */
  --pf-space-sm:  12px;
  --pf-space-md:  16px;
  --pf-space-lg:  32px;
  --pf-space-xl:  48px;

  /* Radius */
  --pf-radius-sm: 2px;
  --pf-radius-md: 4px;
}

body {
  font-family: var(--pf-font-family);
  font-weight: var(--pf-font-weight-normal);
  background: var(--pf-bg-body);
  color: var(--pf-text-primary);
}

h1, h2, h3 {
  font-family: var(--pf-font-family-heading);
  font-weight: 400;
  text-shadow: 0 0 24px #040507;   /* 가독성 halo */
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Age of Wonders: Planetfall
module.exports = {
  theme: {
    extend: {
      colors: {
        'theme-dark':  '#1A1D48',
        'theme-light': '#E5D195',
        surface: {
          body:  '#122534',
          card:  '#1D262C',
          panel: '#2F323B',
          deep:  '#101010',
        },
        text: {
          primary:   '#DED6C1',
          secondary: '#9B998F',
          accent:    '#A38059',
          disabled:  '#777A87',
        },
        accent: {
          gold:   '#E5D195',
          bronze: '#A38059',
          desert: '#9B8971',
        },
        semantic: {
          positive: '#669A55',
          neutral:  '#DED953',
          negative: '#CE4F4F',
          info:     '#819BA3',
          error:    '#FE0542',
          valid:    '#5ABE41',
        },
        pdx: {
          black:       '#101010',
          'black-lt':  '#363636',
          grey:        '#717171',
          'grey-med':  '#BCBCBC',
          'grey-lt':   '#D8D8D8',
          orange:      '#F5A623',
        },
      },
      fontFamily: {
        sans: ['"Source Sans Pro"', 'sans-serif'],
        heading: ['"Aow"', 'sans-serif'],
        title: ['"SpectralSC"', 'sans-serif'],
        content: ['"Chakra Petch"', 'sans-serif'],
      },
      fontWeight: {
        normal: '400',
        bold: '600',
        heavy: '700',
      },
      borderRadius: {
        sm: '2px',
        md: '4px',
        full: '9999px',
      },
      boxShadow: {
        card: '0 4px 4px 2px rgba(0,0,0,.25)',
        modal: '0 4px 8px 0 rgba(0,0,0,.4)',
        inset: '0 0 16px 0 #000 inset',
        glow: '0 0 12px rgba(163,128,89,.25)',
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
| Brand | `#E5D195` |
| Page BG | `#1A1D48` |
| Text Primary | `#000000` |
| Default Theme | dark |

### Component Prompts

> **Hero section**: "Age of Wonders: Planetfall 스타일 hero — `Source Sans Pro` 폰트, `#E5D195` brand color, dark 배경"
>
> **CTA button**: "Age of Wonders: Planetfall primary CTA — brand `#E5D195` 배경 또는 dark fill, `Source Sans Pro` 폰트"
>
> **Card component**: "Age of Wonders: Planetfall 스타일 카드 — dark 테마, 기존 radius/shadow 토큰 준수"

### Iteration Guide

1. **Color 교체 시**: 반드시 §06 Colors 테이블의 실제 hex 참조. AI 추론 색상 사용 금지.
2. **Typography 변경 시**: §04 Font Stack의 font-family 체인 + §05의 weight/size 매핑 확인.
3. **Spacing 조정 시**: §07 Spacing의 토큰 스케일 내에서만 변경.
4. **신규 컴포넌트**: §13 Components의 기존 패턴(radius, shadow, padding)을 기반으로 확장.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO
- `#1A1D48` 을 게임 페이지 primary dark 배경으로 사용. 순수 검정이 아니라 딥 네이비.
- `#E5D195` 골드를 모든 CTA 와 강조 요소에 일관되게 적용. 이것이 Planetfall 시그너처.
- 본문 텍스트는 `#DED6C1` (sand). 순백 `#FFFFFF` 가 아님 — 따뜻한 아이보리 톤.
- heading 에 `text-shadow: 0 0 24px #040507` 가독성 halo 를 반드시 넣을 것.
- 버튼 radius 는 `2px` — SF/밀리터리 느낌의 핵심. 둥글게 만들지 말 것.
- `Source Sans Pro` 를 body 기본으로. weight `400` 이 표준, `600` 이 bold.
- heading 에 게임 커스텀 폰트 (`Aow` 또는 대체재) 를 사용해 세계관 몰입감 유지.
- 호버 효과에 radial-gradient 골드 글로우 사용 — Paradox 게임 페이지의 시그너처 인터랙션.
- `letter-spacing: 1px` + `text-transform: uppercase` 를 버튼·타이틀에 적용.

### DON'T
- 배경을 `#000000` 순수 검정으로 두지 마라 — `#1A1D48` (딥 네이비) 이 정답.
- 본문을 `#FFFFFF` 순백으로 두지 마라 — 눈이 피로하고 게임 분위기가 깨진다. `#DED6C1` 사용.
- 버튼 radius 를 `8px` 이상으로 올리지 마라 — SF/판타지 게임 톤이 무너진다. `2px` 유지.
- `--color-white` 가 `#FFFFFF` 라고 가정하지 마라 — 실제 값은 `#EAE5DE` (warm ivory).
- 골드 악센트를 여러 색으로 분산하지 마라 — `#E5D195` 하나로 통일이 핵심.
- 밝은 테마를 기본으로 가정하지 마라 — 이 서비스는 완전한 다크 테마 전용.
- heading 을 `700` 으로 두지 마라 — Planetfall heading 은 `400` 이 기본.
- `text-shadow` 를 제거하지 마라 — 다크 배경 위 가독성의 핵심 장치.
- 일반 SaaS 톤의 깔끔한 무채색 디자인을 적용하지 마라 — 게임 페이지는 텍스처·글로우·서사적 분위기가 정체성.
