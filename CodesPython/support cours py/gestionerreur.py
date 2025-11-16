#1. Demander un nombre à l’utilisateur et gérer s’il entre une chaîne.
""" try:
    n=int(input("doner un nombre: "))
    print("vous avez entré un nombre entier")
except:
    print("ce n'est pas nombre entier") """
#2. Écrire une fonction de division qui gère la division par zéro.
def division():
    try:
        a= int(input("donner le numerateur: "))
        b= int(input("donner le denominateur: "))
        print(a/b)
    except:
        print("erreur")
division()