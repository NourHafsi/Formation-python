#Exercice 2:
# Créer une classe EmployeHopital avec un salaire et une méthode travailler(). 
# Créer deux sous-classes : Medecin et Infirmier.
# Medecin : diagnostiquer un patient
# Infirmier : soigner un patient 
# Dans chaque sous-classe, redéfinir travailler() 
# pour afficher des actions différentes. Écrire un programme qui affiche le 
# comportement de chaque employé polymorphiquement.

""" class EmployeHopital:
    def __init__(self, salaire):
        self.salaire = salaire

    def travailler(self):
        print(f"L'employé travaille avec un salaire de {self.salaire} dt.")


class Medecin(EmployeHopital):
    def __init__(self, salaire):
        super().__init__(salaire)

    def travailler(self):
        print(f"Le médecin diagnostique le patient avec un salaire de: {self.salaire} dt.")

    def diagnostiquer(self):
        print("Le médecin fait un diagnostic.")


class Infirmier(EmployeHopital):
    def __init__(self, salaire):
        super().__init__(salaire)

    def travailler(self):
        print(f"L'infirmier soigne le patient avec un salaire de: {self.salaire} dt.")

    def soigner(self):
        print("L'infirmier fait un traitement de soin.")


# Programme principal
E = EmployeHopital(1500)
M = Medecin(5000)
I = Infirmier(2000)

# Appel polymorphique
for employe in [E, M, I]:
    employe.travailler()

 """

#Exercice 3 : 
#Créer une classe Produit avec : nom, prix, afficher() 
# Créer des sous-classes : Fruit, Legume, ProduitLaitier. 
# Chaque classe doit ajouter un attribut qui lui est propre (ex : type de fruit, saison, date d’expiration). 
# Redéfinir afficher() dans chaque sous-classe. 
# Créer une liste de produits différents et afficher leurs informations grâce au polymorphisme.

""" class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def afficher(self):
        print(f"Le produit {self.nom} est de {self.prix} DT.")


class Fruit(Produit):
    def __init__(self, nom, prix, type):
        super().__init__(nom, prix)
        self.type = type

    def afficher(self):
        print(f"Le fruit {self.nom} est de type {self.type} et coûte {self.prix} DT.")


class Legume(Produit):
    def __init__(self, nom, prix, saison):
        super().__init__(nom, prix)
        self.saison = saison

    def afficher(self):
        print(f"Le légume {self.nom} est disponible en {self.saison} et coûte {self.prix} DT.")


class ProduitLaitier(Produit):
    def __init__(self, nom, prix, date_exp):
        super().__init__(nom, prix)
        self.date_exp = date_exp

    def afficher(self):
        print(f"Le produit laitier {self.nom} coûte {self.prix} DT et expire le {self.date_exp}.")


# --- Programme principal ---
produits = [
    Fruit("Pomme", 2.5, "pomme rouge"),
    Legume("Carotte", 1.2, "hiver"),
    ProduitLaitier("Yaourt", 1.8, "15/12/2025")
]

# --- Affichage polymorphique ---
for p in produits:
    p.afficher() """

#Exercice 4: 
class Animal:
    def parler(self):
        print("L'animal dit : baaaaaa baaaaaa")

class Chien(Animal):
    def parler(self):
        print("Le chien dit : wouf wouf")

class Chat(Animal):
    def parler(self):
        print("Le chat dit : miaou")

class Oiseau(Animal):
    def parler(self):
        print("L'oiseau dit : cui cui")

def faire_parler(animal):
    animal.parler()


liste_animaux = [Chien(), Chat(), Oiseau(), Animal()]

for a in liste_animaux:
    faire_parler(a)


