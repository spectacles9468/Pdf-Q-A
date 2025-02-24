import numpy as np
from database import connect_db
from embedding import generate_embeddings

# Query for databse for answer
def query_database(user_query):
    user_embedding = generate_embeddings(user_query)
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT text FROM pdf_embeddings
        ORDER BY embedding <-> %s
        LIMIT 1;
        """, (np.array(user_embedding).tolist(),))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0] if result else "No relevant answer found."
