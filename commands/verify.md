---
name: verify
description: "Poll async verifier forked by insane-apply Step 3.5 or insane-build Step 3.5 — collects §18 DON'T violations + screenshot diff (if playwright)"
argument-hint: "[job_id]"
allowed-tools:
  - Bash
  - Read
  - Grep
  - Task
---

# /insane-design:verify Command (v0.2 신규)

apply Step 3.5 / build Step 3.5에서 포크된 비동기 verifier의 결과를 **명시적으로** poll 한다.
자동 다음 턴 주입은 Claude Code가 보장하지 않으므로, 이 커맨드가 결과 수거의 유일한 경로다
(`_shared/README.md` §3, §6 표기 규약).

## Parse Arguments

| Argument | Action |
|---------|--------|
| `[job_id]` | 해당 job의 상태 + 결과 조회 |
| (no argument) | 최근 30분 내 포크된 verifier job 목록 제시 |

## Execute

### job_id 제공된 경우

1. `check_job_status(job_id=$ARGUMENTS)` 로 상태 조회:
   - `running` / `spawned` → "아직 실행 중. 10~30초 후 다시 호출하세요" 안내 후 종료
   - `completed` → 결과 수거 (아래 2단계)
   - `failed` → 실패 사유 보고, Task 재포크 제안
2. `wait_for_job(job_id=$ARGUMENTS, timeout_ms=5000)` 로 결과 JSON 획득
3. JSON 파싱 후 사용자에게 보고:
   ```
   🔍 Verifier 결과 ({job_id}):

   §18 DON'T 위반 (N건):
     - line 45: background: #FFFFFF (design.md §18 "Tesla는 #F4F4F4")
     - line 127: color: #000000 (design.md §18 "#1D1D1F 사용")

   {playwright 모드일 때만}
   📸 스크린샷 diff: insane-build/{session}/variations/v1/screenshot.png
     vs reference: ~{유사도}%

   수정하려면: "위 위반을 수정해줘" 라고 요청하세요.
   ```

### job_id 제공되지 않은 경우

`list_jobs(status="completed")` 로 최근 30분 내 verifier jobs 조회.

완료된 job이 2개 이상이면 AskUserQuestion으로 선택지 제시:

```json
{
  "questions": [
    {
      "question": "어떤 verifier 결과를 확인할까요?",
      "header": "Verifier Jobs",
      "options": [
        {"label": "{job_id_1}", "description": "apply/build 구분 + 포크 시각 + session slug"},
        {"label": "{job_id_2}", "description": "..."}
      ],
      "multiSelect": false
    }
  ]
}
```

완료된 job이 0개면 안내만 출력: "최근 포크된 verifier가 없습니다. apply Step 3.5 / build Step 3.5에서 먼저 포크하세요."

## 에러 핸들링

| 상황 | 처리 |
|------|------|
| `check_job_status` 미지원 (구버전 Claude Code) | "이 기능은 최신 Claude Code에서만 동작합니다" 안내 |
| job_id 형식 오류 | 유효한 job_id 형식 안내 |
| job 만료 (1시간 초과) | 재포크 제안 |
| playwright 모드 결과인데 screenshot 파일 없음 | grep 결과만 보고, screenshot 경고 1줄 |

## References

- `${CLAUDE_PLUGIN_ROOT}/_shared/README.md` §3 Verifier Protocol
- `${CLAUDE_PLUGIN_ROOT}/skills/insane-apply/SKILL.md` Step 3.5
- `${CLAUDE_PLUGIN_ROOT}/skills/insane-build/SKILL.md` Step 3.5
