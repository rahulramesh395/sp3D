# sp3D
---------

## Required HW

1. RaspberryPi 3b+ 
2. Servo Driver Hat for RaspberryPi (16-Channel, 12-bit, I2C)
3. MG996R Servo Motor
4. PiCam

## Installation 

##### Required Packages
1. pip3
2. python 3.7 (or above)
3. pipenv

##### On a raspberry pi with the rasbian OS,

1. `sudo update`
2. `sudo upgrade` 
3. `git clone https://github.com/rahulramesh395/sp3D.git` 
4. `cd sp3D`
5. `pipenv install`

**NOTE:** Skip steps 1 and 2 if running on a any other Linux machine

## Run 
1. `cd sp3D` 
2. `pipenv shell`
3. `python main.py`

Enjoy!!


## File Structure
```
/sp3D
	|_ main.py
	|_ README.md
	|_ kinematics
		|_ kinematics.py 
		|_ simulation.py
	|_ servo_control
		|_ servo_hat_library.py
		|_ servo_control.py
	|_ vision  (Under Contruction !!!)
		|_ vision.py (Under Construction !!)

```

