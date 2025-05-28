from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Student(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin: AnyUrl
    weight: float
    allergies: Optional[List[str]] = None
    contract: Dict[str, str]

def add_student_data(student):
    print(student.name)
    print(student.age)
    print(student.weight)
    print(student.allergies)
    print(student.contract)
    print(type(student.age))

    print("Information inserted into the Database!")

student = {
    "name": "Alice",
    "age": 30, 
    "weight": 65.5, 
    "allergies": ["peanuts", "shellfish"], 
    "contract": {"type": "enrollment", "duration": "1 year"}
}

student_validated = Student(**student) # <class '__main__.Student'>
add_student_data(student_validated)