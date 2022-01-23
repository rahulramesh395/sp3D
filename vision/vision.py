import cv2
import imutils
import numpy as np
import atexit
import time

class Vision:
	def __init__(self):
		self.capture = None
		self.mask = None
		self.show = True

		atexit.register(self._clean_up)

	def _clean_up(self):
		print('Exiting vision ...')
		self.capture.release()
		cv.destroAllWIndows()

	def _start_cam(self):
		# start camera
		self.capture = cv2.VideoCapture(0)

	def _detect_red_color(self):
		ret, frame = self.capture.read()

		# Converting the image to hsv
		# resize the frame, inverted ("vertical flip" w/ 180degrees),
		# blur it, and convert it to the HSV color space
		frame = imutils.resize(frame, width=600)
		frame = imutils.rotate(frame, angle=180)

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		# define range of red color in HSV
		lower_red = np.array([160,50,50])
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
		#cv.imshow("Original", self.frame)
		cv2.imshow("Mask", self.mask)
		if cv2.waitKey(1) == 27:
			self.show = False

	def _draw_contour(self):
		cnts = cv.findContours(self.mask.copy(),cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
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
		while self.show:
			self._detect_red_color()
			self._show_frame()
			#self._draw_contour()

	def get_position(self):
		return xyz 


