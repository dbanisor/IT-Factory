# seturile sunt folosite pt a stoca mai multe elemente intr-o singura
# variabila dar fara duplicate

# Create

fruits = {"apple", "banana", "cherry"}
cars = set()

# Length

print(20 * "-", "Length", 20 * "-")

print(len(fruits))

# Add elements

print(20 * "-", "Adding elements", 20 * "-")

fruits.add("pear")
print(fruits)

tropical = {"mango", "papaya"}
fruits.update(tropical)
print(fruits)

fruits.update(["kiwi", "orange"])
print(fruits)

fruits.add("apple")  # nu poate avea duplicate
print(fruits)

# Remove elements

print(20 * "-", "Removing elements", 20 * "-")

fruits.remove("banana")
print(fruits)

# fruits.remove("grapes") # arunca eroare pt ca elementul nu exista

fruits.discard("grapes")
print(fruits)

fruits.pop()  # elimina ultimul element inserat
print(fruits)

a = {1, 2, 3}
a.clear()
print(a)

# join

print(20 * "-", "Joining elements", 20 * "-")

s1 = {"a", "b", "c"}
s2 = {1, 2, 3}

s3 = s1.union(s2)
print(s3)
print(s1 | s2)  # forma prescurtata "union"

# intersection

print(20 * "-", "Intersecting elements", 20 * "-")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
print(x & y)  # forma prescurtata de la "intersection"

# difference

print(20 * "-", "Differencing elements", 20 * "-")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
print(x - y)  # forma prescurtata de la "difference"

# Symetric difference

print(20 * "-", "Symetric difference", 20 * "-")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
print(x ^ y)  # forma prescurtata de la "symetric difference"

# issubset & issuperset

print(20 * "-", "issubset & issuperset", 20 * "-")

x = {"a", "b", "c"}
y = {"a", "b", "c", "d", "e", "f"}

print(x.issubset(y))
print(y.issuperset(x))


