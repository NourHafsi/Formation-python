from .Utilisateur import Utilisateur
class Administrateur (Utilisateur):
    def __init__(self, identifiant, nom, email):
        super().__init__(identifiant, nom, email, role="Administrateur")
    def ajouter_personne(self):
        return "l'administrateur a ajouté une personne au Systeme"