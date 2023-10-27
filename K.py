from math import pi
from math import sin, cos, sqrt
from sys import argv
import json

with open("AtomMass.JSON", 'r') as f:
	data = f.read()
	Mass = json.loads(data[17:])

def KFactor(P, T, A):
	A = (A/180)*pi
	MR = Mass[P]/Mass[T]
	#k1 = 1 - (2*Projectile*Target/((Projectile+Target)**2))*(1-cos(Angle))
	#k2 = ((sqrt((Target**2)-((Projectile**2)*sin(Angle))) + (Projectile*cos(Angle)))/(Target + Projectile))**2
	K = ((sqrt(1-(MR**2)*sin(A)**2) + MR*cos(A))/(1+MR))**2
	return round(K, 4)

if __name__ == "__main__":
	P, T, A = argv[1], argv[2], float(argv[3])
	print(KFactor(P, T, A))
