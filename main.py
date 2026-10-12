from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "Worlds!"}

@app.get("/greet")
def greet():
    return {"message": "Hello from FastAPI!"}

@app.get("/greet/{name}")
def greet_name(name: str, age: Optional[int] = None):
    return {"message": f"Hello, {name}! You are {age}."}

class Student(BaseModel):
    name: str
    age: int
    roll: int
    grade: Optional[str] = None
    
@app.post("/create_student")
def create_student(student: Student):
    return {"name": student.name, 
            "age": student.age, 
            "roll": student.roll, 
            "grade": student.grade
            }