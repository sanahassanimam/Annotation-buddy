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
```

---

## 🚀 Usage

### **Step 1 — Convert PDFs → JSON (Batch or Single File)

You can now convert PDF research papers into JSON files that Label Studio/Human Signals accepts as one full text block per paper.


**Convert a single PDF → JSON**

If you want to convert a single paper manually, you can still use:

```bash
python pdf_to_json.py input_paper.pdf output_paper.json
```

**Convert a folder of PDFs → JSON**

Example usage:

```bash
python pdf_to_json_batch.py input_folder/ json_files/
```
All converted .json files will be saved in json_files/ (automatically created if missing).

✅ **Explanation:**
- `input_folder/` → the folder containing your PDF papers  
- `json_files/` → new folder where all converted `.json` files will be saved  
- The script automatically processes each PDF and saves a matching `.json` version.

Example result:
```
papers/
├── Paper1.pdf
├── Paper2.pdf
└── Paper3.pdf

json_files/
├── Paper1.json
├── Paper2.json
└── Paper3.json
```

Each JSON file will look like:


```bash
{
  "text": "Full PDF text extracted here..."
}
```
The json file is perfect for importing in HumanSignal/Label Studio.
---

### **Step 2 — Annotate in Label Studio**

1. Open [Label Studio](https://labelstud.io/)
# Install the package
# into python virtual environment
pip install -U label-studio
# Launch it!
label-studio

If you see error you can try this: 

```bash
.venv\Scripts\activate
pip install --upgrade pip setuptools wheel
pip install label-studio --prefer-binary
```


Then open your browser at:
👉 http://localhost:8080


2. Create a new project  
3. Paste the XML schema from:
   ```
   label_definitions/label_schema.xml
   ```
4. Import one of your converted `.txt` files from `txt_files/`
5. Annotate relevant spans (e.g., *SPM12*, *6 mm FWHM*, *AAL atlas*)
6. Export annotations as JSON:
   ```
   project-annotations.json
   ```

---

### **Step 3 — Convert JSON → Excel / CSV**

Use the Python script to convert Label Studio’s exported JSON into a structured Excel or CSV file.

```bash
python labelstudio_json_to_csv_transposed_simple.py project-annotations.json
```

✅ **Output files**
- `project-annotations_structured.csv` — one row per annotation  
- `project-annotations_transposed.xlsx` — one row per paper

---

### **Step 4 — (Optional) Aggregate Multiple CSVs**

If you have multiple CSV files from different projects, you can combine them into a single dataset.

```bash
python aggregate_csvs.py "exports/*_structured.csv" final_dataset.xlsx
```

---

## 🧾 Example Output

| paper_id | Software | Parameters | Atlas definition | ROI definition |
|-----------|-----------|-------------|------------------|----------------|
| 1 | SPM12 | 6 mm FWHM | AAL atlas | PCC, mPFC |
| 2 | FSL FEAT | 8 mm FWHM | Schaefer-400 | DMN ROIs |

---

## 🧱 Folder Structure

```bash
Annotation-buddy/
├── pdf_to_txt.py
├── pdf_to_txt_batch.py
├── labelstudio_json_to_csv_transposed_simple.py
├── aggregate_csvs.py
├── requirements.txt
├── .gitignore
├── LICENSE
├── label_definitions/
│   └── label_schema.xml
└── README.md
```

---

## 🧩 Requirements

Install dependencies listed in `requirements.txt`.  
Main libraries used:

```text
pymupdf
pandas
openpyxl
pdfminer.six
```

---

## 👩‍💻 Author

**Sana Hassan Imam**  
Postdoctoral Researcher, Carl von Ossietzky University of Oldenburg  
PhD in Machine Learning & AI — University of Bremen  

Project: *Automating Meta-Analysis of fMRI Preprocessing Pipelines Using LLMs*

📧 [sanahassanimam@gmail.com](mailto:sanahassanimam@gmail.com)

---

## 📜 License

Distributed under the **MIT License**.  
See [`LICENSE`](LICENSE) for details.

---

## ✅ Summary

| Task | File/Place | Purpose |
|------|-------------|----------|
| Convert PDFs → TXTs | `pdf_to_txt_batch.py` | Batch conversion of papers to text |
| Write workflow, usage, and commands | `README.md` | Main documentation (shown on repo page) |
| Specify ignored files | `.gitignore` | Avoid pushing temp/data files |
| Define license terms | `LICENSE` | Explains how others can reuse your code |
