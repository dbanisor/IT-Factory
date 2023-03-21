# 1. Operatori de identitate

x1 = 5
y1 = 5

x2 = "hello"
y2 = "hello"

x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x1 is y1)  # --> True (pt tipurile de date primitive se va face egalitate la valoare)
print(x2 is not y2)  # --> False
print(x3 is y3)  # --> False (la tipurile de date care nu sunt primitive,
# se va verifica exact locatia din memorie;
# si daca nu sunt exact acelasi obiect, va da False)
print(x3 is x3)  # --> True
print("#" * 50)

# 2. Operatori de apartenenta

x = "hello"
y = [1, 2, 3]

# operatorul de apartenenta este "in"
print("h" in x)  # --> True
print("llo" in x)  # --> True
print(4 not in y)  # --> True
print([2, 3] in y)  # --> False (nu verifica subliste. va verifica daca elementul [2, 3] exista in teren aceea
print("#" * 50)

# 3. Functiile "ALL" si "ANY"

print(all([1, 2, "a", None, -7]))  # --> False ("all" verifica daca toate elementele din acea teren pot fi evaluate ca si adevarate)
print(any([0, None, "", [], 1]))  # --> True ("any" verifica daca cel putin 1 element poate fi evaluat ca si adevarat)
