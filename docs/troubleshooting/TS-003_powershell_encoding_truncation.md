# TS-003: PowerShell Encoding and File Truncation Errors During Piping

## 1. Symptom: Markdown File Corruption and Data Loss

During Step 3 (Verify & Enhance), when attempting to read the draft Markdown and pipe it to `claude`, and then pipe the output back to a file using PowerShell (`Get-Content ... | claude | Out-File ...`), the resulting file was either truncated, completely empty, or suffered from encoding corruption (broken Korean characters).

## 2. Root Cause: PowerShell Default Encoding and Stream Handling

1. **Encoding Mismatches:** PowerShell's older `Out-File` and pipe behavior defaults to UTF-16 LE or ANSI depending on the version, which breaks UTF-8 encoded Markdown containing Korean characters.
2. **File Lock/Truncation:** Attempting to read from a file and pipe the output of a process back into the _same_ file simultaneously in PowerShell can lead to race conditions where the file is truncated to 0 bytes before the pipeline finishes processing.

## 3. Attempted Solutions:

- [Failed] Setting powershell session encoding manually (`[Console]::OutputEncoding = [System.Text.Encoding]::UTF8`).
- [Failed] Using `Set-Content` instead of `Out-File`.
- [Success] Using a Python script to handle file I/O safely.

## 4. Final Resolution: Replaced PowerShell with Python Script

To ensure robust UTF-8 handling and safe file operations, a Python script (`generate_prompt.py`) was created to handle reading the draft, merging it with the prompt instructions, and saving it to a temporary file. The `claude` CLI was then invoked to read this temporary file. This completely bypassed PowerShell's unreliable string piping and encoding mechanics.

## 5. Notes:

For complex text manipulation pipelines involving Unicode (Korean), rely on cross-platform Python scripts rather than native Windows PowerShell piping.
