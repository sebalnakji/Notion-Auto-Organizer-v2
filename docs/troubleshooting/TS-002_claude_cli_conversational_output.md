# TS-002: Claude CLI (Claude Code) Outputting Conversational Text Instead of Raw Markdown

## 1. Symptom: Workflow Pipe Breakage

During Step 1 and Step 3 of the AI-to-AI workflow, the `claude` CLI was used to generate Markdown content and pipe it into a file. However, instead of outputting only the requested Markdown, Claude Code autonomously generated conversational filler (e.g., "I will generate the documentation now...", "Here is the file review..."), which corrupted the final `.md` file structure.

## 2. Root Cause: Autonomous Agent Behavior

Claude Code (v2.1.70) operates as an autonomous agent by default. When given a prompt, it attempts to engage in a conversational tone and self-explain its actions rather than acting as a strict text-transformation pipeline tool (like `cat` or `sed`). The initial prompts did not have strict enough constraints to force a raw `stdout` format.

## 3. Attempted Solutions:

- [Failed] Basic prompt instruction: "Generate Markdown" -> Claude still included conversational prefaces.
- [Success] Advanced Prompt Engineering: Added explicit, strict constraints to the `concept_prompt.md` instructions: "OUTPUT ONLY RAW MARKDOWN", "DO NOT include conversational text", "DO NOT try to save the file yourself".

## 4. Final Resolution: Prompt Refinement & Python Scripting

The issue was resolved by heavily restricting Claude Code's behavior within the prompt itself. Furthermore, to avoid relying entirely on unpredictable stdout piping, the workflow was adjusted to use a Python script (`generate_prompt.py`) to safely assemble the context and instructions, ensuring the prompt passed to Claude explicitly demanded raw output.

## 5. Notes:

When using an Agentic CLI tool like `claude` in automated pipelines, prompts must be designed defensively to suppress its natural conversational instincts.
