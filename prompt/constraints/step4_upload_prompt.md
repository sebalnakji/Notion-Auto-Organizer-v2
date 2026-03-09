# TASK: STEP 4 - NOTION UPLOAD

## INSTRUCTIONS

Upload the attached Markdown draft to Notion.

1. **Format Conversion**:
   - **Overarching Summary**: The very first block of the page MUST be a high-level summary of the entire document. This summary must NOT be placed inside a toggle.
   - **Toggle Sections**: After the overarching summary, map each section to a Notion toggle block (`<details><summary>`).
   - **Toggle Depth Limit**: Limit toggle structure to a MAXIMUM depth of 3 levels to maintain readability.
   - **Code Blocks**: Place essential code blocks outside of deep toggles to improve visibility.
   - **Images**: Insert relevant images using `![description](URL)` format.
   - **Highlights**: Apply Notion color highlights to key terms.

2. **Upload**:
   - **CRITICAL**: If the user provided an exact Target Notion Page ID, you MUST NOT use `notion-search` to find the parent page. Use the exact provided ID directly with `notion-create-page` or the relevant MCP tools to completely bypass semantic search bottlenecks.
   - If no ID was provided, use the Notion MCP tools to search for the designated parent page (e.g., Notion database Sub Tag).
   - Create a new page with the formatted content under that parent page.
   - Confirm toggle structure, images, links, and colors render correctly.
