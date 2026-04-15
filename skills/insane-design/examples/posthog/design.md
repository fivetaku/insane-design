---
slug: posthog
service_name: PostHog
site_url: https://posthog.com
fetched_at: 2026-04-11
default_theme: light
brand_color: "#f54e00"
primary_font: IBM Plex Sans Variable
font_weight_normal: 400
token_prefix: ""
---

# DESIGN.md — PostHog (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

PostHog의 웹사이트는 밝은 배경 위에 독특한 일러스트레이션과 캐릭터가 결합된 친근한 개발자 도구 디자인이다. 전형적인 B2B SaaS의 딱딱함을 벗어나 유쾌하면서도 전문적인 인상을 동시에 전달한다.

타이포그래피는 기본 시스템 서체를 사용한다. 본문 weight는 **400**이며, 깔끔하고 읽기 편한 텍스트 경험을 제공한다.

브랜드 오렌지-레드 `#F54E00`는 CTA와 핵심 인터랙션 요소에 강한 시각적 포인트를 만든다. 밝은 배경 위에서 일러스트레이션의 다양한 컬러와 조화를 이루며 PostHog만의 개성을 표현한다.

**Key Characteristics:**
- **크림 배경** `#eeefe9`가 base. 순백 아님.
- **IBM Plex Sans Variable**을 self-host — 시각적 정체성의 핵심이다.
- **오렌지 `#f54e00`**를 CTA/pagination에 공격적으로 사용.
- **Hard offset 솔리드 섀도** (`4px 4px 0 #151515`)를 카드 패턴으로. blur 없음.
- 다크 섹션에는 `#1e1f23` (coal) 사용. 순수 검정 아님.
---

## 01. Quick Start

> 5분 안에 PostHog처럼 만들기 — 3가지만 하면 80%

```css
/* 1. IBM Plex Sans Variable — 핵심 폰트 */
body {
  font-family: "IBM Plex Sans Variable", "IBM Plex Sans",
               -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
}

/* 2. 크림 배경 + 거의 검정 텍스트 (순백 아님) */
:root {
  --bg-primary: #eeefe9;   /* 따뜻한 크림 */
  --text-primary: #151515; /* 거의 검정 */
}
body { background: var(--bg-primary); color: var(--text-primary); }

/* 3. 오렌지 브랜드 + 크림 액센트 */
:root {
  --brand-orange: #f54e00;  /* CTA 오렌지 */
  --accent-yellow: #f5e2b2; /* 크림 옐로우 하이라이트 */
}
```

**절대 하지 말아야 할 것 하나**: 배경을 순백 `#ffffff`로 두지 말 것. PostHog 사이트의 실제 base 배경은 따뜻한 크림 `#eeefe9`와 페일 옐로우 `#f5e2b2` 계열이다. 순백을 깔면 전체 분위기가 infra SaaS처럼 차가워진다.

---

## 02. Provenance

| | |
|---|---|
| Source URL | `https://posthog.com` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| HTML size | 1,016,563 bytes (Gatsby/Next SSR) |
| CSS files | 1 인라인, 총 615,853자 |
| `@font-face` | 29개 (Source Code Pro 다중, IBM Plex Sans VF) |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack

- **Framework**: Gatsby 마케팅 사이트 (대규모 인라인 CSS, 615KB)
- **Design system**: 전통적 DS 라이브러리 없음 — Tailwind + custom utility
- **CSS architecture**: 2계층
  ```
  Raw tokens       (--text-primary, --bg-primary)   rgba triplet 형태
  Prose overrides  (--tw-prose-*)                   article 타이포용
  ```
- **Class naming**: Tailwind utility + semantic (예: `.bg-primary`, `.text-primary`)
- **Default theme**: light + 크림 배경 (`#eeefe9`), 다크 모드 variant 별도 존재
- **Font loading**: 29개 `@font-face` self-hosted data-URI base64 (Source Code Pro, IBM Plex Sans VF)
- **Canonical anchor**: `#f54e00` 오렌지 — hero CTA + swiper pagination indicator에 사용

---

## 04. Font Stack

- **Display font**: `IBM Plex Sans Variable` (Google Fonts OFL, self-host) — 빈도 12회 최상위
- **Accent display**: `Open Runde` (OFL, 라운드 헤드라인용)
- **Code font**: `Source Code Pro` (self-host, data-URI embedded)
- **Weight normal / bold**: `400` / `700`

```css
:root {
  --font-display: "IBM Plex Sans Variable", "IBM Plex Sans",
                  -apple-system, BlinkMacSystemFont,
                  "avenir next", avenir, "segoe ui", sans-serif;
  --font-accent: "Open Runde", var(--font-display);
  --font-mono: "Source Code Pro", Menlo, Consolas, Monaco, monospace;
}
body {
  font-family: var(--font-display);
  font-weight: 400;
}
```

---

## 05. Typography Scale

| Token | Size | Weight | Line-height |
|---|---|---|---|
| text-xs  | 0.75rem (12px)  | 400 | 1.5  |
| text-sm  | 0.875rem (14px) | 400 | 1.5  |
| text-base| 1rem (16px)     | 400 | 1.5  |
| text-lg  | 1.125rem (18px) | 400 | 1.6  |
| text-xl  | 1.25rem (20px)  | 600 | 1.4  |
| text-2xl | 1.5rem (24px)   | 700 | 1.3  |
| text-3xl | 2.25rem (36px)  | 700 | 1.15 |

> ⚠️ Weight 히스토그램: **700(29회)** > 400(21) > 600(18) > 100(12) > 500(10). 700이 가장 많이 쓰이는 건 hero headline + section title 때문이다.

---

## 06. Colors

### 06-1. Brand / Accent

| Token | Hex | Count | Role |
|---|---|---|---|
| brand-orange | `#f54e00` | 14 | ⭐ CTA / pagination / hero accent |
| hot-coral    | `#c23d00` | 8  | hover / pressed variant |
| burnt        | `#802700` | 8  | darker shade |
| gold         | `#f7a501` | 8  | 보조 accent |
| mustard      | `#f1a82c` | 7  | warning / highlight |
| cream-yellow | `#f5e2b2` | 18 | ⭐ 페일 하이라이트 배경 |

### 06-2. Neutrals (배경 + 텍스트)

| Token | Hex | Count | Role |
|---|---|---|---|
| bg-cream   | `#eeefe9` | 8  | ⭐ 주 크림 배경 |
| bg-white   | `#ffffff` | 8  | 카드 |
| text-ink   | `#151515` | 8  | 본문 |
| text-char  | `#161616` | 10 | 거의 검정 variant |
| coal       | `#1e1f23` | 15 | ⭐ 다크 섹션 배경 |
| text-mute  | `#8d8d8d` | 10 | 보조 텍스트 |
| text-soft  | `#808080` | 7  | tertiary |

### 06-3. Data Viz (그래프)

| Token | Hex | Usage |
|---|---|---|
| teal-mint  | `#29dbbb` | chart line 1 |
| red-alert  | `#e92f2f` | error / chart dec |
| forest     | `#6aa84f` | chart green |
| sunflower  | `#eb9d2a` | chart yellow |
| deep-navy  | `#1e2f46` | chart dark bar |
| bright-grn | `#00ff00` | terminal green (code block) |

### 06-4. Semantic Alias (resolved)

| Alias | Resolves to |
|---|---|
| `--primary`   | `var(--text-primary)` → rgb(77 79 70) |
| `--secondary` | `var(--text-secondary)` → rgb(101 103 94) |
| `--muted`     | `var(--text-muted)` → rgb(158 160 150) |
| `--accent`    | `229 231 224` (warm gray) |
| `--border`    | `191 193 183` (warm gray) |

---

## 07. Spacing

Tailwind base spacing `0.25rem` (4px) 단계 + 단 하나의 전용 변수.

| Token | Value | Use |
|---|---|---|
| `--spacing` (tailwind) | 0.25rem / 4px | 기본 단위 |
| `--viewport-padding` | 25px | 모바일 뷰포트 패딩 |
| 조합 단계 | 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 80 · 96 px | Tailwind class |

---

## 08. Radius

| Value | Count | Context |
|---|---|---|
| `9999px` | 14 | pill 버튼, badge |
| `.25rem` / 4px | 13 | 기본 박스, input |
| `4px` | 11 | 카드 |
| `.375rem` / 6px | 7 | 버튼 |
| `2px` | 7 | 인라인 칩 |

---

## 09. Shadows

PostHog는 과감한 **dual-stroke drop-shadow 패턴**을 쓴다 — 카드 밑에 오렌지/크림 레이어를 겹쳐서 stickery 느낌을 낸다.

```css
/* 대표 카드 패턴 (관측) */
.card {
  background: #eeefe9;
  border: 1.5px solid #151515;
  box-shadow: 4px 4px 0 #151515;   /* solid offset shadow */
  border-radius: 6px;
}

.card--highlight {
  background: #f5e2b2;
  box-shadow: 4px 4px 0 #f54e00;
}
```

시각적 정체성의 핵심 — Notion 스타일 subtle blur 섀도가 아니라 **하드 오프셋 솔리드**.

---

## 12. Responsive Behavior
<!-- SOURCE: auto+manual -->

| Breakpoint | Width | Key Changes |
|---|---|---|
| Mobile | <640px | 단일 컬럼, 헤딩 축소, 카드 스택 |
| Tablet | 640-1024px | 2열 그리드, 중간 패딩 |
| Desktop | 1024-1280px | 풀 레이아웃, 3열 그리드 |
| Large | >1280px | 중앙 정렬 max-width 1200px, 넉넉한 마진 |

> ⚠️ PostHog는 모바일 퍼스트 반응형 디자인을 채택하며, 브레이크포인트별로 그리드와 타이포그래피가 유동적으로 조정된다.

---

## 13. Components

### Hero CTA
```html
<button class="bg-[#f54e00] text-white font-bold px-6 py-3
               border-2 border-[#151515] shadow-[4px_4px_0_#151515]
               hover:translate-y-[-2px] transition rounded-md">
  Get started — free
</button>
```

### Sticker Card
```html
<div class="bg-[#f5e2b2] border-2 border-[#151515]
            shadow-[4px_4px_0_#f54e00] rounded-md p-5">
  <h3 class="font-bold text-[#151515]">Session replay</h3>
  <p class="text-[#161616]">Watch how users really use your product.</p>
</div>
```

---

## 15. Drop-in CSS

```css
/* PostHog — copy into your root stylesheet */
:root {
  /* Fonts */
  --font-display: "IBM Plex Sans Variable", "IBM Plex Sans",
                  -apple-system, BlinkMacSystemFont, sans-serif;
  --font-accent:  "Open Runde", var(--font-display);
  --font-mono:    "Source Code Pro", Menlo, Consolas, monospace;

  /* Brand */
  --brand-orange:  #f54e00;
  --brand-coral:   #c23d00;
  --brand-burnt:   #802700;
  --accent-yellow: #f5e2b2;
  --accent-gold:   #f7a501;

  /* Surfaces */
  --bg-cream:  #eeefe9;
  --bg-coal:   #1e1f23;
  --bg-white:  #ffffff;
  --text-ink:  #151515;
  --text-mute: #8d8d8d;

  /* Semantic */
  --primary:   var(--text-ink);
  --accent:    rgb(229 231 224);
  --border:    rgb(191 193 183);

  /* Sticker shadow atom */
  --shadow-sticker: 4px 4px 0 var(--text-ink);
  --shadow-sticker-alt: 4px 4px 0 var(--brand-orange);
}

body {
  font-family: var(--font-display);
  font-weight: 400;
  background: var(--bg-cream);
  color: var(--text-ink);
}
```

---

## 17. Agent Prompt Guide
<!-- SOURCE: manual -->

### Quick Color Reference
| Role | Hex |
|---|---|
| Primary CTA | `#f54e00` |
| Heading text | `#151515` |
| Body text | `#50565B` |
| Background | `#FFFFFF` |
| Border | `#E5E7E0` |
| Link | `#F54E00` |
| Dark section | `#151515` |

### Example Component Prompts
- "Create a hero section on `#FFFFFF` background. Headline at 3rem `IBM Plex Sans Variable` weight 400. CTA button `#f54e00` with white text."
- "Design a card: `#1c1c1f` background, `#E5E7E0` border, 8px radius. Body text `#50565B` at weight 400."

### Iteration Guide
1. 폰트: `IBM Plex Sans Variable` 패밀리, 본문 weight 400
2. 컬러: 브랜드 `#f54e00`는 CTA/링크에만 집중. 배경 `#FFFFFF`, 텍스트 `#151515`
3. 그림자: flat 디자인 기반, 최소한의 그림자 사용
---

## 18. DO / DON'T

### ✅ DO
- **크림 배경** `#eeefe9`가 base. 순백 아님.
- **IBM Plex Sans Variable**을 self-host — 시각적 정체성의 핵심이다.
- **오렌지 `#f54e00`**를 CTA/pagination에 공격적으로 사용.
- **Hard offset 솔리드 섀도** (`4px 4px 0 #151515`)를 카드 패턴으로. blur 없음.
- 다크 섹션에는 `#1e1f23` (coal) 사용. 순수 검정 아님.
- Code block은 `Source Code Pro` self-host 고수.

### ❌ DON'T
- 순백 `#ffffff` 배경 금지 — PostHog 느낌이 안 남.
- Inter / Roboto 대체 금지 — IBM Plex Sans의 낮은 x-height가 정체성.
- subtle blur 섀도 (`0 4px 12px rgba(0,0,0,0.1)`) 금지. 하드 오프셋이 시그니처.
- 파스텔 톤 오렌지 사용 금지. 풀채도 `#f54e00`이 anchor.
- 차가운 그레이 중립 금지. Warm gray `rgb(191 193 183)` 기반이다.

---

