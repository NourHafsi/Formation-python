#Exercice 1:
def S_carree(L):
    s = 0
    for x in L:
        c = x * x
        s = s + c
    return s
ma_liste = [2, 4, 5]
print("la somme des carrées des elements d'une liste donnée est: ", S_carree(ma_liste))


#2eme methode
""" def Somme_carree():
    Somme=0
    n=int(input("donner moi la longeur de la liste: "))
    L=[]
    for i in range(n):
        m=int(input("donner un nombre:"))
        L.append(m)
    print(L)
    Lcarree=[]
    for j in L:
        Lcarree.append(j**2)
    print(Lcarree)
    for k in Lcarree:
        Somme +=k
    return Somme
print("la somme des carrées des elements d'une liste donnée est: ",Somme_carree()) """

#3eme methode 
""" def Somme_carree():
    Somme = 0
    n = int(input("donner moi la longeur de la liste: "))
    L = []
    for i in range(n):
        m = int(input("donner un nombre: "))
        L.append(m)

    for x in L:
        Somme += x**2

    return Somme
print("la somme des carrées des elements d'une liste donnée est: ",Somme_carree()) """ 
# au lieu de ce print tu peux faire : 
""" resultat = Somme_carree()
print("la somme des carrées des elements d'une liste donnée est: ", resultat) """

#Exercice 2:
def mediane():
    n = int(input("Donner la longueur de la liste: "))
    L = []
    for i in range(n):
        x = int(input("Donner un nombre: "))
        L.append(x)

    # Tri par sélection
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if L[j] < L[min_idx]:
                min_idx = j
        # Échange en deux lignes
        temp = L[i]
        L[i] = L[min_idx]
        L[min_idx] = temp

    return n, L

# Récupérer n et L
n, L = mediane()
print("Liste triée:", L)

# Calcul de la médiane
if n % 2 == 0:
    milieu1 = n // 2
    milieu2 = n // 2 - 1
    x = (L[milieu1] + L[milieu2]) / 2  # utilisation de / pour float
else:
    x = L[n // 2]

print("La médiane de la liste est:", x)

#Exercice 3 : 
#Écrire une fonction qui retourne le nième terme
#de la suite de Fibonacci en utilisant une approche récursive optimisée (mémoïsation).
def nième_terme():
    n= int (input ("donner un nombre: ")) #sous probleme1 : retrouver la suite de fibonnacci jusqu'a "n" qui est donné par l'utilisateur 
    a=0
    b=1
    for c in range(n):
        print(a)
        x=a+b
        a=b
        b=x
    print("le nieme terme de la suite de fibonnaci est ",x)
nième_terme()

def nieme():
    n=int(input("donner un nombre: "))