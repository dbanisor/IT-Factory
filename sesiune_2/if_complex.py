# 1. nested if

a = 5
b = 6
c = 9

if a > b:
    if c != 0:
        print("c diferit de 0")
    elif b == 0:
        print("b este 0")
else:
    if c == 0:
        print("c este 0")

# 2. "if" cu conditii multiple

x, y, z = 0, 2, 4

if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print("x, y si z sunt numere pare")
elif x % 2 == 0 or y % 2 == 0 or z % 2 == 0:
    print("Cel putin unul este par")
else:
    print("Toate sunt impare")

paritate = [x % 2 == 0, y % 2 == 0, z % 2 == 0]

if all(paritate):
    print("toate sunt pare")
elif any(paritate):
    print("cel putin unul este par")
else:
    print("Toate sunt impare")
