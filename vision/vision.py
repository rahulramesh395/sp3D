import cv2 as cv
import imutils
import numpy as np
import atexit
import time

class Vision:
	def _init_(self):
		self.capture = None
		self.mask = None

		atexit.register(self._clean_up)

	def _clean_up(self):
		print('Exiting vision ...')
		self.capture.release()
		cv.destroAllWIndows()

	def _start_cam(self):
		# start camera
		self.capture = cv.VideoCapture(0)

		# wait for camera to stabilize
		time.sleep(1)

	def _detect_red_color(self):
		frame = self._read_frame()
		# Converting the image to hsv
		# resize the frame, inverted ("vertical flip" w/ 180degrees),
		# blur it, and convert it to the HSV color space
		frame = imutils.resize(frame, width=600)
		frame = imutils.rotate(frame, angle=180)
		# blurred = cv2.GaussianBlur(frame, (11, 11), 0)
		hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

		# define range of red color in HSV
		lower_red = np.array([160,50,50])
		upper_red = np.array([180,255,255])

		# threshold the HSV image using inRange function to get only red colors
		mask = cv.inRange(hsv, lower_red, upper_red)
		mask = cv.erode(mask, None, iterations=2)
		mask = cv.dilate(mask, None, iterations=2)
		self.mask = mask

	def _read_frame(self):
		_, frame = self.capture.read()
		return frame

	def _draw_contour(self):
		cnts = cv.findContours(self.mask.copy(),cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
		cnts = cnts[0] if imutils.is_cv2() else cnts[1]
		center = None
		# only proceed if at least one contour was found
		if len(cnts) > 0:
			# find the largest contour in the mask, then use
			# it to compute the minimum enclosing circle and
			# centroid
			c = max(cnts, key=cv.contourArea)
			((x, y), radius) = cv.minEnclosingCircle(c)
			M = cv.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

			# only proceed if the radius meets a minimum size
			if radius > 10:
				# draw the circle and centroid on the frame,
				# then update the list of tracked points
				cv.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
				cv.circle(frame, center, 5, (0, 0, 255), -1)

	def detect_object(self):
		self._start_cam()
		while True:
			self._detect_red_color()
			self._draw_contour()

	def get_position(self):
		return xyz 


