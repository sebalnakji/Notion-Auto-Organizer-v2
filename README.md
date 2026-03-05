# Notion-Auto-Organizer

![Claude](https://img.shields.io/badge/Claude-claude--sonnet-D97757?logo=anthropic&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?logo=googlegemini&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?logo=notion&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![Google_Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?logo=google&logoColor=white)

Claude와 Notion MCP를 활용한 **지식 관리 자동화 워크플로우**입니다.
VSCode기반의 **Google Antigravity**를 IDE로 사용하여 개발 및 자동화 파이프라인을 구축했습니다.

개념 정리, 코드 포트폴리오, 논문 리뷰 등 다양한 지식을 일관된 구조로 정리하고 Notion에 자동 업로드합니다.

---

## 주요 기능

- **개념 정리** — Why → Where → What → How 스토리라인 기반 개념 문서 자동 생성
- **코드 포트폴리오** — 팀/개인 프로젝트를 면접관 관점의 포트폴리오 문서로 정리
- **자료조사** — 논문·자료의 핵심 주제 적합성을 2단계로 검토 후 선별 정리
- **연구 정리** — 논문을 요약본 + 상세본(서론·방법론·결과·결론) 구조로 깊이 있게 정리
- **Notion 자동 업로드** — Notion MCP를 통해 토글 구조로 변환 후 직접 업로드
- **버전 관리** — Git 태그 기반으로 프롬프트 버전을 관리하고 언제든 롤백 가능

---

## 워크플로우

```
사용자 요청 (AI 어시스턴트에게 지시)
    ↓
AI 어시스턴트 — main_prompt.md 읽기 및 작업 준비 (Notion 페이지 확인)
    ↓
AI 어시스턴트 — 터미널을 통해 Claude CLI 호출 (해당 프롬프트와 함께 초안 작성 지시)
    ↓
Claude CLI — 초안 작성 후 반환
    ↓
AI 어시스턴트 — 자체적으로 내용 보완 및 팩트 체크 (Enhance 단계)
    ↓
AI 어시스턴트 — 완성된 최종본을 다시 Claude CLI로 전달하며 업로드 지시
    ↓
Claude CLI — 최종 검증 및 Notion MCP로 지정된 페이지에 직접 업로드
```

---

## 프로젝트 구조

```
Notion-Auto-Organizer-v2/
├── kor_prompt/               # 한글 프롬프트 (해석본)
│   ├── kor_main_prompt.md
│   ├── kor_concept_prompt.md
│   ├── kor_code_prompt.md
│   └── kor_research_prompt.md
├── prompt/                   # 영문 프롬프트 (실제 사용)
│   ├── main_prompt.md
│   ├── concept_prompt.md
│   ├── code_prompt.md
│   └── research_prompt.md
├── src/
│   ├── concept_workspace/    # {대주제}/{중주제}/{개념명}.md
│   ├── code_workspace/       # team|personal/{프로젝트명}/{프로젝트명}.md
│   └── research_workspace/   # {대주제}/{중주제}/{논문제목}.md
└── .gitignore
```

---

## 프롬프트 유형

| 유형      | 설명                               | 저장 위치           |
| --------- | ---------------------------------- | ------------------- |
| 개념 정리 | 개념을 스토리라인 구조로 정리      | concept_workspace/  |
| 코드 정리 | 팀/개인 프로젝트 포트폴리오 문서화 | code_workspace/     |
| 자료조사  | 핵심 주제 기반 다중 자료 선별·정리 | research_workspace/ |
| 연구 정리 | 논문 요약본 + 상세본 구조화        | research_workspace/ |

---

## 버전 관리

프롬프트는 Git 태그로 버전을 관리합니다.

```bash
# 버전 목록 확인
git tag

# 특정 버전으로 이동
git checkout v1.0

# 최신으로 복귀
git checkout main
```

| 버전 규칙 | 의미                            |
| --------- | ------------------------------- |
| `v1.0`    | 최초 릴리즈                     |
| `v1.1`    | 프롬프트 내용 수정/보완         |
| `v2.0`    | 구조 변경 또는 새 프롬프트 추가 |

---

## 사용 방법

### 1. 작업 준비

AI 어시스턴트에게 아래와 같이 새 세션에서 작업을 지시합니다.

```
prompt/main_prompt.md를 읽고 작업을 준비해줘.
Notion 업로드 대상 페이지는 '{Notion 페이지 이름}'이야.
```

### 2. 작업 요청

준비가 완료되면 원하는 작업을 요청합니다.

```
# 개념 정리
"{주제명} 개념 정리해줘"

# 코드 정리
"{레포명} 팀 프로젝트 코드 정리해줘"
"{레포명} 개인 프로젝트 코드 정리해줘"

# 자료조사
"{대주제}/{중주제} 주제로 @{파일명} 자료조사 해줘"

# 연구 정리
"{대주제}/{중주제} 주제로 @{파일명} 논문 정리해줘"
```
