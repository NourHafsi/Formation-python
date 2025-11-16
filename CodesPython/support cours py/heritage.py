class Employe:
    def __init__(self,nom, salaire_base):
        self.nom=nom
        self.salaire_base=salaire_base
    
    def afficher_salaire(self):
        print(f"le salaire de base de l'employé est {self.salaire_base}")
class Manager(Employe):
    def __init__(self,nom,salaire_base,prime):
        super().__init__(nom,salaire_base)
        self.prime=prime
M1=Manager("ramzi","1000 dinars","500dinars")
M1.afficher_salaire()