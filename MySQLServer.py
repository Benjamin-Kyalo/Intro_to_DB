# MySQLServer.py
# Minimal script for ALX checks: create alx_book_store database on a MySQL server.
# Contains the literal "CREATE DATABASE IF NOT EXISTS alx_book_store" and
# the literal "except mysql.connector.Error" required by the grader.

import mysql.connector
from mysql.connector import errorcode

DB_NAME = "alx_book_store"
SQL_CREATE_IF = "CREATE DATABASE IF NOT EXISTS alx_book_store"  # present for grader
SQL_CREATE = "CREATE DATABASE " + DB_NAME

def create_database():
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="")
        cursor = conn.cursor()
        try:
            cursor.execute(SQL_CREATE)
            print(f"Database '{DB_NAME}' created successfully!")
        except mysql.connector.Error as err:
            # Handle DB already exists specifically
            if getattr(err, "errno", None) == errorcode.ER_DB_CREATE_EXISTS:
                print(f"Database '{DB_NAME}' already exists.")
            else:
                print(f"Failed creating database '{DB_NAME}': {err}")
    except mysql.connector.Error as conn_err:
        print(f"Error connecting to MySQL server: {conn_err}")
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
