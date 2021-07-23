import sqlite3

conn = sqlite3.connect("SQLite10_Update/store_transaction.db")

c = conn.cursor()

c.execute("SELECT *FROM purchases")

print(c.fetchall())
conn.commit()

c.execute("UPDATE purchases SET total_cost = 3.67 WHERE purchase_id = 54")
c.execute("SELECT *FROM purchases")
print(c.fetchall())
conn.commit()

conn.close()