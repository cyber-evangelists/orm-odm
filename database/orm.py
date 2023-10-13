import sqlite3

def connect_to_sqlite(database_name):
    conn = sqlite3.connect(f"{database_name}.db")
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor, table_name):
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT,
                        phone TEXT,
                        age INTEGER,
                        city TEXT)''')

def create_document(cursor, conn, table_name, data):
    try:
        cursor.execute(f"INSERT INTO {table_name} (name, email, phone, age, city) VALUES (?, ?, ?, ?, ?)",
                       (data["name"], data["email"], data["phone"], data["age"], data["city"]))
        conn.commit()
        return cursor.lastrowid
    except Exception as e:
        return str(e)

def read_document(cursor, table_name, document_id):
    try:
        cursor.execute(f"SELECT * FROM {table_name} WHERE id=?", (document_id,))
        document = cursor.fetchone()
        return document
    except Exception as e:
        return str(e)

def update_document(cursor, conn, table_name, document_id, new_data):
    try:
        cursor.execute(f"UPDATE {table_name} SET age=? WHERE id=?", (new_data["age"], document_id))
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        return str(e)

def delete_document(cursor, conn, table_name, document_id):
    try:
        cursor.execute(f"DELETE FROM {table_name} WHERE id=?", (document_id,))
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        return str(e)

def read_all_documents(cursor, table_name):
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        documents = cursor.fetchall()
        return documents
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    conn, cursor = connect_to_sqlite("mydatabase")
    table_name = "mycollection"

    create_table(cursor, table_name)

    data = {"name": "John", "email": "abc@xyz.con", "phone": "03124578963", "age": 30, "city": "New York"}
    document_id = create_document(cursor, conn, table_name, data)
    print(f"Inserted document with ID: {document_id}")

    retrieved_document = read_document(cursor, table_name, document_id)
    print("Retrieved document:")
    print(retrieved_document)

    updated_data = {"age": 31}
    modified_count = update_document(cursor, conn, table_name, document_id, updated_data)
    print(f"Modified {modified_count} document(s)")

    updated_document = read_document(cursor, table_name, document_id)
    print("Updated document:")
    print(updated_document)

    all_documents = read_all_documents(cursor, table_name)
    print("All documents in the collection:")
    for doc in all_documents:
        print(doc)

    deleted_count = delete_document(cursor, conn, table_name, document_id)
    print(f"Deleted {deleted_count} document(s)")

    deleted_document = read_document(cursor, table_name, document_id)
    print("Deleted document:")
    print(deleted_document)

    conn.close()
