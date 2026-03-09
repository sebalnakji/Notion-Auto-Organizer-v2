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

## 4. Final Resolution: The `generate_prompt.py` Utility

To ensure robust UTF-8 handling and safe file operations across platforms, the workflow was refactored:

1. Created `src/scripts/generate_prompt.py`. This script accepts `--instruction`, `--draft`, and `--output` arguments to merge text safely into a temporary file.
2. The pipeline now executes:
   ```powershell
   python src\scripts\generate_prompt.py --instruction <inst> --draft <draft> --output $env:TEMP\prompt.txt
   Get-Content $env:TEMP\prompt.txt -Raw | claude -p ... | Out-File -FilePath <out> -Encoding UTF8
   ```
   By managing file concatenation internally via Python open/write paths, we bypassed PowerShell's unpredictable stream truncation and encoding corruption.

## 5. Notes:

- Do not pipe string literals formatting (e.g. `@"..."@`) directly using PowerShell arrays into `claude`.
- Always rely on `generate_prompt.py` to compile the instructions to a `.txt` file first, then use `Get-Content ... -Raw` to pass the payload into Claude.
