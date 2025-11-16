#29. Écrire un programme qui affiche tous les couples (i, j) avec i, j de 1 à 5.
""" for i in range(1,6):
    for j in range(1,6):
        print(i,j) """
#30. Demander un nombre n et afficher tous les nombres premiers ≤ n.
""" n = int(input("Entrez un nombre n: "))
for p in range(2, n + 1):  
    testpremier = True 
    for i in range(2, p): 
        if p % i == 0: 
            testpremier = False
            break
    if testpremier:
        print(p) """

#31. Vérifier si un nombre est palindrome (ex : 121 → oui, 123 → non).
""" n= int(input("Donner un nombre : "))  
ch_n= str(n)                        
inv_ch_n= ""

for x in ch_n:
    inv_ch_n= x + inv_ch_n                      
print("l'inverse de notre nombre est:", inv_ch_n)

if ch_n== inv_ch_n:
    print("Le nombre est palindrome")
else:
    print("Le nombre n'est pas palindrome") """
#32. Calculer la somme des chiffres pairs d’un nombre.
""" n= int(input("Donner un nombre : "))
ch_n= str(n)
S=0
for x in ch_n:
    if int(x) % 2 == 0:
        S=S+int(x)
print("La somme des chiffres pairs est :", S) """    
