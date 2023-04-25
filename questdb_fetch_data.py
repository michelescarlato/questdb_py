import psycopg as pg
import time

# Connect to an existing QuestDB instance

conn_str = 'user=admin password=quest host=127.0.0.1 port=8812 dbname=qdb'
with pg.connect(conn_str, autocommit=True) as connection:
    # Open a cursor to perform database operations

    with connection.cursor() as cur:
        # Query the database and obtain data as Python objects.

        cur.execute('SELECT * FROM sensors;')
        records = cur.fetchall()
        for row in records:
            print(row)

# the connection is now closed
