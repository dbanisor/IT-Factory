'''
1. Sa se scrie un program care citeste 2 nr de la tastatura si afiseaza urmatoarele informatii:
    a. Daca primul numar este par
    b. Daca al doilea numar este impar
    c. Suma numerelor
    d. Catul numerelor daca al doilea este diferit de 0, altfel se afiseaza un mesaj in care se specifica ?Catul nu se poate realiza?
    e. Primul numar ridicat la puterea al doilea numar
    f. Care este numar mai mare
    g. Daca ambele numere sunt pozitive
    h. Daca ambele numere sunt negative
'''

a = int(input("Dati un nr a: "))
b = int(input("Dati un nr b: "))

# a. Daca primul numar este par.
if a % 2 == 0:
    print("a. primul nr este par")
else:
    print("a. ----")

# b. Daca al doilea numar este impar (fara sa folosim operatorii de comparatie)
if b % 2:
    print("al doilea este impar")
else:
    print("b. ----")

# c. Suma numerelor
print(f"Suma numerelor este {a + b}")

# d. Catul numerelor daca al doilea este diferit de 0, altfel se afiseaza un mesaj in care se specifica 'Catul nu se poate realiza'

if b: # asta inseamna 'daca b este diferit de 0'
    print(f"Catul dintre a/b este {a/b}")
else:
    print("Catul nu se poate realiza")

# e. Catul numerelor daca al doilea este diferit de 0, altfel se afiseaza un mesaj in care se specifica ?Catul nu se poate realiza?
print(f"a la puterea b este {a ** b}")

# f. Care este numar mai mare
print("a este mai mare") if a > b else print("b este mai mare")

# g. Daca ambele numere sunt pozitive

# h. Daca ambele numere sunt negative




