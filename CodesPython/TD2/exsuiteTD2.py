#exercice28 de TD2: Demander à l’utilisateur un mot de passe et répéter jusqu’à ce qu’il tape 1234
MP= input("donner un mot de passe\n")
mot_passe="1234"   
while MP!= mot_passe:
   MP= input("donner un mot de passe\n")
print("Mot de Passe est correct")

#deuxieme methode (internet):
mot_de_passe = ""
while mot_de_passe != "1234":
    mot_de_passe = input("Entrez le mot de passe : ")

print("Accès autorisé")

#exercice29 de TD2: Créer une boucle qui s’arrête quand un nombre supérieur à 50 est saisi:probleme????????????????????

n=int(input ("donner un nombre: "))
while n<=50:
    n=int(input ("donner un nombre: "))
#ou
n=0
while n<=50:
    n=int(input ("donner un nombre: "))


#exercice33 de TD2: Utiliser continue pour ignorer le nombre 5 dans une boucle.
for i in range(10):
    if i == 5:
        continue
    print(i)
 

#exercice34 de TD2: Utiliser break pour arrêter la boucle quand le nombre atteint 7.
for i in range(10):
    if i==7:
        break
    print(i)
#exercice35 de TD2: Afficher les 10 premiers nombres impairs: support internet pour connaitre comment ajouter la liste des impairs
n=1
i=0
while i<10:
    print(n)
    n=n+2
    i+=1

#exercice37 de TD2: Afficher uniquement les nombres pairs entre 1 et 20 avec continue.
for n in range(1,21):
    if n%2!=0:
        continue
    print(n)

#exercice38 de TD2: Utiliser range() pour créer une liste de carrés de 1 à 10. # je l'ai fait sans liste
#je l'ai oublié mais j'ai vu sur internet et donc j'ai ajouté la liste
carre=[]
for i in range(1,11):
    carre.append(i*i)
print(carre)
#exercice39 de TD2: Parcourir une chaîne et ignorer les espaces avec continue.
ch= input("donner une chaine: ")
ch1=""
for i in ch:
    if i == " ":
        continue
    ch1+=i
print("chaine sans espace: ",ch1)
    
#exercice40 de TD2: Simuler un compte à rebours (countdown) de 10 à 0.support internet:
for i in range(10, -1, -1):
    print(i)

#deuxieme methoe aussi internet: 
i = 10
while i >= 0:
    print(i)
    i = i - 1



 
