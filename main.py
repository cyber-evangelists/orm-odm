from fastapi import FastAPI, HTTPException
from database.odm import connect_to_mongodb, create_document, read_all_documents, read_document, delete_document, update_document
from database.orm import create_table, read_all_records, create_record, read_record, delete_record, update_record
from models.input import User
from models.update import UpdateUser
from bson import ObjectId
from typing import List

app = FastAPI()

@app.on_event("startup")
def startup():
    # Initialize the database connections during the startup of the FastAPI application.
    connect_to_mongodb()  # Connect to MongoDB
    create_table()  # Create the SQLite table

# ------------------------- ODM functions -------------------------
@app.get("/odm/", tags=["ODM"])
def get_all_odm_users() -> List[dict]:
    # Retrieve and return all documents from the MongoDB collection.
    users = read_all_documents()
    return users

@app.post("/odm/add", tags=["ODM"])
def create_odm_user(user: User) -> dict:
    # Create a new document in the MongoDB collection based on user input.
    input_data = user.dict()
    doc_id = create_document(input_data)
    if doc_id:
        return {"id": str(doc_id)}
    raise HTTPException(status_code=500, detail="ODM insertion failed")

@app.get("/odm/get", tags=["ODM"])
def get_odm_user(id: str) -> dict:
    # Retrieve and return a document from the MongoDB collection by its ID.
    user = read_document(ObjectId(id))
    if user:
        return user
    raise HTTPException(status_code=404, detail="ODM User not found")

@app.delete("/odm/delete", tags=["ODM"])
def delete_odm_user(id: str) -> bool:
    # Delete a document from the MongoDB collection by its ID.
    response = delete_document(ObjectId(id))
    if str(response) == '1':
        return True
    elif str(response) == '0':
        raise HTTPException(status_code=404, detail="ODM id not found!")
    raise HTTPException(status_code=500, detail="ODM unable to delete")

@app.patch("/odm/update", tags=["ODM"])
def update_odm_user(id: str, data: UpdateUser) -> bool:
    # Update a document in the MongoDB collection by its ID with new data.
    data_dict = {field_name: field_value for field_name, field_value in data.dict().items() if field_value is not None}
    response = update_document(ObjectId(id), data_dict)
    if str(response) == '1':
        return True
    elif str(response) == '0':
        raise HTTPException(status_code=404, detail="ODM id not found!")
    raise HTTPException(status_code=500, detail="ODM unable to update")

# ------------------------- ORM functions -------------------------
@app.get("/orm/", tags=["ORM"])
def get_all_orm_users() -> List[dict]:
    # Retrieve and return all records from the SQLite database table.
    users = read_all_records()
    return users

@app.post("/orm/add", tags=["ORM"])
def create_orm_user(user: User) -> dict:
    # Create a new record in the SQLite database table based on user input.
    input_data = user.dict()
    user_id = create_record(input_data)
    if user_id:
        return {"id": str(user_id)}
    raise HTTPException(status_code=500, detail="ORM insertion failed")

@app.get("/orm/get", tags=["ORM"])
def get_orm_user(id: str) -> dict:
    # Retrieve and return a record from the SQLite database table by its ID.
    user = read_record(int(id))
    if user:
        return user
    raise HTTPException(status_code=404, detail="ORM User not found")

@app.delete("/orm/delete", tags=["ORM"])
def delete_orm_user(id: str) -> bool:
    # Delete a record from the SQLite database table by its ID.
    response = delete_record(int(id))
    if str(response) == '1':
        return True
    elif str(response) == '0':
        raise HTTPException(status_code=404, detail="ORM id not found!")
    raise HTTPException(status_code=500, detail="ORM unable to delete")

@app.patch("/orm/update", tags=["ORM"])
def update_orm_user(id: str, data: UpdateUser) -> bool:
    # Update a record in the SQLite database table by its ID with new data.
    data_dict = {field_name: field_value for field_name, field_value in data.dict().items() if field_value is not None}
    response = update_record(int(id), data_dict)
    if str(response) == '1':
        return True
    elif str(response) == '0':
        raise HTTPException(status_code=404, detail="ORM id not found!")
    raise HTTPException(status_code=500, detail="ORM unable to update")
