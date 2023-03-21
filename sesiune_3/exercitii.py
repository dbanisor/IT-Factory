# 1. Sa se scrie un program care citeste un text de la tastatura si afiseaza o teren cu fiecare caracter in ordinea inversa a aparitiei in text

# text = input("Dati un text: ")
# text = text[::-1]
# l = list(text)
# print(l)

# 2. Fie seturile s1 si s2

set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}

# a. sa se afiseze toate elementele care apar in s1 si nu apar in s2
print(set1.difference(set2))
print(set1 - set2)

# b. --||-- (sa se afiseze toate elementele) care apar in ambele seturi
print(set1.intersection(set2))
print(set1 & set2)

# c. --||-- care nu sunt comune
print(set1.symmetric_difference(set2))
print(set1 ^ set2)