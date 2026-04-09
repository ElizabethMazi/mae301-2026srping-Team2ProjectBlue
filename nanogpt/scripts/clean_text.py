from PyPDF2 import PdfReader
import re

# Load PDF file #
reader = PdfReader("C:/Users/Vicde/OneDrive - Arizona State University/Code/Project Blue AI/Data/FY-2025-2029-TIP-Open-House-Presentation.pdf")
text = ""

# Extract text from PDF #
for page in reader.pages:
    page_text = page.extract_text()
    if page_text:                    # only add if not None
        text += page_text + "\n"

# ------------------- Clean the text ----------------- #
# Remove table of contents
text = re.sub(r'TABLE OF CONTENTS.*?APPENDIX 5.*?\n', '', text, flags=re.DOTALL)

match = re.search(r'What is PAG', text)

if match:
    text = text[match.start():]

# Remove repeated headers
text = re.sub(r'CONNECT \| MOVE \| THRIVE', '', text)
text = re.sub(r'2045 Regional Mobility and Accessibility Plan Update\s+[ivx]+', '', text)

# Remove "page left blank"
text = re.sub(r'This Page Left Blank', '', text, flags=re.IGNORECASE)

# Fix space before punctuation
text = re.sub(r'\s+([.,])', r'\1', text)

# Fix broken words (basic)
text = re.sub(r'(\w)-\s+(\w)', r'\1\2', text)

# Fix hyphenated line breaks (most important)
text = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)   # line break hyphen
text = re.sub(r'(\w)\s*-\s*(\w)', r'\1-\2', text)   # normalize hyphen spacing

# Fix common PDF split words (VERY conservative)
COMMON_FIXES = [
    ("de veloped", "developed"),
    ("long range", "long-range"),  # optional preference
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

# Remove excessive spaces
text = re.sub(r' {2,}', ' ', text)

# Clean spacing
text = re.sub(r'\s+', ' ', text)

# Remove page numbers / stray numbers
text = re.sub(r'\n\d+\n', '\n', text)

# Remove TOC-style lines
text = re.sub(r'.+\s+\d+\s*\n', '', text)

# Specific fixes for known issues
text = text.replace("longrange", "long-range")

for wrong, correct in COMMON_FIXES:
    text = text.replace(wrong, correct)

# Normalize line breaks (always last)
text = re.sub(r'\n+', '\n', text) 
# ----------------------------- Clean the Text ---------------------------#


# Restructure text into paragraphs #
# Split text into sections
sections = re.split(r'\n[A-Z][A-Z\s]{5,}\n', text)

# Split text into paragraphs
all_paragraphs = []

for section in sections:
    paragraphs = re.split(r'\n\s*\n', section)
    for p in paragraphs:
        cleaned = p.strip()
        if len(cleaned) > 50:       # filter out junk
            all_paragraphs.append(cleaned)

# Save to file #
cleaned_text = "\n\n".join(all_paragraphs)
with open("C:/Users/Vicde/OneDrive - Arizona State University/Code/Project Blue AI/Data/FY-2025-2029-TIP-Open-House-Presentation.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("Done! Cleaned text saved.")
