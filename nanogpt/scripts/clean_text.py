import re

def clean_text(text: str) -> str:
    lines = []

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        # Remove lines that are just page numbers
        if re.fullmatch(r"\d+", line):
            continue

        # Remove common page labels like "Page 3" or "Page 3 of 12"
        if re.fullmatch(r"page\s+\d+(\s+of\s+\d+)?", line, flags=re.IGNORECASE):
            continue

        lines.append(line)

    cleaned = "\n".join(lines)
    cleaned = re.sub(r"[ \t]+", " ", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)

    return cleaned.strip()
