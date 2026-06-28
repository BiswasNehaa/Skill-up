Problem: 
LLMs are trained on general data. They don't know YOUR specific data — your university courses, your company docs, your PDF. If you ask "what courses should I take to become an AI engineer at my university?" — the LLM has no idea.

Naive solution:
Put the entire document in the prompt. But context window is limited — you can't fit 100 pages into a prompt.

RAG solution: 
Instead of giving the LLM everything, retrieve only the relevant parts and give those. Retrieval Augmented Generation.

Analogy: 
Imagine an open book exam. You don't memorise the entire textbook — you just know which page to look at for each question. RAG does the same — finds the right "page" and gives it to the LLM.

Q: What is RAG and why does it exist?
A: RAG stands for Retrieval Augmented Generation. It exists because LLMs don't know your specific data, and you can't fit entire documents into the context window. RAG retrieves only the relevant chunks and passes them to the LLM to generate a grounded answer.
