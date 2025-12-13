from utils.validateur import *
from utils.generateur import generer_uuid_id
from package.Etudiant import Etudiant
from package.Enseignant import Enseignant
from package.Administrateur import Administrateur
from utils.json_manager import load_json, save_json


class UtilisateurService:
    def __init__(self, fichier="../Data/utilisateurs.json"):
        self.fichier = fichier
        self.utilisateurs = load_json(self.fichier)   # LISTE DE DICTIONNAIRES

    def ajouter_utilisateur(self, nom, email, role):
        # ---- VALIDATIONS ----
        if not valider_emails(email):
            print("Email invalide.")
            return False

        if not valider_noms(nom):
            print("Nom invalide.")
            return False

        if not valider_roles(role):
            print("Rôle invalide.")
            return False

        # ---- GENERATION ID ----
        ID = generer_uuid_id()

        # ---- CREATION DE L'OBJET ----
        if role == 'Etudiant':
            user = Etudiant(ID, nom, email)
            user.cours_inscrits = []  # facultatif
        elif role == 'Enseignant':
            user = Enseignant(ID, nom, email)
        elif role == 'Administrateur':
            user = Administrateur(ID, nom, email)
        else:
            print("Rôle non reconnu.")
            return False

        # ---- AJOUT DANS LA LISTE → TO_DICT ----
        self.utilisateurs.append(user.to_dict())

        # ---- SAUVEGARDE JSON ----
        save_json(self.fichier, self.utilisateurs)

        return user

    def supprimer_utilisateur(self, ID):
        for user in self.utilisateurs:
            if user.ID == ID:
                self.utilisateurs.remove(user)
                save_json(self.fichier, self.utilisateurs)
                return True
        return False

    def lister_utilisateurs(self):
        return self.utilisateurs
