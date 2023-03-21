from math import pi
from datetime import datetime as dt

'''
1. Functie care sa calculeze si sa returneze suma a doua numere.
'''
# def sum_numbers(a, b):
#     return a + b
# print(sum_numbers(2, 3))
# print(sum_numbers(5, 7))

'''
2. Functie care sa returneze True daca un numar este par, False pentru impar.
'''
# def even_or_odd(num):
#     return num % 2 == 0
#
# print(even_or_odd(4))
# print(even_or_odd(7))

'''
3. Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu)
'''
# def nb_char_in_name(nume, prenume, nume_mijlociu):
#     return len(nume) + len(prenume) + len(nume_mijlociu)
# print(nb_char_in_name("Banisor", "Denise", "Ramona"))

'''
4. Functie care returneaza aria dreptunghiului.
'''
# def rectangle_area(length, width):
#     return length * width
# print(rectangle_area(10, 20))

'''
5. Functie care returneaza aria cercului.
'''
# def circle_area(radius):
#     return round(pi, 2) * (radius ** 2)
# print(circle_area(5))

'''
6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat si False daca nu gaseste.
'''
# def is_char_in_string(sentence, character):
#     return character in sentence
# print(is_char_in_string("Ana are mere.", "m"))
# print(is_char_in_string("Ana are mere.", "x"))

'''
7. Functie fara return, primeste un string si printeaza pe ecran:
- numarul de caractere lower case este x
- numarul de caractere upper case este y
'''
# def upper_and_lower(sentence):
#     upper_case = 0
#     lower_case = 0
#     for char in sentence:
#         if char.isupper():
#             upper_case += 1
#         else:
#             lower_case += 1
#     print(f"Numarul de caractere lower case este {lower_case}.")
#     print(f"Numarul de caractere upper case este {upper_case}.")
# upper_and_lower("AlaBaLapOrtOcALA")
# upper_and_lower("AlabalaportocalA")

'''
8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive.
'''
# def positive_numbers(lista_numere):
#     pozitive = []
#     for num in lista_numere:
#         if num > 0:
#             pozitive.append(num)
#     return pozitive
# print(positive_numbers([7, -4, 6, -1, 2, 3]))

'''
9. Functie care nu returneaza nimic. Primeste doua numere si PRINTEAZA:
- primul numar X este mai mare decat al doilea numar Y
- al doilea numar Y este mai mare decat primul numar X
- numerele sunt egale
'''
# def greater_number(a, b):
#     if a > b:
#         print(f"Primul numar {a} este mai mare decat al doilea numar {b}.")
#     elif a < b:
#         print(f"Al doilea numar {b} este mai mare decat primul numar {a}.")
#     else:
#         print("Numerele sunt egale.")
# greater_number(5, 9)
# greater_number(23, 9)
# greater_number(23, 23)

'''
10. Functie care primeste un numar si un set de numere.
- printeaza "am adaugat numarul nou in set" + returneaza True
- printeaza "nu am adaugat numarul in set. Acesta exista deja" + returneaza False
'''
# def add_num_to_set(a, numere: set):
# #  https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-parameters-that-you-pass-in
#     if a not in numere:
#         numere.add(a)
#         print("Am adaugat numarul nou in set.")
#         return True
#     else:
#         print("Nu am adaugat numarul in set. Acesta exista deja")
#         return False
# print(add_num_to_set(5, {1, 2, 3, 4}))
# print(add_num_to_set(2, {1, 2, 3, 4}))

'''
EXERCITII OPTIONALE
'''
'''
1. Functie care primeste o luna din an si returneaza cate zile are acea luna.
'''
# def month_nb_of_days(month):
#     days_31 = ["january", "march", "may", "july", "august", "october", "december"]
#     days_30 = ["april", "june", "september", "november"]
#     if month.lower() in days_31:
#         return f"{month.capitalize()}: 31 days"
#     elif month.lower() in days_30:
#         return f"{month.capitalize()}: 30 days"
#     else:
#         return f"{month.capitalize()}: 28 or 29 days"
# print(month_nb_of_days("February"))

'''
2. Functie calculator care sa returneze 4 valori. Suma, diferenta, inmultirea, impartirea a doua numere.
In final vei putea face:
a, b, c, d = calculator(10, 2)
- print("Suma: ", a)
- print("Diferenta: ", b)
- print("Inmultirea: ", c)
- print("Impartirea: ", d)
'''
# def calculator(a, b):
#     suma = a + b
#     diferenta = a - b
#     inmultirea = a * b
#     impartirea = a / b
#     print(f"Suma: {suma}, a")
#     print(f"Diferenta: {diferenta}, b")
#     print(f"Inmultirea: {inmultirea}, c")
#     print(f"Impartirea: {impartirea}, d")
#     return suma, diferenta, inmultirea, impartirea
# calculator(10, 2)
# a, b, c, d = calculator(10, 2)
# print(a, b, c, d)

'''
3. Functie care primeste o lista de cifre (adica doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra 
=> dict{
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
} 
'''
# def list_to_dict(elements):
#     dict = {}
#     for elem in elements:
#         how_many = elements.count(elem)
#         dict[elem] = how_many
#     return dict
# print(list_to_dict([1, 3, 1, 5, 9, 7, 7, 5, 5]))

'''
4. Functie care primeste 3 numere. Returneaza valoarea maxima dintre ele.
'''
# def max_num(a, b, c):
#     return max(a, b, c)
# print(max_num(1, 3, 2))

'''
5. Functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar.
Exemplu: daca dam numarul 3, suma va fi 6 (0+1+2+3)
'''
# def sum_all_smaller_nums(a):
#     total = 0
#     for i in range(a + 1):
#         total += i
#     return total
# print(sum_all_smaller_nums(3))

'''
EXERCITII BONUS
'''
'''
1. Funtie care primeste 2 liste de numere (numerele pot fi dublate). Returnati doar numerele comune.
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}
'''
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
#
# def find_intersection(lista_1, lista_2):
#     common_nb = set(lista_1).intersection(set(lista_2))
#     return common_nb
# print(find_intersection(list1, list2))

'''
2. Functie care sa aplice o reducere de pret.
Daca produsul costa 100 lei si aplicam reducere de 10%, pretul va fi de 90 lei.
Trateaza cazurile in care reducerea e invalida. De exemplu o reducere de 110% e invalida.
'''
# def discount(price, percentage):
#     if 0 < percentage < 100:
#         return f"Pretul cu discount este {price - (price * (percentage / 100))} lei."
#     else:
#         raise Exception("Discount invalid.")
#
# print(discount(100, 110))

'''
EXERCITII DE ECHIPA
'''
'''
1. Functie care sa afiseze data si ora curenta din Romania
(Bonus: afiseaza si data si ora curenta din China)
'''
# def ro_and_china_time():
#
#     now_time = dt.now()
#
#     ro_day = now_time.day
#     ro_month = now_time.month
#     ro_year = now_time.year
#     ro_hour = now_time.hour
#     ro_minute = now_time.minute
#
#     china_hour = ro_hour + 6
#     china_day = ro_day
#
#     if china_hour == 24:
#         china_hour = 00
#         china_day += 1
#     elif china_hour > 24:
#         china_hour -= 24
#         china_day += 1
#
#     print(f"Data si ora in RO sunt: {ro_day}-{ro_month}-{ro_year} {ro_hour}:{ro_minute}.\n"
#           f"Data si ora in China sunt: {china_day}-{ro_month}-{ro_year} {china_hour}:{ro_minute}.")
#
# ro_and_china_time()

'''
2. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la Craciun daca nu vrei sa ne zici cand e ziua ta :)
'''
# def days_until_bday():
#     birthday = dt(2023, 8, 7, 00, 00, 00)
#     days_remaining = (birthday - dt.now()).days
#     print(f"Pana la ziua mea mai sunt {days_remaining} zile.")
#
# days_until_bday()