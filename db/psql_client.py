import psycopg2
import os

from dotenv import load_dotenv


class PostgresqlClient:


    def __init__(self) -> None:
        print("Connecting to database...")
        load_dotenv()
    
    def connect(self):
        
        dbname = os.getenv('DB_NAME')
        user = os.getenv('PSQL_USER')
        password = os.getenv('PSQL_PASSWORD')
        host =os.getenv('PSQL_HOST')     
        port = os.getenv('PSQL_PORT')

        print("--- Connecting to PostgreSQL ---")
        conn = psycopg2.connect(
            host = host,
            dbname = dbname,
            user =user,
            password = password,
            port = port)
        print("Connected successfully..")

        
        