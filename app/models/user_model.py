from app.db.db_connect import get_db_connection as get_connection

def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) UNIQUE,
                password VARCHAR(255)
            )
        """)
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        return True
    finally:
        cursor.close()
        conn.close()

def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor() 

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()
    return user
