import json
import re

# ====== SETTINGS ======
INPUT_FILE = "C:/Users/Vicde/OneDrive - Arizona State University/Code/Project Blue AI/Data/FY-2025-2029-TIP-Open-House-Presentation.txt"    # your cleaned text file
OUTPUT_FILE = "C:/Users/Vicde/OneDrive - Arizona State University/Code/Project Blue AI/Data/JSON.jsonl"                  # your JSONL file
SOURCE = "Transportation Open House"
REGION = "Pima County, AZ"
CHUNK_SIZE = 1000

# ====== TAG KEYWORDS ======
TAG_RULES = {
    "transportation": ["transportation", "road", "transit", "mobility", "infrastructure"],
    "growth": ["population", "growth", "development", "expansion"],
    "funding": ["funding", "revenue", "budget", "investment"],
    "planning": ["plan", "policy", "strategy", "long-range"],
    
    "governance": ["govern", "board", "council", "authority"],
    "organization": ["association", "agency", "organization"],
    "taxes": ["tax", "excise", "sales tax"],
    "public_input": ["public", "community", "survey", "input", "open house"],
    "transit_services": ["shuttle", "bus", "service"],
    "environment": ["air quality", "water quality"],
    "economy": ["economic", "jobs", "employment"]
}

# ====== IMPACT RULES ======
def generate_impact(tags):
    # --- Combined conditions (highest priority) ---
    if "transportation" in tags and "growth" in tags:
        return "May indicate increased traffic and infrastructure demand as the area grows."

    if "funding" in tags and "taxes" in tags:
        return "May affect local taxes or funding used for transportation and infrastructure projects."

    if "transportation" in tags and "transit_services" in tags:
        return "May improve access to public transportation and reduce reliance on driving."

    if "growth" in tags and "planning" in tags:
        return "May signal planned development that could influence housing demand and neighborhood changes."

    # --- Single tag conditions ---
    if "transportation" in tags:
        return "May affect commute times, traffic patterns, and accessibility."

    if "growth" in tags:
        return "May indicate population growth and increased housing demand."

    if "funding" in tags:
        return "May influence when and where infrastructure improvements occur."

    if "taxes" in tags:
        return "May involve local taxes that support regional improvements."

    if "governance" in tags or "organization" in tags:
        return "Identifies the agencies responsible for planning decisions that may affect the area."

    if "public_input" in tags:
        return "Indicates that community input may influence future development and planning decisions."

    if "transit_services" in tags:
        return "May provide access to public transportation options in the area."

    if "environment" in tags:
        return "May reflect environmental factors like air or water quality that affect livability."

    if "economy" in tags:
        return "May relate to job growth and economic conditions in the area."

    if "planning" in tags:
        return "May influence long-term development and infrastructure planning in the region."

    # --- Default fallback ---
    return "May influence local development and planning decisions."

# ====== LOAD TEXT ======
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

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
        matches = 0
        for word in keywords:
            # match whole words only
            if re.search(rf'\b{re.escape(word)}\b', text_lower):
                matches += 1

        if matches > 0:
            tag_scores[tag] = matches

    # Sort by strongest matches
    sorted_tags = sorted(tag_scores, key=tag_scores.get, reverse=True)

    # Limit to top 4
    top_tags = sorted_tags[:4]

    # Fallback if nothing matched
    if not top_tags:
        top_tags = ["planning"]

    return top_tags

# ====== WRITE TO JSONL (APPEND MODE) ======
start_id = 1

# Optional: continue IDs if file exists
try:
    with open(OUTPUT_FILE, "r") as f:
        start_id = sum(1 for _ in f) + 1
except FileNotFoundError:
    pass

with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
    for i, chunk in enumerate(chunks):
        tags = get_tags(chunk)
        impact = generate_impact(tags)

        entry = {
            "id": f"rmap_{start_id + i:03}",
            "source": SOURCE,
            "region": REGION,
            "tags": tags,
            "content": chunk,
            "impact": impact
        }

        f.write(json.dumps(entry) + "\n")

print(f"Added {len(chunks)} chunks to {OUTPUT_FILE}")
