---
slug: bain
service_name: Bain & Company
site_url: https://www.bain.com
fetched_at: 2026-04-13
default_theme: light
brand_color: "#CC0000"
primary_font: system-ui
font_weight_normal: 400
token_prefix: N/A
---

# DESIGN.md — Bain & Company (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Bain & Company는 전통 경영 컨설팅 firm답게 실용적 권위감의 보수적 디자인을 가진다. 순백 `#FFFFFF` 배경 위에 `#313131`(따뜻한 다크 그레이) 텍스트가 놓이고, 다크 레드 `#CC0000`이 CTA, 링크, 태그에만 절제적으로 사용된다. 시스템 폰트를 채택하여 콘텐츠 권위성에 집중한다.

Heading은 모두 weight 700이고 body는 400으로, 중간값(500, 600)이 없는 명확한 2단계 구분이다. Radius는 0~6px의 작은 값만 사용하고, shadow도 미니멀하다. "분석적, 결과 중심"의 copy voice가 디자인 톤과 일치한다.

**Key Characteristics:**
- 다크 레드 `#CC0000` (순수 빨간 `#FF0000`이 아님 — 절제된 톤)
- 시스템 폰트 의도적 사용 (콘텐츠 권위성 우선)
- Weight 400/700 2단계만 (중간값 없음)
- Radius 0~6px 보수적 사용
- CTA·링크·태그에만 red 사용 — 과도한 적용 금지

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Bain & Company처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight */
body {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-weight: 400;
}

/* 2. 배경 + 텍스트 */
:root { --bg: #FFFFFF; --fg: #313131; }
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 컬러 */
:root { --brand: #CC0000; }
```

**절대 하지 말아야 할 것 하나**: Bain red를 밝은 빨간(#FF0000)으로 쓰는 것. Bain의 브랜드 red는 심오하고 절제된 다크 레드(#CC0000)계열이다. 순수 빨간은 Bain 특유의 전문적 권위감을 해친다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://www.bain.com` |
| Fetched | 2026-04-13 |
| Extractor | curl + Chrome UA (5-tier fallback) |
| HTML size | N/A |
| CSS files | 시스템 폰트, 최소 CSS 구조 |
| Token prefix | N/A (CSS 커스텀 프로퍼티 미발견) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: N/A (콘텐츠 중심 컨설팅 사이트)
- **Design system**: Bespoke — 시스템 폰트, 최소 변수
- **CSS architecture**: Flat CSS, 시스템 폰트 중심
  ```
  core  (직접 hex 값)  텍스트·배경·브랜드 red
  comp  (selector)     버튼·헤더
  ```
- **Class naming**: 기능적 클래스 (BEM 미적용)
- **Default theme**: light (bg = `#FFFFFF`)
- **Font loading**: 시스템 폰트 전용 (외부 폰트 없음)
- **Canonical anchor**: `#CC0000` — Bain brand red

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `system-ui` (OS 기본 폰트)
- **Code font**: N/A
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  --font-weight-normal: 400;
  --font-weight-bold:   700;
}
body {
  font-family: var(--font-family);
  font-weight: var(--font-weight-normal);
}
```

> **참고**: Bain은 BCG와 달리 시스템 폰트를 채택해 모든 디바이스에서 OS 기본 폰트로 렌더링한다. 폰트 개성보다 콘텐츠 권위성에 집중한 선택.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Token | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| display | 3rem | 700 | 1.1 | -0.02em |
| heading-l | 2rem | 700 | 1.2 | -0.01em |
| heading-m | 1.5rem | 700 | 1.3 | 0 |
| heading-s | 1.125rem | 700 | 1.4 | 0 |
| body | 1rem | 400 | 1.65 | 0 |
| small | 0.875rem | 400 | 1.6 | 0 |
| caption | 0.75rem | 400 | 1.5 | 0.02em |
| label | 0.75rem | 700 | 1.4 | 0.06em |

> ⚠️ 시스템 폰트 사용으로 각 OS에서 다른 글자 모양이 렌더링된다. font-weight 400/700 두 단계만 사용.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Ramp (3 steps)

| Token | Hex |
|---|---|
| brand-dark | #8B0000 |
| brand-red | #CC0000 |
| brand-light | #FF6666 |

### 06-3. Neutral Ramp

| Step | Light | Dark |
|---|---|---|
| 0 | #FFFFFF | #313131 |
| 100 | #F5F5F5 | #3D3D3D |
| 200 | #E5E5E5 | #555555 |
| 400 | #9E9E9E | #888888 |
| 700 | #555555 | #CCCCCC |
| 900 | #2A2A2A | #F5F5F5 |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| bg-page | #FFFFFF | 페이지 배경 |
| fg-primary | #313131 | 주 텍스트 |
| fg-secondary | #555555 | 보조 텍스트 |
| border | #E5E5E5 | 구분선 |
| btn-primary-bg | #CC0000 | 주 CTA 배경 |
| btn-primary-fg | #FFFFFF | 주 CTA 텍스트 |
| link | #CC0000 | 링크 컬러 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | #313131 | 2 | 주 텍스트 |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Token | Value | Use case |
|---|---|---|
| space-xs | 4px | 미세 간격 |
| space-sm | 8px | 컴포넌트 내부 |
| space-md | 16px | 섹션 내 |
| space-lg | 32px | 섹션 간 |
| space-xl | 64px | 페이지 레벨 |
| space-xxl | 96px | 대형 영역 |

**주요 alias**:
- `space-md` → 16px (기본 패딩)

---

## 08. Radius
<!-- SOURCE: auto -->

| Token | Value | Context |
|---|---|---|
| radius-none | 0px | 카드·테이블 |
| radius-sm | 3px | 버튼 |
| radius-md | 6px | 드롭다운 |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| shadow-sm | 0 1px 3px rgba(0,0,0,0.08) | 카드 hover |
| shadow-md | 0 4px 12px rgba(0,0,0,0.10) | 드롭다운 |

---

## 11. Layout Patterns
<!-- SOURCE: manual -->

### Hero
- Layout: 전체폭, 좌측 텍스트 + 우측 이미지 또는 전체폭 배경
- Background: #FFFFFF
- H1: `3rem` / weight `700` / tracking `-0.02em`
- Max-width: 1280px

### Section Rhythm
```css
section {
  padding: 64px 40px;
  max-width: 1280px;
}
```

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Breakpoint | Width | Key Changes |
|---|---|---|
| Mobile | <640px | 단일 컬럼, 모바일 네비게이션, 터치 타겟 44px+ |
| Tablet | 640-1024px | 2컬럼 그리드, 사이드 패딩 증가 |
| Desktop | 1024-1280px | 풀 그리드 레이아웃, 확장 네비게이션 |
| Large | >1280px | max-width 컨테이너, 중앙 정렬 |

---

## 13. Components
<!-- SOURCE: auto+manual -->

### Primary Button

```html
<button class="btn btn--primary">
  Contact Us
</button>
```

| Spec | Value |
|---|---|
| background | #CC0000 |
| color | #FFFFFF |
| padding | 12px 24px |
| border-radius | 3px |
| font-weight | 700 |
| text-transform | none |

### Article Card

```html
<div class="article-card">
  <div class="article-card__image">
    <img src="article.jpg" alt="Article">
  </div>
  <div class="article-card__content">
    <span class="article-card__tag">Insights</span>
    <h3 class="article-card__title">Article Title</h3>
    <p class="article-card__excerpt">Short description...</p>
    <a href="#" class="article-card__link">Read more</a>
  </div>
</div>
```

| Spec | Value |
|---|---|
| border-radius | 0px |
| tag color | #CC0000 |
| link color | #CC0000 |
| title weight | 700 |
| excerpt weight | 400 |

---

## 14. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 분석적, 액션 중심 명사구 | "Results Delivered" |
| Primary CTA | 동사 + 목적어 | "Contact Us" |
| Secondary CTA | 소문자, 링크형 | "Read more" |
| Subheading | 분석적, 결과 중심 | |
| Tone | 실용적 권위, 결과 중심, 학구적 과잉 금지 | |

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Bain & Company — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-family-code: ui-monospace, monospace;
  --font-weight-normal: 400;
  --font-weight-bold:   700;

  /* Brand (anchor + 4 steps) */
  --color-brand-25:  #FFEEEE;
  --color-brand-300: #FF6666;
  --color-brand-500: #CC0000;
  --color-brand-600: #CC0000;   /* ← canonical */
  --color-brand-900: #8B0000;

  /* Surfaces */
  --bg-page:   #FFFFFF;
  --bg-dark:   #313131;
  --text:      #313131;
  --text-muted:#555555;

  /* Key spacing */
  --space-sm:  8px;
  --space-md:  16px;
  --space-lg:  32px;

  /* Radius */
  --radius-sm: 3px;
  --radius-md: 6px;
}
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Bain & Company
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25:  '#FFEEEE',
          300: '#FF6666',
          500: '#CC0000',
          600: '#CC0000',
          900: '#8B0000',
        },
        neutral: {
          0:   '#FFFFFF',
          100: '#F5F5F5',
          200: '#E5E5E5',
          400: '#9E9E9E',
          700: '#555555',
          900: '#2A2A2A',
        },
      },
      fontFamily: {
        sans: ['system-ui', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'sans-serif'],
        mono: ['ui-monospace', 'monospace'],
      },
      fontWeight: {
        normal: '400',
        bold:   '700',
      },
      borderRadius: {
        'none': '0px',
        'sm':   '3px',
        'md':   '6px',
      },
      boxShadow: {
        'sm': '0 1px 3px rgba(0,0,0,0.08)',
        'md': '0 4px 12px rgba(0,0,0,0.10)',
      },
    },
  },
};
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: auto+manual -->

### Quick Color Reference

| Role | Value |
|---|---|
| Brand | `#CC0000` |
| Page BG | `#FFFFFF` |
| Text Primary | `#313131` |
| Default Theme | light |

### Component Prompts

> **Hero section**: "Bain & Company 스타일 hero — `system-ui` 폰트, `#CC0000` brand color, light 배경"
>
> **CTA button**: "Bain & Company primary CTA — brand `#CC0000` 배경 또는 dark fill, `system-ui` 폰트"
>
> **Card component**: "Bain & Company 스타일 카드 — light 테마, 기존 radius/shadow 토큰 준수"

### Iteration Guide

1. **Color 교체 시**: 반드시 §06 Colors 테이블의 실제 hex 참조. AI 추론 색상 사용 금지.
2. **Typography 변경 시**: §04 Font Stack의 font-family 체인 + §05의 weight/size 매핑 확인.
3. **Spacing 조정 시**: §07 Spacing의 토큰 스케일 내에서만 변경.
4. **신규 컴포넌트**: §13 Components의 기존 패턴(radius, shadow, padding)을 기반으로 확장.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 브랜드 red는 `#CC0000`(다크 레드)을 쓴다
- primary CTA와 링크에 동일한 `#CC0000`을 사용한다
- heading은 모두 `font-weight: 700`을 적용한다
- 시스템 폰트를 그대로 사용한다 (외부 폰트 불필요)
- 텍스트는 `#313131`(따뜻한 다크 그레이)을 사용한다

### ❌ DON'T
- Bain red를 `#FF0000`(순수 빨간)으로 밝게 쓰지 않는다
- 배경에 빨간 계열 색상을 쓰지 않는다 — 포인트 전용
- `font-weight: 500` 이나 `600`을 쓰지 않는다 — 400/700만
- 과도한 red 사용으로 UI를 채우지 않는다 — CTA·링크·태그만
- `border-radius`에 큰 값(12px 이상)을 넣지 않는다
