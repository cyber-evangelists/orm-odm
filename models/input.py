from pydantic import BaseModel

# Define a Pydantic model named "User" that inherits from "BaseModel."
class User(BaseModel):
    name: str
    email: str
    phone: str
    age: int
    city: str