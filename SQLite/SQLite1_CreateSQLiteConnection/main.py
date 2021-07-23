import sqlite3
# Make database in memory 
conn = sqlite3.connect(':memory:')
# Create a connection
conn = sqlite3.connect('customer.db')