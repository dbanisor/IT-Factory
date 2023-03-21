def say_hi():
    return "Hello!"  # Opreste executia functiei
    print("Salut!")


a = say_hi()
print(a)


def print_first_50():
    for i in range(50):
        print(i)
    # return None
    # return
# print_first_50() are valoare de return implicit None sau se poate specifica explicit cu cele doua variante de mai sus (ele sunt echivalente)

b = print_first_50()
print(b)


def iterare():
    for i in range(5):
        return i

print(iterare())


def doar_daca():
    if False:
        return 1
    print("Nu e False")

print(doar_daca())