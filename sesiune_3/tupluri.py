# Create

fruits = ("apple", "banana", "cherry", "cherry")
print(fruits)

# Count

print(20 * "-", "count", 20 * "-")

print(fruits.count("cherry"))

# Indexing

print(20 * "-", "indexing", 20 * "-")

print(fruits[0])
print(fruits[1:3])
print(fruits[-1])

# Adding elements

print(20 * "-", "Adding elements", 20 * "-")

fruits += ("pear",)
# sau
y = list(fruits)  # transformare intermediara in teren pt a adauga elemente
y.append("orange")
print(tuple(y))

# Remove

print(20 * "-", "Removing elements", 20 * "-")

y = list(fruits)
y.remove("apple")
print(tuple(y))
