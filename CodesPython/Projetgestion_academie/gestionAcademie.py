from Services.utilisateur_service import *
from Services.cours_service import *
from Services.inscription_service import * 
#creation des objets:
user=  UtilisateurService()
cour= Cours_service()
insc= InscriptionService()
ens= user.ajouter_utilisateur("Ali","alimahmoud@gmail.com","Enseignant")
python= cour.ajouter_cours("py11", "cours python", ens, 10)
#ajouter etudiant1:
etu1= user.ajouter_utilisateur("Mouna","amouna@gmail.com","Etudiant")
#inscription du etudiant:
insc.inscrire_etudiant(python, etu1)
insc.lister_etudiants_inscrits(python)
print(f"L'étudiant {etu1.nom} est inscrit au cours {python.titre} enseigné par {python.enseignant.nom}.")
print ("Liste des étudiants inscrits au cours:", insc.lister_etudiants_inscrits(python))
