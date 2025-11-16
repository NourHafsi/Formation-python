#PPCM:
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

#23. Écrire une fonction qui calcule la moyenne d’une série de nombres entrés par l’utilisateur (fin si -1).
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