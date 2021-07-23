import sqlite3 

conn = sqlite3.connect("./SQLite7_PrimaryKey/customer.db")

c = conn.cursor()

c.execute("""
SELECT rowid, *FROM customers
""")

items = c.fetchall()

conn.commit()

for item in items:
    print(item)

conn.close()
