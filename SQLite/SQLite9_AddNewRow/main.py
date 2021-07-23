import sqlite3 

conn = sqlite3.connect("./SQLite9_AddNewRow/store_transaction.db")

c = conn.cursor()

c.execute(""" 
CREATE TABLE IF NOT EXISTS stores(
    store_id INTEGER  PRIMARY KEY,
    location TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS purchases(
    purchase_id INTEGER PRIMARY KEY,
    store_id INTEGER,
    total_cost FLOAT,
    FOREIGN KEY(store_id) REFERENCES stores(store_id)
)
""")

# add to stores table
c.execute("INSERT INTO stores VALUES (21,'Mineapolis,MN')")
c.execute("INSERT INTO stores VALUES (95,'Chicago IL')")
c.execute("INSERT INTO stores VALUES (64,'Iowa City, IA')")

# add to purchases table 
c.execute("INSERT INTO purchases VALUES (54, 21, 15.49)")
c.execute("INSERT INTO purchases VALUES (12, 64, 14.43)")
c.execute("INSERT INTO purchases VALUES (13, 64, 24.1)")
c.execute("INSERT INTO purchases VALUES (16, 95, 99.65)")

c.execute("SELECT * FROM purchases")

items = c.fetchall()

for item in items:
    print(item)

conn.commit()

conn.close()