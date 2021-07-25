import sqlite3

conn = sqlite3.connect("./database.db")

c = conn.cursor()

c.execute("""
CREATE TABLE store(
    store_id INTEGER PRIMARY KEY,
    store_name TEXT,
    store_location TEXT
)
""")

c.execute("""
CREATE TABLE purchase(
    purchase_id INTEGER PRIMARY KEY,
    total FLOAT,
    store_id INTEGER,
    FOREIGN KEY (store_id) REFERENCES store(stores_id)
)
""")

conn.commit()
conn.close()