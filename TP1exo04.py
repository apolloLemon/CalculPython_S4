def f(n):
	s=0
	for i in range(0,n+1):
		s += i**2
	return s

def g(n):
	s=0
	for i in range(0,n+1):
		for j in range(0,n+1):
			s += (i**2 + j**3)
	return s

def h(n):
	s=0
	for j in range(0,n+1):
		for i in range(0,n+1):
			s += (i**2 + j**3)
	return s

print f(2)
print g(2)
print h(2)
# g=h