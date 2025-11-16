""" n=input("donner un nombre : ")
def somme_chiffres(n):
    S=0
    for i in n:
        S=int(i) + S
    print(S)
    
somme_chiffres(n)    """ 

#fonction recursive:
n=int(input("donner un nombre \n"))
S=0
def Somme(n):
    if n < 10:
        return n
    else:
        S= n%10 + Somme(n//10)   # n%10: donne le dernier chiffre et #Somme(n//10) ignore 
        #le dernier chiffre pour faire la somme par exemple 4 + somme(123)
        return S
print(Somme(n))    
