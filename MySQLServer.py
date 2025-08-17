# MySQLServer.py
# Creates the database `alx_book_store` on a PostgreSQL server.
# NOTE: this script is PostgreSQL-compatible because you run scripts on PostgreSQL.

import sys
try:
    import psycopg2
    from psycopg2 import sql, errors
except ImportError:
    print("Missing dependency: install psycopg2-binary (pip install psycopg2-binary)")
    sys.exit(1)

# --- Config: change these if needed ---
DB_NAME = "alx_book_store"
PG_HOST = "localhost"
PG_PORT = 5432
PG_USER = "postgres"
PG_PASSWORD = ""   # add password if your server requires it
# -------------------------------------

def create_database(dbname, host, port, user, password):
    conn = None
    cur = None
    try:
        # connect to default 'postgres' database to run CREATE DATABASE
        conn = psycopg2.connect(dbname="postgres", user=user, password=password, host=host, port=port)
        # CREATE DATABASE cannot run inside a transaction, so set autocommit
        conn.autocommit = True
        cur = conn.cursor()

        try:
            cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname)))
            print(f"Database '{dbname}' created successfully!")
        except errors.DuplicateDatabase:
            # If DB exists, don't fail — just inform
            print(f"Database '{dbname}' already exists. No action needed.")
        except Exception as e:
            # Any other error while creating DB
            print(f"Failed to create database '{dbname}': {e}")

    except Exception as conn_err:
        # Error while connecting to server
        print(f"Error connecting to the PostgreSQL server: {conn_err}")
    finally:
        # Clean up/close resources
        if cur:
            try:
                cur.close()
            except Exception:
                pass
        if conn:
            try:
                conn.close()
            except Exception:
                pass

if __name__ == "__main__":
    create_database(DB_NAME, PG_HOST, PG_PORT, PG_USER, PG_PASSWORD)
