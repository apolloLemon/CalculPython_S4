def equation(a,b,c):
	delta = (b**2)-(4*a*c)

	racines=[]
	if (delta >= 0):
		x1 = (-b - delta)/2*a
		racines.append(x1)

	if (delta > 0):
		x2 = (-b + delta)/2*a
		racines.append(x2)
	
	return racines

def equationbis(a,b,c):
	out = "l'equation "+str(a)+"x**2 + "+str(b)+"x + "+str(c)+" = 0 "

	racines = equation(a,b,c)
	if (len(racines) == 2):
		out += "a deux solutions reelles egale a "+str(racines[0])+" et "+str(racines[1])
	elif (len(racines) == 1):
		out += "a une unique solution reelle egale a "+str(racines[0])
	else :
		out += "n'a pas de solution reelle"

	print out

equationbis(1,0,0)
equationbis(1,0,-1)
equationbis(1)
#print equationbis(1,0,-1)