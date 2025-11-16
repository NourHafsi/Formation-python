#16. Écrire une fonction qui convertit un dictionnaire {clé: [valeurs]} en un dictionnaire inversé
# {valeur: clé} (chaque valeur devient clé).

""" def convert_dict(dictionnaire): 
    dict_inverse = {}  # Nouveau dictionnaire pour stocker l'inversion
    
    # Parcourir chaque clé et sa liste de valeurs
    for cles, valeurs in dictionnaire.items():
        for valeur in valeurs:
            dict_inverse[valeur] = cles  # Inverser la relation
    return dict_inverse

# Dictionnaire d'exemple à convertir
dictionnaire = {
    'A': [1, 2],
    'B': [3, 4]
}

# Appel de la fonction et récupération du résultat
resultat = convert_dict(dictionnaire)

# Affichage du résultat dans le terminal
print("Dictionnaire inversé :", resultat)

 """
#17. Crée une fonction qui demande à l’utilisateur un entier 
# strictement positif, et redemande tant que l’entrée est invalide (gestion ValueError).

""" def entier_strictposi():
    while True:
        try:
            n = int(input("Donnez un entier strictement positif : "))
            if n > 0:
                return n
            else:
                print("Erreur : l'entier doit être strictement positif.")
        except ValueError:
            print("Erreur : vous devez entrer un entier valide.")

n = entier_strictposi()
print(f"Bravo ! Vous avez saisi un entier strictement positif : {n}") """

#18. Écrire une fonction safe_division(a, b) qui :
#● Retourne a / b
#● Gère la division par zéro et les types invalides (avec try...except).
""" def safe_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Erreur : division par zéro.")
    except TypeError:
        print("Erreur : les deux valeurs doivent être des nombres.")


try:
    a = float(input("Donnez un numérateur: "))
    b = float(input("Donnez un dénominateur: "))
    resultat = safe_division(a, b)

    if resultat is not None:
        print("Résultat :", resultat)
except ValueError:
    print("Erreur : vous devez entrer des nombres valides.") """