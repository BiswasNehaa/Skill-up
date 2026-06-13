# Note

# LLM
An LLM is a model trained on large amounts of text data. It generates output by predicting the next token based on the input it receives, one token at a time.


# Token
→APIs charge you per token — input tokens + output tokens
→Context window is measured in tokens, not words
→LLM reads and writes in tokens, not characters.


 A token is a small chunk of text — roughly 4 characters or 0.75 words. LLMs process text as tokens, not words or characters. APIs charge based on token count.


# Context Window
Context window is the max tokens an LLM can process at once. You can't send an entire document — it won't fit. RAG solves this by retrieving only the relevant chunks and sending those instead.

Why this matters for RAG
→You can't stuff an entire PDF into the prompt — it won't fit
→That's exactly why RAG exists — retrieve only the relevant chunks
→If context overflows, older messages get cut off silently


# System prompt , user prompt , temperature

Every API call has 3 roles:
🔧 system — instructions for how the LLM should behave. Set once. "You are a helpful academic advisor."

👤 user — the actual question or input from the user

🤖 assistant — the LLM's previous replies (for multi-turn chat)


# Temperature
Temperature controls randomness of output.
→temperature=0 → same answer every time, very precise. Use for factual tasks.
→temperature=1 → creative, varied answers. Use for writing/brainstorming.
→Your RAG project should use temperature=0 — you want accurate, grounded answers.


 Temperature 0, because RAG needs accurate, deterministic answers grounded in the retrieved context. Higher temperature adds randomness which could cause hallucination.

 
