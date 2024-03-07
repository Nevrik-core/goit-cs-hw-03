# Database Interaction and Automation Project

## Overview

This project demonstrates interaction with two types of databases: a PostgreSQL database for task management and MongoDB for storing information about cats. It includes a Python script to populate the PostgreSQL database with fake data and perform various SQL queries. Another Python script uses PyMongo to perform CRUD operations with MongoDB.

## PostgreSQL Database Setup

The PostgreSQL database contains three main tables:

- `users`: User information with fields for ID, full name, and email.
- `status`: Different statuses of tasks with fields for ID and status name.
- `tasks`: Tasks associated with users and their statuses.

Referential integrity is enforced with cascading delete operations for tasks related to users.

## MongoDB Database Setup

A MongoDB database stores documents in a collection named `cats`, with each document structured to include:

- `_id`: ObjectId of the document.
- `name`: Name of the cat.
- `age`: Age of the cat.
- `features`: An array of features or characteristics of the cat.

## Python Scripts

### PostgreSQL Interaction: `seed.py`

The `seed.py` script interacts with the PostgreSQL database to:

- Insert fake data using `Faker`.
- Execute a series of SQL queries to manipulate and retrieve task-related information.

### MongoDB Interaction: `main.py`

The `main.py` script uses `PyMongo` to:

- Create new cat documents in the `cats` collection.
- Read and display all cat documents or a specific cat by name.
- Update the age of a cat and add new features to it.
- Delete a cat document by name or all documents in the collection.

## SQL Queries

Various SQL queries are executed for tasks such as adding tasks, retrieving tasks by status, updating tasks, and more.

## MongoDB Operations

CRUD operations are implemented through functions that handle exceptions and provide clear, structured code.
