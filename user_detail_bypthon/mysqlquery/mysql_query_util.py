import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pymysql

load_dotenv()


DEPARTMENT_TABLE = os.getenv("MYSQL_DEPARTMENT_TABLE")

#DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"

# def get_client():

#     try:
#         print("Connecting to MongoDB...")
#         client = create_engine(DATABASE_URL)
#         print("Connected to MongoDB!")
#         return client
#     except Exception as e:
#         print("Unexpected error",e)

def get_connection():
    """Create and return a MySQL connection."""
    connection = pymysql.connect(
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSQL_PASSWORD"),
        host = os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT", 3306)),
        db = os.getenv("MYSQL_DB"),       
        cursorclass=pymysql.cursors.DictCursor  # returns results as dicts
    )
    return connection   
# here we can based on requirement we can frame different dao metod.here we want all record
def get_all_department():
    connection=get_connection()
    table_name=DEPARTMENT_TABLE
    """Fetch all rows from a given table (like MongoDB's get_collection)."""
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()
    return result

def save_department(department_id, department_name, department_code,department_address):
    connection = get_connection()
    table_name = DEPARTMENT_TABLE
    """Insert a new department record into the department table."""
    try:
        with connection.cursor() as cursor:
            sql =  f"INSERT INTO {table_name} (department_id,department_address, department_code, department_name) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (department_id,department_address, department_code, department_name))
            connection.commit()  
            
    except Exception as e:
        print("Error inserting department record:", e)
        connection.rollback()  # rollback in case of error
    finally:
        connection.close()


# conn = get_connection()
# departments = get_all_department()
# for dept in departments:
#         print(dept)