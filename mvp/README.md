# Project Blue AI

## Overview

Project Blue AI is a retrieval-augmented AI assistant designed to help first-time homebuyers understand future development in Pima County, Arizona. It processes planning documents and provides clear, source-grounded answers through a simple web interface.

---

## 1. Setup Instructions

### Prerequisites

* Python 3.9+
* Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/project-blue-ai.git
cd project-blue-ai
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Project Structure

```
mvp/
│
├── data/
│   ├── CleanDataCode.py   # Code used to convert PDFs to txt and clean it
│   ├── CreateJSON.py      # Code used to create the JSONL file
|   ├── dataset.jsonl      # Structured dataset
│   └── rawData.txt        # list of source PDFs with links used
│
├── src/
│   ├── __init__.py
|   ├── app.py          # Streamlit app
│   ├── build_index.py  # builds embeddings index
│   ├── embed.py        # embedding functionality
|   ├── generate.py     # Answer generation
|   ├── load.py         # Loads JSONL data
|   └── retrieve.py     # Retrieval logic
│
├──.env               # API key goes here
├──.gitignore         # Specifies files/folders Git should ignore
├── report.md         # Project report
├── requirements.txt  # List of Python dependencies needed to run the project
└── README.md         # Instructions for setup, usage, and project overview
```

---

## 3. Running the Demo

### Build index first (one time) and start the Streamlit App

```bash
python src/build_index.py
python -m streamlit run src/app.py
```

### What You Should See

* A browser window opens automatically
* Input box: "Ask a question about development"
* Generated answer appears below
* Sources listed underneath

If the app does not start:

* Make sure you are in the correct directory
* Confirm dependencies are installed
* Check that `app.py` prints (debugging)

---

## 4. Reproducing the Pipeline

### Step 1: Prepare Data

* Convert PDFs to text files `data/CleanDataCode.py`

### Step 2: Build Dataset

* Chunk text, assign IDs, Generate tags, and export to `documents.jsonl` using `CreateJSON.py`

### Step 3: Verify JSONL Format

Each entry should look like:

```json
"id": "rmap_001", "source": "RMAP 2020", "region": "Pima County, AZ", "text": "...", "tags": ["...", "...", "..."]
```

---

## 5. Running Experiments

### Retrieval Testing

* Modify queries inside `app.py` or test directly in `retrieve.py`
* Evaluate relevance of returned documents

### Generation Testing

* Inspect outputs from `generate.py`
* Compare answers against source documents

---

## 6. Benchmarking (Current State)

Current evaluation is qualitative:

* Check if answers:

  * Are grounded in retrieved documents
  * Correctly summarize planning content
  * Avoid hallucination

---

## 7. Troubleshooting

**Issue: Streamlit hangs or does not start**

* Ensure correct Python environment is active
* Try restarting terminal
* Add debug prints to `app.py`

**Issue: No results returned**

* Check dataset.jsonl exists
* Verify retrieval logic

**Issue: Poor answers**

* Improve tagging function
* Increase dataset size

---

## 8. Notes

* This project uses a Retrieval-Augmented Generation (RAG) architecture
* nanoGPT integration is experimental and not required for the demo

---

**End of README**
