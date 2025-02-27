import psycopg2
import numpy as np

## Parameters
DB_CONFIG = {
    "dbname": "database",
    "user": "postgres",
    "password": "root",
    "host": "localhost",
    "port": "5432",
}

## Functions
#Establishing connection
def connect_db():
    return psycopg2.connect(**DB_CONFIG)

#Creating tables
def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pdf_embeddings (
            id SERIAL PRIMARY KEY,
            document_name TEXT,
            chunk_id INTEGER,
            text TEXT,
            embedding vector(384)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    # print("Connection build.")

#Storing embedding
def store_embedding(doc_name, chunk_id, text, embedding):
    """Store document embeddings in PostgreSQL."""
    conn = connect_db()
    cur = conn.cursor()

    formatted_text = text.replace("\n", " ").strip()
    cur.execute("INSERT INTO pdf_embeddings (document_name, chunk_id, text, embedding) VALUES (%s, %s, %s, %s)",
                (doc_name, chunk_id, formatted_text, np.array(embedding).tolist()))
    conn.commit()
    cur.close()
    conn.close()

# Creating table for the first time
create_table()
