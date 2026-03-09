# TS-002: Claude CLI (Claude Code) Outputting Conversational Text Instead of Raw Markdown

## 1. Symptom: Workflow Pipe Breakage

During Step 1 and Step 3 of the AI-to-AI workflow, the `claude` CLI was used to generate Markdown content and pipe it into a file. However, instead of outputting only the requested Markdown, Claude Code autonomously generated conversational filler (e.g., "I will generate the documentation now...", "Here is the file review..."), which corrupted the final `.md` file structure.

## 2. Root Cause: Autonomous Agent Behavior

Claude Code (v2.1.70) operates as an autonomous agent by default. When given a prompt, it attempts to engage in a conversational tone and self-explain its actions rather than acting as a strict text-transformation pipeline tool (like `cat` or `sed`). The initial prompts did not have strict enough constraints to force a raw `stdout` format.

## 3. Attempted Solutions:

- [Failed] Basic prompt instruction: "Generate Markdown" -> Claude still included conversational prefaces.
- [Success] Advanced Prompt Engineering: Added explicit, strict constraints to the `concept_prompt.md` instructions: "OUTPUT ONLY RAW MARKDOWN", "DO NOT include conversational text", "DO NOT try to save the file yourself".

## 4. Final Resolution: Strict Constraint Templates & generate_prompt.py

The issue was entirely resolved by separating the strict constraints from the core text and using a Python script:

1. **Strict Constraints Templates (`step1_draft_prompt.md`, `step3_verify_prompt.md`)**: Reusable templates that explicitly force Claude CLI to "OUTPUT ONLY RAW MARKDOWN" and forbid conversational filler.
2. **File Assembly via Python**: Using `src/scripts/generate_prompt.py` to safely merge the strict instruction templates with the drafting content before passing it to Claude CLI. This removes ambiguity and forces the AI into a strict data-parsing mindset.

## 5. Notes:

When using an Agentic CLI tool like `claude` in automated pipelines:

- Always apply strict behavior-modifying constraints as a "system prefix" before the main payload.
- As of V2.2, Step 3 (Verify) is marked as `[OPTIONAL]` in the workflow. If Step 2 (Gemini Enhance) was successful, Step 3 can be skipped to further reduce the risk of conversational corruption and save time.
