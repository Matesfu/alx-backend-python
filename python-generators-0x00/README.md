# SQL Streaming Generator Project

## 📌 Overview
This project demonstrates how to:
- Set up a MySQL database programmatically with Python.
- Create a table (`user_data`) to store user information.
- Insert sample data from a CSV file (`user_data.csv`).
- Use a **Python generator** to stream rows from the SQL database one by one instead of loading everything into memory.

It is built as part of the ALX Backend Python tasks.

---

## 📂 Files

### `seed.py`
This file contains all the reusable functions for database setup and data handling:
- `connect_db()` → Connects to the MySQL server.
- `create_database(connection)` → Creates the database `ALX_prodev` if it doesn’t exist.
- `connect_to_prodev()` → Connects to the `ALX_prodev` database.
- `create_table(connection)` → Creates the `user_data` table with fields:
  - `user_id` (UUID, primary key, indexed)
  - `name` (VARCHAR, not null)
  - `email` (VARCHAR, not null)
  - `age` (DECIMAL, not null)
- `insert_data(connection, data)` → Reads from `user_data.csv` and inserts rows into the table.
- `stream_rows(connection, batch_size=1)` → A **generator function** that streams rows from the database one by one (or in batches).


