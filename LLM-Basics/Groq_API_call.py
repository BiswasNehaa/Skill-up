from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client= Groq (api_key=os.getenv("GROQ_API_KEY"))



response=client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role":"system","content":" You are a helpful assistant"},
        {"role":"user","content":" What is a token in LLM"}
    ],
    temperature=0,
    max_tokens=200
)


print(response.choices[0].message.content)