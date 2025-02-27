# Pdf-Q-A
## Overview
This project is an AI-powered document Q&A system that allows users to upload PDFs, extract text, store embeddings in a database, and retrieve relevant answers using vector search. It uses Langchain (embedding), PostgreSQL (PgVector), and Streamlit to create an interactive interface for document-based querying.

## Features
PDF Upload & Text Extraction – Extracts text from uploaded PDFs using PyPDF.
Chunking for Efficient Retrieval – Splits long text into smaller chunks for better search results.
AI-Powered Embeddings – Converts text into numerical vectors using SentenceTransformers.
Vector Database Storage – Stores embeddings in PostgreSQL with PgVector for fast similarity search.
Question Answering System – Matches user queries with relevant document chunks based on vector similarity.
Streamlit UI – Provides an easy-to-use web interface for uploading PDFs and asking questions.

## Tools and Frameworks
Frontend: Streamlit (for UI & user interaction)
Backend: Python, LangChain (for text processing & chunking)
Machine Learning: SentenceTransformers (all-MiniLM-L6-v2) for text embeddings
Database: PostgreSQL with PgVector for efficient vector search
Libraries Used: PyPDF, SentenceTransformers, psycopg2, Streamlit, LangChain

## Setup
1. Install python dependencies (requirements.txt)
2. Set up PostgreSQL and PgVector.
3. Edit configurations in database.py and run the file to create the database
4. Run the application
```streamlit run app.py```
