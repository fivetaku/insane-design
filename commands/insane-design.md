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
  - Task
---

<!-- first-run setup: idempotent, non-blocking, self-skips after first run -->
**Step 0 — run once at the very start, before anything else:** run `bash "${CLAUDE_PLUGIN_ROOT}/setup/setup.sh" ask autoupdate`. If its output starts with `STAR_ASK`, immediately call the **AskUserQuestion** tool once, with the question and options phrased **in the user's language**: prefer the current conversation's language if it is evident; otherwise fall back to the language code that follows `STAR_ASK` in the output (`ko`→Korean, `ja`→Japanese, `en`→English). Never default to Korean blindly.
- header: a short localized "GitHub Star" label
- question: ask whether they'd like to give this plugin (and the gptaku-plugins marketplace) a GitHub ⭐ to support it — note it is optional and every feature works either way
- options: exactly two — (1) yes, star it → then run `bash "${CLAUDE_PLUGIN_ROOT}/setup/setup.sh" star yes`; (2) no thanks → then run `bash "${CLAUDE_PLUGIN_ROOT}/setup/setup.sh" star no`
- If the output contains a line `AUTOUPDATE_ASK <lang>`: ask the user ONCE with AskUserQuestion, written in the language the user is using in this conversation (fall back to <lang> — ko/ja/en — only if the conversation gives no signal). Question: gptaku-plugins can update itself automatically so you always get fixes without running /plugin manually. Turn on auto-update? Options (2): "Turn on auto-update" / "Not now".
  - "Turn on auto-update" → run `bash "${CLAUDE_PLUGIN_ROOT}/setup/setup.sh" autoupdate yes` (prints `AUTOUPDATE_SET <status>`; on `on`/`already` say it is enabled, otherwise say it could not be changed and point to /plugin → Marketplaces → gptaku-plugins → Turn on auto-update).
  - "Not now" → run `bash "${CLAUDE_PLUGIN_ROOT}/setup/setup.sh" autoupdate no`.
  If both STAR_ASK and AUTOUPDATE_ASK appear, put both questions in ONE AskUserQuestion call (two questions).

If the output is empty, just continue silently. (AskUserQuestion must NOT be in frontmatter allowed-tools.) Do not narrate beyond the question itself.

# /insane-design Command (Smart Router)

절차는 SKILL.md에 있다. 인자: `$ARGUMENTS`

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/insane-design/SKILL.md`
2. "Smart Router" 절에 따라 `$ARGUMENTS`로 analysis / apply / build 모드를 판별하고(인자 없으면 모드 선택 질문), 그 절차를 그대로 따른다.
3. Every question MUST use the AskUserQuestion tool
