import random
from matplotlib.pyplot import *
from numpy import *
import math



listXn=[]


def Gener(a, b, m, x0, nbLoop):
	bits = ""
	xn = x0		
	for i in range(nbLoop):
		listXn.append(xn)
		#if i % (nbLoop / 10) == 0:
			#print("... Processing", int(i / (nbLoop/100)), "%")
		xn = ((a * xn + b) % m)
		if xn % 2 == 0:
			bits += "0"
			print("0")
		else:
			bits += "1"
			print("1")
	print("... Processing 100% \n... Done !\n")
	return bits


##Proportion de 0 et de 1 :
def CountBytes(string):
	nb1 = 0
	nb0 = 0
	lenght = len(string)
	for i in string:
		if i == '0':
			nb0 = nb0 + 1
		else:
			nb1 = nb1 + 1
	print("La proportion de '1' est : ", nb1 / lenght, ", celle de '0' est de  ", nb0 / lenght, "\n")
	

def CountDuoBytes(string):
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
		elif subStr == '11':			
			nb11 = nb11 + 1	
	print("La proportion de la sous chaine '00' est : ", nb00 / lenght, ", celle de '01' est de  ", \
			nb01 / lenght, ", celle de '10' est : ", nb10 / lenght, ", celle de '11' est de  ", nb11 / lenght, "\n")



def CountFourBytes(string):
	listCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ## dico
	lenght = len(string) / 4
	listCompare = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

	for i in range(0, len(string), 4):
		subStr = string[i:i+4]
		value = int(subStr, 2)
		if value <= 15:
			listCounter[listCompare.index(int(subStr, 2))] += 1

	for j in range(len(listCounter)):
		listCounter[j] = listCounter[j] / lenght

	print("Les differentes proportion des sous chaines composees de 4 bits sont, par ordre croissant : \n", listCounter, "\n")
	print("Voici les differentes donnees statistiques calculees a partir des differentes proportion des sous chaines composees de 8 bits, soit un octet : ")
	print(" - Etendue : ", max(listCounter) - min(listCounter))
	print(" - moyenne : ", np.mean(listCounter))
	print(" - ecart type : ", np.std(listCounter), '\n')


def CountBits(string):
	listCounter = [0 for x in range(256)]
	listCompare = [x for x in range(256)]

	for i in range(0, len(string), 8):
		subStr = string[i:i+8]
		value = int(subStr, 2)
		if value <= 255:
			listCounter[listCompare.index(int(subStr, 2))] += 1
			
	for j in range(len(listCounter)):
		listCounter[j] = listCounter[j] / (len(string) / 8)

	print("Voici les differentes donnees statistiques calculees a partir des differentes proportion des sous chaines composees de 8 bits, soit un octet : ")
	print(" - Etendue : ", max(listCounter) - min(listCounter))
	print(" - moyenne : ", np.mean(listCounter))
	print(" - ecart type : ", np.std(listCounter))
	
	
	
## Nuage de point de coordonnées (xn+1, xn)
## Semble uniformément répartie
def PlotNuagePoints():
	x = listXn[:-1]   #xn
	y = listXn[1:]    #xn+1
	scatter(x=x, y=y)
	title('Nuage de points du nombre généré Xn+1 en fonction de Xn', fontsize=10)
	xlabel('Xn')
	ylabel('Xn+1')
	show()
	
	
def PlotPariteNuagePoint():
	y = list(map(int, strBytes))
	x = arange(0, len(y),1)
	scatter(x=x, y=y)
	title('Bit généré en fonction de son rang n', fontsize=10)
	xlabel('Rang n (entier)')
	ylabel('Valeur du bit')
	show()



## Bit obtenu par rapport a l'indice i
# number of number generated must be under 500
def PlotPariteCourbe():
	listBytes = list(map(int, strBytes))
	plot(arange(0,len(listBytes),1),listBytes)
	title('Bit généré en fonction de son rang n', fontsize=10)
	xlabel('Rang n (entier)')
	ylabel('Valeur du bit')
	show()
	


### Exe ###

###        Gener(a, b, m, x0, nbLoop)
#strBytes = Gener(314125421, 1, 10**8, 11, 50)
strBytes = Gener(4	, 2, 9, 11, 25)


### Plot ###

#PlotPariteCourbe()

PlotNuagePoints()

#PlotPariteNuagePoint()

### Stat ###

CountBytes(strBytes)
# Pour 1 000 000 de nombres générés:
# La proportion de '1' est 0.499196 , celle de '0' est de 0.500804 

CountDuoBytes(strBytes)
# Pour 1 000 000 de nombres générés:
# La proportion de la sous chaine '00' est :  0.2426 , celle de '01' est de   0.258046,
# celle de '10' est :  0.258362, celle de '11' est de   0.0

CountFourBytes(strBytes)
# Pour 1 000 000 de nombres générés:
# - Etendue :  0.013060
# - Ecart type :  0.0035583

CountBits(strBytes)
# Pour 1 000 000 de nombres générés:
# On obtient ces données statistiques pour chacun des octets générés par la liste de bits : 
# - Etendue :  0.00212                                                                                                    
# - ecart type :  0.00037958                                                                                                                         
#
# Ces données semblent raisonnable au regard du nombre d'octets compabilisé (125 000)
#
# Pour 10 000 000 de nombres générés:
# - Etendue :  0.00181279                                                                                                
# - Ecart type :  0.00034033


