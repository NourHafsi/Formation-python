""" Crée une classe CompteBancaire avec :
attributs : nom et solde
méthodes :
afficher_solde()
deposer(montant)
retirer(montant) """

class CompteBancaire:
    def __init__(self,nom,solde):
        self.nom=nom
        self.solde=solde

    def afficher_solde(self):
        return print(f"l'utilisateur {self.nom} à un solde dans le compte de {self.solde}")
    
    def deposer(self,montant):
        if montant>0:
            self.solde=self.solde+montant
            print(f"le nouveau solde apres l'ajout de {montant} est {self.solde}")
        else:
            print("le montant donné doit etre strictement positif ! ")

    def retirer(self,montant):
        if self.solde>=montant:
            self.solde=self.solde-montant
            print("Transaction effectuée avec succés ! ")
        else:
            print("Transaction refusée ! pas de solde suffisant dans le compte ")


nom=input("donner un nom: ")       
CB1=CompteBancaire(nom, 1500)
CB1.afficher_solde()
montant=int(input("donner un montant: "))
CB1.deposer(montant)
montant1=int(input("donner un montant: "))
CB1.retirer(montant1)

