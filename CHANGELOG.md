# Changelog

## [0.3.2] - 2026-05-03 — Validator + examples sync + verification

### Added
- 🆕 `scripts/validate.py` — v3.2 design.md 8-check validator
  - schema_version, frontmatter_required, mandatory_sections (15)
  - craft_floor (>=5), negative_space_floor (>=5), known_gaps_floor (>=3)
  - file_size (>=12KB), direction_summary_format (4-line block)
  - Usage: `python3 validate.py <file_or_dir>` / `--summary-only` / `--json`

### Fixed
- `skills/insane-design/examples/` 100 site 동기화
  - 51 site schema 3.1 + 49 site unmarked → 100 site schema 3.2

### Verified
- 100/100 site validator PASS (모든 8 checks)
- Best-of-merge (preboost vs current): 0 substitution 필요 (current 모두 우월)
- Aesthetic Anchoring 위반: 0/100
- §13-3 craft 평균 5.0, §00 narrative metaphor 평균 9.70

## [0.3.1] - 2026-05-03 — v3.3 Narrative Vocabulary Catalog

> **목표**: §00 narrative metaphor 빈도 끌어올리기 — 100 site batch에서 metaphor 평균 8.89인데 21 site는 < 3 (archetype-vocabulary mismatch).
> 71 getdesign.md ref 분석으로 archetype별 어휘 카탈로그 확보.

### Added
- 🆕 `references/narrative-vocabulary.md` — 10 archetype × top metaphor + first-sentence 패턴 5종 + Aesthetic Anchoring 적용 예시
- SKILL.md §00 Narrative 가이드에 archetype quick-ref 표 + first-sentence 패턴 + v3.3 negative constraint 추가

### Notes
- ADDITIVE-only — schema_version 3.2 그대로 유지
- 기존 100 site 산출물 재실행 불필요 (선택적 보강만)
- 21 약점 site 선별 재실행 시 어휘 floor 충족 기대

## [0.3.0] - 2026-05-03 — Designer Guidebook Transition (schema 3.2)

> **목표**: design.md 산출물을 awesome-design-md (getdesign.md) 수준의 디자이너 가이드북으로 전환.
> Engineer spec → Designer guidebook. 위는 영혼 (자유 narrative + 비유), 아래는 기계 계약 (apply 정규식 호환).
> **검증**: Apple/Airbnb/Ferrari/BMW 4 사이트 fresh run — ref 도달률 평균 **150%**.

### Added (ADDITIVE only — BREAKING 0)

#### Schema 3.2 frontmatter
- `archetype` + `archetype_confidence` (11 enum + freeform)
- `design_system_level` + `_evidence` (lv1 / lv2 / lv3)
- `colors:` / `typography:` / `components:` 객체 그래프 (OPTIONAL Cross-reference)

#### template.md 신규 sub-sections
- §00 샌드위치: `### Narrative` (자유) + `### Key Characteristics` + `### 🤖 Direction Summary`
- §04 `### Note on Font Substitutes`
- §05 `### Principles` (4-6 numbered)
- §06-8 `### Color Stories` (상위 4 색만)
- §07 `### Whitespace Philosophy`
- §13-2 `### Named Variants` (사이트별 0-N)
- §13-3 `### Signature Micro-Specs` (craft 결합 명칭)
- §18 `### 🚫 What This Site Doesn't Use` (Negative-Space)
- §19 신규 필수: **Known Gaps & Assumptions**

#### SKILL.md 판정 6건 (16 → 22)
- #17 Negative-Space / #18 Signature Micro-Specs / #19 Typography Principles / #20 Known Gaps / #21 Archetype / #22 design_system_level

### Changed
- §00 자유화: 4문단 강제 → 자유 narrative 3-6 문단
- §13 Components 3-tier (Core / Named Variants / Signature Micro-Specs)
- Step 3 EXTRACT 순서: `var_resolver` 먼저 → `brand_candidates` (resolved_tokens.json 활용)

### Fixed
- `apply-workflow.md` §14 → §15 자체 모순 해결
- `brand_candidates.py`: var() 체인으로만 정의된 토큰 추출 가능 (Ferrari `--f-` miss 회귀 해결)

### Documented
- `architecture.md` v2.0 deprecation + v3.2 매핑
- `_shared/README.md` schema 3.2 + 하위 호환 정책

### Verified

| 사이트 | v3.1 | v3.2 | ref | 도달률 |
|--------|----:|----:|----:|:---:|
| Apple (Claude) | 20.4 KB | 37.4 KB | 36.2 KB | **101%** |
| Apple (Codex)  | — | 32.9 KB | 36.2 KB | 91% |
| Airbnb         | 29.7 KB | 44.7 KB | 30.5 KB | **147%** |
| Ferrari        | 10.9 KB | 48.3 KB | 24.3 KB | **199%** |
| BMW            | 5.0 KB  | 42.1 KB | 27.9 KB | **151%** |

### Migration
- v3.1 산출물 호환 (apply/build default 처리)
- v3.0 산출물 = stale corpus, 재생성 권장
- BREAKING 0 — apply Phase 3 정규식 모두 보존

## [0.2.2] - 2026-04-22

### Fixed

- **Build 스킬 레퍼런스 활용률 ~3% 결함 (RCA R6~R8)** — 쿠팡 드라이런 결과물을 시각 검증한 결과, `design.md` 17KB 요약만 읽고 `examples/coupang/`의 나머지 자산(375KB `index.html`, 15개 CSS, `phase1/` JSON, 실측 `screenshots/hero-cropped.png`)을 전혀 읽지 않은 채 빌드. 그 결과 브랜드 정체성(쿠팡 = 정보 밀도 최우선) 대신 임의의 Stripe-influenced 거대 히어로 타이포가 생성됨. 다음 3건 패치:
  - **R6: Phase 0 Visual Grounding Pass 신설** — reference_slug이 있을 때 Step 2-A 본체 진입 전 4개 자산 필수 Read (`screenshots/hero-cropped.png`, `phase1/typography.json`, `phase1/brand_candidates.json`, `phase1/alias_layer.json`). 선택 자산으로 `index.html`, `css/stylesheet_00.css`. 자가 점검 3종 assertion 추가.
  - **R7: Signature ↔ Brand 충돌 감지** — Step 1.7 진입 직전 `bold_direction / aesthetic_category` vs `signature_element` 호환성 rule table로 필터링. 비호환 시그니처는 AskUserQuestion 옵션에서 제거 또는 ⚠️ 경고 description. 예: Coupang = 유틸리티 → `hero_impact` / `typo_contrast` / `minimal_extreme` 모두 비호환, `section_transition`만 허용.
  - **R8: 이미지 placeholder 전략** — 콘텐츠 시드에 이미지 URL 0개 + 카드 3개 이상이면 placeholder mode 활성화. `<picture class="thumb" data-role="placeholder">` + aspect-ratio 매체별 기본값 (web 커머스 1:1, 블로그 16:9, card-news 1:1 or 4:5, design-system 16:9, slide 3:2). Lorem ipsum 금지, 단순 치수 표기 또는 이니셜만.

### Notes

- 이번 사이클은 스킬 개선만 진행, 결과물 재빌드는 하지 않음 (사용자 결정).
- 실제 효과 검증은 차후 드라이런으로 확인 필요. v0.2.1 드라이런 결과물(`coupang-handcream-20260422-1733/v1/index.html`)은 그대로 두되 문제를 명시.

## [0.2.1] - 2026-04-22

### Fixed

- **Build 스킬 레퍼런스 감지 결함 (RCA R1~R5)** — 첫 실사용 드라이런에서 `coupang_핸드크림_20260421.md`를 입력받고도 스킬이 `examples/coupang/design.md`를 자동 매칭하지 않고 "맨바닥 즉석 합성" 경로로 자의 진입하는 버그. 다음 4건 패치:
  - **Pre-Step 0 신설** — 사용자 발화/파일명/기존 프로젝트 디렉토리에서 slug 후보 자동 추출 + `Glob "examples/*/design.md"` 전수 스캔 강제. Step 0 직전의 하드 prerequisite.
  - **Step 0 옵션 동적 재배치** — 감지된 slug이 있으면 "`{slug}` 레퍼런스 사용 (감지됨 — 추천)" 을 1번 옵션 + default로 고정. 맨바닥 즉석 합성은 항상 "마지막 수단"으로 마킹.
  - **Step 0.5 진입 assertion** — 맨바닥 합성 진입 전에 "Glob 호출했는가?" + "사용자가 명시적으로 레퍼런스를 거부했는가?" 2개 self-check 강제. 통과 못 하면 Step 0 AskUserQuestion 재호출.
  - **§18 per-brand 경고** — `_shared/README.md` §2.2 + `insane-build/SKILL.md` Step 2에 "§18 DON'T는 per-brand contract. 즉석 합성 시 다른 브랜드 §18 복사 금지" 경고 블록 추가. 쿠팡 재현이면 `#FFFFFF` 배경이 정답, Tesla 재현이면 금지.

## [0.2.0] - 2026-04-19

### Added

- **`insane-build` 신규 스킬** — 맨바닥 / design.md / URL 레퍼런스 3경로 중 선택해 HTML+CSS를 즉시 빌드. 기본 variation v1 × 1, `--variations=3` 옵션 시에만 v1 극단 / v2 절충 / v3 novel 3개 생성.
- **`_shared/README.md`** — 3개 스킬(analysis / apply / build)이 공유하는 단일 계약 문서. Identity(페르소나 락인) + Contract(§18 DON'T grep + frontmatter v3.1) + Verifier Protocol + AI Slop Extended 12 패턴 + Starter Components 인덱스 통합.
- **`_shared/starter-components/`** — 매체별 HTML 프리셋. `web/` (hero·nav·section·footer), `slide/deck-16x9.html` + 화자 노트, `design-system/catalog.html`, `card-news/` (Instagram 1:1, 4:5, KakaoTalk OG 세이프존), `motion/` (스텁).
- **design.md frontmatter v3.1** — `schema_version: 3.1` 최상단 필수, `medium` (web / slide / design-system / card-news / motion / print) + `medium_confidence` (high / medium / low) 필드 추가.
- **analysis Step 1 매체 감지** — URL 확장자·경로 패턴 + 이미지 비율로 medium 자동 분류.
- **apply Step 3 §18 DON'T grep 쿼터** — 색상 2 / 구조 2 / 타이포 2 최소 6회 grep 호출 강제. 쿼터 미충족 시 Step 3 미통과 처리.
- **apply Step 3.5 비동기 verifier 포크** (opt-in) — `Task(run_in_background=true)` + `/insane-apply verify {job_id}` 명시 polling 커맨드. 자동 다음 턴 주입은 폐기.
- **페르소나 락인 블록** — apply/build SKILL.md 상단에 "expert designer + user as manager" 5줄 Identity 선언 (Claude Design 2026-04-17 프롬프트 차용).
- **build Step 1.7 페르소나 assertion** — 미학 설정 AskUserQuestion 직전 identity 재확인, 중립 옵션 대신 "추천" 태그 유지.
- **plugin.json 키워드 확장** — `insane-apply`, `insane-build`, `redesign`, `scaffold` 추가.
- **라우터 커맨드 확장** — `/insane-design` 라우터에 `build` 서브커맨드 분기 추가. `/insane-design:build` 독립 커맨드 신설.
- **`/insane-design:verify` 커맨드 신설** — apply Step 3.5 / build Step 3.5에서 포크된 비동기 verifier 결과를 `job_id`로 명시 poll. `check_job_status` + `wait_for_job` 사용. job_id 없이 호출하면 최근 30분 내 완료된 job 리스트 제시.
- **Cross-platform `open` 분기** — build Step 4에 macOS(`open`) / Linux(`xdg-open` → `sensible-browser` 폴백) / Windows(`start`) / 미인식 OS(경로 출력) 4-way case 분기. 실패 시 crash 없이 경로만 출력.
- **starter `{TOKEN}` 치환 파이프라인 명문화** — build Step 2에 3-Layer 규칙 추가 (Layer 1: CSS 토큰 = `:root {}` 통째 교체, Layer 2: `{TOKEN}` 콘텐츠 치환 맵, Layer 3: Unforgettable/모션 조건부 주입). 치환 실패 시 원본 토큰 유지 + 미치환 리스트 경고.

### Changed

- **`schema_version` 표기 정렬** — 모든 템플릿 / 문서에서 v3.0 → **v3.1**로 통일. v3.0 파일은 `medium: web`, `medium_confidence: medium`로 하위호환 처리, 경고만 출력, 재생성 강요 금지.
- **Tweaks 라이브 토글 표기** — `localStorage + postMessage` → **`localStorage + URL hash + 재생성` 3단 조합**. postMessage는 Claude Code에서 보장되지 않는 호스트 계약이므로 폐기.
- **비동기 verifier 결과 수거 방식** — "자동 다음 턴 주입" → **명시적 사용자 polling 커맨드** (`/insane-apply verify`, `/insane-build verify`). Claude Code 네이티브 미보장 메커니즘 제거.
- **Playwright 의존 관계** — 필수 의존에서 **감지형 optional fallback**으로 변경. 미설치 환경이 기본 경로, 설치 시 스크린샷 diff 추가. 설치 강요 금지.
- **build variations 기본값** — "v1 / v2 / v3 3개 병렬 생성"에서 **v1 × 1 (토큰 경제 우위 유지)** 로 변경. 3개 variation은 사용자 명시 요청 시에만 opt-in.

### Fixed

- apply Step 3 검증이 design.md §18 DON'T의 색상 hex를 grep 하지 않고 통과하던 갭 — 최소 grep 쿼터 6회로 강제.
- URL 입력 시 자동 analysis 서브호출이 사용자 의도를 오판하던 UX — AskUserQuestion으로 명시 확인으로 전환.
- `_shared/` 디렉토리를 persona.md + contract.md + verifier.md + ai-slop-extended.md 4파일로 분리하던 과잉 구조 — 단일 `_shared/README.md`로 통합.

### Removed

- slide 9:16 세로 덱 프리셋 (한국 모바일 덱 수요 1차 증거 0)
- build Step 0.5에서 AskUserQuestion 2+3회 인터뷰 (1회 압축 폼으로 통합)
- build Step 3의 verifier × 3 병렬 (토큰 폭주 + 포트 경합 — 단일 동기 grep + optional 비동기 포크로 대체)

### Notes

리서치 근거는 `RESEARCH/insane_design_upgrade_20260419/` 하위에 보존:
- `HANDOFF.md` — 업그레이드 구현 가이드
- `outputs/executive_summary.md` — 10 핵심 교훈
- `artifacts/B2_architecture_spec.md` — 아키텍처 상세
- `artifacts/B3_critical_review.md` — 피해야 할 것
- `sources/claude-design-original.txt` — Claude Design (2026-04-17) 유출 프롬프트

---

## [0.1.0] - 2026-04-12

### Added

- 최초 릴리스. `/insane-design [URL]` analysis + `/insane-design [slug]` apply 투트랙.
- `insane-design` 스킬 (7-Step: INIT / FETCH / EXTRACT / INTERPRET / WRITE-MD / RENDER-HTML / VALIDATE)
- `insane-apply` 스킬 (Lv1 토큰 / Lv2 스타일 / Lv3 전체 리디자인 3단계)
- 100개 사전 분석 사이트 (Stripe, Apple, Linear, Tesla, Toss, Nike 등)
- `references/template.md` v3.0 — 19섹션 (§00~§18) design.md 템플릿
- `references/redesign-aesthetics.md` — BOLD 방향성 12가지 + AI Slop 안티패턴
