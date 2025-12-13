from utils.json_manager import load_json, save_json
from package.Cours import Cours
from package.Etudiant import Etudiant


class InscriptionService:
    def __init__(self,
                 fichier_cours="../Data/cours.json",
                 fichier_users="../Data/utilisateurs.json"):
        
        self.fichier_cours = fichier_cours
        self.fichier_users = fichier_users

        # --- Charger les cours ---
        raw_cours = load_json(self.fichier_cours)
        self.cours = [Cours.from_dict(d) for d in raw_cours]

        # --- Charger les utilisateurs ---
        raw_users = load_json(self.fichier_users)
        self.utilisateurs = raw_users   # on garde les dict, pas besoin d'objets ici

    # -----------------------------------------------
    # Helper pour retrouver un cours selon son code
    # -----------------------------------------------
    def get_cours(self, code_cours):
        for c in self.cours:
            if c.code_cours == code_cours:
                return c
        return None

    # -----------------------------------------------
    # Helper pour retrouver un étudiant via son id
    # -----------------------------------------------
    def get_etudiant(self, etu_id):
        for u in self.utilisateurs:
            if u["id"] == etu_id and u["role"] == "Etudiant":
                return u
        return None

    # -----------------------------------------------
    # Sauvegarde interne
    # -----------------------------------------------
    def _sauvegarder(self):
        # Sauvegarder les cours
        data_cours = [c.to_dict() for c in self.cours]
        save_json(self.fichier_cours, data_cours)

        # Sauvegarder utilisateurs modifiés
        save_json(self.fichier_users, self.utilisateurs)

    # -----------------------------------------------
    # Inscrire un étudiant dans un cours
    # -----------------------------------------------
    def inscrire_etudiant(self, code_cours, etu_id):
        cours = self.get_cours(code_cours)
        etudiant = self.get_etudiant(etu_id)

        if cours is None:
            print("Cours introuvable.")
            return False

        if etudiant is None:
            print("Étudiant introuvable.")
            return False

        if etu_id in cours.etudiants_inscrits:
            print("Étudiant déjà inscrit.")
            return False

        if len(cours.etudiants_inscrits) >= cours.capacite_cours:
            print("Capacité atteinte.")
            return False

        # --- Inscription ---
        cours.etudiants_inscrits.append(etu_id)

        # Ajouter ce cours à l'étudiant
        etudiant.setdefault("cours_inscrits", [])
        etudiant["cours_inscrits"].append(code_cours)

        self._sauvegarder()
        return True

    # -----------------------------------------------
    # Désinscription
    # -----------------------------------------------
    def desinscrire_etudiant(self, code_cours, etu_id):
        cours = self.get_cours(code_cours)
        etudiant = self.get_etudiant(etu_id)

        if cours is None or etudiant is None:
            print("Cours ou étudiant introuvable.")
            return False

        if etu_id not in cours.etudiants_inscrits:
            print("Étudiant non inscrit.")
            return False

        cours.etudiants_inscrits.remove(etu_id)

        if "cours_inscrits" in etudiant and code_cours in etudiant["cours_inscrits"]:
            etudiant["cours_inscrits"].remove(code_cours)

        self._sauvegarder()
        return True

    # -----------------------------------------------
    # Liste des inscrits
    # -----------------------------------------------
    def lister_etudiants_inscrits(self, code_cours):
        cours = self.get_cours(code_cours)
        if cours:
            return cours.etudiants_inscrits
        return []
