import sqlite3
from pprint import pprint


conn = sqlite3.connect("students.db")
cursor = conn.cursor()

sql_query = "UPDATE Grades SET grade = ? WHERE student_id = ? AND topic = ? AND GRADE = ?"
cursor.execute(sql_query, (10, 2, "Web Dev", 9))
conn.commit()
cursor.execute("SELECT * FROM Grades")
pprint(cursor.fetchall())