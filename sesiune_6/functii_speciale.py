class Dog:
    species = "mammal"  # class attribute

    def __init__(self, age, name):  # instance attributes
        self.age = age
        self.name = name

    def __str__(self):  # se foloseste pt reprezentarea obiectului clasei sub forma de string.
        # Daca nu este definita o metoda __str__, atunci obiectul implementat va apela metoda __repr__.
        return f"Age: {self.age}, Name: {self.name}, Species: {self.species}"

    def __repr__(self): # aceasta se foloseste cand avem liste. Acestea nu vor fi apelate altfel
        return str(self)  # sau self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Dog):
            return False
        return self.age == other.age and self.name == other.name



d = Dog(2, "Rexy")
print(d)  # printeaza locatia din memorie a obiectului "d"

# d2 = Dog(4, "Puffy")
# l = [d, d2]
# print(l)
#
# d3 = Dog(4, "Puffy")
# print(d2==d3)
#
# print(d2 == 5)
