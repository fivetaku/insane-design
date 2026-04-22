---
slug: tesla
service_name: Tesla
site_url: https://tesla.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#CC0000"
primary_font: N/A
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Tesla (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Tesla처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: "Gotham SSm A", "Gotham SSm B", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #F4F4F4; --fg: #000000; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #CC0000; }
```

**절대 하지 말아야 할 것 하나**: 배경을 순백 `#FFFFFF`로 두는 것. Tesla의 마케팅 사이트 배경은 `#F4F4F4`(밝은 회색)이고 차량 사진이 hero를 채운다. 순백 배경은 즉시 "일반 전자상거래" 느낌을 준다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://tesla.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | 인라인 중심 (토큰 시스템 미확인) |
| Token prefix | N/A — 커스텀 프로퍼티 시스템 미감지 |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: React (Next.js 추정)
- **Design system**: 자체 내부 디자인 시스템 (토큰 prefix 미공개)
- **CSS architecture**: 인라인 스타일 + 최소 글로벌 CSS
- **Class naming**: N/A
- **Default theme**: light (bg = `#F4F4F4`)
- **Font loading**: N/A (CSS에서 font-family 미감지)
- **Canonical anchor**: `#CC0000` — 유일한 chromatic 후보

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: N/A (CSS에서 감지되지 않음)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

> **참고**: Tesla 마케팅 사이트의 CSS에서 font-family가 감지되지 않았다. 시각적으로는 Gotham SSm 계열로 관찰되나 CSS 파싱 데이터 기반으로 확인 불가.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

> N/A — CSS에서 typography scale 토큰이 추출되지 않음.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp

| Token | Hex |
|---|---|
| 브랜드 레드 (chromatic 유일) | `#CC0000` |

### 06-3. Neutral Ramp

| Step | Hex | Count |
|---|---|---|
| 페이지 배경 | `#F4F4F4` | 8회 |
| 텍스트 / 배경 다크 | `#000000` | 1회 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| 페이지 배경 | `#F4F4F4` | body background |
| 텍스트 / 다크 배경 | `#000000` | 텍스트, 다크 섹션 배경 |
| 브랜드 레드 | `#CC0000` | accent, 로고 |

---

## 07. Spacing
<!-- SOURCE: auto -->

> N/A — spacing 토큰이 CSS에서 추출되지 않음.

---

## 08. Radius
<!-- SOURCE: auto -->

> N/A — radius 토큰이 CSS에서 추출되지 않음.

---

## 12. Components
<!-- SOURCE: manual -->

### Hero Section

```html
<section class="hero">
  <div class="hero__media">
    <img src="vehicle.jpg" alt="Tesla Model S" />
  </div>
  <div class="hero__content">
    <h1>Model S</h1>
    <div class="hero__ctas">
      <a href="#" class="btn btn--order">주문하기</a>
      <a href="#" class="btn btn--demo">시승 신청</a>
    </div>
  </div>
</section>
```

| 속성 | 값 |
|---|---|
| 배경 | 차량 전체 폭 사진 |
| H1 색상 | `#FFFFFF` (다크 배경 위) 또는 `#000000` |
| CTA 배경 | `#000000` (주문하기) |
| CTA 색상 | `#FFFFFF` |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 모델명만, 최소한의 수식 | "Model S" |
| Primary CTA | 직접 행동, 간결 | "주문하기" |
| Secondary CTA | 체험 유도 | "시승 신청" |
| Subheading | 스펙 수치 나열 | "제로백 1.99초" |
| Tone | 미니멀, 수치 중심, 과장 없음 | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Tesla — copy into your root stylesheet */
:root {
  /* Fonts — CSS에서 미감지, 시각 관찰 기반 */
  --tesla-font-family: "Gotham SSm A", "Gotham SSm B", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --tesla-font-weight-normal: 400;
  --tesla-font-weight-bold: 700;

  /* Brand */
  --tesla-color-brand-red: #CC0000;

  /* Surfaces */
  --tesla-bg-page: #F4F4F4;
  --tesla-bg-dark: #000000;
  --tesla-text: #000000;
  --tesla-text-on-dark: #FFFFFF;
}
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 페이지 배경에 `#F4F4F4` 사용 (순백 아님)
- Hero는 차량 전체 폭 사진으로 채우기
- CTA 텍스트 최소화 ("주문하기", "시승 신청")
- H1은 모델명만, 수식어 없이
- 스펙 표현 시 실제 수치 명시 (초, km, kWh)

### ❌ DON'T
- 배경을 순백 `#FFFFFF`으로 쓰지 말 것
- 과장형 마케팅 문구 사용하지 말 것 ("혁신적인", "놀라운")
- CTA 버튼 색으로 레드 `#CC0000`을 쓰지 말 것 — 버튼은 블랙
- 레이아웃을 복잡하게 만들지 말 것 — 최대한 단순하게
