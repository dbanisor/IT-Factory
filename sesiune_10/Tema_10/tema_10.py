'''
1. Sa se implementeze un decorator care masoara timpul necesar executiei unei functii.
'''
import functools
from time import perf_counter
import csv


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        stop = perf_counter()
        return stop - start

    return wrapper


@timer
def greetings(name):
    print(f"Welcome to the company {name}.\n"
          f"Should you have any questions, please attend the Induction training.\n"
          f"We hope for a happy collaboration, {name}.")


# new_joiner = greetings("Maria")
# print(new_joiner)

'''
2. Sa se genereze primele 100 de numere prime folosind liste, si apoi folosind generator.
Comparati diferenta de timp necesara generarii.
'''
# prime_nrs = []
# for i in range(2, 101):
#     for j in range(2, 101):
#         if i % j == 0:
#             break
#     if i == j:
#         prime_nrs.append(i)
# print(prime_nrs)

#-------------------------------------

def prime_generator(n):
    nr = 25
    while nr != 0:
        for i in range(2, n+1):
            for j in range(2, n+1):
                if i % j == 0:
                    break
            if i == j:
                yield i
                nr -= 1
gen = prime_generator(100)
# for i in gen:
#     print(i)

'''
3. Scrieti un decorator care primeste ca argument numele unui fisier si 
pentru orice functie apelata, el va scrie in acel fisier numele functiei, 
lista de argumente ca si string si rezultatul apelului. Fisierul este de tip csv. 
Functiile decorate pot primi oricate argumente
'''

def write_file(filename):
    def decorator_write_file(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with open(filename, "w") as f:
                function_name = func.__name__
                result = func(*args, **kwargs)
                writer = csv.writer(f)
                writer.writerows([
                    ["Function name", "Args", "Kwargs", "Result"],
                    [function_name, str(args), str(kwargs), result]])
        return wrapper
    return decorator_write_file

@write_file("test.csv")
def template(name, age, location):
    return f"{name}, age {age}, from {location} has written in a file."

template("John", age=22, location="London")













