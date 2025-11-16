a=int(input("donner a\n"))
b=int(input("danner b\n"))

if(a>b):
    somme=a+b
    print("a est plus grand que b")
    if(a>0):
      print("a est plus grand que b et plus grand que 0")
      print("la somme",somme)
    elif(a<0):
       print("a est plus grand que b et plus petit que 0")
       print("la somme",somme)
elif(a==b):
   print("a est egale a b")
else:
    print("b est plus grand que a")
