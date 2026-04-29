import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="phonebook_db",
        user="altynbex",
        password="7539",
        host="localhost",
        port="5432"
    )