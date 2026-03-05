# RESEARCH PROMPT

## TYPES

- Literature Review: Collect and evaluate multiple sources on a core topic. Assess relevance before documenting.
- Research Note: Summarize a paper/file in depth with an abstract + detailed breakdown.

---

## LITERATURE REVIEW

### Flow

```
Abstract → 1st review → user judgment
  NO  → delete file, stop
  YES → read full paper → final review → user judgment
          NO  → delete file, stop
          YES → write draft → save
```

### STEP 1 — Claude: Relevance Check + Draft

```
Core topic: {core_topic}
File: @{filename}

[A. 1st Review — read abstract only]
Present opinion in the format below and wait for user judgment.
Do not proceed to the next step before receiving a response.

> 1st Review
> Title: {title}
> Abstract summary: {one line}
> Relevance: {high / medium / low} — {reason}
> Recommendation: {proceed / exclude}
> Shall I read the full paper and continue?

- NO  → delete file, stop
- YES → proceed to B

[B. Final Review — read full paper]
Present opinion in the format below and wait for user judgment.
Do not proceed to the next step before receiving a response.

> Final Review
> Core argument: {one line}
> Differs from abstract: {yes / no} — {details}
> Final relevance: {high / medium / low} — {reason}
> Recommendation: {document / exclude}
> Shall I document this paper?

- NO  → delete file, stop
- YES → proceed to C

[C. Write Draft]
Write and save to src/research_workspace/{major_topic}/{sub_topic}/{paper_title}.md

1. Basic info: title, author, source, year
2. Relevance to core topic: how it contributes to {core_topic} in 2–3 sentences
3. Core content [MOST IMPORTANT]: key argument, evidence, conclusion. Explain technical terms in plain language.
4. Key data/evidence: figures, experimental results, or cases supporting the core argument
5. Application points [optional]: how this source can be used in research/projects

Rules:
- Base content strictly on the source. No speculation or arbitrary interpretation.
- Use clear hierarchy for easy Notion toggle conversion.
- Self-review against the original before saving.
- Write in Korean. Technical terms and proper nouns (e.g. RAG, LLM) remain in their original form.
```

### STEP 2 — Gemini: Enhance

```
File: @{paper_title}.md
Core topic: {core_topic}

Review:
1. Basic info: Fill in any missing fields.
2. Relevance to core topic: Clarify if unclear.
3. Core content [HIGHEST PRIORITY]: Is the argument/conclusion clear? Are technical terms unexplained? Does any phrasing differ from the original?
4. Key data/evidence: Are figures and sources accurate?
5. Application points (if present): Are they specific and practical?

Rules:
- Fix content that differs from the original. Remove uncertain content.
- Highlight key figures and arguments with `> ` or `!> `.
- Save after review.
```

### STEP 3 — Claude: Verify & Enhance + Notion Upload

```
File: @{paper_title}.md
Task: Final verification then Notion upload (follow upload rules in main_prompt.md)
After verification, enhance any insufficient sections before uploading.

Verify:
- Basic info: Complete?
- Relevance to core topic: Clear?
- Core content [HIGHEST PRIORITY]: Matches original and clearly communicated?
- Key data/evidence: Accurately cited?
- Remove phrasing that differs from original and uncertain content.
- Fix typos and unnatural phrasing.
```

---

## RESEARCH NOTE

### STEP 1 — Claude: Draft

```
File: @{filename}
Task: Write research note draft and save to src/research_workspace/{major_topic}/{sub_topic}/{paper_title}.md

[Abstract] — Reader must grasp the core within 3 minutes.
- Research purpose: what the study aimed to find (1–2 lines)
- Key findings: most important results (2–3 lines)
- Implications: significance for the field (1–2 lines)

[Detailed breakdown]
1. Introduction: research background, problem statement, necessity
2. Methodology [MOST IMPORTANT]: research method, experimental design, data collection — step by step. Explain technical terms in plain language.
3. Results [MOST IMPORTANT]: key experimental results, figures, core data
4. Conclusion: final conclusion, limitations, suggested future work
5. Additional insights [optional]: particularly noteworthy original perspectives

Rules:
- Base content strictly on the paper. No arbitrary interpretation or speculation.
- Use clear hierarchy for easy Notion toggle conversion.
- Include in-paper citations when present.
- Self-review that abstract and detailed breakdown are consistent before saving.
- Write in Korean. Technical terms and proper nouns (e.g. RAG, LLM) remain in their original form.
```

### STEP 2 — Gemini: Enhance

```
File: @{paper_title}.md

Abstract review:
- Is purpose/findings/implications each clearly communicated?
- Does abstract match detailed breakdown? Fix immediately if not.

Detailed breakdown review:
1. Introduction: Is background and necessity clear?
2. Methodology [HIGHEST PRIORITY]: Is step-by-step explanation clear? Are technical terms unexplained?
3. Results [HIGHEST PRIORITY]: Are figures and data accurately cited? Is interpretation different from original?
4. Conclusion: Are limitations and future directions included?
5. Additional insights (if present): Accurate based on original?

Rules:
- Fix content that differs from the original. Remove uncertain content.
- Highlight key figures and conclusions with `> ` or `!> `.
- Save after review.
```

### STEP 3 — Claude: Verify & Enhance + Notion Upload

```
File: @{paper_title}.md
Task: Final verification then Notion upload (follow upload rules in main_prompt.md)
After verification, enhance any insufficient sections before uploading.

Verify:
- Abstract: Is purpose/findings/implications clear and consistent with detailed breakdown?
- Methodology [HIGHEST PRIORITY]: Is step-by-step explanation clear with technical terms explained?
- Results [HIGHEST PRIORITY]: Are figures and data accurately cited?
- Conclusion: Are limitations and future directions included?
- Remove interpretations differing from original, exaggerations, and uncertain content.
- Fix typos and unnatural phrasing.
```
