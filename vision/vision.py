import cv2
import imutils
import numpy as np
import atexit
import time

class Vision:
	def __init__(self):
		self.capture = None
		self.mask = None
		self.frame = None
		self.show = True
		self.parameters = {"radius": None, "center": [None, None], "recording_points": False}
		atexit.register(self._clean_up)

	def _clean_up(self):
		print('Exiting vision ...')
		self.capture.release()
		cv2.destroyAllWindows()

	def _start_cam(self):
		# start camera
		self.capture = cv2.VideoCapture(0)

	def _detect_red_color(self):
		self.frame = self._read_frame()

		# Converting the image to hsv
		frame = imutils.resize(self.frame, width=1000)
		frame = imutils.rotate(self.frame, angle=180)
		hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

		# define range of red color in masks
		lower_red = np.array([170,120,70])
		upper_red = np.array([180,255,255])

		# threshold the HSV image using inRange function to get only red colors
		mask = cv2.inRange(hsv, lower_red, upper_red)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)
		self.mask = mask

	def _read_frame(self):
		_, frame = self.capture.read()
		return frame

	def _show_frame(self):
		#show frame and mask
		cv2.imshow("Original", self.frame)
		cv2.imshow("Mask", self.mask)
		if cv2.waitKey(1) == 27:
			self.show = False

	def _draw_contour(self):
		cnts = cv2.findContours(self.mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
		center = None
		radius = None
		# only proceed if at least one contour was found
		if len(cnts)>0:
			recording_points = True
			# find the largest contour in the mask, then use
			# it to compute the minimum enclosing circle and
			# centroid
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			# only proceed if the radius meets a minimum size
			if radius > 10:
				# draw the circle and centroid on the frame,
				# then update the list of tracked points
				cv2.circle(self.frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
				cv2.circle(self.frame, center, 5, (0, 0, 255), -1)
		else:
			recording_points = False

		self.parameters = {"radius": radius, "center": center, "recording_points": recording_points}

	def _detect_object(self):
		#start cam
		self._start_cam()
		while self.show:
			#detect object
			self._detect_red_color()
			#draw contour around detected object
			self._draw_contour()
			#show the result
			self._show_frame()

	def get_parameters(self, par):
		return self.parameters[par]
