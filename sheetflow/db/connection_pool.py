from mysql.connector import pooling
from sheetflow.config import get_config

config = get_config()

dbconfig = {
    "host": config['DATABASE']['host'],
    "port": int(config['DATABASE']['port']),
    "user": config['DATABASE']['user'],
    "password": config['DATABASE']['password'],
    "database": config['DATABASE']['database']
}

pool = pooling.MySQLConnectionPool(
    pool_name="sheetflow_pool",
    pool_size=5,
    **dbconfig
)

def get_connection():
    return pool.get_connection()