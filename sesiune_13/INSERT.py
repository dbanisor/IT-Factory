import sqlite3
from pprint import pprint


conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO Students (name, email, age) VALUES ('Adam', 'adam@g.com', '28');")
cursor.execute("INSERT INTO Students (name, email, age) VALUES ('Eva', 'eva@g.com', '25');")
# conn.commit()
# cursor.execute("SELECT * FROM Students;")
pprint(cursor.fetchall())

# materia, nota, id-ul studentului
grades_values = [
    ("Web Dev", 8, 1),
    ("DB Dev", 10, 1),
    ("DB Dev", 6, 2),
    ("Front-End", 10, 2),
    ("Web Dev", 9, 2),
    ("Web Dev", 8, 2),
    ("Web Dev", 7, 1),
]

sq_query = "INSERT INTO Grades (topic, grade, student_id) VALUES (?,?,?)"
cursor.executemany(sq_query, grades_values)
conn.commit()
cursor.execute("SELECT * FROM Grades")
pprint(cursor.fetchall())