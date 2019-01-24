def polynome(a,b,c):
	return lambda x : a*x**2 + b*x + c

f = polynome(1,1,1)
g = polynome(2,0,-3)
print f(3)
print g(3)