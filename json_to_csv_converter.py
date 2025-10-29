import json
import pandas as pd
import os
import sys
from collections import OrderedDict

def convert_labelstudio_json_to_csv(json_file, output_prefix=None):
    # --- Load JSON file ---
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    rows = []
    label_order = []  # to preserve original label order

    for item in data:
        paper_id = item.get("id", None)
        text = item.get("data", {}).get("text", "")
        annotations = item.get("annotations", [])

        for ann in annotations:
            results = ann.get("result", [])
            annotator = ann.get("completed_by", "unknown")
            for r in results:
                value = r.get("value", {})
                labels = value.get("labels", [])
                if not labels:
                    continue
                label = labels[0]
                if label not in label_order:
                    label_order.append(label)  # remember first appearance order

                rows.append({
                    "paper_id": paper_id,
                    "label": label,
                    "extracted_text": value.get("text", ""),
                    "start_offset": value.get("start", ""),
                    "end_offset": value.get("end", ""),
                    "annotator": annotator,
                    "context": text[:300].replace("\n", " ")
                })

    df = pd.DataFrame(rows)
    if df.empty:
        print("⚠️ No annotations found in JSON.")
        return

    if output_prefix is None:
        output_prefix = os.path.splitext(json_file)[0]

    # ---- Long format ----
    long_csv = f"{output_prefix}_structured.csv"
    df.to_csv(long_csv, index=False, encoding='utf-8-sig')
    print(f"✅ Long-format CSV saved: {long_csv}")

    # ---- Transposed (wide) format ----
    pivot = (
        df.groupby(["paper_id", "label"])["extracted_text"]
        .apply(lambda x: "; ".join(set(x)))
        .unstack(fill_value="")
        .reset_index()
    )

    # Reorder columns according to first-seen label order
    cols = ["paper_id"] + [c for c in label_order if c in pivot.columns]
    pivot = pivot[cols]

    transposed_xlsx = f"{output_prefix}_transposed.xlsx"
    pivot.to_excel(transposed_xlsx, index=False, engine="openpyxl")
    print(f"📘 Transposed Excel saved: {transposed_xlsx}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python labelstudio_json_to_csv_transposed_simple.py project-annotations.json")
        sys.exit(1)

    json_path = sys.argv[1]
    convert_labelstudio_json_to_csv(json_path)
