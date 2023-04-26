import psycopg as pg
import time

# Connect to an existing QuestDB instance

conn_str = 'user=admin password=quest host=127.0.0.1 port=8812 dbname=qdb'
with pg.connect(conn_str, autocommit=True) as connection:
    # Open a cursor to perform database operations

    with connection.cursor() as cur:
        # Query the database and obtain data as Python objects.

        cur.execute('SELECT * FROM sensors_data WHERE timems BETWEEN \'2023-03-29T00:00:23.000000Z\' AND \'2023-04-25T00:00:23.500000Z\';')
        records = cur.fetchall()
        for row in records:
            print(row)

# the connection is now closed
