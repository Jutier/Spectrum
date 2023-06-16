from math import pi
from math import sin, cos, sqrt
from sys import argv
import json

with open("ElementMass.JSON") as f:
	Mass = json.loads(f)
	print(Mass)

def Kfactor(P, T, A):
	A = (A/180)*pi
	MR = P/T
	#k1 = 1 - (2*Projectile*Target/((Projectile+Target)**2))*(1-cos(Angle))
	#k2 = ((sqrt((Target**2)-((Projectile**2)*sin(Angle))) + (Projectile*cos(Angle)))/(Target + Projectile))**2
	K = ((sqrt(1-(MR**2)*sin(A)**2) + MR*cos(A))/(1+MR))**2
	return round(K, 4)

if __name__ == "__main__":
	P, T, A = Mass[argv[1]], Mass[argv[2]], float(argv[3])
	print(Kfactor(P, T, A))