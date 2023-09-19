from math import cos, pi
import K as Kpy

#l = list(map(lambda x: round(x, 1), np.arange(0.9, 1.9, 0.1))) + list(map(lambda x: round(x, 2),np.arange(2.0, 2.6, 0.25)))
#for i in l:
#	print(f"{i}: , ",end='')


dDict = {0.9:43.7, 1.0:42.91, 1.1:42.02, 1.2:41.06, 1.3:40.08, 1.4:39.10, 1.5:38.13, 1.6:37.19, 1.7:36.28, 1.8:35.40, 2.0:33.75, 2.25:31.87, 2.5:30.19}

def dE(energy):
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
		raise Exception('Your Stopping list does not  comprehend your energy.')


def SFactor(theta1, theta2, Projectile, Target, E0):
	K = Kpy.KFactor(Projectile, Target, 180-theta2) #Using theta2 as the angle is not right but it works in this case
	return (K*dE(E0))/cos(theta1*pi/180) + dE(K*E0)/cos(theta2*pi/180)

for ele in ['Al', 'O', 'S', 'Cu']:
	print(ele, "=", 5765/SFactor(0, 15, 'He', ele, 2.48), "A/ch")
	
print(dE(1.9354))