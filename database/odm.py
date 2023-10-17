import pymongo
from bson import ObjectId

def connect_to_mongodb():
    try:
        global collection
        # Connect to MongoDB and initialize the global 'collection' variable.
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["mydatabase"]
        collection = db["mycollection"]
        print("[INFO] MongoDB started!")
    except:
        print("[ERROR] MongoDB startup failed!")

def create_document(data):
    try:
        # Create a new document in the MongoDB collection based on the provided data.
        inserted_document = collection.insert_one(data)
        return inserted_document.inserted_id
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return None

def read_document(document_id):
    try:
        # Read a document from the MongoDB collection by its ID and remove the '_id' field.
        document = collection.find_one({"_id": document_id}, projection={'_id': False})
        return document
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return None  

def update_document(document_id, new_data):
    try:
        # Update a document in the MongoDB collection by its ID with new data.
        updated_document = collection.update_one({"_id": document_id}, {"$set": new_data})
        return updated_document.modified_count
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return None

def delete_document(document_id):
    try:
        # Delete a document from the MongoDB collection by its ID.
        deleted_document = collection.delete_one({"_id": document_id})
        return deleted_document.deleted_count
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return None

def read_all_documents():
    try:
        # Read and return all documents from the MongoDB collection, converting ObjectId to a string.
        documents = list(collection.find())
        for doc in documents:
            doc['_id'] = str(doc['_id'])  # Convert ObjectId to a string
        return documents
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return None

if __name__ == "__main__":
    # Uncomment and modify the code as needed to test your functions.
    # data = {"name": "John", "email": "abc@xyz.con", "phone": "03124578963", "age": 30, "city": "New York"}
    # document_id = create_document(data)
    # print(f"Inserted document with ID: {document_id}")

    # retrieved_document = read_document(document_id)
    # print("Retrieved document:")
    # print(retrieved_document)

    # updated_data = {"age": 31}
    # modified_count = update_document(document_id, updated_data)
    # print(f"Modified {modified_count} document(s)")

    # Uncomment the code below to read all documents, delete documents, etc.
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