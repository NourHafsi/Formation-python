from Services.utilisateur_service import * 
from Services.cours_service import * 
from Services.inscription_service import *
# =========================
# INITIALISATION DES SERVICES
# =========================
user_service = UtilisateurService()
cours_service = Cours_service()
inscription_service = InscriptionService()


# =========================
# FONCTIONS UTILITAIRES
# =========================
def afficher_details_cours(code_cours):
    cours = next((c for c in cours_service.cours if c.code_cours == code_cours), None)
    if not cours:
        print("❌ Cours introuvable.")
        return

    enseignant = next((u for u in user_service.utilisateurs if u["id"] == cours.enseignant_id), None)
    administrateur = next((u for u in user_service.utilisateurs if u["id"] == cours.administrateur_id), None)

    print("\n📘 DÉTAILS DU COURS")
    print(f"Code : {cours.code_cours}")
    print(f"Titre : {cours.titre}")
    print(f"Enseignant : {enseignant['nom'] if enseignant else 'Inconnu'}")
    print(f"Administrateur : {administrateur['nom'] if administrateur else 'Inconnu'}")
    print(f"Capacité restante : {cours.capacite_cours}")

    print("\n👨‍🎓 Étudiants inscrits :")
    if not cours.etudiants_inscrits:
        print("Aucun étudiant.")
    else:
        for u in user_service.utilisateurs:
            if u["id"] in cours.etudiants_inscrits:
                print(f"- {u['nom']} ({u['email']})")


# =========================
# MENU
# =========================
def menu():
    print("\n===== MENU GESTION ACADÉMIE =====")
    print("1️⃣ Ajouter un utilisateur")
    print("2️⃣ Ajouter un cours")
    print("3️⃣ Inscrire un étudiant à un cours")
    print("4️⃣ Afficher les détails d’un cours")
    print("5️⃣ Supprimer un cours")
    print("6️⃣ Chercher un cours")
    print("7️⃣ Désinscrire un étudiant d'un cours")
    print("8️⃣ Supprimer un utilisateur")
    print("9️⃣ Chercher un utilisateur")
    print("10 Quitter")


# =========================
# BOUCLE PRINCIPALE
# =========================
while True:
    menu()
    try:
        choix = int(input("Votre choix : "))
    except ValueError:
        print("❌ Veuillez entrer un nombre valide.")
        continue

    # 1️⃣ Ajouter un utilisateur
    if choix == 1:
        nom = input("Nom : ")
        email = input("Email : ")
        role = input("Rôle (Etudiant / Enseignant / Administrateur) : ")

        user = user_service.ajouter_utilisateur(nom, email, role)
        if user:
            print(f"✅ {role} ajouté avec succès.")

    # 2️⃣ Ajouter un cours
    elif choix == 2:
        code = input("Code du cours : ")
        titre = input("Titre du cours : ")
        capacite = int(input("Capacité du cours : "))

        enseignants = [u for u in user_service.utilisateurs if u["role"] == "Enseignant"]
        admins = [u for u in user_service.utilisateurs if u["role"] == "Administrateur"]

        if not enseignants or not admins:
            print("❌ Il faut au moins un enseignant et un administrateur.")
            continue

        print("\nEnseignants :")
        for e in enseignants:
            print(f"- {e['id']} : {e['nom']}")

        ens_id = input("ID de l'enseignant : ")

        print("\nAdministrateurs :")
        for a in admins:
            print(f"- {a['id']} : {a['nom']}")

        admin_id = input("ID de l'administrateur : ")

        # objets temporaires simples
        class Tmp:
            def __init__(self, identifiant):
                self.identifiant = identifiant

        cours_service.ajouter_cours(
            code,
            titre,
            Tmp(ens_id),
            Tmp(admin_id),
            capacite
        )

        print("✅ Cours ajouté avec succès.")

    # 3️⃣ Inscrire un étudiant
    elif choix == 3:
        code_cours = input("Code du cours : ")
        etu_id = input("ID de l'étudiant : ")

        inscription_service.inscrire_etudiant(code_cours, etu_id)

    # 4️⃣ Afficher les détails d’un cours
    elif choix == 4:
        code_cours = input("Code du cours : ")
        afficher_details_cours(code_cours)
    
    # 5  supprimer un cours
    elif choix == 5:
        code_cours = input("Code du cours à supprimer : ")
        cours = cours_service.chercher_cours(code_cours)
        if cours:
            cours_service.supprimer_cours(code_cours)
            print("✅ Cours supprimé avec succès.")
        else:
            print("❌ Cours introuvable.")

    # 6 chercher un cours
    elif choix == 6:
        code_cours = input("Code du cours à chercher : ")
        cours = cours_service.chercher_cours(code_cours)
        if cours:
            print(f"✅ Cours trouvé : {cours.titre} (Capacité restante : {cours.capacite_cours})")
        else:
            print("❌ Cours introuvable.")
    
    # 7 desinscrire un étudiant
    elif choix == 7:
        code_cours = input("Code du cours : ")
        etu_id = input("ID de l'étudiant : ")

        inscription_service.desinscrire_etudiant(code_cours, etu_id)
        print("etudiant désinscrit avec succès.")

    # 8 supprimer un utilisateur
    elif choix == 8:
        ID = input("ID de l'utilisateur à supprimer : ")
        if user_service.supprimer_utilisateur(ID):
            print("✅ Utilisateur supprimé avec succès.")
        else:
            print("❌ Utilisateur introuvable.")
    # 9 chercher un utilisateur
    elif choix == 9:
        ID = input("ID de l'utilisateur à chercher : ")
        user = user_service.chercher_utilisateur(ID)
        if user:
            print(f"✅ Utilisateur trouvé : {user['nom']} ({user['role']})")
        else:
            print("❌ Utilisateur introuvable.")

    # 10 Quitter
    elif choix == 10:
        print("👋 Au revoir !")
        break

    else:
        print("❌ Choix invalide.")
