1. Objective and Current MVP Definition

Objective
Project Blue AI aims to help first-time homebuyers in Pima County, Arizona understand how specific areas are likely to develop over time. The system aggregates complex planning documents (zoning, transportation, infrastructure, and regional plans) and translates them into clear, actionable insights.

Problem
Relevant development information is currently fragmented across lengthy government documents, making it difficult for non-experts to interpret future impacts on neighborhoods.

Current MVP
The current minimum viable product (MVP) is a retrieval-augmented AI assistant that:

Accepts natural language questions about development
Retrieves relevant excerpts from processed planning documents
Generates human-readable answers with cited sources
Runs via a Streamlit interface


2. What Has Been Built So Far

Data Pipeline

Collection of regional planning documents (e.g., PAG, RTA, RMAP)
Conversion of PDFs to clean text format
Structuring of data into JSONL format with fields such as:
id
source
region
text
tags

Tagging System

Keyword-based tagging function
Scores and ranks tags based on frequency of keyword matches
Assigns top 3–4 tags per document chunk for improved retrieval relevance

Retrieval System

Search function (retrieve.py) that returns relevant document chunks based on query
Enables grounding of AI responses in real planning data

Generation System

Answer generation module (generate.py)
Combines user query with retrieved documents to produce responses

User Interface

Streamlit application (app.py)
Simple input box for user queries
Displays generated answers and associated sources


3. Technical Approach

This project follows a Retrieval-Augmented Generation (RAG) architecture.

Data Layer
Raw documents → cleaned text files
Text split into manageable chunks
Stored in JSONL format for efficient processing
Retrieval Layer
Keyword/tag-based retrieval system
Returns top relevant document chunks for a given query
Generation Layer
Uses a generative language model to synthesize answers
Inputs:
User query
Retrieved document context
Output:
Natural language explanation grounded in sources
Interface Layer
Streamlit front-end for rapid prototyping
Provides interactive querying and output visualization


4. Evidence of Progress
Successful extraction and cleaning of planning documents
Functional JSONL dataset with structured entries
Working tagging system improving retrieval relevance
End-to-end pipeline:
Query → Retrieval → Answer generation → Display
Initial Streamlit app deployed locally

Example Capability User can ask:
"What transportation projects are planned in this area?"
System returns a synthesized answer with references to PAG/RTA documents.


5. Current Limitations and Open Risks

Data Limitations

Limited dataset size and coverage
Potential bias toward available documents
Incomplete representation of all planning sources

Retrieval Limitations

Keyword-based retrieval may miss semantically relevant content
Tagging system is heuristic and not learned

Generation Risks

Potential hallucinations if retrieval is weak
Dependence on prompt quality and context formatting

System Limitations

No geographic reasoning (e.g., parcel-level insights)
No structured forecasting or predictive modeling
Limited evaluation metrics for answer quality


6. Plan for Phase 3

Data Expansion

Add more planning documents (zoning maps, infrastructure plans)
Improve document parsing and cleaning

Retrieval Improvements

Transition to embedding-based semantic search
Replace or augment keyword tagging with vector similarity

Model Enhancements

Improve prompt engineering for more reliable outputs
Explore fine-tuning or nanoGPT integration (optional)

Product Improvements

Enhance Streamlit UI (filters, map integration)
Add location-based queries

Evaluation Framework

Define metrics for answer accuracy and relevance
Create benchmark questions and expected outputs


7. Generative Project Details

Data Description

Source: Public planning and infrastructure documents from pima.gov
Format: JSONL with structured metadata and tagged text chunks

Modeling Details

Generative language model used for answer synthesis
RAG approach ensures grounding in real data

Inference Setup

Query → retrieve top documents → pass context to model → generate answer

Representative Outputs

Summarized explanations of planning initiatives
Clear, user-friendly interpretations of technical documents

Evaluation

Currently qualitative (manual inspection)
Future work includes quantitative evaluation metrics

Limitations

Dependent on retrieval quality
Limited dataset affects completeness
