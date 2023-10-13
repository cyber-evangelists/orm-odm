import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]


def create_document(data):
    try:
        inserted_document = collection.insert_one(data)
        return inserted_document.inserted_id
    except Exception as e:
        return False

def read_document(document_id):
    try:
        document = collection.find_one({"_id": document_id}, projection={'_id': False})
        return document
    except Exception as e:
        return None  # Return None when document is not found


def update_document(document_id, new_data):
    try:
        updated_document = collection.update_one({"_id": document_id}, {"$set": new_data})
        return updated_document.modified_count
    except Exception as e:
        return None

def delete_document(document_id):
    try:
        deleted_document = collection.delete_one({"_id": document_id})
        return deleted_document.deleted_count
    except Exception as e:
        return None

def read_all_documents():
    try:
        documents = list(collection.find())
        for doc in documents:
            doc['_id'] = str(doc['_id'])  # Convert ObjectId to a string
        return documents
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # collection = connect_to_mongodb("mydatabase", "mycollection")

    data = {"name": "John", "email": "abc@xyz.con", "phone": "03124578963", "age": 30, "city": "New York"}
    document_id = create_document(data)
    print(f"Inserted document with ID: {document_id}")

    retrieved_document = read_document(document_id)
    print("Retrieved document:")
    print(retrieved_document)

    updated_data = {"age": 31}
    modified_count = update_document(document_id, updated_data)
    print(f"Modified {modified_count} document(s)")

    # updated_document = read_document(document_id)
    # print("Updated document:")
    # print(updated_document)

    # all_documents = read_all_documents()
    # print("All documents in the collection:")
    # for doc in all_documents:
    #     print(doc)

    # deleted_count = delete_document(document_id)
    # print(f"Deleted {deleted_count} document(s)")

    # deleted_document = read_document(document_id)
    # print("Deleted document:")
    # print(deleted_document)
