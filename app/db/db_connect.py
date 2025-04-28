import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    timeout = 10
    return pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db=os.getenv("MYSQLDATABASE"),  # use environment variable
        host=os.getenv("MYSQLHOST"),
        password=os.getenv("MYSQLPASSWORD"),
        read_timeout=timeout,
        port=int(os.getenv("MYSQLPORT")),
        user=os.getenv("MYSQLUSER"),
        write_timeout=timeout,
    )
