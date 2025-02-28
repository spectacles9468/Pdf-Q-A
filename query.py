import numpy as np
from database import connect_db
from embedding import generate_embeddings
from transformers import pipeline

def refine_answer_with_llm(user_query, retrieved_texts):
    context = " ".join(retrieved_texts)  # Combine multiple chunks

    prompt = f"""
    You are an AI assistant. Given the following context from a document:
    ---
    {context}
    ---
    Answer the following question concisely and accurately:
    {user_query}
    """

    messages = [
    {"role": "user", "content": prompt},
    ]
    try:
        pipe = pipeline(
            "text-generation", 
            model="EleutherAI/gpt-neo-1.3B", 
            device_map="cpu"
        )
        response = pipe(prompt, max_new_tokens=200)
    except:
        return retrieved_texts
    else:
        return response[0]["generated_text"]

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
    # Extract the text from the database query results
    # retrieved_texts = [row[0] for row in result]

    # Use LLM to refine the response
    # return refine_answer_with_llm(user_query, retrieved_texts)
