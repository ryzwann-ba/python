import sqlite3
cnx = sqlite3.Connection('ma_base.db')
createur_table = cnx.cursor()
createur_table.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     login TEXT,
     mdp text
)
""")
cnx.commit()

