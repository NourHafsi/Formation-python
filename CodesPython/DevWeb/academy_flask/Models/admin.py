from .user import user
class admin (user):
    def __init__(self, identifiant, nom, email):
        super().__init__(identifiant, nom, email, role="admin")
    def ajouter_personne(self):
        return "l'administrateur a ajouté une personne au Systeme"
    
    def to_dict(self):
        return {
            "id": self.identifiant,
            "nom": self.nom,
            "email": self.email,
            "role": "admin"
        }