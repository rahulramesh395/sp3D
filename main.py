from servo_control.servo_control import ServoControl
from kinematics.kinematics import Kinematics
from kinematics.simulation import Simulation as KineSimulation
import math
import threading
import time

def actuate_servos(Servo, servo_angles):
	id = [0,4,7,10,12,15]
	for i, angle in enumerate(servo_angles):
		Servo.actuate_servo(id[i], abs(angle))

def get_servo_angles_and_actuate(Kinematics, Servo):

	while True:
		time.sleep(1)
		actuate_servos(Servo, Kinematics.get_alpha("deg"))

def main():

	#initialise object instances
	kine = Kinematics()
	servo = ServoControl()

	# start thread to get servo angles and actuate servos
	threading.Thread(target=get_servo_angles_and_actuate, args=(kine,servo,)).start()

	Sim = KineSimulation(kine)
	Sim.start_simulation()


if __name__=="__main__":
	main()
