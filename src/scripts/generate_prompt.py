import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Generate prompt by safely combining instruction and draft into UTF-8 text.")
    parser.add_argument("--instruction", required=True, help="Path to the instruction/template text file")
    parser.add_argument("--draft", help="Path to the markdown draft file to append")
    parser.add_argument("--output", required=True, help="Path to save the combined output prompt")

    args = parser.parse_args()

    # Read the instruction
    with open(args.instruction, "r", encoding="utf-8") as f:
        content = f.read()

    # Append draft if provided
    if args.draft:
        with open(args.draft, "r", encoding="utf-8") as f:
            draft_content = f.read()
        content += "\n\n--- DRAFT CONTENT BELOW ---\n\n" + draft_content

    # Ensure output directory exists (like %TEMP%)
    output_dir = os.path.dirname(os.path.abspath(args.output))
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    # Write combined prompt
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    main()
