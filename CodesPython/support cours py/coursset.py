""" #exemple:
nombres = {4,6,7,3,2,1,200,501,1}
print(nombres)
#ex Set: Créer deux ensembles A et B puis afficher leur union et intersection et difference. """
A={"A","5","b","@","8","6"}
B={"A","3","4","b","1","6"}
x=(A|B)
print("l'union entre les deux ensembles:", x)
y= A & B
print("l'intersection entre les deux ensembles:", y)
z= (A-B)
print("la difference entre l'ensemble A et l'ensemble B est :", z)
w= (B-A)
print("la difference entre l'ensemble B et l'ensemble A est :", w)"""