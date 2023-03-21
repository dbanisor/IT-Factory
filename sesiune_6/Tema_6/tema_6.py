from math import pi
from datetime import datetime
import pandas as pd

'''
1. Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
- descrie_cerc() - va PRINTA culoarea si raza
- aria() - va RETURNA aria
- diametru()
- circumferinta()
'''
# class Cerc:
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descrie_cerc(self):
#         print(f"culoare: {self.culoare}, raza: {self.raza}")
#
#     def aria(self):
#         return pi * (self.raza ** 2)
#
#     def diametru(self):
#         return self.raza * 2
#
#     def circumferinta(self):
#         return 2 * pi * self.raza
#
# cerc = Cerc(5, "red")
# cerc.descrie_cerc()
# print(cerc.diametru())
# print(cerc.aria())
# print(cerc.circumferinta())

'''
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
- descrie()
- aria()
- perimetrul()
- schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
Ea va lua ca si parametru o noua culoare si va suprascrie atributul self.culoare. Poti verifica schimbarea culorii prin apelarea metodei descrie().
'''
# class Dreptunghi:
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie(self):
#         print(f"lungime: {self.lungime}, latime: {self.latime}, culoare: {self.culoare}.")
#
#     def aria(self):
#         return self.latime * self.lungime
#
#     def perimetrul(self):
#         return self.latime * 2 + self.lungime * 2
#
#     def schimba_culoarea(self, noua_culoare):
#         self.culoare = noua_culoare
#
# dreptunghi = Dreptunghi(10, 5, "blue")
# dreptunghi.descrie()
# print(dreptunghi.aria())
# print(dreptunghi.perimetrul())
# dreptunghi.schimba_culoarea("red")
# dreptunghi.descrie()

'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pentru toate atributele
Metode:
- descrie()
- nume_complet()
- salariu_lunar()
- salariu_anual()
- marire_salariu(procent)
'''


# class Angajat:
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(f"nume: {self.nume}, prenume: {self.prenume}, salariu: {self.salariu}.")
#
#     def nume_complet(self):
#         return f"Numele complet: {self.nume} {self.prenume}."
#
#     def salariu_lunar(self):
#         return f"$ {self.salariu}"
#
#     def salariu_anual(self):
#         return f"$ {self.salariu * 12}"
#
#     def marire_salariu(self, procent):  # fara modificarea salariului actual
#         return f"$ {(procent * self.salariu) / 100 + self.salariu}"
#
#
# angajat = Angajat("Doe", "John", 2400)
# angajat.descrie()
# print(angajat.nume_complet())
# print(angajat.salariu_lunar())
# print(angajat.salariu_anual())
# print(angajat.marire_salariu(50))

'''
4. Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
- afisare_sold() - Titularul x are in contul y suma de n lei
- debitare_cont(suma)
- creditare_cont(suma)
'''
# class Cont:
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = int(sold)
#
#     def afisare_sold(self):
#         print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.")
#
#     def debitare_cont(self, suma):
#         self.sold -= suma
#
#     def creditare_cont(self, suma):
#         self.sold += suma
#
# cont = Cont("RO45INGB00009999", "John Doe", "4000")
# cont.afisare_sold()
# cont.debitare_cont(700)
# cont.afisare_sold()
# cont.creditare_cont(300)
# cont.afisare_sold()

'''
EXERCITII OPTIONALE
'''
'''
1. Clasa Factura
Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
- schimba_cantitatea(cantitate)
- schimba_pretul(pret)
- schimba_nume_produs(nume)
- genereaza_factura() - va printa tabelar daca reusiti

Factura seria x numar y
Data: genereaza automat data de azi
Produs | cantitate | pret bucata | Total
Telefon | 7        | 700         | 49000  
'''
# class Factura:
#     serie = "FO"
#
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate = cantitate
#
#     def schimba_pretul(self, pret):
#         self.pret_buc = pret
#
#     def schimba_nume_produs(self, nume):
#         self.nume_produs = nume
#
#     def genereaza_factura(self):
#         data = [{"Nume produs": self.nume_produs,
#                  "Cantitate": self.cantitate,
#                  "Pret bucata": self.pret_buc,
#                  "Total": (self.cantitate * self.pret_buc)}]
#         df = pd.DataFrame(data)
#         print(f"Factura seria {self.serie} numar {self.numar}\n"
#               f"Data: {datetime.today()}\n"
#               f"{df}")
#
# factura = Factura(24, "Telefon", 7, 700)
# factura.genereaza_factura()

'''
Clasa Masina
Atribute: marca, model, viteza_maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alege tu 5-7 culori
Marca = alege tu - fabrica produce o singura marca, dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
descrie() - se vor printa toate atributele, in afara de culori_disponibile
- inmatriculare() - va schimba atributul inmatriculata in True
- vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de
culori disponibile, altfel afisati o eroare
- accelereaza(viteza) - se va accelera la o anumita viteza, daca viteza e negativa-eroare,
daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
- franeaza() - masina se va opri si va avea viteza 0
'''
# class Masina:
#     culori_disponibile = {"red", "green", "blue", "white", "black"}
#     viteza_actuala = 0
#     culoare = "grey"
#     marca = "Nissan"
#     inmatriculata = False
#
#     def __init__(self, model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#
#     def descrie(self):
#         print(f"Marca: {self.marca}, Model: {self.model}, Culoare: {self.culoare}, Viteza actuala: {self.viteza_actuala}, Viteza maxima: {self.viteza_maxima}, Inmatriculata: {self.inmatriculata}.")
#
#     def inmatriculare(self):
#         self.inmatriculata = True
#
#     def vopseste(self, culoare):
#         if culoare in self.culori_disponibile:
#             self.culoare = culoare
#         else:
#             raise "Culoarea nu este disponibila."
#
#     def accelereaza(self, viteza):
#         if viteza <= 0:
#             raise "Ar trebui sa accelerezi..."
#         elif viteza > self.viteza_maxima:
#             self.viteza_actuala = self.viteza_maxima
#         else:
#             self.viteza_actuala += viteza
#
#     def franeaza(self):
#         self.viteza_actuala = 0
#
# masina = Masina("Micra", 120)
# masina.descrie()
# masina.vopseste("red")
# masina.descrie()
# masina.accelereaza(50)
# masina.descrie()
# masina.franeaza()
# masina.descrie()

'''
EXERCITII DE ECHIPA
'''

'''
1.Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor
Metode:
- adauga_task(nume, descriere) - se va adauga in dict
- finalizeaza_task(nume) - se va sterge din dict
- afiseaza_todo_list() - doar cheile
- afiseaza_detalii_suplimentare(nume_task) - in functie de numele taskului, printam detalii suplimentare.
    - Daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa-l adauge.
    - Daca acesta raspunde nu - la revedere
    - Daca raspunde da - ii cerem detalii task si salvam nume+detalii in dict
'''
class ToDoList:
    todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
        print(f"Task-ul {nume} a fost adaugat.")

    def finalizeaza_task(self, nume):
        self.todo.pop(nume)

    def afiseaza_todo_list(self):
        print(list(self.todo.keys()))

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task not in self.todo:
            yn_answer = input("Nu este in To Do List. Vrei sa il adaugi? 'y' sau 'n': ")
            if yn_answer == "n":
                print("Ok bye")
            elif yn_answer == "y":
                details_answer = input("Scrie detaliile suplimentare pe care vrei sa le adaugi la acest task: ")
                self.adauga_task(nume_task, details_answer)
                self.afiseaza_todo_list()
                print(list(self.todo.values()))
            else:
                raise "Raspuns invalid."


todolist = ToDoList()
todolist.adauga_task("facut tema", "revizuit lectia si rezolvat tema")
todolist.adauga_task("cumparaturi", "de cumparat legume si fructe")
todolist.afiseaza_todo_list()
todolist.finalizeaza_task("cumparaturi")
todolist.afiseaza_todo_list()
todolist.afiseaza_detalii_suplimentare("cumparaturi")
