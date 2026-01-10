<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Build a RAG API with FastAPI

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-devops-api)

**Author:** kai.takeuchi21@gmail.com  
**Email:** kai.takeuchi21@gmail.com

---

![Image](http://learn.nextwork.org/calm_rose_happy_ackee/uploads/ai-devops-api_g3h4i5j6)

---

## Introducing Today's Project!

In this project, I will create a RAG API with FastAPI to build a chatbot from documents in my local documents.

### Key services and concepts

I used Python and Ollama for local AI development, build a RAG API using FastAPI, Chroma, and tinyllama. Used curl and Swagger UI to create and retrieve API documentation.

### Challenges and wins

This project took me approximately 3 hours. The most challenging part was debugging different versions, active ports, and navigating new tools like Swagger UI and curl.

It was very rewarding to be able to quickly insert knowledge base documentation, and be able to retrieve it using Swagger UI.

### Why I did this project

I did this project because I've long relied on RAG with ChatGPT, Gemini, and other AI tools, but have not build it myself yet.

---

## Setting Up Python and Ollama

In this step, I'm setting up Python and Ollama to run a LLM on my local machine.

### Python and Ollama setup

![Image](http://learn.nextwork.org/calm_rose_happy_ackee/uploads/ai-devops-api_i9j0k1l2)

### Verifying Python is working

### Ollama and tinyllama ready

Ollama is the LLM I'll run on my local. I decided to use the tinyllama model because it's lightweight and free to use. 

---

## Setting Up a Python Workspace

In this step, I'm setting up my workspace to keep all of my files in one place for this project.

### Python workspace setup

### Virtual environment

A virtual environment is an isolated Python environment that keeps your project's dependencies separate from other Python projects on your computer.

Without a virtual environment, installing packages for one project could break another project that needs a different version. A virtual environment makes sure each project has its own set of packages, preventing conflicts.

### Dependencies

The packages I installed are FastAPI, ChromaDB, Uvicorn, and ollama. Chrom

FastAPI handles incoming questions, ChromaDB finds relevant documents, the ollama client sends everything to tinyllama for answer generation, and uvicorn serves it all up.

![Image](http://learn.nextwork.org/calm_rose_happy_ackee/uploads/ai-devops-api_u1v2w3x4)

---

## Setting Up a Knowledge Base

In this step, I'm creating a knowledge base about health insurance so users can find out what type of insurance would benefit them most based on their location, age, employment status, health history, conditions, and other relevant information.

### Knowledge base setup

![Image](http://learn.nextwork.org/calm_rose_happy_ackee/uploads/ai-devops-api_t1u2v3w4)

### Embeddings created

Embeddings are numerical representations of text. I created them using Chroma, and they're key for RAG because Ollama would scan for the embeddings that are similar in vector to retrieve from.

---

## Building the RAG API

In this step, I'm building a RAG API. An API lets software retrieve and share data with other apps. I'm using FastAPI because it's fast, easy to use, and automatically generates interactive documentation. 

### FastAPI setup

### How the RAG API works

Here's how the RAG API would work:
1. Question arrives: Someone sends a question to your API at /query.
2. Search your documents: Chroma searches through your knowledge base to find text that matches the question's meaning.
3. Get matching text: Chroma returns the most relevant information from your documents (this is called "context").
4. Generate answer: The question and the matching text are sent together to tinyllama, which creates an answer.
5. Send back the answer: The answer is sent back to whoever asked the question.

![Image](http://learn.nextwork.org/calm_rose_happy_ackee/uploads/ai-devops-api_f3g4h5i6)

---

## Testing the RAG API

In this step, I'm testing my RAG API using Swagger UI. Using Swagger UI because it lets me visually explore the API endpoints, see what params they accept from a browser.

### Testing the API

### API query breakdown

I queried my API by running the command curl -X POST "http://127.0.0.1:8000/query" -G --data-urlencode "q=What is Kubernetes?"

The API responded with Kubernetes is a container orchestration platform used to manage containers at scale. It allows organizations to deploy, manage, and scale their containerized    applications automatically. With Kubernetes, developers can easily build, deploy, and manage complex distributed systems using containers without the need for manual intervention or specialized skills."

![Image](http://learn.nextwork.org/calm_rose_happy_ackee/uploads/ai-devops-api_g3h4i5j6)

### Swagger UI exploration

Swagger UI lets me test with API via a web browser. I used it to test the API I created on the retrieving the definition of Kubernetes. The best part about using Swagger UI was not having to download any other tool.

---

## Adding Dynamic Content

In this project extension, I'm going to add a new /add endpoint so I can dynamically add content to the knowledge base through the API.

### Adding the /add endpoint

![Image](http://learn.nextwork.org/calm_rose_happy_ackee/uploads/ai-devops-api_w9x0y1z2)

### Dynamic content endpoint working

The /add endpoint allows me to add new knowledge base documentation. This is useful because I no longer need to update individual txt files, but can send/post the KB via API.

---

---
