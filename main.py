from fastapi import FastAPI
from database.odm import create_document, read_all_documents, read_document, delete_document, update_document
from database.orm import connect_to_sqlite
from models.input import User
from models.update import UpdateUser
from fastapi import HTTPException
from bson import ObjectId 
from typing import List

app = FastAPI()

@app.get("/odm/", tags=["odm"])
def get_all_users() -> List[dict]:
    users = read_all_documents()
    return users

@app.post("/odm/add", tags=["odm"])
def create_user(user: User) -> dict:
    input_data = user.dict()
    doc_id = create_document(input_data)
    if doc_id:
        return {"id": str(doc_id)}
    raise HTTPException(status_code=500, detail="insertion faild")

@app.get("/odm/get", tags=["odm"])
def get_user(id: str) -> dict:
    user = read_document(ObjectId(id))
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/odm/delete", tags=["odm"])
def delete_user(id: str) -> bool:
    response = delete_document(ObjectId(id))
    if response is None:
        raise HTTPException(status_code=500, detail="unable to delete")
    return True

@app.patch("/odm/update", tags=["odm"])
def update_user(id: str, data: UpdateUser) -> bool:
    data_dict = {field_name: field_value for field_name, field_value in data.dict().items() if field_value is not None}
    response = update_document(ObjectId(id), data_dict)
    if response is None:
        raise HTTPException(status_code=500, detail="unable to update")
    return True
