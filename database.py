import mysql.connector

DB_NAME = "skill_match_lite"

# This function will create the database, but only after realizing that it initially doesn't exist.
def create_database():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

    cursor.close()
    conn.close()

# Now that the database exists, we are connecting to it.
def get_connection():
    
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=DB_NAME
    )

# In this function, we are creating the database tables, but after ensuring that they don't already exist.
def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            skills TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            required_skills TEXT NOT NULL
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()


# This function is calling the two functions for creating the database and tables. 
# In the main.py, we will just call this function, instead of calling two separate functions. 
# This is cleaner and more efficient. 

def setup_database():

    create_database()
    init_db()