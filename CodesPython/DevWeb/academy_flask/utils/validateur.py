import re

def valider_emails(email):

    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex, email) is not None


def valider_noms(nom):

    if not isinstance(nom, str):
        return False

    if len(nom.strip()) < 2:
        return False

    return True


def valider_roles(role):

    roles_valides = ["Etudiant", "Enseignant", "Administrateur"]
    return role in roles_valides


def valider_capacites(capacite):

    if isinstance(capacite, int) and capacite > 0:
        return True

    return False
