from .user import user
class student(user):
    def __init__(self, identifiant, nom, email):
        super().__init__(identifiant, nom, email, role="student")
        self.cours_inscrits = []

    def to_dict(self):
        return {
            "id": self.identifiant,
            "nom": self.nom,
            "email": self.email,
            "role": "student"
        }