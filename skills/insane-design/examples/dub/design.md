---
slug: dub
service_name: Dub.co
site_url: https://dub.co
fetched_at: 2026-04-11
default_theme: light
brand_color: "#855AFC"
primary_font: Satoshi
font_weight_normal: 400
token_prefix: shadcn
---

# DESIGN.md — Dub.co (Claude Code Edition)

---

## 00. Visual Theme & Atmosphere
<!-- SOURCE: manual -->

Dub.co는 premium SaaS link analytics 서비스의 세련된 감성을 가진다. 순백 `#FFFFFF` 배경 위에 Tailwind neutral ramp(`#171717` ~ `#FAFAFA`)가 깔끔한 계층을 만들고, brand purple `#855AFC`가 CTA에 집중적으로 사용된다. shadcn/ui 기반 HSL channel 토큰 시스템이 기술적 정교함을 보여준다.

3-폰트 시스템이 특징적이다: Satoshi(display heading)가 premium 감성을, Inter(body)가 가독성을, GeistMono(stats/short link)가 데이터 정확성을 전달한다. 특히 short link 표시(`dub.co/abc123`)에 GeistMono를 사용하는 것이 브랜드 포인트다.

**Key Characteristics:**
- Brand purple `#855AFC` + Tailwind neutral ramp의 정제된 조합
- 3-폰트 분리: Satoshi(heading) + Inter(body) + GeistMono(data)
- Pink inset shadow hover(`#F350663A`) — 시그니처 호버 효과
- Analytics chart palette 6색이 브랜드 확장 역할
- `#000000AA` (67% alpha) 텍스트 — 독특한 alpha text 패턴

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 Dub.co처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 — Satoshi display + Inter body + GeistMono stats */
:root {
  --font-satoshi: "Satoshi", "Satoshi Fallback", system-ui, sans-serif;
  --font-inter:   "Inter", ui-sans-serif, system-ui, -apple-system, sans-serif;
  --font-geist-mono: "GeistMono", ui-monospace, SFMono-Regular, "Roboto Mono", Menlo, monospace;
}
body { font-family: var(--font-inter); font-weight: 400; }
h1, h2, h3 { font-family: var(--font-satoshi); font-weight: 700; }
.stat, .short-link { font-family: var(--font-geist-mono); }

/* 2. 라이트 + Tailwind neutral */
:root {
  --bg:         #FFFFFF;
  --bg-muted:   #FAFAFA;
  --fg:         #171717;
  --fg-alpha:   rgba(0, 0, 0, 0.67);  /* #000000AA · 실제 빈도 2위 */
  --border:     #E5E5E5;
}

/* 3. 브랜드 퍼플 */
:root { --brand: #855AFC; }
```

**절대 하지 말아야 할 것 하나**: Dub의 브랜드 폰트는 **Satoshi**이며 `Inter` 단독이 아니다. headings와 stat 숫자에 Satoshi를 쓰지 않으면 "premium SaaS" 감성이 generic 대시보드로 변질된다. 그리고 정확한 브랜드 퍼플은 `#7B61FF`가 아니라 **`#855AFC`** (12회 실제 등장).

---

## 02. Provenance
<!-- SOURCE: auto -->

| | |
|---|---|
| Source URL | `https://dub.co` |
| Fetched | 2026-04-11 |
| Extractor | `real/fetch_all.py` (curl + Chrome UA) |
| CSS files | 2개 · 290,320자 |
| Custom properties | 154개 (color 13 · shadow 8 · spacing 5) |
| Unique hex | 222개 |
| Method | CSS 커스텀 프로퍼티 직접 파싱 · AI 추론 없음 |

---

## 03. Tech Stack
<!-- SOURCE: auto+manual -->

- **Framework**: Next.js + Tailwind CSS + **shadcn/ui**
- **Design system**: shadcn HSL channel 토큰 시스템
  ```
  shadcn tier     hsl(var(--primary)/50%)  · HSL triplet을 var로 저장 후 opacity modifier
  slot tier       --background / --foreground / --primary / --muted / --border
  tw-prose tier   --tw-prose-* / --tw-prose-invert-*
  ```
- **Class naming**: Tailwind utility + shadcn component 클래스
- **Default theme**: light (bg `#FFFFFF`, 라이트 모드 주력)
- **Font loading**: CSS var 기반 스위칭 — `var(--font-satoshi)`, `var(--font-geist-mono)`, Inter
- **Canonical anchor**: `#855AFC` — brand purple (12회)

---

## 04. Font Stack
<!-- SOURCE: auto -->

- **Display**: `Satoshi` (Indian Type Foundry, paid) — 히어로/헤딩/stat label
- **Body**: `Inter` — 본문 기본
- **Mono / numeric**: `GeistMono` (Vercel Geist) — short link 표시, stat 숫자, code
- **Fallback**: `system-ui`, `ui-sans-serif`, `-apple-system`

```css
:root {
  --font-satoshi:    "Satoshi", "Satoshi Fallback", system-ui, sans-serif;
  --font-inter:      "Inter", ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-geist-mono: "GeistMono", ui-monospace, SFMono-Regular, "Roboto Mono", Menlo, Monaco, "Liberation Mono", "DejaVu Sans Mono", "Courier New", monospace;
}
body { font-family: var(--font-inter); font-weight: 400; }
h1, h2, h3, .display { font-family: var(--font-satoshi); font-weight: 700; letter-spacing: -0.02em; }
.stat-number, .short-link, code { font-family: var(--font-geist-mono); }
```

---

## 05. Typography Scale
<!-- SOURCE: auto (rem/px/em frequency) -->

| Size | Usage |
|---|---|
| 0.75rem (12px) | caption |
| 0.875rem (14px) | small body (freq 4) |
| 1rem (16px) | body (freq 4) |
| 1.125rem (18px) | lead |
| 1.25rem (20px) | h4 |
| 1.5rem (24px) | h3 (freq 3) |
| 1.875rem (30px) | h2 (freq 3) |
| 2.25rem (36px) | h1 stat (freq 3) |
| 3rem (48px) | display (freq 3) |
| 13px | custom UI size (freq 3) |

> ⚠️ em-based sizes (`.875em`, `.8571429em`) 다수 — prose 플러그인 inherit. 일반 텍스트는 rem 기반.

---

## 06. Colors
<!-- SOURCE: auto -->

### 06-1. Brand
| Token | Hex | Count | Role |
|---|---|---|---|
| brand purple | `#855AFC` | 12 | ⭐ primary CTA / link hover |
| brand purple soft | shadcn alpha | - | hover state |

### 06-3. Neutral Ramp (Tailwind neutral)
| Token | Hex | Count | Role |
|---|---|---|---|
| `#FFFFFF` | 38 | page bg |
| `#FAFAFA` | 21 | bg-muted (Tailwind neutral-50) |
| `#E5E5E5` | 29 | border (neutral-200) |
| `#737373` | ~ | text muted (neutral-500) |
| `#525252` | ~ | text subtle (neutral-600) |
| `#404040` | 18 | text dark (neutral-700) |
| `#171717` | 20 | text primary (neutral-900) |
| `#000000` | 18 | stroke / logo |
| `#000000AA` | 35 | 67% alpha text |

### 06-4. Analytics Chart Palette (signature)
<!-- Dub은 link analytics 서비스 — 차트 색이 브랜드 일부 -->

| Hex | Count | Role |
|---|---|---|
| `#229DF3` | 8 | sky blue · chart series 1 |
| `#3A8BFD` | - | blue · chart series 2 |
| `#2563EB` | 9 | Tailwind blue-600 · link |
| `#34A853` | - | green · success metric |
| `#5CFF80` | - | lime · chart accent |
| `#EAB308` | - | yellow · warning metric |
| `#F4950C` | - | orange · chart accent |
| `#F35066` | 6 | pink-red · used in pink inset shadow |
| `#FF0000` | 15 | pure red · severity |

### 06-5. Semantic (shadcn slots)
| shadcn slot | Role |
|---|---|
| `--background` | page bg `#FFFFFF` |
| `--foreground` | body text |
| `--primary` | brand purple `#855AFC` |
| `--primary-foreground` | text on primary |
| `--muted` | `#FAFAFA` |
| `--muted-foreground` | `#737373` |
| `--border` | `#E5E5E5` |
| `--ring` | focus ring color |

### 06-7. Dominant Colors (실제 DOM 빈도 순)
| Rank | Hex | Count | Role |
|---|---|---|---|
| 1 | `#FFFFFF` | 38 | bg |
| 2 | `#000000AA` | 35 | 67% alpha text |
| 3 | `#E5E5E5` | 29 | border |
| 4 | `#FAFAFA` | 21 | bg-muted |
| 5 | `#171717` | 20 | text-900 |
| 6 | `#404040` | 18 | text-700 |
| 7 | `#000000` | 18 | stroke |
| 8 | `#FF0000` | 15 | severity red |
| 9 | `#855AFC` | 12 | **brand purple** |
| 10 | `#2563EB` | 9 | link blue |

---

## 07. Spacing
<!-- SOURCE: auto -->

Dub은 Tailwind spacing 유틸 사용 + 5개 custom props:
| Token | Value |
|---|---|
| `--sheet-margin` | `8px` |
| `--tw-space-*` | Tailwind 내부 |

| Class | Value |
|---|---|
| `.p-1` | 4px |
| `.p-2` | 8px |
| `.p-3` | 12px |
| `.p-4` | 16px |
| `.p-6` | 24px |
| `.p-8` | 32px |
| `.p-12` | 48px |
| `.p-16` | 64px |

---

## 08. Radius
<!-- SOURCE: auto -->

16개 unique 값 사용. 주요:
| Value | Context |
|---|---|
| `5px` | button / input |
| `8px` | small card |
| `12px` | medium card |
| `16px` | card corner |
| `9999px` | pill (stat chip, avatar) |
| `1120.477px` | Figma export floating-point (gradient 원본) |

---

## 09. Shadows
<!-- SOURCE: auto -->

| Token / Value | Usage |
|---|---|
| `--card-shadow` | 카드 기본 |
| `inset 0 1 0 0 #0000001A` | subtle inset highlight |
| `inset 0 1 0 0 #F350663A` | **pink inset hover** — Dub 시그니처 |
| single-layer subtle | 기본 카드 리프트 |

> 특이점: 핑크 알파 inset shadow `#F350663A` — 호버 시 카드 상단에 핑크 glow가 생기는 시그니처 효과.

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

### Link Card (Dub flagship)
- **Background**: `#FFFFFF`
- **Border**: `1px solid #E5E5E5`
- **Radius**: `12px` or `16px`
- **Shadow**: subtle card + optional pink inset on hover
- **Padding**: `16px 20px`
- **Short link display**: GeistMono 14px (`dub.co/abc123`)
- **Stats inline**: GeistMono 13px 숫자

### Primary CTA
- **Background**: `#171717` (neutral-900) or `#855AFC` (brand)
- **Text**: `#FFFFFF`
- **Radius**: `5px`
- **Font**: Satoshi 14px / 600
- **Padding**: `8px 16px`

### Analytics Chart
- **Axis**: GeistMono 11px #737373
- **Series 1**: `#229DF3`
- **Series 2**: `#34A853`
- **Series 3**: `#EAB308`
- **Grid**: `#E5E5E5`
- **Tooltip bg**: `#171717` / text `#FFFFFF`

### Stat chip (pill)
- **Background**: `#FAFAFA`
- **Border**: `1px solid #E5E5E5`
- **Radius**: `9999px` (pill)
- **Font**: GeistMono 12px / 500
- **Padding**: `4px 10px`

### Create link modal
- Shadcn Dialog 컴포넌트 기반
- `#FFFFFF` bg, `#E5E5E5` border, `16px` radius
- 24px padding
- Input with Satoshi labels, Inter placeholders

---

## 15. Drop-in CSS
<!-- SOURCE: auto+manual -->

```css
/* Dub.co — copy into your root stylesheet */
:root {
  /* Fonts (3-way) */
  --font-satoshi:    "Satoshi", "Satoshi Fallback", system-ui, sans-serif;
  --font-inter:      "Inter", ui-sans-serif, system-ui, -apple-system, sans-serif;
  --font-geist-mono: "GeistMono", ui-monospace, SFMono-Regular, "Roboto Mono", Menlo, monospace;

  /* Neutral (Tailwind ramp) */
  --bg:          #FFFFFF;
  --bg-muted:    #FAFAFA;
  --border:      #E5E5E5;
  --text:        #171717;
  --text-alpha:  rgba(0, 0, 0, 0.67);
  --text-muted:  #737373;
  --text-subtle: #525252;

  /* Brand */
  --brand:       #855AFC;
  --link:        #2563EB;

  /* Analytics chart palette */
  --chart-1: #229DF3;
  --chart-2: #34A853;
  --chart-3: #EAB308;
  --chart-4: #F4950C;
  --chart-5: #F35066;
  --chart-6: #5CFF80;

  /* Radius */
  --radius-sm:   5px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-xl:   16px;
  --radius-full: 9999px;

  /* Shadow */
  --card-shadow: 0 1px 2px rgba(0, 0, 0, 0.05), 0 4px 10px rgba(0, 0, 0, 0.03);
  --shadow-pink-inset: inset 0 1px 0 0 rgba(243, 80, 102, 0.23);
}

body {
  font-family: var(--font-inter);
  font-weight: 400;
  background: var(--bg);
  color: var(--text);
}

h1, h2, h3, .display { font-family: var(--font-satoshi); font-weight: 700; letter-spacing: -0.02em; }
.stat, .short-link, code { font-family: var(--font-geist-mono); }
```

---

## 16. Tailwind Config
<!-- SOURCE: auto+manual -->

```js
// tailwind.config.js — Dub.co
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#855AFC',
        },
        chart: {
          1: '#229DF3',
          2: '#34A853',
          3: '#EAB308',
          4: '#F4950C',
          5: '#F35066',
          6: '#5CFF80',
        },
        // neutral: Tailwind 기본 유지
      },
      fontFamily: {
        satoshi: ['"Satoshi"', '"Satoshi Fallback"', 'system-ui', 'sans-serif'],
        sans:    ['"Inter"', 'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
        mono:    ['"GeistMono"', 'ui-monospace', 'SFMono-Regular', '"Roboto Mono"', 'Menlo', 'monospace'],
      },
      fontWeight: {
        thin:    '100',
        light:   '300',
        normal:  '400',
        medium:  '500',
        semibold:'600',
        bold:    '700',
        heavy:   '800',
        black:   '900',
      },
      borderRadius: {
        sm:   '5px',
        md:   '8px',
        lg:   '12px',
        xl:   '16px',
        full: '9999px',
      },
      boxShadow: {
        card: '0 1px 2px rgba(0, 0, 0, 0.05), 0 4px 10px rgba(0, 0, 0, 0.03)',
        'pink-inset': 'inset 0 1px 0 0 rgba(243, 80, 102, 0.23)',
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
| Brand | `#855AFC` |
| Page BG | `#FFFFFF` |
| Text Primary | `#171717` |
| Default Theme | light |

### Component Prompts

> **Hero section**: "Dub.co 스타일 hero — `Satoshi` 폰트, `#855AFC` brand color, light 배경"
>
> **CTA button**: "Dub.co primary CTA — brand `#855AFC` 배경 또는 dark fill, `Satoshi` 폰트"
>
> **Card component**: "Dub.co 스타일 카드 — light 테마, 기존 radius/shadow 토큰 준수"

### Iteration Guide

1. **Color 교체 시**: 반드시 §06 Colors 테이블의 실제 hex 참조. AI 추론 색상 사용 금지.
2. **Typography 변경 시**: §04 Font Stack의 font-family 체인 + §05의 weight/size 매핑 확인.
3. **Spacing 조정 시**: §07 Spacing의 토큰 스케일 내에서만 변경.
4. **신규 컴포넌트**: §13 Components의 기존 패턴(radius, shadow, padding)을 기반으로 확장.

---

## 18. DO / DON'T
<!-- SOURCE: manual -->

### ✅ DO
- **3-폰트 분리**: <b>Satoshi</b> (display/heading) + <b>Inter</b> (body) + <b>GeistMono</b> (stats/short link/code).
- 정확한 brand purple **`#855AFC`** (`#7B61FF` 아님).
- shadcn/ui 기반 HSL channel token 시스템 (<code>hsl(var(--primary)/50%)</code>).
- Tailwind neutral ramp 그대로 사용 (<code>#FFFFFF</code> → <code>#171717</code>).
- Analytics chart palette 6색: <code>#229DF3</code>, <code>#34A853</code>, <code>#EAB308</code>, <code>#F4950C</code>, <code>#F35066</code>, <code>#5CFF80</code>.
- Short link 표시는 반드시 `GeistMono` — link analytics 서비스의 브랜드 포인트.
- Radius `5px`(button) / `12-16px`(card) / `9999px`(pill).
- Pink inset shadow `inset 0 1 0 0 #F350663A`를 hover signature로.
- `#000000AA` (67% alpha) — 실제 text 주력.

### ❌ DON'T
- ❌ `#7B61FF` 브랜드 퍼플 (실제는 `#855AFC` — 10 유닛 차이).
- ❌ `Inter` 단독 — Satoshi 누락 시 premium SaaS 감성 소실.
- ❌ Stat 숫자를 Inter로 — 반드시 `GeistMono`.
- ❌ `color-brand` / `color-gray-*` flat 네이밍 — shadcn HSL slot 사용.
- ❌ `#F9FAFB` (실제 0회) — Tailwind `#FAFAFA` (neutral-50) 사용.
- ❌ `#6B7280` text-muted — 실제는 `#737373` / `#525252`.
- ❌ Heavy multi-layer shadow — Dub은 subtle card + pink inset hover.
- ❌ 단일 brand color — analytics chart 6색 페어링 고려.
