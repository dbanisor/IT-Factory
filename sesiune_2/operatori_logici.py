x = True
y = False

print("x and y is", x and y)
print("x or y is", x or y)
print("not x is", not x)

# "or" va evalua fiecare operand si se va opri la primul care este adevarat --> 0 este fals, se opreste la 4
x = 0 or 4
print(x)

# "or" va evalua fiecare operand si se va opri la primul care este adevarat --> 7 este adevarat, se opreste la 7
y = 7 or 9
print(y)

z = 7 and 0
print(z) # --> 0 (daca nu a gasit nicio valoare falsa pana la ultima, o va da pe ultima, adica "0")

w = 7 and 5
print(w) # --> 5 (daca nu a gasit nicio valoare falsa pana la ultima, o va da pe ultima, adica "5")

r = 7 and 0 and 4
print(r) # --> 0 (daca a gasit o valoare falsa, o va da pe aceea, adica "0")
