import sqlite3
from pprint import pprint


conn = sqlite3.connect("students.db")
cursor = conn.cursor()
sql_query = "DELETE FROM Grades WHERE topic = :topic AND student_id = :id;"  # acestea sunt cheile dintr-un dictionar de unde query-ul isi va lua datele
values_dict = {"id": 1, "topic": "Web Dev"}
cursor.execute(sql_query, values_dict)
conn.commit()
cursor.execute("SELECT * FROM Grades")
pprint(cursor.fetchall())
