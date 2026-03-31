from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"
FINAL_DIR = ROOT / "data" / "final"
OUTPUT_FILE = FINAL_DIR / "project_blue_corpus.txt"


def main() -> None:
    FINAL_DIR.mkdir(parents=True, exist_ok=True)

    text_files = sorted(PROCESSED_DIR.glob("*.txt"))
    if not text_files:
        print("No text files found in data/processed/")
        return

    included_count = 0

    with OUTPUT_FILE.open("w", encoding="utf-8") as outfile:
        for text_file in text_files:
            text = text_file.read_text(encoding="utf-8").strip()

            if not text:
                print(f"Skipping empty file: {text_file.name}")
                continue

            outfile.write("<|document_start|>\n")
            outfile.write(f"source: {text_file.name}\n\n")
            outfile.write(text)
            outfile.write("\n<|document_end|>\n\n")

            included_count += 1

    print(f"Built dataset: {OUTPUT_FILE}")
    print(f"Documents included: {included_count}")


if __name__ == "__main__":
    main()
