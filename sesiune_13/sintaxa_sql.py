'''
SQL (Structured Query Language) este limbajul folosit pentru gestionarea si manipularea bazelor de date relationale. Permite utilizatorilor sa insereze,
sa actualizeze sau sa stearga datele stocate intr-o baza de date.
Sintaxa SQL consta intr-un set de comenzi, clauze si functii care efectueaza operatii specifice asupra datelor stocate intr-o baza de date.
'''

''' 1. CREATE - pt creare de tabel
'''
# CREATE TABLE table_name (
#     column1 datatype1,
#     column2 datatype2,
#     ...
# );

'''2. SELECT - pt a lua date din baza de date
'''
# SELECT column1, column2, ...
# FROM table_name;

''' 3. INSERT - pt a adauga date
'''
# INSERT INTO table_name (column1, column2, ...)
# VALUES (value1, value2, ...);

''' 4. UPDATE - pt a actualiza date
'''
# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE some_column = some_value;

''' 5. DELETE - pt a sterge date
'''
# DELETE FROM table_name
# WHERE some_column = some_value;