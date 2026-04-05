**AI Research Assistant (RAG-Based Document Q&A System)**

**Overview**

This project is an AI-powered research assistant that enables users to upload PDF documents and ask natural language questions, receiving accurate answers grounded directly in the document content.

It is built using a Retrieval-Augmented Generation (RAG) pipeline, combining semantic search with a local Large Language Model to deliver reliable and context-aware responses.

This type of system is ideal for businesses and teams looking to turn their internal documents into intelligent knowledge assistants.

**Key Features**

• Upload and process one or more PDF documents
• Extract and intelligently chunk document content
• Generate embeddings using HuggingFace models
• Store and retrieve vectors using ChromaDB
• Ask natural language questions through an interactive interface
• Generate answers using a local LLM with Ollama
• Display source snippets and page references for transparency
• Reset documents and chat history easily

**Real-World Use Cases**

• Internal company knowledge base assistant
• Research and academic document analysis
• Policy and compliance document Q&A
• Customer support knowledge systems
• Report and document summarization

**Tech Stack**

• Python
• Streamlit
• LangChain
• ChromaDB
• HuggingFace Embeddings
• Ollama
• Llama 3.2 (3B)
• PyPDF

**System Architecture**

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
Answer with Source Citations

**How It Works**

Users upload one or more PDF documents
The system extracts and processes the text
Content is split into optimized chunks
Chunks are converted into vector embeddings
Embeddings are stored in a vector database
When a question is asked, relevant chunks are retrieved
The retrieved context is passed to the LLM
The system generates an accurate answer with source references

**Project Structure**

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

**Installation**

Clone the repository:

git clone https://github.com/MuhammadKhubaib1/ai-research-assistant.git

cd ai-research-assistant

Create and activate a virtual environment

**Install dependencies:**

pip install -r requirements.txt

**Setup Local LLM (Ollama)**

Download and install Ollama:

https://ollama.com/download

Then pull the model:

ollama run llama3.2:3b

**Run the Application**

streamlit run app.py

Open in browser:

http://localhost:8501

**Key Capabilities Demonstrated**

• Building end-to-end RAG pipelines
• Working with vector databases and embeddings
• Implementing semantic search systems
• Integrating local LLMs for privacy-focused AI solutions
• Designing document-aware AI assistants
• Developing interactive AI applications with Streamlit

**Future Improvements**

• Add conversation memory
• Support additional file formats (DOCX, TXT)
• Implement hybrid search (semantic + keyword)
• Add reranking for improved retrieval accuracy
• Export chat history
• Docker-based deployment
• User authentication and multi-user support

**Author**

Muhammad Khubaib Malik

Generative AI Engineer
Specializing in LLM applications, RAG systems, and AI-powered tools
