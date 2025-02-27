import numpy as np
from database import connect_db
from embedding import generate_embeddings

# Query for databse for answer
def query_database(user_query):
    user_embedding = generate_embeddings(user_query)
    conn = connect_db()
    cur = conn.cursor()

    user_embedding_str = "[" + ",".join(map(str, user_embedding)) + "]"
    
    cur.execute("""
        SELECT text FROM pdf_embeddings
        ORDER BY embedding <=> %s::vector
        LIMIT 1;
        """, (user_embedding_str,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0] if result else "No relevant answer found."
