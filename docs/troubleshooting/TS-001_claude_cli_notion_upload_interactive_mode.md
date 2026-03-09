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

## 4. Final Resolution: Manual execution in TTY

The fully automated pipeline was abandoned for this specific step. The upload was executed by manually opening the `claude` interactive REPL, pasting the `claude_prompt_step4.txt` contents, and physically navigating the security approval prompts using the keyboard. The file was successfully uploaded to Notion at `https://www.notion.so/31b3ce39f89c818b8113fdd65b3c4d2f`.

## 5. Notes: Next steps for automation

For future automated workflows, Claude CLI (Claude Code) is a bottleneck for Notion MCP uploads due to its strict interactive UI requirements.

- **Next Step 1:** Explore using the Notion API directly via Python script or Node.js instead of relying on Claude CLI for the final upload.
- **Next Step 2:** Look into running a headless MCP client that can execute standard tool calls asynchronously without Ink UI prompts.
