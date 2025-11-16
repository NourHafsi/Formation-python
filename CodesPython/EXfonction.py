#Crée une fonction qui retourne le carré d’un nombre.
""" def carre(a):
    c= a*a
    print("le carré de ",a, "est",c)
a=int(input("donner un nombre: "))
carre(a) """

#Crée une fonction qui calcule la moyenne d’une liste de notes.

       
#print("la moyenne ",moyenne([20,15,14]))

#2eme methode:
""" def moyenne(note):
    if len(note)==0:
        return 0
       #autre methode #print("la liste est vide")
    else:
        m=sum(note)/len(note)
        return m,print("la moyenne est",m)
note=[]
c=int(input("combien de notes on va calculer"))
for i in range(c):
    n=int(input("donner moi la note"))
    note.append(n)
moyenne(note) """


#Crée une fonction qui retourne le plus grand de deux nombres.

def bigger(a,b):
    if a>b:
        print("la plus grand c'est: ",a)
    else:
        print("la plus grand c'est: ",b)
a,b=int(input("donner moi 1er nombre: ")),int(input("donner moi 1er nombre: "))
#b=int(input("donner moi deuxieme nombre: "))
bigger(a,b)