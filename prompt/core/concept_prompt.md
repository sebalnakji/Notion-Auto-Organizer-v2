# CONCEPT PROMPT

**Goal**: In-depth reference note for working developers.

## TONE & MANNER ROUTING

Adjust the tone based on the user's provided tag:

**[story] (Engaging Narrative Mode)**

- **Goal**: Engaging, story-driven blog post style.
- **Tone**: Polite, friendly, and approachable Korean ("~했습니다", "~합시다").
- **Style**: Connect 'Why' and 'How' seamlessly so it reads like a compelling narrative. Explain complex theories kindly.

**[info] (Fast Information Mode)**

- **Goal**: Intuitive, wiki-style quick reference.
- **Tone**: Objective, concise, and direct Korean ("~함", "~임").
- **Style**: Dry, fact-driven bullet points. Focus purely on step-by-step logic, architecture, and definitions. No filler words or extended analogies.

---

## STRUCTURE (Why → Where → What → How)

- **Why**: Problem origin & technical background.
- **Where**: 2-3 real-world use cases.
- **What [CORE]**: Precise definition & internal mechanics.
- **How [CORE]**: Step-by-step mechanics + practical example/code.
- **Pitfall [Optional]**: Real production mistakes.
- **Tips [Optional]**: Practical know-how (performance, patterns).
- **Reference [Optional]**: Official docs/RFCs/blogs.

---

## STEP 1 — Claude: Draft

- **Task**: Draft `src/concept_workspace/{major_topic}/{sub_topic}/{concept}.md` for `{topic}`.
- Follow STRUCTURE strictly. Allocate most effort to **What/How**.
- Verified facts only. No unconfirmed claims.
- Write in Korean (preserve technical terms in English like RAG, LLM).
- **CRITICAL**: Apply the requested Tone & Manner (`[story]` or `[info]`) precisely.
- Use clear hierarchy for Notion toggles.

## STEP 2 — Gemini: Enhance

- **Task**: Improve document quality in `@{concept}.md`.
- Refine **What/How** to production-level depth.
- Highlight key facts with `> ` or `!> ` to break visual monotony.
- Ensure unbroken flow: Why → Where → What → How.
- **CRITICAL**: Enforce the requested Tone & Manner strictly throughout the entire document. Remove any phrasing that breaks the requested style.

## STEP 3 — Claude: Verify & Enhance

- **Task**: Final fact-check of `@{concept}.md`.
- Verify technical accuracy of **What/How**.
- **CRITICAL**: Ensure the document perfectly matches the requested Tone & Manner (`[story]` or `[info]`).
- Validate references, flow, and fix typos/unnatural phrasing.
- Remove misleading sentences.
