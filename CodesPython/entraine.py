#1. Afficher la table de multiplication d’un nombre saisi par l’utilisateur.
""" n=int(input("donner un nombre : "))
print("La table de multiplication de", n, "est: ")
for i in range(1,11):
    T=n*i
    print(n,"*",i,"=",T) """

#2. Écrire un programme qui affiche les 10 premiers nombres naturels (1,2,3,4,5,6,7,8,9,10) en ordre décroissant.
""" for n in range(10,0,-1): #range(start, stop, step)
    print (n)  """   #ou ca espacés dans la meme ligne "print(n, end=" ")""

#3. Afficher les 20 premiers nombres premiers: sont(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
# a pour diviseurs 1 et lui-même
""" n=2
c=0
while c<20:
    p=True
    for x in range (2,n):
        if n%x == 0:
            p=False
            break
    if p==True:
        print(n,end=" ") 
        c += 1
    n += 1 """
#4. Écrire un programme qui calcule la factorielle d’un nombre n: n!=1*2*3*....*n
""" n=int(input("donner un nombre : "))
f=1
for i in range(1,n+1):
    f=f*i
print(f)
 """
#5. Afficher la suite des 10 premiers nombres de Fibonacci.
#Les 10 premiers nombres de Fibonacci sont(0,1,1,2,3,5,8,13,21,34). Pour trouver la suite,
#  on commence avec F0=(0) et F1=(1) , puis chaque nombre suivant est la somme des deux nombres précédents
#  (Fn=Fn-1+Fn-2). 
#          F0=0
#          F1=1
#F2=F1+F0=1+0=1
#F3=F2+F1=1+1=2
#F4=F3+F2=2+1=3
#F5=F4+F3=3+2=5
#F6=F5+F4=5+3=8
#F7=F6+F5=8+5=13
#F8=F7+F6=13+8=21
#F9=F8+F7=21+13=34
""" a = 0
b = 1
for i in range(10):
    print(a)
    temp = a + b 
    a = b
    b = temp """
#6. Vérifier si une chaîne est un palindrome.
""" ch= input("donner une chaine : ")
n=len(ch)
p=True
for i in range(n//2):
    if ch[i] != ch[n-1-i]:
        p=False
        break
if p:
    print ("la chaine est palindrome")
else: 
    print ("la chaine n'est pas palindrome") """

#2eme methode: 
""" ch= input("donner une chaine : ")
inv=""
for x in ch:
    inv=x+inv   #autre methode ch[::-1]:
print(inv)
if ch == inv:
    print ("la chaine est palindrome")
else:
    print("la chaine n'est pas palindrome") """
#7. Écrire un programme qui compte combien de mots dans une phrase.
""" ch=input("donner une chaine: ")
c=1
n=len(ch)
for i in range(n):
    if ch[i]==" ":
        c+=1
print("le nombre de mots dans cette phrase:", c) """
#8. Demander un mot et afficher ses lettres en ordre inverse.
""" ch=input("donner un mot: ")
inv=""
for i in ch:
    inv=i+inv
print ("le mot inversé est : ",inv) """
#9. Écrire un programme qui affiche combien de fois une lettre donnée apparaît dans une phrase.
""" chaine=input("donner une chaine : ")
ch1=input("donner une lettre : ")
c=0
for ch in chaine:
    if ch == ch1:
        c+=1
print(c)  """ 

#10. Supprimer les espaces d’une chaîne
""" ch=input("donner une chaine: ")
ch_mot=""
for c in ch:
    if c != " ":
        ch_mot+=c
print(ch_mot) """

#11. Écrire un programme qui affiche chaque mot d’une phrase sur une nouvelle ligne.
""" ch=input("donner une chaine: ")
mot=""
for c in ch:
    if c != " ":
        mot+=c
    else:
        print(mot)
        mot=""
print(mot) """ 

#12. Afficher la somme des diagonales d’un carré (matrice carré) de taille n.
""" matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = len(matrice)
somme_principale = 0
somme_secondaire = 0
for i in range(n):
    somme_principale += matrice[i][i]
    somme_secondaire += matrice[i][n - 1 - i]

print("Somme diagonale principale :", somme_principale)
print("Somme diagonale secondaire :", somme_secondaire)
somme_totale = somme_principale + somme_secondaire
# Si la matrice a un nombre impair de lignes/colonnes, 
# il faut soustraire l’élément central une fois (il a été compté deux fois)
if n % 2 != 0:
    centre = matrice[n // 2][n // 2]
    somme_totale -= centre

print("Somme totale des deux diagonales (sans double-comptage) :", somme_totale) """
#2eme methode: 
""" n = int(input("Taille: "))
mat = []
for i in range(n):
    ligne = []
    for j in range(n):
        ligne.append(int(input(f"Entrez mat[{i}][{j}]: ")))
    mat.append(ligne)
    
s = 0
for i in range(n):
    s += mat[i][i] + mat[i][n-1-i]
print("Somme diagonales =", s) """

#13. Afficher tous les couples (i, j) pour i et j entre 1 et 5.
""" for i in range(1,6):
    for j in range(1,6):
        print("(",i,",",j,")",end=" ") """
#14. Afficher une table de multiplication sous forme de tableau.
""" for i in range(1,11):
    for j in range(1,11):
        print(i*j, end="\t") #le saut de ligne par défaut par une tabulation horizontale (\t)
    print()
  """
#15. Afficher un triangle de Pascal jusqu’à n lignes.
""" n = int(input("Donner le nombre de lignes : "))
triangle = []
for i in range(n):
    ligne = [1]  # Chaque ligne commence par 1
    if i > 0:
        for j in range(1,i):
            # Chaque élément est la somme des deux au-dessus
            ligne.append(triangle[i-1][j-1] + triangle[i-1][j])
        ligne.append(1)  # Chaque ligne finit aussi par 1
    triangle.append(ligne) """

# Affichage 
""" for ligne in triangle:
    for x in ligne:
        print(x, end=" ")  # Affiche chaque nombre suivi d’un espace
    print()  # Va à la ligne après chaque ligne du triangle """

#16. Calculer le plus petit commun multiple (PPCM) de deux nombres avec boucles.
# PPCM de 10 et 12.
#  Multiples de 10: 10,20,30,40,50,60,70,.....
# Multiples de 12: 12,24,36,48,60,72,...
# Le plus petit multiple commun est 60
""" a = int(input("Entrer le premier nombre : "))
b = int(input("Entrer le deuxième nombre : "))
ppcm = max(a, b)

while True:
    if ppcm % a == 0 and ppcm % b == 0:
        print("Le PPCM de", a, "et", b, "est :", ppcm)
        break  # Sort de la boucle while dès qu'on trouve le PPCM
    else:
        print("Test échoué pour :", ppcm)
        ppcm += 1 """

#17. Calculer le plus grand commun diviseur (PGCD) avec boucles.
""" a = int(input("Entrer le premier nombre : "))
b = int(input("Entrer le deuxième nombre : "))
PGCD = min(a, b)

while True:
    if a % PGCD == 0 and b % PGCD ==0:
        print("Le PGCD de", a, "et", b, "est :", PGCD)
        break  # Sort de la boucle while dès qu'on trouve le PPCM
    else:
        print("Test échoué pour :", PGCD)
        PGCD -= 1  """    
#meth2: 
""" a = int(input("Entrer le premier nombre : "))
b = int(input("Entrer le deuxième nombre : "))

pgcd = 1  # Valeur initiale

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        pgcd = i  # Mettre à jour si c’est un diviseur commun

print("Le PGCD de", a, "et", b, "est :", pgcd) """
#################################################################################################################

#18. Vérifier si un nombre est parfait (somme de ses diviseurs = lui-même).
""" n=int(input ("donner un nombre\n"))
S=0
for i in range(1,n):
    if n%i==0:
        S+=i
if S == n:
    print(f"{n} est un nombre parfait")
else:
    print(f"{n} n'est pas un nombre parfait") """

#19. Vérifier si un nombre est un nombre d’Armstrong (ex : 153 → 1³+5³+3³=153).
""" chn=input("donner un nombre\n")
p=len(chn)
S=0
for i in range(p):
    S+=int(chn[i])**p
if S == int(chn):
    print("c'est un nombre d’Armstrong")
else:
    print("ce n'est pas un nombre d’Armstrong") """

#20. Écrire un programme qui génère la suite de Collatz pour un nombre donné.
""" n=int(input("donner un nombre\n"))
while n!=1:
    if n%2 == 0:
        print(n,"/",2,"=",n/2)
        n= n/2
    else:
        print(n,"*3 + 1=",n*3+1)
        n= n*3 + 1 """

#21. Écrire un programme qui affiche tous les nombres premiers jusqu’à 1000.
# (superieur à 1 et qui est divisible par 1 et lui meme)
""" n = 2
while n < 1000:
    est_premier = True  # on suppose d'abord que le nombre est premier

    for i in range(2, n):
        if n % i == 0:
            est_premier = False  # trouvé un diviseur
            break  # pas besoin de continuer à vérifier

    if est_premier == True:
        print(n)

    n += 1  # n = n + 1 pour passer au nombre suivant """

#22. Écrire un programme qui calcule la puissance a^b en utilisant une boucle.
""" a= int(input("a="))
b= int(input("b="))
r=1
for i in range(b):
    r=r*a
print("a^b =", r) """

#23. Écrire un programme qui calcule la moyenne d’une série de nombres 
# entrés par l’utilisateur (fin si -1).
""" n=int(input("donner un nombre different de -1 car -1 fait fin à la demande de nombres entrés par l’utilisateur \n "))
S=0
c=0
while n != -1:
    S+=n
    c+=1
    n=int(input("donner un nombre different de -1 car -1 fait fin à la demande de nombres entrés par l’utilisateur \n "))
if c > 0:
    moy = S / c
    print("La moyenne est :", moy)
else:
    print("Aucun nombre entré car la fin c'est -1.") """
#24. Écrire un programme qui génère une pyramide numérique (1, 22, 333, …).
""" n=int(input("donner un nombre: " ))
for i in range(1, n+1):
    print(str(i)*i) """

#2eme methode: 
""" n=int(input("donner un nombre: " ))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ") # end=" ": on met un espace.
    print() # saut de ligne après chaque ligne de i répété """

#25. Écrire un programme qui trouve le premier nombre supérieur à 1000 qui est divisible par 17, 19 et 23.
""" n= 1001
while True:
    if n%17 == 0 and n%19 == 0 and n%23 == 0:
        print(f"{n} est le premier nombre supérieur à 1000 qui est divisible par 17, 19 et 23")
        break
    n+=1 """

#26. Générer un triangle de * de hauteur donnée.
""" n=4 
(i=0,1,2,3)
(i=0,j=0)
(i=1,j=0,1)
(i=2,j=0,1,2)
(i=3,j=0,1,2,3)
i=0 *
i=1 **
i=2 ***
i=3 **** """
#code:
""" n=int(input ("donner la taille de triangle: " ))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()  #pour aller à la ligne après chaque rangée """

#27. Écrire un programme qui affiche la suite de Collatz d’un nombre(est une suite d'entiers où l'on applique des règles successives : 
# si le nombre est pair, on le divise par \(2\) ; si le nombre est impair, on le multiplie par \(3\) et on ajoute \(1\). La conjecture 
# de Collatz affirme que, quelle que soit le nombre entier de départ, la suite finit toujours par atteindre le nombre \(1\)).
""" n = int(input("Donner un nombre : "))
while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(f"n égale à : {n}") """

#28. Écrire un programme qui affiche une pyramide de nombres (1, 22, 333, …).
""" n=int(input ("donner la taille de triangle: " ))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ") #ajoute un espace après chaque chiffre, pour les séparer proprement.
    print()  #pour aller à la ligne après chaque rangée """

#une version centrée de pyramide de nombres :
""" n = int(input("Donner la taille de la pyramide : "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")  # Afficher les espaces avant les nombres pour centrer
    for j in range(i): # Afficher le nombre i répété i fois (avec un espace entre chaque)
        print(i, end=" ") #ajoute un espace après chaque chiffre, pour les séparer proprement.
    print()  # aller à la ligne après chaque rangée """
# Code sans espaces entre les chiffres:
""" n = int(input("Donner la taille de la pyramide : "))
for i in range(1, n + 1):
    print(" " * (n - i), end="") # Espaces avant pour centrer la pyramide.Si on n’avait pas 
    #mis end="", les espaces apparaîtraient sur une ligne séparée,
    # Affichage du nombre i répété i fois, collé
    print(str(i) * i)  ## affiche les chiffres et **retourne automatiquement à la ligne**
    # pas besoin de end="" ici car print() ajoute déjà un retour à la ligne. 
    #Par défaut, elle finit par un retour à la ligne, donc la prochaine itération de la boucle 
    # commence sur la ligne suivante. """

#29. Écrire un programme qui affiche tous les couples (i, j) avec i, j de 1 à 5.
""" for i in range (1,6):
    for j in range(1,6):
        print(f"({i},{j})",end=" ") """

#30. Demander un nombre n et afficher tous les nombres premiers ≤ n (diviseurs positifs : 1 et lui-même).
""" n= int(input("donner un nombre\n"))
for pre in range(2,n+1): # Boucle sur tous les nombres de 2 à n
    is_premier=True      # On suppose que le nombre pre est premier
    for i in range(2,pre): # Vérifier les diviseurs possibles de pre
        if pre % i == 0:   # Si pre est divisible par i
            is_premier = False # pre n'est pas premier
            break              # On peut arrêter la boucle
    if is_premier == True:
        print(pre, end=" ")     # Affiche pre s'il est premier """

#31. Vérifier si un nombre est palindrome (ex : 121 → oui, 123 → non).
""" ch_n=input("donner un nombre: ")  #"121"
ch_inverse=""
for i in ch_n:
    ch_inverse=i+ch_inverse
if ch_n == ch_inverse:
    print("Le nombre est palindrome")
else:
    print("Le nombre n'est pas palindrome") """

#32. Calculer la somme des chiffres pairs d’un nombre.
""" ch_n= input("donner un nombre : ")  #exp: 136 ->"136"
S=0
for i in ch_n:
    chiffre = int(i)      # conversion du caractère en entier
    if chiffre%2 == 0:
        S=chiffre+S
print(S) """

#33. Compter combien de nombres de 1 à 1000 sont divisibles par 7 mais pas par 5.
""" c=0
for nom in range (1,1001):
    if nom % 7 == 0 and nom % 5 != 0:
        c+=1
print("Il y a", c, "nombres divisibles par 7 mais pas par 5 entre 1 et 1000.") """

#34. Écrire un programme qui invente un mot de passe de longueur n avec chiffres et lettres.
""" import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits  = "0123456789"
alphabet = letters + digits
n = int(input("Longueur du mot de passe : "))
password = ""

for _ in range(n): #“Je sais qu’il y a une variable ici, mais je ne vais pas
    # m’en servir. “Fais cette action n fois pour ajouter un caractère au mot de passe.””
    password += random.choice(alphabet)
print("Mot de passe :", password) """

#35. Écrire un programme qui retourne la position de la première voyelle dans un mot.
""" MOT= input("donner un mot: ") 
l=len(MOT)
voy= "aeiouyAEIOUY"
for i in range(l):
    if MOT[i] in voy:
        print("Première voyelle à la position :", i)
        break
    else:
        print("Aucune voyelle trouvée.") """

#36. Écrire un programme qui affiche les 20 premiers termes de la suite
#  de Fibonacci et vérifie lesquels sont pairs.
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, et 4181. 
# La suite commence par 0 et 1, F_{n}=F_{n-1}+F_{n-2}
a=0
b =1
for _ in range(20): # Boucle pour afficher les 20 premiers termes
    # Afficher le terme et s'il est pair ou impair
    if a % 2 == 0:
        print(a, "pair")
    else:
        print(a, "impair")
    # Calculer le terme suivant
    a= b
    b= a + b
#37. Écrire un programme qui affiche tous les nombres de 1 à 100, mais remplace :
# les multiples de 3 par "Fizz"
# les multiples de 5 par "Buzz"
# les multiples de 15 par "FizzBuzz".
""" for n in range(1, 101):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n) """