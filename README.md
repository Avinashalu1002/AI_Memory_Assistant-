# AI Memory Assistant RAG

This project is a Retrieval-Augmented Generation (RAG) system that allows users to upload PDFs and ask questions based on the document content.

## Features in Project

* Upload PDF documents
* Automatic text chunking
* Semantic search using FAISS
* Local LLM (Ollama - phi3)
* Streamlit UI for interaction

## Technologies Used

* Python
* Streamlit
* LangChain
* HuggingFace Embeddings
* FAISS (Vector Database)
* Ollama (Local LLM)

## Steps to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Start Ollama:

```
ollama run phi3
```

3. Run app:

```
streamlit run streamlit_app.py
```

## Note

This project runs locally using Ollama for privacy and zero API cost.

## Future Implementation

* Multi-document support
* Chat history (memory)
* Cloud deployment
* User authentication
