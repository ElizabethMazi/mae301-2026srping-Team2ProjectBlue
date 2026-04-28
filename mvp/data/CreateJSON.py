import json
import re

# ====== SETTINGS ======
INPUT_FILE = "C:/Users/Vicde/OneDrive - Arizona State University/Code/Project Blue AI/Data/Pima-County-Comprehensive-Plan.txt"
OUTPUT_FILE = "C:/Users/Vicde/OneDrive - Arizona State University/Code/Project Blue AI/Data/documents.jsonl"
SOURCE = "Pima County Comprehensive Plan"
REGION = "Pima County, AZ"
CHUNK_SIZE = 1000

# ====== TAG KEYWORDS ======
TAG_RULES = {
    # --- Core Planning ---
    "planning": ["plan", "policy", "strategy", "long-range"],
    "growth": ["population", "growth", "expansion"],
    "land_use": ["land use", "zoning", "rezoning", "density"],

    # --- Housing ---
    "housing": ["housing", "residential", "homes", "units"],
    "housing_supply": ["supply", "inventory", "vacancy", "shortage", "gap", "units"],
    "affordability": ["affordable", "affordability", "income", "ami", "cost burden"],
    "homeownership": ["homeownership", "buyer", "mortgage"],
    "rental": ["rent", "rental", "tenant", "lease"],
    "subsidies": ["subsidy", "voucher", "assistance", "grant", "rehousing"],
    "homelessness": ["homeless", "shelter", "supportive housing"],

    # --- Infrastructure ---
    "transportation": ["transportation", "road", "transit", "mobility"],
    "infrastructure": ["infrastructure", "utilities", "facilities"],
    "water": ["water", "water supply", "hydrology"],
    "energy": ["energy", "electric", "utilities"],
    
    # --- Government ---
    "governance": ["govern", "board", "council", "authority"],
    "public_input": ["public", "community", "engagement", "input"],

    # --- Economy ---
    "economic_development": ["economic", "jobs", "employment", "business"],

    # --- Environment ---
    "environment": ["air quality", "water quality", "climate", "environment"],

    # --- Services ---
    "public_services": ["health", "safety", "education", "library"],
    "parks_recreation": ["parks", "recreation", "trails"]
}

# ====== IMPACT RULES ======
def generate_impact(tags):

    if "housing_supply" in tags:
        return "May signal housing shortages or availability changes that could impact home prices."

    if "affordability" in tags or "subsidies" in tags:
        return "May impact housing affordability or provide financial assistance opportunities."

    if "land_use" in tags:
        return "May influence what types of housing or development are allowed in specific areas."

    if "transportation" in tags:
        return "May affect commute times and accessibility to jobs and services."

    if "infrastructure" in tags or "water" in tags:
        return "May affect availability of utilities and services needed for new housing development."

    if "economic_development" in tags:
        return "May influence job growth and local economic conditions affecting housing demand."

    if "environment" in tags:
        return "May impact environmental quality and long-term livability of the area."

    if "growth" in tags:
        return "May indicate increasing demand for housing and services in the area."

    return "May influence local development and planning decisions."

# ====== LOAD TEXT ======
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Remove obvious noise sections
text = re.sub(r'table of contents.*?\n', '', text, flags=re.IGNORECASE)
text = re.sub(r'exhibit\s+\d+.*?\n', '', text, flags=re.IGNORECASE)

# Split into sentences
sentences = re.split(r'(?<=[.!?]) +', text)

# ====== CHUNKING ======
chunks = []
current_chunk = ""

for sentence in sentences:
    if len(current_chunk) + len(sentence) <= CHUNK_SIZE:
        current_chunk += " " + sentence
    else:
        chunks.append(current_chunk.strip())
        current_chunk = sentence

if current_chunk:
    chunks.append(current_chunk.strip())

# ====== TAGGING FUNCTION ======
def get_tags(text):
    text_lower = text.lower()
    tag_scores = {}

    for tag, keywords in TAG_RULES.items():
        matches = sum(1 for word in keywords if re.search(rf'\b{re.escape(word)}\b', text_lower))
        if matches > 0:
            tag_scores[tag] = matches

    sorted_tags = sorted(tag_scores, key=tag_scores.get, reverse=True)
    top_tags = sorted_tags[:5]

    # Force housing tag if relevant
    if "housing" in text_lower and "housing" not in top_tags:
        top_tags.append("housing")

    if not top_tags:
        top_tags = ["planning"]

    return top_tags

# ====== WRITE TO JSONL ======
start_id = 1

try:
    with open(OUTPUT_FILE, "r") as f:
        start_id = sum(1 for _ in f) + 1
except FileNotFoundError:
    pass

with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
    for i, chunk in enumerate(chunks):

        # Skip junk chunks
        if len(chunk.strip()) < 100:
            continue
        if any(x in chunk.lower() for x in ["table of contents", "appendix", "exhibit"]):
            continue

        tags = get_tags(chunk)
        impact = generate_impact(tags)

        entry = {
            "id": f"compplan_{start_id + i:03}",
            "source": SOURCE,
            "region": REGION,
            "tags": tags,
            "content": chunk,
            "impact": impact
        }

        f.write(json.dumps(entry) + "\n")

print(f"Added {len(chunks)} chunks to {OUTPUT_FILE}")
