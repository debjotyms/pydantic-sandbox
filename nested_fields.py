from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Dict

class Address(BaseModel):
    road_name: Annotated[str, Field(..., title="Road name of your house", max_length=20, min_length=5)]
    road_no: int

class Student(BaseModel):
    name: str = Field(min_length=5, max_length=20)
    email: str = EmailStr
    age: int
    contracts: Dict[str, str]
    address: Address

def add_student_data(student):
    print(student.name)
    print(student.email)
    print(student.age)
    print(student.contracts)
    print(student.address.road_name)

address = {
    "road_name": "Aftabnagar",
    "road_no": '3'
}

address_validated = Address(**address)

student = {
    "name": "Alice",
    "email": "example@g.bracu.ac.bd",
    "age": "12",
    "contracts": {"parents_phone":"0192"},
    "address": address_validated
}

student_validated = Student(**student)
add_student_data(student_validated)