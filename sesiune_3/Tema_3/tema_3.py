import random

'''
Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
Indirect vei exersa si operatorii in cadrul conditiilor ramurilor din if.
X poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte.
X este un int.
'''

'''
1. Declara o teren de note_muzicale in care sa pui do re mi etc pana la do.
- afiseaz-o
- inverseaza ordinea folosind slicing si suprascrie aceasta teren
- printeaza varianta actuala (inversata)
- pe aceasta teren aplica o metoda care banuiesti ca face acelasi lucru, adica sa inverseze ordinea.
Nu trebuie sa o suprascrii in acest caz, deoarece metoda va face asta automat
- printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
'''

# note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# print(note_muzicale)
#
# reverse_note_muzicale = note_muzicale[::-1]
# print(reverse_note_muzicale)
# reverse_note_muzicale.reverse()
# print(reverse_note_muzicale)

'''
2. De cate ori apare "do"?
'''
# print(note_muzicale.count("do"))

'''
3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
Gaseste 2 variante ca se le unesti intr-o singura teren
'''
# l1 = [3, 1, 0, 2]
# l2 = [6, 5, 4]
#
# l3 = l1 + l2
# print(l3)
#
# l1.extend(l2)
# print(l1)

'''
4. Sorteaza si afiseaza teren generata la exercitiul anterior
Sterge numarul 0 folosind o functie
Afiseaza iar teren
'''
# l3.sort()
# print(l3)
#
# l3.remove(0)
# print(l3)

'''
5. Folosind un if, verifica teren generata la exercitiul 3 si afiseaza:
- teren este goala
- teren nu este goala
'''
# if l3:
#     print("teren nu este goala")
# else:
#     print("teren este goala")

'''
6. Foloseste o functie care sa stearga teren de la exercitiul 3
'''
# l3.clear()
# print(l3)

'''
7. Copy paste la exercitiul 5. Verifica inca o data.
Acum ar trebui sa se afiseze ca teren este goala.
'''
# if l3:
#     print("teren nu este goala")
# else:
#     print("teren este goala")

'''
8. Avand dictionarul dict1 = {"Ana": 8, "Gigel": 10, "Dorel": 5}
Foloseste o functie ca sa afisezi Elevii (cheile)
'''
# dict1 = {"Ana": 8, "Gigel": 10, "Dorel": 5}
#
# print(list(dict1.keys()))

'''
9. Printeaza cei 3 elevi si notele lor
Ex. "Ana a luat nota {x}"
Doar nota o vei lua folosindu-te de cheie
'''
# for elev in dict1:
#     print(f"{elev} a luat nota {dict1[elev]}")

'''
10. Dorel a facut contestatie si a primit 6.
- modifica nota lui Dorel in 6
- printeaza nota dupa modificare
'''
# dict1["Dorel"] = 6
# print(f"Dorel a luat nota {dict1['Dorel']}")

'''
11. Gigel se transfera din clasa
- cauta o functie care sa il stearga
- vine un coleg nou. Adauga Ionica, cu nota 9
- printeaza noii elevi
'''
# dict1.pop('Gigel')
#
# dict1['Ionica'] = 9
# print(dict1)

'''
EXERCITII OPTIONALE
'''

'''
1. Ne imaginam o echipa de fotbal pe teren sintetic.
3 schimbari maxime admise

- declara o Lista cu 5 jucatori
- schimbari_efectuate = te joci tu cu valori diferite
- schimbari_max = 3

Daca jucatorul X este in teren si mai avem schimbari la dispozitie:
- efectueaza schimbarea
- sterge jucatorul scos din teren
- adauga jucatorul intrat
- afiseaza a intrat X, a iesit Y, mai ai Z schimbari

Daca jucatorul nu este in teren:
- afiseaza "nu se poate efectua schimbarea deoarece jucatorul X nu e in teren"
- afiseaza "mai ai Z schimbari"

Testeaza codul cu diferite valori
'''

teren = ["Player1", "Player2", "Player3", "Player4", "Player5"]
all_players = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7", "Player8"]

schimbari_efectuate = 0
schimbari_max = 3


### Cauta random in lista cu toti jucatorii un jucator pe care sa il adauge in teren
# dar care sa nu fie cel ales mai sus si sa nu se regaseasca deja pe teren.
def pick_another_player(lst, other_lst, exception):
    while True:
        choice = random.choice(lst)
        if choice != exception and choice not in other_lst:
            return choice


while schimbari_efectuate < schimbari_max:
    ### Alege random un jucator din lista cu toti jucatorii, "all_players" dar nu il va sterge din lista (este cel care va iesi din teren).
    player = random.choice(all_players)
    ### apeleaza functia de mai sus (alege jucatorul care va intra in teren)
    player_to_field = pick_another_player(all_players, teren, player)

    if player in teren:
        schimbari_efectuate += 1
        # Afla indexul jucatorului ales in lista "teren" si apoi il sterge din aceasta lista
        teren.remove(player)
        # Adauga in teren jucatorul ales prin functia pick_another_player
        teren.append(player_to_field)
        print(f"A intrat {player_to_field}, a iesit {player}, mai ai {schimbari_max - schimbari_efectuate} schimbari.")

    else:
        print(f"Nu se poate efectua schimbarea deoarece jucatorul {player} nu e in teren.")
        print(f"Mai ai {schimbari_max - schimbari_efectuate} schimbari")

'''
Stiu ca "m-am complicat" e putin spus dar in timp ce scriam imi tot veneau daca... daca... in minte 
si am incercat sa elimin orice ar putea sa mearga gresit. Oricum, nu le-am eliminat pe toate...
'''





