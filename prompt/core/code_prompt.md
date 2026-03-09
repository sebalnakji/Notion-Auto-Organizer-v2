# CODE PROMPT

**Goal**: Professional portfolio documentation for interviewers. (No code snippets)

## TONE & MANNER ROUTING

Adjust the tone based on the user's provided tag:

**[story] (Engaging Narrative Mode)**

- **Goal**: Engaging, story-driven portfolio.
- **Tone**: Polite, friendly Korean ("~했습니다", "~합시다").
- **Style**: Connect purpose and logic seamlessly so the interviewer naturally grasps the project context. Make rationales easy to relate to.

**[info] (Fast Information Mode)**

- **Goal**: Concise, highly scannable resume/wiki style.
- **Tone**: Objective, precise, and direct Korean ("~함", "~임", "~구현").
- **Style**: Focus strictly on metrics, data flow, and fact-driven impact. No filler narrative. Bullet points highly encouraged.

---

## STRUCTURE

**[Team Project]**: Overview → Stack → My Role → Core Logic
**[Personal Project]**: Purpose → Stack → Key Features → Core Logic
**[Common Optional]**: Insights (Troubleshooting / Perf Optimization / Retrospective)

- **Overview / Purpose**: Purpose, features, team/duration.
- **Stack**: Tech list + 1-line rationale.
- **My Role / Key Features [CORE]**: Specific contribution scope / Problem solved.
- **Core Logic [CORE]**: Step-by-step data flow, decision rationale.
- **Insights [Optional]**: Use ONLY if explicitly provided by user.
  - _Troubleshooting (Problem→Cause→Solution→Result)_
  - _Perf Opt (Before/after metrics)_

---

## STEP 1 — Claude: Draft

- **Task**: Draft `src/code_workspace/{team|personal}/{project_name}/{project_name}.md`.
- Allocate most effort to **[CORE]** sections.
- Verified facts only from repo. No exaggerations.
- Write in Korean (preserve technical terms in English like RAG).
- **CRITICAL**: Apply the requested Tone & Manner (`[story]` or `[info]`) precisely.
- Use clear hierarchy for Notion toggles.

## STEP 2 — Gemini: Enhance

- **Task**: Improve interviewer appeal in `@{project_name}.md`.
- Refine **[CORE]** sections: Replace vague expressions with metrics/features.
- Highlight key metrics/achievements with `> ` or `!> `.
- **CRITICAL**: Enforce the requested Tone & Manner strictly throughout the entire document.
- DO NOT hallucinate Insights. Enhance only provided content.

## STEP 3 — Claude: Verify & Enhance

- **Task**: Final polish of `@{project_name}.md`.
- Verify clarity of **[CORE]** sections & rationales.
- Validate Insights structure (metrics/flow) if present.
- **CRITICAL**: Ensure the document perfectly matches the requested Tone & Manner (`[story]` or `[info]`). Fix contradictory phrasing.
- Remove misleading, exaggerated, or unverifiable claims. Fix typos.
