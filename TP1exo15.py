def Fibonacci(n):
	if n in [0,1]:
		return 1
	return Fibonacci(n-1)+Fibonacci(n-2)

Fibonacci(31)
#for i in range(0,31):
#	print(str(i)+": "+str(Fibonacci(i)))


# 'hand' Optimised Version
def Fibonacci_lite(n):
	if fibtab[n]==0:
		fibtab[n] = Fibonacci_lite(n-1)+Fibonacci_lite(n-2)
	return fibtab[n]

def Fibonacci_lite_launcher(n):
	global fibtab
	fibtab = [0]*(n+1)
	fibtab[0]=fibtab[1]=1
	return Fibonacci_lite(n)

Fibonacci_lite_launcher(30)

# Optimised Version by Socratica
fibonacci_cache = {}
def fibonacci_soc(n):
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	if n == 1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fibonacci_soc(n-1) + fibonacci_soc(n-2)

	fibonacci_cache[n] = value
	return value

# lru_cache Version
from functools import lru_cache
@lru_cache(maxsize = 1000)
def Fibonacci_lru(n):
	if n in [0,1]:
		return 1
	return Fibonacci_lru(n-1)+Fibonacci_lru(n-2)

#import random
import timeit
print(timeit.timeit('''
def Fibonacci(n):
	if n in [0,1]:
		return 1
	return Fibonacci(n-1)+Fibonacci(n-2)

Fibonacci(31)''',number=10))

print(timeit.timeit('''
def Fibonacci_lite(n):
	if fibtab[n]==0:
		fibtab[n] = Fibonacci_lite(n-1)+Fibonacci_lite(n-2)
	return fibtab[n]

def Fibonacci_lite_launcher(n):
	global fibtab
	fibtab = [0]*(n+1)
	fibtab[0]=fibtab[1]=1
	return Fibonacci_lite(n)

Fibonacci_lite_launcher(30)''',number=500000))

#print(timeit.timeit('''
#from functools import lru_cache
#@lru_cache(maxsize = 1000)
#def Fibonacci_lru(n):
#	if n in [0,1]:
#		return 1
#	return Fibonacci_lru(n-1)+Fibonacci_lru(n-2)''',number=500000))