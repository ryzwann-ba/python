import sqlite3
conn = sqlite3.Connection('ma_base.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     login TEXT,
     mdp text
)
""")
conn.commit()
