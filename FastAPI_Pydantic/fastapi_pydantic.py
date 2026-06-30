from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class Student( BaseModel ):
    name: str
    age: int
    email: str
    course: Optional[str] = None
    
@app.post("/student")
def create_student(student: Student):
    return {
        "message": f"Created student {student.name}",
        "age": student.age,
        "course": student.course
    }
    
    