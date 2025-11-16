import json
# Dictionnaire global pour stocker les étudiants
fichier_JSON

# Fonction pour ajouter un étudiant
def ajout_etudiant():
    matricule = input("Donner la matricule de l'étudiant: ")
    nom = input("Donner le nom de l'étudiant: ")
    prenom = input("Donner le prénom de l'étudiant: ")
    note = input("Donner la note de l'étudiant: ")
    #etudiant = {}  <<< PROBLÈME ICI  Cette nouvelle variable masque la variable globale etudiant = {} définie au début.
    # Vérifier si l'étudiant existe déjà
    if matricule in etudiants:
        print("Cet étudiant existe déjà !")
    else:
        # Ajout dans le dictionnaire global
        etudiants[matricule] = {
            'Nom': nom,
            'Prenom': prenom,
            'Note': note
        }
        print("Étudiant ajouté avec succès.")

# Fonction pour Modifier un étudiant
def modif_etudiant():
    matricule= input("donner la matricule de l'etudiant à modifier")
    if matricule in etudiants:
        print(f"etudiant:{etudiants[matricule]}")
    else:
        print("etudiant introuvable")



# Fonction pour afficher tous les étudiants
def affich_etudiants():
    if etudiants:  # le dictionnaire n’est pas vide
        print("\n--- Liste des étudiants ---")
        for matricule, infos in etudiants.items():
            print(f"Matricule: {matricule} | Nom: {infos['Nom']} | Prénom: {infos['Prenom']} | Note: {infos['Note']}")
    else:
        print("Aucun étudiant n'a encore été ajouté.")

# Menu principal
def Menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1: Ajouter un étudiant")
    print("2: Modifier un étudiant")
    print("3: Supprimer un étudiant")
    print("4: Afficher tous les étudiants")
    print("5: Quitter")

# Boucle principale du programme
while True:
    Menu()
    try:
        x = int(input("Donnez votre choix: "))
    except ValueError:
        print("Veuillez entrer un nombre valide (1-5).")
        continue

    if x == 1:
        ajout_etudiant()
    elif x == 2:
        modif_etudiant()
    elif x == 3:
        print("Fonction suppression à implémenter...")
    elif x == 4:
        affich_etudiants()
    elif x == 5:
        print("Au revoir !")
        break
    else:
        print("Choix invalide, veuillez choisir entre 1 et 5.")
