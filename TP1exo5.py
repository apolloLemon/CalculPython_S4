def u(n):
	s=[]
	for i in range(1,n+1):
		s.append(i**2)

	return s


def v(n):
	return [i**2 for i in range(1,n+1)]


print u(3)
print v(3)

valeurs = [i for i in range(1,4)]
w = list(map(lambda x: x**2 ,valeurs))
print w