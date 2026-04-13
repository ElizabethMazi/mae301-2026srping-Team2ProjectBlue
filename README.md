# Project Blue AI

## Overview

Project Blue AI is a retrieval-augmented AI assistant designed to help first-time homebuyers understand future development in Pima County, Arizona. It processes planning documents and provides clear, source-grounded answers through a simple web interface.

---

## 1. Setup Instructions

### Prerequisites

* Python 3.9+
* Git
* (Recommended) Virtual environment tool (venv or conda)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/project-blue-ai.git
cd project-blue-ai
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install core packages manually:

```bash
pip install streamlit openai numpy pandas
```

---

## 2. Project Structure

```
project-blue-ai/
│
├── data/
│   ├── raw/            # Original documents (URLs)
│   ├── processed/      # Cleaned text files
│   └── dataset.jsonl   # Structured dataset
│
├── scripts/
│   ├── app.py          # Streamlit app
│   ├── retrieve.py     # Retrieval logic
│   ├── generate.py     # Answer generation
│   
├── requirements.txt
└── README.md
```

---

## 3. Running the Demo

### Start the Streamlit App

```bash
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

* Add raw documents to `data/raw/`
* Convert PDFs to text files
* Save cleaned text in `data/processed/`

### Step 2: Build Dataset

* Run your data processing script to:

  * Chunk text
  * Assign IDs
  * Generate tags
  * Export to `dataset.jsonl`

### Step 3: Verify JSONL Format

Each entry should look like:

```json
"id": "rmap_001", "source": "RMAP 2020", "region": "Pima County, AZ", "text": "...", "tags": ["transportation", "infrastructure"]
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

Future improvements:

* Add quantitative metrics (precision, recall, answer accuracy)
* Create benchmark question set

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

## 9. Next Steps

* Improve semantic search (embeddings)
* Expand dataset coverage
* Add geographic context (maps)
* Strengthen evaluation framework

---

**End of README**
