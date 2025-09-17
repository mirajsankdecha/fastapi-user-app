import mysql.connector

def create_info(name, age):
    try:
        user_dict = dict()
        user_dict['name'] = name
        user_dict['age'] = age

        # PUT THIS ENTRY IN DB
        conn = establish_connection()
        cursor = conn.cursor()
        insert_query = "INSERT INTO user_info (name, age) VALUES (%s, %s)"
        cursor.execute(insert_query, (user_dict['name'], user_dict['age']))
        conn.commit()
        cursor.close()
        conn.close()

        return True
    except Exception as e:
        print("Error in creating user:", e)
        return False

def create_user(user_dict):
    pass

def establish_connection():
    # create a connection to the database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='user'
    )
    return conn

