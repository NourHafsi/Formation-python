from .Utilisateur import Utilisateur
class Enseignant(Utilisateur):
    def __init__(self, identifiant, nom, email):
        super().__init__(identifiant, nom, email, role="Enseignant")
    
    def to_dict(self):
        return {
            "id": self.identifiant,
            "nom": self.nom,
            "email": self.email,
            "role": "Enseignant"
        }