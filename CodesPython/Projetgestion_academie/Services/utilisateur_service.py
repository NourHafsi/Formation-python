from utils.validateur import *
from utils.generateur import generer_uuid_id
from package.Etudiant import Etudiant
from package.Enseignant import Enseignant
from package.Administrateur import Administrateur
class UtilisateurSerice:
    def __init__(self):
        self.Utilisateurs = []
    def ajouter_utilisateur(self, nom, email, role):
        if not valider_emails(email):
            print("Email invalide.")
            return False
        if not valider_noms(nom):
            print("Nom invalide.")
            return False
        if not valider_roles(role):
            print("Rôle invalide.")
            return False
        ID = generer_uuid_id()
        if role == 'Etudiant':
            user = Etudiant(ID, nom, email)
        elif role == 'Enseignant':
            user = Enseignant(ID, nom, email)
        elif role == 'Administrateur':
            user = Administrateur(ID, nom, email)
        else:
            print("Rôle non reconnu.")
            return False
    def supprimer_utilisateur(self,ID):
        for user in self.Utilisateurs:
            if user.ID == ID:
                self.Utilisateurs.remove(user)
                return True
    def lister_utilisateurs(self):
        return self.Utilisateurs