#!/usr/bin/python3
import mysql.connector

def stream_users():
    """
    Generator that streams users one by one from the user_data table.
    Yields each row as a dictionary.
    """
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # change if needed
            password="yourpassword",  # change if needed
            database="ALX_prodev"
        )

        cursor = connection.cursor(dictionary=True)  # dictionary=True gives results as dicts
        cursor.execute("SELECT * FROM user_data;")

        # Single loop: yield rows one by one
        for row in cursor:
            yield row

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
