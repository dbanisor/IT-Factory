'''
Singleton este un sablon creational care se asigura ca o clasa are doar o singura instanta in timp ce ofera acces global la aceasta.
'''

class SingletonLogger:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("creating object")
            cls._instance = super().__new__(cls)
        return cls._instance

l = SingletonLogger()
print(l)
l2 = SingletonLogger()
print(l2)

'''
Avantaje:
    - poti sa te asiguri ca o clasa are o singura instanta
    - poti avea acces global la acea instanta
    - obiectul singleton este initializat doar cand este cerut pentru prima data
    
Dezavantaje:
    - poate masca design prost de ex. atunci cand componentele unui program stiu prea multe intre ele
'''










