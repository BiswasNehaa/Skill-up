from fastapi import FastAPI

app= FastAPI()

# GET endpoint - simplest one
@app.get("/")
def home():
    return {"message":"Hello World"}

# GET with path parameter
@app.get("/student/{name}")
def get_student(name: str):
    return {"student":name}


""" 
Breaking it down
→ @app.get("/") — decorator that says "this function handles GET requests to /"
→ {name} in the URL — path parameter, captured as function argument
→ uvicorn — the server that actually runs FastAPI
→ --reload — auto-restarts server when you save code changes

"""

# PATH PARAM - part of the URL itself

@app.get("/studet/{student_id}")
def get_student( student_id: int):
    return {"id": student_id}
#URL: /student/5

# QUERY PARAM - after the ? in URL
@app.get("/search")
def search(query: str, limit: int=10):
    return {"query": query, "limit":limit}
# URL: /search?query=AI&limit=5

#BODY - data sent in POST request, not in URL
@app.post("/search")
def create_student(name: str, age: int):
    return {"name": name, "age":age}

"""
When to use which
→Path param → identifying a specific resource (student id 5)
→Query param → optional filters/settings (search, limit, sort)
→Body → sending larger data, usually with POST/PUT

When would you use a path param vs a query param?
A: Path param when identifying a specific resource, like /user/5. 
Query param for optional filters or settings, like /search?query=AI&limit=10.

"""

# Regular function - fine for simple operations
@app.get("/students")
def get_students():
    return {"students": ["Neha", "Priya"]}



""" 

# Async function - use when calling external APIs, DB, file I/O
@app.get("/ask")
async def ask_llm(query: str):
    response = await some_llm_call(query)  # non-blocking
    return {"answer": response}

"""
