def Hardy(n):
	b = int(n**(1/3))
	c = [i**3 for i in range(b)]
	
	l = []
	for i in range(b):
		for j in range(i,b):
			l.append(c[i]+c[j])

	l.sort()
	for i in range(0,n-1):
		if l[i]==l[i+1]:
			return l[i]

print(Hardy(5000))