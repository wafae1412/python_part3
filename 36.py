
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficherInfos(self):
        print("Nom:", self.nom)
        print("Age:", self.age)

class Salarie(Personne):
    def __init__(self, nom, age, numeroSomme, salaire):
        super().__init__(nom, age)
        self.numeroSomme = numeroSomme
        self.salaire = salaire

    def calculerSalaire(self):
        return self.salaire

    def afficherInfos(self):
        super().afficherInfos()
        print("Numero Somme:", self.numeroSomme)
        print("Salaire:", self.salaire)


class Etudiant(Personne):
    def __init__(self, nom, age, cne, notes):
        super().__init__(nom, age)
        self.cne = cne
        self.notes = notes

    def calculerMoyenne(self):
        return sum(self.notes) / len(self.notes)

    def afficherInfos(self):
        super().afficherInfos()
        print("CNE:", self.cne)
        print("Notes:", self.notes)


class Doctorant(Salarie, Etudiant):
    def __init__(self, nom, age, numeroSomme, salaire, cne, notes, departement, anneeInscription):
        Salarie.__init__(self, nom, age, numeroSomme, salaire)
        Etudiant.__init__(self, nom, age, cne, notes)
        self.departement = departement
        self.anneeInscription = anneeInscription

    def afficherInfos(self):
        Personne.afficherInfos(self)
        print("Numero Somme:", self.numeroSomme)
        print("Salaire:", self.salaire)
        print("CNE:", self.cne)
        print("Notes:", self.notes)
        print("Departement:", self.departement)
        print("Annee Inscription:", self.anneeInscription)



d = Doctorant("Wafae", 25, "NS123", 5000, "CNE456", [12, 14, 16], "Informatique", 2023)

d.afficherInfos()
print("Moyenne:", d.calculerMoyenne())
print("Salaire:", d.calculerSalaire())