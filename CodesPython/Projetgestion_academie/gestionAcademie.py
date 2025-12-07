from Services.utilisateur_service import *
from Services.cours_service import *
from Services.inscription_service import * 
#creation des objets:
user=  UtilisateurSerice()
cour= Cours_service()
insc= Inscription()
ens= user.ajouter_utilisateur("Ali","alimahmoud@gmail.com","Enseignant")
python= cour.ajouter_cours("py11", "cours python", ens, 10)
#ajouter etudiant1:
etu1= user.ajouter_utilisateur("Mouna","amouna@gmail.com","Etudiant")
#inscription du etudiant:
insc.inscri_etudiant(python, etu1)
insc.lister_etudiantinscrits(python)
