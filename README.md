# Build a RAG API with FastAPI

---

## Project Overview

This project implements a **Retrieval Augmented Generation (RAG) API** using **FastAPI**, **ChromaDB**, and **Ollama (tinyllama)**. The API allows documents to be ingested into a local vector database and queried in real time, grounding LLM responses in retrieved context rather than relying on model knowledge alone.

The primary goal of this project was tp **build the entire pipeline from scratch** so I can work with embeddings, retrieval, prompt construction, and API design. While I had previously worked with RAG-enabled tools, this project focuses on building a minimal but complete RAG pipeline from first principles.

The knowledge base for this project focuses on **Medicare decision-making**, including enrollment timing, Original Medicare vs Medicare Advantage tradeoffs, Part D prescriptions, and common pitfalls.

### Why Medicare?

Medicare is a strong RAG test case because it involves nuanced tradeoffs, enrollment timing, and plan design details that are easy for language models to oversimplify or hallucinate. Small factual errors can materially change decision outcomes, making grounding especially important.

---

## Why I Built This

I’ve relied heavily on RAG-powered tools like ChatGPT and Gemini in my work, but had never implemented one end-to-end myself. This project was an opportunity to:

- demystify how retrieval actually works under the hood
- understand how vector search quality affects downstream generation
- explore the limitations of small, local models without retrieval
- learn how to expose RAG functionality through a clean API surface

I intentionally chose a **local-first stack** (Ollama + tinyllama) to remove external dependencies and better observe model behavior.

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

---

## What This Project Demonstrates

This project shows:

- how to build a RAG system using open-source tools
- how retrieval changes LLM output quality
- how APIs like FastAPI make experimentation fast and observable
- how even small models can perform well when given the right context
- how hallucinations surface when retrieval fails or is missing

---

## Core Technologies

**FastAPI**: API framework with automatic OpenAPI/Swagger UI
- lightweight and fast to spin up
- Python-native and well-suited for ML workflows

**ChromaDB**: persistent vector database for embeddings
- is easy to run locally without external services
- supports persistent storage for embeddings
- integrates cleanly with Python

**Ollama**: local LLM runtime
- run models locally without relying on external APIs
- free to use

**tinyllama**: lightweight open-source language model
- its small model makes hallucinations more visible when context is missing
- demonstrates how much RAG can compensate for model size

**curl / Swagger UI**: API testing and inspection
- test endpoints interactively
- validate request/response shapes

---

## Architecture Overview

At a high level, the system works as follows:

1. Documents are embedded and stored in ChromaDB
2. A user sends a question to the `/query` endpoint
3. ChromaDB retrieves the most relevant document chunks
4. Retrieved text is injected into the LLM prompt as context
5. The model generates a response grounded in that context
6. The API returns the response to the client

This separation between **retrieval** and **generation** is the core design principle of RAG.

---

## Building the Medicare Knowledge Base (kb.txt)

To make the RAG demo meaningful, I needed a knowledge base that contains actual decision logic (tradeoffs, scenarios, enrollment timing) instead of only definitions. I created a Medicare-focused KB using ChatGPT Deep Research to generate structured content, then stored it locally as `kb.txt` for embedding into ChromaDB.

### Step 1: Generate domain content (ChatGPT Deep Research)

I used ChatGPT Deep Research to generate a Medicare knowledge base that includes:
- core concepts (Parts A/B/C/D)
- enrollment timing (IEP/SEP/GEP) and common pitfalls
- decision framework (Original Medicare vs Medicare Advantage)
- Medigap + Part D reasoning
- scenario-based test cases (turning 65 soon, still working, travel, prescription-heavy users)

Example prompt used for Deep Research:

```text
Create a Medicare knowledge base for a RAG system. Include decision-oriented content, not just definitions:
- Parts A/B/C/D
- Initial Enrollment Period vs Special Enrollment Period vs penalties (high level)
- Original Medicare vs Medicare Advantage tradeoffs (networks, flexibility, predictable costs)
- Medigap and Part D (how to choose, what to compare)
- Common mistakes and how to avoid them
- 10–20 realistic scenarios phrased as user questions
Write it as retrieval-friendly chunks with short titles and clear headings.
Avoid year-specific premium numbers.
```

### Step 2: Create kb.txt

I saved the generated content into kb.txt. In this project version, I embedded the entire file as a single document in ChromaDB for simplicity.

### Step 3: Embed the knowledge base into ChromaDB

I use embed.py to read kb.txt and store it into a persistent ChromaDB collection.
```text
import chromadb

client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection("docs")

with open("kb.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["kb"])

print("Embedding stored in Chroma")
```

Run it:

```text
python embed.py
```

### Step 3: Embed the knowledge base into ChromaDB

Start the API server

```text
uvicorn app:app --reload
http://127.0.0.1:8000/docs
```

#### Example query (curl)

This query is designed to trigger Medicare enrollment + plan tradeoff retrieval:

```text
curl -X POST "http://127.0.0.1:8000/query" \
  -G \
  --data-urlencode "q=I’m turning 65 in 3 months, planning to retire, and I take ongoing prescription medications. How should I think about Medicare Advantage versus Original Medicare, and what should I check first?"
```

Expected behavior:
- Chroma retrieves the most relevant Medicare content from kb.txt
The model answer references decision points (Original vs Advantage), enrollment timing, and Part D considerations

#### Add new knowledge dynamically

The /add endpoint makes the KB expandable without re-running embed.py.

```text
curl -X POST "http://127.0.0.1:8000/add" \
  -G \
  --data-urlencode "text=Medicare Advantage plans typically use provider networks and may require referrals, while Original Medicare allows nationwide access to providers who accept Medicare."
```

#### How the Retrieval Works (in app.py)

Current retrieval behavior is intentionally minimal:
- n_results=1
- the retrieved document is used as the entire context
- the model answers using the retrieved context + question

---

## Building the RAG API

### `/query` endpoint

The `/query` endpoint accepts a natural language question and performs the following steps:

- runs a semantic search against the vector database
- selects the most relevant document chunks
- constructs a prompt that includes both the question and retrieved context
- sends the prompt to the local LLM
- returns the generated answer

This endpoint makes it easy to compare **model-only responses** vs **RAG-grounded responses**.


---

### `/add` endpoint

The `/add` endpoint allows new content to be added dynamically to the knowledge base without redeploying the application.

This enables:
- rapid iteration on documentation
- live updates to the KB
- experimentation with different content structures

It also demonstrates how RAG systems can evolve over time rather than remaining static.

---

## Testing and Exploration

I tested the API using both **curl** and **Swagger UI**.

Swagger UI was particularly useful because it:
- made endpoints self-documenting
- allowed rapid iteration without additional tools
- exposed request/response shapes clearly

Testing with generic questions (e.g. “What is Kubernetes?”) made it easy to verify retrieval behavior before moving into more complex domains.

---

## Before vs After: Why RAG Matters

Without retrieval, the model:
- gives generic, sometimes confident-sounding answers
- may hallucinate facts
- lacks grounding in specific documentation

With retrieval:
- answers become more structured and relevant
- explanations reflect the underlying documents
- hallucinations are reduced
- the model asks better follow-up questions when context is missing

This contrast was one of the most valuable takeaways from the project.

---

## Challenges and Learnings

**Challenges**
- debugging port conflicts and environment issues
- understanding how retrieval parameters affect output
- learning how much chunking strategy matters
- interpreting when hallucinations are model-driven vs retrieval-driven

**Wins**
- getting end-to-end RAG working locally
- dynamically updating the knowledge base
- seeing immediate improvements in answer quality
- gaining intuition for how RAG systems behave in practice

---

## Future Improvements

Potential next steps include:
- adding metadata-based retrieval (topic, category)
- returning citations alongside answers
- increasing top-k retrieval and ranking results
- building an evaluation suite for response quality
- expanding the KB with more scenario-based content

---

## Conclusion

This project deepened my practical understanding of how retrieval quality, chunking, and prompt construction interact in real RAG systems.

Even with a small local model, retrieval dramatically improved answer quality, reinforcing that **context often matters more than model size**.
