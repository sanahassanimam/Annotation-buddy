# 🧠 Annotation Buddy — PDF to Structured Data Workflow

A complete, reproducible workflow for converting **PDF research papers** into **structured CSV/Excel metadata** using **Label Studio** and **Python**.

---

## ⚙️ Installation

Clone the repository and set up a virtual environment.

```bash
git clone https://github.com/sanahassanimam/Annotation-buddy.git
cd Annotation-buddy
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
🚀 Usage
Step 1 — Convert PDF → TXT
Convert your input paper into a plain text file.

bash
Copy code
python pdf_to_txt.py input_paper.pdf output_paper.txt
Step 2 — Annotate in Label Studio
Open Label Studio

Create a new project

Paste the XML schema from:

bash
Copy code
label_definitions/label_schema.xml
Import your converted text file:

Copy code
output_paper.txt
Annotate the relevant spans (e.g., SPM12, 6 mm FWHM, AAL atlas)

Export annotations as JSON:

pgsql
Copy code
project-annotations.json
Step 3 — Convert JSON → Excel / CSV
Use the Python script to convert Label Studio’s exported JSON into a structured Excel or CSV file.

bash
Copy code
python labelstudio_json_to_csv_transposed_simple.py project-annotations.json
✅ Output files

project-annotations_structured.csv — one row per annotation

project-annotations_transposed.xlsx — one row per paper

Step 4 — (Optional) Aggregate Multiple CSVs
If you have multiple CSV files from different projects, you can combine them into a single dataset.

bash
Copy code
python aggregate_csvs.py "exports/*_structured.csv" final_dataset.xlsx
🧾 Example Output
paper_id	Software	Parameters	Atlas definition	ROI definition
1	SPM12	6 mm FWHM	AAL atlas	PCC, mPFC
2	FSL FEAT	8 mm FWHM	Schaefer-400	DMN ROIs

🧱 Folder Structure
bash
Copy code
Annotation-buddy/
├── pdf_to_txt.py
├── labelstudio_json_to_csv_transposed_simple.py
├── aggregate_csvs.py
├── requirements.txt
├── .gitignore
├── LICENSE
├── label_definitions/
│   └── label_schema.xml
└── README.md
🧩 Requirements
Install dependencies listed in requirements.txt.
Main libraries used:

text
Copy code
pymupdf
pandas
openpyxl
pdfminer.six
👩‍💻 Author
Sana Hassan Imam
Postdoctoral Researcher, Carl von Ossietzky University of Oldenburg
PhD in Machine Learning & AI — University of Bremen

Project: Automating Meta-Analysis of fMRI Preprocessing Pipelines Using LLMs

📧 sanahassanimam@gmail.com

📜 License
Distributed under the MIT License.
See LICENSE for details.

✅ Summary
Task	File/Place	Purpose
Write workflow, usage, and commands	README.md	Main documentation (shown on repo page)
Specify ignored files	.gitignore	Avoid pushing temp/data files
Define license terms	LICENSE	Explains how others can reuse your code