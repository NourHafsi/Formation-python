class Cours:
    def __init(self, code_cours, titre, enseignant, capacite_cours):
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
        