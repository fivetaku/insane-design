---
name: insane-design
description: "디자인 시스템 분석(analysis) + 적용(apply) — URL로 분석하거나, 분석 결과를 내 프로젝트에 적용"
argument-hint: "[URL 또는 slug]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

# /insane-design Command (Smart Router)

입력에 따라 analysis 또는 apply 모드를 자동 판별한다.

## Parse Arguments

Inspect `$ARGUMENTS` to determine the action:

| Argument Pattern | Action | 모드 |
|-----------------|--------|------|
| `http://...` 또는 `https://...` | URL 분석 시작 | → analysis |
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

## 자연어인 경우 → 의도 판별

사용자가 URL도 slug도 아닌 자연어를 입력한 경우:
- "분석해줘", "CSS 뜯어봐", "디자인 시스템 뽑아줘" → analysis 모드 (URL 요청)
- "적용해줘", "이 스타일로", "처럼 만들어줘" → apply 모드 (slug 요청)

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
        {"label": "디자인 적용 (apply)", "description": "이미 분석된 디자인(Stripe, Apple 등 100개)을 내 프로젝트에 적용해요. 카테고리별로 선택 가능."}
      ],
      "multiSelect": false
    }
  ]
}
```

- "사이트 분석" → analysis 모드 진입 (URL 입력 요청)
- "디자인 적용" → apply 모드 진입 (slug 선택 요청)
