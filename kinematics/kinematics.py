# Refer https://web.archive.org/web/20130506134518/http://www.wokinghamu3a.org.uk/Maths%20of%20the%20Stewart%20Platform%20v5.pdf for math
import math
import numpy as np

class Kinematics:

	def __init__(self):

		# class variables
		self.alpha = [0]*6
		self.servo_arm_length = 15
		self.leg_length = 100
		self.base_radius = 150
		self.platform_radius = 75
		self.base_joint = [None] * 6
		self.platform_joint = [None] * 6 
		self.link_length = [None] * 6
		self.cord_q = [None] * 6
		PI = math.pi
		self.beta = [0,2*PI/3, 2*PI/3,-2*PI/3, -2*PI/3, 0]
		self.platform_angles = [317, 347, 77, 107.1, 193.9, 227.8]
		self.base_angles = [287, 12.9, 47.1, 132.9, 167.1, 252.9]

		# compute joint parameters
		for i in range(6):
                	xb = self.base_radius * math.cos(math.radians(self.base_angles[i]))
                	yb = self.base_radius * math.sin(math.radians(self.base_angles[i]))
                	zb = 0
                	self.base_joint[i] = np.array([[xb],[yb], [zb]])

		for i in range(6):
			xp = self.platform_radius * math.cos(math.radians(self.platform_angles[i]))
			yp = self.platform_radius * math.sin(math.radians(self.platform_angles[i]))
			zp = 0
			self.platform_joint[i] = np.array([[xp], [yp], [zp]])



	def _compute_alpha(self):
		try:
			for i in range(len(self.link_length)):
				L = self._compute_mag(self.link_length[i])**2 - (self.leg_length**2 - self.servo_arm_length**2)
				M = 2 * self.servo_arm_length * (self.cord_q[i][2] - self.base_joint[i][2])
				N = 2 * self.servo_arm_length * (math.cos(self.beta[i])*(self.cord_q[i][0] - self.base_joint[i][0]) + math.sin(self.beta[i])*(self.cord_q[i][1] - self.base_joint[i][1]))
				self.alpha[i] = math.asin(L/math.sqrt(M**2 + N**2)) - math.atan(N/M)

		except:
			print("Limit Reached")

	def _compute_link_length(self, transition):
		T = np.array([[transition[0]],[transition[1]],[transition[2]]])
		rotations = self._get_rotation_matrix(transition[3:])
		for i in range(len(self.link_length)):
			self.cord_q[i] = T + np.dot(rotations, self.platform_joint[i])
			self.link_length[i] =  (T + np.dot(rotations, self.platform_joint[i])) - self.base_joint[i]
 

	def _get_rotation_matrix(self, rotations):
		phi = math.radians(rotations[0])
		theta = math.radians(rotations[1])
		psi = math.radians(rotations[2])

		Rx = np.array([[1, 0, 0],[0, math.cos(phi), -math.sin(phi)],[0, math.sin(phi), math.cos(phi)]])
		Ry = np.array([[math.cos(theta),0,  math.sin(theta)],[0, 1, 0],[-math.sin(theta), 0, math.cos(theta)]])
		Rz = np.array([[math.cos(psi), -math.sin(psi), 0],[math.sin(psi), math.cos(psi), 0],[0, 0, 1]])

		R = np.dot(Rz,np.dot(Ry,Rx))
		return R

	def _compute_mag(self, array):
		sum_squares = 0
		for i in array:
			 sum_squares = sum_squares + i**2

		return math.sqrt(sum_squares[0])

	def get_alpha(self, units="rad"):
		if units == "deg":
			return [alpha*180/math.pi for alpha in self.alpha]

		return self.alpha


	def apply_transition(self, transition):
		self._compute_link_length(transition)
		self._compute_alpha()


