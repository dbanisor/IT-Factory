'''
API-urile (Application Programming Interface) permit aplicatiilor software sa comunice intre ele.
Actioneaza ca un mediator intre 2 aplicatii permitand uneia sa solicite date sau servicii de la cealalta si sa primeasca un raspuns in schimb.


REST Introduction
REST (Representational State Transfer) este un stil arhitectural pt furnizarea de standarde intre sistemele web, facilitand comunicarea acestora.
Sistemele compatibile REST, numite si sisteme restful, se caracterizeaza prin faptul ca nu au stare (state) si separa clientul de server.
Pt ca un API sa fie restul trebuie sa respecte urmatoarele constrangeri:
    1. arhitectura client-server: clientul si serverul sunt separate si actioneaza indentendent, permitand utilizarea mai multor tehnologii pt fiecare.
    2. stateless: serverul nu stocheaza niciun context intre cereri (requests) astfel incat fiecare cerere contine toate informatiile necesare pt a o finaliza.
    3. capacitatea de cache: clientii pot stoca in cache datele de raspuns reducand numarul de solicitari catre server si astfel imbunatatind performanta.
    4. utilizarea metodelor HTTP: API-urile restful utilizeaza metode HTTP standard (GET, POST, PUT, DELETE) pt a interactiona cu resurse unde
    fiecare metoda reprezinta o actiune specifica (de ex. GET preia date si POST creeaza o noua resursa).
    5. utilizarea codurilor de stare HTTP: folosirea codurilor specifice HTTP cum ar fi 200 (succes), 400 (esec), 404 (negasit).


HTTP methods
Metodele HTTP sunt verbele standard utilizate pt a indica actiunea dorita care trebuie efectuata pe o resursa dintr-un API.
Cele 4 metode HTTP principale sunt:
    1. GET: preia date dintr-o reursa si este folosit pt citire
    2. POST: creeaza o noua resursa si este folosit pt a trimite date catre un server
    3. PUT: actualizeaza o resursa curenta si este folosit pt a modifica datele existente
    4. DELETE: sterge o resursa si este folosit pt a elimina date
'''