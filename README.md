# AI Research Assistant

An AI-powered research assistant that allows users to upload PDF documents, ask natural language questions, and receive answers grounded in the document content using a local Retrieval-Augmented Generation (RAG) pipeline.

This project demonstrates how to build a practical Generative AI application using document ingestion, semantic retrieval, vector search, and a locally running Large Language Model.

---

## Features

- Upload one or more PDF documents
- Extract and chunk document text
- Generate embeddings using HuggingFace models
- Store vectors in ChromaDB
- Ask questions through a chat interface
- Generate answers using a local LLM with Ollama
- Display source snippets and page references
- Reset uploaded documents and chat history

---

## Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Ollama
- Llama 3.2 (3B)
- PyPDF

---

## Architecture

PDF Documents
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
Chroma Vector Database
↓
Retriever
↓
Local LLM (Ollama)
↓
Answer + Source Citations


---

## Project Structure

ai-research-assistant/
├── app.py
├── requirements.txt
├── .env
├── README.md
├── src/
│ ├── ingest.py
│ ├── retriever.py
│ └── qa_chain.py
├── data/
│ └── uploads/
└── chroma_db/


---

## How It Works

1. The user uploads one or more PDF files.
2. The application extracts text from the PDFs.
3. The text is split into smaller chunks.
4. Chunks are converted into vector embeddings.
5. The embeddings are stored in ChromaDB.
6. When a question is asked, the retriever finds the most relevant chunks.
7. The relevant context is passed to a local LLM through Ollama.
8. The assistant returns an answer along with source snippets.

---

## Installation

Clone the repository:

git clone https://github.com/MuhammadKhubaib1/ai-research-assistant.git

Move into the project folder:

cd ai-research-assistant

Create and activate a virtual environment.

Windows PowerShell

python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Install Ollama
---

Download and install Ollama:

https://ollama.com/download

After installing, download the model used in this project:

ollama run llama3.2:3b

When the model finishes downloading, exit with:

/bye

Run the Application
---

Start the Streamlit app:

streamlit run app.py

Then open the local URL shown in the terminal, usually:

http://localhost:8501

Example Use Cases

Research paper question answering

Document summarization

Company knowledge assistants

Academic reading support

Policy and report analysis

Key Learning Outcomes

This project demonstrates practical experience in:

Retrieval-Augmented Generation (RAG)

Vector databases

Semantic search

Local LLM deployment

Prompt design

Streamlit app development

End-to-end GenAI application building

Future Improvements

Add conversation memory

Support DOCX and TXT files

Add hybrid search

Add reranking

Export chat history

Deploy with Docker

Add user authentication

Author

Muhammad Khubaib Malik

Generative AI Engineer | Python | LangChain | RAG Systems
