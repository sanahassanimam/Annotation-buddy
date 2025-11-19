import nbformat
from pathlib import Path

# Clean ONLY notebooks inside `notebooks/` folder
NOTEBOOK_DIR = Path("notebooks")

def clean_notebook(path: Path):
    print(f"Processing {path}...")
    nb = nbformat.read(path, as_version=4)

    # ---- Remove notebook-level widget metadata ----
    if "widgets" in nb.metadata:
        print("  - Removing metadata.widgets")
        del nb.metadata["widgets"]

    # ---- Remove widget metadata inside individual cells ----
    cleaned_in_cells = 0
    for cell in nb.cells:
        if "widgets" in cell.metadata:
            del cell.metadata["widgets"]
            cleaned_in_cells += 1
        if "widget_view" in cell.metadata:
            del cell.metadata["widget_view"]
            cleaned_in_cells += 1

    if cleaned_in_cells > 0:
        print(f"  - Cleaned widget metadata in {cleaned_in_cells} cells")

    nbformat.write(nb, path)
    print(f"  ✓ Saved cleaned notebook: {path}\n")

def main():
    if not NOTEBOOK_DIR.exists():
        print("ERROR: notebooks/ folder not found.")
        return

    for nb_file in NOTEBOOK_DIR.glob("*.ipynb"):
        clean_notebook(nb_file)

if __name__ == "__main__":
    main()
