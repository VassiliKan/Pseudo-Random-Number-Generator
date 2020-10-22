This project contains two pseudo random number generator function. The first one, called unsecurePRNG (you should easily figure out why), is a congruential linear generator (x+1 = ax + b mod m). Depending of the value of m, a and b you choose, it could be a very unsecure PRNG, or be a least a little bit random.
The second, called BBS (from Blum Blum Shub) is supposed to be way more secure. The functions CountBits, CountDuoBits and CountFourBits are usefull to prove the randomness of this algorithm.

