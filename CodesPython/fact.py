n = int(input("Donner un nombre :\n"))
fact = 1  # f(5)=5*4*3*2*1

for i in range(1, n + 1):
    fact = fact * i
print("La factorielle de", n, "est :", fact)