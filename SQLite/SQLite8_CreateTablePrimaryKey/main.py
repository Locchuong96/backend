import sqlite3

conn = sqlite3.connect("./SQLite8_CreateTablePrimaryKey/store_transactions.db")

c = conn.cursor()

#create stores table

c.execute("""
CREATE TABLE IF NOT EXISTS stores(
    store_id INTEGER PRIMARY KEY,
    location TEXT)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS purchases
(
    purchase_id INTEGER PRIMARY KEY,
    store_id INTEGER,
    total_cost  FLOAT,
    FOREIGN KEY(store_id) REFERENCES stores(store_id)
)
""")

conn.commit()

conn.close()

