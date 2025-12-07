class Inscription:
    def inscri_etudiant(self, cours, etudiant):
        if etudiant in cours.etudiants_inscrits:
            print("L'étudiant est déjà inscrit à ce cours.")
            return False
        if len(cours.etudiants_inscrits) >= cours.capacite_cours:
            print("Le cours a atteint sa capacité maximale.")
            return False
        if cours.ajouter_etudiant(etudiant):
            etudiant.cours_inscrits.append(cours)
            return True
        return False
    def deinscri_etudiant(self, cours, etudiant):
        if etudiant not in cours.etudiants_inscrits:
            print("L'étudiant n'est pas inscrit à ce cours.")
            return False
        cours.etudiants_inscrits.remove(etudiant)
        etudiant.cours_inscrits.remove(cours)
        return True
    def lister_etudiantinscrits(self,cours):
        return cours.etudiants_inscrits