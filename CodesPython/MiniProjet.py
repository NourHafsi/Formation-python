etudiant={}
def ajout_etudiant():
    matricule=input("donner la matricule de l'etudiant: ")
    Nom= input("donner le nom de l'etudiant: ")
    Prenom= input("donner le prenom de l'etudiant: ")
    Note= input("donner la Note de l'etudiant: ")
    etudiant={}
    if matricule in etudiant:
        print("cet etudiant existe deja ! ")
    else: 
    # ajout des elements dans mon dictionnaire:
        """ etudiant['matricule']= matricule
        etudiant['Nom']= Nom
        etudiant['Prenom']= Prenom
        etudiant['Note']= Note """
        etudiant[matricule] = {
            'Nom': Nom,
            'Prenom': Prenom,
            'Note': Note
        }
    return etudiant

#fonction afficher tous les etudiants:
def affich_etudiants():
   if etudiant:          #le dectionnaire existe non pas vide
       for matricule, infos in etudiant.items():
            print(f"Matricule: {matricule} | Nom: {infos['Nom']} | Prénom: {infos['Prenom']} | Note: {infos['Note']}")
       """ for Nom,Prenom,Note in etudiant.items:
           print("le nom de l'etudiant:",Nom,"le prenom de l'etudiant:",Prenom,"la note de l'etudiant:",Note) """
   else:
       print("pas d'etudiants ajoutés pour qu'on puisse l'afficher")


def Menu():
    print("c'est le menu principal")
    print("1: ajouter etudiant")
    print("2: modifier etudiant")
    print("3: supprimer etudiant")
    print("4: afficher tous les etudiants")
    print("5: Quitter")

while True:
        Menu()
        x=int(input("donner moi votre choix: "))
        if x==1:
            ajout_etudiant()
        elif x==2:
            print(x)
            #modif_etudiant()
        elif x==3:
            print(x)
            #supp_etudiant()
        elif x==4:
            affich_etudiants()
        elif x==5:
            print("Au revoir ! ")
            break
        else:
            print("choix invalid, tu dois choisir de 1 à 5 ! ")
        





