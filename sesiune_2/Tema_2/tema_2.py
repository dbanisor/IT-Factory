import random

'''
1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
'''
# if else este un bloc de cod prin care daca o conditie este in deplinita se va face ceva, daca nu,
# se va face altceva (se va printa ceva, se va executa orice alta linie de cod data in interiorului blocului de cod.

'''
2. Verifica si afiseaza daca x este numar natural sau nu
'''

x = int(input("Dati un nr x: "))

if x > 0:
    print(f"{x} este numar natural")
else:
    print(f"{x} nu este numar natural")

'''
3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru.
'''

if x > 0:
    print("x este numar pozitiv")
elif x < 0:
    print("x este numar negativ")
elif x == 0:
    print("x este neutru")

'''
4. Verifica si afiseaza daca x este intre -2 si 13
'''

print("x este intre -2 si 13") if -2 < x < 13 else print("x nu este intre -2 si 13")

'''
5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
'''

y = int(input("Dati un nr y: "))

print("diferenta dintre x si y este mai mica de 5") if x - y < 5 else print("diferenta dintre x si y este mai mare sau egala cu 5")

'''
6. Verifica daca x NU este intre 5 si 27 - a se folosi 'not'
'''

print("x nu este intre 5 si 27") if x not in range(5, 27) else print("x este intre 5 si 27") # am presupus ca 5 si 27 nu sunt incluse

'''
7. x si y (int)
Verifica si afiseaza daca sunt egale, daca nu, afiseaza care din ele este mai mare.
'''

if x == y:
    print("x si y sunt egale")
elif x > y:
    print(f"x: {x} este mai mare decat y: {y}")
else:
    print(f"x: {x} nu este mai mare decat y: {y}")

'''
8. x, y, z - laturile unui triunghi.
Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
'''

z = int(input("Dati un nr z: "))

if x == y == z:
    print("Triunghiul este echilateral")
elif x == y != z or x == z != y or y == z != x:
    print("Triunghiul este isoscel")
else:
    print("Triunghiul este oarecare")

'''
9. Citeste o litera de la tastatura.
Verifica si afiseaza daca este vocala sau nu.
'''

litera = input("Dati o litera: ")

print(f"{litera} este o vocala") if litera in ['a', 'e', 'char', 'o', 'u'] else print(f"{litera} nu este o vocala")

'''
10. Transforma si printeaza notele din sistem romanesc in >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''

nota = int(input("Dati o nota in sistemul romanesc: "))
if nota in range(1, 11):
    if nota >= 9:
        print(f"Nota {nota} este nota A")
    elif nota >= 8:
        print(f"Nota {nota} este nota B")
    elif nota >= 7:
        print(f"Nota {nota} este nota C")
    elif nota >= 6:
        print(f"Nota {nota} este nota D")
    elif nota >= 4:
        print(f"Nota {nota} este nota E")
    else:
        print(f"Nota {nota} este nota F")
else:
    print(f"{nota} nu este o nota in sistemul romanesc")

'''
Exercitii optionale - grad de dificultate: Mediu spre greu - might need Google

1. Verifica daca x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre) 
'''

if len(str(x)) >= 4:
    print("x are minim 4 cifre")
else:
    print("x nu are minim 4 cifre")

'''
2. Verifica daca x are exact 6 cifre.
'''

if len(str(x)) == 6:
    print("x are exact 6 cifre")
else:
    print("x nu are 6 cifre")

'''
3. Verifica daca x este numar par sau impar (x e int).
'''

print(f"{x} este numar par") if not x % 2 else print(f"{x} este numar impar")

'''
4. x, y, z (int)
Afiseaza care este cel mai mare dintre ele?
'''

if x > y and x > z:
    print("x este cel mai mare numar.")
elif y > x and y > z:
    print("y este cel mai mare numar.")
else:
    print("z este cel mai mare numar.")

'''
5. x, y, z - reprezinta unghiurile unui triunghi.
Verifica si afiseaza daca triunghiul este valid. 
'''

unghiuri = [x, y, z]
print("Triunghiul este unul valid") if sum(unghiuri) == 180 else print("Triunghiul nu este unul valid.")

'''
6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
Citeste de la tastatura un int x
Afiseaza stringul fara ultimele x caractere
Exemplu: daca ai ales 7 => 'Coral is either the stupidest animal or the smarte'
'''

propozitie = "Coral is either the stupidest animal or the smartest rock"
numar = int(input("Cu cate caractere sa taiem fraza: "))

print(propozitie[0:-numar])

'''
7. Acelasi string. Declara un string nou care sa fie format din primele 5 caractere + ultimele 5.
'''

propozitie_noua = propozitie[:5] + propozitie[len(propozitie)-5:]
print(propozitie_noua)

'''
8. Acelasi string.
Salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock (hint: este o functie care te ajuta sa faci asta)
Folosind aceeasi variabila + sclicing, afiseaza tot stringul pana la acest cuvant
output: 'Coral is either the stupidest animal or the smartest'
'''

rock_position = propozitie.index("rock")
print(rock_position)

sliced_sentence = propozitie[:rock_position - 1]
print(sliced_sentence)

'''
Exercitii Bonus

11. Joc ghicit zarul
Cauta pe net si vezi cum se genereaza un numar random
Ne imaginam ca dai cu zarul si salvam acest numar in dice_roll
Ia numarul ghicit de la utilizator
Verifica si afiseaza daca utilizatorul a ghicit
Vei avea 3 optiuni
- Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
- Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
- Ai ghicit. Felicitari! Ai ales x si zarul a fost y.
'''

dice_roll = random.randint(1, 6)
print(f"Zarul este {dice_roll}.")

guess = int(input("Ghiceste numarul de la zar (1 - 6): "))

if guess in range(1, 7):
    if guess < dice_roll:
        print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {guess} dar a fost {dice_roll}.")
    elif guess > dice_roll:
        print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {guess} dar a fost {dice_roll}.")
    else:
        print(f"Ai ghicit. Felicitari! Ai ales {guess} si zarul a fost {dice_roll}.")
else:
    pass

'''
Exercitii de echipa

1. Citeste de la tastatura un string
Verifica daca primul si ultimul caracter sunt la fel. Se va folosi un assert
'''

word = input("Scrie un string: ").lower()

assert word[0] == word[-1]

'''
2. Avand stringul '0123456789'
- Afiseaza doar numerele pare
- Afiseaza doar numerele impare
(hint: foloseste slicing, controleaza din pas)
'''

cuvant = "0123456789"
nr_pare = []
nr_impare = []

for i in range(len(cuvant)):
    if int(cuvant[i]) % 2 == 0:
        nr_pare.append(i)
    else:
        nr_impare.append(i)
print(nr_pare)
print(nr_impare)

