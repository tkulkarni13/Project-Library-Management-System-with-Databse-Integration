import mysql.connector
from mysql.connector import Error
from password import my_password

# Connect to the MySQL database and return the connection object
def connect_database():
    # Database Connection Parameters
    db_name = "library_db"
    user = "root"
    password = my_password
    host = "localhost"

    try:
        # Attempting to establish a connection
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        print("Connected to MySQL database successfully")
        return conn
    except Error as e:
        # Handling any connections errors
        print(f"Error: {e}")
        return None