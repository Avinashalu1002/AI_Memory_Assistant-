from pypdf import PdfReader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from fastapi import FastAPI

# -------------------------------
# Step 1: Load PDF
# -------------------------------
file_path = r"C:\Users\Avinash\OneDrive\Desktop\ai_assistant\machine learning.pdf"

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# -------------------------------
# Step 2: Chunking
# -------------------------------
def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# -------------------------------
# Step 3: Process Data
# -------------------------------
print("Loading PDF...")
text = load_pdf(file_path)

print("Chunking text...")
chunks = chunk_text(text)
print(f"Total chunks created: {len(chunks)}")

# -------------------------------
# Step 4: Embeddings
# -------------------------------
print("Creating embeddings...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# -------------------------------
# Step 5: Vector Database
# -------------------------------
print("Storing in FAISS...")
db = FAISS.from_texts(chunks, embeddings)

# -------------------------------
# Step 6: LLM (Ollama - phi3)
# -------------------------------
print("Loading Ollama model...")
llm = Ollama(model="phi3")

# -------------------------------
# Step 7: Test Query (Console)
# -------------------------------
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

# -------------------------------
# Step 8: FastAPI App
# -------------------------------
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