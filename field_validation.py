from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Student(BaseModel):
    name: str = Field(min_length=5, max_length=20)
    email: str = EmailStr
    age: int
                      
    @field_validator('email', mode='before') # <- Will get value of email before type coercion
    @classmethod
    def email_validator(cls, value):
        domain = value.split('@')[1]
        if "g.bracu.ac.bd" in domain:
            return value
        else:
            raise ValueError("The student email is not valid")

    @field_validator('name')
    @classmethod
    def name_upper(cls, value):
        return value.upper()


def add_student_data(student):
    print(student.name)
    print(student.email)
    print(student.age)

student = {
    "name": "Alice",
    "email": "example@g.bracu.ac.bd",
    "age": "20"
}

student_validated = Student(**student) # <class '__main__.Student'>
add_student_data(student_validated)