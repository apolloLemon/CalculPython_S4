def Conway(string):
	outstring = ""
	c=1
	if len(string)==1:
		outstring="1"+string

	for i in range(len(string)-1):
		if string[i] == string[i+1]:
			c+=1
			if i == len(string)-2:
				outstring += str(c)+string[i]
		else:
			outstring += str(c)+string[i]
			c=1
			if i == len(string)-2:
				outstring += "1"+string[i+1]

	return outstring


a = "1"
print(a)
for i in range(100):
	a = Conway(a)
	print(a)
