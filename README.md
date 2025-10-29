<<<<<<< HEAD
# Annotation-buddy
Automizing the meta-analysis by annotating the papers
=======
# 🧠 Annotation Buddy Workflow

A reproducible workflow for converting scientific **PDF papers** into **structured Excel/CSV data** using **Label Studio** and **Python**.

---

## 📋 Overview

This repository automates the complete process:

| Step | Tool | Input | Output |
|------|------|--------|--------|
| 1 | PyMuPDF / pdfminer | `.pdf` | `.txt` |
| 2 | Label Studio | `.txt` | Annotated spans |
| 3 | Label Studio Export | `.json` | Annotation file |
| 4 | Python (script) | `.json` | Structured `.csv` / `.xlsx` |
| 5 | Python (optional) | Multiple CSVs | Final aggregated dataset |

---

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/fMRI-Meta-Annotation.git
cd fMRI-Meta-Annotation
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt

🚀 Usage
Step 1 — Convert PDF → TXT
python pdf_to_txt.py input_paper.pdf output_paper.txt

Step 2 — Annotate in Label Studio


Open Label Studio


Create a new project


Paste the XML schema from label_definitions/label_schema.xml


Import output_paper.txt


Annotate spans (e.g., “SPM12”, “6 mm FWHM”, “AAL atlas”)


Export as JSON (e.g., project-annotations.json)


Step 3 — Convert JSON → Excel / CSV
python labelstudio_json_to_csv_transposed_simple.py project-annotations.json

✅ Output:


project-annotations_structured.csv (one row per annotation)


project-annotations_transposed.xlsx (one row per paper)


Step 4 — (Optional) Aggregate multiple CSVs
python aggregate_csvs.py "exports/*_structured.csv" final_dataset.xlsx


🧾 Example Output
paper_idSoftwareParametersAtlas definitionROI definition1SPM126 mm FWHMAAL atlasPCC, mPFC2FSL FEAT8 mm FWHMSchaefer-400DMN ROIs

🧱 Folder Structure
fMRI-Meta-Annotation/
├── pdf_to_txt.py
├── labelstudio_json_to_csv_transposed_simple.py
├── aggregate_csvs.py
├── requirements.txt
├── .gitignore
├── LICENSE
├── label_definitions/
│   └── label_schema.xml
└── README.md


👩‍💻 Author
Sana Hassan Imam
Postdoctoral Researcher, Carl von Ossietzky University of Oldenburg
PhD in Machine Learning & AI — University of Bremen
Project: Automating Meta-Analysis of fMRI Preprocessing Pipelines Using LLMs

📜 License
Distributed under the MIT License.
See LICENSE for details.

---

## ✅ Summary

| Task | File/Place | Why |
|------|-------------|-----|
| Write workflow, usage, and commands | `README.md` | Main documentation (shown on repo page) |
| Specify ignored files | `.gitignore` | Avoid pushing temp/data files |
| Choose license | `LICENSE` | Defines how others can reuse your code |

---

Would you like me to **generate a ready-to-paste README.md** customized with your full name, affiliation, and GitHub link (so you can upload it right away)?
>>>>>>> 12c6b65 (Initial commit: complete annotation workflow)
