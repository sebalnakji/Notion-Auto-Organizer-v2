# TROUBLESHOOTING SOP

1. **SEARCH**: Check `## ISSUE INDEX` to see if the problem exists.
2. **MATCH**: Read linked file → Apply solution → Update existing doc/index if needed.
3. **NO MATCH**: Resolve issue → Create `docs/troubleshooting/TS-[ID]_[keyword].md` using EXACTLY the `## FILE TEMPLATE` format → Prepend to `## ISSUE INDEX` (strict YAML format).

## FILE TEMPLATE

# TS-[ID]: [Brief Title]

- **Symptom**: [Description]
- **Cause**: [Reason]
- **Attempted**: [Status: Failed/Success] [Action] → [Result]
- **Resolution**: [Fix/Code/Config changes]
- **Notes**: [Context/Next steps]

## ISSUE INDEX

# Prepend new issues directly below this line (strict YAML).

- id: TS-003
  status: RESOLVED
  tags: [POWERSHELL, ENCODING, PIPELINE]
  summary: "PowerShell Out-File corrupted UTF-8; bypassed via Python I/O."
  path: "docs/troubleshooting/TS-003_powershell_encoding_truncation.md"

- id: TS-002
  status: RESOLVED
  tags: [CLAUDE_CLI, PROMPT_ENGINEERING, PIPELINE]
  summary: "Claude CLI output conversational text instead of Markdown; resolved via strict prompt constraints."
  path: "docs/troubleshooting/TS-002_claude_cli_conversational_output.md"

- id: TS-001
  status: RESOLVED
  tags: [CLAUDE_CLI, MCP, NOTION, INTERACTIVE_MODE]
  summary: "Notion upload failed in non-interactive pipeline due to TTY constraints; resolved by manual interactive execution."
  path: "docs/troubleshooting/TS-001_claude_cli_notion_upload_interactive_mode.md"

- id: TS-000
  status: RESOLVED
  tags: [CATEGORY]
  summary: "Concise 1-sentence summary of the issue and fix."
  path: "docs/troubleshooting/TS-000_example_issue.md"
