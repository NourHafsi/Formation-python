#19. Écrire une fonction qui lit un fichier JSON et gère les erreurs suivantes :
#● Fichier introuvable
#● Format JSON invalide
#● Erreur de clé manquante

""" import json
def lire_fichier(F,cles):
    try:
        with open(F,"r",encoding="utf-8") as file:
            data=json.load(file)
            print(data[cles])
    except FileNotFoundError: # Fichier introuvable
        print("Fichier introuvable ! ")
    except json.JSONDecodeError: # Format JSON invalide
        print("Format JSON invalide ! ")
    except KeyError: # Erreur de clé manquante
        print("Erreur de clé manquante ! ")

lire_fichier("ex19.json","age")  """

#lire_fichier("ex199.json","age") : pour detecter l'erreur Fichier introuvable ! 
# dans le fichier json si je mets ca "{ "name": "John Doe", "age": 35 }hhhhhhhhhhhhhhhhhh" 
#  j'ai l'erreur Format JSON invalide !
#lire_fichier("ex19.json","age") : avoir un cle valide donc il retourne la valer de cle : 35 
# si on mets lire_fichier("ex19.json","adresse") clé qui n'existe pas donc on
#  aura l'erreur Erreur de clé manquante ! 

