# Database Interaction and Automation Project

## Overview

This project includes the creation of a PostgreSQL database for task management and the development of a Python script to populate the database with fake data using the Faker library. Additionally, SQL queries are executed to manipulate and retrieve data according to various business requirements.

## Database Setup

The PostgreSQL database is structured with three main tables:

- `users`: contains user information with fields for id, full name, and email.
- `status`: stores different statuses of tasks with fields for id and status name.
- `tasks`: holds tasks associated with users and their statuses, with fields for id, title, description, status_id, and user_id.

Relations are established between tables to ensure referential integrity, with cascading delete set up for tasks related to users.

## Python Script

A Python script named `seed.py` is utilized to connect to the PostgreSQL database and insert fake data into the tables. The script utilizes the `psycopg2` library to interact with the database and the `Faker` library to generate random user and task data.

## SQL Queries

A variety of SQL queries are executed to perform operations such as:

- Adding a new task for a specific user.
- Retrieving all tasks not yet completed.
- Deleting a specific task by its id.
- Finding users with a certain email domain.
- Updating a user's name.
- Getting the count of tasks for each status.
- Retrieving tasks assigned to users with a specific email domain.
- Selecting tasks without a description.
- Choosing users and their tasks that are 'in progress'.
- Obtaining users and the count of their tasks.
