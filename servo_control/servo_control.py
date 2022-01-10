from servo_control.servo_hat_library import PCA9685

class ServoControl:

	def __init__(self):
		#set pwm object
		self.pwm = PCA9685(0x40, debug=False)
		self.pwm.setPWMFreq(50)

	def _cal_pulse_from_angle(self, servo_id, angle):
		#calculate pulse of servos from angle
		pulse = 500 + (2000/180)*angle # refer https://www.waveshare.com/w/upload/1/1b/Servo_Driver_HAT_User_Manual_EN.pdf
		return pulse

	def actuate_servo(self, servo_id, angle):
		# send command to actuate servo
		pulse = self._cal_pulse_from_angle(servo_id, angle)
		self.pwm.setServoPulse(servo_id, pulse)


