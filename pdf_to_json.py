import sys, json, fitz  # PyMuPDF

def pdf_to_json(pdf_path, json_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        text = page.get_text("text")
        full_text += text.strip() + "\n\n"

    # Wrap in a JSON object suitable for HumanSignal
    data = {"text": full_text}

    with open(json_path, "w", encoding="utf-8") as out:
        json.dump(data, out, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pdf_to_json.py input.pdf output.json")
        sys.exit(1)

    pdf_to_json(sys.argv[1], sys.argv[2])
