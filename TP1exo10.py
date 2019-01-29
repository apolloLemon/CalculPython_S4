def sommeDiv(n):
	out = 0
	for i in range(1,n):
		if n%i==0 :
			out += i
	return out

def nombresParfait (n):
	out = []
	for i in range(n):
		if i == sommeDiv(i):
			out.append(i)
	return out

def nombresAmicaux(n):
	

print(nombresParfait(100))