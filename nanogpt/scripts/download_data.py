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
