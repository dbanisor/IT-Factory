# 1. Lungime

name = "Dragos"
print(len(name))

# 2. Majuscule

name = "Dragos"
print(name.upper())

# 3. Minuscule

name = "DraGoS"
print(name.lower())

# 4. Numarare

name = "Anamaria"
print(name.count("a")) # numarul de aparitii al caracterului in string
print(name.count("char"))
print(name.count("g"))

# 5. Replace

name = "anamaria"
name = name.replace("a", "b") # toate aparitiile caracterului "a" au fost inlocuite cu "b"
print(name)

food = "pizza"
print(food.replace("zz", "t"))

name = "anamaria"
print(name.replace("a", "b", 3)) # putem sa limitam cate caractere sa inlocuiasca

# 6. Indexing

name = "John"
print(name.index("o")) # pozitia caracterului in string
print(name[0])
print(name[-1])
print(name[len(name)-1])

# 7. Slicing

b = "Hello world"
print(b[2:5]) # de la 2 la 5, fara 5
print(b[:5]) # de la inceput pana la 5, fara 5
print(b[2:]) # de la caracterul al doilea pana la final
print(b[-5:-2]) # indexare negativa


