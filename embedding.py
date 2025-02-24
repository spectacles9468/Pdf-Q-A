from sentence_transformers import SentenceTransformer

# Selected Model
model = SentenceTransformer('all-MiniLM-L6-v2')  

# Generating Embedding
def generate_embeddings(text):
    return model.encode(text).tolist()
