def somme (a,b):
	return a + b

str1='hello'
str2=' world'
liste1=[1,2]
liste2=[3,4]
dico1 = {'chat':'cat','chien':'dog'}
dico2 = {'livre':'book','piano':'piano'}

print somme(1,2)
# 3

print somme(str1,str2)
# hello world

print somme(liste1,liste2)
# [1, 2, 3, 4]

print somme(dico1,dico2)
print somme(liste1,str1)
print somme(1,str1)
print somme(liste2,5)
# ne fonctionne pas