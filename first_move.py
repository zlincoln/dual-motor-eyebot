"""
File: skidsteer_two_pwm_test.py
 
This code will test Raspberry Pi GPIO PWM on four GPIO
pins. The code test ran with L298N H-Bridge driver module connected.
 
Website:	www.bluetin.io
Date:		27/11/2017
"""
 
__author__ = "Mark Heywood"
__version__ = "0.1.0"
__license__ = "MIT"
 
from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep
import XboxController

 
#///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_DRIVE_LEFT = 12		# ENA - H-Bridge enable pin
FORWARD_LEFT_PIN = 14	# IN1 - Forward Drive
REVERSE_LEFT_PIN = 15	# IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_DRIVE_RIGHT = 13		# ENB - H-Bridge enable pin
FORWARD_RIGHT_PIN = 2	# IN1 - Forward Drive
REVERSE_RIGHT_PIN = 3	# IN2 - Reverse Drive
 
# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)
 
# Initialise objects for H-Bridge digital GPIO pins
forwardLeft = PWMOutputDevice(FORWARD_LEFT_PIN)
reverseLeft = PWMOutputDevice(REVERSE_LEFT_PIN)
forwardRight = PWMOutputDevice(FORWARD_RIGHT_PIN)
reverseRight = PWMOutputDevice(REVERSE_RIGHT_PIN)
 
def allStop():
	forwardLeft.value = False
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = False
	driveLeft.value = 0
	driveRight.value = 0
 
def forwardDrive():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 1.0
	driveRight.value = 1.0
 
def reverseDrive():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 1.0
	driveRight.value = 1.0
 
def spinLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 1.0
	driveRight.value = 1.0
 
def SpinRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 1.0
	driveRight.value = 1.0
 
def forwardTurnLeft():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.2
	driveRight.value = 0.8
 
def forwardTurnRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.8
	driveRight.value = 0.2
 
def reverseTurnLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.2
	driveRight.value = 0.8
 
def reverseTurnRight():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.8
	driveRight.value = 0.2
 
def main():
	allStop()
#	print('stop')
	forwardDrive()
	sleep(5)
	reverseDrive()
	sleep(5)
#	spinLeft()
#	sleep(1)
#	SpinRight()
#	sleep(1)
#	forwardTurnLeft()
#	sleep(2)
#	forwardTurnRight()
#	sleep(2)
#	reverseTurnLeft()
#	sleep(1)
#	reverseTurnRight()
#	sleep(1)
#	allStop()
 

def myCallBack(value):
	if value[0] == 0 and value[1] == 1:
		forwardDrive()
	elif value[0] == 0 and value[1] == -1:
		reverseDrive()
	elif value[0] == -1 and value[1] == 0:
		spinLeft()
	elif value[0] == 1 and value[1] == 0:
		SpinRight()
	elif value[0] == -1 and value[1] == 1:
		forwardTurnLeft()
	elif value[0] == 1 and value[1] == 1:
		forwardTurnRight()
	elif value[0] == -1 and value[1] == -1:
		reverseTurnLeft()
	elif value[0] == 1 and value[1] == -1:
		reverseTurnRight()
	else:
		allStop()

xboxCont = XboxController.XboxController()
xboxCont.setupControlCallback(17, myCallBack)

xboxCont.start()
