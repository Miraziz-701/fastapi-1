from pydantic import BaseModel, EmailStr, Field

class Book(BaseModel):
    name: str
    author: str
    
class User(BaseModel):
    email: EmailStr
    password: str = Field(max_length=100, min_length=4)