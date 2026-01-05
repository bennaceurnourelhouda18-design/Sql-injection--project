import sqlite3

def login(username, password):
    conn = sqlite3.connect("security.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("[VULNERABLE QUERY]:", query)

    try:
        cursor.execute(query)
        result = cursor.fetchone()
    except Exception as e:
        print("SQL Error:", e)
        result = None

    conn.close()
    return result is not None





