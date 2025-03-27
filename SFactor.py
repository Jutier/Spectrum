from math import cos, radians
import K as Kpy



def dE(energy, dDict):
	"""Return the expected dE/dx value for the energy, based on dDict

	Parameters:
	energy : float
		The desired energy
	dDict : dict
		A dictionary in the form of {energy:dE/dx}
		such that energy is in it's range

	Return:
	float
		the expected dE/dx for that energy

	Raise:
	IndexError
		If the specified energy is not within the given dDict range
	"""

	eList = list(dDict.keys())
	if energy in eList:
		return dDict[energy]

	elif energy > eList[0] and energy < eList[-1]:
		
		i = 0
		while energy > eList[i]:
			i += 1

		slope = (dDict[eList[i]] - dDict[eList[i-1]]) / (eList[i] - eList[i-1])
		return  dDict[eList[i-1]] + slope * (energy - eList[i-1])

	else:
		raise IndexError(f'Your Stopping list does not comprehend your energy({energy}).')


def SFactor(theta1, theta2, Projectile, Target, E0, dDict):
	"""Return the Energy Loss Factor [S] for a given case (surface aprox.)

	It gets the Energy Loss dE/dx from the fuction dE() with the given dDict.
	It also calculates the theta angle for the colision with the two given angles,
	it should work fine if you know what you're doing, but please be aware.

	Parameters:
	theta1 : float
		The angle between the sample and the bean
	theta2 : float
		The angle between the sample and the detector
	Projectile : str
		The symbol for the bean ion
	Target : str
		The symbol for the target atom
	E0 : float
		Bean energy, any form of eV should work
	dDict : dict
		The dictionary for the dE() function

	Return:
	float
		The S Factor

	"""
	theta = 180 - theta1 - theta2 # The angle between the bean and the detector
	K = Kpy.KFactor(Projectile, Target, theta)

	return (K*dE(E0, dDict))/cos(radians(theta1)) + dE(K*E0, dDict)/cos(radians(theta2))

