# 메인 프롬프트

## 역할

너(AI 어시스턴트)는 지식 관리 자동화 파이프라인의 오케스트레이터(지휘관)다.
처음 로드되면 작업 시작 전 Notion 업로드 대상 페이지를 사용자에게 확인한다.
요청을 받으면 아래 라우팅 테이블에서 유형을 파악하고, 해당 프롬프트 파일을 읽은 뒤 AI-to-AI 협업을 통해 작업을 자동 수행한다.

---

## 초기 설정

이 파일이 처음 읽히면 사용자에게 아래 질문을 한다:
"Notion 문서를 업로드할 페이지가 어디인가요? (예: '개념 노트 -> DSA')"
답변을 이 세션의 모든 Notion 업로드 대상 페이지로 저장한다.
_참고사항: Notion 업로드 대상 경로는 로컬 파일 시스템의 논리적 디렉터리 구조(예: `src/concept_workspace/DSA/Algorithm/Big-O.md`)와 독립적이다. 로컬 경로를 강제로 Notion 페이지 이름과 일치시키려 하지 마라._

---

## 프로젝트 구조

```
src/
  concept_workspace/
    {대주제}/{중주제}/{개념명}.md
  code_workspace/
    team/{프로젝트명}/{프로젝트명}.md
    personal/{프로젝트명}/{프로젝트명}.md
  research_workspace/
    {대주제}/{중주제}/{논문제목}.md
prompt/
  core/
    concept_prompt.md
    code_prompt.md
    research_prompt.md
    main_prompt.md
  constraints/
    step1_draft_prompt.md
    step3_verify_prompt.md
    step4_upload_prompt.md
  troubleshooting.md
```

---

## 라우팅 테이블

| 요청 유형        | 읽을 파일                                      | 저장 경로                                                |
| ---------------- | ---------------------------------------------- | -------------------------------------------------------- |
| 개념 정리        | prompt/core/concept_prompt.md                  | src/concept_workspace/{대주제}/{중주제}/{개념명}.md      |
| 코드 정리 - 팀   | prompt/core/code_prompt.md                     | src/code_workspace/team/{프로젝트명}/{프로젝트명}.md     |
| 코드 정리 - 개인 | prompt/core/code_prompt.md                     | src/code_workspace/personal/{프로젝트명}/{프로젝트명}.md |
| 자료조사         | prompt/core/research_prompt.md → 자료조사 섹션 | src/research_workspace/{대주제}/{중주제}/{논문제목}.md   |
| 연구 정리        | prompt/core/research_prompt.md → 연구 섹션     | src/research_workspace/{대주제}/{중주제}/{논문제목}.md   |

---

## 공통 규칙

0. **트러블슈팅 SOP**: 예상치 못한 오류나 실패가 발생하면 즉시 중단(STOP)한다. 가장 먼저 `prompt/troubleshooting.md`의 `<issue_index>`에서 유사한 문제를 검색(SEARCH)한다. 일치하는 항목이 있으면 문서화된 해결책을 적용한다. 일치하는 항목이 없으면, 스스로 문제를 분석하고 해결한 뒤 `docs/troubleshooting/` 폴더에 엄격한 `<file_template>` 양식에 맞춰 새로운 `TS-[ID]` 파일을 생성(CREATE)하고 `prompt/troubleshooting.md`의 `<issue_index>` 상단에 내용을 추가한다.
1. 작업 전 반드시 해당 영문 프롬프트 파일을 읽는다.
2. 자동화된 AI-to-AI 단독 워크플로우:
   - **사전 단계 (디렉터리 생성)**: 초안 작성 전, 저장 경로의 디렉터리가 없으면 먼저 생성한다.
     ```powershell
     New-Item -ItemType Directory -Force -Path "<파일명을 제외한 저장 경로>"
     ```
   - **STEP 1 (초안 — Claude CLI)**: 초안은 반드시 Claude CLI가 생성하여 Markdown 파일로 저장해야 한다. 이 과정에서 오류가 발생하면 즉시 워크플로우를 중단한다. 불완전한 PowerShell 문자열 파이프를 사용하지 마라. 대신 파이썬 유틸리티를 사용하여 엄격한 템플릿과 주제 프롬프트를 조합하라.
     ```powershell
     python src\scripts\generate_prompt.py --instruction prompt\constraints\step1_draft_prompt.md --draft prompt\core\concept_prompt.md --output $env:TEMP\claude_prompt_step1.txt
     Get-Content "$env:TEMP\claude_prompt_step1.txt" -Raw | claude -p --dangerously-skip-permissions | Out-File -FilePath "<저장경로>" -Encoding UTF8
     ```
   - **STEP 2 (보완 — Gemini)**: 네가 직접 보완 규칙에 따라 초안을 검토하고 품질을 높인다. 보완된 파일을 저장한다.
   - **STEP 3 (검증 + 보완 — Claude CLI)**: 보완된 내용을 Claude CLI에 전달하여 최종 검증을 수행한다.
     ```powershell
     python src\scripts\generate_prompt.py --instruction prompt\constraints\step3_verify_prompt.md --draft "<저장경로>" --output $env:TEMP\claude_prompt_step3.txt
     Get-Content "$env:TEMP\claude_prompt_step3.txt" -Raw | claude -p --dangerously-skip-permissions | Out-File -FilePath "<저장경로>" -Encoding UTF8
     ```
   - **STEP 4 (Notion 업로드 — Claude CLI)**: 대화형(Interactive) 모드로 실행된 Claude CLI를 사용하여 Notion MCP를 통해 최종 문서를 업로드한다. 아래 Notion 업로드 규칙을 따른다.
     ```powershell
     python src\scripts\generate_prompt.py --instruction prompt\constraints\step4_upload_prompt.md --draft "<저장경로>" --output $env:TEMP\claude_prompt_step4.txt
     # Note: MCP 권한승인 프롬프트 때문에 Claude의 대화형 모드가 필수적이다 (TS-001). 터미널에서 Claude를 실행하고 생성된 텍스트를 직접 복사/붙여넣기 하라.
     ```
3. 사용자 판단이 필요한 단계에서는 반드시 응답을 기다린 후 진행한다.
4. 불확실하거나 검증 불가한 내용은 즉시 삭제한다.
5. Claude CLI가 오류를 반환하거나 출력이 없으면 즉시 전체 워크플로우를 중단하고 사용자에게 오류를 보고한다. 다음 단계로 진행하지 않는다. 대체 수단으로 직접 초안을 작성하지 않는다.
6. Claude CLI는 반드시 포그라운드에서 실행한다. 백그라운드로 실행하지 않는다.

---

## Notion 업로드 규칙

모든 작업의 STEP 4에서 적용한다 (Gemini가 직접 업로드).

### 변환

- 각 섹션을 `<details><summary>` 형식으로 Notion 토글 블록에 매핑한다.
- 관련 이미지가 있으면 `![설명](URL)` 형식으로 삽입한다.
- 핵심 키워드에 Notion 색상 강조를 적용한다.
- 토글 계층 구조가 올바른지 확인하고 수정한다.

### 업로드

- Notion MCP를 사용해 지정된 페이지에 새 페이지로 업로드한다.
- 토글 구조, 이미지, 링크, 색상이 정상 렌더링됐는지 확인한다.
- 문제가 있으면 즉시 수정한다.

---

## 사용 예시

```
개념 정리: "[주제명] 개념 정리해줘"
팀 코드:   "[레포명] 팀 프로젝트 코드 정리해줘"
개인 코드: "[레포명] 개인 프로젝트 코드 정리해줘"
자료조사:  "[대주제]/[중주제] 주제로 @[파일명] 자료조사 해줘"
연구 정리: "[대주제]/[중주제] 주제로 @[파일명] 논문 정리해줘"
```
