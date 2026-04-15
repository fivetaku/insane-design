---
slug: spotify
service_name: Spotify
site_url: https://open.spotify.com
fetched_at: 2026-04-11
default_theme: dark
brand_color: "#1ED760"
primary_font: SpotifyMixUI
font_weight_normal: 400
token_prefix: "--encore-*"
---

# DESIGN.md — Spotify (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Spotify의 웹사이트는 다크 배경(`#121212`) 위에 브랜드 그린 `#1ED760`이 빛나는 음악 스트리밍 서비스의 시그니처 디자인이다. 콘텐츠(앨범 아트, 아티스트 이미지)가 주인공이 되도록 UI는 최대한 어둡고 절제된다.

타이포그래피는 Spotify 자체 제작 `SpotifyMixUI`(본문)와 `SpotifyMixUITitle`(헤딩)을 사용한다. 본문 weight는 **400**, 헤딩 최대 weight는 **700**이다. 900 weight는 사용하지 않는다.

브랜드 그린 `#1ED760`(레거시 `#1DB954`가 아님)이 CTA, 재생 버튼, active 상태에 집중 사용된다. hover(`#3BE477`) / press(`#1ABC54`) variant로 인터랙션 상태를 정밀하게 표현한다.

**Key Characteristics:**
- 브랜드 그린 `#1ED760` 하나만 사용. Hover 는 `#3BE477`, press 는 `#1ABC54`.
- Body 는 `SpotifyMixUI`, Title/Headline 은 `SpotifyMixUITitle` — 자체 호스팅 variable 폰트.
- Weight 는 `400` 또는 `700` 만. 500/600/800/900 절대 사용 금지.
- 기본 테마는 dark. 페이지 배경 `#121212`, elevated 카드 `#1F1F1F`, hover `#2A2A2A`.
- Text 대비: primary `#FFFFFF`, subdued `#B3B3B3` (WCAG AA 통과).
---

## 01. Quick Start

> 5분 안에 Spotify처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트: SpotifyMixUI body + SpotifyMixUITitle heading */
body {
  font-family: "SpotifyMixUI", -apple-system, system-ui, sans-serif;
  font-weight: 400;
}
h1, h2, h3 {
  font-family: "SpotifyMixUITitle", -apple-system, system-ui, sans-serif;
  font-weight: 700;  /* Spotify 는 900 없음 — 700 이 최대 */
}

/* 2. 배경 + 텍스트 (dark 고정) */
:root { --bg: #121212; --fg: #FFFFFF; --fg-muted: #B3B3B3; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 — green 1색뿐, pure green 아님 */
:root { --brand: #1ED760; }  /* NOT #1DB954 (구 로고색), NOT #00FF00 */
```

**절대 하지 말아야 할 것 하나**: Spotify 브랜드 그린을 `#1DB954`(레거시 로고 색) 또는 `#1DD1A1`(유사 민트) 로 쓰지 말 것. 실제 CSS 에는 `#1ED760`(37회, 압도적 1위)만 존재한다. 버튼/포커스/active 상태 전부 `#1ED760` 또는 그 variant `#3BE477`(12회, hover) / `#1ABC54`(12회, press).

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://open.spotify.com` (web player) |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | ~231KB (React SPA shell) |
| CSS files | 2개 외부, 총 446,360자 |
| Primary bundle | `web-player.c237e3fa.css` |
| Token prefix | `--encore-*` (Spotify Encore Design System) |
| Method | 305개 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: React SPA (web player). 마케팅 페이지 아님 — 제품 UI 자체.
- **Design system**: **Encore** — Spotify 의 공식 내부 DS. 모든 토큰 `--encore-*` prefix.
- **CSS architecture**: 5-tier semantic hierarchy
  ```
  --encore-{prop}-{scale}        raw token (예: --encore-spacing-base: 16px)
  --encore-text-size-*           typography scale (smaller-3 ~ larger-5)
  --encore-corner-radius-*       smaller/base/larger
  --background-*, --text-*       semantic theme tokens
  --essential-*                  state tokens (base, bright-accent, warning, negative)
  ```
- **Class naming**: `.encore-text-{category}-{size}` + `.e-10180-{component}` (hashed component classes)
- **Default theme**: **dark 고정**. `--background-base: #121212`. Light mode 미지원.
- **Font loading**: 자체 호스팅 `SpotifyMixUI` / `SpotifyMixUITitle` / `CircularSp-*` (언어별) + `SpotifyMixMono` 코드용.
- **Canonical anchor**: `#1ED760` — 브랜드 그린, 버튼/프로그레스바/active 상태 전부.

---

## 04. Font Stack

- **Display/title font**: `SpotifyMixUITitle` (Spotify 자체 제작 variable 폰트, 유료)
- **Body font**: `SpotifyMixUI`
- **Language-specific fallbacks**: `CircularSp-Arab`, `CircularSp-Hebr`, `CircularSp-Cyrl`, `CircularSp-Grek`, `CircularSp-Deva` (Circular Sp는 Spotify 전용 버전)
- **Code font**: `SpotifyMixMono`
- **Weight normal / bold**: `400` / `700` (최대). Weight 800/900 존재하지만 거의 미사용.

```css
:root {
  --encore-title-font-stack:
    SpotifyMixUITitle, CircularSp-Arab, CircularSp-Hebr, CircularSp-Cyrl,
    CircularSp-Grek, CircularSp-Deva, sans-serif;
  --encore-body-font-stack:
    SpotifyMixUI, CircularSp-Arab, CircularSp-Hebr, CircularSp-Cyrl,
    CircularSp-Grek, CircularSp-Deva, sans-serif;
  --encore-bodyMono-font-stack:
    SpotifyMixMono, CircularSp-Arab, CircularSp-Hebr, CircularSp-Cyrl,
    CircularSp-Grek, CircularSp-Deva, monospace;
}
body {
  font-family: var(--encore-body-font-stack);
  font-weight: 400;
}
```

> ⚠️ **Circular 이 아니라 SpotifyMixUI 가 primary.** `Circular Std` 는 Spotify 의 과거 폰트였고, 현재는 자체 variable `SpotifyMixUITitle`/`SpotifyMixUI` 가 기본. `Circular-Sp-*` 는 비라틴 fallback 전용으로만 등장.

---

## 05. Typography Scale

| Token | Size | Class | Weight | Usage |
|---|---|---|---|---|
| `--encore-text-size-smaller-3` | `.5625rem` / 9px | `.encore-text-marginal-small` | 400/700 | 초소형 캡션 |
| `--encore-text-size-smaller-2` | `.6875rem` / 11px | `.encore-text-marginal` | 400/700 | 마진 메타데이터 |
| `--encore-text-size-smaller` | `.8125rem` / 13px | `.encore-text-body-small` | 400/700 | 본문 small |
| `--encore-text-size-base` | `1rem` / 16px | `.encore-text-body-medium` | 400/700 | 본문 기본 |
| `--encore-text-size-large` | `1.125rem` / 18px | `.encore-text-title-extra-small` | 700 | 소형 타이틀 |
| `--encore-text-size-larger` | `1.25rem` / 20px | `.encore-text-title-small` | 700 | 섹션 타이틀 |
| `--encore-text-size-larger-2` | `1.5rem` / 24px | `.encore-text-title-medium` | 700 | 카드 타이틀 |
| `--encore-text-size-larger-3` | `2rem` / 32px | `.encore-text-title-large` | 700 | 페이지 타이틀 |
| `--encore-text-size-larger-4` | `2.5rem` / 40px | `.encore-text-headline-medium` | 700 | 헤드라인 |
| `--encore-text-size-larger-5` | `3rem` / 48px | `.encore-text-headline-large` | 700 | 대형 헤드라인 |

> ⚠️ **Weight 는 400/700 두 개만.** Spotify 의 모든 `encore-text-*` 클래스는 `font-weight: 400` 아니면 `700`. 500/600/800/900 은 제품 UI 에서 쓰이지 않는다. `text-wrap: balance` 가 모든 title/headline 에 기본 적용 — 자동 줄 균형.

---

## 06. Colors

### 06-1. Brand Green

| Token | Hex | Count | Usage |
|---|---|---|---|
| `--text-bright-accent` / `--essential-bright-accent` | `#1ED760` | 37 | 브랜드 · 버튼 · active |
| accent-hover | `#3BE477` | 12 | hover state (밝은 변형) |
| accent-press | `#1ABC54` | 12 | press state (어두운 변형) |
| accent-text | `#1ED760` | (동일) | `--text-positive` 도 동일값 |

### 06-2. Background (dark)

| Token | Hex | Usage |
|---|---|---|
| `--background-base` | `#121212` | 페이지 배경 (메인) |
| `--background-highlight` | `#1F1F1F` | hover 배경 |
| `--background-press` | `#000000` | press 배경 |
| `--background-elevated-base` | `#1F1F1F` | 카드 · 모달 |
| `--background-elevated-highlight` | `#2A2A2A` | 카드 hover |
| `--background-elevated-press` | `#191919` | 카드 press |
| `--background-tinted-base` | `#FFFFFF1A` | 10% white overlay |
| `--background-tinted-highlight` | `#FFFFFF24` | 14% white overlay |
| `--background-tinted-press` | `#FFFFFF36` | 21% white overlay |
| surface-alt | `#282828` | 툴팁 · 드롭다운 |
| surface-alt-2 | `#141414` | 특정 드롭다운 배경 |

### 06-3. Text

| Token | Hex | Usage |
|---|---|---|
| `--text-base` | `#FFFFFF` | primary text |
| `--text-subdued` | `#B3B3B3` | secondary text |
| `--text-negative` | `#F3727F` | 에러 · 경고 텍스트 |
| `--text-warning` | `#FFA42B` | 경고 |
| `--text-positive` / `--text-bright-accent` | `#1ED760` | 성공 · 브랜드 강조 |
| `--text-announcement` | `#539DF5` | 공지 · info |

### 06-4. Decorative Pairs (카테고리별 듀얼톤)

| Pair | Light / Dark | Usage |
|---|---|---|
| Red/Rose | `#FFD2D7` / `#590810` | 러브송 · R&B 카드 (각 20회) |
| Amber | `#FFD97E` / `#491E00` | 팝 · 어쿠스틱 카드 (각 20회) |
| Green | `#96F0B6` / `#073116` | 칠 · 힙합 카드 (각 20회) |
| Blue | `#C8E0FC` / `#052A56` | 슬립 · 클래식 카드 (각 20회) |

> ⚠️ **이 4쌍은 항상 light-on-dark 로 써라.** 각 카테고리 카드의 배경/전경 쌍이며, 혼용하면 명도 대비가 깨진다. WCAG AA 대비비 유지.

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--essential-bright-accent` | `#1ED760` | 브랜드 · 포커스 ring |
| `--essential-warning` | `#FFA42B` | 경고 아이콘 |
| `--essential-negative` | `#F3727F` (추정) | 에러 · focus-outline-color |
| `--essential-announcement` | `#0D72EA` | 정보 |
| accent-red | `#E91429` | 알림 · 라이브 |

### 06-6. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 279 | primary text |
| 2 | `#000000` | 193 | press · overlay |
| 3 | `#FFFFFF1A` | 44 | tinted overlay 10% |
| 4 | `#1ED760` | 37 | **브랜드 그린** |
| 5 | `#FFFFFFB3` | 27 | tinted text 70% |
| 6 | `#121212` | 24 | **페이지 배경** |
| 7 | `#282828` | 23 | surface elevated |
| 8 | `#590810` / `#491E00` / `#073116` / `#052A56` | 20 each | 카테고리 dark bg |
| 9 | `#FFD2D7` / `#FFD97E` / `#96F0B6` / `#C8E0FC` | 20 each | 카테고리 light fg |
| 10 | `#B3B3B3` | 17 | text-subdued |

---

## 07. Spacing

> `--encore-spacing-*` 토큰은 `tighter-5` ~ `looser-6` 의 11단계. 기본 단위 `16px`. 반응형에서 `looser-*` 스텝이 큰 값으로 확장.

| Token | Value | Context |
|---|---|---|
| `--encore-spacing-tighter-5` | `2px` | 아이콘 간격 |
| `--encore-spacing-tighter-4` | `4px` | 인라인 간격 |
| `--encore-spacing-tighter-3` | `6px` | 칩 내부 |
| `--encore-spacing-tighter-2` | `8px` | 작은 gap |
| `--encore-spacing-tighter` | `12px` | 리스트 행 |
| `--encore-spacing-base` | `16px` | 기본 gap |
| `--encore-spacing-looser` | `20px` (desktop `24px`) | 블록 간격 |
| `--encore-spacing-looser-2` | `24px` (desktop `32px`) | 섹션 패딩 |
| `--encore-spacing-looser-3` | `32px` (desktop `48px`) | 섹션 gap |
| `--encore-spacing-looser-4` | `40px` (desktop `64px`) | hero padding |
| `--encore-spacing-looser-5` | `48px` (desktop `96px`) | 큰 섹션 |
| `--encore-spacing-looser-6` | `64px` (desktop `128px`) | 페이지 max |

**주요 alias**:
- `--content-spacing` → `16px`
- `--modal-gap` → `24px`
- `--shelf-gap-horizontal` → `32px`
- `--shelf-gap-vertical` → `24px`

---

## 08. Radius

| Token | Value | Context |
|---|---|---|
| `--encore-corner-radius-smaller` | `2px` | 이미지 · 작은 아이콘 |
| `--encore-corner-radius-base` | `4px` | 기본 (51회, 1위) |
| `--encore-corner-radius-larger` | `6px` | 리스트 row |
| ad-hoc | `8px` | 카드 (41회) |
| ad-hoc | `16px` | 큰 카드 (9회) |
| pill | `100px` | 플레이 버튼 원형 |
| pill-large | `500px` | 완전 원형 CTA |

> ⚠️ **Spotify radius 시스템은 3단 토큰 (2/4/6px)뿐.** 8px 이상은 raw 값으로 ad-hoc. 플레이 버튼 같은 원형은 `100px` / `500px` 로 강제 원형.

---

## 09. Shadows

| Token | Value | Usage |
|---|---|---|
| `--encore-overlay-box-shadow` | `0 16px 24px #0000004D, 0 6px 8px #00000033` | 모달 · 팝오버 |
| `--encore-overlay-drop-shadow` | `0 4px 6px #0000004D` | 드롭다운 |
| `--encore-focus-box-shadow` | `0 3px 0 0` (color 변수) | 인라인 focus underline |
| elevation-max | `0 52px 52px -20px #0000004D, 0 4px 20px #0000001A` | 풀페이지 오버레이 |
| inset-border | `0 0 0 1px var(--essential-subdued) inset` | 보더 대체 |

> ⚠️ **Focus 는 outline 기반.** Spotify 는 `outline: var(--encore-border-width-focus, 3px) solid var(--parents-essential-base)` 을 쓴다. `box-shadow` 기반 focus 는 예외적.

---

## 10. Motion

| Token | Value | Usage |
|---|---|---|
| `--encore-shortest-3` | 짧은 transition duration (hash 뒤 숨김) | 텍스트 컬러 변화 |
| `--encore-productive` | easing 함수 | UI 인터랙션 |
| `--encore-opacity-disabled` | ~0.5 | disabled 상태 |

---

## 11. Layout Patterns

### Web player
- Layout: sidebar + now-playing footer + main content grid
- Background: `#121212` 고정
- Max-width: `--content-max-width` (반응형)
- Sidebar: `--encore-app-inline-size` 에 의해 폭 결정

### Shelf carousel
```css
.shelf {
  gap-horizontal: 32px;   /* --shelf-gap-horizontal */
  gap-vertical:   24px;   /* --shelf-gap-vertical */
  margin: calc(40px + var(--encore-cards-margin) + max(0px, (var(--home-full-width) - var(--content-max-width)) * 0.5));
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

> ⚠️ Spotify는 모바일 퍼스트 반응형 디자인을 채택하며, 브레이크포인트별로 그리드와 타이포그래피가 유동적으로 조정된다.

---

## 13. Components

### Button (primary)

```html
<button class="e-10180-button e-10180-button-primary">
  <span class="e-10180-button__children">Play</span>
</button>
```

```css
.e-10180-button-primary {
  background: #1ED760;
  color: #000000;
  font-family: var(--encore-body-font-stack);
  font-weight: 700;
  border-radius: 500px;   /* 완전 원형 pill */
  padding: 0 32px;
  min-block-size: var(--encore-control-size-base);
}
.e-10180-button-primary:hover { background: #3BE477; transform: scale(1.04); }
.e-10180-button-primary:active { background: #1ABC54; transform: scale(1.00); }
```

### Text helpers (semantic)

```html
<h1 class="encore-text encore-text-headline-large">Good morning</h1>
<h2 class="encore-text encore-text-title-large">Made for you</h2>
<p class="encore-text encore-text-body-medium">New releases weekly.</p>
<span class="encore-text encore-text-marginal">2 hr 34 min</span>
```

### List row

```html
<li class="e-10180-list-row">
  <img class="e-10180-list-row__image" />
  <span class="encore-text encore-text-body-medium-bold">Track name</span>
  <span class="encore-text encore-text-body-small">Artist</span>
</li>
```

```css
.e-10180-list-row {
  background: var(--encore-list-row-bg, transparent);
  border-radius: var(--encore-list-row-border-radius, 6px);
}
.e-10180-list-row:hover { background: var(--background-highlight); }  /* #1F1F1F */
.e-10180-list-row:active { background: var(--background-press); }     /* #000 */
```

### Card

```html
<article class="e-10180-card e-10180-card--elevated">…</article>
```

```css
.e-10180-card--elevated {
  background: var(--background-elevated-base);    /* #1F1F1F */
  border-radius: 8px;
  padding: 16px;
  transition: background 200ms;
}
.e-10180-card--elevated:hover { background: var(--background-elevated-highlight); }
```

---

## 15. Drop-in CSS

```css
/* Spotify — copy into your root stylesheet */
:root {
  /* Fonts */
  --encore-title-font-stack: SpotifyMixUITitle, CircularSp-Arab, CircularSp-Hebr, CircularSp-Cyrl, CircularSp-Grek, CircularSp-Deva, sans-serif;
  --encore-body-font-stack:  SpotifyMixUI, CircularSp-Arab, CircularSp-Hebr, CircularSp-Cyrl, CircularSp-Grek, CircularSp-Deva, sans-serif;
  --encore-bodyMono-font-stack: SpotifyMixMono, monospace;

  /* Brand (single anchor) */
  --encore-brand-25:   #96F0B6;   /* pale green (decorative) */
  --encore-brand-300:  #3BE477;   /* hover */
  --encore-brand-500:  #1ED760;   /* ← canonical */
  --encore-brand-600:  #1ABC54;   /* press */
  --encore-brand-900:  #073116;   /* decorative dark */

  /* Surfaces (dark only) */
  --background-base:             #121212;
  --background-highlight:        #1F1F1F;
  --background-press:            #000000;
  --background-elevated-base:    #1F1F1F;
  --background-elevated-highlight: #2A2A2A;
  --background-tinted-base:      rgba(255, 255, 255, 0.1);
  --text-base:                   #FFFFFF;
  --text-subdued:                #B3B3B3;

  /* Key spacing */
  --encore-spacing-tighter-2: 8px;
  --encore-spacing-base:      16px;
  --encore-spacing-looser-2:  24px;
  --encore-spacing-looser-3:  32px;

  /* Radius */
  --encore-corner-radius-smaller: 2px;
  --encore-corner-radius-base:    4px;
  --encore-corner-radius-larger:  6px;
}

body {
  font-family: var(--encore-body-font-stack);
  font-weight: 400;
  background: var(--background-base);
  color: var(--text-base);
}
h1, h2, h3 {
  font-family: var(--encore-title-font-stack);
  font-weight: 700;
  text-wrap: balance;
}
```

---

## 16. Tailwind Config

```js
// tailwind.config.js — Spotify
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '#96F0B6',   // decorative pale
          300: '#3BE477',   // hover
          500: '#1ED760',   // canonical
          600: '#1ABC54',   // press
          900: '#073116',   // decorative dark
        },
        bg: {
          base:    '#121212',
          highlight: '#1F1F1F',
          press:   '#000000',
          elevated: '#1F1F1F',
          'elevated-highlight': '#2A2A2A',
          surface:  '#282828',
        },
        text: {
          base:     '#FFFFFF',
          subdued:  '#B3B3B3',
          negative: '#F3727F',
          warning:  '#FFA42B',
          positive: '#1ED760',
          announcement: '#539DF5',
        },
      },
      fontFamily: {
        sans:  ['SpotifyMixUI', 'system-ui', 'sans-serif'],
        title: ['SpotifyMixUITitle', 'system-ui', 'sans-serif'],
        mono:  ['SpotifyMixMono', 'ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        bold:   '700',
      },
      spacing: {
        '0.5': '2px', '1': '4px', '1.5': '6px', '2': '8px',
        '3': '12px', '4': '16px', '5': '20px', '6': '24px',
        '8': '32px', '10': '40px', '12': '48px', '16': '64px',
      },
      borderRadius: {
        xs:   '2px',
        sm:   '4px',
        md:   '6px',
        lg:   '8px',
        pill: '500px',
      },
      boxShadow: {
        overlay: '0 16px 24px rgba(0,0,0,0.3), 0 6px 8px rgba(0,0,0,0.2)',
        drop:    '0 4px 6px rgba(0,0,0,0.3)',
        max:     '0 52px 52px -20px rgba(0,0,0,0.3), 0 4px 20px rgba(0,0,0,0.1)',
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
| Primary CTA | `#1ED760` |
| Heading text | `#FFFFFF` |
| Body text | `#B3B3B3` |
| Background | `#121212` |
| Border | `#282828` |
| Link | `#1ED760` |
| Dark section | `#121212` |

### Example Component Prompts
- "Create a hero section on `#121212` background. Headline at 3rem `SpotifyMixUI` weight 400. CTA button `#1ED760` with white text."
- "Design a card: `#FFFFFF` background, `#282828` border, 8px radius. Body text `#B3B3B3` at weight 400."

### Iteration Guide
1. 폰트: `SpotifyMixUI` 패밀리, 본문 weight 400
2. 컬러: 브랜드 `#1ED760`는 CTA/링크에만 집중. 배경 `#121212`, 텍스트 `#FFFFFF`
3. 그림자: 다크 테마에서 카드 배경색 차이로 elevation 표현
---

## 18. DO / DON'T

### ✅ DO
- 브랜드 그린 `#1ED760` 하나만 사용. Hover 는 `#3BE477`, press 는 `#1ABC54`.
- Body 는 `SpotifyMixUI`, Title/Headline 은 `SpotifyMixUITitle` — 자체 호스팅 variable 폰트.
- Weight 는 `400` 또는 `700` 만. 500/600/800/900 절대 사용 금지.
- 기본 테마는 dark. 페이지 배경 `#121212`, elevated 카드 `#1F1F1F`, hover `#2A2A2A`.
- Text 대비: primary `#FFFFFF`, subdued `#B3B3B3` (WCAG AA 통과).
- 원형 CTA 는 `border-radius: 500px` 또는 `100px` — 완전 원형.
- Title/headline 에는 `text-wrap: balance` 기본 적용.
- Focus 는 `outline: 3px solid` (box-shadow 아님).

### ❌ DON'T
- ❌ `#1DB954` 레거시 로고 그린 (현재 CSS 에 없음 — 2021년 이전 색)
- ❌ `#00FF00` 또는 `#1DD1A1` 같은 유사 그린 (공식 아님)
- ❌ `Circular Std` 폰트 (과거 Spotify 폰트, 현재 `SpotifyMixUI` 로 대체됨)
- ❌ Light mode 지원 가정 (`#121212` 고정 dark, light variant 없음)
- ❌ `font-weight: 500` / `600` / `900` (Spotify 는 400/700 만 씀)
- ❌ 카테고리 듀얼톤(rose/amber/green/blue)의 light/dark 혼용 — 항상 페어로 유지
- ❌ `--color-primary` / `--color-brand` 같은 커스텀 토큰 이름 (실제는 `--encore-*` / `--text-bright-accent` / `--essential-bright-accent`)
- ❌ `outline: none` 처리 — Spotify 의 focus 는 명시적 outline 기반

---

