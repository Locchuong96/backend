import sqlite3 

conn = sqlite3.connect("./SQLite16_LimitResult/customer.db")

c = conn.cursor()

# c.execute("SELECT rowid, *FROM customers LIMIT 2")

c.execute("SELECT rowid, *FROM customers ORDER BY rowid DESC LIMIT 3")
items  = c.fetchall()

print(items)

conn.commit()

conn.close()