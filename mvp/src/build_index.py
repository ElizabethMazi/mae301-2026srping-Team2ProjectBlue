import sys
import os
sys.path.append(os.path.abspath("."))

import pickle
import numpy as np

from src.load import load_data
from src.embed import embed, prepare_text

# Make sure embeddings folder exists
os.makedirs("embeddings", exist_ok=True)

# Load data
data = load_data("data/documents.jsonl")

vectors = []
metadata = []

# Create embeddings
for i, row in enumerate(data):
    print(f"\nProcessing {i+1}/{len(data)}")

    text = prepare_text(row)
    print(f"Text length: {len(text)}")

    # Skip extremely large chunks (prevents hanging)
    if len(text) > 5000:
        print(f"Skipping {i} (text too long)")
        continue

    try:
        vector = embed(text)

        vectors.append(vector)
        metadata.append(row)

    except Exception as e:
        print(f"Skipping {i} due to error: {e}")
        continue

# Convert to numpy array
vectors = np.array(vectors).astype("float32")

# Save vectors
with open("embeddings/vectors.pkl", "wb") as f:
    pickle.dump(vectors, f)

# Save metadata
with open("embeddings/metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)

print("\nIndex built successfully!")
