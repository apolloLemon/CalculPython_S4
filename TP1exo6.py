def F(a,b):
	print str(a)+" "+str(b)
	while b!=0:
		a,b = b,a%b
		print str(a)+" "+str(b)
	return a

print F(34,23)