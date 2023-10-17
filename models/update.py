from pydantic import BaseModel

# Define a Pydantic model named "UpdateUser" that inherits from "BaseModel."
class UpdateUser(BaseModel):
    name: str = None
    email: str = None
    phone: str = None
    age: int = None
    city: str = None