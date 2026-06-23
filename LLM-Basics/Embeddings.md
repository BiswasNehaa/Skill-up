# Vector:

A vector is just a list of numbers. That's it. Nothing scary.

# These are all vectors:
[1, 2, 3]
[0.5, 0.1, 0.9, 0.3]
[128 numbers representing a word]
[384 numbers representing a sentence]

Analogy: Think of a city on a map. It has coordinates — latitude and longitude. Those 2 numbers represent that city's position. A vector is the same idea — a list of numbers that represent the "position" of a piece of text in meaning-space.
Key point
→Texts that mean similar things have vectors that are close to each other
→"dog" and "cat" will have closer vectors than "dog" and "car"
→This is what makes semantic search possible



# Embeddings :

An embedding is the process of converting text into a vector. You give it a sentence, it gives you back a list of numbers that capture the meaning of that sentence.

Analogy: Imagine translating a sentence into a secret code — but the code is designed so that similar sentences have similar codes. "I love pizza" and "Pizza is my favourite food" would have very similar codes. "I love pizza" and "The stock market crashed" would have very different codes.

# Text → Embedding model → Vector

"I love pizza"  →  [0.2, 0.8, 0.1, 0.5, ...]  (384 numbers)
"Pizza is great" →  [0.2, 0.7, 0.1, 0.6, ...]  (384 numbers)
"Stock market"  →  [0.9, 0.1, 0.7, 0.2, ...]  (384 numbers)

# First two are similar → vectors are close
# Third is different → vector is far away

Why embeddings exist
→Computers can't understand words — they only understand numbers
→Embeddings convert meaning into numbers computers can compare
→This is the foundation of your entire RAG project



# Cosine similarity :
Cosine similarity measures how similar two vectors are. It gives a score between -1 and 1.
→Score = 1 → vectors are identical (same meaning)
→Score = 0 → vectors are unrelated
→Score = -1 → vectors are opposite
Why cosine and not just subtraction? Because we care about the direction of the vector, not its size. "dog" and "dogs" might have different sized vectors but point in the same direction — cosine catches this correctly.

# You don't need to memorise the formula
# But understand what it does:

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

vec1 = np.array([[1, 0, 1]])   # "dog"
vec2 = np.array([[1, 0, 1]])   # "dogs" - same direction
vec3 = np.array([[0, 1, 0]])   # "car" - different direction

print(cosine_similarity(vec1, vec2))  # → 1.0 (identical)
print(cosine_similarity(vec1, vec3))  # → 0.0 (unrelated)

Why use cosine similarity instead of Euclidean distance?
A: Cosine similarity measures the angle between vectors, not their size. Two sentences can have different lengths but same meaning — cosine handles this correctly while Euclidean distance would treat them as different.




# FAISS :
FAISS = Facebook AI Similarity Search. It's a library that stores vectors and lets you find the most similar ones very fast.
Analogy: Imagine you have 10,000 sentences all converted to vectors. A user asks a question. You need to find the 3 most similar sentences. Comparing one by one would be slow. FAISS organises all vectors smartly so it can find the closest ones in milliseconds.
What FAISS does step by step
1You give it a list of vectors → it stores them in an index
2You give it a query vector → it finds the top-k most similar vectors
3It returns the indexes of those vectors so you can find the original text
FAISS vs normal SQL database
→SQL stores text and searches by exact match or keyword
→FAISS stores vectors and searches by meaning/similarity
→SQL: find rows WHERE name = "Neha" → exact
→FAISS: find sentences similar to "AI engineer jobs" → semantic


What does FAISS do and why did you use it in your project?
A: FAISS stores embeddings and enables fast similarity search. In my RAG project, I embedded all course data and stored it in FAISS. When a user asks a question, I embed the question and FAISS finds the most relevant course chunks instantly.