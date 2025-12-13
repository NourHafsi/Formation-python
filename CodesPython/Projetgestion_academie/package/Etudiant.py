from .Utilisateur import Utilisateur
class Etudiant(Utilisateur):
    def __init__(self, identifiant, nom, email):
        super().__init__(identifiant, nom, email, role="Etudiant")
        self.cours_inscrits = []

    def to_dict(self):
        return {
            "id": self.identifiant,
            "nom": self.nom,
            "email": self.email,
            "role": "Etudiant"
        }
        
