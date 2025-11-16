""" #exercice1 TD2 Partie 1 :Créer une liste contenant vos 5 fruits préférés et l’afficher.
Fruit= ['fraise','banane','kiwi','watermelon','pomme']
print(Fruit)
#exercice2 TD2 Partie 1 :Ajouter un élément à une liste existante avec append().
Fruit.append('poire')
print(Fruit)
#exercice3 TD2 Partie 1 :Supprimer un élément d’une liste avec remove().
Fruit.remove('watermelon')
print(Fruit) """
#exercice15 TD2 Partie 2 : Vérifier si une lettre est une voyelle ou une consonne.
""" l= input("donner une lettre\n")
voy= ['A','a','O','o','I','i','E','e','Y','y','U','u']
search= False
for x in voy:
 if l==x:
  search=True
  #print ("la lettre saisie est une voyelle")
  break
if search: # si on mets search: c'est comme ci on a mis search ==True
 print("il ya voyelle")
else:
 print("il ya consonne") """
#exercice26 TD2 Partie 3 : Afficher les éléments d’une liste avec une boucle for.
""" l= ['lit','chaise','bureau','table']
for i in l:
    print(i) """
  
#exercice36 TD2 Partie 4 : Parcourir une liste et arrêter à la première occurrence de la valeur 0.
liste=[3,4,0,8,7,0]
for i in liste:
    if i==0:
        print("j ai trouvé la premiere valeur de 0")
        continue
        print(i)
    



