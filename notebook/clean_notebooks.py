import nbformat
from pathlib import Path

# Adjust this if your notebooks live somewhere else
NOTEBOOK_DIR = Path(".")

def clean_notebook(path: Path):
    print(f"Processing {path}...")
    nb = nbformat.read(path, as_version=4)

    # Remove notebook-level widgets metadata if present
    if "widgets" in nb.metadata:
        print("  - Removing metadata.widgets")
        del nb.metadata["widgets"]

    # (Optional) Also clean widget metadata from cells
    changed_cells = 0
    for cell in nb.cells:
        if "widgets" in cell.metadata:
            del cell.metadata["widgets"]
            changed_cells += 1
        if "widget_view" in cell.metadata:
            del cell.metadata["widget_view"]
            changed_cells += 1
    if changed_cells:
        print(f"  - Cleaned widget metadata from {changed_cells} cells")

    nbformat.write(nb, path)
    print(f"  ✓ Saved cleaned notebook: {path}\n")

def main():
    for nb_path in NOTEBOOK_DIR.rglob("*.ipynb"):
        clean_notebook(nb_path)

if __name__ == "__main__":
    main()
