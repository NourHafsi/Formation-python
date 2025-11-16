#1. Afficher la table de multiplication d’un nombre saisi par l’utilisateur.
""" n=int(input("donner un nombre: "))
print("la table de multiplication de",n,"est: ")
for i in range(1,10):
    t=n*i
    print(n,"*",i,"=",t) """
#2. Écrire un programme qui affiche les 10 premiers nombres naturels (0, 1, 2, 3, 4, 5, 6, 7, 8, et 9) en ordre décroissant (9, 8, 7, 6, 5,
#  4, 3, 2, 1, 0).
""" for i in range (9,-1,-1):
    print(i) """
#methode 2 avec while:
""" i=9
while i>=0:
    print(i)
    i-=1 """

#3.Afficher les 20 premiers nombres premiers (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67 et 71).
# Définir un nombre premier : Un nombre premier est un entier naturel supérieur ou égal à 2 qui possède exactement deux diviseurs : 
# 1 et lui-même.
""" nbre_premiers = []  # Liste pour stocker les nombres premiers
n = 2  # Commencer avec le premier nombre premier (2)

while len(nbre_premiers) < 20:  # Tant qu'on n'a pas trouvé 20 nombres premiers
    premier = True  # On suppose que n est premier
    for i in range(2, n):  # On teste les diviseurs de 2 à n-1
        if n % i == 0:  # Si n est divisible par i, ce n'est pas un nombre premier
            premier = False
            break  # Si n est divisible, on arrête la recherche de diviseurs pour ce n
    
    if premier:  # Si n est premier, on l'ajoute à la liste
        nbre_premiers.append(n)
    
    n += 1  # Passer au nombre suivant

# Afficher les 20 premiers nombres premiers
print(nbre_premiers) """
#4. Écrire un programme qui calcule la factorielle d’un nombre n.
""" n=int(input("donner un nombre: "))
f=1
for i in range(1,n+1):
    f=f*i
print(f) """
#5. Afficher la suite des 10 premiers nombres de Fibonacci(0, 1, 1, 2, 3, 5, 8, 13, 21 et 34).
""" 
Termes :     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
cal:       0, 1, 0+1=1, 1+1=2, 2+1=3, 3+2=5, 5+3=8, 8+5=13, 13+8=21, 21+13=34,
0,
1,
0+1=1, 
1+1=2, 
2+1=3, 
3+2=5, 
5+3=8, 
8+5=13, 
13+8=21, 
21+13=34 ...
Position :   1  2  3  4  5  6  7   8   9   10

"""
""" f0=0
f1=1
for i in range(10): # for _ in range(10)
    print(f0)

    fn=f0+f1
    f0=f1
    f1=fn
 """
#deuxieme methode : 
NbFibo = [0, 1]  # On commence avec les deux premiers nombres

while len(NbFibo) < 10:  # Tant qu'on n'a pas 10 nombres
    suivant = NbFibo[-1] + NbFibo[-2]  # On ajoute les deux derniers
    NbFibo.append(suivant)  # On ajoute le résultat à la liste

print(NbFibo)
#6. Vérifier si une chaîne est un palindrome(si elle peut 
# être lue de la même manière de gauche à droite et de droite à gauche).

ch= input("donner une chaine: ")

