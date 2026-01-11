# Build a RAG API with FastAPI

This project implements a **Retrieval Augmented Generation (RAG) API** using **FastAPI**, **ChromaDB**, **Ollama (tinyllama)**, and **Swagger UI**.  
The API allows dynamically adding documents to a vector database and querying them to generate grounded answers using a local LLM.

The knowledge base for this project focuses on **Medicare decision-making**, including enrollment timing, Original Medicare vs Medicare Advantage tradeoffs, Part D prescriptions, and common pitfalls.

---

## What This Project Does

The API exposes two core capabilities:

- **Add knowledge dynamically** to a persistent vector database
- **Answer user questions** using retrieved context instead of pure LLM generation

This demonstrates how RAG improves factual grounding, consistency, and decision quality compared to a model-only approach.

---
## Before vs After: Demonstrating RAG

### Before (Model Only)
#### Sample query 1
I live in North Carolina, I’m turning 65 in 3 months, I’m planning to retire when I turn 65, I take a few ongoing prescription medications, and I want to understand my first Medicare decisions. What should I look at first and what tradeoffs should I consider?

#### Response before RAG
*As a highly specialized platform, Docker is designed to cater specifically to the needs of businesses who need to package applications with all their dependencies. To answer your questions on retiring when you turn 65, taking medications, and making your Medicare decisions, we would recommend reviewing the following information:*  
- *Retirement planning: Docker provides guidance on how to plan for retirement, including potential sources of income, investment options, and financial strategies. This can help you better understand what kind of benefits you may be eligible for under Medicare Part A (Hospital Insurance) and Part B (Medical Insurance).*  
- *Medication management: Docker also provides guidance on how to manage prescription medications, including potential drug interactions, dosages, and costs. This can help you better understand the impact of your prescriptions on your health and financial situation, as well as how to choose the right medications for your needs based on your goals and resources.*  
- *Medicare options: Docker provides information on how to enroll in Medicare Part A (Hospital Insurance) or Part B (Medical Insurance). This can help you better understand the benefits, costs, and requirements of each option, as well as any potential coverage gaps or limitations.*  

*In terms of tradeoffs, we would recommend considering these factors:*  
- *Income: Depending on your income, Medicare Part A and Part B may provide different levels of coverage for healthcare expenses. If you have a higher-earning job or are in a higher tax bracket, you may be better off opting for Part B, which offers more comprehensive coverage for medical expenses. However, if you qualify for Medicaid or other government assistance programs, you may want to consider choosing Medicare Part A instead.*  
- *Drug costs: Medicare Parts A and B may have drug cost limits that apply to certain prescription medications. If you need a specific medication for a chronic condition or ailment, it is worth considering if you can afford the full cost upfront or if there are alternatives with lower costs.*  
- *Coverage gaps: Medicare Part A and Part B offer coverage for some services, but not all. If you need certain medical procedures or treatments that are not covered by either option, you may want to consider supplementary health insurance or other alternative sources of financial support.*  

*In summary, Docker provides comprehensive information on retirement planning, medication management, and Medicare options. By understanding your unique needs and considering potential tradeoffs, you can make informed decisions about how to best prepare for retirement and optimize your Medicare benefits.*

#### Without retrieval, the LLM:
- Mentions "Docker" as the specialized platform to provide Medicare information.
- Gives generic explanations
- Provides irrelevant information (retirement planning, which is not relevant to Medicare health insurance)
- Does not reference Medicare tradeoffs clearly
- Has no grounding in a specific knowledge base

<img width="1158" height="442" alt="Before RAG_Test Q1" src="https://github.com/user-attachments/assets/0c2ac47d-cc98-4699-8d23-6248c119680d" />

### After (With RAG)

#### Same sample query 1
I live in North Carolina, I’m turning 65 in 3 months, I’m planning to retire when I turn 65, I take a few ongoing prescription medications, and I want to understand my first Medicare decisions. What should I look at first and what tradeoffs should I consider?

#### Response after RAG
- *Firstly, let's review some of the key benefits and drawbacks of Medicare:*  
*Benefits: Medicare offers several benefits, including:*  
- *Insurance coverage for medical, dental, and optical care*  
- *Healthcare services (e.g., hospitals, clinics)*  
- *Prescription drugs*  
- *Long-term care insurance*  
- *Advantage plans that combine Medicare coverage with employer-sponsored health insurance benefits*  
- *Telehealth options for remote consultations and video visits.*  

*Tradeoffs: While Medicare offers several benefits, there are some drawbacks to consider. Some of these include:*  
- *Out-of-pocket expenses (i.e., deductibles, copayments)*  
- *Limited access to specialists and other providers*  
- *Cost sharing required for some services, such as outpatient hospital care or skilled nursing facility stays.*  

*As you move forward in your Medicare decision-making process, keep these potential tradeoffs in mind. For example, if you're currently enrolled in a Part D prescription drug plan and decide to switch to Medicare Advantage (MA), you may have to pay higher deductibles or coinsurance rates for certain services. In contrast, if you choose not to enroll in any Medicare plan, you will be limited to specific providers and facilities, and may not be able to receive some of the benefits covered by Medicare.*  

#### With the Medicare knowledge base:
- Explains Initial Enrollment Period timing
- Walks through Original vs Medicare Advantage
- Highlights Part D prescription considerations
- Asks appropriate follow-up questions
- Produces structured, decision-oriented answers

<img width="1165" height="277" alt="After RAG_Test Q1" src="https://github.com/user-attachments/assets/91be01a4-5b27-4a8d-8d54-10ce73f08acb" />

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



#### Future Improvements
- Add metadata-based retrieval (topic, scenario)
- Return citations with each answer
- Add evaluation test suite
- Support batch document ingestion (JSONL)
- Expand scenario coverage
