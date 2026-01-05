import sqlite3

def login(username, password):
    conn = sqlite3.connect("security.db")
    cursor = conn.cursor()

    print("[SECURE QUERY]: username=?, password=?")

    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    result = cursor.fetchone()
    conn.close()
    return result is not None



