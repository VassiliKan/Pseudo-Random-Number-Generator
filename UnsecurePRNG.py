import random
import matplotlib.pyplot as plt
import numpy as np
import math 


m = 9576890767
a = 314125421
b = 1
x0 = 8423411 
nbBoucle=1000
list=[]


def Gener(a, b, m, x0):
	i = 0
	xn = x0		
	nbI = 0
	nbP = 0
	while (i < nbBoucle):
		xn = ((a * xn + b) % m)
		list.append(xn)
		if xn % 2 == 0:
			nbP = nbP + 1
			#print("1")
			#list.append(1)
		else:
			nbI = nbI + 1
			#print("0")
			#list.append(0)
		i = i + 1
	print("nbPaire : ", nbP, "nbImpaire : ", nbI)
	x = list[:-1]
	y = list[1:]
	return x, y


def isPrime(nb):
	for i in range(2, round(math.sqrt(nb) + 1)):
		print(i)



#x, y = Gener(a, b, m, x0)

#y = np.arange(0, nbBoucle)

#plt.plot(list0, list[:-1])

#plt.scatter(x=x, y=y)
#plt.show()