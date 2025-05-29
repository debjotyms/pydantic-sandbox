from pydantic import BaseModel, EmailStr, Field, computed_field
from typing import Dict

class Student(BaseModel):
    name: str = Field(min_length=5, max_length=20)
    email: str = EmailStr
    age: int
    height: float
    weight: float
    contracts: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height)**2)
        return bmi

def add_student_data(student):
    print(student.name)
    print(student.email)
    print(student.age)
    print(student.height)
    print(student.weight)
    print(student.bmi)
    print(student.contracts)

student = {
    "name": "Alice",
    "email": "example@g.bracu.ac.bd",
    "age": "12",
    "height": 1.72,
    "weight": 75.2,
    "contracts": {"parents_phone":"0192"}
}

student_validated = Student(**student)
add_student_data(student_validated)