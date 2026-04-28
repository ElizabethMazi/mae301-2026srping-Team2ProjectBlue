print("SCRIPT STARTED")

import pdfplumber
import re

# Load PDF file #
pdf_path = "C:/Users/Vicde/OneDrive - Arizona State University/Code/Project Blue AI/Data/Pima-County-Comprehensive-Plan.pdf"
text = ""

# Pages to skip (0-based indexing)
BAD_PAGES = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 26, 33, 36, 37, 42, 49, 57, 58, 72, 73, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 158, 168, 197, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250}

# Extract text from PDF #
with pdfplumber.open(pdf_path) as pdf:
    print("Total pages:", len(pdf.pages))
    
    for i, page in enumerate(pdf.pages):

        if i in BAD_PAGES:
            print(f"Skipping problematic page {i}")
            continue

        print(f"Processing page {i}")

        try:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        except Exception as e:
            print(f"Skipped page {i} due to error: {e}")

# ------------------- Clean the text ----------------- #

# Remove table of contents
text = re.sub(r'TABLE OF CONTENTS.*?APPENDIX 5.*?\n', '', text, flags=re.DOTALL)
print("TOC removed")

match = re.search(r'What is PAG', text)
if match:
    text = text[match.start():]

# Remove repeated headers
text = re.sub(r'CONNECT \| MOVE \| THRIVE', '', text)
text = re.sub(r'2045 Regional Mobility and Accessibility Plan Update\s+[ivx]+', '', text)

# Remove "page left blank"
text = re.sub(r'This Page Left Blank', '', text, flags=re.IGNORECASE)

# Fix spacing issues
text = re.sub(r'\s+([.,])', r'\1', text)
text = re.sub(r'(\w)-\s+(\w)', r'\1\2', text)
text = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)
text = re.sub(r'(\w)\s*-\s*(\w)', r'\1-\2', text)

# Fix common PDF split words
COMMON_FIXES = [
    ("de veloped", "developed"),
    ("long range", "long-range"),
    ("per formance", "performance"),
    ("trans portation", "transportation"),
    ("wasteRTA", "waste RTA"),
    ("regionThe", "region. The"),
    ("billionThe", "billion. The"),
    ("yearsRTA", "years RTA"),
    ("oreduces", "reduces"),
    ("oimproves", "improves"),
    ("oenhances", "enhances"),
    ("LivabilityThe", "Livability. The"),
    ("DECIDEReview", "DECIDER. Review"),
    ("inputA", "input. A"),
    ("ballotPima", "ballot Pima"),
    ("PlanPAG", "Plan PAG"),
    ("aRide", "a-Ride"),
    ("TransitProject", "Transit Project"),
    ("u sed", "used"),
    ("engage ment", "engagement"),
    ("strategie s", "strategies"),
    ("m illion", "million")
]

for wrong, correct in COMMON_FIXES:
    text = text.replace(wrong, correct)

# Remove duplicate words
text = re.sub(r'\b(\w+)\s+\1\b', r'\1', text)

# Handle bullet points
text = text.replace("•", ". ")

# Clean spacing
text = re.sub(r' {2,}', ' ', text)
text = re.sub(r'\s+', ' ', text)

# Remove standalone page numbers safely
text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)

# Normalize line breaks
text = re.sub(r'\n+', '\n', text)

# ----------------------------- Restructure --------------------------- #

sections = text.split("\n\n")  # faster + safer than heavy regex

all_paragraphs = []

for section in sections:
    cleaned = section.strip()
    if len(cleaned) > 50:
        all_paragraphs.append(cleaned)

# Save to file #
output_path = "C:/Users/Vicde/OneDrive - Arizona State University/Code/Project Blue AI/Data/Pima-County-Comprehensive-Plan.txt"

cleaned_text = "\n\n".join(all_paragraphs)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("Done! Cleaned text saved.")
