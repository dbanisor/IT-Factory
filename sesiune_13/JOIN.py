import sqlite3
from pprint import pprint


conn = sqlite3.connect("students.db")
cursor = conn.cursor()

sql_query = "SELECT * FROM Students s JOIN Grades g ON s.id = g.student_id WHERE s.name = 'Eva'"
cursor.execute(sql_query)
pprint(cursor.fetchall())

sql_query = "SELECT s.name, g.grade, g.topic FROM Students s JOIN Grades g ON s.id = g.student_id WHERE s.name = 'Eva'"
cursor.execute(sql_query)
pprint(cursor.fetchall())