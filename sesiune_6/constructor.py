class Dog:
    species = "mammal" # class attribute -> acelasi pt toate obiectele din aceasta clasa
    age = 12
    name = "Rexy"


d = Dog()
print(d.name)

d2 = Dog()
d2.name = "Puffy" # name -> devine atribut de instanta

print(d.name, d2.name)

Dog.name = "Bruno"
print(d.name, d2.name)

'''
Atributele de clasa sunt in general folosite pt a crea constante in acea clasa.
'''

class Dog2:
    species = "mammal"  # class attribute

    def __init__(self, age, name):  # instance attributes
        self.age = age
        self.name = name

my_dog = Dog2(2, "Pufy")
print(my_dog.age)
print(my_dog.name)
print(my_dog.species)
# print(Dog2.name)  # --> incorect pt ca "name" este un atribut de instanta si poate fi accesat doar printr-un obiect al acestei clase.





