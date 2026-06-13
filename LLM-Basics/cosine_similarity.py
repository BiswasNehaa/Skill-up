
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

vec1 = np.array([[1, 0, 1]])   # "dog"
vec2 = np.array([[1, 0, 1]])   # "dogs" - same direction
vec3 = np.array([[0, 1, 0]])   # "car" - different direction

print(cosine_similarity(vec1, vec2))  # → 1.0 (identical)
print(cosine_similarity(vec1, vec3))  # → 0.0 (unrelated)