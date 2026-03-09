# Notion-Auto-Organizer

![Claude](https://img.shields.io/badge/Claude-claude--sonnet-D97757?logo=anthropic&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?logo=googlegemini&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?logo=notion&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![Google_Antigravity](https://img.shields.io/badge/Google_Antigravity-4285F4?logo=google&logoColor=white)

Claude CLI와 Notion MCP를 활용한 **지식 관리 자동화 워크플로우**입니다.

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
STEP 0 — AI 어시스턴트(Gemini): main_prompt.md 읽기 및 작업 준비 (Notion 페이지 확인)
    ↓
STEP 1 — Claude CLI: 해당 프롬프트 기반 초안 작성 → Markdown 파일 저장
    ↓
STEP 2 — AI 어시스턴트(Gemini): 초안 검토 및 보완 (Enhance 단계)
    ↓
STEP 3 — Claude CLI: 최종 검증 및 추가 보완 → 파일 덮어쓰기
    ↓
STEP 4 — Claude CLI (대화형 모드): Notion MCP 연결을 통한 최종 문서 직접 업로드
```

---

## 프로젝트 구조

```
Notion-Auto-Organizer-v2/
├── docs/
│   ├── kor_prompt/               # 한글 프롬프트 (해석본)
│   └── troubleshooting/          # 트러블슈팅 개별 문서 (TS-[ID].md)
├── prompt/                       # 영문 프롬프트 (실제 사용)
│   ├── core/                     # 메인 및 주제별 코어 프롬프트
│   ├── constraints/              # Claude CLI 실행 제약사항 템플릿
│   └── troubleshooting.md        # 트러블슈팅 인덱스 및 SOP 가이드
├── src/
│   ├── concept_workspace/        # {대주제}/{중주제}/{개념명}.md
│   ├── code_workspace/           # team|personal/{프로젝트명}/{프로젝트명}.md
│   ├── research_workspace/       # {대주제}/{중주제}/{논문제목}.md
│   └── scripts/                  # 파이프라인 자동화 스크립트 (generate_prompt.py 등)
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

## 버전 연혁 (Changelog)

### V2.2 (현재 버전) - 작동 속도 최적화 및 워크플로우 병목 제거

- **Notion 업로드 병목(Semantic Search) 건너뛰기**: 정확한 타겟 페이지 ID(`ID: xxxxxxxx`)를 지정하여 가장 느리고 오류가 잦은 `notion-search` 단계를 생략하고 즉각 업로드(`notion-create-page`)하도록 개선.
- **인터랙티브 권한 승인 자동화 (Interactive Lock 해제)**: Claude CLI가 Notion MCP 접근 권한을 요구하며 무한 대기하는 현상을 막기 위해, 항상 `2번(Yes, and don't ask again)`을 선택하도록 전역 규칙 강제.
- **불필요한 중복 검증 생략**: 오케스트레이터(Gemini)에 의한 2단계(Enhance) 보완이 확실할 경우, 토큰과 시간을 많이 소모하는 3단계 Claude 재검증(Verify)을 거치지 않고 바로 4단계(Upload)로 직행할 수 있게 `[OPTIONAL]` 처리.
- **트러블슈팅(TS-001~003) 문서 최신화**: 파이프라인 스크립트화 및 속도 최적화 과정에서 경험한 문제와 최종 확정된 해결책 가이드를 상세 문서화.

### V2.1 - 듀얼 어조 라우팅 및 프롬프트 최적화

- **듀얼 어조 분기(Dual-Tone Routing) 시스템**: 사용자가 요청 앞에 `[story]` 또는 `[info]` 태그를 붙여 AI의 톤 앤 매너를 제어할 수 있는 기능 추가.
  - `[story]`: 테크 블로그나 교양 서적 느낌의 스토리텔링 모드.
  - `[info]`: 논문 초록이나 위키 스타일의 극도로 건조하고 직관적인 정보 압축 모드.
- **프롬프트 토큰 전면 최적화**: 모든 프롬프트(`concept`, `code`, `research`)와 시스템 제약 문서(`step1~4`), 트러블슈팅 인덱스의 지시 구조를 컴팩트한 마크다운 및 개조식으로 압축하여 API 토큰 사용량을 대폭 절감.

### V2 - 파이프라인 안정성 강화 및 구조 고도화

- **프롬프트 모듈화**: 역할에 따른 `core` 프롬프트 그룹과 Claude CLI 오작동·환각 방지를 위한 `constraints` 단계별 템플릿 분리.
- **안정적인 파일 병합 스크립트 (`generate_prompt.py`) 도입**: PowerShell 파이프 통신 시 발생하던 인코딩 밀림 및 병합 오류를 해결하기 위해 Python 기반 프롬프트 생성 유틸리티 구축.
- **트러블슈팅 SOP 체계화**: 파이프라인 실행 중 발생하는 에러에 대한 자가 해결 및 문서화(SOP) 규칙 강제화. `troubleshooting.md` 인덱스와 `docs/troubleshooting/` 폴더 구성.
- **디렉터리 구조 시맨틱 분리**: Notion 타겟 페이지 제약(예: '개념 노트' 폴더)을 없애고 로컬 파일 시스템을 완전한 논리적 계층(`{대주제}/{중주제}`)으로 리팩토링.
- **Notion 업로드 주체 변경**: 권한 승인 상호작용(Interactive)이 필요한 Notion MCP 특성을 반영하여 자동화 주체를 기존 Gemini에서 Claude CLI 포그라운드 모드로 이관 (TS-001 대응).

### V1 - 초기 구축

- **기본 AI-to-AI 협업 파이프라인**: Gemini(오케스트레이터 및 보완)와 Claude CLI(초안 작성 및 MCP 업로드) 역할 분담 구축.
- **지식 관리 카테고리화**: 개념 정리, 코드 포트폴리오, 자료조사 및 논문 리뷰 문서의 템플릿 구성.
- **PowerShell 기반 파이프라인**: 파이프 구문(`|`)과 임시 텍스트 파일을 활용한 기본적인 파이프라인 연결 구현.

---

## 버전 관리

버전은 Git 태그로 관리합니다.

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

준비가 완료되면 원하는 어조 태그(`[story]` 혹은 `[info]`)를 포함하여 작업을 요청합니다. 태그를 생략하면 기본적으로 `[story]` 모드로 동작합니다.

```
# 개념 정리
"[story] {주제명} 개념 정리해줘"

# 코드 내용 정리
"[info] {레포명} 팀 프로젝트 코드 내용 정리해줘"
"[story] {레포명} 개인 프로젝트 코드 내용 정리해줘"

# 자료조사
"[info] {대주제}/{중주제} 주제로 @{파일명} 자료조사 해줘"

# 연구 정리
"[story] {대주제}/{중주제} 주제로 @{파일명} 논문 정리해줘"
```
