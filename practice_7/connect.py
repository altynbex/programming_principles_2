import psycopg2
from config import *

def create_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        host=DB_HOST,
        password=DB_PASSWORD
    )