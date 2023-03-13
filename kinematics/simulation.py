import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.animation import FuncAnimation
from matplotlib.patches import RegularPolygon
from matplotlib.widgets import Slider, Button
import numpy as np
import math


class Simulation():

	def __init__(self, Kinematics):

		#Intialise Kinematics object
		self.kinematics = Kinematics

		#Initialise figure and figure properties
		self.fig = plt.figure()
		self.ax = plt.axes(projection='3d')
		plt.subplots_adjust(left=0.1, right=0.9, top=1.00, bottom=0.360)
		self.line = []

		for _ in range(6):
			line, = self.ax.plot3D([],[],[], 'black')
			self.line.append(line)

		self.moving_platform,  = self.ax.plot3D([],[],[], 'red')

		#Setting the axes properties
		self.ax.set_xlim3d([-250.0, 250.0])
		self.ax.set_xlabel('X')

		self.ax.set_ylim3d([-250.0, 250.0])
		self.ax.set_ylabel('Y')

		self.ax.set_zlim3d([0.0, 60.0])
		self.ax.set_zlabel('Z')

		#Slider properties
		px_slider = plt.axes([0.25,0.30,0.50,0.02])
		py_slider = plt.axes([0.25,0.25,0.50,0.02])
		pz_slider = plt.axes([0.25,0.20,0.50,0.02])
		alpha_slider = plt.axes([0.25,0.15,0.50,0.02])
		beta_slider = plt.axes([0.25,0.10,0.50,0.02])
		gamma_slider = plt.axes([0.25,0.05,0.50,0.02])

		#initialise slider
		self.slide_px = Slider(px_slider, 'px', -10, 10, valinit=0)
		self.slide_py = Slider(py_slider, 'py', -10, 10, valinit=0)
		self.slide_pz = Slider(pz_slider, 'pz', 30, 45, valinit=40)
		self.slide_alpha = Slider(alpha_slider, 'alpha', -1.57, 1.57, valinit=0)
		self.slide_beta  = Slider(beta_slider, 'beta', -1.57, 1.57, valinit=0)
		self.slide_gamma = Slider(gamma_slider, 'gamma', -1.57, 1.57, valinit=0)

		#intialise transition
		self.transition = [self.slide_px.val, self.slide_py.val,self.slide_pz.val, self.slide_alpha.val, self.slide_beta.val, self.slide_gamma.val]

		#reset button
		resetax = plt.axes([0.85, 0.025, 0.1, 0.04])
		self.button = Button(resetax, 'Reset', color='lightgoldenrodyellow', hovercolor='0.975')


	def _draw_platform(self, transition):

		#get parameters
		self._get_platform_params(transition)

		# draw basplate and topplate
		thetas = np.linspace(0, 360, 7)
		radius_b = self.kinematics.base_radius
		radius_p = self.kinematics.platform_radius

		xb=[]
		yb=[]
		zb = np.zeros(6)
		xp=[]
		yp=[]
		zp = np.zeros(6)

		for theta in thetas:
			xb.append(radius_b*math.cos(math.radians(theta)))
			yb.append(radius_b*math.sin(math.radians(theta)))
			xp.append(radius_p*math.cos(math.radians(theta)))
			yp.append(radius_p*math.sin(math.radians(theta)))

		self.ax.plot3D(xb,yb,np.zeros(len(xb)), 'blue')

		# draw servo points
		base_angles = self.kinematics.base_angles
		radius_s=self.kinematics.base_radius
		x =[]
		y=[]
		z = np.zeros(6)

		for angle in base_angles:
       			x.append(radius_s*math.cos(math.radians(angle)))
        		y.append(radius_s*math.sin(math.radians(angle)))

		#self.ax.plot3D(x,y,np.zeros(len(x)), '*')

		# draw link lengths:
		xl=[]
		yl=[]
		zl=[]

		for id, link in enumerate(self.kinematics.link_length):
			xl.append(link[0][0] + self.kinematics.base_joint[id][0][0])
			yl.append(link[1][0] + self.kinematics.base_joint[id][1][0])
			zl.append(link[2][0] + self.kinematics.base_joint[id][2][0])

		xl.append(xl[0])
		yl.append(yl[0])
		zl.append(zl[0])

		self.moving_platform.set_data(xl,yl)
		self.moving_platform.set_3d_properties(zl)

		#draw servo arm
		xs = []
		ys = []
		zs = []
		a = self.kinematics.servo_arm_length
		alpha = self.kinematics.get_alpha()
		beta = self.kinematics.beta

		for arm in range(6):
			if arm%2 == 1:
				xs.append(a*math.cos(alpha[arm])*math.cos(beta[arm]) + x[arm])
				ys.append(a*math.cos(alpha[arm])*math.sin(beta[arm]) + y[arm])
				zs.append(a*math.sin(alpha[arm]) + z[arm])
			else:
				xs.append(a*(-math.cos(alpha[arm]))*(-math.cos(beta[arm])) + x[arm])
				ys.append(a*(-math.cos(alpha[arm]))*(-math.sin(beta[arm])) + y[arm])
				zs.append(a*math.sin(alpha[arm]) + z[arm])


		#draw connections
		for ii in range(6):
			#self.ax.plot3D([x[ii], xs[ii], xl[ii]], [y[ii], ys[ii], yl[ii]], [z[ii], zs[ii], zl[ii]], 'black')
			self.line[ii].set_data([x[ii], xs[ii], xl[ii]], [y[ii], ys[ii], yl[ii]])
			self.line[ii].set_3d_properties([z[ii], zs[ii], zl[ii]])

		self.fig.canvas.draw_idle()


	def _adjust_slider(self):
		self.slide_px.on_changed(self._draw_platform)
		self.slide_py.on_changed(self._draw_platform)
		self.slide_pz.on_changed(self._draw_platform)
		self.slide_alpha.on_changed(self._draw_platform)
		self.slide_beta.on_changed(self._draw_platform)
		self.slide_gamma.on_changed(self._draw_platform)

	def _get_platform_params(self, val):
		self.transition = [self.slide_px.val, self.slide_py.val,self.slide_pz.val, self.slide_alpha.val, self.slide_beta.val, self.slide_gamma.val]
		self.kinematics.apply_transition(self.transition)

	def _reset(self, event):
    		self.slide_px.reset()
    		self.slide_py.reset()
    		self.slide_pz.reset()
    		self.slide_alpha.reset()
    		self.slide_beta.reset()
    		self.slide_gamma.reset()

	def get_transition_vals(self):
		return self.transition

	def start_simulation(self):
		self._adjust_slider()
		self.button.on_clicked(self._reset)
		plt.show()
