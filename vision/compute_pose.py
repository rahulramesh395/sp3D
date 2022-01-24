import math
import time

class ComputePose:

	def __init__(self, vision):
		self.vision = vision
		self.pose = None
		self.calibration_complete = False

		#intial position
		self.init_x = None
		self.init_y = None
		self.init_z = None

		#define thresholds
		z_threahold = None
		y_threshold = None
		x_threshold = None

	def _callibrate(self):

		x_init_pts = []
		y_init_pts = []
		z_init_pts = []
		count = 0

		time.sleep(10) #wating to stabilise

		while not self.calibration_complete:
			center = self._get_center()
			x_init_pts.append(center[0] if center is not None else None)
			y_init_pts.append(center[1] if center is not None else None)
			z_init_pts.append(self._get_area())

			if self.vision.get_parameters("recording_points"):
				count = count + 1
				print(count)

			if count > 2000:
				self.calibration_complete = True

		#filter None points
		x_init_pts = list(filter(None, x_init_pts))
		y_init_pts = list(filter(None, y_init_pts))
		z_init_pts = list(filter(None, z_init_pts))

		#get mean of recorded points
		self.init_x = sum(x_init_pts)/len(x_init_pts)
		self.init_y = sum(y_init_pts)/len(y_init_pts)
		self.init_z = sum(z_init_pts)/len(z_init_pts)

		print(self.init_x)
		print(self.init_y)
		print(self.init_z)

	def _get_center(self):
		center = self.vision.get_parameters("center")
		return center

	def _get_area(self):
		radius = self.vision.get_parameters("radius")
		if radius is not None:
			area = math.pi * radius**2
		else:
			area = None

		return area

	#def _get_height_change():

	def get_position(self):
		return xyz
