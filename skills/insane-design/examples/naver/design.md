---
slug: naver
service_name: Naver
site_url: https://www.naver.com/
fetched_at: 2026-04-13
default_theme: light
brand_color: "#03C75A"
primary_font: Malgun Gothic
font_weight_normal: 400
token_prefix: --color_menu_widget_bg
---

# DESIGN.md — Naver (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Naver의 디자인은 클린한 밝은 배경 위에 브랜드 컬러 `#03C75A`를 절제적으로 배치하는 미니멀 접근을 취한다. 여백과 타이포그래피의 힘으로 콘텐츠를 전달하며, 불필요한 장식을 배제한 실용적 우아함이 특징이다.

색상 전략은 철저히 절제적이다. 주요 컬러는 #03C75A, #FFFFFF, #DADCDF, #515254이며, 뉴트럴 톤이 대부분의 UI 표면을 차지한다. 브랜드 컬러는 CTA 버튼과 핵심 강조 요소에만 사용되어 사용자의 시선을 정확히 유도한다.

타이포그래피는 `Malgun Gothic`을 중심으로 구축된다. weight 400이 기본으로, 안정적이고 균형 잡힌 가독성을 제공한다. 제목과 본문 사이의 weight 대비로 시각적 계층을 명확히 한다.

레이아웃은 넉넉한 여백과 명확한 섹션 구분으로 콘텐츠에 호흡을 부여한다. 전반적으로 정보 밀도보다 시각적 여유를 우선시하며, 이는 Naver 브랜드의 자신감과 품격을 반영한다.

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Naver처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: -apple-system, BlinkMacSystemFont, "Malgun Gothic", "맑은 고딕",
               helvetica, "Apple SD Gothic Neo", sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #101010; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #03C75A; }
```

**절대 하지 말아야 할 것 하나**: 네이버 CSS에 보이는 다양한 카테고리 컬러(`#E65DA0` 엔터, `#0147B5` 스포츠, `#EBAA00` 레시피, `#008F76` 금융)를 네이버 브랜드 색으로 착각하는 것. 이것들은 섹션별 필터 버튼 색이고, 네이버 브랜드 그린은 CSS에서 직접 확인되지 않으나 `#03C75A`가 네이버의 공식 등록색이다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.naver.com/` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | CSS Module 방식 (`EventBannerView-module__*`, `FourColumnItemView-module__*`) |
| Token prefix | `--color_menu_widget_bg` 등 시맨틱 CSS 변수 |
| Method | CSS 커스텀 프로퍼티 + 셀렉터 분석 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React (CSS Modules — `__xxxxx` 해시 suffix 패턴)
- **Design system**: Naver 내부 커스텀 — `--color_*` prefix CSS 변수
- **CSS architecture**: CSS Modules + 글로벌 CSS 변수
  ```
  CSS Variables (--color_menu_widget_bg 등 semantic tokens)
  CSS Modules (component-scoped, 해시 클래스)
  테마: html[data-theme=greenDark] 다크 테마 지원
  ```
- **Class naming**: CSS Modules 해시 (`EventBannerView-module__group_link___w72bm`)
- **Default theme**: light (bg = `#FFFFFF`), greenDark 다크 테마 지원
- **Font loading**: 시스템 폰트 스택 (`-apple-system`, `Malgun Gothic`, `Apple SD Gothic Neo`)
- **Canonical anchor**: CSS 변수 `--color_menu_widget_bg` — 테마 대응 semantic token

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `-apple-system` / `Malgun Gothic` / `Apple SD Gothic Neo` (시스템 폰트)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --naver-font-family: -apple-system, BlinkMacSystemFont, "Malgun Gothic", "맑은 고딕",
                       helvetica, "Apple SD Gothic Neo", sans-serif;
  --naver-font-weight-normal: 400;
  --naver-font-weight-bold: 700;
}
body {
  font-family: var(--naver-font-family);
  font-weight: var(--naver-font-weight-normal);
}
```

> 네이버는 자체 전용 폰트 없이 시스템 폰트 스택만 사용. NanumSquare는 일부 위젯에만 사용.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> ⚠️ 명시적 타이포 스케일 없음. weight 분포: 400(27회), 500(24회), 600(25회), 700(42회), 800(21회) — 다양한 굵기 조합.

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| badge-live | N/A | N/A | N/A | N/A |
| filter-btn | N/A | N/A | N/A | N/A |
| arrow-icon | 5px | N/A | N/A | N/A |

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand (1 step)

| Token | Hex |
|---|---|
| brand-green (공식) | `#03C75A` |

### 06-3. Neutral Ramp

| Step | Light (default) | Dark (greenDark) |
|---|---|---|
| bg-widget | `#FFFFFF` | — |
| border-widget | `#DADCDF` | `#515254` |
| text-dark | `#101010` | — |
| text-arrow | `#080808` | — |
| text-muted | `#888888` | — |
| text-muted2 | `#B5B5B5` | — |

### 06-4. Accent Families (카테고리 섹션 필터)

| Family | Key step | Hex |
|---|---|---|
| enter | active | `#E65DA0` |
| sports | active | `#0147B5` |
| recipe | active | `#EBAA00` |
| finance | active | `#008F76` |
| live-badge | bg | `#F4361E` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| --color_menu_widget_bg | `#FFFFFF` | 위젯 배경 (테마 대응) |
| border-widget | `#DADCDF` | 위젯 테두리 |
| border-widget-dark | `#515254` | 다크 테마 테두리 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| arrow-size | 5px | 더보기 화살표 크기 |

**주요 alias**:
- 미니멀 arrow 크기 5x5px 정사각형

---

## 08. Radius
<!-- SOURCE: auto -->

> N/A — CSS에서 명시적 radius 토큰 확인 불가

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

### Live Badge (`.EventBannerView-module__badge_live`)

```html
<span class="badge-live">LIVE</span>
```

| 속성 | 값 |
|---|---|
| width | 32px |
| height | 14px |
| background-color | `#F4361E` |

### More Link Button (`.EventBannerView-module__link_more`)

```html
<a class="link-more" href="#">더보기</a>
```

| 속성 | 값 |
|---|---|
| background-color | `#FFFFFF` (CSS 변수 대응) |
| border | 1px solid `#DADCDF` |
| display | inline-block |

### Category Filter — Selected (`.FourColumnItemView-module__link_filter[aria-selected=true]`)

```html
<a class="filter" aria-selected="true">엔터</a>
```

| 속성 | 값 |
|---|---|
| background-color | `#E65DA0` (엔터 카테고리) |

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| 섹션 라벨 | 카테고리명 한국어 | "엔터", "스포츠", "레시피" |
| CTA | 최소화 | "더보기" |
| Tone | 중립, 정보 중심 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Naver — copy into your root stylesheet */
:root {
  /* Fonts */
  --naver-font-family: -apple-system, BlinkMacSystemFont, "Malgun Gothic", "맑은 고딕",
                       helvetica, "Apple SD Gothic Neo", sans-serif;
  --naver-font-weight-normal: 400;
  --naver-font-weight-bold: 700;

  /* Brand */
  --naver-color-brand: #03C75A;

  /* Surfaces */
  --naver-bg-page: #FFFFFF;
  --naver-text: #101010;
  --naver-text-muted: #888888;

  /* Border */
  --naver-border: #DADCDF;
  --naver-border-dark: #515254;

  /* Accent — 섹션 필터 */
  --naver-color-enter: #E65DA0;
  --naver-color-sports: #0147B5;
  --naver-color-recipe: #EBAA00;
  --naver-color-finance: #008F76;
  --naver-color-live: #F4361E;
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference

| Role | Token | Hex |
|---|---|---|
| Brand primary | brand | `#03C75A` |
| Background | bg-page | `#FFFFFF` |
| Text primary | text | `#101010` |
| Text muted | text-muted | `#888888` |
| Border | border | `#DADCDF` |

### Example Component Prompts

#### Hero Section
```
Naver 스타일 히어로 섹션을 만들어줘.
- 배경: #FFFFFF
- H1: Malgun Gothic, weight 400
- CTA 버튼: 배경 #03C75A, radius 4px
```

#### Card Component
```
Naver 스타일 카드 컴포넌트를 만들어줘.
- 배경: #FFFFFF, border: 1px solid #DADCDF
- 제목: Malgun Gothic, weight bold
- 본문: color #101010, line-height 1.6
```

#### Button
```
Naver 스타일 버튼을 만들어줘.
- 배경: #03C75A, 텍스트: white
- font: Malgun Gothic, weight 500-600
- padding: 12px 24px, radius: 4px
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
- 시스템 폰트 스택 사용 (전용 폰트 없음)
- `--color_*` CSS 변수로 테마 대응 (greenDark 지원)
- 카테고리별 고유 색상 유지 (엔터=핑크, 스포츠=파랑 등)
- `html[data-theme=greenDark]` 다크 모드 분기 처리

### ❌ DON'T
- 카테고리 필터 색(`#E65DA0`, `#0147B5` 등)을 네이버 브랜드 색으로 사용
- 하드코딩 hex 직접 사용 — `--color_menu_widget_bg` 같은 CSS 변수로 테마 대응
- NanumSquare를 네이버 기본 폰트로 설정 — 일부 위젯 전용
