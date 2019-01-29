def f(x):
	return x**2 + x + 1

def g(x):
	print f(x)


f(1) #ceci calcule f(1)
g(1) #ceci affiche f(1)

g(f(1)) 
#ceci calcul f(1) sois 3
#puis le donne a g 
#qui affiche le resultat de f(3)

f(g(1))
#ceci marche pas car g ne retourne rien
#a f, et f peux pas faire son calcul