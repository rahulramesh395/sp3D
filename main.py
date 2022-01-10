from servo_control.servo_control import ServoControl
from kinematics.kinematics import Kinematics
from kinematics.simulation import Simulation as KineSimulation
import math
import threading

def main():

	# init objects
	K = Kinematics()
	S = ServoControl()
	Sim = KineSimulation()

	Sim.start_simulation()
	while True:
		transition = Sim.get_transition()
		print(transition)
		print(K.get_alpha())

	#for i in range(6):
	#	t = input('Enter transition ')
	#	transition.append(int(t))

	#K.apply_transition(transition)

	#servo_angles = K.get_alpha()
	#id = [0,4,12,9,10,15]

	#for i, angle in enumerate(servo_angles):
	#	print(angle)
	#	S.actuate_servo(id[i], abs(angle))

if __name__=="__main__":
	main()
