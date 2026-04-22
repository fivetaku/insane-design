---
name: build
description: "Scaffold a new site / deck / card / catalog from design.md (or synthesize on the fly) — insane-build skill router"
argument-hint: "[design.md path | URL | --variations=3]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - AskUserQuestion
  - Task
---

# /insane-design:build Command (v0.2 신규)

design.md를 기반으로 (또는 맨바닥에서 즉석 합성해) 새 HTML+CSS 빌드를 생성한다.
기본은 v1 × 1 variation. `--variations=3` 또는 "v1 v2 v3 만들어줘"가 있을 때만 3개 생성.

## Parse Arguments

Inspect `$ARGUMENTS`:

| Argument Pattern | Action |
|-----------------|--------|
| 경로 (`./...` 또는 `insane-design/*/design.md`) | 해당 design.md로 빌드 |
| `http://...` 또는 `https://...` | URL 레퍼런스 (사용자 명시 승인 후 analysis 선행) |
| `--variations=3` 또는 "v1 v2 v3" 언급 | 3개 variation 생성 (opt-in) |
| (no argument) | entry 분기 질문 |

## Execute

1. Read `${CLAUDE_PLUGIN_ROOT}/_shared/README.md` — 공통 계약 (Identity · Contract · Verifier · AI Slop · Starter Components)
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/insane-build/SKILL.md`
3. Follow SKILL.md Step 0~4. `$ARGUMENTS`가 경로면 Step 1로, URL이면 Step 0에서 "URL 레퍼런스" 옵션 기본 선택, 인자 없으면 Step 0 entry 분기부터 시작.
4. Every question MUST use the AskUserQuestion tool
5. **URL 자동 analysis 서브호출 금지** — 사용자가 "URL 레퍼런스로 분석 후 빌드" 옵션을 **명시 선택**한 경우에만 analysis 실행.

## 산출물 경로

```
insane-build/{session}/
├── design.md                 ← (맨바닥 선택 시) Step 0.5에서 즉석 합성
├── variations/
│   ├── v1/index.html         ← 기본
│   ├── v2/index.html         ← --variations=3 선택 시만
│   └── v3/index.html         ← --variations=3 선택 시만
└── (playwright 감지 시) variations/v1/screenshot.png
```

Step 4 완료 시 `open` 명령으로 v1을 브라우저에 자동 오픈한다.
