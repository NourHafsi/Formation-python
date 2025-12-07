from .Utilisateur import Utilisateur
class Enseignant(Utilisateur):
    def __init__(self, identifiant, nom, email):
        super().__init__(identifiant, nom, email, role="Enseignant")