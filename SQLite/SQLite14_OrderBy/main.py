import sqlite3 

conn = sqlite3.connect("./SQLite14_OrderBy/customer.db")

c = conn.cursor()

# c.execute(""" 
# SELECT rowid, *FROM  customers ORDER BY last_name
# """)

c.execute("""
SELECT rowid, *FROM customers ORDER BY rowid DESC
""")

items  = c.fetchall()

print(items)

conn.commit()

conn.close()