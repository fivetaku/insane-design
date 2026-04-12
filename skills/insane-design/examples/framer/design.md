---
slug: framer
service_name: Framer
site_url: https://www.framer.com
fetched_at: 2026-04-11
default_theme: dark
brand_color: "#0099FF"
primary_font: Inter
font_weight_normal: 400
token_prefix: framer
---

# DESIGN.md — Framer (Claude Code Edition)

---

## 01. Quick Start

> 5분 안에 Framer처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight — Inter Variable 3종 스택 */
body {
  font-family: "Inter Variable", "Inter Display", "Inter", -apple-system, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 — 완전 블랙 캔버스 + 순백 */
:root { --bg: #000000; --fg: #ffffff; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 — 전자 파랑 단일 */
:root { --brand: #0099FF; }
a { color: var(--brand); }
::selection { background: #0099ff4d; color: #fff; }
```

**절대 하지 말아야 할 것 하나**: dark surface를 `#1A1A1A` 같은 불투명 회색으로 채우지 말 것. Framer의 "유리 같은" 느낌은 전적으로 `#FFFFFF1A` (white 10%) 같은 알파 흰색 레이어를 검은 캔버스 위에 쌓아서 나온다. 불투명 surface는 싸구려처럼 보인다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://www.framer.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 2,918,851 bytes (Framer 자체 빌더 SSR) |
| CSS files | 0 외부 + 1 인라인, 총 476,587자 |
| Token prefix | `--framer-*` (런타임) / `--token-{UUID}` (디자이너 토큰) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Framer 자체 빌더 (No-code, SSR로 정적 HTML 출력)
- **Design system**: 디자이너가 Framer Studio에서 만든 Color Styles — UUID 기반 CSS 변수로 직렬화
- **CSS architecture**: 이중 네임스페이스 CSS-in-JS
  ```
  --token-{UUID}        디자이너 생성 "Color Style" (body 레벨 정의)
  --framer-*            런타임 프레임워크 변수 (text/font/spacing)
  framer-{HASH}         페이지별 자동 해시 클래스 (재사용 불가)
  ```
- **Class naming**: `class="framer-0dh8F framer-14xxkp7"` — 2개 해시가 기본, 런타임 생성이라 **클래스명 그대로 복제하지 말 것**
- **Default theme**: Dark (bg = `#000000`, Framer 2025 리브랜드 이후 단일 다크)
- **Font loading**: Google Fonts 호스팅 + Framer 런타임 Placeholder 폴백 메커니즘 (layout shift 방지용 `"Inter Variable Placeholder"`)
- **Canonical anchor**: `--token-958e2cd1-...` = `#000000` (page bg), `--token-26e3cb56-...` = `#ffffff` (primary text), `--token-7caf96a9-...` = `#09f` (brand blue)

---

## 04. Font Stack

- **Display font**: `Inter Display` (Inter Variable용 display optical size)
- **Body font**: `Inter Variable` + `"Inter Variable Placeholder"` fallback chain
- **Code font**: `Geist Mono`, `JetBrains Mono`, `Azeret Mono` — 컨텍스트별 혼재
- **Special display**: `GT Walsheim Medium`, `Satoshi`, `Space Grotesk`, `Mona Sans` — CMS 블로그/페이지별 커스텀 폰트

```css
:root {
  --framer-font-family:      "Inter Variable", "Inter Variable Placeholder", "Inter Display", "Inter", -apple-system, sans-serif;
  --framer-font-family-code: "Geist Mono", "JetBrains Mono", ui-monospace, monospace;
}
body {
  font-family: var(--framer-font-family);
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
}
```

> ⚠️ Framer 런타임은 `"{FontName} Placeholder"` 가상 폰트를 삽입해 웹폰트 로딩 중 레이아웃 시프트를 방지한다. `Inter Variable` 만 쓰면 Framer 소스와 다르게 보이므로 Placeholder 레이어까지 포함한 3단 스택을 유지할 것.

---

## 05. Typography Scale

Framer는 디자인 시스템 기반 스케일 대신 페이지별 인라인 폰트 사이즈를 사용한다 (`--framer-font-size: 85px` 형태). 실제 홈페이지에서 관찰된 사이즈 빈도 기반 추론 스케일:

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Hero display XL  | 110px  | 500–700 | 1.0  | -0.05em |
| Hero display L   | 85px   | 500–700 | 1.05 | -0.05em |
| Hero display M   | 62px   | 500–700 | 1.05 | -0.04em |
| Heading XL       | 54px   | 500     | 1.1  | -0.03em |
| Heading L        | 48px   | 500     | 1.15 | -0.02em |
| Heading M        | 42px   | 500     | 1.2  | -0.02em |
| Heading S        | 36px   | 500     | 1.25 | -0.02em |
| Heading XS       | 34px   | 500     | 1.3  | -0.01em |
| Subheading       | 26px   | 500     | 1.35 | -0.01em |
| Body XL          | 24px   | 400     | 1.4  | -0.005em |
| Body L           | 20px   | 400     | 1.5  | 0em |
| Body M           | 18px   | 400     | 1.55 | 0em |
| Body base        | 16px   | 400     | 1.55 | 0em |
| Body S           | 15px   | 400     | 1.55 | 0em |
| Caption          | 14px   | 400     | 1.5  | 0em |
| Label mono       | 13px   | 500     | 1.4  | 0em |
| Micro            | 12px   | 400     | 1.45 | 0em |

> ⚠️ Framer 타이포의 핵심 시그너처는 **극한의 tight tracking** (`--framer-letter-spacing: -.05em`). 기본 Inter 기본 trackling으로는 재현 안 된다. 히어로는 `-0.05em`, 본문은 `0em`로 스텝핑할 것. 또한 가중치 100–900 전 스펙트럼이 사용되므로 variable 폰트 아니면 복제 불가.

---

## 06. Colors

### 06-1. Brand Ramp (electric blue family)

| Token | Hex |
|---|---|
| brand-bright (link)    | `#09f` (≡ `#0099FF`) |
| brand-primary-alias    | `#0099FF` |
| brand-selection 30%    | `#0099ff4d` (`selection-background-color`) |

Framer의 브랜드는 단일 hex (`#0099FF`) 앵커이며, 해당 색의 5단계 팔레트 대신 알파 변종으로 elevation을 표현한다. UUID로 저장된 "Blue Swatches" 세트:

| UUID token | Hex | 역할 |
|---|---|---|
| `--token-7caf96a9-...` | `#09f`    | link / CTA primary |
| `--token-bd71055c-...` | `#09f`    | 보조 정의 |
| `--token-eb0d9e00-...` | `#05f`    | deep blue (hover/pressed) |
| `--token-ee053477-...` | `#0cf`    | cyan variant |
| `--token-3ead4217-...` | `#09f`    | 3차 정의 (페이지별 재선언) |

### 06-2. Neutral Ramp (black family — alpha stacked)

Framer는 단일 `#000000` 위에 흰색 알파를 쌓는다. 실제 DOM 빈도 기준 Top 8:

| Hex | 역할 | 빈도 |
|---|---|---|
| `#000000`  | page bg (canvas)             | 134 |
| `#FFFFFF`  | primary text                 | 85 |
| `#FFFFFF1A`| hairline border (white 10%)  | 54 |
| `#00000000`| 투명 (border placeholder)    | 50 |
| `#FFFFFF14`| subtle overlay (white ~8%)   | 32 |
| `#FFFFFF99`| secondary text (white 60%)   | 20 |
| `#FFFFFFCC`| emphasized text (white 80%)  | 4  |
| `#FFFFFF66`| tertiary text (white 40%)    | 8  |

### 06-3. Dark Surface Steps (opaque)

| Hex | 역할 |
|---|---|
| `#080808` | surface-deep |
| `#141414` | surface-1 (card) |
| `#171717` | surface-1 alt |
| `#1A1A1A` | surface-2 |
| `#1D1D1D` | surface-2 alt |
| `#1F1F1F` | surface-3 |
| `#212121` | surface-3 alt |
| `#222222` | surface-4 |
| `#242424` | elevated card |
| `#2B2B2B` | modal / dropdown |
| `#2E2E2E` | divider between panels |
| `#474747` | border-strong |

### 06-4. Accent Families (Color Style 팔레트)

디자이너가 Studio에서 만든 컬러 프리셋. UUID 기반 — DESIGN.md에서 UUID를 재현할 수는 없지만 hex는 토큰화 가능.

| Family | Key step | Hex |
|---|---|---|
| purple       | primary | `#60f` (`#6600ff`) |
| violet       | bright  | `#90f` (`#9900ff`) |
| pink         | bright  | `#f06` (`#ff0066`) |
| red          | bright  | `#f02` (`#ff0022`) |
| orange       | primary | `#fd7702` |
| yellow       | bright  | `#fb0` (`#ffbb00`) |
| cyan         | primary | `#0cf` (`#00ccff`) |
| teal         | primary | `#2dd` (`#22dddd`) |
| green-mint   | primary | `#4cd963` |
| gray-muted   | text    | `#888`, `#999` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| text-primary       | `#ffffff`   | 주 텍스트 |
| text-secondary     | `#FFFFFF99` | 보조 텍스트 (60% 알파) |
| text-tertiary      | `#FFFFFF66` | 비활성 텍스트 (40% 알파) |
| link               | `#09f`      | 링크 기본 |
| selection-bg       | `#0099ff4d` | 선택 영역 배경 (30% 알파) |
| border-hairline    | `#FFFFFF1A` | 카드/섹션 경계선 |
| overlay-soft       | `#FFFFFF14` | 미묘한 오버레이 |
| divider-black      | `#0000000D` | 검은 divider (5% 알파) |

### 06-6. Semantic Alias Layer

Framer Studio의 "Color Style" → 런타임 CSS 변수 매핑. 앱이 UUID를 써서 디자이너 토큰을 참조한다.

| Alias | Resolves to | Usage |
|---|---|---|
| `--token-958e2cd1-...` | `#000000`    | page background |
| `--token-26e3cb56-...` | `#ffffff`    | primary text (framer-text-color 기본값) |
| `--token-c534b380-...` | `#ffffff1a`  | default border |
| `--token-289cb3ad-...` | `#fffc`      | emphasized text (80% 알파) |
| `--token-8f5eb515-...` | `#fff9`      | secondary text (60% 알파) |
| `--token-f5637926-...` | `#fff6`      | tertiary text (40% 알파) |
| `--token-81eeded8-...` | `#ffffff14`  | soft overlay |
| `--token-5e0b3b72-...` | `#1d1d1d`    | card surface |
| `--token-5e2a9781-...` | `#080808`    | deep surface |
| `--token-7caf96a9-...` | `#09f`       | brand blue (link / CTA) |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#000000`   | 134 | canvas bg |
| 2 | `#FFFFFF`   |  85 | primary text |
| 3 | `#0099FF`   |  56 | brand link |
| 4 | `#FFFFFF1A` |  54 | hairline border |
| 5 | `#00000000` |  50 | transparent slot |
| 6 | `#FFFFFF14` |  32 | soft overlay |
| 7 | `#FFFFFF99` |  20 | secondary text |
| 8 | `#2B2B2B`   |  16 | modal surface |
| 9 | `#222222`   |  14 | surface-4 |
| 10| `#1A1A1A`   |  12 | surface-2 |

---

## 07. Spacing

Framer는 디자이너가 픽셀 단위로 직접 배치하므로 코어 spacing 토큰은 존재하지 않는다. `--framer-paragraph-spacing`, `--framer-letter-spacing` 등 8개 타이포 전용 변수만 런타임 변수로 존재. 실제 레이아웃 간격은 인라인 px.

| Token | Value | Use case |
|---|---|---|
| `--framer-paragraph-spacing` | 40px (hero), 20px (blockquote) | paragraph 간격 |
| `--framer-letter-spacing`    | -0.05em (hero), 0em (body)     | optical tracking |
| `--framer-font-size-scale`   | 0.8                            | 반응형 축소 |
| `--ticker-gap`               | 10px                           | 로고 ticker 간격 |

**권장 대체 scale** (Framer 홈 인라인 값 빈도 기반):

| Token | Value | Use case |
|---|---|---|
| space-1  | 4px   | 아이콘 간격 |
| space-2  | 8px   | 버튼 내부 |
| space-3  | 12px  | 버튼 gap |
| space-4  | 16px  | 카드 내부 |
| space-5  | 24px  | section 내부 |
| space-6  | 32px  | 섹션 간격 |
| space-7  | 48px  | section gap |
| space-8  | 64px  | block gap |
| space-9  | 80px  | hero 여백 |
| space-10 | 120px | major section |

---

## 08. Radius

Framer는 14종의 radius를 사용. 홈페이지 빈도 Top 기준:

| Token | Value | Context |
|---|---|---|
| radius-xs    | 2px   | badge, inline chip |
| radius-sm    | 5px   | small button |
| radius-md    | 6px   | input |
| radius-md+   | 7px   | dense button |
| radius-lg    | 8px   | card, primary button (31회 — **가장 많음**) |
| radius-lg+   | 10px  | modal / CTA card (22회) |
| radius-xl    | 15px  | hero card (7회) |
| radius-xl+   | 18px  | large card |
| radius-2xl   | 20px  | overlay |
| radius-pill  | 100px | pill button, avatar (6회) |

---

## 09. Shadows

Framer는 shadow CSS 변수가 **0개**다. 모든 그림자는 인라인 선언이며 3-레이어 합성 패턴을 사용한다.

| Level | Value | Usage |
|---|---|---|
| shadow-ring-light  | `0 0 0 1px #ffffff1a`                                               | 카드 hairline 링 |
| shadow-ring-dark   | `0 0 0 2px #090909`                                                 | 다크 카드 이중 링 |
| shadow-card        | `0 2px 4px #00000026, 0 1px #0000000d, 0 0 0 1px #ffffff26`         | 표준 카드 (3-layer) |
| shadow-card-alt    | `0 2px 4px #0000001a, 0 1px #0000000d, 0 0 0 1px #ffffff26`         | 호버 카드 |
| shadow-card-soft   | `0 2px 4px #0000000d, 0 1px #00000005, 0 0 0 1px #00000003`         | light 섹션 카드 |
| shadow-popover     | `0 10px 10px #0000004d`                                             | 팝오버 / 툴팁 |
| shadow-side        | `-15px 0 10px #00000073`                                            | 가로 드랍 (side panel) |
| shadow-side-deep   | `-50px 0 10px #0006`                                                | 깊은 side overlay |
| shadow-drawer      | `-10px 10px 20px 10px #0009`                                        | 드로어 / 모달 |

> ⚠️ Framer 카드의 "표면에 떠 있는" 느낌은 **bottom shadow + top inner-ring** 이중 패턴이 핵심. 단일 `box-shadow: 0 4px 12px black`로는 재현 안 된다.

---

## 11. Layout Patterns

### Hero
- Layout: 중앙 정렬 단일 컬럼, 텍스트 위 / 미디어 아래
- Background: `#000000` + 풀블리드 그라디언트 SVG orb
- H1: `85–110px` / weight `500–700` / tracking `-0.05em`
- Max-width: 1200px
- Padding: 120px 64px

### Section Rhythm
```css
section {
  padding: 120px 64px;
  max-width: 1440px;
  margin-inline: auto;
}
```

### Typewriter slideshow
- 홈 히어로 내부에서 텍스트가 자동 회전 (`Sites → Startups → Apps → Portfolios...`)
- CSS `animation` + `overflow: hidden` 구현. JS로 텍스트 배열 주입.

### Ticker (logo carousel)
- 무한 스크롤 로고 스트립. `--ticker-gap: 10px`
- `transform: translateX(-100%)` + 무한 loop

---

## 12. Components

### 12.1 Primary CTA Button

```html
<a class="framer-primary-cta">
  <div>Start for free</div>
</a>
```

| Spec | Value |
|---|---|
| Background  | `#ffffff` (!! — 다크 사이트인데 primary는 흰색 fill) |
| Text color  | `#000000` |
| Font weight | 500 |
| Padding     | 14px 24px |
| Radius      | 8px |
| Hover       | opacity: 0.9 |

### 12.2 Secondary CTA Button

```html
<a class="framer-secondary-cta">
  <div>Learn more</div>
</a>
```

| Spec | Value |
|---|---|
| Background  | `#FFFFFF1A` (10% 알파) |
| Text color  | `#ffffff` |
| Border      | `1px solid #FFFFFF1A` |
| Padding     | 14px 24px |
| Radius      | 8px |

### 12.3 Hero Card (feature block)

```html
<div class="framer-hero-card">
  <h3>Site builder</h3>
  <p>Drag, drop, ship.</p>
</div>
```

| Spec | Value |
|---|---|
| Background  | `#141414` — `#1D1D1D` (surface-1~2) |
| Border      | `1px solid #FFFFFF1A` |
| Radius      | 15px |
| Padding     | 32px |
| Shadow      | `0 2px 4px #00000026, 0 1px #0000000d, 0 0 0 1px #ffffff26` |

### 12.4 Link (inline)

```html
<a href="#">read more</a>
```

| Spec | Value |
|---|---|
| Color       | `#09f` |
| text-decoration | none (hover: underline) |

> ⚠️ Framer는 이른바 "BEM 컴포넌트 클래스"가 없다. 실제 마크업은 `class="framer-0dh8F framer-14xxkp7"`처럼 빌더가 생성한 해시 2개가 붙으며, 페이지마다 해시가 다르다. **DESIGN.md의 클래스명(`framer-primary-cta` 등)은 재구현용 임시 이름이며, 실제 Framer 사이트 HTML을 직접 재사용할 수는 없다.**

---

## 14. Drop-in CSS

```css
/* Framer — copy into your root stylesheet */
:root {
  /* Fonts */
  --framer-font-family:      "Inter Variable", "Inter Variable Placeholder", "Inter Display", "Inter", -apple-system, sans-serif;
  --framer-font-family-code: "Geist Mono", "JetBrains Mono", ui-monospace, monospace;
  --framer-font-weight-normal: 400;
  --framer-font-weight-bold:   500;
  --framer-letter-spacing-tight: -0.05em;

  /* Brand */
  --framer-color-brand:         #0099FF;
  --framer-color-brand-deep:    #0055FF;
  --framer-color-brand-selection:#0099ff4d;

  /* Surfaces */
  --framer-bg-page:    #000000;
  --framer-bg-deep:    #080808;
  --framer-bg-card-1:  #141414;
  --framer-bg-card-2:  #1D1D1D;
  --framer-bg-modal:   #2B2B2B;

  /* Text (알파 stack) */
  --framer-text-max:   #ffffff;
  --framer-text-high:  #ffffffcc;   /* 80% */
  --framer-text-med:   #ffffff99;   /* 60% */
  --framer-text-low:   #ffffff66;   /* 40% */

  /* Borders (알파 stack) */
  --framer-border-hairline: #ffffff1a; /* 10% */
  --framer-overlay-soft:    #ffffff14; /* 8%  */
  --framer-border-strong:   #474747;

  /* Radius */
  --framer-radius-sm: 5px;
  --framer-radius-md: 8px;
  --framer-radius-lg: 15px;
  --framer-radius-pill: 100px;

  /* Shadows */
  --framer-shadow-card:    0 2px 4px #00000026, 0 1px #0000000d, 0 0 0 1px #ffffff26;
  --framer-shadow-popover: 0 10px 10px #0000004d;
}

html, body {
  background: var(--framer-bg-page);
  color: var(--framer-text-max);
  font-family: var(--framer-font-family);
  font-weight: var(--framer-font-weight-normal);
  -webkit-font-smoothing: antialiased;
}

::selection { background: var(--framer-color-brand-selection); color: #fff; }
a { color: var(--framer-color-brand); text-decoration: none; }
h1, h2, h3 { letter-spacing: var(--framer-letter-spacing-tight); font-weight: 500; }
```

---

## 16. DO / DON'T

### ✅ DO
- `#0099FF` (동일 표기: `#09f`)를 링크 / CTA / selection 브랜드 컬러로 고정할 것.
- Dark surface는 불투명 회색이 아니라 `#000000` 위에 `#FFFFFF1A` / `#FFFFFF14` 알파 레이어를 쌓아서 만들 것.
- Hero 타이포는 `85–110px` + `-0.05em` tracking + weight 500~700. 기본 Inter tracking으로는 Framer 히어로가 나오지 않는다.
- `Inter Variable` + `"Inter Variable Placeholder"` 폴백을 함께 선언해 Framer 런타임의 layout-shift 방지 패턴을 재현할 것.
- 카드 그림자는 3-layer 합성 (`0 2px 4px #00000026, 0 1px #0000000d, 0 0 0 1px #ffffff26`)으로 할 것.
- Primary CTA는 **흰 배경 + 검은 텍스트** (다크 사이트인데도). Secondary는 `#FFFFFF1A` 알파 fill.
- Radius는 8px가 기본 (31회), 대형 카드는 15px, pill은 100px.

### ❌ DON'T
- ❌ 불투명 `#1A1A1A` / `#222` 단일 카드 bg로 섹션을 채우지 말 것 → Framer 특유의 레이어드 룩이 사라진다.
- ❌ `font-weight: 400`만 쓰지 말 것 — 실제로는 100, 200, 300, 500, 700, 800, 900까지 전 스펙트럼 사용.
- ❌ `Inter` 단일 선언 → Display / Variable / Placeholder 3-stack 필요.
- ❌ 단일 `box-shadow: 0 4px 12px rgba(0,0,0,0.5)` → Framer의 "떠 있는" 느낌은 top hairline ring + bottom shadow 조합이 필수.
- ❌ 해시 클래스 (`framer-0dh8F`)를 복사해서 쓰지 말 것 — 페이지마다 재생성되므로 의미 없다.
- ❌ `#0099FF`에 별도 hover 색을 만들지 말 것 — Framer는 `#05F` (deep blue)로만 내리고 알파 조작은 하지 않는다.
- ❌ Hero 타이포에 양수 tracking (`0.02em`)을 주지 말 것 — Framer는 항상 음수 (-.05em ~ -.03em).
- ❌ 페이지 배경을 `#0d1117` 같은 블루틴트 다크로 만들지 말 것 — Framer는 순수 `#000000` 앵커.
