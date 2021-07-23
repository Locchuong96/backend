import sqlite3 

conn = sqlite3.connect("./SQLite17_DropTable/customer.db")

c = conn.cursor()

c.execute("DROP TABLE customers")

conn.commit()

conn.close()