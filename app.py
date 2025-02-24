import streamlit as st
import os
from pdf_processing import extract_text_from_pdf, chunk_text
from embedding import generate_embeddings
from database import store_embedding
from query import query_database

st.title("AI-Powered PDF Q&A System")

# Uploading File
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
if uploaded_file:
    file_path = os.path.join("temp.pdf")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = extract_text_from_pdf(file_path)
    chunks = chunk_text(text)
    chunk_embeddings = [generate_embeddings(chunk) for chunk in chunks]

    for i, (chunk, embedding) in enumerate(zip(chunks, chunk_embeddings)):
        store_embedding(uploaded_file.name, i, chunk, embedding)

    st.success(f"PDF processed and stored successfully!")

# Q&A section
user_query = st.text_input("Ask a question:")
if user_query:
    answer = query_database(user_query)
    st.write("Answer:", answer)
