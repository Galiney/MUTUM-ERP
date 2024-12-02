from dotenv import load_dotenv
import os, mysql.connector

def connect_db():
    load_dotenv()

    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        charset="utf8mb4",
        collation="utf8mb4_unicode_ci"  
    )