# DesignMD Writer — Workflow & Methodology

> URL 하나를 입력받아 실제 사이트 CSS 기반의 독립 레퍼런스 문서
> (`DESIGN.claude.manual.md` + `report.ko.html`)를 생성하는 전체 파이프라인.
> Stripe를 포함한 34개 서비스에 검증된 절차.

---

## 0. 개요

### 목표
실제 사이트 HTML/CSS 를 수집 → 디자인 토큰 추출 → 멀티모달 시각 검증 → Claude Code 가 바로 사용할 수 있는 레퍼런스 문서 생성.

### 핵심 원칙
1. **Facts from CSS, not from screenshots of screenshots** — 값은 반드시 실제 번들 CSS 에서 파싱, AI 추론/환각 금지
2. **템플릿 v2.0 일관성** — 16개 섹션, YAML frontmatter 맨 위, 선택 섹션은 `<!-- OPTIONAL -->` 마커로 표시
3. **독립 레퍼런스** — 기존 어떤 소스와도 비교하지 않는 독립 문서. "X가 주장했지만…" 같은 표현 금지
4. **Korean 톤** — 리포트/설명은 한국어, 토큰명/CSS 값/변수명은 원본 그대로

### 결과물 (서비스당 2개 파일)
```
real/{slug}/
├── DESIGN.claude.manual.md  — YAML frontmatter + 16 섹션 마크다운 (~10-25KB)
└── report.ko.html            — 인터랙티브 HTML 리포트 (~25-75KB)
```

---

## 1. 입력 요구사항

### 필수
- **URL 하나** (예: `https://stripe.com`)
- **slug** (예: `stripe`) — 디렉토리명으로 사용

### 선택
- **서비스 이름** (예: `Stripe`) — URL 에서 자동 추론 가능

---

## 2. Phase 1: 데이터 수집 (~5분)

### 2.1 HTML 홈페이지 수집

```bash
curl -sL \
  -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -o "designmd-data/real/{slug}/index.html" \
  "https://{site_url}"
```

**주의**: User-Agent 없이 curl 하면 bot 차단당하는 사이트가 많다. Chrome UA 필수.

### 2.2 외부 CSS 파일 수집

```bash
# HTML 에서 stylesheet 링크 추출
grep -oE '<link[^>]+rel="stylesheet"[^>]+href="[^"]+"' index.html | \
  grep -oE 'href="[^"]+"' | sed 's/href="//;s/"$//'

# 병렬 다운로드 (최대 10개 동시)
cat css-urls.txt | xargs -n1 -P10 -I{} curl -sL -o "css/$(basename {})" "{}"
```

**재시도 로직**: CDN 오류 시 (`curl exit 56` 등) 최대 3회 재시도.

### 2.3 스크린샷 확보 (선택)

`designmd-data/assets/screenshots/{slug}.jpg` — DesignMD 쇼케이스에서 미리 받은 1280×800 스크린샷이 있으면 사용. 없으면 Playwright 로 캡처:

```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    page.goto(site_url)
    page.screenshot(full_page=True, path="fullpage.png")
    page.screenshot(path="hero.png")
```

### 2.4 수집 검증 체크리스트

- [ ] `index.html` 크기 > 5KB (일부 SPA 는 JS 렌더링이라 HTML 이 거의 빈 경우 있음 — 그럴 땐 Playwright 로 rendered HTML 저장)
- [ ] CSS 파일 ≥ 1개
- [ ] 총 CSS 크기 > 5KB

---

## 3. Phase 2: CSS 파싱 (~10분)

### 3.1 CSS 커스텀 프로퍼티 전수 추출

```python
import re
vars_ = re.findall(r'--([a-zA-Z0-9_-]+)\s*:\s*([^;}]+)', all_css)
# → dict: {var_name: raw_value}
```

### 3.2 토큰 prefix 감지

```python
from collections import Counter
prefixes = Counter()
for name in props:
    parts = name.split("-", 2)
    if len(parts) >= 2 and len(parts[0]) <= 4:
        prefixes[parts[0]] += 1
# 가장 빈번한 prefix = 해당 사이트의 design system namespace
# 예: Stripe → --hds-*, Vercel → --ds-* / --geist-*
```

### 3.3 컬러 램프 그룹핑

```python
import re
ramps = {}  # "prefix-family": {step: hex}
for name, val in props.items():
    if not re.match(r'^#[0-9a-fA-F]{3,8}$', val.strip()):
        continue
    m = re.match(r'(.+?)-([a-zA-Z]+)-(\d+)$', name)
    if m:
        prefix, family, step = m.groups()
        key = f"{prefix}-{family}"
        ramps.setdefault(key, {})[step] = val.strip()
# 결과: brand, brandDark, neutral, neutralDark, success, error 등
```

### 3.4 타이포그래피 스케일 추출

```python
import re
typo = {}  # "category-variant": {size, weight, lineHeight, letterSpacing}
for name, val in props.items():
    m = re.match(
        r'.*font-(heading|text|display|body|title|label|caption|input|quote)-?([a-zA-Z0-9]*)-(size|weight|lineHeight|line-height|letterSpacing|letter-spacing)$',
        name
    )
    if m:
        cat, variant, prop = m.groups()
        key = f"{cat}-{variant or 'base'}"
        typo.setdefault(key, {})[prop] = val.strip()
```

### 3.5 스페이싱 토큰 추출

```python
spacing = {}
for name, val in props.items():
    if re.search(r'space|spacing', name, re.I) and re.match(r'^[\d.]+(px|rem)$', val.strip()):
        spacing[name] = val.strip()
```

### 3.6 Radius / Shadow 추출

- `border-radius` 선언 값 수집 → Counter
- `box-shadow` 선언 값 수집 → 복수 레이어 감지
- `--*-radius-*`, `--*-shadow-*` 변수 수집

### 3.7 폰트 family 빈도

```python
fam_counter = Counter()
for m in re.finditer(r'font-family\s*:\s*([^;{}]+)', css):
    fam = m.group(1).strip()
    if fam.startswith('var('):
        continue
    first = re.match(r'\s*["\']?([A-Za-z][A-Za-z0-9 _-]+)["\']?', fam)
    if first:
        fam_counter[first.group(1).strip()] += 1
# 상위 5개가 해당 사이트의 실제 폰트
```

### 3.8 BEM 클래스 추출 (HTML)

```python
class_counter = Counter()
for m in re.finditer(r'class="([^"]+)"', html):
    for c in m.group(1).split():
        if re.match(r'[a-z][a-z0-9]*[-_]{1,2}[a-z]', c):
            class_counter[c] += 1
# 상위 25개 중 의미 있는 패턴 선택 (button/heading/link 등)
```

### 3.9 var() 체인 해결 (optional)

```python
def resolve(name, props, seen=None):
    if seen is None: seen = set()
    if name in seen: return None  # cycle
    seen.add(name)
    val = props.get(name)
    if not val: return None
    m = re.match(r'var\(--([^,)]+)(?:,\s*([^)]+))?\)', val)
    if m:
        ref = m.group(1).strip()
        fallback = m.group(2)
        resolved = resolve(ref, props, seen)
        if resolved: return resolved
        if fallback: return fallback.strip()
        return None
    return val.strip()
# util-action-bg-solid → core-brand-600 → #533AFD
```

---

## 4. Phase 3: 시각 검증 (~2분)

### 4.1 Light/Dark 테마 판정

1. 스크린샷 열기
2. Hero 영역 배경색 확인
3. Luminance 계산: `0.299R + 0.587G + 0.114B`
   - `> 0.9` → **light**
   - `< 0.1` → **dark**
   - 사이 → **mixed**
4. 스크린샷에서 "전체가 다크인지, 섹션별로 번갈아 가는지" 눈으로 확인

**⚠️ 함정**: frequency 1위 hex 가 `#FFFFFF` 이라고 light 단정 금지. Hero 를 다크로 쓰는 사이트(GitHub, Linear 등)도 body 안쪽에 흰 카드가 많다.

### 4.2 브랜드 컬러 확정

- Phase 2 에서 추출한 `brand-600` 또는 `primary-*` 변수의 hex
- 크로스체크: `top_hex_by_frequency` 상위 10개 + CTA 버튼 selector 안쪽 hex
- 두 소스가 일치하면 confidence: **high**
- 한쪽만 일치하면 스크린샷으로 최종 확인

### 4.3 폰트 시각적 검증

- Phase 2 의 폰트 family 빈도 top 5 확인
- 커스텀 폰트 식별:
  - `sohne-var`, `Mona Sans`, `Geist`, `Berkeley Mono`, `Circular`, `figmaSans`, `Salesforce-Sans` 등 → 유료/커스텀
  - `Inter`, `Roboto`, `Source Sans Pro`, `JetBrains Mono` → 오픈
- 스크린샷에서 폰트 특성 확인 (특히 얇은 weight, 특이한 a/g 형태)

### 4.4 DS 네임스페이스 확인

- `--hds-*` (Stripe HDS), `--ds-*` (Vercel), `--framer-*` (Framer), `--color-cocoaDarkBrown` (Convex) 등
- 단일 prefix 가 지배적이면 그게 이 사이트의 design system namespace

---

## 5. Phase 4: DESIGN.claude.manual.md 작성 (~20-30분)

### 5.1 파일 구조

```markdown
---
slug: {slug}
service_name: {Service Name}
site_url: {URL}
fetched_at: {YYYY-MM-DD}
default_theme: {light|dark|mixed}
brand_color: "#XXXXXX"
primary_font: {font name}
font_weight_normal: {N}
token_prefix: {prefix}
---

# DESIGN.md — {Service Name} (Claude Code Edition)

---

## 01. Quick Start
<!-- SOURCE: manual -->

> 5분 안에 {Service}처럼 만들기 — 3가지만 하면 80%

```css
/* 1. 폰트 */
/* 2. 배경+텍스트 */
/* 3. 브랜드 컬러 */
```

**절대 하지 말아야 할 것 하나**: {가장 치명적인 실수}

## 02. Provenance
## 03. Tech Stack
## 04. Font Stack
## 05. Typography Scale
## 06. Colors
  ### 06-1. Brand Ramp
  ### 06-2. Brand Dark Variant  <!-- OPTIONAL -->
  ### 06-3. Neutral Ramp
  ### 06-4. Accent Families  <!-- OPTIONAL -->
  ### 06-5. Semantic
  ### 06-6. Semantic Alias Layer
  ### 06-7. Dominant Colors
## 07. Spacing
## 08. Radius
## 09. Shadows  <!-- OPTIONAL if no shadow system -->
## 10. Motion  <!-- OPTIONAL -->
## 11. Layout Patterns  <!-- OPTIONAL -->
## 12. Components
## 13. Content / Copy Voice  <!-- OPTIONAL -->
## 14. Drop-in CSS
## 15. Tailwind Config  <!-- OPTIONAL -->
## 16. DO / DON'T
```

### 5.2 필수 섹션 (10개 — 데이터 없어도 반드시 존재)

| # | 섹션 | 출처 |
|---|---|---|
| 01 | Quick Start | manual |
| 02 | Provenance | auto |
| 03 | Tech Stack | auto+manual |
| 04 | Font Stack | auto+manual |
| 05 | Typography Scale | auto |
| 06 | Colors | auto |
| 07 | Spacing | auto |
| 08 | Radius | auto |
| 12 | Components | auto+manual |
| 14 | Drop-in CSS | auto+manual |
| 16 | DO / DON'T | manual |

### 5.3 선택 섹션 (6개 — 데이터 없으면 통째로 제거)

| # | 섹션 | 제거 조건 |
|---|---|---|
| 09 | Shadows | `box-shadow` 변수/선언 없음 |
| 10 | Motion | transition/animation 토큰 없음 |
| 11 | Layout Patterns | breakpoint/grid 정보 부족 |
| 13 | Content / Copy Voice | manual 분석 생략 |
| 15 | Tailwind Config | tailwind.config 유도 어려움 |
|  | 06-2 Brand Dark Variant | 다크 시리즈 없음 |
|  | 06-4 Accent Families | accent 패밀리 없음 |

### 5.4 Quick Start (§01) 작성 규칙

가장 중요한 세 가지를 CSS 스니펫으로:
1. **폰트 + weight**
2. **배경 + 텍스트 색** (light 또는 dark)
3. **브랜드 컬러**

그리고 **"절대 하지 말아야 할 것 하나"** — 이 서비스에서 가장 치명적인 한 가지 실수:
- Stripe → "body weight 300 (400 아님)"
- Warp → "light 테마 (cream/ivory). dark 아님"
- Notion → "warm ink `#37352F` (순흑 아님)"
- Retool → "크림 + 보르도 (orange 아님, 리브랜딩 반영)"

### 5.5 작성 원칙

- **영어 토큰명 + 한국어 설명**: `--hds-color-core-brand-600` 같은 식별자는 원본, "이 보라는 brand-600 과 brandDark-600 둘 다에 고정되어 있다" 같은 설명은 한국어
- **구체 수치**: "살짝 높은 편" ❌ → "18px 기준 line-height 1.45" ✅
- **출처 명시**: §02 Provenance 에 fetched_at, CSS 바이트 수, CDN URL 등
- **독립성**: 다른 소스와 비교하는 문장 금지

---

## 6. Phase 5: HTML 리포트 생성 (~15-20분)

### 6.1 베이스 템플릿

`real/stripe/report.ko.html` 이 gold standard. 구조:

```html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{Service} — 디자인 시스템 리포트</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter&family=JetBrains+Mono&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
  <style>
    /* shadcn-style neutral (zinc) theme */
    :root {
      --font-sans: "Pretendard Variable", Inter, -apple-system, sans-serif;
      --font-mono: "JetBrains Mono", ui-monospace, Menlo, monospace;
      --background: #fafafa;
      --foreground: #09090b;
      --card: #ffffff;
      --muted: #f4f4f5;
      --muted-foreground: #71717a;
      --border: #e4e4e7;
      --accent: #18181b;
      --radius: 0.5rem;
    }
    /* ... 나머지 스타일 ... */
  </style>
</head>
<body>
  <div class="layout">
    <!-- Sidebar TOC -->
    <nav class="toc">...</nav>
    <!-- Main -->
    <main class="main">
      <section id="hero">...</section>
      <section id="provenance">...</section>
      <section id="stack">...</section>
      <section id="typography">...</section>
      <section id="colors">...</section>
      <section id="spacing">...</section>
      <section id="radius">...</section>
      <section id="shadows">...</section>
      <section id="components">...</section>
      <section id="verdict">...</section>
    </main>
  </div>
</body>
</html>
```

### 6.2 HTML 리포트 ↔ DESIGN.md 매핑

| DESIGN.md 섹션 | HTML 리포트 섹션 |
|---|---|
| §01 Quick Start | `#hero` (TL;DR 포함) |
| §02 Provenance | `#provenance` |
| §03 Tech Stack | `#stack` |
| §04 Font Stack + §05 Typography Scale | `#typography` (합쳐짐) |
| §06 Colors | `#colors` |
| §07 Spacing | `#spacing` |
| §08 Radius | `#radius` |
| §09 Shadows | `#shadows` |
| §12 Components | `#components` |
| §16 DO/DON'T | `#verdict` |

§10 Motion, §11 Layout, §13 Content Voice, §14 Drop-in CSS, §15 Tailwind 는 리포트에서 제외 (별도 문서에서 참조).

### 6.3 인터랙티브 요소 필수

- **컬러 스와치**: 호버 시 hex 표시, 클릭 시 복사
- **타이포그래피 live preview**: 실제 폰트 스케일로 렌더링
- **스페이싱 시각 바**: 토큰 값을 px 너비로 막대 표현
- **Radius 시각 박스**: 각 단계를 실제 적용한 박스
- **Shadow 시각 카드**: box-shadow 를 그대로 적용한 데모 카드

### 6.4 스타일 가이드

- **테마**: shadcn-style neutral (zinc palette), light-first
- **폰트**: Pretendard Variable (한글) + Inter (라틴) + JetBrains Mono (code)
- **레이아웃**: 좌측 260px 고정 TOC + 우측 flexible main
- **언어**: 한국어 (token 이름/CSS 값/변수명은 영문 그대로)
- **section padding**: 72px 64px

### 6.5 파일 크기 기준

- HTML ≥ 20KB (인터랙티브 요소 포함)
- 일반적으로 25-75KB 범위

---

## 7. Phase 6: 품질 검증

### 7.1 자동 체크 (스크립트)

```bash
# 1. YAML frontmatter 맨 위 있는가?
head -1 DESIGN.claude.manual.md | grep -q '^---$'

# 2. 필수 섹션 모두 있는가?
for n in 01 02 03 04 05 06 07 08 12 14 16; do
  grep -q "^## $n\\." DESIGN.claude.manual.md || echo "Missing §$n"
done

# 3. 파일 크기 기준
[ $(wc -c < DESIGN.claude.manual.md) -ge 8000 ]
[ $(wc -c < report.ko.html) -ge 20000 ]

# 4. 독립성 체크 — 외부 소스 비교 표현 없는가?
grep -ci "designmd\|previously claimed" DESIGN.claude.manual.md  # 0이어야 함

# 5. hex 실존 검증 — 주요 hex 가 실제 CSS 에 있는가?
for hex in $(grep -oE '#[0-9A-F]{6}' DESIGN.claude.manual.md | sort -u | head -5); do
  grep -qi "$hex" designmd-data/real/{slug}/css/*.css || echo "Missing: $hex"
done
```

### 7.2 수동 체크 (샘플링)

- 랜덤 1-2개 파일 열어서 읽기
- Quick Start 가 실제로 80% 느낌을 내는가?
- 톤이 한국어로 자연스러운가?
- 토큰명이 원본 그대로인가? (가상 토큰명 `color-brand` 같은 거 없어야 함)

---

## 8. 서비스당 총 소요 시간

| Phase | 작업 | 시간 |
|---|---|---|
| 1 | 데이터 수집 | 5분 |
| 2 | CSS 파싱 | 10분 |
| 3 | 시각 검증 | 2-5분 |
| 4 | DESIGN.claude.manual.md 작성 | 20-30분 |
| 5 | HTML 리포트 생성 | 15-20분 |
| 6 | 품질 검증 | 5분 |
| **합계** | | **~1시간/서비스** |

4명의 분석가가 병렬로 처리하면 34개 서비스 → **약 8-10시간**.

---

## 9. 발견된 함정 14가지 (이전 감사 기록)

다음 패턴이 나오면 특히 조심:

1. **가상 토큰명** — `color-brand`, `space-1` 같은 이름은 어떤 사이트에도 없다. 실제는 prefix-scoped.
2. **브랜드 키트 vs UI 색 혼동** — 로고 5색은 일러스트 전용, 실제 UI 는 그걸 거의 안 쓴다 (Figma, Slack).
3. **리브랜딩 지체** — Atlassian `#0052CC` → `#1868DB`, Prisma indigo → teal, Retool orange → cream/bordeaux.
4. **Light/Dark 역전** — Warp 는 light 마케팅 사이트인데 제품 UI 만 보고 dark 로 착각하기 쉽다.
5. **앱 UI vs 마케팅 사이트 레이어 혼동** — Linear, Framer, GitHub 은 이 둘이 다른 팔레트.
6. **Hero Specification 블라인드** — 구체 수치(clamp, gradient angle, overlay opacity) 누락하기 쉬움.
7. **DS 네임스페이스 누락** — `--hds-*`, `--ds-*`, `--framer-*` 같은 실제 prefix 대신 일반화.
8. **Tailwind v4 `@theme` 미반영** — v4 는 `--color-*-NNN` 팔레트를 root 에 노출.
9. **next/font metric fallback 누락** — `Inter Fallback`, `Mona Sans Header Fallback` 등.
10. **Warm vs Cool neutral 구분 부재** — Notion `#37352F` warm ink, Retool `#E9EBDF` cream 등은 순흑/순백 아님.
11. **Composite multi-layer shadow 단일화** — Stripe, GitHub, Linear 는 2~5 레이어 stack.
12. **Customer logo wall hex 오염** — "trusted by" 섹션의 SVG 로고 색이 top frequency 에 침투.
13. **Letter-spacing optical compensation 누락** — 큰 headings 의 negative tracking 미언급 시 "풀어진" 느낌.
14. **Variable font 비표준 weight** — Saans `300/380/570`, ShopifySans `330/420/550` 등 일반 Inter 로 재현 불가.

---

## 10. 생성된 34개 레퍼런스

```
/Users/chulrolee/designmd-writer/real/
├── atlassian/
│   ├── DESIGN.claude.manual.md
│   └── report.ko.html
├── axiom/
├── cal/
├── clerk/
├── contentful/
├── convex/
├── discord/
├── dub/
├── figma/
├── framer/
├── github/
├── hashnode/
├── lemon-squeezy/
├── linear/
├── mintlify/
├── neon/
├── notion/
├── planetfall/            (대기 중)
├── planetscale/
├── posthog/
├── prisma/
├── railway/
├── raycast/
├── resend/
├── retool/
├── shopify/
├── slack/
├── spotify/
├── stripe/                (재작성 완료, 구 버전 대체)
├── supabase/
├── tailwindcss/
├── tinybird/
├── twitch/
├── vercel/
└── warp/                  (대기 중)
```

---

## 11. 관련 문서

- `/Users/chulrolee/designmd-writer/METHODOLOGY.md` — 분석 5단계 상세
- `/Users/chulrolee/designmd-writer/DESIGN.claude.template.md` — 템플릿 v2.0 (16섹션)
- `/Users/chulrolee/designmd-writer/real/stripe/DESIGN.claude.manual.md` — Gold standard 예시
- `/Users/chulrolee/designmd-writer/real/stripe/report.ko.html` — HTML 리포트 Gold standard
- `/Users/chulrolee/designmd-writer/.kkirikkiri/TEAM_FINDINGS.md` — 서비스별 발견 기록
- `/Users/chulrolee/designmd-writer/.kkirikkiri/archive/FINDINGS-2026-04-11-audit.md` — 이전 감사 (14가지 실패 패턴)
