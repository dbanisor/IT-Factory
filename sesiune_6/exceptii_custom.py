class CustomExceptions(Exception):
    pass

# Sa se scrie o functie care verifica daca o lista de numere intregi contine numere negative.
# Daca da, sa se arunce o exceptie specifica

class ContainsNegativeException(Exception):
    pass

def verify_negative_numbers(numbers):
    for num in numbers:
        if num < 0:
            raise ContainsNegativeException(f"Il contine pe {num}.")

verify_negative_numbers([1, 3, 4, -2, 5])







