---
slug: atlassian
service_name: Atlassian
site_url: https://www.atlassian.com
fetched_at: 2026-04-11
default_theme: light
brand_color: "#1868DB"
primary_font: Atlassian Sans
font_weight_normal: 400
token_prefix: ds
---

# DESIGN.md — Atlassian (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Atlassian의 시각 언어는 **신뢰·생산성·명료함**을 3대 축으로 삼는다. 마케팅 사이트(`atlassian.com`)와 앱 UI(Jira·Confluence·Atlaskit)는 각각 다른 폰트 팔레트를 쓰지만, 브랜드 블루 `#1868DB` 하나로 시각적 일관성을 유지한다. 모든 텍스트·링크·CTA가 이 색 하나를 앵커로 삼는다.

배경은 순수 화이트(`#FFFFFF`)와 연한 선큰 그레이(`#F8F8F8`) 두 단계만 쓴다. 그 위에 텍스트는 `#292A2E`(primary) → `#505258`(subtle) → `#6B6E76`(subtlest) 3단계 명도로 계층을 표현한다. 별도의 배경 색조 없이 타이포그래피 명도 차이만으로 정보 위계를 만드는 것이 특징이다.

가변 폰트 weight `653`이 브랜드 개성의 핵심이다. Atlassian Sans의 비표준 bold weight는 일반 700과 달리 획이 더 정밀하게 조절되어 헤딩에 고유한 밀도감을 준다. 마케팅 헤딩은 `Charlie Display`로 전환되어 앱 UI와 시각적 온도 차를 만든다.

accent 컬러 10개 family(red·orange·yellow·lime·green·teal·blue·purple·magenta·gray)는 lozenge/badge 전용 시맨틱 컬러로 사용된다. subtlest 배경 + bolder 텍스트 페어가 낮은 채도로 상태를 표현하는 패턴이 Atlassian UI 전체를 관통한다. purple(`#803FA5`)은 discovery/new 상태 전용이며 보조 브랜드 컬러로 오용해선 안 된다.

elevation은 단일 shadow가 아닌 **dual-layer 원자**(offset shadow + hairline outline)로 구현된다. `0px 1px 1px #1E1F2140, 0px 0px 1px #1E1F214F` 패턴이 카드·팝오버·드롭다운 모두에 일관되게 적용된다. 이 미세한 두께 차이가 Atlassian UI에 특유의 정밀하고 절제된 depth감을 만든다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Atlassian처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Atlassian Sans", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #292A2E; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #1868DB; }
```

**절대 하지 말아야 할 것 하나**: 구 브랜드 블루 `#0052CC`를 쓰지 말 것. 현재 ADS v2의 브랜드는 `#1868DB`이며, CSS 전체 빈도 596회로 절대 다수를 차지한다 (`#0052CC`는 28회로 legacy alias만 남음). 또한 헤딩 볼드는 `700`이 아니라 **`653`** — Atlassian Sans 가변 폰트의 비표준 weight다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.atlassian.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| CSS files | 4개 (atlaskit-tokens_light + spacing + typography + inline) |
| CSS total | 334,143 chars |
| Custom properties | 490개 (`--ds-*` 기준) |
| Color vars | 314개 |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: marketing site (Atlassian 공식 `.atlassian.com`)
- **Design system**: ADS (Atlassian Design System v2) — token prefix `--ds-*`
- **CSS architecture**: 시맨틱 2-tier, 다크모드 `data-color-mode="dark"` 스위칭 구조
  ```
  semantic tier   (--ds-text-*, --ds-background-*, --ds-border-*)
  component tier  (--ds-surface-*, --ds-shadow-*, --ds-space-*)
  theme switcher  html[data-color-mode="light|dark"][data-theme~="light:light"]
  ```
- **Class naming**: atlaskit 유틸 기반 (emotion-in-JS), 런타임 hash 클래스 (`_1ikmwd8` 등) 대거 사용
- **Default theme**: light (bg = `#FFFFFF`, surface = `#FFFFFF`, sunken = `#F8F8F8`)
- **Font loading**: 마케팅 사이트는 `Charlie Text`/`Charlie Display` 브랜드 폰트, 앱 UI는 `Atlassian Sans` (가변 폰트)
- **Canonical anchor**: `--ds-text-brand: #1868DB` — 단일 링크/CTA 블루 앵커

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font (브랜드)**: `Charlie Display` (마케팅 히어로/피처 제목)
- **Body font (브랜드)**: `Charlie Text` (마케팅 본문)
- **UI font (앱)**: `Atlassian Sans` (가변 폰트, Atlaskit 전체)
- **Code font**: `Atlassian Mono`
- **Weight normal / medium / semibold / bold**: `400` / `500` / `600` / **`653`**

```css
:root {
  /* Atlaskit UI (앱) */
  --ds-font-family-body:    "Atlassian Sans", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, "Helvetica Neue", sans-serif;
  --ds-font-family-heading: "Atlassian Sans", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, "Helvetica Neue", sans-serif;
  --ds-font-family-code:    "Atlassian Mono", ui-monospace, Menlo, "Segoe UI Mono", "Ubuntu Mono", monospace;

  /* Atlassian.com (마케팅) */
  --ds-font-family-brand-heading: "Charlie Display", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, "Helvetica Neue", sans-serif;
  --ds-font-family-brand-body:    "Charlie Text", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, "Helvetica Neue", sans-serif;

  --ds-font-weight-regular:  400;
  --ds-font-weight-medium:   500;
  --ds-font-weight-semibold: 600;
  --ds-font-weight-bold:     653; /* ⚠ 비표준 가변 폰트 weight */
}
```

> **주의**: `653`은 Atlassian Sans variable font 전용 비표준 weight. 일반 font-weight: bold (700)로 대체하면 헤딩 획 두께가 다르게 렌더된다.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Family |
|---|---|---|---|---|
| `--ds-font-heading-xxlarge` | 2rem (32px) | 653 | 2.25rem (36px) | Atlassian Sans |
| `--ds-font-heading-xlarge`  | 1.75rem (28px) | 653 | 2rem (32px) | Atlassian Sans |
| `--ds-font-heading-large`   | 1.5rem (24px)  | 653 | 1.75rem (28px) | Atlassian Sans |
| `--ds-font-heading-medium`  | 1.25rem (20px) | 653 | 1.5rem (24px)  | Atlassian Sans |
| `--ds-font-heading-small`   | 1rem (16px)    | 653 | 1.25rem (20px) | Atlassian Sans |
| `--ds-font-heading-xsmall`  | 0.875rem (14px)| 653 | 1.25rem (20px) | Atlassian Sans |
| `--ds-font-heading-xxsmall` | 0.75rem (12px) | 653 | 1rem (16px)    | Atlassian Sans |
| `--ds-font-body-large`      | 1rem (16px)    | 400 | 1.5rem (24px)  | Atlassian Sans |
| `--ds-font-body`            | 0.875rem (14px)| 400 | 1.25rem (20px) | Atlassian Sans |
| `--ds-font-body-small`      | 0.75rem (12px) | 400 | 1rem (16px)    | Atlassian Sans |
| `--ds-font-metric-large`    | 1.75rem (28px) | 653 | 2rem (32px)    | Atlassian Sans |
| `--ds-font-metric-medium`   | 1.5rem (24px)  | 653 | 1.75rem (28px) | Atlassian Sans |
| `--ds-font-metric-small`    | 1rem (16px)    | 653 | 1.25rem (20px) | Atlassian Sans |
| `--ds-font-code`            | 0.875em        | 400 | 1              | Atlassian Mono |

> ⚠️ 모든 heading/metric scale은 weight **`653`** 고정. line-height는 px 단위가 아닌 `rem` 쌍(2rem/2.25rem)으로 CSS `font` shorthand에 인코딩되어 있다. 헤딩과 본문의 폰트 패밀리는 동일 (`Atlassian Sans`) — 차별은 size + weight만으로 낸다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Blue (canonical)
<!-- --ds-text-brand / --ds-background-brand-* / --ds-background-accent-blue-* -->

| Token | Hex |
|---|---|
| `--ds-text-brand` / `--ds-link` | `#1868DB` ⭐ **primary blue** |
| `--ds-link-pressed` / `--ds-background-brand-bold-hovered` | `#1558BC` |
| `--ds-background-brand-bold-pressed` | `#144794` |
| `--ds-background-accent-blue-subtle` | `#669DF1` |
| `--ds-background-accent-blue-subtle-hovered` | `#8FB8F6` |
| `--ds-background-accent-blue-subtler` | `#CFE1FD` |
| `--ds-background-accent-blue-subtlest` | `#E9F2FE` |
| `--ds-text-accent-blue-bolder` | `#123263` |
| `--ds-background-brand-boldest` | `#1C2B42` |

### 06-3. Neutral (gray)
<!-- SOURCE: auto -->

| Token | Hex | Usage |
|---|---|---|
| `--ds-text` | `#292A2E` | primary text |
| `--ds-text-subtle` | `#505258` | secondary text |
| `--ds-text-subtlest` | `#6B6E76` | tertiary text |
| `--ds-background-accent-gray-subtle` | `#8C8F97` | divider mid |
| `--ds-background-accent-gray-subtler` | `#DDDEE1` | chip bg |
| `--ds-background-accent-gray-subtlest` | `#F0F1F2` | surface subtle |
| `--ds-surface-sunken` | `#F8F8F8` | page sunken |
| `--ds-surface` | `#FFFFFF` | card surface |
| `--ds-text-inverse` | `#FFFFFF` | text on dark |
| `--ds-background-neutral-bold` | `#292A2E` | dark CTA bg |

### 06-4. Accent Families
<!-- SOURCE: auto -->

ADS는 10개 accent family를 full 계층(subtlest / subtler / subtle / bolder)으로 운영. 각 family의 대표 step:

| Family | Subtlest (bg) | Subtle (mid) | Bolder (text/bold) |
|---|---|---|---|
| **red** (danger) | `#FFECEB` | `#F87168` | `#AE2E24` |
| **orange** | `#FFF5DB` | `#FCA700` | `#9E4C00` |
| **yellow** (warning) | `#FEF7C8` | `#EED12B` | `#7F5F01` |
| **lime** (success) | `#EFFFD6` | `#94C748` | `#4C6B1F` |
| **green** | `#DCFFF1` | `#4BCE97` | `#216E4E` |
| **teal** | `#E7F9FF` | `#6CC3E0` | `#206A83` |
| **blue** (brand) | `#E9F2FE` | `#669DF1` | `#1558BC` |
| **purple** (discovery) | `#F8EEFE` | `#C97CF4` | `#803FA5` |
| **magenta** | `#FFECF8` | `#E774BB` | `#943D73` |
| **gray** | `#F0F1F2` | `#8C8F97` | `#505258` |

### 06-5. Semantic
<!-- SOURCE: auto -->

| Token | Hex | Usage |
|---|---|---|
| `--ds-text-brand` | `#1868DB` | link / CTA text |
| `--ds-text-danger` | `#AE2E24` | error text |
| `--ds-text-warning` | `#9E4C00` | warning text |
| `--ds-text-success` | `#4C6B1F` | success text |
| `--ds-text-discovery` | `#803FA5` | purple badge text |
| `--ds-text-information` | `#1558BC` | info text |
| `--ds-icon-danger` | `#C9372C` | error icon |
| `--ds-icon-warning` | `#E06C00` | warning icon |
| `--ds-icon-success` | `#6A9A23` | success icon |
| `--ds-border-focused` | `#4688EC` | focus ring |

### 06-6. Semantic Alias Layer
<!-- SOURCE: auto -->
<!-- 이 tier가 컴포넌트 레벨 API. core hex보다 alias를 우선 사용. -->

| Alias | Resolves to | Usage |
|---|---|---|
| `--ds-background-brand-bold` | `#1868DB` | primary button bg |
| `--ds-background-brand-bold-hovered` | `#1558BC` | primary button hover |
| `--ds-background-brand-bold-pressed` | `#144794` | primary button pressed |
| `--ds-background-selected` | `#E9F2FE` | list/row selected bg |
| `--ds-background-selected-bold` | `#1868DB` | active nav bg |
| `--ds-background-neutral` | `#0515240F` | subtle surface (6% alpha black) |
| `--ds-background-neutral-hovered` | `#0B120E24` | hover subtle |
| `--ds-background-neutral-pressed` | `#080F214A` | pressed subtle |
| `--ds-blanket` | `#050C1F75` | modal overlay (46% alpha) |
| `--ds-skeleton` | `#0515240F` | loading placeholder |
| `--ds-border` | `#0B120E24` | default border (14% alpha) |
| `--ds-border-input` | `#8C8F97` | form input border |
| `--ds-interaction-hovered` | `#00000029` | hover lift tint |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto (CSS frequency count) -->

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#101214` | 1024 | dark UI text (boldest) |
| 2 | `#1868DB` | 596 | brand blue (text/link/CTA) |
| 3 | `#505258` | 235 | secondary text |
| 4 | `#FFFFFF` | 214 | surface / inverse |
| 5 | `#1558BC` | 138 | blue bolder / pressed |
| 6 | `#F8F8F8` | 134 | sunken surface |
| 7 | `#803FA5` | 123 | discovery purple |
| 8 | `#48245D` | 115 | purple bolder |
| 9 | `#DDDEE1` | 77 | border mid |
| 10 | `#FCA700` | 46 | orange subtle |

---

## 07. Spacing
<!-- SOURCE: auto -->
<!-- 네이밍 규칙: rem 기반, 토큰 번호 × 0.125rem = value (100 = 0.5rem = 8px) -->

| Token | Value | px | Use case |
|---|---|---|---|
| `--ds-space-0`   | 0rem     | 0   | reset |
| `--ds-space-025` | 0.125rem | 2   | hairline |
| `--ds-space-050` | 0.25rem  | 4   | icon inset |
| `--ds-space-075` | 0.375rem | 6   | dense chip |
| `--ds-space-100` | 0.5rem   | 8   | tight gap |
| `--ds-space-150` | 0.75rem  | 12  | compact |
| `--ds-space-200` | 1rem     | 16  | base gap |
| `--ds-space-250` | 1.25rem  | 20  | form stack |
| `--ds-space-300` | 1.5rem   | 24  | section internal |
| `--ds-space-400` | 2rem     | 32  | card padding |
| `--ds-space-500` | 2.5rem   | 40  | section gap |
| `--ds-space-600` | 3rem     | 48  | block stack |
| `--ds-space-800` | 4rem     | 64  | hero padding |
| `--ds-space-1000`| 5rem     | 80  | page rhythm |

**Negative scale**: 동일한 14-step이 `--ds-space-negative-025 … -400`까지 음수 변종으로 존재. 마진-오버랩/풀블리드 컴포넌트용.

**주요 alias**:
- `--ds--button--new-icon-padding-start` → `--ds-space-050` (4px)
- `--cl-gap: 24px` — Confluence/Jira 열 그리드 간격

---

## 08. Radius
<!-- SOURCE: auto -->

| Raw value | Count | Context |
|---|---|---|
| `3px` | 12 | input / button tight radius |
| `4px` | 9  | chip / tag |
| `6px` | 6  | card corner |
| `8px` | 5  | popover / modal |
| `2px` | 5  | hairline accent |
| `20px`| 4  | pill button |
| `15px`| 4  | rounded banner |
| `24px`| 3  | hero card |

> Atlaskit은 radius를 변수로 노출하지 않고 각 컴포넌트에서 직접 상수(`3px`/`4px`)를 사용. 이 점이 Stripe/HDS와 가장 큰 구조적 차이.

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| `--ds-shadow-raised` | `0px 1px 1px #1E1F2140, 0px 0px 1px #1E1F214F` | 카드 리프트 (2-layer) |
| `--ds-shadow-overlay` | `0px 8px 12px #1E1F2126, 0px 0px 1px #1E1F214F` | popover/dropdown |
| `--ds-shadow-overflow` | `0px 0px 8px #1E1F2129, 0px 0px 1px #1E1F211F` | 스크롤 끝단 페이드 |
| `--ds-shadow-overflow-perimeter` | `#1E1F211F` | 스크롤 perimeter 색상 only |
| `--ds-shadow-overflow-spread` | `#1E1F2129` | 스크롤 spread 색상 only |

> **패턴**: 모든 elevation이 dual-shadow 원자 (offset + hairline outline). 색은 모두 `#1E1F21` + 알파 차등.

---

## 12. Responsive Behavior
<!-- SOURCE: manual -->

Atlaskit/ADS는 공식 breakpoint 토큰을 CSS 커스텀 프로퍼티로 노출하지 않는다. 마케팅 사이트(`atlassian.com`)와 Confluence/Jira 앱 공통으로 쓰이는 실질적 그리드 기준점은 아래와 같다.

| Breakpoint | Min-width | Grid columns | Max content width | 대표 컨텍스트 |
|---|---|---|---|---|
| **xs** (mobile) | 0px     | 4  | 100%    | 모바일 단일 컬럼 |
| **sm**          | 480px   | 8  | 100%    | 큰 폰, 태블릿 세로 |
| **md**          | 768px   | 12 | 100%    | 태블릿 가로, 소형 랩탑 |
| **lg**          | 1024px  | 12 | 1280px  | 데스크탑 기본 |
| **xl**          | 1280px  | 12 | 1440px  | 와이드 데스크탑 |
| **xxl**         | 1440px  | 12 | 1680px  | 울트라와이드 |

**컬럼 간격**: `--cl-gap: 24px` (Confluence/Jira 열 그리드 기준). 마케팅 사이트 히어로 섹션은 md 이하에서 단일 컬럼, lg 이상에서 2~3 컬럼 그리드로 전환된다.

**spacing 리듬**: 모바일(`xs`/`sm`)에서는 `--ds-space-200`(16px) 기본 패딩, 데스크탑(`lg`+)에서는 `--ds-space-400`(32px) ~ `--ds-space-800`(64px) 히어로 패딩으로 단계 확장한다.

> Atlaskit 공식 `@atlaskit/primitives` 패키지는 `xcss` 유틸과 emotion 기반 반응형 prop을 지원한다. 순수 CSS 작업 시 위 기준점으로 직접 미디어 쿼리를 작성한다.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Primary button (atlaskit)
- **Background**: `var(--ds-background-brand-bold)` = `#1868DB`
- **Hover**: `var(--ds-background-brand-bold-hovered)` = `#1558BC`
- **Pressed**: `var(--ds-background-brand-bold-pressed)` = `#144794`
- **Text**: `var(--ds-text-inverse)` = `#FFFFFF`
- **Radius**: `3px` (가장 빈번)
- **Padding**: `var(--ds-space-050) var(--ds-space-150)` (4px 12px)
- **Font**: `var(--ds-font-body)` (14px / 400 / 1.25rem)

```html
<button class="ak-button ak-button--primary">Get started</button>
```

### Link / CTA (marketing)
- **Color**: `var(--ds-link)` = `#1868DB`
- **Pressed**: `var(--ds-link-pressed)` = `#1558BC`
- **Visited**: `var(--ds-link-visited)` = `#803FA5`

### Surface / Card
- **Background**: `var(--ds-surface)` = `#FFFFFF`
- **Border**: `1px solid var(--ds-border)` = `#0B120E24` (14% alpha)
- **Shadow**: `var(--ds-shadow-raised)`
- **Sunken variant**: `var(--ds-surface-sunken)` = `#F8F8F8`

### Lozenge / Badge (semantic)
Atlaskit의 signature 컴포넌트. 10개 accent family를 `subtlest + bolder` 페어로 조합:

```html
<span class="ak-lozenge ak-lozenge--information">IN PROGRESS</span>
<!-- bg: #E9F2FE, text: #123263 -->
<span class="ak-lozenge ak-lozenge--success">DONE</span>
<!-- bg: #EFFFD6, text: #37471F -->
<span class="ak-lozenge ak-lozenge--discovery">NEW</span>
<!-- bg: #F8EEFE, text: #48245D -->
```

### Navigation selected
- **Background**: `var(--ds-background-selected)` = `#E9F2FE`
- **Text**: `var(--ds-text-selected)` = `#1868DB`
- **Border-left**: `3px solid var(--ds-border-selected)` = `#1868DB`

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Atlassian — copy into your root stylesheet */
:root {
  /* Fonts */
  --ds-font-family-body:    "Atlassian Sans", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, sans-serif;
  --ds-font-family-heading: "Atlassian Sans", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, sans-serif;
  --ds-font-family-code:    "Atlassian Mono", ui-monospace, Menlo, "Segoe UI Mono", monospace;
  --ds-font-weight-regular:  400;
  --ds-font-weight-medium:   500;
  --ds-font-weight-semibold: 600;
  --ds-font-weight-bold:     653; /* 비표준 가변 폰트 weight */

  /* Brand blue — single anchor */
  --ds-text-brand:                   #1868DB;
  --ds-link:                         #1868DB;
  --ds-link-pressed:                 #1558BC;
  --ds-background-brand-bold:        #1868DB;
  --ds-background-brand-bold-hovered:#1558BC;
  --ds-background-brand-bold-pressed:#144794;
  --ds-background-brand-subtlest:    #E9F2FE;

  /* Surfaces (light default) */
  --ds-surface:        #FFFFFF;
  --ds-surface-sunken: #F8F8F8;
  --ds-surface-hovered:#F0F1F2;
  --ds-text:           #292A2E;
  --ds-text-subtle:    #505258;
  --ds-text-subtlest:  #6B6E76;
  --ds-text-inverse:   #FFFFFF;

  /* Borders (all alpha-black) */
  --ds-border:         #0B120E24; /* 14% */
  --ds-border-input:   #8C8F97;
  --ds-border-focused: #4688EC;

  /* Key spacing (rem 기반) */
  --ds-space-100: 0.5rem;
  --ds-space-200: 1rem;
  --ds-space-300: 1.5rem;
  --ds-space-400: 2rem;
  --ds-space-600: 3rem;

  /* Shadows (dual-layer 원자) */
  --ds-shadow-raised:  0px 1px 1px #1E1F2140, 0px 0px 1px #1E1F214F;
  --ds-shadow-overlay: 0px 8px 12px #1E1F2126, 0px 0px 1px #1E1F214F;
}

body {
  font-family: var(--ds-font-family-body);
  font-weight: var(--ds-font-weight-regular);
  background: var(--ds-surface);
  color: var(--ds-text);
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--ds-font-family-heading);
  font-weight: var(--ds-font-weight-bold); /* 653 */
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Atlassian
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT:   '#1868DB',
          subtlest:  '#E9F2FE',
          subtler:   '#CFE1FD',
          subtle:    '#669DF1',
          bolder:    '#1558BC',
          boldest:   '#144794',
        },
        neutral: {
          0:    '#FFFFFF',
          50:   '#F8F8F8',
          100:  '#F0F1F2',
          200:  '#DDDEE1',
          300:  '#B7B9BE',
          400:  '#8C8F97',
          500:  '#6B6E76',
          600:  '#505258',
          700:  '#3B3D42',
          800:  '#292A2E',
          900:  '#1E1F21',
          950:  '#101214',
        },
        red:     { subtle: '#F87168', bold: '#C9372C', bolder: '#AE2E24' },
        orange:  { subtle: '#FCA700', bold: '#E06C00', bolder: '#9E4C00' },
        yellow:  { subtle: '#EED12B', bold: '#B38600', bolder: '#7F5F01' },
        lime:    { subtle: '#94C748', bold: '#6A9A23', bolder: '#4C6B1F' },
        green:   { subtle: '#4BCE97', bold: '#22A06B', bolder: '#216E4E' },
        teal:    { subtle: '#6CC3E0', bold: '#2898BD', bolder: '#206A83' },
        purple:  { subtle: '#C97CF4', bold: '#AF59E1', bolder: '#803FA5' },
        magenta: { subtle: '#E774BB', bold: '#CD519D', bolder: '#943D73' },
      },
      fontFamily: {
        sans: ['"Atlassian Sans"', 'ui-sans-serif', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'sans-serif'],
        brand: ['"Charlie Display"', 'ui-sans-serif', 'sans-serif'],
        body: ['"Charlie Text"', 'ui-sans-serif', 'sans-serif'],
        mono: ['"Atlassian Mono"', 'ui-monospace', 'Menlo', 'monospace'],
      },
      fontWeight: {
        normal:   '400',
        medium:   '500',
        semibold: '600',
        bold:     '653', // 비표준
      },
      spacing: {
        '0.25': '0.125rem', '0.5': '0.25rem', '0.75': '0.375rem',
        '1':    '0.5rem',   '1.5': '0.75rem', '2':   '1rem',
        '2.5':  '1.25rem',  '3':   '1.5rem',  '4':   '2rem',
        '5':    '2.5rem',   '6':   '3rem',    '8':   '4rem',
        '10':   '5rem',
      },
      borderRadius: {
        xs: '2px',
        sm: '3px',
        md: '4px',
        lg: '6px',
        xl: '8px',
      },
      boxShadow: {
        raised:  '0 1px 1px rgba(30,31,33,0.25), 0 0 1px rgba(30,31,33,0.31)',
        overlay: '0 8px 12px rgba(30,31,33,0.15), 0 0 1px rgba(30,31,33,0.31)',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Purpose | Hex | Token |
|---|---|---|
| Brand blue (link/CTA/button) | `#1868DB` | `--ds-text-brand`, `--ds-link`, `--ds-background-brand-bold` |
| Blue hover | `#1558BC` | `--ds-background-brand-bold-hovered` |
| Blue pressed | `#144794` | `--ds-background-brand-bold-pressed` |
| Blue subtlest (selected bg) | `#E9F2FE` | `--ds-background-brand-subtlest` |
| Primary text | `#292A2E` | `--ds-text` |
| Secondary text | `#505258` | `--ds-text-subtle` |
| Tertiary text | `#6B6E76` | `--ds-text-subtlest` |
| Surface / card | `#FFFFFF` | `--ds-surface` |
| Sunken surface | `#F8F8F8` | `--ds-surface-sunken` |
| Subtle surface | `#F0F1F2` | `--ds-surface-hovered` |
| Border (alpha) | `#0B120E24` | `--ds-border` |
| Inverse text (on dark) | `#FFFFFF` | `--ds-text-inverse` |
| Discovery / new badge | `#803FA5` | `--ds-text-discovery` |
| Danger text | `#AE2E24` | `--ds-text-danger` |
| Success text | `#4C6B1F` | `--ds-text-success` |

### Prompts

**컴포넌트 생성 프롬프트 예시:**

```
Atlassian ADS v2 스타일로 [컴포넌트명]을 만들어줘.
- 브랜드 블루: #1868DB (--ds-background-brand-bold)
- 폰트: Atlassian Sans, font-weight 400 (body) / 653 (heading)
- 카드 shadow: 0px 1px 1px #1E1F2140, 0px 0px 1px #1E1F214F
- border: 1px solid #0B120E24 (14% alpha)
- radius: 3px (button/input), 4px (chip), 6px (card)
```

**상태 뱃지/lozenge 프롬프트 예시:**

```
Atlaskit lozenge 스타일로 상태 뱃지를 만들어줘.
- IN PROGRESS: bg #E9F2FE, text #123263
- DONE: bg #EFFFD6, text #37471F
- NEW: bg #F8EEFE, text #48245D
- ERROR: bg #FFECEB, text #AE2E24
- WARNING: bg #FEF7C8, text #7F5F01
font-weight: 653, font-size: 11px, text-transform: uppercase
```

**다크 모드 전환 프롬프트 예시:**

```
Atlassian ADS 다크 모드를 구현해줘.
- 스위칭 어트리뷰트: html[data-color-mode="dark"][data-theme~="light:light"]
- 다크 모드 토큰은 ADS atlaskit-tokens_dark CSS 파일에서 --ds-surface, --ds-text 계열을 참조
- 브랜드 블루는 동일하게 #1868DB (--ds-text-brand) 유지
- 역상 텍스트: --ds-text-inverse = #FFFFFF
```

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- `#1868DB`를 브랜드 블루로 사용 — `--ds-text-brand`, `--ds-link`, `--ds-background-brand-bold` 모두 이 값.
- 헤딩에 `font-weight: 653` 적용 — Atlassian Sans 가변 폰트 전용 weight.
- 마케팅 사이트엔 `Charlie Display` + `Charlie Text`, 앱 UI엔 `Atlassian Sans` 분리.
- 10개 accent family를 `subtlest + bolder` 페어로 lozenge/badge에 사용.
- rem 기반 spacing (`0.5rem = 8px` base) 리듬 유지. 토큰 번호 × `0.125rem` = value.
- dual-shadow 원자 (`0 1px 1px + 0 0 1px`)로 card elevation 표현.
- border 색상은 순수 hex 대신 알파-블랙 (`#0B120E24`, 14%) 사용.
- 다크 모드는 `data-color-mode="dark"` 어트리뷰트로 스위칭.

### ❌ DON'T
- ❌ `#0052CC` 구 브랜드 블루 사용 (legacy alias로만 28회, 현 브랜드는 `#1868DB` 596회).
- ❌ `font-weight: 700` (Atlassian Sans의 bold는 `653`).
- ❌ `color-brand`/`color-gray-*` 같은 flat 네이밍 (실제는 `--ds-text-brand`, `--ds-background-neutral-*` 시맨틱).
- ❌ 마케팅 헤딩에 `Atlassian Sans` 강제 — `Charlie Display`가 브랜드 자산.
- ❌ 단일 shadow — Atlaskit은 모든 elevation을 dual-layer로 구성.
- ❌ radius 토큰 변수 (`--radius-md`) 기대 — Atlaskit은 컴포넌트에 하드코딩 (3px / 4px / 6px).
- ❌ purple을 보조 브랜드로 취급 — `#803FA5`는 discovery/new 상태 전용 semantic color.
