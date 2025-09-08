#!/usr/bin/python3
import mysql.connector

def stream_users_in_batches(batch_size):
    """
    Generator that streams users in batches from the user_data table.
    Each yield returns a list of rows (batch).
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          
            password="password",
            database="user_data"
        )

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data;")

        while True:
            batch = cursor.fetchmany(batch_size)  # fetch batch_size rows
            if not batch:  # stop if no more rows
                break
            yield batch

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def batch_processing(batch_size):
    """
    Processes batches of users.
    Filters users with age > 25 and prints them.
    """
    for batch in stream_users_in_batches(batch_size):       # loop 1
        for user in batch:                                  # loop 2
            if user["age"] > 25:                            # filtering
                print(user)
