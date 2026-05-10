""" 
Exercice :
1.Crée un fichier produits.csv avec les colonnes : nom, prix,
quantite.
2.Ajoute 3 produits dans le fichier.
3.Lis le fichier et affiche le total de chaque produit (prix *
quantite).
4.Enregistre le résultat dans un fichier total.json. """


import csv
import json

# Étape 1 : Créer le fichier CSV
produits = ["nom", "prix", "quantite"]

with open("produits.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=produits)
    writer.writeheader()

    # Étape 2 : Ajouter 3 produits
    writer.writerow({"nom": "tomate", "prix": 3.5, "quantite": 5})
    writer.writerow({"nom": "pomme", "prix": 4.5, "quantite": 10})
    writer.writerow({"nom": "pain", "prix": 1.0, "quantite": 2})

# Étape 3 : Lire le fichier et calculer les totaux
totaux = []

with open("produits.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = float(row["prix"]) * int(row["quantite"])
        totaux.append({
            "nom": row["nom"],
            "total": total
        })
        print(f"Total pour {row['nom']} : {total}")

# Étape 4 : Enregistrer dans un fichier JSON
with open("total.json", mode="w") as file:
    json.dump(totaux, file, indent=4)




