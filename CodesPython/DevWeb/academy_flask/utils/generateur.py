import uuid

def generer_uuid_id():
    """Génère un identifiant unique universel (UUID) aléatoire."""
    return str(uuid.uuid4())[:6] # Retourne les 6 premiers caractères du UUID