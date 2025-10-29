import sys, glob, pandas as pd

def aggregate_csvs(pattern, output="final_dataset.xlsx"):
    files = glob.glob(pattern)
    if not files:
        print("⚠️ No matching files.")
        return
    df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
    df.to_excel(output, index=False)
    print(f"✅ Combined file saved: {output} ({len(df)} rows)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python aggregate_csvs.py 'exports/*_structured.csv'")
        sys.exit(1)
    pattern = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "final_dataset.xlsx"
    aggregate_csvs(pattern, out)
