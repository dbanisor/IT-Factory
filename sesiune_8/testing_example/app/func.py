'''
Sa se scrie o functie care primeste ca parametru un intreg si returneaza:
    * 35 daca nr este divizibil cu 3 si cu 5
    * 3 daca nr este divizibil cu 3
    * 5 daca nr este divizibil cu 5
'''

def is_div_3_5(n):
    if n % 3 == 0 and n % 5 == 0:
        return 35
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5

'''
Sa se scrie o functie care primeste ca parametru o lista si 
arunca o exceptie specifica daca lista contine si altceva decat inregi.
'''

class NotIntException(Exception):
    pass

def only_ints(lst):
    for elem in lst:
        if not isinstance(elem, int):
            raise NotIntException(f"{elem} is not an int.")

