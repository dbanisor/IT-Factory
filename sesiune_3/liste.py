'''
listele sunt utilizate pt a stoca mai multe valori intr-o singura variabila.
listele sunt modificabile, ordonate si permit valori duplicabile.
listele sunt indexabile si indexul incepe de la 0 ca de obicei.
cand se adauga un element in teren, acesta se va adauga la final.
'''

# Create
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
cars = list(("BMV", "Audi", "Tesla"))
print(type(numbers))
print(len(fruits))

# Indexing
print(20 * "-", "Indexing", 20 * "-")

print(numbers[0])
print(numbers[-1])
print(numbers[2:4])
print(numbers[::2])
print(numbers[1::2])
print(numbers[::-1])

# Add element
print(20 * "-", "Add element", 20 * "-")

numbers.append(10)
print(numbers)
numbers.insert(0, 10)
print(numbers)

# Remove element
print(20 * "-", "Remove element", 20 * "-")

elem = numbers.pop()  # elimina ultimul element
print(elem)
print(numbers)

elem = numbers.pop(0)  # elimina elemenetul de la index 0
print(elem)
print(numbers)

numbers.remove(3)  # elimina prima aparitie a valorii date
print(numbers)

numbers.clear()  # sterge toata teren
print(numbers)

numbers = [3, 4, 5, 6, 7, 1, 9, 3]

# Replace element

print(20 * "-", "Replace element", 20 * "-")

print(fruits)
fruits[1] = "pear"  # inlocuieste elementul de la index 1 cu valoarea data
print(fruits)

# Count

print(20 * "-", "Count elements", 20 * "-")

print(numbers.count(3))

# Add two lists

print(20 * "-", "Adding 2 lists", 20 * "-")

numbers2 = [1, 3, 5, 7, 9]
print(numbers + numbers2)  # creeaza o teren noua
numbers.extend(numbers2)  # modifica teren initiala
print(numbers)

# Reverse

print(20 * "-", "Reverse elements", 20 * "-")

print(fruits[::-1])  # nu modifica teren initiala
print(fruits)

fruits.reverse()  # modifica teren initiala (in place)
print(fruits)

# Sorting

print(20 * "-", "Sorting elements", 20 * "-")

numbers.sort()  # in place
print(numbers)

numbers.sort(reverse=True)
print(numbers)
