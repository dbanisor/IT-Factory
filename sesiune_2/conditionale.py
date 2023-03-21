# 1. "if"

a = 33
b = 200

if a < b:
    print("a este mai mic ca b")

if b:
    print("b nu este fals")

if a == 0:
    print("a este 0")  # --> nu se executa linia de cod pt ca conditia de mai sus este falsa

if b and b > a:  # --> daca b este evaluat ca adevarat si daca este mai mare decat a
    print("Da")

# 2. if ... else

a = 333
b = 200

if b > a:
    print("b este mai mare decat a")
else:
    print("b este mai mic decat a")

# 3. if ... elif ... else

a = 333
b = 0

if b > a:
    print("b este mai mare decat a")
elif b == a:
    print("b este egal cu a")
elif b == 0:
    print("b este 0")
else:  # --> nu este obligatoriu sa avem "else" aici pt ca este redundant
    print("b este mai mic decat a")

# 4. shorthand

a = 333
b = 200

x = a if a > b else b
print("a") if a > b else print("b")
