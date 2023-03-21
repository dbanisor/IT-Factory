for i in range(10):
    print(i)

print(20 * "*", 20 * "*")

for i in range(1, 6):
    print(i)

print(20 * "*", 20 * "*")

for i in range(1, 6, 2):
    print(i)

print(20 * "*", "Iterare folosing range", 20 * "*")

l = [1, 2, 3, 4, 5]
for i in range(len(l)):
    print(f"Element: {l[i]}")

print(20 * "*", "For each", 20 * "*")

fruits = ["apple", "banana", "cherry", "prune", "apricot"]

for fruit in fruits:
    print(fruit)

for x in "Ana are mere":
    print(x)

dct = {
    "a": 1,
    "b": 2,
}

print("***************************")

for x in dct:  # iterarea prin dictionar se face prin cheile dictionarelor.
    print(x)
print("!" * 50, "Important", "!" * 50)
# Daca vrem sa iteram prin chei si valori:
for key, value in dct.items():
    print(key, value)
print("!" * 50, "Important", "!" * 50)

print(20 * "*", "Break", 20 * "*")

for x in fruits:
    print(x)
    if x == "banana":
        break

print(20 * "*", "Continue", 20 * "*")

for x in fruits:
    if x == "banana":
        continue
    print(x)

print(20 * "*", "Else", 20 * "*")

for x in range(6):
    print(x)
else:
    print("In blocul Else")

print(20 * "*", "Else + break", 20 * "*")

for x in range(6):
    print(x)
    if x == 3:
        break
else:
    print("In blocul Else")

print(20 * "*", "Nested for", 20 * "*")

adj = ["red", "big", "tasty"]

for x in adj:
    for y in fruits:
        print(x, y)

print(20 * "*", "Pass", 20 * "*")

for x in [1, 2, 3]:
    # pass
    ...  # este echivalent cu "pass"

print(20 * "*", "Enumerate", 20 * "*")

for index, elem in enumerate(fruits):
    print(index, elem)


