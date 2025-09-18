import mysql.connector
import json

# ✅ DB Connection
def establish_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="user"
    )

# ✅ Create new table for JSON method
def create_new_user_table():
    conn = establish_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS new_user_info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            age INT,
            gender VARCHAR(20),
            country VARCHAR(100)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# ✅ Old Method (insert into old table: user_info)
def create_info(name, age):
    try:
        conn = establish_connection()
        cursor = conn.cursor()
        query = "INSERT INTO user_info (first_name, age) VALUES (%s, %s)"
        cursor.execute(query, (name, age))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("❌ Error in create_info:", e)
        return False

# ✅ New Method (insert into new table: new_user_info)
def create_user(user_json):
    try:
        user = json.loads(user_json)  # parse JSON
        conn = establish_connection()
        cursor = conn.cursor()
        query = "INSERT INTO new_user_info (first_name, age, gender, country) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (user["first_name"], user["age"], user["gender"], user["country"]))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("❌ Error in create_user:", e)
        return False
    
