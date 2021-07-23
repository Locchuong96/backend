import sqlite3

conn = sqlite3.connect("./SQLite12_Delete/customer.db")

# create a cursor
c = conn.cursor()
#select table
c.execute("""
SELECT rowid, * FROM customers
"""
)

conn.commit()

items = c.fetchall()
print(items)

input("Delete?")

c.execute("DELETE from customers WHERE rowid = 3")
conn.commit()

c.execute("""
SELECT rowid, * FROM customers
"""
)
items = c.fetchall()
print(items)

conn.close()