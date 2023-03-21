count = 0

while count < 3:
    count += 1
    print(f"count: {count}")


print(20 * "*", "Iterare prin lista", 20 * "*")

l = [1, 2, 3, 4, 5]
index = 0

while index < len(l):
    print(f"Element: {l[index]}")
    index += 1

print(20 * "*", "Break", 20 * "*")

i = 1

while i < 6:
    print(i)
    if i == 3:
        break  # forteaza iesirea din bucla
    i += 1

print(20 * "*", "Break + bucla infinita", 20 * "*")

import random

while True:
    nr = random.randint(0, 9)
    print(nr)
    if nr % 2 == 0:
        break

print(20 * "*", "Continue", 20 * "*")

i = 0

while i < 6:
    i += 1
    if i == 3:
        continue  # sare peste codul de dedesubt
    print(i)

print(20 * "*", "Else", 20 * "*")

count = 0
while count < 3:
    count += 1
    print(f"Count: {count}")
else:  # se executa la finalul buclei while, cand conditia devine falsa
    print("In blocul Else")

print(20 * "*", "Else + break", 20 * "*")

count = 0
while count < 3:
    count += 1
    print(f"Count: {count}")
    if count == 2:
        break
else:  # nu se mai executa pt ca a aparut un break
    print("In blocul Else")




