---
slug: square
service_name: Square
site_url: https://squareup.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#006AFF"
primary_font: Square Sans Text VF
font_weight_normal: 400
token_prefix: --color-*
---

# DESIGN.md — Square (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Square의 디지털 인터페이스는 라이트 테마를 기본으로 한다. 밝은 배경 위에 브랜드 컬러 `#006AFF`가 절제적으로 사용되어 깔끔하고 신뢰감 있는 시각적 인상을 만든다.

색상 전략은 `#006AFF`, `#0055CC` 등을 중심으로 구성된다. 브랜드의 canonical 컬러인 `#006AFF`가 CTA와 주요 인터랙션 요소에 사용되며, 나머지 뉴트럴 팔레트가 배경과 텍스트 계층을 형성한다.

타이포그래피는 `Square Sans Text VF` 폰트를 중심으로 브랜드 고유의 성격을 표현한다. 기본 weight 400으로 본문을 구성하며, heading에서 더 무거운 weight를 사용해 시각적 위계를 만든다.

레이아웃은 풀 너비 히어로 섹션과 콘텐츠 영역의 리듬감 있는 교차로 구성된다. 충분한 여백을 활용하여 콘텐츠에 시각적 호흡 공간을 부여하고, 핵심 메시지와 CTA에 자연스럽게 시선을 유도한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Square처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: 'Square Sans Text VF', 'Square Sans Text',
    Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #1A1A1A; }
body { background: var(--bg); color: var(--fg); }

/* 3. Square 블루 */
:root { --color-theme: #006AFF; }
```

**절대 하지 말아야 할 것 하나**: `Cash Sans`를 Square의 메인 UI 폰트로 사용하는 것. `Cash Sans`는 Square의 Cash App 제품라인 전용 폰트다. Square 웹사이트의 메인 UI 폰트는 `Square Sans Text VF`이며, `Cash Sans` 혼용은 완전히 다른 제품의 아이덴티티가 섞이는 결과를 낳는다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://squareup.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA |
| HTML size | N/A bytes |
| CSS files | Svelte-compiled CSS (`.svelte-*` 해시 클래스) + Square DS 토큰 |
| Token prefix | `--color-*`, `--action-variant-*`, `--text-variant-*`, `--font-family-*` |
| Method | CSS 커스텀 프로퍼티 파싱 + selector_role 확인 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: SvelteKit (`.svelte-*` 해시 클래스 — Svelte 컴파일드 CSS 증거)
- **Design system**: 자체 DS — Square Sans 폰트 패밀리 + `--color-*` / `--action-variant-*` 토큰 체계
- **CSS architecture**: Svelte scoped CSS (`.svelte-kyz8oo`, `.svelte-wxk8im` 등 컴포넌트별 해시), CSS 커스텀 프로퍼티 토큰 병용
- **Default theme**: light (흰 배경 `#FFFFFF`, near-black 텍스트 `#1A1A1A`, 블루 CTA `#006AFF`)
- **Font loading**: 자체 호스트 `Square Sans Text VF`, `Square Sans Display`, `Square Sans Mono` + `Cash Sans` (Cash App)
- **Canonical anchor**: `#006AFF` — `.primary.svelte-wxk8im { background-color: var(--color-theme, #006aff) }`, `--action-variant-button-alt-text-color` 양방향 확인

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Primary/Body font**: `Square Sans Text VF` (64회 + `Square Sans Text` 8회 = 72회 — 압도적 1위)
- **Display font**: `Square Sans Display` (9회), `Square Sans Display VF` (4회) — 히어로 헤드라인
- **Mono**: `Square Sans Mono` (4회), `Square Sans Mono VF` (1회) — 코드, 데이터
- **Cash App 전용**: `Cash Sans` (12회), `Cash Sans Mono` (3회) — Cash App 제품 페이지 전용
- **레거시/특수**: `Exact Block` (2회 — 장식용 디스플레이), `Noto Sans JP` (1회 — 일본어)
- **Weight system**: 300, 400, 500, 600, 700

```css
/* 기본 UI */
body {
  font-family: 'Square Sans Text VF', 'Square Sans Text',
    Helvetica, Arial, 'Hiragino Kaku Gothic Pro',
    'ヒラギノ角ゴ Pro W3', 'メイリオ', meiryo,
    'ＭＳ Ｐゴシック', sans-serif;
  font-weight: 400;
}

/* 히어로 디스플레이 */
h1, h2 {
  font-family: 'Square Sans Display VF', 'Square Sans Display',
    Helvetica, Arial, sans-serif;
  font-weight: 700;
}

/* 코드 / 데이터 */
.mono {
  font-family: 'Square Sans Mono', monospace;
  font-weight: 400;
}
```

> **주의**: `Cash Sans`(12회)는 Square의 메인 폰트가 아니다. Cash App 제품 섹션 전용. 오픈소스 대체재: `Square Sans Text VF` → `Inter` 또는 `DM Sans`, `Square Sans Display` → `Plus Jakarta Sans`.

---

## 05. Typography Scale
<!-- SOURCE: manual -->

| 역할 | 크기 | Weight | 폰트 |
|---|---|---|---|
| Hero Display | clamp(40px, 6vw, 72px) | 700 | Square Sans Display VF |
| Section Heading | 28px–40px | 600–700 | Square Sans Display |
| Card Title | 16px–20px | 600 | Square Sans Text VF |
| Body | 14px–16px | 400 | Square Sans Text VF |
| Price / Data | 18px–24px | 500–600 | Square Sans Text VF |
| Code / Terminal | 13px–14px | 400 | Square Sans Mono |
| Caption | 12px | 400 | Square Sans Text VF |
| Button | 15px–16px | 600 | Square Sans Text VF |

---

## 06. Colors
<!-- SOURCE: auto+manual -->

### Brand

| Token | Hex | 역할 | 출처 |
|---|---|---|---|
| `--color-theme` | `#006AFF` | 브랜드 블루 — primary CTA 배경 | `.primary.svelte-wxk8im` |
| `--action-variant-button-alt-text-color` | `#006AFF` | 버튼 텍스트 (light+dark 동일) | semantic_vars |
| `--action-variant-button-alt-border-color (light)` | `#006AFF` | 버튼 테두리 (라이트 모드) | semantic_vars |

### CTA Details

| Hex | 역할 |
|---|---|
| `#006AFF` | primary 버튼 배경 |
| `#0055CC` | primary 버튼 focus/hover 오버레이 |
| `#FFFFFF` | primary 버튼 텍스트 |

### Neutrals

| Hex | 역할 |
|---|---|
| `#1A1A1A` | 메인 텍스트 (near-black) |
| `#FFFFFF` | 기본 배경 |
| `#D9D9D9` | 보더 컬러 |
| `#F7F6F5` | 라이트 배경 accent (light mode) |
| `#1F1F1F` | 다크 배경 accent (dark mode) |

---

## 07. Spacing
<!-- SOURCE: manual -->

| Step | Value |
|---|---|
| xs | 4px |
| sm | 8px |
| md | 16px |
| lg | 24px |
| xl | 32px |
| 2xl | 48px |
| 3xl | 64px |
| 4xl | 96px |

---

## 08. Radius
<!-- SOURCE: manual -->

| 역할 | Radius |
|---|---|
| Button | 4px–6px |
| Card | 8px–12px |
| Input | 4px |
| Modal | 12px |
| Badge | 999px |
| Jump Link | 5px |

> Square의 버튼 radius는 작다 — `4px–6px`. 결제 처리 회사로서 샤프하고 신뢰감 있는 비즈니스 느낌 유지. Wise의 pill(40px)과 완전히 대조적.

---

## 09. Shadows
<!-- SOURCE: manual -->

| 레이어 | CSS |
|---|---|
| Card | `box-shadow: 0 2px 8px rgba(0,0,0,.08)` |
| Dropdown | `box-shadow: 0 4px 16px rgba(0,0,0,.12)` |
| Modal | `box-shadow: 0 8px 32px rgba(0,0,0,.16)` |

---

## 10. Motion
<!-- SOURCE: manual -->

| 패턴 | Duration | Easing |
|---|---|---|
| Button hover | 150ms | ease |
| Nav toggle | 200ms | ease-out |
| Card hover | 180ms | ease |
| Modal open | 250ms | ease-out |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

- **히어로**: 흰 배경, 큰 Display 헤드라인, 블루 CTA — 비즈니스 솔루션 소개
- **Feature 섹션**: 제품 카드 그리드 + 설명. POS 기기, 결제, 대출 등
- **내비게이션**: DesktopNav 흰 배경, 메뉴 드롭다운 — Svelte 컴포넌트 기반
- **컨테이너**: `max-width: 1200px; margin: 0 auto; padding: 0 24px`
- **Dark mode**: `--color-background-accent-color-mode-dark: #1F1F1F` — 다크 모드 지원 (accent 영역)

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

### Primary CTA Button

```css
.btn-primary {
  background: var(--color-theme, #006AFF);
  color: #FFFFFF;
  border: none;
  border-radius: 4px;
  padding: 14px 24px;
  font-family: 'Square Sans Text VF', Helvetica, sans-serif;
  font-weight: 600;
  font-size: 16px;
  transition: all 150ms ease;
  position: relative;
  overflow: hidden;
}
/* hover/focus overlay */
.btn-primary::before {
  content: "";
  display: block;
  position: absolute;
  inset: 0;
  background: var(--color-theme-focus, #0055CC);
  opacity: 0;
  transition: opacity 150ms ease;
}
.btn-primary:hover::before {
  opacity: 1;
}
```

### Secondary Button (Alt variant)

```css
.btn-alt {
  background: transparent;
  color: #006AFF;
  border: 2px solid #006AFF;
  border-radius: 4px;
  padding: 12px 22px;
  font-family: 'Square Sans Text VF', Helvetica, sans-serif;
  font-weight: 600;
  font-size: 16px;
}
```

### Jump Link (Skip nav — 접근성)

```css
.jump-link {
  background: #FFFFFF;
  color: #1A1A1A;
  border: 2px solid #006AFF;
  border-radius: 5px;
  padding: 10px;
  font-weight: 600;
}
```

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

- **헤드라인**: 비즈니스 성장, 판매 효율. "Grow your business with Square."
- **수치**: 처리 비율, 소요 시간. "2.6% + 10¢ per swipe"
- **CTA**: "Get started", "Talk to sales", "See pricing" — 비즈니스 직접적
- **어조**: 전문적이고 명확. SMB(소상공인) 친화적. 복잡한 금융을 단순하게

---

## 15. Drop-in CSS
<!-- SOURCE: manual -->

```css
/* Square Design System — Drop-in */
:root {
  --color-theme:             #006AFF;   /* primary CTA */
  --color-theme-focus:       #0055CC;   /* hover/focus */
  --color-text:              #1A1A1A;
  --color-background:        #FFFFFF;
  --color-border:            #D9D9D9;
  --color-background-accent: #F7F6F5;

  --font-family-base: 'Square Sans Text VF', 'Square Sans Text',
    Helvetica, Arial, sans-serif;
  --font-family-display: 'Square Sans Display VF', 'Square Sans Display',
    Helvetica, Arial, sans-serif;
  --font-family-mono: 'Square Sans Mono', monospace;
}

body {
  font-family: var(--font-family-base);
  font-weight: 400;
  background: var(--color-background);
  color: var(--color-text);
  -webkit-font-smoothing: antialiased;
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
        square: {
          blue:       '#006AFF',
          'blue-hover': '#0055CC',
          dark:       '#1A1A1A',
          border:     '#D9D9D9',
          accent:     '#F7F6F5',
        },
      },
      fontFamily: {
        sans:    ['"Square Sans Text VF"', '"Square Sans Text"', 'Helvetica', 'Arial', 'sans-serif'],
        display: ['"Square Sans Display VF"', '"Square Sans Display"', 'Helvetica', 'Arial', 'sans-serif'],
        mono:    ['"Square Sans Mono"', 'monospace'],
      },
      borderRadius: {
        btn:  '4px',
        card: '8px',
        lg:   '12px',
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
| Brand primary | brand | `#006AFF` |
| Background | bg-page | `#FFFFFF` |
| Text primary | text | `#1A1A1A` |
| Text muted | text-muted | `#666666` |
| Border | border | `#D9D9D9` |

### Example Component Prompts

#### Hero Section
```
Square 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: Square Sans Text VF, weight 700
- 서브텍스트: #666666
- CTA 버튼: 배경 #006AFF, 텍스트 white
```

#### Card Component
```
Square 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF, border: 1px solid #D9D9D9
- radius: 4px
- 제목: Square Sans Text VF, 16px, weight 700
- 본문: 14px, color #1A1A1A
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

- `#006AFF` Square 블루를 primary CTA 배경에 — `var(--color-theme, #006AFF)` 패턴
- 버튼에 `::before` hover overlay 패턴 (`#0055CC`, opacity 0→1)
- `Square Sans Text VF`로 UI 전체, `Square Sans Display`로 히어로 헤드라인
- 버튼 radius는 작게 — `4px` (비즈니스/결제 신뢰감)
- `Square Sans Mono`로 코드/수치 데이터 표시

### DON'T

- `Cash Sans`를 메인 UI 폰트로 사용 — Cash App 전용 폰트
- pill shape 버튼(`border-radius: 999px`) — Square는 샤프한 비즈니스 느낌
- 다크 배경을 기본으로 — 라이트가 Square의 주 테마
- `--color-theme` 없이 하드코딩만 — CSS 변수 패턴 유지

### 자주 하는 오해 vs 실제

| 오해 | 실제 |
|---|---|
| Cash Sans = Square 메인 폰트 | Cash App 전용. Square 메인은 `Square Sans Text VF` |
| Square = 결제 = 검정/흰 | 라이트 테마 + 블루 CTA — `#006AFF` |
| 버튼이 둥글 것 | `4px` 작은 radius — 비즈니스 샤프함 |
| Svelte 해시 클래스 = 의미 없음 | `.primary.svelte-wxk8im`에서 브랜드 컬러 직접 확인 가능 |
