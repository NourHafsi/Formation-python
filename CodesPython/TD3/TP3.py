#1. Écrire une fonction qui retourne la somme des carrés des éléments d’une liste donnée.
""" liste= input("donner une liste : parcourir une liste ")
carré des elements dans la liste
somme des carrées """

""" def Somme_carree():
    Somme=0
    n=int(input("donner moi la longeur de la liste: "))
    L=[]
    for i in range(n):
        m=int(input("donner un nombre:"))
        L.append(m)
    Lcarree=[]
    for J in L:
        Lcarree.append(J**2)
    for k in Lcarree:
        Somme +=k
    return Somme
print("la somme des carrées des elements d'une liste donnée est: ",Somme_carree()) """

#2. Crée une fonction qui prend une liste de nombres et retourne la médiane.
""" def liste():
    n=int(input("donner moi la longeur de la liste: "))
    L=[]
    for i in range(n):
        m=int(input("donner un nombre:"))
        L.append(m)
    return L,n
def mediane(L,n):
    for i in range(n):       #sous probleme 1: trier la liste:
        for j in range(i+1,n):
            if L[i]>L[j]:
                grand=L[i]
                L[i]=L[j]
                L[j]=grand
    print(L)
    if n%2 ==0: #sous probleme2: verifier si n pair ou impair(si impair : milieu: (n+1)2; si pair: moyenne de deux milieux(n/2) et (n/2+1))
        x=(L[n//2] + L[(n//2-1)])//2
    else:
        x=L[(n)//2]
    print(x)

liste,H=liste()
mediane(liste,H) """

#3. Écrire une fonction qui retourne le nième terme de la suite de Fibonacci en utilisant une approche
#  récursive optimisée (mémoïsation).
""" input =n
output = le nième terme de la suite de Fibonacci  """
""" def nième_terme():
    n= int (input ("donner un nombre: ")) #sous probleme1 : retrouver la suite
      de fibonnacci jusqu'a "n" qui est donné par l'utilisateur 
    a=0
    b=1
    for c in range(n):
        print(a)
        x=a+b
        a=b
        b=x
    print("le nieme terme de la suite de fibonnaci est ",x)
nième_terme() """
#3'. Écrire une fonction qui retourne le nième terme de la suite de Fibonacci
""" n= int (input ("donner un nombre: "))
a=0
b=1
for c in range(n):
    print(a)
    x=a+b
    a=b
    b=x """

#4. Écrire une fonction qui prend une chaîne de caractères et retourne un 
# dictionnaire contenant la fréquence de chaque mot.

""" input: donner une chaine de caracteres
output: chaque mot a ete repeté combien de fois :decitionnaire"""


#sous probleme2: on doit initialiser un dectionnaire vide parcourir la chaine 
# et verifier si le mot est existant donc on mets 1++ et on le ajoue dans le dectionnaire
#sinon pas de repetation donc on ajoute dans le dectionaire 1 (puisque il m'a demmandé combien de fois)
""" texte= input("donner moi une phrase: ") #sous probleme1: diviser une phrase en des mots: en utilisant la fonction definie .split()
def frequence(texte):
    mot=texte.split()
    freq={}
    for i in mot:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print(freq)
frequence(texte) """

#5. Crée une fonction qui trie une liste de nombres sans 
# utiliser sort() ni sorted() (ex : tri à bulles ou insertion).

""" def tri_à_bulles():
    n=int(input("donner moi la longeur de la liste: "))
    L=[]
    for i in range(n):
        m=int(input("donner un nombre:"))
        L.append(m)
    for i in range(n):       #sous probleme 1: trier la liste:
        for j in range(i+1,n):
            if L[i]>L[j]:
                grand=L[i]
                L[i]=L[j]
                L[j]=grand
    print(L)
tri_à_bulles() """

#methode 2: avec sort()

""" def Trie_sort():
    n=int(input("donner moi la longeur de la liste: "))
    L=[]
    for i in range(n):
        m=int(input("donner un nombre:"))
        L.append(m)
    L.sort()
    print(L)
Trie_sort() """

#methode 3: avec sorted() # trier dans une nouvelle liste pas notre liste deja donnée

""" def Trie_sorted():
    n=int(input("donner moi la longeur de la liste: "))
    L=[]
    for i in range(n):
        m=int(input("donner un nombre:"))
        L.append(m)
    Lsorted= sorted(L)
    print(L)
    print(Lsorted)
Trie_sorted() """

#6. Écrire une fonction qui vérifie si deux chaînes sont des anagrammes (ex : "chien" et "niche").
""" ch= input("donner moi la premiere chaine: ")
ch1= input("donner moi la deuxieme chaine: ")
def anagramme(ch,ch1):
    if len(ch) == len(ch1):
        for i in ch:
            x=False
            for j in ch1:
                if i == j:
                    x= True
                    break
        if x==False:
            print("les deux chaines données ne sont pas anagrammes")    
        if x:
            print("les deux chaines données sont anagrammes")       
    else:
        print("les deux chaines données ne sont pas anagrammes")
anagramme(ch,ch1) """

#7. Crée une fonction qui retourne tous les sous-ensembles possibles (combinaisons) d’une liste donnée.
#[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]] : [1, 2, 3]
""" Entrée : Une liste L
Sortie : Tous les sous-ensembles de L

Créer une liste result contenant un seul élément : la liste vide [].

Pour chaque élément e de la liste L :
a. Pour chaque sous-ensemble s déjà présent dans result :

Créer un nouveau sous-ensemble s + [e]
b. Ajouter tous ces nouveaux sous-ensembles à result

Retourner result """
""" def sous_ensemble():
    n=int(input("donner la taille de la liste: "))
    L=[]
    for i in range(n):
        m=int(input("donner un nombre: "))
        L.append(m)
    Lr=[[]] #Liste avec une sous liste qui est une liste vide (c'est le 1er sous ensemble qu'on commence avec)
    for x in L:
        newliste=[]
        for y in Lr:
            newliste.append(y+[x])
        Lr.extend(newliste) #  ajout de tous les listes dans une autre liste (ajout de newliste dans Lr)
    print(Lr)
sous_ensemble() """

#8. Crée deux ensembles A et B et écris une fonction qui retourne :
#a. Les éléments uniques à chaque ensemble (différence symétrique)
#b. Les éléments communs
#c. Et la proportion d’intersection par rapport à l’union (Indice de Jaccard).
""" def ret_ensemble():
    A= set()
    B= set()
    n=int(input("donner moi la taille de l'ensemble: "))
    for i in range(n):
        m=int(input("donner un nombre pour remplir l'ensembe A: "))
        A.add(m)
        x=int(input("donner un nombre pour remplir l'ensemble B: "))
        B.add(x)
    print(A,B)
    print("les elements uniques à l'ensemble A sont:",A-B)
    print("les elements uniques à l'ensemble B sont:",B-A)
    print("l'intersection entre A et B est :",A & B)
    print("l'union de A avec B est :",A | B)
    z= A & B
    w= A | B
    try:
        J=len(z)/len(w)
        print(J)
    except:
        print(len(w))
ret_ensemble() """

#9. Écrire une fonction qui vérifie si un ensemble A est un sous-ensemble strict d’un autre ensemble B.
""" B={1,2,3}
A={1,2} """
""" def verifsous():
    n=int(input("donner la taille de l'ensemble B: "))
    m=int(input("donner la taille de l'ensemble A: "))
    A= set()
    B= set()
    for i in range(n):
        x=int(input("donner un nombre à mettre dans l'ensemble B: "))
        B.add(x)
    for j in range(m):
        y=int(input("donner un nombre à mettre dans l'ensemble A: "))
        A.add(y)
    print(A,B)
    if A != B:
        bol=True
        for elem in A:
            if elem not in B:
                bol=False
                break
        if bol==True:
            print("le sous ensemble A est dans B")
        else:
            print("le sous ensemble A n'est pas un sous ensemble strict de B")
verifsous() """

#10. Écrire une fonction qui prend une liste de listes et retourne l’ensemble de tous les éléments uniques.
#[[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
#E={1,2,3}

""" def elemunique(L):
    x=set()
    for i in L:
        for elem in i:
            x.add(elem)
    print(x)

L=[[1,2],[1],[2],[1,3],[3]]
elemunique(L) """

#11. Crée une fonction qui compare deux ensembles de mots et retourne les mots présents 
# dans l’un mais pas l’autre (utilisation utile pour la comparaison de textes).
""" def compareensemble():
    n=int(input("donner la taille de l'ensemble A: "))
    m=int(input("donner la taille de l'ensemble B: "))
    A= set()
    B= set()
    for i in range(n):
        mot1=input("donner un mot à mettre dans l'ensemble A: ")
        B.add(mot1)
    for j in range(m):
        mot2=input("donner un mot à mettre dans l'ensemble B: ")
        A.add(mot2)
    print("l'ensemble A est:" ,A,"et l'ensemble B est:",B)
    print("les elements uniques à l'ensemble A sont:",A-B)
    print("les elements uniques à l'ensemble B sont:",B-A)
compareensemble() """

#12.Crée un dictionnaire représentant des étudiants Écris une fonction qui retourne le nom 
# de l’étudiant ayant la meilleure moyenne générale.
""" def creedict():
    etudiants = {}  # Dictionnaire vide pour tous les étudiants
    n = int(input("Combien d'étudiants voulez-vous entrer ? "))
    for i in range(n):
        print(f"\nÉtudiant :")
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        moyenne = float(input("Moyenne générale : "))
    # Ajouter chaque étudiant dans le dictionnaire avec clé unique
        etudiants[nom] = {
            'Prenom': prenom,
            'Moyenne_generale': moyenne
            }
        print(etudiants)
    return etudiants
def moyenneetudiant():
    C = creedict()
    # Prendre le premier étudiant comme référence
    meilleur_nom = list(C.keys())[0]
    meilleur = C[meilleur_nom]

    for nom, info in C.items():
        if info['Moyenne_generale'] > meilleur['Moyenne_generale']:
            meilleur = info
            meilleur_nom = nom
            print(info['Moyenne_generale'])
    print(meilleur,meilleur_nom)
    
moyenneetudiant() """

#13. Crée une fonction qui fusionne deux dictionnaires :
#● Si une clé est présente dans les deux, additionner leurs valeurs.
#● Sinon, conserver la clé telle quelle.
""" def fusionne(d1,d2):
    d3={}
    #print(d1.keys()|d2.keys())
    for i in d1.keys()|d2.keys():
        if i in d1 and i in d2:
            d3[i]=d1[i]+d2[i]
        elif i in d1:
            d3[i]=d1[i]
        else:
            d3[i]=d2[i]

    print(d3)
d1={
    "A":10,
    "B":3
}

d2={
    "A":5,
    "D":4
}
fusionne(d1,d2) """

#14. Écrire une fonction qui trie un dictionnaire par valeur décroissante et retourne un nouveau dictionnaire trié.
""" d={
    "A":4,
    "D":9
}
def tri_dict(d):
    L=list(d.items())
    #print(L)
    n=len(L)
    for i in range(n-1):
        for j in range(n-i-1):
            if L[j][1]< L[j+1][1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    
    nd={}
    for cles,valeurs in L:
        nd[cles]=valeurs

    print(nd)
tri_dict(d) """

#15. Crée une fonction qui retourne un nouveau dictionnaire contenant uniquement 
# les clés dont les valeurs dépassent une certaine limite donnée en paramètre.

""" input : dictionnaire
output: nouveau dictionnaire """

""" def filtrage(dict,limite):
    nouveau_dict={}
    for cles,valeurs in dict.items():
        if valeurs > limite:
            nouveau_dict[cles]=valeurs
    print(nouveau_dict)
dict={
    "A":5,
    "B":10,
    "C":12
}
limite=8
filtrage(dict,limite) """

#20. Crée une fonction qui lit une clé dans un dictionnaire et :
#● Gère KeyError si la clé n’existe pas
#● Gère TypeError si le dictionnaire n’est pas valide
#● Retourne une valeur par défaut en cas d’erreur.

""" def lire_cle(d,clés,default=None):
    try:
        print(d[clés])
    except KeyError:
        print("la clé n’existe pas ! ")
        return print(default)
    except TypeError:
        print("le dictionnaire n’est pas valide ! ")
        return print(default)
d={
    "A":5,
    "B":10
}
#pour afficher l'erreur TypeError
#d=["a","b"]
# lire_cle(d,"B") : 
#d=5 
# lire_cle(d,"B"):pour afficher l'erreur TypeError
lire_cle(d,"D")  #pour afficher l'erreur KeyError """