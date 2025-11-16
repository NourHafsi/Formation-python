#creez une classe animal qui a :
#.attribut nom
#.attribut type
#.méthode description()
#creez une classe oiseau qui hérite de animal et redinit la méthode description
class Animal:
    def __init__(self,nom,type):
        self.nom=nom
        self.type=type
    def description(self):
        print(f"l'animal {self.nom} est de type {self.type}")
class Zoo:
    def __init__(self,nomz,localisation):
        self.nomz=nomz
        self.localisation=localisation
    
    def affichage(self):
        print(f"le zoo {self.nomz} est situé à {self.localisation}")

class oiseau(Animal,Zoo):
    def __init__(self,nom,type,nomz,localisation,couleur):
        Animal.__init__(self,nom,type)
        Zoo.__init__(self,nomz,localisation)
        self.couleur=couleur
oiseau1=oiseau("lion","sauvage","belvedre","tunis","noir")
oiseau1.description()
oiseau1.affichage()
