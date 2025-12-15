class Cours:
    def __init__(self, code_cours, titre, enseignant_id, administrateur_id, capacite_cours, etudiants_inscrits=None):
        self.code_cours = code_cours
        self.titre = titre
        self.enseignant_id = enseignant_id
        self.administrateur_id = administrateur_id
        self.capacite_cours = capacite_cours
        self.etudiants_inscrits = etudiants_inscrits or []

    def to_dict(self):
        return {
            "code_cours": self.code_cours,
            "titre": self.titre,
            "enseignant_id": self.enseignant_id,
            "administrateur_id" : self.administrateur_id,
            "capacite_cours": self.capacite_cours,
            "etudiants_inscrits": self.etudiants_inscrits
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            code_cours=data["code_cours"],
            titre=data["titre"],
            enseignant_id=data["enseignant_id"],
            administrateur_id=data["administrateur_id"],
            capacite_cours=data["capacite_cours"],
            etudiants_inscrits=data.get("etudiants_inscrits", [])
        )