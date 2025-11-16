""" class Test:
 y = 5
t = Test()
t.y = 10
print(Test.y, t.y) """

#5.
""" class Compteur:
    x = 0
    def __init__(self):
     print(Compteur.x)
     Compteur.x = 1 + Compteur.x
c1 = Compteur()
c2 = Compteur()
c3= Compteur()
print(c1.x, c2.x,c3.x) """

#8.
""" class Exemple:
  def __init__(self, x):
    self.x = x
  def doubler(self):
    self.x=self.x*2
    return self.x
    #print("hello",self.x)

e1 = Exemple(5) """
""" e2 = Exemple(10)
print(e1.x + e2.x) """
#print(e1.doubler())
#y= e1.doubler()
#print((e1.doubler()) // 2) #c'est considerer comme une variable
#avec return donc on peut le modifier ou faire des operations  

#11
class Parent:
 def afficher(self):
   print("Parent")
 def afficher2(self):
   print("Méthode du parent")
class Enfant(Parent):
 def afficher(self):
   print("Enfant")

e = Enfant()
e.afficher2()