from numpy import *
from matplotlib.pyplot import *


primeList1 = [
231231251, 231231257, 231231269, 231231289,	231231293, 231231323, 231231337, 231231347, 231231353, 231231367,
231231391, 231231409, 231231439, 231231503, 231231551, 231231557, 231231613, 231231731, 231231743, 231231757,
231231779, 231231823, 231231827, 231231829, 231231853, 231231859, 231231863, 231231901, 231231911, 231231947,
231231971, 231231989, 231231997, 231232003, 231232009, 231232061, 231232081, 231232091, 231232097, 231232117,
231232123, 231232153, 231232159, 231232217, 231232231, 231232237, 231232241, 231232247, 231232279, 231232291,
231232307, 231232321, 231232357, 231232367, 231232373, 231232381, 231232411, 231232427, 231232429, 231232471,
231232513, 231232541, 231232553, 231232559, 231232601, 231232609, 231232613, 231232637, 231232667, 231232681,
231232697, 231232699, 231232723, 231232783, 231232787, 231232789, 231232817, 231232843, 231232853, 231232867,
231232873, 231232877, 231232889, 231232931, 231232949, 231233027, 231233029, 231233039, 231233063, 231233069,
231233081, 231233087, 231233089, 231233129, 231233141, 231233183, 231233203, 231233221, 231233227, 231233243,
231233251, 231233257, 231233263, 231233291, 231233293, 231233341, 231233347, 231233407, 231233411, 231233417,
231233441, 231233447, 231233459, 231233479, 231233491, 231233531, 231233533, 231233543, 231233573, 231233579,
231233603, 231233623, 231233633, 231233641, 231233687, 231233689, 231233693, 231233701, 231233713, 231233729,
231233759, 231233773, 231233801, 231233903, 231233909, 231233911, 231233917, 231233939, 231233941, 231233953]

primeList2 = [
231233993, 231233999, 231234013, 231234041, 231234061, 231234067, 231234077, 231234083, 231234097, 231234109,
231234131, 231234151, 231234181, 231234191, 231234209, 231234229, 231234233, 231234251, 231234253, 231234271,
231234277, 231234281, 231234287, 231234293, 231234299, 231234317, 231234319, 231234329, 231234359, 231234401,
231234403, 231234449, 231234457, 231234473, 231234529, 231234569, 231234587, 231234613, 231234623, 231234631,
231234643, 231234683, 231234737, 231234767, 231234791, 231234803, 231234823, 231234827, 231234851, 231234853,
231234863, 231234923, 231234937, 231234947, 231234953, 231235007, 231235021, 231235027, 231235049, 231235057,
231235061, 231235063, 231235091, 231235093, 231235097, 231235117, 231235141, 231235171, 231235229, 231235259,
231235267, 231235271, 231235289, 231235297, 231235321, 231235331, 231235349, 231235373, 231235391, 231235393,
231235421, 231235463, 231235469, 231235489, 231235519, 231235579, 231235591, 231235597, 231235637, 231235651,
231235657, 231235663, 231235673, 231235699, 231235703, 231235729, 231235769, 231235783, 231235799, 231235831,
231235847, 231235877, 231235889, 231235891, 231235919, 231235943, 231235969, 231235981, 231235987, 231236003,
231236011, 231236063, 231236087, 231236107, 231236119, 231236123, 231236143, 231236147, 231236149, 231236153,
231236171, 231236179, 231236183, 231236189, 231236207, 231236221, 231236231, 231236233, 231236237, 231236293,
231236311, 231236321, 231236371, 231236389,	231236407, 231236419, 231236449, 231236491, 231236519, 231236539,
231236557, 231236561, 231236573, 231236587, 231236591, 231236609, 231236623, 231236627, 231236639, 231236653,
231236659, 231236689, 231236729, 231236741, 231236801, 231236809, 231236813, 231236833, 231236861, 231236881,
231236893, 231236903, 231236911, 231236927, 231236959, 231236977, 231236987, 231237023, 231237047, 231237067,
231237073, 231237109, 231237119, 231237121,	231237143, 231237151, 231237157, 231237191, 231237199, 231237241,
231237263, 231237283, 231237289, 231237313,	231237341, 231237367, 231237373, 231237389, 231237431, 231237439,
231237443, 231237493, 231237521, 231237527,	231237529, 231237541, 231237571, 231237613, 231237631, 231237637,
231237667, 231237673, 231237683, 231237691,	231237707, 231237731, 231237737, 231237761, 231237767, 231237803,
231237833, 231237857, 231237871, 231237899, 231237907, 231237911, 231237913, 231237949, 231237953, 231238001]


listBit = []
listXn = []


def mod3plus4(a):
	if a % 4 == 3:
		return True
	else:
		return False
		
def getPQ(list):
	for i in range(len(list)):
		if (mod3plus4(list[i])):
			return list[i]
	return -1
	
	
def pgcd(a,b) :
	while a%b != 0 :
		a, b = b, a%b
	return b


def findX(n):
	for i in range (round(n/2), n):
		if pgcd(i,n) == 1:
			return i
	return -1
	
	
def BBS(nb):
	p = getPQ(primeList1)
	q = getPQ(primeList2)
	n = p * q	
	x = findX(n)
	x0 = xi = x**2 % n
	bits = ""
	for i in range(nb):
		#listXn.append(xi)
		xiPlus1 = xi**2 % n
		if xi % 2 == 0:
			#listBit.append(0)
			bits += "0"
		else:
			#listBit.append(1)
			bits += "1"
			
		xi = xiPlus1 
	return bits

##Proportion de 0 et de 1 :
def CountBits():
	nb1 = 0
	nb0 = 0
	for i in listBit:
		if i == 0:
			nb0 = nb0 + 1
		else:
			nb1 = nb1 + 1
	print("La proportion de 1 est : ", nb1 / len(listBit), ", celle de 0 est de  ", nb0 / len(listBit))
	

def CountDuoBits():
	nb00 = 0
	nb01 = 0
	nb10 = 0
	nb11 = 0
	tailleEchantillon = len(listBit) / 2
	for i in range(0, len(listBit), 2):
		xi = listBit[i]
		xiPlusUn = listBit[i+1]
		if xi == 0 and xiPlusUn == 0:
			nb00 = nb00 + 1
		if xi == 0 and xiPlusUn == 1:
			nb01 = nb01 + 1
		if xi == 1 and xiPlusUn == 0:
			nb10 = nb10 + 1
		if xi == 1 and xiPlusUn == 1:
			nb11 = nb11 + 1	
	print("La proportion de 00 est : ", nb00 / tailleEchantillon, ", celle de 01 est de  ", nb01 / tailleEchantillon, "La proportion de 10 est : ", nb10 / tailleEchantillon, ", celle de 11 est de  ", nb11 / tailleEchantillon)


def CountFourBits():

	
## Nuage de point de coordonnées (xn+1, xn)
## Semble uniformément répartie
def PlotNuagePoints():
	x = listXn[:-1]
	y = listXn[1:]
	scatter(x=x, y=y)
	show()
	

## Bit obtenu par rapport a l'indice i
def PlotCourbe():
	plot(arange(0,400,1),listBit)
	show()


#BBS(100000)
print(BBS(100))

#CountBits()
#La proportion de 1 est de 0.500079, celle de 0 est de 0.499921

#CountDuoBits()
#La proportion de 00 est de 0.249792, celle de 01 est de 0.250412, celle de 10 est : 0.249846, et celle de 11 est de 0.24995

CountFourBits()


