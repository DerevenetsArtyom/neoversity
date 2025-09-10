"""PostgreSQL connection module"""

from contextlib import contextmanager
from psycopg2 import connect, DatabaseError

config = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "password12345",
    "host": "localhost",
    "port": "5432",
}

username = config.get("user", "user")
password = config.get("password", "pass")
host = config.get("host", "host")
db_name = config.get("dbname", "db_name")


@contextmanager
def connection():
    """Function that provides a connection to the PostgreSQL database."""
    conn = None
    try:
        conn = connect(host=host, user=username, database=db_name, password=password)
        yield conn
        conn.commit()
    except DatabaseError as err:
        print(err)
        conn.rollback()
    finally:
        if conn:
            conn.close()
