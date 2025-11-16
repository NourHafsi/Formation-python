#exercice4 de TD2: Afficher le premier et le dernier élément d’une liste.
l= ['ali','ahmed','Anisa','fatma','rahma']
print(l[0])
print(l[-1])
#exercice5 de TD2: Compter combien de fois un élément apparaît dans une liste.
l= ['ali','ahmed','Anisa','fatma','rahma','ahmed']
print(l.count('ahmed'))
#exercice6 de TD2: Trier une liste de nombres dans l’ordre croissant.problem depuis la derniere seance j'ai 
# pas encore reflichie car j'ai pas le temps ??????????????
L=[4,1,3]
print(L)
i=0
for i:
 if L[i]>L[i+1]:
    elsupp=L.pop(i)
    L.insert(i+1,elsupp)
    print(L)
 else: 
   print(L)
 
    
#exercice8 de TD2: Créer une liste de 10 nombres pairs avec range().
nbpairs=[]
for n in range(10):
  if n%2==0:
    nbpairs.append(n)
    #print('la liste demmandee est',nbpairs)
print('la liste demmandee est',nbpairs)
#exercice9 de TD2: Vérifier si un élément est présent dans une liste avec in.  
l=[1,2,6,8,7]
i=int(input("donner un nombre\n"))
if i in l:
  print('element is present in list')
else:
  print('element is not present in list')

#exercice10 de TD2: Parcourir une liste et afficher chaque élément.
l= ['un','deux','trois']
for i in l:
    print(i)
    
#exercice11 de TD2: Vérifier si un nombre est positif, négatif ou nul.
n= int(input("donner un nombre\n"))
if n>0:
    print("le nombre est positif")
elif n<0:
    print("le nombre est negatif")
else:
    print("le nombre est null")
#exercice12 de TD2: Vérifier si un nombre est pair ou impair.
n= int(input("donner un nombre\n"))
if n%2==0:
    print("le nombre est pair")
else:
    print("le nombre est impair")
#exercice13 de TD2: Vérifier si une personne est mineure ou majeure selon son âge.
n= int(input("donner ton age\n"))
limit=18
if n>=limit:
    print("Tu es majeur")
else:
    print("Tu es mineur")
#exercice14 de TD2: Vérifier si une année est bissextile. 
anne=int(input("donner une année\n"))
if anne%4==0:
    print("cette annee est bissextile")
else:
    print("cette annee n'est pas bissextile")
#exercice16 de TD2: Comparer deux nombres et afficher le plus grand.
n=int(input("donner un nombre\n"))
m=int(input("donner un deuxieme nombre\n"))
if n>m:
    print("le plus grand est",n)
else:
    print("le plus grand est",m)

#exercice17 de TD2:Vérifier si une chaîne de caractères contient le mot Python.
ch=input("une chaine de caractere\n")
ch1="Python" 
if ch1 in ch:
    print ("la chaine contient le mot")
else:
    print ("la chaine ne contient pas le mot")
#exercice18 de TD2: Vérifier si un étudiant est admis (note >= 10) ou recalé.
note=int(input("donner la note\n"))
if note>=10:
   print("etiduant Admis")
else:
   print("etiduant Recalé")
#exercice19 de TD2: Vérifier si un triangle est équilatéral, isocèle ou scalène.
l1=float(input("donner la 1ere longueur\n"))
l2=float(input("donner la 2eme longueur\n"))
l3=float(input("donner la 3eme longueur\n"))
if l1==l2==l3:
    print("triangle est équilatéral")
elif l1==l2 or l2==l3 or l3==l1:
    print("triangle est isocèle")
else:
    print("triangle est scalène")

#exercice21 de TD2: Afficher les nombres de 1 à 10 avec for.
for n in range(1,11):
    print (n)
#exercice22 de TD2: Afficher les nombres pairs de 0 à 20.
for i in range (21):
    if i%2==0:
        print(i)
#exercice23 de TD2: Calculer la somme des entiers de 1 à 100.
for i in range(1,101):
    S = i*(i + 1) / 2
print(S)
#exercice24 de TD2: Afficher les tables de multiplication de 1 à 10.
for i in range(11):
    for n in range(1,11):
        n=n*i
        print(n)
#exercice25 de TD2: Compter le nombre de voyelles dans une chaîne donnée.
ch= input ("donner une chaine\n")
ch1= "AEIOUYaeiouy"
c=0
for x in range(12):
    for i in ch:
        if i == ch1[x]:
            c+=1
print(c)

#exercice26 de TD2: Afficher les éléments d’une liste avec une boucle for.
liste= [1,2,3,5,8,7]
for i in liste:
    print(i)
#exercice27 de TD2: Utiliser une boucle while pour compter jusqu’à 10.
i=0
while i<11:
    print (i)
    i+=1
#peut l'utiliser ou non ?????
i=0 
while i in range(11):
    print (i)
    i+=1

#exercice30 de TD2: Calculer la factorielle d’un nombre avec une boucle.:j'ai un probleme comment 
# je peux sommer le factoriel donc j'ai utilisé internet
n = int(input("Donner un nombre :\n"))
fact = 1  # f(5)=5*4*3*2*1

for i in range(1, n + 1):
    fact = fact * i
print("La factorielle de", n, "est :", fact)

#exercice31 de TD2: Utiliser range() pour afficher les nombres de 5 à 15.
for i in range (5,16):
        print(i)
#exercice32 de TD2:Afficher les multiples de 3 entre 0 et 30.
for i in range (31):
    if i%3==0:
        print(i)
