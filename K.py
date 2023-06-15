from math import pi
from math import sin, cos, sqrt
Angle = 160*(pi/180)
Projectile = 4
Target = 8
k1 = 1 - (2*Projectile*Target/((Projectile+Target)**2))*(1-cos(Angle))
k2 = ((sqrt((Target**2)-((Projectile**2)*sin(Angle))) + (Projectile*cos(Angle)))/(Target + Projectile))**2
mr = Projectile/Target
k3 = ((sqrt(1-(mr**2)*sin(Angle)**2) + mr*cos(Angle))/(1+mr))**2
print(k1, k2, k3)