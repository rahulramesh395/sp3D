from servo_hat_library import PCA9685
import time

pwm = PCA9685(0x40, True)
pwm.setPWMFreq(50)
ids = [0, 4, 7, 10, 12, 15]
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
	for i, id in enumerate(ids):
		if i%2 == 1:
			pwm.setServoPulse(id, 2500)
		else:
			pwm.setServoPulse(id, 500)
            

	time.sleep(1.5)
	# Input
	print("Enter the servo angular displacement values (in degrees) ")
	servo1 = input("Servo 1: ")
	servo2 = input("Servo 2: ")
	servo3 = input("Servo 3: ")
	servo4 = input("Servo 4: ")
	servo5 = input("Servo 5: ")
	servo6 = input("Servo 6: ")
	
	servo_angle = [servo1, servo2, servo3, servo4, servo5, servo6]
# 	servo_angle = [servo1]
	

	# Actuation
	print("Actuating servos ...")
	for i, servo_id in enumerate(ids):
		pulse = (2000/180)*int(servo_angle[i])
		if i%2 == 1:
			pwm.setServoPulse(servo_id, 2500 - pulse)
		else:
			pwm.setServoPulse(servo_id, 500 + pulse)            

