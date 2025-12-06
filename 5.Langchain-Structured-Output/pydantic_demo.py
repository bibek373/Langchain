from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Employee(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0.0, lt=10.0, description="CGPA must be between 0.0 and 10.0")

new_employee = {'name': 'Bibek', 'age':23, 'email': 'abc@gmail.com', 'cgpa': 9.1}

employee = Employee(**new_employee)

print(employee)