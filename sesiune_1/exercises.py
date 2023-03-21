# 1. Sa se scrie un program care citeste date de la
# tastatura si afiseaza doar primere 3 caractere diferite de spatiu  primite.

# a = input("Text: ")
# a = a.replace(" ", "")
# print(a[:3])

# 2. Sa se scrie un program care citeste date de la
# # tastatura si afiseaza urmatoarele:
# a: nr de litere al textului introdus
# b: prima si ultima litera
# c: textul scris doar cu litere mari
# d: de cate ori apare prima litera
# e: cate cuvinte are textul

a = input("Text: ")
print(f"a. {len(a)}")
print(f"b. {a[0]} {a[-1]}")
print(f"c. {a.upper()}")
print(f"d. {a.count(a[0])}")
print(f"e. {a.count(' ') + 1}")