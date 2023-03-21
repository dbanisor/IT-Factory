# 1. Functii ca argument

# def say_hello(name):
#     return f"Hello {name}"
#
#
# def say_hi(name):
#     return f"Hi {name}"
#
#
# def greet_bob(func):
#     return func("Bob")


# print(greet_bob(say_hi))
# print(greet_bob(say_hello))


# 2. Functii interioare

def parent():
    print("parent")

    def first_child():
        print("first child")

    def second_child():
        print("second child")

    second_child()
    first_child()


# parent()

# 3. Returnare de functii

def parent(n):
    def first_child():
        return "first child"

    def second_child():
        return "second child"

    if n == 1:
        return first_child
    else:
        return second_child

f = parent(2)
print(type(f))
print(f())