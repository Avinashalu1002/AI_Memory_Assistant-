import streamlit as st
from pypdf import PdfReader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM

st.title("🧠 AI Memory Assistant")

# Load PDF
def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Chunking
def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Upload file
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    st.success("PDF uploaded successfully!")

    text = load_pdf(uploaded_file)
    chunks = chunk_text(text)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_texts(chunks, embeddings)

    llm = OllamaLLM(model="phi3")

    query = st.text_input("Ask a question")

    if query:
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

        st.write("### Answer:")
        st.write(response)