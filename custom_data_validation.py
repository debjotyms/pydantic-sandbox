from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Optional, Annotated

class Student(BaseModel):
    name: str = Field(min_length=5, max_length=20)
    email: str = EmailStr
    age: Annotated[int, Field(default=None, gt=18, lt=30, title="Age of the student", description="The age should be greater than 18 and less than 30", examples=["21", "23"])]
    weight: Annotated[float, Field(default=None, strict=True)]
    allergies: Optional[List[str]] = Field(max_length=10)
    contract: Dict[str, str]

def add_student_data(student):
    print(student.name)
    print(student.age)
    print(student.weight)
    print(student.allergies)
    print(student.contract)
    print("Information inserted into the Database!")

student = {
    "name": "Alice",
    "age": 25, 
    "weight": 65,
    "allergies": ["peanuts", "shellfish"], 
    "contract": {"type": "enrollment", "duration": "1 year"}
}

student_validated = Student(**student) # <class '__main__.Student'>
add_student_data(student_validated)