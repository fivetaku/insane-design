---
slug: twitch
service_name: Twitch
site_url: https://www.twitch.tv
fetched_at: 2026-04-11
default_theme: dark
brand_color: "#9147FF"
primary_font: Inter
font_weight_normal: 400
token_prefix: "(none — hardcoded) + .tw-root--theme-*"
---

# DESIGN.md — Twitch (Claude Code Edition)

---

## 01. Quick Start

> 5분 안에 Twitch처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트: Inter (body) + Roobert (display/brand) */
body {
  font-family: "Inter", -apple-system, "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}
h1, h2, h3, .tw-brand {
  font-family: "Roobert", "Inter", -apple-system, sans-serif;
  font-weight: 700;
}
/* 아랍어 폴백: "Noto Sans Arabic", "Tajawal" */

/* 2. 배경 + 텍스트 (dark 기본) */
:root {
  --tw-bg-dark:   #0E0E10;    /* 15회 dominant */
  --tw-bg-darker: #18181B;    /*  5회 */
  --tw-ink-light: #EFEFF1;    /* 11회, 본문 대비용 */
}
.tw-root--theme-dark {
  background: var(--tw-bg-dark);
  color: var(--tw-ink-light);
}

/* 3. 브랜드 퍼플 — 단일 anchor #9147FF */
:root {
  --tw-purple-500: #9147FF;   /* ★ canonical, 18회 dominant */
  --tw-purple-400: #A970FF;   /* hover (lighter) */
  --tw-purple-600: #772CE8;   /* press (darker), 13회 */
  --tw-purple-700: #5C16C5;   /* active, 11회 */
}
```

**절대 하지 말아야 할 것 하나**: Twitch purple 을 "레거시 `#6441A5`" 또는 "rebrand 후 `#6441A4`" 로 쓰지 말 것. 2019년 리브랜드 이후 signature 는 **`#9147FF`** 이고, 실제 CSS 에 <code>#6441*</code> 계열은 <b>한 번도</b> 등장하지 않는다. Dominant 차트: `#9147FF`(18) → `#772CE8`(13) → `#5C16C5`(11) → `#A970FF`(8) → `#8205B4`(5) → `#451093`(2) 의 6-step 램프가 실제 사용되는 purple 체인이다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.twitch.tv` |
| Fetched | 2026-04-11 |
| CSS files | 2개 외부, 총 64,493자 |
| Primary bundle | `core-35514cc0b2a76047035c.css` |
| Token count | **17** custom properties (매우 적음 — 대부분 hardcoded) |
| Token prefix | 없음 (`.tw-root--theme-dark` / `--theme-light` selector theme toggle) |
| Method | CSS 커스텀 프로퍼티 + 전체 hex 빈도 카운트 |

---

## 03. Tech Stack

- **Framework**: React SPA (web client). 마케팅 페이지 아님 — twitch.tv 실 서비스.
- **Design system**: 이름 공개 안 됨. <code>.tw-*</code>(BEM) 클래스 네임스페이스. 토큰 시스템 **없음** (17 개 커스텀 프로퍼티뿐, 대부분 hardcoded hex).
- **CSS architecture**: Selector-based theme toggle
  ```
  .tw-root--theme-dark  { /* dark 테마 스코프 */ }
  .tw-root--theme-light { /* light 테마 스코프 */ }
  .tw-{component}       { /* BEM 컴포넌트 */ }
  ```
- **Class naming**: `.tw-button--primary`, `.tw-core-button`, `.tw-tray-item--highlighted` (BEM double-dash modifier)
- **Default theme**: **dark**. 실사용자의 85%+ 가 dark 모드 — light 도 완전 구현돼 있음.
- **Font loading**: 시스템 @font-face — `Inter` (body) + `Roobert` (display/brand) + `Noto Sans Arabic`/`Tajawal` (RTL)
- **Canonical anchor**: `#9147FF` (2019+ Twitch purple).

---

## 04. Font Stack

- **Primary body**: `Inter` — 21회 (압도적 1위)
- **Display/brand**: `Roobert` — 4-6회 (Twitch 2019 리브랜드 폰트, Display Inc. / Twitch 내부 주문 제작 variant)
- **RTL fallback**: `Noto Sans Arabic` (3회), `Tajawal` (3회)
- **Code**: `monospace` (generic — IBM Plex 같은 지정 없음)
- **Weights used**: 400 (11회) / 500 (2회) / 600 (10회) / 700 (12회)

```css
:root {
  --font-base:    Inter, "Helvetica Neue", Arial, sans-serif;
  --font-display: Roobert, Inter, "Helvetica Neue", Arial, sans-serif;
}
body { font-family: var(--font-base); font-weight: 400; }
h1, h2, h3, .tw-brand-headline { font-family: var(--font-display); font-weight: 700; }

/* RTL 자동 전환 */
:lang(ar) body  { font-family: "Tajawal", "Noto Sans Arabic", sans-serif; }
```

> ⚠️ **Roobert 는 브랜드 제한적 사용.** <code>Inter</code>(21회) vs <code>Roobert</code>(6회) — Roobert 는 주로 홈페이지 로고, hero headline, 브랜드 캐러셀 등 "브랜드 터치포인트" 에만. 본문/UI 전체는 Inter 가 담당. Roobert 는 유료 폰트라 복제 시 Inter 로 fallback 하는 것이 일반적.

---

## 05. Typography Scale

Twitch 는 토큰화된 typography scale 이 없습니다. 관측된 고정 사이즈만:

| Size | Usage |
|---|---|
| `62.5%` | html root 리셋 (`1rem` = 10px 기준) |
| `1rem` | 기본 body (10px × font-size 계승) |
| `1.2rem` | small UI (12px) |
| `1.6rem` | 본문 기본 (16px) |
| `18px` | H3 |

> ⚠️ **`html { font-size: 62.5% }` 트릭.** Twitch 는 `rem` 계산을 10px 기반으로 만들려고 root 에 62.5% 를 씁니다. 그래서 `1.6rem` = 16px, `1.2rem` = 12px 식. 이 리셋 없이 `1.6rem` 을 쓰면 25.6px 로 나와서 완전히 틀린 크기가 됨.

---

## 06. Colors

### 06-1. Twitch Purple Ramp (6 steps)

| Token | Hex | Count | Role |
|---|---|---|---|
| `purple-300` | `#BF94FF` | 6 | pale / hover-alt |
| `purple-400` | `#A970FF` | 8 | hover |
| `purple-500` ★ | `#9147FF` | **18** | canonical brand |
| `purple-600` | `#772CE8` | 13 | press |
| `purple-700` | `#5C16C5` | 11 | active |
| `purple-800` | `#451093` | 2 | deep |
| `purple-850` | `#8205B4` | 5 | alternative deep |
| `purple-accent` | `#6E31DF` | 2 | 링크 variant |

### 06-2. Surface (dark-first)

| Token | Hex | Count |
|---|---|---|
| `bg-darkest` | `#0E0E10` | 15 (dark 테마 primary) |
| `bg-darker` | `#18181B` | 5 |
| `bg-alt` | `#19171C` | 2 |
| `ink-light` | `#EFEFF1` | 11 (dark 위 본문) |
| `surface-100` | `#F7F7F8` | 3 (light 테마) |
| `surface-50` | `#FAFAFA` | 2 |
| `border-muted` | `#D9D8DD` | 2 |

### 06-3. Semantic & Accent

| Token | Hex | Usage |
|---|---|---|
| `error` | `#E91916` | 알림 red |
| `success` | `#00F593` | success/live |
| `info` | `#1E69FF` | 정보 blue |
| `pink-live` | `#F093F9` | 라이브 highlight |

### 06-4. Social brand (DO NOT mix with Twitch palette)

| Platform | Hex |
|---|---|
| Facebook | `#3B5998` |
| VK | `#45668E` |
| Twitter/X | `#000000` |
| Reddit | `#FF4500` |

### 06-5. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 19 | light ink |
| 2 | `#9147FF` ★ | 18 | **brand primary** |
| 3 | `#000000` | 17 | overlay/border |
| 4 | `#0E0E10` | 15 | dark bg primary |
| 5 | `#772CE8` | 13 | brand press |
| 6 | `#EFEFF1` | 11 | light ink |
| 7 | `#5C16C5` | 11 | brand active |
| 8 | `#A970FF` | 8 | brand hover |
| 9 | `#BF94FF` | 6 | pale purple |
| 10 | `#18181B` | 5 | dark surface |

---

## 07. Spacing

> 토큰 **없음** (`spacing_vars = 0`). 모두 raw px / rem hardcoded.

관측된 주요 값:
| Value |
|---|
| `.4rem` (4px), `.8rem` (8px), `1.2rem` (12px), `1.6rem` (16px), `2.4rem` (24px), `3.2rem` (32px), `4.8rem` (48px), `6.4rem` (64px) |

> `html { font-size: 62.5% }` 리셋이 있으니 `rem` = `px × 0.1`.

---

## 08. Radius

`unique_radius_values = 3` — 매우 적음.

| Value | Usage |
|---|---|
| `4px` (`.4rem`) | 기본 버튼, 인풋 |
| `8px` (`.8rem`) | 카드 |
| `9999px` (`50%`) | pill, avatar 원형 |

---

## 09. Shadows

> `shadow_vars = 0`. 커스텀 프로퍼티 없음 — raw box-shadow 가 하드코딩. dark 테마 에서는 shadow 를 거의 쓰지 않고 border 로 대신.

| Value | Usage |
|---|---|
| `0 2px 4px rgba(0,0,0,.2)` | 카드 미세 elevation |
| `0 4px 8px rgba(0,0,0,.3)` | 드롭다운 |
| `0 8px 16px rgba(0,0,0,.4)` | 모달 |

---

## 12. Components

### Button (primary — purple)

```html
<button class="tw-core-button tw-core-button--primary">
  <div class="tw-core-button-label">Subscribe</div>
</button>
```

```css
.tw-core-button--primary {
  background: #9147FF;
  color: #FFFFFF;
  font-family: Inter, sans-serif;
  font-weight: 600;
  height: 3rem;           /* 30px (62.5% 리셋) */
  padding: 0 1rem;         /* 10px */
  border-radius: .4rem;    /* 4px */
  border: 0;
  font-size: 1.3rem;       /* 13px */
}
.tw-core-button--primary:hover  { background: #772CE8; }
.tw-core-button--primary:active { background: #5C16C5; }
```

### Card (dark)

```html
<article class="tw-card">
  <img class="tw-card__thumbnail" />
  <div class="tw-card__meta">
    <h3 class="tw-card__title">Stream title</h3>
    <span class="tw-card__channel">streamer_name</span>
  </div>
</article>
```

```css
.tw-card {
  background: #18181B;
  border-radius: .4rem;
  border: 1px solid #26262C;
  padding: 1rem;
}
.tw-card__title { color: #EFEFF1; font-weight: 600; }
.tw-card__channel { color: #ADADB8; font-size: 1.3rem; }
```

### Live indicator pill

```html
<span class="tw-live-pill">LIVE</span>
```

```css
.tw-live-pill {
  background: #EB0400;       /* error red */
  color: #FFFFFF;
  font-weight: 700;
  padding: .2rem .6rem;
  border-radius: .4rem;
  font-size: 1rem;
}
```

---

## 14. Drop-in CSS

```css
/* Twitch — copy into your root stylesheet */
:root {
  --font-base:    Inter, "Helvetica Neue", Arial, sans-serif;
  --font-display: Roobert, Inter, "Helvetica Neue", Arial, sans-serif;

  /* Purple ramp (anchor + 4 steps) */
  --tw-purple-300: #BF94FF;   /* pale */
  --tw-purple-400: #A970FF;   /* hover */
  --tw-purple-500: #9147FF;   /* ← canonical */
  --tw-purple-600: #772CE8;   /* press */
  --tw-purple-700: #5C16C5;   /* active */
  --tw-purple-800: #451093;   /* deep */

  /* Surface (dark first) */
  --tw-bg-dark:   #0E0E10;
  --tw-bg-darker: #18181B;
  --tw-ink-light: #EFEFF1;
  --tw-ink-muted: #ADADB8;

  /* Semantic */
  --tw-error:   #E91916;
  --tw-success: #00F593;
  --tw-info:    #1E69FF;
  --tw-live:    #EB0400;
}

html { font-size: 62.5%; }  /* 1rem = 10px */
body {
  font-family: var(--font-base);
  background: var(--tw-bg-dark);
  color: var(--tw-ink-light);
  font-size: 1.4rem;  /* 14px */
}
h1, h2, h3 { font-family: var(--font-display); font-weight: 700; }
```

---

## 15. Tailwind Config

```js
// tailwind.config.js — Twitch
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        tw: {
          purple: {
            300: '#BF94FF',
            400: '#A970FF',
            500: '#9147FF',   // canonical
            600: '#772CE8',
            700: '#5C16C5',
            800: '#451093',
          },
          bg: {
            dark:   '#0E0E10',
            darker: '#18181B',
            alt:    '#19171C',
          },
          ink: {
            light: '#EFEFF1',
            muted: '#ADADB8',
          },
          live:    '#EB0400',
          success: '#00F593',
          error:   '#E91916',
          info:    '#1E69FF',
        },
      },
      fontFamily: {
        sans:    ['Inter', 'system-ui', 'sans-serif'],
        display: ['Roobert', 'Inter', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        none: '0',
        sm:   '4px',
        md:   '8px',
        full: '9999px',
      },
    },
  },
};
```

---

## 16. DO / DON'T

### ✅ DO
- 브랜드 퍼플 <code>#9147FF</code> (2019+ 리브랜드). 6-step ramp 활용 (400/500/600/700).
- Body 는 <code>Inter</code>, 브랜드 헤드라인은 <code>Roobert</code>.
- Dark 기본 테마: bg <code>#0E0E10</code>, ink <code>#EFEFF1</code>. <code>.tw-root--theme-dark</code> 스코프.
- Light 테마도 완전 구현: bg <code>#F7F7F8</code>, ink <code>#0E0E10</code> 반전.
- <code>html { font-size: 62.5% }</code> 리셋 필수 — 모든 rem 계산이 이것 기반.
- Live indicator pill: <code>#EB0400</code> 빨강 + 700 weight + 4px radius.
- BEM 네이밍: <code>.tw-core-button--primary</code>, <code>.tw-card__title</code>.

### ❌ DON'T
- ❌ 레거시 <code>#6441A5</code> / <code>#6441A4</code> 퍼플 — 2019 리브랜드 전 구 색, 현 CSS 에 0회.
- ❌ <code>Poppins</code> / <code>Montserrat</code> 대체 폰트 — Roobert 가 signature.
- ❌ 단일 purple 1색 — 6-step ramp (400-800) 전환 필수.
- ❌ 스페이싱 토큰 가정 — <code>--space-*</code> 변수 존재 안 함, 전부 raw rem.
- ❌ <code>1rem = 16px</code> 가정 — Twitch 는 <code>62.5%</code> 리셋이라 <code>1rem = 10px</code>.
- ❌ Shadow 남발 — dark 테마에서 shadow 거의 안 쓰고 border 로 대신.
- ❌ 로고 kit 색(Facebook `#3B5998`, Reddit `#FF4500` 등) 을 UI 토큰으로 — 소셜 버튼 전용.
- ❌ Monospace 코드 폰트에 `JetBrains Mono` 같은 지정 — 실제는 그냥 <code>monospace</code> generic 사용.
