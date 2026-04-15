---
slug: krafton
service_name: Krafton
site_url: https://www.krafton.com/
fetched_at: 2026-04-13
default_theme: dark
brand_color: "#F9423A"
primary_font: system-ui
font_weight_normal: 400
token_prefix: --wp--preset--color--primary
---

# DESIGN.md — Krafton (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Krafton의 디자인은 다크 배경 위에 구축된 몰입형 시각 경험을 추구한다. 브랜드 컬러 `#F9423A`를 절제된 포인트로 활용하며, 전반적으로 깊이감 있는 다크 톤이 서비스의 전문성과 프리미엄 감성을 전달한다.

색상 전략은 철저히 절제적이다. 주요 컬러는 #F9423A, #0073A8, #005075, #FFFFFF이며, 뉴트럴 톤이 대부분의 UI 표면을 차지한다. 브랜드 컬러는 CTA 버튼과 핵심 강조 요소에만 사용되어 사용자의 시선을 정확히 유도한다.

타이포그래피는 시스템 폰트를 전략적으로 활용한다. `font-weight: 400`을 기본으로 두어 정보 전달에 최적화된 가독성을 확보하며, 폰트 로딩 없이도 크로스 플랫폼 일관성을 유지한다.

레이아웃은 넉넉한 여백과 명확한 섹션 구분으로 콘텐츠에 호흡을 부여한다. 전반적으로 정보 밀도보다 시각적 여유를 우선시하며, 이는 Krafton 브랜드의 자신감과 품격을 반영한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Krafton처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: system-ui, -apple-system, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #000000; --fg: #FFFFFF; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #F9423A; }
```

**절대 하지 말아야 할 것 하나**: `#0073A8` (WordPress preset primary)를 Krafton 브랜드 색으로 사용하는 것. `#0073A8`은 WordPress Gutenberg의 기본 preset color이며 실제 Krafton 브랜드와 무관하다. SVG 패턴에서 7회 등장하는 `#F9423A`가 실제 Krafton 레드 브랜드 컬러다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.krafton.com/` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | WordPress (자동 생성 인라인 CSS) |
| Token prefix | `--wp--preset--color--primary` (WordPress preset) |
| Method | CSS hex frequency 분석 · 커스텀 프로퍼티 파싱 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: WordPress (블록 에디터 Gutenberg 사용)
- **Design system**: WordPress 블록 테마 + 크래프톤 커스텀
- **CSS architecture**: WordPress 자동 생성 CSS
  ```
  /*# sourceURL=wp-img-auto-sizes-contain-inline-css */
  --wp--preset--color--* (WordPress 프리셋 토큰)
  .wp-block-button__link (Gutenberg 블록 버튼)
  .wp-block-file__button (파일 다운로드 버튼)
  ```
- **Class naming**: WordPress 블록 (`wp-block-button__link`, `wp-block-file__button`)
- **Default theme**: dark (bg = `#000000`)
- **Font loading**: 시스템 폰트 (전용 폰트 CSS 미확인)
- **Canonical anchor**: `#F9423A` — Krafton 레드, SVG 패턴 7회 등장

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: 시스템 폰트 (CSS에서 전용 폰트 미확인)
- **Code font**: N/A
- **Weight normal / bold**: `400` / N/A

```css
:root {
  --krafton-font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --krafton-font-weight-normal: 400;
}
body {
  font-family: var(--krafton-font-family);
  font-weight: var(--krafton-font-weight-normal);
}
```

> CSS 번들에서 전용 폰트 패밀리 미확인. WordPress 테마 기본 시스템 폰트 사용 추정.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> ⚠️ CSS에서 타이포 스케일 토큰 확인 불가. WordPress 기본값 사용.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| body | N/A | 400 | N/A | N/A |

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| brand-red | `#F9423A` |
| brand-teal | `#0073A8` |
| brand-teal-dark | `#005075` |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| white | `#FFFFFF` | — |
| black | `#000000` | — |
| near-black | `#111111` | — |
| dark-btn | `#32373C` | — |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| wp-green | preset | `#00D084` |
| wp-blue | preset | `#0693E3` |
| wp-purple | preset | `#9B51E0` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| --wp--preset--color--primary | `#0073A8` | WordPress 프리셋 (브랜드 아님) |
| brand-red | `#F9423A` | Krafton 브랜드 레드 |
| btn-default-bg | `#32373C` | WordPress 기본 버튼 배경 |
| btn-default-color | `#FFFFFF` | WordPress 기본 버튼 텍스트 |

---

## 07. Spacing
<!-- SOURCE: auto -->

> N/A — CSS에서 스페이싱 토큰 확인 불가

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| wp-block-button | 9999px | Gutenberg 버튼 기본 (pill shape) |

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

### Block Button (`.wp-block-button__link`)

```html
<div class="wp-block-button">
  <a class="wp-block-button__link">게임 보기</a>
</div>
```

| 속성 | 값 |
|---|---|
| color | `#FFFFFF` |
| background-color | `#32373C` |
| border-radius | 9999px |
| box-shadow | none |
| text-decoration | none |

### File Download Button (`.wp-block-file__button`)

```html
<a class="wp-block-file__button" href="#">다운로드</a>
```

| 속성 | 값 |
|---|---|
| background | `#32373C` |
| color | `#FFFFFF` |
| text-decoration | none |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Krafton — copy into your root stylesheet */
:root {
  /* Fonts */
  --krafton-font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  --krafton-font-weight-normal: 400;

  /* Brand */
  --krafton-color-brand: #F9423A;
  --krafton-color-teal: #0073A8;
  --krafton-color-teal-dark: #005075;

  /* Surfaces */
  --krafton-bg-page: #000000;
  --krafton-text: #FFFFFF;

  /* Button */
  --krafton-btn-bg: #32373C;
  --krafton-btn-radius: 9999px;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#F9423A` |
| Background | bg-page | `#000000` |
| Text primary | text | `#FFFFFF` |
| Text muted | text-muted | `#666666` |
| Border | border | `#E0E0E0` |

### Example Component Prompts

#### Hero Section
```
Krafton 스타일 히어로 섹션을 만들어줘.
- 배경: #000000
- H1: system-ui, weight 400
- CTA 버튼: 배경 #F9423A, radius 9999px
```

#### Card Component
```
Krafton 스타일 카드 컴포넌트를 만들어줘.
- 배경: #000000, border: 1px solid #E0E0E0
- 제목: system-ui, weight bold
- 본문: color #FFFFFF, line-height 1.6
```

#### Button
```
Krafton 스타일 버튼을 만들어줘.
- 배경: #F9423A, 텍스트: white
- font: system-ui, weight 500-600
- padding: 12px 24px, radius: 9999px
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
- 배경은 `#000000` 순수 검정 (다크 테마가 기본)
- Krafton 브랜드 레드는 `#F9423A`
- WordPress 블록 버튼은 pill shape (border-radius: 9999px)
- 텍스트는 `#FFFFFF` 순수 흰색

### ❌ DON'T
- `#0073A8`을 Krafton 브랜드 색으로 사용 — WordPress 프리셋 기본값
- `#32373C` 버튼 배경을 Krafton 브랜드 색으로 혼동 — WordPress 기본 버튼색
- 라이트 테마 기본으로 설정 — Krafton 웹은 다크 테마가 기본
