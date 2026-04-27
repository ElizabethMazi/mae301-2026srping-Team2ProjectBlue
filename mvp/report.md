# Project Blue AI

---

# MVP Report

## Overview

Project Blue AI is a retrieval-augmented AI assistant designed to help first-time homebuyers understand future development in Pima County, Arizona. It processes planning documents and provides clear, source-grounded answers through a simple web interface. The MVP demonstrates a working prototype that combines document retrieval, language model reasoning, and a user-friendly experience.

---

# 1. Executive Summary

## Problem

Homebuyers often make purchasing decisions without knowing how future developments may affect traffic, schools, property values, or neighborhood growth. Although this information exists in public planning documents, it is difficult to locate and interpret.

## Solution

Project Blue AI simplifies this process by allowing users to ask natural language questions and receive summarized answers based on planning documents.

## What the MVP Does

- Accepts user questions about future development
- Searches relevant planning documents
- Retrieves useful passages
- Uses an AI model to generate readable answers
- Provides results through a web-based interface

---

# 2. User & Use Case

## Target User

**First-Time Homebuyer**

Someone purchasing a home who wants to understand future neighborhood growth before making a financial decision.

## Example Scenario

A user asks:

```text
What developments are planned near this neighborhood?
```

Project Blue AI returns a summary of future roads, residential projects, schools, or commercial growth mentioned in planning records.

---

# 3. System Design

## Purpose

The system is designed to convert user questions into reliable answers using planning documents as evidence.

## Core Components

- Web interface for user interaction
- Retrieval engine for searching documents
- Language model for summarization
- Processed planning document database

## How It Works

```text
User Question
     |
     v
Web Interface
     |
     v
Retriever Search
     |
     v
Relevant Document Chunks
     |
     v
Language Model
     |
     v
Final Response
```

## Why This Design Works

This structure allows the model to answer based on real documents instead of guessing.

---

# 4. Data

## Sources

The MVP uses publicly available regional planning information, including:

- Pima County planning reports
- Zoning and land use documents
- Transportation studies
- Future development proposals

## Preparation Process

Before use, documents were:

- Converted into readable text
- Cleaned for formatting errors
- Broken into smaller searchable chunks
- Organized for fast retrieval

## Current Scope

The current dataset is a prototype-sized regional collection focused on useful local planning knowledge.

---

# 5. Models

## AI Strategy

Project Blue AI uses a **Retrieval-Augmented Generation (RAG)** system.

## Model Roles

### Retrieval Model

Searches for the most relevant document passages based on the user’s question.

### Generative Model

Uses a frontier language model to turn retrieved evidence into clear summaries.

## Prompting Workflow

The model is guided to:

- Stay factual
- Use retrieved context
- Avoid unsupported claims
- Keep responses concise
- Admit uncertainty when needed

## Why This Model Choice Works

This combines search accuracy with strong natural language explanations.

---

# 6. Evaluation

## What Was Tested

The MVP was evaluated through prototype testing focused on:

- Accuracy of retrieved passages
- Response clarity
- Speed of responses
- Usefulness to homebuyers

## Example Prompt

```text
Will traffic increase near this area?
```

## Example Result

The system summarized likely road expansion projects and future congestion concerns based on planning records.

## Key Findings

- Responses were easy to understand
- Retrieval often found relevant context
- System worked quickly enough for live use

## Challenges Observed

- Broad prompts need clearer locations
- Some documents may be outdated
- Limited data can reduce precision

---

# 7. Limitations & Risks

## Current Limitations

- Geographic focus limited to Pima County
- Prototype-sized dataset
- No live city database updates
- Depends on public document quality

## Risks

### Hallucination Risk

If retrieval misses strong evidence, the model may overgeneralize.

### Data Freshness Risk

Planning decisions can change over time.

### Privacy Risk

Future saved searches or address storage would need security protections.

### Bias Risk

Public planning sources may not reflect every community perspective.

---

# 8. Next Steps

## Technical Improvements

- Expand geographic coverage
- Improve retrieval ranking accuracy
- Add citations to each response
- Integrate live planning updates
- Add interactive map search

## Product Improvements

- Compare two neighborhoods tool
- Home investment scorecard
- Mobile-ready experience
- Realtor dashboard
- Personalized saved reports

## Long-Term Vision

Project Blue AI can become a trusted planning intelligence assistant for buyers, investors, and communities.

---
