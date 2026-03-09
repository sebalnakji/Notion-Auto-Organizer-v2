# CODE PROMPT

## GOAL

Document the project so interviewers/reviewers can understand it quickly and accurately.
Focus on logic flow and decision rationale — no code snippets.

---

## STRUCTURE

### Team Project

Required: Overview → Stack → My Role → Core Logic
Optional: Insights (only if user provides the content directly)

- Overview: 1–2 line summary of purpose and features, team size, duration
- Stack: Tech list + one-line reason for key technology choices
- My Role: Features/modules owned, scope of contribution (core)
- Core Logic: Step-by-step implementation flow, decision rationale, data flow (core)
- Insights: Troubleshooting / Performance optimization / Retrospective

### Personal Project

Required: Purpose → Stack → Key Features → Core Logic
Optional: Insights (only if user provides the content directly)

- Purpose: What problem it solves and why it was built
- Stack: Tech list + one-line reason for key technology choices
- Key Features: Feature list + what problem each feature solves (core)
- Core Logic: Step-by-step flow, decision rationale, data flow (core)
- Insights: Troubleshooting / Performance optimization / Retrospective

My Role/Key Features and Core Logic are the most critical sections. These are what interviewers focus on most.

Insights rules:

- Cannot be inferred from code alone. Write only if the user explicitly provides the content.
- If not provided, omit entirely — no exceptions.
- Troubleshooting: Problem → Cause → Solution → Result
- Performance optimization: Before/after metrics required
- Retrospective: Lessons learned, regrets, future improvements

---

## STEP 1 — Claude: Draft

```
Repo: {repo_name}
Type: {team / personal}
Task: Write portfolio draft and save to src/code_workspace/{team or personal}/{project_name}/{project_name}.md

Follow the STRUCTURE in order.
- Allocate the most effort to My Role/Key Features and Core Logic.
- Explain Core Logic using input → process → output flow.
- Write Insights only if the user has provided the content.

Rules:
- Base content strictly on the actual repo. No speculation or exaggeration.
- Use clear hierarchy for easy Notion toggle conversion.
- Self-review flow and facts before saving.
- Write in Korean. Technical terms and proper nouns (e.g. RAG, LLM) remain in their original form.
```

---

## STEP 2 — Gemini: Enhance

```
File: @{project_name}.md
Task: Improve document quality from an interviewer's perspective.

Team project review:
1. Overview: Is the purpose immediately clear?
2. Stack: Are the technology choices justifiable?
3. My Role [HIGHEST PRIORITY]: Is the contribution scope specific? Replace vague expressions with metrics or feature names.
4. Core Logic [HIGHEST PRIORITY]: Is the flow clear? Is the decision rationale convincing?
5. Insights (if present): Enhance based only on user-provided content. Do not add anything independently.

Personal project review:
1. Purpose: Is the motivation specific and relatable?
2. Stack: Are the technology choices justifiable?
3. Key Features [HIGHEST PRIORITY]: Is it clear what problem each feature solves? Restructure from problem-solving perspective if too list-like.
4. Core Logic [HIGHEST PRIORITY]: Is the flow clear? Is the decision rationale convincing?
5. Insights (if present): Enhance based only on user-provided content. Do not add anything independently.

Rules:
- Fix content that differs from or exaggerates the repo.
- Remove unnecessary explanations. Concise portfolios are stronger.
- Highlight key metrics and achievements with `> ` or `!> `.
- Save after review.
```

---

## STEP 3 — Claude: Verify & Enhance

```
File: @{project_name}.md
Task: Final verification and enhancement of any insufficient sections.

Verify:
- Overview/Purpose + Stack: Immediately understandable at a glance?
- My Role/Key Features [HIGHEST PRIORITY]: Is the contribution specific and clear?
- Core Logic [HIGHEST PRIORITY]: Is the flow clear with convincing decision rationale?
- Insights (if present): Contains only user-provided content? Check troubleshooting structure, optimization metrics, and retrospective specificity.
- Remove exaggerations, errors, and unverifiable content.
- Remove or replace invalid links.
- Fix typos and unnatural phrasing.
```
