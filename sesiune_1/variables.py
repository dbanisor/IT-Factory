# variabila -> container din memorie pt a stoca valori

# 1. Creare variabile

x = 5
y = "Ionut"

print(x, y)

'''
2. Denumire variabile

Reguli:
    * numele variabilei trebuie sa inceapa cu litera sau _
    * numele nu poate sa inceapa cu numar
    * numele poate contine doar caractere alfanumerice si _ (0-9, a-z, A-Z, _)
    * numele sunt case sensitive (new_age, Age, AGE sunt 3 variabile diferite)
'''

# asa

myvar = "dina"
my_var = "dina"
_myvar = "dina"
myVar = "dina"
MYVAR = "dina"
myvar2 = "dina"

# nu asa

# 2myvar = "dina"
# my-var = "dina"
# my var = "dina"

# 3. Mai multe valori la mai multe variabile

x, y, z = 6, 7, 8
print(x, z, y)

# t = x
# x = y
# y = t

x, y = y, x
print(x, y)

# 4. O valoare la mai multe variabile

a = b = c = 10

print(a, b, c)