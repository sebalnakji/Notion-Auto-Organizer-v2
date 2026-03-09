<system_instruction>
You are an AI agent for the "Antigravity" project. This file is your primary troubleshooting knowledge base and memory index. You MUST strictly follow the <sop> below.
</system_instruction>

<sop>
1. SEARCH: Check <issue_index> to see if the current problem exists.
2. IF MATCH_FOUND:
   - Read the detailed markdown file linked in the index.
   - Apply the solution.
   - UPDATE the file if you find a better solution or need to add context.
3. IF NO_MATCH:
   - Troubleshoot and resolve the issue.
   - Create a NEW file in `docs/troubleshooting/`.
   - Naming Convention: `TS-[3-digit-ID]_[snake_case_keywords].md`.
   - You MUST strictly use the <file_template> for the new file.
4. UPDATE_INDEX: Prepend the new entry to the TOP of the <issue_index> using the specified YAML format.
</sop>

<file_template>

# TS-[ID]: [Brief Title]

## 1. Symptom: [Description]

## 2. Root Cause: [Reason]

## 3. Attempted Solutions: [Status: Failed/Success] [Action] - [Result]

## 4. Final Resolution: [Code/Config changes]

## 5. Notes: [Context/Next steps]

</file_template>

<issue_index>

# INSTRUCTION: Prepend new issues directly below this line using the exact YAML format.

- id: TS-003
  status: RESOLVED
  tags: [POWERSHELL, ENCODING, PIPELINE]
  summary: "PowerShell Out-File piping corrupted Korean UTF-8 characters and truncated files; bypassed using a Python I/O script."
  file_path: "docs/troubleshooting/TS-003_powershell_encoding_truncation.md"

- id: TS-002
  status: RESOLVED
  tags: [CLAUDE_CLI, PROMPT_ENGINEERING, PIPELINE]
  summary: "Claude CLI broke pipeline by outputting conversational text instead of raw Markdown; resolved via strict prompt constraints."
  file_path: "docs/troubleshooting/TS-002_claude_cli_conversational_output.md"

- id: TS-001
  status: RESOLVED
  tags: [CLAUDE_CLI, MCP, NOTION, INTERACTIVE_MODE]
  summary: "Notion upload via Claude CLI failed in non-interactive pipeline due to Ink TTY constraints; resolved by manual interactive execution."
  file_path: "docs/troubleshooting/TS-001_claude_cli_notion_upload_interactive_mode.md"

- id: TS-000
  status: RESOLVED
  tags: [CATEGORY]
  summary: "Concise 1-sentence summary of the issue and fix."
  file_path: "docs/troubleshooting/TS-000_example_issue.md"

</issue_index>
