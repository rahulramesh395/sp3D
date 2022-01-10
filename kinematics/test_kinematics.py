from kinematics import Kinematics
import math
from simulation import Simulation

S = Simulation()
k = Kinematics()

#k._compute_link_length([0,0,46,0,0,0,0])
#print(k.link_length)
#alpha = k.get_alpha()

#for a in alpha:
#	print(a*180/math.pi)

S.start_simulation()
