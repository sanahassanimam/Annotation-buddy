import sys, fitz  # PyMuPDF

def pdf_to_txt(pdf_path, txt_path):
    doc = fitz.open(pdf_path)
    with open(txt_path, "w", encoding="utf-8") as out:
        for page in doc:
            text = page.get_text("text")
            out.write(text.strip() + "\n\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pdf_to_txt.py input.pdf output.txt")
        sys.exit(1)
    pdf_to_txt(sys.argv[1], sys.argv[2])
