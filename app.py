from pypdf import PdfReader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from fastapi import FastAPI

# Load PDF
file_path = r"C:\Users\Avinash\OneDrive\Desktop\ai_assistant\machine learning.pdf"

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


# Chunking
def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Process Data
print("Loading PDF...")
text = load_pdf(file_path)

print("Chunking text...")
chunks = chunk_text(text)
print(f"Total chunks created: {len(chunks)}")

# Embeddings
print("Creating embeddings...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Vector Database
print("Storing in FAISS...")
db = FAISS.from_texts(chunks, embeddings)


# LLM
print("Loading Ollama model...")
llm = Ollama(model="phi3")

#  Test
query = "What is machine learning?"

docs = db.similarity_search(query, k=3)
context = " ".join([doc.page_content for doc in docs])

response = llm.invoke(f"""
You are a helpful AI assistant.
Answer ONLY from the given context.
If the answer is not in the context, say "Not found".

Context:
{context}

Question:
{query}
""")

print("\nTest Response:\n", response)

# FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Memory Assistant is running"}

@app.get("/ask")
def ask(query: str):
    docs = db.similarity_search(query, k=3)
    context = " ".join([doc.page_content for doc in docs])

    response = llm.invoke(f"""
    You are a helpful AI assistant.
    Answer ONLY from the given context.
    If the answer is not in the context, say "Not found".

    Context:
    {context}

    Question:
    {query}
    """)

    return {"answer": response}
