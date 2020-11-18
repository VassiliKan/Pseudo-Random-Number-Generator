import random
import matplotlib.pyplot as plt
import numpy as np
import math
import time


def Gener(a, b, m, x0, nbLoop):
	bits = ""
	xn = x0		
	for i in range(nbLoop):
		if i % (nbLoop / 10) == 0:
			print("... Processing", int(i / (nbLoop/100)), "%")
		xn = ((a * xn + b) % m)
		if xn % 2 == 0:
			bits += "0"
		else:
			bits += "1"
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
		elif subStr == '10':			
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
	x = listXn[:-1]
	y = listXn[1:]
	scatter(x=x, y=y)
	show()
	

## Bit obtenu par rapport a l'indice i
# number of number generated must be under 500
def PlotCourbe():
	listBytes = list(map(int, strBytes))
	print(listBytes)
	plot(arange(0,len(listBytes),1),listBytes)
	show()
	

### Exe ###

strBytes = Gener(31, 3, 9576890767, 411, 1000)



### Plot ###

#PlotCourbe()

#PlotNuagePoints()


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
# On obtient les proportions suivantes pour chacun des demis octets existants : 
# [0.056792, 0.059792, 0.06474, 0.059784, 0.064796, 0.068888, 0.064392, 0.060256,
#  0.061304, 0.064752, 0.068388, 0.063936, 0.0612, 0.064328, 0.060824, 0.055828] 
# 
# - Etendue :  0.013060                                                                                       
# - Moyenne :  0.0625                                                                                                     
# - Ecart type :  0.0035583

CountBits(strBytes)
# Pour 1 000 000 de nombres générés:
# On obtient ces données statistiques pour chacun des octets générés par la liste de bits : 
# - Etendue :  0.00212                                                                                                    
# - moyenne :  0.00390625                                                                                                 
# - ecart type :  0.00037958                                                                                                                         
#
# Ces données semblent raisonnable au regard du nombre d'octets compabilisé (125 000)
#
# Pour 10 000 000 de nombres générés:
# - Etendue :  0.00181279                                                                                      
# - Moyenne :  0.00390625                                                                                                 
# - Ecart type :  0.00034033


