class Personne:
    def __init__(self,nom,age):
            self._nom=nom
            self._age=age
     # getter pour le nom
    def get_age(self):
        return self._age
    # setter pour le nom
    def set_age(self,new):
        if new >= 0 and new <= 120:
            self._age = new
        else:
            print("age invalide") 
nom =Personne("wafae",20)
print(nom.get_age())
nom.set_age(21)
print(nom.get_age())