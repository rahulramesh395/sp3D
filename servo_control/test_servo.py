from servo_hat_library import PCA9685
import time

pwm = PCA9685(0x40, True)
pwm.setPWMFreq(50)
ids = [0, 4, 12]
#while True:
#	# setServoPulse(2,2500)
#	for j in ids:
#		for i in range(500,2500,10):
#			pwm.setServoPulse(j,i)
#			time.sleep(0.0002)
#
#		for i in range(2500,500,-10):
#			pwm.setServoPulse(j,i)
#			time.sleep(0.0002)

# Driving to home
while True:
	time.sleep(2)
	print("Reseting servo position")
	for id in ids:
        	pwm.setServoPulse(id, 500)

	time.sleep(1.5)
	# Input
	print("Enter the servo angular displacement values (in degrees) ")
	servo1 = input("Servo 1: ")
	servo2 = input("Servo 2: ")
	servo3 = input("Servo 3: ")

	servo_angle = [servo1, servo2, servo3] 

	# Actuation
	print("Actuating servos ...")
	for i, servo_id in enumerate(ids):
		pulse = 500 + (2000/180)*int(servo_angle[i])
		pwm.setServoPulse(servo_id, pulse)

