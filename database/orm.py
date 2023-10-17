import sqlite3
table_name = "mytable"

def connect_to_sqlite():
    # Establish a connection to the SQLite database and return the connection and cursor.
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    return conn, cursor

def create_table():
    conn, cursor = connect_to_sqlite()
    # Create a table in the database if it doesn't exist, defining its structure.
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT,
                        phone TEXT,
                        age INTEGER,
                        city TEXT)''')

def create_record(data):
    conn, cursor = connect_to_sqlite()
    try:
        # Insert a new record into the SQLite table with the provided data.
        cursor.execute(f"INSERT INTO {table_name} (name, email, phone, age, city) VALUES (?, ?, ?, ?, ?)",
                       (data["name"], data["email"], data["phone"], data["age"], data["city"]))
        conn.commit()
        return cursor.lastrowid
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return None
    finally:
        if conn:
            conn.close()

def read_record(user_id):
    conn, cursor = connect_to_sqlite()
    try:
        # Retrieve a specific record by its ID and return it as a dictionary.
        cursor.execute(f"SELECT * FROM {table_name} WHERE id=?", (user_id,))
        user = cursor.fetchone()
        if user is not None:
            columns = [desc[0] for desc in cursor.description]
            user_dict = dict(zip(columns, user))
            return user_dict
        else:
            return None
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return None
    finally:
        if conn:
            conn.close()

def update_record(user_id, new_data):
    conn, cursor = connect_to_sqlite()
    try:
        # Update a record with new data, with flexibility for any number of updates.
        set_clause = ", ".join([f"{key} = ?" for key in new_data.keys()])
        values = tuple(new_data.values())
        update_query = f"UPDATE {table_name} SET {set_clause} WHERE id = ?"
        cursor.execute(update_query, values + (user_id,))
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return None
    finally:
        if conn:
            conn.close()

def delete_record(user_id):
    conn, cursor = connect_to_sqlite()
    try:
        # Delete a record with the given ID.
        cursor.execute(f"DELETE FROM {table_name} WHERE id=?", (user_id,))
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return None
    finally:
        if conn:
            conn.close()

def read_all_records():
    conn, cursor = connect_to_sqlite()
    try:
        # Read and return all records from the SQLite table as a list of dictionaries.
        cursor.execute(f"SELECT * FROM {table_name}")
        columns = [desc[0] for desc in cursor.description]  # Get column names
        users = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return users
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return None
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_table()

    # Uncomment and modify the code as needed to test your functions.
    # data = {"name": "John", "email": "abc@xyz.con", "phone": "03124578963", "age": 30, "city": "New York"}
    # user_id = create_record(data)
    # print(f"Inserted record with ID: {user_id}")

    # retrieved_record = read_record(user_id)
    # print("Retrieved record:")
    # print(retrieved_record)

    updated_data = {"age": 31, "name": "ali"}
    modified_count = update_record(7, updated_data)
    print(f"Modified {modified_count} record(s)")

    # Uncomment the code below to read all records, delete records, etc.
    # updated_record = read_record(user_id)
    # print("Updated record:")
    # print(updated_record)

    # all_records = read_all_records()
    # print("All records in the collection:")
    # print(all_records)
    # for record in all_records:
    #     print(record)

    # deleted_count = delete_record(user_id)
    # print(f"Deleted {deleted_count} record(s)")

    # deleted_record = read_record(user_id)
    # print("Deleted record:")
    # print(deleted_record)
