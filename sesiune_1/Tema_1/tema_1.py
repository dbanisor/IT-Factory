
''' 1. In cadrul unui comentariu, explica cu cuvintele tale ce este o variabila.'''

'''
 o variabila este un tip de date stocate sub forma de sir de caractere,
 numar intreg, numar cu zecimale, valoare adevarata sau falsa sau multime vida.
'''

''' 2. Declara si initializeaza cate o variabila din fiecare din urmatoarele tipuri de variabila:
- string '''
name = "John"
'''- int'''
age = 20
''' - float'''
height = 1.80
''' - bool'''
student = False

''' Observatie: Valorile vor fi alese de tine dupa preferinte.'''

''' 3. Utilizeaza functia type pentru a verifica daca au tipul de date asteptat.'''

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(student))

''' 4. Rotunjeste float ul folosind functia round() si salveaza aceasta
modificare in aceeasi variabila (suprascriere). Verifica tipul acesteia.'''

# height = round(height, 1)
# print(height)

''' 5. Foloseste print() si printeaza in consola 4 propozitii folosind cele 4 variabile.
Rezolva nepotrivirile de tip prin ce modalitate doresti.'''

# print(f"{name} are {age} ani, {height} m inaltime cu aproximatie. Este student? {student}")

''' 6. Citeste de la tastatura:
- numele
- prenumele
Afiseaza: "Numele complet are x caractere".'''

# last_name = input("What's your last name: ")
# first_name = input("What's your first name: ")
# print(f"Numele complet are {len(last_name + first_name)} caractere.")

''' 7. Citeste de la tastatura:
 - lungimea
 - latimea
Afiseaza: "Aria dreptunghiului este x".'''

# lungime = int(input("Lungime in cm: "))
# latime = int(input("Latime in cm: "))
# print(f"Aria dreptunghiului este {lungime * latime} cm.")

''' 8. Avand string-ul: "Coral is either the stupidest animal or the smartest rock":
- afiseaza de cate ori apare cuvantul "the"'''

# sentence = "Coral is either the stupidest animal or the smartest rock."
# print(sentence.count("the"))

''' 9. Acelasi string:
- inlocuieste "the" cu "THE"
- printeaza rezultatul'''

# new_sentence = sentence.replace("the", "THE")
# print(new_sentence)

''' 10. Acelasi string:
Foloseste un assert ca sa verifici daca acest string contine doar numere:'''

# assert not sentence.isdigit()

'''Exercitii optionale
1. Citeste de la tastatura un string de dimensiune impara.
afiseaza caracterul din mijloc'''

# propozitie = input("Scrie un cuvant de dimensiune impara: ")
# print(propozitie[int(len(propozitie) / 2)])

''' 2. Folosind o singura linie de cod:
- citeste un string de la tastatura (ex: "alabala portocala")
- salveaza fiecare cuvant intr-o variabila
- printeaza ambele variabile pentru verificare'''

# one, two, *_ = lista_cuvinte = input("Scrie o propozitie: ").split()
#
# for cuvant in lista_cuvinte:
#     print(cuvant)

'''Exercitii de grup
1. Exercitiu
- citeste un string de la tastatura (ex.: alabala portocala)
- salveaza primul caracter intr-o variabila
- capitalizeaza acest caracter peste tot, mai putin primul si ultimul caracter'''

# raspuns = input("Scrie un string: ")
# first_char = raspuns[0]
# last_char = raspuns[-1]
# new_raspuns = raspuns[1:-1].replace(first_char, first_char.upper())
# print(f"{first_char}{new_raspuns}{last_char}")