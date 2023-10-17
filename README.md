# FastAPI User Management with ODM, ORM

FastAPI User Management is a web application that allows you to manage user records using both Object-Document Mapping (ODM) with MongoDB and Object-Relational Mapping (ORM) with SQLite databases. This project demonstrates how to create, read, update, and delete (CRUD) user records using FastAPI with different database technologies.

## Features

- **ODM (Object-Document Mapping)**: The application supports user management with MongoDB using ODM. You can create, retrieve, update, and delete user records stored in a MongoDB database.

- **ORM (Object-Relational Mapping)**: The application also includes support for user management with SQLite using ORM. It enables you to perform CRUD operations on user records stored in an SQLite database.

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python.

- [MongoDB](https://www.mongodb.com/): A NoSQL database used for ODM (Object-Document Mapping).

- [SQLite](https://www.sqlite.org/): A lightweight, serverless, self-contained SQL database engine used for ORM (Object-Relational Mapping).

- [Pydantic](https://pydantic-docs.helpmanual.io/): Data validation and parsing library, used for defining data models.

## Installation

1. Clone the repository:

   ```bash
    git clone https://github.com/cyber-evangelists/orm-odm.git

```bash
cd orm-odm

pip install -r requirements.txt

uvicorn main:app --reload
```



## Usage

- ODM Endpoints:

        - GET /odm/: Get a list of all users.
        - POST /odm/add: Create a user.
        - GET /odm/get: Get a user by ID.
        - PATCH /odm/update: Update a user by ID.
        - DELETE /odm/delete: Delete a user by ID.

- ORM Endpoints:

        - GET /orm/: Get a list of all users.
        - POST /orm/add: Create a user.
        - GET /orm/get: Get a user by ID.
        - PATCH /orm/update: Update a user by ID.
        - DELETE /orm/delete: Delete a user by ID.

# Conclusion

## ODM (Object-Document Mapping)

ODM, as implemented in our project with MongoDB, offers a flexible approach for managing user records, making it particularly well-suited for applications dealing with evolving and unstructured data. The integration of Pydantic models enhances its suitability for such use cases.

**Pros of ODM:**

- *Schemaless*: ODM is ideal for applications with varying data structures, allowing for adaptability as data requirements change.
- *Scalability*: MongoDB, used in conjunction with ODM, can efficiently handle large volumes of data and offers horizontal scalability.
- *Fast Development*: The combination of FastAPI and ODM streamlines development, supporting rapid project iteration.

**Cons of ODM:**

- *Lack of Transactions*: MongoDB lacks support for transactions, which can be a limitation when performing multi-document operations.
- *Limited Query Capabilities*: ODMs may not provide the same extensive range of querying options available in traditional SQL databases.

## ORM (Object-Relational Mapping)

In our project with SQLite, ORM plays a crucial role in mapping object-oriented models to a relational database. ORM proves to be a strong choice for applications that require robust data consistency, transaction support, and complex querying capabilities.

**Pros of ORM:**

- *Data Consistency*: ORM, when used with SQL databases like SQLite, ensures data consistency and supports ACID transactions.
- *Strong Querying*: ORM empowers applications with advanced querying capabilities, enabling complex data manipulation.
- *Compatibility*: ORM aligns seamlessly with relational databases and SQL-based tools, making it suitable for a wide range of applications.

**Cons of ORM:**

- *Schema Constraints*: ORM's reliance on SQL databases may introduce constraints related to schema definitions, potentially limiting flexibility when data structures need to evolve.
- *Slower Development*: ORM setup and usage can be more complex compared to ODM, which may result in slower development cycles.

In conclusion, the choice between ODM and ORM should be guided by the specific needs of your project. ODM excels in applications dealing with flexible, changing data structures, while ORM is better suited for data-intensive projects requiring strong data consistency and advanced SQL-like querying capabilities. Your choice should be determined by your project's database requirements and overall priorities.


## Contribution

Feel free to contribute to this project by opening issues or submitting pull requests.
License


This project is licensed under the MIT License. See the LICENSE file for details.
