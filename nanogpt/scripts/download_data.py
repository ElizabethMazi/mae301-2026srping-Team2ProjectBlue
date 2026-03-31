from pathlib import Path
from urllib.parse import urlparse, unquote
import re
import requests

ROOT = Path(__file__).resolve().parents[1]
URL_FILE = ROOT / "data" / "source_urls.txt"
RAW_DIR = ROOT / "data" / "raw"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ProjectBlueDataCollector/1.0)"
}


def load_urls() -> list[str]:
    if not URL_FILE.exists():
        raise FileNotFoundError(f"Missing file: {URL_FILE}")

    urls = []
    for line in URL_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        urls.append(line)

    return urls


def safe_filename(url: str, index: int) -> str:
    parsed = urlparse(url)
    raw_name = unquote(Path(parsed.path).name)

    if not raw_name:
        raw_name = f"document_{index}.pdf"

    if not raw_name.lower().endswith(".pdf"):
        raw_name += ".pdf"

    raw_name = re.sub(r"[^A-Za-z0-9._-]+", "_", raw_name)
    return f"{index:03d}_{raw_name}"


def download_pdf(url: str, index: int) -> None:
    response = requests.get(url, headers=HEADERS, timeout=60, stream=True)
    response.raise_for_status()

    content_type = response.headers.get("content-type", "").lower()
    looks_like_pdf = "pdf" in content_type or url.lower().split("?")[0].endswith(".pdf")

    if not looks_like_pdf:
        raise ValueError(f"URL does not appear to be a direct PDF link: {url}")

    filename = safe_filename(url, index)
    output_path = RAW_DIR / filename

    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"Downloaded: {output_path.name}")


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    urls = load_urls()
    if not urls:
        print("No URLs found in data/source_urls.txt")
        return

    for i, url in enumerate(urls, start=1):
        try:
            download_pdf(url, i)
        except Exception as exc:
            print(f"Failed: {url}")
            print(f"Reason: {exc}\n")


if __name__ == "__main__":
    main()
