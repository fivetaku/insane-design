---
slug: sonos
service_name: Sonos
site_url: https://www.sonos.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#DE8579"
primary_font: aktiv-grotesk
font_weight_normal: 400
token_prefix: --color-*
---

# DESIGN.md — Sonos (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Sonos의 디지털 인터페이스는 라이트 테마를 기본으로 한다. 밝은 배경 위에 브랜드 컬러 `#DE8579`가 절제적으로 사용되어 깔끔하고 신뢰감 있는 시각적 인상을 만든다.

색상 전략은 `#DE8579`, `#C59C6E`, `#FFFFFF` 등을 중심으로 구성된다. 브랜드의 canonical 컬러인 `#DE8579`가 CTA와 주요 인터랙션 요소에 사용되며, 나머지 뉴트럴 팔레트가 배경과 텍스트 계층을 형성한다.

타이포그래피는 `aktiv-grotesk` 폰트를 중심으로 브랜드 고유의 성격을 표현한다. 기본 weight 400으로 본문을 구성하며, heading에서 더 무거운 weight를 사용해 시각적 위계를 만든다.

레이아웃은 풀 너비 히어로 섹션과 콘텐츠 영역의 리듬감 있는 교차로 구성된다. 충분한 여백을 활용하여 콘텐츠에 시각적 호흡 공간을 부여하고, 핵심 메시지와 CTA에 자연스럽게 시선을 유도한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Sonos처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "aktiv-grotesk", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #2E2E2E; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 테라코타 */
:root { --brand: #DE8579; }
```

**절대 하지 말아야 할 것 하나**: Sonos의 브랜드 컬러를 표준 오렌지나 레드로 대체하는 것. `#DE8579`는 로즈 테라코타 — 차갑지도 뜨겁지도 않은 절제된 따뜻함이다. 일반 `#FF5500` 같은 오렌지를 쓰면 하이엔드 오디오 브랜드가 소비재처럼 보인다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.sonos.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA |
| HTML size | N/A bytes |
| CSS files | Tailwind 기반 + 커스텀 컬러 토큰 |
| Token prefix | `--color-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js / React (Tailwind CSS 사용)
- **Design system**: 자체 DS — `--color-accentRed`, `--color-accentGold` 토큰
- **CSS architecture**: Tailwind utility + 커스텀 프로퍼티 결합
- **Class naming**: Tailwind (.tw-sticky-nav 등 prefix)
- **Default theme**: light (흰 배경, 다크 그레이 텍스트)
- **Font loading**: Adobe Fonts로 `aktiv-grotesk` 서빙 (TypeKit)
- **Canonical anchor**: `#DE8579` — `--color-accentRed` 명시, 3회 사용

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary font**: `aktiv-grotesk` (Adobe Fonts / Dalton Maag)
- **Fallback**: Helvetica, Arial, sans-serif
- **Weight system**: 100(thin), 300(light), 400(regular), 500(medium), 600(semibold), 700(bold)

```css
body {
  font-family: aktiv-grotesk, Helvetica, Arial, sans-serif;
  font-weight: 400;
}
```

> **라이선스**: `aktiv-grotesk`는 Adobe Fonts 구독 또는 TypeKit 라이선스 필요. 오픈소스 대체재: `Inter` 또는 `DM Sans` (시각적으로 유사).

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | 크기 | Weight |
|---|---|---|
| Hero Display | clamp(40px, 6vw, 80px) | 700 |
| Section Title | 36px–48px | 600–700 |
| Card Title | 20px–24px | 500–600 |
| Body | 15px–17px | 400 |
| Caption | 12px–13px | 300–400 |
| Nav item | 14px | 500 |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Accent (브랜드)

| Token | Hex | 역할 |
|---|---|---|
| --color-accentRed | `#DE8579` | 주요 CTA, 하이라이트 |
| --color-accentGold | `#C59C6E` | 보조 액센트, 고급감 |

### Neutrals (frequency 상위)

| Hex | Count | 역할 |
|---|---|---|
| `#FFFFFF` | 372 | 기본 배경 |
| `#000000` | 87 | 진한 텍스트 |
| `#2E2E2E` | 71 | 메인 텍스트 |
| `#4C4C4C` | 43 | 보조 텍스트 |
| `#424242` | 26 | 아이콘, 보더 |
| `#7F7F7F` | 26 | 플레이스홀더 |
| `#BCBCBC` | 32 | 연한 보더 |
| `#E0E0E0` | 17 | 섀도우 (nav 보더) |
| `#EEEEEE` | 13 | 배경 섹션 |

---

## 07. Spacing
<!-- SOURCE: manual -->

| Step | Value | 용도 |
|---|---|---|
| xs | 4px | 아이콘 |
| sm | 8px | 인라인 |
| md | 16px | 컴포넌트 |
| lg | 24px | 카드 내부 |
| xl | 40px | 섹션 내부 |
| 2xl | 64px | 섹션 간 |
| 3xl | 96px | 히어로 |
| 4xl | 128px | 대섹션 |

---

## 08. Radius
<!-- SOURCE: manual -->

| 역할 | Radius |
|---|---|
| Button | 4px–8px |
| Card | 8px–12px |
| Image | 0px (square) |
| Pill / Badge | 999px |
| Input | 4px |

---

## 09. Shadows
<!-- SOURCE: auto+manual -->

| 레이어 | CSS |
|---|---|
| Nav (sticky) | `inset 0 -1px 0 #E0E0E0` |
| Card hover | `0 0 24px rgba(0,0,0,.25)` |
| Button press | `0 2px 8px rgba(0,0,0,.15)` |

---

## 10. Motion
<!-- SOURCE: manual -->

| 패턴 | Duration | Easing |
|---|---|---|
| Button hover | 180ms | ease |
| Nav 스크롤 | 200ms | ease-out |
| Image fade | 300ms | ease |
| 페이지 전환 | 400ms | ease-in-out |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **히어로**: 풀 블리드 제품 이미지 + 텍스트 오버레이, max-width 1440px
- **제품 그리드**: 3-4 column, 충분한 white space
- **Sticky Nav**: height 4rem, `--tw-bg-opacity: 1`, 흰 배경 + inset 하단 보더
- **섹션**: `padding: 80px 64px`, 번갈아 흰/회색 배경
- **컨테이너**: `max-width: 1280px; margin: 0 auto`

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
<!-- SOURCE: manual -->

### Primary CTA Button

```css
.btn-primary {
  background: #DE8579;  /* --color-accentRed */
  color: #FFFFFF;
  border: none;
  border-radius: 6px;
  padding: 14px 28px;
  font-family: aktiv-grotesk, Helvetica, Arial, sans-serif;
  font-weight: 500;
  font-size: 15px;
  transition: all 180ms ease;
}
.btn-primary:hover {
  background: #C9706A;  /* 약간 어두운 hover */
}
```

### Product Card

```css
.product-card {
  background: #FFFFFF;
  border-radius: 8px;
  overflow: hidden;
}
.product-card:hover .card-image {
  transform: scale(1.02);
  transition: transform 300ms ease;
}
```

### Gold Accent Badge

```css
.badge-gold {
  background: #C59C6E;  /* --color-accentGold */
  color: #FFFFFF;
  border-radius: 999px;
  padding: 4px 12px;
  font-size: 12px;
  font-weight: 600;
}
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

- **헤드라인**: 감성적, 경험 중심. "Fill every room with sound."
- **바디**: 기술과 감성의 균형. 스펙보다 청취 경험을 먼저
- **CTA**: "Shop speakers", "Explore", "Add to cart"
- **어조**: 프리미엄, 따뜻함, 일상의 럭셔리

---

## 15. Drop-in CSS
<!-- SOURCE: manual -->

```css
/* Sonos Design System — Drop-in */
:root {
  --color-accentRed:  #DE8579;
  --color-accentGold: #C59C6E;

  --color-text-primary:   #2E2E2E;
  --color-text-secondary: #4C4C4C;
  --color-text-muted:     #7F7F7F;

  --color-bg-page:    #FFFFFF;
  --color-bg-section: #EEEEEE;
  --color-border:     #BCBCBC;
  --color-border-str: #E0E0E0;

  --font-primary: "aktiv-grotesk", Helvetica, Arial, sans-serif;

  --space-xs:  4px;
  --space-sm:  8px;
  --space-md:  16px;
  --space-lg:  24px;
  --space-xl:  40px;
  --space-2xl: 64px;
}

body {
  font-family: var(--font-primary);
  font-weight: 400;
  background: var(--color-bg-page);
  color: var(--color-text-primary);
}
```

---

## 16. Tailwind Config
<!-- SOURCE: manual -->

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        accent: {
          red:  '#DE8579',
          gold: '#C59C6E',
        },
        neutral: {
          900: '#2E2E2E',
          700: '#4C4C4C',
          500: '#7F7F7F',
          300: '#BCBCBC',
          200: '#E0E0E0',
          100: '#EEEEEE',
        },
      },
      fontFamily: {
        sans: ['aktiv-grotesk', 'Helvetica', 'Arial', 'sans-serif'],
      },
    },
  },
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#DE8579` |
| Background | bg-page | `#FFFFFF` |
| Text primary | text | `#2E2E2E` |
| Text muted | text-muted | `#7F7F7F` |
| Border | border | `#BCBCBC` |

### Example Component Prompts

#### Hero Section
```
Sonos 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: aktiv-grotesk, weight 700
- 서브텍스트: #7F7F7F
- CTA 버튼: 배경 #DE8579, 텍스트 white
```

#### Card Component
```
Sonos 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF, border: 1px solid #BCBCBC
- radius: 4px
- 제목: aktiv-grotesk, 16px, weight 700
- 본문: 14px, color #2E2E2E
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

### DO

- `#DE8579` 테라코타를 CTA에 사용 — 이 컬러가 Sonos의 따뜻함
- `#C59C6E` 골드를 프리미엄 배지, 보조 액센트에 활용
- `aktiv-grotesk` 또는 `Inter` 사용 — 기술적이면서 따뜻한 느낌
- 충분한 white space — 하이엔드 오디오 브랜드의 여백
- 제품 사진은 크고 선명하게 — 시각적 프레전스가 핵심

### DON'T

- 일반 오렌지/레드로 브랜드 컬러 대체 — `#DE8579` 특유의 절제된 따뜻함
- 과도한 포인트 컬러 — 테라코타 + 골드 2가지면 충분
- 배경에 강한 색상 — Sonos는 흰 배경이 프리미엄 신호
- 작은 제품 이미지 — Sonos는 제품이 주인공

### 자주 하는 오해 vs 실제

| 오해 | 실제 |
|---|---|
| 브랜드 컬러가 검정 | 검정은 텍스트. 브랜드는 `#DE8579` 테라코타 |
| 일반 오렌지로 대체 가능 | `#DE8579`는 로즈 테라코타 — 오렌지와 전혀 다름 |
| 무채색 브랜드 | 따뜻한 테라코타 + 골드 2색 액센트 시스템 |
