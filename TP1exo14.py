def fact(n):
	total = 1
	while(n):
		total *= n
		n -= 1
	return total

def fact_recursif(n):
	if n in [0,1]:
		return 1
	return fact_recursif(n-1)*n


for i in range(0,10):
	print(str(i)+"! = "+str(fact(i)))