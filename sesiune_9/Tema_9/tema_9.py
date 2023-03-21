'''
1. Sa se scrie o functie care citeste date dintr-un fisier csv si le scrie intr-un fisier json.
Functia primeste numele fisierelor ca parametri.
'''
import csv
import json
from pprint import pprint

# def read_and_write(out_filename, in_filename):
#     with open(out_filename, "r") as f:
#         reader = csv.DictReader(f)
#         result = []
#         for row in reader:
#             result.append(row)
#
#     with open(in_filename, "w") as f:
#         json.dump(result, f, indent=4)
#
# read_and_write("exercitiul1.csv", "tema_exercitiul1.json")

'''
2. Sa se scrie o functie care citeste date dintr-un fisier json si le imparte in alte doua fisiere astfel incat prima jumatate
a datelor va fi in fisierul prima_jumatate.json, iar a doua in a_doua_jumatate.json.
'''

# def read_and_write(out_filename, in_filename1, in_filename2):
#     with open(out_filename, "r") as f:
#         reader = json.load(f)
#         first_half = reader[:2]
#         second_half = reader[2:]
#     with open(in_filename1, "w") as f:
#         json.dump(first_half, f, indent=4)
#     with open(in_filename2, "w") as f:
#         json.dump(second_half, f, indent=4)
#
# pprint(read_and_write("exercitiul2.json", "prima_jumatate.json", "a_doua_jumatate.json"))

'''
3. Sa se scrie o functie care citeste date dintr-un fisier csv si le elimina pe cele care in 
oricare coloana contin litera "a". Dupa aceea va actualiza fisierul cu datele ce raman.
'''
def read_and_write(filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        result = []
        for row in reader:
            for key, value in row:
                if "a" not in value:
                    result.append(row)
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=result[0].keys())
        writer.writeheader()
        writer.writerows(result)

pprint(read_and_write("exercitiul3.csv"))