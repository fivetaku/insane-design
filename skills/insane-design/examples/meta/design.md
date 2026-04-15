---
slug: meta
service_name: Meta
site_url: https://meta.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#0866FF"
primary_font: Optimistic Display
font_weight_normal: 400
token_prefix: --primary-button-*
---

# DESIGN.md — Meta (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Meta의 디자인은 클린한 밝은 배경 위에 브랜드 컬러 `#0866FF`를 절제적으로 배치하는 미니멀 접근을 취한다. 여백과 타이포그래피의 힘으로 콘텐츠를 전달하며, 불필요한 장식을 배제한 실용적 우아함이 특징이다.

색상 전략은 철저히 절제적이다. 주요 컬러는 #0866FF, #4267B2, #0095F6, #283943이며, 뉴트럴 톤이 대부분의 UI 표면을 차지한다. 브랜드 컬러는 CTA 버튼과 핵심 강조 요소에만 사용되어 사용자의 시선을 정확히 유도한다.

타이포그래피는 `Optimistic Display`을 중심으로 구축된다. weight 400이 기본으로, 안정적이고 균형 잡힌 가독성을 제공한다. 제목과 본문 사이의 weight 대비로 시각적 계층을 명확히 한다.

레이아웃은 넉넉한 여백과 명확한 섹션 구분으로 콘텐츠에 호흡을 부여한다. 전반적으로 정보 밀도보다 시각적 여유를 우선시하며, 이는 Meta 브랜드의 자신감과 품격을 반영한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Meta처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Optimistic Text", Montserrat, Helvetica, Arial, Noto Sans, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #1C1E21; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #0866FF; }
```

**절대 하지 말아야 할 것 하나**: 브랜드 블루로 `#1877F2`(구 Facebook 파랑)를 쓰는 것. Meta 리브랜딩 이후 CTA 버튼 공식 색은 `#0866FF`로 바뀌었다. `#1877F2`를 쓰면 즉시 "아직도 Facebook 시대" 느낌이 난다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://meta.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | 서버 렌더링 (React) |
| CSS files | 인라인 + 외부 CSS (Optimistic 폰트) |
| Token prefix | `--primary-button-*` |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React (Meta 자체 빌드 시스템)
- **Design system**: 자체 커스텀 (Optimistic 폰트 시스템)
- **CSS architecture**: 플랫 CSS 변수 + 클래스 스타일
  ```
  vars  (--primary-button-background, --primary-button-text)
  class (Optimistic Display/Text 폰트 클래스)
  ```
- **Class naming**: 해시 기반 (`.inputbutton`, `.uiHeaderNav`, `._rz3`)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: Optimistic 폰트 시리즈 셀프 호스트 (Display, Text, VF, Bold 등 다수)
- **Canonical anchor**: `#0866FF` — `--primary-button-background`에서 확인

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Optimistic Display` (Meta 전용)
- **Body font**: `Optimistic Text` (Meta 전용)
- **Variable font**: `Optimistic VF` (가변 폰트)
- **Code font**: `Menlo, Consolas, Monaco, monospace`
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-family: "Optimistic Text", Montserrat, Helvetica, Arial, "Noto Sans", sans-serif;
  --font-family-display: "Optimistic Display", Montserrat, Helvetica, Arial, "Noto Sans", sans-serif;
  --font-family-code: Menlo, Consolas, Monaco, monospace;
  --font-weight-normal: 400;
  --font-weight-bold: 700;
}
body {
  font-family: var(--font-family);
  font-weight: var(--font-weight-normal);
}
```

> **참고**: Optimistic 폰트는 메타 전용이라 재배포 불가. `Montserrat`(오픈소스)가 가장 가까운 대체재.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| caption | 0.75rem | 400 | 1.33 | 0 |
| body-sm | 0.875rem | 400 | 1.43 | 0 |
| body | 1rem | 400 | 1.5 | 0 |
| title-sm | 1.25rem | 700 | 1.3 | -0.005em |
| title | 1.5rem | 700 | 1.25 | -0.01em |
| headline | 2rem | 700 | 1.2 | -0.015em |
| display | 3rem | 700 | 1.13 | -0.02em |

> ⚠️ Meta 마케팅 사이트 heading은 모두 `font-weight: 700`. 본문만 400이고 제목 계열은 굵다.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (Meta Blue)

| Token | Hex |
|---|---|
| btn-bg (현재) | `#0866FF` ⭐ **canonical** |
| btn-bg (legacy) | `#4267B2` |
| btn-bg (Instagram) | `#0095F6` |
| dark-text | `#283943` |

### 06-3. Neutral Ramp

| Step | Hex |
|---|---|
| bg | `#FFFFFF` |
| bg-secondary | `#F5F6F7` |
| border | `#CCD0D5` |
| border-str | `#DADDE1` |
| fg | `#1C1E21` |
| fg-muted | `#7F7F7F` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--primary-button-background` | `#0866FF` | primary CTA 버튼 배경 |
| `--primary-button-text` | `#FFFFFF` | primary CTA 텍스트 |
| legacy-btn | `#4267B2` | 구 Facebook 버튼 (일부 잔존) |
| instagram-btn | `#0095F6` | Instagram 연동 버튼 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | high | 배경, 버튼 텍스트 |
| 2 | `#F5F6F7` | medium | 보조 배경 |
| 3 | `#CCD0D5` | medium | 테두리 |
| 4 | `#4267B2` | low | 레거시 버튼 |
| 5 | `#0095F6` | low | Instagram CTA |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| nav-margin | 8px 0 0 6px | 헤더 nav 마진 |
| nav-padding | 7px 6px 3px 5px | 헤더 nav 패딩 |

**주요 alias**:
- 기본 여백 → 8px 배수 (Meta 내부 grid)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| btn | 6px | 일반 버튼 |
| card | 8px | 콘텐츠 카드 |
| pill | 999px | 배지, 태그 |

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

### Button — Primary

```html
<button class="btn-primary" style="--primary-button-background:#0866FF;--primary-button-text:#FFFFFF;" type="button">
  시작하기
</button>
```

| Spec | Value |
|---|---|
| `--primary-button-background` | `#0866FF` |
| `--primary-button-text` | `#FFFFFF` |
| font-weight | 700 |
| border-radius | 6px |

### Legacy Form Button

```html
<input class="inputbutton" type="submit" value="로그인">
```

| Spec | Value |
|---|---|
| background | `#4267B2` |
| color | `#FFFFFF` |
| padding | `2px 15px 3px` |

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 사람 중심, 연결 강조 | "Give everyone the power to build community" |
| Primary CTA | 동사형, 간결 | "Get started" |
| Tone | 포용적, 따뜻함. 기술 용어 최소화 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Meta — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: "Optimistic Text", Montserrat, Helvetica, Arial, "Noto Sans", sans-serif;
  --font-family-display: "Optimistic Display", Montserrat, Helvetica, Arial, sans-serif;
  --font-weight-normal: 400;
  --font-weight-bold: 700;

  /* Brand */
  --brand: #0866FF;   /* ← canonical (2023 Meta blue) */
  --brand-legacy: #4267B2;
  --brand-instagram: #0095F6;

  /* Surfaces */
  --bg-page: #FFFFFF;
  --bg-secondary: #F5F6F7;
  --text: #1C1E21;
  --text-muted: #7F7F7F;

  /* Key spacing */
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 32px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-pill: 999px;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#0866FF` |
| Background | bg-page | `#FFFFFF` |
| Text primary | text | `#1C1E21` |
| Text muted | text-muted | `#7F7F7F` |
| Border | border | `#CCD0D5` |

### Example Component Prompts

#### Hero Section
```
Meta 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: Optimistic Display, weight 400
- CTA 버튼: 배경 #0866FF, radius 6px
```

#### Card Component
```
Meta 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF, border: 1px solid #CCD0D5
- 제목: Optimistic Display, weight bold
- 본문: color #1C1E21, line-height 1.6
```

#### Button
```
Meta 스타일 버튼을 만들어줘.
- 배경: #0866FF, 텍스트: white
- font: Optimistic Display, weight 500-600
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

### DO
- CTA 버튼 배경은 `#0866FF`(2023 Meta blue)을 써라.
- 텍스트는 `#1C1E21`을 써라 — 순흑이 아닌 Meta의 dark gray다.
- 보조 배경에는 `#F5F6F7`을 써라.
- 큰 heading에 `font-weight: 700`을 써라.
- letter-spacing은 heading 크기에 비례해 음수값으로 미세 조정하라.

### DON'T
- `#1877F2`(구 Facebook 파랑)를 primary로 쓰지 마라 — Meta 리브랜딩 이후 `#0866FF`로 교체됐다.
- `#4267B2`를 현재 CTA에 쓰지 마라 — 레거시 폼 버튼 잔재다.
- Optimistic 폰트를 재배포하지 마라 — Meta 전용이다. Montserrat를 fallback으로 쓰라.
- 본문에 `font-weight: 700`을 쓰지 마라 — 기본은 400이다.
- 다크 테마를 기본으로 쓰지 마라 — Meta는 라이트 기반이다.
