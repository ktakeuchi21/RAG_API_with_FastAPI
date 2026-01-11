# Build a RAG API with FastAPI (Medicare Knowledge Base)

This project implements a **Retrieval Augmented Generation (RAG) API** using **FastAPI**, **ChromaDB**, and **Ollama (tinyllama)**.  
The API allows dynamically adding documents to a vector database and querying them to generate grounded answers using a local LLM.

The knowledge base for this project focuses on **Medicare decision-making**, including enrollment timing, Original Medicare vs Medicare Advantage tradeoffs, Part D prescriptions, and common pitfalls.

---

## What This Project Does

The API exposes two core capabilities:

- **Add knowledge dynamically** to a persistent vector database
- **Answer user questions** using retrieved context instead of pure LLM generation

This demonstrates how RAG improves factual grounding, consistency, and decision quality compared to a model-only approach.

---

## Tech Stack

- **FastAPI** – API framework with automatic Swagger UI
- **ChromaDB** – Persistent vector database for embeddings
- **Ollama** – Local LLM runtime
- **tinyllama** – Lightweight open-source LLM
- **Python 3.10+**


## Project Structure

- app.py        # FastAPI server
- embed.py      # Embedding + chunking script
- kb.txt        # Medicare knowledge base
- db/           # ChromaDB persistent storage
- README.md

## Setup Instructions

### Prerequisites

- Python 3.10+
- Ollama 0.6.1+
- uvicorn 0.40.+
- chromadb 1.4.0+

### Pull the model:

ollama pull tinyllama

### Create Virtual Environment

python3 -m venv .venv
source .venv/bin/activate

### Install Dependencies

pip install fastapi uvicorn chromadb ollama

## Knowledge Base Setup

Create a file called kb.txt.

This file contains the Medicare knowledge base, including:
	•	Medicare fundamentals
	•	Enrollment timing (IEP, SEP, GEP)
	•	Original Medicare vs Medicare Advantage tradeoffs
	•	Part D prescription decision logic
	•	Common mistakes and scenarios

### Embedding the Knowledge Base

Run the embedding script:

python embed.py

What this does:
	•	Reads kb.txt
	•	Splits it into chunks
	•	Stores embeddings persistently in ChromaDB (./db)

## Running the API

Start the FastAPI server:
uvicorn app:app --reload

Open Swagger UI:
http://127.0.0.1:8000/docs

## API Endpoints

Add Knowledge

POST /add

Adds new text to the knowledge base.

Example:
curl -X POST "http://127.0.0.1:8000/add" \
  -G \
  --data-urlencode "text=Medicare Advantage plans typically use provider networks and may require referrals."

## Query the Knowledge Base (RAG)

POST /query

Example:
curl -X POST "http://127.0.0.1:8000/query" \
  -G \
  --data-urlencode "q=I’m turning 65 in 3 months and planning to retire. What Medicare decisions should I make first?"

## Before vs After: Demonstrating RAG

### Before (Model Only)

Without retrieval, the LLM:
	•	Gives generic explanations
	•	Misses enrollment timing nuance
	•	Does not reference Medicare tradeoffs clearly
	•	Has no grounding in a specific knowledge base

### After (With RAG)

With the Medicare knowledge base:
	•	Explains Initial Enrollment Period timing
	•	Walks through Original vs Medicare Advantage
	•	Highlights Part D prescription considerations
	•	Asks appropriate follow-up questions
	•	Produces structured, decision-oriented answers


#### Future Improvements
	•	Add metadata-based retrieval (topic, scenario)
	•	Return citations with each answer
	•	Add evaluation test suite
	•	Support batch document ingestion (JSONL)
	•	Expand scenario coverage
