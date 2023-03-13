from servo_control.servo_hat_library import PCA9685

class ServoControl:

	def __init__(self):
		#set pwm object
		self.pwm = PCA9685(0x40, debug=False)
		self.pwm.setPWMFreq(50)
		self.servo_id = [0,4,7,10,12,15]

	def _cal_pulse_from_angle(self, servo_id, angle):
		#calculate pulse of servos from angle
		pulse = (2000/180)*angle # refer https://www.waveshare.com/w/upload/1/1b/Servo_Driver_HAT_User_Manual_EN.pdf
		return pulse

	def actuate_servo(self, servo_pin, servo_id, angle):
		# send command to actuate servo
		pulse = self._cal_pulse_from_angle(servo_pin, angle)
		if servo_id%2 == 1:
			self.pwm.setServoPulse(servo_pin, 2500-pulse)
		else:
			self.pwm.setServoPulse(servo_pin, 500+pulse)

