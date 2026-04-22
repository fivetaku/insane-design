---
name: insane-design
description: >
  Extracts a deterministic design system from any URL by fetching real CSS, parsing custom
  properties, and generating a 19-section design.md plus an interactive HTML report. v0.2
  writes frontmatter schema_version 3.1 with medium detection (web / slide / design-system /
  card-news / motion / print). Pairs with insane-apply and insane-build via the §18 DON'T
  hex-grep contract. Korean triggers: "디자인 분석해줘", "이 사이트 디자인 시스템 뽑아줘",
  "CSS 뜯어봐", "design.md 만들어줘", "레퍼런스 리포트 만들어줘", "사이트 분석",
  "디자인 토큰 추출". English triggers: "analyze design", "extract design tokens",
  "rip the design system", "what CSS does this site use".
---

# Insane Design

> URL 하나 → 실제 CSS 기반 design.md + 인터랙티브 HTML 리포트

---

## WHEN TRIGGERED - EXECUTE IMMEDIATELY

이 문서는 참고 문서가 아니라 **실행 지시서**다.
URL이 제공되면 즉시 Step 1부터 실행한다.

---

## 사전 준비

스킬 실행 전 다음 레퍼런스를 필요한 Step에서 읽는다:

- `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/references/template.md` — design.md 19섹션 v3.1 템플릿 (§00~§18) (Step 5에서 Read)
- `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/references/report-prompt.md` — HTML 리포트 생성 규칙 v2.1 (Step 6에서 Read)
- `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/references/report.css` — canonical CSS (Step 6에서 Read, 있으면 사용)
- `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/references/pitfalls.md` — 14가지 함정 (Step 4에서 Read)
- `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/examples/stripe/design.md` — 골드 스탠다드 예시 (Step 5에서 참조)
- `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/examples/stripe/report.ko.html` — 리포트 골드 스탠다드 (Step 6에서 참조)

---

## 워크플로우 — 7 Steps

> **경로 규칙**: 모든 Bash 명령은 반드시 **프로젝트 루트에서** 실행한다.
> Step 실행 전 `WORK_DIR`을 확정하고, 모든 경로를 절대 경로 또는 `$WORK_DIR` 기준으로 사용한다.
> 모든 결과물은 `insane-design/{slug}/` 하위에 통합 저장한다.

```bash
# Step 0: 프로젝트 루트 확정 (모든 Step에서 공유)
WORK_DIR="$(pwd)"   # 사용자의 현재 디렉토리를 프로젝트 루트로 사용
```

### Step 1: INIT
**Type**: script

URL을 파싱하고 작업 환경을 준비한다.

1. URL에서 slug 추출 (도메인 → kebab-case: `stripe.com` → `stripe`, `linear.app` → `linear`)
2. URL 검증 (**보안 필수**):
   - `http://` 또는 `https://` 프로토콜 확인
   - `localhost`, `127.0.0.1`, `file://` 차단
   - 도메인 형식 유효성 확인
   - **셸 특수문자 검증**: URL에 `` ` ``, `$`, `(`, `)`, `;`, `|`, `&`, `>`, `<` 등 셸 메타문자가 포함되면 거부
   - 이후 모든 Bash 명령에서 URL은 반드시 **큰따옴표로 감싸서** 사용: `"$URL"`
3. 🆕 **매체(medium) 감지** (v3.1 frontmatter 필드용):

   | 입력 패턴 | medium | medium_confidence |
   |----------|--------|-------------------|
   | URL이 `.pptx`/`.ppt`로 끝남 | `slide` | `high` |
   | URL이 `docs.google.com/presentation/*` | `slide` | `high` |
   | URL이 `*.pdf`로 끝남 | `print` | `high` (스텁만, 현 세션 미구현) |
   | URL이 `*.figma.com/file/*` (디자인 시스템 탐지 시) | `design-system` | `medium` |
   | 이미지 업로드 입력 + 정사각 비율 | `card-news` | `medium` |
   | 그 외 일반 URL | `web` | `high` (기본값) |

   감지 결과는 Step 5 WRITE-MD에서 frontmatter `medium`, `medium_confidence` 필드에 그대로 기록한다.
4. 출력 디렉토리 생성 (**절대 경로 사용**):

```bash
mkdir -p "$WORK_DIR/insane-design/{slug}/{screenshots,css,phase1}"
```

5. 사용자에게 시작 알림:
```
🎨 {slug} 디자인 분석을 시작합니다.
URL: {url}
예상 소요: 3-5분
```

---

### Step 2: FETCH
**Type**: script

HTML/CSS와 스크린샷을 **병렬**로 수집한다.

#### 2A. HTML + CSS 수집

5-tier fallback 체인으로 HTML 홈페이지를 수집한다:

```bash
# Tier 1: curl + Chrome UA (절대 경로)
# ⚠️ URL은 Step 1에서 검증 완료된 값만 사용. 반드시 큰따옴표로 감쌈.
URL="{url}"  # Step 1에서 검증된 URL
curl -sL \
  -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -H "Accept: text/html,application/xhtml+xml" \
  -H "Accept-Language: en-US,en;q=0.9" \
  --compressed --max-time 30 \
  -o "$WORK_DIR/insane-design/{slug}/index.html" \
  "$URL"
```

성공 판정: 파일 크기 ≥ 5KB + `<html>` 태그 존재 + Cloudflare challenge 없음.
실패 시 Tier 2(Mobile UA) → Tier 3(Jina HTML mode: `curl -H "X-Return-Format: html" "https://r.jina.ai/$URL"`) 순서로 시도.

> **⚠️ 외부 API 고지**: Tier 3에서 Jina Reader API(`r.jina.ai`)와 Step 2B 스크린샷 수집에서 대상 URL이 외부 서비스로 전송됩니다. 민감한 내부 URL에는 사용하지 마세요.

HTML에서 CSS 링크 추출 + 병렬 다운로드:
```bash
# 1. CSS 링크 추출 (상대/절대 URL 모두)
grep -oE 'href="[^"]+\.css[^"]*"' "$WORK_DIR/insane-design/{slug}/index.html" | \
  sed 's/href="//;s/"$//' > "$WORK_DIR/insane-design/{slug}/css/_urls.txt"

# 2. 상대 경로 → 절대 URL 변환 후 병렬 다운로드
BASE_URL="{url}"  # Step 1에서 검증된 URL
while IFS= read -r css_href; do
  # 절대 URL이면 그대로, 상대 경로면 BASE_URL과 결합
  case "$css_href" in
    http*) abs_url="$css_href" ;;
    //*) abs_url="https:$css_href" ;;
    /*) abs_url="$(echo "$BASE_URL" | grep -oE 'https?://[^/]+')$css_href" ;;
    *) abs_url="$BASE_URL/$css_href" ;;
  esac
  fname="$(echo "$css_href" | sed 's/[?#].*//' | xargs basename)"
  curl -sL --max-time 15 -o "$WORK_DIR/insane-design/{slug}/css/$fname" "$abs_url" &
done < "$WORK_DIR/insane-design/{slug}/css/_urls.txt"
wait
rm -f "$WORK_DIR/insane-design/{slug}/css/_urls.txt"
```

#### 2B. 스크린샷 수집 (병렬)

```bash
# Jina Reader API로 스크린샷 캡처
# ⚠️ 프라이버시 고지: 대상 URL이 Jina Reader API (r.jina.ai)로 전송됩니다.
#    Jina는 이를 Puppeteer로 렌더링 후 스크린샷을 반환합니다.
#    민감한 내부 URL에는 사용하지 마세요.
# ⏱️ X-Wait-For: 5000 → 페이지 로드 후 5초 대기 (애니메이션/lazy load 완료 보장)
curl -sL \
  -H "X-Respond-With: screenshot" \
  -H "X-Wait-For: 5000" \
  --max-time 45 \
  "https://r.jina.ai/$URL" \
  -o "$WORK_DIR/insane-design/{slug}/screenshots/jina-hero.png"

# PIL crop (1280×1280 → 1280×800)
python3 -c "
from PIL import Image
img = Image.open('$WORK_DIR/insane-design/{slug}/screenshots/jina-hero.png')
w, h = img.size
cropped = img.crop((0, 0, w, min(800, h)))
cropped.save('$WORK_DIR/insane-design/{slug}/screenshots/hero-cropped.png')
"
```

Jina Reader 실패 시 (파일 < 5KB) → Playwright fallback 시도:
```bash
# Playwright fallback — networkidle 대기 + 추가 3초 딜레이
python3 -c "
from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 800})
    page.goto('$URL', wait_until='networkidle', timeout=30000)
    time.sleep(3)  # 애니메이션/lazy load 완료 대기
    page.screenshot(path='$WORK_DIR/insane-design/{slug}/screenshots/jina-hero.png')
    browser.close()
"
```

#### 수집 실패 처리

- HTML 5-tier 전부 실패 → 사용자에게 "접근 불가" 메시지 + 중단
- CSS 0개 → 인라인 `<style>` 블록 추출 시도
- 스크린샷 실패 → 경고 후 계속 진행 (스크린샷 없어도 design.md 생성 가능)

---

### Step 3: EXTRACT
**Type**: script

CSS에서 디자인 토큰을 추출한다. 4개 스크립트를 `$WORK_DIR`에서 순차 호출:

```bash
cd "$WORK_DIR"

python3 "${CLAUDE_PLUGIN_ROOT}/skills/insane-design/scripts/brand_candidates.py" {slug}
python3 "${CLAUDE_PLUGIN_ROOT}/skills/insane-design/scripts/var_resolver.py" {slug}
python3 "${CLAUDE_PLUGIN_ROOT}/skills/insane-design/scripts/typo_extractor.py" {slug}
python3 "${CLAUDE_PLUGIN_ROOT}/skills/insane-design/scripts/alias_layer.py" {slug}
```

결과: `$WORK_DIR/insane-design/{slug}/phase1/` 에 4개 JSON:
- `brand_candidates.json` — 브랜드 색상 후보 (semantic + selector-role + frequency)
- `resolved_tokens.json` — var() 체인 해결된 토큰
- `typography.json` — 타이포 스케일 (heading/text/input/quote)
- `alias_layer.json` — tier 분류 (util/action/component/core)

> **§11 Layout / §12 Responsive / §13 Components는 스크립트로 추출하지 않는다.**
> 사이트마다 CSS 구조가 완전히 다르므로 범용 파서가 불가능하다.
> Step 4에서 Claude가 CSS를 직접 읽고 AI 판단으로 분석한다.

#### 추출 실패 처리

CSS custom properties 0개면:
- "CSS 토큰 부족 — Tailwind/CSS-in-JS 사이트일 수 있습니다. 빈도 기반 hex 분석으로 대체합니다." 경고
- hex frequency 기반 분석으로 전환 (brand_candidates.json의 frequency_candidates 활용)

---

### Step 4: INTERPRET
**Type**: prompt (멀티모달)

Claude가 스크린샷 + 추출 결과 + **CSS 원본**을 직접 읽고 AI 판정을 수행한다.

1. Read: `insane-design/{slug}/screenshots/hero-cropped.png` (또는 `jina-hero.png`)
2. Read: `insane-design/{slug}/phase1/brand_candidates.json`
3. Read: `insane-design/{slug}/phase1/typography.json`
4. Read: `insane-design/{slug}/phase1/alias_layer.json`
5. Read: `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/references/pitfalls.md` — 14가지 함정
6. Read: `insane-design/{slug}/index.html` — HTML 구조 직접 확인 (§11/§13용)
7. Read: `insane-design/{slug}/css/` 주요 CSS 파일 — 레이아웃/컴포넌트 직접 분석 (§11/§12/§13용)

> **§11/§12/§13은 스크립트가 아니라 Claude가 직접 CSS를 읽고 분석한다.**
> 사이트마다 클래스명, 레이아웃 방식, 컴포넌트 구조가 전부 다르기 때문에
> 범용 파서가 아닌 AI 해석이 필요하다.
> CSS 파일이 너무 크면 (>500KB) 상위 2-3개 파일만 읽되, 주요 패턴을 파악한다.

**판정 항목 (16가지)** — 🆕 v3.1: BOLD 방향성 4개 추가 (apply Lv3 지원):

| # | 판정 | 출력 |
|---|---|---|
| 1 | Brand color 확정 | hex (예: `#533AFD`) |
| 2 | Light/Dark 테마 | `light` / `dark` / `mixed` |
| 3 | Custom font 식별 | `sohne-var = 유료`, `Inter = 오픈` 등 |
| 4 | Framework 식별 | `Next.js + HDS`, `Tailwind v4` 등 |
| 5 | Hero anatomy 서술 | "2-column, gradient flame bg" 등 |
| 6 | Quick Start "절대 하지 말 것" | 가장 치명적인 한 가지 |
| 7 | DO/DON'T | 각 4~8 항목 (**색상 DON'T는 hex 명시 강제**) |
| 8 | §00 Visual Theme & Atmosphere | 3~5문단 서술 + BOLD Direction Summary 블록 |
| 9 | §11 Layout Patterns 분석 | Grid, Hero(+Pattern Summary, BG Treatment), Section, Card, Nav 구조 |
| 10 | §12 Responsive Behavior | 브레이크포인트, 터치 타겟, 접기 전략 |
| 11 | §13 Components 확장 | 카드, 네비, 인풋, 히어로 컴포넌트 |
| 12 | §17 Agent Prompt Guide | Quick Color Reference + 프롬프트 예시 |
| **13** | **🆕 BOLD 방향성** | 1~2 단어 (예: `Industrial Minimalism`, `Refined SaaS`) |
| **14** | **🆕 Aesthetic Category** | redesign-aesthetics.md §3 12가지 중 1개 |
| **15** | **🆕 Signature Element** | `hero_impact` / `typo_contrast` / `section_transition` / `minimal_extreme` |
| **16** | **🆕 Code Complexity** | `low` / `medium` / `high` / `very_high` + 근거 한줄 |

#### 🆕 BOLD 방향성 매핑 판단 트리 (판정 #13~16)

`${CLAUDE_PLUGIN_ROOT}/skills/insane-apply/references/redesign-aesthetics.md` §3을 먼저 Read.

**판정 #13 (BOLD 방향성) 결정 알고리즘:**

```
1. 채도 측정: brand_candidates.json 최빈 chromatic hex의 HSL 채도(%)
2. 레이아웃 밀도: §11 grid-columns × card-count 추산 (low / medium / high)
3. 톤 키워드: §00 1문단의 핵심 단어 (warm / cool / neon / monochrome / industrial)

매핑 규칙:
- 채도 <15% + 밀도 낮음                → "Industrial Minimalism" / "Monochrome Luxury"
- 채도 <15% + 밀도 높음                → "Brutalist Raw" / "Cool Productivity"
- 채도 50-80% + 밀도 낮음              → "Refined SaaS" / "Friendly Fintech"
- 채도 >80% + 밀도 높음                → "Playful Gradient" / "Maximalist Chaos"
- warm 키워드 + 낮은 채도              → "Warm Productivity" / "Editorial Magazine"
- neon 키워드 + dark 테마              → "Retro-Futuristic"
- pastel 키워드                        → "Soft Pastel"

12가지 중 가장 부합하는 1개 선택. 두 가지 사이면 더 극단적인 것.
```

**판정 #15 (Signature Element) 결정 기준:**

| Signature | 적용 조건 |
|-----------|----------|
| `hero_impact` | Hero가 100vh 풀스크린, 큰 H1, 강한 contrast (Apple, Tesla) |
| `typo_contrast` | display vs body 10배 이상 사이즈 차이 (Stripe, Editorial Magazine) |
| `section_transition` | 섹션마다 배경 톤 drastic 변화 (Notion, Discord) |
| `minimal_extreme` | 장식 완전 제거, 색 3개 이내 (Vercel, Brutalist) |

**판정 #16 (Code Complexity) 결정 기준:**

| Complexity | 미학 예시 | 근거 |
|-----------|----------|------|
| `low` | Refined Minimalism, Brutalist | CSS 변수 + 1개 transition + 절제된 hover |
| `medium` | Industrial Minimalism, Editorial | + staggered reveal, IntersectionObserver |
| `high` | Playful Gradient, Refined SaaS | + 다층 그라디언트, hover bounce, 풍부한 transitions |
| `very_high` | Maximalist Chaos | + parallax, scroll-triggered, particle, custom cursor |

**Step 5 WRITE-MD에서:**
- frontmatter에 4개 필드(`bold_direction`, `aesthetic_category`, `signature_element`, `code_complexity`) 채움
- §00 끝에 `### BOLD Direction Summary` 블록 4줄 추가

#### §00 Visual Theme & Atmosphere 작성 (판정 #8)

스크린샷 + tokens.json(brand_candidates, typography, alias_layer) 기반으로 브랜드 분위기와 디자인 철학을 **3~5문단**으로 서술한다.

작성 구조:
- **1문단**: 전반적 분위기와 디자인 철학 (예: "차갑고 기술적이면서도 친근한 fintech 톤")
- **2문단**: 색상 사용 전략 (브랜드 컬러 역할, 배경/전경 대비, 뉴트럴 활용)
- **3문단**: 타이포그래피 성격 (폰트 선택 이유, weight 활용, 계층 표현)
- **4문단**: 여백/공간 활용과 레이아웃 철학 (밀도 vs 여유, 리듬감)
- **5문단 (선택)**: 인터랙션/모션 성격 (정적 vs 다이내믹, 전환 속도)

**Key Characteristics 리스트** 포함: 핵심 시각적 특징 5~8가지를 불릿으로 나열.

#### §11 Layout Patterns 분석 (판정 #9)

HTML 구조 + CSS를 분석하여 다음 항목을 추출:

- **Grid System**: content max-width, grid type (CSS Grid / Flexbox / float), column count, gutter
- **Hero**: layout 방식 (1-column centered / 2-column split / full-width image), background, H1 스펙, max-width
- **Section Rhythm**: section padding (vertical/horizontal), max-width
- **Card Patterns**: card bg, border, radius, padding, shadow, hover 효과
- **Navigation Structure**: type (horizontal / hamburger), position (fixed/sticky/static), height, bg, border
- **Content Width**: prose max-width, container max-width, sidebar width

분석 소스:
- HTML의 `<section>`, `<nav>`, `<header>`, `<main>`, `<article>` 태그 구조
- CSS의 `max-width`, `display: grid`, `display: flex`, `grid-template-columns` 속성
- CSS의 `padding`, `margin`, `gap` 값에서 섹션 리듬 파악

#### §12 Responsive Behavior 분석 (판정 #10)

CSS에서 `@media` 쿼리를 추출하여 다음을 파싱:

- **Breakpoints**: 모든 `min-width` / `max-width` 값 수집 → Name/Value/Description 테이블
- **Touch Targets**: 모바일에서의 button height, input height, minimum tap size (44px 이상인지)
- **Collapsing Strategy**: 네비게이션 접기 방식, 그리드 컬럼 축소, 사이드바 처리, 히어로 레이아웃 변경
- **Image Behavior**: `max-width: 100%`, `object-fit`, aspect-ratio 처리

분석 소스:
- CSS의 `@media (min-width: ...)` / `@media (max-width: ...)` 블록
- 모바일 퍼스트 vs 데스크톱 퍼스트 판별 (`min-width` 우세 → 모바일 퍼스트)

#### §13 Components 확장 분석 (판정 #11)

기존 Buttons/Badges 외에 추가 분석:

- **Cards & Containers**: bg, border, radius, padding, shadow, hover 상태 (shadow 변화, border-color 변화, transform)
- **Navigation**: 링크 스타일, active 상태 표시, 모바일 메뉴 구조
- **Inputs & Forms**: input height, padding, border, focus 스타일 (ring/outline), error 스타일, placeholder 색상
- **Hero Section**: 배경 처리, 텍스트 크기/weight, CTA 배치, 이미지/일러스트 레이아웃

각 컴포넌트: BEM 클래스명 + HTML 마크업 + spec 표 + 상태별(hover/active/focus) 값

#### §17 Agent Prompt Guide 생성 (판정 #12)

분석된 토큰을 바탕으로 자동 생성:

- **Quick Color Reference**: 역할별(Brand primary, Background, Text primary, Text muted, Border, Success, Error) hex 요약 테이블
- **Example Component Prompts**: Hero Section, Card, Badge, Navigation 각각에 대한 복사-가능한 프롬프트 예시
  - 프롬프트에는 실제 추출된 hex, font, size, weight, radius 값 삽입
- **Iteration Guide**: 색상/폰트/여백/컴포넌트 변경 시 주의사항 (semantic token 사용, spacing scale 준수 등)

#### 🆕 §18 DON'T 작성 규칙 (판정 #7 상세) — apply 자동 검증 지원

**색상 관련 DON'T 항목은 반드시 구체 hex를 포함**해야 한다. apply 스킬의 Step 3 자동 위반 검증이 hex를 grep 패턴으로 사용하기 때문.

**❌ 잘못된 작성 (apply가 검증 불가)**:
- "순백 배경을 쓰지 말 것"
- "검정 텍스트 쓰지 말 것"
- "본문 weight 가볍게 두지 말 것"

**✅ 올바른 작성 (apply가 grep 가능)**:
- "배경을 `#FFFFFF` 또는 `white`로 두지 말 것 — 대신 `#F4F4F4` 사용"
- "텍스트를 `#000000` 또는 `black`으로 두지 말 것 — 대신 `#1D1D1F` 사용"
- "body에 `font-weight: 400` 사용 금지 — Stripe는 300이 맞다"

**작성 패턴**:
```
"X를 [금지 hex/값]으로 두지 말 것 — 대신 [올바른 hex/값] 사용"
```

apply가 자동 grep 하는 패턴 예시:
- `background:\s*(#fff|#FFFFFF|white)` → 위반 알림
- `color:\s*(#000|#000000|black)` → 위반 알림
- `body[^{]*\{[^}]*font-weight:\s*400` → 위반 알림

**비-색상 DON'T (구조적 금지)는 자유 형식**:
- "CTA 버튼을 정사각형으로 만들지 마라 — pill shape (border-radius 980px)"
- "다크 배경 링크에 brand-500을 그대로 쓰지 마라"

#### Brand color 선택 규칙 (판정 #1 상세)

brand_color는 아래 우선순위로 결정한다:

| 우선순위 | 소스 | 예시 |
|---------|------|------|
| 1 | **CTA/primary button의 background-color** | Stripe `#533AFD`, Toss `#3182F6` |
| 2 | **CSS 토큰에서 `brand`/`primary`/`accent` 이름을 가진 변수** | `--hds-color-core-brand-600` |
| 3 | **chromatic hex 빈도 상위** (neutral/white/black 제외) | brand_candidates.json의 chromatic 1위 |
| 4 | **공식 로고 색** (위 3가지가 모두 불명확할 때만) | — |

**brand_color가 될 수 없는 것**:
- `#000000`, `#FFFFFF` 또는 near-black/near-white (채도 < 5%) — 이들은 neutral이지 brand가 아님
- foreground text 색 (`#1d1c1b` 같은 본문 색)
- 고객사 로고/SVG에서만 등장하는 색 (logo wall 오염)

**Dual-anchor 사이트** (light hero와 dark section에 서로 다른 accent가 있는 경우):
- brand_color에는 **CTA 버튼 색** 또는 **더 높은 빈도의 chromatic** 선택
- 나머지는 §06 Colors에서 별도 서술

#### Monochrome 사이트 처리

채도 있는 컬러가 거의 없는 사이트 (Figma, Vercel, Warp 등):

1. **frontmatter에 `color_system: monochrome` 추가**
2. **brand_color**: 가장 채도 높은 accent hex 선택. accent도 없으면 `#000000` 사용하되, §01 Quick Start에 "이 사이트는 monochrome 디자인" 명시
3. **§06 Colors**: 컬러 램프 대신 **grayscale/neutral ramp** + **accent 목록** 구조로 작성
4. **§18 DO/DON'T**: "❌ 임의의 brand color를 지어내지 말 것 — 이 사이트의 정체성은 색이 아니라 톤/타이포"

**원칙 3가지** (절대 위반 금지):
1. AI는 hex 값을 만들지 않는다 — CSS에 없는 hex 생성 = 환각
2. AI는 토큰명을 만들지 않는다 — `color-brand` 같은 가상 이름 금지
3. AI는 팩트 위에 해석만 얹는다 — 값 변경 NO, 분류/설명 OK

---

### Step 5: WRITE-MD
**Type**: generate

design.md를 생성한다.

1. Read: `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/references/template.md` — 19섹션 v3.1 (§00~§18)
2. Read: `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/examples/stripe/design.md` — 골드 스탠다드 (구조 참조)
3. Step 3 팩트 + Step 4 해석(판정 #1~#12)을 조합하여 19섹션 채우기
4. Write: `insane-design/{slug}/design.md`

**필수 사항**:
- YAML frontmatter 맨 위 (`---` 블록)
- 🆕 frontmatter 최상단에 `schema_version: 3.1` 필수
- 🆕 frontmatter에 `medium` + `medium_confidence` 필드 (Step 1에서 감지한 값) 필수
- 필수 섹션 14개: 00, 01, 02, 03, 04, 05, 06, 07, 08, 11, 13, 15, 17, 18
- 선택 섹션 5개: 09, 10, 12, 14, 16 — 데이터 없으면 통째 제거
- 파일 크기 ≥ 8KB
- 모든 hex 값이 실제 CSS에 존재

**v3 섹션 번호 매핑** (§00~§18):
| § | 섹션 | 필수 |
|---|---|---|
| 00 | Visual Theme & Atmosphere | ✅ |
| 01 | Quick Start | ✅ |
| 02 | Provenance | ✅ |
| 03 | Tech Stack | ✅ |
| 04 | Font Stack | ✅ |
| 05 | Typography Scale | ✅ |
| 06 | Colors | ✅ |
| 07 | Spacing | ✅ |
| 08 | Radius | ✅ |
| 09 | Shadows | ⭕ |
| 10 | Motion | ⭕ |
| 11 | Layout Patterns | ✅ |
| 12 | Responsive Behavior | ⭕ |
| 13 | Components | ✅ |
| 14 | Content / Copy Voice | ⭕ |
| 15 | Drop-in CSS | ✅ |
| 16 | Tailwind Config | ⭕ |
| 17 | Agent Prompt Guide | ✅ |
| 18 | DO / DON'T | ✅ |

---

### Step 6: RENDER-HTML
**Type**: generate

report.ko.html을 생성한다.

1. Read: `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/references/report-prompt.md` — 생성 규칙 v2.1 (v3 섹션 매핑 포함)
2. Read: `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/references/report.css` — canonical CSS (있으면 사용, 없으면 Stripe report에서 추출)
3. Read: `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/examples/stripe/report.ko.html` — 골드 스탠다드 (CSS/JS/구조 복사)
4. Read: `insane-design/{slug}/design.md` — 데이터 소스
5. Stripe report의 `<style>` 블록 + JS 구조를 기반으로, 토큰/섹션만 현재 서비스로 교체
6. Write: `insane-design/{slug}/report.ko.html`

**v3 → report 섹션 매핑** (template.md 주석 참조):
- §00 Visual Theme → report mood section
- §01 Quick Start → report hero
- §02 Provenance → report §01
- §03 Tech Stack → report §02
- §04+§05 Font/Typography → report §03 (통합)
- §06 Colors → report §04
- §07 Spacing → report §05
- §08 Radius → report §06
- §09 Shadows → report §07
- §10 Motion → report §08 (optional)
- §11 Layout Patterns → report §09
- §12 Responsive → report §09-resp
- §13 Components → report §10
- §14 Content Voice → report §11 (optional)
- §15+§16 CSS/Tailwind → report sidebar
- §17 Agent Prompt → report §agent
- §18 DO/DON'T → report §12

**필수 사항**:
- 한국어
- shadcn zinc 테마 (Pretendard Variable + Inter + JetBrains Mono)
- `--brand-color` 만 서비스별로 교체
- 인터랙티브: 컬러 스와치 hover, 타이포 live preview, 스페이싱 바, Copy 버튼
- 스크린샷: `screenshots/hero-cropped.png` hero 섹션에 삽입
- 파일 크기 ≥ 20KB

---

### Step 7: VALIDATE
**Type**: script + review

생성 결과를 검증한다.

```bash
# 1. YAML frontmatter 맨 위
head -1 insane-design/{slug}/design.md | grep -q '^---$'

# 2. 필수 섹션 존재 (v3: §00~§18)
for n in 00 01 02 03 04 05 06 07 08 11 13 15 17 18; do
  grep -q "^## $n\." insane-design/{slug}/design.md || echo "Missing §$n"
done

# 3. 파일 크기
[ $(wc -c < insane-design/{slug}/design.md) -ge 8000 ]
[ $(wc -c < insane-design/{slug}/report.ko.html) -ge 20000 ]

# 4. hex 실존 (상위 3개)
for hex in $(grep -oE '#[0-9A-Fa-f]{6}' insane-design/{slug}/design.md | sort -u | head -3); do
  grep -qi "$hex" insane-design/{slug}/css/*.css || echo "Missing: $hex"
done
```

**실패 시**: 최대 2회 재생성 (실패 항목만 수정). 2회 후에도 실패면 경고 포함 출력.

**성공 시**:
```
✅ {slug} 분석 완료!

📄 design.md:     insane-design/{slug}/design.md ({size}KB)
🌐 report.ko.html: insane-design/{slug}/report.ko.html ({size}KB)
📸 screenshot:     insane-design/{slug}/screenshots/hero-cropped.png

design.md를 Claude Code에 첨부하면 이 사이트 스타일로 UI를 만들 수 있습니다.
report.ko.html을 브라우저에서 열면 인터랙티브 디자인 리포트를 볼 수 있습니다.
```

---

## References

| 파일 | 용도 | 참조 Step |
|------|------|-----------|
| **`references/architecture.md`** | 전체 시스템 아키텍처 (Phase 1~6, 스크립트/AI 분담, 파일 구조) | 전체 |
| **`references/data-collection.md`** | 5-tier fallback 수집 전략 + Jina Reader 스크린샷 상세 | Step 2 |
| **`references/methodology.md`** | 분석 5단계 프로세스 + 서비스당 체크리스트 | 전체 |
| **`references/workflow.md`** | 서비스당 절차 상세 (소요 시간, 섹션별 데이터 소스) | 전체 |
| **`references/template.md`** | design.md 19섹션 템플릿 v3.1 (§00~§18, YAML frontmatter, 필수/선택 섹션, medium 분기, N/A 규칙) | Step 5 |
| **`references/report-prompt.md`** | HTML 리포트 생성 규칙 v2.1 (v3 섹션 매핑, 인터랙티브 요소, 한글 네이밍) | Step 6 |
| **`references/report.css`** | canonical CSS (리포트 공통 스타일시트, 있으면 사용) | Step 6 |
| **`references/pitfalls.md`** | 35개 서비스 분석에서 발견된 14가지 함정 (가상 토큰명, 리브랜딩, light/dark 역전 등) | Step 4 |

## Scripts

- **`scripts/brand_candidates.py`** — CSS에서 브랜드 색상 후보 추출 (semantic + selector-role + frequency)
- **`scripts/var_resolver.py`** — CSS var() 체인 재귀 해결
- **`scripts/typo_extractor.py`** — 타이포그래피 스케일 추출
- **`scripts/alias_layer.py`** — 시멘틱 alias tier 분류 (util/action/component/core)
- **`scripts/capture_jina_screenshots.py`** — Jina Reader API 스크린샷 + PIL crop

## Examples

- **`examples/stripe/design.md`** — Stripe 골드 스탠다드 (25KB, 16섹션)
- **`examples/stripe/report.ko.html`** — Stripe HTML 리포트 골드 스탠다드 (74KB)

## Settings

| 설정 | 기본값 | 변경 방법 |
|------|--------|-----------|
| 리포트 언어 | 한국어 (report.ko.html) | Step 6에서 영어 전환 가능 |
| 스크린샷 | Jina Reader + PIL crop | Playwright fallback 자동 |
| design.md 파일명 | `design.md` | Step 5에서 변경 가능 |
| 출력 경로 | `insane-design/{slug}/` | Step 1에서 변경 가능 |
