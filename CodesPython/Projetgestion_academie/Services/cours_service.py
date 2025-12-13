from utils.json_manager import load_json, save_json
from package.Cours import Cours


class Cours_service:
    def __init__(self, fichier="../Data/cours.json"):
        self.fichier = fichier

        # Charger la liste des cours sous forme de dictionnaires
        data = load_json(self.fichier)

        # Convertir chaque dictionnaire en objet Cours
        self.cours = [Cours.from_dict(d) for d in data]

    def ajouter_cours(self, code_cours, titre, enseignant, capacite_cours):
        cours = Cours(code_cours, titre, enseignant, capacite_cours)

        # Ajouter l'objet dans la liste
        self.cours.append(cours)

        # Sauvegarder la liste mise à jour
        self._sauvegarder()

        return cours

    def supprimer_cours(self, code_cours):
        for c in self.cours:
            if c.code_cours == code_cours:
                self.cours.remove(c)
                self._sauvegarder()
                return True
        return False

    def lister_cours(self):
        return self.cours

    def chercher_cours(self, code_cours):
        for c in self.cours:
            if c.code_cours == code_cours:
                return c
        return None

    def _sauvegarder(self):
        """Sauvegarde interne : convertit les objets en dictionnaires."""
        data = [c.to_dict() for c in self.cours]
        save_json(self.fichier, data)
