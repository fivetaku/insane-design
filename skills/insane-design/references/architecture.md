# DesignMD Writer — System Architecture

> ⚠️ **DEPRECATED v2.0 ARCHITECTURE NOTE** (2026-05-02)
>
> 이 문서는 v2.0 (16섹션 §01~§16) 시점의 아키텍처 기록이다.
> 현행은 v3.2 (19섹션 §00~§18 + §19 Known Gaps + frontmatter 객체화).
> **단일 진실 소스는 `SKILL.md` + `template.md` + `_shared/README.md` 3종이다.**
> 본 문서는 시스템 진화 기록 + Phase 1~6 데이터 수집 전략 참조용.
>
> 섹션 번호 매핑이 SKILL.md와 다른 부분(§01 Quick Start로 시작 / §00 부재 / §16 DO/DON'T)은 무시할 것.

---

## 0. 현행 19섹션 매핑 (v3.2 — 2026-05-02 업데이트)

| v2.0 (이 문서) | v3.2 (SKILL.md, template.md) |
|----------------|------------------------------|
| (없음) | §00 Direction & Metaphor (샌드위치) |
| §01 Quick Start | §01 Quick Start |
| §02 Provenance | §02 Provenance |
| §03~§13 | §03~§13 (대체로 일치) |
| §14 Drop-in CSS | §15 Drop-in CSS (1단계 시프트) |
| §15 Tailwind | §16 Tailwind Config |
| §16 DO/DON'T | §17 Agent Prompt + §18 DO/DON'T (분리) |
| (없음) | §19 Known Gaps & Assumptions |

→ 본 문서 4-9절의 Phase 1-6 흐름은 여전히 유효. 섹션 번호 매핑만 위 표 따라 보정해서 읽을 것.

---

## 1. 전체 흐름 — 한 눈에

```
         ┌──────────┐
         │  URL 입력  │
         └─────┬────┘
               ▼

---

## 1. 전체 흐름 — 한 눈에

```
         ┌──────────┐
         │  URL 입력  │
         └─────┬────┘
               ▼
   ┌──────────────────────┐
   │  Phase 1: 수집        │  자동 · 스크립트
   │  fetch_site.py        │  5-tier fallback (HTML/CSS)
   │  + Jina Reader        │  스크린샷 (병렬)
   │  ─────────────────── │
   │  → index.html         │
   │  → css/*.css          │
   │  → screenshots/       │
   │     jina-hero.png     │
   └─────────┬────────────┘
             ▼
   ┌──────────────────────┐
   │  Phase 2: 추출        │  자동 · 스크립트
   │  parse_tokens.py      │  정규식 파싱
   │  ─────────────────── │
   │  → tokens.json        │  팩트(hex, font, spacing...)
   └─────────┬────────────┘
             ▼
   ┌──────────────────────┐
   │  Phase 3: 판정        │  AI · 멀티모달
   │  Claude 직접 처리      │  스크린샷 + tokens.json
   │  ─────────────────── │
   │  → brand color 확정    │
   │  → light/dark 판정     │
   │  → font 식별           │
   │  → hero anatomy 서술   │
   │  → DO/DON'T 선정       │
   └─────────┬────────────┘
             ▼
   ┌──────────────────────┐
   │  Phase 4: 작성        │  AI · 템플릿 기반
   │  design.md 작성        │  16 섹션 마크다운
   │  .md 작성             │
   └─────────┬────────────┘
             ▼
   ┌──────────────────────┐
   │  Phase 5: 리포트       │  자동+AI · HTML 생성
   │  report.ko.html       │  인터랙티브 리포트
   └─────────┬────────────┘
             ▼
   ┌──────────────────────┐
   │  Phase 6: 검증        │  자동 · grep/wc 체크
   │  validate_designmd.py │
   └──────────────────────┘
```

**핵심**: Phase 1~2 는 **결정적(deterministic)** — 같은 URL 이면 항상 같은 결과. Phase 3~5 는 **AI** — 팩트 위에 해석을 얹는다. Phase 6 은 다시 **결정적** — 결과물 검증.

---

## 2. 입력과 출력

### 입력
```
URL 하나 (예: https://stripe.com)
slug 하나 (예: stripe)
```

### 출력 (서비스당)
```
real/{slug}/
├── design.md                  텍스트 레퍼런스 (8~25KB)
├── report.ko.html             인터랙티브 HTML 리포트 (23~75KB)
└── screenshots/
    └── jina-hero.png          Jina Reader 캡처 (1280×1280)
```

### 중간 산출물 (디버깅/재사용용)
```
designmd-data/real/{slug}/
├── index.html                 원본 HTML
├── css/*.css                  원본 CSS 파일들
├── tokens.json                파싱된 전체 토큰
└── fetch_report.json          수집 tier/quality 메타데이터
```

---

## 3. Phase 1: 수집 (Data Collection)

### 3.1 무엇을 수집하는가

| 대상 | 왜 필요한가 | 저장 위치 |
|---|---|---|
| **HTML 홈페이지** | 클래스명 추출, 구조 파악 | `index.html` |
| **외부 CSS 파일** | 토큰 파싱의 유일한 진실 소스 | `css/*.css` |
| **인라인 `<style>` 블록** | 일부 사이트는 CSS 번들 없이 인라인 | `css/_inline.css` |
| **스크린샷 (Jina Reader)** | 브랜드 컬러/테마 시각 검증, 리포트 삽입 | `screenshots/jina-hero.png` |

### 3.2 수집 순서

**HTML/CSS 수집** 과 **스크린샷 수집** 은 서로 독립적이므로 **병렬**로 진행한다.

```
URL 입력
  ├── (A) HTML/CSS 수집 (5-tier fallback)
  │     → index.html, css/*.css
  │
  └── (B) 스크린샷 수집 (Jina Reader 1순위)
        → screenshots/jina-hero.png
```

### 3.3 스크린샷 수집 — Jina Reader 우선

> **35개 서비스 검증 결과: Jina Reader 100% 성공, Playwright 54% 성공.**
> bot 차단, Cloudflare, 쿠키 팝업, 리다이렉트 문제를 전부 우회.

**1순위: Jina Reader API** (설치 불필요, 무료, 3초)

```bash
curl -sL \
  -H "X-Respond-With: screenshot" \
  --max-time 30 \
  "https://r.jina.ai/{URL}" \
  -o screenshots/jina-hero.png
```

- 1280×1280 PNG 반환
- bot 차단 우회 (Puppeteer 기반 실제 브라우저 렌더링)
- 쿠키 배너 자동 dismiss
- JS SPA 완전 렌더링 후 캡처
- **Rate limit**: 동시 2-3개로 제한 (5개 초과 시 293 bytes 에러 응답)

**2순위 fallback: Playwright** (Jina 실패 시에만)

```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    page.goto(url, wait_until="domcontentloaded", timeout=30000)
    page.screenshot(path="screenshots/jina-hero.png")
```

⚠️ Playwright 는 bot 차단에 취약 — 35개 중 16개 사이트에서 잘못된 페이지(정책 문서, 앱 내부 화면, Cloudflare challenge) 를 캡처함. Jina 실패 시에만 사용.

**스크린샷 검증**:
```python
def is_valid_screenshot(path: str) -> bool:
    import os
    if not os.path.exists(path): return False
    size = os.path.getsize(path)
    if size < 5000: return False      # 에러 응답 (293 bytes 등)
    # PNG magic bytes
    with open(path, 'rb') as f:
        return f.read(4) == b'\x89PNG'
```

**스크린샷 후처리 — hero-cropped.png 생성**:

Jina Reader 는 1280×1280 정사각형을 반환한다. 리포트에 삽입할 때는 하단 여백을 잘라내고 상단 hero 영역만 남긴 1280×800 을 사용한다.

```python
from PIL import Image

def crop_hero(slug: str):
    src = f"real/{slug}/screenshots/jina-hero.png"
    dst = f"real/{slug}/screenshots/hero-cropped.png"
    img = Image.open(src)
    # 상단 800px 유지 (하단 480px 잘라냄)
    cropped = img.crop((0, 0, 1280, 800))
    cropped.save(dst)
```

```
jina-hero.png (1280×1280, 원본)
  │
  └─▶ crop(0, 0, 1280, 800)
        │
        └─▶ hero-cropped.png (1280×800, 리포트 삽입용)
```

- **입력**: `screenshots/jina-hero.png` (Jina Reader 원본)
- **출력**: `screenshots/hero-cropped.png` (리포트 Hero 섹션에 삽입)
- **시점**: Phase 1 수집 완료 직후, Phase 3 판정 시작 전
- **Phase 5 에서의 사용**: `GENERATE_REPORT_PROMPT.md` §4 에 따라 `hero-cropped.png` 이 존재하면 Hero 에 `<img>` 삽입, 없으면 생략

### 3.4 HTML/CSS 수집 — 5-tier Fallback 체인

```
Tier 1: curl + Chrome UA         80% 커버, 5초
  ↓ 실패 시
Tier 2: curl + Mobile UA         네이버 등 모바일 우선 사이트
  ↓ 실패 시
Tier 3: Jina Reader HTML mode    JS SPA 렌더링 + CSS 링크 보존
  ↓ 실패 시
Tier 4: curl_cffi chrome124      Cloudflare TLS 핑거프린트 우회
  ↓ 실패 시
Tier 5: Playwright headless      최후 수단, 모든 JS 실행
```

#### 각 tier 상세

| Tier | 의존성 | 시간 | 커버 케이스 | 한계 |
|---|---|---|---|---|
| 1 | 없음 (curl) | 5초 | 일반 SSR 사이트 | bot 차단, SPA 빈 HTML |
| 2 | 없음 (curl) | 5초 | 네이버/한국 사이트 | TLS 차단, SPA |
| 3 | 없음 (HTTP API) | 10초 | JS SPA 전부 | CSS 링크 일부 손실 가능 |
| 4 | `pip install curl_cffi` | 5초 | Cloudflare/Akamai WAF | 극소수 사이트 |
| 5 | `pip install playwright` | 30초 | 전부 | 느림, 설치 복잡 |

> **Tier 3 Jina Reader HTML mode**: `curl -H "X-Return-Format: html" "https://r.jina.ai/{URL}"` — Puppeteer 로 렌더링된 HTML 을 원본 형태로 반환. CSS `<link>` 태그가 보존되어 별도 CSS 다운로드 가능.

#### HTML 성공 판정 기준

```python
def is_valid(html: str) -> bool:
    if len(html) < 5000: return False                          # 너무 짧음
    if "Just a moment..." in html: return False                # Cloudflare challenge
    if "cf-chl-bypass" in html: return False                   # Cloudflare
    body_text = extract_body_text(html)
    if len(body_text) < 500: return False                      # SPA 빈 껍질
    return True
```

#### 수집 품질 메타데이터

```json
{
  "slug": "stripe",
  "url": "https://stripe.com",
  "html_tier": 1,
  "html_quality": "direct",
  "html_bytes": 574643,
  "css_files": 8,
  "css_total_bytes": 425918,
  "screenshot_source": "jina",
  "screenshot_bytes": 723456,
  "errors": []
}
```

### 3.3 CSS 링크 추출 + 다운로드

```python
# HTML 에서 stylesheet 링크 추출
links = re.findall(
    r'<link[^>]+rel=["\']?stylesheet["\']?[^>]+href=["\']([^"\']+)["\']',
    html, re.I
)
# 상대 경로 → 절대 URL 변환
absolute = [urllib.parse.urljoin(base_url, href) for href in links]
# 병렬 다운로드
xargs -n1 -P10 curl -sL -o css/{basename} {url}
```

---

## 4. Phase 2: 추출 (Token Extraction)

### 4.1 무엇을 추출하는가

| 추출 대상 | 방법 | 결과 키 |
|---|---|---|
| CSS 커스텀 프로퍼티 | `--name: value` 정규식 | `custom_properties` |
| 토큰 prefix | prefix 빈도 카운트 | `token_prefix` |
| 컬러 ramp 그룹핑 | `--prefix-family-step` 패턴 | `color_ramps` |
| 전체 hex 빈도 | `#[0-9a-fA-F]{3,8}` 카운트 | `hex_frequency` |
| 타이포 스케일 | `--*-font-heading-*-size/weight/lh/ls` | `typography_scale` |
| font-family 빈도 | `font-family:` 선언 카운트 | `font_families` |
| 스페이싱 토큰 | `--*-space-*` 또는 `--*-spacing-*` | `spacing` |
| Radius 토큰/값 | `border-radius:` 선언 카운트 | `radius` |
| Shadow 토큰/값 | `box-shadow:` + `--*-shadow-*` | `shadows` |
| BEM 클래스 | HTML `class=""` 파싱 + 빈도 | `component_classes` |
| var() 체인 해결 | 재귀 `var(--x, fallback)` 추적 | `resolved_tokens` |
| Brand 후보 | semantic name + selector role + frequency | `brand_candidates` |
| Alias layer 분류 | util/action/component/core tier | `alias_tiers` |

### 4.2 스크립트 매핑

| 스크립트 | 추출 대상 | 입력 | 출력 |
|---|---|---|---|
| `parse_tokens.py` (신규) | 위 전체 통합 | `css/*.css` + `index.html` | `tokens.json` |
| `brand_candidates.py` (기존) | 브랜드 후보 | `css/*.css` + `index.html` | `brand_candidates.json` |
| `var_resolver.py` (기존) | var() 체인 | `css/*.css` | `resolved_tokens.json` |
| `typo_extractor.py` (기존) | 타이포 스케일 | `css/*.css` | `typography.json` |
| `alias_layer.py` (기존) | tier 분류 | `css/*.css` | `alias_layer.json` |

> 최종 스킬에서는 `parse_tokens.py` 하나로 통합하되, 기존 5개 스크립트의 로직을 내부 함수로 흡수.

### 4.3 추출 결과 스키마 (`tokens.json`)

```json
{
  "slug": "stripe",
  "fetched_at": "2026-04-11",
  "token_prefix": "hds",
  "stats": {
    "custom_properties": 819,
    "unique_hex_colors": 286,
    "font_families": 7,
    "spacing_tokens": 35,
    "radius_tokens": 7,
    "shadow_levels": 3,
    "typography_scales": 16,
    "component_classes": 25
  },
  "color_ramps": { "brand": { "25": "#F5F5FF", ... }, ... },
  "hex_frequency": [["#FFFFFF", 67], ["#000000", 42], ...],
  "typography_scale": { "heading-xxl": { "size": "2.125rem", ... }, ... },
  "font_families": [["sohne-var", 3], ["SourceCodePro", 1]],
  "font_vars": { "family": "...", "family_code": "...", "weight_normal": "300", "weight_bold": "400" },
  "spacing": { "core-0": "0px", "core-50": "4px", ... },
  "radius": { "none": "0px", "sm": "4px", "md": "6px", ... },
  "shadows": { "sm": "0 5px 14px ...", "md": "...", "lg": "..." },
  "alias_tiers": { "util": 105, "action": 107, "component": 120, "core": 189 },
  "brand_candidates": { "semantic": [...], "selector_role": [...], "frequency_chromatic": [...] },
  "component_classes": [["hds-heading", 80], ["hds-text--md", 70], ...]
}
```

---

## 5. Phase 3: 판정 (AI Interpretation)

> **이 Phase 가 "사실"과 "해석"의 경계선이다.**
> Phase 2 까지는 스크립트가 뽑은 raw data.
> Phase 3 부터는 AI 가 "이 중 어떤 게 진짜 중요한가"를 결정한다.

### 5.1 AI 가 결정하는 것 (7가지)

| # | 판정 항목 | 입력 | 출력 | 왜 AI 필요 |
|---|---|---|---|---|
| 1 | **Brand color 확정** | hex_frequency + brand_candidates + hero screenshot | `#533AFD` | frequency 1위는 항상 `#FFF`/`#000`. CTA 버튼 시각 확인 필요 |
| 2 | **Light/Dark 테마** | hero screenshot + hex_frequency | `light` / `dark` / `mixed` | luminance 만으로는 Warp 같은 오판 발생 |
| 3 | **Custom font 식별** | font_families 리스트 | `sohne-var = 유료 커스텀` | `Salesforce-Sans`, `figmaSans` 같은 건 지식 필요 |
| 4 | **Framework 식별** | token_prefix + HTML 구조 | `Next.js + HDS` | `--hds-*` 만으로 95% 가능하지만 Framer/Webflow 는 구조 판단 필요 |
| 5 | **Hero anatomy 서술** | hero screenshot + HTML | 2-column, gradient flame | 시각 관찰 |
| 6 | **Quick Start "절대 하지 말 것"** | 전체 분석 종합 | `body weight 300 (400 아님)` | 가장 치명적인 한 가지 고르는 판단 |
| 7 | **DO/DON'T 선정** | 전체 분석 종합 | 각 4~8 항목 | 서비스 고유 실수 패턴 파악 |

### 5.2 AI 가 결정하지 않는 것 (Phase 2 에서 이미 확정)

| 팩트 | 결정 주체 | 비고 |
|---|---|---|
| 모든 hex 값 | 스크립트 | CSS 에서 직접 파싱 |
| 모든 토큰명 | 스크립트 | `--hds-color-core-brand-600` 그대로 |
| 타이포 스케일 수치 | 스크립트 | size/weight/lh/ls |
| 스페이싱 토큰 | 스크립트 | `--hds-space-core-200: 16px` |
| font-family 선언 | 스크립트 | `"sohne-var", "SF Pro Display", sans-serif` |
| BEM 클래스명 + 빈도 | 스크립트 | `hds-button--primary: 13회` |
| Color ramp 그룹핑 | 스크립트 | brand-25~975 |
| var() 체인 terminal | 스크립트 | alias → core → hex |

> **원칙**: AI 는 팩트를 바꾸지 않는다. 팩트 위에 "어떤 게 더 중요한가"를 판정할 뿐.

---

## 6. Phase 4: 작성 (DESIGN.md)

### 6.1 템플릿 v2.0 구조

```yaml
# YAML frontmatter (맨 위)
---
slug, service_name, site_url, fetched_at,
default_theme, brand_color, primary_font,
font_weight_normal, token_prefix
---
```

```markdown
# DESIGN.md — {Service} (Claude Code Edition)

## 01. Quick Start              ← AI 작성 (치트시트)
## 02. Provenance               ← 스크립트 (fetch 메타)
## 03. Tech Stack               ← AI + 스크립트
## 04. Font Stack               ← AI + 스크립트 (CSS 블록 포함)
## 05. Typography Scale         ← 스크립트 (테이블)
## 06. Colors                   ← 스크립트 (ramp 테이블) + AI (alias 해석)
  ### 06-1. Brand Ramp
  ### 06-2. Brand Dark          <!-- OPTIONAL -->
  ### 06-3. Neutral Ramp
  ### 06-4. Accent Families     <!-- OPTIONAL -->
  ### 06-5. Semantic
  ### 06-6. Semantic Alias Layer
  ### 06-7. Dominant Colors
## 07. Spacing                  ← 스크립트
## 08. Radius                   ← 스크립트
## 09. Shadows                  <!-- OPTIONAL --> ← 스크립트
## 10. Motion                   <!-- OPTIONAL --> ← AI (관찰)
## 11. Layout Patterns          <!-- OPTIONAL --> ← AI (관찰)
## 12. Components               ← AI + 스크립트
## 13. Content / Copy Voice     <!-- OPTIONAL --> ← AI (관찰)
## 14. Drop-in CSS              ← 스크립트 + AI (선별)
## 15. Tailwind Config          <!-- OPTIONAL --> ← 스크립트 + AI
## 16. DO / DON'T               ← AI
```

### 6.2 각 섹션의 데이터 소스 흐름

```
tokens.json ──┬── §05 Typography Scale (그대로)
              ├── §06 Colors (ramp 테이블 그대로)
              ├── §07 Spacing (그대로)
              ├── §08 Radius (그대로)
              ├── §09 Shadows (그대로)
              └── §14 Drop-in CSS (선별해서)

brand_candidates ── AI 판정 ──── §01 Quick Start (brand hex)
                                 §06-7 Dominant Colors
                                 §14 Drop-in CSS (brand 토큰)

screenshots/ ─── AI 판정 ────── §01 Quick Start (테마)
                                 §02 Provenance (스크린샷 경로)
                                 §03 Tech Stack (테마 판정)
                                 §11 Layout Patterns (hero 구조)

font_families ── AI 판정 ────── §04 Font Stack (커스텀 식별)

component_classes ── AI 그룹핑 ── §12 Components (역할별 정리)

alias_tiers ──── AI 해석 ────── §06-6 Semantic Alias Layer

AI 관찰 ────────────────────── §10 Motion (CSS 에 없는 것)
                                 §13 Content Voice (사이트 톤)
                                 §16 DO / DON'T (종합 판단)
```

### 6.3 필수 vs 선택 섹션

| 구분 | 섹션 번호 | 기준 |
|---|---|---|
| **필수** (11개) | 01, 02, 03, 04, 05, 06, 07, 08, 12, 14, 16 | 어떤 사이트든 데이터 존재 |
| **선택** (5개) | 09, 10, 11, 13, 15 | 데이터 없으면 통째 제거 |
| **서브 선택** | 06-2, 06-4 | 다크 ramp / accent 없는 사이트 |

---

## 7. Phase 5: HTML 리포트

> **생성 프롬프트 정본**: `GENERATE_REPORT_PROMPT.md` (v2.1)
> **골드 스탠다드**: `real/stripe/report.ko.html` (수작업 확정본)
> **생성 방식**: Python 스크립트가 아닌 **Claude Code 에이전트**가 design.md 를 읽고 직접 생성. 서비스마다 테이블/섹션 구조가 다르므로 의미 기반 이해가 필수.

### 7.1 HTML 구조

```
report.ko.html (단일 자체완결 HTML, CDN 폰트만 외부 의존)
├── <head>
│   ├── Pretendard Variable (한글 · jsdelivr CDN)
│   ├── Inter 400/500/600 (라틴 · Google Fonts)
│   ├── JetBrains Mono 400/500 (코드 · Google Fonts)
│   └── <style> shadcn zinc theme CSS (인라인, 전 서비스 공유)
│       └── --brand-color: {서비스별 brand_color} ← 유일한 서비스별 변수
│
├── <body>
│   └── <div.layout> (grid: 260px sidebar + main)
│       │
│       ├── <aside.toc> — 좌측 고정 (sticky, 100vh)
│       │   ├── brand name + sub
│       │   ├── 6개 그룹 (Overview / Foundations / Tokens / Patterns / Code / Rules)
│       │   │   └── 각 그룹: .toc__group-label (영어 uppercase) + .toc__list (한글 항목)
│       │   └── footer (생성 파일, 날짜)
│       │
│       └── <main>
│           ├── <section#hero>
│           │   ├── eyebrow pill "Design System Report"
│           │   ├── h1 "{service_name} — {system/prefix}"
│           │   ├── sub (design.md 에서 한 줄 요약)
│           │   ├── screenshot (있으면): screenshots/hero-cropped.png
│           │   ├── Quick Start 카드 (3칸 dark code + 빨간 경고)
│           │   └── 4-stat 카드 (Source / Fetched / System / 핵심수치)
│           │
│           ├── <section#provenance>  → §02 (key-value 테이블)
│           ├── <section#stack>       → §03 (2×3 카드 그리드)
│           ├── <section#typography>  → §04 + §05 합쳐짐
│           │   ├── Font Stack 카드 (폰트명, weight, fallback)
│           │   ├── Heading scale 테이블 (실제 size/weight inline style 렌더)
│           │   └── Text scale 테이블
│           ├── <section#colors>      → §06 전체
│           │   ├── Brand ramp 스와치 (step 수만큼 grid columns)
│           │   ├── BrandDark ramp (있으면)
│           │   ├── Neutral pair (2열 비교)
│           │   ├── Accent 카드 (4열 그리드)
│           │   ├── Semantic 카드 (success/error)
│           │   ├── Alias 테이블 (util-* → core-* 매핑)
│           │   └── Dominant colors 누적 막대 차트 (있으면)
│           ├── <section#spacing>     → §07 (토큰 + 실제 폭 bar)
│           ├── <section#radius>      → §08 (실제 border-radius 적용 박스)
│           ├── <section#shadows>     → §09 OPTIONAL (실제 box-shadow 카드)
│           ├── <section#motion>      → §10 OPTIONAL (인터랙션 패턴 테이블)
│           ├── <section#layout>      → §11 OPTIONAL (Hero/Section rhythm 카드)
│           ├── <section#components>  → §12
│           │   └── 각 컴포넌트: 데모 + 스펙 + HTML 마크업 코드 + Copy 버튼
│           ├── <section#voice>       → §13 OPTIONAL (라이팅 원칙 카드)
│           ├── <section#export>      → §14 + §15 합쳐짐
│           │   └── 탭 UI: "CSS 스니펫" | "Tailwind 설정" + Copy 버튼
│           └── <section#verdict>     → §16 Do / Don't
│               ├── Do 카드 (녹색) + Don't 카드 (빨간)
│               └── Myth 교정표 (있으면)
│
└── <script> 탭 전환 + 클립보드 복사 JS (30줄)
```

### 7.2 인터랙티브 요소

| 요소 | 섹션 | 구현 |
|---|---|---|
| 컬러 스와치 hover → 확대 + hex 표시 | `#colors` | CSS `transform: scale(1.06)` |
| 타이포 live preview | `#typography` | 실제 font-size/weight/lh/ls inline style |
| 스페이싱 시각 바 | `#spacing` | `width: {px}px` 실제 폭 막대 |
| Radius 시각 박스 | `#radius` | `border-radius: {px}` 적용된 정사각 박스 |
| Shadow 시각 카드 | `#shadows` | `box-shadow` 실제 적용 (듀얼 레이어) |
| 스크린샷 | `#hero` | `<img src="screenshots/hero-cropped.png">` 조건부 |
| Code Export 탭 전환 | `#export` | JS `data-tab` / `data-pane` 속성 기반 |
| Copy 버튼 | `#export`, `#components` | `navigator.clipboard.writeText()` |
| 컴포넌트 버튼/링크 데모 | `#components` | 실제 CSS 적용 (서비스 폰트 + 스펙) |
| Dominant colors 누적 막대 | `#colors` | flex 비율 기반 가로 바 |

### 7.3 생성 방식

**Python 스크립트(render_report.py)가 아닌 Claude Code 에이전트가 생성한다.**

이유: 서비스마다 design.md 의 테이블 컬럼 구조, 섹션 수, 데이터 형식이 다름. 정규식 파서로는 edge case 가 끝없이 나오고 (weight 에 px 값 삽입, `.875rem` 앞점 탈락, `"400 (3회)"` → `4003` 파싱 등), LLM 이 의미 기반으로 이해하는 게 더 정확.

```
생성 흐름:
1. Claude 에이전트가 GENERATE_REPORT_PROMPT.md (v2.1) 규칙 읽음
2. real/stripe/report.ko.html 골드 스탠다드 읽음 (구조/CSS/JS 참조)
3. 대상 서비스의 design.md 읽음 (데이터)
4. report.ko.html 생성 (Write)
5. 자체 체크리스트 검증 (§체크리스트 참조)
```

### 7.4 한글 네이밍 규칙

| 영역 | 처리 |
|---|---|
| CSS 속성·토큰명·클래스·hex | 영어 유지 |
| TOC 섹션명 | 혼용 외래어: 스페이싱, 라디우스, 섀도우, 컴포넌트 |
| TOC 그룹 라벨 | 영어 uppercase: Overview, Foundations, Tokens, Patterns, Code, Rules |
| 본문 설명 | 한국어 서술, 과장 부사 금지 |
| Do / Don't | 영어 유지 (번역하면 어색) |
| 첫 등장 용어 | 하이브리드: `라디우스(모서리 반경)`, `스페이싱(간격 체계)` |

### 7.5 섹션 타이틀 작성법

직역 금지, 정보 서술형:
- ❌ "일곱 개의 모서리" → ✅ "라디우스 7단"
- ❌ "가짜 데이터의 함정" → ✅ "자주 틀리는 것들"
- ❌ "그림자는 쌍으로 온다" → ✅ "섀도우는 항상 두 겹"
- 각 서비스의 핵심 특징 반영: Stripe "본문 굵기는 300이다", Linear "Marketing vs App 이중 팔레트"

### 7.6 선택 섹션 처리

design.md 에 해당 `## NN.` 이 없으면 HTML 섹션 **AND** TOC 항목 둘 다 제거.
TOC 번호는 제거 후 연속으로 재계산 (빈 번호 없이).

### 7.7 반응형 처리

`@media (max-width: 1024px)` 에서:
- sidebar → `position: relative` (sticky 해제), 상단 고정
- 2열 grid → 1열
- padding 축소 (64px → 32px)
- 악센트 그리드 4열 → 2열, 라디우스 7열 → 4열, 섀도우 3열 → 1열

### 7.8 상세 규칙 위임

Phase 5 의 상세 규칙 (에러 처리, 배치 격리, 안티패턴, 타이포 정규화, 색상 밝기 판단 등)은
**`GENERATE_REPORT_PROMPT.md` (v2.1)** 에 정의돼 있다. 이 문서에서 중복하지 않는다.

| 규칙 | 위치 |
|---|---|
| 입력 계약 (frontmatter fallback) | GENERATE_REPORT_PROMPT.md §17 |
| 타이포 컬럼 정규화 | §18 |
| 실패 정책 | §19 |
| 배치 격리 | §20 |
| 안티패턴 | §21 |
| 색상 밝기 판단 | §22 |
| 생성 후 체크리스트 | §체크리스트 |

---

## 8. Phase 6: 검증

### 8.1 자동 검증 (스크립트)

```bash
# 1. YAML frontmatter 맨 위
head -1 design.md | grep -q '^---$'

# 2. 필수 섹션 존재
for n in 01 02 03 04 05 06 07 08 12 14 16; do
  grep -q "^## $n\\." design.md || echo "Missing §$n"
done

# 3. 파일 크기
[ $(wc -c < design.md) -ge 8000 ]
[ $(wc -c < report.ko.html) -ge 20000 ]

# 4. 독립성 — 외부 소스 비교 표현 없음
grep -ci "designmd" design.md  # 0이어야 함

# 5. hex 실존 — 주요 hex 가 실제 CSS 에 있는가
for hex in $(grep -oE '#[0-9A-Fa-f]{6}' design.md | sort -u | head -5); do
  grep -qi "$hex" designmd-data/real/{slug}/css/*.css || echo "Missing: $hex"
done
```

### 8.2 수동 검증 (AI/사람)

- Quick Start 가 실제로 "3가지만 하면 80%"인가?
- 톤이 한국어로 자연스러운가?
- 토큰명이 실제 CSS 변수명 그대로인가? (가상 이름 아닌지)

---

## 9. 스크립트 vs AI 분담 요약

```
┌──────────────────────────────────────────────────────────┐
│                        스크립트 영역                       │
│  ┌──────────────────────────────────────────────┐        │
│  │ Phase 1: 수집                                │        │
│  │   fetch_site.py (5-tier fallback)            │        │
│  │   capture_screenshots.py                     │        │
│  ├──────────────────────────────────────────────┤        │
│  │ Phase 2: 추출                                │        │
│  │   parse_tokens.py                            │        │
│  │   (brand_candidates, var_resolver, typo,     │        │
│  │    alias_layer 통합)                         │        │
│  ├──────────────────────────────────────────────┤        │
│  │ Phase 6: 검증                                │        │
│  │   validate_designmd.py                       │        │
│  └──────────────────────────────────────────────┘        │
│                                                          │
│  결과: tokens.json, screenshots/, fetch_report.json       │
│  특성: 결정적. 같은 URL = 같은 결과. 재현 가능.           │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│                        AI 영역                            │
│  ┌──────────────────────────────────────────────┐        │
│  │ Phase 3: 판정                                │        │
│  │   Brand color 확정 (스크린샷 보고)            │        │
│  │   Light/Dark 테마 판정                        │        │
│  │   Custom font 식별                           │        │
│  │   Framework 식별                              │        │
│  │   Hero anatomy 서술                           │        │
│  ├──────────────────────────────────────────────┤        │
│  │ Phase 4: 작성                                │        │
│  │   16 섹션 design.md             │        │
│  │   (필수 11 + 선택 5)                          │        │
│  ├──────────────────────────────────────────────┤        │
│  │ Phase 5: 리포트                              │        │
│  │   report.ko.html (한국어, 인터랙티브)          │        │
│  └──────────────────────────────────────────────┘        │
│                                                          │
│  입력: tokens.json + screenshots/                         │
│  특성: 템플릿 제약. 팩트는 변경 안 함. 해석만 추가.      │
└──────────────────────────────────────────────────────────┘
```

### 원칙 3가지

1. **AI 는 hex 값을 만들지 않는다** — CSS 에 없는 hex 를 생성하면 검증 실패
2. **AI 는 토큰명을 만들지 않는다** — `color-brand` 같은 가상 이름 금지, 실제 `--hds-*` 사용
3. **AI 는 팩트 위에 해석만 얹는다** — "이 hex 가 브랜드 색이다" 판정은 OK, 값 자체를 바꾸는 건 NO

---

## 10. 파일 구조 (전체)

```
/Users/chulrolee/designmd-writer/
│
├── ARCHITECTURE.md             ← 이 문서 (단일 진실 소스)
├── DESIGN.claude.template.md   ← 템플릿 v2.0 (16 섹션)
├── METHODOLOGY.md              ← Phase 별 상세 (ARCHITECTURE 하위)
├── WORKFLOW.md                 ← 서비스당 절차 (ARCHITECTURE 하위)
├── DATA_COLLECTION.md          ← Phase 1 상세 (ARCHITECTURE 하위)
│
├── real/                       ← 최종 결과물
│   ├── stripe/
│   │   ├── design.md
│   │   ├── report.ko.html
│   │   └── screenshots/
│   ├── atlassian/
│   │   └── ...
│   └── ... (34개 서비스)
│
├── designmd-data/              ← 입력 데이터 + 스크립트
│   ├── real/                   ← 실제 사이트 원본 (HTML/CSS/tokens.json)
│   │   ├── stripe/
│   │   │   ├── index.html
│   │   │   ├── css/*.css
│   │   │   └── tokens.json
│   │   └── ... (34개)
│   ├── scripts/                ← Phase 1~2 스크립트
│   │   ├── fetch_site.py       (신규 예정)
│   │   ├── parse_tokens.py     (신규 예정)
│   │   ├── brand_candidates.py (기존)
│   │   ├── var_resolver.py     (기존)
│   │   ├── typo_extractor.py   (기존)
│   │   ├── alias_layer.py      (기존)
│   │   └── capture_screenshots.py (기존)
│   └── services/               ← DesignMD 원본 (분석 참고용, 불필요 시 삭제)
│
├── skills/                     ← 스킬 빌드 시 사용
│   └── designmd-analyzer/
│       ├── SKILL.md            (미구현)
│       └── references/         (미구현)
│
└── .kkirikkiri/                ← kkirikkiri 팀 세션 메모리
    ├── TEAM_PLAN.md
    ├── TEAM_PROGRESS.md
    ├── TEAM_FINDINGS.md
    └── archive/
```

---

## 11. 스킬화 시 변환 매핑

이 아키텍처가 Claude Code 스킬로 변환될 때:

```
ARCHITECTURE.md  →  SKILL.md (워크플로우 정의)
TEMPLATE.md      →  references/template.md
DATA_COLLECTION  →  references/data-collection.md
Phase 1 scripts  →  scripts/ (스킬 내장)
Phase 3~5        →  SKILL.md Step 정의 (AI 가 직접 수행)
```

### 스킬 실행 흐름

```
User: "/designmd-analyzer https://linear.app"
  ↓
Step 1: fetch_site.py linear https://linear.app   → 수집
Step 2: parse_tokens.py linear                    → 추출
Step 3: Claude 가 screenshots/ + tokens.json 읽기  → 판정
Step 4: Claude 가 template 기반 DESIGN.md 작성     → 작성
Step 5: Claude 가 report.ko.html 생성             → 리포트
Step 6: validate_designmd.py linear               → 검증
  ↓
Result: real/linear/design.md + report.ko.html
```

---

## 12. 발견된 14가지 함정

스킬 구현 시 Phase 3 (AI 판정) 프롬프트에 반드시 포함해야 할 검증 포인트:

1. **가상 토큰명 금지** — `color-brand` 아님, 실제 `--hds-*` 사용
2. **브랜드 키트 ≠ UI 색** — 로고 5색은 일러스트 전용일 수 있다
3. **리브랜딩 감지** — 구 브랜드 hex 가 CSS 에 소수만 남아있을 수 있다
4. **Light/Dark 역전** — 마케팅 사이트 ≠ 앱 UI 테마
5. **앱 UI vs 마케팅 분리** — 다른 팔레트
6. **Hero 구체 수치 필수** — 추상 서술 금지
7. **DS namespace 보존** — `--hds-*`, `--ds-*` 등 prefix 그대로
8. **Tailwind v4 `@theme`** — `--tw-*` 시그너처 감지
9. **next/font metric fallback** — `Inter Fallback` 등
10. **Warm vs Cool neutral** — `#37352F` (Notion) ≠ `#000000`
11. **Multi-layer shadow** — 2~5 레이어 stack
12. **Customer logo wall 오염** — "trusted by" SVG 로고 hex 제외
13. **Letter-spacing optical** — 큰 headings 의 negative tracking
14. **Variable font 비표준 weight** — `330/380/420/550/570` 등

---

## 13. 관련 문서 인덱스

| 문서 | 역할 | 이 문서와의 관계 |
|---|---|---|
| `ARCHITECTURE.md` | 전체 아키텍처 | **이 문서 = 최상위** |
| `DESIGN.claude.template.md` | 템플릿 v2.0 | §6 Phase 4 의 상세 구현 |
| `DATA_COLLECTION.md` | 5-tier fallback | §3 Phase 1 의 상세 구현 |
| `METHODOLOGY.md` | 분석 5단계 | §3~§8 의 절차적 설명 (구버전, 업데이트 필요) |
| `WORKFLOW.md` | 서비스당 절차 | §3~§8 의 실행 뷰 |
| `real/stripe/design.md` | Gold standard | §6 의 완성 예시 |
| `real/stripe/report.ko.html` | 리포트 gold standard | §7 의 완성 예시 |
