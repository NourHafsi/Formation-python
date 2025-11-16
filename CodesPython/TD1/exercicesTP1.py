#c'est le programme de l'exercice 15 de la 1ere seance: Homework
z0= int(input("donner le 1er nombre\n"))
z1= int(input("donner le 2eme nombre\n"))
S= z0+z1
D= z0-z1
P= z0*z1
M= (z0+z1)/2
if(z0>z1):
 print ("Le plus grand est",z0)
else:
 print("Le plus grand est",z1)
print("la somme de",z0,"et",z1,"est",S)
print("la Difference entre",z0,"et",z1,"est",D)
print("le produit de",z0,"et",z1,"est",P)
print("la moyenne de",z0,"et",z1,"est",M)
#c'est le programme de l'exercice 9 de la 2ere seance: Homework
#Demander à utilisateur son âge. Afficher True si âge est supérieur ou égal à 18, sinon False.
A= int(input("donner ton age\n"))
if A>=18:
    print("True")
else: 
    print("False")
#c'est le programme de l'exercice 10 de la 2ere seance: Homework
#Écrire un programme qui vérifie si deux nombres sont égaux ou non.
a,b= 10,14
if a==b:
    print("a egale à b")
else:
    print("a n'est pas egale à b")
#c'est le programme de l'exercice 11 de la 2ere seance: Homework
#Demander un nombre et afficher True si il est pair, False sinon. si le reste(modulo %) de la division est 0 le nombre g est pair
g= int(input("donner un nombre\n"))
if g % 2== 0:
 print("True le nombre est pair")
else:
 print("False le nombre est impair")

