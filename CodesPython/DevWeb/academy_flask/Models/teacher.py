from .user import user
class teacher(user):
    def __init__(self, identifiant, nom, email):
        super().__init__(identifiant, nom, email, role="teacher")
    
    def to_dict(self):
        return {
            "id": self.identifiant,
            "nom": self.nom,
            "email": self.email,
            "role": "teacher"
        }