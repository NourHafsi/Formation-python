#33. Compter combien de nombres de 1 à 1000 sont divisibles par 7 mais pas par 5.
""" c=0
for n in range(1,1001):
    if n%7==0 and n%5!=0:
        c+=1
print(c) """

#34. Écrire un programme qui invente un mot de passe de longueur n avec chiffres et lettres.
""" n = int(input("Donner la longueur du mot de passe : "))
chiff_lett = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
mot_pass = ""

if n <= 0:
    print("La longueur doit être un entier positif.")
else:
    for i in range(n):
        mot_pass += chiff_lett[i % len(chiff_lett)]
    print("Le mot de passe composé est :", mot_pass) """

#35. Écrire un programme qui retourne la position de la première voyelle dans un mot.   
""" ch = input("Donner un mot : ")
chv = "aeiouyAEIOUY" 
n = len(ch)

for i in range(n):
    if ch[i] in chv:
        print(i, " position de la première voyelle trouvée dans le mot")
        break  """

#36. Écrire un programme qui affiche les 20 premiers termes de la suite de Fibonacci et vérifie lesquels sont pairs.
""" a=0
b=1
for c in range(20):
    print(a)
    if a%2 == 0:
        print("le nombre est pair")
    x=a+b
    a=b
    b=x """
#37. Écrire un programme qui affiche tous les nombres de 1 à 100, mais remplace :
# ● les multiples de 3 par "Fizz"
# ● les multiples de 5 par "Buzz"
# ● les multiples de 15 par "FizzBuzz".

""" for n in range(1, 101):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n) """