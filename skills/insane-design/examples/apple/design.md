---
slug: apple
service_name: Apple
site_url: https://apple.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#0071E3"
primary_font: SF Pro Text
font_weight_normal: 400
token_prefix: --sk-*
---

# DESIGN.md — Apple (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Apple의 웹사이트는 살짝 회색빛이 도는 오프화이트 `#F5F5F7` 배경으로 고급스러운 공기감을 연출한다. 넓은 여백과 대형 제품 이미지, 감성적이고 간결한 카피가 어우러져 프리미엄하면서도 접근 가능한 인상을 전달한다.

타이포그래피는 Apple 전용 `SF Pro Display`(디스플레이)와 `SF Pro Text`(본문)를 사용한다. 본문 weight는 **400**, 헤딩은 **600**이며, 큰 헤딩에는 `-0.02em`의 타이트한 letter-spacing이 적용되어 Apple 특유의 밀도 있는 제목 느낌을 만든다.

브랜드 블루 `#0071E3`는 CTA 버튼, focus ring, 링크에 일관되게 적용된다. hover(`#0076DF`) → active(`#006EDB`)의 정확한 3단계 상태 변화가 인터랙션의 정교함을 보여준다. 다크 배경에서는 링크가 `#2997FF`로 전환된다.

**Key Characteristics:**
- 페이지 배경은 `#F5F5F7`을 써라 — 순백이 아닌 Apple의 시그니처 오프화이트다.
- 텍스트는 `#1D1D1F`를 써라 — 순흑이 아닌 따뜻한 다크다.
- CTA 버튼은 `#0071E3`으로 시작하고, hover는 `#0076DF`, active는 `#006EDB`로 정확히 3단계를 유지하라.
- focus ring 색도 `#0071E3`으로 일치시켜라 — SkinKit 원칙이다.
- 큰 heading에 `letter-spacing: -0.02em`을 적용하라.
---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Apple처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "SF Pro Text", "SF Pro Icons", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #F5F5F7; --fg: #1D1D1F; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #0071E3; }
```

**절대 하지 말아야 할 것 하나**: 배경을 순백(`#FFFFFF`)으로 두는 것. Apple의 페이지 배경은 살짝 회색빛이 도는 `#F5F5F7`이다. 순백으로 두면 Apple 특유의 고급스러운 공기감이 사라진다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://apple.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 서버 렌더링 (Apple 자체 빌드) |
| CSS files | 셀프 호스트 SF Pro 시리즈 + 국제화 변형 폰트 다수 |
| Token prefix | `--sk-*` (SkinKit) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Apple 자체 마케팅 SSR
- **Design system**: SkinKit — prefix `--sk-*`
- **CSS architecture**: 2-tier
  ```
  core    (--sk-focus-color, --sk-button-background)  raw hex
  comp    (--localnav-focus-color, --sk-button-color-hover)
  ```
- **Class naming**: BEM-ish (`ac-globalfooter`, `ac-localnav`, `ac-ln-button`)
- **Default theme**: light (bg = `#F5F5F7`)
- **Font loading**: 셀프 호스트 SF Pro 시리즈 (Text / Display / KR / JP / HK / TH / AR 등 언어별 12종)
- **Canonical anchor**: `#0071E3` — focus ring, CTA button background 전부 이 색

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `SF Pro Display` (Apple 전용, 재배포 불가)
- **Body font**: `SF Pro Text` (Apple 전용)
- **Code font**: N/A (Apple 마케팅 사이트에 코드 폰트 없음)
- **Weight normal / bold**: `400` / `600`

```css
:root {
  --font-family-text: "SF Pro Text", "SF Pro Icons", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-family-display: "SF Pro Display", "SF Pro Icons", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold: 600;
}
body {
  font-family: var(--font-family-text);
  font-weight: var(--font-weight-normal);
}
```

> **라이선스 주의**: SF Pro는 Apple 기기에만 번들됨. 재배포 불가. 비Apple 환경에서는 `-apple-system, BlinkMacSystemFont` fallback이 동일 폰트를 로드한다.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| body-sm | 0.875rem | 400 | 1.4 | 0 |
| body | 1rem | 400 | 1.5 | 0 |
| heading-sm | 1.125rem | 600 | 1.3 | -0.01em |
| heading-md | 1.5rem | 600 | 1.2 | -0.01em |
| heading-lg | 2rem | 600 | 1.1 | -0.02em |
| hero | 3.5rem | 600 | 1.08 | -0.02em |

> ⚠️ Apple heading에는 negative letter-spacing이 적용된다. `-0.01em`(소형) ~ `-0.02em`(대형). 이 미세 조정이 없으면 Apple 특유의 타이트한 제목 느낌이 나지 않는다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (블루 계열)

| Token | Hex |
|---|---|
| `--sk-button-background-hover` | `#0076DF` |
| primary | `#0071E3` ⭐ **canonical** |
| `--sk-button-background-active` | `#006EDB` |
| dark-link | `#2997FF` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| bg | `#F5F5F7` | `#1D1D1F` |
| nav btn bg | `#1D1D1F` | `#FFFFFF` |
| hover | `#272729` | N/A |
| active | `#18181A` | `#EDEDF2` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--sk-focus-color` | `#0071E3` | focus ring 기본 |
| `--sk-button-background` | `#0071E3` | primary 버튼 배경 |
| `--sk-button-background-hover` | `#0076DF` | hover 상태 |
| `--sk-button-background-active` | `#006EDB` | active 상태 |
| dark-link | `#2997FF` | 다크 배경에서 링크 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| focus-offset | 1px | focus ring 오프셋 |
| btn-focus-offset | 3px | 버튼 컨테이너 focus |

**주요 alias**:
- `--sk-focus-offset` → 1px (전체 focus ring 오프셋)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| btn | 980px | CTA 버튼 (pill shape) |
| card | 18px | 제품 카드 |
| tag | 4px | 소형 배지 |

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Breakpoint | Width | Key Changes |
|---|---|---|
| Mobile | <640px | 단일 컬럼, 헤딩 축소, 카드 스택 |
| Tablet | 640-1024px | 2열 그리드, 중간 패딩 |
| Desktop | 1024-1280px | 풀 레이아웃, 3열 그리드 |
| Large | >1280px | 중앙 정렬 max-width 1200px, 넉넉한 마진 |

> ⚠️ Apple는 모바일 퍼스트 반응형 디자인을 채택하며, 브레이크포인트별로 그리드와 타이포그래피가 유동적으로 조정된다.

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Button — Primary CTA (Pill)

```html
<a class="ac-ln-button" href="#" role="button">
  지금 구입하기
</a>
```

| Spec | Value |
|---|---|
| `--sk-button-background` | `#0071E3` |
| `--sk-button-color` | `#FFFFFF` |
| `--sk-button-background-hover` | `#0076DF` |
| `--sk-button-background-active` | `#006EDB` |
| border-radius | ~980px (pill) |

### Nav Button — Neutral (Dark)

```html
<a class="ac-ln-button-neutral" href="#" role="button">
  더 알아보기
</a>
```

| Spec | Value |
|---|---|
| background | `#1D1D1F` |
| color | `#FFFFFF` |
| hover bg | `#272729` |

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 간결·감성적. 마침표 없음 | "당신의 삶을 바꿀 iPhone." |
| Primary CTA | 직접적 동사형 | "지금 구입하기" |
| Secondary CTA | 정보 유도형 | "더 알아보기 >" |
| Tone | 친근하지만 프리미엄. 기술 용어는 최소화 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Apple — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: "SF Pro Text", "SF Pro Icons", -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
  --font-family-display: "SF Pro Display", "SF Pro Icons", -apple-system, sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold: 600;

  /* Brand (anchor + steps) */
  --brand-active: #006EDB;
  --brand-500: #0071E3;   /* ← canonical */
  --brand-hover: #0076DF;
  --brand-dark: #2997FF;

  /* Surfaces */
  --bg-page: #F5F5F7;
  --bg-dark: #1D1D1F;
  --text: #1D1D1F;
  --text-muted: #6E6E73;

  /* Key spacing */
  --space-sm: 8px;
  --space-md: 20px;
  --space-lg: 52px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 18px;
  --radius-pill: 980px;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference
| Role | Hex |
|---|---|
| Primary CTA | `#0071E3` |
| Heading text | `#1D1D1F` |
| Body text | `#1D1D1F` |
| Background | `#F5F5F7` |
| Border | `#D2D2D7` |
| Link | `#0071E3` |
| Dark section | `#1D1D1F` |

### Example Component Prompts
- "Create a hero section on `#F5F5F7` background. Headline at 3.5rem `SF Pro Text` weight 400. CTA button `#0071E3` with white text."
- "Design a card: `#FFFFFF` background, `#D2D2D7` border, 18px radius. Body text `#1D1D1F` at weight 400."

### Iteration Guide
1. 폰트: `SF Pro Text` 패밀리, 본문 weight 400
2. 컬러: 브랜드 `#0071E3`는 CTA/링크에만 집중. 배경 `#F5F5F7`, 텍스트 `#1D1D1F`
3. 그림자: 최소한의 그림자 — 배경색 대비와 카드 분리로 elevation 표현
---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### DO
- 페이지 배경은 `#F5F5F7`을 써라 — 순백이 아닌 Apple의 시그니처 오프화이트다.
- 텍스트는 `#1D1D1F`를 써라 — 순흑이 아닌 따뜻한 다크다.
- CTA 버튼은 `#0071E3`으로 시작하고, hover는 `#0076DF`, active는 `#006EDB`로 정확히 3단계를 유지하라.
- focus ring 색도 `#0071E3`으로 일치시켜라 — SkinKit 원칙이다.
- 큰 heading에 `letter-spacing: -0.02em`을 적용하라.

### DON'T
- 배경을 `#FFFFFF`로 두지 마라 — Apple의 배경은 `#F5F5F7`이다.
- CTA 버튼을 정사각형으로 만들지 마라 — Apple은 pill shape(border-radius 980px)이다.
- SF Pro를 재배포하지 마라 — 라이선스 위반이다. 대신 `-apple-system, BlinkMacSystemFont`를 쓰라.
- 다크 배경 링크에 `#0071E3`을 그대로 쓰지 마라 — 다크 테마에서는 `#2997FF`로 교체해야 한다.
- heading에 `font-weight: 400`을 쓰지 마라 — Apple heading은 600이다.

---

