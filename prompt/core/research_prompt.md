# RESEARCH PROMPT

**Goal**: Engaging, story-driven research documentation OR fast scannable notes. Make complex papers accessible.

## TONE & MANNER ROUTING

Adjust the tone based on the user's provided tag:

**[story] (Engaging Narrative Mode)**

- **Goal**: Story-driven research documentation.
- **Tone**: Polite, friendly Korean. Translate complex academic jargon into plain, easy-to-understand developer language.
- **Style**: Narrative flow. Tell the story of _why_ the researchers did this, _how_ they proved it, and _what_ it means for us.

**[info] (Fast Information Mode)**

- **Goal**: Highly scannable, data-dense abstract/wiki.
- **Tone**: Objective, precise, and direct Korean ("~함", "~임", "~증명").
- **Style**: Focus purely on core findings, methodology facts, and hard numbers. Use bullet points heavily. Strip out all narrative context and non-essential background.

---

## LITERATURE REVIEW

### Flow

```text
Abstract → 1st review → user YES/NO
  YES → Read full paper → final review → user YES/NO
    YES → Write draft
```

### STEP 1 — Claude: Check & Draft

- **Task**: For `{filename}` on `{core_topic}`.
- **[A. 1st Review]**: Read abstract. Output Title, Abstract summary (1 line), Relevance (high/med/low + reason), Recommendation. Wait for user YES/NO.
- **[B. Final Review]**: Read full paper. Output Core argument, Differs from abstract? (yes/no), Final relevance, Recommendation. Wait for user YES/NO.
- **[C. Write Draft]**: Save to `src/research_workspace/{major}/{sub}/{title}.md`.
  - Basic info / Relevance to topic (2-3 sentences).
  - **Core content [CORE]**: Argument, evidence, conclusion.
  - **Key data/evidence**: Figures/experimental results.
  - **Application**: How to use this.
- Write in Korean (preserve English tech terms). Verified facts only.
- **CRITICAL**: Apply the requested Tone & Manner (`[story]` or `[info]`) precisely.

### STEP 2 — Gemini: Enhance

- **Task**: Improve flow and academic depth in `@{title}.md`.
- Refine **[CORE]** sections: Make the argument/evidence compelling or highly scannable based on the tag.
- Ensure figures/data are accurate.
- Highlight key findings with `> ` or `!> ` to break visual monotony.
- NO HALLUCINATION. Do not invent methodology steps or data.
- **CRITICAL**: Enforce the requested Tone & Manner strictly throughout the entire document.

### STEP 3 — Claude: Verify & Enhance

- **Task**: Final fact-check of `@{title}.md`.
- Verify accuracy of **[CORE]** sections against original.
- **CRITICAL**: Ensure the document perfectly matches the requested Tone & Manner (`[story]` or `[info]`).
- Remove misleading interpretations, hallucinations, and typos.

---

## RESEARCH NOTE

### STEP 1 — Claude: Draft

- **Task**: Draft `src/research_workspace/{major}/{sub}/{title}.md` for `@{filename}`.
- **[Abstract]**: Purpose (1-2 lines), Key findings (2-3 lines), Implications (1-2 lines). Graspable in 3 mins.
- **[Detailed breakdown]**:
  - Introduction: Background & necessity.
  - **Methodology [CORE]**: Experimental design step-by-step.
  - **Results [CORE]**: Key figures/core data.
  - Conclusion: Limitations & future work.
  - Insights [Optional].
- Base strictly on paper. Write in Korean.
- **CRITICAL**: Apply the requested Tone & Manner (`[story]` or `[info]`) precisely.

### STEP 2 — Gemini: Enhance

- **Task**: Improve readability of `@{title}.md`.
- Ensure Abstract matches Detailed breakdown perfectly.
- Refine **[CORE]** sections.
- Highlight key conclusions with `> ` or `!> `.
- DO NOT invent methodology or skew original interpretation.
- **CRITICAL**: Enforce the requested Tone & Manner strictly throughout the entire document.

### STEP 3 — Claude: Verify & Enhance

- **Task**: Final polish of `@{title}.md`.
- Verify **[CORE]** sections are accurately cited and perfectly clear.
- **CRITICAL**: Ensure the document perfectly matches the requested Tone & Manner (`[story]` or `[info]`).
- Remove exaggerations or inaccuracies.
