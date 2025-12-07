import re
def valider_emails(emails):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, emails):
        return True
    else:
        return False
def valider_noms(nom):
    if not isinstance(nom, str):
        print("Erreur : Le nom doit être une chaîne de caractères.")
        return False
    if not nom.strip(): # .strip() enlève les espaces blancs au début/fin
        print("Erreur : Le nom ne peut pas être vide.")
        return False
    if len(nom.strip()) < 2:
        print("Erreur : Le nom doit contenir au moins 2 caractères.")
        return False
    if not nom.replace(" ", "").isalpha(): # isalpha() vérifie si tout est alphabétique
        print("Erreur : Le nom ne doit contenir que des lettres et des espaces.")
        return False
    return True # Si toutes les conditions sont passées, le nom est valide
def valider_roles(role):
    roles_valides = ["Etudiant", "Enseignant", "Administrateur"]
    if role not in roles_valides:
        return False
    return True
def valider_capacites(capacites):
    if not capacites > 0:
        return False
    if not isinstance(capacites, int):
        return False
    return True
