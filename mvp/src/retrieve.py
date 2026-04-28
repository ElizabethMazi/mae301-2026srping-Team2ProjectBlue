import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

from src.embed import embed


# Cache the data so it only loads once
@st.cache_resource
def load_data():
    with open("embeddings/vectors.pkl", "rb") as f:
        vectors = pickle.load(f)

    with open("embeddings/metadata.pkl", "rb") as f:
        metadata = pickle.load(f)

    return vectors, metadata


def search(query, k=5):
    # Load cached data
    vectors, metadata = load_data()

    # Convert query to vector
    q_vec = embed(query)
    q_vec = np.array([q_vec]).astype("float32")

    # Compute similarity scores
    similarities = cosine_similarity(q_vec, vectors)[0]

    # Get top k most similar indices
    top_k = np.argsort(similarities)[-k:][::-1]

    # Return matching documents
    return [metadata[i] for i in top_k]
