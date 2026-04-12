---
name: insane-design
description: >
  URL 하나로 웹사이트의 실제 CSS를 분석해 디자인 시스템 레퍼런스(design.md)와
  인터랙티브 HTML 리포트(report.ko.html)를 생성하는 스킬.
  "디자인 분석해줘", "이 사이트 디자인 시스템 뽑아줘", "insane-design",
  "CSS 뜯어봐", "design.md 만들어줘", "레퍼런스 리포트 만들어줘",
  "사이트 분석", "디자인 토큰 추출", "analyze design", "extract design tokens".
  Use this skill whenever the user provides a URL and asks about design systems,
  design tokens, CSS analysis, or wants to replicate a website's look and feel.
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

- `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/references/template.md` — design.md 16섹션 템플릿 (Step 5에서 Read)
- `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/references/report-prompt.md` — HTML 리포트 생성 규칙 (Step 6에서 Read)
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
2. URL 검증:
   - `http://` 또는 `https://` 프로토콜 확인
   - `localhost`, `127.0.0.1`, `file://` 차단
   - 도메인 형식 유효성 확인
3. 출력 디렉토리 생성 (**절대 경로 사용**):

```bash
mkdir -p "$WORK_DIR/insane-design/{slug}/{screenshots,css,phase1}"
```

4. 사용자에게 시작 알림:
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
curl -sL \
  -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -H "Accept: text/html,application/xhtml+xml" \
  -H "Accept-Language: en-US,en;q=0.9" \
  --compressed --max-time 30 \
  -o "$WORK_DIR/insane-design/{slug}/index.html" \
  "{url}"
```

성공 판정: 파일 크기 ≥ 5KB + `<html>` 태그 존재 + Cloudflare challenge 없음.
실패 시 Tier 2(Mobile UA) → Tier 3(Jina HTML mode: `curl -H "X-Return-Format: html" "https://r.jina.ai/{url}"`) 순서로 시도.

HTML에서 CSS 링크 추출 + 병렬 다운로드:
```bash
grep -oE 'href="[^"]+\.css[^"]*"' "$WORK_DIR/insane-design/{slug}/index.html" | \
  sed 's/href="//;s/"$//' | \
  xargs -n1 -P8 -I{} curl -sL -o "$WORK_DIR/insane-design/{slug}/css/$(basename {})" "{absolute_url}"
```

#### 2B. 스크린샷 수집 (병렬)

```bash
# Jina Reader API 직접 호출 (slug 하드코딩 아닌 동적)
curl -sL -H "X-Respond-With: screenshot" --max-time 30 \
  "https://r.jina.ai/{url}" \
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

Jina Reader 실패 시 (파일 < 5KB) → Playwright fallback 시도.

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

# 브랜드 색상 후보
python3 "${CLAUDE_PLUGIN_ROOT}/skills/insane-design/scripts/brand_candidates.py" {slug}

# CSS var() 체인 해결
python3 "${CLAUDE_PLUGIN_ROOT}/skills/insane-design/scripts/var_resolver.py" {slug}

# 타이포그래피 스케일
python3 "${CLAUDE_PLUGIN_ROOT}/skills/insane-design/scripts/typo_extractor.py" {slug}

# 시멘틱 alias 계층 분류
python3 "${CLAUDE_PLUGIN_ROOT}/skills/insane-design/scripts/alias_layer.py" {slug}
```

결과: `$WORK_DIR/insane-design/{slug}/phase1/` 에 4개 JSON:
- `brand_candidates.json` — 브랜드 색상 후보 (semantic + selector-role + frequency)
- `resolved_tokens.json` — var() 체인 해결된 토큰
- `typography.json` — 타이포 스케일 (heading/text/input/quote)
- `alias_layer.json` — tier 분류 (util/action/component/core)

#### 추출 실패 처리

CSS custom properties 0개면:
- "CSS 토큰 부족 — Tailwind/CSS-in-JS 사이트일 수 있습니다. 빈도 기반 hex 분석으로 대체합니다." 경고
- hex frequency 기반 분석으로 전환 (brand_candidates.json의 frequency_candidates 활용)

---

### Step 4: INTERPRET
**Type**: prompt (멀티모달)

Claude가 스크린샷 + 추출 결과를 보고 AI 판정을 수행한다.

1. Read: `insane-design/{slug}/screenshots/hero-cropped.png` (또는 `jina-hero.png`)
2. Read: `insane-design/{slug}/phase1/brand_candidates.json`
3. Read: `insane-design/{slug}/phase1/typography.json`
4. Read: `insane-design/{slug}/phase1/alias_layer.json`
5. Read: `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/references/pitfalls.md` — 14가지 함정

**판정 항목 (7가지)**:

| # | 판정 | 출력 |
|---|---|---|
| 1 | Brand color 확정 | hex (예: `#533AFD`) |
| 2 | Light/Dark 테마 | `light` / `dark` / `mixed` |
| 3 | Custom font 식별 | `sohne-var = 유료`, `Inter = 오픈` 등 |
| 4 | Framework 식별 | `Next.js + HDS`, `Tailwind v4` 등 |
| 5 | Hero anatomy 서술 | "2-column, gradient flame bg" 등 |
| 6 | Quick Start "절대 하지 말 것" | 가장 치명적인 한 가지 |
| 7 | DO/DON'T | 각 4~8 항목 |

**원칙 3가지** (절대 위반 금지):
1. AI는 hex 값을 만들지 않는다 — CSS에 없는 hex 생성 = 환각
2. AI는 토큰명을 만들지 않는다 — `color-brand` 같은 가상 이름 금지
3. AI는 팩트 위에 해석만 얹는다 — 값 변경 NO, 분류/설명 OK

---

### Step 5: WRITE-MD
**Type**: generate

design.md를 생성한다.

1. Read: `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/references/template.md` — 16섹션 v2.0
2. Read: `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/examples/stripe/design.md` — 골드 스탠다드 (구조 참조)
3. Step 3 팩트 + Step 4 해석을 조합하여 16섹션 채우기
4. Write: `insane-design/{slug}/design.md`

**필수 사항**:
- YAML frontmatter 맨 위 (`---` 블록)
- 필수 섹션 11개: 01, 02, 03, 04, 05, 06, 07, 08, 12, 14, 16
- 선택 섹션 5개: 09, 10, 11, 13, 15 — 데이터 없으면 통째 제거
- 파일 크기 ≥ 8KB
- 모든 hex 값이 실제 CSS에 존재

---

### Step 6: RENDER-HTML
**Type**: generate

report.ko.html을 생성한다.

1. Read: `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/references/report-prompt.md` — 생성 규칙
2. Read: `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/examples/stripe/report.ko.html` — 골드 스탠다드 (CSS/JS/구조 복사)
3. Read: `insane-design/{slug}/design.md` — 데이터 소스
4. Stripe report의 `<style>` 블록 + JS 구조를 기반으로, 토큰/섹션만 현재 서비스로 교체
5. Write: `insane-design/{slug}/report.ko.html`

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

# 2. 필수 섹션 존재
for n in 01 02 03 04 05 06 07 08 12 14 16; do
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
| **`references/template.md`** | design.md 16섹션 템플릿 v2.0 (YAML frontmatter, 필수/선택 섹션, N/A 규칙) | Step 5 |
| **`references/report-prompt.md`** | HTML 리포트 생성 규칙 v2.1 (섹션 매핑, 인터랙티브 요소, 한글 네이밍) | Step 6 |
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
