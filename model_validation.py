from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Student(BaseModel):
    name: str = Field(min_length=5, max_length=20)
    email: str = EmailStr
    age: int
    contracts: Dict[str, str]

    @model_validator(mode="after")
    def ageParents(cls, model):
        if model.age < 18 and "parents_phone" not in model.contracts:
            raise ValueError("Age less than 18. Parents Phone no is a must.")
        return model

def add_student_data(student):
    print(student.name)
    print(student.email)
    print(student.age)
    print(student.contracts)

student = {
    "name": "Alice",
    "email": "example@g.bracu.ac.bd",
    "age": "12",
    "contracts": {"parents_phone":"0192"}
}

student_validated = Student(**student)
add_student_data(student_validated)