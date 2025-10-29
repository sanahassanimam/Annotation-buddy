# 🧠 Annotation Buddy — PDF to Structured Data Workflow

A complete, reproducible workflow for converting **PDF research papers** into **structured CSV/Excel metadata** using **Label Studio** and **Python**.

---

## ⚙️ Installation

```bash
git clone https://github.com/sanahassanimam/Annotation-buddy.git
cd Annotation-buddy
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

Annotate spans (e.g., SPM12, 6 mm FWHM, AAL atlas)

Export as JSON (e.g., project-annotations.json)

Step 3 — Convert JSON → Excel / CSV
python labelstudio_json_to_csv_transposed_simple.py project-annotations.json


✅ Output files

project-annotations_structured.csv — one row per annotation

project-annotations_transposed.xlsx — one row per paper

Step 4 — (Optional) Aggregate multiple CSVs
python aggregate_csvs.py "exports/*_structured.csv" final_dataset.xlsx

🧾 Example Output
paper_id	Software	Parameters	Atlas definition	ROI definition
1	SPM12	6 mm FWHM	AAL atlas	PCC, mPFC
2	FSL FEAT	8 mm FWHM	Schaefer-400	DMN ROIs
🧱 Folder Structure
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

👩‍💻 Author

Sana Hassan Imam
Postdoctoral Researcher, Carl von Ossietzky University of Oldenburg

📜 License

Distributed under the MIT License.
See LICENSE
 for details.