---
slug: kakaocorp
service_name: Kakao
site_url: https://www.kakaocorp.com/
fetched_at: 2026-04-13
default_theme: light
brand_color: "#FEE500"
primary_font: KakaoBig
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Kakao (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Kakao의 디자인은 클린한 밝은 배경 위에 브랜드 컬러 `#FEE500`를 절제적으로 배치하는 미니멀 접근을 취한다. 여백과 타이포그래피의 힘으로 콘텐츠를 전달하며, 불필요한 장식을 배제한 실용적 우아함이 특징이다.

색상 전략은 철저히 절제적이다. 주요 컬러는 #FEE500, #FFFFFF, #333333, #888888이며, 뉴트럴 톤이 대부분의 UI 표면을 차지한다. 브랜드 컬러는 CTA 버튼과 핵심 강조 요소에만 사용되어 사용자의 시선을 정확히 유도한다.

타이포그래피는 `KakaoBig`을 중심으로 구축된다. weight 400이 기본으로, 안정적이고 균형 잡힌 가독성을 제공한다. 제목과 본문 사이의 weight 대비로 시각적 계층을 명확히 한다.

레이아웃은 넉넉한 여백과 명확한 섹션 구분으로 콘텐츠에 호흡을 부여한다. 전반적으로 정보 밀도보다 시각적 여유를 우선시하며, 이는 Kakao 브랜드의 자신감과 품격을 반영한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Kakao처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: KakaoBig, "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #333333; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #FEE500; }
```

**절대 하지 말아야 할 것 하나**: 카카오 브랜드 노랑(`#FEE500`)을 텍스트 색으로 쓰는 것. `#FEE500`은 배경색으로만 사용하고 텍스트는 항상 검정(`#000000`)과 함께 쓴다 — 실제 CSS에서 `.btn_play` 배경이 `#FEE500`이고 color가 `#000000`임.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.kakaocorp.com/` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | Vue.js scoped CSS (data-v- 해시 포함) |
| Token prefix | N/A (Vue scoped, 리터럴 hex) |
| Method | CSS 셀렉터 역할 분석 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Vue.js (scoped CSS — `[data-v-61c8860e]` 패턴)
- **Design system**: Kakao 전용 커스텀 — `KakaoBig`, `KakaoSmall` 폰트 패밀리
- **CSS architecture**: Vue scoped 컴포넌트 CSS
  ```
  global base (body, button, input 리셋)
  scoped component (data-v-* suffix)
  ```
- **Class naming**: 시맨틱 + 기능 (`.btn_play`, `.btn_stop`, `.btn_more`, `.mo_header`)
- **Default theme**: light (bg = `#FFFFFF`, text = `#333333`)
- **Font loading**: 자체 호스팅 (KakaoBig, KakaoSmall, KakaoDigitLatin)
- **Canonical anchor**: `#FEE500` — 카카오 시그니처 노랑, 배경 전용

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `KakaoBig` (카카오 전용, 대제목용)
- **Body font**: `KakaoSmall` (카카오 전용, 본문용)
- **Digit font**: `KakaoDigitLatin` (숫자/라틴 전용)
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --kakao-font-big: KakaoBig, "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", sans-serif;
  --kakao-font-small: KakaoSmall, "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", sans-serif;
  --kakao-font-weight-normal: 400;
  --kakao-font-weight-bold: 700;
}
body {
  font-family: var(--kakao-font-small);
  font-size: 14px;
  line-height: 1.5;
  font-weight: var(--kakao-font-weight-normal);
  color: #333;
}
```

> 대제목은 KakaoBig(count:108), 본문/UI는 KakaoSmall. `kakaobi`는 아이콘 폰트.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> ⚠️ CSS 리터럴 값 기반 — 체계적 스케일 토큰 없음.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| body-base | 14px | 400 | 1.5 | N/A |
| btn_play | 16px | 400 | 1.75 | N/A |
| link-subinfo | 12px | 400 | N/A | -0.2px |

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (1 step)

| Token | Hex |
|---|---|
| brand-yellow | `#FEE500` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white | `#FFFFFF` | — |
| text-primary | `#333333` | — |
| text-secondary | `#888888` | — |
| text-tertiary | `#999999` | — |
| text-on-yellow | `#000000` | — |
| border-muted | `#EEEEEE` | — |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| btn_play-bg | `#FEE500` | 재생 버튼 배경 (카카오 노랑) |
| btn_play-color | `#000000` | 재생 버튼 텍스트 |
| btn_stop-border | `#EEEEEE` | 정지 버튼 테두리 |
| direct-link-bg | `#333333` | 스킵 링크 배경 |
| ico_outlink | `#888888` | 외부 링크 아이콘 stroke |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| btn_play-py | 9px 9px 11px | 재생 버튼 패딩 |
| btn_stop-bottom | 40px | 정지 버튼 하단 여백 |
| direct-link-px | 10px | 스킵 링크 패딩 |
| link-subinfo-ls | -0.2px | 서브 링크 자간 |

**주요 alias**:
- 버튼 패딩 비대칭: top 9px, bottom 11px (시각 보정)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| btn_play | 6px | 재생 버튼 |

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

### Breakpoints

| Name | Value | Description |
|---|---|---|
| Mobile | < 768px | 단일 컬럼, 터치 최적화 |
| Tablet | 768px–1024px | 2컬럼 그리드, 축소된 여백 |
| Desktop | 1024px–1440px | 전체 레이아웃, 다중 컬럼 |
| Large | > 1440px | max-width 고정, 좌우 auto margin |

### Touch Targets
- **Minimum tap size**: 44×44px (WCAG 2.5.5)
- **Button height (mobile)**: 48px
- **Input height (mobile)**: 48px

### Collapsing Strategy
- **Navigation**: 모바일에서 축소/햄버거 메뉴 전환
- **Grid columns**: desktop 다중 컬럼 → mobile 단일 컬럼
- **Hero layout**: 이미지+텍스트 분할 → 모바일에서 수직 스택

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Button — Play (`.btn_play`)

```html
<button class="btn_play" type="button">재생</button>
```

| 속성 | 값 |
|---|---|
| display | block |
| width | 100% |
| padding | 9px 9px 11px |
| border-radius | 6px |
| font-size | 16px |
| line-height | 1.75 |
| color | `#000000` |
| background | `#FEE500` |

### Navigation Link (`.mo_header .inner_gnb .ico_outlink`)

```html
<span class="ico_outlink"></span>
```

| 속성 | 값 |
|---|---|
| stroke | `#888888` |

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 카카오 서비스명 중심 | "카카오" |
| Primary CTA | 기능 동사 | "재생" |
| Tone | 친근하고 간결 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Kakao — copy into your root stylesheet */
:root {
  /* Fonts */
  --kakao-font-big: KakaoBig, "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", sans-serif;
  --kakao-font-small: KakaoSmall, "Apple SD Gothic Neo", "Malgun Gothic", "맑은 고딕", sans-serif;
  --kakao-font-weight-normal: 400;
  --kakao-font-weight-bold: 700;

  /* Brand */
  --kakao-color-brand: #FEE500;
  --kakao-color-brand-text: #000000;

  /* Surfaces */
  --kakao-bg-page: #FFFFFF;
  --kakao-text: #333333;
  --kakao-text-muted: #888888;

  /* Key spacing */
  --kakao-radius-btn: 6px;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#FEE500` |
| Background | bg-page | `#FFFFFF` |
| Text primary | text | `#333333` |
| Text muted | text-muted | `#EEEEEE` |
| Border | border | `#EEEEEE` |

### Example Component Prompts

#### Hero Section
```
Kakao 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: KakaoBig, weight 400
- CTA 버튼: 배경 #FEE500, radius 6px
```

#### Card Component
```
Kakao 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF, border: 1px solid #EEEEEE
- 제목: KakaoBig, weight bold
- 본문: color #333333, line-height 1.6
```

#### Button
```
Kakao 스타일 버튼을 만들어줘.
- 배경: #FEE500, 텍스트: white
- font: KakaoBig, weight 500-600
- padding: 12px 24px, radius: 6px
```

### Iteration Guide

- **색상 변경 시**: 반드시 §06의 semantic token을 사용. raw hex 직접 사용 금지.
- **폰트 변경 시**: weight 400이 기본. bold는 제목/강조에만.
- **여백 조정 시**: §07의 spacing scale 단위로만. 임의 값(13px, 27px 등) 금지.
- **새 컴포넌트 추가 시**: §13의 기존 패턴(radius, shadow, border 스타일)을 따를 것.
- **반응형**: §12의 breakpoint를 그대로 사용. 커스텀 breakpoint 추가 금지.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 카카오 노랑(`#FEE500`) 위에는 항상 검정(`#000000`) 텍스트
- 대제목은 `KakaoBig`, 본문은 `KakaoSmall` 구분 사용
- 버튼 패딩 비대칭 유지: top 9px, bottom 11px
- 아이콘 stroke 색은 `#888888` (회색)

### ❌ DON'T
- `#FEE500` 노랑을 텍스트 색으로 사용 — 배경 전용
- KakaoBig과 KakaoSmall을 하나의 font-family로 통합 — 별도 패밀리
- 카카오 UI에서 border-radius 8px 이상 — 현재 CSS 기준 6px가 최대
