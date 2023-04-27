import logging
import sys
import psycopg as pg
from datetime import datetime
import time
import socket
from mira_utils import read_conf,convert_seconds

log_name = str(datetime.now())
log_name = log_name.replace(" ","_")
hostname = str(socket.gethostname())
print(log_name)
logging.basicConfig(filename="logs/Fetch_data_"+hostname+"_"+str(log_name)+"_run.log", level=logging.INFO)

file_name = sys.argv[1]
url, user, table, dbname, password, port = read_conf.read_conf_fetch_data(file_name)
# start script temporizer
start = time.time()

# Connect to an existing QuestDB instance
conn_str = f'user={user} password={password} host={url} port={port} dbname={dbname}'
with pg.connect(conn_str, autocommit=True) as connection:
    # Open a cursor to perform database operations
    with connection.cursor() as cur:
        # Query the database and obtain data as Python objects.
        cur.execute(f'SELECT m001_abs_good FROM {table} WHERE timems BETWEEN \'2023-03-29T00:00:23.000000Z\' AND \'2023-04-25T00:00:23.500000Z\';')
        records = cur.fetchall()

# the connection is now closed

end = time.time()
elapsed_time = end - start
minutes = convert_seconds.convert_seconds(elapsed_time)
print("Total time elapsed:")
print(minutes)
logging.info("Total time elapsed (hh:mm:ss): "+str(minutes))