# CONCEPT PROMPT

## GOAL

Write a precise, in-depth concept reference note for working developers to solidify their understanding.
Assume the reader has basic programming experience but may lack deep knowledge of the specific topic.

---

## STRUCTURE

Required: Why → Where → What → How
Optional: Pitfall, Tips, Reference (include when relevant)

- Why: Technical background and the problem this concept was created to solve
- Where: 2–3 real-world scenarios explaining why this concept is needed in each context
- What: Precise technical definition + internal mechanism. Analogy only as a supplementary aid (core)
- How: Step-by-step mechanics + practical example based on real-world scenarios (core)
- Pitfall: 2–3 mistakes or misconceptions commonly encountered in production
- Tips: Practical know-how not easily found in official docs — performance/design tips, idiomatic patterns, useful conventions
- Reference: Official docs, RFCs, notable technical blogs, or related specifications

What and How are the most critical sections. If either is unclear, the entire document fails.

---

## STEP 1 — Claude: Draft

```
Topic: {topic}
Task: Write a concept note draft and save to src/concept_workspace/{major_topic}/{sub_topic}/{concept}.md

Follow the STRUCTURE in order.
- Allocate the most effort to What and How.
- What: Focus on precise definition and internal mechanism. Use analogy only as a supplement.
- How must include a practical example (code / scenario / diagram — choose the most appropriate for working developers).
- Include Pitfall, Tips, Reference only when relevant content exists.

Rules:
- Include only verified facts. Exclude uncertain content.
- Write at a level appropriate for working developers, not beginners.
- Use clear hierarchy for easy Notion toggle conversion.
- Include official docs or reliable links when available.
- Self-review story flow and facts before saving.
- Write in Korean. Technical terms and proper nouns (e.g. RAG, LLM) remain in their original form.
```

---

## STEP 2 — Gemini: Enhance

```
File: @{concept}.md
Task: Improve document quality while maintaining story flow.

Review in order:
1. Why: Is the technical background sufficient to explain the origin of the problem? Add depth if lacking.
2. Where: Are scenarios specific with clear context on why the concept is needed? Strengthen if vague.
3. What [HIGHEST PRIORITY]: Is the technical definition precise? Is the internal mechanism explained clearly? Remove oversimplified analogies that add no value.
4. How [HIGHEST PRIORITY]: Is the step-by-step explanation production-level? Is the practical example realistic? Improve if too basic.
5. Pitfall (if present): Are these real production issues, not beginner mistakes? Remove unverified content.
6. Tips (if present): Is this genuinely useful practical know-how? Remove anything obvious or easily found in docs.
7. Reference (if present): Are links valid and authoritative? Add official docs if missing.

Rules:
- Remove uncertain content.
- Rearrange to ensure Why → Where → What → How flow is unbroken.
- Highlight important information with `> ` or `!> `.
- Remove unnecessary filler words. Keep it concise.
- Save after review.
```

---

## STEP 3 — Claude: Verify & Enhance

```
File: @{concept}.md
Task: Final verification and enhancement of any insufficient sections.

Verify:
- Why/Where: Does the flow connect naturally with sufficient technical context?
- What [HIGHEST PRIORITY]: Is the definition precise and the mechanism clearly explained?
- How [HIGHEST PRIORITY]: Is the step-by-step explanation specific with a production-level practical example?
- Pitfall/Tips/Reference (if present): Is the content accurate, useful, and valid?
- Remove misleading sentences, unverifiable claims, and invalid links.
- Fix typos and unnatural phrasing.
```
