from math import radians, sin, cos, sqrt
from sys import argv
import json

with open("AtomMass.JSON", 'r') as f:
	Mass = json.load(f)

def KFactor(P, T, A):
	"""Calculates the Kinematic Factor K
	
	Can work with both symbols of atoms, from wich it gets the mass
	or with given masses

	Parameters:
	P : str or float
		The projectile, atomic symbol or mass
	T : str or float
		The target, atomic symbol or mass
	A : float
		Angle in degrees, from the change in trajectory, not the directions

	Return:
		float
		K factor rounded to 4 decimal points

	"""
	A = radians(A)
	P = (Mass[P] if P.isalpha() else int(P))
	T = (Mass[T] if T.isalpha() else int(T))
	MR = P/T

	#K7 = 1 - (2*P*T/((P+T)**2))*(1-cos(A)) # Chu Eq. 2.7, should be used with cof coordinates
	#K6 = ((sqrt((T**2)-((P**2)*sin(A))) + (P*cos(A)))/(T + P))**2 # Chu Eq. 2.6a, somehow doesn't work
	K = ((sqrt(1-(MR**2)*sin(A)**2) + MR*cos(A))/(1+MR))**2 # Chu Eq. 2.6b, matches with chu tables

	return round(K, 4)

if __name__ == "__main__":
	P, T, A = argv[1], argv[2], float(argv[3])
	print(KFactor(P, T, A))
