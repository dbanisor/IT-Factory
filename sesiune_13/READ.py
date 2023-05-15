import sqlite3
from pprint import pprint


conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Students;")
pprint(cursor.fetchall())
pprint(cursor.fetchone())
cursor.execute("SELECT * FROM Grades")
pprint(cursor.fetchmany(4))
pprint(cursor.fetchmany(3))

cursor.execute("SELECT topic,grade FROM Grades")
pprint(cursor.fetchall())

cursor.execute("SELECT * FROM Grades WHERE topic = ?",("Web Dev",))
pprint(cursor.fetchall())

