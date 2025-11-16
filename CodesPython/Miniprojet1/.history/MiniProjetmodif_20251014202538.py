import json
# Dictionnaire global pour stocker les étudiants
fichier_JSON="etudiants.json"
etudiant={}

#fonction pour charger le json file (pour etre utilisable coté python: soit remplissage, modification, affichage)
def charger_JSON():
    try:
        with open(fichier_JSON, 'r') as file:
            data = json.load(file) #read data from json file
        print(data)
        print(type(data))
    except FileNotFoundError:
        print("Error: 'data.json' not found. Please ensure the file exists.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in 'data.json'.")

def sauvegarde_JSON():
    with open(fichier_JSON, 'w', encoding='utf-8') as file:
        json.dump(etudiant, file)
        #json.dump(etudiants, file, indent=4, ensure_ascii=False) #pour envoyer des datas of code python (donnees etusdiants) to json file


# Fonction pour ajouter un étudiant
def ajout_etudiant():
    matricule = input("Donner la matricule de l'étudiant: ")
    nom = input("Donner le nom de l'étudiant: ")
    prenom = input("Donner le prénom de l'étudiant: ")
    note = input("Donner la note de l'étudiant: ")
    #etudiant = {}  <<< PROBLÈME ICI  Cette nouvelle variable masque la variable globale etudiant = {} définie au début.
    # Vérifier si l'étudiant existe déjà
    if matricule in etudiant:
        print("Cet étudiant existe déjà !")
    else:
        # Ajout dans le dictionnaire global
        etudiant[matricule] = {
            'Nom': nom,
            'Prenom': prenom,
            'Note': note
        }
        print("Étudiant ajouté avec succès.")
        sauvegarde_JSON()
# Fonction pour Modifier un étudiant
def modif_etudiant():
    matricule= input("donner la matricule de l'etudiant à modifier")
    if matricule in etudiant:
        print(f"etudiant:{etudiant[matricule]}")
    else:
        print("etudiant introuvable")
        #sauvegarde_JSON()


# Fonction pour afficher tous les étudiants
def affich_etudiants():
    """ if etudiants:  # le dictionnaire n’est pas vide
        print("\n--- Liste des étudiants ---")
        for matricule, infos in etudiants.items():
            print(f"Matricule: {matricule} | Nom: {infos['Nom']} | Prénom: {infos['Prenom']} | Note: {infos['Note']}")
    else:
        print("Aucun étudiant n'a encore été ajouté.") """
    print()
# Menu principal
def Menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1: Ajouter un étudiant")
    print("2: Modifier un étudiant")
    print("3: Supprimer un étudiant")
    print("4: Afficher tous les étudiants")
    print("5: Quitter")
etudiants=charger_JSON()
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
