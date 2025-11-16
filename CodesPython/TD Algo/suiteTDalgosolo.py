#6. Vérifier si une chaîne est un palindrome(si elle peut être lue de la 
# même manière de gauche à droite et de droite à gauche).
#3eme methode? avec for 
""" ch = input("Donner une chaine : ")
p = True
n = len(ch)

for i in range(n // 2):
    if ch[i] != ch[n - 1 - i]:
        p = False
        break

if p:
    print("La chaine est palindrome")
else:
    print("La chaine n'est pas palindrome") """
#9'. Écrire un programme qui affiche combien de fois un mot donnée apparaît dans une phrase.
#meth1:
""" ch= input("donner moi une phrase : ")
ch1= input("donner moi un mot : ")
compteur = 0
mots = ch.split()

for m in mots:
    if m == ch1:
        compteur = compteur + 1

print("Le mot",ch1, "apparaît", compteur, "fois.") """
#meth2: 
""" ch = input("donner moi une phrase : ")
ch1 = input("donner moi un mot : ")

compteur = 0
i = 0

while i <= len(ch) - len(ch1):
    if ch[i:i+len(ch1)] == ch1:
        compteur = compteur + 1
    i = i + 1

print("Le mot", ch1, "apparaît", compteur, "fois.") """
#12. Afficher la somme des diagonales d’un carré (matrice) de taille n.(d=AB"2 = CA"2 + CB"2)
#methode2:
""" n = int(input("Taille du carré (n) : "))
somme = 0

print("Entrer les", n, "nombres de la diagonale principale :")
for i in range(n):
    x = int(input(f"Nombre {i+1} : "))
    somme += x

print("Entrer les", n, "nombres de la diagonale secondaire :")
for i in range(n):
    y = int(input(f"Nombre {i+1} : "))
    somme += y

# Si n est impair, enlever le nombre du centre (le même dans les deux diagonales)
if n % 2 == 1:
    centre = int(input("Entrez le nombre au centre (déjà donné) : "))
    somme -= centre

print("Somme des diagonales =", somme) """
#exemple par 3 nombres: 
""" n = int(input("Taille du carré (n) : "))
somme = 0

print("Entrer les nombres de la diagonale principale :")
a = int(input("1er nombre : "))
b = int(input("2ème nombre : "))
c = int(input("3ème nombre : "))
somme = somme + a + b + c

print("Entrer les nombres de la diagonale secondaire :")
d = int(input("1er nombre : "))
e = int(input("2ème nombre : "))
f = int(input("3ème nombre : "))
somme = somme + d + e + f

# Si n est impair, il faut retirer le centre (ici, c’est le 2ème nombre de chaque diagonale : b ou e)
if n % 2 == 1:
    somme = somme - b  # ou - e, c’est le même

print("Somme des diagonales =", somme) """

#13. Afficher tous les couples (i, j) pour i et j entre 1 et 5.
""" for i in range(1,6):
    for j in range(1,6):
        print("l'ensemble des couples est: ",(i,j)) """
#14. Afficher une table de multiplication sous forme de tableau.
""" for i in range(1,10):
    for j in range(1,10):
        T=i*j
        print(f"{i} * {j}=" ,T, end="\t")  # afficher le résultat et rester sur la même ligne avec tabulation
    print()  # saut de ligne après chaque ligne de la table """
    #ou
""" for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}*{j}={i*j}", end="\t")
    print() """

#15. Afficher un triangle de Pascal jusqu’à n lignes.
""" 
n = int(input("Combien de lignes du triangle de Pascal voulez-vous afficher ? "))

# La liste triangle contiendra toutes les lignes du triangle.
triangle = []

# Initialiser la première ligne.
premiere_ligne = [1]
triangle.append(premiere_ligne)

# Construire les lignes suivantes jusqu'à n.
for i in range(1, n):
    ligne_precedente = triangle[i - 1]
    ligne_actuelle = [1]  # Chaque ligne commence par 1.

    # Calculer les éléments intermédiaires
    for j in range(len(ligne_precedente) - 1):
        somme = ligne_precedente[j] + ligne_precedente[j + 1]
        ligne_actuelle.append(somme)

    ligne_actuelle.append(1)  # Chaque ligne finit par 1.
    triangle.append(ligne_actuelle)

# Afficher le triangle ligne par ligne.
for ligne in triangle:
    print(ligne) """

#une autre solution? 
#fontion ppcm et pgcd in python ???????????????????
#PPCM:
#while True	Lance une boucle infinie.
# break	Stoppe la boucle quand on a trouvé ce qu’on cherchait.
# Avantage	Pas besoin de connaître d’avance combien d’itérations seront faites.
#  Cette ligne crée une boucle infinie. Cela signifie que Python va exécuter les instructions
# à l’intérieur du bloc encore et encore, sans fin, sauf si on l'arrête nous-mêmes.Donc, 
# pour ne pas tourner pour toujours, on doit
# mettre une condition à l'intérieur pour "casser" la
# boucle quand on a fini — c’est là qu’intervient break. 
""" a=int(input("donner un nombre:"))
b=int(input("donner un nombre: "))
i=1
while True:
    M=a*i
    if M%b == 0:
        print(M, "est le PPCM de :",a,"et",b)
        break
    i+=1 """

#PGCD:
""" a=int(input("donner un nombre:"))
b=int(input("donner un nombre:"))
for i in range(1,min(a, b)+1):
    if a % i == 0 and b % i == 0:
        pgcd=i
print(pgcd,"est le PGCD de :",a,"et",b) """

#22. Écrire une fonction qui calcule la puissance a^b en utilisant une boucle.
""" def puissance(a,b):
    p=1
    for i in range(1,b+1):
        p=p*a
    print("la puissance de",a,"^",b,"=",p)   
a=int(input("donner un nombre:"))
b=int(input("donner un nombre pour l'tiliser en tant que puissance:"))
puissance(a,b) """

#autre methode: 
""" def puissance(a, b):
    p = 1
    for i in range(1, b + 1):
        p = p * a
    return p

a = int(input("Donner un nombre: "))
b = int(input("Donner un exposant: "))
resultat = puissance(a, b)
print("La puissance de", a, "^", b, "=", resultat) """

#23. Écrire une fonction qui calcule la moyenne d’une série de nombres entrés par l’utilisateur (fin si -1).

""" Exemple d’ordre des opérations dans ta tête :
S = 0, C = 0
Demander n
Tant que n != -1:
  - ajouter n à S
  - augmenter C de 1
  - demander un nouveau n
Calculer la moyenne M = S / C
Afficher M """

""" def moyenne(n):
    S = 0
    C = 0
    while n!=-1:
        S=S+n
        C+=1
        n=int(input("donner un nombre: "))
    if C>0:
        M=S/C
        print("la moyenne de",C, "nombres données par l'utilisateur est egale: ",M)
    else:
        print("Aucun nombre valide n'a été entré.")
n = int(input("donner un nombre: "))
moyenne(n) """

#2eme approche:
""" def moyenne():
    S = 0
    C = 0
    while True:
        n = int(input("Donner un nombre (-1 pour arrêter) : "))
        if n == -1:
            break
        S += n
        C += 1
    if C > 0:
        M = S / C
        print("La moyenne de", C, "nombres données par l'utilisateur est égale:", M)
    else:
        print("Aucun nombre valide n'a été entré.")

moyenne() """
