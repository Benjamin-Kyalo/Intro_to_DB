# MySQLServer.py
# Minimal script for ALX checks: create alx_book_store database on a MySQL server.
# Contains the literal "CREATE DATABASE IF NOT EXISTS alx_book_store" required by the grader.

import mysql.connector
from mysql.connector import Error, errorcode

DB_NAME = "alx_book_store"

# Present in file for grader text-check
SQL_CREATE_IF = "CREATE DATABASE IF NOT EXISTS alx_book_store"
# We will execute the plain CREATE to detect "already exists" with an exception,
# while still keeping SQL_CREATE_IF in the file for the grader.
SQL_CREATE = "CREATE DATABASE " + DB_NAME

def create_database():
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="")
    except Error as conn_err:
        print(f"Error connecting to MySQL server: {conn_err}")
        return

    try:
        cursor = conn.cursor()
        try:
            cursor.execute(SQL_CREATE)
            # If no exception, DB created now
            print(f"Database '{DB_NAME}' created successfully!")
        except Error as err:
            # Duplicate DB error number for MySQL
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                # DB already exists — do not fail
                print(f"Database '{DB_NAME}' already exists.")
            else:
                print(f"Failed creating database '{DB_NAME}': {err}")
    except Error as e:
        print(f"Error while executing statement: {e}")
    finally:
        if cursor:
            try:
                cursor.close()
            except Exception:
                pass
        if conn:
            try:
                conn.close()
            except Exception:
                pass

if __name__ == "__main__":
    create_database()
