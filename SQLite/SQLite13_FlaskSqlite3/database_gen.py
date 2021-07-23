import sqlite3 

conn = sqlite3.connect("./SQLite13_FlaskSqlite3/database.db")

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS User(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    score FLOAT
)
""")

conn.commit()

conn.close()