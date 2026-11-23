# Codex에서 실행할 때 (insane-design · insane-apply · insane-build 공통)

SKILL.md 절차는 그대로 따르고, 아래 차이만 적용한다. `${CLAUDE_PLUGIN_ROOT}`는 이 플러그인 루트(SKILL.md에서 두 단계 위 폴더)로 바꿔 읽는다.

## 질문 = 질문 도구 (이번 세션 도구 목록으로 판단)

1. `request_user_input_async`가 있으면 `AskUserQuestion` 1콜 = 이 도구 1콜(문항 ≤4).
   - 형식: `{"questions":[{"title":"헤더 — 질문","options":["추천안 (추천) — 설명","대안 — 설명"]}]}`
   - 문항에는 `title`·`options`만. `question`·`header`·`id`를 넣으면 파싱 오류가 난다(2026-11-23 실측).
   - 추천안을 맨 앞에. "기타" 옵션은 넣지 않는다(자유 입력 칸이 붙는다). SKILL.md의 JSON 예시(`question`·`header`·`label`)는 Claude용이니 `title`·`options` 문자열로 옮긴다.
   - 부른 뒤 "위 질문에 답해 주시면 이어서 진행합니다" 한 줄만 쓰고 턴을 끝낸다. 답은 다음 사용자 메시지로 온다.
2. Plan 모드에서 `request_user_input`만 있으면: 1콜 3문항까지(넘으면 나눔), `header`(12자 이내)·`id`(snake_case)·`question`, 선택지 2~3개, 추천 라벨 끝에 `(Recommended)`.
3. 둘 다 없으면 채팅에 번호 블록(`질문:` + `1. 추천안 — 설명` / `2. 대안` / `3. 문장으로 직접 수정 요청`)으로 묻고 "모르면 1번으로 진행"을 덧붙인다.
4. `codex exec`처럼 사람이 답할 수 없는 실행이면 묻지 않고 추천안으로 진행하고 가정을 결과에 적는다.

선택지 `multiSelect`는 제목 끝에 "(여러 개면 쉼표로)". `preview`가 있으면 도구 호출 직전에 채팅에 짧게 먼저 보인다.
analysis는 추출형이라 URL이 있으면 묻지 않는다(URL이 없을 때만 질문).

## Claude 전용 도구 대체

- 스킬 호출(`/insane-design:apply`·`build` 등) → 해당 `skills/<이름>/SKILL.md`를 열어 그 절차를 따른다. 슬래시 명령(`commands/`)은 Codex에서 쓰지 않는다.
- 비동기 verifier(`Task(run_in_background)`, `check_job_status`/`wait_for_job`/`list_jobs`) → Codex에는 없다. `spawn_agent`로 같은 지시를 맡기고(불가하면 같은 턴에 grep 검증을 직접 수행), 결과는 사용자가 "검증 결과 보여줘"라고 할 때 회수해 보고한다. 자동으로 다음 턴에 주입하지 않는다.
- `verify` 모드의 job 조회 → 스폰한 에이전트의 결과 회수로 대체한다.

## 브라우저·스크린샷 (Codex 샌드박스)

- 기본 경로는 브라우저가 필요 없다: curl(Tier 1~2), Jina Reader HTML·스크린샷(Tier 3), curl_cffi(Tier 4), Wayback(Tier 5). 먼저 이것으로 끝낸다. Jina는 대상 URL을 r.jina.ai로 보내므로 외부 네트워크 허용이 필요하다.
- Tier 6 · 2차 스크린샷은 파이썬 headless Playwright(`import playwright`가 되고 chromium이 설치돼 있을 때만). Codex 샌드박스에서는 네트워크 차단·chromium 실행 권한 때문에 실패할 수 있다 — 실패하면 승인(권한 상승) 요청 없이 건너뛰고 "스크린샷 없이 CSS 기반으로 진행"을 결과에 한 줄 적는다. 오너가 권한 상승을 허용한 세션에서만 실행한다.
- Playwright MCP·aside-browser 같은 외부 브라우저 도구는 Codex 기본 환경에 없다. 없으면 쓰지 않는다. 사용자의 로컬 브라우저 창을 띄우지 않는다.
- build 완료 시 `open`/`xdg-open`으로 v1을 여는 단계는 샌드박스에서 실패해도 무시하고 산출물 경로만 알린다.
- playwright 미설치는 정상 경로다(grep-only 검증, 설치 강요 금지).

## 그 밖의 차이

- 첫 실행 설정(`setup/setup.sh`)과 별 표시·자동 업데이트 질문은 Claude Code 전용이다. Codex에서는 실행하지 않는다.
- design.md 산출 위치(`insane-design/{slug}/`, `insane-build/{session}/`)는 현재 작업 폴더 기준으로 동일하다.
