---
slug: toss
service_name: Toss
site_url: https://toss.im
fetched_at: 2026-04-12
default_theme: light
brand_color: "#3182F6"
primary_font: Toss Product Sans
font_weight_normal: 500
token_prefix: --adaptive*
---

# DESIGN.md — Toss (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Toss처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 + weight 500 */
body {
  font-family: "Toss Product Sans", "SF Pro KR", "SF Pro Display",
               -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo",
               sans-serif;
  font-weight: 500;   /* ⚠️ 400이 아님. Toss body는 500이 기본. */
}

/* 2. 배경 + 텍스트 */
:root {
  --bg: #F2F4F6;      /* light gray — 순백 아님 */
  --fg: #191F28;      /* cool dark navy-black */
}
body { background: var(--bg); color: var(--fg); }

/* 3. 브랜드 블루 */
:root { --brand: #3182F6; }
```

**절대 하지 말아야 할 것 하나**: 배경을 `#FFFFFF` 순백으로 두는 것. Toss의 기본 배경은 **`#F2F4F6`** cool gray다. 순백 바탕에 놓으면 Toss 특유의 카드 위 카드 레이어링 구조가 무너지고 그냥 "평범한 앱"이 된다.

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://toss.im` |
| Fetched | 2026-04-12 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 99,561 bytes (SSR) |
| CSS files | 6개 외부, 총 556,215자 |
| Token prefix | `--adaptive*`, `--t*` (TDS — Toss Design System) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: SSR (서버 사이드 렌더링, React 기반 추정)
- **Design system**: TDS (Toss Design System) — `tds.min.css` 파일에 정의, prefix `--adaptive*` + `--t*`
- **CSS architecture**: 1-tier 플랫 구조
  ```
  core       (--adaptive*, --t*)      raw hex값 + rgba opacity
  util       없음 (semantic alias tier 미존재)
  component  없음 (컴포넌트 스타일은 직접 hex 사용)
  ```
- **Class naming**: BEM-ish (`button--size-big`, `button--type-danger`, `button--style-weak`)
- **Default theme**: light (bg = `#F2F4F6`, dark 모드용 `--adaptive*` 변수 내장)
- **Font loading**: 셀프 호스트 woff2 (`Toss Product Sans`, `Basier Square`, `SD Gothic Neo` — `static.toss.im`)
- **Canonical anchor**: `#3182F6` — `.button` 기본 배경색이자 `.text-button--type-primary` 컬러. Toss 블루의 핵심.

---

## 04. Font Stack
<!-- SOURCE: auto+manual -->

- **Display font**: `Toss Product Sans` (Toss 자체 제작, 비공개 라이선스)
- **Latin fallback**: `Basier Square` (atipo foundry, 유료 라이선스)
- **System fallback**: `SF Pro KR`, `SF Pro Display`, `-apple-system`, `Apple SD Gothic Neo`
- **Weight normal / bold**: `500` / `700`

```css
body {
  font-family: "Toss Product Sans", Tossface, "SF Pro KR",
               "SF Pro Display", "SF Pro Icons",
               -apple-system, BlinkMacSystemFont,
               "Basier Square", "Apple SD Gothic Neo",
               "Roboto", "Noto Sans KR", "Noto Sans",
               "Helvetica Neue", Helvetica, Arial, sans-serif,
               "Apple Color Emoji", "Segoe UI Emoji",
               "Segoe UI Symbol", "Noto Color Emoji";
  font-weight: 500;
  -webkit-font-smoothing: antialiased;
}
```

> **라이선스 주의**: `Toss Product Sans`는 Toss 전용 폰트라 외부 프로젝트에서 사용 불가. 가장 가까운 대체재는 `Pretendard` (한글) + `Inter` (라틴). `Basier Square`는 Latin 전용 유료 폰트.

---

## 05. Typography Scale
<!-- SOURCE: auto -->

| Class | Size | Line-height | Usage |
|---|---|---|---|
| `.typography-t1` | 30px | 1.333 | 최대 제목 |
| `.typography-t2` | 26px | 1.346 | 섹션 헤더 |
| `.typography-t3` | 22px | 1.409 | 서브 헤더 |
| `.typography-t4` | 20px | 1.45 | 카드 제목 |
| `.typography-t5` | 17px | 1.5 | 본문 대 |
| `.typography-t6` | 15px | 1.5 | 본문 기본 |
| `.typography-t7` | 13px | 1.5 | 캡션 |
| `.typography-st1` | 29px | 1.31 | 서브 타이틀 1 |
| `.typography-st2` | 28px | 1.321 | 서브 타이틀 2 |
| `.typography-st3` | 27px | 1.333 | 서브 타이틀 3 |
| `.typography-st4` | 25px | 1.36 | 서브 타이틀 4 |
| `.typography-st5` | 24px | 1.375 | 서브 타이틀 5 |
| `.typography-st6` | 23px | 1.391 | 서브 타이틀 6 |
| `.typography-st7` | 21px | 1.429 | 서브 타이틀 7 |
| `.typography-st8` | 19px | 1.474 | 서브 타이틀 8 |
| `.typography-st9` | 18px | 1.5 | 서브 타이틀 9 |
| `.typography-st10` | 16px | 1.5 | 서브 타이틀 10 |
| `.typography-st11` | 14px | 1.5 | 서브 타이틀 11 |
| `.typography-st12` | 12px | 1.5 | 서브 타이틀 12 |
| `.typography-st13` | 11px | 1.5 | 서브 타이틀 13 |

> ⚠️ Toss는 1px 단위의 촘촘한 타이포 스케일을 사용한다. `t1`~`t7` (7단)이 주 스케일이고, `st1`~`st13` (13단)은 1px 간격 보간 스케일이다. CSS 변수 `--toss-font-size-{N}`, `--toss-line-height-{N}` 형태로 매핑되지만, fallback으로 항상 고정 px 값이 먼저 선언된다.
>
> Weight 클래스는 별도 없이 컴포넌트별로 직접 `font-weight` 지정. `button`은 600, heading은 700, body는 컨텍스트에 따라 400~500.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand Blue Ramp (10 steps)

| Token | Hex |
|---|---|
| `.blue50` | `#E8F3FF` |
| `.blue100` | `#C9E2FF` |
| `.blue200` | `#90C2FF` |
| `.blue300` | `#64A8FF` |
| `.blue400` | `#4593FC` |
| `.blue500` | `#3182F6` ⭐ **canonical Toss Blue** |
| `.blue600` | `#2272EB` |
| `.blue700` | `#1B64DA` |
| `.blue800` | `#1957C2` |
| `.blue900` | `#194AA6` |

### 06-3. Grey Ramp (neutral)

| Step | Light (`grey`) | Dark (`inverseGrey`) |
|---|---|---|
| 50  | `#F9FAFB` | `#202027` |
| 100 | `#F2F4F6` | `#2C2C35` |
| 200 | `#E5E8EB` | `#3C3C47` |
| 300 | `#D1D6DB` | `#4D4D59` |
| 400 | `#B0B8C1` | `#62626D` |
| 500 | `#8B95A1` | `#7E7E87` |
| 600 | `#6B7684` | `#9E9EA4` |
| 700 | `#4E5968` | `#C3C3C6` |
| 800 | `#333D4B` | `#E4E4E5` |
| 900 | `#191F28` | `#FFFFFF` |

### 06-4. Accent Families

| Family | Key step | Hex |
|---|---|---|
| **Red** | 600 | `#E42939` |
| Red | 500 | `#F04452` |
| **Green** | 700 | `#029359` |
| Green | 600 | `#02A262` |
| **Teal** | 700 | `#0C8585` |
| Teal | 600 | `#109595` |
| **Orange** | 500 | `#FE9800` |
| **Yellow** | 900 | `#DD7D02` |
| **Purple** | 500 | `#A234C7` |

### 06-5. Semantic

| Token | Hex | Usage |
|---|---|---|
| `--tBlueBadgeColor` | `#1B64DA` | 정보 배지 텍스트 |
| `--tRedBadgeColor` | `#D22030` | 에러/위험 배지 텍스트 |
| `--tGreenBadgeColor` | `#029359` | 성공 배지 텍스트 |
| `--tTealBadgeColor` | `#0C8585` | 보조 정보 배지 텍스트 |
| `--tYellowBadgeColor` | `#DD7D02` | 경고 배지 텍스트 |
| `--tElephantBadgeColor` | `#4E5968` | 비활성/중립 배지 텍스트 |

### 06-6. Component Token Layer

| Alias | Hex | Usage |
|---|---|---|
| `--adaptiveBackground` | `#FFFFFF` | 기본 배경 |
| `--adaptiveGreyBackground` | `#F2F4F6` | 회색 배경 (페이지 기본) |
| `--adaptiveGrey900` | `#191F28` | 최고 진한 텍스트 |
| `--adaptiveGrey800` | `#333D4B` | 보조 텍스트 |
| `--adaptiveGrey700` | `#4E5968` | 약한 텍스트 |
| `--tPrimaryWeakButtonBackground` | `#E8F3FF` | 약한 primary 버튼 배경 |
| `--tDarkWeakButtonBackground` | `#F2F4F6` | 약한 dark 버튼 배경 |
| `--tDangerWeakButtonBackground` | `#FFEEEE` | 약한 danger 버튼 배경 |
| `--tDarkFillButtonBackground` | `#4E5968` | dark 채움 버튼 배경 |
| `--adaptiveDisabledBlue500` | `#C9E2FF` | 비활성 primary 버튼 |

### 06-7. Dominant Colors (실제 DOM 빈도 순)

| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 114 | 카드/배경 white |
| 2 | `#333D4B` | 47 | body text dark |
| 3 | `#4E5968` | 38 | secondary text |
| 4 | `#8B95A1` | 35 | muted text |
| 5 | `#191F28` | 34 | heading text |
| 6 | `#F2F4F6` | 31 | page background |
| 7 | `#3182F6` | 27 | brand primary CTA |
| 8 | `#6B7684` | 26 | tertiary text |
| 9 | `#B0B8C1` | 22 | border/divider |
| 10 | `#4593FC` | 17 | blue accent hover |
| 11 | `#E5E8EB` | 16 | light border |
| 12 | `#F9FAFB` | 15 | lightest background |
| 13 | `#D1D6DB` | 13 | medium border |
| 14 | `#E42939` | 13 | error red |
| 15 | `#1B64DA` | 10 | link blue deep |

---

## 07. Spacing
<!-- SOURCE: auto -->

| Value | Use case |
|---|---|
| 4px | 인라인 간격, 아이콘-텍스트 gap |
| 8px | 컴포넌트 내부 여백 |
| 12px | 버튼 내부 패딩 |
| 16px | 카드 내부 패딩 기본, 리스트 아이템 간격 |
| 20px | 섹션 좌우 패딩 (모바일 기준) |
| 24px | 카드 여유 패딩, 배너 마진 |
| 32px | 섹션 수직 간격 |

> ⚠️ Toss는 명시적 spacing 토큰 변수를 사용하지 않는다. 모든 간격은 컴포넌트별로 직접 px 값을 지정하며, 4px 기반 그리드를 암묵적으로 따른다.

---

## 08. Radius
<!-- SOURCE: auto -->

| Value | Context |
|---|---|
| 4px | 인풋 필드, 키패드 버튼, 작은 요소 |
| 6px | tiny 버튼 (`button--size-tiny`) |
| 8px | medium 버튼 (`button--size-medium`), 일반 카드 |
| 10px | 중간 카드, 바텀시트 내 요소 |
| 12px | large 버튼 (`button--size-large`) |
| 16px | big 버튼 (`button--size-big`), 대형 카드 |
| 20px | pill 형태 |
| 50% / 100% | 원형 아바타, 라디오 인디케이터 |

> 버튼 사이즈가 커질수록 radius도 비례 증가하는 것이 Toss의 특징: tiny(6) → medium(8) → large(12) → big(16).

---

## 09. Shadows
<!-- SOURCE: auto -->

| Level | Value | Usage |
|---|---|---|
| elevation-low | `0 0 0 1px rgba(0,23,51,0.02), 0 6px 20px 0 rgba(2,32,71,0.05), 0 1px 3px 0 rgba(0,27,55,0.1)` | 기본 카드, 조용한 float |
| elevation-high | `0 0 0 1px rgba(2,32,71,0.05), 0 6px 20px 0 rgba(0,29,54,0.31), 0 1px 3px 0 rgba(0,27,55,0.1)` | 바텀시트 CTA, 모달 |
| elevation-modal | `0 0 0 1px rgba(0,0,0,0.04), 0 6px 20px 0 rgba(0,0,0,0.26), 0 1px 3px 0 rgba(0,0,0,0.07)` | 풀 모달 다이얼로그 |
| inset-focus | `inset 0 0 0 1px rgba(0,0,33,0.16)` | 포커스 링 |
| inset-border | `inset 0 0 0 1px rgba(0,0,0,0.02)` | 가벼운 인셋 보더 |

> 모든 elevation shadow는 3-layer 구조: `outline ring + spread + edge`. rgba 기반이라 다크 모드에서도 자연스럽다.

---

## 10. Motion
<!-- SOURCE: auto -->

| Pattern | Value | Usage |
|---|---|---|
| button-feedback | `background-color .1s ease-in-out` | 버튼 hover/active 피드백 |
| state-change | `color .1s ease-in-out, background-color .1s ease-in-out, border-color .1s ease-in-out, box-shadow .1s ease-in-out` | 전체 상태 전환 |
| background-soft | `background-color .2s ease` | 배경색 부드러운 전환 |
| transform | `-webkit-transform .2s ease-in-out` | 슬라이드/회전 |
| progress | `transform .5s ease-in-out` | 프로그레스 바 |
| input-morph | `font-size .1s cubic-bezier(.4,0,.2,1), font-weight .1s cubic-bezier(.4,0,.2,1), color .1s cubic-bezier(.4,0,.2,1)` | 인풋 라벨 변형 |
| generic | `.25s ease-in-out` | 일반 전환 |

---

## 12. Components
<!-- SOURCE: auto+manual -->

### Button (`.button`)

```html
<button class="button button--size-large">확인</button>
<button class="button button--size-large button--style-weak">취소</button>
<button class="button button--size-large button--type-danger">삭제</button>
<button class="button button--size-large button--type-dark">이전</button>
```

| Spec | Value |
|---|---|
| Default bg | `#3182F6` (Toss Blue) |
| Default text | `#FFFFFF` |
| font-weight | `600` |
| Sizes | tiny(6px radius) · medium(8px) · large(12px) · big(16px) |
| Weak variant | bg `#E8F3FF`, text `#3182F6` |
| Danger variant | bg `#F04452` |
| Dark variant | bg `#4E5968` |
| Hover overlay | `rgba(0,29,54,0.31)` pseudo-element |
| Transition | `color .1s ease-in-out, background-color .1s ease-in-out` |

### Text Button (`.text-button`)

```html
<button class="text-button text-button--type-primary">자세히 보기</button>
<button class="text-button text-button--type-grey">닫기</button>
```

| Spec | Value |
|---|---|
| Primary color | `#3182F6` |
| Grey color | `#6B7684` |
| Underline border | `1px solid #B0B8C1` |
| Background | transparent |

### Alert Dialog (`.alert-dialog`)

```html
<div class="alert-dialog">
  <div class="alert-dialog__message">정말 삭제하시겠어요?</div>
  <button class="alert-dialog__button">확인</button>
</div>
```

| Spec | Value |
|---|---|
| Button color | `#3182F6` |
| Border-radius | `12px` |
| Padding | `4px 10px` |

### Badge

| Variant | Background | Text |
|---|---|---|
| Blue | `rgba(49,130,246,0.16)` | `#1B64DA` |
| Red | `rgba(244,67,54,0.16)` | `#D22030` |
| Green | `rgba(2,162,98,0.16)` | `#029359` |
| Teal | `rgba(0,129,138,0.16)` | `#0C8585` |
| Yellow | `rgba(255,179,49,0.16)` | `#DD7D02` |
| Elephant | `rgba(78,89,104,0.16)` | `#4E5968` |

---

## 13. Content / Copy Voice
<!-- SOURCE: manual -->

| Pattern | Rule | Example |
|---|---|---|
| Headline | 짧은 한국어, 구어체 톤. 물음표 혹은 ~해보세요 종결 | "내 돈 관리, 이렇게 쉬웠나요?" |
| Primary CTA | 2~4글자 동사형 | "시작하기" |
| Secondary CTA | 설명 + 동사 | "자세히 알아보기" |
| Subheading | 기능 설명을 1문장으로 | "한 눈에 보는 내 자산" |
| Tone | 친근하고 쉬운 금융. 전문 용어 최소화. 반말/존댓말 혼용 없이 일관된 존댓말. | |

---

## 14. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Toss — copy into your root stylesheet */
:root {
  /* Fonts */
  font-family: "Toss Product Sans", "SF Pro KR", "SF Pro Display",
               -apple-system, BlinkMacSystemFont,
               "Apple SD Gothic Neo", sans-serif;

  /* Brand Blue (anchor + 4 steps) */
  --toss-color-blue-50:  #E8F3FF;
  --toss-color-blue-300: #64A8FF;
  --toss-color-blue-500: #3182F6;   /* ← canonical */
  --toss-color-blue-700: #1B64DA;
  --toss-color-blue-900: #194AA6;

  /* Surfaces */
  --toss-bg-page:   #F2F4F6;
  --toss-bg-card:   #FFFFFF;
  --toss-bg-dark:   #17171C;
  --toss-text:      #191F28;
  --toss-text-secondary: #333D4B;
  --toss-text-muted:#8B95A1;

  /* Key spacing (4px grid) */
  --toss-space-sm:  8px;
  --toss-space-md:  16px;
  --toss-space-lg:  24px;

  /* Radius */
  --toss-radius-sm: 8px;
  --toss-radius-md: 12px;
  --toss-radius-lg: 16px;
}
```

---

## 15. Tailwind Config
<!-- SOURCE: manual -->

```js
// tailwind.config.js — Toss
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          50:  '#E8F3FF',
          100: '#C9E2FF',
          200: '#90C2FF',
          300: '#64A8FF',
          400: '#4593FC',
          500: '#3182F6',
          600: '#2272EB',
          700: '#1B64DA',
          800: '#1957C2',
          900: '#194AA6',
        },
        grey: {
          50:  '#F9FAFB',
          100: '#F2F4F6',
          200: '#E5E8EB',
          300: '#D1D6DB',
          400: '#B0B8C1',
          500: '#8B95A1',
          600: '#6B7684',
          700: '#4E5968',
          800: '#333D4B',
          900: '#191F28',
        },
      },
      fontFamily: {
        sans: ['"Toss Product Sans"', '"SF Pro KR"', 'system-ui'],
      },
      fontWeight: {
        normal: '500',
        bold:   '700',
      },
      borderRadius: {
        sm: '8px',
        DEFAULT: '12px',
        lg: '16px',
      },
      boxShadow: {
        low:  '0 0 0 1px rgba(0,23,51,0.02), 0 6px 20px 0 rgba(2,32,71,0.05), 0 1px 3px 0 rgba(0,27,55,0.1)',
        high: '0 0 0 1px rgba(2,32,71,0.05), 0 6px 20px 0 rgba(0,29,54,0.31), 0 1px 3px 0 rgba(0,27,55,0.1)',
      },
    },
  },
};
```

---

## 16. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- 배경은 `#F2F4F6` cool gray, 그 위에 `#FFFFFF` 카드를 올려라 — Toss의 레이어 구조 핵심
- 브랜드 블루 `#3182F6`는 CTA 버튼과 primary 링크에만 써라
- 버튼 사이즈에 맞는 radius를 쓸 것: tiny=6, medium=8, large=12, big=16
- Grey ramp `#191F28` → `#333D4B` → `#4E5968` → `#8B95A1` → `#B0B8C1` 5단계 텍스트 위계를 지킬 것
- 본문 font-weight는 `500`이 기본. 400은 서브텍스트, 600은 버튼, 700은 제목에만
- shadow는 항상 3-layer (outline + spread + edge) 구조
- badge 배경은 해당 색상의 `rgba(*, 0.16)` opacity 패턴

### ❌ DON'T
- 배경에 `#FFFFFF` 순백을 쓰지 마라 — Toss의 기본 page background는 `#F2F4F6`
- 브랜드 블루를 배경색으로 넓게 깔지 마라 — 블루는 포인트 컬러로만 사용
- `font-weight: 400`을 body 기본으로 두지 마라 — Toss는 `500`이 normal
- Grey scale에서 `#000000` 순흑 사용 금지 — 가장 진한 텍스트도 `#191F28`
- 단일 레이어 `box-shadow`로 elevation을 재현하지 마라 — 3-layer가 아니면 깊이감이 다름
- Toss Product Sans 없이 `Inter`로 대체할 때 letter-spacing을 건드리지 마라 — 기본값이 맞다
