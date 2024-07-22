import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="7828",
            database="school"
        )
        if connection.is_connected():
            return connection            
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None