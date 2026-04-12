---
slug: discord
service_name: Discord
site_url: https://discord.com
fetched_at: 2026-04-11
default_theme: mixed
brand_color: "#5865F2"
primary_font: ABC Ginto
font_weight_normal: 400
token_prefix: size
---

# DESIGN.md — Discord (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Discord처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — ABC Ginto triple (display / nord / app) */
:root {
  --font-display: "ABC Ginto Normal", "Ginto", sans-serif;
  --font-nord:    "ABC Ginto Nord", "Ginto Nord", sans-serif;  /* 800 weight heavy display */
  --font-app:     "gg sans", "Ginto", -apple-system, sans-serif; /* 앱 UI 전용 */
}
body { font-family: var(--font-display); font-weight: 400; }

/* 2. 배경 — 순수 black + Blurple */
:root {
  --bg:        #000000;   /* 1145회 — 실제 dominant */
  --bg-elev:   #23272A;   /* 앱 내부 surface */
  --text:      #FFFFFF;
  --blurple:   #5865F2;   /* 브랜드 앵커 */
}
body { background: var(--bg); color: var(--text); }

/* 3. Aurora gradient 시그니처 */
.hero {
  background: linear-gradient(135deg, #5865F2 0%, #B377F3 50%, #FF6AEF 100%);
}
```

**절대 하지 말아야 할 것 하나**: Discord의 마케팅 사이트 정체성은 **Blurple 단색이 아니라 10+ 테마의 Aurora gradient 시스템**이다. `aurora`, `chroma-glow`, `citrus-sherbert`, `cotton-candy`, `crimson-moon`, `forest`, `hanami`, `lofi-vibes` 등 수십 개 gradient가 각 섹션 배경/카드에 배치된다. Blurple 단색으로만 만들면 "generic 게이머 다크 채팅"이 된다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://discord.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| CSS files | 3개 (메인 + discord-2022.shared + styles) · 3,116,533자 (3.1MB) |
| Custom properties | **4,181개** (color 647 · spacing 90 · shadow 25) |
| Unique hex | 553개 |
| Unique fonts | 59 families |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: discord.com marketing site (Ember? React?)
- **Design system**: 내부 DS — prefix 다중 (`--size-*`, `--space-*`, `--bg-gradient-*`, `--shadow-*`)
- **CSS architecture**: 4,181개 변수, 2-tier spacing + gradient tier
  ```
  raw tier         --size-{0..192}       (px 기반 raw atom)
  semantic tier    --size-{xxs..xxxl}    (semantic alias)
  space tier       --space-{0..128}      (독립 19-step scale)
  gradient tier    --bg-gradient-{theme}-{N}  (10+ 테마)
  shadow tier      --shadow-{low,medium,high,ledge,button-overlay}
  ```
- **Class naming**: BEM + component slot
- **Default theme**: **mixed** — 마케팅 사이트는 light/dark 섹션 혼합, 앱 UI는 dark-first
- **Font loading**: 3-way 분리 — `ABC Ginto` (display), `ABC Ginto Nord` (nord heavy 800), `gg sans` (app UI)
- **Canonical anchor**: `#5865F2` Blurple (229회) — 2020년 리브랜딩 후 브랜드

> **중요**: Discord 앱과 마케팅 사이트는 **다른 디자인 언어**. 앱은 `--interactive-normal`, `#313338` 등 내부 토큰을 쓰지만, 마케팅 사이트는 aurora gradient + ABC Ginto 중심. 본 문서는 **마케팅 사이트** 기준.

---

## 04. Font Stack
<!-- SOURCE: auto -->

- **Display primary**: `ABC Ginto Normal` (Dinamo Typefaces, paid) — 마케팅 히어로 / 제목
- **Display heavy**: `ABC Ginto Nord` (800 weight) — 임팩트 강한 타이틀
- **App UI**: `gg sans` — Discord 앱 전용 (멀티 weight)
- **Hybrid**: `Abcgintodiscord` — 커스텀 브랜드 빌드 (306회 최다)
- **Fallback**: `-apple-system`, `BlinkMacSystemFont`, sans-serif

```css
:root {
  --font-display: "Abcgintodiscord", "ABC Ginto Normal", "Ginto", -apple-system, BlinkMacSystemFont, sans-serif;
  --font-nord:    "Abcgintonord 800", "ABC Ginto Nord", "Ginto Nord", sans-serif;
  --font-app:     "gg sans", "Ginto", -apple-system, BlinkMacSystemFont, sans-serif;
}
body { font-family: var(--font-display); font-weight: 400; }
h1, .display-xl { font-family: var(--font-nord); font-weight: 800; }
.app-ui { font-family: var(--font-app); }
```

> Weight distribution: `700` (336) > `500` (287) > `400` (241) > `600` (118) > `800` (39) > `900` (36) > `300` (24) > `100` (6) > `200` (3). ABC Ginto는 variable font라 full axis 사용 가능.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Size | Count | Usage |
|---|---|---|
| 16px | 374 | body 기본 (최다) |
| 20px | 356 | lead text |
| 24px | 265 | h4 / card title |
| 32px | 243 | h3 |
| 14px | 186 | small body |
| 1.25rem (20px) | 173 | rem-based lead |
| 1rem (16px) | 165 | rem body |
| 48px | 157 | h2 |
| 18px | 145 | body large |
| 40px | 140 | display sm |
| 56px | 134 | display md |
| 1.5rem (24px) | 133 | rem h4 |
| 64px | 100+ | display lg |
| 88px | ~ | display xl |
| 112px | ~ | hero mega |

> ⚠️ `16px` (374회)와 `20px` (356회)가 body의 양대 산맥. rem/px 혼용 — `1rem`(165)과 `16px`(374)가 별개 카운트. 총 **127 unique sizes** — 마케팅 페이지별 다른 hero 스케일 사용.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Blurple
| Token | Hex | Count | Role |
|---|---|---|---|
| Blurple 2020+ | `#5865F2` | 229 | ⭐ **current brand** (primary CTA, logo) |
| Legacy Blurple | `#7289DA` | 21 | 2020년 리브랜딩 전 색 (일부 페이지 잔존) |
| Blurple deep | `#4752C4` (추정) | - | hover/pressed |
| Blurple tint | `#8A9BFF` | - | disabled/subtle |

### 06-3. Neutral Ramp (실제 빈도)
| Hex | Count | Role |
|---|---|---|
| `#000000` | 1145 | **true black** — 실제 마케팅 dominant |
| `#FFFFFF` | 570 | primary text |
| `#23272A` | 128 | app internal dark surface |
| `#F6F6F6` | 92 | light mode bg |

> **놀라운 사실**: Discord 마케팅 CSS에서 `#000000`이 1145회로 절대 다수. "순수 black을 쓰지 말라"는 일반적 advice는 Discord엔 적용 안 됨 — aurora gradient가 순수 black 위에서 가장 비비드하게 빛나기 때문.

### 06-4. Neon Aurora Accent Palette
<!-- SOURCE: auto — 마케팅 페이지 실제 빈도 -->

| Token | Hex | Count | Role |
|---|---|---|---|
| mint neon | `#15F5BA` | 25 | fresh accent · aurora hue |
| lavender | `#B377F3` | 23 | purple accent |
| pink neon | `#FF6AEF` | 23 | hot accent |
| baby blue | `#8CD9FF` | 19 | cool accent |
| legacy blurple | `#7289DA` | 21 | nostalgia accent |

### 06-5. Aurora Gradient Tier (signature)
<!-- SOURCE: auto - --bg-gradient-* 토큰 그룹 -->

실제 CSS에 등재된 gradient 테마 (10+):

| Theme | Token family | Vibes |
|---|---|---|
| **aurora** | `--bg-gradient-aurora-{1..5}` | Discord의 sig — purple → pink → blue |
| **blurple-twilight** | `-blurple-twilight-{1,2}` | blurple deep night |
| **chroma-glow** | `-chroma-glow-{1..5}` | rainbow iridescent |
| **citrus-sherbert** | `-citrus-sherbert-{1,2}` | orange/yellow/pink |
| **cotton-candy** | `-cotton-candy-{1,2}` | pink/baby-blue pastel |
| **crimson-moon** | `-crimson-moon-{1,2}` | red/dark moody |
| **desert-khaki** | `-desert-khaki-{1..3}` | warm earth tones |
| **dusk** | `-dusk-{1,2}` | twilight blues |
| **easter-egg** | `-easter-egg-{1,2}` | pastel mix |
| **forest** | `-forest-{1..5}` | greens |
| **hanami** | `-hanami-{1..3}` | pink cherry blossom |
| **lofi-vibes** | `-lofi-vibes-{1..3}` | retro purple/orange |

> 각 테마는 1~5개 variant를 가지며, 섹션 배경, 카드 bg, 일러스트 wash에 사용. Discord 마케팅 사이트는 이 gradient 시스템이 **전체의 정체성**.

### 06-6. Semantic Alias Layer

| Alias | Resolves to | Usage |
|---|---|---|
| `--size-xxs` | `var(--size-4)` | 4px tightest gap |
| `--size-xs` | `var(--size-8)` | 8px |
| `--size-sm` | `var(--size-12)` | 12px |
| `--size-md` | `var(--size-16)` | 16px |
| `--size-lg` | `var(--size-20)` | 20px |
| `--size-xl` | `var(--size-24)` | 24px |
| `--size-xxl` | `var(--size-32)` | 32px |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#000000` | 1145 | page bg (마케팅) |
| 2 | `#FFFFFF` | 570 | text primary |
| 3 | `#5865F2` | 229 | Blurple |
| 4 | `#23272A` | 128 | app dark surface |
| 5 | `#F6F6F6` | 92 | light bg |
| 6 | `#15F5BA` | 25 | mint neon |
| 7 | `#B377F3` | 23 | lavender |
| 8 | `#FF6AEF` | 23 | pink neon |
| 9 | `#7289DA` | 21 | legacy blurple |
| 10 | `#8CD9FF` | 19 | baby blue |

---

## 07. Spacing
<!-- SOURCE: auto -->

Discord는 **2-tier spacing 시스템**:

### Raw tier — `--size-{N}` (px 기반)
| Token | px |
|---|---|
| `--size-0` | 0 |
| `--size-4` | 4 |
| `--size-8` | 8 |
| `--size-12` | 12 |
| `--size-16` | 16 |
| `--size-20` | 20 |
| `--size-24` | 24 |
| `--size-32` | 32 |
| `--size-48` | 48 |
| `--size-64` | 64 |
| `--size-80` | 80 |
| `--size-96` | 96 |
| `--size-128` | 128 |
| `--size-160` | 160 |
| `--size-192` | 192 |

### Semantic tier — `--size-{xxs..xxl}` alias

| Alias | → | Value |
|---|---|---|
| `--size-xxs` | → | `--size-4` (4px) |
| `--size-xs` | → | `--size-8` (8px) |
| `--size-sm` | → | `--size-12` (12px) |
| `--size-md` | → | `--size-16` (16px) |
| `--size-lg` | → | `--size-20` (20px) |
| `--size-xl` | → | `--size-24` (24px) |
| `--size-xxl` | → | `--size-32` (32px) |

추가로 독립 `--space-{0..128}` 19-step scale도 존재. 총 **90개** spacing 변수.

---

## 08. Radius
<!-- SOURCE: auto -->

Discord는 **77개** unique radius 값 사용. 상위 10:

| Value | Count | Context |
|---|---|---|
| `8px` | 139 | 기본 button / chip (최다) |
| `16px` | 114 | card corner |
| `40px` | 105 | large card / modal |
| `12px` | 82 | input |
| `56px` | 79 | hero card |
| `64px` | 74 | xl card |
| `48px` | 70 | medium card |
| `32px` | 64 | button pill |
| `88px` | 49 | mega card |
| `20px` | 47 | small card |

> Discord는 각 섹션/컴포넌트마다 다른 radius를 사용. `8px`는 UI 기본, `16px~88px`는 aurora gradient 카드별 optical balance.

---

## 09. Shadows
<!-- SOURCE: auto -->

25개 shadow 변수. 주요 slot 네이밍:

| Token | Usage |
|---|---|
| `--shadow-low` | subtle resting elevation |
| `--shadow-low-hover` | hover 리프트 |
| `--shadow-medium` | dropdown, menu |
| `--shadow-high` | modal, overlay |
| `--shadow-button-overlay` | button press inner |
| `--shadow-ledge` | sticky header |
| `--shadow-mobile-navigator-x` | 모바일 네비 전용 |
| `--shadow-top-high` | top sheet |

> 모든 shadow가 **component-slot 네이밍** — 값보다 "어디에 쓰는지"가 토큰명에 명시.

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Blurple CTA (primary)
- **Background**: `#5865F2` (Blurple)
- **Hover**: `#4752C4`
- **Text**: `#FFFFFF`
- **Radius**: `8px` 또는 `32px` (pill)
- **Font**: ABC Ginto Normal 16px / 500
- **Padding**: `12px 24px`

```html
<button class="btn btn--blurple">Open Discord in your browser</button>
```

### Aurora Hero Card
- **Background**: `linear-gradient(135deg, #5865F2, #B377F3, #FF6AEF)` (aurora-1)
- **Border**: none
- **Radius**: `40px` ~ `88px`
- **Padding**: `48px 64px`
- **Text**: white / ABC Ginto Nord 800 for heading

### Download CTA (2-CTA block)
- Primary: `#5865F2` Blurple + `#FFFFFF` text
- Secondary: `#FFFFFF` + `#23272A` text
- Radius: `32px` (pill)
- Icon inset: `--size-8`

### Feature card
- Background: aurora gradient 1종 (per-section 테마)
- Heading: ABC Ginto Nord 48px / 800
- Body: ABC Ginto Normal 16px / 400
- Padding: `var(--size-xxl)` (32px)
- Radius: `32px`

### Download button group
- Platform icons (Windows, Mac, Linux, iOS, Android)
- Icons 24×24 + label
- Stacked with `var(--size-md)` gap

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Discord — copy into your root stylesheet */
:root {
  /* Fonts (3-way) */
  --font-display: "Abcgintodiscord", "ABC Ginto Normal", "Ginto", -apple-system, BlinkMacSystemFont, sans-serif;
  --font-nord:    "Abcgintonord 800", "ABC Ginto Nord", "Ginto Nord", sans-serif;
  --font-app:     "gg sans", "Ginto", -apple-system, BlinkMacSystemFont, sans-serif;

  /* Brand Blurple */
  --blurple:        #5865F2;
  --blurple-hover:  #4752C4;
  --blurple-legacy: #7289DA; /* pre-2020 */

  /* Neutral */
  --bg:             #000000; /* 마케팅 bg */
  --bg-app:         #23272A; /* 앱 surface */
  --bg-light:       #F6F6F6;
  --text:           #FFFFFF;

  /* Aurora neon accents */
  --mint:           #15F5BA;
  --lavender:       #B377F3;
  --pink:           #FF6AEF;
  --baby-blue:      #8CD9FF;

  /* Size raw tier */
  --size-0:   0;
  --size-4:   4px;
  --size-8:   8px;
  --size-12:  12px;
  --size-16:  16px;
  --size-20:  20px;
  --size-24:  24px;
  --size-32:  32px;
  --size-48:  48px;
  --size-64:  64px;
  --size-80:  80px;
  --size-96:  96px;
  --size-128: 128px;

  /* Size semantic alias */
  --size-xxs: var(--size-4);
  --size-xs:  var(--size-8);
  --size-sm:  var(--size-12);
  --size-md:  var(--size-16);
  --size-lg:  var(--size-20);
  --size-xl:  var(--size-24);
  --size-xxl: var(--size-32);

  /* Aurora gradients */
  --bg-gradient-aurora-1: linear-gradient(135deg, #5865F2 0%, #B377F3 50%, #FF6AEF 100%);
  --bg-gradient-cotton-candy-1: linear-gradient(135deg, #FF6AEF 0%, #8CD9FF 100%);
  --bg-gradient-forest-1: linear-gradient(135deg, #15F5BA 0%, #5865F2 100%);
  --bg-gradient-crimson-moon-1: linear-gradient(135deg, #FF6AEF 0%, #000000 100%);
}

body {
  font-family: var(--font-display);
  font-weight: 400;
  background: var(--bg);
  color: var(--text);
}

.display-heavy { font-family: var(--font-nord); font-weight: 800; }
```

---

## 15. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Discord
module.exports = {
  theme: {
    extend: {
      colors: {
        blurple: {
          DEFAULT: '#5865F2',
          hover:   '#4752C4',
          legacy:  '#7289DA',
        },
        neon: {
          mint:    '#15F5BA',
          lavender:'#B377F3',
          pink:    '#FF6AEF',
          blue:    '#8CD9FF',
        },
        surface: {
          marketing: '#000000',
          app:       '#23272A',
          light:     '#F6F6F6',
        },
      },
      fontFamily: {
        display: ['"Abcgintodiscord"', '"ABC Ginto Normal"', '"Ginto"', '-apple-system', 'sans-serif'],
        nord:    ['"Abcgintonord 800"', '"ABC Ginto Nord"', '"Ginto Nord"', 'sans-serif'],
        app:     ['"gg sans"', '"Ginto"', '-apple-system', 'sans-serif'],
      },
      fontWeight: {
        thin:    '100',
        light:   '300',
        normal:  '400',
        medium:  '500',
        semibold:'600',
        bold:    '700',
        heavy:   '800',
        black:   '900',
      },
      spacing: {
        'xxs': '4px',
        'xs':  '8px',
        'sm':  '12px',
        'md':  '16px',
        'lg':  '20px',
        'xl':  '24px',
        'xxl': '32px',
      },
      borderRadius: {
        sm:  '8px',
        md:  '12px',
        lg:  '16px',
        xl:  '32px',
        '2xl':'40px',
        '3xl':'56px',
        '4xl':'64px',
        '5xl':'88px',
      },
      backgroundImage: {
        'aurora':     'linear-gradient(135deg, #5865F2 0%, #B377F3 50%, #FF6AEF 100%)',
        'cotton':     'linear-gradient(135deg, #FF6AEF, #8CD9FF)',
        'forest':     'linear-gradient(135deg, #15F5BA, #5865F2)',
        'crimson':    'linear-gradient(135deg, #FF6AEF, #000000)',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- **Blurple `#5865F2`**를 primary CTA로 (2020년 리브랜딩 후 current brand).
- **순수 black `#000000`** 페이지 bg 사용 — 실제 1145회 dominant. aurora gradient가 black 위에서 가장 비비드하게 빛남.
- **Aurora gradient 시스템** 활용: `aurora`, `cotton-candy`, `forest`, `crimson-moon`, `hanami`, `lofi-vibes` 등 10+ 테마. 섹션마다 다른 gradient.
- **3-폰트 분리**: `ABC Ginto Normal` (display), `ABC Ginto Nord 800` (heavy impact), `gg sans` (app UI).
- **2-tier spacing**: raw `--size-{N}` + semantic `--size-{xxs..xxl}` alias.
- **Neon accent palette**: `#15F5BA` (mint), `#B377F3` (lavender), `#FF6AEF` (pink), `#8CD9FF` (baby blue).
- **Component-slot shadow 네이밍**: `--shadow-low`, `--shadow-ledge`, `--shadow-button-overlay`.
- Radius는 컴포넌트별 다름 — `8px` (button), `16px`/`40px`/`88px` (card variants).

### ❌ DON'T
- ❌ Blurple 단색만 사용 — Discord 마케팅의 정체성은 **multi-accent + gradient**.
- ❌ **Legacy Blurple** `#7289DA` (2020년 전 색) — 일부 페이지 잔존하지만 current 브랜드 아님.
- ❌ `gg sans`를 마케팅 헤딩에 — 앱 UI 전용. 마케팅은 ABC Ginto Nord.
- ❌ `#313338` / `#2B2D31` (app 내부 surface) — 마케팅 페이지에는 0회. 앱 컨텍스트 전용.
- ❌ `color-brand` / `color-gray-*` flat 네이밍 — Discord는 `--size-*`, `--space-*`, `--bg-gradient-*` semantic tier.
- ❌ Aurora gradient 없이 flat 카드 — marketing 감성 소실.
- ❌ 단일 radius 값 사용 — Discord는 컴포넌트별 8px ~ 88px 다양하게 사용.
- ❌ "Don't use pure black" 룰 — 실제로는 반대, `#000000`이 1145회 dominant.
