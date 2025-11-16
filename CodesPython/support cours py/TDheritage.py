
#EX1:
class Personne:
    def __init__(self,nom,age):
        self.nom= nom
        self.age= age
    def afficher_informations(self):
        print(f"l'eleve {self.nom} a {self.age} ans.")
class Etudiant(Personne):
    def __init__(self,nom,age,niveau):
        super().__init__(nom,age)
        self.niveau=niveau
    def afficher_informations(self):
        print(f"l'eleve {self.nom} a {self.age} ans et il est en {self.niveau}")

class Enseignant(Personne):
    def __init__(self,nom,age,matiere):
        super().__init__(nom,age)
        self.matiere=matiere
    def afficher_informations(self):
        print(f"l'enseignant {self.nom} a {self.age} ans et il donne le cours de  {self.matiere}")
P=Personne("ALI",23)
P.afficher_informations()
ET= Etudiant("SARRA",18,"bac")
ET.afficher_informations()
En=Enseignant("MAHMOUD",40,"Maths")
En.afficher_informations()
Liste=[P,ET,En]
for x in Liste:
    Liste.afficher_informations()