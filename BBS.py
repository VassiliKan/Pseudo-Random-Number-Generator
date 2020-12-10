from numpy import *
from matplotlib.pyplot import *



listXn=[]

def mod3plus4(a):
	if a % 4 == 3:
		return True
	else:
		return False
	
def pgcd(a,b) :
	while a%b != 0 :
		a, b = b, a%b
	return b

# Cherche un entier premier a n. La recherche debute a partir d'un nombre egale a n / 2 afin qu'il soit suffisament grand
def findX(n):
	for i in range (round(n/2), n):
		if pgcd(i,n) == 1:
			return i
	return -1
	
	
def BBS(nb):	
	bits = ""
	p = 231231251 # a prime number
	q = 231233999 # another prime number
	if mod3plus4(p) : print ("p is ok")   # check if p and q are equals to 3 mod 4 
	if mod3plus4(q) : print ("q is ok\n")  
	n = p * q	
	x = findX(n)
	x0 = xi = x**2 % n
	for i in range(nb):
		listXn.append(xi)
		if i % (nb / 10) == 0:
			print("... Processing", int(i / (nb/100)), "%")
		xiPlus1 = xi**2 % n
		if xi % 2 == 0:
			bits += "0"
		else:
			bits += "1"
		xi = xiPlus1 
	print("... Processing 100% \n... Done !\n")
	return bits
	

##Proportion de 0 et de 1 :
def CountBits(string):
	nb1 = 0
	nb0 = 0
	lenght = len(string)
	for i in string:
		if i == '0':
			nb0 = nb0 + 1
		else:
			nb1 = nb1 + 1
	print("La proportion de '1' est : ", nb1 / lenght, ", celle de '0' est de  ", nb0 / lenght, "\n")
	

def CountDuoBits(string):
	nb00 = 0
	nb01 = 0
	nb10 = 0
	nb11 = 0
	lenght = len(string) / 2
	
	for i in range(0, len(string), 2):
		subStr = string[i:i+2]
		if subStr == '00':			
			nb00 = nb00 + 1
		elif subStr == '01':			
			nb01 = nb01 + 1
		elif subStr == '10':			
			nb10 = nb10 + 1
		elif subStr == '10':			
			nb11 = nb11 + 1	
	print("La proportion de la sous chaine '00' est : ", nb00 / lenght, ", celle de '01' est de  ", \
			nb01 / lenght, ", celle de '10' est : ", nb10 / lenght, ", celle de '11' est de  ", nb11 / lenght, "\n")



def CountFourBits(string):
	listCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ## dico
	lenght = len(string) / 4

	for i in range(0, len(string), 4):
		subStr = string[i:i+4]
		value = int(subStr, 2)
		if value <= 15:
			listCounter[value] += 1

	for j in range(len(listCounter)):
		listCounter[j] = listCounter[j] / lenght

	print("Les differentes proportion des sous chaines composees de 4 bits sont, par ordre croissant : \n", listCounter, "\n")
	print("Voici les differentes donnees statistiques calculees a partir des differentes proportion des sous chaines composees de 8 bits, soit un octet : ")
	print(" - Etendue : ", max(listCounter) - min(listCounter))
	print(" - moyenne : ", mean(listCounter))
	print(" - ecart type : ", std(listCounter), "\n")


def CountBytes(string):
	listCounter = [0 for x in range(256)]

	for i in range(0, len(string), 8):
		subStr = string[i:i+8]
		value = int(subStr, 2)
		if value <= 255:
			listCounter[value] += 1
			
	for j in range(len(listCounter)):
		listCounter[j] = listCounter[j] / (len(string) / 8)

	#print(listCounter)	
	print("Voici les differentes donnees statistiques calculees a partir des differentes proportion des sous chaines composees de 8 bits, soit un octet : ")
	print(" - Etendue : ", max(listCounter) - min(listCounter))
	print(" - moyenne : ", mean(listCounter))
	print(" - ecart type : ", std(listCounter))
	
	
	
## Nuage de point de coordonnées (xn+1, xn)
## Semble uniformément répartie
def PlotNuagePoints():
	x = listXn[:-1]
	y = listXn[1:]
	scatter(x=x, y=y)
	title('Nuage de points du nombre généré Xn en fonction de Xn+1', fontsize=10)	
	xlabel('Xn+1')
	ylabel('Xn')
	show()
	

## Bit obtenu par rapport a l'indice i
# number of number generated must be under 500
def PlotCourbe():
	listBytes = list(map(int, strBytes))
	plot(arange(0,len(listBytes),1),listBytes)
	show()



### Exe ####

strBytes = BBS(1000)


### Plot ###

PlotCourbe()

PlotNuagePoints()



### Stat ###

CountBytes(strBytes)
# Pour 1 000 000 de nombres générés:
# La proportion de 1 est de 0.500079, celle de 0 est de 0.499921

CountDuoBytes(strBytes)
# Pour 1 000 000 de nombres générés:
# La proportion de 00 est de 0.249792, celle de 01 est de 0.250412, celle de 10 est : 0.249846, et celle de 11 est de 0.24995

CountFourBytes(strBytes)
# Pour 1 000 000 de nombres générés:
# On obtient les proportions suivantes pour chacun des demis octets existants : 
# [0.062464, 0.062244, 0.063016, 0.062628, 0.0635, 0.06206, 0.062548, 0.062612, 
# 0.06134, 0.062716, 0.06258, 0.062456, 0.061928, 0.063084, 0.062456, 0.062368]         

CountBits(strBytes)
# Pour 1 000 000 de nombres générés:
# On obtient ces données statistiques pour chacun des octets générés par la liste de bits : 
#
# Min :  0.003392                                                                                                      
# Max :  0.004456
# Moyenne :  0.00390625
# Ecart-type :  0.00018                                                                                                                           
#
# Ces données semblent raisonnable au regard du nombre d'octets compabilisé (125 000)
#
# Pour 10 000 000 de nombres générés:
# Min :  0.00372 
# Max :  0.0040464
# Moyenne :  0.00390625                                                                                                 
# Ecart type :  0.000053275 
# L'ecart-type est bien plus faible
