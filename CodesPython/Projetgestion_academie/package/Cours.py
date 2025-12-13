class Cours:
    def __init__(self, code_cours, titre, enseignant, capacite_cours):
        self.code_cours = code_cours
        self.titre = titre
        self.enseignant = enseignant
        self.capacite_cours = capacite_cours
        self.etudiants_inscrits = []
    def ajouter_etudiant (self, etudiant):
        if len(self.etudiants_inscrits) >= self.capacite_cours:
            return False
        self.etudiants_inscrits.append(etudiant)
        return True
    
    def to_dict(self):
        return {
            "code_cours": self.code_cours,
            "titre": self.titre,
            "enseignant": self.enseignant,
            "capacite_cours": self.capacite_cours,
            "etudiants_inscrits": self.etudiants_inscrits
        }    
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            code_cours=data["code_cours"],
            titre=data["titre"],
            enseignant=data["enseignant"],
            capacite_cours=data["capacite_cours"],
            etudiants_inscrits=data["etudiants_inscrits"]
        )