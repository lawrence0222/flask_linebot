import sqlite3

conn = sqlite3.connect("test1.db")
c = conn.cursor()
c.execute("SELECT * FROM PEOPLE ")
print(c.fetchall())