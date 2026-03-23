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

## Demo
<img width="1075" height="698" alt="Screenshot 2026-03-23 123855" src="https://github.com/user-attachments/assets/acdd93c1-7e18-4e9c-814a-fceef33fd6dc" />

<img width="1018" height="648" alt="Screenshot 2026-03-23 123756" src="https://github.com/user-attachments/assets/99a4166f-d16a-4e36-8bec-213b43da5ee1" />

