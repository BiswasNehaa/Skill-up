 📄 Load document → ✂️ Chunk text → 🔢 Embed chunks → 💾 Store in FAISS → ❓ User query → 🔍 Retrieve top-k → 📝 Build prompt → 🤖 LLM answers

# Walk me through your RAG pipeline end to end.
A: First I load the course catalog document using PyPDFLoader. Then I split it into 500-character chunks with 50-character overlap using RecursiveCharacterTextSplitter. Each chunk is embedded using HuggingFace sentence-transformers and stored in a FAISS vector index. When a user asks a question, I embed the query and retrieve the top 3 most similar chunks from FAISS. These chunks are injected into a prompt template along with the question and sent to LLaMA 3.3 via Groq API. The LLM generates an answer grounded only in the retrieved context.
