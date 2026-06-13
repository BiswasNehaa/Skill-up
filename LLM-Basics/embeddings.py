# embeded sentences 
from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Your sentences
sentences = [
    "I love programming in Python",
    "Machine learning is fascinating",
    "The weather is sunny today",
    "Deep learning uses neural networks",
    "I enjoy cooking Italian food"
]

# Convert to vectors
embeddings = model.encode(sentences)

print(embeddings.shape)  # → (5, 384) = 5 sentences, 384 numbers each
print(embeddings[0])     # print first vector - 384 numbers

# store in FAISS

import faiss

# Create FAISS index
dimension = 384  # must match embedding size
index = faiss.IndexFlatL2(dimension)

# Add embeddings to index
index.add(embeddings.astype('float32'))
print(f"Total stored: {index.ntotal}")  # → 5

# Query — find most similar to this question
query = "What is neural network?"
query_vector = model.encode([query]).astype('float32')

# Search top 2 most similar
distances, indexes = index.search(query_vector, k=2)

print("Most similar sentences:")
for i in indexes[0]:
    print(f"  → {sentences[i]}" )


