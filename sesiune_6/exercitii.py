# 1. Sa se creeze o clasa student cu atributele: nume, universitate, an (toate la constructor).
# 2. Sa se creeze functiile specifice astfel incat la printarea unui student se afiseaza toate atributele acestuia.
# 3. Fie lista de studenti students = [
#         Student(name="Alex", university="Babes", year=3),
#         Student(name="Cristina", university="Yale", year=4),
#         Student(name="Meredith", university="Chicago", year=3),
#         Student(name="George", university="Harvard", year=1),
#         Student(name="Mark", university="NYU", year=4),
#       Student(name="Owen", university="NYU", year=4),
#       Student(name="Derek", university="Columbia", year=4)
#     ]
# a) sa se creeze clasa StudentsDB in care sa se adauge ca si atribut de clasa, lista de studenti
# b) sa se creeze o functie care primeste ca parametru numele unui student si verifica daca acel student este inregistrat la vreo universitate
# c) sa se creeze o functie care adauga un nou student in lista de studenti

class Student:
    def __init__(self, name, university, year):
        self.name = name
        self.university = university
        self.year = year

    def __str__(self):
        return f"Name: {self.name}, University: {self.university}, Year: {self.year}"

    def __repr__(self):
        return str(self)


new_student = Student("John", "UCLA", "2016")
print(new_student)


class StudentsDB:
    students = [
        Student(name="Alex", university="Babes", year=3),
        Student(name="Cristina", university="Yale", year=4),
        Student(name="Meredith", university="Chicago", year=3),
        Student(name="George", university="Harvard", year=1),
        Student(name="Mark", university="NYU", year=4),
        Student(name="Owen", university="NYU", year=4),
        Student(name="Derek", university="Columbia", year=4)
    ]

    def check_enrolled_student(self, name):
        for student in self.students:
            if name == student.name and student.university:
                return True
        return False

    def add_student(self, student):
        self.students.append(student)

db = StudentsDB()
print(db.check_enrolled_student("Mark"))

print(db.add_student(new_student))
print(db.students)