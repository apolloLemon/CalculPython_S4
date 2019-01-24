# TP1 : un peu de programmation
# 17 janvier 2019
# exercices de 1 a 9

##################################"
# exercice 1  ecriture de fonctions
##################################"

def f(x):
    return x**2+x+1

def g(x):
    print(x**2+x+1)
    
# la fonction f renvoie un objet (de meme type que x)
# alors que la fonction g ne retourne rien (type None), 
# elle ne fait qu'afficher une valeur
# si on fait a=g(1), a  est du type None et f(a) n'a pas de sens

##################################"
# Exercice 2 fonction somme
##################################"

def somme(a,b):
    return a+b

# cette fonction admet tous les types possibles a et b 
# qui peuvent s'additionner


######################################
# exercice 3 equations du second degre
######################################

from math import sqrt
# pour disposer de la fonction racine carree

def equation(a,b,c):
    d=b**2-4*a*c
    if d>0:
        x1=-b-sqrt(d)
        x1/=2*a
        x2=-b+sqrt(d)
        x2/=2*a
        resu=[x1,x2]
    elif d==0:
        x0=-b/(2*a)
        resu=[x0]
    else:
        resu=[]
    return resu
    
def equationbis(a,b,c):
    d=b**2-4*a*c
    if d>0:
        x1=-b-sqrt(d)
        x1/=2*a
        x2=-b+sqrt(d)
        x2/=2*a
        message=f"l'equation a deux solutions reelles {x1} et {x2}"
    elif d==0:
        x0=-b/(2*a)
        message=f"l'equation {a}x**2+{b}x+{c}=0 a une unique solution reelle {x0}"
    else:
        message=f"l'equation {a}x**2+{b}x+{c}=0 n'a pas de solution reelle"
    print(message)

        
def equation2(liste):
    # on  doit transmettre une liste
    lg=len(liste)
    if lg!=3 or liste[0]==0:
        raise ValueError("Ce n'est pas une equation du second degre")
    a,b,c=liste
    d=b**2-4*a*c
    if d>0:
        x1=-b-sqrt(d)
        x1/=2*a
        x2=-b+sqrt(d)
        x2/=2*a
        resu=[x1,x2]
    elif d==0:
        x0=-b/(2*a)
        resu=[x0]
    else:
        resu=[]
    return resu    



##################################"
# exercice 4 calcul d'une somme
##################################"

def somme1(n):
    S=0.
    for i in range (n+1):
        S+=i**2
    return S

def somme2(n):
    S=0.
    for i in range (n+1):
        for j in range(n+1):
            S+=i**2+j**3
    return S

def somme3(n):
    S=0.
    for j in range (n+1):
        for i in range(n+1):
            S+=i**2+j**3
    return S

####################################"
#Exercice 5 constructions de listes
####################################""
    
def l1(n):
    L=[]
    for i in range(n+1):
        L.append(i**2)
    return L

def l2(n):
    L=[i**2 for i in range(n+1)]
    return L

def carre(x):
    return x**2

def l3(n):
    L=range(n+1)
    L=list(map(carre,L))
    return L

####################################"
# Exercice 6 autopsie
####################################"
# algorithme d'Euclide

def F(a,b):
     while b!=0:
         #a,b=b,a%b
         q=a//b;r=a%b
         c=f"{a}={b}*{q}+{r}"
         print(c)
         a,b=b,a%b
     return a

####################################"
# Exercice 7 autopsie
####################################"

def cesar(C,n) :
    # pour les minuscules
    k=len(C)
    D="" # chaine de caractere vide
    for i in range(k):
        a=ord(C[i])+n
        if a>ord('z'):
            a-=26
        D=D+chr(a)  # ajoute chr(a) a la chaine D
    return D
 
#C='bonjour'
#print(cesar(C,9))

#########################################  
# Exercice 8  persistance multiplicative
########################################

def produit(n):
    a=str(n)# transformation en chaine de caracteres
    k=len(a)
    p=1
    for i in range(k):
       p*=int(a[i]) # transforme chaque chiffre en entier
    return p

def per(n):
    m=n
    compteur=0
    while len(str(m))>1:
        m=produit(m)
        compteur+=1
    return compteur

def recherche(p):
    n=1
    while per(n)<p:
        n+=1
    return(n)
    
>>> recherche(5)
679
>>> recherche(6)
6788
    
##########################
# Exercice 9 Syracuse
##########################

def f(n):
    if n%2==0:
        u=n//2
    else:
        u=3*n+1
    return u

def syra(a,n):
    # retourne la liste des u_a,k
    # pour 0<= k <= n
    u=a
    L=[a]
    for i in range(n):
        u=f(u)
        L.append(u)
    return(L)

def L(a):
    # retourne la longueur
    u=a
    L=[a]
    while u!=1:
        u=f(u)
        L.append(u)
    #print(L)
    return(len(L))

def H(a):
    # retourne la hauteur
    u=a
    L=[a]
    while u!=1:
        u=f(u)
        L.append(u)
    # print(L)
    return(max(L))

def Lmax(A):
    # retourne la longueur max pour
    # a de 1 a A
    l=[] # liste des longueurs
    for a in range(1,A+1):
        l.append(L(a))
    lmax=max(l)
    return (lmax,l.index(lmax))

def Hmax(A):
    # retourne la longueur max pour
    # a de 1 a A
    l=[] # liste des longueurs
    for a in range(1,A+1):
        l.append(H(a))
    lmax=max(l)
    return (lmax,l.index(lmax))
    
    


   


