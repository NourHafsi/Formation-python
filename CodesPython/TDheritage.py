
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
#1ere methode
P=Personne("ALI",23)
P.afficher_informations()
ET= Etudiant("SARRA",18,"bac")
ET.afficher_informations()
En=Enseignant("MAHMOUD",40,"Maths")
En.afficher_informations()

#2eme methode d'affichage:via une boucle qui appelle afficher_informations().
P=Personne("ALI",23)
ET= Etudiant("SARRA",18,"bac")
En=Enseignant("MAHMOUD",40,"Maths")
Liste=[P,ET,En]
for x in Liste:
    x.afficher_informations()