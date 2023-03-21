import random
'''
1. Avand lista:
masini = ["Audi", "Volvo", "BMW", "Mercedes", "Aston Martin", "Lastun", "Fiat", "Trabant", "Opel"]
foloseste un for ca sa iterezi prin toata lista si sa afisezi:
- "Masina mea preferata este x."
- Fa acelasi lucru cu un for each
- Fa acelasi lucru cu un while
'''

# masini = ["Audi", "Volvo", "BMW", "Mercedes", "Aston Martin", "Lastun", "Fiat", "Trabant", "Opel"]

# for i in range(len(masini)):
#     print(f" Masina mea preferata este {masini[i]}.")
#
# for car in masini:
#     print(f"Masina mea preferata este {car}.")
#
# index = 0
# while index < len(masini):
#     print(f" Masina mea preferata este {masini[index]}.")
#     index += 1

'''
2. Aceeasi lista: foloseste un for else
In for:
- modifica elementele din lista astfel incat sa fie scrise cu majuscule, exceptand primul si ultimul
In else:
- printeaza lista
'''

# for index, car in enumerate(masini):
#     masini[index] = masini[index][0].lower() + masini[index][1:-1].upper() + masini[index][-1].lower()
# else:
#     print(masini)

'''
3. Aceeasi lista: Vine un cumparator care doreste sa cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasa de tine.
Daca masina e Mercedes:
- printeaza "am gasit masina dorita de dvs."
- iesi din ciclu folosind un cuvant cheie care face acest lucru
Altfel:
- printeaza "Am gasit maxina X. Mai cautam."
'''

# for car in masini:
#     if car == "Mercedes":
#         print("Am gasit masina dorita de dvs.")
#         break
#     else:
#         print(f"Am gasit maxina {car}. Mai cautam.")

'''
4. Aceeasi lista: Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
Daca masina e Trabant sau Lastun:
- foloseste un cuvant cheie care as dea skip la ce urmeaza (nu trebuie else).
- printeaza "s-ar putea sa va placa masina x."
'''

# for car in masini:
#     if car == "Trabant" or car == "Lastun":
#         continue
#     print(f"s-ar putea sa va placa masina {car}.")

'''
5. Modernizeaza parcul de masini.
- creeaza o lista goala, masini_vechi
- itereaza prin masini
- cand gasesti Lastun sau Trabant:
    - salveaza aceste masini in masini_vechi
    - suprascrie-le cu Tesla (in lista initiala de masini)
- printeaza Modele vechi: x
- Modele noi: x
'''

# masini_vechi = []
#
# for index, car in enumerate(masini):
#     if car == "Trabant" or car == "Lastun":
#         masini_vechi.append(car)
#         masini[index] = "Tesla"
# print(masini_vechi)
# print(masini)

'''
6. Avand dict:
pret_masini = {
"Dacia": 6800,
"Lastun": 500,
"Opel": 1100,
"Audi": 19000,
"BMW": 23000
}
Vine un client cu un buget de 15000 euro. 
- printeaza toate masinile care se incadreaza in acest buget
- itereaza prin dict.items() si acceseaza masina si pretul
- printeaza "Pentru un buget de sub 15000 euro puteti alege masina xLastun
- Itereaza prin lista
'''

# pret_masini = {
# "Dacia": 6800,
# "Lastun": 500,
# "Opel": 1100,
# "Audi": 19000,
# "BMW": 23000
# }
# buget = 15000
#
# for key, value in pret_masini.items():
#     if value <= buget:
#         print(f"Pentru un buget de sub 15000 euro puteti alege masina {key}.")
#         print(f"{key}: {value} euro")

'''
7. Avand lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
- itereaza prin ea
- afiseaza de cate ori apare 3 (nu ai voie sa folosesti count)
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# count_three = 0
#
# for num in numere:
#     if num == 3:
#         count_three += 1
# print(count_three)

'''
8. Aceeasi lista:
- itereaza prin ea
- calculeaza si afiseaza suma numerelor (nu ai voie sa folosesti sum).
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# sum = 0
# for num in numere:
#     sum += num
# print(sum)

'''
9. Aceeasi lista:
- itereaza prin ea
- afiseaza cel mai mare numar (nu ai voie sa folosesti max).
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# max = 0
# for num in numere:
#     if num > max:
#         max = num
# print(max)

'''
10. Aceeasi lista:
- itereaza prin ea
- daca numarul e pozitiv, inlocuieste-l cu valoarea lui negativa (ex.: daca e 3, sa devina -3)
- afiseaza noua lista
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# for index, num in enumerate(numere):
#     if num > 0:
#         numere[index] = num * -1
# print(numere)

'''
EXERCITII OPTIONALE
'''
'''
1. 
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin lista alte_numere
Populeaza corect celelalte liste
Afiseaza cele 4 liste la final
'''
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
#
# for num in alte_numere:
#     if num > 0 and num % 2 == 0:
#         numere_pare.append(num)
#         numere_pozitive.append(num)
#     elif num > 0 and num % 2 != 0:
#         numere_impare.append(num)
#         numere_pozitive.append(num)
#     elif num < 0 and num % 2 == 0:
#         numere_pare.append(num)
#         numere_negative.append(num)
#     else:
#         numere_impare.append(num)
#         numere_negative.append(num)
#
# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)

'''
2. Aceeasi lista:
Ordoneaza crescator lista fara sa folosesti sort.
'''
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
# are_sorted = "yes"
# l = 1
# index = 0
#
# while l < len(alte_numere):
#     if alte_numere[l] < alte_numere[l - 1]:
#         are_sorted = "no"
#         for i in range(len(alte_numere)):
#             while index < len(alte_numere) - 1:
#                 if alte_numere[index] > alte_numere[index + 1]:
#                     alte_numere[index], alte_numere[index + 1] = alte_numere[index + 1], alte_numere[index]
#                 index += 1
#             else:
#                 index = 0
#                 l = 0
#                 break
#     l += 1
# print(alte_numere)
'''
3. Ghicitoare de numar:
numar_secret = Generati un numar random intre 1 si 30
numar_ghicit = None
Folosind un while
- user alege un numar
- programul ii spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitari! Ai ghicit!
'''

# numar_secret = random.randint(1, 31)
# numar_ghicit = None
# print(numar_secret)
#
# while numar_ghicit != numar_secret:
#     numar_ghicit = int(input("Alege un numar intre 1 - 30: "))
#     if numar_ghicit > numar_secret:
#         print("Nr secret e mai mic.")
#     elif numar_ghicit < numar_secret:
#         print("Nr secret e mai mare.")
#     else:
#         print("Felicitari! Ai ghicit!")

'''
EXERCITII DE ECHIPA
'''
'''
1. Alege un numar de la tastatura, ex. 7
Scrie un program care sa genereze in consola urmatoarea piramida
1
22
333
4444
55555
666666
7777777
'''

# numar = int(input("Alege un numar: "))
#
# for i in range(numar):
#     print(str(i + 1) * (i + 1))

'''
2. tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Itereaza prin lista 2d 
Printeaza "Cifra curenta este x"
(hint: nested for - adica for in for)
'''

# tastatura_telefon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]
#
# for i in tastatura_telefon:
#     for j in i:
#         print(f"Cifra curenta este {j}.")