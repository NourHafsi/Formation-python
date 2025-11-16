#ex1: Afficher la table de multiplication d’un nombre saisi par l’utilisateur.
""" intput: nombre saisi par l'utilisat
output: table de mutiplic: 10 nombres
prob: calculer et afficher la table de mutiplic

Tasks:
- input un nombre n
- parcourir une boucle for de i variable de range (1,11) :
     - t=i*n
     - print (T) """

#code:
""" n= int(input("donner un nombre: "))
print("la table de multiplication de ",n , "est:\n")
for i in range(11):
    t=i*n
    print(n,"*",i,"=",t) """

#ex2: Écrire un programme qui affiche les 10 premiers nombres naturels en ordre décroissant.
""" input: 10 premiers nombres naturels
output: 10 premiers nombres naturels decroisants
prob: inverser les nombres et les afficher  """
""" range(start, stop, step) : génère une séquence de nombres.
start = 10 => commence à 10
stop = 0 =>s’arrête avant 0 (0 n’est pas inclus)
step = -1 => descend de 1 à chaque itération """


""" for i in range(10,-1,-1):
    print(i) """

#2eme methode: 
""" i=10
while i>=0:
    print(i)
    i=i-1 #i-=1 """

#ex3: Afficher les 20 premiers nombres premiers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71. 
""" input : deux variables initialisé : 2 et l'autre à 0
output: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71
prb: calculer les 20 premiers nombres premiers et les afficher
tasks: 
- initialisation n=2 ; c=0
- deux boucles à utiliser : 
1ere boucle : boucle while jusqu'a c>=20' 
for x in range(2)
- if n% x==0 """

""" n=2
c=0
while c<20:
    p=True
    for x in range(2,n):
        if n%x==0:
            p=False
            break
    
    if p==True:
        print(n)
        c=c+1
    n=n+1 """

#ex4: Écrire un programme qui calcule la factorielle d’un nombre n.

""" input: donner un nombre quelquonce
output: valeur de la factorielle
prb: calculer la factorielle w affichih . exp : 3!=3*2*1=6

tasks: 
- input int
- for i in range(1,n): 3
f=3*1
f=3*2
f=6
f=n*i
-output : nombre factoriel """
""" n=int(input("donner un nombre\n"))
f=1
for i in range(1,n+1):
    f=f*i
print("factorielle egale:",f) """


# à faire deuxieme methode du factorielle par la boucle while ? 
""" n=int(input("donner un nombre n\n"))
f=1
i=1
while i<=n:
    f=i*f
    i+=1
print(f) """
#ex5: Afficher la suite des 10 premiers nombres de Fibonacci: 0, 1(0+1), 2(1+1), 2(1+1), 3(1+2), 5(.....), 8, 13, 21, 34
""" a=0
b=1
for c in range(10):
    print(a,b)
    x=a+b
    a=b
    b=x """

#6. Vérifier si une chaîne est un palindrome(si elle peut être lue de la 
# même manière de gauche à droite et de droite à gauche).
""" ch= input("donner une chaine: ")
chi=""
for x in ch:
    chi=x+chi
print(chi)
if chi==ch:
    print("La chaine est palindrome")
else:
    print("La chaine n'est pas palindrome")  """
#2eme methode:

""" ch= input("donner une chaine: ")
p=True
g=len(ch)-1
print(g)
i=0
while i<g:
    if ch[i]!=ch[g]:
        p=False
        break
    i+=1
    g-=1
if p:
    print("La chaine est palindrome")
else:
    print("La chaine n'est palindrome") """
#3eme methode? avec for 
#7. Écrire un programme qui compte combien de mots dans une phrase.
""" ch= input("donner une chaine: ")
c=1
for i in ch:
    if i==" ":
        c=c+1
print(c) """

""" ch= input("donner une chaine: ")
i=0
c=1
while i<len(ch):
    if ch[i] ==" ":
        c=c+1
    i+=1
print(c) """
#8. Demander un mot et afficher ses lettres en ordre inverse.
""" ch= input("donner une chaine: ")
ch1=""
for i in ch:
    ch1=i+ch1
print(ch1) """
#9. Écrire un programme qui affiche combien de fois une lettre donnée apparaît dans une phrase.
""" ch= input("donner moi une phrase: ")
char= input("donner moi une lettre a chercher dans une phrase: ")
c=0
for i in ch:
    if i == char:
        c+=1
print(c) """
#9'. Écrire un programme qui affiche combien de fois un mot donnée apparaît dans une phrase.
#10. Supprimer les espaces d’une chaîne

""" ch= input("donner une chaine: ")
ch1=""
for i in ch:
    if i != " ":
        ch1=ch1+i
print(ch1) """
#2eme methode:
""" ch= input("donner une chaine: ")
ch1=ch.replace(" ", "")
print(ch)
print(ch1) """
#2' methode
""" ch= input("donner une chaine: ")
ch=ch.replace(" ", "")
print(ch) """
#11. Écrire un programme qui affiche chaque mot d’une phrase sur une nouvelle ligne.
""" ch= input("donner une chaine: ")
m=""
for i in ch:
    if i != " ":
        m=m+i
    else:
        print("le mot est: ",m)
        m=""
print(m) """
#12. Afficher la somme des diagonales d’un carré (matrice) de taille n.(d=AB"2 = CA"2 + CB"2)
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
print("Somme diagonales =", s)
 """

#15. Afficher un triangle de Pascal jusqu’à n lignes.
""" Input: entité n : exp n=6
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
   1 5 10 10 5 1
Output: triangle de pascal de n lignes
prb: 
1-input/-2-comment fonctionne le triangle de pascal suivant le theoreme : boucle for/3- calcul/4- affichage  """
#methode1:
""" n = int(input("Nombre de lignes: "))

triangle = []

for i in range(n):
    if i == 0:
        triangle.append([1])
        #print (triangle)
    else:
        ligne = [1]
        for j in range(1, i):
           # print(triangle[i-1][j-1], triangle[i-1][j])
           #n=3
            ligne.append(triangle[i-1][j-1]+ triangle[i-1][j])

        ligne.append(1)
        triangle.append(ligne)
        

for ligne in triangle:
    print(ligne)
 """
#methode2:
""" n = int(input("Nombre de lignes: "))
for i in range(n):
    x=1

    for j in range(i+1):
        print(x,end=" ")
        x=x*(i-j)//(j+1)
    print() """

#16. Calculer le plus petit commun multiple (PPCM) de deux nombres avec boucles.
""" input:donner deux nombres a et b.
verifier le plus grand entre les deux
condtion: le plus grand % a==0 and le plus grand % b==0
output: valeur de ppcm (calculer et afficher)
prob: comment calculer le ppcm? """

""" a= int(input("donner nombre1: "))
b= int(input("donner nombre2: "))
if a>b:
    ppcm=a
else:
    ppcm=b
bol=True
while bol:
    if ppcm % a==0 and ppcm % b==0:
        print("le ppcm de ",a,"et",b,"egale à: ",ppcm)
        break
    ppcm+=1 """

#un petit chang dans le code:

""" a= int(input("donner nombre1: "))
b= int(input("donner nombre2: "))
if a>b:
    ppcm=a
else:
    ppcm=b
bol=True
while bol:
    if ppcm % a==0 and ppcm % b==0:
        break
    ppcm+=1 

print("le ppcm de ",a,"et",b,"egale à: ",ppcm) """


#une autre solution? 
#fontion ppcm et pgcd in python ???????????????????

#17. Calculer le plus grand commun diviseur (PGCD) avec boucles.
""" PGCD(12 ; 18) = 6 : 
Les diviseurs de 12 sont 1, 2, 3, 4, 6, 12. 
Les diviseurs de 18 sont 1, 2, 3, 6, 9, 18.
Le plus grand diviseur commun est 6.
18%12=6  print(18%12)
12%6= 0

Algorithme d'Euclide : 
Diviser le plus grand nombre par le plus petit. 
Remplacer le plus grand nombre par le plus petit et le plus petit par le reste de la division. 
Répéter le processus jusqu'à ce que le reste soit zéro. 
Le PGCD est le dernier reste non nul obtenu.  
 """
""" a= int(input("donner nombre1: "))
b= int(input("donner nombre2: "))
p=1
if a>b:
    G=a
    petit=b
else:
    G=b
    petit=a
while p!=0:
    p=G%petit
    G=petit
    petit=p    
print("le PGCD est: ",G) """

#18. Vérifier si un nombre est parfait (somme de ses diviseurs = lui-même).
""" def parfait(n):
    S=0
    for i in range(1,n):
        if n%i==0:
            S=S+i
    return S
n=int(input("doner un nombre: "))
if parfait(n)==n:
    print("le nombre donné est parfait")
else:
    print("le nombre donné n'est pas parfait") """

#2eme methode dans la fonction pas en dehors:
""" def parfait(n):
    S=0
    for i in range(1,n):
        if n%i==0:
            S=S+i
    return S==n  # return S==n donne comme resultat la sortie de la fonction booleen soit true , soit false puisque S==n est une condtion
n=int(input("doner un nombre: "))
if parfait(n):
    print("le nombre donné est parfait")
else:
    print("le nombre donné n'est pas parfait") """
#19. Vérifier si un nombre est un nombre d’Armstrong (ex : 153 → 1³+5³+3³=153).
""" faire la somme des chiffres mais chaque chiffre a la puissance nombre de chiffres
si somme ==n 
print ( c'est un nombre d'armstrong) """

""" n=(input("donner un nombre: "))
p=len(n)
S=0
for i in n:
    a=int(i)**p
    S=S+a
    print(S)
if S==int(n):
    print("le nombre donné est un nombre d'Armstrong")
else:
    print("le nombre donné n'est pas un nombre d'Armstrong")
print(type(n))
print(type(S)) """

#20. Écrire un programme qui génère la suite de Collatz pour un nombre donné.
""" Pour un nombre entier positif donné :
- Si le nombre est pair, on le divise par 2.
- Si le nombre est impair, on le multiplie par 3 et on ajoute 1.
- On répète ces étapes avec le nouveau nombre obtenu.
- La suite continue jusqu’à ce qu’on atteigne 1. """

""" n=int(input("donner un nombre: "))
while n!=1:
    if n%2==0:
        print(n,"/",2,"=",n/2)
        n=n/2
    else:
        print(n,"*3 + 1="," ",n*3+1)
        n=n*3+1 """

#21. Écrire un programme qui affiche tous les nombres premiers jusqu’à 1000.
""" n=2
#c=0
while n<1000:
    p=True
    for x in range(2,n):
        if n%x==0:
            p=False
            break
    
    if p==True:
        print(n)
        #c=c+1
    n=n+1 """

#24. Écrire un programme qui génère une pyramide numérique (1, 22, 333, …).

""" 1
22
333
4444
55555 """
""" n=int(input("donner moi le nombre de lignes de pyramide: "))
def pyramide(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=" ")
        print()
pyramide(n) """

#25. Écrire un programme qui trouve le premier nombre supérieur à 1000 qui est divisible par 17, 19 et 23.
""" n=1001
def nombre_div(n):
    while True:
        if n%17 == 0 and n%19 == 0 and n%23 == 0:
            print("le premier nombre supérieur à 1000 qui est divisible par 17, 19 et 23 est :", n )
            break
        n+=1
nombre_div(n) """

""" try:
    n=int(input("donner un nombre superieur à 1000: "))
    if n>1000:
        while True:
            if n%17 == 0 and n%19 == 0 and n%23 == 0:
                print("le premier nombre supérieur à 1000 qui est divisible par 17, 19 et 23 est :", n )
                break
            n+=1
    else:
        print("le nombre saisi est inferieur à 1000. Tu dois mettre un nombre superieur à 1000.")

except:
    print("tu dois mettre un entier pas une chaine") """
#methode d'optimisation :
""" try:
    i=0
    Test=False
    while i<3:
        n=int(input("donner un nombre superieur à 1000: "))
        if n>1000:
            Test=True
            break
        else:
            print("le nombre saisi est inferieur à 1000. Tu dois mettre un nombre superieur à 1000.")
            i+=1
    while Test:
                if n%17 == 0 and n%19 == 0 and n%23 == 0:
                    print("le premier nombre supérieur à 1000 qui est divisible par 17, 19 et 23 est :", n )
                    break
                n+=1
except:
    print("tu dois mettre un entier pas une chaine") """

#26. Générer un triangle de * de hauteur donnée.
#triangle isocele:
""" h=int(input("donner moi l'hauteur de triangle: "))
def pyramide(h):
    for i in range(1,h+1):
        for x in range(h-i):
            print(" ",end=" ")  
        for j in range(2*i-1):
            print("*",end=" ")
        print()
pyramide(h) """
#triangle rectangle:
""" h=int(input("donner moi l'hauteur de triangle: "))
def pyramide(h):
    for i in range(1,h+1): 
        for j in range(i):
            print("*",end=" ")
        print()
pyramide(h) """

# a faire methode de pascal ??????????????

   









    





