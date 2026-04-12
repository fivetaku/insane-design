---
slug: stripe
service_name: Stripe
site_url: https://stripe.com
fetched_at: 2026-04-11
default_theme: mixed
brand_color: "#533AFD"
primary_font: sohne-var
font_weight_normal: 300
token_prefix: --hds-*
---

# DESIGN.md — Stripe (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Stripe처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight 300 */
body {
  font-family: "sohne-var", "SF Pro Display", -apple-system, sans-serif;
  font-weight: 300;   /* ⚠️ 400 아님. Stripe body는 300. */
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #F8FAFD;      /* 살짝 푸른 near-white */
  --fg: #061B31;      /* 거의 검정이지만 쿨한 네이비 */
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 보라 */
:root { --brand: #533AFD; }
```

**절대 하지 말아야 할 것 하나**: 본문을 `font-weight: 400`으로 두는 것. Stripe 타이포그래피의 정체성은 **weight 300** 이다. 400으로 두면 전체가 순식간에 "평범한 SaaS"처럼 보인다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://stripe.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 574,643 bytes (Next.js SSR) |
| CSS files | 7개 외부 + 1 인라인 = 8개, 총 425,918자 |
| Token prefix | `--hds-*` (HDS — Highline Design System) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js (`mkt-ssr-statics` — Stripe 내부 마케팅 SSR 빌드)
- **Design system**: HDS (Highline Design System) — 토큰 prefix `--hds-*`
- **CSS architecture**: 3-tier 토큰 계층
  ```
  core       (--hds-color-core-*, --hds-space-core-*)   raw hex · raw px
  util       (--hds-color-util-*, --hds-color-action-*) semantic alias, core 참조
  component  (--hds-space-button-*, --hds-font-heading-xl-*) 컴포넌트별 조합
  ```
- **Class naming**: BEM-ish (`hds-button--primary`, `hds-heading--md`, `section-row`)
- **Default theme**: mixed (light 기본 `#F8FAFD`, dark 섹션 `#061B31` 교차)
- **Font loading**: 셀프 호스트 woff2 (Next.js 폰트 로더로 `sohne-var` + `SourceCodePro`)
- **Canonical anchor**: `#533AFD` — 이 보라는 `brand-600` 과 `brandDark-600` 둘 다에 고정되어 있어 라이트/다크 테마를 넘어 변하지 않는다

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `sohne-var` (Klim Type Foundry, 유료 라이선스)
- **Code font**: `SourceCodePro` (Adobe, 오픈소스)
- **Weight normal / bold**: `300` / `400`

```css
:root {
  --hds-font-family:      "sohne-var", "SF Pro Display", -apple-system, BlinkMacSystemFont, sans-serif;
  --hds-font-family-code: "SourceCodePro", "SFMono-Regular", ui-monospace, monospace;
  --hds-font-weight-normal: 300;   /* ⚠️ "normal" = 300. 400 아님. */
  --hds-font-weight-bold:   400;   /* ⚠️ "bold" = 400. 700 아님. */
}
body {
  font-family: var(--hds-font-family);
  font-weight: var(--hds-font-weight-normal);
}
```

> **라이선스 주의**: `sohne-var` 는 유료 라이선스 폰트라 재배포 불가. 자체 프로젝트에서는 `Inter Tight` 또는 (라이선스 있으면) `Söhne` 가 가장 가까운 대체재. 단 시각 매칭은 완벽하지 않다.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| `--hds-font-heading-xxs-*`  | 0.875rem (14px) | 400 | 1.2  | 0em |
| `--hds-font-heading-xs-*`   | 1rem (16px)     | 400 | 1.2  | 0em |
| `--hds-font-heading-sm-*`   | 1.125rem (18px) | 300 | 1.25 | 0em |
| `--hds-font-heading-md-*`   | 1.25rem (20px)  | 300 | 1.2  | -0.01em |
| `--hds-font-heading-lg-*`   | 1.375rem (22px) | 300 | 1.2  | -0.01em |
| `--hds-font-heading-xl-*`   | 1.75rem (28px)  | 300 | 1.07 | -0.01em |
| `--hds-font-heading-xxl-*`  | 2.125rem (34px) | 300 | 1.03 | -0.02em |
| `--hds-font-text-xxs-*`     | 0.75rem (12px)  | 300 | 1.45 | 0em |
| `--hds-font-text-xs-*`      | 0.75rem (12px)  | 300 | 1.45 | 0em |
| `--hds-font-text-sm-*`      | 0.875rem (14px) | 300 | 1.4  | 0em |
| `--hds-font-text-md-*`      | 1rem (16px)     | 300 | 1.4  | 0em |
| `--hds-font-text-lg-*`      | 1rem (16px)     | 300 | 1.35 | 0em |
| `--hds-font-text-xl-*`      | 1.125rem (18px) | 300 | 1.4  | 0em |
| `--hds-font-text-xxl-*`     | 1.75rem (28px)  | 300 | 1.07 | -0.01em |

> ⚠️ 본문은 모두 weight 300이다. `heading-xxs` 와 `heading-xs` 만 예외적으로 weight 400 인데, 이 두 스케일은 overline/eyebrow 용도(본문 블록 위에 얹는 작은 라벨). 그 외 `sm` 이상의 모든 headings 도 전부 weight 300.
>
> 큰 headings 는 negative letter-spacing 으로 optical compensation: `md~xl` = `-0.01em`, `xxl` = `-0.02em`. 이 미세 조정이 없으면 제목이 "풀어진" 느낌이 된다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (15 steps · light variant)

| Token | Hex |
|---|---|
| `--hds-color-core-brand-25`  | `#F5F5FF` |
| `--hds-color-core-brand-50`  | `#E8E9FF` |
| `--hds-color-core-brand-75`  | `#E2E4FF` |
| `--hds-color-core-brand-100` | `#D6D9FC` |
| `--hds-color-core-brand-200` | `#B9B9F9` |
| `--hds-color-core-brand-300` | `#9A9AFE` |
| `--hds-color-core-brand-400` | `#7F7DFC` |
| `--hds-color-core-brand-500` | `#665EFD` |
| `--hds-color-core-brand-600` | `#533AFD` ⭐ **canonical 보라** |
| `--hds-color-core-brand-700` | `#4032C8` |
| `--hds-color-core-brand-800` | `#2E2B8C` |
| `--hds-color-core-brand-900` | `#1C1E54` |
| `--hds-color-core-brand-925` | `#1C1E54` |
| `--hds-color-core-brand-950` | `#161741` |
| `--hds-color-core-brand-975` | `#0F1137` |

### 06-2. Brand Dark Variant (`brandDark`)

| Token | Hex |
|---|---|
| `--hds-color-core-brandDark-25`  | `#F6F7FF` |
| `--hds-color-core-brandDark-50`  | `#E4EAFF` |
| `--hds-color-core-brandDark-75`  | `#CCDAFF` |
| `--hds-color-core-brandDark-100` | `#C3D3FF` |
| `--hds-color-core-brandDark-200` | `#A8BFFF` |
| `--hds-color-core-brandDark-300` | `#92ADFF` |
| `--hds-color-core-brandDark-400` | `#7389FF` |
| `--hds-color-core-brandDark-500` | `#5D64FE` |
| `--hds-color-core-brandDark-600` | `#533AFD` ⭐ (brand-600 과 동일 anchor) |
| `--hds-color-core-brandDark-700` | `#362BAA` |
| `--hds-color-core-brandDark-800` | `#2C2484` |
| `--hds-color-core-brandDark-900` | `#222069` |
| `--hds-color-core-brandDark-925` | `#1C1B5A` |
| `--hds-color-core-brandDark-950` | `#191A51` |
| `--hds-color-core-brandDark-975` | `#171055` |

> `brand-600` 과 `brandDark-600` 이 **둘 다 `#533AFD`** 로 고정되어 있어 라이트/다크 어느 테마에서도 캐노니컬 브랜드 보라는 동일하다. 이 anchor 때문에 "Stripe 느낌"이 테마 전환에도 무너지지 않는다.

### 06-3. Neutral Ramp (light `neutral` + dark `neutralDark`)

| Step | Light (`neutral`) | Dark (`neutralDark`) |
|---|---|---|
| 0   | `#FFFFFF` | — |
| 25  | `#F8FAFD` | `#F2F7FE` |
| 50  | `#E5EDF5` | `#E3ECF7` |
| 100 | `#D4DEE9` | `#D4DEEF` |
| 200 | `#BAC8DA` | `#C0CEE6` |
| 300 | `#95A4BA` | `#A3B5D6` |
| 400 | `#7D8BA4` | `#839BC8` |
| 500 | `#64748D` | `#6480B2` |
| 600 | `#50617A` | `#45639D` |
| 700 | `#3C4F69` | `#273F73` |
| 800 | `#273951` | `#23356E` |
| 900 | `#1A2C44` | `#182659` |
| 950 | `#11273E` | `#122054` |
| 975 | `#0D253D` | `#101D4E` |
| 990 | `#061B31` | `#0D1738` |

> 주의: `neutralDark-990 = #0D1738` 은 거의 완전한 블랙 네이비. Stripe의 다크 섹션 배경은 순수 `#000` 이 아니라 여기에 고정된다.

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| **lemon** (옐로) | 200 · signature | `#F9B900` |
| lemon | 25 | `#FFF2D8` |
| lemon | 100 | `#FFE1A3` |
| lemon | 300 | `#E8A30B` |
| lemon | 500 | `#9B6829` |
| **orange** | 350 · signature | `#FF6118` |
| orange | 50 | `#FFE5DA` |
| orange | 100 | `#FFD8C6` |
| orange | 600 | `#AB3500` |
| **magenta** | 350 · signature | `#F44BCC` |
| magenta | 50 | `#FFE6F5` |
| magenta | 100 | `#FFD7EF` |
| magenta | 600 | `#A51D85` |
| **ruby** (레드핑크) | 400 · signature | `#EA2261` |
| ruby | 50 | `#FEE8EB` |
| ruby | 100 | `#FED9DE` |
| ruby | 600 | `#B51145` |

> 이 4 family 는 Stripe hero 를 감싸는 **"플레임 그래디언트"** 의 stop 으로 쓰인다. brand 보라 `#533AFD` 에서 시작해 orange `#FF6118` → magenta `#F44BCC` → ruby `#EA2261` → lemon `#F9B900` 로 흐르는 SVG 애니메이션.

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--hds-color-core-success-100` | `#B6F2C7` | success surface |
| `--hds-color-core-success-400` | `#00B261` | success icon / text |
| `--hds-color-core-success-600` | `#006F3A` | success solid |
| `--hds-color-core-error-100` | `#FEB9AC` | error surface |
| `--hds-color-core-error-400` | `#F3432A` | error icon |
| `--hds-color-core-error-500` | `#D8351E` | error solid |
| `--hds-color-core-error-600` | `#A01400` | error emphasis |

### 06-6. Semantic Alias Layer

> 이 tier 가 **컴포넌트 레벨 API** 다. 스타일링 시 core 토큰보다 alias 를 우선 사용.

```css
/* 액션 (버튼, 링크, CTA) */
--hds-color-util-action-bg-solid:      var(--hds-color-core-brandDark-500);  /* primary btn bg */
--hds-color-util-action-bg-soft:       var(--hds-color-core-brandDark-600);  /* hover */
--hds-color-util-action-bg-emphasized: var(--hds-color-core-brandDark-400);  /* active */
--hds-color-util-action-bg-subdued:    var(--hds-color-core-brandDark-700);  /* disabled */
--hds-color-util-action-border-solid:  var(--hds-color-core-brandDark-200);
--hds-color-util-action-text-max:      var(--hds-color-core-neutral-0);      /* solid btn label */

/* 배경 */
--hds-color-util-bg-min:     var(--hds-color-core-neutralDark-990);  /* page bg, dark */
--hds-color-util-bg-quiet:   var(--hds-color-core-neutralDark-950);
--hds-color-util-bg-soft:    var(--hds-color-core-neutralDark-800);

/* 텍스트 */
--hds-color-util-text-solid:   var(--hds-color-core-neutral-0);        /* primary text */
--hds-color-util-text-soft:    var(--hds-color-core-neutralDark-300);
--hds-color-util-text-quiet:   var(--hds-color-core-neutralDark-500);
--hds-color-util-text-subdued: var(--hds-color-core-neutralDark-400);

/* 보더 */
--hds-color-util-border-solid:    var(--hds-color-core-neutralDark-100);
--hds-color-util-border-soft:     var(--hds-color-core-neutralDark-300);
--hds-color-util-border-quiet:    var(--hds-color-core-neutralDark-800);
--hds-color-util-border-subdued:  var(--hds-color-core-neutralDark-700);
```

> **중요 인사이트**: util-* 가 `brandDark` / `neutralDark` 를 참조한다. Stripe 의 유틸 레이어 기본은 **다크 테마** 이다. 라이트 테마에서 쓸 때는 `util-brand-*` alias 가 `brandDark-*` 쪽으로 매핑되면서 **invert** 되는 구조 — 한 색이 primary 인 단순 시스템으로는 이 동작을 표현할 수 없다.

### 06-7. Dominant Colors (실제 DOM 빈도 순)
<!-- SOURCE: auto (CSS frequency count) -->

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 67 | card surface, solid btn text |
| 2 | `#000000` | 42 | 기본 텍스트 (몇몇 섹션) |
| 3 | `#181818` | 12 | 다크 surface |
| 4 | `#F8FAFD` | 11 | light page background (neutral-25) |
| 5 | `#533AFD` | 9 | ⭐ brand-600 canonical |
| 6 | `#FF6118` | 8 | orange-350 (플레임 gradient) |
| 7 | `#9966FF` | 8 | decorative |
| 8 | `#061B31` | 7 | neutral-990 (다크 섹션 bg) |
| 9 | `#FB76FA` | 6 | stop-color (gradient) |
| 10 | `#7232F1` | 6 | gradient stop |
| 11 | `#F6F9FC` | 6 | subtle panel bg |
| 12 | `#1318C1` | 6 | primary dark variant |
| 13 | `#FCFDFE` | 6 | near-white |
| 14 | `#FFFFFF00` | 6 | transparent overlay |
| 15 | `#0D173833` | 6 | neutral 20% alpha |

> §06-1~06-6 은 **설계된 토큰 시스템** (design time), §06-7 은 **실제 페이지 빈도** (runtime measurement). 역할이 달라 중복이 있는 건 정상.

---

## 07. Spacing
<!-- SOURCE: auto -->

> **네이밍 규칙**: `token 번호 = px × 12.5`. 즉 `space-core-200 = 16px` (200 ÷ 12.5). 소수점 없이 4px granularity 표현.

| Token | Value | Use case |
|---|---|---|
| `--hds-space-core-0`    | 0px   | zero |
| `--hds-space-core-1`    | 1px   | hairline |
| `--hds-space-core-25`   | 2px   | tight icon gap |
| `--hds-space-core-50`   | 4px   | inline gap |
| `--hds-space-core-75`   | 6px   | tight stack |
| `--hds-space-core-100`  | 8px   | element gap |
| `--hds-space-core-150`  | 12px  | form gap |
| `--hds-space-core-200`  | 16px  | card padding, section gap |
| `--hds-space-core-250`  | 20px  | comfortable gap |
| `--hds-space-core-300`  | 24px  | component spacing |
| `--hds-space-core-350`  | 28px  | — |
| `--hds-space-core-400`  | 32px  | section padding |
| `--hds-space-core-450`  | 36px  | — |
| `--hds-space-core-500`  | 40px  | — |
| `--hds-space-core-550`  | 44px  | button height (default) |
| `--hds-space-core-600`  | 48px  | large section gap |
| `--hds-space-core-700`  | 56px  | — |
| `--hds-space-core-800`  | 64px  | page section spacing |
| `--hds-space-core-900`  | 72px  | — |
| `--hds-space-core-1000` | 80px  | hero padding |
| `--hds-space-core-1200` | 96px  | — |
| `--hds-space-core-1400` | 112px | — |
| `--hds-space-core-1600` | 128px | — |
| `--hds-space-core-1800` | 144px | — |
| `--hds-space-core-2000` | 160px | — |
| `--hds-space-core-2200` | 176px | — |
| `--hds-space-core-2400` | 192px | — |
| `--hds-space-core-2500` | 200px | — |

**주요 alias**:
- `--hds-space-button-height` → `--hds-space-core-550` (44px)
- `--hds-space-block-stack-gap-md/lg/xl` → 섹션 스택 gap
- `--hds-space-block-column-gap` → 가로 column gap
- `--hds-space-layout-content-maxWidth` → 레이아웃 그리드 max width

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| `--hds-space-core-radius-none`  | 0px    | 모서리 없음 |
| `--hds-space-core-radius-xs`    | 2px    | 인라인 칩, 작은 태그 |
| `--hds-space-core-radius-sm`    | 4px    | 작은 버튼, 배지 |
| `--hds-space-core-radius-md`    | 6px    | 버튼, 인풋 (기본) |
| `--hds-space-core-radius-lg`    | 16px   | 카드 |
| `--hds-space-core-radius-xl`    | 32px   | 히어로 카드, 모달 |
| `--hds-space-core-radius-round` | 99999px | 필, 아바타, 원형 |

---

## 09. Shadows
<!-- SOURCE: auto -->

> **패턴**: 모든 elevation 이 **듀얼 섀도 원자** — 상단 offset 하나와 하단 offset 하나를 겹쳐 쌓는 구조. 단층 `box-shadow` 로 치환하면 깊이감이 무너진다.

| Level | Value | Usage |
|---|---|---|
| `--hds-shadow-sm` | `0 5px 14px <color>, 0 2px 8px <color>` | 정적 카드, 인라인 surface |
| `--hds-shadow-md` | `0 6px 22px <color>, 0 4px 8px <color>` | 팝오버, 드롭다운, 플로팅 nav |
| `--hds-shadow-lg` | `0 15px 40px -2px <color>, 0 5px 20px -2px <color>` | 모달, 커맨드 팔레트, 오버레이 |

각 원자는 컴포넌트 변수로 분해돼 있다: `--hds-shadow-sm-top-offset-y`, `--hds-shadow-sm-bottom-blur` 등. 한쪽 레이어만 독립 조정 가능 — 전체 토큰을 새로 쓸 필요 없다.

---

## 10. Motion
<!-- OPTIONAL -->
<!-- SOURCE: manual -->

CSS 에 별도 motion 토큰 변수(`--hds-motion-*` 또는 `--hds-transition-*`)는 없지만, 관측된 인터랙션 패턴:

| Pattern | Value | Usage |
|---|---|---|
| hover arrow slide | `200ms ease` | `.hds-icon-hover-arrow` — 링크 호버 시 화살표가 오른쪽으로 이동 |
| button darken | `150ms ease` | primary button hover → `brandDark-600` 로 10% 어두워짐 |
| focus ring | `150ms ease` | focus-visible 시 2px offset 보라 링 |

---

## 11. Layout Patterns
<!-- OPTIONAL -->
<!-- SOURCE: manual -->

### Hero
- **Layout**: 2-column — 왼쪽 텍스트 스택, 오른쪽 프로덕트 UI 목업
- **Background**: 라이트 네이비-화이트 (`#F8FAFD`), 뒤로 플레임 SVG 그래디언트
- **H1**: `2.125rem` / weight `300` / tracking `-0.02em` / color `#0D173B` (neutralDark-990 근방)
- **Subheading**: `1rem-1.125rem` / weight `300` / color `#50617A` (util-text-quiet)

### Section Rhythm
```css
section {
  padding: 80px 24px;           /* --hds-space-core-1000 × --hds-space-core-300 */
  max-width: 1200px;             /* 콘텐츠 max width */
  margin-inline: auto;
}
```

---

## 12. Components
<!-- SOURCE: auto+manual -->

BEM 클래스는 실제 rendered HTML 에서 관측한 그대로.

### `.hds-button`

```html
<button class="hds-button hds-button--primary">Start now</button>
<button class="hds-button hds-button--secondary">Contact sales</button>
```

| Property | Primary | Secondary |
|---|---|---|
| background | `#5D64FE` (util-action-bg-solid → brandDark-500) | transparent |
| color | `#FFFFFF` (util-action-text-max) | `#FFFFFF` |
| border | none | 1px `#A8BFFF` (util-action-border-solid) |
| height | `44px` (space-core-550) | `44px` |
| radius | `6px` (radius-md) | `6px` |
| weight | `400` (font-weight-bold) | `400` |
| hover | → `#533AFD` (brandDark-600) | border brightens |

> 이 빌드에 `--ghost` variant 는 없다. 필요하면 `secondary` 에서 border 만 제거하면 된다.

### `.hds-heading`

- 7 scales: `xxs · xs · sm · md · lg · xl · xxl`
- modifiers: `--subdued` (util-text-soft 적용), `--inline` (인라인 플로우)
- `xxs` / `xs` 만 weight 400 (overline 용도), `sm` 이상은 모두 weight 300
- 큰 scale 은 letter-spacing 음수 optical compensation

```html
<h1 class="hds-heading hds-heading--xxl">Financial infrastructure to grow your revenue.</h1>
```

### `.hds-text`

- 7 scales: `xxs · xs · sm · md · lg · xl · xxl`
- modifiers: `--soft` (util-text-soft), `--emphasized` (util-text-solid), `--inline`
- 모두 weight 300

### `.hds-link--callout`

- 링크 CTA (버튼 아님) — `.hds-icon-hover-arrow` 와 페어
- color `#92ADFF` (brandDark-300) on dark, `#533AFD` 로 라이트에서 가독성
- 호버 시 화살표가 200ms 이동 — Stripe 특유의 시그너처 인터랙션

```html
<a href="/docs" class="hds-link hds-link--callout">
  Explore the API
  <svg class="hds-icon-hover-arrow"><!-- arrow --></svg>
</a>
```

### 레이아웃 프리미티브

- `.section-row` — space-block-column-gap 반응형 row
- `.carousel__inner` / `.carousel__item` — 가로 스크롤
- `.logo-carousel__item` — 고객 로고 스트립

레이아웃 프리미티브는 일반 "컴포넌트"가 아니라 HDS spacing 토큰으로 콘텐츠를 감싸는 **구조적 원자**. Hero 카피는 거의 항상 `.section-row` 로 래핑되고, 그 gap 은 `space-block-stack-gap-*` 를 소비한다.

---

## 13. Content / Copy Voice
<!-- OPTIONAL -->
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 선언문, 6~10 단어, 종결 "." | "Financial infrastructure to grow your revenue." |
| Primary CTA | 동사 우선 2 단어 | "Start now" · "Get started" |
| Secondary CTA | 영업/세일즈 동선 | "Contact sales" |
| Link callout | 동사 + 목적어 | "Explore the API" · "Read the docs" · "View pricing" |
| Subheading | headline 뒷받침 한 문장, 수치/범위 포함 가능 | "from your first transaction to your billionth." |
| Tone | 자신감 있는 선언형. 마케팅 형용사 최소화. | — |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Stripe — 프로젝트 루트 스타일시트에 복사 */
:root {
  /* Fonts */
  --hds-font-family:       "sohne-var", "SF Pro Display", -apple-system, BlinkMacSystemFont, sans-serif;
  --hds-font-family-code:  "SourceCodePro", "SFMono-Regular", ui-monospace, monospace;
  --hds-font-weight-normal: 300;
  --hds-font-weight-bold:   400;

  /* Brand (anchor + 4 steps) */
  --hds-color-core-brand-25:  #F5F5FF;
  --hds-color-core-brand-300: #9A9AFE;
  --hds-color-core-brand-500: #665EFD;
  --hds-color-core-brand-600: #533AFD;   /* ← canonical */
  --hds-color-core-brand-900: #1C1E54;

  /* Surfaces */
  --hds-color-core-neutral-25:      #F8FAFD;   /* light page bg */
  --hds-color-core-neutralDark-990: #0D1738;   /* dark section bg */
  --hds-color-core-neutral-0:       #FFFFFF;   /* card surface */
  --hds-color-util-text-solid:      #0D173B;   /* dark ink text */
  --hds-color-util-text-soft:       #50617A;   /* muted text */

  /* Semantic aliases */
  --hds-color-util-action-bg-solid: #5D64FE;   /* primary btn bg */

  /* Key spacing */
  --hds-space-core-100: 8px;
  --hds-space-core-150: 12px;
  --hds-space-core-200: 16px;
  --hds-space-core-300: 24px;
  --hds-space-core-400: 32px;
  --hds-space-core-550: 44px;   /* button height */
  --hds-space-core-600: 48px;

  /* Radius */
  --hds-space-core-radius-md: 6px;
  --hds-space-core-radius-lg: 16px;
}

body {
  font-family: var(--hds-font-family);
  font-weight: var(--hds-font-weight-normal);
  background: var(--hds-color-core-neutral-25);
  color: var(--hds-color-util-text-solid);
}

h1, h2, h3 {
  font-weight: var(--hds-font-weight-normal);   /* 300 — 상식과 반대 */
  letter-spacing: -0.01em;
}
h1 { letter-spacing: -0.02em; }
strong, b { font-weight: var(--hds-font-weight-bold); }   /* 400 */
```

---

## 15. Tailwind Config
<!-- OPTIONAL -->
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Stripe
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '#F5F5FF', 50:  '#E8E9FF', 75:  '#E2E4FF', 100: '#D6D9FC',
          200: '#B9B9F9', 300: '#9A9AFE', 400: '#7F7DFC', 500: '#665EFD',
          600: '#533AFD', 700: '#4032C8', 800: '#2E2B8C', 900: '#1C1E54',
          925: '#1C1E54', 950: '#161741', 975: '#0F1137',
        },
        neutral: {
          0:   '#FFFFFF', 25:  '#F8FAFD', 50:  '#E5EDF5', 100: '#D4DEE9',
          200: '#BAC8DA', 300: '#95A4BA', 400: '#7D8BA4', 500: '#64748D',
          600: '#50617A', 700: '#3C4F69', 800: '#273951', 900: '#1A2C44',
          950: '#11273E', 975: '#0D253D', 990: '#061B31',
        },
        neutralDark: {
          25: '#F2F7FE',  50: '#E3ECF7', 100: '#D4DEEF', 200: '#C0CEE6',
          300: '#A3B5D6', 400: '#839BC8', 500: '#6480B2', 600: '#45639D',
          700: '#273F73', 800: '#23356E', 900: '#182659', 950: '#122054',
          975: '#101D4E', 990: '#0D1738',
        },
        orange:  { 350: '#FF6118' },
        magenta: { 350: '#F44BCC' },
        ruby:    { 400: '#EA2261' },
        lemon:   { 200: '#F9B900' },
        success: { 400: '#00B261' },
        error:   { 500: '#D8351E' },
      },
      fontFamily: {
        sans: ['"sohne-var"', '"SF Pro Display"', '-apple-system', 'sans-serif'],
        mono: ['"SourceCodePro"', '"SFMono-Regular"', 'monospace'],
      },
      fontWeight: {
        normal: '300',   // ⚠️ 400 아님
        bold:   '400',   // ⚠️ 700 아님
      },
      spacing: {
        '0.25': '2px', '0.5': '4px', '0.75': '6px', '1': '8px',
        '1.5': '12px', '2': '16px', '2.5': '20px', '3': '24px',
        '3.5': '28px', '4': '32px', '4.5': '36px', '5': '40px',
        '5.5': '44px', '6': '48px', '7': '56px', '8': '64px',
        '9': '72px', '10': '80px', '11': '88px', '12': '96px',
      },
      borderRadius: {
        xs: '2px', sm: '4px', md: '6px', lg: '16px', xl: '32px',
      },
      boxShadow: {
        sm: '0 5px 14px 0 rgb(0 0 0 / 0.1), 0 2px 8px 0 rgb(0 0 0 / 0.06)',
        md: '0 6px 22px 0 rgb(0 0 0 / 0.1), 0 4px 8px 0 rgb(0 0 0 / 0.06)',
        lg: '0 15px 40px -2px rgb(0 0 0 / 0.1), 0 5px 20px -2px rgb(0 0 0 / 0.06)',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- `#533AFD` 를 canonical 보라로. Stripe 로고와 primary CTA 에 쓰이는 유일한 보라다.
- 본문을 `font-weight: 300` 으로. 네, 삼백이다. 이게 Stripe 타이포그래피의 정체성.
- 헤딩 weight 도 `300` (단 `heading-xxs` / `heading-xs` 는 overline 이라 `400`)
- `sohne-var` + `SF Pro Display` → `-apple-system` fallback 체인 사용
- 큰 heading 에 negative letter-spacing: `md~xl` = `-0.01em`, `xxl` = `-0.02em`
- 4px / 8px spacing 리듬 (`space-core-50`, `space-core-100` 기반)
- 카드/모달은 **듀얼 섀도 원자** 로 (위/아래 2 layer 겹치기)
- 마케팅 page bg 는 `#F8FAFD` (순백 아님, 살짝 푸른 쿨 톤)
- 다크 섹션은 `#061B31` (`neutral-990`) — 순수 `#000` 아님
- 컴포넌트 스타일링 시 core 토큰보다 `util-*` / `action-*` alias 우선 사용

### ❌ DON'T
- `font-weight: 400` 으로 본문 두지 마라 — 너무 두꺼워 보인다
- `font-weight: 700` 으로 bold 두지 마라 — Stripe bold 는 400
- 카드에 단층 `box-shadow` 쓰지 마라 — 깊이가 무너진다
- 일반 `Inter` 로 `sohne-var` 를 대체하지 마라 — 글자 형태가 눈에 띄게 다르다
- `JetBrains Mono` 나 `Fira Code` 쓰지 마라 — Stripe 코드는 `SourceCodePro`
- 순백 `#FFFFFF` 를 page bg 로 두지 마라 — 살짝 푸른 `#F8FAFD` 가 정답
- Primary 버튼을 다크 테마에서도 `brand-600` 으로 하드코딩하지 마라 — `util-brand-*` alias 가 이미 `brandDark-*` 로 invert 해서 라이트 luminance 로 잡아 준다
- 큰 headings 에 letter-spacing 을 그대로 두지 마라 — optical compensation 없으면 "풀어진" 느낌이 난다
