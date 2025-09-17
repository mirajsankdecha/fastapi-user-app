import mysql.connector

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='user'
        )
        cursor = conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS user_info (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age VARCHAR(255) NOT NULL
        )"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        return conn
    except mysql.connector.Error as err:
        print("Error: ", err)
        return None


if __name__ == "__main__":
    conn = get_db_connection()
    if conn and conn.is_connected():
        print("DB is connected and table created")
        conn.close()
    else:
        print("DB is not connected")
