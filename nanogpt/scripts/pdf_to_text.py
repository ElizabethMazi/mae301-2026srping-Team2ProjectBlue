from pathlib import Path
import sys
import pdfplumber

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.append(str(SCRIPT_DIR))

from clean_text import clean_text

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"


def extract_text_from_pdf(pdf_path: Path) -> str:
    pages = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text() or ""
            if page_text.strip():
                pages.append(page_text)

    return "\n\n".join(pages)


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted(RAW_DIR.glob("*.pdf"))
    if not pdf_files:
        print("No PDF files found in data/raw/")
        return

    for pdf_path in pdf_files:
        try:
            raw_text = extract_text_from_pdf(pdf_path)
            cleaned = clean_text(raw_text)

            output_path = PROCESSED_DIR / f"{pdf_path.stem}.txt"
            output_path.write_text(cleaned, encoding="utf-8")

            print(f"Created: {output_path.name}")
        except Exception as exc:
            print(f"Failed to process {pdf_path.name}")
            print(f"Reason: {exc}\n")


if __name__ == "__main__":
    main()
