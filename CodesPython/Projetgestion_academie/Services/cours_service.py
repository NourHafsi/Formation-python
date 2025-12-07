from package.Cours import Cours
class Cours_service:
    def __init__(self):
        self.cours = []
    def ajouter_cours(self, code_cours, titre, enseignant, capacite_cours):
        cours = Cours(code_cours, titre, enseignant, capacite_cours)
        self.cours.append(cours)
        return Cours
    def supprimer_Cours(self, code_cours):
        for cours in self.cours:
            if cours.code_cours == code_cours:
                self.cours.remove(cours)
                return True
        return False
    def lister_cours(self, code_cours):
        for cours in self.cours:
            if cours.code_cours == code_cours:
                return cours
        