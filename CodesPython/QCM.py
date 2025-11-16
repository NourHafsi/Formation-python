""" class A:
    def __init__(self, x):
      self.x = x
a = A(5)
b= A(9)
print(a.x)

print(type(a)) """
##################################################
""" class A:
    def hello(self):
        print("je suis dans la classe A ")
class B:
    def hello(self):
        print("je suis dans la classe B ")

class C(B,A):
    pass

X= C()
X.hello() """
##########################################################""
class A:
    def talk(self):
     return "A"
class B(A):
    def talk(self):
     return "B"
class C(B):
    pass
print(C().talk())
