import sys
import os
sys.path.append(os.path.abspath("."))

import pickle
import numpy as np

from scripts.load import load_data
from scripts.embed import embed, prepare_text


# Make sure embeddings folder exists
os.makedirs("embeddings", exist_ok=True)

# Load data
data = load_data("data/documents.jsonl")

vectors = []
metadata = []

# Create embeddings
for row in data:
    text = prepare_text(row)
    vector = embed(text)

    vectors.append(vector)
    metadata.append(row)

# Convert to numpy array
vectors = np.array(vectors).astype("float32")

# Save vectors
with open("embeddings/vectors.pkl", "wb") as f:
    pickle.dump(vectors, f)

# Save metadata
with open("embeddings/metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)

print("Index built successfully!")
