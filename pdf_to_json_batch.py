import sys
import os
import json
import fitz  # PyMuPDF

def pdf_to_text(pdf_path):
    """Extract full text from a single PDF file."""
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        text = page.get_text("text")
        full_text += text.strip() + "\n\n"
    return full_text.strip()


def pdf_to_json_single(pdf_path, json_path):
    """Convert a single PDF to a JSON file with key 'text'."""
    full_text = pdf_to_text(pdf_path)
    data = {"text": full_text}

    with open(json_path, "w", encoding="utf-8") as out:
        json.dump(data, out, ensure_ascii=False, indent=2)


def pdf_to_json_batch(input_folder, output_folder):
    """Convert all PDFs in input_folder to JSON files in output_folder."""
    # Normalize paths
    input_folder = os.path.abspath(input_folder)
    output_folder = os.path.abspath(output_folder)

    if not os.path.isdir(input_folder):
        print(f"Error: Input folder does not exist or is not a directory: {input_folder}")
        sys.exit(1)

    os.makedirs(output_folder, exist_ok=True)

    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print(f"No PDF files found in: {input_folder}")
        return

    print(f"Found {len(pdf_files)} PDF files. Converting to JSON...")

    for filename in pdf_files:
        pdf_path = os.path.join(input_folder, filename)
        base_name = os.path.splitext(filename)[0]
        json_filename = base_name + ".json"
        json_path = os.path.join(output_folder, json_filename)

        print(f"- Converting: {filename} -> {json_filename}")
        pdf_to_json_single(pdf_path, json_path)

    print("✅ Done. All PDFs converted to JSON.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_json_batch.py input_folder/ output_folder/json_files/")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    pdf_to_json_batch(input_folder, output_folder)
