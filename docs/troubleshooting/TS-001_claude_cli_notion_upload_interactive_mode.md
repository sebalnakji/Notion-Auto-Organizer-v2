# TS-001: Claude CLI (Claude Code) Interactive Mode Limitation with Notion MCP Upload

## 1. Symptom: Notion Upload pipeline step failed when using Claude CLI non-interactively.

The CI/CD or automated script pipeline (Step 4) designed to upload a generated Markdown file to Notion via Claude CLI's MCP integration consistently failed. Errors included `Raw mode is not supported on the current process.stdin` and connection closures.

## 2. Root Cause: TTY requirement and Interactive Prompts

1. **Ink Library Constraints:** Claude Code (`claude`) uses the Ink framework for its terminal UI, which explicitly requires an interactive TTY session (`process.stdin.isTTY`). Running it in a piped (`|`), redirected (`<`), or background process causes it to crash immediately with a raw mode error.
2. **Security & Workspace Trust Prompts:** Claude CLI enforces interactive confirmation prompts for trusting new directories and authorizing specific MCP commands (e.g., `notion-search`, `notion-fetch`, `notion-create-pages`). These prompts block execution when arguments like `--dangerously-skip-permissions` do not fully bypass them.

## 3. Attempted Solutions:

- [Failed] Pipe the prompt directly (`Get-Content prompt.txt | claude -p`) - Resulted in `Raw mode is not supported...` error due to non-interactive stdin.
- [Failed] Redirect stdin via `cmd.exe` (`type prompt.txt | claude`) - Resulted in the same TTY restriction error.
- [Failed] Pass prompt as direct CLI argument (`claude "Read prompt..."`) - Blocked by the "Trust Folder" security prompt which required arrow-key/enter interaction.
- [Failed] Direct Notion MCP API Call via AI Assistant Tool (`mcp_notion-mcp-server_API-post-search`) - Resulted in `connection closed: EOF`, likely due to an inactive or improperly configured background MCP server instance.
- [Success] Manual Interactive Execution - Ran `claude` in an interactive terminal, manually bypassed the directory trust prompt, pasted the Markdown payload instructions directly into the chat, and manually authorized ("Always Allow") each MCP action (`notion-search`, `notion-fetch`, `notion-create-pages`).

## 4. Final Resolution: Exact Target ID & Auto-Approve Permissions

The fully automated pipeline is now functional using the following two fixes:

1. **Bypass Semantic Search Bottleneck:** Requiring the exact Notion Page ID (`(ID: xxxxxxxx)`) in the Target Page setup completely skips the fragile `notion-search` step, allowing the agent to use `notion-create-page` directly under the correct parent ID.
2. **Bypass Interactive Security Prompts:** When Claude Code issues permission prompts (e.g. for Notion workspace access), the agent MUST explicitly input `2` ("Yes, and don't ask again") to automatically authorize the action and prevent the pipeline from hanging on the TTY interface.

## 5. Notes: Next steps for automation

For robust automated workflows using `claude` (Claude Code) and MCP:

- Always configure the agent to auto-approve interactive prompts.
- Avoid loose semantic searches (`notion-search`) when precise creation (`notion-create-page` with known `page_id`) is available, as searches take too long and are prone to mismatch errors.
