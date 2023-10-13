from pydantic import BaseModel

class UpdateUser(BaseModel):
    name: str = None
    email: str = None
    phone: str = None
    age: int = None
    city: str = None