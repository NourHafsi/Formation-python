# creation d'une liste et la remplir:
n=int(input("donner la longueur de la liste: "))
L=[]
for i in range(n):
    m=int(input("donner un nombre: "))
    L.append(m)

# Tri d'une liste:
def tri_selection(L):
    n = len(L)
    for i in range(n):
        # Trouver l'indice du minimum dans la sous-liste L[i:]
        min_idx = i
        for j in range(i+1, n):
            if L[j] < L[min_idx]:
                min_idx = j
        # Échanger L[i] et L[min_idx]
        L[i]= L[min_idx]
        L[min_idx] = L[i]
    return L

# Exemple d'utilisation
ma_liste = [5, 2, 9, 1]
tri_selection(ma_liste)
print(ma_liste)  # Affichera la liste triée
    