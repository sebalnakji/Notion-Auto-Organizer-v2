# CONCEPT PROMPT

## GOAL

Explain the concept clearly, quickly, and accurately — as a teacher explaining to a student with zero prior knowledge.

---

## STRUCTURE

Required: Why → Where → What → How
Optional: Pitfall, So What (only when misconceptions are common or further guidance is needed)

- Why: Background and the problem this concept was created to solve
- Where: 2–3 real-world use cases
- What: Definition + real-life analogy (core; add more analogies if insufficient)
- How: Step-by-step mechanics + practical example (core)
- Pitfall: 2–3 common mistakes beginners make
- So What: Next concepts to explore

What and How are the most critical sections. If either is unclear, the entire document fails.

---

## STEP 1 — Claude: Draft

```
Topic: {topic}
Task: Write a concept note draft and save to src/concept_workspace/{major_topic}/{sub_topic}/{concept}.md

Follow the STRUCTURE in order.
- Allocate the most effort to What and How.
- How must include a practical example (code / scenario / diagram — choose the most appropriate).
- Include Pitfall and So What only when necessary.

Rules:
- Include only verified facts. Exclude uncertain content.
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
1. Why: Is the historical/technical background sufficient? Add if lacking.
2. Where: Are examples specific and varied? Strengthen them.
3. What [HIGHEST PRIORITY]: Is the analogy intuitive? Are technical terms used without explanation? Replace or add if insufficient.
4. How [HIGHEST PRIORITY]: Is the step-by-step explanation clear? Is there a practical example? Add if missing.
5. Pitfall (if present): Remove unverified content.
6. So What (if present): Add reference links.

Rules:
- Remove uncertain content.
- Rearrange to ensure Why → Where → What → How flow is unbroken.
- Highlight important information with `> ` or `!> `.
- Remove unnecessary filler words. Keep it concise.
- Save after review.
```

---

## STEP 3 — Claude: Verify & Enhance + Notion Upload

```
File: @{concept}.md
Task: Final verification then Notion upload (follow upload rules in main_prompt.md)
After verification, enhance any insufficient sections before uploading.

Verify:
- Why/Where: Does the flow connect naturally?
- What [HIGHEST PRIORITY]: Is the analogy clear enough for a complete beginner?
- How [HIGHEST PRIORITY]: Is the step-by-step explanation specific with a practical example?
- Pitfall/So What (if present): Is the content accurate and valid?
- Remove misleading sentences, unverifiable claims, and invalid links.
- Fix typos and unnatural phrasing.
```
