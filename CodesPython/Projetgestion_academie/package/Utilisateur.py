class Utilisateur:
    def __init__(self, identifiant, nom, email, role):
        self.identifiant = identifiant
        self.nom = nom
        self.email = email
        self.role = role
    def afficher_role(self):
        return self.role
    def Consulter_infos(self):
        return f"Nom: {self.nom}, Email: {self.email}, Rôle: {self.role}"

