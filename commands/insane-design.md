---
name: insane-design
description: "Design system analyze / apply / build — URL extract, apply pre-analyzed style, or scaffold from scratch"
argument-hint: "[URL | slug | build]"
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

# /insane-design Command (Smart Router)

입력에 따라 analysis / apply / build 모드를 자동 판별한다. v0.2 신규: `build` 서브커맨드.

## Parse Arguments

Inspect `$ARGUMENTS` to determine the action:

| Argument Pattern | Action | 모드 |
|-----------------|--------|------|
| `http://...` 또는 `https://...` | URL 분석 시작 | → analysis |
| `build` 또는 `build ...` | 새 빌드 시작 (맨바닥 / design.md / URL) | → build |
| `[slug]` (URL이 아닌 문자열) | 해당 design.md를 프로젝트에 적용 | → apply |
| (no argument) | 모드 선택 요청 | → 아래 질문 |

## URL인 경우 → Analysis

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/SKILL.md`
2. Follow SKILL.md's 7-Step workflow with the provided URL: `$ARGUMENTS`
3. Every question MUST use the AskUserQuestion tool

## Slug인 경우 → Apply

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/insane-apply/SKILL.md`
2. Follow SKILL.md's 5-Step workflow with the provided slug: `$ARGUMENTS`
3. Every question MUST use the AskUserQuestion tool

## `build` 인 경우 → Build (🆕 v0.2)

1. Read `${CLAUDE_PLUGIN_ROOT}/_shared/README.md` — 공통 계약
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/insane-build/SKILL.md`
3. Follow SKILL.md's Step 0~4 workflow. 남은 인자는 build 서브에 전달 (`$ARGUMENTS`의 `build ` 이후 텍스트).
4. Every question MUST use the AskUserQuestion tool

## 자연어인 경우 → 의도 판별

사용자가 URL도 slug도 build 리터럴도 아닌 자연어를 입력한 경우:
- "분석해줘", "CSS 뜯어봐", "디자인 시스템 뽑아줘" → analysis 모드 (URL 요청)
- "적용해줘", "이 스타일로", "처럼 만들어줘" → apply 모드 (slug 요청)
- "만들어줘", "빌드", "처음부터", "랜딩 만들어줘", "덱 만들어줘", "카드뉴스 만들어줘" → build 모드

## No Argument Provided

**EXECUTE:** 아래 JSON으로 AskUserQuestion 도구를 즉시 호출한다:

```json
{
  "questions": [
    {
      "question": "무엇을 할까요?",
      "header": "모드 선택",
      "options": [
        {"label": "사이트 분석 (analysis)", "description": "URL을 입력하면 해당 사이트의 디자인 시스템을 분석해서 design.md + report를 생성해요."},
        {"label": "디자인 적용 (apply)", "description": "이미 분석된 디자인(Stripe, Apple 등 100개)을 내 프로젝트에 적용해요."},
        {"label": "🆕 새 빌드 (build)", "description": "맨바닥에서 랜딩/덱/카드뉴스/디자인 시스템 카탈로그를 즉석 합성 또는 design.md 기반으로 빌드해요."}
      ],
      "multiSelect": false
    }
  ]
}
```

- "사이트 분석" → analysis 모드 진입 (URL 입력 요청)
- "디자인 적용" → apply 모드 진입 (slug 선택 요청)
- "새 빌드" → build 모드 진입 (entry 분기 질문)
